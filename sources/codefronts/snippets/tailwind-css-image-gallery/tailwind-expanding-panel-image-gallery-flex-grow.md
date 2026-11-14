---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-expanding-panel-image-gallery-flex-grow/"
title: "Tailwind Expanding Panel Image Gallery with Flex-Grow Transitions"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "A full-bleed split of tall panels that slide open from flex:1 to flex:5 on hover or keyboard focus, revealing a title, blurb and call-to-action over the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Expanding Panel Image Gallery with Flex-Grow Transitions
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-expanding-panel-image-gallery-flex-grow/

A full-bleed split of tall panels that slide open from flex:1 to flex:5 on hover or keyboard focus, revealing a title, blurb and call-to-action over the photograph. The immersive case-study index, ported so that the open state and the copy reveal are declared on the elements they affect.
## HTML
```html
<section class="tgl-03 w-full min-h-svh flex items-stretch bg-tgl03-bg font-tgl03-sans" aria-label="Expanding panel gallery">
  <div class="flex w-full min-h-svh">
    <a href="#" style="--img:url('https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?q=80&w=900&h=1100&auto=format&fit=crop')" class="group relative flex-[1_1_0] min-w-0 overflow-hidden no-underline bg-[image:var(--img)] bg-cover bg-center brightness-[0.62] transition-[flex,filter] duration-[600ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:flex-[5_1_0] hover:brightness-100 focus-within:flex-[5_1_0] focus-within:brightness-100 focus-visible:outline-3 focus-visible:outline-tgl03-acc focus-visible:-outline-offset-[3px] motion-reduce:transition-none">
      <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(0deg,oklch(0.15_0.02_265/0.85),transparent_60%)]"></span>
      <span class="absolute left-0 right-0 top-6 z-[2] text-center text-[11px] font-bold tracking-[0.18em] uppercase text-white/70 transition-opacity duration-300 group-hover:opacity-0 group-focus-within:opacity-0">Structures</span>
      <div class="absolute left-0 right-0 bottom-0 z-[2] p-8 max-w-[520px] text-white opacity-0 translate-y-6 transition-[opacity,translate] duration-500 delay-150 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none">
        <h3 class="text-[30px] font-bold tracking-[-0.01em] m-0">Structures</h3>
        <p class="mt-2 text-[15px] leading-[1.5] text-white/85">Concrete, glass and the geometry of modern cities.</p>
        <span class="inline-block mt-3.5 text-[13px] font-bold tracking-[0.04em] text-tgl03-acc">View series &rarr;</span>
      </div>
    </a>
    <a href="#" style="--img:url('https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?q=80&w=900&h=1100&auto=format&fit=crop')" class="group relative flex-[1_1_0] min-w-0 overflow-hidden no-underline bg-[image:var(--img)] bg-cover bg-center brightness-[0.62] transition-[flex,filter] duration-[600ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:flex-[5_1_0] hover:brightness-100 focus-within:flex-[5_1_0] focus-within:brightness-100 focus-visible:outline-3 focus-visible:outline-tgl03-acc focus-visible:-outline-offset-[3px] motion-reduce:transition-none">
      <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(0deg,oklch(0.15_0.02_265/0.85),transparent_60%)]"></span>
      <span class="absolute left-0 right-0 top-6 z-[2] text-center text-[11px] font-bold tracking-[0.18em] uppercase text-white/70 transition-opacity duration-300 group-hover:opacity-0 group-focus-within:opacity-0">Wilderness</span>
      <div class="absolute left-0 right-0 bottom-0 z-[2] p-8 max-w-[520px] text-white opacity-0 translate-y-6 transition-[opacity,translate] duration-500 delay-150 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none">
        <h3 class="text-[30px] font-bold tracking-[-0.01em] m-0">Wilderness</h3>
        <p class="mt-2 text-[15px] leading-[1.5] text-white/85">Remote landscapes far from the nearest road.</p>
        <span class="inline-block mt-3.5 text-[13px] font-bold tracking-[0.04em] text-tgl03-acc">View series &rarr;</span>
      </div>
    </a>
    <a href="#" style="--img:url('https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?q=80&w=900&h=1100&auto=format&fit=crop')" class="group relative flex-[1_1_0] min-w-0 overflow-hidden no-underline bg-[image:var(--img)] bg-cover bg-center brightness-[0.62] transition-[flex,filter] duration-[600ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:flex-[5_1_0] hover:brightness-100 focus-within:flex-[5_1_0] focus-within:brightness-100 focus-visible:outline-3 focus-visible:outline-tgl03-acc focus-visible:-outline-offset-[3px] motion-reduce:transition-none">
      <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(0deg,oklch(0.15_0.02_265/0.85),transparent_60%)]"></span>
      <span class="absolute left-0 right-0 top-6 z-[2] text-center text-[11px] font-bold tracking-[0.18em] uppercase text-white/70 transition-opacity duration-300 group-hover:opacity-0 group-focus-within:opacity-0">Portraits</span>
      <div class="absolute left-0 right-0 bottom-0 z-[2] p-8 max-w-[520px] text-white opacity-0 translate-y-6 transition-[opacity,translate] duration-500 delay-150 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none">
        <h3 class="text-[30px] font-bold tracking-[-0.01em] m-0">Portraits</h3>
        <p class="mt-2 text-[15px] leading-[1.5] text-white/85">Faces and the stories written across them.</p>
        <span class="inline-block mt-3.5 text-[13px] font-bold tracking-[0.04em] text-tgl03-acc">View series &rarr;</span>
      </div>
    </a>
    <a href="#" style="--img:url('https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?q=80&w=900&h=1100&auto=format&fit=crop')" class="group relative flex-[1_1_0] min-w-0 overflow-hidden no-underline bg-[image:var(--img)] bg-cover bg-center brightness-[0.62] transition-[flex,filter] duration-[600ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:flex-[5_1_0] hover:brightness-100 focus-within:flex-[5_1_0] focus-within:brightness-100 focus-visible:outline-3 focus-visible:outline-tgl03-acc focus-visible:-outline-offset-[3px] motion-reduce:transition-none">
      <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(0deg,oklch(0.15_0.02_265/0.85),transparent_60%)]"></span>
      <span class="absolute left-0 right-0 top-6 z-[2] text-center text-[11px] font-bold tracking-[0.18em] uppercase text-white/70 transition-opacity duration-300 group-hover:opacity-0 group-focus-within:opacity-0">Water</span>
      <div class="absolute left-0 right-0 bottom-0 z-[2] p-8 max-w-[520px] text-white opacity-0 translate-y-6 transition-[opacity,translate] duration-500 delay-150 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none">
        <h3 class="text-[30px] font-bold tracking-[-0.01em] m-0">Water</h3>
        <p class="mt-2 text-[15px] leading-[1.5] text-white/85">Oceans, rivers and everything in between.</p>
        <span class="inline-block mt-3.5 text-[13px] font-bold tracking-[0.04em] text-tgl03-acc">View series &rarr;</span>
      </div>
    </a>
    <a href="#" style="--img:url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=900&h=1100&auto=format&fit=crop')" class="group relative flex-[1_1_0] min-w-0 overflow-hidden no-underline bg-[image:var(--img)] bg-cover bg-center brightness-[0.62] transition-[flex,filter] duration-[600ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:flex-[5_1_0] hover:brightness-100 focus-within:flex-[5_1_0] focus-within:brightness-100 focus-visible:outline-3 focus-visible:outline-tgl03-acc focus-visible:-outline-offset-[3px] motion-reduce:transition-none">
      <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(0deg,oklch(0.15_0.02_265/0.85),transparent_60%)]"></span>
      <span class="absolute left-0 right-0 top-6 z-[2] text-center text-[11px] font-bold tracking-[0.18em] uppercase text-white/70 transition-opacity duration-300 group-hover:opacity-0 group-focus-within:opacity-0">After Dark</span>
      <div class="absolute left-0 right-0 bottom-0 z-[2] p-8 max-w-[520px] text-white opacity-0 translate-y-6 transition-[opacity,translate] duration-500 delay-150 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none">
        <h3 class="text-[30px] font-bold tracking-[-0.01em] m-0">After Dark</h3>
        <p class="mt-2 text-[15px] leading-[1.5] text-white/85">Long exposures under a moving sky.</p>
        <span class="inline-block mt-3.5 text-[13px] font-bold tracking-[0.04em] text-tgl03-acc">View series &rarr;</span>
      </div>
    </a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl03-bg: #0c0e12;
  --color-tgl03-bg: oklch(0.14 0.012 265);
  --color-tgl03-acc: #6fa8ff;
  --color-tgl03-acc: oklch(0.75 0.14 250);
  --font-tgl03-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tgl-03 {
  width: 100%;
  min-height: 100svh;
}

.tgl-03 ::selection {
  background: var(--color-tgl03-acc);
  color: #0c0e12;
}
```
