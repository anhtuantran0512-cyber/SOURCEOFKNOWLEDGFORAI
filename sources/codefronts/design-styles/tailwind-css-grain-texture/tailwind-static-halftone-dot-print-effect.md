---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-static-halftone-dot-print-effect/"
title: "Tailwind Static Halftone Dot Print Effect"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "A print halftone built from one radial-gradient tiled at a pitch, rotated to a screen angle, and blended over a high-contrast greyscale photograph."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Static Halftone Dot Print Effect
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-static-halftone-dot-print-effect/

A print halftone built from one radial-gradient tiled at a pitch, rotated to a screen angle, and blended over a high-contrast greyscale photograph. Three pitches on a specimen row, plus a two-ink duotone with its screens at 15° and 75° — thirty degrees apart, because that is what stops two dot grids from beating into moiré.
## HTML
```html
<section class="gtw-14 relative block w-full min-h-svh bg-gtw14-bg text-gtw14-ink" aria-labelledby="gtw-14-title">
  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-40">
    <input type="checkbox" id="gtw-14-theme" class="gtw-14-theme peer sr-only">
    <label for="gtw-14-theme" class="grid place-items-center w-11 h-11 rounded-full border border-gtw14-line bg-gtw14-surf text-gtw14-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-gtw14-acc peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <main class="w-[min(78rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto pt-[clamp(2.5rem,7vw,4.5rem)] pb-[clamp(2.5rem,6vw,4rem)] grid gap-[clamp(2rem,5vw,3.2rem)]">
    <header class="grid gap-2 pb-[clamp(1rem,3vw,1.6rem)] border-b-[3px] border-double border-gtw14-ink">
      <p class="m-0 font-gtw14-mono text-[0.72rem] leading-none tracking-[0.16em] uppercase text-gtw14-mut">Late edition · No. 214 · Printed on recycled stock</p>
      <h1 id="gtw-14-title" class="m-0 font-gtw14-display text-[clamp(2.8rem,10vw,6.5rem)] font-normal leading-[0.92] tracking-[-0.03em]">The Dot Screen</h1>
      <p class="m-0 max-w-[40rem] text-gtw14-mut text-[clamp(0.95rem,1.9vw,1.06rem)] text-pretty">One <code class="font-gtw14-mono text-[0.9em]">radial-gradient</code>, one blend mode, one contrast boost. Everything below is ink on paper as far as your eye is concerned.</p>
    </header>

    <article class="group grid gap-[clamp(1.2rem,3vw,2.2rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,20rem),1fr))] items-start">
      <div class="relative isolate overflow-hidden aspect-[7/5] bg-gtw14-ink border border-gtw14-line">
        <img src="https://picsum.photos/id/1005/1400/1000" alt="A portrait of a person looking away from the camera in strong daylight" loading="lazy" width="1400" height="1000" class="absolute inset-0 w-full h-full object-cover grayscale contrast-[1.6] brightness-[1.06]">
        <span aria-hidden="true" class="absolute -inset-[30%] pointer-events-none rotate-[15deg] mix-blend-screen opacity-[0.92] transition-opacity duration-300 group-hover:opacity-[0.7] motion-reduce:transition-none bg-[radial-gradient(circle_at_center,#ffffff_0_var(--gtw14-dot),transparent_calc(var(--gtw14-dot)+0.45px))] bg-[length:var(--gtw14-pitch)_var(--gtw14-pitch)]"></span>
        <span aria-hidden="true" class="absolute -inset-[30%] pointer-events-none rotate-[75deg] mix-blend-lighten opacity-[0.7] bg-[radial-gradient(circle_at_center,var(--color-gtw14-acc)_0_var(--gtw14-dot),transparent_calc(var(--gtw14-dot)+0.45px))] bg-[length:var(--gtw14-pitch)_var(--gtw14-pitch)]"></span>
      </div>
      <div class="grid gap-[0.65rem] min-w-0">
        <p class="m-0 font-gtw14-mono text-[0.7rem] font-medium leading-none tracking-[0.14em] uppercase text-gtw14-acc">Two inks · screens at 15° and 75°</p>
        <h2 class="m-0 font-gtw14-display text-[clamp(1.5rem,4vw,2.4rem)] font-normal leading-[1.08] tracking-[-0.02em] text-balance">Duotone, the way two-ink presses actually work</h2>
        <p class="m-0 max-w-[34rem] text-gtw14-mut text-[clamp(0.93rem,1.9vw,1.02rem)] text-pretty">A black screen at fifteen degrees, a red screen at seventy-five, and thirty degrees of separation so the two grids never beat against each other. The photograph underneath is pushed to contrast 1.6 and fully desaturated before either screen lands on it.</p>
        <dl class="flex flex-wrap gap-y-[0.4rem] gap-x-[1.6rem] mt-[0.3rem] mb-0 pt-[0.8rem] border-t border-gtw14-line">
          <div class="grid gap-[0.1rem]"><dt class="m-0 font-gtw14-mono text-[0.66rem] leading-none tracking-[0.12em] uppercase text-gtw14-mut">Pitch</dt><dd class="m-0 font-gtw14-mono text-[1rem] font-medium leading-none">6px</dd></div>
          <div class="grid gap-[0.1rem]"><dt class="m-0 font-gtw14-mono text-[0.66rem] leading-none tracking-[0.12em] uppercase text-gtw14-mut">Angles</dt><dd class="m-0 font-gtw14-mono text-[1rem] font-medium leading-none">15° / 75°</dd></div>
          <div class="grid gap-[0.1rem]"><dt class="m-0 font-gtw14-mono text-[0.66rem] leading-none tracking-[0.12em] uppercase text-gtw14-mut">Contrast</dt><dd class="m-0 font-gtw14-mono text-[1rem] font-medium leading-none">1.6</dd></div>
        </dl>
      </div>
    </article>

    <ul class="list-none m-0 p-0 grid gap-[clamp(1rem,2.5vw,1.6rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,15rem),1fr))]">
      <li class="group grid gap-2 min-w-0 [--gtw14-pitch:4px]">
        <div class="relative isolate overflow-hidden aspect-[9/11] bg-gtw14-ink border border-gtw14-line">
          <img src="https://picsum.photos/id/1074/900/1100" alt="A lion resting in dry grass" loading="lazy" width="900" height="1100" class="absolute inset-0 w-full h-full object-cover grayscale contrast-[1.6] brightness-[1.06]">
          <span aria-hidden="true" class="absolute -inset-[30%] pointer-events-none rotate-[15deg] mix-blend-screen opacity-[0.92] transition-opacity duration-300 group-hover:opacity-[0.7] motion-reduce:transition-none bg-[radial-gradient(circle_at_center,#ffffff_0_var(--gtw14-dot),transparent_calc(var(--gtw14-dot)+0.45px))] bg-[length:var(--gtw14-pitch)_var(--gtw14-pitch)]"></span>
        </div>
        <h3 class="mt-[0.2rem] mb-0 font-gtw14-display text-[1.15rem] font-normal leading-[1.15]">Fine screen · 4px</h3>
        <p class="m-0 text-gtw14-mut text-[0.87rem] text-pretty">Magazine pitch. Holds detail, reads as print rather than as pattern.</p>
      </li>
      <li class="group grid gap-2 min-w-0 [--gtw14-pitch:7px]">
        <div class="relative isolate overflow-hidden aspect-[9/11] bg-gtw14-ink border border-gtw14-line">
          <img src="https://picsum.photos/id/1080/900/1100" alt="A close-up of strawberries in a crate" loading="lazy" width="900" height="1100" class="absolute inset-0 w-full h-full object-cover grayscale contrast-[1.6] brightness-[1.06]">
          <span aria-hidden="true" class="absolute -inset-[30%] pointer-events-none rotate-[15deg] mix-blend-screen opacity-[0.92] transition-opacity duration-300 group-hover:opacity-[0.7] motion-reduce:transition-none bg-[radial-gradient(circle_at_center,#ffffff_0_var(--gtw14-dot),transparent_calc(var(--gtw14-dot)+0.45px))] bg-[length:var(--gtw14-pitch)_var(--gtw14-pitch)]"></span>
        </div>
        <h3 class="mt-[0.2rem] mb-0 font-gtw14-display text-[1.15rem] font-normal leading-[1.15]">Newsprint · 7px</h3>
        <p class="m-0 text-gtw14-mut text-[0.87rem] text-pretty">The default. Visibly a screen at reading distance, still legible as an image.</p>
      </li>
      <li class="group grid gap-2 min-w-0 [--gtw14-pitch:11px]">
        <div class="relative isolate overflow-hidden aspect-[9/11] bg-gtw14-ink border border-gtw14-line">
          <img src="https://picsum.photos/id/1084/900/1100" alt="A mountain lake surrounded by pines" loading="lazy" width="900" height="1100" class="absolute inset-0 w-full h-full object-cover grayscale contrast-[1.6] brightness-[1.06]">
          <span aria-hidden="true" class="absolute -inset-[30%] pointer-events-none rotate-[15deg] mix-blend-screen opacity-[0.92] transition-opacity duration-300 group-hover:opacity-[0.7] motion-reduce:transition-none bg-[radial-gradient(circle_at_center,#ffffff_0_var(--gtw14-dot),transparent_calc(var(--gtw14-dot)+0.45px))] bg-[length:var(--gtw14-pitch)_var(--gtw14-pitch)]"></span>
        </div>
        <h3 class="mt-[0.2rem] mb-0 font-gtw14-display text-[1.15rem] font-normal leading-[1.15]">Pop · 11px</h3>
        <p class="m-0 text-gtw14-mut text-[0.87rem] text-pretty">Coarse enough to become the subject. Use once per page, never behind type.</p>
      </li>
    </ul>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw14-bg: #f2efe8;
  --color-gtw14-bg: oklch(0.95 0.012 85);
  --color-gtw14-surf: #fbfaf6;
  --color-gtw14-surf: oklch(0.98 0.006 85);
  --color-gtw14-ink: #14110e;
  --color-gtw14-ink: oklch(0.2 0.008 70);
  --color-gtw14-mut: #5d574d;
  --color-gtw14-mut: oklch(0.45 0.015 80);
  --color-gtw14-line: #d8d2c5;
  --color-gtw14-line: oklch(0.87 0.018 85);
  --color-gtw14-acc: #d2231f;
  --color-gtw14-acc: oklch(0.53 0.21 28);
  --font-gtw14-display: 'Instrument Serif', 'Playfair Display', Georgia, serif;
  --font-gtw14-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}

.gtw-14 {
  width: 100%;
  min-height: 100svh;
  --gtw14-pitch: 6px;
  --gtw14-dot: 1.15px;
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
}
/* Screen pitch is in CSS pixels, so a dense display needs a tighter grid or the halftone
   reads twice as fine as intended. Pitch and dot radius must move together. */

@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 2dppx) {
  .gtw-14 {
    --gtw14-pitch: 5px;
    --gtw14-dot: 0.95px;
  }
}

.gtw-14:has(.gtw-14-theme:checked) {
  --color-gtw14-bg: #100e0c;
  --color-gtw14-bg: oklch(0.17 0.006 70);
  --color-gtw14-surf: #191614;
  --color-gtw14-surf: oklch(0.22 0.008 70);
  --color-gtw14-ink: #f4f1ea;
  --color-gtw14-ink: oklch(0.96 0.008 85);
  --color-gtw14-mut: #a29a8c;
  --color-gtw14-mut: oklch(0.7 0.015 80);
  --color-gtw14-line: #2e2823;
  --color-gtw14-line: oklch(0.3 0.012 75);
  --color-gtw14-acc: #ff6b5e;
  --color-gtw14-acc: oklch(0.74 0.17 30);
}

@media (prefers-color-scheme: dark) {
  .gtw-14 {
    --color-gtw14-bg: #100e0c;
    --color-gtw14-bg: oklch(0.17 0.006 70);
    --color-gtw14-surf: #191614;
    --color-gtw14-surf: oklch(0.22 0.008 70);
    --color-gtw14-ink: #f4f1ea;
    --color-gtw14-ink: oklch(0.96 0.008 85);
    --color-gtw14-mut: #a29a8c;
    --color-gtw14-mut: oklch(0.7 0.015 80);
    --color-gtw14-line: #2e2823;
    --color-gtw14-line: oklch(0.3 0.012 75);
    --color-gtw14-acc: #ff6b5e;
    --color-gtw14-acc: oklch(0.74 0.17 30);
  }

  .gtw-14:has(.gtw-14-theme:checked) {
    --color-gtw14-bg: #f2efe8;
    --color-gtw14-bg: oklch(0.95 0.012 85);
    --color-gtw14-surf: #fbfaf6;
    --color-gtw14-surf: oklch(0.98 0.006 85);
    --color-gtw14-ink: #14110e;
    --color-gtw14-ink: oklch(0.2 0.008 70);
    --color-gtw14-mut: #5d574d;
    --color-gtw14-mut: oklch(0.45 0.015 80);
    --color-gtw14-line: #d8d2c5;
    --color-gtw14-line: oklch(0.87 0.018 85);
    --color-gtw14-acc: #d2231f;
    --color-gtw14-acc: oklch(0.53 0.21 28);
  }
}

@media (prefers-color-scheme: light) {
  .gtw-14:has(.gtw-14-theme:checked) {
    --color-gtw14-bg: #100e0c;
    --color-gtw14-bg: oklch(0.17 0.006 70);
    --color-gtw14-surf: #191614;
    --color-gtw14-surf: oklch(0.22 0.008 70);
    --color-gtw14-ink: #f4f1ea;
    --color-gtw14-ink: oklch(0.96 0.008 85);
    --color-gtw14-mut: #a29a8c;
    --color-gtw14-mut: oklch(0.7 0.015 80);
    --color-gtw14-line: #2e2823;
    --color-gtw14-line: oklch(0.3 0.012 75);
    --color-gtw14-acc: #ff6b5e;
    --color-gtw14-acc: oklch(0.74 0.17 30);
  }
}
```
