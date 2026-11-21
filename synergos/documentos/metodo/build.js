// Construye el documento del método Synergós en .docx a partir de los ficheros 0*.md
const fs = require('fs'); const path = require('path');
const D = require('docx');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, ImageRun, Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, BorderStyle, PageBreak, Footer, Header, PageNumber, TableOfContents, LevelFormat, TabStopType } = D;

const INK = '1F1D1A', GREEN = '2C6D3F', LIGHT = '7CC090', GREY = '56606A', PALE = 'E8F1EB', LINE = 'D7DCDC';
const TERRA = 'B5512A', ALBERO = 'C89A2A', ALBT = '8A6508', TERRAPALE = 'FBF1EC', SOFT = 'F4F6F6';
const HF = 'EB Garamond', BF = 'Public Sans', SF = 'Public Sans', BOLD = 'Public Sans SemiBold';
const FONTDIR = '/tmp/claude-0/-home-user-MiLinkedIn/8b3653e3-6315-50f3-96b3-ad0bde922485/scratchpad/ttf/';
const PAGE_W = 11906, MARGIN = 1418, TEXT_W = PAGE_W - 2 * MARGIN; // A4, 2,5 cm
const dir = __dirname;
const imgSize = { 'fig-arquitectura.png': [1600, 960], 'fig-fases.png': [1800, 620], 'fig-girasol.png': [1200, 1000], 'logo.png': [2000, 520], 'portada-girasol.png': [1600, 1300], 'portada-doc.png': [1240, 1754] };
const cmToPx = cm => Math.round(cm / 2.54 * 96);
const pngSize = f => { const b = fs.readFileSync(path.join(dir, f)); return [b.readUInt32BE(16), b.readUInt32BE(20)]; };

function runs(text, base = {}) {
  // **negrita** y *cursiva*
  const out = []; const re = /(\*\*[^*]+\*\*|\*[^*]+\*)/g; let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const t = m[0];
    if (t.startsWith('**')) out.push(new TextRun({ ...base, text: t.slice(2, -2), font: BOLD }));
    else out.push(new TextRun({ text: t.slice(1, -1), italics: true, ...base }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), ...base }));
  return out;
}
function image(file, widthCm, align = AlignmentType.CENTER) {
  const [w, h] = pngSize(file); const pw = cmToPx(widthCm);
  return new Paragraph({ alignment: align, spacing: { before: 160, after: 200 }, children: [new ImageRun({ type: 'png', data: fs.readFileSync(path.join(dir, file)), transformation: { width: pw, height: Math.round(pw * h / w) } })] });
}
const cellBorder = { style: BorderStyle.SINGLE, size: 4, color: LINE }; const noB = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
function colWidths(rows, MIN) {
  const n = rows[0].length;
  const lens = Array.from({ length: n }, (_, i) => Math.min(70, Math.max(12, rows.slice(1).reduce((a, r) => a + (r[i] || '').length, 0) / Math.max(1, rows.length - 1))));
  let fixed = new Array(n).fill(false), cols = new Array(n).fill(0);
  for (let it = 0; it < n; it++) {
    const freeTot = lens.reduce((a, l, i) => a + (fixed[i] ? 0 : l), 0), room = TEXT_W - cols.reduce((a, c, i) => a + (fixed[i] ? c : 0), 0);
    let again = false;
    lens.forEach((l, i) => { if (!fixed[i]) { cols[i] = Math.round(room * l / freeTot); } });
    lens.forEach((l, i) => { if (!fixed[i] && cols[i] < MIN) { cols[i] = MIN; fixed[i] = true; again = true; } });
    if (!again) break;
  }
  cols[n - 1] += TEXT_W - cols.reduce((a, c) => a + c, 0);
  return cols;
}
const gap = { style: BorderStyle.SINGLE, size: 18, color: 'FFFFFF' };
const SHADE = f => ({ type: ShadingType.CLEAR, fill: f, color: 'auto' });
function table(rows) {
  const n = rows[0].length;
  if (n >= 6) return fichas(rows);
  const cols = colWidths(rows, n > 3 ? 1500 : 2000);
  if (cols[0] < 2100) { const need = 2100 - cols[0]; let j = cols.indexOf(Math.max(...cols.slice(1))); cols[0] += need; cols[j] -= need; }
  const hair = { style: BorderStyle.SINGLE, size: 4, color: LINE };
  return new Table({
    width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: cols,
    rows: rows.map((r, ri) => new TableRow({
      tableHeader: ri === 0, cantSplit: true,
      children: r.map((c, ci) => new TableCell({
        width: { size: cols[ci], type: WidthType.DXA },
        shading: SHADE(ri === 0 ? TINT[curPart] : (ci === 0 ? DEEP[curPart] : 'F6F7F7')),
        margins: { top: 130, bottom: 130, left: 170, right: 150 },
        borders: { top: gap, bottom: gap, left: gap, right: gap },
        children: [new Paragraph({ spacing: { before: 0, after: 0, line: 270 }, children: runs(ri === 0 ? c.toUpperCase() : c, { font: (ri === 0 || ci === 0) ? BOLD : SF, size: ri === 0 ? 15 : 18, color: ri === 0 ? TXT[curPart] : (ci === 0 ? TXT[curPart] : INK), characterSpacing: ri === 0 ? 30 : 0 }) })]
      }))
    }))
  });
}
// Tablas de seis o más columnas: una ficha por fila (cabecera de color y pares etiqueta/valor)
function fichas(rows) {
  const head = rows[0], LW = 2500, VW = TEXT_W - LW, hair = { style: BorderStyle.SINGLE, size: 4, color: LINE };
  const tints = [GREEN, TERRA, INK, ALBT];
  const out = [];
  rows.slice(1).forEach((r, k) => {
    const rowsT = [new TableRow({ cantSplit: true, children: [new TableCell({ columnSpan: 2, width: { size: TEXT_W, type: WidthType.DXA }, shading: SHADE(tints[k % tints.length]), margins: { top: 150, bottom: 150, left: 200, right: 200 }, borders: { top: noB, bottom: noB, left: noB, right: noB },
      children: [new Paragraph({ keepNext: true, spacing: { before: 0, after: 0 }, children: runs(r[0], { font: HF, size: 30, color: 'FFFFFF' }) })] })] })];
    for (let j = 1; j < head.length; j++) {
      const last = j === head.length - 1;
      rowsT.push(new TableRow({ cantSplit: true, children: [
        new TableCell({ width: { size: LW, type: WidthType.DXA }, shading: SHADE('F4F6F6'), margins: { top: 110, bottom: 110, left: 200, right: 120 }, borders: { top: noB, bottom: hair, left: noB, right: noB },
          children: [new Paragraph({ keepNext: !last, spacing: { before: 0, after: 0, line: 250 }, children: [new TextRun({ text: head[j].toUpperCase(), font: BOLD, size: 14, color: GREEN, characterSpacing: 14 })] })] }),
        new TableCell({ width: { size: VW, type: WidthType.DXA }, margins: { top: 110, bottom: 110, left: 200, right: 160 }, borders: { top: noB, bottom: hair, left: noB, right: noB },
          children: [new Paragraph({ keepNext: !last, spacing: { before: 0, after: 0, line: 276 }, children: runs(r[j] || '', { font: SF, size: 18, color: INK }) })] }),
      ] }));
    }
    out.push(new Table({ width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: [LW, VW], rows: rowsT }));
    if (k < rows.length - 2) out.push(spacer(200));
  });
  return out;
}
function callout(title, body, color = TERRA, label = null) {
  let lab = label, head = title;
  if (!lab) { const m = /^Pregunta abierta\.\s*(.*)$/.exec(title); if (m) { lab = 'Pregunta abierta'; head = m[1]; } else { lab = 'Nota'; } }
  const W1 = 2600, W2 = TEXT_W - W1; const hair = { style: BorderStyle.SINGLE, size: 6, color: LINE };
  const left = [new Paragraph({ spacing: { before: 0, after: 80 }, children: [new TextRun({ text: lab.toUpperCase(), font: BOLD, size: 15, color, characterSpacing: 50 })] })];
  if (head) left.push(new Paragraph({ spacing: { before: 0, after: 0, line: 280 }, children: [new TextRun({ text: head, font: HF, size: 27, color: INK })] }));
  return new Table({ width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: [W1, W2], rows: [new TableRow({ cantSplit: true, children: [
    new TableCell({ width: { size: W1, type: WidthType.DXA }, shading: SHADE(color === TERRA ? TERRAPALE : PALE), margins: { top: 200, bottom: 200, left: 240, right: 280 }, borders: { top: noB, bottom: noB, left: noB, right: noB }, children: left }),
    new TableCell({ width: { size: W2, type: WidthType.DXA }, shading: SHADE(color === TERRA ? TERRAPALE : PALE), margins: { top: 200, bottom: 200, left: 0, right: 240 }, borders: { top: noB, bottom: noB, left: noB, right: noB }, children: [new Paragraph({ spacing: { before: 0, after: 0, line: 300 }, children: runs(body, { font: BF, size: 19, color: GREY }) })] }),
  ] })] });
}
const spacer = (after = 120) => new Paragraph({ spacing: { before: 0, after }, children: [] });


const ESENCIA = {
  'I': 'Casi todo lo que hace fracasar una transformación estaba ahí antes de que llegara la tecnología.',
  'II': 'Tres elementos que avanzan al mismo compás y un orden que los sostiene.',
  'III': 'Cinco fases. Al final de cada una, una puerta con criterios escritos antes.',
  'IV': 'Personas, conocimiento y tecnología pesan lo mismo. El orden decide si llegan juntos.',
  'V': 'Veinticuatro módulos para lo que el método toca en varias fases. Casi nunca hacen falta todos.',
  'VI': 'Las dudas, las críticas y lo que todavía falta por probar.'
};
function tricolor(h = 60) {
  const w = Math.floor(TEXT_W / 3); const nb = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
  return new Table({ width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: [w, w, TEXT_W - 2 * w],
    rows: [new TableRow({ height: { value: h, rule: 'exact' }, children: [TERRA, GREEN, ALBERO].map((c, i) => new TableCell({ width: { size: i < 2 ? w : TEXT_W - 2 * w, type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, color: 'auto', fill: c }, borders: { top: nb, bottom: nb, left: nb, right: nb }, children: [new Paragraph({ spacing: { before: 0, after: 0, line: 40 }, children: [] })] })) })] });
}
const TINT = { I: TERRAPALE, II: PALE, III: 'FAF3DF', IV: TERRAPALE, V: PALE, VI: 'FAF3DF' };
const DEEP = { I: 'F5E2D8', II: 'D9E8DD', III: 'F3E6BE', IV: 'F5E2D8', V: 'D9E8DD', VI: 'F3E6BE' };
const TXT = { I: TERRA, II: GREEN, III: ALBT, IV: TERRA, V: GREEN, VI: ALBT };
const ROMAN = { I: 1, II: 2, III: 3, IV: 4, V: 5, VI: 6 };
const ACC = { I: 'E0693A', II: '58B27A', III: 'E6B53C', IV: 'E0693A', V: '58B27A', VI: 'E6B53C' };    // acento sobre fondo oscuro
const PCOL = { I: TERRA, II: GREEN, III: ALBERO, IV: TERRA, V: GREEN, VI: ALBERO };                    // acento sobre fondo claro
let curPart = 'I';
function portadilla(title) {
  const m = /^Parte ([IVX]+)\. (.*)$/.exec(title); const num = m[1]; curPart = num;
  const bg = new ImageRun({ type: 'png', data: fs.readFileSync(path.join(dir, 'portadilla-fondo-' + ROMAN[num] + '.png')), transformation: { width: 794, height: 1123 },
    floating: { horizontalPosition: { relative: D.HorizontalPositionRelativeFrom.PAGE, offset: 0 }, verticalPosition: { relative: D.VerticalPositionRelativeFrom.PAGE, offset: 0 }, behindDocument: true, allowOverlap: true, lockAnchor: true } });
  return { part: 'PARTE ' + num + ' · ' + m[2].split(':')[0].toUpperCase(), portadilla: [
    new Paragraph({ pageBreakBefore: true, spacing: { before: 2200, after: 0 }, children: [bg, new TextRun({ text: 'PARTE ' + num, font: BOLD, size: 20, color: ACC[num], characterSpacing: 90 })] }),
    new Paragraph({ spacing: { before: 500, after: 300 }, children: [new TextRun({ text: num, font: HF, size: 260, color: ACC[num] })] }),
    new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 0, after: 360, line: 880 }, children: [new TextRun({ text: title, font: HF, size: 80, color: 'FFFFFF' })] }),
    tricolor(40),
    new Paragraph({ spacing: { before: 360, after: 0, line: 420 }, children: [new TextRun({ text: ESENCIA[num] || '', font: HF, size: 32, color: 'C9D2CD', italics: true })] }),
  ] };
}
function pilar(t) { if (/^15\. /.test(t)) return TERRA; if (/^16\. /.test(t)) return GREEN; if (/^17\. /.test(t)) return ALBT; const c = PCOL[curPart]; return c === ALBERO ? ALBT : c; }
function kicker(t) {
  let k = null, m;
  if ((m = /^(\d+)\. /.exec(t))) k = 'Capítulo ' + m[1]; else if ((m = /^Módulo (\d+)\./.exec(t))) k = 'Módulo ' + m[1]; else if ((m = /^Anexo ([A-Z])\./.exec(t))) k = 'Anexo ' + m[1];
  if (!k) return null;
  return [new Paragraph({ keepNext: true, pageBreakBefore: true, spacing: { before: 0, after: 200, line: 40, lineRule: 'exact' }, indent: { right: TEXT_W - 1100 }, border: { top: { style: BorderStyle.SINGLE, size: 36, color: PCOL[curPart], space: 0 } }, children: [new TextRun({ text: '', size: 2 })] }),
    new Paragraph({ keepNext: true, spacing: { before: 0, after: 60 }, children: [new TextRun({ text: k.toUpperCase(), font: BOLD, size: 16, color: pilar(t), characterSpacing: 70 })] })];
}
function cita(text) {
  const c = PCOL[curPart] === ALBERO ? ALBERO : PCOL[curPart];
  return [new Paragraph({ keepNext: true, spacing: { before: 280, after: 0, line: 520, lineRule: 'exact' }, children: [new TextRun({ text: '\u201C', font: HF, size: 150, color: c })] }),
    new Paragraph({ spacing: { before: 0, after: 380, line: 460 }, indent: { left: 0, right: 600 }, children: [new TextRun({ text, font: HF, size: 38, color: INK, italics: true })] })];
}
function firma() {
  return [new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { before: 300, after: 0 }, children: [new TextRun({ text: 'Alejandro Berruezo', font: HF, size: 30, italics: true, color: INK })] }),
    new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { before: 40, after: 0 }, children: [new TextRun({ text: 'Madrid, noviembre de 2026', font: SF, size: 17, color: GREY })] })];
}

function parse(md) {
  const out = []; const lines = md.split('\n'); let i = 0; let firstH1 = true;
  while (i < lines.length) {
    let l = lines[i];
    if (!l.trim()) { i++; continue; }
    if (l.startsWith('# ')) {
      heads.push([1, l.slice(2)]);
      if (/^Parte [IVX]+\. /.test(l.slice(2))) { out.push(portadilla(l.slice(2))); i++; continue; }
      out.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new TextRun({ text: l.slice(2) })] }));
      out.push(new Paragraph({ spacing: { before: 0, after: 240 }, border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: GREEN, space: 1 } }, children: [] }));
      i++; continue;
    }
    if (l.startsWith('## ')) { const t = l.slice(3); heads.push([2, t]); const k = kicker(t); if (k) out.push(...k); out.push(new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: k ? { before: 60, after: 160 } : undefined, children: [new TextRun({ text: t })] })); i++; continue; }
    if (l.startsWith('### ')) { out.push(new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun({ text: l.slice(4) })] })); i++; continue; }
    if (l.startsWith('>> ')) { out.push(...cita(l.slice(3))); i++; continue; }
    if (l.trim() === '{{firma}}') { out.push(...firma()); i++; continue; }
    if (/^\*Señal de fallo:\*/.test(l)) { out.push(spacer(60)); out.push(callout('', l.replace(/^\*Señal de fallo:\*\s*/, '').replace(/^./, c => c.toUpperCase()), TERRA, 'Señal de fallo')); out.push(spacer(160)); i++; continue; }
    if (l.startsWith('{{img:')) { const [f, w] = l.slice(6, -2).split('|'); out.push(image(f, +w)); i++; continue; }
    if (l.startsWith('!! ')) { const [t, ...b] = l.slice(3).split(' | '); out.push(spacer(60)); out.push(callout(t, b.join(' | '))); out.push(spacer(160)); i++; continue; }
    if (l.startsWith('|')) {
      const rows = []; while (i < lines.length && lines[i].startsWith('|')) { const cells = lines[i].trim().slice(1, -1).split('|').map(s => s.trim()); if (!cells.every(c => /^-+$/.test(c))) rows.push(cells); i++; }
      [].concat(table(rows)).forEach(x => out.push(x)); out.push(spacer(180)); continue;
    }
    if (/^- /.test(l)) { while (i < lines.length && /^- /.test(lines[i])) { out.push(new Paragraph({ numbering: { reference: 'vinetas', level: 0 }, spacing: { before: 0, after: 80, line: 300 }, children: runs(lines[i].slice(2)) })); i++; } out.push(spacer(80)); continue; }
    if (/^\d+\. /.test(l)) { const ref = 'num' + i; numRefs.push(ref); while (i < lines.length && /^\d+\. /.test(lines[i])) { out.push(new Paragraph({ numbering: { reference: ref, level: 0 }, spacing: { before: 0, after: 80, line: 300 }, children: runs(lines[i].replace(/^\d+\. /, '')) })); i++; } out.push(spacer(80)); continue; }
    out.push(new Paragraph({ spacing: { before: 0, after: 170, line: 320 }, children: runs(l) }));
    i++;
  }
  return out;
}
const numRefs = []; const heads = [];
const pages = fs.existsSync(path.join(dir, 'toc-pages.json')) ? JSON.parse(fs.readFileSync(path.join(dir, 'toc-pages.json'))) : {};
const files = fs.readdirSync(dir).filter(f => /^0\d[a-z]?-.*\.md$/.test(f)).sort();
const bodyAll = files.flatMap(f => parse(fs.readFileSync(path.join(dir, f), 'utf8')));

// Portada
const cover = [new Paragraph({ spacing: { before: 0, after: 0 }, children: [new ImageRun({ type: 'png', data: fs.readFileSync(path.join(dir, 'portada-doc.png')), transformation: { width: 793, height: 1122 } })] })];
const toc = [
  new Paragraph({ pageBreakBefore: true, spacing: { before: 0, after: 300 }, children: [new TextRun({ text: 'Índice', font: HF, size: 48, color: INK })] }),
  ...heads.map(([lv, t]) => new Paragraph({ spacing: { before: lv === 1 ? 200 : 40, after: lv === 1 ? 60 : 20 }, indent: { left: lv === 1 ? 0 : 360 },
    tabStops: [{ type: TabStopType.RIGHT, position: TEXT_W, leader: 'dot' }],
    children: [new TextRun({ text: t, font: lv === 1 ? HF : BF, size: lv === 1 ? 24 : 20, color: lv === 1 ? GREEN : INK }), new TextRun({ text: '\t' + (pages[t] || '0'), font: SF, size: 18, color: GREY })] })),
];

function sectionsOf() {
  const mainProps = { page: { margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } } };
  const hair = { style: BorderStyle.SINGLE, size: 4, color: LINE };
  const pnum = part => { const m = /^PARTE ([IVX]+)/.exec(part || ''); return m ? m[1] : 'I'; };
  const hdrOf = part => { const n = pnum(part), nm = (part || '').split(' · ')[1] || '';
    return { default: new Header({ children: [new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: PCOL[n], space: 8 } }, tabStops: [{ type: TabStopType.RIGHT, position: TEXT_W }],
      children: [new TextRun({ text: 'SYNERGÓS', font: BOLD, size: 15, color: INK, characterSpacing: 80 }), new TextRun({ text: '  EL MÉTODO', font: SF, size: 14, color: GREY, characterSpacing: 60 }),
        new TextRun({ text: '\t', font: SF, size: 14 }), new TextRun({ text: part ? 'PARTE ' + n + '  ' : '', font: BOLD, size: 14, color: TXT[n], characterSpacing: 60 }), new TextRun({ text: nm, font: SF, size: 14, color: GREY, characterSpacing: 60 })] })] }) }; };
  const ftrOf = part => { const n = pnum(part), dark = PCOL[n] === ALBERO, nb = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, top = { style: BorderStyle.SINGLE, size: 4, color: LINE };
    const mark = new ImageRun({ type: 'png', data: fs.readFileSync(path.join(dir, 'marca-agua.png')), transformation: { width: 420, height: 420 }, floating: { horizontalPosition: { relative: D.HorizontalPositionRelativeFrom.PAGE, align: D.HorizontalPositionAlign.RIGHT }, verticalPosition: { relative: D.VerticalPositionRelativeFrom.PAGE, align: D.VerticalPositionAlign.BOTTOM }, behindDocument: true, allowOverlap: true, lockAnchor: true } });
    return { default: new Footer({ children: [
      new Table({ width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: [TEXT_W - 760, 760], rows: [new TableRow({ children: [
        new TableCell({ width: { size: TEXT_W - 760, type: WidthType.DXA }, margins: { top: 100, bottom: 0, left: 0, right: 0 }, borders: { top, bottom: nb, left: nb, right: nb },
          children: [new Paragraph({ spacing: { before: 0, after: 0 }, children: [new TextRun({ text: 'Crecer a la vez.', font: HF, size: 26, color: GREEN, italics: true })] })] }),
        new TableCell({ width: { size: 760, type: WidthType.DXA }, shading: SHADE(PCOL[n]), margins: { top: 70, bottom: 70, left: 0, right: 0 }, borders: { top: nb, bottom: nb, left: nb, right: nb },
          children: [new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 0 }, children: [new TextRun({ children: [PageNumber.CURRENT], font: BOLD, size: 18, color: dark ? INK : 'FFFFFF' })] })] }),
      ] })] }),
      new Paragraph({ spacing: { before: 0, after: 0, line: 20, lineRule: 'exact' }, children: [mark] }),
    ] }) }; };
  const empty = { default: new Header({ children: [new Paragraph({ children: [] })] }) }, emptyF = { default: new Footer({ children: [new Paragraph({ children: [] })] }) };
  const secs = [{ properties: { page: { margin: { top: 0, bottom: 0, left: 0, right: 0, header: 0, footer: 0 } }, titlePage: true }, children: cover }];
  let cur = [...toc], first = true, part = '';
  const push = (children, withStart) => secs.push({ properties: withStart ? { ...mainProps, page: { ...mainProps.page, pageNumbers: { start: 2 } } } : mainProps, headers: hdrOf(part), footers: ftrOf(part), children });
  for (const el of bodyAll) {
    if (el && el.portadilla) {
      push(cur, first); first = false; cur = []; part = el.part;
      secs.push({ properties: mainProps, headers: empty, footers: emptyF, children: el.portadilla });
    } else cur.push(el);
  }
  push(cur, first);
  secs.push({ properties: { page: { margin: { top: 0, bottom: 0, left: 0, right: 0, header: 0, footer: 0 } } }, headers: empty, footers: emptyF, children: [new Paragraph({ spacing: { before: 0, after: 0 }, children: [new ImageRun({ type: 'png', data: fs.readFileSync(path.join(dir, 'contraportada.png')), transformation: { width: 793, height: 1122 } })] })] });
  return secs;
}
const doc = new Document({
  creator: 'Alejandro Berruezo', title: 'Synergós. El método. Versión 1.8', description: 'Método Synergós, documento de trabajo',
  features: { updateFields: true },
  styles: {
    default: { document: { run: { font: BF, size: 21, color: INK } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: HF, size: 76, color: INK }, paragraph: { spacing: { before: 0, after: 120 }, keepNext: true, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: HF, size: 64, color: INK }, paragraph: { spacing: { before: 360, after: 200 }, keepNext: true, outlineLevel: 1 } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: HF, size: 36, color: INK }, paragraph: { spacing: { before: 240, after: 100 }, keepNext: true, outlineLevel: 2 } },
    ]
  },
  numbering: { config: [
    { reference: 'vinetas', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 300 } }, run: { color: GREEN } } }] },
    ...numRefs.map(r => ({ reference: r, levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 360 } }, run: { color: GREEN, bold: true } } }] }))
  ] },
  fonts: [
    { name: 'Public Sans', data: fs.readFileSync(FONTDIR + 'public-sans-400-normal.ttf'), characterSet: D.CharacterSet.ANSI },
    { name: 'Public Sans SemiBold', data: fs.readFileSync(FONTDIR + 'public-sans-600-normal.ttf'), characterSet: D.CharacterSet.ANSI },
    { name: 'EB Garamond', data: fs.readFileSync(FONTDIR + 'eb-garamond-400-normal.ttf'), characterSet: D.CharacterSet.ANSI },
  ],
  sections: sectionsOf()
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync(path.join(dir, 'Synergos-El-metodo-v1.8.docx'), b); console.log('ok', files.length, 'ficheros'); });
