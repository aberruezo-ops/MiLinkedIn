import math
# marca de girasol pequeña
seeds=[]; R=7.0; c=R/math.sqrt(30)
cols=['#B5512A','#2C6D3F','#C89A2A']
for n in range(31):
    r=c*math.sqrt(n); t=math.radians(n*137.5)
    seeds.append(f'<circle cx="{R+1+r*math.cos(t):.2f}" cy="{R+1+r*math.sin(t):.2f}" r=".62" fill="{cols[n%3]}"/>')
MARK=f'<svg viewBox="0 0 {2*R+2} {2*R+2}" width="15mm" height="15mm">{"".join(seeds)}</svg>'

fases=[("1","Diagnóstico","Entender dónde se pierde tiempo, calidad o dinero, y por qué.","Restricción nombrada, línea base medida y mapa de lo que nadie escribió."),
("2","Diseño","Decidir qué se cambia, cómo y con qué. Primero el trabajo, después la herramienta.","Cartera priorizada y criterios del piloto firmados. Cinco preguntas por opción."),
("3","Piloto","Probar en pequeño, con gente y datos reales, donde fallaría primero.","Resultado contra la línea base. Pasar, ajustar o retirar, sin reescribir criterios."),
("4","Escala","Extender lo que funciona, por etapas, con roles e incentivos.","Los indicadores aguantan al ampliar y los tres elementos aguantan la carga."),
("5","Sostenimiento","Que la mejora siga cuando el equipo del programa se vaya.","Dueño operativo, presupuesto recurrente e indicadores estables dos ciclos.")]
lanes=[("Personas","per",["Mapa de actores: quién gana, quién pierde, quién decide y quién sabe.","Nuevo diseño del trabajo: qué decide cada rol y qué deja de hacer.","Espacio para fallar: retirar se dice en voz alta antes de empezar.","Formación en el puesto, por rol, y una comunidad con varios referentes.","Quien enseña lo que la tarea enseñaba tiene nombre y tiempo."]),
("Conocimiento","con",["El mapa de lo que nadie escribió: qué sabe cada persona que no está en ningún sitio.","Qué pasa con cada fila: se queda, pasa al sistema revisable o se pierde.","Lecciones del piloto contra la línea base, escritas.","Lo que aprendieron los usuarios avanzados entra en el procedimiento.","Supervisión y revisión de supuestos en cada ciclo."]),
("Tecnología e IA","tec",["Madurez de los tres elementos y regla de entrada: nada entra sin nivel 2.","Acelera, automatiza o aumenta, y el techo de autonomía de cada sistema.","Autonomía baja: sugiere o propone, con registro y derecho a parar.","Cada subida de nivel se gana en una puerta, con criterio y responsable.","Coste por tarea completada y revisión de construir, comprar o retirar."])]

lec=[("La adopción al 100 % no prueba nada.","Se puede adoptar muy bien una transformación que hace perder pericia. Medir la capacidad, no solo el uso."),
("Medir en el flujo de trabajo.","Coste por tarea completada, calidad frente al proceso actual y uso real en producción."),
("La tecnología da acceso; la capacidad da la adopción.","Formación por rol, aplicada al trabajo de cada uno, y medida en el uso."),
("Un solo embajador es un punto único de fallo.","Si se va, se va el saber. Estándares y una comunidad, no un héroe."),
("Puede funcionar y no salir a cuenta.","Modelo económico desde el diseño: reutilizar antes de comprar, comprar antes de construir."),
("Un piloto sin dueño ni medida pactada se queda en piloto.","Y antes de aprobarlo, preguntar qué decisión cambiará su resultado.")]
evo=["Indicador de capacidad en pareja con el de uso.","Coste por tarea completada en el modelo económico.","Comunidad con varios referentes por área.","En los criterios del piloto: qué decisión cambiará su resultado.","Revisión por ciclo de construir, comprar o retirar."]

CSS='''
@font-face{font-family:Fr;src:url('file:///home/user/MiLinkedIn/synergos/imagenes/fonts/Fraunces.ttf');font-weight:100 900}
@page{size:A4 landscape;margin:0}
:root{--ink:#1F1D1A;--mute:#5E625C;--rule:#D9DED9;--verde:#2C6D3F;--terra:#B5512A;--albero:#C89A2A;--bg:#F4F6F6;--r:3mm 0 3mm 0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:297mm;height:210mm;background:#fff;color:var(--ink);font-family:'Bitstream Charter','Liberation Serif',serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.pg{width:297mm;height:210mm;overflow:hidden;padding:10mm 11mm 8mm;display:grid;grid-template-rows:auto 1fr auto;gap:4.2mm}
header{display:grid;grid-template-columns:1fr auto;align-items:end;border-bottom:.35mm solid var(--ink);padding-bottom:3mm}
h1{font-family:Fr,serif;font-weight:380;font-size:23pt;line-height:1.02;letter-spacing:-.3pt}
.sub{font-family:Fr,serif;font-size:10.6pt;margin-top:1.6mm;color:#33372F}
.brand{display:flex;align-items:center;gap:2.5mm;font-family:Inter,sans-serif;font-size:7.2pt;color:var(--mute);text-align:right;line-height:1.35}
.brand b{display:block;font-family:Fr,serif;font-weight:500;font-size:11pt;color:var(--ink)}
.main{display:grid;grid-template-columns:1fr 74mm;gap:6mm;min-height:0}
.grid{display:grid;grid-template-columns:23mm repeat(5,1fr);column-gap:2.2mm;row-gap:2.6mm;align-content:start}
.ph{position:relative;background:var(--ink);color:#fff;border-radius:var(--r);padding:2.2mm 2.6mm 2.4mm}
.ph .n{font-family:Fr,serif;font-size:15pt;line-height:1;color:#D9B65C}
.ph .t{font-family:Fr,serif;font-weight:560;font-size:11.4pt;margin:.6mm 0 1mm}
.ph p{font-size:8pt;line-height:1.32;color:#E8ECE8}
.gate{grid-column:span 1;border:.3mm dashed #8A8F87;border-radius:var(--r);padding:1.8mm 2.4mm 2mm;font-size:7.8pt;line-height:1.28;color:#33372F;background:#fff}
.gate b{display:block;font-family:Inter,sans-serif;font-size:6pt;letter-spacing:.6pt;text-transform:uppercase;color:var(--mute);margin-bottom:.4mm;font-weight:600}
.rl{font-family:Fr,serif;font-style:italic;font-size:10.6pt;line-height:1.1;display:flex;align-items:center}
.cell{border-radius:var(--r);padding:2.2mm 2.5mm;font-size:7.9pt;line-height:1.32}
.per{background:#F6E3DA}.per.rl{color:var(--terra);background:none}
.con{background:#E2EEE5}.con.rl{color:var(--verde);background:none}
.tec{background:#F5EBCF}.tec.rl{color:#7A5C16;background:none}
.lane-h{grid-column:1/-1;font-family:Inter,sans-serif;font-size:6.4pt;letter-spacing:.8pt;text-transform:uppercase;color:var(--mute);margin-top:1mm;display:flex;align-items:center;gap:2mm}
.lane-h:after{content:"";flex:1;height:.25mm;background:var(--rule)}
aside{display:flex;flex-direction:column;gap:3mm;min-height:0}
aside h2{font-family:Fr,serif;font-weight:560;font-size:10.4pt}
aside .src{font-family:Inter,sans-serif;font-size:6.2pt;color:var(--mute);margin-top:.3mm}
.lec{list-style:none;display:flex;flex-direction:column;gap:1.5mm;margin-top:1.4mm}
.lec li{font-size:7.7pt;line-height:1.3;padding-left:3mm;position:relative}
.lec li:before{content:"";position:absolute;left:0;top:.5em;width:1.2mm;height:1.2mm;border-radius:50%;background:var(--ink)}
.lec b{font-weight:700}
.evo{background:var(--bg);border-radius:var(--r);padding:2.4mm 3mm}
.evo ul{list-style:none;margin-top:1.2mm;display:flex;flex-direction:column;gap:1mm}
.evo li{font-size:7.7pt;line-height:1.28;padding-left:3mm;position:relative}
.evo li:before{content:"";position:absolute;left:0;top:.5em;width:1.2mm;height:1.2mm;border-radius:50%;background:var(--verde)}
footer{display:grid;grid-template-columns:1.25fr 1fr 1.1fr;gap:4mm;border-top:.25mm solid var(--rule);padding-top:2.6mm}
footer h3{font-family:Inter,sans-serif;font-size:6.4pt;letter-spacing:.8pt;text-transform:uppercase;color:var(--mute);font-weight:600;margin-bottom:1mm}
footer p{font-size:7.6pt;line-height:1.32}
.auto{display:flex;gap:1mm}
.auto div{flex:1;border-radius:var(--r);padding:1.1mm 1.6mm;font-size:6.5pt;line-height:1.2;background:var(--bg)}
.auto div b{display:block;font-family:Fr,serif;font-size:8.6pt;font-weight:560}
.auto div.top{background:#E7E9E6;color:#6B6F68}
.exits{display:flex;gap:1.2mm;margin-top:.8mm}
.exits span{font-family:Inter,sans-serif;font-size:6.6pt;font-weight:600;padding:.6mm 2.2mm;border-radius:2mm 0 2mm 0}
'''
def phase(n,t,p): return f'<div class="ph"><div class="n">{n}</div><div class="t">{t}</div><p>{p}</p></div>'
H=[]
H.append('<div></div>'+''.join(phase(n,t,p) for n,t,p,_ in fases))
H.append('<div class="rl" style="font-size:9.4pt;color:var(--ink)">Puerta: qué tiene que ser cierto</div>'+''.join(f'<div class="gate">{g}</div>' for *_,g in fases))
H.append('<div class="lane-h">Los tres elementos crecen a la vez</div>')
for name,cls,cells in lanes:
    H.append(f'<div class="rl {cls}">{name}</div>'+''.join(f'<div class="cell {cls}">{c}</div>' for c in cells))
GRID=''.join(H)
LEC=''.join(f'<li><b>{a}</b> {b}</li>' for a,b in lec)
EVO=''.join(f'<li>{e}</li>' for e in evo)
HTML=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Adopción de innovación e IA</title><style>{CSS}</style></head><body><div class="pg">
<header><div><h1>Adoptar innovación e IA: de la idea al trabajo de cada día</h1>
<div class="sub">Cinco fases, una puerta en cada una y tres elementos que crecen a la vez. La tecnología pesa lo mismo que las personas y el conocimiento.</div></div>
<div class="brand"><div><b>Synergós</b>Método de adopción<br>Versión de trabajo, noviembre de 2026</div>{MARK}</div></header>
<div class="main"><div class="grid">{GRID}</div>
<aside>
<div><h2>Lo que enseñan otros</h2><div class="src">Experiencias publicadas en LinkedIn, octubre y noviembre de 2026</div><ul class="lec">{LEC}</ul></div>
<div class="evo"><h2>Lo que añadimos al método</h2><ul>{EVO}</ul></div>
</aside></div>
<footer>
<div><h3>Cómo se mide</h3><p>Línea base antes de cambiar nada. Pocos indicadores y en pareja: velocidad con calidad, coste con satisfacción, uso con capacidad. Al menos uno por elemento. La mejora se cuenta como delta: lo recorrido desde la línea base hacia el objetivo.</p></div>
<div><h3>Cada puerta tiene tres salidas</h3><div class="exits"><span style="background:#E2EEE5;color:var(--verde)">Pasar</span><span style="background:#F5EBCF;color:#7A5C16">Ajustar y repetir</span><span style="background:#F6E3DA;color:var(--terra)">Retirar</span></div><p style="margin-top:1.2mm">Retirar en el piloto es barato. Los criterios se firman antes y no se reescriben al ver el resultado.</p></div>
<div><h3>Autonomía de la IA, peldaño a peldaño</h3><div class="auto"><div><b>1</b>Sugiere</div><div><b>2</b>Propone</div><div><b>3</b>Actúa con revisión</div><div class="top"><b>4</b>Actúa e informa</div></div><p style="margin-top:1mm">Cada sistema tiene un techo escrito. Las decisiones sobre derechos de las personas se quedan en el 3.</p></div>
</footer></div></body></html>'''
open('onepager.html','w',encoding='utf-8').write(HTML)
