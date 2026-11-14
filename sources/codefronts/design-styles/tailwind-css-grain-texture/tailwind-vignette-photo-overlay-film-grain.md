---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-vignette-photo-overlay-film-grain/"
title: "Tailwind Vignette Photo Overlay with Film Grain"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "A contact sheet of three frames, each with a lens vignette under a luminosity-blended grain layer and its own grain weight."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vignette Photo Overlay with Film Grain
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-vignette-photo-overlay-film-grain/

A contact sheet of three frames, each with a lens vignette under a luminosity-blended grain layer and its own grain weight. No canvas, no image processing, no filters on the photograph — four ordinary layers over an <img>. The port's neat trick: the per-frame weight that needed an inline style attribute is now an arbitrary-property utility, [--gtw08-weight:0.13].
## HTML
```html
<section class="gtw-08 relative block w-full min-h-svh bg-gtw08-bg text-gtw08-ink" aria-labelledby="gtw-08-title">
  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-40">
    <input type="checkbox" id="gtw-08-theme" class="gtw-08-theme peer sr-only">
    <label for="gtw-08-theme" class="grid place-items-center w-11 h-11 rounded-full border border-gtw08-line bg-gtw08-surf text-gtw08-ink cursor-pointer transition-colors duration-200 hover:border-gtw08-acc peer-focus-visible:outline-2 peer-focus-visible:outline-gtw08-acc peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <main class="w-[min(78rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto pt-[clamp(3rem,8vw,5.5rem)] pb-[clamp(2.5rem,6vw,4rem)] grid gap-[clamp(2rem,5vw,3.2rem)]">
    <header class="max-w-[46rem] grid gap-[0.6rem]">
      <p class="m-0 font-gtw08-mono text-[0.74rem] leading-none tracking-[0.16em] uppercase text-gtw08-acc">Roll 04 · 400 ISO · pushed one stop</p>
      <h1 id="gtw-08-title" class="m-0 font-gtw08-display text-[clamp(2.6rem,8vw,5rem)] font-normal leading-[0.95] tracking-[-0.02em]">Contact sheet</h1>
      <p class="m-0 max-w-[38rem] text-gtw08-mut text-[clamp(0.95rem,1.9vw,1.08rem)] text-pretty">Vignette below the grain, grain in <code class="font-gtw08-mono text-[0.9em]">luminosity</code>, weight set per frame with <code class="font-gtw08-mono text-[0.9em]">[--gtw08-weight:…]</code>. No filters, no canvas, no image processing — four layers of CSS over an ordinary <code class="font-gtw08-mono text-[0.9em]">&lt;img&gt;</code>.</p>
    </header>

    <div class="grid gap-[clamp(1rem,2.5vw,1.6rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,17rem),1fr))] items-start">
      <figure class="group m-0 grid gap-[0.7rem] min-w-0 [--gtw08-weight:0.13]">
        <div class="gtw-08-plate relative isolate overflow-hidden rounded aspect-[4/5] bg-[#101012]">
          <img src="https://picsum.photos/id/1015/1200/1500" alt="A river running between steep rock walls under an overcast sky" loading="lazy" width="1200" height="1500" class="absolute inset-0 z-0 block w-full h-full object-cover [filter:contrast(1.04)_saturate(0.94)] transition-[scale] duration-[620ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:scale-[1.035] motion-reduce:transition-none motion-reduce:group-hover:scale-100">
          <span aria-hidden="true" class="absolute inset-0 z-[1] pointer-events-none bg-[radial-gradient(120%_100%_at_50%_46%,transparent_45%,oklch(0.12_0.01_285/0.24)_76%,oklch(0.12_0.01_285/0.44)_100%)]"></span>
          <span aria-hidden="true" class="gtw-08-grain absolute inset-0 z-[2] pointer-events-none opacity-[var(--gtw08-weight)] mix-blend-luminosity transition-opacity duration-300 group-hover:opacity-[calc(var(--gtw08-weight)*1.25)] motion-reduce:transition-none"></span>
        </div>
        <figcaption class="grid gap-[0.2rem]">
          <b class="font-gtw08-mono text-[0.9rem] font-medium leading-tight tracking-[0.04em]">01 · Gorge</b>
          <span class="text-gtw08-mut text-[0.85rem] text-pretty">Bright, flat frame. Grain pushed to 0.13 to give the sky some tooth.</span>
        </figcaption>
      </figure>

      <figure class="group m-0 grid gap-[0.7rem] min-w-0 [--gtw08-weight:0.07]">
        <div class="gtw-08-plate relative isolate overflow-hidden rounded aspect-[4/5] bg-[#101012]">
          <img src="https://picsum.photos/id/1039/1600/1000" alt="A waterfall seen from above, surrounded by dense forest" loading="lazy" width="1600" height="1000" class="absolute inset-0 z-0 block w-full h-full object-cover [filter:contrast(1.04)_saturate(0.94)] transition-[scale] duration-[620ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:scale-[1.035] motion-reduce:transition-none motion-reduce:group-hover:scale-100">
          <span aria-hidden="true" class="absolute inset-0 z-[1] pointer-events-none bg-[radial-gradient(120%_100%_at_50%_46%,transparent_45%,oklch(0.12_0.01_285/0.24)_76%,oklch(0.12_0.01_285/0.44)_100%)]"></span>
          <span aria-hidden="true" class="gtw-08-grain absolute inset-0 z-[2] pointer-events-none opacity-[var(--gtw08-weight)] mix-blend-luminosity transition-opacity duration-300 group-hover:opacity-[calc(var(--gtw08-weight)*1.25)] motion-reduce:transition-none"></span>
        </div>
        <figcaption class="grid gap-[0.2rem]">
          <b class="font-gtw08-mono text-[0.9rem] font-medium leading-tight tracking-[0.04em]">02 · Falls</b>
          <span class="text-gtw08-mut text-[0.85rem] text-pretty">Dark and contrasty. Grain held at 0.07 — any more and the shadows turn to mud.</span>
        </figcaption>
      </figure>

      <figure class="group m-0 grid gap-[0.7rem] min-w-0 [--gtw08-weight:0.1]">
        <div class="gtw-08-plate relative isolate overflow-hidden rounded aspect-[4/5] bg-[#101012]">
          <img src="https://picsum.photos/id/1043/1200/1500" alt="A person standing on a rock outcrop looking across a valley" loading="lazy" width="1200" height="1500" class="absolute inset-0 z-0 block w-full h-full object-cover [filter:contrast(1.04)_saturate(0.94)] transition-[scale] duration-[620ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:scale-[1.035] motion-reduce:transition-none motion-reduce:group-hover:scale-100">
          <span aria-hidden="true" class="absolute inset-0 z-[1] pointer-events-none bg-[radial-gradient(120%_100%_at_50%_46%,transparent_45%,oklch(0.12_0.01_285/0.24)_76%,oklch(0.12_0.01_285/0.44)_100%)]"></span>
          <span aria-hidden="true" class="gtw-08-grain absolute inset-0 z-[2] pointer-events-none opacity-[var(--gtw08-weight)] mix-blend-luminosity transition-opacity duration-300 group-hover:opacity-[calc(var(--gtw08-weight)*1.25)] motion-reduce:transition-none"></span>
        </div>
        <figcaption class="grid gap-[0.2rem]">
          <b class="font-gtw08-mono text-[0.9rem] font-medium leading-tight tracking-[0.04em]">03 · Outcrop</b>
          <span class="text-gtw08-mut text-[0.85rem] text-pretty">Falloff kept outside the figure so the vignette reads as lens, not retouching.</span>
        </figcaption>
      </figure>
    </div>

    <aside class="grid gap-[0.9rem] p-[clamp(1.2rem,3vw,1.9rem)] rounded-[14px] border border-gtw08-line bg-gtw08-surf">
      <h2 class="m-0 font-gtw08-display text-[clamp(1.3rem,3vw,1.7rem)] font-normal leading-[1.15]">Layer order, bottom to top</h2>
      <ol class="gtw-08-stack list-none m-0 p-0 grid gap-[0.1rem]">
        <li class="grid grid-cols-[1.6rem_minmax(0,1fr)] gap-x-[0.6rem] gap-y-[0.15rem] py-[0.55rem] border-t border-gtw08-line"><b class="font-semibold text-[0.92rem]">Photograph</b><span class="font-gtw08-mono text-[0.8rem] leading-[1.4] text-gtw08-mut">object-cover, aspect-ratio declared</span></li>
        <li class="grid grid-cols-[1.6rem_minmax(0,1fr)] gap-x-[0.6rem] gap-y-[0.15rem] py-[0.55rem] border-t border-gtw08-line"><b class="font-semibold text-[0.92rem]">Vignette</b><span class="font-gtw08-mono text-[0.8rem] leading-[1.4] text-gtw08-mut">radial-gradient, transparent to 45%</span></li>
        <li class="grid grid-cols-[1.6rem_minmax(0,1fr)] gap-x-[0.6rem] gap-y-[0.15rem] py-[0.55rem] border-t border-gtw08-line"><b class="font-semibold text-[0.92rem]">Grain</b><span class="font-gtw08-mono text-[0.8rem] leading-[1.4] text-gtw08-mut">mix-blend-luminosity — above the vignette</span></li>
        <li class="grid grid-cols-[1.6rem_minmax(0,1fr)] gap-x-[0.6rem] gap-y-[0.15rem] py-[0.55rem] border-t border-gtw08-line"><b class="font-semibold text-[0.92rem]">Caption plate</b><span class="font-gtw08-mono text-[0.8rem] leading-[1.4] text-gtw08-mut">own backdrop, always legible</span></li>
      </ol>
    </aside>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw08-bg: #0a0a0b;
  --color-gtw08-bg: oklch(0.16 0.003 285);
  --color-gtw08-surf: #141416;
  --color-gtw08-surf: oklch(0.21 0.004 285);
  --color-gtw08-line: #262629;
  --color-gtw08-line: oklch(0.3 0.005 285);
  --color-gtw08-ink: #f0efec;
  --color-gtw08-ink: oklch(0.95 0.005 85);
  --color-gtw08-mut: #97948d;
  --color-gtw08-mut: oklch(0.68 0.01 85);
  --color-gtw08-acc: #e8b84b;
  --color-gtw08-acc: oklch(0.8 0.13 85);
  --font-gtw08-display: 'Instrument Serif', 'Playfair Display', Georgia, serif;
  --font-gtw08-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}

.gtw-08 {
  width: 100%;
  min-height: 100svh;
  --gtw08-weight: 0.1;
  --gtw08-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='170' height='170'%3E%3Cfilter id='gtw08n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.82' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='170' height='170' filter='url(%23gtw08n)'/%3E%3C/svg%3E");
  --gtw08-noise-fine: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='170' height='170'%3E%3Cfilter id='gtw08f'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.25' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='170' height='170' filter='url(%23gtw08f)'/%3E%3C/svg%3E");
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
}
/* The grain image and its retina swap: one element, one resolution query, no utility worth writing. */

.gtw-08-grain {
  background-image: var(--gtw08-noise);
}

@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 2dppx) {
  .gtw-08-grain {
    background-image: var(--gtw08-noise-fine);
    opacity: calc(var(--gtw08-weight) * 1.15);
  }
}
/* Counter numerals on the layer-order list — counters have no utility form. */

.gtw-08-stack {
  counter-reset: gtw08;
}

.gtw-08-stack li {
  counter-increment: gtw08;
}

.gtw-08-stack li::before {
  content: counter(gtw08);
  grid-row: span 2;
  font: 400 0.8rem/1.6 var(--font-gtw08-mono);
  color: var(--color-gtw08-acc);
}

.gtw-08:has(.gtw-08-theme:checked) {
  --color-gtw08-bg: #f2f0ec;
  --color-gtw08-bg: oklch(0.95 0.008 85);
  --color-gtw08-surf: #ffffff;
  --color-gtw08-surf: oklch(1 0 0);
  --color-gtw08-line: #ded9d1;
  --color-gtw08-line: oklch(0.88 0.012 85);
  --color-gtw08-ink: #0a0a0b;
  --color-gtw08-ink: oklch(0.16 0.003 285);
  --color-gtw08-mut: #635f58;
  --color-gtw08-mut: oklch(0.48 0.012 85);
  --color-gtw08-acc: #9a6b12;
  --color-gtw08-acc: oklch(0.55 0.11 78);
}

@media (prefers-color-scheme: light) {
  .gtw-08 {
    --color-gtw08-bg: #f2f0ec;
    --color-gtw08-bg: oklch(0.95 0.008 85);
    --color-gtw08-surf: #ffffff;
    --color-gtw08-surf: oklch(1 0 0);
    --color-gtw08-line: #ded9d1;
    --color-gtw08-line: oklch(0.88 0.012 85);
    --color-gtw08-ink: #0a0a0b;
    --color-gtw08-ink: oklch(0.16 0.003 285);
    --color-gtw08-mut: #635f58;
    --color-gtw08-mut: oklch(0.48 0.012 85);
    --color-gtw08-acc: #9a6b12;
    --color-gtw08-acc: oklch(0.55 0.11 78);
  }

  .gtw-08:has(.gtw-08-theme:checked) {
    --color-gtw08-bg: #0a0a0b;
    --color-gtw08-bg: oklch(0.16 0.003 285);
    --color-gtw08-surf: #141416;
    --color-gtw08-surf: oklch(0.21 0.004 285);
    --color-gtw08-line: #262629;
    --color-gtw08-line: oklch(0.3 0.005 285);
    --color-gtw08-ink: #f0efec;
    --color-gtw08-ink: oklch(0.95 0.005 85);
    --color-gtw08-mut: #97948d;
    --color-gtw08-mut: oklch(0.68 0.01 85);
    --color-gtw08-acc: #e8b84b;
    --color-gtw08-acc: oklch(0.8 0.13 85);
  }
}

@media (prefers-color-scheme: dark) {
  .gtw-08:has(.gtw-08-theme:checked) {
    --color-gtw08-bg: #f2f0ec;
    --color-gtw08-bg: oklch(0.95 0.008 85);
    --color-gtw08-surf: #ffffff;
    --color-gtw08-surf: oklch(1 0 0);
    --color-gtw08-line: #ded9d1;
    --color-gtw08-line: oklch(0.88 0.012 85);
    --color-gtw08-ink: #0a0a0b;
    --color-gtw08-ink: oklch(0.16 0.003 285);
    --color-gtw08-mut: #635f58;
    --color-gtw08-mut: oklch(0.48 0.012 85);
    --color-gtw08-acc: #9a6b12;
    --color-gtw08-acc: oklch(0.55 0.11 78);
  }
}
```
