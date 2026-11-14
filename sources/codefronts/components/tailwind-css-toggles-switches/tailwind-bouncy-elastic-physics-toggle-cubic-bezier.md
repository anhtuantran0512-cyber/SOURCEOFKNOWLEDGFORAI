---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-bouncy-elastic-physics-toggle-cubic-bezier/"
title: "Tailwind Bouncy Elastic Physics Toggle (Overshoot Cubic-Bezier)"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "Premium motion from one token: --ease-ttg05-spring in @theme mints an ease-ttg05-spring utility whose negative first control point winds the thumb backwards…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Bouncy Elastic Physics Toggle (Overshoot Cubic-Bezier)
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-bouncy-elastic-physics-toggle-cubic-bezier/

Premium motion from one token: --ease-ttg05-spring in @theme mints an ease-ttg05-spring utility whose negative first control point winds the thumb backwards before it shoots across and bounces off the far wall. One transition, no keyframes, no spring library.
## HTML
```html
<section class="ttg-05 w-full min-h-svh flex flex-col items-center justify-center gap-7 px-5 py-14 bg-ttg05-bg font-ttg05-sans" aria-label="Bouncy elastic physics toggle">
  <label for="ttg-05-sw" class="group flex items-center gap-9 px-7 py-5 rounded-3xl cursor-pointer bg-white border border-ttg05-edge shadow-[0_18px_40px_-28px_oklch(0.55_0.09_75/0.55)]">
    <span class="flex items-center gap-3">
      <span aria-hidden="true" class="w-2 h-2 rounded-full bg-ttg05-edge transition-transform duration-[550ms] ease-ttg05-spring group-has-checked:bg-ttg05-on group-has-checked:scale-150"></span>
      <span class="flex flex-col gap-0.5">
        <span class="text-[15.5px] font-semibold text-ttg05-ink">Confetti on publish</span>
        <span class="text-[12.5px] text-ttg05-mute">Because shipping should feel like something</span>
      </span>
    </span>
    <input type="checkbox" id="ttg-05-sw" role="switch" class="appearance-none shrink-0 w-[76px] h-10 rounded-full bg-ttg05-off relative cursor-pointer transition-colors duration-[450ms] before:content-[''] before:absolute before:top-1 before:left-1 before:w-8 before:h-8 before:rounded-full before:bg-white before:shadow-[0_3px_7px_oklch(0.45_0.06_75/0.3)] before:transition-transform before:duration-[550ms] before:ease-ttg05-spring checked:bg-ttg05-on checked:before:translate-x-9 active:before:scale-[0.92] checked:active:before:translate-x-9 checked:active:before:scale-[0.92] focus-visible:outline-3 focus-visible:outline-ttg05-on focus-visible:outline-offset-4 motion-reduce:before:duration-200 motion-reduce:before:ease-out">
  </label>
  <p class="font-ttg05-mono text-[11.5px] text-ttg05-mute">cubic-bezier(0.4, &minus;0.3, 0.6, 1.3)</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg05-bg: #fdf8ef;
  --color-ttg05-bg: oklch(0.98 0.015 85);
  --color-ttg05-edge: #ece0ca;
  --color-ttg05-edge: oklch(0.91 0.025 85);
  --color-ttg05-off: #e6dcc8;
  --color-ttg05-off: oklch(0.89 0.03 85);
  --color-ttg05-on: #2f9e63;
  --color-ttg05-on: oklch(0.63 0.16 155);
  --color-ttg05-ink: #453c2d;
  --color-ttg05-ink: oklch(0.38 0.025 80);
  --color-ttg05-mute: #8d8269;
  --color-ttg05-mute: oklch(0.6 0.03 85);
  --font-ttg05-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttg05-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --ease-ttg05-spring: cubic-bezier(0.4, -0.3, 0.6, 1.3);
}

.ttg-05 {
  width: 100%;
  min-height: 100svh;
}

.ttg-05 input[type="checkbox"] {
  -webkit-appearance: none;
}
```
