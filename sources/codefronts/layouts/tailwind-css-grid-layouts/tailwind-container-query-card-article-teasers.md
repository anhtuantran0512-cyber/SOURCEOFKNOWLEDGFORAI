---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-container-query-card-article-teasers/"
title: "Tailwind Container Query Card for Reusable Article Teasers"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "One article teaser, two layouts — decided by the card's own width."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Container Query Card for Reusable Article Teasers
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-container-query-card-article-teasers/

One article teaser, two layouts — decided by the card's own width. Dropped in the main column it goes horizontal with a wide photo; the identical markup in the sidebar stacks. In v4 the container query is core syntax.
## HTML
```html
<section class="tgx-20 w-full min-h-svh bg-tgx20-bg font-tgx20-sans p-6">
  <div class="grid grid-cols-[minmax(0,2fr)_minmax(0,1fr)] max-md:grid-cols-[minmax(0,1fr)] gap-5">
    <main class="flex flex-col gap-2.5">
      <p class="font-tgx20-mono text-[0.66rem] text-tgx20-mut">main · wide container → horizontal</p>
      <div class="@container/card">
        <article class="grid [grid-template-areas:'media'_'body'] @md/card:[grid-template-areas:'media_body'] @md/card:grid-cols-[150px_minmax(0,1fr)] rounded-2xl overflow-hidden bg-white border border-tgx20-edge shadow-[0_12px_28px_-22px_oklch(0.45_0.05_45/0.9)]">
          <div class="[grid-area:media] relative min-h-[130px] @md/card:min-h-full bg-tgx20-cell">
            <img src="https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?w=500&h=500&q=80&auto=format&fit=crop" alt="Trail winding through coastal pine woodland" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
          </div>
          <div class="[grid-area:body] p-4 flex flex-col gap-2">
            <p class="text-[0.64rem] font-semibold tracking-[0.14em] uppercase text-tgx20-link">Trail guide</p>
            <h3 class="text-[clamp(0.92rem,4.5cqi,1.2rem)] font-semibold text-tgx20-ink leading-[1.25]">The coast path, in three days</h3>
            <p class="text-[0.8rem] leading-[1.55] text-tgx20-mut">Same markup, same stylesheet. The card asked its container — not the viewport — how much room it has, and chose the horizontal arrangement.</p>
            <a href="#0" class="mt-auto inline-flex items-center gap-1 min-h-11 text-[0.8rem] font-semibold text-tgx20-link no-underline hover:underline underline-offset-4 focus-visible:outline-2 focus-visible:outline-tgx20-link focus-visible:outline-offset-2 rounded">Read guide <span aria-hidden="true">→</span></a>
          </div>
        </article>
      </div>
    </main>
    <aside class="flex flex-col gap-2.5">
      <p class="font-tgx20-mono text-[0.66rem] text-tgx20-mut">aside · narrow → stacked</p>
      <div class="@container/card">
        <article class="grid [grid-template-areas:'media'_'body'] @md/card:[grid-template-areas:'media_body'] @md/card:grid-cols-[150px_minmax(0,1fr)] rounded-2xl overflow-hidden bg-white border border-tgx20-edge shadow-[0_12px_28px_-22px_oklch(0.45_0.05_45/0.9)]">
          <div class="[grid-area:media] relative min-h-[130px] @md/card:min-h-full bg-tgx20-cell">
            <img src="https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?w=500&h=500&q=80&auto=format&fit=crop" alt="Trail winding through coastal pine woodland" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
          </div>
          <div class="[grid-area:body] p-4 flex flex-col gap-2">
            <p class="text-[0.64rem] font-semibold tracking-[0.14em] uppercase text-tgx20-link">Trail guide</p>
            <h3 class="text-[clamp(0.92rem,4.5cqi,1.2rem)] font-semibold text-tgx20-ink leading-[1.25]">The coast path, in three days</h3>
            <p class="text-[0.8rem] leading-[1.55] text-tgx20-mut">Identical component, adapted by its container.</p>
            <a href="#0" class="mt-auto inline-flex items-center gap-1 min-h-11 text-[0.8rem] font-semibold text-tgx20-link no-underline hover:underline underline-offset-4 focus-visible:outline-2 focus-visible:outline-tgx20-link focus-visible:outline-offset-2 rounded">Read guide <span aria-hidden="true">→</span></a>
          </div>
        </article>
      </div>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx20-bg: #faf4ee;
  --color-tgx20-bg: oklch(0.965 0.012 60);
  --color-tgx20-cell: #eadfd3;
  --color-tgx20-cell: oklch(0.9 0.02 60);
  --color-tgx20-edge: #e7cdb6;
  --color-tgx20-edge: oklch(0.87 0.05 60);
  --color-tgx20-ink: #3a2a1e;
  --color-tgx20-ink: oklch(0.3 0.04 45);
  --color-tgx20-mut: #6b5648;
  --color-tgx20-mut: oklch(0.47 0.03 45);
  --color-tgx20-link: #a1481f;
  --color-tgx20-link: oklch(0.52 0.15 40);
  --font-tgx20-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tgx20-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tgx-20 {
  width: 100%;
  min-height: 100svh;
}
```
