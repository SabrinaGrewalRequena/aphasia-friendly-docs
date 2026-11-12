"""Batch 6: 25 made-up pairs reserved as the TEST SET (split="test"). These are never used for
training. They cover every document type and format in the project, in English (15) and
Spanish (10). All names, clinics, IDs and numbers are invented (phones use 555-01xx; websites
use example.org). Approved with no changes by a CCC-SLP (anonymous) on 2026-11-12.

Run:  python data/sources/batch6_test.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from batch2_helpers import B, C, CR, P, PH, S, T, mark_reviewed, pair as _pair, write  # noqa: E402,F401

TEL = "teléfono"
PHs = lambda t: PH(t, TEL)
CRs = lambda t: CR(t, "ambulancia")


def pair(*args, **kw):
    kw.setdefault("split", "test")
    return _pair(*args, **kw)


PAIRS = [
# ════════════════════════════ ENGLISH ════════════════════════════
# t1 ── Discharge after hemorrhagic stroke ──────────────────────────────────────
pair("test-discharge-hemorrhage-en", "en", "discharge", "Discharge instructions after bleeding stroke (made-up example)",
     "DISCHARGE INSTRUCTIONS — Carolina Valley Medical Center, Neuro ICU Step-Down\n"
     "Patient: Curtis Langley | DOB: 06/19/1955 | MRN: 01430667\n"
     "Diagnosis: Intracerebral hemorrhage (bleeding in the brain), right basal ganglia, due to uncontrolled hypertension.\n"
     "BLOOD PRESSURE GOAL: below 130/80. Check BP twice daily and record.\n"
     "MEDICATIONS: START amlodipine 10 mg by mouth once daily. START losartan 50 mg by mouth once daily. DO NOT take aspirin, "
     "ibuprofen, naproxen, or any blood thinner unless your neurologist says it is safe.\n"
     "ACTIVITY: No lifting over 10 pounds for 4 weeks. No driving until cleared.\n"
     "FOLLOW-UP: Neurosurgery Clinic, Dr. Nina Castellano, Wednesday, February 10, 2027 at 2:15 p.m. Repeat CT scan the same "
     "morning at 11:00 a.m.\n"
     "CALL 911 for: sudden severe headache, new weakness or numbness, trouble speaking, confusion, seizure, or vomiting with "
     "headache.\nQuestions: Neuro Nurse Line (919) 555-0174, 24 hours a day.",
     "Going home after your stroke",
     [P("You had a stroke",
        T("For: **Curtis Langley**", "person"),
        T("You had **bleeding** in your **brain**.", "brain"),
        T("It was on the **right side**.", "brain"),
        T("It happened because your **blood pressure** was **too high**.", "blood pressure")),
      P("Blood pressure goal",
        T("Keep it **below 130/80**.", "target"),
        T("Check it **twice** a day.", "blood pressure"),
        T("**Write it down**.", "write")),
      P("New medicines",
        T("**Start** amlodipine **10 mg**, by mouth, **once** a day.", "pill"),
        T("**Start** losartan **50 mg**, by mouth, **once** a day.", "pill")),
      P("Do not take",
        T("**No** aspirin, ibuprofen or naproxen.", "no pill"),
        T("**No** blood thinners.", "no pill"),
        T("Unless your **neurologist** says it is **safe**.", "doctor")),
      P("Activity",
        T("Do **not lift** more than **10 pounds**.", "lift"),
        T("For **4 weeks**.", "calendar"),
        T("**No driving** until your doctor says **okay**.", "no driving")),
      P("CT scan",
        T("**Wednesday, February 10, 2027**", "calendar"),
        T("CT scan at **11:00 a.m.**", "ct scan")),
      P("Neurosurgery visit",
        T("Same day, at **2:15 p.m.**", "clock"),
        T("See **Dr. Nina Castellano**.", "surgeon"),
        T("At the **Neurosurgery Clinic**.", "clinic")),
      P("Call 911",
        T("**Sudden**, very bad **headache**? **Vomiting** with headache?", "headache"),
        T("New **weakness** or **numbness**? Trouble **speaking**?", "weak arm"),
        T("**Confusion**? **Seizure**?", "confused"),
        CR("Call 911")),
      P("Questions?",
        T("**Neuro Nurse Line**, **24 hours** a day.", "nurse"),
        PH("Phone: (919) 555-0174"))],
     omitted=["DOB 06/19/1955: not needed by the reader", "MRN 01430667: record number",
              "Unit name Neuro ICU Step-Down and 'basal ganglia': hospital details"]),

# t2 ── Faxed OT referral ───────────────────────────────────────────────────────
pair("test-referral-ot-en", "en", "referral", "Faxed referral to occupational therapy (made-up example)",
     "REFERRAL — OUTPATIENT OCCUPATIONAL THERAPY\nTO: Lakeside Therapy Partners, fax (919) 555-0176 | FROM: Dr. Karen Liu, "
     "Maple Ridge Family Medicine\nPt: Shirley Abernathy, 71 yo F, hx L CVA 10/2026, R hand weakness, difficulty w/ "
     "buttons, writing, cooking. Goals: ↑ independence in ADLs (dressing, grooming, meal prep). Eval & treat, 2x/wk x 6 wks.\n"
     "Pt prefers morning appts. Pt's daughter will drive.\nClinic will call pt within 3 business days. Questions: "
     "(919) 555-0121.",
     "Your doctor sent you to occupational therapy",
     [P("Occupational therapy",
        T("For: **Shirley Abernathy**", "person"),
        T("**Dr. Karen Liu** sent you to **occupational therapy**.", "occupational therapy"),
        T("At **Lakeside Therapy Partners**.", "clinic")),
      P("Why",
        T("After your **stroke**, your **right hand** is **weak**.", "hand"),
        T("**Buttons**, **writing** and **cooking** are hard.", "buttons")),
      P("Your goals",
        T("Do more **on your own**.", "person"),
        T("**Dressing**, **grooming** and making **meals**.", "dressing")),
      P("How often",
        T("**2 times** a week.", "calendar"),
        T("For **6 weeks**.", "calendar"),
        T("**Morning** visits, like you asked.", "sunrise")),
      P("Next step",
        T("The clinic will **call you** within **3 business days**.", "phone"),
        PH("Questions: (919) 555-0121"))],
     ["'Pt's daughter will drive' is left out; please add a line if useful."],
     omitted=["Fax number (919) 555-0176: for the offices", "Age 71 yo F and stroke date 10/2026: office details",
              "Daughter will drive: arrangement already known to the reader"]),

# t3 ── Telehealth neurology follow-up ──────────────────────────────────────────
pair("test-appointment-video-en", "en", "appointment", "Video visit reminder for neurology (made-up example)",
     "VIDEO VISIT REMINDER — Carolina Valley Neurology\nPatient: Leon Fraser\nYour follow-up video visit with Dr. Ravi Patel "
     "is on Thursday, April 22, 2027 at 3:20 p.m.\nBEFORE YOUR VISIT: Download the free CareConnect app or use a web browser. "
     "Log in 15 minutes early to test your camera and microphone. Have your blood pressure log, medication bottles, and a list "
     "of questions ready. A family member may join you.\nIf the video does not work, the doctor will call you at the phone "
     "number we have on file.\nTechnical help: (919) 555-0177. To reschedule: (919) 555-0124.",
     "Your video visit",
     [P("Your video visit",
        T("For: **Leon Fraser**", "person"),
        T("A **video visit** with **Dr. Ravi Patel**.", "video call"),
        T("**Thursday, April 22, 2027**", "calendar"),
        T("**3:20 p.m.**", "clock")),
      P("Get ready",
        S("Get the free **CareConnect** app, or use a **web browser**.", "phone app"),
        S("Log in **15 minutes early**.", "clock"),
        S("Test your **camera** and **microphone**.", "camera")),
      P("Have these ready",
        T("Your **blood pressure** list.", "blood pressure"),
        T("Your **medicine bottles**.", "pill bottle"),
        T("Your **questions**.", "question"),
        T("A **family member** can join you.", "family")),
      P("Video not working?",
        T("The doctor will **call** your **phone** instead.", "phone"),
        PH("Technical help: (919) 555-0177")),
      P("Change your visit",
        PH("Phone: (919) 555-0124"))]),

# t4 ── New seizure medicine ────────────────────────────────────────────────────
pair("test-medication-levetiracetam-en", "en", "medication", "New seizure medicine instructions (made-up example)",
     "NEW MEDICATION: LEVETIRACETAM (KEPPRA) 500 MG TABLET\nPatient: Curtis Langley | Prescriber: Dr. Ravi Patel\n"
     "You had a seizure after your stroke. Levetiracetam helps prevent more seizures.\nHow to take: 1 tablet by mouth twice "
     "a day, about 12 hours apart (for example, 8 a.m. and 8 p.m.). Do not stop suddenly; stopping can cause seizures.\n"
     "Side effects: sleepiness, dizziness, and mood changes such as irritability or feeling down. Tell your doctor about mood "
     "changes. If you have thoughts of hurting yourself, call or text 988.\nSafety: Do not drive until your doctor says it is "
     "safe. Do not swim or bathe alone.\nCall 911 if a seizure lasts longer than 5 minutes, or if you have a second seizure "
     "without waking up in between.\nQuestions: (919) 555-0125.",
     "Your new medicine: levetiracetam",
     [P("Your new medicine",
        T("For: **Curtis Langley**", "person"),
        T("**Levetiracetam** (**Keppra**) **500 mg**", "pill"),
        T("From **Dr. Ravi Patel**.", "doctor")),
      P("Why you take it",
        T("You had a **seizure** after your stroke.", "seizure"),
        T("This medicine helps stop **more seizures**.", "shield")),
      P("How to take it",
        T("Take **1 tablet** by mouth.", "pill"),
        T("**Twice** a day, about **12 hours** apart.", "clock"),
        T("For example, **8 a.m.** and **8 p.m.**", "clock")),
      P("Do not stop suddenly",
        T("**Do not stop** this medicine **suddenly**.", "stop"),
        T("Stopping can cause **seizures**.", "seizure")),
      P("Side effects",
        T("You may feel **sleepy** or **dizzy**.", "sleepy"),
        T("Your **mood** may change: **irritable** or **down**.", "sad"),
        T("**Tell** your **doctor** about mood changes.", "doctor")),
      P("Thoughts of hurting yourself?",
        CR("Call or text 988", "phone")),
      P("Stay safe",
        T("**No driving** until your doctor says it is **safe**.", "no driving"),
        T("Do **not swim** or **bathe alone**.", "bath")),
      P("Call 911",
        T("Seizure **longer** than **5 minutes**?", "clock"),
        T("A **second** seizure **without waking up** in between?", "seizure"),
        CR("Call 911")),
      P("Questions?",
        PH("Phone: (919) 555-0125"))]),

# t5 ── Depression screening follow-up letter ───────────────────────────────────
pair("test-mental-health-depression-en", "en", "mental_health", "Depression screening follow-up letter (made-up example)",
     "Dear Mr. Bernard Okafor,\nAt your last visit, you answered questions about your mood using the SADQ-10, a depression "
     "checklist made for people with communication difficulties. Your answers suggest you may have depression. Depression is "
     "common after stroke and is treatable.\nDr. Karen Liu recommends: (1) a visit with a counselor at Oak Valley Counseling "
     "Center, which offers aphasia-friendly sessions; call (919) 555-0108; and (2) a follow-up visit with Dr. Liu in 4 weeks "
     "to talk about whether medicine could help.\nThe Aphasia Café on Saturdays at 10:00 a.m. may also help you feel less "
     "alone.\nIf you ever have thoughts of hurting yourself, call or text 988. In an emergency, call 911.",
     "About your mood",
     [P("About your mood",
        T("For: **Mr. Bernard Okafor**", "person"),
        T("You answered questions about your **mood**.", "mood"),
        T("Your answers show you may have **depression**.", "sad")),
      P("You are not alone",
        T("Depression is **common** after a **stroke**.", "group of people"),
        T("It can be **treated**.", "improve")),
      P("Talk to a counselor",
        T("**Oak Valley Counseling Center**", "building"),
        T("They make sessions **easy** for people with **aphasia**.", "counselor"),
        PH("Phone: (919) 555-0108")),
      P("See Dr. Liu again",
        T("See **Dr. Karen Liu** in **4 weeks**.", "doctor"),
        T("Talk about whether **medicine** could **help**.", "pill")),
      P("Aphasia Café",
        T("The **Aphasia Café** may help you feel **less alone**.", "coffee"),
        T("**Saturdays** at **10:00 a.m.**", "calendar")),
      P("Help now",
        T("Thinking about **hurting yourself**?", "help"),
        CR("Call or text 988", "phone"),
        CR("Emergency? Call 911"))],
     ["The name of the checklist (SADQ-10) is left out of the handout."],
     omitted=["SADQ-10: name of the screening checklist, not needed by the reader"]),

# t6 ── Swallow study results (checkbox) ────────────────────────────────────────
pair("test-results-mbss-en", "en", "results", "Swallow study results form (made-up example)",
     "MODIFIED BARIUM SWALLOW STUDY — RESULTS AND RECOMMENDATIONS for ____________\n"
     "Findings: [ ] Food or liquid went into the airway (aspiration) [ ] Food stayed in the throat after swallowing (residue) "
     "[ ] Delayed swallow [ ] Coughed when food went the wrong way [ ] Did not cough (silent aspiration) [ ] Swallow was safe "
     "for all foods and liquids.\n"
     "Diet: [ ] Regular [ ] Soft and bite-sized [ ] Minced and moist [ ] Pureed. Liquids: [ ] Thin [ ] Mildly thick "
     "[ ] Moderately thick.\n"
     "Strategies: [ ] Chin tuck when swallowing [ ] Swallow twice for each bite [ ] Small sips from a cup, no straws "
     "[ ] Alternate bites and sips.\nRepeat study in: ___ weeks. Speech therapist: ____________ Phone: ____________",
     "Your swallow study results",
     [P("Your swallow study",
        B("Results for: ____________", "person"),
        T("We watched you **swallow** on an **X-ray** video.", "x-ray")),
      P("What we saw",
        C("Food or drink went into your **airway**.", "lungs"),
        C("Food **stayed** in your **throat** after swallowing.", "throat"),
        C("Your swallow was **slow** to start.", "clock"),
        C("You **coughed** when food went the **wrong way**.", "cough"),
        C("You did **not cough** when food went the **wrong way**.", "no cough"),
        C("Your swallow was **safe** for **all** foods and drinks.", "check mark")),
      P("What to eat",
        C("**Regular** food", "plate of food"),
        C("**Soft** and **bite-sized**", "soft food"),
        C("**Minced** and **moist**", "minced food"),
        C("**Pureed**", "puree")),
      P("What to drink",
        C("**Thin** liquids", "glass of water"),
        C("**Mildly** thick liquids", "thick drink"),
        C("**Moderately** thick liquids", "thick drink")),
      P("Ways to swallow safely",
        C("**Tuck** your **chin** when you swallow.", "chin down"),
        C("Swallow **twice** for each bite.", "swallow"),
        C("**Small sips** from a cup. **No straws**.", "cup"),
        C("**Take turns**: a bite, then a sip.", "bite and sip")),
      P("Next steps",
        B("Do this test again in: ___ weeks", "calendar"),
        B("Speech therapist: ____________", "speech therapist"),
        B("Phone: ____________", "phone"))],
     ["The study name (modified barium swallow) is explained as 'an X-ray video'.",
      "'Silent aspiration' is written as 'you did not cough when food went the wrong way'. Please confirm."]),

# t7 ── General consent for treatment ───────────────────────────────────────────
pair("test-consent-treatment-en", "en", "consent", "Consent for outpatient therapy (made-up example)",
     "CONSENT FOR OUTPATIENT THERAPY SERVICES — Lakeside Therapy Partners\n"
     "I agree to receive evaluation and treatment by licensed therapists. I understand that therapy may involve physical "
     "activity, exercises, and practice of daily tasks, and that I may feel tired or sore. I understand that results are not "
     "guaranteed. I may ask questions at any time, refuse any part of treatment, or stop therapy at any time.\n"
     "Cancellation policy: Please cancel at least 24 hours before your visit. After 3 missed visits without notice, your "
     "remaining visits may be cancelled.\nI have received the Notice of Privacy Practices.\n"
     "[ ] I agree to treatment.\nPatient or representative signature: ____________ Date: ____________\n"
     "Questions: (919) 555-0121",
     "Agreeing to therapy",
     [P("Agreeing to therapy",
        T("You agree to **therapy** at **Lakeside Therapy Partners**.", "clinic"),
        T("Your therapists have a **license**.", "certificate")),
      P("What therapy is like",
        T("You will **move**, do **exercises** and **practice** daily tasks.", "exercise"),
        T("You may feel **tired** or **sore**.", "tired"),
        T("We **cannot promise** results.", "no promise")),
      P("Your choices",
        T("Ask **questions** any time.", "question"),
        T("Say **no** to any part.", "no"),
        T("**Stop** therapy any time.", "stop")),
      P("Cancelling",
        T("Cancel at least **24 hours** before.", "clock"),
        T("**3** missed visits without calling? Your **other visits** may be **cancelled**.", "calendar")),
      P("Privacy",
        T("You got the **privacy notice**.", "lock")),
      P("Sign",
        C("I **agree** to treatment.", "yes"),
        B("Signature: ____________", "signature"),
        B("Date: ____________", "calendar"),
        PH("Questions: (919) 555-0121"))],
     ["Consent form: the clinic's legal team should also approve the wording."]),

# t8 ── Explanation of benefits ─────────────────────────────────────────────────
pair("test-insurance-eob-en", "en", "insurance", "Explanation of benefits (made-up example)",
     "EXPLANATION OF BENEFITS — THIS IS NOT A BILL\nMember: Gloria Whitaker | Member ID: XJH227461 | Plan: Carolina "
     "Community Health Plan\nClaim: Outpatient speech therapy, Piedmont Speech Clinic, service date 01/19/2027\n"
     "Amount billed: $240.00 | Plan discount: -$95.00 | Plan paid: $125.00 | YOU MAY OWE: $20.00 (copay)\n"
     "The provider may send you a bill for the amount you may owe. Visits used this year: 7 of 30.\n"
     "Questions about this claim: Member Services 1-800-555-0105 (TTY 711).",
     "Insurance summary: not a bill",
     [P("This is NOT a bill",
        T("This paper is **not a bill**.", "no bill"),
        T("It shows what your **insurance** paid.", "insurance card"),
        T("For: **Gloria Whitaker**, Member ID **XJH227461**", "person")),
      P("Your visit",
        T("**Speech therapy** at **Piedmont Speech Clinic**.", "speech therapist")),
      P("The money",
        T("The clinic charged **$240.00**.", "bill"),
        T("Your plan took off **$95.00** and paid **$125.00**.", "insurance card"),
        T("You may owe **$20.00** (your **copay**).", "money")),
      P("What happens next",
        T("The clinic may **send you a bill** for **$20.00**.", "envelope")),
      P("Your visits this year",
        T("You used **7** of **30** visits.", "calendar")),
      P("Questions?",
        T("Call **Member Services**.", "phone"),
        PH("Phone: 1-800-555-0105"),
        PH("TTY: 711", "tty"))],
     omitted=["Service date 01/19/2027: past visit date"]),

# t9 ── Payment plan agreement ──────────────────────────────────────────────────
pair("test-billing-payment-plan-en", "en", "billing", "Payment plan agreement (made-up example)",
     "PAYMENT PLAN AGREEMENT — Carolina Valley Medical Center\nAccount: 4471-882-019 | Guarantor: Gloria Whitaker\n"
     "Balance: $1,500.00. Monthly payment: $125.00 for 12 months. No interest. First payment due: April 1, 2027; then on the "
     "1st of each month.\nIf a payment is more than 30 days late, the full balance may be sent to a collection agency. If your "
     "income changes, call us before you miss a payment; we can change your plan.\nPay online at www.example.org/paybill or "
     "call (919) 555-0135.\nSignature: ____________ Date: ____________",
     "Your payment plan",
     [P("Your payment plan",
        T("For: **Gloria Whitaker**", "person"),
        T("Account: **4471-882-019**", "card"),
        T("You owe **$1,500.00**.", "money")),
      P("How you pay",
        T("Pay **$125.00** each month.", "money"),
        T("For **12 months**.", "calendar"),
        T("**No interest**.", "no")),
      P("When",
        T("First payment: **April 1, 2027**.", "calendar"),
        T("Then on the **1st** of **each month**.", "calendar")),
      P("Late payments",
        T("More than **30 days** late?", "clock"),
        T("The **whole amount** may go to a **collection agency**.", "warning")),
      P("Money trouble?",
        T("Your **income changed**? **Call** before you miss a payment.", "phone"),
        T("We can **change** your plan.", "change")),
      P("Sign",
        B("Signature: ____________", "signature"),
        B("Date: ____________", "calendar")),
      P("How to pay",
        T("Online: **www.example.org/paybill**", "computer"),
        PH("Phone: (919) 555-0135"))]),

# t10 ── Using thickener ────────────────────────────────────────────────────────
pair("test-how-to-thickener-en", "en", "how_to", "How to thicken drinks (made-up example)",
     "HOW TO THICKEN DRINKS — MILDLY THICK\nYour speech therapist, Maria Ochoa, recommends mildly thick liquids for all drinks, "
     "including water, coffee, and soup broth.\n1. Pour 4 oz (120 mL) of your drink into a clean cup. 2. Add 1 scoop of "
     "ThickWell gel powder. 3. Stir with a fork for 30 seconds. 4. Wait 1 minute before drinking. 5. Check: it should pour "
     "slowly off a spoon, like nectar.\nDo not add extra powder. Do not use thin liquids, ice cream, or gelatin; they melt into "
     "thin liquid. Throw away thickened drinks after 2 hours at room temperature.\nQuestions: (919) 555-0131.",
     "Making drinks thicker",
     [P("Thick drinks",
        T("**Maria Ochoa**, your **speech therapist**, wants all drinks **mildly thick**.", "thick drink"),
        T("Even **water**, **coffee** and **soup broth**.", "cup")),
      P("How to make it",
        S("Pour **4 oz** (**120 mL**) into a clean **cup**.", "cup"),
        S("Add **1 scoop** of **ThickWell** gel powder.", "scoop"),
        S("**Stir** with a **fork** for **30 seconds**.", "stir")),
      P("Check it",
        S("**Wait 1 minute**.", "clock"),
        S("It should pour **slowly** off a spoon, like **nectar**.", "spoon")),
      P("Do not",
        T("Do **not** add **extra** powder.", "no"),
        T("**No thin** liquids.", "no glass of water"),
        T("**No ice cream** or **gelatin**: they **melt** into thin liquid.", "ice cream")),
      P("Throw it away",
        T("Throw away thick drinks after **2 hours** at **room temperature**.", "trash")),
      P("Questions?",
        PH("Phone: (919) 555-0131"))]),

# t11 ── Colonoscopy prep ───────────────────────────────────────────────────────
pair("test-procedure-colonoscopy-en", "en", "procedure", "Colonoscopy preparation (made-up example)",
     "COLONOSCOPY PREPARATION — Riverside GI Associates, 2100 Medical Park Drive, Suite 140\n"
     "Procedure: Monday, May 10, 2027. Arrive 8:00 a.m.\n"
     "5 DAYS BEFORE: Stop iron pills. Ask your neurologist before stopping clopidogrel; do not stop it on your own.\n"
     "1 DAY BEFORE: Clear liquids only all day (water, clear broth, apple juice, plain gelatin; nothing red or purple). "
     "At 6:00 p.m., drink the first half of the prep solution (1 liter) over 1 hour.\n"
     "DAY OF PROCEDURE: At 3:00 a.m., drink the second half (1 liter). Nothing by mouth after 4:00 a.m.\n"
     "You will receive sedation. An adult must drive you home. No driving for the rest of the day.\n"
     "Questions or to reschedule: (919) 555-0178.",
     "Getting ready for your colonoscopy",
     [P("Your colonoscopy",
        T("**Monday, May 10, 2027**", "calendar"),
        T("Arrive at **8:00 a.m.**", "clock"),
        T("**Riverside GI Associates**", "clinic"),
        T("**2100 Medical Park Drive, Suite 140**", "map")),
      P("5 days before",
        T("**Stop** iron pills.", "stop"),
        T("**Ask** your **neurologist** about clopidogrel.", "doctor"),
        T("Do **not** stop clopidogrel **on your own**.", "no")),
      P("1 day before: food",
        T("**Clear liquids only**, all day.", "glass of water"),
        T("**Water**, clear broth, **apple juice**, plain gelatin.", "apple juice"),
        T("**Nothing red** or **purple**.", "no")),
      P("1 day before: at 6:00 p.m.",
        T("Drink the **first half** of the prep (**1 liter**).", "bottle"),
        T("Drink it over **1 hour**.", "clock")),
      P("Day of the test",
        T("At **3:00 a.m.**, drink the **second half** (**1 liter**).", "bottle"),
        T("**Nothing** by mouth after **4:00 a.m.**", "no food")),
      P("Going home",
        T("You will get medicine to make you **sleepy**.", "sleepy"),
        T("An **adult** must **drive** you home.", "car"),
        T("**No driving** for the rest of the day.", "no driving")),
      P("Questions or changes",
        PH("Phone: (919) 555-0178"))],
     ["'Sedation' explained as 'medicine to make you sleepy'."]),

# t12 ── Low blood sugar ────────────────────────────────────────────────────────
pair("test-education-low-sugar-en", "en", "education", "Low blood sugar handout (made-up example)",
     "LOW BLOOD SUGAR (HYPOGLYCEMIA)\nLow blood sugar is a reading below 70 mg/dL. Signs include shaking, sweating, fast "
     "heartbeat, hunger, confusion, and trouble speaking. After a stroke, it can be hard to tell low blood sugar from stroke "
     "symptoms, so check your sugar.\nRULE OF 15: 1. Eat or drink 15 grams of fast sugar: 4 oz (half cup) of juice or regular "
     "soda, or 4 glucose tablets. 2. Wait 15 minutes. 3. Check again. 4. If still below 70, repeat. 5. When above 70, eat a "
     "snack or meal.\nIf the person cannot swallow safely or is not awake, do not give food or drink. Call 911.\n"
     "Call your diabetes team at (919) 555-0152 if you have low blood sugar more than 2 times in a week.",
     "Low blood sugar",
     [P("Low blood sugar",
        T("Low blood sugar is **below 70 mg/dL**.", "glucose meter")),
      P("Signs",
        T("**Shaking**, **sweating**, **fast heartbeat**.", "shaking"),
        T("**Hunger**, **confusion**, trouble **speaking**.", "confused"),
        T("These can look like a **stroke**. **Check** your sugar.", "glucose meter")),
      P("The rule of 15",
        S("Eat or drink **15 grams** of **fast sugar**.", "juice"),
        S("**Wait 15 minutes**.", "clock"),
        S("**Check** again.", "glucose meter")),
      P("Fast sugar ideas",
        T("**4 oz** (half cup) of **juice** or **regular soda**.", "juice"),
        T("Or **4 glucose tablets**.", "tablets")),
      P("After you check",
        S("Still **below 70**? **Repeat**.", "repeat"),
        S("**Above 70**? Eat a **snack** or **meal**.", "meal")),
      P("Emergency",
        T("Cannot **swallow** safely? Not **awake**?", "unconscious"),
        T("Do **not** give **food** or **drink**.", "no food"),
        CR("Call 911")),
      P("Call your diabetes team",
        T("Low sugar **more than 2 times** in a week?", "calendar"),
        PH("Phone: (919) 555-0152"))]),

# t13 ── Portal message about PT exercises ──────────────────────────────────────
pair("test-message-pt-en", "en", "message", "Portal message from a physical therapist (made-up example)",
     "From: Daniel Park, PT (Bright Path Home Health)\nTo: Dolores Pruitt\nSubject: your new exercises\n\n"
     "Hi Dolores! Great job this week. I added 2 new exercises to your home program. Here's the video link so your daughter "
     "can help: www.example.org/pt-video. Do each one 10 times, 2 times a day: (1) sit to stand from a firm chair WITHOUT "
     "using your hands, and (2) side steps holding the kitchen counter. Keep doing your walking with the walker 3 times a "
     "day. STOP if you feel dizzy or have chest pain. I'll see you Thursday at 1 p.m. Questions? Call the office at "
     "(919) 555-0131. - Daniel",
     "New exercises from your physical therapist",
     [P("New exercises",
        T("For: **Dolores Pruitt**", "person"),
        T("From **Daniel Park, PT**.", "physical therapist"),
        T("**Great job** this week!", "thumbs up")),
      P("Exercise: sit to stand",
        T("Sit on a **firm chair**.", "chair"),
        T("**Stand up** without using your **hands**.", "stand up"),
        T("**10 times**, **2 times** a day.", "calendar")),
      P("Exercise: side steps",
        T("Hold the **kitchen counter**.", "counter"),
        T("Take **side steps**.", "side step"),
        T("**10 times**, **2 times** a day.", "calendar")),
      P("Keep walking",
        T("Walk with your **walker** **3 times** a day.", "walker")),
      P("Video",
        T("Your **daughter** can watch the video and **help**.", "family"),
        T("**www.example.org/pt-video**", "video")),
      P("Stop if",
        T("You feel **dizzy** or have **chest pain**. **Stop**.", "stop")),
      P("Next visit",
        T("**Thursday** at **1 p.m.**", "calendar"),
        PH("Questions? Call (919) 555-0131"))]),

# t14 ── Urgent care visit summary ──────────────────────────────────────────────
pair("test-visit-summary-urgent-en", "en", "visit_summary", "Urgent care visit summary (made-up example)",
     "URGENT CARE VISIT SUMMARY — QuickCare Durham\nPatient: Walter Simmons | Visit: 02/27/2027\nDiagnosis: urinary tract "
     "infection (UTI).\nNEW MEDICINE: nitrofurantoin 100 mg capsule, 1 capsule by mouth twice a day with food for 5 days. "
     "Take all of it, even if you feel better.\nDrink plenty of water. Your urine may turn dark yellow or brown; this is normal "
     "with this medicine.\nWe sent a urine culture. We will call you only if you need a different antibiotic.\nGo to the "
     "emergency room if you have fever over 101°F with back pain, vomiting, or confusion.\nFollow up with your primary care "
     "doctor if not better in 3 days. QuickCare: (919) 555-0179.",
     "Your urgent care visit",
     [P("Your visit",
        T("For: **Walter Simmons**", "person"),
        T("You have a **bladder infection** (**UTI**).", "bladder")),
      P("New medicine",
        T("**Nitrofurantoin 100 mg**", "capsule"),
        T("Take **1 capsule** by mouth, **twice** a day, with **food**.", "capsule"),
        T("For **5 days**.", "calendar"),
        T("Take **all** of it, even if you feel **better**.", "check mark")),
      P("Good to know",
        T("Drink **plenty of water**.", "glass of water"),
        T("Your urine may turn **dark yellow** or **brown**. This is **normal**.", "toilet")),
      P("Urine test",
        T("We sent your urine to the **lab**.", "lab"),
        T("We will **call** only if you need a **different medicine**.", "phone")),
      P("Go to the emergency room",
        T("**Fever** over **101°F** with **back pain**?", "fever"),
        T("**Vomiting**? **Confusion**?", "vomit"),
        T("Go to the **emergency room**.", "hospital")),
      P("Not better?",
        T("Not better in **3 days**? See your **primary care** doctor.", "doctor"),
        PH("QuickCare: (919) 555-0179"))],
     ["'Urinary tract infection' written as 'bladder infection'. Please confirm.",
      "'Urine culture' written as 'we sent your urine to the lab'."],
     omitted=["Visit date 02/27/2027: today's date"]),

# t15 ── Reading home program (checkbox) ────────────────────────────────────────
pair("test-home-program-reading-en", "en", "home_program", "Home program: reading practice (made-up example)",
     "HOME PROGRAM: READING COMPREHENSION\nDo the checked activities for 20 minutes, 4 days per week.\n"
     "[ ] Match 10 written words to pictures. [ ] Read a short sentence and point to the matching picture. [ ] Read signs and "
     "labels in your kitchen and say what they mean. [ ] Read a menu and choose a meal. [ ] Read one short news story with "
     "a family member and answer 3 yes/no questions. [ ] Use the text-to-speech button on your tablet to check your reading.\n"
     "Use large print (at least 18 point). Keep a ruler or your finger under the line you are reading.\n"
     "Write your practice on the log and bring it to therapy. Therapist: ____________",
     "Reading practice at home",
     [P("Reading practice",
        T("Practice **reading** at home.", "read"),
        T("**20 minutes** a day.", "clock"),
        T("**4 days** a week.", "calendar")),
      P("Do the checked activities",
        C("Match **10 words** to **pictures**.", "picture cards"),
        C("Read a **short sentence**. **Point** to the picture.", "point"),
        C("Read **signs** and **labels** in your **kitchen**.", "kitchen")),
      P("More activities",
        C("Read a **menu** and **choose** a meal.", "menu"),
        C("Read a **news story** with **family**. Answer **3** yes/no questions.", "newspaper"),
        C("Use **text-to-speech** on your **tablet** to check.", "tablet")),
      P("Tips",
        T("Use **large print**: at least **18 point**.", "large print"),
        T("Keep a **ruler** or your **finger** under the line.", "ruler")),
      P("Keep track",
        T("Write your practice on the **log**.", "log sheet"),
        T("**Bring** it to **therapy**.", "speech therapist"),
        B("Therapist: ____________", "speech therapist"))]),

# ════════════════════════════ SPANISH ════════════════════════════
# t16 ── Alta tras fractura de muñeca ───────────────────────────────────────────
pair("test-alta-fractura-es", "es", "discharge", "Instrucciones de alta por fractura de muñeca (ejemplo inventado)",
     "INSTRUCCIONES DE ALTA — Emergencias, Hospital Comunitario San Marcos\nPaciente: Guadalupe Torres | Expediente: "
     "01127748\nDiagnóstico: fractura de la muñeca izquierda después de una caída. Se le puso una férula.\nCUIDADOS: Mantenga "
     "el brazo levantado sobre una almohada. Ponga hielo envuelto en una toalla 20 minutos cada 2 horas. No moje la férula; "
     "cúbrala con una bolsa para bañarse. Mueva los dedos con frecuencia.\nDOLOR: acetaminofén 500 mg, 2 tabletas cada 6 "
     "horas si lo necesita. No más de 3,000 mg en 24 horas.\nSEGUIMIENTO: Clínica de Ortopedia, Dr. Alan Brooks, lunes 15 de "
     "marzo de 2027 a las 10:00 a.m.\nREGRESE A EMERGENCIAS si los dedos están fríos, azules, entumidos o muy hinchados, o si "
     "el dolor empeora mucho.\nCaídas: pida a su médico una evaluación para prevenir caídas. Preguntas: (919) 555-0180.",
     "Su muñeca fracturada",
     [P("Su muñeca",
        T("Para: **Guadalupe Torres**", "persona"),
        T("Se **fracturó** la **muñeca izquierda** en una caída.", "muñeca"),
        T("Le pusieron una **férula**.", "férula")),
      P("Cuidados",
        T("Ponga el brazo **arriba**, sobre una **almohada**.", "almohada"),
        T("**Hielo** envuelto en una toalla, **20 minutos** cada **2 horas**.", "hielo"),
        T("Mueva los **dedos** seguido.", "dedos")),
      P("No moje la férula",
        T("**No moje** la férula.", "no agua"),
        T("Para bañarse, **cúbrala** con una **bolsa**.", "bolsa")),
      P("Para el dolor",
        T("**Acetaminofén 500 mg**, **2 tabletas**.", "pastilla"),
        T("Cada **6 horas**, si lo necesita.", "reloj"),
        T("**No más** de **3,000 mg** en **24 horas**.", "advertencia")),
      P("Su cita",
        T("**Clínica de Ortopedia**, **Dr. Alan Brooks**", "médico"),
        T("**lunes 15 de marzo de 2027**", "calendario"),
        T("**10:00 a.m.**", "reloj")),
      P("Regrese a Emergencias",
        T("¿Dedos **fríos**, **azules** o **entumidos**?", "dedos"),
        T("¿Muy **hinchados**? ¿El dolor **empeora** mucho?", "dolor"),
        T("**Regrese** a **Emergencias**.", "hospital")),
      P("Prevenir caídas",
        T("Pida a su **médico** una evaluación para **prevenir caídas**.", "caída"),
        PHs("Preguntas: (919) 555-0180"))],
     omitted=["Expediente 01127748: número de registro"]),

# t17 ── Visita anual de bienestar ──────────────────────────────────────────────
pair("test-cita-bienestar-es", "es", "appointment", "Recordatorio de visita anual de bienestar (ejemplo inventado)",
     "RECORDATORIO: VISITA ANUAL DE BIENESTAR DE MEDICARE\nPaciente: Alberto Ruiz\nSu visita anual de bienestar es el "
     "martes 20 de abril de 2027 a las 8:00 a.m. con la Dra. Ana Morales, Clínica Familiar Las Palmas. Esta visita no tiene "
     "costo para usted con Medicare.\nEn la visita: revisaremos sus medicamentos, su memoria, su riesgo de caídas y sus "
     "vacunas. Puede recibir la vacuna de la gripe y la del neumococo ese día.\nTraiga: todos sus frascos de medicinas, sus "
     "lentes y audífonos, y la lista de sus otros médicos. Su hijo puede venir con usted.\nNo necesita estar en ayunas.\nPara "
     "cambiar la cita: (919) 555-0144.",
     "Su visita anual",
     [P("Su visita anual",
        T("Para: **Alberto Ruiz**", "persona"),
        T("Con la **Dra. Ana Morales**.", "doctora"),
        T("En la **Clínica Familiar Las Palmas**.", "clínica"),
        T("**No cuesta** nada con **Medicare**.", "gratis")),
      P("Cuándo",
        T("**martes 20 de abril de 2027**", "calendario"),
        T("**8:00 a.m.**", "reloj"),
        T("**Puede comer** antes.", "comer")),
      P("Qué revisamos",
        T("Sus **medicinas** y su **memoria**.", "pastillas"),
        T("Su riesgo de **caídas**.", "caída"),
        T("Sus **vacunas**.", "vacuna")),
      P("Vacunas",
        T("Puede recibir la vacuna de la **gripe**.", "vacuna"),
        T("Y la del **neumococo**.", "vacuna")),
      P("Qué traer",
        S("**Todos** sus **frascos** de medicinas.", "frasco de pastillas"),
        S("Sus **lentes** y **audífonos**.", "lentes"),
        S("La **lista** de sus otros **médicos**.", "lista")),
      P("Puede venir acompañado",
        T("Su **hijo** puede venir con usted.", "familia")),
      P("Cambiar la cita",
        PHs("Teléfono: (919) 555-0144"))],
     ["'No necesita estar en ayunas' se escribió como 'Puede comer antes'."]),

# t18 ── Prednisona en disminución ──────────────────────────────────────────────
pair("test-medicamento-prednisona-es", "es", "medication", "Instrucciones de prednisona con dosis que bajan (ejemplo inventado)",
     "PREDNISONA 10 MG TABLETAS — DOSIS QUE BAJA POCO A POCO\nPaciente: Teresa Campos | Médico: Dr. Tomás Aguilar\n"
     "Tome las tabletas por la boca cada mañana con el desayuno:\n"
     "| Días | Tabletas cada mañana | Dosis |\n| Días 1 a 3 | 4 tabletas | 40 mg |\n| Días 4 a 6 | 3 tabletas | 30 mg |\n"
     "| Días 7 a 9 | 2 tabletas | 20 mg |\n| Días 10 a 12 | 1 tableta | 10 mg |\nLuego pare.\n"
     "No deje de tomarla de repente. Puede subir su azúcar en la sangre; si tiene diabetes, revise su azúcar 2 veces al día. "
     "Puede causar problemas para dormir y cambios de humor.\nLlame al (919) 555-0144 si su azúcar pasa de 300 o tiene "
     "fiebre.",
     "Su prednisona: la dosis baja poco a poco",
     [P("Su medicina",
        T("Para: **Teresa Campos**", "persona"),
        T("**Prednisona 10 mg**, tabletas", "pastilla"),
        T("Del **Dr. Tomás Aguilar**.", "médico"),
        T("Tómela cada **mañana** con el **desayuno**, por la boca.", "desayuno")),
      P("Días 1 a 3",
        T("**4 tabletas** cada mañana (**40 mg**).", "pastilla")),
      P("Días 4 a 6",
        T("**3 tabletas** cada mañana (**30 mg**).", "pastilla")),
      P("Días 7 a 9",
        T("**2 tabletas** cada mañana (**20 mg**).", "pastilla")),
      P("Días 10 a 12",
        T("**1 tableta** cada mañana (**10 mg**).", "pastilla"),
        T("Luego **pare**.", "parar")),
      P("Importante",
        T("**No deje** de tomarla de **repente**.", "no parar"),
        T("Puede **subir** su **azúcar**.", "glucómetro"),
        T("¿Tiene **diabetes**? Revise su azúcar **2 veces** al día.", "glucómetro"),
        T("Puede causar problemas para **dormir** y cambios de **humor**.", "cama")),
      P("Llame",
        T("¿Azúcar de **más de 300**? ¿**Fiebre**?", "termómetro"),
        PHs("Teléfono: (919) 555-0144"))],
     ["Cada paso de la dosis tiene su propia página; marque los días en un calendario puede ayudar (no está en el original)."]),

# t19 ── Ansiedad y apoyo ───────────────────────────────────────────────────────
pair("test-salud-mental-ansiedad-es", "es", "mental_health", "Ansiedad después de un derrame (ejemplo inventado)",
     "LA ANSIEDAD DESPUÉS DE UN DERRAME CEREBRAL\nMuchas personas sienten nervios, preocupación o miedo después de un derrame. "
     "Con la afasia, puede dar ansiedad hablar con otros o contestar el teléfono.\nLo que puede ayudar: respirar despacio "
     "(inhale contando 4, exhale contando 6); tener una tarjeta que diga \"Tengo afasia. Por favor hable despacio\"; practicar "
     "conversaciones con su terapeuta del habla; y hablar con un consejero.\nEl Centro de Consejería Oak Valley tiene "
     "consejeros que hablan español: (919) 555-0160.\nSi piensa en hacerse daño, llame o envíe un mensaje de texto al 988. "
     "Si está en peligro, llame al 911.",
     "La ansiedad después de un derrame",
     [P("Sentir nervios",
        T("Muchas personas sienten **nervios** o **miedo** después de un **derrame**.", "nervioso"),
        T("Con **afasia**, hablar o contestar el **teléfono** puede dar **ansiedad**.", TEL)),
      P("Respire despacio",
        S("**Inhale** contando hasta **4**.", "inhalar"),
        S("**Exhale** contando hasta **6**.", "exhalar")),
      P("Una tarjeta",
        T("Lleve una **tarjeta** que diga:", "tarjeta"),
        T("**\"Tengo afasia. Por favor hable despacio.\"**", "tarjeta")),
      P("Más ayuda",
        T("Practique **conversaciones** con su **terapeuta del habla**.", "terapeuta del habla"),
        T("Hable con un **consejero**.", "consejero")),
      P("Consejería en español",
        T("**Centro de Consejería Oak Valley**", "edificio"),
        PHs("Teléfono: (919) 555-0160")),
      P("Ayuda ahora",
        T("¿Piensa en **hacerse daño**?", "ayuda"),
        CR("Llame o envíe un mensaje de texto al 988", TEL),
        CRs("¿Está en peligro? Llame al 911"))]),

# t20 ── Resultados de resonancia ───────────────────────────────────────────────
pair("test-resultados-resonancia-es", "es", "results", "Carta de resultados de resonancia (ejemplo inventado)",
     "Estimada Sra. Esperanza Vidal:\nLa Dra. Lucía Herrera revisó su resonancia magnética del cerebro del 11/02/2027.\n"
     "Resultado: Se ve el área del derrame cerebral que tuvo en enero, en el lado izquierdo. No hay derrames nuevos. No hay "
     "sangrado. Las arterias del cuello se ven bien.\nQué significa: su tratamiento está funcionando. Siga tomando el "
     "clopidogrel 75 mg y la atorvastatina 40 mg igual.\nSu próxima cita es el viernes 9 de abril de 2027 a las 11:30 a.m.\n"
     "Si tiene preguntas, llame al (919) 555-0145.",
     "Sus resultados de la resonancia",
     [P("Sus resultados",
        T("Para: **Sra. Esperanza Vidal**", "persona"),
        T("La **Dra. Lucía Herrera** revisó su **resonancia** del **cerebro**.", "resonancia magnética")),
      P("Lo que se ve",
        T("Se ve el área del **derrame** de **enero**, en el lado **izquierdo**.", "cerebro"),
        T("**No** hay derrames **nuevos**.", "bien"),
        T("**No** hay **sangrado**.", "bien"),
        T("Las **arterias** del cuello se ven **bien**.", "cuello")),
      P("Qué significa",
        T("Su tratamiento está **funcionando**.", "pulgar arriba")),
      P("Sus medicinas",
        T("Siga tomando **clopidogrel 75 mg** igual.", "pastilla"),
        T("Siga tomando **atorvastatina 40 mg** igual.", "pastilla")),
      P("Próxima cita",
        T("**viernes 9 de abril de 2027**", "calendario"),
        T("**11:30 a.m.**", "reloj")),
      P("¿Preguntas?",
        PHs("Teléfono: (919) 555-0145"))],
     omitted=["Fecha de la resonancia 11/02/2027: fecha pasada"]),

# t21 ── Renovación de Medicaid ─────────────────────────────────────────────────
pair("test-seguro-renovacion-es", "es", "insurance", "Carta de renovación de Medicaid (ejemplo inventado)",
     "AVISO DE RENOVACIÓN DE MEDICAID — ACCIÓN REQUERIDA\nMiembro: Carmen Ruiz | Número de caso: 7730-551\nEs hora de "
     "renovar su Medicaid. Si no renueva antes del 31 de mayo de 2027, su cobertura puede terminar.\nCómo renovar: en línea en "
     "www.example.org/renovar, por teléfono al 1-800-555-0182, o en persona en el Departamento de Servicios Sociales del "
     "Condado, 300 Elm Street.\nEnvíe: comprobante de ingresos de los últimos 30 días (talones de pago o carta del Seguro "
     "Social) y comprobante de domicilio (factura de luz o contrato de renta).\nSi necesita ayuda por su afasia, puede pedir "
     "que alguien de su confianza le ayude o pedir una cita con un trabajador de casos.",
     "Renueve su Medicaid",
     [P("Renueve su Medicaid",
        T("Para: **Carmen Ruiz**", "persona"),
        T("Número de caso: **7730-551**", "tarjeta"),
        T("Es hora de **renovar** su **Medicaid**.", "formulario")),
      P("Fecha límite",
        T("Renueve antes del **31 de mayo de 2027**.", "calendario"),
        T("Si no, su **cobertura** puede **terminar**.", "advertencia")),
      P("Qué enviar",
        T("Prueba de **ingresos** de los últimos **30 días**.", "dinero"),
        T("Como **talones de pago** o carta del **Seguro Social**.", "documento"),
        T("Prueba de **domicilio**: factura de **luz** o contrato de **renta**.", "casa")),
      P("Ayuda con la afasia",
        T("Alguien de su **confianza** le puede **ayudar**.", "familia"),
        T("O pida una cita con un **trabajador de casos**.", "trabajadora social")),
      P("Dónde, en persona",
        T("**Departamento de Servicios Sociales** del **Condado**", "edificio")),
      P("Cómo renovar",
        S("**En línea**: www.example.org/renovar", "computadora"),
        S("Por **teléfono**.", TEL),
        S("En persona: **300 Elm Street**.", "edificio"),
        PHs("Teléfono: 1-800-555-0182"))],
     ["La dirección '300 Elm Street' no tiene ciudad en el original."]),

# t22 ── Cómo usar el inhalador ─────────────────────────────────────────────────
pair("test-como-inhalador-es", "es", "how_to", "Cómo usar el inhalador (ejemplo inventado)",
     "CÓMO USAR SU INHALADOR CON ESPACIADOR\nMedicina: albuterol, 2 inhalaciones cada 4 a 6 horas si le falta el aire.\n"
     "1. Agite el inhalador 5 veces. 2. Ponga el inhalador en el espaciador. 3. Saque todo el aire de sus pulmones. 4. Ponga "
     "la boquilla en su boca y cierre bien los labios. 5. Oprima el inhalador una vez. 6. Respire lento y profundo. 7. "
     "Aguante la respiración 10 segundos. 8. Espere 1 minuto y repita para la segunda inhalación.\nLave el espaciador una vez "
     "por semana con agua y jabón; déjelo secar al aire.\nLlame al 911 si le falta mucho el aire, tiene los labios azules o "
     "no puede hablar por la falta de aire. Preguntas: Farmacia Central (919) 555-0154.",
     "Cómo usar su inhalador",
     [P("Su inhalador",
        T("Medicina: **albuterol**.", "inhalador"),
        T("**2 inhalaciones** cada **4 a 6 horas**.", "reloj"),
        T("Solo si le **falta el aire**.", "respirar")),
      P("Prepare",
        S("**Agite** el inhalador **5 veces**.", "agitar"),
        S("Póngalo en el **espaciador**.", "espaciador"),
        S("Saque **todo el aire** de sus pulmones.", "exhalar")),
      P("Use",
        S("Boquilla en la **boca**. Cierre bien los **labios**.", "boca"),
        S("**Oprima** el inhalador **una vez**.", "oprimir"),
        S("Respire **lento** y **profundo**.", "inhalar")),
      P("Termine",
        S("**Aguante** la respiración **10 segundos**.", "reloj"),
        S("Espere **1 minuto**. **Repita** una vez más.", "repetir")),
      P("Limpieza",
        T("Lave el **espaciador** una vez por **semana**.", "lavar"),
        T("Con **agua** y **jabón**. Déjelo **secar** al aire.", "secar")),
      P("Emergencia",
        T("¿Le falta **mucho** el aire? ¿Labios **azules**?", "respirar"),
        T("¿No puede **hablar** por la falta de aire?", "hablar"),
        CRs("Llame al 911")),
      P("¿Preguntas?",
        T("**Farmacia Central**", "farmacia"),
        PHs("Teléfono: (919) 555-0154"))]),

# t23 ── Plan de terapia ocupacional ────────────────────────────────────────────
pair("test-plan-to-es", "es", "therapy_plan", "Plan de terapia ocupacional (ejemplo inventado)",
     "PLAN DE CUIDADO — TERAPIA OCUPACIONAL\nLakeside Therapy Partners | Paciente: Jorge Castillo | Terapeuta: Luis Romero, "
     "OTR/L\nDiagnóstico: debilidad del lado derecho después de un derrame cerebral (I69.351).\nMETAS (8 semanas): (1) Vestirse "
     "la parte de arriba sin ayuda. (2) Abotonar una camisa en menos de 3 minutos. (3) Preparar un sándwich de forma segura. "
     "(4) Escribir su nombre de forma que se pueda leer.\nFRECUENCIA: 2 veces por semana por 8 semanas.\nTRATAMIENTO: "
     "ejercicios para la mano, práctica de tareas diarias, y enseñar a la familia.\nFirma del médico: ____________",
     "Su plan de terapia ocupacional",
     [P("Su plan de terapia",
        T("Para: **Jorge Castillo**", "persona"),
        T("Terapeuta: **Luis Romero, OTR/L**", "terapia ocupacional"),
        T("En **Lakeside Therapy Partners**.", "clínica"),
        T("Su lado **derecho** está **débil** por el **derrame**.", "brazo débil")),
      P("Meta 1 y meta 2",
        T("**Vestirse** la parte de arriba **sin ayuda**.", "camisa"),
        T("**Abotonar** una camisa en menos de **3 minutos**.", "botones")),
      P("Meta 3 y meta 4",
        T("Preparar un **sándwich** de forma **segura**.", "sándwich"),
        T("**Escribir** su nombre para que se pueda **leer**.", "escribir")),
      P("Cada cuánto",
        T("**2 veces** por semana.", "calendario"),
        T("Por **8 semanas**.", "calendario")),
      P("Qué va a hacer",
        T("**Ejercicios** para la **mano**.", "mano"),
        T("Practicar **tareas diarias**.", "práctica"),
        T("Su **familia** aprende a **ayudar**.", "familia"))],
     omitted=["Código I69.351: código de facturación", "Línea de firma del médico: para el médico"]),

# t24 ── Referido a rehabilitación cardíaca ─────────────────────────────────────
pair("test-referido-cardiaca-es", "es", "referral", "Referido a rehabilitación cardíaca (ejemplo inventado)",
     "REFERIDO A REHABILITACIÓN CARDÍACA\nPaciente: Héctor Navarro | Médico: Dr. Pablo Serrano, Cardiología\nMotivo: "
     "fibrilación auricular y derrame cerebral reciente. Programa de ejercicio supervisado para el corazón.\nPrograma: 3 "
     "sesiones por semana por 12 semanas, en el Centro de Rehabilitación Cardíaca San Marcos, 2do piso. Cada sesión dura 1 "
     "hora: ejercicio con monitor del corazón y clases sobre alimentación y medicinas.\nUse ropa y zapatos cómodos. Coma algo "
     "ligero 1 a 2 horas antes. Traiga su lista de medicinas.\nEl programa lo llamará en 1 semana. Si no lo llaman: "
     "(919) 555-0183.",
     "Ejercicio para su corazón",
     [P("Rehabilitación cardíaca",
        T("Para: **Héctor Navarro**", "persona"),
        T("El **Dr. Pablo Serrano** lo refirió.", "médico"),
        T("Es **ejercicio** con **supervisión** para su **corazón**.", "corazón")),
      P("Por qué",
        T("Usted tiene **fibrilación auricular**.", "corazón"),
        T("Y tuvo un **derrame cerebral** hace poco.", "cerebro")),
      P("El programa",
        T("**3 sesiones** por semana, por **12 semanas**.", "calendario"),
        T("Cada sesión dura **1 hora**.", "reloj"),
        T("**Centro de Rehabilitación Cardíaca San Marcos**, **2do piso**", "edificio")),
      P("En cada sesión",
        T("**Ejercicio** con un **monitor** del corazón.", "monitor cardíaco"),
        T("**Clases** sobre **comida** y **medicinas**.", "clase")),
      P("Antes de cada sesión",
        T("Use ropa y zapatos **cómodos**.", "zapatos"),
        T("Coma algo **ligero** **1 a 2 horas** antes.", "comida"),
        T("Traiga su **lista** de **medicinas**.", "lista de medicamentos")),
      P("Lo van a llamar",
        T("El programa lo llamará en **1 semana**.", TEL),
        T("¿No lo llamaron? **Llame** usted.", TEL),
        PHs("Teléfono: (919) 555-0183"))]),

# t25 ── Mensaje de voz de la farmacia ──────────────────────────────────────────
pair("test-buzon-farmacia-es", "es", "message", "Mensaje de voz de la farmacia (ejemplo inventado)",
     "[Transcripción de mensaje de voz, 4:05 PM] \"Buenas tardes, este mensaje es para Marisol Vega, de la Farmacia "
     "Central. Su receta de empagliflozina 10 mg ya está lista. Eh, el seguro la cubrió y su copago es de $15. La puede "
     "recoger hoy hasta las 9:00 p.m. o mañana desde las 8:00 a.m. Si prefiere que se la mandemos a su casa, el envío es "
     "gratis, nada más llámenos. Recuerde traer su identificación. Nuestro número es el (919) 555-0154. Gracias.\"",
     "Su medicina está lista",
     [P("Su medicina está lista",
        T("Para: **Marisol Vega**", "persona"),
        T("Llamó la **Farmacia Central**.", "farmacia"),
        T("Su **empagliflozina 10 mg** está **lista**.", "pastilla")),
      P("Costo",
        T("El seguro la **cubrió**.", "tarjeta de seguro"),
        T("Usted paga **$15**.", "dinero")),
      P("Cuándo recogerla",
        T("**Hoy**, hasta las **9:00 p.m.**", "reloj"),
        T("O **mañana**, desde las **8:00 a.m.**", "reloj"),
        T("Traiga su **identificación**.", "identificación")),
      P("Envío a su casa",
        T("Se la pueden **mandar** a su casa **gratis**.", "casa"),
        T("**Llame** para pedirlo.", TEL),
        PHs("Farmacia Central: (919) 555-0154"))],
     ["'Hoy' y 'mañana' dependen del día del mensaje; el mensaje no da la fecha."],
     omitted=["Hora del mensaje 4:05 PM: cuándo llamaron"]),
]

mark_reviewed(PAIRS, "CCC-SLP (anonymous)", "2026-11-12")
write(PAIRS, "batch6_test.jsonl")
