---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-gaming-trading-card-flip-character-stats-rarity/"
title: "Tailwind Gaming Trading Card Flip with Character Stats & Rarity Glow"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "A legendary-rarity character card: inline-SVG art and ability slots on the front, a four-stat ledger and lore on the back."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gaming Trading Card Flip with Character Stats & Rarity Glow
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-gaming-trading-card-flip-character-stats-rarity/

A legendary-rarity character card: inline-SVG art and ability slots on the front, a four-stat ledger and lore on the back. The turn pops 60px toward the camera at its midpoint while a gold aura blooms behind &mdash; and the aura deliberately lives on the scene, not the card, because a filter or shadow on a preserve-3d element disables backface culling in Chromium and collapses the whole illusion.
## HTML
```html
<section class="tfc-08 w-full min-h-svh grid place-items-center bg-tfc08-bg font-tfc08-sans px-5 py-10 text-tfc08-ink">
  <div class="group relative w-[290px] h-[450px] [perspective:1200px] rounded-2xl transition-shadow duration-500 hover:shadow-[0_0_60px_8px_oklch(0.83_0.16_82/0.35)] has-checked:shadow-[0_0_60px_8px_oklch(0.83_0.16_82/0.35)] has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc08-gold has-[:focus-visible]:outline-offset-4">
    <input id="tfc-08-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-08-flip" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show Vex Nightbane's competitive stats</span></label>

    <div class="relative w-full h-full [transform-style:preserve-3d] group-hover:animate-tfc08-reveal group-has-checked:animate-tfc08-reveal group-has-[:focus-visible]:animate-tfc08-reveal motion-reduce:animate-none motion-reduce:group-has-checked:[transform:rotateY(180deg)]">

      <div class="absolute inset-0 flex flex-col rounded-2xl overflow-hidden bg-linear-160 from-tfc08-panel to-tfc08-panel2 border-2 border-tfc08-gold/35 shadow-[inset_0_1px_0_oklch(0.83_0.16_82/0.2),0_18px_40px_-16px_oklch(0_0_0/0.8)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <div class="flex items-center justify-between border-b border-tfc08-gold/15 bg-linear-to-r from-tfc08-gold/15 to-transparent px-4 py-3">
          <p class="text-[9px] font-extrabold uppercase tracking-[0.2em] text-tfc08-gold">&#9733; Legendary</p>
          <p class="text-xl font-black text-tfc08-gold [text-shadow:0_0_15px_oklch(0.83_0.16_82/0.5)]">CP 4800</p>
        </div>
        <div class="relative grid flex-1 place-items-center overflow-hidden bg-linear-160 from-tfc08-art1 via-tfc08-art2 to-tfc08-art3 before:absolute before:inset-0 before:bg-[radial-gradient(circle_at_50%_60%,oklch(0.63_0.22_25/0.2),transparent_60%)]">
          <svg class="relative z-1" width="160" height="180" viewBox="0 0 160 180" role="img" aria-label="Illustration of Vex Nightbane, a cloaked dark sorcerer holding a staff">
            <ellipse cx="80" cy="40" rx="28" ry="30" fill="oklch(0.63 0.22 25 / 0.7)"/>
            <ellipse cx="80" cy="40" rx="18" ry="20" fill="#1a000a"/>
            <circle cx="72" cy="38" r="5" fill="oklch(0.83 0.16 82 / 0.9)"/>
            <circle cx="88" cy="38" r="5" fill="oklch(0.83 0.16 82 / 0.9)"/>
            <circle cx="72" cy="38" r="2" fill="#000"/>
            <circle cx="88" cy="38" r="2" fill="#000"/>
            <path d="M52 75 Q80 60 108 75 L115 150 Q80 160 45 150 Z" fill="oklch(0.63 0.2 295 / 0.5)"/>
            <path d="M62 75 Q80 65 98 75 L102 140 Q80 150 58 140 Z" fill="oklch(0.15 0.1 300 / 0.8)"/>
            <rect x="105" y="50" width="6" height="90" rx="3" fill="oklch(0.83 0.16 82 / 0.6)" transform="rotate(15 108 95)"/>
            <polygon points="108,50 114,40 120,55" fill="oklch(0.63 0.22 25 / 0.8)" transform="rotate(15 108 95)"/>
            <path d="M52 80 Q30 120 35 160 Q52 140 52 120" fill="oklch(0.63 0.2 295 / 0.3)"/>
            <path d="M108 80 Q130 120 125 160 Q108 140 108 120" fill="oklch(0.63 0.2 295 / 0.3)"/>
            <circle cx="80" cy="40" r="35" fill="none" stroke="oklch(0.83 0.16 82 / 0.2)" stroke-width="2"/>
          </svg>
        </div>
        <div class="border-y border-tfc08-gold/15 bg-linear-to-r from-tfc08-red/15 to-tfc08-violet/10 px-4 py-3">
          <h3 class="text-[17px] font-black tracking-[0.02em] text-white">Vex Nightbane</h3>
          <p class="mt-0.5 text-[10px] font-semibold uppercase tracking-[0.15em] text-tfc08-red">Dark Sorcerer &middot; Elite</p>
        </div>
        <ul class="flex gap-1.5 px-4 py-2.5" aria-label="Abilities">
          <li class="grid size-7 place-items-center rounded-lg border border-tfc08-gold/20 bg-tfc08-gold/10 text-sm" title="Fire">&#128293;</li>
          <li class="grid size-7 place-items-center rounded-lg border border-tfc08-gold/20 bg-tfc08-gold/10 text-sm" title="Lightning">&#9889;</li>
          <li class="grid size-7 place-items-center rounded-lg border border-tfc08-gold/20 bg-tfc08-gold/10 text-sm" title="Necrosis">&#128128;</li>
          <li class="grid size-7 place-items-center rounded-lg border border-tfc08-gold/20 bg-tfc08-gold/10 text-sm" title="Ward">&#128737;</li>
        </ul>
      </div>

      <div class="absolute inset-0 flex flex-col gap-2.5 rounded-2xl overflow-hidden p-5 bg-linear-160 from-tfc08-back to-tfc08-back2 border-2 border-tfc08-violet/35 shadow-[inset_0_1px_0_oklch(0.63_0.2_295/0.2),0_18px_40px_-16px_oklch(0_0_0/0.8)] [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <div class="flex items-center justify-between">
          <h3 class="text-base font-black text-white">Vex Nightbane</h3>
          <p class="text-xs font-bold text-tfc08-gold">CP 4800</p>
        </div>
        <ul class="flex flex-wrap gap-1.5">
          <li class="rounded-full border border-tfc08-red/30 bg-tfc08-red/20 px-2 py-0.5 text-[9px] font-bold tracking-[0.06em] text-tfc08-red">Fire</li>
          <li class="rounded-full border border-tfc08-violet/30 bg-tfc08-violet/20 px-2 py-0.5 text-[9px] font-bold tracking-[0.06em] text-tfc08-violet">Dark</li>
        </ul>
        <dl class="grid grid-cols-2 gap-2">
          <div class="rounded-xl border border-white/7 bg-white/4 px-3 py-2.5"><dt id="tfc-08-atk" class="mb-1 text-[9px] uppercase tracking-[0.12em] text-tfc08-dim">Attack</dt><dd class="flex items-center gap-1.5"><span class="min-w-6 text-[15px] font-extrabold text-white">94</span><span role="progressbar" aria-labelledby="tfc-08-atk" aria-valuenow="94" aria-valuemin="0" aria-valuemax="100" class="block h-1 flex-1 overflow-hidden rounded-full bg-white/8"><span class="block h-full w-[94%] rounded-full bg-linear-to-r from-tfc08-red to-tfc08-orange"></span></span></dd></div>
          <div class="rounded-xl border border-white/7 bg-white/4 px-3 py-2.5"><dt id="tfc-08-mag" class="mb-1 text-[9px] uppercase tracking-[0.12em] text-tfc08-dim">Magic</dt><dd class="flex items-center gap-1.5"><span class="min-w-6 text-[15px] font-extrabold text-white">98</span><span role="progressbar" aria-labelledby="tfc-08-mag" aria-valuenow="98" aria-valuemin="0" aria-valuemax="100" class="block h-1 flex-1 overflow-hidden rounded-full bg-white/8"><span class="block h-full w-[98%] rounded-full bg-linear-to-r from-tfc08-violet to-tfc08-lilac"></span></span></dd></div>
          <div class="rounded-xl border border-white/7 bg-white/4 px-3 py-2.5"><dt id="tfc-08-def" class="mb-1 text-[9px] uppercase tracking-[0.12em] text-tfc08-dim">Defense</dt><dd class="flex items-center gap-1.5"><span class="min-w-6 text-[15px] font-extrabold text-white">60</span><span role="progressbar" aria-labelledby="tfc-08-def" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" class="block h-1 flex-1 overflow-hidden rounded-full bg-white/8"><span class="block h-full w-[60%] rounded-full bg-linear-to-r from-tfc08-gold to-tfc08-sand"></span></span></dd></div>
          <div class="rounded-xl border border-white/7 bg-white/4 px-3 py-2.5"><dt id="tfc-08-spd" class="mb-1 text-[9px] uppercase tracking-[0.12em] text-tfc08-dim">Speed</dt><dd class="flex items-center gap-1.5"><span class="min-w-6 text-[15px] font-extrabold text-white">82</span><span role="progressbar" aria-labelledby="tfc-08-spd" aria-valuenow="82" aria-valuemin="0" aria-valuemax="100" class="block h-1 flex-1 overflow-hidden rounded-full bg-white/8"><span class="block h-full w-[82%] rounded-full bg-linear-to-r from-tfc08-green to-tfc08-mint"></span></span></dd></div>
        </dl>
        <blockquote class="mt-auto border-l-2 border-tfc08-violet/30 pl-2.5 text-[11px] italic leading-[1.6] text-tfc08-ink/70">&ldquo;Born from shadow and flame, Vex commands armies of wraiths and bends reality itself. Few have witnessed his full power &mdash; fewer still survived.&rdquo;</blockquote>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc08-bg: #0a0005;
  --color-tfc08-bg: oklch(0.13 0.03 10);
  --color-tfc08-panel: #1a0010;
  --color-tfc08-panel: oklch(0.18 0.07 350);
  --color-tfc08-panel2: #0d000a;
  --color-tfc08-panel2: oklch(0.13 0.04 350);
  --color-tfc08-art1: #2d0020;
  --color-tfc08-art1: oklch(0.22 0.11 330);
  --color-tfc08-art2: #0d0030;
  --color-tfc08-art2: oklch(0.17 0.1 285);
  --color-tfc08-art3: #1a000a;
  --color-tfc08-art3: oklch(0.16 0.06 10);
  --color-tfc08-back: #0d0020;
  --color-tfc08-back: oklch(0.15 0.08 290);
  --color-tfc08-back2: #15001a;
  --color-tfc08-back2: oklch(0.16 0.07 315);
  --color-tfc08-red: #ef4444;
  --color-tfc08-red: oklch(0.63 0.22 25);
  --color-tfc08-orange: #f97316;
  --color-tfc08-orange: oklch(0.7 0.19 45);
  --color-tfc08-gold: #fbbf24;
  --color-tfc08-gold: oklch(0.83 0.16 82);
  --color-tfc08-sand: #fde68a;
  --color-tfc08-sand: oklch(0.92 0.09 90);
  --color-tfc08-violet: #8b5cf6;
  --color-tfc08-violet: oklch(0.63 0.2 295);
  --color-tfc08-lilac: #a78bfa;
  --color-tfc08-lilac: oklch(0.73 0.16 295);
  --color-tfc08-green: #22c55e;
  --color-tfc08-green: oklch(0.73 0.18 150);
  --color-tfc08-mint: #86efac;
  --color-tfc08-mint: oklch(0.88 0.13 155);
  --color-tfc08-ink: #fff5f5;
  --color-tfc08-ink: oklch(0.97 0.01 20);
  --color-tfc08-dim: #9a8590;
  --color-tfc08-dim: oklch(0.66 0.02 350);
  --font-tfc08-sans: 'Sora', system-ui, sans-serif;
  --animate-tfc08-reveal: tfc08-reveal 0.9s cubic-bezier(.4,0,.2,1) forwards;
}

@keyframes tfc08-reveal {
  0% {
    transform: rotateY(0deg) translateZ(0);
  }

  50% {
    transform: rotateY(90deg) translateZ(60px);
  }

  100% {
    transform: rotateY(180deg) translateZ(0);
  }
}

.tfc-08 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-08 * {
    animation: none !important;
    transition-duration: 1ms !important;
  }
}
```
