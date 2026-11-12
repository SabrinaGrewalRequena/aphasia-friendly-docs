"""Batch 5 (English): 13 made-up pairs in messy real-world formats (portal messages, pharmacy
labels, text reminders, voicemail transcripts, tables, faxed referrals, scanned-page errors,
email threads, legal fine print). All names, clinics, IDs and numbers are invented (phones use
555-01xx; websites use example.org). Approved with no changes by a CCC-SLP (anonymous) on 2026-11-12.

Run:  python data/sources/batch5_en.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from batch2_helpers import B, C, CR, P, PH, S, T, mark_reviewed, pair, write  # noqa: E402,F401

PAIRS = [
# 1 ── Patient portal message from a nurse ──────────────────────────────────────
pair("portal-message-en-001", "en", "message", "Patient portal message (made-up example)",
     "From: Megan Hollis, RN (Maple Ridge Family Medicine)\nTo: Harold Jenkins\nSubject: RE: blood pressure readings\n\n"
     "Hi Mr. Jenkins, thanks for sending your readings!! Dr. Liu looked at them. Since your BPs have been running low-ish "
     "(lots of 100s/60s) and you mentioned feeling dizzy when you stand up, she wants you to HOLD the amlodipine 10 mg for "
     "now - don't take it starting tomorrow AM. Keep taking everything else the same. Please keep checking your BP every "
     "morning & send us the numbers again in 1 week. If you get really dizzy, faint, or fall, call us right away at "
     "(919) 555-0123 or go to urgent care. If you have chest pain or stroke symptoms call 911!! Thanks, Megan",
     "Message from your nurse",
     [P("Message from your nurse",
        T("For: **Harold Jenkins**", "person"),
        T("From **Megan Hollis, RN**.", "nurse"),
        T("**Dr. Liu** looked at your **blood pressure** numbers.", "doctor")),
      P("What they saw",
        T("Your blood pressure is a bit **low**.", "blood pressure"),
        T("Many readings in the **100s/60s**.", "blood pressure"),
        T("You said you feel **dizzy** when you **stand up**.", "dizzy")),
      P("Medicine change",
        T("**Stop** amlodipine **10 mg** for now.", "stop"),
        T("Start **tomorrow morning**.", "sunrise"),
        T("Keep taking **everything else** the same.", "pills")),
      P("Keep checking",
        T("Check your **blood pressure** every **morning**.", "blood pressure"),
        T("**Send** the numbers again in **1 week**.", "message")),
      P("Very dizzy? Fainted? Fell?",
        T("**Call** the clinic right away.", "phone"),
        PH("Clinic: (919) 555-0123"),
        T("Or go to **urgent care**.", "clinic")),
      P("Emergency",
        T("**Chest pain**? **Stroke** signs?", "chest pain"),
        CR("Call 911"))],
     ["'Hold the amlodipine' became 'Stop amlodipine for now'. Please confirm 'stop for now' is clear enough that it is not permanent."]),

# 2 ── Pharmacy label ───────────────────────────────────────────────────────────
pair("pharmacy-label-en-001", "en", "medication", "Pharmacy label (made-up example)",
     "RIVERBEND PHARMACY  (919) 555-0102\nRx# 0048213   Date filled: 01/20/2027\nJENKINS, HAROLD\n"
     "GABAPENTIN 300 MG CAPSULE\nTAKE 1 CAPSULE BY MOUTH THREE TIMES DAILY\nQty: 90   Refills: 2   Dr. Karen Liu\n"
     "Discard after: 01/20/2028\n"
     "[Yellow sticker] MAY CAUSE DROWSINESS OR DIZZINESS. USE CARE WHEN DRIVING OR OPERATING MACHINERY.\n"
     "[Red sticker] DO NOT DRINK ALCOHOL WHILE TAKING THIS MEDICATION.\n"
     "[Blue sticker] DO NOT STOP TAKING SUDDENLY WITHOUT ASKING YOUR DOCTOR.",
     "Your medicine label: gabapentin",
     [P("Your medicine",
        T("For: **Harold Jenkins**", "person"),
        T("**Gabapentin 300 mg** capsule", "capsule"),
        T("From **Dr. Karen Liu**.", "doctor")),
      P("How to take it",
        T("Take **1 capsule**.", "capsule"),
        T("By **mouth**.", "mouth"),
        T("**Three times** a day.", "calendar")),
      P("Warnings",
        T("You may feel **sleepy** or **dizzy**.", "sleepy"),
        T("Be **careful** driving or using **machines**.", "car"),
        T("**No alcohol**.", "no alcohol")),
      P("Do not stop suddenly",
        T("**Do not stop** this medicine **suddenly**.", "stop"),
        T("**Ask** your **doctor** first.", "doctor")),
      P("Refills",
        T("**2 refills** left.", "pill bottle"),
        T("Rx number: **0048213**", "label"),
        T("Throw away after **01/20/2028**.", "trash")),
      P("Pharmacy",
        T("**Riverbend Pharmacy**", "pharmacy"),
        PH("Phone: (919) 555-0102"))],
     ["The label is written in capital letters; the handout uses normal letters.",
      "'Qty: 90' is left out (pharmacy count, no action)."],
     omitted=["Date filled 01/20/2027: past date", "Qty: 90: number of capsules in the bottle, no action"]),

# 3 ── Text message reminder ────────────────────────────────────────────────────
pair("sms-reminder-en-001", "en", "appointment", "Text message appointment reminder (made-up example)",
     "PiedmontSpeech: Reminder: Bernard has an appt w/ J. Ellis SLP on Thu 3/18 @ 1:30PM at 1420 Duke St Ste 2. "
     "Reply C to confirm, R to reschedule, STOP to opt out. Msg&data rates may apply. Need help? Call 919-555-0107",
     "Text message reminder",
     [P("Appointment reminder",
        T("**Bernard** has **speech therapy**.", "speech therapist"),
        T("With **J. Ellis**, speech therapist.", "speech therapist"),
        T("At **Piedmont Speech** clinic.", "clinic")),
      P("When and where",
        T("**Thu 3/18**", "calendar"),
        T("**1:30PM**", "clock"),
        T("**1420 Duke St Ste 2**", "map")),
      P("Answer the text",
        T("Type **C** to say **yes**, you will come.", "yes"),
        T("Type **R** to **change** the time.", "calendar"),
        T("Type **STOP** to get **no more** texts.", "no")),
      P("Need help?",
        PH("Call 919-555-0107"))],
     ["Date and time kept exactly as in the text ('Thu 3/18', '1:30PM') because the fact check needs them unchanged; an SLP may prefer 'Thursday, March 18'.",
      "'Msg&data rates may apply' left out."],
     omitted=["Msg&data rates may apply: phone company fine print"]),

# 4 ── Voicemail transcript ─────────────────────────────────────────────────────
pair("voicemail-en-001", "en", "message", "Voicemail transcript (made-up example)",
     "[Voicemail transcript, 2:14 PM] \"Hi, um, this message is for Dolores Pruitt. This is, uh, Kayla from Northgate "
     "Imaging calling about your MRI. So we had to move it, the machine is getting serviced that day, sorry about that. Your "
     "new time is Friday, February 5, 2027 at 3:45 p.m., that's in the afternoon, same place, 4410 Pinecrest Parkway. Um, "
     "everything else is the same, no metal, you can eat. If that time doesn't work just give us a call back at "
     "(919) 555-0181, again that's (919) 555-0181. Okay, thanks, bye.\"",
     "Your MRI time changed",
     [P("Your MRI time changed",
        T("For: **Dolores Pruitt**", "person"),
        T("**Kayla** from **Northgate Imaging** called.", "phone"),
        T("Your **MRI** time **changed**.", "mri")),
      P("Why",
        T("The **machine** needs **repairs** that day.", "repair")),
      P("New time",
        T("**Friday, February 5, 2027**", "calendar"),
        T("**3:45 p.m.** (afternoon)", "clock")),
      P("Same place",
        T("**4410 Pinecrest Parkway**", "map")),
      P("Everything else is the same",
        T("**No metal**.", "no metal"),
        T("You can **eat**.", "eat")),
      P("Time does not work?",
        T("**Call** them back.", "phone"),
        PH("Phone: (919) 555-0181"))],
     ["'Getting serviced' became 'needs repairs'."],
     omitted=["Voicemail time stamp 2:14 PM: when the call came, no action"]),

# 5 ── Surgery prep with abbreviations ──────────────────────────────────────────
pair("pre-op-en-001", "en", "procedure", "Pre-procedure instructions with abbreviations (made-up example)",
     "PRE-PROCEDURE INSTRUCTIONS — Carotid endarterectomy (CEA), L side\n"
     "Pt: Walter Simmons | Surgeon: Dr. Nina Castellano | Date: Mon 3/8/27 | Arrive: 6 AM, Surgical Admissions, CVMC "
     "Main Bldg 2nd fl\n"
     "• NPO after MN (nothing to eat or drink after midnight), incl. gum, mints, water.\n"
     "• HOLD clopidogrel x 5 days before surgery (last dose Tues 3/2/27).\n"
     "• Take metoprolol AM of surgery w/ small sip of water.\n"
     "• Shower w/ CHG soap night before & AM of surgery.\n"
     "• Bring: med list, ID, ins card, CPAP if you use one.\n"
     "• Must have responsible adult to drive you home & stay w/ you x 24 hrs.\n"
     "Questions/illness before surgery (fever, cough): call Pre-Op Clinic (919) 555-0169.",
     "Getting ready for your neck surgery",
     [P("Your surgery",
        T("For: **Walter Simmons**", "person"),
        T("Surgery on the **left side** of your **neck**.", "neck"),
        T("It **cleans out** a blood vessel (**carotid endarterectomy**).", "blood vessel"),
        T("Surgeon: **Dr. Nina Castellano**", "surgeon")),
      P("When and where",
        T("**Mon 3/8/27**", "calendar"),
        T("Arrive at **6 AM**.", "clock"),
        T("**Surgical Admissions**, Main Building, **2nd floor**", "hospital")),
      P("Nothing to eat or drink",
        T("**Nothing** to **eat** or **drink** after **midnight**.", "no food"),
        T("**No** gum, mints or water.", "no")),
      P("Clopidogrel",
        T("**Stop** clopidogrel **5 days** before surgery.", "stop"),
        T("Last dose: **Tues 3/2/27**.", "calendar")),
      P("Metoprolol",
        T("**Take** metoprolol the **morning** of surgery.", "pill"),
        T("With a **small sip** of **water**.", "glass of water")),
      P("Shower",
        T("Shower with the **special soap** (**CHG**).", "shower"),
        T("The **night before** and the **morning** of surgery.", "calendar")),
      P("What to bring",
        S("Your **medicine list**.", "medicine list"),
        S("Your **ID** and **insurance card**.", "identity card"),
        S("Your **CPAP**, if you use one.", "cpap")),
      P("A ride home",
        T("An **adult** must **drive** you home.", "car"),
        T("They must **stay** with you for **24 hours**.", "family")),
      P("Sick before surgery?",
        T("**Fever**? **Cough**? Questions?", "fever"),
        PH("Pre-Op Clinic: (919) 555-0169"))],
     ["Abbreviations spelled out: NPO, MN, HOLD, w/, x, AM, CHG.",
      "'Cleans out a blood vessel' explains endarterectomy; please confirm.",
      "'CVMC' (hospital name) not spelled out because the original does not give it in full; please add if known."],
     omitted=["CVMC: hospital abbreviation not spelled out in the original"]),

# 6 ── Letter with legal fine print ─────────────────────────────────────────────
pair("letter-legal-en-001", "en", "appointment", "Appointment letter with legal notices (made-up example)",
     "Carolina Valley Medical Center — Neurology\n"
     "Dear Ms. Evelyn Carter: This letter confirms your new patient appointment with Dr. Ravi Patel on Wednesday, March 10, "
     "2027 at 9:00 a.m. Please arrive 30 minutes early to complete paperwork. Bring your insurance card, photo ID, and all "
     "medication bottles.\n\n"
     "NOTICE OF NONDISCRIMINATION: Carolina Valley Medical Center complies with applicable Federal civil rights laws and does "
     "not discriminate on the basis of race, color, national origin, age, disability, or sex. We provide free aids and "
     "services to people with disabilities to communicate effectively with us, such as qualified sign language interpreters "
     "and written information in other formats (large print, audio, accessible electronic formats). If you believe we have "
     "failed to provide these services, you can file a grievance with our Civil Rights Coordinator at 1-800-555-0171.\n"
     "ATTENTION: If you speak Spanish, language assistance services, free of charge, are available to you. Call "
     "1-800-555-0171 (TTY: 711). ATENCIÓN: si habla español, tiene a su disposición servicios gratuitos de asistencia "
     "lingüística. Llame al 1-800-555-0171 (TTY: 711).\n"
     "To reschedule, call (919) 555-0124.",
     "Your neurology appointment",
     [P("Your appointment",
        T("For: **Ms. Evelyn Carter**", "person"),
        T("New visit with **Dr. Ravi Patel**.", "doctor"),
        T("At **Carolina Valley Medical Center**, **Neurology**.", "hospital")),
      P("When",
        T("**Wednesday, March 10, 2027**", "calendar"),
        T("**9:00 a.m.**", "clock"),
        T("Arrive **30 minutes early** for **paperwork**.", "clock")),
      P("What to bring",
        S("Your **insurance card**.", "insurance card"),
        S("Your **photo ID**.", "identity card"),
        S("**All** your **medicine bottles**.", "pill bottle")),
      P("Free help to communicate",
        T("You can get **free help** to talk with us.", "help"),
        T("Like **big print**, audio, or **sign language**.", "large print"),
        T("Free **language help** too.", "interpreter")),
      P("Ask for help or complain",
        PH("Phone: 1-800-555-0171"),
        PH("TTY: 711", "tty")),
      P("Change your appointment",
        PH("Phone: (919) 555-0124"))],
     ["Most of the legal notice is summarized in one page ('free help to communicate'). The Spanish tagline is not repeated; the handout is English. Please check this is acceptable for the clinic."],
     omitted=["Full nondiscrimination notice text: legal fine print; key rights kept on the 'Free help' pages"]),

# 7 ── Medication table ─────────────────────────────────────────────────────────
pair("medication-table-en-001", "en", "medication", "Medication schedule table (made-up example)",
     "DAILY MEDICATION SCHEDULE — Dolores Pruitt (updated 01/08/2027)\n"
     "| Medication | Dose | Breakfast | Lunch | Dinner | Bedtime | Purpose |\n"
     "| Apixaban | 5 mg | X | | X | | blood thinner |\n"
     "| Atorvastatin | 80 mg | | | | X | cholesterol |\n"
     "| Metoprolol | 25 mg | X | | X | | heart rate |\n"
     "| Vitamin D | 1000 units | X | | | | bones |\n"
     "Questions: Stroke Nurse Line (919) 555-0125.",
     "My medicine times",
     [P("My medicine times",
        T("For: **Dolores Pruitt**", "person")),
      P("Breakfast",
        T("**Apixaban 5 mg**: blood thinner", "pill"),
        T("**Metoprolol 25 mg**: heart rate", "pill"),
        T("**Vitamin D 1000 units**: bones", "pill")),
      P("Lunch",
        T("**No** medicines at lunch.", "no pill")),
      P("Dinner",
        T("**Apixaban 5 mg**: blood thinner", "pill"),
        T("**Metoprolol 25 mg**: heart rate", "pill")),
      P("Bedtime",
        T("**Atorvastatin 80 mg**: cholesterol", "pill")),
      P("Questions?",
        T("**Stroke Nurse Line**", "nurse"),
        PH("Phone: (919) 555-0125"))],
     ["The table is turned into one page per time of day."],
     omitted=["Updated 01/08/2027: date the list was made"]),

# 8 ── Faxed referral full of abbreviations ─────────────────────────────────────
pair("fax-referral-en-001", "en", "referral", "Faxed referral with abbreviations (made-up example)",
     "FAX COVER — CONFIDENTIAL. If you received this in error, please notify the sender and destroy all copies.\n"
     "TO: Piedmont Speech Clinic, fax (919) 555-0170 | FROM: Neurology, Dr. Ravi Patel, ph (919) 555-0125 | Pages: 2\n"
     "RE: Pt Marcus Bell, 64 yo M, s/p L MCA CVA 12/14/2026 w/ nonfluent aphasia, mild dysarthria, R hemiparesis. "
     "Pls eval & tx. Dx: I69.320. Freq: 2x/wk x 12 wks. Interpreter needed: N. Ins: Medicare. Pt lives w/ spouse; "
     "spouse to attend sessions. Pt reports frustration w/ word-finding; hx depression, on sertraline.\n"
     "Clinic: pls call pt to schedule.",
     "Your doctor sent you to speech therapy",
     [P("Speech therapy referral",
        T("For: **Marcus Bell**", "person"),
        T("**Dr. Ravi Patel** sent you to **speech therapy**.", "doctor"),
        T("At **Piedmont Speech Clinic**.", "clinic")),
      P("Why",
        T("You had a **stroke** on the **left side** of your brain.", "brain"),
        T("Talking is **hard** (**aphasia**).", "talk"),
        T("Your speech muscles are a little **weak**.", "mouth"),
        T("Your **right side** is **weak**.", "weak arm")),
      P("How often",
        T("**2** times a week.", "calendar"),
        T("For **12 weeks**.", "calendar")),
      P("Your spouse",
        T("Your **spouse** will **come** to sessions too.", "family")),
      P("Feelings",
        T("Finding **words** is **frustrating**.", "frustrated"),
        T("Your **doctor** knows about your **depression** medicine.", "doctor")),
      P("Next step",
        T("The clinic will **call you** to make a visit.", "phone"),
        PH("Dr. Patel's office: (919) 555-0125"))],
     ["Written for the patient, from a referral meant for the clinic.",
      "'Your doctor knows about your depression medicine' is a gentle summary of 'hx depression, on sertraline'. An SLP may prefer to leave this page out; please decide.",
      "Abbreviations expanded: Pt, yo, s/p, L MCA CVA, w/, R, Dx, Freq, x, wk(s), hx."],
     omitted=["Fax number (919) 555-0170: for the offices, not the patient", "Stroke date 12/14/2026: past date",
              "Age 64 yo, diagnosis code I69.320, insurance Medicare, interpreter N: office details",
              "Fax confidentiality notice and page count: fine print"]),

# 9 ── Scanned discharge page with OCR errors ───────────────────────────────────
pair("ocr-discharge-en-001", "en", "discharge", "Scanned discharge page with scanning errors (made-up example)",
     "Page 1 of 2          CAROLINA VALLEY MEDICAL CENTER          Discharge Instruc-\ntions\n"
     "Patient: Gloria Whitaker\nYou were treated for a transient isch-\nemic attack (TIA). Take aspirin 81 mg by mouth once\n"
     "dai1y. Take atorvastatin 40 mg by mouth at bed-\ntime. Fo11ow up with Dr. Samuel Ortiz on Tuesday, March 2, 2027\n"
     "at 2:00 p.m.\nPage 1 of 2          CAROLINA VALLEY MEDICAL CENTER\nIf you have face droop, arm weak-\nness or trouble "
     "speaking, ca11 911 right away. Do not\ndrive for 2 weeks. Ques-\ntions: Stroke Nurse Line (919) 555-0125.",
     "Going home after your TIA",
     [P("You had a TIA",
        T("For: **Gloria Whitaker**", "person"),
        T("You had a **TIA**, a short **blockage** of blood to the **brain**.", "brain")),
      P("Your medicines",
        T("Take **aspirin 81 mg**, by mouth, **once** a day.", "pill"),
        T("Take **atorvastatin 40 mg**, by mouth, at **bedtime**.", "bed")),
      P("See your doctor",
        T("See **Dr. Samuel Ortiz**.", "doctor"),
        T("**Tuesday, March 2, 2027**", "calendar"),
        T("**2:00 p.m.**", "clock")),
      P("No driving",
        T("**Do not drive** for **2 weeks**.", "no driving")),
      P("Emergency",
        T("**Face** drooping? Arm **weak**? Trouble **speaking**?", "face"),
        CR("Call 911 right away")),
      P("Questions?",
        T("**Stroke Nurse Line**", "nurse"),
        PH("Phone: (919) 555-0125"))],
     ["The scan had errors ('dai1y', 'Fo11ow', 'ca11' with the number 1 instead of the letter l) and words split across lines. The handout fixes these. Please check nothing was misread.",
      "'A short blockage of blood to the brain' explains TIA; the original only says 'transient ischemic attack'. Please confirm."],
     omitted=["'Page 1 of 2' and repeated hospital header: scanning artifacts"]),

# 10 ── Lab report with flags ───────────────────────────────────────────────────
pair("lab-report-flags-en-001", "en", "results", "Lab report with high/low flags (made-up example)",
     "LABORATORY REPORT — Maple Ridge Family Medicine\nPatient: Shirley Abernathy | Collected: 02/10/2027 07:42\n"
     "TEST            RESULT   FLAG   REFERENCE RANGE   UNITS\n"
     "SODIUM          134      L      135-145           mmol/L\n"
     "POTASSIUM       4.2             3.5-5.1           mmol/L\n"
     "GLUCOSE         128      H      70-99             mg/dL\n"
     "CREATININE      0.9             0.6-1.1           mg/dL\n"
     "HEMOGLOBIN      11.8     L      12.0-15.5         g/dL\n"
     "Comment (Dr. Karen Liu): Slightly low sodium and hemoglobin, slightly high glucose. Not dangerous. We will repeat these "
     "tests at your next visit. No changes to your medicines. Call (919) 555-0123 with questions.",
     "Your lab results",
     [P("Your lab results",
        T("For: **Shirley Abernathy**", "person"),
        T("**Dr. Karen Liu** looked at your results.", "doctor")),
      P("A little low",
        T("**Sodium**: **134**. Normal: **135-145**.", "salt"),
        T("**Hemoglobin** (blood): **11.8**. Normal: **12.0-15.5**.", "blood")),
      P("A little high",
        T("**Glucose** (blood sugar): **128**. Normal: **70-99**.", "blood sugar")),
      P("Normal",
        T("**Potassium**: **4.2**.", "check mark"),
        T("**Creatinine** (kidneys): **0.9**.", "kidney")),
      P("What it means",
        T("This is **not dangerous**.", "check mark"),
        T("We will **test again** at your **next visit**.", "blood test"),
        T("**No changes** to your medicines.", "pills")),
      P("Questions?",
        PH("Phone: (919) 555-0123"))],
     ["Units (mmol/L, mg/dL, g/dL) and the potassium and creatinine normal ranges are left out to keep pages short. Please check this is acceptable."],
     omitted=["Collected 02/10/2027 07:42: when the blood was drawn",
              "Units mmol/L, mg/dL, g/dL and ranges 3.5-5.1 and 0.6-1.1 for normal results: detail without action"]),

# 11 ── After-hours nurse call summary ──────────────────────────────────────────
pair("nurse-call-en-001", "en", "message", "After-hours nurse call summary (made-up example)",
     "AFTER-HOURS NURSE ADVICE LINE — CALL SUMMARY\nCaller: Linda Marsh (patient) | Call time: Sat 01/30/2027 21:10\n"
     "Reason for call: Headache since this afternoon, 5/10, no weakness, no trouble speaking, no vision changes.\n"
     "Advice given: Take acetaminophen 500 mg, 2 tablets, may repeat in 6 hours if needed. Rest in a quiet, dark room. "
     "Drink water. Check blood pressure; if top number is over 180, call back.\n"
     "Go to the Emergency Department or call 911 if: worst headache of your life, sudden weakness, numbness, trouble "
     "speaking, confusion, or vision loss.\n"
     "Follow-up: call your primary care office on Monday: (919) 555-0106. Nurse line: (919) 555-0172.",
     "Advice from the nurse line",
     [P("Your call to the nurse",
        T("For: **Linda Marsh**", "person"),
        T("You called about a **headache**.", "headache")),
      P("What to do now",
        T("Take **acetaminophen 500 mg**, **2 tablets**.", "pill"),
        T("You may take it **again** after **6 hours** if needed.", "clock"),
        T("**Rest** in a **quiet**, **dark** room.", "bed"),
        T("Drink **water**.", "glass of water")),
      P("Check your blood pressure",
        T("Check your **blood pressure**.", "blood pressure"),
        T("Top number **over 180**? **Call back**.", "phone"),
        PH("Nurse line: (919) 555-0172")),
      P("Emergency",
        T("**Worst** headache of your life?", "headache"),
        T("Sudden **weakness**, **numbness** or **confusion**?", "weak arm"),
        T("Trouble **speaking**? Can't **see**?", "speech"),
        CR("Call 911 or go to the Emergency Department")),
      P("On Monday",
        T("**Call** your **primary care** office.", "phone"),
        PH("Phone: (919) 555-0106"))],
     ["The headache rating (5/10) and the symptoms she did not have are left out."],
     omitted=["Call time Sat 01/30/2027 21:10: when the call happened",
              "Pain 5/10 and 'no weakness, no trouble speaking, no vision changes': what the caller reported"]),

# 12 ── Daily care checklist for a caregiver ────────────────────────────────────
pair("caregiver-checklist-en-001", "en", "home_program", "Daily care checklist (made-up example)",
     "DAILY CARE CHECKLIST — for family caregivers\nPatient: Bernard Okafor\n"
     "MORNING: [ ] Check blood pressure and write it down [ ] Give morning medicines from the pill box [ ] Help with "
     "shower using the shower chair [ ] Do the home speech practice for 15 minutes\n"
     "AFTERNOON: [ ] Walk together for 10 minutes with the cane [ ] Offer water every 2 hours [ ] Practice the "
     "communication book at lunch\n"
     "EVENING: [ ] Give evening medicines [ ] Check skin on heels and hips for red spots [ ] Night-light on in hallway\n"
     "Call the home health nurse at (919) 555-0131 if you see a red spot that does not fade, a fever over 100.4°F, or new "
     "confusion. Call 911 for stroke signs.",
     "Daily care checklist",
     [P("Daily care checklist",
        T("For the **family** caring for **Bernard Okafor**.", "family"),
        T("**Tick** each box when it is **done**.", "check mark")),
      P("Morning",
        C("Check **blood pressure**. Write it down.", "blood pressure"),
        C("Give **morning medicines** from the **pill box**.", "pill organizer"),
        C("Help with the **shower**. Use the **shower chair**.", "shower chair"),
        C("**Speech practice** for **15 minutes**.", "practice")),
      P("Afternoon",
        C("**Walk** together **10 minutes** with the **cane**.", "cane"),
        C("Offer **water** every **2 hours**.", "glass of water"),
        C("Use the **communication book** at **lunch**.", "communication book")),
      P("Evening",
        C("Give **evening medicines**.", "pill"),
        C("Check **heels** and **hips** for **red spots**.", "skin"),
        C("**Night-light** on in the hallway.", "night-light")),
      P("Call the nurse",
        T("A **red spot** that does **not fade**?", "skin"),
        T("**Fever** over **100.4°F**?", "thermometer"),
        T("New **confusion**?", "confused"),
        PH("Home health nurse: (919) 555-0131")),
      P("Emergency",
        T("**Stroke** signs?", "stroke"),
        CR("Call 911"))]),

# 13 ── Email thread about scheduling ───────────────────────────────────────────
pair("email-thread-en-001", "en", "message", "Email thread about scheduling (made-up example)",
     "From: scheduling@example.org\nSent: Tuesday, February 2, 2027 4:51 PM\nTo: Anthony Russo\nSubject: RE: RE: FW: "
     "swallow study??\n\n"
     "Hi Anthony, sorry for the confusion below. The swallow study (modified barium swallow) IS scheduled. It's Thursday, "
     "February 18, 2027 at 10:30 a.m. in Radiology, Carolina Valley Medical Center, Ground Floor. Please don't eat or drink "
     "for 2 hours before. Bring your glasses. The speech therapist, Maria Ochoa, will be there with you. If you need to change "
     "it please call us, don't reply to this email since this inbox isn't monitored on weekends.\nThanks, Scheduling Team | "
     "(919) 555-0128\n\n"
     "-----Original Message-----\nFrom: Anthony Russo\nSent: Monday, February 1, 2027 9:02 AM\nSubject: FW: swallow study??\n"
     "is this still happening? nobody called me\n\n"
     "CONFIDENTIALITY NOTICE: This email may contain protected health information...",
     "Your swallow study",
     [P("Your swallow study",
        T("For: **Anthony Russo**", "person"),
        T("Your **swallow study** **is scheduled**.", "swallow"),
        T("It is an **X-ray** of you **swallowing** (**modified barium swallow**).", "x-ray")),
      P("When and where",
        T("**Thursday, February 18, 2027**", "calendar"),
        T("**10:30 a.m.**", "clock"),
        T("**Radiology**, **Carolina Valley Medical Center**", "hospital"),
        T("**Ground Floor**", "building")),
      P("Before",
        T("**Do not eat** or **drink** for **2 hours** before.", "no food"),
        T("Bring your **glasses**.", "glasses")),
      P("Who will be there",
        T("Your **speech therapist**, **Maria Ochoa**.", "speech therapist")),
      P("Need to change it?",
        T("**Call**. Do **not** answer the **email**.", "phone"),
        PH("Scheduling: (919) 555-0128"))],
     ["'It is an X-ray of you swallowing' explains the test; the email does not say X-ray. Please confirm or remove.",
      "Email headers, the earlier message and the confidentiality notice are left out."],
     omitted=["Email dates Tuesday, February 2, 2027 4:51 PM and Monday, February 1, 2027 9:02 AM: when the emails were sent",
              "scheduling@example.org: inbox not monitored; the reader should call instead",
              "Earlier message and confidentiality notice: not needed"]),
]

mark_reviewed(PAIRS, "CCC-SLP (anonymous)", "2026-11-12")
write(PAIRS, "batch5_en.jsonl")
