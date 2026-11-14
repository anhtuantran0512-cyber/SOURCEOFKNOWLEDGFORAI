---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-3d-clay-button-press-squish-animation/"
title: "Tailwind 3D Clay Button with Press & Squish Animation"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "Six clay buttons with a real physical press: on active: the object squashes (scale-y-93), sinks 4px and swaps to an inverted-inset shadow, then springs back…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Clay Button with Press & Squish Animation
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-3d-clay-button-press-squish-animation/

Six clay buttons with a real physical press: on active: the object squashes (scale-y-93), sinks 4px and swaps to an inverted-inset shadow, then springs back on an overshooting curve. The port adds a latching toggle — a Follow pill that stays pressed in — and fixes the disabled button's redundant aria-disabled.
## HTML
```html
<section class="tcl-09 w-full min-h-svh grid place-items-center bg-tcl09-bg bg-[radial-gradient(75%_55%_at_50%_5%,var(--color-tcl09-glow),transparent_65%)] px-5 py-14 font-tcl09-sans text-tcl09-ink" aria-label="Clay button press and squish states demo">
  <div class="grid w-full justify-items-center gap-[clamp(26px,4vw,42px)]">
    <header class="grid max-w-[56ch] gap-2.5 text-center">
      <h2 class="font-tcl09-display text-[clamp(30px,4.4vw,44px)] font-semibold leading-[1.05] tracking-[-0.02em] text-balance">Press it. It squishes.</h2>
      <p class="text-[15px] leading-relaxed text-tcl09-mut text-pretty">Squash on Y, sink 4px, invert both insets — then release on a springy curve. Hold a button down to feel all three.</p>
    </header>
    <div class="flex w-full max-w-[900px] flex-wrap items-center justify-center gap-[clamp(12px,2vw,20px)]">
      <button type="button" class="grid min-h-[58px] cursor-pointer place-items-center rounded-[26px] bg-tcl09-accent px-8.5 font-tcl09-display text-base font-semibold shadow-tcl09-hero transition-[scale,translate,box-shadow,filter] duration-200 ease-[cubic-bezier(.2,.8,.3,1.5)] hover:-translate-y-0.75 hover:brightness-103 active:translate-y-1 active:scale-y-93 active:shadow-tcl09-press active:brightness-100 focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tcl09-ink motion-reduce:active:scale-y-100">Start lesson</button>
      <button type="button" class="grid min-h-[58px] cursor-pointer place-items-center rounded-[26px] bg-tcl09-clay px-7.5 font-tcl09-display text-[15px] font-semibold shadow-tcl09-rest transition-[scale,translate,box-shadow,filter] duration-200 ease-[cubic-bezier(.2,.8,.3,1.5)] hover:-translate-y-0.75 hover:brightness-103 active:translate-y-1 active:scale-y-93 active:shadow-tcl09-press active:brightness-100 focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tcl09-ink motion-reduce:active:scale-y-100">Save draft</button>
      <label class="grid min-h-[58px] cursor-pointer place-items-center rounded-full bg-tcl09-clay px-7.5 font-tcl09-display text-[15px] font-semibold shadow-tcl09-rest transition-[scale,translate,box-shadow,background-color] duration-200 ease-[cubic-bezier(.2,.8,.3,1.5)] select-none hover:-translate-y-0.75 active:translate-y-1 active:scale-y-93 active:shadow-tcl09-press has-checked:translate-y-0.5 has-checked:bg-tcl09-latched has-checked:shadow-tcl09-press has-focus-visible:outline-3 has-focus-visible:outline-offset-4 has-focus-visible:outline-tcl09-ink motion-reduce:active:scale-y-100">
        <input type="checkbox" class="peer sr-only" aria-label="Follow">
        <span aria-hidden="true" class="peer-checked:hidden">+ Follow</span><span aria-hidden="true" class="hidden peer-checked:inline">✓ Following</span>
      </label>
      <button type="button" aria-label="Add to favourites" class="grid size-[58px] cursor-pointer place-items-center rounded-[22px] bg-tcl09-clay text-tcl09-heart shadow-tcl09-rest transition-[scale,translate,box-shadow,filter] duration-200 ease-[cubic-bezier(.2,.8,.3,1.5)] hover:-translate-y-0.75 hover:brightness-103 active:translate-y-1 active:scale-93 active:shadow-tcl09-press focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tcl09-ink motion-reduce:active:scale-100">
        <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M12 20.3l-1.4-1.3C6 14.9 3.5 12.6 3.5 9.6A4.1 4.1 0 017.6 5.5c1.5 0 2.9.7 3.8 1.9.9-1.2 2.3-1.9 3.8-1.9a4.1 4.1 0 014.1 4.1c0 3-2.5 5.3-7.1 9.4z" fill="currentColor"/></svg>
      </button>
      <button type="button" class="grid min-h-[58px] cursor-pointer place-items-center rounded-[26px] bg-tcl09-danger px-7.5 font-tcl09-display text-[15px] font-semibold text-tcl09-dangerink shadow-tcl09-rest transition-[scale,translate,box-shadow,filter] duration-200 ease-[cubic-bezier(.2,.8,.3,1.5)] hover:-translate-y-0.75 hover:brightness-103 active:translate-y-1 active:scale-y-93 active:shadow-tcl09-press active:brightness-100 focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tcl09-ink motion-reduce:active:scale-y-100">Delete</button>
      <button type="button" disabled class="grid min-h-[58px] place-items-center rounded-[26px] bg-tcl09-soft px-7.5 font-tcl09-display text-[15px] font-semibold text-tcl09-mut shadow-tcl09-off disabled:cursor-not-allowed">Unavailable</button>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/55 px-4 py-2 text-center font-tcl09-mono text-[11.5px] text-tcl09-mut">active:scale-y-93 · active:translate-y-1 · active:shadow-tcl09-press · has-checked: latch</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcl09-bg: #daf2e6;
  --color-tcl09-bg: oklch(0.94 0.03 165);
  --color-tcl09-glow: #e0fdef;
  --color-tcl09-glow: oklch(0.97 0.035 165);
  --color-tcl09-clay: #b1e5d1;
  --color-tcl09-clay: oklch(0.88 0.06 170);
  --color-tcl09-soft: #e5f5ed;
  --color-tcl09-soft: oklch(0.955 0.02 165);
  --color-tcl09-accent: #79dd9f;
  --color-tcl09-accent: oklch(0.82 0.13 155);
  --color-tcl09-latched: #8fdfb4;
  --color-tcl09-latched: oklch(0.84 0.1 160);
  --color-tcl09-danger: #ff958c;
  --color-tcl09-danger: oklch(0.79 0.14 25);
  --color-tcl09-dangerink: #400c0c;
  --color-tcl09-dangerink: oklch(0.25 0.08 25);
  --color-tcl09-heart: #c4334f;
  --color-tcl09-heart: oklch(0.55 0.18 15);
  --color-tcl09-shade: #2e82698c;
  --color-tcl09-shade: oklch(0.55 0.09 170 / 0.55);
  --color-tcl09-light: #f6fffef2;
  --color-tcl09-light: oklch(1 0.015 170 / 0.95);
  --color-tcl09-ink: #042e23;
  --color-tcl09-ink: oklch(0.27 0.05 170);
  --color-tcl09-mut: #3e6054;
  --color-tcl09-mut: oklch(0.46 0.045 170);
  --font-tcl09-display: 'Fredoka', system-ui, sans-serif;
  --font-tcl09-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl09-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcl09-rest: 0 18px 30px -10px var(--color-tcl09-shade), inset 0 -14px 22px -10px var(--color-tcl09-shade), inset 0 16px 22px -8px var(--color-tcl09-light);
  --shadow-tcl09-hero: 0 22px 36px -12px var(--color-tcl09-shade), inset 0 -16px 24px -10px var(--color-tcl09-shade), inset 0 18px 24px -8px var(--color-tcl09-light);
  --shadow-tcl09-press: 0 0 0 0 transparent, inset 0 14px 20px -8px var(--color-tcl09-shade), inset 0 -10px 18px -10px var(--color-tcl09-light);
  --shadow-tcl09-off: 0 0 0 0 transparent, inset 0 6px 12px -8px var(--color-tcl09-shade), inset 0 -5px 10px -8px var(--color-tcl09-light);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-09 {
  width: 100%;
  min-height: 100svh;
}
```
