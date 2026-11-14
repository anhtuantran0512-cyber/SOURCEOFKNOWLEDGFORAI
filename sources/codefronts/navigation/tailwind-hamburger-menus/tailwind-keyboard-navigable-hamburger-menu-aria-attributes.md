---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-keyboard-navigable-hamburger-menu-aria-attributes/"
title: "Tailwind Keyboard Navigable Hamburger Menu with ARIA Attributes"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "The WAI-ARIA disclosure-navigation pattern in utilities, and the port has a genuine win: because the open state IS aria-expanded, aria-expanded: and…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Keyboard Navigable Hamburger Menu with ARIA Attributes
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-keyboard-navigable-hamburger-menu-aria-attributes/

The WAI-ARIA disclosure-navigation pattern in utilities, and the port has a genuine win: because the open state IS aria-expanded, aria-expanded: and group-has-aria-expanded: style straight off the accessibility attribute. Style and semantics cannot drift, because there is only one source of truth. Arrow/Home/End roving focus, Escape that returns focus, no focus trap &mdash; a disclosure, not a dialog.
## HTML
```html
<section class="thb-02 w-full min-h-svh bg-thb02-bg font-thb02-sans text-thb02-ink px-5 py-9" aria-label="Keyboard navigable ARIA hamburger menu demo">
  <div class="min-h-105 flex flex-col gap-4.5 p-6.5 rounded-[18px] border border-thb02-edge bg-thb02-bg">
    <div class="group w-[min(440px,100%)] mx-auto overflow-hidden rounded-2xl border border-thb02-edge bg-thb02-panel shadow-[0_16px_40px_-28px_oklch(0.35_0.05_260/0.5)]">
      <header class="flex items-center justify-between py-3 pl-4.5 pr-3">
        <span class="flex items-center gap-2.25 text-[15px] font-bold tracking-[-0.01em]">
          <i class="w-4.5 h-4.5 rounded-[5px] bg-[conic-gradient(from_180deg,var(--color-thb02-acc),oklch(0.7_0.13_200))]" aria-hidden="true"></i>Fieldnote
        </span>
        <button type="button" aria-expanded="false" aria-controls="thb02-panel" class="group flex items-center gap-2.5 min-h-11 px-4 rounded-[11px] border border-thb02-edge bg-thb02-panel font-thb02-sans text-[13.5px] font-semibold text-thb02-ink cursor-pointer transition-[background,border-color] duration-200 hover:bg-thb02-hover hover:border-thb02-edge2 focus-visible:outline-2 focus-visible:outline-thb02-acc focus-visible:outline-offset-2">
          <span class="relative block w-4 h-3" aria-hidden="true">
            <i class="absolute left-0 top-0 w-4 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-250 group-aria-expanded:translate-y-1.25 group-aria-expanded:rotate-45 motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-1.25 w-4 h-0.5 rounded-sm bg-current transition-[opacity,translate] duration-200 group-aria-expanded:opacity-0 group-aria-expanded:-translate-x-1.25 motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-2.5 w-4 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-250 group-aria-expanded:-translate-y-1.25 group-aria-expanded:-rotate-45 motion-reduce:transition-none"></i>
          </span>Menu
        </button>
      </header>
      <nav id="thb02-panel" aria-label="Primary" class="grid opacity-0 [grid-template-rows:0fr] transition-[grid-template-rows,opacity] duration-350 ease-thb02 group-has-aria-expanded:opacity-100 group-has-aria-expanded:[grid-template-rows:1fr] motion-reduce:transition-none">
        <ul class="list-none min-h-0 overflow-hidden flex flex-col px-2 group-has-aria-expanded:pb-2 group-has-aria-expanded:border-t group-has-aria-expanded:border-thb02-edge">
          <li><a href="#dashboard" aria-current="page" class="flex items-center min-h-11.5 mt-1 px-3 rounded-[9px] no-underline text-sm font-semibold text-thb02-mut transition-[background,color] duration-150 hover:bg-thb02-hover hover:text-thb02-ink focus-visible:text-thb02-ink focus-visible:outline-2 focus-visible:outline-thb02-acc focus-visible:-outline-offset-2 aria-current:text-thb02-acc aria-current:bg-[color-mix(in_oklch,var(--color-thb02-acc)_9%,transparent)]">Dashboard</a></li>
          <li><a href="#projects" class="flex items-center min-h-11.5 mt-1 px-3 rounded-[9px] no-underline text-sm font-semibold text-thb02-mut transition-[background,color] duration-150 hover:bg-thb02-hover hover:text-thb02-ink focus-visible:text-thb02-ink focus-visible:outline-2 focus-visible:outline-thb02-acc focus-visible:-outline-offset-2">Projects</a></li>
          <li><a href="#reports" class="flex items-center min-h-11.5 mt-1 px-3 rounded-[9px] no-underline text-sm font-semibold text-thb02-mut transition-[background,color] duration-150 hover:bg-thb02-hover hover:text-thb02-ink focus-visible:text-thb02-ink focus-visible:outline-2 focus-visible:outline-thb02-acc focus-visible:-outline-offset-2">Reports</a></li>
          <li><a href="#team" class="flex items-center min-h-11.5 mt-1 px-3 rounded-[9px] no-underline text-sm font-semibold text-thb02-mut transition-[background,color] duration-150 hover:bg-thb02-hover hover:text-thb02-ink focus-visible:text-thb02-ink focus-visible:outline-2 focus-visible:outline-thb02-acc focus-visible:-outline-offset-2">Team</a></li>
          <li><a href="#settings" class="flex items-center min-h-11.5 mt-1 px-3 rounded-[9px] no-underline text-sm font-semibold text-thb02-mut transition-[background,color] duration-150 hover:bg-thb02-hover hover:text-thb02-ink focus-visible:text-thb02-ink focus-visible:outline-2 focus-visible:outline-thb02-acc focus-visible:-outline-offset-2">Settings</a></li>
        </ul>
      </nav>
    </div>
    <p class="w-[min(440px,100%)] mx-auto text-center text-xs leading-[2.1] text-thb02-mut text-pretty" aria-hidden="true">
      <kbd class="inline-block min-w-6.5 mx-0.5 px-1.5 py-0.5 text-center font-thb02-mono text-[11px] font-semibold text-thb02-ink bg-thb02-panel border border-b-2 border-thb02-edge rounded-md">Tab</kbd> reach button &middot;
      <kbd class="inline-block min-w-6.5 mx-0.5 px-1.5 py-0.5 text-center font-thb02-mono text-[11px] font-semibold text-thb02-ink bg-thb02-panel border border-b-2 border-thb02-edge rounded-md">Enter</kbd> open &middot;
      <kbd class="inline-block min-w-6.5 mx-0.5 px-1.5 py-0.5 text-center font-thb02-mono text-[11px] font-semibold text-thb02-ink bg-thb02-panel border border-b-2 border-thb02-edge rounded-md">&darr;</kbd><kbd class="inline-block min-w-6.5 mx-0.5 px-1.5 py-0.5 text-center font-thb02-mono text-[11px] font-semibold text-thb02-ink bg-thb02-panel border border-b-2 border-thb02-edge rounded-md">&uarr;</kbd> move &middot;
      <kbd class="inline-block min-w-6.5 mx-0.5 px-1.5 py-0.5 text-center font-thb02-mono text-[11px] font-semibold text-thb02-ink bg-thb02-panel border border-b-2 border-thb02-edge rounded-md">Home</kbd><kbd class="inline-block min-w-6.5 mx-0.5 px-1.5 py-0.5 text-center font-thb02-mono text-[11px] font-semibold text-thb02-ink bg-thb02-panel border border-b-2 border-thb02-edge rounded-md">End</kbd> jump &middot;
      <kbd class="inline-block min-w-6.5 mx-0.5 px-1.5 py-0.5 text-center font-thb02-mono text-[11px] font-semibold text-thb02-ink bg-thb02-panel border border-b-2 border-thb02-edge rounded-md">Esc</kbd> close &amp; return
    </p>
    <output class="w-[min(440px,100%)] mx-auto text-center font-thb02-mono text-xs text-thb02-mut" aria-hidden="true">aria-expanded: <b class="text-thb02-acc">false</b></output>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb02-bg: #fafafc;
  --color-thb02-bg: oklch(0.985 0.003 250);
  --color-thb02-panel: #ffffff;
  --color-thb02-panel: oklch(1 0 0);
  --color-thb02-hover: #f3f4f7;
  --color-thb02-hover: oklch(0.965 0.006 250);
  --color-thb02-edge: #e3e5ea;
  --color-thb02-edge: oklch(0.9 0.01 250);
  --color-thb02-edge2: #c6c9d1;
  --color-thb02-edge2: oklch(0.8 0.02 255);
  --color-thb02-ink: #33384a;
  --color-thb02-ink: oklch(0.25 0.02 255);
  --color-thb02-mut: #74798a;
  --color-thb02-mut: oklch(0.54 0.015 255);
  --color-thb02-acc: #4a5fd0;
  --color-thb02-acc: oklch(0.52 0.17 262);
  --font-thb02-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb02-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb02: cubic-bezier(0.2, 0.7, 0.2, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-02 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.thb-02 div.group').forEach(function (bar) {
    if (bar.dataset.bound) return; bar.dataset.bound = '1';
    var btn = bar.querySelector('button[aria-controls="thb02-panel"]'),
        panel = bar.querySelector('#thb02-panel'),
        out = bar.closest('.thb-02').querySelector('output b'),
        links = Array.prototype.slice.call(panel.querySelectorAll('a'));
    function set(open, refocus) {
      btn.setAttribute('aria-expanded', String(open));
      if (out) out.textContent = String(open);
      if (open) links[0].focus();
      else if (refocus) btn.focus();
    }
    btn.addEventListener('click', function () { set(btn.getAttribute('aria-expanded') !== 'true'); });
    bar.addEventListener('keydown', function (e) {
      var open = btn.getAttribute('aria-expanded') === 'true';
      if (e.key === 'Escape' && open) { set(false, true); return; }
      var i = links.indexOf(document.activeElement);
      if (i < 0) return;
      var next = { ArrowDown: i + 1, ArrowUp: i - 1, Home: 0, End: links.length - 1 }[e.key];
      if (next === undefined) return;
      e.preventDefault();
      links[(next + links.length) % links.length].focus();
    });
    bar.addEventListener('focusout', function () {
      requestAnimationFrame(function () {
        if (!bar.contains(document.activeElement)) set(false, false);
      });
    });
  });
})();
```
