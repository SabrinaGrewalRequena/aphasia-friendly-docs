"""Batch 4 (Spanish): 15 made-up pairs for document types the set had few of (consent,
insurance, how-to, procedure, referral, letters, equipment). All names, clinics, IDs and
numbers are invented (phones use 555-01xx; websites use example.org). Approved with no changes by a CCC-SLP (anonymous) on 2026-11-12.

Run:  python data/sources/batch4_es.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from batch2_helpers import B, C, CR, P, PH, S, T, mark_reviewed, pair, write  # noqa: E402,F401

TEL = "teléfono"
PHs = lambda t: PH(t, TEL)

PAIRS = [
# 1 ── Consentimiento para telesalud ────────────────────────────────────────────
pair("consentimiento-telesalud-es-001", "es", "consent", "Consentimiento para telesalud (ejemplo inventado)",
     "CONSENTIMIENTO PARA SERVICIOS DE TELESALUD — Clínica del Habla Piedmont\n"
     "Telesalud significa recibir terapia del habla por video en vivo, en lugar de ir a la clínica. Su terapeuta usará una "
     "plataforma de video segura. Las sesiones no se graban sin su permiso por escrito. Puede haber problemas con la imagen "
     "o el sonido y, en raras ocasiones, interrupciones o fallas de privacidad. Usted puede terminar una sesión en cualquier "
     "momento y pedir una visita en persona. Su seguro puede pagar la telesalud de forma diferente; pregunte a su plan.\n"
     "[ ] Acepto recibir terapia del habla por telesalud.\n"
     "[ ] No acepto telesalud. Quiero solo visitas en persona.\n"
     "Firma del paciente: ____________ Fecha: ____________\n"
     "Preguntas: (919) 555-0165",
     "Terapia del habla por video",
     [P("Terapia por video",
        T("Puede recibir **terapia del habla** por **video**.", "videollamada"),
        T("En lugar de ir a la **clínica**.", "clínica"),
        T("El video es **seguro**.", "candado")),
      P("Grabación",
        T("**No grabamos** el video.", "no cámara"),
        T("Solo si usted dice que **sí** por **escrito**.", "firma")),
      P("Posibles problemas",
        T("La **imagen** o el **sonido** pueden fallar.", "videollamada"),
        T("A veces la llamada se puede **cortar**.", "pausa"),
        T("Rara vez puede fallar la **privacidad**.", "candado")),
      P("Usted decide",
        T("Puede **terminar** cuando quiera.", "parar"),
        T("Puede pedir una visita **en persona**.", "clínica"),
        T("Su **seguro** puede pagar **diferente**. Pregunte a su plan.", "tarjeta de seguro")),
      P("Por favor escoja",
        C("**Sí**, quiero terapia por **video**.", "sí"),
        C("**No**, quiero solo visitas **en persona**.", "no")),
      P("Firme",
        B("Firma: ____________", "firma"),
        B("Fecha: ____________", "calendario"),
        PHs("¿Preguntas? Llame al (919) 555-0165"))],
     ["Formulario de consentimiento: el equipo legal o de privacidad de la clínica también debe aprobar el texto."]),

# 2 ── Autorización para compartir información ──────────────────────────────────
pair("autorizacion-informacion-es-001", "es", "consent", "Autorización para compartir información médica (ejemplo inventado)",
     "AUTORIZACIÓN PARA DIVULGAR INFORMACIÓN MÉDICA\n"
     "Paciente: Isabel Fuentes | Fecha de nacimiento: 09/11/1960\n"
     "Yo autorizo a la Clínica del Habla Piedmont a compartir mi información médica con: Nombre: ____________ Relación: "
     "____________\n"
     "Información que se puede compartir: [ ] Resultados de evaluaciones [ ] Notas de terapia [ ] Horario de citas "
     "[ ] Toda mi información de terapia del habla.\n"
     "Esta autorización vence el 31 de diciembre de 2027, a menos que yo la cancele antes por escrito. No tengo que firmar "
     "esta autorización para recibir tratamiento. La información compartida puede ya no estar protegida por las leyes de "
     "privacidad.\n"
     "Firma: ____________ Fecha: ____________",
     "Compartir su información médica",
     [P("Compartir su información",
        T("Para: **Isabel Fuentes**", "persona"),
        T("Usted puede dejar que la clínica **comparta** su información.", "compartir"),
        T("Con una **persona** que usted **escoja**.", "persona")),
      P("¿Con quién?",
        B("Nombre: ____________", "persona"),
        B("Relación: ____________", "familia")),
      P("¿Qué información?",
        C("**Resultados** de evaluaciones", "informe"),
        C("**Notas** de terapia", "notas"),
        C("**Horario** de citas", "calendario"),
        C("**Toda** mi información de terapia del habla", "carpeta")),
      P("¿Hasta cuándo?",
        T("Hasta el **31 de diciembre de 2027**.", "calendario"),
        T("Puede **cancelarla** antes, **por escrito**.", "escribir")),
      P("Importante",
        T("**No tiene que** firmar para recibir **tratamiento**.", "no"),
        T("La información compartida puede ya **no estar protegida**.", "candado abierto")),
      P("Firme",
        B("Firma: ____________", "firma"),
        B("Fecha: ____________", "calendario"))],
     ["Formulario legal (HIPAA): la clínica debe aprobar el texto. 'Ya no estar protegida por las leyes de privacidad' se acortó."],
     omitted=["Fecha de nacimiento 09/11/1960: no la necesita el lector"]),

# 3 ── Negación del seguro con apelación ────────────────────────────────────────
pair("negacion-seguro-es-001", "es", "insurance", "Carta de negación del seguro (ejemplo inventado)",
     "AVISO DE NEGACIÓN DE COBERTURA\n"
     "Miembro: Teresa Campos | Número de miembro: MCD660314 | Plan: Plan Comunitario de Salud de Carolina\n"
     "Su solicitud de una silla de ruedas eléctrica fue negada. Motivo: la información recibida no muestra que una silla de "
     "ruedas manual o un andador no sean suficientes para usted.\n"
     "SU DERECHO A APELAR: Usted o alguien que usted escoja, como su médico, puede pedirnos que revisemos esta decisión. Debe "
     "apelar dentro de 60 días a partir de la fecha de esta carta. Envíe información nueva, como notas de su terapeuta "
     "físico. Para apelar, llame a Servicios para Miembros al 1-800-555-0115 (TTY 711).\n"
     "Si no está de acuerdo con la decisión de la apelación, puede pedir una revisión externa independiente.\n"
     "Ayuda gratis: Línea de Ayuda de Seguros Médicos 1-800-555-0162. Hay intérpretes de español.",
     "Su seguro dijo que no",
     [P("Su seguro dijo que no",
        T("Para: **Teresa Campos**", "persona"),
        T("Número de miembro: **MCD660314**", "tarjeta"),
        T("Usted pidió una **silla de ruedas eléctrica**.", "silla de ruedas eléctrica"),
        T("Su plan dijo que **no**.", "no")),
      P("Por qué",
        T("El plan cree que una silla **manual** o un **andador** pueden ser **suficientes**.", "andador")),
      P("Puede apelar",
        T("**Apelar** es pedir que lo **revisen otra vez**.", "revisar"),
        T("Usted o alguien que **escoja** lo puede hacer.", "persona"),
        T("Su **médico** puede ayudar.", "médico")),
      P("Fecha límite",
        T("Apele dentro de **60 días** de la fecha de la carta.", "calendario"),
        T("Envíe **información nueva**, como notas de su **terapeuta físico**.", "documento")),
      P("Cómo apelar",
        T("Llame a **Servicios para Miembros**.", TEL),
        PHs("Teléfono: 1-800-555-0115"),
        PH("TTY: 711", "tty")),
      P("¿Sigue sin estar de acuerdo?",
        T("Pida una **revisión externa**.", "revisar"),
        T("Alguien **fuera** del plan la va a revisar.", "persona")),
      P("Ayuda gratis",
        T("**Línea de Ayuda de Seguros Médicos**", "ayuda"),
        T("Hay **intérpretes** de **español**.", "intérprete"),
        PHs("Teléfono: 1-800-555-0162"))],
     ["'La información recibida no muestra que una silla manual o un andador no sean suficientes' se explicó como 'el plan cree que pueden ser suficientes'. Por favor confirme."]),

# 4 ── Cómo llenar el pastillero ────────────────────────────────────────────────
pair("como-pastillero-es-001", "es", "how_to", "Cómo llenar el pastillero semanal (ejemplo inventado)",
     "CÓMO LLENAR SU PASTILLERO SEMANAL\n"
     "Use un pastillero de 7 días con 2 horarios por día (mañana y noche).\n"
     "1. Escoja un día de la semana para llenarlo, por ejemplo el domingo. 2. Lávese y séquese las manos. 3. Ponga en fila "
     "sus frascos de pastillas y su lista de medicamentos. 4. Llene un medicamento a la vez: póngalo en cada cajita donde va "
     "y luego guarde el frasco. 5. Al terminar, compare cada cajita con su lista. 6. Cierre todas las tapas.\n"
     "No ponga en el pastillero medicamentos líquidos, inhaladores ni pastillas que deben quedarse en su paquete.\n"
     "Si una pastilla tiene otro color o forma, llame a su farmacia antes de tomarla: (919) 555-0149.\n"
     "Pida a un familiar o a su farmacéutico que revise su pastillero las primeras veces.",
     "Cómo llenar su pastillero",
     [P("Su pastillero",
        T("Su pastillero tiene **7 días**.", "pastillero"),
        T("**2 horarios**: **mañana** y **noche**.", "sol y luna")),
      P("Prepárese",
        S("Escoja **un día** cada semana, como el **domingo**.", "calendario"),
        S("**Lávese** y **séquese** las manos.", "lavarse las manos"),
        S("Ponga en fila sus **frascos** y su **lista**.", "frasco de pastillas")),
      P("Llénelo",
        S("Llene **un medicamento** a la vez.", "pastilla"),
        S("Póngalo en **cada cajita** donde va.", "pastillero"),
        S("**Guarde** ese frasco.", "frasco de pastillas")),
      P("Revíselo",
        S("**Compare** cada cajita con su **lista**.", "revisar"),
        S("**Cierre** todas las tapas.", "cerrar")),
      P("No van en el pastillero",
        T("Medicamentos **líquidos**.", "jarabe"),
        T("**Inhaladores**.", "inhalador"),
        T("Pastillas que deben quedarse en su **paquete**.", "blíster")),
      P("Pida ayuda",
        T("Pida a un **familiar** o a su **farmacéutico** que lo revise.", "familia"),
        T("Las **primeras veces**.", "calendario")),
      P("¿Pastilla diferente?",
        T("¿Otro **color** u otra **forma**?", "pastilla"),
        T("**Llame** a su farmacia **antes** de tomarla.", "farmacia"),
        PHs("Farmacia: (919) 555-0149"))],
     ["El paso 4 del original se dividió en 3 pasos; los números de los pasos cambian."]),

# 5 ── Cómo tomarse la presión ──────────────────────────────────────────────────
pair("como-presion-es-001", "es", "how_to", "Cómo tomarse la presión en casa (ejemplo inventado)",
     "CÓMO TOMARSE LA PRESIÓN ARTERIAL EN CASA\n"
     "Antes: no fume, no haga ejercicio y no tome café por 30 minutos. Vaya al baño.\n"
     "Pasos: 1. Siéntese en una silla con la espalda apoyada y los dos pies en el piso. 2. Descanse en silencio por 5 minutos. "
     "3. Póngase el brazalete en la parte de arriba del brazo, sin ropa, a la altura del corazón. 4. Oprima el botón. No hable "
     "ni se mueva. 5. Anote los dos números y la hora. 6. Espere 1 minuto y tómela otra vez.\n"
     "Su meta: menos de 130/80. Traiga sus anotaciones a cada cita.\n"
     "Llame a su médico al (919) 555-0144 si el número de arriba es más de 180 o el de abajo es más de 110 en dos lecturas.\n"
     "Llame al 911 si su presión está así de alta Y tiene dolor de pecho, dificultad para hablar, debilidad o cambios en la "
     "vista.",
     "Tomarse la presión",
     [P("Antes",
        T("**No fume**, no haga **ejercicio**, no tome **café** por **30 minutos**.", "no café"),
        T("Vaya al **baño** primero.", "inodoro")),
      P("Siéntese y descanse",
        S("**Siéntese** con la **espalda** apoyada.", "silla"),
        S("Los dos **pies** en el **piso**.", "pies"),
        S("**Descanse** en silencio **5 minutos**.", "reloj")),
      P("Póngase el brazalete",
        S("En la parte de **arriba** del **brazo**, sin ropa.", "brazalete de presión"),
        S("A la altura del **corazón**.", "corazón")),
      P("Tome la lectura",
        S("Oprima el **botón**. **No hable** ni se mueva.", "botón"),
        S("**Anote** los dos números y la **hora**.", "escribir"),
        S("Espere **1 minuto**. Tómela **otra vez**.", "reloj")),
      P("Su meta",
        T("Menos de **130/80**.", "meta"),
        T("Traiga sus **anotaciones** a **cada cita**.", "lista")),
      P("Llame a su médico",
        T("¿El número de **arriba** más de **180**?", "presión arterial"),
        T("¿O el de **abajo** más de **110**?", "presión arterial"),
        T("¿En **dos** lecturas? **Llame**.", TEL),
        PHs("Médico: (919) 555-0144")),
      P("Emergencia",
        T("¿Presión **así de alta**, y además:", "advertencia"),
        T("¿**Dolor de pecho**? ¿Le cuesta **hablar**?", "dolor de pecho"),
        T("¿**Debilidad**? ¿Cambios en la **vista**?", "brazo débil"),
        CR("Llame al 911", "ambulancia"))]),

# 6 ── Electroencefalograma ─────────────────────────────────────────────────────
pair("procedimiento-eeg-es-001", "es", "procedure", "Preparación para electroencefalograma (ejemplo inventado)",
     "ELECTROENCEFALOGRAMA (EEG) DE RUTINA — INSTRUCCIONES\n"
     "Un EEG registra la actividad eléctrica de su cerebro con pequeños discos de metal (electrodos) que se pegan en la cabeza "
     "con una pasta. No duele y no le pasa electricidad al cuerpo.\n"
     "Cita: martes 23 de febrero de 2027 a las 8:30 a.m., Pruebas de Neurología, Plaza Médica Westfield, 600 Oakmont Drive, "
     "Suite 310.\n"
     "La noche antes: lávese el pelo solo con champú. No use acondicionador, aceite, gel ni laca.\n"
     "Tome sus medicamentos de siempre, a menos que su médico le diga otra cosa. No tome café ni bebidas con cafeína el día "
     "de la prueba.\n"
     "La prueba dura de 60 a 90 minutos. Le pueden pedir que respire hondo y que mire una luz que parpadea.\n"
     "Para cambiar la cita: (919) 555-0113.",
     "Su prueba de ondas del cerebro (EEG)",
     [P("Su EEG",
        T("Un **EEG** revisa las **ondas** de su **cerebro**.", "cerebro"),
        T("Le pegan **discos de metal** en la **cabeza** con una **pasta**.", "electrodos")),
      P("No duele",
        T("**No duele**.", "sin dolor"),
        T("**No** le pasa **electricidad** al cuerpo.", "sin electricidad")),
      P("Cuándo y dónde",
        T("**martes 23 de febrero de 2027**", "calendario"),
        T("**8:30 a.m.**", "reloj"),
        T("**Pruebas de Neurología**, **Plaza Médica Westfield**", "hospital"),
        T("**600 Oakmont Drive, Suite 310**", "mapa")),
      P("La noche antes",
        T("Lávese el **pelo** solo con **champú**.", "champú"),
        T("**Sin** acondicionador, aceite, gel ni laca.", "no")),
      P("Medicinas y café",
        T("Tome sus **medicinas** de siempre.", "pastilla"),
        T("A menos que su **médico** diga otra cosa.", "médico"),
        T("**Sin café** ni **cafeína** el día de la prueba.", "no café")),
      P("Durante la prueba",
        T("Dura de **60 a 90 minutos**.", "reloj"),
        T("Puede que **respire hondo**.", "respirar"),
        T("Puede que mire una **luz** que **parpadea**.", "luz")),
      P("Cambiar la cita",
        PHs("Teléfono: (919) 555-0113"))]),

# 7 ── Ecocardiograma ───────────────────────────────────────────────────────────
pair("procedimiento-eco-es-001", "es", "procedure", "Preparación para ecocardiograma (ejemplo inventado)",
     "ECOCARDIOGRAMA TRANSTORÁCICO — LO QUE DEBE SABER\n"
     "Su médico pidió un ecocardiograma para ver cómo funciona su corazón y buscar coágulos que pudieron causar su derrame "
     "cerebral. La prueba usa ondas de sonido; no usa radiación y no duele.\n"
     "Cita: jueves 25 de febrero de 2027 a las 10:00 a.m., Laboratorio de Cardiología, Hospital Comunitario San Marcos, "
     "tercer piso.\n"
     "Puede comer, beber y tomar sus medicamentos como siempre. Use ropa cómoda; le pedirán que se quite la ropa de la "
     "cintura para arriba y le darán una bata.\n"
     "Se acostará sobre el lado izquierdo. El técnico pondrá gel y moverá un aparato pequeño sobre su pecho. Puede durar "
     "unos 45 minutos.\n"
     "Su médico le dará los resultados en su próxima cita. Preguntas: (919) 555-0166.",
     "Su ecocardiograma",
     [P("Su ecocardiograma",
        T("Es una prueba del **corazón**.", "corazón"),
        T("Mira cómo **funciona** su corazón.", "corazón"),
        T("Busca **coágulos** que pudieron causar su **derrame**.", "coágulo")),
      P("No duele",
        T("Usa **ondas de sonido**.", "ondas de sonido"),
        T("**Sin radiación**. **No duele**.", "sin dolor")),
      P("Cuándo y dónde",
        T("**jueves 25 de febrero de 2027**", "calendario"),
        T("**10:00 a.m.**", "reloj"),
        T("**Laboratorio de Cardiología**, **tercer piso**", "puerta"),
        T("**Hospital Comunitario San Marcos**", "hospital")),
      P("Antes",
        T("Puede **comer**, **beber** y tomar sus **medicinas** como siempre.", "comer"),
        T("Use ropa **cómoda**.", "ropa")),
      P("Durante la prueba",
        T("Se quita la **ropa** de la cintura para **arriba**. Le dan una **bata**.", "bata"),
        T("Se **acuesta** sobre el lado **izquierdo**.", "acostado"),
        T("Le ponen **gel** y mueven un **aparato** sobre el **pecho**.", "ultrasonido"),
        T("Dura unos **45 minutos**.", "reloj")),
      P("Resultados",
        T("Su **médico** le da los **resultados** en la **próxima cita**.", "médico"),
        PHs("Preguntas: (919) 555-0166"))],
     ["'Transtorácico' no se usa en el folleto."]),

# 8 ── Referido a grupo de afasia ───────────────────────────────────────────────
pair("referido-grupo-afasia-es-001", "es", "referral", "Referido a programa comunitario de afasia (ejemplo inventado)",
     "REFERIDO — PROGRAMA COMUNITARIO DE AFASIA\n"
     "Para: Conexiones de Afasia del Triángulo | De: Laura Méndez, M.S., CCC-SLP, Clínica del Habla Piedmont\n"
     "El señor Rafael Ortega terminó la terapia del habla y se refiere a su programa para mantener sus habilidades de "
     "comunicación y su participación social.\n"
     "Información para el paciente: el programa tiene un grupo de conversación en español los miércoles de 2:00 p.m. a "
     "3:30 p.m. y una clase de computación. La membresía cuesta $25 al mes; hay becas. Los familiares pueden asistir gratis.\n"
     "Próximo paso: una coordinadora lo llamará dentro de 2 semanas para una visita de admisión de 30 minutos. Si no lo "
     "llaman, llame al (919) 555-0163.",
     "Un programa para personas con afasia",
     [P("Un programa para usted",
        T("Para: **Rafael Ortega**", "persona"),
        T("**Laura Méndez, M.S., CCC-SLP** lo refirió a un **programa**.", "terapeuta del habla"),
        T("Es **Conexiones de Afasia del Triángulo**.", "grupo")),
      P("Para qué",
        T("Para mantener su **comunicación**.", "conversación"),
        T("Para estar con **otras personas**.", "amigos")),
      P("Qué ofrecen",
        T("Un **grupo de conversación** en **español**.", "conversación"),
        T("Los **miércoles**, de **2:00 p.m.** a **3:30 p.m.**", "calendario"),
        T("Una clase de **computación**.", "computadora")),
      P("Costo",
        T("**$25** al mes.", "dinero"),
        T("Hay **becas** para ayudar con el costo.", "dinero"),
        T("Su **familia** puede ir **gratis**.", "familia")),
      P("Próximo paso",
        T("Lo van a **llamar** dentro de **2 semanas**.", TEL),
        T("Para una primera visita de **30 minutos**.", "reloj"),
        T("¿No lo llamaron? **Llame** usted.", TEL),
        PHs("Teléfono: (919) 555-0163"))]),

# 9 ── Referido a nutricionista ─────────────────────────────────────────────────
pair("referido-nutricion-es-001", "es", "referral", "Referido a nutricionista (ejemplo inventado)",
     "REFERIDO: TERAPIA DE NUTRICIÓN MÉDICA\n"
     "Paciente: Marisol Vega | Proveedor: Dr. Tomás Aguilar | Diagnósticos: diabetes tipo 2, presión alta, historia de "
     "derrame cerebral.\n"
     "Motivo: educación sobre alimentación para la diabetes y una dieta baja en sal (menos de 2,000 mg de sodio al día).\n"
     "Cita: lunes 1 de marzo de 2027 a las 11:00 a.m. con Daniela Rojas, nutricionista, en la Clínica Familiar Las Palmas. "
     "La consulta es en español.\n"
     "Traiga: un diario de comida de 3 días (todo lo que come y bebe), su lista de medicamentos y su glucómetro. Si alguien "
     "cocina para usted, invítelo a venir.\n"
     "Para cambiar la cita, llame al (919) 555-0144.",
     "Cita con la nutricionista",
     [P("Cita con la nutricionista",
        T("Para: **Marisol Vega**", "persona"),
        T("El **Dr. Tomás Aguilar** quiere que vea a una **nutricionista**.", "nutricionista"),
        T("Ella le ayuda con la **comida** y la **salud**.", "comida sana")),
      P("Para qué",
        T("Aprender a comer bien con **diabetes**.", "diabetes"),
        T("Comer **menos sal**: menos de **2,000 mg** de **sodio** al día.", "sal")),
      P("Cuándo y dónde",
        T("**lunes 1 de marzo de 2027**", "calendario"),
        T("**11:00 a.m.**", "reloj"),
        T("Con **Daniela Rojas**, nutricionista.", "nutricionista"),
        T("En la **Clínica Familiar Las Palmas**. En **español**.", "clínica")),
      P("Qué traer",
        S("Un **diario de comida** de **3 días**.", "diario"),
        S("Su **lista** de **medicamentos**.", "lista de medicamentos"),
        S("Su **glucómetro**.", "glucómetro")),
      P("Traiga a quien cocina",
        T("¿Alguien **cocina** para usted?", "cocinar"),
        T("**Invítelo** a venir.", "familia")),
      P("Cambiar la cita",
        PHs("Teléfono: (919) 555-0144"))],
     ["'Ella le ayuda con la comida y la salud' agrega una explicación corta."]),

# 10 ── Carta de trabajo ────────────────────────────────────────────────────────
pair("carta-trabajo-es-001", "es", "letter", "Carta de estado laboral (ejemplo inventado)",
     "INFORME DE ESTADO LABORAL\n"
     "Paciente: Jorge Castillo | Empleador: Constructora Piedmont | Proveedor: Dra. Lucía Herrera, Neurología\n"
     "El paciente está bajo mi cuidado después de un derrame cerebral el 18/11/2026.\n"
     "Estado: no puede trabajar hasta el lunes 15 de marzo de 2027. Después puede volver con restricciones por 6 semanas: "
     "máximo 6 horas al día; no subir escaleras de mano ni andamios; no manejar vehículos de la compañía; no levantar más de "
     "20 libras.\n"
     "Revisaremos las restricciones en su próxima cita, el lunes 26 de abril de 2027 a las 9:00 a.m.\n"
     "Preguntas: (919) 555-0145.",
     "Volver al trabajo",
     [P("Su trabajo",
        T("Para: **Jorge Castillo**", "persona"),
        T("De la **Dra. Lucía Herrera**.", "doctora"),
        T("Para su trabajo en **Constructora Piedmont**.", "trabajo")),
      P("Todavía no trabaje",
        T("**No trabaje** hasta el **lunes 15 de marzo de 2027**.", "no trabajar")),
      P("Volver poco a poco",
        T("Después, vuelva con **límites** por **6 semanas**.", "calendario"),
        T("Máximo **6 horas** al día.", "reloj")),
      P("Límites en el trabajo",
        T("**No suba** escaleras de mano ni **andamios**.", "escalera"),
        T("**No maneje** vehículos de la compañía.", "no manejar"),
        T("**No levante** más de **20 libras**.", "levantar")),
      P("Próxima cita",
        T("Revisamos sus **límites** otra vez.", "revisar"),
        T("**lunes 26 de abril de 2027**", "calendario"),
        T("**9:00 a.m.**", "reloj")),
      P("¿Preguntas?",
        PHs("Teléfono: (919) 555-0145"))],
     omitted=["Fecha del derrame 18/11/2026: fecha pasada"]),

# 11 ── Cómo inscribirse en el portal ───────────────────────────────────────────
pair("como-portal-es-001", "es", "how_to", "Cómo inscribirse en el portal del paciente (ejemplo inventado)",
     "INSCRÍBASE EN EL PORTAL DEL PACIENTE\n"
     "En el portal puede ver sus resultados, pedir más medicina y mandar mensajes a su equipo médico. El portal está en "
     "español.\n"
     "Su código de activación: 4MZ8-QT2L-W7HC. El código vence el 30 de abril de 2027.\n"
     "1. Vaya a www.example.org/portal. 2. Haga clic en \"Español\" y luego en \"Inscribirse\". 3. Escriba su código, su "
     "fecha de nacimiento y su código postal. 4. Cree un nombre de usuario y una contraseña. Anótelos y guárdelos en un lugar "
     "seguro.\n"
     "Un familiar puede tener acceso para ayudarle; pida el formulario en la recepción.\n"
     "No use los mensajes del portal para emergencias. Llame al 911.\n"
     "Ayuda con el portal: (919) 555-0167, de lunes a viernes, de 8:00 a.m. a 5:00 p.m.",
     "Inscribirse en el portal",
     [P("¿Qué es el portal?",
        T("Vea sus **resultados**.", "computadora"),
        T("Pida **más medicina**.", "frasco de pastillas"),
        T("Mande **mensajes** a su **equipo médico**.", "mensaje"),
        T("Está en **español**.", "hablar")),
      P("Su código",
        T("Su código: **4MZ8-QT2L-W7HC**", "llave"),
        T("Úselo antes del **30 de abril de 2027**.", "calendario")),
      P("Inscríbase",
        S("Vaya a **www.example.org/portal**", "sitio web"),
        S("Haga clic en **\"Español\"** y luego en **\"Inscribirse\"**.", "clic"),
        S("Escriba su **código**, su fecha de nacimiento y su código postal.", "teclado"),
        S("Cree un **usuario** y una **contraseña**. **Anótelos**.", "contraseña")),
      P("Su familia puede ayudar",
        T("Un **familiar** puede ayudarle con el portal.", "familia"),
        T("Pida el **formulario** en la **recepción**.", "documento")),
      P("No es para emergencias",
        T("**No** use los mensajes para **emergencias**.", "no"),
        CR("Llame al 911", "ambulancia")),
      P("Ayuda con el portal",
        T("De **lunes** a **viernes**, de **8:00 a.m.** a **5:00 p.m.**", "reloj"),
        PHs("Teléfono: (919) 555-0167"))]),

# 12 ── Aprobación de equipo médico ─────────────────────────────────────────────
pair("aprobacion-equipo-es-001", "es", "insurance", "Aprobación de equipo médico (ejemplo inventado)",
     "AVISO DE APROBACIÓN — EQUIPO MÉDICO DURADERO\n"
     "Miembro: Alberto Ruiz | Número de miembro: MCD449120\n"
     "Su plan aprobó: 1 andador con ruedas y asiento; 1 silla para la ducha; 1 barra de apoyo para el inodoro.\n"
     "Proveedor de equipo: Suministros Médicos Rest Easy. Ellos lo llamarán dentro de 5 días hábiles para coordinar la "
     "entrega a su casa. No tiene que pagar copago.\n"
     "Si el equipo no le queda bien o se rompe, llame al proveedor al (919) 555-0139. Para preguntas sobre su cobertura, "
     "llame a Servicios para Miembros al 1-800-555-0115 (TTY 711).",
     "Su equipo está aprobado",
     [P("Su equipo está aprobado",
        T("Para: **Alberto Ruiz**", "persona"),
        T("Número de miembro: **MCD449120**", "tarjeta"),
        T("Su plan dijo que **sí**.", "sí")),
      P("Lo que va a recibir",
        T("**1 andador** con **ruedas** y **asiento**.", "andador"),
        T("**1 silla** para la **ducha**.", "silla de ducha"),
        T("**1 barra de apoyo** para el **inodoro**.", "barra de apoyo")),
      P("La entrega",
        T("**Suministros Médicos Rest Easy** lo va a llamar.", TEL),
        T("Dentro de **5 días hábiles**.", "calendario"),
        T("Le llevan el equipo a su **casa**.", "casa"),
        T("**No paga** copago.", "dinero")),
      P("¿Problemas con el equipo?",
        T("¿No le **queda bien**? ¿Se **rompió**?", "roto"),
        PHs("Rest Easy: (919) 555-0139")),
      P("Preguntas sobre su seguro",
        T("Llame a **Servicios para Miembros**.", TEL),
        PHs("Teléfono: 1-800-555-0115"),
        PH("TTY: 711", "tty"))]),

# 13 ── Cómo usar el andador ────────────────────────────────────────────────────
pair("como-andador-es-001", "es", "how_to", "Cómo usar su andador con ruedas (ejemplo inventado)",
     "CÓMO USAR SU ANDADOR CON RUEDAS\n"
     "Altura: las manijas deben quedar a la altura de su muñeca cuando está parado con los brazos sueltos. Su terapeuta físico "
     "ajustará la altura.\n"
     "Para caminar: 1. Póngase de pie derecho dentro del andador. 2. Empuje el andador un paso adelante. 3. Dé un paso con la "
     "pierna más débil primero. 4. Luego dé un paso con la pierna más fuerte. Mire hacia adelante, no a los pies.\n"
     "Para sentarse en el asiento del andador: ponga los frenos primero. Nunca se siente si las ruedas no tienen freno.\n"
     "No use el andador en escaleras. Quite tapetes sueltos de su casa.\n"
     "Si se cae, no se levante solo si está herido; llame al 911. Preguntas para su terapeuta físico: (919) 555-0121.",
     "Cómo usar su andador",
     [P("La altura",
        T("Las **manijas** van a la altura de su **muñeca**.", "andador"),
        T("Su **terapeuta físico** ajusta la **altura**.", "terapeuta físico")),
      P("Para caminar",
        S("Párese **derecho** dentro del andador.", "de pie"),
        S("**Empuje** el andador un paso **adelante**.", "andador"),
        S("Paso con la pierna **más débil** primero.", "pierna"),
        S("Luego paso con la pierna **más fuerte**.", "pierna")),
      P("Mire adelante",
        T("Mire hacia **adelante**, no a los **pies**.", "mirar adelante")),
      P("Para sentarse",
        T("Ponga los **frenos** primero.", "freno"),
        T("**Nunca** se siente sin **frenos**.", "no")),
      P("Seguridad",
        T("**No** use el andador en **escaleras**.", "no escaleras"),
        T("Quite los **tapetes** sueltos de su casa.", "tapete")),
      P("Si se cae",
        T("¿Está **herido**? **No** se levante solo.", "caída"),
        CR("Llame al 911", "ambulancia"),
        PHs("Preguntas para su terapeuta físico: (919) 555-0121"))],
     ["La frase 'cuando está parado con los brazos sueltos' no se incluyó; el terapeuta ajusta la altura. Por favor revise."]),

# 14 ── Referido a oftalmología ─────────────────────────────────────────────────
pair("referido-ojos-es-001", "es", "referral", "Referido a oftalmología (ejemplo inventado)",
     "REFERIDO A OFTALMOLOGÍA\n"
     "Paciente: Carmen Ruiz | Médico que refiere: Dra. Lucía Herrera\n"
     "Motivo: pérdida del campo visual del lado derecho (hemianopsia homónima derecha) después de un derrame cerebral. "
     "Evaluación del campo visual y recomendaciones para la seguridad y la lectura.\n"
     "Cita: viernes 12 de marzo de 2027 a las 1:15 p.m. con el Dr. Pablo Serrano, Centro Oftalmológico Valle Verde, "
     "900 Riverside Drive. Le pondrán gotas para dilatar las pupilas; su vista puede quedar borrosa por 4 a 6 horas. Traiga "
     "a alguien que maneje y traiga sus lentes.\n"
     "Hasta su cita: gire la cabeza hacia la derecha para ver lo que no ve. No maneje.\n"
     "Para cambiar la cita: (919) 555-0168.",
     "Cita para sus ojos",
     [P("Cita para sus ojos",
        T("Para: **Carmen Ruiz**", "persona"),
        T("La **Dra. Lucía Herrera** quiere que vea a un médico de los **ojos**.", "ojo")),
      P("Por qué",
        T("Después del derrame, **no ve** bien el lado **derecho**.", "ojo"),
        T("Van a revisar **cuánto** puede ver.", "examen de la vista"),
        T("Le darán ideas para **leer** y estar **seguro**.", "leer")),
      P("Cuándo y dónde",
        T("**viernes 12 de marzo de 2027**", "calendario"),
        T("**1:15 p.m.**", "reloj"),
        T("Con el **Dr. Pablo Serrano**, **Centro Oftalmológico Valle Verde**", "médico"),
        T("**900 Riverside Drive**", "mapa")),
      P("Gotas en los ojos",
        T("Le ponen **gotas** en los ojos.", "gotas para los ojos"),
        T("Su vista puede quedar **borrosa** de **4 a 6 horas**.", "borroso"),
        T("Traiga a alguien que **maneje**.", "carro"),
        T("Traiga sus **lentes**.", "lentes")),
      P("Hasta su cita",
        T("**Gire la cabeza** hacia la **derecha** para ver más.", "girar cabeza derecha"),
        T("**No maneje**.", "no manejar")),
      P("Cambiar la cita",
        PHs("Teléfono: (919) 555-0168"))],
     ["'Hemianopsia homónima derecha' se explicó como 'no ve bien el lado derecho'. Por favor confirme."]),

# 15 ── Consentimiento para fotos ───────────────────────────────────────────────
pair("consentimiento-fotos-es-001", "es", "consent", "Permiso para fotos (ejemplo inventado)",
     "PERMISO PARA FOTOGRAFÍAS\n"
     "La Clínica del Habla Piedmont quiere tomarle fotos para hacer materiales de comunicación personales, como un tablero "
     "de dibujos o un libro de fotos de su familia y sus actividades. Con su permiso, también podemos usar fotos en folletos "
     "de la clínica o en nuestro sitio web. Su nombre no aparecerá con ninguna foto usada fuera de sus materiales. Puede "
     "cancelar este permiso cuando quiera, diciéndole a su terapeuta; las fotos ya impresas tal vez no se puedan recoger. "
     "Decir que no no cambia su atención.\n"
     "[ ] Sí, fotos solo para mis materiales.\n"
     "[ ] Sí, fotos para mis materiales Y para folletos o el sitio web de la clínica.\n"
     "[ ] No quiero fotos.\n"
     "Firma: ____________ Fecha: ____________",
     "Fotos de usted",
     [P("Fotos de usted",
        T("Queremos tomarle **fotos**.", "cámara"),
        T("Para hacer su **tablero** o su **libro de fotos**.", "álbum de fotos"),
        T("De su **familia** y sus **actividades**.", "familia")),
      P("Otro uso",
        T("Si dice **sí**, podemos usar fotos en **folletos** de la clínica.", "folleto"),
        T("O en el **sitio web**.", "sitio web"),
        T("Su **nombre** **no** aparece con las fotos.", "sin nombre")),
      P("Usted decide",
        T("Puede **cambiar de opinión** cuando quiera.", "cambiar"),
        T("Dígale a su **terapeuta**.", "terapeuta del habla"),
        T("Las fotos **ya impresas** tal vez **no** se puedan recoger.", "impresora"),
        T("Decir no **no cambia** su **atención**.", "atención médica")),
      P("Por favor escoja",
        C("**Sí**, solo para **mis** materiales.", "sí"),
        C("**Sí**, para mis materiales **y** folletos o sitio web.", "sí"),
        C("**No** quiero fotos.", "no")),
      P("Firme",
        B("Firma: ____________", "firma"),
        B("Fecha: ____________", "calendario"))]),
]

mark_reviewed(PAIRS, "CCC-SLP (anonymous)", "2026-11-12")
write(PAIRS, "batch4_es.jsonl")
