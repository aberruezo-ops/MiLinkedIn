# 20 paginas de pasatiempos para los libros de Lua. Se parametriza con un dict `cfg`:
#   cast: lista de 4 dicts {name, fig(cx,g,s), h, like}   (personajes para sombras y parejas)
#   head_main(cx,cy,s,mood)  cabeza de Lua            hero_sit(cx,g,s,mood)  Lua sentada
#   head_hat(cx,cy,s) cabeza para disenar el sombrero, hat_name
#   words: palabras de la sopa de letras                story: 4 callables -> svg 750x780 de escenas
#   extra: dict con funciones de decorado (bee, snail, ...)
import math
import random
from lib import *
from animales import ladybug, butterfly


def _pg(num, title, tag, inner, instr, vb='0 0 750 740', defs=''):
    w, h = [float(v) for v in vb.split()[2:]]
    svg = (f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" style="width:7.3in;height:{7.3 * h / w:.3f}in;display:block;margin:0 auto">'
           f'<defs>{defs}</defs>{inner}</svg>')
    return (f'<section class="page"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:.05in">'
            f'<span style="font-size:10.5pt;font-weight:700;font-family:Nunito">PASATIEMPOS {num}/20</span>'
            f'<span style="border:2px solid #111;border-radius:.3in;padding:.01in .14in;font-size:10.5pt;font-weight:700;font-family:Nunito">{tag}</span></div>'
            f'<h2 class="center" style="font-size:25pt;margin:0 0 .06in">{title}</h2>'
            f'<div class="art">{svg}</div>'
            f'<div class="txt"><p style="font-size:13pt;font-family:Nunito;font-weight:700;line-height:1.35">{instr}</p></div></section>')


def _t(x, y, txt, size=24, w=700, anchor='middle'):
    return f'<text x="{x}" y="{y}" {font(size, w, anchor)} fill="#111">{txt}</text>'


def _sil(fn):
    """Silueta negra de un dibujo."""
    return f'<g filter="url(#sil)">{fn}</g>'


SIL = '<filter id="sil"><feColorMatrix type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 1 0"/></filter>'


# ---------------------------------------------------------------- 1. pixel art
PIX = ["01100000000110", "01210000001210", "01221111112210", "01222222222210", "12222222222221", "12255222255221", "12254222245221",
       "12222222222221", "12222233222221", "12222244222221", "12224222242221", "12222444422221", "01222222222210", "00111111111100"]


def pixel():
    cs, ox, oy = 44, (750 - 14 * 44) / 2, 10
    s = ''
    for r, row in enumerate(PIX):
        for c, ch in enumerate(row):
            x, y = ox + c * cs, oy + r * cs
            s += f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="#fff" stroke="#111" stroke-width="2.2"/>'
            if ch != '0':
                s += _t(x + cs / 2, y + cs / 2 + 8, ch, 22)
    for i, (n, t) in enumerate((('1', 'gris'), ('2', 'gris claro'), ('3', 'rosa'), ('4', 'negro'), ('5', 'verde'))):
        x = 30 + i * 140
        s += f'<rect x="{x}" y="662" width="34" height="34" rx="6" fill="#fff" {ST} stroke-width="3"/>' + _t(x + 17, 687, n, 20)
        s += _t(x + 42, 686, t, 18, 600, 'start')
    s += _t(375, 725, 'El 0 (casillas sin número) se deja en blanco', 17, 600)
    return s


# ---------------------------------------------------------------- 2. laberinto
def maze_data(n=13, seed=11):
    rnd = random.Random(seed)
    openp = {(r, c): set() for r in range(n) for c in range(n)}
    seen, stack = {(0, 0)}, [(0, 0)]
    while stack:
        r, c = stack[-1]
        nb = [(r + dr, c + dc) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (r + dr, c + dc) in openp and (r + dr, c + dc) not in seen]
        if not nb:
            stack.pop()
            continue
        nx = rnd.choice(nb)
        openp[(r, c)].add(nx)
        openp[nx].add((r, c))
        seen.add(nx)
        stack.append(nx)
    prev, q = {(0, 0): None}, [(0, 0)]
    for cur in q:
        for nx in openp[cur]:
            if nx not in prev:
                prev[nx] = cur
                q.append(nx)
    path, cur = [], (n - 1, n - 1)
    while cur:
        path.append(cur)
        cur = prev[cur]
    return openp, path[::-1]


def maze(sol=False, scale=1.0):
    n, cs = 13, 46
    openp, path = maze_data(n)
    ox, oy = 76, 40
    s = ''
    for r in range(n):
        for c in range(n):
            x, y = ox + c * cs, oy + r * cs
            if (r, c + 1) not in openp[(r, c)]:
                s += f'<path d="M{x + cs},{y} L{x + cs},{y + cs}" {ST} stroke-width="4.4"/>'
            if (r + 1, c) not in openp[(r, c)] and (r, c) != (n - 1, n - 1):
                s += f'<path d="M{x},{y + cs} L{x + cs},{y + cs}" {ST} stroke-width="4.4"/>'
            if c == 0:
                s += f'<path d="M{x},{y} L{x},{y + cs}" {ST} stroke-width="4.4"/>'
            if r == 0 and c != 0:
                s += f'<path d="M{x},{y} L{x + cs},{y}" {ST} stroke-width="4.4"/>'
    if sol:
        pts = ' '.join(f'{ox + c * cs + cs / 2},{oy + r * cs + cs / 2}' for r, c in path)
        s += f'<polyline points="{pts}" fill="none" stroke="#111" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="2 10"/>'
    return s, ox, oy, n * cs


# ---------------------------------------------------------------- 3. espejo
def mirror(cfg):
    s = '<defs><clipPath id="half"><rect x="0" y="0" width="375" height="740"/></clipPath></defs>'
    s += f'<g clip-path="url(#half)">{cfg["head_main"](375, 330, 1.9, "happy")}</g>'
    s += f'<path d="M375,60 L375,700" fill="none" {ST} stroke-width="3.4" stroke-dasharray="3 12"/>'
    for gx in range(390, 740, 40):
        for gy in range(80, 700, 40):
            s += f'<circle cx="{gx}" cy="{gy}" r="2.4" fill="#111" opacity=".35"/>'
    s += _t(190, 725, 'Así es Lúa', 20, 600) + _t(560, 725, 'Dibuja tú la otra mitad', 20, 600)
    return s


# ---------------------------------------------------------------- 4. diferencias
DIF = [('sol', (92, 60, 40)), ('nube', (455, 46, 62)), ('boca', (260, 246, 24)), ('flor', (160, 278, 30)),
       ('mariposa', (620, 92, 36)), ('manzana', (565, 190, 22)), ('abeja', (340, 60, 30))]


def diff_panel(v, cfg):
    s = f'<rect x="0" y="0" width="700" height="340" rx="18" fill="#fff" {ST}/>'
    s += sun(92, 60, 24, face=(v == 0))
    if v == 0:
        s += cloud(400, 22, 110)
    s += cfg['hero_sit'](260, 330, 0.36, 'happy' if v == 0 else 'smile')
    s += flower(110, 262, 0.7) + flower(160, 276, 0.7) * (v == 0) + flower(210, 268, 0.7)
    s += tree(560, 330, 0.55)
    for dx, dy in ((540, 215), (590, 220)) + (((565, 190),) if v == 0 else ()):
        s += f'<circle cx="{dx}" cy="{dy}" r="9" fill="#fff" {ST} stroke-width="3"/>'
    s += butterfly(560 if v == 0 else 620, 120 if v == 0 else 90, 0.3)
    if v == 0:
        s += cfg['extra']['bee'](340, 60, 0.7, -10)
    s += f'<path d="M0,318 Q350,296 700,318" fill="none" {ST} stroke-width="3"/>'
    return s


def diferencias(cfg, sol=False):
    s = f'<g transform="translate(25,10)">{diff_panel(0, cfg)}</g>'
    s += f'<g transform="translate(25,370)">{diff_panel(1, cfg)}</g>'
    if sol:
        for _, (x, y, r) in DIF:
            s += f'<circle cx="{x + 25}" cy="{y + 370}" r="{r * .8:.0f}" fill="none" stroke="#111" stroke-width="4" stroke-dasharray="4 6"/>'
    return s


# ---------------------------------------------------------------- 5. unir puntos
PTS = [(110, 60), (190, 170), (270, 140), (375, 128), (480, 140), (560, 170), (640, 60), (665, 190), (695, 300), (672, 410), (620, 490),
       (540, 540), (450, 565), (375, 572), (300, 565), (210, 540), (130, 490), (78, 410), (55, 300), (85, 190)]


def puntos():
    s = ''
    for i, (x, y) in enumerate(PTS):
        dx = -18 if x < 375 else 18
        s += f'<circle cx="{x + 10}" cy="{y + 60}" r="7" fill="#111"/>' + _t(x + 10 + dx, y + 67, i + 1, 20, 700)
    s += f'<circle cx="{PTS[0][0] + 10}" cy="{PTS[0][1] + 60}" r="15" fill="none" {ST} stroke-width="3"/>'
    for dx, dy in ((-52, 250), (52, 250)):
        s += f'<ellipse cx="{375 + dx}" cy="{dy + 60}" rx="26" ry="36" fill="#fff" {ST} stroke-width="3.4" stroke-dasharray="2 8"/>'
    s += f'<path d="M355,430 L395,430 L375,458 Z" fill="#fff" {ST} stroke-width="3.4" stroke-dasharray="2 8"/>'
    s += _t(375, 715, 'Une los puntos del 1 al 20 y vuelve al 1. ¡Después, colorea!', 19, 600)
    return s


# ---------------------------------------------------------------- 6. contar
def contar(cfg):
    rnd = random.Random(5)
    icons = [lambda x, y: heart(x, y, .26), lambda x, y: star(x, y, 17), lambda x, y: flower(x, y, .38), lambda x, y: cfg['extra']['bee'](x, y, .55, 0),
             lambda x, y: butterfly(x, y, .22)]
    counts = [rnd.randint(2, 9) for _ in icons]
    s = ''
    for i, (ic, n) in enumerate(zip(icons, counts)):
        y0 = 30 + i * 135
        s += f'<rect x="25" y="{y0}" width="560" height="115" rx="16" fill="#fff" {ST} stroke-width="3.4"/>'
        cells = [(60 + (k % 8) * 65, y0 + 32 + (k // 8) * 55) for k in range(16)]
        rnd.shuffle(cells)
        for (x, y) in cells[:n]:
            s += ic(x + rnd.randint(-6, 6), y + rnd.randint(-4, 4))
        s += f'<rect x="610" y="{y0 + 18}" width="110" height="80" rx="14" fill="#fff" {ST}/>'
    return s, counts


# ---------------------------------------------------------------- 7. sombrero
def sombrero(cfg):
    s = cfg['head_hat'](375, 440, 2.0)
    s += f'<path d="M150,290 Q375,130 600,290" fill="none" {ST} stroke-width="3.4" stroke-dasharray="3 12"/>'
    s += _t(375, 120, f'¡{cfg["hat_name"]} necesita un sombrero!', 26, 700) + _t(375, 720, 'Puede ser grande, pequeño, de flores, de fiesta, de lo que tú quieras', 18, 600)
    return s


# ---------------------------------------------------------------- 8. sopa de letras
def wordsearch(words, n=10, seed=3):
    rnd = random.Random(seed)
    grid = [[''] * n for _ in range(n)]
    dirs = [(0, 1), (1, 0), (1, 1)]
    pos = {}
    for w in sorted(words, key=len, reverse=True):
        for _ in range(500):
            dr, dc = rnd.choice(dirs)
            r, c = rnd.randint(0, n - 1), rnd.randint(0, n - 1)
            er, ec = r + dr * (len(w) - 1), c + dc * (len(w) - 1)
            if er >= n or ec >= n:
                continue
            cells = [(r + dr * i, c + dc * i) for i in range(len(w))]
            if all(grid[a][b] in ('', w[i]) for i, (a, b) in enumerate(cells)):
                for i, (a, b) in enumerate(cells):
                    grid[a][b] = w[i]
                pos[w] = cells
                break
    letters = 'ABCDEFGHIJLMNOPRSTUV'
    for r in range(n):
        for c in range(n):
            if not grid[r][c]:
                grid[r][c] = rnd.choice(letters)
    return grid, pos


def sopa(cfg, sol=False, size=56, ox=95, oy=20, grid_pos=None):
    grid, pos = grid_pos or wordsearch(cfg['words'])
    n = len(grid)
    s = ''
    for r in range(n):
        for c in range(n):
            s += _t(ox + c * size + size / 2, oy + r * size + size / 2 + 9, grid[r][c], size * .42, 700)
    s += f'<rect x="{ox}" y="{oy}" width="{n * size}" height="{n * size}" rx="10" fill="none" {ST}/>'
    if sol:
        for w, cells in pos.items():
            (r0, c0), (r1, c1) = cells[0], cells[-1]
            s += (f'<line x1="{ox + c0 * size + size / 2}" y1="{oy + r0 * size + size / 2}" x2="{ox + c1 * size + size / 2}" y2="{oy + r1 * size + size / 2}" '
                  f'stroke="#111" stroke-width="{size * .5}" stroke-linecap="round" opacity=".28"/>')
    return s, grid, pos


# ---------------------------------------------------------------- 9. mandala
def mandala():
    cx, cy = 375, 370
    s = ''
    for i in range(16):
        a = i * 22.5
        s += f'<ellipse cx="{cx}" cy="{cy - 255}" rx="30" ry="62" transform="rotate({a} {cx} {cy})" fill="#fff" {ST} stroke-width="3.4"/>'
        s += f'<circle cx="{cx}" cy="{cy - 255}" r="10" transform="rotate({a} {cx} {cy})" fill="#fff" {ST} stroke-width="3"/>'
    for i in range(32):
        a = math.radians(i * 11.25)
        s += f'<circle cx="{cx + math.cos(a) * 322:.1f}" cy="{cy + math.sin(a) * 322:.1f}" r="8" fill="#fff" {ST} stroke-width="3"/>'
    for i in range(12):
        a = i * 30 + 15
        s += f'<ellipse cx="{cx}" cy="{cy - 165}" rx="26" ry="52" transform="rotate({a} {cx} {cy})" fill="#fff" {ST} stroke-width="3.4"/>'
    for i in range(24):
        a = math.radians(i * 15)
        s += f'<path d="M{cx + math.cos(a) * 100:.1f},{cy + math.sin(a) * 100:.1f} L{cx + math.cos(a) * 118:.1f},{cy + math.sin(a) * 118:.1f}" fill="none" {ST} stroke-width="3.4"/>'
    for i in range(8):
        a = i * 45
        s += f'<ellipse cx="{cx}" cy="{cy - 58}" rx="20" ry="38" transform="rotate({a} {cx} {cy})" fill="#fff" {ST} stroke-width="3.4"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="24" fill="#fff" {ST}/>' + star(cx, cy, 16)
    return s


# ---------------------------------------------------------------- 10. sombras
def sombras(cfg):
    rnd = random.Random(2)
    cast = cfg.get('sombra_cast', cfg['cast'])
    order = list(range(4))
    rnd.shuffle(order)
    s = ''
    for i, ch in enumerate(cast):
        x = 95 + i * 187
        s += ch['fig'](x, 240, 170 / ch['h']) + _t(x, 280, ch['name'], 22, 700)
    for j, k in enumerate(order):
        ch = cast[k]
        x = 95 + j * 187
        s += _sil(ch['fig'](x, 600, 170 / ch['h'])) + f'<circle cx="{x}" cy="{630}" r="20" fill="#fff" {ST}/>'
    return s, order, ''.join(c['name'][0] for c in cast)


# ---------------------------------------------------------------- 11. busca y encuentra
def busca(cfg):
    ex = cfg['extra']
    rnd = random.Random(9)
    targets = [('mariquita', lambda x, y: ladybug(x, y, .26)), ('caracol', lambda x, y: ex['snail'](x, y + 14, .34)), ('abeja', lambda x, y: ex['bee'](x, y, .6, -10)),
               ('mariposa', lambda x, y: butterfly(x, y, .2)), ('corazón', lambda x, y: heart(x, y, .28)), ('estrella', lambda x, y: star(x, y, 18)),
               ('lata', lambda x, y: ex['tin_can'](x, y, .62, 20)), ('flor', lambda x, y: flower(x, y, .44))]
    decoys = [lambda x, y: ex['leaf'](x, y, 46, rnd.randint(-60, 60)), lambda x, y: ex['rocks'](x - 20, y + 20, .38), lambda x, y: cloud(x - 30, y - 12, 60),
              lambda x, y: ex['sprout'](x, y + 22, .6)]
    cells = [(60 + (k % 6) * 118, 60 + (k // 6) * 118) for k in range(30)]
    rnd.shuffle(cells)
    s = f'<rect x="20" y="10" width="710" height="595" rx="22" fill="#fff" {ST}/>'
    items = [(t, f) for t, f in targets] + [('', rnd.choice(decoys)) for _ in range(22)]
    rnd.shuffle(items)
    for (name, f), (x, y) in zip(items, cells):
        s += f(x + rnd.randint(-10, 18), y + rnd.randint(-6, 14))
    s += _t(375, 650, 'Encuentra y rodea:', 22, 700)
    x0 = 30
    for i, (name, f) in enumerate(targets):
        x = 50 + (i % 4) * 175
        y = 690 + (i // 4) * 0
    names = '   '.join(t for t, _ in targets)
    s += _t(375, 690, '   ·   '.join(t for t, _ in targets[:4]), 19, 600) + _t(375, 722, '   ·   '.join(t for t, _ in targets[4:]), 19, 600)
    return s


# ---------------------------------------------------------------- 12. sudoku de dibujos
def _cuenta_soluciones(clues, limite=2):
    g = [row[:] for row in clues]
    cnt = [0]

    def ok(r, c, v):
        if any(g[r][k] == v for k in range(4)) or any(g[k][c] == v for k in range(4)):
            return False
        br, bc = r // 2 * 2, c // 2 * 2
        return not any(g[br + i][bc + j] == v for i in range(2) for j in range(2))

    def rec(pos):
        if cnt[0] >= limite:
            return
        if pos == 16:
            cnt[0] += 1
            return
        r, c = divmod(pos, 4)
        if g[r][c] is not None:
            rec(pos + 1)
            return
        for v in range(4):
            if ok(r, c, v):
                g[r][c] = v
                rec(pos + 1)
                g[r][c] = None
    rec(0)
    return cnt[0]


def sudoku_data(seed=4):
    base = [[0, 1, 2, 3], [2, 3, 0, 1], [1, 0, 3, 2], [3, 2, 1, 0]]
    rnd = random.Random(seed)
    perm = list(range(4))
    rnd.shuffle(perm)
    grid = [[perm[v] for v in row] for row in base]
    clues = [[None] * 4 for _ in range(4)]
    cells = [(r, c) for r in range(4) for c in range(4)]
    rnd.shuffle(cells)
    for (r, c) in cells:
        clues[r][c] = grid[r][c]
        if sum(v is not None for row in clues for v in row) >= 6 and _cuenta_soluciones(clues) == 1:
            break
    return grid, clues


def sudoku(cfg, sol=False):
    grid, clues = sudoku_data()
    icons = [lambda x, y: heart(x, y + 4, .5), lambda x, y: star(x, y, 36), lambda x, y: flower(x, y - 6, 0.8), lambda x, y: cfg['extra']['bee'](x, y, 1.2, 0)]
    cs, ox, oy = 125, 125, 40
    s = f'<rect x="{ox}" y="{oy}" width="{4 * cs}" height="{4 * cs}" rx="8" fill="#fff" {ST} stroke-width="6"/>'
    for i in range(1, 4):
        w = 7 if i == 2 else 2.8
        s += f'<path d="M{ox + i * cs},{oy} L{ox + i * cs},{oy + 4 * cs} M{ox},{oy + i * cs} L{ox + 4 * cs},{oy + i * cs}" fill="none" {ST} stroke-width="{w}"/>'
    for r in range(4):
        for c in range(4):
            v = grid[r][c] if sol else clues[r][c]
            if v is not None:
                s += icons[v](ox + c * cs + cs / 2, oy + r * cs + cs / 2)
    for i, ic in enumerate(icons):
        s += ic(155 + i * 150, 640) + _t(155 + i * 150, 700, ('corazón', 'estrella', 'flor', 'abeja')[i], 18, 600)
    return s


# ---------------------------------------------------------------- 13. emociones
def emociones(cfg):
    s = ''
    for i, nom in enumerate(('Alegría', 'Tristeza', 'Miedo', 'Enfado', 'Sorpresa', 'Calma')):
        x, y = 125 + (i % 3) * 250, 140 + (i // 3) * 270
        s += f'<circle cx="{x}" cy="{y + 20}" r="95" fill="#fff" {ST}/>' + _t(x, y + 150, nom, 28, 700)
    s += _t(375, 700, 'Hoy me siento ____________ porque ____________', 21, 600)
    return s


# ---------------------------------------------------------------- 14. ordenar la historia
def ordenar(cfg):
    order = [2, 0, 3, 1]
    s = ''
    for k, i in enumerate(order):
        x, y = 25 + (k % 2) * 360, 20 + (k // 2) * 350
        s += f'<g transform="translate({x},{y}) scale(.45)"><svg x="0" y="0" width="750" height="780" viewBox="0 0 750 780">{cfg["story"][i]()}</svg></g>'
        s += f'<rect x="{x}" y="{y}" width="335" height="345" rx="16" fill="none" {ST}/>'
        s += f'<circle cx="{x + 30}" cy="{y + 315}" r="22" fill="#fff" {ST}/>'
    return s, order


# ---------------------------------------------------------------- 15. retos en familia
RETOS = ['Abraza a un árbol, de verdad.', 'Huele tres flores distintas.', 'Cierra los ojos y escucha cinco sonidos.',
         'Busca un bicho y obsérvalo sin tocarlo.', 'Cuenta cuántos colores de hoja encuentras.', 'Cuenta tus pasos hasta el árbol más cercano.',
         'Haz una corona o un collar con hojas.', 'Planta una semilla y ponle nombre.', 'Dibuja una nube que veas hoy.', 'Dale las gracias a alguien, mirándole a los ojos.']


def retos(lista=None):
    s = ''
    for i, t in enumerate(lista or RETOS):
        y = 30 + i * 70
        s += f'<rect x="40" y="{y}" width="46" height="46" rx="10" fill="#fff" {ST}/>' + _t(112, y + 33, t, 23, 600, 'start')
    return s


# ---------------------------------------------------------------- 16. adivinanzas
ADIV = [('Con bigotes de seda y patas de terciopelo, me lamo entera y siempre caigo de pie.', 'El gato'),
        ('Zumbo de flor en flor, no paro de trabajar, y guardo en mi panal el dulce más especial.', 'La abeja'),
        ('Nací pequeñita, una semilla de nada. Con agua y con sol ahora miro al cielo con cara de sol.', 'El girasol'),
        ('Llevo la casa a cuestas y no pago alquiler. Voy despacio y dejo un camino de brillo.', 'El caracol'),
        ('Tengo hojas y no soy libro, tengo ramas y no soy río. Doy sombra y doy frutos si me cuidas.', 'El árbol'),
        ('Antes fui oruga y ahora vuelo con alas de colores, sin hacer ruido, de flor en flor.', 'La mariposa')]


def adivinanzas():
    s = ''
    for i, (t, _) in enumerate(ADIV):
        y = 20 + i * 118
        s += f'<rect x="25" y="{y}" width="700" height="105" rx="16" fill="#fff" {ST} stroke-width="3.4"/>'
        words, lines, cur = t.split(), [], ''
        for w in words:
            if len(cur) + len(w) > 52:
                lines.append(cur)
                cur = w
            else:
                cur = (cur + ' ' + w).strip()
        lines.append(cur)
        for j, l in enumerate(lines):
            s += _t(50, y + 34 + j * 28, l, 21, 600, 'start')
        s += f'<path d="M520,{y + 90} L700,{y + 90}" {ST} stroke-width="3"/>'
    return s


# ---------------------------------------------------------------- 17. copiar con cuadricula
def cuadricula(cfg):
    cs, n = 55, 6
    s = '<defs><clipPath id="g1"><rect x="30" y="140" width="330" height="330"/></clipPath></defs>'
    for ox in (30, 390):
        s += f'<rect x="{ox}" y="140" width="{n * cs}" height="{n * cs}" fill="#fff" {ST} stroke-width="4"/>'
        for i in range(1, n):
            s += f'<path d="M{ox + i * cs},140 L{ox + i * cs},{140 + n * cs} M{ox},{140 + i * cs} L{ox + n * cs},{140 + i * cs}" fill="none" {ST} stroke-width="1.6" opacity=".55"/>'
    s += f'<g clip-path="url(#g1)">{cfg["head_main"](195, 330, 0.82, "happy")}</g>'
    s += _t(195, 110, 'Mira', 30, 700) + _t(555, 110, 'Copia', 30, 700)
    s += _t(375, 600, 'Fíjate en qué cuadrito está cada línea y cópiala en el de la derecha.', 19, 600)
    return s


# ---------------------------------------------------------------- 18. parejas
def fish(x, y, k=1.0):
    return (f'<path d="M{x - 40 * k},{y} Q{x},{y - 34 * k} {x + 36 * k},{y} Q{x},{y + 34 * k} {x - 40 * k},{y} Z" fill="#fff" {ST}/>'
            f'<path d="M{x + 32 * k},{y} L{x + 62 * k},{y - 24 * k} L{x + 62 * k},{y + 24 * k} Z" fill="#fff" {ST}/><circle cx="{x - 20 * k}" cy="{y - 4 * k}" r="{4 * k}" fill="#111"/>')


def bone(x, y, k=1.0):
    return (f'<path d="M{x - 38 * k},{y - 10 * k} L{x + 38 * k},{y - 10 * k} L{x + 38 * k},{y + 10 * k} L{x - 38 * k},{y + 10 * k} Z" fill="#fff" {ST}/>'
            + ''.join(f'<circle cx="{x + sx * 40 * k}" cy="{y + sy * 14 * k}" r="{13 * k}" fill="#fff" {ST}/>' for sx in (-1, 1) for sy in (-1, 1)))


def yarn2(x, y, r):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" {ST}/>'
            f'<path d="M{x - r * .8:.0f},{y - r * .3:.0f} Q{x},{y - r * .9:.0f} {x + r * .8:.0f},{y - r * .2:.0f} M{x - r * .9:.0f},{y + r * .2:.0f} Q{x},{y - r * .5:.0f} {x + r * .9:.0f},{y + r * .3:.0f}" fill="none" {ST} stroke-width="3"/>')


def ball(x, y, r):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" {ST}/><path d="M{x - r},{y} Q{x},{y - r * .6:.0f} {x + r},{y} M{x - r * .7:.0f},{y + r * .7:.0f} Q{x},{y + r * .2:.0f} {x + r * .7:.0f},{y + r * .7:.0f}" fill="none" {ST} stroke-width="3"/>'


LIKE = {'pez': lambda x, y: fish(x, y, 1.0), 'ovillo': lambda x, y: yarn2(x, y, 40), 'hueso': lambda x, y: bone(x, y, 1.0), 'pelota': lambda x, y: ball(x, y, 40),
        'bellota': lambda x, y: f'<ellipse cx="{x}" cy="{y + 6}" rx="26" ry="32" fill="#fff" {ST}/><path d="M{x - 30},{y - 8} Q{x},{y - 46} {x + 30},{y - 8} Z" fill="#fff" {ST}/>',
        'nido': lambda x, y: f'<path d="M{x - 48},{y - 10} Q{x},{y + 56} {x + 48},{y - 10} Z" fill="#fff" {ST}/><ellipse cx="{x}" cy="{y - 10}" rx="48" ry="12" fill="#fff" {ST}/>',
        'zanahoria': lambda x, y: f'<path d="M{x - 18},{y - 34} L{x + 18},{y - 34} L{x},{y + 40} Z" fill="#fff" {ST}/><path d="M{x},{y - 34} l-12,-22 M{x},{y - 34} l12,-22" fill="none" {ST}/>'}


def parejas(cfg):
    rnd = random.Random(8)
    cast = cfg['cast']
    right = list(range(4))
    rnd.shuffle(right)
    s = ''
    for i, ch in enumerate(cast):
        y = 150 + i * 150
        s += ch['fig'](150, y + 62, 120 / ch['h'] * 1.0) + f'<circle cx="290" cy="{y}" r="9" fill="#fff" {ST}/>'
    for j, k in enumerate(right):
        y = 150 + j * 150
        s += LIKE[cast[k]['like']](600, y) + f'<circle cx="460" cy="{y}" r="9" fill="#fff" {ST}/>'
    s += _t(375, 40, 'Une cada amigo con lo que más le gusta', 24, 700)
    return s, right


# ---------------------------------------------------------------- 19. tres cosas buenas
def gratitud():
    s = ''
    for i in range(3):
        x = 25 + i * 240
        s += f'<rect x="{x}" y="60" width="220" height="320" rx="20" fill="#fff" {ST} stroke-dasharray="2 12"/>' + _t(x + 110, 420, f'{i + 1}', 30, 700)
    s += _t(375, 40, 'Tres cosas buenas de hoy', 26, 700)
    s += f'<path d="M60,520 L690,520 M60,580 L690,580 M60,640 L690,640" fill="none" {ST} stroke-width="3"/>' + _t(60, 505, 'Se lo cuento a:', 21, 700, 'start')
    s += heart(375, 700, 0.3)
    return s


# ---------------------------------------------------------------- 20. soluciones
def soluciones(cfg, ws):
    ms, ox, oy, size = maze(sol=True)
    s = f'<g transform="translate(10,10) scale(.45)">{ms}</g>' + _t(160, 338, 'Laberinto', 19, 700)
    s += f'<g transform="translate(380,10) scale(.42)">{diferencias(cfg, sol=True)}</g>' + _t(520, 338, 'Diferencias', 19, 700)
    ws_svg, grid, pos = ws
    s += f'<g transform="translate(20,350) scale(.4)">{sopa(cfg, True, grid_pos=(grid, pos))[0]}</g>' + _t(160, 640, 'Sopa de letras', 19, 700)
    s += f'<g transform="translate(400,345) scale(.38)">{sudoku(cfg, True)}</g>' + _t(520, 640, 'Sudoku', 19, 700)
    return s


def build(cfg, tit):
    cast = cfg['cast']
    out = []
    ws_svg, grid, pos = sopa(cfg)
    cnt_svg, counts = contar(cfg)
    som_svg, som_order, _ = sombras(cfg)
    par_svg, par_right = parejas(cfg)
    ord_svg, story_order = ordenar(cfg)
    out.append(_pg(1, 'Colorea por números', 'Para hacer solo o sola', pixel(), 'Busca cada número en la leyenda y pinta la casilla de ese color. ¿Quién aparece?', '0 0 750 740'))
    ms, ox, oy, size = maze()
    mz = ms + cfg['head_main'](ox + 23, 18, .17, 'happy') + flower(ox + size - 23, oy + size + 36, .5)
    out.append(_pg(2, 'El laberinto de Lúa', 'Para hacer solo o sola', mz, 'Ayuda a Lúa a llegar hasta la flor. Hazlo con lápiz, por si te equivocas.', '0 0 750 700'))
    out.append(_pg(3, 'La otra mitad', 'Para hacer solo o sola', mirror(cfg), 'Dibuja la otra mitad de la cara de Lúa. Puedes usar los puntitos como guía.', '0 0 750 740'))
    out.append(_pg(4, 'Las 7 diferencias', 'En familia', diferencias(cfg), 'Hay siete diferencias entre los dos dibujos. ¡A ver quién las encuentra antes!', '0 0 750 740'))
    out.append(_pg(5, 'Une los puntos', 'Para hacer solo o sola', puntos(), '', '0 0 750 740'))
    out.append(_pg(6, 'Cuenta y escribe', 'Con un adulto', cnt_svg, 'Cuenta cuántos hay en cada fila y escribe el número en la casilla.', '0 0 750 710'))
    out.append(_pg(7, f'Un sombrero para {cfg["hat_name"]}', 'Para hacer solo o sola', sombrero(cfg), 'Dibuja el sombrero y coloréalo.', '0 0 750 740'))
    out.append(_pg(8, 'Sopa de letras', 'En familia', ws_svg + _t(375, 640, ' · '.join(cfg['words'][:4]), 20, 700) + _t(375, 676, ' · '.join(cfg['words'][4:]), 20, 700), 'Busca las palabras. Pueden ir hacia la derecha, hacia abajo o en diagonal.', '0 0 750 700'))
    out.append(_pg(9, 'Mandala de flores', 'Para hacer en calma', mandala(), 'Colorea sin prisa. Pon música suave, respira hondo y pinta lo que más te guste.', '0 0 750 740'))
    out.append(_pg(10, '¿Quién es la sombra?', 'Para hacer solo o sola', som_svg, 'Une cada amigo con su sombra y escribe su inicial dentro del círculo.', '0 0 750 700', SIL))
    out.append(_pg(11, 'Busca y encuentra', 'En familia', busca(cfg), 'Hay ocho cosas escondidas. Rodea cada una cuando la encuentres.', '0 0 750 740'))
    out.append(_pg(12, 'Sudoku de dibujos', 'Con un adulto', sudoku(cfg), 'Dibuja en cada fila, columna y cuadrado grande los cuatro dibujos, sin repetir ninguno.', '0 0 750 740'))
    out.append(_pg(13, '¿Cómo me siento?', 'Para hacer solo o sola', emociones(cfg), 'Dibuja la cara de cada emoción. Después cuéntale a alguien cuándo te has sentido así.', '0 0 750 740'))
    out.append(_pg(14, 'Ordena la historia', 'Para hacer solo o sola', ord_svg, 'Estos cuatro dibujos están desordenados. Escribe 1, 2, 3 y 4 según pasó en el cuento.', '0 0 750 740'))
    out.append(_pg(15, cfg.get('retos_titulo', 'Diez retos de jardín'), 'En familia', retos(cfg.get('retos')), 'Marca cada reto cuando lo hayáis hecho.', '0 0 750 740'))
    out.append(_pg(16, 'Adivinanzas', 'En familia', adivinanzas(), 'Un adulto lee la adivinanza y tú dices la respuesta. ¡Las soluciones están al final!', '0 0 750 740'))
    out.append(_pg(17, 'Copia con cuadrícula', 'Para hacer solo o sola', cuadricula(cfg), '', '0 0 750 640'))
    out.append(_pg(18, 'Las parejas', 'Para hacer solo o sola', par_svg, 'Traza una línea desde cada amigo hasta lo que más le gusta.', '0 0 750 740'))
    out.append(_pg(19, 'Tres cosas buenas', 'En familia', gratitud(), 'Antes de dormir, dibujad juntos tres cosas buenas del día y contádselas a alguien.', '0 0 750 740'))
    # soluciones
    sol_svg = soluciones(cfg, (ws_svg, grid, pos))
    nombres = [c['name'] for c in cfg.get('sombra_cast', cast)]
    texto = (f'<p style="font-size:11pt;margin:.03in 0"><b>Cuenta:</b> {", ".join(str(c) for c in counts)} (de arriba abajo). '
             f'<b>Sombras:</b> de izquierda a derecha, {", ".join(nombres[k] for k in som_order)}. '
             f'<b>Ordena la historia:</b> arriba izquierda {story_order[0] + 1}, arriba derecha {story_order[1] + 1}, abajo izquierda {story_order[2] + 1}, abajo derecha {story_order[3] + 1}. '
             f'<b>Parejas:</b> {"; ".join(cast[i]["name"] + " con " + cast[i]["like"] for i in range(4))}.</p>'
             f'<p style="font-size:11pt;margin:.03in 0"><b>Adivinanzas:</b> {"; ".join(f"{i + 1}. {r}" for i, (_, r) in enumerate(ADIV))}.</p>')
    out.append(_pg(20, 'Soluciones', 'Para los adultos', sol_svg, '', '0 0 750 660').replace('</div></section>', texto + '</div></section>'))
    return out
