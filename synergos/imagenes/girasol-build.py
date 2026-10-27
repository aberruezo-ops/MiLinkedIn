# Genera imágenes de semillas de girasol con el modelo de Vogel (1979): r = c*sqrt(n), ángulo = n*137,5 grados.
import math
INK="#1F1D1A"; GREEN="#2C6D3F"; LIGHT="#7CC090"; BG="#F4F6F6"
GA=math.radians(137.50776405)  # ángulo áureo exacto

def mix(c1,c2,t):
    a=[int(c1[i:i+2],16) for i in (1,3,5)]; b=[int(c2[i:i+2],16) for i in (1,3,5)]
    return "#%02X%02X%02X"%tuple(round(a[i]+(b[i]-a[i])*t) for i in range(3))

def seeds(N, c, cx, cy):
    out=[]
    for n in range(1,N+1):
        r=c*math.sqrt(n); th=n*GA
        out.append((n, cx+r*math.cos(th), cy+r*math.sin(th), r))
    return out

def svg(kind, size=1200, N=900):
    c=size*0.46/math.sqrt(N); cx=cy=size/2
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}"><rect width="{size}" height="{size}" fill="{BG}"/>']
    for n,x,y,r in seeds(N,c,cx,cy):
        rad=c*(0.40+0.10*math.sqrt(n/N))
        if kind=="gradiente":      # del centro (tinta) al borde (verde claro)
            col=mix(INK,GREEN,min(1,n/N*1.6)) if n<N*0.62 else mix(GREEN,LIGHT,(n/N-0.62)/0.38)
        elif kind=="espirales":    # resalta una de las familias de espirales de Fibonacci (21)
            col=GREEN if (n%21)%3==0 else INK   # 21 brazos de espiral, uno de cada tres en verde
        else:                      # "a la vez": todas verdes salvo la semilla 1, en tinta
            col=INK if n<=1 else GREEN
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rad:.1f}" fill="{col}"/>')
    o.append('</svg>')
    return "\n".join(o)

def svg_angulo(size=1200, N=21):
    # primeras semillas grandes, con el ángulo marcado entre la 1ª y la 2ª
    c=size*0.40/math.sqrt(N); cx=cy=size/2
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}"><rect width="{size}" height="{size}" fill="{BG}"/>']
    pts=seeds(N,c,cx,cy)
    for (n,x,y,r) in pts:
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{c*0.36:.1f}" fill="{GREEN if n>2 else INK}"/>')
        if n<=2: o.append(f'<text x="{x:.1f}" y="{y+c*0.12:.1f}" font-family="DejaVu Sans" font-size="{c*0.30:.0f}" fill="#F4F6F6" text-anchor="middle">{n}</text>')
    # rayos a las semillas 1 y 2 y arco del ángulo
    (n1,x1,y1,r1),(n2,x2,y2,r2)=pts[0],pts[1]
    a1=math.atan2(y1-cy,x1-cx); a2=math.atan2(y2-cy,x2-cx)
    R=c*math.sqrt(N)*0.9
    for a,col in ((a1,INK),(a2,INK)):
        o.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+R*math.cos(a):.1f}" y2="{cy+R*math.sin(a):.1f}" stroke="{col}" stroke-width="4" opacity="0.7"/>')
    ra=R*0.55
    d=(a2-a1)%(2*math.pi)  # sentido horario en pantalla
    large=1 if d>math.pi else 0
    o.append(f'<path d="M{cx+ra*math.cos(a1):.1f},{cy+ra*math.sin(a1):.1f} A{ra:.1f},{ra:.1f} 0 {large} 1 {cx+ra*math.cos(a2):.1f},{cy+ra*math.sin(a2):.1f}" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>')
    o.append(f'<text x="{cx-ra*1.55:.1f}" y="{cy+ra*0.10:.1f}" font-family="DejaVu Serif" font-size="64" fill="{INK}" text-anchor="middle">137,5°</text>')
    o.append('</svg>')
    return "\n".join(o)

open("girasol-gradiente.svg","w").write(svg("gradiente"))
open("girasol-espirales.svg","w").write(svg("espirales"))
open("girasol-angulo.svg","w").write(svg_angulo())
print("ok")
