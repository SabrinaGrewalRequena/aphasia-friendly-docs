"""Batch 1: 12 made-up pairs (original + aphasia-friendly version).

Every name, clinic, address and phone number is invented. Phone numbers use the
fictional 555-01xx range; websites and emails use example.org. Nothing here is a
real patient document. Reviewed and approved with no changes by a CCC-SLP (anonymous) on 2026-11-11.

Run:  python data/sources/madeup_batch1.py
"""
import json
from pathlib import Path


def L(kind, text, picture=""):
    return {"kind": kind, "text": text, "picture": picture}


def P(topic, *lines):
    return {"topic": topic, "lines": list(lines)}


T = lambda t, p="": L("text", t, p)
S = lambda t, p="": L("step", t, p)
C = lambda t, p="": L("checkbox", t, p)
B = lambda t, p="": L("blank", t, p)
PH = lambda t, p="phone": L("phone", t, p)
CR = lambda t, p="ambulance": L("crisis", t, p)


def pair(pid, lang, doc_type, source, original, title, pages, notes=()):
    return {
        "id": pid, "language": lang, "doc_type": doc_type, "split": "train",
        "provenance": "made-up (written for this project)", "license": "CC BY 4.0 (project-authored)",
        "slp_reviewed": True, "reviewed_by": "CCC-SLP (anonymous)", "review_date": "2026-11-11", "source": source, "original": original,
        "target": {"title": title, "language": lang, "source": source, "pages": pages,
                   "notes_for_reviewer": list(notes)},
    }


PAIRS = [
# 1 ── Referral to PT/OT (English) ──────────────────────────────────────────────
pair("referral-rehab-en-002", "en", "referral", "Referral for outpatient rehabilitation (made-up example)",
     "Referral for Outpatient Rehabilitation Services. Patient: James Whitfield. Referring provider: Dr. Priya Nair, "
     "Internal Medicine. The patient is referred for outpatient physical therapy (PT) and occupational therapy (OT) "
     "following a left middle cerebral artery stroke with residual right-sided weakness. Services will be provided at "
     "Lakeside Therapy Partners, 1180 Hillcrest Road, Durham, NC. Therapy is anticipated 2 times per week for 8 weeks. "
     "The clinic will contact the patient within 3 business days to schedule. If you have not been contacted, please call "
     "(919) 555-0121. Wear comfortable clothing and closed-toe shoes to each session.",
     "Therapy after your stroke",
     [P("Therapy after your stroke",
        T("For: **James Whitfield**", "person"),
        T("You had a **stroke**.", "brain"),
        T("Your **right side** is **weak**.", "weak arm"),
        T("**Therapy** can help you **move** better.", "physical therapy")),
      P("Two kinds of therapy",
        T("**Dr. Priya Nair** wants you to go.", "doctor"),
        T("**Physical therapy** (PT).", "physical therapy"),
        T("**Occupational therapy** (OT).", "occupational therapy")),
      P("Where",
        T("**Lakeside Therapy Partners**", "clinic"),
        T("**1180 Hillcrest Road, Durham, NC**", "map")),
      P("How often",
        T("**2 times** a week.", "calendar"),
        T("For **8 weeks**.", "calendar")),
      P("What to wear",
        T("Wear **comfortable** clothes.", "clothes"),
        T("Wear **closed-toe shoes**.", "shoes")),
      P("Making your visit",
        T("The clinic will **call you**.", "phone"),
        T("They call within **3 business days**.", "calendar"),
        T("No call? **Call them**.", "phone"),
        PH("Phone: (919) 555-0121"))],
     ["'Left middle cerebral artery stroke' simplified to 'stroke'. PT/OT kept by name without extra explanation; the SLP may want to add one simple line about each."]),

# 2 ── Referral to swallow study (Spanish) ──────────────────────────────────────
pair("referral-swallow-study-es-001", "es", "referral", "Orden de estudio de deglución (ejemplo inventado)",
     "Orden de estudio. Paciente: Rosa Delgado. Se ha ordenado un estudio videofluoroscópico de la deglución (VFSS) para "
     "evaluar disfagia orofaríngea. Este estudio usa rayos X para ver cómo traga. El estudio se realizará en el Departamento de "
     "Radiología del Hospital Comunitario San Marcos, 2500 Avenida Central, primer piso. Su cita es el martes 9 de febrero "
     "de 2027 a las 9:30 a.m. Llegue 30 minutos antes para registrarse. No es necesario estar en ayunas. Traiga su lista de "
     "medicamentos y sus dentaduras, si las usa. Para preguntas, llame a Terapia del Habla al (919) 555-0146.",
     "Un estudio para tragar",
     [P("Un estudio para tragar",
        T("Para: **Rosa Delgado**", "persona"),
        T("Usted tiene **problemas** para **tragar**.", "tragar"),
        T("Le van a hacer un **estudio**.", "examen"),
        T("Usa **rayos X** para ver cómo traga.", "rayos x")),
      P("Cuándo",
        T("**martes 9 de febrero de 2027**", "calendario"),
        T("**9:30 a.m.**", "reloj"),
        T("Llegue **30 minutos antes**.", "reloj")),
      P("Dónde",
        T("**Hospital Comunitario San Marcos**", "hospital"),
        T("**Departamento de Radiología**", "rayos x"),
        T("**2500 Avenida Central**, **primer piso**", "mapa")),
      P("Antes del estudio",
        T("**Puede comer** antes del estudio.", "comer")),
      P("Qué traer",
        S("Su **lista** de **medicamentos**.", "lista de medicamentos"),
        S("Sus **dentaduras**, si las usa.", "dentadura")),
      P("¿Preguntas?",
        T("**Llame** a **Terapia del Habla**.", "teléfono"),
        PH("Teléfono: (919) 555-0146", "teléfono"))],
     ["'No es necesario estar en ayunas' rewritten as 'Puede comer antes del estudio'. Please confirm this is the same meaning for patients."]),

# 3 ── Telehealth appointment (English) ─────────────────────────────────────────
pair("appointment-telehealth-en-001", "en", "appointment", "Telehealth visit instructions (made-up example)",
     "Your Telehealth Speech Therapy Visit. Your video visit with Alex Romero, M.A., CCC-SLP, is scheduled for "
     "Thursday, March 4, 2027 at 11:00 a.m. 15 minutes before your visit, open the email from Piedmont Speech Clinic "
     "and click the link to join. You can also join at www.example.org/visit. You will need a computer, tablet, or "
     "smartphone with a camera and microphone. Find a quiet, well-lit room. Have your glasses and hearing aids ready, "
     "if you use them. If you have technical problems, call (919) 555-0193.",
     "Your video visit",
     [P("Your video visit",
        T("You have a **video visit**.", "video call"),
        T("This is **speech therapy**.", "speech therapist"),
        T("With **Alex Romero, M.A., CCC-SLP**.", "speech therapist")),
      P("When",
        T("**Thursday, March 4, 2027**", "calendar"),
        T("**11:00 a.m.**", "clock")),
      P("What you need",
        T("A **computer**, **tablet** or **smartphone**.", "computer"),
        T("It needs a **camera** and a **microphone**.", "camera")),
      P("Get ready",
        T("Find a **quiet** room.", "quiet"),
        T("Find a room with good **light**.", "lamp"),
        T("Have your **glasses** and **hearing aids**, if you use them.", "glasses")),
      P("Join the visit",
        S("Wait until **15 minutes** before your visit.", "clock"),
        S("Open the **email** from **Piedmont Speech Clinic**.", "email"),
        S("**Click** the **link**.", "click"),
        T("Or go to: **www.example.org/visit**", "website")),
      P("Need help?",
        T("**Computer problems**? **Call**.", "help"),
        PH("Help: (919) 555-0193"))]),

# 4 ── Lab appointment with fasting (Spanish) ───────────────────────────────────
pair("appointment-lab-es-001", "es", "appointment", "Recordatorio de cita de laboratorio (ejemplo inventado)",
     "Recordatorio de cita para análisis de sangre. Tiene una cita en el Laboratorio de la Clínica Familiar Las Palmas el "
     "lunes 15 de marzo de 2027 a las 7:45 a.m. Este análisis requiere ayuno. No coma ni beba nada excepto agua durante "
     "8 horas antes de su cita. Puede tomar sus medicamentos habituales con agua, a menos que su médico le indique lo "
     "contrario. Traiga una identificación con foto y su tarjeta de seguro. Si necesita cambiar la cita, llame al "
     "(919) 555-0172.",
     "Análisis de sangre",
     [P("Análisis de sangre",
        T("Usted tiene una **cita**.", "cita médica"),
        T("Le van a sacar **sangre**.", "análisis de sangre"),
        T("En el **Laboratorio** de la **Clínica Familiar Las Palmas**.", "laboratorio")),
      P("Cuándo",
        T("**lunes 15 de marzo de 2027**", "calendario"),
        T("**7:45 a.m.**", "reloj")),
      P("No coma antes",
        T("**No coma** nada por **8 horas** antes.", "no comer"),
        T("**No beba** nada, solo **agua**.", "agua")),
      P("Sus medicamentos",
        T("Puede tomar sus **medicamentos** con **agua**.", "pastilla y agua"),
        T("A menos que su **médico** le diga **otra cosa**.", "médico")),
      P("Qué traer",
        S("Su **identificación** con **foto**.", "identificación"),
        S("Su **tarjeta de seguro**.", "tarjeta de seguro")),
      P("Cambiar la cita",
        T("¿Necesita **cambiar** la cita?", "calendario"),
        PH("Teléfono: (919) 555-0172", "teléfono"))]),

# 5 ── Discharge after TIA (English) ────────────────────────────────────────────
pair("discharge-tia-en-001", "en", "discharge", "Discharge instructions after TIA (made-up example)",
     "Discharge Summary: Patient Instructions. Diagnosis: Transient ischemic attack (TIA). A TIA is a temporary blockage of "
     "blood flow to the brain. It is a warning sign that you are at higher risk for a stroke. Medication: aspirin 81 mg by "
     "mouth once daily. Check your blood pressure at home every morning and write it down. Bring your log to your follow-up "
     "with Dr. Samuel Ortiz on Wednesday, January 20, 2027 at 3:00 p.m. Call 911 right away if you have any of these signs: "
     "face drooping, arm weakness, speech difficulty. Remember BE FAST: Balance, Eyes, Face, Arm, Speech, Time to call 911. "
     "Questions: call the Stroke Clinic at (919) 555-0109.",
     "Going home after your TIA",
     [P("You had a TIA",
        T("You had a **TIA**.", "brain"),
        T("**Blood** to your **brain** was **blocked** for a short time.", "brain"),
        T("It is a **warning sign**.", "warning"),
        T("You are at **higher risk** for a **stroke**.", "stroke")),
      P("Your medicine",
        T("Take **aspirin 81 mg**.", "pill"),
        T("Take it **once** every **day**.", "calendar"),
        T("Swallow it **by mouth**.", "mouth")),
      P("Check your blood pressure",
        S("Check your **blood pressure** every **morning**.", "blood pressure"),
        S("**Write it down**.", "write"),
        S("**Bring** the list to your **doctor**.", "list")),
      P("See your doctor",
        T("See **Dr. Samuel Ortiz**.", "doctor"),
        T("**Wednesday, January 20, 2027**", "calendar"),
        T("**3:00 p.m.**", "clock")),
      P("Stroke warning signs",
        T("Face **drooping**?", "face"),
        T("Arm **weak**?", "weak arm"),
        T("Trouble **speaking**?", "speech"),
        CR("Call 911 right away")),
      P("Remember BE FAST",
        T("**B**alance, **E**yes, **F**ace", "balance"),
        T("**A**rm, **S**peech", "arm"),
        CR("Time to call 911")),
      P("Questions?",
        T("**Questions**? Call the **Stroke Clinic**.", "question"),
        PH("Stroke Clinic: (919) 555-0109"))],
     ["'Temporary blockage of blood flow' rewritten as 'blood to your brain was blocked for a short time'.",
      "BE FAST letters are split over 2 lines plus the 911 line. Please check this is clear."]),

# 6 ── Discharge after stroke (Spanish) ─────────────────────────────────────────
pair("discharge-stroke-es-001", "es", "discharge", "Instrucciones al salir del hospital (ejemplo inventado)",
     "Instrucciones al salir del hospital. Usted fue tratado por un accidente cerebrovascular (derrame cerebral). "
     "Medicamentos nuevos: atorvastatina 40 mg, una tableta cada noche; clopidogrel 75 mg, una tableta cada mañana. "
     "No deje de tomar sus medicamentos sin hablar con su médico. Actividad: puede caminar dentro de la casa. No maneje "
     "hasta que su médico lo autorice. Cita de seguimiento: Dra. Lucía Herrera, Neurología, viernes 22 de enero de 2027 "
     "a las 10:00 a.m. Si tiene debilidad repentina, dificultad para hablar o la cara caída, llame al 911 de inmediato.",
     "Al salir del hospital",
     [P("Usted tuvo un derrame",
        T("Usted tuvo un **derrame cerebral**.", "cerebro"),
        T("El hospital lo **trató**.", "hospital"),
        T("Ahora va a **casa**.", "casa")),
      P("Medicina de la noche",
        T("**Atorvastatina 40 mg**", "pastilla"),
        T("Tome **una tableta**.", "pastilla"),
        T("Cada **noche**.", "noche")),
      P("Medicina de la mañana",
        T("**Clopidogrel 75 mg**", "pastilla"),
        T("Tome **una tableta**.", "pastilla"),
        T("Cada **mañana**.", "mañana")),
      P("No pare sus medicinas",
        T("**No deje** de tomar sus medicinas.", "no parar"),
        T("Primero **hable** con su **médico**.", "médico")),
      P("Actividad",
        T("Puede **caminar** dentro de la **casa**.", "caminar"),
        T("**No maneje**.", "no manejar"),
        T("Espere a que su **médico** diga que **sí**.", "médico")),
      P("Su cita",
        T("Con la **Dra. Lucía Herrera**.", "doctora"),
        T("Es en **Neurología**.", "cerebro"),
        T("**viernes 22 de enero de 2027**", "calendario"),
        T("**10:00 a.m.**", "reloj")),
      P("Emergencia",
        T("¿**Debilidad** de repente?", "brazo débil"),
        T("¿Le cuesta **hablar**?", "hablar"),
        T("¿La **cara** caída?", "cara"),
        CR("Llame al 911 de inmediato", "ambulancia"))],
     ["'Accidente cerebrovascular' shortened to 'derrame cerebral', the term the original also gives."]),

# 7 ── Warfarin (English) ───────────────────────────────────────────────────────
pair("medication-warfarin-en-001", "en", "medication", "Warfarin instructions (made-up example)",
     "Medication Instructions: Warfarin (Coumadin). Your dose: warfarin 5 mg by mouth once daily at 5:00 p.m. Warfarin thins "
     "your blood to help prevent clots. You will need regular blood tests (INR) to check your dose. Your next INR check is on "
     "Monday, February 1, 2027 at Cedar Grove Anticoagulation Clinic. Keep the amount of green leafy vegetables you eat about "
     "the same each week. Do not take aspirin or ibuprofen unless your doctor says it is okay. Call the clinic at "
     "(919) 555-0138 if you notice unusual bruising, bleeding gums, or blood in your urine or stool. Call 911 for a bad fall, "
     "a hit to the head, or bleeding that will not stop.",
     "Your medicine: warfarin",
     [P("Your medicine: warfarin",
        T("Your medicine is **warfarin** (**Coumadin**).", "pill"),
        T("It **thins** your **blood**.", "blood"),
        T("It helps stop **blood clots**.", "blood clot")),
      P("How to take it",
        T("Take **warfarin 5 mg**.", "pill"),
        T("Take it **once** a **day**.", "calendar"),
        T("Take it at **5:00 p.m.**", "clock"),
        T("Swallow it **by mouth**.", "mouth")),
      P("Blood tests",
        T("You need **blood tests**.", "blood test"),
        T("The test is called **INR**.", "blood test"),
        T("It checks your **dose**.", "check")),
      P("Your next blood test",
        T("**Monday, February 1, 2027**", "calendar"),
        T("At **Cedar Grove Anticoagulation Clinic**.", "clinic")),
      P("Food",
        T("Eat about the **same amount** of green leafy vegetables.", "lettuce"),
        T("Keep it the same **each week**.", "calendar")),
      P("Other medicines",
        T("**No aspirin**.", "no pill"),
        T("**No ibuprofen**.", "no pill"),
        T("Only if your **doctor** says it is **okay**.", "doctor")),
      P("Call the clinic",
        T("Strange **bruises**?", "bruise"),
        T("**Bleeding** gums?", "teeth"),
        T("**Blood** in your **urine** or **stool**?", "toilet"),
        PH("Clinic: (919) 555-0138")),
      P("Emergency",
        T("A **bad fall**?", "fall"),
        T("You **hit** your **head**?", "head"),
        T("**Bleeding** that will **not stop**?", "blood"),
        CR("Call 911"))]),

# 8 ── Lisinopril (Spanish) ─────────────────────────────────────────────────────
pair("medication-lisinopril-es-001", "es", "medication", "Instrucciones de lisinopril (ejemplo inventado)",
     "Instrucciones de medicamento: Lisinopril 10 mg. Tome 1 tableta por la boca una vez al día, por la mañana. Este "
     "medicamento baja la presión arterial. Levántese despacio si está sentado o acostado, porque puede sentirse mareado. "
     "Si tiene tos seca que no se quita, llame a su farmacia: Farmacia Central, (919) 555-0154. Si tiene hinchazón en la "
     "cara, los labios o la lengua, o dificultad para respirar, llame al 911.",
     "Su medicina: lisinopril",
     [P("Su medicina",
        T("Su medicina es **lisinopril 10 mg**.", "pastilla"),
        T("Baja la **presión arterial**.", "presión arterial")),
      P("Cómo tomarla",
        T("Tome **1 tableta**.", "pastilla"),
        T("Por la **boca**.", "boca"),
        T("**Una vez** al día, por la **mañana**.", "mañana")),
      P("Levántese despacio",
        T("Puede sentirse **mareado**.", "mareo"),
        T("Si está sentado o acostado, levántese **despacio**.", "levantarse")),
      P("Tos seca",
        T("¿Tiene **tos seca** que no se quita?", "tos"),
        T("Llame a la **Farmacia Central**.", "farmacia"),
        PH("Farmacia: (919) 555-0154", "teléfono")),
      P("Emergencia",
        T("¿**Hinchazón** en la cara, los labios o la lengua?", "cara hinchada"),
        T("¿Le cuesta **respirar**?", "respirar"),
        CR("Llame al 911", "ambulancia"))]),

# 9 ── Emotional support (Spanish) ──────────────────────────────────────────────
pair("mental-health-es-001", "es", "mental_health", "Apoyo emocional después de un derrame (ejemplo inventado)",
     "Apoyo emocional después de un derrame cerebral. Es común sentir tristeza, ansiedad o enojo después de un derrame "
     "cerebral. Estos sentimientos pueden afectar su recuperación. Hable con su médico o terapeuta si se siente triste la "
     "mayor parte del día durante más de dos semanas. El Grupo de Apoyo Juntos se reúne en español el segundo martes de cada "
     "mes a las 6:30 p.m. en la Iglesia San José, salón 4. Para información, llame a María Torres al (919) 555-0168. "
     "Si tiene pensamientos de hacerse daño, llame o envíe un mensaje de texto al 988 (Línea 988 de Prevención del Suicidio "
     "y Crisis). Está disponible las 24 horas.",
     "Sus sentimientos después de un derrame",
     [P("Sus sentimientos",
        T("Muchas personas se sienten **tristes**.", "triste"),
        T("O sienten **ansiedad** o **enojo**.", "enojado"),
        T("Es **común** después de un **derrame cerebral**.", "cerebro"),
        T("Esto puede afectar su **recuperación**.", "recuperación")),
      P("Hable con alguien",
        T("¿Triste casi **todo el día**?", "triste"),
        T("¿Por **más de dos semanas**?", "calendario"),
        T("**Hable** con su **médico** o **terapeuta**.", "médico")),
      P("Un grupo puede ayudar",
        T("**Grupo de Apoyo Juntos**", "grupo"),
        T("Es en **español**.", "hablar"),
        T("El **segundo martes** de cada mes.", "calendario"),
        T("A las **6:30 p.m.**", "reloj")),
      P("Dónde",
        T("**Iglesia San José**, **salón 4**.", "iglesia"),
        PH("María Torres: (919) 555-0168", "teléfono")),
      P("Ayuda ahora",
        T("¿Piensa en **hacerse daño**?", "ayuda"),
        CR("Llame o envíe un mensaje de texto al 988 (Línea 988 de Prevención del Suicidio y Crisis)", "teléfono"),
        T("Está disponible las **24 horas**.", "reloj"))],
     ["Crisis line kept word for word."]),

# 10 ── Social connection (English) ─────────────────────────────────────────────
pair("mental-health-connection-en-002", "en", "mental_health", "Social connection and aphasia (made-up example)",
     "Social Connection and Aphasia. People with aphasia are at increased risk of social isolation and depression. Staying "
     "socially engaged supports emotional well-being and language recovery. Consider joining an aphasia-friendly community "
     "program. The Aphasia Café meets every Saturday at 10:00 a.m. at Brightleaf Coffee, 305 Main Street. Trained volunteers "
     "support conversation. For more information, contact Priya Shah at (919) 555-0127 or pshah@example.org. If you feel "
     "hopeless or have thoughts of suicide, call or text 988 to reach the 988 Suicide & Crisis Lifeline.",
     "Stay connected",
     [P("Stay connected",
        T("Aphasia can make you feel **alone**.", "alone"),
        T("Some people feel **depressed**.", "sad"),
        T("**Talking** with others **helps**.", "conversation"),
        T("It helps your **mood** and your **language**.", "happy")),
      P("Aphasia Café",
        T("Join the **Aphasia Café**.", "coffee"),
        T("**Volunteers** help you **talk**.", "volunteer"),
        T("Every **Saturday** at **10:00 a.m.**", "calendar")),
      P("Where",
        T("**Brightleaf Coffee**", "cafe"),
        T("**305 Main Street**", "map")),
      P("More information",
        T("Contact **Priya Shah**.", "person"),
        PH("Phone: (919) 555-0127"),
        T("Email: **pshah@example.org**", "email")),
      P("Help now",
        T("Feel **hopeless**?", "sad"),
        T("Thinking about **suicide**?", "help"),
        CR("Call or text 988 — 988 Suicide & Crisis Lifeline", "phone"))]),

# 11 ── Speech-language results form (English, clinician ticks) ─────────────────
pair("results-language-en-001", "en", "results", "Speech-language evaluation summary form (made-up example)",
     "Speech-Language Evaluation: Summary of Results for ____________. Diagnosis: [ ] Expressive aphasia "
     "[ ] Receptive aphasia [ ] Global aphasia [ ] Apraxia of speech [ ] Dysarthria. Areas of difficulty: [ ] Word retrieval "
     "[ ] Auditory comprehension [ ] Reading comprehension [ ] Written expression [ ] Speech intelligibility. "
     "Recommendation: speech-language therapy ___ times per week for ___ weeks. Treatment goals: [ ] Improve word retrieval "
     "in conversation [ ] Improve comprehension of multi-step directions [ ] Improve functional reading (e.g., medication "
     "labels) [ ] Use a communication book or device. Your therapist: ____________ Phone: ____________",
     "Your speech and language results",
     [P("Your results",
        B("Results for: ____________", "person"),
        T("You had a **speech** and **language** test.", "speech therapist")),
      P("What you have",
        C("Hard to **say** what you want (**expressive aphasia**).", "talk"),
        C("Hard to **understand** words (**receptive aphasia**).", "listen"),
        C("Hard to **talk** and **understand** (**global aphasia**).", "talk and listen"),
        C("Hard to **move** your mouth to speak (**apraxia of speech**).", "mouth"),
        C("Speech muscles are **weak**, speech is **unclear** (**dysarthria**).", "mouth")),
      P("What is hard for you",
        C("**Finding** words.", "search"),
        C("**Understanding** what people say.", "listen"),
        C("**Reading**.", "read"),
        C("**Writing**.", "write"),
        C("Others **understanding** your speech.", "conversation")),
      P("Your therapy",
        B("Speech therapy ___ times a week.", "calendar"),
        B("For ___ weeks.", "calendar")),
      P("Your goals",
        C("Find **words** when you **talk**.", "talk"),
        C("Follow **directions** with **steps**.", "steps"),
        C("**Read** things like **medicine labels**.", "medicine label"),
        C("Use a **communication book** or **device**.", "communication book")),
      P("Your therapist",
        B("Therapist: ____________", "speech therapist"),
        B("Phone: ____________", "phone"))],
     ["Diagnosis names are kept in brackets after a plain explanation. Please check the plain explanations are accurate."]),

# 12 ── MRI preparation (English) ───────────────────────────────────────────────
pair("procedure-mri-en-001", "en", "procedure", "MRI preparation instructions (made-up example)",
     "Preparing for Your MRI. Your MRI of the brain is scheduled for Tuesday, February 16, 2027 at 1:30 p.m. at Northgate "
     "Imaging Center, 4410 Pinecrest Parkway. Arrive 30 minutes early. You may eat and take your medications as usual. "
     "Remove all metal objects, including jewelry, hearing aids, and hairpins. Tell the technologist if you have a pacemaker, "
     "metal implants, or a medication pump. The scan takes about 45 minutes. You will need to lie still. The machine makes "
     "loud knocking sounds; earplugs will be provided. Questions: (919) 555-0181.",
     "Your brain MRI",
     [P("Your brain MRI",
        T("You will have an **MRI**.", "mri"),
        T("It takes **pictures** of your **brain**.", "brain")),
      P("When and where",
        T("**Tuesday, February 16, 2027**", "calendar"),
        T("**1:30 p.m.**", "clock"),
        T("**Northgate Imaging Center**", "hospital"),
        T("**4410 Pinecrest Parkway**", "map")),
      P("Before you come",
        T("Come **30 minutes early**.", "clock"),
        T("You can **eat** as usual.", "eat"),
        T("Take your **medicines** as usual.", "pill")),
      P("No metal",
        T("Take off all **metal**.", "no metal"),
        T("**Jewelry**, **hearing aids**, **hairpins**.", "jewelry")),
      P("Tell the staff",
        T("Do you have a **pacemaker**?", "heart"),
        T("**Metal implants**?", "implant"),
        T("A **medicine pump**?", "pump"),
        T("**Tell** the **technologist**.", "nurse")),
      P("During the MRI",
        T("It takes about **45 minutes**.", "clock"),
        T("**Lie still**.", "lie down"),
        T("It is **loud**. You will get **earplugs**.", "earplugs")),
      P("Questions?",
        PH("Questions? Call (919) 555-0181"))]),
]

out = Path(__file__).resolve().parent.parent / "pairs" / "madeup_batch1.jsonl"
with out.open("w", encoding="utf-8") as fh:
    for p in PAIRS:
        fh.write(json.dumps(p, ensure_ascii=False) + "\n")
print(f"Wrote {len(PAIRS)} pairs to {out}")
