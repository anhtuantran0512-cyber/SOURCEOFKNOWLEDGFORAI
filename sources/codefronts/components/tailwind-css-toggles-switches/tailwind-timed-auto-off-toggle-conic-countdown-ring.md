---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-timed-auto-off-toggle-conic-countdown-ring/"
title: "Tailwind Timed Auto-Off Toggle with Conic Countdown Ring"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "A switch that disarms itself: flip it on and a conic ring drains for 8 seconds, then the toggle flips back off with the change announced politely."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Timed Auto-Off Toggle with Conic Countdown Ring
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-timed-auto-off-toggle-conic-countdown-ring/

A switch that disarms itself: flip it on and a conic ring drains for 8 seconds, then the toggle flips back off with the change announced politely. The ring is a registered custom property the browser tweens natively &mdash; no requestAnimationFrame loop anywhere.
## HTML
```html
<section class="ttg-10 w-full min-h-svh grid place-items-center px-5 py-14 bg-ttg10-bg font-ttg10-sans" aria-label="Timed auto-off toggle">
  <div class="w-[min(340px,100%)] flex flex-col items-center gap-5 px-9 py-8 rounded-[22px] bg-ttg10-card border border-ttg10-edge">
    <div class="flex flex-col items-center gap-1 text-center">
      <b class="text-[17px] font-bold text-ttg10-ink">Temporarily allow</b>
      <span class="text-[12.5px] text-ttg10-mute">USB debugging &middot; auto-off in 8s</span>
    </div>
    <span id="ttg-10-ring" class="relative grid place-items-center w-28 h-28 rounded-full [background:conic-gradient(var(--color-ttg10-warn)_var(--ttg10-p,100%),var(--color-ttg10-rail)_0)] before:content-[''] before:absolute before:inset-[5px] before:rounded-full before:bg-ttg10-card data-counting:animate-ttg10-drain">
      <input type="checkbox" id="ttg-10-sw" role="switch" aria-label="Temporarily allow USB debugging" class="appearance-none relative z-10 w-16 h-9 rounded-full bg-ttg10-off cursor-pointer transition-colors duration-300 before:content-[''] before:absolute before:top-[3px] before:left-[3px] before:w-[30px] before:h-[30px] before:rounded-full before:bg-white before:shadow-[0_2px_6px_oklch(0_0_0/0.5)] before:transition-transform before:duration-300 before:ease-[cubic-bezier(0.25,0.9,0.3,1.1)] checked:bg-ttg10-warn checked:before:translate-x-7 focus-visible:outline-3 focus-visible:outline-ttg10-warn focus-visible:outline-offset-4 motion-reduce:transition-none motion-reduce:before:transition-none">
    </span>
    <p id="ttg-10-live" aria-live="polite" class="min-h-[1.2em] text-center text-[12.5px] text-ttg10-mute">Off &mdash; flip to allow for 8 seconds</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Registration is what makes the sweep interpolable; without it the conic gradient
   jumps between computed values instead of animating. */

@property --ttg10-p {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 100%;
}

@theme {
  --color-ttg10-bg: #14161c;
  --color-ttg10-bg: oklch(0.2 0.01 265);
  --color-ttg10-card: #1c2029;
  --color-ttg10-card: oklch(0.25 0.012 265);
  --color-ttg10-edge: #2b303c;
  --color-ttg10-edge: oklch(0.32 0.014 265);
  --color-ttg10-rail: #2b303c;
  --color-ttg10-rail: oklch(0.32 0.014 265);
  --color-ttg10-off: #343a4a;
  --color-ttg10-off: oklch(0.36 0.018 265);
  --color-ttg10-warn: #eea23c;
  --color-ttg10-warn: oklch(0.78 0.15 68);
  --color-ttg10-ink: #e8eaf2;
  --color-ttg10-ink: oklch(0.93 0.008 265);
  --color-ttg10-mute: #939bad;
  --color-ttg10-mute: oklch(0.68 0.015 265);
  --font-ttg10-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --animate-ttg10-drain: ttg10-drain 8s linear forwards;
}

@keyframes ttg10-drain {
  from {
    --ttg10-p: 100%;
  }

  to {
    --ttg10-p: 0%;
  }
}

.ttg-10 {
  width: 100%;
  min-height: 100svh;
}

.ttg-10 input[type="checkbox"] {
  -webkit-appearance: none;
}
```

## JavaScript
```js
(() => {
  const DURATION = 8000;
  const sw = document.querySelector('#ttg-10-sw');
  const ring = document.querySelector('#ttg-10-ring');
  const live = document.querySelector('#ttg-10-live');
  if (!sw || !ring || !live) return;
  let timer = null;

  // The script owns exactly one attribute; every visual consequence is a Tailwind variant.
  const count = (on) => {
    ring.removeAttribute('data-counting');
    if (!on) return;
    void ring.offsetWidth; // restart the CSS countdown
    ring.setAttribute('data-counting', '');
  };

  sw.addEventListener('change', () => {
    clearTimeout(timer);
    count(sw.checked);
    if (!sw.checked) { live.textContent = 'Disabled'; return; }
    live.textContent = 'Enabled for 8 seconds';
    timer = setTimeout(() => {
      sw.checked = false;
      count(false);
      live.textContent = 'Auto-disabled';
    }, DURATION);
  });
})();
```
