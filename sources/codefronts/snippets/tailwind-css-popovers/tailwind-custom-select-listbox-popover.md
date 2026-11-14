---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-custom-select-listbox-popover/"
title: "Tailwind Custom Select Listbox Popover"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "Popover supplies the container — top layer, light dismiss, Escape, focus return — and nothing about listbox semantics."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Custom Select Listbox Popover
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-custom-select-listbox-popover/

Popover supplies the container — top layer, light dismiss, Escape, focus return — and nothing about listbox semantics. Thirty-odd lines of vanilla JS add roving tabindex, arrow/Home/End/Enter and now typeahead; everything visual reads the ARIA state directly: aria-selected:font-semibold aria-selected:text-tpop11-sel on options and aria-expanded:border-tpop11-sel on the trigger. The script never touches a class.
## HTML
```html
<section class="tpop-11 transition-[--tpop11-d] duration-300 ease-in-out motion-reduce:transition-none dark:[--tpop11-d:1] [[data-theme=dark]_&]:[--tpop11-d:1] [[data-theme=light]_&]:[--tpop11-d:0] w-full min-h-svh bg-tpop11-bg px-4.5 py-10 font-tpop11-sans text-tpop11-ink" aria-label="Custom select listbox popover demo">
  <div class="grid min-h-[calc(100svh-80px)] max-w-full place-items-center">
    <div class="w-full min-w-0 max-w-[24rem] rounded-2xl border border-tpop11-rule bg-tpop11-surface px-4.5 pt-5 pb-4.5 shadow-[0_14px_30px_-22px_oklch(0.2_0.02_290/0.45)]">
      <p class="mb-4 text-[10.5px] font-bold uppercase tracking-[0.2em] text-tpop11-sel">Report settings</p>
      <label id="tpop-11-label" for="tpop-11-trigger" class="mb-1.5 block text-[12.5px] font-semibold text-tpop11-mut">Group results by</label>
      <button id="tpop-11-trigger" type="button" popovertarget="tpop-11-list" aria-expanded="false" aria-labelledby="tpop-11-label tpop-11-trigger" class="group/trig flex min-h-11 w-full cursor-pointer items-center justify-between gap-2.5 rounded-xl border border-tpop11-rule bg-tpop11-surface px-3 text-left text-[14px] font-medium text-tpop11-ink transition-[border-color,box-shadow] duration-150 [anchor-name:--tpop11-a] hover:border-tpop11-sel focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop11-sel aria-expanded:border-tpop11-sel aria-expanded:shadow-[0_0_0_3px_oklch(0.52_0.24_285/0.14)]">
        <span id="tpop-11-value" class="min-w-0 truncate">Account owner</span>
        <svg class="flex-none text-tpop11-mut transition-transform duration-200 motion-reduce:transition-none group-aria-expanded/trig:rotate-180" viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true"><path d="M4 6.5 8 10.5 12 6.5"/></svg>
      </button>
      <p class="mt-3 flex flex-wrap items-center gap-1 text-[12.5px] leading-relaxed text-tpop11-mut">
        <kbd class="rounded-md border border-b-2 border-tpop11-rule px-1.5 font-tpop11-mono text-[11px] text-tpop11-ink">↑</kbd><kbd class="rounded-md border border-b-2 border-tpop11-rule px-1.5 font-tpop11-mono text-[11px] text-tpop11-ink">↓</kbd> move ·
        <kbd class="rounded-md border border-b-2 border-tpop11-rule px-1.5 font-tpop11-mono text-[11px] text-tpop11-ink">Enter</kbd> commits · type a letter to jump
      </p>
    </div>
  </div>

  <div popover="auto" id="tpop-11-list" role="listbox" aria-labelledby="tpop-11-label" tabindex="-1" class="fixed m-auto w-[min(22rem,calc(100vw-32px))] rounded-xl border border-tpop11-rule bg-tpop11-surface p-1.5 text-tpop11-ink opacity-0 shadow-[0_20px_40px_-22px_oklch(0.2_0.02_290/0.5)] transition-[opacity,translate,display,overlay] duration-150 ease-out transition-discrete [position-anchor:--tpop11-a] [position-area:block-end_span-inline-end] [position-try-fallbacks:flip-block] open:opacity-100 starting:open:-translate-y-1 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mt-1.5 supports-[anchor-name:--a]:w-[anchor-size(width)]">
    <div role="option" tabindex="0" aria-selected="true" class="flex min-h-11 min-w-0 cursor-pointer items-center rounded-lg px-3 text-[14px] transition-colors hover:bg-tpop11-sel/6 focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop11-sel aria-selected:bg-tpop11-sel/10 aria-selected:font-semibold aria-selected:text-tpop11-sel aria-selected:after:ml-auto aria-selected:after:h-2 aria-selected:after:w-3.5 aria-selected:after:-translate-y-0.5 aria-selected:after:-rotate-45 aria-selected:after:border-b-2 aria-selected:after:border-l-2 aria-selected:after:border-current aria-selected:after:content-['']">Account owner</div>
    <div role="option" tabindex="-1" aria-selected="false" class="flex min-h-11 min-w-0 cursor-pointer items-center rounded-lg px-3 text-[14px] transition-colors hover:bg-tpop11-sel/6 focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop11-sel aria-selected:bg-tpop11-sel/10 aria-selected:font-semibold aria-selected:text-tpop11-sel aria-selected:after:ml-auto aria-selected:after:h-2 aria-selected:after:w-3.5 aria-selected:after:-translate-y-0.5 aria-selected:after:-rotate-45 aria-selected:after:border-b-2 aria-selected:after:border-l-2 aria-selected:after:border-current aria-selected:after:content-['']">Region</div>
    <div role="option" tabindex="-1" aria-selected="false" class="flex min-h-11 min-w-0 cursor-pointer items-center rounded-lg px-3 text-[14px] transition-colors hover:bg-tpop11-sel/6 focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop11-sel aria-selected:bg-tpop11-sel/10 aria-selected:font-semibold aria-selected:text-tpop11-sel aria-selected:after:ml-auto aria-selected:after:h-2 aria-selected:after:w-3.5 aria-selected:after:-translate-y-0.5 aria-selected:after:-rotate-45 aria-selected:after:border-b-2 aria-selected:after:border-l-2 aria-selected:after:border-current aria-selected:after:content-['']">Plan tier</div>
    <div role="option" tabindex="-1" aria-selected="false" class="flex min-h-11 min-w-0 cursor-pointer items-center rounded-lg px-3 text-[14px] transition-colors hover:bg-tpop11-sel/6 focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop11-sel aria-selected:bg-tpop11-sel/10 aria-selected:font-semibold aria-selected:text-tpop11-sel aria-selected:after:ml-auto aria-selected:after:h-2 aria-selected:after:w-3.5 aria-selected:after:-translate-y-0.5 aria-selected:after:-rotate-45 aria-selected:after:border-b-2 aria-selected:after:border-l-2 aria-selected:after:border-current aria-selected:after:content-['']">Signup month</div>
    <div role="option" tabindex="-1" aria-selected="false" class="flex min-h-11 min-w-0 cursor-pointer items-center rounded-lg px-3 text-[14px] transition-colors hover:bg-tpop11-sel/6 focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tpop11-sel aria-selected:bg-tpop11-sel/10 aria-selected:font-semibold aria-selected:text-tpop11-sel aria-selected:after:ml-auto aria-selected:after:h-2 aria-selected:after:w-3.5 aria-selected:after:-translate-y-0.5 aria-selected:after:-rotate-45 aria-selected:after:border-b-2 aria-selected:after:border-l-2 aria-selected:after:border-current aria-selected:after:content-['']">Churn risk band</div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop11-bg: #f5f5f7;
  --color-tpop11-bg: oklch(0.97 0.003 290);
  --color-tpop11-surface: #ffffff;
  --color-tpop11-surface: oklch(1 0 0);
  --color-tpop11-ink: #16151a;
  --color-tpop11-ink: oklch(0.2 0.01 290);
  --color-tpop11-mut: #5d5c66;
  --color-tpop11-mut: oklch(0.48 0.015 290);
  --color-tpop11-rule: #dedde2;
  --color-tpop11-rule: oklch(0.9 0.006 290);
  --color-tpop11-sel: #653de9;
  --color-tpop11-sel: oklch(0.52 0.24 285);
  --font-tpop11-sans: 'Geist', system-ui, sans-serif;
  --font-tpop11-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Theme dial: 0 = light, 1 = dark. Registered so the root can transition it. */

@property --tpop11-d {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles — plus the dark palette. Each @theme colour is
   re-declared on the root as a light/dark mix of the dial, so every utility (and every open
   popover, which inherits from the root) follows it. Light value last, dark value first. */

.tpop-11 {
  width: 100%;
  min-height: 100svh;
  --color-tpop11-bg: color-mix(in oklch, oklch(0.16 0.008 290) calc(var(--tpop11-d) * 100%), oklch(0.97 0.003 290));
  --color-tpop11-surface: color-mix(in oklch, oklch(0.21 0.01 290) calc(var(--tpop11-d) * 100%), oklch(1 0 0));
  --color-tpop11-ink: color-mix(in oklch, oklch(0.95 0.005 290) calc(var(--tpop11-d) * 100%), oklch(0.2 0.01 290));
  --color-tpop11-mut: color-mix(in oklch, oklch(0.73 0.015 290) calc(var(--tpop11-d) * 100%), oklch(0.48 0.015 290));
  --color-tpop11-rule: color-mix(in oklch, oklch(0.3 0.012 290) calc(var(--tpop11-d) * 100%), oklch(0.9 0.006 290));
  --color-tpop11-sel: color-mix(in oklch, oklch(0.74 0.15 285) calc(var(--tpop11-d) * 100%), oklch(0.52 0.24 285));
}
```

## JavaScript
```js
(() => {
  const list = document.getElementById('tpop-11-list');
  if (!list || list.dataset.wired) return;
  list.dataset.wired = '1';
  const trigger = document.getElementById('tpop-11-trigger');
  const value = document.getElementById('tpop-11-value');
  const opts = [...list.querySelectorAll('[role="option"]')];
  let buffer = '', bufferTimer = 0;
  const move = (to) => {
    const i = Math.max(0, Math.min(opts.length - 1, to));
    opts.forEach((o, n) => o.setAttribute('tabindex', n === i ? '0' : '-1'));
    opts[i].focus();
  };
  const commit = (o) => {
    opts.forEach((x) => x.setAttribute('aria-selected', String(x === o)));
    value.textContent = o.textContent.trim();
    list.hidePopover();
  };
  list.addEventListener('keydown', (e) => {
    const i = opts.indexOf(document.activeElement);
    const keys = { ArrowDown: i + 1, ArrowUp: i - 1, Home: 0, End: opts.length - 1 };
    if (e.key in keys) { e.preventDefault(); move(keys[e.key]); return; }
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); if (i > -1) commit(opts[i]); return; }
    if (e.key.length === 1 && !e.ctrlKey && !e.metaKey && !e.altKey) {
      clearTimeout(bufferTimer);
      buffer += e.key.toLowerCase();
      bufferTimer = setTimeout(() => { buffer = ''; }, 500);
      const hit = opts.findIndex((o) => o.textContent.trim().toLowerCase().startsWith(buffer));
      if (hit > -1) move(hit);
    }
  });
  opts.forEach((o) => o.addEventListener('click', () => commit(o)));
  list.addEventListener('toggle', (e) => {
    const open = e.newState === 'open';
    trigger.setAttribute('aria-expanded', String(open));
    if (open) move(opts.findIndex((o) => o.getAttribute('aria-selected') === 'true'));
  });
})();
```
