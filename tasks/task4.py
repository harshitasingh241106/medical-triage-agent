from data.patients import PATIENTS

TASK4_DESCRIPTION = """
You are a senior medical triage officer.
Read the patient report below and reply in exactly this format:
Department: <department>
Priority: <priority>
Risk: <High or Low>
Reasoning: <one sentence explaining your triage decision>
Action: <recommended immediate action in 2-3 sentences>

For Department choose from: Emergency, General, Specialist, Mental Health
For Priority choose from: Immediate, Urgent, Standard
For Risk: High if patient faces life-threatening or serious risk, Low otherwise.

Patient Report: {patient_text}

Reply in the exact format shown. No extra explanation.
"""

def get_task4_patients():
    return PATIENTS

def grade_task4(patient_id, agent_answer):
    correct = None
    for patient in PATIENTS:
        if patient["id"] == patient_id:
            correct = patient
            break

    if correct is None:
        return 0.0

    score = 0.0
    agent_lower = agent_answer.lower()

    # Department — 0.25
    if correct["department"].lower() in agent_lower:
        score += 0.25

    # Priority — 0.25
    if correct["priority"].lower() in agent_lower:
        score += 0.25

    # Risk flag — 0.20
    risk_line = ""
    for line in agent_answer.split("\n"):
        if line.lower().startswith("risk:"):
            risk_line = line.lower()
            break

    if risk_line:
        agent_risk = "high" in risk_line
        correct_risk = correct["risk_flag"] == "High"
        if agent_risk == correct_risk:
            score += 0.20

    # Action quality — 0.30
    action_part = ""
    for line in agent_answer.split("\n"):
        if line.lower().startswith("action:"):
            action_part = line.replace("Action:", "").replace("action:", "").strip().lower()
            break

    if action_part:
        stop_words = {"the", "a", "an", "is", "are", "we", "you", "your",
                      "our", "in", "on", "at", "to", "for", "of", "and",
                      "or", "it", "this", "that", "will", "can", "if",
                      "please", "with", "from", "have", "has", "be", "as"}

        correct_keywords = [
            word for word in correct["action"].lower().split()
            if word not in stop_words and len(word) > 3
        ]

        if correct_keywords:
            matched = sum(1 for word in correct_keywords if word in action_part)
            score += 0.30 * (matched / len(correct_keywords))

    return round(score, 2)