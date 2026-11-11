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
legend=[('prog','1996 to 1998','Software AG and Thales','Programmer, with Telefónica and the GISS as clients'),
('nexus','1998 to 2006','Nexus IT and Business Integration (BT)','Presales, consulting and projects'),
('getr','2006 to 2017','Getronics (formerly Thales)','From presales to leading alliances and offers'),
('trans','2017 to 2019','Studies and Enzyme','Big Data master\'s and nine months setting up an office'),
('mins','2019 to present','Minsait (Indra)','Governance of the GISS digital transformation')]
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
HTML=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Alejandro Berruezo Márquez, CV</title><style>{CSS}</style></head><body>
<div class="page">
<header>
  <div><h1>Alejandro Berruezo Márquez</h1>
  <div class="role">Commercial transformation, program governance and adoption</div></div>
  <div class="foto" role="img" aria-label="Alejandro Berruezo"></div>
</header>
<div class="contact"><span>Madrid, Spain</span><span>+34 620 316 370</span><span>aberruezo@gmail.com</span><span>linkedin.com/in/alejandro-berruezo</span></div>

<div class="row"><div class="lab">Profile</div><div>
  <p class="lead">For 30 years I have been getting technology into real work in organizations with many stakeholders and heavy regulation: public sector, private banking, industry and services.</p>
  <p>I turn strategic objectives into executable plans and make sure they are adopted. I have run commercial processes at scale (3,800 opportunities a year at Getronics), led bids of more than €500M in total and governed a program of more than 300 professionals. I am a computer engineer with a master's in Big Data and Business Analytics. Today I focus on landing the models I implement and getting them running, until they reach cruising speed, and I formalized how in Synergós, my own method for leading transformations.</p>
</div></div>

<div class="row"><div class="lab">What I bring</div><div class="apt">
  <div><h3>Commercial processes and go-to-market</h3><p>Defined, implemented and audited opportunity-management procedures at Getronics: 3,800 opportunities a year, a win rate of 11 to 19% and a portfolio of more than 50 solutions. Presales, offers and bids with teams of up to 25 people.</p></div>
  <div><h3>Program governance</h3><p>Governance of the GISS digital transformation, with more than 300 professionals. Gate committee with prior criteria, owners, dependencies, risks and a decision log, with escalation paths.</p></div>
  <div><h3>Aligning senior stakeholders</h3><p>Support to the GISS steering committee on the decisions of each phase. Proposals above €30M with bid teams of more than 12 people, coordinating internal teams and partners.</p></div>
  <div><h3>Delivery, adoption and handover</h3><p>Landing and launching the models I implement until they run at cruising speed. Written criteria for scaling, adjusting or withdrawing, so work moves into the permanent operating model.</p></div>
  <div><h3>Partners and ecosystems</h3><p>More than 30 partners a year with joint plans and commitment tracking at Getronics, about 12% more opportunities. MINEsait inside Minsait, a collaborative ecosystem.</p></div>
  <div><h3>Measuring outcomes</h3><p>Business cases and measurement with a baseline and paired indicators, reported as progress toward each target. ITIL certified, ISO 9001 and CMMi.</p></div>
</div></div>

<div class="row job"><div class="dt"><b>Jun 2019 to present</b>Madrid, hybrid</div><div>
  <div class="ti">Senior Manager / Principal, Digital Transformation, Presales and Projects</div>
  <div class="co">Minsait (Indra)</div>
  <div class="fig"><div><b>+€500M</b>in bids led</div><div><b>≈50%</b>win rate on key opportunities</div><div><b>+€30M</b>largest proposals</div><div><b>+12</b>people on bid teams</div><div><b>400</b>people in the services bid</div></div>
  <div class="box"><div class="ti">Digital transformation of the GISS</div>
    <ul class="b"><li>Spain's Social Security IT Management (GISS): leading a program of more than 300 professionals.</li>
    <li>Governance model across engineering, architecture, product, operations and the client's leadership, and support to its steering committee on the decisions of each phase.</li></ul></div>
  <ul class="b">
    <li>Governance of technology platforms, products and ecosystems; transformation strategies, target models and executable roadmaps in the public sector and large regulated environments.</li>
    <li><b>New ways of working.</b> Creation of MINEsait inside Minsait, a collaborative innovation and intrapreneurship ecosystem that changes how teams organize and work together.</li>
    <li><b>Applied innovation, with method.</b> I take it into real programs with written criteria, owners and decision gates, the approach I have formalized in Synergós.</li>
  </ul></div></div>
</div>

<div class="page">
<div class="row" style="margin-top:0"><div><div class="lab" style="margin-bottom:2mm">Career</div>{SVG}</div><div style="padding-top:7mm"><ul class="legend">{LEG}</ul>
<div class="cap">One seed per year, 1996 to 2026, placed at the golden angle of 137.5 degrees, the same as the Synergós sunflower.</div></div></div>

<div class="row"><div class="lab">Before Minsait</div><div>
  <div class="job" style="margin-bottom:2.4mm"><div class="ti hd"><span>Senior Manager and Presales Manager</span><span class="dt">Sep 2018 to May 2019</span></div><div class="co">Enzyme Advising Group, Madrid</div>
    <div class="fig" style="margin-top:.8mm"><div><b>≈10</b>people in the Madrid office</div><div><b>≈25</b>opportunities in the pipeline</div><div><b>€0.8 to 0.9M</b>approximate total volume</div></div>
    <ul class="b"><li>Set up the Madrid office, with services support from Barcelona: presales, business development and strategic accounts.</li></ul></div>
  <div class="job" style="margin-bottom:2.4mm"><div class="ti hd"><span>Presales, Alliances &amp; Offering Director</span><span class="dt">May 2012 to Feb 2017</span></div><div class="co">Getronics, Madrid</div>
    <div class="fig" style="margin-top:.8mm"><div><b>25</b>people in charge</div><div><b>3,800</b>opportunities a year</div><div><b>+€400M</b>volume</div><div><b>11 to 19%</b>win rate</div><div><b>-20%</b>area cost in 3 years</div></div>
    <ul class="b"><li>Led presales, business development and consulting.</li>
    <li>Alliances, almost nonexistent until then: more than 30 partners a year with joint plans and commitment tracking, about 12% more opportunities.</li>
    <li>Portfolio of more than 50 digital transformation solutions, with 8% more opportunities a year. Integration of teams and processes.</li></ul></div>
  <div class="old"><div class="ti hd"><span>Presales &amp; Bid Director</span><span class="dt">Dec 2010 to May 2012</span></div><p>Getronics. National presales focused on Public Administration. Defined, implemented and audited the opportunity-management procedures.</p></div>
  <div class="old"><div class="ti hd"><span>Presales Manager</span><span class="dt">Jun 2006 to Nov 2010</span></div><p>Getronics (formerly Thales). Coordinated technical presales; defined, launched and audited opportunity and project procedures.</p></div>
  <div class="old"><div class="ti hd"><span>Presales Engineer, Consultant and Project Manager</span><span class="dt">Feb 1998 to May 2006</span></div><p>Nexus IT and later Business Integration (BT). Solutions, estimating and project management; quality plans, operating manuals and service transition.</p></div>
  <div class="old"><div class="ti hd"><span>Programmer</span><span class="dt">1996 to 1998</span></div><p>Software AG (Natural and Adabas, for Telefónica) and Thales (at the GISS, the body I have governed since 2019).</p></div>
</div></div>

<div class="row"><div class="lab">Entrepreneurship</div><div>
  <div class="old"><div class="ti hd"><span>Founder, Synergós</span><span class="dt">2024 to present</span></div><p>Own method for leading transformations with AI, rooted in MINEsait. Version 1.5. Gate committee built into program governance, a four-level autonomy scale with criteria, owner and log, and an inventory of systems and risks with a people and knowledge column.</p></div>
  <div class="old"><div class="ti hd"><span>Co-founder, Hestía, your home!</span><span class="dt">Dec 2016 to present</span></div><p>Own tourist accommodation in Vera Playa, Almería, running for almost ten years and a local reference: operations, marketing and customer relations.</p></div>
</div></div>

<div class="row"><div class="lab">Education and skills</div><div class="cols3">
  <div><h4>Education</h4><ul><li>Computer Engineering (Ingeniero Superior en Informática), Universidad Autónoma de Madrid, 1996</li><li>Advanced Management Program and Executive Business Administration Program, IE Business School, 2017</li><li>Master in Big Data and Business Analytics, MSMK, 2018</li><li>Operational excellence, BTS, 2025</li></ul></div>
  <div><h4>Certifications and languages</h4><ul><li>Certified Scrum Master, 2018</li><li>Design Thinking Professional, 2024</li><li>ITIL (EXIN), 2008</li><li>Spanish native; English B2, First Certificate, University of Edinburgh</li></ul></div>
  <div><h4>Sectors and technology</h4><div class="chips" style="margin:0 0 1.4mm"><span>Public Administration</span><span>Social Security</span><span>Private banking</span><span>Industry</span><span>Health and services</span><span>Retail</span></div><p>Cloud, APIs, DevOps, big data, Scrum and Lean, generative AI, ITIL, ISO 9001 and CMMi.</p></div>
</div></div>
</div>
</body></html>'''
open('cv9.tpl.html','w',encoding='utf-8').write(HTML)
