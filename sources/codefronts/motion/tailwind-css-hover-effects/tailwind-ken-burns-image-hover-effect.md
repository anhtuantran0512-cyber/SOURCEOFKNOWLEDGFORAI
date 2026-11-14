---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-ken-burns-image-hover-effect/"
title: "Tailwind Ken Burns Image Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Six documentary-style slow zoom and pan presets that run only while hovered."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Ken Burns Image Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-ken-burns-image-hover-effect/

Six documentary-style slow zoom and pan presets that run only while hovered. Each animation is paused at rest and resumed on hover — animation-play-state has no utility, so it rides as an arbitrary property, which is exactly the right call.
## HTML
```html
<section class="thv-23 w-full min-h-svh bg-thv23-bg font-thv23-sans px-8 py-10">
  <p class="text-center text-[0.78rem] tracking-[0.12em] uppercase text-thv23-dim mb-8">Ken Burns Hover — 6 Presets</p>
  <div class="grid grid-cols-[repeat(auto-fit,minmax(230px,1fr))] gap-5 max-w-[860px] mx-auto">
    <figure class="group relative m-0 aspect-[3/2] overflow-hidden rounded-xl shadow-[0_4px_20px_rgba(0,0,0,.5)] cursor-pointer">
      <img src="https://picsum.photos/seed/kb1/400/260" alt="Coastline at dawn" class="block w-full h-full object-cover animate-thv23-zoom-in [animation-play-state:paused] group-hover:[animation-play-state:running] motion-reduce:[animation-play-state:paused]!">
      <figcaption class="absolute bottom-2.5 left-2.5 px-2 py-1 rounded bg-black/65 backdrop-blur-[4px] text-[0.7rem] tracking-[0.08em] text-white pointer-events-none">Zoom In</figcaption>
    </figure>
    <figure class="group relative m-0 aspect-[3/2] overflow-hidden rounded-xl shadow-[0_4px_20px_rgba(0,0,0,.5)] cursor-pointer">
      <img src="https://picsum.photos/seed/kb2/400/260" alt="Mountain ridge" class="block w-full h-full object-cover animate-thv23-zoom-out [animation-play-state:paused] group-hover:[animation-play-state:running] motion-reduce:[animation-play-state:paused]!">
      <figcaption class="absolute bottom-2.5 left-2.5 px-2 py-1 rounded bg-black/65 backdrop-blur-[4px] text-[0.7rem] tracking-[0.08em] text-white pointer-events-none">Zoom Out</figcaption>
    </figure>
    <figure class="group relative m-0 aspect-[3/2] overflow-hidden rounded-xl shadow-[0_4px_20px_rgba(0,0,0,.5)] cursor-pointer">
      <img src="https://picsum.photos/seed/kb3/400/260" alt="City skyline" class="block w-full h-full object-cover animate-thv23-pan-right [animation-play-state:paused] group-hover:[animation-play-state:running] motion-reduce:[animation-play-state:paused]!">
      <figcaption class="absolute bottom-2.5 left-2.5 px-2 py-1 rounded bg-black/65 backdrop-blur-[4px] text-[0.7rem] tracking-[0.08em] text-white pointer-events-none">Pan Right</figcaption>
    </figure>
    <figure class="group relative m-0 aspect-[3/2] overflow-hidden rounded-xl shadow-[0_4px_20px_rgba(0,0,0,.5)] cursor-pointer">
      <img src="https://picsum.photos/seed/kb4/400/260" alt="Forest path" class="block w-full h-full object-cover animate-thv23-pan-left [animation-play-state:paused] group-hover:[animation-play-state:running] motion-reduce:[animation-play-state:paused]!">
      <figcaption class="absolute bottom-2.5 left-2.5 px-2 py-1 rounded bg-black/65 backdrop-blur-[4px] text-[0.7rem] tracking-[0.08em] text-white pointer-events-none">Pan Left</figcaption>
    </figure>
    <figure class="group relative m-0 aspect-[3/2] overflow-hidden rounded-xl shadow-[0_4px_20px_rgba(0,0,0,.5)] cursor-pointer">
      <img src="https://picsum.photos/seed/kb5/400/260" alt="Desert dunes" class="block w-full h-full object-cover animate-thv23-drift-up [animation-play-state:paused] group-hover:[animation-play-state:running] motion-reduce:[animation-play-state:paused]!">
      <figcaption class="absolute bottom-2.5 left-2.5 px-2 py-1 rounded bg-black/65 backdrop-blur-[4px] text-[0.7rem] tracking-[0.08em] text-white pointer-events-none">Drift Up</figcaption>
    </figure>
    <figure class="group relative m-0 aspect-[3/2] overflow-hidden rounded-xl shadow-[0_4px_20px_rgba(0,0,0,.5)] cursor-pointer">
      <img src="https://picsum.photos/seed/kb6/400/260" alt="Harbour at night" class="block w-full h-full object-cover animate-thv23-diagonal [animation-play-state:paused] group-hover:[animation-play-state:running] motion-reduce:[animation-play-state:paused]!">
      <figcaption class="absolute bottom-2.5 left-2.5 px-2 py-1 rounded bg-black/65 backdrop-blur-[4px] text-[0.7rem] tracking-[0.08em] text-white pointer-events-none">Diagonal</figcaption>
    </figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv23-bg: #0d0d0d;
  --color-thv23-bg: oklch(0.14 0 0);
  --color-thv23-dim: #9a9a9a;
  --color-thv23-dim: oklch(0.68 0 0);
  --font-thv23-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-thv23-zoom-in: thv23-zoom-in 6s cubic-bezier(.25,.46,.45,.94) both;
  --animate-thv23-zoom-out: thv23-zoom-out 6s cubic-bezier(.25,.46,.45,.94) both;
  --animate-thv23-pan-right: thv23-pan-right 6s cubic-bezier(.25,.46,.45,.94) both;
  --animate-thv23-pan-left: thv23-pan-left 6s cubic-bezier(.25,.46,.45,.94) both;
  --animate-thv23-drift-up: thv23-drift-up 6s cubic-bezier(.25,.46,.45,.94) both;
  --animate-thv23-diagonal: thv23-diagonal 6s cubic-bezier(.25,.46,.45,.94) both;
}

.thv-23 {
  width: 100%;
  min-height: 100svh;
}

.thv-23 ::selection {
  background: #ffffff;
  color: #000;
}

@keyframes thv23-zoom-in {
  from {
    transform: scale(1) translate(0,0);
  }

  to {
    transform: scale(1.18) translate(-2%,-2%);
  }
}

@keyframes thv23-zoom-out {
  from {
    transform: scale(1.2) translate(-3%,-3%);
  }

  to {
    transform: scale(1) translate(0,0);
  }
}

@keyframes thv23-pan-right {
  from {
    transform: scale(1.14) translate(-5%,0);
  }

  to {
    transform: scale(1.14) translate(5%,0);
  }
}

@keyframes thv23-pan-left {
  from {
    transform: scale(1.14) translate(5%,0);
  }

  to {
    transform: scale(1.14) translate(-5%,0);
  }
}

@keyframes thv23-drift-up {
  from {
    transform: scale(1.14) translate(0,5%);
  }

  to {
    transform: scale(1.14) translate(0,-5%);
  }
}

@keyframes thv23-diagonal {
  from {
    transform: scale(1) translate(0,0);
  }

  to {
    transform: scale(1.2) translate(-4%,-4%);
  }
}
```
