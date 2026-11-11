"""Batch 1: 8 pairs built from aphasia-friendly handouts on the UNC School of Medicine
public web page (provided by the project owner, who confirmed they may be used).

The TARGETS follow the UNC handouts closely, put into this project's page format.
The ORIGINALS were written for this project in clinical language, because the UNC
handouts don't come with their source documents.

Spelling mistakes in the UNC handouts were corrected; every other change is listed
in notes_for_reviewer. None of these are SLP-reviewed yet.

Run:  python data/sources/unc_batch1.py
"""
import json
from pathlib import Path

UNC = "UNC School of Medicine (public web page)"


def L(kind, text, picture=""):
    return {"kind": kind, "text": text, "picture": picture}


def P(topic, *lines):
    return {"topic": topic, "lines": list(lines)}


def pair(pid, lang, doc_type, unc_file, source, original, title, pages, notes):
    return {
        "id": pid, "language": lang, "doc_type": doc_type, "split": "train",
        "provenance": f"Target adapted from {UNC}, file {unc_file}; original written for this project",
        "license": "UNC content used with the project owner's confirmation; check UNC terms before publishing",
        "slp_reviewed": False, "source": source, "original": original,
        "target": {"title": title, "language": lang, "source": source, "pages": pages,
                   "notes_for_reviewer": notes},
    }


C = lambda t, p="": L("checkbox", t, p)
T = lambda t, p="": L("text", t, p)
S = lambda t, p="": L("step", t, p)
B = lambda t, p="": L("blank", t, p)

PAIRS = []

# 1 ── Swallowing results (English) ─────────────────────────────────────────────
PAIRS.append(pair(
    "unc-swallow-results-en", "en", "results", "D10.pdf", "Clinical swallow evaluation: results and recommendations",
    "Clinical Swallow Evaluation: Results and Recommendations. "
    "Findings: [ ] Oropharyngeal dysphagia for solid consistencies. [ ] Oropharyngeal dysphagia for liquid consistencies. "
    "Dysphagia increases the risk of aspiration pneumonia. Goal: safe oral intake. "
    "Recommended diet texture: [ ] Regular solids [ ] Advanced (soft) [ ] Mechanical-altered [ ] Pureed. "
    "Recommended liquid consistency: [ ] Thin liquids [ ] Nectar-thick liquids [ ] Honey-thick liquids. "
    "Avoid: [ ] chewy foods (e.g., candies, tough meats) [ ] pea-sized foods (e.g., rice, seeds, peas, corn) "
    "[ ] mixed-consistency foods (e.g., watermelon, cereal with milk) [ ] eating and drinking at the same time "
    "[ ] eating when fatigued. "
    "Recommended strategies: [ ] Eat and drink at a slow rate. [ ] Chew food thoroughly. [ ] Perform oral care "
    "5-6 times daily. [ ] Sit fully upright during meals. [ ] Referral to: ____________. "
    "Medication administration: [ ] Take pills with water. [ ] Take 1 pill at a time. [ ] Crush pills. "
    "[ ] Take pills in applesauce. "
    "Compensatory strategies: [ ] Chin tuck. [ ] Head turn to the left. [ ] Head turn to the right. "
    "[ ] Effortful swallow. [ ] Alternate solids and liquids: 1 bite, then 1 sip.",
    "Swallowing results",
    [P("Swallowing results",
       C("You have problems swallowing **food**.", "eating"),
       C("You have problems swallowing **liquids**.", "drinking"),
       T("Swallowing **problems** can cause **pneumonia**.", "lungs"),
       T("The **goal** is to swallow **safely**.", "swallow")),
     P("What to eat?",
       C("**Regular** solids", "plate of food"),
       C("**Advanced** (soft)", "soft food"),
       C("**Mechanical**-altered", "minced food"),
       C("**Pureed**", "puree")),
     P("What to drink?",
       C("**Thin** liquids", "glass of water"),
       C("**Nectar**-thick liquids", "thick drink"),
       C("**Honey**-thick liquids", "honey")),
     P("Do not",
       C("Do **not** eat **chewy** foods. (Examples: candies, tough meats)", "candy"),
       C("Do **not** eat **pea-sized** foods. (Examples: rice, seeds, peas, corn)", "peas"),
       C("Do **not** eat **mixed** foods. (Examples: watermelon, cereal/milk)", "cereal"),
       C("Do **not** eat and drink **together**.", "eat and drink"),
       C("Do **not** eat when **tired**.", "tired")),
     P("Do",
       C("Eat and drink **slowly**.", "eat slowly"),
       C("**Chew** your food **well**.", "chew"),
       C("**Brush** your teeth **5-6 times** daily.", "brush teeth"),
       C("**Sit upright** during meals.", "sit at table"),
       C("You may want to see ____________.", "doctor")),
     P("Taking medicine",
       C("Swallow your **pills** with **water**.", "pill and water"),
       C("Swallow **1 pill** at a time.", "pill"),
       C("**Crush** your pills.", "crush pill"),
       C("Swallow your **pills** in **applesauce**.", "applesauce")),
     P("Helpful tips",
       C("Tuck your chin **down**.", "chin down"),
       C("Turn head to the **left**.", "turn head left"),
       C("Turn head to the **right**.", "turn head right"),
       C("Swallow **hard**.", "swallow"),
       C("Take **1 bite**, then **1 sip**.", "bite and sip"))],
    ["Same content as the UNC handout. 'Do not' is now written on each line of the Do-not page, so each line is safe on its own; please confirm.",
     "Clinician ticks every option that applies before giving it to the patient."]))

# 2 ── Swallowing results (Spanish) ─────────────────────────────────────────────
PAIRS.append(pair(
    "unc-swallow-results-es", "es", "results", "R1S.pdf", "Evaluación clínica de la deglución: resultados y recomendaciones",
    "Evaluación clínica de la deglución: resultados y recomendaciones. "
    "Hallazgos: [ ] Disfagia orofaríngea con consistencias sólidas. [ ] Disfagia orofaríngea con consistencias líquidas. "
    "La disfagia aumenta el riesgo de neumonía por aspiración. Objetivo: alimentación oral segura. "
    "Textura de dieta recomendada: [ ] Sólidos regulares [ ] Avanzado (suave) [ ] Mecánico-ajustado [ ] Puré. "
    "Consistencia de líquidos recomendada: [ ] Líquidos delgados [ ] Líquidos de consistencia néctar "
    "[ ] Líquidos de consistencia miel. "
    "Evitar: [ ] alimentos gomosos (p. ej., caramelos, carne dura) [ ] alimentos del tamaño de un chícharo "
    "(p. ej., arroz, semillas, guisantes, maíz) [ ] alimentos de consistencia mixta (p. ej., sandía, cereal con leche) "
    "[ ] comer y beber al mismo tiempo [ ] comer cuando está fatigado. "
    "Estrategias recomendadas: [ ] Comer y beber despacio. [ ] Masticar bien los alimentos. [ ] Higiene oral "
    "5-6 veces al día. [ ] Sentarse en posición vertical durante las comidas. [ ] Referido a: ____________. "
    "Administración de medicamentos: [ ] Tomar las pastillas con agua. [ ] Tomar 1 pastilla a la vez. "
    "[ ] Triturar las pastillas. [ ] Tomar las pastillas en puré de manzana. "
    "Estrategias compensatorias: [ ] Barbilla hacia abajo. [ ] Girar la cabeza a la izquierda. "
    "[ ] Girar la cabeza a la derecha. [ ] Deglución con esfuerzo. [ ] Alternar sólidos y líquidos: 1 bocado, luego 1 sorbo.",
    "Resultados del tragar",
    [P("Resultados del tragar",
       C("Usted tiene problemas tragando **comida**.", "comer"),
       C("Usted tiene problemas tragando **líquidos**.", "beber"),
       T("Los **problemas** del tragar pueden causar **neumonía**.", "pulmones"),
       T("La **meta** es tragar **sin peligro**.", "tragar")),
     P("¿Qué hay para comer?",
       C("**Sólidos** regulares", "plato de comida"),
       C("**Avanzado** (suave)", "comida blanda"),
       C("**Mecánico**-ajustado", "comida picada"),
       C("**Puré**", "puré")),
     P("¿Qué hay para beber?",
       C("Líquidos **delgados**", "vaso de agua"),
       C("Líquidos de consistencia **néctar**", "bebida espesa"),
       C("Líquidos de consistencia **miel**", "miel")),
     P("No",
       C("**No** coma comida **gomosa**. (Ejemplos: caramelos, carne dura)", "caramelo"),
       C("**No** coma alimentos del tamaño de un **chícharo**. (Ejemplos: arroz, semillas, guisantes, maíz)", "guisantes"),
       C("**No** coma comida **mezclada**. (Ejemplos: sandía, cereal/leche)", "cereal"),
       C("**No** coma y tome al **mismo tiempo**.", "comer y beber"),
       C("**No** coma cuando está **cansado**.", "cansado")),
     P("Sí",
       C("Coma y tome **despacio**.", "comer despacio"),
       C("**Mastique** su comida **bien**.", "masticar"),
       C("**Cepille** sus dientes **5-6 veces** al día.", "cepillarse los dientes"),
       C("**Siéntese** derecho durante las comidas.", "sentarse a la mesa"),
       C("Quizás desee ver a ____________.", "médico")),
     P("Tomando medicina",
       C("Trague sus **pastillas** con **agua**.", "pastilla y agua"),
       C("Trague **1 pastilla** cada vez.", "pastilla"),
       C("**Muela** sus pastillas.", "triturar pastilla"),
       C("Trague sus **pastillas** en **puré de manzana**.", "puré de manzana")),
     P("Consejos útiles",
       C("Baje la **barbilla**.", "barbilla abajo"),
       C("Gire la cabeza a la **izquierda**.", "girar cabeza izquierda"),
       C("Gire la cabeza a la **derecha**.", "girar cabeza derecha"),
       C("Trague **fuerte**.", "tragar"),
       C("Tome **1 bocado**, luego **1 sorbo**.", "bocado y sorbo"))],
    ["Same content as the UNC handout. 'No' is written on each line of the 'No' page; please confirm.",
     "'Siéntese en posición vertical' was simplified to 'Siéntese derecho'; 'Dirija su barbilla hacia abajo' to 'Baje la barbilla'. Please check the Spanish wording with a bilingual SLP."]))

# 3 ── Communication tips ───────────────────────────────────────────────────────
PAIRS.append(pair(
    "unc-communication-tips-en", "en", "home_program", "C1.pdf", "Communication strategy recommendations",
    "Communication Strategy Recommendations for: ____________. "
    "Speaker strategies: [ ] Establish clear context before changing topic. [ ] Present one idea at a time. "
    "[ ] Verify comprehension. [ ] Use facial expression, gesture, and tone of voice. "
    "Word-retrieval strategies: [ ] Self-cueing [ ] Circumlocution (describing the target word) [ ] Written output "
    "[ ] Drawings and photographs. "
    "Self-cueing: [ ] For numbers: use an automatic counting sequence. [ ] For serial items such as days of the week: "
    "recite the series. [ ] Produce semantically related words. "
    "Circumlocution: [ ] Describe visual features. [ ] Describe function. [ ] Use gesture and pointing. [ ] Provide the antonym. "
    "Written cueing: [ ] Attempt to write the target word. [ ] Write part of the word: [ ] first letter [ ] first sound. "
    "[ ] Use a computer. "
    "Drawings and photographs: [ ] Produce simple drawings. [ ] Use photographs to provide context. "
    "Listener strategies: [ ] Establish clear context. [ ] Attend to facial expression, gesture, and tone of voice. "
    "[ ] Do not feign comprehension.",
    "Communication tips",
    [P("Communication tips",
       B("Communication tips for: ____________", "person"),
       T("Tips for **talking**, **finding words** and **listening**.", "conversation")),
     P("Tips for speaking",
       C("Make the **topic clear**.", "speech bubble"),
       C("Say **one point** at a time.", "one"),
       C("**Check** that the other person **understands**.", "question"),
       C("Use your **face**, **hands** and voice.", "gesture")),
     P("If I get stuck on a word, I can…",
       C("Give myself a **hint**.", "light bulb"),
       C("**Describe** the word.", "describe"),
       C("Use **writing**.", "write"),
       C("Use **drawings** and **photographs**.", "drawing")),
     P("Give myself a hint",
       C("For numbers: try **counting** first.", "numbers"),
       C("For a list, like the **days of the week**: say the **other days**.", "calendar"),
       C("Try saying words that are **similar**.", "similar")),
     P("Describe the word",
       C("What does it **look like**?", "look"),
       C("What is it **used for**?", "tool"),
       C("Use **gestures** and **pointing**.", "point"),
       C("Say its **opposite**.", "opposite")),
     P("Use writing",
       C("Try to **write** the word.", "write"),
       C("Write the **first letter**.", "letter"),
       C("Write the **first sound**.", "sound"),
       C("Try a **computer**.", "computer")),
     P("Use drawings and photographs",
       C("Make simple **drawings**.", "drawing"),
       C("Use **photographs** to show what you mean.", "photo")),
     P("Tips for listening",
       C("Make the **topic clear**.", "speech bubble"),
       C("**Watch** face, hands and tone of voice.", "watch face"),
       C("Do **not pretend** to understand.", "stop"))],
    ["Same content as the UNC handout, with small wording changes ('Clear context' -> 'Make the topic clear'). Please confirm.",
     "UNC nests 'first letter / first sound' under 'write part of the word'; here they are separate checkboxes."]))

# 4 ── Communication bill of rights ─────────────────────────────────────────────
PAIRS.append(pair(
    "unc-communication-rights-en", "en", "education", "Communication-bill-of-rights.pdf",
    "Communication rights (based on Brady et al., 2016, Am J Intellect Dev Disabil 121(2):121-138)",
    "Communication Rights of ____________. Every person, regardless of the type or severity of disability, "
    "holds fundamental rights related to communication. "
    "Basic rights: the right to services that improve communication; the right to communicate using spoken language; "
    "the right to communicate using nonverbal and augmentative means. "
    "Choice: the right to make choices; the right to request desired objects, actions, events, and people; "
    "the right to refuse undesired objects, actions, events, and people. "
    "Expression: the right to express feelings; the right to share opinions and ideas; the right to ask and answer questions. "
    "Social participation: the right to social interaction; the right to communication that is relevant to one's interests; "
    "the right to receive information about the people and events in one's environment. "
    "Community: the right to communicate across different settings; the right to inclusion in the community; "
    "the right to communication consistent with one's cultural and linguistic background. "
    "Communication partners: the right to receive a response; the right to be treated with dignity and respect; "
    "the right to be addressed directly rather than spoken about. These rights apply to all individuals.",
    "Communication rights",
    [P("Communication rights",
       B("Communication rights for: ____________", "person"),
       T("**Rights** are true for **everyone**.", "group of people")),
     P("Basic communication rights",
       T("The right to **improve** communication.", "improve"),
       T("The right to speak **with words**.", "talk"),
       T("The right to speak **without words**.", "gesture")),
     P("Rights for choosing",
       T("The right to have **choices**.", "choose"),
       T("The right to **ask for** things.", "request"),
       T("The right to say **no**.", "no")),
     P("Rights for sharing",
       T("The right to say your **feelings**.", "feelings"),
       T("The right to share your **ideas**.", "idea"),
       T("The right to ask **questions**.", "question")),
     P("Rights for socializing",
       T("The right to be **social**.", "friends"),
       T("The right to talk about things that **matter to you**.", "conversation"),
       T("The right to **know about people** around you.", "people")),
     P("Rights in the community",
       T("The right to communicate in **different places**.", "places"),
       T("The right to be part of the **community**.", "community"),
       T("The right to share your **culture**.", "culture")),
     P("Rights with other people",
       T("The right to get an **answer**.", "answer"),
       T("The right to **respect**.", "respect"),
       T("People should talk **to you**, not **about you**.", "talk to person")),
     P("Reminder",
       T("**Rights** are true for **everyone**.", "group of people"))],
    ["UNC wording simplified in places: 'request' -> 'ask for things', 'refuse' -> 'say no', 'relevant communication' -> "
     "'talk about things that matter to you', 'direct communication' -> 'people should talk to you, not about you'. Please confirm.",
     "Citation kept in the source line (footer), not on a page."]))

# 5 ── Tips to keep your brain healthy ──────────────────────────────────────────
PAIRS.append(pair(
    "unc-brain-health-en", "en", "education", "C8.pdf",
    "Neuroplasticity patient education (adapted from Kleim & Jones, 2008, JSLHR 51)",
    "Principles of Experience-Dependent Neuroplasticity: Patient Education. "
    "The brain can reorganize to improve cognitive function, but this change depends on active engagement. "
    "(1) Use it or lose it: cognitive domains include reasoning, memory, auditory comprehension, attention, and language. "
    "Domains that are engaged are strengthened; domains that are not engaged deteriorate. "
    "(2) Use it and improve it: improving a specific skill requires training that skill. Tasks should be challenging but achievable. "
    "(3) Specificity: choose novel, creative, and active rather than passive activities. A passive activity can be made active, "
    "for example by recording points, fouls, and time-outs while watching a basketball game. Recommended activities: keeping "
    "a journal (thoughts, goals, memories); keeping lists (plans, tasks, groceries); games (crossword, Sudoku, riddles, puzzles, "
    "Scrabble, Pictionary, Taboo, Mad Libs, cards); internet research (look up a person and record their history, research "
    "personal interests, learn a new craft or project). "
    "(4) Repetition: daily practice is required. For example, improving writing requires writing daily; writing on only 1 or 2 days "
    "is not sufficient. "
    "(5) Intensity: increased effort and time increase skill gains; meaningful change requires many hours of practice. "
    "(6) Time: begin now. The brain continues to change over a long period. "
    "(7) Salience: activities that are personally meaningful produce greater improvement. Social engagement is recommended: "
    "time with family or friends, attending church, community volunteering, and a genuine conversation every day. "
    "Patient plan: ____________.",
    "Tips to keep your brain healthy",
    [P("Keep your brain healthy",
       T("Your **brain** can **change**.", "brain"),
       T("It can improve your **thinking**.", "thinking"),
       T("But you need to **work** for it.", "work")),
     P("1. Use it or lose it",
       T("Your brain has **thinking skills**.", "brain"),
       T("Like **memory**, **listening**, **attention**, **language**.", "memory"),
       T("**Using** them makes them **stronger**.", "strong"),
       T("**Not using** them makes them **weaker**.", "weak")),
     P("2. Use it and improve it",
       T("To get better at a skill, **practice** that **skill**.", "practice"),
       T("A task should be **hard**.", "hard"),
       T("But **not impossible**.", "possible")),
     P("3. Choose the right activities",
       T("Do things that are **new** and **creative**.", "creative"),
       T("Be **active**, not **passive**.", "active"),
       T("Watch a **basketball** game.", "basketball"),
       T("Write down the **points**, **fouls** and **time-outs**.", "write")),
     P("Write things down",
       T("Keep a **diary**: thoughts, goals, memories.", "diary"),
       T("Keep a **list**: plans, things to do, groceries.", "list")),
     P("Play games",
       T("**Puzzles**: crossword, Sudoku, riddles.", "puzzle"),
       T("**Games**: Scrabble, Pictionary, Taboo, Mad Libs, cards.", "board game")),
     P("Search the internet",
       T("Look up a **person**. Write down their **history**.", "person"),
       T("Look up your **interests**.", "interests"),
       T("Learn something **new**, like a **craft**.", "craft")),
     P("4. Practice every day",
       T("Your brain needs **practice** every **day**.", "calendar"),
       T("To write better, **write** every day.", "write"),
       T("**1 or 2 days** is **not enough**.", "not enough")),
     P("5. Effort and time",
       T("**Effort** and **time** make skills grow.", "clock"),
       T("It takes **many hours**.", "hours")),
     P("6. Start now",
       T("**Now** is a good time to **start**.", "start"),
       T("Your brain keeps **changing** for a **long time**.", "brain")),
     P("7. Do what matters to you",
       T("Do things that are **important** to you.", "heart"),
       T("Your brain will **improve more**.", "improve")),
     P("Be social",
       T("**Spend time** with family or friends.", "family"),
       T("Go to **church**.", "church"),
       T("**Volunteer** in the community.", "volunteer"),
       T("Have a real **conversation** every day.", "conversation")),
     P("My plan",
       B("This is my plan: ____________", "plan"),
       B("____________", ""),
       B("____________", ""))],
    ["The UNC handout is dense (about 300 words). Here it is split into 13 short pages. Please check nothing important was lost.",
     "Spelling fixed: 'Sodoku' -> 'Sudoku'."]))

# 6 ── Independent practice ─────────────────────────────────────────────────────
PAIRS.append(pair(
    "unc-independent-practice-en", "en", "home_program", "Independent-practice.pdf", "Independent communication practice (home program)",
    "Home Exercise Program: Independent Communication Practice. The following activities support progress toward "
    "communication goals. "
    "Verbal expression: oral reading daily, repeating passages until fluent; functional scripts (write down frequently used "
    "phrases and rehearse until automatic); loudness monitoring with the Noise Meter Pro app for visual feedback on vocal "
    "loudness; confrontation naming of objects or people in the home, in magazines, or in photographs, creating a practice set, "
    "repeating it, and describing each item named. "
    "Reading comprehension: audiobooks, reading along while listening, or reading a passage independently and then listening "
    "to verify comprehension (sources: Audible reading app; BARD website, free audiobooks; LibriVox website, free audiobooks); "
    "eBooks with enlarged text and increased white space. "
    "Written expression: speech-to-text on a phone or tablet (speak the word, copy it, use it to verify spelling); texting or "
    "email, one message daily, using spell check and word prediction, and text-to-speech if stuck; Scrabble tiles (copy letters, "
    "build words, check spelling on a phone); copy and recall (copy written text such as birthday cards, greeting cards, books, "
    "emails, or texts, then attempt to write the message without looking). "
    "Auditory comprehension: podcasts (recall important details, sequence events, add a second task for challenge); "
    "listening to television without watching (record sports scores, follow soap opera plots, check understanding by watching). "
    "Conversational strategies: prepare for conversations in advance by taking photos of people or activities, creating photo "
    "albums, writing scripts on likely topics, and bringing pen and paper. "
    "You are in charge of your recovery: set personal goals and challenge yourself.",
    "Practice on your own",
    [P("Practice on your own",
       T("These activities help your **communication goals**.", "goal"),
       T("Practice **speaking**, **reading**, **writing** and **listening**.", "practice")),
     P("Speaking: read out loud",
       T("**Read out loud** every day.", "read aloud"),
       T("**Repeat** until it is **easy**.", "repeat")),
     P("Speaking: scripts",
       T("Write down **phrases** you use **every day**.", "write"),
       T("**Repeat** them until **easy**.", "repeat")),
     P("Speaking: loudness",
       T("Use the **Noise Meter Pro** app.", "phone app"),
       T("It shows how **loud** your **voice** is.", "loud")),
     P("Speaking: naming",
       T("**Name** things in your **house**, **magazines** or **photos**.", "house"),
       T("Make a **set** and **repeat** it.", "cards"),
       T("**Describe** each thing you name.", "describe")),
     P("Reading: audiobooks",
       T("**Read** while you **listen**.", "audiobook"),
       T("Or read **alone**, then **listen** to check.", "headphones")),
     P("Where to find audiobooks",
       T("**Audible**: reading app.", "phone app"),
       T("**Bard**: website, free audiobooks.", "website"),
       T("**LibriVox**: website, free audiobooks.", "website")),
     P("Reading: eBooks",
       T("Make the **text bigger**.", "big text"),
       T("Add more **white space**.", "space")),
     P("Writing: speech to text",
       T("**Say** a word into your **phone** or **tablet**.", "talk to phone"),
       T("**Copy** the word.", "copy"),
       T("Use it to check **spelling**.", "spelling")),
     P("Writing: texts and emails",
       T("Write **one** a **day**.", "text message"),
       T("Use **spell check** and **word prediction**.", "spell check"),
       T("Stuck? Use **text to speech**.", "speaker")),
     P("Writing: Scrabble tiles",
       T("**Copy** letters.", "letters"),
       T("Make **words** with the tiles.", "scrabble"),
       T("Check **spelling** on your **phone**.", "phone")),
     P("Writing: copy and recall",
       T("**Copy** cards, books, emails or texts.", "copy"),
       T("Then write it **without looking**.", "write")),
     P("Listening: podcasts",
       T("Listen to a **podcast**.", "podcast"),
       T("**Remember** the important **details**.", "remember"),
       T("Put events in **order**.", "order"),
       T("For a challenge, do **two things** at once.", "multitask")),
     P("Listening: TV",
       T("**Listen** to TV **without watching**.", "listen"),
       T("Write down **sports scores**.", "score"),
       T("Follow **soap opera** stories.", "television"),
       T("**Look** at the TV to check.", "watch tv")),
     P("Conversation tools",
       T("**Plan** conversations **ahead**.", "plan"),
       T("Take **pictures** of people and activities.", "camera"),
       T("Make **photo albums** and **scripts**.", "photo album"),
       T("Bring **pen** and **paper**.", "pen and paper")),
     P("You are in charge",
       T("You are **in charge** of your **recovery**.", "person"),
       T("Set **personal goals**.", "goal"),
       T("**Challenge** yourself!", "challenge"))],
    ["The UNC handout numbers sections (1), (2), (3), (5), (5); numbering removed here.",
     "UNC's picture is a Shutterstock image; it is not used. Pictures here are suggestions for ARASAAC.",
     "'Multitask for a challenge' -> 'For a challenge, do two things at once'."]))

# 7 ── Derrame cerebral (Spanish) ───────────────────────────────────────────────
PAIRS.append(pair(
    "unc-stroke-es", "es", "education", "Derrame-cerebral-stroke.pdf", "Derrame cerebral: información para pacientes",
    "Accidente cerebrovascular (derrame cerebral): información para pacientes. "
    "Un accidente cerebrovascular, también llamado \"ataque cerebral\", ocurre cuando se interrumpe la circulación de sangre "
    "en el cerebro. Esto sucede por la obstrucción de un vaso sanguíneo en el cerebro o el cuello (accidente isquémico), "
    "o por la ruptura de un vaso con sangrado dentro del cerebro (accidente hemorrágico). "
    "Cualquier persona puede tener un derrame cerebral. Ciertos factores de riesgo aumentan la posibilidad: edad, género, raza, "
    "antecedentes familiares de derrame cerebral, presión arterial alta, obesidad, falta de ejercicio, diabetes, enfermedad del "
    "corazón (cardiopatía), desequilibrio del colesterol y fumar cigarrillos. "
    "Los factores de riesgo que usted puede controlar son: la presión arterial alta, la obesidad, la diabetes, la cardiopatía, "
    "el desequilibrio del colesterol, fumar cigarrillos y la falta de ejercicio. Consulte a su médico para aprender cómo "
    "controlarlos. "
    "Para prevenir un derrame cerebral: visite al médico con regularidad, tome sus medicamentos como se le recetaron, "
    "deje de fumar y haga ejercicio con frecuencia. "
    "Conozca los síntomas con la palabra HEROE: H, habla incoherente o extraña; E, extremidades con parálisis, adormecimiento "
    "o debilidad; R, rostro adormecido o desviado; O, ojo cegado o paralizado; E, emergencia. "
    "Si tiene estos síntomas, llame al 911.",
    "Derrame cerebral",
    [P("¿Qué es un derrame cerebral?",
       T("Es un **\"ataque de cerebro\"**.", "cerebro"),
       T("**No llega sangre** al **cerebro**.", "cerebro")),
     P("¿Por qué no llega sangre?",
       T("Un **vaso** en el cerebro o el cuello se **tapa**.", "vaso sanguíneo"),
       T("O un vaso se **rompe** y hay **sangre** en el cerebro.", "sangre")),
     P("¿Quién puede tener un derrame?",
       T("**Cualquier persona** puede tener un derrame.", "grupo de personas"),
       T("Hay **factores de riesgo**.", "riesgo"),
       T("Estos **aumentan** la posibilidad.", "aumentar")),
     P("Factores de riesgo",
       T("**Edad**", "edad"),
       T("**Género**", "hombre y mujer"),
       T("**Raza**", "personas"),
       T("**Familia** con derrames", "familia")),
     P("Más factores de riesgo",
       T("**Presión** de sangre **alta**", "presión arterial"),
       T("**Obesidad**", "obesidad"),
       T("No hacer **ejercicio**", "sofá"),
       T("**Diabetes**", "diabetes")),
     P("Más factores de riesgo",
       T("**Enfermedad** del **corazón**", "corazón"),
       T("**Colesterol** desequilibrado", "colesterol"),
       T("**Fumar** cigarrillos", "cigarrillo")),
     P("Usted puede controlar estos",
       T("**Presión alta**, **obesidad**, **diabetes**.", "controlar"),
       T("**Corazón**, **colesterol**, **fumar**, **ejercicio**.", "controlar"),
       T("**Vaya al médico** para aprender cómo **controlarlos**.", "médico")),
     P("Consejos para prevenir un derrame",
       T("**Vaya al médico** seguido.", "médico"),
       T("Tome sus **medicinas** como le dicen.", "pastilla"),
       T("**Deje de fumar**.", "no fumar"),
       T("Haga **ejercicio** seguido.", "ejercicio")),
     P("Síntomas: HEROE",
       T("**H**: **Habla** incoherente o extraña", "hablar"),
       T("**E**: **Extremidades** con parálisis, adormecimiento o debilidad", "brazo débil"),
       T("**R**: **Rostro** adormecido o desviado", "cara"),
       T("**O**: **Ojo** cegado o paralizado", "ojo")),
     P("E: Emergencia",
       T("¿Tiene estos **síntomas**?", "ambulancia"),
       L("crisis", "Llame al 911", "ambulancia"))],
    ["Spelling fixed from the UNC handout: 'síntonmas' -> 'síntomas', 'colestorol' -> 'colesterol', 'La Diabete' -> 'Diabetes', "
     "'incoherent' -> 'incoherente', 'cigarillos' -> 'cigarrillos'.",
     "Commands changed to the usted form ('Va al médico' -> 'Vaya al médico', 'Toma' -> 'Tome', 'Deja' -> 'Deje', 'Hace' -> 'Haga').",
     "UNC's long risk-factor list (11 items) is split across 3 pages. Please check the Spanish with a bilingual SLP."]))

# 8 ── Connect iPhone to hearing aids ───────────────────────────────────────────
PAIRS.append(pair(
    "unc-iphone-hearing-aids-en", "en", "how_to", "R5.pdf", "Pairing hearing aids with iPhone (based on Apple support instructions)",
    "Pairing Made for iPhone Hearing Aids. Pairing your hearing aids with your iPhone can improve audibility for phone calls "
    "and for speech practice activities. "
    "Instructions: 1. Open the battery doors on your hearing aids. 2. Unlock your iPhone. 3. Go to Settings. 4. Select General. "
    "5. Select Accessibility. 6. Select Hearing Aids. 7. Close the battery doors on your hearing aids. 8. When the name of your "
    "hearing aids appears, tap it. 9. Tap \"Pair\" when the pairing request appears. 10. Wait; pairing can take up to one minute. "
    "11. Confirm the pairing: a check mark appears next to the hearing aid name, and hearing aid controls are available on the "
    "Lock Screen.",
    "Connect your iPhone to your hearing aids",
    [P("Why connect?",
       T("Hear **better** on **phone calls**.", "phone call"),
       T("Hear **better** for **speech practice**.", "speech practice")),
     P("How to connect",
       S("**Open** the hearing aid **battery doors**.", "hearing aid"),
       S("**Unlock** your iPhone.", "unlock phone"),
       S("Open **Settings**.", "settings"),
       S("Tap **General**.", "tap")),
     P("How to connect",
       S("Tap **Accessibility**.", "tap"),
       S("Tap **Hearing Aids**.", "hearing aid"),
       S("**Close** the hearing aid **battery doors**.", "hearing aid"),
       S("Tap the **name** of your hearing aid.", "tap")),
     P("How to connect",
       S("Tap **\"Pair\"**.", "tap"),
       S("**Wait** one minute.", "clock"),
       S("**Check** that it worked.", "check mark")),
     P("Did it work?",
       T("A **check mark** is next to your hearing aid.", "check mark"),
       T("Hearing aid **controls** are on the **Lock Screen**.", "phone"))],
    ["Steps match the UNC handout. Newer iPhones may say 'Hearing Devices' instead of 'Hearing Aids', and the menu may be "
     "under Accessibility, not General; please check against the current iPhone before printing.",
     "Step numbers continue across pages (1-11)."]))

out = Path(__file__).resolve().parent.parent / "pairs" / "unc_batch1.jsonl"
with out.open("w", encoding="utf-8") as fh:
    for p in PAIRS:
        fh.write(json.dumps(p, ensure_ascii=False) + "\n")
print(f"Wrote {len(PAIRS)} pairs to {out}")
