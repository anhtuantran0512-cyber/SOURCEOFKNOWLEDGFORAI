---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/download-queue-progress-with-per-file-bars-and-overall-total/"
title: "Download Queue Progress with Per File Bars and Overall Total"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "Four parallel downloads with their own bars, speeds and pause buttons, under one aggregate header that reports the weighted total — not the average of four…"
has_js: "true"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Download Queue Progress with Per File Bars and Overall Total
Source: https://codefronts.com/components/css-progress-bars/download-queue-progress-with-per-file-bars-and-overall-total/

Four parallel downloads with their own bars, speeds and pause buttons, under one aggregate header that reports the weighted total — not the average of four percentages, which is the bug almost every queue UI ships with.
## HTML
```html
<div class="pb-07">
  <button class="pb-07__theme" type="button" aria-pressed="false" aria-label="Toggle dark or light theme">
    <svg class="pb-07__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-07__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
  </button>

  <div class="pb-07__stage">
    <div class="pb-07__card">
      <header class="pb-07__head">
        <span class="pb-07__icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none"><path d="M12 4v9.4M8.3 10.2 12 13.9l3.7-3.7" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M4.5 16.5v1.9A1.6 1.6 0 0 0 6.1 20h11.8a1.6 1.6 0 0 0 1.6-1.6v-1.9" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        </span>
        <span class="pb-07__headMeta">
          <span class="pb-07__title">Syncing workspace</span>
          <span class="pb-07__sub pb-07__mono" id="pb-07-count">1 of 4 complete &middot; 186.4 MB total</span>
        </span>
        <span class="pb-07__total pb-07__mono" id="pb-07-total">37%</span>
      </header>

      <div class="pb-07__bar pb-07__bar--total" id="pb-07-agg" role="progressbar" aria-valuenow="37" aria-valuemin="0" aria-valuemax="100" aria-valuetext="37 percent of 186.4 megabytes downloaded" aria-label="Overall download progress" style="--value:37">
        <span class="pb-07__fill"></span>
      </div>

      <ul class="pb-07__rows" id="pb-07-rows">
        <li class="pb-07__row" data-state="active" data-i="0">
          <span class="pb-07__glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M6.5 3.8h7.2l4 4v12.4H6.5z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M13.5 3.8v4.2h4.2" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></span>
          <span class="pb-07__rowMeta">
            <span class="pb-07__name">dataset.csv</span>
            <span class="pb-07__sub pb-07__mono"><span class="pb-07__loaded">3.1 MB</span> / 12.8 MB &middot; <span class="pb-07__speed">1.4 MB/s</span></span>
          </span>
          <span class="pb-07__bar" role="progressbar" aria-valuenow="24" aria-valuemin="0" aria-valuemax="100" aria-valuetext="3.1 of 12.8 megabytes" aria-label="dataset.csv" style="--value:24"><span class="pb-07__fill"></span></span>
          <button class="pb-07__pause" type="button" aria-pressed="false" aria-label="Pause dataset.csv">
            <svg class="pb-07__pauseIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M9.5 6.5v11M14.5 6.5v11" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            <svg class="pb-07__playIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M8.5 6l9 6-9 6z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
            <svg class="pb-07__doneIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 12.4l4 4L18.4 8" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
        </li>
        <li class="pb-07__row" data-state="active" data-i="1">
          <span class="pb-07__glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><rect x="4" y="5" width="16" height="14" rx="2.4" stroke="currentColor" stroke-width="1.6"/><path d="M4 9.4h16" stroke="currentColor" stroke-width="1.6"/></svg></span>
          <span class="pb-07__rowMeta">
            <span class="pb-07__name">framer-motion.tgz</span>
            <span class="pb-07__sub pb-07__mono"><span class="pb-07__loaded">18.9 MB</span> / 42.6 MB &middot; <span class="pb-07__speed">3.2 MB/s</span></span>
          </span>
          <span class="pb-07__bar" role="progressbar" aria-valuenow="44" aria-valuemin="0" aria-valuemax="100" aria-valuetext="18.9 of 42.6 megabytes" aria-label="framer-motion.tgz" style="--value:44"><span class="pb-07__fill"></span></span>
          <button class="pb-07__pause" type="button" aria-pressed="false" aria-label="Pause framer-motion.tgz">
            <svg class="pb-07__pauseIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M9.5 6.5v11M14.5 6.5v11" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            <svg class="pb-07__playIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M8.5 6l9 6-9 6z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
            <svg class="pb-07__doneIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 12.4l4 4L18.4 8" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
        </li>
        <li class="pb-07__row" data-state="active" data-i="2">
          <span class="pb-07__glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M12 4.5 19 8.2v7.6L12 19.5 5 15.8V8.2z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></span>
          <span class="pb-07__rowMeta">
            <span class="pb-07__name">podcast-episode-47.mp3</span>
            <span class="pb-07__sub pb-07__mono"><span class="pb-07__loaded">41.0 MB</span> / 88.2 MB &middot; <span class="pb-07__speed">5.8 MB/s</span></span>
          </span>
          <span class="pb-07__bar" role="progressbar" aria-valuenow="46" aria-valuemin="0" aria-valuemax="100" aria-valuetext="41.0 of 88.2 megabytes" aria-label="podcast-episode-47.mp3" style="--value:46"><span class="pb-07__fill"></span></span>
          <button class="pb-07__pause" type="button" aria-pressed="false" aria-label="Pause podcast-episode-47.mp3">
            <svg class="pb-07__pauseIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M9.5 6.5v11M14.5 6.5v11" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            <svg class="pb-07__playIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M8.5 6l9 6-9 6z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
            <svg class="pb-07__doneIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 12.4l4 4L18.4 8" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
        </li>
        <li class="pb-07__row" data-state="done" data-i="3">
          <span class="pb-07__glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M7 4.5h10v15H7z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M9.6 9h4.8M9.6 12.4h4.8M9.6 15.8h3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></span>
          <span class="pb-07__rowMeta">
            <span class="pb-07__name">theme.css</span>
            <span class="pb-07__sub pb-07__mono"><span class="pb-07__loaded">42.8 MB</span> / 42.8 MB &middot; <span class="pb-07__speed">done</span></span>
          </span>
          <span class="pb-07__bar" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" aria-valuetext="42.8 of 42.8 megabytes" aria-label="theme.css" style="--value:100"><span class="pb-07__fill"></span></span>
          <button class="pb-07__pause" type="button" aria-pressed="false" aria-label="theme.css complete" disabled>
            <svg class="pb-07__pauseIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M9.5 6.5v11M14.5 6.5v11" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            <svg class="pb-07__playIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M8.5 6l9 6-9 6z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
            <svg class="pb-07__doneIcon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 12.4l4 4L18.4 8" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
        </li>
      </ul>

      <footer class="pb-07__foot">
        <p class="pb-07__note pb-07__mono">overall = sum(loaded) / sum(total) &mdash; weighted, never averaged</p>
        <button class="pb-07__btn" type="button" id="pb-07-restart">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.2v5.4M12 4.2 8.6 7.6M12 4.2l3.4 3.4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/><path d="M5.4 11.2a6.9 6.9 0 1 0 6.6-5" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>Restart queue
        </button>
      </footer>
      <p class="pb-07__live" id="pb-07-live" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-07 {
  --bg: #07090e;
  --card: #0c1016;
  --card2: #11161f;
  --ink: #e9eef7;
  --muted: rgba(233,238,247,.58);
  --line: rgba(233,238,247,.11);
  --track: rgba(233,238,247,.08);
  --accent: #38bdf8;
  --accent-2: #818cf8;
  --ok: #10b981;
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

@supports (color: oklch(76% .13 220)) {
  .pb-07 {
    --accent: oklch(78% .13 220);
    --accent-2: oklch(70% .16 277);
    --ok: oklch(74% .16 162);
  }
}

.pb-07 *,
.pb-07 *::before,
.pb-07 *::after {
  box-sizing: border-box;
}

.pb-07__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(90% 60% at 100% 0%,color-mix(in srgb,var(--accent) 15%,transparent),transparent 60%), radial-gradient(80% 60% at 0% 100%,color-mix(in srgb,var(--accent-2) 12%,transparent),transparent 60%);
}

.pb-07__theme {
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

.pb-07__theme:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.11);
}

.pb-07__theme:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-07__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-07__sun {
  display: none;
}

.pb-07__moon {
  display: block;
}

.pb-07[data-theme="light"] .pb-07__sun {
  display: block;
}

.pb-07[data-theme="light"] .pb-07__moon {
  display: none;
}

.pb-07__card {
  inline-size: min(44rem,100%);
  display: grid;
  gap: clamp(.9rem,2.1vw,1.3rem);
  padding: clamp(1.2rem,3vw,1.9rem);
  border-radius: 1.5rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--card) 93%,transparent);
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset,0 32px 76px -42px rgba(0,0,0,.95);
}

.pb-07__head {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: .85rem;
  align-items: center;
}

.pb-07__icon {
  inline-size: 2.6rem;
  block-size: 2.6rem;
  display: grid;
  place-items: center;
  border-radius: .8rem;
  color: var(--accent);
  border: 1px solid color-mix(in srgb,var(--accent) 30%,transparent);
  background: color-mix(in srgb,var(--accent) 14%,transparent);
}

.pb-07__icon svg {
  inline-size: 1.45rem;
  block-size: 1.45rem;
}

.pb-07__headMeta {
  display: grid;
  gap: .15rem;
  min-inline-size: 0;
}

.pb-07__title {
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.pb-07__mono {
  font-family: var(--mono);
  font-variant-numeric: tabular-nums;
}

.pb-07__sub {
  font-size: .74rem;
  color: var(--muted);
}

.pb-07__total {
  font-size: 1.35rem;
  font-weight: 650;
  letter-spacing: -.02em;
}

.pb-07__bar {
  position: relative;
  display: block;
  inline-size: 100%;
  block-size: .45rem;
  border-radius: 99px;
  overflow: hidden;
  background: var(--track);
  border: 1px solid var(--line);
  box-shadow: 0 1px 2px rgba(0,0,0,.4) inset;
}

.pb-07__bar--total {
  block-size: .7rem;
}

.pb-07__fill {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: calc(var(--value,0) * 1%);
  border-radius: 99px;
  background: linear-gradient(90deg,var(--accent),var(--accent-2));
  transition: inline-size .3s linear;
}

.pb-07__rows {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .15rem;
}

.pb-07__row {
  display: grid;
  grid-template-columns: auto minmax(0,1fr) minmax(5rem,10rem) auto;
  gap: .8rem;
  align-items: center;
  padding: .7rem .25rem;
  border-block-start: 1px solid var(--line);
}

.pb-07__glyph {
  inline-size: 2.1rem;
  block-size: 2.1rem;
  display: grid;
  place-items: center;
  border-radius: .6rem;
  color: var(--muted);
  background: color-mix(in srgb,var(--ink) 6%,transparent);
}

.pb-07__glyph svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-07__rowMeta {
  display: grid;
  gap: .12rem;
  min-inline-size: 0;
}

.pb-07__name {
  font-size: .88rem;
  font-weight: 550;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.pb-07__row[data-state="done"] .pb-07__fill {
  background: var(--ok);
}

.pb-07__row[data-state="done"] .pb-07__glyph {
  color: var(--ok);
  background: color-mix(in srgb,var(--ok) 14%,transparent);
}

.pb-07__row[data-state="paused"] .pb-07__fill {
  background: color-mix(in srgb,var(--ink) 32%,transparent);
}

.pb-07__row[data-state="paused"] .pb-07__name,
.pb-07__row[data-state="paused"] .pb-07__sub {
  color: var(--muted);
}

.pb-07__pause {
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  border-radius: .7rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 6%,transparent);
  color: var(--ink);
  cursor: pointer;
  transition: background .18s,transform .18s;
}

.pb-07__pause:hover:not([disabled]) {
  transform: translateY(-1px);
  background: color-mix(in srgb,var(--ink) 13%,transparent);
}

.pb-07__pause:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-07__pause[disabled] {
  cursor: default;
  color: var(--ok);
  border-color: color-mix(in srgb,var(--ok) 34%,transparent);
  background: color-mix(in srgb,var(--ok) 12%,transparent);
}

.pb-07__pause svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  grid-area: 1/1;
  display: none;
}

.pb-07__row[data-state="active"] .pb-07__pauseIcon {
  display: block;
}

.pb-07__row[data-state="paused"] .pb-07__playIcon {
  display: block;
}

.pb-07__row[data-state="done"] .pb-07__doneIcon {
  display: block;
}

.pb-07__foot {
  display: flex;
  flex-wrap: wrap;
  gap: .8rem;
  align-items: center;
  justify-content: space-between;
  padding-block-start: .3rem;
  border-block-start: 1px solid var(--line);
}

.pb-07__note {
  margin: 0;
  font-size: .72rem;
  color: var(--muted);
}

.pb-07__btn {
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
  font-size: .85rem;
  font-weight: 550;
  cursor: pointer;
  transition: transform .18s,background .18s;
}

.pb-07__btn svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.pb-07__btn:hover {
  transform: translateY(-1px);
  background: color-mix(in srgb,var(--ink) 12%,transparent);
}

.pb-07__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-07__live {
  margin: 0;
  min-block-size: 1.1rem;
  font-size: .78rem;
  color: var(--ok);
}

.pb-07[data-theme="light"] {
  --bg: #f4f6fa;
  --card: #ffffff;
  --card2: #f8fafc;
  --ink: #0a1020;
  --muted: rgba(10,16,32,.6);
  --line: rgba(10,16,32,.1);
  --track: rgba(10,16,32,.07);
  --accent: #0284c7;
  --accent-2: #4f46e5;
  --ok: #059669;
}

.pb-07[data-theme="light"] .pb-07__theme {
  background: rgba(10,16,32,.05);
}

@media (prefers-color-scheme: light) {
  .pb-07:not([data-theme="dark"]) {
    --bg: #f4f6fa;
    --card: #ffffff;
    --card2: #f8fafc;
    --ink: #0a1020;
    --muted: rgba(10,16,32,.6);
    --line: rgba(10,16,32,.1);
    --track: rgba(10,16,32,.07);
    --accent: #0284c7;
    --accent-2: #4f46e5;
    --ok: #059669;
  }

  .pb-07:not([data-theme="dark"]) .pb-07__theme {
    background: rgba(10,16,32,.05);
  }

  .pb-07:not([data-theme="dark"]) .pb-07__sun {
    display: block;
  }

  .pb-07:not([data-theme="dark"]) .pb-07__moon {
    display: none;
  }

  .pb-07[data-theme="dark"] .pb-07__sun {
    display: none;
  }

  .pb-07[data-theme="dark"] .pb-07__moon {
    display: block;
  }
}

@media (max-width: 40rem) {
  .pb-07__row {
    grid-template-columns: auto minmax(0,1fr) auto;
    row-gap: .5rem;
  }

  .pb-07__row .pb-07__bar {
    grid-column: 1 / -1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-07 *,
    .pb-07 *::before,
    .pb-07 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .pb-07__card,
    .pb-07__bar,
    .pb-07__btn,
    .pb-07__pause,
    .pb-07__theme,
    .pb-07__glyph {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .pb-07__fill {
    background: Highlight;
  }
}
```

## JavaScript
```js
const pb07 = document.querySelector('.pb-07');
if (pb07) {
  const FILES = [{ total: 12.8, rate: 0.42 }, { total: 42.6, rate: 0.95 }, { total: 88.2, rate: 1.7 }, { total: 42.8, rate: 1.1 }];
  const rows = [...pb07.querySelectorAll('.pb-07__row')];
  const agg = pb07.querySelector('#pb-07-agg'), live = pb07.querySelector('#pb-07-live');
  const mb = (n) => n.toFixed(1) + ' MB';
  const state = FILES.map((f, i) => ({ ...f, loaded: i === 3 ? f.total : f.total * [0.24, 0.44, 0.46][i] }));
  const paint = () => {
    let sum = 0, all = 0, done = 0;
    state.forEach((f, i) => {
      const row = rows[i], bar = row.querySelector('.pb-07__bar'), pct = Math.round(f.loaded / f.total * 100);
      if (pct >= 100 && row.dataset.state !== 'done') { row.dataset.state = 'done'; row.querySelector('.pb-07__pause').disabled = true; row.querySelector('.pb-07__speed').textContent = 'done'; live.textContent = row.querySelector('.pb-07__name').textContent + ' finished.'; }
      bar.style.setProperty('--value', pct); bar.setAttribute('aria-valuenow', pct);
      bar.setAttribute('aria-valuetext', mb(f.loaded) + ' of ' + mb(f.total));
      row.querySelector('.pb-07__loaded').textContent = mb(f.loaded);
      sum += f.loaded; all += f.total; done += pct >= 100 ? 1 : 0;
    });
    const o = Math.round(sum / all * 100);
    agg.style.setProperty('--value', o); agg.setAttribute('aria-valuenow', o);
    agg.setAttribute('aria-valuetext', o + ' percent of ' + mb(all) + ' downloaded');
    pb07.querySelector('#pb-07-total').textContent = o + '%';
    pb07.querySelector('#pb-07-count').innerHTML = done + ' of 4 complete \u00b7 ' + mb(all) + ' total';
    if (done === 4) live.textContent = 'All 4 files downloaded, ' + mb(all) + ' total.';
  };
  setInterval(() => {
    state.forEach((f, i) => { if (rows[i].dataset.state === 'active') f.loaded = Math.min(f.total, f.loaded + f.rate); });
    paint();
  }, 220);
  rows.forEach((row) => row.querySelector('.pb-07__pause').addEventListener('click', (e) => {
    const paused = row.dataset.state === 'active';
    row.dataset.state = paused ? 'paused' : 'active';
    e.currentTarget.setAttribute('aria-pressed', String(paused));
    const name = row.querySelector('.pb-07__name').textContent;
    e.currentTarget.setAttribute('aria-label', (paused ? 'Resume ' : 'Pause ') + name);
    row.querySelector('.pb-07__speed').textContent = paused ? 'paused' : ['1.4 MB/s', '3.2 MB/s', '5.8 MB/s', '1.1 MB/s'][Number(row.dataset.i)];
  }));
  pb07.querySelector('#pb-07-restart').addEventListener('click', () => {
    state.forEach((f, i) => { f.loaded = 0; rows[i].dataset.state = 'active'; rows[i].querySelector('.pb-07__pause').disabled = false; rows[i].querySelector('.pb-07__pause').setAttribute('aria-pressed', 'false'); rows[i].querySelector('.pb-07__speed').textContent = ['1.4 MB/s', '3.2 MB/s', '5.8 MB/s', '1.1 MB/s'][i]; });
    live.textContent = ''; paint();
  });
  pb07.querySelector('.pb-07__theme').addEventListener('click', (e) => {
    const light = pb07.dataset.theme !== 'light';
    pb07.dataset.theme = light ? 'light' : 'dark';
    e.currentTarget.setAttribute('aria-pressed', String(!light));
  });
  paint();
}
```
