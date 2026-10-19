"""Reel 9:16 con motion design (versión pro) de la guía y el manual de IA v0.4.

Escenas encadenadas sin cortes en seco: hook cinético, hub de nodos, anillo de
cláusulas, conteo del Anexo A, amenazas con glitch, curva de aprendizaje,
tachado y reescritura de la conclusión, portadas en 3D y cierre.
Todo el texto sale de content.py. Sin audio (la música se agrega en Instagram).
Salida: compositions/reel-pro-es.html
"""
import math
from pathlib import Path

R = Path(__file__).resolve().parent
DUR = 33

CSS = r'''@font-face{font-family:Inter;src:url(../assets/inter.woff2) format("woff2");font-weight:100 900}
*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;background:#060A11;color:#fff;font-family:Inter,sans-serif}
#main{position:relative;width:1080px;height:1920px;overflow:hidden;background:#060A11}
.full{position:absolute;inset:0}
#grid{position:absolute;inset:-200px;background-image:linear-gradient(rgba(100,163,255,.075) 1px,transparent 1px),linear-gradient(90deg,rgba(100,163,255,.075) 1px,transparent 1px);background-size:72px 72px;
 -webkit-mask-image:radial-gradient(ellipse 60% 50% at 50% 48%,#000 0,transparent 100%);mask-image:radial-gradient(ellipse 60% 50% at 50% 48%,#000 0,transparent 100%)}
.orb{position:absolute;border-radius:50%;filter:blur(40px)}
#o1{width:900px;height:900px;left:-300px;top:200px;background:radial-gradient(circle,rgba(21,87,166,.55),transparent 65%)}
#o2{width:800px;height:800px;right:-320px;top:1000px;background:radial-gradient(circle,rgba(100,163,255,.28),transparent 65%)}
#vig{background:radial-gradient(ellipse 75% 60% at 50% 50%,transparent 55%,rgba(0,0,0,.7) 100%)}
#grain{opacity:.07;mix-blend-mode:overlay}
#logo{position:absolute;top:150px;left:80px;width:240px;height:56px;z-index:20}
.sc{position:absolute;inset:0;opacity:0}
.cam{position:absolute;inset:0;transform-origin:540px 960px}
.ct{position:absolute;left:60px;right:60px;text-align:center}
.big{font-weight:850;letter-spacing:-.06em;line-height:.95}
.acc{color:#64a3ff}
.kick{position:absolute;left:80px;top:300px;font-size:30px;letter-spacing:.14em;color:#64a3ff;font-weight:800}
.ttl{position:absolute;left:80px;right:80px;top:350px;font-size:76px;font-weight:850;letter-spacing:-.05em;line-height:1.02}
.note{position:absolute;left:80px;right:80px;font-size:26px;color:#8ea2b9;line-height:1.3}
/* A hook */
.hl{font-size:132px}
.ul{position:absolute;height:12px;border-radius:6px;background:#64a3ff;transform-origin:0 50%}
.w3 span{display:inline-block}
.pill{position:absolute;font-size:44px;font-weight:850;padding:20px 36px;border-radius:999px;border:3px solid #64a3ff;background:rgba(14,30,56,.85);box-shadow:0 0 60px rgba(100,163,255,.35)}
.ring{position:absolute;border-radius:50%;border:3px solid #64a3ff}
/* B hub */
.hubn{position:absolute;left:400px;top:760px;width:280px;height:280px;border-radius:50%;border:4px solid #64a3ff;background:radial-gradient(circle at 50% 38%,#163566 0,#0a1322 72%);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;box-shadow:0 0 90px rgba(100,163,255,.35)}
.hubn img{width:120px;margin-bottom:8px}.hubn b{font-size:34px;line-height:1.08;letter-spacing:-.02em}
.sat{position:absolute;width:240px;height:76px;margin:-38px 0 0 -120px;border-radius:999px;background:#0e1a2c;border:2px solid #2c4f86;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:700;color:#dfe8f2}
.bcard{position:absolute;left:80px;right:80px;border-radius:28px;padding:30px 36px;background:rgba(13,21,34,.92);border:2px solid #1557a6}
.bcard .r{font-size:30px;font-weight:850;color:#64a3ff;letter-spacing:.02em}.bcard b{display:block;font-size:56px;letter-spacing:-.04em;margin-top:6px}
/* C ring */
.cnum{position:absolute;left:340px;top:880px;width:400px;text-align:center}
.cnum .n{position:absolute;left:0;right:0;top:-60px;font-size:150px;font-weight:850;letter-spacing:-.06em;opacity:0}
.cnum .m{position:absolute;left:0;right:0;top:110px;font-size:40px;font-weight:700;color:#bcd6ff;opacity:0}
.callout{position:absolute;left:80px;right:80px;top:1350px;padding:26px 32px;border-left:7px solid #64a3ff;background:rgba(15,29,51,.95);border-radius:0 22px 22px 0}
.callout .k{font-size:28px;letter-spacing:.1em;color:#64a3ff;font-weight:850}.callout p{font-size:38px;line-height:1.22;margin:8px 0 0;font-weight:650}
/* D annex */
.n38{position:absolute;left:0;right:0;top:470px;text-align:center;font-size:400px;font-weight:850;letter-spacing:-.08em;line-height:.8}
.lbl{position:absolute;left:0;right:0;text-align:center;font-size:48px;font-weight:800}
.tile{position:absolute;width:296px;height:150px;border-radius:20px;background:rgba(13,21,34,.95);border:2px solid #22344a;padding:18px 20px;overflow:hidden}
.tile .i{font-size:32px;font-weight:850;color:#64a3ff}.tile .t{font-size:28px;font-weight:650;line-height:1.12;margin-top:6px}
.tile .bar{position:absolute;left:0;bottom:0;height:6px;width:100%;background:#64a3ff;transform-origin:0 50%}
/* E threats */
.track{position:absolute;left:110px;top:600px;width:6px;height:780px;background:#64a3ff;border-radius:3px;transform-origin:50% 0;box-shadow:0 0 18px rgba(100,163,255,.6)}
.sd{position:absolute;left:94px;width:38px;height:38px;border-radius:50%;background:#060A11;border:6px solid #64a3ff}
.pn{position:absolute;left:160px;font-size:30px;font-weight:850;color:#9fb3c8;letter-spacing:.06em;text-transform:uppercase}
.chip{position:absolute;height:112px;border-radius:18px;background:#1557a6;padding:14px 22px;display:flex;flex-direction:column;justify-content:center}
.chip.op{background:#13294d;border:2px solid #2f5a99}
.chip .t{font-size:31px;font-weight:750;line-height:1.1}.chip .r{font-size:24px;font-weight:850;color:#bcd6ff;letter-spacing:.06em;margin-top:4px}
.stat{position:absolute;left:80px;right:80px;top:1400px;display:flex;align-items:center;gap:26px}
.stat .v{font-size:130px;font-weight:850;letter-spacing:-.06em;line-height:1}.stat .l{font-size:33px;line-height:1.22;color:#dfe8f2}
/* F learn */
.wk{position:absolute;left:80px;height:112px;border-radius:20px;background:#13294d;transform-origin:0 50%;display:flex;align-items:center;padding:0 28px;gap:24px;overflow:hidden}
.wk.pay{background:#1557a6}
.wk .w{font-size:28px;font-weight:850;color:#9cc4ff;letter-spacing:.05em;white-space:nowrap}.wk b{font-size:44px;letter-spacing:-.03em;white-space:nowrap}
.uh{position:absolute;left:80px;right:80px;top:1080px;font-size:30px;font-weight:850;color:#64a3ff}
.ur{position:absolute;left:80px;right:80px;height:70px;display:grid;grid-template-columns:400px 1fr;align-items:center;font-size:34px;font-weight:700}
.ut{height:42px;background:#121c2a;border-radius:10px;position:relative;overflow:hidden}
.uf{position:absolute;left:0;top:0;bottom:0;border-radius:10px;background:linear-gradient(90deg,#1557a6,#64a3ff);transform-origin:0 50%;display:flex;align-items:center;justify-content:flex-end;padding-right:14px;font-size:22px;font-weight:850;color:#06101e;letter-spacing:.06em}
.uf.low{background:#3a4c63;color:#dfe8f2;justify-content:flex-start;padding-left:12px}
.strike{position:absolute;left:-8px;top:50%;height:6px;width:calc(100% + 16px);margin-top:-3px;background:#ff5d73;border-radius:3px;transform-origin:0 50%}
.rel{position:relative;display:inline-block}
/* G evidence */
.vt{position:absolute;left:136px;top:600px;width:8px;height:560px;background:#1c2a3b;border-radius:4px}
.vf{position:absolute;left:136px;top:600px;width:8px;height:560px;background:#64a3ff;border-radius:4px;transform-origin:50% 0;box-shadow:0 0 18px rgba(100,163,255,.6)}
.st{position:absolute;left:80px;right:80px;height:120px;display:flex;align-items:center;gap:34px}
.st .c{position:relative;width:120px;height:120px;flex:0 0 120px;border-radius:50%;background:#0d1522;border:6px solid #2a4060;font-size:48px;font-weight:850}
.st .c span{position:absolute;inset:0;display:flex;align-items:center;justify-content:center}
.st b{display:block;font-size:52px;letter-spacing:-.03em}.st i{display:block;font-style:normal;font-size:30px;color:#b8c7d8;margin-top:2px}
.qb{position:absolute;left:80px;right:80px;top:1330px;height:120px;border-radius:22px;border:2px solid #5a2a35;background:#1a1216}
.qt{position:absolute;left:36px;top:0;bottom:0;display:flex;align-items:center;font-size:44px;font-weight:800;white-space:nowrap}
/* H cta */
.persp{position:absolute;left:0;right:0;top:330px;height:700px;perspective:1600px}
.cov{position:absolute;top:0;width:430px;height:608px;border-radius:10px;box-shadow:0 40px 90px rgba(0,0,0,.75),0 0 0 1px #22344a}
.glow{position:absolute;left:140px;top:420px;width:800px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(100,163,255,.5),transparent 65%);filter:blur(30px)}
.h8{position:absolute;left:80px;right:80px;top:1035px;font-size:96px;font-weight:850;letter-spacing:-.055em;line-height:1}
.h8 span{display:inline-block;margin-right:22px}
.url{position:absolute;left:80px;top:1265px;font-size:50px;font-weight:850;white-space:nowrap}
.url span{display:inline-block}
.m8{position:absolute;left:80px;right:80px;top:1350px;font-size:31px;line-height:1.4;color:#c9d6e4}
'''


def arc(cx, cy, r, a0, a1):
    def p(a):
        t = math.radians(a - 90)
        return cx + r * math.cos(t), cy + r * math.sin(t)
    x0, y0 = p(a0); x1, y1 = p(a1)
    return f'M{x0:.1f} {y0:.1f} A{r} {r} 0 {1 if a1 - a0 > 180 else 0} 1 {x1:.1f} {y1:.1f}'


def html():
    # ---------- A: hook ----------
    A = ('<div class="sc" id="A"><div class="cam" id="Ac">'
         '<div class="ct big hl" id="a1" style="top:760px;opacity:0">¿Tu empresa<br>ya usa IA?</div>'
         '<div class="ct big hl" id="a2" style="top:760px;opacity:0">¿Quién la<br><span class="rel"><span id="a2w" class="acc">gobierna?</span><span id="a3w" class="acc" style="position:absolute;left:0;top:0;opacity:0">protege?</span></span></div>'
         '<div class="ul" id="aul" style="left:250px;top:1030px;width:580px"></div>'
         '<div class="ring" id="ar" style="left:290px;top:610px;width:500px;height:500px;opacity:0"></div>'
         '<div class="ct big w3" id="a4" style="top:560px;font-size:170px"><span>Dos</span><br><span>normas</span><br><span class="acc">ISO.</span></div>'
         '<div class="pill" id="p1" style="left:80px;top:1180px;opacity:0">42001</div>'
         '<div class="pill" id="p2" style="right:80px;top:1180px;opacity:0">27090</div>'
         '<div class="ct" id="a5" style="top:1340px;font-size:40px;font-weight:650;color:#c9d6e4;opacity:0">Una dice cómo gobernarla.<br>La otra, cómo la atacan.</div>'
         '</div></div>')
    # ---------- B: hub ----------
    cx, cy, rr = 540, 900, 345
    sats = ['datos', 'modelo', 'prompts', 'herramientas', 'salidas']
    lines, satd = '', ''
    for i, s in enumerate(sats):
        a = math.radians(-90 + 72 * i + 36)
        x, y = cx + rr * math.cos(a), cy + rr * math.sin(a) * .82
        lines += f'<path id="bl{i}" d="M{cx} {cy} L{x:.0f} {y:.0f}" stroke="#2f5a99" stroke-width="3" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
        satd += f'<div class="sat" id="bs{i}" style="left:{x:.0f}px;top:{y:.0f}px">{s}</div>'
    B = ('<div class="sc" id="B"><div class="cam" id="Bc">'
         f'<svg class="full" viewBox="0 0 1080 1920">{lines}'
         '<path id="bk1" d="M540 470 L540 760" stroke="#64a3ff" stroke-width="4" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
         '<path id="bk2" d="M540 1330 L540 1040" stroke="#64a3ff" stroke-width="4" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
         '<circle id="bd1" cx="540" cy="470" r="11" fill="#9cc4ff" opacity="0"/><circle id="bd2" cx="540" cy="1330" r="11" fill="#9cc4ff" opacity="0"/></svg>'
         f'{satd}'
         '<div class="hubn" id="bh"><img src="../assets/ghost.svg" alt=""><b>Tu sistema<br>de IA</b></div>'
         '<div class="bcard" id="bc1" style="top:280px"><div class="r">ISO/IEC 42001:2023</div><b>Cómo gobernarla</b></div>'
         '<div class="bcard" id="bc2" style="top:1330px"><div class="r">ISO/IEC 27090:2026</div><b>Cómo la atacan</b></div>'
         '</div></div>')
    # ---------- C: anillo de cláusulas ----------
    ccx, ccy, cr, gap, span = 540, 960, 270, 4, 360 / 7
    cl = [('4', 'Contexto'), ('5', 'Liderazgo'), ('6', 'Planificación'), ('7', 'Apoyo'), ('8', 'Operación'), ('9', 'Evaluación'), ('10', 'Mejora')]
    segs = f'<circle cx="{ccx}" cy="{ccy}" r="{cr}" stroke="#0f1826" stroke-width="96" fill="none"/>'
    for i, (n, _) in enumerate(cl):
        a0, a1 = i * span + gap / 2, (i + 1) * span - gap / 2
        t = math.radians((a0 + a1) / 2 - 90)
        segs += (f'<path id="cs{i}" d="{arc(ccx, ccy, cr, a0, a1)}" stroke="{"#64a3ff" if n == "6" else "#1557a6"}" stroke-width="96" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
                 f'<text id="ct{i}" x="{ccx + cr * math.cos(t):.1f}" y="{ccy + cr * math.sin(t) + 14:.1f}" text-anchor="middle" font-size="40" font-weight="850" fill="#fff" opacity="0">{n}</text>')
    cnum = ''.join(f'<div class="n" id="cn{i}">{n}</div><div class="m" id="cm{i}">{m}</div>' for i, (n, m) in enumerate(cl))
    C = ('<div class="sc" id="C"><div class="cam" id="Cc">'
         '<div class="kick">ISO/IEC 42001 POR DENTRO</div><div class="ttl">7 cláusulas auditables</div>'
         f'<svg class="full" viewBox="0 0 1080 1920"><circle id="cglow" cx="{ccx}" cy="{ccy}" r="{cr}" stroke="#64a3ff" stroke-width="2" fill="none" opacity="0"/>{segs}</svg>'
         f'<div class="cnum">{cnum}<div class="n acc" id="cn7" style="font-size:120px;top:-40px">6.1.4</div></div>'
         '<div class="callout" id="cco"><div class="k">LA PIEZA NUEVA</div><p>Evaluación de impacto: efectos sobre personas, grupos y la sociedad.</p></div>'
         '</div></div>')
    # ---------- D: Anexo A ----------
    objs = [('A.2', 'Políticas de IA'), ('A.3', 'Organización interna'), ('A.4', 'Recursos'), ('A.5', 'Evaluación de impactos'),
            ('A.6', 'Ciclo de vida'), ('A.7', 'Datos'), ('A.8', 'Información a partes'), ('A.9', 'Uso de la IA'), ('A.10', 'Terceros y clientes')]
    tiles = ''
    for i, (a, t) in enumerate(objs):
        x, y = 80 + (i % 3) * 312, 1010 + (i // 3) * 166
        tiles += f'<div class="tile" id="dt{i}" style="left:{x}px;top:{y}px" data-dx="{540 - (x + 148)}" data-dy="{960 - (y + 75)}"><div class="i">{a}</div><div class="t">{t}</div><div class="bar"></div></div>'
    D = ('<div class="sc" id="D"><div class="cam" id="Dc">'
         '<div class="kick">ISO/IEC 42001 · ANEXO A</div>'
         '<div class="n38" id="dn">0</div><div class="lbl acc" id="dl1" style="top:810px">controles</div>'
         '<div class="lbl" id="dl2" style="top:880px;font-size:40px;color:#c9d6e4;font-weight:650">en <span id="dn9">0</span> objetivos</div>'
         f'{tiles}'
         '<div class="note" id="dnote" style="top:1520px">Estructura según fuentes secundarias; verificar en la norma.</div>'
         '</div></div>')
    # ---------- E: amenazas ----------
    chips = [(0, 'Envenenamiento de datos o modelos', 'LLM04', 160, 650, 820), (1, 'Cadena de suministro', 'LLM03', 160, 880, 600),
             (2, 'Inversión de modelos y fuga', 'LLM02', 160, 1110, 410), (2, 'Robo de modelos', 'ATLAS', 584, 1110, 416),
             (2, 'Inyección indirecta de prompts', 'LLM01', 160, 1236, 410), (2, 'Agentes con herramientas', 'LLM06', 584, 1236, 416)]
    ch = ''.join(f'<div class="chip{" op" if p == 2 else ""}" id="ec{i}" style="left:{x}px;top:{y}px;width:{w}px"><div class="t">{t}</div><div class="r">{r}</div></div>' for i, (p, t, r, x, y, w) in enumerate(chips))
    E = ('<div class="sc" id="E"><div class="cam" id="Ec">'
         '<div class="kick">ISO/IEC 27090:2026</div><div class="ttl">Amenazas en todo<br>el ciclo de vida</div>'
         '<div class="track" id="etr"></div>'
         '<div class="sd" id="ed0" style="top:592px"></div><div class="pn" id="ep0" style="top:592px">Datos y entrenamiento</div>'
         '<div class="sd" id="ed1" style="top:822px"></div><div class="pn" id="ep1" style="top:822px">Desarrollo y despliegue</div>'
         '<div class="sd" id="ed2" style="top:1052px"></div><div class="pn" id="ep2" style="top:1052px">Operación e integración</div>'
         f'{ch}'
         '<div class="stat" id="est"><div class="v"><span id="e12">0</span>+</div><div class="l">escenarios de ataque deliberado, según el ISO27k Forum</div></div>'
         '<div class="note" id="enote" style="top:1530px">Correspondencia aproximada con OWASP y MITRE ATLAS.</div>'
         '</div></div>')
    # ---------- F: aprendizaje ----------
    weeks = [('S1', 'Mapa', 560), ('S2', 'Amenazas', 700), ('S3', 'Controles', 840), ('S4', 'Aplicar', 920)]
    wk = ''.join(f'<div class="wk{" pay" if i == 2 else ""}" id="fw{i}" style="top:{530 + i * 128}px;width:{w}px"><span class="w">{s}</span><b>{t}</b></div>' for i, (s, t, w) in enumerate(weeks))
    util = [('Recuperación', 'ALTA', 1), ('Práctica espaciada', 'ALTA', 1), ('Releer', 'BAJA', .26), ('Subrayar', 'BAJA', .26)]
    ur = ''.join(f'<div class="ur" id="fr{i}" style="top:{1140 + i * 86}px"><span><span class="rel">{n}{"<span class=strike id=fs" + str(i) + "></span>" if v < 1 else ""}</span></span><div class="ut"><div class="uf{" low" if v < 1 else ""}" id="ff{i}" style="width:{v * 100:.0f}%">{lv}</div></div></div>' for i, (n, lv, v) in enumerate(util))
    F = ('<div class="sc" id="F"><div class="cam" id="Fc">'
         '<div class="kick">CAMINO DE APRENDIZAJE</div><div class="ttl">Apréndelas en<br>4 semanas</div>'
         f'{wk}<div class="uh" id="fuh">Qué funciona para estudiar · Dunlosky et al. (2013)</div>{ur}'
         '</div></div>')
    # ---------- G: evidencia ----------
    states = [('Propuesto', 'El plan existe'), ('Observado', 'Hay respuesta, con contexto'), ('Reproducido', 'Se repite el efecto'), ('Verificado', 'Un revisor lo confirma')]
    st = ''.join(f'<div class="st" id="gs{i}" style="top:{540 + i * 172}px"><div class="c" id="gc{i}"><span id="gn{i}">{i + 1}</span><span id="gk{i}" style="opacity:0">✓</span></div><div><b>{n}</b><i>{d}</i></div></div>' for i, (n, d) in enumerate(states))
    G = ('<div class="sc" id="G"><div class="cam" id="Gc">'
         '<div class="kick">MÉTODO DE EVIDENCIA</div><div class="ttl">Investiga con evidencia</div>'
         f'<div class="vt"></div><div class="vf" id="gvf"></div>{st}'
         '<div class="qb" id="gq"><div class="qt" id="gq1" style="color:#e6b3bd"><span class="rel">«No es vulnerable»<span class="strike" id="gstr"></span></span></div>'
         '<div class="qt" id="gq2" style="clip-path:inset(0 100% 0 0)">«No observado bajo estas condiciones»</div></div>'
         '</div></div>')
    # ---------- H: cierre ----------
    H = ('<div class="sc" id="H"><div class="cam" id="Hc">'
         '<div class="glow" id="hg"></div>'
         '<div class="persp"><img class="cov" id="hc1" src="../assets/guide.png" style="left:85px" alt="Guía de investigación"><img class="cov" id="hc2" src="../assets/manual.png" style="left:565px" alt="Manual de buenas prácticas"></div>'
         '<div class="h8" id="h8"><span>Guía</span><span>y</span><span>manual,</span><span class="acc">abiertos.</span></div>'
         '<div class="url" id="hu"><span>nullghost.io</span><span class="acc">/ia-normas.html</span></div>'
         '<div class="m8" id="hm">Versión de trabajo v0.4 · revisión técnica pendiente.<br>No acredita certificación.</div>'
         '</div></div>')

    grain = ('<svg class="full" id="grain" viewBox="0 0 1080 1920"><filter id="nz"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="7"/></filter>'
             '<rect width="1080" height="1920" filter="url(#nz)"/></svg>')
    body = (f'<div id="main" data-composition-id="main" data-width="1080" data-height="1920" data-duration="{DUR}">'
            '<div class="full" id="bg"><div id="grid"></div><div class="orb" id="o1"></div><div class="orb" id="o2"></div></div>'
            f'{A}{B}{C}{D}{E}{F}{G}{H}'
            f'<div class="full" id="vig"></div>{grain}<img id="logo" src="../assets/logo.svg" alt="NullGhost"></div>')
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=1080,height=1920">'
            f'<title>NullGhost · ISO IA · reel</title><script src="../assets/vendor/gsap.min.js"></script><style>{CSS}</style></head><body>'
            f'{body}<script>{JS}</script></body></html>')


JS = r'''
window.__timelines=window.__timelines||{};
const tl=gsap.timeline({paused:true});
const sp='back.out(1.8)', ex='expo.out', io='power2.inOut';
const show=(id,t)=>tl.set(id,{opacity:1},t);
const hide=(id,t)=>tl.set(id,{opacity:0},t);
// fly-in con desenfoque de movimiento
const blurIn=(sel,t,o)=>tl.fromTo(sel,Object.assign({opacity:0,scale:1.25,filter:'blur(18px)'},o||{}),{opacity:1,scale:1,x:0,y:0,filter:'blur(0px)',duration:.45,ease:ex},t);
const pop=(sel,t,st)=>tl.fromTo(sel,{opacity:0,scale:.4},{opacity:1,scale:1,duration:.5,ease:sp,stagger:st||0},t);
const up=(sel,t,st)=>tl.fromTo(sel,{opacity:0,y:50},{opacity:1,y:0,duration:.5,ease:ex,stagger:st||0},t);
// transición: la escena saliente se va hacia la cámara con desenfoque; la entrante llega desde atrás
const zoomOut=(id,t)=>{tl.to(id,{scale:1.6,opacity:0,filter:'blur(16px)',duration:.4,ease:'power2.in'},t);};
const zoomIn=(id,t)=>{tl.fromTo(id,{opacity:0,scale:.7,filter:'blur(16px)'},{opacity:1,scale:1,filter:'blur(0px)',duration:.5,ease:ex},t);};
const push=(cam,t,d,s)=>tl.fromTo(cam,{scale:1},{scale:s||1.07,duration:d,ease:'none'},t);

// ambiente continuo
tl.fromTo('#grid',{backgroundPosition:'0px 0px'},{backgroundPosition:'0px 432px',duration:33,ease:'none'},0);
tl.fromTo('#o1',{x:0,y:0},{x:260,y:180,duration:16.5,ease:'sine.inOut',yoyo:true,repeat:1},0);
tl.fromTo('#o2',{x:0,y:0},{x:-220,y:-260,duration:16.5,ease:'sine.inOut',yoyo:true,repeat:1},0);
tl.fromTo('#logo',{opacity:0,y:-20},{opacity:1,y:0,duration:.6,ease:ex},.2);
tl.to('#logo',{opacity:0,duration:.3},28.2);

// ===== A: hook (0 - 4.4) =====
show('#A',0); push('#Ac',0,4.4,1.06);
blurIn('#a1',.05); tl.to('#a1',{opacity:0,scale:.9,filter:'blur(10px)',duration:.18,ease:'power2.in'},.95);
pop('#a2',1.1);
tl.fromTo('#aul',{scaleX:0},{scaleX:1,duration:.35,ease:ex},1.35);
// cambio de palabra en seco: gobierna -> protege, con destello del subrayado
tl.set('#a2w',{opacity:0},1.95); tl.set('#a3w',{opacity:1},1.95);
tl.fromTo('#aul',{scaleX:0,transformOrigin:'0 50%'},{scaleX:1,duration:.3,ease:ex},1.95);
tl.fromTo('#a2',{scale:1.08},{scale:1,duration:.3,ease:sp},1.95);
// zoom a través del texto
tl.to(['#a2','#aul'],{scale:5,opacity:0,filter:'blur(14px)',duration:.4,ease:'power3.in'},2.55);
tl.fromTo('#a4 span',{opacity:0,y:120,filter:'blur(12px)'},{opacity:1,y:0,filter:'blur(0px)',duration:.4,ease:ex,stagger:.13},2.85);
tl.fromTo('#ar',{opacity:.9,scale:.3},{opacity:0,scale:2.2,duration:.9,ease:'power2.out'},3.2);
tl.fromTo('#p1',{opacity:0,x:-500,filter:'blur(20px)'},{opacity:1,x:0,filter:'blur(0px)',duration:.45,ease:ex},3.35);
tl.fromTo('#p2',{opacity:0,x:500,filter:'blur(20px)'},{opacity:1,x:0,filter:'blur(0px)',duration:.45,ease:ex},3.5);
up('#a5',3.75);
zoomOut('#A',4.4);

// ===== B: hub (4.5 - 8.7) =====
zoomIn('#B',4.45); push('#Bc',4.45,4.3,1.08);
pop('#bh',4.55);
tl.to(['#bl0','#bl1','#bl2','#bl3','#bl4'],{strokeDashoffset:0,duration:.4,ease:ex,stagger:.08},4.8);
pop('#B .sat',4.95,.08);
tl.fromTo('#B .sat',{y:0},{y:-10,duration:1.2,ease:'sine.inOut',yoyo:true,repeat:2,stagger:.15},5.6);
tl.fromTo('#bc1',{opacity:0,y:-160,filter:'blur(14px)'},{opacity:1,y:0,filter:'blur(0px)',duration:.55,ease:sp},5.7);
tl.to('#bk1',{strokeDashoffset:0,duration:.35,ease:ex},6.05);
tl.fromTo('#bc2',{opacity:0,y:160,filter:'blur(14px)'},{opacity:1,y:0,filter:'blur(0px)',duration:.55,ease:sp},6.4);
tl.to('#bk2',{strokeDashoffset:0,duration:.35,ease:ex},6.75);
tl.set(['#bd1','#bd2'],{opacity:1},6.9);
tl.fromTo('#bd1',{attr:{cy:470}},{attr:{cy:760},duration:.6,ease:'power1.in',repeat:2},6.9);
tl.fromTo('#bd2',{attr:{cy:1330}},{attr:{cy:1040},duration:.6,ease:'power1.in',repeat:2},6.9);
tl.fromTo('#bh',{boxShadow:'0 0 90px rgba(100,163,255,.35)'},{boxShadow:'0 0 160px rgba(100,163,255,.85)',duration:.3,yoyo:true,repeat:5},6.9);
// el hub se hunde y abre el anillo
tl.to('#B',{scale:.35,opacity:0,filter:'blur(12px)',duration:.45,ease:'power3.in'},8.35);

// ===== C: anillo (8.6 - 13.3) =====
tl.fromTo('#C',{opacity:0,scale:1.5,filter:'blur(16px)'},{opacity:1,scale:1,filter:'blur(0px)',duration:.55,ease:ex},8.6); push('#Cc',8.6,4.7,1.06);
up('#C .kick',8.7); up('#C .ttl',8.78);
for(let i=0;i<7;i++){const t=9.05+i*.36;
 tl.to('#cs'+i,{strokeDashoffset:0,duration:.34,ease:ex},t);
 tl.to('#ct'+i,{opacity:1,duration:.15},t+.15);
 tl.fromTo(['#cn'+i,'#cm'+i],{opacity:0,y:30},{opacity:1,y:0,duration:.18,ease:ex},t);
 if(i<6) tl.set(['#cn'+i,'#cm'+i],{opacity:0},t+.36);}
tl.to(['#cn6','#cm6'],{opacity:0,duration:.15},11.75);
tl.to(['#cs0','#cs1','#cs3','#cs4','#cs5','#cs6'],{opacity:.3,duration:.3},11.8);
tl.fromTo('#cs2',{attr:{'stroke-width':96}},{attr:{'stroke-width':120},duration:.35,ease:sp},11.8);
tl.fromTo('#cglow',{opacity:.9,scale:1,svgOrigin:'540 960'},{opacity:0,scale:1.35,duration:.8,ease:'power2.out'},11.85);
pop('#cn7',11.85);
tl.fromTo('#cco',{opacity:0,x:-120,filter:'blur(12px)'},{opacity:1,x:0,filter:'blur(0px)',duration:.5,ease:ex},12.05);
// zoom dentro del segmento 6 hacia el Anexo A
tl.to('#C',{scale:3,x:-500,y:200,opacity:0,filter:'blur(14px)',duration:.45,ease:'power3.in'},13.0);

// ===== D: Anexo A (13.3 - 16.9) =====
zoomIn('#D',13.3); push('#Dc',13.3,3.6,1.06);
up('#D .kick',13.35);
tl.fromTo('#dn',{innerText:0,opacity:0,scale:.6},{innerText:38,snap:{innerText:1},opacity:1,scale:1,duration:1.1,ease:'power3.out'},13.4);
up('#dl1',14.0); up('#dl2',14.2);
tl.fromTo('#dn9',{innerText:0},{innerText:9,snap:{innerText:1},duration:.7,ease:'power2.out'},14.2);
for(let i=0;i<9;i++){const el='#dt'+i;
 tl.fromTo(el,{opacity:0,scale:.2,x:()=>+document.querySelector(el).dataset.dx,y:()=>+document.querySelector(el).dataset.dy},{opacity:1,scale:1,x:0,y:0,duration:.55,ease:sp},14.3+i*.07);}
tl.fromTo('#D .tile .bar',{scaleX:0},{scaleX:1,duration:.3,stagger:.07,ease:ex},14.9);
up('#dnote',15.6);
tl.to('#D',{y:-500,opacity:0,filter:'blur(12px)',duration:.45,ease:'power3.in'},16.55);

// ===== E: amenazas (16.8 - 21.5) =====
tl.fromTo('#E',{opacity:0,y:500,filter:'blur(12px)'},{opacity:1,y:0,filter:'blur(0px)',duration:.5,ease:ex},16.8); push('#Ec',16.8,4.7,1.05);
up('#E .kick',16.85); up('#E .ttl',16.92);
tl.fromTo('#etr',{scaleY:0},{scaleY:1,duration:1.1,ease:'power2.inOut'},17.1);
for(let i=0;i<3;i++){pop('#ed'+i,17.2+i*.35); tl.fromTo('#ep'+i,{opacity:0,x:-40},{opacity:1,x:0,duration:.35,ease:ex},17.25+i*.35);}
const ct=[17.55,17.95,18.35,18.5,18.65,18.8];
ct.forEach((t,i)=>{const el='#ec'+i;
 tl.fromTo(el,{opacity:0,x:700,filter:'blur(24px)'},{opacity:1,x:0,filter:'blur(0px)',duration:.32,ease:'expo.out'},t);
 // glitch cromático al aterrizar
 tl.fromTo(el+' .t',{textShadow:'7px 0 #ff3b6b,-7px 0 #3bd5ff'},{textShadow:'0px 0 rgba(255,59,107,0),0px 0 rgba(59,213,255,0)',duration:.28,ease:'steps(4)'},t+.25);
 tl.to(el,{keyframes:{x:[10,-8,6,-3,0]},duration:.22,ease:'none'},t+.25);});
tl.fromTo('#est',{opacity:0,y:40},{opacity:1,y:0,duration:.4,ease:ex},19.35);
tl.fromTo('#e12',{innerText:0},{innerText:12,snap:{innerText:1},duration:.8,ease:'power2.out'},19.4);
up('#enote',19.9);
// los chips se dispersan en profundidad
tl.to('#E .chip',{opacity:0,scale:1.6,filter:'blur(18px)',x:(i)=>[-200,120,-260,260,-160,220][i],y:(i)=>[-160,-80,40,20,160,140][i],duration:.4,ease:'power3.in',stagger:.02},21.1);
tl.to('#E',{opacity:0,duration:.25},21.3);

// ===== F: aprendizaje (21.5 - 25.1) =====
show('#F',21.45); push('#Fc',21.45,3.7,1.05);
tl.fromTo('#F',{clipPath:'circle(0% at 50% 50%)'},{clipPath:'circle(75% at 50% 50%)',duration:.6,ease:'power3.out'},21.45);
up('#F .kick',21.5); up('#F .ttl',21.58);
tl.fromTo('#F .wk',{scaleX:0,opacity:0},{scaleX:1,opacity:1,duration:.5,ease:ex,stagger:.14},21.8);
up('#fuh',22.55);
tl.fromTo('#F .ur',{opacity:0,x:-40},{opacity:1,x:0,duration:.35,ease:ex,stagger:.1},22.7);
tl.fromTo('#F .uf',{scaleX:0},{scaleX:1,duration:.5,ease:ex,stagger:.12},22.9);
tl.fromTo(['#fs2','#fs3'],{scaleX:0},{scaleX:1,duration:.3,ease:'power2.out',stagger:.18},23.75);
tl.to(['#fr2','#fr3'],{opacity:.45,duration:.3},24.0);
tl.fromTo(['#ff0','#ff1'],{boxShadow:'0 0 0 rgba(100,163,255,0)'},{boxShadow:'0 0 40px rgba(100,163,255,.9)',duration:.3,yoyo:true,repeat:1},24.05);
tl.to('#F',{clipPath:'inset(0% 0% 100% 0%)',duration:.45,ease:'power3.inOut'},24.75);

// ===== G: evidencia (25.1 - 28.4) =====
show('#G',24.95); push('#Gc',24.95,3.4,1.05);
tl.fromTo('#G',{clipPath:'inset(100% 0% 0% 0%)'},{clipPath:'inset(0% 0% 0% 0%)',duration:.45,ease:'power3.inOut'},24.95);
up('#G .kick',25.1); up('#G .ttl',25.18);
tl.fromTo('#G .st',{opacity:0,x:-50},{opacity:1,x:0,duration:.35,ease:ex,stagger:.1},25.3);
tl.fromTo('#gvf',{scaleY:0},{scaleY:1,duration:1.2,ease:'none'},25.6);
for(let i=0;i<4;i++){const t=25.6+i*.4;
 tl.to('#gc'+i,{backgroundColor:'#1557a6',borderColor:'#64a3ff',duration:.15},t);
 tl.to('#gn'+i,{opacity:0,scale:.3,duration:.12},t);
 tl.fromTo('#gk'+i,{opacity:0,scale:.3},{opacity:1,scale:1,duration:.3,ease:sp},t+.08);}
tl.fromTo('#gq',{opacity:0,y:40},{opacity:1,y:0,duration:.35,ease:ex},26.75);
tl.fromTo('#gstr',{scaleX:0},{scaleX:1,duration:.3,ease:'power2.out'},27.2);
tl.to('#gq1',{opacity:0,x:-30,duration:.2},27.55);
tl.to('#gq',{backgroundColor:'#0f1d33',borderColor:'#64a3ff',duration:.25},27.6);
tl.fromTo('#gq2',{clipPath:'inset(0 100% 0 0)'},{clipPath:'inset(0 0% 0 0)',duration:.5,ease:'steps(18)'},27.65);
zoomOut('#G',28.35);

// ===== H: cierre (28.5 - 33) =====
zoomIn('#H',28.5);
tl.fromTo('#hg',{opacity:0,scale:.5},{opacity:1,scale:1,duration:.9,ease:ex},28.6);
tl.fromTo('#hc1',{opacity:0,rotationY:70,x:-420,z:-300},{opacity:1,rotationY:-6,x:0,z:0,duration:.8,ease:ex},28.6);
tl.fromTo('#hc2',{opacity:0,rotationY:-70,x:420,z:-300},{opacity:1,rotationY:6,x:0,z:0,duration:.8,ease:ex},28.72);
tl.to('#hc1',{rotationY:4,y:-10,duration:3.6,ease:'sine.inOut'},29.4);
tl.to('#hc2',{rotationY:-4,y:10,duration:3.6,ease:'sine.inOut'},29.4);
tl.fromTo('#h8 span',{opacity:0,y:80,filter:'blur(10px)'},{opacity:1,y:0,filter:'blur(0px)',duration:.4,ease:ex,stagger:.1},29.3);
tl.fromTo('#hu span',{opacity:0,x:-30},{opacity:1,x:0,duration:.35,ease:ex,stagger:.25},29.9);
up('#hm',30.45);
tl.fromTo('#logo',{opacity:0},{opacity:1,duration:.4},30.6);
window.__timelines['main']=tl;
'''

(R / 'compositions' / 'reel-pro-es.html').write_text(html())
print('reel pro built')
