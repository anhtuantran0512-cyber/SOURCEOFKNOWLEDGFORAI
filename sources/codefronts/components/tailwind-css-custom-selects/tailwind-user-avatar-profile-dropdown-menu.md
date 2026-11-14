---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-user-avatar-profile-dropdown-menu/"
title: "Tailwind User Avatar Profile Dropdown Menu"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "The navbar account menu, and the port's win is that there is no state attribute to invent: the panel opens off the button's own aria-expanded through…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind User Avatar Profile Dropdown Menu
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-user-avatar-profile-dropdown-menu/

The navbar account menu, and the port's win is that there is no state attribute to invent: the panel opens off the button's own aria-expanded through group-has-aria-expanded:. Actions, not values &mdash; so this one is a role="menu" with roving focus, not a listbox, and the sign-out row tints itself from the danger token.
## HTML
```html
<section class="tcs-05 w-full min-h-svh bg-tcs05-bg font-tcs05-sans text-tcs05-ink" aria-label="User avatar profile dropdown demo">
  <div class="flex items-center justify-between gap-4 px-6.5 py-4 bg-tcs05-bar border-b border-tcs05-line">
    <span class="text-[17px] font-extrabold tracking-[0.3px]">Dashboard</span>
    <div class="group relative">
      <button id="tcs05-trigger" data-trigger type="button" aria-haspopup="menu" aria-expanded="false" aria-controls="tcs05-menu" class="flex items-center gap-1.75 min-h-11 pl-1.25 pr-2.5 rounded-full border border-tcs05-line2 bg-tcs05-surface cursor-pointer transition-[border-color,box-shadow] duration-200 hover:border-tcs05-line3 focus-visible:outline-none focus-visible:border-tcs05-acc focus-visible:shadow-[0_0_0_4px_color-mix(in_oklch,var(--color-tcs05-acc)_25%,transparent)]">
        <span class="grid place-items-center w-8.5 h-8.5 rounded-full bg-linear-[135deg,var(--color-tcs05-av1),var(--color-tcs05-av2)] text-white text-[13px] font-extrabold tracking-[0.5px]" aria-hidden="true">AM</span>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tcs05-mut [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-has-aria-expanded:rotate-180 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <div id="tcs05-menu" role="menu" aria-labelledby="tcs05-trigger" tabindex="-1" class="absolute top-[calc(100%+12px)] right-0 z-30 w-66.5 p-2 rounded-2xl border border-tcs05-line2 bg-tcs05-panel shadow-[0_30px_60px_-16px_oklch(0.08_0.01_265/0.75)] origin-top-right invisible opacity-0 scale-94 -translate-y-2 [transition:opacity_.2s,scale_.26s_var(--ease-tcs05),translate_.26s_var(--ease-tcs05),visibility_0s_.26s] group-has-aria-expanded:visible group-has-aria-expanded:opacity-100 group-has-aria-expanded:scale-100 group-has-aria-expanded:translate-y-0 group-has-aria-expanded:[transition:opacity_.2s,scale_.26s_var(--ease-tcs05),translate_.26s_var(--ease-tcs05),visibility_0s_0s] motion-reduce:transition-none">
        <div class="flex items-center gap-3 px-2.5 pt-2.5 pb-3">
          <span class="grid place-items-center w-11 h-11 rounded-full bg-linear-[135deg,var(--color-tcs05-av1),var(--color-tcs05-av2)] text-white text-base font-extrabold" aria-hidden="true">AM</span>
          <span class="flex flex-col min-w-0 leading-[1.35]"><b class="text-[14.5px]">Alex Morgan</b><small class="text-xs text-tcs05-mut truncate">[email protected]</small></span>
        </div>
        <div class="h-px mx-1 my-1.25 bg-tcs05-line" role="separator"></div>
        <button type="button" role="menuitem" class="flex w-full items-center gap-3 min-h-11 px-3 rounded-[10px] border-0 bg-transparent text-left font-tcs05-sans text-sm text-tcs05-ink2 cursor-pointer transition-colors duration-150 hover:bg-tcs05-hover focus-visible:bg-tcs05-hover focus-visible:outline-2 focus-visible:outline-tcs05-acc focus-visible:-outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-current [stroke-width:1.9] [stroke-linecap:round] [stroke-linejoin:round] opacity-85"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg>My Profile</button>
        <button type="button" role="menuitem" class="flex w-full items-center gap-3 min-h-11 px-3 rounded-[10px] border-0 bg-transparent text-left font-tcs05-sans text-sm text-tcs05-ink2 cursor-pointer transition-colors duration-150 hover:bg-tcs05-hover focus-visible:bg-tcs05-hover focus-visible:outline-2 focus-visible:outline-tcs05-acc focus-visible:-outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-current [stroke-width:1.9] [stroke-linecap:round] [stroke-linejoin:round] opacity-85"><circle cx="12" cy="12" r="3"/><path d="M19.4 13a7.6 7.6 0 0 0 0-2l2-1.5-2-3.4-2.4 1a7.6 7.6 0 0 0-1.7-1L14.9 3H9.1l-.4 3.1a7.6 7.6 0 0 0-1.7 1l-2.4-1-2 3.4L4.6 11a7.6 7.6 0 0 0 0 2l-2 1.5 2 3.4 2.4-1a7.6 7.6 0 0 0 1.7 1l.4 3.1h5.8l.4-3.1a7.6 7.6 0 0 0 1.7-1l2.4 1 2-3.4z"/></svg>Settings</button>
        <button type="button" role="menuitem" class="flex w-full items-center gap-3 min-h-11 px-3 rounded-[10px] border-0 bg-transparent text-left font-tcs05-sans text-sm text-tcs05-ink2 cursor-pointer transition-colors duration-150 hover:bg-tcs05-hover focus-visible:bg-tcs05-hover focus-visible:outline-2 focus-visible:outline-tcs05-acc focus-visible:-outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-current [stroke-width:1.9] [stroke-linecap:round] [stroke-linejoin:round] opacity-85"><rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 10h19M6 15h4"/></svg>Billing</button>
        <div class="h-px mx-1 my-1.25 bg-tcs05-line" role="separator"></div>
        <button type="button" role="menuitem" class="flex w-full items-center gap-3 min-h-11 px-3 rounded-[10px] border-0 bg-transparent text-left font-tcs05-sans text-sm text-tcs05-danger cursor-pointer transition-colors duration-150 hover:bg-[color-mix(in_oklch,var(--color-tcs05-danger)_14%,transparent)] focus-visible:bg-tcs05-hover focus-visible:outline-2 focus-visible:outline-tcs05-acc focus-visible:-outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-current [stroke-width:1.9] [stroke-linecap:round] [stroke-linejoin:round] opacity-85"><path d="M16 17l5-5-5-5M21 12H9M13 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h8"/></svg>Sign out</button>
      </div>
    </div>
  </div>
  <div class="grid gap-3.5 max-w-150 mx-auto px-6 py-10" aria-hidden="true">
    <div class="h-40 rounded-2xl bg-tcs05-surface border border-tcs05-line"></div>
    <div class="h-3 w-[72%] rounded-full bg-tcs05-line2"></div>
    <div class="h-3 w-[54%] rounded-full bg-tcs05-line2"></div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs05-bg: #0b0e16;
  --color-tcs05-bg: oklch(0.16 0.02 265);
  --color-tcs05-bar: #141622;
  --color-tcs05-bar: oklch(0.2 0.02 265);
  --color-tcs05-surface: #1b1f30;
  --color-tcs05-surface: oklch(0.24 0.02 265);
  --color-tcs05-panel: #161a29;
  --color-tcs05-panel: oklch(0.22 0.02 265);
  --color-tcs05-hover: #212639;
  --color-tcs05-hover: oklch(0.27 0.02 265);
  --color-tcs05-line: #262b3e;
  --color-tcs05-line: oklch(0.29 0.02 265);
  --color-tcs05-line2: #2c3145;
  --color-tcs05-line2: oklch(0.32 0.02 265);
  --color-tcs05-line3: #3d4460;
  --color-tcs05-line3: oklch(0.4 0.03 265);
  --color-tcs05-ink: #e7e9f3;
  --color-tcs05-ink: oklch(0.92 0.01 265);
  --color-tcs05-ink2: #d3d7e6;
  --color-tcs05-ink2: oklch(0.87 0.01 265);
  --color-tcs05-mut: #8990ad;
  --color-tcs05-mut: oklch(0.64 0.03 265);
  --color-tcs05-acc: #8b5cf6;
  --color-tcs05-acc: oklch(0.62 0.2 293);
  --color-tcs05-danger: #fb7185;
  --color-tcs05-danger: oklch(0.72 0.17 15);
  --color-tcs05-av1: #f43f5e;
  --color-tcs05-av1: oklch(0.65 0.22 15);
  --color-tcs05-av2: #8b5cf6;
  --color-tcs05-av2: oklch(0.62 0.2 293);
  --font-tcs05-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tcs05: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-05 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-05 .group').forEach(function (field) {
    if (field.dataset.bound) return; field.dataset.bound = '1';
    var btn = field.querySelector('[data-trigger]');
    var items = Array.prototype.slice.call(field.querySelectorAll('[role="menuitem"]'));
    function set(open, refocus) {
      btn.setAttribute('aria-expanded', String(open));
      if (open) items[0].focus();
      else if (refocus) btn.focus();
    }
    btn.addEventListener('click', function () { set(btn.getAttribute('aria-expanded') !== 'true'); });
    field.addEventListener('keydown', function (e) {
      if (btn.getAttribute('aria-expanded') !== 'true') {
        if (e.key === 'ArrowDown') { e.preventDefault(); set(true); }
        return;
      }
      var at = items.indexOf(document.activeElement);
      if (e.key === 'ArrowDown') { e.preventDefault(); items[(at + 1) % items.length].focus(); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); items[(at - 1 + items.length) % items.length].focus(); }
      else if (e.key === 'Home') { e.preventDefault(); items[0].focus(); }
      else if (e.key === 'End') { e.preventDefault(); items[items.length - 1].focus(); }
      else if (e.key === 'Escape') { e.preventDefault(); set(false, true); }
    });
    field.addEventListener('focusout', function () {
      requestAnimationFrame(function () {
        if (!field.contains(document.activeElement)) set(false);
      });
    });
    document.addEventListener('pointerdown', function (e) { if (!field.contains(e.target)) set(false); });
  });
})();
```
