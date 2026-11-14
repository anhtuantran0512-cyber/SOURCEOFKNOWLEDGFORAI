---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-recipe-card-cook-time-meta-grid/"
title: "Tailwind Recipe Card with Cook-Time Meta Grid"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "An editorial recipe index: one hero dish with a four-cell Total / Serves / Level / Calories meta grid, diet chips and a cook-mode bar that rises on hover,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Recipe Card with Cook-Time Meta Grid
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-recipe-card-cook-time-meta-grid/

An editorial recipe index: one hero dish with a four-cell Total / Serves / Level / Calories meta grid, diet chips and a cook-mode bar that rises on hover, beside two stacked quick picks. The port's win is line-clamp-2 &mdash; the four-declaration -webkit-box ritual becomes one utility that cannot be half-written.
## HTML
```html
<section class="twc-03 w-full min-h-svh flex flex-col items-center justify-center gap-4 px-5 py-9 bg-twc03-bg [background-image:radial-gradient(ellipse_at_20%_15%,oklch(0.55_0.17_42/0.06),transparent_45%),radial-gradient(ellipse_at_80%_85%,oklch(0.52_0.15_35/0.06),transparent_45%),linear-gradient(180deg,#fbeee2_0%,#f2d8bf_100%)] font-twc03-sans" aria-label="Recipes">

  <header class="w-full max-w-[780px]">
    <div class="inline-flex items-center gap-1.5 mb-2.5 px-2.5 py-1 rounded-full font-twc03-mono text-[10px] font-extrabold tracking-[0.14em] text-twc03-accink bg-twc03-acc/8 border border-twc03-acc/20">
      <span aria-hidden="true" class="size-[5px] rounded-full bg-twc03-acc shadow-[0_0_8px_oklch(0.55_0.17_42/0.5)] animate-twc03-pulse motion-reduce:animate-none"></span>
      TODAY'S PICK &middot; WEEKNIGHT
    </div>
    <div class="flex max-sm:flex-col max-sm:items-start items-center justify-between gap-3">
      <h3 class="m-0 text-xl font-extrabold tracking-[-0.025em] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">Cook something great tonight</h3>
      <a href="#all" class="inline-flex items-center gap-1 min-h-11 px-3 rounded-full no-underline text-xs font-bold text-twc03-accink bg-white/60 transition-[color,background] duration-200 hover:text-twc03-accdark hover:bg-white/90 focus-visible:outline-2 focus-visible:outline-twc03-acc focus-visible:outline-offset-2">
        Explore all
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
    </div>
  </header>

  <div class="w-full max-w-[780px] grid grid-cols-[minmax(0,1.4fr)_minmax(0,1fr)] max-[700px]:grid-cols-1 max-[700px]:max-w-[360px] gap-3.5 items-stretch">

    <article class="group/card flex flex-col overflow-hidden rounded-twc03-card bg-white border border-black/6 shadow-[0_12px_30px_-18px_oklch(0.42_0.1_45/0.2),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow,border-color] duration-300 hover:-translate-y-[3px] hover:border-twc03-acc/25 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="relative aspect-[4/3] overflow-hidden bg-twc03-mediabg">
        <img src="https://images.unsplash.com/photo-1580476262798-bddd9f4b7369?w=1000&q=80&auto=format&fit=crop" alt="Miso-glazed salmon with sesame rice" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover block transition-transform duration-500 ease-out group-hover/card:scale-105 motion-reduce:transition-none motion-reduce:group-hover/card:scale-100">
        <div class="absolute top-2.5 left-2.5 flex flex-wrap gap-1.5 max-w-[calc(100%-60px)]">
          <span class="inline-flex items-center gap-1 px-2 py-[3px] rounded-[5px] font-twc03-mono text-[9px] font-extrabold tracking-[0.14em] [background:linear-gradient(180deg,#fef3c7,#fde68a)] text-twc03-amberdeep border border-twc03-amberink/25 shadow-[0_2px_5px_oklch(0.78_0.15_70/0.3)]">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            EDITOR'S PICK
          </span>
        </div>
        <button type="button" aria-label="Save Miso-Glazed Salmon recipe" class="absolute top-2.5 right-2.5 inline-flex items-center gap-1 min-h-8 pl-1.5 pr-2 rounded-full bg-white/92 backdrop-blur-[6px] border border-black/6 text-twc03-ink text-[10.5px] font-bold cursor-pointer transition-[color,background,transform] duration-200 hover:text-twc03-acc hover:bg-white hover:scale-105 focus-visible:outline-2 focus-visible:outline-twc03-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
          <span class="font-twc03-mono text-[10px] [font-variant-numeric:tabular-nums]">8.2k</span>
        </button>
        <div aria-hidden="true" class="absolute bottom-2.5 left-3 inline-flex items-center gap-1.5 px-2 py-[3px] rounded-full bg-white/92 backdrop-blur-[6px] border border-black/6 text-twc03-greenink text-[10px] font-bold">
          <span class="size-[5px] rounded-full bg-twc03-green shadow-[0_0_6px_oklch(0.72_0.15_163)] animate-twc03-pulse motion-reduce:animate-none"></span>
          You have 9/12 ingredients
        </div>
        <div class="absolute bottom-11 left-3 right-3 opacity-0 translate-y-2.5 pointer-events-none transition-[opacity,transform] duration-250 group-hover/card:opacity-100 group-hover/card:translate-y-0 group-hover/card:pointer-events-auto group-focus-within/card:opacity-100 group-focus-within/card:translate-y-0 group-focus-within/card:pointer-events-auto [@media(hover:none)]:opacity-100 [@media(hover:none)]:translate-y-0 [@media(hover:none)]:pointer-events-auto motion-reduce:transition-none">
          <button type="button" class="inline-flex w-full items-center justify-center gap-1.5 min-h-11 px-3 rounded-[10px] bg-twc03-ink/92 backdrop-blur-[8px] border border-white/15 text-white text-xs font-bold cursor-pointer transition-colors duration-200 hover:bg-twc03-ink focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
            Start cook mode
          </button>
        </div>
      </div>
      <div class="flex flex-col gap-2.5 px-4.5 py-4">
        <div class="flex flex-wrap items-center gap-1.5">
          <span class="inline-flex items-center px-2 py-[3px] rounded-full font-twc03-mono text-[9px] font-extrabold tracking-[0.14em] uppercase text-twc03-accink bg-twc03-acc/10 border border-twc03-acc/20">MAIN &middot; JAPANESE</span>
          <span class="inline-flex items-center px-2 py-[3px] rounded-full font-twc03-mono text-[9px] font-extrabold tracking-[0.14em] uppercase text-twc03-greenink bg-twc03-green/10 border border-twc03-green/25">HIGH-PROTEIN</span>
          <span class="inline-flex items-center px-2 py-[3px] rounded-full font-twc03-mono text-[9px] font-extrabold tracking-[0.14em] uppercase text-twc03-amberink bg-twc03-amber/10 border border-twc03-amber/25">GLUTEN-FREE</span>
        </div>
        <div class="flex items-start justify-between gap-2.5">
          <h4 class="m-0 text-[17px]/[1.3] font-extrabold tracking-[-0.02em] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">Miso-Glazed Salmon with Sesame Rice</h4>
          <div role="img" aria-label="Rated 4.9 out of 5, 1,247 reviews" class="inline-flex flex-none items-center gap-1 px-2 py-[3px] rounded-full bg-twc03-amber/10 border border-twc03-amber/20">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" class="text-twc03-amber" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            <span class="font-twc03-mono text-[11px] font-extrabold text-twc03-amberink [font-variant-numeric:tabular-nums]">4.9</span>
            <span class="text-[10px] font-semibold text-twc03-dim">(1,247)</span>
          </div>
        </div>
        <p class="m-0 text-[12.5px]/[1.5] text-twc03-muted line-clamp-2">Sweet-savory miso glaze on flaky salmon, crispy sesame rice, quick pickled cucumber. On the table in 25.</p>
        <div class="grid grid-cols-4 max-[700px]:grid-cols-2 gap-2 p-3 rounded-xl [background:linear-gradient(180deg,#faf7f2_0%,#f5eee2_100%)] border border-black/4">
          <div class="flex items-center gap-2 min-w-0">
            <div class="inline-flex flex-none items-center justify-center size-6.5 rounded-lg bg-twc03-indigo/12 text-twc03-indigoink"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
            <div class="flex flex-col min-w-0">
              <span class="font-twc03-mono text-[8.5px] font-extrabold tracking-[0.12em] uppercase text-twc03-dim">Total</span>
              <span class="text-xs font-extrabold tracking-[-0.01em] text-twc03-ink [font-variant-numeric:tabular-nums]">25 min</span>
            </div>
          </div>
          <div class="flex items-center gap-2 min-w-0">
            <div class="inline-flex flex-none items-center justify-center size-6.5 rounded-lg bg-twc03-green/15 text-twc03-greenink"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
            <div class="flex flex-col min-w-0">
              <span class="font-twc03-mono text-[8.5px] font-extrabold tracking-[0.12em] uppercase text-twc03-dim">Serves</span>
              <span class="text-xs font-extrabold tracking-[-0.01em] text-twc03-ink [font-variant-numeric:tabular-nums]">4</span>
            </div>
          </div>
          <div class="flex items-center gap-2 min-w-0">
            <div class="inline-flex flex-none items-center justify-center size-6.5 rounded-lg bg-twc03-amber/15 text-twc03-amberink"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 15 12 9 18 15"/></svg></div>
            <div class="flex flex-col min-w-0">
              <span class="font-twc03-mono text-[8.5px] font-extrabold tracking-[0.12em] uppercase text-twc03-dim">Level</span>
              <span class="text-xs font-extrabold tracking-[-0.01em] text-twc03-ink">Medium</span>
            </div>
          </div>
          <div class="flex items-center gap-2 min-w-0">
            <div class="inline-flex flex-none items-center justify-center size-6.5 rounded-lg bg-twc03-red/12 text-twc03-redink"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2s4 4 4 8a4 4 0 0 1-8 0c0-1 1-2 1-2s2 2 2 5a5 5 0 0 0 6 0"/></svg></div>
            <div class="flex flex-col min-w-0">
              <span class="font-twc03-mono text-[8.5px] font-extrabold tracking-[0.12em] uppercase text-twc03-dim">Calories</span>
              <span class="text-xs font-extrabold tracking-[-0.01em] text-twc03-ink [font-variant-numeric:tabular-nums]">480</span>
            </div>
          </div>
        </div>
        <div class="flex items-center justify-between gap-2 pt-2 border-t border-dashed border-black/10">
          <div class="flex items-center gap-2">
            <span aria-hidden="true" class="flex items-center justify-center size-7 rounded-full border-[1.5px] border-white [background:linear-gradient(135deg,#c2410c,#7c2d12)] text-white text-[10px] font-extrabold shadow-[0_1px_3px_oklch(0_0_0/0.1)]">SN</span>
            <div class="flex flex-col min-w-0">
              <span class="inline-flex items-center gap-1 text-[11.5px] font-bold text-twc03-ink">
                Sana Novak
                <svg role="img" aria-label="Verified chef" width="11" height="11" viewBox="0 0 24 24" fill="none" class="flex-none"><path d="M12 2 L14 4 L17 3 L18 6 L21 7 L20 10 L22 12 L20 14 L21 17 L18 18 L17 21 L14 20 L12 22 L10 20 L7 21 L6 18 L3 17 L4 14 L2 12 L4 10 L3 7 L6 6 L7 3 L10 4 Z" fill="#c2410c"/><path d="M9 12 L11 14 L15 10" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </span>
              <span class="text-[10px] text-twc03-dim">Test Kitchen &middot; 4h ago</span>
            </div>
          </div>
          <a href="#recipe" class="inline-flex items-center gap-1 min-h-11 px-3.5 rounded-full no-underline text-[11.5px] font-bold text-white [background:linear-gradient(180deg,#1e1e2c_0%,#06070c_100%)] shadow-[0_3px_10px_oklch(0_0_0/0.22),inset_0_0_0_1px_oklch(1_0_0/0.14)] transition-[transform,background] duration-200 hover:-translate-y-px hover:[background:linear-gradient(180deg,#c2410c_0%,#7c2d12_100%)] focus-visible:outline-2 focus-visible:outline-twc03-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
            View recipe
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
        </div>
      </div>
    </article>

    <div class="flex flex-col gap-3.5 min-w-0">

      <article class="group/card flex-1 flex flex-col overflow-hidden rounded-twc03-card bg-white border border-black/6 shadow-[0_12px_30px_-18px_oklch(0.42_0.1_45/0.2),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow,border-color] duration-300 hover:-translate-y-[3px] hover:border-twc03-acc/25 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div class="relative aspect-video overflow-hidden bg-twc03-mediabg">
          <img src="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600&q=80&auto=format&fit=crop" alt="Herby green shakshuka in a skillet" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover block transition-transform duration-500 ease-out group-hover/card:scale-105 motion-reduce:transition-none motion-reduce:group-hover/card:scale-100">
          <span class="absolute top-2 left-2 inline-flex items-center gap-1 px-2 py-[3px] rounded-[5px] font-twc03-mono text-[9px] font-extrabold tracking-[0.14em] [background:linear-gradient(180deg,#d1fae5,#a7f3d0)] text-twc03-greenink border border-twc03-greenink/20">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7z"/></svg>
            VEGAN
          </span>
          <button type="button" aria-label="Save Herby Green Shakshuka recipe" class="absolute top-1.5 right-1.5 inline-flex items-center justify-center size-11 rounded-full bg-white/92 backdrop-blur-[6px] border border-black/6 text-twc03-ink cursor-pointer transition-[color,background,transform] duration-200 hover:text-twc03-acc hover:bg-white hover:scale-105 focus-visible:outline-2 focus-visible:outline-twc03-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
          </button>
          <span class="absolute bottom-2 right-2 inline-flex items-center gap-1 px-[7px] py-[3px] rounded-full bg-black/55 backdrop-blur-[6px] border border-white/15 text-white text-[10px] font-bold">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            20 min
          </span>
        </div>
        <div class="flex flex-col gap-1.5 px-3.5 pt-3 pb-3.5">
          <span class="self-start font-twc03-mono text-[8.5px] font-extrabold tracking-[0.14em] text-twc03-accink">BRUNCH</span>
          <h4 class="m-0 text-[13px]/[1.3] font-extrabold tracking-[-0.015em] text-twc03-ink line-clamp-2">Herby Green Shakshuka</h4>
          <div class="self-start inline-flex items-center gap-1 px-1.5 py-0.5 rounded-full bg-twc03-amber/10 font-twc03-mono text-[10px] font-extrabold text-twc03-amberink [font-variant-numeric:tabular-nums]">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="currentColor" class="text-twc03-amber" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            4.7 &middot; <span class="font-bold text-twc03-dim">823 saves</span>
          </div>
        </div>
      </article>

      <article class="group/card flex-1 flex flex-col overflow-hidden rounded-twc03-card bg-white border border-black/6 shadow-[0_12px_30px_-18px_oklch(0.42_0.1_45/0.2),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow,border-color] duration-300 hover:-translate-y-[3px] hover:border-twc03-acc/25 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div class="relative aspect-video overflow-hidden bg-twc03-mediabg">
          <img src="https://images.unsplash.com/photo-1509365465985-25d11c17e812?w=600&q=80&auto=format&fit=crop" alt="Salted chocolate babka loaf" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover block transition-transform duration-500 ease-out group-hover/card:scale-105 motion-reduce:transition-none motion-reduce:group-hover/card:scale-100">
          <span class="absolute top-2 left-2 inline-flex items-center gap-1 px-2 py-[3px] rounded-[5px] font-twc03-mono text-[9px] font-extrabold tracking-[0.14em] bg-twc03-red/90 backdrop-blur-[6px] text-white border border-white/15 shadow-[0_2px_5px_oklch(0.58_0.22_25/0.3)]">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="17 6 12 11 8 8 3 13"/><polyline points="14 6 17 6 17 9"/></svg>
            TRENDING
          </span>
          <button type="button" aria-label="Save Salted Chocolate Babka recipe" class="absolute top-1.5 right-1.5 inline-flex items-center justify-center size-11 rounded-full bg-white/92 backdrop-blur-[6px] border border-black/6 text-twc03-ink cursor-pointer transition-[color,background,transform] duration-200 hover:text-twc03-acc hover:bg-white hover:scale-105 focus-visible:outline-2 focus-visible:outline-twc03-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
          </button>
          <span class="absolute bottom-2 right-2 inline-flex items-center gap-1 px-[7px] py-[3px] rounded-full bg-black/55 backdrop-blur-[6px] border border-white/15 text-white text-[10px] font-bold">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            2 hr
          </span>
        </div>
        <div class="flex flex-col gap-1.5 px-3.5 pt-3 pb-3.5">
          <span class="self-start font-twc03-mono text-[8.5px] font-extrabold tracking-[0.14em] text-twc03-accink">DESSERT</span>
          <h4 class="m-0 text-[13px]/[1.3] font-extrabold tracking-[-0.015em] text-twc03-ink line-clamp-2">Salted Chocolate Babka</h4>
          <div class="self-start inline-flex items-center gap-1 px-1.5 py-0.5 rounded-full bg-twc03-amber/10 font-twc03-mono text-[10px] font-extrabold text-twc03-amberink [font-variant-numeric:tabular-nums]">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="currentColor" class="text-twc03-amber" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            4.9 &middot; <span class="font-bold text-twc03-dim">2.1k saves</span>
          </div>
        </div>
      </article>

    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc03-bg: #fbeee2;
  --color-twc03-bg: oklch(0.95 0.025 70);
  --color-twc03-mediabg: #f5e6d3;
  --color-twc03-mediabg: oklch(0.93 0.03 78);
  --color-twc03-ink: #1a1a1a;
  --color-twc03-ink: oklch(0.21 0.005 270);
  --color-twc03-muted: #6b6b7c;
  --color-twc03-muted: oklch(0.51 0.02 285);
  --color-twc03-dim: #9ca3af;
  --color-twc03-dim: oklch(0.71 0.02 265);
  --color-twc03-acc: #c2410c;
  --color-twc03-acc: oklch(0.55 0.17 42);
  --color-twc03-accink: #9a3412;
  --color-twc03-accink: oklch(0.44 0.15 42);
  --color-twc03-accdark: #7c2d12;
  --color-twc03-accdark: oklch(0.37 0.12 42);
  --color-twc03-amber: #f59e0b;
  --color-twc03-amber: oklch(0.78 0.16 70);
  --color-twc03-amberink: #92400e;
  --color-twc03-amberink: oklch(0.44 0.12 55);
  --color-twc03-amberdeep: #78350f;
  --color-twc03-amberdeep: oklch(0.38 0.1 55);
  --color-twc03-green: #34d399;
  --color-twc03-green: oklch(0.78 0.14 165);
  --color-twc03-greenink: #065f46;
  --color-twc03-greenink: oklch(0.43 0.09 165);
  --color-twc03-red: #dc2626;
  --color-twc03-red: oklch(0.58 0.22 25);
  --color-twc03-redink: #b91c1c;
  --color-twc03-redink: oklch(0.5 0.2 25);
  --color-twc03-indigo: #6366f1;
  --color-twc03-indigo: oklch(0.55 0.2 275);
  --color-twc03-indigoink: #4338ca;
  --color-twc03-indigoink: oklch(0.42 0.21 275);
  --font-twc03-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc03-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --radius-twc03-card: 20px;
  --animate-twc03-pulse: twc03-pulse 2s ease-in-out infinite;
}

@keyframes twc03-pulse {
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

.twc-03 {
  width: 100%;
  min-height: 100svh;
}
```
