---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-editorial-magazine-grid-gallery-blend-mode/"
title: "Tailwind Editorial Magazine Grid Gallery with Blend-Mode Headline"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "A premium editorial spread: a tall hero with the headline set directly over it in mix-blend-mode: difference, flanked by an asymmetric grid of supporting shots."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Editorial Magazine Grid Gallery with Blend-Mode Headline
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-editorial-magazine-grid-gallery-blend-mode/

A premium editorial spread: a tall hero with the headline set directly over it in mix-blend-mode: difference, flanked by an asymmetric grid of supporting shots. The port keeps the print-inspired type treatment and adds the scrim the blend mode needs to be safe.
## HTML
```html
<section class="tgl-09 w-full min-h-svh grid place-items-center bg-tgl09-bg font-tgl09-sans px-5 py-11" aria-label="Magazine layout gallery">
  <div class="w-[min(940px,100%)] grid grid-cols-2 gap-3.5 max-[640px]:grid-cols-1">
    <figure class="relative m-0 rounded-md overflow-hidden [grid-area:1/1/3/2] max-[640px]:[grid-area:auto]">
      <img src="https://images.unsplash.com/photo-1481277542470-605612bd2d61?q=80&w=900&h=700&auto=format&fit=crop" alt="Winding coastal road at sunset" loading="lazy" decoding="async" class="block w-full h-full object-cover [aspect-ratio:9/11]">
      <span aria-hidden="true" class="absolute inset-x-0 bottom-0 h-1/3 bg-[linear-gradient(0deg,rgba(0,0,0,0.45),transparent)]"></span>
      <figcaption class="absolute inset-x-0 bottom-0 p-6 mix-blend-difference text-white">
        <span class="block font-tgl09-mono text-xs tracking-[0.2em] uppercase opacity-90">Issue 24 &middot; Travel</span>
        <h3 class="mt-2 font-tgl09-serif text-[40px] leading-[1.02] font-bold tracking-[-0.01em] text-balance max-[640px]:text-[32px]">The Long Way North</h3>
      </figcaption>
    </figure>
    <figure class="group relative m-0 rounded-md overflow-hidden bg-tgl09-well">
      <img src="https://images.unsplash.com/photo-1531403009284-440f080d1e12?q=80&w=500&h=500&auto=format&fit=crop" alt="Fishing harbour at first light" loading="lazy" decoding="async" class="block w-full h-full object-cover aspect-square transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-105 motion-reduce:transition-none">
      <figcaption class="absolute inset-x-0 bottom-0 px-3.5 py-2.5 w-full text-white font-tgl09-serif italic text-[15px] bg-[linear-gradient(0deg,rgba(0,0,0,0.65),transparent)]">Harbour mornings</figcaption>
    </figure>
    <figure class="group relative m-0 rounded-md overflow-hidden bg-tgl09-well">
      <img src="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=500&h=500&auto=format&fit=crop" alt="Timber cabin among pines" loading="lazy" decoding="async" class="block w-full h-full object-cover aspect-square transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-105 motion-reduce:transition-none">
      <figcaption class="absolute inset-x-0 bottom-0 px-3.5 py-2.5 w-full text-white font-tgl09-serif italic text-[15px] bg-[linear-gradient(0deg,rgba(0,0,0,0.65),transparent)]">Off the map</figcaption>
    </figure>
    <figure class="group relative m-0 col-span-2 rounded-md overflow-hidden bg-tgl09-well max-[640px]:col-span-1">
      <img src="https://images.unsplash.com/photo-1611432579699-484f7990b127?q=80&w=900&h=450&auto=format&fit=crop" alt="Empty mountain highway" loading="lazy" decoding="async" class="block w-full h-full object-cover [aspect-ratio:2/1] transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-105 motion-reduce:transition-none">
      <figcaption class="absolute inset-x-0 bottom-0 px-3.5 py-2.5 w-full text-white font-tgl09-serif italic text-[15px] bg-[linear-gradient(0deg,rgba(0,0,0,0.65),transparent)]">Nothing but road ahead</figcaption>
    </figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl09-bg: #f7f5f0;
  --color-tgl09-bg: oklch(0.97 0.008 85);
  --color-tgl09-well: #e7e3da;
  --color-tgl09-well: oklch(0.91 0.012 85);
  --color-tgl09-acc: #1a1a1a;
  --color-tgl09-acc: oklch(0.2 0 0);
  --font-tgl09-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tgl09-serif: 'Playfair Display', Georgia, 'Times New Roman', serif;
  --font-tgl09-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
}

.tgl-09 {
  width: 100%;
  min-height: 100svh;
}

.tgl-09 ::selection {
  background: var(--color-tgl09-acc);
  color: #fff;
}
```
