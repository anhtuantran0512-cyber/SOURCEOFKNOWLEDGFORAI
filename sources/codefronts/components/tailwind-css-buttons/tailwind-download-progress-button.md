---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-download-progress-button/"
title: "Tailwind Download Progress Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A download button that becomes its own progress bar: the fill sweeps behind the label, a conic ring mirrors it on the icon, and the percentage is a…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Download Progress Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-download-progress-button/

A download button that becomes its own progress bar: the fill sweeps behind the label, a conic ring mirrors it on the icon, and the percentage is a registered custom property so the digits interpolate instead of stepping. One variable drives three visuals — which is exactly the case where Tailwind's job is to expose the variable, not to own it.
## HTML
```html
<div class="tb-10 w-full min-h-svh grid place-items-center font-tb10-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" data-state="idle" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" aria-label="Download the 2026 report" class="tb-10__btn group relative overflow-hidden isolate cursor-pointer w-[min(100%,20rem)] min-h-14 px-6 border border-tb10-line rounded-[0.9rem] text-[0.9375rem] font-semibold text-left text-tb10-ink bg-tb10-surface transition-[border-color,translate] duration-300 ease-tb10-out hover:-translate-y-0.5 hover:border-tb10-accent-line focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tb10-accent data-[state=busy]:cursor-progress data-[state=done]:border-tb10-ok motion-reduce:transition-none">
    <span aria-hidden="true" class="absolute inset-0 -z-10 origin-left scale-x-[calc(var(--tb-10-p)/100%)] bg-[linear-gradient(90deg,var(--color-tb10-fill-a),var(--color-tb10-fill-b))] transition-[scale,background] duration-[400ms] ease-tb10-out group-data-[state=done]:bg-[linear-gradient(90deg,var(--color-tb10-ok-a),var(--color-tb10-ok-b))] motion-reduce:transition-none"></span>
    <span class="grid grid-flow-col items-center gap-3 [grid-template-columns:auto_1fr_auto]">
      <span aria-hidden="true" class="relative grid place-items-center size-6 text-tb10-accent group-data-[state=done]:text-tb10-ok">
        <span class="absolute inset-0 rounded-full opacity-0 transition-opacity duration-300 bg-[conic-gradient(currentColor_var(--tb-10-p),var(--color-tb10-ring-track)_0)] [mask-image:radial-gradient(farthest-side,transparent_calc(100%-3px),#000_calc(100%-3px))] group-data-[state=busy]:opacity-100"></span>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" class="tb-10__svg size-[1.15rem]">
          <path class="tb-10__arrow" d="M12 4v10m0 0 4-4m-4 4-4-4"/>
          <path class="tb-10__tray" d="M5 18.5h14"/>
          <path class="tb-10__tick" d="M6.5 12.5 10.5 16.5 17.5 8"/>
        </svg>
      </span>
      <span class="tb-10__label">Download report</span>
      <span aria-hidden="true" class="tb-10__pct text-[0.8125rem] font-bold tabular-nums text-tb10-accent opacity-0 transition-opacity duration-300 group-data-[state=busy]:opacity-100">0%</span>
    </span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@property --tb-10-p {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 0%;
}

@theme {
  --color-tb10-bg: #0b0f14;
  --color-tb10-bg: oklch(0.16 0.02 250);
  --color-tb10-surface: #151b23;
  --color-tb10-surface: oklch(0.24 0.02 250);
  --color-tb10-line: #26303b;
  --color-tb10-line: oklch(0.33 0.02 250);
  --color-tb10-ink: #e9eef5;
  --color-tb10-ink: oklch(0.94 0.008 250);
  --color-tb10-accent: #38bdf8;
  --color-tb10-accent: oklch(0.78 0.13 222);
  --color-tb10-accent-line: #2a7fa8;
  --color-tb10-accent-line: oklch(0.58 0.09 222);
  --color-tb10-ok: #34d399;
  --color-tb10-ok: oklch(0.78 0.14 165);
  --color-tb10-fill-a: #38bdf842;
  --color-tb10-fill-a: oklch(0.78 0.13 222 / 0.26);
  --color-tb10-fill-b: #38bdf86b;
  --color-tb10-fill-b: oklch(0.78 0.13 222 / 0.42);
  --color-tb10-ok-a: #34d39938;
  --color-tb10-ok-a: oklch(0.78 0.14 165 / 0.22);
  --color-tb10-ok-b: #34d39957;
  --color-tb10-ok-b: oklch(0.78 0.14 165 / 0.34);
  --color-tb10-ring-track: #38bdf82e;
  --color-tb10-ring-track: oklch(0.78 0.13 222 / 0.18);
  --font-tb10-sans: "Sora", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb10-out: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tb10-bob: tb-10-bob 1.1s ease-in-out infinite;
}

@keyframes tb-10-bob {
  50% {
    translate: 0 2px;
    opacity: 0.5;
  }
}

@keyframes tb-10-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.tb-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(50rem 30rem at 50% 0%, var(--color-tb10-ring-track), transparent 70%), var(--color-tb10-bg);
}

.tb-10__btn {
  --tb-10-p: 0%;
}
/* Safari ≤15.3 mask shim. */

.tb-10 [class*="mask-image"] {
  -webkit-mask-image: radial-gradient(farthest-side, transparent calc(100% - 3px), #000 calc(100% - 3px));
}
/* SVG path state: geometry and per-path visibility. No utility form. */

.tb-10__tick {
  stroke-dasharray: 24;
  stroke-dashoffset: 24;
}

.tb-10__btn[data-state="busy"] .tb-10__arrow {
  animation: var(--animate-tb10-bob);
}

.tb-10__btn[data-state="done"] :is(.tb-10__arrow, .tb-10__tray) {
  opacity: 0;
}

.tb-10__btn[data-state="done"] .tb-10__tick {
  animation: tb-10-draw 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
/* The animated counter: Chrome/Safari only, with the JS-written text as fallback. */

@supports (counter-reset: x calc(1 / 1)) {
  .tb-10__pct {
    counter-reset: tb-10-n calc(var(--tb-10-p) / 1%);
    font-size: 0;
  }

  .tb-10__pct::after {
    content: counter(tb-10-n) "%";
    font-size: 0.8125rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tb-10__btn[data-state="busy"] .tb-10__arrow {
    animation: none;
  }

  .tb-10__tick {
    stroke-dashoffset: 0;
    animation: none;
  }
}

@media (prefers-color-scheme: light) {
  .tb-10:not([data-theme="dark"]) {
    --color-tb10-bg: oklch(0.95 0.008 250);
    --color-tb10-surface: #ffffff;
    --color-tb10-line: oklch(0.88 0.012 250);
    --color-tb10-ink: oklch(0.2 0.02 250);
    --color-tb10-accent: oklch(0.55 0.13 235);
    --color-tb10-ok: oklch(0.56 0.13 162);
  }
}

.tb-10[data-theme="light"] {
  --color-tb10-bg: oklch(0.95 0.008 250);
  --color-tb10-surface: #ffffff;
  --color-tb10-line: oklch(0.88 0.012 250);
  --color-tb10-ink: oklch(0.2 0.02 250);
  --color-tb10-accent: oklch(0.55 0.13 235);
}

@media (forced-colors: active) {
  .tb-10__btn {
    border: 1px solid ButtonText;
    color: ButtonText;
    background: ButtonFace;
  }

  .tb-10__btn > span:first-child {
    background: Highlight;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.tb-10__btn');
  const pct = document.querySelector('.tb-10__pct');
  const label = document.querySelector('.tb-10__label');
  if (!btn) return;
  let timer, p = 0;
  btn.addEventListener('click', () => {
    if (btn.dataset.state !== 'idle') return;
    btn.dataset.state = 'busy';
    p = 0;
    // Swap this fake ticker for your XHR/fetch progress events.
    const step = () => {
      p = Math.min(100, p + Math.random() * 7 + 2);
      btn.style.setProperty('--tb-10-p', p + '%');
      btn.setAttribute('aria-valuenow', String(Math.round(p)));
      pct.textContent = Math.round(p) + '%';
      if (p < 100) { timer = setTimeout(step, 140); }
      else { btn.dataset.state = 'done'; label.textContent = 'Report downloaded'; }
    };
    step();
  });
  window.addEventListener('pagehide', () => clearTimeout(timer));
})();
```
