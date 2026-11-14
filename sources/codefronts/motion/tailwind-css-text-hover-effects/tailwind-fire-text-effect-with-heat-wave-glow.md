---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-fire-text-effect-with-heat-wave-glow/"
title: "Tailwind Fire Text Effect with Heat Wave Glow"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A hot-sauce wordmark that catches fire on hover: five upward-stacked text-shadow layers — yellow core to smoke — jittered by a steps(3) keyframe, plus a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Fire Text Effect with Heat Wave Glow
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-fire-text-effect-with-heat-wave-glow/

A hot-sauce wordmark that catches fire on hover: five upward-stacked text-shadow layers — yellow core to smoke — jittered by a steps(3) keyframe, plus a ±0.5° skew loop for heat haze. At rest a slow ember pulse breathes. Both hover animations ship as one --animate-tth24-blaze token.
## HTML
```html
<section class="tth-24 w-full min-h-svh grid place-items-center bg-tth24-bg bg-[radial-gradient(90%_60%_at_50%_100%,oklch(0.26_0.07_35/0.85),transparent_60%),radial-gradient(90%_70%_at_50%_20%,var(--color-tth24-glow),var(--color-tth24-bg)_75%)] px-5 py-14 font-tth24-sans text-tth24-ink" aria-label="Fire heat wave text demo">
  <div class="flex flex-col items-center gap-[clamp(16px,3vw,26px)] text-center">
    <p class="text-xs font-bold uppercase tracking-[0.26em] text-tth24-mut">Small-batch hot sauce &middot; Carolina Reaper edition</p>
    <a id="tth24-top" href="#tth24-top" class="inline-block rounded-lg px-[0.2em] pt-[0.35em] pb-[0.12em] font-tth24-display text-[clamp(60px,14vw,150px)] leading-none tracking-[0.01em] text-tth24-coal no-underline animate-tth24-ember hover:text-tth24-flame hover:animate-tth24-blaze focus-visible:text-tth24-flame focus-visible:animate-tth24-blaze focus-visible:outline-2 focus-visible:outline-offset-8 focus-visible:outline-tth24-hot motion-reduce:animate-none! motion-reduce:hover:[text-shadow:0_-.06em_.1em_oklch(0.85_0.15_75/0.7),0_-.16em_.22em_oklch(0.65_0.18_45/0.5),0_-.28em_.3em_oklch(0.5_0.15_30/0.35)]">SCORCH</a>
    <p class="max-w-[44ch] text-[15px] leading-[1.7] text-tth24-mut">Bottled at 1.2 million Scoville. Hover the name; decide if you're serious.</p>
    <div class="mt-1 flex flex-col items-center gap-2.5">
      <a href="#tth24-top" class="grid min-h-[54px] place-items-center rounded-xl bg-[linear-gradient(180deg,oklch(0.6_0.21_40),oklch(0.48_0.19_30))] px-[30px] text-base font-extrabold text-white no-underline shadow-[0_0_0_transparent,0_0_0_transparent,inset_0_1px_0_oklch(1_0_0/0.2)] transition-[box-shadow,translate] duration-400 hover:-translate-y-0.5 hover:shadow-[0_-6px_22px_oklch(0.62_0.21_40/0.5),0_8px_26px_oklch(0.4_0.15_30/0.55),inset_0_1px_0_oklch(1_0_0/0.2)] focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth24-flame">Dare the sauce</a>
      <span class="text-xs italic text-tth24-mut">ships with a waiver, mostly as a joke</span>
    </div>
    <p class="max-w-[54ch] text-[12.5px] leading-[1.7] text-tth24-mut">Five <code class="rounded bg-tth24-chip px-1.5 py-px font-tth24-mono text-[0.9em] text-tth24-hot">text-shadow</code> layers stacked upward &mdash; yellow to smoke &mdash; jittered by <code class="rounded bg-tth24-chip px-1.5 py-px font-tth24-mono text-[0.9em] text-tth24-hot">steps(3)</code>; a &plusmn;.5deg skew loop is the heat haze.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth24-bg: #110a08;
  --color-tth24-bg: oklch(0.14 0.01 30);
  --color-tth24-glow: #1a1210;
  --color-tth24-glow: oklch(0.18 0.014 30);
  --color-tth24-chip: #2a1d18;
  --color-tth24-chip: oklch(0.24 0.02 35);
  --color-tth24-ink: #f2e2c4;
  --color-tth24-ink: oklch(0.91 0.04 75);
  --color-tth24-mut: #b09a8a;
  --color-tth24-mut: oklch(0.71 0.03 45);
  --color-tth24-hot: #f7a440;
  --color-tth24-hot: oklch(0.79 0.16 60);
  --color-tth24-coal: #e8b878;
  --color-tth24-coal: oklch(0.82 0.1 65);
  --color-tth24-flame: #fff2b0;
  --color-tth24-flame: oklch(0.95 0.09 95);
  --font-tth24-display: 'Bowlby One', Impact, sans-serif;
  --font-tth24-sans: 'Chivo', system-ui, sans-serif;
  --font-tth24-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tth24-ember: tth24-ember 2.8s ease-in-out infinite;
  --animate-tth24-blaze: tth24-flick 0.55s steps(3, jump-none) infinite, tth24-haze 0.18s ease-in-out infinite alternate;

  @keyframes tth24-ember {
    0%,
        100% {
      text-shadow: 0 -0.04em 0.06em oklch(0.7 0.14 55 / 0.35), 0 -0.12em 0.16em oklch(0.55 0.15 35 / 0.25), 0 -0.2em 0.25em oklch(0.4 0.12 28 / 0.2), 0 -0.3em 0.3em transparent, 0 -0.4em 0.35em transparent;
    }

    50% {
      text-shadow: 0 -0.05em 0.07em oklch(0.7 0.14 55 / 0.5), 0 -0.14em 0.18em oklch(0.55 0.15 35 / 0.35), 0 -0.22em 0.27em oklch(0.4 0.12 28 / 0.28), 0 -0.32em 0.32em transparent, 0 -0.42em 0.37em transparent;
    }
  }

  @keyframes tth24-flick {
    0%,
        100% {
      text-shadow: 0 -0.04em 0.02em oklch(0.93 0.15 95), 0 -0.13em 0.06em oklch(0.78 0.17 55), 0 -0.26em 0.12em oklch(0.62 0.21 32), 0 -0.42em 0.2em oklch(0.45 0.16 25), 0.02em -0.6em 0.3em oklch(0.3 0.05 25 / 0.8);
    }

    38% {
      text-shadow: 0 -0.05em 0.02em oklch(0.93 0.15 95), 0.01em -0.16em 0.07em oklch(0.78 0.17 55), -0.02em -0.3em 0.13em oklch(0.62 0.21 32), 0.02em -0.48em 0.22em oklch(0.45 0.16 25), -0.03em -0.66em 0.32em oklch(0.3 0.05 25 / 0.8);
    }

    72% {
      text-shadow: 0 -0.035em 0.02em oklch(0.93 0.15 95), -0.015em -0.11em 0.05em oklch(0.78 0.17 55), 0.02em -0.22em 0.11em oklch(0.62 0.21 32), -0.02em -0.38em 0.19em oklch(0.45 0.16 25), 0.03em -0.55em 0.28em oklch(0.3 0.05 25 / 0.8);
    }
  }

  @keyframes tth24-haze {
    from {
      transform: skewX(-0.5deg);
    }

    to {
      transform: skewX(0.5deg);
    }
  }
}

.tth-24 {
  width: 100%;
  min-height: 100svh;
}
```
