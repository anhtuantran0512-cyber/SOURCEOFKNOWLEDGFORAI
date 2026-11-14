---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/accessible-custom-checkbox-tailwind-focus-ring/"
title: "Accessible Custom Checkbox in Tailwind CSS — WCAG Focus Ring"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "The reference implementation for keyboard users: a double focus ring (white gap + 3px blue) that only appears for keyboard focus via peer-focus-visible:, a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Custom Checkbox in Tailwind CSS — WCAG Focus Ring
Source: https://codefronts.com/components/tailwind-css-checkboxes/accessible-custom-checkbox-tailwind-focus-ring/

The reference implementation for keyboard users: a double focus ring (white gap + 3px blue) that only appears for keyboard focus via peer-focus-visible:, a disabled row that stays legible instead of fading to 50% opacity, and a described-by hint so screen readers explain why it's disabled.
## HTML
```html
<section class="tcb-06 w-full min-h-svh grid place-items-center bg-tcb06-bg px-5 py-14 font-tcb06-sans text-tcb06-ink selection:bg-tcb06-ring selection:text-white" aria-label="Accessible checkbox group">
  <fieldset class="w-full max-w-[26rem] rounded-2xl border border-tcb06-line bg-white px-5 pb-4 pt-3">
    <legend class="px-1 text-xs font-bold uppercase tracking-[0.12em] text-tcb06-mut">Notification preferences</legend>
    <label class="group flex min-h-11 cursor-pointer items-center gap-3.5 text-[15px]"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="grid size-[22px] flex-none place-items-center rounded-md border-2 border-tcb06-box bg-white text-white transition-colors duration-150 group-hover:border-tcb06-acc peer-checked:border-tcb06-acc peer-checked:bg-tcb06-acc peer-focus-visible:ring-3 peer-focus-visible:ring-tcb06-ring peer-focus-visible:ring-offset-2 peer-focus-visible:ring-offset-white motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 scale-50 opacity-0 transition duration-150 ease-[cubic-bezier(.2,.9,.3,1.2)] group-has-checked:scale-100 group-has-checked:opacity-100 motion-reduce:transition-none"><path d="M20 6 9 17l-5-5"/></svg></span>Enable desktop alerts</label>
    <label class="group flex min-h-11 cursor-pointer items-center gap-3.5 text-[15px]"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-[22px] flex-none place-items-center rounded-md border-2 border-tcb06-box bg-white text-white transition-colors duration-150 group-hover:border-tcb06-acc peer-checked:border-tcb06-acc peer-checked:bg-tcb06-acc peer-focus-visible:ring-3 peer-focus-visible:ring-tcb06-ring peer-focus-visible:ring-offset-2 peer-focus-visible:ring-offset-white motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 scale-50 opacity-0 transition duration-150 ease-[cubic-bezier(.2,.9,.3,1.2)] group-has-checked:scale-100 group-has-checked:opacity-100 motion-reduce:transition-none"><path d="M20 6 9 17l-5-5"/></svg></span>Play a sound on mention</label>
    <label class="group flex min-h-11 cursor-pointer items-center gap-3.5 text-[15px]"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="grid size-[22px] flex-none place-items-center rounded-md border-2 border-tcb06-box bg-white text-white transition-colors duration-150 group-hover:border-tcb06-acc peer-checked:border-tcb06-acc peer-checked:bg-tcb06-acc peer-focus-visible:ring-3 peer-focus-visible:ring-tcb06-ring peer-focus-visible:ring-offset-2 peer-focus-visible:ring-offset-white motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 scale-50 opacity-0 transition duration-150 ease-[cubic-bezier(.2,.9,.3,1.2)] group-has-checked:scale-100 group-has-checked:opacity-100 motion-reduce:transition-none"><path d="M20 6 9 17l-5-5"/></svg></span>Weekly summary email</label>
    <label class="group flex min-h-11 cursor-not-allowed items-center gap-3.5 text-[15px] text-tcb06-dis"><input type="checkbox" class="peer sr-only" disabled aria-describedby="tcb06-hint"><span aria-hidden="true" class="size-[22px] flex-none rounded-md border-2 border-dashed border-tcb06-disline bg-tcb06-disbg"></span><span>SMS alerts <span id="tcb06-hint" class="text-[13px]">— upgrade to Pro to enable</span></span></label>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb06-bg: #fbfbfc;
  --color-tcb06-bg: oklch(0.988 0.002 265);
  --color-tcb06-ink: #2a2f3a;
  --color-tcb06-ink: oklch(0.3 0.02 265);
  --color-tcb06-mut: #636a76;
  --color-tcb06-mut: oklch(0.51 0.02 265);
  --color-tcb06-line: #e6e7ea;
  --color-tcb06-line: oklch(0.925 0.005 265);
  --color-tcb06-box: #8f96a3;
  --color-tcb06-box: oklch(0.67 0.02 265);
  --color-tcb06-acc: #2b303b;
  --color-tcb06-acc: oklch(0.3 0.02 262);
  --color-tcb06-ring: #2f7de1;
  --color-tcb06-ring: oklch(0.6 0.17 255);
  --color-tcb06-dis: #6b7280;
  --color-tcb06-dis: oklch(0.55 0.02 265);
  --color-tcb06-disline: #c9ccd3;
  --color-tcb06-disline: oklch(0.84 0.01 265);
  --color-tcb06-disbg: #f3f4f6;
  --color-tcb06-disbg: oklch(0.967 0.003 265);
  --font-tcb06-sans: 'Instrument Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-06 {
  width: 100%;
  min-height: 100svh;
}
```
