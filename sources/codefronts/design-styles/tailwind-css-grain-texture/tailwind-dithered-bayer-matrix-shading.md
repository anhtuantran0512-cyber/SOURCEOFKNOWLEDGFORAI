---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-dithered-bayer-matrix-shading/"
title: "Tailwind Dithered Bayer Matrix Shading Effect"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "Ordered dithering, the 1984 way: sixteen dispersed threshold values in a 4×4 tile, blended in hard-light over a deliberately banded gradient."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dithered Bayer Matrix Shading Effect
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-dithered-bayer-matrix-shading/

Ordered dithering, the 1984 way: sixteen dispersed threshold values in a 4×4 tile, blended in hard-light over a deliberately banded gradient. Your eye reassembles the dot pattern into a smooth ramp. Three matrix sizes set three eras, and the same layer turns photographs into one-bit images.
## HTML
```html
<section class="gtw-15 relative block w-full min-h-svh bg-gtw15-bg text-gtw15-ink" aria-labelledby="gtw-15-title">
  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-40">
    <input type="checkbox" id="gtw-15-theme" class="gtw-15-theme peer sr-only">
    <label for="gtw-15-theme" class="grid place-items-center w-11 h-11 rounded border border-gtw15-line bg-gtw15-surf text-gtw15-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-gtw15-acc peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <main class="w-[min(74rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto pt-[clamp(3rem,8vw,5rem)] pb-[clamp(2.5rem,6vw,4rem)] grid gap-[clamp(2rem,5vw,3rem)]">
    <header class="max-w-[44rem] grid gap-[0.6rem]">
      <p class="m-0 font-gtw15-mono text-[0.72rem] font-medium leading-none tracking-[0.18em] uppercase text-gtw15-acc">Ordered dither · 4×4 Bayer</p>
      <h1 id="gtw-15-title" class="m-0 font-gtw15-display text-[clamp(2rem,5.4vw,3.4rem)] font-semibold leading-[1.02] tracking-[-0.04em] text-balance">Thresholds, not noise</h1>
      <p class="m-0 max-w-[38rem] text-gtw15-mut text-[clamp(0.95rem,1.9vw,1.07rem)] text-pretty">Sixteen dispersed threshold values tiled at four pixels, blended in <code class="font-gtw15-mono text-[0.9em]">hard-light</code>. The same maths that gave 1984 its shading, running as one CSS layer.</p>
    </header>

    <div class="relative isolate overflow-hidden grid items-end min-h-[clamp(16rem,42vw,26rem)] rounded-md border border-gtw15-line bg-[linear-gradient(172deg,var(--color-gtw15-acc2)_0%_12%,color-mix(in_oklab,var(--color-gtw15-acc2)_70%,var(--color-gtw15-acc))_12%_26%,color-mix(in_oklab,var(--color-gtw15-acc2)_45%,var(--color-gtw15-acc))_26%_40%,color-mix(in_oklab,var(--color-gtw15-acc)_70%,var(--color-gtw15-acc2))_40%_54%,var(--color-gtw15-acc)_54%_68%,color-mix(in_oklab,var(--color-gtw15-acc)_60%,var(--color-gtw15-bg))_68%_82%,color-mix(in_oklab,var(--color-gtw15-acc)_25%,var(--color-gtw15-bg))_82%_92%,var(--color-gtw15-bg)_92%_100%)]">
      <span aria-hidden="true" class="gtw-15-dither absolute inset-0 pointer-events-none bg-[image:var(--gtw15-matrix)] bg-repeat bg-[length:4px_4px] mix-blend-hard-light opacity-[0.55]"></span>
      <div class="relative z-[2] grid gap-2 max-w-[34rem] p-[clamp(1.2rem,3.4vw,2.2rem)] text-white">
        <p class="m-0 justify-self-start px-[0.6rem] py-[0.25rem] rounded bg-[oklch(0.15_0.02_250/0.72)] font-gtw15-mono text-[0.7rem] font-medium leading-[1.5] tracking-[0.1em] uppercase">4×4 · 8 bands · hard-light</p>
        <h2 class="m-0 font-gtw15-display text-[clamp(1.3rem,3.4vw,1.9rem)] font-semibold leading-[1.1] tracking-[-0.03em]">Sunset, quantised</h2>
        <p class="m-0 max-w-[32rem] text-white text-[0.93rem] text-pretty">A stepped gradient of eight flat bands. The matrix breaks each boundary into a dot pattern that your eye averages back into a smooth ramp.</p>
      </div>
    </div>

    <section class="grid gap-4" aria-labelledby="gtw-15-h-mx">
      <div class="grid gap-[0.3rem] pb-[0.7rem] border-b border-gtw15-line">
        <h2 id="gtw-15-h-mx" class="m-0 font-gtw15-display text-[clamp(1.3rem,3.4vw,1.9rem)] font-semibold leading-[1.1] tracking-[-0.03em]">Matrix size sets the era</h2>
        <p class="m-0 text-gtw15-mut text-[0.87rem]">Same source gradient, same blend mode, three matrices.</p>
      </div>
      <ul class="list-none m-0 p-0 grid gap-[clamp(0.8rem,2vw,1.3rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,14rem),1fr))]">
        <li class="group grid gap-[0.35rem] min-w-0">
          <span aria-hidden="true" class="gtw-15-swatch relative isolate block h-[clamp(7rem,16vw,10rem)] overflow-hidden rounded-md border border-gtw15-line bg-[linear-gradient(160deg,var(--color-gtw15-acc)_0%_20%,color-mix(in_oklab,var(--color-gtw15-acc)_60%,var(--color-gtw15-bg))_20%_45%,color-mix(in_oklab,var(--color-gtw15-acc)_30%,var(--color-gtw15-bg))_45%_72%,var(--color-gtw15-bg)_72%_100%)] transition-[translate] duration-[280ms] group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:mix-blend-hard-light after:opacity-[0.6] after:bg-[image:var(--gtw15-m2)] after:bg-[length:4px_4px]"></span>
          <b class="font-gtw15-mono text-[0.95rem] font-semibold leading-none">2×2</b><span class="text-gtw15-mut text-[0.85rem] text-pretty">Four levels. Early monochrome displays, chunky and unmistakable.</span>
        </li>
        <li class="group grid gap-[0.35rem] min-w-0">
          <span aria-hidden="true" class="gtw-15-swatch relative isolate block h-[clamp(7rem,16vw,10rem)] overflow-hidden rounded-md border border-gtw15-line bg-[linear-gradient(160deg,var(--color-gtw15-acc)_0%_20%,color-mix(in_oklab,var(--color-gtw15-acc)_60%,var(--color-gtw15-bg))_20%_45%,color-mix(in_oklab,var(--color-gtw15-acc)_30%,var(--color-gtw15-bg))_45%_72%,var(--color-gtw15-bg)_72%_100%)] transition-[translate] duration-[280ms] group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:mix-blend-hard-light after:opacity-[0.6] after:bg-[image:var(--gtw15-m4)] after:bg-[length:4px_4px]"></span>
          <b class="font-gtw15-mono text-[0.95rem] font-semibold leading-none">4×4</b><span class="text-gtw15-mut text-[0.85rem] text-pretty">Sixteen levels. The classic Macintosh and Atari look, and the default here.</span>
        </li>
        <li class="group grid gap-[0.35rem] min-w-0">
          <span aria-hidden="true" class="gtw-15-swatch relative isolate block h-[clamp(7rem,16vw,10rem)] overflow-hidden rounded-md border border-gtw15-line bg-[linear-gradient(160deg,var(--color-gtw15-acc)_0%_20%,color-mix(in_oklab,var(--color-gtw15-acc)_60%,var(--color-gtw15-bg))_20%_45%,color-mix(in_oklab,var(--color-gtw15-acc)_30%,var(--color-gtw15-bg))_45%_72%,var(--color-gtw15-bg)_72%_100%)] transition-[translate] duration-[280ms] group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:mix-blend-hard-light after:opacity-[0.6] after:bg-[image:var(--gtw15-m8)] after:bg-[length:8px_8px]"></span>
          <b class="font-gtw15-mono text-[0.95rem] font-semibold leading-none">8×8</b><span class="text-gtw15-mut text-[0.85rem] text-pretty">Sixty-four levels. Nearly continuous — use it as a texture, not a statement.</span>
        </li>
      </ul>
    </section>

    <section class="grid gap-4" aria-labelledby="gtw-15-h-photo">
      <h2 id="gtw-15-h-photo" class="m-0 font-gtw15-display text-[clamp(1.3rem,3.4vw,1.9rem)] font-semibold leading-[1.1] tracking-[-0.03em]">One-bit image treatment</h2>
      <div class="grid gap-[clamp(0.8rem,2vw,1.3rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,15rem),1fr))]">
        <figure class="group m-0 grid gap-[0.4rem] min-w-0">
          <div class="relative isolate overflow-hidden aspect-[5/6] rounded-md border border-gtw15-line bg-gtw15-surf transition-[translate] duration-[280ms] group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0">
            <img src="https://picsum.photos/id/1011/1000/1200" alt="A person sitting on a kayak on a still lake" loading="lazy" width="1000" height="1200" class="absolute inset-0 w-full h-full object-cover grayscale contrast-[1.45] brightness-[1.02]">
            <span aria-hidden="true" class="gtw-15-dither absolute inset-0 pointer-events-none bg-[image:var(--gtw15-matrix)] bg-repeat bg-[length:4px_4px] mix-blend-hard-light opacity-[0.55]"></span>
          </div>
          <figcaption class="font-gtw15-mono text-[0.78rem] leading-[1.4] text-gtw15-mut">grayscale(1) contrast(1.45) + 4×4</figcaption>
        </figure>
        <figure class="group m-0 grid gap-[0.4rem] min-w-0">
          <div class="relative isolate overflow-hidden aspect-[5/6] rounded-md border border-gtw15-line bg-gtw15-surf transition-[translate] duration-[280ms] group-hover:-translate-y-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-y-0">
            <img src="https://picsum.photos/id/1024/1000/1200" alt="A bear standing in shallow water" loading="lazy" width="1000" height="1200" class="absolute inset-0 w-full h-full object-cover grayscale contrast-[1.45] brightness-[1.02]">
            <span aria-hidden="true" class="gtw-15-dither absolute inset-0 pointer-events-none bg-[image:var(--gtw15-matrix)] bg-repeat bg-[length:8px_8px] mix-blend-hard-light opacity-[0.55]"></span>
          </div>
          <figcaption class="font-gtw15-mono text-[0.78rem] leading-[1.4] text-gtw15-mut">Same treatment at 8px tile</figcaption>
        </figure>
      </div>
    </section>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw15-bg: #05070f;
  --color-gtw15-bg: oklch(0.13 0.02 265);
  --color-gtw15-surf: #0c1120;
  --color-gtw15-surf: oklch(0.18 0.03 265);
  --color-gtw15-line: #1d2740;
  --color-gtw15-line: oklch(0.28 0.04 265);
  --color-gtw15-ink: #e8eeff;
  --color-gtw15-ink: oklch(0.94 0.02 265);
  --color-gtw15-mut: #8f9dc0;
  --color-gtw15-mut: oklch(0.68 0.04 265);
  --color-gtw15-acc: #38bdf8;
  --color-gtw15-acc: oklch(0.76 0.14 232);
  --color-gtw15-acc2: #fb7185;
  --color-gtw15-acc2: oklch(0.72 0.17 15);
  --font-gtw15-display: 'Space Grotesk', 'Inter Tight', ui-sans-serif, system-ui, sans-serif;
  --font-gtw15-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}

.gtw-15 {
  width: 100%;
  min-height: 100svh;
  --gtw15-m4: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='4' height='4' shape-rendering='crispEdges'%3E%3Cg%3E%3Crect x='0' y='0' width='1' height='1' fill='%23000'/%3E%3Crect x='2' y='0' width='1' height='1' fill='%23606060'/%3E%3Crect x='1' y='2' width='1' height='1' fill='%23909090'/%3E%3Crect x='3' y='2' width='1' height='1' fill='%23303030'/%3E%3Crect x='2' y='1' width='1' height='1' fill='%23e0e0e0'/%3E%3Crect x='0' y='1' width='1' height='1' fill='%23a0a0a0'/%3E%3Crect x='3' y='3' width='1' height='1' fill='%23c0c0c0'/%3E%3Crect x='1' y='3' width='1' height='1' fill='%23505050'/%3E%3Crect x='1' y='1' width='1' height='1' fill='%23202020'/%3E%3Crect x='3' y='1' width='1' height='1' fill='%23808080'/%3E%3Crect x='0' y='3' width='1' height='1' fill='%23f0f0f0'/%3E%3Crect x='2' y='3' width='1' height='1' fill='%23707070'/%3E%3Crect x='3' y='0' width='1' height='1' fill='%23404040'/%3E%3Crect x='1' y='0' width='1' height='1' fill='%23b0b0b0'/%3E%3Crect x='0' y='2' width='1' height='1' fill='%23d0d0d0'/%3E%3Crect x='2' y='2' width='1' height='1' fill='%23101010'/%3E%3C/g%3E%3C/svg%3E");
  --gtw15-m2: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='2' height='2' shape-rendering='crispEdges'%3E%3Crect x='0' y='0' width='1' height='1' fill='%23000'/%3E%3Crect x='1' y='0' width='1' height='1' fill='%23aaa'/%3E%3Crect x='1' y='1' width='1' height='1' fill='%23555'/%3E%3Crect x='0' y='1' width='1' height='1' fill='%23fff'/%3E%3C/svg%3E");
  --gtw15-m8: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='8' height='8'%3E%3Cfilter id='gtw15d'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.5' numOctaves='1' seed='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3CfeComponentTransfer%3E%3CfeFuncR type='discrete' tableValues='0 0.14 0.28 0.42 0.57 0.71 0.85 1'/%3E%3CfeFuncG type='discrete' tableValues='0 0.14 0.28 0.42 0.57 0.71 0.85 1'/%3E%3CfeFuncB type='discrete' tableValues='0 0.14 0.28 0.42 0.57 0.71 0.85 1'/%3E%3C/feComponentTransfer%3E%3C/filter%3E%3Crect width='8' height='8' filter='url(%23gtw15d)'/%3E%3C/svg%3E");
  --gtw15-matrix: var(--gtw15-m4);
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
}
/* image-rendering needs the crisp-edges fallback for older Firefox, and Tailwind has no
   utility for it — a two-declaration class is the honest answer. */

.gtw-15-dither,
.gtw-15-swatch::after {
  image-rendering: pixelated;
  image-rendering: crisp-edges;
}

.gtw-15:has(.gtw-15-theme:checked) {
  --color-gtw15-bg: #eef1f8;
  --color-gtw15-bg: oklch(0.95 0.01 265);
  --color-gtw15-surf: #ffffff;
  --color-gtw15-surf: oklch(1 0 0);
  --color-gtw15-line: #d5dced;
  --color-gtw15-line: oklch(0.88 0.02 265);
  --color-gtw15-ink: #05070f;
  --color-gtw15-ink: oklch(0.13 0.02 265);
  --color-gtw15-mut: #556180;
  --color-gtw15-mut: oklch(0.45 0.04 265);
  --color-gtw15-acc: #0369a1;
  --color-gtw15-acc: oklch(0.48 0.11 235);
  --color-gtw15-acc2: #be123c;
  --color-gtw15-acc2: oklch(0.5 0.19 16);
}

@media (prefers-color-scheme: light) {
  .gtw-15 {
    --color-gtw15-bg: #eef1f8;
    --color-gtw15-bg: oklch(0.95 0.01 265);
    --color-gtw15-surf: #ffffff;
    --color-gtw15-surf: oklch(1 0 0);
    --color-gtw15-line: #d5dced;
    --color-gtw15-line: oklch(0.88 0.02 265);
    --color-gtw15-ink: #05070f;
    --color-gtw15-ink: oklch(0.13 0.02 265);
    --color-gtw15-mut: #556180;
    --color-gtw15-mut: oklch(0.45 0.04 265);
    --color-gtw15-acc: #0369a1;
    --color-gtw15-acc: oklch(0.48 0.11 235);
    --color-gtw15-acc2: #be123c;
    --color-gtw15-acc2: oklch(0.5 0.19 16);
  }

  .gtw-15:has(.gtw-15-theme:checked) {
    --color-gtw15-bg: #05070f;
    --color-gtw15-bg: oklch(0.13 0.02 265);
    --color-gtw15-surf: #0c1120;
    --color-gtw15-surf: oklch(0.18 0.03 265);
    --color-gtw15-line: #1d2740;
    --color-gtw15-line: oklch(0.28 0.04 265);
    --color-gtw15-ink: #e8eeff;
    --color-gtw15-ink: oklch(0.94 0.02 265);
    --color-gtw15-mut: #8f9dc0;
    --color-gtw15-mut: oklch(0.68 0.04 265);
    --color-gtw15-acc: #38bdf8;
    --color-gtw15-acc: oklch(0.76 0.14 232);
    --color-gtw15-acc2: #fb7185;
    --color-gtw15-acc2: oklch(0.72 0.17 15);
  }
}

@media (prefers-color-scheme: dark) {
  .gtw-15:has(.gtw-15-theme:checked) {
    --color-gtw15-bg: #eef1f8;
    --color-gtw15-bg: oklch(0.95 0.01 265);
    --color-gtw15-surf: #ffffff;
    --color-gtw15-surf: oklch(1 0 0);
    --color-gtw15-line: #d5dced;
    --color-gtw15-line: oklch(0.88 0.02 265);
    --color-gtw15-ink: #05070f;
    --color-gtw15-ink: oklch(0.13 0.02 265);
    --color-gtw15-mut: #556180;
    --color-gtw15-mut: oklch(0.45 0.04 265);
    --color-gtw15-acc: #0369a1;
    --color-gtw15-acc: oklch(0.48 0.11 235);
    --color-gtw15-acc2: #be123c;
    --color-gtw15-acc2: oklch(0.5 0.19 16);
  }
}
```
