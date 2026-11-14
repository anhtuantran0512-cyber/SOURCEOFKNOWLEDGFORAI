---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-button-group-cursor-spotlight-glow/"
title: "Tailwind Button Group with Cursor-Following Spotlight Glow (Date Range Presets)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "Date-range preset buttons lit by a warm spotlight that follows the cursor across the whole group &mdash; one glow spanning every button, because each reads…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Button Group with Cursor-Following Spotlight Glow (Date Range Presets)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-button-group-cursor-spotlight-glow/

Date-range preset buttons lit by a warm spotlight that follows the cursor across the whole group &mdash; one glow spanning every button, because each reads the same pointer coordinates from --mx/--my. Selection is pure radios; the script only writes two variables. Below the presets, the resolved range (Oct 2 – Oct 8, 2026) updates as you choose, so users see exactly which dates they're getting.
## HTML
```html
<section class="tbg-25 w-full min-h-svh grid place-items-center bg-tbg25-bg bg-[radial-gradient(130%_120%_at_50%_0%,var(--color-tbg25-glow),transparent_70%)] px-5 py-14 font-tbg25-sans text-tbg25-ink" aria-label="Cursor-following spotlight button group demo">
  <div class="group/w grid w-full max-w-[38rem] gap-4">
    <p id="tbg25-label" class="ml-0.5 text-xs font-extrabold uppercase tracking-[0.16em] text-tbg25-acc">Date range</p>
    <div data-tbg25-group role="radiogroup" aria-labelledby="tbg25-label" class="group/g flex flex-wrap gap-3">
      <label class="relative isolate flex min-h-12.5 cursor-pointer items-center overflow-hidden rounded-[13px] border-[1.5px] border-tbg25-line bg-tbg25-key px-5.5 text-[15px] font-bold text-tbg25-mut transition-[color,border-color] duration-200 [--mx:50%] [--my:50%] before:absolute before:inset-0 before:-z-1 before:bg-[radial-gradient(220px_circle_at_var(--mx)_var(--my),color-mix(in_oklab,var(--color-tbg25-acc)_55%,transparent),transparent_60%)] before:opacity-0 before:transition-opacity before:duration-300 before:content-[''] group-hover/g:before:opacity-100 has-focus-visible:before:opacity-100 hover:border-tbg25-acc hover:text-tbg25-ink has-checked:border-tbg25-acc has-checked:bg-tbg25-acc has-checked:text-tbg25-on has-checked:shadow-[0_8px_24px_-10px_var(--color-tbg25-acc)] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg25-acc motion-reduce:transition-none"><input type="radio" name="tbg25" id="tbg25-today" class="sr-only">Today</label>
      <label class="relative isolate flex min-h-12.5 cursor-pointer items-center overflow-hidden rounded-[13px] border-[1.5px] border-tbg25-line bg-tbg25-key px-5.5 text-[15px] font-bold text-tbg25-mut transition-[color,border-color] duration-200 [--mx:50%] [--my:50%] before:absolute before:inset-0 before:-z-1 before:bg-[radial-gradient(220px_circle_at_var(--mx)_var(--my),color-mix(in_oklab,var(--color-tbg25-acc)_55%,transparent),transparent_60%)] before:opacity-0 before:transition-opacity before:duration-300 before:content-[''] group-hover/g:before:opacity-100 has-focus-visible:before:opacity-100 hover:border-tbg25-acc hover:text-tbg25-ink has-checked:border-tbg25-acc has-checked:bg-tbg25-acc has-checked:text-tbg25-on has-checked:shadow-[0_8px_24px_-10px_var(--color-tbg25-acc)] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg25-acc motion-reduce:transition-none"><input type="radio" name="tbg25" id="tbg25-7d" class="sr-only" checked>Last 7 days</label>
      <label class="relative isolate flex min-h-12.5 cursor-pointer items-center overflow-hidden rounded-[13px] border-[1.5px] border-tbg25-line bg-tbg25-key px-5.5 text-[15px] font-bold text-tbg25-mut transition-[color,border-color] duration-200 [--mx:50%] [--my:50%] before:absolute before:inset-0 before:-z-1 before:bg-[radial-gradient(220px_circle_at_var(--mx)_var(--my),color-mix(in_oklab,var(--color-tbg25-acc)_55%,transparent),transparent_60%)] before:opacity-0 before:transition-opacity before:duration-300 before:content-[''] group-hover/g:before:opacity-100 has-focus-visible:before:opacity-100 hover:border-tbg25-acc hover:text-tbg25-ink has-checked:border-tbg25-acc has-checked:bg-tbg25-acc has-checked:text-tbg25-on has-checked:shadow-[0_8px_24px_-10px_var(--color-tbg25-acc)] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg25-acc motion-reduce:transition-none"><input type="radio" name="tbg25" id="tbg25-30d" class="sr-only">Last 30 days</label>
      <label class="relative isolate flex min-h-12.5 cursor-pointer items-center overflow-hidden rounded-[13px] border-[1.5px] border-tbg25-line bg-tbg25-key px-5.5 text-[15px] font-bold text-tbg25-mut transition-[color,border-color] duration-200 [--mx:50%] [--my:50%] before:absolute before:inset-0 before:-z-1 before:bg-[radial-gradient(220px_circle_at_var(--mx)_var(--my),color-mix(in_oklab,var(--color-tbg25-acc)_55%,transparent),transparent_60%)] before:opacity-0 before:transition-opacity before:duration-300 before:content-[''] group-hover/g:before:opacity-100 has-focus-visible:before:opacity-100 hover:border-tbg25-acc hover:text-tbg25-ink has-checked:border-tbg25-acc has-checked:bg-tbg25-acc has-checked:text-tbg25-on has-checked:shadow-[0_8px_24px_-10px_var(--color-tbg25-acc)] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg25-acc motion-reduce:transition-none"><input type="radio" name="tbg25" id="tbg25-q" class="sr-only">Quarter</label>
      <label class="relative isolate flex min-h-12.5 cursor-pointer items-center overflow-hidden rounded-[13px] border-[1.5px] border-tbg25-line bg-tbg25-key px-5.5 text-[15px] font-bold text-tbg25-mut transition-[color,border-color] duration-200 [--mx:50%] [--my:50%] before:absolute before:inset-0 before:-z-1 before:bg-[radial-gradient(220px_circle_at_var(--mx)_var(--my),color-mix(in_oklab,var(--color-tbg25-acc)_55%,transparent),transparent_60%)] before:opacity-0 before:transition-opacity before:duration-300 before:content-[''] group-hover/g:before:opacity-100 has-focus-visible:before:opacity-100 hover:border-tbg25-acc hover:text-tbg25-ink has-checked:border-tbg25-acc has-checked:bg-tbg25-acc has-checked:text-tbg25-on has-checked:shadow-[0_8px_24px_-10px_var(--color-tbg25-acc)] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg25-acc motion-reduce:transition-none"><input type="radio" name="tbg25" id="tbg25-y" class="sr-only">Year to date</label>
    </div>
    <p class="ml-0.5 flex items-center gap-2 text-sm text-tbg25-mut"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg><span class="font-semibold text-tbg25-ink"><span class="hidden group-has-[#tbg25-today:checked]/w:inline">Oct 8, 2026</span><span class="hidden group-has-[#tbg25-7d:checked]/w:inline">Oct 2 – Oct 8, 2026</span><span class="hidden group-has-[#tbg25-30d:checked]/w:inline">Sep 9 – Oct 8, 2026</span><span class="hidden group-has-[#tbg25-q:checked]/w:inline">Oct 1 – Oct 8, 2026 (Q4)</span><span class="hidden group-has-[#tbg25-y:checked]/w:inline">Jan 1 – Oct 8, 2026</span></span></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg25-bg: #0b0705;
  --color-tbg25-glow: #22160c;
  --color-tbg25-key: #1b120b;
  --color-tbg25-line: #3a2a1c;
  --color-tbg25-ink: #fff2e2;
  --color-tbg25-mut: #d2bea3;
  --color-tbg25-mut: oklch(0.81 0.04 70);
  --color-tbg25-on: #1a0f06;
  --color-tbg25-acc: #f5a83a;
  --color-tbg25-acc: oklch(0.79 0.15 68);
  --font-tbg25-sans: 'Hanken Grotesk', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-25 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-tbg25-group]').forEach((group) => {
    if (group.dataset.wired) return;
    group.dataset.wired = '1';
    const btns = [...group.querySelectorAll('label')];
    group.addEventListener('pointermove', (e) => {
      btns.forEach((b) => {
        const r = b.getBoundingClientRect();
        b.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        b.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    }, { passive: true });
    group.addEventListener('pointerleave', () => {
      btns.forEach((b) => { b.style.removeProperty('--mx'); b.style.removeProperty('--my'); });
    });
  });
})();
```
