---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-css-responsive-hamburger-menu-component/"
title: "Tailwind CSS Responsive Hamburger Menu Component"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "The canonical Tailwind navbar &mdash; and in this collection it is the one demo that needed no port at all, because the original was already written in…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Responsive Hamburger Menu Component
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-css-responsive-hamburger-menu-component/

The canonical Tailwind navbar &mdash; and in this collection it is the one demo that needed no port at all, because the original was already written in utilities. What it gains here is honesty: the CSS version had to ship a hand-written shim to render those classes, and this one runs the real compiler, so what you see is exactly what hidden md:flex produces.
## HTML
```html
<section class="thb-15 w-full min-h-svh bg-thb15-bg font-thb15-sans text-thb15-ink px-5 py-9" aria-label="Tailwind CSS hamburger menu demo">
  <div class="grid gap-3.5 p-5 rounded-[18px] border border-thb15-edge bg-thb15-bg">
    <div class="@container overflow-hidden rounded-[14px] border border-thb15-edge bg-white shadow-[0_14px_34px_-26px_oklch(0.3_0.02_286/0.6)]">
      <nav class="flex items-center justify-between px-4 py-3 bg-white border-b border-thb15-edge" aria-label="Primary">
        <a href="#home" class="flex items-center gap-2 font-bold text-thb15-ink no-underline">
          <span class="w-4.5 h-4.5 rounded-md bg-[conic-gradient(from_200deg,var(--color-thb15-acc),oklch(0.72_0.14_190))]" aria-hidden="true"></span>tailfleet
        </a>
        <div class="hidden @md:flex @md:items-center @md:gap-1">
          <a href="#features" aria-current="page" class="inline-flex items-center min-h-9.5 px-3 rounded-[9px] text-[13.5px] font-semibold text-thb15-mut no-underline transition-[color,background] duration-150 hover:text-thb15-ink hover:bg-thb15-hover focus-visible:outline-2 focus-visible:outline-thb15-acc focus-visible:outline-offset-2 aria-current:text-thb15-acc">Features</a>
          <a href="#pricing" class="inline-flex items-center min-h-9.5 px-3 rounded-[9px] text-[13.5px] font-semibold text-thb15-mut no-underline transition-[color,background] duration-150 hover:text-thb15-ink hover:bg-thb15-hover focus-visible:outline-2 focus-visible:outline-thb15-acc focus-visible:outline-offset-2">Pricing</a>
          <a href="#docs" class="inline-flex items-center min-h-9.5 px-3 rounded-[9px] text-[13.5px] font-semibold text-thb15-mut no-underline transition-[color,background] duration-150 hover:text-thb15-ink hover:bg-thb15-hover focus-visible:outline-2 focus-visible:outline-thb15-acc focus-visible:outline-offset-2">Docs</a>
          <a href="#blog" class="inline-flex items-center min-h-9.5 px-3 rounded-[9px] text-[13.5px] font-semibold text-thb15-mut no-underline transition-[color,background] duration-150 hover:text-thb15-ink hover:bg-thb15-hover focus-visible:outline-2 focus-visible:outline-thb15-acc focus-visible:outline-offset-2">Blog</a>
        </div>
        <div class="flex items-center gap-2">
          <a href="#signup" class="hidden @md:inline-flex items-center min-h-10 px-4 rounded-[10px] bg-thb15-ink text-white text-[13px] font-bold no-underline transition-[background] duration-200 hover:bg-thb15-acc focus-visible:outline-2 focus-visible:outline-thb15-acc focus-visible:outline-offset-2">Sign up</a>
          <button type="button" aria-expanded="false" aria-controls="thb15-menu" aria-label="Open menu" class="thb15-burger grid place-items-center w-11 h-11 rounded-[10px] border border-thb15-edge bg-white text-thb15-ink cursor-pointer transition-[background] duration-150 hover:bg-thb15-hover focus-visible:outline-2 focus-visible:outline-thb15-acc focus-visible:outline-offset-2 @md:hidden">
            <svg class="thb15-open [grid-area:1/1]" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
            <svg class="thb15-close hidden [grid-area:1/1]" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg>
          </button>
        </div>
      </nav>
      <div id="thb15-menu" class="hidden px-3 pb-3 bg-white border-b border-thb15-edge @md:hidden">
        <a href="#features" aria-current="page" class="flex items-center min-h-11 px-3 rounded-[9px] text-sm font-semibold text-thb15-mut no-underline transition-[background,color] duration-150 hover:bg-thb15-hover hover:text-thb15-ink focus-visible:outline-2 focus-visible:outline-thb15-acc focus-visible:-outline-offset-2 aria-current:text-thb15-acc">Features</a>
        <a href="#pricing" class="flex items-center min-h-11 px-3 rounded-[9px] text-sm font-semibold text-thb15-mut no-underline transition-[background,color] duration-150 hover:bg-thb15-hover hover:text-thb15-ink focus-visible:outline-2 focus-visible:outline-thb15-acc focus-visible:-outline-offset-2">Pricing</a>
        <a href="#docs" class="flex items-center min-h-11 px-3 rounded-[9px] text-sm font-semibold text-thb15-mut no-underline transition-[background,color] duration-150 hover:bg-thb15-hover hover:text-thb15-ink focus-visible:outline-2 focus-visible:outline-thb15-acc focus-visible:-outline-offset-2">Docs</a>
        <a href="#blog" class="flex items-center min-h-11 px-3 rounded-[9px] text-sm font-semibold text-thb15-mut no-underline transition-[background,color] duration-150 hover:bg-thb15-hover hover:text-thb15-ink focus-visible:outline-2 focus-visible:outline-thb15-acc focus-visible:-outline-offset-2">Blog</a>
        <a href="#signup" class="flex items-center justify-center w-full min-h-10 mt-2 px-4 rounded-[10px] bg-thb15-ink text-white text-[13px] font-bold no-underline transition-[background] duration-200 hover:bg-thb15-acc focus-visible:outline-2 focus-visible:outline-thb15-acc focus-visible:outline-offset-2">Sign up</a>
      </div>
      <div class="grid gap-2.75 p-4" aria-hidden="true">
        <span class="block h-2.5 w-[70%] rounded-full bg-thb15-line"></span>
        <span class="block h-2.5 w-[88%] rounded-full bg-thb15-line"></span>
        <span class="block h-2.5 w-[54%] rounded-full bg-thb15-line"></span>
      </div>
    </div>
    <p class="text-xs leading-relaxed text-thb15-mut text-pretty" aria-hidden="true">Real Tailwind, no shim &mdash; the CSS version of this demo had to hand-write these utilities to render. The card is narrower than <code class="font-thb15-mono text-[11px] px-1.5 py-0.5 rounded bg-thb15-line">@md</code>, so you see the mobile state; the docs give the <code class="font-thb15-mono text-[11px] px-1.5 py-0.5 rounded bg-thb15-line">peer-checked</code> no-JS variant.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb15-bg: #fafafa;
  --color-thb15-bg: oklch(0.985 0 0);
  --color-thb15-edge: #e4e4e7;
  --color-thb15-edge: oklch(0.92 0.004 286);
  --color-thb15-line: #ededf0;
  --color-thb15-line: oklch(0.94 0.002 286);
  --color-thb15-hover: #f4f4f5;
  --color-thb15-hover: oklch(0.96 0.002 286);
  --color-thb15-ink: #27272a;
  --color-thb15-ink: oklch(0.21 0.006 286);
  --color-thb15-mut: #71717a;
  --color-thb15-mut: oklch(0.55 0.014 286);
  --color-thb15-acc: #2f7fd4;
  --color-thb15-acc: oklch(0.59 0.16 245);
  --font-thb15-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb15-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-15 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.thb-15 .thb15-burger').forEach(function (btn) {
    if (btn.dataset.bound) return; btn.dataset.bound = '1';
    var menu = document.getElementById('thb15-menu');
    btn.addEventListener('click', function () {
      var open = menu.classList.toggle('hidden') === false;
      btn.setAttribute('aria-expanded', String(open));
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      btn.querySelector('.thb15-open').classList.toggle('hidden', open);
      btn.querySelector('.thb15-close').classList.toggle('hidden', !open);
    });
  });
})();
```
