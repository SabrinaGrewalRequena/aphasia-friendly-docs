"""Batch 2 (Spanish): 12 made-up pairs. All names, clinics, IDs and numbers are invented
(phones use 555-01xx; websites use example.org). Approved with no changes by a CCC-SLP (anonymous) on 2026-11-11.

Run:  python data/sources/batch2_es.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from batch2_helpers import B, C, CR, P, PH, S, T, mark_reviewed, pair, write  # noqa: E402

TEL = "teléfono"

PAIRS = [
# 1 ── Aspirina ─────────────────────────────────────────────────────────────────
pair("medication-aspirina-es-001", "es", "medication", "Instrucciones de aspirina (ejemplo inventado)",
     "Instrucciones de medicamento: aspirina 81 mg. Tome 1 tableta por la boca una vez al día, con comida. La aspirina ayuda "
     "a prevenir otro derrame cerebral. No tome ibuprofeno ni naproxeno sin hablar con su médico. Llame a su médico al "
     "(919) 555-0112 si tiene moretones raros o heces negras. Llame al 911 si vomita sangre o tiene un sangrado que no para.",
     "Su medicina: aspirina",
     [P("Su medicina",
        T("Su medicina es **aspirina 81 mg**.", "pastilla"),
        T("Ayuda a **prevenir** otro **derrame cerebral**.", "cerebro")),
      P("Cómo tomarla",
        T("Tome **1 tableta**.", "pastilla"),
        T("**Una vez** al día.", "calendario"),
        T("Con **comida**.", "comida"),
        T("Por la **boca**.", "boca")),
      P("Otras medicinas",
        T("**No tome** ibuprofeno.", "no pastilla"),
        T("**No tome** naproxeno.", "no pastilla"),
        T("Primero **hable** con su **médico**.", "médico")),
      P("Llame a su médico",
        T("¿**Moretones** raros?", "moretón"),
        T("¿**Heces negras**?", "inodoro"),
        PH("Médico: (919) 555-0112", TEL)),
      P("Emergencia",
        T("¿**Vomita** sangre?", "vomitar"),
        T("¿Un **sangrado** que **no para**?", "sangre"),
        CR("Llame al 911", "ambulancia"))]),

# 2 ── Horario de medicamentos (formulario) ─────────────────────────────────────
pair("medication-schedule-es-001", "es", "medication", "Formulario de horario de medicamentos (ejemplo inventado)",
     "Horario diario de medicamentos de: ____________. Actualizado el: ____________. Mañana: medicamento ____________ "
     "dosis ____________. Mediodía: medicamento ____________ dosis ____________. Tarde/noche: medicamento ____________ dosis "
     "____________. Al acostarse: medicamento ____________ dosis ____________. [ ] Tomar con comida [ ] Tomar con un vaso "
     "lleno de agua [ ] No manejar después de tomarlo. Traiga este horario y todos sus frascos de pastillas a cada cita. "
     "Teléfono de la farmacia: ____________.",
     "Mi horario de medicinas",
     [P("Mi horario de medicinas",
        B("De: ____________", "persona"),
        B("Actualizado el: ____________", "calendario")),
      P("Mañana",
        B("Medicina: ____________", "amanecer"),
        B("Dosis: ____________", "pastilla")),
      P("Mediodía",
        B("Medicina: ____________", "sol"),
        B("Dosis: ____________", "pastilla")),
      P("Tarde y noche",
        B("Medicina: ____________", "atardecer"),
        B("Dosis: ____________", "pastilla")),
      P("Al acostarse",
        B("Medicina: ____________", "cama"),
        B("Dosis: ____________", "pastilla")),
      P("Recuerde",
        C("Tomar con **comida**.", "comida"),
        C("Tomar con un vaso lleno de **agua**.", "vaso de agua"),
        C("**No manejar** después de tomarla.", "no manejar")),
      P("Traiga a cada cita",
        T("Traiga este **horario**.", "horario"),
        T("Traiga todos sus **frascos** de pastillas.", "frasco de pastillas"),
        B("Teléfono de la farmacia: ____________", TEL))],
     ["Formulario: el clínico o farmacéutico escribe los medicamentos y marca los recordatorios."]),

# 3 ── Cita de neurología ───────────────────────────────────────────────────────
pair("appointment-neuro-es-001", "es", "appointment", "Recordatorio de cita de neurología (ejemplo inventado)",
     "Recordatorio de cita. Tiene una cita de seguimiento con el Dr. Andrés Molina, Neurología, el miércoles 7 de abril de "
     "2027 a las 11:15 a.m. Lugar: Plaza Médica Westfield, 600 Oakmont Drive, Suite 310. No tiene que traer un intérprete; "
     "la clínica le dará un intérprete de español gratis. Traiga su registro de presión arterial y una lista de sus "
     "medicamentos. Para cancelar, llame por lo menos 24 horas antes al (919) 555-0113.",
     "Su cita",
     [P("Su cita",
        T("Con el **Dr. Andrés Molina**.", "médico"),
        T("Es en **Neurología**.", "cerebro"),
        T("**miércoles 7 de abril de 2027**", "calendario"),
        T("**11:15 a.m.**", "reloj")),
      P("Dónde",
        T("**Plaza Médica Westfield**", "hospital"),
        T("**600 Oakmont Drive, Suite 310**", "mapa")),
      P("Intérprete",
        T("La clínica le da un **intérprete** de **español**.", "intérprete"),
        T("Es **gratis**.", "gratis"),
        T("**No tiene que** traer uno.", "no")),
      P("Qué traer",
        S("Su registro de **presión arterial**.", "presión arterial"),
        S("Una **lista** de sus **medicamentos**.", "lista de medicamentos")),
      P("¿Necesita cancelar?",
        T("Llame por lo menos **24 horas** antes.", "reloj"),
        PH("Teléfono: (919) 555-0113", TEL))]),

# 4 ── Visita por video ─────────────────────────────────────────────────────────
pair("appointment-telehealth-es-001", "es", "appointment", "Instrucciones de visita por video (ejemplo inventado)",
     "Su visita de terapia del habla por video. Su visita por video con Alex Romero, M.A., CCC-SLP, es el jueves 18 de marzo "
     "de 2027 a las 4:00 p.m. 15 minutos antes, abra el mensaje de texto de la Clínica del Habla Piedmont y toque el enlace. "
     "También puede entrar en www.example.org/visita. Necesita un teléfono, tableta o computadora con cámara y micrófono. "
     "Busque un cuarto tranquilo. Si tiene problemas técnicos, llame al (919) 555-0114.",
     "Su visita por video",
     [P("Su visita por video",
        T("Usted tiene una **visita por video**.", "videollamada"),
        T("Es **terapia del habla**.", "terapeuta del habla"),
        T("Con **Alex Romero, M.A., CCC-SLP**.", "terapeuta del habla")),
      P("Cuándo",
        T("**jueves 18 de marzo de 2027**", "calendario"),
        T("**4:00 p.m.**", "reloj")),
      P("Qué necesita",
        T("Un **teléfono**, **tableta** o **computadora**.", "computadora"),
        T("Con **cámara** y **micrófono**.", "cámara"),
        T("Busque un cuarto **tranquilo**.", "silencio")),
      P("Cómo entrar",
        S("Espere hasta **15 minutos** antes.", "reloj"),
        S("Abra el **mensaje de texto** de la Clínica del Habla Piedmont.", "mensaje de texto"),
        S("**Toque** el **enlace**.", "tocar"),
        T("O entre en: **www.example.org/visita**", "sitio web")),
      P("¿Necesita ayuda?",
        T("¿Problemas con la **tecnología**? **Llame**.", "ayuda"),
        PH("Ayuda: (919) 555-0114", TEL))]),

# 5 ── Consentimiento para grabar ───────────────────────────────────────────────
pair("consent-recording-es-001", "es", "consent", "Consentimiento para grabación (ejemplo inventado)",
     "Consentimiento para grabación de audio y video. Durante la terapia del habla, su terapeuta puede grabar sus sesiones. "
     "Las grabaciones ayudan a seguir su progreso y se pueden usar para enseñar a estudiantes. Las grabaciones se guardan de "
     "forma segura y no se comparten fuera de la Clínica del Habla Piedmont sin su permiso por escrito. Usted puede decir que "
     "no. Decir que no no cambia su atención. Puede cambiar de opinión en cualquier momento; solo dígale a su terapeuta. "
     "Por favor escoja: [ ] Acepto que me graben para seguir mi progreso. [ ] Acepto que me graben para enseñar a estudiantes. "
     "[ ] No acepto que me graben. Firma: ____________ Fecha: ____________",
     "Grabar su terapia",
     [P("Grabar su terapia",
        T("Su terapeuta puede **grabar** sus sesiones.", "cámara de video"),
        T("**Sonido** y **video**.", "micrófono")),
      P("¿Por qué grabar?",
        T("Para ver su **progreso**.", "gráfica"),
        T("Para **enseñar** a estudiantes.", "estudiantes")),
      P("Sus grabaciones están seguras",
        T("Se guardan de forma **segura**.", "candado"),
        T("Se quedan en la **Clínica del Habla Piedmont**.", "clínica"),
        T("Se comparten **solo** si usted dice **sí** por escrito.", "firma")),
      P("Usted decide",
        T("Usted puede decir **no**.", "no"),
        T("Decir no **no cambia** su **atención**.", "atención médica"),
        T("Puede **cambiar de opinión** cuando quiera.", "cambiar"),
        T("Solo dígale a su **terapeuta**.", "terapeuta del habla")),
      P("Por favor escoja",
        C("**Sí**, grábenme para ver mi **progreso**.", "sí"),
        C("**Sí**, grábenme para **enseñar** a estudiantes.", "sí"),
        C("**No**, no me graben.", "no")),
      P("Firme",
        B("Firma: ____________", "firma"),
        B("Fecha: ____________", "calendario"))],
     ["Formulario de consentimiento: el equipo legal o de privacidad de la clínica también debe aprobar el texto."]),

# 6 ── Aviso del seguro ─────────────────────────────────────────────────────────
pair("insurance-approval-es-001", "es", "insurance", "Aviso de autorización del seguro (ejemplo inventado)",
     "Aviso de autorización. Miembro: Carmen Ruiz. Número de miembro: MCD772019. Su plan de salud, Plan Comunitario de Salud "
     "de Carolina, aprobó 8 visitas de terapia ocupacional en Lakeside Therapy Partners. Debe usar estas visitas entre el "
     "1 de febrero de 2027 y el 31 de julio de 2027. Usted no tiene que pagar copago por estas visitas. Si necesita más "
     "visitas, su terapeuta debe pedirlas antes de que se terminen. Si tiene preguntas, llame a Servicios para Miembros al "
     "1-800-555-0115 (TTY 711).",
     "Su terapia está aprobada",
     [P("Su terapia está aprobada",
        T("Para: **Carmen Ruiz**", "persona"),
        T("Número de miembro: **MCD772019**", "tarjeta"),
        T("Su **plan de salud** dijo que **sí**.", "sí"),
        T("**Plan Comunitario de Salud de Carolina**", "tarjeta de seguro")),
      P("Cuántas visitas",
        T("**8 visitas** de **terapia ocupacional**.", "terapia ocupacional"),
        T("En **Lakeside Therapy Partners**.", "clínica")),
      P("Cuándo",
        T("Úselas entre el **1 de febrero de 2027**", "calendario"),
        T("y el **31 de julio de 2027**.", "calendario")),
      P("Costo",
        T("Usted **no paga** copago.", "dinero")),
      P("¿Necesita más visitas?",
        T("Su **terapeuta** debe **pedirlas**.", "terapeuta"),
        T("Antes de que se **terminen**.", "calendario")),
      P("¿Preguntas?",
        T("Llame a **Servicios para Miembros**.", "ayuda"),
        PH("Teléfono: 1-800-555-0115", TEL),
        PH("TTY: 711", "tty"))]),

# 7 ── Programa en casa: comprensión (casillas) ─────────────────────────────────
pair("home-program-listening-es-001", "es", "home_program", "Programa de práctica en casa: comprensión (ejemplo inventado)",
     "Programa de práctica en casa: comprensión. Haga las actividades marcadas por 15 minutos, 5 días a la semana. "
     "[ ] Escuche las noticias y diga 2 cosas que escuchó. [ ] Siga instrucciones de 2 pasos (por ejemplo, \"toque la mesa y "
     "luego la puerta\"). [ ] Lea una receta corta y responda preguntas de sí o no. [ ] Mire fotos de su familia y diga quién "
     "es cada persona. [ ] Escuche una canción y diga de qué se trata. Anote su práctica en la hoja de registro y tráigala a "
     "su próxima sesión. Su terapeuta: ____________",
     "Practicar en casa: entender",
     [P("Practique en casa",
        T("Practique **entender** lo que oye y lee.", "escuchar"),
        T("**15 minutos** al día.", "reloj"),
        T("**5 días** a la semana.", "calendario")),
      P("Haga las actividades marcadas",
        C("Escuche las **noticias**. Diga **2 cosas** que escuchó.", "noticias"),
        C("Siga **instrucciones** de **2 pasos**. (Ejemplo: \"toque la mesa y luego la puerta\")", "instrucciones"),
        C("Lea una **receta** corta. Responda **sí** o **no**.", "receta")),
      P("Más actividades",
        C("Mire **fotos** de su **familia**. Diga quién es cada persona.", "fotos de familia"),
        C("Escuche una **canción**. Diga de qué se **trata**.", "música")),
      P("Anote su práctica",
        T("Anote su práctica en la **hoja de registro**.", "hoja de registro"),
        T("**Tráigala** a su próxima **sesión**.", "terapeuta del habla"),
        B("Su terapeuta: ____________", "terapeuta del habla"))]),

# 8 ── Resultados de habla y lenguaje (casillas) ────────────────────────────────
pair("results-language-es-001", "es", "results", "Resumen de evaluación de habla y lenguaje (ejemplo inventado)",
     "Evaluación de habla y lenguaje: resumen de resultados de ____________. Diagnóstico: [ ] Afasia expresiva [ ] Afasia "
     "receptiva [ ] Afasia global [ ] Apraxia del habla [ ] Disartria. Áreas de dificultad: [ ] Encontrar palabras "
     "[ ] Comprensión auditiva [ ] Comprensión de lectura [ ] Expresión escrita [ ] Inteligibilidad del habla. "
     "Recomendación: terapia de habla y lenguaje ___ veces por semana por ___ semanas. Metas: [ ] Mejorar encontrar palabras "
     "en la conversación [ ] Mejorar la comprensión de instrucciones de varios pasos [ ] Mejorar la lectura funcional (por "
     "ejemplo, etiquetas de medicamentos) [ ] Usar un libro o aparato de comunicación. Su terapeuta: ____________ "
     "Teléfono: ____________",
     "Sus resultados de habla y lenguaje",
     [P("Sus resultados",
        B("Resultados de: ____________", "persona"),
        T("Usted hizo una prueba de **habla** y **lenguaje**.", "terapeuta del habla")),
      P("Lo que usted tiene",
        C("Le cuesta **decir** lo que quiere (**afasia expresiva**).", "hablar"),
        C("Le cuesta **entender** palabras (**afasia receptiva**).", "escuchar"),
        C("Le cuesta **hablar** y **entender** (**afasia global**).", "hablar y escuchar"),
        C("Le cuesta **mover** la boca para hablar (**apraxia del habla**).", "boca"),
        C("Los músculos del habla están **débiles**; el habla no es **clara** (**disartria**).", "boca")),
      P("Lo que le cuesta",
        C("**Encontrar** palabras.", "buscar"),
        C("**Entender** lo que dicen.", "escuchar"),
        C("**Leer**.", "leer"),
        C("**Escribir**.", "escribir"),
        C("Que otros **entiendan** su habla.", "conversación")),
      P("Su terapia",
        B("Terapia del habla ___ veces por semana.", "calendario"),
        B("Por ___ semanas.", "calendario")),
      P("Sus metas",
        C("Encontrar **palabras** cuando **habla**.", "hablar"),
        C("Seguir **instrucciones** con varios **pasos**.", "pasos"),
        C("**Leer** cosas como **etiquetas de medicamentos**.", "etiqueta de medicina"),
        C("Usar un **libro** o **aparato** de comunicación.", "libro de comunicación")),
      P("Su terapeuta",
        B("Terapeuta: ____________", "terapeuta del habla"),
        B("Teléfono: ____________", TEL))],
     ["Los nombres de diagnóstico van entre paréntesis después de una explicación simple. Por favor revise que las explicaciones sean correctas."]),

# 9 ── Alta de terapia del habla ────────────────────────────────────────────────
pair("discharge-therapy-es-001", "es", "discharge", "Resumen de alta de terapia del habla (ejemplo inventado)",
     "Resumen de alta: terapia del habla. Paciente: Jorge Castillo. Fechas: del 14 de septiembre de 2026 al 5 de febrero de "
     "2027. Sesiones: 28. Metas cumplidas: decir frases cortas para pedir lo que necesita; usar gestos para comunicarse. "
     "Recomendaciones: continuar el programa de práctica en casa 3 días a la semana; asistir al Grupo de Apoyo Juntos. "
     "Si nota cambios nuevos en su habla, pida a su médico un nuevo referido o llame al (919) 555-0116.",
     "Terminó su terapia del habla",
     [P("Terminó su terapia",
        T("Para: **Jorge Castillo**", "persona"),
        T("Su **terapia del habla** **terminó**.", "terminar"),
        T("Del **14 de septiembre de 2026** al **5 de febrero de 2027**.", "calendario"),
        T("Usted vino **28 veces**.", "calendario")),
      P("Lo que logró",
        T("Usted dice **frases cortas** para **pedir** lo que necesita.", "hablar"),
        T("Usted usa **gestos** para comunicarse.", "gestos")),
      P("Siga practicando",
        T("Haga su **práctica en casa** **3 días** a la semana.", "practicar"),
        T("Vaya al **Grupo de Apoyo Juntos**.", "grupo")),
      P("Vuelva si",
        T("¿Nota **cambios nuevos** en su **habla**?", "hablar"),
        T("Pida a su **médico** un **nuevo referido**.", "médico"),
        T("O **llame**.", TEL),
        PH("Teléfono: (919) 555-0116", TEL))]),

# 10 ── ¿Qué es la afasia? ──────────────────────────────────────────────────────
pair("education-aphasia-es-001", "es", "education", "Información sobre la afasia (ejemplo inventado)",
     "Afasia: información para pacientes y familias. La afasia es un trastorno adquirido del lenguaje causado por daño en las "
     "áreas del lenguaje del cerebro, casi siempre por un derrame cerebral. Puede afectar el habla, la comprensión, la lectura "
     "y la escritura. La afasia no afecta la inteligencia. Las personas con afasia saben lo que quieren decir, pero les puede "
     "costar encontrar las palabras. La terapia del habla puede mejorar la comunicación, y muchas personas siguen mejorando "
     "por años. La familia puede ayudar si habla despacio, usa frases cortas, escribe palabras clave y da más tiempo. Para más "
     "información, llame a la Clínica del Habla Piedmont al (919) 555-0117.",
     "¿Qué es la afasia?",
     [P("¿Qué es la afasia?",
        T("La afasia es un problema del **lenguaje**.", "globo de diálogo"),
        T("Viene de un **daño** en el **cerebro**.", "cerebro"),
        T("Casi siempre por un **derrame cerebral**.", "derrame cerebral")),
      P("Qué afecta",
        T("**Hablar**", "hablar"),
        T("**Entender**", "escuchar"),
        T("**Leer**", "leer"),
        T("**Escribir**", "escribir")),
      P("Usted sigue siendo inteligente",
        T("La afasia **no** cambia su **inteligencia**.", "cerebro"),
        T("Usted **sabe** lo que quiere decir.", "idea"),
        T("Encontrar las **palabras** puede **costar**.", "buscar")),
      P("Puede mejorar",
        T("La **terapia del habla** puede ayudar.", "terapeuta del habla"),
        T("Muchas personas **mejoran** por **años**.", "mejorar")),
      P("Cómo puede ayudar la familia",
        T("Hable **despacio**.", "despacio"),
        T("Use frases **cortas**.", "corto"),
        T("**Escriba** palabras clave.", "escribir"),
        T("Dé **más tiempo**.", "reloj")),
      P("Más información",
        T("Llame a la **Clínica del Habla Piedmont**.", "clínica"),
        PH("Teléfono: (919) 555-0117", TEL))]),

# 11 ── Cuidar al cuidador ──────────────────────────────────────────────────────
pair("mental-health-caregiver-es-001", "es", "mental_health", "Cuidando al cuidador (ejemplo inventado)",
     "Cuidando al cuidador. Cuidar a un familiar después de un derrame cerebral puede causar estrés. Es común sentirse cansado, "
     "abrumado o solo. Cuidarse a sí mismo le ayuda a cuidar a su familiar. Pida ayuda a familiares y amigos con tareas "
     "específicas, como comidas o transporte. Tome descansos cortos cada día. El grupo Cuidadores Unidos se reúne en línea cada "
     "jueves a las 7:00 p.m.; inscríbase en www.example.org/cuidadores. Para servicios de relevo, llame a la Agencia del Área "
     "para Personas Mayores al (919) 555-0118. Si está en crisis, llame o envíe un mensaje de texto al 988.",
     "Cuidar al cuidador",
     [P("Cuidar es difícil",
        T("Cuidar a un **familiar** puede causar **estrés**.", "cuidador"),
        T("Es **común** sentirse **cansado**.", "cansado"),
        T("O **abrumado**, o **solo**.", "solo")),
      P("Cuídese usted también",
        T("Cuidarse le ayuda a **cuidar** a su **familiar**.", "corazón"),
        T("Tome **descansos cortos** cada día.", "descanso")),
      P("Pida ayuda",
        T("Pida **ayuda** a familia y amigos.", "familia"),
        T("Con **comidas**.", "comida"),
        T("Con **transporte**.", "carro")),
      P("Un grupo en línea",
        T("Grupo **Cuidadores Unidos**", "grupo"),
        T("Cada **jueves** a las **7:00 p.m.**", "calendario"),
        T("Inscríbase en: **www.example.org/cuidadores**", "sitio web")),
      P("Servicios de relevo",
        T("Alguien puede **cuidar** a su familiar por un **rato**.", "cuidador"),
        T("**Llame** a la Agencia del Área para Personas Mayores.", "edificio"),
        PH("Teléfono: (919) 555-0118", TEL)),
      P("Ayuda ahora",
        T("¿Está en **crisis**?", "ayuda"),
        CR("Llame o envíe un mensaje de texto al 988", TEL))],
     ["'Servicios de relevo' se explica como 'alguien puede cuidar a su familiar por un rato'. Por favor confirme."]),

# 12 ── Referido a trabajo social ───────────────────────────────────────────────
pair("referral-social-work-es-001", "es", "referral", "Referido a trabajo social (ejemplo inventado)",
     "Referido a trabajo social. Su médico lo refirió a la trabajadora social Ana Beltrán. Ella puede ayudarle con transporte "
     "a sus citas, solicitudes de beneficios como Medicaid y recursos de comida en su comunidad. Ella lo llamará en los "
     "próximos 5 días hábiles. Si no recibe una llamada, llame al (919) 555-0122. Su oficina está en el Hospital Comunitario "
     "San Marcos, segundo piso, sala 214.",
     "Una trabajadora social le puede ayudar",
     [P("Una trabajadora social",
        T("Su médico quiere que hable con **Ana Beltrán**.", "persona"),
        T("Ella es **trabajadora social**.", "trabajadora social")),
      P("Ella le puede ayudar con",
        T("**Transporte** a sus citas.", "carro"),
        T("**Beneficios**, como **Medicaid**.", "formulario"),
        T("**Comida** en su comunidad.", "comida")),
      P("Dónde está",
        T("**Hospital Comunitario San Marcos**", "hospital"),
        T("**Segundo piso**, **sala 214**.", "puerta")),
      P("Ella lo va a llamar",
        T("Ella lo **llamará** en **5 días hábiles**.", TEL),
        T("¿No lo llamó? **Llame** usted.", TEL),
        PH("Teléfono: (919) 555-0122", TEL))]),
]

mark_reviewed(PAIRS, "CCC-SLP (anonymous)", "2026-11-11")
write(PAIRS, "batch2_es.jsonl")
