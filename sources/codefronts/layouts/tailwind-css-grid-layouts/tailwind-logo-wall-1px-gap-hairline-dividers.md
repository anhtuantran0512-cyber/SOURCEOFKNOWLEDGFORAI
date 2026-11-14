---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-logo-wall-1px-gap-hairline-dividers/"
title: "Tailwind Logo Wall with 1px Gap Hairline Dividers"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "The 'trusted by' band done properly: hairline dividers that come from a 1px gap over a coloured background, so they never double up and keep working at every…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Logo Wall with 1px Gap Hairline Dividers
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-logo-wall-1px-gap-hairline-dividers/

The 'trusted by' band done properly: hairline dividers that come from a 1px gap over a coloured background, so they never double up and keep working at every column count auto-fit produces.
## HTML
```html
<section class="tgx-29 w-full min-h-svh bg-tgx29-paper font-tgx29-sans px-6 py-10 grid content-center gap-6">
  <header class="flex flex-col items-center gap-2 text-center">
    <h2 class="text-[0.72rem] tracking-[0.2em] uppercase text-tgx29-mut">Powering front-ends at</h2>
    <p class="text-[1.15rem] font-semibold text-tgx29-ink tracking-[-0.01em] max-w-[34ch]">1,400 teams ship on Relay every week</p>
  </header>
  <ul class="list-none grid grid-cols-[repeat(auto-fit,minmax(min(150px,100%),1fr))] gap-px bg-tgx29-hairline border border-tgx29-hairline rounded-xl overflow-hidden w-[min(820px,100%)] mx-auto">
    <li class="bg-tgx29-paper"><a href="#0" class="grid place-items-center min-h-[86px] p-4 no-underline grayscale opacity-60 transition duration-300 hover:grayscale-0 hover:opacity-100 hover:bg-tgx29-hover focus-visible:grayscale-0 focus-visible:opacity-100 focus-visible:bg-tgx29-hover focus-visible:outline-2 focus-visible:outline-tgx29-ink focus-visible:-outline-offset-2 motion-reduce:transition-none"><b class="font-tgx29-serif text-[1.05rem] tracking-[0.02em] text-tgx29-ink">Meridian</b></a></li>
    <li class="bg-tgx29-paper"><a href="#0" class="grid place-items-center min-h-[86px] p-4 no-underline grayscale opacity-60 transition duration-300 hover:grayscale-0 hover:opacity-100 hover:bg-tgx29-hover focus-visible:grayscale-0 focus-visible:opacity-100 focus-visible:bg-tgx29-hover focus-visible:outline-2 focus-visible:outline-tgx29-ink focus-visible:-outline-offset-2 motion-reduce:transition-none"><b class="font-tgx29-mono text-[1.05rem] text-tgx29-ink">hexlab_</b></a></li>
    <li class="bg-tgx29-paper"><a href="#0" class="grid place-items-center min-h-[86px] p-4 no-underline grayscale opacity-60 transition duration-300 hover:grayscale-0 hover:opacity-100 hover:bg-tgx29-hover focus-visible:grayscale-0 focus-visible:opacity-100 focus-visible:bg-tgx29-hover focus-visible:outline-2 focus-visible:outline-tgx29-ink focus-visible:-outline-offset-2 motion-reduce:transition-none"><b class="text-[1.05rem] font-semibold tracking-[0.08em] text-tgx29-ink">NORTHBEAM</b></a></li>
    <li class="bg-tgx29-paper"><a href="#0" class="grid place-items-center min-h-[86px] p-4 no-underline grayscale opacity-60 transition duration-300 hover:grayscale-0 hover:opacity-100 hover:bg-tgx29-hover focus-visible:grayscale-0 focus-visible:opacity-100 focus-visible:bg-tgx29-hover focus-visible:outline-2 focus-visible:outline-tgx29-ink focus-visible:-outline-offset-2 motion-reduce:transition-none"><b class="font-tgx29-serif italic text-[1.05rem] text-tgx29-ink">Foundry &amp; Co.</b></a></li>
    <li class="bg-tgx29-paper"><a href="#0" class="grid place-items-center min-h-[86px] p-4 no-underline grayscale opacity-60 transition duration-300 hover:grayscale-0 hover:opacity-100 hover:bg-tgx29-hover focus-visible:grayscale-0 focus-visible:opacity-100 focus-visible:bg-tgx29-hover focus-visible:outline-2 focus-visible:outline-tgx29-ink focus-visible:-outline-offset-2 motion-reduce:transition-none"><b class="text-[1.05rem] font-medium lowercase tracking-[0.04em] text-tgx29-ink">plexus</b></a></li>
    <li class="bg-tgx29-paper"><a href="#0" class="grid place-items-center min-h-[86px] p-4 no-underline grayscale opacity-60 transition duration-300 hover:grayscale-0 hover:opacity-100 hover:bg-tgx29-hover focus-visible:grayscale-0 focus-visible:opacity-100 focus-visible:bg-tgx29-hover focus-visible:outline-2 focus-visible:outline-tgx29-ink focus-visible:-outline-offset-2 motion-reduce:transition-none"><b class="font-tgx29-mono text-[1.05rem] text-tgx29-ink">[cadence]</b></a></li>
    <li class="bg-tgx29-paper"><a href="#0" class="grid place-items-center min-h-[86px] p-4 no-underline grayscale opacity-60 transition duration-300 hover:grayscale-0 hover:opacity-100 hover:bg-tgx29-hover focus-visible:grayscale-0 focus-visible:opacity-100 focus-visible:bg-tgx29-hover focus-visible:outline-2 focus-visible:outline-tgx29-ink focus-visible:-outline-offset-2 motion-reduce:transition-none"><b class="text-[1.05rem] font-semibold text-tgx29-ink">Waypoint</b></a></li>
    <li class="bg-tgx29-paper"><a href="#0" class="grid place-items-center min-h-[86px] p-4 no-underline grayscale opacity-60 transition duration-300 hover:grayscale-0 hover:opacity-100 hover:bg-tgx29-hover focus-visible:grayscale-0 focus-visible:opacity-100 focus-visible:bg-tgx29-hover focus-visible:outline-2 focus-visible:outline-tgx29-ink focus-visible:-outline-offset-2 motion-reduce:transition-none"><b class="font-tgx29-serif text-[1.05rem] text-tgx29-ink">Aurelia</b></a></li>
  </ul>
  <p class="text-center text-[0.76rem] text-tgx29-mut">Every divider above is a 1px gap over a coloured wall — no borders, no <code class="font-tgx29-mono">:nth-child</code> arithmetic.</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx29-paper: #faf9f6;
  --color-tgx29-paper: oklch(0.975 0.006 90);
  --color-tgx29-hairline: #d8d4cb;
  --color-tgx29-hairline: oklch(0.86 0.012 90);
  --color-tgx29-hover: #f1efe8;
  --color-tgx29-hover: oklch(0.94 0.01 90);
  --color-tgx29-ink: #40382f;
  --color-tgx29-ink: oklch(0.34 0.02 60);
  --color-tgx29-mut: #6f6558;
  --color-tgx29-mut: oklch(0.5 0.02 60);
  --font-tgx29-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tgx29-serif: 'Fraunces', Georgia, serif;
  --font-tgx29-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tgx-29 {
  width: 100%;
  min-height: 100svh;
}
```
