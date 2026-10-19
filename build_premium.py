#!/usr/bin/env python3
"""Genera la guía y el manual con el diseño editorial premium de NullGhost (HTML → PDF con Chrome).

Mismo contenido que build_pdf.py (content.py). Requiere Google Chrome instalado. Sin red: fuentes, listón y
logos salen de assets/. Cada página es de tamaño fijo; si algún bloque se sale de su página, el build falla
en vez de cortar texto en silencio.
"""
from pathlib import Path
from html import escape as E
import subprocess, sys, shutil, tempfile, re
from content import RESEARCH_GUIDE, MANUAL, SOURCES, VERSION, DATE_LABEL

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'assets'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

CSS = r'''
@font-face{font-family:Inter;src:url(premium/Inter-Variable.ttf) format('truetype-variations');font-weight:100 900}
@page{size:A4;margin:0}*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,Arial,sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact;color:#0E1B2E}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always}
/* portada */
.cover{background:#090D14;color:#fff}
.cover .rib{position:absolute;inset:0;background:url(premium/bg-ribbon.png) no-repeat;background-size:auto 66%;background-position:right -38mm bottom -8mm}
.cover .shade{position:absolute;inset:0;background:linear-gradient(180deg,#090D14 0%,rgba(9,13,20,.92) 42%,rgba(9,13,20,.12) 74%,rgba(9,13,20,.8) 100%),linear-gradient(90deg,#090D14 0%,rgba(9,13,20,0) 22%)}
.cover .in{position:absolute;inset:0;padding:20mm}
.cover .logo{height:9mm}
.cover .kick{margin-top:24mm;font-size:9pt;font-weight:600;letter-spacing:.2em;color:#85BCFF;text-transform:uppercase}
.cover h1{font-size:44pt;line-height:1;letter-spacing:-.045em;font-weight:760;margin-top:6mm}
.cover .sub{margin-top:8mm;width:142mm;font-size:12.5pt;line-height:1.5;color:#C9D6E6}
.cover .iso{margin-top:8mm;font-size:9pt;font-weight:650;color:#85BCFF;letter-spacing:.08em}
.cover .steps{position:absolute;left:20mm;bottom:40mm}
.cover .steps .lbl{font-size:7.5pt;letter-spacing:.2em;color:#85BCFF;font-weight:700}
.cover .steps div{margin-top:2.6mm;font-size:10pt;color:#DCE6F2}
.cover .steps b{color:#85BCFF;font-weight:700;margin-right:3mm}
.cover .meta{position:absolute;left:20mm;right:20mm;bottom:17mm;display:flex;justify-content:space-between;font-size:8.5pt;color:#A5B6C9;border-top:1px solid rgba(255,255,255,.16);padding-top:4mm}
/* interiores */
.paper{background:#FBFCFE}
.band{position:absolute;left:0;top:0;bottom:0;width:6.5mm;background:linear-gradient(180deg,#1557A6,#64A3FF)}
.pi{position:absolute;left:25mm;right:19mm;top:15mm;bottom:21mm}
.hd{display:flex;justify-content:space-between;align-items:center;font-size:7.3pt;letter-spacing:.14em;color:#6B7F96;text-transform:uppercase;padding-bottom:3.5mm;border-bottom:1px solid #DCE5EF}
.hd img{height:5.6mm}
.titlerow{display:flex;gap:6mm;margin-top:9mm;align-items:flex-start}
.num{font-size:58pt;font-weight:800;letter-spacing:-.06em;color:#1557A6;line-height:.84}
.eyebrow{font-size:7.3pt;letter-spacing:.18em;color:#1557A6;font-weight:700;text-transform:uppercase}
h2{font-size:21pt;letter-spacing:-.03em;line-height:1.1;font-weight:740;color:#0E1B2E;margin-top:1.2mm}
.body{margin-top:6.5mm}
.body p{font-size:10.1pt;line-height:1.58;color:#33465E;margin-bottom:3.6mm}
.body h3{font-size:12.2pt;letter-spacing:-.01em;font-weight:720;color:#0E1B2E;margin:5.5mm 0 2.4mm}
table{width:100%;border-collapse:collapse;font-size:8.9pt;margin:2mm 0 5mm}
th{text-align:left;font-size:6.9pt;letter-spacing:.14em;text-transform:uppercase;color:#1557A6;font-weight:700;padding:0 3mm 2.4mm 0;border-bottom:1.4px solid #1557A6}
td{padding:2.7mm 3mm 2.7mm 0;border-bottom:1px solid #E3EAF2;line-height:1.48;vertical-align:top;color:#33465E}
td:first-child{font-weight:650;color:#0E1B2E}
table.c2 td:first-child{width:36%}
table.c3 td:first-child{width:27%}table.c3 td:nth-child(2){width:37%}
.call{margin:3mm 0 5mm;background:#090D14;color:#fff;border-radius:3.2mm;padding:5mm 6.5mm;position:relative;overflow:hidden}
.call:after{content:"";position:absolute;right:-22mm;top:-14mm;width:72mm;height:52mm;background:url(premium/bg-ribbon.png) no-repeat;background-size:cover;opacity:.32}
.call .t{position:relative;font-size:7pt;letter-spacing:.18em;color:#85BCFF;font-weight:700}
.call p{position:relative;margin-top:1.8mm;font-size:9.7pt;line-height:1.55;color:#E6EEF8;width:86%}
.steps{margin:1.5mm 0 4mm}
.step{display:flex;gap:4mm;margin-bottom:3.4mm}
.step .n{flex:none;width:7mm;height:7mm;border-radius:50%;background:#1557A6;color:#fff;font-size:8.5pt;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:.4mm}
.step b{display:block;font-size:10.4pt;font-weight:700;color:#0E1B2E;letter-spacing:-.01em}
.step span{display:block;margin-top:.8mm;font-size:9.6pt;line-height:1.52;color:#33465E}
.rel{margin:2mm 0 5mm;background:#090D14;border-radius:3.2mm;padding:5mm;position:relative;overflow:hidden}
.rel:after{content:"";position:absolute;right:-30mm;bottom:-30mm;width:90mm;height:60mm;background:url(premium/bg-ribbon.png) no-repeat;background-size:cover;opacity:.22}
.rel .boxes{position:relative;display:flex;gap:3mm}
.rel .bx{flex:1;border:1px solid rgba(133,188,255,.35);background:rgba(21,87,166,.16);border-radius:2.5mm;padding:3.5mm;text-align:center}
.rel .bx b{display:block;font-size:9.4pt;color:#fff}
.rel .bx span{display:block;margin-top:1.4mm;font-size:8pt;line-height:1.4;color:#AAC3DD}
.rel .voc{position:relative;margin-top:4mm;padding-top:3mm;border-top:1px dashed rgba(133,188,255,.35);text-align:center;font-size:8.3pt;color:#85BCFF}
pre{margin:2mm 0 4.5mm;background:#090D14;color:#85BCFF;border-radius:3mm;padding:4.5mm 5.5mm;font:8.6pt/1.55 Menlo,monospace;white-space:pre}
.src{margin-bottom:3.2mm}
.src b{font-size:9.6pt;color:#0E1B2E}
.src span{display:block;margin-top:.6mm;font-size:8.4pt;line-height:1.45;color:#52667D}
.src a{font-size:8.2pt;color:#1557A6;text-decoration:none}
.ft{position:absolute;left:25mm;right:19mm;bottom:10mm;display:flex;justify-content:space-between;font-size:7.3pt;color:#8A9BB0}
.ft b{color:#1557A6}
.OVERFLOW{color:red}
'''

def block(b):
    t = b[0]
    if t == 'p':
        return f'<p>{E(b[1])}</p>'
    if t == 'heading':
        return f'<h3>{E(b[1])}</h3>'
    if t == 'callout':
        return f'<div class="call"><div class="t">{E(b[1])}</div><p>{E(b[2])}</p></div>'
    if t == 'table':
        cls = 'c2' if len(b[1]) == 2 else 'c3'
        head = ''.join(f'<th>{E(h)}</th>' for h in b[1])
        rows = ''.join('<tr>' + ''.join(f'<td>{E(c)}</td>' for c in r) + '</tr>' for r in b[2])
        return f'<table class="{cls}"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>'
    if t == 'steps':
        return '<div class="steps">' + ''.join(
            f'<div class="step"><div class="n">{i}</div><div><b>{E(a)}</b><span>{E(x)}</span></div></div>'
            for i, (a, x) in enumerate(b[1], 1)) + '</div>'
    if t == 'code':
        return f'<pre>{E(b[1])}</pre>'
    if t == 'relation':
        boxes = [('ISO/IEC 42001', 'Gobernar: política, roles, riesgo, impacto y mejora'),
                 ('ISO/IEC 27090', 'Proteger: amenazas a la IA en todo su ciclo de vida'),
                 ('ISO/IEC 27001 / 27002', 'Seguridad de la información de la organización')]
        inner = ''.join(f'<div class="bx"><b>{E(a)}</b><span>{E(x)}</span></div>' for a, x in boxes)
        return (f'<div class="rel"><div class="boxes">{inner}</div><div class="voc">Vocabulario abierto para estudiar: '
                f'NIST AI 100-2 · OWASP Top 10 para LLM · MITRE ATLAS</div></div>')
    if t == 'sources':
        return ''.join(f'<div class="src"><b>[{E(i)}] {E(ti)}</b><span>{E(n)}</span><a href="{E(u)}">{E(u)}</a></div>'
                       for i, ti, n, u in SOURCES)
    raise ValueError(t)

def doc_html(d):
    total = len(d['pages']) + 1
    is_guide = d is RESEARCH_GUIDE
    run = ('Guía de investigación' if is_guide else 'Manual de buenas prácticas') + ' · ' + VERSION
    foot = 'NullGhost · ' + ('Gestión y seguridad de IA con ISO' if is_guide else 'Manual de buenas prácticas de IA')
    title_html = '<br>'.join(E(x) for x in d['title'].split('\n'))
    steps = ''.join(f'<div><b>{i:02d}</b>{E(s)}</div>' for i, s in enumerate(d['cover_steps'], 1))
    pages = [f'''<section class="page cover"><div class="rib"></div><div class="shade"></div><div class="in">
<img class="logo" src="brand/nullghost-horizontal-reverse.svg" alt="NullGhost">
<div class="kick">{E(d['kind'])} · {VERSION}</div><h1>{title_html}</h1>
<p class="sub">{E(d['subtitle'])}</p><div class="iso">{E(d['cover_iso'])}</div>
<div class="steps"><div class="lbl">UNA RUTA DE TRABAJO</div>{steps}</div>
<div class="meta"><span>Ricardo Martínez · NullGhost Research</span><span>{DATE_LABEL} · {total:02d} páginas</span></div>
</div></section>''']
    for i, (num, title, items) in enumerate(d['pages'], 2):
        eyebrow = 'Investigación' if is_guide else 'Aplicación'
        pages.append(f'''<section class="page paper"><div class="band"></div><div class="pi">
<div class="hd"><img src="brand/nullghost-horizontal-light.svg" alt="NullGhost"><span>{E(run)}</span></div>
<div class="titlerow"><div class="num">{num}</div><div><div class="eyebrow">{eyebrow}</div><h2>{E(title)}</h2></div></div>
<div class="body">{''.join(block(b) for b in items)}</div></div>
<div class="ft"><span>{E(foot)}</span><span><b>{i:02d}</b> / {total:02d}</span></div></section>''')
    # Detecta desbordes: si el contenido pasa del área útil, deja una marca de texto que el build busca en el PDF.
    check = '''<script>for(const p of document.querySelectorAll('.paper .pi')){const b=p.querySelector('.body');
const lim=p.getBoundingClientRect().bottom;const r=b.getBoundingClientRect().bottom;
if(r>lim+1){const m=document.createElement('div');m.className='OVERFLOW';m.textContent='OVERFLOW_'+Math.round(r-lim);m.style.cssText='position:absolute;top:0;left:0;font-size:9pt';p.prepend(m);}}</script>'''
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{E(d["title"].replace(chr(10), " "))}</title>'
            f'<style>{CSS}</style></head><body>{"".join(pages)}{check}</body></html>')

def build(d):
    out = ROOT / d['directory'] / d['filename']
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        shutil.copytree(ASSETS / 'premium', tmp / 'premium')
        shutil.copytree(ASSETS / 'brand', tmp / 'brand')
        page = tmp / 'doc.html'
        page.write_text(doc_html(d), encoding='utf-8')
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', '--virtual-time-budget=4000',
                        f'--print-to-pdf={out}', page.as_uri()], check=True, capture_output=True)
    text = subprocess.run(['pdftotext', str(out), '-'], capture_output=True, text=True).stdout
    pages = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', str(out)], capture_output=True, text=True).stdout).group(1))
    over = re.findall(r'OVERFLOW_\d+', text)
    expected = len(d['pages']) + 1
    print(d['filename'], 'páginas', pages, 'esperadas', expected, 'desbordes', over or 'ninguno')
    from build_pdf import markdown
    out.with_suffix('.md').write_text(markdown(d), encoding='utf-8')
    if over or pages != expected:
        sys.exit(f'Fallo de maquetación en {d["filename"]}: {over} / {pages} páginas')

if __name__ == '__main__':
    for d in (RESEARCH_GUIDE, MANUAL):
        build(d)
