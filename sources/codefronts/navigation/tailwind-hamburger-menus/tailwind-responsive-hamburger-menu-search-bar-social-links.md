---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-responsive-hamburger-menu-search-bar-social-links/"
title: "Tailwind Responsive Hamburger Menu with Integrated Search Bar & Social Links"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "The publisher/e-commerce drawer that carries a whole header's worth of jobs &mdash; auto-focused search, nav with counts, a New badge, a social row and a…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Responsive Hamburger Menu with Integrated Search Bar & Social Links
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-responsive-hamburger-menu-search-bar-social-links/

The publisher/e-commerce drawer that carries a whole header's worth of jobs &mdash; auto-focused search, nav with counts, a New badge, a social row and a pinned newsletter CTA. The port's real content is one class list: grid grid-rows-[auto_1fr_auto] on the drawer plus min-h-0 overflow-auto on the middle row, which is the whole reason feature-rich drawers stop losing their footer.
## HTML
```html
<section class="thb-06 w-full min-h-svh grid justify-center content-start bg-thb06-bg font-thb06-sans text-thb06-ink px-5 py-9" aria-label="Hamburger menu with search and social links demo">
  <div class="group relative w-[min(400px,88vw)] h-140 rounded-3xl overflow-hidden bg-thb06-bg border border-thb06-edge">
    <header class="flex items-center gap-3 h-16.5 px-4.5 bg-thb06-panel border-b border-thb06-edge">
      <button type="button" aria-expanded="false" aria-controls="thb06-drawer" aria-label="Open menu" class="grid place-items-center w-11 h-11 -ml-2 rounded-xl border-0 bg-transparent text-thb06-ink cursor-pointer transition-[background] duration-200 hover:bg-thb06-hover focus-visible:outline-2 focus-visible:outline-thb06-acc focus-visible:outline-offset-2">
        <span class="relative block w-5 h-3.5" aria-hidden="true">
          <i class="absolute left-0 top-0 w-5 h-0.5 rounded-sm bg-current"></i>
          <i class="absolute left-0 top-1.5 w-5 h-0.5 rounded-sm bg-current"></i>
          <i class="absolute left-0 top-3 w-5 h-0.5 rounded-sm bg-current"></i>
        </span>
      </button>
      <span class="text-[17px] font-extrabold tracking-[0.14em]">KIOSK<i class="not-italic font-normal tracking-normal text-thb06-acc">daily</i></span>
      <span class="relative ml-auto text-thb06-ink" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4.5 7h15L18 20H6Z"/><path d="M8.5 7a3.5 3.5 0 0 1 7 0"/></svg>
        <b class="absolute -top-1.75 -right-2.25 px-1.5 py-px rounded-full bg-thb06-acc text-white text-[9.5px] font-bold">2</b>
      </span>
    </header>
    <div class="grid gap-3.25 p-4.5" aria-hidden="true">
      <div class="h-45 rounded-[14px] bg-linear-[145deg,oklch(0.9_0.03_50),oklch(0.85_0.055_25)]"></div>
      <div class="h-2.75 w-[86%] rounded-full bg-thb06-line"></div>
      <div class="h-2.75 w-[64%] rounded-full bg-thb06-line"></div>
    </div>
    <button type="button" tabindex="-1" aria-hidden="true" class="absolute inset-0 z-2 border-0 p-0 cursor-pointer opacity-0 invisible bg-[oklch(0.22_0.02_40/0.42)] backdrop-blur-[2px] [transition:opacity_.3s,visibility_0s_.3s] group-data-open:opacity-100 group-data-open:visible group-data-open:[transition:opacity_.3s,visibility_0s_0s]"></button>
    <aside id="thb06-drawer" aria-label="Menu" class="absolute inset-y-0 left-0 z-3 grid grid-rows-[auto_1fr_auto] w-[min(88%,330px)] bg-thb06-panel shadow-[24px_0_48px_-24px_oklch(0.25_0.03_40/0.45)] -translate-x-[102%] invisible [transition:translate_.42s_var(--ease-thb06),visibility_0s_.42s] group-data-open:translate-x-0 group-data-open:visible group-data-open:[transition:translate_.42s_var(--ease-thb06),visibility_0s_0s] motion-reduce:[transition:opacity_.15s,visibility_0s_.15s]">
      <div class="flex items-center gap-2.5 px-4 pt-4 pb-3">
        <form role="search" class="flex flex-1 items-center gap-2.25 min-h-11 px-3.5 rounded-xl border-[1.5px] border-thb06-edge text-thb06-mut transition-[border-color,color] duration-200 focus-within:border-thb06-acc focus-within:text-thb06-acc">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
          <input type="search" placeholder="Search stories, topics&hellip;" aria-label="Search" class="flex-1 min-w-0 border-0 outline-none bg-transparent font-thb06-sans text-sm text-thb06-ink">
        </form>
        <button type="button" aria-label="Close menu" class="grid place-items-center shrink-0 w-11 h-11 rounded-xl border-[1.5px] border-thb06-edge bg-thb06-panel text-thb06-ink cursor-pointer transition-[background] duration-200 hover:bg-thb06-hover focus-visible:outline-2 focus-visible:outline-thb06-acc focus-visible:outline-offset-2">
          <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg>
        </button>
      </div>
      <nav aria-label="Sections" class="flex flex-col min-h-0 overflow-auto overscroll-contain px-2.5 py-1">
        <a href="#latest" class="flex items-center justify-between gap-3 min-h-12.5 px-3 rounded-[11px] no-underline text-[15.5px] font-bold tracking-[-0.01em] text-thb06-ink transition-[background,color] duration-150 hover:bg-thb06-hover hover:text-thb06-acc focus-visible:outline-2 focus-visible:outline-thb06-acc focus-visible:-outline-offset-2">Latest<span class="text-[11.5px] font-semibold text-thb06-mut tabular-nums">128</span></a>
        <a href="#tech" class="flex items-center justify-between gap-3 min-h-12.5 px-3 rounded-[11px] no-underline text-[15.5px] font-bold tracking-[-0.01em] text-thb06-ink transition-[background,color] duration-150 hover:bg-thb06-hover hover:text-thb06-acc focus-visible:outline-2 focus-visible:outline-thb06-acc focus-visible:-outline-offset-2">Technology<span class="text-[11.5px] font-semibold text-thb06-mut tabular-nums">41</span></a>
        <a href="#design" class="flex items-center justify-between gap-3 min-h-12.5 px-3 rounded-[11px] no-underline text-[15.5px] font-bold tracking-[-0.01em] text-thb06-ink transition-[background,color] duration-150 hover:bg-thb06-hover hover:text-thb06-acc focus-visible:outline-2 focus-visible:outline-thb06-acc focus-visible:-outline-offset-2">Design<span class="text-[11.5px] font-semibold text-thb06-mut tabular-nums">27</span></a>
        <a href="#culture" class="flex items-center justify-between gap-3 min-h-12.5 px-3 rounded-[11px] no-underline text-[15.5px] font-bold tracking-[-0.01em] text-thb06-ink transition-[background,color] duration-150 hover:bg-thb06-hover hover:text-thb06-acc focus-visible:outline-2 focus-visible:outline-thb06-acc focus-visible:-outline-offset-2">Culture<b class="px-2 py-0.75 rounded-full bg-thb06-acc text-white text-[10px] font-extrabold tracking-[0.08em] uppercase">New</b></a>
        <a href="#podcasts" class="flex items-center justify-between gap-3 min-h-12.5 px-3 rounded-[11px] no-underline text-[15.5px] font-bold tracking-[-0.01em] text-thb06-ink transition-[background,color] duration-150 hover:bg-thb06-hover hover:text-thb06-acc focus-visible:outline-2 focus-visible:outline-thb06-acc focus-visible:-outline-offset-2">Podcasts<span class="text-[11.5px] font-semibold text-thb06-mut tabular-nums">12</span></a>
        <a href="#archive" class="flex items-center justify-between gap-3 min-h-12.5 px-3 rounded-[11px] no-underline text-[15.5px] font-bold tracking-[-0.01em] text-thb06-ink transition-[background,color] duration-150 hover:bg-thb06-hover hover:text-thb06-acc focus-visible:outline-2 focus-visible:outline-thb06-acc focus-visible:-outline-offset-2">Archive</a>
      </nav>
      <footer class="grid gap-3 px-4 pt-3.5 pb-4.5 border-t border-thb06-edge">
        <div class="flex gap-2">
          <a href="#x" aria-label="Follow on X" class="grid place-items-center w-11 h-11 rounded-xl border-[1.5px] border-thb06-edge text-thb06-ink transition-[border-color,color,translate] duration-200 hover:border-thb06-acc hover:text-thb06-acc hover:-translate-y-0.5 focus-visible:border-thb06-acc focus-visible:text-thb06-acc focus-visible:outline-2 focus-visible:outline-thb06-acc focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" class="w-4.5 h-4.5 fill-current" aria-hidden="true"><path d="M4 4l7.2 9.3L4.4 20h2.1l5.6-5.5L16.8 20H20l-7.5-9.7L18.9 4h-2.1l-5.2 5.1L7.2 4H4Z"/></svg></a>
          <a href="#instagram" aria-label="Follow on Instagram" class="grid place-items-center w-11 h-11 rounded-xl border-[1.5px] border-thb06-edge text-thb06-ink transition-[border-color,color,translate] duration-200 hover:border-thb06-acc hover:text-thb06-acc hover:-translate-y-0.5 focus-visible:border-thb06-acc focus-visible:text-thb06-acc focus-visible:outline-2 focus-visible:outline-thb06-acc focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" class="w-4.5 h-4.5 fill-current" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17.2" cy="6.8" r="1.3"/></svg></a>
          <a href="#youtube" aria-label="Subscribe on YouTube" class="grid place-items-center w-11 h-11 rounded-xl border-[1.5px] border-thb06-edge text-thb06-ink transition-[border-color,color,translate] duration-200 hover:border-thb06-acc hover:text-thb06-acc hover:-translate-y-0.5 focus-visible:border-thb06-acc focus-visible:text-thb06-acc focus-visible:outline-2 focus-visible:outline-thb06-acc focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" class="w-4.5 h-4.5 fill-current" aria-hidden="true"><rect x="2.5" y="6" width="19" height="12" rx="3.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M10.5 9.8v4.4l4-2.2Z"/></svg></a>
          <a href="#rss" aria-label="RSS feed" class="grid place-items-center w-11 h-11 rounded-xl border-[1.5px] border-thb06-edge text-thb06-ink transition-[border-color,color,translate] duration-200 hover:border-thb06-acc hover:text-thb06-acc hover:-translate-y-0.5 focus-visible:border-thb06-acc focus-visible:text-thb06-acc focus-visible:outline-2 focus-visible:outline-thb06-acc focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" class="w-4.5 h-4.5 fill-current" aria-hidden="true"><path d="M5 19a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"/><path d="M4 11a9 9 0 0 1 9 9M4 5a15 15 0 0 1 15 15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></a>
        </div>
        <button type="button" class="min-h-12 rounded-xl border-0 bg-thb06-ink font-thb06-sans text-sm font-bold text-thb06-bg cursor-pointer transition-[background] duration-200 hover:bg-thb06-acc focus-visible:outline-2 focus-visible:outline-thb06-acc focus-visible:outline-offset-2">Get the newsletter</button>
      </footer>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb06-bg: #fbfaf7;
  --color-thb06-bg: oklch(0.975 0.006 70);
  --color-thb06-panel: #ffffff;
  --color-thb06-panel: oklch(1 0 0);
  --color-thb06-hover: #f4f2ed;
  --color-thb06-hover: oklch(0.96 0.008 70);
  --color-thb06-edge: #e3e0d9;
  --color-thb06-edge: oklch(0.89 0.01 70);
  --color-thb06-line: #e7e4dd;
  --color-thb06-line: oklch(0.9 0.008 70);
  --color-thb06-ink: #35302b;
  --color-thb06-ink: oklch(0.23 0.015 50);
  --color-thb06-mut: #7b7469;
  --color-thb06-mut: oklch(0.54 0.015 50);
  --color-thb06-acc: #cf3d24;
  --color-thb06-acc: oklch(0.6 0.19 25);
  --font-thb06-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb06-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb06: cubic-bezier(0.32, 0.72, 0.28, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-06 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.thb-06 > .group').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var btn = stage.querySelector('button[aria-controls="thb06-drawer"]'),
        scrim = stage.querySelector('button[aria-hidden="true"]'),
        close = stage.querySelector('button[aria-label="Close menu"]'),
        input = stage.querySelector('input[type="search"]');
    function set(open) {
      stage.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      if (open) input.focus({ preventScroll: true }); else btn.focus();
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
