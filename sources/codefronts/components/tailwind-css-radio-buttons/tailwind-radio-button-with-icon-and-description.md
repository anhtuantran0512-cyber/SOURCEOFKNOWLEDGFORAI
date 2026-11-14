---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-radio-button-with-icon-and-description/"
title: "Tailwind Radio Button with Icon and Description"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "The settings-page staple: a vertical option list where every row carries an icon tile, a title, a one-line description and a custom radio on the right."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Radio Button with Icon and Description
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-radio-button-with-icon-and-description/

The settings-page staple: a vertical option list where every row carries an icon tile, a title, a one-line description and a custom radio on the right. Three grid columns, one has-checked: on the row, and group-has-checked: on everything that responds — tint, tile, icon and dot.
## HTML
```html
<section class="trb-03 w-full min-h-svh grid place-items-center bg-trb03-bg px-6 py-14 font-trb03-sans text-trb03-ink" aria-label="Radio options with icon and description demo">
  <fieldset class="w-full max-w-[29rem]">
    <legend class="text-2xl font-extrabold tracking-[-0.02em]">Notifications</legend>
    <p class="mt-1 text-sm text-trb03-mut">Choose what reaches your inbox.</p>
    <div class="mt-5 grid gap-2.5">
      <label class="group relative grid cursor-pointer grid-cols-[auto_1fr_auto] items-center gap-3.5 rounded-2xl border-[1.5px] border-trb03-line bg-white p-4 transition duration-250 hover:border-trb03-acc/35 has-checked:border-trb03-acc has-checked:bg-trb03-acc/5 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-trb03-acc motion-reduce:transition-none">
        <input type="radio" name="trb-03" value="all" class="sr-only" checked>
        <span aria-hidden="true" class="grid size-[42px] place-items-center rounded-[11px] bg-trb03-tile text-trb03-icon transition duration-250 *:size-[22px] group-has-checked:bg-trb03-acc/14 group-has-checked:text-trb03-acc motion-safe:group-has-checked:*:scale-110 *:transition-transform"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9a6 6 0 0 1 12 0c0 5 2 6 2 6H4s2-1 2-6"/><path d="M10 19a2 2 0 0 0 4 0"/></svg></span>
        <span class="grid gap-0.5"><span class="text-[15px] font-bold">All activity</span><span class="text-[13px] leading-[1.45] text-trb03-mut">Every comment, mention and follow — delivered instantly.</span></span>
        <span aria-hidden="true" class="grid size-[22px] place-items-center rounded-full border-2 border-trb03-ring transition after:size-[9px] after:scale-0 after:rounded-full after:bg-white after:transition-transform after:duration-300 after:ease-trb03-spring after:content-[''] group-has-checked:border-trb03-acc group-has-checked:bg-trb03-acc group-has-checked:after:scale-100"></span>
      </label>
      <label class="group relative grid cursor-pointer grid-cols-[auto_1fr_auto] items-center gap-3.5 rounded-2xl border-[1.5px] border-trb03-line bg-white p-4 transition duration-250 hover:border-trb03-acc/35 has-checked:border-trb03-acc has-checked:bg-trb03-acc/5 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-trb03-acc motion-reduce:transition-none">
        <input type="radio" name="trb-03" value="mentions" class="sr-only">
        <span aria-hidden="true" class="grid size-[42px] place-items-center rounded-[11px] bg-trb03-tile text-trb03-icon transition duration-250 *:size-[22px] group-has-checked:bg-trb03-acc/14 group-has-checked:text-trb03-acc motion-safe:group-has-checked:*:scale-110 *:transition-transform"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M16 8v5a3 3 0 0 0 6 0v-1a10 10 0 1 0-4 8"/></svg></span>
        <span class="grid gap-0.5"><span class="text-[15px] font-bold">Mentions only</span><span class="text-[13px] leading-[1.45] text-trb03-mut">Stay focused — only direct @mentions get through.</span></span>
        <span aria-hidden="true" class="grid size-[22px] place-items-center rounded-full border-2 border-trb03-ring transition after:size-[9px] after:scale-0 after:rounded-full after:bg-white after:transition-transform after:duration-300 after:ease-trb03-spring after:content-[''] group-has-checked:border-trb03-acc group-has-checked:bg-trb03-acc group-has-checked:after:scale-100"></span>
      </label>
      <label class="group relative grid cursor-pointer grid-cols-[auto_1fr_auto] items-center gap-3.5 rounded-2xl border-[1.5px] border-trb03-line bg-white p-4 transition duration-250 hover:border-trb03-acc/35 has-checked:border-trb03-acc has-checked:bg-trb03-acc/5 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-trb03-acc motion-reduce:transition-none">
        <input type="radio" name="trb-03" value="muted" class="sr-only">
        <span aria-hidden="true" class="grid size-[42px] place-items-center rounded-[11px] bg-trb03-tile text-trb03-icon transition duration-250 *:size-[22px] group-has-checked:bg-trb03-acc/14 group-has-checked:text-trb03-acc motion-safe:group-has-checked:*:scale-110 *:transition-transform"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5a3 3 0 0 1 6 0c3 1 3 4 3 6 0 2 1 4 1 4H5s1-2 1-4c0-2 0-5 3-6Z" opacity=".35"/><path d="m4 4 16 16"/></svg></span>
        <span class="grid gap-0.5"><span class="text-[15px] font-bold">Muted</span><span class="text-[13px] leading-[1.45] text-trb03-mut">Nothing until you turn notifications back on.</span></span>
        <span aria-hidden="true" class="grid size-[22px] place-items-center rounded-full border-2 border-trb03-ring transition after:size-[9px] after:scale-0 after:rounded-full after:bg-white after:transition-transform after:duration-300 after:ease-trb03-spring after:content-[''] group-has-checked:border-trb03-acc group-has-checked:bg-trb03-acc group-has-checked:after:scale-100"></span>
      </label>
    </div>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb03-bg: #f5f5f9;
  --color-trb03-bg: oklch(0.97 0.006 285);
  --color-trb03-ink: #1d2233;
  --color-trb03-ink: oklch(0.24 0.03 275);
  --color-trb03-mut: #5f6579;
  --color-trb03-mut: oklch(0.5 0.025 275);
  --color-trb03-line: #e5e7f0;
  --color-trb03-line: oklch(0.93 0.01 275);
  --color-trb03-ring: #c7cddd;
  --color-trb03-ring: oklch(0.85 0.02 270);
  --color-trb03-tile: #eef0f6;
  --color-trb03-tile: oklch(0.955 0.008 275);
  --color-trb03-icon: #737b96;
  --color-trb03-icon: oklch(0.58 0.035 275);
  --color-trb03-acc: #7447e0;
  --color-trb03-acc: oklch(0.55 0.21 290);
  --ease-trb03-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --font-trb03-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-03 {
  width: 100%;
  min-height: 100svh;
}
```
