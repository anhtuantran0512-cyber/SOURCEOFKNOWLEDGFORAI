---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-infinite-logo-scroller-marquee-no-javascript/"
title: "Tailwind Infinite Logo Scroller Marquee with No JavaScript"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "A seamless, endlessly looping strip of partner logos — the 'trusted by' band on almost every SaaS landing page."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Infinite Logo Scroller Marquee with No JavaScript
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-infinite-logo-scroller-marquee-no-javascript/

A seamless, endlessly looping strip of partner logos — the 'trusted by' band on almost every SaaS landing page. The port's lesson: --animate-* in @theme mints animate-tcar03-scroll, so the animation becomes a design token like any colour.
## HTML
```html
<section class="tcar-03 w-full min-h-svh flex flex-col items-center justify-center gap-6 bg-tcar03-bg font-tcar03-sans py-10" aria-label="Trusted by leading teams">
  <p class="text-xs tracking-[0.16em] uppercase text-tcar03-mute m-0">Trusted by 4,000+ teams</p>
  <div class="group w-[min(720px,100%)] overflow-hidden [mask-image:linear-gradient(90deg,transparent,#000_12%,#000_88%,transparent)]">
    <ul class="list-none flex items-center gap-16 w-max m-0 p-0 animate-tcar03-scroll group-hover:[animation-play-state:paused] group-focus-within:[animation-play-state:paused] motion-reduce:animate-none motion-reduce:flex-wrap motion-reduce:justify-center motion-reduce:w-auto motion-reduce:gap-x-12 motion-reduce:gap-y-8">
      <li class="flex-none text-[22px] font-bold tracking-[0.02em] text-tcar03-logo whitespace-nowrap font-tcar03-serif opacity-75">NORTHWIND</li>
      <li class="flex-none text-[22px] font-bold tracking-[0.02em] text-tcar03-logo whitespace-nowrap font-tcar03-serif opacity-75">Lumen&amp;Co</li>
      <li class="flex-none text-[22px] font-bold tracking-[0.02em] text-tcar03-logo whitespace-nowrap font-tcar03-serif opacity-75">ARCADIA</li>
      <li class="flex-none text-[22px] font-bold tracking-[0.02em] text-tcar03-logo whitespace-nowrap font-tcar03-serif opacity-75">F&ouml;hn</li>
      <li class="flex-none text-[22px] font-bold tracking-[0.02em] text-tcar03-logo whitespace-nowrap font-tcar03-serif opacity-75">Kestrel</li>
      <li class="flex-none text-[22px] font-bold tracking-[0.02em] text-tcar03-logo whitespace-nowrap font-tcar03-serif opacity-75">MONOLITH</li>
      <li aria-hidden="true" class="flex-none text-[22px] font-bold tracking-[0.02em] text-tcar03-logo whitespace-nowrap font-tcar03-serif opacity-75">NORTHWIND</li>
      <li aria-hidden="true" class="flex-none text-[22px] font-bold tracking-[0.02em] text-tcar03-logo whitespace-nowrap font-tcar03-serif opacity-75">Lumen&amp;Co</li>
      <li aria-hidden="true" class="flex-none text-[22px] font-bold tracking-[0.02em] text-tcar03-logo whitespace-nowrap font-tcar03-serif opacity-75">ARCADIA</li>
      <li aria-hidden="true" class="flex-none text-[22px] font-bold tracking-[0.02em] text-tcar03-logo whitespace-nowrap font-tcar03-serif opacity-75">F&ouml;hn</li>
      <li aria-hidden="true" class="flex-none text-[22px] font-bold tracking-[0.02em] text-tcar03-logo whitespace-nowrap font-tcar03-serif opacity-75">Kestrel</li>
      <li aria-hidden="true" class="flex-none text-[22px] font-bold tracking-[0.02em] text-tcar03-logo whitespace-nowrap font-tcar03-serif opacity-75">MONOLITH</li>
    </ul>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar03-bg: #f6f7f9;
  --color-tcar03-bg: oklch(0.97 0.003 255);
  --color-tcar03-mute: #8a93a3;
  --color-tcar03-mute: oklch(0.65 0.02 255);
  --color-tcar03-logo: #3e4654;
  --color-tcar03-logo: oklch(0.42 0.02 255);
  --font-tcar03-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcar03-serif: 'Newsreader', Georgia, serif;
  --animate-tcar03-scroll: tcar03-scroll 24s linear infinite;
}
/* Keyframes have no utility form and never will. */

@keyframes tcar03-scroll {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(-50%);
  }
}

.tcar-03 {
  width: 100%;
  min-height: 100svh;
}

.tcar-03 ::selection {
  background: #111827;
  color: #fff;
}
/* Safari < 15.4 mask prefix. */

.tcar-03 .group {
  -webkit-mask: linear-gradient(90deg, transparent, #000 12%, #000 88%, transparent);
}
```
