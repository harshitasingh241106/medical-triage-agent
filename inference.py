import os
from openai import OpenAI
from dotenv import load_dotenv
from environment import MedicalTriageEnv, Action

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "meta-llama/Llama-3.1-8B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN", "")

if not HF_TOKEN:
    print("Warning: HF_TOKEN not set. API calls will fail but environment will still run.")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN if HF_TOKEN else "dummy")

def run_task(task_number: int, episodes: int = 3):
    print(f"\n{'='*50}")
    labels = {
        1: "Department Routing (Easy)",
        2: "Department + Priority (Medium)",
        3: "Full Triage (Hard)",
        4: "Expert Triage Officer (Expert)"
    }
    print(f"TASK {task_number} — {labels[task_number]}")
    print('='*50)

    env = MedicalTriageEnv(task_number=task_number)
    total_score = 0.0

    for episode in range(episodes):
        obs = env.reset()
        print(f"\nEpisode {episode + 1}")
        print(f"Patient: {obs.patient_text[:70]}...")

        try:
            completion = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": obs.prompt}],
                max_tokens=300,
                temperature=0.1
            )
            agent_response = completion.choices[0].message.content or ""
        except Exception as e:
            print(f"API call failed: {e}")
            agent_response = "General"

        print(f"Agent response: {agent_response.strip()[:100]}")

        action = Action(response=agent_response)
        obs, reward, done, info = env.step(action)

        print(f"Score: {reward.score} | Feedback: {reward.feedback}")
        total_score += reward.score

    avg_score = total_score / episodes
    print(f"\nAverage score for Task {task_number}: {avg_score:.2f}")
    return avg_score


def main():
    print("Medical Triage Agent — Baseline Inference")
    print("Model:", MODEL_NAME)
    print("API:", API_BASE_URL)

    scores = {}
    scores["task1"] = run_task(task_number=1, episodes=3)
    scores["task2"] = run_task(task_number=2, episodes=3)
    scores["task3"] = run_task(task_number=3, episodes=3)
    scores["task4"] = run_task(task_number=4, episodes=3)

    print(f"\n{'='*50}")
    print("FINAL BASELINE SCORES")
    print('='*50)
    for task, score in scores.items():
        print(f"{task}: {score:.2f}")
    overall = sum(scores.values()) / len(scores)
    print(f"Overall average: {overall:.2f}")


if __name__ == "__main__":
    main()