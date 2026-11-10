import io
S,E=1996.5,2026.9
def pct(x): return (x-S)/(E-S)*100
def bar(a,b,label,cls,row):
    return f'<div class="seg {cls}" style="left:{pct(a):.2f}%;width:{pct(b)-pct(a):.2f}%;top:{row}mm"><span>{label}</span></div>'
segs=[bar(1996.67,1997.55,'','c1',0),bar(1997.55,1998.08,'','c9',0),bar(1998.08,2006.42,'Nexus IT y Business Integration','c2',0),
bar(2006.42,2017.13,'Getronics','c3',0),bar(2017.13,2018.67,'','c8',0),bar(2018.67,2019.42,'','c4',0),bar(2019.42,2026.85,'Minsait (Indra)','c5',0),
bar(2016.92,2026.85,'Hestía, your home!','c6',8.2),bar(2024.85,2026.85,'','c7',14.4)]
grid=''.join(f'<div class="tgrid" style="left:{pct(y):.2f}%"></div>' for y in (2000,2010,2020))
ticks=''.join(f'<span style="position:absolute;left:{pct(y):.2f}%;transform:translateX(-50%)">{y}</span>' for y in (2000,2006,2010,2016,2020,2026))
tl=f'''<div class="tl"><div class="tlbars">{grid}{"".join(segs)}</div>
<div class="tlnote"><span style="left:0">Software AG, Thales</span><span style="left:{pct(2016.6):.2f}%">estudios: máster Big Data</span><span style="right:{100-pct(2024.85)+1:.2f}%;top:14.9mm">Synergós, 2024</span></div></div>'''
CSS='''
@font-face{font-family:Fr;src:url('file:///home/user/MiLinkedIn/synergos/imagenes/fonts/Fraunces.ttf')}
@page{size:A4;margin:0}
:root{--ink:#1E2420;--mute:#5F6862;--rule:#DDE3DE;--dk:#183327;--acc:#2C6D3F;--tint:#EDF3EE;--lt:#C9DACE;--gold:#B08A2E}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:210mm;background:#fff;color:var(--ink);font-family:'Bitstream Charter','Charter','Liberation Serif',serif;font-size:8.7pt;line-height:1.36;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{display:grid;grid-template-columns:62mm 1fr;grid-template-areas:"side main";width:210mm;height:297mm;overflow:hidden;page-break-after:always}
.page:last-child{page-break-after:auto}
aside{grid-area:side;background:var(--dk);color:#E6EEE8;padding:13mm 7mm 10mm 8.5mm;display:flex;flex-direction:column;gap:5.4mm}
main{grid-area:main;padding:13mm 12mm 9mm 11mm}
.foto{width:44mm;height:44mm;background:#ccc url(data:image/jpeg;base64,__FOTO__) center/cover;border-radius:50%;margin:0 auto 2mm;box-shadow:0 0 0 1mm var(--dk),0 0 0 1.4mm #D9B65C}
h1{font-family:Fr,'Liberation Serif',serif;font-weight:400;font-size:26pt;line-height:1.02;letter-spacing:-.5pt;color:var(--dk)}
.role{font-family:Inter,'Liberation Sans',sans-serif;font-size:6.9pt;letter-spacing:1.8pt;text-transform:uppercase;color:var(--gold);margin:3mm 0 1mm;font-weight:600}
.target{font-family:Fr,'Liberation Serif',serif;font-size:9.9pt;line-height:1.25;color:var(--ink)}
h2{font-family:Inter,'Liberation Sans',sans-serif;font-size:6.8pt;letter-spacing:1.7pt;text-transform:uppercase;font-weight:600;color:var(--dk);margin:0 0 2.4mm;display:flex;align-items:center;gap:2.5mm}
h2:before{content:"";width:5mm;height:.55mm;background:var(--gold)}
h2:after{content:"";flex:1;height:.25mm;background:var(--rule)}
aside h2{color:#EAD9A6;margin-bottom:2mm}aside h2:before{width:3mm}aside h2:after{background:#35584A}
aside p,aside li{font-size:8.1pt;line-height:1.38;color:#E6EEE8}
aside ul{list-style:none}aside li{margin-bottom:1.5mm}aside b{font-weight:700;color:#fff}
.k{display:block;font-family:Inter,'Liberation Sans',sans-serif;font-size:6.2pt;letter-spacing:.8pt;text-transform:uppercase;color:#9FC4AC;margin-bottom:.1mm}
aside .small{color:#AFC8B7}
section{margin-top:4.6mm}
p{margin-bottom:1.8mm}
.lead{font-size:9.6pt;line-height:1.42;color:var(--ink)}
.kw{display:flex;flex-wrap:wrap;gap:1.2mm;margin-top:2.4mm}
.kw span,.chips span{font-family:Inter,'Liberation Sans',sans-serif;font-size:6.6pt;border:.25mm solid #BFD3C5;color:var(--dk);padding:.6mm 2mm;border-radius:2.2mm 0 2.2mm 0;font-weight:500}
.chips{display:flex;flex-wrap:wrap;gap:1.1mm}
aside .chips span{border-color:#3C6350;color:#E6EEE8}
.match{display:grid;grid-template-columns:1fr 1fr;gap:3mm 5mm;counter-reset:m}
.match div{position:relative;border-top:.25mm solid var(--lt);padding:1.8mm 0 0 7mm;counter-increment:m}
.match div:before{content:counter(m,decimal-leading-zero);position:absolute;left:0;top:1.4mm;font-family:Fr,'Liberation Serif',serif;font-size:11pt;color:var(--gold);line-height:1}
.match b{display:block;font-family:Inter,'Liberation Sans',sans-serif;font-size:7.2pt;font-weight:600;color:var(--dk);line-height:1.25;margin-bottom:.7mm}
.match span{font-size:8pt;line-height:1.32;display:block;color:#2E3631}
.job{margin-bottom:3.2mm}
.jh{display:flex;justify-content:space-between;align-items:baseline;gap:4mm}
.jt{font-family:Inter,'Liberation Sans',sans-serif;font-weight:600;font-size:8.7pt;color:var(--dk);line-height:1.28}
.jd{font-family:Inter,'Liberation Sans',sans-serif;font-size:6.9pt;color:var(--mute);white-space:nowrap;letter-spacing:.2pt}
.jc{font-size:8.4pt;color:var(--mute);margin-bottom:1.2mm;font-style:italic}
ul.b{list-style:none}
ul.b li{position:relative;padding-left:3.4mm;margin-bottom:.9mm}
ul.b li:before{content:"";position:absolute;left:0;top:.62em;width:1.6mm;height:.28mm;background:var(--gold)}
.inss{border:.25mm solid #CFE0D3;background:var(--tint);padding:2.4mm 3.6mm 1.4mm;margin:1.4mm 0 2.4mm;border-radius:5mm 0 5mm 0}
.inss .tag{font-family:Inter,'Liberation Sans',sans-serif;font-size:6.3pt;letter-spacing:1.4pt;text-transform:uppercase;color:var(--acc);font-weight:600;margin-bottom:.6mm}
.inss .big{font-family:Fr,'Liberation Serif',serif;font-size:10.5pt;margin-bottom:.9mm;color:var(--dk)}
.small{font-size:8.2pt;color:var(--mute)}
.nums{display:flex;margin:1.8mm 0 1.8mm;border:.25mm solid var(--lt);border-radius:4mm 0 4mm 0;overflow:hidden}
.nums div{flex:1;padding:1.3mm 2mm 1.2mm;font-size:6.6pt;color:var(--mute);line-height:1.2;font-family:Inter,'Liberation Sans',sans-serif;border-right:.25mm solid var(--rule)}
.nums div:first-child{padding-left:2.4mm}.nums div:last-child{border-right:0}
.num{white-space:nowrap;font-family:Fr,'Liberation Serif',serif;font-size:13pt;line-height:1.05;color:var(--acc);display:block}
.tl{position:relative;height:21mm;margin:1mm 0 0}
.tlbars{position:relative;height:100%}
.tgrid{position:absolute;top:0;bottom:0;border-left:.2mm dotted #C5D0C8}
.seg{position:absolute;height:5mm;border-radius:2.4mm 0 2.4mm 0;overflow:hidden;display:flex;align-items:center;justify-content:center;font-family:Inter,'Liberation Sans',sans-serif;font-size:6pt;color:#fff;white-space:nowrap;font-weight:500}
.c1{background:#9DBBA6}.c2{background:#6E9A7E}.c3{background:#3F7F54}.c4{background:#7BA88A}.c5{background:var(--dk)}.c6{background:var(--gold)}.c7{background:#7A5C16}.c8{background:#D3DDD5}.c9{background:#BFD3C5}
.tlnote{position:absolute;left:0;right:0;top:5.5mm;font-family:Inter,'Liberation Sans',sans-serif;font-size:5.8pt;color:var(--mute)}
.tlnote span{position:absolute;white-space:nowrap}
.tlax{position:relative;height:3mm;font-family:Inter,'Liberation Sans',sans-serif;font-size:6pt;color:var(--mute);margin-top:.4mm}
'''
FOTO='__FOTO__'
HTML=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Alejandro Berruezo Márquez, CV</title><style>{CSS}</style></head><body>
<div class="page">
<main>
  <h1>Alejandro Berruezo Márquez</h1>
  <div class="role">Perfil profesional</div>
  <div class="target">Transformación digital, gobierno de tecnología e IA y desarrollo de negocio</div>
  <div class="kw"><span>Transformación digital</span><span>Gobierno de programas y tecnología</span><span>Preventa y desarrollo de negocio</span><span>IA y adopción</span><span>Innovación aplicada</span></div>

  <section><h2>Perfil</h2>
    <p class="lead">Llevo 30 años haciendo que la tecnología llegue al trabajo real en organizaciones con muchos actores y mucha regulación: sector público, banca privada, industria y servicios.</p>
    <p>Combino análisis, asesoría y gobierno de programas y plataformas con desarrollo de negocio: dirijo equipos de hasta 25 personas, programas de más de 300 profesionales y ofertas de gran tamaño. Ingeniero informático de formación, hoy me dedico al aterrizaje y la puesta en marcha de los modelos que implanto, hasta que alcanzan velocidad de crucero. Creo nuevos modelos de trabajo y llevo la innovación a programas reales con criterio escrito. Lo he formalizado en Synergós, mi método propio para dirigir transformaciones con IA, que publico cada semana.</p>
  </section>

  <section><h2>Lo que aporto</h2>
    <div class="match">
      <div><b>Gobierno de programas y modelos operativos</b><span>Gobierno de la transformación digital de la GISS, con un programa de más de 300 profesionales entre ingeniería, arquitectura, producto, operaciones y dirección del cliente.</span></div>
      <div><b>Preventa, ofertas y desarrollo de negocio</b><span>Más de 500 M€ en ofertas lideradas, con adjudicación cercana al 50 %, y propuestas de más de 30 M€. En Getronics, 3.800 oportunidades al año y tasa de éxito del 11 al 19 %.</span></div>
      <div><b>Alianzas y ecosistemas</b><span>Más de 30 partners al año con planes de negocio conjuntos en Getronics, con cerca de un 12 % más de oportunidades. Gobierno de plataformas y ecosistemas tecnológicos.</span></div>
      <div><b>Innovación y nuevos modelos de trabajo</b><span>MINEsait dentro de Minsait: innovación colaborativa e intraemprendimiento. Cartera de más de 50 soluciones de transformación digital en Getronics.</span></div>
      <div><b>IA y adopción</b><span>Uso diario de IA generativa y método propio (Synergós): puertas de decisión, escala de autonomía, registro y derecho a parar. Análisis de riesgos de uso y de normativa europea.</span></div>
      <div><b>Procedimientos, calidad y control</b><span>Definición, implantación y auditoría de procedimientos de oportunidades y de proyectos (Getronics). ITIL certificado, ISO 9001 y CMMi.</span></div>
    </div>
  </section>

  <section><h2>Experiencia</h2>
    <div class="job">
      <div class="jh"><span class="jt">Senior Manager / Principal, Transformación Digital, Preventa y Proyectos</span><span class="jd">Jun 2019 a hoy</span></div>
      <div class="jc">Minsait (Indra), Madrid, modelo híbrido</div>
      <div class="nums">
        <div><span class="num">+500 M€</span>en ofertas lideradas</div>
        <div><span class="num">≈50 %</span>de adjudicación en oportunidades clave</div>
        <div><span class="num">+30 M€</span>propuestas de mayor tamaño</div>
        <div><span class="num">+12</span>personas en equipos de oferta</div>
        <div><span class="num">400</span>personas en servicios ofertados</div>
      </div>
      <div class="inss">
        <div class="tag">Proyecto destacado</div>
        <div class="big">Transformación digital de la GISS</div>
        <ul class="b">
          <li>Gerencia de Informática de la Seguridad Social (GISS): liderazgo de un programa de más de 300 profesionales.</li>
          <li>Modelo de gobierno entre ingeniería, arquitectura, producto, operaciones y la dirección del cliente. Acompañamiento a su comité de dirección en las decisiones de cada fase.</li>
        </ul>
      </div>
      <ul class="b">
        <li>Gobierno de plataformas, productos y ecosistemas tecnológicos; estrategias de transformación, modelos objetivo y hojas de ruta ejecutables en sector público y grandes entornos regulados.</li>
        <li><b>Nuevos modelos de trabajo.</b> Creación de MINEsait dentro de Minsait: un ecosistema de innovación colaborativa e intraemprendimiento que cambia cómo se organizan y colaboran los equipos.</li>
        <li><b>Innovación aplicada y bajo método.</b> La llevo a programas reales con criterios escritos, responsables y puertas de decisión, el enfoque que he formalizado en Synergós.</li>
      </ul>
    </div>
  </section>
</main>
<aside>
  <div class="foto" role="img" aria-label="Alejandro Berruezo"></div>
  <div><h2>Contacto</h2>
    <ul>
      <li><span class="k">Ciudad</span>Madrid</li>
      <li><span class="k">Teléfono</span>+34 620 316 370</li>
      <li><span class="k">Correo</span>aberruezo@gmail.com</li>
      <li><span class="k">LinkedIn</span>linkedin.com/in/alejandro-berruezo</li>
    </ul></div>
  <div><h2>Idiomas</h2>
    <ul>
      <li><b>Castellano</b>, nativo</li>
      <li><b>Inglés</b>, competencia profesional (B2)<br><span class="small">First Certificate, Universidad de Edimburgo</span></li>
    </ul></div>
  <div><h2>Multisectorial</h2>
    <p>Mis modelos no están circunscritos a un sector. Tienen una parte de negocio que requiere aterrizaje, y no preveo que adaptarme a la banca sea un problema.</p>
    <div class="chips" style="margin-top:2mm"><span>Administración Pública</span><span>Seguridad Social</span><span>Banca privada</span><span>Industria</span><span>Sanidad y servicios</span><span>Retail</span></div></div>
  <div><h2>Tecnología</h2>
    <ul>
      <li>Cloud, API management, microservicios y DevOps</li>
      <li>Big data y analítica</li>
      <li>Metodologías ágiles, Scrum y Lean</li>
      <li>IA generativa como herramienta de trabajo y análisis de sus riesgos</li>
    </ul></div>
</aside>
</div>

<div class="page">
<main>
  <section style="margin-top:0"><h2>Trayectoria</h2>{tl}
    <div class="tlax">{ticks}</div>
  </section>

  <section><h2>Experiencia</h2>
    <div class="job">
      <div class="jh"><span class="jt">Senior Manager y Presales Manager</span><span class="jd">Sep 2018 a may 2019</span></div>
      <div class="jc">Enzyme Advising Group, Madrid</div>
      <div class="nums">
        <div><span class="num">≈10</span>personas en la oficina de Madrid</div>
        <div><span class="num">≈25</span>oportunidades en cartera</div>
        <div><span class="num">0,8 a 0,9 M€</span>de volumen total aproximado</div>
      </div>
      <ul class="b"><li>Puesta en marcha de la oficina de Madrid, con soporte de servicios desde Barcelona: preventa, desarrollo de negocio y relación con las cuentas estratégicas.</li></ul>
    </div>
    <div class="job">
      <div class="jh"><span class="jt">Presales, Alliances &amp; Offering Director</span><span class="jd">May 2012 a feb 2017</span></div>
      <div class="jc">Getronics, Madrid</div>
      <div class="nums">
        <div><span class="num">25</span>personas a cargo</div>
        <div><span class="num">3.800</span>oportunidades al año</div>
        <div><span class="num">+400 M€</span>de volumen</div>
        <div><span class="num">11 a 19 %</span>tasa de éxito</div>
        <div><span class="num">-20 %</span>coste del área en 3 años</div>
      </div>
      <ul class="b">
        <li>Dirección del área de preventa, desarrollo de negocio y consultoría.</li>
        <li>Estrategia de alianzas, casi inexistente hasta entonces: más de 30 partners al año con planes conjuntos y seguimiento de compromisos, cerca de un 12 % más de oportunidades.</li>
        <li>Cartera de más de 50 soluciones de transformación digital, con un 8 % más de oportunidades al año. Integración de equipos y procesos.</li>
      </ul>
    </div>
    <div class="job">
      <div class="jh"><span class="jt">Presales &amp; Bid Director</span><span class="jd">Dic 2010 a may 2012</span></div>
      <div class="jc">Getronics, Madrid</div>
      <ul class="b"><li>Preventa nacional con foco en Administración Pública. Definición, implantación y auditoría de los procedimientos de gestión de oportunidades.</li></ul>
    </div>
    <div class="job">
      <div class="jh"><span class="jt">Presales Manager</span><span class="jd">Jun 2006 a nov 2010</span></div>
      <div class="jc">Getronics (antes Thales), Madrid</div>
      <ul class="b"><li>Coordinación de la preventa técnica; definición, puesta en marcha y auditoría de procedimientos de oportunidades y proyectos.</li></ul>
    </div>
    <div class="job">
      <div class="jh"><span class="jt">Presales Engineer, Consultant y Project Manager</span><span class="jd">Feb 1998 a may 2006</span></div>
      <div class="jc">Nexus IT y después Business Integration (BT), Madrid</div>
      <ul class="b"><li>Soluciones, estimación y gestión de proyectos; planes de calidad, manuales operativos y transición de servicios.</li></ul>
    </div>
    <div class="job">
      <div class="jh"><span class="jt">Programador</span><span class="jd">1997 a 1998</span></div>
      <div class="jc">Thales, Madrid</div>
      <ul class="b"><li>Desarrollo en la GISS, el organismo que gobierno desde 2019.</li></ul>
    </div>
    <div class="job">
      <div class="jh"><span class="jt">Programador Natural y Adabas</span><span class="jd">1996 a 1997</span></div>
      <div class="jc">Software AG, Madrid</div>
      <ul class="b"><li>Desarrollo para Telefónica.</li></ul>
    </div>
  </section>

  <section><h2>Emprendimiento personal y profesional</h2>
    <div class="job">
      <div class="jh"><span class="jt">Fundador, Synergós</span><span class="jd">2024 a hoy</span></div>
      <div class="jc">Método propio para dirigir transformaciones con IA, con origen en MINEsait. Versión 1.5</div>
      <ul class="b">
        <li><b>Gobierno.</b> Comité de puertas integrado en el gobierno del programa. Inventario de sistemas y riesgos con una columna de personas y conocimiento.</li>
        <li><b>Autonomía y decisión.</b> Cuatro niveles; cada subida exige criterio, responsable y registro. Antes de aprobar, si la herramienta acelera, automatiza o aumenta.</li>
      </ul>
    </div>
    <div class="job">
      <div class="jh"><span class="jt">Cofundador, Hestía, your home!</span><span class="jd">Dic 2016 a hoy</span></div>
      <div class="jc">Vera Playa, Almería</div>
      <ul class="b"><li>Alojamiento turístico propio, en marcha desde hace casi diez años y convertido en referencia local: operación, comercialización y relación con clientes.</li></ul>
    </div>
  </section>
</main>
<aside>
  <div><h2>Formación</h2>
    <ul>
      <li><b>Ingeniero Superior en Informática</b><br>Universidad Autónoma de Madrid, 1992 a 1996</li>
      <li><b>Advanced Management Program</b><br>IE Business School, 2017</li>
      <li><b>Programa Directivo de Administración de Empresas</b><br>IE Business School, 2017</li>
      <li><b>Máster en Big Data y Business Analytics</b><br>MSMK, 2017 a 2018</li>
      <li><b>Excelencia operativa</b><br>BTS, 2025</li>
    </ul></div>
  <div><h2>Certificaciones</h2>
    <ul>
      <li>Certified Scrum Master, Scrum Alliance, 2018</li>
      <li>Design Thinking Professional, CertiProf, 2024</li>
      <li>ITIL, EXIN, 2008</li>
      <li>UML, Garben, 2005</li>
    </ul></div>
  <div><h2>Marcos y normas</h2>
    <ul>
      <li>ITIL, ISO 9001, CMMi</li>
      <li>Reglamento europeo de IA, en el método Synergós</li>
      <li>Seguridad: cifrado, firma electrónica, certificados</li>
      <li>Banca: conceptos de PSD2</li>
    </ul></div>
  <div><h2>Competencias</h2>
    <div class="chips"><span>Casos de negocio y medición del valor</span><span>Gestión del cambio</span><span>Propuestas complejas</span><span>Design Thinking</span><span>Comunidades de práctica</span></div></div>
</aside>
</div>
</body></html>'''
open('cv4.tpl.html','w',encoding='utf-8').write(HTML)
