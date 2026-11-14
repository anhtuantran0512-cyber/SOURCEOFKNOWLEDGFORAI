---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-css-glitch-text-hover-effect/"
title: "Tailwind CSS Glitch Text Hover Effect"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A cyberpunk title that shreds on hover: two clones generated with before:content-[attr(data-text)] — one red, one cyan — sliced by clip-path keyframes on a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Glitch Text Hover Effect
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-css-glitch-text-hover-effect/

A cyberpunk title that shreds on hover: two clones generated with before:content-[attr(data-text)] — one red, one cyan — sliced by clip-path keyframes on a steps() clock while the base jitters. Scanlines are an before: repeating gradient on the stage. Pure Tailwind: every keyframe lives in @theme.
## HTML
```html
<section class="tth-06 @container relative isolate w-full min-h-svh grid place-items-center overflow-clip bg-tth06-bg bg-[radial-gradient(90%_70%_at_50%_30%,var(--color-tth06-glow),var(--color-tth06-bg)_70%)] px-5 py-14 font-tth06-mono text-tth06-ink before:pointer-events-none before:absolute before:inset-0 before:-z-10 before:bg-[repeating-linear-gradient(0deg,oklch(1_0_0/0.035)_0_1px,transparent_1px_3px)] before:content-['']" aria-label="Glitch text hover demo">
  <div class="relative flex flex-col items-center gap-[clamp(14px,2.6cqi,22px)] text-center">
    <p class="text-[11.5px] tracking-[0.3em] text-tth06-mut">///&nbsp;SIGNAL 07 &mdash; UNSTABLE FEED</p>
    <a id="tth06-top" href="#tth06-top" data-text="NULLSECT//26" class="relative z-0 inline-block font-tth06-display text-[clamp(38px,9.4cqi,96px)] font-bold leading-[1.05] tracking-[-0.01em] no-underline [text-shadow:1px_0_color-mix(in_oklch,var(--color-tth06-red)_55%,transparent),-1px_0_color-mix(in_oklch,var(--color-tth06-cyan)_55%,transparent)] before:pointer-events-none before:absolute before:inset-0 before:-z-10 before:text-tth06-red before:opacity-0 before:content-[attr(data-text)] after:pointer-events-none after:absolute after:inset-0 after:-z-20 after:text-tth06-cyan after:opacity-0 after:content-[attr(data-text)] hover:animate-tth06-base hover:before:opacity-90 hover:before:animate-tth06-slice-a hover:after:opacity-90 hover:after:animate-tth06-slice-b focus-visible:animate-tth06-base focus-visible:before:opacity-90 focus-visible:before:animate-tth06-slice-a focus-visible:after:opacity-90 focus-visible:after:animate-tth06-slice-b focus-visible:outline-2 focus-visible:outline-offset-[10px] focus-visible:outline-tth06-cyan motion-reduce:animate-none! motion-reduce:before:animate-none! motion-reduce:after:animate-none!">NULLSECT//26</a>
    <p class="text-[13.5px] tracking-[0.06em] text-tth06-mut">Live briefing &mdash; offensive security summit &middot; night block</p>
    <div class="mt-1 flex flex-wrap justify-center gap-2.5">
      <span class="border border-tth06-line px-3.5 py-2.5 text-[11px] tracking-[0.18em] text-tth06-mut">OCT 31</span>
      <span class="border border-tth06-line px-3.5 py-2.5 text-[11px] tracking-[0.18em] text-tth06-mut">SYDNEY + STREAM</span>
      <a href="#tth06-top" class="inline-flex min-h-11 items-center gap-2 border border-tth06-cyan/45 bg-tth06-cyan/6 px-3.5 text-[11px] tracking-[0.18em] text-tth06-cyan no-underline transition-colors hover:bg-tth06-cyan hover:text-tth06-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tth06-cyan"><span aria-hidden="true" class="size-1.5 rounded-full bg-current animate-pulse motion-reduce:animate-none"></span>REGISTER FOR STREAM</a>
    </div>
    <p class="max-w-[56ch] text-xs leading-[1.7] text-tth06-mut">Hover or focus the title. Two <code class="rounded bg-tth06-chip px-1.5 py-px text-[0.92em] text-tth06-cyan">content-[attr(data-text)]</code> clones, red and cyan, shredded by <code class="rounded bg-tth06-chip px-1.5 py-px text-[0.92em] text-tth06-cyan">clip-path</code> on a <code class="rounded bg-tth06-chip px-1.5 py-px text-[0.92em] text-tth06-cyan">steps()</code> clock.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth06-bg: #0c0d13;
  --color-tth06-bg: oklch(0.14 0.01 270);
  --color-tth06-glow: #15161f;
  --color-tth06-glow: oklch(0.19 0.02 275);
  --color-tth06-chip: #1f2029;
  --color-tth06-chip: oklch(0.24 0.015 270);
  --color-tth06-line: #33343f;
  --color-tth06-line: oklch(0.34 0.02 260);
  --color-tth06-ink: #f0f5f6;
  --color-tth06-ink: oklch(0.96 0.005 200);
  --color-tth06-mut: #9da2b0;
  --color-tth06-mut: oklch(0.72 0.02 250);
  --color-tth06-red: #f2304a;
  --color-tth06-red: oklch(0.62 0.24 22);
  --color-tth06-cyan: #5fd8ec;
  --color-tth06-cyan: oklch(0.8 0.13 200);
  --font-tth06-mono: 'Space Mono', ui-monospace, monospace;
  --font-tth06-display: 'Space Grotesk', system-ui, sans-serif;
  --animate-tth06-base: tth06-base 0.8s steps(2, jump-none) infinite;
  --animate-tth06-slice-a: tth06-slice-a 0.7s steps(2, jump-none) infinite;
  --animate-tth06-slice-b: tth06-slice-b 0.9s steps(2, jump-none) infinite;

  @keyframes tth06-base {
    0%,
        100% {
      transform: translate(0, 0);
    }

    25% {
      transform: translate(1px, 0) skewX(0.4deg);
    }

    50% {
      transform: translate(-1px, 0);
    }

    75% {
      transform: translate(0, 1px) skewX(-0.4deg);
    }
  }

  @keyframes tth06-slice-a {
    0% {
      clip-path: inset(12% -2% 61% -2%);
      transform: translate(-3px, -2px);
    }

    25% {
      clip-path: inset(46% -2% 32% -2%);
      transform: translate(3px, 1px) skewX(2deg);
    }

    50% {
      clip-path: inset(78% -2% 5% -2%);
      transform: translate(-2px, 2px);
    }

    75% {
      clip-path: inset(4% -2% 82% -2%);
      transform: translate(2px, -1px);
    }

    100% {
      clip-path: inset(33% -2% 51% -2%);
      transform: translate(-3px, 0);
    }
  }

  @keyframes tth06-slice-b {
    0% {
      clip-path: inset(64% -2% 18% -2%);
      transform: translate(3px, 1px);
    }

    25% {
      clip-path: inset(8% -2% 74% -2%);
      transform: translate(-3px, -1px) skewX(-2deg);
    }

    50% {
      clip-path: inset(41% -2% 39% -2%);
      transform: translate(2px, 2px);
    }

    75% {
      clip-path: inset(84% -2% 2% -2%);
      transform: translate(-2px, 0);
    }

    100% {
      clip-path: inset(21% -2% 58% -2%);
      transform: translate(3px, -2px);
    }
  }
}

.tth-06 {
  width: 100%;
  min-height: 100svh;
}
```
