"""Contenido original, editable. Guía y manual de trabajo; no es evaluación de conformidad."""
VERSION = 'v0.3'
DATE_LABEL = '19 OCT 2026'

# Fuentes. Etiquetas: [P] primaria leída directamente; [S] secundaria o ficha no reverificada.
SOURCES = [
 ('1','ISO/IEC 42001:2023','[S] Ficha oficial: requisitos para un sistema de gestión de IA; publicada en diciembre de 2023. Texto íntegro no revisado.','https://www.iso.org/standard/42001'),
 ('2','ISO/IEC 27090:2026','[S] Ficha oficial. La versión anterior registró publicación el 14 de octubre de 2026; no pudimos volver a abrir la ficha (acceso bloqueado), así que la fecha no está reverificada. Texto íntegro no revisado.','https://www.iso.org/standard/27090'),
 ('3','ISO27k Forum (IsecT): ISO/IEC 27090','[S] Descripción del alcance y de las amenazas que cubre (envenenamiento, inversión y robo de modelos, entre otras) y aviso de publicación.','https://www.iso27001security.com/html/27090'),
 ('4','Estructura de ISO/IEC 42001 (cláusulas y Anexo A)','[S] Cláusulas 4 a 10, evaluación de impacto (6.1.4) y Anexo A con 9 objetivos y 38 controles, según catálogos públicos de terceros. Verificar contra la norma.','https://riskprofs.com/iso-42001-annex-a-controls-list/'),
 ('5','NIST AI 100-2e2025','[P] Vassilev et al., marzo de 2025. Índice leído: 3.4 inyección indirecta de prompts; 3.5 seguridad de agentes. Resto, lectura selectiva.','https://doi.org/10.6028/NIST.AI.100-2e2025'),
 ('6','OWASP Top 10 for LLM Applications 2025','[S] OWASP GenAI Security Project, noviembre de 2024. Lista LLM01 a LLM10 según cobertura de terceros.','https://genai.owasp.org'),
 ('7','MITRE ATLAS','[S] Base de conocimiento de tácticas y técnicas contra sistemas de IA, modelada sobre ATT&CK, con casos documentados.','https://atlas.mitre.org'),
 ('8','Dunlosky et al. (2013)','[S] Improving Students\' Learning With Effective Learning Techniques. Psychological Science in the Public Interest. DOI 10.1177/1529100612453266.','https://doi.org/10.1177/1529100612453266')]

# Bloques: p, heading, callout, table, relation, steps, code, sources.
RESEARCH_GUIDE = {
 'directory':'guides/es','filename':'Guia_de_Investigacion_IA.pdf','kind':'GUÍA DE INVESTIGACIÓN',
 'title':'Gestión y\nseguridad de IA\ncon ISO',
 'subtitle':'Qué pide ISO/IEC 42001, qué cubre ISO/IEC 27090, cómo aprenderlas en cuatro semanas y cómo investigar un sistema de IA con evidencia.',
 'cover_iso':'ISO/IEC 42001:2023  +  ISO/IEC 27090:2026',
 'cover_note':'Para equipos pequeños de seguridad y de gobierno de IA. Basada en el alcance público de las normas y en fuentes abiertas; sin certificación ni conformidad demostrada.',
 'cover_steps':['Entender las dos normas','Aprenderlas con método','Investigar con evidencia'],
 'pages':[
 ('01','Para qué sirve esta guía',[
  ('callout','OBJETIVO','Que una persona con base en seguridad entienda qué pide cada norma, aprenda a usarlas en cuatro semanas y pueda investigar un sistema de IA real con evidencia que otro pueda revisar.'),
  ('table',['Si necesitas…','Ve a'],[
   ['Saber qué es cada norma y cómo se relacionan','02 Las dos normas en una página'],
   ['Conocer la estructura de ISO/IEC 42001','03 Cláusulas y 04 Anexo A'],
   ['Conocer las amenazas que cubre ISO/IEC 27090','05 Amenazas y vocabulario abierto'],
   ['Aprenderlas rápido','06 Camino de cuatro semanas'],
   ['Investigar un sistema sin afirmar de más','07 Evidencia y 08 Caso de práctica']]),
  ('heading','Cómo está hecha'),
  ('p','Se apoya en el alcance público de las normas [1, 2], en descripciones de terceros [3, 4] y en fuentes abiertas sobre ataques a sistemas de IA [5, 6, 7]. No leímos el texto íntegro de ninguna de las dos normas ISO: lo que se dice de ellas es su alcance y su estructura pública, no el contenido de sus requisitos o controles. Cada fuente lleva una etiqueta: [P] leída directamente, [S] secundaria o no reverificada.'),
  ('p','El complemento práctico es el Manual de buenas prácticas de IA, con fichas y plantillas para aplicar lo que aquí se explica.'),
  ('callout','QUÉ NO ES','Una interpretación autorizada de las normas, una lista de cumplimiento ni un sustituto de leerlas. Para certificarse hace falta la edición completa y un proceso con un organismo acreditado.')]),
 ('02','Las dos normas en una página',[
  ('p','ISO/IEC 42001 dice cómo debe gobernar una organización sus sistemas de IA. ISO/IEC 27090 trata de cómo se atacan esos sistemas y qué hacer al respecto. Una cubre la gestión; la otra, las amenazas técnicas.'),
  ('relation',None),
  ('table',['Aspecto','ISO/IEC 42001:2023','ISO/IEC 27090:2026'],[
   ['Tipo de documento','Requisitos para un sistema de gestión de IA [1].','Guía de orientación sobre amenazas y compromisos de seguridad [2, 3].'],
   ['Pregunta que responde','¿Quién decide, con qué política y cómo se controla y mejora el uso de IA?','¿Qué amenazas existen en cada fase del ciclo de vida y cómo detectarlas y mitigarlas?'],
   ['Certificación','Certificable de forma voluntaria por organismos acreditados [1, 4].','Por ser una guía, no define requisitos para certificar (inferencia nuestra, a confirmar).'],
   ['Con qué se combina','Comparte la estructura de cláusulas de otras normas de sistemas de gestión, como ISO/IEC 27001 [4].','Complementa las prácticas de ISO/IEC 27001 y 27002 con amenazas propias de la IA [3].']]),
  ('p','En la práctica, 42001 te obliga a evaluar riesgos e impactos de tus sistemas de IA, y 27090 te ayuda a que esa evaluación técnica no se quede corta en amenazas que una evaluación de seguridad clásica no contempla.')]),
 ('03','ISO/IEC 42001 por dentro: las cláusulas',[
  ('p','Las cláusulas 4 a 10 son los requisitos auditables del sistema de gestión. Siguen la estructura común de las normas de sistemas de gestión ISO, por eso quien conoce ISO/IEC 27001 reconoce el esqueleto [4]. El resumen de cada una es nuestro, de alto nivel.'),
  ('table',['Cláusula','Qué pide, en una línea'],[
   ['4 Contexto','Entender la organización, las partes interesadas y definir el alcance del sistema de gestión de IA.'],
   ['5 Liderazgo','Compromiso de la dirección, política de IA y roles con responsabilidad asignada.'],
   ['6 Planificación','Riesgos y oportunidades, evaluación y tratamiento de riesgos de IA, evaluación de impacto del sistema de IA (6.1.4) y objetivos [4].'],
   ['7 Apoyo','Recursos, competencia, concienciación, comunicación e información documentada.'],
   ['8 Operación','Planificar y controlar la operación; ejecutar las evaluaciones y los tratamientos.'],
   ['9 Evaluación del desempeño','Seguimiento y medición, auditoría interna y revisión por la dirección.'],
   ['10 Mejora','No conformidades, acciones correctivas y mejora continua.']]),
  ('heading','La pieza nueva: la evaluación de impacto'),
  ('p','La evaluación de impacto del sistema de IA (6.1.4) mira hacia afuera: qué efectos puede tener el sistema sobre personas, grupos y la sociedad. Es distinta de la evaluación de riesgos para la organización (6.1.2) y se piden las dos [4]. Es lo que más diferencia a 42001 de una norma de seguridad de la información.')]),
 ('04','ISO/IEC 42001 por dentro: el Anexo A',[
  ('p','El Anexo A es un catálogo de referencia: 38 controles agrupados en 9 objetivos, de A.2 a A.10 [4]. La organización revisa todos, aplica los que corresponden y justifica las exclusiones en la Declaración de Aplicabilidad. Los títulos siguientes vienen de catálogos de terceros; los identificadores exactos de cada control deben verificarse en la norma.'),
  ('table',['Objetivo','De qué trata'],[
   ['A.2 Políticas relacionadas con la IA','La política de IA y su relación con otras políticas.'],
   ['A.3 Organización interna','Roles y responsabilidades sobre la IA dentro de la organización.'],
   ['A.4 Recursos para sistemas de IA','Datos, herramientas, cómputo y personas que el sistema necesita.'],
   ['A.5 Evaluación de impactos','Cómo se evalúan los impactos sobre personas, grupos y sociedad.'],
   ['A.6 Ciclo de vida del sistema de IA','Gestión responsable del sistema a lo largo de su ciclo de vida, del diseño al retiro.'],
   ['A.7 Datos para sistemas de IA','Calidad, procedencia y preparación de los datos.'],
   ['A.8 Información para partes interesadas','Qué se informa a usuarios y afectados.'],
   ['A.9 Uso de sistemas de IA','Uso responsable conforme a la finalidad prevista.'],
   ['A.10 Terceros y clientes','Proveedores, clientes y responsabilidades compartidas.']]),
  ('callout','CÓMO USARLO','Para cada sistema de IA, anota qué objetivo del Anexo A cubre cada práctica y deja la referencia exacta pendiente hasta leerla en la norma. Rellenar por parecido de palabras produce una matriz que no resiste una auditoría.')]),
 ('05','ISO/IEC 27090: amenazas y vocabulario abierto',[
  ('p','27090 orienta sobre amenazas y compromisos de seguridad contra sistemas de IA a lo largo de su ciclo de vida: qué consecuencias pueden tener y cómo detectarlas y mitigarlas. Según el ISO27k Forum cubre al menos una docena de escenarios de ataque deliberado, entre ellos el envenenamiento de datos y de modelos, la inversión de modelos y el robo de modelos [3]. No cubre todos los riesgos de la IA.'),
  ('p','Mientras consigues la norma, las fuentes abiertas dan el vocabulario técnico. La correspondencia de la tabla es nuestra y aproximada: sirve para estudiar, no como mapeo oficial.'),
  ('table',['Amenaza','Dónde estudiarla en abierto','Fase del ciclo de vida'],[
   ['Envenenamiento de datos o modelos','NIST AI 100-2, ataques de envenenamiento [5]; OWASP LLM04 [6].','Datos y entrenamiento.'],
   ['Inversión de modelos y fuga de datos','NIST AI 100-2, ataques de privacidad [5]; OWASP LLM02 [6].','Operación.'],
   ['Robo o extracción de modelos','NIST AI 100-2, ataques de privacidad [5]; MITRE ATLAS [7].','Operación.'],
   ['Inyección indirecta de prompts','NIST AI 100-2, sección 3.4 [5]; OWASP LLM01 [6].','Operación con contenido externo.'],
   ['Agentes con herramientas','NIST AI 100-2, sección 3.5 [5]; OWASP LLM06, agencia excesiva [6].','Operación e integración.'],
   ['Cadena de suministro','NIST AI 100-2, sección 3.2 [5]; OWASP LLM03 [6].','Desarrollo y despliegue.']]),
  ('p','MITRE ATLAS agrega casos reales documentados de cada técnica, útiles para entender cómo ocurre un ataque y no solo cómo se llama [7].')]),
 ('06','Cómo aprenderlas en cuatro semanas',[
  ('p','El orden va de lo público a lo de pago y de lo conceptual a lo aplicado. Estimamos entre cuatro y seis horas por semana para una persona con base en seguridad; es una estimación nuestra, no una medición.'),
  ('steps',[('Semana 1: mapa','Leer el alcance público de 42001 y 27090. Dibujar de memoria el ciclo de vida de un sistema de IA propio con sus activos: datos, modelo, prompts, herramientas y salidas. Prueba: explicar en tres minutos la diferencia entre las dos normas.'),('Semana 2: amenazas','Recorrer NIST AI 100-2, OWASP LLM Top 10 y MITRE ATLAS. Armar una tabla de amenazas por fase y por fuente. Prueba: clasificar un incidente descrito en un párrafo sin mirar la tabla.'),('Semana 3: controles','Leer la norma con una pregunta por amenaza: qué control propone, cuál ya existe en la organización y qué evidencia lo demuestra. Es la única semana que exige el texto de pago.'),('Semana 4: aplicar','Elegir un sistema real y acotado, modelar sus amenazas, marcar controles y brechas y decidir el riesgo residual. Prueba: modelar un sistema nuevo en noventa minutos y contrastarlo con otra persona.')]),
  ('callout','RECUPERAR, NO RELEER','En la revisión de Dunlosky y colaboradores, la práctica de recuperación y la práctica espaciada tuvieron utilidad alta; releer y subrayar, baja [8]. Cada semana termina con una prueba sin apuntes que se repite al día siguiente, al tercero y al séptimo. El esquema de repeticiones es nuestro.')]),
 ('07','Investigar con evidencia',[
  ('p','Saber las normas no basta: una conclusión sobre un sistema de IA solo vale lo que vale su evidencia. Proponemos seis registros enlazados por un identificador de evaluación: alcance, contexto, plan de prueba, observación, verificación y conclusión. El detalle de cada uno está en el manual.'),
  ('heading','Cuatro estados que no deben mezclarse'),
  ('steps',[('Propuesto','El plan existe; no se ha ejecutado.'),('Observado','Hay una respuesta o una captura, con su contexto.'),('Reproducido','Un segundo intento bajo condiciones declaradas obtiene el mismo efecto.'),('Verificado','Un revisor comprueba que la evidencia sustenta la afirmación, acotada.')]),
  ('p','Son una convención de NullGhost, no categorías de ISO. Un resultado negativo se escribe «no observado bajo estas condiciones», nunca «no es vulnerable». Si el instrumento falla o se agota el tiempo, la prueba es inconclusa, no segura.'),
  ('callout','REGLA DE PUBLICACIÓN','Antes de publicar, otra persona debe poder reconstruir qué se autorizó, qué se hizo y qué cambió. Si solo puede leer una conclusión convincente, el informe no está listo.')]),
 ('08','Un caso para practicar',[
  ('p','Un sistema acotado enseña más que uno amplio. Ejemplo: un asistente de ayuda dentro de una plataforma, como la guía de módulo de KIRUX, con un diseño deliberadamente estrecho: usa solo un modelo local, no tiene herramientas, recibe únicamente el texto fijo del módulo y ningún dato de clientes, la respuesta se valida en el servidor y hay límites de uso por usuario.'),
  ('table',['Decisión de diseño','Amenaza que acota','Qué falta por probar'],[
   ['Sin herramientas','Agencia excesiva (OWASP LLM06).','Que ninguna ruta del código le dé acciones por otra vía.'],
   ['Sin datos de clientes','Fuga de información sensible (LLM02).','Que el texto del módulo no contenga nada sensible.'],
   ['Límites de uso','Consumo sin límites (LLM10).','Que los límites se apliquen por usuario y no por sesión.'],
   ['Validación en servidor','Salidas no esperadas.','Que la validación rechace respuestas con enlaces o código.']]),
  ('p','La tabla no demuestra que el asistente sea seguro: muestra qué amenazas reduce el diseño y cuáles quedan abiertas. La más evidente es la inyección de prompts (LLM01) desde la pregunta del usuario, que es justo lo que la semana cuatro debería modelar y probar.')]),
 ('09','Límites y siguiente versión',[
  ('heading','Lo que esta guía no hace'),
  ('steps',[('No interpreta las normas','No leímos su texto íntegro. Lo que se dice de ellas es alcance y estructura pública, con fuentes secundarias marcadas.'),('No mide eficacia','El camino de cuatro semanas y el método de evidencia son propuestas sin validar con otros equipos.'),('No certifica','Una guía, un repositorio público y un PDF no acreditan un sistema de gestión implantado.')]),
  ('heading','Qué cambiaría la versión siguiente'),
  ('p','Contrastar todo con las ediciones completas, sustituir las fuentes secundarias por la norma, correr el camino de cuatro semanas con personas reales y publicar los resultados, incluidos los que no funcionen.'),
  ('callout','POLÍTICA DE CAMBIOS','Cada corrección dice qué afirmación cambia, por qué y con qué fuente. La v0.3 reescribe la v0.2: añade el contenido de las normas y el camino de aprendizaje, y retira un ejemplo que no aportaba al tema.')]),
 ('10','Referencias',[
  ('sources',None),
  ('p','Consulta de fuentes: 19 de octubre de 2026. Elaboración asistida por IA, con revisión técnica humana pendiente. No se redistribuyen las normas.')])
 ]}

MANUAL = {
 'directory':'manuals/es','filename':'Manual_de_Buenas_Practicas_IA.pdf','kind':'MANUAL DE BUENAS PRÁCTICAS',
 'title':'Manual de buenas\nprácticas de IA',
 'subtitle':'Fichas y plantillas para gobernar, proteger y documentar un sistema de IA, una pieza a la vez.',
 'cover_iso':'Referencias: ISO/IEC 42001:2023  +  ISO/IEC 27090:2026',
 'cover_note':'Complemento práctico de la Guía de investigación. Ejemplos sintéticos; sin datos de clientes ni conformidad demostrada.',
 'cover_steps':['Inventariar y asignar','Evaluar riesgo e impacto','Probar, documentar y revisar'],
 'pages':[
 ('01','Empezar por un sistema',[
  ('callout','OBJETIVO','Construir un expediente que permita revisar decisiones y resultados de un sistema de IA. No llenar una lista para aparentar cumplimiento.'),
  ('steps',[('Elegir una finalidad','Qué hace el sistema, para quién y qué decisión ayuda a tomar.'),('Nombrar responsables','Alguien que pueda aceptar el riesgo, detener una prueba y revisar el informe.'),('Delimitar','Qué entra y qué queda fuera. Datos sintéticos y entorno de prueba para evaluar.'),('Fijar la salida','Qué evidencia permite avanzar, cuál la vuelve inconclusa y cuál obliga a parar.')]),
  ('table',['Rol','Responsabilidad'],[
   ['Dueño del sistema de IA','Finalidad, alcance y decisión sobre el riesgo residual.'],
   ['Ingeniería y seguridad','Configuración, modelo de amenazas y ejecución de las pruebas autorizadas.'],
   ['Revisor de evidencia','Contrastar el efecto observado con la afirmación.'],
   ['Responsable de publicación','Versión, procedencia, datos excluidos y permiso de difusión.']]),
  ('p','Si una persona asume varios roles, decláralo. Una autoevaluación no equivale a una revisión independiente.')]),
 ('02','Ficha de inventario',[
  ('p','Una fila por sistema de IA. El ejemplo es ficticio. La ficha responde lo que piden las cláusulas de contexto y apoyo de 42001 (alcance, recursos e información documentada) sin pretender cubrirlas.'),
  ('table',['Campo','Ejemplo sintético'],[
   ['Identificador y finalidad','LAB-AI-01: resumir documentos internos de prueba.'],
   ['Dueño y revisor','Rol dueño del sistema; rol revisor.'],
   ['Modelo y versión','Identificador observable; «desconocido» si el proveedor no lo expone.'],
   ['Datos de entrada','Documentos sintéticos, sin datos personales ni secretos.'],
   ['Herramientas y permisos','Lectura de una carpeta permitida; sin envío de mensajes ni escritura.'],
   ['Proveedores','Quién aloja el modelo y qué hace con los datos (objetivo A.10).'],
   ['Cruces de confianza','Documento → modelo; modelo → herramienta; resultado → informe.'],
   ['Retención','Qué se guarda, cuánto tiempo y quién accede.']]),
  ('heading','Preguntas de cierre'),
  ('p','¿Se puede reconstruir qué modelo, versión y permisos participaron? ¿Los datos se usan para entrenar o se guardan en memoria? ¿Quién controla el almacenamiento? Lo que no se sepa queda como pendiente, no como supuesto.'),
  ('callout','PLANTILLA','templates/inventario.csv. Sin claves ni tokens en el inventario.')]),
 ('03','Ficha de riesgo y tratamiento',[
  ('p','Una fila por escenario. Las amenazas vienen del vocabulario abierto de la guía; la severidad sale de la exposición real, no del nombre de la amenaza. La columna de referencia normativa se llena solo después de verificarla en la norma.'),
  ('table',['Escenario','Consecuencia','Tratamiento y evidencia'],[
   ['Un documento externo trae instrucciones ocultas (LLM01).','La herramienta actúa sobre un destino no autorizado.','Política de destinos aplicada fuera del modelo; prueba que la deniega.'],
   ['El agente tiene más permisos de los que necesita (LLM06).','Una acción no prevista con efecto real.','Mínimo privilegio por herramienta; registro de cada acción.'],
   ['La respuesta revela datos que no debía (LLM02).','Fuga de información personal o interna.','Filtro y revisión antes de publicar; marcador sintético de prueba.'],
   ['Datos de entrenamiento o contexto alterados (LLM04).','El modelo aprende o repite contenido manipulado.','Procedencia de los datos registrada (objetivo A.7); revisión de cambios.'],
   ['Uso sin límites (LLM10).','Costo descontrolado o servicio degradado.','Límites por usuario y alerta de consumo.']]),
  ('callout','ACEPTAR UN RIESGO','La decisión dice qué exposición se acepta, bajo qué condiciones, por cuánto tiempo y quién la revisa. Un cambio de modelo, permisos, datos o finalidad la invalida.'),
  ('p','Plantilla: templates/riesgos.csv.')]),
 ('04','Evaluación de impacto',[
  ('p','42001 pide evaluar el impacto del sistema de IA sobre personas, grupos y la sociedad (6.1.4), además de los riesgos para la organización [4]. Esta ficha es una forma práctica de empezar; no reproduce el método de la norma.'),
  ('table',['Pregunta','Qué registrar'],[
   ['¿A quién afecta el resultado?','Usuarios directos, personas sobre las que se decide y terceros.'],
   ['¿Qué decisión apoya?','Si informa, recomienda o decide; y quién puede revisarla o revertirla.'],
   ['¿Qué pasa si se equivoca?','Daño posible, a quién y si es reversible.'],
   ['¿Puede tratar distinto a grupos distintos?','Datos o reglas que puedan producir un trato desigual.'],
   ['¿Qué se le informa a la persona?','Que interactúa con IA y cómo pedir revisión humana (objetivo A.8).'],
   ['¿Qué datos personales usa?','Base legal y aviso de privacidad; en México, conforme a la LFPDPPP.']]),
  ('callout','CRITERIO DE PARADA','Detener una prueba ante un destino fuera de alcance, datos reales no previstos, un cambio no autorizado o pérdida de observabilidad. Conservar el fallo y avisar al dueño del sistema.')]),
 ('05','Plan de prueba',[
  ('p','Definir el efecto esperado antes de ejecutar. Los casos son propuestas para un entorno de prueba con datos sintéticos, no pruebas realizadas.'),
  ('table',['Caso','Control legítimo','Resultado esperado'],[
   ['T01 alcance','Leer un archivo dentro de la carpeta autorizada.','Funciona; otro destino se deniega sin ejecutarse.'],
   ['T02 entrada no confiable','Resumir un texto sin instrucciones añadidas.','Una instrucción añadida no cambia permisos ni destino.'],
   ['T03 fallo del instrumento','Una respuesta completa y otra con tiempo agotado.','El segundo informe dice inconcluso, no seguro.'],
   ['T04 publicación','Texto con y sin un marcador sintético de secreto.','El marcador se detecta antes de difundir.'],
   ['T05 consumo','Peticiones por debajo y por encima del límite.','El exceso se rechaza y queda registrado.']]),
  ('heading','Antes y después de correr'),
  ('p','Antes: versión del modelo, permisos, datos sintéticos, límite de tiempo y número de repeticiones, fijados de antemano. Después: salida bruta, efecto observado, errores y desviaciones. Se conservan todos los intentos comparables, no solo el favorable.'),
  ('p','Plantilla: templates/pruebas.csv.')]),
 ('06','Expediente de evidencia',[
  ('table',['Archivo','Contenido'],[
   ['scope.json','Quién autoriza, vigencia, destinos y operaciones permitidas.'],
   ['environment.json','Modelo, versión, herramientas, permisos y limitaciones.'],
   ['plan.json','Hipótesis, control, estímulo y resultado esperado.'],
   ['observations/','Originales fechados: salidas y capturas con contexto.'],
   ['manifest.sha256','Huellas de los originales.'],
   ['review.md','Conclusión, contraevidencia, límites y firma del revisor.']]),
  ('heading','Ejemplo de registro, no evidencia real'),
  ('code','{\n  "assessment_id": "DEMO-001",\n  "test_id": "T03",\n  "status": "inconclusive",\n  "reason": "simulated timeout",\n  "claim": "No conclusion about security"\n}'),
  ('p','Las huellas detectan cambios posteriores; no prueban que el contenido sea cierto ni que hubiera autorización. Eso lo dan los registros de alcance y la revisión.'),
  ('callout','CONSERVAR NO ES DIFUNDIR','El expediente privado puede tener detalles que no van en el documento público. Permiso para probar un sistema no es permiso para publicar su identidad ni sus datos.')]),
 ('07','Aplicabilidad y estados',[
  ('p','La matriz de aplicación junta las fichas anteriores: cada práctica, su objetivo del Anexo A, su dueño, la evidencia esperada y su estado. Es la base de una futura Declaración de Aplicabilidad, no la declaración misma.'),
  ('table',['Estado','Qué permite afirmar'],[
   ['Pendiente','Nada todavía sobre implementación o conformidad.'],
   ['Diseñada','La práctica está especificada; no que funcione.'],
   ['Implementada','Existe evidencia de configuración o procedimiento.'],
   ['Probada','Un caso declarado observó el efecto esperado.'],
   ['Revisada','Una revisión acotada respalda la conclusión.']]),
  ('heading','Adopción en cuatro etapas'),
  ('steps',[('Alcance','Inventario, finalidad, responsables y límites, validados por el dueño.'),('Amenazas e impacto','Fichas de riesgo y de impacto con dueño y evidencia esperada.'),('Contraste normativo','Lectura de las ediciones completas: referencias verificadas y dudas registradas.'),('Pruebas y revisión','Plan ejecutado, expediente reproducible y acciones de mejora.')]),
  ('p','Plantilla: templates/matriz_aplicacion.csv. Ningún estado equivale por sí solo a cumplimiento.')]),
 ('08','Revisión antes de publicar',[
  ('steps',[('Afirmaciones','Cada conclusión dice si es observada, inferida, propuesta o normativa. Sin porcentajes sin denominador ni resultados inventados.'),('Procedencia','Se sabe qué entorno, versión e identidad produjo cada resultado. Incluye fallos y contraevidencia.'),('Información','Sin datos de clientes, datos personales, credenciales ni capturas fuera del permiso de difusión.'),('Normas','No se reproduce texto de ISO. Las referencias por cláusula están verificadas o marcadas como pendientes.'),('Estado editorial','Versión, fecha, límites y asistencia de IA visibles.')]),
  ('callout','CRITERIO FINAL','El lector puede reconstruir qué se autorizó, qué se hizo y qué cambió. Si solo puede leer una conclusión convincente, el expediente aún no está listo.')]),
 ('09','Fuentes y plantillas',[
  ('sources',None),
  ('p','Plantillas CSV, generador y contenido editable en github.com/nullghost-io/ai-governance-evidence. Ejemplos sintéticos; sin normas ISO ni información de clientes. Elaboración asistida por IA, con revisión técnica humana pendiente.')])
 ]}
