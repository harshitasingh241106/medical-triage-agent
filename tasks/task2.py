from data.patients import PATIENTS

TASK2_DESCRIPTION = """
You are a medical triage nurse.
Read the patient report below and reply in exactly this format:
Department: <department>
Priority: <priority>

For Department choose from: Emergency, General, Specialist, Mental Health
For Priority choose from: Immediate, Urgent, Standard

Patient Report: {patient_text}

Reply in the exact format shown. No extra explanation.
"""

def get_task2_patients():
    return PATIENTS

def grade_task2(patient_id, agent_answer):
    correct = None
    for patient in PATIENTS:
        if patient["id"] == patient_id:
            correct = patient
            break

    if correct is None:
        return 0.0

    score = 0.0
    agent_lower = agent_answer.lower()

    if correct["department"].lower() in agent_lower:
        score += 0.5
    if correct["priority"].lower() in agent_lower:
        score += 0.5

    return score