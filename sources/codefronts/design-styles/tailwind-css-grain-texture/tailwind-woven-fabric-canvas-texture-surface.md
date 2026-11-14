---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-woven-fabric-canvas-texture-surface/"
title: "Tailwind Woven Fabric and Canvas Texture Surface"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "Four upholstery fabrics — linen, canvas, hessian, denim — built from two crossed repeating-linear-gradients, a highlight pass and a turbulence slub layer."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Woven Fabric and Canvas Texture Surface
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-woven-fabric-canvas-texture-surface/

Four upholstery fabrics — linen, canvas, hessian, denim — built from two crossed repeating-linear-gradients, a highlight pass and a turbulence slub layer. Under 500 bytes each, tiling perfectly by construction, and fully recolourable, which is the version that actually works in a product configurator where the customer picks the colour.
## HTML
```html
<section class="gtw-18 relative block w-full min-h-svh bg-gtw18-bg text-gtw18-ink" aria-labelledby="gtw-18-title">
  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-40">
    <input type="checkbox" id="gtw-18-theme" class="gtw-18-theme peer sr-only">
    <label for="gtw-18-theme" class="grid place-items-center w-11 h-11 rounded-full border border-gtw18-line bg-gtw18-surf text-gtw18-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-gtw18-acc peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <main class="w-[min(76rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto pt-[clamp(3rem,8vw,5rem)] pb-[clamp(2.5rem,6vw,4rem)] grid gap-[clamp(2rem,5vw,3rem)]">
    <header class="max-w-[46rem] grid gap-[0.6rem]">
      <p class="m-0 font-gtw18-mono text-[0.72rem] font-medium leading-none tracking-[0.18em] uppercase text-gtw18-acc">Material library · upholstery</p>
      <h1 id="gtw-18-title" class="m-0 font-gtw18-display text-[clamp(2rem,5.2vw,3.3rem)] font-semibold leading-[1.04] tracking-[-0.035em] text-balance">Four fabrics, three numbers, no photography</h1>
      <p class="m-0 max-w-[40rem] text-gtw18-mut text-[clamp(0.95rem,1.9vw,1.07rem)] text-pretty">Warp and weft as two crossed <code class="font-gtw18-mono text-[0.9em]">repeating-linear-gradient</code>s, irregularity from turbulence, and every swatch recolourable because none of it is an image.</p>
    </header>

    <ul class="list-none m-0 p-0 grid gap-[clamp(1rem,2.4vw,1.5rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,18rem),1fr))]">
      <li class="grid grid-rows-[auto_1fr] min-w-0 overflow-hidden rounded-[14px] border border-gtw18-line bg-gtw18-surf transition-[translate,border-color] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 hover:border-gtw18-acc motion-reduce:transition-none motion-reduce:hover:translate-y-0 [--gtw18-pitch:3px] [--gtw18-thread:1.2px] [--gtw18-depth:0.1] [--gtw18-col:#c9b79a]">
        <span aria-hidden="true" class="relative isolate block h-[clamp(9rem,20vw,12rem)] bg-[color:var(--gtw18-col)] [background-image:repeating-linear-gradient(90deg,rgba(0,0,0,var(--gtw18-depth))_0_var(--gtw18-thread),transparent_var(--gtw18-thread)_var(--gtw18-pitch)),repeating-linear-gradient(0deg,rgba(0,0,0,var(--gtw18-depth))_0_var(--gtw18-thread),transparent_var(--gtw18-thread)_var(--gtw18-pitch)),repeating-linear-gradient(90deg,rgba(255,255,255,calc(var(--gtw18-depth)*0.55))_0_1px,transparent_1px_var(--gtw18-pitch))] [background-blend-mode:multiply,multiply,screen]">
          <span class="gtw-18-slub absolute inset-0 pointer-events-none bg-[image:var(--gtw18-noise)] opacity-[var(--gtw18-slub)] mix-blend-multiply"></span>
        </span>
        <div class="grid content-start gap-2 p-[clamp(1rem,2.4vw,1.4rem)]">
          <div class="flex items-baseline justify-between gap-[0.6rem]"><h2 class="m-0 font-gtw18-display text-[1.05rem] font-semibold leading-tight tracking-[-0.02em]">Belgian linen</h2><span class="font-gtw18-mono text-[0.72rem] leading-none tracking-[0.1em] text-gtw18-mut">LN-04</span></div>
          <p class="m-0 text-gtw18-mut text-[0.87rem] text-pretty">Fine pitch, low contrast. The closest weave to a plain surface — use it where texture should be felt rather than seen.</p>
          <dl class="flex flex-wrap gap-y-[0.3rem] gap-x-[1.2rem] mt-[0.2rem] mb-0 pt-[0.7rem] border-t border-gtw18-line">
            <div class="grid gap-[0.05rem]"><dt class="m-0 font-gtw18-mono text-[0.64rem] leading-none tracking-[0.1em] uppercase text-gtw18-mut">pitch</dt><dd class="m-0 font-gtw18-mono text-[0.85rem] font-medium leading-none">3px</dd></div>
            <div class="grid gap-[0.05rem]"><dt class="m-0 font-gtw18-mono text-[0.64rem] leading-none tracking-[0.1em] uppercase text-gtw18-mut">thread</dt><dd class="m-0 font-gtw18-mono text-[0.85rem] font-medium leading-none">1.2px</dd></div>
            <div class="grid gap-[0.05rem]"><dt class="m-0 font-gtw18-mono text-[0.64rem] leading-none tracking-[0.1em] uppercase text-gtw18-mut">depth</dt><dd class="m-0 font-gtw18-mono text-[0.85rem] font-medium leading-none">0.10</dd></div>
          </dl>
        </div>
      </li>

      <li class="grid grid-rows-[auto_1fr] min-w-0 overflow-hidden rounded-[14px] border border-gtw18-line bg-gtw18-surf transition-[translate,border-color] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 hover:border-gtw18-acc motion-reduce:transition-none motion-reduce:hover:translate-y-0 [--gtw18-pitch:6px] [--gtw18-thread:2.4px] [--gtw18-depth:0.16] [--gtw18-col:#d9cfb8]">
        <span aria-hidden="true" class="relative isolate block h-[clamp(9rem,20vw,12rem)] bg-[color:var(--gtw18-col)] [background-image:repeating-linear-gradient(90deg,rgba(0,0,0,var(--gtw18-depth))_0_var(--gtw18-thread),transparent_var(--gtw18-thread)_var(--gtw18-pitch)),repeating-linear-gradient(0deg,rgba(0,0,0,var(--gtw18-depth))_0_var(--gtw18-thread),transparent_var(--gtw18-thread)_var(--gtw18-pitch)),repeating-linear-gradient(90deg,rgba(255,255,255,calc(var(--gtw18-depth)*0.55))_0_1px,transparent_1px_var(--gtw18-pitch))] [background-blend-mode:multiply,multiply,screen]">
          <span class="gtw-18-slub absolute inset-0 pointer-events-none bg-[image:var(--gtw18-noise)] opacity-[var(--gtw18-slub)] mix-blend-multiply"></span>
        </span>
        <div class="grid content-start gap-2 p-[clamp(1rem,2.4vw,1.4rem)]">
          <div class="flex items-baseline justify-between gap-[0.6rem]"><h2 class="m-0 font-gtw18-display text-[1.05rem] font-semibold leading-tight tracking-[-0.02em]">Cotton canvas</h2><span class="font-gtw18-mono text-[0.72rem] leading-none tracking-[0.1em] text-gtw18-mut">CV-12</span></div>
          <p class="m-0 text-gtw18-mut text-[0.87rem] text-pretty">Medium pitch, heavier thread. The default upholstery weight, and the one that photographs worst — so build it in CSS.</p>
          <dl class="flex flex-wrap gap-y-[0.3rem] gap-x-[1.2rem] mt-[0.2rem] mb-0 pt-[0.7rem] border-t border-gtw18-line">
            <div class="grid gap-[0.05rem]"><dt class="m-0 font-gtw18-mono text-[0.64rem] leading-none tracking-[0.1em] uppercase text-gtw18-mut">pitch</dt><dd class="m-0 font-gtw18-mono text-[0.85rem] font-medium leading-none">6px</dd></div>
            <div class="grid gap-[0.05rem]"><dt class="m-0 font-gtw18-mono text-[0.64rem] leading-none tracking-[0.1em] uppercase text-gtw18-mut">thread</dt><dd class="m-0 font-gtw18-mono text-[0.85rem] font-medium leading-none">2.4px</dd></div>
            <div class="grid gap-[0.05rem]"><dt class="m-0 font-gtw18-mono text-[0.64rem] leading-none tracking-[0.1em] uppercase text-gtw18-mut">depth</dt><dd class="m-0 font-gtw18-mono text-[0.85rem] font-medium leading-none">0.16</dd></div>
          </dl>
        </div>
      </li>

      <li class="grid grid-rows-[auto_1fr] min-w-0 overflow-hidden rounded-[14px] border border-gtw18-line bg-gtw18-surf transition-[translate,border-color] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 hover:border-gtw18-acc motion-reduce:transition-none motion-reduce:hover:translate-y-0 [--gtw18-pitch:11px] [--gtw18-thread:4.5px] [--gtw18-depth:0.26] [--gtw18-col:#b1935f]">
        <span aria-hidden="true" class="relative isolate block h-[clamp(9rem,20vw,12rem)] bg-[color:var(--gtw18-col)] [background-image:repeating-linear-gradient(90deg,rgba(0,0,0,var(--gtw18-depth))_0_var(--gtw18-thread),transparent_var(--gtw18-thread)_var(--gtw18-pitch)),repeating-linear-gradient(0deg,rgba(0,0,0,var(--gtw18-depth))_0_var(--gtw18-thread),transparent_var(--gtw18-thread)_var(--gtw18-pitch)),repeating-linear-gradient(90deg,rgba(255,255,255,calc(var(--gtw18-depth)*0.55))_0_1px,transparent_1px_var(--gtw18-pitch))] [background-blend-mode:multiply,multiply,screen]">
          <span class="gtw-18-slub absolute inset-0 pointer-events-none bg-[image:var(--gtw18-noise)] opacity-[calc(var(--gtw18-slub)*1.8)] mix-blend-multiply"></span>
        </span>
        <div class="grid content-start gap-2 p-[clamp(1rem,2.4vw,1.4rem)]">
          <div class="flex items-baseline justify-between gap-[0.6rem]"><h2 class="m-0 font-gtw18-display text-[1.05rem] font-semibold leading-tight tracking-[-0.02em]">Jute hessian</h2><span class="font-gtw18-mono text-[0.72rem] leading-none tracking-[0.1em] text-gtw18-mut">HS-01</span></div>
          <p class="m-0 text-gtw18-mut text-[0.87rem] text-pretty">Wide pitch, high contrast, heavy slub. Open enough that the backing colour reads through the gaps.</p>
          <dl class="flex flex-wrap gap-y-[0.3rem] gap-x-[1.2rem] mt-[0.2rem] mb-0 pt-[0.7rem] border-t border-gtw18-line">
            <div class="grid gap-[0.05rem]"><dt class="m-0 font-gtw18-mono text-[0.64rem] leading-none tracking-[0.1em] uppercase text-gtw18-mut">pitch</dt><dd class="m-0 font-gtw18-mono text-[0.85rem] font-medium leading-none">11px</dd></div>
            <div class="grid gap-[0.05rem]"><dt class="m-0 font-gtw18-mono text-[0.64rem] leading-none tracking-[0.1em] uppercase text-gtw18-mut">thread</dt><dd class="m-0 font-gtw18-mono text-[0.85rem] font-medium leading-none">4.5px</dd></div>
            <div class="grid gap-[0.05rem]"><dt class="m-0 font-gtw18-mono text-[0.64rem] leading-none tracking-[0.1em] uppercase text-gtw18-mut">depth</dt><dd class="m-0 font-gtw18-mono text-[0.85rem] font-medium leading-none">0.26</dd></div>
          </dl>
        </div>
      </li>

      <li class="grid grid-rows-[auto_1fr] min-w-0 overflow-hidden rounded-[14px] border border-gtw18-line bg-gtw18-surf transition-[translate,border-color] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 hover:border-gtw18-acc motion-reduce:transition-none motion-reduce:hover:translate-y-0 [--gtw18-pitch:4px] [--gtw18-thread:1.8px] [--gtw18-depth:0.2] [--gtw18-col:#3f5878]">
        <span aria-hidden="true" class="relative isolate block h-[clamp(9rem,20vw,12rem)] bg-[color:var(--gtw18-col)] [background-image:repeating-linear-gradient(90deg,rgba(0,0,0,var(--gtw18-depth))_0_var(--gtw18-thread),transparent_var(--gtw18-thread)_var(--gtw18-pitch)),repeating-linear-gradient(0deg,rgba(0,0,0,var(--gtw18-depth))_0_var(--gtw18-thread),transparent_var(--gtw18-thread)_var(--gtw18-pitch)),repeating-linear-gradient(90deg,rgba(255,255,255,calc(var(--gtw18-depth)*0.55))_0_1px,transparent_1px_var(--gtw18-pitch))] [background-blend-mode:multiply,multiply,screen]">
          <span class="gtw-18-slub absolute inset-0 pointer-events-none bg-[image:var(--gtw18-nap)] opacity-[calc(var(--gtw18-slub)*1.5)] mix-blend-overlay"></span>
        </span>
        <div class="grid content-start gap-2 p-[clamp(1rem,2.4vw,1.4rem)]">
          <div class="flex items-baseline justify-between gap-[0.6rem]"><h2 class="m-0 font-gtw18-display text-[1.05rem] font-semibold leading-tight tracking-[-0.02em]">Indigo denim</h2><span class="font-gtw18-mono text-[0.72rem] leading-none tracking-[0.1em] text-gtw18-mut">DN-08</span></div>
          <p class="m-0 text-gtw18-mut text-[0.87rem] text-pretty">Plain weave plus an anisotropic nap layer, which gives the surface a direction the way real twill does.</p>
          <dl class="flex flex-wrap gap-y-[0.3rem] gap-x-[1.2rem] mt-[0.2rem] mb-0 pt-[0.7rem] border-t border-gtw18-line">
            <div class="grid gap-[0.05rem]"><dt class="m-0 font-gtw18-mono text-[0.64rem] leading-none tracking-[0.1em] uppercase text-gtw18-mut">pitch</dt><dd class="m-0 font-gtw18-mono text-[0.85rem] font-medium leading-none">4px</dd></div>
            <div class="grid gap-[0.05rem]"><dt class="m-0 font-gtw18-mono text-[0.64rem] leading-none tracking-[0.1em] uppercase text-gtw18-mut">nap</dt><dd class="m-0 font-gtw18-mono text-[0.85rem] font-medium leading-none">0.02 0.9</dd></div>
            <div class="grid gap-[0.05rem]"><dt class="m-0 font-gtw18-mono text-[0.64rem] leading-none tracking-[0.1em] uppercase text-gtw18-mut">depth</dt><dd class="m-0 font-gtw18-mono text-[0.85rem] font-medium leading-none">0.20</dd></div>
          </dl>
        </div>
      </li>
    </ul>

    <aside class="grid gap-2 p-[clamp(1.2rem,3vw,1.8rem)] rounded-[14px] border border-gtw18-line bg-gtw18-surf">
      <h2 class="m-0 font-gtw18-display text-[clamp(1.1rem,2.6vw,1.35rem)] font-semibold leading-tight">Why not a photograph</h2>
      <p class="m-0 max-w-[52rem] text-gtw18-mut text-[0.92rem] text-pretty">A fabric photo is 80–300KB, tiles visibly, and cannot be recoloured. This is under 500 bytes, tiles perfectly by construction, and takes its colour from your tokens — which is the only version that works in a configurator where the customer picks the colour.</p>
    </aside>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw18-bg: #f1ebe0;
  --color-gtw18-bg: oklch(0.94 0.015 85);
  --color-gtw18-surf: #fbf7ef;
  --color-gtw18-surf: oklch(0.98 0.01 88);
  --color-gtw18-line: #dcd2bf;
  --color-gtw18-line: oklch(0.87 0.02 85);
  --color-gtw18-ink: #241f17;
  --color-gtw18-ink: oklch(0.25 0.012 78);
  --color-gtw18-mut: #6b6252;
  --color-gtw18-mut: oklch(0.47 0.02 82);
  --color-gtw18-acc: #7a5a2e;
  --color-gtw18-acc: oklch(0.48 0.09 66);
  --font-gtw18-display: 'Space Grotesk', 'Inter Tight', ui-sans-serif, system-ui, sans-serif;
  --font-gtw18-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}

.gtw-18 {
  width: 100%;
  min-height: 100svh;
  --gtw18-pitch: 5px;
  --gtw18-thread: 2px;
  --gtw18-depth: 0.16;
  --gtw18-col: #d0c0a4;
  --gtw18-slub: 0.08;
  --gtw18-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='gtw18n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.6' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='180' height='180' filter='url(%23gtw18n)'/%3E%3C/svg%3E");
  --gtw18-nap: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='gtw18p'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.02 0.9' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='180' height='180' filter='url(%23gtw18p)'/%3E%3C/svg%3E");
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
}
/* Dense displays show the weave finer, so the slub comes up slightly to compensate. */

@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 2dppx) {
  .gtw-18-slub {
    opacity: calc(var(--gtw18-slub) * 1.15);
  }
}

.gtw-18:has(.gtw-18-theme:checked) {
  --color-gtw18-bg: #16130e;
  --color-gtw18-bg: oklch(0.19 0.01 80);
  --color-gtw18-surf: #1f1b15;
  --color-gtw18-surf: oklch(0.24 0.012 80);
  --color-gtw18-line: #342d22;
  --color-gtw18-line: oklch(0.32 0.018 80);
  --color-gtw18-ink: #f2ece0;
  --color-gtw18-ink: oklch(0.94 0.015 85);
  --color-gtw18-mut: #a49a86;
  --color-gtw18-mut: oklch(0.7 0.02 85);
  --color-gtw18-acc: #d7a75d;
  --color-gtw18-acc: oklch(0.77 0.11 72);
  --gtw18-slub: 0.12;
}

@media (prefers-color-scheme: dark) {
  .gtw-18 {
    --color-gtw18-bg: #16130e;
    --color-gtw18-bg: oklch(0.19 0.01 80);
    --color-gtw18-surf: #1f1b15;
    --color-gtw18-surf: oklch(0.24 0.012 80);
    --color-gtw18-line: #342d22;
    --color-gtw18-line: oklch(0.32 0.018 80);
    --color-gtw18-ink: #f2ece0;
    --color-gtw18-ink: oklch(0.94 0.015 85);
    --color-gtw18-mut: #a49a86;
    --color-gtw18-mut: oklch(0.7 0.02 85);
    --color-gtw18-acc: #d7a75d;
    --color-gtw18-acc: oklch(0.77 0.11 72);
    --gtw18-slub: 0.12;
  }

  .gtw-18:has(.gtw-18-theme:checked) {
    --color-gtw18-bg: #f1ebe0;
    --color-gtw18-bg: oklch(0.94 0.015 85);
    --color-gtw18-surf: #fbf7ef;
    --color-gtw18-surf: oklch(0.98 0.01 88);
    --color-gtw18-line: #dcd2bf;
    --color-gtw18-line: oklch(0.87 0.02 85);
    --color-gtw18-ink: #241f17;
    --color-gtw18-ink: oklch(0.25 0.012 78);
    --color-gtw18-mut: #6b6252;
    --color-gtw18-mut: oklch(0.47 0.02 82);
    --color-gtw18-acc: #7a5a2e;
    --color-gtw18-acc: oklch(0.48 0.09 66);
    --gtw18-slub: 0.08;
  }
}

@media (prefers-color-scheme: light) {
  .gtw-18:has(.gtw-18-theme:checked) {
    --color-gtw18-bg: #16130e;
    --color-gtw18-bg: oklch(0.19 0.01 80);
    --color-gtw18-surf: #1f1b15;
    --color-gtw18-surf: oklch(0.24 0.012 80);
    --color-gtw18-line: #342d22;
    --color-gtw18-line: oklch(0.32 0.018 80);
    --color-gtw18-ink: #f2ece0;
    --color-gtw18-ink: oklch(0.94 0.015 85);
    --color-gtw18-mut: #a49a86;
    --color-gtw18-mut: oklch(0.7 0.02 85);
    --color-gtw18-acc: #d7a75d;
    --color-gtw18-acc: oklch(0.77 0.11 72);
    --gtw18-slub: 0.12;
  }
}
```
