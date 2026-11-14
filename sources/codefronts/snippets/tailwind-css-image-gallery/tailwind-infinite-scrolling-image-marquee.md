---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-infinite-scrolling-image-marquee/"
title: "Tailwind Infinite Scrolling Image Marquee with Seamless Loop"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "A banner of images that scrolls forever with no visible seam or reset, pausing when you hover it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Infinite Scrolling Image Marquee with Seamless Loop
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-infinite-scrolling-image-marquee/

A banner of images that scrolls forever with no visible seam or reset, pausing when you hover it. The loop is the oldest trick in the book — duplicate the set, translate &minus;50% — and Tailwind turns it into one @theme animation plus one mask.
## HTML
```html
<section class="tgl-19 w-full min-h-svh grid place-items-center bg-tgl19-bg font-tgl19-sans py-10" aria-label="Infinite scrolling image strip">
  <div class="group w-full overflow-hidden [mask-image:linear-gradient(90deg,transparent,#000_12%,#000_88%,transparent)]">
    <div class="flex gap-4 w-max animate-tgl19-marquee group-hover:[animation-play-state:paused] motion-reduce:animate-none">
      <img src="https://images.unsplash.com/photo-1449157291145-7efd050a4d0e?q=80&w=300&h=300&auto=format&fit=crop" alt="Concrete facade in monochrome" loading="lazy" decoding="async" class="block w-[220px] h-[220px] flex-[0_0_auto] object-cover rounded-xl grayscale contrast-[1.05] transition-[filter] duration-[400ms] hover:grayscale-0 motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=300&h=300&auto=format&fit=crop" alt="City block from above" loading="lazy" decoding="async" class="block w-[220px] h-[220px] flex-[0_0_auto] object-cover rounded-xl grayscale contrast-[1.05] transition-[filter] duration-[400ms] hover:grayscale-0 motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=300&h=300&auto=format&fit=crop" alt="Bare trees in winter" loading="lazy" decoding="async" class="block w-[220px] h-[220px] flex-[0_0_auto] object-cover rounded-xl grayscale contrast-[1.05] transition-[filter] duration-[400ms] hover:grayscale-0 motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1633356122544-f134324a6cee?q=80&w=300&h=300&auto=format&fit=crop" alt="Portrait in hard light" loading="lazy" decoding="async" class="block w-[220px] h-[220px] flex-[0_0_auto] object-cover rounded-xl grayscale contrast-[1.05] transition-[filter] duration-[400ms] hover:grayscale-0 motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1531891437562-4301cf35b7e4?q=80&w=300&h=300&auto=format&fit=crop" alt="Crossing in the rain" loading="lazy" decoding="async" class="block w-[220px] h-[220px] flex-[0_0_auto] object-cover rounded-xl grayscale contrast-[1.05] transition-[filter] duration-[400ms] hover:grayscale-0 motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=300&h=300&auto=format&fit=crop" alt="Ridge line against cloud" loading="lazy" decoding="async" class="block w-[220px] h-[220px] flex-[0_0_auto] object-cover rounded-xl grayscale contrast-[1.05] transition-[filter] duration-[400ms] hover:grayscale-0 motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1449157291145-7efd050a4d0e?q=80&w=300&h=300&auto=format&fit=crop" alt="" aria-hidden="true" loading="lazy" decoding="async" class="block w-[220px] h-[220px] flex-[0_0_auto] object-cover rounded-xl grayscale contrast-[1.05]">
      <img src="https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=300&h=300&auto=format&fit=crop" alt="" aria-hidden="true" loading="lazy" decoding="async" class="block w-[220px] h-[220px] flex-[0_0_auto] object-cover rounded-xl grayscale contrast-[1.05]">
      <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=300&h=300&auto=format&fit=crop" alt="" aria-hidden="true" loading="lazy" decoding="async" class="block w-[220px] h-[220px] flex-[0_0_auto] object-cover rounded-xl grayscale contrast-[1.05]">
      <img src="https://images.unsplash.com/photo-1633356122544-f134324a6cee?q=80&w=300&h=300&auto=format&fit=crop" alt="" aria-hidden="true" loading="lazy" decoding="async" class="block w-[220px] h-[220px] flex-[0_0_auto] object-cover rounded-xl grayscale contrast-[1.05]">
      <img src="https://images.unsplash.com/photo-1531891437562-4301cf35b7e4?q=80&w=300&h=300&auto=format&fit=crop" alt="" aria-hidden="true" loading="lazy" decoding="async" class="block w-[220px] h-[220px] flex-[0_0_auto] object-cover rounded-xl grayscale contrast-[1.05]">
      <img src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=300&h=300&auto=format&fit=crop" alt="" aria-hidden="true" loading="lazy" decoding="async" class="block w-[220px] h-[220px] flex-[0_0_auto] object-cover rounded-xl grayscale contrast-[1.05]">
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl19-bg: #0f0f0f;
  --color-tgl19-bg: oklch(0.16 0 0);
  --color-tgl19-acc: #e08a4a;
  --color-tgl19-acc: oklch(0.72 0.13 50);
  --font-tgl19-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tgl19-marquee: tgl19-marquee 30s linear infinite;
}

@keyframes tgl19-marquee {
  to {
    transform: translateX(-50%);
  }
}

.tgl-19 {
  width: 100%;
  min-height: 100svh;
}
/* Older WebKit mask prefix. */

.tgl-19 > div {
  -webkit-mask-image: linear-gradient(90deg, transparent, #000 12%, #000 88%, transparent);
}

.tgl-19 ::selection {
  background: var(--color-tgl19-acc);
  color: #111;
}
```
