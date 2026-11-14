---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-ghost-outline-button/"
title: "Tailwind Ghost / Outline Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A ghost button that keeps its 1px silhouette at rest and fills from the bottom edge on hover, the label inverting in the same beat."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Ghost / Outline Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-ghost-outline-button/

A ghost button that keeps its 1px silhouette at rest and fills from the bottom edge on hover, the label inverting in the same beat. The fill is one background-size transition on a fixed gradient — no pseudo-element, no overflow clipping — and the border is currentColor, so one colour utility re-skins the whole control.
## HTML
```html
<div class="tb-03 w-full min-h-svh grid place-items-center bg-tb03-bg font-tb03-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="group cursor-pointer inline-grid grid-flow-col items-center gap-2.5 min-h-13 px-7 border border-current rounded-full text-[0.9375rem] font-medium tracking-[0.01em] text-tb03-accent bg-transparent bg-[linear-gradient(var(--color-tb03-accent),var(--color-tb03-accent))] bg-no-repeat bg-bottom bg-[length:100%_0%] transition-[background-size,color,letter-spacing] duration-[420ms] ease-tb03-out [transition-delay:0ms,60ms,0ms] hover:bg-[length:100%_100%] hover:text-tb03-on-accent hover:tracking-[0.03em] focus-visible:bg-[length:100%_100%] focus-visible:text-tb03-on-accent focus-visible:tracking-[0.03em] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tb03-accent active:scale-[0.985] disabled:cursor-not-allowed disabled:opacity-40 disabled:bg-[length:100%_0%] motion-reduce:transition-[color,background-size] motion-reduce:duration-100 motion-reduce:hover:tracking-[0.01em]">
    <span>Read the case study</span>
    <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" class="w-[1.05rem] h-[1.05rem] transition-transform duration-[420ms] ease-tb03-out group-hover:rotate-45 group-focus-visible:rotate-45 motion-reduce:transition-none motion-reduce:group-hover:rotate-0"><path d="M7 17 17 7"/><path d="M8.5 7H17v8.5"/></svg>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb03-bg: #faf9f6;
  --color-tb03-bg: oklch(0.978 0.006 95);
  --color-tb03-accent: #111827;
  --color-tb03-accent: oklch(0.22 0.02 265);
  --color-tb03-on-accent: #f9fafb;
  --color-tb03-on-accent: oklch(0.98 0.003 265);
  --font-tb03-sans: "Space Grotesk", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb03-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}

@media (prefers-color-scheme: dark) {
  .tb-03:not([data-theme="light"]) {
    --color-tb03-bg: oklch(0.14 0.004 265);
    --color-tb03-accent: oklch(0.96 0.004 95);
    --color-tb03-on-accent: oklch(0.16 0.006 265);
  }
}

.tb-03[data-theme="dark"] {
  --color-tb03-bg: oklch(0.14 0.004 265);
  --color-tb03-accent: oklch(0.96 0.004 95);
  --color-tb03-on-accent: oklch(0.16 0.006 265);
}

@media (forced-colors: active) {
  .tb-03 button {
    background: none;
    border-color: ButtonText;
    color: ButtonText;
  }

  .tb-03 button:hover {
    background: Highlight;
    color: HighlightText;
  }
}
```
