---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-cassette-mixtape-label-button/"
title: "Tailwind Cassette Mixtape Label Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A Type-II cassette with a hand-written label: both reels turn while you hover, and clicking flips the shell to side B."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Cassette Mixtape Label Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-cassette-mixtape-label-button/

A Type-II cassette with a hand-written label: both reels turn while you hover, and clicking flips the shell to side B. The reels are conic gradients, the spool teeth a repeating conic, and the flip the same transform-3d construction as the coin.
## HTML
```html
<div class="tb-37 w-full min-h-svh grid place-items-center perspective-[1000px] font-tb37-sans p-[clamp(1.5rem,6vw,4rem)]">
  <label class="group relative block cursor-pointer w-76 h-46 [-webkit-tap-highlight-color:transparent]">
    <input type="checkbox" aria-label="Flip the cassette to side B" class="sr-only">
    <span aria-hidden="true" class="relative block size-full transform-3d transition-[transform,translate] duration-[900ms] ease-tb37-out group-hover:-translate-y-[3px] group-active:scale-[0.985] group-has-checked:rotate-y-180 group-has-focus-visible:outline-2 group-has-focus-visible:outline-offset-[6px] group-has-focus-visible:outline-tb37-accent group-has-focus-visible:rounded-[0.55rem] motion-reduce:transition-none">
      <span class="tb-37__face absolute inset-0 grid grid-rows-[auto_1fr] gap-3 p-3.5 rounded-[0.55rem] backface-hidden shadow-[inset_0_1px_0_#ffffff33,inset_0_-2px_6px_#00000080,0_18px_30px_-14px_#000000cc]">
        <span class="flex items-center justify-between gap-4 px-6 py-2.5 rounded-[0.3rem] bg-[linear-gradient(180deg,#00000080,#00000047)] shadow-[inset_0_0_0_1px_#ffffff14]">
          <span class="tb-37__reel block size-13 rounded-full shadow-[inset_0_0_0_1px_#ffffff1f] animate-tb37-spin [animation-play-state:paused] group-hover:[animation-play-state:running] group-has-focus-visible:[animation-play-state:running] motion-reduce:animate-none"></span>
          <span class="tb-37__reel block size-13 rounded-full shadow-[inset_0_0_0_1px_#ffffff1f] animate-tb37-spin [animation-duration:4.6s] [animation-play-state:paused] group-hover:[animation-play-state:running] group-has-focus-visible:[animation-play-state:running] motion-reduce:animate-none"></span>
        </span>
        <span class="tb-37__label relative flex items-end justify-between gap-3 px-3 py-2 rounded-[0.2rem] shadow-[inset_0_0_0_1px_#0000001f]">
          <span class="relative z-20 font-tb37-hand text-2xl font-bold text-tb37-ink">summer, mostly</span>
          <span class="text-xs font-bold tracking-[0.14em] text-tb37-accent px-1.5 py-0.5 rounded-[0.2rem] bg-tb37-accent-tint">A</span>
        </span>
      </span>
      <span class="tb-37__face absolute inset-0 grid grid-rows-[auto_1fr] gap-3 p-3.5 rounded-[0.55rem] backface-hidden rotate-y-180 shadow-[inset_0_1px_0_#ffffff33,inset_0_-2px_6px_#00000080,0_18px_30px_-14px_#000000cc]">
        <span class="flex items-center justify-between gap-4 px-6 py-2.5 rounded-[0.3rem] bg-[linear-gradient(180deg,#00000080,#00000047)] shadow-[inset_0_0_0_1px_#ffffff14]">
          <span class="tb-37__reel block size-13 rounded-full shadow-[inset_0_0_0_1px_#ffffff1f] animate-tb37-spin [animation-play-state:paused] group-hover:[animation-play-state:running] motion-reduce:animate-none"></span>
          <span class="tb-37__reel block size-13 rounded-full shadow-[inset_0_0_0_1px_#ffffff1f] animate-tb37-spin [animation-duration:4.6s] [animation-play-state:paused] group-hover:[animation-play-state:running] motion-reduce:animate-none"></span>
        </span>
        <span class="tb-37__label relative flex items-end justify-between gap-3 px-3 py-2 rounded-[0.2rem] shadow-[inset_0_0_0_1px_#0000001f]">
          <span class="relative z-20 font-tb37-hand text-2xl font-bold text-tb37-ink">the drive home</span>
          <span class="text-xs font-bold tracking-[0.14em] text-tb37-accent px-1.5 py-0.5 rounded-[0.2rem] bg-tb37-accent-tint">B</span>
        </span>
      </span>
    </span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb37-bg: #181a20;
  --color-tb37-bg: oklch(0.2 0.012 275);
  --color-tb37-shell: #2b2f38;
  --color-tb37-shell: oklch(0.28 0.015 275);
  --color-tb37-shell-hi: #3b414d;
  --color-tb37-shell-hi: oklch(0.35 0.018 275);
  --color-tb37-paper: #f2ead6;
  --color-tb37-paper: oklch(0.93 0.03 90);
  --color-tb37-ink: #2c2419;
  --color-tb37-ink: oklch(0.26 0.025 75);
  --color-tb37-hub: #dfe3ea;
  --color-tb37-tape: #3a2a1c;
  --color-tb37-teeth: #9aa2b0;
  --color-tb37-accent: #c2452a;
  --color-tb37-accent: oklch(0.53 0.17 32);
  --color-tb37-accent-tint: #c2452a29;
  --color-tb37-accent-tint: oklch(0.53 0.17 32 / 0.16);
  --font-tb37-hand: "Caveat", ui-rounded, cursive;
  --font-tb37-sans: "Archivo", ui-sans-serif, system-ui, sans-serif;
  --ease-tb37-out: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tb37-spin: tb-37-spin 3.4s linear infinite;
}

@keyframes tb-37-spin {
  to {
    rotate: 1turn;
  }
}

.tb-37 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(34rem 20rem at 50% 44%, #23262f, transparent 74%), var(--color-tb37-bg);
}
/* PLASTIC SHELL: top-light over a diagonal body. */

.tb-37__face {
  background: linear-gradient(180deg, rgba(255,255,255,.12), transparent 34%), linear-gradient(165deg, var(--color-tb37-shell-hi), var(--color-tb37-shell));
}
/* REELS: spool teeth (repeating conic) over hub + wound tape (radial). Four reels
   across two faces must be identical, so the recipe lives once. */

.tb-37__reel {
  background: repeating-conic-gradient(from 0deg, var(--color-tb37-teeth) 0 8deg, transparent 8deg 30deg), radial-gradient(circle, var(--color-tb37-hub) 30%, var(--color-tb37-tape) 33%, var(--color-tb37-tape) 80%, transparent 81%);
}
/* AGED LABEL + its ruled line. */

.tb-37__label {
  background: linear-gradient(180deg, color-mix(in oklab, var(--color-tb37-paper) 92%, white), var(--color-tb37-paper));
}

.tb-37__label::after {
  content: '';
  position: absolute;
  left: .8rem;
  right: 3rem;
  bottom: .55rem;
  height: 1px;
  background: color-mix(in oklab, var(--color-tb37-ink) 22%, transparent);
}

@media (prefers-color-scheme: light) {
  .tb-37:not([data-theme="dark"]) {
    --color-tb37-bg: oklch(0.24 0.015 275);
  }
}

.tb-37[data-theme="light"] {
  --color-tb37-bg: oklch(0.24 0.015 275);
}

@media (forced-colors: active) {
  .tb-37__face {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .tb-37__label {
    background: Canvas;
  }

  .tb-37__label span {
    color: CanvasText;
  }
}
```
