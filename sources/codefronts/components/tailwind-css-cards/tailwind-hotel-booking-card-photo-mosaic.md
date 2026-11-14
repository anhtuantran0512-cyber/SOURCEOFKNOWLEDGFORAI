---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-hotel-booking-card-photo-mosaic/"
title: "Tailwind Hotel Booking Card with Photo Mosaic & Price Breakdown"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "A four-cell photo mosaic over a booking panel: amenity chips, a check-in/check-out/guests strip, an itemised price breakdown that ends in a total, and a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Hotel Booking Card with Photo Mosaic & Price Breakdown
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-hotel-booking-card-photo-mosaic/

A four-cell photo mosaic over a booking panel: amenity chips, a check-in/check-out/guests strip, an itemised price breakdown that ends in a total, and a reserve CTA. The port's win is the mosaic &mdash; four cells, four spans and four asymmetric corner sets, each declared on the cell it shapes instead of in four look-alike rules.
## HTML
```html
<section class="twc-05 w-full min-h-svh flex items-center justify-center px-5 py-9 bg-twc05-bg [background-image:radial-gradient(ellipse_at_20%_15%,oklch(0.68_0.2_350/0.06),transparent_45%),radial-gradient(ellipse_at_80%_85%,oklch(0.48_0.09_185/0.06),transparent_45%),linear-gradient(180deg,#e8f2ef_0%,#cde0d9_100%)] font-twc05-sans" aria-label="Hotel booking">

  <article class="w-full max-w-[460px] overflow-hidden rounded-3xl bg-white border border-black/6 shadow-[0_30px_60px_-30px_oklch(0.4_0.06_175/0.28),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow] duration-300 hover:-translate-y-[3px] hover:shadow-[0_40px_80px_-30px_oklch(0.4_0.06_175/0.38)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">

    <div class="grid grid-cols-[1.7fr_1fr_1fr] grid-rows-2 gap-[3px] h-65 p-[3px] bg-twc05-seam">
      <div class="group/cell relative row-span-2 min-w-0 min-h-0 overflow-hidden rounded-[20px_6px_6px_20px]">
        <img src="https://images.unsplash.com/photo-1566073771259-6a8506099945?w=1000&q=80&auto=format&fit=crop" alt="The Everly hotel exterior" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover block transition-transform duration-500 ease-out group-hover/cell:scale-105 motion-reduce:transition-none motion-reduce:group-hover/cell:scale-100">
        <span class="absolute top-3 left-3 z-2 inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-white/95 backdrop-blur-[6px] border border-white/60 text-twc05-redink font-twc05-mono text-[9px] font-extrabold tracking-[0.14em] shadow-[0_2px_5px_oklch(0_0_0/0.14)]">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor" class="text-twc05-red" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
          SUPERHOST
        </span>
        <button type="button" aria-label="Add The Everly to wishlist" class="absolute top-3 right-3 z-2 inline-flex items-center justify-center size-11 rounded-full bg-white/95 backdrop-blur-[6px] border border-black/6 text-twc05-ink cursor-pointer transition-[color,transform] duration-200 hover:text-twc05-red hover:scale-108 focus-visible:outline-2 focus-visible:outline-twc05-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 1 0-7.8 7.8L12 21.1l8.8-8.7a5.5 5.5 0 0 0 0-7.8z"/></svg>
        </button>
      </div>
      <div class="group/cell relative min-w-0 min-h-0 overflow-hidden rounded-[6px_20px_6px_6px]">
        <img src="https://images.unsplash.com/photo-1590490360182-c33d57733427?w=400&q=80&auto=format&fit=crop" alt="Hotel room interior" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover block transition-transform duration-500 ease-out group-hover/cell:scale-105 motion-reduce:transition-none motion-reduce:group-hover/cell:scale-100">
      </div>
      <div class="group/cell relative min-w-0 min-h-0 overflow-hidden rounded-md">
        <img src="https://images.unsplash.com/photo-1618773928121-c32242e63f39?w=400&q=80&auto=format&fit=crop" alt="Hotel bathroom" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover block transition-transform duration-500 ease-out group-hover/cell:scale-105 motion-reduce:transition-none motion-reduce:group-hover/cell:scale-100">
      </div>
      <button type="button" class="group/cell relative col-span-2 min-w-0 min-h-0 overflow-hidden rounded-[6px_6px_20px_6px] cursor-pointer border-0 p-0 focus-visible:outline-2 focus-visible:outline-twc05-acc focus-visible:outline-offset-2">
        <img src="https://images.unsplash.com/photo-1584132967334-10e028bd69f7?w=400&q=80&auto=format&fit=crop" alt="" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover block transition-transform duration-500 ease-out group-hover/cell:scale-105 motion-reduce:transition-none motion-reduce:group-hover/cell:scale-100">
        <span class="absolute inset-0 z-2 flex items-center justify-center gap-1.5 bg-black/50 backdrop-blur-[2px] text-white text-[11px] font-extrabold transition-colors duration-200 group-hover/cell:bg-black/60">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
          View all 32 photos
        </span>
      </button>
    </div>

    <div class="flex flex-col gap-3.5 px-5 pt-4.5 pb-5">

      <div class="flex items-start justify-between gap-3">
        <div class="min-w-0">
          <div class="inline-flex items-center gap-1.5 mb-1">
            <span class="font-twc05-mono text-[9.5px] font-extrabold tracking-[0.14em] text-twc05-teal">BOUTIQUE HOTEL</span>
            <span aria-hidden="true" class="text-twc05-hair">&middot;</span>
            <span class="text-[10.5px] font-bold text-twc05-muted">Shibuya</span>
          </div>
          <h3 class="m-0 mb-1 text-xl font-extrabold tracking-[-0.025em] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">The Everly, Tokyo</h3>
          <p class="inline-flex items-center gap-1 m-0 text-[11.5px] text-twc05-muted">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none text-twc05-teal"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            0.4 mi from Shibuya Crossing
          </p>
        </div>
        <div class="flex flex-none flex-col items-end gap-1 min-w-22 px-2.5 py-2 rounded-xl [background:linear-gradient(180deg,#f0fdf4_0%,#dcfce7_100%)] border border-twc05-teal/16">
          <span class="text-xl/none font-extrabold tracking-[-0.03em] text-twc05-teal [font-variant-numeric:tabular-nums]">4.9<span class="text-[10px] font-bold text-twc05-greenink"> / 5</span></span>
          <div aria-hidden="true" class="w-15 h-[3px] rounded-sm overflow-hidden bg-twc05-teal/15">
            <span class="block w-[92%] h-full rounded-sm [background:linear-gradient(90deg,#14b8a6,#0f766e)]"></span>
          </div>
          <span class="text-[9.5px] font-bold text-twc05-teal [font-variant-numeric:tabular-nums]">2,847 reviews</span>
        </div>
      </div>

      <ul class="flex flex-wrap gap-1.5 list-none m-0 p-0">
        <li class="inline-flex items-center gap-1 px-2 py-1 rounded-full bg-twc05-teal/8 border border-twc05-teal/20 text-[10.5px] font-bold text-twc05-teal">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12a10 10 0 0 1 14 0"/><path d="M8.5 15.5a5 5 0 0 1 7 0"/><line x1="12" y1="19" x2="12" y2="19"/></svg>
          Wi-Fi
        </li>
        <li class="inline-flex items-center gap-1 px-2 py-1 rounded-full bg-twc05-teal/8 border border-twc05-teal/20 text-[10.5px] font-bold text-twc05-teal">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12h20M2 8h20M2 16h20"/></svg>
          Pool
        </li>
        <li class="inline-flex items-center gap-1 px-2 py-1 rounded-full bg-twc05-teal/8 border border-twc05-teal/20 text-[10.5px] font-bold text-twc05-teal">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>
          Breakfast
        </li>
        <li class="inline-flex items-center gap-1 px-2 py-1 rounded-full bg-twc05-teal/8 border border-twc05-teal/20 text-[10.5px] font-bold text-twc05-teal">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M8 21V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v16"/></svg>
          Gym
        </li>
        <li class="inline-flex items-center px-2 py-1 rounded-full border border-black/10 text-[10.5px] font-bold text-twc05-muted">+8 more</li>
      </ul>

      <div class="grid grid-cols-[1fr_20px_1fr_1fr] items-center gap-2 px-3 py-2.5 rounded-xl [background:linear-gradient(180deg,#fafafd_0%,#f4f4f0_100%)] border border-black/5">
        <div class="flex flex-col gap-px min-w-0">
          <span class="font-twc05-mono text-[8.5px] font-extrabold tracking-[0.12em] uppercase text-twc05-dim">Check-in</span>
          <span class="text-[12.5px] font-extrabold tracking-[-0.01em] text-twc05-ink [font-variant-numeric:tabular-nums]">Jul 12</span>
        </div>
        <div aria-hidden="true" class="flex items-center justify-center text-twc05-hair">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
        </div>
        <div class="flex flex-col gap-px min-w-0">
          <span class="font-twc05-mono text-[8.5px] font-extrabold tracking-[0.12em] uppercase text-twc05-dim">Check-out</span>
          <span class="text-[12.5px] font-extrabold tracking-[-0.01em] text-twc05-ink [font-variant-numeric:tabular-nums]">Jul 15</span>
        </div>
        <div class="flex flex-col gap-px min-w-0">
          <span class="font-twc05-mono text-[8.5px] font-extrabold tracking-[0.12em] uppercase text-twc05-dim">Guests</span>
          <span class="text-[12.5px] font-extrabold tracking-[-0.01em] text-twc05-ink [font-variant-numeric:tabular-nums]">2 adults</span>
        </div>
      </div>

      <div class="px-3.5 py-3 rounded-xl [background:linear-gradient(180deg,#fdfef9_0%,#f0f9f5_100%)] border border-twc05-teal/15">
        <div class="flex flex-col gap-1">
          <div class="flex items-center justify-between text-[11.5px] text-twc05-ink2 [font-variant-numeric:tabular-nums]"><span>$184 &times; 3 nights</span><span>$552</span></div>
          <div class="flex items-center justify-between text-[11.5px] text-twc05-ink2 [font-variant-numeric:tabular-nums]"><span>Cleaning fee</span><span>$32</span></div>
          <div class="flex items-center justify-between text-[11.5px] font-bold text-twc05-greenink [font-variant-numeric:tabular-nums]"><span>Weekend discount</span><span>&minus;$24</span></div>
          <div class="flex items-center justify-between pt-2 mt-1 border-t border-dashed border-black/10 text-sm font-extrabold tracking-[-0.01em] text-twc05-ink [font-variant-numeric:tabular-nums]"><span>Total (USD)</span><span>$560</span></div>
        </div>
        <div class="inline-flex items-center gap-1.5 mt-2 text-[10.5px] font-bold text-twc05-greenink">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
          Free cancellation until Jul 10
        </div>
      </div>

      <div class="flex items-center justify-between gap-3 pt-1">
        <div class="inline-flex items-center gap-1.5 text-[11px] text-twc05-muted">
          <span aria-hidden="true" class="size-1.5 rounded-full bg-twc05-red shadow-[0_0_8px_oklch(0.58_0.22_25)] animate-twc05-blink motion-reduce:animate-none"></span>
          <strong class="font-extrabold text-twc05-red">17 people</strong> looking now
        </div>
        <button type="button" class="inline-flex items-center gap-1.5 min-h-11 px-5 rounded-full border-0 cursor-pointer text-[13px] font-extrabold tracking-[-0.01em] text-white [background:linear-gradient(180deg,#ec4899_0%,#be185d_100%)] shadow-[0_6px_16px_oklch(0.68_0.2_350/0.38),inset_0_0_0_1px_oklch(1_0_0/0.14)] transition-[transform,box-shadow] duration-200 hover:-translate-y-0.5 hover:shadow-[0_10px_22px_oklch(0.68_0.2_350/0.48),inset_0_0_0_1px_oklch(1_0_0/0.2)] focus-visible:outline-2 focus-visible:outline-twc05-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
          Reserve
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
        </button>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc05-bg: #e8f2ef;
  --color-twc05-bg: oklch(0.95 0.015 175);
  --color-twc05-seam: #f4ede4;
  --color-twc05-seam: oklch(0.94 0.014 75);
  --color-twc05-ink: #1a1a1a;
  --color-twc05-ink: oklch(0.21 0.005 270);
  --color-twc05-ink2: #4b4b57;
  --color-twc05-ink2: oklch(0.4 0.015 280);
  --color-twc05-muted: #6b6b7c;
  --color-twc05-muted: oklch(0.51 0.02 285);
  --color-twc05-dim: #9ca3af;
  --color-twc05-dim: oklch(0.71 0.02 265);
  --color-twc05-hair: #cbd5e1;
  --color-twc05-hair: oklch(0.85 0.02 250);
  --color-twc05-teal: #0f766e;
  --color-twc05-teal: oklch(0.48 0.09 185);
  --color-twc05-greenink: #059669;
  --color-twc05-greenink: oklch(0.56 0.13 163);
  --color-twc05-acc: #ec4899;
  --color-twc05-acc: oklch(0.68 0.2 350);
  --color-twc05-red: #dc2626;
  --color-twc05-red: oklch(0.58 0.22 25);
  --color-twc05-redink: #b91c1c;
  --color-twc05-redink: oklch(0.5 0.2 25);
  --font-twc05-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc05-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --animate-twc05-blink: twc05-blink 1.6s ease-in-out infinite;
}

@keyframes twc05-blink {
  0%,
    100% {
    opacity: 1;
    transform: scale(1);
  }

  50% {
    opacity: 0.4;
    transform: scale(0.8);
  }
}

.twc-05 {
  width: 100%;
  min-height: 100svh;
}
```
