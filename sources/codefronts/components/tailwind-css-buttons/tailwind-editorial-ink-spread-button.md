---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-editorial-ink-spread-button/"
title: "Tailwind Editorial Ink Spread Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "Letterpress restraint: a serif label on cream stock, a hairline rule that grows into a full underline, and an ink blot that floods from the baseline with a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Editorial Ink Spread Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-editorial-ink-spread-button/

Letterpress restraint: a serif label on cream stock, a hairline rule that grows into a full underline, and an ink blot that floods from the baseline with a soft irregular edge. The feathered mask is the whole effect and stays one arbitrary value — feathering is a recipe, not a design token.
## HTML
```html
<div class="tb-19 w-full min-h-svh grid place-items-center font-tb19-serif p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="group relative overflow-hidden isolate cursor-pointer min-h-14 px-8 pt-1.5 pb-2 border border-tb19-edge rounded-[0.25rem] bg-transparent text-tb19-ink text-[1.375rem] tracking-[0.005em] [font-variant-ligatures:common-ligatures] transition-[border-color,color] duration-[400ms] [transition-delay:0ms,100ms] hover:text-tb19-paper hover:border-tb19-ink focus-visible:text-tb19-paper focus-visible:border-tb19-ink focus-visible:outline-1 focus-visible:outline-tb19-accent focus-visible:outline-offset-[5px] active:scale-[0.99] disabled:cursor-not-allowed disabled:text-tb19-ink-off disabled:border-tb19-edge-off motion-reduce:transition-[color] motion-reduce:duration-100">
    <span aria-hidden="true" class="tb-19__ink absolute -inset-y-[20%] -inset-x-[10%] z-10 origin-bottom scale-[0.25] opacity-0 bg-tb19-ink [mask-image:radial-gradient(58%_120%_at_50%_112%,#000_38%,rgba(0,0,0,0.5)_64%,transparent_80%)] transition-[scale,opacity,background-color] duration-[620ms] ease-tb19-out group-hover:scale-[1.45] group-hover:opacity-100 group-focus-visible:scale-[1.45] group-focus-visible:opacity-100 group-active:bg-tb19-accent group-disabled:hidden motion-reduce:transition-opacity motion-reduce:duration-150 motion-reduce:scale-[1.45]"></span>
    <span class="relative z-20 after:content-[''] after:absolute after:inset-x-0 after:-bottom-[0.28rem] after:h-px after:bg-current after:origin-left after:scale-x-0 after:transition-transform after:duration-500 after:ease-tb19-out group-hover:after:scale-x-100 group-focus-visible:after:scale-x-100 motion-reduce:after:transition-none">Read the essay</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb19-paper: #f4efe4;
  --color-tb19-paper: oklch(0.95 0.018 85);
  --color-tb19-ink: #1a1614;
  --color-tb19-ink: oklch(0.2 0.012 40);
  --color-tb19-ink-off: #7a716a;
  --color-tb19-ink-off: oklch(0.55 0.012 50);
  --color-tb19-edge: #1a16144d;
  --color-tb19-edge: oklch(0.2 0.012 40 / 0.3);
  --color-tb19-edge-off: #1a161426;
  --color-tb19-edge-off: oklch(0.2 0.012 40 / 0.15);
  --color-tb19-accent: #8c2f1f;
  --color-tb19-accent: oklch(0.43 0.13 32);
  --font-tb19-serif: "Instrument Serif", ui-serif, Georgia, "Times New Roman", serif;
  --ease-tb19-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-19 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(60rem 40rem at 50% 0%, color-mix(in oklab, white 55%, transparent), transparent 60%), var(--color-tb19-paper);
}
/* Safari ≤15.3 mask shim — the utility emits the unprefixed property only. */

.tb-19__ink {
  -webkit-mask-image: radial-gradient(58% 120% at 50% 112%, #000 38%, rgba(0, 0, 0, 0.5) 64%, transparent 80%);
}

@media (prefers-color-scheme: dark) {
  .tb-19:not([data-theme="light"]) {
    --color-tb19-paper: oklch(0.16 0.012 45);
    --color-tb19-ink: oklch(0.93 0.02 80);
    --color-tb19-ink-off: oklch(0.6 0.015 60);
    --color-tb19-accent: oklch(0.72 0.12 40);
  }
}

.tb-19[data-theme="dark"] {
  --color-tb19-paper: oklch(0.16 0.012 45);
  --color-tb19-ink: oklch(0.93 0.02 80);
  --color-tb19-accent: oklch(0.72 0.12 40);
}

@media (forced-colors: active) {
  .tb-19 button {
    color: ButtonText;
    border-color: ButtonText;
    background: ButtonFace;
  }

  .tb-19__ink {
    display: none;
  }

  .tb-19 button:hover {
    background: Highlight;
    color: HighlightText;
  }
}
```
