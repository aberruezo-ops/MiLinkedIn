# Escenas del cuento "Lua, la gatita gris". Lienzo: 750 x 780.
from lib import *
from animales import *

W, H = 750, 780


def firefly(x, y):
    s = f'<circle cx="{x}" cy="{y}" r="8" fill="#fff" {ST} stroke-width="4"/>'
    for dx, dy in ((-16, -4), (16, -4), (0, -18), (-12, 12), (12, 12)):
        s += f'<path d="M{x + dx * .6:.0f},{y + dy * .6:.0f} L{x + dx:.0f},{y + dy:.0f}" {ST} stroke-width="3"/>'
    return s


def stars_night(pts):
    return ''.join(star(x, y, r) if i % 2 == 0 else twinkle(x, y, r / 14) for i, (x, y, r) in enumerate(pts))


NIGHT = [(90, 90, 18), (230, 190, 14), (380, 80, 16), (500, 210, 12), (680, 330, 14), (60, 330, 12), (300, 290, 12)]


def flowers(pts):
    return ''.join(flower(x, y, k) for x, y, k in pts)


def e_flores():
    s = sun(650, 90, 36) + cloud(60, 60, 150) + hill(700, W, H, 20)
    s += cat_sit(375, 370, 1.0, 'sad', tail='down')
    for x, y in ((300, 278), (350, 245), (408, 243), (455, 280), (322, 540), (428, 562), (375, 605), (288, 470), (466, 482)):
        s += petal_head(x, y, 0.7)
    for x, y, r in ((190, 410, 20), (570, 350, -30), (520, 580, 40), (235, 610, -10), (600, 480, 15)):
        s += f'<ellipse cx="{x}" cy="{y}" rx="9" ry="15" transform="rotate({r} {x} {y})" fill="#fff" {ST} stroke-width="3.4"/>'
    s += f'<ellipse cx="375" cy="735" rx="210" ry="42" fill="#fff" {ST}/>'
    s += f'<g transform="translate(375,738) scale(0.3,-0.3)">{cat_head(0.3, "sad")}</g>'
    s += f'<path d="M205,736 q10,-6 20,0 M520,742 q10,-6 20,0" fill="none" {ST} stroke-width="3"/>' + grass(90, 700)
    return s


def e_luna():
    s = moon(590, 150, 105) + stars_night(NIGHT) + hill(660, W, H, 20)
    s += cat_sit(250, 425, 1.0, 'smile')
    cx0, cy0 = 250, 425
    for ang in range(200, 341, 20):
        r = math.radians(ang)
        s += f'<path d="M{cx0 + math.cos(r) * 168:.0f},{cy0 + math.sin(r) * 168:.0f} L{cx0 + math.cos(r) * 196:.0f},{cy0 + math.sin(r) * 196:.0f}" {ST} stroke-width="4"/>'
    s += twinkle(90, 520, 0.9) + twinkle(420, 520, 0.9) + twinkle(100, 640, 0.6) + star(405, 640, 12)
    s += bird(575, 715, 1.1, 'happy', flip=-1, wings='up')
    return s


def e_buho():
    s = moon(110, 100, 60) + stars_night(NIGHT[1:]) + hill(660, W, H, 20)
    nx, ny = nest_pos(570, 705, 1.4)
    s += tree(570, 705, 1.4, branch=True)
    s += owl(nx, ny + 6, 0.6, look=-1)
    s += bubble(60, 150, 250, 66, '¿Quién anda ahí?', nx - 40, ny - 150, 28)
    s += cloud(20, 600, 240) + cloud(455, 615, 210)
    s += cat_side(290, 742, 0.95, 'smile', flip=1, tail='up')
    s += bird(280, 588, 0.45, 'happy')
    s += f'<path d="M110,758 l50,0 M200,765 l60,0 M360,760 l50,0" {ST} stroke-width="3"/>'
    return s


def e1():
    s = sun(95, 100, 42) + cloud(500, 50, 160) + cloud(300, 160, 110)
    s += hill(700, W, H, 20) + tree(615, 718, 1.15)
    s += cat_sit(375, 395, 1.15, 'happy')
    s += butterfly(555, 330, 0.55)
    s += flowers([(110, 725, 1.0), (205, 750, 0.9), (560, 735, 1.0), (470, 752, 0.8)]) + grass(280, 770) + grass(520, 775)
    return s


def e2():
    s = sun(650, 90, 36) + cloud(60, 60, 150) + hill(700, W, H, 20)
    s += squirrel(150, 725, 0.95, 'happy')
    s += rabbit(315, 730, 0.9, 'happy')
    s += ladybug(450, 655, 0.8)
    s += butterfly(470, 330, 1.0)
    s += cat_sit(610, 520, 0.7, 'sad', look=-1, tail='up')
    s += flowers([(60, 750, 0.9), (400, 765, 0.8), (560, 760, 0.8)]) + heart(250, 200, 0.4) + star(390, 150, 16)
    return s


def e3():
    s = sun(660, 80, 34) + cloud(50, 50, 140) + hill(700, W, H, 20)
    s += cat_sit(190, 420, 1.0, 'sad', tear=True, tail='down')
    s += squirrel(445, 722, 0.9, 'open')
    s += rabbit(585, 728, 0.85, 'happy', flip=-1)
    s += ladybug(690, 660, 0.55)
    s += butterfly(640, 330, 0.8)
    s += bubble(300, 300, 240, 72, '¡Muy gris!', 440, 480, 32)
    s += flowers([(330, 760, 0.8), (60, 755, 0.8)]) + grass(520, 775)
    return s


def e4():
    s = sun(650, 110, 38) + cloud(90, 80, 150)
    s += hill(600, W, H, 12) + tree(110, 640, 0.7)
    s += squirrel(620, 600, 0.32, 'happy') + rabbit(690, 604, 0.3, 'happy') + butterfly(560, 470, 0.4)
    s += cat_side(430, 735, 1.05, 'sad', flip=-1, tail='down', head_down=True)
    s += flowers([(90, 735, 0.9), (210, 765, 0.8)]) + grass(600, 760)
    return s


def e5():
    s = moon(590, 160, 85) + stars_night(NIGHT) + hill(640, W, H, 25) + tree(610, 655, 1.2)
    s += cat_sit(290, 400, 1.0, 'sad', tail='curl')
    s += firefly(130, 470) + firefly(470, 600) + firefly(520, 400) + firefly(90, 580)
    s += grass(430, 750) + flower(60, 700, 0.8)
    return s


def e6():
    s = moon(120, 130, 70) + stars_night(NIGHT[2:]) + hill(650, W, H, 20)
    s += cat_sit(300, 400, 1.05, 'open', tail='curl')
    s += cloud(560, 440, 170) + f'<path d="M600,500 q15,-14 30,0 M650,495 q15,-14 30,0" fill="none" {ST} stroke-width="4"/>'
    s += bubble(430, 200, 270, 72, 'Piii... piii...', 640, 430, 30)
    for k in (1, 2, 3):
        s += f'<path d="M{430 + k * 18},{360 - k * 18} Q{450 + k * 28},{385} {430 + k * 18},{410 + k * 18}" fill="none" {ST} stroke-width="4"/>'
    s += grass(150, 760) + flower(650, 700, 0.9)
    return s


def e7():
    s = moon(630, 110, 68) + stars_night(NIGHT) + hill(650, W, H, 20)
    s += cat_sit(225, 410, 1.0, 'smile', look=1)
    s += bird(560, 710, 1.2, 'sad', flip=-1, tear=True)
    s += heart(395, 520, 0.35) + grass(430, 775) + flower(80, 735, 0.8)
    return s


def e8():
    s = moon(110, 110, 65) + stars_night(NIGHT[1:]) + hill(650, W, H, 20)
    nx, ny = nest_pos(570, 705, 1.4)
    s += tree(570, 705, 1.4, branch=True)
    s += nest_back(nx, ny) + bird(nx, ny + 6, 0.6, 'sad', flip=-1) + nest_front(nx, ny)
    s += bubble(170, 190, 170, 62, '¡Pipa!', nx - 20, ny - 112, 32)
    s += cat_side(255, 745, 1.05, 'happy', flip=1, tail='up')
    s += bird(245, 572, 0.5, 'happy')
    s += twinkle(120, 520, 0.5) + grass(90, 770) + flower(680, 765, 0.7)
    return s


def e9():
    s = moon(110, 100, 60) + star(250, 90, 14) + star(420, 70, 12) + hill(715, W, H, 15)
    nx, ny = nest_pos(570, 725, 1.4)
    s += tree(570, 725, 1.4, branch=True)
    s += nest_back(nx, ny) + bird(nx + 24, ny + 6, 0.62, 'happy', flip=-1) + bird(nx - 28, ny + 8, 0.42, 'happy') + nest_front(nx, ny)
    s += cat_sit(110, 480, 0.9, 'joy', look=1)
    s += heart(nx, ny - 160, 0.4) + heart(nx - 75, ny - 120, 0.25) + heart(nx + 75, ny - 120, 0.25)
    s += grass(300, 775) + flower(60, 755, 0.8)
    return s


def e10():
    s = sun(375, 105, 46) + cloud(80, 60, 150) + cloud(520, 80, 150) + hill(715, W, H, 15)
    s += bird(170, 725, 1.25, 'happy')
    s += cat_sit(400, 420, 1.0, 'joy')
    s += bird(615, 725, 0.9, 'happy', flip=-1)
    s += bubble(40, 300, 280, 72, '¡Gracias, Lúa!', 175, 520, 32)
    s += heart(400, 230, 0.5) + heart(300, 190, 0.3) + heart(500, 190, 0.3)
    s += flowers([(60, 755, 0.8), (700, 755, 0.8)]) + grass(300, 775)
    return s


def e11():
    s = sun(110, 100, 36) + cloud(400, 50, 150) + hill(715, W, H, 15)
    s += squirrel(135, 730, 0.9, 'sorry', item='flower')
    s += rabbit(295, 735, 0.85, 'sorry', item='flower')
    s += ladybug(405, 668, 0.6)
    s += butterfly(400, 380, 0.7)
    s += cat_sit(575, 430, 1.0, 'happy', tail='up')
    s += bubble(50, 250, 220, 72, '¡Perdón!', 135, 450, 34)
    s += heart(480, 250, 0.35) + flowers([(660, 755, 0.8), (40, 760, 0.7)]) + grass(380, 775)
    return s


def e12():
    s = rainbow(375, 560, 330, 5, 30) + sun(90, 90, 36) + cloud(560, 40, 130) + hill(715, W, H, 15)
    s += cat_sit(375, 430, 0.9, 'joy', tail='up')
    s += squirrel(120, 725, 0.8, 'happy') + rabbit(245, 730, 0.75, 'happy')
    s += bird(585, 725, 0.8, 'happy', flip=-1) + ladybug(705, 668, 0.45)
    s += butterfly(510, 380, 0.7) + butterfly(240, 330, 0.55, flip=-1)
    s += star(60, 360, 14) + star(700, 360, 14) + heart(375, 640, 0.35)
    return s


def e13():
    s = f'<path d="M-10,700 L760,700" {ST}/>'
    s += f'<rect x="520" y="60" width="190" height="190" rx="14" fill="#fff" {ST}/><path d="M615,60 L615,250 M520,155 L710,155" {ST}/>'
    s += moon(566, 108, 28) + star(668, 106, 10) + star(662, 205, 9) + star(560, 205, 9)
    s += cat_sit(330, 380, 1.05, 'smile', tail='curl')
    s += cat_sit(335, 545, 0.55, 'joy', tail='up')
    s += tube2('M247,470 Q200,580 300,615', 36, '#fff', 1) + tube2('M413,470 Q462,580 366,615', 36, '#fff', 1)
    s += heart(330, 200, 0.55) + heart(220, 250, 0.3) + heart(440, 250, 0.3)
    return s


def e14():
    s = heart(375, 330, 5.4)
    s += cat_sit(375, 300, 0.62, 'joy', tail='up')
    s += star(80, 80, 22) + star(680, 90, 22) + star(60, 420, 14) + star(700, 430, 14) + twinkle(120, 200, 1) + twinkle(640, 220, 1)
    s += squirrel(95, 755, 0.5, 'happy') + rabbit(215, 758, 0.48, 'happy') + bird(360, 758, 0.55, 'happy')
    s += ladybug(520, 705, 0.5) + butterfly(650, 690, 0.55)
    return s


SCENES = [e1, e2, e3, e_flores, e4, e5, e6, e7, e_luna, e8, e_buho, e9, e10, e11, e12, e13, e14]

# Mora, la mariquita escondida, en las escenas donde no sale ya a la vista (indice de escena: x, y)
HIDDEN = {0: (140, 655), 3: (110, 705), 4: (185, 705), 5: (110, 645), 6: (110, 705), 7: (405, 705), 8: (130, 700), 9: (430, 750), 10: (690, 705), 11: (660, 740), 12: (520, 748), 15: (620, 690)}

TEXTOS = [
    "Lúa era una gatita gris, y le encantaba jugar.",
    "Sus amigos tenían colores muy vivos y siempre andaban juntos.",
    "«Tú eres muy gris», le dijeron. «No eres como nosotros».",
    "Lúa probó a cubrirse de flores. Pero al mirarse en el charco, no se reconoció.",
    "Lúa se fue sola, con el rabo caído.",
    "Llegó la noche. Lúa estaba triste, y estar triste está bien.",
    "De pronto, alguien lloraba muy bajito.",
    "Era Pipa, un pajarito que se había perdido.",
    "Bajo la luna, el pelo de Lúa brillaba como plata. Pipa dejó de llorar.",
    "Lúa veía muy bien en la oscuridad. «Súbete», le dijo.",
    "Un búho vigilaba el camino. Pero el gris de Lúa se mezclaba con las sombras, y no la vio.",
    "Juntos llegaron hasta su nido, despacito.",
    "«¡Gracias, Lúa!», dijo la mamá de Pipa.",
    "Pipa lo contó todo. Los amigos de Lúa le pidieron perdón. Debieron quererla desde el principio.",
    "Lúa sonrió: «¿Jugamos?».",
    "Esa noche, mamá la abrazó: «Te quiero tal como eres».",
    "Lúa valía igual antes que después. Todos valemos tal como somos.",
]
