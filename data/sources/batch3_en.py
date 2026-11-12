"""Batch 3 (English): 13 long, realistic made-up pairs, written to look like real hospital
paperwork (headers, record numbers, codes, jargon, fine print). All names, clinics, IDs and
numbers are invented (phones use 555-01xx; websites use example.org). Approved with no changes by a CCC-SLP (anonymous) on 2026-11-12.

Run:  python data/sources/batch3_en.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from batch2_helpers import B, C, CR, P, PH, S, T, mark_reviewed, pair, write  # noqa: E402,F401

PAIRS = [
# 1 ── After-visit summary, primary care ────────────────────────────────────────
pair("avs-primary-care-en-001", "en", "visit_summary", "After visit summary (made-up example)",
     "AFTER VISIT SUMMARY — Maple Ridge Family Medicine\n"
     "Patient: Harold Jenkins | DOB: 05/02/1951 | MRN: 00739215 | Visit date: 01/12/2027\n"
     "Provider: Dr. Karen Liu, MD\n"
     "Reason for visit: Follow-up hypertension; history of CVA (2026).\n"
     "Vitals: BP 148/92 | HR 76 | Wt 189 lb\n"
     "Diagnoses addressed: Essential hypertension (I10); Personal history of cerebral infarction (Z86.73).\n"
     "MEDICATION CHANGES: INCREASE amlodipine from 5 mg to 10 mg by mouth once daily. Continue all other medications as "
     "previously prescribed.\n"
     "ORDERS: Basic metabolic panel. Have blood drawn at the lab within 1 week.\n"
     "INSTRUCTIONS: Limit sodium to less than 2,000 mg per day. Check BP at home 3 times a week and record readings.\n"
     "NEXT APPOINTMENT: Tuesday, February 9, 2027 at 10:20 a.m. with Dr. Karen Liu.\n"
     "MyChart: view your test results at www.example.org/mychart.\n"
     "This summary is provided for your records. Questions: (919) 555-0123. In an emergency, call 911.",
     "Your visit today",
     [P("Your visit today",
        T("For: **Harold Jenkins**", "person"),
        T("You saw **Dr. Karen Liu**.", "doctor"),
        T("At **Maple Ridge Family Medicine**.", "clinic")),
      P("Why you came",
        T("Your **blood pressure** is **high**.", "blood pressure"),
        T("You had a **stroke** in **2026**.", "brain"),
        T("Your blood pressure today: **148/92**", "blood pressure")),
      P("Medicine change",
        T("**Amlodipine**: take **more**.", "pill"),
        T("Old dose: **5 mg**", "pill"),
        T("New dose: **10 mg**", "pill"),
        T("Take it **once** a day, by **mouth**.", "calendar")),
      P("Other medicines",
        T("Keep taking your **other medicines**.", "pills"),
        T("**No changes**.", "check mark")),
      P("Blood test",
        T("Get a **blood test** at the **lab**.", "blood test"),
        T("Go within **1 week**.", "calendar")),
      P("Less salt",
        T("Eat **less salt**.", "salt"),
        T("Less than **2,000 mg** of **sodium** a day.", "salt")),
      P("Check your blood pressure",
        S("Check it at **home**.", "blood pressure"),
        S("**3 times** a week.", "calendar"),
        S("**Write down** the numbers.", "write")),
      P("Next visit",
        T("**Tuesday, February 9, 2027**", "calendar"),
        T("**10:20 a.m.**", "clock"),
        T("With **Dr. Karen Liu**.", "doctor")),
      P("Your test results",
        T("See results online: **www.example.org/mychart**", "computer")),
      P("Questions?",
        PH("Phone: (919) 555-0123"),
        CR("Emergency? Call 911"))],
     ["'Hypertension' became 'blood pressure is high'; 'CVA' became 'stroke'."],
     omitted=["DOB 05/02/1951: not needed by the reader", "MRN 00739215: record number",
              "Visit date 01/12/2027: today's date, already past", "HR 76 and Wt 189 lb: visit measurements, no action",
              "Diagnosis codes I10 and Z86.73: billing codes"]),

# 2 ── Hospital discharge packet after stroke ───────────────────────────────────
pair("discharge-packet-en-002", "en", "discharge", "Hospital discharge instructions (made-up example)",
     "DISCHARGE INSTRUCTIONS — Carolina Valley Medical Center, Stroke Unit (4 West)\n"
     "Patient: Dolores Pruitt | DOB: 11/23/1946 | MRN: 01182044 | Admit: 01/03/2027 | Discharge: 01/08/2027\n"
     "Principal diagnosis: Acute ischemic stroke, left MCA territory, s/p IV alteplase. Secondary: Atrial fibrillation (new "
     "diagnosis); oropharyngeal dysphagia.\n"
     "Hospital course: Patient presented with acute expressive aphasia and right hemiparesis. MRI confirmed left MCA infarct.\n"
     "DISCHARGE MEDICATIONS: START apixaban 5 mg by mouth twice daily (blood thinner for atrial fibrillation). START "
     "atorvastatin 80 mg by mouth at bedtime. STOP aspirin 81 mg. CONTINUE metoprolol 25 mg by mouth twice daily.\n"
     "DIET: Mechanical soft solids, thin liquids. Sit upright for all meals and for 30 minutes after.\n"
     "ACTIVITY: Walk with your rolling walker and a family member at all times until cleared by physical therapy.\n"
     "FOLLOW-UP: Stroke Clinic, Dr. Ravi Patel, Thursday, January 21, 2027 at 1:00 p.m. Outpatient speech therapy: the "
     "clinic will call you to schedule. Cardiology: call (919) 555-0124 to schedule within 2 weeks.\n"
     "WHEN TO CALL 911: new or worsening weakness, trouble speaking, facial droop, vision loss, severe headache, or "
     "bleeding that will not stop.\n"
     "Questions after discharge: Stroke Nurse Line (919) 555-0125, available 24 hours a day.",
     "Going home after your stroke",
     [P("You had a stroke",
        T("For: **Dolores Pruitt**", "person"),
        T("You had a **stroke**.", "brain"),
        T("Blood was **blocked** on the **left side** of your brain.", "brain"),
        T("This makes **talking** and moving your **right side** hard.", "weak arm")),
      P("Two other problems",
        T("You have **atrial fibrillation**.", "heart"),
        T("Your **heart** beats **unevenly**.", "heartbeat"),
        T("You also have trouble **swallowing**.", "swallow")),
      P("New medicine: apixaban",
        T("**Start** apixaban **5 mg**.", "pill"),
        T("**Twice** a day, by mouth.", "calendar"),
        T("It is a **blood thinner**.", "blood")),
      P("New medicine: atorvastatin",
        T("**Start** atorvastatin **80 mg**.", "pill"),
        T("By mouth at **bedtime**.", "bed")),
      P("Stop this medicine",
        T("**Stop** aspirin **81 mg**.", "stop")),
      P("Keep taking",
        T("**Keep taking** metoprolol **25 mg**.", "pill"),
        T("**Twice** a day, by mouth.", "calendar")),
      P("Eating and drinking",
        T("Eat **soft** foods (mechanical soft).", "soft food"),
        T("**Thin** liquids are okay.", "glass of water"),
        T("**Sit up** to eat.", "sit at table"),
        T("Stay sitting up **30 minutes** after.", "clock")),
      P("Walking",
        T("Use your **rolling walker**.", "walker"),
        T("Have a **family member** with you.", "family"),
        T("**Every time**, until **physical therapy** says okay.", "physical therapist")),
      P("Stroke Clinic visit",
        T("See **Dr. Ravi Patel**.", "doctor"),
        T("**Thursday, January 21, 2027**", "calendar"),
        T("**1:00 p.m.**", "clock")),
      P("Other visits",
        T("**Speech therapy** will **call you**.", "speech therapist"),
        T("**Cardiology** (heart doctor): **call** within **2 weeks**.", "heart"),
        PH("Cardiology: (919) 555-0124")),
      P("Call 911",
        T("New or worse **weakness**?", "weak arm"),
        T("Trouble **speaking**? **Face** drooping?", "face"),
        T("Can't **see**? Bad **headache**? **Bleeding** that won't stop?", "headache"),
        CR("Call 911")),
      P("Questions?",
        T("**Stroke Nurse Line**, **24 hours** a day.", "nurse"),
        PH("Stroke Nurse Line: (919) 555-0125"))],
     ["'Atrial fibrillation' is kept by name with a plain explanation ('heart beats unevenly'). Please check.",
      "'Cardiology (heart doctor)' adds a plain explanation of the word."],
     omitted=["DOB 11/23/1946: not needed by the reader", "MRN 01182044: record number",
              "Admit 01/03/2027 and Discharge 01/08/2027: past dates",
              "Stroke Unit (4 West): hospital unit name", "IV alteplase and MRI details: hospital course, no action"]),

# 3 ── Medication guide: apixaban ───────────────────────────────────────────────
pair("medguide-apixaban-en-001", "en", "medication", "Medication guide: apixaban (made-up example, not the official FDA guide)",
     "MEDICATION GUIDE — Apixaban (Eliquis) Tablets\n"
     "Read this Medication Guide before you start taking apixaban and each time you get a refill.\n"
     "What is the most important information I should know about apixaban?\n"
     "• Do not stop taking apixaban without talking to the doctor who prescribes it. Stopping increases your risk of stroke.\n"
     "• Apixaban can cause serious bleeding, which may lead to death. You may bruise more easily, and bleeding may take "
     "longer to stop.\n"
     "Get medical help right away if you have: unexpected or heavy bleeding; red, pink, or brown urine; red or black "
     "stools that look like tar; coughing up blood or vomiting blood.\n"
     "How should I take apixaban? Take apixaban exactly as prescribed, 2 times every day, with or without food. If you miss "
     "a dose, take it as soon as you remember on the same day, then go back to your regular schedule. Do not take 2 doses "
     "at the same time.\n"
     "Tell all your doctors and dentists that you take apixaban before any surgery or procedure.\n"
     "Distributed by: Example Pharma, Inc. Revised: 03/2026. For more information, call 1-800-555-0126.",
     "Your medicine: apixaban",
     [P("Your medicine: apixaban",
        T("Your medicine is **apixaban** (**Eliquis**).", "pill"),
        T("Read this **guide** at **every refill**.", "read")),
      P("Most important",
        T("**Do not stop** apixaban on your own.", "stop"),
        T("**Talk** to your **doctor** first.", "doctor"),
        T("Stopping can cause a **stroke**.", "brain")),
      P("Bleeding",
        T("Apixaban can cause **bleeding**.", "blood"),
        T("It can be **serious**. It can even cause **death**.", "warning"),
        T("You may **bruise** more **easily**.", "bruise"),
        T("Bleeding may take **longer** to stop.", "clock")),
      P("Get medical help right away",
        T("**Heavy** or **unexpected** bleeding?", "blood"),
        T("**Red**, pink or brown **urine**?", "toilet"),
        T("**Red** or **black** stools, like **tar**?", "toilet"),
        T("**Coughing** or **vomiting** blood?", "cough")),
      P("How to take it",
        T("Take it **2 times** every day.", "calendar"),
        T("With or without **food**.", "meal"),
        T("Take it **exactly** as your doctor said.", "doctor")),
      P("Missed a dose?",
        S("Take it when you **remember**, the **same day**.", "clock"),
        S("Then go back to your **usual times**.", "calendar"),
        T("**Never** take **2 doses** at once.", "no")),
      P("Before surgery",
        T("Tell **all** your **doctors** and **dentists**.", "dentist"),
        T("Say you take **apixaban**.", "pill"),
        T("Do this **before** any **surgery** or **procedure**.", "surgery")),
      P("More information",
        PH("Call 1-800-555-0126"))],
     ["This is a made-up guide in the style of an FDA Medication Guide; it is not the official one."],
     omitted=["Distributed by Example Pharma, Inc.; Revised 03/2026: publisher details"]),

# 4 ── Speech therapy plan of care ──────────────────────────────────────────────
pair("plan-of-care-slp-en-001", "en", "therapy_plan", "Speech therapy plan of care (made-up example)",
     "OUTPATIENT SPEECH-LANGUAGE PATHOLOGY PLAN OF CARE\n"
     "Piedmont Speech Clinic, 1420 Duke Street, Suite 2\n"
     "Patient: Marcus Bell | DOB: 08/30/1962 | Medicare ID: 1EG4-TE5-MK73 | Referring physician: Dr. Ravi Patel | "
     "Onset: 12/14/2026\n"
     "Treatment diagnoses: Aphasia following cerebral infarction (I69.320); dysarthria (R47.1).\n"
     "LONG-TERM GOALS (90 days): (1) Patient will produce 3-4 word phrases to express wants and needs with 80% accuracy "
     "given minimal cues. (2) Patient will follow 2-step commands with 90% accuracy. (3) Patient and spouse will "
     "independently use a written choice strategy during conversation.\n"
     "FREQUENCY/DURATION: 2 times per week for 12 weeks.\n"
     "PLAN: Treatment will include word retrieval therapy, script training, and caregiver education.\n"
     "CERTIFICATION PERIOD: 01/11/2027 to 04/10/2027. I certify the need for these services furnished under this plan of "
     "treatment. Physician signature: ____________ Date: ____________\n"
     "Therapist: Jordan Ellis, M.S., CCC-SLP",
     "Your speech therapy plan",
     [P("Your speech therapy plan",
        T("For: **Marcus Bell**", "person"),
        T("Your therapist: **Jordan Ellis, M.S., CCC-SLP**", "speech therapist"),
        T("Sent by **Dr. Ravi Patel**.", "doctor"),
        T("At **Piedmont Speech Clinic**.", "clinic")),
      P("Where",
        T("**1420 Duke Street, Suite 2**", "map")),
      P("Why you come",
        T("You have **aphasia** from a **stroke**.", "brain"),
        T("Your speech muscles are **weak** (**dysarthria**).", "mouth")),
      P("Goal 1",
        T("Say **3-4 word** phrases.", "talk"),
        T("To ask for what you **want** and **need**.", "request"),
        T("Right **80%** of the time, with a **little help**.", "target")),
      P("Goal 2",
        T("Follow **2-step** directions.", "steps"),
        T("Right **90%** of the time.", "target")),
      P("Goal 3",
        T("You and your **spouse** use **written choices**.", "write"),
        T("To help you **talk** together, on your **own**.", "conversation")),
      P("How often",
        T("**2 times** a week.", "calendar"),
        T("For **12 weeks**.", "calendar"),
        T("Goals are for **90 days**.", "target")),
      P("What you will do",
        T("Practice **finding words**.", "search"),
        T("Practice **scripts**.", "script"),
        T("Your **family** learns how to **help**.", "family")),
      P("Plan dates",
        T("**01/11/2027** to **04/10/2027**", "calendar"))],
     ["Goal wording was simplified ('with minimal cues' -> 'with a little help'). Please check the goals still match."],
     omitted=["DOB 08/30/1962: not needed by the reader", "Medicare ID 1EG4-TE5-MK73: insurance number",
              "Onset 12/14/2026: past date", "Diagnosis codes I69.320 and R47.1: billing codes",
              "Physician certification statement and signature lines: for the doctor, not the patient"]),

# 5 ── CT angiogram with contrast ───────────────────────────────────────────────
pair("procedure-cta-en-001", "en", "procedure", "CT angiography preparation (made-up example)",
     "CT ANGIOGRAPHY (CTA) HEAD AND NECK WITH IV CONTRAST — PATIENT PREPARATION\n"
     "Exam: Wednesday, February 3, 2027, 7:30 a.m. Arrival: 7:00 a.m., Radiology Check-In, Carolina Valley Medical Center, "
     "Main Building, Ground Floor.\n"
     "BEFORE YOUR EXAM: Do not eat solid food for 4 hours before your exam. You may drink clear liquids up to 1 hour "
     "before. Take your usual medications with sips of water. If you take metformin, do not take it for 48 hours after the "
     "exam unless your provider tells you otherwise.\n"
     "Tell us before your exam if you: have had an allergic reaction to contrast dye or iodine; have kidney disease; are "
     "pregnant or could be pregnant. A blood test for kidney function (creatinine) may be needed before the exam.\n"
     "DURING THE EXAM: An IV will be placed in your arm. You may feel warm or have a metallic taste when the contrast is "
     "injected; this is normal and passes quickly. The scan takes about 10 minutes.\n"
     "AFTER THE EXAM: Drink extra water for the rest of the day.\n"
     "To reschedule, call Central Scheduling at (919) 555-0128.",
     "Your CT scan",
     [P("Your CT scan",
        T("You will have a **CT scan**.", "ct scan"),
        T("Of your **head** and **neck**.", "head"),
        T("It shows your **blood vessels**.", "blood vessel"),
        T("You get **contrast dye** through an **IV**.", "injection")),
      P("When",
        T("**Wednesday, February 3, 2027**", "calendar"),
        T("Scan at **7:30 a.m.**", "clock"),
        T("**Arrive** at **7:00 a.m.**", "clock")),
      P("Where",
        T("**Carolina Valley Medical Center**", "hospital"),
        T("**Main Building**, **Ground Floor**", "building"),
        T("Go to **Radiology Check-In**.", "front desk")),
      P("Food and drink before",
        T("**No solid food** for **4 hours** before.", "no food"),
        T("**Clear liquids** are okay until **1 hour** before.", "glass of water"),
        T("Take your **usual medicines** with sips of **water**.", "pill")),
      P("Do you take metformin?",
        T("**Do not take** metformin for **48 hours** after the scan.", "no pill"),
        T("Unless your **provider** says something else.", "doctor")),
      P("Tell us first",
        T("Allergic to **contrast dye** or **iodine**?", "allergy"),
        T("**Kidney disease**?", "kidney"),
        T("**Pregnant**, or could be?", "pregnant"),
        T("**Tell us** before the scan.", "talk")),
      P("Blood test",
        T("You may need a **blood test** first.", "blood test"),
        T("It checks your **kidneys**.", "kidney")),
      P("During the scan",
        T("An **IV** goes in your **arm**.", "injection"),
        T("You may feel **warm** or taste **metal**.", "warm"),
        T("This is **normal**. It goes away **fast**.", "check mark"),
        T("The scan takes about **10 minutes**.", "clock")),
      P("After the scan",
        T("Drink **extra water** the rest of the **day**.", "glass of water")),
      P("Change your visit",
        T("Call **Central Scheduling**.", "phone"),
        PH("Phone: (919) 555-0128"))],
     ["'CT angiography' explained as 'CT scan that shows your blood vessels'. 'Creatinine' not named."]),

# 6 ── Discharge medication list ────────────────────────────────────────────────
pair("medication-list-en-001", "en", "medication", "Discharge medication list (made-up example)",
     "MEDICATION RECONCILIATION — DISCHARGE MEDICATION LIST\n"
     "Patient: Walter Simmons | Prepared by: Angela Cho, PharmD | Allergies: Penicillin (rash)\n"
     "STOP taking these medications: Lisinopril 20 mg tablet (replaced by losartan). Ibuprofen 200 mg tablet as needed "
     "(increases bleeding risk with your new medication).\n"
     "START taking these medications: Losartan 50 mg tablet: take 1 tablet by mouth once daily in the morning. Clopidogrel "
     "75 mg tablet: take 1 tablet by mouth once daily.\n"
     "CHANGE: Atorvastatin: NEW DOSE 40 mg at bedtime (was 20 mg).\n"
     "CONTINUE without changes: Levothyroxine 50 mcg: take 1 tablet by mouth every morning on an empty stomach.\n"
     "For pain, you may use acetaminophen 500 mg, up to 2 tablets every 6 hours as needed. Do not take more than 3,000 mg "
     "in 24 hours.\n"
     "Bring this list to all appointments. Questions: Pharmacy Discharge Line (919) 555-0129.",
     "Your medicine list",
     [P("Your medicine list",
        T("For: **Walter Simmons**", "person"),
        T("From your **pharmacist**, **Angela Cho, PharmD**.", "pharmacist"),
        T("**Allergy**: penicillin (**rash**).", "allergy")),
      P("Stop: lisinopril",
        T("**Stop** lisinopril **20 mg**.", "stop"),
        T("**Losartan** takes its place.", "swap")),
      P("Stop: ibuprofen",
        T("**Stop** ibuprofen **200 mg**.", "stop"),
        T("It can cause **bleeding** with your **new medicine**.", "blood")),
      P("Start: losartan",
        T("**Start** losartan **50 mg**.", "pill"),
        T("Take **1 tablet** by mouth.", "pill"),
        T("**Once** a day, in the **morning**.", "sunrise")),
      P("Start: clopidogrel",
        T("**Start** clopidogrel **75 mg**.", "pill"),
        T("Take **1 tablet** by mouth.", "pill"),
        T("**Once** a day.", "calendar")),
      P("Change: atorvastatin",
        T("Atorvastatin has a **new dose**.", "pill"),
        T("New: **40 mg** at **bedtime**.", "bed"),
        T("Old: **20 mg**.", "pill")),
      P("Keep taking: levothyroxine",
        T("Keep taking levothyroxine **50 mcg**.", "pill"),
        T("Take **1 tablet** by mouth every **morning**.", "sunrise"),
        T("On an **empty stomach**.", "stomach")),
      P("For pain",
        T("You may take **acetaminophen 500 mg**.", "pill"),
        T("Up to **2 tablets** every **6 hours**, if needed.", "clock"),
        T("**No more** than **3,000 mg** in **24 hours**.", "warning")),
      P("Bring this list",
        T("Bring this **list** to **every visit**.", "list"),
        PH("Pharmacy: (919) 555-0129"))]),

# 7 ── Home health welcome letter ───────────────────────────────────────────────
pair("home-health-welcome-en-001", "en", "home_health", "Home health welcome letter (made-up example)",
     "Welcome to Bright Path Home Health\n"
     "Your home health services were ordered by Dr. Karen Liu after your hospital stay.\n"
     "YOUR CARE TEAM: Registered Nurse (RN): Tasha Greene. Visits 2 times per week for 4 weeks to check vital signs, review "
     "medications, and teach about stroke prevention. Physical Therapist (PT): Daniel Park. Visits 3 times per week for "
     "6 weeks. Speech-Language Pathologist (SLP): Maria Ochoa. Visits 2 times per week for 6 weeks. Home Health Aide: help "
     "with bathing 2 times per week.\n"
     "Your first nurse visit is scheduled for Monday, January 11, 2027 between 9:00 a.m. and 12:00 p.m.\n"
     "PATIENT RIGHTS: You have the right to be treated with respect, to take part in planning your care, to refuse "
     "treatment, and to file a complaint without fear. To file a complaint, call our office or the State Home Health Hotline "
     "at 1-800-555-0130.\n"
     "Our office is open Monday through Friday, 8:00 a.m. to 5:00 p.m. After hours, call our 24-hour on-call nurse at "
     "(919) 555-0131. In an emergency, call 911.",
     "Welcome to home health",
     [P("Welcome",
        T("Welcome to **Bright Path Home Health**.", "house"),
        T("We will **visit** you at **home**.", "home visit"),
        T("**Dr. Karen Liu** asked us to come.", "doctor")),
      P("Your nurse",
        T("Nurse: **Tasha Greene**, **RN**", "nurse"),
        T("**2 times** a week, for **4 weeks**.", "calendar"),
        T("The nurse checks your **health** and **medicines**.", "blood pressure"),
        T("The nurse teaches about **preventing stroke**.", "brain")),
      P("Your physical therapist",
        T("**Daniel Park**, **PT**", "physical therapist"),
        T("**3 times** a week, for **6 weeks**.", "calendar")),
      P("Your speech therapist",
        T("**Maria Ochoa**, **SLP**", "speech therapist"),
        T("**2 times** a week, for **6 weeks**.", "calendar")),
      P("Your aide",
        T("An **aide** helps you **bathe**.", "bath"),
        T("**2 times** a week.", "calendar")),
      P("First visit",
        T("Your first **nurse** visit:", "nurse"),
        T("**Monday, January 11, 2027**", "calendar"),
        T("Between **9:00 a.m.** and **12:00 p.m.**", "clock")),
      P("Your rights",
        T("Be treated with **respect**.", "respect"),
        T("Help **plan** your care.", "plan"),
        T("Say **no** to treatment.", "no"),
        T("**Complain** without **fear**.", "talk")),
      P("To complain",
        T("Call our **office**.", "phone"),
        T("Or call the **State Home Health Hotline**.", "phone"),
        PH("Hotline: 1-800-555-0130")),
      P("Office hours",
        T("**Monday** to **Friday**.", "calendar"),
        T("**8:00 a.m.** to **5:00 p.m.**", "clock")),
      P("After hours",
        T("Call our **on-call nurse**, **24 hours** a day.", "nurse"),
        PH("On-call nurse: (919) 555-0131"),
        CR("Emergency? Call 911"))],
     ["'Check vital signs' became 'checks your health'. Please confirm this is enough."]),

# 8 ── Lab results letter ───────────────────────────────────────────────────────
pair("lab-results-en-001", "en", "results", "Lab results letter (made-up example)",
     "Lab Results Letter\n"
     "Dear Ms. Evelyn Carter,\n"
     "Your blood tests from 01/15/2027 have been reviewed by Dr. Samuel Ortiz.\n"
     "Lipid panel: Total cholesterol 228 mg/dL (desirable: under 200). LDL cholesterol 142 mg/dL (your goal: under 70). "
     "HDL cholesterol 48 mg/dL. Triglycerides 190 mg/dL (normal: under 150).\n"
     "Hemoglobin A1c: 6.1% (prediabetes range: 5.7 to 6.4%). Kidney function: normal.\n"
     "Plan: Your LDL is above your goal. Dr. Ortiz recommends increasing atorvastatin from 40 mg to 80 mg at bedtime. "
     "A new prescription has been sent to your pharmacy. Repeat lipid panel in 3 months.\n"
     "Your A1c is in the prediabetes range. Dr. Ortiz recommends meeting with a dietitian; call (919) 555-0132 to schedule.\n"
     "If you have questions, send a message through the patient portal or call the clinic at (919) 555-0133.",
     "Your blood test results",
     [P("Your blood test results",
        T("For: **Ms. Evelyn Carter**", "person"),
        T("**Dr. Samuel Ortiz** looked at your **blood tests**.", "doctor")),
      P("Cholesterol",
        T("Total **cholesterol**: **228 mg/dL**", "blood test"),
        T("Best is **under 200**.", "target")),
      P("LDL cholesterol",
        T("**LDL**: **142 mg/dL**", "blood test"),
        T("Your goal: **under 70**.", "target"),
        T("Your LDL is **too high**.", "warning")),
      P("Other results",
        T("**HDL** cholesterol: **48 mg/dL**", "blood test"),
        T("**Triglycerides**: **190 mg/dL**", "blood test"),
        T("Normal is **under 150**.", "target")),
      P("Blood sugar and kidneys",
        T("**A1c**: **6.1%**", "blood sugar"),
        T("This is in the **prediabetes** range (**5.7 to 6.4%**).", "blood sugar"),
        T("**Kidneys**: **normal**.", "kidney")),
      P("Medicine change",
        T("**Atorvastatin**: take **more**.", "pill"),
        T("Old dose: **40 mg**. New dose: **80 mg**.", "pill"),
        T("Take it at **bedtime**.", "bed"),
        T("Your **pharmacy** has the new **prescription**.", "pharmacy")),
      P("Next test",
        T("Check **cholesterol** again in **3 months**.", "calendar")),
      P("See a dietitian",
        T("Meet with a **dietitian**.", "dietitian"),
        T("**Call** to make a visit.", "phone"),
        PH("Dietitian: (919) 555-0132")),
      P("Questions?",
        T("Send a **message** in the **patient portal**.", "computer"),
        T("Or **call** the clinic.", "phone"),
        PH("Clinic: (919) 555-0133"))],
     ["'Above your goal' became 'too high'. Please confirm."],
     omitted=["Test date 01/15/2027: past date"]),

# 9 ── Hospital bill with financial assistance ──────────────────────────────────
pair("billing-statement-en-001", "en", "billing", "Hospital billing statement (made-up example)",
     "PATIENT STATEMENT — Carolina Valley Medical Center\n"
     "Statement date: 02/01/2027 | Account number: 4471-882-019 | Guarantor: Gloria Whitaker\n"
     "Service dates: 01/03/2027 to 01/08/2027 (Inpatient)\n"
     "Total charges: $48,312.00 | Insurance payments and adjustments: -$46,812.00 | AMOUNT DUE: $1,500.00\n"
     "PAYMENT DUE BY: March 3, 2027\n"
     "Ways to pay: online at www.example.org/paybill, by phone at (919) 555-0135, or by mail using the attached coupon. "
     "Payment plans with no interest are available.\n"
     "FINANCIAL ASSISTANCE: You may qualify for free or reduced-cost care based on household income. Apply at "
     "www.example.org/assist or call a financial counselor at (919) 555-0136. Applying will place your account on hold while "
     "your application is reviewed.\n"
     "If you believe this bill is wrong, call Patient Accounts at (919) 555-0135 within 60 days.",
     "Your hospital bill",
     [P("Your hospital bill",
        T("For: **Gloria Whitaker**", "person"),
        T("From **Carolina Valley Medical Center**.", "hospital"),
        T("For your **hospital stay**.", "hospital bed")),
      P("What you owe",
        T("You owe **$1,500.00**.", "money"),
        T("Pay by **March 3, 2027**.", "calendar")),
      P("How the bill adds up",
        T("The hospital charged **$48,312.00**.", "bill"),
        T("Insurance paid or took off **$46,812.00**.", "insurance card")),
      P("Your account number",
        T("Your account number: **4471-882-019**", "card"),
        T("Have it ready when you **pay**.", "money")),
      P("How to pay",
        S("**Online**: www.example.org/paybill", "computer"),
        S("By **phone**.", "phone"),
        S("By **mail**, with the **coupon**.", "envelope"),
        PH("Payments: (919) 555-0135")),
      P("Payment plan",
        T("You can pay a **little** at a time.", "money"),
        T("**No interest**.", "no")),
      P("Help paying",
        T("You may get **free** or **lower-cost** care.", "money"),
        T("It depends on your **household income**.", "house"),
        T("While we **review**, your bill is **on hold**.", "pause")),
      P("Apply for help",
        T("Apply online: **www.example.org/assist**", "computer"),
        T("Or call a **financial counselor**.", "counselor"),
        PH("Financial counselor: (919) 555-0136")),
      P("Think the bill is wrong?",
        T("**Call** Patient Accounts within **60 days**.", "phone"),
        PH("Patient Accounts: (919) 555-0135"))],
     ["'Have it ready when you pay' is added to explain why the account number is shown. Please confirm."],
     omitted=["Statement date 02/01/2027: not needed", "Service dates 01/03/2027 to 01/08/2027: past dates of the stay"]),

# 10 ── Advance care planning ───────────────────────────────────────────────────
pair("education-advance-directive-en-001", "en", "education", "Advance care planning information (made-up example)",
     "Advance Care Planning: Health Care Power of Attorney and Living Will\n"
     "An advance directive is a legal document that lets you state your wishes for medical care if you become unable to make "
     "decisions for yourself. A Health Care Power of Attorney names a person (your health care agent) to make medical "
     "decisions for you if you cannot. A Living Will states which treatments you would or would not want at the end of life, "
     "such as a breathing machine or a feeding tube. These forms must be signed according to your state's rules, which often "
     "require witnesses or a notary.\n"
     "Having aphasia does not mean you cannot make your own decisions. Your speech-language pathologist can help you "
     "understand the forms and communicate your choices.\n"
     "Free forms are available from your state. For help completing the forms, call Triangle Legal Help at (919) 555-0137.",
     "Planning your medical care",
     [P("Plan ahead",
        T("You can **plan** your **medical care** ahead.", "plan"),
        T("This is called an **advance directive**.", "document"),
        T("It shows your **wishes** if you **cannot decide** later.", "wish")),
      P("Choose a person",
        T("**Health Care Power of Attorney**", "document"),
        T("You **choose a person**.", "person"),
        T("They **decide** for you if you **cannot**.", "decide")),
      P("Your wishes",
        T("**Living Will**", "document"),
        T("It says which **treatments** you **want** or **do not want**.", "choose"),
        T("Like a **breathing machine** or **feeding tube**.", "hospital bed"),
        T("At the **end of life**.", "end")),
      P("Signing",
        T("Forms must be **signed** by your **state's rules**.", "signature"),
        T("Often with **witnesses** or a **notary**.", "witness")),
      P("Aphasia and decisions",
        T("Aphasia does **not** mean you **cannot decide**.", "decide"),
        T("Your **speech therapist** can **help**.", "speech therapist"),
        T("They help you **understand** the forms.", "read"),
        T("And **share** your choices.", "talk")),
      P("Getting help",
        T("The forms are **free** from your **state**.", "free"),
        T("For help, call **Triangle Legal Help**.", "lawyer"),
        PH("Phone: (919) 555-0137"))],
     ["Legal topic: wording is general on purpose; a real version should be checked for the reader's state."]),

# 11 ── CPAP instructions ───────────────────────────────────────────────────────
pair("how-to-cpap-en-001", "en", "how_to", "CPAP instructions (made-up example)",
     "CPAP THERAPY INSTRUCTIONS\n"
     "You have been diagnosed with obstructive sleep apnea (OSA). Untreated sleep apnea increases the risk of stroke, high "
     "blood pressure, and heart disease.\n"
     "Your CPAP settings: pressure 10 cm H2O, ramp 20 minutes, heated humidifier level 3.\n"
     "Use CPAP every night, for the entire night, including naps.\n"
     "DAILY: Wash the mask cushion with mild soap and warm water. Empty the water chamber and let it air-dry.\n"
     "WEEKLY: Wash the tubing and headgear; let them air-dry. Refill the humidifier with distilled water only.\n"
     "Replace the mask cushion every month and the filter every 2 weeks.\n"
     "Your insurance requires use of at least 4 hours per night on 70% of nights during the first 90 days.\n"
     "Sleep medicine follow-up: Friday, March 26, 2027 at 9:40 a.m.\n"
     "Call Rest Easy Medical Supply at (919) 555-0139 for supplies or equipment problems.",
     "Using your CPAP",
     [P("Your CPAP",
        T("You have **sleep apnea**.", "sleep"),
        T("Your **breathing stops** while you **sleep**.", "breathing"),
        T("Without treatment, the risk of **stroke** goes **up**.", "brain"),
        T("And **high blood pressure** and heart disease.", "heart")),
      P("Use it every night",
        T("Use your **CPAP** every **night**.", "cpap"),
        T("Use it **all night**.", "moon"),
        T("Use it for **naps** too.", "nap")),
      P("Every day",
        S("Wash the **mask cushion** with mild soap and warm water.", "wash"),
        S("**Empty** the **water chamber**.", "water"),
        S("Let it **air-dry**.", "dry")),
      P("Every week",
        S("Wash the **tubing** and **headgear**.", "wash"),
        S("Let them **air-dry**.", "dry"),
        T("Use **distilled water** only.", "water bottle")),
      P("Replace parts",
        T("New **mask cushion** every **month**.", "calendar"),
        T("New **filter** every **2 weeks**.", "filter")),
      P("Insurance rule",
        T("Use it at least **4 hours** a night.", "clock"),
        T("On **70%** of nights.", "calendar"),
        T("For the first **90 days**.", "calendar")),
      P("Sleep doctor visit",
        T("**Friday, March 26, 2027**", "calendar"),
        T("**9:40 a.m.**", "clock")),
      P("Supplies or problems",
        T("Call **Rest Easy Medical Supply**.", "phone"),
        PH("Phone: (919) 555-0139"))],
     ["'Obstructive sleep apnea' explained as 'your breathing stops while you sleep'. Please confirm."],
     omitted=["CPAP settings (pressure 10 cm H2O, ramp 20 minutes, humidifier level 3): set by the supplier, no action"]),

# 12 ── Driving after stroke ────────────────────────────────────────────────────
pair("letter-driving-en-001", "en", "letter", "Letter about driving after stroke (made-up example)",
     "Re: Driving After Stroke\n"
     "Dear Mr. Leon Fraser,\n"
     "Following your stroke, your physician, Dr. Ravi Patel, recommends that you do not drive until you complete a formal "
     "driving evaluation. Stroke can affect vision, reaction time, attention, and judgment, even when you feel ready to "
     "drive.\n"
     "A certified driver rehabilitation specialist at Safe Roads Driver Rehab will complete a clinical assessment (about "
     "1.5 hours) and an on-road test (about 1 hour). Most insurance plans do not cover the evaluation; the cost is $450. "
     "Call (919) 555-0140 to schedule.\n"
     "Bring your driver's license, glasses, and a list of your medications.\n"
     "You will receive a written report. It may recommend driving with restrictions, adaptive equipment, more training, or "
     "stopping driving.\n"
     "Until then, please arrange other transportation. Triangle Ride Access offers door-to-door rides: (919) 555-0141.",
     "About driving",
     [P("About driving",
        T("For: **Mr. Leon Fraser**", "person"),
        T("**Dr. Ravi Patel** says: **do not drive** for now.", "no driving"),
        T("First you need a **driving test**.", "car")),
      P("Why",
        T("A stroke can change your **vision**.", "eye"),
        T("And how **fast** you **react**.", "fast"),
        T("And your **attention** and **judgment**.", "brain"),
        T("Even if you feel **ready**.", "person")),
      P("The driving test",
        T("At **Safe Roads Driver Rehab**.", "car"),
        T("**Office test**: about **1.5 hours**.", "clock"),
        T("**Road test**: about **1 hour**.", "road")),
      P("Cost",
        T("It costs **$450**.", "money"),
        T("Most **insurance** does **not pay**.", "insurance card")),
      P("Make an appointment",
        T("**Call** Safe Roads Driver Rehab.", "phone"),
        PH("Phone: (919) 555-0140")),
      P("What to bring",
        S("Your **driver's license**.", "license"),
        S("Your **glasses**.", "glasses"),
        S("A **list** of your **medicines**.", "medicine list")),
      P("After the test",
        T("You get a **written report**.", "report"),
        T("It may say: drive with **limits**.", "limit"),
        T("Or use **special equipment**, or get **more training**.", "car"),
        T("Or **stop driving**.", "no driving")),
      P("Until then",
        T("Find **other rides**.", "bus"),
        T("**Triangle Ride Access** picks you up at your **door**.", "van"),
        PH("Phone: (919) 555-0141"))],
     ["'Certified driver rehabilitation specialist' is not named; page 3 just names the place. Please check."]),

# 13 ── Neuropsychological evaluation appointment ───────────────────────────────
pair("appointment-neuropsych-en-001", "en", "appointment", "Neuropsychological evaluation confirmation (made-up example)",
     "NEUROPSYCHOLOGICAL EVALUATION — APPOINTMENT CONFIRMATION\n"
     "Patient: Ruth Ann Mabry. Your evaluation with Dr. Elena Vasquez, PhD, is scheduled for Tuesday, April 13, 2027, from "
     "8:30 a.m. to approximately 12:30 p.m. Location: Brainworks Neuropsychology, 77 Commerce Boulevard, Building B.\n"
     "The evaluation includes an interview and paper-and-pencil and computer tasks of memory, attention, language, and "
     "problem solving. Because you have aphasia, tasks will be adapted, and a family member may join the interview.\n"
     "Please bring: glasses and hearing aids; a list of medications; any previous test reports. Get a good night's sleep "
     "and eat breakfast. Breaks will be provided.\n"
     "Results will be reviewed at a feedback appointment about 2 weeks later.\n"
     "CANCELLATION POLICY: Please give 48 hours' notice. Late cancellations and missed appointments are charged a $75 fee. "
     "To reschedule: (919) 555-0143.",
     "Your thinking tests",
     [P("Your thinking tests",
        T("For: **Ruth Ann Mabry**", "person"),
        T("You have **thinking tests**.", "brain"),
        T("With **Dr. Elena Vasquez, PhD**.", "doctor")),
      P("When",
        T("**Tuesday, April 13, 2027**", "calendar"),
        T("**8:30 a.m.** to about **12:30 p.m.**", "clock")),
      P("Where",
        T("**Brainworks Neuropsychology**", "clinic"),
        T("**77 Commerce Boulevard, Building B**", "map")),
      P("What happens",
        T("First, a **talk** with the doctor.", "conversation"),
        T("Then **tasks** on **paper** and **computer**.", "computer"),
        T("They test **memory**, attention, **language** and problem solving.", "brain")),
      P("Made for aphasia",
        T("Tasks will be **changed** to fit your **aphasia**.", "adapt"),
        T("A **family member** can join the **talk**.", "family")),
      P("What to bring",
        S("**Glasses** and **hearing aids**.", "glasses"),
        S("A **list** of your **medicines**.", "medicine list"),
        S("Old **test reports**.", "report")),
      P("Get ready",
        T("**Sleep** well the night before.", "sleep"),
        T("Eat **breakfast**.", "breakfast"),
        T("You will get **breaks**.", "break")),
      P("Your results",
        T("You get your **results** at another visit.", "report"),
        T("About **2 weeks** later.", "calendar")),
      P("Cancel or change",
        T("Tell us **48 hours** before.", "clock"),
        T("Late cancel or missed visit: **$75** fee.", "money"),
        PH("Phone: (919) 555-0143"))]),
]

mark_reviewed(PAIRS, "CCC-SLP (anonymous)", "2026-11-12")
write(PAIRS, "batch3_en.jsonl")
