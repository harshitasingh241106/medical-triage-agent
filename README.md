---
title: Medical Triage Agent
emoji: 🏥
colorFrom: red
colorTo: blue
sdk: docker
pinned: false
tags:
  - openenv
  - medical
  - triage
---

# Medical Triage Agent — OpenEnv Environment

An OpenEnv environment where an AI agent reads real patient symptom reports
and must correctly triage them by department, priority level, risk, and recommended action.

## Why This Matters

Hospitals worldwide face critical triage bottlenecks. Incorrect or delayed triage
leads to preventable deaths. This environment simulates that challenge — training
and evaluating AI agents that can assist medical staff in routing patients correctly
under pressure.

## Tasks

| Task | Difficulty | What the Agent Must Do | Max Score |
|------|-----------|------------------------|-----------|
| Task 1 | Easy | Route patient to correct department | 1.0 |
| Task 2 | Medium | Route patient + classify priority level | 1.0 |
| Task 3 | Hard | Route + priority + recommend action | 1.0 |
| Task 4 | Expert | Route + priority + risk flag + reasoning + action | 1.0 |

## Departments

- **Emergency** — life-threatening conditions requiring immediate care
- **General** — routine conditions manageable by a GP
- **Specialist** — conditions requiring specialist referral
- **Mental Health** — psychiatric and psychological conditions

## Priority Levels

- **Immediate** — life-threatening, act within minutes
- **Urgent** — serious, act within hours
- **Standard** — non-urgent, routine appointment

## Baseline Scores

Tested with `meta-llama/Llama-3.1-8B-Instruct` via Hugging Face router:

| Task 1 — Department Routing (Easy) | 0.99 |
| Task 2 — Department + Priority (Medium) | 0.99 |
| Task 3 — Full Triage (Hard) | ~0.6–0.7 |
| Task 4 — Expert Triage Officer (Expert) | ~0.5–0.8 |
| **Overall Average** | **~0.7–0.8** |

> Note: Scores are clipped to the range (0, 1) to comply with evaluation requirements.

## Observation Space

| Field | Type | Description |
|-------|------|-------------|
| patient_id | string | Unique patient identifier |
| patient_text | string | Patient symptom report |
| task_number | integer | Which task (1, 2, 3, or 4) |
| prompt | string | Formatted prompt for the agent |
| steps_taken | integer | Number of steps taken |
| done | boolean | Whether episode is complete |

## Action Space

| Field | Type | Description |
|-------|------|-------------|
| response | string | The agent's triage decision |

## Reward

- Scores range from 0.0 to 1.0
- Partial credit given for partially correct answers
- Task 1: binary (correct department = 1.0)
- Task 2: 0.5 per correct element (department + priority)
- Task 3: 0.3 + 0.3 + 0.4 (department + priority + action quality)
- Task 4: 0.25 + 0.25 + 0.20 + 0.30 (department + priority + risk + action)

## Setup
```bash
git clone https://github.com/harshitasingh241106/medical-triage-agent.git
cd medical-triage-agent
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Running the API
```bash
uvicorn app:app --reload
```

Visit http://localhost:7860/docs for the interactive API explorer.

## Running the Inference Script

Create a `.env` file with:
```
API_BASE_URL=https://router.huggingface.co/v1
MODEL_NAME=meta-llama/Llama-3.1-8B-Instruct
HF_TOKEN=your_hugging_face_token
```

Then run:
```bash
python inference.py
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| / | GET | Environment info |
| /health | GET | Health check |
| /reset | POST | Start new episode |
| /step | POST | Submit agent action |
| /state | GET | Current environment state |
| /tasks | GET | List all tasks |

## Docker
```bash
docker build -t medical-triage-agent .
docker run -p 7860:7860 medical-triage-agent
```