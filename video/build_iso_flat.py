"""Video 16:9 de la guía ISO ('Dos normas ISO') en el estilo PLANO de Research,
no el premium. Silencioso, ES/EN, ~44 s. Reemplaza iso-ai-es/en en el sitio.
Salida: compositions/iso-flat-es.html y iso-flat-en.html.
"""
from pathlib import Path
from html import escape as E

R = Path(__file__).resolve().parent
DUR = 44
SCENES = [('s1', 0, 5), ('s2', 5, 6), ('s3', 11, 6.5), ('s4', 17.5, 6), ('s5', 23.5, 6.5), ('s6', 30, 5.5), ('s7', 35.5, 5), ('s8', 40.5, 3.5)]

COPY = {
 'es': dict(bar='DOS NORMAS ISO PARA LA IA',
   h1=['Dos normas ISO', 'para la IA'], s1='Una dice cómo gobernarla. La otra, cómo la atacan.', chips=['ISO/IEC 42001:2023', 'ISO/IEC 27090:2026'],
   h2='Dos preguntas distintas', c2=[('ISO/IEC 42001:2023', 'Gestión de IA', '¿Quién decide, con qué política y cómo se controla y mejora el uso de IA?'),
                                     ('ISO/IEC 27090:2026', 'Amenazas al sistema', '¿Qué amenazas hay en cada fase del ciclo de vida y cómo detectarlas y mitigarlas?')],
   h3='ISO/IEC 42001 por dentro', clauses=[('4','Contexto'),('5','Liderazgo'),('6','Planificación'),('7','Apoyo'),('8','Operación'),('9','Evaluación'),('10','Mejora')],
   note3='6.1.4 · la pieza nueva: evaluación de impacto sobre personas, grupos y la sociedad.',
   h4='El Anexo A, en cifras', n4=[('38','controles'),('9','objetivos')], objs=['A.2 Políticas','A.3 Organización','A.4 Recursos','A.5 Impactos','A.6 Ciclo de vida','A.7 Datos','A.8 Información','A.9 Uso','A.10 Terceros'],
   note4='Estructura según fuentes secundarias; verificar en la norma.',
   h5='ISO/IEC 27090: amenazas por fase', ph=[('Datos y entrenamiento',['Envenenamiento (LLM04)']),('Desarrollo y despliegue',['Cadena de suministro (LLM03)']),('Operación',['Inversión y fuga (LLM02)','Inyección de prompts (LLM01)','Agentes con herramientas (LLM06)'])],
   stat5='12+', statl5='escenarios de ataque deliberado (ISO27k Forum)',
   h6='Aprenderlas en 4 semanas', weeks=[('Semana 1','Mapa y vocabulario'),('Semana 2','Amenazas (NIST, OWASP, ATLAS)'),('Semana 3','Controles, con la norma'),('Semana 4','Aplicar a un sistema real')],
   h7='Investigar con evidencia', states=['Propuesto','Observado','Reproducido','Verificado'], note7='«No observado bajo estas condiciones», nunca «no es vulnerable».',
   h8='Guía y manual, abiertos', url='nullghost.io/ia-normas.html', meta8='Versión de trabajo v0.4 · revisión técnica pendiente',
   src='NullGhost Research. Fuentes: fichas públicas de ISO, NIST AI 100-2, OWASP, MITRE ATLAS. No se leyó el texto íntegro de las normas.'),
 'en': dict(bar='TWO ISO STANDARDS FOR AI',
   h1=['Two ISO standards', 'for AI'], s1='One says how to govern it. The other, how it gets attacked.', chips=['ISO/IEC 42001:2023', 'ISO/IEC 27090:2026'],
   h2='Two different questions', c2=[('ISO/IEC 42001:2023', 'AI management', 'Who decides, under which policy, and how is AI use controlled and improved?'),
                                     ('ISO/IEC 27090:2026', 'Threats to the system', 'Which threats exist at each lifecycle stage, and how are they detected and mitigated?')],
   h3='Inside ISO/IEC 42001', clauses=[('4','Context'),('5','Leadership'),('6','Planning'),('7','Support'),('8','Operation'),('9','Evaluation'),('10','Improvement')],
   note3='6.1.4 · the new piece: impact assessment on individuals, groups and society.',
   h4='Annex A, in numbers', n4=[('38','controls'),('9','objectives')], objs=['A.2 Policies','A.3 Organization','A.4 Resources','A.5 Impacts','A.6 Lifecycle','A.7 Data','A.8 Information','A.9 Use','A.10 Third parties'],
   note4='Structure per secondary sources; verify against the standard.',
   h5='ISO/IEC 27090: threats by phase', ph=[('Data and training',['Poisoning (LLM04)']),('Development and deployment',['Supply chain (LLM03)']),('Operation',['Inversion and leakage (LLM02)','Prompt injection (LLM01)','Agents with tools (LLM06)'])],
   stat5='12+', statl5='deliberate attack scenarios (ISO27k Forum)',
   h6='Learn them in 4 weeks', weeks=[('Week 1','Map and vocabulary'),('Week 2','Threats (NIST, OWASP, ATLAS)'),('Week 3','Controls, with the standard'),('Week 4','Apply to a real system')],
   h7='Investigate with evidence', states=['Proposed','Observed','Reproduced','Verified'], note7='“Not observed under these conditions,” never “not vulnerable.”',
   h8='Guide and manual, open', url='nullghost.io/en/ia-normas.html', meta8='Working version v0.4 · technical review pending',
   src='NullGhost Research. Sources: public ISO listings, NIST AI 100-2, OWASP, MITRE ATLAS. The standards were not read in full.'),
}

CSS = '''@font-face{font-family:Inter;src:url(../assets/inter.woff2) format("woff2");font-weight:100 900}
*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;background:#0a0f1a;color:#eaf1f8;font-family:Inter,sans-serif}
#main{position:relative;width:1920px;height:1080px;overflow:hidden;background:#0a0f1a}
.bar{position:absolute;left:96px;right:96px;top:70px;display:flex;align-items:center;justify-content:space-between;font-size:24px;letter-spacing:.14em;color:#6f8097;font-weight:700}
.bar img{width:46px;height:42px;opacity:.9}
.hair{position:absolute;left:96px;right:96px;top:128px;height:1px;background:rgba(130,160,200,.18)}
.src{position:absolute;left:96px;right:96px;bottom:66px;text-align:center;font-size:22px;color:#5e6f85}
.sc{position:absolute;inset:0;opacity:0}
.h{position:absolute;left:96px;right:96px;top:205px;font-size:72px;font-weight:800;letter-spacing:-.045em;line-height:1.02;margin:0}
.acc{color:#64a3ff}
/* s1 */
.t1{position:absolute;left:96px;top:360px;font-size:128px;font-weight:900;letter-spacing:-.055em;line-height:.98;margin:0}
.t1 span{display:block}
.s1t{position:absolute;left:96px;top:680px;font-size:42px;color:#9fb1c6;font-weight:500}
.chips{position:absolute;left:96px;top:780px;display:flex;gap:20px}
.chip{font-size:34px;font-weight:800;padding:16px 30px;border-radius:14px;border:1px solid #2f6ad1;background:#13233c;color:#cfe0f5}
/* s2 cards */
.c2{position:absolute;left:96px;top:340px;width:820px;height:520px;border-radius:20px;border:1px solid #243449;background:#101826;padding:44px 46px}
.c2 .r{font-size:30px;font-weight:800;color:#64a3ff}.c2 h3{font-size:56px;font-weight:800;letter-spacing:-.03em;margin:14px 0 26px}.c2 p{font-size:36px;line-height:1.3;color:#c3d0de;margin:0}
/* s3 clauses strip */
.strip{position:absolute;left:96px;right:96px;top:460px;display:flex;gap:14px}
.cl{flex:1;height:170px;border-radius:14px;border:1px solid #243449;background:#101826;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px}
.cl.k{border-color:#2f6ad1;background:#13233c}
.cl b{font-size:50px;font-weight:900;color:#64a3ff}.cl span{font-size:26px;color:#c3d0de;font-weight:600}
.cal{position:absolute;left:96px;right:96px;top:700px;padding:28px 34px;border-left:6px solid #64a3ff;background:#0f1d33;border-radius:0 16px 16px 0;font-size:38px;font-weight:650;line-height:1.25}
/* s4 numbers + tiles */
.nums{position:absolute;left:96px;top:420px;display:flex;gap:70px}
.nums .v{font-size:200px;font-weight:900;letter-spacing:-.06em;line-height:.85;color:#64a3ff}.nums .l{font-size:40px;color:#c3d0de;font-weight:600;margin-top:10px}
.tiles{position:absolute;left:820px;right:96px;top:430px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px}
.tile{height:120px;border-radius:14px;border:1px solid #243449;background:#101826;display:flex;align-items:center;justify-content:center;text-align:center;font-size:28px;font-weight:700;padding:0 12px}
/* s5 phases */
.cols{position:absolute;left:96px;right:96px;top:440px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px}
.col .ph{font-size:28px;font-weight:800;color:#9fb3c8;margin-bottom:16px;padding-bottom:10px;border-bottom:2px solid #243449}
.thr{border-radius:12px;background:#13233c;border:1px solid #2f5a99;padding:18px 22px;margin-bottom:14px;font-size:30px;font-weight:700;line-height:1.15}
.stat{position:absolute;left:96px;right:96px;top:900px;display:flex;align-items:center;gap:24px}
.stat .v{font-size:90px;font-weight:900;letter-spacing:-.05em;color:#64a3ff}.stat .l{font-size:32px;color:#c3d0de}
/* s6 weeks */
.wk{position:absolute;left:96px;right:96px;height:120px;border-radius:16px;border:1px solid #243449;background:#101826;display:flex;align-items:center;padding:0 36px;gap:30px;transform-origin:0 50%}
.wk .w{font-size:30px;font-weight:800;color:#64a3ff;white-space:nowrap}.wk b{font-size:40px;font-weight:700;letter-spacing:-.02em}
/* s7 states */
.st{position:absolute;left:96px;display:flex;align-items:center;gap:30px}
.st .n{width:96px;height:96px;flex:0 0 96px;border-radius:50%;border:4px solid #2f6ad1;background:#13233c;display:flex;align-items:center;justify-content:center;font-size:42px;font-weight:900;color:#64a3ff}
.st b{font-size:48px;font-weight:800;letter-spacing:-.02em}
.note7{position:absolute;left:96px;right:96px;top:900px;font-size:34px;color:#c3d0de;font-weight:600}
/* s8 close */
.h8{position:absolute;left:96px;top:380px;font-size:104px;font-weight:900;letter-spacing:-.05em;line-height:1;margin:0}
.u8{position:absolute;left:96px;top:620px;font-size:52px;font-weight:800;color:#64a3ff}
.m8{position:absolute;left:96px;top:720px;font-size:34px;color:#9fb1c6}
'''


def html(lang, c):
    s1 = (f'<h1 class="t1" id="t1">' + ''.join(f'<span>{E(x)}</span>' for x in c['h1']) + '</h1>'
          f'<div class="s1t" id="s1t">{E(c["s1"])}</div>'
          '<div class="chips" id="chips">' + ''.join(f'<div class="chip">{E(x)}</div>' for x in c['chips']) + '</div>')
    cards = ''
    for i,(r,t,p) in enumerate(c['c2']):
        cards += f'<div class="c2" id="c2{i}" style="left:{96 if i==0 else 1004}px"><div class="r">{E(r)}</div><h3>{E(t)}</h3><p>{E(p)}</p></div>'
    s2 = f'<h1 class="h" id="h2">{E(c["h2"])}</h1>{cards}'
    strip = '<div class="strip" id="strip">' + ''.join(f'<div class="cl{" k" if n=="6" else ""}" id="cl{i}"><b>{n}</b><span>{E(nm)}</span></div>' for i,(n,nm) in enumerate(c['clauses'])) + '</div>'
    s3 = f'<h1 class="h" id="h3">{E(c["h3"])}</h1>{strip}<div class="cal" id="cal">{E(c["note3"])}</div>'
    nums = '<div class="nums" id="nums">' + ''.join(f'<div><div class="v" id="n4{i}">0</div><div class="l">{E(l)}</div></div>' for i,(v,l) in enumerate(c['n4'])) + '</div>'
    tiles = '<div class="tiles" id="tiles">' + ''.join(f'<div class="tile">{E(o)}</div>' for o in c['objs']) + '</div>'
    s4 = f'<h1 class="h" id="h4">{E(c["h4"])}</h1>{nums}{tiles}<div class="src" style="bottom:120px;text-align:left" id="note4">{E(c["note4"])}</div>'
    cols = '<div class="cols" id="cols">'
    for i,(ph,thrs) in enumerate(c['ph']):
        cols += f'<div class="col" id="col{i}"><div class="ph">{E(ph)}</div>' + ''.join(f'<div class="thr">{E(t)}</div>' for t in thrs) + '</div>'
    cols += '</div>'
    s5 = f'<h1 class="h" id="h5">{E(c["h5"])}</h1>{cols}<div class="stat" id="stat"><div class="v">{E(c["stat5"])}</div><div class="l">{E(c["statl5"])}</div></div>'
    wks = ''.join(f'<div class="wk{" k" if i==2 else ""}" id="wk{i}" style="top:{440+i*135}px"><span class="w">{E(w)}</span><b>{E(t)}</b></div>' for i,(w,t) in enumerate(c['weeks']))
    s6 = f'<h1 class="h" id="h6">{E(c["h6"])}</h1>{wks}'
    sts = ''.join(f'<div class="st" id="st{i}" style="top:{420+i*120}px"><div class="n">{i+1}</div><b>{E(x)}</b></div>' for i,x in enumerate(c['states']))
    s7 = f'<h1 class="h" id="h7">{E(c["h7"])}</h1>{sts}<div class="note7" id="note7">{E(c["note7"])}</div>'
    s8 = f'<h1 class="h8" id="h8">{E(c["h8"])}</h1><div class="u8" id="u8">{E(c["url"])}</div><div class="m8" id="m8">{E(c["meta8"])}</div>'
    B = dict(s1=s1,s2=s2,s3=s3,s4=s4,s5=s5,s6=s6,s7=s7,s8=s8)
    secs = ''.join(f'<section class="sc" id="{k}">{B[k]}</section>' for k,_,_ in SCENES)
    body = (f'<div id="main" data-composition-id="main" data-width="1920" data-height="1080" data-duration="{DUR}">'
            f'<div class="bar"><span>NULLGHOST RESEARCH · {E(c["bar"])}</span><img src="../assets/ghost.svg" alt=""></div><div class="hair"></div>'
            f'{secs}<div class="src" id="src">{E(c["src"])}</div></div>')
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=1920,height=1080">'
            f'<title>NullGhost · ISO</title><script src="../assets/vendor/gsap.min.js"></script><style>{CSS}</style></head><body>'
            f'{body}<script>{JS}</script></body></html>')


JS = r'''
window.__timelines=window.__timelines||{};const tl=gsap.timeline({paused:true});
const ex='power3.out',sp='back.out(1.6)';
const show=(id,t)=>tl.set(id,{opacity:1},t),hide=(id,t)=>tl.to(id,{opacity:0,duration:.35},t);
const up=(s,t,st)=>tl.fromTo(s,{opacity:0,y:28},{opacity:1,y:0,duration:.5,ease:ex,stagger:st||0},t);
tl.fromTo('.bar',{opacity:0},{opacity:1,duration:.5},.1);tl.fromTo('.hair',{scaleX:0,transformOrigin:'0 50%'},{scaleX:1,duration:.6,ease:ex},.2);tl.fromTo('#src',{opacity:0},{opacity:1,duration:.5},.5);
const S={s1:0,s2:5,s3:11,s4:17.5,s5:23.5,s6:30,s7:35.5,s8:40.5};
const E_={s1:5,s2:11,s3:17.5,s4:23.5,s5:30,s6:35.5,s7:40.5};
show('#s1',0);tl.fromTo('#t1 span',{opacity:0,y:60,filter:'blur(8px)'},{opacity:1,y:0,filter:'blur(0px)',duration:.5,ease:ex,stagger:.14},.3);up('#s1t',1.3);up('#chips .chip',1.7,.18);hide('#s1',E_.s1-.3);
show('#s2',5);up('#h2',5.1);up('#c20',5.5);up('#c21',5.9);hide('#s2',E_.s2-.3);
show('#s3',11);up('#h3',11.1);tl.fromTo('#strip .cl',{opacity:0,y:20},{opacity:1,y:0,duration:.4,ease:ex,stagger:.1},11.5);up('#cal',13.6);hide('#s3',E_.s3-.3);
show('#s4',17.5);up('#h4',17.6);up('#nums',17.9);tl.fromTo('#n40',{innerText:0},{innerText:38,snap:{innerText:1},duration:1,ease:'power2.out'},18);tl.fromTo('#n41',{innerText:0},{innerText:9,snap:{innerText:1},duration:.8,ease:'power2.out'},18.3);up('#tiles .tile',18.4,.06);up('#note4',20.5);hide('#s4',E_.s4-.3);
show('#s5',23.5);up('#h5',23.6);up('#col0 .ph',23.9);up('#col1 .ph',24.0);up('#col2 .ph',24.1);tl.fromTo('#cols .thr',{opacity:0,y:20},{opacity:1,y:0,duration:.4,ease:ex,stagger:.14},24.3);up('#stat',27.8);hide('#s5',E_.s5-.3);
show('#s6',30);up('#h6',30.1);tl.fromTo('#s6 .wk',{opacity:0,scaleX:.4},{opacity:1,scaleX:1,duration:.5,ease:ex,stagger:.16},30.4);hide('#s6',E_.s6-.3);
show('#s7',35.5);up('#h7',35.6);for(let i=0;i<4;i++){up('#st'+i,35.9+i*.35);tl.fromTo('#st'+i+' .n',{scale:0},{scale:1,duration:.3,ease:sp},36+i*.35);}up('#note7',38.2);hide('#s7',E_.s7-.3);
show('#s8',40.5);up('#h8',40.7);up('#u8',41.2);up('#m8',41.5);
window.__timelines['main']=tl;
'''

for lang, c in COPY.items():
    (R / 'compositions' / f'iso-flat-{lang}.html').write_text(html(lang, c))
print('iso flat videos built')
