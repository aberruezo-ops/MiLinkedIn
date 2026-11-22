# Genera interior.html (miolo del libro) y portada.html (cubierta completa para KDP).
import os, sys
from lib import *
from escenas import SCENES, TEXTOS, P

# ---- datos editables ---------------------------------------------------
TITULO = 'Teo y las pelotas de colores'
SUBTITULO = 'Un cuento para colorear sobre aceptar a los demás'
AUTOR = 'TU NOMBRE'
ANIO = '2026'
PAGINAS_TOTAL = 40            # debe coincidir con el interior generado
GROSOR_PAPEL = 0.002252       # pulgadas por pagina, papel blanco KDP (verificar con la calculadora de KDP)
# -------------------------------------------------------------------------

AQUI = os.path.dirname(os.path.abspath(__file__))

CSS = """
@font-face{font-family:'Fredoka';font-weight:600;src:url('fonts/fredoka-latin-600-normal.woff2')}
@font-face{font-family:'Fredoka';font-weight:700;src:url('fonts/fredoka-latin-700-normal.woff2')}
@font-face{font-family:'Nunito';font-weight:400;src:url('fonts/nunito-latin-400-normal.woff2')}
@font-face{font-family:'Nunito';font-weight:700;src:url('fonts/nunito-latin-700-normal.woff2')}
@font-face{font-family:'Nunito';font-weight:800;src:url('fonts/nunito-latin-800-normal.woff2')}
@page{size:8.5in 11in;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#fff;color:#111;font-family:'Nunito',sans-serif}
.page{width:8.5in;height:11in;padding:.5in;position:relative;overflow:hidden;page-break-after:always;break-after:page}
.art svg{width:7.5in;height:7in;display:block}
.txt{margin-top:.15in}
.num{display:inline-flex;width:.5in;height:.5in;border:3px solid #111;border-radius:50%;align-items:center;justify-content:center;font-family:'Fredoka';font-weight:700;font-size:20pt;float:left;margin:.02in .18in 0 0}
.txt p{margin:0;font-size:18pt;line-height:1.32;font-weight:700}
.txt .q{margin-top:.16in;font-size:15.5pt;font-weight:800;padding:.1in .18in;border:3px dashed #111;border-radius:.18in;clear:both}
h1,h2,h3{font-family:'Fredoka';font-weight:700;margin:0}
.note h2{font-size:26pt;margin-bottom:.2in}
.note h3{font-size:16pt;margin:.22in 0 .06in}
.note p,.note li{font-size:12.5pt;line-height:1.45;margin:.05in 0}
.note ul,.note ol{margin:.04in 0;padding-left:.28in}
.note .legal{position:absolute;left:.5in;right:.5in;bottom:.5in;font-size:9.5pt;line-height:1.4;border-top:2px solid #111;padding-top:.1in}
.center{text-align:center}
.line{border-bottom:3px solid #111;height:.5in;margin:.05in 0}
"""


def svg(inner, vb='0 0 750 700'):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'


def pag(html, cls=''):
    return f'<section class="page {cls}">{html}</section>'


BLANCO = pag('')


def pagina_titulo():
    s = sun(90, 95, 38) + cloud(560, 40, 130)
    s += hill(560)
    names = ['Rita', 'Sol', 'Teo', 'Mar', 'Lola', 'Nano']
    xs = [75, 195, 315, 435, 555, 675]
    r = 40
    for i, (x, n) in enumerate(zip(xs, names)):
        left = 'up' if i == 0 else (x - 30, stand(r, 660) + 22)
        right = 'up' if i == 5 else (x + 30, stand(r, 660) + 22)
        s += P(n, x, 660, r, mood='happy', arms=(left, right))
    s += rainbow(375, 450, 300, 4, 28)
    s += star(70, 330, 14) + star(680, 340, 14)
    return pag(f'''
<div class="center" style="margin-top:.1in">
  <h1 style="font-size:56pt;line-height:1.05;-webkit-text-stroke:2px #111;color:#fff">Teo y las<br>pelotas de colores</h1>
  <p style="font-family:Fredoka;font-weight:600;font-size:16pt;margin:.14in 0 0">{SUBTITULO}</p>
</div>
<div class="art" style="margin-top:.2in">{svg(s, '0 0 750 720')}</div>
<p class="center" style="position:absolute;bottom:.5in;left:0;right:0;font-family:Fredoka;font-weight:600;font-size:15pt">Texto e ilustraciones: {AUTOR}</p>''')


def pagina_nota():
    return pag(f'''<div class="note">
<h2>Nota para madres, padres y docentes</h2>
<p>Este libro cuenta cómo Teo, una pelota negra, llega a un grupo de pelotas de colores y es rechazada por ser diferente. Hasta que un día las demás descubren lo que Teo tenía de igual que ellas. Está pensado para niñas y niños de 4 a 8 años y sirve para hablar de inclusión, empatía y respeto mientras se colorea.</p>
<h3>Cómo usarlo</h3>
<ol>
<li>Leed una escena cada vez, en voz alta.</li>
<li>Dejad que coloreen con calma. Pintar ayuda a que la idea se quede.</li>
<li>Haced la pregunta del recuadro y escuchad la respuesta sin corregirla.</li>
</ol>
<h3>Ideas para conversar</h3>
<ul>
<li>¿Alguna vez te dejaron fuera de un juego? ¿Cómo te sentiste?</li>
<li>¿Qué cosas tenemos todos en común, aunque seamos distintos?</li>
<li>¿Qué puedes hacer cuando llegue alguien nuevo a tu clase?</li>
</ul>
<h3>Antes de empezar</h3>
<p>Los personajes se pueden pintar del color que cada niño elija. La parte de atrás de cada dibujo está en blanco para que los rotuladores no estropeen la página siguiente.</p>
<div class="legal">© {ANIO} {AUTOR}. Todos los derechos reservados. Prohibida la reproducción total o parcial de esta obra sin permiso del autor. Primera edición.</div>
</div>''')


def pagina_personajes():
    s = f'<text x="375" y="60" {font(46, 700)} fill="#111">Conoce a los amigos</text>'
    pos = [('Rita', 'la roja', 130, 330), ('Sol', 'la amarilla', 375, 330), ('Mar', 'la azul', 620, 330),
           ('Lola', 'la verde', 130, 640), ('Nano', 'el naranja', 375, 640), ('Teo', 'la negra', 620, 640)]
    for n, d, x, g in pos:
        r = 62
        s += P(n, x, g - 60, r, mood='happy', arms=('up', 'down') if n != 'Teo' else ('down', 'up'))
        s += f'<text x="{x}" y="{g + 10}" {font(36, 700)} fill="#111">{n}</text>'
        s += f'<text x="{x}" y="{g + 40}" {font(22, 600)} fill="#111">{d}</text>'
    return pag(f'<div class="art">{svg(s, "0 0 750 700")}</div>'
               f'<div class="txt"><p class="center" style="font-size:15pt">Pinta a cada amigo como quieras. ¿Quién es tu favorito?</p></div>')


def pagina_escena(i):
    texto, preg = TEXTOS[i]
    return pag(f'<div class="art">{svg(SCENES[i]())}</div>'
               f'<div class="txt"><span class="num">{i + 1}</span><p>{texto}</p>'
               f'<p class="q">Para pensar: {preg}</p></div>')


def pagina_emociones():
    s = f'<text x="375" y="60" {font(44, 700)} fill="#111">Las emociones de Teo</text>'
    datos = [('happy', 'Alegría'), ('sad', 'Tristeza'), ('worried', 'Miedo'), ('angry', 'Enfado'),
             ('open', 'Sorpresa'), ('smile', 'Calma')]
    for i, (m, nom) in enumerate(datos):
        x = 130 + (i % 3) * 245
        y = 215 + (i // 3) * 270
        s += ball(x, y, 82, mood=m, deco='none', arms=(None, None), legs=False, tear=(m == 'sad'))
        s += f'<text x="{x}" y="{y + 130}" {font(34, 700)} fill="#111">{nom}</text>'
    return pag(f'<div class="art">{svg(s)}</div>'
               f'<div class="txt"><p class="q" style="margin-top:0">Colorea cada cara. Después cuéntale a un adulto cuándo te has sentido así.</p></div>')


def pagina_amigo():
    s = f'<text x="375" y="60" {font(44, 700)} fill="#111">Dibuja a un amigo diferente a ti</text>'
    s += f'<rect x="60" y="100" width="630" height="520" rx="30" fill="#fff" {ST} stroke-dasharray="2 14"/>'
    s += star(95, 135, 20) + star(655, 135, 20) + heart(95, 585, 0.4) + heart(655, 585, 0.4)
    return pag(f'<div class="art">{svg(s)}</div>'
               f'<div class="txt"><p>Se llama:</p><div class="line"></div>'
               f'<p style="margin-top:.1in">Lo que más me gusta de él o de ella es:</p><div class="line"></div></div>')


def pagina_valores():
    vals = [('Respeto', 'Tratar bien a todos, aunque sean diferentes.', 'smile', 'star'),
            ('Empatía', 'Sentir lo que siente el otro.', 'sad', 'heart'),
            ('Amistad', 'Estar a su lado cuando te necesita.', 'happy', 'heart'),
            ('Valentía', 'Ayudar aunque dé un poco de miedo.', 'happy', 'star'),
            ('Perdón', 'Reconocer un error y arreglarlo.', 'sorry', 'dots'),
            ('Inclusión', 'Hacer sitio a todos en el juego.', 'happy', 'stripes')]
    cards = ''
    for n, d, m, deco in vals:
        icon = svg(ball(60, 62, 46, mood=m, deco=deco, arms=(None, None), legs=False), '0 0 120 120')
        cards += (f'<div style="display:flex;align-items:center;gap:.12in;border:3px solid #111;border-radius:.2in;padding:.1in .15in">'
                  f'<div style="width:1.1in;flex:none">{icon}</div>'
                  f'<div><div style="font-family:Fredoka;font-weight:700;font-size:20pt">{n}</div>'
                  f'<div style="font-size:14pt;font-weight:700;line-height:1.3">{d}</div></div></div>')
    return pag(f'<h2 class="center" style="font-size:30pt;margin-top:.05in">Los valores de Teo</h2>'
               f'<p class="center" style="font-size:13pt;margin:.1in 0 .3in;font-weight:700">Colorea cada cara y lee en voz alta lo que significa.</p>'
               f'<div style="display:grid;grid-template-columns:1fr;gap:.14in">{cards}</div>')


def pagina_diploma():
    s = f'<rect x="20" y="20" width="710" height="660" rx="30" fill="none" {ST} stroke-width="8"/>'
    s += f'<rect x="42" y="42" width="666" height="616" rx="20" fill="none" {ST} stroke-dasharray="3 12"/>'
    s += star(95, 95, 26) + star(655, 95, 26) + star(95, 605, 26) + star(655, 605, 26)
    s += outlined_text(375, 150, 'DIPLOMA', 80)
    s += f'<text x="375" y="205" {font(28, 600)} fill="#111">de amigo que acepta a los demás</text>'
    s += f'<path d="M150,300 L600,300" {ST} stroke-width="4"/>'
    s += f'<text x="375" y="335" {font(22, 600)} fill="#111">(escribe aquí tu nombre)</text>'
    prom = ['Trataré bien a todos, sean como sean.', 'Haré sitio en el juego a quien llegue nuevo.',
            'Pediré perdón cuando me equivoque.']
    for i, p in enumerate(prom):
        s += star(130, 400 + i * 50, 14) + f'<text x="165" y="{407 + i * 50}" {font(26, 600, "start")} fill="#111">{p}</text>'
    s += P('Teo', 140, 665, 28, mood='happy', arms=('up', 'up')) if False else ''
    s += ball(150, 585, 26, mood='happy', deco='heart', arms=('up', 'up'), legs=False)
    s += ball(600, 585, 26, mood='happy', deco='star', arms=('up', 'up'), legs=False)
    s += f'<path d="M300,610 L450,610" {ST} stroke-width="4"/><text x="375" y="640" {font(20, 600)} fill="#111">Firma</text>'
    return pag(f'<div style="margin-top:.35in">{svg(s)}</div>')


def interior():
    p = [pagina_titulo(), BLANCO, pagina_nota(), BLANCO, pagina_personajes(), BLANCO]
    for i in range(13):
        p += [pagina_escena(i), BLANCO]
    p += [pagina_emociones(), BLANCO, pagina_amigo(), BLANCO, pagina_valores(), BLANCO, pagina_diploma(), BLANCO]
    assert len(p) == PAGINAS_TOTAL, len(p)
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{TITULO}</title><style>{CSS}</style></head><body>{"".join(p)}</body></html>'


# ----------------------------------------------------------------- cubierta
COL = {'Rita': '#ef4b4b', 'Sol': '#ffd23f', 'Mar': '#3fa7e8', 'Lola': '#5cc85c', 'Nano': '#ff9a2e', 'Teo': '#23232b'}


def cb(name, cx, g, r, **kw):
    deco = {'Rita': 'stripes', 'Sol': 'dots', 'Mar': 'waves', 'Lola': 'star', 'Nano': 'zig', 'Teo': 'heart'}[name]
    ink = '#fff' if name == 'Teo' else INK
    return ball(cx, stand(r, g), r, deco=deco, fill=COL[name], ink=ink, shoe='#fff', **kw)


def cubierta():
    spine = PAGINAS_TOTAL * GROSOR_PAPEL
    W = 2 * 8.5 + spine + 0.25
    H = 11 + 0.25
    u = 100  # unidades por pulgada
    Wu, Hu = round(W * u), round(H * u)
    xs = round(spine * u)
    front_x = round((0.125 + 8.5 + spine) * u)  # inicio del frente (con corte)
    # fondo
    s = f'<rect width="{Wu}" height="{Hu}" fill="#bfe6ff"/>'
    s += f'<path d="M0,{Hu - 190} Q{Wu * .25},{Hu - 230} {Wu * .5},{Hu - 190} T{Wu},{Hu - 195} L{Wu},{Hu} L0,{Hu} Z" fill="#8fd46b"/>'
    s += f'<rect x="{round((0.125 + 8.5) * u)}" y="0" width="{xs}" height="{Hu}" fill="#ffd23f"/>'
    # ---- frente
    fx = front_x
    fw = round(8.5 * u) + 12
    cx0 = fx + 425
    for i, c in enumerate(['#ef4b4b', '#ff9a2e', '#ffd23f', '#5cc85c', '#3fa7e8']):
        r = 330 - i * 28
        s += f'<path d="M{cx0 - r},560 A{r},{r} 0 0 1 {cx0 + r},560" fill="none" stroke="{c}" stroke-width="28"/>'
    s += f'<circle cx="{fx + 90}" cy="130" r="55" fill="#fff6a8"/>'
    s += f'<path d="M{fx + 520},95 q20,-45 70,-30 q30,-35 70,-5 q40,-5 40,35 q-20,25 -60,15 q-30,20 -70,5 q-45,10 -50,-20z" fill="#fff"/>'
    s += (f'<text x="{cx0}" y="160" {font(72, 700)} fill="#fff" stroke="#23232b" stroke-width="10" paint-order="stroke" stroke-linejoin="round">TEO Y LAS</text>'
          f'<text x="{cx0}" y="245" {font(72, 700)} fill="#fff" stroke="#23232b" stroke-width="10" paint-order="stroke" stroke-linejoin="round">PELOTAS DE</text>'
          f'<text x="{cx0}" y="330" {font(82, 700)} fill="#ffd23f" stroke="#23232b" stroke-width="10" paint-order="stroke" stroke-linejoin="round">COLORES</text>')
    s += f'<rect x="{cx0 - 300}" y="360" width="600" height="56" rx="28" fill="#fff" stroke="#23232b" stroke-width="4"/>'
    s += f'<text x="{cx0}" y="400" {font(28, 700)} fill="#23232b">Libro para colorear · 4 a 8 años</text>'
    names = ['Rita', 'Sol', 'Teo', 'Mar', 'Lola', 'Nano']
    xs_b = [fx + 95 + k * 133 for k in range(6)]
    r = 52
    for i, (x, n) in enumerate(zip(xs_b, names)):
        left = 'up' if i == 0 else (x - 40, stand(r, 960) + 30)
        right = 'up' if i == 5 else (x + 40, stand(r, 960) + 30)
        s += cb(n, x, 960, r, mood='happy', arms=(left, right))
    s += f'<text x="{cx0}" y="1070" {font(34, 700)} fill="#23232b">{AUTOR}</text>'
    # ---- reverso
    bx0 = 12 + 425
    s += f'<rect x="{bx0 - 330}" y="140" width="660" height="470" rx="30" fill="#fff" fill-opacity=".92" stroke="#23232b" stroke-width="5"/>'
    lineas = ['Teo es una pelota negra que llega', 'a un cajón de juguetes lleno de pelotas', 'de colores. Al principio no la dejan',
              'jugar. Pero un día, todas descubren', 'lo que tenían en común.', '', 'Un cuento para colorear que ayuda a hablar',
              'de respeto, empatía e inclusión.']
    for i, l in enumerate(lineas):
        s += f'<text x="{bx0}" y="{205 + i * 46}" {font(30, 600)} fill="#23232b">{l}</text>'
    s += cb('Teo', bx0 - 150, 900, 60, mood='happy') + cb('Sol', bx0 + 150, 900, 60, mood='happy')
    # hueco para el codigo de barras de KDP (2 x 1.2 in) abajo a la derecha
    s += f'<rect x="{round((0.125 + 8.5 - 0.25 - 2) * u)}" y="{round((0.125 + 11 - 0.25 - 1.2) * u)}" width="200" height="120" fill="#fff"/>'
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS.replace("@page{size:8.5in 11in;margin:0}", "@page{size:%.4fin %.4fin;margin:0}" % (W, H))}'
            f'body{{margin:0}} svg{{width:{W:.4f}in;height:{H:.4f}in;display:block}}</style></head><body>'
            f'<svg viewBox="0 0 {Wu} {Hu}" xmlns="http://www.w3.org/2000/svg">{s}</svg></body></html>')


if __name__ == '__main__':
    open(os.path.join(AQUI, 'interior.html'), 'w').write(interior())
    open(os.path.join(AQUI, 'portada.html'), 'w').write(cubierta())
    print('ok', PAGINAS_TOTAL, 'paginas; lomo %.3f in' % (PAGINAS_TOTAL * GROSOR_PAPEL))
