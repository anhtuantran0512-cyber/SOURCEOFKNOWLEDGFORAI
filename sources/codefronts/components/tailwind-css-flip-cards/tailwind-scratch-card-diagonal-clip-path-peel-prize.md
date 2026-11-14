---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-scratch-card-diagonal-clip-path-peel-prize/"
title: "Tailwind Scratch Card with Diagonal clip-path Peel & Prize Reveal"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "A reward card whose surface peels away diagonally: a four-point clip-path polygon collapses toward the top-left corner, wiping the scratch layer off the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Scratch Card with Diagonal clip-path Peel & Prize Reveal
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-scratch-card-diagonal-clip-path-peel-prize/

A reward card whose surface peels away diagonally: a four-point clip-path polygon collapses toward the top-left corner, wiping the scratch layer off the prize underneath. Stars fade in on staggered delays once the wipe is nearly done. No 3D, no rotation &mdash; and no hover-only trap, because a reward you cannot claim on a phone is not a reward.
## HTML
```html
<section class="tfc-23 w-full min-h-svh grid place-items-center content-center gap-7 bg-tfc23-bg font-tfc23-sans px-5 py-10 text-tfc23-ink">
  <div class="group relative h-[250px] w-[380px] max-w-full overflow-hidden rounded-[18px] shadow-[0_0_50px_oklch(0.63_0.2_295/0.12)] has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc23-violet has-[:focus-visible]:outline-offset-4">
    <input id="tfc-23-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-23-flip" class="absolute inset-0 z-20 cursor-pointer peer-checked:pointer-events-none"><span class="sr-only">Scratch the card to reveal your prize</span></label>

    <div class="absolute inset-0 isolate flex flex-col items-center justify-center gap-3 rounded-[18px] border border-tfc23-violet/30 bg-linear-135 from-tfc23-p1 via-tfc23-p2 to-tfc23-p3 p-7 before:pointer-events-none before:absolute before:inset-0 before:rounded-[18px] before:bg-[radial-gradient(ellipse_at_50%_50%,oklch(0.77_0.16_70/0.08),transparent_70%)]">
      <span class="relative z-1 grid size-18 place-items-center rounded-full border-2 border-tfc23-gold/40 bg-linear-135 from-tfc23-gold/20 to-tfc23-gold/5 shadow-[0_0_30px_oklch(0.77_0.16_70/0.2)]">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" class="text-tfc23-gold" aria-hidden="true"><path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M17 5h3a3 3 0 0 1-3 3M7 5H4a3 3 0 0 0 3 3"/></svg>
      </span>
      <p class="relative z-1 text-[11px] font-bold uppercase tracking-[0.18em] text-tfc23-muted">You won</p>
      <p class="relative z-1 bg-linear-135 from-tfc23-gold via-tfc23-sand to-tfc23-gold bg-clip-text text-[42px] font-black leading-none tracking-[-0.02em] text-transparent">$250</p>
      <p class="relative z-1 text-xs text-tfc23-muted">Store credit &middot; valid 30 days</p>
      <button type="button" class="relative z-30 mt-1 min-h-11 rounded-full bg-linear-135 from-tfc23-gold to-tfc23-goldD px-7 text-[13px] font-extrabold tracking-[0.04em] text-black transition-[filter,box-shadow] duration-150 hover:brightness-110 hover:shadow-[0_6px_18px_oklch(0.77_0.16_70/0.4)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Claim reward &rarr;</button>
    </div>

    <span aria-hidden="true" class="absolute top-[15%] left-[12%] z-15 size-1.5 rounded-full bg-tfc23-gold opacity-0 transition-opacity duration-300 delay-[800ms] group-hover:opacity-100 group-has-checked:opacity-100"></span>
    <span aria-hidden="true" class="absolute top-[22%] right-[15%] z-15 size-1 rounded-full bg-tfc23-gold opacity-0 transition-opacity duration-300 delay-[900ms] group-hover:opacity-100 group-has-checked:opacity-100"></span>
    <span aria-hidden="true" class="absolute bottom-[20%] left-[18%] z-15 size-1.5 rounded-full bg-tfc23-gold opacity-0 transition-opacity duration-300 delay-[1000ms] group-hover:opacity-100 group-has-checked:opacity-100"></span>
    <span aria-hidden="true" class="absolute right-[12%] bottom-[18%] z-15 size-1.5 rounded-full bg-tfc23-gold opacity-0 transition-opacity duration-300 delay-[850ms] group-hover:opacity-100 group-has-checked:opacity-100"></span>
    <span aria-hidden="true" class="absolute top-1/2 left-[8%] z-15 size-1 rounded-full bg-tfc23-gold opacity-0 transition-opacity duration-300 delay-[1100ms] group-hover:opacity-100 group-has-checked:opacity-100"></span>
    <span aria-hidden="true" class="absolute top-[45%] right-[9%] z-15 size-1 rounded-full bg-tfc23-gold opacity-0 transition-opacity duration-300 delay-[950ms] group-hover:opacity-100 group-has-checked:opacity-100"></span>

    <div class="absolute inset-0 z-10 overflow-hidden rounded-[18px] [clip-path:polygon(0%_0%,100%_0%,100%_100%,0%_100%)] transition-[clip-path] duration-[900ms] ease-[cubic-bezier(.4,0,.2,1)] group-hover:[clip-path:polygon(0%_0%,0%_0%,0%_0%,0%_0%)] group-has-checked:[clip-path:polygon(0%_0%,0%_0%,0%_0%,0%_0%)] group-has-[:focus-visible]:[clip-path:polygon(0%_0%,0%_0%,0%_0%,0%_0%)] motion-reduce:transition-none">
      <div class="absolute inset-0 rounded-[18px] border border-tfc23-violet/30 bg-[radial-gradient(circle_at_20%_30%,oklch(0.63_0.2_295/0.15)_0%,transparent_40%),radial-gradient(circle_at_80%_70%,oklch(0.65_0.22_300/0.12)_0%,transparent_40%),linear-gradient(135deg,#1a0d38,#250f4a,#12082a)] after:absolute after:inset-0 after:rounded-[18px] after:bg-[repeating-linear-gradient(45deg,oklch(1_0_0/0.025)_0px,oklch(1_0_0/0.025)_1px,transparent_1px,transparent_8px),repeating-linear-gradient(-45deg,oklch(1_0_0/0.015)_0px,oklch(1_0_0/0.015)_1px,transparent_1px,transparent_8px)]"></div>
      <div class="relative z-1 flex h-full flex-col items-center justify-center gap-3 p-7">
        <p class="flex items-center gap-2 text-[15px] font-extrabold tracking-[0.06em] text-tfc23-ink/90"><span class="size-2 rounded-full bg-tfc23-violet"></span>NovaPay Rewards</p>
        <h2 class="text-center text-[22px] font-black leading-tight text-white">Instant win<br>scratch card</h2>
        <p class="text-center text-xs text-tfc23-muted">Hover, tap or press Space to reveal your prize</p>
        <p class="flex items-center gap-2.5 rounded-xl border border-white/10 bg-white/6 px-5 py-2.5">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" class="animate-tfc23-wiggle text-tfc23-gold motion-reduce:animate-none" aria-hidden="true"><circle cx="12" cy="12" r="8"/><path d="M12 8v8M9.5 10.5h5M9.5 13.5h5"/></svg>
          <span class="text-xs font-semibold text-tfc23-muted">Scratch to reveal</span>
        </p>
      </div>
      <span aria-hidden="true" class="pointer-events-none absolute -top-[20%] -left-[20%] h-[60%] w-[60%] bg-[linear-gradient(135deg,transparent_40%,oklch(0_0_0/0.35)_50%,oklch(0.63_0.2_295/0.2)_55%,transparent_65%)] transition-[transform,opacity] duration-[900ms] ease-[cubic-bezier(.4,0,.2,1)] group-hover:-translate-x-[60%] group-hover:-translate-y-[60%] group-hover:opacity-0 group-has-checked:-translate-x-[60%] group-has-checked:-translate-y-[60%] group-has-checked:opacity-0"></span>
    </div>
  </div>
  <p class="text-center text-[10px] uppercase tracking-[0.15em] text-tfc23-dim">Pure clip-path &mdash; no 3D transform anywhere</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc23-bg: #06040e;
  --color-tfc23-bg: oklch(0.11 0.025 295);
  --color-tfc23-p1: #0d0a20;
  --color-tfc23-p1: oklch(0.16 0.05 295);
  --color-tfc23-p2: #1a0d3a;
  --color-tfc23-p2: oklch(0.21 0.09 295);
  --color-tfc23-p3: #0a1a1a;
  --color-tfc23-p3: oklch(0.19 0.03 190);
  --color-tfc23-violet: #8b5cf6;
  --color-tfc23-violet: oklch(0.63 0.2 295);
  --color-tfc23-purple: #a855f7;
  --color-tfc23-purple: oklch(0.65 0.22 300);
  --color-tfc23-gold: #f59e0b;
  --color-tfc23-gold: oklch(0.77 0.16 70);
  --color-tfc23-goldD: #d97706;
  --color-tfc23-goldD: oklch(0.68 0.16 60);
  --color-tfc23-sand: #fde68a;
  --color-tfc23-sand: oklch(0.92 0.09 90);
  --color-tfc23-ink: #faf5ff;
  --color-tfc23-ink: oklch(0.98 0.015 300);
  --color-tfc23-muted: #b5a9c4;
  --color-tfc23-muted: oklch(0.77 0.035 300);
  --color-tfc23-dim: #877f99;
  --color-tfc23-dim: oklch(0.62 0.03 300);
  --font-tfc23-sans: 'Sora', system-ui, sans-serif;
  --animate-tfc23-wiggle: tfc23-wiggle 1.5s ease-in-out infinite;
}

@keyframes tfc23-wiggle {
  0%,
    100% {
    transform: rotate(-8deg);
  }

  50% {
    transform: rotate(8deg);
  }
}

.tfc-23 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-23 * {
    animation: none !important;
    transition-duration: 1ms !important;
  }
}
```
