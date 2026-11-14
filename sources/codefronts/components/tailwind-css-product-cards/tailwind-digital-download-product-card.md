---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-digital-download-product-card/"
title: "Tailwind Digital Download Product Card"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "For products with no photograph: a big file-type wordmark on a gradient, a rating line, a meta row of pills (format, size, version) and a download button…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Digital Download Product Card
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-digital-download-product-card/

For products with no photograph: a big file-type wordmark on a gradient, a rating line, a meta row of pills (format, size, version) and a download button whose arrow nudges down on hover. The whole micro-animation is group-hover:translate-y-[3px] on the glyph, and the gradient badge is one bg-linear-[…].
## HTML
```html
<section class="tpc-15 w-full min-h-svh grid place-items-center bg-tpc15-bg font-tpc15-sans px-5 py-12" aria-label="Digital download product card demo">
  <article class="w-[min(340px,100%)] rounded-[18px] overflow-hidden bg-tpc15-card shadow-[0_16px_40px_-22px_oklch(0.25_0.04_300/0.4)]">
    <div role="img" aria-label="Preview: the UI kit open on a designer's workstation" class="relative aspect-[16/9] grid place-items-center bg-[url('https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=800&h=450&fit=crop&q=70')] bg-cover bg-center">
      <span aria-hidden="true" class="absolute inset-0 bg-linear-[135deg,color-mix(in_oklch,var(--color-tpc15-g1)_82%,transparent),color-mix(in_oklch,var(--color-tpc15-g2)_78%,transparent)]"></span>
      <span aria-hidden="true" class="relative font-tpc15-mono text-[40px] font-extrabold leading-none tracking-[0.06em] text-tpc15-onacc [text-shadow:0_2px_12px_oklch(0.2_0.05_300/0.45)]">.ZIP</span>
    </div>
    <div class="px-5.5 pt-5 pb-5.5">
      <h3 class="text-[18px] font-semibold leading-[1.35] text-tpc15-ink text-pretty">Nimbus UI Kit &mdash; 240 Components</h3>
      <p class="mt-2.5 text-[13px] text-tpc15-mut" aria-label="Rated 4.9 out of 5 from 860 reviews"><span aria-hidden="true" class="text-tpc15-star tracking-[0.05em]">&#9733;&#9733;&#9733;&#9733;&#9733;</span> 4.9 &middot; 860 reviews</p>
      <ul class="mt-3.5 flex flex-wrap gap-2 list-none">
        <li class="px-2.5 py-1.25 rounded-lg bg-tpc15-chip text-tpc15-chipink text-[12px] font-medium">Figma + Sketch</li>
        <li class="px-2.5 py-1.25 rounded-lg bg-tpc15-chip text-tpc15-chipink text-[12px] font-medium tabular-nums">48&nbsp;MB</li>
        <li class="px-2.5 py-1.25 rounded-lg bg-tpc15-chip text-tpc15-chipink text-[12px] font-medium tabular-nums">v3.2</li>
      </ul>
      <div class="mt-4.5 flex flex-wrap items-center justify-between gap-3">
        <p class="text-[22px] font-extrabold text-tpc15-ink tabular-nums">$39</p>
        <a href="#" download class="group inline-flex items-center gap-2 min-h-11 h-11.5 px-5.5 rounded-xl no-underline bg-tpc15-acc text-tpc15-onacc text-[14px] font-bold shadow-[0_10px_24px_-12px_var(--color-tpc15-acc)] transition-colors duration-150 hover:bg-tpc15-acc2 focus-visible:outline-3 focus-visible:outline-tpc15-ring focus-visible:outline-offset-2 motion-reduce:transition-none">
          <span aria-hidden="true" class="inline-block transition-transform duration-300 group-hover:translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0">&darr;</span> Download
        </a>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc15-bg: #f2f1f7;
  --color-tpc15-bg: oklch(0.95 0.008 300);
  --color-tpc15-card: #ffffff;
  --color-tpc15-card: oklch(1 0 0);
  --color-tpc15-ink: #1a1330;
  --color-tpc15-ink: oklch(0.23 0.04 300);
  --color-tpc15-mut: #5d5578;
  --color-tpc15-mut: oklch(0.48 0.035 300);
  --color-tpc15-chip: #f2f0f8;
  --color-tpc15-chip: oklch(0.96 0.01 300);
  --color-tpc15-chipink: #4a4266;
  --color-tpc15-chipink: oklch(0.42 0.04 300);
  --color-tpc15-g1: #8b5cf0;
  --color-tpc15-g1: oklch(0.6 0.18 295);
  --color-tpc15-g2: #4f6ae0;
  --color-tpc15-g2: oklch(0.55 0.17 268);
  --color-tpc15-acc: #6b3fd4;
  --color-tpc15-acc: oklch(0.5 0.19 292);
  --color-tpc15-acc2: #5a33b8;
  --color-tpc15-acc2: oklch(0.44 0.18 292);
  --color-tpc15-star: #d8a01f;
  --color-tpc15-star: oklch(0.75 0.14 82);
  --color-tpc15-ring: #c3a9f2;
  --color-tpc15-ring: oklch(0.78 0.1 292);
  --color-tpc15-onacc: #ffffff;
  --color-tpc15-onacc: oklch(1 0 0);
  --font-tpc15-sans: 'Manrope', system-ui, sans-serif;
  --font-tpc15-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tpc-15 {
  width: 100%;
  min-height: 100svh;
}

.tpc-15 ::selection {
  background: var(--color-tpc15-acc);
  color: #fff;
}
```
