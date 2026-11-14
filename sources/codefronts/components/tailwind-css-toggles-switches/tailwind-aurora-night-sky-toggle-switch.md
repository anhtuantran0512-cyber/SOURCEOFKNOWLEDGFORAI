---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-aurora-night-sky-toggle-switch/"
title: "Tailwind Aurora Night Sky Toggle Switch"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "A dark-mode switch with weather: flip it and three blurred aurora ribbons drift across a deep sky at different speeds while the horizon cools."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Aurora Night Sky Toggle Switch
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-aurora-night-sky-toggle-switch/

A dark-mode switch with weather: flip it and three blurred aurora ribbons drift across a deep sky at different speeds while the horizon cools. Demo 18 moves objects; this one moves atmosphere, which is a different kind of quiet.
## HTML
```html
<section class="ttg-39 relative overflow-hidden w-full min-h-svh grid place-items-center px-5 py-14 bg-ttg39-daysky font-ttg39-sans transition-colors duration-[900ms] has-checked:bg-ttg39-nightsky motion-reduce:transition-none" aria-label="Aurora night sky toggle">
  <span aria-hidden="true" class="ttg39-aurora pointer-events-none absolute inset-x-0 top-0 h-2/3 opacity-0 transition-opacity duration-[900ms] -skew-y-[8deg] motion-reduce:transition-none">
    <i class="absolute left-[-30%] top-[18%] w-[160%] h-20 rounded-full blur-[42px] mix-blend-screen bg-linear-to-r from-transparent via-ttg39-aur1 to-transparent [animation:ttg39-drift_14s_ease-in-out_infinite_alternate] motion-reduce:[animation:none]"></i>
    <i class="absolute left-[-30%] top-[34%] w-[160%] h-16 rounded-full blur-[42px] mix-blend-screen bg-linear-to-r from-transparent via-ttg39-aur2 to-transparent [animation:ttg39-drift_19s_ease-in-out_infinite_alternate] motion-reduce:[animation:none]"></i>
    <i class="absolute left-[-30%] top-[50%] w-[160%] h-24 rounded-full blur-[42px] mix-blend-screen bg-linear-to-r from-transparent via-ttg39-aur3 to-transparent [animation:ttg39-drift_24s_ease-in-out_infinite_alternate] motion-reduce:[animation:none]"></i>
  </span>
  <span aria-hidden="true" class="ttg39-horizon pointer-events-none absolute inset-x-0 bottom-0 h-1/3 bg-linear-to-t from-ttg39-glow to-transparent transition-opacity duration-[900ms] motion-reduce:transition-none"></span>
  <label for="ttg-39-sw" class="relative z-10 flex items-center gap-8 px-7 py-5 rounded-[22px] cursor-pointer bg-white/8 border border-white/15 backdrop-blur-xl">
    <span class="flex flex-col gap-0.5">
      <b class="text-[15.5px] font-semibold text-white">Night sky</b>
      <span class="text-[12.5px] text-white/70">Dims the workspace and wakes the aurora</span>
    </span>
    <input type="checkbox" id="ttg-39-sw" role="switch" aria-label="Night sky" class="peer appearance-none shrink-0 w-[68px] h-9 rounded-full bg-white/20 relative cursor-pointer transition-colors duration-500 before:content-[''] before:absolute before:top-1 before:left-1 before:w-7 before:h-7 before:rounded-full before:bg-white before:shadow-[0_2px_8px_oklch(0_0_0/0.4)] before:transition-transform before:duration-500 before:ease-[cubic-bezier(0.3,1,0.35,1.05)] checked:bg-ttg39-aur1/60 checked:before:translate-x-8 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-3 motion-reduce:transition-none motion-reduce:before:transition-none">
  </label>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg39-daysky: #2b3550;
  --color-ttg39-daysky: oklch(0.36 0.05 265);
  --color-ttg39-nightsky: #070b18;
  --color-ttg39-nightsky: oklch(0.14 0.03 270);
  --color-ttg39-aur1: #4ef0b0;
  --color-ttg39-aur1: oklch(0.85 0.17 165);
  --color-ttg39-aur2: #58c8f0;
  --color-ttg39-aur2: oklch(0.8 0.13 215);
  --color-ttg39-aur3: #9b7cf0;
  --color-ttg39-aur3: oklch(0.7 0.16 290);
  --color-ttg39-glow: #3d4a6e;
  --color-ttg39-glow: oklch(0.42 0.06 265 / 0.7);
  --font-ttg39-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

@keyframes ttg39-drift {
  from {
    transform: translateX(-6%) scaleY(1);
  }

  to {
    transform: translateX(6%) scaleY(1.25);
  }
}

.ttg-39 {
  width: 100%;
  min-height: 100svh;
}

.ttg-39 input[type="checkbox"] {
  -webkit-appearance: none;
}

.ttg-39 label {
  -webkit-backdrop-filter: blur(24px);
}

.ttg-39:has(:checked) .ttg39-aurora {
  opacity: 1;
}

.ttg-39:has(:checked) .ttg39-horizon {
  opacity: 0;
}
```
