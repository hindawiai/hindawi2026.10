# S02: BUILD-0102 as received. The tree at tag build-0102 holds every file of the archive byte for byte, less the six
# generated compiler outputs CHANGE-LOG.md's C0 lists; C0 changed .gitignore and began CHANGE-LOG.md; anything else in that
# tree belongs to the seed (its notes, metadata, gate, originals, handover and seal).
import hashlib, subprocess, sys, zipfile
ARCHIVE = "releases/originals/BUILD-0102__pushkalavati-hindawi-ilm-2026-10-16.zip"
TAG = sys.argv[1] if len(sys.argv) > 1 else "build-0102"
LEFT_OUT = {"tools/pushkalavati-compiler/out/" + n for n in ("functional-classification.json", "generated-rules.json",
            "meta-compiler-catalog.json", "meta-expansion.json", "progress.json", "rules-ir.json")}
SEED = ("SEED-NOTE.md", "misty.json", "CITATION.cff", "MANIFEST.sha256", "MANIFEST.sha256.ots",
        "ops/", "releases/", "attest/", "docs/handover/")
def blob(data): return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()
out = subprocess.run(["git", "ls-tree", "-r", "-z", TAG], capture_output=True, check=True).stdout
tree = {}
for rec in out.split(b"\0"):
    if rec:
        meta, path = rec.split(b"\t", 1)
        tree[path.decode("utf-8", "surrogateescape")] = meta.split()[2].decode()
z = zipfile.ZipFile(ARCHIVE)
files = {}
for info in z.infolist():
    if info.is_dir():
        continue
    name = info.filename if info.flag_bits & 0x800 else info.filename.encode("cp437").decode("utf-8", "surrogateescape")
    files[name.split("/", 1)[1]] = info
bad = []
for path, info in files.items():
    if path in LEFT_OUT:
        if path in tree: bad.append(f"left out by C0 but present: {path}")
        continue
    if path not in tree: bad.append(f"missing: {path}")
    elif path != ".gitignore" and tree[path] != blob(z.read(info)): bad.append(f"differs: {path}")
for path in tree:
    if path not in files and path not in (".gitignore", "CHANGE-LOG.md") and not path.startswith(SEED):
        bad.append(f"not in the archive: {path}")
for b in bad[:15]: print(b)
if bad: print(f"{len(bad)} difference(s)"); sys.exit(1)
print(f"{len(files) - len(LEFT_OUT)} files of BUILD-0102 at tag {TAG}, byte for byte")
