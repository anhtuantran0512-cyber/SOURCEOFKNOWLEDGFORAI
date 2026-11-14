---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-stroke-dashoffset-button-outline-animation/"
title: "Tailwind Stroke Dashoffset Button Outline Animation"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "Three pads, three jobs for one number &mdash; ported so the difference between them is readable in the class lists."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stroke Dashoffset Button Outline Animation
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-stroke-dashoffset-button-outline-animation/

Three pads, three jobs for one number &mdash; ported so the difference between them is readable in the class lists. Both loops are declared once as --animate-* theme entries, so the markup only says animate-svgb02-orbit; hovering flips [animation-play-state:paused] to running rather than restarting the animation; and the twenty waveform bars share a single class list because h-(--h) reads each bar's own inline variable.
## HTML
```html
<section class="svgb-02 relative block w-full min-h-svh bg-svgb02-bg text-svgb02-fg font-svgb02-sans">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-02-theme">
  <label class="absolute z-[5] top-4 right-4 grid place-items-center size-11 rounded-full border border-current/20 bg-current/5 cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/15 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-02-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="min-h-svh grid place-items-center p-[clamp(20px,5vw,64px)]">
    <div class="w-full max-w-160 flex flex-col gap-[clamp(18px,3vw,28px)] p-[clamp(22px,4vw,36px)] rounded-md bg-linear-to-b from-svgb02-rack to-[color-mix(in_oklab,var(--color-svgb02-rack)_80%,#000)] shadow-[inset_0_1px_0_oklch(1_0_0/0.07),0_40px_80px_-50px_#000]">
      <div class="flex justify-between items-baseline">
        <span class="text-[13px] tracking-[0.14em] uppercase text-svgb02-muted">Take 07</span>
        <span class="font-svgb02-mono text-[clamp(20px,3.4vw,30px)] tracking-[-0.01em] tabular-nums text-svgb02-line">00:02:41:18</span>
      </div>
      <div class="flex items-end gap-1 h-21" aria-hidden="true">
        <span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:22%"></span><span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:54%"></span><span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:38%"></span><span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:76%"></span>
        <span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:92%"></span><span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:61%"></span><span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:44%"></span><span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:83%"></span>
        <span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:35%"></span><span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:67%"></span><span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:96%"></span><span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:52%"></span>
        <span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:29%"></span><span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:71%"></span><span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:48%"></span><span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:88%"></span>
        <span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:33%"></span><span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:59%"></span><span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:41%"></span><span class="flex-1 h-(--h) rounded-[1px] bg-svgb02-fg/20" style="--h:24%"></span>
      </div>
      <div class="h-1.5">
        <svg class="w-full h-1.5 overflow-visible" viewBox="0 0 560 6" preserveAspectRatio="none" aria-hidden="true">
          <line class="stroke-svgb02-fg/15 [stroke-width:2]" x1="1" y1="3" x2="559" y2="3" vector-effect="non-scaling-stroke"/>
          <line class="stroke-svgb02-line [stroke-width:2] [stroke-linecap:round] [stroke-dasharray:26_534] [stroke-dashoffset:var(--svgb-02-phase)] animate-svgb02-run motion-reduce:animate-none" x1="1" y1="3" x2="559" y2="3" vector-effect="non-scaling-stroke"/>
        </svg>
      </div>
      <div class="flex flex-wrap justify-between gap-[clamp(18px,4vw,40px)] pt-1.5">
        <div class="flex flex-col items-center gap-3">
          <button class="group relative grid place-items-center size-30 p-0 border-0 rounded-full bg-[radial-gradient(circle_at_50%_30%,color-mix(in_oklab,var(--color-svgb02-fg)_7%,transparent),transparent_70%)] cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb02-line focus-visible:outline-offset-4" type="button" aria-label="Play take">
            <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 120 120" aria-hidden="true">
              <circle class="fill-none stroke-svgb02-fg/15 [stroke-width:1.5]" cx="60" cy="60" r="57"/>
              <circle class="fill-none stroke-svgb02-line [stroke-width:2.4] [stroke-linecap:round] [stroke-dasharray:360] [stroke-dashoffset:360] transition-[stroke-dashoffset] duration-[760ms] ease-[cubic-bezier(0.16,1,0.3,1)] group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dashoffset:0]" cx="60" cy="60" r="57"/>
            </svg>
            <svg class="relative z-[1] size-[30px] transition-[fill,stroke] duration-300 stroke-none fill-svgb02-fg group-hover:fill-svgb02-line group-focus-visible:fill-svgb02-line" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6.5 18 12l-9 5.5Z"/></svg>
          </button>
          <span class="font-svgb02-mono text-[10.5px] leading-[1.55] text-center text-svgb02-muted">dasharray 360<br>offset &rarr; 0</span>
        </div>
        <div class="flex flex-col items-center gap-3">
          <button class="group relative grid place-items-center size-30 p-0 border-0 rounded-full bg-[radial-gradient(circle_at_50%_30%,color-mix(in_oklab,var(--color-svgb02-fg)_7%,transparent),transparent_70%)] cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb02-line focus-visible:outline-offset-4" type="button" aria-label="Arm recording">
            <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 120 120" aria-hidden="true">
              <circle class="fill-none stroke-svgb02-fg/15 [stroke-width:1.5]" cx="60" cy="60" r="57"/>
              <circle class="fill-none stroke-svgb02-line [stroke-width:2.4] [stroke-linecap:round] [stroke-dasharray:40_320] [stroke-dashoffset:var(--svgb-02-phase)] animate-svgb02-orbit [animation-play-state:paused] group-hover:[animation-play-state:running] group-focus-visible:[animation-play-state:running] motion-reduce:animate-none" cx="60" cy="60" r="57"/>
            </svg>
            <svg class="relative z-[1] size-[30px] transition-[fill,stroke] duration-300 fill-none stroke-svgb02-fg [stroke-width:1.6] [stroke-linecap:round] [stroke-linejoin:round] group-hover:stroke-svgb02-line group-focus-visible:stroke-svgb02-line" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="5.5"/></svg>
          </button>
          <span class="font-svgb02-mono text-[10.5px] leading-[1.55] text-center text-svgb02-muted">dasharray 40 320<br>offset &rarr; -360</span>
        </div>
        <div class="flex flex-col items-center gap-3">
          <button class="group relative grid place-items-center size-30 p-0 border-0 rounded-full bg-[radial-gradient(circle_at_50%_30%,color-mix(in_oklab,var(--color-svgb02-fg)_7%,transparent),transparent_70%)] cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb02-line focus-visible:outline-offset-4" type="button" aria-label="Loop region">
            <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 120 120" aria-hidden="true">
              <circle class="fill-none stroke-svgb02-fg/15 [stroke-width:1.5]" cx="60" cy="60" r="57"/>
              <circle class="fill-none stroke-svgb02-line [stroke-width:2.4] [stroke-linecap:round] [stroke-dasharray:180_180] [stroke-dashoffset:var(--svgb-02-phase)] animate-svgb02-orbit [animation-play-state:paused] group-hover:[animation-play-state:running] group-focus-visible:[animation-play-state:running] motion-reduce:animate-none" cx="60" cy="60" r="57"/>
            </svg>
            <svg class="relative z-[1] size-[30px] transition-[fill,stroke] duration-300 fill-none stroke-svgb02-fg [stroke-width:1.6] [stroke-linecap:round] [stroke-linejoin:round] group-hover:stroke-svgb02-line group-focus-visible:stroke-svgb02-line" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 9.5A5 5 0 0 1 10 5h8m0 0-3-3m3 3-3 3M19 14.5A5 5 0 0 1 14 19H6m0 0 3 3m-3-3 3-3"/></svg>
          </button>
          <span class="font-svgb02-mono text-[10.5px] leading-[1.55] text-center text-svgb02-muted">dasharray 180 180<br>offset &rarr; -360</span>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb02-bg: #0a0a0b;
  --color-svgb02-bg: oklch(0.15 0.002 60);
  --color-svgb02-fg: #f2efe9;
  --color-svgb02-fg: oklch(0.955 0.008 80);
  --color-svgb02-muted: #8e8981;
  --color-svgb02-muted: oklch(0.665 0.012 80);
  --color-svgb02-rack: #131211;
  --color-svgb02-rack: oklch(0.20 0.004 70);
  --color-svgb02-line: #ffb020;
  --color-svgb02-line: oklch(0.81 0.16 76);
  --font-svgb02-sans: 'Sora', system-ui, sans-serif;
  --font-svgb02-mono: 'IBM Plex Mono', ui-monospace, monospace;
  /* Named animations become animate-* utilities. The offset moves by exactly
       one pattern repeat, so the loop wraps with no visible jump. */
  --animate-svgb02-run: svgb02-run 2.6s linear infinite;
  --animate-svgb02-orbit: svgb02-orbit 2.4s linear infinite;
}

@property --svgb-02-phase {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}

@keyframes svgb02-run {
  to {
    --svgb-02-phase: -560;
  }
}

@keyframes svgb02-orbit {
  to {
    --svgb-02-phase: -360;
  }
}
/* Engines without @property cannot interpolate the registered number, so the
   fallback animates the presentation attribute directly. */

@keyframes svgb02-run-fb {
  to {
    stroke-dashoffset: -560;
  }
}

@keyframes svgb02-orbit-fb {
  to {
    stroke-dashoffset: -360;
  }
}

@supports not (background: paint(x)) {
  .animate-svgb02-run {
    animation-name: svgb02-run-fb;
  }

  .animate-svgb02-orbit {
    animation-name: svgb02-orbit-fb;
  }
}

.svgb-02:has(#svgb-02-theme:checked) {
  --color-svgb02-bg: #edeae4;
  --color-svgb02-bg: oklch(0.94 0.008 85);
  --color-svgb02-fg: #14130f;
  --color-svgb02-fg: oklch(0.19 0.006 80);
  --color-svgb02-muted: #6a655d;
  --color-svgb02-muted: oklch(0.535 0.012 80);
  --color-svgb02-rack: #fbfaf7;
  --color-svgb02-rack: oklch(0.985 0.004 85);
  --color-svgb02-line: #8a4b00;
  --color-svgb02-line: oklch(0.50 0.13 62);
}
```
