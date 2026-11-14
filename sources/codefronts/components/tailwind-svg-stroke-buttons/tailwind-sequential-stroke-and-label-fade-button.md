---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-sequential-stroke-and-label-fade-button/"
title: "Tailwind Sequential Stroke and Label Fade Button"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "Four beats in, four beats out &mdash; and both ladders are visible on the same elements, because every step carries a delay-[...] for leaving and a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sequential Stroke and Label Fade Button
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-sequential-stroke-and-label-fade-button/

Four beats in, four beats out &mdash; and both ladders are visible on the same elements, because every step carries a delay-[...] for leaving and a group-hover:delay-[...] for arriving. All eight delays are multiples of one variable via delay-[calc(var(--svgb-13-step)*2.6)], so changing the beat retimes the whole cascade, and the second card becomes a two-beat version by setting that variable inline.
## HTML
```html
<section class="svgb-13 relative block w-full min-h-svh bg-svgb13-bg text-svgb13-fg font-svgb13-sans">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-13-theme">
  <label class="absolute z-[5] top-4 right-4 grid place-items-center size-11 rounded-full border border-current/22 bg-current/7 cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/14 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-13-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="relative min-h-svh grid place-items-center p-[clamp(22px,5vw,70px)]">
    <div class="flex flex-col items-center gap-[clamp(18px,3vw,30px)]">
      <p class="m-0 font-svgb13-serif text-[13px] tracking-[0.42em] uppercase text-svgb13-muted">Maison Verrier &middot; Est. 1904</p>
      <button class="group relative w-[min(420px,92vw)] h-50 grid place-items-center border-0 p-0 bg-svgb13-fg/3 cursor-pointer focus-visible:outline-1 focus-visible:outline-svgb13-stroke focus-visible:outline-offset-8" type="button">
        <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 420 200" aria-hidden="true">
          <rect class="fill-none stroke-svgb13-rest [stroke-width:1]" x="2" y="2" width="416" height="196" pathLength="1"/>
          <rect class="fill-none stroke-svgb13-rest [stroke-width:1]" x="16" y="16" width="388" height="168" pathLength="1"/>
          <rect class="fill-none stroke-svgb13-stroke [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[620ms] ease-svgb13 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 [stroke-width:1.6] delay-[calc(var(--svgb-13-step)*1.6)] group-hover:delay-0 group-focus-visible:delay-0" x="2" y="2" width="416" height="196" pathLength="1"/>
          <rect class="fill-none stroke-svgb13-stroke [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[620ms] ease-svgb13 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 [stroke-width:0.9] delay-[calc(var(--svgb-13-step)*1.2)] group-hover:delay-[calc(var(--svgb-13-step)*1.4)] group-focus-visible:delay-[calc(var(--svgb-13-step)*1.4)]" x="16" y="16" width="388" height="168" pathLength="1"/>
        </svg>
        <span class="relative z-[1] flex flex-col items-center gap-2 px-10 text-center">
          <span class="text-[9.5px] tracking-[0.34em] uppercase text-svgb13-muted opacity-75 transition-[opacity,color] duration-[460ms] delay-[calc(var(--svgb-13-step)*0.6)] motion-reduce:!transition-none group-hover:opacity-100 group-hover:text-svgb13-stroke group-hover:delay-[calc(var(--svgb-13-step)*2.4)] group-focus-visible:opacity-100 group-focus-visible:text-svgb13-stroke group-focus-visible:delay-[calc(var(--svgb-13-step)*2.4)]">Private view</span>
          <span class="font-svgb13-serif text-[clamp(28px,4.6vw,44px)] font-normal leading-[1.05] tracking-[0.01em] opacity-66 [transition:opacity_460ms_ease,letter-spacing_620ms_var(--ease-svgb13),color_460ms_ease] delay-[calc(var(--svgb-13-step)*0.3)] motion-reduce:!transition-none group-hover:opacity-100 group-hover:tracking-[0.06em] group-hover:delay-[calc(var(--svgb-13-step)*2.6)] group-focus-visible:opacity-100 group-focus-visible:tracking-[0.06em] group-focus-visible:delay-[calc(var(--svgb-13-step)*2.6)]">The Glass Hours</span>
          <span class="text-[11.5px] tracking-[0.16em] uppercase text-svgb13-muted opacity-0 translate-y-[5px] transition-[opacity,translate] duration-[320ms] delay-0 motion-reduce:!transition-none group-hover:opacity-100 group-hover:translate-y-0 group-hover:delay-[calc(var(--svgb-13-step)*3.1)] group-focus-visible:opacity-100 group-focus-visible:translate-y-0 group-focus-visible:delay-[calc(var(--svgb-13-step)*3.1)]">Thursday, 12 November &middot; 19:00</span>
          <span class="absolute -bottom-[26px] -right-[14px] grid place-items-center size-[54px] opacity-0 scale-90 transition-[opacity,scale] duration-[420ms] delay-0 motion-reduce:!transition-none group-hover:opacity-100 group-hover:scale-100 group-hover:delay-[calc(var(--svgb-13-step)*3.6)] group-focus-visible:opacity-100 group-focus-visible:scale-100 group-focus-visible:delay-[calc(var(--svgb-13-step)*3.6)] [&_svg]:absolute [&_svg]:inset-0 [&_svg]:w-full [&_svg]:h-full" aria-hidden="true">
            <svg viewBox="0 0 40 40" aria-hidden="true">
              <circle class="fill-none stroke-svgb13-stroke [stroke-width:1.4] [stroke-linecap:round] [stroke-linejoin:round]" cx="20" cy="20" r="17" pathLength="1"/>
              <path class="fill-none stroke-svgb13-stroke [stroke-width:1.4] [stroke-linecap:round] [stroke-linejoin:round]" d="M13 21.5 18 26.5 27.5 14" pathLength="1"/>
            </svg>
            <span class="relative text-[7.5px] tracking-[0.18em] uppercase text-svgb13-stroke">RSVP</span>
          </span>
        </span>
      </button>
      <button class="group relative w-[min(420px,92vw)] h-50 grid place-items-center border-0 p-0 bg-svgb13-fg/3 cursor-pointer focus-visible:outline-1 focus-visible:outline-svgb13-stroke focus-visible:outline-offset-8 [--svgb-13-step:0ms]" type="button">
        <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 420 200" aria-hidden="true">
          <rect class="fill-none stroke-svgb13-rest [stroke-width:1]" x="2" y="2" width="416" height="196" pathLength="1"/>
          <rect class="fill-none stroke-svgb13-rest [stroke-width:1]" x="16" y="16" width="388" height="168" pathLength="1"/>
          <rect class="fill-none stroke-svgb13-stroke [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[620ms] ease-svgb13 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 [stroke-width:1.6] delay-[calc(var(--svgb-13-step)*1.6)] group-hover:delay-0 group-focus-visible:delay-0" x="2" y="2" width="416" height="196" pathLength="1"/>
          <rect class="fill-none stroke-svgb13-stroke [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[620ms] ease-svgb13 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 [stroke-width:0.9] delay-[calc(var(--svgb-13-step)*1.2)] group-hover:delay-[calc(var(--svgb-13-step)*1.4)] group-focus-visible:delay-[calc(var(--svgb-13-step)*1.4)]" x="16" y="16" width="388" height="168" pathLength="1"/>
        </svg>
        <span class="relative z-[1] flex flex-col items-center gap-2 px-10 text-center">
          <span class="text-[9.5px] tracking-[0.34em] uppercase text-svgb13-muted opacity-75 transition-[opacity,color] duration-[460ms] delay-[calc(var(--svgb-13-step)*0.6)] motion-reduce:!transition-none group-hover:opacity-100 group-hover:text-svgb13-stroke group-hover:delay-[calc(var(--svgb-13-step)*2.4)] group-focus-visible:opacity-100 group-focus-visible:text-svgb13-stroke group-focus-visible:delay-[calc(var(--svgb-13-step)*2.4)]">Two-beat version</span>
          <span class="font-svgb13-serif text-[clamp(28px,4.6vw,44px)] font-normal leading-[1.05] tracking-[0.01em] opacity-66 [transition:opacity_460ms_ease,letter-spacing_620ms_var(--ease-svgb13),color_460ms_ease] delay-[calc(var(--svgb-13-step)*0.3)] motion-reduce:!transition-none group-hover:opacity-100 group-hover:tracking-[0.06em] group-hover:delay-[200ms] group-focus-visible:opacity-100 group-focus-visible:tracking-[0.06em] group-focus-visible:delay-[200ms]">Waiting list</span>
          <span class="text-[11.5px] tracking-[0.16em] uppercase text-svgb13-muted opacity-0 translate-y-[5px] transition-[opacity,translate] duration-[320ms] delay-0 motion-reduce:!transition-none group-hover:opacity-100 group-hover:translate-y-0 group-hover:delay-[240ms] group-focus-visible:opacity-100 group-focus-visible:translate-y-0 group-focus-visible:delay-[240ms]">Frames together &middot; text at 200ms</span>
          <span class="absolute -bottom-[26px] -right-[14px] grid place-items-center size-[54px] opacity-0 scale-90 transition-[opacity,scale] duration-[420ms] delay-0 motion-reduce:!transition-none group-hover:opacity-100 group-hover:scale-100 group-hover:delay-[280ms] group-focus-visible:opacity-100 group-focus-visible:scale-100 group-focus-visible:delay-[280ms] [&_svg]:absolute [&_svg]:inset-0 [&_svg]:w-full [&_svg]:h-full" aria-hidden="true">
            <svg viewBox="0 0 40 40" aria-hidden="true">
              <circle class="fill-none stroke-svgb13-stroke [stroke-width:1.4] [stroke-linecap:round] [stroke-linejoin:round]" cx="20" cy="20" r="17" pathLength="1"/>
              <path class="fill-none stroke-svgb13-stroke [stroke-width:1.4] [stroke-linecap:round] [stroke-linejoin:round]" d="M13 21.5 18 26.5 27.5 14" pathLength="1"/>
            </svg>
            <span class="relative text-[7.5px] tracking-[0.18em] uppercase text-svgb13-stroke">Join</span>
          </span>
        </span>
      </button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb13-bg: #100e0a;
  --color-svgb13-bg: oklch(0.175 0.012 70);
  --color-svgb13-fg: #f4eee1;
  --color-svgb13-fg: oklch(0.95 0.02 85);
  --color-svgb13-muted: #a2967f;
  --color-svgb13-muted: oklch(0.68 0.028 80);
  --color-svgb13-rest: rgba(244, 238, 225, 0.14);
  --color-svgb13-rest: oklch(0.95 0.02 85 / 0.14);
  --color-svgb13-stroke: #d9b26a;
  --color-svgb13-stroke: oklch(0.79 0.10 82);
  --font-svgb13-sans: 'Manrope', system-ui, sans-serif;
  --font-svgb13-serif: 'Cormorant Garamond', ui-serif, Georgia, serif;
  --ease-svgb13: cubic-bezier(0.22, 1, 0.36, 1);
}
/* One beat length. Every delay in the markup is a multiple of it, so the whole
   four-step cascade retimes from this single value — and the second card sets
   it to 0ms inline to become a two-beat version. */

.svgb-13 {
  --svgb-13-step: 130ms;
}

.svgb-13::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(60% 50% at 50% 30%, color-mix(in oklab, var(--color-svgb13-stroke) 9%, transparent), transparent 70%);
}

.svgb-13:has(#svgb-13-theme:checked) {
  --color-svgb13-bg: #f7f3ea;
  --color-svgb13-bg: oklch(0.968 0.014 85);
  --color-svgb13-fg: #1b1710;
  --color-svgb13-fg: oklch(0.215 0.015 70);
  --color-svgb13-muted: #6f6551;
  --color-svgb13-muted: oklch(0.525 0.025 80);
  --color-svgb13-rest: rgba(27, 23, 16, 0.16);
  --color-svgb13-rest: oklch(0.215 0.015 70 / 0.16);
  --color-svgb13-stroke: #7a5a12;
  --color-svgb13-stroke: oklch(0.50 0.10 80);
}
```
