---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/fetch-upload-progress-bar-with-xhr-onprogress-event/"
title: "Fetch Upload Progress Bar with XHR onprogress Event"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "The upload card every file picker needs: filename, byte counter, live percentage, cancel button, and a completion state with a real checkmark."
has_js: "true"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fetch Upload Progress Bar with XHR onprogress Event
Source: https://codefronts.com/components/css-progress-bars/fetch-upload-progress-bar-with-xhr-onprogress-event/

The upload card every file picker needs: filename, byte counter, live percentage, cancel button, and a completion state with a real checkmark. The bar is driven by xhr.upload.onprogress — the only browser event that reports upload bytes, since fetch() still cannot.
## HTML
```html
<div class="pb-03">
  <button class="pb-03__theme" type="button" aria-pressed="false" aria-label="Toggle dark or light theme">
    <svg class="pb-03__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-03__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
  </button>

  <div class="pb-03__stage">
    <div class="pb-03__card" id="pb-03-card" data-state="uploading">
      <header class="pb-03__head">
        <p class="pb-03__eyebrow"><span class="pb-03__badge">Assets</span><span class="pb-03__mono">POST /api/assets</span></p>
        <h2 class="pb-03__title">Uploading to your media library</h2>
      </header>

      <div class="pb-03__file">
        <span class="pb-03__thumb" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none"><rect x="3.2" y="4.4" width="17.6" height="15.2" rx="2.6" stroke="currentColor" stroke-width="1.7"/><circle cx="8.8" cy="9.6" r="1.7" stroke="currentColor" stroke-width="1.5"/><path d="M3.6 16.4l4.3-3.6 3.5 2.9 3.2-2.6 5.8 4.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
        <span class="pb-03__fileMeta">
          <span class="pb-03__name" id="pb-03-name">hero-banner-v3.png</span>
          <span class="pb-03__sub pb-03__mono" id="pb-03-sub">1.2 MB / 2.4 MB &middot; 52%</span>
        </span>
        <span class="pb-03__status" id="pb-03-status">
          <svg class="pb-03__spin" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 3.5a8.5 8.5 0 1 0 8.5 8.5" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"/></svg>
          <svg class="pb-03__check" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9.2" stroke="currentColor" stroke-width="1.7"/><path d="M7.8 12.4l3 3 5.4-6" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <svg class="pb-03__cross" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9.2" stroke="currentColor" stroke-width="1.7"/><path d="M8.8 8.8l6.4 6.4M15.2 8.8l-6.4 6.4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        </span>
      </div>

      <div class="pb-03__bar" id="pb-03-bar" role="progressbar" aria-valuenow="52" aria-valuemin="0" aria-valuemax="100" aria-valuetext="1.2 MB of 2.4 MB uploaded" aria-label="Uploading hero-banner-v3.png" style="--value:52">
        <span class="pb-03__fill"></span>
      </div>

      <div class="pb-03__footer">
        <p class="pb-03__msg" id="pb-03-msg">Transferring &middot; <span class="pb-03__mono">1.9 MB/s</span></p>
        <div class="pb-03__actions">
          <button class="pb-03__btn" type="button" id="pb-03-cancel">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7L7 17" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>Cancel
          </button>
          <button class="pb-03__btn pb-03__btn--primary" type="button" id="pb-03-retry">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.2v5.4M12 4.2 8.6 7.6M12 4.2l3.4 3.4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/><path d="M5.4 11.2a6.9 6.9 0 1 0 6.6-5" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>Upload again
          </button>
        </div>
      </div>
      <p class="pb-03__live" id="pb-03-live" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-03 {
  --bg: #080b11;
  --card: #0d121c;
  --ink: #eaf0fa;
  --muted: rgba(234,240,250,.6);
  --line: rgba(234,240,250,.12);
  --track: rgba(234,240,250,.08);
  --accent: #3b82f6;
  --accent-2: #60a5fa;
  --ok: #10b981;
  --err: #ef4444;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono",SFMono-Regular,Menlo,monospace;
  inline-size: 100%;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(70% .18 260)) {
  .pb-03 {
    --accent: oklch(64% .17 258);
    --ok: oklch(74% .16 162);
    --err: oklch(64% .21 25);
  }
}

.pb-03 *,
.pb-03 *::before,
.pb-03 *::after {
  box-sizing: border-box;
}

.pb-03__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(100% 70% at 20% 0%,color-mix(in srgb,var(--accent) 18%,transparent),transparent 58%);
}

.pb-03__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,2.4vw,1.6rem);
  inset-inline-end: clamp(.9rem,2.4vw,1.6rem);
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 99px;
  border: 1px solid var(--line);
  color: var(--ink);
  background: rgba(255,255,255,.06);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .2s,transform .2s;
}

.pb-03__theme:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.11);
}

.pb-03__theme:focus-visible {
  outline: 2px solid var(--accent-2);
  outline-offset: 3px;
}

.pb-03__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-03__sun {
  display: none;
}

.pb-03__moon {
  display: block;
}

.pb-03[data-theme="light"] .pb-03__sun {
  display: block;
}

.pb-03[data-theme="light"] .pb-03__moon {
  display: none;
}

.pb-03__card {
  inline-size: min(38rem,100%);
  display: grid;
  gap: clamp(.95rem,2.2vw,1.4rem);
  padding: clamp(1.3rem,3.2vw,2rem);
  border-radius: 1.5rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--card) 94%,transparent);
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset,0 30px 70px -40px rgba(0,0,0,.95);
}

.pb-03__head {
  display: grid;
  gap: .45rem;
}

.pb-03__eyebrow {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .6rem;
}

.pb-03__badge {
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: .28rem .55rem;
  border-radius: .45rem;
  color: var(--accent-2);
  background: color-mix(in srgb,var(--accent) 16%,transparent);
  border: 1px solid color-mix(in srgb,var(--accent) 32%,transparent);
}

.pb-03__mono {
  font-family: var(--mono);
  font-size: .76rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pb-03__title {
  margin: 0;
  font-size: clamp(1.15rem,2.6vw,1.5rem);
  line-height: 1.2;
  letter-spacing: -.02em;
  font-weight: 600;
}

.pb-03__file {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: .85rem;
  align-items: center;
}

.pb-03__thumb {
  inline-size: 2.9rem;
  block-size: 2.9rem;
  display: grid;
  place-items: center;
  border-radius: .8rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--accent) 14%,transparent);
  color: var(--accent-2);
}

.pb-03__thumb svg {
  inline-size: 1.5rem;
  block-size: 1.5rem;
}

.pb-03__fileMeta {
  display: grid;
  gap: .2rem;
  min-inline-size: 0;
}

.pb-03__name {
  font-size: .95rem;
  font-weight: 550;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.pb-03__status {
  display: grid;
  place-items: center;
  inline-size: 1.6rem;
  block-size: 1.6rem;
}

.pb-03__status svg {
  inline-size: 1.35rem;
  block-size: 1.35rem;
  grid-area: 1/1;
  display: none;
}

.pb-03__spin {
  color: var(--accent-2);
  animation: pb-03-spin 900ms linear infinite;
}

@keyframes pb-03-spin {
  to {
    transform: rotate(360deg);
  }
}

.pb-03__check {
  color: var(--ok);
}

.pb-03__cross {
  color: var(--err);
}

.pb-03__card[data-state="uploading"] .pb-03__spin,
.pb-03__card[data-state="done"] .pb-03__check,
.pb-03__card[data-state="cancelled"] .pb-03__cross {
  display: block;
}

.pb-03__card[data-state="cancelled"] .pb-03__name {
  text-decoration: line-through;
  color: var(--muted);
}

.pb-03__bar {
  position: relative;
  inline-size: 100%;
  block-size: .7rem;
  border-radius: 99px;
  background: var(--track);
  border: 1px solid var(--line);
  overflow: hidden;
  box-shadow: 0 1px 2px rgba(0,0,0,.4) inset;
}

.pb-03__fill {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: calc(var(--value,0) * 1%);
  border-radius: 99px;
  background: linear-gradient(90deg,var(--accent),var(--accent-2));
  transition: inline-size .3s linear,background .3s;
  will-change: inline-size;
}

.pb-03__card[data-state="done"] .pb-03__fill {
  background: linear-gradient(90deg,var(--ok),color-mix(in srgb,var(--ok) 70%,var(--accent-2)));
}

.pb-03__card[data-state="cancelled"] .pb-03__fill {
  background: color-mix(in srgb,var(--err) 70%,transparent);
}

.pb-03__footer {
  display: flex;
  flex-wrap: wrap;
  gap: .75rem;
  align-items: center;
  justify-content: space-between;
}

.pb-03__msg {
  margin: 0;
  font-size: .85rem;
  color: var(--muted);
}

.pb-03__card[data-state="done"] .pb-03__msg {
  color: var(--ok);
  font-weight: 550;
}

.pb-03__card[data-state="cancelled"] .pb-03__msg {
  color: var(--err);
  font-weight: 550;
}

.pb-03__actions {
  display: flex;
  gap: .5rem;
}

.pb-03__btn {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-block-size: 2.75rem;
  padding: .6rem 1rem;
  border-radius: .8rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 6%,transparent);
  color: var(--ink);
  font: inherit;
  font-size: .86rem;
  font-weight: 550;
  cursor: pointer;
  transition: transform .18s,background .18s;
}

.pb-03__btn svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.pb-03__btn:hover {
  transform: translateY(-1px);
  background: color-mix(in srgb,var(--ink) 12%,transparent);
}

.pb-03__btn:focus-visible {
  outline: 2px solid var(--accent-2);
  outline-offset: 3px;
}

.pb-03__btn--primary {
  background: var(--accent);
  border-color: transparent;
  color: #fff;
}

.pb-03__btn--primary:hover {
  background: color-mix(in srgb,var(--accent) 88%,white);
}

.pb-03__card[data-state="uploading"] .pb-03__btn--primary {
  display: none;
}

.pb-03__card:not([data-state="uploading"]) #pb-03-cancel {
  display: none;
}

.pb-03__live {
  margin: 0;
  min-block-size: 1.1rem;
  font-size: .78rem;
  color: var(--muted);
}

.pb-03[data-theme="light"] {
  --bg: #f5f7fb;
  --card: #ffffff;
  --ink: #0a1020;
  --muted: rgba(10,16,32,.62);
  --line: rgba(10,16,32,.1);
  --track: rgba(10,16,32,.07);
  --accent: #2563eb;
  --accent-2: #1d4ed8;
  --ok: #059669;
  --err: #dc2626;
}

.pb-03[data-theme="light"] .pb-03__theme {
  background: rgba(10,16,32,.05);
}

@media (prefers-color-scheme: light) {
  .pb-03:not([data-theme="dark"]) {
    --bg: #f5f7fb;
    --card: #ffffff;
    --ink: #0a1020;
    --muted: rgba(10,16,32,.62);
    --line: rgba(10,16,32,.1);
    --track: rgba(10,16,32,.07);
    --accent: #2563eb;
    --accent-2: #1d4ed8;
    --ok: #059669;
    --err: #dc2626;
  }

  .pb-03:not([data-theme="dark"]) .pb-03__theme {
    background: rgba(10,16,32,.05);
  }

  .pb-03:not([data-theme="dark"]) .pb-03__sun {
    display: block;
  }

  .pb-03:not([data-theme="dark"]) .pb-03__moon {
    display: none;
  }

  .pb-03[data-theme="dark"] .pb-03__sun {
    display: none;
  }

  .pb-03[data-theme="dark"] .pb-03__moon {
    display: block;
  }
}

@media (max-width: 26rem) {
  .pb-03__footer {
    align-items: flex-start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-03 *,
    .pb-03 *::before,
    .pb-03 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .pb-03__card,
    .pb-03__bar,
    .pb-03__btn,
    .pb-03__theme,
    .pb-03__thumb {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .pb-03__fill {
    background: Highlight;
  }
}
```

## JavaScript
```js
const pb03 = document.querySelector('.pb-03');
if (pb03) {
  const q = (s) => pb03.querySelector(s);
  const [card, bar, sub, msg, live] = ['#pb-03-card','#pb-03-bar','#pb-03-sub','#pb-03-msg','#pb-03-live'].map(q);
  const TOTAL = 2.4, mb = (n) => n.toFixed(1) + ' MB';
  let pct = 0, timer;
  // Real usage: xhr.upload.onprogress = (e) => e.lengthComputable && set(Math.round(e.loaded / e.total * 100));
  const set = (n) => {
    pct = Math.min(100, n);
    bar.style.setProperty('--value', pct);
    bar.setAttribute('aria-valuenow', pct);
    bar.setAttribute('aria-valuetext', mb(TOTAL * pct / 100) + ' of ' + mb(TOTAL) + ' uploaded');
    sub.innerHTML = mb(TOTAL * pct / 100) + ' / ' + mb(TOTAL) + ' \u00b7 ' + pct + '%';
  };
  const stop = () => clearInterval(timer);
  const start = () => {
    stop(); card.dataset.state = 'uploading'; live.textContent = ''; set(0);
    msg.innerHTML = 'Transferring \u00b7 <span class="pb-03__mono">1.9 MB/s</span>';
    timer = setInterval(() => {
      set(pct + 4);
      if (pct >= 100) { stop(); card.dataset.state = 'done'; msg.textContent = 'Upload complete'; live.textContent = 'hero-banner-v3.png uploaded, 2.4 megabytes.'; }
    }, 120);
  };
  q('#pb-03-cancel').addEventListener('click', () => { // real usage: xhr.abort()
    stop(); card.dataset.state = 'cancelled'; msg.textContent = 'Cancelled'; live.textContent = 'Upload cancelled.';
  });
  q('#pb-03-retry').addEventListener('click', start);
  q('.pb-03__theme').addEventListener('click', (e) => {
    const light = pb03.dataset.theme !== 'light';
    pb03.dataset.theme = light ? 'light' : 'dark';
    e.currentTarget.setAttribute('aria-pressed', String(!light));
  });
  start();
}
```
