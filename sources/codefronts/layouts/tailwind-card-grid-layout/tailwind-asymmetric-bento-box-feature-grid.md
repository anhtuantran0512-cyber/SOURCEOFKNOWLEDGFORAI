---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-asymmetric-bento-box-feature-grid/"
title: "Tailwind Asymmetric Bento Box Feature Grid"
section: "layouts"
category: "tailwind-card-grid-layout"
category_name: "Tailwind Card Grid Layouts"
description: "A dark 4-column bento where one hero tile holds a 2&times;2 block and four smaller tiles flow around it, each ringed by a gradient hairline."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Asymmetric Bento Box Feature Grid
Source: https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-asymmetric-bento-box-feature-grid/

A dark 4-column bento where one hero tile holds a 2&times;2 block and four smaller tiles flow around it, each ringed by a gradient hairline. The gradient border is the whole story of this port: two backgrounds, two clip boxes and a transparent border, expressed as one arbitrary bg-[…padding-box,…border-box] utility that reads its colour from a per-tile --glow.
## HTML
```html
<section class="tcg-02 w-full min-h-svh bg-tcg02-bg font-tcg02-sans text-tcg02-ink px-6 py-12" aria-label="Asymmetric bento box feature grid demo">
  <div class="max-w-[1000px] mx-auto grid grid-cols-4 max-[640px]:grid-cols-2 [grid-auto-rows:140px] gap-4.5">

    <article style="--glow:#7c6af7" class="col-span-2 row-span-2 max-[640px]:row-span-1 flex flex-col justify-end gap-2 p-6 rounded-[20px] border border-transparent [background:linear-gradient(#0f0e18,#0f0e18)_padding-box,linear-gradient(135deg,var(--glow),transparent_70%)_border-box] transition-[translate,box-shadow] duration-300 hover:-translate-y-[3px] hover:shadow-[0_0_0_1px_var(--glow),0_20px_40px_-20px_var(--glow)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="w-8.5 h-8.5 mb-1 rounded-[9px] opacity-90 bg-[var(--glow)]" aria-hidden="true"></div>
      <h3 class="text-[1.4rem] font-bold tracking-[-0.01em]">Real-Time Sync Engine</h3>
      <p class="mt-0.5 text-[.82rem] leading-[1.45] text-tcg02-dim text-pretty">Every change propagates across devices in under 80ms with conflict-free merge resolution.</p>
    </article>

    <article style="--glow:#00d4ff" class="col-span-2 max-[640px]:col-span-1 flex flex-col justify-end gap-2 p-6 rounded-[20px] border border-transparent [background:linear-gradient(#0f0e18,#0f0e18)_padding-box,linear-gradient(135deg,var(--glow),transparent_70%)_border-box] transition-[translate,box-shadow] duration-300 hover:-translate-y-[3px] hover:shadow-[0_0_0_1px_var(--glow),0_20px_40px_-20px_var(--glow)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="w-8.5 h-8.5 mb-1 rounded-[9px] opacity-90 bg-[var(--glow)]" aria-hidden="true"></div>
      <h3 class="text-[1.05rem] font-bold tracking-[-0.01em]">Edge Caching</h3>
      <p class="mt-0.5 text-[.82rem] leading-[1.45] text-tcg02-dim">Global CDN with smart invalidation.</p>
    </article>

    <article style="--glow:#ff6b9d" class="col-span-2 max-[640px]:col-span-1 flex flex-col justify-end gap-2 p-6 rounded-[20px] border border-transparent [background:linear-gradient(#0f0e18,#0f0e18)_padding-box,linear-gradient(135deg,var(--glow),transparent_70%)_border-box] transition-[translate,box-shadow] duration-300 hover:-translate-y-[3px] hover:shadow-[0_0_0_1px_var(--glow),0_20px_40px_-20px_var(--glow)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="w-8.5 h-8.5 mb-1 rounded-[9px] opacity-90 bg-[var(--glow)]" aria-hidden="true"></div>
      <h3 class="text-[1.05rem] font-bold tracking-[-0.01em]">Zero-Config Auth</h3>
      <p class="mt-0.5 text-[.82rem] leading-[1.45] text-tcg02-dim">Drop-in identity, fully managed.</p>
    </article>

    <article style="--glow:#ffd166" class="col-span-2 max-[640px]:col-span-1 flex flex-col justify-end gap-2 p-6 rounded-[20px] border border-transparent [background:linear-gradient(#0f0e18,#0f0e18)_padding-box,linear-gradient(135deg,var(--glow),transparent_70%)_border-box] transition-[translate,box-shadow] duration-300 hover:-translate-y-[3px] hover:shadow-[0_0_0_1px_var(--glow),0_20px_40px_-20px_var(--glow)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="w-8.5 h-8.5 mb-1 rounded-[9px] opacity-90 bg-[var(--glow)]" aria-hidden="true"></div>
      <h3 class="text-[1.05rem] font-bold tracking-[-0.01em]">Usage Insights</h3>
      <p class="mt-0.5 text-[.82rem] leading-[1.45] text-tcg02-dim">Live dashboards, no setup.</p>
    </article>

    <article style="--glow:#34d399" class="col-span-2 max-[640px]:col-span-1 flex flex-col justify-end gap-2 p-6 rounded-[20px] border border-transparent [background:linear-gradient(#0f0e18,#0f0e18)_padding-box,linear-gradient(135deg,var(--glow),transparent_70%)_border-box] transition-[translate,box-shadow] duration-300 hover:-translate-y-[3px] hover:shadow-[0_0_0_1px_var(--glow),0_20px_40px_-20px_var(--glow)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="w-8.5 h-8.5 mb-1 rounded-[9px] opacity-90 bg-[var(--glow)]" aria-hidden="true"></div>
      <h3 class="text-[1.05rem] font-bold tracking-[-0.01em]">Type-Safe SDKs</h3>
      <p class="mt-0.5 text-[.82rem] leading-[1.45] text-tcg02-dim">Generated clients for every stack.</p>
    </article>

  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcg02-bg: #08070d;
  --color-tcg02-bg: oklch(0.13 0.01 285);
  --color-tcg02-tile: #0f0e18;
  --color-tcg02-tile: oklch(0.17 0.02 285);
  --color-tcg02-ink: #f5f5fa;
  --color-tcg02-ink: oklch(0.97 0.004 285);
  --color-tcg02-dim: #a3a3b8;
  --color-tcg02-dim: oklch(0.73 0.02 285);
  --font-tcg02-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract. */

.tcg-02 {
  width: 100%;
  min-height: 100svh;
}

.tcg-02 ::selection {
  background: #7c6af7;
  color: #fff;
}
```
