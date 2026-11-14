---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-vertical-tabs-with-view-transitions-api-animation/"
title: "Tailwind Vertical Tabs with View Transitions API Animation"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "A travel field guide whose destinations morph into each other: one document.startViewTransition() call wraps a plain attribute swap, and three names &mdash;…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vertical Tabs with View Transitions API Animation
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-vertical-tabs-with-view-transitions-api-animation/

A travel field guide whose destinations morph into each other: one document.startViewTransition() call wraps a plain attribute swap, and three names &mdash; the scene, the title and the selected pill &mdash; glide from their old boxes to their new ones. The names are Tailwind arbitrary properties, and the pill's name is applied by aria-selected:before:[view-transition-name:tvt-14-pill], so only the selected tab ever carries it. Each destination is a fully illustrated inline-SVG landscape.
## HTML
```html
<section class="tvt-14 w-full min-h-svh grid place-items-center bg-tvt14-bg bg-[radial-gradient(60%_50%_at_20%_0%,var(--color-tvt14-glow),transparent_70%),radial-gradient(50%_45%_at_100%_10%,var(--color-tvt14-glow2),transparent_70%)] px-4 py-14 font-tvt14-sans text-tvt14-ink antialiased sm:px-6" aria-label="Tailwind vertical tabs with View Transitions API demo">
  <div class="grid w-full max-w-[60rem] justify-items-center gap-7">
    <header class="grid justify-items-center gap-3 text-center">
      <p class="inline-flex items-center gap-2 rounded-full bg-tvt14-card px-3 py-1.5 font-tvt14-mono text-[11.5px] text-tvt14-acc-ink ring-1 ring-tvt14-line"><span aria-hidden="true" class="size-1.5 rounded-full bg-tvt14-acc shadow-[0_0_0_3px] shadow-tvt14-acc/25"></span>document.startViewTransition()</p>
      <h2 class="font-tvt14-serif text-[clamp(30px,4.8vw,48px)] leading-[1.02] font-medium tracking-[-0.025em] text-balance">A field guide that <em class="text-tvt14-acc-ink">morphs</em></h2>
      <p class="max-w-[48ch] text-[15px] leading-relaxed text-tvt14-mut text-pretty">Pick a destination: the scene, the title and the selection pill each glide from their old box to their new one. Arrow keys work too.</p>
    </header>

    <div class="@container w-full">
    <div id="tvt-14-guide" class="grid w-full grid-cols-[minmax(13rem,16rem)_minmax(0,1fr)] gap-4 rounded-[26px] bg-tvt14-card p-3 shadow-tvt14-card ring-1 ring-tvt14-line transition-[opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none sm:p-4 @max-[44rem]:grid-cols-1">
      <div class="flex flex-col gap-3 rounded-[20px] bg-tvt14-rail p-2.5 ring-1 ring-tvt14-line">
        <div class="flex items-center justify-between px-2 pt-1.5 @max-[44rem]:hidden">
          <p class="font-tvt14-mono text-[10.5px] font-medium tracking-[0.16em] text-tvt14-mut uppercase">Field guide</p>
          <p class="font-tvt14-mono text-[10.5px] text-tvt14-mut tabular-nums">03 routes</p>
        </div>
        <div role="tablist" aria-orientation="vertical" aria-label="Destinations" class="grid gap-1 @max-[44rem]:grid-cols-3">

          <button type="button" role="tab" id="tvt-14-tab1" aria-controls="tvt-14-p1" aria-selected="true" class="group/tab relative flex min-h-14 w-full cursor-pointer items-center gap-3 rounded-2xl px-2.5 py-2 text-start text-tvt14-mut transition-colors duration-200 hover:text-tvt14-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt14-ring aria-selected:text-tvt14-ink before:absolute before:inset-0 before:rounded-2xl before:bg-tvt14-pill before:opacity-0 before:shadow-tvt14-pill before:ring-1 before:ring-tvt14-acc/25 before:transition-opacity aria-selected:before:opacity-100 aria-selected:before:[view-transition-name:tvt-14-pill] hover:before:opacity-60 aria-selected:hover:before:opacity-100 @max-[44rem]:flex-col @max-[44rem]:justify-center @max-[44rem]:gap-1.5 @max-[44rem]:text-center">
            <span aria-hidden="true" class="relative z-10 grid size-9 shrink-0 place-items-center overflow-hidden rounded-[10px] bg-linear-to-br from-[#3a3470] to-[#f0a070] ring-1 ring-black/10 shadow-sm"><span class="absolute inset-x-0 bottom-0 h-1/2 bg-black/20 [clip-path:polygon(0_60%,30%_10%,55%_55%,75%_25%,100%_70%,100%_100%,0_100%)]"></span></span>
            <span class="relative z-10 grid min-w-0 leading-tight">
              <span class="text-[14.5px] font-semibold tracking-[-0.01em] @max-[44rem]:text-[13px]">Coastline</span>
              <span class="mt-0.5 truncate text-[12px] text-tvt14-mut @max-[44rem]:hidden">Big Sur · 4 trails</span>
            </span>
            <svg aria-hidden="true" viewBox="0 0 20 20" width="16" height="16" class="relative z-10 ms-auto shrink-0 opacity-0 transition-opacity group-aria-selected/tab:opacity-100 text-tvt14-acc-ink @max-[44rem]:hidden" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>

          <button type="button" role="tab" id="tvt-14-tab2" aria-controls="tvt-14-p2" aria-selected="false" tabindex="-1" class="group/tab relative flex min-h-14 w-full cursor-pointer items-center gap-3 rounded-2xl px-2.5 py-2 text-start text-tvt14-mut transition-colors duration-200 hover:text-tvt14-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt14-ring aria-selected:text-tvt14-ink before:absolute before:inset-0 before:rounded-2xl before:bg-tvt14-pill before:opacity-0 before:shadow-tvt14-pill before:ring-1 before:ring-tvt14-acc/25 before:transition-opacity aria-selected:before:opacity-100 aria-selected:before:[view-transition-name:tvt-14-pill] hover:before:opacity-60 aria-selected:hover:before:opacity-100 @max-[44rem]:flex-col @max-[44rem]:justify-center @max-[44rem]:gap-1.5 @max-[44rem]:text-center">
            <span aria-hidden="true" class="relative z-10 grid size-9 shrink-0 place-items-center overflow-hidden rounded-[10px] bg-linear-to-br from-[#86bde6] to-[#6d8fae] ring-1 ring-black/10 shadow-sm"><span class="absolute inset-x-0 bottom-0 h-1/2 bg-black/20 [clip-path:polygon(0_60%,30%_10%,55%_55%,75%_25%,100%_70%,100%_100%,0_100%)]"></span></span>
            <span class="relative z-10 grid min-w-0 leading-tight">
              <span class="text-[14.5px] font-semibold tracking-[-0.01em] @max-[44rem]:text-[13px]">Highlands</span>
              <span class="mt-0.5 truncate text-[12px] text-tvt14-mut @max-[44rem]:hidden">Isle of Skye · 6 trails</span>
            </span>
            <svg aria-hidden="true" viewBox="0 0 20 20" width="16" height="16" class="relative z-10 ms-auto shrink-0 opacity-0 transition-opacity group-aria-selected/tab:opacity-100 text-tvt14-acc-ink @max-[44rem]:hidden" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>

          <button type="button" role="tab" id="tvt-14-tab3" aria-controls="tvt-14-p3" aria-selected="false" tabindex="-1" class="group/tab relative flex min-h-14 w-full cursor-pointer items-center gap-3 rounded-2xl px-2.5 py-2 text-start text-tvt14-mut transition-colors duration-200 hover:text-tvt14-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt14-ring aria-selected:text-tvt14-ink before:absolute before:inset-0 before:rounded-2xl before:bg-tvt14-pill before:opacity-0 before:shadow-tvt14-pill before:ring-1 before:ring-tvt14-acc/25 before:transition-opacity aria-selected:before:opacity-100 aria-selected:before:[view-transition-name:tvt-14-pill] hover:before:opacity-60 aria-selected:hover:before:opacity-100 @max-[44rem]:flex-col @max-[44rem]:justify-center @max-[44rem]:gap-1.5 @max-[44rem]:text-center">
            <span aria-hidden="true" class="relative z-10 grid size-9 shrink-0 place-items-center overflow-hidden rounded-[10px] bg-linear-to-br from-[#bfe0b4] to-[#2f5a3e] ring-1 ring-black/10 shadow-sm"><span class="absolute inset-x-0 bottom-0 h-1/2 bg-black/20 [clip-path:polygon(0_60%,30%_10%,55%_55%,75%_25%,100%_70%,100%_100%,0_100%)]"></span></span>
            <span class="relative z-10 grid min-w-0 leading-tight">
              <span class="text-[14.5px] font-semibold tracking-[-0.01em] @max-[44rem]:text-[13px]">Deep forest</span>
              <span class="mt-0.5 truncate text-[12px] text-tvt14-mut @max-[44rem]:hidden">Olympic NP · 5 trails</span>
            </span>
            <svg aria-hidden="true" viewBox="0 0 20 20" width="16" height="16" class="relative z-10 ms-auto shrink-0 opacity-0 transition-opacity group-aria-selected/tab:opacity-100 text-tvt14-acc-ink @max-[44rem]:hidden" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
        </div>
        <div class="mt-auto rounded-2xl bg-tvt14-card p-3.5 ring-1 ring-tvt14-line @max-[44rem]:hidden">
          <p class="text-[12px] font-semibold">Morph engine</p>
          <p data-support class="mt-1 flex items-center gap-1.5 font-tvt14-mono text-[11px] text-tvt14-mut"><span aria-hidden="true" class="size-1.5 rounded-full bg-tvt14-sand"></span>checking…</p>
        </div>
      </div>
      <div class="min-w-0">

          <article role="tabpanel" id="tvt-14-p1" aria-labelledby="tvt-14-tab1" tabindex="0" class="grid gap-5 rounded-2xl p-1 transition-[opacity,translate] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt14-ring starting:translate-y-1 starting:opacity-0 motion-reduce:transition-none">
            <figure class="relative aspect-[16/10] overflow-hidden rounded-2xl bg-tvt14-rail shadow-tvt14-hero ring-1 ring-black/5 [view-transition-name:tvt-14-hero]">
              <svg viewBox="0 0 640 400" preserveAspectRatio="xMidYMid slice" class="block size-full" role="img" aria-label="Illustration: a lighthouse on dark sea cliffs at dusk, with the sun setting over a calm violet ocean">
              <defs>
                <linearGradient id="tvt-14-c-sky" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#262a5e"/><stop offset=".45" stop-color="#8a4f86"/><stop offset=".8" stop-color="#e98a73"/><stop offset="1" stop-color="#f7c07e"/></linearGradient>
                <linearGradient id="tvt-14-c-sea" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#6b5592"/><stop offset="1" stop-color="#1c1d45"/></linearGradient>
                <radialGradient id="tvt-14-c-sun" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffe2a3" stop-opacity=".85"/><stop offset="1" stop-color="#ffe2a3" stop-opacity="0"/></radialGradient>
              </defs>
              <rect width="640" height="252" fill="url(#tvt-14-c-sky)"/>
              <circle cx="430" cy="238" r="120" fill="url(#tvt-14-c-sun)"/>
              <circle cx="430" cy="240" r="40" fill="#ffd894"/>
              <path d="M330 252Q380 236 440 242T560 236Q600 232 640 238V252Z" fill="#7c4a72"/>
              <path d="M470 252Q520 244 580 246T640 244V252Z" fill="#5d3a63"/>
              <rect y="250" width="640" height="150" fill="url(#tvt-14-c-sea)"/>
              <g fill="#ffd894"><rect x="392" y="258" width="76" height="3" rx="1.5" opacity=".75"/><rect x="404" y="268" width="54" height="3" rx="1.5" opacity=".55"/><rect x="384" y="279" width="88" height="2.5" rx="1.25" opacity=".4"/><rect x="412" y="291" width="40" height="2.5" rx="1.25" opacity=".35"/><rect x="398" y="304" width="62" height="2" rx="1" opacity=".22"/></g>
              <g fill="none" stroke="#fff" stroke-linecap="round" opacity=".16" stroke-width="1.5"><path d="M260 300q20-6 40 0t40 0"/><path d="M520 322q20-6 40 0t40 0"/><path d="M330 352q24-7 48 0t48 0"/><path d="M560 372q20-6 40 0"/></g>
              <path d="M0 132L48 140L96 150L128 176L160 196L196 236L226 262L258 312L286 400H0Z" fill="#221a3a"/>
              <path d="M0 132L48 140L96 150L128 176L106 172L72 158L30 148L0 150Z" fill="#3a2b52"/>
              <path d="M226 262L258 312L286 400H262L240 330L212 280Z" fill="#171230"/>
              <path d="M226 330q14 6 20 22M200 300q10 6 16 18" fill="none" stroke="#fff" stroke-opacity=".25" stroke-width="2" stroke-linecap="round"/>
              <path d="M70 108L-40 70V146Z" fill="#ffe9b0" opacity=".2"/>
              <rect x="62" y="104" width="16" height="38" fill="#f2ece6"/><rect x="62" y="116" width="16" height="7" fill="#c9504f"/><rect x="62" y="131" width="16" height="7" fill="#c9504f"/>
              <rect x="60" y="96" width="20" height="9" rx="2" fill="#ffe08f"/><path d="M58 96L70 86L82 96Z" fill="#2b2140"/>
              <path d="M174 68q3 -3 6 2q3 -5 6 -2" fill="none" stroke="#2b2140" stroke-width="1.4" stroke-linecap="round"/><path d="M199.5 80.5q2.25 -2.25 4.5 1.5q2.25 -3.75 4.5 -1.5" fill="none" stroke="#2b2140" stroke-width="1.0" stroke-linecap="round"/><path d="M514.6 94.2q2.7 -2.7 5.4 1.8q2.7 -4.5 5.4 -1.8" fill="none" stroke="#2b2140" stroke-width="1.3" stroke-linecap="round"/><path d="M542.4 86.8q1.7999999999999998 -1.7999999999999998 3.5999999999999996 1.2q1.7999999999999998 -3 3.5999999999999996 -1.2" fill="none" stroke="#2b2140" stroke-width="0.8" stroke-linecap="round"/>
            </svg>
              <figcaption class="absolute inset-x-0 bottom-0 flex flex-wrap items-end justify-between gap-2 bg-linear-to-t from-black/55 to-transparent px-4 pt-10 pb-3.5 text-white">
                <span class="text-[13px] font-semibold">Big Sur, California</span>
                <span class="rounded-full bg-white/15 px-2.5 py-1 font-tvt14-mono text-[11px] backdrop-blur-sm">36.27°N 121.81°W</span>
              </figcaption>
            </figure>
            <div class="grid gap-3 px-1.5 pb-1.5">
              <h3 class="font-tvt14-serif text-[clamp(24px,3vw,32px)] leading-[1.05] font-medium tracking-[-0.02em] text-balance [view-transition-name:tvt-14-title]">Cliffs that catch the last light</h3>
              <p class="max-w-[52ch] text-[14.5px] leading-relaxed text-tvt14-mut text-pretty">A 9.6 km ridge-and-cove loop above Pfeiffer Beach. Start an hour before sunset so the lighthouse beam is on by the time you reach the overlook.</p>
              <dl class="grid grid-cols-3 gap-2"><div class="rounded-xl bg-tvt14-rail px-3 py-2.5 ring-1 ring-tvt14-line"><dt class="text-[11.5px] font-medium text-tvt14-mut">Distance</dt><dd class="mt-0.5 text-[15px] font-bold tracking-[-0.01em] tabular-nums">9.6 km</dd></div><div class="rounded-xl bg-tvt14-rail px-3 py-2.5 ring-1 ring-tvt14-line"><dt class="text-[11.5px] font-medium text-tvt14-mut">Climb</dt><dd class="mt-0.5 text-[15px] font-bold tracking-[-0.01em] tabular-nums">410 m</dd></div><div class="rounded-xl bg-tvt14-rail px-3 py-2.5 ring-1 ring-tvt14-line"><dt class="text-[11.5px] font-medium text-tvt14-mut">Best light</dt><dd class="mt-0.5 text-[15px] font-bold tracking-[-0.01em] tabular-nums">Dusk</dd></div></dl>
              <p class="flex gap-2.5 rounded-xl border border-dashed border-tvt14-acc/35 bg-tvt14-acc/[0.06] px-3.5 py-2.5 text-[13px] leading-relaxed text-tvt14-mut"><svg aria-hidden="true" viewBox="0 0 20 20" width="16" height="16" class="mt-0.5 shrink-0 text-tvt14-acc-ink" focusable="false"><path d="M10 2.5l1.9 4.6 4.6 1.9-4.6 1.9L10 15.5l-1.9-4.6L3.5 9l4.6-1.9Z" fill="currentColor"/></svg><span><b class="font-semibold text-tvt14-ink">The browser owns the morph.</b> One <code class="rounded bg-tvt14-ink/[0.07] px-1 py-px font-tvt14-mono text-[12px] text-tvt14-ink">view-transition-name</code> on the scene and it scales from its old box to its new one &mdash; no FLIP maths, no library.</span></p>
            </div>
          </article>

          <article role="tabpanel" id="tvt-14-p2" aria-labelledby="tvt-14-tab2" tabindex="0" hidden class="grid gap-5 rounded-2xl p-1 transition-[opacity,translate] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt14-ring starting:translate-y-1 starting:opacity-0 motion-reduce:transition-none">
            <figure class="relative aspect-[16/10] overflow-hidden rounded-2xl bg-tvt14-rail shadow-tvt14-hero ring-1 ring-black/5 [view-transition-name:tvt-14-hero]">
              <svg viewBox="0 0 640 400" preserveAspectRatio="xMidYMid slice" class="block size-full" role="img" aria-label="Illustration: snow-capped highland ridges above drifting valley mist, with a winding trail through green foothills">
              <defs>
                <linearGradient id="tvt-14-h-sky" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#7fb7e2"/><stop offset=".7" stop-color="#d4e9f2"/><stop offset="1" stop-color="#f1f4ea"/></linearGradient>
                <linearGradient id="tvt-14-h-mist" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".75"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
                <linearGradient id="tvt-14-h-hill" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#5d8d5c"/><stop offset="1" stop-color="#365e3d"/></linearGradient>
              </defs>
              <rect width="640" height="400" fill="url(#tvt-14-h-sky)"/>
              <circle cx="520" cy="72" r="26" fill="#fff8de"/><circle cx="520" cy="72" r="46" fill="#fff8de" opacity=".25"/>
              <path d="M0 214L70 160L118 186L196 108L262 170L330 120L404 176L470 96L548 160L640 128V260H0Z" fill="#a8bfd6"/>
              <path d="M196 108L218 130L208 128L196 140L184 128L176 126Z M470 96L494 120L482 118L470 132L458 120L448 122Z M330 120L348 138L330 134L316 140Z" fill="#fbfdff"/>
              <path d="M0 250L90 186L150 218L240 150L320 222L400 170L486 228L560 182L640 220V300H0Z" fill="#7895b0"/>
              <path d="M240 150L262 172L250 170L240 182L228 170L218 172Z M560 182L578 200L566 198L556 206L548 196Z" fill="#eef4fa"/>
              <rect y="214" width="640" height="70" fill="url(#tvt-14-h-mist)"/>
              <path d="M0 300Q120 248 230 276T450 262T640 270V400H0Z" fill="url(#tvt-14-h-hill)"/>
              <path d="M0 340Q140 300 300 330T640 318V400H0Z" fill="#2c4f33"/>
              <path d="M330 400Q360 360 320 340T350 300Q368 288 352 276" fill="none" stroke="#e4cf98" stroke-width="5" stroke-linecap="round"/>
              <path d="M60 315.9L67.2 331.8L52.8 331.8ZM60 325.7L71.1 341.5L48.9 341.5ZM60 335.4L75.0 351.3L45.0 351.3ZM58.5 344.8h3.0V352h-3.0Z" fill="#1d3a25"/><path d="M84 317.5L91.2 335.3L76.8 335.3ZM84 328.4L95.1 346.3L72.9 346.3ZM84 339.4L99.0 357.2L69.0 357.2ZM82.5 349.9h3.0V358h-3.0Z" fill="#1d3a25"/><path d="M572 307.1L579.2 326.9L564.8 326.9ZM572 319.2L583.1 339.0L560.9 339.0ZM572 331.4L587.0 351.1L557.0 351.1ZM570.5 343.0h3.0V352h-3.0Z" fill="#1d3a25"/><path d="M598 308.7L605.2 330.4L590.8 330.4ZM598 322.0L609.1 343.7L586.9 343.7ZM598 335.3L613.0 357.0L583.0 357.0ZM596.5 348.1h3.0V358h-3.0Z" fill="#1d3a25"/><path d="M622 313.7L629.2 330.6L614.8 330.6ZM622 324.1L633.1 340.9L610.9 340.9ZM622 334.4L637.0 351.2L607.0 351.2ZM620.5 344.3h3.0V352h-3.0Z" fill="#1d3a25"/>
              <path d="M144.6 90.2q2.7 -2.7 5.4 1.8q2.7 -4.5 5.4 -1.8" fill="none" stroke="#3d5570" stroke-width="1.3" stroke-linecap="round"/><path d="M167.8 102.6q2.0999999999999996 -2.0999999999999996 4.199999999999999 1.4q2.0999999999999996 -3.5 4.199999999999999 -1.4" fill="none" stroke="#3d5570" stroke-width="1.0" stroke-linecap="round"/><path d="M375.2 68.4q2.4000000000000004 -2.4000000000000004 4.800000000000001 1.6q2.4000000000000004 -4 4.800000000000001 -1.6" fill="none" stroke="#3d5570" stroke-width="1.1" stroke-linecap="round"/>
            </svg>
              <figcaption class="absolute inset-x-0 bottom-0 flex flex-wrap items-end justify-between gap-2 bg-linear-to-t from-black/55 to-transparent px-4 pt-10 pb-3.5 text-white">
                <span class="text-[13px] font-semibold">Isle of Skye, Scotland</span>
                <span class="rounded-full bg-white/15 px-2.5 py-1 font-tvt14-mono text-[11px] backdrop-blur-sm">57.50°N 6.17°W</span>
              </figcaption>
            </figure>
            <div class="grid gap-3 px-1.5 pb-1.5">
              <h3 class="font-tvt14-serif text-[clamp(24px,3vw,32px)] leading-[1.05] font-medium tracking-[-0.02em] text-balance [view-transition-name:tvt-14-title]">Ridges above the morning mist</h3>
              <p class="max-w-[52ch] text-[14.5px] leading-relaxed text-tvt14-mut text-pretty">The Quiraing traverse climbs out of the valley fog onto open ridgeline. Mist usually burns off by ten; set off early and walk up into the light.</p>
              <dl class="grid grid-cols-3 gap-2"><div class="rounded-xl bg-tvt14-rail px-3 py-2.5 ring-1 ring-tvt14-line"><dt class="text-[11.5px] font-medium text-tvt14-mut">Distance</dt><dd class="mt-0.5 text-[15px] font-bold tracking-[-0.01em] tabular-nums">6.8 km</dd></div><div class="rounded-xl bg-tvt14-rail px-3 py-2.5 ring-1 ring-tvt14-line"><dt class="text-[11.5px] font-medium text-tvt14-mut">Climb</dt><dd class="mt-0.5 text-[15px] font-bold tracking-[-0.01em] tabular-nums">320 m</dd></div><div class="rounded-xl bg-tvt14-rail px-3 py-2.5 ring-1 ring-tvt14-line"><dt class="text-[11.5px] font-medium text-tvt14-mut">Best light</dt><dd class="mt-0.5 text-[15px] font-bold tracking-[-0.01em] tabular-nums">Sunrise</dd></div></dl>
              <p class="flex gap-2.5 rounded-xl border border-dashed border-tvt14-acc/35 bg-tvt14-acc/[0.06] px-3.5 py-2.5 text-[13px] leading-relaxed text-tvt14-mut"><svg aria-hidden="true" viewBox="0 0 20 20" width="16" height="16" class="mt-0.5 shrink-0 text-tvt14-acc-ink" focusable="false"><path d="M10 2.5l1.9 4.6 4.6 1.9-4.6 1.9L10 15.5l-1.9-4.6L3.5 9l4.6-1.9Z" fill="currentColor"/></svg><span><b class="font-semibold text-tvt14-ink">Names must be unique.</b> Two rendered elements sharing a name abort the whole transition &mdash; that is why only the <em>selected</em> tab's pill carries <code class="rounded bg-tvt14-ink/[0.07] px-1 py-px font-tvt14-mono text-[12px] text-tvt14-ink">tvt-14-pill</code>.</span></p>
            </div>
          </article>

          <article role="tabpanel" id="tvt-14-p3" aria-labelledby="tvt-14-tab3" tabindex="0" hidden class="grid gap-5 rounded-2xl p-1 transition-[opacity,translate] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt14-ring starting:translate-y-1 starting:opacity-0 motion-reduce:transition-none">
            <figure class="relative aspect-[16/10] overflow-hidden rounded-2xl bg-tvt14-rail shadow-tvt14-hero ring-1 ring-black/5 [view-transition-name:tvt-14-hero]">
              <svg viewBox="0 0 640 400" preserveAspectRatio="xMidYMid slice" class="block size-full" role="img" aria-label="Illustration: shafts of sunlight falling through layered pine forest onto a mossy clearing with ferns">
              <defs>
                <linearGradient id="tvt-14-f-sky" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#cfe7c4"/><stop offset=".55" stop-color="#8fbf96"/><stop offset="1" stop-color="#2f5a3e"/></linearGradient>
                <linearGradient id="tvt-14-f-beam" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#fff6c9" stop-opacity=".55"/><stop offset="1" stop-color="#fff6c9" stop-opacity="0"/></linearGradient>
                <linearGradient id="tvt-14-f-fog" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#e6f3dc" stop-opacity="0"/><stop offset="1" stop-color="#e6f3dc" stop-opacity=".55"/></linearGradient>
              </defs>
              <rect width="640" height="400" fill="url(#tvt-14-f-sky)"/>
              <circle cx="380" cy="40" r="60" fill="#fffbe0" opacity=".7"/>
              <path d="M20 147.0L36.8 201.1L3.2 201.1ZM20 180.2L45.9 234.3L-5.9 234.3ZM20 213.4L55.0 267.5L-15.0 267.5ZM16.5 245.4h7.0V270h-7.0Z" fill="#7fae86"/><path d="M70 132.0L86.8 192.7L53.2 192.7ZM70 169.3L95.9 230.0L44.1 230.0ZM70 206.5L105.0 267.2L35.0 267.2ZM66.5 242.4h7.0V270h-7.0Z" fill="#7fae86"/><path d="M120 117.0L136.8 184.3L103.2 184.3ZM120 158.3L145.9 225.6L94.1 225.6ZM120 199.6L155.0 266.9L85.0 266.9ZM116.5 239.4h7.0V270h-7.0Z" fill="#7fae86"/><path d="M175 102.0L191.8 175.9L158.2 175.9ZM175 147.4L200.9 221.3L149.1 221.3ZM175 192.7L210.0 266.6L140.0 266.6ZM171.5 236.4h7.0V270h-7.0Z" fill="#7fae86"/><path d="M230 139.5L246.8 196.9L213.2 196.9ZM230 174.7L255.9 232.2L204.1 232.2ZM230 210.0L265.0 267.4L195.0 267.4ZM226.5 243.9h7.0V270h-7.0Z" fill="#7fae86"/><path d="M290 124.5L306.8 188.5L273.2 188.5ZM290 163.8L315.9 227.8L264.1 227.8ZM290 203.1L325.0 267.1L255.0 267.1ZM286.5 240.9h7.0V270h-7.0Z" fill="#7fae86"/><path d="M345 109.5L361.8 180.1L328.2 180.1ZM345 152.8L370.9 223.5L319.1 223.5ZM345 196.2L380.0 266.8L310.0 266.8ZM341.5 237.9h7.0V270h-7.0Z" fill="#7fae86"/><path d="M400 147.0L416.8 201.1L383.2 201.1ZM400 180.2L425.9 234.3L374.1 234.3ZM400 213.4L435.0 267.5L365.0 267.5ZM396.5 245.4h7.0V270h-7.0Z" fill="#7fae86"/><path d="M455 132.0L471.8 192.7L438.2 192.7ZM455 169.3L480.9 230.0L429.1 230.0ZM455 206.5L490.0 267.2L420.0 267.2ZM451.5 242.4h7.0V270h-7.0Z" fill="#7fae86"/><path d="M510 117.0L526.8 184.3L493.2 184.3ZM510 158.3L535.9 225.6L484.1 225.6ZM510 199.6L545.0 266.9L475.0 266.9ZM506.5 239.4h7.0V270h-7.0Z" fill="#7fae86"/><path d="M565 102.0L581.8 175.9L548.2 175.9ZM565 147.4L590.9 221.3L539.1 221.3ZM565 192.7L600.0 266.6L530.0 266.6ZM561.5 236.4h7.0V270h-7.0Z" fill="#7fae86"/><path d="M615 139.5L631.8 196.9L598.2 196.9ZM615 174.7L640.9 232.2L589.1 232.2ZM615 210.0L650.0 267.4L580.0 267.4ZM611.5 243.9h7.0V270h-7.0Z" fill="#7fae86"/>
              <rect y="190" width="640" height="90" fill="url(#tvt-14-f-fog)"/>
              <path d="M360 0L420 0L300 400H190Z M450 0H480L420 400H360Z" fill="url(#tvt-14-f-beam)"/>
              <path d="M0 141.4L24.0 224.4L-24.0 224.4ZM0 192.3L37.0 275.3L-37.0 275.3ZM0 243.2L50.0 326.2L-50.0 326.2ZM-5.0 292.3h10.0V330h-10.0Z" fill="#3f6f4c"/><path d="M80 132.4L104.0 225.5L56.0 225.5ZM80 189.5L117.0 282.6L43.0 282.6ZM80 246.7L130.0 339.8L30.0 339.8ZM75.0 301.7h10.0V344h-10.0Z" fill="#3f6f4c"/><path d="M150 95.4L174.0 198.6L126.0 198.6ZM150 158.7L187.0 262.0L113.0 262.0ZM150 222.1L200.0 325.3L100.0 325.3ZM145.0 283.1h10.0V330h-10.0Z" fill="#3f6f4c"/><path d="M470 86.4L494.0 199.7L446.0 199.7ZM470 156.0L507.0 269.3L433.0 269.3ZM470 225.5L520.0 338.8L420.0 338.8ZM465.0 292.5h10.0V344h-10.0Z" fill="#3f6f4c"/><path d="M540 129.9L564.0 217.9L516.0 217.9ZM540 183.9L577.0 272.0L503.0 272.0ZM540 238.0L590.0 326.0L490.0 326.0ZM535.0 290.0h10.0V330h-10.0Z" fill="#3f6f4c"/><path d="M610 120.9L634.0 219.1L586.0 219.1ZM610 181.1L647.0 279.3L573.0 279.3ZM610 241.4L660.0 339.5L560.0 339.5ZM605.0 299.4h10.0V344h-10.0Z" fill="#3f6f4c"/>
              <path d="M0 330Q160 300 320 318T640 312V400H0Z" fill="#2a4a31"/>
              <ellipse cx="330" cy="352" rx="150" ry="18" fill="#c9d98c" opacity=".35"/>
              <path d="M-20 139.4L13.6 258.5L-53.6 258.5ZM-20 212.5L31.8 331.5L-71.8 331.5ZM-20 285.5L50.0 404.6L-90.0 404.6ZM-27.0 355.9h14.0V410h-14.0Z" fill="#16301e"/><path d="M60 116.4L93.6 250.0L26.4 250.0ZM60 198.4L111.8 332.0L8.2 332.0ZM60 280.3L130.0 413.9L-10.0 413.9ZM53.0 359.3h14.0V420h-14.0Z" fill="#16301e"/><path d="M560 73.4L593.6 221.5L526.4 221.5ZM560 164.3L611.8 312.4L508.2 312.4ZM560 255.2L630.0 403.3L490.0 403.3ZM553.0 342.7h14.0V410h-14.0Z" fill="#16301e"/><path d="M650 50.4L683.6 213.0L616.4 213.0ZM650 150.2L701.8 312.8L598.2 312.8ZM650 250.0L720.0 412.6L580.0 412.6ZM643.0 346.1h14.0V420h-14.0Z" fill="#16301e"/>
              <g fill="none" stroke="#5f9a5c" stroke-width="3" stroke-linecap="round"><path d="M250 384q-16-26-40-34M250 384q-6-30 8-46M250 384q14-24 38-30"/><path d="M420 390q-12-22-32-28M420 390q4-26 18-38M420 390q16-18 36-20"/></g>
              <g fill="#f3e6a6"><circle cx="300" cy="230" r="2"/><circle cx="350" cy="260" r="1.6"/><circle cx="410" cy="214" r="1.8"/><circle cx="268" cy="288" r="1.4"/></g>
            </svg>
              <figcaption class="absolute inset-x-0 bottom-0 flex flex-wrap items-end justify-between gap-2 bg-linear-to-t from-black/55 to-transparent px-4 pt-10 pb-3.5 text-white">
                <span class="text-[13px] font-semibold">Olympic National Park, WA</span>
                <span class="rounded-full bg-white/15 px-2.5 py-1 font-tvt14-mono text-[11px] backdrop-blur-sm">47.86°N 123.93°W</span>
              </figcaption>
            </figure>
            <div class="grid gap-3 px-1.5 pb-1.5">
              <h3 class="font-tvt14-serif text-[clamp(24px,3vw,32px)] leading-[1.05] font-medium tracking-[-0.02em] text-balance [view-transition-name:tvt-14-title]">Light shafts in the old growth</h3>
              <p class="max-w-[52ch] text-[14.5px] leading-relaxed text-tvt14-mut text-pretty">The Hall of Mosses loop is short, flat and endlessly green. Midday is best here: the sun is high enough to cut straight through the canopy.</p>
              <dl class="grid grid-cols-3 gap-2"><div class="rounded-xl bg-tvt14-rail px-3 py-2.5 ring-1 ring-tvt14-line"><dt class="text-[11.5px] font-medium text-tvt14-mut">Distance</dt><dd class="mt-0.5 text-[15px] font-bold tracking-[-0.01em] tabular-nums">1.3 km</dd></div><div class="rounded-xl bg-tvt14-rail px-3 py-2.5 ring-1 ring-tvt14-line"><dt class="text-[11.5px] font-medium text-tvt14-mut">Climb</dt><dd class="mt-0.5 text-[15px] font-bold tracking-[-0.01em] tabular-nums">30 m</dd></div><div class="rounded-xl bg-tvt14-rail px-3 py-2.5 ring-1 ring-tvt14-line"><dt class="text-[11.5px] font-medium text-tvt14-mut">Best light</dt><dd class="mt-0.5 text-[15px] font-bold tracking-[-0.01em] tabular-nums">Noon</dd></div></dl>
              <p class="flex gap-2.5 rounded-xl border border-dashed border-tvt14-acc/35 bg-tvt14-acc/[0.06] px-3.5 py-2.5 text-[13px] leading-relaxed text-tvt14-mut"><svg aria-hidden="true" viewBox="0 0 20 20" width="16" height="16" class="mt-0.5 shrink-0 text-tvt14-acc-ink" focusable="false"><path d="M10 2.5l1.9 4.6 4.6 1.9-4.6 1.9L10 15.5l-1.9-4.6L3.5 9l4.6-1.9Z" fill="currentColor"/></svg><span><b class="font-semibold text-tvt14-ink">Feature-detect, always.</b> Where <code class="rounded bg-tvt14-ink/[0.07] px-1 py-px font-tvt14-mono text-[12px] text-tvt14-ink">startViewTransition</code> is missing, the swap is instant and a <code class="rounded bg-tvt14-ink/[0.07] px-1 py-px font-tvt14-mono text-[12px] text-tvt14-ink">starting:</code> fade covers it. Nobody sees a broken state.</span></p>
            </div>
          </article>
      </div>
    </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tvt14-card px-3.5 py-2 text-center font-tvt14-mono text-[11.5px] text-tvt14-mut ring-1 ring-tvt14-line">[view-transition-name:tvt-14-hero] · startViewTransition()</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt14-bg: #f9f2e2;
  --color-tvt14-bg: oklch(0.962 0.022 85);
  --color-tvt14-glow: #b7e5bf8c;
  --color-tvt14-glow: oklch(0.88 0.07 150 / 0.55);
  --color-tvt14-glow2: #b6e6ff80;
  --color-tvt14-glow2: oklch(0.9 0.06 230 / 0.5);
  --color-tvt14-card: #fffcf8;
  --color-tvt14-card: oklch(0.993 0.007 85);
  --color-tvt14-rail: #f4f0e1;
  --color-tvt14-rail: oklch(0.955 0.02 95);
  --color-tvt14-pill: #ffffff;
  --color-tvt14-pill: oklch(1 0 0);
  --color-tvt14-ink: #0a281a;
  --color-tvt14-ink: oklch(0.25 0.045 160);
  --color-tvt14-mut: #4b614f;
  --color-tvt14-mut: oklch(0.47 0.04 150);
  --color-tvt14-line: #dedbc9;
  --color-tvt14-line: oklch(0.89 0.025 100);
  --color-tvt14-acc: #0b764d;
  --color-tvt14-acc: oklch(0.5 0.11 160);
  --color-tvt14-acc-ink: #00603d;
  --color-tvt14-acc-ink: oklch(0.43 0.1 160);
  --color-tvt14-sand: #d09945;
  --color-tvt14-sand: oklch(0.72 0.12 75);
  --color-tvt14-ring: #00764c;
  --color-tvt14-ring: oklch(0.5 0.12 160);
  --font-tvt14-sans: 'Manrope', system-ui, sans-serif;
  --font-tvt14-serif: 'Fraunces', Georgia, serif;
  --font-tvt14-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --shadow-tvt14-card: 0 1px 2px oklch(0.3 0.05 160 / 0.07), 0 32px 70px -34px oklch(0.35 0.08 160 / 0.42);
  --shadow-tvt14-pill: 0 1px 2px oklch(0.3 0.05 160 / 0.1), 0 8px 20px -10px oklch(0.4 0.1 160 / 0.45);
  --shadow-tvt14-hero: 0 18px 40px -22px oklch(0.25 0.06 160 / 0.6);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-14 {
  width: 100%;
  min-height: 100svh;
}
/* View Transitions: pseudo-elements live on the document root, so they are plain CSS. The names are
   namespaced (tvt-14-*), so these rules never touch another demo's transition. */

::view-transition-group(tvt-14-pill) {
  animation-duration: .45s;
  animation-timing-function: cubic-bezier(.34, 1.28, .44, 1);
}

::view-transition-group(tvt-14-hero) {
  animation-duration: .5s;
  animation-timing-function: cubic-bezier(.32, .72, .3, 1);
}

::view-transition-old(tvt-14-title) {
  animation: .22s ease both tvt14-title-out;
}

::view-transition-new(tvt-14-title) {
  animation: .38s cubic-bezier(.16, 1, .3, 1) .08s both tvt14-title-in;
}

@keyframes tvt14-title-out {
  to {
    opacity: 0;
    translate: 0 -8px;
  }
}

@keyframes tvt14-title-in {
  from {
    opacity: 0;
    translate: 0 10px;
  }
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(tvt-14-pill),
    ::view-transition-group(tvt-14-hero),
    ::view-transition-old(tvt-14-title),
    ::view-transition-new(tvt-14-title) {
    animation: none;
  }
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-14:not([data-theme="light"]) {
    --color-tvt14-bg: #05130d;
    --color-tvt14-bg: oklch(0.17 0.025 165);
    --color-tvt14-glow: #033d2680;
    --color-tvt14-glow: oklch(0.32 0.07 160 / 0.5);
    --color-tvt14-glow2: #00334666;
    --color-tvt14-glow2: oklch(0.3 0.06 230 / 0.4);
    --color-tvt14-card: #091d15;
    --color-tvt14-card: oklch(0.21 0.03 165);
    --color-tvt14-rail: #061710;
    --color-tvt14-rail: oklch(0.185 0.028 165);
    --color-tvt14-pill: #123021;
    --color-tvt14-pill: oklch(0.28 0.045 160);
    --color-tvt14-ink: #f2efe0;
    --color-tvt14-ink: oklch(0.95 0.02 95);
    --color-tvt14-mut: #abb9a7;
    --color-tvt14-mut: oklch(0.77 0.03 140);
    --color-tvt14-line: #23382d;
    --color-tvt14-line: oklch(0.32 0.035 160);
    --color-tvt14-acc: #57bc8a;
    --color-tvt14-acc: oklch(0.72 0.12 160);
    --color-tvt14-acc-ink: #8ee0ab;
    --color-tvt14-acc-ink: oklch(0.84 0.11 155);
    --color-tvt14-sand: #eabc6e;
    --color-tvt14-sand: oklch(0.82 0.11 80);
    --color-tvt14-ring: #6bcf9d;
    --color-tvt14-ring: oklch(0.78 0.12 160);
  }
}

.tvt-14[data-theme="dark"] {
  --color-tvt14-bg: #05130d;
  --color-tvt14-bg: oklch(0.17 0.025 165);
  --color-tvt14-glow: #033d2680;
  --color-tvt14-glow: oklch(0.32 0.07 160 / 0.5);
  --color-tvt14-glow2: #00334666;
  --color-tvt14-glow2: oklch(0.3 0.06 230 / 0.4);
  --color-tvt14-card: #091d15;
  --color-tvt14-card: oklch(0.21 0.03 165);
  --color-tvt14-rail: #061710;
  --color-tvt14-rail: oklch(0.185 0.028 165);
  --color-tvt14-pill: #123021;
  --color-tvt14-pill: oklch(0.28 0.045 160);
  --color-tvt14-ink: #f2efe0;
  --color-tvt14-ink: oklch(0.95 0.02 95);
  --color-tvt14-mut: #abb9a7;
  --color-tvt14-mut: oklch(0.77 0.03 140);
  --color-tvt14-line: #23382d;
  --color-tvt14-line: oklch(0.32 0.035 160);
  --color-tvt14-acc: #57bc8a;
  --color-tvt14-acc: oklch(0.72 0.12 160);
  --color-tvt14-acc-ink: #8ee0ab;
  --color-tvt14-acc-ink: oklch(0.84 0.11 155);
  --color-tvt14-sand: #eabc6e;
  --color-tvt14-sand: oklch(0.82 0.11 80);
  --color-tvt14-ring: #6bcf9d;
  --color-tvt14-ring: oklch(0.78 0.12 160);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tvt-14-guide');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const tabs = [...root.querySelectorAll('[role="tab"]')];
  const support = root.querySelector('[data-support]');
  const calm = matchMedia('(prefers-reduced-motion: reduce)');
  const canMorph = typeof document.startViewTransition === 'function';
  if (support) support.lastChild.textContent = canMorph ? 'View Transitions: native' : 'Fallback: CSS fade';
  const swap = (tab) => tabs.forEach((t) => {
    const on = t === tab;
    t.setAttribute('aria-selected', String(on));
    t.tabIndex = on ? 0 : -1;
    document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
  });
  const activate = (tab) => {
    if (!tab || tab.getAttribute('aria-selected') === 'true') return;
    if (!canMorph || calm.matches) return swap(tab);
    document.startViewTransition(() => swap(tab));
  };
  root.addEventListener('click', (e) => activate(e.target.closest('[role="tab"]')));
  root.querySelector('[role="tablist"]').addEventListener('keydown', (e) => {
    const step = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 }[e.key];
    const i = tabs.indexOf(document.activeElement);
    let to = -1;
    if (step) to = (i + step + tabs.length) % tabs.length;
    else if (e.key === 'Home') to = 0;
    else if (e.key === 'End') to = tabs.length - 1;
    if (to < 0) return;
    e.preventDefault();
    tabs[to].focus();
    activate(tabs[to]);
  });
})();
```
