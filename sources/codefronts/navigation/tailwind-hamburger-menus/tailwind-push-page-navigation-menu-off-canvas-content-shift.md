---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-push-page-navigation-menu-off-canvas-content-shift/"
title: "Tailwind Push Page Navigation Menu (Off-Canvas Content Shift)"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "Instead of layering a drawer OVER the page, the whole canvas glides aside to reveal a menu resting beneath it &mdash; the page becomes a sheet you slide off…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Push Page Navigation Menu (Off-Canvas Content Shift)
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-push-page-navigation-menu-off-canvas-content-shift/

Instead of layering a drawer OVER the page, the whole canvas glides aside to reveal a menu resting beneath it &mdash; the page becomes a sheet you slide off a shelf. One element transitions; the menu never moves. In utilities the canvas's entire open state (push, 6% shrink, corner radius, deep shadow) is four group-data-open: classes sitting next to its resting state.
## HTML
```html
<section class="thb-08 w-full min-h-svh grid justify-center content-start bg-thb08-bg font-thb08-sans text-thb08-ink px-5 py-9" aria-label="Push page off-canvas navigation demo">
  <div class="group relative w-[min(400px,88vw)] h-135 rounded-3xl overflow-hidden border border-thb08-edge bg-thb08-bg bg-[radial-gradient(120%_100%_at_0%_100%,oklch(0.26_0.06_300/0.6),transparent_55%)]" style="--w:270px">
    <nav id="thb08-menu" aria-label="Site" class="absolute inset-y-0 left-0 w-[var(--w)] flex flex-col gap-1 px-5.5 py-7.5 text-thb08-menuink">
      <b style="--i:0" class="mb-4.5 text-[17px] font-bold tracking-[-0.01em] -translate-x-6.5 opacity-40 transition-[translate,opacity] duration-500 ease-thb08 group-data-open:translate-x-0 group-data-open:opacity-100 group-data-open:[transition-delay:calc(var(--i)*35ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">Good evening, Ash</b>
      <a href="#today" aria-current="page" style="--i:1" class="flex items-center gap-3 min-h-11.5 -mx-3 px-3 rounded-xl no-underline text-[14.5px] font-semibold text-thb08-menumut -translate-x-6.5 opacity-40 transition-[translate,opacity,background,color] duration-500 ease-thb08 hover:bg-[oklch(1_0_0/0.07)] hover:text-thb08-menuink focus-visible:bg-[oklch(1_0_0/0.07)] focus-visible:text-thb08-menuink focus-visible:outline-2 focus-visible:outline-thb08-acc focus-visible:-outline-offset-2 aria-current:text-thb08-menuink aria-current:bg-[color-mix(in_oklch,var(--color-thb08-acc)_22%,transparent)] group-data-open:translate-x-0 group-data-open:opacity-100 group-data-open:[transition-delay:calc(var(--i)*35ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
        <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 shrink-0 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2 2M19.1 4.9 17 7M7 17l-2.1 2.1"/></svg>Today
      </a>
      <a href="#inbox" style="--i:2" class="flex items-center gap-3 min-h-11.5 -mx-3 px-3 rounded-xl no-underline text-[14.5px] font-semibold text-thb08-menumut -translate-x-6.5 opacity-40 transition-[translate,opacity,background,color] duration-500 ease-thb08 hover:bg-[oklch(1_0_0/0.07)] hover:text-thb08-menuink focus-visible:bg-[oklch(1_0_0/0.07)] focus-visible:text-thb08-menuink focus-visible:outline-2 focus-visible:outline-thb08-acc focus-visible:-outline-offset-2 group-data-open:translate-x-0 group-data-open:opacity-100 group-data-open:[transition-delay:calc(var(--i)*35ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
        <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 shrink-0 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><path d="M3 13h5l2 3h4l2-3h5"/><path d="M5 5h14l2 8v6H3v-6Z"/></svg>Inbox
        <b class="ml-auto px-1.75 py-0.5 rounded-full bg-thb08-acc text-thb08-bg text-[10.5px] font-bold">7</b>
      </a>
      <a href="#projects" style="--i:3" class="flex items-center gap-3 min-h-11.5 -mx-3 px-3 rounded-xl no-underline text-[14.5px] font-semibold text-thb08-menumut -translate-x-6.5 opacity-40 transition-[translate,opacity,background,color] duration-500 ease-thb08 hover:bg-[oklch(1_0_0/0.07)] hover:text-thb08-menuink focus-visible:bg-[oklch(1_0_0/0.07)] focus-visible:text-thb08-menuink focus-visible:outline-2 focus-visible:outline-thb08-acc focus-visible:-outline-offset-2 group-data-open:translate-x-0 group-data-open:opacity-100 group-data-open:[transition-delay:calc(var(--i)*35ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
        <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 shrink-0 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><rect x="3.5" y="5" width="17" height="15" rx="2.5"/><path d="M3.5 10h17M9 5V3.5M15 5V3.5"/></svg>Projects
      </a>
      <a href="#notes" style="--i:4" class="flex items-center gap-3 min-h-11.5 -mx-3 px-3 rounded-xl no-underline text-[14.5px] font-semibold text-thb08-menumut -translate-x-6.5 opacity-40 transition-[translate,opacity,background,color] duration-500 ease-thb08 hover:bg-[oklch(1_0_0/0.07)] hover:text-thb08-menuink focus-visible:bg-[oklch(1_0_0/0.07)] focus-visible:text-thb08-menuink focus-visible:outline-2 focus-visible:outline-thb08-acc focus-visible:-outline-offset-2 group-data-open:translate-x-0 group-data-open:opacity-100 group-data-open:[transition-delay:calc(var(--i)*35ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
        <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 shrink-0 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><path d="M5 4h11l3 3v13H5Z"/><path d="M15.5 4v3.5H19M8.5 12h7M8.5 16h5"/></svg>Notes
      </a>
      <a href="#settings" style="--i:5" class="flex items-center gap-3 min-h-11.5 -mx-3 px-3 rounded-xl no-underline text-[14.5px] font-semibold text-thb08-menumut -translate-x-6.5 opacity-40 transition-[translate,opacity,background,color] duration-500 ease-thb08 hover:bg-[oklch(1_0_0/0.07)] hover:text-thb08-menuink focus-visible:bg-[oklch(1_0_0/0.07)] focus-visible:text-thb08-menuink focus-visible:outline-2 focus-visible:outline-thb08-acc focus-visible:-outline-offset-2 group-data-open:translate-x-0 group-data-open:opacity-100 group-data-open:[transition-delay:calc(var(--i)*35ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">
        <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 shrink-0 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/></svg>Settings
      </a>
      <span style="--i:6" class="mt-auto font-thb08-mono text-[11px] text-thb08-menudim -translate-x-6.5 opacity-40 transition-[translate,opacity] duration-500 ease-thb08 group-data-open:translate-x-0 group-data-open:opacity-100 group-data-open:[transition-delay:calc(var(--i)*35ms)] motion-reduce:translate-x-0 motion-reduce:duration-150">v4.2 &middot; push-canvas pattern</span>
    </nav>
    <div id="thb08-canvas" class="relative z-1 flex flex-col h-full bg-thb08-page transition-[translate,scale,border-radius,box-shadow] duration-500 ease-thb08 group-data-open:translate-x-[min(var(--w),76%)] group-data-open:scale-94 group-data-open:rounded-[22px] group-data-open:shadow-[-30px_24px_60px_-20px_oklch(0.12_0.04_280/0.6)] motion-reduce:duration-150">
      <header class="flex items-center gap-3 h-16 px-4 border-b border-thb08-edge2">
        <button type="button" aria-expanded="false" aria-controls="thb08-menu" aria-label="Open menu" class="grid place-items-center w-11 h-11 rounded-xl border-0 bg-transparent text-thb08-ink2 cursor-pointer transition-[background] duration-200 hover:bg-thb08-hover focus-visible:outline-2 focus-visible:outline-thb08-acc focus-visible:outline-offset-2">
          <span class="relative block w-4.75 h-3.25" aria-hidden="true">
            <i class="absolute left-0 top-0 w-4.75 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 group-data-open:translate-y-[5.5px] group-data-open:rotate-45 motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-[5.5px] w-4.75 h-0.5 rounded-sm bg-current transition-[opacity] duration-200 group-data-open:opacity-0 motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-[11px] w-4.75 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 group-data-open:-translate-y-[5.5px] group-data-open:-rotate-45 motion-reduce:transition-none"></i>
          </span>
        </button>
        <strong class="text-[15px] font-bold tracking-[-0.01em] text-thb08-ink2">Daybook</strong>
        <span class="grid place-items-center ml-auto w-8 h-8 rounded-full bg-linear-[140deg,var(--color-thb08-acc),oklch(0.55_0.18_260)] text-white text-xs font-bold" aria-hidden="true">A</span>
      </header>
      <div class="flex-1 grid content-start gap-3.25 p-5" aria-hidden="true">
        <div class="h-37.5 rounded-2xl bg-linear-[140deg,oklch(0.93_0.02_290),oklch(0.88_0.045_310)]"></div>
        <div class="h-2.75 w-[83%] rounded-full bg-thb08-line"></div>
        <div class="h-2.75 w-[64%] rounded-full bg-thb08-line"></div>
        <div class="h-2.75 w-[71%] rounded-full bg-thb08-line"></div>
        <div class="flex gap-3">
          <span class="flex-1 h-21 rounded-[14px] bg-white border border-thb08-edge2"></span>
          <span class="flex-1 h-21 rounded-[14px] bg-white border border-thb08-edge2"></span>
        </div>
      </div>
    </div>
    <button type="button" tabindex="-1" aria-hidden="true" class="absolute inset-y-0 right-0 left-[var(--w)] z-5 hidden border-0 bg-transparent cursor-w-resize group-data-open:block"></button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb08-bg: #2d2740;
  --color-thb08-bg: oklch(0.2 0.035 280);
  --color-thb08-edge: #494066;
  --color-thb08-edge: oklch(0.32 0.04 280);
  --color-thb08-menuink: #eae7f2;
  --color-thb08-menuink: oklch(0.93 0.01 280);
  --color-thb08-menumut: #b3adc4;
  --color-thb08-menumut: oklch(0.75 0.025 285);
  --color-thb08-menudim: #8b85a0;
  --color-thb08-menudim: oklch(0.6 0.03 285);
  --color-thb08-page: #fbfbfd;
  --color-thb08-page: oklch(0.98 0.004 260);
  --color-thb08-edge2: #e3e3ea;
  --color-thb08-edge2: oklch(0.9 0.008 260);
  --color-thb08-line: #e9e9ef;
  --color-thb08-line: oklch(0.92 0.006 265);
  --color-thb08-hover: #eeeef4;
  --color-thb08-hover: oklch(0.94 0.008 265);
  --color-thb08-ink: #f0eef7;
  --color-thb08-ink: oklch(0.95 0.01 280);
  --color-thb08-ink2: #34313f;
  --color-thb08-ink2: oklch(0.25 0.02 265);
  --color-thb08-acc: #b47ae4;
  --color-thb08-acc: oklch(0.7 0.16 300);
  --font-thb08-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb08-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb08: cubic-bezier(0.32, 0.72, 0.28, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-08 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.thb-08 > .group').forEach(function (vp) {
    if (vp.dataset.bound) return; vp.dataset.bound = '1';
    var btn = vp.querySelector('button[aria-controls="thb08-menu"]'),
        canvas = vp.querySelector('#thb08-canvas'),
        catcher = vp.querySelector('button[aria-hidden="true"]');
    function set(open) {
      vp.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      if (open) { canvas.setAttribute('inert', ''); vp.querySelector('#thb08-menu a').focus(); }
      else { canvas.removeAttribute('inert'); btn.focus(); }
    }
    btn.addEventListener('click', function () { set(true); });
    catcher.addEventListener('click', function () { set(false); });
    vp.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && vp.hasAttribute('data-open')) set(false);
    });
  });
})();
```
