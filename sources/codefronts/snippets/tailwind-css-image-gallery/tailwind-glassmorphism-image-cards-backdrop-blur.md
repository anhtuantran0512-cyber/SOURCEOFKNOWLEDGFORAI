---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-glassmorphism-image-cards-backdrop-blur/"
title: "Tailwind Glassmorphism Image Cards with backdrop-blur"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "Frosted-glass image cards floating over a vivid gradient scene, lifting and brightening as you hover."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Image Cards with backdrop-blur
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-glassmorphism-image-cards-backdrop-blur/

Frosted-glass image cards floating over a vivid gradient scene, lifting and brightening as you hover. Tailwind ships backdrop-blur-* and backdrop-saturate-* as composable utilities, so the pane-of-glass recipe — fill, blur, border, inset highlight — is four classes rather than four declarations.
## HTML
```html
<section class="tgl-14 w-full min-h-svh grid place-items-center px-5 py-10 font-tgl14-sans bg-[radial-gradient(45%_55%_at_12%_20%,oklch(0.72_0.2_25/0.95),transparent_60%),radial-gradient(45%_55%_at_88%_25%,oklch(0.72_0.2_280/0.95),transparent_60%),radial-gradient(55%_65%_at_55%_95%,oklch(0.76_0.19_190/0.9),transparent_60%),linear-gradient(135deg,oklch(0.3_0.12_300),oklch(0.2_0.08_265))]" aria-label="Glassmorphism hover cards gallery">
  <div class="flex flex-wrap justify-center gap-6 w-[min(900px,100%)]">
    <article class="group relative w-[250px] p-4 rounded-[22px] bg-white/15 backdrop-blur-[16px] backdrop-saturate-[1.4] border border-white/30 shadow-[0_24px_50px_-26px_rgba(0,0,0,0.55),inset_0_1px_0_rgba(255,255,255,0.4)] transition-[transform,box-shadow,border-color] duration-[400ms] hover:-translate-y-2 hover:border-white/50 hover:shadow-[0_36px_64px_-26px_rgba(0,0,0,0.6),inset_0_1px_0_rgba(255,255,255,0.55)] before:content-[''] before:absolute before:top-0 before:left-[14%] before:right-[14%] before:h-px before:bg-[linear-gradient(90deg,transparent,rgba(255,255,255,0.85),transparent)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="rounded-[14px] overflow-hidden border border-white/25 bg-white/10"><img src="https://images.unsplash.com/photo-1483058712412-4245e9b90334?q=80&w=400&h=400&auto=format&fit=crop" alt="Tropical sunset over the water" loading="lazy" decoding="async" class="block w-full aspect-square object-cover"></div>
      <h3 class="mt-3.5 text-[18px] font-bold text-white [text-shadow:0_1px_6px_rgba(0,0,0,0.35)]">Golden Hour</h3>
      <p class="mt-0.5 text-[13px] text-white/90">Maldives &middot; 2025</p>
    </article>
    <article class="group relative w-[250px] p-4 rounded-[22px] bg-white/15 backdrop-blur-[16px] backdrop-saturate-[1.4] border border-white/30 shadow-[0_24px_50px_-26px_rgba(0,0,0,0.55),inset_0_1px_0_rgba(255,255,255,0.4)] transition-[transform,box-shadow,border-color] duration-[400ms] hover:-translate-y-2 hover:border-white/50 hover:shadow-[0_36px_64px_-26px_rgba(0,0,0,0.6),inset_0_1px_0_rgba(255,255,255,0.55)] before:content-[''] before:absolute before:top-0 before:left-[14%] before:right-[14%] before:h-px before:bg-[linear-gradient(90deg,transparent,rgba(255,255,255,0.85),transparent)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="rounded-[14px] overflow-hidden border border-white/25 bg-white/10"><img src="https://images.unsplash.com/photo-1524985069026-dd778a71c7b4?q=80&w=400&h=400&auto=format&fit=crop" alt="Northern lights over a fjord" loading="lazy" decoding="async" class="block w-full aspect-square object-cover"></div>
      <h3 class="mt-3.5 text-[18px] font-bold text-white [text-shadow:0_1px_6px_rgba(0,0,0,0.35)]">Aurora</h3>
      <p class="mt-0.5 text-[13px] text-white/90">Troms&oslash; &middot; 2025</p>
    </article>
    <article class="group relative w-[250px] p-4 rounded-[22px] bg-white/15 backdrop-blur-[16px] backdrop-saturate-[1.4] border border-white/30 shadow-[0_24px_50px_-26px_rgba(0,0,0,0.55),inset_0_1px_0_rgba(255,255,255,0.4)] transition-[transform,box-shadow,border-color] duration-[400ms] hover:-translate-y-2 hover:border-white/50 hover:shadow-[0_36px_64px_-26px_rgba(0,0,0,0.6),inset_0_1px_0_rgba(255,255,255,0.55)] before:content-[''] before:absolute before:top-0 before:left-[14%] before:right-[14%] before:h-px before:bg-[linear-gradient(90deg,transparent,rgba(255,255,255,0.85),transparent)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="rounded-[14px] overflow-hidden border border-white/25 bg-white/10"><img src="https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?q=80&w=400&h=400&auto=format&fit=crop" alt="Red canyon walls at midday" loading="lazy" decoding="async" class="block w-full aspect-square object-cover"></div>
      <h3 class="mt-3.5 text-[18px] font-bold text-white [text-shadow:0_1px_6px_rgba(0,0,0,0.35)]">Red Rock</h3>
      <p class="mt-0.5 text-[13px] text-white/90">Arizona &middot; 2024</p>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl14-acc: #ffffff;
  --font-tgl14-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tgl-14 {
  width: 100%;
  min-height: 100svh;
}
/* Safari < 16.4 backdrop-filter prefix, for builds targeting older WebKit. */

.tgl-14 article {
  -webkit-backdrop-filter: blur(16px) saturate(1.4);
}

.tgl-14 ::selection {
  background: rgba(255,255,255,0.85);
  color: #2a1a4a;
}
```
