---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/retro-pixel-art-checkbox-tailwind/"
title: "Retro Pixel Art Checkbox in Tailwind CSS — 8-Bit Arcade Menu"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "An arcade menu where every tick is drawn in pixels: one 3px square plus a shadow-tcb19-tick token that stamps six more."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro Pixel Art Checkbox in Tailwind CSS — 8-Bit Arcade Menu
Source: https://codefronts.com/components/tailwind-css-checkboxes/retro-pixel-art-checkbox-tailwind/

An arcade menu where every tick is drawn in pixels: one 3px square plus a shadow-tcb19-tick token that stamps six more. Now with the real game-menu touch — a blinking ▶ cursor that appears beside the row you're on (hover or keyboard focus), in Press Start 2P.
## HTML
```html
<section class="tcb-19 w-full min-h-svh grid place-items-center bg-tcb19-bg px-5 py-14 font-tcb19-pixel text-tcb19-ink selection:bg-tcb19-c selection:text-tcb19-bg" aria-label="Retro pixel checkboxes">
  <div class="w-full max-w-[25rem] border-2 border-tcb19-line bg-tcb19-panel p-3 shadow-tcb19-panel">
    <p class="px-2 pb-3 pt-1 text-[10px] tracking-[0.1em] text-tcb19-c">— PLAYER 1 —</p>
    <label class="group flex min-h-13 cursor-pointer items-center gap-3 px-1"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="w-3 text-[10px] text-tcb19-c opacity-0 group-hover:animate-tcb19-blink group-hover:opacity-100 group-has-focus-visible:animate-tcb19-blink group-has-focus-visible:opacity-100 motion-reduce:animate-none">▶</span><span aria-hidden="true" class="relative size-7 flex-none border-2 border-tcb19-box bg-tcb19-well shadow-tcb19-bevel transition-colors duration-100 ease-[steps(2)] peer-checked:border-tcb19-c peer-checked:bg-tcb19-on peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb19-c"><span class="absolute left-[5px] top-[13px] size-[3px] bg-tcb19-c opacity-0 shadow-tcb19-tick transition-opacity duration-100 ease-[steps(2)] group-has-checked:opacity-100"></span></span><span class="text-[11px] leading-5 tracking-[0.06em] group-has-checked:text-tcb19-c">INSERT COIN</span></label>
    <label class="group flex min-h-13 cursor-pointer items-center gap-3 px-1"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="w-3 text-[10px] text-tcb19-c opacity-0 group-hover:animate-tcb19-blink group-hover:opacity-100 group-has-focus-visible:animate-tcb19-blink group-has-focus-visible:opacity-100 motion-reduce:animate-none">▶</span><span aria-hidden="true" class="relative size-7 flex-none border-2 border-tcb19-box bg-tcb19-well shadow-tcb19-bevel transition-colors duration-100 ease-[steps(2)] peer-checked:border-tcb19-c peer-checked:bg-tcb19-on peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb19-c"><span class="absolute left-[5px] top-[13px] size-[3px] bg-tcb19-c opacity-0 shadow-tcb19-tick transition-opacity duration-100 ease-[steps(2)] group-has-checked:opacity-100"></span></span><span class="text-[11px] leading-5 tracking-[0.06em] group-has-checked:text-tcb19-c">CONTINUE?</span></label>
    <label class="group flex min-h-13 cursor-pointer items-center gap-3 px-1"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="w-3 text-[10px] text-tcb19-c opacity-0 group-hover:animate-tcb19-blink group-hover:opacity-100 group-has-focus-visible:animate-tcb19-blink group-has-focus-visible:opacity-100 motion-reduce:animate-none">▶</span><span aria-hidden="true" class="relative size-7 flex-none border-2 border-tcb19-box bg-tcb19-well shadow-tcb19-bevel transition-colors duration-100 ease-[steps(2)] peer-checked:border-tcb19-c peer-checked:bg-tcb19-on peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb19-c"><span class="absolute left-[5px] top-[13px] size-[3px] bg-tcb19-c opacity-0 shadow-tcb19-tick transition-opacity duration-100 ease-[steps(2)] group-has-checked:opacity-100"></span></span><span class="text-[11px] leading-5 tracking-[0.06em] group-has-checked:text-tcb19-c">EXTRA LIFE</span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb19-bg: #12131f;
  --color-tcb19-bg: oklch(0.18 0.025 280);
  --color-tcb19-panel: #1b1d2e;
  --color-tcb19-panel: oklch(0.22 0.03 280);
  --color-tcb19-well: #0e0f18;
  --color-tcb19-well: oklch(0.15 0.02 280);
  --color-tcb19-on: #2a2f45;
  --color-tcb19-on: oklch(0.3 0.04 275);
  --color-tcb19-line: #2f3350;
  --color-tcb19-line: oklch(0.32 0.05 278);
  --color-tcb19-box: #5a6099;
  --color-tcb19-box: oklch(0.5 0.09 278);
  --color-tcb19-ink: #c8ccec;
  --color-tcb19-ink: oklch(0.86 0.04 280);
  --color-tcb19-c: #39ff6a;
  --color-tcb19-c: oklch(0.88 0.24 145);
  --font-tcb19-pixel: 'Press Start 2P', ui-monospace, monospace;
  --shadow-tcb19-panel: 6px 6px 0 #07080e;
  --shadow-tcb19-bevel: inset -2px -2px 0 #07080e;
  --shadow-tcb19-tick: 3px 3px 0 #39ff6a, 6px 6px 0 #39ff6a, 9px 3px 0 #39ff6a, 12px 0 0 #39ff6a, 15px -3px 0 #39ff6a, 18px -6px 0 #39ff6a;
  --animate-tcb19-blink: tcb19-blink 0.8s steps(1) infinite;

  @keyframes tcb19-blink {
    0%,
        100% {
      opacity: 1;
    }

    50% {
      opacity: 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-19 {
  width: 100%;
  min-height: 100svh;
}
```
