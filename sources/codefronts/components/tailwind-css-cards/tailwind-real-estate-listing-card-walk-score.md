---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-real-estate-listing-card-walk-score/"
title: "Tailwind Real Estate Listing Card with Walk Score Rings"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "A single listing, dense with the six things a buyer scans first: price and delta, address, specs, walk and transit score rings, days on market, and the agent."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Real Estate Listing Card with Walk Score Rings
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-real-estate-listing-card-walk-score/

A single listing, dense with the six things a buyer scans first: price and delta, address, specs, walk and transit score rings, days on market, and the agent. The port's win is that six absolutely-positioned hero overlays stop being six CSS rules and become six sets of absolute offsets you can read in place.
## HTML
```html
<section class="twc-04 w-full min-h-svh flex items-center justify-center px-5 py-9 bg-twc04-bg [background-image:radial-gradient(ellipse_at_20%_15%,oklch(0.62_0.17_255/0.06),transparent_45%),radial-gradient(ellipse_at_80%_85%,oklch(0.62_0.19_45/0.05),transparent_45%),linear-gradient(180deg,#fef3e1_0%,#f4dcb3_100%)] font-twc04-sans" aria-label="Property listing">

  <article class="group/card w-full max-w-[420px] overflow-hidden rounded-[22px] bg-white border border-black/6 shadow-[0_30px_60px_-30px_oklch(0.45_0.06_75/0.28),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow] duration-300 hover:-translate-y-[3px] hover:shadow-[0_40px_80px_-30px_oklch(0.45_0.06_75/0.36)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">

    <div class="relative aspect-[5/3] overflow-hidden bg-twc04-mediabg">
      <img src="https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=1200&q=80&auto=format&fit=crop" alt="142 Elm Street exterior" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover block transition-transform duration-600 ease-out group-hover/card:scale-105 motion-reduce:transition-none motion-reduce:group-hover/card:scale-100">
      <div aria-hidden="true" class="absolute inset-0 pointer-events-none [background:linear-gradient(180deg,transparent_0%,transparent_60%,oklch(0_0_0/0.4)_100%)]"></div>

      <div class="absolute top-3 left-3 flex flex-wrap gap-1.5 max-w-[calc(100%-100px)]">
        <span class="inline-flex items-center gap-1 px-2 py-[3px] rounded-[5px] font-twc04-mono text-[9px] font-extrabold tracking-[0.14em] [background:linear-gradient(180deg,#ea580c_0%,#c2410c_100%)] text-white border border-white/15 shadow-[0_2px_5px_oklch(0.62_0.19_45/0.4)]">
          <svg width="9" height="9" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13 2 3 14h9l-1 8 10-12h-9z"/></svg>
          HOT LISTING
        </span>
        <span class="inline-flex items-center gap-1 px-2 py-[3px] rounded-[5px] font-twc04-mono text-[9px] font-extrabold tracking-[0.14em] bg-twc04-acc/92 backdrop-blur-[6px] text-white border border-white/16">
          <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 2"/></svg>
          3D TOUR
        </span>
      </div>

      <button type="button" aria-label="Save listing" class="absolute top-3 right-3 inline-flex items-center gap-1 min-h-8 pl-2 pr-2.5 rounded-full bg-white/95 backdrop-blur-[6px] border border-black/6 text-twc04-ink text-[11px] font-bold cursor-pointer transition-[color,transform] duration-200 hover:text-twc04-red hover:scale-105 focus-visible:outline-2 focus-visible:outline-twc04-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 1 0-7.8 7.8L12 21.1l8.8-8.7a5.5 5.5 0 0 0 0-7.8z"/></svg>
        <span class="font-twc04-mono text-[10px] [font-variant-numeric:tabular-nums]">1,284</span>
      </button>

      <button type="button" aria-label="Share listing" class="absolute top-14 right-3 inline-flex items-center justify-center size-11 rounded-full bg-white/95 backdrop-blur-[6px] border border-black/6 text-twc04-ink cursor-pointer transition-colors duration-200 hover:text-twc04-acc focus-visible:outline-2 focus-visible:outline-twc04-acc focus-visible:outline-offset-2">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.6" y1="13.5" x2="15.4" y2="17.5"/><line x1="15.4" y1="6.5" x2="8.6" y2="10.5"/></svg>
      </button>

      <div aria-hidden="true" class="absolute bottom-3 left-3 inline-flex items-center gap-1 pl-1.5 pr-2 py-1 rounded-full bg-black/55 backdrop-blur-[6px]">
        <span class="w-4 h-1.5 rounded-full bg-white"></span>
        <span class="size-1.5 rounded-full bg-white/40"></span>
        <span class="size-1.5 rounded-full bg-white/40"></span>
        <span class="size-1.5 rounded-full bg-white/40"></span>
        <span class="ml-1 font-twc04-mono text-[9.5px] font-bold text-white tracking-[0.02em] [font-variant-numeric:tabular-nums]">1 / 24</span>
      </div>

      <div class="absolute bottom-3 right-3 inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-white/95 backdrop-blur-[6px] border border-white/60 text-twc04-greenink text-[10px] font-bold">
        <span aria-hidden="true" class="size-[5px] rounded-full bg-twc04-green shadow-[0_0_6px_oklch(0.72_0.15_163)] animate-twc04-pulse motion-reduce:animate-none"></span>
        3 days on market
      </div>
    </div>

    <div class="flex flex-col gap-3.5 px-5 pt-4.5 pb-5">

      <div class="flex items-start justify-between gap-3 px-3.5 py-3 rounded-2xl [background:linear-gradient(180deg,#fafafd_0%,#f4f4f0_100%)] border border-black/5">
        <div>
          <div class="flex items-baseline gap-2 mb-1">
            <span class="text-2xl font-extrabold tracking-[-0.03em] [font-variant-numeric:tabular-nums] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">$1,285,000</span>
            <span class="inline-flex items-center gap-0.5 px-[7px] py-0.5 rounded-full bg-twc04-green/15 font-twc04-mono text-[10px] font-extrabold text-twc04-greenink">
              <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>
              &minus;$15K
            </span>
          </div>
          <p class="m-0 text-[10.5px] text-twc04-muted [font-variant-numeric:tabular-nums]">Zestimate&reg; $1.31M &middot; $758/mo est.</p>
        </div>
        <div class="flex flex-col items-end gap-px">
          <span class="font-twc04-mono text-[9px] font-extrabold tracking-[0.1em] uppercase text-twc04-dim">Mo. payment</span>
          <span class="text-[15px] font-extrabold tracking-[-0.02em] text-twc04-ink [font-variant-numeric:tabular-nums]">$7,842</span>
        </div>
      </div>

      <address class="not-italic">
        <h4 class="m-0 mb-0.5 text-base font-extrabold tracking-[-0.015em] text-twc04-ink">142 Elm Street, Unit 3B</h4>
        <p class="m-0 text-[12.5px] text-twc04-muted2">Brooklyn Heights, NY 11201</p>
      </address>

      <ul class="flex flex-wrap gap-y-1.5 gap-x-2.5 list-none m-0 p-0">
        <li class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-full bg-white/70 border border-black/5 text-xs text-twc04-ink2 [font-variant-numeric:tabular-nums]">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none text-twc04-dim"><path d="M2 20V8h20v12"/><path d="M2 16h20"/><rect x="6" y="10" width="4" height="4"/><rect x="14" y="10" width="4" height="4"/></svg>
          <strong class="font-extrabold text-twc04-ink">3</strong> bed
        </li>
        <li class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-full bg-white/70 border border-black/5 text-xs text-twc04-ink2 [font-variant-numeric:tabular-nums]">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none text-twc04-dim"><path d="M9 6V4a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/><path d="M4 10h16v4a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5z"/></svg>
          <strong class="font-extrabold text-twc04-ink">2</strong> bath
        </li>
        <li class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-full bg-white/70 border border-black/5 text-xs text-twc04-ink2 [font-variant-numeric:tabular-nums]">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none text-twc04-dim"><path d="M3 3h18v18H3z"/><path d="M3 12h18M12 3v18"/></svg>
          <strong class="font-extrabold text-twc04-ink">1,240</strong> sqft
        </li>
        <li class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-full bg-white/70 border border-black/5 text-xs text-twc04-ink2 [font-variant-numeric:tabular-nums]">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none text-twc04-dim"><path d="M12 2s8 4 8 10-8 10-8 10S4 18 4 12s8-10 8-10z"/></svg>
          Built <strong class="font-extrabold text-twc04-ink">1899</strong>
        </li>
      </ul>

      <div class="grid grid-cols-2 gap-2 p-3 rounded-2xl [background:linear-gradient(180deg,#fff_0%,#fafaf7_100%)] border border-black/5">
        <div class="flex items-center gap-2.5">
          <div class="relative flex-none size-8.5">
            <svg width="34" height="34" viewBox="0 0 36 36" aria-hidden="true">
              <circle cx="18" cy="18" r="15" fill="none" stroke="oklch(0 0 0 / 0.06)" stroke-width="3"/>
              <circle cx="18" cy="18" r="15" fill="none" stroke="#059669" stroke-width="3" stroke-dasharray="87 100" stroke-linecap="round" transform="rotate(-90 18 18)"/>
            </svg>
            <span class="absolute inset-0 flex items-center justify-center font-twc04-mono text-[11px] font-extrabold tracking-[-0.02em] text-twc04-ink [font-variant-numeric:tabular-nums]">92</span>
          </div>
          <div class="flex flex-col min-w-0">
            <span class="text-[11px] font-extrabold tracking-[-0.01em] text-twc04-ink">Walk score</span>
            <span class="text-[10px] text-twc04-muted">Walker's paradise</span>
          </div>
        </div>
        <div class="flex items-center gap-2.5">
          <div class="relative flex-none size-8.5">
            <svg width="34" height="34" viewBox="0 0 36 36" aria-hidden="true">
              <circle cx="18" cy="18" r="15" fill="none" stroke="oklch(0 0 0 / 0.06)" stroke-width="3"/>
              <circle cx="18" cy="18" r="15" fill="none" stroke="#3b82f6" stroke-width="3" stroke-dasharray="78 100" stroke-linecap="round" transform="rotate(-90 18 18)"/>
            </svg>
            <span class="absolute inset-0 flex items-center justify-center font-twc04-mono text-[11px] font-extrabold tracking-[-0.02em] text-twc04-ink [font-variant-numeric:tabular-nums]">78</span>
          </div>
          <div class="flex flex-col min-w-0">
            <span class="text-[11px] font-extrabold tracking-[-0.01em] text-twc04-ink">Transit</span>
            <span class="text-[10px] text-twc04-muted">Excellent</span>
          </div>
        </div>
      </div>

      <div class="flex max-[400px]:flex-col max-[400px]:items-stretch items-center justify-between gap-2 pt-3 border-t border-dashed border-black/10">
        <div class="flex items-center gap-2 min-w-0">
          <span aria-hidden="true" class="flex flex-none items-center justify-center size-8 rounded-full border-[1.5px] border-white [background:linear-gradient(135deg,#ea580c,#7c2d12)] text-white text-[11px] font-extrabold shadow-[0_1px_3px_oklch(0_0_0/0.1)]">SC</span>
          <div class="flex flex-col min-w-0">
            <span class="inline-flex items-center gap-1 text-xs font-extrabold text-twc04-ink">
              Sarah Chen
              <svg role="img" aria-label="Verified agent" width="11" height="11" viewBox="0 0 24 24" fill="none" class="flex-none"><path d="M12 2 L14 4 L17 3 L18 6 L21 7 L20 10 L22 12 L20 14 L21 17 L18 18 L17 21 L14 20 L12 22 L10 20 L7 21 L6 18 L3 17 L4 14 L2 12 L4 10 L3 7 L6 6 L7 3 L10 4 Z" fill="#3b82f6"/><path d="M9 12 L11 14 L15 10" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
            <span class="text-[10px] font-bold text-twc04-greenink">Compass &middot; Responds &lt; 1h</span>
          </div>
        </div>
        <div class="flex flex-none gap-1.5">
          <button type="button" class="inline-flex items-center justify-center gap-1 min-h-11 px-3.5 rounded-full border-0 cursor-pointer text-[11.5px] font-bold text-twc04-ink bg-black/4 transition-[background,transform] duration-200 hover:bg-black/8 hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-twc04-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            Tour
          </button>
          <button type="button" class="inline-flex items-center justify-center gap-1 min-h-11 px-3.5 rounded-full border-0 cursor-pointer text-[11.5px] font-bold text-white [background:linear-gradient(180deg,#1e1e2c_0%,#06070c_100%)] shadow-[0_3px_10px_oklch(0_0_0/0.22),inset_0_0_0_1px_oklch(1_0_0/0.14)] transition-[background,transform] duration-200 hover:[background:linear-gradient(180deg,#3b82f6_0%,#1e40af_100%)] hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-twc04-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
            Contact agent
          </button>
        </div>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc04-bg: #fef3e1;
  --color-twc04-bg: oklch(0.96 0.03 80);
  --color-twc04-mediabg: #f4dcb3;
  --color-twc04-mediabg: oklch(0.9 0.05 82);
  --color-twc04-ink: #1a1a1a;
  --color-twc04-ink: oklch(0.21 0.005 270);
  --color-twc04-ink2: #4b4b57;
  --color-twc04-ink2: oklch(0.4 0.015 280);
  --color-twc04-muted: #6b6b7c;
  --color-twc04-muted: oklch(0.51 0.02 285);
  --color-twc04-muted2: #6b6459;
  --color-twc04-muted2: oklch(0.49 0.015 75);
  --color-twc04-dim: #9ca3af;
  --color-twc04-dim: oklch(0.71 0.02 265);
  --color-twc04-acc: #3b82f6;
  --color-twc04-acc: oklch(0.62 0.17 255);
  --color-twc04-green: #10b981;
  --color-twc04-green: oklch(0.72 0.15 163);
  --color-twc04-greenink: #059669;
  --color-twc04-greenink: oklch(0.56 0.13 163);
  --color-twc04-red: #dc2626;
  --color-twc04-red: oklch(0.58 0.22 25);
  --font-twc04-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc04-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --animate-twc04-pulse: twc04-pulse 2s ease-in-out infinite;
}

@keyframes twc04-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(1.4);
    opacity: 0.7;
  }
}

.twc-04 {
  width: 100%;
  min-height: 100svh;
}
```
