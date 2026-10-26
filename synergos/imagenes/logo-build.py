# Genera el logo de Synergós: Fraunces (OFL) vectorizada, acento propio a 137,5 grados y muescas en los bordes.
import math, sys
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.boundsPen import BoundsPen

f = instantiateVariableFont(TTFont("fonts/Fraunces.ttf"), {"opsz":144,"wght":700,"SOFT":0,"WONK":1})
gs = f.getGlyphSet(); cmap = f.getBestCmap()
INK="#15191E"; MAG="#C2185B"
A = 137.5                      # ángulo áureo entre el acento y la línea base (lado izquierdo)
a = math.radians(180-A)        # 42,5 grados: inclinación del acento respecto a la horizontal
D = (math.cos(a), math.sin(a)) # dirección del acento (y hacia arriba, unidades de fuente)
N = (-math.sin(a), math.cos(a))# normal "arriba-izquierda"

def kern(g1,g2):
    for lk in f['GPOS'].table.LookupList.Lookup:
        for st in lk.SubTable:
            if lk.LookupType!=2: continue
            cov=st.Coverage.glyphs
            if g1 not in cov: continue
            if st.Format==1:
                for pv in st.PairSet[cov.index(g1)].PairValueRecord:
                    if pv.SecondGlyph==g2: return pv.Value1.XAdvance or 0
            else:
                v=st.Class1Record[st.ClassDef1.classDefs.get(g1,0)].Class2Record[st.ClassDef2.classDefs.get(g2,0)].Value1
                if v and v.XAdvance: return v.XAdvance
    return 0

def points(g):
    rp=DecomposingRecordingPen(gs); gs[g].draw(rp); pts=[]; cur=None
    for op,args in rp.value:
        if op in("moveTo","lineTo"): cur=args[0]; pts.append(cur)
        elif op in("qCurveTo","curveTo"):
            p0=cur; ctrl=list(args)
            for t in [i/12 for i in range(1,13)]:
                # muestreo lineal por tramos (suficiente para hallar extremos)
                pass
            for p in ctrl: pts.append(p)
            cur=ctrl[-1]
    return pts

word="Synergós"; glyphs=[]; x=0; prev=None
for ch in word:
    g = cmap[ord('o')] if ch=='ó' else cmap[ord(ch)]
    gadv = cmap[ord(ch)]
    if prev: x+=kern(prev,gadv)
    pen=SVGPathPen(gs); gs[g].draw(pen); bp=BoundsPen(gs); gs[g].draw(bp)
    glyphs.append(dict(ch=ch,x=x,d=pen.getCommands(),b=bp.bounds,pts=points(g)))
    x+=gs[gadv].width; prev=gadv
TOTAL=x; ASC=1500; DESC=520

def chip(gl, side, depth):
    """Quita una rebanada paralela al acento en el borde arriba-izquierda (side=+1) o abajo-derecha (side=-1)."""
    n=(N[0]*side, N[1]*side)
    ext=max(gl['pts'], key=lambda p: p[0]*n[0]+p[1]*n[1])
    cx=gl['x']+ext[0]-n[0]*depth; cy=ext[1]-n[1]*depth   # punto de la línea de corte
    # rectángulo grande cuyo borde inferior pasa por (cx,cy) y se extiende hacia n
    L=1200; y0 = -L if side>0 else 0
    return (f'<rect x="{-L}" y="{y0}" width="{2*L}" height="{L}" fill="black" '
            f'transform="translate({cx:.1f},{-cy:.1f}) rotate({-(180-A):.1f})"/>')

def accent(ox, otop, ocx):
    """Acento propio: cuña recta inclinada 42,5 grados. Devuelve (path, vértice)."""
    L=470; w0=80; w1=165            # longitud, grosor en la base y en la punta
    vx=ox+ocx+20; vy=otop+80         # vértice (extremo inferior)
    def P(t,w):                      # punto a distancia t sobre el eje, desplazado w/2 en la normal
        return (vx+D[0]*t - N[0]*w/2, vy+D[1]*t - N[1]*w/2), (vx+D[0]*t + N[0]*w/2, vy+D[1]*t + N[1]*w/2)
    (a1,a2)=P(0,w0); (b1,b2)=P(L,w1)
    path=f'M{a1[0]:.1f},{-a1[1]:.1f} L{b1[0]:.1f},{-b1[1]:.1f} L{b2[0]:.1f},{-b2[1]:.1f} L{a2[0]:.1f},{-a2[1]:.1f} Z'
    return path,(vx,vy)

def arc(v, r=290, sw=22, label=False):
    vx,vy=v
    p1=(vx-r, vy); p2=(vx+D[0]*r, vy+D[1]*r)   # desde la horizontal izquierda hasta el acento (137,5 grados)
    s=f'<path d="M{p1[0]:.1f},{-p1[1]:.1f} A{r},{r} 0 0 1 {p2[0]:.1f},{-p2[1]:.1f}" fill="none" stroke="{INK}" stroke-width="{sw}" stroke-linecap="round"/>'
    s+=f'<path d="M{vx-r-50:.0f},{-vy:.0f} L{vx+50:.0f},{-vy:.0f}" stroke="{INK}" stroke-width="{sw*0.6:.0f}" stroke-dasharray="34 34"/>'
    if label:
        s+=digits("137,5°", vx-r-20, vy+110, 0.10)
    return s

def digits(txt, x0, y0, sc):
    out=[]; x=0
    for ch in txt:
        g=cmap.get(ord(ch))
        if not g: continue
        pen=SVGPathPen(gs); gs[g].draw(pen)
        out.append(f'<path transform="translate({x0+x*sc:.1f},{-y0:.1f}) scale({sc},{-sc})" d="{pen.getCommands()}" fill="{INK}"/>')
        x+=gs[g].width
    return "".join(out)

def build(chips, depth, label=False, ink=INK, name="x"):
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-80 -{ASC} {TOTAL+160} {ASC+DESC}">']
    for i,gl in enumerate(glyphs):
        col = MAG if gl['ch'] in "gó" else ink
        x0,y0,x1,y1=gl['b']; m=f"m{name}{i}"
        out.append(f'<mask id="{m}"><rect x="{gl["x"]+x0-5:.0f}" y="{-y1-5:.0f}" width="{x1-x0+10:.0f}" height="{y1-y0+10:.0f}" fill="white"/>')
        if gl['ch'] in chips: out.append(chip(gl, chips[gl['ch']], depth))
        out.append('</mask>')
        out.append(f'<g mask="url(#{m})"><path transform="translate({gl["x"]},0) scale(1,-1)" d="{gl["d"]}" fill="{col}"/></g>')
    o=[g for g in glyphs if g['ch']=='ó'][0]; x0,y0,x1,y1=o['b']
    p,v=accent(o['x'], y1, (x0+x1)/2)
    out.append(f'<path d="{p}" fill="{MAG}"/>')
    out.append(arc(v, label=label).replace(INK, ink))
    out.append('</svg>')
    return "\n".join(out)

CH={'S':+1,'y':-1,'n':+1,'e':-1,'r':+1,'g':-1,'s':-1}
open("logo-synergos.svg","w").write(build(CH,130,name="a"))
open("logo-synergos-dark.svg","w").write(build(CH,130,ink="#F4F6F6",name="ad"))
open("logo-synergos-sin-muescas.svg","w").write(build({},0,name="d"))
print("ok")
