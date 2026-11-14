---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-3d-vertical-button-group-hover/"
title: "Tailwind 3D Vertical Button Group with Hover Depth (Perspective Stack)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "A vertical navigation stack tilted into 3D, where the hovered (or keyboard-focused) card lifts toward you while its siblings sink back and dim."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Vertical Button Group with Hover Depth (Perspective Stack)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-3d-vertical-button-group-hover/

A vertical navigation stack tilted into 3D, where the hovered (or keyboard-focused) card lifts toward you while its siblings sink back and dim. It's a showcase for v4's native 3D utilities &mdash; perspective-[760px], transform-3d, rotate-x-34, translate-z-[70px] &mdash; combined with group-has-[button:hover]/stack:not-hover:, which targets &ldquo;every card except the one under the pointer&rdquo; in one variant.
## HTML
```html
<section class="tbg-20 w-full min-h-svh grid place-items-center bg-tbg20-bg bg-linear-165 from-tbg20-bg to-tbg20-bg2 px-5 py-14 font-tbg20-sans text-tbg20-ink" aria-label="3D hover depth vertical button group demo">
  <nav aria-label="Workspace" class="perspective-[760px] perspective-origin-[50%_42%]">
    <div class="group/stack flex w-[min(21rem,86vw)] flex-col gap-4.5 transform-3d rotate-x-34 -rotate-z-1 motion-reduce:transform-none">
      <button type="button" aria-current="page" style="--c:#ff8a4c" class="flex cursor-pointer items-center gap-4 rounded-2xl border-l-4 border-(--c) bg-linear-to-b from-tbg20-card to-tbg20-card2 px-5.5 py-4.5 text-left shadow-tbg20-card transform-3d transition-[translate,rotate,opacity,filter,box-shadow] duration-400 ease-[cubic-bezier(.34,1.4,.4,1)] hover:translate-z-[70px] hover:-rotate-x-14 hover:shadow-[0_40px_60px_-24px_rgb(0_0_0/0.9),0_0_0_1px_var(--c)] focus-visible:translate-z-[70px] focus-visible:-rotate-x-14 focus-visible:shadow-[0_40px_60px_-24px_rgb(0_0_0/0.9),0_0_0_3px_var(--c)] focus-visible:outline-none group-has-[button:hover]/stack:not-hover:-translate-z-[55px] group-has-[button:hover]/stack:not-hover:opacity-50 group-has-[button:hover]/stack:not-hover:brightness-75 group-has-[button:focus-visible]/stack:not-focus-visible:-translate-z-[55px] group-has-[button:focus-visible]/stack:not-focus-visible:opacity-50 motion-reduce:transform-none! motion-reduce:transition-opacity">
        <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-xl bg-(--c)/15 text-(--c)"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"><rect x="4" y="4" width="7" height="9" rx="1.5"/><rect x="13" y="4" width="7" height="5" rx="1.5"/><rect x="13" y="11" width="7" height="9" rx="1.5"/><rect x="4" y="15" width="7" height="5" rx="1.5"/></svg></span>
        <span class="grid gap-0.5"><span class="text-[17px] font-extrabold tracking-[-0.01em]">Dashboard</span><span class="text-[13px] text-tbg20-mut">Overview &amp; metrics</span></span>
        <span class="ml-auto rounded-full bg-(--c)/15 px-2 py-0.5 text-[11px] font-bold text-(--c)">Current</span>
      </button>
      <button type="button" style="--c:#ffd24c" class="flex cursor-pointer items-center gap-4 rounded-2xl border-l-4 border-(--c) bg-linear-to-b from-tbg20-card to-tbg20-card2 px-5.5 py-4.5 text-left shadow-tbg20-card transform-3d transition-[translate,rotate,opacity,filter,box-shadow] duration-400 ease-[cubic-bezier(.34,1.4,.4,1)] hover:translate-z-[70px] hover:-rotate-x-14 hover:shadow-[0_40px_60px_-24px_rgb(0_0_0/0.9),0_0_0_1px_var(--c)] focus-visible:translate-z-[70px] focus-visible:-rotate-x-14 focus-visible:shadow-[0_40px_60px_-24px_rgb(0_0_0/0.9),0_0_0_3px_var(--c)] focus-visible:outline-none group-has-[button:hover]/stack:not-hover:-translate-z-[55px] group-has-[button:hover]/stack:not-hover:opacity-50 group-has-[button:hover]/stack:not-hover:brightness-75 group-has-[button:focus-visible]/stack:not-focus-visible:-translate-z-[55px] group-has-[button:focus-visible]/stack:not-focus-visible:opacity-50 motion-reduce:transform-none! motion-reduce:transition-opacity">
        <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-xl bg-(--c)/15 text-(--c)"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg></span>
        <span class="grid gap-0.5"><span class="text-[17px] font-extrabold tracking-[-0.01em]">Projects</span><span class="text-[13px] text-tbg20-mut">12 active</span></span>
      </button>
      <button type="button" style="--c:#6ee7a8" class="flex cursor-pointer items-center gap-4 rounded-2xl border-l-4 border-(--c) bg-linear-to-b from-tbg20-card to-tbg20-card2 px-5.5 py-4.5 text-left shadow-tbg20-card transform-3d transition-[translate,rotate,opacity,filter,box-shadow] duration-400 ease-[cubic-bezier(.34,1.4,.4,1)] hover:translate-z-[70px] hover:-rotate-x-14 hover:shadow-[0_40px_60px_-24px_rgb(0_0_0/0.9),0_0_0_1px_var(--c)] focus-visible:translate-z-[70px] focus-visible:-rotate-x-14 focus-visible:shadow-[0_40px_60px_-24px_rgb(0_0_0/0.9),0_0_0_3px_var(--c)] focus-visible:outline-none group-has-[button:hover]/stack:not-hover:-translate-z-[55px] group-has-[button:hover]/stack:not-hover:opacity-50 group-has-[button:hover]/stack:not-hover:brightness-75 group-has-[button:focus-visible]/stack:not-focus-visible:-translate-z-[55px] group-has-[button:focus-visible]/stack:not-focus-visible:opacity-50 motion-reduce:transform-none! motion-reduce:transition-opacity">
        <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-xl bg-(--c)/15 text-(--c)"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="9" cy="8" r="3.2"/><path d="M3.5 20a5.5 5.5 0 0 1 11 0M16 5.5a3 3 0 0 1 0 5.5M18 20a5 5 0 0 0-2.5-4.3"/></svg></span>
        <span class="grid gap-0.5"><span class="text-[17px] font-extrabold tracking-[-0.01em]">Team</span><span class="text-[13px] text-tbg20-mut">8 members</span></span>
      </button>
      <button type="button" style="--c:#5cc8ff" class="flex cursor-pointer items-center gap-4 rounded-2xl border-l-4 border-(--c) bg-linear-to-b from-tbg20-card to-tbg20-card2 px-5.5 py-4.5 text-left shadow-tbg20-card transform-3d transition-[translate,rotate,opacity,filter,box-shadow] duration-400 ease-[cubic-bezier(.34,1.4,.4,1)] hover:translate-z-[70px] hover:-rotate-x-14 hover:shadow-[0_40px_60px_-24px_rgb(0_0_0/0.9),0_0_0_1px_var(--c)] focus-visible:translate-z-[70px] focus-visible:-rotate-x-14 focus-visible:shadow-[0_40px_60px_-24px_rgb(0_0_0/0.9),0_0_0_3px_var(--c)] focus-visible:outline-none group-has-[button:hover]/stack:not-hover:-translate-z-[55px] group-has-[button:hover]/stack:not-hover:opacity-50 group-has-[button:hover]/stack:not-hover:brightness-75 group-has-[button:focus-visible]/stack:not-focus-visible:-translate-z-[55px] group-has-[button:focus-visible]/stack:not-focus-visible:opacity-50 motion-reduce:transform-none! motion-reduce:transition-opacity">
        <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-xl bg-(--c)/15 text-(--c)"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M5.6 18.4l2.1-2.1M16.3 7.7l2.1-2.1"/></svg></span>
        <span class="grid gap-0.5"><span class="text-[17px] font-extrabold tracking-[-0.01em]">Settings</span><span class="text-[13px] text-tbg20-mut">Workspace config</span></span>
      </button>
    </div>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg20-bg: #2a1c14;
  --color-tbg20-bg2: #160f0a;
  --color-tbg20-card: #35291e;
  --color-tbg20-card2: #241a12;
  --color-tbg20-ink: #f6eadb;
  --color-tbg20-mut: #c4ab93;
  --color-tbg20-mut: oklch(0.76 0.05 65);
  --shadow-tbg20-card: 0 16px 30px -14px rgb(0 0 0 / 0.85), inset 0 1px 0 rgb(255 255 255 / 0.08);
  --font-tbg20-sans: 'Schibsted Grotesk', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-20 {
  width: 100%;
  min-height: 100svh;
}
```
