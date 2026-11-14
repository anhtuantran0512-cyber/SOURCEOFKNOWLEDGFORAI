---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-press-and-hold-to-confirm-toggle-fingerprint/"
title: "Tailwind Press-and-Hold to Confirm Toggle (Fingerprint Scan)"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "A destructive-action guard shaped like a fingerprint sensor: press and hold 1.2s while a scan line sweeps and a ring fills. Release early and it disarms. The…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Press-and-Hold to Confirm Toggle (Fingerprint Scan)
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-press-and-hold-to-confirm-toggle-fingerprint/

A destructive-action guard shaped like a fingerprint sensor: press and hold 1.2s while a scan line sweeps and a ring fills. Release early and it disarms. The state lives on aria-checked, so the styling variant and the accessibility contract are literally the same attribute.
## HTML
```html
<section class="ttg-11 w-full min-h-svh grid place-items-center px-5 py-14 bg-ttg11-bg font-ttg11-sans" aria-label="Hold to confirm toggle">
  <div class="w-[min(340px,100%)] flex flex-col items-center gap-5 px-10 py-8 rounded-[22px] bg-ttg11-card border border-ttg11-edge">
    <div class="flex flex-col items-center gap-1 text-center">
      <b class="text-[16px] font-bold text-ttg11-ink">Delete production database</b>
      <span class="text-[12.5px] text-ttg11-mute">Hold the sensor for 1.2s to arm</span>
    </div>
    <button type="button" id="ttg-11-btn" role="switch" aria-checked="false" class="relative grid place-items-center w-26 h-26 rounded-full border-0 overflow-hidden cursor-pointer select-none [touch-action:none] bg-ttg11-sensor text-ttg11-idle transition-colors duration-300 aria-checked:text-ttg11-ok focus-visible:outline-3 focus-visible:outline-ttg11-scanline focus-visible:outline-offset-4 data-holding:[&_.ttg11-scan]:opacity-100 data-holding:[&_.ttg11-scan]:animate-ttg11-scan data-holding:[&_.ttg11-ring]:animate-ttg11-fill motion-reduce:data-holding:[&_.ttg11-scan]:animate-none">
      <svg viewBox="0 0 40 48" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" class="relative z-10 w-[46px] h-14 transition-[filter] duration-300 [.ttg11-btn[aria-checked=true]_&]:drop-shadow-[0_0_8px_currentColor]">
        <path d="M20 6c-8 0-13 6-13 13v6"/><path d="M20 12c-5 0-8 4-8 8v9"/><path d="M20 18c-2.5 0-4 2-4 4v12"/><path d="M20 25v14"/><path d="M25 21c.6 1 .9 2.2.9 3.5V37"/><path d="M29.5 17c1.6 2 2.5 4.5 2.5 7v9"/><path d="M27 9.5c3.7 2.3 6 6.3 6 10.5v3"/>
      </svg>
      <span aria-hidden="true" class="ttg11-scan absolute left-[18px] right-[18px] top-0 z-20 h-[3px] rounded-sm opacity-0 bg-ttg11-scanline shadow-[0_0_12px_var(--color-ttg11-scanline)]"></span>
      <span aria-hidden="true" class="ttg11-ring absolute inset-0 rounded-full [background:conic-gradient(var(--color-ttg11-ok)_var(--ttg11-p,0deg),transparent_0)] [mask:radial-gradient(circle,transparent_46px,#000_47px)]"></span>
    </button>
    <p id="ttg-11-state" aria-live="polite" class="min-h-[1.2em] text-[13px] font-semibold tracking-[0.08em] uppercase text-ttg11-mute">Locked</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --ttg11-p {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

@theme {
  --color-ttg11-bg: #0f1219;
  --color-ttg11-bg: oklch(0.18 0.012 265);
  --color-ttg11-card: #171c26;
  --color-ttg11-card: oklch(0.23 0.014 265);
  --color-ttg11-edge: #262d3c;
  --color-ttg11-edge: oklch(0.3 0.016 265);
  --color-ttg11-sensor: #1f2533;
  --color-ttg11-sensor: oklch(0.26 0.018 265);
  --color-ttg11-idle: #737d94;
  --color-ttg11-idle: oklch(0.58 0.02 265);
  --color-ttg11-ok: #4fd398;
  --color-ttg11-ok: oklch(0.79 0.15 160);
  --color-ttg11-scanline: #58b6f0;
  --color-ttg11-scanline: oklch(0.75 0.14 230);
  --color-ttg11-ink: #e7eaf3;
  --color-ttg11-ink: oklch(0.93 0.008 265);
  --color-ttg11-mute: #8d95a8;
  --color-ttg11-mute: oklch(0.66 0.016 265);
  --font-ttg11-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --animate-ttg11-scan: ttg11-scan 1.2s ease-in-out;
  --animate-ttg11-fill: ttg11-fill 1.2s linear forwards;
}

@keyframes ttg11-scan {
  0% {
    transform: translateY(14px);
  }

  50% {
    transform: translateY(88px);
  }

  100% {
    transform: translateY(14px);
  }
}

@keyframes ttg11-fill {
  from {
    --ttg11-p: 0deg;
  }

  to {
    --ttg11-p: 360deg;
  }
}
/* The armed ring has to stay full after the animation is removed, and an aria state
   cannot set a custom property through a utility. */

.ttg-11 [aria-checked="true"] .ttg11-ring {
  --ttg11-p: 360deg;
}

.ttg-11 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const HOLD_MS = 1200;
  const btn = document.querySelector('#ttg-11-btn');
  const state = document.querySelector('#ttg-11-state');
  if (!btn || !state) return;
  let timer = null;

  const arm = () => {
    if (timer) return;
    btn.setAttribute('data-holding', '');
    state.textContent = 'Scanning\u2026';
    timer = setTimeout(() => {
      timer = null;
      btn.removeAttribute('data-holding');
      const next = btn.getAttribute('aria-checked') !== 'true';
      btn.setAttribute('aria-checked', String(next));
      state.textContent = next ? 'Armed \u2014 verified' : 'Locked';
    }, HOLD_MS);
  };

  const disarm = () => {
    if (!timer) return;
    clearTimeout(timer);
    timer = null;
    btn.removeAttribute('data-holding');
    state.textContent = 'Released too early';
  };

  btn.addEventListener('pointerdown', (e) => { btn.setPointerCapture(e.pointerId); arm(); });
  ['pointerup', 'pointercancel', 'pointerleave'].forEach((t) => btn.addEventListener(t, disarm));
  btn.addEventListener('keydown', (e) => {
    if ((e.key === ' ' || e.key === 'Enter') && !e.repeat) { e.preventDefault(); arm(); }
  });
  btn.addEventListener('keyup', (e) => { if (e.key === ' ' || e.key === 'Enter') disarm(); });
})();
```
