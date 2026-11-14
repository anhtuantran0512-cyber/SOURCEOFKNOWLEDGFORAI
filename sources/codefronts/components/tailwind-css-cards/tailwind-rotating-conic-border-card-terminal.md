---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-rotating-conic-border-card-terminal/"
title: "Tailwind Rotating Conic-Border Card with Terminal Panel"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "A dev-tool card wrapped in a laser edge that rotates: a registered --angle custom property drives a conic gradient around a 1.5px rim, over a terminal panel…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Rotating Conic-Border Card with Terminal Panel
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-rotating-conic-border-card-terminal/

A dev-tool card wrapped in a laser edge that rotates: a registered --angle custom property drives a conic gradient around a 1.5px rim, over a terminal panel with a spinner, a tick and a blinking caret. The port's win is honest about its limit &mdash; @property and @keyframes cannot be utilities, so they stay CSS and everything else moves.
## HTML
```html
<section class="twc-18 relative w-full min-h-svh flex items-center justify-center overflow-hidden px-5 py-9 bg-twc18-bg font-twc18-sans">

  <div aria-hidden="true" class="absolute inset-0 z-0 overflow-hidden pointer-events-none">
    <div class="absolute inset-0 [background-image:radial-gradient(1px_1px_at_15%_25%,oklch(1_0_0/0.5)_50%,transparent),radial-gradient(1px_1px_at_78%_40%,oklch(1_0_0/0.6)_50%,transparent),radial-gradient(1px_1px_at_42%_78%,oklch(1_0_0/0.4)_50%,transparent),radial-gradient(1.5px_1.5px_at_25%_60%,oklch(1_0_0/0.4)_50%,transparent),radial-gradient(1px_1px_at_62%_20%,oklch(1_0_0/0.5)_50%,transparent),radial-gradient(1px_1px_at_5%_90%,oklch(1_0_0/0.3)_50%,transparent),radial-gradient(1px_1px_at_95%_55%,oklch(1_0_0/0.4)_50%,transparent)]"></div>
    <div class="absolute top-1/2 left-1/2 size-200 -translate-x-1/2 -translate-y-1/2 blur-[60px] [background:radial-gradient(circle_at_30%_30%,oklch(0.65_0.28_350/0.18)_0%,transparent_45%),radial-gradient(circle_at_70%_70%,oklch(0.8_0.13_200/0.16)_0%,transparent_45%)]"></div>
  </div>

  <article class="twc18-rim group/card relative z-1 isolate w-full max-w-[400px] overflow-hidden rounded-2xl p-[1.5px] animate-twc18-arc motion-reduce:animate-none shadow-[0_30px_60px_-20px_oklch(0_0_0/0.8),0_20px_40px_-20px_oklch(0.65_0.28_350/0.25)] transition-[transform,box-shadow] duration-500 ease-[cubic-bezier(0.34,1.2,0.64,1)] hover:-translate-y-[3px] hover:shadow-[0_40px_80px_-20px_oklch(0_0_0/0.9),0_28px_50px_-20px_oklch(0.65_0.28_350/0.35)] motion-reduce:transition-none motion-reduce:hover:translate-y-0 before:absolute before:inset-[1.5px] before:z-0 before:rounded-[14.5px] before:content-[''] before:[background:linear-gradient(180deg,oklch(1_0_0/0.03)_0%,transparent_30%),linear-gradient(160deg,#0d0d16_0%,#12121e_100%)] before:shadow-[inset_0_1px_0_oklch(1_0_0/0.08)]">

    <div aria-hidden="true" class="absolute inset-[1.5px] z-3 overflow-hidden rounded-[14.5px] pointer-events-none opacity-0 transition-opacity duration-400 group-hover/card:opacity-100 motion-reduce:transition-none">
      <span class="absolute bottom-0 left-[20%] size-[3px] rounded-full bg-twc18-hot shadow-[0_0_8px_currentColor] text-twc18-hot animate-twc18-rise motion-reduce:animate-none"></span>
      <span class="absolute bottom-0 left-[35%] size-[3px] rounded-full bg-twc18-cyan shadow-[0_0_8px_currentColor] text-twc18-cyan animate-twc18-rise [animation-delay:0.6s] motion-reduce:animate-none"></span>
      <span class="absolute bottom-0 left-[55%] size-[3px] rounded-full bg-twc18-hot shadow-[0_0_8px_currentColor] text-twc18-hot animate-twc18-rise [animation-delay:1.2s] motion-reduce:animate-none"></span>
      <span class="absolute bottom-0 left-[72%] size-[3px] rounded-full bg-twc18-lime shadow-[0_0_8px_currentColor] text-twc18-lime animate-twc18-rise [animation-delay:1.8s] motion-reduce:animate-none"></span>
      <span class="absolute bottom-0 left-[88%] size-[3px] rounded-full bg-twc18-cyan shadow-[0_0_8px_currentColor] text-twc18-cyan animate-twc18-rise [animation-delay:2.4s] motion-reduce:animate-none"></span>
    </div>

    <div class="relative z-2 px-4.5 pt-4 pb-5 text-twc18-ink">

      <header class="flex items-center justify-between gap-2 pb-3 mb-3.5 border-b border-white/6">
        <div class="flex items-center gap-2">
          <span aria-hidden="true" class="size-4 rounded-full [background:radial-gradient(circle_at_30%_30%,#ff6bb1_0%,#ff2d92_40%,#7a1148_80%)] shadow-[0_0_10px_oklch(0.65_0.28_350/0.5),inset_0_1px_0_oklch(1_0_0/0.3)]"></span>
          <span class="font-twc18-mono text-xs font-bold tracking-[-0.005em] text-white/85">nova/generate</span>
          <span class="inline-flex items-center gap-1 px-1.5 py-0.5 rounded font-twc18-mono text-[10px] font-bold text-twc18-lime/90 bg-twc18-lime/8 border border-twc18-lime/22">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9v3a3 3 0 0 1-3 3H9"/></svg>
            main
          </span>
        </div>
        <div aria-hidden="true" class="flex gap-1.5">
          <span class="size-[9px] rounded-full bg-[#ff5f57] shadow-[inset_0_0_0_1px_oklch(0_0_0/0.25)]"></span>
          <span class="size-[9px] rounded-full bg-[#febc2e] shadow-[inset_0_0_0_1px_oklch(0_0_0/0.25)]"></span>
          <span class="size-[9px] rounded-full bg-[#28c840] shadow-[inset_0_0_0_1px_oklch(0_0_0/0.25)]"></span>
        </div>
      </header>

      <div role="img" aria-label="Terminal transcript: running nova generate with style van gogh; the nova-v4-turbo diffusion model loads and 12 styles are ready in 2.4 seconds." class="flex flex-col gap-1.5 p-3 mb-3.5 rounded-[10px] bg-black/35 border border-white/6 font-twc18-mono text-[11.5px]/[1.5]">
        <div class="flex items-center gap-1.5">
          <span class="font-extrabold text-twc18-hot">$</span>
          <span class="tracking-[-0.005em] text-white/92">nova generate <span class="text-twc18-cyan">--style</span> <span class="text-twc18-lime">"van gogh"</span></span>
        </div>
        <div class="flex items-center gap-1.5 pl-0.5 text-white/55">
          <span aria-hidden="true" class="inline-block size-[9px] rounded-full border-[1.5px] border-white/20 border-t-twc18-cyan animate-twc18-spin motion-reduce:animate-none"></span>
          <span class="tracking-[-0.005em]">Loading diffusion model <span class="text-twc18-cyan">nova-v4-turbo</span></span>
        </div>
        <div class="flex items-center gap-1.5 pl-0.5">
          <span aria-hidden="true" class="inline-flex items-center justify-center size-3 text-twc18-lime">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
          </span>
          <span class="tracking-[-0.005em] text-white/85">12 styles ready in <span class="font-bold text-twc18-hot">2.4s</span></span>
        </div>
        <div class="flex items-center gap-1.5">
          <span class="font-extrabold text-twc18-hot">$</span>
          <span aria-hidden="true" class="inline-block w-[7px] h-[13px] bg-white/85 animate-twc18-caret motion-reduce:animate-none motion-reduce:bg-white/50"></span>
        </div>
      </div>

      <div class="flex flex-wrap items-center gap-1.5 mb-3">
        <span class="inline-flex items-center gap-1 px-2 py-[3px] rounded-full font-twc18-mono text-[9px] font-extrabold tracking-[0.14em] uppercase text-twc18-hot bg-twc18-hot/12 border border-twc18-hot/26">
          <span aria-hidden="true" class="size-[5px] rounded-full bg-twc18-hot text-twc18-hot shadow-[0_0_6px_currentColor] animate-twc18-pulse motion-reduce:animate-none"></span>
          NEURAL v4
        </span>
        <span class="inline-flex items-center px-2 py-[3px] rounded-full font-twc18-mono text-[9px] font-extrabold tracking-[0.14em] uppercase text-white/85 bg-white/6 border border-white/12">4K OUTPUT</span>
        <span class="inline-flex items-center px-2 py-[3px] rounded-full font-twc18-mono text-[9px] font-extrabold tracking-[0.14em] uppercase text-white/85 bg-white/6 border border-white/12">MIT</span>
      </div>

      <h3 class="m-0 mb-1.5 text-xl/[1.15] font-extrabold tracking-[-0.02em] text-white [background-image:linear-gradient(135deg,#ffffff_0%,#ffb3d9_100%)] bg-clip-text text-transparent forced-colors:text-[CanvasText] forced-colors:[-webkit-text-fill-color:CanvasText]">Neural Style Transfer</h3>
      <p class="m-0 mb-4 text-[12.5px]/[1.55] tracking-[-0.005em] text-white/65">Diffusion models trained on 12 curated art movements. Brush-level control, in the terminal or on the canvas.</p>

      <div class="grid grid-cols-[1fr_auto] gap-1.5">
        <a href="#try" class="group/cta relative isolate inline-flex items-center justify-center overflow-hidden min-h-11 px-4.5 rounded-xl no-underline text-[12.5px] font-bold tracking-[-0.01em] text-twc18-ctaink [background:linear-gradient(180deg,#ff5cb1_0%,#ff2d92_100%)] [forced-color-adjust:none] shadow-[0_4px_12px_oklch(0.65_0.28_350/0.4),inset_0_0_0_1px_oklch(1_0_0/0.14)] transition-[transform,box-shadow] duration-200 hover:-translate-y-px hover:shadow-[0_8px_22px_oklch(0.65_0.28_350/0.6),inset_0_0_0_1px_oklch(1_0_0/0.24)] focus-visible:outline-2 focus-visible:outline-twc18-focus focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
          <span aria-hidden="true" class="absolute -inset-[30px] z-0 opacity-0 blur-[12px] transition-opacity duration-300 group-hover/cta:opacity-100 motion-reduce:transition-none [background:radial-gradient(circle_at_center,oklch(0.65_0.28_350/0.7)_0%,transparent_60%)]"></span>
          <span class="relative z-2 inline-flex items-center gap-1.5">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
            Try nova free
          </span>
          <span aria-hidden="true" class="relative z-2 ml-1.5 inline-flex items-center transition-transform duration-200 group-hover/cta:translate-x-1 motion-reduce:transition-none motion-reduce:group-hover/cta:translate-x-0">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </span>
        </a>
        <a href="#docs" class="inline-flex items-center justify-center gap-1.5 min-h-11 px-3.5 rounded-xl no-underline text-[12.5px] font-semibold tracking-[-0.01em] text-white bg-white/6 border border-white/12 transition-[background] duration-200 hover:bg-white/12 focus-visible:outline-2 focus-visible:outline-twc18-focus focus-visible:outline-offset-2">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
          Docs
        </a>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc18-bg: #050510;
  --color-twc18-bg: oklch(0.1 0.02 280);
  --color-twc18-ink: #f4f4fb;
  --color-twc18-ink: oklch(0.96 0.005 285);
  --color-twc18-hot: #ff2d92;
  --color-twc18-hot: oklch(0.65 0.28 350);
  --color-twc18-cyan: #22d3ee;
  --color-twc18-cyan: oklch(0.8 0.13 200);
  --color-twc18-lime: #a3ff5f;
  --color-twc18-lime: oklch(0.91 0.22 130);
  --color-twc18-focus: #a5f3fc;
  --color-twc18-focus: oklch(0.91 0.07 200);
  --color-twc18-ctaink: #12001a;
  --color-twc18-ctaink: oklch(0.12 0.06 320);
  --font-twc18-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc18-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --animate-twc18-arc: twc18-arc 4s linear infinite;
  --animate-twc18-spin: twc18-spin 0.8s linear infinite;
  --animate-twc18-caret: twc18-caret 1s step-end infinite;
  --animate-twc18-pulse: twc18-pulse 2s ease-in-out infinite;
  --animate-twc18-rise: twc18-rise 3.5s ease-in-out infinite;
}
/* @property is the one thing in this collection that CANNOT be a utility:
   a custom property must be registered with a syntax before it can be
   interpolated, and the rotating rim is an animated gradient angle. */

@property --twc18-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}
/* The rim's conic gradient reads --twc18-angle, so it lives in a class rather
   than an arbitrary property: an arbitrary value cannot reference a registered
   property that the same element animates. */

.twc18-rim {
  background: conic-gradient(from var(--twc18-angle),
      transparent 0deg,
      oklch(0.65 0.28 350) 6deg,
      transparent 26deg,
      transparent 180deg,
      oklch(0.8 0.13 200) 186deg,
      transparent 206deg,
      transparent 360deg);
}
/* iOS Safari < 16 paints an unsupported conic-gradient as flat colour. */

@supports not (background: conic-gradient(from 0deg, red, blue)) {
  .twc18-rim {
    background: linear-gradient(135deg, oklch(0.65 0.28 350), oklch(0.8 0.13 200));
  }
}

@keyframes twc18-arc {
  to {
    --twc18-angle: 360deg;
  }
}

@keyframes twc18-spin {
  to {
    transform: rotate(360deg);
  }
}

@keyframes twc18-caret {
  50% {
    opacity: 0;
  }
}

@keyframes twc18-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(1.4);
    opacity: 0.5;
  }
}

@keyframes twc18-rise {
  0% {
    bottom: 0;
    opacity: 0;
    transform: translateX(0);
  }

  15% {
    opacity: 1;
  }

  100% {
    bottom: 100%;
    opacity: 0;
    transform: translateX(20px);
  }
}

.twc-18 {
  width: 100%;
  min-height: 100svh;
}
```
