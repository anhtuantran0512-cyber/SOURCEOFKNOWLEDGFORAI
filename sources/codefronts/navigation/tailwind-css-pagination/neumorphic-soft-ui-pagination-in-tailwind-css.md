---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/neumorphic-soft-ui-pagination-in-tailwind-css/"
title: "Neumorphic Soft UI Pagination in Tailwind CSS"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "Soft UI with the accessibility problem actually solved: keys extruded from the surface by a dual shadow, the current page pressed into it with v4's…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Soft UI Pagination in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-pagination/neumorphic-soft-ui-pagination-in-tailwind-css/

Soft UI with the accessibility problem actually solved: keys extruded from the surface by a dual shadow, the current page pressed into it with v4's inset-shadow-* &mdash; and also marked by accent colour, weight and a dot, because a shadow-only state sits near 1.5:1. The press morphs instead of snapping, a forced-colors: layer restores borders, and arrow keys walk the pages.
## HTML
```html
<section class="tpg-20 w-full min-h-svh grid place-items-center bg-tpg20-bg px-4 py-14 font-tpg20-sans text-tpg20-ink antialiased sm:px-5" aria-label="Neumorphic soft UI pagination demo">
  <div class="grid w-full justify-items-center gap-8">
    <div id="tpg-20-queue" class="w-full max-w-[34rem] rounded-[2rem] bg-tpg20-bg p-4 shadow-tpg20-card sm:p-7">
      <header class="flex items-center justify-between gap-4 px-1">
        <div>
          <p class="font-tpg20-mono text-[11px] tracking-[0.12em] text-tpg20-acc uppercase">Listening queue</p>
          <h2 class="mt-1 text-xl font-semibold tracking-[-0.02em]">Slow Design Radio</h2>
        </div>
        <span aria-hidden="true" class="grid size-12 flex-none place-items-center rounded-full bg-tpg20-bg text-tpg20-acc shadow-tpg20-out"><svg viewBox="0 0 20 20" width="18" height="18"><path d="M6.5 4.6v10.8a.6.6 0 0 0 .9.5l8.4-5.4a.6.6 0 0 0 0-1L7.4 4.1a.6.6 0 0 0-.9.5z" fill="currentColor"/></svg></span>
      </header>
      <ol class="mt-6 grid grid-cols-[minmax(0,1fr)] gap-1 rounded-2xl bg-tpg20-bg p-2 inset-shadow-tpg20-well">
        <li class="flex min-w-0 items-center gap-3 rounded-xl px-3 py-3 sm:gap-4"><span class="w-7 flex-none font-tpg20-mono text-xs text-tpg20-mut tabular-nums">E31</span><span class="min-w-0 flex-1"><span class="block truncate text-[15px] font-medium">The chair that outlived its designer</span><span class="block text-[13px] text-tpg20-mut">with Hana Okafor</span></span><span class="flex-none font-tpg20-mono text-xs text-tpg20-mut tabular-nums">42:10</span></li>
        <li class="flex min-w-0 items-center gap-3 rounded-xl px-3 py-3 sm:gap-4"><span class="w-7 flex-none font-tpg20-mono text-xs text-tpg20-mut tabular-nums">E32</span><span class="min-w-0 flex-1"><span class="block truncate text-[15px] font-medium">Clay, kilns and patience</span><span class="block text-[13px] text-tpg20-mut">with Teodor Lindqvist</span></span><span class="flex-none font-tpg20-mono text-xs text-tpg20-mut tabular-nums">36:48</span></li>
        <li class="flex min-w-0 items-center gap-3 rounded-xl px-3 py-3 sm:gap-4"><span class="w-7 flex-none font-tpg20-mono text-xs text-tpg20-mut tabular-nums">E33</span><span class="min-w-0 flex-1"><span class="block truncate text-[15px] font-medium">Why buttons used to look like buttons</span><span class="block text-[13px] text-tpg20-mut">with Priya Raman</span></span><span class="flex-none font-tpg20-mono text-xs text-tpg20-mut tabular-nums">51:02</span></li>
      </ol>
      <footer class="mt-7 grid justify-items-center">
        <nav aria-label="Pagination" data-keys="" class="grid w-full grid-cols-[auto_1fr_auto] items-center gap-x-3 gap-y-5 sm:w-auto sm:grid-cols-[auto_auto_auto] sm:gap-x-3">
          <button type="button" data-step="-1" aria-label="Previous page" class="grid size-11 cursor-pointer place-items-center rounded-2xl bg-tpg20-bg text-tpg20-ink shadow-tpg20-out inset-shadow-tpg20-in0 transition-[box-shadow,color,translate] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-px hover:text-tpg20-acc active:translate-y-0 active:shadow-tpg20-out0 active:inset-shadow-tpg20-in focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg20-acc disabled:cursor-not-allowed disabled:text-tpg20-dim disabled:shadow-tpg20-out0 disabled:hover:translate-y-0 forced-colors:border forced-colors:border-[CanvasText] motion-reduce:transition-none sm:size-12"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
          <ol class="col-span-3 order-first flex items-center justify-center gap-2.5 sm:order-none sm:col-span-1 sm:gap-3">
            <li><button type="button" data-page="1" aria-label="Page 1" class="relative grid size-11 cursor-pointer place-items-center rounded-2xl bg-tpg20-bg text-[15px] font-medium text-tpg20-ink tabular-nums shadow-tpg20-out inset-shadow-tpg20-in0 transition-[box-shadow,color,translate] duration-300 ease-[cubic-bezier(.16,1,.3,1)] after:absolute after:bottom-1.5 after:size-1 after:rounded-full after:bg-transparent after:transition-all after:duration-300 hover:-translate-y-px hover:text-tpg20-acc active:translate-y-0 active:shadow-tpg20-out0 active:inset-shadow-tpg20-in focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg20-acc aria-[current=page]:cursor-default aria-[current=page]:translate-y-0 aria-[current=page]:font-bold aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg20-tx1 aria-[current=page]:to-tpg20-tx2 aria-[current=page]:bg-clip-text aria-[current=page]:text-transparent aria-[current=page]:shadow-tpg20-out0 aria-[current=page]:inset-shadow-tpg20-in aria-[current=page]:after:w-3.5 aria-[current=page]:after:bg-linear-to-r aria-[current=page]:after:from-tpg20-ac1 aria-[current=page]:after:to-tpg20-ac2 aria-[current=page]:after:shadow-[0_0_8px_1px_var(--color-tpg20-ac2)] forced-colors:border forced-colors:border-[CanvasText] forced-colors:aria-[current=page]:bg-[Highlight] forced-colors:aria-[current=page]:text-[HighlightText] forced-colors:aria-[current=page]:bg-clip-border forced-colors:aria-[current=page]:forced-color-adjust-none motion-reduce:transition-none sm:size-12">1</button></li>
            <li><button type="button" data-page="2" aria-label="Page 2" class="relative grid size-11 cursor-pointer place-items-center rounded-2xl bg-tpg20-bg text-[15px] font-medium text-tpg20-ink tabular-nums shadow-tpg20-out inset-shadow-tpg20-in0 transition-[box-shadow,color,translate] duration-300 ease-[cubic-bezier(.16,1,.3,1)] after:absolute after:bottom-1.5 after:size-1 after:rounded-full after:bg-transparent after:transition-all after:duration-300 hover:-translate-y-px hover:text-tpg20-acc active:translate-y-0 active:shadow-tpg20-out0 active:inset-shadow-tpg20-in focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg20-acc aria-[current=page]:cursor-default aria-[current=page]:translate-y-0 aria-[current=page]:font-bold aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg20-tx1 aria-[current=page]:to-tpg20-tx2 aria-[current=page]:bg-clip-text aria-[current=page]:text-transparent aria-[current=page]:shadow-tpg20-out0 aria-[current=page]:inset-shadow-tpg20-in aria-[current=page]:after:w-3.5 aria-[current=page]:after:bg-linear-to-r aria-[current=page]:after:from-tpg20-ac1 aria-[current=page]:after:to-tpg20-ac2 aria-[current=page]:after:shadow-[0_0_8px_1px_var(--color-tpg20-ac2)] forced-colors:border forced-colors:border-[CanvasText] forced-colors:aria-[current=page]:bg-[Highlight] forced-colors:aria-[current=page]:text-[HighlightText] forced-colors:aria-[current=page]:bg-clip-border forced-colors:aria-[current=page]:forced-color-adjust-none motion-reduce:transition-none sm:size-12">2</button></li>
            <li><button type="button" data-page="3" aria-label="Page 3" aria-current="page" class="relative grid size-11 cursor-pointer place-items-center rounded-2xl bg-tpg20-bg text-[15px] font-medium text-tpg20-ink tabular-nums shadow-tpg20-out inset-shadow-tpg20-in0 transition-[box-shadow,color,translate] duration-300 ease-[cubic-bezier(.16,1,.3,1)] after:absolute after:bottom-1.5 after:size-1 after:rounded-full after:bg-transparent after:transition-all after:duration-300 hover:-translate-y-px hover:text-tpg20-acc active:translate-y-0 active:shadow-tpg20-out0 active:inset-shadow-tpg20-in focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg20-acc aria-[current=page]:cursor-default aria-[current=page]:translate-y-0 aria-[current=page]:font-bold aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg20-tx1 aria-[current=page]:to-tpg20-tx2 aria-[current=page]:bg-clip-text aria-[current=page]:text-transparent aria-[current=page]:shadow-tpg20-out0 aria-[current=page]:inset-shadow-tpg20-in aria-[current=page]:after:w-3.5 aria-[current=page]:after:bg-linear-to-r aria-[current=page]:after:from-tpg20-ac1 aria-[current=page]:after:to-tpg20-ac2 aria-[current=page]:after:shadow-[0_0_8px_1px_var(--color-tpg20-ac2)] forced-colors:border forced-colors:border-[CanvasText] forced-colors:aria-[current=page]:bg-[Highlight] forced-colors:aria-[current=page]:text-[HighlightText] forced-colors:aria-[current=page]:bg-clip-border forced-colors:aria-[current=page]:forced-color-adjust-none motion-reduce:transition-none sm:size-12">3</button></li>
            <li><button type="button" data-page="4" aria-label="Page 4" class="relative grid size-11 cursor-pointer place-items-center rounded-2xl bg-tpg20-bg text-[15px] font-medium text-tpg20-ink tabular-nums shadow-tpg20-out inset-shadow-tpg20-in0 transition-[box-shadow,color,translate] duration-300 ease-[cubic-bezier(.16,1,.3,1)] after:absolute after:bottom-1.5 after:size-1 after:rounded-full after:bg-transparent after:transition-all after:duration-300 hover:-translate-y-px hover:text-tpg20-acc active:translate-y-0 active:shadow-tpg20-out0 active:inset-shadow-tpg20-in focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg20-acc aria-[current=page]:cursor-default aria-[current=page]:translate-y-0 aria-[current=page]:font-bold aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg20-tx1 aria-[current=page]:to-tpg20-tx2 aria-[current=page]:bg-clip-text aria-[current=page]:text-transparent aria-[current=page]:shadow-tpg20-out0 aria-[current=page]:inset-shadow-tpg20-in aria-[current=page]:after:w-3.5 aria-[current=page]:after:bg-linear-to-r aria-[current=page]:after:from-tpg20-ac1 aria-[current=page]:after:to-tpg20-ac2 aria-[current=page]:after:shadow-[0_0_8px_1px_var(--color-tpg20-ac2)] forced-colors:border forced-colors:border-[CanvasText] forced-colors:aria-[current=page]:bg-[Highlight] forced-colors:aria-[current=page]:text-[HighlightText] forced-colors:aria-[current=page]:bg-clip-border forced-colors:aria-[current=page]:forced-color-adjust-none motion-reduce:transition-none sm:size-12">4</button></li>
            <li><button type="button" data-page="5" aria-label="Page 5" class="relative grid size-11 cursor-pointer place-items-center rounded-2xl bg-tpg20-bg text-[15px] font-medium text-tpg20-ink tabular-nums shadow-tpg20-out inset-shadow-tpg20-in0 transition-[box-shadow,color,translate] duration-300 ease-[cubic-bezier(.16,1,.3,1)] after:absolute after:bottom-1.5 after:size-1 after:rounded-full after:bg-transparent after:transition-all after:duration-300 hover:-translate-y-px hover:text-tpg20-acc active:translate-y-0 active:shadow-tpg20-out0 active:inset-shadow-tpg20-in focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg20-acc aria-[current=page]:cursor-default aria-[current=page]:translate-y-0 aria-[current=page]:font-bold aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg20-tx1 aria-[current=page]:to-tpg20-tx2 aria-[current=page]:bg-clip-text aria-[current=page]:text-transparent aria-[current=page]:shadow-tpg20-out0 aria-[current=page]:inset-shadow-tpg20-in aria-[current=page]:after:w-3.5 aria-[current=page]:after:bg-linear-to-r aria-[current=page]:after:from-tpg20-ac1 aria-[current=page]:after:to-tpg20-ac2 aria-[current=page]:after:shadow-[0_0_8px_1px_var(--color-tpg20-ac2)] forced-colors:border forced-colors:border-[CanvasText] forced-colors:aria-[current=page]:bg-[Highlight] forced-colors:aria-[current=page]:text-[HighlightText] forced-colors:aria-[current=page]:bg-clip-border forced-colors:aria-[current=page]:forced-color-adjust-none motion-reduce:transition-none sm:size-12">5</button></li>
          </ol>
          <button type="button" data-step="1" aria-label="Next page" class="max-sm:order-2 grid size-11 cursor-pointer place-items-center rounded-2xl bg-tpg20-bg text-tpg20-ink shadow-tpg20-out inset-shadow-tpg20-in0 transition-[box-shadow,color,translate] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-px hover:text-tpg20-acc active:translate-y-0 active:shadow-tpg20-out0 active:inset-shadow-tpg20-in focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg20-acc disabled:cursor-not-allowed disabled:text-tpg20-dim disabled:shadow-tpg20-out0 disabled:hover:translate-y-0 forced-colors:border forced-colors:border-[CanvasText] motion-reduce:transition-none sm:size-12"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
          <p role="status" aria-live="polite" class="justify-self-center text-center text-[13px] text-tpg20-mut tabular-nums max-sm:order-1 sm:col-span-3">Episodes <span data-range="" class="font-semibold text-tpg20-acc">31–45</span> of 74</p>
        </nav>
      </footer>
    </div>
    <p aria-hidden="true" class="max-w-full rounded-2xl px-3.5 py-2 text-center font-tpg20-mono text-[11.5px] text-tpg20-mut shadow-tpg20-out [overflow-wrap:anywhere]">shadow-tpg20-out &middot; aria-[current=page]:inset-shadow-tpg20-in &middot; forced-colors:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg20-bg: #e6e7f5;
  --color-tpg20-bg: oklch(0.931 0.022 280);
  --color-tpg20-hi: #ffffff;
  --color-tpg20-hi: oklch(1 0 0);
  --color-tpg20-lo: #c2c3e0;
  --color-tpg20-lo: oklch(0.83 0.045 280);
  --color-tpg20-ink: #2a2c4e;
  --color-tpg20-ink: oklch(0.31 0.065 280);
  --color-tpg20-mut: #55588a;
  --color-tpg20-mut: oklch(0.47 0.08 280);
  --color-tpg20-dim: #9294c0;
  --color-tpg20-dim: oklch(0.68 0.065 280);
  --color-tpg20-acc: #4f46e5;
  --color-tpg20-acc: oklch(0.511 0.262 277);
  --color-tpg20-ac1: #6366f1;
  --color-tpg20-ac1: oklch(0.585 0.233 277.1);
  --color-tpg20-ac2: #8b5cf6;
  --color-tpg20-ac2: oklch(0.606 0.25 292.7);
  --color-tpg20-tx1: #4f46e5;
  --color-tpg20-tx1: oklch(0.511 0.262 277);
  --color-tpg20-tx2: #6d28d9;
  --color-tpg20-tx2: oklch(0.491 0.241 292.6);
  --font-tpg20-sans: 'DM Sans', system-ui, sans-serif;
  --font-tpg20-mono: 'DM Mono', ui-monospace, monospace;
  --shadow-tpg20-card: 14px 14px 32px var(--color-tpg20-lo), -14px -14px 32px var(--color-tpg20-hi);
  --shadow-tpg20-out: 5px 5px 12px var(--color-tpg20-lo), -5px -5px 12px var(--color-tpg20-hi);
  --shadow-tpg20-out0: 5px 5px 12px transparent, -5px -5px 12px transparent;
  --inset-shadow-tpg20-in: inset 4px 4px 9px var(--color-tpg20-lo), inset -4px -4px 9px var(--color-tpg20-hi), inset 0 0 0 1px oklch(0.585 0.233 277.1 / 0.28);
  --inset-shadow-tpg20-in0: inset 4px 4px 9px transparent, inset -4px -4px 9px transparent, inset 0 0 0 1px transparent;
  --inset-shadow-tpg20-well: inset 6px 6px 14px var(--color-tpg20-lo), inset -6px -6px 14px var(--color-tpg20-hi);
}

@media (prefers-color-scheme: dark) {
  .tpg-20:not([data-theme="light"]) {
    --color-tpg20-bg: #262844;
    --color-tpg20-bg: oklch(0.29 0.055 280);
    --color-tpg20-hi: #30335a;
    --color-tpg20-hi: oklch(0.345 0.065 280);
    --color-tpg20-lo: #1a1b33;
    --color-tpg20-lo: oklch(0.225 0.045 280);
    --color-tpg20-ink: #e8e9ff;
    --color-tpg20-ink: oklch(0.94 0.03 280);
    --color-tpg20-mut: #aeb0dc;
    --color-tpg20-mut: oklch(0.77 0.06 280);
    --color-tpg20-dim: #6f72a3;
    --color-tpg20-dim: oklch(0.56 0.075 280);
    --color-tpg20-acc: #a5b4fc;
    --color-tpg20-acc: oklch(0.785 0.115 274.7);
    --color-tpg20-tx1: #a5b4fc;
    --color-tpg20-tx1: oklch(0.785 0.115 274.7);
    --color-tpg20-tx2: #c4b5fd;
    --color-tpg20-tx2: oklch(0.811 0.111 293.6);
  }
}

.tpg-20[data-theme="dark"] {
  --color-tpg20-bg: #262844;
  --color-tpg20-bg: oklch(0.29 0.055 280);
  --color-tpg20-hi: #30335a;
  --color-tpg20-hi: oklch(0.345 0.065 280);
  --color-tpg20-lo: #1a1b33;
  --color-tpg20-lo: oklch(0.225 0.045 280);
  --color-tpg20-ink: #e8e9ff;
  --color-tpg20-ink: oklch(0.94 0.03 280);
  --color-tpg20-mut: #aeb0dc;
  --color-tpg20-mut: oklch(0.77 0.06 280);
  --color-tpg20-dim: #6f72a3;
  --color-tpg20-dim: oklch(0.56 0.075 280);
  --color-tpg20-acc: #a5b4fc;
  --color-tpg20-acc: oklch(0.785 0.115 274.7);
  --color-tpg20-tx1: #a5b4fc;
  --color-tpg20-tx1: oklch(0.785 0.115 274.7);
  --color-tpg20-tx2: #c4b5fd;
  --color-tpg20-tx2: oklch(0.811 0.111 293.6);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-20 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tpg-20-queue');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const pages = Array.from(root.querySelectorAll('[data-page]'));
  const prev = root.querySelector('[data-step="-1"]');
  const next = root.querySelector('[data-step="1"]');
  const range = root.querySelector('[data-range]');
  const per = 15, total = 74, last = pages.length;
  let cur = 3;
  const go = (n, focus) => {
    cur = Math.min(last, Math.max(1, n));
    pages.forEach((b, i) => {
      if (i + 1 === cur) b.setAttribute('aria-current', 'page');
      else b.removeAttribute('aria-current');
    });
    prev.disabled = cur === 1;
    next.disabled = cur === last;
    range.textContent = ((cur - 1) * per + 1) + '–' + Math.min(total, cur * per);
    const lost = [prev, next].indexOf(document.activeElement) > -1 && document.activeElement.disabled;
    if (focus || lost) pages[cur - 1].focus();
  };
  pages.forEach((b) => b.addEventListener('click', () => go(Number(b.dataset.page))));
  prev.addEventListener('click', () => go(cur - 1));
  next.addEventListener('click', () => go(cur + 1));
  root.querySelector('[data-keys]').addEventListener('keydown', (e) => {
    const map = { ArrowLeft: cur - 1, ArrowRight: cur + 1, Home: 1, End: last };
    if (!(e.key in map)) return;
    e.preventDefault();
    go(map[e.key], true);
  });
  go(cur);
})();
```
