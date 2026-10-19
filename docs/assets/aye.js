// aye.js: on every page, (1) select text and ask an AI about it, and (2) doubt any section: copy its hash, check it
// yourself, report it as a GitHub issue, or take on a work package. A few badges and hidden finds reward the curious.
// © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
(function () {
  "use strict";
  const REPO = "https://github.com/hindawiai/hindawi2026.10";
  const WP = "https://hindawiai.github.io/hindawi2026.10/hindawi/work-packages.html";
  const AIS = [["Claude", "https://claude.ai/new?q="], ["ChatGPT", "https://chatgpt.com/?q="], ["Perplexity", "https://www.perplexity.ai/search?q="],
               ["Copilot", "https://copilot.microsoft.com/?q="], ["Grok", "https://grok.com/?q="], ["Gemini", "https://gemini.google.com/app#"]];
  const css = `.aye-menu{position:fixed;z-index:9999;background:#fff;color:#1d1b17;border:1px solid #ccc;border-radius:10px;box-shadow:0 6px 24px rgba(0,0,0,.18);font:15px system-ui,sans-serif;padding:6px;min-width:190px}
.aye-menu b{display:block;padding:4px 8px;font-size:13px;color:#6b6457}.aye-menu a,.aye-menu button{display:block;width:100%;text-align:left;padding:7px 10px;border:0;background:none;color:#1e4f8a;font:inherit;cursor:pointer;text-decoration:none;border-radius:6px}
.aye-menu a:hover,.aye-menu button:hover{background:#f3ede1}.aye-ask{position:fixed;right:12px;bottom:calc(14px + env(safe-area-inset-bottom,0px));z-index:9998;display:none;padding:10px 14px;border-radius:22px;border:0;background:#b4530a;color:#fff;font:600 15px system-ui,sans-serif;box-shadow:0 4px 14px rgba(0,0,0,.25)}
.aye-doubt{font:600 12px system-ui,sans-serif;margin-left:10px;padding:3px 9px;border-radius:12px;border:1px solid #b4530a;background:none;color:#b4530a;cursor:pointer;vertical-align:middle}
.aye-panel{border:1px dashed #b4530a;border-radius:10px;padding:10px 12px;margin:8px 0;font:14px/1.5 system-ui,sans-serif}.aye-panel code{word-break:break-all;font-size:12px}
.aye-badge{position:fixed;left:12px;bottom:calc(14px + env(safe-area-inset-bottom,0px));z-index:9998;padding:6px 11px;border-radius:16px;border:1px solid #ccc;background:#fff;color:#1d1b17;font:13px system-ui,sans-serif;cursor:pointer}
@media (prefers-color-scheme: dark){.aye-menu,.aye-badge{background:#1f1c17;color:#eee8dc;border-color:#3a342a}.aye-menu a,.aye-menu button{color:#7fb0ef}.aye-menu a:hover,.aye-menu button:hover{background:#2a261f}}`;
  const st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);

  // ---- badges, kept in this browser only
  const B = JSON.parse(localStorage.getItem("aye-badges") || "{}");
  const NAMES = {curious: "Curious: asked an AI", sceptic: "Sceptic: doubted a section", critic: "Critic: opened an issue",
                 builder: "Builder: looked at a work package", qwantum: "Qwan-tum: found the horse", archivist: "Archivist: knocked five times"};
  const badge = document.createElement("button"); badge.className = "aye-badge"; document.body.appendChild(badge);
  function award(k) { if (!B[k]) { B[k] = Date.now(); try { localStorage.setItem("aye-badges", JSON.stringify(B)); } catch (e) {} flash(NAMES[k]); } show(); }
  function show() { const n = Object.keys(B).length; badge.textContent = `🏅 ${n} of ${Object.keys(NAMES).length}`; badge.style.display = n ? "block" : "none"; }
  function flash(t) { const d = document.createElement("div"); d.className = "aye-menu"; d.style.cssText += "left:12px;bottom:60px;"; d.textContent = "🏅 " + t; document.body.appendChild(d); setTimeout(() => d.remove(), 2600); }
  badge.onclick = () => menu(Object.entries(NAMES).map(([k, t]) => `<b>${B[k] ? "🏅" : "·"} ${t}</b>`).join("") + "<b>Hidden finds remain.</b>", badge.getBoundingClientRect());
  show();

  // ---- ask an AI about the selected text
  let box = null;
  function close() { if (box) { box.remove(); box = null; } }
  function menu(html, r) { close(); box = document.createElement("div"); box.className = "aye-menu"; box.innerHTML = html; document.body.appendChild(box);
    const w = box.offsetWidth, h = box.offsetHeight; box.style.left = Math.max(6, Math.min(innerWidth - w - 6, r.left)) + "px";
    box.style.top = Math.max(6, Math.min(innerHeight - h - 6, r.bottom + 4)) + "px"; return box; }
  function prompt(sel) { return `From the page "${document.title}" (${location.href}):\n\n"${sel}"\n\nExplain this simply, then say how I could check it myself.`; }
  function askMenu(sel, r) {
    const p = prompt(sel), m = menu("<b>Ask an AI about the selection</b>" + AIS.map(([n, u]) => `<a target="_blank" rel="noopener" href="${u}${encodeURIComponent(p)}" data-ai>${n}</a>`).join("") +
      `<button data-copy>Copy the question</button><b style="font-size:12px">The question is also copied, to paste if a site does not fill it in.</b>`, r);
    m.querySelectorAll("[data-ai]").forEach(a => a.addEventListener("click", () => { navigator.clipboard && navigator.clipboard.writeText(p).catch(() => {}); award("curious"); setTimeout(close, 50); }));
    m.querySelector("[data-copy]").onclick = () => { navigator.clipboard && navigator.clipboard.writeText(p); close(); };
  }
  document.addEventListener("contextmenu", e => { const s = String(getSelection()).trim(); if (!s) return; e.preventDefault();
    askMenu(s.slice(0, 1500), {left: e.clientX, bottom: e.clientY}); });
  const ask = document.createElement("button"); ask.className = "aye-ask"; ask.textContent = "Ask AI"; document.body.appendChild(ask);
  document.addEventListener("selectionchange", () => { ask.style.display = String(getSelection()).trim() ? "block" : "none"; });
  ask.onclick = () => askMenu(String(getSelection()).trim().slice(0, 1500), ask.getBoundingClientRect());
  document.addEventListener("click", e => { if (box && !box.contains(e.target) && e.target !== ask && e.target !== badge) close(); });

  // ---- doubt a section: its hash, a way to check, an issue, a work package
  async function hash(t) { const d = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(t));
    return Array.from(new Uint8Array(d)).map(b => b.toString(16).padStart(2, "0")).join(""); }
  document.querySelectorAll("section").forEach(sec => {
    const h = sec.querySelector("h2"); if (!h) return;
    const btn = document.createElement("button"); btn.className = "aye-doubt"; btn.textContent = "Doubt this?"; btn.type = "button"; h.appendChild(btn);
    btn.onclick = async () => {
      const old = sec.querySelector(".aye-panel"); if (old) { old.remove(); return; }
      const title = h.firstChild.textContent.trim(), text = (sec.innerText || sec.textContent).replace(/Doubt this\?/g, "").replace(/\s+/g, " ").trim();
      const hx = await hash(text), check = sec.dataset.check || "Every number here comes from tools in the repository: run them, or use this page's own controls, and compare. A difference is a finding.";
      const body = encodeURIComponent(`Page: ${location.href}\nSection: ${title}\nSection hash (SHA-256): ${hx}\n\nWhat I checked:\n\nWhat I found:\n\nHow to reproduce it:\n`);
      const p = document.createElement("div"); p.className = "aye-panel";
      p.innerHTML = `<b>Doubt this section? Good: check it.</b><br>Its fingerprint (SHA-256 of the text you see): <code>${hx}</code>
        <button type="button" class="aye-doubt" data-c>Copy</button><br><b>Check it yourself:</b> ${check}<br>
        <a target="_blank" rel="noopener" href="${REPO}/issues/new?title=${encodeURIComponent("Doubt: " + title)}&body=${body}" data-i>Report what you found as a GitHub issue</a>
        · <a target="_blank" rel="noopener" href="${WP}" data-w>Take on a work package and make it better</a><br>
        <span class="mut" style="font-size:12px">No time? Copy the fingerprint into a message: it names exactly the text you are disputing, even after the page changes.</span>`;
      h.after(p); award("sceptic");
      p.querySelector("[data-c]").onclick = () => navigator.clipboard && navigator.clipboard.writeText(hx);
      p.querySelector("[data-i]").onclick = () => award("critic"); p.querySelector("[data-w]").onclick = () => award("builder");
    };
  });

  // ---- hidden finds
  let typed = ""; document.addEventListener("keydown", e => { typed = (typed + (e.key || "")).slice(-6).toLowerCase();
    if (typed === "tumtum") { award("qwantum"); const hz = document.createElement("div"); hz.textContent = "🐎";
      hz.style.cssText = "position:fixed;top:40%;left:-60px;font-size:56px;z-index:9999;transition:left 3s linear"; document.body.appendChild(hz);
      requestAnimationFrame(() => { hz.style.left = innerWidth + 60 + "px"; }); setTimeout(() => hz.remove(), 3200); } });
  let knocks = 0; const foot = document.querySelector("footer"); if (foot) foot.addEventListener("click", () => { if (++knocks === 5) award("archivist"); });
})();
