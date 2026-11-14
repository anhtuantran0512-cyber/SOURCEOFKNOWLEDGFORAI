---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-travel-postcard-flip-card-diagonal-rotate3d/"
title: "Tailwind Travel Postcard Flip Card with Diagonal rotate3d Twist"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "The collection's one light-theme card, and its one diagonal axis: rotate3d(1,1,0,180deg) twists it corner to corner as though you grabbed the top-left and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Travel Postcard Flip Card with Diagonal rotate3d Twist
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-travel-postcard-flip-card-diagonal-rotate3d/

The collection's one light-theme card, and its one diagonal axis: rotate3d(1,1,0,180deg) twists it corner to corner as though you grabbed the top-left and bottom-right and turned. The airmail border is a masked repeating gradient &mdash; three arbitrary properties that Tailwind rightly has no scale for, sitting next to two dozen ordinary utilities.
## HTML
```html
<section class="tfc-20 w-full min-h-svh grid place-items-center bg-tfc20-paper font-tfc20-serif px-5 py-10 text-tfc20-ink [background-image:repeating-linear-gradient(45deg,var(--color-tfc20-paper)_0_12px,var(--color-tfc20-paper2)_12px_24px)]">
  <div class="group relative h-[480px] w-[360px] max-w-full [perspective:1200px] rounded-sm has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc20-red has-[:focus-visible]:outline-offset-4">
    <input id="tfc-20-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-20-flip" class="absolute inset-0 z-20 cursor-pointer"><span class="sr-only">Read the message on the back of this postcard</span></label>

    <div class="relative h-full w-full transition-transform duration-1000 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotate3d(1,1,0,180deg)] group-has-checked:[transform:rotate3d(1,1,0,180deg)] group-has-[:focus-visible]:[transform:rotate3d(1,1,0,180deg)] motion-reduce:transition-none">

      <div class="absolute inset-0 flex flex-col overflow-hidden border-6 border-tfc20-card bg-tfc20-card outline-2 outline-dashed outline-tfc20-ink/25 -outline-offset-12 shadow-[0_4px_10px_oklch(0.35_0.02_70/0.12),0_18px_40px_oklch(0.35_0.02_70/0.25)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <div class="h-40 w-full shrink-0 border-b border-tfc20-ink/15">
          <svg width="100%" height="160" viewBox="0 0 360 160" preserveAspectRatio="none" role="img" aria-label="Sunset skyline of pastel hillside buildings">
            <defs>
              <linearGradient id="tfc-20-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f7c8a0"/><stop offset="60%" stop-color="#f4a87d"/><stop offset="100%" stop-color="#e88e6e"/></linearGradient>
              <linearGradient id="tfc-20-bldg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fef3c7"/><stop offset="100%" stop-color="#fbbf24"/></linearGradient>
            </defs>
            <rect width="360" height="160" fill="url(#tfc-20-sky)"/>
            <circle cx="280" cy="48" r="22" fill="#fff3cf" opacity="0.85"/>
            <g fill="url(#tfc-20-bldg)">
              <rect x="20" y="92" width="34" height="68"/><polygon points="20,92 37,75 54,92"/>
              <rect x="64" y="100" width="42" height="60"/><polygon points="64,100 85,80 106,100"/>
              <rect x="116" y="84" width="38" height="76"/><polygon points="116,84 135,68 154,84"/>
              <rect x="164" y="96" width="46" height="64"/><polygon points="164,96 187,76 210,96"/>
              <rect x="220" y="78" width="40" height="82"/><polygon points="220,78 240,60 260,78"/>
              <rect x="270" y="100" width="34" height="60"/><polygon points="270,100 287,82 304,100"/>
              <rect x="314" y="92" width="36" height="68"/><polygon points="314,92 332,75 350,92"/>
            </g>
            <g fill="#0c0a07" opacity="0.6">
              <rect x="28" y="100" width="3" height="5"/><rect x="36" y="100" width="3" height="5"/><rect x="44" y="100" width="3" height="5"/>
              <rect x="28" y="115" width="3" height="5"/><rect x="36" y="115" width="3" height="5"/><rect x="44" y="115" width="3" height="5"/>
              <rect x="72" y="110" width="3" height="5"/><rect x="80" y="110" width="3" height="5"/><rect x="88" y="110" width="3" height="5"/>
              <rect x="124" y="92" width="3" height="5"/><rect x="132" y="92" width="3" height="5"/><rect x="142" y="92" width="3" height="5"/>
              <rect x="172" y="106" width="3" height="5"/><rect x="184" y="106" width="3" height="5"/><rect x="196" y="106" width="3" height="5"/>
              <rect x="228" y="90" width="3" height="5"/><rect x="240" y="90" width="3" height="5"/><rect x="252" y="90" width="3" height="5"/>
              <rect x="320" y="100" width="3" height="5"/><rect x="332" y="100" width="3" height="5"/><rect x="342" y="100" width="3" height="5"/>
            </g>
          </svg>
        </div>
        <div class="px-6 pt-5 pb-3 text-center">
          <p class="mb-1.5 text-[13px] font-bold uppercase tracking-[0.25em] text-tfc20-accent">Greetings from</p>
          <h2 class="font-tfc20-script text-[52px] font-semibold leading-none tracking-[-0.01em] text-tfc20-ink">Lisbon</h2>
          <p class="mt-2 text-[11px] uppercase tracking-[0.15em] text-tfc20-ink/60">Portugal &middot; postcards from the road</p>
        </div>
        <span aria-hidden="true" class="absolute top-3.5 right-3.5 flex h-16 w-13.5 rotate-6 flex-col items-center justify-center gap-0.5 border-2 border-dashed border-tfc20-red bg-tfc20-card2 shadow-[0_2px_4px_oklch(0.35_0.02_70/0.18)]">
          <span class="text-lg leading-none text-tfc20-red">&#9733;</span>
          <span class="text-center text-[8px] font-bold uppercase leading-[1.1] tracking-[0.05em] text-tfc20-red">Par<br>Avion</span>
        </span>
        <p class="mt-auto px-6 py-3.5 text-center text-[10px] uppercase italic tracking-[0.25em] text-tfc20-ink/55">Hover, tap or press Space to read</p>
      </div>

      <div class="absolute inset-0 flex flex-col overflow-hidden border-6 border-tfc20-card2 bg-tfc20-card2 px-6 py-6 shadow-[0_4px_10px_oklch(0.35_0.02_70/0.12),0_18px_40px_oklch(0.35_0.02_70/0.25)] [transform:rotate3d(1,1,0,180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden] before:pointer-events-none before:absolute before:inset-y-0 before:left-1/2 before:w-px before:bg-[repeating-linear-gradient(to_bottom,oklch(0.58_0.21_27/0.35)_0_4px,transparent_4px_10px)] after:pointer-events-none after:absolute after:inset-2 after:border-2 after:border-transparent after:opacity-50 after:bg-[repeating-linear-gradient(45deg,#1e40af_0_8px,transparent_8px_16px,#dc2626_16px_24px,transparent_24px_32px)] after:[-webkit-mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] after:[-webkit-mask-composite:xor] after:[mask-composite:exclude]">
        <div class="mb-3 flex justify-between text-[10px] uppercase tracking-[0.2em] text-tfc20-ink/60">
          <span class="font-bold text-tfc20-accent">Postcard &middot; 02</span>
          <span>June 14</span>
        </div>
        <div class="flex-1 pr-5 font-tfc20-script text-[19px] leading-[1.5] text-tfc20-ink">
          <p class="mb-2">Dear friend,</p>
          <p class="mb-2">The pastel buildings climb every hill and at sunset the whole city turns the colour of warm bread. I am drinking ginjinha in a paper cup and listening to a man play fado outside the cathedral.</p>
          <p class="mb-2">Wish you were here.</p>
          <p class="mt-2.5 text-[20px]">&mdash; V.</p>
        </div>
        <div class="absolute right-5.5 bottom-5.5 flex w-[42%] flex-col gap-3.5" aria-hidden="true">
          <span class="h-px bg-tfc20-ink/30"></span>
          <span class="h-px bg-tfc20-ink/30"></span>
          <span class="h-px bg-tfc20-ink/30"></span>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc20-paper: #f5f0e6;
  --color-tfc20-paper: oklch(0.95 0.015 85);
  --color-tfc20-paper2: #efe7d6;
  --color-tfc20-paper2: oklch(0.92 0.02 85);
  --color-tfc20-card: #faf6ec;
  --color-tfc20-card: oklch(0.97 0.012 85);
  --color-tfc20-card2: #fef9ec;
  --color-tfc20-card2: oklch(0.98 0.02 88);
  --color-tfc20-ink: #3a2f24;
  --color-tfc20-ink: oklch(0.33 0.02 70);
  --color-tfc20-red: #dc2626;
  --color-tfc20-red: oklch(0.58 0.21 27);
  --color-tfc20-blue: #1e40af;
  --color-tfc20-blue: oklch(0.4 0.17 265);
  --color-tfc20-accent: #a5642f;
  --color-tfc20-accent: oklch(0.55 0.1 60);
  --font-tfc20-serif: 'Lora', Georgia, serif;
  --font-tfc20-script: 'Caveat', 'Brush Script MT', cursive;
}

.tfc-20 {
  width: 100%;
  min-height: 100svh;
}
/* Reduced motion: cross-fade the faces instead of twisting them. */

@media (prefers-reduced-motion: reduce) {
  .tfc-20 * {
    transition-duration: 1ms !important;
  }
}
```
