---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-textured-section-divider-svg-grain/"
title: "Tailwind Textured Section Divider with SVG Grain"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "Three ways for two sections to meet like materials rather than like divs: a torn edge driven by feDisplacementMap, a masked grain fade, and a hairline with a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Textured Section Divider with SVG Grain
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-textured-section-divider-svg-grain/

Three ways for two sections to meet like materials rather than like divs: a torn edge driven by feDisplacementMap, a masked grain fade, and a hairline with a grain wash spilling past it. The continuity trick is the same in all three — the grain layer runs across the join at identical weight, which is what makes two bands read as one surface.
## HTML
```html
<section class="gtw-13 relative block w-full min-h-svh bg-gtw13-bottom text-gtw13-ink" aria-labelledby="gtw-13-title">
  <svg class="absolute w-0 h-0 overflow-hidden" width="0" height="0" aria-hidden="true" focusable="false">
    <filter id="gtw-13-tear" x="-20%" y="-40%" width="140%" height="180%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.012 0.34" numOctaves="3" seed="23" result="gtw13noise"/>
      <feDisplacementMap in="SourceGraphic" in2="gtw13noise" scale="18" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
  </svg>

  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-60">
    <input type="checkbox" id="gtw-13-theme" class="gtw-13-theme peer sr-only">
    <label for="gtw-13-theme" class="grid place-items-center w-11 h-11 rounded-full border border-[color-mix(in_oklab,var(--color-gtw13-ink)_22%,transparent)] bg-gtw13-bottom text-gtw13-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-gtw13-acc peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <section class="relative isolate bg-gtw13-top pt-[clamp(3.5rem,9vw,6rem)] pb-[calc(var(--gtw13-tear)+clamp(2rem,5vw,3.5rem))]" aria-labelledby="gtw-13-title">
    <div class="relative z-[3] w-[min(64rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto grid gap-3 max-w-[46rem]">
      <p class="m-0 font-gtw13-mono text-[0.72rem] font-medium leading-none tracking-[0.18em] uppercase text-gtw13-acc">Field guide · issue 12</p>
      <h1 id="gtw-13-title" class="m-0 font-gtw13-display text-[clamp(2rem,5.6vw,3.5rem)] font-semibold leading-[1.03] tracking-[-0.035em] text-balance">Sections should meet like materials, not like divs</h1>
      <p class="m-0 max-w-[40rem] text-gtw13-mut text-[clamp(0.97rem,2vw,1.1rem)] text-pretty">Below this paragraph the edge is torn by an SVG displacement map, and the grain band runs straight across the join. That continuity is what makes it read as one surface.</p>
    </div>
    <span aria-hidden="true" class="absolute inset-x-0 bottom-0 z-[2] h-[var(--gtw13-tear)] bg-gtw13-top [filter:url(#gtw-13-tear)] pointer-events-none"></span>
    <span aria-hidden="true" class="absolute inset-x-0 inset-y-[calc(var(--gtw13-tear)*-1)] z-[1] pointer-events-none bg-[image:var(--gtw13-noise)] opacity-[var(--gtw13-grain)] mix-blend-overlay"></span>
  </section>

  <section class="relative isolate bg-gtw13-mid text-gtw13-onmid pt-[clamp(3rem,8vw,5rem)] pb-[clamp(5rem,12vw,8rem)] -mt-[var(--gtw13-tear)]" aria-labelledby="gtw-13-h-fade">
    <span aria-hidden="true" class="absolute inset-x-0 inset-y-[calc(var(--gtw13-tear)*-1)] z-[1] pointer-events-none bg-[image:var(--gtw13-noise)] opacity-[var(--gtw13-grain)] mix-blend-overlay"></span>
    <div class="relative z-[3] w-[min(64rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto grid gap-3 max-w-[46rem]">
      <h2 id="gtw-13-h-fade" class="m-0 font-gtw13-display text-[clamp(1.4rem,3.6vw,2.1rem)] font-semibold leading-[1.1] tracking-[-0.03em] text-balance">The grained fade</h2>
      <p class="m-0 max-w-[42rem] text-[clamp(0.95rem,1.9vw,1.05rem)] text-pretty">The workhorse. A <code class="font-gtw13-mono text-[0.9em]">linear-gradient</code> mask dissolves the section boundary over 8rem while the grain layer continues at identical weight on both sides. Use it in long documents where you want sections to breathe without adding visual events. It costs one mask and no extra DOM.</p>
      <ul class="list-none mt-[0.4rem] mb-0 p-0 flex flex-wrap gap-y-2 gap-x-[1.8rem]">
        <li class="grid gap-[0.1rem]"><b class="font-gtw13-display text-[0.8rem] font-semibold leading-tight">Mask</b><span class="font-gtw13-mono text-[0.78rem] leading-tight">linear-gradient, 8rem</span></li>
        <li class="grid gap-[0.1rem]"><b class="font-gtw13-display text-[0.8rem] font-semibold leading-tight">Grain</b><span class="font-gtw13-mono text-[0.78rem] leading-tight">continuous, 0.05</span></li>
        <li class="grid gap-[0.1rem]"><b class="font-gtw13-display text-[0.8rem] font-semibold leading-tight">DOM added</b><span class="font-gtw13-mono text-[0.78rem] leading-tight">none</span></li>
      </ul>
    </div>
    <span aria-hidden="true" class="gtw-13-fade absolute inset-x-0 bottom-0 z-[2] h-[clamp(5rem,12vw,8rem)] bg-gtw13-bottom pointer-events-none"></span>
  </section>

  <section class="gtw-13-ruled relative isolate bg-gtw13-bottom pt-[clamp(3rem,8vw,5rem)] pb-[clamp(3.5rem,9vw,6rem)]" aria-labelledby="gtw-13-h-rule">
    <span aria-hidden="true" class="absolute inset-x-0 inset-y-[calc(var(--gtw13-tear)*-1)] z-[1] pointer-events-none bg-[image:var(--gtw13-noise)] opacity-[var(--gtw13-grain)] mix-blend-overlay"></span>
    <div class="relative z-[3] w-[min(64rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto grid gap-3 max-w-[46rem]">
      <h2 id="gtw-13-h-rule" class="m-0 font-gtw13-display text-[clamp(1.4rem,3.6vw,2.1rem)] font-semibold leading-[1.1] tracking-[-0.03em] text-balance">The ruled divider that does not look like a border</h2>
      <p class="m-0 max-w-[42rem] text-[clamp(0.95rem,1.9vw,1.05rem)] text-pretty">A hairline with a grain wash spilling past it in both directions. Utilitarian, appropriate in dashboards and documentation, and the only one of the three that survives being used a dozen times on one page.</p>
      <p class="mt-2 mb-0 pt-[0.8rem] border-t border-[color-mix(in_oklab,var(--color-gtw13-ink)_16%,transparent)] text-gtw13-mut text-[0.85rem] text-pretty">Pick one divider per page. This demo shows all three because it is a specimen sheet — shipping all three would be a design failure, not a feature.</p>
    </div>
  </section>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw13-top: #e9ecdf;
  --color-gtw13-top: oklch(0.93 0.02 120);
  --color-gtw13-mid: #47543a;
  --color-gtw13-mid: oklch(0.42 0.05 130);
  --color-gtw13-bottom: #f4f5ee;
  --color-gtw13-bottom: oklch(0.96 0.01 120);
  --color-gtw13-ink: #1f2418;
  --color-gtw13-ink: oklch(0.24 0.02 125);
  --color-gtw13-onmid: #eef2e4;
  --color-gtw13-onmid: oklch(0.95 0.015 120);
  --color-gtw13-mut: #616a55;
  --color-gtw13-mut: oklch(0.47 0.025 125);
  --color-gtw13-acc: #5f7a26;
  --color-gtw13-acc: oklch(0.52 0.12 128);
  --font-gtw13-display: 'Space Grotesk', 'Inter Tight', ui-sans-serif, system-ui, sans-serif;
  --font-gtw13-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}

.gtw-13 {
  width: 100%;
  min-height: 100svh;
  --gtw13-grain: 0.05;
  --gtw13-tear: clamp(3rem, 8vw, 6rem);
  --gtw13-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='170' height='170'%3E%3Cfilter id='gtw13n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='170' height='170' filter='url(%23gtw13n)'/%3E%3C/svg%3E");
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.6;
}
/* Gradient mask + the -webkit- twin Tailwind does not emit. */

.gtw-13-fade {
  -webkit-mask-image: linear-gradient(to bottom, transparent, #000 82%);
  mask-image: linear-gradient(to bottom, transparent, #000 82%);
}
/* The hairline rule: a ::before on the band, because it must sit inside the band's own
   centred measure rather than being a border on it. */

.gtw-13-ruled::before {
  content: "";
  display: block;
  block-size: 1px;
  inline-size: min(64rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin: 0 auto clamp(2rem, 5vw, 3rem);
  background: color-mix(in oklab, var(--color-gtw13-ink) 20%, transparent);
}

.gtw-13:has(.gtw-13-theme:checked) {
  --color-gtw13-top: #171a13;
  --color-gtw13-top: oklch(0.2 0.02 125);
  --color-gtw13-mid: #2b3324;
  --color-gtw13-mid: oklch(0.28 0.04 130);
  --color-gtw13-bottom: #101208;
  --color-gtw13-bottom: oklch(0.16 0.02 118);
  --color-gtw13-ink: #e8eddd;
  --color-gtw13-ink: oklch(0.94 0.015 120);
  --color-gtw13-onmid: #e8eddd;
  --color-gtw13-onmid: oklch(0.94 0.015 120);
  --color-gtw13-mut: #9aa68c;
  --color-gtw13-mut: oklch(0.71 0.025 125);
  --color-gtw13-acc: #b6d16a;
  --color-gtw13-acc: oklch(0.83 0.15 122);
  --gtw13-grain: 0.075;
}

@media (prefers-color-scheme: dark) {
  .gtw-13 {
    --color-gtw13-top: #171a13;
    --color-gtw13-top: oklch(0.2 0.02 125);
    --color-gtw13-mid: #2b3324;
    --color-gtw13-mid: oklch(0.28 0.04 130);
    --color-gtw13-bottom: #101208;
    --color-gtw13-bottom: oklch(0.16 0.02 118);
    --color-gtw13-ink: #e8eddd;
    --color-gtw13-ink: oklch(0.94 0.015 120);
    --color-gtw13-onmid: #e8eddd;
    --color-gtw13-onmid: oklch(0.94 0.015 120);
    --color-gtw13-mut: #9aa68c;
    --color-gtw13-mut: oklch(0.71 0.025 125);
    --color-gtw13-acc: #b6d16a;
    --color-gtw13-acc: oklch(0.83 0.15 122);
    --gtw13-grain: 0.075;
  }

  .gtw-13:has(.gtw-13-theme:checked) {
    --color-gtw13-top: #e9ecdf;
    --color-gtw13-top: oklch(0.93 0.02 120);
    --color-gtw13-mid: #47543a;
    --color-gtw13-mid: oklch(0.42 0.05 130);
    --color-gtw13-bottom: #f4f5ee;
    --color-gtw13-bottom: oklch(0.96 0.01 120);
    --color-gtw13-ink: #1f2418;
    --color-gtw13-ink: oklch(0.24 0.02 125);
    --color-gtw13-onmid: #eef2e4;
    --color-gtw13-onmid: oklch(0.95 0.015 120);
    --color-gtw13-mut: #616a55;
    --color-gtw13-mut: oklch(0.47 0.025 125);
    --color-gtw13-acc: #5f7a26;
    --color-gtw13-acc: oklch(0.52 0.12 128);
    --gtw13-grain: 0.05;
  }
}

@media (prefers-color-scheme: light) {
  .gtw-13:has(.gtw-13-theme:checked) {
    --color-gtw13-top: #171a13;
    --color-gtw13-top: oklch(0.2 0.02 125);
    --color-gtw13-mid: #2b3324;
    --color-gtw13-mid: oklch(0.28 0.04 130);
    --color-gtw13-bottom: #101208;
    --color-gtw13-bottom: oklch(0.16 0.02 118);
    --color-gtw13-ink: #e8eddd;
    --color-gtw13-ink: oklch(0.94 0.015 120);
    --color-gtw13-onmid: #e8eddd;
    --color-gtw13-onmid: oklch(0.94 0.015 120);
    --color-gtw13-mut: #9aa68c;
    --color-gtw13-mut: oklch(0.71 0.025 125);
    --color-gtw13-acc: #b6d16a;
    --color-gtw13-acc: oklch(0.83 0.15 122);
    --gtw13-grain: 0.075;
  }
}
```
