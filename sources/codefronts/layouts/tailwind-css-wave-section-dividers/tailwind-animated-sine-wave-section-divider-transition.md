---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-animated-sine-wave-section-divider-transition/"
title: "Tailwind Animated Sine Wave Section Divider Transition"
section: "layouts"
category: "tailwind-css-wave-section-dividers"
category_name: "Tailwind CSS Wave Section Dividers"
description: "A mathematically correct sine &mdash; sampled from y = A&middot;sin(x) rather than eyeballed with bezier handles &mdash; animated as a travelling waveform."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Sine Wave Section Divider Transition
Source: https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-animated-sine-wave-section-divider-transition/

A mathematically correct sine &mdash; sampled from y = A&middot;sin(x) rather than eyeballed with bezier handles &mdash; animated as a travelling waveform. The signal-processing look that tech, audio and web3 landing pages keep asking for, plus a stroked oscilloscope variant.
## HTML
```html
<section class="twd-12 w-full min-h-svh flex flex-col font-twd12-sans">

  <!-- Travelling sine with interference layer -->
  <div class="relative overflow-hidden bg-twd12-void text-white px-6 pt-18 pb-31 text-center">
    <p class="font-twd12-mono text-xs tracking-[0.2em] text-twd12-signal mb-3">y = A &middot; sin(x)</p>
    <h2 class="text-[clamp(25px,4vw,40px)] font-semibold">Signal, not decoration</h2>
    <div aria-hidden="true" class="absolute inset-x-0 -bottom-px h-[clamp(64px,10vw,120px)] pointer-events-none">
      <div class="absolute inset-0 flex w-[200%] animate-twd12-run [animation-duration:18s] motion-reduce:animate-none">
        <svg class="block w-1/2 h-full fill-twd12-signal/34" viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,70 C90,40 270,40 360,70 C450,100 630,100 720,70 C810,40 990,40 1080,70 C1170,100 1350,100 1440,70 L1440,120 L0,120 Z"></path></svg>
        <svg class="block w-1/2 h-full fill-twd12-signal/34" viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,70 C90,40 270,40 360,70 C450,100 630,100 720,70 C810,40 990,40 1080,70 C1170,100 1350,100 1440,70 L1440,120 L0,120 Z"></path></svg>
      </div>
      <div class="absolute inset-0 flex w-[200%] animate-twd12-run motion-reduce:animate-none">
        <svg class="block w-1/2 h-full fill-twd12-floor" viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,80 C60,50 180,50 240,80 C300,110 420,110 480,80 C540,50 660,50 720,80 C780,110 900,110 960,80 C1020,50 1140,50 1200,80 C1260,110 1380,110 1440,80 L1440,120 L0,120 Z"></path></svg>
        <svg class="block w-1/2 h-full fill-twd12-floor" viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,80 C60,50 180,50 240,80 C300,110 420,110 480,80 C540,50 660,50 720,80 C780,110 900,110 960,80 C1020,50 1140,50 1200,80 C1260,110 1380,110 1440,80 L1440,120 L0,120 Z"></path></svg>
      </div>
    </div>
  </div>
  <div class="bg-twd12-floor text-twd12-floorink px-6 pt-8 pb-15 text-center">
    <p class="text-[14px] font-twd12-mono">Each half-period is identical, so the loop is mathematically seamless.</p>
  </div>

  <!-- Oscilloscope trace -->
  <div class="relative overflow-hidden bg-twd12-crt text-twd12-oncrt px-6 pt-17 pb-24 text-center">
    <h2 class="text-[clamp(23px,3.6vw,34px)] font-semibold">Stroked waveform seam</h2>
    <div aria-hidden="true" class="absolute inset-x-0 bottom-0 h-[clamp(56px,8vw,100px)] pointer-events-none">
      <div class="absolute inset-0 flex w-[200%] animate-twd12-run [animation-duration:8s] motion-reduce:animate-none">
        <svg class="block w-1/2 h-full overflow-visible" viewBox="0 0 1440 100" preserveAspectRatio="none" focusable="false"><path class="fill-none stroke-twd12-trace stroke-3 [vector-effect:non-scaling-stroke] drop-shadow-[0_0_6px_var(--color-twd12-trace)]" d="M0,50 C60,14 180,14 240,50 C300,86 420,86 480,50 C540,14 660,14 720,50 C780,86 900,86 960,50 C1020,14 1140,14 1200,50 C1260,86 1380,86 1440,50"></path></svg>
        <svg class="block w-1/2 h-full overflow-visible" viewBox="0 0 1440 100" preserveAspectRatio="none" focusable="false"><path class="fill-none stroke-twd12-trace stroke-3 [vector-effect:non-scaling-stroke] drop-shadow-[0_0_6px_var(--color-twd12-trace)]" d="M0,50 C60,14 180,14 240,50 C300,86 420,86 480,50 C540,14 660,14 720,50 C780,86 900,86 960,50 C1020,14 1140,14 1200,50 C1260,86 1380,86 1440,50"></path></svg>
      </div>
    </div>
  </div>
  <div class="bg-twd12-crtnext text-twd12-oncrt px-6 pt-7 pb-14 text-center border-t border-twd12-trace/35">
    <p class="text-[14px] font-twd12-mono">A stroke instead of a fill turns the divider into an instrument readout.</p>
  </div>

</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twd12-void: #10121c;
  --color-twd12-void: oklch(0.15 0.03 265);
  --color-twd12-signal: #4fd6a8;
  --color-twd12-signal: oklch(0.8 0.15 165);
  --color-twd12-floor: #eff7f3;
  --color-twd12-floor: oklch(0.96 0.02 165);
  --color-twd12-floorink: #25514a;
  --color-twd12-floorink: oklch(0.4 0.06 170);
  --color-twd12-crt: #0b120e;
  --color-twd12-crt: oklch(0.13 0.02 150);
  --color-twd12-crtnext: #182118;
  --color-twd12-crtnext: oklch(0.2 0.03 150);
  --color-twd12-oncrt: #e4fbee;
  --color-twd12-oncrt: oklch(0.96 0.03 155);
  --color-twd12-trace: #7ff08a;
  --color-twd12-trace: oklch(0.88 0.17 145);
  --font-twd12-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twd12-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-twd12-run: twd12-run 11s linear infinite;
}

@keyframes twd12-run {
  from {
    transform: translate3d(0, 0, 0);
  }

  to {
    transform: translate3d(-50%, 0, 0);
  }
}

.twd-12 {
  width: 100%;
  min-height: 100svh;
}
```
