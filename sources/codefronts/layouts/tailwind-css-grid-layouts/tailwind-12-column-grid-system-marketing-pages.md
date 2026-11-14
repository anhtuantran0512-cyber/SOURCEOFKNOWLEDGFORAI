---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-12-column-grid-system-marketing-pages/"
title: "Tailwind 12 Column Grid System for Marketing Pages"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A landing page assembled from a real 12-column system — hero, article, sidebar, three features, split CTA — with the design-tool column overlay rendered live…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 12 Column Grid System for Marketing Pages
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-12-column-grid-system-marketing-pages/

A landing page assembled from a real 12-column system — hero, article, sidebar, three features, split CTA — with the design-tool column overlay rendered live behind the content so you can see every span land on its tracks.
## HTML
```html
<section class="tgx-08 w-full min-h-svh bg-tgx08-paper font-tgx08-sans p-6">
  <div class="flex items-center justify-between gap-3 flex-wrap mb-3">
    <p class="font-tgx08-mono text-[0.68rem] tracking-[0.1em] uppercase text-tgx08-mut">Lumen · landing page skeleton</p>
    <p class="font-tgx08-mono text-[0.68rem] text-tgx08-mut">12 tracks · gap 12px · overlay on</p>
  </div>
  <div class="relative rounded-xl border border-tgx08-edge p-[var(--tgx08-gap)] bg-[repeating-linear-gradient(90deg,var(--tgx08-overlay)_0_calc((100%_+_var(--tgx08-gap))/12_-_var(--tgx08-gap)),transparent_calc((100%_+_var(--tgx08-gap))/12_-_var(--tgx08-gap))_calc((100%_+_var(--tgx08-gap))/12))] bg-origin-content bg-clip-content">
    <div class="grid grid-cols-12 gap-[var(--tgx08-gap)]">
      <div class="col-span-12 rounded-xl bg-tgx08-hero text-white p-6 flex flex-col gap-2.5">
        <p class="font-tgx08-mono text-[0.64rem] tracking-[0.16em] uppercase text-tgx08-herodim">span 12 · hero</p>
        <h2 class="text-[clamp(1.4rem,3.4vw,2.1rem)] leading-[1.1] font-semibold tracking-[-0.015em] text-balance">Ship the layout, not the framework</h2>
        <p class="text-[0.88rem] leading-[1.6] text-tgx08-herodim max-w-[54ch]">Twelve tracks, span utilities, and nothing else. The pink ruler behind this page is the same arithmetic your design tool draws.</p>
      </div>
      <article class="col-span-8 max-sm:col-span-12 rounded-xl bg-white border border-tgx08-blockedge p-5 flex flex-col gap-2">
        <p class="font-tgx08-mono text-[0.62rem] uppercase tracking-[0.12em] text-tgx08-indigo">span 8 · article</p>
        <h3 class="text-[1.02rem] font-semibold text-tgx08-ink">Why spans beat breakpoints</h3>
        <p class="text-[0.84rem] leading-[1.6] text-tgx08-mut">A span is a statement about proportion. A breakpoint is a guess about a device. Write the proportion, let the container decide when it stops working, and add exactly one variant.</p>
      </article>
      <aside class="col-span-4 max-sm:col-span-12 rounded-xl bg-tgx08-block border border-tgx08-blockedge p-5 flex flex-col gap-2">
        <p class="font-tgx08-mono text-[0.62rem] uppercase tracking-[0.12em] text-tgx08-indigo">span 4 · sidebar</p>
        <p class="text-[0.84rem] leading-[1.6] text-tgx08-mut">8 + 4 = 12. The row is full, so the next block starts a new one.</p>
      </aside>
      <div class="col-span-4 max-sm:col-span-6 rounded-xl bg-white border border-tgx08-blockedge p-4 flex flex-col gap-1.5">
        <span class="size-7 grid place-items-center rounded-lg bg-tgx08-block text-tgx08-indigo font-tgx08-mono text-[0.8rem]">↯</span>
        <h4 class="text-[0.9rem] font-semibold text-tgx08-ink">Fast by default</h4>
        <p class="text-[0.78rem] leading-[1.55] text-tgx08-mut">No runtime, no layout thrash.</p>
      </div>
      <div class="col-span-4 max-sm:col-span-6 rounded-xl bg-white border border-tgx08-blockedge p-4 flex flex-col gap-1.5">
        <span class="size-7 grid place-items-center rounded-lg bg-tgx08-block text-tgx08-indigo font-tgx08-mono text-[0.8rem]">◫</span>
        <h4 class="text-[0.9rem] font-semibold text-tgx08-ink">Readable spans</h4>
        <p class="text-[0.78rem] leading-[1.55] text-tgx08-mut">The layout is in the markup.</p>
      </div>
      <div class="col-span-4 max-sm:col-span-12 rounded-xl bg-white border border-tgx08-blockedge p-4 flex flex-col gap-1.5">
        <span class="size-7 grid place-items-center rounded-lg bg-tgx08-block text-tgx08-indigo font-tgx08-mono text-[0.8rem]">⇲</span>
        <h4 class="text-[0.9rem] font-semibold text-tgx08-ink">One gap token</h4>
        <p class="text-[0.78rem] leading-[1.55] text-tgx08-mut">Rhythm and ruler stay in sync.</p>
      </div>
      <div class="col-span-6 max-sm:col-span-12 rounded-xl bg-tgx08-block border border-tgx08-blockedge p-5 flex flex-col gap-2">
        <h4 class="text-[0.95rem] font-semibold text-tgx08-ink">Start with the grid</h4>
        <p class="text-[0.8rem] leading-[1.55] text-tgx08-mut">Copy the twelve-track container and build inward.</p>
      </div>
      <div class="col-span-6 max-sm:col-span-12 rounded-xl bg-tgx08-indigo text-white p-5 flex flex-col gap-2 justify-between">
        <h4 class="text-[0.95rem] font-semibold">Get the starter</h4>
        <a href="#0" class="w-fit inline-flex items-center min-h-11 px-4 rounded-lg bg-white text-tgx08-indigo text-[0.82rem] font-semibold no-underline transition-colors hover:bg-tgx08-block focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Download</a>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx08-paper: #f7f6fc;
  --color-tgx08-paper: oklch(0.97 0.008 280);
  --color-tgx08-edge: #ded9ee;
  --color-tgx08-edge: oklch(0.89 0.02 280);
  --color-tgx08-block: #edeafa;
  --color-tgx08-block: oklch(0.94 0.02 280);
  --color-tgx08-blockedge: #cdc6ec;
  --color-tgx08-blockedge: oklch(0.83 0.05 280);
  --color-tgx08-indigo: #5236b8;
  --color-tgx08-indigo: oklch(0.45 0.19 280);
  --color-tgx08-hero: #241a4d;
  --color-tgx08-hero: oklch(0.26 0.1 285);
  --color-tgx08-herodim: #c3bade;
  --color-tgx08-herodim: oklch(0.82 0.04 285);
  --color-tgx08-ink: #2c2545;
  --color-tgx08-ink: oklch(0.29 0.05 285);
  --color-tgx08-mut: #5f5880;
  --color-tgx08-mut: oklch(0.48 0.05 285);
  --font-tgx08-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tgx08-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tgx-08 {
  width: 100%;
  min-height: 100svh;
  --tgx08-gap: 12px;
  --tgx08-overlay: oklch(0.65 0.24 350 / 0.14);
}
```
