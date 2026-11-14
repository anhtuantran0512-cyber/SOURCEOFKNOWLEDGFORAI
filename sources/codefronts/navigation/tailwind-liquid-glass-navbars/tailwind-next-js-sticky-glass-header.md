---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-next-js-sticky-glass-header/"
title: "Tailwind Next.js Sticky Glass Header"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "The SSR-safe header: it ships its final glass state in the server-rendered HTML, then deepens the frost past the hero."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Next.js Sticky Glass Header
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-next-js-sticky-glass-header/

The SSR-safe header: it ships its final glass state in the server-rendered HTML, then deepens the frost past the hero. The port is the strongest argument for utilities in a Next.js app &mdash; because the class strings are static and complete, the first painted frame already matches the hydrated one, and the scroll enhancement is one data-scrolled attribute.
## HTML
```html
<section class="nbtw-09 relative block w-full min-h-svh overflow-hidden font-nb09-sans bg-[#0b0b10]" aria-label="Next.js sticky glass header demo">
  <div class="absolute inset-0 overflow-y-auto" id="nbtw-09-scroll">
    <header class="sticky top-0 z-[6] flex flex-wrap items-center gap-x-4.5 gap-y-3 px-5 py-3.5 text-white bg-[rgba(20,20,28,.35)] border-b border-white/[0.08] backdrop-blur-[10px] backdrop-saturate-[1.4] shadow-none transition-[background-color,backdrop-filter,box-shadow,border-color] duration-300 data-[scrolled=true]:bg-[rgba(14,14,20,.72)] data-[scrolled=true]:border-white/[0.14] data-[scrolled=true]:backdrop-blur-[22px] data-[scrolled=true]:backdrop-saturate-[1.7] data-[scrolled=true]:shadow-[0_14px_34px_-20px_rgba(0,0,0,.8)] motion-reduce:transition-none" id="nbtw-09-bar" data-scrolled="false">
      <a class="text-base font-extrabold no-underline text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-09">▲ next-glass</a>
      <nav class="flex gap-0.5 ms-auto" aria-label="Primary">
        <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-white/[0.78] text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/10 hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 aria-[current=page]:bg-white/10 aria-[current=page]:text-white" href="#nbtw-09" aria-current="page">Home</a>
        <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-white/[0.78] text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/10 hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-09">Showcase</a>
        <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-white/[0.78] text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/10 hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-09">Docs</a>
      </nav>
      <button class="min-h-10 px-4.5 rounded-[10px] border-0 bg-white text-[#0b0b10] text-sm font-bold cursor-pointer focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" type="button">Deploy</button>
    </header>
    <div class="h-75 grid place-items-center bg-[radial-gradient(circle_at_50%_30%,#2a2350,#0b0b10_70%)]">
      <h2 class="px-5 text-center text-white text-2xl font-extrabold">Scroll — the header deepens</h2>
    </div>
    <p class="max-w-[46ch] mx-auto p-6 text-[15px] leading-[1.7] text-white/[0.82]">Server-rendered glass state means no flash of an unstyled transparent bar on hydration. The class strings are static literals, so the first frame the browser paints is the finished header.</p>
    <p class="max-w-[46ch] mx-auto p-6 text-[15px] leading-[1.7] text-white/[0.82]">Past the hero the frost, tint, border and shadow intensify — four <code>data-[scrolled=true]:</code> utilities on the same element, not a second rule that has to out-specify the first.</p>
    <p class="max-w-[46ch] mx-auto p-6 text-[15px] leading-[1.7] text-white/[0.82]">In Next.js the header is a Client Component wrapping only the scroll flag. Because the flag is an attribute, that component holds no visual knowledge at all.</p>
    <p class="max-w-[46ch] mx-auto p-6 text-[15px] leading-[1.7] text-white/[0.82]"><code>sticky top-0</code> keeps CLS at 0 — the header reserves its box before scroll begins, so nothing shifts when the tint deepens past 120px.</p>
    <p class="max-w-[46ch] mx-auto p-6 text-[15px] leading-[1.7] text-white/[0.82]">The handler is <code>requestAnimationFrame</code>-throttled so the attribute write stays inside a frame — INP-friendly even on mid-tier Android.</p>
    <p class="max-w-[46ch] mx-auto p-6 text-[15px] leading-[1.7] text-white/[0.82]">Scroll back up: below 120px the attribute flips to false and the header returns to its light glass state through the same four transitions.</p>
    <p class="max-w-[46ch] mx-auto p-6 text-[15px] leading-[1.7] text-white/[0.82]">Nothing in the transition list is a layout property, which is what keeps the deepening free of reflow.</p>
    <p class="max-w-[46ch] mx-auto p-6 text-[15px] leading-[1.7] text-white/[0.82]">That is the whole recipe: one attribute, two tiers, four transitions, zero flash on hydration.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb09-sans: system-ui, 'Segoe UI', sans-serif;
}
```

## JavaScript
```js
(() => {
  const scroll = document.querySelector('#nbtw-09-scroll');
  const bar = document.querySelector('#nbtw-09-bar');
  if (!scroll || !bar) return;
  let ticking = false;
  scroll.addEventListener('scroll', () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      bar.dataset.scrolled = String(scroll.scrollTop > 120);
      ticking = false;
    });
  }, { passive: true });
})();
```
