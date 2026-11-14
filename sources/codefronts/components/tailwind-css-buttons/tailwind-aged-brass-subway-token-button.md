---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-aged-brass-subway-token-button/"
title: "Tailwind Aged Brass Subway Token Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A 1953 transit token: milled rim, tarnished brass, and a knocked-out letter you can see the background through — a mask-composite cut, not a coloured glyph."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Aged Brass Subway Token Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-aged-brass-subway-token-button/

A 1953 transit token: milled rim, tarnished brass, and a knocked-out letter you can see the background through — a mask-composite cut, not a coloured glyph. Press it and the token drops into the slot and springs back.
## HTML
```html
<div class="tb-42 w-full min-h-svh grid place-items-center font-tb42-sans p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" aria-label="Use one transit token" class="group relative cursor-pointer border-0 bg-transparent p-0 w-30 h-[9.5rem] grid place-items-start justify-center [-webkit-tap-highlight-color:transparent] focus-visible:outline-none disabled:cursor-not-allowed disabled:grayscale-[0.7] disabled:brightness-[0.85]">
    <span aria-hidden="true" class="absolute inset-x-[12%] bottom-1.5 h-2 rounded-full bg-[linear-gradient(180deg,#0a0c0b,#1d221f)] shadow-[inset_0_2px_4px_#000000e6,0_1px_0_#ffffff14]"></span>
    <span aria-hidden="true" class="tb-42__disc relative grid place-items-center size-30 rounded-full isolate text-tb42-brass-lo shadow-[inset_0_2px_3px_#ffffff66,inset_0_-3px_6px_#00000073,0_14px_22px_-10px_#000000cc] transition-[translate,filter] duration-300 ease-tb42-out group-hover:-translate-y-[3px] group-hover:brightness-105 group-active:animate-tb42-drop group-focus-visible:outline-2 group-focus-visible:outline-offset-[5px] group-focus-visible:outline-tb42-brass-hi motion-reduce:transition-none motion-reduce:group-active:animate-none">
      <span class="absolute inset-0 z-20 rounded-full opacity-85 bg-[repeating-conic-gradient(from_0deg,var(--color-tb42-reed-hi)_0deg_1.6deg,var(--color-tb42-reed-lo)_1.6deg_3.2deg)] [mask-image:radial-gradient(farthest-side,transparent_calc(100%-6px),#000_calc(100%-6px))]"></span>
      <span class="tb-42__patina absolute inset-0 z-10 rounded-full opacity-45"></span>
      <span class="tb-42__glyph relative z-30 text-[3.1rem] font-bold leading-none text-tb42-brass-lo [text-shadow:0_1px_0_#ffffff59,0_-1px_0_#00000073]">T</span>
    </span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb42-bg: #191c1a;
  --color-tb42-bg: oklch(0.21 0.008 150);
  --color-tb42-brass: #a98a4a;
  --color-tb42-brass: oklch(0.64 0.08 88);
  --color-tb42-brass-hi: #dcbe7c;
  --color-tb42-brass-hi: oklch(0.82 0.09 90);
  --color-tb42-brass-lo: #6d5527;
  --color-tb42-brass-lo: oklch(0.44 0.07 85);
  --color-tb42-patina: #4f7a5f;
  --color-tb42-patina: oklch(0.55 0.07 160);
  --color-tb42-reed-hi: #cfae68;
  --color-tb42-reed-hi: oklch(0.76 0.09 88);
  --color-tb42-reed-lo: #7a5f2c;
  --color-tb42-reed-lo: oklch(0.48 0.08 86);
  --font-tb42-sans: "Oswald", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb42-out: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tb42-drop: tb-42-drop 0.62s cubic-bezier(0.3, 0.05, 0.4, 1);
}

@keyframes tb-42-drop {
  0% {
    translate: 0 0;
  }

  38% {
    translate: 0 1.15rem;
    scale: 1 0.94;
  }

  62% {
    translate: 0 -0.3rem;
    scale: 1 1.02;
  }

  100% {
    translate: 0 0;
    scale: 1 1;
  }
}

.tb-42 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(30rem 20rem at 50% 44%, #26302a, transparent 74%), var(--color-tb42-bg);
}

.tb-42__disc {
  background: radial-gradient(circle at 34% 28%, var(--color-tb42-brass-hi), transparent 54%), radial-gradient(circle at 72% 78%, var(--color-tb42-brass-lo), transparent 56%), linear-gradient(152deg, var(--color-tb42-brass), color-mix(in oklab, var(--color-tb42-brass) 80%, black));
}

.tb-42__patina {
  mix-blend-mode: color-burn;
  background: radial-gradient(2rem 1.6rem at 26% 74%, var(--color-tb42-patina), transparent 72%), radial-gradient(1.6rem 2rem at 76% 32%, var(--color-tb42-patina), transparent 74%);
}
/* Safari ≤15.3 rim mask shim. */

.tb-42 [class*="mask-image"] {
  -webkit-mask-image: radial-gradient(farthest-side, transparent calc(100% - 6px), #000 calc(100% - 6px));
}
/* THE KNOCKOUT: the glyph is subtracted from the metal, so the hole shows the page.
   A data-URI SVG text mask keeps the cut crisp at any size. Where mask-composite is
   unavailable the fallback above stands: a normal engraved letter. */

@supports ((mask-composite: exclude) or (-webkit-mask-composite: destination-out)) {
  .tb-42__glyph {
    color: transparent;
    text-shadow: none;
  }

  .tb-42__disc {
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Ctext x='60' y='86' font-family='Oswald,sans-serif' font-size='78' font-weight='700' text-anchor='middle' fill='%23000'%3ET%3C/text%3E%3C/svg%3E") 50% 50%/60% 60% no-repeat, linear-gradient(#000, #000);
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Ctext x='60' y='86' font-family='Oswald,sans-serif' font-size='78' font-weight='700' text-anchor='middle' fill='%23000'%3ET%3C/text%3E%3C/svg%3E") 50% 50%/60% 60% no-repeat, linear-gradient(#000, #000);
    -webkit-mask-composite: destination-out;
    mask-composite: exclude;
  }
}

@media (prefers-color-scheme: light) {
  .tb-42:not([data-theme="dark"]) {
    --color-tb42-bg: oklch(0.26 0.01 150);
  }
}

.tb-42[data-theme="light"] {
  --color-tb42-bg: oklch(0.26 0.01 150);
}

@media (forced-colors: active) {
  .tb-42__disc {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
    mask: none;
    -webkit-mask: none;
  }

  .tb-42__glyph {
    color: ButtonText;
    text-shadow: none;
  }

  .tb-42__disc > span:not(.tb-42__glyph) {
    display: none;
  }
}
```
