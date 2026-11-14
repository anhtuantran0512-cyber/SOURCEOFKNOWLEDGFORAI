---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-add-to-cart-liquid-glass-ripple-button/"
title: "Tailwind Add-to-Cart Liquid Glass Ripple Button"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A Liquid Glass 'Add to Cart' CTA that ripples like a disturbed pool on click &mdash; a real SVG displacement map radiates from the pointer and warps the…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Add-to-Cart Liquid Glass Ripple Button
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-add-to-cart-liquid-glass-ripple-button/

A Liquid Glass 'Add to Cart' CTA that ripples like a disturbed pool on click &mdash; a real SVG displacement map radiates from the pointer and warps the frosted surface, then decays. Includes a success morph, an aria-live status and a High-Performance toggle that swaps the GPU-heavy warp for a pure-CSS ripple.
## HTML
```html
<section class="tbh-36 w-full min-h-svh grid place-items-center p-6 font-tbh36-sans bg-[conic-gradient(from_200deg_at_40%_60%,var(--color-tbh36-g1),var(--color-tbh36-g2),var(--color-tbh36-g3),var(--color-tbh36-g1))] bg-[length:220%_220%] animate-tbh36-bg motion-reduce:animate-none" aria-label="Add to cart ripple glass button demo">
  <svg aria-hidden="true" width="0" height="0" class="absolute">
    <filter id="tbh36-ripple">
      <feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="3" result="n">
        <animate attributeName="baseFrequency" dur="6s" values="0.02;0.035;0.02" repeatCount="indefinite"></animate>
      </feTurbulence>
      <feDisplacementMap id="tbh36-disp" in="SourceGraphic" in2="n" scale="0" xChannelSelector="R" yChannelSelector="G"></feDisplacementMap>
    </filter>
  </svg>
  <div id="tbh-36-stage" data-perf="high" class="group/stage grid justify-items-center gap-4">
    <button id="tbh-36-btn" type="button" class="group/btn relative isolate overflow-hidden min-h-[52px] px-[30px] cursor-pointer rounded-full border border-white/45 text-base font-bold text-white bg-[color-mix(in_oklab,white_16%,transparent)] shadow-[inset_0_1px_0_oklch(1_0_0/0.6),0_18px_40px_-18px_oklch(0_0_0/0.7)] backdrop-blur-[16px] backdrop-saturate-[1.8] transition-[box-shadow,background-color,border-color] duration-300 hover:shadow-[inset_0_1px_0_oklch(1_0_0/0.7),0_22px_46px_-18px_oklch(0_0_0/0.7)] focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-[3px] data-done:bg-[color-mix(in_oklab,var(--color-tbh36-accent)_70%,transparent)] data-done:border-transparent">
      <span aria-hidden="true" class="absolute inset-0 z-0 bg-[radial-gradient(140px_140px_at_var(--mx,50%)_var(--my,50%),oklch(1_0_0/0.4),transparent_60%)] group-data-[perf=high]/stage:[filter:url(#tbh36-ripple)] group-data-[perf=css]/stage:group-[.is-ripple]/btn:animate-tbh36-css motion-reduce:[filter:none]"></span>
      <span class="relative z-[1] inline-flex items-center gap-[9px] transition-[opacity,scale] duration-300 group-data-done/btn:scale-[1.04]">
        <span class="inline-flex items-center gap-[9px] group-data-done/btn:hidden">
          <span aria-hidden="true" class="text-[17px]">&#128722;</span>Add to Cart &middot; $89
        </span>
        <span class="hidden items-center gap-[9px] group-data-done/btn:inline-flex">
          <span aria-hidden="true">&check;</span>Added to Cart
        </span>
      </span>
    </button>
    <p id="tbh-36-status" aria-live="polite" class="min-h-[1.2em] text-[13px] font-semibold text-white [text-shadow:0_1px_6px_oklch(0_0_0/0.3)]"></p>
    <label class="flex items-center gap-[7px] text-[12.5px] text-white/85 cursor-pointer">
      <input id="tbh-36-perf" type="checkbox" class="accent-tbh36-accent"> High-Performance Mode (CSS ripple)
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh36-accent: #4ec98d;
  --color-tbh36-accent: oklch(0.68 0.18 155);
  --color-tbh36-g1: #0ea5e9;
  --color-tbh36-g1: oklch(0.7 0.15 230);
  --color-tbh36-g2: #6366f1;
  --color-tbh36-g2: oklch(0.58 0.22 275);
  --color-tbh36-g3: #ec4899;
  --color-tbh36-g3: oklch(0.65 0.24 350);
  --font-tbh36-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tbh36-bg: tbh36-bg 20s ease-in-out infinite;
  --animate-tbh36-css: tbh36-css 0.6s ease-out;
}
/* Stays CSS: the drifting stage gradient and the fallback ripple keyframes. */

@keyframes tbh36-bg {
  50% {
    background-position: 100% 100%;
  }
}

@keyframes tbh36-css {
  0% {
    scale: 0.3;
    opacity: 0.9;
  }

  100% {
    scale: 2.4;
    opacity: 0;
  }
}
/* Stays CSS: Safari < 16.4 prefixed backdrop-filter. */

.tbh-36 button {
  -webkit-backdrop-filter: blur(16px) saturate(180%);
}

.tbh-36 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const stage = document.querySelector('#tbh-36-stage');
  const btn = document.querySelector('#tbh-36-btn');
  const disp = document.querySelector('#tbh36-disp');
  const status = document.querySelector('#tbh-36-status');
  const perf = document.querySelector('#tbh-36-perf');
  if (!stage || !btn) return;

  perf.addEventListener('change', () => { stage.dataset.perf = perf.checked ? 'css' : 'high'; });

  const setPos = e => {
    const r = btn.getBoundingClientRect();
    btn.style.setProperty('--mx', (e.clientX - r.left) + 'px');
    btn.style.setProperty('--my', (e.clientY - r.top) + 'px');
  };
  btn.addEventListener('pointermove', setPos);

  let raf;
  const rippleSVG = () => {
    if (!disp) return;
    let s = 26;
    cancelAnimationFrame(raf);
    const step = () => {
      s -= 1.6;
      if (s <= 0) { disp.setAttribute('scale', 0); return; }
      disp.setAttribute('scale', s);
      raf = requestAnimationFrame(step);
    };
    step();
  };

  let reset;
  btn.addEventListener('click', e => {
    setPos(e);
    if (stage.dataset.perf === 'high') rippleSVG();
    else { btn.classList.remove('is-ripple'); void btn.offsetWidth; btn.classList.add('is-ripple'); }
    btn.dataset.done = '';
    status.textContent = 'Added to cart — 1 item';
    clearTimeout(reset);
    reset = setTimeout(() => { delete btn.dataset.done; status.textContent = ''; }, 1600);
  });
})();
```
