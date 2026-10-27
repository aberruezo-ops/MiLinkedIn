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

def svg_trozo(size=1200, N=900, R=600):
    """Trozo de la primera imagen: el abanico de 137,5 grados del girasol, con el arco del ángulo en el vértice."""
    c=R/math.sqrt(N)
    half=math.radians(137.5)/2
    ax=size/2; ay=size/2+R/2          # vértice del abanico, para centrar el trozo en el lienzo
    up=-math.pi/2
    a1=up-half; a2=up+half
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}"><rect width="{size}" height="{size}" fill="{BG}"/>']
    for n in range(1,N+1):
        r=c*math.sqrt(n); th=n*GA
        # ángulo de la semilla medido respecto a la vertical hacia arriba, normalizado a [-pi, pi]
        d=(th-up+math.pi)%(2*math.pi)-math.pi
        if abs(d)>half-0.012: continue   # fuera del abanico (con un pequeño margen para no pisar los bordes)
        x=ax+r*math.cos(th); y=ay+r*math.sin(th)
        rad=c*(0.40+0.10*math.sqrt(n/N))
        col=mix(INK,GREEN,min(1,n/N*1.6)) if n<N*0.62 else mix(GREEN,LIGHT,(n/N-0.62)/0.38)
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rad:.1f}" fill="{col}"/>')
    for a in (a1,a2):
        o.append(f'<line x1="{ax}" y1="{ay}" x2="{ax+(R*1.02)*math.cos(a):.1f}" y2="{ay+(R*1.02)*math.sin(a):.1f}" stroke="{INK}" stroke-width="3" opacity="0.55"/>')
    ra=R*0.20
    p1=(ax+ra*math.cos(a1), ay+ra*math.sin(a1)); p2=(ax+ra*math.cos(a2), ay+ra*math.sin(a2))
    arc=f'M{p1[0]:.1f},{p1[1]:.1f} A{ra:.1f},{ra:.1f} 0 0 1 {p2[0]:.1f},{p2[1]:.1f}'
    o.append(f'<path d="{arc}" fill="none" stroke="{BG}" stroke-width="26" stroke-linecap="round"/>')
    o.append(f'<path d="{arc}" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>')
    o.append('</svg>')
    return "\n".join(o)

open("girasol-trozo.svg","w").write(svg_trozo())

def svg_porcion(size=1200, N=900, tenue=0.16):
    """El girasol entero (igual que la primera imagen) con las semillas fuera de 137,5 grados muy tenues y el trozo destacado."""
    c=size*0.46/math.sqrt(N); cx=cy=size/2
    half=math.radians(137.5)/2
    up=-math.pi/2+math.radians(0)   # la bisectriz del trozo apunta hacia arriba
    R=c*math.sqrt(N)
    a1=up-half; a2=up+half
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}"><rect width="{size}" height="{size}" fill="{BG}"/>']
    for n in range(1,N+1):
        r=c*math.sqrt(n); th=n*GA
        d=(th-up+math.pi)%(2*math.pi)-math.pi
        dentro=abs(d)<=half
        x=cx+r*math.cos(th); y=cy+r*math.sin(th)
        rad=c*(0.40+0.10*math.sqrt(n/N))
        col=mix(INK,GREEN,min(1,n/N*1.6)) if n<N*0.62 else mix(GREEN,LIGHT,(n/N-0.62)/0.38)
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rad:.1f}" fill="{col}" opacity="{1 if dentro else tenue}"/>')
    for a in (a1,a2):
        o.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+(R*1.03)*math.cos(a):.1f}" y2="{cy+(R*1.03)*math.sin(a):.1f}" stroke="{INK}" stroke-width="3" opacity="0.6"/>')
    ra=R*0.17
    p1=(cx+ra*math.cos(a1), cy+ra*math.sin(a1)); p2=(cx+ra*math.cos(a2), cy+ra*math.sin(a2))
    arc=f'M{p1[0]:.1f},{p1[1]:.1f} A{ra:.1f},{ra:.1f} 0 0 1 {p2[0]:.1f},{p2[1]:.1f}'
    o.append(f'<path d="{arc}" fill="none" stroke="{BG}" stroke-width="26" stroke-linecap="round"/>')
    o.append(f'<path d="{arc}" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>')
    o.append('</svg>')
    return "\n".join(o)

open("girasol-porcion.svg","w").write(svg_porcion())

def svg_zoom(size=1200, N=900):
    """El girasol entero a la izquierda y, en una lente, el zoom de su centro con el ángulo entre las dos primeras semillas."""
    # girasol principal
    cx, cy, R0 = 600, 600, 552
    c0 = R0/math.sqrt(N)
    # lente
    lx, ly, RL = cx+225, cy-225, 215   # la lente queda dentro del contorno del girasol
    NL = 13
    cl = RL*0.92/math.sqrt(NL)
    s = cl/c0                     # factor de ampliación
    rs = RL/s                     # radio del círculo pequeño que se amplía
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}"><defs><clipPath id="lente"><circle cx="{lx}" cy="{ly}" r="{RL-4}"/></clipPath></defs><rect width="{size}" height="{size}" fill="{BG}"/>']
    # girasol entero
    for n in range(1,N+1):
        r=c0*math.sqrt(n); th=n*GA
        col=mix(INK,GREEN,min(1,n/N*1.6)) if n<N*0.62 else mix(GREEN,LIGHT,(n/N-0.62)/0.38)
        rad=c0*(0.40+0.10*math.sqrt(n/N))
        o.append(f'<circle cx="{cx+r*math.cos(th):.1f}" cy="{cy+r*math.sin(th):.1f}" r="{rad:.1f}" fill="{col}"/>')
    # conos de zoom
    dx, dy = lx-cx, ly-cy; L=math.hypot(dx,dy); ux, uy = dx/L, dy/L; nx, ny = -uy, ux
    for sg in (1,-1):
        o.append(f'<line x1="{cx+sg*nx*rs:.1f}" y1="{cy+sg*ny*rs:.1f}" x2="{lx+sg*nx*RL:.1f}" y2="{ly+sg*ny*RL:.1f}" stroke="{INK}" stroke-width="3" opacity="0.55"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{rs:.1f}" fill="none" stroke="{INK}" stroke-width="5"/>')
    # lente
    o.append(f'<circle cx="{lx}" cy="{ly}" r="{RL}" fill="#FFFFFF" stroke="{INK}" stroke-width="8"/>')
    off=math.radians(-150)-GA        # coloca el rayo de la semilla 1 a -150 grados
    o.append('<g clip-path="url(#lente)">')
    a1=math.radians(-150); a2=a1+GA
    for a in (a1,a2):
        o.append(f'<line x1="{lx}" y1="{ly}" x2="{lx+RL*math.cos(a):.1f}" y2="{ly+RL*math.sin(a):.1f}" stroke="{INK}" stroke-width="4" opacity="0.7"/>')
    for n in range(1,NL+1):
        r=cl*math.sqrt(n); th=n*GA+off
        col=mix(INK,GREEN,(n-1)/(NL-1)*0.9)
        rad=cl*(0.34+0.04*math.sqrt(n/NL))
        o.append(f'<circle cx="{lx+r*math.cos(th):.1f}" cy="{ly+r*math.sin(th):.1f}" r="{rad:.1f}" fill="{col}"/>')
    ra=cl*0.58
    p1=(lx+ra*math.cos(a1), ly+ra*math.sin(a1)); p2=(lx+ra*math.cos(a2), ly+ra*math.sin(a2))
    arc=f'M{p1[0]:.1f},{p1[1]:.1f} A{ra:.1f},{ra:.1f} 0 0 1 {p2[0]:.1f},{p2[1]:.1f}'
    o.append(f'<path d="{arc}" fill="none" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round"/>')
    o.append(f'<path d="{arc}" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>')
    o.append('</g></svg>')
    return "\n".join(o)

open("girasol-zoom.svg","w").write(svg_zoom())

def svg_zoom_fiel(size=1200, N=900, s=2.0):
    """Zoom fiel: la lente muestra exactamente las semillas del círculo marcado, sin girar, ampliadas s veces."""
    cx, cy, R0 = 600, 600, 552
    c0 = R0/math.sqrt(N)
    lx, ly, RL = cx+235, cy-235, 215
    rs = RL/s                              # radio de la zona ampliada
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}"><defs><clipPath id="lente"><circle cx="{lx}" cy="{ly}" r="{RL-4}"/></clipPath></defs><rect width="{size}" height="{size}" fill="{BG}"/>']
    def color(n):
        if n<=2: return GREEN            # las dos primeras semillas, en el verde del logo
        return mix(INK,GREEN,min(1,n/N*1.6)) if n<N*0.62 else mix(GREEN,LIGHT,(n/N-0.62)/0.38)
    for n in range(1,N+1):
        r=c0*math.sqrt(n); th=n*GA
        rad=c0*(0.40+0.10*math.sqrt(n/N))
        o.append(f'<circle cx="{cx+r*math.cos(th):.1f}" cy="{cy+r*math.sin(th):.1f}" r="{rad:.1f}" fill="{color(n)}"/>')
    dx, dy = lx-cx, ly-cy; L=math.hypot(dx,dy); ux, uy = dx/L, dy/L; nx, ny = -uy, ux
    for sg in (1,-1):
        o.append(f'<line x1="{cx+sg*nx*rs:.1f}" y1="{cy+sg*ny*rs:.1f}" x2="{lx+sg*nx*RL:.1f}" y2="{ly+sg*ny*RL:.1f}" stroke="{INK}" stroke-width="3" opacity="0.55"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{rs:.1f}" fill="none" stroke="{INK}" stroke-width="5"/>')
    o.append(f'<circle cx="{lx}" cy="{ly}" r="{RL}" fill="#FFFFFF" stroke="{INK}" stroke-width="8"/>')
    o.append('<g clip-path="url(#lente)">')
    a1=GA; a2=2*GA                          # direcciones reales de las semillas 1 y 2
    for a in (a1,a2):
        o.append(f'<line x1="{lx}" y1="{ly}" x2="{lx+RL*math.cos(a):.1f}" y2="{ly+RL*math.sin(a):.1f}" stroke="{INK}" stroke-width="3" opacity="0.6"/>')
    for n in range(1,N+1):
        r=c0*math.sqrt(n)*s
        if r>RL*1.05: break
        th=n*GA
        rad=c0*(0.40+0.10*math.sqrt(n/N))*s
        o.append(f'<circle cx="{lx+r*math.cos(th):.1f}" cy="{ly+r*math.sin(th):.1f}" r="{rad:.1f}" fill="{color(n)}"/>')
    ra=c0*s*2.4
    p1=(lx+ra*math.cos(a1), ly+ra*math.sin(a1)); p2=(lx+ra*math.cos(a2), ly+ra*math.sin(a2))
    arc=f'M{p1[0]:.1f},{p1[1]:.1f} A{ra:.1f},{ra:.1f} 0 0 1 {p2[0]:.1f},{p2[1]:.1f}'
    o.append(f'<path d="{arc}" fill="none" stroke="#FFFFFF" stroke-width="16" stroke-linecap="round"/>')
    o.append(f'<path d="{arc}" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>')
    o.append('</g></svg>')
    return "\n".join(o)

open("girasol-zoom.svg","w").write(svg_zoom_fiel())

def svg_zoom_cabecera(W=1584, H=396, cx=1235, cy=198, R0=182, N=900, s=2.0):
    """Zoom fiel para la cabecera de LinkedIn: flor entera y lente interior, sobre fondo transparente. Incluye comprobaciones de simetría."""
    k=R0/552.0                              # factor de escala respecto a la versión cuadrada
    c0=R0/math.sqrt(N)
    RL=215*k; lx=cx+235*k; ly=cy-235*k
    rs=RL/s
    # comprobaciones geométricas
    assert math.hypot(lx-cx,ly-cy)+RL <= R0, "la lente sobresale del girasol"
    assert math.hypot(lx-cx,ly-cy) > RL+rs, "la lente tapa el círculo que amplía"
    n_ok=0
    for n in range(1,N+1):
        r=c0*math.sqrt(n)
        if r<=rs:
            px,py=r*math.cos(n*GA), r*math.sin(n*GA)               # posición real respecto al centro de la flor
            qx,qy=c0*s*math.sqrt(n)*math.cos(n*GA), c0*s*math.sqrt(n)*math.sin(n*GA)  # posición en la lente respecto a su centro
            assert abs(qx-s*px)<1e-9 and abs(qy-s*py)<1e-9, "la lente no es una ampliación exacta"
            n_ok+=1
    print(f"comprobado: {n_ok} semillas del círculo aparecen en la lente exactamente x{s}; la lente queda dentro de la flor")
    def color(n):
        if n<=2: return GREEN
        return mix(INK,GREEN,min(1,n/N*1.6)) if n<N*0.62 else mix(GREEN,LIGHT,(n/N-0.62)/0.38)
    lw=lambda v: max(1.4, v*k*1.0)
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><defs><clipPath id="lente"><circle cx="{lx:.1f}" cy="{ly:.1f}" r="{RL-2:.1f}"/></clipPath></defs>']
    for n in range(1,N+1):
        r=c0*math.sqrt(n); th=n*GA
        rad=c0*(0.40+0.10*math.sqrt(n/N))
        o.append(f'<circle cx="{cx+r*math.cos(th):.1f}" cy="{cy+r*math.sin(th):.1f}" r="{rad:.2f}" fill="{color(n)}"/>')
    dx,dy=lx-cx,ly-cy; L=math.hypot(dx,dy); ux,uy=dx/L,dy/L; nx,ny=-uy,ux
    for sg in (1,-1):
        o.append(f'<line x1="{cx+sg*nx*rs:.1f}" y1="{cy+sg*ny*rs:.1f}" x2="{lx+sg*nx*RL:.1f}" y2="{ly+sg*ny*RL:.1f}" stroke="{INK}" stroke-width="{lw(3):.1f}" opacity="0.55"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{rs:.1f}" fill="none" stroke="{INK}" stroke-width="{lw(5):.1f}"/>')
    o.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="{RL:.1f}" fill="#FFFFFF" stroke="{INK}" stroke-width="{lw(8):.1f}"/>')
    o.append('<g clip-path="url(#lente)">')
    a1=GA; a2=2*GA
    for a in (a1,a2):
        o.append(f'<line x1="{lx:.1f}" y1="{ly:.1f}" x2="{lx+RL*math.cos(a):.1f}" y2="{ly+RL*math.sin(a):.1f}" stroke="{INK}" stroke-width="{lw(3):.1f}" opacity="0.6"/>')
    for n in range(1,N+1):
        r=c0*math.sqrt(n)*s
        if r>RL*1.05: break
        th=n*GA
        rad=c0*(0.40+0.10*math.sqrt(n/N))*s
        o.append(f'<circle cx="{lx+r*math.cos(th):.1f}" cy="{ly+r*math.sin(th):.1f}" r="{rad:.2f}" fill="{color(n)}"/>')
    ra=c0*s*2.4
    p1=(lx+ra*math.cos(a1), ly+ra*math.sin(a1)); p2=(lx+ra*math.cos(a2), ly+ra*math.sin(a2))
    arc=f'M{p1[0]:.1f},{p1[1]:.1f} A{ra:.1f},{ra:.1f} 0 0 1 {p2[0]:.1f},{p2[1]:.1f}'
    o.append(f'<path d="{arc}" fill="none" stroke="#FFFFFF" stroke-width="{lw(16):.1f}" stroke-linecap="round"/>')
    o.append(f'<path d="{arc}" fill="none" stroke="{INK}" stroke-width="{lw(7):.1f}" stroke-linecap="round"/>')
    o.append('</g></svg>')
    return "\n".join(o)


def svg_sesgo_cabecera(W=1584, H=396, cx=1155, cy=198, R0=182, N=900, h=0.64):
    """Girasol entero sin zoom y con un único corte en diagonal en el lado superior, paralelo a la tilde del logo (137,5 grados)."""
    c0=R0/math.sqrt(N)
    a=math.radians(180-137.5)              # 42,5 grados: inclinación del corte respecto a la horizontal
    D=(math.cos(a), -math.sin(a))          # dirección del corte en pantalla (sube hacia la derecha)
    Nn=(-math.sin(a), -math.cos(a))        # normal hacia arriba-izquierda (lado que se corta)
    Lg=R0*1.6; hh=R0*h
    pts=[(cx+hh*Nn[0]+Lg*D[0], cy+hh*Nn[1]+Lg*D[1]), (cx+hh*Nn[0]-Lg*D[0], cy+hh*Nn[1]-Lg*D[1]),
         (cx-2*R0*Nn[0]-Lg*D[0], cy-2*R0*Nn[1]-Lg*D[1]), (cx-2*R0*Nn[0]+Lg*D[0], cy-2*R0*Nn[1]+Lg*D[1])]
    poly=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    def color(n):
        return mix(INK,GREEN,min(1,n/N*1.6)) if n<N*0.62 else mix(GREEN,LIGHT,(n/N-0.62)/0.38)
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><defs><clipPath id="corte"><polygon points="{poly}"/></clipPath></defs><g clip-path="url(#corte)">']
    for n in range(1,N+1):
        r=c0*math.sqrt(n); th=n*GA
        rad=c0*(0.40+0.10*math.sqrt(n/N))
        o.append(f'<circle cx="{cx+r*math.cos(th):.1f}" cy="{cy+r*math.sin(th):.1f}" r="{rad:.2f}" fill="{color(n)}"/>')
    o.append('</g></svg>')
    print(f"comprobado: un único corte en el lado superior, paralelo a la tilde (42,5 grados sobre la horizontal), a {h:.2f} del radio del centro")
    return "\n".join(o)

open("girasol-cabecera.svg","w").write(svg_sesgo_cabecera())

# girasol con el corte superior para la tarjeta cuadrada (mismas proporciones que en la cabecera)
open("girasol-tarjeta.svg","w").write(svg_sesgo_cabecera(W=1200,H=1200,cx=852,cy=782,R0=266))

# girasol con el corte superior para la portada apaisada del artículo (1920x1080)
open("girasol-portada.svg","w").write(svg_sesgo_cabecera(W=1920,H=1080,cx=1222,cy=720,R0=287))
