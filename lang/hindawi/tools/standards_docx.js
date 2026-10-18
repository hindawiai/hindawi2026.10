#!/usr/bin/env node
// © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
// standards_docx.js: each standards/<lang>/standard.json as standard.docx, in the layout standards bodies take drafts
// in: a title page, numbered clauses as Word headings, normative annexes, tables with a shaded header row, the
// document identifier in the header and the page number in the footer. Needs the npm package docx.
//   node lang/hindawi/tools/standards_docx.js [standards-directory] [lang ...]
const fs = require("fs"), path = require("path");
const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, WidthType, ShadingType,
        AlignmentType, Header, Footer, PageNumber, LevelFormat, BorderStyle, PageBreak } = require("docx");

const root = process.argv[2] || path.join(__dirname, "../../../standards");
const only = process.argv.slice(3);
const FONT = { DEVANAGARI: "Noto Sans Devanagari", ARABIC: "Noto Naskh Arabic", BENGALI: "Noto Sans Bengali",
  GURMUKHI: "Noto Sans Gurmukhi", GUJARATI: "Noto Sans Gujarati", ORIYA: "Noto Sans Oriya", TAMIL: "Noto Sans Tamil",
  TELUGU: "Noto Sans Telugu", KANNADA: "Noto Sans Kannada", MALAYALAM: "Noto Sans Malayalam", SINHALA: "Noto Sans Sinhala",
  THAI: "Noto Sans Thai", LAO: "Noto Sans Lao", KHMER: "Noto Sans Khmer", MYANMAR: "Noto Sans Myanmar", TIBETAN: "Noto Serif Tibetan",
  HEBREW: "Noto Sans Hebrew", SYRIAC: "Noto Sans Syriac", CYRILLIC: "Calibri", CJK: "Noto Sans CJK SC", HANGUL: "Noto Sans CJK KR" };
const RTL = /[\u0590-\u08FF\uFB1D-\uFDFF\uFE70-\uFEFF]/;

function run(text, script, opts = {}) {
  const cs = FONT[script.toUpperCase()] || "Noto Sans";
  return new TextRun({ text, font: { ascii: "Calibri", hAnsi: "Calibri", cs, eastAsia: FONT.CJK },
                       rightToLeft: RTL.test(text), size: opts.size || 21, bold: !!opts.bold });
}

function table(b, script) {
  const total = 9026, n = b.head.length;                      // A4 text width with 2.5 cm margins, in DXA
  const widths = n === 3 ? [2600, 3826, 2600] : Array(n).fill(Math.floor(total / n));
  const border = { style: BorderStyle.SINGLE, size: 4, color: "999999" };
  const borders = { top: border, bottom: border, left: border, right: border };
  const cell = (text, i, head) => new TableCell({
    width: { size: widths[i], type: WidthType.DXA }, borders,
    shading: head ? { type: ShadingType.CLEAR, fill: "E7E6E6", color: "auto" } : undefined,
    margins: { top: 40, bottom: 40, left: 80, right: 80 },
    children: [new Paragraph({ children: [run(String(text), script, { bold: head, size: 19 })] })] });
  return new Table({ width: { size: widths.reduce((a, c) => a + c, 0), type: WidthType.DXA }, columnWidths: widths,
    rows: [new TableRow({ tableHeader: true, children: b.head.map((t, i) => cell(t, i, true)) }),
           ...b.rows.map(r => new TableRow({ children: r.map((t, i) => cell(t, i, false)) }))] });
}

function build(m) {
  const s = m.meta.script, kids = [];
  kids.push(new Paragraph({ spacing: { before: 2400, after: 240 }, children: [run(m.meta.identifier, s, { size: 28, bold: true })] }));
  kids.push(new Paragraph({ spacing: { after: 480 }, children: [run(m.meta.title, s, { size: 36, bold: true })] }));
  for (const line of [`Edition ${m.meta.edition}`, `Stage: ${m.meta.stage}`, `Date: ${m.meta.date}`,
                      `Language: ${m.meta.language} (${m.meta.code}), ${m.meta.script} script, ${m.meta.direction}`,
                      m.meta.publisher, m.meta.copyright])
    kids.push(new Paragraph({ spacing: { after: 120 }, children: [run(line, s)] }));
  kids.push(new Paragraph({ children: [new PageBreak()] }));
  for (const b of m.blocks) {
    if (b.type === "h1") kids.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: [run(b.text, s, { size: 28, bold: true })] }));
    else if (b.type === "h2") kids.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [run(b.text, s, { size: 24, bold: true })] }));
    else if (b.type === "p") kids.push(new Paragraph({ spacing: { after: 120 }, alignment: AlignmentType.JUSTIFIED, children: [run(b.text, s)] }));
    else if (b.type === "list") for (const i of b.items)
      kids.push(new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { after: 60 }, children: [run(i, s)] }));
    else if (b.type === "table") { kids.push(table(b, s)); kids.push(new Paragraph({ children: [] })); }
  }
  return new Document({
    creator: m.meta.publisher, title: `${m.meta.identifier} ${m.meta.title}`,
    styles: { default: { document: { run: { font: "Calibri", size: 21 } } } },
    numbering: { config: [{ reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "\u2022",
      alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] }] },
    sections: [{
      properties: { page: { margin: { top: 1418, bottom: 1418, left: 1418, right: 1418 } } },
      headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [run(m.meta.identifier, s, { size: 18 })] })] }) },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
        new TextRun({ text: `${m.meta.copyright}   `, size: 16 }), new TextRun({ children: [PageNumber.CURRENT], size: 16 })] })] }) },
      children: kids }] });
}

(async () => {
  let n = 0;
  for (const lang of fs.readdirSync(root).sort()) {
    const j = path.join(root, lang, "standard.json");
    if (!fs.existsSync(j) || (only.length && !only.includes(lang))) continue;
    const m = JSON.parse(fs.readFileSync(j, "utf8"));
    fs.writeFileSync(path.join(root, lang, "standard.docx"), await Packer.toBuffer(build(m)));
    n++;
  }
  console.log(`standards_docx: ${n} standards written as .docx`);
})();
