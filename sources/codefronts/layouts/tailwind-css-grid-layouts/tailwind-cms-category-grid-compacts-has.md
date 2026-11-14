---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-cms-category-grid-compacts-has/"
title: "Tailwind CMS Category Grid that Compacts Itself with has()"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A blog's topic index that re-designs itself by count: three topics render as feature cards with descriptions and post counts; add a fifth and the same list…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CMS Category Grid that Compacts Itself with has()
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-cms-category-grid-compacts-has/

A blog's topic index that re-designs itself by count: three topics render as feature cards with descriptions and post counts; add a fifth and the same list compacts into a chip wall. One class list, no JavaScript, no editor training.
## HTML
```html
<section class="tgx-12 w-full min-h-svh bg-tgx12-coal font-tgx12-sans p-6 flex flex-col gap-4">
  <header class="flex flex-col gap-1">
    <p class="font-tgx12-mono text-[0.66rem] tracking-[0.16em] uppercase text-tgx12-amber">Fieldnotes · Topics</p>
    <h2 class="text-[1.3rem] font-semibold text-white tracking-[-0.01em]">Browse by topic</h2>
  </header>
  <div class="flex flex-col gap-2">
    <p class="text-[0.75rem] text-tgx12-dim">Featured collections <span class="text-tgx12-amber">· 3 items → roomy cards</span></p>
    <ul class="list-none grid gap-3 grid-cols-[repeat(auto-fit,minmax(min(220px,100%),1fr))] *:flex *:flex-col *:gap-1.5 *:rounded-xl *:border *:border-tgx12-edge *:bg-tgx12-card *:p-4 has-[>*:nth-child(5)]:gap-2 has-[>*:nth-child(5)]:grid-cols-[repeat(auto-fit,minmax(min(116px,100%),1fr))] has-[>*:nth-child(5)]:*:p-2.5 has-[>*:nth-child(5)]:*:items-center has-[>*:nth-child(5)]:*:text-center has-[>*:nth-child(5)]:*:justify-center">
      <li><strong class="text-[0.95rem] font-semibold text-tgx12-amber">Layout</strong><span class="text-[0.78rem] leading-[1.5] text-tgx12-dim">Grid, subgrid and the geometry of a page.</span><span class="mt-1 text-[0.7rem] tabular-nums text-tgx12-faint">24 posts</span></li>
      <li><strong class="text-[0.95rem] font-semibold text-tgx12-amber">Typography</strong><span class="text-[0.78rem] leading-[1.5] text-tgx12-dim">Measure, rhythm and the case against 16px everywhere.</span><span class="mt-1 text-[0.7rem] tabular-nums text-tgx12-faint">18 posts</span></li>
      <li><strong class="text-[0.95rem] font-semibold text-tgx12-amber">Performance</strong><span class="text-[0.78rem] leading-[1.5] text-tgx12-dim">Shipping less, measuring honestly.</span><span class="mt-1 text-[0.7rem] tabular-nums text-tgx12-faint">31 posts</span></li>
    </ul>
  </div>
  <div class="flex flex-col gap-2">
    <p class="text-[0.75rem] text-tgx12-dim">All topics <span class="text-tgx12-amber">· 8 items → the same list compacts</span></p>
    <ul class="list-none grid gap-3 grid-cols-[repeat(auto-fit,minmax(min(220px,100%),1fr))] *:flex *:flex-col *:gap-1.5 *:rounded-xl *:border *:border-tgx12-edge *:bg-tgx12-card *:p-4 has-[>*:nth-child(5)]:gap-2 has-[>*:nth-child(5)]:grid-cols-[repeat(auto-fit,minmax(min(116px,100%),1fr))] has-[>*:nth-child(5)]:*:p-2.5 has-[>*:nth-child(5)]:*:items-center has-[>*:nth-child(5)]:*:text-center has-[>*:nth-child(5)]:*:justify-center">
      <li><strong class="text-[0.8rem] font-semibold text-tgx12-amber">Layout</strong><span class="text-[0.68rem] tabular-nums text-tgx12-faint">24</span></li>
      <li><strong class="text-[0.8rem] font-semibold text-tgx12-amber">Typography</strong><span class="text-[0.68rem] tabular-nums text-tgx12-faint">18</span></li>
      <li><strong class="text-[0.8rem] font-semibold text-tgx12-amber">Performance</strong><span class="text-[0.68rem] tabular-nums text-tgx12-faint">31</span></li>
      <li><strong class="text-[0.8rem] font-semibold text-tgx12-amber">Accessibility</strong><span class="text-[0.68rem] tabular-nums text-tgx12-faint">22</span></li>
      <li><strong class="text-[0.8rem] font-semibold text-tgx12-amber">Tooling</strong><span class="text-[0.68rem] tabular-nums text-tgx12-faint">14</span></li>
      <li><strong class="text-[0.8rem] font-semibold text-tgx12-amber">Colour</strong><span class="text-[0.68rem] tabular-nums text-tgx12-faint">9</span></li>
      <li><strong class="text-[0.8rem] font-semibold text-tgx12-amber">Motion</strong><span class="text-[0.68rem] tabular-nums text-tgx12-faint">11</span></li>
      <li><strong class="text-[0.8rem] font-semibold text-tgx12-amber">Process</strong><span class="text-[0.68rem] tabular-nums text-tgx12-faint">7</span></li>
    </ul>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx12-coal: #211d16;
  --color-tgx12-coal: oklch(0.21 0.012 75);
  --color-tgx12-card: #2b261d;
  --color-tgx12-card: oklch(0.26 0.015 75);
  --color-tgx12-edge: #4a4130;
  --color-tgx12-edge: oklch(0.38 0.03 75);
  --color-tgx12-amber: #f0c46a;
  --color-tgx12-amber: oklch(0.83 0.13 80);
  --color-tgx12-dim: #c2b8a5;
  --color-tgx12-dim: oklch(0.8 0.02 80);
  --color-tgx12-faint: #9a9081;
  --color-tgx12-faint: oklch(0.67 0.02 80);
  --font-tgx12-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tgx12-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tgx-12 {
  width: 100%;
  min-height: 100svh;
}
```
