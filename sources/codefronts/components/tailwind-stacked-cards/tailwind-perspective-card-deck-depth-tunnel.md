---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-perspective-card-deck-depth-tunnel/"
title: "Tailwind Perspective Card Deck Depth Tunnel"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "Four panels receding into the screen on negative Z, tilting as a group on hover while the front card pushes toward you."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Perspective Card Deck Depth Tunnel
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-perspective-card-deck-depth-tunnel/

Four panels receding into the screen on negative Z, tilting as a group on hover while the front card pushes toward you. Four :nth-child rules become one index expression &mdash; depth, vertical offset and opacity all fall out of --i &mdash; and the opacity ramp doubles as the contrast fix, because a panel that recedes should also read as background.
## HTML
```html
<section class="stk-33 grid w-full min-h-svh place-items-center px-5 py-15 font-stk33-sans bg-stk33-bg [background-image:radial-gradient(circle_at_50%_50%,var(--color-stk33-glow),transparent_70%)]" aria-label="Sector status deck">
  <div class="group h-95 w-75 [perspective:900px]">
    <div class="relative size-full [transform-style:preserve-3d] transition-transform duration-800 ease-out group-hover:[transform:rotateX(18deg)_rotateY(-12deg)] motion-reduce:transition-none motion-reduce:rotate-none!">
      <article class="absolute inset-0 flex flex-col justify-end rounded-[20px] border border-stk33-neon/35 bg-linear-[155deg,var(--color-stk33-c1),var(--color-stk33-c2)] p-6.5 text-stk33-ink backdrop-blur-[2px] shadow-[0_0_40px_var(--color-stk33-halo)] opacity-[calc(1-var(--i)*0.2)] [transform:translateZ(calc(var(--i)*-80px))_translateY(calc(var(--i)*-26px))] transition-[transform,opacity] duration-800 ease-stk33 group-hover:[transform:translateZ(60px)] motion-reduce:transition-none" style="--i:0">
        <h3 class="m-0 font-stk33-display text-[1.3rem] tracking-[0.08em]">SECTOR 01</h3>
        <p class="m-0 text-[0.95rem] tracking-[0.05em] text-stk33-ink/75">Active node // online</p>
      </article>
      <article class="absolute inset-0 flex flex-col justify-end rounded-[20px] border border-stk33-neon/35 bg-linear-[155deg,var(--color-stk33-c1),var(--color-stk33-c2)] p-6.5 text-stk33-ink backdrop-blur-[2px] shadow-[0_0_40px_var(--color-stk33-halo)] opacity-[calc(1-var(--i)*0.2)] [transform:translateZ(calc(var(--i)*-80px))_translateY(calc(var(--i)*-26px))] transition-[transform,opacity] duration-800 ease-stk33 motion-reduce:transition-none" style="--i:1" aria-hidden="true">
        <h3 class="m-0 font-stk33-display text-[1.3rem] tracking-[0.08em]">SECTOR 02</h3>
        <p class="m-0 text-[0.95rem] tracking-[0.05em] text-stk33-ink/75">Buffered // standby</p>
      </article>
      <article class="absolute inset-0 flex flex-col justify-end rounded-[20px] border border-stk33-neon/35 bg-linear-[155deg,var(--color-stk33-c1),var(--color-stk33-c2)] p-6.5 text-stk33-ink backdrop-blur-[2px] shadow-[0_0_40px_var(--color-stk33-halo)] opacity-[calc(1-var(--i)*0.2)] [transform:translateZ(calc(var(--i)*-80px))_translateY(calc(var(--i)*-26px))] transition-[transform,opacity] duration-800 ease-stk33 motion-reduce:transition-none" style="--i:2" aria-hidden="true">
        <h3 class="m-0 font-stk33-display text-[1.3rem] tracking-[0.08em]">SECTOR 03</h3>
        <p class="m-0 text-[0.95rem] tracking-[0.05em] text-stk33-ink/75">Cached // idle</p>
      </article>
      <article class="absolute inset-0 flex flex-col justify-end rounded-[20px] border border-stk33-neon/35 bg-linear-[155deg,var(--color-stk33-c1),var(--color-stk33-c2)] p-6.5 text-stk33-ink backdrop-blur-[2px] shadow-[0_0_40px_var(--color-stk33-halo)] opacity-[calc(1-var(--i)*0.2)] [transform:translateZ(calc(var(--i)*-80px))_translateY(calc(var(--i)*-26px))] transition-[transform,opacity] duration-800 ease-stk33 motion-reduce:transition-none" style="--i:3" aria-hidden="true">
        <h3 class="m-0 font-stk33-display text-[1.3rem] tracking-[0.08em]">SECTOR 04</h3>
        <p class="m-0 text-[0.95rem] tracking-[0.05em] text-stk33-ink/75">Archived // sleep</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk33-bg: #05060a;
  --color-stk33-bg: oklch(0.08 0.012 275);
  --color-stk33-glow: #10131f;
  --color-stk33-glow: oklch(0.19 0.022 275);
  --color-stk33-c1: #28345a;
  --color-stk33-c1: oklch(0.32 0.055 265);
  --color-stk33-c2: #121628;
  --color-stk33-c2: oklch(0.20 0.030 270);
  --color-stk33-ink: #cfe0ff;
  --color-stk33-ink: oklch(0.90 0.040 260);
  --color-stk33-neon: #78aaff;
  --color-stk33-neon: oklch(0.74 0.130 260);
  --color-stk33-halo: rgba(70, 120, 255, 0.18);
  --font-stk33-sans: 'Rajdhani', system-ui, sans-serif;
  --font-stk33-display: 'Orbitron', system-ui, sans-serif;
  --ease-stk33: cubic-bezier(0.2, 0.8, 0.2, 1);
}
```
