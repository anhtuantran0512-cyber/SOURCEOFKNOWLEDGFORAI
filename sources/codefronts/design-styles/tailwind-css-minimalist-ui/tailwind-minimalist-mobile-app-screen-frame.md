---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-minimalist-mobile-app-screen-frame/"
title: "Tailwind Minimalist Mobile App Screen in a Frame"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "A banking home screen inside a 390&times;844 frame, holding up under real content: a balance sized in container units, a three-way segmented control wired to…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimalist Mobile App Screen in a Frame
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-minimalist-mobile-app-screen-frame/

A banking home screen inside a 390&times;844 frame, holding up under real content: a balance sized in container units, a three-way segmented control wired to the full WAI-ARIA tab pattern, a transaction list that truncates long merchant names instead of wrapping, and one full-width primary action. The frame is an @container, so the screen scales as a unit at any width.
## HTML
```html
<section class="tmu-19 relative w-full min-h-svh bg-tmu19-bg font-tmu19-ui text-tmu19-ink antialiased" aria-labelledby="tmu19-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu19-theme" type="checkbox" class="peer sr-only">
    <label for="tmu19-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu19-line bg-tmu19-surface text-tmu19-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu19-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu19-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid max-w-[68rem] items-center gap-12 px-5 pt-20 pb-16 md:grid-cols-[minmax(0,1fr)_minmax(0,24rem)] md:px-12">
    <div class="grid min-w-0 content-start gap-8">
    <header class="grid max-w-[62ch] gap-3">
      <p class="inline-flex items-center gap-2.5 font-tmu19-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu19-ink-2"><span class="tabular-nums text-tmu19-acc">19</span><span aria-hidden="true" class="h-px w-6 bg-tmu19-line"></span>Mobile screen</p>
      <h2 id="tmu19-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">A calm screen under real pressure</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu19-ink-2 text-pretty">Long names, pending money, three views and one action &mdash; in 390 points. Nothing decorative survives the width.</p>
    </header>
      <ol class="grid gap-4 text-sm text-tmu19-ink-2">
        <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-3"><span class="grid size-7 place-items-center rounded-full bg-tmu19-surface font-tmu19-mono text-xs font-semibold text-tmu19-acc ring-1 ring-tmu19-line">1</span><span class="grid gap-0.5"><b class="font-semibold text-tmu19-ink">Numbers get the size</b>The balance is the only large type, sized in container units so it fits any frame.</span></li>
        <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-3"><span class="grid size-7 place-items-center rounded-full bg-tmu19-surface font-tmu19-mono text-xs font-semibold text-tmu19-acc ring-1 ring-tmu19-line">2</span><span class="grid gap-0.5"><b class="font-semibold text-tmu19-ink">Names truncate, amounts never do</b>Merchant names ellipsise; the amount column is auto-width and never wraps.</span></li>
        <li class="grid grid-cols-[1.75rem_minmax(0,1fr)] gap-x-3"><span class="grid size-7 place-items-center rounded-full bg-tmu19-surface font-tmu19-mono text-xs font-semibold text-tmu19-acc ring-1 ring-tmu19-line">3</span><span class="grid gap-0.5"><b class="font-semibold text-tmu19-ink">One primary action</b>Send money is the only filled control on the screen.</span></li>
      </ol>
    </div>
    <div class="mx-auto w-full min-w-0 max-w-[390px] rounded-[40px] bg-tmu19-shell p-2.5 shadow-[0_30px_60px_-30px_rgb(0_0_0/0.45)]">
      <div id="tmu19-screen" class="@container grid aspect-[390/844] min-w-0 grid-rows-[auto_auto_auto_minmax(0,1fr)_auto] overflow-hidden rounded-[30px] bg-tmu19-surface">
        <header class="flex items-center justify-between gap-3 px-5 pt-3 pb-1">
          <p class="text-[0.9375rem] font-bold uppercase tracking-[0.06em]">Vale</p>
          <button type="button" aria-label="Account settings" class="grid size-11 place-items-center rounded-full text-tmu19-ink cursor-pointer hover:bg-tmu19-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu19-acc"><svg class="size-[22px]" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="8" r="3.4" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M5.5 20a6.5 6.5 0 0 1 13 0" fill="none" stroke="currentColor" stroke-width="1.7"/></svg></button>
        </header>
        <div class="grid gap-1 px-5 pt-2 pb-5">
          <p class="text-xs font-medium uppercase tracking-[0.08em] text-tmu19-ink-2">Available balance</p>
          <p class="text-[clamp(1.875rem,8cqi,2.375rem)] font-bold leading-[1.05] tracking-[-0.03em] tabular-nums">&pound;4,182.60</p>
          <p class="inline-flex items-center gap-1.5 text-xs text-tmu19-ink-2"><span aria-hidden="true" class="size-1.5 rounded-full bg-tmu19-acc"></span>&pound;620.00 pending &middot; settles Tuesday</p>
        </div>
        <div role="tablist" aria-label="Account view" class="mx-5 flex gap-1 rounded-[14px] bg-tmu19-bg p-1"><button type="button" role="tab" id="tmu19-tab-1" aria-controls="tmu19-panel-1" aria-selected="true" class="min-h-11 min-w-11 flex-1 rounded-[10px] px-2 text-sm font-semibold text-tmu19-ink-2 cursor-pointer transition-[background-color,color,box-shadow] duration-200 hover:text-tmu19-ink aria-selected:bg-tmu19-surface aria-selected:text-tmu19-ink aria-selected:shadow-[0_1px_2px_rgb(0_0_0/0.08),0_2px_8px_-2px_rgb(0_0_0/0.08)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmu19-acc motion-reduce:transition-none">Activity</button><button type="button" role="tab" id="tmu19-tab-2" aria-controls="tmu19-panel-2" aria-selected="false" tabindex="-1" class="min-h-11 min-w-11 flex-1 rounded-[10px] px-2 text-sm font-semibold text-tmu19-ink-2 cursor-pointer transition-[background-color,color,box-shadow] duration-200 hover:text-tmu19-ink aria-selected:bg-tmu19-surface aria-selected:text-tmu19-ink aria-selected:shadow-[0_1px_2px_rgb(0_0_0/0.08),0_2px_8px_-2px_rgb(0_0_0/0.08)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmu19-acc motion-reduce:transition-none">Scheduled</button><button type="button" role="tab" id="tmu19-tab-3" aria-controls="tmu19-panel-3" aria-selected="false" tabindex="-1" class="min-h-11 min-w-11 flex-1 rounded-[10px] px-2 text-sm font-semibold text-tmu19-ink-2 cursor-pointer transition-[background-color,color,box-shadow] duration-200 hover:text-tmu19-ink aria-selected:bg-tmu19-surface aria-selected:text-tmu19-ink aria-selected:shadow-[0_1px_2px_rgb(0_0_0/0.08),0_2px_8px_-2px_rgb(0_0_0/0.08)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmu19-acc motion-reduce:transition-none">Cards</button></div>
        <div class="min-h-0 min-w-0 overflow-y-auto">
            <div role="tabpanel" id="tmu19-panel-1" aria-labelledby="tmu19-tab-1" tabindex="0" class="min-w-0 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmu19-acc">
              <ul class="grid px-5 py-2">
                <li class="grid min-h-11 min-w-0 grid-cols-[2.25rem_minmax(0,1fr)_auto] items-center gap-x-3 border-b border-tmu19-line py-2.5 last:border-b-0"><span aria-hidden="true" class="row-span-2 grid size-9 place-items-center rounded-full bg-tmu19-bg text-xs font-semibold text-tmu19-ink-2">B</span><span class="min-w-0 truncate text-sm font-medium">Basalt Coffee Roasters</span><span class="col-start-3 row-span-2 row-start-1 whitespace-nowrap text-sm font-semibold tabular-nums">&minus;&pound;4.80</span><span class="col-start-2 text-xs text-tmu19-ink-2">Today</span></li>
                <li class="grid min-h-11 min-w-0 grid-cols-[2.25rem_minmax(0,1fr)_auto] items-center gap-x-3 border-b border-tmu19-line py-2.5 last:border-b-0"><span aria-hidden="true" class="row-span-2 grid size-9 place-items-center rounded-full bg-tmu19-bg text-xs font-semibold text-tmu19-ink-2">M</span><span class="min-w-0 truncate text-sm font-medium">Meridian salary</span><span class="col-start-3 row-span-2 row-start-1 whitespace-nowrap text-sm font-semibold tabular-nums text-tmu19-in">+&pound;3,410.00</span><span class="col-start-2 text-xs text-tmu19-ink-2">28 Aug</span></li>
                <li class="grid min-h-11 min-w-0 grid-cols-[2.25rem_minmax(0,1fr)_auto] items-center gap-x-3 border-b border-tmu19-line py-2.5 last:border-b-0"><span aria-hidden="true" class="row-span-2 grid size-9 place-items-center rounded-full bg-tmu19-bg text-xs font-semibold text-tmu19-ink-2">O</span><span class="min-w-0 truncate text-sm font-medium">Orbit Broadband monthly</span><span class="col-start-3 row-span-2 row-start-1 whitespace-nowrap text-sm font-semibold tabular-nums">&minus;&pound;38.00</span><span class="col-start-2 text-xs text-tmu19-ink-2">27 Aug</span></li>
                <li class="grid min-h-11 min-w-0 grid-cols-[2.25rem_minmax(0,1fr)_auto] items-center gap-x-3 border-b border-tmu19-line py-2.5 last:border-b-0"><span aria-hidden="true" class="row-span-2 grid size-9 place-items-center rounded-full bg-tmu19-bg text-xs font-semibold text-tmu19-ink-2">F</span><span class="min-w-0 truncate text-sm font-medium">Fern Grocery, Islington</span><span class="col-start-3 row-span-2 row-start-1 whitespace-nowrap text-sm font-semibold tabular-nums">&minus;&pound;61.24</span><span class="col-start-2 text-xs text-tmu19-ink-2">26 Aug</span></li>
                <li class="grid min-h-11 min-w-0 grid-cols-[2.25rem_minmax(0,1fr)_auto] items-center gap-x-3 border-b border-tmu19-line py-2.5 last:border-b-0"><span aria-hidden="true" class="row-span-2 grid size-9 place-items-center rounded-full bg-tmu19-bg text-xs font-semibold text-tmu19-ink-2">T</span><span class="min-w-0 truncate text-sm font-medium">Transfer to savings</span><span class="col-start-3 row-span-2 row-start-1 whitespace-nowrap text-sm font-semibold tabular-nums">&minus;&pound;400.00</span><span class="col-start-2 text-xs text-tmu19-ink-2">25 Aug</span></li>
              </ul>
            </div>
            <div role="tabpanel" id="tmu19-panel-2" aria-labelledby="tmu19-tab-2" tabindex="0" hidden class="min-w-0 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmu19-acc">
              <ul class="grid px-5 py-2">
                <li class="grid min-h-11 min-w-0 grid-cols-[2.25rem_minmax(0,1fr)_auto] items-center gap-x-3 border-b border-tmu19-line py-2.5 last:border-b-0"><span aria-hidden="true" class="row-span-2 grid size-9 place-items-center rounded-full bg-tmu19-bg text-xs font-semibold text-tmu19-ink-2">R</span><span class="min-w-0 truncate text-sm font-medium">Rent, Talon Property</span><span class="col-start-3 row-span-2 row-start-1 whitespace-nowrap text-sm font-semibold tabular-nums">&minus;&pound;1,240.00</span><span class="col-start-2 text-xs text-tmu19-ink-2">1 Sep</span></li>
                <li class="grid min-h-11 min-w-0 grid-cols-[2.25rem_minmax(0,1fr)_auto] items-center gap-x-3 border-b border-tmu19-line py-2.5 last:border-b-0"><span aria-hidden="true" class="row-span-2 grid size-9 place-items-center rounded-full bg-tmu19-bg text-xs font-semibold text-tmu19-ink-2">P</span><span class="min-w-0 truncate text-sm font-medium">Prism Energy</span><span class="col-start-3 row-span-2 row-start-1 whitespace-nowrap text-sm font-semibold tabular-nums">&minus;&pound;92.50</span><span class="col-start-2 text-xs text-tmu19-ink-2">4 Sep</span></li>
                <li class="grid min-h-11 min-w-0 grid-cols-[2.25rem_minmax(0,1fr)_auto] items-center gap-x-3 border-b border-tmu19-line py-2.5 last:border-b-0"><span aria-hidden="true" class="row-span-2 grid size-9 place-items-center rounded-full bg-tmu19-bg text-xs font-semibold text-tmu19-ink-2">S</span><span class="min-w-0 truncate text-sm font-medium">Savings standing order</span><span class="col-start-3 row-span-2 row-start-1 whitespace-nowrap text-sm font-semibold tabular-nums">&minus;&pound;400.00</span><span class="col-start-2 text-xs text-tmu19-ink-2">6 Sep</span></li>
              </ul>
            </div>
            <div role="tabpanel" id="tmu19-panel-3" aria-labelledby="tmu19-tab-3" tabindex="0" hidden class="min-w-0 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmu19-acc">
              <ul class="grid px-5 py-2">
                <li class="grid min-h-11 min-w-0 grid-cols-[2.25rem_minmax(0,1fr)_auto] items-center gap-x-3 border-b border-tmu19-line py-2.5 last:border-b-0"><span aria-hidden="true" class="row-span-2 grid size-9 place-items-center rounded-full bg-tmu19-bg text-xs font-semibold text-tmu19-ink-2">P</span><span class="min-w-0 truncate text-sm font-medium">Physical &middot; 4412</span><span class="col-start-3 row-span-2 row-start-1 whitespace-nowrap text-sm font-semibold tabular-nums">&pound;500 / day</span><span class="col-start-2 text-xs text-tmu19-ink-2">Active</span></li>
                <li class="grid min-h-11 min-w-0 grid-cols-[2.25rem_minmax(0,1fr)_auto] items-center gap-x-3 border-b border-tmu19-line py-2.5 last:border-b-0"><span aria-hidden="true" class="row-span-2 grid size-9 place-items-center rounded-full bg-tmu19-bg text-xs font-semibold text-tmu19-ink-2">V</span><span class="min-w-0 truncate text-sm font-medium">Virtual &middot; subscriptions</span><span class="col-start-3 row-span-2 row-start-1 whitespace-nowrap text-sm font-semibold tabular-nums">&pound;120 / mo</span><span class="col-start-2 text-xs text-tmu19-ink-2">Active</span></li>
                <li class="grid min-h-11 min-w-0 grid-cols-[2.25rem_minmax(0,1fr)_auto] items-center gap-x-3 border-b border-tmu19-line py-2.5 last:border-b-0"><span aria-hidden="true" class="row-span-2 grid size-9 place-items-center rounded-full bg-tmu19-bg text-xs font-semibold text-tmu19-ink-2">V</span><span class="min-w-0 truncate text-sm font-medium">Virtual &middot; travel</span><span class="col-start-3 row-span-2 row-start-1 whitespace-nowrap text-sm font-semibold tabular-nums">&mdash;</span><span class="col-start-2 text-xs text-tmu19-ink-2">Frozen</span></li>
              </ul>
            </div>
        </div>
        <footer class="border-t border-tmu19-line px-5 pt-3 pb-[calc(0.75rem+env(safe-area-inset-bottom,0px))]">
          <button type="button" class="inline-flex min-h-12 w-full items-center justify-center gap-2 rounded-xl bg-tmu19-acc text-[0.9375rem] font-bold text-tmu19-acc-ink cursor-pointer transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu19-ink motion-reduce:transition-none">Send money<svg class="size-[18px]" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h13m0 0-5-5m5 5-5 5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></button>
        </footer>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu19-bg: light-dark(#eaefe9, #0f1310);
  --color-tmu19-bg: light-dark(oklch(94% 0.016 145), oklch(17.5% 0.01 145));
  --color-tmu19-shell: light-dark(#d7ddd5, #1c211c);
  --color-tmu19-shell: light-dark(oklch(88% 0.014 145), oklch(24% 0.012 145));
  --color-tmu19-surface: light-dark(#ffffff, #171c17);
  --color-tmu19-surface: light-dark(oklch(100% 0 0), oklch(21.5% 0.011 145));
  --color-tmu19-ink: light-dark(#14180f, #edf1ea);
  --color-tmu19-ink: light-dark(oklch(19% 0.012 130), oklch(95.5% 0.01 140));
  --color-tmu19-ink-2: light-dark(#4d5548, #a3ac9d);
  --color-tmu19-ink-2: light-dark(oklch(44% 0.014 135), oklch(73.5% 0.014 140));
  --color-tmu19-line: light-dark(#dfe3dc, #2c332b);
  --color-tmu19-line: light-dark(oklch(90% 0.008 140), oklch(29% 0.012 145));
  --color-tmu19-acc: light-dark(#1d5c3a, #74d3a1);
  --color-tmu19-acc: light-dark(oklch(42% 0.1 158), oklch(82% 0.12 158));
  --color-tmu19-acc-ink: light-dark(#ffffff, #0d1a12);
  --color-tmu19-acc-ink: light-dark(oklch(100% 0 0), oklch(17% 0.02 158));
  --color-tmu19-in: light-dark(#14663f, #74d3a1);
  --color-tmu19-in: light-dark(oklch(43% 0.11 158), oklch(82% 0.12 158));
  --font-tmu19-ui: ui-rounded, "SF Pro Rounded", "Hiragino Maru Gothic ProN", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-tmu19-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-19 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-19:has(#tmu19-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-19:has(#tmu19-theme:checked) {
    color-scheme: light;
  }
}
```

## JavaScript
```js
(() => {
  const screen = document.querySelector('#tmu19-screen');
  if (!screen) return;
  const tabs = [...screen.querySelectorAll('[role="tab"]')];
  if (!tabs.length) return;

  const select = (tab) => {
    for (const t of tabs) {
      const on = t === tab;
      t.setAttribute('aria-selected', String(on));
      t.tabIndex = on ? 0 : -1;
      const panel = screen.querySelector('#' + t.getAttribute('aria-controls'));
      if (panel) panel.hidden = !on;
    }
    tab.focus();
  };
  const onClick = (e) => select(e.currentTarget);
  const onKey = (e) => {
    const i = tabs.indexOf(e.currentTarget);
    const next = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 }[e.key];
    if (next === undefined) return;
    e.preventDefault();
    select(tabs[(next + tabs.length) % tabs.length]);
  };

  for (const t of tabs) {
    t.addEventListener('click', onClick);
    t.addEventListener('keydown', onKey);
  }

  screen.__tmuCleanup = () => {
    for (const t of tabs) {
      t.removeEventListener('click', onClick);
      t.removeEventListener('keydown', onKey);
    }
  };
})();
```
