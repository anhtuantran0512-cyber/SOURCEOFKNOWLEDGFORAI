---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-stacked-radio-list-payment-method/"
title: "Tailwind Stacked Radio List (Payment Method)"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "The connected vertical list: options stacked in one bordered container with hairline dividers — one object, not floating cards — and a tinted rail that…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stacked Radio List (Payment Method)
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-stacked-radio-list-payment-method/

The connected vertical list: options stacked in one bordered container with hairline dividers — one object, not floating cards — and a tinted rail that scales in beside the checked row. Dividers are divide-y on the container, the rail is scale-y-0 group-has-checked:scale-y-100, and each row now carries a card-brand chip.
## HTML
```html
<section class="trb-22 w-full min-h-svh grid place-items-center bg-trb22-bg px-6 py-14 font-trb22-sans text-trb22-ink" aria-label="Stacked vertical radio list demo">
  <fieldset class="w-full max-w-[28rem]">
    <legend class="text-2xl font-bold tracking-[-0.02em]">Payment method</legend>
    <div class="mt-5 divide-y divide-trb22-line overflow-hidden rounded-2xl border-[1.5px] border-trb22-line bg-white shadow-trb22-stack">
      <label class="group relative flex min-h-16 cursor-pointer items-center gap-3.5 px-5 transition-colors duration-250 hover:bg-trb22-hover has-checked:bg-trb22-acc/5 has-focus-visible:outline-3 has-focus-visible:-outline-offset-3 has-focus-visible:outline-trb22-acc">
        <input type="radio" name="trb-22" value="visa" class="sr-only" checked>
        <span aria-hidden="true" class="absolute inset-y-0 left-0 w-[3px] scale-y-0 bg-trb22-acc transition-transform duration-300 ease-trb22-glide group-has-checked:scale-y-100 motion-reduce:transition-none"></span>
        <span aria-hidden="true" class="grid size-[21px] flex-none place-items-center rounded-full border-2 border-trb22-ring transition-colors after:size-2.5 after:scale-0 after:rounded-full after:bg-trb22-acc after:transition-transform after:duration-300 after:ease-trb22-spring after:content-[''] group-has-checked:border-trb22-acc group-has-checked:after:scale-100"></span>
        <span aria-hidden="true" class="grid h-7 w-11 flex-none place-items-center rounded-md bg-[#1a1f71] font-trb22-mono text-[10px] font-medium tracking-[0.04em] text-white">VISA</span>
        <span class="grid flex-1 gap-px"><span class="text-[15px] font-semibold">Visa ending 4242</span><span class="text-[12.5px] text-trb22-mut">Expires 09/28</span></span>
        <span class="text-xs font-semibold tracking-[0.03em] text-trb22-mut group-has-checked:text-trb22-acc">Default</span>
      </label>
      <label class="group relative flex min-h-16 cursor-pointer items-center gap-3.5 px-5 transition-colors duration-250 hover:bg-trb22-hover has-checked:bg-trb22-acc/5 has-focus-visible:outline-3 has-focus-visible:-outline-offset-3 has-focus-visible:outline-trb22-acc">
        <input type="radio" name="trb-22" value="amex" class="sr-only">
        <span aria-hidden="true" class="absolute inset-y-0 left-0 w-[3px] scale-y-0 bg-trb22-acc transition-transform duration-300 ease-trb22-glide group-has-checked:scale-y-100 motion-reduce:transition-none"></span>
        <span aria-hidden="true" class="grid size-[21px] flex-none place-items-center rounded-full border-2 border-trb22-ring transition-colors after:size-2.5 after:scale-0 after:rounded-full after:bg-trb22-acc after:transition-transform after:duration-300 after:ease-trb22-spring after:content-[''] group-has-checked:border-trb22-acc group-has-checked:after:scale-100"></span>
        <span aria-hidden="true" class="grid h-7 w-11 flex-none place-items-center rounded-md bg-[#2e77bb] font-trb22-mono text-[10px] font-medium tracking-[0.04em] text-white">AMEX</span>
        <span class="grid flex-1 gap-px"><span class="text-[15px] font-semibold">Amex ending 1005</span><span class="text-[12.5px] text-trb22-mut">Expires 02/27</span></span>
      </label>
      <label class="group relative flex min-h-16 cursor-pointer items-center gap-3.5 px-5 transition-colors duration-250 hover:bg-trb22-hover has-checked:bg-trb22-acc/5 has-focus-visible:outline-3 has-focus-visible:-outline-offset-3 has-focus-visible:outline-trb22-acc">
        <input type="radio" name="trb-22" value="bank" class="sr-only">
        <span aria-hidden="true" class="absolute inset-y-0 left-0 w-[3px] scale-y-0 bg-trb22-acc transition-transform duration-300 ease-trb22-glide group-has-checked:scale-y-100 motion-reduce:transition-none"></span>
        <span aria-hidden="true" class="grid size-[21px] flex-none place-items-center rounded-full border-2 border-trb22-ring transition-colors after:size-2.5 after:scale-0 after:rounded-full after:bg-trb22-acc after:transition-transform after:duration-300 after:ease-trb22-spring after:content-[''] group-has-checked:border-trb22-acc group-has-checked:after:scale-100"></span>
        <span aria-hidden="true" class="grid h-7 w-11 flex-none place-items-center rounded-md bg-trb22-chip text-trb22-mut"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10h18M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18M12 3l9 5H3z"/></svg></span>
        <span class="grid flex-1 gap-px"><span class="text-[15px] font-semibold">Bank transfer</span><span class="text-[12.5px] text-trb22-mut">2–3 business days</span></span>
        <span class="text-xs font-semibold tracking-[0.03em] text-trb22-mut group-has-checked:text-trb22-acc">No fee</span>
      </label>
    </div>
    <p class="mt-3.5 flex items-center gap-2 text-[13px] text-trb22-mut"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>Payments are encrypted and processed securely.</p>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb22-bg: #f5f6f9;
  --color-trb22-bg: oklch(0.97 0.005 265);
  --color-trb22-ink: #1e222e;
  --color-trb22-ink: oklch(0.25 0.025 270);
  --color-trb22-mut: #5f6578;
  --color-trb22-mut: oklch(0.5 0.025 270);
  --color-trb22-line: #e2e5ee;
  --color-trb22-line: oklch(0.92 0.01 270);
  --color-trb22-hover: #f8f9fc;
  --color-trb22-hover: oklch(0.98 0.004 270);
  --color-trb22-chip: #eef0f5;
  --color-trb22-chip: oklch(0.95 0.007 270);
  --color-trb22-ring: #b8bed0;
  --color-trb22-ring: oklch(0.8 0.02 270);
  --color-trb22-acc: #2d63c8;
  --color-trb22-acc: oklch(0.52 0.16 255);
  --shadow-trb22-stack: 0 1px 4px oklch(0.25 0.03 270 / 0.05);
  --ease-trb22-glide: cubic-bezier(0.22, 1, 0.36, 1);
  --ease-trb22-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --font-trb22-sans: 'Geist', system-ui, sans-serif;
  --font-trb22-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-22 {
  width: 100%;
  min-height: 100svh;
}
```
