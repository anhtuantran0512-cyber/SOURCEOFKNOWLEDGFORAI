---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-order-success-modal-css-confetti-elastic-morph/"
title: "Tailwind Order Success Modal with CSS-Only Confetti Burst"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "The peak-dopamine moment: the card springs from 12% scale while twelve CSS particles fire outward on cos()/sin() paths."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Order Success Modal with CSS-Only Confetti Burst
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-order-success-modal-css-confetti-elastic-morph/

The peak-dopamine moment: the card springs from 12% scale while twelve CSS particles fire outward on cos()/sin() paths. No canvas, no particle library — each span carries its own angle, distance and colour as custom properties, and the port keeps them as inline --* values because per-particle randomness is data, not design tokens.
## HTML
```html
<section class="tw-15 w-full min-h-svh grid place-items-center bg-tw15-bg font-tw15-sans px-6 py-10">
  <button type="button" data-tw15-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-[9px] border-0 bg-tw15-ink text-[15px] font-bold text-tw15-card tabular-nums shadow-[0_10px_22px_-6px_#1e293b66] cursor-pointer transition-colors duration-200 hover:bg-black focus-visible:outline-2 focus-visible:outline-tw15-brand focus-visible:outline-offset-2">Complete order · $189</button>

  <dialog id="tw-15-dlg" aria-labelledby="tw-15-title" class="group m-auto w-[min(460px,94vw)] p-0 border-0 rounded-2xl text-center text-tw15-ink bg-tw15-card shadow-[0_40px_60px_-20px_#1e293b59] will-change-transform opacity-0 scale-[0.12] transition-[opacity,scale,overlay,display] duration-[650ms] ease-[cubic-bezier(.68,-0.55,.32,1.55)] transition-discrete open:opacity-100 open:scale-100 open:starting:opacity-0 open:starting:scale-[0.12] open:backdrop:bg-tw15-scrim open:backdrop:backdrop-blur-[6px] motion-reduce:transition-[opacity] motion-reduce:duration-200 motion-reduce:scale-100">
    <div class="relative px-[30px] pt-9 pb-6">
      <div aria-hidden="true" class="absolute top-1/2 left-1/2 size-0 pointer-events-none motion-reduce:hidden">
        <span style="--c:#e05252;--angle:12deg;--dist:180px" class="absolute w-2.5 h-3.5 rounded-[2px] bg-[var(--c)] opacity-0 group-open:animate-tw15-confetti"></span>
        <span style="--c:#2aa79e;--angle:47deg;--dist:210px" class="absolute w-2.5 h-3.5 rounded-[2px] bg-[var(--c)] opacity-0 group-open:animate-tw15-confetti"></span>
        <span style="--c:#c9a961;--angle:88deg;--dist:170px" class="absolute w-2.5 h-3.5 rounded-[2px] bg-[var(--c)] opacity-0 group-open:animate-tw15-confetti"></span>
        <span style="--c:#a855f7;--angle:128deg;--dist:200px" class="absolute w-2.5 h-3.5 rounded-[2px] bg-[var(--c)] opacity-0 group-open:animate-tw15-confetti"></span>
        <span style="--c:#10b981;--angle:165deg;--dist:190px" class="absolute w-2.5 h-3.5 rounded-[2px] bg-[var(--c)] opacity-0 group-open:animate-tw15-confetti"></span>
        <span style="--c:#ff6b6b;--angle:205deg;--dist:220px" class="absolute w-2.5 h-3.5 rounded-[2px] bg-[var(--c)] opacity-0 group-open:animate-tw15-confetti"></span>
        <span style="--c:#4ecdc4;--angle:240deg;--dist:180px" class="absolute w-2.5 h-3.5 rounded-[2px] bg-[var(--c)] opacity-0 group-open:animate-tw15-confetti"></span>
        <span style="--c:#c9a961;--angle:275deg;--dist:210px" class="absolute w-2.5 h-3.5 rounded-[2px] bg-[var(--c)] opacity-0 group-open:animate-tw15-confetti"></span>
        <span style="--c:#a855f7;--angle:312deg;--dist:200px" class="absolute w-2.5 h-3.5 rounded-[2px] bg-[var(--c)] opacity-0 group-open:animate-tw15-confetti"></span>
        <span style="--c:#10b981;--angle:340deg;--dist:190px" class="absolute w-2.5 h-3.5 rounded-[2px] bg-[var(--c)] opacity-0 group-open:animate-tw15-confetti"></span>
        <span style="--c:#ec4899;--angle:60deg;--dist:150px" class="absolute w-2.5 h-3.5 rounded-[2px] bg-[var(--c)] opacity-0 group-open:animate-tw15-confetti"></span>
        <span style="--c:#3b82f6;--angle:220deg;--dist:150px" class="absolute w-2.5 h-3.5 rounded-[2px] bg-[var(--c)] opacity-0 group-open:animate-tw15-confetti"></span>
      </div>

      <button type="button" data-tw15-close aria-label="Close dialog" class="absolute top-3.5 right-3.5 z-10 grid place-items-center size-9 rounded-lg border-0 bg-transparent text-[15px] text-tw15-sub cursor-pointer transition-colors duration-200 hover:bg-tw15-hover hover:text-tw15-ink focus-visible:outline-2 focus-visible:outline-tw15-brand focus-visible:outline-offset-2">&#10005;</button>

      <span aria-hidden="true" class="inline-grid place-items-center size-13 mb-3.5 rounded-full bg-linear-to-br from-tw15-good to-tw15-brand text-2xl font-black text-white shadow-[0_8px_20px_-4px_var(--color-tw15-glow)]">&#10003;</span>
      <p class="mb-2 font-tw15-mono text-xs font-bold uppercase tracking-[0.14em] text-tw15-sub">Order #TR-8842</p>
      <h2 id="tw-15-title" class="mb-2 font-tw15-display text-[1.55rem] font-extrabold tracking-[-0.02em] leading-tight text-balance">Thanks for your order, Alex</h2>
      <p class="mb-[18px] text-sm leading-relaxed text-tw15-sub text-pretty">A confirmation is on its way to <strong class="font-semibold text-tw15-ink">[email protected]</strong>. Your package ships in 24 hours.</p>
      <p aria-live="assertive" class="sr-only">Order TR-8842 confirmed. Total charged $189.00. Confirmation sent to [email protected].</p>

      <div class="flex flex-wrap justify-between items-center gap-3 mb-3.5 px-3.5 py-3 rounded-[9px] bg-tw15-goodtint text-left">
        <div>
          <p class="text-[0.66rem] font-bold uppercase tracking-wide text-tw15-brand">Estimated delivery</p>
          <p class="mt-0.5 text-sm font-bold text-tw15-ink">Tue, Jul 30 — Thu, Aug 1</p>
        </div>
        <span class="px-2.5 py-1.5 rounded-full bg-tw15-brand text-xs font-bold text-white whitespace-nowrap">Free 2-day shipping</span>
      </div>

      <div class="mb-4 px-4 py-3.5 rounded-[9px] border border-tw15-line text-left">
        <div class="flex justify-between text-sm text-tw15-sub"><span>Subtotal (2 items)</span><span class="tabular-nums">$168.00</span></div>
        <div class="flex justify-between mt-1.5 text-sm text-tw15-sub"><span>Shipping</span><span class="font-bold text-tw15-brand">Free</span></div>
        <div class="flex justify-between mt-1.5 text-sm text-tw15-sub"><span>Tax</span><span class="tabular-nums">$21.00</span></div>
        <div class="flex justify-between pt-2.5 mt-2.5 border-t border-tw15-line text-tw15-ink"><strong class="text-[0.9rem] font-extrabold">Total charged</strong><strong class="text-[0.9rem] font-extrabold tabular-nums">$189.00</strong></div>
      </div>

      <button type="button" autofocus data-tw15-close class="w-full min-h-11 mb-2.5 px-5 py-3.5 rounded-[9px] border-0 bg-tw15-ink text-[15px] font-extrabold text-tw15-card cursor-pointer transition-[background-color,translate] duration-200 hover:bg-black hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tw15-brand focus-visible:outline-offset-[3px] motion-reduce:hover:translate-y-0">Track your order &rarr;</button>
      <div class="grid grid-cols-2 gap-2">
        <button type="button" data-tw15-close class="min-h-11 px-3 rounded-md border-0 bg-transparent text-[13px] font-semibold text-tw15-sub cursor-pointer transition-colors duration-200 hover:bg-tw15-hover hover:text-tw15-ink focus-visible:outline-2 focus-visible:outline-tw15-brand focus-visible:outline-offset-2">Print receipt</button>
        <button type="button" data-tw15-close class="min-h-11 px-3 rounded-md border-0 bg-transparent text-[13px] font-semibold text-tw15-sub cursor-pointer transition-colors duration-200 hover:bg-tw15-hover hover:text-tw15-ink focus-visible:outline-2 focus-visible:outline-tw15-brand focus-visible:outline-offset-2">Share purchase</button>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tw15-bg: #fdf7f4;
  --color-tw15-bg: oklch(0.97 0.012 40);
  --color-tw15-card: #faf7f0;
  --color-tw15-card: oklch(0.97 0.012 85);
  --color-tw15-ink: #1e293b;
  --color-tw15-ink: oklch(0.3 0.03 258);
  --color-tw15-sub: #5d5749;
  --color-tw15-sub: oklch(0.46 0.02 80);
  --color-tw15-line: #eee5d0;
  --color-tw15-line: oklch(0.93 0.025 85);
  --color-tw15-brand: #047857;
  --color-tw15-brand: oklch(0.52 0.12 164);
  --color-tw15-good: #10b981;
  --color-tw15-good: oklch(0.7 0.15 163);
  --color-tw15-goodtint: #10b98114;
  --color-tw15-goodtint: oklch(0.7 0.15 163 / 0.1);
  --color-tw15-glow: #10b98180;
  --color-tw15-glow: oklch(0.7 0.15 163 / 0.5);
  --color-tw15-hover: #1a1a1a0f;
  --color-tw15-hover: oklch(0.22 0 0 / 0.06);
  --color-tw15-scrim: #1e293b8c;
  --color-tw15-scrim: oklch(0.3 0.03 258 / 0.55);
  --font-tw15-sans: 'Outfit', system-ui, sans-serif;
  --font-tw15-display: 'Playfair Display', Georgia, serif;
  --font-tw15-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tw15-confetti: tw15-confetti 1.2s cubic-bezier(.4, 0, .2, 1) forwards;
}

.tw-15 {
  width: 100%;
}
/* One keyframe, twelve particles: each span's own --angle/--dist do the aiming. */

@keyframes tw15-confetti {
  0% {
    opacity: 0;
    translate: -50% -50%;
    rotate: 0deg;
  }

  15% {
    opacity: 1;
  }

  100% {
    opacity: 0;
    translate: calc(-50% + cos(var(--angle)) * var(--dist)) calc(-50% + sin(var(--angle)) * var(--dist));
    rotate: 720deg;
  }
}
/* The burst's organic feel comes from the angle doubling as the stagger. */

#tw-15-dlg [style*="--angle"] {
  animation-delay: calc(var(--angle) / 360 * 0.5s);
}

#tw-15-dlg::backdrop {
  background: oklch(0.3 0.03 258 / 0);
  backdrop-filter: blur(0px);
  transition: background .3s ease, backdrop-filter .3s ease, overlay .3s allow-discrete, display .3s allow-discrete;
}

@starting-style {
  #tw-15-dlg[open]::backdrop {
    background: oklch(0.3 0.03 258 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tw-15-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tw-15');
  var dlg = root.querySelector('#tw-15-dlg');
  var card = dlg.firstElementChild;
  root.querySelector('[data-tw15-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelectorAll('[data-tw15-close]').forEach(function (b) {
    b.addEventListener('click', function () { dlg.close(); });
  });
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
