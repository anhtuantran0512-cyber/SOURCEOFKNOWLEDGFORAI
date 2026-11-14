---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-mobile-bottom-navigation-bar-floating-hamburger-toggle/"
title: "Tailwind Mobile Bottom Navigation Bar with Floating Hamburger Toggle"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "The app-store staple: a four-tab bottom bar whose centre slot holds a raised floating hamburger sitting in a real curved notch cut from the bar with a CSS…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mobile Bottom Navigation Bar with Floating Hamburger Toggle
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-mobile-bottom-navigation-bar-floating-hamburger-toggle/

The app-store staple: a four-tab bottom bar whose centre slot holds a raised floating hamburger sitting in a real curved notch cut from the bar with a CSS mask &mdash; not a fake shadow trick. Tapping it lifts a bottom sheet. The tabs are a radio group styled with has-checked:, which is the utility that makes one-of-N view switching work with no script at all.
## HTML
```html
<section class="thb-21 w-full min-h-svh grid justify-center content-start bg-thb21-bg font-thb21-sans text-thb21-ink px-5 py-9" aria-label="Bottom navigation with floating hamburger demo">
  <div class="group relative w-[min(400px,88vw)] h-140 rounded-3xl overflow-hidden bg-thb21-bg border border-thb21-edge">
    <div class="grid gap-3.5 p-6" aria-hidden="true">
      <div class="h-45 rounded-[18px] bg-linear-[145deg,oklch(0.9_0.03_290),oklch(0.85_0.05_265)]"></div>
      <div class="h-2.75 w-[82%] rounded-full bg-thb21-line"></div>
      <div class="h-2.75 w-[64%] rounded-full bg-thb21-line"></div>
      <div class="h-2.75 w-[73%] rounded-full bg-thb21-line"></div>
    </div>
    <button type="button" tabindex="-1" aria-hidden="true" class="absolute inset-0 z-2 border-0 p-0 cursor-pointer opacity-0 invisible bg-[oklch(0.22_0.02_265/0.42)] [transition:opacity_.3s,visibility_0s_.3s] group-data-open:opacity-100 group-data-open:visible group-data-open:[transition:opacity_.3s,visibility_0s_0s]"></button>
    <div id="thb21-sheet" aria-label="Quick actions" class="absolute inset-x-2.5 bottom-24 z-3 px-3.5 pt-2.5 pb-4 rounded-[22px] bg-thb21-panel border border-thb21-edge shadow-[0_-18px_44px_-22px_oklch(0.25_0.04_270/0.5)] translate-y-[calc(100%+110px)] invisible [transition:translate_.45s_var(--ease-thb21),visibility_0s_.45s] group-data-open:translate-y-0 group-data-open:visible group-data-open:[transition:translate_.45s_var(--ease-thb21),visibility_0s_0s] motion-reduce:[transition:opacity_.15s,visibility_0s_.15s]">
      <i class="block w-9.5 h-[4.5px] mx-auto mt-0.5 mb-3 rounded-full bg-thb21-grab" aria-hidden="true"></i>
      <div class="grid grid-cols-2 gap-2.5">
        <a href="#new" style="--i:0" class="flex items-center gap-2.75 min-h-14 px-4 rounded-[14px] border border-thb21-edge bg-thb21-bg text-[13.5px] font-semibold text-thb21-ink no-underline opacity-0 translate-y-3 transition-[border-color,color,opacity,translate] duration-350 ease-thb21in hover:border-thb21-acc hover:text-thb21-acc focus-visible:border-thb21-acc focus-visible:text-thb21-acc focus-visible:outline-2 focus-visible:outline-thb21-acc focus-visible:outline-offset-2 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(100ms+var(--i)*40ms)] motion-reduce:translate-y-0 motion-reduce:duration-150">
          <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 shrink-0 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>New entry
        </a>
        <a href="#scan" style="--i:1" class="flex items-center gap-2.75 min-h-14 px-4 rounded-[14px] border border-thb21-edge bg-thb21-bg text-[13.5px] font-semibold text-thb21-ink no-underline opacity-0 translate-y-3 transition-[border-color,color,opacity,translate] duration-350 ease-thb21in hover:border-thb21-acc hover:text-thb21-acc focus-visible:border-thb21-acc focus-visible:text-thb21-acc focus-visible:outline-2 focus-visible:outline-thb21-acc focus-visible:outline-offset-2 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(100ms+var(--i)*40ms)] motion-reduce:translate-y-0 motion-reduce:duration-150">
          <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 shrink-0 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><path d="M4 8V5.5A1.5 1.5 0 0 1 5.5 4H8M16 4h2.5A1.5 1.5 0 0 1 20 5.5V8M20 16v2.5a1.5 1.5 0 0 1-1.5 1.5H16M8 20H5.5A1.5 1.5 0 0 1 4 18.5V16M4 12h16"/></svg>Scan
        </a>
        <a href="#send" style="--i:2" class="flex items-center gap-2.75 min-h-14 px-4 rounded-[14px] border border-thb21-edge bg-thb21-bg text-[13.5px] font-semibold text-thb21-ink no-underline opacity-0 translate-y-3 transition-[border-color,color,opacity,translate] duration-350 ease-thb21in hover:border-thb21-acc hover:text-thb21-acc focus-visible:border-thb21-acc focus-visible:text-thb21-acc focus-visible:outline-2 focus-visible:outline-thb21-acc focus-visible:outline-offset-2 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(100ms+var(--i)*40ms)] motion-reduce:translate-y-0 motion-reduce:duration-150">
          <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 shrink-0 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><path d="m4 11 16-7-7 16-2.5-6.5Z"/></svg>Send
        </a>
        <a href="#archive" style="--i:3" class="flex items-center gap-2.75 min-h-14 px-4 rounded-[14px] border border-thb21-edge bg-thb21-bg text-[13.5px] font-semibold text-thb21-ink no-underline opacity-0 translate-y-3 transition-[border-color,color,opacity,translate] duration-350 ease-thb21in hover:border-thb21-acc hover:text-thb21-acc focus-visible:border-thb21-acc focus-visible:text-thb21-acc focus-visible:outline-2 focus-visible:outline-thb21-acc focus-visible:outline-offset-2 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(100ms+var(--i)*40ms)] motion-reduce:translate-y-0 motion-reduce:duration-150">
          <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 shrink-0 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><rect x="3.5" y="4" width="17" height="5" rx="1.5"/><path d="M5.5 9v9.5h13V9M10 13h4"/></svg>Archive
        </a>
      </div>
    </div>
    <div class="absolute inset-x-2.5 bottom-2.5 z-4 h-18.5">
      <div class="absolute inset-0 drop-shadow-[0_14px_26px_oklch(0.3_0.03_265/0.28)]">
        <nav aria-label="Tabs" class="absolute inset-0 flex items-stretch rounded-[22px] bg-thb21-panel [mask:radial-gradient(circle_37px_at_50%_0,transparent_98%,black_100%)]">
          <label class="relative flex flex-1 flex-col items-center justify-center gap-0.75 rounded-[14px] cursor-pointer text-thb21-mut transition-[color] duration-200 hover:text-thb21-ink has-checked:text-thb21-acc has-focus-visible:outline-2 has-focus-visible:outline-thb21-acc has-focus-visible:-outline-offset-4">
            <input type="radio" name="thb21" checked class="absolute opacity-0 pointer-events-none">
            <svg viewBox="0 0 24 24" class="w-5.25 h-5.25 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round] transition-[translate] duration-250 ease-thb21pop" aria-hidden="true"><path d="M3 11.5 12 4l9 7.5"/><path d="M5.5 10v10h13V10"/></svg>
            <span class="text-[10px] font-semibold">Home</span>
            <i class="absolute bottom-1.75 w-1 h-1 rounded-full bg-thb21-acc scale-0 transition-[scale] duration-250 ease-thb21pop" aria-hidden="true"></i>
          </label>
          <label class="relative flex flex-1 flex-col items-center justify-center gap-0.75 rounded-[14px] cursor-pointer text-thb21-mut transition-[color] duration-200 hover:text-thb21-ink has-checked:text-thb21-acc has-focus-visible:outline-2 has-focus-visible:outline-thb21-acc has-focus-visible:-outline-offset-4">
            <input type="radio" name="thb21" class="absolute opacity-0 pointer-events-none">
            <svg viewBox="0 0 24 24" class="w-5.25 h-5.25 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round] transition-[translate] duration-250 ease-thb21pop" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
            <span class="text-[10px] font-semibold">Search</span>
            <i class="absolute bottom-1.75 w-1 h-1 rounded-full bg-thb21-acc scale-0 transition-[scale] duration-250 ease-thb21pop" aria-hidden="true"></i>
          </label>
          <span class="flex-none w-18" aria-hidden="true"></span>
          <label class="relative flex flex-1 flex-col items-center justify-center gap-0.75 rounded-[14px] cursor-pointer text-thb21-mut transition-[color] duration-200 hover:text-thb21-ink has-checked:text-thb21-acc has-focus-visible:outline-2 has-focus-visible:outline-thb21-acc has-focus-visible:-outline-offset-4">
            <input type="radio" name="thb21" class="absolute opacity-0 pointer-events-none">
            <svg viewBox="0 0 24 24" class="w-5.25 h-5.25 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round] transition-[translate] duration-250 ease-thb21pop" aria-hidden="true"><path d="M6 4h12v16l-6-4-6 4Z"/></svg>
            <span class="text-[10px] font-semibold">Saved</span>
            <i class="absolute bottom-1.75 w-1 h-1 rounded-full bg-thb21-acc scale-0 transition-[scale] duration-250 ease-thb21pop" aria-hidden="true"></i>
          </label>
          <label class="relative flex flex-1 flex-col items-center justify-center gap-0.75 rounded-[14px] cursor-pointer text-thb21-mut transition-[color] duration-200 hover:text-thb21-ink has-checked:text-thb21-acc has-focus-visible:outline-2 has-focus-visible:outline-thb21-acc has-focus-visible:-outline-offset-4">
            <input type="radio" name="thb21" class="absolute opacity-0 pointer-events-none">
            <svg viewBox="0 0 24 24" class="w-5.25 h-5.25 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round] transition-[translate] duration-250 ease-thb21pop" aria-hidden="true"><circle cx="12" cy="8.5" r="3.5"/><path d="M5 20a7 7 0 0 1 14 0"/></svg>
            <span class="text-[10px] font-semibold">Profile</span>
            <i class="absolute bottom-1.75 w-1 h-1 rounded-full bg-thb21-acc scale-0 transition-[scale] duration-250 ease-thb21pop" aria-hidden="true"></i>
          </label>
        </nav>
      </div>
      <button type="button" aria-expanded="false" aria-controls="thb21-sheet" aria-label="Open quick actions" class="absolute left-1/2 -top-6.5 -translate-x-1/2 grid place-items-center w-14 h-14 rounded-full border-0 bg-linear-[150deg,var(--color-thb21-acc),oklch(0.5_0.19_300)] text-white cursor-pointer shadow-[0_14px_28px_-10px_color-mix(in_oklch,var(--color-thb21-acc)_65%,transparent)] transition-[scale,box-shadow] duration-250 hover:scale-106 active:scale-93 focus-visible:outline-2 focus-visible:outline-thb21-acc focus-visible:outline-offset-3 motion-reduce:transition-none">
        <span class="relative block w-4.5 h-3" aria-hidden="true">
          <i class="absolute left-0 top-0 w-4.5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 group-data-open:translate-y-[5px] group-data-open:rotate-45 motion-reduce:transition-none"></i>
          <i class="absolute left-0 top-[5px] w-4.5 h-0.5 rounded-sm bg-current transition-[opacity] duration-200 group-data-open:opacity-0 motion-reduce:transition-none"></i>
          <i class="absolute left-0 top-2.5 w-4.5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 group-data-open:-translate-y-[5px] group-data-open:-rotate-45 motion-reduce:transition-none"></i>
        </span>
      </button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb21-bg: #f3f4f8;
  --color-thb21-bg: oklch(0.965 0.006 250);
  --color-thb21-panel: #ffffff;
  --color-thb21-panel: oklch(1 0 0);
  --color-thb21-edge: #e3e4ea;
  --color-thb21-edge: oklch(0.9 0.008 250);
  --color-thb21-line: #e6e7ed;
  --color-thb21-line: oklch(0.9 0.007 250);
  --color-thb21-grab: #d9dae1;
  --color-thb21-grab: oklch(0.87 0.008 250);
  --color-thb21-ink: #34374a;
  --color-thb21-ink: oklch(0.25 0.018 260);
  --color-thb21-mut: #7a7d90;
  --color-thb21-mut: oklch(0.56 0.014 260);
  --color-thb21-acc: #6b4de8;
  --color-thb21-acc: oklch(0.58 0.19 285);
  --font-thb21-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb21-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb21: cubic-bezier(0.32, 0.72, 0.28, 1);
  --ease-thb21in: cubic-bezier(0.2, 0.7, 0.2, 1);
  --ease-thb21pop: cubic-bezier(0.3, 1.4, 0.4, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-21 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.thb-21 > .group').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var fab = stage.querySelector('button[aria-controls="thb21-sheet"]'),
        scrim = stage.querySelector('button[aria-hidden="true"]');
    function set(open) {
      stage.toggleAttribute('data-open', open);
      fab.setAttribute('aria-expanded', String(open));
      fab.setAttribute('aria-label', open ? 'Close quick actions' : 'Open quick actions');
    }
    fab.addEventListener('click', function () { set(fab.getAttribute('aria-expanded') !== 'true'); });
    scrim.addEventListener('click', function () { set(false); });
    stage.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && stage.hasAttribute('data-open')) { set(false); fab.focus(); }
    });
  });
})();
```
