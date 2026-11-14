---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-chalkboard-menu-button/"
title: "Tailwind Chalkboard Menu Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "Slate with real chalk behaviour: a dusty uneven board, a hand-drawn double border, letterforms that sit in the tooth of the surface, and a puff of chalk dust…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Chalkboard Menu Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-chalkboard-menu-button/

Slate with real chalk behaviour: a dusty uneven board, a hand-drawn double border, letterforms that sit in the tooth of the surface, and a puff of chalk dust when you press. Hover wipes a faint smudge across the board.
## HTML
```html
<div class="tb-38 w-full min-h-svh grid place-items-center font-tb38-hand p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="tb-38__board group relative cursor-pointer grid place-items-center min-h-17 px-11 border-2 border-dashed border-tb38-chalk-52 rounded-lg text-2xl tracking-[0.02em] shadow-[0_16px_26px_-16px_#000000cc,inset_0_0_30px_#00000059] transition-[translate,box-shadow] duration-[220ms] ease-tb38-out [-webkit-tap-highlight-color:transparent] before:content-[''] before:absolute before:inset-1.5 before:pointer-events-none before:border before:border-dashed before:border-tb38-chalk-28 before:rounded-[0.35rem] before:rotate-[0.25deg] hover:-translate-y-0.5 focus-visible:-translate-y-0.5 focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tb38-chalk active:translate-y-px active:shadow-[0_6px_12px_-10px_#000000cc,inset_0_0_36px_#00000073] disabled:cursor-not-allowed disabled:opacity-55 motion-reduce:transition-none">
    <span aria-hidden="true" class="absolute inset-0 z-20 pointer-events-none opacity-0 bg-[linear-gradient(104deg,transparent_30%,rgba(244,241,230,0.1)_50%,transparent_70%)] transition-opacity duration-[400ms] group-hover:opacity-100 group-focus-visible:opacity-100 motion-reduce:transition-none"></span>
    <span aria-hidden="true" class="absolute left-1/2 -bottom-2 w-32 h-5 -ml-16 rounded-[50%] pointer-events-none opacity-0 blur-[4px] bg-[radial-gradient(closest-side,rgba(244,241,230,0.6),transparent_74%)] group-active:animate-tb38-dust motion-reduce:hidden"></span>
    <span class="relative z-30 text-tb38-chalk-92 [text-shadow:0_0_1px_var(--color-tb38-chalk-55),0_0_7px_var(--color-tb38-chalk-20),0_1px_0_#00000059]">Today's special</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb38-bg: #20242b;
  --color-tb38-bg: oklch(0.26 0.015 265);
  --color-tb38-slate: #26302f;
  --color-tb38-slate: oklch(0.3 0.015 175);
  --color-tb38-slate-2: #1b2322;
  --color-tb38-slate-2: oklch(0.23 0.015 175);
  --color-tb38-chalk: #f4f1e6;
  --color-tb38-chalk: oklch(0.96 0.01 90);
  --color-tb38-chalk-92: #f4f1e6eb;
  --color-tb38-chalk-92: oklch(0.96 0.01 90 / 0.92);
  --color-tb38-chalk-55: #f4f1e68c;
  --color-tb38-chalk-55: oklch(0.96 0.01 90 / 0.55);
  --color-tb38-chalk-52: #f4f1e685;
  --color-tb38-chalk-52: oklch(0.96 0.01 90 / 0.52);
  --color-tb38-chalk-28: #f4f1e647;
  --color-tb38-chalk-28: oklch(0.96 0.01 90 / 0.28);
  --color-tb38-chalk-20: #f4f1e633;
  --color-tb38-chalk-20: oklch(0.96 0.01 90 / 0.2);
  --font-tb38-hand: "Patrick Hand", ui-rounded, "Comic Sans MS", cursive;
  --ease-tb38-out: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tb38-dust: tb-38-dust 0.6s ease-out;
}

@keyframes tb-38-dust {
  0% {
    opacity: 0.75;
    scale: 0.4 0.5;
  }

  100% {
    opacity: 0;
    scale: 1.6 1.4;
  }
}

.tb-38 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: repeating-linear-gradient(92deg, rgba(0,0,0,.05) 0 2px, transparent 2px 9px), var(--color-tb38-bg);
}
/* THE SLATE: two dust speckle tiles, two broad washes, and the base. */

.tb-38__board {
  background-color: var(--color-tb38-slate);
  background-image: radial-gradient(.08rem .08rem at 24% 36%, rgba(244,241,230,.2) 99%, transparent), radial-gradient(.06rem .06rem at 68% 72%, rgba(244,241,230,.16) 99%, transparent), radial-gradient(8rem 5rem at 20% 15%, rgba(255,255,255,.05), transparent 70%), radial-gradient(9rem 6rem at 82% 88%, rgba(255,255,255,.04), transparent 72%), linear-gradient(160deg, var(--color-tb38-slate), var(--color-tb38-slate-2));
  background-size: 9px 9px, 13px 13px, 100% 100%, 100% 100%, 100% 100%;
}

@media (prefers-color-scheme: light) {
  .tb-38:not([data-theme="dark"]) {
    --color-tb38-bg: oklch(0.32 0.015 265);
  }
}

.tb-38[data-theme="light"] {
  --color-tb38-bg: oklch(0.32 0.015 265);
}

@media (forced-colors: active) {
  .tb-38__board {
    background: ButtonFace;
    border: 2px solid ButtonText;
    box-shadow: none;
  }

  .tb-38__board::before {
    display: none;
  }

  .tb-38__board span {
    color: ButtonText;
    text-shadow: none;
  }

  .tb-38__board span[aria-hidden] {
    display: none;
  }
}
```
