---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/tailwind-drawer-close-button-native-dialog/"
title: "Tailwind Drawer Close Button with Native Dialog"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "A slide-over built on <dialog>: the browser traps focus, Esc closes it and focus returns to the opener for free."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Drawer Close Button with Native Dialog
Source: https://codefronts.com/components/tailwind-css-close-buttons/tailwind-drawer-close-button-native-dialog/

A slide-over built on <dialog>: the browser traps focus, Esc closes it and focus returns to the opener for free. Tailwind v4 animates both directions with open:translate-x-0, starting:open:translate-x-full and transition-discrete — the entry and the exit, with the dialog still painted while it slides out. The port turns the demo into a real filter drawer with an Apply footer.
## HTML
```html
<section class="tcb-10 w-full min-h-svh grid place-items-center bg-[linear-gradient(180deg,var(--color-tcb10-bg),var(--color-tcb10-bg2))] px-6 py-12 font-tcb10-sans text-tcb10-ink" aria-label="Native dialog drawer close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <button id="tcb-10-open" type="button" class="inline-flex min-h-12 cursor-pointer items-center gap-2.5 rounded-xl bg-tcb10-acc px-5.5 text-sm font-semibold text-white shadow-[0_12px_26px_-12px_var(--color-tcb10-glow)] transition duration-150 hover:-translate-y-px focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcb10-acc active:scale-97 motion-reduce:transition-none">
      <svg aria-hidden="true" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 6h16M7 12h10M10 18h4"/></svg>
      Filters
    </button>
    <dialog id="tcb-10-drawer" aria-labelledby="tcb-10-title" class="fixed inset-y-0 start-auto end-0 m-0 flex h-dvh max-h-none w-[min(20rem,85vw)] max-w-none translate-x-full flex-col border-0 border-s border-tcb10-line bg-white p-0 text-tcb10-ink shadow-[-24px_0_60px_-30px_var(--color-tcb10-shadow)] transition-[translate,display,overlay] transition-discrete duration-350 ease-[cubic-bezier(.4,0,.2,1)] not-open:hidden open:translate-x-0 starting:open:translate-x-full backdrop:bg-tcb10-scrim backdrop:backdrop-blur-[3px] motion-reduce:transition-none">
      <header class="flex items-center justify-between gap-3 border-b border-tcb10-line px-5 py-4">
        <h3 id="tcb-10-title" class="text-base font-semibold">Filters</h3>
        <button id="tcb-10-close" type="button" aria-label="Close filters" autofocus class="relative grid size-11 cursor-pointer place-items-center rounded-xl bg-tcb10-soft transition-colors hover:bg-tcb10-soft2 focus-visible:outline-[2.5px] focus-visible:outline-offset-2 focus-visible:outline-tcb10-acc active:scale-93 motion-reduce:transition-none">
          <span aria-hidden="true" class="relative size-4 before:absolute before:top-1/2 before:left-1/2 before:h-0.5 before:w-4 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-tcb10-ink after:absolute after:top-1/2 after:left-1/2 after:h-0.5 after:w-4 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-tcb10-ink"></span>
        </button>
      </header>
      <fieldset class="grid gap-1 px-5 py-4">
        <legend class="mb-2 text-xs font-semibold tracking-[0.08em] text-tcb10-mut uppercase">Category</legend>
        <label class="flex min-h-11 cursor-pointer items-center gap-3 text-sm"><input type="checkbox" checked class="size-4.5 accent-tcb10-acc"> Running shoes</label>
        <label class="flex min-h-11 cursor-pointer items-center gap-3 text-sm"><input type="checkbox" class="size-4.5 accent-tcb10-acc"> Trail</label>
        <label class="flex min-h-11 cursor-pointer items-center gap-3 text-sm"><input type="checkbox" class="size-4.5 accent-tcb10-acc"> Apparel</label>
      </fieldset>
      <p class="px-5 text-[13px]/[1.55] text-tcb10-mut">Esc, the ×, Apply or a backdrop click all close me — the browser handles the focus trap.</p>
      <footer class="mt-auto border-t border-tcb10-line p-5">
        <button id="tcb-10-apply" type="button" class="min-h-11 w-full cursor-pointer rounded-xl bg-tcb10-ink text-sm font-semibold text-white transition hover:brightness-125 focus-visible:outline-[2.5px] focus-visible:outline-offset-2 focus-visible:outline-tcb10-acc">Apply filters</button>
      </footer>
    </dialog>
    <p aria-hidden="true" class="rounded-full bg-white/70 px-3.5 py-2 font-tcb10-mono text-[11.5px] text-tcb10-mut ring-1 ring-black/8">open:translate-x-0 · starting:open: · transition-discrete</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb10-bg: #f1f6f9;
  --color-tcb10-bg: oklch(0.96 0.008 220);
  --color-tcb10-bg2: #e0eaf0;
  --color-tcb10-bg2: oklch(0.92 0.015 225);
  --color-tcb10-ink: #273746;
  --color-tcb10-ink: oklch(0.3 0.03 240);
  --color-tcb10-mut: #536473;
  --color-tcb10-mut: oklch(0.47 0.03 235);
  --color-tcb10-line: #dbe3e8;
  --color-tcb10-line: oklch(0.9 0.01 225);
  --color-tcb10-soft: #edf2f5;
  --color-tcb10-soft: oklch(0.95 0.008 220);
  --color-tcb10-soft2: #dfe7ec;
  --color-tcb10-soft2: oklch(0.91 0.015 220);
  --color-tcb10-acc: #1f7fb8;
  --color-tcb10-acc: oklch(0.55 0.13 235);
  --color-tcb10-glow: #1d6e9fb3;
  --color-tcb10-glow: oklch(0.5 0.12 235 / 0.7);
  --color-tcb10-shadow: #2a405580;
  --color-tcb10-shadow: oklch(0.35 0.06 225 / 0.5);
  --color-tcb10-scrim: #1b28365a;
  --color-tcb10-scrim: oklch(0.25 0.03 240 / 0.35);
  --font-tcb10-sans: 'Geist', system-ui, sans-serif;
  --font-tcb10-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-10 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const drawer = document.getElementById('tcb-10-drawer');
  if (!drawer || drawer.dataset.wired) return;
  drawer.dataset.wired = '1';
  document.getElementById('tcb-10-open').addEventListener('click', () => drawer.showModal());
  document.getElementById('tcb-10-close').addEventListener('click', () => drawer.close());
  document.getElementById('tcb-10-apply').addEventListener('click', () => drawer.close());
  drawer.addEventListener('click', (e) => { if (e.target === drawer) drawer.close(); });
})();
```
