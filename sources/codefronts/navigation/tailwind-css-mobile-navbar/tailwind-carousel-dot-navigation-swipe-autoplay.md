---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-carousel-dot-navigation-swipe-autoplay/"
title: "Tailwind Carousel with Dot Navigation, Swipe & Autoplay Progress"
section: "navigation"
category: "tailwind-css-mobile-navbar"
category_name: "Tailwind CSS Mobile Navbars & Menus"
description: "A five-slide onboarding carousel with drag-to-swipe, arrow buttons, keyboard arrows and dots that stretch into a pill &mdash; and the active pill fills like…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Carousel with Dot Navigation, Swipe & Autoplay Progress
Source: https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-carousel-dot-navigation-swipe-autoplay/

A five-slide onboarding carousel with drag-to-swipe, arrow buttons, keyboard arrows and dots that stretch into a pill &mdash; and the active pill fills like a progress bar as autoplay counts down. The fill is the timer: when its CSS animation ends the script advances, so pausing on hover or focus is just animation-play-state.
## HTML
```html
<section class="tmn-12 w-full min-h-svh grid place-items-center bg-tmn12-stage px-4 py-6 font-tmn12-sans antialiased" aria-label="Tailwind carousel with dot navigation demo">
  <div data-tmn12 role="region" aria-roledescription="carousel" aria-label="Product tour" tabindex="0" class="group relative h-[min(667px,calc(100svh-3rem))] w-full max-w-[375px] touch-pan-y overflow-hidden rounded-[2.25rem] text-white shadow-[0_40px_100px_-30px_oklch(0_0_0/0.85)] select-none focus-visible:ring-2 focus-visible:ring-white/60 focus-visible:outline-none">
    <div data-track class="flex h-full transition-[translate] duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-data-dragging:transition-none">
      <div role="group" aria-roledescription="slide" aria-label="1 of 5" class="flex h-full w-full flex-none flex-col items-center justify-center bg-linear-160 from-[#1e1b4b] to-[#3730a3] px-9 text-center">
        <span class="mb-7 grid size-24 place-items-center rounded-[28px] bg-white/10 ring-1 ring-white/20 backdrop-blur"><svg viewBox="0 0 24 24" class="size-11" aria-hidden="true"><path d="M4.5 16.5c-1.5 1.3-2 5-2 5s3.7-.5 5-2c.7-.8.7-2.1-.1-2.9a2.2 2.2 0 0 0-2.9-.1zM12 15l-3-3a22 22 0 0 1 2-3.9A12.9 12.9 0 0 1 22 2c0 2.7-.8 7.5-6 11a22.4 22.4 0 0 1-4 2zM9 12H4s.6-3 2-4c1.6-1.1 5 0 5 0M12 15v5s3-.6 4-2c1.1-1.6 0-5 0-5"/></svg></span>
        <h2 class="mb-3 text-[30px] leading-tight font-bold tracking-[-0.02em]">Launch your ideas</h2>
        <p class="max-w-[28ch] text-[15px] leading-relaxed text-white/75">Build and ship products 10× faster on one streamlined platform.</p>
        <a href="#" class="mt-8 inline-flex min-h-12 items-center rounded-full bg-white px-7 text-sm font-semibold text-[#1e1b4b]">Get started</a>
      </div>
      <div role="group" aria-roledescription="slide" aria-label="2 of 5" inert class="flex h-full w-full flex-none flex-col items-center justify-center bg-linear-160 from-[#0c1446] to-[#1e4e7a] px-9 text-center">
        <span class="mb-7 grid size-24 place-items-center rounded-[28px] bg-white/10 ring-1 ring-white/20 backdrop-blur"><svg viewBox="0 0 24 24" class="size-11" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg></span>
        <h2 class="mb-3 text-[30px] leading-tight font-bold tracking-[-0.02em]">Security first</h2>
        <p class="max-w-[28ch] text-[15px] leading-relaxed text-white/75">Enterprise-grade encryption and SOC 2 compliance in every layer.</p>
        <a href="#" class="mt-8 inline-flex min-h-12 items-center rounded-full bg-white px-7 text-sm font-semibold text-[#0c1446]">Learn more</a>
      </div>
      <div role="group" aria-roledescription="slide" aria-label="3 of 5" inert class="flex h-full w-full flex-none flex-col items-center justify-center bg-linear-160 from-[#2a0845] to-[#6b21a8] px-9 text-center">
        <span class="mb-7 grid size-24 place-items-center rounded-[28px] bg-white/10 ring-1 ring-white/20 backdrop-blur"><svg viewBox="0 0 24 24" class="size-11" aria-hidden="true"><path d="M13 2 3 14h9l-1 8 10-12h-9z"/></svg></span>
        <h2 class="mb-3 text-[30px] leading-tight font-bold tracking-[-0.02em]">Lightning fast</h2>
        <p class="max-w-[28ch] text-[15px] leading-relaxed text-white/75">Sub-100ms responses worldwide on our global edge network.</p>
        <a href="#" class="mt-8 inline-flex min-h-12 items-center rounded-full bg-white px-7 text-sm font-semibold text-[#2a0845]">See benchmarks</a>
      </div>
      <div role="group" aria-roledescription="slide" aria-label="4 of 5" inert class="flex h-full w-full flex-none flex-col items-center justify-center bg-linear-160 from-[#052e1a] to-[#166534] px-9 text-center">
        <span class="mb-7 grid size-24 place-items-center rounded-[28px] bg-white/10 ring-1 ring-white/20 backdrop-blur"><svg viewBox="0 0 24 24" class="size-11" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg></span>
        <h2 class="mb-3 text-[30px] leading-tight font-bold tracking-[-0.02em]">Global scale</h2>
        <p class="max-w-[28ch] text-[15px] leading-relaxed text-white/75">Deploy to 32 regions worldwide in a single click.</p>
        <a href="#" class="mt-8 inline-flex min-h-12 items-center rounded-full bg-white px-7 text-sm font-semibold text-[#052e1a]">Explore regions</a>
      </div>
      <div role="group" aria-roledescription="slide" aria-label="5 of 5" inert class="flex h-full w-full flex-none flex-col items-center justify-center bg-linear-160 from-[#3b1305] to-[#9a3412] px-9 text-center">
        <span class="mb-7 grid size-24 place-items-center rounded-[28px] bg-white/10 ring-1 ring-white/20 backdrop-blur"><svg viewBox="0 0 24 24" class="size-11" aria-hidden="true"><path d="M3 18v-6a9 9 0 0 1 18 0v6M21 19a2 2 0 0 1-2 2h-1v-6h3zM3 19a2 2 0 0 0 2 2h1v-6H3z"/></svg></span>
        <h2 class="mb-3 text-[30px] leading-tight font-bold tracking-[-0.02em]">Premium support</h2>
        <p class="max-w-[28ch] text-[15px] leading-relaxed text-white/75">24/7 experts with a guaranteed one-hour response.</p>
        <a href="#" class="mt-8 inline-flex min-h-12 items-center rounded-full bg-white px-7 text-sm font-semibold text-[#3b1305]">Talk to us</a>
      </div>
    </div>

    <p aria-hidden="true" class="absolute top-6 left-6 text-xs font-bold tracking-[0.2em] text-white/60 uppercase">Discover</p>
    <p class="absolute top-6 right-6 text-[13px] font-semibold tracking-wide text-white/60 tabular-nums" aria-live="polite"><span data-count class="text-white">1</span> / 5</p>

    <button type="button" data-prev class="absolute top-1/2 left-3 z-10 grid size-11 -translate-y-1/2 place-items-center rounded-full bg-white/12 ring-1 ring-white/20 backdrop-blur transition hover:bg-white/22 focus-visible:ring-2 focus-visible:ring-white focus-visible:outline-none pointer-coarse:hidden"><span class="sr-only">Previous slide</span><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="m15 6-6 6 6 6"/></svg></button>
    <button type="button" data-next class="absolute top-1/2 right-3 z-10 grid size-11 -translate-y-1/2 place-items-center rounded-full bg-white/12 ring-1 ring-white/20 backdrop-blur transition hover:bg-white/22 focus-visible:ring-2 focus-visible:ring-white focus-visible:outline-none pointer-coarse:hidden"><span class="sr-only">Next slide</span><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></button>

    <div data-dots class="absolute bottom-7 left-1/2 z-10 flex -translate-x-1/2 items-center">
      <button type="button" aria-label="Slide 1" aria-current="true" class="group/dot grid h-11 place-items-center px-1"><span class="block h-2 w-2 overflow-hidden rounded-full bg-white/35 transition-[width] duration-350 ease-[cubic-bezier(.34,1.56,.64,1)] group-aria-[current=true]/dot:w-7 group-focus-visible/dot:ring-2 group-focus-visible/dot:ring-white"><span class="block h-full origin-left scale-x-0 rounded-full bg-white group-aria-[current=true]/dot:animate-tmn12-fill group-data-paused:[animation-play-state:paused] motion-reduce:group-aria-[current=true]/dot:scale-x-100 motion-reduce:animate-none"></span></span></button>
      <button type="button" aria-label="Slide 2" class="group/dot grid h-11 place-items-center px-1"><span class="block h-2 w-2 overflow-hidden rounded-full bg-white/35 transition-[width] duration-350 ease-[cubic-bezier(.34,1.56,.64,1)] group-aria-[current=true]/dot:w-7 group-focus-visible/dot:ring-2 group-focus-visible/dot:ring-white"><span class="block h-full origin-left scale-x-0 rounded-full bg-white group-aria-[current=true]/dot:animate-tmn12-fill group-data-paused:[animation-play-state:paused] motion-reduce:group-aria-[current=true]/dot:scale-x-100 motion-reduce:animate-none"></span></span></button>
      <button type="button" aria-label="Slide 3" class="group/dot grid h-11 place-items-center px-1"><span class="block h-2 w-2 overflow-hidden rounded-full bg-white/35 transition-[width] duration-350 ease-[cubic-bezier(.34,1.56,.64,1)] group-aria-[current=true]/dot:w-7 group-focus-visible/dot:ring-2 group-focus-visible/dot:ring-white"><span class="block h-full origin-left scale-x-0 rounded-full bg-white group-aria-[current=true]/dot:animate-tmn12-fill group-data-paused:[animation-play-state:paused] motion-reduce:group-aria-[current=true]/dot:scale-x-100 motion-reduce:animate-none"></span></span></button>
      <button type="button" aria-label="Slide 4" class="group/dot grid h-11 place-items-center px-1"><span class="block h-2 w-2 overflow-hidden rounded-full bg-white/35 transition-[width] duration-350 ease-[cubic-bezier(.34,1.56,.64,1)] group-aria-[current=true]/dot:w-7 group-focus-visible/dot:ring-2 group-focus-visible/dot:ring-white"><span class="block h-full origin-left scale-x-0 rounded-full bg-white group-aria-[current=true]/dot:animate-tmn12-fill group-data-paused:[animation-play-state:paused] motion-reduce:group-aria-[current=true]/dot:scale-x-100 motion-reduce:animate-none"></span></span></button>
      <button type="button" aria-label="Slide 5" class="group/dot grid h-11 place-items-center px-1"><span class="block h-2 w-2 overflow-hidden rounded-full bg-white/35 transition-[width] duration-350 ease-[cubic-bezier(.34,1.56,.64,1)] group-aria-[current=true]/dot:w-7 group-focus-visible/dot:ring-2 group-focus-visible/dot:ring-white"><span class="block h-full origin-left scale-x-0 rounded-full bg-white group-aria-[current=true]/dot:animate-tmn12-fill group-data-paused:[animation-play-state:paused] motion-reduce:group-aria-[current=true]/dot:scale-x-100 motion-reduce:animate-none"></span></span></button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmn12-stage: #0b0a14;
  --color-tmn12-stage: oklch(0.15 0.015 285);
  --font-tmn12-sans: 'Urbanist', system-ui, sans-serif;
  --animate-tmn12-fill: tmn12-fill 5s linear forwards;

  @keyframes tmn12-fill {
    from {
      scale: 0 1;
    }

    to {
      scale: 1 1;
    }
  }
}
/* Icon base: utilities still win because this sits in the base layer. */

@layer base {
  .tmn-12 svg {
    fill: none;
    stroke: currentColor;
    stroke-width: 1.8;
    stroke-linecap: round;
    stroke-linejoin: round;
    flex: none;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is
   sized before the browser build compiles. */

.tmn-12 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-tmn12]').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const track = root.querySelector('[data-track]');
    const slides = [...track.children];
    const dots = [...root.querySelectorAll('[data-dots] button')];
    const count = root.querySelector('[data-count]');
    const n = slides.length;
    let i = 0, drag = null;
    const reasons = new Set();

    const go = (to) => {
      i = (to + n) % n;
      track.style.translate = '';
      track.style.translate = (-i * 100) + '% 0';
      slides.forEach((s, k) => { s.inert = k !== i; });
      dots.forEach((d, k) => { if (k === i) d.setAttribute('aria-current', 'true'); else d.removeAttribute('aria-current'); });
      count.textContent = String(i + 1);
    };
    const pause = (why, on) => { if (on) reasons.add(why); else reasons.delete(why); root.toggleAttribute('data-paused', reasons.size > 0); };

    root.querySelector('[data-prev]').addEventListener('click', () => go(i - 1));
    root.querySelector('[data-next]').addEventListener('click', () => go(i + 1));
    dots.forEach((d, k) => d.addEventListener('click', () => go(k)));
    root.addEventListener('animationend', (e) => { if (e.animationName === 'tmn12-fill') go(i + 1); });
    root.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight') { e.preventDefault(); go(i + 1); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); go(i - 1); }
    });
    root.addEventListener('pointerenter', (e) => { if (e.pointerType === 'mouse') pause('hover', true); });
    root.addEventListener('pointerleave', () => pause('hover', false));
    root.addEventListener('focusin', () => pause('focus', true));
    root.addEventListener('focusout', (e) => { if (!root.contains(e.relatedTarget)) pause('focus', false); });
    if ('IntersectionObserver' in window) new IntersectionObserver(([en]) => pause('offscreen', !en.isIntersecting)).observe(root);

    track.addEventListener('pointerdown', (e) => { if (e.button > 0 || e.target.closest('a,button')) return; drag = { x: e.clientX, y: e.clientY, t: performance.now(), dx: 0, on: false, id: e.pointerId }; });
    track.addEventListener('pointermove', (e) => {
      if (!drag) return;
      const dx = e.clientX - drag.x, dy = e.clientY - drag.y;
      if (!drag.on) {
        if (Math.abs(dy) > 12 && Math.abs(dy) > Math.abs(dx)) { drag = null; return; }
        if (Math.abs(dx) < 8) return;
        drag.on = true; root.setAttribute('data-dragging', ''); pause('drag', true);
        try { track.setPointerCapture(drag.id); } catch (err) {}
      }
      drag.dx = dx;
      track.style.translate = 'calc(' + (-i * 100) + '% + ' + dx + 'px) 0';
    });
    const end = () => {
      if (!drag) return;
      const d = drag; drag = null;
      if (!d.on) return;
      root.removeAttribute('data-dragging'); pause('drag', false);
      const v = d.dx / Math.max(1, performance.now() - d.t);
      if (d.dx < -root.offsetWidth * 0.2 || v < -0.5) go(i + 1);
      else if (d.dx > root.offsetWidth * 0.2 || v > 0.5) go(i - 1);
      else go(i);
    };
    track.addEventListener('pointerup', end);
    track.addEventListener('pointercancel', end);
    go(0);
  });
})();
```
