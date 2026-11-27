import sys, random, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
F='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
AMB=(255,176,0)
# letra, hora, x, y, giro  (lienzo 1360x2048) semiescondidas
L={1:[('Ρ','4:15',873,900,-12),('Κ','4:12',300,1900,8)],
   2:[('Σ','4:17',215,1010,-14),('Α','4:13',915,1790,20)],
   3:[('Ο','4:16',120,690,10),('Ι','4:14',1010,560,-18)]}
def letras(im,n,debug=False):
    im=im.convert('RGBA'); g=np.asarray(im.convert('L')).astype(float)
    f=ImageFont.truetype(F,36); fs=ImageFont.truetype(F,13)
    for ch,h,x,y,rot in L[n]:
        lum=g[y-25:y+25,x-25:x+25].mean()
        col=(20,14,6) if lum>110 else (235,205,150)
        al=175 if lum>110 else 120
        t=Image.new('RGBA',(120,120),(0,0,0,0)); d=ImageDraw.Draw(t)
        d.text((60,52),ch,font=f,fill=col+(al,),anchor='mm')
        d.text((60,80),h,font=fs,fill=col+(al,),anchor='mm')
        t=t.rotate(rot,resample=Image.BICUBIC).filter(ImageFilter.GaussianBlur(0.6))
        im.alpha_composite(t,(x-60,y-60))
        if debug: ImageDraw.Draw(im).ellipse([x-55,y-55,x+55,y+55],outline=(255,0,0,255),width=3)
    return im.convert('RGB')
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
outs=[];outs_d=[]
for n in (1,2,3):
    im=Image.open(f'v2_cubierta_c{n}.png').convert('RGB')
    e=envejecer(letras(im,n),n*7); e.save(f'v4_cubierta_c{n}.jpg',quality=93); outs.append(e.resize((600,904)))
    dd=envejecer(letras(im,n,True),n*7)
    for k,(ch,h,x,y,r) in enumerate(L[n]): e.crop((x-110,y-110,x+110,y+110)).resize((440,440)).save(f'zoom_{n}_{k}.png')
    outs_d.append(dd.resize((600,904)))
w=Image.new('RGB',(1800,904));[w.paste(o,(600*i,0)) for i,o in enumerate(outs)];w.save('v4_cubiertas_s.png')
w=Image.new('RGB',(1800,904));[w.paste(o,(600*i,0)) for i,o in enumerate(outs_d)];w.save('v4_donde_s.png')
z=Image.new('RGB',(1320,880))
for n in (1,2,3):
    for k in (0,1): z.paste(Image.open(f'zoom_{n}_{k}.png'),((n-1)*440,k*440))
z.save('v4_zoom.png')
