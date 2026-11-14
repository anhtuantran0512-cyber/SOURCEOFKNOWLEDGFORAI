---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-slide-in-off-canvas-drawer-dimmed-backdrop-overlay/"
title: "Tailwind Slide-In Off-Canvas Drawer with Dimmed Backdrop Overlay"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "The app-drawer everyone means when they say &ldquo;hamburger menu&rdquo;: a right-hand panel that slides in on translate-x (never on offsets), over a scrim…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Slide-In Off-Canvas Drawer with Dimmed Backdrop Overlay
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-slide-in-off-canvas-drawer-dimmed-backdrop-overlay/

The app-drawer everyone means when they say &ldquo;hamburger menu&rdquo;: a right-hand panel that slides in on translate-x (never on offsets), over a scrim that dims and blurs the page behind it. In utilities the drawer and the scrim each carry their own closed and open geometry, and the scrim stays a real <button> &mdash; so click-outside-to-close needs no document listener.
## HTML
```html
<section class="thb-04 w-full min-h-svh grid justify-center content-start bg-thb04-bg font-thb04-sans text-thb04-ink px-5 py-9" aria-label="Off-canvas drawer with dimmed backdrop demo">
  <div class="group relative w-[min(400px,88vw)] h-135 rounded-3xl overflow-hidden bg-thb04-bg border border-thb04-edge shadow-[0_30px_60px_-35px_oklch(0.35_0.04_50/0.4)]">
    <header class="flex items-center justify-between h-17 pl-5.5 pr-3.5 bg-thb04-panel border-b border-thb04-edge">
      <span class="flex items-center gap-2.25 text-[15px] font-bold">
        <i class="w-4.75 h-4.75 rounded-md bg-[conic-gradient(from_200deg,var(--color-thb04-acc),oklch(0.75_0.12_85))]" aria-hidden="true"></i>Northwind
      </span>
      <button type="button" aria-expanded="false" aria-controls="thb04-drawer" aria-label="Open menu" class="group/btn grid place-items-center w-11 h-11 rounded-xl border-0 bg-transparent text-thb04-ink cursor-pointer transition-[background] duration-200 hover:bg-thb04-hover focus-visible:outline-2 focus-visible:outline-thb04-acc focus-visible:outline-offset-2">
        <span class="relative block w-5 h-3.5" aria-hidden="true">
          <i class="absolute right-0 top-0 w-5 h-0.5 rounded-sm bg-current transition-[width] duration-250"></i>
          <i class="absolute right-0 top-1.5 w-3.5 h-0.5 rounded-sm bg-current transition-[width] duration-250 group-hover/btn:w-5"></i>
          <i class="absolute right-0 top-3 w-5 h-0.5 rounded-sm bg-current transition-[width] duration-250"></i>
        </span>
      </button>
    </header>
    <div class="grid gap-3.5 px-5.5 py-5" aria-hidden="true">
      <div class="h-37.5 rounded-2xl bg-linear-[140deg,oklch(0.92_0.03_60),oklch(0.88_0.05_35)]"></div>
      <div class="flex gap-3">
        <span class="flex-1 h-18 rounded-[13px] bg-thb04-panel border border-thb04-edge"></span>
        <span class="flex-1 h-18 rounded-[13px] bg-thb04-panel border border-thb04-edge"></span>
      </div>
      <div class="h-2.75 w-[88%] rounded-full bg-thb04-line"></div>
      <div class="h-2.75 w-[70%] rounded-full bg-thb04-line"></div>
      <div class="h-2.75 w-[79%] rounded-full bg-thb04-line"></div>
    </div>
    <button type="button" tabindex="-1" aria-hidden="true" class="absolute inset-0 z-2 border-0 p-0 cursor-pointer opacity-0 invisible bg-[oklch(0.25_0.02_50/0.45)] backdrop-blur-[3px] [transition:opacity_.35s,visibility_0s_.35s] group-data-open:opacity-100 group-data-open:visible group-data-open:[transition:opacity_.35s,visibility_0s_0s]"></button>
    <aside id="thb04-drawer" aria-label="Menu" class="absolute inset-y-0 right-0 z-3 flex flex-col w-[min(84%,320px)] bg-thb04-panel shadow-[-24px_0_48px_-24px_oklch(0.25_0.03_50/0.5)] translate-x-full invisible [transition:translate_.4s_var(--ease-thb04),visibility_0s_.4s] group-data-open:translate-x-0 group-data-open:visible group-data-open:[transition:translate_.4s_var(--ease-thb04),visibility_0s_0s] motion-reduce:[transition:opacity_.15s,visibility_0s_.15s]">
      <header class="flex items-center justify-between pt-4.5 pb-3.5 pl-5.5 pr-3.5">
        <b class="text-base font-bold tracking-[-0.01em]">Menu</b>
        <button type="button" aria-label="Close menu" class="grid place-items-center w-10 h-10 rounded-[11px] border border-thb04-edge bg-thb04-panel text-thb04-ink cursor-pointer transition-[background,rotate] duration-300 hover:bg-thb04-hover hover:rotate-90 focus-visible:outline-2 focus-visible:outline-thb04-acc focus-visible:outline-offset-2 motion-reduce:transition-none">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg>
        </button>
      </header>
      <nav aria-label="Primary" class="flex flex-col gap-0.75 px-3 py-1.5 overflow-auto overscroll-contain">
        <a href="#home" aria-current="page" style="--i:0" class="flex items-center gap-3.25 min-h-12 px-3 rounded-xl no-underline text-[14.5px] font-semibold text-thb04-mut opacity-0 translate-x-4 transition-[background,color,opacity,translate] duration-350 ease-thb04in hover:bg-thb04-hover hover:text-thb04-ink focus-visible:text-thb04-ink focus-visible:outline-2 focus-visible:outline-thb04-acc focus-visible:-outline-offset-2 aria-current:text-thb04-acc aria-current:bg-[color-mix(in_oklch,var(--color-thb04-acc)_9%,transparent)] group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(120ms+var(--i)*45ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
          <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 shrink-0 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><path d="M3 11.5 12 4l9 7.5"/><path d="M5.5 10v10h13V10"/></svg>Home
        </a>
        <a href="#orders" style="--i:1" class="flex items-center gap-3.25 min-h-12 px-3 rounded-xl no-underline text-[14.5px] font-semibold text-thb04-mut opacity-0 translate-x-4 transition-[background,color,opacity,translate] duration-350 ease-thb04in hover:bg-thb04-hover hover:text-thb04-ink focus-visible:text-thb04-ink focus-visible:outline-2 focus-visible:outline-thb04-acc focus-visible:-outline-offset-2 group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(120ms+var(--i)*45ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
          <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 shrink-0 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><path d="M4.5 7h15L18 20H6Z"/><path d="M8.5 7a3.5 3.5 0 0 1 7 0"/></svg>Orders
          <b class="ml-auto px-2 py-0.5 rounded-full bg-thb04-acc text-white text-[11px] font-bold">3</b>
        </a>
        <a href="#saved" style="--i:2" class="flex items-center gap-3.25 min-h-12 px-3 rounded-xl no-underline text-[14.5px] font-semibold text-thb04-mut opacity-0 translate-x-4 transition-[background,color,opacity,translate] duration-350 ease-thb04in hover:bg-thb04-hover hover:text-thb04-ink focus-visible:text-thb04-ink focus-visible:outline-2 focus-visible:outline-thb04-acc focus-visible:-outline-offset-2 group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(120ms+var(--i)*45ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
          <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 shrink-0 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 6.6 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10Z"/></svg>Saved
        </a>
        <a href="#account" style="--i:3" class="flex items-center gap-3.25 min-h-12 px-3 rounded-xl no-underline text-[14.5px] font-semibold text-thb04-mut opacity-0 translate-x-4 transition-[background,color,opacity,translate] duration-350 ease-thb04in hover:bg-thb04-hover hover:text-thb04-ink focus-visible:text-thb04-ink focus-visible:outline-2 focus-visible:outline-thb04-acc focus-visible:-outline-offset-2 group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(120ms+var(--i)*45ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
          <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 shrink-0 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><circle cx="12" cy="8.5" r="3.5"/><path d="M5 20a7 7 0 0 1 14 0"/></svg>Account
        </a>
        <a href="#help" style="--i:4" class="flex items-center gap-3.25 min-h-12 px-3 rounded-xl no-underline text-[14.5px] font-semibold text-thb04-mut opacity-0 translate-x-4 transition-[background,color,opacity,translate] duration-350 ease-thb04in hover:bg-thb04-hover hover:text-thb04-ink focus-visible:text-thb04-ink focus-visible:outline-2 focus-visible:outline-thb04-acc focus-visible:-outline-offset-2 group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(120ms+var(--i)*45ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
          <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 shrink-0 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M9.6 9.4a2.5 2.5 0 1 1 3.4 3l-1 .8v1.3"/><path d="M12 17.5v.01"/></svg>Help centre
        </a>
      </nav>
      <footer class="mt-auto px-5.5 py-4 border-t border-thb04-edge">
        <button type="button" class="w-full min-h-11 rounded-xl border border-thb04-edge bg-thb04-bg font-thb04-sans text-[13.5px] font-semibold text-thb04-ink cursor-pointer transition-[border-color] duration-200 hover:border-thb04-edge2 focus-visible:outline-2 focus-visible:outline-thb04-acc focus-visible:outline-offset-2">Sign out</button>
      </footer>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb04-bg: #fafaf7;
  --color-thb04-bg: oklch(0.98 0.004 80);
  --color-thb04-panel: #ffffff;
  --color-thb04-panel: oklch(1 0 0);
  --color-thb04-hover: #f2f1ec;
  --color-thb04-hover: oklch(0.955 0.007 80);
  --color-thb04-edge: #e5e3dc;
  --color-thb04-edge: oklch(0.9 0.008 80);
  --color-thb04-edge2: #b9b4a8;
  --color-thb04-edge2: oklch(0.75 0.02 60);
  --color-thb04-line: #e8e6df;
  --color-thb04-line: oklch(0.91 0.006 80);
  --color-thb04-ink: #3a3630;
  --color-thb04-ink: oklch(0.25 0.015 60);
  --color-thb04-mut: #7d7669;
  --color-thb04-mut: oklch(0.55 0.015 60);
  --color-thb04-acc: #c2643a;
  --color-thb04-acc: oklch(0.62 0.15 40);
  --font-thb04-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb04-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb04: cubic-bezier(0.32, 0.72, 0.28, 1);
  --ease-thb04in: cubic-bezier(0.2, 0.7, 0.2, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-04 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.thb-04 > .group').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var btn = stage.querySelector('button[aria-controls="thb04-drawer"]'),
        scrim = stage.querySelector('button[aria-hidden="true"]'),
        close = stage.querySelector('button[aria-label="Close menu"]');
    function set(open) {
      stage.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      if (open) close.focus(); else btn.focus();
    }
    btn.addEventListener('click', function () { set(true); });
    scrim.addEventListener('click', function () { set(false); });
    close.addEventListener('click', function () { set(false); });
    stage.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && stage.hasAttribute('data-open')) set(false);
    });
  });
})();
```
