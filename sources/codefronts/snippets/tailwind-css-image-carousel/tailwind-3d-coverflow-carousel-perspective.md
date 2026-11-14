---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-3d-coverflow-carousel-perspective/"
title: "Tailwind 3D Coverflow Carousel with Perspective Transforms"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "The Cover Flow effect: the centre image faces you full-size while the flanking covers tilt back in 3D."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Coverflow Carousel with Perspective Transforms
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-3d-coverflow-carousel-perspective/

The Cover Flow effect: the centre image faces you full-size while the flanking covers tilt back in 3D. Tailwind v4 added real perspective-*, transform-3d and rotate-y-* utilities, so the 3D is native — but this is also the one demo where the port relocates complexity rather than removing it.
## HTML
```html
<section class="tcar-13 w-full min-h-svh grid place-items-center bg-tcar13-bg font-tcar13-sans px-5 py-10" aria-label="Album coverflow">
  <div class="group w-[min(560px,100%)] perspective-[1200px]">
    <input type="radio" name="tcar-13" id="tcar-13-1" class="sr-only">
    <input type="radio" name="tcar-13" id="tcar-13-2" class="sr-only">
    <input type="radio" name="tcar-13" id="tcar-13-3" class="sr-only" checked>
    <input type="radio" name="tcar-13" id="tcar-13-4" class="sr-only">
    <input type="radio" name="tcar-13" id="tcar-13-5" class="sr-only">
    <div class="relative h-[300px] transform-3d">
      <figure class="absolute top-1/2 left-1/2 size-[220px] -mt-[110px] -ml-[110px] m-0 rounded-[10px] overflow-hidden transform-3d opacity-55 shadow-[0_24px_40px_-20px_oklch(0_0_0/0.8)] transition-[translate,scale,opacity,transform] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-has-[#tcar-13-1:checked]:translate-x-0 group-has-[#tcar-13-1:checked]:rotate-y-0 group-has-[#tcar-13-1:checked]:scale-100 group-has-[#tcar-13-1:checked]:opacity-100 group-has-[#tcar-13-1:checked]:z-[5] group-has-[#tcar-13-2:checked]:-translate-x-[120px] group-has-[#tcar-13-2:checked]:rotate-y-[42deg] group-has-[#tcar-13-2:checked]:scale-[0.82] group-has-[#tcar-13-2:checked]:opacity-75 group-has-[#tcar-13-2:checked]:z-[4] group-has-[#tcar-13-3:checked]:-translate-x-[210px] group-has-[#tcar-13-3:checked]:rotate-y-[48deg] group-has-[#tcar-13-3:checked]:scale-[0.66] group-has-[#tcar-13-3:checked]:z-[3] group-has-[#tcar-13-4:checked]:-translate-x-[285px] group-has-[#tcar-13-4:checked]:rotate-y-[52deg] group-has-[#tcar-13-4:checked]:scale-[0.52] group-has-[#tcar-13-4:checked]:opacity-35 group-has-[#tcar-13-4:checked]:z-[2] group-has-[#tcar-13-5:checked]:-translate-x-[345px] group-has-[#tcar-13-5:checked]:rotate-y-[54deg] group-has-[#tcar-13-5:checked]:scale-[0.42] group-has-[#tcar-13-5:checked]:opacity-20 group-has-[#tcar-13-5:checked]:z-[1] group-has-[#tcar-13-1:focus-visible]:outline-3 group-has-[#tcar-13-1:focus-visible]:outline-tcar13-acc group-has-[#tcar-13-1:focus-visible]:outline-offset-4 motion-reduce:transition-none">
        <img src="https://picsum.photos/seed/cover-1/500/500" width="500" height="500" loading="lazy" decoding="async" alt="Album: Nocturne" class="size-full object-cover block pointer-events-none"><label for="tcar-13-1" aria-label="Show cover 1" class="absolute inset-0 cursor-pointer"></label>
      </figure>
      <figure class="absolute top-1/2 left-1/2 size-[220px] -mt-[110px] -ml-[110px] m-0 rounded-[10px] overflow-hidden transform-3d opacity-55 shadow-[0_24px_40px_-20px_oklch(0_0_0/0.8)] transition-[translate,scale,opacity,transform] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-has-[#tcar-13-1:checked]:translate-x-[120px] group-has-[#tcar-13-1:checked]:rotate-y-[-42deg] group-has-[#tcar-13-1:checked]:scale-[0.82] group-has-[#tcar-13-1:checked]:opacity-75 group-has-[#tcar-13-1:checked]:z-[4] group-has-[#tcar-13-2:checked]:translate-x-0 group-has-[#tcar-13-2:checked]:rotate-y-0 group-has-[#tcar-13-2:checked]:scale-100 group-has-[#tcar-13-2:checked]:opacity-100 group-has-[#tcar-13-2:checked]:z-[5] group-has-[#tcar-13-3:checked]:-translate-x-[120px] group-has-[#tcar-13-3:checked]:rotate-y-[42deg] group-has-[#tcar-13-3:checked]:scale-[0.82] group-has-[#tcar-13-3:checked]:opacity-75 group-has-[#tcar-13-3:checked]:z-[4] group-has-[#tcar-13-4:checked]:-translate-x-[210px] group-has-[#tcar-13-4:checked]:rotate-y-[48deg] group-has-[#tcar-13-4:checked]:scale-[0.66] group-has-[#tcar-13-4:checked]:z-[3] group-has-[#tcar-13-5:checked]:-translate-x-[285px] group-has-[#tcar-13-5:checked]:rotate-y-[52deg] group-has-[#tcar-13-5:checked]:scale-[0.52] group-has-[#tcar-13-5:checked]:opacity-35 group-has-[#tcar-13-5:checked]:z-[2] group-has-[#tcar-13-2:focus-visible]:outline-3 group-has-[#tcar-13-2:focus-visible]:outline-tcar13-acc group-has-[#tcar-13-2:focus-visible]:outline-offset-4 motion-reduce:transition-none">
        <img src="https://picsum.photos/seed/cover-2/500/500" width="500" height="500" loading="lazy" decoding="async" alt="Album: Parallel" class="size-full object-cover block pointer-events-none"><label for="tcar-13-2" aria-label="Show cover 2" class="absolute inset-0 cursor-pointer"></label>
      </figure>
      <figure class="absolute top-1/2 left-1/2 size-[220px] -mt-[110px] -ml-[110px] m-0 rounded-[10px] overflow-hidden transform-3d opacity-55 shadow-[0_24px_40px_-20px_oklch(0_0_0/0.8)] transition-[translate,scale,opacity,transform] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-has-[#tcar-13-1:checked]:translate-x-[210px] group-has-[#tcar-13-1:checked]:rotate-y-[-48deg] group-has-[#tcar-13-1:checked]:scale-[0.66] group-has-[#tcar-13-1:checked]:z-[3] group-has-[#tcar-13-2:checked]:translate-x-[120px] group-has-[#tcar-13-2:checked]:rotate-y-[-42deg] group-has-[#tcar-13-2:checked]:scale-[0.82] group-has-[#tcar-13-2:checked]:opacity-75 group-has-[#tcar-13-2:checked]:z-[4] group-has-[#tcar-13-3:checked]:translate-x-0 group-has-[#tcar-13-3:checked]:rotate-y-0 group-has-[#tcar-13-3:checked]:scale-100 group-has-[#tcar-13-3:checked]:opacity-100 group-has-[#tcar-13-3:checked]:z-[5] group-has-[#tcar-13-4:checked]:-translate-x-[120px] group-has-[#tcar-13-4:checked]:rotate-y-[42deg] group-has-[#tcar-13-4:checked]:scale-[0.82] group-has-[#tcar-13-4:checked]:opacity-75 group-has-[#tcar-13-4:checked]:z-[4] group-has-[#tcar-13-5:checked]:-translate-x-[210px] group-has-[#tcar-13-5:checked]:rotate-y-[48deg] group-has-[#tcar-13-5:checked]:scale-[0.66] group-has-[#tcar-13-5:checked]:z-[3] group-has-[#tcar-13-3:focus-visible]:outline-3 group-has-[#tcar-13-3:focus-visible]:outline-tcar13-acc group-has-[#tcar-13-3:focus-visible]:outline-offset-4 motion-reduce:transition-none">
        <img src="https://picsum.photos/seed/cover-3/500/500" width="500" height="500" decoding="async" alt="Album: Solstice" class="size-full object-cover block pointer-events-none"><label for="tcar-13-3" aria-label="Show cover 3" class="absolute inset-0 cursor-pointer"></label>
      </figure>
      <figure class="absolute top-1/2 left-1/2 size-[220px] -mt-[110px] -ml-[110px] m-0 rounded-[10px] overflow-hidden transform-3d opacity-55 shadow-[0_24px_40px_-20px_oklch(0_0_0/0.8)] transition-[translate,scale,opacity,transform] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-has-[#tcar-13-1:checked]:translate-x-[285px] group-has-[#tcar-13-1:checked]:rotate-y-[-52deg] group-has-[#tcar-13-1:checked]:scale-[0.52] group-has-[#tcar-13-1:checked]:opacity-35 group-has-[#tcar-13-1:checked]:z-[2] group-has-[#tcar-13-2:checked]:translate-x-[210px] group-has-[#tcar-13-2:checked]:rotate-y-[-48deg] group-has-[#tcar-13-2:checked]:scale-[0.66] group-has-[#tcar-13-2:checked]:z-[3] group-has-[#tcar-13-3:checked]:translate-x-[120px] group-has-[#tcar-13-3:checked]:rotate-y-[-42deg] group-has-[#tcar-13-3:checked]:scale-[0.82] group-has-[#tcar-13-3:checked]:opacity-75 group-has-[#tcar-13-3:checked]:z-[4] group-has-[#tcar-13-4:checked]:translate-x-0 group-has-[#tcar-13-4:checked]:rotate-y-0 group-has-[#tcar-13-4:checked]:scale-100 group-has-[#tcar-13-4:checked]:opacity-100 group-has-[#tcar-13-4:checked]:z-[5] group-has-[#tcar-13-5:checked]:-translate-x-[120px] group-has-[#tcar-13-5:checked]:rotate-y-[42deg] group-has-[#tcar-13-5:checked]:scale-[0.82] group-has-[#tcar-13-5:checked]:opacity-75 group-has-[#tcar-13-5:checked]:z-[4] group-has-[#tcar-13-4:focus-visible]:outline-3 group-has-[#tcar-13-4:focus-visible]:outline-tcar13-acc group-has-[#tcar-13-4:focus-visible]:outline-offset-4 motion-reduce:transition-none">
        <img src="https://picsum.photos/seed/cover-4/500/500" width="500" height="500" loading="lazy" decoding="async" alt="Album: Undertow" class="size-full object-cover block pointer-events-none"><label for="tcar-13-4" aria-label="Show cover 4" class="absolute inset-0 cursor-pointer"></label>
      </figure>
      <figure class="absolute top-1/2 left-1/2 size-[220px] -mt-[110px] -ml-[110px] m-0 rounded-[10px] overflow-hidden transform-3d opacity-55 shadow-[0_24px_40px_-20px_oklch(0_0_0/0.8)] transition-[translate,scale,opacity,transform] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-has-[#tcar-13-1:checked]:translate-x-[345px] group-has-[#tcar-13-1:checked]:rotate-y-[-54deg] group-has-[#tcar-13-1:checked]:scale-[0.42] group-has-[#tcar-13-1:checked]:opacity-20 group-has-[#tcar-13-1:checked]:z-[1] group-has-[#tcar-13-2:checked]:translate-x-[285px] group-has-[#tcar-13-2:checked]:rotate-y-[-52deg] group-has-[#tcar-13-2:checked]:scale-[0.52] group-has-[#tcar-13-2:checked]:opacity-35 group-has-[#tcar-13-2:checked]:z-[2] group-has-[#tcar-13-3:checked]:translate-x-[210px] group-has-[#tcar-13-3:checked]:rotate-y-[-48deg] group-has-[#tcar-13-3:checked]:scale-[0.66] group-has-[#tcar-13-3:checked]:z-[3] group-has-[#tcar-13-4:checked]:translate-x-[120px] group-has-[#tcar-13-4:checked]:rotate-y-[-42deg] group-has-[#tcar-13-4:checked]:scale-[0.82] group-has-[#tcar-13-4:checked]:opacity-75 group-has-[#tcar-13-4:checked]:z-[4] group-has-[#tcar-13-5:checked]:translate-x-0 group-has-[#tcar-13-5:checked]:rotate-y-0 group-has-[#tcar-13-5:checked]:scale-100 group-has-[#tcar-13-5:checked]:opacity-100 group-has-[#tcar-13-5:checked]:z-[5] group-has-[#tcar-13-5:focus-visible]:outline-3 group-has-[#tcar-13-5:focus-visible]:outline-tcar13-acc group-has-[#tcar-13-5:focus-visible]:outline-offset-4 motion-reduce:transition-none">
        <img src="https://picsum.photos/seed/cover-5/500/500" width="500" height="500" loading="lazy" decoding="async" alt="Album: Vantage" class="size-full object-cover block pointer-events-none"><label for="tcar-13-5" aria-label="Show cover 5" class="absolute inset-0 cursor-pointer"></label>
      </figure>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar13-bg: #111018;
  --color-tcar13-bg: oklch(0.18 0.015 290);
  --color-tcar13-acc: #7c5cff;
  --color-tcar13-acc: oklch(0.6 0.2 285);
  --font-tcar13-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tcar-13 {
  width: 100%;
  min-height: 100svh;
}

.tcar-13 ::selection {
  background: var(--color-tcar13-acc);
  color: #fff;
}
```
