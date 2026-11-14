---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-reduced-motion-fallback-for-stroke-buttons/"
title: "Tailwind Reduced Motion Fallback for Stroke Buttons"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "The best argument for utilities in the whole collection: Tailwind's motion-reduce: variant is @media (prefers-reduced-motion: reduce), so the fallback lives…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Reduced Motion Fallback for Stroke Buttons
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-reduced-motion-fallback-for-stroke-buttons/

The best argument for utilities in the whole collection: Tailwind's motion-reduce: variant is @media (prefers-reduced-motion: reduce), so the fallback lives in the markup next to the thing it replaces &mdash; you cannot ship the animation and forget the fallback in another file. And the fallback restates the end state rather than deleting the transition, because a bare transition-none leaves a button that never responds at all.
## HTML
```html
<section class="svgb-19 relative block w-full min-h-svh bg-svgb19-bg text-svgb19-fg font-svgb19-sans">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-19-theme">
  <label class="absolute z-[5] top-4 right-4 grid place-items-center size-11 rounded-full border border-current/20 bg-current/7 cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/14 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-19-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="min-h-svh grid place-items-center p-[clamp(16px,4vw,56px)]">
    <div class="w-full max-w-235 grid grid-cols-[minmax(0,200px)_1fr] rounded-[14px] overflow-hidden bg-svgb19-win border border-svgb19-rest shadow-[0_1px_2px_oklch(0_0_0/0.06),0_30px_70px_-50px_oklch(0_0_0/0.4)]">
      <div class="flex flex-col gap-0.5 p-2.5 bg-svgb19-side border-e border-svgb19-rest">
        <span class="px-2.5 pt-1.5 pb-3 text-xs font-semibold tracking-[0.1em] uppercase text-svgb19-muted">Accessibility</span>
        <span class="px-2.5 py-[9px] rounded-[7px] text-sm text-svgb19-muted">Display</span>
        <span class="px-2.5 py-[9px] rounded-[7px] text-sm bg-svgb19-stroke/12 text-svgb19-fg font-medium">Motion</span>
        <span class="px-2.5 py-[9px] rounded-[7px] text-sm text-svgb19-muted">Pointer</span>
        <span class="px-2.5 py-[9px] rounded-[7px] text-sm text-svgb19-muted">Captions</span>
        <span class="px-2.5 py-[9px] rounded-[7px] text-sm text-svgb19-muted">Audio</span>
      </div>
      <div class="flex flex-col gap-4 p-[clamp(20px,3.5vw,34px)]">
        <h1 class="m-0 text-[clamp(24px,3.4vw,32px)] font-semibold tracking-[-0.025em]">Motion</h1>
        <div class="border border-svgb19-rest rounded-xl">
          <input class="peer/sim absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-19-sim">
          <label class="flex items-center justify-between gap-5 px-[18px] py-4 cursor-pointer peer-focus-visible/sim:outline-2 peer-focus-visible/sim:outline-svgb19-stroke peer-focus-visible/sim:-outline-offset-2 peer-focus-visible/sim:rounded-xl peer-checked/sim:[&>span:last-child]:bg-svgb19-stroke peer-checked/sim:[&>span:last-child>span]:translate-x-5" for="svgb-19-sim">
            <span class="flex flex-col gap-[3px]">
              <span class="text-[15px] font-medium">Reduce motion</span>
              <span class="text-[13px] text-svgb19-muted">Replaces animated transitions with instant state changes.</span>
            </span>
            <span class="relative flex-none w-[50px] h-[30px] rounded-full bg-svgb19-fg/16 transition-[background-color] duration-200 motion-reduce:transition-none" aria-hidden="true"><span class="absolute top-[3px] left-[3px] size-6 rounded-full [background:var(--svgb-19-knob)] shadow-[0_1px_3px_oklch(0_0_0/0.3)] transition-[translate] duration-[220ms] ease-[cubic-bezier(0.22,1,0.36,1)] motion-reduce:transition-none"></span></span>
          </label>
        </div>

        <p class="mt-1.5 mb-0 font-svgb19-mono text-[10.5px] tracking-[0.16em] uppercase text-svgb19-muted">Preview</p>
        <div class="grid gap-[clamp(12px,2vw,18px)] grid-cols-[repeat(auto-fit,minmax(min(100%,236px),1fr))]">
          <div class="flex flex-col gap-[9px]">
            <button class="group relative w-full max-w-59 h-15 grid place-items-center border-0 p-0 rounded-xl bg-svgb19-fg/4 text-[14.5px] font-medium cursor-pointer overflow-hidden focus-visible:outline-2 focus-visible:outline-svgb19-stroke focus-visible:outline-offset-[3px]" type="button">
              <svg class="absolute inset-0 w-full h-full overflow-visible [&_rect]:fill-none [&_rect]:[stroke-linecap:round]" viewBox="0 0 236 60" aria-hidden="true">
                <rect class="stroke-svgb19-rest [stroke-width:1.4]" x="2" y="2" width="232" height="56" rx="12" pathLength="1"/>
                <rect class="svgb-19__ink stroke-svgb19-stroke [stroke-width:2.2] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[640ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" x="2" y="2" width="232" height="56" rx="12" pathLength="1"/>
              </svg>
              <span class="svgb-19__label relative z-[1] transition-[translate,color] duration-[320ms] ease-[cubic-bezier(0.22,1,0.36,1)]">Perimeter draw</span>
            </button>
            <span class="font-svgb19-mono text-[10.5px] text-svgb19-muted">travel &rarr; instant presence</span>
          </div>
          <div class="flex flex-col gap-[9px]">
            <button class="group relative w-full max-w-59 h-15 grid place-items-center border-0 p-0 rounded-xl bg-svgb19-fg/4 text-[14.5px] font-medium cursor-pointer overflow-hidden focus-visible:outline-2 focus-visible:outline-svgb19-stroke focus-visible:outline-offset-[3px]" type="button">
              <svg class="absolute inset-0 w-full h-full overflow-visible [&_rect]:fill-none [&_rect]:[stroke-linecap:round]" viewBox="0 0 236 60" aria-hidden="true">
                <rect class="stroke-svgb19-rest [stroke-width:1.4]" x="2" y="2" width="232" height="56" rx="12" pathLength="1"/>
                <rect class="svgb-19__ink--march stroke-svgb19-stroke [stroke-width:2.2] [stroke-dasharray:0.05_0.05] [stroke-dashoffset:0] opacity-0 transition-opacity duration-200 animate-svgb19-march [animation-play-state:paused] group-hover:opacity-100 group-hover:[animation-play-state:running] group-focus-visible:opacity-100 group-focus-visible:[animation-play-state:running] motion-reduce:animate-none" x="2" y="2" width="232" height="56" rx="12" pathLength="1"/>
              </svg>
              <span class="svgb-19__label relative z-[1] transition-[translate,color] duration-[320ms] ease-[cubic-bezier(0.22,1,0.36,1)]">Marching dash</span>
            </button>
            <span class="font-svgb19-mono text-[10.5px] text-svgb19-muted">loop &rarr; static dash</span>
          </div>
          <div class="flex flex-col gap-[9px]">
            <button class="group relative w-full max-w-59 h-15 grid place-items-center border-0 p-0 rounded-xl bg-svgb19-fg/4 text-[14.5px] font-medium cursor-pointer overflow-hidden focus-visible:outline-2 focus-visible:outline-svgb19-stroke focus-visible:outline-offset-[3px]" type="button">
              <svg class="absolute inset-0 w-full h-full overflow-visible [&_rect]:fill-none [&_rect]:[stroke-linecap:round]" viewBox="0 0 236 60" aria-hidden="true">
                <rect class="stroke-svgb19-rest [stroke-width:1.4]" x="2" y="2" width="232" height="56" rx="12" pathLength="1"/>
                <rect class="svgb-19__ink stroke-svgb19-stroke [stroke-width:2.2] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[640ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" x="2" y="2" width="232" height="56" rx="12" pathLength="1"/>
              </svg>
              <span class="svgb-19__label relative z-[1] transition-[translate,color] duration-[320ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:-translate-y-0.5 group-hover:text-svgb19-stroke group-focus-visible:-translate-y-0.5 group-focus-visible:text-svgb19-stroke motion-reduce:transition-[color] motion-reduce:group-hover:translate-y-0 motion-reduce:group-focus-visible:translate-y-0">Sliding label</span>
            </button>
            <span class="font-svgb19-mono text-[10.5px] text-svgb19-muted">slide &rarr; colour only</span>
          </div>
        </div>
        <p class="mt-1 mb-0 flex gap-[9px] items-baseline text-[12.5px] text-svgb19-muted"><span class="flex-none font-svgb19-mono text-[10px] px-[7px] py-[3px] rounded-[5px] bg-svgb19-stroke/12 text-[color-mix(in_oklab,var(--color-svgb19-stroke)_78%,var(--color-svgb19-fg))]">WCAG 2.3.3</span> Motion from interaction can be disabled, unless essential.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb19-bg: #e7e9ec;
  --color-svgb19-bg: oklch(0.935 0.005 250);
  --color-svgb19-fg: #12151a;
  --color-svgb19-fg: oklch(0.19 0.007 250);
  --color-svgb19-muted: #5b616b;
  --color-svgb19-muted: oklch(0.505 0.012 250);
  --color-svgb19-win: #ffffff;
  --color-svgb19-win: oklch(1 0 0);
  --color-svgb19-side: #f2f3f6;
  --color-svgb19-side: oklch(0.965 0.004 250);
  --color-svgb19-rest: rgba(18, 21, 26, 0.15);
  --color-svgb19-rest: oklch(0.19 0.007 250 / 0.15);
  --color-svgb19-stroke: #1a63d8;
  --color-svgb19-stroke: oklch(0.50 0.20 260);
  --font-svgb19-sans: 'Public Sans', system-ui, sans-serif;
  --font-svgb19-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-svgb19-march: svgb19-march 900ms linear infinite;
}

@keyframes svgb19-march {
  to {
    stroke-dashoffset: -0.1;
  }
}

.svgb-19 {
  --svgb-19-knob: #ffffff;
}
/* The real fallback is in the markup, as motion-reduce:* utilities — that
   variant IS this media query. What cannot be a variant is a *simulated*
   setting, so the switch re-applies the identical rules through :has(), which
   is what makes the fallback reviewable without changing OS preferences. */

.svgb-19:has(#svgb-19-sim:checked) .svgb-19__ink {
  transition: none;
  stroke-dasharray: none;
  stroke-dashoffset: 0;
  opacity: 0;
}

.svgb-19:has(#svgb-19-sim:checked) button:hover .svgb-19__ink,
.svgb-19:has(#svgb-19-sim:checked) button:focus-visible .svgb-19__ink {
  opacity: 1;
}

.svgb-19:has(#svgb-19-sim:checked) .svgb-19__ink--march {
  animation: none;
  stroke-dasharray: 0.05 0.05;
}

.svgb-19:has(#svgb-19-sim:checked) .svgb-19__label {
  transition: color 220ms ease;
}

.svgb-19:has(#svgb-19-sim:checked) button:hover .svgb-19__label,
.svgb-19:has(#svgb-19-sim:checked) button:focus-visible .svgb-19__label {
  translate: 0 0;
}

.svgb-19:has(#svgb-19-theme:checked) {
  --color-svgb19-bg: #0b0d11;
  --color-svgb19-bg: oklch(0.165 0.007 250);
  --color-svgb19-fg: #edeff3;
  --color-svgb19-fg: oklch(0.955 0.004 250);
  --color-svgb19-muted: #8c929c;
  --color-svgb19-muted: oklch(0.67 0.012 250);
  --color-svgb19-win: #15181e;
  --color-svgb19-win: oklch(0.22 0.009 250);
  --color-svgb19-side: #11141a;
  --color-svgb19-side: oklch(0.19 0.008 250);
  --color-svgb19-rest: rgba(237, 239, 243, 0.16);
  --color-svgb19-rest: oklch(0.955 0.004 250 / 0.16);
  --color-svgb19-stroke: #85b4ff;
  --color-svgb19-stroke: oklch(0.79 0.13 262);
  --svgb-19-knob: #0d1014;
}
```
