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


def e1():
    s = sun(95, 100, 42) + cloud(500, 50, 160) + cloud(300, 160, 110)
    s += hill(700, W, H, 20) + tree(655, 715, 0.85)
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
    s = moon(590, 160, 85) + stars_night(NIGHT) + hill(640, W, H, 25) + tree(650, 650, 0.95)
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
    s = moon(110, 110, 65) + stars_night(NIGHT[1:]) + hill(650, W, H, 20) + tree(645, 660, 0.95)
    s += nest_front(640, 455)
    s += cat_side(320, 725, 1.0, 'happy', flip=1, tail='up')
    s += bird(300, 565, 0.5, 'happy', wings='down')
    s += twinkle(520, 560, 0.7) + twinkle(560, 520, 0.5) + grass(120, 770)
    return s


def e9():
    s = moon(110, 100, 60) + star(250, 90, 14) + star(420, 70, 12) + hill(715, W, H, 15)
    s += tree(540, 725, 1.55)
    s += bird(545, 385, 0.7, 'happy', flip=-1, wings='up') + nest_front(545, 372)
    s += bird(385, 340, 0.5, 'happy', wings='up')
    s += f'<path d="M330,360 l-40,8 M335,330 l-44,-4 M345,392 l-34,16" {ST} stroke-width="4"/>'
    s += cat_sit(185, 430, 0.95, 'smile', look=1)
    s += heart(470, 260, 0.35) + grass(300, 770) + flower(80, 740, 0.8)
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
    s = heart(375, 330, 5.4)
    s += cat_sit(375, 300, 0.62, 'joy', tail='up')
    s += star(80, 80, 22) + star(680, 90, 22) + star(60, 420, 14) + star(700, 430, 14) + twinkle(120, 200, 1) + twinkle(640, 220, 1)
    s += squirrel(95, 755, 0.5, 'happy') + rabbit(215, 758, 0.48, 'happy') + bird(360, 758, 0.55, 'happy')
    s += ladybug(520, 705, 0.5) + butterfly(650, 690, 0.55)
    return s


SCENES = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13]

TEXTOS = [
    "Lúa era una gatita gris.",
    "Sus amigos tenían colores muy vivos.",
    "«Tú eres muy gris», le dijeron.",
    "Lúa se fue sola.",
    "Llegó la noche y Lúa estaba triste.",
    "De pronto, alguien lloraba muy bajito.",
    "Era Pipa, un pajarito perdido.",
    "Lúa veía muy bien en la oscuridad y lo llevó a cuestas.",
    "Juntos llegaron hasta su nido.",
    "«¡Gracias, Lúa!», dijo la mamá de Pipa.",
    "Al día siguiente, sus amigos le pidieron perdón.",
    "Lúa sonrió: «¿Jugamos?».",
    "Todos somos especiales, tal como somos.",
]
