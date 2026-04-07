import os
from openai import OpenAI
from dotenv import load_dotenv
from environment import MedicalTriageEnv, Action

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "meta-llama/Llama-3.1-8B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN", "")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN if HF_TOKEN else "dummy")

MAX_STEPS = 1   # triage is single-step task
SUCCESS_THRESHOLD = 0.5


def log_start(task, env, model):
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(step, action, reward, done, error=None):
    error_val = error if error else "null"
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error={error_val}",
        flush=True
    )


def log_end(success, steps, score, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}",
        flush=True
    )


def run_task(task_number: int):
    TASK_NAME = f"triage-task-{task_number}"
    BENCHMARK = "medical_triage"

    env = MedicalTriageEnv(task_number=task_number)

    log_start(TASK_NAME, BENCHMARK, MODEL_NAME)

    rewards = []
    steps_taken = 0
    score = 0.0
    success = False

    try:
        obs = env.reset()

        try:
            completion = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": obs.prompt}],
                max_tokens=200,
                temperature=0.1
            )
            agent_response = completion.choices[0].message.content or ""
        except Exception as e:
            agent_response = "General"
            error = str(e)
        else:
            error = None

        action = Action(response=agent_response)
        obs, reward_obj, done, info = env.step(action)

        reward = float(reward_obj.score)
        rewards.append(reward)
        steps_taken = 1

        log_step(
            step=1,
            action=agent_response.strip().replace("\n", " "),
            reward=reward,
            done=done,
            error=error
        )

        score = reward  # already normalized [0,1]
        success = score >= SUCCESS_THRESHOLD

    finally:
        try:
            env.close()
        except:
            pass

        log_end(success, steps_taken, score, rewards)


def main():
    for task in [1, 2, 3, 4]:
        run_task(task)


if __name__ == "__main__":
    main()