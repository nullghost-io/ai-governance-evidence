"""Genera las composiciones ES/EN del video de la guía y el manual de IA (v0.4).

Todo el texto sale de content.py (guía y manual); no hay cifras propias.
Salida: index.html (ES) y compositions/en.html (EN). Render con HyperFrames.
"""
import math
from pathlib import Path
from html import escape as E

R = Path(__file__).resolve().parent
DUR = 56
VERSION = 'v0.4'

# Escenas: (id, inicio, duración)
SCENES = [('s1', 0, 5.5), ('s2', 5.5, 7.5), ('s3', 13, 8), ('s4', 21, 7),
          ('s5', 28, 8), ('s6', 36, 8), ('s7', 44, 6), ('s8', 50, 6)]

COPY = {
 'es': dict(
  category='GUÍA Y MANUAL DE IA', footer='Referencias para investigar y evaluar. No acredita certificación.',
  s1_kick='ISO · INTELIGENCIA ARTIFICIAL', s1_title=['Dos normas ISO', 'para la IA.'],
  s1_sub='Una dice cómo gobernarla. La otra, cómo la atacan.',
  s2_title='Dos preguntas distintas sobre el mismo sistema',
  a_name='Sistema de gestión de IA', a_q='¿Quién decide, con qué política y cómo se controla y mejora el uso de IA?', a_tag='Requisitos · certificable',
  b_name='Amenazas contra sistemas de IA', b_q='¿Qué amenazas hay en cada fase del ciclo de vida y cómo detectarlas y mitigarlas?', b_tag='Guía de orientación',
  node='Tu sistema de IA', assets=['datos', 'modelo', 'prompts', 'herramientas', 'salidas'],
  s2_note='42001 obliga a evaluar riesgos e impactos. 27090 evita que esa evaluación se quede corta.',
  s3_kick='ISO/IEC 42001:2023 POR DENTRO', s3_title='Siete cláusulas auditables',
  ring_c='Cláusulas', ring_s='4 a 10',
  clauses=[('4', 'Contexto', 'alcance y partes interesadas'), ('5', 'Liderazgo', 'política de IA y roles'),
           ('6', 'Planificación', 'riesgos, impacto y objetivos'), ('7', 'Apoyo', 'recursos y competencia'),
           ('8', 'Operación', 'ejecutar evaluaciones y tratamientos'), ('9', 'Evaluación', 'medición, auditoría y revisión'),
           ('10', 'Mejora', 'acciones correctivas')],
  impact_k='6.1.4 · LA PIEZA NUEVA', impact='Evaluación de impacto: efectos sobre personas, grupos y la sociedad. Se pide además de la de riesgos (6.1.2).',
  s4_kick='ISO/IEC 42001 · ANEXO A', s4_title='Un catálogo de referencia',
  n_ctrl='controles', n_obj='objetivos',
  objectives=[('A.2', 'Políticas de IA'), ('A.3', 'Organización interna'), ('A.4', 'Recursos'),
              ('A.5', 'Evaluación de impactos'), ('A.6', 'Ciclo de vida'), ('A.7', 'Datos'),
              ('A.8', 'Información a partes interesadas'), ('A.9', 'Uso de sistemas de IA'), ('A.10', 'Terceros y clientes')],
  soa=['Revisar todos', 'Aplicar los que corresponden', 'Justificar exclusiones', 'Declaración de Aplicabilidad'],
  s4_src='Estructura según catálogos públicos de terceros. Verificar en la norma.',
  s5_kick='ISO/IEC 27090:2026', s5_title='Amenazas en todo el ciclo de vida',
  phases=['Datos y entrenamiento', 'Desarrollo y despliegue', 'Operación e integración'],
  threats=[(0, 'Envenenamiento de datos o modelos', 'LLM04'), (1, 'Cadena de suministro', 'LLM03'),
           (2, 'Inversión de modelos y fuga de datos', 'LLM02'), (2, 'Robo o extracción de modelos', 'ATLAS'),
           (2, 'Inyección indirecta de prompts', 'LLM01'), (2, 'Agentes con herramientas', 'LLM06')],
  s5_stat='12+', s5_stat_l='escenarios de ataque deliberado, según el ISO27k Forum',
  s5_src='Correspondencia aproximada de NullGhost con NIST AI 100-2, OWASP Top 10 para LLM y MITRE ATLAS. No es un mapeo oficial.',
  s6_kick='CAMINO DE APRENDIZAJE', s6_title='Aprenderlas en cuatro semanas',
  weeks=[('Semana 1', 'Mapa', 'alcance y ciclo de vida'), ('Semana 2', 'Amenazas', 'NIST · OWASP · ATLAS'),
         ('Semana 3', 'Controles', 'leer la norma completa'), ('Semana 4', 'Aplicar', 'un sistema real y acotado')],
  hours='4 a 6 horas por semana · estimación nuestra',
  util_t='Utilidad de cada técnica · Dunlosky et al. (2013)',
  util=[('Práctica de recuperación', 'alta', 1.0), ('Práctica espaciada', 'alta', 1.0), ('Releer', 'baja', .28), ('Subrayar', 'baja', .28)],
  rep_t='Cada semana cierra con una prueba sin apuntes', rep_l='Repetir el día', days='día',
  s7_kick='MÉTODO DE EVIDENCIA', s7_title='Cuatro estados que no se mezclan',
  states=[('Propuesto', 'El plan existe; no se ha ejecutado.'), ('Observado', 'Hay una respuesta o captura, con contexto.'),
          ('Reproducido', 'Un segundo intento obtiene el mismo efecto.'), ('Verificado', 'Un revisor confirma que la evidencia lo sustenta.')],
  bad='«No es vulnerable»', good='«No observado bajo estas condiciones»',
  s7_note='Si el instrumento falla o se agota el tiempo, la prueba es inconclusa, no segura.',
  s8_title=['Entender, aprender', 'y probar con evidencia.'],
  guide='Guía de investigación', guide_d='11 páginas',
  manual='Manual de buenas prácticas', manual_d='10 páginas · plantillas CSV',
  url='nullghost.io/ia-normas.html', repo='github.com/nullghost-io/ai-governance-evidence',
  status=f'Versión de trabajo {VERSION} · Revisión técnica pendiente · PDF en español'),
 'en': dict(
  category='AI GUIDE & MANUAL', footer='References for research and evaluation. Not a certification.',
  s1_kick='ISO · ARTIFICIAL INTELLIGENCE', s1_title=['Two ISO standards', 'for AI.'],
  s1_sub='One says how to govern it. The other, how it gets attacked.',
  s2_title='Two different questions about the same system',
  a_name='AI management system', a_q='Who decides, under which policy, and how is AI use controlled and improved?', a_tag='Requirements · certifiable',
  b_name='Threats against AI systems', b_q='Which threats exist at each lifecycle stage, and how are they detected and mitigated?', b_tag='Guidance document',
  node='Your AI system', assets=['data', 'model', 'prompts', 'tools', 'outputs'],
  s2_note='42001 requires assessing risks and impacts. 27090 keeps that assessment from falling short.',
  s3_kick='INSIDE ISO/IEC 42001:2023', s3_title='Seven auditable clauses',
  ring_c='Clauses', ring_s='4 to 10',
  clauses=[('4', 'Context', 'scope and interested parties'), ('5', 'Leadership', 'AI policy and roles'),
           ('6', 'Planning', 'risks, impact and objectives'), ('7', 'Support', 'resources and competence'),
           ('8', 'Operation', 'run assessments and treatments'), ('9', 'Evaluation', 'measurement, audit and review'),
           ('10', 'Improvement', 'corrective action')],
  impact_k='6.1.4 · THE NEW PIECE', impact='AI system impact assessment: effects on individuals, groups and society. Required in addition to risk assessment (6.1.2).',
  s4_kick='ISO/IEC 42001 · ANNEX A', s4_title='A reference catalogue',
  n_ctrl='controls', n_obj='objectives',
  objectives=[('A.2', 'AI policies'), ('A.3', 'Internal organization'), ('A.4', 'Resources'),
              ('A.5', 'Impact assessment'), ('A.6', 'AI system lifecycle'), ('A.7', 'Data'),
              ('A.8', 'Information for interested parties'), ('A.9', 'Use of AI systems'), ('A.10', 'Third parties and customers')],
  soa=['Review all', 'Apply what fits', 'Justify exclusions', 'Statement of Applicability'],
  s4_src='Structure per public third-party catalogues. Verify against the standard.',
  s5_kick='ISO/IEC 27090:2026', s5_title='Threats across the lifecycle',
  phases=['Data and training', 'Development and deployment', 'Operation and integration'],
  threats=[(0, 'Data or model poisoning', 'LLM04'), (1, 'Supply chain', 'LLM03'),
           (2, 'Model inversion and data leakage', 'LLM02'), (2, 'Model theft or extraction', 'ATLAS'),
           (2, 'Indirect prompt injection', 'LLM01'), (2, 'Agents with tools', 'LLM06')],
  s5_stat='12+', s5_stat_l='deliberate attack scenarios, per the ISO27k Forum',
  s5_src='Approximate NullGhost mapping to NIST AI 100-2, OWASP Top 10 for LLM and MITRE ATLAS. Not an official mapping.',
  s6_kick='LEARNING PATH', s6_title='Learn them in four weeks',
  weeks=[('Week 1', 'Map', 'scope and lifecycle'), ('Week 2', 'Threats', 'NIST · OWASP · ATLAS'),
         ('Week 3', 'Controls', 'read the full standard'), ('Week 4', 'Apply', 'one real, bounded system')],
  hours='4 to 6 hours per week · our estimate',
  util_t='Utility of each technique · Dunlosky et al. (2013)',
  util=[('Practice testing', 'high', 1.0), ('Distributed practice', 'high', 1.0), ('Rereading', 'low', .28), ('Highlighting', 'low', .28)],
  rep_t='Each week ends with a closed-book test', rep_l='Repeat on day', days='day',
  s7_kick='EVIDENCE METHOD', s7_title='Four states that never mix',
  states=[('Proposed', 'The plan exists; not yet run.'), ('Observed', 'A response or capture exists, with context.'),
          ('Reproduced', 'A second attempt gets the same effect.'), ('Verified', 'A reviewer confirms the evidence supports it.')],
  bad='“Not vulnerable”', good='“Not observed under these conditions”',
  s7_note='If the instrument fails or times out, the test is inconclusive, not safe.',
  s8_title=['Understand, learn', 'and test with evidence.'],
  guide='Research guide', guide_d='11 pages · in Spanish',
  manual='Good-practice manual', manual_d='10 pages · CSV templates',
  url='nullghost.io/en/ia-normas.html', repo='github.com/nullghost-io/ai-governance-evidence',
  status=f'Working version {VERSION} · Technical review pending · PDFs in Spanish'),
}

CSS = '''@font-face{font-family:Inter;src:url(assets/inter.woff2) format("woff2");font-weight:100 900}
*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;background:#090D14;color:#fff;font-family:Inter,sans-serif}
#main{position:relative;width:1920px;height:1080px;overflow:hidden;background:#090D14}
.clip{position:absolute;inset:0;width:100%;height:100%}
.brand{position:absolute;top:54px;left:112px;width:320px;height:74px;z-index:5}
.category{position:absolute;right:112px;top:80px;font-size:22px;letter-spacing:.14em;color:#a5b6c9;font-weight:600;z-index:5}
.rule{position:absolute;left:112px;right:112px;bottom:92px;height:2px;background:#1c2a3b;z-index:5}
.prog{position:absolute;left:112px;bottom:92px;height:2px;width:1696px;background:#64a3ff;transform-origin:0 50%;z-index:6}
.footer{position:absolute;left:112px;bottom:42px;font-size:22px;color:#7f93aa;z-index:5}
.count{position:absolute;right:112px;bottom:42px;font-size:22px;color:#7f93aa;font-weight:600;letter-spacing:.08em}
.count b{color:#fff}
.in{position:absolute;inset:0}
.kick{position:absolute;left:112px;top:178px;font-size:24px;letter-spacing:.14em;color:#64a3ff;font-weight:700}
.h{position:absolute;left:112px;top:220px;font-size:66px;line-height:1.05;letter-spacing:-.045em;font-weight:800;margin:0}
.muted{color:#a5b6c9}.acc{color:#64a3ff}
.ribbon{position:absolute;right:-120px;top:150px;width:1250px;height:auto;opacity:.95;mix-blend-mode:lighten;
 -webkit-mask-image:linear-gradient(90deg,transparent 0,#000 38%),linear-gradient(180deg,transparent 0,#000 18%,#000 80%,transparent 100%);-webkit-mask-composite:source-in;mask-image:linear-gradient(90deg,transparent 0,#000 38%),linear-gradient(180deg,transparent 0,#000 18%,#000 80%,transparent 100%);mask-composite:intersect}
/* s1 */
.s1k{position:absolute;left:112px;top:330px;font-size:26px;letter-spacing:.14em;color:#64a3ff;font-weight:700}
.s1t{position:absolute;left:112px;top:385px;font-size:138px;line-height:.98;letter-spacing:-.06em;font-weight:800;margin:0}
.s1t span{display:block}
.s1s{position:absolute;left:112px;top:700px;font-size:40px;color:#c9d6e4;letter-spacing:-.01em}
.pills{position:absolute;left:112px;top:800px;display:flex;gap:18px}
.pill{font-size:28px;font-weight:700;padding:14px 26px;border:2px solid #1557a6;border-radius:999px;background:#0e1828}
/* s2 */
.card{position:absolute;top:360px;width:560px;height:440px;padding:36px 38px;border:1px solid #22344a;border-radius:22px;background:#0d1522}
.card .ref{font-size:26px;font-weight:800;color:#64a3ff;letter-spacing:-.01em}
.card h3{font-size:42px;line-height:1.08;letter-spacing:-.03em;margin:16px 0 18px;font-weight:800}
.card p{font-size:28px;line-height:1.35;color:#b8c7d8;margin:0}
.card .tag{position:absolute;left:38px;bottom:34px;font-size:22px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#fff;background:#1557a6;padding:9px 16px;border-radius:8px}
.node{position:absolute;left:800px;top:420px;width:320px;height:320px;border-radius:50%;border:3px solid #1557a6;background:radial-gradient(circle at 50% 40%,#12294d 0,#0b1320 70%);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.node img{width:118px;height:auto;margin-bottom:12px}
.node b{font-size:32px;letter-spacing:-.02em;line-height:1.1;max-width:240px}
.chips{position:absolute;left:0;width:1920px;top:838px;display:flex;justify-content:center;gap:12px}
.chip{font-size:23px;color:#c9d6e4;border:1px solid #2a4060;border-radius:999px;padding:8px 18px;background:#0d1522}
.note{position:absolute;left:112px;right:112px;top:910px;font-size:29px;color:#dfe8f2;text-align:center}
svg.over{position:absolute;left:0;top:0;width:1920px;height:1080px;overflow:visible}
/* s3 */
.ringc{position:absolute;left:330px;top:500px;width:380px;text-align:center}
.ringc b{display:block;font-size:44px;letter-spacing:-.03em}
.ringc span{font-size:30px;color:#a5b6c9}
.clist{position:absolute;left:1010px;top:335px;width:800px}
.crow{display:grid;grid-template-columns:70px 250px 1fr;align-items:baseline;height:60px;border-bottom:1px solid #1c2a3b;font-size:28px}
.crow .n{font-weight:800;color:#64a3ff;font-size:30px}.crow .t{font-weight:700}.crow .d{color:#a5b6c9;font-size:25px}
.impact{position:absolute;left:1010px;top:785px;width:798px;padding:22px 28px;border-left:5px solid #64a3ff;background:#0f1d33;border-radius:0 14px 14px 0}
.impact .k{font-size:21px;letter-spacing:.12em;color:#64a3ff;font-weight:800}
.impact p{font-size:26px;line-height:1.33;margin:8px 0 0}
/* s4 */
.big{position:absolute;left:112px;top:340px;width:520px}
.big .num{font-size:250px;font-weight:800;letter-spacing:-.07em;line-height:.9;color:#fff}
.big .lab{font-size:42px;font-weight:700;color:#64a3ff;margin-top:6px}
.big .num2{font-size:110px;font-weight:800;letter-spacing:-.05em;line-height:1;margin-top:34px}
.big .lab2{font-size:36px;color:#a5b6c9}
.grid{position:absolute;left:700px;top:330px;width:1108px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.tile{height:128px;border:1px solid #22344a;border-radius:16px;background:#0d1522;padding:20px 24px;position:relative;overflow:hidden}
.tile .id{font-size:26px;font-weight:800;color:#64a3ff}.tile .nm{font-size:26px;font-weight:600;line-height:1.2;margin-top:8px}
.tile .bar{position:absolute;left:0;bottom:0;height:5px;width:100%;background:#1557a6;transform-origin:0 50%}
.soa{position:absolute;left:700px;top:790px;width:1108px;display:flex;gap:10px}
.soa div{flex:1;font-size:23px;font-weight:700;padding:16px 18px;background:#12294d;clip-path:polygon(0 0,calc(100% - 20px) 0,100% 50%,calc(100% - 20px) 100%,0 100%,20px 50%);padding-left:34px}
.soa div:first-child{clip-path:polygon(0 0,calc(100% - 20px) 0,100% 50%,calc(100% - 20px) 100%,0 100%);padding-left:22px}
.soa div:last-child{background:#1557a6}
.src{position:absolute;left:112px;right:112px;top:905px;font-size:22px;color:#7f93aa}
/* s5 */
.axis{position:absolute;left:112px;width:1250px;top:820px;height:3px;background:#2a4060}
.phase{position:absolute;top:840px;width:400px;text-align:center;font-size:26px;font-weight:700;color:#c9d6e4}
.col{position:absolute;bottom:262px;width:400px;display:flex;flex-direction:column-reverse;gap:12px}
.thr{height:86px;border-radius:12px;background:#1557a6;padding:12px 18px;display:flex;flex-direction:column;justify-content:center}
.thr .nm{font-size:24px;font-weight:700;line-height:1.15}.thr .rf{font-size:19px;font-weight:700;color:#bcd6ff;letter-spacing:.06em;margin-top:4px}
.thr.op{background:#12294d;border:1px solid #2c4f86}
.stat{position:absolute;left:1440px;top:420px;width:370px}
.stat .v{font-size:150px;font-weight:800;letter-spacing:-.06em;line-height:1}
.stat .l{font-size:29px;line-height:1.3;color:#c9d6e4;margin-top:10px}
/* s6 */
.gantt{position:absolute;left:112px;top:330px;width:1696px;height:240px}
.wk{position:absolute;top:0;width:410px;height:42px;font-size:22px;font-weight:700;color:#7f93aa;letter-spacing:.06em;text-transform:uppercase}
.gb{position:absolute;top:44px;height:118px;border-radius:14px;padding:16px 22px;background:#12294d;transform-origin:0 50%}
.gb b{display:block;font-size:34px;letter-spacing:-.02em}.gb span{font-size:23px;color:#c9d6e4}
.gb.pay{background:#1557a6}
.hours{position:absolute;left:112px;top:525px;font-size:24px;color:#a5b6c9}
.util{position:absolute;left:112px;top:600px;width:900px}
.util h4,.rep h4{font-size:24px;font-weight:700;color:#64a3ff;margin:0 0 16px;letter-spacing:.02em}
.ur{display:grid;grid-template-columns:330px 1fr;align-items:center;height:56px;font-size:26px}
.ut{height:30px;background:#141f2e;border-radius:6px;position:relative;overflow:hidden}
.uf{position:absolute;left:0;top:0;bottom:0;background:#64a3ff;border-radius:6px;transform-origin:0 50%;display:flex;align-items:center;justify-content:flex-end;padding-right:12px;font-size:19px;font-weight:800;color:#06101e;text-transform:uppercase;letter-spacing:.06em}
.uf.low{background:#3a4c63;color:#dfe8f2;justify-content:flex-start;padding-left:12px}
.rep{position:absolute;left:1110px;top:600px;width:698px}
.rep .ax{position:absolute;left:20px;right:20px;top:130px;height:3px;background:#2a4060}
.dot{position:absolute;top:110px;width:44px;height:44px;margin-left:-22px;border-radius:50%;background:#64a3ff;border:5px solid #090D14}
.dot.t0{background:#fff}
.dl{position:absolute;top:168px;width:120px;margin-left:-60px;text-align:center;font-size:23px;color:#c9d6e4;font-weight:600}
.rep p{font-size:26px;margin:0;color:#dfe8f2}
/* s7 */
.track{position:absolute;left:310px;width:1300px;top:448px;height:6px;background:#1c2a3b;border-radius:3px}
.fill{position:absolute;left:310px;width:1300px;top:448px;height:6px;background:#64a3ff;border-radius:3px;transform-origin:0 50%}
.st{position:absolute;top:410px;width:400px;margin-left:-200px;text-align:center}
.st .c{width:82px;height:82px;margin:0 auto;border-radius:50%;background:#0d1522;border:4px solid #2a4060;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:800}
.st .c.on{background:#1557a6;border-color:#64a3ff}
.st b{display:block;font-size:34px;margin-top:20px;letter-spacing:-.02em}.st span{display:block;font-size:24px;color:#a5b6c9;line-height:1.3;margin-top:8px}
.vs{position:absolute;left:112px;right:112px;top:735px;display:grid;grid-template-columns:1fr 1fr;gap:28px}
.q{padding:22px 30px;border-radius:16px;font-size:34px;font-weight:700;display:flex;align-items:center;gap:20px}
.q i{font-style:normal;width:46px;height:46px;flex:0 0 46px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:28px}
.q.bad{background:#1a1216;border:1px solid #5a2a35;color:#e6b3bd}.q.bad i{background:#5a2a35;color:#fff}
.q.good{background:#0f1d33;border:1px solid #2c4f86}.q.good i{background:#1557a6;color:#fff}
.s7n{position:absolute;left:112px;right:112px;top:868px;font-size:27px;color:#c9d6e4}
/* s8 */
.covers{position:absolute;left:112px;top:240px;display:flex;gap:34px}
.doc img{width:420px;height:594px;display:block;border-radius:6px;box-shadow:0 30px 70px #000a;border:1px solid #22344a}
.doc b{display:block;font-size:27px;margin-top:20px}.doc span{font-size:23px;color:#a5b6c9}
.s8r{position:absolute;left:1060px;top:300px;width:760px}
.s8r h2{font-size:78px;line-height:1.04;letter-spacing:-.05em;font-weight:800;margin:0}
.s8r h2 span{display:block}
.url{font-size:36px;font-weight:800;color:#64a3ff;margin-top:44px}
.repo{font-size:25px;color:#c9d6e4;margin-top:14px}
.status{font-size:23px;color:#a5b6c9;margin-top:34px;line-height:1.5}
'''


def arc(cx, cy, r, a0, a1):
    def p(a):
        t = math.radians(a - 90)
        return cx + r * math.cos(t), cy + r * math.sin(t)
    x0, y0 = p(a0)
    x1, y1 = p(a1)
    large = 1 if a1 - a0 > 180 else 0
    return f'M{x0:.1f} {y0:.1f} A{r} {r} 0 {large} 1 {x1:.1f} {y1:.1f}'


def build(lang, c):
    S = {k: (s, d) for k, s, d in SCENES}
    n = len(SCENES)

    def sec(k, body, idx):
        s, d = S[k]
        return (f'<section id="{k}" class="clip" data-start="{s}" data-duration="{d}" data-track-index="1">'
                f'<div class="in" id="{k}i">{body}</div><div class="count"><b>{idx:02d}</b> / {n:02d}</div></section>')

    # s1
    s1 = (f'<img class="ribbon" id="rb1" src="assets/ribbon.jpg" alt="">'
          f'<div class="s1k" id="s1k">{E(c["s1_kick"])}</div>'
          f'<h1 class="s1t" id="s1t">' + ''.join(f'<span>{E(t)}</span>' for t in c['s1_title']) + '</h1>'
          f'<div class="s1s" id="s1s">{E(c["s1_sub"])}</div>'
          '<div class="pills"><div class="pill" id="p1">ISO/IEC 42001:2023</div><div class="pill" id="p2">ISO/IEC 27090:2026</div></div>')
    # s2
    s2 = (f'<div class="h" id="s2h">{E(c["s2_title"])}</div>'
          '<svg class="over" viewBox="0 0 1920 1080">'
          '<path id="l1" d="M672 580 L800 580" stroke="#64a3ff" stroke-width="3" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
          '<path id="l2" d="M1248 580 L1120 580" stroke="#64a3ff" stroke-width="3" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
          '<circle id="d1" cx="672" cy="580" r="8" fill="#64a3ff" opacity="0"/><circle id="d2" cx="1248" cy="580" r="8" fill="#64a3ff" opacity="0"/></svg>'
          f'<div class="card" id="ca" style="left:112px"><div class="ref">ISO/IEC 42001:2023</div><h3>{E(c["a_name"])}</h3><p>{E(c["a_q"])}</p><div class="tag">{E(c["a_tag"])}</div></div>'
          f'<div class="card" id="cb" style="left:1248px"><div class="ref">ISO/IEC 27090:2026</div><h3>{E(c["b_name"])}</h3><p>{E(c["b_q"])}</p><div class="tag">{E(c["b_tag"])}</div></div>'
          f'<div class="node" id="nd"><img src="assets/ghost.svg" alt=""><b>{E(c["node"])}</b></div>'
          '<div class="chips">' + ''.join(f'<div class="chip">{E(a)}</div>' for a in c['assets']) + '</div>'
          f'<div class="note" id="s2n">{E(c["s2_note"])}</div>')
    # s3: anillo de 7 segmentos
    cx, cy, r, gap = 520, 590, 230, 4
    span = 360 / 7
    segs, labels = [], []
    for i, (num, _, _) in enumerate(c['clauses']):
        a0, a1 = i * span + gap / 2, (i + 1) * span - gap / 2
        col = '#64a3ff' if num == '6' else '#1557a6'
        segs.append(f'<path id="sg{i}" class="seg" d="{arc(cx, cy, r, a0, a1)}" stroke="{col}" stroke-width="70" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>')
        t = math.radians((a0 + a1) / 2 - 90)
        lx, ly = cx + r * math.cos(t), cy + r * math.sin(t)
        labels.append(f'<text id="sl{i}" class="sl" x="{lx:.1f}" y="{ly + 12:.1f}" text-anchor="middle" font-size="34" font-weight="800" fill="#fff" opacity="0">{num}</text>')
    s3 = (f'<div class="kick">{E(c["s3_kick"])}</div><div class="h" id="s3h">{E(c["s3_title"])}</div>'
          f'<svg class="over" viewBox="0 0 1920 1080"><circle cx="{cx}" cy="{cy}" r="{r}" stroke="#121c2a" stroke-width="70" fill="none"/>'
          + ''.join(segs) + ''.join(labels) + '</svg>'
          f'<div class="ringc" id="rc"><b>{E(c["ring_c"])}</b><span>{E(c["ring_s"])}</span></div>'
          '<div class="clist">' + ''.join(f'<div class="crow"><span class="n">{E(a)}</span><span class="t">{E(b)}</span><span class="d">{E(d)}</span></div>' for a, b, d in c['clauses']) + '</div>'
          f'<div class="impact" id="imp"><div class="k">{E(c["impact_k"])}</div><p>{E(c["impact"])}</p></div>')
    # s4
    s4 = (f'<div class="kick">{E(c["s4_kick"])}</div><div class="h" id="s4h">{E(c["s4_title"])}</div>'
          f'<div class="big"><div class="num" id="n38">0</div><div class="lab">{E(c["n_ctrl"])}</div>'
          f'<div class="num2" id="n9">0</div><div class="lab2">{E(c["n_obj"])}</div></div>'
          '<div class="grid">' + ''.join(f'<div class="tile"><div class="id">{E(a)}</div><div class="nm">{E(b)}</div><div class="bar"></div></div>' for a, b in c['objectives']) + '</div>'
          '<div class="soa">' + ''.join(f'<div>{E(x)}</div>' for x in c['soa']) + '</div>'
          f'<div class="src">{E(c["s4_src"])}</div>')
    # s5: columnas apiladas por fase
    cols = ''
    for pi, ph in enumerate(c['phases']):
        x = 112 + pi * 425
        items = [t for t in c['threats'] if t[0] == pi]
        cols += f'<div class="col" style="left:{x}px">' + ''.join(
            f'<div class="thr{" op" if pi == 2 else ""}"><div class="nm">{E(nm)}</div><div class="rf">{E(rf)}</div></div>' for _, nm, rf in items) + '</div>'
        cols += f'<div class="phase" style="left:{x}px">{E(ph)}</div>'
    s5 = (f'<div class="kick">{E(c["s5_kick"])}</div><div class="h" id="s5h">{E(c["s5_title"])}</div>'
          f'<div class="axis" id="ax"></div>{cols}'
          f'<div class="stat" id="st5"><div class="v">{E(c["s5_stat"])}</div><div class="l">{E(c["s5_stat_l"])}</div></div>'
          f'<div class="src" style="top:910px">{E(c["s5_src"])}</div>')
    # s6
    g = ''
    for i, (w, t, d) in enumerate(c['weeks']):
        x = i * 428
        g += f'<div class="wk" style="left:{x}px">{E(w)}</div><div class="gb{" pay" if i == 2 else ""}" style="left:{x}px;width:410px"><b>{E(t)}</b><span>{E(d)}</span></div>'
    u = ''.join(f'<div class="ur"><span>{E(nm)}</span><div class="ut"><div class="uf{" low" if v < 1 else ""}" style="width:{v * 100:.0f}%">{E(lv)}</div></div></div>' for nm, lv, v in c['util'])
    dots = ''
    for i, dday in enumerate([0, 1, 3, 7]):
        x = 20 + dday / 7 * 658
        lab = ('0' if lang == 'en' else '0') if dday == 0 else str(dday)
        dots += f'<div class="dot{" t0" if dday == 0 else ""}" style="left:{x:.0f}px"></div><div class="dl" style="left:{x:.0f}px">{E(c["days"])} {lab}</div>'
    s6 = (f'<div class="kick">{E(c["s6_kick"])}</div><div class="h" id="s6h">{E(c["s6_title"])}</div>'
          f'<div class="gantt">{g}</div><div class="hours" id="hrs">{E(c["hours"])}</div>'
          f'<div class="util" id="ut"><h4>{E(c["util_t"])}</h4>{u}</div>'
          f'<div class="rep" id="rp"><h4>{E(c["rep_t"])}</h4><p>{E(c["rep_l"])} 1 · 3 · 7</p><div class="ax"></div>{dots}</div>')
    # s7
    st = ''
    for i, (nm, d) in enumerate(c['states']):
        x = 310 + i * (1300 / 3)
        st += f'<div class="st" id="st{i}" style="left:{x:.0f}px"><div class="c">{i + 1}</div><b>{E(nm)}</b><span>{E(d)}</span></div>'
    s7 = (f'<div class="kick">{E(c["s7_kick"])}</div><div class="h" id="s7h">{E(c["s7_title"])}</div>'
          f'<div class="track"></div><div class="fill" id="fl"></div>{st}'
          f'<div class="vs"><div class="q bad" id="qb"><i>✕</i>{E(c["bad"])}</div><div class="q good" id="qg"><i>✓</i>{E(c["good"])}</div></div>'
          f'<div class="s7n" id="s7n">{E(c["s7_note"])}</div>')
    # s8
    s8 = (f'<div class="covers"><div class="doc" id="dg"><img src="assets/guide.png" alt="{E(c["guide"])}"><b>{E(c["guide"])}</b><span>{E(c["guide_d"])}</span></div>'
          f'<div class="doc" id="dm"><img src="assets/manual.png" alt="{E(c["manual"])}"><b>{E(c["manual"])}</b><span>{E(c["manual_d"])}</span></div></div>'
          '<div class="s8r"><h2 id="s8t">' + ''.join(f'<span>{E(t)}</span>' for t in c['s8_title']) + '</h2>'
          f'<div class="url" id="u8">{E(c["url"])}</div><div class="repo" id="r8">{E(c["repo"])}</div>'
          f'<div class="status" id="z8">{E(c["status"])}</div></div>')

    bodies = [s1, s2, s3, s4, s5, s6, s7, s8]
    sections = ''.join(sec(k, b, i + 1) for i, ((k, _, _), b) in enumerate(zip(SCENES, bodies)))

    st_ = {k: s for k, s, _ in SCENES}
    end = {k: s + d for k, s, d in SCENES}
    js = ['window.__timelines=window.__timelines||{};const tl=gsap.timeline({paused:true});',
          "const U=(sel,t,o)=>tl.fromTo(sel,{opacity:0,y:o||26},{opacity:1,y:0,duration:.6,ease:'power3.out'},t);",
          "const ST=(sel,t,s)=>tl.fromTo(sel,{opacity:0,y:22},{opacity:1,y:0,duration:.5,ease:'power3.out',stagger:s||.1},t);",
          f"tl.fromTo('#prog',{{scaleX:0}},{{scaleX:1,duration:{DUR},ease:'none'}},0);"]
    # salida de cada escena (salvo la última)
    for k, s, d in SCENES[:-1]:
        js.append(f"tl.to('#{k}i',{{opacity:0,duration:.35,ease:'power2.in'}},{s + d - .35});")
    a = st_['s1']
    js += [f"tl.fromTo('#rb1',{{opacity:0,x:60}},{{opacity:.95,x:0,duration:1.4,ease:'power2.out'}},{a});",
           f"tl.to('#rb1',{{x:-30,duration:4,ease:'none'}},{a + 1.4});",
           f"U('#s1k',{a + .2});ST('#s1t span',{a + .4},.14);U('#s1s',{a + 1.4});ST('.pills .pill',{a + 2.2},.25);"]
    a = st_['s2']
    js += [f"U('#s2h',{a + .1});U('#ca',{a + .5},40);U('#cb',{a + .9},40);",
           f"tl.fromTo('#nd',{{opacity:0,scale:.85}},{{opacity:1,scale:1,duration:.7,ease:'back.out(1.6)'}},{a + 1.3});",
           f"tl.to(['#l1','#l2'],{{strokeDashoffset:0,duration:.6,ease:'power2.out'}},{a + 1.9});",
           f"tl.set(['#d1','#d2'],{{opacity:1}},{a + 2.4});",
           f"tl.fromTo('#d1',{{attr:{{cx:672}}}},{{attr:{{cx:800}},duration:1,repeat:3,ease:'power1.inOut'}},{a + 2.4});",
           f"tl.fromTo('#d2',{{attr:{{cx:1248}}}},{{attr:{{cx:1120}},duration:1,repeat:3,ease:'power1.inOut'}},{a + 2.4});",
           f"ST('#s2 .chip',{a + 2.6},.08);U('#s2n',{a + 3.6});"]
    a = st_['s3']
    js += [f"U('#s3 .kick',{a});U('#s3h',{a + .15});U('#rc',{a + .5},10);"]
    for i in range(7):
        t = a + .8 + i * .55
        js.append(f"tl.to('#sg{i}',{{strokeDashoffset:0,duration:.5,ease:'power2.out'}},{t:.2f});")
        js.append(f"tl.to('#sl{i}',{{opacity:1,duration:.3}},{t + .25:.2f});")
        js.append(f"tl.fromTo('#s3 .crow:nth-child({i + 1})',{{opacity:0,x:30}},{{opacity:1,x:0,duration:.45,ease:'power3.out'}},{t:.2f});")
    js += [f"tl.to('#s3 .crow:nth-child(3)',{{backgroundColor:'#12294d',duration:.4}},{a + 5.0});",
           f"U('#imp',{a + 5.2});"]
    a = st_['s4']
    js += [f"U('#s4 .kick',{a});U('#s4h',{a + .15});U('.big',{a + .3});",
           f"tl.fromTo('#n38',{{innerText:0}},{{innerText:38,snap:{{innerText:1}},duration:1.6,ease:'power2.out'}},{a + .5});",
           f"tl.fromTo('#n9',{{innerText:0}},{{innerText:9,snap:{{innerText:1}},duration:1.2,ease:'power2.out'}},{a + 1.2});",
           f"ST('#s4 .tile',{a + .9},.13);",
           f"tl.fromTo('#s4 .tile .bar',{{scaleX:0}},{{scaleX:1,duration:.5,stagger:.13,ease:'power2.out'}},{a + 1.3});",
           f"tl.fromTo('#s4 .soa div',{{opacity:0,x:-20}},{{opacity:1,x:0,duration:.45,stagger:.3,ease:'power3.out'}},{a + 3.2});",
           f"U('#s4 .src',{a + 4.4},10);"]
    a = st_['s5']
    js += [f"U('#s5 .kick',{a});U('#s5h',{a + .15});",
           f"tl.fromTo('#ax',{{scaleX:0,transformOrigin:'0 50%'}},{{scaleX:1,duration:.7,ease:'power2.out'}},{a + .4});",
           f"ST('#s5 .phase',{a + .7},.15);",
           f"tl.fromTo('#s5 .thr',{{opacity:0,y:-60}},{{opacity:1,y:0,duration:.5,ease:'bounce.out',stagger:.38}},{a + 1.3});",
           f"U('#st5',{a + 4.0});U('#s5 .src',{a + 4.8},10);"]
    a = st_['s6']
    js += [f"U('#s6 .kick',{a});U('#s6h',{a + .15});ST('#s6 .wk',{a + .4},.15);",
           f"tl.fromTo('#s6 .gb',{{opacity:0,scaleX:.2}},{{opacity:1,scaleX:1,duration:.55,stagger:.25,ease:'power3.out'}},{a + .5});",
           f"U('#hrs',{a + 1.8},10);U('#ut h4',{a + 2.2},10);",
           f"ST('#ut .ur',{a + 2.4},.15);",
           f"tl.fromTo('#ut .uf',{{scaleX:0}},{{scaleX:1,duration:.7,stagger:.18,ease:'power2.out'}},{a + 2.6});",
           f"U('#rp h4',{a + 3.6},10);U('#rp p',{a + 3.8},10);",
           f"tl.fromTo('#rp .ax',{{scaleX:0,transformOrigin:'0 50%'}},{{scaleX:1,duration:.8,ease:'power2.out'}},{a + 4.0});",
           f"tl.fromTo('#rp .dot',{{scale:0}},{{scale:1,duration:.35,stagger:.3,ease:'back.out(2)'}},{a + 4.2});",
           f"ST('#rp .dl',{a + 4.3},.3);"]
    a = st_['s7']
    js += [f"U('#s7 .kick',{a});U('#s7h',{a + .15});",
           f"tl.fromTo('#fl',{{scaleX:0}},{{scaleX:1,duration:2.4,ease:'none'}},{a + .7});"]
    for i in range(4):
        t = a + .6 + i * .8
        js.append(f"tl.fromTo('#st{i}',{{opacity:0,y:20}},{{opacity:1,y:0,duration:.45,ease:'power3.out'}},{t:.2f});")
        js.append(f"tl.to('#st{i} .c',{{backgroundColor:'#1557a6',borderColor:'#64a3ff',duration:.3}},{t + .2:.2f});")
    js += [f"U('#qb',{a + 3.5},16);U('#qg',{a + 3.9},16);U('#s7n',{a + 4.5},10);"]
    a = st_['s8']
    js += [f"U('#dg',{a + .2},40);U('#dm',{a + .5},40);ST('#s8t span',{a + .6},.15);",
           f"U('#u8',{a + 1.5},12);U('#r8',{a + 1.8},12);U('#z8',{a + 2.2},10);",
           "window.__timelines['main']=tl;"]

    html = (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=1920,height=1080">'
            f'<title>NullGhost · ISO AI · {lang}</title><script src="assets/vendor/gsap.min.js"></script><style>{CSS}</style></head><body>'
            f'<div id="main" data-composition-id="main" data-width="1920" data-height="1080" data-duration="{DUR}">'
            f'<img class="brand" src="assets/logo.svg" alt="NullGhost"><div class="category">{E(c["category"])}</div>'
            f'<div class="rule"></div><div class="prog" id="prog"></div><div class="footer">{E(c["footer"])}</div>'
            f'{sections}</div><script>' + '\n'.join(js) + '</script></body></html>')
    return html


for lang, c in COPY.items():
    html = build(lang, c)
    target = R / ('index.html' if lang == 'es' else 'compositions/en.html')
    if lang == 'en':
        html = html.replace('assets/', '../assets/')
    target.write_text(html)
print('ES/EN compositions built')
