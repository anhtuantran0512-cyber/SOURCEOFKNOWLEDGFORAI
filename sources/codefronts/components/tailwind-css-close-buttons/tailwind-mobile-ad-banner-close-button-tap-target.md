---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/tailwind-mobile-ad-banner-close-button-tap-target/"
title: "Tailwind Mobile Ad Banner Close Button (48px Tap Target)"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "The IAB rule in one component: a 20px visual dot inflated to a 48×48 tap target with p-3.5 and pulled back into the corner with -mt-3.5 -me-3.5. The…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mobile Ad Banner Close Button (48px Tap Target)
Source: https://codefronts.com/components/tailwind-css-close-buttons/tailwind-mobile-ad-banner-close-button-tap-target/

The IAB rule in one component: a 20px visual dot inflated to a 48×48 tap target with p-3.5 and pulled back into the corner with -mt-3.5 -me-3.5. The original's "set --debug:0" instruction became a real toggle: a checkbox the stage reads with group-has-[:checked]/stage:, so the dashed hit-area overlay switches on and off with zero JavaScript.
## HTML
```html
<section class="tcb-06 group/stage w-full min-h-svh grid place-items-center bg-tcb06-bg px-6 py-12 font-tcb06-sans text-tcb06-ink" aria-label="Mobile ad banner close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="flex w-full max-w-[22.5rem] flex-col items-center gap-5">
      <div class="relative h-16 w-full rounded-xl bg-linear-100 from-tcb06-a to-tcb06-b shadow-[0_14px_30px_-16px_var(--color-tcb06-shadow)]">
        <div class="flex h-full flex-col justify-center gap-1 px-4 text-white">
          <span class="text-[15px] leading-none font-extrabold tracking-[0.06em]">SUMMER SALE</span>
          <span class="text-xs">Up to 60% off — today only</span>
        </div>
        <span class="absolute end-2 bottom-1.5 rounded-sm bg-black/35 px-1 text-[9px] font-semibold tracking-wide text-white">AD</span>
        <button type="button" aria-label="Close ad" class="group absolute top-0 end-0 -mt-3.5 -me-3.5 cursor-pointer rounded-[14px] p-3.5 outline-offset-[-2px] group-has-[#tcb-06-debug:checked]/stage:outline-[1.5px] group-has-[#tcb-06-debug:checked]/stage:outline-dashed group-has-[#tcb-06-debug:checked]/stage:outline-tcb06-acc focus-visible:outline-3 focus-visible:outline-solid focus-visible:outline-offset-0 focus-visible:outline-tcb06-acc">
          <span aria-hidden="true" class="relative block size-5 rounded-full bg-[rgb(20_16_14/0.72)] ring-1 ring-white/50 transition duration-150 before:absolute before:top-1/2 before:left-1/2 before:h-[1.5px] before:w-2.5 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-white after:absolute after:top-1/2 after:left-1/2 after:h-[1.5px] after:w-2.5 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-white group-hover:scale-110 group-active:scale-90 motion-reduce:transition-none"></span>
        </button>
      </div>
      <label class="flex min-h-11 cursor-pointer items-center gap-3 rounded-full bg-white px-4 text-[13px] font-medium shadow-sm ring-1 ring-black/8 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tcb06-acc">
        <input id="tcb-06-debug" type="checkbox" checked class="peer sr-only">
        <span aria-hidden="true" class="relative h-5 w-9 rounded-full bg-tcb06-ink/25 transition-colors after:absolute after:top-0.5 after:left-0.5 after:size-4 after:rounded-full after:bg-white after:shadow after:transition-transform peer-checked:bg-tcb06-acc peer-checked:after:translate-x-4 motion-reduce:transition-none motion-reduce:after:transition-none"></span>
        Show the 48×48 tap target
      </label>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/70 px-3.5 py-2 font-tcb06-mono text-[11.5px] text-tcb06-mut ring-1 ring-black/8">p-3.5 -mt-3.5 -me-3.5 · group-has-[:checked]/stage:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb06-bg: #f1ede6;
  --color-tcb06-bg: oklch(0.94 0.01 80);
  --color-tcb06-ink: #34291f;
  --color-tcb06-ink: oklch(0.3 0.03 60);
  --color-tcb06-mut: #6b5d4f;
  --color-tcb06-mut: oklch(0.49 0.03 60);
  --color-tcb06-a: #e2622c;
  --color-tcb06-a: oklch(0.64 0.19 40);
  --color-tcb06-b: #c9303a;
  --color-tcb06-b: oklch(0.55 0.2 20);
  --color-tcb06-acc: #b33a1c;
  --color-tcb06-acc: oklch(0.52 0.17 35);
  --color-tcb06-shadow: #8e3a1f99;
  --color-tcb06-shadow: oklch(0.45 0.15 30 / 0.6);
  --font-tcb06-sans: 'Geist', system-ui, sans-serif;
  --font-tcb06-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-06 {
  width: 100%;
  min-height: 100svh;
}
```
