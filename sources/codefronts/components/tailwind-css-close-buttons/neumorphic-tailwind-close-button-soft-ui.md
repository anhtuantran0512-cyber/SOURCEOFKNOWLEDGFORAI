---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/neumorphic-tailwind-close-button-soft-ui/"
title: "Neumorphic Tailwind Close Button (Soft UI)"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "Soft UI done responsibly: two opposing shadows — a light one up-left, a dark one down-right — extrude the button from the surface; active: swaps them for…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Tailwind Close Button (Soft UI)
Source: https://codefronts.com/components/tailwind-css-close-buttons/neumorphic-tailwind-close-button-soft-ui/

Soft UI done responsibly: two opposing shadows — a light one up-left, a dark one down-right — extrude the button from the surface; active: swaps them for inset copies so it physically sinks with zero layout shift. The port adds what neumorphism usually forgets: a 3:1 hairline edge, a solid focus ring, and a glyph that turns accent on press so state is not signalled by shadow alone.
## HTML
```html
<section class="tcb-07 w-full min-h-svh grid place-items-center bg-tcb07-surface px-6 py-12 font-tcb07-sans text-tcb07-ink" aria-label="Neumorphic close button demo">
  <div class="grid w-full justify-items-center gap-8">
    <div class="flex w-full max-w-[20rem] items-center justify-between gap-4 rounded-[1.75rem] bg-tcb07-surface px-6 py-5 shadow-[-10px_-10px_24px_var(--color-tcb07-lite),10px_10px_24px_var(--color-tcb07-dark)]">
      <div>
        <div class="text-[15px] font-semibold">Focus mode</div>
        <div class="mt-0.5 text-[13px] text-tcb07-mut">Notifications paused</div>
      </div>
      <button type="button" aria-label="Close focus mode" class="group relative size-14 flex-none cursor-pointer rounded-full bg-tcb07-surface shadow-[-6px_-6px_14px_var(--color-tcb07-lite),6px_6px_14px_var(--color-tcb07-dark)] ring-1 ring-tcb07-ink/12 transition-shadow duration-100 hover:shadow-[-8px_-8px_18px_var(--color-tcb07-lite),8px_8px_18px_var(--color-tcb07-dark)] focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcb07-acc active:shadow-[inset_-5px_-5px_12px_var(--color-tcb07-lite),inset_5px_5px_12px_var(--color-tcb07-dark)] motion-reduce:transition-none">
        <span aria-hidden="true" class="absolute inset-0 before:absolute before:top-1/2 before:left-1/2 before:h-[2.5px] before:w-5 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-tcb07-ink before:transition-colors after:absolute after:top-1/2 after:left-1/2 after:h-[2.5px] after:w-5 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-tcb07-ink after:transition-colors group-active:before:bg-tcb07-acc group-active:after:bg-tcb07-acc"></span>
      </button>
    </div>
    <p class="text-xs font-medium tracking-[0.05em] text-tcb07-mut">Press and hold the ×</p>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tcb07-mono text-[11.5px] text-tcb07-mut shadow-[inset_-3px_-3px_6px_var(--color-tcb07-lite),inset_3px_3px_6px_var(--color-tcb07-dark)]">shadow-[…lite,…dark] · active:shadow-[inset_…]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb07-surface: #dde1ea;
  --color-tcb07-surface: oklch(0.9 0.015 260);
  --color-tcb07-lite: #f5f6f9;
  --color-tcb07-lite: oklch(0.97 0.005 260);
  --color-tcb07-dark: #b8bcc6;
  --color-tcb07-dark: oklch(0.79 0.015 260);
  --color-tcb07-ink: #474d63;
  --color-tcb07-ink: oklch(0.42 0.04 265);
  --color-tcb07-mut: #525870;
  --color-tcb07-mut: oklch(0.45 0.035 265);
  --color-tcb07-acc: #3d4fcf;
  --color-tcb07-acc: oklch(0.5 0.18 265);
  --font-tcb07-sans: 'Geist', system-ui, sans-serif;
  --font-tcb07-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-07 {
  width: 100%;
  min-height: 100svh;
}
```
