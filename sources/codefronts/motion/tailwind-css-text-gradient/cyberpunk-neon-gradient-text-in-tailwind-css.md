---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/cyberpunk-neon-gradient-text-in-tailwind-css/"
title: "Cyberpunk Neon Gradient Text in Tailwind CSS"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "A CRT-lit HUD panel: pink, cyan and acid-yellow gradient type with drop-shadow-[0_0_10px_…] neon bloom, a scanline overlay drawn with…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cyberpunk Neon Gradient Text in Tailwind CSS
Source: https://codefronts.com/motion/tailwind-css-text-gradient/cyberpunk-neon-gradient-text-in-tailwind-css/

A CRT-lit HUD panel: pink, cyan and acid-yellow gradient type with drop-shadow-[0_0_10px_…] neon bloom, a scanline overlay drawn with repeating-linear-gradient, corner brackets and a shimmering sync bar. The CSS original's labels sat at 2:1 contrast; every label here clears 4.5:1 without losing the mood.
## HTML
```html
<section class="ttg-09 w-full min-h-svh grid place-items-center bg-ttg09-bg bg-[radial-gradient(70%_50%_at_50%_0%,var(--color-ttg09-glow),transparent)] px-5 py-14 font-ttg09-display text-ttg09-ink" aria-label="Cyberpunk neon gradient text demo">
  <div class="relative w-full max-w-2xl overflow-hidden border border-ttg09-cyan/25 bg-ttg09-panel p-9 before:absolute before:top-2 before:left-2 before:size-4 before:border-t-2 before:border-l-2 before:border-ttg09-cyan after:absolute after:right-2 after:bottom-2 after:size-4 after:border-r-2 after:border-b-2 after:border-ttg09-pink max-sm:p-6">
    <span aria-hidden="true" class="pointer-events-none absolute inset-0 z-10 bg-[repeating-linear-gradient(0deg,transparent_0_2px,var(--color-ttg09-scan)_2px_4px)]"></span>
    <p class="font-ttg09-mono text-[11px] tracking-[0.14em] text-ttg09-cyan-soft">SYS://NEXUS_2077 — USER AUTHENTICATED<span aria-hidden="true" class="ml-1 inline-block h-3 w-1.5 translate-y-0.5 bg-ttg09-cyan animate-ttg09-caret motion-reduce:animate-none"></span></p>
    <h1 class="mt-5 flex flex-wrap gap-x-[0.18em] text-[clamp(3rem,11vw,6rem)] leading-[0.95] font-bold tracking-[0.03em]">
      <span class="bg-linear-to-r from-ttg09-pink to-ttg09-purple bg-clip-text text-transparent drop-shadow-[0_0_10px_var(--color-ttg09-pink)]">CYBER</span><span class="bg-linear-to-r from-ttg09-cyan to-ttg09-blue bg-clip-text text-transparent drop-shadow-[0_0_10px_var(--color-ttg09-cyan)]">PUNK</span>
    </h1>
    <p class="mt-2 text-[clamp(1.1rem,3.6vw,1.9rem)] font-semibold tracking-[0.2em]"><span class="bg-linear-to-r from-ttg09-yellow to-ttg09-orange bg-clip-text text-transparent drop-shadow-[0_0_6px_var(--color-ttg09-yellow)]">NEON</span> <span class="bg-linear-to-r from-ttg09-purple to-ttg09-pink bg-clip-text text-transparent">INTERFACE</span></p>
    <dl class="mt-8 grid grid-cols-3 gap-4 border-y border-white/8 py-5">
      <div class="flex flex-col-reverse gap-1"><dt class="font-ttg09-mono text-[10.5px] tracking-[0.14em] text-ttg09-mut">THREAT</dt><dd class="w-fit bg-linear-to-r from-ttg09-pink to-ttg09-purple bg-clip-text text-2xl font-bold text-transparent">78%</dd></div>
      <div class="flex flex-col-reverse gap-1"><dt class="font-ttg09-mono text-[10.5px] tracking-[0.14em] text-ttg09-mut">CREDITS</dt><dd class="w-fit bg-linear-to-r from-ttg09-yellow to-ttg09-orange bg-clip-text text-2xl font-bold text-transparent">4,096</dd></div>
      <div class="flex flex-col-reverse gap-1"><dt class="font-ttg09-mono text-[10.5px] tracking-[0.14em] text-ttg09-mut">CLEARANCE</dt><dd class="w-fit bg-linear-to-r from-ttg09-cyan to-ttg09-blue bg-clip-text text-2xl font-bold text-transparent">LVL 9</dd></div>
    </dl>
    <div class="mt-5">
      <div class="flex justify-between font-ttg09-mono text-[10.5px] tracking-[0.14em] text-ttg09-mut"><span id="ttg09-sync">NEURAL SYNC</span><span aria-hidden="true" class="text-ttg09-cyan-soft">78%</span></div>
      <div class="mt-2 h-1.5 overflow-hidden rounded-full bg-white/8" role="progressbar" aria-labelledby="ttg09-sync" aria-valuenow="78" aria-valuemin="0" aria-valuemax="100"><div class="h-full w-[78%] rounded-full bg-linear-to-r from-ttg09-cyan via-ttg09-purple to-ttg09-pink bg-[length:200%_100%] shadow-[0_0_12px_var(--color-ttg09-purple)] animate-ttg09-scan motion-reduce:animate-none"></div></div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg09-bg: #05020d;
  --color-ttg09-bg: oklch(0.12 0.03 295);
  --color-ttg09-glow: #2b0a4a99;
  --color-ttg09-glow: oklch(0.25 0.12 305 / 0.6);
  --color-ttg09-panel: #0a0617e6;
  --color-ttg09-panel: oklch(0.15 0.035 295 / 0.9);
  --color-ttg09-ink: #ece5f7;
  --color-ttg09-ink: oklch(0.93 0.02 300);
  --color-ttg09-mut: #a597c4;
  --color-ttg09-mut: oklch(0.71 0.06 295);
  --color-ttg09-scan: #00f0ff0d;
  --color-ttg09-scan: oklch(0.88 0.15 200 / 0.05);
  --color-ttg09-pink: #ff2d78;
  --color-ttg09-pink: oklch(0.65 0.25 5);
  --color-ttg09-cyan: #00f0ff;
  --color-ttg09-cyan: oklch(0.88 0.15 200);
  --color-ttg09-cyan-soft: #8ff2ff;
  --color-ttg09-cyan-soft: oklch(0.91 0.09 205);
  --color-ttg09-blue: #2b8cff;
  --color-ttg09-blue: oklch(0.64 0.19 255);
  --color-ttg09-purple: #c040ff;
  --color-ttg09-purple: oklch(0.63 0.27 310);
  --color-ttg09-yellow: #ffe600;
  --color-ttg09-yellow: oklch(0.92 0.19 102);
  --color-ttg09-orange: #ff8c00;
  --color-ttg09-orange: oklch(0.75 0.18 60);
  --font-ttg09-display: 'Chakra Petch', system-ui, sans-serif;
  --font-ttg09-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ttg09-scan: ttg09-scan 2.4s linear infinite;
  --animate-ttg09-caret: ttg09-caret 1.1s step-end infinite;

  @keyframes ttg09-scan {
    from {
      background-position: 0% 50%;
    }

    to {
      background-position: 200% 50%;
    }
  }

  @keyframes ttg09-caret {
    50% {
      opacity: 0;
    }
  }
}

.ttg-09 {
  width: 100%;
  min-height: 100svh;
}
```
