---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/cloud-storage-drop-zone/"
title: "Cloud Storage Drop Zone"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "Uploading rarely means \"from this laptop\" any more."
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cloud Storage Drop Zone
Source: https://codefronts.com/components/css-file-upload-button/cloud-storage-drop-zone/

Uploading rarely means "from this laptop" any more. This zone offers three sources — device, connected cloud drive, and a direct URL — switched entirely in CSS with a radio group and :has(), so tabbing between sources costs zero JavaScript. A quota meter, a destination bucket selector and per-source empty states make it read like a real storage product rather than a styled input.
## HTML
```html
<div class="fu-17">
  <button class="fu-17__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-17__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-17__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <section class="fu-17__panelWrap" aria-labelledby="fu-17-h">
    <header class="fu-17__head">
      <div>
        <h2 class="fu-17__h" id="fu-17-h">Add to storage</h2>
        <p class="fu-17__sub">Destination
          <select class="fu-17__dest" id="fu-17-dest" aria-label="Destination bucket">
            <option>prod-assets / 2026</option>
            <option>prod-assets / archive</option>
            <option>staging-scratch</option>
          </select>
        </p>
      </div>
      <div class="fu-17__quota">
        <span class="fu-17__quotaTxt">184 GB of 250 GB</span>
        <span class="fu-17__meter"><span></span></span>
      </div>
    </header>

    <fieldset class="fu-17__tabs">
      <legend class="fu-17__vh">Upload source</legend>
      <label class="fu-17__tab"><input type="radio" name="fu-17-src" id="fu-17-device" checked><span>This device</span></label>
      <label class="fu-17__tab"><input type="radio" name="fu-17-src" id="fu-17-cloud"><span>Cloud drive</span></label>
      <label class="fu-17__tab"><input type="radio" name="fu-17-src" id="fu-17-url"><span>From URL</span></label>
    </fieldset>

    <div class="fu-17__panel fu-17__panel--device">
      <div class="fu-17__zone" id="fu-17-zone" role="button" tabindex="0" aria-label="Drop files here or press Enter to browse this device">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M7.4 18.5A4.4 4.4 0 0 1 7 9.8a5.6 5.6 0 0 1 10.7-1.2 3.9 3.9 0 0 1-.5 9.9z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M12 19v-7m0 0-2.6 2.6M12 12l2.6 2.6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <p class="fu-17__zt">Drop files, or <label class="fu-17__browse" for="fu-17-file">browse</label></p>
        <p class="fu-17__zs">Any file type <span aria-hidden="true">·</span> 5 GB per file</p>
        <input class="fu-17__input" id="fu-17-file" type="file" multiple>
      </div>
    </div>

    <div class="fu-17__panel fu-17__panel--cloud">
      <ul class="fu-17__cloud">
        <li><button type="button" data-cloud="brand-kit-2026.zip" data-size="820 MB"><span class="fu-17__ci" aria-hidden="true"></span>brand-kit-2026.zip<em>820 MB</em></button></li>
        <li><button type="button" data-cloud="customer-interviews.mp3" data-size="1.4 GB"><span class="fu-17__ci" aria-hidden="true"></span>customer-interviews.mp3<em>1.4 GB</em></button></li>
        <li><button type="button" data-cloud="q2-financials.xlsx" data-size="3.2 MB"><span class="fu-17__ci" aria-hidden="true"></span>q2-financials.xlsx<em>3.2 MB</em></button></li>
      </ul>
    </div>

    <div class="fu-17__panel fu-17__panel--url">
      <label class="fu-17__urlLabel" for="fu-17-urlin">Public file URL</label>
      <div class="fu-17__urlRow">
        <input class="fu-17__url" id="fu-17-urlin" type="url" inputmode="url" placeholder="https://cdn.example.com/report.pdf" pattern="https://.*" aria-describedby="fu-17-urlerr">
        <button class="fu-17__import" id="fu-17-import" type="button">Import</button>
      </div>
      <p class="fu-17__urlErr" id="fu-17-urlerr">Enter a full https:// URL</p>
    </div>

    <ul class="fu-17__result" id="fu-17-result"></ul>
    <p class="fu-17__status" id="fu-17-status" role="status" aria-live="polite"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fu-17 {
  --bg: #f4f6fa;
  --surface: #ffffff;
  --raise: #f7f9fc;
  --ink: #0b1018;
  --muted: #5a6377;
  --line: #e2e7f0;
  --acc: #0b7cff;
  --ok: #0f9d63;
  --danger: #d92548;
  --used: 74%;
  --sans: "Outfit",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(70% 45% at 0% 0%, color-mix(in oklab,var(--acc) 12%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.fu-17,
.fu-17 *,
.fu-17 *::before,
.fu-17 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-17 {
    --acc: oklch(58% .2 255);
    --ok: oklch(58% .14 158);
    --danger: oklch(55% .2 18);
  }
}

.fu-17__panelWrap {
  container-type: inline-size;
  inline-size: min(34rem,100%);
  display: grid;
  gap: .9rem;
  padding: clamp(1.1rem,3.5vw,1.5rem);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.4rem;
  box-shadow: 0 30px 70px -55px rgba(11,16,24,.6);
}

.fu-17__head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.fu-17__h {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: -.03em;
}

.fu-17__sub {
  margin: .3rem 0 0;
  display: flex;
  align-items: center;
  gap: .4rem;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

.fu-17__dest {
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--ink);
  background: var(--raise);
  border: 1px solid var(--line);
  border-radius: .5rem;
  padding: .35rem .5rem;
  min-block-size: 2rem;
  cursor: pointer;
}

.fu-17__dest:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.fu-17__quota {
  display: grid;
  gap: .3rem;
  justify-items: end;
}

.fu-17__quotaTxt {
  font-family: var(--mono);
  font-size: .625rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.fu-17__meter {
  display: block;
  inline-size: 8rem;
  block-size: .35rem;
  border-radius: 999px;
  background: var(--line);
  overflow: hidden;
}

.fu-17__meter span {
  display: block;
  block-size: 100%;
  inline-size: var(--used);
  background: linear-gradient(90deg,var(--acc),var(--ok));
  border-radius: 999px;
}

.fu-17__tabs {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: .25rem;
  border: 0;
  margin: 0;
  padding: .25rem;
  border-radius: .8rem;
  background: var(--raise);
  border: 1px solid var(--line);
}

.fu-17__tab {
  position: relative;
  display: grid;
}

.fu-17__tab input {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.fu-17__tab span {
  display: grid;
  place-items: center;
  min-block-size: 2.5rem;
  padding: .4rem .6rem;
  cursor: pointer;
  border-radius: .6rem;
  font-size: .8125rem;
  font-weight: 600;
  color: var(--muted);
  transition: background .25s ease, color .25s ease, box-shadow .25s ease;
}

.fu-17__tab span:hover {
  color: var(--ink);
}

.fu-17__tab input:checked + span {
  background: var(--surface);
  color: var(--acc);
  box-shadow: 0 1px 3px rgba(11,16,24,.12);
}

.fu-17__tab input:focus-visible + span {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.fu-17__panel {
  display: none;
  gap: .6rem;
}

.fu-17:has(#fu-17-device:checked) .fu-17__panel--device {
  display: grid;
}

.fu-17:has(#fu-17-cloud:checked) .fu-17__panel--cloud {
  display: grid;
}

.fu-17:has(#fu-17-url:checked) .fu-17__panel--url {
  display: grid;
}

.fu-17__zone {
  position: relative;
  cursor: pointer;
  display: grid;
  justify-items: center;
  gap: .3rem;
  text-align: center;
  padding: clamp(1.5rem,5vw,2.25rem) 1rem;
  border-radius: 1.1rem;
  border: 2px dashed var(--line);
  background: var(--raise);
  color: var(--muted);
  transition: border-color .25s ease, background .25s ease, transform .25s cubic-bezier(.16,1,.3,1);
}

.fu-17__zone svg {
  inline-size: 2.1rem;
  block-size: 2.1rem;
  color: var(--acc);
}

.fu-17__zone:hover {
  border-color: color-mix(in oklab,var(--acc) 45%,var(--line));
}

.fu-17__zone:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.fu-17__zone.is-over {
  border-color: var(--acc);
  border-style: solid;
  background: color-mix(in oklab,var(--acc) 8%,var(--raise));
  transform: scale(1.01);
}

.fu-17__zt {
  margin: 0;
  font-size: .9375rem;
  font-weight: 600;
  color: var(--ink);
}

.fu-17__zs {
  margin: 0;
  font-family: var(--mono);
  font-size: .625rem;
}

.fu-17__browse {
  cursor: pointer;
  color: var(--acc);
  text-decoration: underline;
  text-underline-offset: 3px;
}

.fu-17__input {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: 0;
  border: 0;
  overflow: hidden;
  opacity: 0;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  white-space: nowrap;
}

.fu-17__cloud {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .4rem;
}

.fu-17__cloud button {
  inline-size: 100%;
  display: flex;
  align-items: center;
  gap: .7rem;
  cursor: pointer;
  text-align: start;
  min-block-size: 3rem;
  padding: .6rem .75rem;
  border-radius: .8rem;
  border: 1px solid var(--line);
  background: var(--raise);
  color: var(--ink);
  font-family: var(--sans);
  font-size: .875rem;
  font-weight: 600;
  transition: border-color .2s ease, background .2s ease, transform .2s cubic-bezier(.16,1,.3,1);
}

.fu-17__cloud button:hover {
  border-color: var(--acc);
  background: var(--surface);
  transform: translateX(2px);
}

.fu-17__cloud button:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.fu-17__cloud em {
  margin-inline-start: auto;
  font-family: var(--mono);
  font-size: .625rem;
  font-style: normal;
  color: var(--muted);
}

.fu-17__ci {
  inline-size: 1.6rem;
  block-size: 1.6rem;
  border-radius: .45rem;
  background: color-mix(in oklab,var(--acc) 18%,transparent);
  flex: none;
}

.fu-17__urlLabel {
  font-family: var(--mono);
  font-size: .625rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.fu-17__urlRow {
  display: flex;
  gap: .5rem;
}

.fu-17__url {
  flex: 1;
  min-inline-size: 0;
  min-block-size: 2.85rem;
  padding: .6rem .8rem;
  border-radius: .75rem;
  border: 1px solid var(--line);
  background: var(--raise);
  color: var(--ink);
  font-family: var(--mono);
  font-size: .8125rem;
}

.fu-17__url:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  border-color: var(--acc);
}

.fu-17__url:user-invalid {
  border-color: var(--danger);
}

.fu-17__urlErr {
  margin: 0;
  display: none;
  font-family: var(--mono);
  font-size: .625rem;
  color: var(--danger);
}

.fu-17__url:user-invalid ~ .fu-17__urlErr,
.fu-17__panel--url:has(.fu-17__url:user-invalid) .fu-17__urlErr {
  display: block;
}

.fu-17__import {
  min-block-size: 2.85rem;
  padding: .6rem 1.1rem;
  cursor: pointer;
  border: 0;
  border-radius: .75rem;
  background: var(--acc);
  color: #fff;
  font-family: var(--sans);
  font-size: .875rem;
  font-weight: 600;
  transition: filter .2s ease, transform .2s cubic-bezier(.16,1,.3,1);
}

.fu-17__import:hover {
  filter: brightness(1.08);
  transform: translateY(-1px);
}

.fu-17__import:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.fu-17__result {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .35rem;
}

.fu-17__result:empty {
  display: none;
}

.fu-17__result li {
  display: flex;
  align-items: center;
  gap: .5rem;
  padding: .5rem .7rem;
  border-radius: .7rem;
  background: color-mix(in oklab,var(--ok) 9%,transparent);
  border: 1px solid color-mix(in oklab,var(--ok) 28%,transparent);
  font-family: var(--mono);
  font-size: .6875rem;
  color: color-mix(in oklab,var(--ok) 70%,var(--ink));
}

.fu-17__result li em {
  margin-inline-start: auto;
  font-style: normal;
  opacity: .8;
}

.fu-17__status {
  margin: 0;
  min-block-size: 1rem;
  font-family: var(--mono);
  font-size: .625rem;
  color: var(--muted);
}

.fu-17__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@container (max-width: 26rem) {
  .fu-17__quota {
    justify-items: start;
  }

  .fu-17__meter {
    inline-size: 100%;
  }
}

@media (prefers-color-scheme: dark) {
  .fu-17:not([data-theme="light"]) {
    --bg: #080a0f;
    --surface: #101319;
    --raise: #161a23;
    --ink: #eef1f7;
    --muted: #8a93a6;
    --line: #232936;
    --acc: #4b9bff;
    --ok: #35d68f;
    --danger: #ff5f77;
  }
}

.fu-17[data-theme="dark"] {
  --bg: #080a0f;
  --surface: #101319;
  --raise: #161a23;
  --ink: #eef1f7;
  --muted: #8a93a6;
  --line: #232936;
  --acc: #4b9bff;
  --ok: #35d68f;
  --danger: #ff5f77;
}

@media (prefers-reduced-motion: reduce) {
  .fu-17 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fu-17__panelWrap,
    .fu-17__zone,
    .fu-17__cloud button {
    border: 1px solid CanvasText;
  }

  .fu-17__tab input:checked + span {
    background: Highlight;
    color: HighlightText;
  }

  .fu-17__import {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
/* ── in-demo theme toggle ── */

.fu-17 {
  position: relative;
}

.fu-17__theme {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.4rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.4rem);
  z-index: 20;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab,currentColor 30%,transparent);
  background: color-mix(in oklab,currentColor 12%,transparent);
  color: inherit;
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1), border-color .25s ease;
}

.fu-17__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-17__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-17__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-17__sun {
  display: none;
}

.fu-17__theme[aria-pressed="true"] .fu-17__sun {
  display: block;
}

.fu-17__theme[aria-pressed="true"] .fu-17__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-17__theme {
    transition: none;
  }

  .fu-17__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-17__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-17');
  if (!root) return;
  const zone = root.querySelector('#fu-17-zone');
  const input = root.querySelector('#fu-17-file');
  const result = root.querySelector('#fu-17-result');
  const status = root.querySelector('#fu-17-status');
  const dest = root.querySelector('#fu-17-dest');
  const urlIn = root.querySelector('#fu-17-urlin');
  let depth = 0;

  const fmt = (n) => {
    const u = ['B','KB','MB','GB']; let i = 0;
    while (n >= 1024 && i < u.length - 1) { n /= 1024; i++; }
    return Math.round(n) + ' ' + u[i];
  };
  const land = (name, size) => {
    const li = document.createElement('li');
    li.append(name, Object.assign(document.createElement('em'), { textContent: size }));
    result.prepend(li);
    status.textContent = name + ' queued for ' + dest.value;
  };

  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(t =>
    zone.addEventListener(t, e => { e.preventDefault(); e.stopPropagation(); })
  );
  zone.addEventListener('dragenter', () => { depth++; zone.classList.add('is-over'); });
  zone.addEventListener('dragleave', () => { if (--depth <= 0) { depth = 0; zone.classList.remove('is-over'); } });
  zone.addEventListener('drop', e => {
    depth = 0; zone.classList.remove('is-over');
    [...e.dataTransfer.files].forEach(f => land(f.name, fmt(f.size)));
  });
  zone.addEventListener('click', e => { if (!e.target.closest('label')) input.click(); });
  zone.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); input.click(); } });
  input.addEventListener('change', () => { [...input.files].forEach(f => land(f.name, fmt(f.size))); input.value = ''; });

  root.querySelectorAll('[data-cloud]').forEach(btn =>
    btn.addEventListener('click', () => land(btn.dataset.cloud, btn.dataset.size))
  );

  root.querySelector('#fu-17-import').addEventListener('click', () => {
    if (!urlIn.checkValidity() || !urlIn.value) { urlIn.focus(); status.textContent = 'Enter a valid https URL first'; return; }
    const name = urlIn.value.split('/').pop() || 'remote-file';
    status.textContent = 'Fetching ' + name + '…';
    setTimeout(() => { land(name, 'remote'); urlIn.value = ''; }, 900);   // simulated server-side fetch
  });

  root.querySelectorAll('input[name="fu-17-src"]').forEach(r =>
    r.addEventListener('change', () => { status.textContent = r.nextElementSibling.textContent + ' selected as the source'; })
  );
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-17');
  const btn = root && root.querySelector('.fu-17__theme');
  if (!btn) return;
  const isDark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    btn.setAttribute('aria-pressed', String(isDark()));
    btn.setAttribute('aria-label', isDark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  sync();
})();
```
