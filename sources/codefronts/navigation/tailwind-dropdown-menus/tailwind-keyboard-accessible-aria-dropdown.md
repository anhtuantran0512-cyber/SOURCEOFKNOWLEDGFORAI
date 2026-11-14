---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-keyboard-accessible-aria-dropdown/"
title: "Tailwind Keyboard Accessible ARIA Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "The WAI-ARIA menu button, and the port's cleanest win: the open state is aria-expanded, so aria-expanded: on the button and group-has-aria-expanded: on its…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Keyboard Accessible ARIA Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-keyboard-accessible-aria-dropdown/

The WAI-ARIA menu button, and the port's cleanest win: the open state is aria-expanded, so aria-expanded: on the button and group-has-aria-expanded: on its panel style straight off the accessibility attribute. Style and semantics cannot drift, because there is only one source of truth.
## HTML
```html
<section class="tdd-17 w-full min-h-svh grid place-items-center bg-linear-[135deg,var(--color-tdd17-bg1),var(--color-tdd17-bg2)] font-tdd17-sans text-tdd17-ink px-5 py-10" aria-label="Keyboard accessible ARIA dropdown demo">
  <div class="flex flex-col items-center gap-5">
    <div class="flex items-center gap-3">
      <span class="rounded-full bg-tdd17-badge px-2.5 py-1 text-[11px] font-bold tracking-[0.04em] text-tdd17-acc">&#9654; Keyboard</span>
      <span class="text-[12.5px] text-tdd17-mut">Try: Enter, &#8593;&#8595;, Home/End, Escape</span>
    </div>
    <div class="group relative">
      <button type="button" id="tdd17-btn" aria-haspopup="true" aria-expanded="false" aria-controls="tdd17-menu" class="flex min-h-11 cursor-pointer items-center gap-2.5 rounded-xl border border-tdd17-edge bg-white py-2.5 pr-3.5 pl-4.5 font-tdd17-sans text-sm font-semibold text-tdd17-ink shadow-[0_1px_4px_oklch(0_0_0/0.05)] transition-[box-shadow,border-color] duration-150 hover:border-tdd17-ring hover:shadow-[0_4px_16px_oklch(0_0_0/0.1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd17-acc aria-expanded:border-tdd17-acc aria-expanded:shadow-[0_0_0_3px_oklch(0.6_0.13_163/0.16)]">
        <span>My Account</span>
        <span class="flex size-8 items-center justify-center rounded-full bg-tdd17-acc text-xs font-bold tracking-[0.04em] text-white" aria-hidden="true">JD</span>
      </button>
      <ul id="tdd17-menu" role="menu" aria-labelledby="tdd17-btn" class="pointer-events-none invisible absolute top-[calc(100%+8px)] right-0 min-w-50 origin-top-right -translate-y-2 scale-97 list-none rounded-xl border border-tdd17-edge bg-white p-1.5 opacity-0 shadow-[0_12px_40px_oklch(0_0_0/0.12)] transition-[opacity,translate,scale] duration-220 ease-tdd17 group-has-aria-expanded:pointer-events-auto group-has-aria-expanded:visible group-has-aria-expanded:translate-y-0 group-has-aria-expanded:scale-100 group-has-aria-expanded:opacity-100 motion-reduce:transition-none">
        <li role="none"><a href="#profile" role="menuitem" tabindex="-1" class="flex min-h-11 items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd17-ink no-underline transition-colors duration-150 hover:bg-tdd17-tint hover:text-tdd17-acc focus-visible:bg-tdd17-tint focus-visible:text-tdd17-acc focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdd17-acc"><span aria-hidden="true">&#128100;</span>Profile</a></li>
        <li role="none"><a href="#settings" role="menuitem" tabindex="-1" class="flex min-h-11 items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd17-ink no-underline transition-colors duration-150 hover:bg-tdd17-tint hover:text-tdd17-acc focus-visible:bg-tdd17-tint focus-visible:text-tdd17-acc focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdd17-acc"><span aria-hidden="true">&#9881;</span>Settings</a></li>
        <li role="none"><a href="#billing" role="menuitem" tabindex="-1" class="flex min-h-11 items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd17-ink no-underline transition-colors duration-150 hover:bg-tdd17-tint hover:text-tdd17-acc focus-visible:bg-tdd17-tint focus-visible:text-tdd17-acc focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdd17-acc"><span aria-hidden="true">&#128178;</span>Billing</a></li>
        <li role="none"><a href="#upgrade" role="menuitem" tabindex="-1" class="flex min-h-11 items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd17-ink no-underline transition-colors duration-150 hover:bg-tdd17-tint hover:text-tdd17-acc focus-visible:bg-tdd17-tint focus-visible:text-tdd17-acc focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdd17-acc"><span aria-hidden="true">&#127381;</span>Upgrade</a></li>
        <li role="separator" class="my-1 h-px bg-tdd17-edge"></li>
        <li role="none"><a href="#signout" role="menuitem" tabindex="-1" class="flex min-h-11 items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd17-danger no-underline transition-colors duration-150 hover:bg-tdd17-dangerbg focus-visible:bg-tdd17-dangerbg focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdd17-danger"><span aria-hidden="true">&#128275;</span>Sign Out</a></li>
      </ul>
    </div>
    <p class="text-xs italic text-tdd17-mut">Styled straight off aria-expanded &mdash; no second state to keep in sync</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd17-bg1: #f0fdf4;
  --color-tdd17-bg1: oklch(0.98 0.02 150);
  --color-tdd17-bg2: #ecfdf5;
  --color-tdd17-bg2: oklch(0.98 0.02 165);
  --color-tdd17-ink: #111827;
  --color-tdd17-ink: oklch(0.21 0.02 265);
  --color-tdd17-mut: #6b7280;
  --color-tdd17-mut: oklch(0.55 0.02 265);
  --color-tdd17-edge: #e5e7eb;
  --color-tdd17-edge: oklch(0.91 0.005 265);
  --color-tdd17-ring: #6ee7b7;
  --color-tdd17-ring: oklch(0.85 0.13 165);
  --color-tdd17-badge: #d1fae5;
  --color-tdd17-badge: oklch(0.92 0.06 165);
  --color-tdd17-tint: #f0fdf4;
  --color-tdd17-tint: oklch(0.98 0.02 150);
  --color-tdd17-acc: #059669;
  --color-tdd17-acc: oklch(0.6 0.13 163);
  --color-tdd17-danger: #ef4444;
  --color-tdd17-danger: oklch(0.63 0.22 25);
  --color-tdd17-dangerbg: #fef2f2;
  --color-tdd17-dangerbg: oklch(0.97 0.01 20);
  --font-tdd17-sans: 'Inter', system-ui, sans-serif;
  --ease-tdd17: cubic-bezier(0.16, 1, 0.3, 1);
}

.tdd-17 {
  width: 100%;
  min-height: 100svh;
}

.tdd-17 ::selection {
  background: var(--color-tdd17-acc);
  color: #ecfdf5;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tdd-17').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var btn = root.querySelector('#tdd17-btn'),
        menu = root.querySelector('#tdd17-menu');
    if (!btn || !menu) return;
    var items = function () { return Array.from(menu.querySelectorAll('[role="menuitem"]')); };
    var isOpen = function () { return btn.getAttribute('aria-expanded') === 'true'; };

    function set(open, focusFirst) {
      btn.setAttribute('aria-expanded', String(open));
      if (open && focusFirst) { var i = items(); if (i.length) i[0].focus(); }
    }

    btn.addEventListener('click', function () { set(!isOpen(), true); });
    btn.addEventListener('keydown', function (e) {
      if ((e.key === 'Enter' || e.key === ' ') && !isOpen()) { e.preventDefault(); set(true, true); }
      else if (e.key === 'Escape' && isOpen()) set(false);
    });
    menu.addEventListener('keydown', function (e) {
      var list = items(), idx = list.indexOf(document.activeElement);
      if (e.key === 'ArrowDown') { e.preventDefault(); list[(idx + 1) % list.length].focus(); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); list[(idx - 1 + list.length) % list.length].focus(); }
      else if (e.key === 'Home') { e.preventDefault(); list[0].focus(); }
      else if (e.key === 'End') { e.preventDefault(); list[list.length - 1].focus(); }
      else if (e.key === 'Escape') { set(false); btn.focus(); }
      else if (e.key === 'Tab') set(false);
    });
    document.addEventListener('mousedown', function (e) {
      if (!btn.contains(e.target) && !menu.contains(e.target)) set(false);
    });
  });
})();
```
