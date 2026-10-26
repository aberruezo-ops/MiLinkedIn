import math, sys
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

f = TTFont("fonts/Fraunces.ttf")
f = instantiateVariableFont(f, {"opsz":144, "wght":700, "SOFT":0, "WONK":1})
gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f['head'].unitsPerEm
word = "Synergós"
glyphs = []
x = 0
# GPOS pair kerning (simple lookup)
def kern(a,b):
    try:
        gpos=f['GPOS'].table
        for lk in gpos.LookupList.Lookup:
            for st in lk.SubTable:
                if getattr(st,'LookupType',lk.LookupType)==2 and st.Format==1:
                    cov=st.Coverage.glyphs
                    if a in cov:
                        ps=st.PairSet[cov.index(a)]
                        for pv in ps.PairValueRecord:
                            if pv.SecondGlyph==b: return pv.Value1.XAdvance or 0
                elif getattr(st,'LookupType',lk.LookupType)==2 and st.Format==2:
                    if a in st.Coverage.glyphs:
                        c1=st.ClassDef1.classDefs.get(a,0); c2=st.ClassDef2.classDefs.get(b,0)
                        v=st.Class1Record[c1].Class2Record[c2].Value1
                        if v and v.XAdvance: return v.XAdvance
    except Exception as e: pass
    return 0
prev=None
for ch in word:
    g = cmap[ord(ch)]
    if prev: x += kern(prev,g)
    pen = SVGPathPen(gs); gs[g].draw(pen)
    bp = BoundsPen(gs); gs[g].draw(bp)
    glyphs.append((ch, g, x, pen.getCommands(), bp.bounds))
    x += gs[g].width; prev=g
total = x
asc, desc = 1480, 520  # visual box
H = asc+desc
ink = "#15191E"; mag = sys.argv[1] if len(sys.argv)>1 else "#C2185B"
ANG = 137.5  # golden angle between the cut line and the baseline (its complement is 42.5)
def cut_rect(cx, cy, w, h):
    # rectangle centred at cx,cy (font units, y up), rotated so its long side runs at 42.5 deg from horizontal (= 137.5 from the other side)
    return f'<rect x="{cx-w/2:.0f}" y="{-cy-h/2:.0f}" width="{w:.0f}" height="{h:.0f}" transform="rotate({(180-ANG):.1f} {cx:.0f} {-cy:.0f})" fill="black"/>'
def svg(cuts, name, label, ink=ink):
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -{asc} {total} {H}" width="{total/10:.0f}" height="{H/10:.0f}">']
    out.append(f'<mask id="m{name}"><rect x="0" y="-{asc}" width="{total}" height="{H}" fill="white"/>')
    out += cuts
    out.append('</mask>')
    out.append(f'<g mask="url(#m{name})">')
    for ch,g,gx,d,b in glyphs:
        col = mag if ch in "gó" else ink
        out.append(f'<path transform="translate({gx},0) scale(1,-1)" d="{d}" fill="{col}"/>')
    out.append('</g></svg>')
    return "\n".join(out)

G = {ch:(gx,b) for ch,g,gx,d,b in glyphs}
def c(ch, fx, fy, w=90, h=900):
    gx,(x0,y0,x1,y1) = G[ch]
    return cut_rect(gx + x0 + (x1-x0)*fx, y0 + (y1-y0)*fy, w, h)
# fine-tune positions by inspection (fractions of glyph bbox)
variants = {
 "I": ([c('S',0.5,0.5,70,420), c('n',0.2,0.5,70,330), c('g',0.17,0.66,70,330), c('s',0.5,0.5,70,330)], ""),
 "J": ([c('S',0.5,0.5,70,420), c('n',0.2,0.5,70,330), c('g',0.2,0.14,70,330), c('s',0.5,0.5,70,330)], ""),
 "K": ([c('S',0.5,0.5,70,420), c('g',0.17,0.66,70,330), c('s',0.5,0.5,70,330)], ""),

 "E": ([c('S',0.5,0.5,70,420), c('g',0.5,0.47,70,380), c('s',0.5,0.5,70,330)], ""),
 "F": ([c('S',0.5,0.5,70,420), c('n',0.2,0.5,70,330), c('g',0.5,0.47,70,380), c('s',0.5,0.5,70,330)], ""),
 "G": ([c('S',0.5,0.5,70,420), c('s',0.5,0.5,70,330)], ""),
 "H": ([c('S',0.5,0.5,70,420), c('y',0.62,0.55,70,330), c('r',0.2,0.5,70,330), c('g',0.5,0.47,70,380), c('s',0.5,0.5,70,330)], ""),

 "A": ([c('S',0.5,0.5), c('g',0.5,0.52), c('s',0.5,0.5)], "Tres cortes: S, g, s"),
 "B": ([c('S',0.5,0.5), c('n',0.22,0.5), c('g',0.5,0.52), c('s',0.5,0.5)], "Cuatro cortes: S, n, g, s"),
 "C": ([c('S',0.5,0.5), c('y',0.5,0.45), c('e',0.5,0.5), c('g',0.5,0.52), c('s',0.5,0.5)], "Cinco cortes alternos"),
 "D": ([c('S',0.5,0.5,70,900), c('g',0.5,0.52,70,900)], "Dos cortes finos: S y g"),
}
import json
for k,(cuts,label) in variants.items():
    open(f"logo-fraunces-{k}.svg","w").write(svg(cuts,k,label))
open("logo-fraunces-I-dark.svg","w").write(svg(variants["I"][0],"Id","",ink="#F4F6F6"))
open("logo-fraunces-0.svg","w").write(svg([], "0", "sin cortes"))
print(total, {ch:(gx,b) for ch,g,gx,d,b in glyphs})
