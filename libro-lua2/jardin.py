# Hera (labradora) y decorado de jardin para el libro 2.
from animales import *


# ------------------------------------------------------------- Hera
def hera_sit(cx, g, s=1.0, mood='smile', flip=1, look=0):
    """Labradora mayor sentada de frente. Pies en g; altura total ~330*s."""
    body, light, gray, dark = fc('hera_body'), fc('hera_light'), fc('hera_gray'), fc('hera_dark', '#111')
    o = grp(cx, g, s, flip)
    o += tube2('M92,-46 Q172,-38 178,-104', 44, body, s)
    for sd in (-1, 1):
        o += f'<ellipse cx="{sd * 92}" cy="-66" rx="52" ry="64" fill="{body}" {L(s)}/>'
        o += f'<ellipse cx="{sd * 96}" cy="-12" rx="40" ry="17" fill="{body}" {L(s)}/>'
    o += f'<path d="M-92,-130 Q-118,-8 -62,-4 L62,-4 Q118,-8 92,-130 Q64,-215 0,-215 Q-64,-215 -92,-130 Z" fill="{body}" {L(s)}/>'
    o += f'<ellipse cx="0" cy="-92" rx="44" ry="76" fill="{light}" {L(s, .75)}/>'
    for sd in (-1, 1):
        x = sd * 38
        o += tube2(f'M{x},-130 L{x},-26', 46, body, s)
        o += f'<ellipse cx="{x + sd * 2}" cy="-10" rx="38" ry="17" fill="{body}" {L(s)}/>'
        o += f'<path d="M{x - 10},-22 L{x - 10},-6 M{x + 8},-22 L{x + 8},-6" fill="none" {L(s, .6)}/>'
    o += f'<path d="M-56,-216 Q0,-194 56,-216 L52,-198 Q0,-176 -52,-198 Z" fill="{fc("hera_collar")}" {L(s, .9)}/>'
    o += f'<circle cx="0" cy="-176" r="11" fill="{fc("hera_tag", "#fff")}" {L(s, .8)}/>'
    o += f'<ellipse cx="0" cy="-262" rx="80" ry="68" fill="{body}" {L(s)}/>'
    for sd in (-1, 1):
        o += (f'<path d="M{sd * 60},-318 Q{sd * 122},-304 {sd * 106},-212 Q{sd * 90},-192 {sd * 72},-228 Z" '
              f'fill="{body}" {L(s)}/>')
    o += f'<path d="M-50,-262 Q-56,-210 0,-206 Q56,-210 50,-262 Q0,-284 -50,-262 Z" fill="{gray}" {L(s, .9)}/>'
    for px, py in ((-30, -238), (-18, -224), (-4, -232), (14, -222), (28, -238), (22, -250), (-24, -250), (6, -214)):
        o += f'<path d="M{px},{py} l5,3" fill="none" {L(s, .55)}/>'
    o += f'<ellipse cx="0" cy="-256" rx="22" ry="14" fill="{dark}" {L(s, .8)}/>'
    if mood == 'smile':
        o += f'<path d="M0,-242 L0,-228 M-30,-228 Q-15,-208 0,-228 Q15,-208 30,-228" fill="none" {L(s, .9)}/>'
    elif mood == 'open':
        o += f'<path d="M-26,-230 Q0,-190 26,-230 Z" fill="{fc("mouth")}" {L(s, .85)}/><path d="M0,-242 L0,-230" fill="none" {L(s, .85)}/>'
    for sd in (-1, 1):
        ex = sd * 34
        if mood == 'sleep':
            o += f'<path d="M{ex - 12},-282 Q{ex},-268 {ex + 12},-282" fill="none" {L(s, 1.1)}/>'
        else:
            o += f'<ellipse cx="{ex + look * 3}" cy="-284" rx="9" ry="11" fill="#111"/><circle cx="{ex + look * 3 + 3}" cy="-288" r="3.4" fill="#fff"/>'
        o += f'<path d="M{ex - 12},-266 q12,8 24,0" fill="none" {L(s, .6)}/>'
        o += f'<path d="M{sd * 50},-304 Q{sd * 36},-316 {sd * 20},-306" fill="none" {L(s, .9)}/>'
    o += f'<path d="M-22,-322 q22,-9 44,0 M-14,-333 q14,-6 28,0" fill="none" {L(s, .6)}/>'
    return o + '</g>'


def hera_lie(cx, g, s=1.0, flip=1, mood='smile'):
    """Hera tumbada de perfil mirando a la derecha."""
    body, light, gray, dark = fc('hera_body'), fc('hera_light'), fc('hera_gray'), fc('hera_dark', '#111')
    o = grp(cx, g, s, flip)
    o += tube2('M-150,-38 Q-218,-30 -232,-6', 38, body, s)
    o += f'<ellipse cx="-12" cy="-74" rx="138" ry="64" fill="{body}" {L(s)}/>'
    o += f'<ellipse cx="-92" cy="-52" rx="62" ry="50" fill="{body}" {L(s)}/>'
    o += f'<ellipse cx="-42" cy="-10" rx="46" ry="17" fill="{body}" {L(s)}/>'
    o += tube2('M62,-40 L190,-26', 42, body, s)
    o += f'<ellipse cx="206" cy="-24" rx="36" ry="21" fill="{body}" {L(s)}/>'
    o += f'<path d="M190,-36 L190,-14 M206,-38 L206,-12" fill="none" {L(s, .6)}/>'
    o += f'<ellipse cx="150" cy="-112" rx="66" ry="58" fill="{body}" {L(s)}/>'
    o += f'<path d="M168,-120 Q226,-124 244,-96 Q246,-62 200,-58 Q160,-60 160,-96 Z" fill="{gray}" {L(s, .9)}/>'
    o += f'<ellipse cx="246" cy="-98" rx="13" ry="10" fill="{dark}" {L(s, .8)}/>'
    for px, py in ((184, -90), (200, -78), (214, -86), (226, -72)):
        o += f'<path d="M{px},{py} l5,3" fill="none" {L(s, .55)}/>'
    o += f'<path d="M232,-82 Q216,-70 200,-80" fill="none" {L(s, .9)}/>'
    if mood == 'sleep':
        o += f'<path d="M168,-130 Q180,-118 192,-130" fill="none" {L(s, 1.1)}/>'
    else:
        o += f'<ellipse cx="180" cy="-130" rx="8" ry="10" fill="#111"/><circle cx="183" cy="-134" r="3" fill="#fff"/>'
    o += f'<path d="M168,-146 Q182,-156 196,-148" fill="none" {L(s, .9)}/>'
    o += f'<path d="M122,-150 Q96,-110 118,-56 Q148,-52 158,-92 Q160,-130 122,-150 Z" fill="{body}" {L(s)}/>'
    return o + '</g>'


# ------------------------------------------------------------- plantas
def leaf(x, y, size=40, ang=0, vein=True):
    s = f'<g transform="translate({x},{y}) rotate({ang})">'
    s += f'<path d="M0,0 Q{size * .55:.0f},{-size * .5:.0f} {size:.0f},0 Q{size * .55:.0f},{size * .5:.0f} 0,0 Z" fill="{fc("leaf")}" {ST} stroke-width="3.4"/>'
    if vein:
        s += f'<path d="M2,0 L{size * .9:.0f},0" fill="none" {ST} stroke-width="2.4"/>'
        for t in (.3, .5, .7):
            s += f'<path d="M{size * t:.0f},0 l{size * .12:.0f},{-size * .16:.0f} M{size * t:.0f},0 l{size * .12:.0f},{size * .16:.0f}" fill="none" {ST} stroke-width="2.2"/>'
    return s + '</g>'


def stem(x, g, h, w=10):
    return f'<path d="M{x},{g} Q{x + 8},{g - h / 2} {x},{g - h}" fill="none" stroke="{INK}" stroke-width="{w + 5}" stroke-linecap="round"/><path d="M{x},{g} Q{x + 8},{g - h / 2} {x},{g - h}" fill="none" stroke="{fc("stem", "#fff")}" stroke-width="{w}" stroke-linecap="round"/>'


def sunflower(x, g, k=1.0, h=190):
    top = g - h * k
    s = stem(x, g, h * k, 9 * k)
    s += leaf(x, g - h * .35 * k, 46 * k, -35) + leaf(x, g - h * .5 * k, 46 * k, 215)
    for i in range(14):
        a = i * 360 / 14
        s += (f'<path d="M0,-{26 * k:.0f} Q{12 * k:.0f},-{44 * k:.0f} 0,-{64 * k:.0f} Q-{12 * k:.0f},-{44 * k:.0f} 0,-{26 * k:.0f} Z" '
              f'transform="translate({x},{top}) rotate({a})" fill="{fc("fl_petal")}" {ST} stroke-width="3.2"/>')
    s += f'<circle cx="{x}" cy="{top}" r="{27 * k:.0f}" fill="{fc("fl_mid")}" {ST}/>'
    for i in range(7):
        a = math.radians(i * 51)
        s += f'<circle cx="{x + math.cos(a) * 14 * k:.1f}" cy="{top + math.sin(a) * 14 * k:.1f}" r="{2.6 * k:.1f}" fill="#111"/>'
    s += f'<circle cx="{x}" cy="{top}" r="{3 * k:.1f}" fill="#111"/>'
    return s


def daisy(x, g, k=1.0, h=120):
    top = g - h * k
    s = stem(x, g, h * k, 7 * k) + leaf(x, g - h * .4 * k, 34 * k, -30)
    for i in range(10):
        s += (f'<ellipse cx="{x}" cy="{top - 24 * k:.0f}" rx="{8 * k:.1f}" ry="{19 * k:.1f}" transform="rotate({i * 36} {x} {top})" '
              f'fill="{fc("fl_petal")}" {ST} stroke-width="3.2"/>')
    return s + f'<circle cx="{x}" cy="{top}" r="{11 * k:.1f}" fill="{fc("fl_mid")}" {ST}/>'


def lavender(x, g, k=1.0, h=150):
    s = stem(x, g, h * k, 5 * k)
    for i in range(7):
        y = g - (h * .55 + i * 11) * k
        s += (f'<ellipse cx="{x - 9 * k:.0f}" cy="{y:.0f}" rx="{5 * k:.1f}" ry="{8 * k:.1f}" transform="rotate(-25 {x - 9 * k:.0f} {y:.0f})" fill="{fc("lav", "#fff")}" {ST} stroke-width="2.8"/>'
              f'<ellipse cx="{x + 9 * k:.0f}" cy="{y - 4 * k:.0f}" rx="{5 * k:.1f}" ry="{8 * k:.1f}" transform="rotate(25 {x + 9 * k:.0f} {y - 4 * k:.0f})" fill="{fc("lav", "#fff")}" {ST} stroke-width="2.8"/>')
    s += f'<ellipse cx="{x}" cy="{g - (h * .55 + 78) * k:.0f}" rx="{5 * k:.1f}" ry="{9 * k:.1f}" fill="{fc("lav", "#fff")}" {ST} stroke-width="2.8"/>'
    return s + leaf(x, g - 20 * k, 40 * k, -40) + leaf(x, g - 30 * k, 36 * k, 220)


def sprout(x, g, k=1.0):
    s = stem(x, g, 40 * k, 5 * k)
    return s + leaf(x, g - 36 * k, 34 * k, -35) + leaf(x, g - 36 * k, 34 * k, 215)


def sapling(x, g, k=1.0):
    s = f'<path d="M{x},{g} Q{x + 6},{g - 60 * k} {x},{g - 120 * k}" fill="none" {ST} stroke-width="{9 * k}"/>'
    for dy, ang in ((-50, -40), (-70, 220), (-95, -30), (-112, 215)):
        s += leaf(x, g + dy * k, 40 * k, ang)
    return s + f'<circle cx="{x + 2}" cy="{g - 124 * k:.0f}" r="{9 * k:.1f}" fill="{fc("apple", "#fff")}" {ST}/>'


def apple_tree(x, g, k=1.0):
    s = tree(x, g, k)
    for dx, dy in ((-60, -235), (10, -280), (70, -240), (-20, -180), (50, -190)):
        s += f'<circle cx="{x + dx * k * .9:.0f}" cy="{g + dy * k * .9:.0f}" r="{11 * k:.1f}" fill="{fc("apple", "#fff")}" {ST} stroke-width="3.2"/>'
    return s


def fence(x0, x1, g, h=90):
    s = f'<path d="M{x0},{g - h * .65} L{x1},{g - h * .65} M{x0},{g - h * .25} L{x1},{g - h * .25}" fill="none" {ST} stroke-width="4"/>'
    x = x0
    while x < x1:
        s += f'<path d="M{x},{g} L{x},{g - h} L{x + 13},{g - h - 14} L{x + 26},{g - h} L{x + 26},{g} Z" fill="#fff" {ST} stroke-width="3.6"/>'
        x += 36
    return s


def watering_can(x, g, k=1.0):
    s = f'<path d="M{x + 60 * k},{g - 70 * k} L{x + 118 * k},{g - 112 * k}" fill="none" {ST} stroke-width="{12 * k}"/>'
    s += f'<path d="M{x + 114 * k},{g - 126 * k} L{x + 134 * k},{g - 104 * k} L{x + 106 * k},{g - 98 * k} Z" fill="#fff" {ST}/>'
    s += f'<path d="M{x - 55 * k},{g - 80 * k} Q{x - 105 * k},{g - 95 * k} {x - 62 * k},{g - 32 * k}" fill="none" {ST} stroke-width="{8 * k}"/>'
    s += f'<path d="M{x - 55 * k},{g} L{x - 62 * k},{g - 78 * k} Q{x},{g - 96 * k} {x + 62 * k},{g - 78 * k} L{x + 55 * k},{g} Z" fill="{fc("can", "#fff")}" {ST}/>'
    s += f'<path d="M{x - 58 * k},{g - 48 * k} L{x + 58 * k},{g - 48 * k}" fill="none" {ST} stroke-width="3"/>'
    return s


def wheelbarrow(x, g, k=1.0):
    s = f'<path d="M{x - 40 * k},{g - 60 * k} L{x - 120 * k},{g - 82 * k} M{x + 30 * k},{g - 50 * k} L{x - 40 * k},{g - 80 * k}" fill="none" {ST} stroke-width="{8 * k}"/>'
    s += f'<path d="M{x - 70 * k},{g - 78 * k} L{x + 84 * k},{g - 78 * k} L{x + 60 * k},{g - 24 * k} L{x - 46 * k},{g - 24 * k} Z" fill="#fff" {ST}/>'
    s += f'<circle cx="{x + 72 * k:.0f}" cy="{g - 24 * k:.0f}" r="{24 * k:.0f}" fill="#fff" {ST}/><circle cx="{x + 72 * k:.0f}" cy="{g - 24 * k:.0f}" r="{6 * k:.0f}" fill="#fff" {ST} stroke-width="3"/>'
    s += f'<path d="M{x - 60 * k},{g - 24 * k} L{x - 76 * k},{g} M{x - 40 * k},{g - 24 * k} L{x - 28 * k},{g}" fill="none" {ST} stroke-width="{7 * k}"/>'
    return s


def tin_can(x, y, k=1.0, ang=0):
    return (f'<g transform="translate({x},{y}) rotate({ang})"><path d="M{-16 * k},{-22 * k} L{-16 * k},{22 * k} Q0,{30 * k} {16 * k},{22 * k} L{16 * k},{-22 * k} Z" fill="#fff" {ST} stroke-width="3.4"/>'
            f'<ellipse cx="0" cy="{-22 * k}" rx="{16 * k}" ry="{6 * k}" fill="#fff" {ST} stroke-width="3.4"/><path d="M{-16 * k},{-6 * k} L{16 * k},{-6 * k} M{-16 * k},{8 * k} L{16 * k},{8 * k}" fill="none" {ST} stroke-width="2.4"/></g>')


def rocks(x, g, k=1.0):
    return (f'<path d="M{x},{g} Q{x - 8 * k},{g - 34 * k} {x + 30 * k},{g - 40 * k} Q{x + 66 * k},{g - 40 * k} {x + 70 * k},{g} Z" fill="#fff" {ST}/>'
            f'<path d="M{x + 50 * k},{g} Q{x + 52 * k},{g - 24 * k} {x + 80 * k},{g - 24 * k} Q{x + 104 * k},{g - 20 * k} {x + 102 * k},{g} Z" fill="#fff" {ST}/>'
            f'<path d="M{x + 14 * k},{g - 22 * k} l12,-3 M{x + 70 * k},{g - 10 * k} l10,-2" fill="none" {ST} stroke-width="2.6"/>')


def snail(x, g, k=1.0):
    s = f'<path d="M{x - 40 * k},{g} Q{x - 46 * k},{g - 16 * k} {x - 26 * k},{g - 18 * k} L{x + 52 * k},{g - 18 * k} Q{x + 74 * k},{g - 22 * k} {x + 72 * k},{g - 44 * k} Q{x + 68 * k},{g - 4 * k} {x + 54 * k},{g} Z" fill="#fff" {ST}/>'
    s += f'<path d="M{x + 62 * k},{g - 40 * k} L{x + 60 * k},{g - 62 * k} M{x + 70 * k},{g - 38 * k} L{x + 78 * k},{g - 58 * k}" fill="none" {ST} stroke-width="3.4"/>'
    s += f'<circle cx="{x + 60 * k:.0f}" cy="{g - 64 * k:.0f}" r="{4 * k:.1f}" fill="#111"/><circle cx="{x + 79 * k:.0f}" cy="{g - 60 * k:.0f}" r="{4 * k:.1f}" fill="#111"/>'
    s += f'<circle cx="{x}" cy="{g - 40 * k:.0f}" r="{34 * k:.0f}" fill="{fc("snail", "#fff")}" {ST}/>'
    s += f'<path d="M{x},{g - 40 * k} m0,-4 a6,6 0 1 1 -8,6 a14,14 0 1 1 14,16 a22,22 0 1 1 -24,-24" fill="none" {ST} stroke-width="3"/>'
    return s


def bee(x, y, k=1.0, ang=0):
    s = f'<g transform="translate({x},{y}) rotate({ang})">'
    s += f'<ellipse cx="-8" cy="-14" rx="{12 * k}" ry="{8 * k}" transform="rotate(-30 -8 -14)" fill="#fff" {ST} stroke-width="3"/><ellipse cx="8" cy="-14" rx="{12 * k}" ry="{8 * k}" transform="rotate(30 8 -14)" fill="#fff" {ST} stroke-width="3"/>'
    s += f'<ellipse cx="0" cy="0" rx="{22 * k}" ry="{15 * k}" fill="{fc("bee", "#fff")}" {ST} stroke-width="3.4"/>'
    s += f'<path d="M-6,-14 L-6,14 M6,-14 L6,14" fill="none" {ST} stroke-width="3.4"/><circle cx="{-16 * k}" cy="-2" r="2.6" fill="#111"/>'
    return s + '</g>'


def sign(x, y, w, text, size=26):
    s = f'<path d="M{x + w / 2 - 6},{y + 70} L{x + w / 2 - 6},{y + 190} M{x + w / 2 + 6},{y + 70} L{x + w / 2 + 6},{y + 190}" fill="none" {ST} stroke-width="5"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="80" rx="12" fill="#fff" {ST}/>'
    for i, line in enumerate(text.split('|')):
        n = len(text.split('|'))
        s += f'<text x="{x + w / 2}" y="{y + 40 + size * .34 + (i - (n - 1) / 2) * size * 1.05:.1f}" {font(size, 700)} fill="#111">{line}</text>'
    return s


def storm_cloud(x, y, w, rain=True):
    s = cloud(x, y, w, fc('stormc', '#fff')) + cloud(x + w * .45, y + w * .12, w * .8, fc('stormc', '#fff'))
    if rain:
        for i in range(9):
            rx = x + 20 + i * w * .13
            s += f'<path d="M{rx:.0f},{y + w * .55:.0f} l-10,32" fill="none" {ST} stroke-width="3.6"/>'
    return s


def seed(kind, x, y, k=1.0):
    """Semillas grandes para la pagina de aprendizaje."""
    s = ''
    if kind == 'bean':
        s += f'<path d="M{x - 40 * k},{y} Q{x - 40 * k},{y - 36 * k} {x},{y - 34 * k} Q{x + 46 * k},{y - 30 * k} {x + 44 * k},{y + 4 * k} Q{x + 40 * k},{y + 34 * k} {x},{y + 32 * k} Q{x - 18 * k},{y + 28 * k} {x - 6 * k},{y + 6 * k} Q{x - 28 * k},{y + 12 * k} {x - 40 * k},{y} Z" fill="#fff" {ST}/>'
        s += f'<path d="M{x - 8 * k},{y - 16 * k} q{16 * k},{-6 * k} {26 * k},{4 * k}" fill="none" {ST} stroke-width="3"/>'
    elif kind == 'sunflower':
        s += f'<path d="M{x},{y - 46 * k} Q{x + 30 * k},{y} {x},{y + 46 * k} Q{x - 30 * k},{y} {x},{y - 46 * k} Z" fill="#fff" {ST}/>'
        for dx in (-10, 0, 10):
            s += f'<path d="M{x + dx * k},{y - 36 * k} L{x + dx * k},{y + 36 * k}" fill="none" {ST} stroke-width="2.6"/>'
    elif kind == 'pea':
        for dx, dy in ((-24, 0), (24, 0), (0, -26), (0, 26)):
            s += f'<circle cx="{x + dx * k:.0f}" cy="{y + dy * k:.0f}" r="{22 * k:.0f}" fill="#fff" {ST}/>'
    elif kind == 'maple':
        s += f'<circle cx="{x - 10 * k:.0f}" cy="{y + 20 * k:.0f}" r="{14 * k:.0f}" fill="#fff" {ST}/>'
        s += f'<path d="M{x - 6 * k},{y + 8 * k} Q{x + 10 * k},{y - 50 * k} {x + 44 * k},{y - 46 * k} Q{x + 36 * k},{y - 6 * k} {x + 2 * k},{y + 8 * k} Z" fill="#fff" {ST}/>'
        s += f'<path d="M{x + 2 * k},{y} Q{x + 18 * k},{y - 20 * k} {x + 36 * k},{y - 38 * k}" fill="none" {ST} stroke-width="2.6"/>'
    elif kind == 'dandelion':
        s += f'<path d="M{x},{y + 40 * k} L{x},{y - 6 * k}" fill="none" {ST} stroke-width="3.4"/>'
        for i in range(9):
            a = math.radians(-180 + i * 22.5)
            s += f'<path d="M{x},{y - 6 * k} L{x + math.cos(a) * 44 * k:.0f},{y - 6 * k + math.sin(a) * 44 * k:.0f}" fill="none" {ST} stroke-width="2.6"/>'
            s += f'<circle cx="{x + math.cos(a) * 48 * k:.0f}" cy="{y - 6 * k + math.sin(a) * 48 * k:.0f}" r="{5 * k:.1f}" fill="#fff" {ST} stroke-width="2.6"/>'
        s += f'<ellipse cx="{x}" cy="{y + 44 * k:.0f}" rx="{7 * k:.1f}" ry="{10 * k:.1f}" fill="#fff" {ST} stroke-width="3"/>'
    elif kind == 'dust':
        for dx, dy in ((-30, -10), (-8, 14), (14, -16), (34, 10), (-18, 34), (24, 36), (0, -34)):
            s += f'<circle cx="{x + dx * k:.0f}" cy="{y + dy * k:.0f}" r="{4.5 * k:.1f}" fill="#111"/>'
    return s
