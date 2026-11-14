---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-glassmorphism-frosted-toggle-backdrop-blur/"
title: "Tailwind Glassmorphism Frosted Toggle with backdrop-blur"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "A frosted-glass switch floating over a vivid scene: backdrop-blur-[14px] backdrop-saturate-150 on the pane, a denser frost puck for the thumb, and two…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Frosted Toggle with backdrop-blur
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-glassmorphism-frosted-toggle-backdrop-blur/

A frosted-glass switch floating over a vivid scene: backdrop-blur-[14px] backdrop-saturate-150 on the pane, a denser frost puck for the thumb, and two drifting gradient blobs behind it that visibly refract through both as it slides.
## HTML
```html
<section class="ttg-21 relative overflow-hidden w-full min-h-svh grid place-items-center px-5 py-14 bg-linear-135 from-ttg21-scenehi to-ttg21-scenelo font-ttg21-sans" aria-label="Glassmorphism frosted toggle">
  <span aria-hidden="true" class="absolute top-[6%] left-[14%] w-85 h-85 rounded-full blur-[60px] opacity-85 bg-radial from-ttg21-bloba to-transparent to-70% animate-ttg21-drift motion-reduce:animate-none"></span>
  <span aria-hidden="true" class="absolute bottom-[4%] right-[12%] w-85 h-85 rounded-full blur-[60px] opacity-85 bg-radial from-ttg21-blobb to-transparent to-70% animate-ttg21-drift [animation-delay:-4.5s] motion-reduce:animate-none"></span>
  <label for="ttg-21-sw" class="relative z-10 flex items-center gap-9 px-7 py-5 rounded-[20px] cursor-pointer bg-white/10 border border-white/30 backdrop-blur-[14px] backdrop-saturate-150 shadow-[inset_0_1px_0_oklch(1_0_0/0.35),0_24px_50px_-24px_oklch(0_0_0/0.7)]">
    <span class="flex flex-col gap-0.5">
      <b class="text-[16px] font-semibold text-white">Ambient blur</b>
      <small class="text-[12.5px] text-white/75">Frost the dock &amp; sidebar</small>
    </span>
    <input type="checkbox" id="ttg-21-sw" role="switch" checked class="appearance-none shrink-0 w-19 h-10 rounded-[22px] relative cursor-pointer bg-white/15 border border-white/35 backdrop-blur-[8px] shadow-[inset_0_1px_0_oklch(1_0_0/0.3)] transition-[background-color,border-color] duration-[350ms] checked:bg-ttg21-tint/25 checked:border-ttg21-tint/70 before:content-[''] before:absolute before:top-1 before:left-1 before:w-7.5 before:h-7.5 before:rounded-full before:bg-white/80 before:shadow-[0_3px_10px_oklch(0_0_0/0.35),inset_0_1px_0_#fff] before:transition-transform before:duration-[350ms] before:ease-[cubic-bezier(0.3,1,0.35,1.05)] checked:before:translate-x-9 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-3 motion-reduce:transition-none motion-reduce:before:transition-none">
  </label>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg21-scenehi: #1d1038;
  --color-ttg21-scenehi: oklch(0.24 0.08 300);
  --color-ttg21-scenelo: #0c2438;
  --color-ttg21-scenelo: oklch(0.27 0.06 235);
  --color-ttg21-bloba: #e05fd0;
  --color-ttg21-bloba: oklch(0.68 0.24 330);
  --color-ttg21-blobb: #56cbe8;
  --color-ttg21-blobb: oklch(0.75 0.16 200);
  --color-ttg21-tint: #7cf0b4;
  --color-ttg21-tint: oklch(0.86 0.16 160);
  --font-ttg21-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --animate-ttg21-drift: ttg21-drift 9s ease-in-out infinite alternate;
}

@keyframes ttg21-drift {
  from {
    transform: translate(0, 0);
  }

  to {
    transform: translate(46px, -30px);
  }
}

.ttg-21 {
  width: 100%;
  min-height: 100svh;
}

.ttg-21 input[type="checkbox"] {
  -webkit-appearance: none;
  -webkit-backdrop-filter: blur(8px);
}

.ttg-21 label {
  -webkit-backdrop-filter: blur(14px) saturate(1.5);
}
/* Without backdrop-filter the pane is fully transparent and the label becomes unreadable,
   so the fallback is a solid surface rather than a slightly different glass. */

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .ttg-21 label {
    background: oklch(0.25 0.05 290 / 0.88);
  }

  .ttg-21 input[type="checkbox"] {
    background: oklch(1 0 0 / 0.16);
  }
}
```
