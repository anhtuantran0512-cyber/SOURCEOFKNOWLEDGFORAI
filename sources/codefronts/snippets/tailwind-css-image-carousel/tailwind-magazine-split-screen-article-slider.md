---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-magazine-split-screen-article-slider/"
title: "Tailwind Magazine Split-Screen Article Slider"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "A featured-article slider split down the middle: photograph on one side, headline and excerpt on the other, stacking to one column on mobile."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Magazine Split-Screen Article Slider
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-magazine-split-screen-article-slider/

A featured-article slider split down the middle: photograph on one side, headline and excerpt on the other, stacking to one column on mobile. The layout is a two-column grid; the state is one :has() condition per story.
## HTML
```html
<section class="tcar-10 w-full min-h-svh grid place-items-center bg-tcar10-bg font-tcar10-serif px-5 py-10" aria-label="Featured articles">
  <div class="group w-[min(880px,100%)]">
    <input type="radio" name="tcar-10" id="tcar-10-1" class="sr-only" checked>
    <input type="radio" name="tcar-10" id="tcar-10-2" class="sr-only">
    <input type="radio" name="tcar-10" id="tcar-10-3" class="sr-only">
    <div class="relative bg-white border border-tcar10-edge rounded-md overflow-hidden shadow-[0_24px_50px_-34px_oklch(0.4_0.06_60/0.6)] sm:min-h-[340px]">
      <article class="hidden sm:grid sm:absolute sm:inset-0 grid-cols-1 sm:grid-cols-[1.1fr_1fr] opacity-0 pointer-events-none transition-opacity duration-500 group-has-[#tcar-10-1:checked]:grid group-has-[#tcar-10-1:checked]:opacity-100 group-has-[#tcar-10-1:checked]:pointer-events-auto motion-reduce:transition-none">
        <div class="overflow-hidden bg-tcar10-ph max-sm:aspect-[16/10]"><img src="https://picsum.photos/seed/mag-1/900/700" width="900" height="700" decoding="async" alt="Aerial view of a coastal city" class="size-full object-cover block"></div>
        <div class="p-[clamp(22px,4vw,44px)] flex flex-col justify-center">
          <span class="font-tcar10-sans text-[11px] tracking-[0.18em] uppercase text-tcar10-acc font-bold mb-3">City Guide</span>
          <h3 class="text-[clamp(22px,3.4vw,30px)] leading-[1.16] text-tcar10-ink mb-3.5 text-balance">48 hours in Lisbon, off the tourist trail</h3>
          <p class="text-[15px] leading-relaxed text-tcar10-mute mb-5">Where locals actually eat, drink and swim &mdash; a slower map of the city's seven hills.</p>
          <a href="#" class="font-tcar10-sans text-[13px] font-bold text-tcar10-ink no-underline border-b-2 border-tcar10-acc self-start pb-0.5 focus-visible:outline-2 focus-visible:outline-tcar10-acc focus-visible:outline-offset-4">Read story &rarr;</a>
        </div>
      </article>
      <article class="hidden sm:grid sm:absolute sm:inset-0 grid-cols-1 sm:grid-cols-[1.1fr_1fr] opacity-0 pointer-events-none transition-opacity duration-500 group-has-[#tcar-10-2:checked]:grid group-has-[#tcar-10-2:checked]:opacity-100 group-has-[#tcar-10-2:checked]:pointer-events-auto motion-reduce:transition-none">
        <div class="overflow-hidden bg-tcar10-ph max-sm:aspect-[16/10]"><img src="https://picsum.photos/seed/mag-2/900/700" width="900" height="700" loading="lazy" decoding="async" alt="Studio workspace with plants" class="size-full object-cover block"></div>
        <div class="p-[clamp(22px,4vw,44px)] flex flex-col justify-center">
          <span class="font-tcar10-sans text-[11px] tracking-[0.18em] uppercase text-tcar10-acc font-bold mb-3">Workspaces</span>
          <h3 class="text-[clamp(22px,3.4vw,30px)] leading-[1.16] text-tcar10-ink mb-3.5 text-balance">The quiet rise of the two-hour workday</h3>
          <p class="text-[15px] leading-relaxed text-tcar10-mute mb-5">Deep-work rituals from designers who ship more by doing less, on purpose.</p>
          <a href="#" class="font-tcar10-sans text-[13px] font-bold text-tcar10-ink no-underline border-b-2 border-tcar10-acc self-start pb-0.5 focus-visible:outline-2 focus-visible:outline-tcar10-acc focus-visible:outline-offset-4">Read story &rarr;</a>
        </div>
      </article>
      <article class="hidden sm:grid sm:absolute sm:inset-0 grid-cols-1 sm:grid-cols-[1.1fr_1fr] opacity-0 pointer-events-none transition-opacity duration-500 group-has-[#tcar-10-3:checked]:grid group-has-[#tcar-10-3:checked]:opacity-100 group-has-[#tcar-10-3:checked]:pointer-events-auto motion-reduce:transition-none">
        <div class="overflow-hidden bg-tcar10-ph max-sm:aspect-[16/10]"><img src="https://picsum.photos/seed/mag-3/900/700" width="900" height="700" loading="lazy" decoding="async" alt="Close-up of ceramic bowls" class="size-full object-cover block"></div>
        <div class="p-[clamp(22px,4vw,44px)] flex flex-col justify-center">
          <span class="font-tcar10-sans text-[11px] tracking-[0.18em] uppercase text-tcar10-acc font-bold mb-3">Craft</span>
          <h3 class="text-[clamp(22px,3.4vw,30px)] leading-[1.16] text-tcar10-ink mb-3.5 text-balance">Why handmade ceramics are having a moment</h3>
          <p class="text-[15px] leading-relaxed text-tcar10-mute mb-5">A generation trading screens for clay, and the studios teaching them how.</p>
          <a href="#" class="font-tcar10-sans text-[13px] font-bold text-tcar10-ink no-underline border-b-2 border-tcar10-acc self-start pb-0.5 focus-visible:outline-2 focus-visible:outline-tcar10-acc focus-visible:outline-offset-4">Read story &rarr;</a>
        </div>
      </article>
    </div>
    <div class="flex justify-center mt-2">
      <label for="tcar-10-1" aria-label="Story 1" class="group/dot size-11 grid place-items-center cursor-pointer"><span class="size-[11px] rounded-full bg-tcar10-dot transition-[scale,background-color] duration-200 group-hover/dot:bg-tcar10-dothover group-has-[#tcar-10-1:checked]:bg-tcar10-acc group-has-[#tcar-10-1:checked]:scale-[1.3] group-has-[#tcar-10-1:focus-visible]:outline-3 group-has-[#tcar-10-1:focus-visible]:outline-tcar10-acc group-has-[#tcar-10-1:focus-visible]:outline-offset-[3px] motion-reduce:transition-none"></span></label>
      <label for="tcar-10-2" aria-label="Story 2" class="group/dot size-11 grid place-items-center cursor-pointer"><span class="size-[11px] rounded-full bg-tcar10-dot transition-[scale,background-color] duration-200 group-hover/dot:bg-tcar10-dothover group-has-[#tcar-10-2:checked]:bg-tcar10-acc group-has-[#tcar-10-2:checked]:scale-[1.3] group-has-[#tcar-10-2:focus-visible]:outline-3 group-has-[#tcar-10-2:focus-visible]:outline-tcar10-acc group-has-[#tcar-10-2:focus-visible]:outline-offset-[3px] motion-reduce:transition-none"></span></label>
      <label for="tcar-10-3" aria-label="Story 3" class="group/dot size-11 grid place-items-center cursor-pointer"><span class="size-[11px] rounded-full bg-tcar10-dot transition-[scale,background-color] duration-200 group-hover/dot:bg-tcar10-dothover group-has-[#tcar-10-3:checked]:bg-tcar10-acc group-has-[#tcar-10-3:checked]:scale-[1.3] group-has-[#tcar-10-3:focus-visible]:outline-3 group-has-[#tcar-10-3:focus-visible]:outline-tcar10-acc group-has-[#tcar-10-3:focus-visible]:outline-offset-[3px] motion-reduce:transition-none"></span></label>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar10-bg: #f7f3ec;
  --color-tcar10-bg: oklch(0.96 0.012 80);
  --color-tcar10-edge: #e6ddce;
  --color-tcar10-edge: oklch(0.9 0.018 80);
  --color-tcar10-ph: #e9e0d0;
  --color-tcar10-ph: oklch(0.91 0.02 80);
  --color-tcar10-ink: #241d15;
  --color-tcar10-ink: oklch(0.24 0.018 60);
  --color-tcar10-mute: #5c5040;
  --color-tcar10-mute: oklch(0.45 0.022 70);
  --color-tcar10-dot: #d8ccb8;
  --color-tcar10-dot: oklch(0.86 0.025 80);
  --color-tcar10-dothover: #b7a68b;
  --color-tcar10-dothover: oklch(0.73 0.035 80);
  --color-tcar10-acc: #a8362a;
  --color-tcar10-acc: oklch(0.48 0.16 28);
  --font-tcar10-serif: 'Newsreader', Georgia, serif;
  --font-tcar10-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tcar-10 {
  width: 100%;
  min-height: 100svh;
}

.tcar-10 ::selection {
  background: var(--color-tcar10-acc);
  color: #fff;
}
```
