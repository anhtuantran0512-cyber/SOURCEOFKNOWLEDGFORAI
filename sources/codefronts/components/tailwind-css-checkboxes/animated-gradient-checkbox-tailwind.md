---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/animated-gradient-checkbox-tailwind/"
title: "Animated Gradient Checkbox in Tailwind CSS — Rainbow Sweep"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "Checked boxes fill with a rainbow that sweeps endlessly: a 300%-wide gradient on before:, scrolled by animate-tcb16-sweep."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Gradient Checkbox in Tailwind CSS — Rainbow Sweep
Source: https://codefronts.com/components/tailwind-css-checkboxes/animated-gradient-checkbox-tailwind/

Checked boxes fill with a rainbow that sweeps endlessly: a 300%-wide gradient on before:, scrolled by animate-tcb16-sweep. New: the checked label picks up the same gradient as text via bg-clip-text, tying label and box together.
## HTML
```html
<section class="tcb-16 w-full min-h-svh grid place-items-center bg-tcb16-bg px-5 py-14 font-tcb16-sans text-tcb16-ink selection:bg-tcb16-violet selection:text-white" aria-label="Gradient sweep checkboxes">
  <div class="w-full max-w-[25rem] rounded-2xl border border-tcb16-line bg-tcb16-panel px-4 py-3">
    <label class="group flex min-h-13 cursor-pointer items-center gap-3.5 px-1.5"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="relative grid size-[26px] flex-none place-items-center overflow-hidden rounded-lg border-2 border-tcb16-box bg-tcb16-well text-white transition-colors duration-250 peer-checked:border-transparent peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb16-violet before:absolute before:inset-0 before:bg-[linear-gradient(115deg,#ff2e97,#ff9a3d,#ffe74c,#2effc8,#5b8bff,#c04cff,#ff2e97)] before:[background-size:300%_300%] before:opacity-0 before:transition-opacity before:duration-300 before:content-[''] group-has-checked:before:animate-tcb16-sweep group-has-checked:before:opacity-100 motion-reduce:before:animate-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="relative size-[15px] scale-50 opacity-0 drop-shadow-[0_1px_1px_rgb(0_0_0/0.35)] transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="bg-[linear-gradient(90deg,#ff7ab8,#ffc36b,#7dffd9,#9db8ff)] bg-clip-text text-[15px] font-medium transition-colors group-has-checked:text-transparent">Mint on completion</span></label>
    <label class="group flex min-h-13 cursor-pointer items-center gap-3.5 px-1.5"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="relative grid size-[26px] flex-none place-items-center overflow-hidden rounded-lg border-2 border-tcb16-box bg-tcb16-well text-white transition-colors duration-250 peer-checked:border-transparent peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb16-violet before:absolute before:inset-0 before:bg-[linear-gradient(115deg,#ff2e97,#ff9a3d,#ffe74c,#2effc8,#5b8bff,#c04cff,#ff2e97)] before:[background-size:300%_300%] before:opacity-0 before:transition-opacity before:duration-300 before:content-[''] group-has-checked:before:animate-tcb16-sweep group-has-checked:before:opacity-100 motion-reduce:before:animate-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="relative size-[15px] scale-50 opacity-0 drop-shadow-[0_1px_1px_rgb(0_0_0/0.35)] transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="bg-[linear-gradient(90deg,#ff7ab8,#ffc36b,#7dffd9,#9db8ff)] bg-clip-text text-[15px] font-medium transition-colors group-has-checked:text-transparent">Enable gasless mode</span></label>
    <label class="group flex min-h-13 cursor-pointer items-center gap-3.5 px-1.5"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="relative grid size-[26px] flex-none place-items-center overflow-hidden rounded-lg border-2 border-tcb16-box bg-tcb16-well text-white transition-colors duration-250 peer-checked:border-transparent peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb16-violet before:absolute before:inset-0 before:bg-[linear-gradient(115deg,#ff2e97,#ff9a3d,#ffe74c,#2effc8,#5b8bff,#c04cff,#ff2e97)] before:[background-size:300%_300%] before:opacity-0 before:transition-opacity before:duration-300 before:content-[''] group-has-checked:before:animate-tcb16-sweep group-has-checked:before:opacity-100 motion-reduce:before:animate-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="relative size-[15px] scale-50 opacity-0 drop-shadow-[0_1px_1px_rgb(0_0_0/0.35)] transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="bg-[linear-gradient(90deg,#ff7ab8,#ffc36b,#7dffd9,#9db8ff)] bg-clip-text text-[15px] font-medium transition-colors group-has-checked:text-transparent">Show floor price</span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb16-bg: #0f1020;
  --color-tcb16-bg: oklch(0.17 0.03 280);
  --color-tcb16-panel: #181a30;
  --color-tcb16-panel: oklch(0.22 0.04 280);
  --color-tcb16-well: #12142a;
  --color-tcb16-well: oklch(0.19 0.04 280);
  --color-tcb16-line: #2a2d4a;
  --color-tcb16-line: oklch(0.3 0.05 280);
  --color-tcb16-box: #4a4f80;
  --color-tcb16-box: oklch(0.43 0.08 280);
  --color-tcb16-ink: #c7cbe6;
  --color-tcb16-ink: oklch(0.85 0.04 280);
  --color-tcb16-violet: #c04cff;
  --color-tcb16-violet: oklch(0.64 0.26 310);
  --font-tcb16-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tcb16-sweep: tcb16-sweep 4s linear infinite;

  @keyframes tcb16-sweep {
    from {
      background-position: 0% 50%;
    }

    to {
      background-position: 300% 50%;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-16 {
  width: 100%;
  min-height: 100svh;
}
```
