---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-3d-hover-flip-card-grid/"
title: "Tailwind 3D Hover Flip Card Grid"
section: "layouts"
category: "tailwind-card-grid-layout"
category_name: "Tailwind Card Grid Layouts"
description: "A flashcard wall where hovering a tile rotates it 180&deg; to reveal an accent-coloured back face of metrics, and the grid never shifts because only a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Hover Flip Card Grid
Source: https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-3d-hover-flip-card-grid/

A flashcard wall where hovering a tile rotates it 180&deg; to reveal an accent-coloured back face of metrics, and the grid never shifts because only a transform animates. v4 ships perspective-*, transform-3d, backface-hidden and rotate-y-* as real utilities, so the entire 3D scene is expressible without touching the stylesheet.
## HTML
```html
<section class="tcg-06 w-full min-h-svh bg-tcg06-bg font-tcg06-sans text-white px-6 py-12" aria-label="3D hover flip card grid demo">
  <div class="max-w-[780px] mx-auto grid [grid-template-columns:repeat(auto-fit,minmax(160px,1fr))] gap-5">

    <div class="group perspective-[1000px] h-40">
      <div class="relative w-full h-full transform-3d transition-transform duration-600 ease-tcg06 rotate-y-180 group-hover:rotate-y-0 group-focus-within:rotate-y-0 motion-reduce:transition-none motion-reduce:rotate-y-0">
        <div class="absolute inset-0 flex flex-col justify-end gap-1.5 p-4.5 rounded-[14px] backface-hidden border border-white/10 bg-tcg06-face">
          <span class="text-[.7rem] font-semibold tracking-[0.1em] uppercase text-tcg06-dim">Latency</span>
          <h3 class="text-[1.2rem] font-bold">API</h3>
        </div>
        <div style="--accent:#7c6af7" class="absolute inset-0 flex flex-col justify-end gap-1 p-4.5 rounded-[14px] backface-hidden rotate-y-180 bg-[var(--accent)] text-tcg06-bg">
          <span class="text-[1.5rem] font-extrabold tracking-[-0.02em] tabular-nums">42ms</span>
          <p class="text-[.78rem] font-semibold opacity-80">p95 response time</p>
        </div>
      </div>
    </div>

    <div class="group perspective-[1000px] h-40">
      <div class="relative w-full h-full transform-3d transition-transform duration-600 ease-tcg06 group-hover:rotate-y-180 group-focus-within:rotate-y-180 motion-reduce:transition-none motion-reduce:group-hover:rotate-y-0">
        <div class="absolute inset-0 flex flex-col justify-end gap-1.5 p-4.5 rounded-[14px] backface-hidden border border-white/10 bg-tcg06-face">
          <span class="text-[.7rem] font-semibold tracking-[0.1em] uppercase text-tcg06-dim">Uptime</span>
          <h3 class="text-[1.2rem] font-bold">SLA</h3>
        </div>
        <div style="--accent:#00c2a8" class="absolute inset-0 flex flex-col justify-end gap-1 p-4.5 rounded-[14px] backface-hidden rotate-y-180 bg-[var(--accent)] text-tcg06-bg">
          <span class="text-[1.5rem] font-extrabold tracking-[-0.02em] tabular-nums">99.98%</span>
          <p class="text-[.78rem] font-semibold opacity-80">last 90 days</p>
        </div>
      </div>
    </div>

    <div class="group perspective-[1000px] h-40">
      <div class="relative w-full h-full transform-3d transition-transform duration-600 ease-tcg06 group-hover:rotate-y-180 group-focus-within:rotate-y-180 motion-reduce:transition-none motion-reduce:group-hover:rotate-y-0">
        <div class="absolute inset-0 flex flex-col justify-end gap-1.5 p-4.5 rounded-[14px] backface-hidden border border-white/10 bg-tcg06-face">
          <span class="text-[.7rem] font-semibold tracking-[0.1em] uppercase text-tcg06-dim">Throughput</span>
          <h3 class="text-[1.2rem] font-bold">Requests</h3>
        </div>
        <div style="--accent:#ff6b9d" class="absolute inset-0 flex flex-col justify-end gap-1 p-4.5 rounded-[14px] backface-hidden rotate-y-180 bg-[var(--accent)] text-tcg06-bg">
          <span class="text-[1.5rem] font-extrabold tracking-[-0.02em] tabular-nums">12k/s</span>
          <p class="text-[.78rem] font-semibold opacity-80">peak sustained</p>
        </div>
      </div>
    </div>

    <div class="group perspective-[1000px] h-40">
      <div class="relative w-full h-full transform-3d transition-transform duration-600 ease-tcg06 group-hover:rotate-y-180 group-focus-within:rotate-y-180 motion-reduce:transition-none motion-reduce:group-hover:rotate-y-0">
        <div class="absolute inset-0 flex flex-col justify-end gap-1.5 p-4.5 rounded-[14px] backface-hidden border border-white/10 bg-tcg06-face">
          <span class="text-[.7rem] font-semibold tracking-[0.1em] uppercase text-tcg06-dim">Storage</span>
          <h3 class="text-[1.2rem] font-bold">Database</h3>
        </div>
        <div style="--accent:#ffb454" class="absolute inset-0 flex flex-col justify-end gap-1 p-4.5 rounded-[14px] backface-hidden rotate-y-180 bg-[var(--accent)] text-tcg06-bg">
          <span class="text-[1.5rem] font-extrabold tracking-[-0.02em] tabular-nums">4.2TB</span>
          <p class="text-[.78rem] font-semibold opacity-80">across all shards</p>
        </div>
      </div>
    </div>

  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcg06-bg: #0d0d12;
  --color-tcg06-bg: oklch(0.15 0.006 285);
  --color-tcg06-face: #16161d;
  --color-tcg06-face: oklch(0.2 0.008 285);
  --color-tcg06-dim: #a1a1b0;
  --color-tcg06-dim: oklch(0.72 0.01 285);
  --font-tcg06-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tcg06: cubic-bezier(0.4, 0.2, 0.2, 1);
}
/* Root rule: the full-bleed contract. */

.tcg-06 {
  width: 100%;
  min-height: 100svh;
}

.tcg-06 ::selection {
  background: #7c6af7;
  color: #fff;
}
```
