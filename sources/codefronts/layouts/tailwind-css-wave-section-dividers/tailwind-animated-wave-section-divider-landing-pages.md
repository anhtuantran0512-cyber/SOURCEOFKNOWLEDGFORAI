---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-animated-wave-section-divider-landing-pages/"
title: "Tailwind Animated Wave Section Divider for Landing Pages"
section: "layouts"
category: "tailwind-css-wave-section-dividers"
category_name: "Tailwind CSS Wave Section Dividers"
description: "Continuous liquid motion for SaaS and agency heroes: two identical seamless wave tiles slide sideways forever, so the crest never appears to end."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Wave Section Divider for Landing Pages
Source: https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-animated-wave-section-divider-landing-pages/

Continuous liquid motion for SaaS and agency heroes: two identical seamless wave tiles slide sideways forever, so the crest never appears to end. The port turns the whole animation into one utility &mdash; animate-twd02-drift &mdash; because in v4 an --animate-* token mints exactly that.
## HTML
```html
<section class="twd-02 w-full min-h-svh flex flex-col font-twd02-sans">

  <!-- Infinite ocean drift -->
  <div class="relative overflow-hidden bg-twd02-hero text-white px-6 pt-19 pb-29 text-center">
    <p class="font-twd02-mono text-xs tracking-[0.2em] uppercase text-twd02-onhero mb-3">Landing page hero</p>
    <h2 class="text-[clamp(26px,4.2vw,42px)] leading-[1.1] font-semibold">Ship faster with fluid sections</h2>
    <div aria-hidden="true" class="absolute inset-x-0 -bottom-px h-[clamp(60px,9vw,110px)] pointer-events-none">
      <div class="flex w-[200%] h-full animate-twd02-drift motion-reduce:animate-none">
        <svg class="block w-1/2 h-full fill-twd02-pale" viewBox="0 0 1440 110" preserveAspectRatio="none" focusable="false"><path d="M0,60 C180,100 360,20 720,60 C1080,100 1260,20 1440,60 L1440,110 L0,110 Z"></path></svg>
        <svg class="block w-1/2 h-full fill-twd02-pale" viewBox="0 0 1440 110" preserveAspectRatio="none" focusable="false"><path d="M0,60 C180,100 360,20 720,60 C1080,100 1260,20 1440,60 L1440,110 L0,110 Z"></path></svg>
      </div>
    </div>
  </div>
  <div class="bg-twd02-pale text-twd02-deep px-6 pt-9 pb-16 text-center">
    <p class="text-[15px]">Transform-only loop &mdash; 0 layout, 0 paint, 0 CLS.</p>
  </div>

  <!-- Three-layer parallax swell -->
  <div class="relative overflow-hidden bg-twd02-sea text-white px-6 pt-18 pb-31 text-center">
    <h2 class="text-[clamp(25px,4vw,38px)] font-semibold">Layered liquid depth</h2>
    <div aria-hidden="true" class="absolute inset-x-0 -bottom-px h-[clamp(66px,10vw,120px)] pointer-events-none">
      <div class="absolute inset-0 flex w-[200%] animate-twd02-drift [animation-duration:22s] motion-reduce:animate-none">
        <svg class="block w-1/2 h-full fill-twd02-foam/30" viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,70 C240,110 480,30 720,70 C960,110 1200,30 1440,70 L1440,120 L0,120 Z"></path></svg>
        <svg class="block w-1/2 h-full fill-twd02-foam/30" viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,70 C240,110 480,30 720,70 C960,110 1200,30 1440,70 L1440,120 L0,120 Z"></path></svg>
      </div>
      <div class="absolute inset-0 flex w-[200%] animate-twd02-drift [animation-duration:15s] [animation-direction:reverse] motion-reduce:animate-none">
        <svg class="block w-1/2 h-full fill-twd02-foam/60" viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,84 C200,44 420,120 720,84 C1020,48 1240,120 1440,84 L1440,120 L0,120 Z"></path></svg>
        <svg class="block w-1/2 h-full fill-twd02-foam/60" viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,84 C200,44 420,120 720,84 C1020,48 1240,120 1440,84 L1440,120 L0,120 Z"></path></svg>
      </div>
      <div class="absolute inset-0 flex w-[200%] animate-twd02-drift [animation-duration:9s] motion-reduce:animate-none">
        <svg class="block w-1/2 h-full fill-twd02-foam" viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,96 C260,120 460,64 720,96 C980,124 1180,64 1440,96 L1440,120 L0,120 Z"></path></svg>
        <svg class="block w-1/2 h-full fill-twd02-foam" viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,96 C260,120 460,64 720,96 C980,124 1180,64 1440,96 L1440,120 L0,120 Z"></path></svg>
      </div>
    </div>
  </div>
  <div class="bg-twd02-foam text-twd02-seaink px-6 pt-9 pb-16 text-center">
    <p class="text-[15px]">Different durations per layer = parallax with no scroll listener.</p>
  </div>

</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twd02-hero: #2a3a6b;
  --color-twd02-hero: oklch(0.34 0.12 262);
  --color-twd02-onhero: #b9c2e2;
  --color-twd02-onhero: oklch(0.8 0.05 262);
  --color-twd02-pale: #f2f5fb;
  --color-twd02-pale: oklch(0.96 0.02 255);
  --color-twd02-deep: #37426b;
  --color-twd02-deep: oklch(0.38 0.07 262);
  --color-twd02-sea: #1a6f8e;
  --color-twd02-sea: oklch(0.48 0.12 225);
  --color-twd02-foam: #f0f8fb;
  --color-twd02-foam: oklch(0.97 0.02 215);
  --color-twd02-seaink: #22566a;
  --color-twd02-seaink: oklch(0.4 0.07 225);
  --font-twd02-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twd02-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-twd02-drift: twd02-drift 14s linear infinite;
}

@keyframes twd02-drift {
  from {
    transform: translate3d(0, 0, 0);
  }

  to {
    transform: translate3d(-50%, 0, 0);
  }
}

.twd-02 {
  width: 100%;
  min-height: 100svh;
}
```
