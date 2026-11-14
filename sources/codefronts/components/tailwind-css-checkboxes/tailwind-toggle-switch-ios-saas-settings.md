---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/tailwind-toggle-switch-ios-saas-settings/"
title: "Tailwind CSS Toggle Switch — iOS-Style SaaS Settings"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "The settings-page classic in utilities: a pill track and a gliding thumb, driven by a peer checkbox that stays in the tab order via sr-only."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Toggle Switch — iOS-Style SaaS Settings
Source: https://codefronts.com/components/tailwind-css-checkboxes/tailwind-toggle-switch-ios-saas-settings/

The settings-page classic in utilities: a pill track and a gliding thumb, driven by a peer checkbox that stays in the tab order via sr-only. The track paints with peer-checked:bg-tcb01-acc; the thumb, nested one level deeper, moves with group-has-checked:translate-x-5.
## HTML
```html
<section class="tcb-01 w-full min-h-svh grid place-items-center bg-tcb01-bg px-5 py-14 font-tcb01-sans text-tcb01-ink selection:bg-tcb01-acc selection:text-white" aria-label="SaaS dashboard toggle switches">
  <div class="w-full max-w-[26rem] overflow-hidden rounded-2xl border border-tcb01-line bg-white shadow-tcb01-panel">
    <header class="border-b border-tcb01-line px-5.5 py-4">
      <h2 class="text-[15px] font-bold tracking-[-0.01em]">Notifications</h2>
      <p class="mt-0.5 text-[13px] text-tcb01-mut">Choose what lands in your inbox.</p>
    </header>
    <div class="divide-y divide-tcb01-line">
      <label class="group flex min-h-16 cursor-pointer items-center justify-between gap-4 px-5.5 py-4 transition-colors hover:bg-tcb01-hover">
        <span><span class="block text-[15px] font-semibold">Email notifications</span><span class="mt-0.5 block text-[13px] text-tcb01-mut">Product news &amp; weekly digest</span></span>
        <input type="checkbox" class="peer sr-only" checked>
        <span aria-hidden="true" class="relative h-[26px] w-[46px] flex-none rounded-full bg-tcb01-off transition-colors duration-300 peer-checked:bg-tcb01-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb01-acc motion-reduce:transition-none">
          <span class="absolute left-[3px] top-[3px] size-5 rounded-full bg-white shadow-tcb01-thumb transition-transform duration-300 ease-[cubic-bezier(.2,.8,.2,1)] group-has-checked:translate-x-5 motion-reduce:transition-none"></span>
        </span>
      </label>
      <label class="group flex min-h-16 cursor-pointer items-center justify-between gap-4 px-5.5 py-4 transition-colors hover:bg-tcb01-hover">
        <span><span class="block text-[15px] font-semibold">Two-factor auth</span><span class="mt-0.5 block text-[13px] text-tcb01-mut">Require a code at sign-in</span></span>
        <input type="checkbox" class="peer sr-only">
        <span aria-hidden="true" class="relative h-[26px] w-[46px] flex-none rounded-full bg-tcb01-off transition-colors duration-300 peer-checked:bg-tcb01-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb01-acc motion-reduce:transition-none">
          <span class="absolute left-[3px] top-[3px] size-5 rounded-full bg-white shadow-tcb01-thumb transition-transform duration-300 ease-[cubic-bezier(.2,.8,.2,1)] group-has-checked:translate-x-5 motion-reduce:transition-none"></span>
        </span>
      </label>
      <label class="group flex min-h-16 cursor-pointer items-center justify-between gap-4 px-5.5 py-4 transition-colors hover:bg-tcb01-hover">
        <span><span class="block text-[15px] font-semibold">Usage analytics</span><span class="mt-0.5 block text-[13px] text-tcb01-mut">Share anonymised metrics</span></span>
        <input type="checkbox" class="peer sr-only" checked>
        <span aria-hidden="true" class="relative h-[26px] w-[46px] flex-none rounded-full bg-tcb01-off transition-colors duration-300 peer-checked:bg-tcb01-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb01-acc motion-reduce:transition-none">
          <span class="absolute left-[3px] top-[3px] size-5 rounded-full bg-white shadow-tcb01-thumb transition-transform duration-300 ease-[cubic-bezier(.2,.8,.2,1)] group-has-checked:translate-x-5 motion-reduce:transition-none"></span>
        </span>
      </label>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb01-bg: #f4f5f7;
  --color-tcb01-bg: oklch(0.97 0.004 260);
  --color-tcb01-ink: #1f2430;
  --color-tcb01-ink: oklch(0.25 0.02 265);
  --color-tcb01-mut: #5d6472;
  --color-tcb01-mut: oklch(0.49 0.02 265);
  --color-tcb01-line: #eceef2;
  --color-tcb01-line: oklch(0.945 0.006 265);
  --color-tcb01-hover: #f8f9fb;
  --color-tcb01-hover: oklch(0.982 0.003 265);
  --color-tcb01-off: #cfd4dc;
  --color-tcb01-off: oklch(0.86 0.012 265);
  --color-tcb01-acc: #2f7de1;
  --color-tcb01-acc: oklch(0.6 0.17 255);
  --font-tcb01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --shadow-tcb01-panel: 0 18px 40px -28px rgb(16 24 40 / 0.5);
  --shadow-tcb01-thumb: 0 2px 5px rgb(16 24 40 / 0.35);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-01 {
  width: 100%;
  min-height: 100svh;
}
```
