---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-animated-toggle-switch-button/"
title: "Tailwind Animated Toggle Switch with peer-checked & has-checked"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "Three iOS-style switches where the visuals are entirely zero-JS: peer-checked: moves the knob and tints the track, has-checked: highlights the whole row, and…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Toggle Switch with peer-checked & has-checked
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-animated-toggle-switch-button/

Three iOS-style switches where the visuals are entirely zero-JS: peer-checked: moves the knob and tints the track, has-checked: highlights the whole row, and the on/off label swaps with peer-checked:hidden. The only JavaScript left announces the change.
## HTML
```html
<section class="tab-17 w-full min-h-svh grid place-items-center bg-tab17-bg font-tab17-sans px-6 py-10">
  <div class="w-[min(380px,100%)]">
    <p class="mb-5 text-[0.8rem] font-bold tracking-[0.14em] uppercase text-tab17-mut m-0">Preferences</p>
    <div class="flex flex-col gap-2">
      <div class="flex items-center justify-between gap-4 p-4 bg-white border-[1.5px] border-tab17-edge rounded-xl transition-[border-color,background-color] duration-300 has-checked:border-tab17-acc/30 has-checked:bg-tab17-tint motion-reduce:transition-none">
        <div>
          <p class="text-[0.93rem] font-semibold text-tab17-ink m-0">Dark Mode</p>
          <p class="mt-0.5 text-[0.78rem] text-tab17-dim m-0">Applies across the whole workspace</p>
        </div>
        <label class="relative shrink-0 [--on:#7c3aed] cursor-pointer">
          <input type="checkbox" class="peer sr-only" data-label="Dark Mode">
          <span class="flex items-center w-[50px] h-7 p-[3px] bg-tab17-off rounded-full transition-colors duration-300 peer-checked:bg-[var(--on)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-[var(--on)] peer-checked:[&_span]:translate-x-[22px] motion-reduce:transition-none">
            <span class="size-[22px] bg-white rounded-full shadow-[0_1px_4px_oklch(0_0_0/0.2)] transition-transform duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none"></span>
          </span>
          <span class="sr-only peer-checked:hidden">Off</span>
          <span class="sr-only hidden peer-checked:inline">On</span>
        </label>
      </div>
      <div class="flex items-center justify-between gap-4 p-4 bg-white border-[1.5px] border-tab17-edge rounded-xl transition-[border-color,background-color] duration-300 has-checked:border-tab17-acc/30 has-checked:bg-tab17-tint motion-reduce:transition-none">
        <div>
          <p class="text-[0.93rem] font-semibold text-tab17-ink m-0">Push Notifications</p>
          <p class="mt-0.5 text-[0.78rem] text-tab17-dim m-0">Deploys, alerts and mentions</p>
        </div>
        <label class="relative shrink-0 [--on:#0e7490] cursor-pointer">
          <input type="checkbox" class="peer sr-only" data-label="Push Notifications">
          <span class="flex items-center w-[50px] h-7 p-[3px] bg-tab17-off rounded-full transition-colors duration-300 peer-checked:bg-[var(--on)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-[var(--on)] peer-checked:[&_span]:translate-x-[22px] motion-reduce:transition-none">
            <span class="size-[22px] bg-white rounded-full shadow-[0_1px_4px_oklch(0_0_0/0.2)] transition-transform duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none"></span>
          </span>
          <span class="sr-only peer-checked:hidden">Off</span>
          <span class="sr-only hidden peer-checked:inline">On</span>
        </label>
      </div>
      <div class="flex items-center justify-between gap-4 p-4 bg-white border-[1.5px] border-tab17-edge rounded-xl transition-[border-color,background-color] duration-300 has-checked:border-tab17-acc/30 has-checked:bg-tab17-tint motion-reduce:transition-none">
        <div>
          <p class="text-[0.93rem] font-semibold text-tab17-ink m-0">Auto-Save</p>
          <p class="mt-0.5 text-[0.78rem] text-tab17-dim m-0">Every 30 seconds while editing</p>
        </div>
        <label class="relative shrink-0 [--on:#059669] cursor-pointer">
          <input type="checkbox" class="peer sr-only" data-label="Auto-Save" checked>
          <span class="flex items-center w-[50px] h-7 p-[3px] bg-tab17-off rounded-full transition-colors duration-300 peer-checked:bg-[var(--on)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-[var(--on)] peer-checked:[&_span]:translate-x-[22px] motion-reduce:transition-none">
            <span class="size-[22px] bg-white rounded-full shadow-[0_1px_4px_oklch(0_0_0/0.2)] transition-transform duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none"></span>
          </span>
          <span class="sr-only peer-checked:hidden">Off</span>
          <span class="sr-only hidden peer-checked:inline">On</span>
        </label>
      </div>
    </div>
    <p id="tab17-status" role="status" aria-live="polite" class="sr-only"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab17-bg: #f8fafc;
  --color-tab17-bg: oklch(0.98 0.004 250);
  --color-tab17-ink: #1e293b;
  --color-tab17-ink: oklch(0.28 0.03 258);
  --color-tab17-mut: #64748b;
  --color-tab17-mut: oklch(0.55 0.03 255);
  --color-tab17-dim: #94a3b8;
  --color-tab17-dim: oklch(0.72 0.03 255);
  --color-tab17-edge: #e2e8f0;
  --color-tab17-edge: oklch(0.92 0.01 250);
  --color-tab17-off: #cbd5e1;
  --color-tab17-off: oklch(0.85 0.02 250);
  --color-tab17-acc: #7c3aed;
  --color-tab17-acc: oklch(0.53 0.25 295);
  --color-tab17-tint: #faf7ff;
  --color-tab17-tint: oklch(0.98 0.01 300);
  --font-tab17-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tab-17 {
  width: 100%;
  min-height: 100svh;
}

.tab-17 ::selection {
  background: var(--color-tab17-acc);
  color: #fff;
}
```

## JavaScript
```js
(function () {
  var status = document.getElementById('tab17-status');
  var inputs = document.querySelectorAll('.tab-17 input[type="checkbox"]');
  if (!status || !inputs.length) return;
  inputs.forEach(function (input) {
    input.addEventListener('change', function () {
      status.textContent = (input.dataset.label || 'Setting') + (input.checked ? ' on' : ' off');
    });
  });
})();
```
