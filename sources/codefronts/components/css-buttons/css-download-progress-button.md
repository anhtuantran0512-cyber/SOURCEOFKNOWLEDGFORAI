---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-download-progress-button/"
title: "CSS Download Progress Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A download button that becomes its own progress bar: the fill sweeps left-to-right behind the label, a conic ring mirrors it on the icon, and the percentage…"
has_js: "true"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Download Progress Button
Source: https://codefronts.com/components/css-buttons/css-download-progress-button/

A download button that becomes its own progress bar: the fill sweeps left-to-right behind the label, a conic ring mirrors it on the icon, and the percentage is a registered custom property so the digits interpolate smoothly instead of stepping. Ends on a drawn tick and a real role="progressbar" so the value is exposed, not implied.
## HTML
```html
<div class="cb-10">
  <div class="cb-10__stage">
    <button class="cb-10__btn" type="button" data-state="idle" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" aria-label="Download the 2026 report">
      <span class="cb-10__fill" aria-hidden="true"></span>
      <span class="cb-10__body">
        <span class="cb-10__ico" aria-hidden="true">
          <span class="cb-10__ring"></span>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path class="cb-10__arrow" d="M12 4v10m0 0 4-4m-4 4-4-4"/><path class="cb-10__tray" d="M5 18.5h14"/><path class="cb-10__tick" d="M6.5 12.5 10.5 16.5 17.5 8"/></svg>
        </span>
        <span class="cb-10__label">Download report</span>
        <span class="cb-10__pct" aria-hidden="true">0%</span>
      </span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&display=swap');

@property --cb-10-p {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 0%;
}

.cb-10 {
  --bg: #0b0f14;
  --surface: #151b23;
  --line: #26303b;
  --ink: #e9eef5;
  --accent: #38bdf8;
  --ok: #34d399;
  --radius: .9rem;
  --sans: "Sora",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(50rem 30rem at 50% 0%, color-mix(in oklab,var(--accent) 10%,transparent), transparent 70%), var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-10 {
    --surface: oklch(24% .02 250);
    --accent: oklch(78% .13 222);
    --ok: oklch(78% .14 165);
  }
}

@media (prefers-color-scheme: light) {
  .cb-10:not([data-theme="dark"]) {
    --bg: #eef2f7;
    --surface: #ffffff;
    --line: #d8e0ea;
    --ink: #0d1520;
    --accent: #0284c7;
    --ok: #059669;
  }
}

.cb-10[data-theme="light"] {
  --bg: #eef2f7;
  --surface: #ffffff;
  --line: #d8e0ea;
  --ink: #0d1520;
  --accent: #0284c7;
  --ok: #059669;
}

.cb-10,
.cb-10 *,
.cb-10 *::before,
.cb-10 *::after {
  box-sizing: border-box;
}

.cb-10__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-10__btn {
  --cb-10-p: 0%;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  cursor: pointer;
  width: min(100%,20rem);
  min-height: 3.5rem;
  padding: 0 1.4rem;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  font: inherit;
  font-size: .9375rem;
  font-weight: 600;
  color: var(--ink);
  text-align: left;
  background: var(--surface);
  transition: border-color .3s ease, translate .2s cubic-bezier(.16,1,.3,1);
}

.cb-10__fill {
  position: absolute;
  inset: 0;
  z-index: -1;
  transform-origin: left center;
  background: linear-gradient(90deg, color-mix(in oklab,var(--accent) 26%,transparent), color-mix(in oklab,var(--accent) 42%,transparent));
  scale: 0 1;
  transition: scale .4s cubic-bezier(.16,1,.3,1), background .4s ease;
}

@supports (background: conic-gradient(red var(--cb-10-p), transparent 0)) {
  .cb-10__fill {
    scale: calc(var(--cb-10-p) / 100%) 1;
  }
}

.cb-10__body {
  display: grid;
  grid-auto-flow: column;
  align-items: center;
  gap: .75rem;
  grid-template-columns: auto 1fr auto;
}

.cb-10__ico {
  position: relative;
  width: 1.55rem;
  height: 1.55rem;
  display: grid;
  place-items: center;
  color: var(--accent);
}

.cb-10__ico svg {
  width: 1.15rem;
  height: 1.15rem;
}

.cb-10__ring {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(currentColor var(--cb-10-p), color-mix(in oklab,currentColor 18%,transparent) 0);
  -webkit-mask: radial-gradient(farthest-side,transparent calc(100% - 3px),#000 calc(100% - 3px));
  mask: radial-gradient(farthest-side,transparent calc(100% - 3px),#000 calc(100% - 3px));
  opacity: 0;
  transition: opacity .3s ease;
}

.cb-10__pct {
  font-size: .8125rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  opacity: 0;
  color: var(--accent);
  transition: opacity .3s ease;
}

@supports (counter-reset: x calc(1 / 1)) {
  .cb-10__pct {
    counter-reset: cb-10-n calc(var(--cb-10-p) / 1%);
    font-size: 0;
  }

  .cb-10__pct::after {
    content: counter(cb-10-n) "%";
    font-size: .8125rem;
  }
}

.cb-10__tick {
  stroke-dasharray: 24;
  stroke-dashoffset: 24;
}

.cb-10__btn[data-state="busy"] {
  cursor: progress;
}

.cb-10__btn[data-state="busy"] .cb-10__ring,
.cb-10__btn[data-state="busy"] .cb-10__pct {
  opacity: 1;
}

.cb-10__btn[data-state="busy"] .cb-10__arrow {
  animation: cb-10-bob 1.1s ease-in-out infinite;
}

@keyframes cb-10-bob {
  50% {
    translate: 0 2px;
    opacity: .5;
  }
}

.cb-10__btn[data-state="done"] {
  border-color: var(--ok);
}

.cb-10__btn[data-state="done"] .cb-10__ico {
  color: var(--ok);
}

.cb-10__btn[data-state="done"] .cb-10__fill {
  background: linear-gradient(90deg,color-mix(in oklab,var(--ok) 22%,transparent),color-mix(in oklab,var(--ok) 34%,transparent));
}

.cb-10__btn[data-state="done"] :is(.cb-10__arrow,.cb-10__tray) {
  opacity: 0;
}

.cb-10__btn[data-state="done"] .cb-10__tick {
  animation: cb-10-draw .5s cubic-bezier(.16,1,.3,1) forwards;
}

@keyframes cb-10-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.cb-10__btn:hover {
  translate: 0 -2px;
  border-color: color-mix(in oklab,var(--accent) 60%,var(--line));
}

.cb-10__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .cb-10__btn,
    .cb-10__fill,
    .cb-10__ring,
    .cb-10__pct {
    transition: none;
  }

  .cb-10__btn[data-state="busy"] .cb-10__arrow {
    animation: none;
  }

  .cb-10__tick {
    stroke-dashoffset: 0;
    animation: none;
  }
}

@media (forced-colors: active) {
  .cb-10__fill {
    background: Highlight;
  }

  .cb-10__btn {
    border: 1px solid ButtonText;
    color: ButtonText;
    background: ButtonFace;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.cb-10__btn');
  const pct = document.querySelector('.cb-10__pct');
  if (!btn) return;
  let raf, p = 0;
  btn.addEventListener('click', () => {
    if (btn.dataset.state !== 'idle') return;
    btn.dataset.state = 'busy';
    p = 0;
    // Swap this fake ticker for your XHR/fetch progress events.
    const step = () => {
      p = Math.min(100, p + Math.random() * 7 + 2);
      btn.style.setProperty('--cb-10-p', p + '%');
      btn.setAttribute('aria-valuenow', String(Math.round(p)));
      pct.textContent = Math.round(p) + '%';
      if (p < 100) { raf = setTimeout(step, 140); }
      else { btn.dataset.state = 'done'; btn.querySelector('.cb-10__label').textContent = 'Report downloaded'; }
    };
    step();
  });
  window.addEventListener('pagehide', () => clearTimeout(raf));
})();
```
