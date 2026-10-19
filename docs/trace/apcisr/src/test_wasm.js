// Run the WebAssembly build on every input the native build ran, and compare every output byte for byte.
const fs = require('fs');
const stub = () => 0;
const inst = new WebAssembly.Instance(new WebAssembly.Module(fs.readFileSync('apcisr.wasm')),
  {wasi_snapshot_preview1: {fd_close: stub, fd_fdstat_get: stub, fd_seek: stub, fd_write: stub}});
const X = inst.exports, mem = () => new Uint8Array(X.memory.buffer), dv = () => new DataView(X.memory.buffer);
function run(bytes) {
  const p = X.in_ptr(); const m = mem(); m.set(bytes, p); m[p + bytes.length] = 0;
  const r = X.run(0), M = mem(), U = r, Mi = r + 1024, N = r + 2048;
  let s = '';
  for (let k = 0; k < 1024 && (M[U + k] || M[Mi + k] || M[N + k]); k++)
    s += [M[U + k], M[Mi + k], M[N + k]].map(v => v.toString(16).padStart(2, '0')).join('') + ' ';
  return s + '| ' + dv().getInt32(r + 3072, true);
}
const inputs = fs.readFileSync('inputs.bin').toString('latin1').split('\n'); inputs.pop();
const expected = fs.readFileSync('expected.txt').toString('latin1').split('\n'); expected.pop();
let same = 0;
inputs.forEach((s, i) => { if (run(Buffer.from(s, 'latin1')) === expected[i]) same++; });
console.log(`WebAssembly against native: ${same} of ${inputs.length} outputs identical; trace steps for the last input: ${X.tr_count()} (record ${X.tr_size()} bytes)`);
