import sys, random, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
F='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
AMB=(255,176,0)
# letra, hora, x, y  (lienzo 1360x2048)
L={1:[('Ρ','4:15',420,1180),('Κ','4:12',905,1270)],
   2:[('Σ','4:17',215,1335),('Α','4:13',1120,1335)],
   3:[('Ο','4:16',204,800),('Ι','4:14',816,800)]}
def letras(im,n):
    lay=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(lay)
    f=ImageFont.truetype(F,46); fs=ImageFont.truetype(F,19)
    for ch,h,x,y in L[n]:
        d.ellipse([x-34,y-34,x+34,y+34],outline=AMB+(200,),width=2)
        d.text((x,y-2),ch,font=f,fill=AMB+(235,),anchor='mm')
        d.text((x,y+50),h,font=fs,fill=AMB+(190,),anchor='mm')
        d.line([x,y+64,x,y+84],fill=AMB+(170,),width=2)
    glow=lay.filter(ImageFilter.GaussianBlur(6))
    return Image.alpha_composite(Image.alpha_composite(im.convert('RGBA'),glow),lay).convert('RGB')
def envejecer(im,seed):
    rnd=random.Random(seed); rs=np.random.RandomState(seed)
    W,H=im.size; a=np.asarray(im).astype(np.float32)/255
    # desaturar un poco y virar a papel calido, negros levantados
    g=a.mean(2,keepdims=True); a=a*0.82+g*0.18
    a=a*np.array([1.0,0.96,0.86])
    a=0.045+a*0.93
    # grano
    a+=rs.normal(0,0.035,(H,W,1))
    # manchas grandes (humedad / foxing)
    m=Image.fromarray((rs.rand(H//64+1,W//64+1)*255).astype(np.uint8)).resize((W,H),Image.BICUBIC)
    m=np.asarray(m).astype(np.float32)/255
    a*= (0.86+0.22*m)[...,None]
    lay=Image.new('L',(W,H),0); d=ImageDraw.Draw(lay)
    for _ in range(70):
        x,y,r=rnd.randrange(W),rnd.randrange(H),rnd.randint(3,16)
        d.ellipse([x-r,y-r,x+r,y+r],fill=rnd.randint(30,90))
    fox=np.asarray(lay.filter(ImageFilter.GaussianBlur(5))).astype(np.float32)/255
    a=a*(1-fox[...,None]*0.5)+np.array([0.55,0.38,0.18])*fox[...,None]*0.5
    # pliegues y araniazos claros
    lay=Image.new('L',(W,H),0); d=ImageDraw.Draw(lay)
    for x0 in (int(W*0.045),):
        pts=[(x0+rnd.randint(-3,3),y) for y in range(0,H+40,40)]
        d.line(pts,fill=150,width=3)
    y0=int(H*0.52); d.line([(x,y0+rnd.randint(-2,2)) for x in range(0,W+40,40)],fill=70,width=2)
    for _ in range(45):
        x,y=rnd.randrange(W),rnd.randrange(H); l=rnd.randint(20,160); an=rnd.uniform(-0.4,0.4)+rnd.choice([0,1.57])
        d.line([x,y,x+l*np.cos(an),y+l*np.sin(an)],fill=rnd.randint(40,120),width=1)
    cr=np.asarray(lay.filter(ImageFilter.GaussianBlur(0.8))).astype(np.float32)/255
    a=a+(np.array([0.93,0.88,0.78])-a)*cr[...,None]*0.55
    # bordes y esquinas gastados
    yy,xx=np.mgrid[0:H,0:W]
    e=np.minimum.reduce([xx,W-1-xx,yy,H-1-yy]).astype(np.float32)
    n=np.asarray(Image.fromarray((rs.rand(H//10+1,W//10+1)*255).astype(np.uint8)).resize((W,H),Image.BICUBIC)).astype(np.float32)/255
    wear=np.clip((26*n*n+4-e)/14,0,1)
    cor=np.minimum.reduce([np.hypot(xx,yy),np.hypot(W-xx,yy),np.hypot(xx,H-yy),np.hypot(W-xx,H-yy)])
    wear=np.maximum(wear,np.clip((90*n-cor*0.9)/30,0,1))
    a=a+(np.array([0.90,0.85,0.74])-a)*wear[...,None]*0.85
    # vineta
    v=1-0.22*(((xx/W-0.5)**2+(yy/H-0.5)**2)*2)
    a*=v[...,None]
    return Image.fromarray((np.clip(a,0,1)*255).astype(np.uint8))
outs=[]
for n in (1,2,3):
    im=Image.open(f'v2_cubierta_c{n}.png').convert('RGB')
    im=envejecer(letras(im,n),n*7); im.save(f'v3_cubierta_c{n}.jpg',quality=93); outs.append(im.resize((600,904)))
w=Image.new('RGB',(1800,904));[w.paste(o,(600*i,0)) for i,o in enumerate(outs)];w.save('v3_cubiertas_s.png')
