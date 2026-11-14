---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-image-tilt-depth-hover-effect/"
title: "Tailwind Image Tilt Depth Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Four photo cards that lean in 3D, each with a conic specular sheen and a caption that rises on hover."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Image Tilt Depth Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-image-tilt-depth-hover-effect/

Four photo cards that lean in 3D, each with a conic specular sheen and a caption that rises on hover. The shadow direction is matched to the lean on every variant, which is what sells the depth.
## HTML
```html
<section class="thv-24 w-full min-h-svh bg-thv24-bg font-thv24-sans px-8 py-12">
  <p class="text-center text-[0.75rem] tracking-[0.14em] uppercase text-thv24-dim mb-10">Image Tilt Depth — 4 Variants</p>
  <div class="flex flex-wrap justify-center items-start gap-10">
    <a href="#" class="group perspective-[700px] block rounded-xl no-underline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv24-acc">
      <span class="relative block w-[220px] aspect-[3/4] overflow-hidden rounded-xl transform-3d shadow-[0_8px_30px_rgba(0,0,0,.55)] transition-[transform,box-shadow] duration-450 ease-[cubic-bezier(.23,1,.32,1)] group-hover:rotate-y-[12deg] group-hover:rotate-x-[-6deg] group-hover:shadow-[-14px_18px_50px_rgba(0,0,0,.7)] group-focus-visible:rotate-y-[12deg] group-focus-visible:rotate-x-[-6deg] motion-reduce:transition-none motion-reduce:group-hover:rotate-y-0 motion-reduce:group-hover:rotate-x-0">
        <img src="https://picsum.photos/seed/tilt1/300/400" alt="Portrait study in warm light" class="block w-full h-full object-cover">
        <span aria-hidden="true" class="absolute inset-0 rounded-[inherit] opacity-0 pointer-events-none transition-opacity duration-400 bg-[conic-gradient(from_135deg_at_50%_0%,rgba(255,255,255,.18)_0deg,transparent_80deg)] group-hover:opacity-100 group-focus-visible:opacity-100"></span>
        <span class="absolute inset-x-0 bottom-0 px-3.5 py-2.5 text-[0.78rem] tracking-[0.06em] text-white opacity-0 translate-y-1 transition-[opacity,transform] duration-350 bg-[linear-gradient(transparent,rgba(0,0,0,.75))] group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0">Portrait Tilt</span>
      </span>
    </a>
    <a href="#" class="group perspective-[700px] block rounded-xl no-underline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv24-acc">
      <span class="relative block w-[320px] max-w-full aspect-video overflow-hidden rounded-xl transform-3d shadow-[0_8px_30px_rgba(0,0,0,.55)] transition-[transform,box-shadow] duration-450 ease-[cubic-bezier(.23,1,.32,1)] group-hover:rotate-x-[10deg] group-hover:rotate-y-[-5deg] group-hover:shadow-[0_-14px_40px_rgba(0,0,0,.6)] group-focus-visible:rotate-x-[10deg] group-focus-visible:rotate-y-[-5deg] motion-reduce:transition-none motion-reduce:group-hover:rotate-x-0 motion-reduce:group-hover:rotate-y-0">
        <img src="https://picsum.photos/seed/tilt2/400/260" alt="Wide landscape at golden hour" class="block w-full h-full object-cover">
        <span aria-hidden="true" class="absolute inset-0 rounded-[inherit] opacity-0 pointer-events-none transition-opacity duration-400 bg-[conic-gradient(from_135deg_at_50%_0%,rgba(255,255,255,.18)_0deg,transparent_80deg)] group-hover:opacity-100 group-focus-visible:opacity-100"></span>
        <span class="absolute inset-x-0 bottom-0 px-3.5 py-2.5 text-[0.78rem] tracking-[0.06em] text-white opacity-0 translate-y-1 transition-[opacity,transform] duration-350 bg-[linear-gradient(transparent,rgba(0,0,0,.75))] group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0">Landscape Tilt</span>
      </span>
    </a>
    <a href="#" class="group perspective-[500px] block rounded-xl no-underline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv24-acc">
      <span class="relative block w-[220px] aspect-[3/4] overflow-hidden rounded-xl transform-3d shadow-[0_8px_30px_rgba(0,0,0,.55)] transition-[transform,box-shadow] duration-450 ease-[cubic-bezier(.23,1,.32,1)] group-hover:rotate-y-[-16deg] group-hover:rotate-x-[8deg] group-hover:shadow-[20px_14px_60px_rgba(0,0,0,.8)] group-focus-visible:rotate-y-[-16deg] group-focus-visible:rotate-x-[8deg] motion-reduce:transition-none motion-reduce:group-hover:rotate-y-0 motion-reduce:group-hover:rotate-x-0">
        <img src="https://picsum.photos/seed/tilt3/300/400" alt="Architectural detail in shadow" class="block w-full h-full object-cover">
        <span aria-hidden="true" class="absolute inset-0 rounded-[inherit] opacity-0 pointer-events-none transition-opacity duration-400 bg-[conic-gradient(from_135deg_at_50%_0%,rgba(255,255,255,.18)_0deg,transparent_80deg)] group-hover:opacity-100 group-focus-visible:opacity-100"></span>
        <span class="absolute inset-x-0 bottom-0 px-3.5 py-2.5 text-[0.78rem] tracking-[0.06em] text-white opacity-0 translate-y-1 transition-[opacity,transform] duration-350 bg-[linear-gradient(transparent,rgba(0,0,0,.75))] group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0">Deep Perspective</span>
      </span>
    </a>
    <a href="#" class="group perspective-[700px] block rounded-xl no-underline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv24-acc">
      <span class="relative block w-[320px] max-w-full aspect-video overflow-hidden rounded-xl transform-3d shadow-[0_8px_30px_rgba(0,0,0,.55)] transition-[transform,box-shadow] duration-450 ease-[cubic-bezier(.23,1,.32,1)] group-hover:rotate-x-[5deg] group-hover:rotate-y-[5deg] group-hover:translate-z-[12px] group-hover:shadow-[-8px_20px_50px_rgba(0,0,0,.65)] group-focus-visible:rotate-x-[5deg] group-focus-visible:rotate-y-[5deg] motion-reduce:transition-none motion-reduce:group-hover:rotate-x-0 motion-reduce:group-hover:rotate-y-0">
        <img src="https://picsum.photos/seed/tilt4/400/260" alt="Still life on a flat surface" class="block w-full h-full object-cover">
        <span aria-hidden="true" class="absolute inset-0 rounded-[inherit] opacity-0 pointer-events-none transition-opacity duration-400 bg-[conic-gradient(from_135deg_at_50%_0%,rgba(255,255,255,.18)_0deg,transparent_80deg)] group-hover:opacity-100 group-focus-visible:opacity-100"></span>
        <span class="absolute inset-x-0 bottom-0 px-3.5 py-2.5 text-[0.78rem] tracking-[0.06em] text-white opacity-0 translate-y-1 transition-[opacity,transform] duration-350 bg-[linear-gradient(transparent,rgba(0,0,0,.75))] group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0">Flat Hover Lift</span>
      </span>
    </a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv24-bg: #0e0e12;
  --color-thv24-bg: oklch(0.15 0.01 285);
  --color-thv24-dim: #94949e;
  --color-thv24-dim: oklch(0.67 0.01 285);
  --color-thv24-acc: #a78bfa;
  --color-thv24-acc: oklch(0.72 0.15 295);
  --font-thv24-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-24 {
  width: 100%;
  min-height: 100svh;
}

.thv-24 ::selection {
  background: var(--color-thv24-acc);
  color: #000;
}
```
