"""Writes the 5 made-up seed pairs to data/pairs/seed.jsonl.
They show the format. Reviewed and approved with no changes by a CCC-SLP (anonymous) on 2026-11-11.
Run:  python data/sources/seed_pairs.py
"""
import json
from pathlib import Path

def L(kind, text, picture=""):
    return {"kind": kind, "text": text, "picture": picture}

PAIRS = [
{
 "id": "referral-speech-en-001", "language": "en", "doc_type": "referral", "split": "train",
 "provenance": "made-up", "license": "CC BY 4.0 (project-authored)", "slp_reviewed": True, "reviewed_by": "CCC-SLP (anonymous)", "review_date": "2026-11-11",
 "source": "Referral letter (made-up example)",
 "original": ("You have been referred to Outpatient Speech-Language Pathology at Riverside Rehabilitation Center "
              "for evaluation and treatment of expressive aphasia. Please contact the scheduling department at "
              "(919) 555-0142 within 5 business days to arrange your initial appointment. Please bring your "
              "insurance card, a photo ID, and a list of your current medications. Riverside Rehabilitation "
              "Center is located at 410 Oak Street, Suite 200."),
 "target": {"title": "Speech therapy", "language": "en", "source": "Referral letter (made-up example)", "pages": [
   {"topic": "Speech therapy", "lines": [
     L("text", "**Speech therapy** can help you **talk**.", "speech therapist"),
     L("text", "Your **doctor** wants you to go.", "doctor"),
     L("text", "The place is **Riverside Rehabilitation Center**.", "hospital")]},
   {"topic": "Call to make a visit", "lines": [
     L("text", "**Call** to make a **visit**.", "phone"),
     L("phone", "Phone: (919) 555-0142", "phone"),
     L("text", "Call in the next **5 business days**.", "calendar")]},
   {"topic": "What to bring", "lines": [
     L("step", "Your **insurance card**.", "insurance card"),
     L("step", "Your **photo ID**.", "identity card"),
     L("step", "A **list** of your **medicines**.", "medicine list")]},
   {"topic": "Where to go", "lines": [
     L("text", "**Riverside Rehabilitation Center**", "hospital"),
     L("text", "**410 Oak Street, Suite 200**", "map"),
     L("phone", "Questions? Call (919) 555-0142", "phone")]}],
  "notes_for_reviewer": ["'expressive aphasia' was not named; the page says speech therapy helps you talk."]}
},
{
 "id": "discharge-stroke-en-001", "language": "en", "doc_type": "discharge", "split": "train",
 "provenance": "made-up", "license": "CC BY 4.0 (project-authored)", "slp_reviewed": True, "reviewed_by": "CCC-SLP (anonymous)", "review_date": "2026-11-11",
 "source": "Discharge instructions (made-up example)",
 "original": ("Discharge Instructions. You were treated for an ischemic stroke. Take clopidogrel 75 mg by mouth once "
              "daily. Do not stop taking this medication unless instructed by your physician. Follow up with "
              "Dr. Maria Chen in Neurology on Tuesday, December 8 at 10:30 a.m. Call 911 immediately if you "
              "experience sudden face drooping, arm weakness, or difficulty speaking. For non-urgent questions, "
              "call the Neurology clinic at (919) 555-0187."),
 "target": {"title": "Going home after your stroke", "language": "en", "source": "Discharge instructions (made-up example)", "pages": [
   {"topic": "You had a stroke", "lines": [
     L("text", "You had a **stroke**.", "brain"),
     L("text", "The hospital **treated** you.", "hospital"),
     L("text", "Now you can go **home**.", "house")]},
   {"topic": "Your medicine", "lines": [
     L("text", "Take **clopidogrel 75 mg**.", "pill"),
     L("text", "Take it **once** every **day**.", "calendar"),
     L("text", "Swallow it **by mouth**.", "mouth"),
     L("text", "**Do not stop** unless your doctor says.", "stop")]},
   {"topic": "See your doctor", "lines": [
     L("text", "See **Dr. Maria Chen**.", "doctor"),
     L("text", "**Tuesday, December 8**", "calendar"),
     L("text", "**10:30 a.m.**", "clock")]},
   {"topic": "Emergency", "lines": [
     L("text", "Face **drooping**? Arm **weak**? Hard to **speak**?", "stroke signs"),
     L("crisis", "Call 911 now", "ambulance")]},
   {"topic": "Questions", "lines": [
     L("text", "Have a **question**? It is **not** an emergency?", "question"),
     L("phone", "Neurology clinic: (919) 555-0187", "phone")]}],
  "notes_for_reviewer": ["'ischemic' was simplified to 'stroke'.", "Check the SLP is happy with 'once every day' for 'once daily'."]}
},
{
 "id": "appointment-es-001", "language": "es", "doc_type": "appointment", "split": "train",
 "provenance": "made-up", "license": "CC BY 4.0 (project-authored)", "slp_reviewed": True, "reviewed_by": "CCC-SLP (anonymous)", "review_date": "2026-11-11",
 "source": "Carta de cita (ejemplo inventado)",
 "original": ("Estimado paciente: Le recordamos que tiene una cita de seguimiento en la Clínica de Rehabilitación "
              "Central el jueves 14 de enero de 2027 a las 2:15 p.m. con la Dra. Ana Morales. Por favor, llegue 15 "
              "minutos antes para completar los formularios de registro. Si necesita cancelar o cambiar su cita, "
              "llame al (919) 555-0163 con al menos 24 horas de anticipación."),
 "target": {"title": "Su cita", "language": "es", "source": "Carta de cita (ejemplo inventado)", "pages": [
   {"topic": "Usted tiene una cita", "lines": [
     L("text", "Usted tiene una **cita**.", "cita médica"),
     L("text", "Con la **Dra. Ana Morales**.", "doctora"),
     L("text", "En la **Clínica de Rehabilitación Central**.", "hospital")]},
   {"topic": "Cuándo", "lines": [
     L("text", "**jueves 14 de enero de 2027**", "calendario"),
     L("text", "**2:15 p.m.**", "reloj")]},
   {"topic": "Llegue temprano", "lines": [
     L("text", "Llegue **15 minutos antes**.", "reloj"),
     L("text", "Va a **llenar** unos **papeles**.", "formulario")]},
   {"topic": "¿No puede ir?", "lines": [
     L("text", "¿Necesita **cancelar** o **cambiar** la cita?", "cancelar"),
     L("text", "**Llame** por lo menos **24 horas** antes.", "teléfono"),
     L("phone", "Teléfono: (919) 555-0163", "teléfono")]}],
  "notes_for_reviewer": []}
},
{
 "id": "medication-en-001", "language": "en", "doc_type": "medication", "split": "train",
 "provenance": "made-up", "license": "CC BY 4.0 (project-authored)", "slp_reviewed": True, "reviewed_by": "CCC-SLP (anonymous)", "review_date": "2026-11-11",
 "source": "Medication instructions (made-up example)",
 "original": ("Atorvastatin 40 mg tablet. Take 1 tablet by mouth every evening. This medication lowers cholesterol "
              "to reduce your risk of another stroke. Avoid grapefruit and grapefruit juice while taking this "
              "medication. Contact your pharmacist at (919) 555-0119 if you experience unexplained muscle pain or "
              "weakness."),
 "target": {"title": "Your medicine: atorvastatin", "language": "en", "source": "Medication instructions (made-up example)", "pages": [
   {"topic": "Your medicine", "lines": [
     L("text", "Your medicine is **atorvastatin 40 mg**.", "pill"),
     L("text", "It **lowers cholesterol**.", "heart"),
     L("text", "It helps **stop another stroke**.", "brain")]},
   {"topic": "How to take it", "lines": [
     L("text", "Take **1 tablet**.", "pill"),
     L("text", "Swallow it **by mouth**.", "mouth"),
     L("text", "Take it every **evening**.", "evening")]},
   {"topic": "No grapefruit", "lines": [
     L("text", "**Do not** eat **grapefruit**.", "grapefruit"),
     L("text", "**Do not** drink **grapefruit juice**.", "juice")]},
   {"topic": "Muscle pain?", "lines": [
     L("text", "Muscles **hurt** or feel **weak**? You do not know why?", "muscle pain"),
     L("text", "**Call** your **pharmacist**.", "pharmacist"),
     L("phone", "Pharmacist: (919) 555-0119", "phone")]}],
  "notes_for_reviewer": []}
},
{
 "id": "mental-health-en-001", "language": "en", "doc_type": "mental_health", "split": "train",
 "provenance": "made-up", "license": "CC BY 4.0 (project-authored)", "slp_reviewed": True, "reviewed_by": "CCC-SLP (anonymous)", "review_date": "2026-11-11",
 "source": "Support resources handout (made-up example)",
 "original": ("Feeling down after a stroke is common. Many survivors experience sadness, frustration, or loss of "
              "interest in activities they once enjoyed. Talk to your doctor if these feelings last more than "
              "two weeks. The Stroke Survivors Group meets every Wednesday at 6:00 p.m. at the Cary Community "
              "Center; call (919) 555-0175 for details. If you are thinking about hurting yourself, call or text "
              "988 to reach the 988 Suicide & Crisis Lifeline, available 24 hours a day."),
 "target": {"title": "Feeling sad after a stroke", "language": "en", "source": "Support resources handout (made-up example)", "pages": [
   {"topic": "Feeling sad is common", "lines": [
     L("text", "Many people feel **sad** after a **stroke**.", "sad face"),
     L("text", "You may feel **frustrated**.", "frustrated"),
     L("text", "Things you liked may feel **less fun**.", "hobby")]},
   {"topic": "Talk to your doctor", "lines": [
     L("text", "Sad for **more than two weeks**?", "calendar"),
     L("text", "**Talk** to your **doctor**.", "doctor")]},
   {"topic": "A group can help", "lines": [
     L("text", "The **Stroke Survivors Group** meets.", "group"),
     L("text", "Every **Wednesday** at **6:00 p.m.**", "calendar"),
     L("text", "At the **Cary Community Center**.", "building"),
     L("phone", "Phone: (919) 555-0175", "phone")]},
   {"topic": "Help now", "lines": [
     L("text", "Thinking about **hurting yourself**?", "help"),
     L("crisis", "Call or text 988 — 988 Suicide & Crisis Lifeline", "phone"),
     L("text", "Help is there **24 hours a day**.", "clock")]}],
  "notes_for_reviewer": ["Crisis line kept word for word."]}
},
]

out = Path(__file__).resolve().parent.parent / "pairs" / "seed.jsonl"
with out.open("w", encoding="utf-8") as fh:
    for p in PAIRS:
        fh.write(json.dumps(p, ensure_ascii=False) + "\n")
print(f"Wrote {len(PAIRS)} pairs to {out}")
