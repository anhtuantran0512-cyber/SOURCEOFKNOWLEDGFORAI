---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-animated-radio-button-concentric-ripple/"
title: "Tailwind Animated Radio Button (Concentric Ripple)"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "A radio with physicality: on check two concentric rings burst outward from the dot like a droplet hitting water — the input's own after: ring, chased 120ms…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Radio Button (Concentric Ripple)
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-animated-radio-button-concentric-ripple/

A radio with physicality: on check two concentric rings burst outward from the dot like a droplet hitting water — the input's own after: ring, chased 120ms later by a sibling ring driven with peer-checked:. Both are one-shot animate-* tokens, so re-checking replays the splash for free.
## HTML
```html
<section class="trb-07 w-full min-h-svh grid place-items-center bg-trb07-bg px-6 py-14 font-trb07-sans text-trb07-ink" aria-label="Concentric ripple radio buttons demo">
  <fieldset class="w-full max-w-[22rem] rounded-2xl bg-white/80 p-5 shadow-trb07-card ring-1 ring-trb07-line">
    <legend class="sr-only">Meeting length</legend>
    <p aria-hidden="true" class="px-2 text-xl font-bold tracking-[-0.02em]">Meeting length</p>
    <div class="mt-2 grid">
      <label class="group flex min-h-[3.25rem] cursor-pointer items-center gap-3.5 rounded-xl px-2 transition-colors hover:bg-trb07-bg has-checked:bg-trb07-acc/6"><span class="relative size-6 flex-none"><input type="radio" name="trb-07" value="15" class="peer relative z-2 grid size-6 cursor-pointer appearance-none place-items-center rounded-full border-2 border-trb07-ring bg-white transition-colors before:size-3 before:scale-0 before:rounded-full before:bg-trb07-acc before:transition-transform before:duration-300 before:ease-trb07-spring before:content-[''] after:pointer-events-none after:absolute after:-inset-0.5 after:rounded-full after:border-2 after:border-trb07-acc after:opacity-0 after:content-[''] checked:border-trb07-acc checked:before:scale-100 checked:after:animate-trb07-burst focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-trb07-acc motion-reduce:checked:after:animate-none forced-colors:appearance-auto"><span aria-hidden="true" class="pointer-events-none absolute inset-0 z-1 rounded-full border-2 border-trb07-acc/70 opacity-0 peer-checked:animate-trb07-burst-late motion-reduce:peer-checked:animate-none"></span></span><span class="text-[15.5px] group-has-checked:font-semibold">15 minutes</span><span class="ml-auto text-[13px] text-trb07-mut">Quick sync</span></label>
      <label class="group flex min-h-[3.25rem] cursor-pointer items-center gap-3.5 rounded-xl px-2 transition-colors hover:bg-trb07-bg has-checked:bg-trb07-acc/6"><span class="relative size-6 flex-none"><input type="radio" name="trb-07" value="30" checked class="peer relative z-2 grid size-6 cursor-pointer appearance-none place-items-center rounded-full border-2 border-trb07-ring bg-white transition-colors before:size-3 before:scale-0 before:rounded-full before:bg-trb07-acc before:transition-transform before:duration-300 before:ease-trb07-spring before:content-[''] after:pointer-events-none after:absolute after:-inset-0.5 after:rounded-full after:border-2 after:border-trb07-acc after:opacity-0 after:content-[''] checked:border-trb07-acc checked:before:scale-100 checked:after:animate-trb07-burst focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-trb07-acc motion-reduce:checked:after:animate-none forced-colors:appearance-auto"><span aria-hidden="true" class="pointer-events-none absolute inset-0 z-1 rounded-full border-2 border-trb07-acc/70 opacity-0 peer-checked:animate-trb07-burst-late motion-reduce:peer-checked:animate-none"></span></span><span class="text-[15.5px] group-has-checked:font-semibold">30 minutes</span><span class="ml-auto text-[13px] text-trb07-mut">Most booked</span></label>
      <label class="group flex min-h-[3.25rem] cursor-pointer items-center gap-3.5 rounded-xl px-2 transition-colors hover:bg-trb07-bg has-checked:bg-trb07-acc/6"><span class="relative size-6 flex-none"><input type="radio" name="trb-07" value="60" class="peer relative z-2 grid size-6 cursor-pointer appearance-none place-items-center rounded-full border-2 border-trb07-ring bg-white transition-colors before:size-3 before:scale-0 before:rounded-full before:bg-trb07-acc before:transition-transform before:duration-300 before:ease-trb07-spring before:content-[''] after:pointer-events-none after:absolute after:-inset-0.5 after:rounded-full after:border-2 after:border-trb07-acc after:opacity-0 after:content-[''] checked:border-trb07-acc checked:before:scale-100 checked:after:animate-trb07-burst focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-trb07-acc motion-reduce:checked:after:animate-none forced-colors:appearance-auto"><span aria-hidden="true" class="pointer-events-none absolute inset-0 z-1 rounded-full border-2 border-trb07-acc/70 opacity-0 peer-checked:animate-trb07-burst-late motion-reduce:peer-checked:animate-none"></span></span><span class="text-[15.5px] group-has-checked:font-semibold">1 hour</span><span class="ml-auto text-[13px] text-trb07-mut">Deep dive</span></label>
    </div>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb07-bg: #eef5f9;
  --color-trb07-bg: oklch(0.965 0.01 225);
  --color-trb07-ink: #1d2530;
  --color-trb07-ink: oklch(0.25 0.02 250);
  --color-trb07-mut: #5b6776;
  --color-trb07-mut: oklch(0.51 0.025 250);
  --color-trb07-line: #dde7ee;
  --color-trb07-line: oklch(0.925 0.012 230);
  --color-trb07-ring: #98a7b7;
  --color-trb07-ring: oklch(0.72 0.03 245);
  --color-trb07-acc: #1690c4;
  --color-trb07-acc: oklch(0.6 0.14 230);
  --shadow-trb07-card: 0 14px 40px -20px oklch(0.3 0.05 240 / 0.3);
  --ease-trb07-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --font-trb07-sans: 'Geist', system-ui, sans-serif;
  --animate-trb07-burst: trb07-burst 0.7s cubic-bezier(0.22, 1, 0.36, 1);
  --animate-trb07-burst-late: trb07-burst 0.8s cubic-bezier(0.22, 1, 0.36, 1) 0.12s;

  @keyframes trb07-burst {
    0% {
      transform: scale(0.4);
      opacity: 0.9;
    }

    100% {
      transform: scale(2.6);
      opacity: 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-07 {
  width: 100%;
  min-height: 100svh;
}
```
