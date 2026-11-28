# Convierte cubierta-300ppp.png (de aplanar_cubierta.js) en cubierta-KDP.pdf de una sola imagen a 300 ppp.
from PIL import Image
from libro import PAGINAS_TOTAL, GROSOR_PAPEL
Image.MAX_IMAGE_PIXELS = None
spine = PAGINAS_TOTAL * GROSOR_PAPEL
W, H = round((2 * 8.5 + spine + 0.25) * 300), round(11.25 * 300)
im = Image.open('cubierta-300ppp.png').convert('RGB')
if im.size != (W, H):
    im = im.resize((W, H), Image.LANCZOS)
im.save('cubierta-KDP.pdf', 'PDF', resolution=300.0)
im.crop((round((0.125 + 8.5 + spine) * 300), 0, W, H)).save('portada-frontal.jpg', quality=92)
print('ok', W, H)
