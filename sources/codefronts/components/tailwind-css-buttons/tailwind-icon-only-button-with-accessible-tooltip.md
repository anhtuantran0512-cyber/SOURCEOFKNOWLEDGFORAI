---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-icon-only-button-with-accessible-tooltip/"
title: "Tailwind Icon-Only Button with Accessible Tooltip"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A four-button icon toolbar where each control carries a real accessible name, a 44px touch target inside a 40px visual square, and a tooltip that appears on…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Icon-Only Button with Accessible Tooltip
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-icon-only-button-with-accessible-tooltip/

A four-button icon toolbar where each control carries a real accessible name, a 44px touch target inside a 40px visual square, and a tooltip that appears on hover and keyboard focus. has-hover: and has-focus-visible: on the wrapper are the port's headline: the relational CSS selector becomes two variants sitting on the element that owns the tooltip.
## HTML
```html
<div class="tb-04 w-full min-h-svh grid place-items-center bg-tb04-bg text-tb04-text font-tb04-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <div role="toolbar" aria-label="Article actions" class="flex items-center gap-1.5 p-1.5 rounded-full bg-tb04-surface border border-tb04-line shadow-[0_12px_30px_-18px_var(--color-tb04-shadow)]">
    <span class="group/item relative inline-flex">
      <button type="button" aria-label="Share article" aria-describedby="tb-04-t1" style="anchor-name:--tb-04-a1" class="relative cursor-pointer grid place-items-center size-10 border-0 rounded-full text-tb04-muted bg-transparent transition-[background-color,color,scale] duration-200 ease-tb04-out after:content-[''] after:absolute after:-inset-1.5 after:rounded-full hover:text-tb04-accent hover:bg-tb04-tint hover:scale-105 active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tb04-accent focus-visible:text-tb04-accent motion-reduce:transition-colors motion-reduce:hover:scale-100">
        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="size-[1.15rem]"><circle cx="18" cy="5" r="2.6"/><circle cx="6" cy="12" r="2.6"/><circle cx="18" cy="19" r="2.6"/><path d="M8.4 10.8 15.6 6.6M8.4 13.2l7.2 4.2"/></svg>
      </button>
      <span role="tooltip" id="tb-04-t1" style="position-anchor:--tb-04-a1" class="tb-04__tip hidden opacity-0 translate-y-1 absolute left-1/2 -translate-x-1/2 bottom-full mb-2.5 z-10 pointer-events-none whitespace-nowrap px-2.5 py-1.5 rounded-md text-xs font-semibold tracking-[0.01em] text-tb04-tip-ink bg-tb04-tip-bg transition-[opacity,translate] transition-discrete duration-200 ease-tb04-out group-hover/item:block group-hover/item:opacity-100 group-hover/item:translate-y-0 group-has-focus-visible/item:block group-has-focus-visible/item:opacity-100 group-has-focus-visible/item:translate-y-0 starting:opacity-0 starting:translate-y-1 motion-reduce:transition-none">Share</span>
    </span>
    <span class="group/item relative inline-flex">
      <button type="button" aria-label="Bookmark article" aria-describedby="tb-04-t2" aria-pressed="false" style="anchor-name:--tb-04-a2" class="relative cursor-pointer grid place-items-center size-10 border-0 rounded-full text-tb04-muted bg-transparent transition-[background-color,color,scale] duration-200 ease-tb04-out after:content-[''] after:absolute after:-inset-1.5 after:rounded-full hover:text-tb04-accent hover:bg-tb04-tint hover:scale-105 active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tb04-accent focus-visible:text-tb04-accent aria-pressed:text-tb04-accent aria-pressed:bg-tb04-tint motion-reduce:transition-colors motion-reduce:hover:scale-100">
        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="size-[1.15rem]"><path d="M7 4h10a1 1 0 0 1 1 1v15l-6-4-6 4V5a1 1 0 0 1 1-1z"/></svg>
      </button>
      <span role="tooltip" id="tb-04-t2" style="position-anchor:--tb-04-a2" class="tb-04__tip hidden opacity-0 translate-y-1 absolute left-1/2 -translate-x-1/2 bottom-full mb-2.5 z-10 pointer-events-none whitespace-nowrap px-2.5 py-1.5 rounded-md text-xs font-semibold tracking-[0.01em] text-tb04-tip-ink bg-tb04-tip-bg transition-[opacity,translate] transition-discrete duration-200 ease-tb04-out group-hover/item:block group-hover/item:opacity-100 group-hover/item:translate-y-0 group-has-focus-visible/item:block group-has-focus-visible/item:opacity-100 group-has-focus-visible/item:translate-y-0 starting:opacity-0 starting:translate-y-1 motion-reduce:transition-none">Save for later</span>
    </span>
    <span class="group/item relative inline-flex">
      <button type="button" aria-label="Copy link" aria-describedby="tb-04-t3" style="anchor-name:--tb-04-a3" class="relative cursor-pointer grid place-items-center size-10 border-0 rounded-full text-tb04-muted bg-transparent transition-[background-color,color,scale] duration-200 ease-tb04-out after:content-[''] after:absolute after:-inset-1.5 after:rounded-full hover:text-tb04-accent hover:bg-tb04-tint hover:scale-105 active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tb04-accent focus-visible:text-tb04-accent motion-reduce:transition-colors motion-reduce:hover:scale-100">
        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="size-[1.15rem]"><path d="M10 14a4 4 0 0 0 5.66 0l2.5-2.5A4 4 0 0 0 12.5 5.84L11 7.3"/><path d="M14 10a4 4 0 0 0-5.66 0l-2.5 2.5A4 4 0 0 0 11.5 18.16L13 16.7"/></svg>
      </button>
      <span role="tooltip" id="tb-04-t3" style="position-anchor:--tb-04-a3" class="tb-04__tip hidden opacity-0 translate-y-1 absolute left-1/2 -translate-x-1/2 bottom-full mb-2.5 z-10 pointer-events-none whitespace-nowrap px-2.5 py-1.5 rounded-md text-xs font-semibold tracking-[0.01em] text-tb04-tip-ink bg-tb04-tip-bg transition-[opacity,translate] transition-discrete duration-200 ease-tb04-out group-hover/item:block group-hover/item:opacity-100 group-hover/item:translate-y-0 group-has-focus-visible/item:block group-has-focus-visible/item:opacity-100 group-has-focus-visible/item:translate-y-0 starting:opacity-0 starting:translate-y-1 motion-reduce:transition-none">Copy link</span>
    </span>
    <span class="group/item relative inline-flex">
      <button type="button" aria-label="Report article" aria-describedby="tb-04-t4" style="anchor-name:--tb-04-a4" class="relative cursor-pointer grid place-items-center size-10 border-0 rounded-full text-tb04-muted bg-transparent transition-[background-color,color,scale] duration-200 ease-tb04-out after:content-[''] after:absolute after:-inset-1.5 after:rounded-full hover:text-tb04-danger hover:bg-tb04-danger-tint hover:scale-105 active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tb04-danger focus-visible:text-tb04-danger motion-reduce:transition-colors motion-reduce:hover:scale-100">
        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="size-[1.15rem]"><path d="M12 4v11M12 19h.01"/><path d="M12 4 3.5 19h17L12 4z"/></svg>
      </button>
      <span role="tooltip" id="tb-04-t4" style="position-anchor:--tb-04-a4" class="tb-04__tip hidden opacity-0 translate-y-1 absolute left-1/2 -translate-x-1/2 bottom-full mb-2.5 z-10 pointer-events-none whitespace-nowrap px-2.5 py-1.5 rounded-md text-xs font-semibold tracking-[0.01em] text-tb04-tip-ink bg-tb04-tip-bg transition-[opacity,translate] transition-discrete duration-200 ease-tb04-out group-hover/item:block group-hover/item:opacity-100 group-hover/item:translate-y-0 group-has-focus-visible/item:block group-has-focus-visible/item:opacity-100 group-has-focus-visible/item:translate-y-0 starting:opacity-0 starting:translate-y-1 motion-reduce:transition-none">Report</span>
    </span>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb04-bg: #f4f4f2;
  --color-tb04-bg: oklch(0.968 0.004 100);
  --color-tb04-surface: #ffffff;
  --color-tb04-text: #18181b;
  --color-tb04-text: oklch(0.2 0.005 285);
  --color-tb04-muted: #6b6b74;
  --color-tb04-muted: oklch(0.49 0.01 285);
  --color-tb04-line: #e2e2dd;
  --color-tb04-line: oklch(0.9 0.005 100);
  --color-tb04-accent: #2563eb;
  --color-tb04-accent: oklch(0.53 0.21 262);
  --color-tb04-tint: #2563eb1f;
  --color-tb04-tint: oklch(0.53 0.21 262 / 0.12);
  --color-tb04-danger: #dc2626;
  --color-tb04-danger: oklch(0.55 0.21 27);
  --color-tb04-danger-tint: #dc26261f;
  --color-tb04-danger-tint: oklch(0.55 0.21 27 / 0.12);
  --color-tb04-tip-bg: #18181b;
  --color-tb04-tip-bg: oklch(0.2 0.005 285);
  --color-tb04-tip-ink: #fafafa;
  --color-tb04-shadow: #18181b8c;
  --color-tb04-shadow: oklch(0.2 0.005 285 / 0.55);
  --font-tb04-sans: "Manrope", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb04-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-04 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
/* Tooltip arrow — a pseudo-element with a border triangle has no utility form worth writing. */

.tb-04__tip::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  translate: -50% -1px;
  border: 0.3rem solid transparent;
  border-top-color: var(--color-tb04-tip-bg);
}
/* Anchor positioning: each button owns a unique inline anchor-name; one shared name on a
   class would tether all four tooltips to the same button. */

@supports (anchor-name: --a) {
  .tb-04__tip {
    position: fixed;
    position-area: block-start;
    justify-self: anchor-center;
    left: auto;
    bottom: auto;
    margin-bottom: 0.625rem;
  }
}

@media (prefers-color-scheme: dark) {
  .tb-04:not([data-theme="light"]) {
    --color-tb04-bg: oklch(0.13 0.004 285);
    --color-tb04-surface: oklch(0.18 0.005 285);
    --color-tb04-text: oklch(0.95 0.003 285);
    --color-tb04-muted: oklch(0.68 0.008 285);
    --color-tb04-line: oklch(0.29 0.008 285);
    --color-tb04-tip-bg: oklch(0.96 0.003 285);
    --color-tb04-tip-ink: oklch(0.16 0.006 285);
    --color-tb04-accent: oklch(0.74 0.14 262);
    --color-tb04-danger: oklch(0.7 0.17 27);
  }
}

.tb-04[data-theme="dark"] {
  --color-tb04-bg: oklch(0.13 0.004 285);
  --color-tb04-surface: oklch(0.18 0.005 285);
  --color-tb04-text: oklch(0.95 0.003 285);
  --color-tb04-muted: oklch(0.68 0.008 285);
  --color-tb04-line: oklch(0.29 0.008 285);
  --color-tb04-tip-bg: oklch(0.96 0.003 285);
  --color-tb04-tip-ink: oklch(0.16 0.006 285);
}

@media (forced-colors: active) {
  .tb-04 [role="toolbar"],
    .tb-04 button {
    border: 1px solid ButtonText;
  }

  .tb-04__tip {
    background: Canvas;
    color: CanvasText;
    border: 1px solid CanvasText;
  }
}
```
