# Personajes del cuento de Lua. Cada funcion devuelve SVG. Origen local: ver cada una.
# COLORS vacio = dibujo para colorear (relleno blanco). Con valores = version en color (cubierta).
from lib import *

COLORS = {}


def fc(n, d='#fff'):
    return COLORS.get(n, d)


def L(s, k=1.0):
    return f'stroke="{INK}" stroke-width="{4.2 * k / s:.2f}" stroke-linejoin="round" stroke-linecap="round"'


def tube2(path, w, fill, s):
    return (f'<path d="{path}" fill="none" stroke="{INK}" stroke-width="{w:.1f}" stroke-linecap="round"/>'
            f'<path d="{path}" fill="none" stroke="{fill}" stroke-width="{w - 8.4 / s:.1f}" stroke-linecap="round"/>')


def grp(cx, cy, s, flip=1):
    return f'<g transform="translate({cx},{cy}) scale({flip * s},{s})">'


# ------------------------------------------------------------------ gata
def cat_head(s=1.0, mood='happy', look=0, tear=False):
    """Cabeza centrada en 0,0 (ancho ~200)."""
    body, inner, belly, nose = fc('cat_body'), fc('cat_inner'), fc('cat_belly'), fc('nose')
    o = ''
    for sd in (-1, 1):
        o += f'<path d="M{sd * 92},-18 L{sd * 84},-130 L{sd * 20},-78 Z" fill="{body}" {L(s)}/>'
        o += f'<path d="M{sd * 78},-44 L{sd * 74},-103 L{sd * 38},-76 Z" fill="{inner}" {L(s, .75)}/>'
    o += f'<ellipse cx="0" cy="0" rx="100" ry="84" fill="{body}" {L(s)}/>'
    for dx, dy in ((-20, -70), (0, -74), (20, -70)):
        o += f'<path d="M{dx},{dy} L{dx * .6:.0f},{dy + 26}" fill="none" {L(s)}/>'
    o += f'<ellipse cx="0" cy="40" rx="54" ry="34" fill="{belly}" {L(s, .75)}/>'
    for sd in (-1, 1):
        ex = sd * 38
        if mood == 'joy':
            o += f'<path d="M{ex - 18},0 Q{ex},-26 {ex + 18},0" fill="none" {L(s, 1.2)}/>'
        else:
            o += f'<ellipse cx="{ex}" cy="-8" rx="20" ry="27" fill="#fff" {L(s, .9)}/>'
            if COLORS:
                o += f'<ellipse cx="{ex + look * 5}" cy="-4" rx="14" ry="21" fill="{fc("eye")}" {L(s, .6)}/>'
            o += f'<ellipse cx="{ex + look * 5}" cy="-4" rx="9" ry="16" fill="#111"/>'
            o += f'<circle cx="{ex + look * 5 + 4}" cy="-12" r="5" fill="#fff"/>'
    if mood in ('sad', 'worried'):
        for sd in (-1, 1):
            o += f'<path d="M{sd * 62},-30 L{sd * 28},-47" fill="none" {L(s)}/>'
    if mood == 'angry':
        for sd in (-1, 1):
            o += f'<path d="M{sd * 64},-52 L{sd * 24},-34" fill="none" {L(s, 1.2)}/>'
    o += f'<path d="M-10,16 L10,16 L0,29 Z" fill="{nose}" {L(s, .85)}/>'
    if mood in ('happy', 'joy'):
        o += f'<path d="M-25,38 Q0,82 25,38 Z" fill="{fc("mouth")}" {L(s, .85)}/>'
        o += f'<path d="M0,29 L0,38" fill="none" {L(s, .85)}/>'
    elif mood == 'smile':
        o += f'<path d="M0,29 L0,38 M0,38 Q-12,53 -26,41 M0,38 Q12,53 26,41" fill="none" {L(s, .85)}/>'
    elif mood == 'sad':
        o += f'<path d="M0,29 L0,38 M-22,58 Q0,38 22,58" fill="none" {L(s, .85)}/>'
    elif mood == 'worried':
        o += f'<path d="M0,29 L0,38 M-26,56 q8,-12 17,0 t17,0 t17,0" fill="none" {L(s, .85)}/>'
    elif mood == 'angry':
        o += f'<path d="M0,29 L0,38 M-20,56 Q0,46 20,56" fill="none" {L(s, .85)}/>'
    elif mood == 'open':
        o += f'<ellipse cx="0" cy="50" rx="11" ry="15" fill="{fc("mouth")}" {L(s, .85)}/>'
        o += f'<path d="M0,29 L0,35" fill="none" {L(s, .85)}/>'
    for sd in (-1, 1):
        for (y0, y1, x1) in ((30, 12, 136), (40, 40, 140), (50, 68, 130)):
            o += f'<path d="M{sd * 58},{y0} L{sd * x1},{y1}" fill="none" {L(s, .6)}/>'
    if tear:
        o += f'<path d="M-52,20 q-12,22 0,32 q12,-10 0,-32 z" fill="{fc("tear", "#fff")}" {L(s, .75)}/>'
    return o


def cat_sit(cx, cy, s=1.0, mood='happy', flip=1, tail='curl', look=0, tear=False):
    """Gata sentada de frente. (cx,cy) = centro de la cabeza; los pies quedan en cy+272*s."""
    body, belly = fc('cat_body'), fc('cat_belly')
    o = grp(cx, cy, s, flip)
    if tail == 'curl':
        d = 'M70,240 Q175,262 168,160 Q165,105 196,92'
    elif tail == 'down':
        d = 'M70,245 Q165,272 186,250'
    else:
        d = 'M70,240 Q150,250 152,180 Q152,135 130,112'
    o += tube2(d, 34, body, s)
    if tail == 'curl':
        o += f'<path d="M153,205 L186,200 M152,150 L183,145" fill="none" {L(s, .8)}/>'
    for sd in (-1, 1):
        o += f'<ellipse cx="{sd * 84}" cy="205" rx="36" ry="52" fill="{body}" {L(s)}/>'
        o += f'<ellipse cx="{sd * 90}" cy="258" rx="34" ry="16" fill="{body}" {L(s)}/>'
    o += (f'<path d="M-85,130 Q-112,262 -60,264 L60,264 Q112,262 85,130 Q60,68 0,68 Q-60,68 -85,130 Z" '
          f'fill="{body}" {L(s)}/>')
    o += f'<ellipse cx="0" cy="182" rx="44" ry="70" fill="{belly}" {L(s, .75)}/>'
    for sd in (-1, 1):
        x = sd * 38
        o += tube2(f'M{x},205 L{x},248', 34, body, s)
        o += f'<ellipse cx="{x + sd * 2}" cy="257" rx="30" ry="16" fill="{body}" {L(s)}/>'
        o += f'<path d="M{x - 6},250 L{x - 6},262 M{x + 8},250 L{x + 8},262" fill="none" {L(s, .6)}/>'
    o += cat_head(s, mood, look, tear)
    return o + '</g>'


def cat_side(cx, g, s=1.0, mood='smile', flip=1, tail='up', look=0, tear=False, head_down=False):
    """Gata caminando de perfil con la cara de frente. (cx,g)=centro del cuerpo a nivel del suelo."""
    body = fc('cat_body')
    o = grp(cx, g, s, flip)
    for x in (-46, 90):
        o += tube2(f'M{x},-70 L{x},-16', 28, body, s)
        o += f'<ellipse cx="{x + 6}" cy="-9" rx="24" ry="12" fill="{body}" {L(s)}/>'
    d = {'up': 'M-100,-115 Q-190,-125 -172,-225', 'down': 'M-100,-100 Q-185,-95 -194,-28'}[tail]
    o += tube2(d, 28, body, s)
    o += f'<ellipse cx="0" cy="-102" rx="112" ry="60" fill="{body}" {L(s)}/>'
    for x in (-50, -20, 10):
        o += f'<path d="M{x},-158 q8,22 2,44" fill="none" {L(s)}/>'
    for x in (-82, 58):
        o += tube2(f'M{x},-70 L{x},-16', 30, body, s)
        o += f'<ellipse cx="{x + 6}" cy="-9" rx="25" ry="12" fill="{body}" {L(s)}/>'
    hy = -100 if head_down else -138
    o += f'<g transform="translate(128,{hy}) scale(0.62)">' + cat_head(s * 0.62, mood, look, tear) + '</g>'
    return o + '</g>'


# ------------------------------------------------------------ cara sencilla
def face_simple(cx, cy, r, s, mood='happy', look=0):
    o = ''
    for sd in (-1, 1):
        x = cx + sd * .38 * r
        o += f'<ellipse cx="{x + look * 2:.1f}" cy="{cy - .02 * r:.1f}" rx="{.11 * r:.1f}" ry="{.15 * r:.1f}" fill="#111"/>'
        o += f'<circle cx="{x + look * 2 + .04 * r:.1f}" cy="{cy - .08 * r:.1f}" r="{.04 * r:.1f}" fill="#fff"/>'
        if mood in ('sad', 'sorry'):
            o += f'<path d="M{cx + sd * .62 * r:.1f},{cy - .22 * r:.1f} L{cx + sd * .3 * r:.1f},{cy - .36 * r:.1f}" fill="none" {L(s, .8)}/>'
    o += f'<ellipse cx="{cx}" cy="{cy + .2 * r:.1f}" rx="{.09 * r:.1f}" ry="{.065 * r:.1f}" fill="{fc("nose")}" {L(s, .7)}/>'
    my = cy + .28 * r
    if mood in ('sad', 'sorry'):
        o += f'<path d="M{cx - .2 * r:.1f},{my + .22 * r:.1f} Q{cx},{my + .04 * r:.1f} {cx + .2 * r:.1f},{my + .22 * r:.1f}" fill="none" {L(s, .8)}/>'
    elif mood == 'open':
        o += f'<ellipse cx="{cx}" cy="{my + .16 * r:.1f}" rx="{.1 * r:.1f}" ry="{.14 * r:.1f}" fill="{fc("mouth")}" {L(s, .7)}/>'
    else:
        o += (f'<path d="M{cx},{cy + .26 * r:.1f} L{cx},{my + .04 * r:.1f} M{cx},{my + .04 * r:.1f} '
              f'Q{cx - .1 * r:.1f},{my + .2 * r:.1f} {cx - .22 * r:.1f},{my + .08 * r:.1f} M{cx},{my + .04 * r:.1f} '
              f'Q{cx + .1 * r:.1f},{my + .2 * r:.1f} {cx + .22 * r:.1f},{my + .08 * r:.1f}" fill="none" {L(s, .8)}/>')
    if mood in ('happy', 'open'):
        for sd in (-1, 1):
            o += f'<ellipse cx="{cx + sd * .68 * r:.1f}" cy="{cy + .22 * r:.1f}" rx="{.1 * r:.1f}" ry="{.065 * r:.1f}" fill="{fc("blush")}" {L(s, .5)}/>'
    return o


def squirrel(cx, g, s=1.0, mood='happy', flip=1, item='acorn'):
    body, light = fc('sq_body'), fc('sq_light')
    o = grp(cx, g, s, flip)
    d = 'M-38,-35 C-155,-20 -170,-190 -98,-272 C-72,-300 -24,-272 -50,-232 C-72,-198 -62,-120 -28,-85 Z'
    o += f'<path d="{d}" fill="{body}" {L(s)}/>'
    o += f'<path d="M-112,-205 Q-84,-180 -72,-140 M-128,-150 Q-100,-125 -84,-90" fill="none" {L(s, .7)}/>'
    for sd in (-1, 1):
        o += f'<ellipse cx="{sd * 26}" cy="-9" rx="27" ry="13" fill="{body}" {L(s)}/>'
    o += f'<ellipse cx="0" cy="-74" rx="52" ry="66" fill="{body}" {L(s)}/>'
    o += f'<ellipse cx="0" cy="-64" rx="32" ry="46" fill="{light}" {L(s, .75)}/>'
    for sd in (-1, 1):
        o += f'<path d="M{sd * 18},-190 L{sd * 30},-246 L{sd * 54},-186 Z" fill="{body}" {L(s)}/>'
        o += f'<path d="M{sd * 29},-200 L{sd * 34},-228 L{sd * 44},-197 Z" fill="{fc("cat_inner")}" {L(s, .6)}/>'
    o += f'<ellipse cx="0" cy="-160" rx="58" ry="50" fill="{body}" {L(s)}/>'
    o += f'<ellipse cx="0" cy="-143" rx="30" ry="21" fill="{light}" {L(s, .7)}/>'
    o += face_simple(0, -160, 50, s, mood)
    if item == 'acorn':
        o += f'<ellipse cx="0" cy="-70" rx="17" ry="21" fill="{fc("acorn")}" {L(s)}/>'
        o += f'<path d="M-20,-80 Q0,-104 20,-80 Z" fill="{fc("acorn_cap")}" {L(s)}/>'
    for sd in (-1, 1):
        o += f'<ellipse cx="{sd * 38}" cy="-86" rx="14" ry="22" transform="rotate({-sd * 25} {sd * 38} -86)" fill="{body}" {L(s)}/>'
    if item == 'flower':
        o += flower_held(-2, -80, s)
    return o + '</g>'


def flower_held(x, y, s):
    o = f'<path d="M{x},{y} L{x},{y + 40}" fill="none" {L(s)}/>'
    for i in range(5):
        a = math.radians(i * 72 - 90)
        o += f'<circle cx="{x + math.cos(a) * 13:.1f}" cy="{y - 20 + math.sin(a) * 13:.1f}" r="9" fill="{fc("fl_petal")}" {L(s, .8)}/>'
    o += f'<circle cx="{x}" cy="{y - 20}" r="7" fill="{fc("fl_mid")}" {L(s, .8)}/>'
    return o


def rabbit(cx, g, s=1.0, mood='happy', flip=1, item=None):
    body, inner = fc('rb_body'), fc('rb_inner')
    o = grp(cx, g, s, flip)
    for sd in (-1, 1):
        o += f'<ellipse cx="{sd * 26}" cy="-255" rx="24" ry="68" transform="rotate({sd * 9} {sd * 26} -255)" fill="{body}" {L(s)}/>'
        o += f'<ellipse cx="{sd * 26}" cy="-250" rx="11" ry="46" transform="rotate({sd * 9} {sd * 26} -250)" fill="{inner}" {L(s, .7)}/>'
    for sd in (-1, 1):
        o += f'<ellipse cx="{sd * 38}" cy="-12" rx="36" ry="16" fill="{body}" {L(s)}/>'
    o += f'<ellipse cx="0" cy="-80" rx="58" ry="72" fill="{body}" {L(s)}/>'
    o += f'<ellipse cx="0" cy="-68" rx="34" ry="48" fill="{fc("rb_belly", "#fff")}" {L(s, .7)}/>'
    o += f'<circle cx="0" cy="-160" r="56" fill="{body}" {L(s)}/>'
    o += face_simple(0, -160, 52, s, mood)
    o += f'<path d="M-9,-136 L-9,-120 L9,-120 L9,-136" fill="#fff" {L(s, .7)}/>'
    for sd in (-1, 1):
        o += f'<ellipse cx="{sd * 36}" cy="-88" rx="14" ry="24" transform="rotate({-sd * 20} {sd * 36} -88)" fill="{body}" {L(s)}/>'
    if item == 'flower':
        o += flower_held(0, -80, s)
    return o + '</g>'


def ladybug(cx, cy, s=1.0, mood='happy'):
    shell = fc('lb_shell')
    o = grp(cx, cy, s)
    for dy in (-12, 14, 38):
        for sd in (-1, 1):
            o += f'<path d="M{sd * 52},{dy} L{sd * 84},{dy + 10}" fill="none" {L(s, 1.3)}/>'
    for sd in (-1, 1):
        o += f'<path d="M{sd * 16},-78 Q{sd * 22},-106 {sd * 38},-108" fill="none" {L(s, .9)}/>'
        o += f'<circle cx="{sd * 38}" cy="-108" r="6" fill="#fff" {L(s, .8)}/>'
    o += f'<circle cx="0" cy="8" r="62" fill="{shell}" {L(s)}/>'
    o += f'<path d="M0,-38 L0,70" fill="none" {L(s, .8)}/>'
    for dx, dy, r in ((-32, 0, 11), (32, 0, 11), (-34, 38, 10), (34, 38, 10), (0, 52, 9)):
        o += f'<circle cx="{dx}" cy="{dy}" r="{r}" fill="{fc("lb_dot", "#fff")}" {L(s, .8)}/>'
    o += f'<path d="M-34,-40 Q0,-100 34,-40 Z" fill="{fc("lb_head")}" {L(s)}/>'
    for sd in (-1, 1):
        o += f'<circle cx="{sd * 13}" cy="-58" r="7" fill="#fff" {L(s, .6)}/><circle cx="{sd * 13}" cy="-57" r="3" fill="#111"/>'
    o += f'<path d="M-9,-47 Q0,-40 9,-47" fill="none" stroke="{"#fff" if COLORS else INK}" stroke-width="{3 / s:.1f}" stroke-linecap="round"/>'
    return o + '</g>'


def butterfly(cx, cy, s=1.0, flip=1):
    w1, w2 = fc('bf_w1'), fc('bf_w2')
    o = grp(cx, cy, s, flip)
    for sd in (-1, 1):
        o += (f'<path d="M{sd * 8},-22 C{sd * 95},-100 {sd * 135},-30 {sd * 98},8 C{sd * 80},28 {sd * 30},10 {sd * 8},-5 Z" '
              f'fill="{w1}" {L(s)}/>')
        o += (f'<path d="M{sd * 8},2 C{sd * 75},10 {sd * 92},72 {sd * 52},80 C{sd * 22},80 {sd * 8},44 {sd * 8},12 Z" '
              f'fill="{w2}" {L(s)}/>')
        o += f'<circle cx="{sd * 68}" cy="-28" r="13" fill="#fff" {L(s, .8)}/><circle cx="{sd * 44}" cy="52" r="9" fill="#fff" {L(s, .8)}/>'
        o += f'<path d="M{sd * 6},-62 Q{sd * 14},-92 {sd * 34},-96" fill="none" {L(s, .9)}/>'
    o += f'<ellipse cx="0" cy="12" rx="10" ry="48" fill="{fc("bf_body", "#fff")}" {L(s)}/>'
    o += f'<circle cx="0" cy="-48" r="17" fill="{fc("bf_body", "#fff")}" {L(s)}/>'
    o += f'<circle cx="-6" cy="-50" r="2.6" fill="#111"/><circle cx="6" cy="-50" r="2.6" fill="#111"/>'
    o += f'<path d="M-6,-42 Q0,-36 6,-42" fill="none" {L(s, .6)}/>'
    return o + '</g>'


def bird(cx, g, s=1.0, mood='happy', flip=1, tear=False, wings='down'):
    body, light = fc('bd_body'), fc('bd_light')
    o = grp(cx, g, s, flip)
    o += f'<path d="M-44,-50 L-104,-68 L-96,-44 L-110,-30 L-92,-16 L-44,-30 Z" fill="{body}" {L(s)}/>'
    o += f'<path d="M-8,-12 L-8,-2 M-14,-2 L-2,-2 M14,-12 L14,-2 M8,-2 L20,-2" fill="none" {L(s)}/>'
    o += f'<ellipse cx="0" cy="-54" rx="58" ry="48" fill="{body}" {L(s)}/>'
    o += f'<ellipse cx="14" cy="-42" rx="34" ry="30" fill="{light}" {L(s, .7)}/>'
    o += f'<circle cx="30" cy="-112" r="42" fill="{body}" {L(s)}/>'
    o += f'<path d="M64,-116 L94,-106 L64,-96 Z" fill="{fc("beak")}" {L(s)}/>'
    o += f'<path d="M22,-152 q-6,-16 -14,-18 M32,-153 q0,-16 -4,-22 M42,-150 q6,-12 12,-14" fill="none" {L(s, .8)}/>'
    o += f'<ellipse cx="44" cy="-122" rx="8" ry="11" fill="#111"/><circle cx="47" cy="-126" r="3" fill="#fff"/>'
    if mood == 'sad':
        o += f'<path d="M34,-142 L56,-134" fill="none" {L(s, .8)}/>'
    o += f'<ellipse cx="46" cy="-98" rx="10" ry="6" fill="{fc("blush")}" {L(s, .5)}/>'
    if tear:
        o += f'<path d="M38,-108 q-7,12 0,18 q7,-6 0,-18 z" fill="{fc("tear", "#fff")}" {L(s, .6)}/>'
    if wings == 'down':
        o += f'<path d="M-28,-64 Q10,-96 44,-58 Q12,-24 -28,-64 Z" fill="{body}" {L(s)}/>'
    else:
        o += f'<path d="M-20,-70 Q-40,-170 20,-175 Q16,-110 30,-72 Z" fill="{body}" {L(s)}/>'
    return o + '</g>'


# ---------------------------------------------------------------- decorado
def moon(cx, cy, r):
    return (f'<path d="M{cx},{cy - r} A{r},{r} 0 1 0 {cx},{cy + r} A{r * .7},{r} 0 1 1 {cx},{cy - r} Z" '
            f'fill="#fff" {ST}/>')


def twinkle(x, y, k=1.0):
    return f'<path d="M{x},{y - 16 * k} L{x},{y + 16 * k} M{x - 16 * k},{y} L{x + 16 * k},{y}" {ST} stroke-width="4"/>'


def tree(x, g, k=1.0, branch=False):
    """Arbol con raices, corteza y hojas. Con branch=True lleva una rama larga a la izquierda para el nido."""
    k *= 0.9
    s = ''
    if branch:
        s += tube2(f'M{x - 18 * k:.1f},{g - 205 * k:.1f} Q{x - 110 * k:.1f},{g - 190 * k:.1f} {x - 205 * k:.1f},{g - 225 * k:.1f}', 26 * k, '#fff', 1)
        s += tube2(f'M{x - 175 * k:.1f},{g - 222 * k:.1f} Q{x - 200 * k:.1f},{g - 250 * k:.1f} {x - 190 * k:.1f},{g - 275 * k:.1f}', 14 * k, '#fff', 1)
    s += (f'<path d="M{x - 40 * k:.1f},{g} Q{x - 22 * k:.1f},{g - 35 * k:.1f} {x - 24 * k:.1f},{g - 150 * k:.1f} '
          f'L{x + 24 * k:.1f},{g - 150 * k:.1f} Q{x + 22 * k:.1f},{g - 35 * k:.1f} {x + 40 * k:.1f},{g} Z" fill="#fff" {ST}/>')
    s += (f'<path d="M{x - 6 * k:.1f},{g - 10 * k:.1f} Q{x - 10 * k:.1f},{g - 70 * k:.1f} {x - 4 * k:.1f},{g - 130 * k:.1f} '
          f'M{x + 10 * k:.1f},{g - 20 * k:.1f} Q{x + 14 * k:.1f},{g - 70 * k:.1f} {x + 8 * k:.1f},{g - 120 * k:.1f}" fill="none" {ST} stroke-width="3"/>')
    P = lambda dx, dy: f'{x + dx * k:.1f},{g + dy * k:.1f}'
    d = (f'M{P(-95, -150)} Q{P(-135, -215)} {P(-85, -250)} Q{P(-80, -325)} {P(-10, -310)} Q{P(50, -345)} {P(90, -285)} '
         f'Q{P(140, -250)} {P(105, -195)} Q{P(135, -150)} {P(80, -140)} Q{P(0, -120)} {P(-95, -150)} Z')
    s += f'<path d="{d}" fill="#fff" {ST}/>'
    for dx, dy in ((-70, -200), (-25, -255), (30, -205), (75, -250), (-92, -170), (0, -165), (62, -170), (-45, -290), (22, -300), (-10, -215)):
        s += (f'<path d="M{x + dx * k:.1f},{g + dy * k:.1f} q{7 * k:.1f},{-12 * k:.1f} {16 * k:.1f},0 '
              f'M{x + (dx + 8) * k:.1f},{g + (dy - 2) * k:.1f} q{-3 * k:.1f},{-9 * k:.1f} {2 * k:.1f},{-14 * k:.1f}" fill="none" {ST} stroke-width="3"/>')
    return s


def nest_pos(x, g, k):
    return x - 205 * 0.9 * k, g - 225 * 0.9 * k


def nest_back(cx, cy):
    s = ''
    for dx in (-84, -58, 56, 86):
        s += f'<path d="M{cx + dx},{cy - 2} l{dx * .18:.0f},-20" fill="none" {ST} stroke-width="3.5"/>'
    s += f'<ellipse cx="{cx}" cy="{cy}" rx="82" ry="20" fill="{fc("nest", "#fff")}" {ST}/>'
    return s


def nest_front(cx, cy):
    s = f'<path d="M{cx - 82},{cy} Q{cx},{cy + 98} {cx + 82},{cy} Q{cx},{cy + 22} {cx - 82},{cy} Z" fill="{fc("nest", "#fff")}" {ST}/>'
    s += (f'<path d="M{cx - 60},{cy + 22} Q{cx},{cy + 52} {cx + 60},{cy + 22} M{cx - 40},{cy + 44} Q{cx},{cy + 68} {cx + 40},{cy + 44} '
          f'M{cx - 18},{cy + 14} L{cx - 30},{cy + 62} M{cx + 22},{cy + 16} L{cx + 34},{cy + 60}" fill="none" {ST} stroke-width="3"/>')
    return s


def flower(x, y, k=1.0):
    v = (int(x) // 10) % 3
    s = f'<path d="M{x},{y} L{x},{y + 55 * k}" {ST}/>'
    s += f'<path d="M{x},{y + 40 * k} q{16 * k},{-14 * k} {26 * k},{-4 * k} q{-12 * k},{14 * k} {-26 * k},{4 * k} z" fill="#fff" {ST}/>'
    if v == 0:  # tulipan
        s += (f'<path d="M{x - 14 * k},{y + 6 * k} Q{x - 18 * k},{y - 26 * k} {x - 7 * k},{y - 34 * k} L{x},{y - 20 * k} L{x + 7 * k},{y - 34 * k} '
              f'Q{x + 18 * k},{y - 26 * k} {x + 14 * k},{y + 6 * k} Q{x},{y + 18 * k} {x - 14 * k},{y + 6 * k} Z" fill="{fc("fl_petal")}" {ST}/>')
    elif v == 1:  # margarita
        for i in range(8):
            a = i * 45
            s += f'<ellipse cx="{x}" cy="{y - 15 * k}" rx="{5.5 * k}" ry="{13 * k}" transform="rotate({a} {x} {y})" fill="{fc("fl_petal")}" {ST} stroke-width="3"/>'
        s += f'<circle cx="{x}" cy="{y}" r="{7 * k}" fill="{fc("fl_mid")}" {ST}/>'
    else:
        for i in range(5):
            a = math.radians(i * 72 - 90)
            s += f'<circle cx="{x + math.cos(a) * 15 * k:.1f}" cy="{y + math.sin(a) * 15 * k:.1f}" r="{11 * k:.1f}" fill="{fc("fl_petal")}" {ST}/>'
        s += f'<circle cx="{x}" cy="{y}" r="{9 * k:.1f}" fill="{fc("fl_mid")}" {ST}/>'
    return s


def owl(cx, g, s=1.0, look=0, flip=1):
    body, light = fc('ow_body'), fc('ow_light')
    o = grp(cx, g, s, flip)
    o += f'<path d="M-26,-6 L-26,0 M-34,0 L-18,0 M26,-6 L26,0 M18,0 L34,0" fill="none" {L(s)}/>'
    o += f'<ellipse cx="0" cy="-82" rx="64" ry="82" fill="{body}" {L(s)}/>'
    o += f'<ellipse cx="0" cy="-66" rx="40" ry="56" fill="{light}" {L(s, .75)}/>'
    for y in (-100, -76, -52):
        o += f'<path d="M-24,{y} q12,12 24,0 q12,12 24,0" fill="none" {L(s, .7)}/>'
    for sd in (-1, 1):
        o += f'<path d="M{sd * 62},-130 Q{sd * 98},-70 {sd * 58},-14 Q{sd * 48},-70 {sd * 62},-130 Z" fill="{body}" {L(s)}/>'
    o += f'<ellipse cx="0" cy="-168" rx="68" ry="52" fill="{body}" {L(s)}/>'
    for sd in (-1, 1):
        o += f'<path d="M{sd * 34},-208 L{sd * 52},-252 L{sd * 64},-198 Z" fill="{body}" {L(s)}/>'
        o += f'<circle cx="{sd * 28}" cy="-170" r="30" fill="{light}" {L(s, .75)}/>'
        o += f'<circle cx="{sd * 28}" cy="-170" r="18" fill="#fff" {L(s, .9)}/>'
        o += f'<circle cx="{sd * 28 + look * 5}" cy="-170" r="9" fill="#111"/><circle cx="{sd * 28 + look * 5 + 3}" cy="-174" r="3" fill="#fff"/>'
        o += f'<path d="M{sd * 52},-198 L{sd * 10},-188" fill="none" {L(s, 1.1)}/>'
    o += f'<path d="M-9,-160 L9,-160 L0,-140 Z" fill="{fc("beak")}" {L(s, .85)}/>'
    return o + '</g>'


def petal_head(x, y, k=1.0):
    o = ''
    for i in range(5):
        ang = math.radians(i * 72 - 90)
        o += f'<circle cx="{x + math.cos(ang) * 15 * k:.1f}" cy="{y + math.sin(ang) * 15 * k:.1f}" r="{11 * k:.1f}" fill="{fc("fl_petal")}" {ST} stroke-width="3.4"/>'
    return o + f'<circle cx="{x}" cy="{y}" r="{8 * k:.1f}" fill="{fc("fl_mid")}" {ST} stroke-width="3.4"/>'
