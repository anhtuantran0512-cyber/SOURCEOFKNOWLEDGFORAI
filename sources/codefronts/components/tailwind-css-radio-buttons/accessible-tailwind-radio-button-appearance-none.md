---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/accessible-tailwind-radio-button-appearance-none/"
title: "Accessible Tailwind Radio Button (appearance-none)"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "The reference implementation every custom radio should start from: style the native <input type=\"radio\"> itself with appearance-none."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Tailwind Radio Button (appearance-none)
Source: https://codefronts.com/components/tailwind-css-radio-buttons/accessible-tailwind-radio-button-appearance-none/

The reference implementation every custom radio should start from: style the native <input type="radio"> itself with appearance-none. No hidden input, no wrapper spans, no ARIA — checked:, disabled: and focus-visible: sit directly on the element that owns those states, and forced-colors:appearance-auto hands the control back to Windows High Contrast.
## HTML
```html
<section class="trb-05 w-full min-h-svh grid place-items-center bg-trb05-bg px-6 py-14 font-trb05-sans text-trb05-ink" aria-label="Accessible Tailwind radio buttons demo">
  <fieldset class="w-full max-w-[24rem] rounded-2xl border border-trb05-line bg-white p-6 shadow-trb05-card">
    <legend class="sr-only">How did you hear about us?</legend>
    <p aria-hidden="true" class="text-xl font-bold tracking-[-0.02em]">How did you hear about us?</p>
    <div class="mt-3 grid">
      <label class="flex min-h-12 cursor-pointer items-center gap-3 rounded-[10px] px-2 transition-colors hover:bg-trb05-hover"><input type="radio" name="trb-05" value="search" checked class="grid size-[22px] flex-none cursor-pointer appearance-none place-items-center rounded-full border-2 border-trb05-ring bg-white transition-colors before:size-[11px] before:scale-0 before:rounded-full before:bg-trb05-acc before:transition-transform before:duration-250 before:ease-trb05-spring before:content-[''] checked:border-trb05-acc checked:before:scale-100 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-trb05-acc motion-reduce:before:transition-none forced-colors:appearance-auto"><span class="text-[15.5px]">Search engine</span></label>
      <label class="flex min-h-12 cursor-pointer items-center gap-3 rounded-[10px] px-2 transition-colors hover:bg-trb05-hover"><input type="radio" name="trb-05" value="social" class="grid size-[22px] flex-none cursor-pointer appearance-none place-items-center rounded-full border-2 border-trb05-ring bg-white transition-colors before:size-[11px] before:scale-0 before:rounded-full before:bg-trb05-acc before:transition-transform before:duration-250 before:ease-trb05-spring before:content-[''] checked:border-trb05-acc checked:before:scale-100 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-trb05-acc motion-reduce:before:transition-none forced-colors:appearance-auto"><span class="text-[15.5px]">Social media</span></label>
      <label class="flex min-h-12 cursor-pointer items-center gap-3 rounded-[10px] px-2 transition-colors hover:bg-trb05-hover"><input type="radio" name="trb-05" value="friend" class="grid size-[22px] flex-none cursor-pointer appearance-none place-items-center rounded-full border-2 border-trb05-ring bg-white transition-colors before:size-[11px] before:scale-0 before:rounded-full before:bg-trb05-acc before:transition-transform before:duration-250 before:ease-trb05-spring before:content-[''] checked:border-trb05-acc checked:before:scale-100 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-trb05-acc motion-reduce:before:transition-none forced-colors:appearance-auto"><span class="text-[15.5px]">Friend or colleague</span></label>
      <label class="flex min-h-12 cursor-pointer items-center gap-3 rounded-[10px] px-2 transition-colors hover:bg-trb05-hover has-disabled:cursor-not-allowed has-disabled:text-trb05-off has-disabled:hover:bg-transparent"><input type="radio" name="trb-05" value="event" disabled aria-describedby="trb-05-note" class="grid size-[22px] flex-none cursor-pointer appearance-none place-items-center rounded-full border-2 border-trb05-ring bg-white transition-colors before:size-[11px] before:scale-0 before:rounded-full before:bg-trb05-acc before:content-[''] disabled:cursor-not-allowed disabled:border-trb05-line disabled:bg-trb05-hover forced-colors:appearance-auto"><span class="text-[15.5px]">Event</span><em id="trb-05-note" class="ml-auto rounded-full bg-trb05-hover px-2.5 py-1 text-xs font-medium not-italic text-trb05-mut">Unavailable</em></label>
    </div>
    <p class="mt-4 border-t border-trb05-line pt-4 text-[13px] text-trb05-mut">Use <kbd class="rounded border border-trb05-line px-1.5 py-0.5 text-xs font-medium">↑</kbd> <kbd class="rounded border border-trb05-line px-1.5 py-0.5 text-xs font-medium">↓</kbd> to move between options.</p>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb05-bg: #f4f4f7;
  --color-trb05-bg: oklch(0.965 0.004 285);
  --color-trb05-ink: #20242f;
  --color-trb05-ink: oklch(0.25 0.02 270);
  --color-trb05-mut: #5e6475;
  --color-trb05-mut: oklch(0.5 0.02 270);
  --color-trb05-off: #767c8e;
  --color-trb05-off: oklch(0.58 0.02 270);
  --color-trb05-line: #e4e6ec;
  --color-trb05-line: oklch(0.925 0.008 270);
  --color-trb05-hover: #f1f2f6;
  --color-trb05-hover: oklch(0.96 0.005 270);
  --color-trb05-ring: #a9afc0;
  --color-trb05-ring: oklch(0.76 0.02 270);
  --color-trb05-acc: #2860d8;
  --color-trb05-acc: oklch(0.52 0.18 260);
  --shadow-trb05-card: 0 1px 2px oklch(0.2 0.02 270 / 0.05), 0 12px 32px -16px oklch(0.2 0.02 270 / 0.18);
  --ease-trb05-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --font-trb05-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-05 {
  width: 100%;
  min-height: 100svh;
}
```
