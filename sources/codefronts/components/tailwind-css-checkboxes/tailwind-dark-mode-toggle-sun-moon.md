---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/tailwind-dark-mode-toggle-sun-moon/"
title: "Tailwind Dark Mode Toggle Switch — Sun & Moon, No JavaScript"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "A day/night switch that actually changes the theme around it: has-checked: on the stage and group-has-checked/stage: on the card recolour the whole demo,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Toggle Switch — Sun & Moon, No JavaScript
Source: https://codefronts.com/components/tailwind-css-checkboxes/tailwind-dark-mode-toggle-sun-moon/

A day/night switch that actually changes the theme around it: has-checked: on the stage and group-has-checked/stage: on the card recolour the whole demo, while the thumb morphs from a glowing sun into a cratered moon over a star field. Zero JavaScript.
## HTML
```html
<section class="tcb-22 group/stage w-full min-h-svh grid place-items-center bg-tcb22-day px-5 py-14 font-tcb22-sans transition-colors duration-500 has-checked:bg-tcb22-night selection:bg-tcb22-sun selection:text-tcb22-ink motion-reduce:transition-none" aria-label="Dark mode toggle">
  <label class="group flex cursor-pointer items-center gap-6 rounded-2xl border border-tcb22-line bg-white px-6.5 py-5 shadow-tcb22-card transition-colors duration-500 group-has-checked/stage:border-white/10 group-has-checked/stage:bg-tcb22-card motion-reduce:transition-none">
    <span class="grid">
      <span class="text-base font-semibold text-tcb22-ink transition-colors group-has-checked/stage:text-white">Dark mode</span>
      <span class="text-[13px] text-tcb22-mut transition-colors group-has-checked/stage:text-tcb22-mutnight">Easier on the eyes at night</span>
    </span>
    <input type="checkbox" class="peer sr-only" checked>
    <span aria-hidden="true" class="relative h-9 w-[76px] flex-none overflow-hidden rounded-full bg-linear-to-b from-tcb22-sky1 to-tcb22-sky2 peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb22-ring">
      <span class="absolute inset-0 bg-linear-to-b from-tcb22-sky3 to-tcb22-sky4 opacity-0 transition-opacity duration-500 group-has-checked:opacity-100"></span>
      <span class="absolute inset-0 bg-[radial-gradient(1.5px_1.5px_at_18px_12px,#fff_99%,transparent),radial-gradient(1.5px_1.5px_at_30px_24px,#fff_99%,transparent),radial-gradient(1px_1px_at_24px_8px,#fff_99%,transparent),radial-gradient(1.5px_1.5px_at_40px_16px,#fff_99%,transparent),radial-gradient(1px_1px_at_12px_26px,#fff_99%,transparent)] opacity-0 transition-opacity duration-500 group-has-checked:opacity-100"></span>
      <span class="absolute left-1 top-1 size-7 rounded-full bg-tcb22-sun shadow-tcb22-sun transition-[translate,background-color,box-shadow] duration-500 ease-[cubic-bezier(.4,.8,.3,1)] group-has-checked:translate-x-10 group-has-checked:bg-tcb22-moon group-has-checked:shadow-tcb22-moon motion-reduce:transition-none"></span>
    </span>
  </label>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb22-day: #e9edf3;
  --color-tcb22-day: oklch(0.94 0.01 255);
  --color-tcb22-night: #0f1424;
  --color-tcb22-night: oklch(0.18 0.035 270);
  --color-tcb22-card: #1a2136;
  --color-tcb22-card: oklch(0.24 0.04 270);
  --color-tcb22-line: #e0e5ec;
  --color-tcb22-line: oklch(0.92 0.01 255);
  --color-tcb22-ink: #2a3140;
  --color-tcb22-ink: oklch(0.3 0.025 260);
  --color-tcb22-mut: #5b6474;
  --color-tcb22-mut: oklch(0.49 0.025 260);
  --color-tcb22-mutnight: #a3adc4;
  --color-tcb22-mutnight: oklch(0.75 0.03 265);
  --color-tcb22-sky1: #7ec8ff;
  --color-tcb22-sky1: oklch(0.8 0.11 240);
  --color-tcb22-sky2: #cdeeff;
  --color-tcb22-sky2: oklch(0.93 0.05 225);
  --color-tcb22-sky3: #1b2542;
  --color-tcb22-sky3: oklch(0.25 0.05 270);
  --color-tcb22-sky4: #2a3766;
  --color-tcb22-sky4: oklch(0.33 0.08 270);
  --color-tcb22-sun: #ffd76b;
  --color-tcb22-sun: oklch(0.89 0.14 88);
  --color-tcb22-moon: #e6ecf5;
  --color-tcb22-moon: oklch(0.94 0.012 255);
  --color-tcb22-ring: #4d7fff;
  --color-tcb22-ring: oklch(0.62 0.2 265);
  --font-tcb22-sans: 'Outfit', system-ui, sans-serif;
  --shadow-tcb22-card: 0 18px 40px -30px rgb(16 24 40 / 0.5);
  --shadow-tcb22-sun: 0 0 10px rgb(255 200 60 / 0.9);
  --shadow-tcb22-moon: inset -8px 2px 0 0 #b9c4d6;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-22 {
  width: 100%;
  min-height: 100svh;
}
```
