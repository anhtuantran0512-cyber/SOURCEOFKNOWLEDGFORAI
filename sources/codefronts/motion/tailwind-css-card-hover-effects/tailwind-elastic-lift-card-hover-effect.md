---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-elastic-lift-card-hover-effect/"
title: "Tailwind Elastic Lift Card with Spring Cubic-Bezier"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A coffee card that springs up and overshoots on hover, with an ember glow rising from below."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Elastic Lift Card with Spring Cubic-Bezier
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-elastic-lift-card-hover-effect/

A coffee card that springs up and overshoots on hover, with an ember glow rising from below. One value carries the whole effect, so it earns a @theme entry: --ease-tch07-bounce mints ease-tch07-bounce and three elements share the same spring.
## HTML
```html
<section class="tch-07 w-full min-h-svh grid place-items-center bg-tch07-bg bg-[radial-gradient(circle_at_20%_20%,#ffe7c2_0%,transparent_45%),radial-gradient(circle_at_80%_80%,#ffc9d4_0%,transparent_45%)] font-tch07-mono p-8">
  <article tabindex="0" class="group relative w-[320px] h-[420px] rounded-[28px] overflow-hidden cursor-pointer origin-bottom bg-[linear-gradient(160deg,#1c1410_0%,#3a2618_100%)] text-tch07-ink shadow-[0_10px_25px_rgb(60_30_10/0.25)] transition-[translate,scale,box-shadow] duration-550 ease-tch07-bounce hover:-translate-y-6 hover:scale-104 hover:shadow-[0_40px_60px_rgb(60_30_10/0.4)] focus-visible:-translate-y-6 focus-visible:scale-104 outline-none focus-visible:outline-3 focus-visible:outline-tch07-ember focus-visible:outline-offset-4 motion-reduce:ease-out motion-reduce:hover:scale-100 before:content-[''] before:absolute before:inset-0 before:opacity-0 before:transition-opacity before:duration-500 before:bg-[radial-gradient(circle_at_50%_120%,var(--color-tch07-ember)_0%,transparent_60%)] group-hover:before:opacity-55 group-focus-visible:before:opacity-55">
    <div class="relative z-2 h-full px-8 py-9 flex flex-col justify-between">
      <span class="text-[0.72rem] tracking-[0.32em] uppercase text-tch07-tag">Seasonal Roast</span>
      <div class="font-tch07-display font-black text-[5.5rem] leading-[0.85] transition-transform duration-550 ease-tch07-bounce group-hover:-translate-y-1.5 motion-reduce:transition-none">04</div>
      <div>
        <h2 class="font-tch07-display font-semibold text-[1.9rem] leading-[1.1]">Ember Drip<br>Coffee Co.</h2>
        <p class="text-[0.85rem] leading-[1.6] text-tch07-body max-w-[90%] mt-2">Slow-roasted single origin beans with notes of burnt caramel and stone fruit.</p>
      </div>
    </div>
    <span class="absolute bottom-7 right-7 z-3 size-3.5 rounded-full bg-tch07-ember shadow-[0_0_0_0_rgb(255_138_60/0.6)] transition-[box-shadow] duration-500 group-hover:shadow-[0_0_0_10px_rgb(255_138_60/0)]"></span>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch07-bg: #f4ede4;
  --color-tch07-bg: oklch(0.94 0.014 70);
  --color-tch07-ink: #f4ede4;
  --color-tch07-ink: oklch(0.94 0.014 70);
  --color-tch07-body: #cdb9a6;
  --color-tch07-body: oklch(0.79 0.03 65);
  --color-tch07-tag: #ffb27a;
  --color-tch07-tag: oklch(0.82 0.11 55);
  --color-tch07-ember: #ff8a3c;
  --color-tch07-ember: oklch(0.74 0.17 48);
  --font-tch07-mono: 'Spline Sans Mono', ui-monospace, monospace;
  --font-tch07-display: 'Fraunces', Georgia, serif;
  --ease-tch07-bounce: cubic-bezier(0.34, 1.8, 0.4, 1);
}

.tch-07 {
  width: 100%;
  min-height: 100svh;
}
```
