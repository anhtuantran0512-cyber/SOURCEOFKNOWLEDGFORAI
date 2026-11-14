---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-right-click-context-menu-dropdown/"
title: "Tailwind Right-Click Context Menu Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "A custom right-click menu that opens at the pointer."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Right-Click Context Menu Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-right-click-context-menu-dropdown/

A custom right-click menu that opens at the pointer. The port draws the line the whole collection argues for: JavaScript computes the two numbers only the runtime can know — left and top, clamped to the viewport — and writes one data-open attribute. Every visual state is a data-open: variant in the markup.
## HTML
```html
<section class="tdd-16 relative w-full min-h-svh select-none bg-linear-[135deg,var(--color-tdd16-bg1),var(--color-tdd16-bg2)] font-tdd16-sans text-tdd16-ink p-5" aria-label="Right-click context menu demo">
  <div id="tdd16-zone" class="flex min-h-[calc(100svh-40px)] cursor-context-menu flex-col items-center justify-center gap-6 rounded-2xl border-2 border-dashed border-tdd16-dash">
    <div class="flex flex-col items-center gap-2 text-[13.5px] font-medium text-tdd16-mut">
      <span class="text-3xl" aria-hidden="true">&#128432;</span>
      <p>Right-click anywhere in this area</p>
    </div>
    <button type="button" id="tdd16-file" class="flex min-h-11 cursor-pointer items-center gap-2 rounded-lg border border-tdd16-edge bg-white px-4.5 py-2.5 text-[13.5px] font-medium text-tdd16-ink shadow-[0_2px_8px_oklch(0_0_0/0.06)] transition-shadow duration-150 hover:shadow-[0_4px_16px_oklch(0_0_0/0.1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd16-acc">
      <span aria-hidden="true">&#128196;</span><span>document.pdf</span>
    </button>
  </div>
  <ul id="tdd16-menu" role="menu" class="pointer-events-none fixed z-[9999] min-w-48 origin-top-left scale-92 list-none rounded-xl border border-tdd16-edge bg-white p-1.5 opacity-0 shadow-[0_8px_30px_oklch(0_0_0/0.16)] transition-[opacity,scale] duration-200 ease-tdd16 data-open:pointer-events-auto data-open:scale-100 data-open:opacity-100 motion-reduce:transition-none">
    <li role="menuitem" tabindex="-1" class="flex cursor-pointer items-center gap-2.5 rounded-[7px] px-3 py-2 text-[13.5px] font-medium text-tdd16-ink transition-colors duration-150 hover:bg-tdd16-tint hover:text-tdd16-acc focus-visible:bg-tdd16-tint focus-visible:outline-none"><span class="w-4.5 text-center text-sm" aria-hidden="true">&#128196;</span>Open</li>
    <li role="menuitem" tabindex="-1" class="flex cursor-pointer items-center gap-2.5 rounded-[7px] px-3 py-2 text-[13.5px] font-medium text-tdd16-ink transition-colors duration-150 hover:bg-tdd16-tint hover:text-tdd16-acc focus-visible:bg-tdd16-tint focus-visible:outline-none"><span class="w-4.5 text-center text-sm" aria-hidden="true">&#128065;</span>Preview</li>
    <li role="separator" class="my-1 h-px bg-tdd16-edge"></li>
    <li role="menuitem" tabindex="-1" class="flex cursor-pointer items-center gap-2.5 rounded-[7px] px-3 py-2 text-[13.5px] font-medium text-tdd16-ink transition-colors duration-150 hover:bg-tdd16-tint hover:text-tdd16-acc focus-visible:bg-tdd16-tint focus-visible:outline-none"><span class="w-4.5 text-center text-sm" aria-hidden="true">&#128461;</span>Copy</li>
    <li role="menuitem" tabindex="-1" class="flex cursor-pointer items-center gap-2.5 rounded-[7px] px-3 py-2 text-[13.5px] font-medium text-tdd16-ink transition-colors duration-150 hover:bg-tdd16-tint hover:text-tdd16-acc focus-visible:bg-tdd16-tint focus-visible:outline-none"><span class="w-4.5 text-center text-sm" aria-hidden="true">&#9999;</span>Rename</li>
    <li role="menuitem" tabindex="-1" class="flex cursor-pointer items-center gap-2.5 rounded-[7px] px-3 py-2 text-[13.5px] font-medium text-tdd16-ink transition-colors duration-150 hover:bg-tdd16-tint hover:text-tdd16-acc focus-visible:bg-tdd16-tint focus-visible:outline-none"><span class="w-4.5 text-center text-sm" aria-hidden="true">&#128279;</span>Copy Link</li>
    <li role="separator" class="my-1 h-px bg-tdd16-edge"></li>
    <li role="menuitem" tabindex="-1" class="flex cursor-pointer items-center gap-2.5 rounded-[7px] px-3 py-2 text-[13.5px] font-medium text-tdd16-danger transition-colors duration-150 hover:bg-tdd16-dangerbg focus-visible:bg-tdd16-dangerbg focus-visible:outline-none"><span class="w-4.5 text-center text-sm" aria-hidden="true">&#128465;</span>Delete</li>
  </ul>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd16-bg1: #f8fafc;
  --color-tdd16-bg1: oklch(0.98 0.005 255);
  --color-tdd16-bg2: #e0f2fe;
  --color-tdd16-bg2: oklch(0.95 0.04 230);
  --color-tdd16-ink: #111827;
  --color-tdd16-ink: oklch(0.21 0.02 265);
  --color-tdd16-mut: #6b7280;
  --color-tdd16-mut: oklch(0.55 0.02 265);
  --color-tdd16-edge: #e5e7eb;
  --color-tdd16-edge: oklch(0.91 0.005 265);
  --color-tdd16-dash: #bae6fd;
  --color-tdd16-dash: oklch(0.88 0.07 230);
  --color-tdd16-tint: #f0f9ff;
  --color-tdd16-tint: oklch(0.98 0.02 230);
  --color-tdd16-acc: #0ea5e9;
  --color-tdd16-acc: oklch(0.68 0.15 233);
  --color-tdd16-danger: #ef4444;
  --color-tdd16-danger: oklch(0.63 0.22 25);
  --color-tdd16-dangerbg: #fef2f2;
  --color-tdd16-dangerbg: oklch(0.97 0.01 20);
  --font-tdd16-sans: 'Inter', system-ui, sans-serif;
  --ease-tdd16: cubic-bezier(0.16, 1, 0.3, 1);
}

.tdd-16 {
  width: 100%;
  min-height: 100svh;
}

.tdd-16 ::selection {
  background: var(--color-tdd16-acc);
  color: #fff;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tdd-16').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var zone = root.querySelector('#tdd16-zone'),
        menu = root.querySelector('#tdd16-menu');
    if (!zone || !menu) return;

    function open(x, y) {
      menu.toggleAttribute('data-open', true);
      var w = menu.offsetWidth || 200, h = menu.offsetHeight || 240;
      menu.style.left = Math.max(8, Math.min(x, window.innerWidth - w - 8)) + 'px';
      menu.style.top = Math.max(8, Math.min(y, window.innerHeight - h - 8)) + 'px';
    }
    function close() { menu.toggleAttribute('data-open', false); }

    zone.addEventListener('contextmenu', function (e) {
      e.preventDefault();
      close();
      requestAnimationFrame(function () { open(e.clientX, e.clientY); });
    });
    document.addEventListener('click', function (e) { if (!menu.contains(e.target)) close(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
    menu.querySelectorAll('[role="menuitem"]').forEach(function (item) {
      item.addEventListener('click', close);
    });
  });
})();
```
