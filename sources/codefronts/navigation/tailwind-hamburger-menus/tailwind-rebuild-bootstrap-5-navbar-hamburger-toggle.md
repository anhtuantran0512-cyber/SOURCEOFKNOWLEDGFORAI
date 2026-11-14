---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-rebuild-bootstrap-5-navbar-hamburger-toggle/"
title: "Tailwind Rebuild of the Bootstrap 5 Navbar Hamburger Toggle"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "What the Bootstrap 5 navbar becomes when you migrate it &mdash; the same markup shape, the same breakpoint behaviour, the same animated collapse, with no…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Rebuild of the Bootstrap 5 Navbar Hamburger Toggle
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-rebuild-bootstrap-5-navbar-hamburger-toggle/

What the Bootstrap 5 navbar becomes when you migrate it &mdash; the same markup shape, the same breakpoint behaviour, the same animated collapse, with no framework CSS and no collapse plugin. Every Bootstrap class in the chain is mapped to its utility equivalent in the docs, so this doubles as a migration table for the most-copied navbar on the web.
## HTML
```html
<section class="thb-16 w-full min-h-svh bg-thb16-bg font-thb16-sans text-thb16-ink px-5 py-9" aria-label="Bootstrap navbar rebuilt in Tailwind demo">
  <div class="grid gap-3.5 p-5 rounded-[18px] border border-thb16-edge bg-thb16-bg">
    <div class="group @container overflow-hidden rounded-[14px] border border-thb16-edge bg-white shadow-[0_14px_34px_-26px_oklch(0.3_0.03_262/0.6)]">
      <nav class="py-2 bg-thb16-tertiary border-b border-thb16-edge" aria-label="Main">
        <div class="flex flex-wrap items-center justify-between gap-2 px-4">
          <a href="#home" class="flex items-center gap-2.25 py-1.5 text-[16.5px] font-semibold text-thb16-ink no-underline">
            <span class="w-4.75 h-4.75 rounded-[5px] bg-linear-[140deg,var(--color-thb16-primary),oklch(0.65_0.2_300)]" aria-hidden="true"></span>Bootlace
          </a>
          <button type="button" aria-expanded="false" aria-controls="thb16-nav" aria-label="Toggle navigation" class="group grid place-items-center w-13 h-11 rounded-lg border border-thb16-edge2 bg-transparent text-thb16-ink cursor-pointer transition-[box-shadow] duration-150 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_color-mix(in_oklch,var(--color-thb16-primary)_35%,transparent)] @min-lg:hidden">
            <span class="relative block w-5 h-3.5" aria-hidden="true">
              <i class="absolute left-0 top-0 w-5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-280 group-aria-expanded:translate-y-1.5 group-aria-expanded:rotate-45 motion-reduce:transition-none"></i>
              <i class="absolute left-0 top-1.5 w-5 h-0.5 rounded-sm bg-current transition-[opacity] duration-200 group-aria-expanded:opacity-0 motion-reduce:transition-none"></i>
              <i class="absolute left-0 top-3 w-5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-280 group-aria-expanded:-translate-y-1.5 group-aria-expanded:-rotate-45 motion-reduce:transition-none"></i>
            </span>
          </button>
          <div id="thb16-nav" class="grid basis-full [grid-template-rows:0fr] transition-[grid-template-rows] duration-300 ease-out group-data-open:[grid-template-rows:1fr] @min-lg:basis-auto @min-lg:ml-auto @min-lg:[grid-template-rows:1fr] motion-reduce:transition-none">
            <ul class="list-none flex flex-col min-h-0 overflow-hidden px-1 pt-1.5 pb-2.5 @min-lg:flex-row @min-lg:gap-0.5 @min-lg:p-0">
              <li><a href="#home" aria-current="page" class="block px-3 py-2.5 rounded-lg text-[14.5px] font-medium text-thb16-mut no-underline transition-[color,background] duration-150 hover:text-thb16-ink hover:bg-thb16-hover focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_color-mix(in_oklch,var(--color-thb16-primary)_35%,transparent)] aria-current:text-thb16-ink aria-current:font-semibold">Home</a></li>
              <li><a href="#features" class="block px-3 py-2.5 rounded-lg text-[14.5px] font-medium text-thb16-mut no-underline transition-[color,background] duration-150 hover:text-thb16-ink hover:bg-thb16-hover focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_color-mix(in_oklch,var(--color-thb16-primary)_35%,transparent)]">Features</a></li>
              <li><a href="#pricing" class="block px-3 py-2.5 rounded-lg text-[14.5px] font-medium text-thb16-mut no-underline transition-[color,background] duration-150 hover:text-thb16-ink hover:bg-thb16-hover focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_color-mix(in_oklch,var(--color-thb16-primary)_35%,transparent)]">Pricing</a></li>
              <li><a href="#beta" aria-disabled="true" class="block px-3 py-2.5 rounded-lg text-[14.5px] font-medium text-thb16-mut no-underline aria-disabled:text-thb16-off aria-disabled:pointer-events-none">Beta</a></li>
            </ul>
          </div>
        </div>
      </nav>
      <div class="grid gap-2.75 p-4" aria-hidden="true">
        <span class="block h-2.5 w-[76%] rounded-full bg-thb16-line"></span>
        <span class="block h-2.5 w-[90%] rounded-full bg-thb16-line"></span>
        <span class="block h-2.5 w-[58%] rounded-full bg-thb16-line"></span>
      </div>
    </div>
    <p class="text-xs leading-relaxed text-thb16-mut text-pretty" aria-hidden="true">No Bootstrap CSS and no collapse plugin &mdash; the height animation is a grid row track, and the whole script is a four-line attribute toggle. The card is narrower than <code class="font-thb16-mono text-[11px] px-1.5 py-0.5 rounded bg-thb16-line">@lg</code>, so the toggler shows.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb16-bg: #fafafc;
  --color-thb16-bg: oklch(0.985 0.003 260);
  --color-thb16-tertiary: #f6f7f9;
  --color-thb16-tertiary: oklch(0.97 0.004 260);
  --color-thb16-edge: #e3e4ea;
  --color-thb16-edge: oklch(0.9 0.007 260);
  --color-thb16-edge2: #c8cad4;
  --color-thb16-edge2: oklch(0.82 0.012 262);
  --color-thb16-line: #ebecf1;
  --color-thb16-line: oklch(0.93 0.005 260);
  --color-thb16-hover: #eceef3;
  --color-thb16-hover: oklch(0.94 0.006 260);
  --color-thb16-ink: #3b3f52;
  --color-thb16-ink: oklch(0.28 0.02 262);
  --color-thb16-mut: #6a6f85;
  --color-thb16-mut: oklch(0.5 0.016 262);
  --color-thb16-off: #b0b2bd;
  --color-thb16-off: oklch(0.72 0.008 262);
  --color-thb16-primary: #4b5fd6;
  --color-thb16-primary: oklch(0.55 0.19 262);
  --font-thb16-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb16-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-16 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.thb-16 div.group').forEach(function (frame) {
    if (frame.dataset.bound) return; frame.dataset.bound = '1';
    var btn = frame.querySelector('button[aria-controls="thb16-nav"]');
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') !== 'true';
      frame.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
    });
  });
})();
```
