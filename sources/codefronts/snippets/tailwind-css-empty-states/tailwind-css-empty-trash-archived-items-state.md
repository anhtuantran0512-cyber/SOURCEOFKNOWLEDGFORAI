---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-empty-trash-archived-items-state/"
title: "Tailwind CSS Empty Trash / Archived Items State"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "A cloud drive's empty Trash that explains its own rules: how long deletions wait, and where to change it."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Empty Trash / Archived Items State
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-empty-trash-archived-items-state/

A cloud drive's empty Trash that explains its own rules: how long deletions wait, and where to change it. "Retention" is a disclosure (aria-expanded:) holding a radio segmented control; picking 7, 30 or 90 days rewrites the copy and animates the retention meter in the sidebar.
## HTML
```html
<div class="tes-15 w-full min-h-svh bg-tes15-bg font-tes15-sans text-tes15-ink antialiased">
  <div class="grid min-h-svh md:grid-cols-[14rem_minmax(0,1fr)]">
    <aside class="hidden flex-col gap-5 border-r border-tes15-line p-4 md:flex">
      <span class="flex items-center gap-2 px-2 font-semibold"><span aria-hidden="true" class="size-5 rounded-md bg-linear-to-br from-tes15-acc to-tes15-acc/50"></span>Slate Drive</span>
      <nav class="grid gap-0.5 text-sm">
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes15-mut hover:bg-tes15-sunk hover:text-tes15-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes15-acc">My files</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes15-mut hover:bg-tes15-sunk hover:text-tes15-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes15-acc">Shared</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes15-mut hover:bg-tes15-sunk hover:text-tes15-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes15-acc">Recent</a>
        <a href="#" aria-current="page" class="flex min-h-10 items-center rounded-lg bg-tes15-sunk px-3 font-medium focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes15-acc">Trash</a>
      </nav>
      <div class="mt-auto grid gap-2 rounded-xl bg-tes15-card p-3 ring-1 ring-tes15-line">
        <span aria-hidden="true" class="h-1.5 overflow-hidden rounded-full bg-tes15-sunk"><span id="tes15-fill" class="block h-full w-[8%] rounded-full bg-tes15-acc transition-[width] duration-500 ease-out"></span></span>
        <span id="tes15-note" class="text-xs text-tes15-mut">Trash is emptied 30 days after deletion</span>
      </div>
    </aside>
    <main class="flex min-w-0 flex-col">
      <header class="flex flex-wrap items-center justify-between gap-3 border-b border-tes15-line px-[clamp(1rem,4vw,2rem)] py-3">
        <div class="flex items-center gap-2 text-sm"><span class="text-tes15-mut">Slate Drive</span><span aria-hidden="true" class="text-tes15-line2">/</span><span class="font-medium">Trash</span></div>
        <div class="flex gap-2">
          <button type="button" data-ret aria-expanded="false" aria-controls="tes15-ret" class="min-h-11 rounded-lg border border-tes15-line px-3.5 text-sm transition hover:bg-tes15-sunk aria-expanded:bg-tes15-sunk aria-expanded:font-medium focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes15-acc">Retention</button>
          <button type="button" disabled class="min-h-11 rounded-lg border border-tes15-line px-3.5 text-sm text-tes15-mut disabled:cursor-not-allowed disabled:opacity-50">Empty trash</button>
        </div>
      </header>
      <div aria-hidden="true" class="hidden grid-cols-[minmax(0,3fr)_1fr_1fr_6rem] border-b border-tes15-line px-[clamp(1rem,4vw,2rem)] py-2.5 text-xs text-tes15-mut sm:grid"><span>Name</span><span>Deleted</span><span>Owner</span><span class="text-right">Size</span></div>
      <div class="grid flex-1 place-items-center px-5 py-14">
        <div class="grid max-w-md justify-items-center text-center">
          <span aria-hidden="true" class="relative grid h-22 w-20 place-items-end justify-center">
            <span class="absolute top-1 h-2.5 w-17 rounded-md bg-tes15-line2 transition-transform duration-500 group-hover:-rotate-6"></span>
            <span class="absolute top-0 left-1/2 h-1.5 w-6 -translate-x-1/2 rounded-t-md border-2 border-b-0 border-tes15-line2"></span>
            <span class="grid h-16 w-14 grid-cols-3 gap-2 rounded-b-xl bg-linear-to-b from-tes15-card to-tes15-sunk px-3 py-2.5 ring-1 ring-tes15-line"><i class="rounded-full bg-tes15-line"></i><i class="rounded-full bg-tes15-line"></i><i class="rounded-full bg-tes15-line"></i></span>
          </span>
          <h1 class="mt-6 text-xl font-semibold tracking-tight">Trash is empty</h1>
          <p id="tes15-copy" aria-live="polite" class="mt-2 text-sm/6 text-tes15-mut text-pretty">Nothing has been deleted in the last 30 days. Anything you remove will wait here before it goes for good.</p>
          <div class="mt-6 flex flex-wrap justify-center gap-2.5">
            <button type="button" class="min-h-11 rounded-xl bg-tes15-ink px-5 text-sm font-medium text-white transition hover:bg-tes15-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes15-acc">Back to my files</button>
            <button type="button" data-ret aria-expanded="false" aria-controls="tes15-ret" class="min-h-11 rounded-xl border border-tes15-line2 px-4 text-sm transition hover:bg-tes15-sunk aria-expanded:bg-tes15-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes15-acc">Change retention</button>
          </div>
          <fieldset id="tes15-ret" hidden class="mt-6 grid w-full justify-items-center gap-3 rounded-2xl bg-tes15-card p-4 ring-1 ring-tes15-line transition-opacity duration-300 starting:opacity-0">
            <legend class="sr-only">Keep deleted files for</legend>
            <p aria-hidden="true" class="text-xs font-medium text-tes15-mut">Keep deleted files for</p>
            <div class="flex rounded-xl bg-tes15-sunk p-1 text-sm">
              <label class="inline-flex min-h-10 cursor-pointer items-center rounded-lg px-4 text-tes15-mut transition has-checked:bg-tes15-card has-checked:font-medium has-checked:text-tes15-ink has-checked:shadow-sm has-focus-visible:outline-2 has-focus-visible:outline-tes15-acc"><input type="radio" name="tes15-days" value="7" class="sr-only">7 days</label>
              <label class="inline-flex min-h-10 cursor-pointer items-center rounded-lg px-4 text-tes15-mut transition has-checked:bg-tes15-card has-checked:font-medium has-checked:text-tes15-ink has-checked:shadow-sm has-focus-visible:outline-2 has-focus-visible:outline-tes15-acc"><input type="radio" name="tes15-days" value="30" checked class="sr-only">30 days</label>
              <label class="inline-flex min-h-10 cursor-pointer items-center rounded-lg px-4 text-tes15-mut transition has-checked:bg-tes15-card has-checked:font-medium has-checked:text-tes15-ink has-checked:shadow-sm has-focus-visible:outline-2 has-focus-visible:outline-tes15-acc"><input type="radio" name="tes15-days" value="90" class="sr-only">90 days</label>
            </div>
          </fieldset>
        </div>
      </div>
    </main>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes15-bg: #f8f8f6;
  --color-tes15-bg: oklch(0.978 0.003 110);
  --color-tes15-card: #ffffff;
  --color-tes15-card: oklch(1 0 0);
  --color-tes15-sunk: #efefec;
  --color-tes15-sunk: oklch(0.947 0.004 110);
  --color-tes15-line: #e2e2dd;
  --color-tes15-line: oklch(0.905 0.006 110);
  --color-tes15-line2: #c5c5bd;
  --color-tes15-line2: oklch(0.82 0.01 110);
  --color-tes15-ink: #1c1c19;
  --color-tes15-ink: oklch(0.22 0.005 110);
  --color-tes15-mut: #5e5e57;
  --color-tes15-mut: oklch(0.47 0.009 110);
  --color-tes15-acc: #0e7c86;
  --color-tes15-acc: oklch(0.53 0.09 205);
  --font-tes15-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-15 {
  width: 100%;
  min-height: 100svh;
}

.tes-15 [hidden] {
  display: none !important;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tes-15');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const ret = root.querySelector('#tes15-ret');
  const triggers = [...root.querySelectorAll('[data-ret]')];
  const widths = { 7: '4%', 30: '8%', 90: '17%' };
  triggers.forEach((t) => t.addEventListener('click', () => {
    const open = ret.hidden;
    ret.hidden = !open;
    triggers.forEach((x) => x.setAttribute('aria-expanded', String(open)));
    if (open) ret.querySelector('input:checked').focus(); else t.focus();
  }));
  ret.addEventListener('change', (e) => {
    const d = e.target.value;
    root.querySelector('#tes15-note').textContent = 'Trash is emptied ' + d + ' days after deletion';
    root.querySelector('#tes15-copy').textContent = 'Nothing has been deleted in the last ' + d + ' days. Anything you remove will wait here for ' + d + ' days before it goes for good.';
    root.querySelector('#tes15-fill').style.width = widths[d];
  });
})();
```
