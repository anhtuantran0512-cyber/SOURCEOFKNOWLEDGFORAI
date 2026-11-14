---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-roving-tabindex-for-sidebar-keyboard-navigation/"
title: "Tailwind Roving Tabindex for Sidebar Keyboard Navigation"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "Ten folders means ten tab stops before a keyboard user reaches the content &mdash; unless the list is one stop and the arrow keys move inside it."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Roving Tabindex for Sidebar Keyboard Navigation
Source: https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-roving-tabindex-for-sidebar-keyboard-navigation/

Ten folders means ten tab stops before a keyboard user reaches the content &mdash; unless the list is one stop and the arrow keys move inside it. Roving tabindex is script by definition (it rewrites tabindex as focus moves), so the port's interesting half is the focus treatment: focus-visible: utilities give the moved-to item a ring AND a tint, because with one tab stop the focus indicator is the only thing telling the user where they are.
## HTML
```html
<section class="tsb-06 block relative w-full min-h-svh bg-tsb06-bg text-tsb06-ink font-tsb06-sans leading-[1.55]" aria-label="Ranger file manager">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-06-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-06-theme">
    <label class="grid place-items-center w-11 h-11 rounded-[0.4rem] border border-tsb06-line bg-tsb06-surf text-tsb06-ink cursor-pointer shadow-[inset_0_1px_3px_oklch(25%_0.02_140/0.14)] peer-focus-visible:outline-2 peer-focus-visible:outline-tsb06-acc peer-focus-visible:outline-offset-2" for="tsb-06-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] min-h-svh r46:grid-cols-[17rem_minmax(0,1fr)]">
    <nav class="min-w-0 px-3 py-4 bg-tsb06-surf border-b border-tsb06-line shadow-[inset_0_2px_6px_oklch(25%_0.02_140/0.09)] r46:border-b-0 r46:border-r r46:border-tsb06-line" aria-label="Ranger folders">
      <p class="m-0 mb-2 px-2.5 text-[0.72rem] tracking-[0.1em] uppercase text-tsb06-mut">All folders</p>
      <ul class="list-none m-0 p-0 grid gap-px" id="tsb-06-roving">
        <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.3rem] text-[0.93rem] text-tsb06-ink no-underline hover:bg-tsb06-surf2 focus-visible:outline-2 focus-visible:outline-tsb06-acc focus-visible:-outline-offset-2 focus-visible:bg-tsb06-accsoft aria-[current=page]:bg-tsb06-accsoft aria-[current=page]:text-tsb06-acc aria-[current=page]:font-semibold" href="#tsb-06-main" tabindex="0" aria-current="page">Deployments</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.3rem] text-[0.93rem] text-tsb06-ink no-underline hover:bg-tsb06-surf2 focus-visible:outline-2 focus-visible:outline-tsb06-acc focus-visible:-outline-offset-2 focus-visible:bg-tsb06-accsoft" href="#tsb-06-main" tabindex="-1">Design source</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.3rem] text-[0.93rem] text-tsb06-ink no-underline hover:bg-tsb06-surf2 focus-visible:outline-2 focus-visible:outline-tsb06-acc focus-visible:-outline-offset-2 focus-visible:bg-tsb06-accsoft" href="#tsb-06-main" tabindex="-1">Contracts 2026</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.3rem] text-[0.93rem] text-tsb06-ink no-underline hover:bg-tsb06-surf2 focus-visible:outline-2 focus-visible:outline-tsb06-acc focus-visible:-outline-offset-2 focus-visible:bg-tsb06-accsoft" href="#tsb-06-main" tabindex="-1">Audit exports</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.3rem] text-[0.93rem] text-tsb06-ink no-underline hover:bg-tsb06-surf2 focus-visible:outline-2 focus-visible:outline-tsb06-acc focus-visible:-outline-offset-2 focus-visible:bg-tsb06-accsoft" href="#tsb-06-main" tabindex="-1">Vendor invoices</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.3rem] text-[0.93rem] text-tsb06-ink no-underline hover:bg-tsb06-surf2 focus-visible:outline-2 focus-visible:outline-tsb06-acc focus-visible:-outline-offset-2 focus-visible:bg-tsb06-accsoft" href="#tsb-06-main" tabindex="-1">Brand assets</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.3rem] text-[0.93rem] text-tsb06-ink no-underline hover:bg-tsb06-surf2 focus-visible:outline-2 focus-visible:outline-tsb06-acc focus-visible:-outline-offset-2 focus-visible:bg-tsb06-accsoft" href="#tsb-06-main" tabindex="-1">Field photos</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.3rem] text-[0.93rem] text-tsb06-ink no-underline hover:bg-tsb06-surf2 focus-visible:outline-2 focus-visible:outline-tsb06-acc focus-visible:-outline-offset-2 focus-visible:bg-tsb06-accsoft" href="#tsb-06-main" tabindex="-1">Board minutes</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.3rem] text-[0.93rem] text-tsb06-ink no-underline hover:bg-tsb06-surf2 focus-visible:outline-2 focus-visible:outline-tsb06-acc focus-visible:-outline-offset-2 focus-visible:bg-tsb06-accsoft" href="#tsb-06-main" tabindex="-1">Payroll archive</a></li>
        <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.3rem] text-[0.93rem] text-tsb06-ink no-underline hover:bg-tsb06-surf2 focus-visible:outline-2 focus-visible:outline-tsb06-acc focus-visible:-outline-offset-2 focus-visible:bg-tsb06-accsoft" href="#tsb-06-main" tabindex="-1">Trash</a></li>
      </ul>
    </nav>

    <main class="min-w-0 content-start px-5 pt-6 pb-10 r46:px-9 r46:pt-10 r46:pb-12" id="tsb-06-main">
      <h2 class="m-0 mb-1 font-tsb06-display text-[clamp(1.4rem,3.6vw,2rem)] leading-[1.1]">Deployments</h2>
      <p class="m-0 mb-5 text-[0.88rem] text-tsb06-mut">42 items &middot; last change 2 hours ago</p>
      <table class="w-full border-collapse overflow-hidden text-[0.9rem] bg-tsb06-surf border border-tsb06-line rounded-[0.5rem]">
        <thead><tr class="[&>th]:px-3.5 [&>th]:py-2.5 [&>th]:text-start [&>th]:border-b [&>th]:border-tsb06-line [&>th]:text-[0.72rem] [&>th]:tracking-[0.1em] [&>th]:uppercase [&>th]:font-bold [&>th]:text-tsb06-mut"><th scope="col">Name</th><th scope="col">Owner</th><th scope="col">Size</th></tr></thead>
        <tbody class="[&>tr>td]:px-3.5 [&>tr>td]:py-2.5 [&>tr>td]:border-b [&>tr>td]:border-tsb06-line [&>tr:last-child>td]:border-b-0 [&>tr>td:last-child]:text-tsb06-mut [&>tr>td:last-child]:tabular-nums">
          <tr><td>release-notes.md</td><td>Priya Sharma</td><td>18 KB</td></tr>
          <tr><td>rollback-runbook.pdf</td><td>Jordan Lee</td><td>1.2 MB</td></tr>
          <tr><td>env-matrix.csv</td><td>Sam Rivera</td><td>44 KB</td></tr>
          <tr><td>token-exchange.log</td><td>Ada Okafor</td><td>7.8 MB</td></tr>
          <tr><td>staging-snapshot.zip</td><td>Tomas Vidal</td><td>212 MB</td></tr>
        </tbody>
      </table>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb06-bg: #eef1ea;
  --color-tsb06-bg: oklch(94.5% 0.012 130);
  --color-tsb06-surf: #f8faf5;
  --color-tsb06-surf: oklch(98% 0.008 130);
  --color-tsb06-surf2: #e3e8db;
  --color-tsb06-surf2: oklch(92% 0.018 130);
  --color-tsb06-line: #c8d1bd;
  --color-tsb06-line: oklch(84% 0.03 130);
  --color-tsb06-ink: #1b2118;
  --color-tsb06-ink: oklch(22% 0.02 140);
  --color-tsb06-mut: #5b6653;
  --color-tsb06-mut: oklch(47% 0.03 140);
  --color-tsb06-acc: #2f6b45;
  --color-tsb06-acc: oklch(46% 0.1 155);
  --color-tsb06-accsoft: #d9e8dd;
  --color-tsb06-accsoft: oklch(91% 0.03 155);
  --font-tsb06-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb06-display: 'Cabin', Optima, 'Gill Sans', Candara, system-ui, sans-serif;
  --breakpoint-r46: 46rem;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.tsb-06 {
  width: 100%;
  min-height: 100svh;
}

.tsb-06 *,
.tsb-06 *::before,
.tsb-06 *::after {
  box-sizing: border-box;
}
/* Token flip for the pure-CSS theme toggle, plus the two mandatory mirror blocks. */

.tsb-06:has(.tsb-06-theme-input:checked) {
  --color-tsb06-bg: #0f1310;
  --color-tsb06-surf: #161c16;
  --color-tsb06-surf2: #1e251d;
  --color-tsb06-line: #2d372b;
  --color-tsb06-ink: #eaf0e6;
  --color-tsb06-mut: #9aa694;
  --color-tsb06-acc: #8fd2a8;
  --color-tsb06-acc: oklch(82% 0.11 155);
  --color-tsb06-accsoft: #1d2c22;
}

@media (prefers-color-scheme: dark) {
  .tsb-06 {
    --color-tsb06-bg: #0f1310;
    --color-tsb06-surf: #161c16;
    --color-tsb06-surf2: #1e251d;
    --color-tsb06-line: #2d372b;
    --color-tsb06-ink: #eaf0e6;
    --color-tsb06-mut: #9aa694;
    --color-tsb06-acc: #8fd2a8;
    --color-tsb06-acc: oklch(82% 0.11 155);
    --color-tsb06-accsoft: #1d2c22;
  }

  .tsb-06:has(.tsb-06-theme-input:checked) {
    --color-tsb06-bg: #eef1ea;
    --color-tsb06-surf: #f8faf5;
    --color-tsb06-surf2: #e3e8db;
    --color-tsb06-line: #c8d1bd;
    --color-tsb06-ink: #1b2118;
    --color-tsb06-mut: #5b6653;
    --color-tsb06-acc: #2f6b45;
    --color-tsb06-acc: oklch(46% 0.1 155);
    --color-tsb06-accsoft: #d9e8dd;
  }
}

@media (prefers-color-scheme: light) {
  .tsb-06:has(.tsb-06-theme-input:checked) {
    --color-tsb06-bg: #0f1310;
    --color-tsb06-surf: #161c16;
    --color-tsb06-surf2: #1e251d;
    --color-tsb06-line: #2d372b;
    --color-tsb06-ink: #eaf0e6;
    --color-tsb06-mut: #9aa694;
    --color-tsb06-acc: #8fd2a8;
    --color-tsb06-acc: oklch(82% 0.11 155);
    --color-tsb06-accsoft: #1d2c22;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tsb-06').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var rail = root.querySelector('#tsb-06-roving'),
        items = Array.prototype.slice.call(rail.querySelectorAll('a[href]')),
        index = Math.max(0, items.findIndex(function (a) { return a.hasAttribute('aria-current'); }));
    function move(next) {
      index = Math.min(items.length - 1, Math.max(0, next));
      items.forEach(function (a, i) { a.setAttribute('tabindex', i === index ? '0' : '-1'); });
      items[index].focus();
    }
    function onKey(e) {
      var map = { ArrowDown: index + 1, ArrowUp: index - 1, Home: 0, End: items.length - 1 };
      if (!(e.key in map)) return;
      e.preventDefault();
      move(map[e.key]);
    }
    function onFocus(e) { var i = items.indexOf(e.target); if (i > -1) index = i; }
    rail.addEventListener('keydown', onKey);
    rail.addEventListener('focusin', onFocus);
    root.__tsbCleanup = function () {
      rail.removeEventListener('keydown', onKey);
      rail.removeEventListener('focusin', onFocus);
    };
  });
})();
```
