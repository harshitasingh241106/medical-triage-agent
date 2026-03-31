PATIENTS = [
    # ─── Emergency ─────────────────────────────────────────────
    {
        "id": "P001",
        "text": "Patient is a 52-year-old male with sudden severe chest pain radiating to the left arm, sweating profusely, and difficulty breathing for the past 20 minutes.",
        "department": "Emergency",
        "priority": "Immediate",
        "action": "Call emergency team immediately, administer oxygen, prepare for ECG and cardiac monitoring.",
        "risk_flag": "High"
    },
    {
        "id": "P002",
        "text": "A 7-year-old child was brought in after a severe allergic reaction to peanuts. Face is swollen, having difficulty breathing, and skin shows hives.",
        "department": "Emergency",
        "priority": "Immediate",
        "action": "Administer epinephrine immediately, monitor airway, call allergy specialist.",
        "risk_flag": "High"
    },
    {
        "id": "P003",
        "text": "Patient is a 35-year-old female found unconscious at home. Family reports she has diabetes and may not have eaten today.",
        "department": "Emergency",
        "priority": "Immediate",
        "action": "Check blood glucose immediately, administer glucose if hypoglycemic, monitor vitals.",
        "risk_flag": "High"
    },
    {
        "id": "P004",
        "text": "68-year-old male with sudden severe headache he describes as the worst of his life, stiff neck, and sensitivity to light.",
        "department": "Emergency",
        "priority": "Immediate",
        "action": "Immediate CT scan and lumbar puncture to rule out subarachnoid hemorrhage or meningitis.",
        "risk_flag": "High"
    },
    {
        "id": "P005",
        "text": "45-year-old female with sudden weakness on the right side of her body, slurred speech, and facial drooping started 30 minutes ago.",
        "department": "Emergency",
        "priority": "Immediate",
        "action": "Activate stroke protocol immediately, CT scan, evaluate for tPA administration within window.",
        "risk_flag": "High"
    },
    {
        "id": "P006",
        "text": "22-year-old male brought in after a motorcycle accident with suspected head injury, loss of consciousness for 2 minutes, and bleeding laceration on forehead.",
        "department": "Emergency",
        "priority": "Immediate",
        "action": "Stabilize cervical spine, CT head scan, monitor neurological status closely.",
        "risk_flag": "High"
    },
    {
        "id": "P007",
        "text": "Patient is a 60-year-old with severe difficulty breathing, oxygen saturation at 82%, and blue tinge to lips.",
        "department": "Emergency",
        "priority": "Immediate",
        "action": "Administer high-flow oxygen immediately, prepare for intubation if needed, chest X-ray.",
        "risk_flag": "High"
    },
    {
        "id": "P008",
        "text": "30-year-old female with heavy vaginal bleeding, dizziness, and sharp lower abdominal pain. Last period was 8 weeks ago.",
        "department": "Emergency",
        "priority": "Immediate",
        "action": "Rule out ectopic pregnancy immediately, ultrasound, IV access and fluid resuscitation.",
        "risk_flag": "High"
    },
    {
        "id": "P009",
        "text": "55-year-old male with known heart failure presenting with sudden worsening shortness of breath, cannot lie flat, legs severely swollen.",
        "department": "Emergency",
        "priority": "Immediate",
        "action": "Administer diuretics, oxygen, monitor cardiac output, cardiology consult urgent.",
        "risk_flag": "High"
    },
    {
        "id": "P010",
        "text": "18-year-old male with severe asthma attack not responding to his inhaler, speaking in single words only due to breathlessness.",
        "department": "Emergency",
        "priority": "Immediate",
        "action": "Nebulized bronchodilators, systemic steroids, oxygen, prepare for possible intubation.",
        "risk_flag": "High"
    },

    # ─── General ───────────────────────────────────────────────
    {
        "id": "P011",
        "text": "28-year-old female with mild fever of 38.2C, sore throat, and fatigue for the past 3 days. No difficulty swallowing.",
        "department": "General",
        "priority": "Standard",
        "action": "Throat swab for strep, rest, hydration, paracetamol for fever if needed.",
        "risk_flag": "Low"
    },
    {
        "id": "P012",
        "text": "40-year-old male requesting a routine annual health checkup and blood pressure monitoring.",
        "department": "General",
        "priority": "Standard",
        "action": "Schedule full physical exam, blood panel, blood pressure monitoring.",
        "risk_flag": "Low"
    },
    {
        "id": "P013",
        "text": "32-year-old female with mild lower back pain for a week after lifting heavy boxes. No neurological symptoms.",
        "department": "General",
        "priority": "Standard",
        "action": "Rest, NSAIDs for pain relief, physiotherapy referral if not improving in 2 weeks.",
        "risk_flag": "Low"
    },
    {
        "id": "P014",
        "text": "55-year-old male with mild cough and cold symptoms for 4 days. No fever, no chest pain.",
        "department": "General",
        "priority": "Standard",
        "action": "Symptomatic treatment, rest, fluids. Return if symptoms worsen or persist beyond 10 days.",
        "risk_flag": "Low"
    },
    {
        "id": "P015",
        "text": "25-year-old female requesting contraceptive advice and prescription renewal.",
        "department": "General",
        "priority": "Standard",
        "action": "Review contraceptive history, blood pressure check, renew prescription if appropriate.",
        "risk_flag": "Low"
    },
    {
        "id": "P016",
        "text": "65-year-old female with mild knee pain worsening over 6 months, worse going up stairs.",
        "department": "General",
        "priority": "Standard",
        "action": "X-ray knee, consider physiotherapy, NSAIDs for pain, weight management advice.",
        "risk_flag": "Low"
    },
    {
        "id": "P017",
        "text": "38-year-old male with recurrent heartburn and acid reflux after meals for the past month.",
        "department": "General",
        "priority": "Standard",
        "action": "Lifestyle modifications, antacids, consider PPI therapy, follow up in 4 weeks.",
        "risk_flag": "Low"
    },
    {
        "id": "P018",
        "text": "50-year-old female requesting flu vaccination and advice on travel vaccines for upcoming trip.",
        "department": "General",
        "priority": "Standard",
        "action": "Administer flu vaccine, review travel destination requirements, prescribe as needed.",
        "risk_flag": "Low"
    },
    {
        "id": "P019",
        "text": "12-year-old child with mild rash on arms and legs, no fever, no breathing difficulty. Likely eczema flare.",
        "department": "General",
        "priority": "Standard",
        "action": "Topical corticosteroids, moisturizer, avoid known triggers, follow up in 2 weeks.",
        "risk_flag": "Low"
    },
    {
        "id": "P020",
        "text": "29-year-old male with mild anxiety about a mole on his back that has slightly changed color over 3 months.",
        "department": "General",
        "priority": "Urgent",
        "action": "Dermatoscopy assessment, photograph and measure lesion, refer to dermatology if suspicious.",
        "risk_flag": "Low"
    },

    # ─── Specialist ────────────────────────────────────────────
    {
        "id": "P021",
        "text": "45-year-old female with persistent joint pain and swelling in multiple joints, morning stiffness lasting over an hour, fatigue for 3 months.",
        "department": "Specialist",
        "priority": "Urgent",
        "action": "Rheumatology referral, RF and anti-CCP blood tests, consider early DMARDs.",
        "risk_flag": "Low"
    },
    {
        "id": "P022",
        "text": "60-year-old male with recent diagnosis of Type 2 diabetes requiring specialist management and insulin initiation.",
        "department": "Specialist",
        "priority": "Urgent",
        "action": "Endocrinology referral, HbA1c monitoring, diabetes education, dietitian referral.",
        "risk_flag": "Low"
    },
    {
        "id": "P023",
        "text": "35-year-old female with unexplained weight loss of 8kg over 2 months, night sweats, and enlarged lymph nodes in neck.",
        "department": "Specialist",
        "priority": "Urgent",
        "action": "Urgent oncology referral, CT scan, lymph node biopsy, full blood count.",
        "risk_flag": "High"
    },
    {
        "id": "P024",
        "text": "52-year-old male with worsening vision in right eye over 3 weeks, no pain, like a curtain coming down.",
        "department": "Specialist",
        "priority": "Urgent",
        "action": "Urgent ophthalmology referral, rule out retinal detachment, same day review.",
        "risk_flag": "High"
    },
    {
        "id": "P025",
        "text": "48-year-old female with recurrent episodes of rapid heartbeat, lasting 10-15 minutes, with dizziness.",
        "department": "Specialist",
        "priority": "Urgent",
        "action": "Cardiology referral, 24-hour Holter monitor, ECG, echo if indicated.",
        "risk_flag": "Low"
    },
    {
        "id": "P026",
        "text": "55-year-old male with difficulty swallowing solid foods progressively worsening over 6 weeks, unintentional weight loss.",
        "department": "Specialist",
        "priority": "Urgent",
        "action": "Urgent gastroenterology referral, endoscopy, rule out esophageal malignancy.",
        "risk_flag": "High"
    },
    {
        "id": "P027",
        "text": "40-year-old female with chronic migraine headaches occurring more than 15 days per month despite standard treatment.",
        "department": "Specialist",
        "priority": "Urgent",
        "action": "Neurology referral, preventive migraine therapy, review current medication overuse.",
        "risk_flag": "Low"
    },
    {
        "id": "P028",
        "text": "70-year-old male with progressive memory loss, confusion, and personality changes over 12 months.",
        "department": "Specialist",
        "priority": "Urgent",
        "action": "Neurology referral, cognitive assessment, MRI brain, rule out dementia or reversible causes.",
        "risk_flag": "Low"
    },
    {
        "id": "P029",
        "text": "33-year-old female with infertility concerns after trying to conceive for 18 months with no success.",
        "department": "Specialist",
        "priority": "Standard",
        "action": "Gynecology referral, hormonal panel, partner semen analysis, pelvic ultrasound.",
        "risk_flag": "Low"
    },
    {
        "id": "P030",
        "text": "58-year-old male with blood in urine for the past 2 weeks, no pain, no urinary symptoms.",
        "department": "Specialist",
        "priority": "Urgent",
        "action": "Urgent urology referral, cystoscopy, rule out bladder or kidney malignancy.",
        "risk_flag": "High"
    },

    # ─── Mental Health ──────────────────────────────────────────
    {
        "id": "P031",
        "text": "19-year-old female presenting with persistent low mood, loss of interest in activities, poor sleep, and feelings of worthlessness for 6 weeks.",
        "department": "Mental Health",
        "priority": "Urgent",
        "action": "Depression screening, refer to psychiatry or psychology, consider antidepressants, safety assessment.",
        "risk_flag": "Low"
    },
    {
        "id": "P032",
        "text": "25-year-old male brought by friend after expressing thoughts of suicide and giving away possessions.",
        "department": "Mental Health",
        "priority": "Immediate",
        "action": "Immediate psychiatric assessment, do not leave patient alone, consider inpatient admission.",
        "risk_flag": "High"
    },
    {
        "id": "P033",
        "text": "42-year-old female with severe panic attacks occurring multiple times daily, unable to leave home for 2 weeks.",
        "department": "Mental Health",
        "priority": "Urgent",
        "action": "Psychiatry referral, CBT therapy, consider short-term anxiolytics, safety plan.",
        "risk_flag": "Low"
    },
    {
        "id": "P034",
        "text": "35-year-old male with a history of bipolar disorder presenting with 5 days of no sleep, grandiose ideas, and reckless spending.",
        "department": "Mental Health",
        "priority": "Urgent",
        "action": "Psychiatry review, assess medication compliance, consider mood stabilizer adjustment or admission.",
        "risk_flag": "High"
    },
    {
        "id": "P035",
        "text": "16-year-old female referred by school counselor for suspected eating disorder, significant weight loss over 3 months.",
        "department": "Mental Health",
        "priority": "Urgent",
        "action": "Eating disorder assessment, dietitian referral, family therapy, monitor physical health closely.",
        "risk_flag": "High"
    },
    {
        "id": "P036",
        "text": "50-year-old male struggling with alcohol dependency, drinking over 20 units per day, requesting help to stop.",
        "department": "Mental Health",
        "priority": "Urgent",
        "action": "Addiction psychiatry referral, supervised detox program, thiamine supplementation, counseling.",
        "risk_flag": "High"
    },
    {
        "id": "P037",
        "text": "28-year-old female with work-related stress and mild anxiety, difficulty sleeping, but functioning normally.",
        "department": "Mental Health",
        "priority": "Standard",
        "action": "Counseling referral, sleep hygiene advice, stress management techniques, follow up in 4 weeks.",
        "risk_flag": "Low"
    },
    {
        "id": "P038",
        "text": "45-year-old male with PTSD following a road accident 6 months ago, recurring nightmares and hypervigilance.",
        "department": "Mental Health",
        "priority": "Urgent",
        "action": "Trauma-focused CBT referral, psychiatry assessment, consider SSRI therapy.",
        "risk_flag": "Low"
    },
    {
        "id": "P039",
        "text": "70-year-old female with increasing confusion, agitation at night, and suspected delirium following hip surgery.",
        "department": "Mental Health",
        "priority": "Urgent",
        "action": "Geriatric psychiatry consult, identify and treat underlying cause, reorientation strategies.",
        "risk_flag": "High"
    },
    {
        "id": "P040",
        "text": "22-year-old male with first episode of psychosis, hearing voices and believing people are following him for 2 weeks.",
        "department": "Mental Health",
        "priority": "Immediate",
        "action": "Urgent psychiatry assessment, consider antipsychotic medication, evaluate need for inpatient care.",
        "risk_flag": "High"
    },

    # ─── Mixed difficult cases ──────────────────────────────────
    {
        "id": "P041",
        "text": "48-year-old male with chest pain on exertion that resolves with rest, occurring for 2 weeks. No pain at rest currently.",
        "department": "Specialist",
        "priority": "Urgent",
        "action": "Cardiology referral, stress ECG, rule out stable angina, consider coronary angiography.",
        "risk_flag": "High"
    },
    {
        "id": "P042",
        "text": "62-year-old female with gradual onset confusion, weight gain, hair loss, and feeling cold all the time for 3 months.",
        "department": "Specialist",
        "priority": "Urgent",
        "action": "Thyroid function tests, endocrinology referral, thyroid replacement therapy if confirmed hypothyroid.",
        "risk_flag": "Low"
    },
    {
        "id": "P043",
        "text": "38-year-old male construction worker with deep laceration on forearm from a metal sheet, bleeding controlled with pressure.",
        "department": "Emergency",
        "priority": "Urgent",
        "action": "Wound assessment, suturing, tetanus prophylaxis, check neurovascular status of hand.",
        "risk_flag": "Low"
    },
    {
        "id": "P044",
        "text": "55-year-old female with new onset seizure at home, first ever, lasted 3 minutes, now confused and drowsy.",
        "department": "Emergency",
        "priority": "Immediate",
        "action": "CT brain, EEG referral, neurology consult, initiate seizure precautions.",
        "risk_flag": "High"
    },
    {
        "id": "P045",
        "text": "30-year-old female with severe nausea, vomiting, and diarrhea for 24 hours after eating at a restaurant. Unable to keep fluids down.",
        "department": "General",
        "priority": "Urgent",
        "action": "IV fluid rehydration, antiemetics, stool culture, monitor electrolytes.",
        "risk_flag": "Low"
    },
    {
        "id": "P046",
        "text": "14-year-old male with severe acne not responding to topical treatments for 6 months, affecting self-esteem significantly.",
        "department": "Specialist",
        "priority": "Standard",
        "action": "Dermatology referral, consider oral antibiotics or isotretinoin, mental health screening.",
        "risk_flag": "Low"
    },
    {
        "id": "P047",
        "text": "72-year-old female who fell at home, complaining of hip pain, unable to weight bear, leg appears shortened and rotated.",
        "department": "Emergency",
        "priority": "Immediate",
        "action": "X-ray hip, orthopaedic consult, pain management, prepare for likely surgical repair.",
        "risk_flag": "High"
    },
    {
        "id": "P048",
        "text": "26-year-old female with painful urination, frequent urge to urinate, and lower abdominal discomfort for 2 days.",
        "department": "General",
        "priority": "Standard",
        "action": "Urine dipstick and culture, antibiotics if UTI confirmed, increase fluid intake.",
        "risk_flag": "Low"
    },
    {
        "id": "P049",
        "text": "58-year-old male smoker with chronic cough producing blood-tinged sputum for 3 weeks, 5kg weight loss.",
        "department": "Specialist",
        "priority": "Urgent",
        "action": "Urgent chest X-ray, CT thorax, respiratory referral, rule out lung malignancy.",
        "risk_flag": "High"
    },
    {
        "id": "P050",
        "text": "33-year-old male with sudden onset severe testicular pain and swelling for 2 hours. Nausea and vomiting present.",
        "department": "Emergency",
        "priority": "Immediate",
        "action": "Urgent urology review, testicular ultrasound, surgical exploration if torsion suspected.",
        "risk_flag": "High"
    },
]