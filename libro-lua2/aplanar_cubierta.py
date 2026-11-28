# Convierte cubierta-300ppp.png (de aplanar_cubierta.js) en PDFs de cubierta KDP de una sola imagen a 300 ppp,
# uno para papel blanco y otro para papel crema (lomo distinto), y en portada-frontal.jpg.
from PIL import Image
from libro import PAGINAS_TOTAL
Image.MAX_IMAGE_PIXELS = None
H = round(11.25 * 300)
src = Image.open('cubierta-300ppp.png').convert('RGB')
sp0 = PAGINAS_TOTAL * 0.002252
src = src.resize((round((17.25 + sp0) * 300), H), Image.LANCZOS) if src.size[1] != H else src
back = src.crop((0, 0, round(8.625 * 300), H))
front = src.crop((round((8.625 + sp0) * 300), 0, src.size[0], H))
front.save('portada-frontal.jpg', quality=92)
for nombre, grosor in (('blanco', 0.002252), ('crema', 0.0025)):
    W = round((17.25 + PAGINAS_TOTAL * grosor) * 300)
    im = Image.new('RGB', (W, H), (233, 196, 106))
    im.paste(back, (0, 0)); im.paste(front, (W - front.size[0], 0))
    im.save(f'cubierta-KDP-papel-{nombre}.pdf', 'PDF', resolution=300.0)
    if nombre == 'blanco':
        im.save('cubierta-KDP.pdf', 'PDF', resolution=300.0)
    print(nombre, round(W / 300, 3), 'x 11.25 in')
