---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-luxury-product-card-hinged-book-open-unfold/"
title: "Tailwind Luxury Product Card with Hinged Book-Open 3D Unfold"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "A watch card that opens like a book: the back panel is hinged at the card's right edge and swings in from rotateY(-90deg) rather than spinning around the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Luxury Product Card with Hinged Book-Open 3D Unfold
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-luxury-product-card-hinged-book-open-unfold/

A watch card that opens like a book: the back panel is hinged at the card's right edge and swings in from rotateY(-90deg) rather than spinning around the centre. It is the collection's one demo that deliberately sets backface-visibility: visible &mdash; the panel never passes 90&deg; relative to the viewer, so hiding its back face would hide the panel itself.
## HTML
```html
<section class="tfc-19 w-full min-h-svh grid place-items-center bg-tfc19-bg font-tfc19-serif px-5 py-10 text-tfc19-ivory">
  <div class="group relative h-[510px] w-[360px] max-w-full [perspective:1600px] rounded-md has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc19-gold has-[:focus-visible]:outline-offset-4">
    <input id="tfc-19-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-19-flip" class="absolute inset-0 z-30 cursor-pointer rounded-md peer-checked:pointer-events-none"><span class="sr-only">Open the specification panel for the Heritage Chronograph 1957</span></label>

    <div class="absolute inset-0 z-1 flex flex-col items-center rounded-md overflow-hidden border border-tfc19-gold/25 bg-linear-160 from-tfc19-p1 to-tfc19-p2 px-8 py-9 shadow-[inset_0_1px_0_oklch(0.95_0.05_85/0.06),0_12px_30px_oklch(0_0_0/0.5)] transition-[opacity,transform] duration-[800ms] ease-[cubic-bezier(.4,0,.2,1)] group-hover:-translate-x-[3%] group-hover:opacity-50 group-has-checked:-translate-x-[3%] group-has-checked:opacity-50 group-has-[:focus-visible]:opacity-50 motion-reduce:transition-none">
      <p class="mb-2 flex items-center gap-2">
        <span class="grid size-8 place-items-center border border-tfc19-gold font-tfc19-serif text-lg font-semibold text-tfc19-gold">M</span>
        <span class="font-tfc19-serif text-[11px] font-medium tracking-[0.45em] text-tfc19-gold">MERIDIAN</span>
      </p>
      <div class="my-1 mb-4">
        <svg width="180" height="180" viewBox="0 0 200 200" fill="none" role="img" aria-label="Rose-gold chronograph watch with a black dial">
          <defs>
            <linearGradient id="tfc-19-bezel" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fef3c7"/><stop offset="50%" stop-color="#d4af37"/><stop offset="100%" stop-color="#8c6917"/></linearGradient>
            <radialGradient id="tfc-19-dial" cx="0.5" cy="0.5" r="0.6"><stop offset="0%" stop-color="#1c1c1c"/><stop offset="80%" stop-color="#0a0a0a"/></radialGradient>
          </defs>
          <circle cx="100" cy="100" r="90" fill="url(#tfc-19-bezel)"/>
          <circle cx="100" cy="100" r="78" fill="url(#tfc-19-dial)"/>
          <circle cx="100" cy="100" r="76" fill="none" stroke="#d4af37" stroke-width="0.5" opacity="0.4"/>
          <g stroke="#d4af37" stroke-width="2" stroke-linecap="round"><line x1="100" y1="32" x2="100" y2="42"/><line x1="100" y1="158" x2="100" y2="168"/><line x1="32" y1="100" x2="42" y2="100"/><line x1="158" y1="100" x2="168" y2="100"/></g>
          <g stroke="#fef3c7" stroke-width="1.2" stroke-linecap="round" opacity="0.7"><line x1="151" y1="65" x2="146" y2="69"/><line x1="151" y1="135" x2="146" y2="131"/><line x1="49" y1="65" x2="54" y2="69"/><line x1="49" y1="135" x2="54" y2="131"/></g>
          <line x1="100" y1="100" x2="100" y2="50" stroke="#fef3c7" stroke-width="2.4" stroke-linecap="round"/>
          <line x1="100" y1="100" x2="138" y2="120" stroke="#fef3c7" stroke-width="2" stroke-linecap="round"/>
          <line x1="100" y1="100" x2="80" y2="124" stroke="#d4af37" stroke-width="1" stroke-linecap="round"/>
          <circle cx="100" cy="100" r="3" fill="#d4af37"/>
          <text x="100" y="148" text-anchor="middle" font-family="serif" font-size="7" fill="#d4af37" letter-spacing="2">MERIDIAN</text>
        </svg>
      </div>
      <h3 class="text-center text-lg italic tracking-[0.02em] text-tfc19-ivory">Heritage Chronograph 1957</h3>
      <p class="mt-3.5 flex flex-col items-center gap-0.5">
        <span class="font-tfc19-serif text-[28px] font-medium tracking-[0.04em] text-tfc19-gold">$12,400</span>
        <span class="font-tfc19-ui text-[10px] uppercase tracking-[0.3em] text-tfc19-ivory/45">Limited release</span>
      </p>
      <p class="mt-auto font-tfc19-ui text-[10px] uppercase tracking-[0.25em] text-tfc19-gold/60">Hover, tap or press Space to open</p>
    </div>

    <div class="absolute inset-0 z-2 flex origin-left flex-col items-center rounded-md overflow-hidden border border-tfc19-gold/40 bg-linear-160 from-tfc19-b1 to-tfc19-b2 px-8 py-9 shadow-[inset_0_1px_0_oklch(0.95_0.05_85/0.1),0_16px_40px_oklch(0_0_0/0.6)] [transform:rotateY(-90deg)] [backface-visibility:visible] [-webkit-backface-visibility:visible] transition-transform duration-[900ms] ease-[cubic-bezier(.4,0,.2,1)] group-hover:[transform:rotateY(0deg)] group-has-checked:[transform:rotateY(0deg)] group-has-[:focus-visible]:[transform:rotateY(0deg)] motion-reduce:transition-none">
      <p class="mb-2 font-tfc19-ui text-[10px] font-semibold uppercase tracking-[0.4em] text-tfc19-gold">Specifications</p>
      <h3 class="mb-4.5 text-center text-xl italic leading-tight text-tfc19-ivory">Heritage Chronograph 1957</h3>
      <dl class="mb-4.5 flex w-full flex-col gap-2.5">
        <div class="flex flex-col gap-0.5 border-b border-tfc19-gold/12 pb-2"><dt class="font-tfc19-ui text-[9px] font-semibold uppercase tracking-[0.25em] text-tfc19-gold/70">Case</dt><dd class="font-tfc19-serif text-[13px] text-tfc19-ivory">18k Rose Gold &middot; 40 mm</dd></div>
        <div class="flex flex-col gap-0.5 border-b border-tfc19-gold/12 pb-2"><dt class="font-tfc19-ui text-[9px] font-semibold uppercase tracking-[0.25em] text-tfc19-gold/70">Movement</dt><dd class="font-tfc19-serif text-[13px] text-tfc19-ivory">Caliber M-29 Automatic</dd></div>
        <div class="flex flex-col gap-0.5 border-b border-tfc19-gold/12 pb-2"><dt class="font-tfc19-ui text-[9px] font-semibold uppercase tracking-[0.25em] text-tfc19-gold/70">Reserve</dt><dd class="font-tfc19-serif text-[13px] text-tfc19-ivory">72-hour power reserve</dd></div>
        <div class="flex flex-col gap-0.5 border-b border-tfc19-gold/12 pb-2"><dt class="font-tfc19-ui text-[9px] font-semibold uppercase tracking-[0.25em] text-tfc19-gold/70">Water</dt><dd class="font-tfc19-serif text-[13px] text-tfc19-ivory">100 m &middot; screw-down crown</dd></div>
        <div class="flex flex-col gap-0.5 border-b border-tfc19-gold/12 pb-2"><dt class="font-tfc19-ui text-[9px] font-semibold uppercase tracking-[0.25em] text-tfc19-gold/70">Crystal</dt><dd class="font-tfc19-serif text-[13px] text-tfc19-ivory">Domed sapphire &middot; AR coated</dd></div>
        <div class="flex flex-col gap-0.5"><dt class="font-tfc19-ui text-[9px] font-semibold uppercase tracking-[0.25em] text-tfc19-gold/70">Strap</dt><dd class="font-tfc19-serif text-[13px] text-tfc19-ivory">Alligator &middot; pin buckle</dd></div>
      </dl>
      <a href="#" class="relative z-30 flex min-h-11 w-full items-center justify-center bg-linear-135 from-tfc19-gold to-tfc19-goldD font-tfc19-ui text-[11px] font-semibold uppercase tracking-[0.3em] text-black no-underline shadow-[0_6px_18px_oklch(0.78_0.13_85/0.25)] transition-[filter,box-shadow] duration-200 hover:brightness-110 focus-visible:outline-2 focus-visible:outline-tfc19-ivory focus-visible:outline-offset-2">Reserve this piece</a>
      <p class="mt-3.5 text-center font-tfc19-ui text-[9px] uppercase tracking-[0.25em] text-tfc19-ivory/40">12 / 200 cast &middot; made in Switzerland</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc19-bg: #080806;
  --color-tfc19-bg: oklch(0.13 0.005 90);
  --color-tfc19-p1: #1a1610;
  --color-tfc19-p1: oklch(0.2 0.015 80);
  --color-tfc19-p2: #0c0a07;
  --color-tfc19-p2: oklch(0.14 0.01 80);
  --color-tfc19-b1: #15110b;
  --color-tfc19-b1: oklch(0.18 0.015 80);
  --color-tfc19-b2: #0a0805;
  --color-tfc19-b2: oklch(0.13 0.01 80);
  --color-tfc19-gold: #d4af37;
  --color-tfc19-gold: oklch(0.78 0.13 85);
  --color-tfc19-goldD: #b8941f;
  --color-tfc19-goldD: oklch(0.68 0.13 85);
  --color-tfc19-ivory: #f5f1e8;
  --color-tfc19-ivory: oklch(0.96 0.015 85);
  --font-tfc19-serif: 'Cormorant Garamond', Georgia, serif;
  --font-tfc19-ui: 'Inter Tight', system-ui, sans-serif;
}

.tfc-19 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-19 * {
    transition-duration: 1ms !important;
  }
}
```
