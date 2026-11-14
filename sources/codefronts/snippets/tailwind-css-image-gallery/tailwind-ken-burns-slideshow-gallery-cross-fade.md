---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-ken-burns-slideshow-gallery-cross-fade/"
title: "Tailwind Ken Burns Slideshow Gallery with Staggered Cross-Fade"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "A cinematic auto-playing slideshow where each image slowly zooms and pans while cross-fading to the next."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Ken Burns Slideshow Gallery with Staggered Cross-Fade
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-ken-burns-slideshow-gallery-cross-fade/

A cinematic auto-playing slideshow where each image slowly zooms and pans while cross-fading to the next. Two animations per slide — one for the fade, one for the pan — both minted as @theme utilities, staggered by four [animation-delay:...] values.
## HTML
```html
<section class="tgl-20 w-full min-h-svh grid place-items-center bg-tgl20-bg font-tgl20-sans px-5 py-10" aria-label="Ken Burns slideshow" aria-roledescription="carousel">
  <div class="relative w-[min(920px,100%)] [aspect-ratio:12/7] rounded-2xl overflow-hidden shadow-[0_40px_80px_-40px_rgba(0,0,0,0.9)]">
    <figure class="absolute inset-0 m-0 opacity-0 animate-tgl20-fade [animation-delay:0s] motion-reduce:animate-none motion-reduce:opacity-100">
      <img src="https://images.unsplash.com/photo-1418985991508-e47386d96a71?q=80&w=1200&h=700&auto=format&fit=crop" alt="Sweeping mountain vista" loading="lazy" decoding="async" class="w-full h-full object-cover origin-center animate-tgl20-kb [animation-delay:0s] motion-reduce:animate-none motion-reduce:scale-105">
      <figcaption class="absolute inset-x-0 bottom-0 px-8 py-7 w-full text-white font-tgl20-serif text-[26px] font-bold tracking-[-0.01em] bg-[linear-gradient(0deg,rgba(0,0,0,0.65),transparent)]">The High Passes</figcaption>
    </figure>
    <figure class="absolute inset-0 m-0 opacity-0 animate-tgl20-fade [animation-delay:6s] motion-reduce:animate-none">
      <img src="https://images.unsplash.com/photo-1517701550927-30cf4ba1dba5?q=80&w=1200&h=700&auto=format&fit=crop" alt="Open ocean at golden hour" loading="lazy" decoding="async" class="w-full h-full object-cover origin-center animate-tgl20-kb [animation-delay:6s] motion-reduce:animate-none">
      <figcaption class="absolute inset-x-0 bottom-0 px-8 py-7 w-full text-white font-tgl20-serif text-[26px] font-bold tracking-[-0.01em] bg-[linear-gradient(0deg,rgba(0,0,0,0.65),transparent)]">Endless Blue</figcaption>
    </figure>
    <figure class="absolute inset-0 m-0 opacity-0 animate-tgl20-fade [animation-delay:12s] motion-reduce:animate-none">
      <img src="https://images.unsplash.com/photo-1517180102446-f3ece451e9d8?q=80&w=1200&h=700&auto=format&fit=crop" alt="Desert at dusk" loading="lazy" decoding="async" class="w-full h-full object-cover origin-center animate-tgl20-kb [animation-delay:12s] motion-reduce:animate-none">
      <figcaption class="absolute inset-x-0 bottom-0 px-8 py-7 w-full text-white font-tgl20-serif text-[26px] font-bold tracking-[-0.01em] bg-[linear-gradient(0deg,rgba(0,0,0,0.65),transparent)]">The Dry Lands</figcaption>
    </figure>
    <figure class="absolute inset-0 m-0 opacity-0 animate-tgl20-fade [animation-delay:18s] motion-reduce:animate-none">
      <img src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?q=80&w=1200&h=700&auto=format&fit=crop" alt="Ancient forest interior" loading="lazy" decoding="async" class="w-full h-full object-cover origin-center animate-tgl20-kb [animation-delay:18s] motion-reduce:animate-none">
      <figcaption class="absolute inset-x-0 bottom-0 px-8 py-7 w-full text-white font-tgl20-serif text-[26px] font-bold tracking-[-0.01em] bg-[linear-gradient(0deg,rgba(0,0,0,0.65),transparent)]">Old Growth</figcaption>
    </figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl20-bg: #0a0a0c;
  --color-tgl20-bg: oklch(0.13 0.004 280);
  --color-tgl20-acc: #d9a441;
  --color-tgl20-acc: oklch(0.76 0.12 75);
  --font-tgl20-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tgl20-serif: 'Playfair Display', Georgia, serif;
  --animate-tgl20-fade: tgl20-fade 24s infinite;
  --animate-tgl20-kb: tgl20-kb 24s infinite;
}

@keyframes tgl20-fade {
  0% {
    opacity: 0;
  }

  2% {
    opacity: 1;
  }

  23% {
    opacity: 1;
  }

  27% {
    opacity: 0;
  }

  100% {
    opacity: 0;
  }
}

@keyframes tgl20-kb {
  0% {
    transform: scale(1) translate(0, 0);
  }

  27% {
    transform: scale(1.18) translate(-3%, 2%);
  }

  100% {
    transform: scale(1.18) translate(-3%, 2%);
  }
}

.tgl-20 {
  width: 100%;
  min-height: 100svh;
}

.tgl-20 ::selection {
  background: var(--color-tgl20-acc);
  color: #111;
}
```
