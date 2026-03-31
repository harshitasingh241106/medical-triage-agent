import random
from pydantic import BaseModel
from data.patients import PATIENTS
from tasks.task1 import grade_task1, TASK1_DESCRIPTION
from tasks.task2 import grade_task2, TASK2_DESCRIPTION
from tasks.task3 import grade_task3, TASK3_DESCRIPTION
from tasks.task4 import grade_task4, TASK4_DESCRIPTION


class Observation(BaseModel):
    patient_id: str
    patient_text: str
    task_number: int
    prompt: str
    steps_taken: int
    done: bool

class Action(BaseModel):
    response: str

class Reward(BaseModel):
    score: float
    feedback: str


class MedicalTriageEnv:
    def __init__(self, task_number: int = 1):
        if task_number not in [1, 2, 3, 4]:
            raise ValueError("task_number must be 1, 2, 3, or 4")
        self.task_number = task_number
        self.patients = PATIENTS
        self.current_patient = None
        self.steps_taken = 0
        self.done = False

    def reset(self) -> Observation:
        self.current_patient = random.choice(self.patients)
        self.steps_taken = 0
        self.done = False
        return Observation(
            patient_id=self.current_patient["id"],
            patient_text=self.current_patient["text"],
            task_number=self.task_number,
            prompt=self._get_prompt(),
            steps_taken=self.steps_taken,
            done=self.done
        )

    def step(self, action: Action):
        if self.done:
            raise RuntimeError("Episode is done. Please call reset() first.")

        reward = self._grade(action.response)
        self.steps_taken += 1
        self.done = True

        observation = Observation(
            patient_id=self.current_patient["id"],
            patient_text=self.current_patient["text"],
            task_number=self.task_number,
            prompt=self._get_prompt(),
            steps_taken=self.steps_taken,
            done=self.done
        )

        info = {
            "patient_id": self.current_patient["id"],
            "task_number": self.task_number,
            "steps_taken": self.steps_taken
        }

        return observation, reward, self.done, info

    def state(self) -> dict:
        return {
            "task_number": self.task_number,
            "current_patient_id": self.current_patient["id"] if self.current_patient else None,
            "steps_taken": self.steps_taken,
            "done": self.done,
            "total_patients": len(self.patients)
        }

    def _get_prompt(self) -> str:
        prompts = {
            1: TASK1_DESCRIPTION,
            2: TASK2_DESCRIPTION,
            3: TASK3_DESCRIPTION,
            4: TASK4_DESCRIPTION,
        }
        return prompts[self.task_number].format(
            patient_text=self.current_patient["text"]
        )

    def _grade(self, agent_response: str) -> Reward:
        patient_id = self.current_patient["id"]

        if self.task_number == 1:
            score = grade_task1(patient_id, agent_response)
            feedback = "Correct department!" if score == 1.0 else "Wrong department."

        elif self.task_number == 2:
            score = grade_task2(patient_id, agent_response)
            if score == 1.0:
                feedback = "Correct department and priority!"
            elif score == 0.5:
                feedback = "Got one of department/priority correct."
            else:
                feedback = "Both department and priority wrong."

        elif self.task_number == 3:
            score = grade_task3(patient_id, agent_response)
            if score >= 0.8:
                feedback = "Excellent! All elements correct."
            elif score >= 0.5:
                feedback = "Partial credit. Some elements correct."
            else:
                feedback = "Needs improvement."

        else:
            score = grade_task4(patient_id, agent_response)
            if score >= 0.8:
                feedback = "Excellent! All elements including risk flag correct."
            elif score >= 0.5:
                feedback = "Partial credit. Some elements correct."
            else:
                feedback = "Needs improvement across all elements."

        return Reward(score=score, feedback=feedback)