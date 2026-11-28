# Libro 3: "Lúa y el vecino nuevo". Genera interior.html y portada.html (cubierta KDP).
import os
import animales as A
import pasatiempos as P
from base import *
from escenas import SCENES, TEXTOS, HIDDEN, csit, stars_night, sniff

# ---- datos editables ---------------------------------------------------
TITULO = 'Lúa y el vecino nuevo'
SUBTITULO = 'Un cuento para colorear sobre el miedo a lo diferente'
VOLUMEN = 'Volumen III'
AUTOR = 'Alex Berruezo'
CREDITO = AUTOR               # linea de la portadilla (ver ESTADO-LUA.md: decision pendiente sobre "ilustraciones")
ANIO = '2026'
PAGINAS_TOTAL = 80            # debe coincidir con el interior generado
GROSOR_PAPEL = 0.002252       # pulgadas por pagina, papel blanco KDP (verificar con la calculadora de KDP)
# -------------------------------------------------------------------------

AQUI = os.path.dirname(os.path.abspath(__file__))


def pagina_titulo():
    s = moon(640, 80, 40) + cloud(80, 40, 140) + hill(640, 750, 740, 18)
    s += csit(130, 715, 0.75, mood='happy') + csit(265, 705, 0.6, mood='mischief', kind='raspi')
    s += tilo(410, 712, 0.75, 'happy') + hera_sit(560, 722, 0.7, 'smile') + csit(690, 705, 0.5, mood='silly', kind='neu')
    s += chispa(330, 300, 0.9) + falling([(200, 300, 20), (520, 330, -30)])
    return pag(f'''
<div class="center" style="margin-top:.05in">
  <p style="margin:0 0 .04in;font-family:Fraunces;font-weight:700;font-size:15pt;letter-spacing:.18em;text-transform:uppercase">{VOLUMEN} de la serie Lúa</p>
  <h1 style="font-size:55pt;line-height:1.05;-webkit-text-stroke:2px #111;color:#fff">Lúa y el<br>vecino nuevo</h1>
  <p style="font-family:Fraunces;font-weight:600;font-style:italic;font-size:16pt;margin:.14in 0 0">{SUBTITULO}</p>
</div>
<div class="art" style="margin-top:.1in">{svg(s, '0 0 750 740')}</div>
<p class="center" style="position:absolute;bottom:.45in;left:0;right:0;font-family:Fraunces;font-weight:600;font-size:14pt">{CREDITO}</p>''')


def pagina_guia1():
    return pag(f'''<div class="note">
<h2>Para las familias</h2>
<p>Este cuento habla de una emoción que todos conocemos: el miedo a lo que no conocemos. Un compañero nuevo en clase, una vecina que habla otro idioma, un niño que se mueve o se viste distinto. A veces ese miedo se convierte en rumores y motes, y los niños se suman sin darse cuenta.</p>
<h3>Lo que trabaja cada personaje</h3>
<ul>
<li><b>Lúa</b> ya sabe lo que es ser la distinta, y aun así siente miedo. Aprende que el miedo no se va solo: se va preguntando y acercándose.</li>
<li><b>Raspi</b> exagera, inventa y le pone un mote a Tilo. La historia muestra que pedir perdón de verdad arregla mucho.</li>
<li><b>Neu</b> rompe el hielo con humor. Reírse con alguien, y no de alguien, es una forma de dar la bienvenida.</li>
<li><b>Hera</b> no da sermones: anima a preguntar, y ella también aprende algo nuevo (lo de la leche).</li>
<li><b>Tilo</b> es el nuevo. Tiene miedo, ha perdido su casa y es distinto en casi todo. Justo lo que le hace raro es lo que salva a Raspi.</li>
</ul>
<h3>Cuatro ideas que se repiten</h3>
<ul>
<li><b>Lo que no conocemos asusta.</b> Es normal, y no es culpa de nadie.</li>
<li><b>Los rumores crecen.</b> Cada vez que se cuenta una historia sin comprobarla, el monstruo se hace más grande.</li>
<li><b>Los nombres importan.</b> Un mote puede doler mucho aunque se diga en broma.</li>
<li><b>Preguntar es mejor que imaginar.</b> Y escuchar la respuesta, también.</li>
</ul>
<h3>Cómo usarlo, con 5 minutos al día</h3>
<ol>
<li>Leed una escena y preguntad qué siente cada personaje. También Tilo.</li>
<li>Parad en la escena 4, cuando el monstruo crece, y preguntad: ¿alguien lo había visto de verdad?</li>
<li>Dejad que coloreen como quieran. Tilo puede ser marrón, azul o de lunares.</li>
</ol>
<p>En cada escena se esconde Chispa, la luciérnaga. ¡Buscadla! Al final hay 20 páginas de pasatiempos, impresas por las dos caras: usad lápices o rotuladores finos.</p>
</div>''')


def pagina_guia2():
    return pag(f'''<div class="note">
<h2>Frases y preguntas</h2>
<h3>Frases que ayudan</h3>
<ul>
<li>Si le da miedo alguien nuevo: «Es normal tener un poco de miedo. ¿Qué te gustaría saber de él o de ella?»</li>
<li>Si repite un rumor: «¿Eso lo has visto tú o te lo han contado?»</li>
<li>Si pone un mote: «¿Cómo se llama de verdad? Vamos a llamarle por su nombre.»</li>
<li>Si el nuevo es él o ella: «Los demás también están un poco nerviosos. Para empezar, basta con un hola.»</li>
</ul>
<h3>Preguntas para conversar</h3>
<ul>
<li>¿Por qué pensaba Raspi que Tilo era un monstruo? ¿Lo había visto?</li>
<li>¿Cómo se sintió Tilo cuando le llamaron «Pincho»?</li>
<li>¿Quién tenía más miedo, los amigos o Tilo?</li>
<li>¿Qué cosa rara de Tilo acabó siendo muy útil?</li>
<li>¿Alguna vez has sido el nuevo o la nueva? ¿Qué te ayudó?</li>
</ul>
<h3>Cuándo buscar ayuda</h3>
<p>Este libro es un apoyo para conversar en casa, no un tratamiento. Si tu hijo lleva semanas triste o muy retraído, evita ir al colegio o sufre burlas, rechazo o agresiones repetidas, habla con su tutor o tutora y con su pediatra o un psicólogo infantil.</p>
<p style="font-size:11.5pt">Lo que cuenta Tilo es cierto: los erizos salen de noche, ven poco, tienen un olfato excelente y la leche les sienta mal.</p>
<div class="legal">© {ANIO} {AUTOR}. Todos los derechos reservados. Prohibida la reproducción total o parcial de esta obra sin permiso del autor. Primera edición. {VOLUMEN} de la serie «Lúa».</div>
</div>''')


def pagina_personajes():
    s = f'<text x="375" y="52" {font(44, 700)} fill="#111">Conoce a los amigos</text>'
    s += csit(130, 330, 0.55, mood='happy') + tilo(375, 330, 0.75, 'happy') + hera_sit(620, 335, 0.58, 'smile')
    s += csit(250, 655, 0.58, mood='mischief', kind='raspi') + csit(500, 655, 0.58, mood='silly', kind='neu')
    for n, d, x, y in (('Lúa', 'la gatita gris', 130, 378), ('Tilo', 'el erizo nuevo', 375, 378), ('Hera', 'la labradora sabia', 620, 378),
                       ('Raspi', 'la gata parda', 250, 703), ('Neu', 'la gata blanca', 500, 703)):
        s += f'<text x="{x}" y="{y}" {font(34, 700)} fill="#111">{n}</text><text x="{x}" y="{y + 28}" {font(19, 600)} fill="#111">{d}</text>'
    return pag(f'<div class="art">{svg(s, "0 0 750 760")}</div>'
               f'<div class="txt"><p style="font-size:14pt">Y Chispa, la luciérnaga, que se esconde en cada escena. ¡Buscadla!</p></div>')


def pagina_escena(i):
    return pag(f'<div class="art">{svg(SCENES[i]() + chispa(*HIDDEN[i], 0.62), "0 0 750 780", marco=True)}</div><div class="txt">{PAW}<p>{TEXTOS[i]}</p></div>')


# ------------------------------------------------------------- actividades
def pagina_imaginado():
    s = f'<text x="375" y="46" {font(34, 700)} fill="#111">Lo que imaginaban y lo que era</text>'
    for x in (25, 390):
        s += f'<rect x="{x}" y="80" width="335" height="420" rx="22" fill="#fff" {ST}/>'
    s += monster(192, 280, 1.05) + tilo(557, 450, 1.0, 'happy')
    s += f'<text x="192" y="540" {font(24, 700)} fill="#111">Lo que imaginaban</text><text x="557" y="540" {font(24, 700)} fill="#111">Cómo es Tilo</text>'
    return pag(f'<div class="art">{svg(s, "0 0 750 560")}</div>'
               f'<div class="note"><p style="font-size:14pt;text-align:center"><b>Colorea los dos dibujos.</b></p>'
               f'<p style="font-family:Fraunces;font-weight:600;font-size:16pt;margin-top:.15in">¿Alguna vez algo te dio miedo y luego no era para tanto? Dibújalo o escríbelo:</p>'
               f'<div class="line"></div><div class="line"></div><div class="line"></div></div>')


def pagina_aprendizaje():
    filas = [('lua', 'happy', 'Lúa aprendió que lo diferente asusta hasta que lo conoces.'),
             ('raspi', 'mischief', 'Raspi aprendió que los motes duelen y que pedir perdón arregla mucho.'),
             ('neu', 'silly', 'Neu aprendió que una risa puede abrir una puerta.'),
             ('hera', 'smile', 'Hera nos recordó que preguntando se aprende.'),
             ('tilo', 'happy', 'Tilo aprendió que en un sitio nuevo también se hacen amigos.')]
    filas_html = ''
    for kind, mood, texto in filas:
        if kind == 'hera':
            icon = svg(hera_sit(60, 112, 0.34, 'smile'), '0 0 120 120', False, .95)
        elif kind == 'tilo':
            icon = svg(tilo(60, 114, 0.42, 'happy'), '0 0 120 120', False, .95)
        else:
            icon = svg(f'<g transform="translate(60,62) scale(0.5)">{cat_head(0.5, mood, 0, False, kind)}</g>', '0 0 120 120', False, .95)
        filas_html += (f'<div style="display:flex;align-items:center;gap:.15in;border:3px solid #111;border-radius:.2in;padding:.05in .15in;margin-bottom:.1in">'
                       f'<div style="width:.95in;flex:none">{icon}</div>'
                       f'<div style="font-family:Fraunces;font-weight:600;font-size:15pt;line-height:1.28">{texto}</div></div>')
    return pag(f'<h2 class="center" style="font-size:28pt;margin-top:.05in">¿Qué aprendió cada amigo?</h2>'
               f'<p class="center" style="font-size:13pt;margin:.08in 0 .18in;font-family:Nunito;font-weight:700">Colorea a cada amigo y lee en voz alta lo que aprendió.</p>'
               f'{filas_html}'
               f'<p style="font-family:Fraunces;font-weight:600;font-size:16pt;margin-top:.12in">Y tú, ¿qué has aprendido?</p><div class="line"></div>')


def pagina_erizos():
    s = f'<text x="375" y="46" {font(34, 700)} fill="#111">Ayuda a los erizos de tu barrio</text>'
    s += hill(420, 750, 470, 0) + fence_hole(10, 740, 420, 250, 110) + tilo(400, 440, 0.6, 'happy', look=1)
    s += bowl(560, 455, 0.9) + leaf_pile(680, 460, 0.7) + moon(660, 120, 40) + star(520, 100, 12) + twinkle(120, 120, .8)
    tips = ['Ponle un plato bajo con agua. Nunca leche ni pan.', 'Deja un agujero de unos 13 cm en la base de la valla.',
            'No uses venenos para caracoles ni babosas.', 'Guarda un rincón con hojas secas y ramitas.',
            'No lo cojas ni te lo lleves a casa.', 'Si ves uno de día, herido o dando vueltas, avisa a un adulto:\npuede necesitar un centro de recuperación de fauna.']
    lis = ''.join(f'<li style="margin:.06in 0">{t.replace(chr(10), " ")}</li>' for t in tips)
    return pag(f'<div class="art">{svg(s, "0 0 750 480")}</div><div class="note"><ul style="margin-top:.1in">{lis}</ul>'
               f'<p style="font-size:12pt">Colorea el dibujo. Los erizos salen de noche y recorren mucho camino buscando comida: un agujero en la valla les abre el paso de jardín en jardín.</p></div>')


def pagina_hola():
    holas = [('Hola', 'español'), ('Hello', 'inglés'), ('Bonjour', 'francés'), ('Ciao', 'italiano'), ('Olá', 'portugués'), ('Hallo', 'alemán'),
             ('Bon dia', 'catalán'), ('Kaixo', 'euskera'), ('Ola', 'gallego'), ('Marhaba', 'árabe'), ('Ni hao', 'chino'), ('Merhaba', 'turco')]
    s = f'<text x="375" y="46" {font(34, 700)} fill="#111">Hola en muchos idiomas</text>'
    for i, (h, l) in enumerate(holas):
        x, y = 30 + (i % 3) * 235, 90 + (i // 3) * 140
        s += bubble(x, y, 215, 80, h, x + 50, y + 108, 32) + f'<text x="{x + 120}" y="{y + 124}" {font(18, 600, "start")} fill="#111">{l}</text>'
    s += tilo(90, 760, 0.42, 'happy') + csit(660, 760, 0.42, mood='happy')
    return pag(f'<div class="art">{svg(s, "0 0 750 770")}</div>'
               f'<div class="txt" style="text-align:left"><p style="font-size:14pt;font-family:Nunito;font-weight:700">Cuando alguien llega nuevo, un hola en su idioma es un buen regalo. ¿Cómo se dice hola en tu casa o en la de tus amigos?</p><div class="line"></div></div>')


def pagina_vecindario():
    s = f'<text x="375" y="54" {font(40, 700)} fill="#111">Mi calle y mis vecinos</text>'
    s += f'<rect x="50" y="95" width="650" height="520" rx="30" fill="#fff" {ST} stroke-dasharray="2 14"/>'
    s += moon(120, 165, 26) + chispa(640, 160, 0.8) + tilo(640, 600, 0.3, 'happy')
    return pag(f'<div class="art">{svg(s, "0 0 750 670")}</div>'
               f'<div class="txt" style="text-align:left"><p style="font-size:15pt;font-family:Nunito;font-weight:700">Un vecino o vecina que me gustaría conocer mejor:</p><div class="line"></div></div>')


def pagina_diploma():
    s = f'<rect x="20" y="20" width="710" height="660" rx="30" fill="none" {ST} stroke-width="8"/>'
    s += f'<rect x="42" y="42" width="666" height="616" rx="20" fill="none" {ST} stroke-dasharray="3 12"/>'
    s += chispa(95, 115, 0.9) + chispa(655, 115, 0.9)
    s += outlined_text(375, 150, 'DIPLOMA', 80)
    s += f'<text x="375" y="198" {font(25, 600)} fill="#111">de buen vecino o buena vecina</text>'
    s += f'<path d="M150,290 L600,290" {ST} stroke-width="4"/><text x="375" y="325" {font(21, 600)} fill="#111">(escribe aquí tu nombre)</text>'
    prom = ['Antes de juzgar a alguien, le preguntaré.', 'Llamaré a cada uno por su nombre.', 'Daré la bienvenida a quien llegue nuevo.']
    for i, p in enumerate(prom):
        s += star(100, 392 + i * 50, 13) + f'<text x="130" y="{399 + i * 50}" {font(23, 600, "start")} fill="#111">{p}</text>'
    s += f'<g transform="translate(140,575) scale(.3)">{cat_head(.3, "happy")}</g>' + tilo(610, 625, 0.34, 'happy')
    s += f'<path d="M230,610 L370,610 M390,610 L530,610" {ST} stroke-width="4"/><text x="300" y="640" {font(18, 600)} fill="#111">Mi firma</text><text x="460" y="640" {font(18, 600)} fill="#111">Un adulto que me quiere</text>'
    return pag(f'<div style="margin-top:.35in">{svg(s, "0 0 750 700")}</div>')


def pasatiempos():
    P.ADIV[1] = ('Llevo un abrigo de pinchos, duermo todo el invierno y salgo de noche a buscar mi cena.', 'El erizo')
    P.LIKE['hojas'] = lambda x, y: leaf_pile(x, y + 40, 0.75)
    cast = [dict(name='Lúa', fig=lambda cx, g, s: csit(cx, g, s, mood='happy'), h=402, like='pez'),
            dict(name='Tilo', fig=lambda cx, g, s: tilo(cx, g, s, 'happy'), h=250, like='hojas'),
            dict(name='Hera', fig=lambda cx, g, s: hera_sit(cx, g, s, 'smile'), h=335, like='hueso'),
            dict(name='Raspi', fig=lambda cx, g, s: csit(cx, g, s, mood='mischief', kind='raspi'), h=402, like='ovillo')]
    sombra_cast = [dict(name='Tilo', fig=lambda cx, g, s: tilo(cx, g, s, 'happy'), h=250),
                   dict(name='Hera', fig=lambda cx, g, s: hera_sit(cx, g, s, 'smile'), h=335),
                   dict(name='Nuez', fig=lambda cx, g, s: squirrel(cx, g, s, 'happy'), h=300),
                   dict(name='Pipa', fig=lambda cx, g, s: bird(cx, g, s, 'happy'), h=150)]
    cfg = dict(cast=cast, sombra_cast=sombra_cast, hat_name='Tilo', words=['LUA', 'TILO', 'ERIZO', 'NEU', 'HERA', 'RASPI', 'VECINO', 'HOLA'],
               head_main=lambda cx, cy, s, mood: f'<g transform="translate({cx},{cy}) scale({s})">{cat_head(s, mood)}</g>',
               head_hat=lambda cx, cy, s: tilo(cx, cy + 100 * s, s * 0.8, 'happy'),
               hero_sit=lambda cx, g, s, mood: csit(cx, g, s, mood=mood),
               story=[SCENES[0], SCENES[6], SCENES[16], SCENES[19]],
               retos=['Saluda a un vecino o vecina por su nombre.', 'Aprende a decir hola en otro idioma.', 'Pregúntale a alguien cuál es su comida favorita.',
                      'Invita a jugar a alguien que esté solo.', 'Pon un plato de agua para los animales.', 'Busca un bicho de noche con una linterna.',
                      'Cuenta una cosa buena de alguien que no conoces mucho.', 'Huele tres cosas con los ojos cerrados.', 'Haz un dibujo de bienvenida para alguien.',
                      'Pide perdón si has dicho algo que dolió.'],
               extra=dict(bee=bee, snail=snail, tin_can=tin_can, rocks=rocks, sprout=sprout, leaf=leaf))
    out = P.build(cfg, TITULO)
    rep = {'Mandala del jardín': 'Mandala del otoño', 'Diez retos de jardín': 'Diez retos de buen vecino',
           'Valen el jardín, el parque o un paseo.': 'Podéis hacerlos en casa, en el cole o en la calle.'}
    res = []
    for h in out:
        for a, b in rep.items():
            h = h.replace(a, b)
        res.append(h)
    return res


def interior():
    p = [pagina_titulo(), BLANCO, pagina_guia1(), pagina_guia2(), pagina_personajes(), BLANCO]
    for i in range(len(SCENES)):
        p += [pagina_escena(i), BLANCO]
    p += [pagina_imaginado(), BLANCO, pagina_aprendizaje(), BLANCO, pagina_erizos(), BLANCO, pagina_hola(), BLANCO,
          pagina_vecindario(), BLANCO, pagina_diploma(), BLANCO] + pasatiempos()
    assert len(p) == PAGINAS_TOTAL, len(p)
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{TITULO}</title><style>{CSS}</style></head><body>{"".join(p)}</body></html>'


# ----------------------------------------------------------------- cubierta
COLORES = {
    'cat_body': '#9ea8b5', 'cat_belly': '#e1e6ec', 'cat_inner': '#f4b5c5', 'nose': '#ee7f98', 'eye': '#8bd36b',
    'mouth': '#ef6b86', 'blush': '#f8b4c0', 'tongue': '#ff8fa8',
    'raspi_body': '#b88a5c', 'raspi_belly': '#e8d3b8', 'neu_body': '#fbfbfb', 'neu_belly': '#ffffff',
    'hera_body': '#6a3d2a', 'hera_light': '#8b5a3f', 'hera_gray': '#cdbcae', 'hera_collar': '#e53935', 'hera_tag': '#ffd23f', 'hera_dark': '#2b1d17',
    'tilo_spikes': '#8a6a4f', 'tilo_face': '#e8cfae', 'tilo_belly': '#f5e6d0', 'tilo_dark': '#2b1d17',
    'leaf': '#e09a3e', 'stem': '#7a5a2b',
}


def _geom():
    spine = PAGINAS_TOTAL * GROSOR_PAPEL
    Wi, Hi = 2 * 8.5 + spine + 0.25, 11.25
    u = 100
    Wu, Hu = round(Wi * u), round(Hi * u)
    sx, sw = round((0.125 + 8.5) * u), round(spine * u)
    return spine, Wi, Hi, u, Wu, Hu, sx, sw, sx + sw


CONTRA = ['Volumen III de la serie Lúa', 'Una casita de hojas aparece bajo el seto', 'y en el jardín empiezan los rumores:',
          '¡vive un monstruo con mil pinchos!', 'Lúa, Hera, Raspi y Neu descubren que', 'lo diferente asusta hasta que lo conoces,',
          'que los motes duelen y que preguntar', 'es más valiente que imaginar.', 'Con guía para familias.']


def _html(s, Wi, Hi, Wu, Hu):
    css = CSS.replace('@page{size:8.5in 11in;margin:0}', '@page{size:%.4fin %.4fin;margin:0}' % (Wi, Hi))
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{css}body{{margin:0}} '
            f'svg{{width:{Wi:.4f}in;height:{Hi:.4f}in;display:block}}</style></head><body>'
            f'<svg viewBox="0 0 {Wu} {Hu}" xmlns="http://www.w3.org/2000/svg">{s}</svg></body></html>')


def cubierta():
    """Cubierta dibujada con codigo, en color. Provisional hasta tener la acuarela."""
    A.COLORS.update(COLORES)
    spine, Wi, Hi, u, Wu, Hu, sx, sw, fx = _geom()
    cx0, bx0 = fx + 425, 12 + 425
    s = f'<rect width="{Wu}" height="{Hu}" fill="#f6e2c4"/>'
    s += f'<path d="M0,{Hu - 250} Q{Wu * .25},{Hu - 300} {Wu * .5},{Hu - 240} T{Wu},{Hu - 255} L{Wu},{Hu} L0,{Hu} Z" fill="#a8c66c"/>'
    s += f'<rect x="{sx}" y="0" width="{sw}" height="{Hu}" fill="#d9822b"/>'
    s += f'<circle cx="{fx + 110}" cy="125" r="52" fill="#fff6a8"/>'
    t = lambda y, txt, sz, col: (f'<text x="{cx0}" y="{y}" font-family="Fraunces" font-weight="700" font-size="{sz}" fill="{col}" stroke="#23232b" '
                                 f'stroke-width="9" paint-order="stroke" stroke-linejoin="round" text-anchor="middle">{txt}</text>')
    s += (f'<text x="{cx0}" y="125" font-family="Fraunces" font-weight="700" font-size="36" fill="#fff" stroke="#23232b" stroke-width="8" '
          f'paint-order="stroke" stroke-linejoin="round" text-anchor="middle" letter-spacing="6">VOLUMEN III</text>')
    s += t(228, 'Lúa y el', 92, '#fff') + t(322, 'vecino nuevo', 92, '#f2a541')
    s += f'<rect x="{cx0 - 300}" y="338" width="600" height="54" rx="27" fill="#fff" stroke="#23232b" stroke-width="4"/>'
    s += f'<text x="{cx0}" y="376" font-family="Fraunces" font-weight="600" font-size="25" text-anchor="middle" fill="#23232b">Para colorear · 4 a 8 años · Con guía para familias</text>'
    s += hedge(fx + 20, fx + 850, 870, 150)
    s += leaf_house(fx + 720, 880, 0.9)
    s += hera_sit(cx0 + 290, 1020, 0.72, 'smile') + csit(cx0 - 250, 1010, 0.85, mood='happy')
    s += csit(cx0 - 130, 1015, 0.55, mood='mischief', kind='raspi') + csit(cx0 + 175, 1015, 0.48, mood='silly', kind='neu')
    s += tilo(cx0 + 10, 1018, 1.0, 'happy')
    s += falling([(cx0 - 250, 560, 20), (cx0 + 230, 520, -40), (cx0 - 60, 470, 60)]) + chispa(cx0 + 240, 640, 1.1)
    s += f'<text x="{cx0}" y="1100" font-family="Fraunces" font-weight="700" font-size="34" text-anchor="middle" fill="#23232b">{AUTOR}</text>'
    s += f'<rect x="{bx0 - 330}" y="120" width="660" height="520" rx="30" fill="#fff" fill-opacity=".94" stroke="#23232b" stroke-width="5"/>'
    for i, l in enumerate(CONTRA):
        s += f'<text x="{bx0}" y="{185 + i * 50}" font-family="Fraunces" font-weight="{700 if i in (0, 8) else 600}" font-size="{29 if i in (0, 8) else 27}" text-anchor="middle" fill="#23232b">{l}</text>'
    s += csit(bx0 - 150, 1000, 0.65, mood='joy') + tilo(bx0 + 150, 1005, 0.8, 'smile')
    s += f'<rect x="{round((0.125 + 8.5 - 0.25 - 2) * u)}" y="{round((0.125 + 11 - 0.25 - 1.2) * u)}" width="200" height="120" fill="#fff"/>'
    A.COLORS.clear()
    return _html(s, Wi, Hi, Wu, Hu)


def cubierta_acuarela():
    """Cubierta con ilustraciones en acuarela (arte/), misma maqueta que el volumen II."""
    spine, Wi, Hi, u, Wu, Hu, sx, sw, fx = _geom()
    cx0, bx0 = fx + 425, 12 + 425
    tinta, crema = '#3a2a1e', '#fffaf0'
    s = f'<image href="arte/contraportada-acuarela.jpg" x="0" y="0" width="{sx}" height="{Hu}" preserveAspectRatio="xMidYMid slice"/>'
    s += f'<image href="arte/portada-acuarela.jpg" x="{fx}" y="0" width="{Wu - fx}" height="{Hu}" preserveAspectRatio="xMidYMid slice"/>'
    s += f'<rect x="{sx}" y="0" width="{sw}" height="{Hu}" fill="#d9822b"/>'
    halo = f'stroke="{crema}" stroke-width="10" stroke-opacity=".85" paint-order="stroke" stroke-linejoin="round"'
    s += f'<text x="{cx0}" y="120" font-family="Fraunces" font-weight="700" font-size="30" fill="{tinta}" {halo} text-anchor="middle" letter-spacing="9">VOLUMEN III</text>'
    s += f'<text x="{cx0}" y="222" font-family="Fraunces" font-weight="700" font-size="96" fill="{tinta}" {halo} text-anchor="middle">Lúa y el</text>'
    s += f'<text x="{cx0}" y="318" font-family="Fraunces" font-weight="700" font-size="88" fill="#b5562b" {halo} text-anchor="middle">vecino nuevo</text>'
    s += f'<rect x="{cx0 - 285}" y="342" width="570" height="48" rx="24" fill="{crema}" fill-opacity=".9"/>'
    s += f'<text x="{cx0}" y="374" font-family="Fraunces" font-weight="600" font-size="23" text-anchor="middle" fill="{tinta}">Para colorear · 4 a 8 años · Con guía para familias</text>'
    s += f'<rect x="{cx0 - 170}" y="968" width="340" height="56" rx="28" fill="{crema}" fill-opacity=".88"/>'
    s += f'<text x="{cx0}" y="1006" font-family="Fraunces" font-weight="700" font-size="32" text-anchor="middle" fill="{tinta}">{AUTOR}</text>'
    s += f'<rect x="{bx0 - 350}" y="55" width="700" height="400" rx="26" fill="{crema}" fill-opacity=".92"/>'
    for i, l in enumerate(CONTRA):
        s += f'<text x="{bx0}" y="{100 + i * 39 + (8 if i else 0)}" font-family="Fraunces" font-weight="{700 if i in (0, 8) else 600}" font-size="{27 if i == 0 else 24}" text-anchor="middle" fill="{tinta}">{l}</text>'
    s += f'<rect x="{round((0.125 + 8.5 - 0.25 - 2) * u)}" y="{round((0.125 + 11 - 0.25 - 1.2) * u)}" width="200" height="120" fill="#fff"/>'
    return _html(s, Wi, Hi, Wu, Hu)


if __name__ == '__main__':
    open(os.path.join(AQUI, 'interior.html'), 'w').write(interior())
    acu = os.path.exists(os.path.join(AQUI, 'arte', 'portada-acuarela.jpg'))
    open(os.path.join(AQUI, 'portada.html'), 'w').write(cubierta_acuarela() if acu else cubierta())
    print('ok', PAGINAS_TOTAL, 'paginas; lomo %.3f in' % (PAGINAS_TOTAL * GROSOR_PAPEL), '; cubierta', 'acuarela' if acu else 'dibujada con codigo')
