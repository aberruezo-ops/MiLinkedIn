# Añade el campo "enlaces" ([{t, u}]) a los JSON de la parrilla: todo el material de cada fila.
# Uso: python3 datos-parrilla/gen-enlaces.py   (desde synergos/). Si una fila ya existe, se reescribe su lista de enlaces.
import json, os
BASE = 'https://github.com/aberruezo-ops/MiLinkedIn'
RAMA = 'claude/linkedin-skills-guide-o8dp6v'
G = lambda p: f'{BASE}/blob/{RAMA}/synergos/{p}'
T = lambda p: f'{BASE}/tree/{RAMA}/synergos/{p}'
LI = lambda urn: f'https://www.linkedin.com/feed/update/{urn}'
PM = lambda p: f'https://media.publora.com/{p}'
PULSE = {
 'AR1': 'https://www.linkedin.com/pulse/crecer-la-vez-los-mimbres-de-synerg%C3%B3s-alejandro-berruezo-m%C3%A1rquez-tl1ie/',
 'AR2': 'https://www.linkedin.com/pulse/el-mapa-de-lo-que-nadie-escribi%C3%B3-alejandro-berruezo-m%C3%A1rquez-gxrze/',
 'AR3': 'https://www.linkedin.com/pulse/la-bola-negra-qui%C3%A9n-decide-cabe-alejandro-berruezo-m%C3%A1rquez-aybee/',
 'AR4': 'https://www.linkedin.com/pulse/acelera-automatiza-o-aumenta-alejandro-berruezo-m%C3%A1rquez-ydp9e'}
BACKLOG = ('Banco y calendario de posts', G('03-backlog-posts.md'))
def l(t, u): return {'t': t, 'u': u}
SYN = {
 '2026-10-27': [l('Post de presentación en LinkedIn', LI('urn:li:share:7520748674851917824')), l('Artículo en LinkedIn', PULSE['AR1']), l('Texto del artículo', G('articulos/01-los-mimbres.md'))],
 '2026-10-28': [l('En LinkedIn', LI('urn:li:share:7521111054538514432')), l('Texto', G('posts/2026-10-28-B6.md'))],
 '2026-10-29': [l('En LinkedIn', LI('urn:li:share:7521473452176867329')), l('Texto', G('posts/2026-10-29-B1.md')), l('Tarjeta', G('imagenes/tarjeta-B1.png'))],
 '2026-11-02': [l('Artículo en LinkedIn', PULSE['AR2']), l('Texto del artículo', G('articulos/02-el-mapa.md')), l('Portada', G('imagenes/portada-articulo-02.png')), l('Vídeo', G('imagenes/anim-articulo-02.mp4'))],
 '2026-11-03': [l('En LinkedIn', LI('urn:li:ugcPost:7523285369702731777')), l('Texto', G('posts/2026-11-03-B12-propuesta.md')), l('Vídeo', PM('videos/1793395946794-anim-infografia-B12.mp4'))],
 '2026-11-04': [l('En LinkedIn', LI('urn:li:ugcPost:7523647746566791168')), l('Texto', G('posts/2026-11-04-C12.md')), l('Vídeo', PM('videos/1793463828148-0-7d427c27-212ac430-71d9-4d06-a906-cdc8731c3b65.mp4'))],
 '2026-11-05': [l('En LinkedIn', LI('urn:li:ugcPost:7524010142628114433')), l('Texto', G('posts/2026-11-05-B13.md')), l('Vídeo', PM('videos/1793704458722-anim-infografia-B13.mp4')), l('Previsualización', G('previsualizaciones/2026-11-05-B13.html'))],
 '2026-11-06': [l('En LinkedIn', LI('urn:li:ugcPost:7524378649509265408')), l('Texto', G('posts/2026-11-06-V1.md')), l('Vídeo', PM('videos/1793951642786-anim-resumen-semana-V1.mp4'))],
 '2026-11-09': [l('Artículo en LinkedIn', PULSE['AR4']), l('Post de presentación', G('posts/2026-11-09-AR4-post.md')), l('Texto del artículo', G('articulos/04-acelera-automatiza-aumenta-para-pegar.md')), l('Portada', G('imagenes/portada-articulo-04.png')), l('Vídeo', G('imagenes/anim-articulo-04.mp4'))],
 '2026-11-10': [l('En LinkedIn', LI('urn:li:ugcPost:7525822078038753280')), l('Texto', G('posts/2026-11-10-B18.md')), l('Vídeo', PM('videos/1793952054509-anim-infografia-B18.mp4'))],
 '2026-11-11': [l('En LinkedIn', LI('urn:li:ugcPost:7526184472648523776')), l('Texto', G('posts/2026-11-11-C13.md')), l('Vídeo', PM('videos/1794053128602-anim-comunidad-C13.mp4'))],
 '2026-11-12': [l('En LinkedIn', LI('urn:li:ugcPost:7526546865744543745')), l('Texto', G('posts/2026-11-12-B15.md')), l('Vídeo', PM('videos/1794053129090-anim-infografia-B15.mp4'))],
 '2026-11-13': [l('En LinkedIn', LI('urn:li:ugcPost:7526909233515200512')), l('Texto', G('posts/2026-11-13-V2.md')), l('Vídeo', PM('videos/1794512108138-anim-resumen-semana-V2.mp4'))],
 '2026-11-16': [l('Artículo en LinkedIn', PULSE['AR3']), l('Post de presentación', G('posts/2026-11-16-AR3-post.md')), l('Texto del artículo', G('articulos/03-la-bola-negra-para-pegar.md')), l('Portada', G('imagenes/portada-articulo-03.png')), l('Vídeo', G('imagenes/anim-articulo-03.mp4')), l('Vídeo promocional', G('imagenes/anim-promo-AR3.mp4')), l('Estudio base', G('estudios/01-la-bola-negra-y-el-canon.md'))],
 '2026-11-17': [l('En LinkedIn', LI('urn:li:ugcPost:7528358789184507904')), l('Texto', G('posts/2026-11-17-B11.md')), l('Vídeo', PM('videos/1794850022070-anim-infografia-B11.mp4'))],
 '2026-11-18': [l('En LinkedIn', LI('urn:li:ugcPost:7528726959498121216')), l('Texto', G('posts/2026-11-18-C4.md')), l('Vídeo', PM('videos/1794988350567-anim-comunidad-C4.mp4'))],
 '2026-11-19': [l('En LinkedIn', LI('urn:li:ugcPost:7529104370664116224')), l('Texto', G('posts/2026-11-19-B23.md')), l('Vídeo', PM('videos/1794988835613-anim-infografia-B23.mp4')), l('Carpeta que se usó para publicar', T('listos-para-publicar/2026-11-19-jueves'))],
 '2026-11-20': [l('En LinkedIn', LI('urn:li:ugcPost:7529451636377903104')), l('Texto', G('posts/2026-11-20-V3.md')), l('Vídeo', PM('videos/1794988836237-anim-resumen-semana-V3.mp4')), l('Carpeta preparada', T('listos-para-publicar/2026-11-20-viernes'))],
 '2026-11-23': [l('Texto del artículo', G('articulos/05-diagnostico-antes-que-solucion-para-pegar.md')), l('Notas del borrador', G('articulos/05-diagnostico-antes-que-solucion.md')), l('Post de presentación', G('posts/2026-11-23-AR5-post.md')), l('Portada', G('imagenes/portada-articulo-05.png')), l('Vídeo', G('imagenes/anim-articulo-05.mp4'))],
 '2026-11-24': [l('Texto del post', G('posts/2026-11-24-B24.md')), l('Vídeo', G('imagenes/anim-infografia-B24.mp4')), l('Banco y calendario de posts', G('03-backlog-posts.md'))],
 '2026-11-25': [l('Texto', G('posts/2026-11-11-C11.md')), l('Tarjeta', G('imagenes/tarjeta-comunidad-C11.png')), l('Vídeo (por regenerar)', G('imagenes/anim-comunidad-C11.mp4'))],
 '2026-11-27': [l('Regla del cierre semanal', G('README.md')), l('Plantilla de vídeo', G('imagenes/anim-resumen-semana-V3.html'))],
}
PERFIL = {'p4': [l('Cabecera', G('imagenes/cabecera.png')), l('Avatar', G('imagenes/avatar.png'))]}
CV = lambda f: l('CV ' + f.split('_')[-1].replace('.pdf', '').replace('.docx', ''), G('documentos/cv/' + f))
def cv_empleo(empresa):
    e = empresa.lower(); out = []
    if 'santander' in e: out = [l('CV de Santander', G('documentos/cv/CV_Alejandro_Berruezo_Santander.pdf')), l('CV de Santander para sistemas de selección', G('documentos/cv/CV_Alejandro_Berruezo_Santander_ATS.docx'))]
    elif 'capgemini invent' in e: out = [l('CV de Capgemini Invent', G('documentos/cv/CV_Alejandro_Berruezo_Capgemini_Invent.pdf')), l('CV de Capgemini Invent en inglés', G('documentos/cv/CV_Alejandro_Berruezo_Capgemini_Invent_EN.pdf'))]
    elif 'hbx' in e: out = [l('CV de HBX en inglés', G('documentos/cv/CV_Alejandro_Berruezo_HBX_EN.pdf')), l('Aplicaciones HBX y Wolters Kluwer', G('documentos/cv/aplicaciones-hbx-wolters-kluwer.md'))]
    elif 'hays' in e: out = [l('CV de Hays', G('documentos/cv/CV_Alejandro_Berruezo_Hays.pdf'))]
    elif 'wolters' in e: out = [l('CV de Wolters Kluwer en inglés', G('documentos/cv/CV_Alejandro_Berruezo_WoltersKluwer_EN.pdf')), l('Aplicaciones HBX y Wolters Kluwer', G('documentos/cv/aplicaciones-hbx-wolters-kluwer.md'))]
    else: out = [l('CV general', G('documentos/cv/CV_Alejandro_Berruezo_General.pdf'))]
    return out + [l('Registro de ofertas', G('13-empleo.md'))]
HESTIA = {
 'h1': [l('En LinkedIn', LI('urn:li:share:7521118645364744192')), l('Foto', PM('images/1793007342092-hestia-thalassa-salon-li-2026-10-1.jpg'))],
 'h2': [l('En LinkedIn', LI('urn:li:ugcPost:7522930580859187201')), l('Vídeo', PM('videos/1793394758998-elige-tu-hestia-li-2026-11-1.mp4'))],
 'h3': [l('En LinkedIn', LI('urn:li:ugcPost:7525467226112638976')), l('Foto 1', PM('images/1793396706924-hestia-mar-salon-1-li-2026-11-2.jpg')), l('Foto 2', PM('images/1793396781912-hestia-mar-salon-2-li-2026-11-2.jpg')), l('Foto 3', PM('images/1793396784607-hestia-mar-salon-3-li-2026-11-2.jpg'))]}
def aplica(fich, fn):
    d = json.load(open(fich, encoding='utf-8'))
    for r in d: r['enlaces'] = fn(r)
    json.dump(d, open(fich, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return d
d = aplica('datos-parrilla/parrilla.json', lambda r: SYN.get(r['fecha']) or [l(*BACKLOG)])
aplica('datos-parrilla/hestia.json', lambda r: HESTIA.get(r['id'], []))
aplica('datos-parrilla/perfil.json', lambda r: [l('Plan del perfil', G('07-perfil.md'))] + PERFIL.get(r['id'], []))
aplica('datos-parrilla/empleos.json', lambda r: cv_empleo(r['empresa']))
print('filas con enlaces:', sum(1 for r in d if r['enlaces']), 'de', len(d))
