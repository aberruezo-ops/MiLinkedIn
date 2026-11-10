import io
S,E=1996.5,2026.9
def pct(x): return (x-S)/(E-S)*100
def bar(a,b,label,cls,row):
    return f'<div class="seg {cls}" style="left:{pct(a):.2f}%;width:{pct(b)-pct(a):.2f}%;top:{row}mm"><span>{label}</span></div>'
segs=[bar(1996.67,1998.08,'Thales','c1',0),bar(1998.08,2006.42,'Nexus IT y Business Integration','c2',0),
bar(2006.42,2017.13,'Getronics','c3',0),bar(2018.67,2019.42,'','c4',0),bar(2019.42,2026.85,'Minsait (Indra)','c5',0),
bar(2016.92,2026.85,'Hestía, your home!','c6',9),bar(2025.9,2026.85,'','c7',16)]
ticks=''.join(f'<span style="position:absolute;left:{pct(y):.2f}%;transform:translateX(-50%)">{y}</span>' for y in (2000,2006,2010,2016,2020,2026))
tl=f'''<div class="tl"><div class="tlbars">{"".join(segs)}</div>
<div class="tlnote"><span style="left:{pct(2016.9):.2f}%">máster Big Data 2017 a 2018</span><span style="right:{100-pct(2025.9)+1:.2f}%;top:9.6mm">Synergós, 2026</span></div></div>'''
CSS='''
@font-face{font-family:Fr;src:url('file:///home/user/MiLinkedIn/synergos/imagenes/fonts/Fraunces.ttf')}
@page{size:A4;margin:0}
:root{--ink:#1F1D1A;--mute:#5E625F;--rule:#D5DBD6;--dk:#1B3A29;--acc:#2C6D3F;--tint:#E8F0EA;--lt:#CFE0D3}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:210mm;background:#fff;color:var(--ink);font-family:'Bitstream Charter','Charter','Liberation Serif',serif;font-size:8.7pt;line-height:1.33;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{display:grid;grid-template-columns:64mm 1fr;grid-template-areas:"side main";width:210mm;height:297mm;overflow:hidden;page-break-after:always}
.page:last-child{page-break-after:auto}
aside{grid-area:side;background:var(--dk);color:#EAF1EC;padding:12mm 7mm 10mm 8.5mm;display:flex;flex-direction:column;gap:5mm}
main{grid-area:main;padding:12mm 12mm 9mm 10mm}
.foto{width:46mm;height:46mm;background:#ccc url(data:image/jpeg;base64,__FOTO__) center/cover;border-radius:50%;margin:0 auto 1.5mm;box-shadow:0 0 0 .9mm var(--dk),0 0 0 1.5mm #EAF1EC}
h1{font-family:Fr,'Liberation Serif',serif;font-weight:400;font-size:25pt;line-height:1.04;letter-spacing:-.4pt;color:var(--dk)}
.role{font-family:Inter,'Liberation Sans',sans-serif;font-size:7.4pt;letter-spacing:.9pt;text-transform:uppercase;color:var(--acc);margin:2.6mm 0 1mm;font-weight:600}
.target{font-size:10.1pt;line-height:1.3}
h2{font-family:Inter,'Liberation Sans',sans-serif;font-size:7.1pt;letter-spacing:1.3pt;text-transform:uppercase;font-weight:600;color:var(--acc);margin:0 0 2mm;display:flex;align-items:center;gap:2.5mm}
h2:after{content:"";flex:1;height:.3mm;background:var(--lt)}
aside h2{color:#9CC9A8;margin-bottom:1.8mm}aside h2:after{background:#3C6350}
aside p,aside li{font-size:8.2pt;line-height:1.35;color:#EAF1EC}
aside ul{list-style:none}aside li{margin-bottom:1.4mm}aside b{font-weight:700;color:#fff}
.k{display:block;font-family:Inter,'Liberation Sans',sans-serif;font-size:6.4pt;letter-spacing:.7pt;text-transform:uppercase;color:#9CC9A8;margin-bottom:.1mm}
aside .small{color:#B9D0C0}
section{margin-top:3.8mm}
p{margin-bottom:1.8mm}
.lead{font-size:9.5pt;line-height:1.4}
.kw{display:flex;flex-wrap:wrap;gap:1.2mm;margin-top:2.2mm}
.kw span,.chips span{font-family:Inter,'Liberation Sans',sans-serif;font-size:6.9pt;background:var(--tint);color:var(--dk);padding:.7mm 2mm;border-radius:2mm;font-weight:500}
.chips{display:flex;flex-wrap:wrap;gap:1.1mm}
aside .chips span{background:#2A5640;color:#EAF1EC}
.match{display:grid;grid-template-columns:1fr 1fr;gap:1.8mm}
.match div{border-top:.7mm solid var(--acc);background:#F5F8F5;padding:1.3mm 2.2mm 1.4mm}
.match b{display:block;font-family:Inter,'Liberation Sans',sans-serif;font-size:7.2pt;font-weight:600;color:var(--dk);line-height:1.25;margin-bottom:.6mm}
.match span{font-size:8pt;line-height:1.3;display:block}
.job{margin-bottom:3mm}
.jh{display:flex;justify-content:space-between;align-items:baseline;gap:4mm}
.jt{font-weight:700;font-size:9.4pt;color:var(--dk)}
.jd{font-family:Inter,'Liberation Sans',sans-serif;font-size:7pt;color:var(--mute);white-space:nowrap}
.jc{font-size:8.5pt;color:var(--mute);margin-bottom:1.1mm;font-style:italic}
ul.b{list-style:none}
ul.b li{position:relative;padding-left:3.4mm;margin-bottom:.9mm}
ul.b li:before{content:"";position:absolute;left:0;top:.62em;width:1.7mm;height:.28mm;background:var(--acc)}
.inss{border-left:.9mm solid var(--acc);background:var(--tint);padding:2.2mm 3.2mm 1.2mm;margin:1.4mm 0 2.2mm;border-radius:0 1.5mm 1.5mm 0}
.inss .tag{font-family:Inter,'Liberation Sans',sans-serif;font-size:6.6pt;letter-spacing:1pt;text-transform:uppercase;color:var(--acc);font-weight:600;margin-bottom:.6mm}
.inss .big{font-weight:700;font-size:9.3pt;margin-bottom:.8mm;color:var(--dk)}
.small{font-size:8.2pt;color:var(--mute)}
.nums{display:flex;gap:0;margin:1.8mm 0 1.6mm;border:.25mm solid var(--rule);border-radius:1.5mm;overflow:hidden}
.nums div{flex:1;padding:1.2mm 1.8mm;font-size:6.9pt;color:var(--mute);line-height:1.2;font-family:Inter,'Liberation Sans',sans-serif;border-right:.25mm solid var(--rule)}
.nums div:last-child{border-right:0}
.nums.in{background:#fff;border-color:#BCD2C2;margin-top:1mm}
.num{white-space:nowrap;font-family:Fr,'Liberation Serif',serif;font-size:12.5pt;line-height:1.05;color:var(--acc);display:block}
.tl{position:relative;height:23mm;margin:1mm 0 1mm}
.tlbars{position:relative;height:100%}
.seg{position:absolute;height:6mm;border-radius:1mm;overflow:hidden;display:flex;align-items:center;justify-content:center;font-family:Inter,'Liberation Sans',sans-serif;font-size:6.2pt;color:#fff;white-space:nowrap;font-weight:500}
.c1{background:#9DBBA6}.c2{background:#6F9B7F}.c3{background:#3F7F54}.c4{background:#7BA88A}.c5{background:var(--dk)}.c6{background:#B8860B;opacity:.9}.c7{background:#7A5A07}
.tlnote{position:absolute;left:0;right:0;top:6.5mm;font-family:Inter,'Liberation Sans',sans-serif;font-size:6pt;color:var(--mute)}
.tlnote span{position:absolute;white-space:nowrap}
.tlax{position:relative;height:3mm;font-family:Inter,'Liberation Sans',sans-serif;font-size:6.2pt;color:var(--mute);margin-top:.5mm}
.legend{font-family:Inter,'Liberation Sans',sans-serif;font-size:6.2pt;color:var(--mute);margin-top:.4mm}
.tlseg2{font-family:Inter,'Liberation Sans',sans-serif}
'''
FOTO='__FOTO__'
HTML=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Alejandro Berruezo Márquez, CV</title><style>{CSS}</style></head><body>
<div class="page">
<main>
  <h1>Alejandro Berruezo Márquez</h1>
  <div class="role">Candidatura</div>
  <div class="target">Head of Governance &amp; Orchestration (Agentic Organization), Santander, CDAIO</div>
  <div class="kw"><span>Análisis, asesoría y gobierno de tecnología e IA</span><span>Modelo operativo</span><span>Estándares, trazabilidad y auditoría</span><span>Comunidades de práctica y adopción</span></div>

  <section><h2>Perfil</h2>
    <p class="lead">Llevo 30 años haciendo que la tecnología llegue al trabajo real en organizaciones con muchos actores y mucha regulación: sector público, con especial peso de la Seguridad Social (GISS), banca privada, industria y servicios sociales.</p>
    <p>Más de 15 años en análisis, asesoría y gobierno de programas, plataformas y procedimientos tecnológicos: defino criterios, roles y control, y lidero equipos de hasta 25 personas y programas de más de 300 profesionales. Ingeniero informático de formación, hoy me dedico al aterrizaje y la puesta en marcha de los modelos que implanto, hasta que alcanzan velocidad de crucero. Encaja con una organización agéntica (AI governance): nada pasa a producción sin criterio escrito antes, cada decisión tiene responsable y registro, y quien trabaja con el sistema puede pararlo. Lo he formalizado en Synergós, mi método propio, que publico cada semana.</p>
  </section>

  <section><h2>Lo que pide el puesto y lo que aporto</h2>
    <div class="match">
      <div><b>Modelo operativo, roles, estándares y criterios para pasar a producción</b><span>Gobierno de la transformación digital de la GISS. En Synergós, puertas con criterios firmados antes y tres salidas: escalar, ajustar o retirar.</span></div>
      <div><b>Decisiones documentadas, trazabilidad y auditoría</b><span>Definición, implantación y auditoría de procedimientos (Getronics). ITIL certificado, ISO 9001 y CMMi. En Synergós, registro de riesgos y decisiones con firma de patrocinador y responsable.</span></div>
      <div><b>Revisión independiente y reparto de funciones</b><span>Derechos de decisión escritos: quién decide, quién ejecuta y quién mide. Firma doble (patrocinador y persona sin interés en la iniciativa) para retirar un piloto.</span></div>
      <div><b>Control de agentes y riesgos de aplicaciones con LLM</b><span>Escala de autonomía en cuatro niveles con criterio, responsable y registro antes de cada subida, y derecho a parar. Análisis del uso sin comprobar y del uso oculto. Uso diario de IA generativa.</span></div>
      <div><b>Normativa de IA y sector regulado</b><span>Gestión de riesgos alineada con el Reglamento europeo de IA en el método Synergós. Banca privada y conceptos de PSD2; seguridad (cifrado, firma, certificados).</span></div>
      <div><b>Coordinación sin jerarquía, comunidad y adopción</b><span>Programa de más de 300 profesionales (GISS). MINEsait dentro de Minsait: innovación colaborativa e intraemprendimiento. Innovación aplicada bajo método.</span></div>
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
  <div><h2>Idiomas</h2>
    <ul>
      <li><b>Castellano</b>, nativo</li>
      <li><b>Inglés</b>, competencia profesional (B2)<br><span class="small">First Certificate, Universidad de Edimburgo</span></li>
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
      <div class="jh"><span class="jt">Minsait (Indra), continuación</span><span class="jd">Jun 2019 a hoy</span></div>
      <ul class="b">
        <li><b>Innovación aplicada y bajo método.</b> La llevo a programas reales con criterios escritos, responsables y puertas de decisión, el enfoque que he formalizado en Synergós.</li>
      </ul>
    </div>
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
        <li>Estrategia de alianzas, casi inexistente hasta entonces: más de 30 partners al año con planes de negocio conjuntos, objetivos compartidos y seguimiento de compromisos, que aportaron cerca de un 12 % más de oportunidades.</li>
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
      <div class="jc">Getronics, Madrid</div>
      <ul class="b"><li>Coordinación de la preventa técnica; definición, puesta en marcha y auditoría de procedimientos de oportunidades y proyectos.</li></ul>
    </div>
    <div class="job">
      <div class="jh"><span class="jt">Presales Engineer, Consultant y Project Manager</span><span class="jd">Feb 1998 a may 2006</span></div>
      <div class="jc">Nexus IT y Business Integration, Madrid</div>
      <ul class="b"><li>Soluciones, estimación y gestión de proyectos; planes de calidad, manuales operativos y transición de servicios.</li></ul>
    </div>
    <div class="job">
      <div class="jh"><span class="jt">Programador</span><span class="jd">Sep 1996 a feb 1998</span></div>
      <div class="jc">Thales y Software AG, Madrid</div>
      <ul class="b"><li>Desarrollo para la Gerencia de Informática de la Seguridad Social (GISS) y para Telefónica.</li></ul>
    </div>
  </section>

  <section><h2>Emprendimiento personal y profesional</h2>
    <div class="job">
      <div class="jh"><span class="jt">Fundador, Synergós</span><span class="jd">Oct 2026 a hoy</span></div>
      <div class="jc">Método propio para dirigir transformaciones con IA. Versión 1.5, 81 páginas, publicación semanal en LinkedIn</div>
      <ul class="b">
        <li><b>Gobierno.</b> Comité de puertas integrado en el gobierno del programa. Inventario de sistemas y riesgos con una columna de personas y conocimiento.</li>
        <li><b>Autonomía.</b> Cuatro niveles; cada subida exige criterio, responsable y registro para auditar.</li>
        <li><b>Decisión.</b> Antes de aprobar: si la herramienta acelera, automatiza o aumenta.</li>
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
  <div><h2>Multisectorial</h2>
    <p>Mis modelos no están circunscritos a un sector. Tienen una parte de negocio que requiere aterrizaje, y no preveo que adaptarme a la banca sea un problema.</p>
    <div class="chips" style="margin-top:2mm"><span>Administración Pública</span><span>Seguridad Social</span><span>Banca privada</span><span>Industria</span><span>Sanidad y servicios</span><span>Retail</span></div></div>
  <div><h2>Conocimiento técnico</h2>
    <ul>
      <li>Cloud, API management, microservicios y DevOps</li>
      <li>Big data y analítica</li>
      <li>Metodologías ágiles, Scrum y Lean</li>
      <li>IA generativa como herramienta de trabajo y análisis de sus riesgos</li>
    </ul></div>
  <div><h2>Marcos y normas</h2>
    <ul>
      <li>ITIL, ISO 9001, CMMi</li>
      <li>Reglamento europeo de IA, en el método Synergós</li>
      <li>Seguridad: cifrado, firma electrónica, certificados</li>
      <li>Banca: conceptos de PSD2</li>
    </ul></div>
  <div><h2>Otras competencias</h2>
    <div class="chips"><span>Casos de negocio y medición del valor</span><span>Gestión del cambio</span><span>Propuestas complejas</span><span>Design Thinking</span><span>Comunidades de práctica</span></div></div>
</aside>
</div>
</body></html>'''
open('cv2.tpl.html','w',encoding='utf-8').write(HTML)
