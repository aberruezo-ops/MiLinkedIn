# Tilo (el erizo) y decorado nuevo para el libro 3.
import math
from jardin import *


def _spikes(cx, cy, R, r, n, a0=0, a1=360, k=1.0):
    """Corona de pinchos: alterna radio exterior R e interior r entre los angulos a0 y a1."""
    pts = []
    steps = n * 2
    for i in range(steps + 1):
        a = math.radians(a0 + (a1 - a0) * i / steps)
        rr = R if i % 2 else r
        pts.append(f'{cx + math.cos(a) * rr:.1f},{cy + math.sin(a) * rr:.1f}')
    return 'M' + ' L'.join(pts)


def tilo(cx, g, s=1.0, mood='happy', flip=1, look=0):
    """Erizo de frente. Pies en g; altura total ~250*s, ancho ~280*s."""
    sp, face, dark = fc('tilo_spikes'), fc('tilo_face'), fc('tilo_dark', '#111')
    o = grp(cx, g, s, flip)
    # abrigo de pinchos (largo, casi hasta el suelo)
    o += f'<path d="{_spikes(0, -112, 140, 100, 22, 140, 400)} Z" fill="{sp}" {L(s)}/>'
    o += f'<ellipse cx="0" cy="-100" rx="108" ry="96" fill="{sp}" {L(s, .7)}/>'
    for a in range(160, 390, 18):
        r = math.radians(a)
        x1, y1 = math.cos(r) * 70, -104 + math.sin(r) * 64
        x2, y2 = math.cos(r) * 96, -104 + math.sin(r) * 88
        o += f'<path d="M{x1:.0f},{y1:.0f} L{x2:.0f},{y2:.0f}" fill="none" {L(s, .55)}/>'
    # barriga y patitas
    o += f'<path d="M-58,-14 Q-62,-70 0,-72 Q62,-70 58,-14 Z" fill="{fc("tilo_belly", "#fff")}" {L(s, .8)}/>'
    for sd in (-1, 1):
        o += f'<ellipse cx="{sd * 40}" cy="-10" rx="26" ry="12" fill="{face}" {L(s)}/>'
        o += f'<path d="M{sd * 40 - 7},-17 L{sd * 40 - 7},-6 M{sd * 40 + 7},-17 L{sd * 40 + 7},-6" fill="none" {L(s, .55)}/>'
    # orejas
    for sd in (-1, 1):
        o += f'<ellipse cx="{sd * 50}" cy="-170" rx="15" ry="13" fill="{face}" {L(s)}/><ellipse cx="{sd * 50}" cy="-170" rx="7" ry="6" fill="{fc("cat_inner")}" {L(s, .5)}/>'
    # cara en forma de gota con el hocico puntiagudo hacia abajo
    o += f'<path d="M-62,-150 Q-60,-182 0,-184 Q60,-182 62,-150 Q58,-118 26,-96 Q12,-82 0,-78 Q-12,-82 -26,-96 Q-58,-118 -62,-150 Z" fill="{face}" {L(s)}/>'
    o += f'<ellipse cx="0" cy="-80" rx="12" ry="9" fill="{dark}"/><ellipse cx="-4" cy="-83" rx="3.5" ry="2.5" fill="#fff"/>'
    # ojos
    ex = 3 * look
    for sd in (-1, 1):
        if mood == 'sleep':
            o += f'<path d="M{sd * 26 - 9},-142 Q{sd * 26},-135 {sd * 26 + 9},-142" fill="none" {L(s, .9)}/>'
        else:
            ry = 11 if mood in ('scared', 'open') else 9
            o += f'<ellipse cx="{sd * 26 + ex}" cy="-144" rx="7.5" ry="{ry}" fill="{dark}"/><circle cx="{sd * 26 + ex + 2.5}" cy="-147" r="2.8" fill="#fff"/>'
    if mood in ('scared', 'sad'):
        for sd in (-1, 1):
            o += f'<path d="M{sd * 16},-164 L{sd * 36},-158" fill="none" {L(s, .85)}/>'
    # boca, justo debajo del hocico
    if mood in ('happy', 'joy'):
        o += f'<path d="M-16,-68 Q-8,-58 0,-62 Q8,-58 16,-68" fill="none" {L(s, .8)}/>'
    elif mood == 'smile':
        o += f'<path d="M-12,-66 Q0,-60 12,-66" fill="none" {L(s, .8)}/>'
    elif mood == 'sad':
        o += f'<path d="M-11,-62 Q0,-69 11,-62" fill="none" {L(s, .8)}/>'
    elif mood in ('scared', 'open'):
        o += f'<ellipse cx="0" cy="-64" rx="6" ry="7" fill="{fc("mouth")}" {L(s, .7)}/>'
    if mood in ('happy', 'joy', 'smile'):
        for sd in (-1, 1):
            o += f'<ellipse cx="{sd * 42}" cy="-122" rx="9" ry="6" fill="{fc("blush")}" {L(s, .4)}/>'
    return o + '</g>'


def tilo_ball(cx, g, s=1.0, peek=False):
    """Tilo hecho una bola. Apoyado en g; diametro ~170*s."""
    sp = fc('tilo_spikes')
    o = grp(cx, g, s)
    o += f'<path d="{_spikes(0, -78, 92, 70, 17)} Z" fill="{sp}" {L(s)}/>'
    o += f'<circle cx="0" cy="-78" r="70" fill="{sp}" {L(s, .7)}/>'
    for a in range(0, 360, 40):
        r = math.radians(a)
        x, y = math.cos(r) * 42, -78 + math.sin(r) * 42
        o += f'<path d="M{x - 8:.0f},{y + 7:.0f} L{x:.0f},{y - 7:.0f} L{x + 8:.0f},{y + 7:.0f}" fill="none" {L(s, .6)}/>'
    if peek:
        o += f'<path d="M-22,-16 Q0,-40 22,-16 Q0,-4 -22,-16 Z" fill="{fc("tilo_face")}" {L(s, .8)}/>'
        o += f'<ellipse cx="0" cy="-22" rx="7" ry="5" fill="#111"/>'
        for sd in (-1, 1):
            o += f'<circle cx="{sd * 12}" cy="-30" r="3.5" fill="#111"/>'
    return o + '</g>'


def leaf_house(x, g, k=1.0, door=True):
    """Casita de hojas secas bajo el seto."""
    s = f'<path d="M{x - 120 * k},{g} Q{x - 110 * k},{g - 130 * k} {x},{g - 140 * k} Q{x + 110 * k},{g - 130 * k} {x + 120 * k},{g} Z" fill="#fff" {ST}/>'
    for dx, dy, a in ((-80, -40, -30), (-40, -95, 20), (30, -110, -10), (75, -60, 35), (-95, -12, 60), (95, -15, -60), (0, -125, 80)):
        s += leaf(x + dx * k, g + dy * k, 46 * k, a)
    if door:
        s += f'<path d="M{x - 34 * k},{g} Q{x - 34 * k},{g - 62 * k} {x},{g - 64 * k} Q{x + 34 * k},{g - 62 * k} {x + 34 * k},{g} Z" fill="#fff" {ST}/>'
    return s


def hedge(x0, x1, g, h=150):
    """Seto largo hecho de bultos."""
    s = ''
    x = x0
    i = 0
    while x < x1:
        w = 150 + (i % 3) * 25
        s += bush(x, g, w) if h >= 140 else bush(x, g, w * h / 150)
        x += w * .8
        i += 1
    return s


def brambles(x0, x1, g, h=260, seed=3):
    """Zarzas enredadas con espinas y moras."""
    import random
    rnd = random.Random(seed)
    s = ''
    for i in range(9):
        xa = x0 + (x1 - x0) * i / 8
        xb = xa + rnd.randint(-120, 120)
        top = g - h + rnd.randint(0, 80)
        d = f'M{xa:.0f},{g} C{xa + 60:.0f},{top + 40} {xb - 60:.0f},{top} {xb:.0f},{top + rnd.randint(20, 60)}'
        s += f'<path d="{d}" fill="none" {ST} stroke-width="5"/>'
        for t in (0.3, 0.55, 0.8):
            px = (1 - t) ** 3 * xa + 3 * (1 - t) ** 2 * t * (xa + 60) + 3 * (1 - t) * t * t * (xb - 60) + t ** 3 * xb
            py = (1 - t) ** 3 * g + 3 * (1 - t) ** 2 * t * (top + 40) + 3 * (1 - t) * t * t * top + t ** 3 * (top + 40)
            s += f'<path d="M{px - 6:.0f},{py:.0f} L{px:.0f},{py - 13:.0f} L{px + 6:.0f},{py:.0f}" fill="#fff" {ST} stroke-width="3"/>'
        bx, by = xb + rnd.randint(-30, 30), top + rnd.randint(40, 120)
        s += f'<circle cx="{bx}" cy="{by}" r="11" fill="#fff" {ST} stroke-width="3"/><circle cx="{bx + 15}" cy="{by + 6}" r="9" fill="#fff" {ST} stroke-width="3"/>'
        s += leaf(xb + rnd.randint(-40, 40), top + rnd.randint(60, 150), 34, rnd.randint(-60, 60))
    return s


def monster(cx, cy, k=1.0):
    """El monstruo que imaginan: una sombra enorme con pinchos y colmillos."""
    s = f'<path d="{_spikes(cx, cy, 120 * k, 88 * k, 14)} Z" fill="#fff" {ST}/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="{86 * k}" fill="#fff" {ST}/>'
    for sd in (-1, 1):
        s += f'<path d="M{cx + sd * 50 * k},{cy - 38 * k} L{cx + sd * 18 * k},{cy - 22 * k}" fill="none" {ST} stroke-width="5"/>'
        s += f'<circle cx="{cx + sd * 34 * k}" cy="{cy - 6 * k}" r="{12 * k}" fill="#fff" {ST}/><circle cx="{cx + sd * 34 * k}" cy="{cy - 6 * k}" r="{4 * k}" fill="#111"/>'
    s += f'<path d="M{cx - 50 * k},{cy + 30 * k} Q{cx},{cy + 70 * k} {cx + 50 * k},{cy + 30 * k} Z" fill="#fff" {ST}/>'
    for dx in (-30, 12):
        s += f'<path d="M{cx + dx * k},{cy + 34 * k} L{cx + (dx + 9) * k},{cy + 56 * k} L{cx + (dx + 18) * k},{cy + 36 * k}" fill="#fff" {ST} stroke-width="3.4"/>'
    return s


def bowl(x, g, k=1.0, water=True):
    s = f'<path d="M{x - 50 * k},{g - 30 * k} Q{x},{g + 18 * k} {x + 50 * k},{g - 30 * k} Z" fill="#fff" {ST}/>'
    s += f'<ellipse cx="{x}" cy="{g - 30 * k}" rx="{50 * k}" ry="{11 * k}" fill="#fff" {ST}/>'
    if water:
        s += f'<path d="M{x - 30 * k},{g - 31 * k} q8,-5 16,0 t16,0" fill="none" {ST} stroke-width="3"/>'
    return s


def road(x, y, w, h):
    """Carretera vista de lado, para el recuerdo de Tilo."""
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fff" {ST}/>'
    for i in range(int(w // 50)):
        s += f'<rect x="{x + 12 + i * 50}" y="{y + h / 2 - 4}" width="26" height="8" fill="#fff" {ST} stroke-width="2.6"/>'
    return s


def car(x, g, k=1.0):
    s = f'<path d="M{x - 70 * k},{g - 20 * k} L{x - 70 * k},{g - 50 * k} L{x - 40 * k},{g - 50 * k} L{x - 20 * k},{g - 78 * k} L{x + 40 * k},{g - 78 * k} L{x + 60 * k},{g - 50 * k} L{x + 75 * k},{g - 46 * k} L{x + 75 * k},{g - 20 * k} Z" fill="#fff" {ST}/>'
    s += f'<path d="M{x - 12 * k},{g - 70 * k} L{x + 8 * k},{g - 70 * k} L{x + 8 * k},{g - 52 * k} L{x - 26 * k},{g - 52 * k} Z M{x + 18 * k},{g - 70 * k} L{x + 36 * k},{g - 70 * k} L{x + 48 * k},{g - 52 * k} L{x + 18 * k},{g - 52 * k} Z" fill="#fff" {ST} stroke-width="3"/>'
    for dx in (-40, 45):
        s += f'<circle cx="{x + dx * k}" cy="{g - 18 * k}" r="{16 * k}" fill="#fff" {ST}/>'
    return s


def fence_hole(x0, x1, g, hx, h=90):
    """Valla con un agujero en la base para que pase un erizo."""
    s = fence(x0, x1, g, h)
    s += f'<path d="M{hx - 34},{g} L{hx - 34},{g - 30} Q{hx},{g - 52} {hx + 34},{g - 30} L{hx + 34},{g} Z" fill="#fff" {ST} stroke-width="3.6"/>'
    s += f'<path d="M{hx - 26},{g - 6} L{hx + 26},{g - 6}" fill="none" stroke="#fff" stroke-width="6"/>'
    return s


def leaf_pile(x, g, k=1.0):
    s = f'<path d="M{x - 80 * k},{g} Q{x},{g - 90 * k} {x + 80 * k},{g} Z" fill="#fff" {ST}/>'
    for dx, dy, a in ((-40, -22, -20), (0, -50, 30), (40, -24, 70), (-10, -12, -60), (25, -8, 10)):
        s += leaf(x + dx * k, g + dy * k, 34 * k, a)
    return s


def chispa(x, y, k=1.0):
    """Chispa, la luciernaga escondida: cuerpo, alas y luz."""
    s = f'<g transform="translate({x},{y}) scale({k})">'
    for a in (-70, -35, 0, 35, 70, 110, 145, 180, 215, 250):
        r = math.radians(a)
        s += f'<path d="M{math.cos(r) * 24:.0f},{12 + math.sin(r) * 24:.0f} L{math.cos(r) * 34:.0f},{12 + math.sin(r) * 34:.0f}" fill="none" {ST} stroke-width="3"/>'
    s += f'<ellipse cx="0" cy="12" rx="11" ry="15" fill="#fff" {ST} stroke-width="3.4"/>'
    s += f'<ellipse cx="-14" cy="-6" rx="13" ry="8" transform="rotate(-30 -14 -6)" fill="#fff" {ST} stroke-width="3"/>'
    s += f'<ellipse cx="14" cy="-6" rx="13" ry="8" transform="rotate(30 14 -6)" fill="#fff" {ST} stroke-width="3"/>'
    s += f'<circle cx="0" cy="-10" r="9" fill="#fff" {ST} stroke-width="3.4"/>'
    s += f'<path d="M-4,-18 Q-10,-30 -16,-30 M4,-18 Q10,-30 16,-30" fill="none" {ST} stroke-width="2.6"/>'
    return s + '</g>'
