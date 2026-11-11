"""Batch 5 (Spanish): 12 made-up pairs in messy real-world formats (portal messages, bilingual
pharmacy labels, text reminders, voicemail, abbreviations, legal fine print, tables, mixed
English/Spanish forms, scanning errors, email, nurse call notes). All names, clinics, IDs and
numbers are invented (phones use 555-01xx; websites use example.org). Not SLP-reviewed yet.

Run:  python data/sources/batch5_es.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from batch2_helpers import B, C, CR, P, PH, S, T, pair, write  # noqa: E402,F401

TEL = "teléfono"
PHs = lambda t: PH(t, TEL)
CRs = lambda t: CR(t, "ambulancia")

PAIRS = [
# 1 ── Mensaje del portal ───────────────────────────────────────────────────────
pair("mensaje-portal-es-001", "es", "message", "Mensaje del portal del paciente (ejemplo inventado)",
     "De: Patricia Lozano, RN (Clínica Familiar Las Palmas)\nPara: Rosario Méndez\nAsunto: RE: azúcar alta\n\n"
     "Hola Sra. Méndez, gracias por mandar sus números!! El Dr. Aguilar los revisó. Como su azúcar en ayunas ha estado "
     "arriba de 200 casi todos los días, él quiere que empiece a usar insulina glargina 10 unidades por la noche, a la hora "
     "de dormir. La receta ya está en su farmacia. Mañana a las 2:00 p.m. la enfermera le va a enseñar cómo ponérsela, aquí "
     "en la clínica. Siga con la metformina igual. Si su azúcar baja de 70 o se siente temblorosa, sudada o confundida, coma "
     "algo dulce y llámenos al (919) 555-0144. Si se desmaya o no puede despertar, llamen al 911!! Saludos, Patricia",
     "Mensaje de su enfermera",
     [P("Mensaje de su enfermera",
        T("Para: **Rosario Méndez**", "persona"),
        T("De **Patricia Lozano, RN**.", "enfermera"),
        T("El **Dr. Aguilar** revisó sus números de **azúcar**.", "médico")),
      P("Lo que vieron",
        T("Su azúcar en ayunas está **arriba de 200** casi **todos los días**.", "glucómetro")),
      P("Medicina nueva",
        T("**Empiece** insulina glargina **10 unidades**.", "insulina"),
        T("Por la **noche**, a la hora de **dormir**.", "cama"),
        T("La **receta** ya está en su **farmacia**.", "farmacia")),
      P("Aprenda a usarla",
        T("**Mañana** a las **2:00 p.m.**", "reloj"),
        T("La **enfermera** le enseña cómo **ponérsela**.", "enfermera"),
        T("Aquí en la **clínica**.", "clínica")),
      P("Siga igual",
        T("Siga con la **metformina** igual.", "pastilla")),
      P("¿Azúcar baja?",
        T("¿Azúcar **menos de 70**? ¿**Temblorosa**, **sudada** o **confundida**?", "mareo"),
        T("**Coma algo dulce**.", "jugo"),
        PHs("Llame al (919) 555-0144")),
      P("Emergencia",
        T("¿Se **desmaya**? ¿No puede **despertar**?", "desmayo"),
        CRs("Llamen al 911"))],
     ["'Mañana' depende de la fecha del mensaje; el mensaje no da la fecha. Por favor revise."]),

# 2 ── Etiqueta de farmacia bilingüe ────────────────────────────────────────────
pair("etiqueta-farmacia-es-001", "es", "medication", "Etiqueta de farmacia bilingüe (ejemplo inventado)",
     "FARMACIA CENTRAL  (919) 555-0154\nRx# 0071930   Fecha: 01/25/2027\nPAREDES, ANA LUCIA\n"
     "AMLODIPINE 5 MG TABLET / AMLODIPINO 5 MG TABLETA\nTOME 1 TABLETA POR LA BOCA UNA VEZ AL DÍA\nQty: 30   Refills: 5   "
     "Dr. Tomás Aguilar\nDiscard after / Desechar después de: 01/25/2028\n"
     "[Sticker] MAY CAUSE DIZZINESS / PUEDE CAUSAR MAREO\n"
     "[Sticker] TAKE AT THE SAME TIME EVERY DAY / TÓMELA A LA MISMA HORA TODOS LOS DÍAS",
     "La etiqueta de su medicina: amlodipino",
     [P("Su medicina",
        T("Para: **Ana Lucía Paredes**", "persona"),
        T("**Amlodipino 5 mg**, tableta", "pastilla"),
        T("Del **Dr. Tomás Aguilar**.", "médico")),
      P("Cómo tomarla",
        T("Tome **1 tableta**.", "pastilla"),
        T("Por la **boca**.", "boca"),
        T("**Una vez** al día.", "calendario"),
        T("A la **misma hora** todos los días.", "reloj")),
      P("Cuidado",
        T("Puede causar **mareo**.", "mareo")),
      P("Más medicina",
        T("Le quedan **5** resurtidos (**refills**).", "frasco de pastillas"),
        T("Número de receta (Rx): **0071930**", "etiqueta"),
        T("Deséchela después del **01/25/2028**.", "basura")),
      P("Farmacia",
        T("**Farmacia Central**", "farmacia"),
        PHs("Teléfono: (919) 555-0154"))],
     ["La etiqueta mezcla inglés y español; el folleto está solo en español.",
      "Las fechas de la etiqueta están en formato de EE. UU. (mes/día/año). Se copiaron igual; un lector hispano puede leerlas como día/mes. Por favor revise."],
     omitted=["Fecha de surtido 01/25/2027: fecha pasada", "Qty: 30: cantidad en el frasco, sin acción"]),

# 3 ── Recordatorio por mensaje de texto ────────────────────────────────────────
pair("sms-recordatorio-es-001", "es", "appointment", "Recordatorio por mensaje de texto (ejemplo inventado)",
     "ClinicaPalmas: Recordatorio: Marisol tiene cita c/ Dr. T. Aguilar el lun 3/22 a las 8:45AM en Clínica Familiar Las "
     "Palmas. Responda 1 para confirmar, 2 para cambiar, ALTO para no recibir mensajes. Pueden aplicar cargos. ¿Ayuda? "
     "919-555-0144",
     "Recordatorio por mensaje de texto",
     [P("Recordatorio de cita",
        T("**Marisol** tiene una **cita**.", "cita médica"),
        T("Con el **Dr. T. Aguilar**.", "médico"),
        T("En la **Clínica Familiar Las Palmas**.", "clínica")),
      P("Cuándo",
        T("**lun 3/22**", "calendario"),
        T("**8:45AM**", "reloj")),
      P("Conteste el mensaje",
        T("Escriba **1** para decir que **sí** va.", "sí"),
        T("Escriba **2** para **cambiar** la cita.", "calendario"),
        T("Escriba **ALTO** para **no recibir** más mensajes.", "no")),
      P("¿Ayuda?",
        PHs("Llame al 919-555-0144"))],
     ["La fecha y la hora se copiaron igual que en el mensaje ('lun 3/22', '8:45AM'). '3/22' es 22 de marzo.",
      "'Pueden aplicar cargos' se dejó fuera."],
     omitted=["Pueden aplicar cargos: letra pequeña de la compañía de teléfono"]),

# 4 ── Mensaje de voz ───────────────────────────────────────────────────────────
pair("buzon-voz-es-001", "es", "message", "Transcripción de mensaje de voz (ejemplo inventado)",
     "[Transcripción de mensaje de voz, 11:32 AM] \"Hola, eh, este mensaje es para Héctor Navarro. Habla Sofía del "
     "Laboratorio de Cardiología del Hospital San Marcos. Le llamo por su prueba del corazón, el Holter. Este, se nos "
     "canceló un paciente y le podemos adelantar la cita para el miércoles 17 de febrero de 2027 a las 9:00 de la mañana, "
     "o sea 9:00 a.m. Va a tener que llevar el aparato puesto 24 horas y regresarlo el jueves. No se bañe mientras lo tenga. "
     "Si le sirve, llámenos al (919) 555-0166, otra vez, (919) 555-0166. Gracias, que esté bien.\"",
     "Pueden adelantar su prueba del corazón",
     [P("Su prueba del corazón",
        T("Para: **Héctor Navarro**", "persona"),
        T("Llamó **Sofía** del **Laboratorio de Cardiología**.", TEL),
        T("Es sobre su prueba **Holter** del **corazón**.", "corazón")),
      P("Una cita más pronto",
        T("Pueden **adelantar** su cita.", "calendario"),
        T("**miércoles 17 de febrero de 2027**", "calendario"),
        T("**9:00 a.m.**", "reloj")),
      P("El aparato",
        T("Lleva el **aparato** puesto **24 horas**.", "monitor cardíaco"),
        T("Lo **regresa** el **jueves**.", "calendario"),
        T("**No se bañe** mientras lo tenga.", "no bañarse")),
      P("¿Le sirve la nueva fecha?",
        T("**Llame** para decir que **sí**.", TEL),
        PHs("Teléfono: (919) 555-0166"))],
     ["El mensaje dice 'Hospital San Marcos' sin 'Comunitario'; se dejó como 'Laboratorio de Cardiología'."],
     omitted=["Hora del mensaje 11:32 AM: cuándo llamaron, sin acción", "Hospital San Marcos: nombre corto del hospital"]),

# 5 ── Preparación para cirugía con abreviaturas ────────────────────────────────
pair("preparacion-cirugia-es-001", "es", "procedure", "Instrucciones antes de un procedimiento con abreviaturas (ejemplo inventado)",
     "INSTRUCCIONES PRE-PROCEDIMIENTO — Colocación de sonda de gastrostomía (PEG)\n"
     "Pte: Esperanza Vidal | Médico: Dr. Pablo Serrano | Fecha: vie 2/26/27 | Llegar: 7 AM, Admisión de Cirugía, HCSM "
     "edificio principal, 1er piso\n"
     "• NPO desp. de medianoche (nada de comer ni beber), incl. chicle y agua.\n"
     "• SUSPENDER clopidogrel x 5 días antes (última dosis dom 2/21/27).\n"
     "• Tomar metoprolol la mañana del proced. c/ un sorbito de agua.\n"
     "• Traer: lista de meds, identificación, tarjeta de seguro.\n"
     "• Debe venir con un adulto responsable que la lleve a casa.\n"
     "Preguntas o si está enferma antes (fiebre, tos): Clínica Pre-Op (919) 555-0169.",
     "Antes de su procedimiento",
     [P("Su procedimiento",
        T("Para: **Esperanza Vidal**", "persona"),
        T("Le van a poner una **sonda** en el **estómago** (**PEG**).", "sonda"),
        T("Médico: **Dr. Pablo Serrano**", "médico")),
      P("Cuándo y dónde",
        T("**vie 2/26/27**", "calendario"),
        T("Llegue a las **7 AM**.", "reloj"),
        T("**Admisión de Cirugía**, edificio principal, **1er piso**", "hospital")),
      P("Nada de comer ni beber",
        T("**Nada** de **comer** ni **beber** después de **medianoche**.", "no comer"),
        T("**Ni** chicle **ni** agua.", "no")),
      P("Clopidogrel",
        T("**Deje** el clopidogrel **5 días** antes.", "parar"),
        T("Última dosis: **dom 2/21/27**.", "calendario")),
      P("Metoprolol",
        T("**Tome** metoprolol la **mañana** del procedimiento.", "pastilla"),
        T("Con un **sorbito** de **agua**.", "vaso de agua")),
      P("Qué traer",
        S("Su **lista** de **medicinas**.", "lista de medicamentos"),
        S("Su **identificación**.", "identificación"),
        S("Su **tarjeta de seguro**.", "tarjeta de seguro")),
      P("Quién la lleva a casa",
        T("Un **adulto** debe venir con usted.", "familia"),
        T("Y **llevarla** a casa.", "carro")),
      P("¿Enferma antes?",
        T("¿**Fiebre**? ¿**Tos**? ¿Preguntas?", "fiebre"),
        PHs("Clínica Pre-Op: (919) 555-0169"))],
     ["Abreviaturas explicadas: Pte, NPO, desp., incl., x, proced., c/, meds.",
      "'Gastrostomía' se explicó como 'una sonda en el estómago'. Por favor confirme.",
      "Fechas copiadas en el formato del original (mes/día/año)."],
     omitted=["HCSM: abreviatura del hospital que el original no explica"]),

# 6 ── Carta con avisos legales ─────────────────────────────────────────────────
pair("carta-avisos-es-001", "es", "appointment", "Carta de cita con avisos legales (ejemplo inventado)",
     "Hospital Comunitario San Marcos — Neurología\n"
     "Estimada Sra. Teresa Campos: Esta carta confirma su cita de paciente nuevo con la Dra. Lucía Herrera el jueves 4 de "
     "marzo de 2027 a las 2:30 p.m. Llegue 30 minutos antes para llenar formularios. Traiga su tarjeta de seguro, una "
     "identificación con foto y todos sus frascos de medicinas. Tendrá un intérprete de español gratis.\n\n"
     "AVISO DE NO DISCRIMINACIÓN: El Hospital Comunitario San Marcos cumple con las leyes federales de derechos civiles "
     "aplicables y no discrimina por raza, color, nacionalidad, edad, discapacidad o sexo. Ofrecemos ayudas y servicios "
     "gratuitos a personas con discapacidades para que se comuniquen con nosotros, como intérpretes de lenguaje de señas e "
     "información escrita en otros formatos (letra grande, audio). Si cree que no le dimos estos servicios, puede presentar "
     "una queja ante nuestro Coordinador de Derechos Civiles al 1-800-555-0173 (TTY: 711).\n"
     "Para cambiar la cita, llame al (919) 555-0113.",
     "Su cita de neurología",
     [P("Su cita",
        T("Para: **Sra. Teresa Campos**", "persona"),
        T("Cita nueva con la **Dra. Lucía Herrera**.", "doctora"),
        T("En **Neurología**, **Hospital Comunitario San Marcos**.", "hospital")),
      P("Cuándo",
        T("**jueves 4 de marzo de 2027**", "calendario"),
        T("**2:30 p.m.**", "reloj"),
        T("Llegue **30 minutos antes** para llenar **formularios**.", "formulario")),
      P("Qué traer",
        S("Su **tarjeta de seguro**.", "tarjeta de seguro"),
        S("Una **identificación** con **foto**.", "identificación"),
        S("**Todos** sus **frascos** de medicinas.", "frasco de pastillas")),
      P("Intérprete",
        T("Tendrá un **intérprete** de **español** gratis.", "intérprete")),
      P("Ayuda gratis para comunicarse",
        T("Puede pedir ayuda **gratis** para **comunicarse**.", "ayuda"),
        T("Como **letra grande**, audio o lenguaje de señas.", "letra grande"),
        T("¿No le dieron esta ayuda? Puede **quejarse**.", "hablar"),
        PHs("Teléfono: 1-800-555-0173")),
      P("TTY",
        PH("TTY: 711", "tty")),
      P("Cambiar la cita",
        PHs("Teléfono: (919) 555-0113"))],
     ["El aviso legal se resume en una página. Por favor revise que la clínica lo acepte."],
     omitted=["Texto completo del aviso de no discriminación: letra pequeña legal; los derechos principales se mantienen"]),

# 7 ── Tabla de medicamentos ────────────────────────────────────────────────────
pair("tabla-medicamentos-es-001", "es", "medication", "Tabla de horario de medicamentos (ejemplo inventado)",
     "HORARIO DIARIO DE MEDICAMENTOS — Esperanza Vidal (actualizado 15/01/2027)\n"
     "| Medicamento | Dosis | Desayuno | Almuerzo | Cena | Al acostarse | Para qué |\n"
     "| Clopidogrel | 75 mg | X | | | | prevenir coágulos |\n"
     "| Lisinopril | 10 mg | X | | | | presión |\n"
     "| Atorvastatina | 40 mg | | | | X | colesterol |\n"
     "| Metformina | 500 mg | X | | X | | azúcar |\n"
     "Preguntas: Línea de enfermería (919) 555-0145.",
     "Mis horarios de medicinas",
     [P("Mis horarios de medicinas",
        T("Para: **Esperanza Vidal**", "persona")),
      P("Desayuno",
        T("**Clopidogrel 75 mg**: prevenir coágulos", "pastilla"),
        T("**Lisinopril 10 mg**: presión", "pastilla"),
        T("**Metformina 500 mg**: azúcar", "pastilla")),
      P("Almuerzo",
        T("**No** hay medicinas en el almuerzo.", "no pastilla")),
      P("Cena",
        T("**Metformina 500 mg**: azúcar", "pastilla")),
      P("Al acostarse",
        T("**Atorvastatina 40 mg**: colesterol", "pastilla")),
      P("¿Preguntas?",
        T("**Línea de enfermería**", "enfermera"),
        PHs("Teléfono: (919) 555-0145"))],
     ["La tabla se convirtió en una página por cada hora del día."],
     omitted=["Actualizado 15/01/2027: fecha de la lista"]),

# 8 ── Formulario mezclado inglés/español ───────────────────────────────────────
pair("formulario-mixto-es-001", "es", "form", "Formulario de admisión en inglés y español (ejemplo inventado)",
     "NEW PATIENT INTAKE / FORMULARIO DE ADMISIÓN — Piedmont Speech Clinic\n"
     "Please complete before your first visit. / Por favor llénelo antes de su primera visita.\n"
     "Name / Nombre: ____________ Preferred language / Idioma preferido: ____________\n"
     "Interpreter needed? / ¿Necesita intérprete? [ ] Yes / Sí [ ] No\n"
     "Emergency contact / Contacto de emergencia: ____________ Phone / Teléfono: ____________\n"
     "How do you communicate best? (check all) / ¿Cómo se comunica mejor? (marque todo lo que aplique) [ ] Speaking / "
     "Hablando [ ] Writing / Escribiendo [ ] Gestures / Gestos [ ] Pointing to pictures / Señalando dibujos [ ] Device / "
     "Aparato\n"
     "Return this form to the front desk or by fax to (919) 555-0170. / Entregue este formulario en la recepción o por fax al "
     "(919) 555-0170.\nQuestions / Preguntas: (919) 555-0107",
     "Formulario para pacientes nuevos",
     [P("Formulario para pacientes nuevos",
        T("De la **Clínica del Habla Piedmont**.", "clínica"),
        T("Llénelo **antes** de su **primera visita**.", "formulario")),
      P("Sus datos",
        B("Nombre: ____________", "persona"),
        B("Idioma preferido: ____________", "hablar")),
      P("Intérprete",
        T("¿Necesita **intérprete**?", "intérprete"),
        C("**Sí**", "sí"),
        C("**No**", "no")),
      P("Contacto de emergencia",
        B("Nombre: ____________", "persona"),
        B("Teléfono: ____________", TEL)),
      P("¿Cómo se comunica mejor?",
        C("**Hablando**", "hablar"),
        C("**Escribiendo**", "escribir"),
        C("Con **gestos**", "gestos"),
        C("**Señalando** dibujos", "señalar"),
        C("Con un **aparato**", "tableta")),
      P("Entréguelo",
        T("En la **recepción**.", "recepción"),
        T("O por **fax**.", "fax"),
        PH("Fax: (919) 555-0170", "fax"),
        PHs("Preguntas: (919) 555-0107"))],
     ["El formulario está en inglés y español; el folleto está solo en español.",
      "'Marque todo lo que aplique' está en el título de la página de casillas como pregunta; por favor revise que sea claro."]),

# 9 ── Alta escaneada con errores ───────────────────────────────────────────────
pair("alta-escaneada-es-001", "es", "discharge", "Página de alta escaneada con errores (ejemplo inventado)",
     "Página 1 de 2          HOSPITAL COMUNITARIO SAN MARCOS          Instruc-\nciones de alta\n"
     "Paciente: Rafael Ortega\nUsted fue tratado por un derrame cere-\nbral. Tome aspirina 81 mg por la boca una vez a1 día. "
     "Tome\natorvastatina 40 mg por la boca en la no-\nche. Su cita con la Dra. Lucía Herrera es e1 miércoles 3 de marzo de "
     "2027\na las 10:30 a.m.\nPágina 1 de 2          HOSPITAL COMUNITARIO SAN MARCOS\nSi tiene la cara caída, debi-\nlidad en "
     "un brazo o le cuesta hablar, 11ame a1 911 de inmediato. No ma-\nneje por 4 semanas. Pre-\nguntas: Línea de enfermería "
     "(919) 555-0145.",
     "Al salir del hospital",
     [P("Usted tuvo un derrame",
        T("Para: **Rafael Ortega**", "persona"),
        T("Usted tuvo un **derrame cerebral**.", "cerebro")),
      P("Sus medicinas",
        T("Tome **aspirina 81 mg**, por la boca, **una vez** al día.", "pastilla"),
        T("Tome **atorvastatina 40 mg**, por la boca, en la **noche**.", "noche")),
      P("Su cita",
        T("Con la **Dra. Lucía Herrera**.", "doctora"),
        T("**miércoles 3 de marzo de 2027**", "calendario"),
        T("**10:30 a.m.**", "reloj")),
      P("No maneje",
        T("**No maneje** por **4 semanas**.", "no manejar")),
      P("Emergencia",
        T("¿La **cara** caída? ¿**Debilidad** en un brazo? ¿Le cuesta **hablar**?", "cara"),
        CRs("Llame al 911 de inmediato")),
      P("¿Preguntas?",
        T("**Línea de enfermería**", "enfermera"),
        PHs("Teléfono: (919) 555-0145"))],
     ["El escaneo tenía errores ('a1', 'e1', '11ame' con el número 1 en vez de la letra l) y palabras cortadas. El folleto los corrige. Por favor revise."],
     omitted=["'Página 1 de 2' y el encabezado repetido: errores del escaneo"]),

# 10 ── Resultados de laboratorio en tabla ──────────────────────────────────────
pair("resultados-tabla-es-001", "es", "results", "Informe de laboratorio con marcas A/B (ejemplo inventado)",
     "INFORME DE LABORATORIO — Clínica Familiar Las Palmas\nPaciente: Marisol Vega | Tomada: 02/12/2027 08:05\n"
     "PRUEBA          RESULTADO   MARCA   RANGO DE REFERENCIA\n"
     "GLUCOSA         184         A       70-99\n"
     "HEMOGLOBINA A1C 8.6         A       4.0-5.6\n"
     "POTASIO         4.0                 3.5-5.1\n"
     "CREATININA      0.8                 0.6-1.1\n"
     "Comentario (Dr. Tomás Aguilar): Su azúcar está alta. Vamos a hablar de un cambio de medicina en su cita del lunes 1 de "
     "marzo de 2027. Mientras tanto, siga su dieta y tome su metformina. Preguntas: (919) 555-0144.",
     "Sus resultados de laboratorio",
     [P("Sus resultados",
        T("Para: **Marisol Vega**", "persona"),
        T("El **Dr. Tomás Aguilar** revisó sus resultados.", "médico")),
      P("Alto",
        T("**Glucosa** (azúcar): **184**. Normal: **70-99**.", "glucómetro"),
        T("**A1c**: **8.6**. Normal: **4.0-5.6**.", "análisis de sangre"),
        T("Su **azúcar** está **alta**.", "advertencia")),
      P("Normal",
        T("**Potasio**: **4.0**.", "bien"),
        T("**Creatinina** (riñones): **0.8**.", "riñón")),
      P("Qué hacer",
        T("Siga su **dieta**.", "comida sana"),
        T("Tome su **metformina**.", "pastilla"),
        T("En su cita van a hablar de un **cambio** de medicina.", "médico")),
      P("Su cita",
        T("**lunes 1 de marzo de 2027**", "calendario")),
      P("¿Preguntas?",
        PHs("Teléfono: (919) 555-0144"))],
     ["'A' en la tabla significa alto. Los rangos de potasio y creatinina (normales) se dejaron fuera."],
     omitted=["Tomada 02/12/2027 08:05: cuándo se sacó la sangre",
              "Rangos 3.5-5.1 y 0.6-1.1 de resultados normales: detalle sin acción"]),

# 11 ── Correo electrónico ──────────────────────────────────────────────────────
pair("correo-es-001", "es", "message", "Hilo de correo electrónico (ejemplo inventado)",
     "De: citas@example.org\nEnviado: martes 9 de febrero de 2027 5:12 p.m.\nPara: Jorge Castillo\nAsunto: RE: RE: ¿mi "
     "cita de terapia?\n\n"
     "Hola Jorge, disculpe la confusión. Su evaluación de terapia ocupacional SÍ está programada: viernes 26 de febrero de "
     "2027 a las 3:00 p.m. con Luis Romero, en Lakeside Therapy Partners, 1180 Hillcrest Road. Use ropa cómoda y zapatos "
     "cerrados. Traiga sus lentes y su férula de la mano si la usa. Si necesita cambiarla, por favor llame; no conteste este "
     "correo porque no lo revisamos los fines de semana.\nGracias, Equipo de Citas | (919) 555-0121\n\n"
     "-----Mensaje original-----\nDe: Jorge Castillo\nnadie me ha llamado, sigue en pie??\n\n"
     "AVISO DE CONFIDENCIALIDAD: Este correo puede contener información médica protegida...",
     "Su cita de terapia ocupacional",
     [P("Su cita está programada",
        T("Para: **Jorge Castillo**", "persona"),
        T("Su evaluación de **terapia ocupacional** **sí** está programada.", "terapia ocupacional")),
      P("Cuándo y dónde",
        T("**viernes 26 de febrero de 2027**", "calendario"),
        T("**3:00 p.m.**", "reloj"),
        T("Con **Luis Romero**, en **Lakeside Therapy Partners**", "clínica"),
        T("**1180 Hillcrest Road**", "mapa")),
      P("Qué usar y traer",
        T("Ropa **cómoda** y zapatos **cerrados**.", "zapatos"),
        T("Sus **lentes**.", "lentes"),
        T("Su **férula** de la mano, si la usa.", "férula")),
      P("¿Necesita cambiarla?",
        T("**Llame**. **No** conteste el **correo**.", TEL),
        PHs("Equipo de Citas: (919) 555-0121"))],
     omitted=["Fecha del correo martes 9 de febrero de 2027 5:12 p.m.: cuándo se envió",
              "citas@example.org: no lo revisan; el lector debe llamar",
              "Mensaje anterior y aviso de confidencialidad: no se necesitan"]),

# 12 ── Notas de llamada a la enfermera ─────────────────────────────────────────
pair("llamada-enfermera-es-001", "es", "message", "Resumen de llamada a la línea de enfermería (ejemplo inventado)",
     "LÍNEA DE ENFERMERÍA FUERA DE HORARIO — RESUMEN DE LLAMADA\nQuien llamó: Alberto Ruiz (hijo de la paciente Carmen "
     "Ruiz) | Hora: dom 02/14/2027 19:40\n"
     "Motivo: la paciente tiene tos con flema y fiebre de 100.8°F desde ayer; tose al tomar agua.\n"
     "Consejo: Dele acetaminofén 500 mg, 2 tabletas, puede repetir en 6 horas si lo necesita. Que se siente derecha para "
     "comer y beber. Dele líquidos espesos como le indicó su terapeuta del habla. Llame mañana a su médico para una cita el "
     "mismo día: (919) 555-0144.\n"
     "Vaya a Emergencias o llame al 911 si: le cuesta respirar, tiene los labios azules, está muy confundida, o la fiebre "
     "pasa de 103°F.\nLínea de enfermería: (919) 555-0172.",
     "Consejos de la línea de enfermería",
     [P("Su llamada a la enfermera",
        T("Para la familia de **Carmen Ruiz**.", "familia"),
        T("Llamaron por **tos** con **flema** y **fiebre** de **100.8°F**.", "tos"),
        T("Ella **tose** al tomar **agua**.", "tos")),
      P("Qué hacer ahora",
        T("Dele **acetaminofén 500 mg**, **2 tabletas**.", "pastilla"),
        T("Puede **repetir** en **6 horas** si lo necesita.", "reloj"),
        T("Que se **siente derecha** para comer y beber.", "sentarse a la mesa"),
        T("Dele **líquidos espesos**, como dijo su terapeuta del habla.", "bebida espesa")),
      P("Mañana",
        T("**Llame** a su **médico** para una cita el **mismo día**.", "médico"),
        PHs("Médico: (919) 555-0144")),
      P("Emergencia",
        T("¿Le cuesta **respirar**? ¿Labios **azules**?", "respirar"),
        T("¿Muy **confundida**? ¿Fiebre de **más de 103°F**?", "termómetro"),
        CRs("Llame al 911 o vaya a Emergencias")),
      P("Línea de enfermería",
        PHs("Teléfono: (919) 555-0172"))],
     ["Escrito para la familia que llamó. 'Tose al tomar agua' puede ser señal de problemas para tragar; el folleto no lo interpreta. Por favor revise."],
     omitted=["Hora de la llamada dom 02/14/2027 19:40: cuándo llamaron", "Nombre de quien llamó (Alberto Ruiz, hijo): no se necesita"]),
]

write(PAIRS, "batch5_es.jsonl")
