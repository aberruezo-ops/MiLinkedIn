# Utilidades de maquetacion comunes (copiadas del volumen II).
import os
from escenas import *

CSS = """
@font-face{font-family:'Fraunces';font-weight:400;src:url('fonts/fraunces-latin-400-normal.woff2')}
@font-face{font-family:'Fraunces';font-weight:600;src:url('fonts/fraunces-latin-600-normal.woff2')}
@font-face{font-family:'Fraunces';font-weight:700;src:url('fonts/fraunces-latin-700-normal.woff2')}
@font-face{font-family:'Fraunces';font-weight:600;font-style:italic;src:url('fonts/fraunces-latin-600-italic.woff2')}
@font-face{font-family:'Fredoka';font-weight:600;src:url('fonts/fredoka-latin-600-normal.woff2')}
@font-face{font-family:'Fredoka';font-weight:700;src:url('fonts/fredoka-latin-700-normal.woff2')}
@font-face{font-family:'Nunito';font-weight:400;src:url('fonts/nunito-latin-400-normal.woff2')}
@font-face{font-family:'Nunito';font-weight:700;src:url('fonts/nunito-latin-700-normal.woff2')}
@page{size:8.5in 11in;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#fff;color:#111;font-family:'Nunito',sans-serif}
.page{width:8.5in;height:11in;padding:.4in;position:relative;overflow:hidden;page-break-after:always;break-after:page}
.art svg{display:block;margin:0 auto}
.txt{margin-top:.08in;text-align:center;padding:0 .15in}
.txt p{margin:0;font-family:'Fraunces',serif;font-weight:600;font-size:16.5pt;line-height:1.38}
h1,h2,h3{font-family:'Fraunces',serif;font-weight:700;margin:0}
.note h2{font-size:27pt;margin-bottom:.18in}
.note h3{font-size:17pt;margin:.18in 0 .05in}
.note p,.note li{font-size:13.5pt;line-height:1.42;margin:.05in 0}
.note ul,.note ol{margin:.04in 0;padding-left:.28in}
.note .legal{position:absolute;left:.5in;right:.5in;bottom:.5in;font-size:9.5pt;line-height:1.4;border-top:2px solid #111;padding-top:.1in}
.center{text-align:center}
.line{border-bottom:3px solid #111;height:.5in;margin:.05in 0}
"""

SVGW = 7.1


def svg(inner, vb, marco=False, wi=None):
    w, h = [float(v) for v in vb.split()[2:]]
    ww = wi or SVGW
    if marco:
        r = f'x="8" y="8" width="{w - 16:.0f}" height="{h - 16:.0f}" rx="28"'
        inner = (f'<defs><clipPath id="c"><rect {r}/></clipPath>'
                 f'<filter id="w" x="-2%" y="-2%" width="104%" height="104%"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="7" result="n"/>'
                 f'<feDisplacementMap in="SourceGraphic" in2="n" scale="3.2"/></filter></defs>'
                 f'<g clip-path="url(#c)"><g filter="url(#w)">{inner}</g></g>'
                 f'<rect {r} fill="none" stroke="#111" stroke-width="4.2"/>')
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" style="width:{ww}in;height:{ww * h / w:.3f}in">{inner}</svg>'


def pag(html, cls=''):
    return f'<section class="page {cls}">{html}</section>'


BLANCO = pag('')
PAW = ('<svg viewBox="0 0 60 50" style="height:.28in;display:block;margin:0 auto .02in"><g fill="#fff" stroke="#111" stroke-width="3">'
       '<ellipse cx="30" cy="34" rx="14" ry="11"/><ellipse cx="12" cy="20" rx="6" ry="8"/><ellipse cx="25" cy="10" rx="6" ry="8"/>'
       '<ellipse cx="38" cy="10" rx="6" ry="8"/><ellipse cx="50" cy="20" rx="6" ry="8"/></g></svg>')


