---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-morphing-sun-to-moon-icon-toggle/"
title: "Tailwind Morphing Sun-to-Moon Icon Toggle (SVG Stroke)"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "One SVG becomes two icons: the sun's rays retract into their own centres via stroke-dashoffset while a mask circle slides in to bite a crescent out of the disc."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Morphing Sun-to-Moon Icon Toggle (SVG Stroke)
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-morphing-sun-to-moon-icon-toggle/

One SVG becomes two icons: the sun's rays retract into their own centres via stroke-dashoffset while a mask circle slides in to bite a crescent out of the disc. No icon swap, no second file &mdash; the same eight paths morph.
## HTML
```html
<section class="ttg-46 w-full min-h-svh grid place-items-center px-5 py-14 bg-ttg46-bg font-ttg46-sans transition-colors duration-500 has-checked:bg-ttg46-nightbg motion-reduce:transition-none" aria-label="Sun to moon icon toggle">
  <div class="flex flex-col items-center gap-6">
    <input type="checkbox" id="ttg-46-sw" role="switch" aria-label="Dark theme" class="peer sr-only">
    <label for="ttg-46-sw" class="grid place-items-center w-24 h-24 rounded-full cursor-pointer bg-ttg46-btn border border-ttg46-edge transition-colors duration-500 peer-checked:bg-ttg46-btnnight peer-checked:border-ttg46-edgenight peer-focus-visible:outline-3 peer-focus-visible:outline-ttg46-focus peer-focus-visible:outline-offset-4 peer-checked:[&_.ttg46-icon]:-rotate-[25deg] peer-checked:[&_.ttg46-ray]:[stroke-dashoffset:9px] peer-checked:[&_.ttg46-bite]:translate-x-0 peer-checked:[&_.ttg46-disc]:fill-ttg46-moon">
      <svg viewBox="0 0 48 48" class="ttg46-icon w-12 h-12 transition-transform duration-500 ease-[cubic-bezier(0.3,1,0.35,1.05)] motion-reduce:duration-75" aria-hidden="true">
        <defs>
          <mask id="ttg46-crescent">
            <rect x="0" y="0" width="48" height="48" fill="white"/>
            <circle class="ttg46-bite transition-transform duration-500 ease-[cubic-bezier(0.3,1,0.35,1.05)] translate-x-[26px] motion-reduce:duration-75" cx="30" cy="18" r="13" fill="black"/>
          </mask>
        </defs>
        <circle class="ttg46-disc fill-ttg46-sun transition-[fill] duration-500" cx="24" cy="24" r="10" mask="url(#ttg46-crescent)"/>
        <g class="ttg46-rays" stroke="currentColor" stroke-width="3" stroke-linecap="round" fill="none">
          <line class="ttg46-ray stroke-ttg46-sun [stroke-dasharray:9px] [stroke-dashoffset:0px] transition-[stroke-dashoffset,stroke] duration-300 [transition-delay:0ms]" x1="24" y1="3" x2="24" y2="10"/>
          <line class="ttg46-ray stroke-ttg46-sun [stroke-dasharray:9px] [stroke-dashoffset:0px] transition-[stroke-dashoffset,stroke] duration-300 [transition-delay:40ms]" x1="38.8" y1="9.2" x2="34" y2="14"/>
          <line class="ttg46-ray stroke-ttg46-sun [stroke-dasharray:9px] [stroke-dashoffset:0px] transition-[stroke-dashoffset,stroke] duration-300 [transition-delay:80ms]" x1="45" y1="24" x2="38" y2="24"/>
          <line class="ttg46-ray stroke-ttg46-sun [stroke-dasharray:9px] [stroke-dashoffset:0px] transition-[stroke-dashoffset,stroke] duration-300 [transition-delay:120ms]" x1="38.8" y1="38.8" x2="34" y2="34"/>
          <line class="ttg46-ray stroke-ttg46-sun [stroke-dasharray:9px] [stroke-dashoffset:0px] transition-[stroke-dashoffset,stroke] duration-300 [transition-delay:160ms]" x1="24" y1="45" x2="24" y2="38"/>
          <line class="ttg46-ray stroke-ttg46-sun [stroke-dasharray:9px] [stroke-dashoffset:0px] transition-[stroke-dashoffset,stroke] duration-300 [transition-delay:200ms]" x1="9.2" y1="38.8" x2="14" y2="34"/>
          <line class="ttg46-ray stroke-ttg46-sun [stroke-dasharray:9px] [stroke-dashoffset:0px] transition-[stroke-dashoffset,stroke] duration-300 [transition-delay:240ms]" x1="3" y1="24" x2="10" y2="24"/>
          <line class="ttg46-ray stroke-ttg46-sun [stroke-dasharray:9px] [stroke-dashoffset:0px] transition-[stroke-dashoffset,stroke] duration-300 [transition-delay:280ms]" x1="9.2" y1="9.2" x2="14" y2="14"/>
        </g>
      </svg>
    </label>
    <span class="flex flex-col items-center gap-1 text-center">
      <b class="text-[15.5px] font-semibold text-ttg46-ink transition-colors duration-500 peer-checked:text-ttg46-inknight">Dark theme</b>
      <span class="text-[12.5px] text-ttg46-mute transition-colors duration-500">One icon, morphed &mdash; not two icons swapped</span>
    </span>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg46-bg: #f3f4f7;
  --color-ttg46-bg: oklch(0.96 0.005 265);
  --color-ttg46-nightbg: #0d1120;
  --color-ttg46-nightbg: oklch(0.18 0.03 270);
  --color-ttg46-btn: #ffffff;
  --color-ttg46-btn: oklch(1 0 0);
  --color-ttg46-btnnight: #191f33;
  --color-ttg46-btnnight: oklch(0.24 0.03 270);
  --color-ttg46-edge: #e5e7ee;
  --color-ttg46-edge: oklch(0.92 0.006 265);
  --color-ttg46-edgenight: #2a3350;
  --color-ttg46-edgenight: oklch(0.32 0.04 270);
  --color-ttg46-sun: #e8a317;
  --color-ttg46-sun: oklch(0.75 0.16 78);
  --color-ttg46-moon: #e6ecff;
  --color-ttg46-moon: oklch(0.93 0.03 270);
  --color-ttg46-ink: #222838;
  --color-ttg46-ink: oklch(0.27 0.018 265);
  --color-ttg46-inknight: #dfe4f2;
  --color-ttg46-inknight: oklch(0.91 0.015 270);
  --color-ttg46-mute: #7d8494;
  --color-ttg46-mute: oklch(0.6 0.018 265);
  --font-ttg46-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-46 {
  width: 100%;
  min-height: 100svh;
}
```
