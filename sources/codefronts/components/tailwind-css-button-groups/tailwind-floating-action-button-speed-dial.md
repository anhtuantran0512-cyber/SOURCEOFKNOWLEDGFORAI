---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-floating-action-button-speed-dial/"
title: "Tailwind Floating Action Button with Radial Speed Dial Menu (No JS)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "A floating action button that fans four actions out along an arc."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Floating Action Button with Radial Speed Dial Menu (No JS)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-floating-action-button-speed-dial/

A floating action button that fans four actions out along an arc. A hidden checkbox holds open state; each satellite reads its own offset from inline --x/--y through v4's translate-x-(--x) shorthand, with staggered delay-* for a springy cascade. Closed satellites are now invisible, so they leave the tab order &mdash; the CSS original let keyboard users tab into four hidden buttons.
## HTML
```html
<section class="tbg-21 w-full min-h-svh grid place-items-center bg-tbg21-bg bg-[radial-gradient(120%_120%_at_70%_70%,var(--color-tbg21-glow),transparent_70%)] px-5 py-14 font-tbg21-sans text-tbg21-ink" aria-label="Floating action button speed dial demo">
  <div class="group/fab relative size-16" role="group" aria-label="Quick create">
    <span aria-hidden="true" class="pointer-events-none absolute top-1/2 left-1/2 size-56 -translate-1/2 scale-50 rounded-full border border-dashed border-tbg21-acc/30 opacity-0 transition-[scale,opacity] duration-500 group-has-checked/fab:scale-100 group-has-checked/fab:opacity-100 motion-reduce:transition-none"></span>
    <label aria-label="Quick create menu" class="absolute inset-0 z-3 grid cursor-pointer place-items-center rounded-full bg-tbg21-acc shadow-[0_12px_30px_-8px_var(--color-tbg21-acc)] transition-transform duration-300 hover:scale-105 active:scale-95 has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-white">
      <input type="checkbox" class="sr-only">
      <svg class="transition-transform duration-350 ease-[cubic-bezier(.34,1.4,.4,1)] group-has-checked/fab:rotate-135 motion-reduce:transition-none" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round" aria-hidden="true"><path d="M12 4v16M4 12h16"/></svg>
    </label>
    <button type="button" data-tip="New note" aria-label="New note" style="--x:0px;--y:-96px" class="invisible absolute top-[11px] left-[11px] z-2 grid size-[42px] scale-0 cursor-pointer place-items-center rounded-full bg-tbg21-sat text-tbg21-soft shadow-[0_8px_20px_-8px_#000] transition-[translate,scale,visibility,background-color] duration-400 ease-[cubic-bezier(.34,1.5,.5,1)] hover:bg-tbg21-acc hover:text-white group-has-checked/fab:visible group-has-checked/fab:translate-x-(--x) group-has-checked/fab:translate-y-(--y) group-has-checked/fab:scale-100 group-has-checked/fab:delay-[20ms] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white after:pointer-events-none after:absolute after:right-[calc(100%+10px)] after:rounded-md after:bg-tbg21-tip after:px-2 after:py-1 after:text-xs after:font-semibold after:whitespace-nowrap after:text-white after:opacity-0 after:transition-opacity after:content-[attr(data-tip)] hover:after:opacity-100 focus-visible:after:opacity-100 motion-reduce:transition-[visibility,scale] motion-reduce:duration-150"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h10l4 4v12H5zM15 4v4h4"/></svg></button>
    <button type="button" data-tip="New task" aria-label="New task" style="--x:-84px;--y:-48px" class="invisible absolute top-[11px] left-[11px] z-2 grid size-[42px] scale-0 cursor-pointer place-items-center rounded-full bg-tbg21-sat text-tbg21-soft shadow-[0_8px_20px_-8px_#000] transition-[translate,scale,visibility,background-color] duration-400 ease-[cubic-bezier(.34,1.5,.5,1)] hover:bg-tbg21-acc hover:text-white group-has-checked/fab:visible group-has-checked/fab:translate-x-(--x) group-has-checked/fab:translate-y-(--y) group-has-checked/fab:scale-100 group-has-checked/fab:delay-[70ms] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white after:pointer-events-none after:absolute after:right-[calc(100%+10px)] after:rounded-md after:bg-tbg21-tip after:px-2 after:py-1 after:text-xs after:font-semibold after:whitespace-nowrap after:text-white after:opacity-0 after:transition-opacity after:content-[attr(data-tip)] hover:after:opacity-100 focus-visible:after:opacity-100 motion-reduce:transition-[visibility,scale] motion-reduce:duration-150"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12l5 5L20 6"/></svg></button>
    <button type="button" data-tip="Upload file" aria-label="Upload file" style="--x:-96px;--y:44px" class="invisible absolute top-[11px] left-[11px] z-2 grid size-[42px] scale-0 cursor-pointer place-items-center rounded-full bg-tbg21-sat text-tbg21-soft shadow-[0_8px_20px_-8px_#000] transition-[translate,scale,visibility,background-color] duration-400 ease-[cubic-bezier(.34,1.5,.5,1)] hover:bg-tbg21-acc hover:text-white group-has-checked/fab:visible group-has-checked/fab:translate-x-(--x) group-has-checked/fab:translate-y-(--y) group-has-checked/fab:scale-100 group-has-checked/fab:delay-[120ms] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white after:pointer-events-none after:absolute after:right-[calc(100%+10px)] after:rounded-md after:bg-tbg21-tip after:px-2 after:py-1 after:text-xs after:font-semibold after:whitespace-nowrap after:text-white after:opacity-0 after:transition-opacity after:content-[attr(data-tip)] hover:after:opacity-100 focus-visible:after:opacity-100 motion-reduce:transition-[visibility,scale] motion-reduce:duration-150"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 16V5M7 10l5-5 5 5M5 19h14"/></svg></button>
    <button type="button" data-tip="Invite people" aria-label="Invite people" style="--x:-40px;--y:88px" class="invisible absolute top-[11px] left-[11px] z-2 grid size-[42px] scale-0 cursor-pointer place-items-center rounded-full bg-tbg21-sat text-tbg21-soft shadow-[0_8px_20px_-8px_#000] transition-[translate,scale,visibility,background-color] duration-400 ease-[cubic-bezier(.34,1.5,.5,1)] hover:bg-tbg21-acc hover:text-white group-has-checked/fab:visible group-has-checked/fab:translate-x-(--x) group-has-checked/fab:translate-y-(--y) group-has-checked/fab:scale-100 group-has-checked/fab:delay-[170ms] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white after:pointer-events-none after:absolute after:right-[calc(100%+10px)] after:rounded-md after:bg-tbg21-tip after:px-2 after:py-1 after:text-xs after:font-semibold after:whitespace-nowrap after:text-white after:opacity-0 after:transition-opacity after:content-[attr(data-tip)] hover:after:opacity-100 focus-visible:after:opacity-100 motion-reduce:transition-[visibility,scale] motion-reduce:duration-150"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="9" cy="8" r="3.2"/><path d="M3.5 20a5.5 5.5 0 0 1 11 0M17 8v6M14 11h6"/></svg></button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg21-bg: #0c0716;
  --color-tbg21-glow: #241439;
  --color-tbg21-sat: #2c2148;
  --color-tbg21-tip: #1a1230;
  --color-tbg21-ink: #f1e9ff;
  --color-tbg21-soft: #e6d8ff;
  --color-tbg21-acc: #8c3ff0;
  --color-tbg21-acc: oklch(0.58 0.24 300);
  --font-tbg21-sans: 'Figtree', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-21 {
  width: 100%;
  min-height: 100svh;
}
```
