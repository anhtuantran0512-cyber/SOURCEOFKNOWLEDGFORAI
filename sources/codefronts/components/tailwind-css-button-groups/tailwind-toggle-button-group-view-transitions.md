---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-toggle-button-group-view-transitions/"
title: "Tailwind Toggle Button Group with View Transitions Morphing Highlight"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "A density switcher whose highlight morphs from one button to the next with the View Transitions API — the browser snapshots the old and new highlight (both…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Toggle Button Group with View Transitions Morphing Highlight
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-toggle-button-group-view-transitions/

A density switcher whose highlight morphs from one button to the next with the View Transitions API — the browser snapshots the old and new highlight (both named [view-transition-name:tbg03-thumb]) and tweens between them, no position math. State is pure ARIA: aria-checked:text-white and group-aria-checked:opacity-100 read the attribute a 25-line controller sets, with full arrow-key support.
## HTML
```html
<section class="tbg-03 w-full min-h-svh grid place-items-center bg-tbg03-bg bg-linear-160 from-tbg03-bg to-tbg03-bg2 px-5 py-14 font-tbg03-sans text-tbg03-ink" aria-label="View transitions morphing toggle group demo">
  <div class="grid w-full max-w-xl gap-4">
    <p id="tbg03-label" class="ml-1 text-xs font-bold uppercase tracking-[0.16em] text-tbg03-acc">Workspace density</p>
    <div data-tbg03-group role="radiogroup" aria-labelledby="tbg03-label" class="inline-flex w-fit max-w-full flex-wrap gap-1.5 rounded-2xl border border-tbg03-line bg-white p-1.5 shadow-tbg03-lift">
      <button type="button" role="radio" aria-checked="true" tabindex="0" class="group relative inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-xl px-4.5 text-[15px] font-semibold text-tbg03-mut transition-colors hover:text-tbg03-ink aria-checked:text-white focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg03-acc"><span aria-hidden="true" class="absolute inset-0 rounded-xl bg-tbg03-acc opacity-0 shadow-[0_6px_16px_-6px_var(--color-tbg03-acc)] group-aria-checked:opacity-100 group-aria-checked:[view-transition-name:tbg03-thumb]"></span><svg class="relative" viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/></svg><span class="relative">Focus</span></button>
      <button type="button" role="radio" aria-checked="false" tabindex="-1" class="group relative inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-xl px-4.5 text-[15px] font-semibold text-tbg03-mut transition-colors hover:text-tbg03-ink aria-checked:text-white focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg03-acc"><span aria-hidden="true" class="absolute inset-0 rounded-xl bg-tbg03-acc opacity-0 shadow-[0_6px_16px_-6px_var(--color-tbg03-acc)] group-aria-checked:opacity-100 group-aria-checked:[view-transition-name:tbg03-thumb]"></span><svg class="relative" viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg><span class="relative">Comfortable</span></button>
      <button type="button" role="radio" aria-checked="false" tabindex="-1" class="group relative inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-xl px-4.5 text-[15px] font-semibold text-tbg03-mut transition-colors hover:text-tbg03-ink aria-checked:text-white focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg03-acc"><span aria-hidden="true" class="absolute inset-0 rounded-xl bg-tbg03-acc opacity-0 shadow-[0_6px_16px_-6px_var(--color-tbg03-acc)] group-aria-checked:opacity-100 group-aria-checked:[view-transition-name:tbg03-thumb]"></span><svg class="relative" viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M4 10h16M4 14h16M4 18h16"/></svg><span class="relative">Compact</span></button>
      <button type="button" role="radio" aria-checked="false" tabindex="-1" class="group relative inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-xl px-4.5 text-[15px] font-semibold text-tbg03-mut transition-colors hover:text-tbg03-ink aria-checked:text-white focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg03-acc"><span aria-hidden="true" class="absolute inset-0 rounded-xl bg-tbg03-acc opacity-0 shadow-[0_6px_16px_-6px_var(--color-tbg03-acc)] group-aria-checked:opacity-100 group-aria-checked:[view-transition-name:tbg03-thumb]"></span><svg class="relative" viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M12 4a8 8 0 1 0 8 8 6 6 0 0 1-8-8z"/></svg><span class="relative">Zen</span></button>
    </div>
    <p class="ml-1 text-[13px] text-tbg03-mut">Use the arrow keys to move between options.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg03-bg: #f4f5fa;
  --color-tbg03-bg2: #e7e9f3;
  --color-tbg03-line: #e2e4f0;
  --color-tbg03-ink: #1e2140;
  --color-tbg03-mut: #575c7d;
  --color-tbg03-mut: oklch(0.47 0.05 275);
  --color-tbg03-acc: #3e3fd8;
  --color-tbg03-acc: oklch(0.5 0.22 270);
  --shadow-tbg03-lift: 0 16px 40px -26px rgb(40 30 120 / 0.5);
  --font-tbg03-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* View-transition pseudo-elements live on the document root and have no Tailwind variant. */

::view-transition-group(tbg03-thumb) {
  animation-duration: 0.45s;
  animation-timing-function: cubic-bezier(0.34, 1.25, 0.4, 1);
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(tbg03-thumb) {
    animation-duration: 1ms;
  }
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-03 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('[data-tbg03-group]').forEach((group) => {
    if (group.dataset.wired) return;
    group.dataset.wired = '1';
    const items = [...group.querySelectorAll('[role="radio"]')];
    const select = (target, focus) => {
      const apply = () => items.forEach((b) => {
        const on = b === target;
        b.setAttribute('aria-checked', String(on));
        b.tabIndex = on ? 0 : -1;
      });
      if (document.startViewTransition && !reduce.matches) document.startViewTransition(apply);
      else apply();
      if (focus) target.focus();
    };
    items.forEach((b, i) => {
      b.addEventListener('click', () => select(b));
      b.addEventListener('keydown', (e) => {
        const step = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key];
        if (!step) return;
        e.preventDefault();
        select(items[(i + step + items.length) % items.length], true);
      });
    });
  });
})();
```
