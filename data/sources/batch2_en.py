"""Batch 2 (English): 13 made-up pairs. All names, clinics, IDs and numbers are invented
(phones use 555-01xx; websites use example.org). Approved with no changes by a CCC-SLP (anonymous) on 2026-11-11.

Run:  python data/sources/batch2_en.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from batch2_helpers import B, C, CR, P, PH, S, T, mark_reviewed, pair, write  # noqa: E402

PAIRS = [
# 1 ── Metformin ────────────────────────────────────────────────────────────────
pair("medication-metformin-en-001", "en", "medication", "Metformin instructions (made-up example)",
     "Medication Instructions: Metformin 500 mg. Take 1 tablet by mouth twice daily with breakfast and dinner. Metformin "
     "helps lower blood sugar in type 2 diabetes. Taking it with food helps prevent an upset stomach. Your tablets are "
     "extended-release: do not crush or chew them. Check your blood sugar as your care team instructed. Before any test "
     "that uses contrast dye, stop taking metformin and call your doctor. Questions? Call Riverbend Pharmacy at (919) 555-0102.",
     "Your medicine: metformin",
     [P("Your medicine",
        T("Your medicine is **metformin 500 mg**.", "pill"),
        T("It **lowers** your **blood sugar**.", "blood sugar"),
        T("It is for **type 2 diabetes**.", "diabetes")),
      P("How to take it",
        T("Take **1 tablet**.", "pill"),
        T("**Twice** a day.", "calendar"),
        T("With **breakfast** and **dinner**.", "meal"),
        T("Swallow it **by mouth**.", "mouth")),
      P("Food helps",
        T("Take it with **food**.", "meal"),
        T("This helps your **stomach**.", "stomach")),
      P("Swallow it whole",
        T("Do **not crush** the tablet.", "crush pill"),
        T("Do **not chew** it.", "no chewing")),
      P("Check your blood sugar",
        T("Check your **blood sugar**.", "blood sugar test"),
        T("Do it the way your **care team** said.", "doctor")),
      P("Before some tests",
        T("A test with **contrast dye**?", "x-ray"),
        T("**Stop** metformin first.", "stop"),
        T("**Call** your **doctor**.", "doctor")),
      P("Questions?",
        T("Call **Riverbend Pharmacy**.", "pharmacy"),
        PH("Pharmacy: (919) 555-0102"))],
     ["'Extended-release' is not named on the handout; the page just says swallow it whole. Please confirm."]),

# 2 ── Medication schedule (fill-in form) ───────────────────────────────────────
pair("medication-schedule-en-001", "en", "medication", "Daily medication schedule form (made-up example)",
     "Daily Medication Schedule for: ____________. Updated on: ____________. Morning: medication ____________ dose "
     "____________. Midday: medication ____________ dose ____________. Evening: medication ____________ dose ____________. "
     "Bedtime: medication ____________ dose ____________. [ ] Take with food [ ] Take with a full glass of water "
     "[ ] Do not drive after taking. Bring this schedule and all your pill bottles to every appointment. "
     "Pharmacy phone: ____________.",
     "My medicine schedule",
     [P("My medicine schedule",
        B("For: ____________", "person"),
        B("Updated on: ____________", "calendar")),
      P("Morning",
        B("Medicine: ____________", "sunrise"),
        B("Dose: ____________", "pill")),
      P("Midday",
        B("Medicine: ____________", "sun"),
        B("Dose: ____________", "pill")),
      P("Evening",
        B("Medicine: ____________", "sunset"),
        B("Dose: ____________", "pill")),
      P("Bedtime",
        B("Medicine: ____________", "bed"),
        B("Dose: ____________", "pill")),
      P("Remember",
        C("Take with **food**.", "meal"),
        C("Take with a full glass of **water**.", "glass of water"),
        C("Do **not drive** after taking.", "no driving")),
      P("Bring to every visit",
        T("Bring this **schedule**.", "schedule"),
        T("Bring all your **pill bottles**.", "pill bottle"),
        B("Pharmacy phone: ____________", "phone"))],
     ["Fill-in form: the clinician or pharmacist writes the medicines and ticks the reminders."]),

# 3 ── Neurology appointment reminder ───────────────────────────────────────────
pair("appointment-neuro-en-003", "en", "appointment", "Neurology appointment reminder (made-up example)",
     "Appointment Reminder. You have a follow-up appointment with Dr. Hannah Brooks, Neurology, on Friday, April 9, 2027 "
     "at 2:45 p.m. Location: Westfield Medical Plaza, 600 Oakmont Drive, Suite 310. Park in the garage on Level 2 and bring "
     "your parking ticket to the front desk. Please bring your blood pressure log and a list of your current medications. "
     "If you need to cancel, please call at least 24 hours in advance: (919) 555-0103.",
     "Your appointment",
     [P("Your appointment",
        T("See **Dr. Hannah Brooks**.", "doctor"),
        T("She is in **Neurology**.", "brain"),
        T("**Friday, April 9, 2027**", "calendar"),
        T("**2:45 p.m.**", "clock")),
      P("Where",
        T("**Westfield Medical Plaza**", "hospital"),
        T("**600 Oakmont Drive, Suite 310**", "map")),
      P("Parking",
        T("Park in the **garage**.", "parking garage"),
        T("Go to **Level 2**.", "level"),
        T("Bring your **parking ticket** to the **front desk**.", "ticket")),
      P("What to bring",
        S("Your **blood pressure** log.", "blood pressure"),
        S("A **list** of your **medicines**.", "medicine list")),
      P("Need to cancel?",
        T("Call at least **24 hours** before.", "clock"),
        PH("Phone: (919) 555-0103"))],
     ["'She' assumes the doctor's pronoun; edit if needed."]),

# 4 ── Missed appointment ───────────────────────────────────────────────────────
pair("appointment-missed-en-001", "en", "appointment", "Missed appointment letter (made-up example)",
     "We Missed You. Our records show that you missed your speech therapy appointment on Monday, March 22, 2027. Regular "
     "attendance is important for your progress. Please call Piedmont Speech Clinic at (919) 555-0104 within 2 weeks to "
     "reschedule. If we do not hear from you, your referral may be closed and you may need a new referral from your doctor. "
     "If transportation is a problem, ask about our free ride program.",
     "We missed you",
     [P("You missed a visit",
        T("You **missed** your **speech therapy** visit.", "speech therapist"),
        T("**Monday, March 22, 2027**", "calendar")),
      P("Coming helps",
        T("Coming **every time** helps you **improve**.", "improve")),
      P("If you do not call",
        T("Your **referral** may be **closed**.", "closed"),
        T("You may need a **new referral** from your **doctor**.", "doctor")),
      P("Need a ride?",
        T("Ask about our **free ride** program.", "car")),
      P("Call us",
        T("**Call** to make a **new visit**.", "phone"),
        T("Call within **2 weeks**.", "calendar"),
        PH("Piedmont Speech Clinic: (919) 555-0104"))]),

# 5 ── Consent for recording ────────────────────────────────────────────────────
pair("consent-recording-en-001", "en", "consent", "Consent for audio and video recording (made-up example)",
     "Consent for Audio and Video Recording. During speech therapy, your therapist may record your sessions. Recordings help "
     "track your progress and may be used for training students. Recordings are stored securely and are not shared outside "
     "Piedmont Speech Clinic without your written permission. You may say no. Saying no will not affect your care. You may "
     "change your mind at any time by telling your therapist. Please choose: [ ] I agree to recording for tracking my progress. "
     "[ ] I agree to recording for training students. [ ] I do not agree to recording. Signature: ____________ "
     "Date: ____________",
     "Recording your therapy",
     [P("Recording your therapy",
        T("Your therapist may **record** your sessions.", "video camera"),
        T("**Sound** and **video**.", "microphone")),
      P("Why record?",
        T("To see your **progress**.", "chart"),
        T("To **teach** students.", "students")),
      P("Your recordings are safe",
        T("They are kept **safe**.", "lock"),
        T("They stay at **Piedmont Speech Clinic**.", "clinic"),
        T("Shared outside **only** if you say **yes** in writing.", "signature")),
      P("You choose",
        T("You can say **no**.", "no"),
        T("Saying no does **not change** your **care**.", "care"),
        T("You can **change your mind** any time.", "change"),
        T("Just tell your **therapist**.", "speech therapist")),
      P("Please choose",
        C("**Yes**, record me to see my **progress**.", "yes"),
        C("**Yes**, record me to **teach** students.", "yes"),
        C("**No**, do not record me.", "no")),
      P("Sign",
        B("Signature: ____________", "signature"),
        B("Date: ____________", "calendar"))],
     ["Consent form: the clinic's privacy or legal team should also approve the wording before use."]),

# 6 ── Insurance authorization ──────────────────────────────────────────────────
pair("insurance-approval-en-001", "en", "insurance", "Insurance authorization notice (made-up example)",
     "Notice of Authorization. Member: Robert Hayes. Member ID: XJH448213. Your health plan, Carolina Community Health Plan, "
     "has approved 12 outpatient speech therapy visits at Piedmont Speech Clinic. These visits must be used between "
     "January 4, 2027 and June 30, 2027. Your copay is $20 per visit. If you need more visits, your therapist must send a new "
     "request before your approved visits run out. If you have questions about your benefits, call Member Services at "
     "1-800-555-0105, TTY 711.",
     "Your therapy is approved",
     [P("Your therapy is approved",
        T("For: **Robert Hayes**", "person"),
        T("Member ID: **XJH448213**", "card"),
        T("Your **health plan** said **yes**.", "yes"),
        T("**Carolina Community Health Plan**", "insurance card")),
      P("How many visits",
        T("**12 speech therapy** visits.", "speech therapist"),
        T("At **Piedmont Speech Clinic**.", "clinic")),
      P("When",
        T("Use them between **January 4, 2027**", "calendar"),
        T("and **June 30, 2027**.", "calendar")),
      P("Cost",
        T("You pay **$20** each visit.", "money")),
      P("Need more visits?",
        T("Your **therapist** must **ask** for more.", "speech therapist"),
        T("Before your visits **run out**.", "calendar")),
      P("Questions?",
        T("Call **Member Services**.", "help"),
        PH("Phone: 1-800-555-0105"),
        PH("TTY: 711", "tty"))]),

# 7 ── Home program: word finding (checkbox) ────────────────────────────────────
pair("home-program-words-en-001", "en", "home_program", "Home program: word finding (made-up example)",
     "Home Program: Word Retrieval Practice. Complete the checked activities for 15 minutes, 5 days per week. "
     "[ ] Name 10 items in a category (e.g., foods, animals, clothing). [ ] Describe a photo out loud using 3 sentences. "
     "[ ] Practice your personal script daily. [ ] Read a short news story aloud and summarize it in 1 sentence. "
     "[ ] Use the naming app recommended by your therapist. [ ] Write a grocery list without help. Record your practice on "
     "the log sheet and bring it to your next session. Your therapist: ____________",
     "Practice finding words",
     [P("Practice at home",
        T("Practice finding **words** at home.", "practice"),
        T("**15 minutes** a day.", "clock"),
        T("**5 days** a week.", "calendar")),
      P("Do the checked activities",
        C("Name **10 things** in a group (foods, animals, clothes).", "food"),
        C("Describe a **photo** out loud in **3 sentences**.", "photo"),
        C("Practice your **script** every day.", "script")),
      P("More activities",
        C("Read a short **news story** out loud. Tell it in **1 sentence**.", "newspaper"),
        C("Use the **naming app** your therapist chose.", "phone app"),
        C("Write a **grocery list** without help.", "grocery list")),
      P("Keep track",
        T("Write your practice on the **log sheet**.", "log sheet"),
        T("**Bring** it to your next **session**.", "speech therapist"),
        B("Your therapist: ____________", "speech therapist"))]),

# 8 ── Cognitive-communication results (checkbox) ───────────────────────────────
pair("results-cognitive-en-001", "en", "results", "Cognitive-communication evaluation summary (made-up example)",
     "Cognitive-Communication Evaluation: Summary for ____________. Areas assessed: attention, memory, problem solving, and "
     "executive function (planning and organization). Findings: [ ] Reduced sustained attention [ ] Reduced short-term memory "
     "[ ] Difficulty with problem solving [ ] Difficulty with planning and organization [ ] Within normal limits. "
     "Recommendations: [ ] Use a calendar or planner daily [ ] Set phone alarms for medications [ ] Reduce distractions during "
     "conversations [ ] Supervision for managing finances [ ] Supervision for driving decisions; discuss with physician. "
     "Follow-up: cognitive-communication therapy ___ sessions per week.",
     "Your thinking skills results",
     [P("Your results",
        B("Results for: ____________", "person"),
        T("We tested your **attention**, **memory** and **problem solving**.", "brain"),
        T("And how you **plan** and **organize**.", "plan")),
      P("What we found",
        C("Hard to **pay attention** for a long time.", "attention"),
        C("Hard to **remember** new things.", "memory"),
        C("Hard to **solve problems**.", "puzzle"),
        C("Hard to **plan** and **organize**.", "plan"),
        C("Your results are **normal**.", "check mark")),
      P("Tips that help",
        C("Use a **calendar** or **planner** every day.", "calendar"),
        C("Set **phone alarms** for your **medicines**.", "alarm"),
        C("Turn off **noise** when you **talk**.", "quiet")),
      P("Get help with",
        C("**Money** and **bills**: get help.", "money"),
        C("**Driving**: get help to decide. Talk to your **doctor**.", "car")),
      P("Your therapy",
        B("Therapy: ___ times a week.", "calendar"))],
     ["'Reduce distractions during conversations' became 'Turn off noise when you talk'; please check this covers it.",
      "'Supervision' became 'get help'. Please confirm this is strong enough."]),

# 9 ── Discharge from speech therapy ────────────────────────────────────────────
pair("discharge-therapy-en-001", "en", "discharge", "Speech therapy discharge summary (made-up example)",
     "Discharge Summary: Outpatient Speech Therapy. Patient: Linda Marsh. Dates of service: September 8, 2026 to "
     "January 29, 2027. Total sessions: 32. Goals met: improved word finding in conversation; independent use of a "
     "communication notebook. Goal partially met: reading paragraphs. Recommendations: continue the home program 4 days per "
     "week; attend the Aphasia Café community group. Return to therapy if you notice new changes in your speech or language. "
     "To restart therapy, ask your doctor for a new referral or call (919) 555-0106.",
     "Your speech therapy is finished",
     [P("Therapy is finished",
        T("For: **Linda Marsh**", "person"),
        T("Your **speech therapy** is **finished**.", "finish"),
        T("From **September 8, 2026** to **January 29, 2027**.", "calendar"),
        T("You came **32 times**.", "calendar")),
      P("What you can do now",
        T("You **find words** better when you **talk**.", "conversation"),
        T("You use your **communication notebook** on your own.", "notebook")),
      P("Still working on",
        T("You are still working on **reading paragraphs**.", "read")),
      P("Keep going",
        T("Do your **home practice** **4 days** a week.", "practice"),
        T("Go to the **Aphasia Café** group.", "coffee")),
      P("Come back if",
        T("New **changes** in your **speech** or **language**?", "speech"),
        T("Ask your **doctor** for a **new referral**.", "doctor"),
        T("Or **call** us.", "phone"),
        PH("Phone: (919) 555-0106"))]),

# 10 ── What is aphasia ─────────────────────────────────────────────────────────
pair("education-aphasia-en-001", "en", "education", "Aphasia information for patients and families (made-up example)",
     "Aphasia: Information for Patients and Families. Aphasia is an acquired language disorder caused by damage to the language "
     "areas of the brain, most often from a stroke. It can affect speaking, understanding, reading, and writing. Aphasia does "
     "not affect intelligence. People with aphasia know what they want to say but may have trouble finding the words. "
     "Speech-language therapy can improve communication, and many people continue to improve for years. Communication "
     "partners can help by speaking slowly, using short sentences, writing key words, and allowing extra time. For more "
     "information, contact Piedmont Speech Clinic at (919) 555-0107.",
     "What is aphasia?",
     [P("What is aphasia?",
        T("Aphasia is a **language** problem.", "speech bubble"),
        T("It comes from **damage** to the **brain**.", "brain"),
        T("Most often from a **stroke**.", "stroke")),
      P("What it affects",
        T("**Speaking**", "talk"),
        T("**Understanding**", "listen"),
        T("**Reading**", "read"),
        T("**Writing**", "write")),
      P("You are still smart",
        T("Aphasia does **not** change how **smart** you are.", "brain"),
        T("You **know** what you want to say.", "idea"),
        T("Finding the **words** can be **hard**.", "search")),
      P("It can get better",
        T("**Speech therapy** can help.", "speech therapist"),
        T("Many people **improve** for **years**.", "improve")),
      P("How others can help",
        T("Speak **slowly**.", "slow"),
        T("Use **short** sentences.", "short"),
        T("**Write** key words.", "write"),
        T("Give **extra time**.", "clock")),
      P("More information",
        T("Call **Piedmont Speech Clinic**.", "clinic"),
        PH("Phone: (919) 555-0107"))]),

# 11 ── Anxiety after stroke ────────────────────────────────────────────────────
pair("mental-health-anxiety-en-001", "en", "mental_health", "Managing anxiety after a stroke (made-up example)",
     "Managing Anxiety After a Stroke. Anxiety, such as feeling worried, nervous, or panicky, is common after a stroke. "
     "Strategies that may help: slow breathing (breathe in for 4 counts, out for 6 counts), regular physical activity as "
     "approved by your doctor, keeping a daily routine, and talking with people you trust. Tell your doctor if anxiety makes "
     "it hard to sleep, eat, or do daily activities. Counseling is available through Oak Valley Counseling Center; call "
     "(919) 555-0108. If you are in crisis or thinking about suicide, call or text 988, the 988 Suicide & Crisis Lifeline.",
     "Feeling anxious after a stroke",
     [P("Feeling anxious",
        T("Many people feel **worried** after a **stroke**.", "worried"),
        T("Or **nervous**, or **panicky**.", "nervous"),
        T("This is **common**.", "group of people")),
      P("Slow breathing",
        S("Breathe **in**. Count to **4**.", "breathe in"),
        S("Breathe **out**. Count to **6**.", "breathe out")),
      P("Other things that help",
        T("**Move** your body, if your **doctor** says okay.", "walk"),
        T("Keep a **daily routine**.", "calendar"),
        T("**Talk** with people you **trust**.", "conversation")),
      P("Tell your doctor",
        T("Hard to **sleep**, **eat** or do **daily things**?", "bed"),
        T("**Tell** your **doctor**.", "doctor")),
      P("Counseling",
        T("You can talk to a **counselor**.", "counselor"),
        T("**Oak Valley Counseling Center**", "building"),
        PH("Phone: (919) 555-0108")),
      P("Help now",
        T("In **crisis**? Thinking about **suicide**?", "help"),
        CR("Call or text 988 — 988 Suicide & Crisis Lifeline", "phone"))]),

# 12 ── Carotid ultrasound ──────────────────────────────────────────────────────
pair("procedure-ultrasound-en-001", "en", "procedure", "Carotid ultrasound instructions (made-up example)",
     "Carotid Ultrasound: What to Expect. Your doctor ordered a carotid ultrasound to check blood flow in the arteries in your "
     "neck. The test is painless and uses sound waves, not radiation. It takes about 30 minutes. Wear a shirt with a loose "
     "collar and do not wear necklaces. You will lie on your back while a technician moves a small wand with gel over your "
     "neck. You can eat, drink, and take your medicines as usual. Your appointment: Thursday, March 11, 2027 at 8:15 a.m., "
     "Northgate Imaging Center, 4410 Pinecrest Parkway. Questions: (919) 555-0111.",
     "Your neck ultrasound",
     [P("Your neck ultrasound",
        T("Your doctor wants a **neck ultrasound**.", "ultrasound"),
        T("It checks **blood flow** in your **neck**.", "neck")),
      P("It does not hurt",
        T("The test does **not hurt**.", "no pain"),
        T("It uses **sound waves**.", "sound waves"),
        T("**No radiation**.", "no radiation")),
      P("When and where",
        T("**Thursday, March 11, 2027**", "calendar"),
        T("**8:15 a.m.**", "clock"),
        T("**Northgate Imaging Center**", "hospital"),
        T("**4410 Pinecrest Parkway**", "map")),
      P("What to wear",
        T("Wear a shirt with a **loose collar**.", "shirt"),
        T("**No necklaces**.", "no necklace")),
      P("During the test",
        T("You **lie on your back**.", "lie down"),
        T("A small **wand** with **gel** moves over your neck.", "ultrasound"),
        T("It takes about **30 minutes**.", "clock")),
      P("Food and medicine",
        T("You can **eat** and **drink**.", "eat"),
        T("Take your **medicines** as usual.", "pill")),
      P("Questions?",
        PH("Questions? Call (919) 555-0111"))],
     ["'Carotid' is not used on the handout; it says 'neck ultrasound'. Please confirm."]),

# 13 ── Preventing falls ────────────────────────────────────────────────────────
pair("education-falls-en-001", "en", "education", "Preventing falls at home after a stroke (made-up example)",
     "Preventing Falls at Home After a Stroke. Weakness, balance problems, and changes in vision can increase your risk of "
     "falling. To reduce your risk: remove throw rugs; keep walkways clear of cords and clutter; use night-lights in the "
     "bedroom, hallway, and bathroom; install grab bars near the toilet and in the shower; and wear shoes with non-slip "
     "soles. Use your cane or walker as your physical therapist taught you. If you fall and are hurt, or cannot get up, "
     "call 911.",
     "Stop falls at home",
     [P("Stop falls at home",
        T("After a stroke, falls are **more likely**.", "fall"),
        T("**Weakness**, **balance** problems and **vision** changes can cause falls.", "balance")),
      P("Clear the floor",
        T("**Remove** throw rugs.", "rug"),
        T("Keep walkways **clear**.", "hallway"),
        T("No **cords** or **clutter** on the floor.", "cord")),
      P("Light and grab bars",
        T("Use **night-lights**: bedroom, hallway, bathroom.", "night-light"),
        T("Put **grab bars** by the **toilet**.", "grab bar"),
        T("And in the **shower**.", "shower")),
      P("Walk safely",
        T("Wear shoes with **non-slip** soles.", "shoes"),
        T("Use your **cane** or **walker**.", "walker"),
        T("Use it the way your **therapist** taught you.", "physical therapist")),
      P("If you fall",
        T("Are you **hurt**?", "pain"),
        T("You **cannot get up**?", "fall"),
        CR("Call 911"))],
     ["'Install grab bars' became 'Put grab bars'."]),
]

mark_reviewed(PAIRS, "CCC-SLP (anonymous)", "2026-11-11")
write(PAIRS, "batch2_en.jsonl")
