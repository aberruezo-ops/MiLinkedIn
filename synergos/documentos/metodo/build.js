// Construye el documento del método Synergós en .docx a partir de los ficheros 0*.md
const fs = require('fs'); const path = require('path');
const D = require('docx');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, ImageRun, Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, BorderStyle, PageBreak, Footer, Header, PageNumber, TableOfContents, LevelFormat, TabStopType } = D;

const INK = '1F1D1A', GREEN = '2C6D3F', LIGHT = '7CC090', GREY = '56606A', PALE = 'E8F1EB', LINE = 'D7DCDC';
const TERRA = 'B5512A', ALBERO = 'C89A2A', ALBT = '8A6508', TERRAPALE = 'FBF1EC', SOFT = 'F4F6F6';
const HF = 'Fraunces', BF = 'Georgia', SF = 'Arial';
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
    if (t.startsWith('**')) out.push(new TextRun({ text: t.slice(2, -2), bold: true, ...base }));
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
function table(rows) {
  const n = rows[0].length;
  // anchura de columnas: proporcional a la longitud media del texto, con mínimo
  const lens = Array.from({ length: n }, (_, i) => Math.max(8, rows.reduce((a, r) => a + (r[i] || '').length, 0) / rows.length));
  const tot = lens.reduce((a, b) => a + b, 0);
  let cols = lens.map(l => Math.round(TEXT_W * l / tot));
  const MIN = n > 3 ? 1500 : 2000; let deficit = 0; cols = cols.map(c => { if (c < MIN) { deficit += MIN - c; return MIN; } return c; });
  const big = cols.reduce((a, c) => a + (c > MIN ? c : 0), 0); cols = cols.map(c => c > MIN ? Math.round(c - deficit * c / big) : c);
  cols[n - 1] += TEXT_W - cols.reduce((a, b) => a + b, 0);
  return new Table({
    width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: cols,
    rows: rows.map((r, ri) => new TableRow({
      tableHeader: ri === 0, cantSplit: true,
      children: r.map((c, ci) => new TableCell({
        width: { size: cols[ci], type: WidthType.DXA },
        shading: ri === 0 ? { type: ShadingType.CLEAR, color: 'auto', fill: INK } : (ri % 2 === 0 ? { type: ShadingType.CLEAR, color: 'auto', fill: SOFT } : undefined),
        margins: { top: 90, bottom: 90, left: 120, right: 120 },
        borders: { top: ri === 0 ? { style: BorderStyle.SINGLE, size: 24, color: GREEN } : cellBorder, bottom: cellBorder, left: noB, right: noB },
        children: [new Paragraph({ spacing: { before: 0, after: 0, line: 252 }, children: runs(c, { font: SF, size: 17, color: ri === 0 ? 'FFFFFF' : INK, bold: (ri === 0 || (ci === 0 && n > 1)) ? true : undefined }) })]
      }))
    }))
  });
}
function callout(title, body, color = GREEN, fill = PALE) {
  const b = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
  return new Table({
    width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: [TEXT_W],
    rows: [new TableRow({ cantSplit: true, children: [new TableCell({
      width: { size: TEXT_W, type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, color: 'auto', fill },
      margins: { top: 160, bottom: 160, left: 240, right: 240 },
      borders: { top: b, bottom: b, right: b, left: { style: BorderStyle.SINGLE, size: 36, color } },
      children: [
        new Paragraph({ spacing: { before: 0, after: 80 }, children: [new TextRun({ text: title, font: HF, size: 23, color, bold: true })] }),
        new Paragraph({ spacing: { before: 0, after: 0, line: 288 }, children: runs(body, { font: BF, size: 20, color: INK }) })
      ]
    })] })]
  });
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
function tricolor(h = 120) {
  const w = Math.floor(TEXT_W / 3); const nb = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
  return new Table({ width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: [w, w, TEXT_W - 2 * w],
    rows: [new TableRow({ height: { value: h, rule: 'exact' }, children: [TERRA, GREEN, ALBERO].map((c, i) => new TableCell({ width: { size: i < 2 ? w : TEXT_W - 2 * w, type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, color: 'auto', fill: c }, borders: { top: nb, bottom: nb, left: nb, right: nb }, children: [new Paragraph({ spacing: { before: 0, after: 0, line: 60 }, children: [] })] })) })] });
}
function portadilla(title) {
  const m = /^Parte ([IVX]+)\. (.*)$/.exec(title); const num = m[1], rest = m[2];
  return [
    new Paragraph({ pageBreakBefore: true, spacing: { before: 2600, after: 200 }, children: [new TextRun({ text: 'PARTE ' + num, font: SF, size: 22, color: GREEN, characterSpacing: 80 })] }),
    tricolor(),
    new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 400, after: 300 }, children: [new TextRun({ text: title, size: 2, color: 'FFFFFF' })] }),
    new Paragraph({ spacing: { before: 0, after: 400, line: 760 }, children: [new TextRun({ text: rest, font: HF, size: 68, color: INK })] }),
    new Paragraph({ spacing: { before: 0, after: 0, line: 420 }, children: [new TextRun({ text: ESENCIA[num] || '', font: HF, size: 30, color: GREY, italics: true })] }),
    new Paragraph({ children: [new PageBreak()] }),
  ];
}
function pilar(t) { if (/^15\. /.test(t)) return TERRA; if (/^16\. /.test(t)) return GREEN; if (/^17\. /.test(t)) return ALBT; return GREEN; }
function kicker(t) {
  let k = null; let m;
  if ((m = /^(\d+)\. /.exec(t))) k = 'Capítulo ' + m[1]; else if ((m = /^Módulo (\d+)\./.exec(t))) k = 'Módulo ' + m[1]; else if ((m = /^Anexo ([A-Z])\./.exec(t))) k = 'Anexo ' + m[1];
  if (!k) return null;
  return new Paragraph({ keepNext: true, spacing: { before: 420, after: 0 }, border: { top: { style: BorderStyle.SINGLE, size: 18, color: pilar(t), space: 6 } }, children: [new TextRun({ text: k.toUpperCase(), font: SF, size: 16, color: pilar(t), characterSpacing: 60 })] });
}
function cita(text) {
  return new Paragraph({ spacing: { before: 200, after: 320, line: 440 }, indent: { left: 400, right: 400 }, border: { left: { style: BorderStyle.SINGLE, size: 30, color: ALBERO, space: 14 } },
    children: [new TextRun({ text, font: HF, size: 32, color: GREEN })] });
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
      if (/^Parte [IVX]+\. /.test(l.slice(2))) { out.push(...portadilla(l.slice(2))); i++; continue; }
      out.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new TextRun({ text: l.slice(2) })] }));
      out.push(new Paragraph({ spacing: { before: 0, after: 240 }, border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: GREEN, space: 1 } }, children: [] }));
      i++; continue;
    }
    if (l.startsWith('## ')) { const t = l.slice(3); heads.push([2, t]); const k = kicker(t); if (k) out.push(k); out.push(new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: k ? { before: 60, after: 160 } : undefined, children: [new TextRun({ text: t, color: pilar(t) })] })); i++; continue; }
    if (l.startsWith('### ')) { out.push(new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun({ text: l.slice(4) })] })); i++; continue; }
    if (l.startsWith('>> ')) { out.push(cita(l.slice(3))); i++; continue; }
    if (l.trim() === '{{firma}}') { out.push(...firma()); i++; continue; }
    if (/^\*Señal de fallo:\*/.test(l)) { out.push(callout('Señal de fallo', l.replace(/^\*Señal de fallo:\*\s*/, '').replace(/^./, c => c.toUpperCase()), TERRA, TERRAPALE)); out.push(spacer(160)); i++; continue; }
    if (l.startsWith('{{img:')) { const [f, w] = l.slice(6, -2).split('|'); out.push(image(f, +w)); i++; continue; }
    if (l.startsWith('!! ')) { const [t, ...b] = l.slice(3).split(' | '); out.push(spacer(60)); out.push(callout(t, b.join(' | '))); out.push(spacer(160)); i++; continue; }
    if (l.startsWith('|')) {
      const rows = []; while (i < lines.length && lines[i].startsWith('|')) { const cells = lines[i].trim().slice(1, -1).split('|').map(s => s.trim()); if (!cells.every(c => /^-+$/.test(c))) rows.push(cells); i++; }
      out.push(table(rows)); out.push(spacer(180)); continue;
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
const body = files.flatMap(f => parse(fs.readFileSync(path.join(dir, f), 'utf8')));

// Portada
const cover = [new Paragraph({ spacing: { before: 0, after: 0 }, children: [new ImageRun({ type: 'png', data: fs.readFileSync(path.join(dir, 'portada-doc.png')), transformation: { width: 793, height: 1122 } })] })];
const toc = [
  new Paragraph({ pageBreakBefore: true, spacing: { before: 0, after: 300 }, children: [new TextRun({ text: 'Índice', font: HF, size: 48, color: INK })] }),
  ...heads.map(([lv, t]) => new Paragraph({ spacing: { before: lv === 1 ? 200 : 40, after: lv === 1 ? 60 : 20 }, indent: { left: lv === 1 ? 0 : 360 },
    tabStops: [{ type: TabStopType.RIGHT, position: TEXT_W, leader: 'dot' }],
    children: [new TextRun({ text: t, font: lv === 1 ? HF : BF, size: lv === 1 ? 24 : 20, color: lv === 1 ? GREEN : INK }), new TextRun({ text: '\t' + (pages[t] || '0'), font: SF, size: 18, color: GREY })] })),
];

const doc = new Document({
  creator: 'Alejandro Berruezo', title: 'Synergós. El método. Versión 1.8', description: 'Método Synergós, documento de trabajo',
  features: { updateFields: true },
  styles: {
    default: { document: { run: { font: BF, size: 21, color: INK } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: HF, size: 46, color: INK }, paragraph: { spacing: { before: 0, after: 120 }, keepNext: true, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: HF, size: 32, color: GREEN }, paragraph: { spacing: { before: 360, after: 140 }, keepNext: true, outlineLevel: 1 } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: HF, size: 25, color: INK, bold: true }, paragraph: { spacing: { before: 240, after: 100 }, keepNext: true, outlineLevel: 2 } },
    ]
  },
  numbering: { config: [
    { reference: 'vinetas', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 300 } }, run: { color: GREEN } } }] },
    ...numRefs.map(r => ({ reference: r, levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 360 } }, run: { color: GREEN, bold: true } } }] }))
  ] },
  sections: [
    { properties: { page: { margin: { top: 0, bottom: 0, left: 0, right: 0, header: 0, footer: 0 } }, titlePage: true }, children: cover },
    { properties: { page: { margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN }, pageNumbers: { start: 2 } } },
      headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ text: 'Synergós · El método', font: SF, size: 15, color: GREY })] })] }) },
      footers: { default: new Footer({ children: [new Paragraph({ border: { top: { style: BorderStyle.SINGLE, size: 8, color: GREEN, space: 6 } }, tabStops: [{ type: TabStopType.RIGHT, position: TEXT_W }], children: [new TextRun({ text: 'Crecer a la vez · Versión 1.8 · Documento de trabajo', font: SF, size: 15, color: GREY }), new TextRun({ children: ['\t', PageNumber.CURRENT], font: SF, size: 16, color: GREEN })] })] }) },
      children: [...toc, ...body] }
  ]
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync(path.join(dir, 'Synergos-El-metodo-v1.8.docx'), b); console.log('ok', files.length, 'ficheros'); });
