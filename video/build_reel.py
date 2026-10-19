"""Reel vertical (1080x1920) de la guía y el manual de IA v0.4 para Instagram.

Mismo contenido que el video web, condensado. Texto dentro de la zona segura de
Reels (sin nada clave arriba de y=250 ni abajo de y=1560). Sin audio: la música
se agrega en Instagram. Salida: compositions/reel-es.html.
"""
import math
from pathlib import Path
from html import escape as E

R = Path(__file__).resolve().parent
DUR = 31
SCENES = [('r1', 0, 3), ('r2', 3, 4.5), ('r3', 7.5, 4.5), ('r4', 12, 3.5),
          ('r5', 15.5, 4.5), ('r6', 20, 4), ('r7', 24, 3), ('r8', 27, 4)]

CSS = '''@font-face{font-family:Inter;src:url(../assets/inter.woff2) format("woff2");font-weight:100 900}
*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;background:#090D14;color:#fff;font-family:Inter,sans-serif}
#main{position:relative;width:1080px;height:1920px;overflow:hidden;background:#090D14}
.clip{position:absolute;inset:0;width:100%;height:100%}.in{position:absolute;inset:0}
.brand{position:absolute;top:150px;left:80px;width:250px;height:58px;z-index:5}
.kick{position:absolute;left:80px;top:290px;font-size:30px;letter-spacing:.12em;color:#64a3ff;font-weight:800}
.h{position:absolute;left:80px;right:80px;top:340px;font-size:72px;line-height:1.03;letter-spacing:-.045em;font-weight:800;margin:0}
.src{position:absolute;left:80px;right:80px;font-size:26px;line-height:1.3;color:#8ea2b9}
.ribbon{position:absolute;right:-380px;top:980px;width:1500px;height:auto;mix-blend-mode:lighten;opacity:.95;
 -webkit-mask-image:linear-gradient(180deg,transparent 0,#000 25%,#000 75%,transparent 100%);mask-image:linear-gradient(180deg,transparent 0,#000 25%,#000 75%,transparent 100%)}
/* r1 */
.t1{position:absolute;left:80px;top:420px;font-size:150px;line-height:.95;letter-spacing:-.065em;font-weight:800;margin:0}
.t1 span{display:block}
.s1{position:absolute;left:80px;right:80px;top:930px;font-size:46px;line-height:1.22;color:#dfe8f2;font-weight:600;letter-spacing:-.02em}
.pills{position:absolute;left:80px;top:1110px;display:flex;flex-direction:column;gap:18px}
.pill{font-size:36px;font-weight:800;padding:16px 30px;border:3px solid #1557a6;border-radius:999px;background:#0e1828;align-self:flex-start}
/* r2 */
.card{position:absolute;left:80px;right:80px;height:330px;padding:34px 38px;border:1px solid #22344a;border-radius:26px;background:#0d1522}
.card .ref{font-size:30px;font-weight:800;color:#64a3ff}
.card h3{font-size:50px;line-height:1.05;letter-spacing:-.035em;margin:12px 0 14px;font-weight:800}
.card p{font-size:32px;line-height:1.3;color:#c3d0de;margin:0}
.node{position:absolute;left:400px;top:760px;width:280px;height:280px;border-radius:50%;border:4px solid #1557a6;background:radial-gradient(circle at 50% 40%,#12294d 0,#0b1320 70%);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.node img{width:110px;margin-bottom:10px}.node b{font-size:34px;line-height:1.1;max-width:220px;letter-spacing:-.02em}
svg.over{position:absolute;left:0;top:0;width:1080px;height:1920px}
/* r3 */
.ringc{position:absolute;left:340px;top:690px;width:400px;text-align:center}
.ringc b{display:block;font-size:46px;letter-spacing:-.03em}.ringc span{font-size:32px;color:#a5b6c9}
.legend{position:absolute;left:80px;right:80px;top:1080px;display:grid;grid-template-columns:1fr 1fr;column-gap:30px;row-gap:12px}
.legend div{font-size:32px;font-weight:700}.legend b{color:#64a3ff;display:inline-block;width:56px}
.legend .hi{color:#9cc4ff}
.impact{position:absolute;left:80px;right:80px;top:1310px;padding:24px 30px;border-left:6px solid #64a3ff;background:#0f1d33;border-radius:0 18px 18px 0}
.impact .k{font-size:26px;letter-spacing:.1em;color:#64a3ff;font-weight:800}.impact p{font-size:34px;line-height:1.28;margin:8px 0 0;font-weight:600}
/* r4 */
.nums{position:absolute;left:80px;top:500px;display:flex;gap:70px;align-items:flex-end}
.nums .v{font-size:250px;font-weight:800;letter-spacing:-.07em;line-height:.85}.nums .l{font-size:44px;font-weight:700;color:#64a3ff;margin-top:12px}
.nums .v2{font-size:160px}
.grid{position:absolute;left:80px;right:80px;top:880px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.tile{height:150px;border:1px solid #22344a;border-radius:18px;background:#0d1522;padding:18px 20px;position:relative;overflow:hidden}
.tile .id{font-size:30px;font-weight:800;color:#64a3ff}.tile .nm{font-size:27px;font-weight:600;line-height:1.15;margin-top:6px}
.tile .bar{position:absolute;left:0;bottom:0;height:6px;width:100%;background:#1557a6;transform-origin:0 50%}
/* r5 */
.ph{position:absolute;left:80px;right:80px}
.ph .pn{font-size:30px;font-weight:800;color:#a5b6c9;letter-spacing:.04em;text-transform:uppercase;margin-bottom:14px;padding-bottom:10px;border-bottom:2px solid #2a4060}
.ph .row{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.thr{border-radius:16px;background:#1557a6;padding:16px 20px;min-height:116px;display:flex;flex-direction:column;justify-content:center}
.thr .nm{font-size:31px;font-weight:700;line-height:1.12}.thr .rf{font-size:24px;font-weight:800;color:#bcd6ff;letter-spacing:.06em;margin-top:6px}
.thr.op{background:#12294d;border:1px solid #2c4f86}
.stat{position:absolute;left:80px;right:80px;top:1360px;display:flex;gap:24px;align-items:center}
.stat .v{font-size:110px;font-weight:800;letter-spacing:-.06em;line-height:1}.stat .l{font-size:32px;line-height:1.25;color:#dfe8f2}
/* r6 */
.wk{position:absolute;left:80px;right:80px;height:120px;border-radius:18px;background:#12294d;padding:18px 26px;display:grid;grid-template-columns:200px 1fr;align-items:center;transform-origin:0 50%}
.wk .w{font-size:28px;font-weight:800;color:#9cc4ff;text-transform:uppercase;letter-spacing:.05em}
.wk b{display:block;font-size:42px;letter-spacing:-.02em}.wk span{font-size:28px;color:#c9d6e4}
.wk.pay{background:#1557a6}
.util{position:absolute;left:80px;right:80px;top:1130px}
.util h4{font-size:29px;color:#64a3ff;margin:0 0 18px;font-weight:800}
.ur{display:grid;grid-template-columns:420px 1fr;align-items:center;height:68px;font-size:33px;font-weight:600}
.ut{height:40px;background:#141f2e;border-radius:8px;position:relative;overflow:hidden}
.uf{position:absolute;left:0;top:0;bottom:0;background:#64a3ff;border-radius:8px;transform-origin:0 50%;display:flex;align-items:center;justify-content:flex-end;padding-right:14px;font-size:22px;font-weight:800;color:#06101e;text-transform:uppercase;letter-spacing:.06em}
.uf.low{background:#3a4c63;color:#dfe8f2;justify-content:flex-start;padding-left:12px}
/* r7 */
.vline{position:absolute;left:131px;top:602px;width:6px;height:516px;background:#1c2a3b;border-radius:3px}
.vfill{position:absolute;left:131px;top:602px;width:6px;height:516px;background:#64a3ff;border-radius:3px;transform-origin:50% 0}
.st{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:108px 1fr;align-items:center}
.st .c{width:108px;height:108px;border-radius:50%;background:#0d1522;border:5px solid #2a4060;display:flex;align-items:center;justify-content:center;font-size:42px;font-weight:800}
.st b{display:block;font-size:46px;letter-spacing:-.02em;padding-left:30px}.st span{display:block;font-size:29px;color:#b8c7d8;padding-left:30px;margin-top:4px}
.q{position:absolute;left:80px;right:80px;padding:22px 28px;border-radius:18px;font-size:38px;font-weight:700;display:flex;align-items:center;gap:22px}
.q i{font-style:normal;width:56px;height:56px;flex:0 0 56px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:32px}
.q.bad{background:#1a1216;border:1px solid #5a2a35;color:#e6b3bd}.q.bad i{background:#5a2a35;color:#fff}
.q.good{background:#0f1d33;border:1px solid #2c4f86}.q.good i{background:#1557a6;color:#fff}
/* r8 */
.covers{position:absolute;left:80px;right:80px;top:300px;display:flex;gap:30px;justify-content:center}
.covers img{width:445px;height:629px;border-radius:8px;box-shadow:0 30px 70px #000b;border:1px solid #22344a;display:block}
.t8{position:absolute;left:80px;right:80px;top:1000px;font-size:84px;line-height:1.02;letter-spacing:-.05em;font-weight:800;margin:0}
.t8 span{display:block}
.url{position:absolute;left:80px;right:80px;top:1215px;font-size:44px;font-weight:800;color:#64a3ff}
.meta{position:absolute;left:80px;right:80px;top:1290px;font-size:30px;line-height:1.4;color:#c9d6e4}
.disc{position:absolute;left:80px;right:80px;top:1440px;font-size:26px;color:#8ea2b9}
'''


def arc(cx, cy, r, a0, a1):
    def p(a):
        t = math.radians(a - 90)
        return cx + r * math.cos(t), cy + r * math.sin(t)
    x0, y0 = p(a0); x1, y1 = p(a1)
    return f'M{x0:.1f} {y0:.1f} A{r} {r} 0 {1 if a1 - a0 > 180 else 0} 1 {x1:.1f} {y1:.1f}'


def build():
    sec = lambda k, s, d, body: f'<section id="{k}" class="clip" data-start="{s}" data-duration="{d}" data-track-index="1"><div class="in" id="{k}i">{body}</div></section>'
    b = {}
    b['r1'] = ('<img class="ribbon" id="rb" src="../assets/ribbon.jpg" alt="">'
               '<div class="kick" id="k1">ISO · INTELIGENCIA ARTIFICIAL</div>'
               '<h1 class="t1" id="t1"><span>Dos normas</span><span>ISO para</span><span>la IA.</span></h1>'
               '<div class="s1" id="s1">Una dice cómo gobernarla. La otra, cómo la atacan.</div>'
               '<div class="pills"><div class="pill">ISO/IEC 42001:2023</div><div class="pill">ISO/IEC 27090:2026</div></div>')
    b['r2'] = ('<svg class="over" viewBox="0 0 1080 1920">'
               '<path id="l1" d="M540 640 L540 760" stroke="#64a3ff" stroke-width="4" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
               '<path id="l2" d="M540 1170 L540 1040" stroke="#64a3ff" stroke-width="4" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
               '<circle id="d1" cx="540" cy="640" r="10" fill="#64a3ff" opacity="0"/><circle id="d2" cx="540" cy="1170" r="10" fill="#64a3ff" opacity="0"/></svg>'
               '<div class="card" id="ca" style="top:310px"><div class="ref">ISO/IEC 42001:2023 · GESTIÓN</div><h3>¿Quién decide y cómo se controla?</h3><p>Sistema de gestión de IA. Requisitos, certificable.</p></div>'
               '<div class="node" id="nd"><img src="../assets/ghost.svg" alt=""><b>Tu sistema de IA</b></div>'
               '<div class="card" id="cb" style="top:1170px"><div class="ref">ISO/IEC 27090:2026 · AMENAZAS</div><h3>¿Cómo se ataca y cómo se mitiga?</h3><p>Guía de orientación sobre amenazas en todo el ciclo de vida.</p></div>')
    cx, cy, r, gap, span = 540, 820, 215, 4, 360 / 7
    nums = ['4', '5', '6', '7', '8', '9', '10']
    names = ['Contexto', 'Liderazgo', 'Planificación', 'Apoyo', 'Operación', 'Evaluación', 'Mejora']
    segs = ''
    for i, n in enumerate(nums):
        a0, a1 = i * span + gap / 2, (i + 1) * span - gap / 2
        t = math.radians((a0 + a1) / 2 - 90)
        segs += (f'<path id="sg{i}" d="{arc(cx, cy, r, a0, a1)}" stroke="{"#64a3ff" if n == "6" else "#1557a6"}" stroke-width="80" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
                 f'<text id="sl{i}" x="{cx + r * math.cos(t):.1f}" y="{cy + r * math.sin(t) + 13:.1f}" text-anchor="middle" font-size="38" font-weight="800" fill="#fff" opacity="0">{n}</text>')
    b['r3'] = ('<div class="kick">ISO/IEC 42001 POR DENTRO</div><div class="h">Siete cláusulas auditables</div>'
               f'<svg class="over" viewBox="0 0 1080 1920"><circle cx="{cx}" cy="{cy}" r="{r}" stroke="#121c2a" stroke-width="80" fill="none"/>{segs}</svg>'
               '<div class="ringc" id="rc"><b>Cláusulas</b><span>4 a 10</span></div>'
               '<div class="legend">' + ''.join(f'<div{" class=\"hi\"" if n == "6" else ""}><b>{n}</b>{E(m)}</div>' for n, m in zip(nums, names)) + '</div>'
               '<div class="impact" id="imp"><div class="k">6.1.4 · LA PIEZA NUEVA</div><p>Evaluación de impacto: efectos sobre personas, grupos y la sociedad.</p></div>')
    objs = [('A.2', 'Políticas de IA'), ('A.3', 'Organización interna'), ('A.4', 'Recursos'), ('A.5', 'Evaluación de impactos'),
            ('A.6', 'Ciclo de vida'), ('A.7', 'Datos'), ('A.8', 'Información a partes'), ('A.9', 'Uso de la IA'), ('A.10', 'Terceros y clientes')]
    b['r4'] = ('<div class="kick">ISO/IEC 42001 · ANEXO A</div><div class="h">Un catálogo de referencia</div>'
               '<div class="nums"><div><div class="v" id="n38">0</div><div class="l">controles</div></div><div><div class="v v2" id="n9">0</div><div class="l">objetivos</div></div></div>'
               '<div class="grid">' + ''.join(f'<div class="tile"><div class="id">{a}</div><div class="nm">{E(n)}</div><div class="bar"></div></div>' for a, n in objs) + '</div>'
               '<div class="src" style="top:1400px">Se revisan todos, se aplican los que corresponden y se justifican las exclusiones. Estructura según fuentes secundarias.</div>')
    phases = [('Datos y entrenamiento', [('Envenenamiento de datos o modelos', 'LLM04')], 525),
              ('Desarrollo y despliegue', [('Cadena de suministro', 'LLM03')], 755),
              ('Operación e integración', [('Inversión de modelos y fuga', 'LLM02'), ('Robo de modelos', 'ATLAS'),
                                           ('Inyección indirecta de prompts', 'LLM01'), ('Agentes con herramientas', 'LLM06')], 975)]
    ph = ''
    for pi, (pn, items, top) in enumerate(phases):
        ph += (f'<div class="ph" id="ph{pi}" style="top:{top}px"><div class="pn">{E(pn)}</div><div class="row">'
               + ''.join(f'<div class="thr{" op" if pi == 2 else ""}"><div class="nm">{E(n)}</div><div class="rf">{rf}</div></div>' for n, rf in items) + '</div></div>')
    b['r5'] = ('<div class="kick">ISO/IEC 27090:2026</div><div class="h">Amenazas en todo el ciclo de vida</div>' + ph +
               '<div class="stat" id="st5"><div class="v">12+</div><div class="l">escenarios de ataque deliberado, según el ISO27k Forum</div></div>'
               '<div class="src" style="top:1490px">Correspondencia aproximada con OWASP y MITRE ATLAS. No es un mapeo oficial.</div>')
    weeks = [('Semana 1', 'Mapa', 'alcance y ciclo de vida'), ('Semana 2', 'Amenazas', 'NIST · OWASP · ATLAS'),
             ('Semana 3', 'Controles', 'leer la norma completa'), ('Semana 4', 'Aplicar', 'un sistema real')]
    util = [('Práctica de recuperación', 'alta', 1), ('Práctica espaciada', 'alta', 1), ('Releer', 'baja', .28), ('Subrayar', 'baja', .28)]
    b['r6'] = ('<div class="kick">CAMINO DE APRENDIZAJE</div><div class="h">Apréndelas en cuatro semanas</div>'
               + ''.join(f'<div class="wk{" pay" if i == 2 else ""}" style="top:{540 + i * 136}px"><div class="w">{w}</div><div><b>{t}</b><span>{d}</span></div></div>' for i, (w, t, d) in enumerate(weeks)) +
               '<div class="util" id="ut"><h4>Qué funciona para estudiar · Dunlosky et al. (2013)</h4>'
               + ''.join(f'<div class="ur"><span>{n}</span><div class="ut"><div class="uf{" low" if v < 1 else ""}" style="width:{v * 100:.0f}%">{lv}</div></div></div>' for n, lv, v in util) + '</div>')
    states = [('Propuesto', 'El plan existe; no se ha ejecutado.'), ('Observado', 'Hay respuesta o captura, con contexto.'),
              ('Reproducido', 'Un segundo intento da el mismo efecto.'), ('Verificado', 'Un revisor confirma la evidencia.')]
    b['r7'] = ('<div class="kick">MÉTODO DE EVIDENCIA</div><div class="h">Cuatro estados que no se mezclan</div>'
               '<div class="vline"></div><div class="vfill" id="vf"></div>'
               + ''.join(f'<div class="st" id="st{i}" style="top:{548 + i * 172}px"><div class="c">{i + 1}</div><div><b>{n}</b><span>{d}</span></div></div>' for i, (n, d) in enumerate(states)) +
               '<div class="q bad" id="qb" style="top:1280px"><i>✕</i>«No es vulnerable»</div>'
               '<div class="q good" id="qg" style="top:1405px"><i>✓</i>«No observado bajo estas condiciones»</div>')
    b['r8'] = ('<div class="covers"><img id="cg" src="../assets/guide.png" alt="Guía de investigación"><img id="cm" src="../assets/manual.png" alt="Manual de buenas prácticas"></div>'
               '<h2 class="t8" id="t8"><span>Guía y manual,</span><span>abiertos.</span></h2>'
               '<div class="url" id="u8">nullghost.io/ia-normas.html</div>'
               '<div class="meta" id="m8">Guía de 11 páginas, manual de 10 y plantillas CSV.<br>Versión de trabajo v0.4 · revisión técnica pendiente.</div>'
               '<div class="disc" id="d8">Referencias para investigar y evaluar. No acredita certificación.</div>')

    st = {k: s for k, s, _ in SCENES}
    js = ['window.__timelines=window.__timelines||{};const tl=gsap.timeline({paused:true});',
          "const U=(sel,t,o)=>tl.fromTo(sel,{opacity:0,y:o||30},{opacity:1,y:0,duration:.5,ease:'power3.out'},t);",
          "const ST=(sel,t,s)=>tl.fromTo(sel,{opacity:0,y:30},{opacity:1,y:0,duration:.45,ease:'power3.out',stagger:s||.1},t);"]
    for k, s, d in SCENES[:-1]:
        js.append(f"tl.to('#{k}i',{{opacity:0,duration:.25,ease:'power2.in'}},{s + d - .25});")
        if k != 'r1':
            js.append(f"U('#{k} .kick',{s},20);U('#{k} .h',{s + .08},20);")
    a = st['r1']
    js += [f"tl.fromTo('#rb',{{opacity:0,y:80}},{{opacity:.95,y:0,duration:1.2,ease:'power2.out'}},{a});",
           f"tl.to('#rb',{{y:-40,duration:1.8,ease:'none'}},{a + 1.2});",
           f"U('#k1',{a + .05},20);ST('#t1 span',{a + .15},.12);U('#s1',{a + .8});ST('#r1 .pill',{a + 1.2},.2);"]
    a = st['r2']
    js += [f"U('#ca',{a + .3},40);",
           f"tl.fromTo('#nd',{{opacity:0,scale:.8}},{{opacity:1,scale:1,duration:.55,ease:'back.out(1.7)'}},{a + .6});",
           f"U('#cb',{a + .9},-40);",
           f"tl.to(['#l1','#l2'],{{strokeDashoffset:0,duration:.45,ease:'power2.out'}},{a + 1.2});",
           f"tl.set(['#d1','#d2'],{{opacity:1}},{a + 1.6});",
           f"tl.fromTo('#d1',{{attr:{{cy:640}}}},{{attr:{{cy:760}},duration:.8,repeat:3,ease:'power1.inOut'}},{a + 1.6});",
           f"tl.fromTo('#d2',{{attr:{{cy:1170}}}},{{attr:{{cy:1040}},duration:.8,repeat:3,ease:'power1.inOut'}},{a + 1.6});"]
    a = st['r3']
    js.append(f"U('#rc',{a + .3},10);")
    for i in range(7):
        t = a + .45 + i * .3
        js += [f"tl.to('#sg{i}',{{strokeDashoffset:0,duration:.35,ease:'power2.out'}},{t:.2f});",
               f"tl.to('#sl{i}',{{opacity:1,duration:.2}},{t + .15:.2f});",
               f"tl.fromTo('#r3 .legend div:nth-child({i + 1})',{{opacity:0,x:-20}},{{opacity:1,x:0,duration:.3}},{t:.2f});"]
    js.append(f"U('#imp',{a + 2.7});")
    a = st['r4']
    js += [f"U('#r4 .nums',{a + .2});",
           f"tl.fromTo('#n38',{{innerText:0}},{{innerText:38,snap:{{innerText:1}},duration:1.2,ease:'power2.out'}},{a + .3});",
           f"tl.fromTo('#n9',{{innerText:0}},{{innerText:9,snap:{{innerText:1}},duration:.9,ease:'power2.out'}},{a + .6});",
           f"ST('#r4 .tile',{a + .6},.08);",
           f"tl.fromTo('#r4 .tile .bar',{{scaleX:0}},{{scaleX:1,duration:.35,stagger:.08}},{a + .9});",
           f"U('#r4 .src',{a + 1.9},10);"]
    a = st['r5']
    js += [f"U('#ph0 .pn',{a + .3},10);U('#ph1 .pn',{a + .4},10);U('#ph2 .pn',{a + .5},10);",
           f"tl.fromTo('#r5 .thr',{{opacity:0,scale:.7}},{{opacity:1,scale:1,duration:.4,ease:'back.out(2)',stagger:.25}},{a + .6});",
           f"U('#st5',{a + 2.4});U('#r5 .src',{a + 2.9},10);"]
    a = st['r6']
    js += [f"tl.fromTo('#r6 .wk',{{opacity:0,scaleX:.3}},{{opacity:1,scaleX:1,duration:.45,stagger:.18,ease:'power3.out'}},{a + .3});",
           f"U('#ut h4',{a + 1.3},10);ST('#ut .ur',{a + 1.4},.1);",
           f"tl.fromTo('#ut .uf',{{scaleX:0}},{{scaleX:1,duration:.55,stagger:.14,ease:'power2.out'}},{a + 1.6});"]
    a = st['r7']
    js.append(f"tl.fromTo('#vf',{{scaleY:0}},{{scaleY:1,duration:1.4,ease:'none'}},{a + .3});")
    for i in range(4):
        t = a + .25 + i * .4
        js += [f"tl.fromTo('#st{i}',{{opacity:0,x:-30}},{{opacity:1,x:0,duration:.35,ease:'power3.out'}},{t:.2f});",
               f"tl.to('#st{i} .c',{{backgroundColor:'#1557a6',borderColor:'#64a3ff',duration:.25}},{t + .15:.2f});"]
    js += [f"U('#qb',{a + 1.9},20);U('#qg',{a + 2.2},20);"]
    a = st['r8']
    js += [f"U('#cg',{a + .1},50);U('#cm',{a + .3},50);ST('#t8 span',{a + .6},.12);",
           f"U('#u8',{a + 1.1},15);U('#m8',{a + 1.4},12);U('#d8',{a + 1.7},10);",
           "window.__timelines['main']=tl;"]

    sections = ''.join(sec(k, s, d, b[k]) for k, s, d in SCENES)
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=1080,height=1920">'
            f'<title>NullGhost · ISO IA · reel</title><script src="../assets/vendor/gsap.min.js"></script><style>{CSS}</style></head><body>'
            f'<div id="main" data-composition-id="main" data-width="1080" data-height="1920" data-duration="{DUR}">'
            f'<img class="brand" src="../assets/logo.svg" alt="NullGhost">{sections}</div><script>' + '\n'.join(js) + '</script></body></html>')


(R / 'compositions' / 'reel-es.html').write_text(build())
print('reel built')
