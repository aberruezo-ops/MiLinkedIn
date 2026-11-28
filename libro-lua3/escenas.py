# Libro 3: "Lúa y el vecino nuevo". Lienzo de cada escena: 750 x 780.
from erizo import *

W, H = 750, 780
NIGHT = [(90, 90, 18), (230, 190, 14), (380, 80, 16), (500, 210, 12), (680, 330, 14), (60, 330, 12), (300, 290, 12)]


def csit(cx, g, s=1.0, **kw):
    """Gata sentada apoyada en el suelo g."""
    return cat_sit(cx, g - 272 * s, s, **kw)


def stars_night(pts):
    return ''.join(star(x, y, r) if i % 2 == 0 else twinkle(x, y, r / 14) for i, (x, y, r) in enumerate(pts))


def tufts(pts):
    return ''.join(grass(x, y, k) for x, y, k in pts)


def falling(pts):
    return ''.join(leaf(x, y, 30, a) for x, y, a in pts)


def paw(x, y, k=1.0, ang=0):
    s = f'<g transform="translate({x},{y}) rotate({ang}) scale({k})"><ellipse cx="0" cy="8" rx="13" ry="10" fill="#fff" {ST} stroke-width="3"/>'
    for dx, dy in ((-16, -8), (-6, -17), (6, -17), (16, -8)):
        s += f'<ellipse cx="{dx}" cy="{dy}" rx="5" ry="6.5" fill="#fff" {ST} stroke-width="3"/>'
    return s + '</g>'


def sniff(x, y, k=1.0, side=1):
    """Ondas de olfato saliendo de un hocico."""
    s = ''
    for i in range(3):
        r = (18 + i * 16) * k
        s += f'<path d="M{x + side * r * .5:.0f},{y - r * .8:.0f} Q{x + side * r:.0f},{y:.0f} {x + side * r * .5:.0f},{y + r * .8:.0f}" fill="none" {ST} stroke-width="3"/>'
    return s


def motion(x, y, n=3, side=1, gap=22, ln=50):
    return ''.join(f'<path d="M{x},{y + i * gap} l{side * ln},0" fill="none" {ST} stroke-width="3.4"/>' for i in range(n))


def drum(x, y):
    """Corazon que late: corazon con rayitas."""
    s = heart(x, y, 0.36)
    for dx, dy, ex, ey in ((-38, -10, -54, -16), (38, -10, 54, -16), (-34, 18, -50, 26), (34, 18, 50, 26)):
        s += f'<path d="M{x + dx},{y + dy} L{x + ex},{y + ey}" fill="none" {ST} stroke-width="3.4"/>'
    return s


def cushion(x, g, w=220):
    return f'<path d="M{x - w / 2},{g} Q{x - w / 2 - 10},{g - 50} {x},{g - 46} Q{x + w / 2 + 10},{g - 50} {x + w / 2},{g} Z" fill="#fff" {ST}/>'


def window_night(x, y, w, h):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#fff" {ST}/>'
    s += f'<path d="M{x + w / 2},{y} L{x + w / 2},{y + h} M{x},{y + h / 2} L{x + w},{y + h / 2}" fill="none" {ST} stroke-width="4"/>'
    s += moon(x + w * .74, y + h * .26, 26) + star(x + w * .25, y + h * .25, 10) + star(x + w * .3, y + h * .75, 8) + twinkle(x + w * .75, y + h * .74, .7)
    return s


# --------------------------------------------------------------------- escenas
def e1():
    s = sun(90, 95, 38) + cloud(300, 60, 140) + hill(705, W, H, 15)
    s += hedge(330, 760, 705, 150)
    s += leaf_house(560, 712, 1.0)
    s += csit(190, 712, 0.95, mood='open', look=1)
    s += falling([(250, 230, 20), (470, 260, -40), (640, 220, 60), (110, 330, -10), (400, 380, 35)])
    s += leaf_pile(700, 760, 0.6) + tufts([(60, 760, 1.4), (360, 760, 1.3)])
    return s


def e2():
    s = sun(660, 85, 34) + cloud(60, 60, 140) + hill(705, W, H, 15)
    s += hedge(300, 760, 705, 150) + leaf_house(560, 712, 1.1, door=True)
    # alguien asoma en la puerta: nariz y ojitos
    s += f'<path d="M532,712 Q534,660 560,652 Q588,660 590,712 Z" fill="#fff" {ST}/>'
    s += f'<circle cx="549" cy="676" r="5" fill="#111"/><circle cx="571" cy="676" r="5" fill="#111"/><ellipse cx="560" cy="694" rx="8" ry="6" fill="#111"/>'
    for a in range(200, 345, 18):
        r = math.radians(a)
        s += f'<path d="M{560 + math.cos(r) * 34:.0f},{690 + math.sin(r) * 40:.0f} L{560 + math.cos(r) * 50:.0f},{690 + math.sin(r) * 58:.0f}" fill="none" {ST} stroke-width="3.4"/>'
    s += cat_action(230, 690, 0.7, 'run', 'worried', flip=-1, kind='raspi')
    s += motion(330, 520, 3, 1, 26, 70)
    s += f'<text x="440" y="420" {font(70, 700)} fill="#111">!</text>'
    s += tufts([(80, 760, 1.4), (420, 765, 1.3)])
    return s


def e3():
    s = sun(90, 85, 34) + cloud(520, 50, 150) + hill(705, W, H, 15)
    s += csit(140, 712, 0.8, mood='angry', kind='raspi', tail='up')
    s += bubble(30, 120, 330, 96, '¡Es un|monstruo!', 170, 330, 36)
    s += csit(630, 712, 0.55, mood='worried', kind='neu', look=-1)
    s += hera_sit(530, 718, 0.85, 'open')
    s += csit(330, 712, 0.62, mood='worried')
    s += drum(330, 330)
    s += tufts([(250, 765, 1.3), (700, 765, 1.2)])
    return s


def e4():
    s = hill(705, W, H, 15) + cloud(40, 40, 110)
    s += csit(110, 712, 0.5, mood='mischief', kind='raspi', look=1)
    s += csit(300, 712, 0.5, mood='worried', kind='neu', look=1)
    s += csit(490, 712, 0.5, mood='worried', look=1)
    # el monstruo crece en cada bocadillo
    s += thought(120, 360, 150, 120, [(120, 500, 9), (110, 525, 6)]) + monster(195, 420, 0.32)
    s += thought(260, 230, 220, 180, [(300, 430, 11), (300, 460, 7)]) + monster(370, 320, 0.55)
    s += thought(420, 20, 320, 300, [(500, 360, 14), (490, 400, 9)]) + monster(580, 170, 0.95)
    s += tufts([(660, 765, 1.4), (200, 770, 1.2)])
    return s


def e5():
    s = window_night(470, 60, 230, 200) + hill(705, W, H, 0)
    s += f'<path d="M0,705 L750,705" fill="none" {ST}/>'
    s += cushion(280, 712, 330)
    s += csit(280, 690, 0.85, mood='worried', tail='down')
    s += thought(30, 40, 360, 230, [(260, 300, 14), (280, 335, 9)])
    s += csit(110, 250, 0.3, mood='sad', tear=True) + csit(250, 250, 0.26, mood='happy', kind='raspi') + csit(320, 250, 0.26, mood='happy', kind='neu')
    s += f'<path d="M180,140 L180,250" fill="none" {ST} stroke-width="4" stroke-dasharray="2 12"/>'
    s += yarn_ball(620, 735, 26)
    return s


def yarn_ball(x, g, r):
    y = g - r
    s = f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" {ST}/>'
    s += f'<path d="M{x - r * .8:.0f},{y - r * .3:.0f} Q{x},{y - r * .9:.0f} {x + r * .8:.0f},{y - r * .2:.0f} M{x - r * .9:.0f},{y + r * .2:.0f} Q{x},{y - r * .5:.0f} {x + r * .9:.0f},{y + r * .3:.0f}" fill="none" {ST} stroke-width="3"/>'
    return s


def e6():
    s = sun(660, 85, 34) + cloud(40, 50, 150) + hill(705, W, H, 15) + tree(650, 720, 0.9)
    s += hera_sit(420, 718, 1.0, 'smile')
    s += csit(160, 712, 0.75, mood='worried', look=1)
    s += bubble(250, 110, 360, 100, 'Para eso están|las preguntas', 420, 370, 32)
    s += f'<text x="140" y="300" {font(64, 700)} fill="#111">?</text><text x="200" y="250" {font(44, 700)} fill="#111">?</text>'
    s += tufts([(60, 765, 1.3), (300, 765, 1.3)])
    return s


def e7():
    s = sun(90, 85, 34) + hill(705, W, H, 15)
    s += hedge(350, 760, 705, 150) + leaf_house(600, 712, 1.0)
    s += tilo_ball(460, 715, 0.75)
    s += csit(220, 712, 0.8, mood='worried', look=1)
    for i, (px, py) in enumerate(((30, 770), (70, 745), (110, 770))):
        s += paw(px, py, 0.7, 80)
    s += bubble(250, 150, 170, 80, 'Hola', 260, 440, 36)
    s += drum(120, 380)
    s += tufts([(380, 770, 1.2)])
    return s


def e8():
    s = sun(660, 80, 32) + cloud(30, 40, 130) + hill(705, W, H, 15)
    s += hedge(420, 760, 705, 150)
    s += tilo_ball(500, 715, 0.95, peek=True)
    s += csit(220, 712, 0.95, mood='open', look=1)
    s += bubble(300, 160, 420, 110, 'Un poco. Sois muchos|y yo soy nuevo', 500, 520, 30)
    s += tufts([(60, 765, 1.3), (360, 770, 1.2)])
    return s


def e9():
    s = sun(90, 80, 32) + hill(705, W, H, 15) + hedge(530, 760, 705, 130)
    s += tilo(470, 712, 0.95, 'sad')
    s += csit(160, 712, 0.75, mood='open', look=1)
    s += thought(270, 30, 450, 260, [(420, 310, 14), (440, 345, 9)])
    s += road(320, 150, 350, 60) + car(430, 210, 0.7)
    s += flower(330, 115, 0.5) + flower(640, 112, 0.5) + tufts([(380, 135, .8), (580, 130, .8)])
    s += tufts([(320, 765, 1.3)])
    return s


def e10():
    s = sun(670, 80, 32) + hill(705, W, H, 15)
    s += csit(130, 712, 0.72, mood='mischief', kind='raspi')
    s += bubble(20, 120, 280, 90, 'Hola, Pincho', 140, 440, 32)
    s += tilo(450, 712, 0.85, 'sad', look=-1)
    s += bubble(330, 140, 300, 90, 'Me llamo Tilo', 450, 470, 30)
    s += csit(615, 712, 0.48, mood='worried') + csit(705, 712, 0.38, mood='worried', kind='neu')
    s += tufts([(240, 770, 1.2), (720, 770, 1.2)])
    return s


def e11():
    s = sun(660, 80, 32) + cloud(30, 40, 130) + hill(705, W, H, 15)
    s += csit(210, 712, 0.95, mood='silly', kind='neu', tail='up')
    s += star(80, 300, 16) + star(330, 260, 13) + star(110, 420, 10)
    s += tilo(530, 712, 0.95, 'joy')
    for x, y, a in ((390, 420, -30), (400, 520, 0), (680, 420, 30), (670, 520, 0)):
        s += f'<path d="M{x},{y} l{20 if x > 500 else -20},{-10 if a else 0}" fill="none" {ST} stroke-width="3.4"/>'
    s += f'<text x="470" y="300" {font(36, 700)} fill="#111">ji, ji</text><text x="620" y="250" {font(30, 700)} fill="#111">ja, ja</text>'
    s += tufts([(380, 770, 1.2), (60, 770, 1.3)])
    return s


def e12():
    s = sun(90, 80, 32) + cloud(520, 50, 150) + hill(705, W, H, 15)
    s += hera_sit(220, 718, 0.95, 'smile')
    s += bowl(405, 735, 1.3, water=False) + f'<text x="405" y="768" {font(20, 700)} fill="#111">LECHE</text>'
    s += tilo(590, 712, 0.75, 'open')
    s += bubble(400, 170, 330, 100, 'Mejor agua,|gracias', 590, 500, 32)
    s += tufts([(60, 770, 1.3), (700, 770, 1.2)])
    return s


def e13():
    # mitad dia, mitad noche
    s = f'<path d="M375,0 Q345,200 385,400 Q420,600 375,800" fill="none" {ST} stroke-dasharray="4 14"/>'
    s += sun(110, 100, 36) + moon(630, 110, 60) + star(500, 80, 12) + twinkle(700, 230, .8) + star(560, 260, 10)
    s += hill(705, W, H, 15)
    s += cat_action(200, 450, 0.5, 'leap', 'joy')
    s += csit(240, 712, 0.5, mood='happy', kind='neu') + csit(110, 712, 0.5, mood='happy', kind='raspi')
    s += tilo(560, 712, 0.85, 'smile', look=1)
    s += sniff(600, 600, 1.0, 1)
    s += f'<text x="190" y="290" {font(30, 700)} fill="#111">DÍA</text><text x="570" y="370" {font(30, 700)} fill="#111">NOCHE</text>'
    return s


def e14():
    s = sun(660, 80, 32) + cloud(30, 50, 130) + hill(705, W, H, 15)
    s += csit(180, 712, 0.85, mood='angry', kind='raspi', tail='down', look=-1)
    s += bubble(30, 110, 330, 100, 'Los pinchos son|para pinchar', 170, 440, 30)
    s += motion(290, 560, 3, -1, 22, 40)
    s += tilo(540, 712, 0.75, 'sad', look=-1)
    s += hedge(600, 760, 705, 110) + flower(410, 760, 0.6)
    s += tufts([(330, 770, 1.2)])
    return s


def e15():
    s = f'<path d="M80,705 A100,100 0 0 1 280,705 Z" fill="#fff" {ST}/>'
    for i in range(-5, 6):
        ang = math.radians(270 + i * 15)
        s += f'<path d="M180,705 m{math.cos(ang) * 122:.0f},{math.sin(ang) * 122:.0f} l{math.cos(ang) * 24:.0f},{math.sin(ang) * 24:.0f}" {ST} stroke-width="4"/>'
    s += hill(705, W, H, 10)
    s += brambles(430, 760, 712, 380)
    s += cat_action(330, 640, 0.55, 'leap', 'joy', kind='raspi')
    s += butterfly(560, 260, 0.7)
    s += cloud(40, 60, 130)
    return s


def e16():
    s = moon(110, 110, 50) + star(260, 70, 12) + twinkle(330, 160, .8) + hill(705, W, H, 10)
    s += brambles(420, 760, 712, 420, seed=5)
    s += csit(95, 712, 0.58, mood='open', look=1) + hera_sit(240, 718, 0.6, 'open') + csit(375, 712, 0.45, mood='worried', kind='neu', look=1)
    s += bubble(70, 220, 280, 90, '¡Raspi! ¡Raspi!', 200, 480, 32)
    s += f'<circle cx="610" cy="560" r="7" fill="#111"/><circle cx="634" cy="560" r="7" fill="#111"/>'
    s += f'<text x="620" y="520" {font(40, 700)} fill="#111">?</text>'
    return s


def e17():
    s = stars_night(NIGHT) + moon(620, 100, 55) + hill(705, W, H, 10)
    s += brambles(-20, 300, 712, 420, seed=8) + brambles(450, 770, 712, 420, seed=9)
    s += tilo(380, 712, 0.95, 'smile', look=1)
    s += sniff(390, 610, 1.1, 1)
    for i, x in enumerate(range(480, 700, 45)):
        s += paw(x, 752 - (i % 2) * 14, 0.5, 90)
    s += bubble(250, 220, 260, 90, 'Yo puedo', 380, 470, 36)
    return s


def e18():
    s = stars_night(NIGHT[:4]) + moon(630, 100, 55) + hill(705, W, H, 10)
    s += brambles(590, 800, 712, 360, seed=4)
    s += tilo(495, 712, 0.55, 'happy', flip=-1)
    s += csit(345, 712, 0.55, mood='joy', kind='raspi')
    s += csit(75, 712, 0.5, mood='joy') + hera_sit(205, 718, 0.52, 'smile')
    s += csit(650, 712, 0.42, mood='joy', kind='neu')
    s += heart(260, 300, 0.4) + heart(380, 250, 0.3) + heart(150, 240, 0.28)
    return s


def e19():
    s = sun(90, 80, 32) + cloud(500, 40, 150) + hill(705, W, H, 15)
    s += csit(240, 712, 0.85, mood='sad', kind='raspi', tail='down', look=1)
    s += tilo(520, 712, 0.85, 'smile', look=-1)
    s += bubble(30, 120, 340, 100, 'Perdona por|llamarte Pincho', 260, 380, 30)
    s += bubble(400, 150, 330, 100, 'Yo también tenía|miedo de los gatos', 520, 480, 28)
    s += heart(375, 380, 0.36)
    s += tufts([(80, 770, 1.3), (690, 770, 1.3)])
    return s


def e20():
    s = sun(660, 80, 32) + cloud(40, 40, 140) + hill(600, W, H, 0)
    s += fence_hole(10, 740, 600, 300, 120)
    s += sign(60, 250, 230, 'PASO DE|ERIZOS', 26) + f'<path d="M175,356 L175,480" fill="none" {ST} stroke-width="8"/>'
    s += tilo(410, 655, 0.42, 'happy', look=1)
    s += bowl(300, 752, 0.8) + leaf_pile(480, 762, 0.7)
    s += csit(70, 760, 0.42, mood='happy') + hera_sit(170, 765, 0.38, 'smile')
    s += csit(590, 760, 0.4, mood='happy', kind='raspi') + csit(690, 762, 0.36, mood='silly', kind='neu')
    return s


def e21():
    s = stars_night(NIGHT) + moon(620, 110, 60) + hill(690, W, H, 20)
    s += tilo(375, 712, 0.58, 'smile')
    s += sniff(385, 650, .9, 1) + sniff(365, 650, .9, -1)
    s += csit(85, 712, 0.5, mood='joy') + csit(200, 712, 0.46, mood='happy', kind='raspi')
    s += csit(520, 712, 0.46, mood='silly', kind='neu') + hera_sit(665, 720, 0.5, 'smile')
    s += cloud(60, 250, 110) + heart(375, 400, 0.36)
    return s


SCENES = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21]

# Chispa, la luciernaga escondida (indice de escena: x, y)
HIDDEN = {0: (680, 330), 1: (90, 330), 2: (420, 260), 3: (60, 250), 4: (420, 460), 5: (690, 450), 6: (700, 290), 7: (90, 300),
          8: (80, 440), 9: (700, 300), 10: (60, 560), 11: (80, 400), 12: (330, 160), 13: (90, 420), 14: (700, 140), 15: (690, 120),
          16: (80, 580), 17: (80, 380), 18: (690, 340), 19: (690, 250), 20: (690, 300)}

TEXTOS = [
    "Una mañana de otoño, el jardín de todos amaneció con una sorpresa: bajo el seto había una casita nueva, hecha de hojas secas y ramitas. ¿Quién viviría allí?",
    "Raspi fue la primera en asomarse. Vio una nariz negra, dos ojitos brillantes y un montón de pinchos. Salió corriendo con la cola tiesa como un plumero.",
    "«¡Es un monstruo!», gritó Raspi. «Tiene mil pinchos, sale de noche y seguro que muerde». Neu se escondió detrás de Hera. Hasta Lúa sintió un nudo en la barriga.",
    "Cada vez que alguien contaba la historia, el monstruo crecía un poco más. Ya tenía colmillos. Ya era enorme. Ya comía gatos. Pero nadie lo había visto de verdad.",
    "Esa noche Lúa no podía dormir. Se acordó de cuando nadie la dejaba jugar por ser gris. «Yo también fui la distinta», pensó. «Y no me gustó nada».",
    "Por la mañana fue a ver a Hera. «Me da miedo el vecino nuevo», le contó. Hera la miró con calma: «Lo que no conocemos nos asusta. Para eso están las preguntas».",
    "Lúa se acercó a la casita paso a paso, con el corazón sonando como un tambor. «Hola», dijo bajito. Y el montón de pinchos se hizo una bola.",
    "«¿Tienes miedo?», preguntó Lúa. De la bola salió una vocecita: «Un poco. Sois muchos y yo soy nuevo». Lúa se quedó quieta. ¡El monstruo tenía miedo de ellos!",
    "Poco a poco, la bola se abrió. «Me llamo Tilo y soy un erizo», dijo. «Vivía en un prado, pero hicieron una carretera y tuve que buscar otra casa».",
    "Lúa fue a buscar a los demás. Raspi llegó con las orejas hacia atrás. «Hola, Pincho», soltó. Tilo bajó la nariz. «Me llamo Tilo», dijo muy bajito.",
    "Entonces Neu dio una voltereta, se cayó de culo y puso su cara más tonta. Tilo soltó una risita. Luego otra. Al final se reía tanto que le bailaban todos los pinchos.",
    "Hera le ofreció un cuenco de leche. «Gracias, pero la leche me sienta fatal», dijo Tilo. «Mejor agua». Hera sonrió: «¿Lo veis? Preguntando se aprende».",
    "Tilo era distinto en muchas cosas. Dormía de día y salía de noche. No sabía trepar ni saltar. Pero veía con la nariz: olía cosas que nadie más notaba.",
    "Raspi seguía sin fiarse. «Los pinchos son para pinchar», refunfuñaba. Y cada vez que Tilo pasaba cerca, ella se iba al otro lado del jardín.",
    "Una tarde, Raspi persiguió una mariposa hasta las zarzas del fondo. Se metió tan dentro que no sabía salir. Y el sol empezó a esconderse.",
    "«¡Raspi! ¡Raspi!», llamaban todos. Pero entre las zarzas no se veía nada, y las espinas pinchaban tanto que nadie se atrevía a entrar.",
    "Entonces Tilo dijo: «Yo puedo». Con su abrigo de pinchos, las espinas no le hacían daño. Y con su nariz siguió el rastro de Raspi en la oscuridad.",
    "Tilo guió a Raspi paso a paso hasta la salida. Cuando la vieron aparecer, todos se abrazaron. Bueno, todos menos Tilo, que es difícil de abrazar.",
    "Raspi se acercó a Tilo con las orejas gachas. «Perdona por llamarte Pincho. Y por lo del monstruo». Tilo sonrió: «Yo también tenía miedo de los gatos».",
    "Entre todos hicieron un agujero en la valla para que Tilo pudiera ir y venir, pusieron un plato de agua y juntaron un montón de hojas para su invierno.",
    "Esa noche, bajo las estrellas, Tilo les enseñó a oler la lluvia antes de que llegue. Lúa pensó que lo diferente asusta hasta que lo conoces. El monstruo del seto se llamaba Tilo. Y era su amigo.",
]
