---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-confirm-delete-button/"
title: "Tailwind Confirm Delete Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A destructive action that asks once, inline, without a modal: the row expands to reveal \"Sure?"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Confirm Delete Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-confirm-delete-button/

A destructive action that asks once, inline, without a modal: the row expands to reveal "Sure? / Yes, delete" with the confirm deliberately placed second and never under the original cursor. The 0fr → 1fr grid-track animation ports to two utilities, which is the cleanest possible expression of it.
## HTML
```html
<div class="tb-12 w-full min-h-svh grid place-items-center bg-tb12-bg text-tb12-text font-tb12-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <span class="group grid grid-cols-[auto_0fr] items-center p-1.5 rounded-[1.1rem] bg-tb12-surface border border-tb12-line shadow-[0_14px_34px_-22px_var(--color-tb12-shadow)] transition-[grid-template-columns,border-color] duration-[450ms] ease-tb12-out has-checked:grid-cols-[auto_1fr] has-checked:border-tb12-danger-line has-focus-visible:outline-2 has-focus-visible:outline-offset-[3px] has-focus-visible:outline-tb12-danger motion-reduce:transition-none">
    <label class="cursor-pointer inline-flex items-center gap-2 min-h-11 px-4 rounded-xl text-[0.9375rem] font-semibold text-tb12-muted transition-colors duration-200 [-webkit-tap-highlight-color:transparent] hover:text-tb12-danger hover:bg-tb12-danger-tint group-has-checked:text-tb12-danger motion-reduce:transition-none">
      <input type="checkbox" aria-label="Delete this project, requires confirmation" class="sr-only">
      <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="size-5 shrink-0">
        <g class="tb-12__lid [transform-origin:18%_60%] transition-[rotate,translate] duration-[380ms] ease-tb12-out group-has-checked:-rotate-[24deg] group-has-checked:-translate-x-px group-has-checked:-translate-y-[1.5px] motion-reduce:transition-none"><path d="M4.5 7h15"/><path d="M9.5 7V5.2A1.2 1.2 0 0 1 10.7 4h2.6a1.2 1.2 0 0 1 1.2 1.2V7"/></g>
        <path d="M6.5 7.8 7.4 19a1.5 1.5 0 0 0 1.5 1.4h6.2a1.5 1.5 0 0 0 1.5-1.4l.9-11.2"/><path d="M10.5 11v6M13.5 11v6"/>
      </svg>
      <span class="group-has-checked:line-through group-has-checked:decoration-tb12-danger-line">Delete project</span>
    </label>
    <span class="min-w-0 overflow-hidden">
      <span class="flex items-center gap-2.5 pl-2 pr-0.5 opacity-0 -translate-x-2 transition-[opacity,translate] duration-[400ms] delay-[80ms] ease-tb12-out group-has-checked:opacity-100 group-has-checked:translate-x-0 motion-reduce:transition-none">
        <span class="text-[0.8125rem] font-semibold text-tb12-muted whitespace-nowrap">Sure?</span>
        <button type="button" class="cursor-pointer whitespace-nowrap border-0 rounded-xl min-h-11 px-4.5 text-sm font-bold text-tb12-danger-ink bg-tb12-danger shadow-[0_8px_18px_-12px_var(--color-tb12-danger-glow)] transition-[background-color,translate] duration-200 ease-tb12-out hover:bg-tb12-danger-deep hover:-translate-y-px active:translate-y-px focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tb12-danger motion-reduce:transition-none">Yes, delete</button>
      </span>
    </span>
  </span>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb12-bg: #f6f5f3;
  --color-tb12-bg: oklch(0.968 0.004 90);
  --color-tb12-surface: #ffffff;
  --color-tb12-line: #e3e1dc;
  --color-tb12-line: oklch(0.9 0.008 90);
  --color-tb12-text: #1a1817;
  --color-tb12-text: oklch(0.21 0.006 60);
  --color-tb12-muted: #5c5750;
  --color-tb12-muted: oklch(0.45 0.01 70);
  --color-tb12-danger: #b91c1c;
  --color-tb12-danger: oklch(0.48 0.2 27);
  --color-tb12-danger-deep: #8f1414;
  --color-tb12-danger-deep: oklch(0.4 0.18 27);
  --color-tb12-danger-line: #b91c1c8c;
  --color-tb12-danger-line: oklch(0.48 0.2 27 / 0.55);
  --color-tb12-danger-tint: #b91c1c14;
  --color-tb12-danger-tint: oklch(0.48 0.2 27 / 0.08);
  --color-tb12-danger-glow: #b91c1cd9;
  --color-tb12-danger-glow: oklch(0.48 0.2 27 / 0.85);
  --color-tb12-danger-ink: #ffffff;
  --color-tb12-shadow: #1a1817a6;
  --color-tb12-shadow: oklch(0.21 0.006 60 / 0.65);
  --font-tb12-sans: "Schibsted Grotesk", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb12-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}

@media (prefers-color-scheme: dark) {
  .tb-12:not([data-theme="light"]) {
    --color-tb12-bg: oklch(0.13 0.004 60);
    --color-tb12-surface: oklch(0.18 0.006 60);
    --color-tb12-line: oklch(0.28 0.008 60);
    --color-tb12-text: oklch(0.95 0.006 80);
    --color-tb12-muted: oklch(0.75 0.01 70);
    --color-tb12-danger: oklch(0.65 0.2 27);
    --color-tb12-danger-deep: oklch(0.57 0.2 27);
    --color-tb12-danger-ink: oklch(0.15 0.05 27);
  }
}

.tb-12[data-theme="dark"] {
  --color-tb12-bg: oklch(0.13 0.004 60);
  --color-tb12-surface: oklch(0.18 0.006 60);
  --color-tb12-line: oklch(0.28 0.008 60);
  --color-tb12-text: oklch(0.95 0.006 80);
  --color-tb12-muted: oklch(0.75 0.01 70);
  --color-tb12-danger: oklch(0.65 0.2 27);
  --color-tb12-danger-ink: oklch(0.15 0.05 27);
}

@media (forced-colors: active) {
  .tb-12 > span {
    border: 1px solid ButtonText;
  }

  .tb-12 button {
    background: Highlight;
    color: HighlightText;
  }
}
```
