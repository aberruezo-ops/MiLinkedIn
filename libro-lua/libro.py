# Genera interior.html y portada.html (cubierta completa KDP) de "Lua, la gatita gris".
import os
from lib import *
import animales as A
from animales import *
from jardin import bee, snail, tin_can, rocks, sprout, leaf
from escenas import SCENES, TEXTOS, HIDDEN
from pasatiempos import build as build_pasatiempos

# ---- datos editables ---------------------------------------------------
TITULO = 'Lúa, la gatita gris'
SUBTITULO = 'Un cuento para colorear sobre ser como eres'
VOLUMEN = 'Volumen I'
AUTOR = 'Alex Berruezo'
ANIO = '2026'
PAGINAS_TOTAL = 76            # debe coincidir con el interior generado
GROSOR_PAPEL = 0.002252       # pulgadas por pagina, papel blanco KDP (verificar con la calculadora de KDP)
# -------------------------------------------------------------------------

AQUI = os.path.dirname(os.path.abspath(__file__))

CSS = """
@font-face{font-family:'Fraunces';font-weight:400;src:url('fonts/fraunces-latin-400-normal.woff2')}
@font-face{font-family:'Fraunces';font-weight:600;src:url('fonts/fraunces-latin-600-normal.woff2')}
@font-face{font-family:'Fraunces';font-weight:700;src:url('fonts/fraunces-latin-700-normal.woff2')}
@font-face{font-family:'Fraunces';font-weight:600;font-style:italic;src:url('fonts/fraunces-latin-600-italic.woff2')}
@font-face{font-family:'Fredoka';font-weight:600;src:url('fonts/fredoka-latin-600-normal.woff2')}
@font-face{font-family:'Fredoka';font-weight:700;src:url('fonts/fredoka-latin-700-normal.woff2')}
@font-face{font-family:'Nunito';font-weight:400;src:url('fonts/nunito-latin-400-normal.woff2')}
@font-face{font-family:'Nunito';font-weight:700;src:url('fonts/nunito-latin-700-normal.woff2')}
@page{size:8.5in 11in;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#fff;color:#111;font-family:'Nunito',sans-serif}
.page{width:8.5in;height:11in;padding:.4in;position:relative;overflow:hidden;page-break-after:always;break-after:page}
.art svg{display:block;margin:0 auto}
.txt{margin-top:.08in;text-align:center;padding:0 .15in}
.txt p{margin:0;font-family:'Fraunces',serif;font-weight:600;font-size:16.5pt;line-height:1.38}
h1,h2,h3{font-family:'Fraunces',serif;font-weight:700;margin:0}
.note h2{font-size:27pt;margin-bottom:.18in}
.note h3{font-size:17pt;margin:.18in 0 .05in}
.note p,.note li{font-size:13.5pt;line-height:1.42;margin:.05in 0}
.note ul,.note ol{margin:.04in 0;padding-left:.28in}
.note .legal{position:absolute;left:.5in;right:.5in;bottom:.5in;font-size:9.5pt;line-height:1.4;border-top:2px solid #111;padding-top:.1in}
.center{text-align:center}
.line{border-bottom:3px solid #111;height:.5in;margin:.05in 0}
"""


SVGW = 7.1


def svg(inner, vb, marco=False, wi=None):
    w, h = [float(v) for v in vb.split()[2:]]
    ww = wi or SVGW
    if marco:
        r = f'x="8" y="8" width="{w - 16:.0f}" height="{h - 16:.0f}" rx="28"'
        inner = (f'<defs><clipPath id="c"><rect {r}/></clipPath>'
                 f'<filter id="w" x="-2%" y="-2%" width="104%" height="104%"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="7" result="n"/>'
                 f'<feDisplacementMap in="SourceGraphic" in2="n" scale="3.2"/></filter></defs>'
                 f'<g clip-path="url(#c)"><g filter="url(#w)">{inner}</g></g>'
                 f'<rect {r} fill="none" stroke="#111" stroke-width="4.2"/>')
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" style="width:{ww}in;height:{ww * h / w:.3f}in">{inner}</svg>'


def pag(html, cls=''):
    return f'<section class="page {cls}">{html}</section>'


BLANCO = pag('')
PAW = ('<svg viewBox="0 0 60 50" style="height:.28in;display:block;margin:0 auto .02in"><g fill="#fff" stroke="#111" stroke-width="3">'
       '<ellipse cx="30" cy="34" rx="14" ry="11"/><ellipse cx="12" cy="20" rx="6" ry="8"/><ellipse cx="25" cy="10" rx="6" ry="8"/>'
       '<ellipse cx="38" cy="10" rx="6" ry="8"/><ellipse cx="50" cy="20" rx="6" ry="8"/></g></svg>')


def pagina_titulo():
    s = sun(90, 95, 38) + cloud(550, 40, 140) + cloud(250, 120, 100) + hill(620, 750, 720, 18)
    s += cat_sit(375, 340, 1.2, 'happy')
    s += butterfly(580, 400, 0.6) + butterfly(160, 470, 0.5, flip=-1)
    s += flower(90, 650, 1.0) + flower(190, 680, 0.9) + flower(560, 665, 1.0) + flower(660, 640, 0.9) + grass(300, 700) + grass(470, 705)
    return pag(f'''
<div class="center" style="margin-top:.05in">
  <p style="margin:0 0 .04in;font-family:Fraunces;font-weight:700;font-size:15pt;letter-spacing:.18em;text-transform:uppercase">{VOLUMEN} de la serie Lúa</p>
  <h1 style="font-size:55pt;line-height:1.05;-webkit-text-stroke:2px #111;color:#fff">Lúa,<br>la gatita gris</h1>
  <p style="font-family:Fraunces;font-weight:600;font-style:italic;font-size:16pt;margin:.14in 0 0">{SUBTITULO}</p>
</div>
<div class="art" style="margin-top:.1in">{svg(s, '0 0 750 720')}</div>
<p class="center" style="position:absolute;bottom:.45in;left:0;right:0;font-family:Fraunces;font-weight:600;font-size:14pt">Texto e ilustraciones: {AUTOR}</p>''')


def pagina_guia1():
    return pag(f'''<div class="note">
<h2>Para las familias</h2>
<p>Casi todos los niños viven alguna vez lo que le pasa a Lúa: sentirse dejados fuera por ser distintos. Hablar de ello directamente suele costar. Mientras colorean y escuchan un cuento, les resulta más fácil contarte lo que sienten sin tener que mirarte a los ojos.</p>
<h3>Qué hay detrás de la historia</h3>
<ul>
<li><b>Poco texto.</b> El niño completa la historia con sus palabras, y lo que dice te da pistas de cómo se siente.</li>
<li><b>La tristeza se acompaña, no se arregla.</b> Lúa está triste y nadie le dice que no llore. Poner nombre a lo que sentimos es el primer paso para calmarnos.</li>
<li><b>Se vale por ser, no por servir.</b> Lúa no gana su sitio por ayudar: ya valía antes. Su gris tiene ventajas de noche, pero la historia deja claro que valía igual antes de descubrirlas. Los niños necesitan saber que se les quiere sin condiciones.</li>
<li><b>Defenderse no es pelear.</b> Lúa enseña las uñas y el zorro se va, sin que nadie salga herido. Poner un límite con firmeza no es ser agresivo, y es una buena frase para repetir en casa.</li>\n<li><b>Hay un adulto seguro.</b> La escena de mamá está ahí a propósito: un niño aguanta mucho mejor un mal día si sabe que tiene a quién volver.</li>
<li><b>Hay reparación.</b> Los amigos se equivocan, piden perdón y todo se arregla. Así aprenden que un error no acaba con una amistad.</li>
</ul>
<h3>Cómo usarlo, con 5 minutos al día</h3>
<ol>
<li>Mirad el dibujo y preguntad: ¿qué crees que siente? Escuchad sin corregir.</li>
<li>Dejad que coloreen como quieran. Lúa puede ser gris, rosa o de rayas.</li>
<li>Terminad con la página "Respira con Lúa". Cerrar en calma ayuda a irse a dormir mejor.</li>
</ol>
<p>En cada escena se esconde Mora, la mariquita. Buscarla invita a mirar con atención y a releer. Al final hay 20 páginas de pasatiempos para hacer solos o en familia. Van impresas por las dos caras: usad lápices o rotuladores finos.</p>
</div>''')


def pagina_guia2():
    return pag(f'''<div class="note">
<h2>Frases que ayudan</h2>
<h3>Si tu hijo o hija cuenta que lo han dejado fuera</h3>
<ul>
<li>"Debe doler. Cuéntame más." Funciona mejor que "no pasa nada" o "ignóralos", que sin querer le dicen que su emoción sobra.</li>
<li>"¿Qué necesitas ahora de mí?" A veces es un abrazo y a veces, solo que escuches.</li>
<li>Evita "algo habrás hecho". Primero acompaña y luego, si hace falta, buscad soluciones juntos.</li>
</ul>
<h3>Si es tu hijo o hija quien deja fuera a otros</h3>
<ul>
<li>Mantén la calma y sin etiquetas: "A veces nos equivocamos. ¿Cómo crees que se sintió? ¿Cómo lo podemos arreglar?"</li>
<li>Recuerda que Lúa no hizo nada para merecer el rechazo, y que sus amigos también aprendieron. Se puede cambiar.</li>
</ul>
<h3>Para el día a día</h3>
<ul>
<li>"Eres importante para mí tal como eres."</li>
<li>"Todas las emociones están bien. Lo que hacemos con ellas, a veces hay que mejorarlo."</li>
<li>"Ser diferente no es un defecto. Es lo que te hace tú."</li>
</ul>
<h3>Cuándo buscar ayuda</h3>
<p>Este libro es un apoyo para conversar en casa, no un tratamiento. Si tu hijo lleva semanas triste o muy retraído, no quiere ir al colegio, o sufre burlas o agresiones repetidas, habla con su tutor o tutora y con su pediatra o un psicólogo infantil.</p>
<div class="legal">© {ANIO} {AUTOR}. Todos los derechos reservados. Prohibida la reproducción total o parcial de esta obra sin permiso del autor. Primera edición. {VOLUMEN} de la serie «Lúa».</div>
</div>''')


def pagina_personajes():
    s = f'<text x="375" y="60" {font(46, 700)} fill="#111">Conoce a los amigos</text>'
    s += cat_sit(105, 150, 0.62, 'happy') + squirrel(395, 330, 0.78, 'happy') + rabbit(625, 332, 0.8, 'happy')
    s += ladybug(125, 545, 0.95) + butterfly(375, 535, 1.05) + bird(625, 640, 1.1, 'happy')
    nombres = [('Lúa', 'la gatita gris', 125, 365), ('Nuez', 'la ardilla', 375, 365), ('Trébol', 'la conejita', 625, 365),
               ('Mora', 'la mariquita', 125, 655), ('Mari', 'la mariposa', 375, 655), ('Pipa', 'el pajarito', 625, 680)]
    for n, d, x, y in nombres:
        s += f'<text x="{x}" y="{y}" {font(36, 700)} fill="#111">{n}</text><text x="{x}" y="{y + 30}" {font(22, 600)} fill="#111">{d}</text>'
    return pag(f'<div class="art">{svg(s, "0 0 750 720")}</div>'
               f'<div class="txt"><p style="font-size:17pt">Pinta a cada amigo como quieras. Mora se esconde en cada escena: ¡búscala!</p></div>')


def pagina_escena(i):
    mora = ladybug(*HIDDEN[i], 0.3) if i in HIDDEN else ''
    return pag(f'<div class="art">{svg(SCENES[i]() + mora, "0 0 750 780", marco=True)}</div><div class="txt">{PAW}<p>{TEXTOS[i]}</p></div>')


def pagina_emociones():
    s = f'<text x="375" y="55" {font(40, 700)} fill="#111">¿Cómo se siente Lúa?</text>'
    datos = [('joy', 'Alegría'), ('sad', 'Tristeza'), ('worried', 'Miedo'), ('angry', 'Enfado'), ('open', 'Sorpresa'), ('smile', 'Calma')]
    for i, (m, nom) in enumerate(datos):
        x, y = 125 + (i % 3) * 250, 210 + (i // 3) * 290
        s += f'<g transform="translate({x},{y}) scale(0.8)">{cat_head(0.8, m, 0, m == "sad")}</g>'
        s += f'<text x="{x}" y="{y + 120}" {font(32, 700)} fill="#111">{nom}</text>'
    return pag(f'<div class="art">{svg(s, "0 0 750 700")}</div>'
               f'<div class="txt"><p style="font-size:17pt">Colorea cada cara y cuenta cuándo te has sentido así. Todas las emociones están bien.</p></div>')


def pagina_respira():
    s = f'<text x="375" y="55" {font(42, 700)} fill="#111">Respira con Lúa</text>'
    # panel 1: huele la flor
    s += f'<g transform="translate(190,250) scale(0.9)">{cat_head(0.9, "joy")}</g>'
    s += flower(190, 470, 2.6)
    s += f'<text x="190" y="640" {font(30, 700)} fill="#111">1. Huele la flor</text>'
    s += f'<path d="M80,150 q20,-30 50,-20 M90,110 q20,-30 50,-20" fill="none" {ST} stroke-width="4"/>'
    # panel 2: apaga la vela
    s += f'<g transform="translate(560,250) scale(0.9)">{cat_head(0.9, "open")}</g>'
    s += f'<rect x="520" y="440" width="70" height="140" rx="10" fill="#fff" {ST}/>'
    s += f'<path d="M555,440 L555,425" {ST}/>'
    s += f'<path d="M555,420 q-22,-30 0,-70 q22,40 0,70 Z" fill="#fff" {ST}/>'
    s += f'<path d="M455,350 L500,355 M450,375 L495,375 M455,400 L500,395" fill="none" {ST} stroke-width="4"/>'
    s += f'<text x="560" y="640" {font(30, 700)} fill="#111">2. Apaga la vela</text>'
    return pag(f'<div class="art">{svg(s, "0 0 750 700")}</div>'
               f'<div class="txt"><p style="font-size:17pt">Coge aire despacio por la nariz. Suéltalo poco a poco por la boca. Repite tres veces.</p></div>')


def pagina_superpoder():
    s = f'<text x="375" y="55" {font(36, 700)} fill="#111">Lúa ve en la oscuridad. ¿Y tú?</text>'
    s += f'<rect x="60" y="100" width="630" height="520" rx="30" fill="#fff" {ST} stroke-dasharray="2 14"/>'
    s += star(95, 135, 20) + star(655, 135, 20) + star(95, 585, 20) + star(655, 585, 20)
    s += f'<text x="375" y="380" {font(26, 600)} fill="#111">Dibuja aquí tu superpoder</text>'
    return pag(f'<div class="art">{svg(s, "0 0 750 700")}</div>'
               f'<div class="txt" style="text-align:left"><p style="font-size:15pt;font-family:Nunito;font-weight:700">Mi superpoder es:</p><div class="line"></div></div>')


def pagina_amigo():
    s = f'<text x="375" y="60" {font(42, 700)} fill="#111">Dibuja a un amigo diferente a ti</text>'
    s += f'<rect x="60" y="100" width="630" height="520" rx="30" fill="#fff" {ST} stroke-dasharray="2 14"/>'
    s += star(95, 135, 20) + star(655, 135, 20) + heart(95, 585, 0.4) + heart(655, 585, 0.4)
    return pag(f'<div class="art">{svg(s, "0 0 750 700")}</div>'
               f'<div class="txt" style="text-align:left"><p style="font-size:15pt;font-family:Nunito;font-weight:700">Se llama:</p><div class="line"></div>'
               f'<p style="font-size:15pt;font-family:Nunito;font-weight:700;margin-top:.1in">Lo que más me gusta de él o de ella es:</p><div class="line"></div></div>')


def pagina_diploma():
    s = f'<rect x="20" y="20" width="710" height="660" rx="30" fill="none" {ST} stroke-width="8"/>'
    s += f'<rect x="42" y="42" width="666" height="616" rx="20" fill="none" {ST} stroke-dasharray="3 12"/>'
    s += star(95, 95, 26) + star(655, 95, 26) + star(95, 605, 26) + star(655, 605, 26)
    s += outlined_text(375, 150, 'DIPLOMA', 80)
    s += f'<text x="375" y="205" {font(28, 600)} fill="#111">de amigo o amiga de Lúa</text>'
    s += f'<path d="M150,300 L600,300" {ST} stroke-width="4"/>'
    s += f'<text x="375" y="335" {font(22, 600)} fill="#111">(escribe aquí tu nombre)</text>'
    prom = ['Trataré bien a todos, sean como sean.', 'Haré sitio en el juego a quien llegue nuevo.',
            'Ayudaré a quien lo necesite.']
    for i, p in enumerate(prom):
        s += star(130, 400 + i * 50, 14) + f'<text x="165" y="{407 + i * 50}" {font(26, 600, "start")} fill="#111">{p}</text>'
    s += f'<g transform="translate(140,575) scale(.3)">{cat_head(.3, "happy")}</g>'
    s += f'<g transform="translate(610,575) scale(.3)">{cat_head(.3, "joy")}</g>'
    s += f'<path d="M230,610 L370,610 M390,610 L530,610" {ST} stroke-width="4"/><text x="300" y="640" {font(18, 600)} fill="#111">Mi firma</text><text x="460" y="640" {font(18, 600)} fill="#111">Un adulto que me quiere</text>'
    return pag(f'<div style="margin-top:.35in">{svg(s, "0 0 750 700")}</div>')


def pasatiempos():
    cast = [dict(name='Lúa', fig=lambda cx, g, s: cat_sit(cx, g - 272 * s, s, 'happy'), h=402, like='pez'),
            dict(name='Nuez', fig=lambda cx, g, s: squirrel(cx, g, s, 'happy'), h=300, like='bellota'),
            dict(name='Trébol', fig=lambda cx, g, s: rabbit(cx, g, s, 'happy'), h=325, like='zanahoria'),
            dict(name='Pipa', fig=lambda cx, g, s: bird(cx, g, s, 'happy'), h=150, like='nido')]
    cfg = dict(cast=cast, sombra_cast=cast, hat_name='Lúa', words=['LUA', 'NUEZ', 'TREBOL', 'PIPA', 'MORA', 'MARI', 'LUNA', 'AMIGOS'],
               head_main=lambda cx, cy, s, mood: f'<g transform="translate({cx},{cy}) scale({s})">{cat_head(s, mood)}</g>',
               head_hat=lambda cx, cy, s: f'<g transform="translate({cx},{cy}) scale({s})">{cat_head(s, "happy")}</g>',
               hero_sit=lambda cx, g, s, mood: cat_sit(cx, g - 272 * s, s, mood),
               story=[SCENES[0], SCENES[4], SCENES[12], SCENES[17]],
               retos_titulo='Diez retos de amistad',
               retos=['Invita a jugar a alguien que esté solo.', 'Di algo bonito a un compañero nuevo.', 'Aprende el nombre de alguien de otra clase.', 'Pregunta a un amigo cómo se siente hoy.', 'Comparte tu merienda o tus colores.', 'Pide perdón si te has equivocado.', 'Juega a un juego que elija otro.', 'Mira la luna con alguien que te quiere.', 'Dibuja a tu familia tal como es.', 'Da las gracias a alguien, mirándole a los ojos.'],
               extra=dict(bee=bee, snail=snail, tin_can=tin_can, rocks=rocks, sprout=sprout, leaf=leaf))
    return build_pasatiempos(cfg, TITULO)


def interior():
    p = [pagina_titulo(), BLANCO, pagina_guia1(), pagina_guia2(), pagina_personajes(), BLANCO]
    for i in range(len(SCENES)):
        p += [pagina_escena(i), BLANCO]
    p += [pagina_emociones(), BLANCO, pagina_respira(), BLANCO, pagina_superpoder(), BLANCO,
          pagina_amigo(), BLANCO, pagina_diploma(), BLANCO]
    p += pasatiempos()
    assert len(p) == PAGINAS_TOTAL, len(p)
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{TITULO}</title><style>{CSS}</style></head><body>{"".join(p)}</body></html>'


# ----------------------------------------------------------------- cubierta
COLORES = {
    'cat_body': '#9ea8b5', 'cat_belly': '#e1e6ec', 'cat_inner': '#f4b5c5', 'nose': '#ee7f98', 'eye': '#8bd36b',
    'mouth': '#ef6b86', 'blush': '#f8b4c0', 'tear': '#bfe6ff',
    'sq_body': '#e0873a', 'sq_light': '#f7dcb4', 'acorn': '#c68545', 'acorn_cap': '#8a5a2b',
    'rb_body': '#f6efe6', 'rb_inner': '#f5b5c4', 'rb_belly': '#fffaf3',
    'lb_shell': '#e53935', 'lb_head': '#2b2b33', 'lb_dot': '#2b2b33',
    'bf_w1': '#ffb300', 'bf_w2': '#8e6bd8', 'bf_body': '#5a4636',
    'bd_body': '#3fa7e8', 'bd_light': '#cfeaff', 'beak': '#ffb300', 'nest': '#c9a36b',
    'fl_petal': '#ff8fb1', 'fl_mid': '#ffd23f',
}


def cubierta():
    A.COLORS.update(COLORES)
    spine = PAGINAS_TOTAL * GROSOR_PAPEL
    Wi, Hi = 2 * 8.5 + spine + 0.25, 11.25
    u = 100
    Wu, Hu = round(Wi * u), round(Hi * u)
    sx = round((0.125 + 8.5) * u)
    sw = round(spine * u)
    fx = sx + sw
    cx0 = fx + 425
    s = f'<rect width="{Wu}" height="{Hu}" fill="#c8ebff"/>'
    s += f'<path d="M0,{Hu - 210} Q{Wu * .25},{Hu - 255} {Wu * .5},{Hu - 205} T{Wu},{Hu - 215} L{Wu},{Hu} L0,{Hu} Z" fill="#8fd46b"/>'
    s += f'<rect x="{sx}" y="0" width="{sw}" height="{Hu}" fill="#ffd23f"/>'
    # frente
    for i, c in enumerate(['#ef4b4b', '#ff9a2e', '#ffd23f', '#5cc85c', '#3fa7e8']):
        r = 340 - i * 28
        s += f'<path d="M{cx0 - r},720 A{r},{r} 0 0 1 {cx0 + r},720" fill="none" stroke="{c}" stroke-width="28"/>'
    s += f'<circle cx="{fx + 95}" cy="130" r="55" fill="#fff6a8"/>'
    s += f'<path d="M{fx + 520},95 q20,-45 70,-30 q30,-35 70,-5 q40,-5 40,35 q-20,25 -60,15 q-30,20 -70,5 q-45,10 -50,-20z" fill="#fff"/>'
    s += (f'<text x="{cx0}" y="215" {font(150, 700)} fill="#ffd23f" stroke="#23232b" stroke-width="12" paint-order="stroke" stroke-linejoin="round">LÚA</text>'
          f'<text x="{cx0}" y="320" {font(72, 700)} fill="#fff" stroke="#23232b" stroke-width="10" paint-order="stroke" stroke-linejoin="round">la gatita gris</text>')
    s += f'<rect x="{cx0 - 290}" y="352" width="580" height="54" rx="27" fill="#fff" stroke="#23232b" stroke-width="4"/>'
    s += f'<text x="{cx0}" y="391" {font(25, 700)} fill="#23232b">Para colorear · 4 a 8 años · Con guía para familias</text>'
    s += cat_sit(cx0, 620, 1.3, 'happy', tail='up')
    s += squirrel(cx0 - 300, 1000, 0.95, 'happy') + rabbit(cx0 + 300, 1005, 0.9, 'happy', flip=-1)
    s += butterfly(cx0 + 270, 520, 0.75) + butterfly(cx0 - 260, 560, 0.6, flip=-1)
    s += f'<text x="{cx0}" y="1100" {font(34, 700)} fill="#23232b">{AUTOR}</text>'
    # reverso
    bx0 = 12 + 425
    s += f'<rect x="{bx0 - 330}" y="140" width="660" height="470" rx="30" fill="#fff" fill-opacity=".94" stroke="#23232b" stroke-width="5"/>'
    lineas = ['A Lúa no la dejan jugar porque no', 'tiene colores vivos. Hasta que una noche', 'descubre todo lo que vale, y lo que',
              'ya valía antes.', '', 'Cuento para colorear con muy poco texto,', 'emociones, calma y guía para familias.']
    for i, l in enumerate(lineas):
        s += f'<text x="{bx0}" y="{215 + i * 48}" {font(30, 600)} fill="#23232b">{l}</text>'
    s += cat_sit(bx0 - 130, 790, 0.6, 'joy', tail='up') + bird(bx0 + 130, 955, 0.9, 'happy', flip=-1)
    s += f'<rect x="{round((0.125 + 8.5 - 0.25 - 2) * u)}" y="{round((0.125 + 11 - 0.25 - 1.2) * u)}" width="200" height="120" fill="#fff"/>'
    A.COLORS.clear()
    css = CSS.replace('@page{size:8.5in 11in;margin:0}', '@page{size:%.4fin %.4fin;margin:0}' % (Wi, Hi))
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{css}body{{margin:0}} '
            f'svg{{width:{Wi:.4f}in;height:{Hi:.4f}in;display:block}}</style></head><body>'
            f'<svg viewBox="0 0 {Wu} {Hu}" xmlns="http://www.w3.org/2000/svg">{s}</svg></body></html>')



def cubierta_acuarela():
    """Cubierta con ilustraciones en acuarela (arte/). Misma geometría KDP que cubierta()."""
    spine = PAGINAS_TOTAL * GROSOR_PAPEL
    Wi, Hi = 2 * 8.5 + spine + 0.25, 11.25
    u = 100
    Wu, Hu = round(Wi * u), round(Hi * u)
    sx, sw = round((0.125 + 8.5) * u), round(spine * u)
    fx = sx + sw
    cx0 = fx + 425
    bx0 = 12 + 425
    tinta, crema = '#3a2a1e', '#fffaf0'
    s = f'<image href="arte/contraportada-acuarela.jpg" x="0" y="0" width="{sx}" height="{Hu}" preserveAspectRatio="xMidYMid slice"/>'
    s += f'<image href="arte/portada-acuarela.jpg" x="{fx}" y="0" width="{Wu - fx}" height="{Hu}" preserveAspectRatio="xMidYMid slice"/>'
    s += f'<rect x="{sx}" y="0" width="{sw}" height="{Hu}" fill="#e9c46a"/>'
    halo = f'stroke="{crema}" stroke-width="10" stroke-opacity=".85" paint-order="stroke" stroke-linejoin="round"'
    s += f'<text x="{cx0}" y="120" font-family="Fraunces" font-weight="700" font-size="30" fill="{tinta}" {halo} text-anchor="middle" letter-spacing="9">VOLUMEN I</text>'
    s += f'<text x="{cx0}" y="222" font-family="Fraunces" font-weight="700" font-size="96" fill="{tinta}" {halo} text-anchor="middle">Lúa,</text>'
    s += f'<text x="{cx0}" y="318" font-family="Fraunces" font-weight="700" font-size="88" fill="#b5562b" {halo} text-anchor="middle">la gatita gris</text>'
    s += f'<rect x="{cx0 - 285}" y="342" width="570" height="48" rx="24" fill="{crema}" fill-opacity=".9"/>'
    s += f'<text x="{cx0}" y="374" font-family="Fraunces" font-weight="600" font-size="23" text-anchor="middle" fill="{tinta}">Para colorear · 4 a 8 años · Con guía para familias</text>'
    s += f'<rect x="{cx0 - 170}" y="968" width="340" height="56" rx="28" fill="{crema}" fill-opacity=".88"/>'
    s += f'<text x="{cx0}" y="1006" font-family="Fraunces" font-weight="700" font-size="32" text-anchor="middle" fill="{tinta}">{AUTOR}</text>'
    s += f'<rect x="{bx0 - 350}" y="55" width="700" height="300" rx="26" fill="{crema}" fill-opacity=".92"/>'
    lineas = ['Volumen I de la serie Lúa', 'A Lúa no la dejan jugar porque no tiene', 'colores vivos. Hasta que una noche, ágil,', 'veloz y valiente, ayuda a Pipa a volver', 'a casa y descubre todo lo que vale.', 'Y lo que ya valía antes.', 'Con 20 pasatiempos y guía para familias.']
    for i, l in enumerate(lineas):
        s += f'<text x="{bx0}" y="{100 + i * 37 + (8 if i else 0)}" font-family="Fraunces" font-weight="{700 if i in (0, 6) else 600}" font-size="{27 if i == 0 else 24}" text-anchor="middle" fill="{tinta}">{l}</text>'
    s += f'<rect x="{round((0.125 + 8.5 - 0.25 - 2) * u)}" y="{round((0.125 + 11 - 0.25 - 1.2) * u)}" width="200" height="120" fill="#fff"/>'
    css = CSS.replace('@page{size:8.5in 11in;margin:0}', '@page{size:%.4fin %.4fin;margin:0}' % (Wi, Hi))
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{css}body{{margin:0}} '
            f'svg{{width:{Wi:.4f}in;height:{Hi:.4f}in;display:block}}</style></head><body>'
            f'<svg viewBox="0 0 {Wu} {Hu}" xmlns="http://www.w3.org/2000/svg">{s}</svg></body></html>')


if __name__ == '__main__':
    open(os.path.join(AQUI, 'interior.html'), 'w').write(interior())
    acu = os.path.exists(os.path.join(AQUI, 'arte', 'portada-acuarela.jpg'))
    open(os.path.join(AQUI, 'portada.html'), 'w').write(cubierta_acuarela() if acu else cubierta())
    print('ok', PAGINAS_TOTAL, 'paginas; lomo %.3f in' % (PAGINAS_TOTAL * GROSOR_PAPEL))
