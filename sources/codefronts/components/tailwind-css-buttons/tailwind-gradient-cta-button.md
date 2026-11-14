---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-gradient-cta-button/"
title: "Tailwind Gradient CTA Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A conversion-grade CTA with a conic gradient ring that rotates continuously, a soft bloom underneath, and a mesh body that shifts on hover."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gradient CTA Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-gradient-cta-button/

A conversion-grade CTA with a conic gradient ring that rotates continuously, a soft bloom underneath, and a mesh body that shifts on hover. The rotation needs @property to register the angle as an <angle>, which is the clearest case in the collection for keeping machinery in the stylesheet and exposing only the result as animate-tb05-spin.
## HTML
```html
<div class="tb-05 w-full min-h-svh grid place-items-center font-tb05-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="group relative isolate cursor-pointer inline-grid grid-flow-col items-center gap-2 min-h-14 px-8 border-0 rounded-2xl text-base font-semibold tracking-[-0.005em] text-white bg-[radial-gradient(120%_140%_at_15%_0%,var(--color-tb05-c1-soft),transparent_60%),radial-gradient(120%_140%_at_90%_100%,var(--color-tb05-c2-soft),transparent_60%),var(--color-tb05-body)] bg-[length:150%_150%,150%_150%,100%_100%] bg-[position:0%_0%,100%_100%,0_0] transition-[translate,background-position,scale] duration-300 ease-tb05-out before:content-[''] before:absolute before:-inset-0.5 before:-z-10 before:rounded-[inherit] before:bg-[conic-gradient(from_var(--tb-05-a),var(--color-tb05-c1),var(--color-tb05-c2),var(--color-tb05-c3),var(--color-tb05-c1))] before:animate-tb05-spin after:content-[''] after:absolute after:inset-0.5 after:-z-10 after:rounded-[inherit] after:bg-[conic-gradient(from_var(--tb-05-a),var(--color-tb05-c1),var(--color-tb05-c2),var(--color-tb05-c3),var(--color-tb05-c1))] after:blur-[20px] after:opacity-55 after:animate-tb05-spin after:transition-opacity after:duration-300 hover:-translate-y-0.5 hover:bg-[position:30%_20%,70%_80%,0_0] hover:after:opacity-90 focus-visible:after:opacity-90 active:scale-[0.98] active:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tb05-c2 disabled:cursor-not-allowed disabled:grayscale-[0.85] disabled:opacity-55 motion-reduce:transition-none motion-reduce:before:animate-none motion-reduce:after:animate-none">
    <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" class="size-[1.1rem] text-tb05-c2"><path d="M13 3 4.5 13.5H11l-1 7.5 8.5-10.5H12l1-7.5z"/></svg>
    <span>Upgrade to Pro</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@property --tb-05-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 135deg;
}

@theme {
  --color-tb05-bg: #08070d;
  --color-tb05-bg: oklch(0.13 0.02 290);
  --color-tb05-body: #141024;
  --color-tb05-body: oklch(0.2 0.04 290);
  --color-tb05-c1: #6d28d9;
  --color-tb05-c1: oklch(0.52 0.24 293);
  --color-tb05-c1-soft: #6d28d98c;
  --color-tb05-c1-soft: oklch(0.52 0.24 293 / 0.55);
  --color-tb05-c2: #2dd4bf;
  --color-tb05-c2: oklch(0.8 0.14 182);
  --color-tb05-c2-soft: #2dd4bf59;
  --color-tb05-c2-soft: oklch(0.8 0.14 182 / 0.35);
  --color-tb05-c3: #f472b6;
  --color-tb05-c3: oklch(0.74 0.17 349);
  --font-tb05-sans: "Sora", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb05-out: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tb05-spin: tb-05-spin 4.5s linear infinite;
}

@keyframes tb-05-spin {
  to {
    --tb-05-a: 495deg;
  }
}
/* Stage backdrop: a bloom behind the button plus the base colour. Two layers, one element. */

.tb-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(60rem 40rem at 50% 120%, color-mix(in oklab, var(--color-tb05-c1) 22%, transparent), transparent 70%), var(--color-tb05-bg);
}

.tb-05 button:disabled::before,
.tb-05 button:disabled::after {
  animation-play-state: paused;
}

@media (prefers-color-scheme: light) {
  .tb-05:not([data-theme="dark"]) {
    --color-tb05-bg: oklch(0.96 0.01 290);
    --color-tb05-body: oklch(0.24 0.06 290);
  }
}

.tb-05[data-theme="light"] {
  --color-tb05-bg: oklch(0.96 0.01 290);
  --color-tb05-body: oklch(0.24 0.06 290);
}

@media (forced-colors: active) {
  .tb-05 button {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .tb-05 button::before,
    .tb-05 button::after {
    display: none;
  }
}
```
