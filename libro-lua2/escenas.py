# Libro 2: "Lúa y el jardín de todos". Lienzo de cada escena: 750 x 780.
from jardin import *

W, H = 750, 780
G = 700
NIGHT = [(90, 90, 18), (230, 190, 14), (380, 80, 16), (500, 210, 12), (680, 330, 14), (60, 330, 12), (300, 290, 12)]


def csit(cx, g, s=1.0, **kw):
    """Gata sentada apoyada en el suelo g."""
    return cat_sit(cx, g - 272 * s, s, **kw)


def stars_night(pts):
    return ''.join(star(x, y, r) if i % 2 == 0 else twinkle(x, y, r / 14) for i, (x, y, r) in enumerate(pts))


def firefly(x, y):
    s = f'<circle cx="{x}" cy="{y}" r="8" fill="#fff" {ST} stroke-width="4"/>'
    for dx, dy in ((-16, -4), (16, -4), (0, -18), (-12, 12), (12, 12)):
        s += f'<path d="M{x + dx * .6:.0f},{y + dy * .6:.0f} L{x + dx:.0f},{y + dy:.0f}" {ST} stroke-width="3"/>'
    return s


def paw(x, y, k=1.0, ang=0):
    s = f'<g transform="translate({x},{y}) rotate({ang}) scale({k})"><ellipse cx="0" cy="8" rx="13" ry="10" fill="#fff" {ST} stroke-width="3"/>'
    for dx, dy in ((-16, -8), (-6, -17), (6, -17), (16, -8)):
        s += f'<ellipse cx="{dx}" cy="{dy}" rx="5" ry="6.5" fill="#fff" {ST} stroke-width="3"/>'
    return s + '</g>'


def bulb(x, y, k=1.0):
    s = f'<circle cx="{x}" cy="{y}" r="{30 * k}" fill="#fff" {ST}/>'
    s += f'<path d="M{x - 14 * k},{y + 28 * k} L{x - 14 * k},{y + 46 * k} L{x + 14 * k},{y + 46 * k} L{x + 14 * k},{y + 28 * k}" fill="#fff" {ST}/>'
    s += f'<path d="M{x - 14 * k},{y + 36 * k} L{x + 14 * k},{y + 36 * k}" fill="none" {ST} stroke-width="3"/>'
    s += f'<path d="M{x - 10 * k},{y + 8 * k} L{x - 4 * k},{y - 8 * k} L{x + 4 * k},{y + 8 * k} L{x + 10 * k},{y - 8 * k}" fill="none" {ST} stroke-width="3.4"/>'
    for a in (-70, -35, 0, 35, 70):
        r = math.radians(a - 90)
        s += f'<path d="M{x + math.cos(r) * 42 * k:.0f},{y + math.sin(r) * 42 * k:.0f} L{x + math.cos(r) * 58 * k:.0f},{y + math.sin(r) * 58 * k:.0f}" fill="none" {ST} stroke-width="4"/>'
    return s


def yarn(x, y, r):
    s = f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" {ST}/>'
    s += f'<path d="M{x - r * .8:.0f},{y - r * .3:.0f} Q{x},{y - r * .9:.0f} {x + r * .8:.0f},{y - r * .2:.0f} M{x - r * .9:.0f},{y + r * .2:.0f} Q{x},{y - r * .5:.0f} {x + r * .9:.0f},{y + r * .3:.0f} M{x - r * .7:.0f},{y + r * .6:.0f} Q{x},{y} {x + r * .6:.0f},{y + r * .7:.0f}" fill="none" {ST} stroke-width="3"/>'
    return s + f'<path d="M{x - r},{y + r * .5:.0f} Q{x - r * 2.4:.0f},{y + r * 1.4:.0f} {x - r * 3.4:.0f},{y + r * .7:.0f} T{x - r * 5:.0f},{y + r * .9:.0f}" fill="none" {ST} stroke-width="3"/>'


def pot_tipped(x, g, k=1.0):
    s = f'<g transform="translate({x},{g - 34 * k}) rotate(-78) scale({k})"><path d="M-34,-34 L34,-34 L26,34 L-26,34 Z" fill="#fff" {ST}/><rect x="-40" y="-48" width="80" height="16" rx="5" fill="#fff" {ST}/></g>'
    s += f'<path d="M{x - 40 * k},{g - 10 * k} Q{x - 90 * k},{g - 30 * k} {x - 120 * k},{g} Z" fill="#fff" {ST}/>'
    for dx, dy in ((-60, -6), (-84, -4), (-104, -2), (-72, -16)):
        s += f'<circle cx="{x + dx * k:.0f}" cy="{g + dy * k:.0f}" r="3" fill="#111"/>'
    return s


def bunting(x0, x1, y, sag=40, n=9):
    s = f'<path d="M{x0},{y} Q{(x0 + x1) / 2},{y + sag * 2} {x1},{y}" fill="none" {ST} stroke-width="3.4"/>'
    for i in range(n):
        t = (i + .5) / n
        px = x0 + (x1 - x0) * t
        py = y + 2 * sag * t * (1 - t) * 2 * .5 * 2
        s += f'<path d="M{px - 16:.0f},{py - 2:.0f} L{px + 16:.0f},{py - 2:.0f} L{px:.0f},{py + 34:.0f} Z" fill="#fff" {ST} stroke-width="3.4"/>'
    return s


def flowers(pts):
    return ''.join(flower(x, y, k) for x, y, k in pts)


def tufts(pts):
    return ''.join(grass(x, y, k) for x, y, k in pts)


# --------------------------------------------------------------------- escenas
def e1():
    s = sun(95, 100, 40) + cloud(520, 55, 160) + cloud(300, 150, 100) + hill(690, W, H, 18)
    s += fence(10, 300, 650, 80)
    s += rocks(500, 705, 1.2) + tin_can(110, 712, 1, 20) + tin_can(185, 735, .9, 70) + tin_can(650, 690, .8, -25)
    s += csit(375, 705, 0.95, mood='smile')
    s += tufts([(60, 712, 1.5), (250, 740, 1.4), (580, 748, 1.5), (700, 722, 1.3)])
    s += sprout(150, 758, 1.0) + butterfly(545, 330, 0.6)
    return s


def e2():
    s = sun(660, 90, 38) + cloud(60, 70, 150) + hill(705, W, H, 15) + tree(110, 700, 1.0) + fence(500, 745, 650, 80)
    s += hera_sit(360, 715, 1.05, 'smile')
    s += butterfly(395, 330, 0.5) + snail(590, 735, 0.9)
    s += flowers([(210, 760, 0.9), (540, 765, 0.8), (700, 770, 0.8)]) + tufts([(270, 745, 1.4)])
    return s


def e3():
    s = sun(90, 90, 36) + cloud(520, 60, 150) + hill(705, W, H, 15)
    s += csit(330, 710, 1.0, mood='mischief', kind='raspi', look=1)
    s += bulb(540, 260, 1.0)
    s += pot_tipped(590, 715, 1.0) + yarn(690, 690, 30)
    for i, (px, py) in enumerate(((60, 770), (120, 745), (180, 765), (230, 740))):
        s += paw(px, py, 0.8, 70)
    s += tufts([(470, 750, 1.3)])
    return s


def e4():
    s = sun(650, 90, 36) + cloud(60, 60, 150) + hill(705, W, H, 15)
    s += csit(375, 710, 1.0, mood='silly', kind='neu', tail='up')
    s += tin_can(375, 318, 0.9, 14)
    s += csit(120, 705, 0.55, mood='joy') + bird(615, 705, 0.75, 'happy', flip=-1)
    s += daisy(210, 765, 1.0, 100) + daisy(520, 770, 1.1, 110) + sunflower(700, 770, 0.6, 150)
    s += star(260, 210, 14) + star(500, 190, 12) + heart(640, 300, 0.3)
    return s


def e5():
    s = sun(95, 90, 36) + cloud(520, 50, 150) + hill(705, W, H, 15)
    s += csit(130, 710, 0.62, mood='mischief', kind='raspi', look=1)
    s += csit(300, 710, 0.64, mood='happy')
    s += hera_sit(480, 715, 0.8, 'smile')
    s += csit(650, 710, 0.62, mood='silly', kind='neu')
    s += bubble(110, 150, 340, 96, '¿Y si hacemos|aquí un jardín?', 295, 480, 32)
    s += heart(560, 200, 0.4) + star(640, 150, 16)
    s += tufts([(60, 750, 1.3), (390, 750, 1.4), (700, 748, 1.3)])
    return s


def e6():
    s = sun(100, 90, 36) + cloud(500, 60, 150) + hill(700, W, H, 15)
    s += hera_sit(100, 720, 0.78, 'smile')
    s += wheelbarrow(285, 715, 1.2) + tin_can(250, 640, 1, 10) + tin_can(300, 635, 1, -15) + tin_can(350, 645, .9, 25)
    for x in (230, 330, 405):
        s += tin_can(x, 735, 0.9, 0) + sprout(x, 713, 0.75)
    s += bin_(520, 712, 0.78, 'PAPEL') + bin_(600, 712, 0.78, 'ENVASES') + bin_(680, 712, 0.78, 'VIDRIO')
    s += cat_action(430, 440, 0.55, 'leap', 'happy')
    s += f'<g transform="translate(160,655) scale(0.32)">{cat_head(0.32, "mischief", 1, False, "raspi")}</g>'
    s += csit(520, 570, 0.4, mood='silly', kind='neu') + tin_can(520, 470, .55, 12)
    s += tufts([(20, 748, 1.3), (470, 765, 1.2)])
    return s


def e7():
    s = hill(690, W, H, 15)
    s += f'<path d="M110,600 A110,110 0 0 1 330,600 Z" fill="#fff" {ST}/>'
    for i in range(-5, 6):
        ang = math.radians(270 + i * 15)
        s += f'<path d="M220,600 m{math.cos(ang) * 135:.0f},{math.sin(ang) * 135:.0f} l{math.cos(ang) * 28:.0f},{math.sin(ang) * 28:.0f}" {ST} stroke-width="4.4"/>'
    s += cloud(500, 120, 150) + cloud(40, 130, 110)
    s += csit(150, 600, 0.28, mood='mischief', kind='raspi') + csit(235, 600, 0.28, mood='silly', kind='neu') + hera_lie(560, 602, 0.28, mood='sleep')
    s += csit(375, 725, 1.0, mood='worried')
    for dx, dy in ((520, 345), (540, 390), (180, 340)):
        s += f'<path d="M{dx},{dy} q-10,18 0,26 q10,-8 0,-26 z" fill="#fff" {ST} stroke-width="3.2"/>'
    s += watering_can(620, 745, 0.9) + wheelbarrow(110, 750, 0.9)
    s += f'<path d="M470,700 L560,625" {ST} stroke-width="7"/><path d="M548,612 L585,642 L560,660 L528,634 Z" fill="#fff" {ST}/>'
    return s


def e8():
    s = sun(660, 80, 34) + cloud(40, 70, 140) + hill(660, W, H, 15)
    s += hera_sit(150, 700, 0.95, 'open')
    s += csit(420, 610, 0.5, mood='happy') + csit(535, 612, 0.5, mood='mischief', kind='raspi') + csit(650, 610, 0.5, mood='silly', kind='neu')
    s += bubble(200, 90, 330, 90, 'Cada semilla|es distinta', 160, 390, 34)
    s += f'<rect x="40" y="640" width="670" height="110" rx="14" fill="#fff" {ST}/>'
    names = ['bean', 'sunflower', 'pea', 'maple', 'dandelion', 'dust']
    for i, n in enumerate(names):
        x0 = 40 + i * 111.6
        s += f'<path d="M{x0},640 L{x0},750" fill="none" {ST} stroke-width="3.4"/>' if i else ''
        s += seed(n, x0 + 56, 698, 0.8)
    return s


def e9():
    s = hill(650, W, H, 15)
    s += f'<path d="M-10,720 Q375,670 760,720 L760,790 L-10,790 Z" fill="#fff" {ST}/>'
    for y in (745, 768):
        s += f'<path d="M20,{y} Q375,{y - 40} 730,{y}" fill="none" {ST} stroke-width="3"/>'
    s += csit(110, 715, 0.62, mood='smile') + seed('bean', 165, 748, 0.4)
    s += csit(295, 715, 0.62, mood='mischief', kind='raspi')
    for x in (225, 255, 295, 335, 365, 395):
        s += f'<ellipse cx="{x}" cy="{752 + (x % 3) * 4}" rx="13" ry="6" fill="#fff" {ST} stroke-width="3"/>'
    s += hera_sit(510, 718, 0.68, 'smile')
    s += csit(670, 715, 0.62, mood='silly', kind='neu')
    s += watering_can(640, 520, 0.7)
    for dx, dy in ((690, 560), (700, 590), (715, 625), (675, 600)):
        s += f'<path d="M{dx},{dy} q-6,12 0,18 q6,-6 0,-18 z" fill="#fff" {ST} stroke-width="3"/>'
    s += sun(90, 90, 34) + cloud(300, 50, 150)
    return s


def e10():
    s = hill(690, W, H, 15)
    for i, d in enumerate(('1', '2', '3', '4')):
        x = 50 + i * 165
        s += f'<rect x="{x}" y="55" width="130" height="110" rx="12" fill="#fff" {ST}/><rect x="{x}" y="55" width="130" height="30" rx="12" fill="#fff" {ST}/>'
        s += f'<text x="{x + 65}" y="76" {font(20, 700)} fill="#111">DÍA {d}</text>'
        s += sun(x + 65, 126, 14, face=False) if i % 2 == 0 else cloud(x + 36, 106, 58)
    s += csit(250, 715, 1.0, mood='worried', kind='raspi', look=1)
    s += f'<ellipse cx="540" cy="735" rx="90" ry="24" fill="#fff" {ST}/>'
    s += f'<path d="M540,730 L540,690" {ST} stroke-width="5"/><path d="M540,690 L575,700 L540,712 Z" fill="#fff" {ST}/>'
    s += hera_lie(640, 690, 0.5, mood='sleep') + snail(450, 770, 0.7)
    s += thought(300, 190, 150, 90, [(280, 310, 10), (300, 335, 14)]) + f'<text x="375" y="250" {font(60, 700)} fill="#111">?</text>'
    return s


def e11():
    s = moon(600, 150, 85) + stars_night(NIGHT) + hill(670, W, H, 20)
    s += csit(300, 715, 1.0, mood='worried', kind='raspi', claws=True)
    for x, y, n in ((520, 740, 'bean'), (600, 765, 'sunflower'), (660, 735, 'pea')):
        s += seed(n, x, y, 0.45)
    for x, y in ((470, 560), (540, 520), (610, 570), (180, 480), (110, 520)):
        s += f'<ellipse cx="{x}" cy="{y}" rx="12" ry="8" transform="rotate({x % 40} {x} {y})" fill="#fff" {ST} stroke-width="3.2"/>'
    s += firefly(90, 600) + firefly(660, 470)
    s += tufts([(460, 768, 1.3), (60, 760, 1.4)])
    return s


def e12():
    s = sun(670, 80, 34) + cloud(50, 60, 140) + hill(705, W, H, 15)
    s += csit(180, 715, 0.95, mood='angry')
    s += csit(520, 715, 0.75, mood='sad', kind='raspi')
    s += hera_sit(670, 720, 0.52, 'smile')
    s += bubble(30, 150, 320, 90, '¡Raspi,|siempre igual!', 170, 410, 30)
    s += bubble(380, 270, 310, 90, 'Siempre me|echáis la culpa', 520, 405, 28)
    for x, y, n in ((330, 750, 'bean'), (400, 775, 'sunflower'), (610, 770, 'pea')):
        s += seed(n, x, y, 0.4)
    s += tufts([(260, 760, 1.2)])
    return s


def e13():
    s = sun(120, 80, 36) + cloud(500, 60, 150) + hill(710, W, H, 15)
    s += hera_sit(375, 720, 1.05, 'smile')
    s += csit(140, 715, 0.7, mood='sad', tail='down') + csit(615, 715, 0.7, mood='sad', kind='raspi', tail='down')
    s += bubble(190, 70, 360, 90, 'Equivocarse|es aprender', 375, 360, 32)
    s += heart(215, 360, 0.4) + heart(530, 360, 0.4)
    s += flowers([(60, 765, 0.8), (690, 768, 0.8)]) + tufts([(250, 760, 1.2)])
    return s


def e_compost():
    s = sun(660, 90, 36) + cloud(60, 60, 150) + hill(705, W, H, 15)
    s += compost_bin(440, 712, 1.45)
    s += hera_sit(95, 718, 0.85, 'open')
    s += bubble(30, 90, 360, 96, 'Las cáscaras son comida|para la tierra', 120, 380, 29)
    s += csit(235, 715, 0.5, mood='silly', kind='neu') + banana_peel(205, 600, 0.6)
    s += csit(615, 715, 0.5, mood='mischief', kind='raspi') + csit(700, 715, 0.42, mood='happy')
    s += worm(345, 748, 1.0) + worm(520, 765, 0.9) + banana_peel(330, 770, 0.7)
    s += tufts([(580, 775, 1.2), (180, 770, 1.2)])
    return s


def e14():
    s = storm_cloud(-10, 10, 360) + storm_cloud(330, 20, 400) + hill(690, W, H, 20)
    s += f'<path d="M360,230 L320,330 L360,330 L330,420 L410,300 L368,300 L396,230 Z" fill="#fff" {ST}/>'
    for y in (440, 500, 560):
        s += f'<path d="M30,{y} Q200,{y - 22} 360,{y} M400,{y + 16} Q560,{y - 6} 720,{y + 16}" fill="none" {ST} stroke-width="3"/>'
    for x in (60, 330, 520):
        s += f'<ellipse cx="{x}" cy="755" rx="45" ry="14" fill="#fff" {ST}/><path d="M{x},750 L{x},722" {ST} stroke-width="4"/>'
    s += csit(150, 700, 0.6, mood='worried') + csit(300, 700, 0.6, mood='worried', kind='raspi')
    s += hera_sit(560, 705, 0.72, 'smile') + csit(680, 700, 0.5, mood='open', kind='neu')
    return s


def e15():
    s = storm_cloud(380, 10, 350) + hill(670, W, H, 15)
    s += f'<path d="M520,330 Q480,420 560,470 Q640,520 610,600 Q590,660 520,700" fill="none" {ST} stroke-width="3.4"/>'
    for y in (380, 430, 480):
        s += f'<path d="M600,{y} q10,-8 20,0 t20,0 t20,0" fill="none" {ST} stroke-width="3"/>'
    s += f'<path d="M510,718 Q620,775 760,740" fill="none" {ST} stroke-width="4"/><path d="M510,740 Q620,790 760,760" fill="none" {ST} stroke-width="4"/>'
    for x in (80, 190):
        s += f'<ellipse cx="{x}" cy="640" rx="46" ry="14" fill="#fff" {ST}/><path d="M{x},636 L{x},610" {ST} stroke-width="4"/>'
    s += hera_lie(250, 715, 0.9, mood='smile')
    s += cat_side(600, 735, 0.75, 'smile', kind='raspi', head_down=True)
    for x, y in ((520, 650), (580, 620), (650, 655)):
        s += f'<ellipse cx="{x}" cy="{y}" rx="12" ry="8" transform="rotate({x % 50} {x} {y})" fill="#fff" {ST} stroke-width="3.2"/>'
    for x in range(430, 750, 50):
        s += f'<path d="M{x},250 l-10,34 M{x + 24},300 l-10,34" fill="none" {ST} stroke-width="3.2"/>'
    return s


def e16():
    s = storm_cloud(300, 10, 400) + hill(690, W, H, 15)
    s += f'<rect x="60" y="560" width="300" height="190" rx="10" fill="#fff" {ST}/>'
    for x in (110, 160, 210, 260, 310):
        s += f'<path d="M{x},560 L{x},750" fill="none" {ST} stroke-width="3"/>'
    s += bird(120, 745, 0.5, 'happy') + bird(210, 745, 0.4, 'open') + bird(290, 745, 0.4, 'happy', flip=-1)
    s += csit(430, 730, 0.7, mood='silly', kind='neu')
    s += f'<path d="M540,660 Q620,595 730,650 L726,750 L550,750 Z" fill="#fff" {ST}/>'
    s += f'<path d="M580,650 Q588,700 580,745 M650,628 Q655,690 648,748 M705,645 Q712,700 704,748" fill="none" {ST} stroke-width="3"/>'
    s += cat_action(560, 450, 0.6, 'leap', 'smile')
    for x in range(30, 740, 62):
        s += f'<path d="M{x},120 l-9,30" fill="none" {ST} stroke-width="3"/>' if x < 300 or x > 700 else ''
    return s


def e17():
    s = hill(690, W, H, 15)
    s += f'<path d="M150,640 A225,225 0 0 1 600,640 Z" fill="#fff" {ST}/>'
    for i in range(-6, 7):
        ang = math.radians(270 + i * 13)
        s += f'<path d="M375,640 m{math.cos(ang) * 250:.0f},{math.sin(ang) * 250:.0f} l{math.cos(ang) * 34:.0f},{math.sin(ang) * 34:.0f}" {ST} stroke-width="4.4"/>'
    s += f'<path d="M-10,700 Q375,660 760,700 L760,790 L-10,790 Z" fill="#fff" {ST}/>'
    for i, x in enumerate(range(40, 720, 55)):
        s += sprout(x, 760 + (i % 3) * 6, 1.1) if i not in (3, 8) else f'<ellipse cx="{x}" cy="752" rx="20" ry="7" fill="#fff" {ST} stroke-width="3"/>'
    s += csit(120, 700, 0.55, mood='open') + csit(230, 700, 0.55, mood='open', kind='raspi') + csit(340, 700, 0.5, mood='silly', kind='neu')
    s += hera_sit(600, 710, 0.62, 'smile') + bubble(430, 190, 300, 90, 'Cada una|a su tiempo', 600, 500, 30)
    s += snail(480, 790, 0.6) + cloud(40, 70, 130)
    return s


def e18():
    s = sun(110, 100, 38) + cloud(540, 70, 150) + hill(705, W, H, 15)
    s += sign(270, 60, 210, 'EL JARDÍN|DE TODOS', 24)
    for x in (60, 150, 230, 520, 610, 690):
        s += sunflower(x, 600, 0.8, 170)
    for x in (110, 300, 450, 600, 680):
        s += daisy(x, 665, 0.9, 120)
    for x in (60, 190, 560, 700):
        s += lavender(x, 700, 0.85, 150)
    s += fence(10, 740, 600, 60)
    s += csit(210, 745, 0.4, mood='smile') + csit(290, 745, 0.4, mood='mischief', kind='raspi') + csit(370, 745, 0.4, mood='silly', kind='neu') + hera_sit(480, 750, 0.4, 'smile')
    s += sapling(620, 760, 0.6) + bee(330, 280, 0.8, -15) + bee(560, 300, 0.7, 20) + butterfly(440, 470, 0.5)
    return s


def e19():
    s = bunting(20, 730, 60, 50, 11) + banner(185, 120, 380, 80, 'EL JARDÍN DE TODOS', 30) + hill(710, W, H, 15)
    s += csit(210, 590, 0.5, mood='happy') + csit(310, 592, 0.5, mood='mischief', kind='raspi') + hera_sit(430, 600, 0.55, 'smile') + csit(560, 592, 0.5, mood='silly', kind='neu')
    s += f'<path d="M80,600 L670,600 L690,660 L60,660 Z" fill="#fff" {ST}/><path d="M110,660 L110,740 M640,660 L640,740" fill="none" {ST} stroke-width="8"/>'
    s += f'<circle cx="190" cy="626" r="20" fill="#fff" {ST}/><circle cx="480" cy="624" r="20" fill="#fff" {ST}/>'
    s += f'<path d="M280,640 Q300,570 340,570 Q380,570 400,640 Z" fill="#fff" {ST}/><path d="M310,600 L370,600" {ST} stroke-width="3"/>'
    s += ladybug(580, 625, 0.28) + butterfly(375, 330, 0.6)
    s += squirrel(80, 760, 0.62, 'happy') + rabbit(190, 765, 0.58, 'happy') + bird(560, 760, 0.8, 'happy', flip=-1) + bird(670, 762, 0.5, 'happy', flip=-1)
    return s


def e20():
    s = moon(610, 130, 75) + stars_night(NIGHT) + hill(690, W, H, 20)
    s += sapling(110, 735, 1.5)
    s += csit(260, 715, 0.62, mood='joy') + csit(370, 715, 0.62, mood='mischief', kind='raspi') + csit(480, 715, 0.62, mood='silly', kind='neu')
    s += hera_sit(630, 722, 0.7, 'sleep')
    s += firefly(180, 420) + firefly(300, 330) + firefly(560, 420) + firefly(690, 520) + heart(375, 250, 0.4)
    return s


SCENES = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e_compost, e14, e15, e16, e17, e18, e19, e20]

HIDDEN = {0: (620, 250), 1: (600, 250), 2: (640, 520), 3: (500, 240), 4: (60, 480), 5: (620, 330), 6: (300, 210), 7: (600, 300), 8: (440, 350), 9: (700, 430), 10: (80, 330), 11: (640, 220), 12: (600, 220), 14: (200, 560), 15: (700, 470), 16: (100, 420), 17: (650, 330), 18: (400, 380), 19: (620, 480), 20: (460, 330), 13: (600, 300)}

TEXTOS = [
    "Al final de la calle había un solar lleno de hierbas, piedras y latas viejas. Nadie lo quería. Lúa, que siempre encontraba lo bonito en todas partes, pensó: «Este sitio tiene ganas de ser otra cosa».",
    "Hera, la labradora color chocolate, era la mayor del grupo. Caminaba despacio, hablaba bajito y tenía una paciencia tan grande como su corazón. Los demás decían que era una santa.",
    "Raspi, la gata parda, no paraba quieta ni dormida. Su cabeza era un nido de ideas y de alguna que otra travesura. «¡Se me ha ocurrido algo!» era su frase favorita.",
    "Neu, la gata blanca, era la payasa del grupo. Rodaba por la hierba, hacía muecas y se caía a propósito. Con ella, hasta el día más aburrido sonaba a risa.",
    "«¿Y si hacemos aquí un jardín?», propuso Lúa. A Raspi le brillaron los ojos. Neu dio una voltereta. Hera sonrió despacito: «Los jardines se hacen entre todos».",
    "Quitaron piedras y hierbas y separaron la basura: el papel al contenedor azul, los envases al amarillo y el vidrio al verde. Las latas más bonitas no se tiraron: se convirtieron en macetas.",
    "Lúa quería que todo saliera perfecto, así que intentó hacerlo ella sola. Al caer la tarde estaba agotada. «Se me da bien casi todo», suspiró, «pero no puedo con todo».",
    "Hera abrió un saquito de semillas. Unas eran grandes como garbanzos. Otras, finas como polvo. Otras tenían alas. «Cada semilla es distinta. Unas brotan en días y otras tardan meses. Ninguna es mejor que otra».",
    "Cada uno eligió su semilla. Lúa hizo un hoyo con mucho cuidado. Raspi hizo seis, por si acaso. Neu regó con agua de lluvia, bailando, y mojó a todo el mundo. Hera las tapó una a una, con mimo.",
    "Pasó un día. Pasaron dos. Pasaron tres. La tierra seguía quieta y oscura. «¿Y si no crece nada?», se preguntaba Raspi, con los bigotes temblando.",
    "Raspi no aguantó más. Por la noche desenterró las semillas para ver si estaban creciendo. Cuando amaneció, el jardín parecía un campo de batalla.",
    "«¡Raspi, siempre igual!», gritó Lúa. Raspi agachó las orejas. «Siempre me echáis la culpa de todo», murmuró. Y en el jardín se hizo un silencio muy largo.",
    "Hera se sentó entre las dos. «Raspi, eso no estuvo bien, pero tú no eres «el travieso». Eres Raspi. Y tú, Lúa, sabes cuánto pinchan las etiquetas». Se pidieron perdón y volvieron a plantar juntas.",
    "Hera les enseñó otro secreto: «Las cáscaras y las hojas secas no son basura, son comida para la tierra». Hicieron un montón de compost y las lombrices se pusieron a trabajar.",
    "Esa noche el cielo se puso negro. Llegaron el viento y la lluvia, y el agua empezó a correr hacia las semillas.",
    "Hera se tumbó para frenar el agua con su cuerpo grande y tranquilo. Raspi, tan pequeño y tan listo, cavó una zanja por donde escapó el charco. ¡Su manía de cavar salvó el jardín!",
    "Neu contó chistes a Pipa y a los pajarillos asustados hasta que se rieron a carcajadas. Y Lúa, saltando más rápido que el viento, cubrió las semillas con una lona.",
    "Al amanecer salió el sol y la tierra se llenó de puntitos verdes. Algunas semillas ya asomaban. Otras, todavía no. «Cada una a su tiempo», dijo Hera.",
    "Pasaron las semanas. El solar se llenó de girasoles de Raspi, margaritas de Neu y lavanda de Lúa. Como no usaron venenos, llegaron las abejas y las mariposas. En un rincón creció el manzano de Hera, todavía pequeñito.",
    "Abrieron la puerta y llegaron todos: Nuez, Trébol, Mora, Mari, Pipa y su mamá. Ninguno era igual a otro. En el jardín de todos cabía todo el mundo.",
    "Esa noche, bajo el manzano, cada uno contó lo que había aprendido. Lúa, a pedir ayuda. Raspi, a esperar. Neu, que reír también es un trabajo importante. Y Hera: «Nunca es tarde para plantar algo bonito». Cada uno es distinto. Por eso el jardín es tan bonito.",
]
