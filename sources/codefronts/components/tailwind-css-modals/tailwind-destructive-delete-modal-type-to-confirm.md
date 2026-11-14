---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-destructive-delete-modal-type-to-confirm/"
title: "Tailwind Destructive Delete Modal with Type-to-Confirm Gate"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "The friction that prevents an accidental account deletion: plain-language consequences, a keyword the user must type, and a Delete button that stays…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Destructive Delete Modal with Type-to-Confirm Gate
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-destructive-delete-modal-type-to-confirm/

The friction that prevents an accidental account deletion: plain-language consequences, a keyword the user must type, and a Delete button that stays genuinely disabled until they do. disabled:opacity-40 disabled:cursor-not-allowed styles the gate; the attribute enforces it.
## HTML
```html
<section class="tm-11 w-full min-h-svh grid place-items-center bg-tm11-bg font-tm11-sans px-6 py-10">
  <button type="button" data-tm11-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-xl text-[15px] font-semibold text-tm11-dangerink bg-tm11-dangertint border border-tm11-dangeredge cursor-pointer transition-colors duration-200 hover:bg-tm11-dangerhover hover:border-tm11-danger focus-visible:outline-2 focus-visible:outline-tm11-danger focus-visible:outline-offset-2">Delete account</button>

  <dialog id="tm-11-dlg" aria-labelledby="tm-11-title" aria-describedby="tm-11-desc" class="m-auto w-[min(420px,94vw)] p-0 border-0 rounded-[18px] text-tm11-ink bg-tm11-card shadow-[0_40px_90px_-30px_#000,0_0_0_1px_var(--color-tm11-edge)] opacity-0 translate-y-2.5 scale-[0.97] transition-[opacity,translate,scale,overlay,display] duration-[260ms] transition-discrete open:opacity-100 open:translate-y-0 open:scale-100 open:starting:opacity-0 open:starting:translate-y-2.5 open:starting:scale-[0.97] open:backdrop:bg-tm11-scrim open:backdrop:backdrop-blur-[5px] motion-reduce:transition-none">
    <div class="px-8 pt-8 pb-6">
      <div aria-hidden="true" class="grid place-items-center size-14 mb-4.5 rounded-[14px] text-[26px] text-tm11-danger bg-tm11-dangertint shadow-[inset_0_0_0_1px_var(--color-tm11-dangeredge)]">&#9888;</div>
      <h2 id="tm-11-title" class="mb-2.5 text-[22px] font-bold text-tm11-hi">Delete your account?</h2>
      <p id="tm-11-desc" class="mb-5 text-sm leading-relaxed text-tm11-mut">This <b class="font-semibold text-tm11-hi">permanently</b> deletes your account, 3 projects and all associated data. This action <b class="font-semibold text-tm11-hi">cannot be undone</b>.</p>

      <label for="tm-11-confirm" class="block mb-2 text-[12.5px] text-tm11-mut">Type <code class="px-1.5 py-0.5 rounded bg-tm11-code font-tm11-mono font-bold tracking-[0.06em] text-tm11-dangerink">DELETE</code> to confirm</label>
      <input id="tm-11-confirm" type="text" autocomplete="off" placeholder="DELETE" class="w-full min-h-12 px-3.5 mb-5 rounded-[10px] border border-tm11-edge bg-tm11-well font-tm11-mono text-[15px] tracking-[0.1em] text-tm11-hi placeholder:text-tm11-faint transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tm11-danger focus:shadow-[0_0_0_3px_var(--color-tm11-ring)]">

      <div class="grid grid-cols-2 gap-3">
        <button type="button" data-tm11-cancel autofocus class="min-h-12 rounded-xl text-[14.5px] font-bold cursor-pointer text-tm11-ink bg-tm11-btn border border-tm11-btnedge transition-colors duration-200 hover:bg-tm11-btnhover hover:border-tm11-edge focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Cancel</button>
        <button type="button" data-tm11-delete disabled class="min-h-12 rounded-xl text-[14.5px] font-bold cursor-pointer border-0 bg-tm11-danger text-white transition-[filter,opacity] duration-200 hover:brightness-110 disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:brightness-100 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Delete account</button>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm11-bg: #080706;
  --color-tm11-bg: oklch(0.14 0.008 40);
  --color-tm11-card: #1a1513;
  --color-tm11-card: oklch(0.21 0.015 40);
  --color-tm11-well: #0e0a09;
  --color-tm11-well: oklch(0.16 0.01 40);
  --color-tm11-code: #241816;
  --color-tm11-code: oklch(0.24 0.025 30);
  --color-tm11-btn: #1c1614;
  --color-tm11-btn: oklch(0.22 0.012 40);
  --color-tm11-btnhover: #241c19;
  --color-tm11-btnhover: oklch(0.26 0.015 40);
  --color-tm11-btnedge: #3a2b28;
  --color-tm11-btnedge: oklch(0.32 0.02 30);
  --color-tm11-edge: #43302b;
  --color-tm11-edge: oklch(0.36 0.025 30);
  --color-tm11-hi: #fbeeeb;
  --color-tm11-hi: oklch(0.95 0.012 30);
  --color-tm11-ink: #e6d7d3;
  --color-tm11-ink: oklch(0.89 0.015 30);
  --color-tm11-mut: #c2aca7;
  --color-tm11-mut: oklch(0.76 0.02 30);
  --color-tm11-faint: #8a706b;
  --color-tm11-faint: oklch(0.58 0.025 30);
  --color-tm11-danger: #e8503f;
  --color-tm11-danger: oklch(0.62 0.22 27);
  --color-tm11-dangerink: #ffd9d4;
  --color-tm11-dangerink: oklch(0.9 0.05 25);
  --color-tm11-dangertint: #2b1513;
  --color-tm11-dangertint: oklch(0.25 0.06 27);
  --color-tm11-dangerhover: #3a1c18;
  --color-tm11-dangerhover: oklch(0.3 0.08 27);
  --color-tm11-dangeredge: #7a2e26;
  --color-tm11-dangeredge: oklch(0.42 0.13 27);
  --color-tm11-ring: #e8503f42;
  --color-tm11-ring: oklch(0.62 0.22 27 / 0.26);
  --color-tm11-scrim: #0604039e;
  --color-tm11-scrim: oklch(0.12 0.008 30 / 0.62);
  --font-tm11-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tm11-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tm-11 {
  width: 100%;
}

#tm-11-dlg::backdrop {
  background: oklch(0.12 0.008 30 / 0);
  backdrop-filter: blur(0px);
  transition: background .3s, backdrop-filter .3s, overlay .3s allow-discrete, display .3s allow-discrete;
}

@starting-style {
  #tm-11-dlg[open]::backdrop {
    background: oklch(0.12 0.008 30 / 0);
    backdrop-filter: blur(0px);
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tm-11');
  var dlg = root.querySelector('#tm-11-dlg');
  var input = root.querySelector('#tm-11-confirm');
  var del = root.querySelector('[data-tm11-delete]');
  var KEYWORD = 'DELETE';
  root.querySelector('[data-tm11-open]').addEventListener('click', function () {
    input.value = ''; del.disabled = true; dlg.showModal();   // always reopen clean
  });
  root.querySelector('[data-tm11-cancel]').addEventListener('click', function () { dlg.close(); });
  input.addEventListener('input', function () { del.disabled = input.value.trim() !== KEYWORD; });
  del.addEventListener('click', function () {
    del.textContent = 'Deleting…';
    setTimeout(function () { dlg.close(); del.textContent = 'Delete account'; }, 900);
  });
})();
```
