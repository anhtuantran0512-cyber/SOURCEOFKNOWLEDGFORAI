---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-focus-visible-stroke-outline-for-keyboard-users/"
title: "Tailwind Focus Visible Stroke Outline for Keyboard Users"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "The accessibility argument of the collection, expressed as a naming convention: every hover utility here has a group-focus-visible: twin, so typing one and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Focus Visible Stroke Outline for Keyboard Users
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-focus-visible-stroke-outline-for-keyboard-users/

The accessibility argument of the collection, expressed as a naming convention: every hover utility here has a group-focus-visible: twin, so typing one and not the other leaves a visible hole in the class list. Focus also thickens the stroke and shortens the draw &mdash; a keyboard user is waiting on it, not exploring &mdash; and the forced-colors block stays in CSS because system keywords are not theme tokens.
## HTML
```html
<section class="svgb-09 relative block w-full min-h-svh bg-svgb09-bg text-svgb09-fg font-svgb09-sans">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-09-theme">
  <label class="absolute z-[5] top-4 right-4 grid place-items-center size-11 rounded-lg border border-current/22 bg-current/6 cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/13 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-09-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="min-h-svh grid place-items-center p-[clamp(20px,5vw,64px)]">
    <div class="w-full max-w-140 flex flex-col gap-3.5 p-[clamp(22px,4vw,40px)] rounded-[10px] bg-svgb09-card border border-svgb09-rest">
      <div class="flex flex-wrap justify-between items-baseline gap-3">
        <span class="text-sm font-bold tracking-[0.14em] uppercase">Meridian</span>
        <span class="inline-flex items-center gap-2 font-svgb09-mono text-[11px] text-svgb09-muted"><kbd class="font-[inherit] text-[10.5px] px-2 py-1 rounded-[5px] border border-svgb09-rest shadow-[0_1.5px_0_var(--color-svgb09-rest)]">Tab</kbd> walks the order</span>
      </div>
      <p class="mt-2 mb-0 text-[clamp(34px,6vw,52px)] font-bold tracking-[-0.03em] tabular-nums">&pound;1,480.00</p>
      <p class="mt-0 mb-2.5 text-[13.5px] leading-normal text-svgb09-muted [&_strong]:text-svgb09-fg [&_strong]:font-semibold">to <strong>Halden Studio Ltd</strong> &middot; sort 20-45-11 &middot; acct &bull;&bull;&bull;&bull;8842</p>

      <ol class="list-none m-0 p-0 flex flex-col gap-3">
        <li class="flex items-center gap-3.5">
          <span class="flex-none size-[22px] grid place-items-center rounded-full border border-svgb09-rest font-svgb09-mono text-[10.5px] text-svgb09-muted" aria-hidden="true">1</span>
          <button class="group relative w-[min(340px,100%)] h-15 grid place-items-center border-0 p-0 rounded-lg bg-svgb09-stroke/12 text-[15px] font-semibold cursor-pointer focus:outline-none focus-visible:outline-2 focus-visible:outline-svgb09-ring focus-visible:outline-offset-[3px] focus-visible:shadow-[0_0_0_5px_var(--color-svgb09-ring2)]" type="button">
            <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 340 60" aria-hidden="true">
              <rect class="fill-none stroke-svgb09-rest [stroke-width:1.4] [stroke-linecap:round]" x="1.5" y="1.5" width="337" height="57" rx="8" vector-effect="non-scaling-stroke"/>
              <rect class="fill-none stroke-svgb09-stroke [stroke-width:2] [stroke-linecap:round] [stroke-dasharray:780] [stroke-dashoffset:780] [transition:stroke-dashoffset_560ms_cubic-bezier(0.22,1,0.36,1),stroke-width_160ms_ease] group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] group-focus-visible:[stroke-width:2.8] group-focus-visible:[transition-duration:240ms] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" x="1.5" y="1.5" width="337" height="57" rx="8" vector-effect="non-scaling-stroke"/>
            </svg>
            <span class="relative z-[1]">Confirm payment</span>
          </button>
        </li>
        <li class="flex items-center gap-3.5">
          <span class="flex-none size-[22px] grid place-items-center rounded-full border border-svgb09-rest font-svgb09-mono text-[10.5px] text-svgb09-muted" aria-hidden="true">2</span>
          <button class="group relative w-[min(340px,100%)] h-15 grid place-items-center border-0 p-0 rounded-lg bg-svgb09-fg/4 text-[15px] font-medium cursor-pointer focus:outline-none focus-visible:outline-2 focus-visible:outline-svgb09-ring focus-visible:outline-offset-[3px] focus-visible:shadow-[0_0_0_5px_var(--color-svgb09-ring2)]" type="button">
            <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 340 60" aria-hidden="true">
              <rect class="fill-none stroke-svgb09-rest [stroke-width:1.4] [stroke-linecap:round]" x="1.5" y="1.5" width="337" height="57" rx="8" vector-effect="non-scaling-stroke"/>
              <rect class="fill-none stroke-svgb09-stroke [stroke-width:2] [stroke-linecap:round] [stroke-dasharray:780] [stroke-dashoffset:780] [transition:stroke-dashoffset_560ms_cubic-bezier(0.22,1,0.36,1),stroke-width_160ms_ease] group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] group-focus-visible:[stroke-width:2.8] group-focus-visible:[transition-duration:240ms] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" x="1.5" y="1.5" width="337" height="57" rx="8" vector-effect="non-scaling-stroke"/>
            </svg>
            <span class="relative z-[1]">Schedule for 1 October</span>
          </button>
        </li>
        <li class="flex items-center gap-3.5">
          <span class="flex-none size-[22px] grid place-items-center rounded-full border border-svgb09-rest font-svgb09-mono text-[10.5px] text-svgb09-muted" aria-hidden="true">3</span>
          <button class="group relative w-[min(340px,100%)] h-15 grid place-items-center border-0 p-0 rounded-lg bg-svgb09-fg/4 text-[15px] font-medium cursor-pointer focus:outline-none focus-visible:outline-2 focus-visible:outline-svgb09-ring focus-visible:outline-offset-[3px] focus-visible:shadow-[0_0_0_5px_var(--color-svgb09-ring2)]" type="button">
            <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 340 60" aria-hidden="true">
              <rect class="fill-none stroke-svgb09-rest [stroke-width:1.4] [stroke-linecap:round]" x="1.5" y="1.5" width="337" height="57" rx="8" vector-effect="non-scaling-stroke"/>
              <rect class="fill-none stroke-svgb09-stroke [stroke-width:2] [stroke-linecap:round] [stroke-dasharray:780] [stroke-dashoffset:780] [transition:stroke-dashoffset_560ms_cubic-bezier(0.22,1,0.36,1),stroke-width_160ms_ease] group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] group-focus-visible:[stroke-width:2.8] group-focus-visible:[transition-duration:240ms] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" x="1.5" y="1.5" width="337" height="57" rx="8" vector-effect="non-scaling-stroke"/>
            </svg>
            <span class="relative z-[1]">Edit reference</span>
          </button>
        </li>
        <li class="flex items-center gap-3.5">
          <span class="flex-none size-[22px] grid place-items-center rounded-full border border-svgb09-rest font-svgb09-mono text-[10.5px] text-svgb09-muted" aria-hidden="true">4</span>
          <a class="text-svgb09-stroke text-sm font-medium underline decoration-1 underline-offset-[3px] rounded hover:decoration-2 focus-visible:outline-2 focus-visible:outline-svgb09-ring focus-visible:outline-offset-[3px] focus-visible:shadow-[0_0_0_5px_var(--color-svgb09-ring2)]" href="#svgb-09-terms">Payment limits and cut-off times</a>
        </li>
      </ol>

      <div class="flex flex-wrap gap-4 pt-3.5 mt-1 border-t border-svgb09-rest">
        <span class="inline-flex items-center gap-2 font-svgb09-mono text-[10.5px] text-svgb09-muted"><span class="w-[22px] h-3 rounded-[3px] border-2 border-svgb09-stroke"></span>hover &middot; 2px stroke only</span>
        <span class="inline-flex items-center gap-2 font-svgb09-mono text-[10.5px] text-svgb09-muted"><span class="w-[22px] h-3 rounded-[3px] border-2 border-svgb09-stroke outline-2 outline-svgb09-ring outline-offset-2"></span>focus-visible &middot; outline + stroke</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb09-bg: #eceef2;
  --color-svgb09-bg: oklch(0.945 0.005 265);
  --color-svgb09-fg: #0e1116;
  --color-svgb09-fg: oklch(0.175 0.008 265);
  --color-svgb09-muted: #545a66;
  --color-svgb09-muted: oklch(0.485 0.013 265);
  --color-svgb09-card: #ffffff;
  --color-svgb09-card: oklch(1 0 0);
  --color-svgb09-rest: rgba(14, 17, 22, 0.18);
  --color-svgb09-rest: oklch(0.175 0.008 265 / 0.18);
  --color-svgb09-stroke: #0b5cd6;
  --color-svgb09-stroke: oklch(0.47 0.20 260);
  --color-svgb09-ring: #0b0e14;
  --color-svgb09-ring: oklch(0.17 0.01 265);
  --color-svgb09-ring2: #ffffff;
  --color-svgb09-ring2: oklch(1 0 0);
  --font-svgb09-sans: 'Public Sans', system-ui, sans-serif;
  --font-svgb09-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.svgb-09:has(#svgb-09-theme:checked) {
  --color-svgb09-bg: #0c0f14;
  --color-svgb09-bg: oklch(0.17 0.008 265);
  --color-svgb09-fg: #edeff4;
  --color-svgb09-fg: oklch(0.955 0.005 265);
  --color-svgb09-muted: #8b91a0;
  --color-svgb09-muted: oklch(0.67 0.013 265);
  --color-svgb09-card: #14171e;
  --color-svgb09-card: oklch(0.215 0.01 265);
  --color-svgb09-rest: rgba(237, 239, 244, 0.18);
  --color-svgb09-rest: oklch(0.955 0.005 265 / 0.18);
  --color-svgb09-stroke: #7fb2ff;
  --color-svgb09-stroke: oklch(0.78 0.13 260);
  --color-svgb09-ring: #ffffff;
  --color-svgb09-ring: oklch(1 0 0);
  --color-svgb09-ring2: #00080f;
  --color-svgb09-ring2: oklch(0.14 0.02 250);
}
/* Forced-colors mode discards author colours and remaps a small system palette.
   An SVG stroke is not part of that palette, so the drawn border has to be
   surrendered and a real border put back. There is no utility for this because
   the values are system keywords, not tokens. */

@media (forced-colors: active) {
  .svgb-09 svg rect {
    stroke: transparent;
  }

  .svgb-09 button {
    border: 1px solid ButtonBorder;
  }

  .svgb-09 button:focus-visible,
    .svgb-09 a:focus-visible {
    outline: 3px solid Highlight;
    outline-offset: 3px;
    box-shadow: none;
  }
}
```
