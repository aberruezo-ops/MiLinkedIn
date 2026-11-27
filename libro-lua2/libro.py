# Libro 2: "Lúa y el jardín de todos". Genera interior.html y portada.html (cubierta KDP).
import os
import animales as A
from jardin import *
from escenas import SCENES, TEXTOS, HIDDEN, csit, stars_night
from pasatiempos import build as build_pasatiempos

# ---- datos editables ---------------------------------------------------
TITULO = 'Lúa y el jardín de todos'
SUBTITULO = 'Un cuento para colorear sobre ser distintos y crecer juntos'
VOLUMEN = 'Volumen II'
AUTOR = 'Alex Berruezo'
ANIO = '2026'
PAGINAS_TOTAL = 80            # debe coincidir con el interior generado
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
    s = sun(90, 95, 38) + cloud(550, 40, 140) + cloud(250, 120, 100) + hill(640, 750, 740, 18)
    s += fence(10, 740, 600, 70)
    s += sunflower(70, 700, 0.8, 190) + sunflower(690, 700, 0.8, 190) + lavender(150, 700, 0.9, 150) + lavender(610, 700, 0.9, 150)
    s += csit(215, 715, 1.0, mood='happy') + csit(395, 705, 0.72, mood='mischief', kind='raspi') + hera_sit(530, 722, 0.98, 'smile') + csit(675, 705, 0.62, mood='silly', kind='neu')
    s += bee(330, 270, 0.9, -15) + butterfly(600, 250, 0.7)
    return pag(f'''
<div class="center" style="margin-top:.05in">
  <p style="margin:0 0 .04in;font-family:Fraunces;font-weight:700;font-size:15pt;letter-spacing:.18em;text-transform:uppercase">{VOLUMEN} de la serie Lúa</p>
  <h1 style="font-size:55pt;line-height:1.05;-webkit-text-stroke:2px #111;color:#fff">Lúa y el jardín<br>de todos</h1>
  <p style="font-family:Fraunces;font-weight:600;font-style:italic;font-size:16pt;margin:.14in 0 0">{SUBTITULO}</p>
</div>
<div class="art" style="margin-top:.1in">{svg(s, '0 0 750 740')}</div>
<p class="center" style="position:absolute;bottom:.45in;left:0;right:0;font-family:Fraunces;font-weight:600;font-size:14pt">Texto e ilustraciones: {AUTOR}</p>''')


def pagina_guia1():
    return pag(f'''<div class="note">
<h2>Para las familias</h2>
<p>Este cuento habla de algo que se ve en todos los patios: niños con ritmos y formas de ser muy distintas que tienen que aprender a convivir. Mientras colorean y escuchan la historia, les resulta más fácil contarte lo que sienten.</p>
<h3>Lo que trabaja cada personaje</h3>
<ul>
<li><b>Lúa</b> es buena en casi todo y cree que debe hacerlo todo sola. Aprende que pedir ayuda no es fracasar.</li>
<li><b>Raspi</b> es impaciente y curioso. Su travesura estropea algo y le cae un «siempre igual». La historia enseña a separar lo que alguien hace de lo que alguien es.</li>
<li><b>Neu</b> es la graciosa. Su humor no es una tontería: calma a quien tiene miedo y une al grupo.</li>
<li><b>Hera</b> es la mayor. Ser mayor no es ser inútil, es ser raíz: enseña, calma y planta para los que vendrán.</li>
</ul>
<h3>Cuatro ideas que se repiten</h3>
<ul>
<li><b>Cada uno a su tiempo.</b> Esperar cuesta, y se puede aprender.</li>
<li><b>Equivocarse es aprender.</b> Lo importante es reparar, no esconderse.</li>
<li><b>Lo que nos hace distintos es lo que el grupo necesita.</b> En la tormenta, cada uno salva el jardín a su manera.</li>
<li><b>Cuidar el entorno.</b> El jardín nace de un solar lleno de basura. Separar residuos, reutilizar latas como macetas, hacer compost, regar con agua de lluvia y no usar venenos son hábitos pequeños que se aprenden jugando.</li>
</ul>
<h3>Cómo usarlo, con 5 minutos al día</h3>
<ol>
<li>Leed una escena y mirad el dibujo. Preguntad antes de colorear: ¿qué siente?</li>
<li>Dejad que coloreen como quieran. Lúa puede ser gris, rosa o de rayas.</li>
<li>Haced juntos la actividad de la semilla: es la mejor forma de practicar la espera.</li>
</ol>
<p>En cada escena vuela Zum, la abeja. ¡Buscadla! Al final hay 20 páginas de pasatiempos para hacer solos o en familia. Van impresas por las dos caras: usad lápices o rotuladores finos.</p>
</div>''')


def pagina_guia2():
    return pag(f'''<div class="note">
<h2>Frases y preguntas</h2>
<h3>Frases que ayudan</h3>
<ul>
<li>Si le cuesta esperar: «Esperar cuesta. Mientras tanto, ¿qué podemos hacer?»</li>
<li>Si le ponen una etiqueta: «Haces cosas que a veces no salen bien, y eres mucho más que eso.»</li>
<li>Si quiere hacerlo todo perfecto y solo: «Pedir ayuda es una forma de ser valiente.»</li>
<li>Cuando se equivoca: «¿Cómo lo arreglamos juntos?»</li>
</ul>
<h3>Preguntas para conversar</h3>
<ul>
<li>¿Por qué desenterró Raspi las semillas? ¿Tú qué habrías hecho?</li>
<li>¿Cómo se sintió Raspi cuando Lúa le dijo «siempre igual»?</li>
<li>¿Quién salvó el jardín? ¿Hicieron todos lo mismo?</li>
<li>¿Qué cosa te hace especial a ti?</li>
<li>¿Conoces a alguien mayor que te haya enseñado algo?</li>
</ul>
<h3>Cuándo buscar ayuda</h3>
<p>Este libro es un apoyo para conversar en casa, no un tratamiento. Si tu hijo lleva semanas triste o muy retraído, evita ir al colegio o sufre burlas o agresiones repetidas, habla con su tutor o tutora y con su pediatra o un psicólogo infantil.</p>
<div class="legal">© {ANIO} {AUTOR}. Todos los derechos reservados. Prohibida la reproducción total o parcial de esta obra sin permiso del autor. Primera edición. {VOLUMEN} de la serie «Lúa».</div>
</div>''')


def pagina_personajes():
    s = f'<text x="375" y="52" {font(44, 700)} fill="#111">Conoce a los amigos</text>'
    s += csit(190, 340, 0.62, mood='happy') + hera_sit(565, 345, 0.66, 'smile')
    s += csit(190, 668, 0.62, mood='mischief', kind='raspi') + csit(565, 668, 0.62, mood='silly', kind='neu')
    for n, d, x, y in (('Lúa', 'la gatita gris, buena y ágil', 190, 385), ('Hera', 'la labradora mayor y sabia', 565, 385),
                       ('Raspi', 'la gata parda, traviesa e inventora', 190, 712), ('Neu', 'la gata blanca, juguetona y graciosa', 565, 712)):
        s += f'<text x="{x}" y="{y}" {font(34, 700)} fill="#111">{n}</text><text x="{x}" y="{y + 28}" {font(19, 600)} fill="#111">{d}</text>'
    return pag(f'<div class="art">{svg(s, "0 0 750 760")}</div>'
               f'<div class="txt"><p style="font-size:14pt">Y también: Nuez, Trébol, Mora, Mari, Pipa y Zum, la abeja, que se esconde en cada escena. ¡Buscadla!</p></div>')


def pagina_escena(i):
    zum = bee(*HIDDEN[i], 0.6, -12)
    return pag(f'<div class="art">{svg(SCENES[i]() + zum, "0 0 750 780", marco=True)}</div><div class="txt">{PAW}<p>{TEXTOS[i]}</p></div>')


def pagina_ciclo():
    s = f'<text x="375" y="52" {font(40, 700)} fill="#111">El viaje de una semilla</text>'
    for (x, y) in [(40, 90), (400, 90), (40, 400), (400, 400)]:
        s += f'<rect x="{x}" y="{y}" width="310" height="270" rx="22" fill="#fff" {ST} stroke-dasharray="2 12"/>'
    # mezclados a proposito: flor, semilla, brote, planta
    s += f'<path d="M60,330 Q195,300 330,330" fill="none" {ST}/>' + sunflower(195, 330, 0.9, 160)
    s += f'<path d="M420,330 Q555,300 690,330" fill="none" {ST}/>' + seed('bean', 555, 290, 1.2)
    s += f'<path d="M60,640 Q195,610 330,640" fill="none" {ST}/>' + stem(195, 640, 70, 8) + leaf(195, 590, 60, -30) + leaf(195, 590, 60, 210)
    s += f'<path d="M420,640 Q555,610 690,640" fill="none" {ST}/>' + stem(555, 640, 120, 9) + leaf(555, 590, 70, -35) + leaf(555, 570, 70, 215) + leaf(555, 535, 60, -30)
    for t, x, y in (('Flor', 70, 120), ('Semilla', 430, 120), ('Brote', 70, 430), ('Planta', 430, 430)):
        s += f'<circle cx="{x + 18}" cy="{y + 8}" r="22" fill="#fff" {ST}/>'
        s += f'<text x="{x + 66}" y="{y + 17}" {font(26, 700, "start")} fill="#111">{t}</text>'
    return pag(f'<div class="art">{svg(s, "0 0 750 700")}</div>'
               f'<div class="txt"><p style="font-size:15pt">Colorea cada dibujo. ¿En qué orden crece una semilla? Escribe 1, 2, 3 y 4 en cada círculo.</p></div>')


def pagina_aprendizaje():
    filas = [('lua', 'happy', 'Lúa aprendió a pedir ayuda.'), ('raspi', 'mischief', 'Raspi aprendió a esperar.'),
             ('neu', 'silly', 'Neu aprendió que reír también es un trabajo importante.'), ('hera', 'smile', 'Hera nos recordó que nunca es tarde para plantar algo bonito.')]
    filas_html = ''
    for kind, mood, texto in filas:
        if kind == 'hera':
            icon = svg(hera_sit(60, 112, 0.34, 'smile'), '0 0 120 120', False, 1.1)
        else:
            icon = svg(f'<g transform="translate(60,62) scale(0.5)">{cat_head(0.5, mood, 0, False, kind)}</g>', '0 0 120 120', False, 1.1)
        filas_html += (f'<div style="display:flex;align-items:center;gap:.15in;border:3px solid #111;border-radius:.2in;padding:.08in .15in;margin-bottom:.14in">'
                       f'<div style="width:1.1in;flex:none">{icon}</div>'
                       f'<div style="font-family:Fraunces;font-weight:600;font-size:16pt;line-height:1.3">{texto}</div></div>')
    return pag(f'<h2 class="center" style="font-size:28pt;margin-top:.05in">¿Qué aprendió cada amigo?</h2>'
               f'<p class="center" style="font-size:13pt;margin:.1in 0 .25in;font-family:Nunito;font-weight:700">Colorea a cada amigo y lee en voz alta lo que aprendió.</p>'
               f'{filas_html}'
               f'<p style="font-family:Fraunces;font-weight:600;font-size:16pt;margin-top:.2in">Y tú, ¿qué has aprendido?</p><div class="line"></div><div class="line"></div>')


def pagina_siembra():
    pasos = [('1', 'Moja un algodón y ponlo en un vaso.'), ('2', 'Coloca una judía entre el algodón y el cristal.'),
             ('3', 'Ponlo junto a una ventana con luz.'), ('4', 'Echa unas gotas de agua cada día y espera.')]
    lis = ''.join(f'<li style="margin:.07in 0"><b>{n}.</b> {t}</li>' for n, t in pasos)
    s = f'<text x="375" y="46" {font(36, 700)} fill="#111">Siembra tu propia judía</text>'
    # vaso + judia
    s += f'<path d="M270,130 L290,330 Q375,350 460,330 L480,130" fill="#fff" {ST}/><ellipse cx="375" cy="130" rx="105" ry="16" fill="#fff" {ST}/>'
    s += f'<path d="M300,240 Q340,210 380,240 Q420,215 450,245 L455,325 Q375,342 295,325 Z" fill="#fff" {ST}/>' + seed('bean', 400, 270, 0.42)
    s += f'<path d="M400,200 Q420,140 440,100" fill="none" {ST} stroke-width="3.4" stroke-dasharray="3 10"/>'
    for i, d in enumerate(('1', '3', '7', '10')):
        x = 45 + i * 170
        s += f'<rect x="{x}" y="420" width="150" height="190" rx="16" fill="#fff" {ST} stroke-dasharray="2 10"/>'
        s += f'<text x="{x + 75}" y="650" {font(24, 700)} fill="#111">Día {d}</text>'
    return pag(f'<div class="art">{svg(s, "0 0 750 670")}</div><div class="note"><ol style="list-style:none;padding:0;margin:.02in 0">{lis}</ol>'
               f'<p style="font-size:12pt">Dibuja cómo va creciendo en cada cuadro. Hazlo con un adulto, lávate las manos y no te comas las semillas.</p></div>')


def _eco_t(x, y, t):
    return f'<text x="{x}" y="{y + 8}" {font(20, 600, "start")} fill="#111">{t}</text>'


def pagina_eco():
    s = f'<text x="375" y="46" {font(34, 700)} fill="#111">¿Dónde va cada cosa?</text>'
    items = ['periódico', 'botella de plástico', 'tarro de cristal', 'cáscara de plátano', 'lata']
    for i, n in enumerate(items):
        y = 130 + i * 118
        if n == 'periódico':
            s += f'<rect x="90" y="{y - 30}" width="86" height="64" fill="#fff" {ST}/><path d="M100,{y - 14} L166,{y - 14} M100,{y} L166,{y} M100,{y + 14} L150,{y + 14}" fill="none" {ST} stroke-width="3"/>'
        elif n == 'botella de plástico':
            s += f'<path d="M120,{y - 38} L146,{y - 38} L146,{y - 22} Q166,{y - 8} 166,{y + 8} L166,{y + 36} L100,{y + 36} L100,{y + 8} Q120,{y - 8} 120,{y - 22} Z" fill="#fff" {ST}/>'
        elif n == 'tarro de cristal':
            s += f'<rect x="104" y="{y - 30}" width="56" height="64" rx="10" fill="#fff" {ST}/><rect x="100" y="{y - 40}" width="64" height="14" rx="4" fill="#fff" {ST}/>'
        elif n == 'cáscara de plátano':
            s += banana_peel(98, y + 10, 1.0)
        else:
            s += tin_can(132, y + 4, 1.3)
        s += _eco_t(205, y + 4, n) + f'<circle cx="470" cy="{y}" r="9" fill="#fff" {ST}/>'
    for i, (lab, col) in enumerate((('PAPEL', 'azul'), ('ENVASES', 'amarillo'), ('VIDRIO', 'verde'), ('ORGÁNICO', 'marrón'))):
        y = 190 + i * 150
        s += bin_(660, y + 62, 0.8, lab) + f'<circle cx="545" cy="{y + 10}" r="9" fill="#fff" {ST}/>'
    return pag(f'<div class="art">{svg(s, "0 0 750 720")}</div><div class="txt"><p style="font-size:13pt;font-family:Nunito;font-weight:700">Une cada cosa con su contenedor y coloréalos: azul para papel, amarillo para envases, verde para vidrio y marrón para lo orgánico. En tu ciudad los colores pueden variar. Respuestas para adultos: periódico, azul; botella y lata, amarillo; tarro, verde; cáscara, marrón.</p></div>')


def pagina_jardin():
    s = f'<text x="375" y="54" {font(40, 700)} fill="#111">Mi jardín de todos</text>'
    s += f'<rect x="50" y="95" width="650" height="520" rx="30" fill="#fff" {ST} stroke-dasharray="2 14"/>'
    s += sun(120, 170, 24) + sunflower(640, 610, 0.6, 140) + daisy(580, 610, .8, 100) + flower(95, 600, 0.8)
    return pag(f'<div class="art">{svg(s, "0 0 750 670")}</div>'
               f'<div class="txt" style="text-align:left"><p style="font-size:15pt;font-family:Nunito;font-weight:700">En mi jardín viven:</p><div class="line"></div></div>')


def pagina_diploma():
    s = f'<rect x="20" y="20" width="710" height="660" rx="30" fill="none" {ST} stroke-width="8"/>'
    s += f'<rect x="42" y="42" width="666" height="616" rx="20" fill="none" {ST} stroke-dasharray="3 12"/>'
    s += daisy(95, 120, 0.7, 40) + daisy(655, 120, 0.7, 40)
    s += outlined_text(375, 150, 'DIPLOMA', 80)
    s += f'<text x="375" y="198" {font(25, 600)} fill="#111">de jardinero o jardinera del jardín de todos</text>'
    s += f'<path d="M150,290 L600,290" {ST} stroke-width="4"/><text x="375" y="325" {font(21, 600)} fill="#111">(escribe aquí tu nombre)</text>'
    prom = ['Cuidaré a mis amigos aunque sean muy distintos a mí.', 'Esperaré a que cada cosa crezca a su tiempo.',
            'Pediré ayuda cuando la necesite y la daré cuando pueda.']
    for i, p in enumerate(prom):
        s += star(100, 392 + i * 50, 13) + f'<text x="130" y="{399 + i * 50}" {font(23, 600, "start")} fill="#111">{p}</text>'
    s += f'<g transform="translate(140,575) scale(.3)">{cat_head(.3, "happy")}</g>' + f'<g transform="translate(610,575) scale(.3)">{cat_head(.3, "silly", 0, False, "neu")}</g>'
    s += f'<path d="M230,610 L370,610 M390,610 L530,610" {ST} stroke-width="4"/><text x="300" y="640" {font(18, 600)} fill="#111">Mi firma</text><text x="460" y="640" {font(18, 600)} fill="#111">Un adulto que me quiere</text>'
    return pag(f'<div style="margin-top:.35in">{svg(s, "0 0 750 700")}</div>')


def pasatiempos():
    cast = [dict(name='Lúa', fig=lambda cx, g, s: csit(cx, g, s, mood='happy'), h=402, like='pez'),
            dict(name='Hera', fig=lambda cx, g, s: hera_sit(cx, g, s, 'smile'), h=335, like='hueso'),
            dict(name='Raspi', fig=lambda cx, g, s: csit(cx, g, s, mood='mischief', kind='raspi'), h=402, like='ovillo'),
            dict(name='Neu', fig=lambda cx, g, s: csit(cx, g, s, mood='silly', kind='neu'), h=402, like='pelota')]
    sombra_cast = [dict(name='Hera', fig=lambda cx, g, s: hera_sit(cx, g, s, 'smile'), h=335),
                   dict(name='Nuez', fig=lambda cx, g, s: squirrel(cx, g, s, 'happy'), h=300),
                   dict(name='Trébol', fig=lambda cx, g, s: rabbit(cx, g, s, 'happy'), h=325),
                   dict(name='Pipa', fig=lambda cx, g, s: bird(cx, g, s, 'happy'), h=150)]
    cfg = dict(cast=cast, sombra_cast=sombra_cast, hat_name='Neu', words=['LUA', 'HERA', 'RASPI', 'NEU', 'FLOR', 'SEMILLA', 'JARDIN', 'AMIGOS'],
               head_main=lambda cx, cy, s, mood: f'<g transform="translate({cx},{cy}) scale({s})">{cat_head(s, mood)}</g>',
               head_hat=lambda cx, cy, s: f'<g transform="translate({cx},{cy}) scale({s})">{cat_head(s, "silly", 0, False, "neu")}</g>',
               hero_sit=lambda cx, g, s, mood: csit(cx, g, s, mood=mood),
               story=[SCENES[0], SCENES[7], SCENES[17], SCENES[18]],
               retos=['Recoge tres cosas del suelo y échalas al contenedor.', 'Cierra el grifo mientras te cepillas los dientes.', 'Convierte un bote o una lata en maceta.', 'Riega una planta con agua que hayas guardado.', 'Apaga la luz de una habitación vacía.', 'Planta una semilla y ponle nombre.', 'Huele tres flores y mira quién las visita.', 'Cuenta cuántos colores de hoja encuentras.', 'Abraza a un árbol, de verdad.', 'Dale las gracias a alguien, mirándole a los ojos.'],
               extra=dict(bee=bee, snail=snail, tin_can=tin_can, rocks=rocks, sprout=sprout, leaf=leaf))
    return build_pasatiempos(cfg, TITULO)


def interior():
    p = [pagina_titulo(), BLANCO, pagina_guia1(), pagina_guia2(), pagina_personajes(), BLANCO]
    for i in range(len(SCENES)):
        p += [pagina_escena(i), BLANCO]
    p += [pagina_ciclo(), BLANCO, pagina_aprendizaje(), BLANCO, pagina_siembra(), BLANCO, pagina_eco(), BLANCO, pagina_jardin(), BLANCO, pagina_diploma(), BLANCO] + pasatiempos()
    assert len(p) == PAGINAS_TOTAL, len(p)
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{TITULO}</title><style>{CSS}</style></head><body>{"".join(p)}</body></html>'


# ----------------------------------------------------------------- cubierta
COLORES = {
    'cat_body': '#9ea8b5', 'cat_belly': '#e1e6ec', 'cat_inner': '#f4b5c5', 'nose': '#ee7f98', 'eye': '#8bd36b',
    'mouth': '#ef6b86', 'blush': '#f8b4c0', 'tongue': '#ff8fa8',
    'raspi_body': '#b88a5c', 'raspi_belly': '#e8d3b8', 'neu_body': '#fbfbfb', 'neu_belly': '#ffffff',
    'hera_body': '#6a3d2a', 'hera_light': '#8b5a3f', 'hera_gray': '#cdbcae', 'hera_collar': '#e53935', 'hera_tag': '#ffd23f', 'hera_dark': '#2b1d17',
    'sq_body': '#e0873a', 'sq_light': '#f7dcb4', 'acorn': '#c68545', 'acorn_cap': '#8a5a2b',
    'rb_body': '#f6efe6', 'rb_inner': '#f5b5c4', 'rb_belly': '#fffaf3', 'lb_shell': '#e53935', 'lb_head': '#2b2b33', 'lb_dot': '#2b2b33',
    'bf_w1': '#ffb300', 'bf_w2': '#8e6bd8', 'bf_body': '#5a4636', 'bd_body': '#3fa7e8', 'bd_light': '#cfeaff', 'beak': '#ffb300',
    'fl_petal': '#ffc928', 'fl_mid': '#7a4a22', 'leaf': '#6cc24a', 'stem': '#5fb246', 'lav': '#b79af0', 'bee': '#ffd23f', 'apple': '#e53935',
}


def cubierta():
    A.COLORS.update(COLORES)
    spine = PAGINAS_TOTAL * GROSOR_PAPEL
    Wi, Hi = 2 * 8.5 + spine + 0.25, 11.25
    u = 100
    Wu, Hu = round(Wi * u), round(Hi * u)
    sx, sw = round((0.125 + 8.5) * u), round(spine * u)
    fx = sx + sw
    cx0 = fx + 425
    s = f'<rect width="{Wu}" height="{Hu}" fill="#c8ebff"/>'
    s += f'<path d="M0,{Hu - 250} Q{Wu * .25},{Hu - 300} {Wu * .5},{Hu - 240} T{Wu},{Hu - 255} L{Wu},{Hu} L0,{Hu} Z" fill="#8fd46b"/>'
    s += f'<rect x="{sx}" y="0" width="{sw}" height="{Hu}" fill="#ffd23f"/>'
    s += f'<circle cx="{fx + 95}" cy="125" r="52" fill="#fff6a8"/>'
    s += f'<path d="M{fx + 520},95 q20,-45 70,-30 q30,-35 70,-5 q40,-5 40,35 q-20,25 -60,15 q-30,20 -70,5 q-45,10 -50,-20z" fill="#fff"/>'
    t = lambda y, txt, sz, col: (f'<text x="{cx0}" y="{y}" font-family="Fraunces" font-weight="700" font-size="{sz}" fill="{col}" stroke="#23232b" '
                                 f'stroke-width="9" paint-order="stroke" stroke-linejoin="round" text-anchor="middle">{txt}</text>')
    s += (f'<text x="{cx0}" y="125" font-family="Fraunces" font-weight="700" font-size="36" fill="#fff" stroke="#23232b" stroke-width="8" '
          f'paint-order="stroke" stroke-linejoin="round" text-anchor="middle" letter-spacing="6">VOLUMEN II</text>')
    s += t(228, 'Lúa y el', 92, '#fff') + t(322, 'jardín de todos', 92, '#ffd23f')
    s += f'<rect x="{cx0 - 300}" y="338" width="600" height="54" rx="27" fill="#fff" stroke="#23232b" stroke-width="4"/>'
    s += f'<text x="{cx0}" y="376" font-family="Fraunces" font-weight="600" font-size="25" text-anchor="middle" fill="#23232b">Para colorear · 4 a 8 años · Con guía para familias</text>'
    s += fence(fx + 10, fx + 840, 800, 90)
    for x in (fx + 70, fx + 780):
        s += sunflower(x, 960, 1.15, 230)
    for x in (fx + 160, fx + 690):
        s += lavender(x, 980, 1.1, 170)
    s += csit(cx0 - 150, 1010, 1.0, mood='happy') + hera_sit(cx0 + 170, 1020, 1.1, 'smile')
    s += csit(cx0 - 20, 1010, 0.62, mood='mischief', kind='raspi') + csit(cx0 + 60, 1015, 0.55, mood='silly', kind='neu')
    s += bee(cx0 - 250, 560, 1.3, -15) + butterfly(cx0 + 250, 560, 0.8)
    s += f'<text x="{cx0}" y="1100" font-family="Fraunces" font-weight="700" font-size="34" text-anchor="middle" fill="#23232b">{AUTOR}</text>'
    bx0 = 12 + 425
    s += f'<rect x="{bx0 - 330}" y="120" width="660" height="520" rx="30" fill="#fff" fill-opacity=".94" stroke="#23232b" stroke-width="5"/>'
    lineas = ['Volumen II de la serie Lúa', 'Un solar abandonado, cuatro amigos', 'muy distintos y un montón de semillas.', 'Lúa, Hera, Raspi y Neu descubren que',
              'cada uno crece a su tiempo y que el', 'jardín es más bonito cuando cabe todo', 'el mundo. Y que cuidar el planeta', 'empieza en un solar.', 'Con guía para familias.']
    for i, l in enumerate(lineas):
        s += f'<text x="{bx0}" y="{185 + i * 46}" font-family="Fraunces" font-weight="600" font-size="29" text-anchor="middle" fill="#23232b">{l}</text>'
    s += csit(bx0 - 140, 1000, 0.7, mood='joy') + hera_sit(bx0 + 150, 1005, 0.75, 'smile')
    s += f'<rect x="{round((0.125 + 8.5 - 0.25 - 2) * u)}" y="{round((0.125 + 11 - 0.25 - 1.2) * u)}" width="200" height="120" fill="#fff"/>'
    A.COLORS.clear()
    css = CSS.replace('@page{size:8.5in 11in;margin:0}', '@page{size:%.4fin %.4fin;margin:0}' % (Wi, Hi))
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{css}body{{margin:0}} '
            f'svg{{width:{Wi:.4f}in;height:{Hi:.4f}in;display:block}}</style></head><body>'
            f'<svg viewBox="0 0 {Wu} {Hu}" xmlns="http://www.w3.org/2000/svg">{s}</svg></body></html>')


if __name__ == '__main__':
    open(os.path.join(AQUI, 'interior.html'), 'w').write(interior())
    open(os.path.join(AQUI, 'portada.html'), 'w').write(cubierta())
    print('ok', PAGINAS_TOTAL, 'paginas; lomo %.3f in' % (PAGINAS_TOTAL * GROSOR_PAPEL))
