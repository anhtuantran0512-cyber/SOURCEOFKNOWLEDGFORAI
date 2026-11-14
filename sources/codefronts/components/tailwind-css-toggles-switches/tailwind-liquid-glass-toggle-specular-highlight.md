---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-liquid-glass-toggle-specular-highlight/"
title: "Tailwind Liquid Glass Toggle with Specular Highlight"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "Glass with a lens in it: the thumb brightens and saturates what sits behind it, carries a moving specular sweep across its crown, and drags a soft caustic…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Toggle with Specular Highlight
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-liquid-glass-toggle-specular-highlight/

Glass with a lens in it: the thumb brightens and saturates what sits behind it, carries a moving specular sweep across its crown, and drags a soft caustic shadow along the track. Demo 21 frosts a pane; this one bends light.
## HTML
```html
<section class="ttg-42 relative overflow-hidden w-full min-h-svh grid place-items-center px-5 py-14 bg-linear-140 from-ttg42-scenehi via-ttg42-scenemid to-ttg42-scenelo font-ttg42-sans" aria-label="Liquid glass toggle">
  <span aria-hidden="true" class="pointer-events-none absolute -top-16 left-[12%] w-96 h-96 rounded-full blur-[70px] opacity-80 bg-radial from-ttg42-bloba to-transparent to-70%"></span>
  <span aria-hidden="true" class="pointer-events-none absolute -bottom-20 right-[8%] w-96 h-96 rounded-full blur-[70px] opacity-80 bg-radial from-ttg42-blobb to-transparent to-70%"></span>
  <label for="ttg-42-sw" class="relative z-10 flex items-center gap-9 px-7 py-5 rounded-[24px] cursor-pointer bg-white/10 border border-white/25 backdrop-blur-xl shadow-[inset_0_1px_0_oklch(1_0_0/0.4),0_28px_56px_-28px_oklch(0_0_0/0.75)]">
    <span class="flex flex-col gap-0.5">
      <b class="text-[15.5px] font-semibold text-white">Lens blur</b>
      <small class="text-[12.5px] text-white/75">Refract the wallpaper behind panels</small>
    </span>
    <span class="relative shrink-0 w-[84px] h-11 rounded-full bg-white/12 border border-white/25 shadow-[inset_0_2px_6px_oklch(0_0_0/0.25)] transition-colors duration-[400ms] has-checked:bg-ttg42-tint/25">
      <span aria-hidden="true" class="ttg42-caustic pointer-events-none absolute top-2 left-2 w-8 h-8 rounded-full blur-lg bg-ttg42-caustic transition-transform duration-[400ms] ease-[cubic-bezier(0.3,1,0.35,1.05)] motion-reduce:transition-none"></span>
      <input type="checkbox" id="ttg-42-sw" role="switch" checked class="peer appearance-none absolute inset-0 w-full h-full rounded-full bg-transparent cursor-pointer z-20 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4">
      <span aria-hidden="true" class="ttg42-lens pointer-events-none absolute top-1 left-1 z-10 grid place-items-center w-9 h-9 rounded-full overflow-hidden bg-white/25 backdrop-blur-md backdrop-brightness-125 backdrop-saturate-150 shadow-[inset_0_1px_0_oklch(1_0_0/0.65),inset_0_-2px_6px_oklch(0_0_0/0.25),0_4px_12px_-2px_oklch(0_0_0/0.45)] transition-transform duration-[400ms] ease-[cubic-bezier(0.3,1,0.35,1.05)] motion-reduce:transition-none">
        <i class="absolute -top-2 -left-1 w-10 h-4 rotate-[-18deg] rounded-full bg-linear-to-b from-white/60 to-transparent"></i>
      </span>
    </span>
  </label>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg42-scenehi: #241344;
  --color-ttg42-scenehi: oklch(0.27 0.11 300);
  --color-ttg42-scenemid: #172a52;
  --color-ttg42-scenemid: oklch(0.31 0.09 268);
  --color-ttg42-scenelo: #0d3140;
  --color-ttg42-scenelo: oklch(0.33 0.06 215);
  --color-ttg42-bloba: #f05fc0;
  --color-ttg42-bloba: oklch(0.7 0.22 340);
  --color-ttg42-blobb: #4fd6e8;
  --color-ttg42-blobb: oklch(0.8 0.13 200);
  --color-ttg42-tint: #7cf0b4;
  --color-ttg42-tint: oklch(0.86 0.16 160);
  --color-ttg42-caustic: #ffe9a8;
  --color-ttg42-caustic: oklch(0.92 0.1 90 / 0.5);
  --font-ttg42-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-42 {
  width: 100%;
  min-height: 100svh;
}

.ttg-42 input[type="checkbox"] {
  -webkit-appearance: none;
}

.ttg-42 label {
  -webkit-backdrop-filter: blur(24px);
}

.ttg-42 .ttg42-lens {
  -webkit-backdrop-filter: blur(6px) brightness(1.25) saturate(1.5);
}

.ttg-42 .peer:checked ~ .ttg42-lens {
  transform: translateX(40px);
}

.ttg-42 span:has(.peer:checked) .ttg42-caustic {
  transform: translateX(40px);
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .ttg-42 label {
    background: oklch(0.26 0.06 290 / 0.9);
  }

  .ttg-42 .ttg42-lens {
    background: oklch(1 0 0 / 0.85);
  }
}
```
