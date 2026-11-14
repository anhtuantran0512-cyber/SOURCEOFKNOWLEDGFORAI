---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-pharma-gel-capsule-button/"
title: "Tailwind Pharma Gel Capsule Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A two-tone gelatin capsule with a wet specular streak, a visible seam where the halves overlap, and a dose of liquid that rises through the shell on hover."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pharma Gel Capsule Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-pharma-gel-capsule-button/

A two-tone gelatin capsule with a wet specular streak, a visible seam where the halves overlap, and a dose of liquid that rises through the shell on hover. Press it and the capsule compresses along its long axis like soft gelatin.
## HTML
```html
<div class="tb-26 w-full min-h-svh grid place-items-center font-tb26-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="tb-26__capsule group relative overflow-hidden isolate cursor-pointer min-h-14 pr-9 pl-[calc(var(--tb-26-cap)+1rem)] border-0 rounded-full text-base font-bold tracking-[-0.005em] text-white shadow-[inset_0_-0.35rem_0.7rem_#0000002e,inset_0_0.3rem_0.5rem_#ffffff80,0_14px_26px_-14px_#1e12128c] transition-[scale,translate,box-shadow] duration-300 ease-tb26-out [-webkit-tap-highlight-color:transparent] hover:-translate-y-0.5 active:translate-y-px active:scale-x-[1.03] active:scale-y-90 active:shadow-[inset_0_0.3rem_0.8rem_#00000047] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tb26-body disabled:cursor-not-allowed disabled:grayscale-75 disabled:opacity-70 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
    <span aria-hidden="true" class="tb-26__dose absolute z-20 inset-y-0 left-0 right-[calc(100%-var(--tb-26-cap))] origin-bottom scale-y-[0.22] shadow-[inset_0_0.1rem_0_#ffffff99,inset_0_-0.3rem_0.5rem_#78380038] transition-[scale] duration-[550ms] ease-tb26-out group-hover:scale-y-[0.84] group-focus-visible:scale-y-[0.84] motion-reduce:transition-none"></span>
    <span aria-hidden="true" class="absolute z-30 inset-x-[8%] top-[14%] h-[26%] rounded-full pointer-events-none blur-[1.5px] bg-[linear-gradient(90deg,transparent,rgba(255,255,255,0.85)_20%,rgba(255,255,255,0.5)_58%,transparent)]"></span>
    <span class="relative z-40 [text-shadow:0_1px_1px_#50140e66]">Take one daily</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb26-bg: #eef2f4;
  --color-tb26-bg: oklch(0.955 0.006 220);
  --color-tb26-cap: #f6f8fa;
  --color-tb26-cap: oklch(0.975 0.004 220);
  --color-tb26-body: #cf3f33;
  --color-tb26-body: oklch(0.54 0.19 28);
  --color-tb26-liquid: #ffb347;
  --color-tb26-liquid: oklch(0.82 0.14 72);
  --color-tb26-liquid-hi: #ffd08f;
  --color-tb26-liquid-hi: oklch(0.88 0.1 76);
  --color-tb26-liquid-lo: #d98c22;
  --color-tb26-liquid-lo: oklch(0.7 0.14 68);
  --font-tb26-sans: "DM Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb26-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-26 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(34rem 20rem at 50% 40%, #ffffff, transparent 70%), var(--color-tb26-bg);
}
/* THE SHELL: two halves plus the seam where the cap slides over the body. Both
   layers are driven by --tb-26-cap in four places, so they stay together here. */

.tb-26__capsule {
  --tb-26-cap: 5.5rem;
  background-image: linear-gradient(90deg, var(--color-tb26-cap) 0 var(--tb-26-cap), var(--color-tb26-body) var(--tb-26-cap) 100%), linear-gradient(90deg, transparent calc(var(--tb-26-cap) - .5rem), rgba(0,0,0,.14) calc(var(--tb-26-cap) - .1rem), rgba(255,255,255,.32) calc(var(--tb-26-cap) + .2rem), transparent calc(var(--tb-26-cap) + .7rem));
}

.tb-26__dose {
  background: linear-gradient(180deg, var(--color-tb26-liquid-hi), var(--color-tb26-liquid) 42%, var(--color-tb26-liquid-lo));
}

@media (prefers-color-scheme: dark) {
  .tb-26:not([data-theme="light"]) {
    --color-tb26-bg: oklch(0.18 0.008 220);
    --color-tb26-cap: oklch(0.92 0.008 220);
    --color-tb26-body: oklch(0.5 0.18 28);
  }
}

.tb-26[data-theme="dark"] {
  --color-tb26-bg: oklch(0.18 0.008 220);
  --color-tb26-cap: oklch(0.92 0.008 220);
  --color-tb26-body: oklch(0.5 0.18 28);
}

@media (forced-colors: active) {
  .tb-26__capsule {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .tb-26__capsule span[aria-hidden] {
    display: none;
  }
}
```
