---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-obsidian-glass-shard-button/"
title: "Tailwind Obsidian Glass Shard Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A shard of volcanic glass: an asymmetric faceted silhouette from clip-path, near-black translucency over a blurred backdrop, two facet planes shaded by…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Obsidian Glass Shard Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-obsidian-glass-shard-button/

A shard of volcanic glass: an asymmetric faceted silhouette from clip-path, near-black translucency over a blurred backdrop, two facet planes shaded by opposing gradients, and a razor of light that runs along the leading edge on hover.
## HTML
```html
<div class="tb-34 w-full min-h-svh grid place-items-center font-tb34-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <span class="group inline-block rounded-[0.2rem] drop-shadow-[0_18px_28px_#000000bf] transition-[translate,filter] duration-[350ms] ease-tb34-out has-hover:-translate-y-[3px] has-hover:drop-shadow-[0_26px_34px_#000000cc] has-focus-visible:outline-2 has-focus-visible:outline-offset-[6px] has-focus-visible:outline-tb34-glow motion-reduce:transition-none">
    <button type="button" class="tb-34__shard relative overflow-hidden cursor-pointer grid place-items-center min-h-15 px-12 border-0 text-base font-bold tracking-[0.02em] text-tb34-ink bg-tb34-glass backdrop-blur-[10px] backdrop-saturate-[1.2] transition-[scale] duration-200 ease-tb34-out focus-visible:outline-none active:scale-[0.985] disabled:cursor-not-allowed disabled:text-tb34-muted motion-reduce:transition-none">
      <span aria-hidden="true" class="tb-34__rim absolute inset-px z-10 pointer-events-none shadow-[inset_0_0_0_1px_var(--color-tb34-rim)]"></span>
      <span aria-hidden="true" class="absolute -inset-y-[30%] -inset-x-[40%] z-20 pointer-events-none -translate-x-[70%] bg-[linear-gradient(100deg,transparent_44%,var(--color-tb34-glow-bar)_50%,transparent_56%)] transition-transform duration-[850ms] ease-tb34-out group-hover:translate-x-[70%] group-focus-within:translate-x-[70%] motion-reduce:hidden"></span>
      <span class="relative z-30 [text-shadow:0_1px_10px_#000000b3]">Enter the vault</span>
    </button>
  </span>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb34-bg: #07070a;
  --color-tb34-bg: oklch(0.1 0.008 280);
  --color-tb34-glass: #101116d1;
  --color-tb34-glass: oklch(0.18 0.012 275 / 0.82);
  --color-tb34-ink: #eef2f8;
  --color-tb34-ink: oklch(0.95 0.008 260);
  --color-tb34-muted: #8b93a3;
  --color-tb34-muted: oklch(0.63 0.02 260);
  --color-tb34-glow: #bfe3ff;
  --color-tb34-glow: oklch(0.9 0.06 235);
  --color-tb34-glow-bar: #bfe3ffd9;
  --color-tb34-glow-bar: oklch(0.9 0.06 235 / 0.85);
  --color-tb34-rim: #bfe3ff4d;
  --color-tb34-rim: oklch(0.9 0.06 235 / 0.3);
  --font-tb34-sans: "Syne", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb34-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-34 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  --tb-34-shape: polygon(4% 0, 100% 6%, 96% 82%, 88% 100%, 0 94%, 3% 18%);
  background: radial-gradient(38rem 22rem at 50% 45%, #14161d, transparent 74%), var(--color-tb34-bg);
}
/* The shape is shared by the button and its 1px rim layer — one variable, so the
   inset can never drift at the corners. Facets: two hard-stop planes over the base. */

.tb-34__shard {
  clip-path: var(--tb-34-shape);
  background-image: linear-gradient(122deg, rgba(255,255,255,.1) 0 38%, transparent 38.5%), linear-gradient(-58deg, rgba(255,255,255,.05) 0 30%, transparent 30.5%), linear-gradient(160deg, rgba(52,58,74,.95), rgba(14,16,22,.97));
}

.tb-34__rim {
  clip-path: var(--tb-34-shape);
}

@media (prefers-color-scheme: light) {
  .tb-34:not([data-theme="dark"]) {
    --color-tb34-bg: oklch(0.16 0.012 275);
  }
}

.tb-34[data-theme="light"] {
  --color-tb34-bg: oklch(0.16 0.012 275);
}

@media (forced-colors: active) {
  .tb-34__shard {
    clip-path: none;
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    backdrop-filter: none;
    -webkit-backdrop-filter: none;
  }

  .tb-34__shard span[aria-hidden] {
    display: none;
  }

  .tb-34 > span {
    filter: none;
  }
}
```
