# Las 13 escenas del cuento. Lienzo de cada escena: 750 x 700.
from lib import *

G = 590  # suelo en exteriores


def P(name, cx, g, r, **kw):
    """Personaje por nombre, con su decoracion propia, apoyado en el suelo g."""
    deco = {'Rita': 'stripes', 'Sol': 'dots', 'Mar': 'waves', 'Lola': 'star', 'Nano': 'zig', 'Teo': 'heart'}[name]
    kw.setdefault('deco', deco)
    return ball(cx, stand(r, g), r, **kw)


def e1():
    s = f'<path d="M-10,520 L760,520" {ST}/>'
    s += f'<rect x="520" y="50" width="190" height="150" rx="12" fill="#fff" {ST}/>'
    s += f'<path d="M615,50 L615,200 M520,125 L710,125" {ST}/>'
    s += sun(565, 90, 20, face=False) + cloud(640, 140, 55)
    # cajon de juguetes con la tapa abierta
    s += f'<path d="M205,360 L545,360 L600,235 L260,235 Z" fill="#fff" {ST}/>'
    s += f'<path d="M232,300 L575,300" {ST} stroke-width="3"/>'
    s += star(300, 330, 14) + f'<circle cx="470" cy="332" r="16" fill="#fff" {ST}/>'
    s += f'<rect x="190" y="360" width="370" height="200" rx="16" fill="#fff" {ST}/>'
    s += f'<path d="M190,420 L560,420" {ST}/>' + star(375, 490, 36) + star(280, 490, 18) + star(470, 490, 18)
    s += star(110, 170, 22) + star(430, 150, 16) + heart(95, 330, 0.5) + heart(660, 330, 0.5)
    r = 56
    for x, n, ar in ((90, 'Rita', ('up', 'down')), (235, 'Sol', ('down', 'up')), (375, 'Mar', ('up', 'up')),
                     (515, 'Lola', ('up', 'down')), (660, 'Nano', ('down', 'up'))):
        s += P(n, x, 665, r, mood='happy', arms=ar)
    return s


def e2():
    s = f'<path d="M-10,520 L760,520" {ST}/>'
    s += sun(90, 90, 36) + cloud(540, 50, 110)
    s += P('Mar', 660, 620, 52, mood='open', arms=('up', 'down'), look=-1)
    s += P('Sol', 540, 620, 52, mood='open', arms=('down', 'hip'), look=-1)
    s += P('Rita', 425, 620, 52, mood='neutral', arms=('cheek', 'down'), look=-1)
    # Teo sale de una caja
    s += ball(225, 320, 95, mood='smile', deco='heart', arms=((120, 395), (330, 395)), look=1, legs=False)
    s += f'<path d="M90,400 L360,400 L340,620 L110,620 Z" fill="#fff" {ST}/>'
    s += f'<path d="M90,400 L35,355 L110,345 L135,400 Z M360,400 L415,355 L340,345 L315,400 Z" fill="#fff" {ST}/>'
    s += f'<rect x="160" y="450" width="130" height="95" rx="8" fill="#fff" {ST}/>'
    s += f'<text x="225" y="490" {font(30, 700)} fill="#111">TEO</text><text x="225" y="522" {font(20, 600)} fill="#111">NUEVO</text>'
    s += star(330, 150, 22) + star(150, 160, 16) + heart(350, 235, 0.35)
    return s


def e3():
    s = hill(G)
    s += sun(660, 80, 34) + cloud(40, 60, 120)
    s += P('Teo', 105, G + 30, 80, mood='sad', arms=('down', 'down'), look=1)
    for x, n, ar in ((300, 'Rita', ('down', 'cheek')), (415, 'Sol', ('cheek', 'down')),
                     (530, 'Mar', ('down', 'cheek')), (645, 'Lola', ('cheek', 'down'))):
        s += P(n, x, G + 20, 50, mood='neutral', arms=ar, look=-1)
    s += bubble(270, 310, 190, 64, 'Es distinta...', 340, 430, 28)
    s += bubble(500, 290, 150, 64, '¿Y ese?', 560, 425, 28)
    s += flower(200, 640, 0.8) + grass(250, 675) + grass(600, 675)
    return s


def e4():
    s = hill(G)
    s += sun(80, 90, 34) + cloud(540, 40, 130)
    # cartel del club, apoyado en el suelo detras del grupo
    s += f'<path d="M455,290 L455,{G}" {ST} stroke-width="9"/>'
    s += f'<rect x="335" y="190" width="240" height="95" rx="14" fill="#fff" {ST}/>'
    s += f'<text x="455" y="233" {font(28, 700)} fill="#111">CLUB</text><text x="455" y="266" {font(26, 700)} fill="#111">ARCOÍRIS</text>'
    s += P('Teo', 100, G + 30, 66, mood='worried', arms=('up', 'down'), look=1)
    s += bubble(10, 290, 240, 64, '¿Puedo jugar?', 85, 400, 26)
    s += P('Rita', 310, G + 20, 62, mood='angry', arms=('out', 'hip'), look=-1)
    s += bubble(215, 360, 110, 62, '¡NO!', 270, 440, 34)
    s += P('Sol', 440, G + 20, 52, mood='sad', arms=('down', 'down'), look=-1)
    s += P('Mar', 555, G + 20, 52, mood='neutral', arms=('down', 'down'), look=-1)
    s += P('Lola', 665, G + 20, 52, mood='neutral', arms=('down', 'down'), look=-1)
    s += grass(380, 685) + grass(700, 685)
    return s


def e5():
    s = hill(G)
    s += tree(565, G + 30, 1.25)
    s += cloud(240, 110, 180)
    for dx in (270, 320, 370):
        s += f'<path d="M{dx},170 l-8,28" {ST} stroke-width="4"/>'
    s += P('Teo', 330, G + 40, 80, mood='sad', arms=('down', 'down'), look=-1, tear=True)
    s += bird(480, 640, 1.0)
    s += ball(70, 460, 24, mood='happy', arms=('up', 'up'))
    s += ball(135, 460, 24, mood='happy', arms=('up', 'up'))
    s += ball(200, 460, 24, mood='happy', arms=('up', 'up'))
    s += sun(80, 80, 32) + flower(690, 650, 0.8) + grass(150, 685)
    return s


def e6():
    s = hill(G)
    s += sun(670, 80, 32) + cloud(560, 190, 110)
    s += P('Sol', 230, G + 40, 92, mood='worried', arms=('down', 'cheek'), look=1)
    s += thought(100, 30, 340, 170, [(290, 230, 12), (322, 265, 17), (352, 305, 24)])
    s += f'<text x="270" y="140" {font(95, 700)} fill="#111">?</text>' + heart(185, 115, 0.55) + heart(365, 105, 0.4)
    s += tree(640, G, 0.65)
    s += P('Teo', 505, G, 40, mood='sad', arms=('down', 'down'), look=-1)
    s += flower(60, 640, 0.9) + grass(420, 685) + flower(710, 655, 0.7)
    return s


def e7():
    s = hill(G)
    s += sun(375, 85, 40) + cloud(40, 70, 120) + cloud(580, 90, 110)
    s += P('Sol', 225, G + 40, 88, mood='happy', arms=('up', (336, 500)), look=1)
    s += P('Teo', 525, G + 40, 88, mood='happy', arms=((414, 500), 'up'), look=-1)
    s += note(110, 270) + note(190, 200, 1.2) + note(560, 230) + note(650, 290, 1.2) + note(375, 270, 1.1)
    s += star(120, 380, 16) + star(640, 410, 16) + heart(375, 400, 0.4)
    s += flower(50, 655, 0.9) + flower(705, 655, 0.9) + grass(375, 690)
    return s


def e8():
    s = f'<path d="M-10,470 L760,470" {ST}/>'
    s += window_storm(50, 40, 270, 270)
    # Mar atascada debajo del sofa
    s += ball(575, 545, 36, mood='worried', deco='waves', arms=('up', 'up'), legs=False, look=-1)
    s += sofa(360, 330)
    s += bubble(470, 150, 210, 64, '¡Socorro!', 560, 300, 30)
    s += f'<rect x="400" y="40" width="0" height="0"/>'
    s += P('Rita', 100, 690, 56, mood='open', arms=('up', 'up'), look=1)
    s += P('Lola', 235, 690, 56, mood='open', arms=('up', 'up'), look=1)
    s += star(60, 400, 12) + star(330, 400, 12)
    return s


def e9():
    s = f'<path d="M-10,470 L760,470" {ST}/>'
    s += ball(575, 545, 36, mood='smile', deco='waves', arms=((470, 548), 'up'), legs=False, look=-1)
    s += sofa(360, 330)
    s += window_storm(50, 40, 270, 270)
    s += f'<rect x="440" y="60" width="220" height="150" rx="10" fill="#fff" {ST}/>' + heart(550, 135, 0.8)
    s += P('Teo', 290, 690, 72, mood='happy', arms=('up', (452, 548)), look=1)
    s += P('Sol', 85, 690, 50, mood='happy', arms=('up', 'up'), look=1)
    s += f'<path d="M160,540 l-40,6 M165,572 l-50,0 M170,604 l-40,-8" {ST} stroke-width="4"/>'
    s += star(360, 250, 14)
    return s


def e10():
    s = hill(G)
    s += sun(660, 80, 34) + cloud(50, 60, 130)
    for x in (80, 170, 580, 670):
        s += ball(x, 500, 28, mood='happy', arms=('up', 'up'))
    s += P('Mar', 285, G + 50, 84, mood='happy', arms=('up', (368, 560)))
    s += P('Teo', 465, G + 50, 84, mood='happy', arms=((382, 560), 'up'))
    s += heart(375, 330, 0.9) + heart(290, 250, 0.4) + heart(460, 250, 0.4)
    s += bubble(70, 330, 160, 60, '¡Gracias!', 200, 415, 28) + bubble(520, 330, 160, 60, '¡De nada!', 550, 415, 28)
    s += grass(120, 690) + grass(640, 690) + flower(55, 645, 0.8) + flower(705, 645, 0.8)
    return s


def e11():
    s = hill(G)
    s += sun(375, 70, 34) + cloud(40, 40, 120) + cloud(580, 50, 110)
    for x in (70, 160, 600, 690):
        s += ball(x, 495, 28, mood='smile', arms=('up', 'down'))
    s += P('Rita', 265, G + 50, 80, mood='sorry', arms=('chest', (368, 560)), look=1)
    s += P('Teo', 485, G + 50, 80, mood='happy', arms=((382, 560), 'down'), look=-1)
    s += bubble(95, 300, 220, 62, 'Perdóname', 215, 395, 30)
    s += heart(375, 400, 0.5)
    s += flower(50, 645, 0.8) + flower(715, 645, 0.8) + grass(380, 690)
    return s


def e12():
    s = hill(G + 30)
    s += rainbow(375, 500, 330)
    s += sun(95, 90, 36) + cloud(570, 40, 110)
    s += banner(190, 60, 370, 90, 'EL CLUB DE TODOS', 34)
    xs = [70, 190, 310, 430, 550, 670]
    names = ['Rita', 'Sol', 'Teo', 'Mar', 'Lola', 'Nano']
    r = 48
    cy = stand(r, 665)
    for i, (x, n) in enumerate(zip(xs, names)):
        left = 'up' if i == 0 else (x - 60, cy + 26)
        right = 'up' if i == 5 else (x + 60, cy + 26)
        s += P(n, x, 665, r, mood='happy', arms=(left, right))
    s += star(70, 330, 14) + star(690, 330, 14) + heart(375, 360, 0.45)
    return s


def e13():
    s = heart(375, 270, 5.0)
    s += outlined_text(375, 245, 'TODOS', 70) + outlined_text(375, 320, 'VALEMOS', 70)
    s += star(70, 80, 22) + star(690, 90, 22) + star(95, 420, 14) + star(655, 430, 14)
    xs = [75, 200, 325, 450, 575, 700]
    for x, n in zip(xs, ['Rita', 'Sol', 'Teo', 'Mar', 'Lola', 'Nano']):
        s += P(n, x, 690, 46, mood='happy', arms=('up', 'up'))
    return s


SCENES = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13]

TEXTOS = [
    ("En un cajón de juguetes vivían cinco pelotas muy amigas: Rita, la roja; Sol, la amarilla; Mar, la azul; Lola, la verde y Nano, el naranja. Cada una tenía su forma de ser y se querían tal como eran.",
     "¿Cuántas pelotas ves? ¿Cuál es tu color favorito?"),
    ("Una mañana llegó una caja nueva. De dentro salió Teo, una pelota negra con una sonrisa tímida. Estaba nervioso porque no conocía a nadie.",
     "¿Alguna vez has llegado a un sitio nuevo? ¿Cómo te sentiste?"),
    ("Las pelotas se miraron y empezaron a cuchichear: «Es distinta a nosotras». Teo lo oyó y sintió un nudo en la tripa.",
     "¿Cómo crees que se siente Teo? ¿Por qué?"),
    ("En el recreo, las pelotas jugaban al Club del Arcoíris. Teo se acercó y preguntó: «¿Puedo jugar?». Rita contestó: «No, tú no eres como nosotras».",
     "¿Es justo dejar fuera a alguien por ser distinto? ¿Qué le dirías a Rita?"),
    ("Teo se fue solo bajo un árbol y una lágrima le rodó por la mejilla. Un pajarito se posó a su lado y se quedó con él un ratito.",
     "¿Te has sentido solo alguna vez? ¿Qué te ayudó?"),
    ("Sol lo vio desde lejos y se quedó pensando: «¿Por qué hemos dejado fuera a Teo? No ha hecho nada malo». Algo en su corazón le decía que aquello no estaba bien.",
     "¿Qué crees que va a hacer Sol?"),
    ("Sol se acercó a Teo y charlaron un buen rato. Descubrieron que a los dos les encantaba cantar y saltar. ¡Tenían mucho más en común de lo que parecía!",
     "¿Qué cosas te gustan a ti que también les gustan a tus amigos?"),
    ("Esa tarde estalló una tormenta con truenos y relámpagos. Todas las pelotas salieron corriendo asustadas y Mar se quedó atascada debajo del sofá. «¡Socorro!».",
     "¿Qué harías tú si un amigo estuviera en apuros?"),
    ("Todas tenían miedo de acercarse, menos Teo. Se agachó, estiró el brazo y tiró de Mar con todas sus fuerzas hasta sacarla de allí.",
     "¿Qué valor demostró Teo?"),
    ("«Gracias, Teo», dijo Mar. «No lo hice para que me aceptarais», respondió él. «Lo hice porque eres una pelota como yo y necesitabas ayuda».",
     "¿Por qué crees que Teo ayudó a quien no lo había tratado bien?"),
    ("Rita bajó la mirada: «Perdóname, Teo. Me equivoqué. Pensé que ser diferente era un problema y no lo es». Teo sonrió y le dio la mano.",
     "¿Es fácil pedir perdón? ¿Y perdonar?"),
    ("Desde aquel día, el Club del Arcoíris se llama «El Club de Todos». Hay sitio para cada color, para cada forma de ser y para quien llegue nuevo.",
     "¿Cómo puedes hacer sitio a alguien nuevo en tu clase?"),
    ("Por fuera somos distintos y por dentro somos muy parecidos: todos reímos, todos tenemos miedo alguna vez y todos queremos tener amigos. Eso es lo que nos hace valiosos.",
     "Cuéntale a un adulto qué has aprendido con esta historia."),
]
