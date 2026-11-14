---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-mobile-app-landing-hero-app-store-buttons/"
title: "Mobile App Landing Page Hero in Tailwind CSS with App Store Buttons"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "An iOS-pastel app-launch hero — three phone mockups with real mini-UI screens fanned in lavender, blush and powder blue, spreading wider on hover, above App…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mobile App Landing Page Hero in Tailwind CSS with App Store Buttons
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-mobile-app-landing-hero-app-store-buttons/

An iOS-pastel app-launch hero — three phone mockups with real mini-UI screens fanned in lavender, blush and powder blue, spreading wider on hover, above App Store and Google Play download badges. Gentle, rounded, unmistakably mobile.
## HTML
```html
<section class="ths-23 grid w-full min-h-svh items-center gap-10 overflow-hidden bg-linear-135 from-ths23-lav via-ths23-blush to-ths23-sky px-5 py-16 font-ths23-sans text-ths23-ink sm:px-12 lg:grid-cols-2 lg:gap-14" aria-label="Mobile app landing hero">
  <div class="max-w-lg">
    <span class="inline-flex items-center gap-2 rounded-full bg-white px-3.5 py-1.5 text-xs font-bold text-ths23-violet shadow-[0_6px_18px_-8px_rgb(120_80_150/0.35)]"><span role="img" aria-label="Rated 5 out of 5" class="tracking-[0.06em] text-ths23-star">★★★★★</span>#1 in Lifestyle</span>
    <h1 class="mt-5 text-[clamp(36px,5.4vw,60px)] leading-[1.04] font-extrabold tracking-[-0.025em] text-balance">Mood, sleep, joy — <em class="bg-linear-to-r from-ths23-violet to-ths23-rose bg-clip-text pr-1 text-transparent">tracked gently.</em></h1>
    <p class="mt-5 max-w-md text-[17px] leading-relaxed text-ths23-body">The wellness journal that doesn't gamify your serotonin into a streak.</p>
    <div class="mt-8 flex flex-wrap gap-3">
      <a href="#ios" class="inline-flex min-h-14 items-center gap-3 rounded-2xl bg-ths23-ink px-5 text-white transition hover:-translate-y-0.5 hover:shadow-[0_12px_24px_-10px_rgb(58_42_85/0.6)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths23-ink motion-reduce:transition-none">
        <svg aria-hidden="true" viewBox="0 0 24 24" class="size-6 fill-current"><path d="M16.4 12.6c0-2.4 2-3.6 2.1-3.7-1.2-1.700-3-1.900-3.600-2-1.5-.2-3 .9-3.700.9-.8 0-2-.9-3.200-.8-1.700 0-3.200 1-4 2.400-1.700 3-.4 7.400 1.200 9.800.8 1.200 1.800 2.500 3 2.400 1.200 0 1.700-.8 3.100-.8 1.500 0 1.900.8 3.200.8 1.300 0 2.100-1.200 2.900-2.400.9-1.300 1.300-2.600 1.300-2.700 0 0-2.400-.9-2.300-3.900zM14 5.400c.7-.8 1.100-1.900 1-3-.9 0-2.100.6-2.800 1.400-.6.700-1.200 1.800-1 2.900 1 .1 2.100-.5 2.800-1.300z"/></svg>
        <span class="flex flex-col leading-tight"><span class="text-[10px] tracking-[0.04em] text-white/80">Download on the</span><strong class="text-base font-bold">App Store</strong></span>
      </a>
      <a href="#android" class="inline-flex min-h-14 items-center gap-3 rounded-2xl bg-white px-5 text-ths23-ink ring-1 ring-ths23-ink/10 transition hover:-translate-y-0.5 hover:shadow-[0_12px_24px_-10px_rgb(58_42_85/0.4)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths23-ink motion-reduce:transition-none">
        <svg aria-hidden="true" viewBox="0 0 24 24" class="size-6"><path d="M4 3l10 9-10 9z" fill="#34a853"/><path d="M4 3l13 7.500L14 12z" fill="#4285f4"/><path d="M4 21l13-7.500L14 12z" fill="#ea4335"/><path d="M17 10.500l3 1.500-3 1.500-3-1.500z" fill="#fbbc04"/></svg>
        <span class="flex flex-col leading-tight"><span class="text-[10px] tracking-[0.04em] text-ths23-body">Get it on</span><strong class="text-base font-bold">Google Play</strong></span>
      </a>
    </div>
  </div>
  <div aria-hidden="true" class="group relative grid min-h-[420px] place-items-center">
    <div class="absolute h-[280px] w-[130px] -translate-x-[80%] -rotate-12 rounded-[28px] border-[3px] border-white bg-linear-to-b from-ths23-violet/70 to-ths23-violet p-3 shadow-[0_22px_50px_rgb(120_80_150/0.25)] transition-[translate,rotate] duration-500 ease-out group-hover:-translate-x-[118%] group-hover:-rotate-[16deg] motion-reduce:transition-none">
      <div class="mx-auto h-1.5 w-10 rounded-full bg-white/50"></div>
      <div class="mt-5 flex h-24 items-end gap-1.5"><span class="h-[40%] flex-1 rounded bg-white/60"></span><span class="h-[70%] flex-1 rounded bg-white/80"></span><span class="h-[55%] flex-1 rounded bg-white/60"></span><span class="h-[90%] flex-1 rounded bg-white"></span><span class="h-[65%] flex-1 rounded bg-white/70"></span></div>
      <div class="mt-4 space-y-2"><div class="h-2 w-3/4 rounded bg-white/60"></div><div class="h-2 w-1/2 rounded bg-white/40"></div></div>
    </div>
    <div class="absolute h-[280px] w-[130px] translate-x-[80%] rotate-12 rounded-[28px] border-[3px] border-white bg-linear-to-b from-ths23-sky to-ths23-steel p-3 shadow-[0_22px_50px_rgb(120_80_150/0.25)] transition-[translate,rotate] duration-500 ease-out group-hover:translate-x-[118%] group-hover:rotate-[16deg] motion-reduce:transition-none">
      <div class="mx-auto h-1.5 w-10 rounded-full bg-white/50"></div>
      <div class="mt-5 space-y-2.5"><div class="h-9 rounded-xl bg-white/70"></div><div class="h-9 rounded-xl bg-white/55"></div><div class="h-9 rounded-xl bg-white/45"></div><div class="h-9 rounded-xl bg-white/35"></div></div>
    </div>
    <div class="relative z-10 h-[310px] w-[148px] rounded-[30px] border-[3px] border-white bg-linear-to-b from-ths23-blush to-ths23-rose p-3 shadow-[0_28px_60px_rgb(120_80_150/0.32)] transition-transform duration-500 group-hover:-translate-y-2 motion-reduce:transition-none">
      <div class="mx-auto h-1.5 w-12 rounded-full bg-white/60"></div>
      <p class="mt-5 text-center text-[10px] font-bold tracking-[0.1em] text-ths23-ink/70 uppercase">Sleep</p>
      <div class="mx-auto mt-2 grid size-24 place-items-center rounded-full bg-[conic-gradient(var(--color-ths23-ink)_0_78%,rgb(255_255_255/0.6)_78%_100%)]"><div class="grid size-[78px] place-items-center rounded-full bg-ths23-blush text-lg font-extrabold text-ths23-ink">7h 48</div></div>
      <div class="mt-5 space-y-2"><div class="h-2 rounded bg-white/70"></div><div class="h-2 w-2/3 rounded bg-white/50"></div></div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths23-lav: #e8def0;
  --color-ths23-lav: oklch(0.914 0.026 310.4);
  --color-ths23-blush: #fde0e4;
  --color-ths23-blush: oklch(0.932 0.032 8.3);
  --color-ths23-sky: #d8e8f0;
  --color-ths23-sky: oklch(0.921 0.02 229.1);
  --color-ths23-steel: #94b4d4;
  --color-ths23-steel: oklch(0.757 0.058 248.6);
  --color-ths23-ink: #3a2a55;
  --color-ths23-ink: oklch(0.325 0.076 299.3);
  --color-ths23-body: #574873;
  --color-ths23-body: oklch(0.435 0.071 299.5);
  --color-ths23-violet: #9a5cc0;
  --color-ths23-violet: oklch(0.586 0.158 311.1);
  --color-ths23-rose: #ee7fa6;
  --color-ths23-rose: oklch(0.731 0.142 358.9);
  --color-ths23-star: #e0a21c;
  --color-ths23-star: oklch(0.752 0.15 79.8);
  --font-ths23-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-23 {
  width: 100%;
  min-height: 100svh;
}
```
