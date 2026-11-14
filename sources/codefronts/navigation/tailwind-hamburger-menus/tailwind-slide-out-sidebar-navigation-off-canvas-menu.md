---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-slide-out-sidebar-navigation-off-canvas-menu/"
title: "Tailwind Slide Out Sidebar Navigation / Off Canvas Menu"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "The workhorse app sidebar, structured the way real products need it: grouped sections, icon+label rows with an aria-current-driven indicator bar, shortcut…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Slide Out Sidebar Navigation / Off Canvas Menu
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-slide-out-sidebar-navigation-off-canvas-menu/

The workhorse app sidebar, structured the way real products need it: grouped sections, icon+label rows with an aria-current-driven indicator bar, shortcut hints, and a user card pinned to the bottom. The slide engine is demo 04's; what this demo teaches is interior architecture &mdash; and in utilities the active-state contract (aria-current:) is visible on the row itself.
## HTML
```html
<section class="thb-12 w-full min-h-svh grid justify-center content-start bg-thb12-bg font-thb12-sans text-thb12-ink px-5 py-9" aria-label="Slide out sidebar navigation demo">
  <div class="group relative w-[min(420px,88vw)] h-140 rounded-3xl overflow-hidden bg-thb12-bg border border-thb12-edge" style="--w:288px">
    <header class="flex items-center gap-3 h-16 px-4 bg-white border-b border-thb12-edge">
      <button type="button" aria-expanded="false" aria-controls="thb12-drawer" aria-label="Open navigation" class="group/btn grid place-items-center w-11 h-11 rounded-xl border-0 bg-transparent text-thb12-ink cursor-pointer transition-[background] duration-200 hover:bg-thb12-hover focus-visible:outline-2 focus-visible:outline-thb12-acc focus-visible:outline-offset-2">
        <span class="relative block w-4.75 h-3.25" aria-hidden="true">
          <i class="absolute left-0 top-0 w-4.75 h-0.5 rounded-sm bg-current transition-[width] duration-250"></i>
          <i class="absolute left-0 top-[5.5px] w-3.25 h-0.5 rounded-sm bg-current transition-[width] duration-250 group-hover/btn:w-4.75"></i>
          <i class="absolute left-0 top-[11px] w-4 h-0.5 rounded-sm bg-current transition-[width] duration-250 group-hover/btn:w-4.75"></i>
        </span>
      </button>
      <strong class="text-[15px] font-bold tracking-[-0.01em]">Tessera</strong>
      <span class="text-[13px] text-thb12-mut" aria-hidden="true">/ Q3 planning</span>
    </header>
    <div class="grid gap-3.25 p-4.5" aria-hidden="true">
      <div class="h-40 rounded-[15px] bg-linear-[145deg,oklch(0.92_0.02_190),oklch(0.88_0.035_165)]"></div>
      <div class="flex gap-3">
        <span class="flex-1 h-19.5 rounded-[13px] bg-white border border-thb12-edge"></span>
        <span class="flex-1 h-19.5 rounded-[13px] bg-white border border-thb12-edge"></span>
      </div>
      <div class="h-2.75 w-[78%] rounded-full bg-thb12-line"></div>
      <div class="h-2.75 w-[62%] rounded-full bg-thb12-line"></div>
    </div>
    <button type="button" tabindex="-1" aria-hidden="true" class="absolute inset-0 z-2 border-0 p-0 cursor-pointer opacity-0 invisible bg-[oklch(0.2_0.02_260/0.4)] [transition:opacity_.32s,visibility_0s_.32s] group-data-open:opacity-100 group-data-open:visible group-data-open:[transition:opacity_.32s,visibility_0s_0s]"></button>
    <aside id="thb12-drawer" aria-label="Navigation" class="absolute inset-y-0 left-0 z-3 grid grid-rows-[auto_1fr_auto] w-[min(88%,var(--w))] bg-thb12-dark text-thb12-dink shadow-[24px_0_48px_-22px_oklch(0.15_0.03_262/0.6)] -translate-x-[102%] invisible [transition:translate_.42s_var(--ease-thb12),visibility_0s_.42s] group-data-open:translate-x-0 group-data-open:visible group-data-open:[transition:translate_.42s_var(--ease-thb12),visibility_0s_0s] motion-reduce:[transition:opacity_.15s,visibility_0s_.15s]">
      <header class="flex items-center gap-2.5 pt-4.5 pb-3.5 pl-4.5 pr-3.5">
        <span class="grid place-items-center w-7 h-7 rounded-[9px] bg-linear-[140deg,var(--color-thb12-acc),oklch(0.6_0.12_210)] text-[13px] font-extrabold text-thb12-dark" aria-hidden="true">T</span>
        <b class="text-[15px] font-bold">Tessera</b>
        <button type="button" aria-label="Close navigation" class="grid place-items-center ml-auto w-9.5 h-9.5 rounded-[10px] border border-thb12-dedge bg-transparent text-thb12-dmut cursor-pointer transition-[color,border-color] duration-200 hover:text-thb12-dink hover:border-thb12-dedge2 focus-visible:outline-2 focus-visible:outline-thb12-acc focus-visible:outline-offset-2">
          <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg>
        </button>
      </header>
      <nav aria-label="Primary" class="min-h-0 overflow-auto overscroll-contain px-3 pt-1.5 pb-3.5">
        <div style="--g:0" class="[&+div]:mt-4.5">
          <span class="block px-2.5 pb-1.75 font-thb12-mono text-[10px] font-bold tracking-[0.14em] uppercase text-thb12-dcap">Workspace</span>
          <a href="#board" aria-current="page" style="--g:0" class="relative flex items-center gap-3 min-h-11 pl-3.5 pr-2.5 rounded-[10px] no-underline text-[13.5px] font-semibold text-thb12-dmut opacity-0 -translate-x-3.5 transition-[background,color,opacity,translate] duration-350 ease-thb12 hover:bg-[oklch(1_0_0/0.06)] hover:text-thb12-dink focus-visible:text-thb12-dink focus-visible:outline-2 focus-visible:outline-thb12-acc focus-visible:-outline-offset-2 aria-current:text-thb12-dink aria-current:bg-[oklch(1_0_0/0.07)] group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(100ms+var(--g)*60ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
            <span class="absolute left-0.5 top-[20%] w-[3.5px] h-[60%] rounded-full bg-thb12-acc scale-y-0 transition-[scale] duration-250 aria-current:scale-y-100" aria-hidden="true"></span>
            <svg viewBox="0 0 24 24" class="w-4.5 h-4.5 shrink-0 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round] aria-current:stroke-thb12-acc" aria-hidden="true"><rect x="3.5" y="3.5" width="7.5" height="10" rx="1.5"/><rect x="13" y="3.5" width="7.5" height="6" rx="1.5"/><rect x="13" y="11.5" width="7.5" height="9" rx="1.5"/><rect x="3.5" y="15.5" width="7.5" height="5" rx="1.5"/></svg>Board
            <kbd class="ml-auto px-1.5 py-0.5 rounded-[5px] border border-thb12-dedge font-thb12-mono text-[10px] font-semibold text-thb12-dcap" aria-hidden="true">&#8984;1</kbd>
          </a>
          <a href="#timeline" style="--g:0" class="relative flex items-center gap-3 min-h-11 pl-3.5 pr-2.5 rounded-[10px] no-underline text-[13.5px] font-semibold text-thb12-dmut opacity-0 -translate-x-3.5 transition-[background,color,opacity,translate] duration-350 ease-thb12 hover:bg-[oklch(1_0_0/0.06)] hover:text-thb12-dink focus-visible:text-thb12-dink focus-visible:outline-2 focus-visible:outline-thb12-acc focus-visible:-outline-offset-2 group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(100ms+var(--g)*60ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
            <svg viewBox="0 0 24 24" class="w-4.5 h-4.5 shrink-0 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><path d="M3.5 6h11M3.5 12h17M3.5 18h8"/><circle cx="18" cy="6" r="2"/><circle cx="15" cy="18" r="2"/></svg>Timeline
            <kbd class="ml-auto px-1.5 py-0.5 rounded-[5px] border border-thb12-dedge font-thb12-mono text-[10px] font-semibold text-thb12-dcap" aria-hidden="true">&#8984;2</kbd>
          </a>
          <a href="#backlog" style="--g:0" class="relative flex items-center gap-3 min-h-11 pl-3.5 pr-2.5 rounded-[10px] no-underline text-[13.5px] font-semibold text-thb12-dmut opacity-0 -translate-x-3.5 transition-[background,color,opacity,translate] duration-350 ease-thb12 hover:bg-[oklch(1_0_0/0.06)] hover:text-thb12-dink focus-visible:text-thb12-dink focus-visible:outline-2 focus-visible:outline-thb12-acc focus-visible:-outline-offset-2 group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(100ms+var(--g)*60ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
            <svg viewBox="0 0 24 24" class="w-4.5 h-4.5 shrink-0 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/><circle cx="4" cy="6" r="1.4"/><circle cx="4" cy="12" r="1.4"/><circle cx="4" cy="18" r="1.4"/></svg>Backlog
            <b class="ml-auto px-1.75 py-0.5 rounded-full bg-thb12-acc text-thb12-dark text-[10.5px] font-bold">24</b>
          </a>
        </div>
        <div style="--g:1" class="[&+div]:mt-4.5">
          <span class="block px-2.5 pb-1.75 font-thb12-mono text-[10px] font-bold tracking-[0.14em] uppercase text-thb12-dcap">Library</span>
          <a href="#docs" style="--g:1" class="relative flex items-center gap-3 min-h-11 pl-3.5 pr-2.5 rounded-[10px] no-underline text-[13.5px] font-semibold text-thb12-dmut opacity-0 -translate-x-3.5 transition-[background,color,opacity,translate] duration-350 ease-thb12 hover:bg-[oklch(1_0_0/0.06)] hover:text-thb12-dink focus-visible:text-thb12-dink focus-visible:outline-2 focus-visible:outline-thb12-acc focus-visible:-outline-offset-2 group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(100ms+var(--g)*60ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
            <svg viewBox="0 0 24 24" class="w-4.5 h-4.5 shrink-0 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><path d="M5.5 4h9l4 4v12h-13Z"/><path d="M14 4v4.5h4.5"/></svg>Documents
          </a>
          <a href="#assets" style="--g:1" class="relative flex items-center gap-3 min-h-11 pl-3.5 pr-2.5 rounded-[10px] no-underline text-[13.5px] font-semibold text-thb12-dmut opacity-0 -translate-x-3.5 transition-[background,color,opacity,translate] duration-350 ease-thb12 hover:bg-[oklch(1_0_0/0.06)] hover:text-thb12-dink focus-visible:text-thb12-dink focus-visible:outline-2 focus-visible:outline-thb12-acc focus-visible:-outline-offset-2 group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(100ms+var(--g)*60ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
            <svg viewBox="0 0 24 24" class="w-4.5 h-4.5 shrink-0 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><rect x="3.5" y="5" width="17" height="14" rx="2"/><circle cx="9" cy="10.5" r="1.8"/><path d="m3.5 16.5 5-4 4 3.5 3-2.5 5 3.5"/></svg>Assets
          </a>
          <a href="#reports" style="--g:1" class="relative flex items-center gap-3 min-h-11 pl-3.5 pr-2.5 rounded-[10px] no-underline text-[13.5px] font-semibold text-thb12-dmut opacity-0 -translate-x-3.5 transition-[background,color,opacity,translate] duration-350 ease-thb12 hover:bg-[oklch(1_0_0/0.06)] hover:text-thb12-dink focus-visible:text-thb12-dink focus-visible:outline-2 focus-visible:outline-thb12-acc focus-visible:-outline-offset-2 group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(100ms+var(--g)*60ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
            <svg viewBox="0 0 24 24" class="w-4.5 h-4.5 shrink-0 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><path d="M5 20V9M12 20V4M19 20v-7"/></svg>Reports
          </a>
        </div>
        <div style="--g:2">
          <span class="block px-2.5 pb-1.75 font-thb12-mono text-[10px] font-bold tracking-[0.14em] uppercase text-thb12-dcap">Support</span>
          <a href="#help" style="--g:2" class="relative flex items-center gap-3 min-h-11 pl-3.5 pr-2.5 rounded-[10px] no-underline text-[13.5px] font-semibold text-thb12-dmut opacity-0 -translate-x-3.5 transition-[background,color,opacity,translate] duration-350 ease-thb12 hover:bg-[oklch(1_0_0/0.06)] hover:text-thb12-dink focus-visible:text-thb12-dink focus-visible:outline-2 focus-visible:outline-thb12-acc focus-visible:-outline-offset-2 group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(100ms+var(--g)*60ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
            <svg viewBox="0 0 24 24" class="w-4.5 h-4.5 shrink-0 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M9.6 9.4a2.5 2.5 0 1 1 3.4 3l-1 .8v1.3M12 17.5v.01"/></svg>Help &amp; docs
          </a>
          <a href="#invite" style="--g:2" class="relative flex items-center gap-3 min-h-11 pl-3.5 pr-2.5 rounded-[10px] no-underline text-[13.5px] font-semibold text-thb12-dmut opacity-0 -translate-x-3.5 transition-[background,color,opacity,translate] duration-350 ease-thb12 hover:bg-[oklch(1_0_0/0.06)] hover:text-thb12-dink focus-visible:text-thb12-dink focus-visible:outline-2 focus-visible:outline-thb12-acc focus-visible:-outline-offset-2 group-data-open:opacity-100 group-data-open:translate-x-0 group-data-open:[transition-delay:calc(100ms+var(--g)*60ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
            <svg viewBox="0 0 24 24" class="w-4.5 h-4.5 shrink-0 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><circle cx="10" cy="8.5" r="3.5"/><path d="M3.5 20a6.5 6.5 0 0 1 13 0M18 8v6M15 11h6"/></svg>Invite team
          </a>
        </div>
      </nav>
      <footer class="flex items-center gap-2.75 px-3.5 py-3.25 border-t border-thb12-dedge">
        <span class="grid place-items-center w-8.5 h-8.5 rounded-full bg-linear-[140deg,oklch(0.75_0.12_90),var(--color-thb12-acc)] text-[11.5px] font-bold text-thb12-dark" aria-hidden="true">MK</span>
        <span class="grid leading-tight">
          <b class="text-[13px] font-bold">Mara Kade</b>
          <small class="text-[11px] text-thb12-dmut">[email protected]</small>
        </span>
        <button type="button" aria-label="Account options" class="ml-auto w-9 h-9 rounded-[9px] border-0 bg-transparent text-thb12-dmut text-base cursor-pointer transition-[background,color] duration-200 hover:bg-[oklch(1_0_0/0.07)] hover:text-thb12-dink focus-visible:outline-2 focus-visible:outline-thb12-acc focus-visible:outline-offset-2">&ctdot;</button>
      </footer>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb12-bg: #fafafc;
  --color-thb12-bg: oklch(0.975 0.004 250);
  --color-thb12-edge: #e3e4ea;
  --color-thb12-edge: oklch(0.9 0.008 250);
  --color-thb12-line: #e8e9ee;
  --color-thb12-line: oklch(0.91 0.006 250);
  --color-thb12-hover: #eff0f4;
  --color-thb12-hover: oklch(0.95 0.006 250);
  --color-thb12-ink: #33374a;
  --color-thb12-ink: oklch(0.25 0.015 255);
  --color-thb12-mut: #757a8b;
  --color-thb12-mut: oklch(0.55 0.012 255);
  --color-thb12-dark: #2a2d3d;
  --color-thb12-dark: oklch(0.21 0.022 262);
  --color-thb12-dedge: #43475c;
  --color-thb12-dedge: oklch(0.3 0.025 262);
  --color-thb12-dedge2: #62677f;
  --color-thb12-dedge2: oklch(0.42 0.03 262);
  --color-thb12-dink: #eaebf1;
  --color-thb12-dink: oklch(0.93 0.008 260);
  --color-thb12-dmut: #a1a5b6;
  --color-thb12-dmut: oklch(0.66 0.02 260);
  --color-thb12-dcap: #737890;
  --color-thb12-dcap: oklch(0.52 0.02 262);
  --color-thb12-acc: #4ecfc0;
  --color-thb12-acc: oklch(0.73 0.14 175);
  --font-thb12-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb12-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb12: cubic-bezier(0.32, 0.72, 0.28, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-12 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.thb-12 > .group').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var btn = stage.querySelector('button[aria-controls="thb12-drawer"]'),
        scrim = stage.querySelector('button[aria-hidden="true"]'),
        close = stage.querySelector('button[aria-label="Close navigation"]');
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
