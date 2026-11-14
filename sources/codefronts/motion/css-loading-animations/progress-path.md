---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/progress-path/"
title: "Multi-Step Progress Path Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "A four-stage progress path for any long-running, multi-phase job — mortgage underwriting, KYC, onboarding, a build pipeline."
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Step Progress Path Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/progress-path/

A four-stage progress path for any long-running, multi-phase job — mortgage underwriting, KYC, onboarding, a build pipeline. The connector fills, the active node pulses, completed nodes stroke a tick, and every visual state derives from one data-step attribute on the root, which is the cleanest state pattern in CSS.
## HTML
```html
<div class="la-16" data-state="loading" data-step="1">
  <div class="la-16__chrome">
    <button class="la-16__btn la-16__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-16__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-16__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-16__btn la-16__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <section class="la-16__card" role="status" aria-live="polite">
    <header class="la-16__head">
      <p class="la-16__title">Mortgage application</p>
      <p class="la-16__phase" id="la-16-phase">Verifying documents…</p>
    </header>

    <div class="la-16__path">
      <span class="la-16__rail" aria-hidden="true"><span class="la-16__fill"></span></span>
      <ol class="la-16__list">
        <li class="la-16__node"><span class="la-16__dot" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="m5.5 12.6 4.3 4.3L18.5 7.6"/></svg></span><span class="la-16__name">Applied</span></li>
        <li class="la-16__node"><span class="la-16__dot" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="m5.5 12.6 4.3 4.3L18.5 7.6"/></svg></span><span class="la-16__name">Documents</span></li>
        <li class="la-16__node"><span class="la-16__dot" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="m5.5 12.6 4.3 4.3L18.5 7.6"/></svg></span><span class="la-16__name">Underwriting</span></li>
        <li class="la-16__node"><span class="la-16__dot" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="m5.5 12.6 4.3 4.3L18.5 7.6"/></svg></span><span class="la-16__name">Approved</span></li>
      </ol>
    </div>

    <div class="la-16__meter" role="progressbar" aria-valuemin="0" aria-valuemax="4" aria-valuenow="2" aria-valuetext="Step 2 of 4, documents">
      <span class="la-16__ref">Ref MTG-77140 <span aria-hidden="true">·</span> Sam Rivera</span>
    </div>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

@property --la-16-p {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 0%;
}

.la-16 {
  --bg: #f4f5f9;
  --surface: #ffffff;
  --ink: #0c111b;
  --muted: #616c80;
  --line: #e3e7f0;
  --track: #e7ebf3;
  --acc: #4f46e5;
  --ok: #0f9d63;
  --ring: #4f46e5;
  --shadow: rgba(12,17,27,.16);
  --phase-dur: 2.2s;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(100% 60% at 50% -10%, color-mix(in oklab,var(--acc) 14%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-16,
.la-16 *,
.la-16 *::before,
.la-16 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-16 {
    --acc: oklch(52% .22 280);
    --ok: oklch(62% .15 158);
  }
}

.la-16__card {
  position: relative;
  inline-size: min(27rem,100%);
  padding: 1.6rem 1.5rem 1.3rem;
  display: grid;
  gap: 1.4rem;
  border-radius: 1.5rem;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 1px 0 #fff inset, 0 36px 64px -40px var(--shadow);
}

.la-16__head {
  display: grid;
  gap: .2rem;
}

.la-16__title {
  margin: 0;
  font-size: 1.15rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.la-16__phase {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--acc);
}

.la-16__path {
  position: relative;
  padding-block-start: .2rem;
}

.la-16__rail {
  position: absolute;
  inset-block-start: 1.05rem;
  inset-inline: 1.6rem;
  block-size: .25rem;
  border-radius: 999px;
  background: var(--track);
  overflow: hidden;
}

.la-16__fill {
  display: block;
  block-size: 100%;
  border-radius: inherit;
  inline-size: var(--la-16-p, 25%);
  background: linear-gradient(90deg, color-mix(in oklab,var(--acc) 60%,white), var(--acc));
  transition: inline-size .6s cubic-bezier(.16,1,.3,1);
}

.la-16__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 1fr;
  counter-reset: la-16-step;
  position: relative;
}

.la-16__node {
  counter-increment: la-16-step;
  display: grid;
  justify-items: center;
  gap: .45rem;
  text-align: center;
}

.la-16__dot {
  position: relative;
  inline-size: 2.1rem;
  block-size: 2.1rem;
  border-radius: 999px;
  display: grid;
  place-items: center;
  background: var(--surface);
  border: 2px solid var(--track);
  color: var(--muted);
  font-family: var(--mono);
  font-size: .75rem;
  font-variant-numeric: tabular-nums;
  transition: background .3s ease, border-color .3s ease, color .3s ease, scale .3s cubic-bezier(.16,1,.3,1);
}

.la-16__dot::before {
  content: counter(la-16-step);
}

.la-16__dot svg {
  position: absolute;
  inline-size: 1.05rem;
  block-size: 1.05rem;
  fill: none;
  stroke: #fff;
  stroke-width: 2.4;
  stroke-linecap: round;
  stroke-linejoin: round;
  opacity: 0;
  transition: opacity .25s ease;
}

.la-16__name {
  font-size: .74rem;
  color: var(--muted);
  letter-spacing: -.01em;
}

.la-16__node:has(+ .la-16__node) {
}

.la-16[data-step="1"] .la-16__node:nth-child(1) .la-16__dot,
.la-16[data-step="2"] .la-16__node:nth-child(-n+2) .la-16__dot,
.la-16[data-step="3"] .la-16__node:nth-child(-n+3) .la-16__dot,
.la-16[data-step="4"] .la-16__node .la-16__dot,
.la-16.is-ready .la-16__node .la-16__dot {
  background: var(--acc);
  border-color: var(--acc);
  color: transparent;
}

.la-16[data-step="1"] .la-16__node:nth-child(1) .la-16__dot svg,
.la-16[data-step="2"] .la-16__node:nth-child(-n+2) .la-16__dot svg,
.la-16[data-step="3"] .la-16__node:nth-child(-n+3) .la-16__dot svg,
.la-16[data-step="4"] .la-16__node .la-16__dot svg,
.la-16.is-ready .la-16__node .la-16__dot svg {
  opacity: 1;
}

.la-16[data-step="1"] .la-16__node:nth-child(1) .la-16__name,
.la-16[data-step="2"] .la-16__node:nth-child(-n+2) .la-16__name,
.la-16[data-step="3"] .la-16__node:nth-child(-n+3) .la-16__name,
.la-16[data-step="4"] .la-16__name {
  color: var(--ink);
}

.la-16[data-step="1"] .la-16__node:nth-child(2) .la-16__dot,
.la-16[data-step="2"] .la-16__node:nth-child(3) .la-16__dot,
.la-16[data-step="3"] .la-16__node:nth-child(4) .la-16__dot {
  border-color: var(--acc);
  color: var(--acc);
  scale: 1.08;
}

.la-16[data-step="1"] .la-16__node:nth-child(2) .la-16__dot::after,
.la-16[data-step="2"] .la-16__node:nth-child(3) .la-16__dot::after,
.la-16[data-step="3"] .la-16__node:nth-child(4) .la-16__dot::after {
  content: "";
  position: absolute;
  inset: -.35rem;
  border-radius: 999px;
  pointer-events: none;
  border: 2px solid color-mix(in oklab,var(--acc) 55%,transparent);
  background: transparent;
  animation: la-16-pulse 1.8s ease-out infinite;
}

@keyframes la-16-pulse {
  0% {
    scale: .72;
    opacity: .9;
  }

  100% {
    scale: 1.35;
    opacity: 0;
  }
}

.la-16__meter {
  display: flex;
  justify-content: center;
}

.la-16__ref {
  font-family: var(--mono);
  font-size: .66rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.la-16.is-ready .la-16__phase {
  color: var(--ok);
}

.la-16.is-ready .la-16__fill {
  inline-size: 100%;
  background: var(--ok);
}

.la-16.is-ready .la-16__node .la-16__dot {
  background: var(--ok);
  border-color: var(--ok);
}

.la-16.is-ready .la-16__name {
  color: var(--ink);
}

.la-16__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-16__btn {
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

.la-16__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-16__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-16__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-16__sun {
  display: none;
}

.la-16__theme[aria-pressed="true"] .la-16__sun {
  display: block;
}

.la-16__theme[aria-pressed="true"] .la-16__moon {
  display: none;
}

.la-16__done[aria-pressed="true"] {
  background: var(--ok);
  border-color: transparent;
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .la-16:not([data-theme="light"]) {
    --bg: #080a11;
    --surface: #111621;
    --ink: #eef1f8;
    --muted: #909cb0;
    --line: #212a38;
    --track: #232c3b;
    --acc: #8b83ff;
    --ok: #31d68f;
    --ring: #8b83ff;
    --shadow: rgba(0,0,0,.7);
  }

  .la-16:not([data-theme="light"]) .la-16__card {
    box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
  }

  .la-16:not([data-theme="light"]) .la-16__dot svg {
    stroke: #0b1018;
  }

  .la-16:not([data-theme="light"]) .la-16__done[aria-pressed="true"] {
    color: #04231a;
  }
}

.la-16[data-theme="dark"] {
  --bg: #080a11;
  --surface: #111621;
  --ink: #eef1f8;
  --muted: #909cb0;
  --line: #212a38;
  --track: #232c3b;
  --acc: #8b83ff;
  --ok: #31d68f;
  --ring: #8b83ff;
  --shadow: rgba(0,0,0,.7);
}

.la-16[data-theme="dark"] .la-16__card {
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 40px 70px -40px #000;
}

.la-16[data-theme="dark"] .la-16__dot svg {
  stroke: #0b1018;
}

.la-16[data-theme="dark"] .la-16__done[aria-pressed="true"] {
  color: #04231a;
}

@media (prefers-reduced-motion: reduce) {
  .la-16 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .la-16__card {
    border: 1px solid CanvasText;
  }

  .la-16__fill {
    background: Highlight;
  }

  .la-16__dot {
    border: 2px solid CanvasText;
  }

  .la-16__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-16');
  if (!root) return;
  const theme = root.querySelector('.la-16__theme');
  const done = root.querySelector('.la-16__done');
  const phase = root.querySelector('#la-16-phase');
  const fill = root.querySelector('.la-16__fill');
  const bar = root.querySelector('[role="progressbar"]');
  const TEXT = ['Application received…', 'Verifying documents…', 'Underwriting in review…', 'Finalising approval…'];
  let step = 1;
  const paint = () => {
    root.dataset.step = step;
    fill.style.setProperty('--la-16-p', (step / 4 * 100) + '%');
    phase.textContent = TEXT[step - 1];
    bar.setAttribute('aria-valuenow', step); bar.setAttribute('aria-valuetext', 'Step ' + step + ' of 4');
  };
  const loop = setInterval(() => { if (!root.classList.contains('is-ready')) { step = step % 4 + 1; paint(); } }, 2200);
  const dark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => { theme.setAttribute('aria-pressed', String(dark())); theme.setAttribute('aria-label', dark() ? 'Switch to light theme' : 'Switch to dark theme'); };
  theme.addEventListener('click', () => { root.dataset.theme = dark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  done.addEventListener('click', () => {
    const ready = root.classList.toggle('is-ready');
    root.dataset.state = ready ? 'ready' : 'loading';
    done.setAttribute('aria-pressed', String(ready)); done.setAttribute('aria-label', ready ? 'Return to loading state' : 'Show completed state');
    if (ready) { clearInterval(loop); step = 4; paint(); phase.textContent = 'Approved — offer sent'; }
  });
  paint(); sync();
})();
```
