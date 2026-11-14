---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/javascript-testimonial-quote-slider-tailwind-css/"
title: "JavaScript Testimonial Quote Slider with Tailwind CSS"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "A testimonial carousel built on native scroll-snap (snap-x snap-mandatory), so swipe and trackpad physics are the browser's own."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: JavaScript Testimonial Quote Slider with Tailwind CSS
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/javascript-testimonial-quote-slider-tailwind-css/

A testimonial carousel built on native scroll-snap (snap-x snap-mandatory), so swipe and trackpad physics are the browser's own. The port adds what the accessibility audit asks for — a visible pause/play toggle (WCAG 2.2.2), prev/next buttons, 44px dots — and fixes a drift bug where the index math ignored the gap between slides.
## HTML
```html
<section class="tbq-23 w-full min-h-svh grid place-items-center bg-tbq23-bg bg-[radial-gradient(70%_55%_at_50%_100%,var(--color-tbq23-glow),transparent)] px-5 py-14 font-tbq23-sans text-tbq23-ink" aria-label="Testimonial quote slider demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="w-full max-w-[560px]" id="tbq23-slider" role="region" aria-roledescription="carousel" aria-label="Customer testimonials">
      <div data-track tabindex="0" aria-label="Testimonials — swipe, scroll or use the controls" class="grid auto-cols-[100%] grid-flow-col gap-4.5 overflow-x-auto scroll-smooth snap-x snap-mandatory rounded-3xl px-1.5 pt-1.5 pb-10 -mb-8 [scrollbar-width:none] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tbq23-acc motion-reduce:scroll-auto [&::-webkit-scrollbar]:hidden">
        <figure role="group" aria-roledescription="slide" aria-label="1 of 3" class="grid min-h-[230px] snap-center content-center gap-4.5 rounded-[20px] border border-black/7 bg-tbq23-card p-[clamp(24px,4vw,34px)] shadow-[0_3px_8px_oklch(0.3_0.04_290/0.07),0_18px_40px_oklch(0.3_0.04_290/0.1)]">
          <blockquote><p class="text-[clamp(17px,2.2vw,20px)] leading-[1.6] font-medium tracking-[-0.008em] text-pretty">“We replaced a 2,000-line carousel plugin with scroll-snap and a dozen lines of glue. Support tickets about the slider: zero since.”</p></blockquote>
          <figcaption class="text-[13px] text-tbq23-mut"><strong class="font-bold text-tbq23-acc">Imogen Hart</strong> · Frontend Lead, Lumen Retail</figcaption>
        </figure>
        <figure role="group" aria-roledescription="slide" aria-label="2 of 3" class="grid min-h-[230px] snap-center content-center gap-4.5 rounded-[20px] border border-black/7 bg-tbq23-card p-[clamp(24px,4vw,34px)] shadow-[0_3px_8px_oklch(0.3_0.04_290/0.07),0_18px_40px_oklch(0.3_0.04_290/0.1)]">
          <blockquote><p class="text-[clamp(17px,2.2vw,20px)] leading-[1.6] font-medium tracking-[-0.008em] text-pretty">“The native swipe physics are the feature. No JS carousel ever matched the trackpad feel our users kept complaining about.”</p></blockquote>
          <figcaption class="text-[13px] text-tbq23-mut"><strong class="font-bold text-tbq23-acc">Dario Fontaine</strong> · Product Engineer, Atlas Bank</figcaption>
        </figure>
        <figure role="group" aria-roledescription="slide" aria-label="3 of 3" class="grid min-h-[230px] snap-center content-center gap-4.5 rounded-[20px] border border-black/7 bg-tbq23-card p-[clamp(24px,4vw,34px)] shadow-[0_3px_8px_oklch(0.3_0.04_290/0.07),0_18px_40px_oklch(0.3_0.04_290/0.1)]">
          <blockquote><p class="text-[clamp(17px,2.2vw,20px)] leading-[1.6] font-medium tracking-[-0.008em] text-pretty">“Autoplay that actually pauses — for hover, focus, reduced motion and a real pause button. Our accessibility audit finally has an empty carousel section.”</p></blockquote>
          <figcaption class="text-[13px] text-tbq23-mut"><strong class="font-bold text-tbq23-acc">Sofia Meloni</strong> · Design Systems, Fernwood</figcaption>
        </figure>
      </div>
      <div class="mt-4 flex items-center justify-between gap-3">
        <button type="button" data-toggle aria-pressed="false" aria-label="Pause autoplay" class="group/p grid size-11 cursor-pointer place-items-center rounded-full border border-black/10 bg-tbq23-card text-tbq23-ink transition-colors hover:border-tbq23-acc hover:text-tbq23-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tbq23-acc aria-pressed:bg-tbq23-acc aria-pressed:text-white">
          <svg class="group-aria-pressed/p:hidden" viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><rect x="3.5" y="2.5" width="3" height="11" rx="1" fill="currentColor"/><rect x="9.5" y="2.5" width="3" height="11" rx="1" fill="currentColor"/></svg>
          <svg class="hidden group-aria-pressed/p:block" viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M4.5 2.8v10.4a.6.6 0 0 0 .9.5l8.2-5.2a.6.6 0 0 0 0-1L5.4 2.3a.6.6 0 0 0-.9.5z" fill="currentColor"/></svg>
        </button>
        <div class="flex" aria-label="Choose testimonial">
          <button type="button" data-dot aria-current="true" aria-label="Show testimonial 1" class="grid size-11 cursor-pointer place-items-center rounded-full before:h-2 before:w-2 before:rounded-full before:bg-tbq23-dot before:transition-[width,background-color] before:duration-300 hover:before:bg-tbq23-acc focus-visible:outline-2 focus-visible:-outline-offset-4 focus-visible:outline-tbq23-acc aria-[current=true]:before:w-6.5 aria-[current=true]:before:bg-tbq23-acc motion-reduce:before:transition-none"></button>
          <button type="button" data-dot aria-current="false" aria-label="Show testimonial 2" class="grid size-11 cursor-pointer place-items-center rounded-full before:h-2 before:w-2 before:rounded-full before:bg-tbq23-dot before:transition-[width,background-color] before:duration-300 hover:before:bg-tbq23-acc focus-visible:outline-2 focus-visible:-outline-offset-4 focus-visible:outline-tbq23-acc aria-[current=true]:before:w-6.5 aria-[current=true]:before:bg-tbq23-acc motion-reduce:before:transition-none"></button>
          <button type="button" data-dot aria-current="false" aria-label="Show testimonial 3" class="grid size-11 cursor-pointer place-items-center rounded-full before:h-2 before:w-2 before:rounded-full before:bg-tbq23-dot before:transition-[width,background-color] before:duration-300 hover:before:bg-tbq23-acc focus-visible:outline-2 focus-visible:-outline-offset-4 focus-visible:outline-tbq23-acc aria-[current=true]:before:w-6.5 aria-[current=true]:before:bg-tbq23-acc motion-reduce:before:transition-none"></button>
        </div>
        <div class="flex gap-2">
          <button type="button" data-prev aria-label="Previous testimonial" class="grid size-11 cursor-pointer place-items-center rounded-full border border-black/10 bg-tbq23-card transition-colors hover:border-tbq23-acc hover:text-tbq23-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tbq23-acc"><svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true"><path d="M10 3.5 5.5 8l4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
          <button type="button" data-next aria-label="Next testimonial" class="grid size-11 cursor-pointer place-items-center rounded-full border border-black/10 bg-tbq23-card transition-colors hover:border-tbq23-acc hover:text-tbq23-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tbq23-acc"><svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true"><path d="M6 3.5 10.5 8 6 12.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
        </div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-black/10 bg-white px-3.5 py-2 font-tbq23-mono text-[11.5px] text-tbq23-mut">snap-x snap-mandatory · aria-[current=true]: dots · WCAG 2.2.2 pause</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq23-bg: #efeff7;
  --color-tbq23-bg: oklch(0.955 0.01 285);
  --color-tbq23-glow: #dfd9f699;
  --color-tbq23-glow: oklch(0.9 0.04 295 / 0.6);
  --color-tbq23-card: #ffffff;
  --color-tbq23-card: oklch(1 0 0);
  --color-tbq23-ink: #21202b;
  --color-tbq23-ink: oklch(0.25 0.02 290);
  --color-tbq23-mut: #5d5c68;
  --color-tbq23-mut: oklch(0.48 0.02 290);
  --color-tbq23-acc: #734ac3;
  --color-tbq23-acc: oklch(0.52 0.18 295);
  --color-tbq23-dot: #b7b5ca;
  --color-tbq23-dot: oklch(0.78 0.03 290);
  --font-tbq23-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tbq23-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-23 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tbq23-slider');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const track = root.querySelector('[data-track]');
  const slides = [...track.children];
  const dots = [...root.querySelectorAll('[data-dot]')];
  const toggle = root.querySelector('[data-toggle]');
  const n = slides.length;
  let i = 0, raf = 0, paused = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const step = () => slides[1].offsetLeft - slides[0].offsetLeft;
  const go = (k) => track.scrollTo({ left: step() * ((k + n) % n) });
  dots.forEach((d, k) => d.addEventListener('click', () => go(k)));
  root.querySelector('[data-prev]').addEventListener('click', () => go(i - 1));
  root.querySelector('[data-next]').addEventListener('click', () => go(i + 1));
  track.addEventListener('scroll', () => {
    cancelAnimationFrame(raf);
    raf = requestAnimationFrame(() => {
      i = Math.round(track.scrollLeft / step());
      dots.forEach((d, k) => d.setAttribute('aria-current', String(k === i)));
    });
  });
  const sync = () => toggle.setAttribute('aria-pressed', String(paused));
  toggle.addEventListener('click', () => { paused = !paused; sync(); });
  sync();
  setInterval(() => { if (!paused && !root.matches(':hover, :focus-within')) go(i + 1); }, 5000);
})();
```
