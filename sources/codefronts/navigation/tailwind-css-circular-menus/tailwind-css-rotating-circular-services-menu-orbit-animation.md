---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-rotating-circular-services-menu-orbit-animation/"
title: "Tailwind CSS Rotating Circular Services Menu (Orbit Animation)"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "An agency services ring that orbits a gold monogram on a slow 40-second loop &mdash; and stays perfectly legible, because each chip counter-rotates at the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Rotating Circular Services Menu (Orbit Animation)
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-rotating-circular-services-menu-orbit-animation/

An agency services ring that orbits a gold monogram on a slow 40-second loop &mdash; and stays perfectly legible, because each chip counter-rotates at the same rate. Hover or tab into the ring and it eases to a stop; the centre then swaps the monogram for the hovered service&rsquo;s one-line pitch, all with group-has-[[data-s='2']:is(:hover,:focus-visible)]/ring:. Zero JavaScript.
## HTML
```html
<section class="tcm-07 w-full min-h-svh grid place-items-center overflow-hidden bg-tcm07-bg bg-[radial-gradient(50%_45%_at_50%_48%,var(--color-tcm07-glow),transparent_72%)] px-5 py-14 font-tcm07-sans text-tcm07-ink antialiased" aria-label="Rotating circular services menu demo">
  <div class="grid w-full justify-items-center gap-10">
    <header class="grid justify-items-center gap-2 text-center">
      <p class="font-tcm07-mono text-[11px] tracking-[0.2em] text-tcm07-gold-ink uppercase">Studio Tellier · Since 2014</p>
      <h2 class="font-tcm07-serif text-[clamp(2rem,5vw,2.8rem)] leading-[1.05] font-normal tracking-[-0.01em]">Six crafts, <em class="text-tcm07-gold-ink">one orbit</em></h2>
    </header>
    <nav class="group/ring relative grid size-[min(22rem,88vw)] place-items-center [--n:6] [--r:min(9.5rem,37vw)]" aria-label="Services">
      <span aria-hidden="true" class="absolute inset-[calc(50%-var(--r))] rounded-full border border-dashed border-tcm07-gold/40"></span>
      <span aria-hidden="true" class="absolute inset-[calc(50%-var(--r)+1.75rem)] rounded-full border border-tcm07-gold/15"></span>
      <ul class="absolute inset-0 animate-tcm07-spin group-hover/ring:[animation-play-state:paused] group-focus-within/ring:[animation-play-state:paused] motion-reduce:animate-none">
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:0] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <a href="#tcm-07-0" data-s="0" class="tcm07-polar pointer-events-auto rounded-full bg-tcm07-chip px-4.5 py-2.5 text-[13.5px] font-semibold tracking-[0.01em] whitespace-nowrap text-tcm07-ink shadow-tcm07-chip ring-1 ring-tcm07-gold/35 backdrop-blur-md animate-tcm07-spin [animation-direction:reverse] transition-[background-color,color,box-shadow] duration-300 group-hover/ring:[animation-play-state:paused] group-focus-within/ring:[animation-play-state:paused] hover:bg-linear-to-br hover:from-tcm07-gold hover:to-tcm07-gold2 hover:text-tcm07-on focus-visible:bg-linear-to-br focus-visible:from-tcm07-gold focus-visible:to-tcm07-gold2 focus-visible:text-tcm07-on focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm07-ring motion-reduce:animate-none">Branding</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:1] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <a href="#tcm-07-1" data-s="1" class="tcm07-polar pointer-events-auto rounded-full bg-tcm07-chip px-4.5 py-2.5 text-[13.5px] font-semibold tracking-[0.01em] whitespace-nowrap text-tcm07-ink shadow-tcm07-chip ring-1 ring-tcm07-gold/35 backdrop-blur-md animate-tcm07-spin [animation-direction:reverse] transition-[background-color,color,box-shadow] duration-300 group-hover/ring:[animation-play-state:paused] group-focus-within/ring:[animation-play-state:paused] hover:bg-linear-to-br hover:from-tcm07-gold hover:to-tcm07-gold2 hover:text-tcm07-on focus-visible:bg-linear-to-br focus-visible:from-tcm07-gold focus-visible:to-tcm07-gold2 focus-visible:text-tcm07-on focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm07-ring motion-reduce:animate-none">Web design</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:2] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <a href="#tcm-07-2" data-s="2" class="tcm07-polar pointer-events-auto rounded-full bg-tcm07-chip px-4.5 py-2.5 text-[13.5px] font-semibold tracking-[0.01em] whitespace-nowrap text-tcm07-ink shadow-tcm07-chip ring-1 ring-tcm07-gold/35 backdrop-blur-md animate-tcm07-spin [animation-direction:reverse] transition-[background-color,color,box-shadow] duration-300 group-hover/ring:[animation-play-state:paused] group-focus-within/ring:[animation-play-state:paused] hover:bg-linear-to-br hover:from-tcm07-gold hover:to-tcm07-gold2 hover:text-tcm07-on focus-visible:bg-linear-to-br focus-visible:from-tcm07-gold focus-visible:to-tcm07-gold2 focus-visible:text-tcm07-on focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm07-ring motion-reduce:animate-none">Motion</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:3] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <a href="#tcm-07-3" data-s="3" class="tcm07-polar pointer-events-auto rounded-full bg-tcm07-chip px-4.5 py-2.5 text-[13.5px] font-semibold tracking-[0.01em] whitespace-nowrap text-tcm07-ink shadow-tcm07-chip ring-1 ring-tcm07-gold/35 backdrop-blur-md animate-tcm07-spin [animation-direction:reverse] transition-[background-color,color,box-shadow] duration-300 group-hover/ring:[animation-play-state:paused] group-focus-within/ring:[animation-play-state:paused] hover:bg-linear-to-br hover:from-tcm07-gold hover:to-tcm07-gold2 hover:text-tcm07-on focus-visible:bg-linear-to-br focus-visible:from-tcm07-gold focus-visible:to-tcm07-gold2 focus-visible:text-tcm07-on focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm07-ring motion-reduce:animate-none">Strategy</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:4] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <a href="#tcm-07-4" data-s="4" class="tcm07-polar pointer-events-auto rounded-full bg-tcm07-chip px-4.5 py-2.5 text-[13.5px] font-semibold tracking-[0.01em] whitespace-nowrap text-tcm07-ink shadow-tcm07-chip ring-1 ring-tcm07-gold/35 backdrop-blur-md animate-tcm07-spin [animation-direction:reverse] transition-[background-color,color,box-shadow] duration-300 group-hover/ring:[animation-play-state:paused] group-focus-within/ring:[animation-play-state:paused] hover:bg-linear-to-br hover:from-tcm07-gold hover:to-tcm07-gold2 hover:text-tcm07-on focus-visible:bg-linear-to-br focus-visible:from-tcm07-gold focus-visible:to-tcm07-gold2 focus-visible:text-tcm07-on focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm07-ring motion-reduce:animate-none">Content</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:5] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <a href="#tcm-07-5" data-s="5" class="tcm07-polar pointer-events-auto rounded-full bg-tcm07-chip px-4.5 py-2.5 text-[13.5px] font-semibold tracking-[0.01em] whitespace-nowrap text-tcm07-ink shadow-tcm07-chip ring-1 ring-tcm07-gold/35 backdrop-blur-md animate-tcm07-spin [animation-direction:reverse] transition-[background-color,color,box-shadow] duration-300 group-hover/ring:[animation-play-state:paused] group-focus-within/ring:[animation-play-state:paused] hover:bg-linear-to-br hover:from-tcm07-gold hover:to-tcm07-gold2 hover:text-tcm07-on focus-visible:bg-linear-to-br focus-visible:from-tcm07-gold focus-visible:to-tcm07-gold2 focus-visible:text-tcm07-on focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm07-ring motion-reduce:animate-none">SEO</a>
        </li>
      </ul>
      <div class="relative grid size-[min(10rem,40vw)] place-items-center rounded-full bg-linear-to-br from-tcm07-core to-tcm07-core2 text-center shadow-tcm07-core ring-1 ring-tcm07-gold/30">
        <div class="grid place-items-center">
          <span class="col-start-1 row-start-1 grid justify-items-center gap-0.5 group-has-[[data-s]:is(:hover,:focus-visible)]/ring:hidden"><b class="bg-linear-to-br from-tcm07-gold to-tcm07-gold2 bg-clip-text font-tcm07-serif text-[2.6rem] leading-none font-normal text-transparent">ST</b><span class="text-[10.5px] tracking-[0.32em] text-tcm07-mut uppercase">studio</span></span>
          <span class="col-start-1 row-start-1 hidden group-has-[[data-s='0']:is(:hover,:focus-visible)]/ring:grid justify-items-center gap-1"><b class="font-tcm07-serif text-[1.5rem] leading-none font-normal italic text-tcm07-gold-ink">Branding</b><span class="max-w-[9rem] text-[12px] leading-snug text-tcm07-mut">Identity systems that scale</span></span>
          <span class="col-start-1 row-start-1 hidden group-has-[[data-s='1']:is(:hover,:focus-visible)]/ring:grid justify-items-center gap-1"><b class="font-tcm07-serif text-[1.5rem] leading-none font-normal italic text-tcm07-gold-ink">Web design</b><span class="max-w-[9rem] text-[12px] leading-snug text-tcm07-mut">Sites people remember</span></span>
          <span class="col-start-1 row-start-1 hidden group-has-[[data-s='2']:is(:hover,:focus-visible)]/ring:grid justify-items-center gap-1"><b class="font-tcm07-serif text-[1.5rem] leading-none font-normal italic text-tcm07-gold-ink">Motion</b><span class="max-w-[9rem] text-[12px] leading-snug text-tcm07-mut">Interfaces with rhythm</span></span>
          <span class="col-start-1 row-start-1 hidden group-has-[[data-s='3']:is(:hover,:focus-visible)]/ring:grid justify-items-center gap-1"><b class="font-tcm07-serif text-[1.5rem] leading-none font-normal italic text-tcm07-gold-ink">Strategy</b><span class="max-w-[9rem] text-[12px] leading-snug text-tcm07-mut">Positioning and naming</span></span>
          <span class="col-start-1 row-start-1 hidden group-has-[[data-s='4']:is(:hover,:focus-visible)]/ring:grid justify-items-center gap-1"><b class="font-tcm07-serif text-[1.5rem] leading-none font-normal italic text-tcm07-gold-ink">Content</b><span class="max-w-[9rem] text-[12px] leading-snug text-tcm07-mut">Words that convert</span></span>
          <span class="col-start-1 row-start-1 hidden group-has-[[data-s='5']:is(:hover,:focus-visible)]/ring:grid justify-items-center gap-1"><b class="font-tcm07-serif text-[1.5rem] leading-none font-normal italic text-tcm07-gold-ink">SEO</b><span class="max-w-[9rem] text-[12px] leading-snug text-tcm07-mut">Search you can measure</span></span>
        </div>
      </div>
    </nav>
    <p class="text-[13px] text-tcm07-mut">Hover or tab into the ring to pause it</p>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm07-card px-3.5 py-2 text-center font-tcm07-mono text-[11.5px] text-tcm07-mut ring-1 ring-tcm07-line ">animate-tcm07-spin · [animation-direction:reverse] · group-has-[…:hover]/ring:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm07-bg: #faf6ee;
  --color-tcm07-bg: oklch(0.974 0.011 84.6);
  --color-tcm07-glow: #f3e3bfb3;
  --color-tcm07-glow: oklch(0.92 0.05 86.9 / 0.7);
  --color-tcm07-chip: #fffdf8e6;
  --color-tcm07-chip: oklch(0.994 0.007 88.6 / 0.9);
  --color-tcm07-core: #fffaf0;
  --color-tcm07-core: oklch(0.986 0.014 84.6);
  --color-tcm07-core2: #f6ead3;
  --color-tcm07-core2: oklch(0.94 0.033 83.7);
  --color-tcm07-ink: #2a2116;
  --color-tcm07-ink: oklch(0.255 0.024 72);
  --color-tcm07-mut: #6f6152;
  --color-tcm07-mut: oklch(0.502 0.029 69);
  --color-tcm07-gold: #b8862e;
  --color-tcm07-gold: oklch(0.654 0.118 77.6);
  --color-tcm07-gold2: #d6a84a;
  --color-tcm07-gold2: oklch(0.756 0.123 82.7);
  --color-tcm07-gold-ink: #8a5f12;
  --color-tcm07-gold-ink: oklch(0.519 0.102 75.8);
  --color-tcm07-on: #2a1d08;
  --color-tcm07-on: oklch(0.242 0.039 77.1);
  --color-tcm07-ring: #8a5f12;
  --color-tcm07-ring: oklch(0.519 0.102 75.8);
  --color-tcm07-card: #fffdf8;
  --color-tcm07-card: oklch(0.994 0.007 88.6);
  --color-tcm07-line: #eadfca;
  --color-tcm07-line: oklch(0.907 0.03 83.6);
  --font-tcm07-sans: 'Manrope', system-ui, sans-serif;
  --font-tcm07-serif: 'Instrument Serif', Georgia, serif;
  --font-tcm07-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --shadow-tcm07-chip: 0 8px 20px -12px oklch(0.45 0.08 75 / 0.45), inset 0 1px 0 oklch(1 0 0 / 0.5);
  --shadow-tcm07-core: 0 0 90px -20px oklch(0.75 0.12 80 / 0.6), inset 0 1px 0 oklch(1 0 0 / 0.4);
  --animate-tcm07-spin: tcm07-spin 40s linear infinite;

  @keyframes tcm07-spin {
    to {
      rotate: 360deg;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-07 {
  width: 100%;
  min-height: 100svh;
}
/* The radial formula, as a real utility: position = (cos a · r, sin a · r). Items set --a and --r. */

@utility tcm07-polar {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}
/* Dark theme: champagne night: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-07:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm07-bg: #141009;
    --color-tcm07-bg: oklch(0.176 0.015 81.4);
    --color-tcm07-glow: #5c451a59;
    --color-tcm07-glow: oklch(0.406 0.067 80.4 / 0.35);
    --color-tcm07-chip: #ffffff0f;
    --color-tcm07-chip: oklch(1 0 0 / 0.06);
    --color-tcm07-core: #2a2114;
    --color-tcm07-core: oklch(0.254 0.026 76.3);
    --color-tcm07-core2: #19130b;
    --color-tcm07-core2: oklch(0.192 0.018 74.4);
    --color-tcm07-ink: #f6efe2;
    --color-tcm07-ink: oklch(0.954 0.019 83.1);
    --color-tcm07-mut: #bfae94;
    --color-tcm07-mut: oklch(0.758 0.041 78.5);
    --color-tcm07-gold: #d6a84a;
    --color-tcm07-gold: oklch(0.756 0.123 82.7);
    --color-tcm07-gold2: #f2cf7f;
    --color-tcm07-gold2: oklch(0.867 0.107 86.6);
    --color-tcm07-gold-ink: #f0c56a;
    --color-tcm07-gold-ink: oklch(0.843 0.12 84.4);
    --color-tcm07-on: #1d1405;
    --color-tcm07-on: oklch(0.198 0.031 79.8);
    --color-tcm07-ring: #f0c56a;
    --color-tcm07-ring: oklch(0.843 0.12 84.4);
    --color-tcm07-card: #1d170e;
    --color-tcm07-card: oklch(0.209 0.019 77.5);
    --color-tcm07-line: #3a2f1e;
    --color-tcm07-line: oklch(0.312 0.032 78);
  }
}

.tcm-07[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm07-bg: #141009;
  --color-tcm07-bg: oklch(0.176 0.015 81.4);
  --color-tcm07-glow: #5c451a59;
  --color-tcm07-glow: oklch(0.406 0.067 80.4 / 0.35);
  --color-tcm07-chip: #ffffff0f;
  --color-tcm07-chip: oklch(1 0 0 / 0.06);
  --color-tcm07-core: #2a2114;
  --color-tcm07-core: oklch(0.254 0.026 76.3);
  --color-tcm07-core2: #19130b;
  --color-tcm07-core2: oklch(0.192 0.018 74.4);
  --color-tcm07-ink: #f6efe2;
  --color-tcm07-ink: oklch(0.954 0.019 83.1);
  --color-tcm07-mut: #bfae94;
  --color-tcm07-mut: oklch(0.758 0.041 78.5);
  --color-tcm07-gold: #d6a84a;
  --color-tcm07-gold: oklch(0.756 0.123 82.7);
  --color-tcm07-gold2: #f2cf7f;
  --color-tcm07-gold2: oklch(0.867 0.107 86.6);
  --color-tcm07-gold-ink: #f0c56a;
  --color-tcm07-gold-ink: oklch(0.843 0.12 84.4);
  --color-tcm07-on: #1d1405;
  --color-tcm07-on: oklch(0.198 0.031 79.8);
  --color-tcm07-ring: #f0c56a;
  --color-tcm07-ring: oklch(0.843 0.12 84.4);
  --color-tcm07-card: #1d170e;
  --color-tcm07-card: oklch(0.209 0.019 77.5);
  --color-tcm07-line: #3a2f1e;
  --color-tcm07-line: oklch(0.312 0.032 78);
}
```
