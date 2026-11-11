"""Batch 3 (Spanish): 12 long, realistic made-up pairs, written to look like real hospital
paperwork. All names, clinics, IDs and numbers are invented (phones use 555-01xx; websites use
example.org). Not SLP-reviewed yet.

Run:  python data/sources/batch3_es.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from batch2_helpers import B, C, CR, P, PH, S, T, pair, write  # noqa: E402,F401

TEL = "teléfono"
PHs = lambda t: PH(t, TEL)

PAIRS = [
# 1 ── Resumen de la visita ─────────────────────────────────────────────────────
pair("avs-es-001", "es", "visit_summary", "Resumen de la visita (ejemplo inventado)",
     "RESUMEN DE LA VISITA — Clínica Familiar Las Palmas\n"
     "Paciente: Rosario Méndez | Fecha de nacimiento: 14/07/1958 | N.º de expediente: 00841277 | Fecha de la visita: 18/01/2027\n"
     "Proveedor: Dr. Tomás Aguilar\n"
     "Motivo de la visita: control de diabetes mellitus tipo 2 (E11.9).\n"
     "Signos vitales: PA 132/84 | Peso 168 lb | Hemoglobina A1c: 8.2%\n"
     "CAMBIOS EN SUS MEDICAMENTOS: AUMENTAR metformina de 500 mg a 1000 mg por la boca dos veces al día con comida. "
     "Continúe sus otros medicamentos igual.\n"
     "REFERIDOS: Clase de educación sobre la diabetes. La clase lo llamará en 1 semana.\n"
     "INSTRUCCIONES: Revise su azúcar en la sangre cada mañana antes de comer y anote los números. Camine 30 minutos, "
     "5 días a la semana, si su médico se lo permite.\n"
     "PRÓXIMA CITA: lunes 8 de marzo de 2027 a las 9:15 a.m. con el Dr. Tomás Aguilar.\n"
     "Vea sus resultados en el portal: www.example.org/portal. Preguntas: (919) 555-0144. En una emergencia, llame al 911.",
     "Su visita de hoy",
     [P("Su visita de hoy",
        T("Para: **Rosario Méndez**", "persona"),
        T("Usted vio al **Dr. Tomás Aguilar**.", "médico"),
        T("En la **Clínica Familiar Las Palmas**.", "clínica")),
      P("Por qué vino",
        T("Usted tiene **diabetes tipo 2**.", "diabetes"),
        T("Su **A1c** hoy: **8.2%**", "análisis de sangre")),
      P("Cambio de medicina",
        T("**Metformina**: tome **más**.", "pastilla"),
        T("Antes: **500 mg**. Ahora: **1000 mg**.", "pastilla"),
        T("**Dos veces** al día, por la boca.", "calendario"),
        T("Tómela con **comida**.", "comida")),
      P("Otras medicinas",
        T("Siga tomando sus **otras medicinas** igual.", "pastillas")),
      P("Clase de diabetes",
        T("Va a ir a una **clase** sobre la **diabetes**.", "clase"),
        T("Lo van a **llamar** en **1 semana**.", TEL)),
      P("Su azúcar",
        S("Revise su **azúcar** cada **mañana**.", "glucómetro"),
        S("Hágalo **antes de comer**.", "no comer"),
        S("**Anote** los números.", "escribir")),
      P("Caminar",
        T("Camine **30 minutos**.", "caminar"),
        T("**5 días** a la semana.", "calendario"),
        T("Si su **médico** se lo permite.", "médico")),
      P("Próxima cita",
        T("**lunes 8 de marzo de 2027**", "calendario"),
        T("**9:15 a.m.**", "reloj"),
        T("Con el **Dr. Tomás Aguilar**.", "médico")),
      P("Sus resultados",
        T("Vea sus resultados en: **www.example.org/portal**", "computadora")),
      P("¿Preguntas?",
        PHs("Teléfono: (919) 555-0144"),
        CR("¿Emergencia? Llame al 911", "ambulancia"))],
     omitted=["Fecha de nacimiento 14/07/1958: no la necesita el lector", "N.º de expediente 00841277",
              "Fecha de la visita 18/01/2027: fecha pasada", "PA 132/84 y peso 168 lb: medidas de la visita, sin acción",
              "Código E11.9: código de facturación"]),

# 2 ── Instrucciones de alta tras derrame ───────────────────────────────────────
pair("alta-derrame-es-002", "es", "discharge", "Instrucciones de alta del hospital (ejemplo inventado)",
     "INSTRUCCIONES DE ALTA — Hospital Comunitario San Marcos, Unidad de Derrame Cerebral\n"
     "Paciente: Esperanza Vidal | Fecha de nacimiento: 02/09/1949 | Expediente: 00995310 | Ingreso: 10/01/2027 | "
     "Alta: 15/01/2027\n"
     "Diagnóstico principal: accidente cerebrovascular isquémico agudo, territorio de la arteria cerebral media izquierda. "
     "Diagnóstico secundario: disfagia orofaríngea.\n"
     "MEDICAMENTOS AL ALTA: EMPEZAR clopidogrel 75 mg por la boca una vez al día. EMPEZAR atorvastatina 40 mg por la boca "
     "cada noche. CONTINUAR lisinopril 10 mg por la boca una vez al día.\n"
     "DIETA: comida en puré y líquidos espesos tipo néctar. Siéntese derecho para comer.\n"
     "ACTIVIDAD: no maneje hasta que su médico lo autorice. Camine con su andador.\n"
     "SEGUIMIENTO: Clínica de Derrame Cerebral, Dra. Lucía Herrera, martes 26 de enero de 2027 a las 3:30 p.m. Terapia del "
     "habla para pacientes externos: la clínica lo llamará para hacer la cita.\n"
     "LLAME AL 911 si tiene: debilidad nueva, dificultad para hablar, la cara caída, pérdida de la vista o un dolor de cabeza "
     "muy fuerte.\n"
     "Preguntas después del alta: Línea de enfermería (919) 555-0145, disponible las 24 horas.",
     "Al salir del hospital",
     [P("Usted tuvo un derrame",
        T("Para: **Esperanza Vidal**", "persona"),
        T("Usted tuvo un **derrame cerebral**.", "cerebro"),
        T("Fue en el lado **izquierdo** del cerebro.", "cerebro"),
        T("También le cuesta **tragar**.", "tragar")),
      P("Medicina nueva: clopidogrel",
        T("**Empiece** clopidogrel **75 mg**.", "pastilla"),
        T("**Una vez** al día, por la boca.", "calendario")),
      P("Medicina nueva: atorvastatina",
        T("**Empiece** atorvastatina **40 mg**.", "pastilla"),
        T("Por la boca, cada **noche**.", "noche")),
      P("Siga tomando",
        T("**Siga tomando** lisinopril **10 mg**.", "pastilla"),
        T("**Una vez** al día, por la boca.", "calendario")),
      P("Comer y beber",
        T("Coma comida en **puré**.", "puré"),
        T("Tome líquidos **espesos** tipo **néctar**.", "bebida espesa"),
        T("**Siéntese derecho** para comer.", "sentarse a la mesa")),
      P("Actividad",
        T("**No maneje**.", "no manejar"),
        T("Espere a que su **médico** diga que **sí**.", "médico"),
        T("Camine con su **andador**.", "andador")),
      P("Su cita",
        T("Con la **Dra. Lucía Herrera**.", "doctora"),
        T("En la **Clínica de Derrame Cerebral**.", "clínica"),
        T("**martes 26 de enero de 2027**", "calendario"),
        T("**3:30 p.m.**", "reloj")),
      P("Terapia del habla",
        T("La clínica de **terapia del habla** lo va a **llamar**.", TEL)),
      P("Llame al 911",
        T("¿**Debilidad** nueva? ¿Le cuesta **hablar**?", "brazo débil"),
        T("¿La **cara** caída? ¿No puede **ver**?", "cara"),
        T("¿**Dolor de cabeza** muy fuerte?", "dolor de cabeza"),
        CR("Llame al 911", "ambulancia")),
      P("¿Preguntas?",
        T("**Línea de enfermería**, las **24 horas**.", "enfermera"),
        PHs("Teléfono: (919) 555-0145"))],
     ["'Territorio de la arteria cerebral media izquierda' se simplificó a 'lado izquierdo del cerebro'."],
     omitted=["Fecha de nacimiento 02/09/1949", "Expediente 00995310",
              "Ingreso 10/01/2027 y alta 15/01/2027: fechas pasadas"]),

# 3 ── Guía de warfarina ────────────────────────────────────────────────────────
pair("guia-warfarina-es-001", "es", "medication", "Guía de warfarina (ejemplo inventado)",
     "GUÍA PARA PACIENTES QUE TOMAN WARFARINA (COUMADIN)\n"
     "Su dosis: warfarina 3 mg por la boca una vez al día a las 5:00 p.m.\n"
     "La warfarina hace que su sangre tarde más en coagular. Esto ayuda a prevenir coágulos y derrames cerebrales, pero "
     "aumenta el riesgo de sangrado.\n"
     "PRUEBAS DE SANGRE (INR): Su meta de INR es de 2.0 a 3.0. Su próxima prueba es el jueves 4 de febrero de 2027 en la "
     "Clínica de Anticoagulación Cedar Grove.\n"
     "ALIMENTOS: La vitamina K cambia el efecto de la warfarina. Coma más o menos la misma cantidad de verduras de hoja "
     "verde (espinaca, col rizada, brócoli) cada semana. No tome alcohol en exceso.\n"
     "OTROS MEDICAMENTOS: No empiece ni deje ningún medicamento, vitamina o hierba sin hablar con la clínica.\n"
     "Llame a la clínica al (919) 555-0147 si tiene moretones raros, sangrado de encías o sangre en la orina o en las heces.\n"
     "LLAME AL 911 si se cae y se golpea la cabeza o si tiene un sangrado que no para.",
     "Su medicina: warfarina",
     [P("Su medicina: warfarina",
        T("Su medicina es **warfarina** (**Coumadin**).", "pastilla"),
        T("Ayuda a prevenir **coágulos** y **derrames**.", "cerebro"),
        T("Pero puede causar **sangrado**.", "sangre")),
      P("Cómo tomarla",
        T("Tome **warfarina 3 mg**.", "pastilla"),
        T("**Una vez** al día, por la boca.", "calendario"),
        T("A las **5:00 p.m.**", "reloj")),
      P("Pruebas de sangre",
        T("Necesita pruebas de **INR**.", "análisis de sangre"),
        T("Su meta: **2.0 a 3.0**", "meta")),
      P("Próxima prueba",
        T("**jueves 4 de febrero de 2027**", "calendario"),
        T("En la **Clínica de Anticoagulación Cedar Grove**.", "clínica")),
      P("Comida",
        T("Coma la **misma cantidad** de verduras de hoja verde cada **semana**.", "lechuga"),
        T("Como **espinaca**, **col rizada**, **brócoli**.", "brócoli"),
        T("**No** tome **mucho alcohol**.", "no alcohol")),
      P("Otras medicinas",
        T("No **empiece** ni **deje** ninguna medicina.", "pastillas"),
        T("Tampoco **vitaminas** o **hierbas**.", "vitaminas"),
        T("Primero **hable** con la **clínica**.", "clínica")),
      P("Llame a la clínica",
        T("¿**Moretones** raros? ¿Sangrado de **encías**?", "moretón"),
        T("¿**Sangre** en la **orina** o en las **heces**?", "inodoro"),
        PHs("Clínica: (919) 555-0147")),
      P("Emergencia",
        T("¿Se **cayó** y se **golpeó** la cabeza?", "caída"),
        T("¿Un **sangrado** que **no para**?", "sangre"),
        CR("Llame al 911", "ambulancia"))],
     ["'La vitamina K cambia el efecto' no se explica en el folleto; solo se da la acción. Por favor revise."]),

# 4 ── Plan de cuidado de terapia del habla ─────────────────────────────────────
pair("plan-cuidado-es-001", "es", "therapy_plan", "Plan de cuidado de terapia del habla (ejemplo inventado)",
     "PLAN DE CUIDADO — PATOLOGÍA DEL HABLA Y LENGUAJE (PACIENTE EXTERNO)\n"
     "Clínica del Habla Piedmont, 1420 Duke Street, Suite 2\n"
     "Paciente: Rafael Ortega | Fecha de nacimiento: 21/03/1957 | N.º de Medicaid: 900417735 | Médico que refiere: "
     "Dr. Andrés Molina\n"
     "Diagnóstico de tratamiento: afasia después de infarto cerebral (I69.320).\n"
     "METAS (60 días): (1) El paciente nombrará 20 objetos comunes con 80% de precisión. (2) El paciente seguirá "
     "instrucciones de 1 paso con 90% de precisión. (3) El paciente usará un tablero de comunicación para pedir ayuda sin "
     "apoyo.\n"
     "FRECUENCIA: 3 veces por semana por 8 semanas.\n"
     "PERÍODO DE CERTIFICACIÓN: 18/01/2027 al 18/03/2027. Firma del médico: ____________\n"
     "Terapeuta: Laura Méndez, M.S., CCC-SLP",
     "Su plan de terapia del habla",
     [P("Su plan de terapia",
        T("Para: **Rafael Ortega**", "persona"),
        T("Su terapeuta: **Laura Méndez, M.S., CCC-SLP**", "terapeuta del habla"),
        T("Lo refirió el **Dr. Andrés Molina**.", "médico"),
        T("En la **Clínica del Habla Piedmont**.", "clínica")),
      P("Dónde",
        T("**1420 Duke Street, Suite 2**", "mapa")),
      P("Por qué viene",
        T("Usted tiene **afasia** por un **derrame cerebral**.", "cerebro")),
      P("Meta 1",
        T("Decir el **nombre** de **20 objetos** comunes.", "objetos"),
        T("Bien el **80%** de las veces.", "meta")),
      P("Meta 2",
        T("Seguir **instrucciones** de **1 paso**.", "paso"),
        T("Bien el **90%** de las veces.", "meta")),
      P("Meta 3",
        T("Usar un **tablero de comunicación**.", "tablero de comunicación"),
        T("Para **pedir ayuda** por su **cuenta**.", "ayuda")),
      P("Cada cuánto",
        T("**3 veces** por semana.", "calendario"),
        T("Por **8 semanas**.", "calendario"),
        T("Las metas son para **60 días**.", "meta")),
      P("Fechas del plan",
        T("Del **18/01/2027** al **18/03/2027**", "calendario"))],
     omitted=["Fecha de nacimiento 21/03/1957", "N.º de Medicaid 900417735", "Código I69.320: código de facturación",
              "Línea de firma del médico: para el médico, no para el paciente"]),

# 5 ── Resonancia magnética con contraste ───────────────────────────────────────
pair("preparacion-resonancia-es-001", "es", "procedure", "Preparación para resonancia magnética (ejemplo inventado)",
     "RESONANCIA MAGNÉTICA (RM) DEL CEREBRO CON CONTRASTE — PREPARACIÓN\n"
     "Fecha: jueves 11 de febrero de 2027 a las 2:00 p.m. Llegue a la 1:30 p.m. Lugar: Centro de Imágenes Northgate, "
     "4410 Pinecrest Parkway.\n"
     "ANTES: Puede comer y tomar sus medicamentos como siempre. Quítese todo el metal: joyas, relojes, audífonos, "
     "pasadores y dentaduras con metal.\n"
     "AVÍSENOS si tiene: marcapasos, implantes de metal, una bomba de medicamento, alergia al contraste, problemas de los "
     "riñones, o miedo a los espacios cerrados. Si su médico le receta un medicamento para relajarse, necesitará a alguien "
     "que maneje por usted.\n"
     "DURANTE: Le pondrán una vía (IV) en el brazo para el contraste. La máquina hace ruidos fuertes; le daremos tapones "
     "para los oídos. Debe quedarse quieto. El examen dura unos 45 minutos.\n"
     "Para cambiar la cita, llame al (919) 555-0148.",
     "Su resonancia del cerebro",
     [P("Su resonancia",
        T("Le van a hacer una **resonancia magnética**.", "resonancia magnética"),
        T("Toma **fotos** de su **cerebro**.", "cerebro"),
        T("Le ponen **contraste** por una **vía** en el brazo.", "inyección")),
      P("Cuándo y dónde",
        T("**jueves 11 de febrero de 2027**", "calendario"),
        T("Examen a las **2:00 p.m.** Llegue a la **1:30 p.m.**", "reloj"),
        T("**Centro de Imágenes Northgate**", "hospital"),
        T("**4410 Pinecrest Parkway**", "mapa")),
      P("Antes",
        T("Puede **comer** como siempre.", "comer"),
        T("Tome sus **medicinas** como siempre.", "pastilla")),
      P("Nada de metal",
        T("Quítese todo el **metal**.", "no metal"),
        T("**Joyas**, **relojes**, **audífonos**.", "joyas"),
        T("**Pasadores** y **dentaduras** con metal.", "dentadura")),
      P("Avísenos si tiene",
        T("¿**Marcapasos**? ¿**Implantes** de metal?", "corazón"),
        T("¿**Bomba** de medicina? ¿**Alergia** al contraste?", "alergia"),
        T("¿Problemas de los **riñones**?", "riñón"),
        T("¿**Miedo** a los espacios **cerrados**?", "miedo")),
      P("Medicina para relajarse",
        T("¿Su médico le da medicina para **relajarse**?", "pastilla"),
        T("Entonces **no maneje**. Alguien debe **manejar** por usted.", "carro")),
      P("Durante el examen",
        T("La máquina hace **ruido fuerte**.", "ruido"),
        T("Le damos **tapones** para los oídos.", "tapones para los oídos"),
        T("Quédese **quieto**.", "acostado"),
        T("Dura unos **45 minutos**.", "reloj")),
      P("Cambiar la cita",
        PHs("Teléfono: (919) 555-0148"))]),

# 6 ── Lista de medicamentos al alta ────────────────────────────────────────────
pair("lista-medicamentos-es-001", "es", "medication", "Lista de medicamentos al alta (ejemplo inventado)",
     "CONCILIACIÓN DE MEDICAMENTOS — LISTA AL ALTA\n"
     "Paciente: Ana Lucía Paredes | Preparado por: Miguel Soto, PharmD | Alergias: sulfa (ronchas)\n"
     "SUSPENDER: naproxeno 220 mg (aumenta el riesgo de sangrado con su nueva aspirina).\n"
     "EMPEZAR: amlodipino 5 mg, 1 tableta por la boca una vez al día. Aspirina 81 mg, 1 tableta por la boca una vez al día "
     "con comida.\n"
     "CAMBIAR: metformina, NUEVA DOSIS 1000 mg dos veces al día con comida (antes 500 mg).\n"
     "CONTINUAR SIN CAMBIOS: omeprazol 20 mg, 1 cápsula por la boca 30 minutos antes del desayuno.\n"
     "Traiga esta lista a todas sus citas. Preguntas: Línea de farmacia (919) 555-0149.",
     "Su lista de medicinas",
     [P("Su lista de medicinas",
        T("Para: **Ana Lucía Paredes**", "persona"),
        T("De su **farmacéutico**, **Miguel Soto, PharmD**.", "farmacéutico"),
        T("**Alergia**: sulfa (**ronchas**).", "alergia")),
      P("Pare: naproxeno",
        T("**Pare** el naproxeno **220 mg**.", "parar"),
        T("Con su nueva **aspirina**, puede causar **sangrado**.", "sangre")),
      P("Empiece: amlodipino",
        T("**Empiece** amlodipino **5 mg**.", "pastilla"),
        T("Tome **1 tableta** por la boca.", "pastilla"),
        T("**Una vez** al día.", "calendario")),
      P("Empiece: aspirina",
        T("**Empiece** aspirina **81 mg**.", "pastilla"),
        T("Tome **1 tableta** por la boca.", "pastilla"),
        T("**Una vez** al día, con **comida**.", "comida")),
      P("Cambio: metformina",
        T("Metformina tiene una **dosis nueva**.", "pastilla"),
        T("Ahora: **1000 mg**. Antes: **500 mg**.", "pastilla"),
        T("**Dos veces** al día, con **comida**.", "comida")),
      P("Siga igual: omeprazol",
        T("Siga tomando omeprazol **20 mg**.", "pastilla"),
        T("Tome **1 cápsula** por la boca.", "cápsula"),
        T("**30 minutos** antes del **desayuno**.", "desayuno")),
      P("Traiga esta lista",
        T("Traiga esta **lista** a **todas** sus citas.", "lista"),
        PHs("Farmacia: (919) 555-0149"))]),

# 7 ── Bienvenida de salud en el hogar ──────────────────────────────────────────
pair("salud-hogar-es-001", "es", "home_health", "Carta de bienvenida de salud en el hogar (ejemplo inventado)",
     "Bienvenido a Camino Claro Salud en el Hogar\n"
     "Su médico, el Dr. Tomás Aguilar, pidió servicios de salud en el hogar después de su estadía en el hospital. Todo nuestro "
     "personal habla español o usa un intérprete.\n"
     "SU EQUIPO: Enfermera registrada: Rosa Ibarra, 2 veces por semana por 3 semanas. Terapeuta ocupacional: Luis Romero, "
     "2 veces por semana por 4 semanas. Terapeuta del habla: Carmen Solís, 1 vez por semana por 6 semanas.\n"
     "Su primera visita de enfermería es el miércoles 13 de enero de 2027 entre la 1:00 p.m. y las 4:00 p.m.\n"
     "SUS DERECHOS: Usted tiene derecho a recibir un trato respetuoso, a participar en su plan de cuidado, a rechazar el "
     "tratamiento y a presentar una queja sin miedo. Para una queja, llame a nuestra oficina o a la Línea Estatal de Salud "
     "en el Hogar al 1-800-555-0150.\n"
     "Fuera del horario de oficina, llame a la enfermera de guardia las 24 horas al (919) 555-0151. En una emergencia, llame "
     "al 911.",
     "Bienvenido a salud en el hogar",
     [P("Bienvenido",
        T("Bienvenido a **Camino Claro Salud en el Hogar**.", "casa"),
        T("Lo vamos a **visitar** en su **casa**.", "visita a domicilio"),
        T("Lo pidió el **Dr. Tomás Aguilar**.", "médico"),
        T("Hablamos **español** o usamos un **intérprete**.", "intérprete")),
      P("Su enfermera",
        T("**Rosa Ibarra**, enfermera registrada", "enfermera"),
        T("**2 veces** por semana, por **3 semanas**.", "calendario")),
      P("Su terapeuta ocupacional",
        T("**Luis Romero**", "terapia ocupacional"),
        T("**2 veces** por semana, por **4 semanas**.", "calendario")),
      P("Su terapeuta del habla",
        T("**Carmen Solís**", "terapeuta del habla"),
        T("**1 vez** por semana, por **6 semanas**.", "calendario")),
      P("Primera visita",
        T("Primera visita de la **enfermera**:", "enfermera"),
        T("**miércoles 13 de enero de 2027**", "calendario"),
        T("Entre la **1:00 p.m.** y las **4:00 p.m.**", "reloj")),
      P("Sus derechos",
        T("Recibir un trato con **respeto**.", "respeto"),
        T("**Participar** en su plan de cuidado.", "plan"),
        T("Decir **no** al tratamiento.", "no"),
        T("Presentar una **queja** sin **miedo**.", "hablar")),
      P("Para una queja",
        T("Llame a nuestra **oficina**.", TEL),
        T("O a la **Línea Estatal de Salud en el Hogar**.", TEL),
        PHs("Línea estatal: 1-800-555-0150")),
      P("Fuera de horario",
        T("Llame a la **enfermera de guardia**, las **24 horas**.", "enfermera"),
        PHs("Enfermera de guardia: (919) 555-0151"),
        CR("¿Emergencia? Llame al 911", "ambulancia"))]),

# 8 ── Carta de resultados de laboratorio ───────────────────────────────────────
pair("resultados-lab-es-001", "es", "results", "Carta de resultados de laboratorio (ejemplo inventado)",
     "Carta de resultados de laboratorio\n"
     "Estimado Sr. Ernesto Salas:\n"
     "El Dr. Tomás Aguilar revisó sus análisis de sangre del 20/01/2027.\n"
     "Hemoglobina A1c: 7.8% (meta: menos de 7%). Glucosa en ayunas: 162 mg/dL (normal: 70 a 99). Colesterol LDL: 96 mg/dL "
     "(meta: menos de 100). Función de los riñones: normal.\n"
     "Plan: Su A1c está por encima de la meta. El Dr. Aguilar recomienda empezar empagliflozina 10 mg por la boca una vez al "
     "día por la mañana. Enviamos la receta a su farmacia. Repita la prueba de A1c en 3 meses. Su colesterol LDL está en la "
     "meta; siga con su medicina igual.\n"
     "Le recomendamos una clase de diabetes; llame al (919) 555-0152 para inscribirse.\n"
     "Si tiene preguntas, mande un mensaje por el portal o llame a la clínica al (919) 555-0144.",
     "Sus resultados de sangre",
     [P("Sus resultados",
        T("Para: **Sr. Ernesto Salas**", "persona"),
        T("El **Dr. Tomás Aguilar** revisó sus **análisis de sangre**.", "médico")),
      P("Azúcar en la sangre",
        T("**A1c**: **7.8%**. Meta: menos de **7%**.", "análisis de sangre"),
        T("Su A1c está **alta**.", "advertencia"),
        T("Glucosa en ayunas: **162 mg/dL**", "glucómetro"),
        T("Normal: **70 a 99**.", "meta")),
      P("Colesterol y riñones",
        T("Colesterol **LDL**: **96 mg/dL**", "análisis de sangre"),
        T("Meta: menos de **100**. **Está bien**.", "meta"),
        T("**Riñones**: **normal**.", "riñón")),
      P("Medicina nueva",
        T("**Empiece** empagliflozina **10 mg**.", "pastilla"),
        T("**Una vez** al día, por la **mañana**.", "amanecer"),
        T("Por la **boca**.", "boca"),
        T("La **receta** ya está en su **farmacia**.", "farmacia")),
      P("Su otra medicina",
        T("Siga con su medicina del **colesterol** igual.", "pastilla")),
      P("Próxima prueba",
        T("Repita la prueba de **A1c** en **3 meses**.", "calendario")),
      P("Clase de diabetes",
        T("Le recomendamos una **clase** de **diabetes**.", "clase"),
        PHs("Para inscribirse: (919) 555-0152")),
      P("¿Preguntas?",
        T("Mande un **mensaje** por el **portal**.", "computadora"),
        T("O **llame** a la clínica.", TEL),
        PHs("Clínica: (919) 555-0144"))],
     ["'Por encima de la meta' se escribió 'Su A1c está alta'. Por favor confirme."],
     omitted=["Fecha de los análisis 20/01/2027: fecha pasada"]),

# 9 ── Estado de cuenta del hospital ────────────────────────────────────────────
pair("factura-es-001", "es", "billing", "Estado de cuenta del hospital (ejemplo inventado)",
     "ESTADO DE CUENTA DEL PACIENTE — Hospital Comunitario San Marcos\n"
     "Fecha del estado: 01/02/2027 | Número de cuenta: 5520-114-387 | Responsable: Héctor Navarro\n"
     "Fechas de servicio: 05/01/2027 al 07/01/2027 (hospitalización)\n"
     "Cargos totales: $12,480.00 | Pagos y ajustes del seguro: -$11,980.00 | SALDO A PAGAR: $500.00\n"
     "PAGUE ANTES DEL: 15 de marzo de 2027\n"
     "Formas de pago: en línea en www.example.org/pagar, por teléfono al (919) 555-0153, o por correo con el cupón adjunto. "
     "Hay planes de pago sin intereses.\n"
     "AYUDA FINANCIERA: Usted puede calificar para atención gratis o a menor costo según los ingresos de su hogar. Solicite "
     "en www.example.org/ayuda o llame a un consejero financiero al (919) 555-0155. Mientras revisamos su solicitud, su cuenta "
     "queda en espera.\n"
     "Si cree que esta factura tiene un error, llame a Cuentas de Pacientes al (919) 555-0153 dentro de 60 días.",
     "Su factura del hospital",
     [P("Su factura del hospital",
        T("Para: **Héctor Navarro**", "persona"),
        T("Del **Hospital Comunitario San Marcos**.", "hospital"),
        T("Por su **estadía** en el hospital.", "cama de hospital")),
      P("Lo que debe",
        T("Usted debe **$500.00**.", "dinero"),
        T("Pague antes del **15 de marzo de 2027**.", "calendario")),
      P("Cómo se calcula",
        T("El hospital cobró **$12,480.00**.", "factura"),
        T("El seguro pagó o descontó **$11,980.00**.", "tarjeta de seguro")),
      P("Su número de cuenta",
        T("Número de cuenta: **5520-114-387**", "tarjeta"),
        T("Téngalo a mano cuando **pague**.", "dinero")),
      P("Cómo pagar",
        S("**En línea**: www.example.org/pagar", "computadora"),
        S("Por **teléfono**.", TEL),
        S("Por **correo**, con el **cupón**.", "sobre"),
        PHs("Pagos: (919) 555-0153")),
      P("Plan de pagos",
        T("Puede pagar **poco a poco**.", "dinero"),
        T("**Sin intereses**.", "no")),
      P("Ayuda para pagar",
        T("Puede recibir atención **gratis** o a **menor costo**.", "dinero"),
        T("Depende de los **ingresos** de su hogar.", "casa"),
        T("Mientras revisamos, su cuenta queda en **espera**.", "pausa")),
      P("Pida ayuda",
        T("Solicite en: **www.example.org/ayuda**", "computadora"),
        T("O llame a un **consejero financiero**.", "consejero"),
        PHs("Consejero financiero: (919) 555-0155")),
      P("¿Hay un error?",
        T("**Llame** a Cuentas de Pacientes dentro de **60 días**.", TEL),
        PHs("Cuentas de Pacientes: (919) 555-0153"))],
     omitted=["Fecha del estado 01/02/2027", "Fechas de servicio 05/01/2027 al 07/01/2027: fechas pasadas"]),

# 10 ── Cita con intérprete y transporte ────────────────────────────────────────
pair("cita-transporte-es-001", "es", "appointment", "Confirmación de cita con intérprete y transporte (ejemplo inventado)",
     "CONFIRMACIÓN DE CITA\n"
     "Paciente: Guadalupe Torres. Su cita de medicina de rehabilitación (fisiatría) con el Dr. Alan Brooks es el viernes "
     "19 de febrero de 2027 a las 10:45 a.m. Lugar: Centro de Rehabilitación Lakeside, 1180 Hillcrest Road, Durham.\n"
     "INTÉRPRETE: Tendrá un intérprete de español gratis. No necesita traer a un familiar para interpretar.\n"
     "TRANSPORTE: Si tiene Medicaid, puede pedir transporte gratis. Llame a Transporte Médico al 1-800-555-0156 por lo menos "
     "2 días hábiles antes de su cita. Tenga a mano su número de Medicaid: 900558201.\n"
     "Llegue 15 minutos antes. Traiga su tarjeta de seguro, una identificación con foto y su lista de medicamentos.\n"
     "Para cancelar o cambiar la cita, llame al (919) 555-0157.",
     "Su cita",
     [P("Su cita",
        T("Para: **Guadalupe Torres**", "persona"),
        T("Con el **Dr. Alan Brooks**.", "médico"),
        T("Es un médico de **rehabilitación** (**fisiatría**).", "rehabilitación")),
      P("Cuándo",
        T("**viernes 19 de febrero de 2027**", "calendario"),
        T("**10:45 a.m.**", "reloj"),
        T("Llegue **15 minutos antes**.", "reloj")),
      P("Dónde",
        T("**Centro de Rehabilitación Lakeside**", "clínica"),
        T("**1180 Hillcrest Road, Durham**", "mapa")),
      P("Intérprete",
        T("Tendrá un **intérprete** de **español**.", "intérprete"),
        T("Es **gratis**.", "gratis"),
        T("**No** necesita traer a un **familiar** para interpretar.", "familia")),
      P("Transporte gratis",
        T("¿Tiene **Medicaid**? Puede pedir **transporte gratis**.", "carro"),
        T("Llame por lo menos **2 días hábiles** antes.", "calendario"),
        T("Su número de Medicaid: **900558201**", "tarjeta"),
        PHs("Transporte Médico: 1-800-555-0156")),
      P("Qué traer",
        S("Su **tarjeta de seguro**.", "tarjeta de seguro"),
        S("Una **identificación** con **foto**.", "identificación"),
        S("Su **lista** de **medicamentos**.", "lista de medicamentos")),
      P("Cancelar o cambiar",
        PHs("Teléfono: (919) 555-0157"))]),

# 11 ── Ejercicios para tragar (casillas) ───────────────────────────────────────
pair("programa-deglucion-es-001", "es", "home_program", "Programa de ejercicios para tragar (ejemplo inventado)",
     "PROGRAMA DE EJERCICIOS PARA TRAGAR EN CASA\n"
     "Haga los ejercicios marcados 3 veces al día.\n"
     "[ ] Ejercicio de Shaker: acuéstese boca arriba, levante la cabeza y mire sus pies. Sostenga 60 segundos. Repita 3 veces.\n"
     "[ ] Maniobra de Masako: sostenga la punta de la lengua entre los dientes y trague. Repita 10 veces.\n"
     "[ ] Deglución con esfuerzo: trague con fuerza, apretando todos los músculos de la garganta. Repita 10 veces.\n"
     "[ ] Maniobra de Mendelsohn: al tragar, sostenga la manzana de Adán arriba por 2 segundos. Repita 10 veces.\n"
     "[ ] Presión de lengua: apriete la lengua contra el paladar por 5 segundos. Repita 10 veces.\n"
     "PARE y llame a su terapeuta si tiene tos fuerte, dolor en el pecho o mareo: (919) 555-0159.\n"
     "Su terapeuta: ____________",
     "Ejercicios para tragar",
     [P("Ejercicios para tragar",
        T("Haga los ejercicios **marcados**.", "casilla"),
        T("**3 veces** al día.", "calendario")),
      P("Shaker y Masako",
        C("**Shaker**: acostado, levante la **cabeza** y mire sus **pies**. **60 segundos**, **3 veces**.", "acostado"),
        C("**Masako**: lengua entre los **dientes**, y **trague**. **10 veces**.", "lengua")),
      P("Tragar fuerte y Mendelsohn",
        C("**Trague fuerte**, apretando la **garganta**. **10 veces**.", "tragar"),
        C("**Mendelsohn**: al tragar, mantenga la **manzana de Adán** arriba **2 segundos**. **10 veces**.", "garganta")),
      P("Presión de lengua",
        C("Apriete la **lengua** contra el **paladar**. **5 segundos**, **10 veces**.", "lengua")),
      P("Pare y llame",
        T("¿**Tos** fuerte? ¿**Dolor** en el pecho? ¿**Mareo**?", "tos"),
        T("**Pare** y llame a su **terapeuta**.", "parar"),
        PHs("Teléfono: (919) 555-0159"),
        B("Su terapeuta: ____________", "terapeuta del habla"))],
     ["Los nombres de los ejercicios (Shaker, Masako, Mendelsohn) se dejaron para el terapeuta. Por favor revise que las "
      "instrucciones cortas sean seguras.",
      "Algunas líneas de casilla tienen más de 10 palabras porque cada ejercicio necesita su número de veces."]),

# 12 ── Recursos de salud mental en español ─────────────────────────────────────
pair("recursos-salud-mental-es-001", "es", "mental_health", "Recursos de salud mental en español (ejemplo inventado)",
     "RECURSOS DE SALUD MENTAL EN ESPAÑOL\n"
     "La depresión es común después de un derrame cerebral. Las señales incluyen: tristeza por más de 2 semanas, perder el "
     "interés en cosas que antes disfrutaba, dormir mucho o muy poco, y sentirse sin esperanza. La depresión se puede tratar.\n"
     "CONSEJERÍA: El Centro de Consejería Oak Valley tiene consejeros que hablan español. El costo depende de sus ingresos. "
     "Llame al (919) 555-0160.\n"
     "GRUPO DE APOYO: El Grupo Esperanza se reúne cada jueves a las 5:30 p.m. en la Biblioteca Oakwood, 220 Maple Avenue, "
     "Sala B. Es gratis y en español.\n"
     "CRISIS: Si piensa en hacerse daño, llame o envíe un mensaje de texto al 988. Hay ayuda en español. Si está en peligro "
     "inmediato, llame al 911.",
     "Ayuda para su salud mental",
     [P("La depresión",
        T("La **depresión** es común después de un **derrame**.", "triste"),
        T("Se puede **tratar**.", "mejorar")),
      P("Señales",
        T("¿Triste por **más de 2 semanas**?", "calendario"),
        T("¿Ya **no le interesan** las cosas que le gustaban?", "aburrido"),
        T("¿Duerme **mucho** o **muy poco**?", "cama"),
        T("¿Se siente **sin esperanza**?", "triste")),
      P("Consejería en español",
        T("**Centro de Consejería Oak Valley**", "edificio"),
        T("Los consejeros hablan **español**.", "consejero"),
        T("El **costo** depende de sus **ingresos**.", "dinero"),
        PHs("Teléfono: (919) 555-0160")),
      P("Grupo de apoyo",
        T("**Grupo Esperanza**, gratis y en **español**.", "grupo"),
        T("Cada **jueves** a las **5:30 p.m.**", "calendario"),
        T("**Biblioteca Oakwood**, **220 Maple Avenue**, **Sala B**", "biblioteca")),
      P("Ayuda ahora",
        T("¿Piensa en **hacerse daño**?", "ayuda"),
        CR("Llame o envíe un mensaje de texto al 988. Hay ayuda en español.", TEL),
        T("¿Está en **peligro** ahora?", "peligro"),
        CR("Llame al 911", "ambulancia"))]),
]

write(PAIRS, "batch3_es.jsonl")
