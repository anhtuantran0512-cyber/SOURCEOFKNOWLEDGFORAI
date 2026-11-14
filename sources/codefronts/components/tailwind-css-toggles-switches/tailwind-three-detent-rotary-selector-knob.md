---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-three-detent-rotary-selector-knob/"
title: "Tailwind Three-Detent Rotary Selector Knob"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "Demo 22's knob with somewhere to go: three radio-driven detents at &minus;50&deg;, 0&deg; and 50&deg;, tick marks that light as the pointer reaches them, and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Three-Detent Rotary Selector Knob
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-three-detent-rotary-selector-knob/

Demo 22's knob with somewhere to go: three radio-driven detents at &minus;50&deg;, 0&deg; and 50&deg;, tick marks that light as the pointer reaches them, and a mode readout under the dial. A knob with two positions is a switch; a knob with three is a knob.
## HTML
```html
<section class="ttg-43 w-full min-h-svh grid place-items-center px-5 py-14 bg-ttg43-bg font-ttg43-sans" aria-label="Three detent rotary selector">
  <div role="radiogroup" aria-label="Fan mode" class="relative flex flex-col items-center gap-5 px-10 py-8 rounded-[20px] bg-linear-170 from-ttg43-facehi to-ttg43-facelo shadow-[0_24px_50px_-24px_oklch(0_0_0/0.9),inset_0_1px_0_oklch(1_0_0/0.07)]">
    <input type="radio" name="ttg-43" id="ttg-43-eco" class="peer/eco sr-only">
    <input type="radio" name="ttg-43" id="ttg-43-normal" checked class="peer/normal sr-only">
    <input type="radio" name="ttg-43" id="ttg-43-boost" class="peer/boost sr-only">
    <span class="relative grid place-items-center w-32 h-32 rounded-full [background:radial-gradient(circle,var(--color-ttg43-wellhi)_56%,var(--color-ttg43-wellmid)_58%,var(--color-ttg43-welllo)_100%)] shadow-[inset_0_2px_6px_oklch(0_0_0/0.7)] peer-checked/eco:[&_.ttg43-t1]:bg-ttg43-lit peer-checked/normal:[&_.ttg43-t2]:bg-ttg43-lit peer-checked/boost:[&_.ttg43-t3]:bg-ttg43-lit peer-checked/eco:[&_.ttg43-knob]:rotate-[-50deg] peer-checked/normal:[&_.ttg43-knob]:rotate-0 peer-checked/boost:[&_.ttg43-knob]:rotate-[50deg]">
      <i aria-hidden="true" class="ttg43-t1 absolute top-6 left-6 w-0.5 h-3 rounded-full bg-ttg43-tick rotate-[-45deg] transition-colors duration-200"></i>
      <i aria-hidden="true" class="ttg43-t2 absolute top-2.5 left-1/2 -ml-px w-0.5 h-3 rounded-full bg-ttg43-tick transition-colors duration-200"></i>
      <i aria-hidden="true" class="ttg43-t3 absolute top-6 right-6 w-0.5 h-3 rounded-full bg-ttg43-tick rotate-[45deg] transition-colors duration-200"></i>
      <span aria-hidden="true" class="ttg43-knob relative w-24 h-24 rounded-full [background:radial-gradient(circle_at_32%_26%,oklch(1_0_0/0.32),transparent_46%),conic-gradient(var(--color-ttg43-mhi)_0_8%,var(--color-ttg43-mlo)_8%_16%,var(--color-ttg43-mmid)_16%_24%,var(--color-ttg43-mlo)_24%_32%,var(--color-ttg43-mhi)_32%_40%,var(--color-ttg43-mlo)_40%_48%,var(--color-ttg43-mmid)_48%_56%,var(--color-ttg43-mlo)_56%_64%,var(--color-ttg43-mhi)_64%_72%,var(--color-ttg43-mlo)_72%_80%,var(--color-ttg43-mmid)_80%_88%,var(--color-ttg43-mlo)_88%_96%,var(--color-ttg43-mhi)_96%_100%)] shadow-[0_6px_14px_oklch(0_0_0/0.6),inset_0_-3px_6px_oklch(0_0_0/0.35),inset_0_2px_3px_oklch(1_0_0/0.5)] transition-transform duration-[380ms] ease-[cubic-bezier(0.34,1.45,0.5,1)] before:content-[''] before:absolute before:top-2 before:left-1/2 before:-ml-[3px] before:w-1.5 before:h-6 before:rounded-full before:bg-ttg43-pointer before:shadow-[inset_0_1px_2px_oklch(0_0_0/0.8),0_1px_0_oklch(1_0_0/0.3)] motion-reduce:duration-100"></span>
    </span>
    <div class="flex gap-1.5">
      <label for="ttg-43-eco" class="flex items-center justify-center min-w-16 min-h-11 px-3 rounded-lg cursor-pointer text-[11px] font-bold tracking-[0.14em] text-ttg43-legend transition-colors duration-200 hover:text-ttg43-lit peer-checked/eco:bg-ttg43-chip peer-checked/eco:text-ttg43-lit peer-focus-visible/eco:outline-3 peer-focus-visible/eco:outline-ttg43-focus peer-focus-visible/eco:outline-offset-2">ECO</label>
      <label for="ttg-43-normal" class="flex items-center justify-center min-w-16 min-h-11 px-3 rounded-lg cursor-pointer text-[11px] font-bold tracking-[0.14em] text-ttg43-legend transition-colors duration-200 hover:text-ttg43-lit peer-checked/normal:bg-ttg43-chip peer-checked/normal:text-ttg43-lit peer-focus-visible/normal:outline-3 peer-focus-visible/normal:outline-ttg43-focus peer-focus-visible/normal:outline-offset-2">NORMAL</label>
      <label for="ttg-43-boost" class="flex items-center justify-center min-w-16 min-h-11 px-3 rounded-lg cursor-pointer text-[11px] font-bold tracking-[0.14em] text-ttg43-legend transition-colors duration-200 hover:text-ttg43-lit peer-checked/boost:bg-ttg43-chip peer-checked/boost:text-ttg43-lit peer-focus-visible/boost:outline-3 peer-focus-visible/boost:outline-ttg43-focus peer-focus-visible/boost:outline-offset-2">BOOST</label>
    </div>
    <span aria-hidden="true" class="relative block w-60 h-8">
      <i class="ttg43-r1 absolute inset-0 not-italic grid place-items-center text-center font-ttg43-mono text-[11px] leading-snug text-ttg43-mute opacity-0 transition-opacity duration-200">~18 dB &middot; slowest, coolest running</i>
      <i class="ttg43-r2 absolute inset-0 not-italic grid place-items-center text-center font-ttg43-mono text-[11px] leading-snug text-ttg43-mute opacity-0 transition-opacity duration-200">~26 dB &middot; balanced curve</i>
      <i class="ttg43-r3 absolute inset-0 not-italic grid place-items-center text-center font-ttg43-mono text-[11px] leading-snug text-ttg43-mute opacity-0 transition-opacity duration-200">~41 dB &middot; maximum airflow</i>
    </span>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg43-bg: #232529;
  --color-ttg43-bg: oklch(0.26 0.005 265);
  --color-ttg43-facehi: #34373d;
  --color-ttg43-facehi: oklch(0.34 0.007 265);
  --color-ttg43-facelo: #292b30;
  --color-ttg43-facelo: oklch(0.29 0.006 265);
  --color-ttg43-wellhi: #1d1f23;
  --color-ttg43-wellhi: oklch(0.23 0.005 265);
  --color-ttg43-wellmid: #3b3e45;
  --color-ttg43-wellmid: oklch(0.37 0.007 265);
  --color-ttg43-welllo: #22242a;
  --color-ttg43-welllo: oklch(0.25 0.006 265);
  --color-ttg43-mhi: #c2c7d1;
  --color-ttg43-mhi: oklch(0.83 0.01 265);
  --color-ttg43-mmid: #b3b8c2;
  --color-ttg43-mmid: oklch(0.78 0.01 265);
  --color-ttg43-mlo: #8d939e;
  --color-ttg43-mlo: oklch(0.65 0.012 265);
  --color-ttg43-pointer: #1e2027;
  --color-ttg43-pointer: oklch(0.23 0.008 265);
  --color-ttg43-tick: #5f6672;
  --color-ttg43-tick: oklch(0.5 0.012 265);
  --color-ttg43-lit: #7fd4ff;
  --color-ttg43-lit: oklch(0.84 0.12 235);
  --color-ttg43-chip: #2a3440;
  --color-ttg43-chip: oklch(0.3 0.02 240);
  --color-ttg43-legend: #a2a8b4;
  --color-ttg43-legend: oklch(0.73 0.012 265);
  --color-ttg43-mute: #8b919d;
  --color-ttg43-mute: oklch(0.66 0.012 265);
  --color-ttg43-focus: #6cb6f0;
  --color-ttg43-focus: oklch(0.74 0.14 235);
  --font-ttg43-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttg43-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
}

.ttg-43 {
  width: 100%;
  min-height: 100svh;
}
/* The readout lines are cousins of the radios, not descendants of anything stateful. */

.ttg-43:has(#ttg-43-eco:checked) .ttg43-r1,
.ttg-43:has(#ttg-43-normal:checked) .ttg43-r2,
.ttg-43:has(#ttg-43-boost:checked) .ttg43-r3 {
  opacity: 1;
}
```
