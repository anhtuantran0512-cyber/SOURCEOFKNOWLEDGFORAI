---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/tailwind-modal-close-button-top-right/"
title: "Tailwind Modal Close Button (Top-Right Corner X)"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "The canonical dialog dismiss, rebuilt in utilities: a quiet 44px circle pinned with absolute top-3 end-3, its × drawn by two before:/after: bars — no icon…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Modal Close Button (Top-Right Corner X)
Source: https://codefronts.com/components/tailwind-css-close-buttons/tailwind-modal-close-button-top-right/

The canonical dialog dismiss, rebuilt in utilities: a quiet 44px circle pinned with absolute top-3 end-3, its × drawn by two before:/after: bars — no icon font, no SVG. Hover tints the circle with hover:bg-tcb01-acc/12 and stretches the bars with group-hover:before:scale-x-115; the dialog itself fades in with zero JS via starting:.
## HTML
```html
<section class="tcb-01 w-full min-h-svh grid place-items-center bg-tcb01-bg bg-[linear-gradient(160deg,var(--color-tcb01-bg),var(--color-tcb01-bg2))] px-6 py-12 font-tcb01-sans text-tcb01-ink" aria-label="Modal close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <div role="dialog" aria-labelledby="tcb-01-title" aria-describedby="tcb-01-text" class="relative w-full max-w-[25rem] rounded-[1.25rem] bg-white px-7 pt-8 pb-7 shadow-[0_30px_70px_-30px_var(--color-tcb01-shadow)] ring-1 ring-tcb01-ink/5 transition duration-500 ease-out starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
      <button type="button" aria-label="Close dialog" class="group absolute top-3 end-3 grid size-11 cursor-pointer place-items-center rounded-full transition-colors duration-200 hover:bg-tcb01-acc/12 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcb01-acc active:scale-94 motion-reduce:transition-none">
        <span aria-hidden="true" class="relative size-4 before:absolute before:top-1/2 before:left-1/2 before:h-0.5 before:w-4 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-tcb01-glyph before:transition before:duration-200 after:absolute after:top-1/2 after:left-1/2 after:h-0.5 after:w-4 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-tcb01-glyph after:transition after:duration-200 group-hover:before:scale-x-115 group-hover:before:bg-tcb01-acc group-hover:after:scale-x-115 group-hover:after:bg-tcb01-acc motion-reduce:before:transition-none motion-reduce:after:transition-none"></span>
      </button>
      <span aria-hidden="true" class="mb-5 grid size-11 place-items-center rounded-xl bg-tcb01-acc/10 text-tcb01-acc"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m4 7 8 6 8-6"/></svg></span>
      <h3 id="tcb-01-title" class="pe-10 text-xl font-semibold tracking-[-0.015em]">Confirm your email</h3>
      <p id="tcb-01-text" class="mt-2 text-[15px]/[1.6] text-tcb01-mut text-pretty">We sent a verification link to your inbox. Click it to activate your account.</p>
      <div class="mt-6 flex flex-wrap gap-2.5">
        <button type="button" class="min-h-11 flex-1 cursor-pointer rounded-xl bg-tcb01-acc px-4 text-sm font-semibold text-white transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcb01-acc active:scale-98">Open mail app</button>
        <button type="button" class="min-h-11 flex-1 cursor-pointer rounded-xl px-4 text-sm font-semibold text-tcb01-ink ring-1 ring-tcb01-ink/12 transition hover:bg-tcb01-ink/4 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcb01-acc active:scale-98">Resend link</button>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/60 px-3.5 py-2 font-tcb01-mono text-[11.5px] text-tcb01-mut ring-1 ring-tcb01-ink/10">before:rotate-45 · group-hover:before:scale-x-115 · starting:opacity-0</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb01-bg: #eef0fa;
  --color-tcb01-bg: oklch(0.95 0.015 265);
  --color-tcb01-bg2: #dcdcf5;
  --color-tcb01-bg2: oklch(0.9 0.03 280);
  --color-tcb01-ink: #282a3a;
  --color-tcb01-ink: oklch(0.27 0.025 270);
  --color-tcb01-mut: #5c5f70;
  --color-tcb01-mut: oklch(0.47 0.02 270);
  --color-tcb01-glyph: #545766;
  --color-tcb01-glyph: oklch(0.45 0.02 270);
  --color-tcb01-acc: #4b5ccf;
  --color-tcb01-acc: oklch(0.52 0.17 268);
  --color-tcb01-shadow: #3a347080;
  --color-tcb01-shadow: oklch(0.35 0.08 270 / 0.55);
  --font-tcb01-sans: 'Geist', system-ui, sans-serif;
  --font-tcb01-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-01 {
  width: 100%;
  min-height: 100svh;
}
```
