---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-tactile-card-surface-subtle-noise/"
title: "Tailwind Tactile Card Surface with Subtle Noise"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "Six product cards, identical except for one thing: grain weight tied to elevation."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Tactile Card Surface with Subtle Noise
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-tactile-card-surface-subtle-noise/

Six product cards, identical except for one thing: grain weight tied to elevation. A card that sits higher catches more light and shows more tooth, so its noise is stronger — and the sixth card, with zero grain and the same fill, shadow and radius, is the one that looks like plastic. Four to eight percent opacity is the entire difference between a surface and a rectangle.
## HTML
```html
<section class="gtw-09 relative block w-full min-h-svh bg-gtw09-bg text-gtw09-ink [background-image:var(--gtw09-noise),linear-gradient(var(--color-gtw09-bg),var(--color-gtw09-bg))] [background-blend-mode:multiply,normal]" aria-labelledby="gtw-09-title">
  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-40">
    <input type="checkbox" id="gtw-09-theme" class="gtw-09-theme peer sr-only">
    <label for="gtw-09-theme" class="grid place-items-center w-11 h-11 rounded-full border border-gtw09-line bg-gtw09-surf text-gtw09-ink cursor-pointer shadow-[inset_0_1px_0_var(--gtw09-hl)] transition-colors duration-200 hover:border-gtw09-acc peer-focus-visible:outline-2 peer-focus-visible:outline-gtw09-acc peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <main class="w-[min(74rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto pt-[clamp(3rem,8vw,5.5rem)] pb-[clamp(2.5rem,6vw,4rem)] grid gap-[clamp(2rem,5vw,3rem)]">
    <header class="max-w-[44rem] grid gap-[0.6rem]">
      <p class="m-0 font-gtw09-mono text-[0.72rem] font-medium leading-none tracking-[0.16em] uppercase text-gtw09-acc">Objects · winter catalogue</p>
      <h1 id="gtw-09-title" class="m-0 font-gtw09-display text-[clamp(2rem,5.4vw,3.4rem)] font-semibold leading-[1.03] tracking-[-0.035em] text-balance">Surfaces you can almost feel</h1>
      <p class="m-0 max-w-[38rem] text-gtw09-mut text-[clamp(0.95rem,1.9vw,1.08rem)] text-pretty">Every card carries the same noise token at a weight tied to its elevation, plus a lit top edge. Four percent opacity is the entire difference between plastic and material.</p>
    </header>

    <ul class="list-none m-0 p-0 grid gap-[clamp(0.9rem,2.2vw,1.4rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,16rem),1fr))]">
      <li class="group relative isolate overflow-hidden grid content-start gap-[0.45rem] min-w-0 p-[clamp(1.1rem,2.6vw,1.5rem)] rounded-2xl border border-gtw09-line bg-gtw09-surf [--gtw09-w:var(--gtw09-e3)] shadow-[inset_0_1px_0_var(--gtw09-hl),0_18px_40px_-22px_oklch(0.25_0.03_60/0.35)] transition-[translate,box-shadow] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw09-noise)] after:[mix-blend-mode:var(--gtw09-blend)] after:opacity-[var(--gtw09-w)] after:transition-opacity after:duration-[260ms] group-hover:after:opacity-[calc(var(--gtw09-w)*1.35)]">
        <p class="m-0 font-gtw09-mono text-[0.68rem] font-medium leading-none tracking-[0.12em] uppercase text-gtw09-mut">Elevation 3 · 0.055</p>
        <h2 class="m-0 font-gtw09-display text-[1.08rem] font-semibold leading-[1.25] tracking-[-0.015em] text-balance">Cast brass desk bell</h2>
        <p class="m-0 text-gtw09-mut text-[0.87rem] text-pretty">Solid brass, unlacquered. Develops a patina.</p>
        <div class="flex items-center justify-between gap-3 mt-2 pt-3 border-t border-gtw09-line">
          <span class="font-gtw09-mono text-[1.05rem] font-semibold leading-none">$58</span>
          <a href="#gtw-09-title" class="inline-flex items-center min-h-11 px-[1.05rem] rounded-[10px] no-underline font-gtw09-display text-[0.85rem] font-semibold leading-none text-gtw09-surf bg-[image:var(--gtw09-noise),linear-gradient(var(--color-gtw09-acc),var(--color-gtw09-acc))] [background-blend-mode:soft-light,normal] shadow-[inset_0_1px_0_rgba(255,255,255,0.22)] transition-[filter] duration-200 hover:brightness-[1.07] focus-visible:outline-2 focus-visible:outline-gtw09-acc focus-visible:outline-offset-[3px]">Add</a>
        </div>
      </li>
      <li class="group relative isolate overflow-hidden grid content-start gap-[0.45rem] min-w-0 p-[clamp(1.1rem,2.6vw,1.5rem)] rounded-2xl border border-gtw09-line bg-gtw09-surf [--gtw09-w:var(--gtw09-e2)] shadow-[inset_0_1px_0_var(--gtw09-hl),0_6px_14px_-8px_oklch(0.25_0.03_60/0.22)] transition-[translate,box-shadow] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw09-noise)] after:[mix-blend-mode:var(--gtw09-blend)] after:opacity-[var(--gtw09-w)] after:transition-opacity after:duration-[260ms] group-hover:after:opacity-[calc(var(--gtw09-w)*1.35)]">
        <p class="m-0 font-gtw09-mono text-[0.68rem] font-medium leading-none tracking-[0.12em] uppercase text-gtw09-mut">Elevation 2 · 0.045</p>
        <h2 class="m-0 font-gtw09-display text-[1.08rem] font-semibold leading-[1.25] tracking-[-0.015em] text-balance">Linen-bound notebook</h2>
        <p class="m-0 text-gtw09-mut text-[0.87rem] text-pretty">120gsm, lies flat, 192 pages.</p>
        <div class="flex items-center justify-between gap-3 mt-2 pt-3 border-t border-gtw09-line">
          <span class="font-gtw09-mono text-[1.05rem] font-semibold leading-none">$26</span>
          <a href="#gtw-09-title" class="inline-flex items-center min-h-11 px-[1.05rem] rounded-[10px] no-underline font-gtw09-display text-[0.85rem] font-semibold leading-none text-gtw09-surf bg-[image:var(--gtw09-noise),linear-gradient(var(--color-gtw09-acc),var(--color-gtw09-acc))] [background-blend-mode:soft-light,normal] shadow-[inset_0_1px_0_rgba(255,255,255,0.22)] transition-[filter] duration-200 hover:brightness-[1.07] focus-visible:outline-2 focus-visible:outline-gtw09-acc focus-visible:outline-offset-[3px]">Add</a>
        </div>
      </li>
      <li class="group relative isolate overflow-hidden grid content-start gap-[0.45rem] min-w-0 p-[clamp(1.1rem,2.6vw,1.5rem)] rounded-2xl border border-gtw09-line bg-gtw09-surf [--gtw09-w:var(--gtw09-e1)] shadow-[inset_0_1px_0_var(--gtw09-hl),0_1px_2px_oklch(0.25_0.03_60/0.08)] transition-[translate,box-shadow] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 hover:shadow-[inset_0_1px_0_var(--gtw09-hl),0_10px_22px_-12px_oklch(0.25_0.03_60/0.26)] motion-reduce:transition-none motion-reduce:hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw09-noise)] after:[mix-blend-mode:var(--gtw09-blend)] after:opacity-[var(--gtw09-w)] after:transition-opacity after:duration-[260ms] group-hover:after:opacity-[calc(var(--gtw09-w)*1.35)]">
        <p class="m-0 font-gtw09-mono text-[0.68rem] font-medium leading-none tracking-[0.12em] uppercase text-gtw09-mut">Elevation 1 · 0.035</p>
        <h2 class="m-0 font-gtw09-display text-[1.08rem] font-semibold leading-[1.25] tracking-[-0.015em] text-balance">Stoneware cup, glazed</h2>
        <p class="m-0 text-gtw09-mut text-[0.87rem] text-pretty">Wheel-thrown, small batch. Dishwasher safe.</p>
        <div class="flex items-center justify-between gap-3 mt-2 pt-3 border-t border-gtw09-line">
          <span class="font-gtw09-mono text-[1.05rem] font-semibold leading-none">$19</span>
          <a href="#gtw-09-title" class="inline-flex items-center min-h-11 px-[1.05rem] rounded-[10px] no-underline font-gtw09-display text-[0.85rem] font-semibold leading-none text-gtw09-surf bg-[image:var(--gtw09-noise),linear-gradient(var(--color-gtw09-acc),var(--color-gtw09-acc))] [background-blend-mode:soft-light,normal] shadow-[inset_0_1px_0_rgba(255,255,255,0.22)] transition-[filter] duration-200 hover:brightness-[1.07] focus-visible:outline-2 focus-visible:outline-gtw09-acc focus-visible:outline-offset-[3px]">Add</a>
        </div>
      </li>
      <li class="group relative isolate overflow-hidden grid content-start gap-[0.45rem] min-w-0 p-[clamp(1.1rem,2.6vw,1.5rem)] rounded-2xl border border-gtw09-line bg-gtw09-surf [--gtw09-w:var(--gtw09-e2)] shadow-[inset_0_1px_0_var(--gtw09-hl),0_6px_14px_-8px_oklch(0.25_0.03_60/0.22)] transition-[translate,box-shadow] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw09-noise)] after:[mix-blend-mode:var(--gtw09-blend)] after:opacity-[var(--gtw09-w)] after:transition-opacity after:duration-[260ms] group-hover:after:opacity-[calc(var(--gtw09-w)*1.35)]">
        <p class="m-0 font-gtw09-mono text-[0.68rem] font-medium leading-none tracking-[0.12em] uppercase text-gtw09-mut">Elevation 2 · 0.045</p>
        <h2 class="m-0 font-gtw09-display text-[1.08rem] font-semibold leading-[1.25] tracking-[-0.015em] text-balance">Waxed canvas tool roll</h2>
        <p class="m-0 text-gtw09-mut text-[0.87rem] text-pretty">18oz canvas, brass press studs.</p>
        <div class="flex items-center justify-between gap-3 mt-2 pt-3 border-t border-gtw09-line">
          <span class="font-gtw09-mono text-[1.05rem] font-semibold leading-none">$78</span>
          <a href="#gtw-09-title" class="inline-flex items-center min-h-11 px-[1.05rem] rounded-[10px] no-underline font-gtw09-display text-[0.85rem] font-semibold leading-none text-gtw09-surf bg-[image:var(--gtw09-noise),linear-gradient(var(--color-gtw09-acc),var(--color-gtw09-acc))] [background-blend-mode:soft-light,normal] shadow-[inset_0_1px_0_rgba(255,255,255,0.22)] transition-[filter] duration-200 hover:brightness-[1.07] focus-visible:outline-2 focus-visible:outline-gtw09-acc focus-visible:outline-offset-[3px]">Add</a>
        </div>
      </li>
      <li class="group relative isolate overflow-hidden grid content-start gap-[0.45rem] min-w-0 p-[clamp(1.1rem,2.6vw,1.5rem)] rounded-2xl border border-gtw09-line bg-gtw09-surf [--gtw09-w:var(--gtw09-e1)] shadow-[inset_0_1px_0_var(--gtw09-hl),0_1px_2px_oklch(0.25_0.03_60/0.08)] transition-[translate,box-shadow] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 hover:shadow-[inset_0_1px_0_var(--gtw09-hl),0_10px_22px_-12px_oklch(0.25_0.03_60/0.26)] motion-reduce:transition-none motion-reduce:hover:translate-y-0 after:content-[''] after:absolute after:inset-0 after:-z-[1] after:pointer-events-none after:bg-[image:var(--gtw09-noise)] after:[mix-blend-mode:var(--gtw09-blend)] after:opacity-[var(--gtw09-w)] after:transition-opacity after:duration-[260ms] group-hover:after:opacity-[calc(var(--gtw09-w)*1.35)]">
        <p class="m-0 font-gtw09-mono text-[0.68rem] font-medium leading-none tracking-[0.12em] uppercase text-gtw09-mut">Elevation 1 · 0.035</p>
        <h2 class="m-0 font-gtw09-display text-[1.08rem] font-semibold leading-[1.25] tracking-[-0.015em] text-balance">Beech drawing board</h2>
        <p class="m-0 text-gtw09-mut text-[0.87rem] text-pretty">Oiled beech, A3, cleated back.</p>
        <div class="flex items-center justify-between gap-3 mt-2 pt-3 border-t border-gtw09-line">
          <span class="font-gtw09-mono text-[1.05rem] font-semibold leading-none">$46</span>
          <a href="#gtw-09-title" class="inline-flex items-center min-h-11 px-[1.05rem] rounded-[10px] no-underline font-gtw09-display text-[0.85rem] font-semibold leading-none text-gtw09-surf bg-[image:var(--gtw09-noise),linear-gradient(var(--color-gtw09-acc),var(--color-gtw09-acc))] [background-blend-mode:soft-light,normal] shadow-[inset_0_1px_0_rgba(255,255,255,0.22)] transition-[filter] duration-200 hover:brightness-[1.07] focus-visible:outline-2 focus-visible:outline-gtw09-acc focus-visible:outline-offset-[3px]">Add</a>
        </div>
      </li>
      <li class="group relative isolate overflow-hidden grid content-start gap-[0.45rem] min-w-0 p-[clamp(1.1rem,2.6vw,1.5rem)] rounded-2xl border border-gtw09-line bg-gtw09-surf [--gtw09-w:0] shadow-[inset_0_1px_0_var(--gtw09-hl),0_6px_14px_-8px_oklch(0.25_0.03_60/0.22)] transition-[translate,box-shadow] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <p class="m-0 font-gtw09-mono text-[0.68rem] font-medium leading-none tracking-[0.12em] uppercase text-gtw09-mut">Control · 0</p>
        <h2 class="m-0 font-gtw09-display text-[1.08rem] font-semibold leading-[1.25] tracking-[-0.015em] text-balance">The same card, no grain</h2>
        <p class="m-0 text-gtw09-mut text-[0.87rem] text-pretty">Identical fill, shadow and radius. This is the one that looks like plastic.</p>
        <div class="flex items-center justify-between gap-3 mt-2 pt-3 border-t border-gtw09-line">
          <span class="font-gtw09-mono text-[1.05rem] font-semibold leading-none">—</span>
          <a href="#gtw-09-title" class="inline-flex items-center min-h-11 px-[1.05rem] rounded-[10px] no-underline font-gtw09-display text-[0.85rem] font-semibold leading-none text-gtw09-mut bg-transparent border border-gtw09-line transition-colors duration-200 hover:text-gtw09-ink hover:border-gtw09-acc focus-visible:outline-2 focus-visible:outline-gtw09-acc focus-visible:outline-offset-[3px]">Compare</a>
        </div>
      </li>
    </ul>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw09-bg: #efe9df;
  --color-gtw09-bg: oklch(0.93 0.015 80);
  --color-gtw09-surf: #fbf8f3;
  --color-gtw09-surf: oklch(0.98 0.008 85);
  --color-gtw09-line: #ddd4c6;
  --color-gtw09-line: oklch(0.87 0.018 80);
  --color-gtw09-ink: #211d17;
  --color-gtw09-ink: oklch(0.24 0.012 75);
  --color-gtw09-mut: #6c6355;
  --color-gtw09-mut: oklch(0.48 0.02 80);
  --color-gtw09-acc: #8a5a2b;
  --color-gtw09-acc: oklch(0.5 0.1 62);
  --font-gtw09-display: 'Space Grotesk', 'Inter Tight', ui-sans-serif, system-ui, sans-serif;
  --font-gtw09-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}

.gtw-09 {
  width: 100%;
  min-height: 100svh;
  --gtw09-e1: 0.035;
  --gtw09-e2: 0.045;
  --gtw09-e3: 0.055;
  --gtw09-blend: multiply;
  --gtw09-hl: rgba(255, 255, 255, 0.9);
  --gtw09-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='gtw09n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23gtw09n)'/%3E%3C/svg%3E");
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
}

.gtw-09:has(.gtw-09-theme:checked) {
  --color-gtw09-bg: #14120f;
  --color-gtw09-bg: oklch(0.19 0.008 75);
  --color-gtw09-surf: #1e1b16;
  --color-gtw09-surf: oklch(0.24 0.01 75);
  --color-gtw09-line: #322c23;
  --color-gtw09-line: oklch(0.32 0.015 78);
  --color-gtw09-ink: #f3eee5;
  --color-gtw09-ink: oklch(0.95 0.01 85);
  --color-gtw09-mut: #a79c8b;
  --color-gtw09-mut: oklch(0.71 0.02 80);
  --color-gtw09-acc: #e0a463;
  --color-gtw09-acc: oklch(0.78 0.12 70);
  --gtw09-blend: overlay;
  --gtw09-hl: rgba(255, 255, 255, 0.14);
  --gtw09-e1: 0.05;
  --gtw09-e2: 0.065;
  --gtw09-e3: 0.08;
}

@media (prefers-color-scheme: dark) {
  .gtw-09 {
    --color-gtw09-bg: #14120f;
    --color-gtw09-bg: oklch(0.19 0.008 75);
    --color-gtw09-surf: #1e1b16;
    --color-gtw09-surf: oklch(0.24 0.01 75);
    --color-gtw09-line: #322c23;
    --color-gtw09-line: oklch(0.32 0.015 78);
    --color-gtw09-ink: #f3eee5;
    --color-gtw09-ink: oklch(0.95 0.01 85);
    --color-gtw09-mut: #a79c8b;
    --color-gtw09-mut: oklch(0.71 0.02 80);
    --color-gtw09-acc: #e0a463;
    --color-gtw09-acc: oklch(0.78 0.12 70);
    --gtw09-blend: overlay;
    --gtw09-hl: rgba(255, 255, 255, 0.14);
    --gtw09-e1: 0.05;
    --gtw09-e2: 0.065;
    --gtw09-e3: 0.08;
  }

  .gtw-09:has(.gtw-09-theme:checked) {
    --color-gtw09-bg: #efe9df;
    --color-gtw09-bg: oklch(0.93 0.015 80);
    --color-gtw09-surf: #fbf8f3;
    --color-gtw09-surf: oklch(0.98 0.008 85);
    --color-gtw09-line: #ddd4c6;
    --color-gtw09-line: oklch(0.87 0.018 80);
    --color-gtw09-ink: #211d17;
    --color-gtw09-ink: oklch(0.24 0.012 75);
    --color-gtw09-mut: #6c6355;
    --color-gtw09-mut: oklch(0.48 0.02 80);
    --color-gtw09-acc: #8a5a2b;
    --color-gtw09-acc: oklch(0.5 0.1 62);
    --gtw09-blend: multiply;
    --gtw09-hl: rgba(255, 255, 255, 0.9);
    --gtw09-e1: 0.035;
    --gtw09-e2: 0.045;
    --gtw09-e3: 0.055;
  }
}

@media (prefers-color-scheme: light) {
  .gtw-09:has(.gtw-09-theme:checked) {
    --color-gtw09-bg: #14120f;
    --color-gtw09-bg: oklch(0.19 0.008 75);
    --color-gtw09-surf: #1e1b16;
    --color-gtw09-surf: oklch(0.24 0.01 75);
    --color-gtw09-line: #322c23;
    --color-gtw09-line: oklch(0.32 0.015 78);
    --color-gtw09-ink: #f3eee5;
    --color-gtw09-ink: oklch(0.95 0.01 85);
    --color-gtw09-mut: #a79c8b;
    --color-gtw09-mut: oklch(0.71 0.02 80);
    --color-gtw09-acc: #e0a463;
    --color-gtw09-acc: oklch(0.78 0.12 70);
    --gtw09-blend: overlay;
    --gtw09-hl: rgba(255, 255, 255, 0.14);
    --gtw09-e1: 0.05;
    --gtw09-e2: 0.065;
    --gtw09-e3: 0.08;
  }
}
```
