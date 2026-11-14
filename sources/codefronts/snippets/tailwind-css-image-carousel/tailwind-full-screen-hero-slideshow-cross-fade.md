---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-full-screen-hero-slideshow-cross-fade/"
title: "Tailwind Full-Screen Hero Slideshow with Auto Cross-Fade"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "A high-impact auto-advancing hero that cross-fades full-bleed photography under a headline."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Full-Screen Hero Slideshow with Auto Cross-Fade
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-full-screen-hero-slideshow-cross-fade/

A high-impact auto-advancing hero that cross-fades full-bleed photography under a headline. One shared keyframe plus a negative animation-delay per slide is the entire timeline — no setInterval to leak, desync or keep alive in a background tab.
## HTML
```html
<section class="tcar-05 w-full min-h-svh font-tcar05-sans" aria-label="Featured highlights slideshow" aria-roledescription="carousel">
  <div class="group relative h-svh min-h-[520px] overflow-hidden bg-tcar05-ink">
    <div class="absolute inset-0 opacity-0 animate-tcar05-fade group-hover:[animation-play-state:paused] group-focus-within:[animation-play-state:paused] motion-reduce:animate-none motion-reduce:opacity-100">
      <img src="https://picsum.photos/seed/hero-peaks/1600/900" width="1600" height="900" fetchpriority="high" decoding="async" alt="Mist over mountain peaks at dawn" class="size-full object-cover block">
    </div>
    <div class="absolute inset-0 opacity-0 animate-tcar05-fade [animation-delay:-5s] group-hover:[animation-play-state:paused] group-focus-within:[animation-play-state:paused] motion-reduce:animate-none">
      <img src="https://picsum.photos/seed/hero-coast/1600/900" width="1600" height="900" loading="lazy" decoding="async" alt="Rugged coastline at golden hour" class="size-full object-cover block">
    </div>
    <div class="absolute inset-0 opacity-0 animate-tcar05-fade [animation-delay:-10s] group-hover:[animation-play-state:paused] group-focus-within:[animation-play-state:paused] motion-reduce:animate-none">
      <img src="https://picsum.photos/seed/hero-forest/1600/900" width="1600" height="900" loading="lazy" decoding="async" alt="Sun beams through a pine forest" class="size-full object-cover block">
    </div>
    <div aria-hidden="true" class="absolute inset-0 z-[1] bg-[linear-gradient(90deg,oklch(0.15_0.01_265/0.82),oklch(0.15_0.01_265/0.25)_60%,transparent)]"></div>
    <div class="absolute left-0 bottom-0 z-[2] p-[clamp(28px,6vw,72px)] max-w-[640px] text-white">
      <p class="text-[13px] tracking-[0.24em] uppercase mb-3.5 m-0">New Season</p>
      <h2 class="text-[clamp(38px,7vw,72px)] leading-[1.02] font-black tracking-[-0.02em] m-0 [text-shadow:0_2px_30px_oklch(0_0_0/0.45)]">Go further,<br>pack lighter</h2>
      <a href="#" class="inline-flex items-center min-h-11 mt-6 px-7 rounded-full bg-white text-tcar05-ink font-bold text-sm no-underline transition-[translate,box-shadow] duration-200 hover:-translate-y-0.5 hover:shadow-[0_14px_30px_-14px_oklch(0_0_0/0.6)] focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">Explore the collection</a>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar05-ink: #0d0f12;
  --color-tcar05-ink: oklch(0.16 0.008 265);
  --font-tcar05-sans: 'Archivo', system-ui, sans-serif;
  --animate-tcar05-fade: tcar05-fade 15s ease-in-out infinite;
}

@keyframes tcar05-fade {
  0% {
    opacity: 0;
  }

  5% {
    opacity: 1;
  }

  28% {
    opacity: 1;
  }

  33% {
    opacity: 0;
  }

  100% {
    opacity: 0;
  }
}

.tcar-05 {
  width: 100%;
  min-height: 100svh;
}

.tcar-05 ::selection {
  background: #fff;
  color: #111;
}
```
