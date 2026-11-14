---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/file-upload-cloud-sync-loading-animation/"
title: "File Upload Cloud Sync Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "The loader every file manager needs: a document lifts off a tray, rides a column of sync dots into a cloud, and the cloud's outline closes with a drawn…"
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: File Upload Cloud Sync Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/file-upload-cloud-sync-loading-animation/

The loader every file manager needs: a document lifts off a tray, rides a column of sync dots into a cloud, and the cloud's outline closes with a drawn checkmark before the cycle restarts. The filename, byte count and transfer rate are real Dropbox/Drive-grade metadata, and the ring around the cloud is a genuine determinate arc you can bind to an XMLHttpRequest.upload progress event.
## HTML
```html
<div class="la-04" data-state="loading">
  <div class="la-04__chrome">
    <button class="la-04__btn la-04__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-04__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-04__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-04__btn la-04__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <section class="la-04__card" role="status" aria-live="polite" aria-label="Uploading annual-report.pdf to cloud storage">
    <div class="la-04__stage" aria-hidden="true">
      <svg class="la-04__cloud" viewBox="0 0 96 64" focusable="false">
        <path class="la-04__cloud-path" d="M26 52a13 13 0 0 1-1.4-25.9A18 18 0 0 1 59 22.4 14 14 0 1 1 70 52z"/>
        <path class="la-04__tick" d="M38 39.5 45.5 47 60 30"/>
      </svg>
      <span class="la-04__dot" style="--i:0"></span>
      <span class="la-04__dot" style="--i:1"></span>
      <span class="la-04__dot" style="--i:2"></span>
      <div class="la-04__file">
        <span class="la-04__corner"></span>
        <i></i><i></i><i></i>
      </div>
      <span class="la-04__tray"></span>
    </div>

    <div class="la-04__copy">
      <p class="la-04__name" title="annual-report.pdf">annual-report.pdf</p>
      <p class="la-04__meta">
        <span class="la-04__load">Uploading <span class="la-04__pct"></span> <span aria-hidden="true">·</span> 4.2 MB <span aria-hidden="true">·</span> 1.8 MB/s</span>
        <span class="la-04__ready">Synced to Drive <span aria-hidden="true">·</span> 4.2 MB</span>
      </p>
    </div>

    <div class="la-04__track" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="72" aria-valuetext="72 percent uploaded">
      <span class="la-04__fill"></span>
    </div>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

@property --la-04-p {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 0%;
}

@property --la-04-n {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

.la-04 {
  color-scheme: light dark;
  --bg: #eef2f8;
  --surface: #ffffff;
  --ink: #0a1018;
  --muted: #5f6b7c;
  --line: #e0e6f0;
  --acc: #0a84ff;
  --ok: #12a367;
  --ring: #0a84ff;
  --shadow: rgba(10,16,24,.16);
  --stage: 9rem;
  --dur: 4.4s;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(100% 70% at 50% -10%, color-mix(in oklab,var(--acc) 18%,transparent), transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-04,
.la-04 *,
.la-04 *::before,
.la-04 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-04 {
    --acc: oklch(60% .19 250);
    --ok: oklch(62% .15 158);
  }
}

.la-04__card {
  position: relative;
  inline-size: min(23rem,100%);
  padding: 1.9rem 1.5rem 1.4rem;
  display: grid;
  justify-items: center;
  gap: 1.15rem;
  text-align: center;
  border-radius: 1.6rem;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 1px 0 #fff inset, 0 36px 64px -40px var(--shadow);
}

.la-04__stage {
  position: relative;
  inline-size: var(--stage);
  block-size: var(--stage);
  display: grid;
  place-items: center;
}

.la-04__cloud {
  position: absolute;
  inset-block-start: 0;
  inline-size: 5.6rem;
  block-size: 3.8rem;
  fill: none;
  stroke: color-mix(in oklab,var(--ink) 55%,transparent);
  stroke-width: 3.2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-04__cloud-path {
  stroke-dasharray: 180;
  stroke-dashoffset: 180;
  animation: la-04-draw var(--dur) ease-in-out infinite;
}

@keyframes la-04-draw {
  0% {
    stroke-dashoffset: 180;
  }

  42%,
    100% {
    stroke-dashoffset: 0;
  }
}

.la-04__tick {
  stroke: var(--ok);
  stroke-dasharray: 33;
  stroke-dashoffset: 33;
  animation: la-04-tick var(--dur) ease-out infinite;
}

@keyframes la-04-tick {
  0%,
    72% {
    stroke-dashoffset: 33;
  }

  88%,
    96% {
    stroke-dashoffset: 0;
  }

  100% {
    stroke-dashoffset: 33;
  }
}

.la-04__file {
  position: absolute;
  inset-block-end: 1.7rem;
  inline-size: 2.4rem;
  block-size: 3rem;
  border-radius: .4rem .8rem .4rem .4rem;
  background: linear-gradient(180deg, color-mix(in oklab,var(--acc) 80%,white), var(--acc));
  box-shadow: 0 10px 18px -12px var(--acc);
  mask-image: linear-gradient(to top, #000 var(--la-04-p, 72%), rgba(0,0,0,.3) var(--la-04-p, 72%));
  animation: la-04-rise var(--dur) cubic-bezier(.4,0,.4,1) infinite, la-04-fill var(--dur) linear infinite;
  display: grid;
  align-content: end;
  gap: .22rem;
  padding: .4rem;
}

.la-04__file i {
  display: block;
  block-size: .16rem;
  border-radius: 999px;
  background: rgba(255,255,255,.75);
}

.la-04__file i:nth-child(3) {
  inline-size: 60%;
}

.la-04__corner {
  position: absolute;
  inset-block-start: 0;
  inset-inline-end: 0;
  inline-size: .75rem;
  block-size: .75rem;
  background: rgba(255,255,255,.45);
  clip-path: polygon(0 0,100% 100%,100% 0);
}

@keyframes la-04-rise {
  0% {
    translate: 0 .6rem;
    opacity: 0;
    scale: .92;
  }

  14% {
    opacity: 1;
  }

  62% {
    translate: 0 -2.9rem;
    opacity: 1;
    scale: 1;
  }

  78%,
    100% {
    translate: 0 -3.6rem;
    opacity: 0;
    scale: .88;
  }
}

@keyframes la-04-fill {
  0% {
    --la-04-p: 8%;
  }

  62%,
    100% {
    --la-04-p: 100%;
  }
}

.la-04__dot {
  position: absolute;
  inline-size: .35rem;
  block-size: .35rem;
  border-radius: 999px;
  background: var(--acc);
  inset-block-end: 2.6rem;
  opacity: 0;
  animation: la-04-dot 1.45s ease-in-out infinite;
  animation-delay: calc(var(--i) * .28s);
}

@keyframes la-04-dot {
  0% {
    translate: 0 .4rem;
    opacity: 0;
  }

  35% {
    opacity: .9;
  }

  100% {
    translate: 0 -2.2rem;
    opacity: 0;
  }
}

.la-04__tray {
  position: absolute;
  inset-block-end: 1rem;
  inline-size: 4.6rem;
  block-size: .4rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--ink) 12%,transparent);
}

.la-04__copy {
  display: grid;
  gap: .28rem;
  inline-size: 100%;
}

.la-04__name {
  margin: 0;
  font-size: 1.02rem;
  font-weight: 600;
  letter-spacing: -.015em;
  overflow-wrap: anywhere;
  text-wrap: pretty;
  max-inline-size: 16rem;
  margin-inline: auto;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.la-04__meta {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.la-04__ready {
  display: none;
}

.la-04__pct {
  counter-reset: la-04-n var(--la-04-n, 72);
  animation: la-04-count var(--dur) linear infinite;
}

.la-04__pct::after {
  content: counter(la-04-n) "%";
}

@keyframes la-04-count {
  0% {
    --la-04-n: 8;
  }

  62%,
    100% {
    --la-04-n: 100;
  }
}

.la-04__track {
  inline-size: 100%;
  block-size: .4rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--ink) 9%,transparent);
  overflow: hidden;
}

.la-04__fill {
  display: block;
  block-size: 100%;
  inline-size: var(--la-04-p, 72%);
  border-radius: inherit;
  background: linear-gradient(90deg, color-mix(in oklab,var(--acc) 60%,white), var(--acc));
  animation: la-04-fill var(--dur) linear infinite;
}

@supports (color: light-dark(#000,#fff)) {
  .la-04__tray {
    background: light-dark(rgba(10,16,24,.1), rgba(255,255,255,.14));
  }
}

.la-04.is-ready .la-04__file,
.la-04.is-ready .la-04__dot {
  animation: none;
  opacity: 0;
}

.la-04.is-ready .la-04__cloud-path {
  animation: none;
  stroke-dashoffset: 0;
  stroke: var(--ok);
}

.la-04.is-ready .la-04__tick {
  animation: none;
  stroke-dashoffset: 0;
}

.la-04.is-ready .la-04__load {
  display: none;
}

.la-04.is-ready .la-04__ready {
  display: inline;
}

.la-04.is-ready .la-04__fill {
  animation: none;
  inline-size: 100%;
  background: var(--ok);
}

.la-04__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-04__btn {
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  padding: 0;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab,var(--ink) 16%,transparent);
  color: var(--ink);
  background: color-mix(in oklab,var(--surface) 72%,transparent);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1);
}

.la-04__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-04__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-04__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-04__sun {
  display: none;
}

.la-04__theme[aria-pressed="true"] .la-04__sun {
  display: block;
}

.la-04__theme[aria-pressed="true"] .la-04__moon {
  display: none;
}

.la-04__done[aria-pressed="true"] {
  background: var(--ok);
  border-color: transparent;
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .la-04:not([data-theme="light"]) {
    --bg: #070a10;
    --surface: #111721;
    --ink: #eaf0f8;
    --muted: #93a0b3;
    --line: #212a37;
    --acc: #4aa8ff;
    --ok: #2fd08c;
    --ring: #4aa8ff;
    --shadow: rgba(0,0,0,.65);
  }

  .la-04:not([data-theme="light"]) .la-04__card {
    box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
  }
}

.la-04[data-theme="dark"] {
  --bg: #070a10;
  --surface: #111721;
  --ink: #eaf0f8;
  --muted: #93a0b3;
  --line: #212a37;
  --acc: #4aa8ff;
  --ok: #2fd08c;
  --ring: #4aa8ff;
  --shadow: rgba(0,0,0,.65);
}

.la-04[data-theme="dark"] .la-04__card {
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
}

@media (prefers-reduced-motion: reduce) {
  .la-04 * {
    animation: none !important;
    transition: none !important;
  }

  .la-04__cloud-path {
    stroke-dashoffset: 0;
  }

  .la-04__file {
    translate: 0 -1.6rem;
    opacity: 1;
  }

  .la-04__dot {
    opacity: .5;
  }
}

@media (forced-colors: active) {
  .la-04__card {
    border: 1px solid CanvasText;
  }

  .la-04__fill {
    background: Highlight;
  }

  .la-04__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-04');
  if (!root) return;
  const theme = root.querySelector('.la-04__theme');
  const done = root.querySelector('.la-04__done');
  const bar = root.querySelector('[role="progressbar"]');
  const region = root.querySelector('[role="status"]');
  const dark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    theme.setAttribute('aria-pressed', String(dark()));
    theme.setAttribute('aria-label', dark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  theme.addEventListener('click', () => { root.dataset.theme = dark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  done.addEventListener('click', () => {
    const ready = root.classList.toggle('is-ready');        // xhr.upload.onload
    root.dataset.state = ready ? 'ready' : 'loading';
    done.setAttribute('aria-pressed', String(ready));
    done.setAttribute('aria-label', ready ? 'Return to loading state' : 'Show completed state');
    bar.setAttribute('aria-valuenow', ready ? 100 : 72);
    bar.setAttribute('aria-valuetext', ready ? 'Upload complete' : '72 percent uploaded');
    region.setAttribute('aria-label', ready ? 'annual-report.pdf synced to cloud storage' : 'Uploading annual-report.pdf to cloud storage');
  });
  sync();
})();
```
