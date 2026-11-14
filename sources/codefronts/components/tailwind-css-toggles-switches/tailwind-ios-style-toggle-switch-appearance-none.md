---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-ios-style-toggle-switch-appearance-none/"
title: "Tailwind iOS-Style Toggle Switch with appearance-none"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "The most searched toggle on earth, ported: appearance-none turns the checkbox itself into the 52&times;32 track, a before: thumb glides across on…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind iOS-Style Toggle Switch with appearance-none
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-ios-style-toggle-switch-appearance-none/

The most searched toggle on earth, ported: appearance-none turns the checkbox itself into the 52&times;32 track, a before: thumb glides across on checked:before:translate-x-5, and active:before:w-8 reproduces the native iOS squash. The port's win is that the resting, on, pressed and reduced-motion states all sit in one class list on the input.
## HTML
```html
<section class="ttg-01 w-full min-h-svh flex flex-col items-center justify-center gap-6 px-5 py-14 bg-ttg01-bg font-ttg01-sans" aria-label="iOS-style toggle switch">
  <div class="w-[min(360px,100%)] rounded-3xl bg-white border border-ttg01-edge shadow-[0_1px_2px_oklch(0.55_0.02_255/0.06),0_18px_40px_-28px_oklch(0.45_0.05_255/0.45)] divide-y divide-ttg01-edge overflow-hidden">
    <label for="ttg-01-sw" class="flex items-center gap-6 min-h-16 px-5 py-4 cursor-pointer transition-colors duration-150 hover:bg-ttg01-tint">
      <span class="flex flex-col gap-0.5 flex-1">
        <span class="text-[15.5px] font-semibold text-ttg01-ink">Wi-Fi</span>
        <span class="text-[12.5px] text-ttg01-mute">Auto-join known networks</span>
      </span>
      <input type="checkbox" id="ttg-01-sw" role="switch" checked class="appearance-none shrink-0 w-[52px] h-8 rounded-full bg-ttg01-off relative cursor-pointer transition-colors duration-300 shadow-[inset_0_0_0_1px_oklch(0.55_0.02_255/0.08)] before:content-[''] before:absolute before:top-0.5 before:left-0.5 before:w-7 before:h-7 before:rounded-full before:bg-white before:shadow-[0_3px_8px_oklch(0.3_0.02_255/0.18),0_1px_1px_oklch(0.3_0.02_255/0.16)] before:transition-[transform,width] before:duration-300 before:ease-[cubic-bezier(0.2,0.9,0.25,1.05)] checked:bg-ttg01-on checked:before:translate-x-5 active:before:w-8 checked:active:before:translate-x-[15px] focus-visible:outline-3 focus-visible:outline-ttg01-focus focus-visible:outline-offset-3 motion-reduce:transition-none motion-reduce:before:transition-none">
    </label>
    <label for="ttg-01-bt" class="flex items-center gap-6 min-h-16 px-5 py-4 cursor-pointer transition-colors duration-150 hover:bg-ttg01-tint">
      <span class="flex flex-col gap-0.5 flex-1">
        <span class="text-[15.5px] font-semibold text-ttg01-ink">Bluetooth</span>
        <span class="text-[12.5px] text-ttg01-mute">Discoverable as &ldquo;Studio&rdquo;</span>
      </span>
      <input type="checkbox" id="ttg-01-bt" role="switch" class="appearance-none shrink-0 w-[52px] h-8 rounded-full bg-ttg01-off relative cursor-pointer transition-colors duration-300 shadow-[inset_0_0_0_1px_oklch(0.55_0.02_255/0.08)] before:content-[''] before:absolute before:top-0.5 before:left-0.5 before:w-7 before:h-7 before:rounded-full before:bg-white before:shadow-[0_3px_8px_oklch(0.3_0.02_255/0.18),0_1px_1px_oklch(0.3_0.02_255/0.16)] before:transition-[transform,width] before:duration-300 before:ease-[cubic-bezier(0.2,0.9,0.25,1.05)] checked:bg-ttg01-on checked:before:translate-x-5 active:before:w-8 checked:active:before:translate-x-[15px] focus-visible:outline-3 focus-visible:outline-ttg01-focus focus-visible:outline-offset-3 motion-reduce:transition-none motion-reduce:before:transition-none">
    </label>
  </div>
  <p class="font-ttg01-mono text-[11px] tracking-[0.14em] uppercase text-ttg01-mute">Click &middot; or Tab + Space</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg01-bg: #f1f2f6;
  --color-ttg01-bg: oklch(0.96 0.005 255);
  --color-ttg01-edge: #e6e7ee;
  --color-ttg01-edge: oklch(0.93 0.005 255);
  --color-ttg01-tint: #f7f8fb;
  --color-ttg01-tint: oklch(0.98 0.004 255);
  --color-ttg01-ink: #1c1d22;
  --color-ttg01-ink: oklch(0.24 0.008 265);
  --color-ttg01-mute: #8b8e99;
  --color-ttg01-mute: oklch(0.63 0.012 265);
  --color-ttg01-off: #e4e4ea;
  --color-ttg01-off: oklch(0.92 0.004 265);
  --color-ttg01-on: #2fbf5b;
  --color-ttg01-on: oklch(0.72 0.18 149);
  --color-ttg01-focus: #0a84ff;
  --color-ttg01-focus: oklch(0.62 0.2 256);
  --font-ttg01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttg01-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
}
/* Root rule: the full-bleed contract, also stated in the markup's utilities, so the
   stage is sized correctly before the browser build has compiled. */

.ttg-01 {
  width: 100%;
  min-height: 100svh;
}
/* Older Safari still wants the prefix on a checkbox. */

.ttg-01 input[type="checkbox"] {
  -webkit-appearance: none;
}
```
