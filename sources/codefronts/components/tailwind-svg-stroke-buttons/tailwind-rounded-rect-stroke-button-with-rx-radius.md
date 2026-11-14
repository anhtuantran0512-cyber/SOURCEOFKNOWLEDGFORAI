---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-rounded-rect-stroke-button-with-rx-radius/"
title: "Tailwind Rounded Rect Stroke Button with rx Radius"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "A radius inspector where picking a value cannot desynchronise the maths, because the radius and its measured perimeter are published by the same checked…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Rounded Rect Stroke Button with rx Radius
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-rounded-rect-stroke-button-with-rx-radius/

A radius inspector where picking a value cannot desynchronise the maths, because the radius and its measured perimeter are published by the same checked radio and read in the same breath: [rx:var(--svgb-05-rx,8px)] next to [stroke-dasharray:var(--svgb-05-peri,915)]. The four ghost contours each read their own --svgb-05-g-* opacity variable, so one invalidation point drives all of them.
## HTML
```html
<section class="svgb-05 relative block w-full min-h-svh bg-svgb05-bg text-svgb05-fg font-svgb05-sans">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-05-theme">
  <label class="absolute z-[5] top-4 right-4 grid place-items-center size-11 rounded-full border border-current/20 bg-current/7 cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/15 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-05-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="min-h-svh grid place-items-center p-[clamp(20px,5vw,64px)]">
    <div class="svgb-05__panel w-full max-w-155 flex flex-col gap-[clamp(18px,3vw,26px)] p-[clamp(20px,4vw,34px)] rounded-[18px] bg-svgb05-panel shadow-[0_1px_2px_oklch(0_0_0/0.05),0_26px_60px_-44px_oklch(0_0_0/0.35)]">
      <div class="flex gap-1.5 p-[5px] rounded-xl bg-svgb05-fg/5" role="radiogroup" aria-label="Corner radius">
        <input class="svgb-05__r--0 peer/r0 absolute opacity-0 pointer-events-none" type="radio" name="svgb-05-rx" id="svgb-05-rx0">
        <label class="flex-1 min-h-10 grid place-items-center rounded-[9px] font-svgb05-mono text-[12.5px] cursor-pointer transition-[background-color,color] duration-200 motion-reduce:transition-none hover:text-svgb05-fg [background:var(--svgb-05-sb-0,transparent)] [color:var(--svgb-05-sc-0,var(--color-svgb05-muted))] [box-shadow:var(--svgb-05-ss-0,none)] peer-focus-visible:outline-2 peer-focus-visible:outline-svgb05-stroke peer-focus-visible:outline-offset-2" for="svgb-05-rx0">0</label>
        <input class="svgb-05__r--8 peer/r8 absolute opacity-0 pointer-events-none" type="radio" name="svgb-05-rx" id="svgb-05-rx8" checked>
        <label class="flex-1 min-h-10 grid place-items-center rounded-[9px] font-svgb05-mono text-[12.5px] cursor-pointer transition-[background-color,color] duration-200 motion-reduce:transition-none hover:text-svgb05-fg [background:var(--svgb-05-sb-8,transparent)] [color:var(--svgb-05-sc-8,var(--color-svgb05-muted))] [box-shadow:var(--svgb-05-ss-8,none)] peer-focus-visible:outline-2 peer-focus-visible:outline-svgb05-stroke peer-focus-visible:outline-offset-2" for="svgb-05-rx8">8</label>
        <input class="svgb-05__r--20 peer/r20 absolute opacity-0 pointer-events-none" type="radio" name="svgb-05-rx" id="svgb-05-rx20">
        <label class="flex-1 min-h-10 grid place-items-center rounded-[9px] font-svgb05-mono text-[12.5px] cursor-pointer transition-[background-color,color] duration-200 motion-reduce:transition-none hover:text-svgb05-fg [background:var(--svgb-05-sb-20,transparent)] [color:var(--svgb-05-sc-20,var(--color-svgb05-muted))] [box-shadow:var(--svgb-05-ss-20,none)] peer-focus-visible:outline-2 peer-focus-visible:outline-svgb05-stroke peer-focus-visible:outline-offset-2" for="svgb-05-rx20">20</label>
        <input class="svgb-05__r--52 peer/r52 absolute opacity-0 pointer-events-none" type="radio" name="svgb-05-rx" id="svgb-05-rx52">
        <label class="flex-1 min-h-10 grid place-items-center rounded-[9px] font-svgb05-mono text-[12.5px] cursor-pointer transition-[background-color,color] duration-200 motion-reduce:transition-none hover:text-svgb05-fg [background:var(--svgb-05-sb-52,transparent)] [color:var(--svgb-05-sc-52,var(--color-svgb05-muted))] [box-shadow:var(--svgb-05-ss-52,none)] peer-focus-visible:outline-2 peer-focus-visible:outline-svgb05-stroke peer-focus-visible:outline-offset-2" for="svgb-05-rx52">52 = h/2</label>
      </div>

      <div class="relative grid place-items-center py-[clamp(18px,4vw,32px)]">
        <span class="absolute inset-x-0 top-0 h-full opacity-70 [background:repeating-linear-gradient(90deg,var(--color-svgb05-rest)_0_1px,transparent_1px_20px)] [mask-image:linear-gradient(#000_0_6px,transparent_6px_calc(100%-6px),#000_calc(100%-6px))]" aria-hidden="true"></span>
        <button class="group relative w-[min(360px,100%)] h-26 grid place-items-center border-0 p-0 bg-svgb05-stroke/6 shadow-[inset_0_0_0_1px_var(--color-svgb05-rest)] text-base font-medium cursor-pointer [border-radius:var(--svgb-05-rx,8px)] transition-[border-radius] duration-[420ms] ease-svgb05 motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-svgb05-stroke focus-visible:outline-offset-4" type="button">
          <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 360 104" aria-hidden="true">
            <rect class="fill-none stroke-svgb05-rest [stroke-width:1] [rx:0px] [opacity:var(--svgb-05-g-0,0.4)]" x="0" y="0" width="360" height="104"/>
            <rect class="fill-none stroke-svgb05-rest [stroke-width:1] [rx:8px] [opacity:var(--svgb-05-g-8,0.4)]" x="0" y="0" width="360" height="104"/>
            <rect class="fill-none stroke-svgb05-rest [stroke-width:1] [rx:20px] [opacity:var(--svgb-05-g-20,0.4)]" x="0" y="0" width="360" height="104"/>
            <rect class="fill-none stroke-svgb05-rest [stroke-width:1] [rx:52px] [opacity:var(--svgb-05-g-52,0.4)]" x="0" y="0" width="360" height="104"/>
            <rect class="fill-none stroke-svgb05-rest [stroke-width:1.5] [rx:var(--svgb-05-rx,8px)] transition-[rx] duration-[420ms] ease-svgb05 motion-reduce:transition-none" x="0" y="0" width="360" height="104"/>
            <rect class="fill-none stroke-svgb05-stroke [stroke-width:2.4] [stroke-linecap:butt] [rx:var(--svgb-05-rx,8px)] [stroke-dasharray:var(--svgb-05-peri,915)] [stroke-dashoffset:var(--svgb-05-peri,915)] [transition:rx_420ms_var(--ease-svgb05),stroke-dashoffset_720ms_var(--ease-svgb05)] group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" x="0" y="0" width="360" height="104"/>
          </svg>
          <span class="relative z-[1]">Hover to draw</span>
        </button>
      </div>

      <dl class="m-0 flex flex-col gap-0.5">
        <div class="grid grid-cols-[62px_1fr_auto] gap-3 items-center px-3 py-[9px] rounded-lg font-svgb05-mono text-[11.5px] transition-[background-color,color] duration-200 motion-reduce:transition-none [background:var(--svgb-05-hl-0,transparent)] [color:var(--svgb-05-hc-0,var(--color-svgb05-muted))] [&_dt]:m-0 [&_dd]:m-0"><dt>rx 0</dt><dd>2(360 + 104)</dd><dd class="tabular-nums">928</dd></div>
        <div class="grid grid-cols-[62px_1fr_auto] gap-3 items-center px-3 py-[9px] rounded-lg font-svgb05-mono text-[11.5px] transition-[background-color,color] duration-200 motion-reduce:transition-none [background:var(--svgb-05-hl-8,transparent)] [color:var(--svgb-05-hc-8,var(--color-svgb05-muted))] [&_dt]:m-0 [&_dd]:m-0"><dt>rx 8</dt><dd>2(344) + 2(88) + 2&pi;(8)</dd><dd class="tabular-nums">915</dd></div>
        <div class="grid grid-cols-[62px_1fr_auto] gap-3 items-center px-3 py-[9px] rounded-lg font-svgb05-mono text-[11.5px] transition-[background-color,color] duration-200 motion-reduce:transition-none [background:var(--svgb-05-hl-20,transparent)] [color:var(--svgb-05-hc-20,var(--color-svgb05-muted))] [&_dt]:m-0 [&_dd]:m-0"><dt>rx 20</dt><dd>2(320) + 2(64) + 2&pi;(20)</dd><dd class="tabular-nums">894</dd></div>
        <div class="grid grid-cols-[62px_1fr_auto] gap-3 items-center px-3 py-[9px] rounded-lg font-svgb05-mono text-[11.5px] transition-[background-color,color] duration-200 motion-reduce:transition-none [background:var(--svgb-05-hl-52,transparent)] [color:var(--svgb-05-hc-52,var(--color-svgb05-muted))] [&_dt]:m-0 [&_dd]:m-0"><dt>rx 52</dt><dd>2(256) + &pi;(104)</dd><dd class="tabular-nums">839</dd></div>
      </dl>
      <p class="m-0 flex gap-[9px] items-baseline text-[12.5px] leading-normal text-svgb05-muted"><span class="flex-none font-svgb05-mono text-[10px] tracking-[0.1em] uppercase px-[7px] py-[3px] rounded-[5px] bg-svgb05-fg/8">note</span> rx 999 is not a stadium in SVG &mdash; ry copies rx before clamping, so a 360&times;104 rect resolves to rx 180 / ry 52: an ellipse of about 785 units, not the 839-unit stadium.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb05-bg: #f4f4f6;
  --color-svgb05-bg: oklch(0.962 0.003 300);
  --color-svgb05-fg: #16161c;
  --color-svgb05-fg: oklch(0.20 0.006 300);
  --color-svgb05-muted: #62636f;
  --color-svgb05-muted: oklch(0.525 0.012 300);
  --color-svgb05-panel: #ffffff;
  --color-svgb05-panel: oklch(1 0 0);
  --color-svgb05-rest: rgba(22, 22, 28, 0.14);
  --color-svgb05-rest: oklch(0.20 0.006 300 / 0.14);
  --color-svgb05-stroke: #e5117a;
  --color-svgb05-stroke: oklch(0.58 0.24 358);
  --font-svgb05-sans: 'Outfit', system-ui, sans-serif;
  --font-svgb05-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-svgb05: cubic-bezier(0.16, 1, 0.3, 1);
}
/* One radio, one block, eight values. This is a state machine, not styling:
   the checked radius publishes its rx, its perimeter, its segment pill, its
   table row and which ghost contour to hide. Utilities in the markup read the
   variables; nothing here duplicates a utility. */

.svgb-05 {
  --svgb-05-hlbg: color-mix(in oklab, var(--color-svgb05-stroke) 10%, transparent);
  --svgb-05-hlfg: color-mix(in oklab, var(--color-svgb05-stroke) 70%, var(--color-svgb05-fg));
  --svgb-05-segsh: 0 1px 2px oklch(0 0 0 / 0.12);
}

.svgb-05:has(.svgb-05__r--0:checked) {
  --svgb-05-rx: 0px;
  --svgb-05-peri: 928;
  --svgb-05-g-0: 0;
  --svgb-05-hl-0: var(--svgb-05-hlbg);
  --svgb-05-hc-0: var(--svgb-05-hlfg);
  --svgb-05-sb-0: var(--color-svgb05-panel);
  --svgb-05-sc-0: var(--color-svgb05-fg);
  --svgb-05-ss-0: var(--svgb-05-segsh);
}

.svgb-05:has(.svgb-05__r--8:checked) {
  --svgb-05-rx: 8px;
  --svgb-05-peri: 915;
  --svgb-05-g-8: 0;
  --svgb-05-hl-8: var(--svgb-05-hlbg);
  --svgb-05-hc-8: var(--svgb-05-hlfg);
  --svgb-05-sb-8: var(--color-svgb05-panel);
  --svgb-05-sc-8: var(--color-svgb05-fg);
  --svgb-05-ss-8: var(--svgb-05-segsh);
}

.svgb-05:has(.svgb-05__r--20:checked) {
  --svgb-05-rx: 20px;
  --svgb-05-peri: 894;
  --svgb-05-g-20: 0;
  --svgb-05-hl-20: var(--svgb-05-hlbg);
  --svgb-05-hc-20: var(--svgb-05-hlfg);
  --svgb-05-sb-20: var(--color-svgb05-panel);
  --svgb-05-sc-20: var(--color-svgb05-fg);
  --svgb-05-ss-20: var(--svgb-05-segsh);
}

.svgb-05:has(.svgb-05__r--52:checked) {
  --svgb-05-rx: 52px;
  --svgb-05-peri: 839;
  --svgb-05-g-52: 0;
  --svgb-05-hl-52: var(--svgb-05-hlbg);
  --svgb-05-hc-52: var(--svgb-05-hlfg);
  --svgb-05-sb-52: var(--color-svgb05-panel);
  --svgb-05-sc-52: var(--color-svgb05-fg);
  --svgb-05-ss-52: var(--svgb-05-segsh);
}

.svgb-05:has(#svgb-05-theme:checked) {
  --color-svgb05-bg: #0d0d11;
  --color-svgb05-bg: oklch(0.175 0.006 300);
  --color-svgb05-fg: #eeeef3;
  --color-svgb05-fg: oklch(0.955 0.004 300);
  --color-svgb05-muted: #8d8e9b;
  --color-svgb05-muted: oklch(0.675 0.012 300);
  --color-svgb05-panel: #16161d;
  --color-svgb05-panel: oklch(0.222 0.009 300);
  --color-svgb05-rest: rgba(238, 238, 243, 0.16);
  --color-svgb05-rest: oklch(0.955 0.004 300 / 0.16);
  --color-svgb05-stroke: #ff7ac0;
  --color-svgb05-stroke: oklch(0.79 0.17 355);
}

.svgb-05:has(#svgb-05-theme:checked) .svgb-05__panel {
  box-shadow: inset 0 1px 0 oklch(1 0 0 / 0.05), 0 30px 70px -46px oklch(0 0 0 / 0.85);
}
```
