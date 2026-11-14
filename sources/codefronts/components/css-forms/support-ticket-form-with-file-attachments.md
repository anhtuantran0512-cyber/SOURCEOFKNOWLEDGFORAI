---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/support-ticket-form-with-file-attachments/"
title: "Support Ticket Form with File Attachments"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "A help-desk ticket form in a focused dark developer-tool style: priority as a colour-coded segmented control, category and subject fields, a description with…"
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Support Ticket Form with File Attachments
Source: https://codefronts.com/components/css-forms/support-ticket-form-with-file-attachments/

A help-desk ticket form in a focused dark developer-tool style: priority as a colour-coded segmented control, category and subject fields, a description with markdown hints, and a drag-and-drop attachment zone that is a real <input type="file" multiple> underneath — keyboard-operable, screen-reader-labelled, with per-file progress, image thumbnails, type and size validation, and remove buttons.
## HTML
```html
<div class="frm-06">
  <button type="button" class="frm-06__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-06__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-06__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-06__stage">
    <div class="frm-06__card" role="form" aria-labelledby="frm-06-title">
      <header class="frm-06__head">
        <div><p class="frm-06__crumb">Support / New ticket</p><h2 id="frm-06-title">Open a support ticket</h2></div>
        <span class="frm-06__sla"><i aria-hidden="true"></i>Median first reply: 38 min</span>
      </header>
      <fieldset class="frm-06__prio">
        <legend>Priority</legend>
        <div class="frm-06__seg">
          <label style="--dot:#64748b"><input type="radio" name="frm-06-p" value="low"><span>Low</span></label>
          <label style="--dot:#38bdf8"><input type="radio" name="frm-06-p" value="normal" checked><span>Normal</span></label>
          <label style="--dot:#f59e0b"><input type="radio" name="frm-06-p" value="high"><span>High</span></label>
          <label style="--dot:#f43f5e"><input type="radio" name="frm-06-p" value="urgent"><span>Urgent</span></label>
        </div>
        <p class="frm-06__hint frm-06__urgent">Urgent = production is down or data is at risk. We'll page the on-call engineer.</p>
      </fieldset>
      <div class="frm-06__grid">
        <div class="frm-06__field"><label for="frm-06-cat">Category</label>
          <select id="frm-06-cat"><option>Billing</option><option selected>Bug report</option><option>Integration / API</option><option>Account access</option><option>Feature request</option></select></div>
        <div class="frm-06__field"><label for="frm-06-env">Environment</label>
          <select id="frm-06-env"><option>Production</option><option>Staging</option><option>Local</option></select></div>
      </div>
      <div class="frm-06__field"><label for="frm-06-subj">Subject</label><input id="frm-06-subj" type="text" required placeholder="Webhook retries failing with 502 after deploy"></div>
      <div class="frm-06__field"><label for="frm-06-desc">Description</label>
        <textarea id="frm-06-desc" required placeholder="Steps to reproduce, expected vs actual result, request IDs…" aria-describedby="frm-06-md"></textarea>
        <p class="frm-06__hint" id="frm-06-md">Markdown supported: <code>**bold**</code> <code>&#96;code&#96;</code> <code>- list</code></p></div>
      <div class="frm-06__field">
        <span class="frm-06__label" id="frm-06-att-label">Attachments</span>
        <label class="frm-06__drop">
          <input type="file" multiple accept="image/*,.pdf,.txt,.log,.json,.har,.zip" aria-labelledby="frm-06-att-label" aria-describedby="frm-06-att-hint">
          <span class="frm-06__dropicon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 15v3a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-3"/></svg></span>
          <span class="frm-06__droptext"><b>Drop files here</b> or <u>browse</u></span>
          <span class="frm-06__hint" id="frm-06-att-hint">Screenshots, logs, HAR or PDF · up to 5 files · 10 MB each</span>
        </label>
        <ul class="frm-06__files" aria-label="Attached files"></ul>
        <p class="frm-06__sr" aria-live="polite" id="frm-06-live"></p>
      </div>
      <footer class="frm-06__foot">
        <label class="frm-06__cc"><input type="checkbox"><span>CC my team (ops@)</span></label>
        <button class="frm-06__submit" type="button"><span>Submit ticket</span><kbd>⌘ ↵</kbd></button>
      </footer>
      <p class="frm-06__status" role="status"></p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap');

.frm-06 {
  --bg: #0a0c10;
  --surface: #11141a;
  --raised: #171b23;
  --ink: #e6e9ef;
  --muted: #8b93a3;
  --line: #252a35;
  --accent: #38bdf8;
  --ok: #4ade80;
  --bad: #fb7185;
  --sans: "IBM Plex Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "IBM Plex Mono",ui-monospace,Menlo,monospace;
  --ease: cubic-bezier(.16,1,.3,1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(70rem 36rem at 50% -15%, color-mix(in oklab,var(--accent) 14%,transparent), transparent 70%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.frm-06[data-theme="light"] {
  --bg: #f3f5f8;
  --surface: #ffffff;
  --raised: #f6f8fb;
  --ink: #0f1720;
  --muted: #5b6474;
  --line: #e1e5ec;
  --accent: #0284c7;
  --ok: #15803d;
  --bad: #e11d48;
}

.frm-06,
.frm-06 *,
.frm-06 *::before,
.frm-06 *::after {
  box-sizing: border-box;
}

.frm-06__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,5vw,4rem);
}

.frm-06__card {
  width: 100%;
  max-width: 42rem;
  display: grid;
  gap: 1.25rem;
  padding: clamp(1.25rem,5vw,2.25rem);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  box-shadow: 0 0 0 1px rgba(255,255,255,.02) inset, 0 40px 80px -40px rgba(0,0,0,.8);
}

.frm-06__head {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  justify-content: space-between;
  gap: .8rem;
  padding-bottom: 1.1rem;
  border-bottom: 1px solid var(--line);
}

.frm-06__crumb {
  margin: 0 0 .3rem;
  font: 400 .78rem var(--mono);
  color: var(--muted);
}

.frm-06 h2 {
  margin: 0;
  font-size: 1.45rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.frm-06__sla {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  font: 400 .78rem var(--mono);
  color: var(--muted);
  padding: .35rem .65rem;
  border: 1px solid var(--line);
  border-radius: 999px;
}

.frm-06__sla i {
  width: .5rem;
  height: .5rem;
  border-radius: 50%;
  background: var(--ok);
  box-shadow: 0 0 0 0 var(--ok);
  animation: frm-06-live 2s infinite;
}

@keyframes frm-06-live {
  70% {
    box-shadow: 0 0 0 6px transparent;
  }
}

.frm-06 label,
.frm-06 legend,
.frm-06__label {
  font-size: .82rem;
  font-weight: 500;
  color: var(--ink);
}

.frm-06__prio {
  border: 0;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .55rem;
}

.frm-06__prio legend {
  padding: 0;
  margin-bottom: .55rem;
}

.frm-06__seg {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: .25rem;
  padding: .25rem;
  background: var(--raised);
  border: 1px solid var(--line);
  border-radius: .8rem;
}

.frm-06__seg label {
  position: relative;
}

.frm-06__seg input {
  position: absolute;
  inset: 0;
  opacity: 0;
  margin: 0;
  cursor: pointer;
}

.frm-06__seg span {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: .45rem;
  min-height: 2.6rem;
  border-radius: .6rem;
  font-size: .88rem;
  color: var(--muted);
  transition: background .2s, color .2s;
}

.frm-06__seg span::before {
  content: '';
  width: .5rem;
  height: .5rem;
  border-radius: 50%;
  background: var(--dot);
  opacity: .6;
}

.frm-06__seg label:hover span {
  color: var(--ink);
}

.frm-06__seg input:checked + span {
  color: var(--ink);
  background: color-mix(in oklab,var(--dot) 18%,var(--surface));
  box-shadow: inset 0 0 0 1px color-mix(in oklab,var(--dot) 55%,transparent);
}

.frm-06__seg input:checked + span::before {
  opacity: 1;
  box-shadow: 0 0 10px var(--dot);
}

.frm-06__seg input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.frm-06__urgent {
  display: none;
  color: #fda4af !important;
}

.frm-06[data-theme="light"] .frm-06__urgent {
  color: var(--bad) !important;
}

.frm-06__prio:has([value="urgent"]:checked) .frm-06__urgent {
  display: block;
  animation: frm-06-in .3s var(--ease);
}

@keyframes frm-06-in {
  from {
    opacity: 0;
    translate: 0 -4px;
  }
}

.frm-06__grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,12rem),1fr));
}

.frm-06__field {
  display: grid;
  gap: .45rem;
}

.frm-06 input[type="text"],
.frm-06 select,
.frm-06 textarea {
  width: 100%;
  min-height: 2.9rem;
  padding: .65rem .85rem;
  border-radius: .65rem;
  border: 1px solid var(--line);
  background: var(--raised);
  color: var(--ink);
  font: inherit;
  font-size: .95rem;
  transition: border-color .2s, box-shadow .2s;
}

.frm-06 select {
  appearance: none;
  padding-right: 2.4rem;
  cursor: pointer;
  background: var(--raised) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%238b93a3' stroke-width='2' stroke-linecap='round'%3E%3Cpath d='m7 10 5 5 5-5'/%3E%3C/svg%3E") no-repeat right .7rem center / 1.1rem;
}

.frm-06 textarea {
  min-height: 8rem;
  resize: vertical;
  field-sizing: content;
  max-height: 18rem;
  line-height: 1.55;
}

.frm-06 ::placeholder {
  color: color-mix(in oklab,var(--muted) 70%,transparent);
}

.frm-06 :is(input,select,textarea):focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--accent) 25%,transparent);
}

.frm-06 :user-invalid {
  border-color: var(--bad);
}

.frm-06__hint {
  margin: 0;
  font-size: .78rem;
  color: var(--muted);
}

.frm-06__hint code {
  font: 400 .74rem var(--mono);
  padding: .1rem .35rem;
  border-radius: .3rem;
  background: var(--raised);
  border: 1px solid var(--line);
}

.frm-06__drop {
  position: relative;
  display: grid;
  justify-items: center;
  gap: .4rem;
  padding: 1.6rem 1rem;
  text-align: center;
  cursor: pointer;
  border-radius: .9rem;
  border: 1.5px dashed color-mix(in oklab,var(--muted) 45%,transparent);
  background: var(--raised);
  transition: border-color .2s, background .25s;
}

.frm-06__drop input {
  position: absolute;
  inset: 0;
  opacity: 0;
  cursor: pointer;
  width: 100%;
}

.frm-06__drop:hover {
  border-color: var(--muted);
}

.frm-06__drop:focus-within {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.frm-06__drop.is-over {
  border-color: var(--accent);
  border-style: solid;
  background: color-mix(in oklab,var(--accent) 10%,var(--raised));
}

.frm-06__dropicon {
  display: grid;
  place-items: center;
  width: 2.75rem;
  height: 2.75rem;
  border-radius: .8rem;
  background: var(--surface);
  border: 1px solid var(--line);
  transition: translate .35s var(--ease);
}

.frm-06__drop.is-over .frm-06__dropicon {
  translate: 0 -4px;
}

.frm-06__dropicon svg {
  width: 1.3rem;
  height: 1.3rem;
  fill: none;
  stroke: var(--accent);
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-06__droptext {
  font-size: .95rem;
}

.frm-06__droptext u {
  color: var(--accent);
  text-underline-offset: 3px;
}

.frm-06__files {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .45rem;
}

.frm-06__files li {
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto;
  align-items: center;
  gap: .75rem;
  padding: .55rem .6rem .55rem .55rem;
  border: 1px solid var(--line);
  border-radius: .75rem;
  background: var(--raised);
  animation: frm-06-in .35s var(--ease);
}

.frm-06__thumb {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: .5rem;
  object-fit: cover;
  display: grid;
  place-items: center;
  background: var(--surface);
  border: 1px solid var(--line);
  font: 500 .62rem var(--mono);
  color: var(--muted);
  text-transform: uppercase;
}

.frm-06__meta {
  display: grid;
  gap: .3rem;
  min-width: 0;
}

.frm-06__meta b {
  font-weight: 500;
  font-size: .88rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.frm-06__meta small {
  font: 400 .72rem var(--mono);
  color: var(--muted);
}

.frm-06__track {
  height: .25rem;
  border-radius: 99px;
  background: var(--line);
  overflow: hidden;
}

.frm-06__bar {
  display: block;
  height: 100%;
  background: var(--accent);
  scale: var(--p,0) 1;
  transform-origin: left;
  transition: scale .2s linear;
}

.frm-06__files li.is-done .frm-06__bar {
  background: var(--ok);
}

.frm-06__rm {
  width: 2.25rem;
  height: 2.25rem;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: .55rem;
  background: transparent;
  color: var(--muted);
  cursor: pointer;
}

.frm-06__rm:hover {
  background: color-mix(in oklab,var(--bad) 15%,transparent);
  color: var(--bad);
}

.frm-06__rm:focus-visible {
  outline: 2px solid var(--accent);
}

.frm-06__rm svg {
  width: 1rem;
  height: 1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
}

.frm-06__foot {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding-top: 1.1rem;
  border-top: 1px solid var(--line);
}

.frm-06__cc {
  display: flex;
  align-items: center;
  gap: .55rem;
  min-height: 2.75rem;
  color: var(--muted) !important;
  cursor: pointer;
}

.frm-06__cc input {
  width: 1.05rem;
  height: 1.05rem;
  accent-color: var(--accent);
  margin: 0;
}

.frm-06__submit {
  display: inline-flex;
  align-items: center;
  gap: .8rem;
  min-height: 2.9rem;
  padding: 0 .6rem 0 1.2rem;
  border: 0;
  border-radius: .7rem;
  cursor: pointer;
  font: inherit;
  font-weight: 600;
  color: #04131c;
  background: var(--accent);
  transition: filter .2s, translate .2s var(--ease);
}

.frm-06__submit kbd {
  font: 500 .72rem var(--mono);
  padding: .25rem .45rem;
  border-radius: .4rem;
  background: rgba(0,0,0,.18);
}

.frm-06__submit:hover {
  filter: brightness(1.1);
  translate: 0 -1px;
}

.frm-06__submit:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.frm-06__status {
  margin: -.5rem 0 0;
  font: 400 .82rem var(--mono);
  color: var(--ok);
}

.frm-06__status:empty {
  display: none;
}

.frm-06__status[data-ok="false"] {
  color: var(--bad);
}

.frm-06__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .frm-06 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .frm-06__seg input:checked + span {
    background: Highlight;
    color: HighlightText;
  }

  .frm-06__bar {
    background: Highlight;
  }

  .frm-06__drop {
    border-color: CanvasText;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-06 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-06__theme {
  position: absolute;
  top: 16px;
  right: 16px;
  z-index: 20;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  padding: 0;
  border-radius: 999px;
  border: 1px solid color-mix(in srgb, currentColor 22%, transparent);
  background: color-mix(in srgb, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background-color .2s, transform .2s;
}

.frm-06__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-06__theme:active {
  transform: scale(.94);
}

.frm-06__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-06__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-06__theme .frm-06__sun,
.frm-06__theme[aria-pressed="true"] .frm-06__moon {
  display: none;
}

.frm-06__theme[aria-pressed="true"] .frm-06__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-06__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-06__theme {
    border-color: ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.frm-06').forEach((root) => {
    const btn = root.querySelector(':scope > [data-theme-toggle]');
    if (!btn || btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const mq = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : true);
    const sync = () => {
      const dark = isDark();
      btn.setAttribute('aria-pressed', String(dark));
      btn.title = dark ? 'Switch to light mode' : 'Switch to dark mode';
    };
    btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
    mq.addEventListener('change', sync);
    new MutationObserver(sync).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
    sync();
  });
})();
(() => {
  const root = document.querySelector('.frm-06');
  if (!root) return;
  const MAX_FILES = 5, MAX_MB = 10;
  const drop = root.querySelector('.frm-06__drop'), input = drop.querySelector('input'), list = root.querySelector('.frm-06__files'), live = root.querySelector('#frm-06-live');
  const files = [];
  const size = (b) => b < 1024 ? b + ' B' : b < 1048576 ? (b / 1024).toFixed(0) + ' KB' : (b / 1048576).toFixed(1) + ' MB';
  const setProgress = (row, p) => row.style.setProperty('--p', p / 100);
  const add = (incoming) => {
    const rejected = [];
    [...incoming].forEach((f) => {
      if (files.length >= MAX_FILES) return rejected.push(f.name + ' (limit of ' + MAX_FILES + ' files)');
      if (f.size > MAX_MB * 1048576) return rejected.push(f.name + ' (over ' + MAX_MB + ' MB)');
      const ext = (f.name.split('.').pop() || '').slice(0, 4);
      const li = document.createElement('li');
      const isImg = f.type.startsWith('image/'), url = isImg ? URL.createObjectURL(f) : null;
      li.innerHTML = (isImg ? '<img class="frm-06__thumb" alt="">' : '<span class="frm-06__thumb" aria-hidden="true"></span>') +
        '<div class="frm-06__meta"><b></b><small></small><span class="frm-06__track"><span class="frm-06__bar"></span></span></div>' +
        '<button type="button" class="frm-06__rm"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg></button>';
      if (isImg) li.querySelector('img').src = url; else li.querySelector('.frm-06__thumb').textContent = ext;
      li.querySelector('b').textContent = f.name;
      const meta = li.querySelector('small'); meta.textContent = size(f.size) + ' · uploading…';
      li.querySelector('.frm-06__rm').setAttribute('aria-label', 'Remove ' + f.name);
      const entry = { f, li, url };
      files.push(entry); list.append(li);
      let p = 0;
      const t = setInterval(() => {
        p = Math.min(100, p + 8 + Math.random() * 18); setProgress(li, p);
        if (p >= 100) { clearInterval(t); li.classList.add('is-done'); meta.textContent = size(f.size) + ' · uploaded'; }
      }, 140);
      li.querySelector('.frm-06__rm').addEventListener('click', () => {
        clearInterval(t); if (url) URL.revokeObjectURL(url);
        files.splice(files.indexOf(entry), 1); li.remove(); live.textContent = f.name + ' removed.'; input.focus();
      });
    });
    live.textContent = rejected.length ? 'Not added: ' + rejected.join(', ') : incoming.length + ' file(s) attached.';
  };
  input.addEventListener('change', () => { add(input.files); input.value = ''; });
  let depth = 0;
  drop.addEventListener('dragenter', (e) => { e.preventDefault(); depth++; drop.classList.add('is-over'); });
  drop.addEventListener('dragover', (e) => e.preventDefault());
  drop.addEventListener('dragleave', () => { if (--depth <= 0) { depth = 0; drop.classList.remove('is-over'); } });
  drop.addEventListener('drop', (e) => { e.preventDefault(); depth = 0; drop.classList.remove('is-over'); add(e.dataTransfer.files); });
  const status = root.querySelector('.frm-06__status');
  const submit = () => {
    const bad = [...root.querySelectorAll('[required]')].find((f) => !f.value.trim());
    if (bad) { status.dataset.ok = 'false'; status.textContent = '✕ Subject and description are required.'; bad.focus(); return; }
    const p = root.querySelector('[name="frm-06-p"]:checked').value;
    status.dataset.ok = 'true';
    status.textContent = '✓ Ticket #' + (48000 + Math.floor(Math.random() * 999)) + ' created · priority ' + p + ' · ' + files.length + ' attachment(s)';
  };
  root.querySelector('.frm-06__submit').addEventListener('click', submit);
  root.addEventListener('keydown', (e) => { if ((e.metaKey || e.ctrlKey) && e.key === 'Enter') submit(); });
})();
```
