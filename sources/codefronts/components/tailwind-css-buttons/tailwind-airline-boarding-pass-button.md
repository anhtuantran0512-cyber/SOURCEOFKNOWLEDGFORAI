---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-airline-boarding-pass-button/"
title: "Tailwind Airline Boarding Pass Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A boarding pass with a genuinely perforated seam: a mask punches half-circles down the divide, the stub tears away and rotates on hover, and a barcode is…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Airline Boarding Pass Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-airline-boarding-pass-button/

A boarding pass with a genuinely perforated seam: a mask punches half-circles down the divide, the stub tears away and rotates on hover, and a barcode is drawn with one repeating gradient. Flight numbers use tabular-nums so nothing shifts as they change.
## HTML
```html
<div class="tb-41 w-full min-h-svh grid place-items-center font-tb41-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="group relative cursor-pointer border-0 p-0 bg-transparent grid grid-cols-[1fr_auto] items-stretch w-[min(100%,30rem)] text-left text-tb41-ink drop-shadow-[0_18px_26px_#0000008c] transition-[translate,filter] duration-[350ms] ease-tb41-out [-webkit-tap-highlight-color:transparent] hover:-translate-y-[3px] hover:drop-shadow-[0_26px_34px_#00000099] focus-visible:-translate-y-[3px] focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tb41-brand active:translate-y-px disabled:cursor-not-allowed disabled:grayscale-[0.6] motion-reduce:transition-none">
    <span class="tb-41__body grid gap-3 px-4.5 pt-4 pb-4.5 rounded-l-[0.6rem] border-r border-dashed border-tb41-seam">
      <span class="flex items-baseline justify-between gap-3">
        <span class="text-xs font-extrabold tracking-[0.16em] uppercase text-tb41-brand">Meridian Air</span>
        <span class="text-[0.6875rem] font-semibold tracking-[0.06em] tabular-nums text-tb41-muted">14A · Zone 2</span>
      </span>
      <span class="flex items-center gap-3">
        <span class="text-3xl font-extrabold tracking-[-0.02em] leading-none">LHR</span>
        <svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor" class="size-5 text-tb41-brand transition-transform duration-500 ease-tb41-out group-hover:translate-x-1.5 group-focus-visible:translate-x-1.5 motion-reduce:transition-none"><path d="M2 13.5 22 9l-1 3.2-6.6 2.2-2.2 5.1-2.1.6 1-5-6.6 2.2L2 13.5z"/></svg>
        <span class="text-3xl font-extrabold tracking-[-0.02em] leading-none">JFK</span>
      </span>
      <span class="flex flex-wrap gap-x-4.5 gap-y-1.5 text-xs tabular-nums text-tb41-muted">
        <span>Boards <b class="font-bold text-tb41-ink">18:40</b></span>
        <span>Gate <b class="font-bold text-tb41-ink">B22</b></span>
        <span>Flt <b class="font-bold text-tb41-ink">MA 214</b></span>
      </span>
    </span>
    <span class="tb-41__stub grid gap-2 justify-items-center content-center px-3.5 py-4 rounded-r-[0.6rem] origin-left transition-[rotate,translate] duration-[450ms] ease-tb41-out group-hover:rotate-[3.5deg] group-hover:translate-x-[0.4rem] group-focus-visible:rotate-[3.5deg] group-focus-visible:translate-x-[0.4rem] motion-reduce:transition-none">
      <span class="text-[0.625rem] font-extrabold tracking-[0.14em] uppercase text-center text-tb41-brand">Tap to check in</span>
      <span aria-hidden="true" class="block w-18 h-10 bg-[repeating-linear-gradient(90deg,var(--color-tb41-ink)_0_2px,transparent_2px_4px,var(--color-tb41-ink)_4px_5px,transparent_5px_8px,var(--color-tb41-ink)_8px_11px,transparent_11px_12px,var(--color-tb41-ink)_12px_13px,transparent_13px_16px)]"></span>
      <span class="text-[0.9375rem] font-extrabold tracking-[0.04em] tabular-nums">14A</span>
    </span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb41-bg: #0e1b24;
  --color-tb41-bg: oklch(0.22 0.03 235);
  --color-tb41-card: #fbfbf8;
  --color-tb41-card: oklch(0.985 0.004 90);
  --color-tb41-card-lo: #eceae2;
  --color-tb41-card-lo: oklch(0.93 0.006 90);
  --color-tb41-ink: #131a20;
  --color-tb41-ink: oklch(0.2 0.015 240);
  --color-tb41-muted: #5b646f;
  --color-tb41-muted: oklch(0.47 0.015 240);
  --color-tb41-brand: #0f5f7a;
  --color-tb41-brand: oklch(0.45 0.09 217);
  --color-tb41-seam: #131a2047;
  --color-tb41-seam: oklch(0.2 0.015 240 / 0.28);
  --font-tb41-sans: "Archivo", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb41-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-41 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(38rem 24rem at 50% 30%, #16303e, transparent 72%), var(--color-tb41-bg);
}

.tb-41__body,
.tb-41__stub {
  background: linear-gradient(170deg, var(--color-tb41-card), var(--color-tb41-card-lo));
}
/* THE PERFORATION. Each piece carries its OWN half of the seam, on its own edge.
   Masking the whole button instead leaves the dot column behind in the button's
   coordinate space — so once the stub rotates, the holes stop following it and
   start slicing its corners. XOR, not intersect: intersect would erase everything
   except the .6rem dot column. */

@supports ((mask-composite: exclude) or (-webkit-mask-composite: xor)) {
  .tb-41__body {
    -webkit-mask: radial-gradient(.3rem .3rem at 100% 50%, #000 96%, transparent 0) 100% -.475rem/.6rem .95rem repeat-y, linear-gradient(#000, #000);
    mask: radial-gradient(.3rem .3rem at 100% 50%, #000 96%, transparent 0) 100% -.475rem/.6rem .95rem repeat-y, linear-gradient(#000, #000);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    border-right: 0;
  }

  .tb-41__stub {
    -webkit-mask: radial-gradient(.3rem .3rem at 0 50%, #000 96%, transparent 0) 0 -.475rem/.6rem .95rem repeat-y, linear-gradient(#000, #000);
    mask: radial-gradient(.3rem .3rem at 0 50%, #000 96%, transparent 0) 0 -.475rem/.6rem .95rem repeat-y, linear-gradient(#000, #000);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
  }
}

@media (prefers-color-scheme: light) {
  .tb-41:not([data-theme="dark"]) {
    --color-tb41-bg: oklch(0.3 0.04 235);
  }
}

.tb-41[data-theme="light"] {
  --color-tb41-bg: oklch(0.3 0.04 235);
}

@media (forced-colors: active) {
  .tb-41 button {
    mask: none;
    -webkit-mask: none;
    filter: none;
  }

  .tb-41__body,
    .tb-41__stub {
    background: ButtonFace;
    border: 1px solid ButtonText;
    color: ButtonText;
  }

  .tb-41__stub span[aria-hidden] {
    background: ButtonText;
  }
}
```
