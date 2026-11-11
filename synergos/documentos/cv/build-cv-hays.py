import math
# ---- girasol: una semilla por año (1996 a 2026), ángulo áureo 137,5 grados
cols={'prog':'#7CC090','nexus':'#C89A2A','getr':'#2C6D3F','trans':'#B5512A','mins':'#1F1D1A'}
def stage(y):
    if y<=1997: return 'prog'
    if y<=2005: return 'nexus'
    if y<=2016: return 'getr'
    if y<=2018: return 'trans'
    return 'mins'
seeds=[]
R=17.0; c=R/math.sqrt(30)
for n in range(31):
    y=1996+n; r=c*math.sqrt(n); t=math.radians(n*137.5)
    x=R+1.6+r*math.cos(t); yy=R+1.6+r*math.sin(t)
    seeds.append(f'<circle cx="{x:.2f}" cy="{yy:.2f}" r="{1.05+0.012*n:.2f}" fill="{cols[stage(y)]}"/>')
SVG=f'<svg viewBox="0 0 {2*R+3.2:.1f} {2*R+3.2:.1f}" width="35mm" height="35mm" xmlns="http://www.w3.org/2000/svg">{"".join(seeds)}</svg>'
legend=[('prog','1996 a 1998','Software AG y Thales','Programador, con Telefónica y la GISS como clientes'),
('nexus','1998 a 2006','Nexus IT y Business Integration (BT)','Preventa, consultoría y proyectos'),
('getr','2006 a 2017','Getronics (antes Thales)','De la preventa a la dirección de alianzas y oferta'),
('trans','2017 a 2019','Estudios y Enzyme','Máster de Big Data y nueve meses montando una oficina'),
('mins','2019 a hoy','Minsait (Indra)','Gobierno de la transformación digital de la GISS')]
LEG=''.join(f'<li><i style="background:{cols[k]}"></i><span class="ly">{y}</span><span><b>{n}</b> {d}</span></li>' for k,y,n,d in legend)

CSS='''
@font-face{font-family:Fr;src:url('file:///home/user/MiLinkedIn/synergos/imagenes/fonts/Fraunces.ttf');font-weight:100 900}
@page{size:A4;margin:0}
:root{--ink:#1F1D1A;--mute:#5E625C;--rule:#D9DED9;--verde:#2C6D3F;--terra:#B5512A;--albero:#C89A2A;--tint:#EEF3EF;--r:3.2mm 0 3.2mm 0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:210mm;background:#fff;color:var(--ink);font-family:'Bitstream Charter','Charter','Liberation Serif',serif;font-size:8.6pt;line-height:1.38;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;overflow:hidden;padding:14mm 16mm 10mm 16mm;page-break-after:always;position:relative}
.page:last-child{page-break-after:auto}
.row{display:grid;grid-template-columns:34mm 1fr;column-gap:7mm;margin-top:5.8mm}
.lab{font-family:Fr,'Liberation Serif',serif;font-style:italic;font-weight:400;font-size:11pt;color:var(--verde);line-height:1.15;padding-top:.3mm}
.sans{font-family:Inter,'Liberation Sans',sans-serif}
header{display:grid;grid-template-columns:1fr 34mm;column-gap:7mm;align-items:end}
h1{font-family:Fr,'Liberation Serif',serif;font-weight:360;font-size:31pt;line-height:1;letter-spacing:-.6pt;color:var(--ink)}
.role{font-family:Fr,'Liberation Serif',serif;font-size:11.2pt;line-height:1.25;margin-top:3mm;color:var(--ink)}
.foto{width:33mm;height:33mm;border-radius:50%;background:#ccc url(data:image/jpeg;base64,__FOTO__) center/cover;justify-self:end}
.contact{display:flex;gap:5mm;margin-top:4.2mm;padding-top:2.2mm;border-top:.3mm solid var(--ink);font-family:Inter,'Liberation Sans',sans-serif;font-size:7.3pt;color:var(--ink)}
.contact span+span{padding-left:5mm;border-left:.25mm solid var(--rule)}
p{margin-bottom:1.8mm}
.lead{font-size:10.3pt;line-height:1.42}
.apt{display:grid;grid-template-columns:1fr 1fr;gap:3.2mm 6mm}
.apt h3{font-family:Fr,'Liberation Serif',serif;font-weight:600;font-size:9.2pt;color:var(--ink);line-height:1.2;margin-bottom:.5mm}
.apt p{font-size:8.5pt;line-height:1.36;margin:0;color:#2E322D}
.job .ti{font-family:Fr,'Liberation Serif',serif;font-weight:600;font-size:10pt;line-height:1.22;color:var(--ink)}
.job .co{font-style:italic;color:var(--mute);font-size:8.4pt;margin-bottom:1.2mm}
.dt{font-family:Inter,'Liberation Sans',sans-serif;font-size:7.2pt;color:var(--mute);padding-top:.7mm;line-height:1.35;font-variant-numeric:tabular-nums}
.dt b{display:block;font-weight:600;color:var(--ink)}
ul.b{list-style:none}
ul.b li{position:relative;padding-left:3.4mm;margin-bottom:.9mm}
ul.b li:before{content:"";position:absolute;left:.2mm;top:.58em;width:1.1mm;height:1.1mm;border-radius:50%;background:var(--verde)}
.fig{display:flex;gap:1.8mm;margin:1.6mm 0 2mm}
.fig div{flex:1;background:var(--tint);border-radius:var(--r);padding:1.4mm 2.2mm 1.3mm;font-family:Inter,'Liberation Sans',sans-serif;font-size:6.5pt;line-height:1.2;color:var(--mute)}
.fig b{display:block;font-family:Fr,'Liberation Serif',serif;font-weight:500;font-size:13pt;line-height:1.1;color:var(--verde);white-space:nowrap}
.box{background:var(--tint);border-radius:var(--r);padding:2.6mm 3.8mm 1.6mm;margin:1.4mm 0 2.2mm}
.box .ti{font-family:Fr,'Liberation Serif',serif;font-weight:600;font-size:10pt;margin-bottom:.8mm}
.sun{display:flex;gap:0}
.legend{list-style:none}
.legend li{display:grid;grid-template-columns:3mm 21mm 1fr;align-items:baseline;gap:0 2mm;margin-bottom:1.5mm;font-size:8.2pt;line-height:1.3}
.legend i{width:2.4mm;height:2.4mm;border-radius:50%;display:block;margin-top:.5mm}
.ly{font-family:Inter,'Liberation Sans',sans-serif;font-size:7.2pt;color:var(--mute);font-variant-numeric:tabular-nums}
.cap{font-size:7.4pt;color:var(--mute);font-style:italic;margin-top:1.2mm}
.old{margin-bottom:2.2mm}
.hd{display:flex;justify-content:space-between;align-items:baseline;gap:4mm}
.old .ti{font-family:Fr,'Liberation Serif',serif;font-weight:600;font-size:9.2pt}
.old p{margin:0;font-size:8.3pt}
.cols3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:0 5mm}
.cols3 h4{font-family:Inter,'Liberation Sans',sans-serif;font-size:7pt;font-weight:600;color:var(--ink);margin-bottom:1mm}
.cols3 p,.cols3 li{font-size:7.9pt;line-height:1.32;margin-bottom:1.1mm}
.cols3 ul{list-style:none}
.chips{display:flex;flex-wrap:wrap;gap:1mm;margin-top:1mm}
.chips span{font-family:Inter,'Liberation Sans',sans-serif;font-size:6.5pt;background:var(--tint);padding:.6mm 2mm;border-radius:2.2mm 0 2.2mm 0;color:var(--ink)}
'''
HTML=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Alejandro Berruezo Márquez, CV</title><style>{CSS}</style></head><body>
<div class="page">
<header>
  <div><h1>Alejandro Berruezo Márquez</h1>
  <div class="role">Dirección de transformación digital y soluciones tecnológicas</div></div>
  <div class="foto" role="img" aria-label="Alejandro Berruezo"></div>
</header>
<div class="contact"><span>Madrid</span><span>+34 620 316 370</span><span>aberruezo@gmail.com</span><span>linkedin.com/in/alejandro-berruezo</span></div>

<div class="row"><div class="lab">Perfil</div><div>
  <p class="lead">Llevo 30 años haciendo que la tecnología llegue al trabajo real en organizaciones con muchos actores y mucha regulación: sector público, banca privada, industria y servicios.</p>
  <p>Combino la dirección de unidades y programas grandes con el negocio y la preventa. He gobernado un programa de más de 300 profesionales, dirigido un área de 25 personas con 3.800 oportunidades al año, y liderado ofertas por más de 500 M€. Soy ingeniero informático con un máster en Big Data y Business Analytics, y hoy me dedico al aterrizaje y la puesta en marcha de los modelos que implanto, hasta que alcanzan velocidad de crucero. Lo he formalizado en Synergós, mi método propio para dirigir transformaciones con IA.</p>
</div></div>

<div class="row"><div class="lab">Lo que aporto</div><div class="apt">
  <div><h3>Dirección de unidades y programas grandes</h3><p>Gobierno de la transformación digital de la GISS, con un programa de más de 300 profesionales entre ingeniería, arquitectura, producto, operaciones y dirección del cliente. Equipos de hasta 25 personas en Getronics.</p></div>
  <div><h3>Soluciones y transformación para clientes</h3><p>Estrategias, modelos objetivo y hojas de ruta ejecutables en Administración Pública, banca privada e industria. Cartera de más de 50 soluciones de transformación digital en Getronics.</p></div>
  <div><h3>Preventa y oferta</h3><p>Más de 500 M€ en ofertas lideradas, con adjudicación cercana al 50 %, y propuestas de más de 30 M€ con equipos de oferta de más de 12 personas. 3.800 oportunidades al año en Getronics.</p></div>
  <div><h3>Presupuesto, planificación, riesgos y KPIs</h3><p>Un 20 % menos de coste del área en tres años en Getronics. Casos de negocio, línea base e indicadores en pareja, registro de riesgos y decisiones, y puertas con criterios previos.</p></div>
  <div><h3>Interlocución con dirección</h3><p>Acompañamiento al comité de dirección de la GISS en las decisiones de cada fase. Del cliente a las áreas técnicas y comerciales: preventa, arquitectura y producto en la misma mesa.</p></div>
  <div><h3>Datos, automatización e IA</h3><p>Uso diario de IA generativa y análisis de sus riesgos. Método propio, Synergós, con escala de autonomía, registro y derecho a parar. Máster en Big Data y Business Analytics.</p></div>
</div></div>

<div class="row job"><div class="dt"><b>Jun 2019 a hoy</b>Madrid, híbrido</div><div>
  <div class="ti">Senior Manager / Principal, Transformación Digital, Preventa y Proyectos</div>
  <div class="co">Minsait (Indra)</div>
  <div class="fig"><div><b>+500 M€</b>en ofertas lideradas</div><div><b>≈50 %</b>de adjudicación en oportunidades clave</div><div><b>+30 M€</b>propuestas de mayor tamaño</div><div><b>+12</b>personas en equipos de oferta</div><div><b>400</b>personas en servicios ofertados</div></div>
  <div class="box"><div class="ti">Transformación digital de la GISS</div>
    <ul class="b"><li>Gerencia de Informática de la Seguridad Social: liderazgo de un programa de más de 300 profesionales.</li>
    <li>Modelo de gobierno entre ingeniería, arquitectura, producto, operaciones y la dirección del cliente, y acompañamiento a su comité de dirección en las decisiones de cada fase.</li></ul></div>
  <ul class="b">
    <li>Gobierno de plataformas, productos y ecosistemas tecnológicos; estrategias de transformación, modelos objetivo y hojas de ruta ejecutables en sector público y grandes entornos regulados.</li>
    <li><b>Nuevos modelos de trabajo.</b> Creación de MINEsait dentro de Minsait, un ecosistema de innovación colaborativa e intraemprendimiento que cambia cómo se organizan y colaboran los equipos.</li>
    <li><b>Innovación aplicada y bajo método.</b> La llevo a programas reales con criterios escritos, responsables y puertas de decisión, el enfoque que he formalizado en Synergós.</li>
  </ul></div></div>
</div>

<div class="page">
<div class="row" style="margin-top:0"><div><div class="lab" style="margin-bottom:2mm">Trayectoria</div>{SVG}</div><div style="padding-top:7mm"><ul class="legend">{LEG}</ul>
<div class="cap">Una semilla por año, de 1996 a 2026, colocadas con el ángulo áureo de 137,5 grados, el mismo del girasol de Synergós.</div></div></div>

<div class="row"><div class="lab">Antes de Minsait</div><div>
  <div class="job" style="margin-bottom:2.4mm"><div class="ti hd"><span>Senior Manager y Presales Manager</span><span class="dt">Sep 2018 a may 2019</span></div><div class="co">Enzyme Advising Group, Madrid</div>
    <div class="fig" style="margin-top:.8mm"><div><b>≈10</b>personas en la oficina de Madrid</div><div><b>≈25</b>oportunidades en cartera</div><div><b>0,8 a 0,9 M€</b>de volumen total aproximado</div></div>
    <ul class="b"><li>Puesta en marcha de la oficina de Madrid, con soporte de servicios desde Barcelona: preventa, desarrollo de negocio y cuentas estratégicas.</li></ul></div>
  <div class="job" style="margin-bottom:2.4mm"><div class="ti hd"><span>Presales, Alliances &amp; Offering Director</span><span class="dt">May 2012 a feb 2017</span></div><div class="co">Getronics, Madrid</div>
    <div class="fig" style="margin-top:.8mm"><div><b>25</b>personas a cargo</div><div><b>3.800</b>oportunidades al año</div><div><b>+400 M€</b>de volumen</div><div><b>11 a 19 %</b>tasa de éxito</div><div><b>-20 %</b>coste del área en 3 años</div></div>
    <ul class="b"><li>Dirección del área de preventa, desarrollo de negocio y consultoría.</li>
    <li>Alianzas, casi inexistentes hasta entonces: más de 30 partners al año con planes conjuntos y seguimiento de compromisos, cerca de un 12 % más de oportunidades.</li>
    <li>Cartera de más de 50 soluciones de transformación digital, con un 8 % más de oportunidades al año. Integración de equipos y procesos.</li></ul></div>
  <div class="old"><div class="ti hd"><span>Presales &amp; Bid Director</span><span class="dt">Dic 2010 a may 2012</span></div><p>Getronics. Preventa nacional con foco en Administración Pública. Definición, implantación y auditoría de los procedimientos de gestión de oportunidades.</p></div>
  <div class="old"><div class="ti hd"><span>Presales Manager</span><span class="dt">Jun 2006 a nov 2010</span></div><p>Getronics (antes Thales). Coordinación de la preventa técnica; definición, puesta en marcha y auditoría de procedimientos de oportunidades y proyectos.</p></div>
  <div class="old"><div class="ti hd"><span>Presales Engineer, Consultant y Project Manager</span><span class="dt">Feb 1998 a may 2006</span></div><p>Nexus IT y después Business Integration (BT). Soluciones, estimación y gestión de proyectos; planes de calidad, manuales operativos y transición de servicios.</p></div>
  <div class="old"><div class="ti hd"><span>Programador</span><span class="dt">1996 a 1998</span></div><p>Software AG (Natural y Adabas, para Telefónica) y Thales (en la GISS, el organismo que gobierno desde 2019).</p></div>
</div></div>

<div class="row"><div class="lab">Emprendimiento</div><div>
  <div class="old"><div class="ti hd"><span>Fundador, Synergós</span><span class="dt">2024 a hoy</span></div><p>Método propio para dirigir transformaciones con IA, con origen en MINEsait. Versión 1.5. Comité de puertas integrado en el gobierno del programa, escala de autonomía de cuatro niveles con criterio, responsable y registro, e inventario de sistemas y riesgos con una columna de personas y conocimiento.</p></div>
  <div class="old"><div class="ti hd"><span>Cofundador, Hestía, your home!</span><span class="dt">Dic 2016 a hoy</span></div><p>Alojamiento turístico propio en Vera Playa, Almería, en marcha desde hace casi diez años y convertido en referencia local: operación, comercialización y relación con clientes.</p></div>
</div></div>

<div class="row"><div class="lab">Formación y competencias</div><div class="cols3">
  <div><h4>Formación</h4><ul><li>Ingeniero Superior en Informática, Universidad Autónoma de Madrid, 1996</li><li>Advanced Management Program y Programa Directivo, IE Business School, 2017</li><li>Máster en Big Data y Business Analytics, MSMK, 2018</li><li>Excelencia operativa, BTS, 2025</li></ul></div>
  <div><h4>Certificaciones e idiomas</h4><ul><li>Certified Scrum Master, 2018</li><li>Design Thinking Professional, 2024</li><li>ITIL (EXIN), 2008</li><li>Castellano nativo; inglés B2, First Certificate de la Universidad de Edimburgo</li></ul></div>
  <div><h4>Sectores y tecnología</h4><div class="chips" style="margin:0 0 1.4mm"><span>Administración Pública</span><span>Seguridad Social</span><span>Banca privada</span><span>Industria</span><span>Sanidad y servicios</span><span>Retail</span></div><p>Cloud, APIs, DevOps, big data, Scrum y Lean, IA generativa, ITIL, ISO 9001 y CMMi.</p></div>
</div></div>
</div>
</body></html>'''
open('cv10.tpl.html','w',encoding='utf-8').write(HTML)
