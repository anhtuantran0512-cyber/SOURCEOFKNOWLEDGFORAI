---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-password-toggle-input/"
title: "Tailwind Password Toggle Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "An eye button that swaps type=\"password\" for type=\"text\", with the icon swap driven entirely by aria-pressed."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Password Toggle Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-password-toggle-input/

An eye button that swaps type="password" for type="text", with the icon swap driven entirely by aria-pressed. Role, name and state change in lockstep — WCAG 4.1.2 satisfied by construction rather than by discipline.
## HTML
```html
<div class="tif-27 grid min-h-svh w-full place-items-center bg-tif27-bg px-6 py-14 font-tif27-sans" aria-label="Password toggle input demo">
  <label class="grid w-full max-w-70 gap-1.5">
    <span class="font-tif27-mono text-[10px] tracking-[0.12em] text-tif27-mut uppercase">Password</span>
    <span class="flex items-center rounded-[10px] border border-white/12 bg-tif27-field py-0.5 pr-1 pl-3.5 transition-colors duration-200 focus-within:border-tif27-acc">
      <input type="password" name="tif27-pw" autocomplete="new-password" placeholder="At least 8 characters" minlength="8" data-tif27-input
        class="min-w-0 flex-1 border-0 bg-transparent py-3 text-sm font-medium tracking-[0.08em] text-tif27-ink outline-none placeholder:tracking-normal placeholder:text-tif27-mut">
      <button type="button" aria-label="Show password" aria-pressed="false" data-tif27-toggle
        class="group grid size-11 shrink-0 cursor-pointer place-items-center rounded-md border-0 bg-transparent transition-colors duration-150 hover:bg-white/5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tif27-acc">
        <svg viewBox="0 0 24 24" aria-hidden="true" class="size-4 fill-none stroke-tif27-mut stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed:hidden group-aria-pressed:stroke-tif27-acc"><path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/></svg>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="hidden size-4 fill-none stroke-tif27-acc stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed:block"><path d="M3 3l18 18M9.9 5.1A10 10 0 0 1 22 12a16 16 0 0 1-2.7 3.7M6.7 6.7A16 16 0 0 0 2 12s4 7 10 7a10 10 0 0 0 4.1-.9"/></svg>
      </button>
    </span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif27-bg: #12121a;
  --color-tif27-bg: oklch(0.19 0.015 285);
  --color-tif27-field: #1a1a22;
  --color-tif27-field: oklch(0.23 0.015 285);
  --color-tif27-ink: #f0eeff;
  --color-tif27-ink: oklch(0.95 0.02 290);
  --color-tif27-mut: #b8b6d4;
  --color-tif27-mut: oklch(0.77 0.03 290);
  --color-tif27-acc: #7c6cff;
  --color-tif27-acc: oklch(0.62 0.2 288);
  --font-tif27-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tif27-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tif-27 {
  width: 100%;
}

.tif-27 ::selection {
  background: var(--color-tif27-acc);
  color: #12121a;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tif-27').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var input = root.querySelector('[data-tif27-input]');
    var btn = root.querySelector('[data-tif27-toggle]');
    if (!input || !btn) return;
    btn.addEventListener('click', function () {
      var on = btn.getAttribute('aria-pressed') === 'true';
      btn.setAttribute('aria-pressed', on ? 'false' : 'true');
      btn.setAttribute('aria-label', on ? 'Show password' : 'Hide password');
      input.type = on ? 'password' : 'text';
    });
  });
})();
```
