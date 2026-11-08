from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether, PageBreak
from reportlab.lib.enums import TA_LEFT

root=Path(__file__).resolve().parents[1]
src=root/'resume-public.md'
out=root/'dist/resume.pdf'
pdfmetrics.registerFont(TTFont('CN','/System/Library/Fonts/Supplemental/Arial Unicode.ttf'))
styles={
'body':ParagraphStyle('body',fontName='CN',fontSize=10.2,leading=15.3,spaceAfter=5,wordWrap='CJK',textColor=HexColor('#24303d')),
'name':ParagraphStyle('name',fontName='CN',fontSize=23,leading=29,spaceAfter=4,textColor=HexColor('#18334d')),
'section':ParagraphStyle('section',fontName='CN',fontSize=12,leading=17,spaceBefore=9,spaceAfter=5,textColor=HexColor('#18334d'),keepWithNext=True),
'company':ParagraphStyle('company',fontName='CN',fontSize=10,leading=15,spaceBefore=5,spaceAfter=4,keepWithNext=True,textColor=HexColor('#18334d')),
'sub':ParagraphStyle('sub',fontName='CN',fontSize=9.4,leading=14,spaceBefore=4,spaceAfter=4,keepWithNext=True,textColor=HexColor('#18334d')),
}
story=[]
for line in src.read_text().splitlines():
    line=line.strip()
    if not line: continue
    kind='body'
    if line.startswith('# '):kind='name';line=line[2:]
    elif line.startswith('### '):kind='company';line=line[4:]
    elif line.startswith('## '):
        kind='section';line=line[3:]
        if line=='项目经历':story.append(PageBreak())
    elif line.startswith('**') and line.endswith('**'):kind='sub'
    elif line.startswith('- '):line='• '+line[2:]
    line=re.sub(r'\*\*(.*?)\*\*',r'\1',line)
    line=re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',line)
    story.append(Paragraph(escape(line),styles[kind]))
doc=SimpleDocTemplate(str(out),pagesize=(595.28,841.89),rightMargin=37,leftMargin=37,topMargin=28,bottomMargin=25,title='张力 - Python开发与技术交付',author='张力')
doc.build(story)
print(out)
