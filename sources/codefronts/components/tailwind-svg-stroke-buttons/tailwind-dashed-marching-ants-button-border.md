---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-dashed-marching-ants-button-border/"
title: "Tailwind Dashed Marching Ants Button Border"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "Marching ants where they belong &mdash; a crop selection over a photograph &mdash; with the march declared once as --animate-svgb06-march so the marquee and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dashed Marching Ants Button Border
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-dashed-marching-ants-button-border/

Marching ants where they belong &mdash; a crop selection over a photograph &mdash; with the march declared once as --animate-svgb06-march so the marquee and the Apply button cannot drift apart. The only difference between a selection that marches forever and a button that marches on hover is two utilities: [animation-play-state:paused] group-hover:[animation-play-state:running].
## HTML
```html
<section class="svgb-06 relative block w-full min-h-svh bg-svgb06-bg text-svgb06-fg font-svgb06-sans">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-06-theme">
  <label class="absolute z-[5] top-3.5 right-3.5 grid place-items-center size-11 rounded-full border border-current/20 bg-current/12 backdrop-blur-lg cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/20 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-06-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="min-h-svh grid grid-cols-[64px_1fr] grid-rows-[1fr_auto] gap-px bg-svgb06-fg/8">
    <div class="row-span-2 flex flex-col items-center gap-2 py-3.5 bg-svgb06-chrome">
      <button class="size-11 grid place-items-center border-0 rounded-[10px] bg-transparent text-svgb06-muted cursor-pointer transition-[background-color,color] duration-150 motion-reduce:transition-none hover:bg-svgb06-fg/8 hover:text-svgb06-fg focus-visible:outline-2 focus-visible:outline-svgb06-stroke focus-visible:-outline-offset-2 [&_svg]:size-5 !bg-svgb06-stroke/16 !text-svgb06-stroke" type="button" aria-label="Crop">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M6 2v14a2 2 0 0 0 2 2h14M2 6h14a2 2 0 0 1 2 2v14"/></svg>
      </button>
      <button class="size-11 grid place-items-center border-0 rounded-[10px] bg-transparent text-svgb06-muted cursor-pointer transition-[background-color,color] duration-150 motion-reduce:transition-none hover:bg-svgb06-fg/8 hover:text-svgb06-fg focus-visible:outline-2 focus-visible:outline-svgb06-stroke focus-visible:-outline-offset-2 [&_svg]:size-5" type="button" aria-label="Straighten">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M3 17 17 3m-6 0h6v6"/></svg>
      </button>
      <button class="size-11 grid place-items-center border-0 rounded-[10px] bg-transparent text-svgb06-muted cursor-pointer transition-[background-color,color] duration-150 motion-reduce:transition-none hover:bg-svgb06-fg/8 hover:text-svgb06-fg focus-visible:outline-2 focus-visible:outline-svgb06-stroke focus-visible:-outline-offset-2 [&_svg]:size-5" type="button" aria-label="Levels">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M4 19V9m5 10V5m5 14v-7m5 7V8"/></svg>
      </button>
      <button class="size-11 grid place-items-center border-0 rounded-[10px] bg-transparent text-svgb06-muted cursor-pointer transition-[background-color,color] duration-150 motion-reduce:transition-none hover:bg-svgb06-fg/8 hover:text-svgb06-fg focus-visible:outline-2 focus-visible:outline-svgb06-stroke focus-visible:-outline-offset-2 [&_svg]:size-5" type="button" aria-label="Mask">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="10" cy="12" r="7"/><circle cx="15" cy="12" r="7"/></svg>
      </button>
    </div>

    <div class="relative grid place-items-center overflow-hidden p-[clamp(20px,4vw,54px)] [background:repeating-conic-gradient(oklch(0.24_0_0)_0%_25%,oklch(0.21_0_0)_0%_50%)_0_0/22px_22px]">
      <img class="absolute inset-0 w-full h-full object-cover saturate-[0.8] [opacity:var(--svgb-06-img-op,0.5)]" src="https://picsum.photos/seed/svgb06ridge/1400/950" alt="Mountain ridge at dusk" width="1400" height="950" loading="lazy" decoding="async">
      <div class="relative w-[min(400px,76vw)] aspect-[400/260] [box-shadow:0_0_0_9999px_var(--svgb-06-scrim,oklch(0_0_0/0.55))]">
        <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 400 260" preserveAspectRatio="none" aria-hidden="true">
          <rect class="fill-none stroke-svgb06-antb [stroke-width:1.6] [stroke-dasharray:10_8]" x="1" y="1" width="398" height="258" vector-effect="non-scaling-stroke"/>
          <rect class="fill-none stroke-svgb06-ant [stroke-width:1.6] [stroke-dasharray:10_8] [stroke-dashoffset:-9] animate-svgb06-march motion-reduce:animate-none motion-reduce:[stroke-dashoffset:0]" x="1" y="1" width="398" height="258" vector-effect="non-scaling-stroke"/>
        </svg>
        <span class="svgb-06__thirds absolute inset-0 pointer-events-none" aria-hidden="true"></span>
        <span class="absolute size-[13px] border-2 border-svgb06-ant [background:var(--svgb-06-hbg,oklch(0_0_0/0.4))] -top-[7px] -left-[7px]" aria-hidden="true"></span>
        <span class="absolute size-[13px] border-2 border-svgb06-ant [background:var(--svgb-06-hbg,oklch(0_0_0/0.4))] -top-[7px] -right-[7px]" aria-hidden="true"></span>
        <span class="absolute size-[13px] border-2 border-svgb06-ant [background:var(--svgb-06-hbg,oklch(0_0_0/0.4))] -bottom-[7px] -left-[7px]" aria-hidden="true"></span>
        <span class="absolute size-[13px] border-2 border-svgb06-ant [background:var(--svgb-06-hbg,oklch(0_0_0/0.4))] -bottom-[7px] -right-[7px]" aria-hidden="true"></span>
        <span class="absolute -bottom-[34px] left-0 font-svgb06-mono text-[11px] tabular-nums px-2 py-1 rounded-md bg-black/60 text-white">1620 &times; 1053</span>
      </div>
    </div>

    <div class="flex items-center justify-between gap-4 py-3.5 px-[clamp(14px,3vw,26px)] bg-svgb06-chrome">
      <span class="font-svgb06-mono text-xs text-svgb06-muted">3 : 2</span>
      <div class="flex gap-3">
        <button class="group relative h-[46px] grid place-items-center border-0 p-0 rounded-[10px] text-sm font-medium cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb06-stroke focus-visible:outline-offset-[3px] w-30 bg-svgb06-fg/6" type="button">
          <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 120 46" aria-hidden="true">
            <rect class="fill-none stroke-svgb06-rest [stroke-width:1.6] [stroke-dasharray:10_8] animate-svgb06-march [animation-play-state:paused] transition-[stroke] duration-200 group-hover:[animation-play-state:running] group-hover:stroke-svgb06-stroke group-focus-visible:[animation-play-state:running] group-focus-visible:stroke-svgb06-stroke motion-reduce:animate-none motion-reduce:group-hover:[stroke-dasharray:6_4]" x="1" y="1" width="118" height="44" rx="10" vector-effect="non-scaling-stroke"/>
          </svg>
          <span class="relative z-[1]">Reset</span>
        </button>
        <button class="group relative h-[46px] grid place-items-center border-0 p-0 rounded-[10px] text-sm font-medium cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb06-stroke focus-visible:outline-offset-[3px] w-42 bg-svgb06-stroke/14" type="button">
          <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 168 46" aria-hidden="true">
            <rect class="fill-none stroke-svgb06-rest [stroke-width:1.6] [stroke-dasharray:10_8] animate-svgb06-march [animation-play-state:paused] transition-[stroke] duration-200 group-hover:[animation-play-state:running] group-hover:stroke-svgb06-stroke group-focus-visible:[animation-play-state:running] group-focus-visible:stroke-svgb06-stroke motion-reduce:animate-none motion-reduce:group-hover:[stroke-dasharray:6_4]" x="1" y="1" width="166" height="44" rx="10" vector-effect="non-scaling-stroke"/>
          </svg>
          <span class="relative z-[1]">Apply crop</span>
        </button>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb06-bg: #121316;
  --color-svgb06-bg: oklch(0.19 0.005 260);
  --color-svgb06-chrome: #1b1d22;
  --color-svgb06-chrome: oklch(0.245 0.008 260);
  --color-svgb06-fg: #eceef1;
  --color-svgb06-fg: oklch(0.95 0.004 260);
  --color-svgb06-muted: #8b9099;
  --color-svgb06-muted: oklch(0.67 0.011 260);
  --color-svgb06-rest: rgba(236, 238, 241, 0.16);
  --color-svgb06-rest: oklch(0.95 0.004 260 / 0.16);
  --color-svgb06-stroke: #4ce0a0;
  --color-svgb06-stroke: oklch(0.85 0.16 160);
  /* the two-tone marquee: a light ant over a dark one, both scheme-aware */
  --color-svgb06-ant: #ffffff;
  --color-svgb06-antb: rgba(0, 0, 0, 0.75);
  --color-svgb06-antb: oklch(0 0 0 / 0.75);
  --font-svgb06-sans: 'DM Sans', system-ui, sans-serif;
  --font-svgb06-mono: 'JetBrains Mono', ui-monospace, monospace;
  /* 10 + 8 = one repeat of 18, which is exactly how far the offset travels */
  --animate-svgb06-march: svgb06-march 700ms linear infinite;
}

@keyframes svgb06-march {
  to {
    stroke-dashoffset: -18;
  }
}
/* Rule of thirds: four hairline gradients, decorative, one token */

.svgb-06__thirds {
  background: linear-gradient(90deg, transparent 33.2%, var(--svgb-06-third, oklch(1 0 0 / 0.3)) 33.2% 33.4%, transparent 33.4%), linear-gradient(90deg, transparent 66.5%, var(--svgb-06-third, oklch(1 0 0 / 0.3)) 66.5% 66.7%, transparent 66.7%), linear-gradient(transparent 33.2%, var(--svgb-06-third, oklch(1 0 0 / 0.3)) 33.2% 33.4%, transparent 33.4%), linear-gradient(transparent 66.5%, var(--svgb-06-third, oklch(1 0 0 / 0.3)) 66.5% 66.7%, transparent 66.7%);
}

.svgb-06:has(#svgb-06-theme:checked) {
  --color-svgb06-bg: #eceef0;
  --color-svgb06-bg: oklch(0.945 0.004 260);
  --color-svgb06-chrome: #ffffff;
  --color-svgb06-chrome: oklch(1 0 0);
  --color-svgb06-fg: #14171b;
  --color-svgb06-fg: oklch(0.20 0.006 260);
  --color-svgb06-muted: #5c626b;
  --color-svgb06-muted: oklch(0.505 0.011 260);
  --color-svgb06-rest: rgba(20, 23, 27, 0.18);
  --color-svgb06-rest: oklch(0.20 0.006 260 / 0.18);
  --color-svgb06-stroke: #0a7a52;
  --color-svgb06-stroke: oklch(0.50 0.13 162);
  --color-svgb06-ant: #0b0d10;
  --color-svgb06-antb: rgba(255, 255, 255, 0.85);
  --color-svgb06-antb: oklch(1 0 0 / 0.85);
  --svgb-06-img-op: 0.85;
  --svgb-06-scrim: oklch(1 0 0 / 0.55);
  --svgb-06-hbg: oklch(1 0 0 / 0.6);
  --svgb-06-third: oklch(0 0 0 / 0.28);
}
```
