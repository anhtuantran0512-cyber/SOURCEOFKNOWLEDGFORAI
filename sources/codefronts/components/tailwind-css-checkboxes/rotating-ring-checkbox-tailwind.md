---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/rotating-ring-checkbox-tailwind/"
title: "Rotating Ring Checkbox in Tailwind CSS — Spin-to-Check"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "A circular checkbox whose ring spins a full turn as the tick twists into place."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rotating Ring Checkbox in Tailwind CSS — Spin-to-Check
Source: https://codefronts.com/components/tailwind-css-checkboxes/rotating-ring-checkbox-tailwind/

A circular checkbox whose ring spins a full turn as the tick twists into place. The port fixes a quiet bug: the original rotated a uniform ring, which looks identical at every angle — here the ring has a lighter arc (border-t-tcb14-acc/25), so the group-has-checked:rotate-360 is actually visible.
## HTML
```html
<section class="tcb-14 w-full min-h-svh grid place-items-center bg-tcb14-bg px-5 py-14 font-tcb14-sans text-tcb14-ink selection:bg-tcb14-acc selection:text-white" aria-label="Rotating ring checkboxes">
  <div class="w-full max-w-[25rem] rounded-2xl border border-tcb14-line bg-white px-4 py-2.5">
    <label class="group flex min-h-14 cursor-pointer items-center gap-4 px-2"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="relative grid size-[30px] flex-none place-items-center rounded-full bg-tcb14-chip text-tcb14-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb14-acc"><span class="absolute inset-0 rounded-full border-[2.5px] border-tcb14-box border-t-tcb14-box/35 transition-[rotate,border-color] duration-500 ease-[cubic-bezier(.3,1.3,.4,1)] group-has-checked:rotate-360 group-has-checked:border-tcb14-acc group-has-checked:border-t-tcb14-acc/25 motion-reduce:rotate-0 motion-reduce:transition-colors"></span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-4 -rotate-40 scale-0 opacity-0 transition-[opacity,scale,rotate] delay-120 duration-350 ease-[cubic-bezier(.2,1.3,.4,1)] group-has-checked:rotate-0 group-has-checked:scale-100 group-has-checked:opacity-100 motion-reduce:rotate-0 motion-reduce:scale-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px]">Lock workspace</span></label>
    <label class="group flex min-h-14 cursor-pointer items-center gap-4 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="relative grid size-[30px] flex-none place-items-center rounded-full bg-tcb14-chip text-tcb14-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb14-acc"><span class="absolute inset-0 rounded-full border-[2.5px] border-tcb14-box border-t-tcb14-box/35 transition-[rotate,border-color] duration-500 ease-[cubic-bezier(.3,1.3,.4,1)] group-has-checked:rotate-360 group-has-checked:border-tcb14-acc group-has-checked:border-t-tcb14-acc/25 motion-reduce:rotate-0 motion-reduce:transition-colors"></span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-4 -rotate-40 scale-0 opacity-0 transition-[opacity,scale,rotate] delay-120 duration-350 ease-[cubic-bezier(.2,1.3,.4,1)] group-has-checked:rotate-0 group-has-checked:scale-100 group-has-checked:opacity-100 motion-reduce:rotate-0 motion-reduce:scale-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px]">Require passphrase</span></label>
    <label class="group flex min-h-14 cursor-pointer items-center gap-4 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="relative grid size-[30px] flex-none place-items-center rounded-full bg-tcb14-chip text-tcb14-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb14-acc"><span class="absolute inset-0 rounded-full border-[2.5px] border-tcb14-box border-t-tcb14-box/35 transition-[rotate,border-color] duration-500 ease-[cubic-bezier(.3,1.3,.4,1)] group-has-checked:rotate-360 group-has-checked:border-tcb14-acc group-has-checked:border-t-tcb14-acc/25 motion-reduce:rotate-0 motion-reduce:transition-colors"></span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-4 -rotate-40 scale-0 opacity-0 transition-[opacity,scale,rotate] delay-120 duration-350 ease-[cubic-bezier(.2,1.3,.4,1)] group-has-checked:rotate-0 group-has-checked:scale-100 group-has-checked:opacity-100 motion-reduce:rotate-0 motion-reduce:scale-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px]">Auto-lock on idle</span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb14-bg: #f5f2f8;
  --color-tcb14-bg: oklch(0.965 0.008 305);
  --color-tcb14-ink: #332a3d;
  --color-tcb14-ink: oklch(0.3 0.03 305);
  --color-tcb14-line: #e8e2ee;
  --color-tcb14-line: oklch(0.925 0.012 305);
  --color-tcb14-chip: #f3eff8;
  --color-tcb14-chip: oklch(0.96 0.01 305);
  --color-tcb14-box: #a597b6;
  --color-tcb14-box: oklch(0.7 0.045 305);
  --color-tcb14-acc: #8a3fc4;
  --color-tcb14-acc: oklch(0.52 0.19 305);
  --font-tcb14-sans: 'Sora', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-14 {
  width: 100%;
  min-height: 100svh;
}
```
