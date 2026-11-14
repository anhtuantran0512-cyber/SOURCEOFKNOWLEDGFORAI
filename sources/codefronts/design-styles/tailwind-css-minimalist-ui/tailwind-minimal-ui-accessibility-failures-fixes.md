---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-minimal-ui-accessibility-failures-fixes/"
title: "Tailwind Why Minimal Interfaces Fail Accessibility"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "Four ways a clean interface fails real people &mdash; low-contrast secondary text, a nameless icon button, a placeholder standing in for a label, a 28px…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Why Minimal Interfaces Fail Accessibility
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-minimal-ui-accessibility-failures-fixes/

Four ways a clean interface fails real people &mdash; low-contrast secondary text, a nameless icon button, a placeholder standing in for a label, a 28px target &mdash; each on its own panel with the WCAG criterion, a measured verdict and a switch that shows the fix. The panel owns its state as data-fixed; every fail/fix swap below it is a group-data-fixed/p: utility.
## HTML
```html
<section class="tmu-13 relative w-full min-h-svh bg-tmu13-bg font-tmu13-ui text-tmu13-ink antialiased" aria-labelledby="tmu13-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu13-theme" type="checkbox" class="peer sr-only">
    <label for="tmu13-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu13-line bg-tmu13-surface text-tmu13-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu13-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu13-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div id="tmu13-board" class="mx-auto grid max-w-[78rem] gap-10 px-5 pt-20 pb-20 md:px-12">
    <header class="grid max-w-[62ch] gap-3">
      <p class="inline-flex items-center gap-2.5 font-tmu13-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu13-ink-2"><span class="tabular-nums text-tmu13-acc">13</span><span aria-hidden="true" class="h-px w-6 bg-tmu13-line"></span>Accessibility</p>
      <h2 id="tmu13-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">Four ways a clean UI fails people</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu13-ink-2 text-pretty">Each failure looks tidier than its fix. Flip each panel &mdash; or the whole board &mdash; and compare what was lost.</p>
    </header>
    <div class="flex flex-wrap gap-2">
      <button type="button" data-tmu13-all="1" class="inline-flex min-h-11 items-center rounded-md border border-tmu13-acc bg-tmu13-acc px-4 text-sm font-semibold text-tmu13-acc-ink cursor-pointer hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu13-ring">Fix all four</button>
      <button type="button" data-tmu13-all="0" class="inline-flex min-h-11 items-center rounded-md border border-tmu13-line px-4 text-sm font-medium text-tmu13-ink cursor-pointer hover:border-tmu13-ink-2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu13-ring">Reset</button>
    </div>
    <div class="grid gap-5 grid-cols-[repeat(auto-fit,minmax(min(100%,18rem),1fr))]">
      <article data-tmu13-panel aria-labelledby="tmu13-p1" class="group/p grid min-w-0 content-start gap-3.5 rounded-xl border border-tmu13-line bg-tmu13-surface p-5 transition-[border-color,box-shadow] duration-200 data-fixed:border-tmu13-ok data-fixed:shadow-[0_0_0_3px_var(--color-tmu13-ok-bg)] md:p-6 motion-reduce:transition-none">
        <header class="grid min-w-0 gap-0.5">
          <h3 id="tmu13-p1" class="text-[0.9375rem] font-semibold tracking-[-0.01em]">Low-contrast secondary text</h3>
          <p class="font-tmu13-mono text-[0.6875rem] tracking-[0.04em] text-tmu13-bad group-data-fixed/p:text-tmu13-ok">SC 1.4.3 &middot; Contrast (Minimum)</p>
        </header>
        <div class="grid min-w-0 gap-2 rounded-lg border border-tmu13-line bg-tmu13-bg p-4">
          <p class="font-semibold tracking-[-0.012em]">Monthly recurring revenue</p>
          <p class="text-sm text-tmu13-fail-ink text-pretty group-data-fixed/p:text-tmu13-ink-2">Updated 6 minutes ago by Alex Chen. Includes 42 hours of overage on the Basalt retainer.</p>
        </div>
        <p class="flex flex-wrap gap-1.5 font-tmu13-mono text-xs font-semibold tabular-nums"><b class="inline-flex items-center gap-1.5 text-tmu13-bad group-data-fixed/p:hidden"><span aria-hidden="true">&times;</span>2.9:1 &mdash; fails</b><b class="hidden items-center gap-1.5 text-tmu13-ok group-data-fixed/p:inline-flex"><span aria-hidden="true">&check;</span>7.0:1 &mdash; passes</b></p>
        <button type="button" aria-pressed="false" data-tmu13-switch class="inline-flex min-h-11 min-w-11 items-center gap-2 justify-self-start rounded-md border border-tmu13-line bg-tmu13-bg px-3.5 text-[0.8125rem] font-medium text-tmu13-ink cursor-pointer transition-colors duration-150 hover:border-tmu13-ink-2 aria-pressed:border-tmu13-ok aria-pressed:text-tmu13-ok focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu13-ring motion-reduce:transition-none">
          <span aria-hidden="true" class="relative h-4 w-7 rounded-full bg-tmu13-line transition-colors duration-150 group-data-fixed/p:bg-tmu13-ok after:absolute after:top-0.5 after:left-0.5 after:size-3 after:rounded-full after:bg-tmu13-surface after:transition-transform after:duration-150 group-data-fixed/p:after:translate-x-3 motion-reduce:after:transition-none"></span>
          <span class="group-data-fixed/p:hidden">Show the fix</span><span class="hidden group-data-fixed/p:inline">Show the failure</span>
        </button>
      </article>
      <article data-tmu13-panel aria-labelledby="tmu13-p2" class="group/p grid min-w-0 content-start gap-3.5 rounded-xl border border-tmu13-line bg-tmu13-surface p-5 transition-[border-color,box-shadow] duration-200 data-fixed:border-tmu13-ok data-fixed:shadow-[0_0_0_3px_var(--color-tmu13-ok-bg)] md:p-6 motion-reduce:transition-none">
        <header class="grid min-w-0 gap-0.5">
          <h3 id="tmu13-p2" class="text-[0.9375rem] font-semibold tracking-[-0.01em]">Icon-only button, no name</h3>
          <p class="font-tmu13-mono text-[0.6875rem] tracking-[0.04em] text-tmu13-bad group-data-fixed/p:text-tmu13-ok">SC 4.1.2 &middot; Name, Role, Value</p>
        </header>
        <div class="grid min-w-0 gap-2 rounded-lg border border-tmu13-line bg-tmu13-bg p-4">
          <div class="flex gap-2 pb-6 group-data-fixed/p:hidden"><button type="button" class="group/b relative grid size-11 place-items-center rounded-md border border-tmu13-line bg-tmu13-surface text-tmu13-ink cursor-pointer hover:border-tmu13-ink-2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu13-ring"><svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button><button type="button" class="group/b relative grid size-11 place-items-center rounded-md border border-tmu13-line bg-tmu13-surface text-tmu13-ink cursor-pointer hover:border-tmu13-ink-2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu13-ring"><svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 7h16M9 7V5h6v2M6 7l1 13h10l1-13" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button></div>
          <div class="hidden gap-2 pb-6 group-data-fixed/p:flex"><button type="button" aria-label="Add line item" class="group/b relative grid size-11 place-items-center rounded-md border border-tmu13-line bg-tmu13-surface text-tmu13-ink cursor-pointer hover:border-tmu13-ink-2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu13-ring"><svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><span aria-hidden="true" class="pointer-events-none absolute top-[calc(100%+6px)] left-0 z-10 whitespace-nowrap rounded bg-tmu13-ink px-2 py-1 text-[0.6875rem] text-tmu13-bg opacity-0 transition-opacity duration-150 group-hover/b:opacity-100 group-focus-visible/b:opacity-100 motion-reduce:transition-none">Add line item</span></button><button type="button" aria-label="Delete invoice" class="group/b relative grid size-11 place-items-center rounded-md border border-tmu13-line bg-tmu13-surface text-tmu13-ink cursor-pointer hover:border-tmu13-ink-2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu13-ring"><svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 7h16M9 7V5h6v2M6 7l1 13h10l1-13" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span aria-hidden="true" class="pointer-events-none absolute top-[calc(100%+6px)] left-0 z-10 whitespace-nowrap rounded bg-tmu13-ink px-2 py-1 text-[0.6875rem] text-tmu13-bg opacity-0 transition-opacity duration-150 group-hover/b:opacity-100 group-focus-visible/b:opacity-100 motion-reduce:transition-none">Delete invoice</span></button></div>
        </div>
        <p class="flex flex-wrap gap-1.5 font-tmu13-mono text-xs font-semibold tabular-nums"><b class="inline-flex items-center gap-1.5 text-tmu13-bad group-data-fixed/p:hidden"><span aria-hidden="true">&times;</span>No accessible name</b><b class="hidden items-center gap-1.5 text-tmu13-ok group-data-fixed/p:inline-flex"><span aria-hidden="true">&check;</span>aria-label + visible tip</b></p>
        <button type="button" aria-pressed="false" data-tmu13-switch class="inline-flex min-h-11 min-w-11 items-center gap-2 justify-self-start rounded-md border border-tmu13-line bg-tmu13-bg px-3.5 text-[0.8125rem] font-medium text-tmu13-ink cursor-pointer transition-colors duration-150 hover:border-tmu13-ink-2 aria-pressed:border-tmu13-ok aria-pressed:text-tmu13-ok focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu13-ring motion-reduce:transition-none">
          <span aria-hidden="true" class="relative h-4 w-7 rounded-full bg-tmu13-line transition-colors duration-150 group-data-fixed/p:bg-tmu13-ok after:absolute after:top-0.5 after:left-0.5 after:size-3 after:rounded-full after:bg-tmu13-surface after:transition-transform after:duration-150 group-data-fixed/p:after:translate-x-3 motion-reduce:after:transition-none"></span>
          <span class="group-data-fixed/p:hidden">Show the fix</span><span class="hidden group-data-fixed/p:inline">Show the failure</span>
        </button>
      </article>
      <article data-tmu13-panel aria-labelledby="tmu13-p3" class="group/p grid min-w-0 content-start gap-3.5 rounded-xl border border-tmu13-line bg-tmu13-surface p-5 transition-[border-color,box-shadow] duration-200 data-fixed:border-tmu13-ok data-fixed:shadow-[0_0_0_3px_var(--color-tmu13-ok-bg)] md:p-6 motion-reduce:transition-none">
        <header class="grid min-w-0 gap-0.5">
          <h3 id="tmu13-p3" class="text-[0.9375rem] font-semibold tracking-[-0.01em]">Placeholder used as a label</h3>
          <p class="font-tmu13-mono text-[0.6875rem] tracking-[0.04em] text-tmu13-bad group-data-fixed/p:text-tmu13-ok">SC 3.3.2 &middot; Labels or Instructions</p>
        </header>
        <div class="grid min-w-0 gap-2 rounded-lg border border-tmu13-line bg-tmu13-bg p-4">
          <div class="grid gap-2 group-data-fixed/p:hidden">
            <input type="text" placeholder="Card number" inputmode="numeric" aria-label="Card number (placeholder only)" class="min-h-11 w-full min-w-0 rounded-md border border-tmu13-line bg-tmu13-bg px-2.5 text-sm text-tmu13-ink placeholder:text-tmu13-ink-2 focus-visible:border-tmu13-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu13-ring">
            <input type="text" placeholder="MM / YY" inputmode="numeric" aria-label="Expiry (placeholder only)" class="min-h-11 w-full min-w-0 rounded-md border border-tmu13-line bg-tmu13-bg px-2.5 text-sm text-tmu13-ink placeholder:text-tmu13-ink-2 focus-visible:border-tmu13-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu13-ring">
          </div>
          <div class="hidden gap-3 group-data-fixed/p:grid">
            <div class="grid min-w-0 gap-1"><label for="tmu13-card" class="text-[0.8125rem] font-medium">Card number</label><input id="tmu13-card" type="text" placeholder="4242 4242 4242 4242" inputmode="numeric" class="min-h-11 w-full min-w-0 rounded-md border border-tmu13-line bg-tmu13-bg px-2.5 text-sm text-tmu13-ink placeholder:text-tmu13-ink-2 focus-visible:border-tmu13-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu13-ring"></div>
            <div class="grid min-w-0 gap-1"><label for="tmu13-exp" class="text-[0.8125rem] font-medium">Expiry</label><input id="tmu13-exp" type="text" placeholder="MM / YY" inputmode="numeric" class="min-h-11 w-full min-w-0 rounded-md border border-tmu13-line bg-tmu13-bg px-2.5 text-sm text-tmu13-ink placeholder:text-tmu13-ink-2 focus-visible:border-tmu13-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu13-ring"></div>
          </div>
        </div>
        <p class="flex flex-wrap gap-1.5 font-tmu13-mono text-xs font-semibold tabular-nums"><b class="inline-flex items-center gap-1.5 text-tmu13-bad group-data-fixed/p:hidden"><span aria-hidden="true">&times;</span>Label disappears on input</b><b class="hidden items-center gap-1.5 text-tmu13-ok group-data-fixed/p:inline-flex"><span aria-hidden="true">&check;</span>Label persists, hint remains</b></p>
        <button type="button" aria-pressed="false" data-tmu13-switch class="inline-flex min-h-11 min-w-11 items-center gap-2 justify-self-start rounded-md border border-tmu13-line bg-tmu13-bg px-3.5 text-[0.8125rem] font-medium text-tmu13-ink cursor-pointer transition-colors duration-150 hover:border-tmu13-ink-2 aria-pressed:border-tmu13-ok aria-pressed:text-tmu13-ok focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu13-ring motion-reduce:transition-none">
          <span aria-hidden="true" class="relative h-4 w-7 rounded-full bg-tmu13-line transition-colors duration-150 group-data-fixed/p:bg-tmu13-ok after:absolute after:top-0.5 after:left-0.5 after:size-3 after:rounded-full after:bg-tmu13-surface after:transition-transform after:duration-150 group-data-fixed/p:after:translate-x-3 motion-reduce:after:transition-none"></span>
          <span class="group-data-fixed/p:hidden">Show the fix</span><span class="hidden group-data-fixed/p:inline">Show the failure</span>
        </button>
      </article>
      <article data-tmu13-panel aria-labelledby="tmu13-p4" class="group/p grid min-w-0 content-start gap-3.5 rounded-xl border border-tmu13-line bg-tmu13-surface p-5 transition-[border-color,box-shadow] duration-200 data-fixed:border-tmu13-ok data-fixed:shadow-[0_0_0_3px_var(--color-tmu13-ok-bg)] md:p-6 motion-reduce:transition-none">
        <header class="grid min-w-0 gap-0.5">
          <h3 id="tmu13-p4" class="text-[0.9375rem] font-semibold tracking-[-0.01em]">Target under 44px</h3>
          <p class="font-tmu13-mono text-[0.6875rem] tracking-[0.04em] text-tmu13-bad group-data-fixed/p:text-tmu13-ok">SC 2.5.8 &middot; Target Size (Minimum)</p>
        </header>
        <div class="grid min-w-0 gap-2 rounded-lg border border-tmu13-line bg-tmu13-bg p-4">
          <div class="flex flex-wrap gap-2">
            <button type="button" class="h-7 rounded-sm border border-tmu13-line bg-tmu13-surface px-2.5 text-xs text-tmu13-ink cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu13-ring group-data-fixed/p:h-11 group-data-fixed/p:min-w-11 group-data-fixed/p:rounded-md group-data-fixed/p:border-transparent group-data-fixed/p:bg-tmu13-acc group-data-fixed/p:px-4.5 group-data-fixed/p:text-sm group-data-fixed/p:font-semibold group-data-fixed/p:text-tmu13-acc-ink">Approve</button>
            <button type="button" class="h-7 rounded-sm border border-tmu13-line bg-tmu13-surface px-2.5 text-xs text-tmu13-ink cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu13-ring group-data-fixed/p:h-11 group-data-fixed/p:min-w-11 group-data-fixed/p:rounded-md group-data-fixed/p:bg-transparent group-data-fixed/p:px-4.5 group-data-fixed/p:text-sm">Reject</button>
          </div>
        </div>
        <p class="flex flex-wrap gap-1.5 font-tmu13-mono text-xs font-semibold tabular-nums"><b class="inline-flex items-center gap-1.5 text-tmu13-bad group-data-fixed/p:hidden"><span aria-hidden="true">&times;</span>32 &times; 28px</b><b class="hidden items-center gap-1.5 text-tmu13-ok group-data-fixed/p:inline-flex"><span aria-hidden="true">&check;</span>44 &times; 44px</b></p>
        <button type="button" aria-pressed="false" data-tmu13-switch class="inline-flex min-h-11 min-w-11 items-center gap-2 justify-self-start rounded-md border border-tmu13-line bg-tmu13-bg px-3.5 text-[0.8125rem] font-medium text-tmu13-ink cursor-pointer transition-colors duration-150 hover:border-tmu13-ink-2 aria-pressed:border-tmu13-ok aria-pressed:text-tmu13-ok focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu13-ring motion-reduce:transition-none">
          <span aria-hidden="true" class="relative h-4 w-7 rounded-full bg-tmu13-line transition-colors duration-150 group-data-fixed/p:bg-tmu13-ok after:absolute after:top-0.5 after:left-0.5 after:size-3 after:rounded-full after:bg-tmu13-surface after:transition-transform after:duration-150 group-data-fixed/p:after:translate-x-3 motion-reduce:after:transition-none"></span>
          <span class="group-data-fixed/p:hidden">Show the fix</span><span class="hidden group-data-fixed/p:inline">Show the failure</span>
        </button>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu13-bg: light-dark(#ffffff, #101315);
  --color-tmu13-bg: light-dark(oklch(100% 0 0), oklch(17.5% 0.006 250));
  --color-tmu13-surface: light-dark(#f7f8f9, #191d20);
  --color-tmu13-surface: light-dark(oklch(97.5% 0.003 250), oklch(23% 0.007 250));
  --color-tmu13-ink: light-dark(#15181b, #eef1f3);
  --color-tmu13-ink: light-dark(oklch(19.5% 0.006 250), oklch(95.5% 0.004 250));
  --color-tmu13-ink-2: light-dark(#4f585f, #a5aeb5);
  --color-tmu13-ink-2: light-dark(oklch(45% 0.012 250), oklch(74% 0.01 250));
  --color-tmu13-fail-ink: light-dark(#a9b0b5, #454d53);
  --color-tmu13-fail-ink: light-dark(oklch(75% 0.006 250), oklch(40% 0.01 250));
  --color-tmu13-line: light-dark(#d3d8db, #333b41);
  --color-tmu13-line: light-dark(oklch(86% 0.005 250), oklch(33% 0.011 250));
  --color-tmu13-bad: light-dark(#a11d1d, #f08a8a);
  --color-tmu13-bad: light-dark(oklch(44% 0.18 25), oklch(74% 0.14 25));
  --color-tmu13-ok: light-dark(#15613a, #62c78f);
  --color-tmu13-ok: light-dark(oklch(43% 0.11 155), oklch(78% 0.12 155));
  --color-tmu13-acc: light-dark(#0f4faf, #86b3ff);
  --color-tmu13-acc: light-dark(oklch(44% 0.17 262), oklch(80% 0.12 262));
  --color-tmu13-ring: light-dark(#0f4faf, #86b3ff);
  --color-tmu13-ring: light-dark(oklch(44% 0.17 262), oklch(80% 0.12 262));
  --color-tmu13-acc-ink: light-dark(#ffffff, #0c1526);
  --color-tmu13-acc-ink: light-dark(oklch(100% 0 0), oklch(18% 0.03 258));
  --color-tmu13-ok-bg: color-mix(in oklab, var(--color-tmu13-ok) 16%, transparent);
  --font-tmu13-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-tmu13-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-13:has(#tmu13-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-13:has(#tmu13-theme:checked) {
    color-scheme: light;
  }
}
```

## JavaScript
```js
(() => {
  const board = document.querySelector('#tmu13-board');
  if (!board) return;
  const set = (btn, on) => {
    const panel = btn.closest('[data-tmu13-panel]');
    if (!panel) return;
    btn.setAttribute('aria-pressed', String(on));
    panel.toggleAttribute('data-fixed', on);
  };
  const onClick = (e) => {
    const sw = e.target.closest('[data-tmu13-switch]');
    if (sw) return set(sw, sw.getAttribute('aria-pressed') !== 'true');
    const all = e.target.closest('[data-tmu13-all]');
    if (all) board.querySelectorAll('[data-tmu13-switch]').forEach((b) => set(b, all.dataset.tmu13All === '1'));
  };
  board.addEventListener('click', onClick);
  board.__tmuCleanup = () => board.removeEventListener('click', onClick);
})();
```
