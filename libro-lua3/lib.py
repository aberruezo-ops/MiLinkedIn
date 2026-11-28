# Dibujo vectorial: personajes y decorados para el libro de colorear.
import math

INK = '#111'
ST = f'stroke="{INK}" stroke-width="4.2" stroke-linejoin="round" stroke-linecap="round"'


def tube(path, w, fill='#fff'):
    """Brazo o pierna: tubo con contorno, se puede colorear por dentro."""
    return (f'<path d="{path}" fill="none" stroke="{INK}" stroke-width="{w:.1f}" stroke-linecap="round"/>'
            f'<path d="{path}" fill="none" stroke="{fill}" stroke-width="{w-9:.1f}" stroke-linecap="round"/>')


def star_path(cx, cy, R, r=None, n=5, rot=-90):
    r = r or R * 0.45
    pts = []
    for i in range(n * 2):
        rad = R if i % 2 == 0 else r
        a = math.radians(rot + i * 180 / n)
        pts.append(f'{cx + rad * math.cos(a):.1f},{cy + rad * math.sin(a):.1f}')
    return 'M' + ' L'.join(pts) + ' Z'


def star(cx, cy, R, fill='#fff'):
    return f'<path d="{star_path(cx, cy, R)}" fill="{fill}" {ST}/>'


def heart(x, y, s, fill='#fff'):
    # corazon centrado en x,y, ancho aprox 100*s
    d = 'M0,42 C-62,-4 -46,-46 -22,-46 C-9,-46 0,-36 0,-26 C0,-36 9,-46 22,-46 C46,-46 62,-4 0,42 Z'
    return f'<path d="{d}" transform="translate({x},{y}) scale({s})" fill="{fill}" {ST} vector-effect="non-scaling-stroke"/>'


def ball(cx, cy, r, mood='happy', deco='none', arms=('down', 'down'), fill='#fff',
         ink=INK, look=0, legs=True, tear=False, blush=True, shoe='#fff'):
    s = ''
    w = max(r * 0.24, 13)
    # ----- piernas
    if legs:
        for sd in (-1, 1):
            x = cx + sd * 0.32 * r
            y0 = cy + 0.85 * r
            y1 = cy + 1.38 * r
            s += tube(f'M{x:.1f},{y0:.1f} L{x:.1f},{y1:.1f}', w, fill)
            s += (f'<ellipse cx="{x + sd * 0.07 * r:.1f}" cy="{y1 + 0.06 * r:.1f}" rx="{0.3 * r:.1f}" '
                  f'ry="{0.15 * r:.1f}" fill="{shoe}" {ST}/>')

    # ----- brazos (detras del cuerpo salvo los que cruzan el pecho)
    front = ''
    for side, kind in zip((-1, 1), arms):
        if kind is None:
            continue
        sx, sy = cx + side * r * 0.92, cy + r * 0.2
        if isinstance(kind, tuple):
            ex, ey = kind
            qx, qy = (sx + ex) / 2 + side * r * 0.15, (sy + ey) / 2 + r * 0.35
            behind = True
        elif kind == 'down':
            ex, ey, qx, qy = cx + side * r * 1.45, cy + r * 0.85, cx + side * r * 1.5, cy + r * 0.35; behind = True
        elif kind == 'up':
            ex, ey, qx, qy = cx + side * r * 1.5, cy - r * 0.95, cx + side * r * 1.65, cy - r * 0.1; behind = True
        elif kind == 'out':
            ex, ey, qx, qy = cx + side * r * 1.95, cy + r * 0.05, cx + side * r * 1.4, cy + r * 0.3; behind = True
        elif kind == 'hip':
            ex, ey, qx, qy = cx + side * r * 0.85, cy + r * 0.8, cx + side * r * 1.6, cy + r * 0.55; behind = False
        elif kind == 'cheek':
            ex, ey, qx, qy = cx + side * r * 0.5, cy + r * 0.45, cx + side * r * 1.5, cy + r * 0.8; behind = False
        elif kind == 'cross':
            ex, ey, qx, qy = cx - side * r * 0.5, cy + r * 0.6, cx + side * r * 0.3, cy + r * 0.85; behind = False
        elif kind == 'chest':
            ex, ey, qx, qy = cx + side * r * 0.25, cy + r * 0.7, cx + side * r * 1.2, cy + r * 0.9; behind = False
        else:
            continue
        d = f'M{sx:.1f},{sy:.1f} Q{qx:.1f},{qy:.1f} {ex:.1f},{ey:.1f}'
        hand = f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="{max(r * 0.15, 9):.1f}" fill="{fill}" {ST}/>'
        piece = tube(d, w * 0.85, fill) + hand
        if behind:
            s += piece
        else:
            front += piece

    # ----- cuerpo
    s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" {ST}/>'

    # ----- decoracion para colorear
    def chord(y):
        return math.sqrt(max(r * r - (y * r) ** 2, 0))

    if deco == 'stripes':
        for yy in (-0.55, 0.62):
            hw = chord(yy)
            s += (f'<path d="M{cx - hw:.1f},{cy + yy * r:.1f} Q{cx},{cy + (yy + (0.28 if yy > 0 else -0.28)) * r:.1f} '
                  f'{cx + hw:.1f},{cy + yy * r:.1f}" fill="none" stroke="{ink}" stroke-width="4"/>')
    elif deco == 'dots':
        for dx, dy in ((-0.38, -0.66), (0, -0.78), (0.38, -0.66), (-0.3, 0.72), (0.3, 0.72)):
            s += f'<circle cx="{cx + dx * r:.1f}" cy="{cy + dy * r:.1f}" r="{0.075 * r:.1f}" fill="#fff" stroke="{ink}" stroke-width="3.5"/>'
    elif deco == 'star':
        s += star(cx, cy - 0.64 * r, 0.17 * r).replace(INK, ink)
    elif deco == 'heart':
        s += heart(cx, cy - 0.62 * r, 0.0032 * r, '#fff').replace(INK, ink)
    elif deco == 'waves':
        for yy in (0.62, 0.78):
            hw = chord(yy) * 0.8
            s += (f'<path d="M{cx - hw:.1f},{cy + yy * r:.1f} q{hw * 0.25:.1f},{-0.1 * r:.1f} {hw * 0.5:.1f},0 '
                  f't{hw * 0.5:.1f},0 t{hw * 0.5:.1f},0 t{hw * 0.5:.1f},0" fill="none" stroke="{ink}" stroke-width="4"/>')
    elif deco == 'zig':
        hw = chord(-0.6) * 0.85
        pts = [(cx - hw + i * hw / 3, cy - 0.62 * r + (0.1 * r if i % 2 else 0)) for i in range(7)]
        s += '<path d="M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts) + f'" fill="none" stroke="{ink}" stroke-width="4"/>'

    # ----- cara
    ex, ey, rx, ry = 0.3 * r, cy - 0.08 * r, 0.15 * r, 0.2 * r
    for sd in (-1, 1):
        s += f'<ellipse cx="{cx + sd * ex:.1f}" cy="{ey:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="#fff" stroke="{ink}" stroke-width="3.5"/>'
        s += f'<circle cx="{cx + sd * ex + look * 0.07 * r:.1f}" cy="{ey + 0.03 * r:.1f}" r="{0.08 * r:.1f}" fill="#111"/>'
    if mood in ('sad', 'worried', 'sorry'):
        for sd in (-1, 1):
            s += (f'<path d="M{cx + sd * 0.45 * r:.1f},{cy - 0.34 * r:.1f} L{cx + sd * 0.14 * r:.1f},{cy - 0.46 * r:.1f}" '
                  f'stroke="{ink}" stroke-width="4" stroke-linecap="round"/>')
    if mood == 'angry':
        for sd in (-1, 1):
            s += (f'<path d="M{cx + sd * 0.48 * r:.1f},{cy - 0.46 * r:.1f} L{cx + sd * 0.12 * r:.1f},{cy - 0.32 * r:.1f}" '
                  f'stroke="{ink}" stroke-width="4" stroke-linecap="round"/>')
    my = cy + 0.28 * r
    if mood == 'happy':
        s += (f'<path d="M{cx - 0.3 * r:.1f},{my:.1f} Q{cx},{my + 0.5 * r:.1f} {cx + 0.3 * r:.1f},{my:.1f} Z" '
              f'fill="#fff" stroke="{ink}" stroke-width="4" stroke-linejoin="round"/>')
    elif mood == 'smile':
        s += (f'<path d="M{cx - 0.25 * r:.1f},{my + 0.05 * r:.1f} Q{cx},{my + 0.35 * r:.1f} {cx + 0.25 * r:.1f},{my + 0.05 * r:.1f}" '
              f'fill="none" stroke="{ink}" stroke-width="4" stroke-linecap="round"/>')
    elif mood in ('sad', 'sorry', 'worried'):
        s += (f'<path d="M{cx - 0.25 * r:.1f},{my + 0.28 * r:.1f} Q{cx},{my + 0.02 * r:.1f} {cx + 0.25 * r:.1f},{my + 0.28 * r:.1f}" '
              f'fill="none" stroke="{ink}" stroke-width="4" stroke-linecap="round"/>')
    elif mood == 'angry':
        s += (f'<path d="M{cx - 0.25 * r:.1f},{my + 0.28 * r:.1f} Q{cx},{my + 0.12 * r:.1f} {cx + 0.25 * r:.1f},{my + 0.28 * r:.1f}" '
              f'fill="none" stroke="{ink}" stroke-width="4" stroke-linecap="round"/>')
    elif mood == 'open':
        s += f'<ellipse cx="{cx}" cy="{my + 0.15 * r:.1f}" rx="{0.14 * r:.1f}" ry="{0.19 * r:.1f}" fill="#fff" stroke="{ink}" stroke-width="4"/>'
    else:  # neutral
        s += (f'<path d="M{cx - 0.2 * r:.1f},{my + 0.2 * r:.1f} L{cx + 0.2 * r:.1f},{my + 0.2 * r:.1f}" '
              f'stroke="{ink}" stroke-width="4" stroke-linecap="round"/>')
    if blush and mood in ('happy', 'smile'):
        for sd in (-1, 1):
            s += f'<ellipse cx="{cx + sd * 0.55 * r:.1f}" cy="{cy + 0.3 * r:.1f}" rx="{0.1 * r:.1f}" ry="{0.065 * r:.1f}" fill="#fff" stroke="{ink}" stroke-width="3"/>'
    if tear:
        tx, ty = cx - 0.34 * r, cy + 0.2 * r
        s += (f'<path d="M{tx:.1f},{ty:.1f} q{-0.07 * r:.1f},{0.14 * r:.1f} 0,{0.2 * r:.1f} q{0.07 * r:.1f},{-0.06 * r:.1f} 0,{-0.2 * r:.1f} z" '
              f'fill="#fff" stroke="{ink}" stroke-width="3.5"/>')
    return s + front


def stand(r, ground):
    """cy para que la pelota apoye los pies en 'ground'."""
    return ground - 1.58 * r


# ------------------------------------------------------------------ decorado
def sun(cx, cy, r, face=True):
    s = ''
    for i in range(12):
        a = math.radians(i * 30)
        x1, y1 = cx + math.cos(a) * r * 1.25, cy + math.sin(a) * r * 1.25
        x2, y2 = cx + math.cos(a) * r * 1.65, cy + math.sin(a) * r * 1.65
        s += f'<path d="M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}" {ST} stroke-width="7"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" {ST}/>'
    if face:
        s += (f'<circle cx="{cx - r * .3:.1f}" cy="{cy - r * .1:.1f}" r="{r * .08:.1f}" fill="#111"/>'
              f'<circle cx="{cx + r * .3:.1f}" cy="{cy - r * .1:.1f}" r="{r * .08:.1f}" fill="#111"/>'
              f'<path d="M{cx - r * .35:.1f},{cy + r * .2:.1f} Q{cx},{cy + r * .6:.1f} {cx + r * .35:.1f},{cy + r * .2:.1f}" fill="none" stroke="#111" stroke-width="4" stroke-linecap="round"/>')
    return s


def cloud(x, y, w, fill='#fff'):
    k = w / 100
    d = 'M15,45 Q-6,45 5,28 Q8,12 25,18 Q30,0 52,6 Q68,-4 80,14 Q102,12 98,32 Q102,46 85,45 Z'
    return f'<path d="{d}" transform="translate({x},{y}) scale({k})" fill="{fill}" {ST} vector-effect="non-scaling-stroke"/>'


def tree(x, g, k=1.0):
    s = (f'<path d="M{x - 18 * k},{g} L{x - 12 * k},{g - 130 * k} L{x + 12 * k},{g - 130 * k} L{x + 18 * k},{g} Z" fill="#fff" {ST}/>')
    d = (f'M{x - 85 * k},{g - 120 * k} Q{x - 120 * k},{g - 185 * k} {x - 55 * k},{g - 205 * k} '
         f'Q{x - 35 * k},{g - 275 * k} {x + 20 * k},{g - 250 * k} Q{x + 85 * k},{g - 275 * k} {x + 90 * k},{g - 205 * k} '
         f'Q{x + 135 * k},{g - 165 * k} {x + 90 * k},{g - 120 * k} Q{x},{g - 90 * k} {x - 85 * k},{g - 120 * k} Z')
    s += f'<path d="{d}" fill="#fff" {ST}/>'
    for dx, dy in ((-40, -190), (30, -215), (55, -150), (-10, -140)):
        s += f'<circle cx="{x + dx * k:.1f}" cy="{g + dy * k:.1f}" r="{9 * k:.1f}" fill="#fff" {ST}/>'
    return s


def flower(x, y, k=1.0):
    s = f'<path d="M{x},{y} L{x},{y + 55 * k}" {ST}/>'
    s += f'<path d="M{x},{y + 40 * k} q{16 * k},{-14 * k} {26 * k},{-4 * k} q{-12 * k},{14 * k} {-26 * k},{4 * k} z" fill="#fff" {ST}/>'
    for i in range(5):
        a = math.radians(i * 72 - 90)
        s += f'<circle cx="{x + math.cos(a) * 15 * k:.1f}" cy="{y + math.sin(a) * 15 * k:.1f}" r="{11 * k:.1f}" fill="#fff" {ST}/>'
    s += f'<circle cx="{x}" cy="{y}" r="{9 * k:.1f}" fill="#fff" {ST}/>'
    return s


def grass(x, y, k=1.0):
    d = (f'M{x},{y} L{x - 6 * k},{y - 22 * k} L{x + 3 * k},{y - 10 * k} L{x + 8 * k},{y - 28 * k} '
         f'L{x + 14 * k},{y - 10 * k} L{x + 24 * k},{y - 22 * k} L{x + 20 * k},{y}')
    return f'<path d="{d}" fill="none" {ST}/>'


def hill(g, w=750, h=700, wave=18):
    back = f'M-10,{g - 38} Q{w * .35},{g - 95} {w * .7},{g - 48} T{w + 10},{g - 40}'
    top = f'M-10,{g} Q{w * .25},{g - wave} {w * .5},{g} T{w + 10},{g - 4}'
    return (f'<path d="{back} L{w + 10},{h + 10} L-10,{h + 10} Z" fill="#fff"/><path d="{back}" fill="none" {ST} stroke-width="3.2"/>'
            f'<path d="{top} L{w + 10},{h + 10} L-10,{h + 10} Z" fill="#fff"/>'
            f'<path d="{top}" fill="none" {ST}/>')


def note(x, y, k=1.0):
    return (f'<ellipse cx="{x}" cy="{y}" rx="{11 * k:.1f}" ry="{8 * k:.1f}" transform="rotate(-20 {x} {y})" fill="#fff" {ST}/>'
            f'<path d="M{x + 10 * k:.1f},{y - 3 * k:.1f} L{x + 10 * k:.1f},{y - 42 * k:.1f} q{18 * k:.1f},{4 * k:.1f} {12 * k:.1f},{22 * k:.1f}" fill="none" {ST}/>')


def bird(x, y, k=1.0):
    s = f'<path d="M{x - 6 * k},{y + 18 * k} L{x - 6 * k},{y + 34 * k} M{x + 8 * k},{y + 18 * k} L{x + 8 * k},{y + 34 * k}" {ST}/>'
    s += f'<path d="M{x - 24 * k},{y + 2 * k} L{x - 48 * k},{y - 8 * k} L{x - 40 * k},{y + 14 * k} Z" fill="#fff" {ST}/>'
    s += f'<ellipse cx="{x}" cy="{y}" rx="{28 * k:.1f}" ry="{20 * k:.1f}" fill="#fff" {ST}/>'
    s += f'<circle cx="{x + 22 * k:.1f}" cy="{y - 16 * k:.1f}" r="{14 * k:.1f}" fill="#fff" {ST}/>'
    s += f'<path d="M{x + 34 * k:.1f},{y - 18 * k:.1f} L{x + 48 * k:.1f},{y - 13 * k:.1f} L{x + 34 * k:.1f},{y - 9 * k:.1f} Z" fill="#fff" {ST}/>'
    s += f'<circle cx="{x + 25 * k:.1f}" cy="{y - 19 * k:.1f}" r="{2.6 * k:.1f}" fill="#111"/>'
    s += f'<path d="M{x - 10 * k:.1f},{y - 2 * k:.1f} q{12 * k:.1f},{-10 * k:.1f} {24 * k:.1f},{2 * k:.1f} q{-10 * k:.1f},{12 * k:.1f} {-24 * k:.1f},{-2 * k:.1f}" fill="#fff" {ST} stroke-width="4"/>'
    return s


def font(size, weight=600, anchor='middle'):
    return f'font-family="Fredoka" font-weight="{weight}" font-size="{size}" text-anchor="{anchor}"'


def bubble(x, y, w, h, text, tx, ty, size=30):
    """Bocadillo con cola hacia (tx,ty), que sale del borde inferior."""
    bx = min(max(tx, x + 30), x + w - 30)
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2.6:.0f}" fill="#fff" {ST}/>'
    s += f'<path d="M{bx - 16},{y + h} L{tx},{ty} L{bx + 16},{y + h} Z" fill="#fff" {ST}/>'
    s += f'<path d="M{bx - 13},{y + h} L{bx + 13},{y + h}" stroke="#fff" stroke-width="8" stroke-linecap="butt"/>'
    for i, line in enumerate(text.split('|')):
        n = len(text.split('|'))
        yy = y + h / 2 + size * 0.34 + (i - (n - 1) / 2) * size * 1.05
        s += f'<text x="{x + w / 2}" y="{yy:.1f}" {font(size)} fill="#111">{line}</text>'
    return s


def thought(x, y, w, h, dots):
    s = f'<ellipse cx="{x + w / 2}" cy="{y + h / 2}" rx="{w / 2}" ry="{h / 2}" fill="#fff" {ST}/>'
    for (dx, dy, dr) in dots:
        s += f'<circle cx="{dx}" cy="{dy}" r="{dr}" fill="#fff" {ST}/>'
    return s


def outlined_text(x, y, text, size, weight=700, sw=4):
    return (f'<text x="{x}" y="{y}" {font(size, weight)} fill="#fff" stroke="#111" stroke-width="{sw}" '
            f'stroke-linejoin="round">{text}</text>')


def rainbow(cx, cy, r0, bands=5, bw=30):
    s = ''
    for i in range(bands + 1):
        r = r0 - i * bw
        s += f'<path d="M{cx - r},{cy} A{r},{r} 0 0 1 {cx + r},{cy}" fill="none" {ST} stroke-width="4"/>'
    return s


def sofa(x, y):
    """Sofa con patas altas, ocupa x..x+330, y..y+260 (patas llegan a y+260)."""
    s = ''
    s += f'<rect x="{x}" y="{y}" width="330" height="120" rx="30" fill="#fff" {ST}/>'              # respaldo
    s += f'<rect x="{x - 30}" y="{y + 70}" width="70" height="140" rx="26" fill="#fff" {ST}/>'      # brazo izq
    s += f'<rect x="{x + 290}" y="{y + 70}" width="70" height="140" rx="26" fill="#fff" {ST}/>'     # brazo der
    s += f'<rect x="{x + 30}" y="{y + 110}" width="270" height="70" rx="18" fill="#fff" {ST}/>'     # asiento
    s += f'<path d="M{x + 165},{y + 112} L{x + 165},{y + 178}" {ST} stroke-width="4"/>'
    for lx in (x - 10, x + 320):
        s += f'<path d="M{lx},{y + 210} L{lx},{y + 262}" {ST} stroke-width="14"/>'
    return s


def window_storm(x, y, w, h):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#fff" {ST}/>'
    s += f'<path d="M{x + w / 2},{y} L{x + w / 2},{y + h} M{x},{y + h / 2} L{x + w},{y + h / 2}" {ST}/>'
    s += cloud(x + 20, y + 14, w * 0.5)
    s += cloud(x + w * 0.5, y + 40, w * 0.42)
    bolt = f'M{x + w * .62},{y + h * .42} L{x + w * .5},{y + h * .66} L{x + w * .6},{y + h * .66} L{x + w * .5},{y + h * .92} L{x + w * .78},{y + h * .58} L{x + w * .66},{y + h * .58} L{x + w * .74},{y + h * .42} Z'
    s += f'<path d="{bolt}" fill="#fff" {ST} stroke-width="4"/>'
    for dx in (0.12, 0.28, 0.82, 0.9):
        s += f'<path d="M{x + w * dx},{y + h * .62} l-8,24 M{x + w * dx + 18},{y + h * .74} l-8,24" {ST} stroke-width="4"/>'
    return s


def banner(x, y, w, h, text, size=34):
    s = f'<path d="M{x},{y + 8} Q{x + w / 2},{y - 14} {x + w},{y + 8} L{x + w},{y + h} Q{x + w / 2},{y + h - 22} {x},{y + h} Z" fill="#fff" {ST}/>'
    s += f'<text x="{x + w / 2}" y="{y + h * .62:.1f}" {font(size, 700)} fill="#111">{text}</text>'
    return s
