---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-glowing-gradient-glassmorphic-border-card/"
title: "Tailwind Glowing Gradient & Glassmorphic Border Card"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A dark staking-vault card on frosted glass: a teal-to-violet bloom rises behind the blur and a matching neon ring ignites on whichever edge the cursor is…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glowing Gradient & Glassmorphic Border Card
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-glowing-gradient-glassmorphic-border-card/

A dark staking-vault card on frosted glass: a teal-to-violet bloom rises behind the blur and a matching neon ring ignites on whichever edge the cursor is nearest. backdrop-blur-[14px] saturate-[1.3] is a clean utility win; the masked border ring is the part that has to stay arbitrary, and the class list says so honestly.
## HTML
```html
<section class="tch-02 w-full min-h-svh grid place-items-center bg-tch02-bg bg-[radial-gradient(circle_at_25%_25%,#1a1140_0_20%,transparent_21%),radial-gradient(circle_at_80%_70%,#06343f_0_24%,transparent_25%)] font-tch02-sans p-8">
  <article data-tch02="root" class="group relative w-[340px] h-[440px] overflow-hidden rounded-[22px] cursor-pointer bg-white/5 backdrop-blur-[14px] saturate-[1.3] border border-white/10 shadow-[inset_0_0_0_1px_rgb(255_255_255/0.06)] transition-transform duration-400 hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0
    before:content-[''] before:absolute before:inset-0 before:z-0 before:opacity-0 before:transition-opacity before:duration-400 group-hover:before:opacity-100 before:bg-[radial-gradient(320px_circle_at_var(--tch02-x,50%)_var(--tch02-y,50%),rgb(0_240_200/0.35),rgb(120_80_255/0.18)_40%,transparent_65%)]
    after:content-[''] after:absolute after:inset-0 after:z-3 after:rounded-[inherit] after:p-[1.5px] after:pointer-events-none after:opacity-0 after:transition-opacity after:duration-400 group-hover:after:opacity-100 after:bg-[radial-gradient(260px_circle_at_var(--tch02-x,50%)_var(--tch02-y,50%),var(--color-tch02-acc-a),var(--color-tch02-acc-b)_45%,transparent_60%)] after:[-webkit-mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] after:[-webkit-mask-composite:xor] after:[mask-composite:exclude]">
    <div class="relative z-2 h-full p-[2.2rem] flex flex-col justify-between text-tch02-ink">
      <div class="flex items-center justify-between">
        <div class="size-11 rounded-full bg-[conic-gradient(var(--color-tch02-acc-a),var(--color-tch02-acc-b),var(--color-tch02-acc-a))] shadow-[0_0_22px_rgb(0_240_200/0.4)]"></div>
        <span class="font-tch02-mono text-[0.7rem] tracking-[0.16em] text-tch02-mint border border-tch02-mint/35 px-2.5 py-1 rounded-full">// MAINNET</span>
      </div>
      <div>
        <p class="font-tch02-mono text-[0.74rem] tracking-[0.1em] text-tch02-mut">STAKED BALANCE</p>
        <p class="font-bold text-[2.8rem] leading-none bg-linear-to-r from-tch02-acc-a to-tch02-acc-b bg-clip-text text-transparent">48.20 Ξ</p>
      </div>
      <p class="text-[0.84rem] leading-[1.6] text-tch02-mut">Self-custody vault with live yield. The neon edge ignites and follows your cursor around the glass.</p>
      <a href="#" class="block text-center font-tch02-mono text-[0.82rem] tracking-[0.08em] min-h-11 py-3.5 rounded-xl no-underline bg-tch02-acc-a/12 border border-tch02-acc-a/30 text-tch02-btn transition-colors duration-200 hover:bg-tch02-acc-a/22 focus-visible:outline-2 focus-visible:outline-tch02-acc-a focus-visible:outline-offset-2">STAKE MORE →</a>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch02-bg: #06060e;
  --color-tch02-bg: oklch(0.09 0.02 285);
  --color-tch02-ink: #e8f7f4;
  --color-tch02-ink: oklch(0.96 0.02 175);
  --color-tch02-mut: #9aa6bf;
  --color-tch02-mut: oklch(0.71 0.03 265);
  --color-tch02-mint: #7af0db;
  --color-tch02-mint: oklch(0.88 0.11 175);
  --color-tch02-btn: #5ff5d8;
  --color-tch02-btn: oklch(0.89 0.14 175);
  --color-tch02-acc-a: #00f0c8;
  --color-tch02-acc-a: oklch(0.86 0.17 172);
  --color-tch02-acc-b: #7a50ff;
  --color-tch02-acc-b: oklch(0.56 0.25 285);
  --font-tch02-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tch02-mono: 'Azeret Mono', ui-monospace, monospace;
}

.tch-02 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tch-02');
  if (!root) return;
  const card = root.querySelector('[data-tch02="root"]');
  if (!card) return;
  if (!matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  card.addEventListener('mousemove', (e) => {
    const r = card.getBoundingClientRect();
    card.style.setProperty('--tch02-x', '' + (e.clientX - r.left) + 'px');
    card.style.setProperty('--tch02-y', '' + (e.clientY - r.top) + 'px');
  });
})();
```
