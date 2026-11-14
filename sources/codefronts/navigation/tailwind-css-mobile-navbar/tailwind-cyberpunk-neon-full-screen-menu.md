---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-cyberpunk-neon-full-screen-menu/"
title: "Tailwind Cyberpunk Neon Full-Screen Menu"
section: "navigation"
category: "tailwind-css-mobile-navbar"
category_name: "Tailwind CSS Mobile Navbars & Menus"
description: "A HUD-style overlay that wipes in from the right with a clip-path polygon, over scanlines and a cyan grid, then staggers five neon labels in from the left."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Cyberpunk Neon Full-Screen Menu
Source: https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-cyberpunk-neon-full-screen-menu/

A HUD-style overlay that wipes in from the right with a clip-path polygon, over scanlines and a cyan grid, then staggers five neon labels in from the left. Every glow is an arbitrary [text-shadow:…] property tuned per colour; the scanlines are a single after: gradient on the phone. Zero JavaScript.
## HTML
```html
<section class="tmn-11 w-full min-h-svh grid place-items-center bg-tmn11-stage px-4 py-6 font-tmn11-mono antialiased" aria-label="Tailwind cyberpunk neon menu demo">
  <div class="group relative h-[min(667px,calc(100svh-3rem))] w-full max-w-[375px] overflow-hidden rounded-[2.25rem] bg-tmn11-bg text-tmn11-ink shadow-[0_0_60px_oklch(0.88_0.15_200/0.15),0_40px_100px_-30px_oklch(0_0_0/0.9)] ring-1 ring-tmn11-cyan/20 after:pointer-events-none after:absolute after:inset-0 after:z-40 after:bg-[repeating-linear-gradient(0deg,transparent_0_2px,oklch(0_0_0/0.18)_2px_4px)] after:content-['']">
    <div aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(oklch(0.88_0.15_200/0.05)_1px,transparent_1px),linear-gradient(90deg,oklch(0.88_0.15_200/0.05)_1px,transparent_1px)] bg-size-[40px_40px]"></div>
    <input type="checkbox" id="tmn-11-toggle" class="peer sr-only" aria-label="Toggle system menu">

    <header class="absolute inset-x-0 top-0 z-10 flex h-14 items-center justify-between border-b border-tmn11-cyan/15 px-5">
      <p class="font-tmn11-display text-base font-bold tracking-[0.3em] text-tmn11-cyan [text-shadow:0_0_10px_var(--color-tmn11-cyan)] animate-tmn11-flicker motion-reduce:animate-none">NEXUS</p>
      <label for="tmn-11-toggle" class="grid size-11 cursor-pointer place-content-center gap-1.5 rounded-sm border border-tmn11-cyan/35 bg-tmn11-cyan/5 transition hover:border-tmn11-cyan hover:shadow-[inset_0_0_12px_oklch(0.88_0.15_200/0.35)] peer-focus-visible:ring-2 peer-focus-visible:ring-tmn11-cyan">
        <span class="block h-px w-5 bg-tmn11-cyan shadow-[0_0_6px_var(--color-tmn11-cyan)]"></span>
        <span class="block h-px w-5 bg-tmn11-cyan shadow-[0_0_6px_var(--color-tmn11-cyan)]"></span>
        <span class="block h-px w-3 bg-tmn11-cyan shadow-[0_0_6px_var(--color-tmn11-cyan)]"></span>
      </label>
    </header>

    <main class="absolute inset-x-0 top-14 bottom-0 z-[5] px-5 py-6">
      <p class="mb-1 text-[11px] tracking-[0.25em] text-tmn11-cyan uppercase [text-shadow:0_0_8px_oklch(0.88_0.15_200/0.5)]">// System status</p>
      <h1 class="mb-6 font-tmn11-display text-[30px] font-bold tracking-[-0.01em] uppercase">Nexus Core</h1>
      <article class="relative mb-3 rounded-sm border border-tmn11-cyan/30 bg-tmn11-cyan/[0.03] p-4 before:absolute before:top-0 before:left-4 before:h-0.5 before:w-8 before:bg-tmn11-cyan before:shadow-[0_0_8px_var(--color-tmn11-cyan)] before:content-['']"><h2 class="mb-1 text-[13px] font-bold tracking-[0.08em] uppercase">Active missions</h2><p class="text-xs leading-normal text-tmn11-mut">3 operations in progress &mdash; <span class="text-tmn11-pink">1 critical</span></p></article>
      <article class="relative mb-3 rounded-sm border border-tmn11-pink/30 bg-tmn11-pink/[0.03] p-4 before:absolute before:top-0 before:left-4 before:h-0.5 before:w-8 before:bg-tmn11-pink before:shadow-[0_0_8px_var(--color-tmn11-pink)] before:content-['']"><h2 class="mb-1 text-[13px] font-bold tracking-[0.08em] uppercase">Network uplink</h2><p class="text-xs leading-normal text-tmn11-mut">Encrypted tunnel established · ping 12ms</p></article>
      <article class="relative rounded-sm border border-tmn11-green/30 bg-tmn11-green/[0.03] p-4 before:absolute before:top-0 before:left-4 before:h-0.5 before:w-8 before:bg-tmn11-green before:shadow-[0_0_8px_var(--color-tmn11-green)] before:content-['']"><h2 class="mb-1 text-[13px] font-bold tracking-[0.08em] uppercase">Agent status</h2><p class="text-xs leading-normal text-tmn11-mut">Identity verified · clearance <span class="text-tmn11-green">ALPHA</span></p></article>
    </main>

    <nav aria-label="System" class="invisible absolute inset-0 z-20 flex flex-col justify-center bg-tmn11-bg/97 px-8 py-10 opacity-0 [clip-path:polygon(100%_0,100%_0,100%_100%,100%_100%)] transition-[opacity,clip-path,visibility] duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-has-checked:visible group-has-checked:opacity-100 group-has-checked:[clip-path:polygon(0_0,100%_0,100%_100%,0_100%)]">
      <div class="mb-10 flex items-center justify-between">
        <p class="text-[11px] tracking-[0.2em] text-tmn11-mut uppercase">Sys · <span class="text-tmn11-green">Online</span></p>
        <label for="tmn-11-toggle" class="grid size-11 cursor-pointer place-items-center rounded-sm border border-tmn11-cyan/35 text-tmn11-cyan [text-shadow:0_0_10px_var(--color-tmn11-cyan)] hover:border-tmn11-cyan"><span class="sr-only">Close menu</span><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg></label>
      </div>
      <ul>
        <li class="-translate-x-8 opacity-0 transition duration-400 group-has-checked:translate-x-0 group-has-checked:opacity-100 group-has-checked:delay-[150ms]"><a href="#" class="group/row flex min-h-15 items-center gap-4 border-b border-tmn11-cyan/10 transition-[padding] hover:pl-2 focus-visible:pl-2 focus-visible:outline-none"><span class="min-w-7 text-[11px] text-tmn11-mut">01</span><span class="font-tmn11-display text-[30px] font-bold uppercase text-tmn11-cyan [text-shadow:0_0_12px_oklch(0.88_0.15_200/0.55)]">Missions</span><span aria-hidden="true" class="ml-auto text-lg text-tmn11-mut transition group-hover/row:translate-x-1 group-hover/row:text-tmn11-cyan">→</span></a></li>
        <li class="-translate-x-8 opacity-0 transition duration-400 group-has-checked:translate-x-0 group-has-checked:opacity-100 group-has-checked:delay-[220ms]"><a href="#" class="group/row flex min-h-15 items-center gap-4 border-b border-tmn11-cyan/10 transition-[padding] hover:pl-2 focus-visible:pl-2 focus-visible:outline-none"><span class="min-w-7 text-[11px] text-tmn11-mut">02</span><span class="font-tmn11-display text-[30px] font-bold uppercase text-tmn11-pink [text-shadow:0_0_12px_oklch(0.65_0.28_350/0.55)]">Arsenal</span><span aria-hidden="true" class="ml-auto text-lg text-tmn11-mut transition group-hover/row:translate-x-1 group-hover/row:text-tmn11-pink">→</span></a></li>
        <li class="-translate-x-8 opacity-0 transition duration-400 group-has-checked:translate-x-0 group-has-checked:opacity-100 group-has-checked:delay-[290ms]"><a href="#" class="group/row flex min-h-15 items-center gap-4 border-b border-tmn11-cyan/10 transition-[padding] hover:pl-2 focus-visible:pl-2 focus-visible:outline-none"><span class="min-w-7 text-[11px] text-tmn11-mut">03</span><span class="font-tmn11-display text-[30px] font-bold uppercase text-tmn11-yellow [text-shadow:0_0_12px_oklch(0.92_0.19_103/0.5)]">Intel</span><span aria-hidden="true" class="ml-auto text-lg text-tmn11-mut transition group-hover/row:translate-x-1 group-hover/row:text-tmn11-yellow">→</span></a></li>
        <li class="-translate-x-8 opacity-0 transition duration-400 group-has-checked:translate-x-0 group-has-checked:opacity-100 group-has-checked:delay-[360ms]"><a href="#" class="group/row flex min-h-15 items-center gap-4 border-b border-tmn11-cyan/10 transition-[padding] hover:pl-2 focus-visible:pl-2 focus-visible:outline-none"><span class="min-w-7 text-[11px] text-tmn11-mut">04</span><span class="font-tmn11-display text-[30px] font-bold uppercase text-tmn11-green [text-shadow:0_0_12px_oklch(0.87_0.22_155/0.5)]">Network</span><span aria-hidden="true" class="ml-auto text-lg text-tmn11-mut transition group-hover/row:translate-x-1 group-hover/row:text-tmn11-green">→</span></a></li>
        <li class="-translate-x-8 opacity-0 transition duration-400 group-has-checked:translate-x-0 group-has-checked:opacity-100 group-has-checked:delay-[430ms]"><a href="#" class="group/row flex min-h-15 items-center gap-4 transition-[padding] hover:pl-2 focus-visible:pl-2 focus-visible:outline-none"><span class="min-w-7 text-[11px] text-tmn11-mut">05</span><span class="font-tmn11-display text-[30px] font-bold uppercase">Profile</span><span aria-hidden="true" class="ml-auto text-lg text-tmn11-mut transition group-hover/row:translate-x-1 group-hover/row:text-tmn11-ink">→</span></a></li>
      </ul>
      <p class="mt-10 text-[11px] tracking-[0.16em] text-tmn11-mut uppercase">Build 2.4.7 · <span class="text-tmn11-pink">Classified</span></p>
    </nav>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmn11-stage: #020008;
  --color-tmn11-stage: oklch(0.1 0.02 290);
  --color-tmn11-bg: #05010f;
  --color-tmn11-bg: oklch(0.12 0.03 295);
  --color-tmn11-ink: #e0e0ff;
  --color-tmn11-ink: oklch(0.91 0.04 285);
  --color-tmn11-mut: #8a8ab8;
  --color-tmn11-mut: oklch(0.65 0.06 285);
  --color-tmn11-cyan: #00f5ff;
  --color-tmn11-cyan: oklch(0.88 0.15 200);
  --color-tmn11-pink: #ff2fb0;
  --color-tmn11-pink: oklch(0.65 0.28 350);
  --color-tmn11-yellow: #ffe600;
  --color-tmn11-yellow: oklch(0.92 0.19 103);
  --color-tmn11-green: #00ff88;
  --color-tmn11-green: oklch(0.87 0.22 155);
  --font-tmn11-display: 'Chakra Petch', system-ui, sans-serif;
  --font-tmn11-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tmn11-flicker: tmn11-flicker 4s steps(1, end) infinite;

  @keyframes tmn11-flicker {
    0%,
        100% {
      opacity: 1;
    }

    92% {
      opacity: 1;
    }

    93% {
      opacity: 0.35;
    }

    94% {
      opacity: 1;
    }

    96% {
      opacity: 0.55;
    }

    97% {
      opacity: 1;
    }
  }
}
/* Icon base: utilities still win because this sits in the base layer. */

@layer base {
  .tmn-11 svg {
    fill: none;
    stroke: currentColor;
    stroke-width: 1.8;
    stroke-linecap: round;
    stroke-linejoin: round;
    flex: none;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is
   sized before the browser build compiles. */

.tmn-11 {
  width: 100%;
  min-height: 100svh;
}
```
