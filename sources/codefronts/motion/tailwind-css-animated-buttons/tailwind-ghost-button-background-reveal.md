---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-ghost-button-background-reveal/"
title: "Tailwind Ghost Button with Cursor-Aware Background Reveal"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "A ghost button whose fill grows from wherever the cursor entered and shrinks back toward wherever it left."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Ghost Button with Cursor-Aware Background Reveal
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-ghost-button-background-reveal/

A ghost button whose fill grows from wherever the cursor entered and shrinks back toward wherever it left. Demo 03 showed why a pure-CSS ripple can't do this: CSS has no access to pointer coordinates. Here JS supplies two numbers and nothing else.
## HTML
```html
<section class="tab-20 w-full min-h-svh grid place-items-center bg-tab20-bg font-tab20-sans px-6 py-10">
  <div class="flex flex-col items-center gap-8">
    <p class="text-[0.78rem] tracking-[0.14em] uppercase text-tab20-dim m-0">Hover from any direction</p>
    <div class="flex flex-wrap justify-center gap-4">
      <button type="button" data-state="idle" class="tab20-btn relative overflow-hidden min-h-11 px-9 text-[0.95rem] font-bold text-tab20-violet-ink bg-transparent border-2 border-tab20-violet rounded-[10px] cursor-pointer transition-[color,border-color] duration-[350ms] hover:text-white hover:border-transparent focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab20-violet motion-reduce:transition-none">
        <span class="tab20-fill absolute left-[var(--rx,50%)] top-[var(--ry,50%)] size-0 -translate-x-1/2 -translate-y-1/2 rounded-full bg-tab20-violet pointer-events-none transition-[width,height] duration-500 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none"></span>
        <span class="relative z-10">Get Started</span>
      </button>
      <button type="button" data-state="idle" class="tab20-btn relative overflow-hidden min-h-11 px-9 text-[0.95rem] font-bold text-tab20-cyan-ink bg-transparent border-2 border-tab20-cyan rounded-[10px] cursor-pointer transition-[color,border-color] duration-[350ms] hover:text-white hover:border-transparent focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab20-cyan motion-reduce:transition-none">
        <span class="tab20-fill absolute left-[var(--rx,50%)] top-[var(--ry,50%)] size-0 -translate-x-1/2 -translate-y-1/2 rounded-full bg-tab20-cyan pointer-events-none transition-[width,height] duration-500 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none"></span>
        <span class="relative z-10">View Docs</span>
      </button>
      <button type="button" data-state="idle" class="tab20-btn relative overflow-hidden min-h-11 px-9 text-[0.95rem] font-bold text-tab20-rose-ink bg-transparent border-2 border-tab20-rose rounded-[10px] cursor-pointer transition-[color,border-color] duration-[350ms] hover:text-white hover:border-transparent focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab20-rose motion-reduce:transition-none">
        <span class="tab20-fill absolute left-[var(--rx,50%)] top-[var(--ry,50%)] size-0 -translate-x-1/2 -translate-y-1/2 rounded-full bg-tab20-rose pointer-events-none transition-[width,height] duration-500 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none"></span>
        <span class="relative z-10">Contact Us</span>
      </button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab20-bg: #0a0a14;
  --color-tab20-bg: oklch(0.11 0.02 275);
  --color-tab20-dim: #64748b;
  --color-tab20-dim: oklch(0.55 0.03 255);
  --color-tab20-violet: #6d28d9;
  --color-tab20-violet: oklch(0.47 0.24 295);
  --color-tab20-violet-ink: #c4b5fd;
  --color-tab20-violet-ink: oklch(0.83 0.1 292);
  --color-tab20-cyan: #0e7490;
  --color-tab20-cyan: oklch(0.48 0.1 221);
  --color-tab20-cyan-ink: #a5f3fc;
  --color-tab20-cyan-ink: oklch(0.9 0.08 202);
  --color-tab20-rose: #be123c;
  --color-tab20-rose: oklch(0.49 0.2 14);
  --color-tab20-rose-ink: #fda4af;
  --color-tab20-rose-ink: oklch(0.8 0.12 13);
  --font-tab20-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* The fill's open state: a size driven by a JS-measured custom property, which is
   not expressible as a utility value because --size is written at runtime. */

.tab-20 [data-state="hover"] .tab20-fill {
  width: var(--size, 400px);
  height: var(--size, 400px);
}

.tab-20 {
  width: 100%;
  min-height: 100svh;
}

.tab-20 ::selection {
  background: var(--color-tab20-violet);
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .tab-20 [data-state="hover"] .tab20-fill {
    width: 100%;
    height: 100%;
    border-radius: 0;
  }
}
```

## JavaScript
```js
(function () {
  var calm = window.matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('.tab-20 .tab20-btn').forEach(function (btn) {
    var fill = btn.querySelector('.tab20-fill');
    if (!fill) return;
    function measure() {
      var d = Math.sqrt(Math.pow(btn.offsetWidth, 2) + Math.pow(btn.offsetHeight, 2));
      btn.style.setProperty('--size', d * 3 + 'px');
    }
    measure();
    if (window.ResizeObserver) new ResizeObserver(measure).observe(btn);
    function origin(e) {
      if (calm.matches) return;
      fill.style.setProperty('--rx', e.offsetX + 'px');
      fill.style.setProperty('--ry', e.offsetY + 'px');
    }
    btn.addEventListener('pointerenter', function (e) { origin(e); btn.dataset.state = 'hover'; });
    btn.addEventListener('pointerleave', function (e) { origin(e); btn.dataset.state = 'idle'; });
    btn.addEventListener('focus', function () { btn.dataset.state = 'hover'; });
    btn.addEventListener('blur', function () { btn.dataset.state = 'idle'; });
  });
})();
```
