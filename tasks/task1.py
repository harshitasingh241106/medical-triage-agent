from data.patients import PATIENTS

TASK1_DESCRIPTION = """
You are a medical triage nurse.
Read the patient report below and reply with ONLY one word — the department name.
Choose from exactly these four options: Emergency, General, Specialist, Mental Health

Patient Report: {patient_text}

Reply with only the department name. No explanation.
"""

def get_task1_patients():
    return PATIENTS

def grade_task1(patient_id, agent_answer):
    correct = None
    for patient in PATIENTS:
        if patient["id"] == patient_id:
            correct = patient
            break

    if correct is None:
        return 0.0

    agent_answer = agent_answer.strip().lower()
    correct_department = correct["department"].lower()

    if agent_answer == correct_department:
        return 1.0
    return 0.0