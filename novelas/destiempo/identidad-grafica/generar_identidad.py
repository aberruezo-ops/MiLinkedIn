# Identidad grafica de DESTIEMPO: logotipo, paleta, motivos y portadas conceptuales.
# Uso: python3 generar_identidad.py  (genera HTML) y luego node render.js
import math
import random
import os

INK, PAPER, AMBER, CIAN, INDIGO = '#0B0B10', '#F2EEE6', '#FFB000', '#5BD3E8', '#1A1B3A'
AQUI = os.path.dirname(os.path.abspath(__file__))

CSS = """
@font-face{font-family:'Bebas Neue';src:url('fonts/bebas-neue-latin-400-normal.woff2')}
@font-face{font-family:'Space Grotesk';font-weight:500;src:url('fonts/space-grotesk-latin-500-normal.woff2')}
@font-face{font-family:'Space Grotesk';font-weight:700;src:url('fonts/space-grotesk-latin-700-normal.woff2')}
html,body{margin:0;padding:0;background:#0B0B10}
svg{display:block}
"""


def halftone(w, h, spacing=9, maxr=3.2, mode='bottom', color=PAPER, op=.16, x0=0, y0=0):
    out = []
    for j in range(int(h / (spacing * .9)) + 1):
        for i in range(int(w / spacing) + 1):
            x = i * spacing + (spacing / 2 if j % 2 else 0)
            y = j * spacing * .9
            if mode == 'bottom':
                t = max(0, (y / h - .45) / .55)
            elif mode == 'top':
                t = max(0, (.5 - y / h) / .5)
            elif mode == 'radial':
                t = math.hypot(x - w / 2, y - h / 2) / math.hypot(w / 2, h / 2)
            else:
                t = x / w
            r = maxr * t ** 1.3
            if r > .4:
                out.append(f'<circle cx="{x + x0:.1f}" cy="{y + y0:.1f}" r="{r:.2f}"/>')
    return f'<g fill="{color}" opacity="{op}">' + ''.join(out) + '</g>'


def wordmark(uid, cx, base, size, fill=PAPER, ghost=True, glitch=True):
    """DESTIEMPO partido en dos: la mitad de arriba va un segundo adelantada."""
    cap = size * .7
    split = base - cap * .52
    sh = size * .045
    ls = size * .03
    w = size * 3.55

    def txt(col):
        return (f'<text x="{cx}" y="{base}" text-anchor="middle" font-family="Bebas Neue" font-size="{size}" '
                f'letter-spacing="{ls}" fill="{col}">DESTIEMPO</text>')
    top_y, bot_y = base - size, split
    s = (f'<defs><clipPath id="{uid}t"><rect x="-3000" y="{top_y}" width="9000" height="{split - top_y}"/></clipPath>'
         f'<clipPath id="{uid}b"><rect x="-3000" y="{bot_y}" width="9000" height="{size}"/></clipPath>'
         f'<clipPath id="{uid}g1"><rect x="-3000" y="{base - cap * .86}" width="9000" height="{cap * .06}"/></clipPath>'
         f'<clipPath id="{uid}g2"><rect x="-3000" y="{base - cap * .2}" width="9000" height="{cap * .05}"/></clipPath></defs>')
    s += f'<line x1="{cx - w / 2 - size * .1:.0f}" y1="{split:.1f}" x2="{cx + w / 2 + size * .1:.0f}" y2="{split:.1f}" stroke="{AMBER}" stroke-width="{max(1.5, size * .012):.1f}"/>'
    for xx in (cx - w / 2 - size * .1, cx + w / 2 + size * .1):
        s += f'<circle cx="{xx:.0f}" cy="{split:.1f}" r="{max(2, size * .016):.1f}" fill="{AMBER}"/>'
    if ghost:
        s += f'<g clip-path="url(#{uid}t)" opacity=".38"><g transform="translate({-sh * 1.0:.1f},0)">{txt(AMBER)}</g></g>'
    s += f'<g clip-path="url(#{uid}b)">{txt(fill)}</g>'
    s += f'<g clip-path="url(#{uid}t)"><g transform="translate({sh:.1f},0)">{txt(fill)}</g></g>'
    if glitch:
        s += f'<g clip-path="url(#{uid}g2)" opacity=".95"><g transform="translate({-sh * 2.4:.1f},0)">{txt(CIAN)}</g></g>'
    return s


def logo_svg(bg=True):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1500 440" width="1500" height="440">'
    if bg:
        s += f'<rect width="1500" height="440" fill="{INK}"/>'
    s += wordmark('lg', 750, 320, 340)
    s += f'<text x="750" y="398" text-anchor="middle" font-family="Space Grotesk" font-weight="500" font-size="27" letter-spacing="13" fill="{PAPER}" opacity=".85">HAY PERSONAS QUE VIVEN A OTRA HORA</text>'
    s += f'<text x="1400" y="{320 - 340 * .7 * .52 - 14:.0f}" text-anchor="end" font-family="Space Grotesk" font-weight="700" font-size="22" letter-spacing="4" fill="{AMBER}">4:17</text>'
    return s + '</svg>'


# --------------------------------------------------------------- figuras
def boy(x, base, h, fill='#000', rim=PAPER, rimop=.75, hair=None):
    """Chico de espaldas: hoodie, brazos, mochila y pelo desordenado."""
    k = h / 130
    sw = f'stroke="{rim}" stroke-width="{max(1, 1.2 * k):.1f}" stroke-opacity="{rimop}" stroke-linejoin="round"'
    f = lambda v: f'{v:.1f}'
    s = f'<rect x="{f(x - 18 * k)}" y="{f(base - 100 * k)}" width="{f(36 * k)}" height="{f(46 * k)}" rx="{f(7 * k)}" fill="{fill}" {sw}/>'
    for sd in (-1, 1):  # piernas y zapatillas
        px = x + sd * 8 * k
        s += f'<path d="M{f(px - 6 * k)},{f(base - 50 * k)} L{f(px + 6 * k)},{f(base - 50 * k)} L{f(px + 5.5 * k)},{f(base - 6 * k)} L{f(px - 5.5 * k)},{f(base - 6 * k)} Z" fill="{fill}" {sw}/>'
        s += f'<ellipse cx="{f(px + sd * 1.5 * k)}" cy="{f(base - 3 * k)}" rx="{f(8 * k)}" ry="{f(4 * k)}" fill="{fill}" {sw}/>'
    s += (f'<path d="M{f(x - 25 * k)},{f(base - 94 * k)} C{f(x - 25 * k)},{f(base - 106 * k)} {f(x - 10 * k)},{f(base - 109 * k)} {f(x)},{f(base - 109 * k)} '
          f'C{f(x + 10 * k)},{f(base - 109 * k)} {f(x + 25 * k)},{f(base - 106 * k)} {f(x + 25 * k)},{f(base - 94 * k)} L{f(x + 20 * k)},{f(base - 46 * k)} L{f(x - 20 * k)},{f(base - 46 * k)} Z" fill="{fill}" {sw}/>')
    for sd in (-1, 1):  # brazos
        s += (f'<path d="M{f(x + sd * 23 * k)},{f(base - 100 * k)} L{f(x + sd * 31 * k)},{f(base - 90 * k)} L{f(x + sd * 31 * k)},{f(base - 52 * k)} '
              f'L{f(x + sd * 24 * k)},{f(base - 52 * k)} L{f(x + sd * 20 * k)},{f(base - 86 * k)} Z" fill="{fill}" {sw}/>')
    s += f'<ellipse cx="{f(x)}" cy="{f(base - 108 * k)}" rx="{f(14 * k)}" ry="{f(6 * k)}" fill="{fill}" {sw}/>'
    s += f'<ellipse cx="{f(x)}" cy="{f(base - 121 * k)}" rx="{f(11.5 * k)}" ry="{f(13 * k)}" fill="{fill}" {sw}/>'
    spikes = [(-12, -3), (-10, -11), (-6, -8), (-4, -17), (0, -10), (5, -13), (9, -9), (12, -2)]
    pts = ' '.join(f'{f(x + dx * k)},{f(base - 121 * k + dy * k)}' for dx, dy in spikes)
    s += f'<polygon points="{pts}" fill="{fill}" {sw}/>'
    if hair:
        s += f'<path d="M{f(x - 2 * k)},{f(base - 143 * k)} q{f(3 * k)},{f(-8 * k)} {f(8 * k)},{f(-3 * k)}" fill="none" stroke="{hair}" stroke-width="{f(3.2 * k)}" stroke-linecap="round"/>'
    return s


def girl(x, base, h, fill='#000', rim=PAPER):
    k = h / 130
    f = lambda v: f'{v:.1f}'
    s = boy(x, base, h, fill, rim, .85)
    sw = f'stroke="{rim}" stroke-width="{max(1, 1.2 * k):.1f}" stroke-opacity=".8" stroke-linejoin="round"'
    s += f'<path d="M{f(x - 13 * k)},{f(base - 124 * k)} Q{f(x - 17 * k)},{f(base - 100 * k)} {f(x - 12 * k)},{f(base - 98 * k)} L{f(x + 12 * k)},{f(base - 98 * k)} Q{f(x + 17 * k)},{f(base - 100 * k)} {f(x + 13 * k)},{f(base - 124 * k)} Z" fill="{fill}" {sw}/>'
    s += f'<path d="M{f(x - 17 * k)},{f(base - 120 * k)} Q{f(x)},{f(base - 150 * k)} {f(x + 17 * k)},{f(base - 120 * k)}" fill="none" stroke="{PAPER}" stroke-width="{f(3 * k)}" stroke-linecap="round"/>'
    for sd in (-1, 1):
        s += f'<ellipse cx="{f(x + sd * 17 * k)}" cy="{f(base - 118 * k)}" rx="{f(5 * k)}" ry="{f(7 * k)}" fill="{fill}" stroke="{PAPER}" stroke-width="{f(2 * k)}"/>'
    return s


def elder(x, base, h):
    k = h / 130
    f = lambda v: f'{v:.1f}'
    sw = f'stroke="{PAPER}" stroke-width="{1.3 * k:.1f}" stroke-opacity=".8" stroke-linejoin="round"'
    s = (f'<path d="M{f(x - 26 * k)},{f(base - 98 * k)} C{f(x - 26 * k)},{f(base - 108 * k)} {f(x - 10 * k)},{f(base - 111 * k)} {f(x)},{f(base - 111 * k)} '
         f'C{f(x + 10 * k)},{f(base - 111 * k)} {f(x + 26 * k)},{f(base - 108 * k)} {f(x + 26 * k)},{f(base - 98 * k)} L{f(x + 34 * k)},{f(base - 3 * k)} L{f(x - 34 * k)},{f(base - 3 * k)} Z" fill="#000" {sw}/>')
    s += f'<path d="M{f(x)},{f(base - 108 * k)} L{f(x)},{f(base - 3 * k)}" stroke="{PAPER}" stroke-width="{k:.1f}" opacity=".4"/>'
    s += f'<path d="M{f(x - 15 * k)},{f(base - 108 * k)} L{f(x)},{f(base - 90 * k)} L{f(x + 15 * k)},{f(base - 108 * k)}" fill="none" stroke="{PAPER}" stroke-width="{k:.1f}" opacity=".5"/>'
    s += f'<ellipse cx="{f(x)}" cy="{f(base - 122 * k)}" rx="{f(11.5 * k)}" ry="{f(13 * k)}" fill="#000" {sw}/>'
    spikes = [(-12, -3), (-10, -11), (-6, -8), (-4, -17), (0, -10), (5, -13), (9, -9), (12, -2)]
    pts = ' '.join(f'{f(x + dx * k)},{f(base - 122 * k + dy * k)}' for dx, dy in spikes)
    s += f'<polygon points="{pts}" fill="{PAPER}"/>'
    return s


def clock(cx, cy, r, hh=4, mm=17, col=PAPER, cracks=True, extra=True, seed=3):
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="3"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="{r * .94:.1f}" fill="none" stroke="{col}" stroke-width="1" opacity=".45"/>'
    for i in range(60):
        a = math.radians(i * 6 - 90)
        r1 = r * (.84 if i % 5 == 0 else .9)
        r2 = r * .93
        s += (f'<line x1="{cx + math.cos(a) * r1:.1f}" y1="{cy + math.sin(a) * r1:.1f}" x2="{cx + math.cos(a) * r2:.1f}" y2="{cy + math.sin(a) * r2:.1f}" '
              f'stroke="{col}" stroke-width="{2.4 if i % 5 == 0 else 1}" opacity="{.9 if i % 5 == 0 else .5}"/>')
    ah, am = math.radians((hh % 12) * 30 + mm * .5 - 90), math.radians(mm * 6 - 90)
    s += f'<line x1="{cx}" y1="{cy}" x2="{cx + math.cos(ah) * r * .5:.1f}" y2="{cy + math.sin(ah) * r * .5:.1f}" stroke="{col}" stroke-width="6" stroke-linecap="round"/>'
    s += f'<line x1="{cx}" y1="{cy}" x2="{cx + math.cos(am) * r * .78:.1f}" y2="{cy + math.sin(am) * r * .78:.1f}" stroke="{col}" stroke-width="3.6" stroke-linecap="round"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="7" fill="{col}"/>'
    if extra:  # el segundo de mas: una aguja ambar que flota fuera del eje
        a2 = math.radians(mm * 6 + 24 - 90)
        s += (f'<line x1="{cx + math.cos(a2) * r * .3:.1f}" y1="{cy + math.sin(a2) * r * .3:.1f}" x2="{cx + math.cos(a2) * r * .95:.1f}" y2="{cy + math.sin(a2) * r * .95:.1f}" '
              f'stroke="{AMBER}" stroke-width="2.4" stroke-linecap="round"/>')
    if cracks:
        rnd = random.Random(seed)
        for base_ang in (-30, 35, 110, 200):
            pts = [(cx, cy)]
            a = math.radians(base_ang)
            for step in range(1, 6):
                a += rnd.uniform(-.35, .35)
                d = step * r / 5
                pts.append((cx + math.cos(a) * d, cy + math.sin(a) * d))
            p = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
            s += f'<polyline points="{p}" fill="none" stroke="{AMBER}" stroke-width="9" opacity=".18" stroke-linejoin="round"/>'
            s += f'<polyline points="{p}" fill="none" stroke="{AMBER}" stroke-width="2.4" stroke-linejoin="round"/>'
    return s


def dust(w, h, n, seed, amber=2):
    rnd = random.Random(seed)
    s = ''
    for i in range(n):
        x, y, r = rnd.uniform(15, w - 15), rnd.uniform(40, h * .75), rnd.choice((1.2, 1.8, 2.6))
        col = AMBER if i < amber else PAPER
        s += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}" opacity="{.9 if col == AMBER else .45}"/>'
    return s


def droplet(x, y, k=1.0, col=AMBER):
    return (f'<path d="M{x},{y - 18 * k} Q{x + 12 * k},{y + 2 * k} {x},{y + 12 * k} Q{x - 12 * k},{y + 2 * k} {x},{y - 18 * k} Z" fill="{col}"/>'
            f'<circle cx="{x - 3 * k}" cy="{y + 2 * k}" r="{2 * k}" fill="{PAPER}" opacity=".7"/>')


def skyline(seed, base, w=400, col=PAPER, fill=INK, opacity=1.0):
    rnd = random.Random(seed)
    s = ''
    x = 0
    while x < w:
        bw = rnd.randint(22, 46)
        bh = rnd.randint(40, 120)
        s += f'<rect x="{x}" y="{base - bh}" width="{bw}" height="{bh}" fill="{fill}" stroke="{col}" stroke-width="1.2" opacity="{opacity}"/>'
        for wy in range(base - bh + 8, base - 6, 12):
            for wx in range(x + 5, x + bw - 6, 9):
                if rnd.random() > .55:
                    s += f'<rect x="{wx}" y="{wy}" width="4" height="5" fill="{col}" opacity=".35"/>'
        x += bw + 2
    # torres inclinadas tipo Puerta de Europa
    for sd, bx in ((1, 70), (-1, 150)):
        pts = f'{bx},{base} {bx + 34},{base} {bx + 34 + sd * 40},{base - 190} {bx + sd * 40},{base - 190}'
        s += f'<polygon points="{pts}" fill="{fill}" stroke="{col}" stroke-width="1.8"/>'
        for yy in range(base - 180, base - 10, 14):
            off = sd * 40 * (base - yy) / 190
            s += f'<line x1="{bx + sd * 40 - off:.1f}" y1="{yy}" x2="{bx + 34 + sd * 40 - off:.1f}" y2="{yy}" stroke="{col}" stroke-width=".8" opacity=".4"/>'
    return s


def cover(n, uid):
    """Portada 400 x 600. n = 1, 2 o 3."""
    W, H = 400, 600
    s = f'<rect width="{W}" height="{H}" fill="{INK}"/>'
    s += halftone(W, H, 9, 3.4, 'bottom', PAPER, .15)
    s += halftone(W, H, 9, 2.8, 'top', PAPER, .09)
    titles = {1: ('EL SEGUNDO DE MÁS', 'I'), 2: ('LA HORA QUE NADIE MIRA', 'II'), 3: ('A TIEMPO', 'III')}
    if n == 1:
        s += clock(200, 335, 138, 4, 17, seed=3)
        # pelota congelada con eco
        for i, op in ((3, .12), (2, .22), (1, .4)):
            s += f'<circle cx="{262 + i * 22}" cy="{402 - i * 2}" r="17" fill="none" stroke="{PAPER}" stroke-width="1.6" opacity="{op}"/>'
        s += f'<circle cx="262" cy="402" r="17" fill="{INK}" stroke="{PAPER}" stroke-width="2.2"/><path d="M247,398 Q262,390 277,398 M249,410 Q262,404 275,410" fill="none" stroke="{PAPER}" stroke-width="1.4"/>'
        s += dust(W, H, 28, 4)
        s += droplet(140, 395, 1.3)
        s += boy(200, 500, 150, hair=PAPER)
    elif n == 2:
        s += f'<g opacity=".95">{skyline(7, 330)}</g>'
        s += f'<g transform="translate(0,660) scale(1,-1)" opacity=".7">{skyline(7, 330, col=CIAN, fill=INDIGO)}</g>'
        s += f'<rect x="0" y="334" width="{W}" height="266" fill="{INK}" opacity=".35"/>'
        for yy in (352, 388, 430, 480):
            s += f'<rect x="{random.Random(yy).randint(0, 180)}" y="{yy}" width="{random.Random(yy + 1).randint(60, 220)}" height="3" fill="{CIAN}" opacity=".35"/>'
        s += f'<line x1="0" y1="331" x2="{W}" y2="331" stroke="{AMBER}" stroke-width="2.4"/>'
        s += f'<circle cx="{W - 40}" cy="331" r="4" fill="{AMBER}"/>'
        s += boy(182, 331, 96, rimop=.9) + girl(224, 331, 90)
        s += dust(W, H, 18, 6)
    else:
        s += clock(200, 330, 150, 4, 18, seed=9, extra=False)
        s += f'<rect x="200" y="0" width="200" height="{H}" fill="{INK}" opacity=".35"/>'
        # grieta central ambar
        pts = [(200, 0)]
        rnd = random.Random(5)
        y = 0
        while y < H:
            y += rnd.randint(40, 70)
            pts.append((200 + rnd.randint(-16, 16), min(y, H)))
        p = ' '.join(f'{x},{y}' for x, y in pts)
        s += f'<polyline points="{p}" fill="none" stroke="{AMBER}" stroke-width="16" opacity=".16" stroke-linejoin="round"/>'
        s += f'<polyline points="{p}" fill="none" stroke="{AMBER}" stroke-width="3.2" stroke-linejoin="round"/>'
        s += boy(120, 500, 120, hair=PAPER) + elder(285, 500, 160)
        s += dust(W, H, 22, 8)
    t, rn = titles[n]
    s += wordmark(f'{uid}w', 200, 118, 84)
    s += f'<text x="200" y="168" text-anchor="middle" font-family="Space Grotesk" font-weight="700" font-size="{19 if n == 2 else 22}" letter-spacing="6" fill="{AMBER}">{t}</text>'
    s += f'<text x="30" y="572" font-family="Space Grotesk" font-weight="500" font-size="12" letter-spacing="7" fill="{PAPER}" opacity=".9">ALEX BERRUEZO</text>'
    s += f'<circle cx="362" cy="562" r="20" fill="none" stroke="{AMBER}" stroke-width="2"/><text x="362" y="571" text-anchor="middle" font-family="Bebas Neue" font-size="26" fill="{AMBER}">{rn}</text>'
    return s


def cover_svg(n):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 600" width="800" height="1200">{cover(n, f"c{n}")}</svg>')


# --------------------------------------------------------------- tablero
def tile(x, y, w, h, title, sub, inner):
    s = f'<g transform="translate({x},{y})"><rect width="{w}" height="{h}" rx="6" fill="{INK}" stroke="{PAPER}" stroke-opacity=".25"/>'
    s += f'<g clip-path="url(#tile{x}{y})">{inner}</g><defs><clipPath id="tile{x}{y}"><rect width="{w}" height="{h - 60}" rx="6"/></clipPath></defs>'
    s += f'<line x1="0" y1="{h - 60}" x2="{w}" y2="{h - 60}" stroke="{PAPER}" stroke-opacity=".25"/>'
    s += f'<text x="18" y="{h - 34}" font-family="Space Grotesk" font-weight="700" font-size="17" letter-spacing="4" fill="{AMBER}">{title}</text>'
    s += f'<text x="18" y="{h - 12}" font-family="Space Grotesk" font-weight="500" font-size="14" fill="{PAPER}" opacity=".8">{sub}</text></g>'
    return s


def board():
    W, H = 2400, 2060
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><rect width="{W}" height="{H}" fill="{INK}"/>'
    s += halftone(W, H, 14, 4.4, 'radial', PAPER, .05)
    # cabecera
    s += f'<g transform="translate(70,40)">{logo_svg(False).replace("<svg", "<svg x=\"0\" y=\"0\" width=\"1400\" height=\"411\"", 1)}</g>'
    s += f'<text x="1560" y="150" font-family="Space Grotesk" font-weight="700" font-size="40" letter-spacing="3" fill="{AMBER}">MANGA NOIR DEL</text>'
    s += f'<text x="1560" y="198" font-family="Space Grotesk" font-weight="700" font-size="40" letter-spacing="3" fill="{AMBER}">TIEMPO ROTO</text>'
    for i, line in enumerate(('Tinta, tramas de puntos y una sola luz: el ámbar de las 4:17.',
                              'En cada ilustración se esconde un segundo de más.',
                              'Tiempo estirado: ecos. Tiempo perdido: glitch.',
                              'Madrid de ladrillo y neón. El Destiempo, congelado en cian.')):
        s += f'<text x="1560" y="{262 + i * 44}" font-family="Space Grotesk" font-weight="500" font-size="24" fill="{PAPER}">{line}</text>'
    # paleta
    y0 = 520
    s += f'<text x="70" y="{y0}" font-family="Space Grotesk" font-weight="700" font-size="20" letter-spacing="6" fill="{PAPER}" opacity=".6">PALETA</text>'
    pal = [(INK, 'TINTA', '#0B0B10', '60 %'), (PAPER, 'PAPEL', '#F2EEE6', '25 %'), (AMBER, 'ÁMBAR 4:17', '#FFB000', '8 %'),
           (CIAN, 'CIAN DESTIEMPO', '#5BD3E8', '4 %'), (INDIGO, 'ÍNDIGO NOCHE', '#1A1B3A', '3 %')]
    for i, (c, n, hx, p) in enumerate(pal):
        x = 70 + i * 300
        s += f'<rect x="{x}" y="{y0 + 24}" width="270" height="150" rx="6" fill="{c}" stroke="{PAPER}" stroke-opacity=".4"/>'
        tc = INK if c in (PAPER, AMBER, CIAN) else PAPER
        s += f'<text x="{x + 16}" y="{y0 + 70}" font-family="Space Grotesk" font-weight="700" font-size="20" letter-spacing="2" fill="{tc}">{n}</text>'
        s += f'<text x="{x + 16}" y="{y0 + 100}" font-family="Space Grotesk" font-weight="500" font-size="18" fill="{tc}">{hx}</text>'
        s += f'<text x="{x + 16}" y="{y0 + 150}" font-family="Bebas Neue" font-size="46" fill="{tc}" opacity=".9">{p}</text>'
    # tipografia
    s += f'<text x="1620" y="{y0}" font-family="Space Grotesk" font-weight="700" font-size="20" letter-spacing="6" fill="{PAPER}" opacity=".6">TIPOGRAFÍA</text>'
    s += f'<text x="1620" y="{y0 + 100}" font-family="Bebas Neue" font-size="104" letter-spacing="3" fill="{PAPER}">BEBAS NEUE</text>'
    s += f'<text x="1620" y="{y0 + 132}" font-family="Space Grotesk" font-weight="500" font-size="19" fill="{PAPER}" opacity=".8">Títulos y logotipo</text>'
    s += f'<text x="1620" y="{y0 + 172}" font-family="Space Grotesk" font-weight="700" font-size="34" fill="{AMBER}">Space Grotesk</text>'
    s += f'<text x="2000" y="{y0 + 172}" font-family="Space Grotesk" font-weight="500" font-size="19" fill="{PAPER}" opacity=".8">Textos, pantallas y chats</text>'
    # motivos
    y1 = 760
    s += f'<text x="70" y="{y1 - 20}" font-family="Space Grotesk" font-weight="700" font-size="20" letter-spacing="6" fill="{PAPER}" opacity=".6">LOS CUATRO MOTIVOS</text>'
    ts = 540
    eco = ''.join(f'<g opacity="{o}" transform="translate({-dx},0)">{boy(270, 275, 190, "#000", PAPER, .8)}</g>' for dx, o in ((110, .12), (74, .22), (38, .45))) + boy(270, 275, 190, hair=PAPER)
    s += tile(70, y1, ts, 360, 'ECO', 'tiempo estirado: copias que se quedan atrás', eco)
    gl = ''
    for (ya, yb, dx, col) in ((0, 140, 20, PAPER), (140, 190, -26, CIAN), (190, 300, 0, PAPER)):
        gl += f'<defs><clipPath id="gl{ya}"><rect x="0" y="{ya}" width="{ts}" height="{yb - ya}"/></clipPath></defs><g clip-path="url(#gl{ya})"><g transform="translate({dx},0)">{boy(270, 275, 190, "#000", col, 1)}</g></g>'
    s += tile(70 + 600, y1, ts, 360, 'GLITCH', 'tiempo perdido: la imagen se corta como un vídeo roto', gl)
    tr = halftone(ts, 300, 12, 5.2, 'radial', PAPER, .85)
    tr = f'<g transform="translate(0,0)">{tr}</g><circle cx="{ts / 2}" cy="150" r="70" fill="{INK}"/><circle cx="{ts / 2}" cy="150" r="70" fill="none" stroke="{PAPER}" stroke-width="2"/>'
    s += tile(70 + 1200, y1, ts, 360, 'TRAMA', 'sombra hecha de puntos, nunca degradados lisos', tr)
    sg = f'<rect width="{ts}" height="300" fill="{INK}"/>' + halftone(ts, 300, 12, 3, 'bottom', PAPER, .2)
    sg += f'<line x1="{ts / 2}" y1="0" x2="{ts / 2}" y2="110" stroke="{PAPER}" stroke-width="1.5" opacity=".5"/>' + droplet(ts / 2, 140, 3.2)
    sg += f'<ellipse cx="{ts / 2}" cy="262" rx="46" ry="9" fill="none" stroke="{PAPER}" stroke-width="1.5" opacity=".5"/><ellipse cx="{ts / 2 + 18}" cy="266" rx="40" ry="7" fill="none" stroke="{AMBER}" stroke-width="1.5"/>'
    s += tile(70 + 1800, y1, ts - 40, 360, 'EL SEGUNDO DE MÁS', 'una cosa fuera de hora en cada imagen', sg)
    # portadas
    y2 = 1170
    s += f'<text x="70" y="{y2 - 24}" font-family="Space Grotesk" font-weight="700" font-size="20" letter-spacing="6" fill="{PAPER}" opacity=".6">LAS TRES PORTADAS (CONCEPTO)</text>'
    for i in range(3):
        x = 70 + i * 780
        s += f'<g transform="translate({x},{y2}) scale(1.4)">{cover(i + 1, f"b{i}")}</g><rect x="{x}" y="{y2}" width="560" height="840" fill="none" stroke="{PAPER}" stroke-opacity=".3"/>'
    s += f'<text x="{70 + 600}" y="{y2 + 880}" font-family="Space Grotesk" font-weight="500" font-size="22" fill="{PAPER}" opacity=".8">I · el balón que no llega · II · Madrid y su reflejo · III · dos Edus, una grieta</text>'
    return s + '</svg>'


def pagina(svg):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{svg}</body></html>'


if __name__ == '__main__':
    open(os.path.join(AQUI, 'logo.html'), 'w').write(pagina(logo_svg()))
    open(os.path.join(AQUI, 'logo_transparente.html'), 'w').write(pagina(logo_svg(False).replace(f'<line', '<line', 1)).replace('background:#0B0B10', 'background:transparent'))
    for i in (1, 2, 3):
        open(os.path.join(AQUI, f'portada{i}.html'), 'w').write(pagina(cover_svg(i)))
    open(os.path.join(AQUI, 'tablero.html'), 'w').write(pagina(board()))
    print('ok')
