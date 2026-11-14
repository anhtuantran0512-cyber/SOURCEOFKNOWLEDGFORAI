---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-onboarding-slider-scroll-marker-dots/"
title: "Tailwind Onboarding Slider with Native CSS Scroll-Marker Dots"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "A phone-width first-run tutorial with illustration, copy and indicator dots."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Onboarding Slider with Native CSS Scroll-Marker Dots
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-onboarding-slider-scroll-marker-dots/

A phone-width first-run tutorial with illustration, copy and indicator dots. The dots are not markup at all — ::scroll-marker generates one per panel and tracks the active one, which is the first carousel primitive the browser has ever owned.
## HTML
```html
<section class="tcar-11 w-full min-h-svh grid place-items-center bg-tcar11-bg font-tcar11-sans px-5 py-10" aria-label="App onboarding">
  <div class="w-[300px] max-w-full bg-white rounded-[34px] p-4 border border-tcar11-edge shadow-[0_30px_60px_-34px_oklch(0.3_0.08_290/0.6)]">
    <ol tabindex="0" role="group" aria-label="Onboarding steps, swipe or use arrow keys" class="tcar11-scroller list-none flex overflow-x-auto m-0 p-0 rounded-[22px] snap-x snap-mandatory [scrollbar-width:none] [scroll-marker-group:after] focus-visible:outline-3 focus-visible:outline-tcar11-acc focus-visible:outline-offset-[3px]">
      <li class="flex-none basis-full snap-center px-5 pt-2 pb-5 text-center">
        <div class="aspect-square rounded-[20px] overflow-hidden mb-[22px] bg-[linear-gradient(135deg,#6a5cff,#9b8bff)]"><img src="https://picsum.photos/seed/onb-1/400/400" width="400" height="400" decoding="async" alt="Track your habits illustration" class="size-full object-cover block mix-blend-luminosity opacity-90"></div>
        <p class="text-[11px] font-semibold tracking-[0.14em] uppercase text-tcar11-mute mb-2">Step 1 of 3</p>
        <h3 class="text-xl font-extrabold text-tcar11-ink mb-2">Track what matters</h3>
        <p class="text-sm leading-[1.55] text-tcar11-mute m-0">Log habits in two taps and watch streaks build over time.</p>
      </li>
      <li class="flex-none basis-full snap-center px-5 pt-2 pb-5 text-center">
        <div class="aspect-square rounded-[20px] overflow-hidden mb-[22px] bg-[linear-gradient(135deg,#00b3a4,#4fd1c5)]"><img src="https://picsum.photos/seed/onb-2/400/400" width="400" height="400" loading="lazy" decoding="async" alt="Get reminders illustration" class="size-full object-cover block mix-blend-luminosity opacity-90"></div>
        <p class="text-[11px] font-semibold tracking-[0.14em] uppercase text-tcar11-mute mb-2">Step 2 of 3</p>
        <h3 class="text-xl font-extrabold text-tcar11-ink mb-2">Gentle reminders</h3>
        <p class="text-sm leading-[1.55] text-tcar11-mute m-0">Smart nudges at the right moment &mdash; never spammy, always optional.</p>
      </li>
      <li class="flex-none basis-full snap-center px-5 pt-2 pb-5 text-center">
        <div class="aspect-square rounded-[20px] overflow-hidden mb-[22px] bg-[linear-gradient(135deg,#ff7a59,#ffb057)]"><img src="https://picsum.photos/seed/onb-3/400/400" width="400" height="400" loading="lazy" decoding="async" alt="See progress illustration" class="size-full object-cover block mix-blend-luminosity opacity-90"></div>
        <p class="text-[11px] font-semibold tracking-[0.14em] uppercase text-tcar11-mute mb-2">Step 3 of 3</p>
        <h3 class="text-xl font-extrabold text-tcar11-ink mb-2">See your progress</h3>
        <p class="text-sm leading-[1.55] text-tcar11-mute m-0">Weekly insights that show how far you've come, at a glance.</p>
      </li>
    </ol>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar11-bg: #eceafb;
  --color-tcar11-bg: oklch(0.93 0.025 285);
  --color-tcar11-edge: #e2ddf6;
  --color-tcar11-edge: oklch(0.91 0.025 285);
  --color-tcar11-ink: #231d4a;
  --color-tcar11-ink: oklch(0.28 0.08 285);
  --color-tcar11-mute: #5f5982;
  --color-tcar11-mute: oklch(0.48 0.05 285);
  --color-tcar11-dot: #c9c2f2;
  --color-tcar11-dot: oklch(0.82 0.06 285);
  --color-tcar11-acc: #6a5cff;
  --color-tcar11-acc: oklch(0.55 0.22 285);
  --font-tcar11-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tcar-11 {
  width: 100%;
  min-height: 100svh;
}

.tcar-11 ::selection {
  background: var(--color-tcar11-acc);
  color: #fff;
}

.tcar11-scroller::-webkit-scrollbar {
  display: none;
}
/* CSS Carousel primitives: no utility form exists, and inventing one would obscure them. */

.tcar11-scroller::scroll-marker-group {
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 14px;
}

.tcar11-scroller li::scroll-marker {
  content: "";
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--color-tcar11-dot);
  margin: 6px;
  cursor: pointer;
  border: 0;
  transition: scale .2s, background-color .2s;
}

.tcar11-scroller li::scroll-marker:target-current {
  background: var(--color-tcar11-acc);
  scale: 1.35;
}

@media (prefers-reduced-motion: reduce) {
  .tcar11-scroller {
    scroll-behavior: auto;
  }

  .tcar11-scroller li::scroll-marker {
    transition: none;
  }
}
```
