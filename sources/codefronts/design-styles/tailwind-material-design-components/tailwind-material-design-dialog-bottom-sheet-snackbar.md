---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-dialog-bottom-sheet-snackbar/"
title: "Tailwind Material Design Dialog, Bottom Sheet and Snackbar"
section: "design-styles"
category: "tailwind-material-design-components"
category_name: "Material Design Components in Tailwind CSS"
description: "Three overlay patterns on the real <dialog> element &mdash; an alert dialog, a full dialog and a bottom sheet &mdash; plus a snackbar."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Design Dialog, Bottom Sheet and Snackbar
Source: https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-dialog-bottom-sheet-snackbar/

Three overlay patterns on the real <dialog> element &mdash; an alert dialog, a full dialog and a bottom sheet &mdash; plus a snackbar. The port replaces the CSS collection's checkbox-hack with showModal(), which is the correct upgrade: focus trapping, Esc, inertness and the top layer come from the platform, and Tailwind styles it with open:, backdrop: and starting:.
## HTML
```html
<section class="tmd-05 w-full min-h-svh bg-tmd05-bg font-tmd05-sans text-tmd05-onsurface px-5 py-9" aria-label="Material Design dialogs and sheets demo">
  <div class="w-[min(760px,100%)] mx-auto grid gap-6">
    <header class="grid gap-1.5">
      <h2 class="text-[26px] font-medium tracking-[-0.01em]">Dialogs, sheets &amp; snackbars</h2>
      <p class="text-sm text-tmd05-onvariant">Real <code class="font-tmd05-mono text-[12px]">&lt;dialog&gt;</code> elements: the platform owns modality, utilities own the motion.</p>
    </header>

    <div class="flex flex-wrap gap-3 p-5.5 rounded-3xl bg-tmd05-surface shadow-tmd05-1">
      <button type="button" data-open="tmd05-alert" class="relative overflow-hidden inline-flex items-center gap-2 min-h-10 px-6 rounded-full border-0 bg-tmd05-error text-tmd05-onerror cursor-pointer text-sm font-medium focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd05-error before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08] active:before:opacity-[0.12]"><span class="font-tmd05-icon text-[18px] leading-none" aria-hidden="true">delete</span>Delete project</button>
      <button type="button" data-open="tmd05-full" class="relative overflow-hidden inline-flex items-center gap-2 min-h-10 px-6 rounded-full border-0 bg-tmd05-primary text-tmd05-onprimary cursor-pointer text-sm font-medium focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd05-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08] active:before:opacity-[0.12]"><span class="font-tmd05-icon text-[18px] leading-none" aria-hidden="true">tune</span>Export settings</button>
      <button type="button" data-open="tmd05-sheet" class="relative overflow-hidden inline-flex items-center gap-2 min-h-10 px-6 rounded-full cursor-pointer bg-transparent border border-tmd05-outline text-tmd05-primary text-sm font-medium focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd05-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd05-icon text-[18px] leading-none" aria-hidden="true">expand_less</span>Bottom sheet</button>
      <button type="button" data-snack="Draft saved to Station 4" class="relative overflow-hidden inline-flex items-center gap-2 min-h-10 px-4 rounded-full border-0 bg-transparent cursor-pointer text-sm font-medium text-tmd05-primary focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd05-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]">Show snackbar</button>
    </div>

    <p class="text-sm leading-6 text-tmd05-onvariant text-pretty">Each overlay below is the same element with different box utilities. Press <kbd class="inline-block px-1.5 py-0.5 font-tmd05-mono text-[11px] bg-tmd05-surface border border-b-2 border-tmd05-outlinevariant rounded">Esc</kbd> to close any of them &mdash; that behaviour is not in the script.</p>

    <dialog id="tmd05-alert" role="alertdialog" aria-labelledby="tmd05-alert-t" aria-describedby="tmd05-alert-d" class="m-auto w-[min(420px,92vw)] p-6 rounded-[28px] border-0 bg-tmd05-surface text-tmd05-onsurface font-tmd05-sans shadow-tmd05-3 opacity-0 scale-95 transition-[opacity,scale,display,overlay] duration-200 transition-discrete open:opacity-100 open:scale-100 starting:open:opacity-0 starting:open:scale-95 backdrop:bg-black/40 backdrop:backdrop-blur-sm backdrop:transition-[opacity,display] backdrop:duration-200 motion-reduce:transition-none motion-reduce:scale-100">
      <div class="grid gap-4">
        <span class="font-tmd05-icon text-[24px] leading-none text-tmd05-error" aria-hidden="true">warning</span>
        <h3 id="tmd05-alert-t" class="text-[22px] font-normal tracking-[-0.005em]">Delete &ldquo;Tidal survey&rdquo;?</h3>
        <p id="tmd05-alert-d" class="text-sm leading-6 text-tmd05-onvariant text-pretty">Eighteen stations and 240 readings will be removed. This cannot be undone.</p>
        <div class="flex justify-end gap-2 pt-1">
          <button type="button" data-close class="relative overflow-hidden min-h-10 px-4 rounded-full border-0 bg-transparent cursor-pointer text-sm font-medium text-tmd05-primary focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd05-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]">Cancel</button>
          <button type="button" data-close data-snack="Project deleted" class="relative overflow-hidden min-h-10 px-5 rounded-full border-0 bg-tmd05-error text-tmd05-onerror cursor-pointer text-sm font-medium focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd05-error before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08] active:before:opacity-[0.12]">Delete</button>
        </div>
      </div>
    </dialog>

    <dialog id="tmd05-full" aria-labelledby="tmd05-full-t" class="m-auto w-[min(560px,92vw)] p-0 rounded-[28px] border-0 overflow-hidden bg-tmd05-surface text-tmd05-onsurface font-tmd05-sans shadow-tmd05-3 opacity-0 scale-95 transition-[opacity,scale,display,overlay] duration-200 transition-discrete open:opacity-100 open:scale-100 starting:open:opacity-0 starting:open:scale-95 backdrop:bg-black/40 backdrop:backdrop-blur-sm motion-reduce:transition-none motion-reduce:scale-100">
      <header class="flex items-center gap-3 px-4 py-3 border-b border-tmd05-outlinevariant">
        <button type="button" data-close aria-label="Close" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border-0 bg-transparent cursor-pointer text-tmd05-onsurface focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd05-primary before:absolute before:inset-1 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd05-icon text-[22px] leading-none" aria-hidden="true">close</span></button>
        <h3 id="tmd05-full-t" class="text-[17px] font-medium">Export settings</h3>
        <button type="button" data-close data-snack="Export queued" class="ml-auto relative overflow-hidden min-h-10 px-4 rounded-full border-0 bg-transparent cursor-pointer text-sm font-medium text-tmd05-primary focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd05-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]">Save</button>
      </header>
      <div class="grid gap-1 p-2 max-h-[min(420px,60svh)] overflow-y-auto">
        <label class="flex items-center gap-3 min-h-14 px-3 rounded-2xl cursor-pointer text-sm hover:bg-tmd05-surface2"><input type="radio" name="tmd05-fmt" checked class="w-5 h-5 accent-tmd05-primary">CSV &mdash; one row per reading</label>
        <label class="flex items-center gap-3 min-h-14 px-3 rounded-2xl cursor-pointer text-sm hover:bg-tmd05-surface2"><input type="radio" name="tmd05-fmt" class="w-5 h-5 accent-tmd05-primary">NetCDF &mdash; gridded</label>
        <label class="flex items-center gap-3 min-h-14 px-3 rounded-2xl cursor-pointer text-sm hover:bg-tmd05-surface2"><input type="radio" name="tmd05-fmt" class="w-5 h-5 accent-tmd05-primary">GeoJSON &mdash; station points</label>
        <hr class="my-1 border-0 border-t border-tmd05-outlinevariant">
        <label class="flex items-center gap-3 min-h-14 px-3 rounded-2xl cursor-pointer text-sm hover:bg-tmd05-surface2"><input type="checkbox" checked class="w-5 h-5 accent-tmd05-primary">Include QC flags</label>
        <label class="flex items-center gap-3 min-h-14 px-3 rounded-2xl cursor-pointer text-sm hover:bg-tmd05-surface2"><input type="checkbox" class="w-5 h-5 accent-tmd05-primary">Compress archive</label>
      </div>
    </dialog>

    <dialog id="tmd05-sheet" aria-labelledby="tmd05-sheet-t" class="mt-auto mb-0 mx-auto w-full max-w-[min(560px,100vw)] p-0 rounded-t-[28px] rounded-b-none border-0 bg-tmd05-surface text-tmd05-onsurface font-tmd05-sans shadow-tmd05-3 [transform:translateY(100%)] transition-[transform,display,overlay] duration-300 transition-discrete open:[transform:translateY(0)] starting:open:[transform:translateY(100%)] backdrop:bg-black/40 motion-reduce:transition-none motion-reduce:[transform:translateY(0)]">
      <div class="grid justify-items-center pt-3 pb-1"><span class="w-8 h-1 rounded-full bg-tmd05-outlinevariant" aria-hidden="true"></span></div>
      <h3 id="tmd05-sheet-t" class="px-6 pt-2 pb-1 text-[17px] font-medium">Share survey</h3>
      <div class="grid grid-cols-[repeat(auto-fit,minmax(96px,1fr))] gap-2 p-4">
        <button type="button" data-close data-snack="Link copied" class="grid justify-items-center gap-2 p-3 rounded-2xl border-0 bg-transparent cursor-pointer text-xs text-tmd05-onsurface hover:bg-tmd05-surface2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd05-primary"><span class="grid place-items-center w-12 h-12 rounded-full bg-tmd05-primarycontainer text-tmd05-onprimarycontainer font-tmd05-icon text-[22px] leading-none" aria-hidden="true">link</span>Copy link</button>
        <button type="button" data-close data-snack="Opening mail" class="grid justify-items-center gap-2 p-3 rounded-2xl border-0 bg-transparent cursor-pointer text-xs text-tmd05-onsurface hover:bg-tmd05-surface2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd05-primary"><span class="grid place-items-center w-12 h-12 rounded-full bg-tmd05-primarycontainer text-tmd05-onprimarycontainer font-tmd05-icon text-[22px] leading-none" aria-hidden="true">mail</span>Email</button>
        <button type="button" data-close data-snack="Added to drive" class="grid justify-items-center gap-2 p-3 rounded-2xl border-0 bg-transparent cursor-pointer text-xs text-tmd05-onsurface hover:bg-tmd05-surface2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd05-primary"><span class="grid place-items-center w-12 h-12 rounded-full bg-tmd05-primarycontainer text-tmd05-onprimarycontainer font-tmd05-icon text-[22px] leading-none" aria-hidden="true">cloud_upload</span>Drive</button>
        <button type="button" data-close class="grid justify-items-center gap-2 p-3 rounded-2xl border-0 bg-transparent cursor-pointer text-xs text-tmd05-onsurface hover:bg-tmd05-surface2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd05-primary"><span class="grid place-items-center w-12 h-12 rounded-full bg-tmd05-surface2 text-tmd05-onvariant font-tmd05-icon text-[22px] leading-none" aria-hidden="true">more_horiz</span>More</button>
      </div>
    </dialog>

    <output id="tmd05-snack" role="status" class="fixed left-1/2 bottom-6 z-50 [transform:translate(-50%,96px)] flex items-center gap-4 min-h-12 pl-4 pr-2 rounded-md bg-tmd05-inverse text-tmd05-oninverse text-sm shadow-tmd05-3 opacity-0 transition-[transform,opacity] duration-250 data-[show]:[transform:translate(-50%,0)] data-[show]:opacity-100 motion-reduce:transition-none">
      <span data-snack-text>Saved</span>
      <button type="button" data-snack-dismiss class="min-h-11 px-3 rounded-md border-0 bg-transparent cursor-pointer text-sm font-medium text-tmd05-inverseprimary focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd05-inverseprimary">Dismiss</button>
    </output>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmd05-bg: #ede7f6;
  --color-tmd05-bg: oklch(0.937 0.021 304);
  --color-tmd05-surface: #fffbfe;
  --color-tmd05-surface: oklch(0.992 0.006 334);
  --color-tmd05-surface2: #f3f0fa;
  --color-tmd05-surface2: oklch(0.96 0.014 299.8);
  --color-tmd05-primary: #4527a0;
  --color-tmd05-primary: oklch(0.395 0.181 286);
  --color-tmd05-onprimary: #ffffff;
  --color-tmd05-onprimary: oklch(1 0 89.9);
  --color-tmd05-primarycontainer: #e6dcff;
  --color-tmd05-primarycontainer: oklch(0.913 0.048 298.5);
  --color-tmd05-onprimarycontainer: #21005d;
  --color-tmd05-onprimarycontainer: oklch(0.242 0.14 286.1);
  --color-tmd05-onsurface: #1c1b1f;
  --color-tmd05-onsurface: oklch(0.225 0.008 297.2);
  --color-tmd05-onvariant: #4a4458;
  --color-tmd05-onvariant: oklch(0.401 0.034 298.6);
  --color-tmd05-outline: #79747e;
  --color-tmd05-outline: oklch(0.567 0.016 308.1);
  --color-tmd05-outlinevariant: #d1c4e9;
  --color-tmd05-outlinevariant: oklch(0.843 0.053 301.3);
  --color-tmd05-error: #b3261e;
  --color-tmd05-error: oklch(0.501 0.178 28.7);
  --color-tmd05-onerror: #ffffff;
  --color-tmd05-onerror: oklch(1 0 89.9);
  --color-tmd05-inverse: #322f35;
  --color-tmd05-inverse: oklch(0.311 0.011 308.1);
  --color-tmd05-oninverse: #f5eff7;
  --color-tmd05-oninverse: oklch(0.959 0.012 317.7);
  --color-tmd05-inverseprimary: #cfbcff;
  --color-tmd05-inverseprimary: oklch(0.834 0.094 297.3);
  --font-tmd05-sans: 'Roboto Flex', 'Roboto', system-ui, sans-serif;
  --font-tmd05-mono: 'Roboto Mono', ui-monospace, monospace;
  --font-tmd05-icon: 'Material Symbols Outlined';
  --shadow-tmd05-1: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 1px 3px 1px rgb(0 0 0 / 0.15);
  --shadow-tmd05-3: 0 4px 8px 3px rgb(0 0 0 / 0.15), 0 1px 3px 0 rgb(0 0 0 / 0.3);
}

.tmd-05 {
  width: 100%;
  min-height: 100svh;
}

.tmd-05 .font-tmd05-icon {
  font-feature-settings: 'liga';
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tmd-05').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var snack = root.querySelector('#tmd05-snack'),
        snackText = root.querySelector('[data-snack-text]'),
        timer;
    function toast(msg) {
      snackText.textContent = msg;
      snack.setAttribute('data-show', '');
      clearTimeout(timer);
      timer = setTimeout(function () { snack.removeAttribute('data-show'); }, 4000);
    }
    root.addEventListener('click', function (e) {
      var open = e.target.closest('[data-open]'),
          close = e.target.closest('[data-close]'),
          msg = e.target.closest('[data-snack]'),
          dismiss = e.target.closest('[data-snack-dismiss]');
      if (open) root.querySelector('#' + open.dataset.open).showModal();
      if (close) close.closest('dialog').close();
      if (dismiss) { snack.removeAttribute('data-show'); return; }
      if (msg) toast(msg.dataset.snack);
    });
    root.querySelectorAll('dialog').forEach(function (d) {
      d.addEventListener('click', function (e) { if (e.target === d) d.close(); });
    });
  });
})();
```
