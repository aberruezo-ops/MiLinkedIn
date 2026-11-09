// Construye el documento del método Synergós en .docx a partir de los ficheros 0*.md
const fs = require('fs'); const path = require('path');
const D = require('docx');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, ImageRun, Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, BorderStyle, PageBreak, Footer, Header, PageNumber, TableOfContents, LevelFormat, TabStopType } = D;

const INK = '1F1D1A', GREEN = '2C6D3F', LIGHT = '7CC090', GREY = '56606A', PALE = 'E8F1EB', LINE = 'D7DCDC';
const HF = 'Fraunces', BF = 'Georgia', SF = 'Arial';
const PAGE_W = 11906, MARGIN = 1418, TEXT_W = PAGE_W - 2 * MARGIN; // A4, 2,5 cm
const dir = __dirname;
const imgSize = { 'fig-arquitectura.png': [1600, 960], 'fig-fases.png': [1800, 620], 'fig-girasol.png': [1200, 1000], 'logo.png': [2000, 520], 'portada-girasol.png': [1600, 1300], 'portada-doc.png': [1240, 1754] };
const cmToPx = cm => Math.round(cm / 2.54 * 96);

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
  const [w, h] = imgSize[file]; const pw = cmToPx(widthCm);
  return new Paragraph({ alignment: align, spacing: { before: 160, after: 200 }, children: [new ImageRun({ type: 'png', data: fs.readFileSync(path.join(dir, file)), transformation: { width: pw, height: Math.round(pw * h / w) } })] });
}
const cellBorder = { style: BorderStyle.SINGLE, size: 4, color: LINE };
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
        shading: ri === 0 ? { type: ShadingType.CLEAR, color: 'auto', fill: GREEN } : (ri % 2 === 0 ? { type: ShadingType.CLEAR, color: 'auto', fill: 'F4F6F6' } : undefined),
        margins: { top: 70, bottom: 70, left: 100, right: 100 },
        borders: { top: cellBorder, bottom: cellBorder, left: cellBorder, right: cellBorder },
        children: [new Paragraph({ spacing: { before: 0, after: 0, line: 252 }, children: runs(c, { font: SF, size: 17, color: ri === 0 ? 'FFFFFF' : INK, bold: ri === 0 ? true : undefined }) })]
      }))
    }))
  });
}
function callout(title, body) {
  const b = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
  return new Table({
    width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: [TEXT_W],
    rows: [new TableRow({ cantSplit: true, children: [new TableCell({
      width: { size: TEXT_W, type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, color: 'auto', fill: PALE },
      margins: { top: 160, bottom: 160, left: 240, right: 240 },
      borders: { top: b, bottom: b, right: b, left: { style: BorderStyle.SINGLE, size: 36, color: GREEN } },
      children: [
        new Paragraph({ spacing: { before: 0, after: 80 }, children: [new TextRun({ text: title, font: HF, size: 23, color: GREEN, bold: true })] }),
        new Paragraph({ spacing: { before: 0, after: 0, line: 288 }, children: runs(body, { font: BF, size: 20, color: INK }) })
      ]
    })] })]
  });
}
const spacer = (after = 120) => new Paragraph({ spacing: { before: 0, after }, children: [] });

function parse(md) {
  const out = []; const lines = md.split('\n'); let i = 0; let firstH1 = true;
  while (i < lines.length) {
    let l = lines[i];
    if (!l.trim()) { i++; continue; }
    if (l.startsWith('# ')) {
      heads.push([1, l.slice(2)]);
      out.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new TextRun({ text: l.slice(2) })] }));
      out.push(new Paragraph({ spacing: { before: 0, after: 240 }, border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: GREEN, space: 1 } }, children: [] }));
      i++; continue;
    }
    if (l.startsWith('## ')) { heads.push([2, l.slice(3)]); out.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: l.slice(3) })] })); i++; continue; }
    if (l.startsWith('### ')) { out.push(new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun({ text: l.slice(4) })] })); i++; continue; }
    if (l.startsWith('{{img:')) { const [f, w] = l.slice(6, -2).split('|'); out.push(image(f, +w)); i++; continue; }
    if (l.startsWith('!! ')) { const [t, ...b] = l.slice(3).split(' | '); out.push(spacer(60)); out.push(callout(t, b.join(' | '))); out.push(spacer(160)); i++; continue; }
    if (l.startsWith('|')) {
      const rows = []; while (i < lines.length && lines[i].startsWith('|')) { const cells = lines[i].trim().slice(1, -1).split('|').map(s => s.trim()); if (!cells.every(c => /^-+$/.test(c))) rows.push(cells); i++; }
      out.push(table(rows)); out.push(spacer(180)); continue;
    }
    if (/^- /.test(l)) { while (i < lines.length && /^- /.test(lines[i])) { out.push(new Paragraph({ numbering: { reference: 'vinetas', level: 0 }, spacing: { before: 0, after: 80, line: 300 }, children: runs(lines[i].slice(2)) })); i++; } out.push(spacer(80)); continue; }
    if (/^\d+\. /.test(l)) { const ref = 'num' + i; numRefs.push(ref); while (i < lines.length && /^\d+\. /.test(lines[i])) { out.push(new Paragraph({ numbering: { reference: ref, level: 0 }, spacing: { before: 0, after: 80, line: 300 }, children: runs(lines[i].replace(/^\d+\. /, '')) })); i++; } out.push(spacer(80)); continue; }
    out.push(new Paragraph({ spacing: { before: 0, after: 160, line: 312 }, alignment: AlignmentType.JUSTIFIED, children: runs(l) }));
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
  creator: 'Alejandro Berruezo', title: 'Synergós. El método. Versión 1.5', description: 'Método Synergós, documento de trabajo',
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
      footers: { default: new Footer({ children: [new Paragraph({ border: { top: { style: BorderStyle.SINGLE, size: 8, color: GREEN, space: 6 } }, tabStops: [{ type: TabStopType.RIGHT, position: TEXT_W }], children: [new TextRun({ text: 'Crecer a la vez · Versión 1.5 · Documento de trabajo', font: SF, size: 15, color: GREY }), new TextRun({ children: ['\t', PageNumber.CURRENT], font: SF, size: 16, color: GREEN })] })] }) },
      children: [...toc, ...body] }
  ]
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync(path.join(dir, 'Synergos-El-metodo-v1.5.docx'), b); console.log('ok', files.length, 'ficheros'); });
