---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-glassmorphism-product-card/"
title: "Tailwind Glassmorphism Product Card"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "Frosted glass, and Tailwind ships nearly all of it as core utilities: backdrop-blur-lg, backdrop-saturate-150, an alpha-white fill and a hairline alpha border."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Product Card
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-glassmorphism-product-card/

Frosted glass, and Tailwind ships nearly all of it as core utilities: backdrop-blur-lg, backdrop-saturate-150, an alpha-white fill and a hairline alpha border. The only arbitrary values left are the composed outer+inset shadow and the bright top-edge highlight — the two parts that actually sell the pane of glass.
## HTML
```html
<section class="tpc-07 w-full min-h-svh grid place-items-center font-tpc07-sans px-5 py-14 bg-[radial-gradient(50%_60%_at_15%_20%,oklch(0.7_0.2_20/0.9),transparent_60%),radial-gradient(50%_60%_at_85%_30%,oklch(0.72_0.2_260/0.9),transparent_60%),radial-gradient(60%_70%_at_60%_90%,oklch(0.75_0.19_180/0.85),transparent_60%),linear-gradient(135deg,oklch(0.28_0.09_300),oklch(0.18_0.06_285))]" aria-label="Glassmorphism product card demo">
  <article class="relative w-[19.375rem] max-w-full p-5.5 rounded-[22px] overflow-hidden bg-white/14 backdrop-blur-lg backdrop-saturate-150 border border-white/30 shadow-[0_30px_60px_-30px_oklch(0_0_0/0.5),inset_0_1px_0_oklch(1_0_0/0.4)] transition-[translate,box-shadow,border-color] duration-400 hover:-translate-y-1 hover:border-white/45 hover:shadow-[0_40px_70px_-30px_oklch(0_0_0/0.6),inset_0_1px_0_oklch(1_0_0/0.5)] focus-within:-translate-y-1 focus-within:border-white/45 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
    <span aria-hidden="true" class="absolute top-0 inset-x-[12%] h-px bg-linear-[90deg,transparent,oklch(1_0_0/0.8),transparent]"></span>
    <div role="img" aria-label="Product photo: Prism smart lamp" class="aspect-[16/10] rounded-[14px] border border-white/20 bg-linear-[135deg,oklch(1_0_0/0.3),oklch(1_0_0/0.08)] bg-[url('https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?w=800&h=500&fit=crop&q=70')] bg-cover bg-center"></div>
    <p class="mt-4 font-tpc07-mono text-[11px] tracking-[0.2em] uppercase text-white/80">New drop</p>
    <h3 class="mt-1.5 text-[20px] font-bold text-white [text-shadow:0_1px_6px_oklch(0_0_0/0.25)]">Prism Smart Lamp</h3>
    <p class="mt-1.5 text-[13.5px] leading-[1.5] text-white/85 text-pretty">16M colours, app-controlled, ambient sync.</p>
    <div class="mt-4.5 flex items-center justify-between gap-3">
      <p class="text-[22px] font-extrabold text-white tabular-nums">$89</p>
      <button type="button" class="min-h-11 h-11 px-5.5 rounded-xl border border-white/50 bg-white/90 text-tpc07-ink text-sm font-bold cursor-pointer transition-colors duration-200 hover:bg-white focus-visible:outline-3 focus-visible:outline-white/80 focus-visible:outline-offset-2 motion-reduce:transition-none">Add to Cart</button>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc07-ink: #241844;
  --color-tpc07-ink: oklch(0.25 0.08 295);
  --font-tpc07-sans: 'Outfit', system-ui, sans-serif;
  --font-tpc07-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tpc-07 {
  width: 100%;
  min-height: 100svh;
}

.tpc-07 ::selection {
  background: oklch(1 0 0 / 0.85);
  color: var(--color-tpc07-ink);
}
```
