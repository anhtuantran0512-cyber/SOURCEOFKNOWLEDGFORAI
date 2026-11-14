---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/aurora-gradient-toggle-switch-tailwind/"
title: "Aurora Gradient Toggle Switch in Tailwind CSS — Premium Dark UI"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "A premium dark-UI switch whose track fills with a drifting aurora mesh — three radial gradients over a deep base, animated by animate-tcb29-drift."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Aurora Gradient Toggle Switch in Tailwind CSS — Premium Dark UI
Source: https://codefronts.com/components/tailwind-css-checkboxes/aurora-gradient-toggle-switch-tailwind/

A premium dark-UI switch whose track fills with a drifting aurora mesh — three radial gradients over a deep base, animated by animate-tcb29-drift. The mesh is the collection's one @utility, because a four-layer background repeated in three class lists is worse than a named utility. The thumb now glows when on. Near-zero CSS.
## HTML
```html
<section class="tcb-29 relative isolate w-full min-h-svh grid place-items-center overflow-hidden bg-tcb29-bg px-5 py-14 font-tcb29-sans text-tcb29-ink selection:bg-tcb29-mint selection:text-tcb29-bg" aria-label="Aurora toggle switches">
  <span aria-hidden="true" class="absolute left-1/2 top-1/2 -z-10 h-64 w-[26rem] -translate-1/2 rounded-full bg-linear-90 from-tcb29-blue/25 via-tcb29-mint/20 to-tcb29-violet/25 blur-3xl"></span>
  <div class="flex w-full max-w-[25rem] flex-col divide-y divide-white/[0.06] rounded-2xl border border-tcb29-line bg-tcb29-panel/90 px-4.5 py-2">
    <label class="group flex min-h-16 cursor-pointer items-center justify-between gap-4 px-1"><span class="text-[15px] font-medium transition-colors group-has-checked:text-white">Aurora theme</span>
      <input type="checkbox" class="peer sr-only" checked>
      <span aria-hidden="true" class="relative h-8 w-16 flex-none overflow-hidden rounded-full bg-tcb29-off transition-colors duration-400 peer-checked:bg-tcb29-on peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb29-mint">
        <span class="tcb29-mesh absolute inset-0 opacity-0 transition-opacity duration-500 group-has-checked:animate-tcb29-drift group-has-checked:opacity-100 motion-reduce:animate-none"></span>
        <span class="absolute left-[3px] top-[3px] z-10 size-[26px] rounded-full bg-tcb29-thumb shadow-tcb29-thumb transition-[translate,box-shadow] duration-400 ease-[cubic-bezier(.4,.8,.3,1)] group-has-checked:translate-x-8 group-has-checked:shadow-tcb29-glow motion-reduce:transition-none"></span>
      </span>
    </label>
    <label class="group flex min-h-16 cursor-pointer items-center justify-between gap-4 px-1"><span class="text-[15px] font-medium transition-colors group-has-checked:text-white">Cinematic mode</span>
      <input type="checkbox" class="peer sr-only">
      <span aria-hidden="true" class="relative h-8 w-16 flex-none overflow-hidden rounded-full bg-tcb29-off transition-colors duration-400 peer-checked:bg-tcb29-on peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb29-mint">
        <span class="tcb29-mesh absolute inset-0 opacity-0 transition-opacity duration-500 group-has-checked:animate-tcb29-drift group-has-checked:opacity-100 motion-reduce:animate-none"></span>
        <span class="absolute left-[3px] top-[3px] z-10 size-[26px] rounded-full bg-tcb29-thumb shadow-tcb29-thumb transition-[translate,box-shadow] duration-400 ease-[cubic-bezier(.4,.8,.3,1)] group-has-checked:translate-x-8 group-has-checked:shadow-tcb29-glow motion-reduce:transition-none"></span>
      </span>
    </label>
    <label class="group flex min-h-16 cursor-pointer items-center justify-between gap-4 px-1"><span class="text-[15px] font-medium transition-colors group-has-checked:text-white">Ambient glow</span>
      <input type="checkbox" class="peer sr-only" checked>
      <span aria-hidden="true" class="relative h-8 w-16 flex-none overflow-hidden rounded-full bg-tcb29-off transition-colors duration-400 peer-checked:bg-tcb29-on peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb29-mint">
        <span class="tcb29-mesh absolute inset-0 opacity-0 transition-opacity duration-500 group-has-checked:animate-tcb29-drift group-has-checked:opacity-100 motion-reduce:animate-none"></span>
        <span class="absolute left-[3px] top-[3px] z-10 size-[26px] rounded-full bg-tcb29-thumb shadow-tcb29-thumb transition-[translate,box-shadow] duration-400 ease-[cubic-bezier(.4,.8,.3,1)] group-has-checked:translate-x-8 group-has-checked:shadow-tcb29-glow motion-reduce:transition-none"></span>
      </span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb29-bg: #0c1018;
  --color-tcb29-bg: oklch(0.16 0.015 260);
  --color-tcb29-panel: #141a26;
  --color-tcb29-panel: oklch(0.21 0.02 260);
  --color-tcb29-line: #232b3d;
  --color-tcb29-line: oklch(0.28 0.03 265);
  --color-tcb29-ink: #c3cad9;
  --color-tcb29-ink: oklch(0.84 0.02 265);
  --color-tcb29-off: #2a3244;
  --color-tcb29-off: oklch(0.31 0.03 265);
  --color-tcb29-on: #0a1526;
  --color-tcb29-on: oklch(0.18 0.03 255);
  --color-tcb29-thumb: #eef3ff;
  --color-tcb29-thumb: oklch(0.96 0.015 265);
  --color-tcb29-blue: #4d7fff;
  --color-tcb29-blue: oklch(0.62 0.2 265);
  --color-tcb29-mint: #5effd0;
  --color-tcb29-mint: oklch(0.9 0.15 170);
  --color-tcb29-violet: #c04cff;
  --color-tcb29-violet: oklch(0.64 0.26 310);
  --font-tcb29-sans: 'Sora', system-ui, sans-serif;
  --shadow-tcb29-thumb: 0 2px 6px rgb(0 0 0 / 0.5);
  --shadow-tcb29-glow: 0 0 0 1px rgb(94 255 208 / 0.4), 0 0 14px rgb(94 255 208 / 0.55);
  --animate-tcb29-drift: tcb29-drift 8s ease-in-out infinite;

  @keyframes tcb29-drift {
    0%,
        100% {
      background-position: 0% 50%, 100% 50%, 50% 0%, 0 0;
    }

    50% {
      background-position: 100% 50%, 0% 50%, 50% 100%, 0 0;
    }
  }
}
/* The one custom utility: a four-layer mesh is clearer named than repeated as an arbitrary value. */

@utility tcb29-mesh {
  background: radial-gradient(60% 120% at 15% 40%, #4d7fff 0%, transparent 60%), radial-gradient(60% 120% at 50% 60%, #5effd0 0%, transparent 55%), radial-gradient(70% 130% at 85% 35%, #c04cff 0%, transparent 60%), linear-gradient(90deg, #0b1f3a, #0a2b33);
  background-size: 220% 220%, 220% 220%, 220% 220%, 100% 100%;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-29 {
  width: 100%;
  min-height: 100svh;
}
```
