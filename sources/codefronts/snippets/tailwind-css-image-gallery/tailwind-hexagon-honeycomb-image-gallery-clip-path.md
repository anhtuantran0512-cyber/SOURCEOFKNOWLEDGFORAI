---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-hexagon-honeycomb-image-gallery-clip-path/"
title: "Tailwind Hexagon Honeycomb Image Gallery with clip-path"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "An interlocking honeycomb where square portraits are clipped into hexagons and packed into offset rows with no gaps — the dense geometric grid team pages and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Hexagon Honeycomb Image Gallery with clip-path
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-hexagon-honeycomb-image-gallery-clip-path/

An interlocking honeycomb where square portraits are clipped into hexagons and packed into offset rows with no gaps — the dense geometric grid team pages and portfolios reach for. The port's win is that the hex geometry, the hover zoom and the label reveal all sit on the cell that owns them, so a cell is copy-pasteable in one piece.
## HTML
```html
<section class="tgl-01 w-full min-h-svh grid place-items-center bg-tgl01-bg font-tgl01-sans px-5 py-10 [--hex:132px] max-[520px]:[--hex:96px]" aria-label="Hexagon honeycomb gallery">
  <div class="flex flex-col items-center">
    <div class="flex gap-2">
      <a href="#" class="group relative block w-[var(--hex)] [aspect-ratio:1/1.1547] overflow-hidden bg-tgl01-cell no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] focus-visible:outline-3 focus-visible:outline-tgl01-acc focus-visible:outline-offset-[3px]">
        <img src="https://images.unsplash.com/photo-1483728642387-6c3bdd6c93e5?q=80&w=300&h=300&auto=format&fit=crop" alt="Ava, product designer" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[450ms] group-hover:scale-[1.12] group-focus-visible:scale-[1.12] motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(160deg,var(--color-tgl01-acc),transparent_60%)] opacity-0 transition-opacity duration-300 group-hover:opacity-90 group-focus-visible:opacity-90 motion-reduce:transition-none"></span>
        <span class="absolute inset-x-0 bottom-[22%] z-[2] text-center text-[13px] font-bold tracking-[0.04em] text-white opacity-0 translate-y-1.5 transition-[opacity,translate] duration-300 [text-shadow:0_1px_4px_rgba(0,0,0,0.6)] group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Ava</span>
      </a>
      <a href="#" class="group relative block w-[var(--hex)] [aspect-ratio:1/1.1547] overflow-hidden bg-tgl01-cell no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] focus-visible:outline-3 focus-visible:outline-tgl01-acc focus-visible:outline-offset-[3px]">
        <img src="https://images.unsplash.com/photo-1439853949127-fa647821eba0?q=80&w=300&h=300&auto=format&fit=crop" alt="Liam, engineering lead" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[450ms] group-hover:scale-[1.12] group-focus-visible:scale-[1.12] motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(160deg,var(--color-tgl01-acc),transparent_60%)] opacity-0 transition-opacity duration-300 group-hover:opacity-90 group-focus-visible:opacity-90 motion-reduce:transition-none"></span>
        <span class="absolute inset-x-0 bottom-[22%] z-[2] text-center text-[13px] font-bold tracking-[0.04em] text-white opacity-0 translate-y-1.5 transition-[opacity,translate] duration-300 [text-shadow:0_1px_4px_rgba(0,0,0,0.6)] group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Liam</span>
      </a>
      <a href="#" class="group relative block w-[var(--hex)] [aspect-ratio:1/1.1547] overflow-hidden bg-tgl01-cell no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] focus-visible:outline-3 focus-visible:outline-tgl01-acc focus-visible:outline-offset-[3px]">
        <img src="https://images.unsplash.com/photo-1524805444758-089113d48a6d?q=80&w=300&h=300&auto=format&fit=crop" alt="Noa, research director" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[450ms] group-hover:scale-[1.12] group-focus-visible:scale-[1.12] motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(160deg,var(--color-tgl01-acc),transparent_60%)] opacity-0 transition-opacity duration-300 group-hover:opacity-90 group-focus-visible:opacity-90 motion-reduce:transition-none"></span>
        <span class="absolute inset-x-0 bottom-[22%] z-[2] text-center text-[13px] font-bold tracking-[0.04em] text-white opacity-0 translate-y-1.5 transition-[opacity,translate] duration-300 [text-shadow:0_1px_4px_rgba(0,0,0,0.6)] group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Noa</span>
      </a>
      <a href="#" class="group relative block w-[var(--hex)] [aspect-ratio:1/1.1547] overflow-hidden bg-tgl01-cell no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] focus-visible:outline-3 focus-visible:outline-tgl01-acc focus-visible:outline-offset-[3px]">
        <img src="https://images.unsplash.com/photo-1459749411175-04bf5292ceea?q=80&w=300&h=300&auto=format&fit=crop" alt="Kai, staff engineer" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[450ms] group-hover:scale-[1.12] group-focus-visible:scale-[1.12] motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(160deg,var(--color-tgl01-acc),transparent_60%)] opacity-0 transition-opacity duration-300 group-hover:opacity-90 group-focus-visible:opacity-90 motion-reduce:transition-none"></span>
        <span class="absolute inset-x-0 bottom-[22%] z-[2] text-center text-[13px] font-bold tracking-[0.04em] text-white opacity-0 translate-y-1.5 transition-[opacity,translate] duration-300 [text-shadow:0_1px_4px_rgba(0,0,0,0.6)] group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Kai</span>
      </a>
    </div>
    <div class="flex gap-2 mt-[calc(var(--hex)*-0.28)]">
      <a href="#" class="group relative block w-[var(--hex)] [aspect-ratio:1/1.1547] overflow-hidden bg-tgl01-cell no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] focus-visible:outline-3 focus-visible:outline-tgl01-acc focus-visible:outline-offset-[3px]">
        <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=300&h=300&auto=format&fit=crop" alt="Mia, brand designer" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[450ms] group-hover:scale-[1.12] group-focus-visible:scale-[1.12] motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(160deg,var(--color-tgl01-acc),transparent_60%)] opacity-0 transition-opacity duration-300 group-hover:opacity-90 group-focus-visible:opacity-90 motion-reduce:transition-none"></span>
        <span class="absolute inset-x-0 bottom-[22%] z-[2] text-center text-[13px] font-bold tracking-[0.04em] text-white opacity-0 translate-y-1.5 transition-[opacity,translate] duration-300 [text-shadow:0_1px_4px_rgba(0,0,0,0.6)] group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Mia</span>
      </a>
      <a href="#" class="group relative block w-[var(--hex)] [aspect-ratio:1/1.1547] overflow-hidden bg-tgl01-cell no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] focus-visible:outline-3 focus-visible:outline-tgl01-acc focus-visible:outline-offset-[3px]">
        <img src="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?q=80&w=300&h=300&auto=format&fit=crop" alt="Eli, motion designer" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[450ms] group-hover:scale-[1.12] group-focus-visible:scale-[1.12] motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(160deg,var(--color-tgl01-acc),transparent_60%)] opacity-0 transition-opacity duration-300 group-hover:opacity-90 group-focus-visible:opacity-90 motion-reduce:transition-none"></span>
        <span class="absolute inset-x-0 bottom-[22%] z-[2] text-center text-[13px] font-bold tracking-[0.04em] text-white opacity-0 translate-y-1.5 transition-[opacity,translate] duration-300 [text-shadow:0_1px_4px_rgba(0,0,0,0.6)] group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Eli</span>
      </a>
      <a href="#" class="group relative block w-[var(--hex)] [aspect-ratio:1/1.1547] overflow-hidden bg-tgl01-cell no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] focus-visible:outline-3 focus-visible:outline-tgl01-acc focus-visible:outline-offset-[3px]">
        <img src="https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=300&h=300&auto=format&fit=crop" alt="Zoe, content strategist" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[450ms] group-hover:scale-[1.12] group-focus-visible:scale-[1.12] motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(160deg,var(--color-tgl01-acc),transparent_60%)] opacity-0 transition-opacity duration-300 group-hover:opacity-90 group-focus-visible:opacity-90 motion-reduce:transition-none"></span>
        <span class="absolute inset-x-0 bottom-[22%] z-[2] text-center text-[13px] font-bold tracking-[0.04em] text-white opacity-0 translate-y-1.5 transition-[opacity,translate] duration-300 [text-shadow:0_1px_4px_rgba(0,0,0,0.6)] group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Zoe</span>
      </a>
    </div>
    <div class="flex gap-2 mt-[calc(var(--hex)*-0.28)]">
      <a href="#" class="group relative block w-[var(--hex)] [aspect-ratio:1/1.1547] overflow-hidden bg-tgl01-cell no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] focus-visible:outline-3 focus-visible:outline-tgl01-acc focus-visible:outline-offset-[3px]">
        <img src="https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?q=80&w=300&h=300&auto=format&fit=crop" alt="Ivo, front-end engineer" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[450ms] group-hover:scale-[1.12] group-focus-visible:scale-[1.12] motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(160deg,var(--color-tgl01-acc),transparent_60%)] opacity-0 transition-opacity duration-300 group-hover:opacity-90 group-focus-visible:opacity-90 motion-reduce:transition-none"></span>
        <span class="absolute inset-x-0 bottom-[22%] z-[2] text-center text-[13px] font-bold tracking-[0.04em] text-white opacity-0 translate-y-1.5 transition-[opacity,translate] duration-300 [text-shadow:0_1px_4px_rgba(0,0,0,0.6)] group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Ivo</span>
      </a>
      <a href="#" class="group relative block w-[var(--hex)] [aspect-ratio:1/1.1547] overflow-hidden bg-tgl01-cell no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] focus-visible:outline-3 focus-visible:outline-tgl01-acc focus-visible:outline-offset-[3px]">
        <img src="https://images.unsplash.com/photo-1434389677669-e08b4cac3105?q=80&w=300&h=300&auto=format&fit=crop" alt="Ana, data scientist" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[450ms] group-hover:scale-[1.12] group-focus-visible:scale-[1.12] motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(160deg,var(--color-tgl01-acc),transparent_60%)] opacity-0 transition-opacity duration-300 group-hover:opacity-90 group-focus-visible:opacity-90 motion-reduce:transition-none"></span>
        <span class="absolute inset-x-0 bottom-[22%] z-[2] text-center text-[13px] font-bold tracking-[0.04em] text-white opacity-0 translate-y-1.5 transition-[opacity,translate] duration-300 [text-shadow:0_1px_4px_rgba(0,0,0,0.6)] group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Ana</span>
      </a>
      <a href="#" class="group relative block w-[var(--hex)] [aspect-ratio:1/1.1547] overflow-hidden bg-tgl01-cell no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] focus-visible:outline-3 focus-visible:outline-tgl01-acc focus-visible:outline-offset-[3px]">
        <img src="https://images.unsplash.com/photo-1503602642458-232111445657?q=80&w=300&h=300&auto=format&fit=crop" alt="Ben, photographer" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[450ms] group-hover:scale-[1.12] group-focus-visible:scale-[1.12] motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(160deg,var(--color-tgl01-acc),transparent_60%)] opacity-0 transition-opacity duration-300 group-hover:opacity-90 group-focus-visible:opacity-90 motion-reduce:transition-none"></span>
        <span class="absolute inset-x-0 bottom-[22%] z-[2] text-center text-[13px] font-bold tracking-[0.04em] text-white opacity-0 translate-y-1.5 transition-[opacity,translate] duration-300 [text-shadow:0_1px_4px_rgba(0,0,0,0.6)] group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Ben</span>
      </a>
      <a href="#" class="group relative block w-[var(--hex)] [aspect-ratio:1/1.1547] overflow-hidden bg-tgl01-cell no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] focus-visible:outline-3 focus-visible:outline-tgl01-acc focus-visible:outline-offset-[3px]">
        <img src="https://images.unsplash.com/photo-1591047139829-d91aecb6caea?q=80&w=300&h=300&auto=format&fit=crop" alt="Uma, accessibility lead" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[450ms] group-hover:scale-[1.12] group-focus-visible:scale-[1.12] motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(160deg,var(--color-tgl01-acc),transparent_60%)] opacity-0 transition-opacity duration-300 group-hover:opacity-90 group-focus-visible:opacity-90 motion-reduce:transition-none"></span>
        <span class="absolute inset-x-0 bottom-[22%] z-[2] text-center text-[13px] font-bold tracking-[0.04em] text-white opacity-0 translate-y-1.5 transition-[opacity,translate] duration-300 [text-shadow:0_1px_4px_rgba(0,0,0,0.6)] group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Uma</span>
      </a>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl01-bg: #161318;
  --color-tgl01-bg: oklch(0.19 0.012 310);
  --color-tgl01-cell: #241f28;
  --color-tgl01-cell: oklch(0.26 0.018 310);
  --color-tgl01-acc: #e0762f;
  --color-tgl01-acc: oklch(0.68 0.17 45);
  --font-tgl01-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tgl-01 {
  width: 100%;
  min-height: 100svh;
}
/* Scoped selection colour — no utility form. */

.tgl-01 ::selection {
  background: var(--color-tgl01-acc);
  color: #fff;
}
```
