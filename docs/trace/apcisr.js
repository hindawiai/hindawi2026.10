// apcisr.js: APCISR (the AP Code for Indian Script Representation, © 2003–2006 Abhishek Choudhary, GPL-2.0-or-later)
// running in the browser. acii2cisr() is the original C, compiled to WebAssembly with two trace hooks that only record
// state (apcisr/src). Its output on 896 inputs is byte for byte the native build's. © 1993–2026 Abhishek Choudhary. AyeAI.
"use strict";
(function () {
  const D = window.APCISR_DATA;
  const b64 = s => Uint8Array.from(atob(s), c => c.charCodeAt(0));
  const FONT16 = b64(D.font16), FONT8 = b64(D.font8);
  const stub = () => 0;
  let X = null;
  function engine() {
    if (!X) X = new WebAssembly.Instance(new WebAssembly.Module(b64(D.wasm)),
      {wasi_snapshot_preview1: {fd_close: stub, fd_fdstat_get: stub, fd_seek: stub, fd_write: stub}}).exports;
    return X;
  }
  // Unicode to ISCII, character by character, with the table Romenagri's own uni2acii gives for every Devanagari letter
  function toISCII(text) {
    const bytes = [], unknown = [];
    for (const ch of text.normalize("NFC")) {
      const m = D.uni2iscii[ch];
      if (m) for (const c of m) bytes.push(c.charCodeAt(0));
      else if (ch.codePointAt(0) < 128) bytes.push(ch.codePointAt(0));
      else unknown.push(ch);
    }
    return {bytes, unknown};
  }
  // the table entry acii2cisr() would match at this position: the first whose ISCII bytes begin there
  function entryAt(bytes, at) {
    for (let i = 0; i < D.table.length; i++) {
      const a = D.table[i].acii;
      if (a.length && a.every((v, k) => bytes[at + k] === v)) return {index: i, ...D.table[i]};
    }
    return null;
  }
  function run(text) {
    const x = engine(), {bytes, unknown} = toISCII(text), n = Math.min(bytes.length, 4000);
    let m = new Uint8Array(x.memory.buffer); const p = x.in_ptr();
    m.set(bytes.slice(0, n), p); m[p + n] = 0;
    const r = x.run(0); m = new Uint8Array(x.memory.buffer); const dv = new DataView(x.memory.buffer);
    const cells = [];
    for (let k = 0; k < 1024; k++) { const c = [m[r + k], m[r + 1024 + k], m[r + 2048 + k]]; if (!c[0] && !c[1] && !c[2]) break; cells.push(c); }
    const trace = [], tp = x.tr_ptr(), ts = x.tr_size(), W = 96;
    for (let j = 0; j < x.tr_count(); j++) {
      const b = tp + j * ts, I = k => dv.getInt32(b + 4 * k, true);
      trace.push({matrik: I(0), lipik: I(1), purak: I(2), purna: I(3), varna_purna: I(4), prev_hal: I(5), prev_ra_hal: I(6),
        offset: I(9), u: Array.from(m.slice(b + 40, b + 40 + W)), m: Array.from(m.slice(b + 40 + W, b + 40 + 2 * W)),
        n: Array.from(m.slice(b + 40 + 2 * W, b + 40 + 3 * W))});
    }
    const steps = trace.slice(1).map((after, j) => {
      const before = trace[j], token = bytes.slice(before.offset, after.offset);
      return {before, after, token, entry: entryAt(bytes, before.offset)};
    });
    return {bytes, unknown, cells, curpos: dv.getInt32(r + 3072, true), trace, steps};
  }
  // the working map drawn through the same font substitution the original applies at its end
  function wmGlyph(row, code) {
    const t = D.maps[["cisr_urdha", "cisr_madhya", "cisr_nimna"][row]];
    if (row === 2 && code >= 128) code -= 128;
    return code > 0 && code < t.length ? t[code] : 32;
  }
  function drawGlyph(ctx, code, x, y, s, fg, bg, h) {
    const F = (h || 16) === 16 ? FONT16 : FONT8, H = h || 16;
    if (bg) { ctx.fillStyle = bg; ctx.fillRect(x, y, 8 * s, H * s); }
    ctx.fillStyle = fg;
    for (let row = 0; row < H; row++) { const g = F[code * H + row];
      for (let bit = 0; bit < 8; bit++) if (g & (0x80 >> bit)) ctx.fillRect(x + bit * s, y + row * s, s, s); }
  }
  function bitmap(code) { return Array.from(FONT16.slice(code * 16, code * 16 + 16)); }
  // an 80 x 60 text-mode screen: each cell holds a character code and an attribute, as video memory at B800:0000 does
  const CGA = ["#000000", "#0000aa", "#00aa00", "#00aaaa", "#aa0000", "#aa00aa", "#aa5500", "#aaaaaa",
               "#555555", "#5555ff", "#55ff55", "#55ffff", "#ff5555", "#ff55ff", "#ffff55", "#ffffff"];
  function TextScreen(canvas, cols, rows) {
    this.c = canvas; this.cols = cols || 80; this.rows = rows || 60;
    canvas.width = this.cols * 8; canvas.height = this.rows * 16;
    this.mem = Array.from({length: this.rows * this.cols}, () => ({code: 32, attr: 0x0A}));
    this.ctx = canvas.getContext("2d");
  }
  TextScreen.prototype.put = function (r, c, code, attr) {
    if (r < 0 || r >= this.rows || c < 0 || c >= this.cols) return;
    this.mem[r * this.cols + c] = {code: code & 255, attr: attr === undefined ? 0x0A : attr};
  };
  TextScreen.prototype.write = function (r, c, s, attr) { for (let k = 0; k < s.length; k++) this.put(r, c + k, s.charCodeAt(k) & 255, attr); };
  TextScreen.prototype.writeCells = function (r, c, cells, attr) {   // one APCISR line takes three text rows
    cells.forEach((cell, k) => { for (let z = 0; z < 3; z++) this.put(r + z, c + k, cell[z], attr); });
  };
  TextScreen.prototype.clear = function (attr) { this.mem.forEach(m => { m.code = 32; m.attr = attr === undefined ? 0x0A : attr; }); };
  TextScreen.prototype.draw = function () {
    const ctx = this.ctx;
    for (let r = 0; r < this.rows; r++) for (let c = 0; c < this.cols; c++) {
      const m = this.mem[r * this.cols + c];
      drawGlyph(ctx, m.code, c * 8, r * 16, 1, CGA[m.attr & 15], CGA[(m.attr >> 4) & 7], 16);
    }
  };
  TextScreen.prototype.cellAt = function (ev) {
    const b = this.c.getBoundingClientRect(), col = Math.floor((ev.clientX - b.left) / b.width * this.cols),
      row = Math.floor((ev.clientY - b.top) / b.height * this.rows);
    const m = this.mem[row * this.cols + col] || {code: 32, attr: 0};
    return {row, col, code: m.code, attr: m.attr, address: 0xB8000 + 2 * (row * this.cols + col)};
  };
  window.APC = {run, toISCII, entryAt, wmGlyph, drawGlyph, bitmap, TextScreen, CGA, table: D.table, source: D.source,
    provenance: D.provenance};
})();
