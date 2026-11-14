---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-pure-css-lightbox-gallery-target/"
title: "Tailwind Pure CSS Lightbox Gallery with :target (No JavaScript)"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "Click a thumbnail and the backdrop dims while the full image scales into a centred modal — a complete lightbox with no JavaScript, driven by :target."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pure CSS Lightbox Gallery with :target (No JavaScript)
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-pure-css-lightbox-gallery-target/

Click a thumbnail and the backdrop dims while the full image scales into a centred modal — a complete lightbox with no JavaScript, driven by :target. Tailwind ships target: and group-target: as real variants, which makes this the port where a whole interaction pattern survives intact.
## HTML
```html
<section class="tgl-10 relative w-full min-h-svh grid place-items-center bg-tgl10-bg font-tgl10-sans px-5 py-10" id="tgl-10" aria-label="Lightbox image gallery">
  <div class="w-[min(760px,100%)] grid grid-cols-3 gap-3 max-[560px]:grid-cols-2">
    <a href="#tgl-10-1" aria-label="Open image 1: desert road" class="group block rounded-[10px] overflow-hidden bg-tgl10-cell focus-visible:outline-3 focus-visible:outline-tgl10-acc focus-visible:outline-offset-2"><img src="https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?q=80&w=400&h=300&auto=format&fit=crop" alt="Desert road stretching to the horizon" loading="lazy" decoding="async" class="block w-full [aspect-ratio:4/3] object-cover transition-transform duration-[400ms] group-hover:scale-[1.07] group-focus-visible:scale-[1.07] motion-reduce:transition-none"></a>
    <a href="#tgl-10-2" aria-label="Open image 2: forest path" class="group block rounded-[10px] overflow-hidden bg-tgl10-cell focus-visible:outline-3 focus-visible:outline-tgl10-acc focus-visible:outline-offset-2"><img src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?q=80&w=400&h=300&auto=format&fit=crop" alt="Sunlit path through a forest" loading="lazy" decoding="async" class="block w-full [aspect-ratio:4/3] object-cover transition-transform duration-[400ms] group-hover:scale-[1.07] group-focus-visible:scale-[1.07] motion-reduce:transition-none"></a>
    <a href="#tgl-10-3" aria-label="Open image 3: mountain lake" class="group block rounded-[10px] overflow-hidden bg-tgl10-cell focus-visible:outline-3 focus-visible:outline-tgl10-acc focus-visible:outline-offset-2"><img src="https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?q=80&w=400&h=300&auto=format&fit=crop" alt="Mountain lake at sunrise" loading="lazy" decoding="async" class="block w-full [aspect-ratio:4/3] object-cover transition-transform duration-[400ms] group-hover:scale-[1.07] group-focus-visible:scale-[1.07] motion-reduce:transition-none"></a>
    <a href="#tgl-10-4" aria-label="Open image 4: city at night" class="group block rounded-[10px] overflow-hidden bg-tgl10-cell focus-visible:outline-3 focus-visible:outline-tgl10-acc focus-visible:outline-offset-2"><img src="https://images.unsplash.com/photo-1524985069026-dd778a71c7b4?q=80&w=400&h=300&auto=format&fit=crop" alt="City lights at night" loading="lazy" decoding="async" class="block w-full [aspect-ratio:4/3] object-cover transition-transform duration-[400ms] group-hover:scale-[1.07] group-focus-visible:scale-[1.07] motion-reduce:transition-none"></a>
    <a href="#tgl-10-5" aria-label="Open image 5: snowy peak" class="group block rounded-[10px] overflow-hidden bg-tgl10-cell focus-visible:outline-3 focus-visible:outline-tgl10-acc focus-visible:outline-offset-2"><img src="https://images.unsplash.com/photo-1486718448742-163732cd1544?q=80&w=400&h=300&auto=format&fit=crop" alt="Snow-covered mountain peak" loading="lazy" decoding="async" class="block w-full [aspect-ratio:4/3] object-cover transition-transform duration-[400ms] group-hover:scale-[1.07] group-focus-visible:scale-[1.07] motion-reduce:transition-none"></a>
    <a href="#tgl-10-6" aria-label="Open image 6: coastal cliffs" class="group block rounded-[10px] overflow-hidden bg-tgl10-cell focus-visible:outline-3 focus-visible:outline-tgl10-acc focus-visible:outline-offset-2"><img src="https://images.unsplash.com/photo-1485955900006-10f4d324d411?q=80&w=400&h=300&auto=format&fit=crop" alt="Rugged coastal cliffs" loading="lazy" decoding="async" class="block w-full [aspect-ratio:4/3] object-cover transition-transform duration-[400ms] group-hover:scale-[1.07] group-focus-visible:scale-[1.07] motion-reduce:transition-none"></a>
  </div>

  <div id="tgl-10-1" role="dialog" aria-label="Image 1 enlarged" class="group fixed inset-0 z-50 flex items-center justify-center p-6 invisible opacity-0 transition-[opacity,visibility] duration-300 target:visible target:opacity-100 motion-reduce:transition-none">
    <a href="#tgl-10" aria-label="Close enlarged image" class="absolute inset-0 bg-[oklch(0.15_0.01_265/0.86)] backdrop-blur-[3px]"></a>
    <figure class="relative m-0 max-w-[min(1000px,92vw)] max-h-[86vh] scale-[0.92] transition-transform duration-[350ms] ease-[cubic-bezier(0.2,0.8,0.2,1)] group-target:scale-100 motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?q=80&w=1000&h=700&auto=format&fit=crop" alt="Desert road stretching to the horizon" loading="lazy" decoding="async" class="block max-w-full max-h-[86vh] rounded-lg shadow-[0_40px_80px_-30px_rgba(0,0,0,0.8)]">
      <a href="#tgl-10" aria-label="Close image" class="absolute -top-3.5 -right-3.5 grid place-items-center w-11 h-11 rounded-full bg-white text-tgl10-bg text-base font-bold no-underline shadow-[0_6px_16px_-4px_rgba(0,0,0,0.5)] transition-colors duration-200 hover:bg-tgl10-acc hover:text-white focus-visible:outline-3 focus-visible:outline-tgl10-acc focus-visible:outline-offset-[3px]">&#10005;</a>
    </figure>
  </div>
  <div id="tgl-10-2" role="dialog" aria-label="Image 2 enlarged" class="group fixed inset-0 z-50 flex items-center justify-center p-6 invisible opacity-0 transition-[opacity,visibility] duration-300 target:visible target:opacity-100 motion-reduce:transition-none">
    <a href="#tgl-10" aria-label="Close enlarged image" class="absolute inset-0 bg-[oklch(0.15_0.01_265/0.86)] backdrop-blur-[3px]"></a>
    <figure class="relative m-0 max-w-[min(1000px,92vw)] max-h-[86vh] scale-[0.92] transition-transform duration-[350ms] ease-[cubic-bezier(0.2,0.8,0.2,1)] group-target:scale-100 motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?q=80&w=1000&h=700&auto=format&fit=crop" alt="Sunlit path through a forest" loading="lazy" decoding="async" class="block max-w-full max-h-[86vh] rounded-lg shadow-[0_40px_80px_-30px_rgba(0,0,0,0.8)]">
      <a href="#tgl-10" aria-label="Close image" class="absolute -top-3.5 -right-3.5 grid place-items-center w-11 h-11 rounded-full bg-white text-tgl10-bg text-base font-bold no-underline shadow-[0_6px_16px_-4px_rgba(0,0,0,0.5)] transition-colors duration-200 hover:bg-tgl10-acc hover:text-white focus-visible:outline-3 focus-visible:outline-tgl10-acc focus-visible:outline-offset-[3px]">&#10005;</a>
    </figure>
  </div>
  <div id="tgl-10-3" role="dialog" aria-label="Image 3 enlarged" class="group fixed inset-0 z-50 flex items-center justify-center p-6 invisible opacity-0 transition-[opacity,visibility] duration-300 target:visible target:opacity-100 motion-reduce:transition-none">
    <a href="#tgl-10" aria-label="Close enlarged image" class="absolute inset-0 bg-[oklch(0.15_0.01_265/0.86)] backdrop-blur-[3px]"></a>
    <figure class="relative m-0 max-w-[min(1000px,92vw)] max-h-[86vh] scale-[0.92] transition-transform duration-[350ms] ease-[cubic-bezier(0.2,0.8,0.2,1)] group-target:scale-100 motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?q=80&w=1000&h=700&auto=format&fit=crop" alt="Mountain lake at sunrise" loading="lazy" decoding="async" class="block max-w-full max-h-[86vh] rounded-lg shadow-[0_40px_80px_-30px_rgba(0,0,0,0.8)]">
      <a href="#tgl-10" aria-label="Close image" class="absolute -top-3.5 -right-3.5 grid place-items-center w-11 h-11 rounded-full bg-white text-tgl10-bg text-base font-bold no-underline shadow-[0_6px_16px_-4px_rgba(0,0,0,0.5)] transition-colors duration-200 hover:bg-tgl10-acc hover:text-white focus-visible:outline-3 focus-visible:outline-tgl10-acc focus-visible:outline-offset-[3px]">&#10005;</a>
    </figure>
  </div>
  <div id="tgl-10-4" role="dialog" aria-label="Image 4 enlarged" class="group fixed inset-0 z-50 flex items-center justify-center p-6 invisible opacity-0 transition-[opacity,visibility] duration-300 target:visible target:opacity-100 motion-reduce:transition-none">
    <a href="#tgl-10" aria-label="Close enlarged image" class="absolute inset-0 bg-[oklch(0.15_0.01_265/0.86)] backdrop-blur-[3px]"></a>
    <figure class="relative m-0 max-w-[min(1000px,92vw)] max-h-[86vh] scale-[0.92] transition-transform duration-[350ms] ease-[cubic-bezier(0.2,0.8,0.2,1)] group-target:scale-100 motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1524985069026-dd778a71c7b4?q=80&w=1000&h=700&auto=format&fit=crop" alt="City lights at night" loading="lazy" decoding="async" class="block max-w-full max-h-[86vh] rounded-lg shadow-[0_40px_80px_-30px_rgba(0,0,0,0.8)]">
      <a href="#tgl-10" aria-label="Close image" class="absolute -top-3.5 -right-3.5 grid place-items-center w-11 h-11 rounded-full bg-white text-tgl10-bg text-base font-bold no-underline shadow-[0_6px_16px_-4px_rgba(0,0,0,0.5)] transition-colors duration-200 hover:bg-tgl10-acc hover:text-white focus-visible:outline-3 focus-visible:outline-tgl10-acc focus-visible:outline-offset-[3px]">&#10005;</a>
    </figure>
  </div>
  <div id="tgl-10-5" role="dialog" aria-label="Image 5 enlarged" class="group fixed inset-0 z-50 flex items-center justify-center p-6 invisible opacity-0 transition-[opacity,visibility] duration-300 target:visible target:opacity-100 motion-reduce:transition-none">
    <a href="#tgl-10" aria-label="Close enlarged image" class="absolute inset-0 bg-[oklch(0.15_0.01_265/0.86)] backdrop-blur-[3px]"></a>
    <figure class="relative m-0 max-w-[min(1000px,92vw)] max-h-[86vh] scale-[0.92] transition-transform duration-[350ms] ease-[cubic-bezier(0.2,0.8,0.2,1)] group-target:scale-100 motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1486718448742-163732cd1544?q=80&w=1000&h=700&auto=format&fit=crop" alt="Snow-covered mountain peak" loading="lazy" decoding="async" class="block max-w-full max-h-[86vh] rounded-lg shadow-[0_40px_80px_-30px_rgba(0,0,0,0.8)]">
      <a href="#tgl-10" aria-label="Close image" class="absolute -top-3.5 -right-3.5 grid place-items-center w-11 h-11 rounded-full bg-white text-tgl10-bg text-base font-bold no-underline shadow-[0_6px_16px_-4px_rgba(0,0,0,0.5)] transition-colors duration-200 hover:bg-tgl10-acc hover:text-white focus-visible:outline-3 focus-visible:outline-tgl10-acc focus-visible:outline-offset-[3px]">&#10005;</a>
    </figure>
  </div>
  <div id="tgl-10-6" role="dialog" aria-label="Image 6 enlarged" class="group fixed inset-0 z-50 flex items-center justify-center p-6 invisible opacity-0 transition-[opacity,visibility] duration-300 target:visible target:opacity-100 motion-reduce:transition-none">
    <a href="#tgl-10" aria-label="Close enlarged image" class="absolute inset-0 bg-[oklch(0.15_0.01_265/0.86)] backdrop-blur-[3px]"></a>
    <figure class="relative m-0 max-w-[min(1000px,92vw)] max-h-[86vh] scale-[0.92] transition-transform duration-[350ms] ease-[cubic-bezier(0.2,0.8,0.2,1)] group-target:scale-100 motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1485955900006-10f4d324d411?q=80&w=1000&h=700&auto=format&fit=crop" alt="Rugged coastal cliffs" loading="lazy" decoding="async" class="block max-w-full max-h-[86vh] rounded-lg shadow-[0_40px_80px_-30px_rgba(0,0,0,0.8)]">
      <a href="#tgl-10" aria-label="Close image" class="absolute -top-3.5 -right-3.5 grid place-items-center w-11 h-11 rounded-full bg-white text-tgl10-bg text-base font-bold no-underline shadow-[0_6px_16px_-4px_rgba(0,0,0,0.5)] transition-colors duration-200 hover:bg-tgl10-acc hover:text-white focus-visible:outline-3 focus-visible:outline-tgl10-acc focus-visible:outline-offset-[3px]">&#10005;</a>
    </figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl10-bg: #0f1116;
  --color-tgl10-bg: oklch(0.16 0.01 265);
  --color-tgl10-cell: #1a1d24;
  --color-tgl10-cell: oklch(0.23 0.012 265);
  --color-tgl10-acc: #5b8cf0;
  --color-tgl10-acc: oklch(0.65 0.16 258);
  --font-tgl10-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tgl-10 {
  width: 100%;
  min-height: 100svh;
}

.tgl-10 ::selection {
  background: var(--color-tgl10-acc);
  color: #fff;
}
```
