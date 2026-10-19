#!/usr/bin/env python3
"""Build original NullGhost research PDFs. Python 3 + reportlab. No network."""
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from content import PAPER, GUIDE, SOURCES
import math,sys
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'paper/es';OUT.mkdir(parents=True,exist_ok=True)
W,H=595.276,841.89;M=48;CW=W-2*M
NAVY=HexColor('#081322');INK=HexColor('#12243A');BLUE=HexColor('#0066DA');CYAN=HexColor('#65BCFF');MUTED=HexColor('#52667D');LINE=HexColor('#DCE5EF');PAPERBG=HexColor('#FAFCFF')
font_root=Path('/System/Library/Fonts/Supplemental')
if (font_root/'Arial.ttf').exists():
 for n,f in [('Body','Arial.ttf'),('Strong','Arial Bold.ttf'),('Italic','Arial Italic.ttf')]:pdfmetrics.registerFont(TTFont(n,str(font_root/f)))
else:
 # Portable PDF core fonts. For exactly the same build, install Arial or set this path.
 for n,f in [('Body','Helvetica'),('Strong','Helvetica-Bold'),('Italic','Helvetica-Oblique')]:pdfmetrics.registerFont(pdfmetrics.Font(n,f,'WinAnsiEncoding'))
styles={
 'body':ParagraphStyle('body',fontName='Body',fontSize=10.5,leading=15.4,textColor=INK,spaceAfter=10),
 'heading':ParagraphStyle('heading',fontName='Strong',fontSize=14.5,leading=18.5,textColor=INK,spaceAfter=8),
 'small':ParagraphStyle('small',fontName='Body',fontSize=9,leading=13,textColor=MUTED),
 'cell':ParagraphStyle('cell',fontName='Body',fontSize=9,leading=12.6,textColor=INK),
 'th':ParagraphStyle('th',fontName='Strong',fontSize=8.6,leading=12,textColor=white),
 'callout':ParagraphStyle('callout',fontName='Body',fontSize=11,leading=16,textColor=INK),
 'white':ParagraphStyle('white',fontName='Body',fontSize=15,leading=22,textColor=HexColor('#C3D8EE'))}

def para(c,text,x,y,width=CW,style='body'):
 p=Paragraph(escape(text).replace('\n','<br/>'),styles[style]);_,h=p.wrap(width,1000);p.drawOn(c,x,y-h);return y-h

def wordmark(c,x,y,color=INK):
 c.setFillColor(color)
 # Small original geometric ghost mark accompanying the NullGhost wordmark.
 p=c.beginPath();p.moveTo(x,y-1);p.lineTo(x,y+7);p.curveTo(x,y+20,x+24,y+20,x+24,y+7);p.lineTo(x+24,y-1);p.lineTo(x+18,y+2);p.lineTo(x+12,y-1);p.lineTo(x+6,y+2);p.close();c.drawPath(p,fill=1,stroke=0)
 c.setFillColor(NAVY if color==white else white);c.circle(x+8,y+8,2,fill=1,stroke=0);c.circle(x+16,y+8,2,fill=1,stroke=0)
 c.setFillColor(color);c.setFont('Strong',16);c.drawString(x+32,y,'nullghost')

def cover(c,d,total):
 c.setFillColor(NAVY);c.rect(0,0,W,H,fill=1,stroke=0)
 c.setStrokeColor(HexColor('#102D4C'))
 for r in (115,165,215,265):c.circle(W-18,250,r,fill=0,stroke=1)
 c.setStrokeColor(BLUE);c.setLineWidth(1.5);c.circle(W-18,250,165,stroke=1,fill=0)
 c.setFillColor(CYAN);c.circle(W-18-165,250,4,fill=1,stroke=0)
 wordmark(c,M,H-70,white)
 c.setFillColor(CYAN);c.setFont('Strong',9);c.drawString(M,H-126,d['kind'])
 y=H-174
 c.setFillColor(white);c.setFont('Strong',43)
 for line in d['title'].split('\n'):c.drawString(M,y,line);y-=48
 y-=15;y=para(c,d['subtitle'],M,y,CW-30,'white')
 y-=28;c.setStrokeColor(HexColor('#2E4660'));c.line(M,y,W-M,y)
 y-=22
 c.setFillColor(CYAN);c.setFont('Strong',10);c.drawString(M,y,'ISO/IEC 42001:2023  +  ISO/IEC 27090:2026')
 para(c,d['cover_note'],M,y-24,CW-70,'white')
 c.setFillColor(HexColor('#A4BDD6'));c.setFont('Body',10);c.drawString(M,92,'Ricardo Martínez · NullGhost Research')
 c.setFont('Body',9);c.drawString(M,72,'19 OCT 2026   /   v0.1 · BORRADOR PÚBLICO')
 c.setFillColor(CYAN);c.drawRightString(W-M,72,f'{total:02d} PÁGINAS')
 c.bookmarkPage('cover');c.addOutlineEntry('Portada','cover');c.showPage()

def chrome(c,d,n,total,num,title):
 c.setFillColor(PAPERBG);c.rect(0,0,W,H,fill=1,stroke=0)
 c.setFillColor(BLUE);c.rect(0,H-6,W,6,fill=1,stroke=0)
 wordmark(c,M,H-52)
 c.setFillColor(MUTED);c.setFont('Body',8);c.drawRightString(W-M,H-46,'RESEARCH / IA   ·   v0.1')
 c.setStrokeColor(LINE);c.line(M,47,W-M,47)
 c.setFillColor(MUTED);c.setFont('Body',8);c.drawString(M,31,'Propuesta de NullGhost · Sin conformidad demostrada')
 c.setFont('Strong',9);c.drawRightString(W-M,31,f'{n:02d} / {total:02d}')
 c.setFillColor(BLUE);c.setFont('Strong',9);c.drawString(M,H-93,num+' / '+('INVESTIGACIÓN' if d is PAPER else 'APLICACIÓN'))
 title_style=ParagraphStyle('title',fontName='Strong',fontSize=26,leading=30,textColor=INK)
 p=Paragraph(escape(title),title_style);_,h=p.wrap(CW,100);p.drawOn(c,M,H-114-h)
 c.bookmarkPage('p'+num);c.addOutlineEntry(title,'p'+num)
 return H-114-h-24

def table(c,headers,rows,y):
 cols=len(headers)
 widths=([CW*.33,CW*.67] if cols==2 else [CW*.24,CW*.38,CW*.38])
 items=[[Paragraph(escape(v),styles['th']) for v in headers]]+[[Paragraph(escape(v),styles['cell']) for v in row] for row in rows]
 t=Table(items,colWidths=widths,hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),NAVY),('ROWBACKGROUNDS',(0,1),(-1,-1),[white,HexColor('#EDF3FA')]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),11),('RIGHTPADDING',(0,0),(-1,-1),11),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9),('LINEBELOW',(0,1),(-1,-1),.35,LINE)]))
 _,h=t.wrap(CW,900);t.drawOn(c,M,y-h);return y-h-17

def architecture(c,y):
 h=155;c.setFillColor(NAVY);c.roundRect(M,y-h,CW,h,9,fill=1,stroke=0)
 labels=['OPERADOR','POLÍTICA','MCP / VM','EVIDENCIA'];x=M+14;bw=106;gap=15
 for i,label in enumerate(labels):
  xx=x+i*(bw+gap);c.setStrokeColor(HexColor('#3C6085'));c.setFillColor(HexColor('#122942'));c.roundRect(xx,y-66,bw,34,4,fill=1,stroke=1);c.setFillColor(white);c.setFont('Strong',8.5);c.drawCentredString(xx+bw/2,y-52,label)
  if i<3:
   c.setStrokeColor(CYAN);c.line(xx+bw+2,y-49,xx+bw+gap-2,y-49)
 c.setFillColor(CYAN);c.setFont('Body',9);c.drawString(M+18,y-94,'Autoriza              Restringe                Ejecuta                  Conserva')
 c.setStrokeColor(HexColor('#3C6085'));c.setDash(3,3);c.line(M+18,y-111,W-M-18,y-111);c.setDash()
 c.setFillColor(HexColor('#AAC3DD'));c.setFont('Body',8.5);c.drawString(M+18,y-133,'Revisión humana: contexto, resultado, límites y decisión de publicación.')
 return y-h-18

def blocks(c,items,y):
 for b in items:
  typ=b[0]
  if typ=='p':y=para(c,b[1],M,y)-11
  elif typ=='heading':y=para(c,b[1],M,y-3,style='heading')-8
  elif typ=='table':y=table(c,b[1],b[2],y)
  elif typ=='diagram':y=architecture(c,y)
  elif typ=='callout':
   p=Paragraph(escape(b[2]),styles['callout']);_,h=p.wrap(CW-30,900);height=h+45
   c.setFillColor(HexColor('#E8F2FF'));c.roundRect(M,y-height,CW,height,6,fill=1,stroke=0);c.setFillColor(BLUE);c.rect(M,y-height,3,height,fill=1,stroke=0);c.setFont('Strong',8.5);c.drawString(M+15,y-18,b[1]);p.drawOn(c,M+15,y-33-h);y-=height+18
  elif typ=='steps':
   for i,(label,text) in enumerate(b[1],1):
    c.setFillColor(BLUE);c.circle(M+10,y-10,10,fill=1,stroke=0);c.setFillColor(white);c.setFont('Strong',9);c.drawCentredString(M+10,y-13,str(i))
    y=para(c,label,M+29,y,CW-29,'heading')-4;y=para(c,text,M+29,y,CW-29)-13
  elif typ=='code':
   lines=b[1].split('\n');hh=len(lines)*13+24;c.setFillColor(NAVY);c.roundRect(M,y-hh,CW,hh,5,fill=1,stroke=0);c.setFillColor(CYAN);c.setFont('Courier',9)
   for i,line in enumerate(lines):c.drawString(M+14,y-20-i*13,line)
   y-=hh+16
  elif typ=='sources':
   for ident,title,note,url in SOURCES:
    y=para(c,f'[{ident}] {title}',M,y,style='heading')-3;y=para(c,note,M,y,style='small')-5
    link=Paragraph(f'<link href="{url}" color="#0066DA">{escape(url)}</link>',styles['small']);_,hh=link.wrap(CW,200);link.drawOn(c,M,y-hh);y-=hh+15
   y=para(c,'Consulta de fuentes: 19 de octubre de 2026. No se redistribuyen las normas.',M,y,style='small')-15
  if y<67:raise RuntimeError(f'Page overflow: y={y:.1f}, block={typ}')
 return y

def markdown(d):
 lines=['# '+d['title'].replace('\n',' '),'',d['subtitle'],'','> v0.1 · Borrador público · 19 de octubre de 2026','',d['cover_note'],'']
 for num,title,items in d['pages']:
  lines+=['## '+num+' · '+title,'']
  for b in items:
   if b[0] in ('p','heading'):lines += [('### ' if b[0]=='heading' else '')+b[1],'']
   elif b[0]=='callout':lines += ['> **'+b[1]+'.** '+b[2],'']
   elif b[0]=='table':
    lines+=['| '+' | '.join(b[1])+' |','| '+' | '.join('---' for _ in b[1])+' |']+['| '+' | '.join(row)+' |' for row in b[2]]+['']
   elif b[0]=='steps':lines += [f'{i}. **{t}.** {v}' for i,(t,v) in enumerate(b[1],1)]+['']
   elif b[0]=='code':lines+=['```json',b[1],'```','']
   elif b[0]=='diagram':lines+=['Operador → Política de alcance → MCP / VM → Evidencia. Revisión humana transversal.','']
   elif b[0]=='sources':lines += [f'[{i}] [{t}]({u}). {n}' for i,t,n,u in SOURCES]+['']
 return '\n'.join(lines)

def build(d):
 path=OUT/d['filename'];total=len(d['pages'])+1
 c=canvas.Canvas(str(path),pagesize=(W,H),pageCompression=1,invariant=1)
 c.setTitle(d['title'].replace('\n',' '));c.setAuthor('Ricardo Martínez / NullGhost Research');c.setSubject('Propuesta conceptual v0.1; sin conformidad demostrada')
 cover(c,d,total)
 for i,(num,title,items) in enumerate(d['pages'],2):
  y=chrome(c,d,i,total,num,title);last=blocks(c,items,y);print(d['filename'],i,'bottom',round(last));c.showPage()
 c.save();path.with_suffix('.md').write_text(markdown(d),encoding='utf-8')
for d in (PAPER,GUIDE):build(d)
