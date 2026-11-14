---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-vinyl-record-sleeve-ripple-button/"
title: "Tailwind Vinyl Record Sleeve Ripple Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A record slides half out of its sleeve on hover and starts turning; press it and concentric ripples run out through the grooves like a needle drop."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vinyl Record Sleeve Ripple Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-vinyl-record-sleeve-ripple-button/

A record slides half out of its sleeve on hover and starts turning; press it and concentric ripples run out through the grooves like a needle drop. Grooves and label are pure gradients, and the sleeve carries real cover art with a flat fallback.
## HTML
```html
<div class="tb-39 w-full min-h-svh grid place-items-center font-tb39-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="group relative isolate cursor-pointer border-0 bg-transparent p-0 size-46 [-webkit-tap-highlight-color:transparent] focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tb39-label focus-visible:rounded-[0.35rem] disabled:cursor-not-allowed disabled:grayscale-[0.7]">
    <span aria-hidden="true" class="tb-39__disc absolute z-10 inset-1.5 rounded-full shadow-[0_8px_18px_-6px_#000000cc,inset_0_0_0_1px_#ffffff0f] transition-transform duration-[550ms] ease-tb39-out group-hover:translate-x-[56%] group-hover:animate-tb39-spin group-focus-visible:translate-x-[56%] group-focus-visible:animate-tb39-spin motion-reduce:transition-none motion-reduce:group-hover:animate-none">
      <span class="absolute inset-[20%] rounded-full border-2 border-white/60 opacity-0 group-active:animate-tb39-ripple motion-reduce:hidden"></span>
      <span class="absolute inset-[20%] rounded-full border-2 border-white/60 opacity-0 [animation-delay:0.12s] group-active:animate-tb39-ripple motion-reduce:hidden"></span>
    </span>
    <span class="absolute z-20 inset-0 overflow-hidden grid content-end rounded-[0.25rem] bg-[linear-gradient(150deg,var(--color-tb39-sleeve),var(--color-tb39-sleeve-lo))] shadow-[0_20px_34px_-16px_#000000d9,inset_0_0_0_1px_#0000002e] transition-transform duration-200 group-active:scale-[0.99] motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=700&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="700" height="700" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover bg-tb39-sleeve-lo saturate-105 contrast-105">
      <span aria-hidden="true" class="absolute inset-y-0 left-0 w-2 bg-[linear-gradient(90deg,#00000066,transparent)]"></span>
      <span class="relative z-30 m-3 px-3 py-2 rounded-[0.25rem] text-[0.8125rem] font-extrabold tracking-[-0.01em] text-tb39-sleeve bg-tb39-scrim backdrop-blur-[3px]">Play side one</span>
    </span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb39-bg: #131316;
  --color-tb39-bg: oklch(0.19 0.006 285);
  --color-tb39-sleeve: #e9e4d8;
  --color-tb39-sleeve: oklch(0.91 0.015 90);
  --color-tb39-sleeve-lo: #c9c2b2;
  --color-tb39-sleeve-lo: oklch(0.8 0.02 88);
  --color-tb39-label: #d8483b;
  --color-tb39-label: oklch(0.58 0.19 30);
  --color-tb39-scrim: #0c0c0ec4;
  --color-tb39-scrim: oklch(0.15 0.006 285 / 0.78);
  --font-tb39-sans: "Archivo", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb39-out: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tb39-spin: tb-39-spin 3.4s linear infinite;
  --animate-tb39-ripple: tb-39-ripple 0.7s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes tb-39-spin {
  to {
    rotate: 1turn;
  }
}

@keyframes tb-39-ripple {
  0% {
    opacity: 0.7;
    scale: 0.3;
  }

  100% {
    opacity: 0;
    scale: 1.9;
  }
}

.tb-39 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(34rem 22rem at 50% 44%, #1e1e24, transparent 74%), var(--color-tb39-bg);
}
/* THE RECORD: grooves (repeating radial), a spec sweep (conic), then the label
   and vinyl (radial). Three layers that only read as vinyl together.
   The spindle hole is a pseudo-element punched in the page colour. */

.tb-39__disc {
  background: repeating-radial-gradient(circle at 50% 50%, rgba(255,255,255,.055) 0 1px, transparent 1px 3px), conic-gradient(from 210deg, rgba(255,255,255,.14), transparent 26%, rgba(255,255,255,.1) 56%, transparent 82%), radial-gradient(circle, var(--color-tb39-label) 0 25%, #1a1a1a 26%, #0b0b0b 100%);
}

.tb-39__disc::after {
  content: '';
  position: absolute;
  inset: 47.5%;
  border-radius: 50%;
  background: var(--color-tb39-bg);
  box-shadow: 0 0 0 1px rgba(0,0,0,.6);
}

@media (prefers-color-scheme: light) {
  .tb-39:not([data-theme="dark"]) {
    --color-tb39-bg: oklch(0.23 0.008 285);
  }
}

.tb-39[data-theme="light"] {
  --color-tb39-bg: oklch(0.23 0.008 285);
}

@media (forced-colors: active) {
  .tb-39 button > span:last-child {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .tb-39 button > span:last-child > span:last-child {
    background: ButtonFace;
    color: ButtonText;
  }

  .tb-39__disc {
    display: none;
  }
}
```
