---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-scroll-opacity-sticky-navbar/"
title: "Tailwind Scroll-Opacity Sticky Navbar"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "A navbar that starts fully transparent over a hero and dissolves into frosted glass as you scroll &mdash; continuously, not at a breakpoint."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Scroll-Opacity Sticky Navbar
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-scroll-opacity-sticky-navbar/

A navbar that starts fully transparent over a hero and dissolves into frosted glass as you scroll &mdash; continuously, not at a breakpoint. One registered custom property carries scroll progress from 0 to 1, and four utilities compute the fill, the blur, the border and the text-shadow from it with calc(). There are no transitions in the demo at all: the value is the animation.
## HTML
```html
<section class="nbtw-13 relative block w-full min-h-svh overflow-hidden font-nb13-sans bg-[#0c1418]" aria-label="Scroll opacity sticky navbar demo">
  <div class="absolute inset-0 overflow-y-auto" id="nbtw-13-scroll">
    <header class="sticky top-0 z-[6] flex flex-wrap items-center gap-x-4.5 gap-y-3 px-5.5 py-4 text-white bg-[color-mix(in_oklab,#0e1a22_calc(var(--nb13-p)*82%),transparent)] border-b border-b-[color-mix(in_oklab,white_calc(var(--nb13-p)*22%),transparent)] backdrop-blur-[calc(var(--nb13-p)*22px)] backdrop-saturate-[1.6] [text-shadow:0_2px_10px_rgba(0,0,0,calc(.5-var(--nb13-p)*.5))]" id="nbtw-13-bar" style="--nb13-p:0">
      <a class="text-[17px] font-extrabold no-underline text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-13">☼ Vista</a>
      <nav class="flex gap-0.5 ms-auto" aria-label="Primary">
        <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-white opacity-90 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-white/[0.14] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 aria-[current=page]:opacity-100 aria-[current=page]:bg-white/[0.14]" href="#nbtw-13" aria-current="page">Stays</a>
        <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-white opacity-90 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-white/[0.14] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-13">Trips</a>
        <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-white opacity-90 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-white/[0.14] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-13">Guides</a>
      </nav>
      <button class="min-h-10 px-4.5 rounded-[10px] border border-white/50 bg-white/[0.18] text-white text-sm font-bold cursor-pointer backdrop-blur-[6px] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" type="button">Book</button>
    </header>
    <div class="h-[330px] grid place-items-center bg-[linear-gradient(180deg,rgba(0,0,0,.15),rgba(0,0,0,.4)),url('https://picsum.photos/seed/nb13/1000/700')] bg-center bg-cover">
      <h2 class="px-5 text-center text-white text-[26px] font-extrabold [text-shadow:0_2px_16px_rgba(0,0,0,.5)]">Transparent over the hero</h2>
    </div>
    <p class="max-w-[46ch] mx-auto p-6 text-[15px] leading-[1.7] text-[#dfe7ec]">Scroll and the bar dissolves from fully transparent into frosted glass — fill, blur, border and text-shadow are all <code>calc()</code> functions of one registered <code>--nb13-p</code> property.</p>
    <p class="max-w-[46ch] mx-auto p-6 text-[15px] leading-[1.7] text-[#dfe7ec]">There is no transition anywhere in this demo. A transition would chase a target that moves every frame; a computed value is exact at every scroll offset instead.</p>
    <p class="max-w-[46ch] mx-auto p-6 text-[15px] leading-[1.7] text-[#dfe7ec]">The link text-shadow runs inverse to the frost: full shadow while the bar is transparent over the photograph, none once the glass has arrived.</p>
    <p class="max-w-[46ch] mx-auto p-6 text-[15px] leading-[1.7] text-[#dfe7ec]">The handler is rAF-throttled and clamps to [0,1], because iOS overscroll reports values past both ends and an unclamped multiplier produces invalid colours.</p>
    <p class="max-w-[46ch] mx-auto p-6 text-[15px] leading-[1.7] text-[#dfe7ec]"><code>sticky top-0</code> keeps CLS at 0 — the bar reserves its box in flow and never pushes content as its appearance changes.</p>
    <p class="max-w-[46ch] mx-auto p-6 text-[15px] leading-[1.7] text-[#dfe7ec]">Keep scrolling to reach the fully solidified state; everything completes around the 220px mark, which is the divisor in the handler.</p>
    <p class="max-w-[46ch] mx-auto p-6 text-[15px] leading-[1.7] text-[#dfe7ec]">Now scroll back up. The bar dissolves back to nothing at exactly the same rate, because the fade has no direction of its own.</p>
    <p class="max-w-[46ch] mx-auto p-6 text-[15px] leading-[1.7] text-[#dfe7ec]">One property, six lines of script, zero transitions — the fade is a continuous computed value, not an animation.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb13-sans: system-ui, 'Segoe UI', sans-serif;
}
/* Registering the progress value as a number is what lets the same variable
   multiply into a percentage, a pixel length and an alpha. Unregistered it is
   an untyped string, and calc() with a unit can fail to resolve. */

@property --nb13-p {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
```

## JavaScript
```js
(() => {
  const scroll = document.querySelector('#nbtw-13-scroll');
  const bar = document.querySelector('#nbtw-13-bar');
  if (!scroll || !bar) return;
  let ticking = false;
  scroll.addEventListener('scroll', () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      const p = Math.min(1, Math.max(0, scroll.scrollTop / 220));
      bar.style.setProperty('--nb13-p', p.toFixed(3));
      ticking = false;
    });
  }, { passive: true });
})();
```
