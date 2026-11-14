---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-brass-periscope-lens-button/"
title: "Tailwind Brass Periscope Lens Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A brass periscope objective: a knurled bezel, an engraved focus scale, and a six-blade iris that opens on hover to reveal the glass — each blade a clipped…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Brass Periscope Lens Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-brass-periscope-lens-button/

A brass periscope objective: a knurled bezel, an engraved focus scale, and a six-blade iris that opens on hover to reveal the glass — each blade a clipped triangle rotating about the optical centre, with a reflection sweep across the coated lens.
## HTML
```html
<div class="tb-51 w-full min-h-svh grid place-items-center font-tb51-sans p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" aria-label="Open the viewfinder" class="group cursor-pointer border-0 bg-transparent p-0 [-webkit-tap-highlight-color:transparent] focus-visible:outline-none disabled:cursor-not-allowed disabled:grayscale-[0.7] disabled:brightness-[0.85]">
    <span aria-hidden="true" class="tb-51__bezel relative grid place-items-center size-38 rounded-full shadow-[inset_0_2px_3px_#ffffff73,inset_0_-3px_7px_#0000008c,0_18px_28px_-12px_#000000d9] transition-[rotate,filter] duration-[550ms] ease-tb51-out group-hover:brightness-105 group-active:rotate-6 group-focus-visible:outline-2 group-focus-visible:outline-offset-[5px] group-focus-visible:outline-tb51-brass-hi motion-reduce:transition-none">
      <span class="absolute inset-0 rounded-full bg-[repeating-conic-gradient(from_0deg,#ffffff38_0_1.4deg,#00000047_1.4deg_3deg)] [mask-image:radial-gradient(farthest-side,transparent_86%,#000_88%)]"></span>
      <span class="tb-51__scale absolute inset-[9%] rounded-full opacity-75 bg-[repeating-conic-gradient(from_-90deg,var(--color-tb51-brass-lo)_0_1deg,transparent_1deg_15deg)] [mask-image:radial-gradient(farthest-side,transparent_82%,#000_84%)]"></span>
      <span class="tb-51__barrel relative grid place-items-center w-[66%] h-[66%] rounded-full overflow-hidden shadow-[inset_0_0_0_3px_var(--color-tb51-barrel-ring),inset_0_4px_10px_#000000e6]">
        <span class="tb-51__glass absolute inset-0 rounded-full z-10"></span>
        <span class="absolute inset-0 z-20 rounded-full">
          <span style="--i:0" class="tb-51__blade absolute inset-0 [clip-path:polygon(50%_50%,100%_6%,100%_94%)] shadow-[inset_0_0_0_1px_#00000080] transition-[rotate,scale,opacity] duration-[550ms] ease-tb51-out group-hover:scale-50 group-focus-visible:scale-50 motion-reduce:transition-none"></span>
          <span style="--i:1" class="tb-51__blade absolute inset-0 [clip-path:polygon(50%_50%,100%_6%,100%_94%)] shadow-[inset_0_0_0_1px_#00000080] transition-[rotate,scale,opacity] duration-[550ms] ease-tb51-out group-hover:scale-50 group-focus-visible:scale-50 motion-reduce:transition-none"></span>
          <span style="--i:2" class="tb-51__blade absolute inset-0 [clip-path:polygon(50%_50%,100%_6%,100%_94%)] shadow-[inset_0_0_0_1px_#00000080] transition-[rotate,scale,opacity] duration-[550ms] ease-tb51-out group-hover:scale-50 group-focus-visible:scale-50 motion-reduce:transition-none"></span>
          <span style="--i:3" class="tb-51__blade absolute inset-0 [clip-path:polygon(50%_50%,100%_6%,100%_94%)] shadow-[inset_0_0_0_1px_#00000080] transition-[rotate,scale,opacity] duration-[550ms] ease-tb51-out group-hover:scale-50 group-focus-visible:scale-50 motion-reduce:transition-none"></span>
          <span style="--i:4" class="tb-51__blade absolute inset-0 [clip-path:polygon(50%_50%,100%_6%,100%_94%)] shadow-[inset_0_0_0_1px_#00000080] transition-[rotate,scale,opacity] duration-[550ms] ease-tb51-out group-hover:scale-50 group-focus-visible:scale-50 motion-reduce:transition-none"></span>
          <span style="--i:5" class="tb-51__blade absolute inset-0 [clip-path:polygon(50%_50%,100%_6%,100%_94%)] shadow-[inset_0_0_0_1px_#00000080] transition-[rotate,scale,opacity] duration-[550ms] ease-tb51-out group-hover:scale-50 group-focus-visible:scale-50 motion-reduce:transition-none"></span>
        </span>
        <span class="absolute -inset-[30%] z-30 pointer-events-none -translate-x-[70%] bg-[linear-gradient(104deg,transparent_42%,rgba(255,255,255,0.42)_50%,transparent_58%)] transition-transform duration-[900ms] ease-tb51-out group-hover:translate-x-[70%] group-focus-visible:translate-x-[70%] motion-reduce:hidden"></span>
      </span>
    </span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb51-bg: #141613;
  --color-tb51-bg: oklch(0.18 0.01 130);
  --color-tb51-brass: #b28c4c;
  --color-tb51-brass: oklch(0.66 0.08 84);
  --color-tb51-brass-hi: #e8cc90;
  --color-tb51-brass-hi: oklch(0.86 0.08 88);
  --color-tb51-brass-lo: #6f5426;
  --color-tb51-brass-lo: oklch(0.45 0.07 82);
  --color-tb51-barrel-ring: #4a3819;
  --color-tb51-barrel-ring: oklch(0.34 0.055 82);
  --color-tb51-blade: #2a2b28;
  --color-tb51-blade: oklch(0.28 0.004 130);
  --color-tb51-blade-hi: #4a4b46;
  --color-tb51-blade-hi: oklch(0.42 0.004 130);
  --color-tb51-glass: #1a3b46;
  --color-tb51-glass: oklch(0.32 0.05 220);
  --color-tb51-coat: #4fd6c9;
  --color-tb51-coat: oklch(0.82 0.12 182);
  --font-tb51-sans: "Oswald", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb51-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-51 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(30rem 20rem at 50% 44%, color-mix(in oklab, var(--color-tb51-brass) 14%, transparent), transparent 74%), var(--color-tb51-bg);
}

.tb-51__bezel {
  background: radial-gradient(circle at 34% 26%, var(--color-tb51-brass-hi), transparent 56%), linear-gradient(150deg, var(--color-tb51-brass), var(--color-tb51-brass-lo));
}

.tb-51__barrel {
  background: radial-gradient(circle at 50% 50%, #101210, #050605);
}
/* COATED GLASS: coating tint + specular crescent + catchlight. The three together
   are what stop it reading as a coloured circle. */

.tb-51__glass {
  background: radial-gradient(circle at 62% 70%, color-mix(in oklab, var(--color-tb51-coat) 55%, transparent), transparent 58%), radial-gradient(circle at 34% 26%, rgba(255,255,255,.5), transparent 42%), radial-gradient(circle at 50% 50%, var(--color-tb51-glass), #08181d 78%);
}
/* BLADE ANGLES: each blade carries its own --i inline; the rotation composes it.
   rotate-[calc(var(--i)*60deg)] as a utility would compile ONE static rule that
   all six blades share — the same trap as the shard button's angle. */

.tb-51__blade {
  background: linear-gradient(120deg, var(--color-tb51-blade-hi), var(--color-tb51-blade));
  transform-origin: 50% 50%;
  rotate: calc(var(--i) * 60deg);
}

.tb-51 button:is(:hover, :focus-visible) .tb-51__blade {
  rotate: calc(var(--i) * 60deg + 44deg);
}
/* Safari ≤15.3 shims for the two bezel ring masks. */

.tb-51__bezel > span:first-child {
  -webkit-mask-image: radial-gradient(farthest-side, transparent 86%, #000 88%);
}

.tb-51__scale {
  -webkit-mask-image: radial-gradient(farthest-side, transparent 82%, #000 84%);
}

@media (prefers-color-scheme: light) {
  .tb-51:not([data-theme="dark"]) {
    --color-tb51-bg: oklch(0.23 0.012 130);
  }
}

.tb-51[data-theme="light"] {
  --color-tb51-bg: oklch(0.23 0.012 130);
}

@media (forced-colors: active) {
  .tb-51__bezel {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .tb-51__bezel > span:first-child,
    .tb-51__scale,
    .tb-51__barrel > span:last-child {
    display: none;
  }

  .tb-51__barrel {
    background: Canvas;
    box-shadow: inset 0 0 0 2px CanvasText;
  }

  .tb-51__blade {
    background: ButtonText;
  }
}
```
