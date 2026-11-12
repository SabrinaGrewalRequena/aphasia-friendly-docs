"""Batch 4 (English): 10 made-up pairs for document types the set had few of (consent,
insurance, how-to, procedure, referral, work letter). All names, clinics, IDs and numbers
are invented (phones use 555-01xx; websites use example.org). Approved with no changes by a CCC-SLP (anonymous) on 2026-11-12.

Run:  python data/sources/batch4_en.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from batch2_helpers import B, C, CR, P, PH, S, T, mark_reviewed, pair, write  # noqa: E402,F401

PAIRS = [
# 1 ── Telehealth consent ───────────────────────────────────────────────────────
pair("consent-telehealth-en-001", "en", "consent", "Telehealth consent (made-up example)",
     "CONSENT FOR TELEHEALTH SERVICES — Piedmont Speech Clinic\n"
     "Telehealth means receiving speech therapy by live video instead of in person. Your therapist will use a secure video "
     "platform. Sessions are not recorded unless you give separate written permission. Risks include poor video or sound "
     "quality and, rarely, interruptions or privacy breaches. You may stop a telehealth session at any time and ask for an "
     "in-person visit instead. Your insurance may cover telehealth differently than in-person visits; check with your plan.\n"
     "[ ] I agree to receive speech therapy by telehealth.\n"
     "[ ] I do not agree to telehealth. I want in-person visits only.\n"
     "Patient signature: ____________ Date: ____________\n"
     "Questions: (919) 555-0161",
     "Speech therapy by video",
     [P("Speech therapy by video",
        T("You can have **speech therapy** by **video**.", "video call"),
        T("Instead of going to the **clinic**.", "clinic"),
        T("The video is **secure**.", "lock")),
      P("Recording",
        T("We do **not record** the video.", "no camera"),
        T("Only if you say **yes** in **writing**.", "signature")),
      P("Possible problems",
        T("The **picture** or **sound** may be **poor**.", "video call"),
        T("Rarely, the call may **stop**.", "pause"),
        T("Rarely, **privacy** may be **broken**.", "lock")),
      P("You choose",
        T("You can **stop** any time.", "stop"),
        T("You can ask for an **in-person** visit.", "clinic"),
        T("**Insurance** may pay **differently**. Ask your plan.", "insurance card")),
      P("Please choose",
        C("**Yes**, I want therapy by **video**.", "yes"),
        C("**No**, I want **in-person** visits only.", "no")),
      P("Sign",
        B("Signature: ____________", "signature"),
        B("Date: ____________", "calendar"),
        PH("Questions? Call (919) 555-0161"))],
     ["Consent form: the clinic's privacy or legal team should also approve the wording."]),

# 2 ── Photo release ────────────────────────────────────────────────────────────
pair("consent-photo-en-001", "en", "consent", "Photo release form (made-up example)",
     "PHOTO RELEASE FORM\n"
     "Piedmont Speech Clinic would like to take photos of you to make personal communication materials, such as a picture "
     "board or a photo book of your family and daily activities. With your permission, we may also use photos in printed "
     "clinic materials or on our website. Your name will not appear with any photo used outside your own materials. You may "
     "withdraw this permission at any time by telling your therapist; photos already printed may not be recalled. Saying no "
     "will not affect your care.\n"
     "[ ] Yes, photos for my own communication materials only.\n"
     "[ ] Yes, photos for my materials AND for clinic materials or the website.\n"
     "[ ] No photos.\n"
     "Signature: ____________ Date: ____________",
     "Photos of you",
     [P("Photos of you",
        T("We would like to take **photos** of you.", "camera"),
        T("To make your own **picture board** or **photo book**.", "photo album"),
        T("Of your **family** and **daily activities**.", "family")),
      P("Other use",
        T("If you say **yes**, we may also use photos in **clinic papers**.", "brochure"),
        T("Or on our **website**.", "website"),
        T("Your **name** will **not** be shown with them.", "no name")),
      P("You choose",
        T("You can **change your mind** any time.", "change"),
        T("Tell your **therapist**.", "speech therapist"),
        T("Photos **already printed** may **not** come back.", "printer"),
        T("Saying no does **not change** your **care**.", "care")),
      P("Please choose",
        C("**Yes**, for **my own** materials only.", "yes"),
        C("**Yes**, for my materials **and** clinic papers or website.", "yes"),
        C("**No** photos.", "no")),
      P("Sign",
        B("Signature: ____________", "signature"),
        B("Date: ____________", "calendar"))]),

# 3 ── Insurance denial with appeal ─────────────────────────────────────────────
pair("insurance-denial-en-001", "en", "insurance", "Insurance denial and appeal letter (made-up example)",
     "NOTICE OF DENIAL OF COVERAGE\n"
     "Member: Frank Delgado | Member ID: XJH551902 | Plan: Carolina Community Health Plan\n"
     "Your request for 10 additional outpatient speech therapy visits has been denied. Reason: the information we received "
     "does not show continued measurable progress toward your therapy goals.\n"
     "YOUR RIGHT TO APPEAL: You or someone you choose, such as your therapist, may ask us to review this decision. You must "
     "file your appeal within 60 days of the date on this letter. Send any new information, such as recent progress notes. "
     "To appeal, call Member Services at 1-800-555-0105 (TTY 711) or write to: Appeals Unit, PO Box 4410, Raleigh, NC.\n"
     "If you disagree with our appeal decision, you may ask for an independent external review.\n"
     "Free help is available from the Health Insurance Help Line at 1-800-555-0162.",
     "Your insurance said no",
     [P("Your insurance said no",
        T("For: **Frank Delgado**", "person"),
        T("Member ID: **XJH551902**", "card"),
        T("You asked for **10 more** speech therapy visits.", "speech therapist"),
        T("Your plan said **no**.", "no")),
      P("Why",
        T("The plan did not see enough **progress** toward your **goals**.", "chart")),
      P("You can appeal",
        T("**Appeal** means asking them to **look again**.", "review"),
        T("You or someone you **choose** can do it.", "person"),
        T("Your **therapist** can help.", "speech therapist")),
      P("Deadline",
        T("Appeal within **60 days** of the date on the letter.", "calendar"),
        T("Send **new information**, like **progress notes**.", "document")),
      P("How to appeal: call",
        T("Call **Member Services**.", "phone"),
        PH("Phone: 1-800-555-0105"),
        PH("TTY: 711", "tty")),
      P("How to appeal: write",
        T("Write to: **Appeals Unit, PO Box 4410, Raleigh, NC**", "envelope")),
      P("Still disagree?",
        T("Ask for an **outside review**.", "review"),
        T("Someone **outside** the plan will look at it.", "person")),
      P("Free help",
        T("**Health Insurance Help Line**", "help"),
        PH("Phone: 1-800-555-0162"))],
     ["'Independent external review' became 'outside review: someone outside the plan will look at it'. Please confirm.",
      "The letter's own date is not printed here because the original gives no date; the reader must use the date on the letter."]),

# 4 ── Filling a pill organizer ─────────────────────────────────────────────────
pair("how-to-pill-organizer-en-001", "en", "how_to", "How to fill a weekly pill organizer (made-up example)",
     "HOW TO FILL YOUR WEEKLY PILL ORGANIZER\n"
     "Use a pill organizer with 7 days and 2 times per day (AM and PM).\n"
     "1. Pick one day each week to fill it, for example Sunday. 2. Wash and dry your hands. 3. Line up your pill bottles and "
     "your medication list. 4. Fill one medicine at a time: put it in every box where it belongs, then put the bottle away. "
     "5. When you finish, compare each box with your medication list. 6. Close all the lids.\n"
     "Do not put liquid medicines, inhalers, or pills that must stay in their package into the organizer.\n"
     "If a pill is a different color or shape than usual, call your pharmacy before taking it: (919) 555-0102.\n"
     "Ask a family member or your pharmacist to check your organizer the first few times.",
     "Filling your pill box",
     [P("Your pill box",
        T("Your pill box has **7 days**.", "pill organizer"),
        T("**2 times** a day: **AM** and **PM**.", "sun and moon")),
      P("Get ready",
        S("Pick **one day** each week, like **Sunday**.", "calendar"),
        S("**Wash** and **dry** your hands.", "wash hands"),
        S("Line up your **pill bottles** and your **medicine list**.", "pill bottle")),
      P("Fill it",
        S("Fill **one medicine** at a time.", "pill"),
        S("Put it in **every box** where it belongs.", "pill organizer"),
        S("Put that **bottle away**.", "pill bottle")),
      P("Check it",
        S("**Compare** each box with your **list**.", "check"),
        S("**Close** all the lids.", "close")),
      P("Not in the pill box",
        T("**Liquid** medicines.", "liquid medicine"),
        T("**Inhalers**.", "inhaler"),
        T("Pills that must stay in their **package**.", "blister pack")),
      P("Get help",
        T("Ask **family** or your **pharmacist** to check it.", "family"),
        T("Do this the **first few times**.", "calendar")),
      P("Pill looks different?",
        T("Different **color** or **shape**?", "pill"),
        T("**Call** your pharmacy **before** you take it.", "pharmacy"),
        PH("Pharmacy: (919) 555-0102"))],
     ["Step 4 of the original (fill one medicine, put it in every box, put the bottle away) is split into 3 steps; step numbers on the handout therefore differ from the original."]),

# 5 ── Taking blood pressure at home ────────────────────────────────────────────
pair("how-to-blood-pressure-en-001", "en", "how_to", "How to check your blood pressure at home (made-up example)",
     "HOW TO CHECK YOUR BLOOD PRESSURE AT HOME\n"
     "Before: Do not smoke, exercise, or drink coffee for 30 minutes. Empty your bladder.\n"
     "Steps: 1. Sit in a chair with your back supported and both feet flat on the floor. 2. Rest quietly for 5 minutes. "
     "3. Put the cuff on your bare upper arm, at heart level, on the arm your doctor told you to use. 4. Press start. Do not "
     "talk or move. 5. Write down both numbers and the time. 6. Wait 1 minute and take a second reading.\n"
     "Your goal: below 130/80. Bring your log to every visit.\n"
     "Call your doctor at (919) 555-0123 if your top number is above 180 or your bottom number is above 110 on two readings.\n"
     "Call 911 if your blood pressure is that high AND you have chest pain, trouble speaking, weakness, or vision changes.",
     "Check your blood pressure",
     [P("Before you check",
        T("**No smoking**, **exercise** or **coffee** for **30 minutes**.", "no coffee"),
        T("Go to the **bathroom** first.", "toilet")),
      P("Sit and rest",
        S("**Sit** with your **back** supported.", "chair"),
        S("Both **feet flat** on the floor.", "feet"),
        S("**Rest** quietly for **5 minutes**.", "clock")),
      P("Put on the cuff",
        S("Put the cuff on your **bare upper arm**.", "blood pressure cuff"),
        S("Keep it at **heart level**.", "heart"),
        S("Use the arm your **doctor** told you.", "arm")),
      P("Take the reading",
        S("Press **start**. Do **not talk** or **move**.", "button"),
        S("**Write down** both numbers and the **time**.", "write"),
        S("Wait **1 minute**. Check it **again**.", "clock")),
      P("Your goal",
        T("Below **130/80**.", "target"),
        T("Bring your **list** to **every visit**.", "list")),
      P("Call your doctor",
        T("Top number above **180**?", "blood pressure"),
        T("Or bottom number above **110**?", "blood pressure"),
        T("On **two** readings? **Call**.", "phone"),
        PH("Doctor: (919) 555-0123")),
      P("Emergency",
        T("Blood pressure **that high**, and:", "warning"),
        T("**Chest pain**? Trouble **speaking**?", "chest pain"),
        T("**Weakness**? **Vision** changes?", "weak arm"),
        CR("Call 911"))],
     ["The original's 6 steps are split into 9 shorter steps.", "'Empty your bladder' became 'go to the bathroom first'."]),

# 6 ── EEG preparation ──────────────────────────────────────────────────────────
pair("procedure-eeg-en-001", "en", "procedure", "EEG preparation (made-up example)",
     "ROUTINE EEG (ELECTROENCEPHALOGRAM) — PATIENT INSTRUCTIONS\n"
     "An EEG records the electrical activity of your brain using small metal discs (electrodes) placed on your scalp with a "
     "paste. It does not hurt and does not send electricity into your body.\n"
     "Appointment: Monday, February 22, 2027 at 1:00 p.m., Neurology Testing, Westfield Medical Plaza, 600 Oakmont Drive, "
     "Suite 310.\n"
     "The night before: wash your hair with shampoo only. Do not use conditioner, oil, gel, or hairspray. Your doctor may ask "
     "you to sleep less than usual the night before; follow the instructions on your order.\n"
     "Take your usual medications unless your doctor tells you otherwise. Avoid caffeine on the day of the test.\n"
     "The test takes about 60 to 90 minutes. You may be asked to breathe deeply and look at a flashing light.\n"
     "To reschedule: (919) 555-0103.",
     "Your brain wave test (EEG)",
     [P("Your EEG",
        T("An **EEG** checks your **brain waves**.", "brain"),
        T("Small **metal discs** go on your **head** with a **paste**.", "electrodes")),
      P("It does not hurt",
        T("It does **not hurt**.", "no pain"),
        T("It does **not** put **electricity** into your body.", "no electricity")),
      P("When and where",
        T("**Monday, February 22, 2027**", "calendar"),
        T("**1:00 p.m.**", "clock"),
        T("**Neurology Testing**, **Westfield Medical Plaza**", "hospital"),
        T("**600 Oakmont Drive, Suite 310**", "map")),
      P("The night before",
        T("Wash your **hair** with **shampoo only**.", "shampoo"),
        T("**No** conditioner, oil, gel or hairspray.", "no"),
        T("Your doctor may ask you to **sleep less**.", "sleep"),
        T("Follow the **instructions** on your **order**.", "document")),
      P("Medicine and caffeine",
        T("Take your **usual medicines**.", "pill"),
        T("Unless your **doctor** says something else.", "doctor"),
        T("**No caffeine** on the test day.", "no coffee")),
      P("During the test",
        T("It takes about **60 to 90 minutes**.", "clock"),
        T("You may **breathe deeply**.", "breathe"),
        T("You may look at a **flashing light**.", "light")),
      P("Change your visit",
        PH("Phone: (919) 555-0103"))]),

# 7 ── Referral to community aphasia program ────────────────────────────────────
pair("referral-aphasia-program-en-001", "en", "referral", "Referral to a community aphasia program (made-up example)",
     "REFERRAL — COMMUNITY APHASIA PROGRAM\n"
     "To: Triangle Aphasia Connections | From: Jordan Ellis, M.S., CCC-SLP, Piedmont Speech Clinic\n"
     "Client: Bernard Okafor has completed outpatient speech therapy and is referred for ongoing participation in your "
     "community program to maintain communication skills and social participation.\n"
     "Program information for the client: Triangle Aphasia Connections offers conversation groups, a book club, and a "
     "computer skills class for adults with aphasia. Groups meet Tuesdays and Thursdays, 10:00 a.m. to 12:00 p.m. "
     "Membership is $25 per month; scholarships are available. Care partners may attend at no cost.\n"
     "Next step: an intake coordinator will call you within 2 weeks to schedule a 30-minute intake visit. If you do not hear "
     "from them, call (919) 555-0163.",
     "A program for people with aphasia",
     [P("A program for you",
        T("For: **Bernard Okafor**", "person"),
        T("**Jordan Ellis, M.S., CCC-SLP** sent you to a **program**.", "speech therapist"),
        T("It is **Triangle Aphasia Connections**.", "group")),
      P("Why",
        T("To keep your **communication skills**.", "conversation"),
        T("To stay **social**.", "friends")),
      P("What they offer",
        T("**Conversation** groups.", "conversation"),
        T("A **book club**.", "book"),
        T("A **computer** class.", "computer")),
      P("When",
        T("**Tuesdays** and **Thursdays**.", "calendar"),
        T("**10:00 a.m.** to **12:00 p.m.**", "clock")),
      P("Cost",
        T("**$25** a month.", "money"),
        T("Help with cost (**scholarships**) is available.", "money"),
        T("Your **care partner** comes **free**.", "family")),
      P("Next step",
        T("They will **call you** within **2 weeks**.", "phone"),
        T("To plan a **30-minute** first visit.", "clock"),
        T("No call? **Call them**.", "phone"),
        PH("Phone: (919) 555-0163"))]),

# 8 ── Referral to a dietitian ──────────────────────────────────────────────────
pair("referral-dietitian-en-001", "en", "referral", "Referral to a dietitian (made-up example)",
     "REFERRAL: MEDICAL NUTRITION THERAPY\n"
     "Patient: Shirley Abernathy | Referring provider: Dr. Karen Liu | Diagnoses: hypertension, hyperlipidemia, history of "
     "stroke.\n"
     "Reason for referral: Education on a heart-healthy, low-sodium diet (less than 2,000 mg sodium per day) and weight "
     "management.\n"
     "Appointment: Wednesday, March 17, 2027 at 2:30 p.m. with Nadia Fontaine, RD, at Maple Ridge Family Medicine. Covered by "
     "most insurance plans when ordered by your doctor.\n"
     "Please bring: a 3-day food diary (everything you eat and drink), your medication list, and any food labels you have "
     "questions about. A family member who shops or cooks for you is encouraged to attend.\n"
     "To change your appointment, call (919) 555-0123.",
     "Meeting a dietitian",
     [P("Meeting a dietitian",
        T("For: **Shirley Abernathy**", "person"),
        T("**Dr. Karen Liu** wants you to see a **dietitian**.", "dietitian"),
        T("A dietitian helps with **food** and **health**.", "healthy food")),
      P("Why",
        T("To learn about **heart-healthy** eating.", "heart"),
        T("To eat **less salt**: under **2,000 mg** of **sodium** a day.", "salt"),
        T("To help with your **weight**.", "scale")),
      P("When and where",
        T("**Wednesday, March 17, 2027**", "calendar"),
        T("**2:30 p.m.**", "clock"),
        T("With **Nadia Fontaine, RD**", "dietitian"),
        T("At **Maple Ridge Family Medicine**.", "clinic")),
      P("Cost",
        T("Most **insurance** pays when your **doctor** orders it.", "insurance card")),
      P("What to bring",
        S("A **food diary** for **3 days**: everything you eat and drink.", "diary"),
        S("Your **medicine list**.", "medicine list"),
        S("**Food labels** you have questions about.", "food label")),
      P("Bring a helper",
        T("Does someone **shop** or **cook** for you?", "cooking"),
        T("**Bring them** too.", "family")),
      P("Change your visit",
        PH("Phone: (919) 555-0123"))],
     ["'A dietitian helps with food and health' adds a short plain explanation. Diagnoses (hypertension, hyperlipidemia) are not listed; the reasons page covers them."]),

# 9 ── Work status letter ───────────────────────────────────────────────────────
pair("letter-work-en-001", "en", "letter", "Work status letter (made-up example)",
     "WORK STATUS REPORT\n"
     "Patient: Anthony Russo | Employer: Harbor Freight Logistics | Provider: Dr. Ravi Patel, Neurology\n"
     "The patient is under my care following a stroke on 12/02/2026.\n"
     "Status: Off work until Monday, March 1, 2027. Then return to work with restrictions for 4 weeks: maximum 4 hours per "
     "day; no driving company vehicles; no operating heavy machinery; written instructions should be provided for new tasks; "
     "allow extra time for phone calls and emails.\n"
     "Restrictions will be reviewed at the next appointment on Monday, March 29, 2027 at 11:00 a.m.\n"
     "Please contact our office at (919) 555-0125 with questions. Employees may request reasonable accommodations under the "
     "Americans with Disabilities Act (ADA).",
     "Going back to work",
     [P("About your work",
        T("For: **Anthony Russo**", "person"),
        T("From **Dr. Ravi Patel**.", "doctor"),
        T("For your job at **Harbor Freight Logistics**.", "work")),
      P("Not working yet",
        T("**Do not work** until **Monday, March 1, 2027**.", "no work")),
      P("Going back slowly",
        T("Then go back with **limits** for **4 weeks**.", "calendar"),
        T("Work **4 hours** a day at most.", "clock")),
      P("Limits at work",
        T("**No driving** company vehicles.", "no driving"),
        T("**No heavy machines**.", "machine"),
        T("Get **written instructions** for **new tasks**.", "document"),
        T("Get **extra time** for **calls** and **emails**.", "clock")),
      P("Next visit",
        T("We will check your **limits** again.", "check"),
        T("**Monday, March 29, 2027**", "calendar"),
        T("**11:00 a.m.**", "clock")),
      P("Your rights",
        T("You can ask your **employer** for **changes** at work.", "work"),
        T("This is your right under the **ADA** law.", "law")),
      P("Questions?",
        PH("Phone: (919) 555-0125"))],
     ["'Reasonable accommodations under the ADA' became 'ask your employer for changes at work; this is your right under the ADA law'. Please confirm."],
     omitted=["Date of stroke 12/02/2026: past date"]),

# 10 ── Signing up for the patient portal ───────────────────────────────────────
pair("how-to-portal-en-001", "en", "how_to", "How to sign up for the patient portal (made-up example)",
     "SIGN UP FOR MYCHART\n"
     "With MyChart you can see test results, request prescription refills, and send messages to your care team.\n"
     "Your activation code: 7KQ2-MX4P-R9TD. This code expires on April 30, 2027.\n"
     "1. Go to www.example.org/mychart. 2. Click \"Sign Up Now.\" 3. Enter your activation code, your date of birth, and "
     "your ZIP code. 4. Create a username and password. Write them down and keep them in a safe place. 5. Choose a security "
     "question.\n"
     "A family member can get proxy access to help you manage your account; ask at the front desk for a proxy form.\n"
     "Do not use MyChart messages for emergencies. Call 911.\n"
     "Help with MyChart: (919) 555-0164, Monday to Friday, 8:00 a.m. to 5:00 p.m.",
     "Signing up for MyChart",
     [P("What is MyChart?",
        T("See your **test results**.", "computer"),
        T("Ask for **medicine refills**.", "pill bottle"),
        T("Send **messages** to your **care team**.", "message")),
      P("Your code",
        T("Your code: **7KQ2-MX4P-R9TD**", "key"),
        T("Use it before **April 30, 2027**.", "calendar")),
      P("Sign up",
        S("Go to **www.example.org/mychart**", "website"),
        S("Click **\"Sign Up Now.\"**", "click"),
        S("Type your **code**, **birthday** and **ZIP code**.", "keyboard")),
      P("Make your login",
        S("Make a **username** and **password**.", "password"),
        S("**Write them down**. Keep them **safe**.", "write"),
        S("Choose a **security question**.", "question")),
      P("Family can help",
        T("A **family member** can help with your account.", "family"),
        T("Ask the **front desk** for a **proxy form**.", "document")),
      P("Not for emergencies",
        T("Do **not** use messages for **emergencies**.", "no"),
        CR("Call 911")),
      P("Help with MyChart",
        T("**Monday** to **Friday**, **8:00 a.m.** to **5:00 p.m.**", "clock"),
        PH("Phone: (919) 555-0164"))]),
]

mark_reviewed(PAIRS, "CCC-SLP (anonymous)", "2026-11-12")
write(PAIRS, "batch4_en.jsonl")
