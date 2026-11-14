---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-3d-pop-out-product-card-translatez/"
title: "Tailwind 3D Pop-Out Product Card with translateZ Lift"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "A sneaker drop card that sits tilted at rest and deepens on hover while the product photo lifts out of the frame on translateZ."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Pop-Out Product Card with translateZ Lift
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-3d-pop-out-product-card-translatez/

A sneaker drop card that sits tilted at rest and deepens on hover while the product photo lifts out of the frame on translateZ. The port's win is the sold-out swatch: a diagonal strike plus aria-disabled plus an sr-only label, so the state is no longer communicated by a line alone.
## HTML
```html
<section class="twc-19 relative w-full min-h-svh flex items-center justify-center overflow-hidden px-5 py-9 [perspective:2000px] bg-twc19-bg [background-image:radial-gradient(ellipse_at_20%_15%,oklch(0.62_0.19_45/0.09),transparent_45%),radial-gradient(ellipse_at_80%_85%,oklch(0.38_0.1_55/0.09),transparent_45%),linear-gradient(180deg,#f5f0e8_0%,#ebe1cf_100%)] font-twc19-sans">

  <div aria-hidden="true" class="absolute inset-0 z-0 overflow-hidden pointer-events-none">
    <div class="absolute top-1/2 left-1/2 size-175 -translate-x-1/2 -translate-y-1/2 blur-[60px] [background:radial-gradient(circle,oklch(0.62_0.19_45/0.16)_0%,transparent_55%)]"></div>
    <div class="absolute inset-0 [background-image:linear-gradient(oklch(0.38_0.1_55/0.05)_1px,transparent_1px),linear-gradient(90deg,oklch(0.38_0.1_55/0.05)_1px,transparent_1px)] [background-size:40px_40px] [mask-image:radial-gradient(ellipse_at_center,black_20%,transparent_65%)] [-webkit-mask-image:radial-gradient(ellipse_at_center,black_20%,transparent_65%)]"></div>
  </div>

  <article class="group/card relative z-1 w-full max-w-[380px] rounded-[26px] bg-white border border-black/5 [transform-style:preserve-3d] [transform:perspective(2000px)_rotateX(4deg)_rotateY(-4deg)] transition-[transform,box-shadow] duration-600 ease-[cubic-bezier(0.34,1.2,0.64,1)] hover:[transform:perspective(2000px)_rotateX(2deg)_rotateY(-8deg)_translateY(-6px)] shadow-[0_40px_80px_-30px_oklch(0.4_0.08_50/0.4),0_20px_40px_-20px_oklch(0.62_0.19_45/0.2),inset_0_1px_0_oklch(1_0_0/0.6)] hover:shadow-[0_60px_100px_-30px_oklch(0.4_0.08_50/0.5),0_30px_50px_-20px_oklch(0.62_0.19_45/0.32),inset_0_1px_0_oklch(1_0_0/0.6)] motion-reduce:transition-none motion-reduce:hover:[transform:perspective(2000px)_rotateX(4deg)_rotateY(-4deg)]">

    <div class="relative aspect-[1.4/1] overflow-visible isolate rounded-t-[26px] [transform-style:preserve-3d]">
      <div aria-hidden="true" class="absolute inset-0 overflow-hidden rounded-t-[26px] [background:radial-gradient(ellipse_at_60%_40%,#fed7aa_0%,transparent_55%),linear-gradient(160deg,#ffe4c4_0%,#fdba74_60%,#ea580c_100%)]"></div>
      <div aria-hidden="true" class="absolute bottom-[12%] left-1/2 -translate-x-1/2 size-80 pointer-events-none">
        <div class="absolute inset-0 rounded-full border border-dashed border-twc19-ring/18 animate-twc19-spin motion-reduce:animate-none"></div>
        <div class="absolute inset-[20%] rounded-full border border-dashed border-twc19-ring/14 animate-twc19-spin [animation-direction:reverse] [animation-duration:20s] motion-reduce:animate-none"></div>
      </div>

      <div class="absolute top-3.5 left-3.5 z-4 flex flex-wrap gap-1.5">
        <span class="inline-flex items-center gap-1 px-2 py-1 rounded-md bg-twc19-red/95 text-white border border-white/15 font-twc19-mono text-[9px] font-extrabold tracking-[0.14em] uppercase shadow-[0_2px_8px_oklch(0.58_0.22_25/0.3)]">
          <span aria-hidden="true" class="size-[5px] rounded-full bg-white animate-twc19-blink motion-reduce:animate-none"></span>
          LIVE DROP
        </span>
        <span class="inline-flex items-center gap-1 px-2 py-1 rounded-md bg-white/85 backdrop-blur-[6px] text-twc19-accdark border border-twc19-accdark/20 font-twc19-mono text-[9px] font-extrabold tracking-[0.14em] uppercase">
          <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
          AR
        </span>
      </div>

      <button type="button" aria-label="Add Nova Runner 04 to wishlist" class="absolute top-3.5 right-3.5 z-4 inline-flex items-center justify-center size-11 rounded-full bg-white/85 backdrop-blur-[6px] border border-black/6 text-twc19-ink cursor-pointer transition-[color,transform] duration-200 hover:text-twc19-red hover:scale-108 focus-visible:outline-2 focus-visible:outline-twc19-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 1 0-7.8 7.8L12 21.1l8.8-8.7a5.5 5.5 0 0 0 0-7.8z"/></svg>
      </button>

      <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800&q=85&auto=format&fit=crop" alt="Nova Runner 04 Cloudmist sneaker" loading="lazy" decoding="async" class="absolute bottom-[8%] left-1/2 w-4/5 h-3/4 z-3 object-contain pointer-events-none [transform:translateX(-50%)_translateZ(80px)_rotate(-6deg)] drop-shadow-[0_14px_18px_oklch(0.4_0.08_45/0.3)] transition-[transform,filter] duration-600 ease-[cubic-bezier(0.34,1.2,0.64,1)] group-hover/card:[transform:translateX(-50%)_translateZ(150px)_rotate(-8deg)_scale(1.08)] group-hover/card:drop-shadow-[0_22px_26px_oklch(0.4_0.08_45/0.36)] motion-reduce:transition-none motion-reduce:group-hover/card:[transform:translateX(-50%)_translateZ(80px)_rotate(-6deg)]">
      <div aria-hidden="true" class="absolute bottom-[4%] left-1/2 -translate-x-1/2 w-3/5 h-5 z-2 pointer-events-none blur-[10px] transition-[width,opacity] duration-600 group-hover/card:w-[68%] group-hover/card:opacity-80 motion-reduce:transition-none motion-reduce:group-hover/card:w-3/5 [background:radial-gradient(ellipse,oklch(0.4_0.08_45/0.5),transparent_65%)]"></div>

      <div class="absolute bottom-3 right-3.5 z-4 inline-flex items-center gap-1 pl-1.5 pr-2 py-1 rounded-full bg-white/85 backdrop-blur-[6px]">
        <span aria-hidden="true" class="w-3 h-[5px] rounded-full bg-twc19-accdark"></span>
        <span aria-hidden="true" class="size-[5px] rounded-full bg-twc19-accdark/30"></span>
        <span aria-hidden="true" class="size-[5px] rounded-full bg-twc19-accdark/30"></span>
        <span aria-hidden="true" class="size-[5px] rounded-full bg-twc19-accdark/30"></span>
        <span class="ml-1 font-twc19-mono text-[9px] font-bold tracking-[0.02em] text-twc19-accdark [font-variant-numeric:tabular-nums]">View 1 of 4</span>
      </div>

      <div class="absolute bottom-3 left-3.5 z-4 flex flex-col gap-px px-2.5 py-1.5 rounded-lg bg-white/85 backdrop-blur-[6px]">
        <span class="font-twc19-mono text-[8px] font-extrabold tracking-[0.14em] uppercase text-twc19-accink">DROP CLOSES</span>
        <span class="inline-flex items-baseline gap-px font-twc19-mono text-xs font-extrabold tracking-[-0.01em] text-twc19-accdark [font-variant-numeric:tabular-nums]">
          <span>02</span><em class="not-italic mr-0.5 text-[8px] text-twc19-accink/60">H</em><span>47</span><em class="not-italic mr-0.5 text-[8px] text-twc19-accink/60">M</em><span>13</span><em class="not-italic text-[8px] text-twc19-accink/60">S</em>
        </span>
      </div>
    </div>

    <div class="flex flex-col gap-3 px-4.5 py-4 rounded-b-[26px] [background:linear-gradient(180deg,#fff_0%,#fafaf7_100%)] [transform:translateZ(30px)] [transform-style:preserve-3d]">

      <div class="grid grid-cols-[1fr_auto] items-start gap-3">
        <div>
          <p class="m-0 mb-1 font-twc19-mono text-[9px] font-extrabold tracking-[0.14em] text-twc19-acc">SNEAKERS &middot; NEW DROP &middot; SS27</p>
          <h3 class="m-0 text-[17px]/[1.2] font-extrabold tracking-[-0.02em] text-twc19-ink">Nova Runner 04 <span class="font-bold text-twc19-acc">&middot; Cloudmist</span></h3>
          <div role="img" aria-label="Rated 4.9 out of 5 from 2,847 reservations" class="inline-flex items-center gap-1 mt-1 text-[10.5px]">
            <span aria-hidden="true" class="inline-flex gap-px mr-0.5 text-twc19-amber">
              <svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
              <svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
              <svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
              <svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
              <svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            </span>
            <span class="font-extrabold tracking-[-0.01em] text-twc19-amberink [font-variant-numeric:tabular-nums]">4.9</span>
            <span class="text-twc19-dim">&middot; 2,847 reservations</span>
          </div>
        </div>
        <div class="flex flex-col items-end gap-px">
          <span class="text-2xl font-extrabold tracking-[-0.03em] text-twc19-ink [font-variant-numeric:tabular-nums]">$189</span>
          <span class="text-[9.5px] text-twc19-muted">or 4&times; $47<span class="ml-0.5 font-bold text-twc19-acc">&middot;klarna</span></span>
        </div>
      </div>

      <ul class="flex flex-wrap gap-1.5 list-none m-0 p-0">
        <li class="inline-flex items-center gap-1 px-2 py-[3px] rounded-full text-[10.5px] font-bold text-twc19-greenink bg-twc19-green/12 border border-twc19-green/26">
          <span aria-hidden="true" class="size-[5px] rounded-full bg-twc19-green shadow-[0_0_4px_oklch(0.77_0.2_130)]"></span>
          Ethical
        </li>
        <li class="inline-flex items-center px-2 py-[3px] rounded-full text-[10.5px] font-bold text-twc19-accdark bg-twc19-acc/8 border border-twc19-acc/24">Portugal-made</li>
        <li class="inline-flex items-center px-2 py-[3px] rounded-full text-[10.5px] font-bold text-twc19-ink2 bg-black/3 border border-black/8">Recycled 62%</li>
      </ul>

      <div class="flex items-center justify-between gap-2.5 px-3 py-2.5 rounded-xl bg-black/2 border border-black/5">
        <span class="flex flex-col gap-px font-twc19-mono text-[8.5px] font-extrabold tracking-[0.14em] uppercase text-twc19-muted">
          COLOR
          <em class="not-italic font-twc19-sans text-[11.5px] font-extrabold tracking-[-0.01em] normal-case text-twc19-ink">Cloudmist</em>
        </span>
        <div class="flex gap-1">
          <button type="button" aria-label="Cloudmist" aria-pressed="true" class="relative size-11 p-2.5 rounded-full bg-transparent border-[1.5px] border-twc19-acc cursor-pointer transition-transform duration-200 hover:scale-108 focus-visible:outline-2 focus-visible:outline-twc19-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100"><span class="block size-full rounded-full [background:linear-gradient(135deg,#e5e7eb,#f9fafb)] shadow-[inset_0_1px_0_oklch(1_0_0/0.3),inset_0_-1px_0_oklch(0_0_0/0.15)]"></span></button>
          <button type="button" aria-label="Ember" aria-pressed="false" class="relative size-11 p-2.5 rounded-full bg-transparent border-[1.5px] border-transparent cursor-pointer transition-transform duration-200 hover:scale-108 focus-visible:outline-2 focus-visible:outline-twc19-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100"><span class="block size-full rounded-full [background:linear-gradient(135deg,#ea580c,#7c2d12)] shadow-[inset_0_1px_0_oklch(1_0_0/0.3),inset_0_-1px_0_oklch(0_0_0/0.15)]"></span></button>
          <button type="button" aria-label="Midnight" aria-pressed="false" class="relative size-11 p-2.5 rounded-full bg-transparent border-[1.5px] border-transparent cursor-pointer transition-transform duration-200 hover:scale-108 focus-visible:outline-2 focus-visible:outline-twc19-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100"><span class="block size-full rounded-full [background:linear-gradient(135deg,#1e293b,#0f172a)] shadow-[inset_0_1px_0_oklch(1_0_0/0.3),inset_0_-1px_0_oklch(0_0_0/0.15)]"></span></button>
          <button type="button" aria-label="Sage" aria-disabled="true" class="relative size-11 p-2.5 rounded-full bg-transparent border-[1.5px] border-transparent cursor-not-allowed opacity-70 focus-visible:outline-2 focus-visible:outline-twc19-acc focus-visible:outline-offset-2 after:absolute after:inset-2.5 after:rounded-full after:content-[''] after:[background:linear-gradient(45deg,transparent_45%,oklch(0.58_0.22_25/0.8)_45%,oklch(0.58_0.22_25/0.8)_55%,transparent_55%)]"><span class="block size-full rounded-full [background:linear-gradient(135deg,#84cc16,#365314)] shadow-[inset_0_1px_0_oklch(1_0_0/0.3),inset_0_-1px_0_oklch(0_0_0/0.15)]"></span><span class="sr-only">Sold out</span></button>
        </div>
      </div>

      <div class="grid grid-cols-[1fr_auto] gap-1.5">
        <button type="button" class="group/cta relative inline-flex items-center justify-center gap-1.5 overflow-hidden min-h-11 px-4 rounded-2xl border-0 cursor-pointer text-[13px] font-extrabold tracking-[-0.01em] text-white [background:linear-gradient(180deg,#ea580c_0%,#9a3412_100%)] shadow-[0_6px_16px_oklch(0.62_0.19_45/0.4),inset_0_0_0_1px_oklch(1_0_0/0.14)] transition-[transform,box-shadow] duration-200 hover:-translate-y-px hover:shadow-[0_10px_24px_oklch(0.62_0.19_45/0.55),inset_0_0_0_1px_oklch(1_0_0/0.28)] focus-visible:outline-2 focus-visible:outline-twc19-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
          <span aria-hidden="true" class="absolute top-0 -left-full w-3/5 h-full transition-[left] duration-600 ease-out group-hover/cta:left-[130%] motion-reduce:transition-none motion-reduce:group-hover/cta:-left-full [background:linear-gradient(115deg,transparent_30%,oklch(1_0_0/0.4)_50%,transparent_70%)]"></span>
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="relative"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
          <span class="relative">Reserve for $189</span>
          <span aria-hidden="true" class="relative inline-flex items-center transition-transform duration-200 group-hover/cta:translate-x-1 motion-reduce:transition-none motion-reduce:group-hover/cta:translate-x-0">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </span>
        </button>
        <button type="button" aria-label="View Nova Runner 04 in augmented reality" class="inline-flex items-center justify-center min-h-11 min-w-11 rounded-2xl bg-white border border-twc19-accdark/15 text-twc19-accdark cursor-pointer shadow-[0_2px_6px_oklch(0_0_0/0.04)] transition-[background,border-color] duration-200 hover:bg-twc19-acc/6 hover:border-twc19-acc/24 focus-visible:outline-2 focus-visible:outline-twc19-acc focus-visible:outline-offset-2">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
        </button>
      </div>

      <div class="flex items-center gap-2 pt-2.5 border-t border-dashed border-black/8">
        <div aria-hidden="true" class="flex">
          <span class="size-5 rounded-full border-[1.5px] border-white shadow-[0_0_0_1px_oklch(0_0_0/0.06)] [background:linear-gradient(135deg,#f472b6,#ec4899)]"></span>
          <span class="size-5 -ml-1.5 rounded-full border-[1.5px] border-white shadow-[0_0_0_1px_oklch(0_0_0/0.06)] [background:linear-gradient(135deg,#60a5fa,#3b82f6)]"></span>
          <span class="size-5 -ml-1.5 rounded-full border-[1.5px] border-white shadow-[0_0_0_1px_oklch(0_0_0/0.06)] [background:linear-gradient(135deg,#34d399,#10b981)]"></span>
        </div>
        <span class="text-[10.5px] text-twc19-muted"><strong class="font-extrabold text-twc19-red">2,847</strong> reserving now &middot; ships Mar 12</span>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc19-bg: #f5f0e8;
  --color-twc19-bg: oklch(0.95 0.012 85);
  --color-twc19-ink: #1a1a1a;
  --color-twc19-ink: oklch(0.21 0.005 270);
  --color-twc19-ink2: #4b4b57;
  --color-twc19-ink2: oklch(0.4 0.015 280);
  --color-twc19-muted: #6b6b7c;
  --color-twc19-muted: oklch(0.51 0.02 285);
  --color-twc19-dim: #a1a1aa;
  --color-twc19-dim: oklch(0.7 0.01 285);
  --color-twc19-acc: #ea580c;
  --color-twc19-acc: oklch(0.62 0.19 45);
  --color-twc19-accink: #9a3412;
  --color-twc19-accink: oklch(0.44 0.15 42);
  --color-twc19-accdark: #7c2d12;
  --color-twc19-accdark: oklch(0.37 0.12 42);
  --color-twc19-ring: #78350f;
  --color-twc19-ring: oklch(0.38 0.1 55);
  --color-twc19-red: #dc2626;
  --color-twc19-red: oklch(0.58 0.22 25);
  --color-twc19-amber: #f59e0b;
  --color-twc19-amber: oklch(0.78 0.16 70);
  --color-twc19-amberink: #92400e;
  --color-twc19-amberink: oklch(0.44 0.12 55);
  --color-twc19-green: #84cc16;
  --color-twc19-green: oklch(0.77 0.2 130);
  --color-twc19-greenink: #365314;
  --color-twc19-greenink: oklch(0.38 0.11 130);
  --font-twc19-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc19-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --animate-twc19-spin: twc19-spin 30s linear infinite;
  --animate-twc19-blink: twc19-blink 1.4s ease-in-out infinite;
}

@keyframes twc19-spin {
  to {
    transform: rotate(360deg);
  }
}

@keyframes twc19-blink {
  0%,
    100% {
    opacity: 1;
    transform: scale(1);
  }

  50% {
    opacity: 0.5;
    transform: scale(0.8);
  }
}

.twc-19 {
  width: 100%;
  min-height: 100svh;
}
```
