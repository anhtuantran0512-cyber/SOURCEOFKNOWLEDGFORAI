---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/mobile-swipe-pricing-carousel-tailwind-scroll-snap/"
title: "Mobile Swipe Pricing Carousel with Tailwind Scroll Snap"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "Mobile-first pricing that respects thumbs: cards form a horizontal swipe-and-snap deck with native momentum, peeking neighbours and pagination dots that…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mobile Swipe Pricing Carousel with Tailwind Scroll Snap
Source: https://codefronts.com/components/tailwind-css-pricing-tables/mobile-swipe-pricing-carousel-tailwind-scroll-snap/

Mobile-first pricing that respects thumbs: cards form a horizontal swipe-and-snap deck with native momentum, peeking neighbours and pagination dots that track position live. snap-x snap-mandatory does the physics, an IntersectionObserver only sets data-active and aria-current, and from min-[900px]: the rail relaxes into a normal three-up grid.
## HTML
```html
<section class="tpt-19 w-full min-h-svh grid place-items-center overflow-hidden bg-tpt19-bg bg-[radial-gradient(70%_50%_at_50%_100%,var(--color-tpt19-glow),transparent)] py-16 font-tpt19-sans text-tpt19-ink antialiased" aria-label="Swipeable pricing plans" data-tpt19-root>
  <div class="grid w-full justify-items-center gap-8">
    <h2 class="px-6 text-center text-[clamp(26px,3.8vw,40px)] font-bold tracking-[-0.03em]">Swipe to compare</h2>
    <div data-rail tabindex="0" role="region" aria-label="Pricing plans, scroll horizontally" class="flex w-full snap-x snap-mandatory gap-4 overflow-x-auto px-[max(24px,calc(50vw-170px))] pt-3 pb-6 [scrollbar-width:none] focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpt19-acc min-[900px]:max-w-5xl min-[900px]:justify-center min-[900px]:overflow-visible min-[900px]:px-6 [&::-webkit-scrollbar]:hidden">
      <article data-card class="flex shrink-0 basis-[min(78%,340px)] snap-center scale-94 flex-col gap-2 rounded-3xl border-[1.5px] border-tpt19-line bg-tpt19-card p-7 transition-[scale,border-color,box-shadow] duration-350 data-active:scale-100 data-active:border-tpt19-acc min-[900px]:shrink min-[900px]:basis-72 min-[900px]:scale-100 motion-reduce:transition-none">
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt19-mut uppercase">Mini</h3>
        <p class="text-[44px] leading-tight font-bold tracking-[-0.035em]">$5<small class="text-[15px] font-medium tracking-normal text-tpt19-mut">/mo</small></p>
        <ul class="mt-2 mb-6 grid flex-1 content-start gap-2.5 text-sm text-tpt19-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt19-acc *:before:content-['✓']"><li>1 device</li><li>HD streaming</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl border border-tpt19-line text-sm font-semibold text-tpt19-ink no-underline transition-colors hover:border-tpt19-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt19-acc">Get Mini</a>
      </article>
      <article data-card class="relative flex shrink-0 basis-[min(78%,340px)] snap-center scale-94 flex-col gap-2 rounded-3xl border-[1.5px] border-tpt19-line bg-tpt19-card p-7 transition-[scale,border-color,box-shadow] duration-350 data-active:scale-100 data-active:border-tpt19-acc data-active:shadow-[0_20px_50px_-28px_var(--color-tpt19-acc)] min-[900px]:shrink min-[900px]:basis-72 min-[900px]:scale-100 min-[900px]:border-tpt19-acc motion-reduce:transition-none">
        <span class="absolute -top-3 left-7 rounded-full bg-tpt19-acc px-3 py-1 text-[10.5px] font-bold tracking-[0.08em] text-white uppercase">Most popular</span>
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt19-acc-lite uppercase">Duo</h3>
        <p class="text-[44px] leading-tight font-bold tracking-[-0.035em]">$12<small class="text-[15px] font-medium tracking-normal text-tpt19-mut">/mo</small></p>
        <ul class="mt-2 mb-6 grid flex-1 content-start gap-2.5 text-sm text-tpt19-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt19-acc *:before:content-['✓']"><li>2 devices</li><li>4K streaming</li><li>Offline downloads</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl bg-tpt19-acc text-sm font-semibold text-white no-underline transition hover:brightness-110 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt19-acc">Get Duo</a>
      </article>
      <article data-card class="flex shrink-0 basis-[min(78%,340px)] snap-center scale-94 flex-col gap-2 rounded-3xl border-[1.5px] border-tpt19-line bg-tpt19-card p-7 transition-[scale,border-color,box-shadow] duration-350 data-active:scale-100 data-active:border-tpt19-acc min-[900px]:shrink min-[900px]:basis-72 min-[900px]:scale-100 motion-reduce:transition-none">
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt19-mut uppercase">Family</h3>
        <p class="text-[44px] leading-tight font-bold tracking-[-0.035em]">$19<small class="text-[15px] font-medium tracking-normal text-tpt19-mut">/mo</small></p>
        <ul class="mt-2 mb-6 grid flex-1 content-start gap-2.5 text-sm text-tpt19-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt19-acc *:before:content-['✓']"><li>6 devices</li><li>4K + spatial audio</li><li>Kids profiles</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl border border-tpt19-line text-sm font-semibold text-tpt19-ink no-underline transition-colors hover:border-tpt19-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt19-acc">Get Family</a>
      </article>
    </div>
    <nav aria-label="Plan pager" class="flex items-center gap-3 min-[900px]:hidden">
      <button type="button" data-prev aria-label="Previous plan" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tpt19-line text-tpt19-ink transition-colors hover:border-tpt19-acc disabled:cursor-default disabled:opacity-35 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt19-acc"><svg class="size-4" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 3 5 8l5 5"/></svg></button>
      <div class="flex items-center">
        <button type="button" data-dot aria-label="Plan 1 of 3" aria-current="true" class="grid size-6 cursor-pointer place-items-center before:block before:h-2.5 before:w-2.5 before:rounded-full before:bg-tpt19-dot before:transition-[width,background-color] before:duration-300 before:content-[''] aria-[current=true]:w-9 aria-[current=true]:before:w-6.5 aria-[current=true]:before:bg-tpt19-acc focus-visible:outline-3 focus-visible:outline-tpt19-acc"></button>
        <button type="button" data-dot aria-label="Plan 2 of 3" aria-current="false" class="grid size-6 cursor-pointer place-items-center before:block before:h-2.5 before:w-2.5 before:rounded-full before:bg-tpt19-dot before:transition-[width,background-color] before:duration-300 before:content-[''] aria-[current=true]:w-9 aria-[current=true]:before:w-6.5 aria-[current=true]:before:bg-tpt19-acc focus-visible:outline-3 focus-visible:outline-tpt19-acc"></button>
        <button type="button" data-dot aria-label="Plan 3 of 3" aria-current="false" class="grid size-6 cursor-pointer place-items-center before:block before:h-2.5 before:w-2.5 before:rounded-full before:bg-tpt19-dot before:transition-[width,background-color] before:duration-300 before:content-[''] aria-[current=true]:w-9 aria-[current=true]:before:w-6.5 aria-[current=true]:before:bg-tpt19-acc focus-visible:outline-3 focus-visible:outline-tpt19-acc"></button>
      </div>
      <button type="button" data-next aria-label="Next plan" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tpt19-line text-tpt19-ink transition-colors hover:border-tpt19-acc disabled:cursor-default disabled:opacity-35 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt19-acc"><svg class="size-4" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 3 5 5-5 5"/></svg></button>
    </nav>
    <p aria-hidden="true" class="mx-6 rounded-full border border-white/12 px-3.5 py-2 font-tpt19-mono text-[11.5px] text-tpt19-mut">snap-x snap-mandatory · data-active: · aria-[current=true]:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt19-bg: #161119;
  --color-tpt19-bg: oklch(0.18 0.02 320);
  --color-tpt19-glow: #3d163180;
  --color-tpt19-glow: oklch(0.3 0.08 345 / 0.5);
  --color-tpt19-card: #211a25;
  --color-tpt19-card: oklch(0.225 0.025 320);
  --color-tpt19-line: #3a2f40;
  --color-tpt19-line: oklch(0.33 0.03 320);
  --color-tpt19-dot: #54465c;
  --color-tpt19-dot: oklch(0.42 0.035 320);
  --color-tpt19-ink: #f4eef6;
  --color-tpt19-ink: oklch(0.955 0.01 320);
  --color-tpt19-body: #d6cadd;
  --color-tpt19-body: oklch(0.86 0.025 320);
  --color-tpt19-mut: #ae9cb8;
  --color-tpt19-mut: oklch(0.72 0.04 320);
  --color-tpt19-acc: #e0317a;
  --color-tpt19-acc: oklch(0.6 0.21 355);
  --color-tpt19-acc-lite: #f58ab5;
  --color-tpt19-acc-lite: oklch(0.76 0.14 355);
  --font-tpt19-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tpt19-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-19 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-tpt19-root]').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const rail = root.querySelector('[data-rail]');
    const cards = [...rail.querySelectorAll('[data-card]')];
    const dots = [...root.querySelectorAll('[data-dot]')];
    const prev = root.querySelector('[data-prev]');
    const next = root.querySelector('[data-next]');
    let active = 0;
    const setActive = (i) => {
      active = i;
      cards.forEach((c, j) => c.toggleAttribute('data-active', j === i));
      dots.forEach((d, j) => d.setAttribute('aria-current', j === i ? 'true' : 'false'));
      prev.disabled = i === 0;
      next.disabled = i === cards.length - 1;
    };
    const go = (i) => {
      const c = cards[Math.max(0, Math.min(cards.length - 1, i))];
      /* scroll the rail itself — never scrollIntoView, which can move the page */
      const left = c.offsetLeft - (rail.clientWidth - c.offsetWidth) / 2;
      rail.scrollTo({ left, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
    };
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) setActive(cards.indexOf(e.target)); });
    }, { root: rail, threshold: 0.6 });
    cards.forEach((c) => io.observe(c));
    dots.forEach((d, i) => d.addEventListener('click', () => go(i)));
    prev.addEventListener('click', () => go(active - 1));
    next.addEventListener('click', () => go(active + 1));
    setActive(0);
  });
})();
```
