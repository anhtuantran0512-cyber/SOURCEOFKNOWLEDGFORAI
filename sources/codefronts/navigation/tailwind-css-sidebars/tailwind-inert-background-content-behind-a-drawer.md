---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-inert-background-content-behind-a-drawer/"
title: "Tailwind Inert Background Content Behind a Drawer"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "The half of modal behaviour a focus trap cannot give you: everything behind the drawer is switched off with one attribute."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Inert Background Content Behind a Drawer
Source: https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-inert-background-content-behind-a-drawer/

The half of modal behaviour a focus trap cannot give you: everything behind the drawer is switched off with one attribute. inert takes the background out of the accessibility tree, out of the tab order and out of pointer events at once &mdash; and because Tailwind v4 ships an inert: variant, the visual consequence (a dimmed table) is declared on the element that goes inert, next to its normal state.
## HTML
```html
<section class="tsb-03 block relative w-full min-h-svh bg-tsb03-bg text-tsb03-ink font-tsb03-sans leading-[1.55]" aria-label="Sable order desk">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-03-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-03-theme">
    <label class="grid place-items-center w-11 h-11 rounded-full border border-tsb03-line bg-tsb03-surf text-tsb03-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-tsb03-acc peer-focus-visible:outline-offset-2" for="tsb-03-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="group relative overflow-hidden min-h-svh bg-tsb03-surf">
    <div class="min-w-0 transition-opacity duration-200 inert:opacity-45 motion-reduce:transition-none" id="tsb-03-content">
      <div class="flex flex-wrap items-center gap-1.5 py-2.5 pl-4 pr-[4.2rem] bg-tsb03-surf2 border-b border-tsb03-line">
        <p class="mr-auto m-0 font-tsb03-display text-[1.05rem]">Sable &mdash; order desk</p>
        <a class="inline-flex items-center min-h-11 px-2.5 text-[0.88rem] font-semibold text-tsb03-acc no-underline hover:underline focus-visible:outline-2 focus-visible:outline-tsb03-acc focus-visible:outline-offset-2" href="#tsb-03-content">Fulfilment</a>
        <a class="inline-flex items-center min-h-11 px-2.5 text-[0.88rem] font-semibold text-tsb03-acc no-underline hover:underline focus-visible:outline-2 focus-visible:outline-tsb03-acc focus-visible:outline-offset-2" href="#tsb-03-content">Returns</a>
        <button class="min-h-11 px-4 border border-tsb03-acc bg-tsb03-acc text-tsb03-surf font-tsb03-sans text-[0.9rem] font-semibold cursor-pointer focus-visible:outline-2 focus-visible:outline-tsb03-ink focus-visible:outline-offset-2" type="button" id="tsb-03-open" aria-expanded="false" aria-controls="tsb-03-drawer">Filters</button>
      </div>
      <table class="w-full border-collapse text-[0.9rem]">
        <thead><tr class="[&>th]:px-4 [&>th]:py-3 [&>th]:text-start [&>th]:border-b [&>th]:border-tsb03-line [&>th]:text-[0.74rem] [&>th]:tracking-[0.06em] [&>th]:uppercase [&>th]:font-semibold [&>th]:text-tsb03-mut"><th scope="col">Order</th><th scope="col">Customer</th><th scope="col">State</th><th scope="col"></th></tr></thead>
        <tbody class="[&>tr>td]:px-4 [&>tr>td]:py-3 [&>tr>td]:border-b [&>tr>td]:border-tsb03-line [&>tr>td]:min-w-0">
          <tr><td>SB-4417</td><td>Priya Sharma</td><td>Packing</td><td><a class="inline-flex items-center min-h-11 px-2.5 text-[0.88rem] font-semibold text-tsb03-acc no-underline hover:underline focus-visible:outline-2 focus-visible:outline-tsb03-acc focus-visible:outline-offset-2" href="#tsb-03-content">Open</a></td></tr>
          <tr><td>SB-4418</td><td>Jordan Lee</td><td>Awaiting stock</td><td><a class="inline-flex items-center min-h-11 px-2.5 text-[0.88rem] font-semibold text-tsb03-acc no-underline hover:underline focus-visible:outline-2 focus-visible:outline-tsb03-acc focus-visible:outline-offset-2" href="#tsb-03-content">Open</a></td></tr>
          <tr><td>SB-4421</td><td>Sam Rivera</td><td>Ready to ship</td><td><a class="inline-flex items-center min-h-11 px-2.5 text-[0.88rem] font-semibold text-tsb03-acc no-underline hover:underline focus-visible:outline-2 focus-visible:outline-tsb03-acc focus-visible:outline-offset-2" href="#tsb-03-content">Open</a></td></tr>
          <tr><td>SB-4423</td><td>Ada Okafor</td><td>Packing</td><td><a class="inline-flex items-center min-h-11 px-2.5 text-[0.88rem] font-semibold text-tsb03-acc no-underline hover:underline focus-visible:outline-2 focus-visible:outline-tsb03-acc focus-visible:outline-offset-2" href="#tsb-03-content">Open</a></td></tr>
          <tr><td>SB-4425</td><td>Tomas Vidal</td><td>Awaiting stock</td><td><a class="inline-flex items-center min-h-11 px-2.5 text-[0.88rem] font-semibold text-tsb03-acc no-underline hover:underline focus-visible:outline-2 focus-visible:outline-tsb03-acc focus-visible:outline-offset-2" href="#tsb-03-content">Open</a></td></tr>
        </tbody>
      </table>
    </div>

    <div class="absolute inset-0 z-20 bg-[oklch(25%_0.02_60/0.42)] [&[hidden]]:hidden" data-tsb-03-scrim hidden></div>

    <aside class="absolute inset-y-0 right-0 z-30 flex flex-col w-[min(18rem,84%)] bg-tsb03-surf border-l border-tsb03-line translate-x-full transition-transform duration-[220ms] ease-out group-data-open:translate-x-0 motion-reduce:duration-[1ms] [&[hidden]]:hidden" id="tsb-03-drawer" role="dialog" aria-modal="true" aria-labelledby="tsb-03-dh" hidden>
      <header class="flex items-center gap-2 px-3 py-2.5 border-b border-tsb03-line">
        <h3 class="mr-auto m-0 font-tsb03-display text-[1.1rem]" id="tsb-03-dh">Filters</h3>
        <button class="grid place-items-center w-11 h-11 border border-tsb03-line bg-transparent text-tsb03-ink cursor-pointer [&>svg]:w-4 [&>svg]:h-4 focus-visible:outline-2 focus-visible:outline-tsb03-acc focus-visible:-outline-offset-2" type="button" data-tsb-03-close>
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Close filters</span>
        </button>
      </header>
      <nav class="flex-1 min-h-0 overflow-y-auto [overscroll-behavior:contain]" aria-label="Order views">
        <ul class="list-none m-0 p-0">
          <li><a class="flex items-center min-w-0 min-h-11 px-3 py-2 text-[0.9rem] text-tsb03-ink no-underline border-b border-tsb03-line hover:bg-tsb03-surf2 focus-visible:outline-2 focus-visible:outline-tsb03-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb03-accsoft aria-[current=page]:text-tsb03-acc aria-[current=page]:font-semibold" href="#tsb-03-content" aria-current="page">All open orders</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-3 py-2 text-[0.9rem] text-tsb03-ink no-underline border-b border-tsb03-line hover:bg-tsb03-surf2 focus-visible:outline-2 focus-visible:outline-tsb03-acc focus-visible:-outline-offset-2" href="#tsb-03-content">Awaiting stock</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-3 py-2 text-[0.9rem] text-tsb03-ink no-underline border-b border-tsb03-line hover:bg-tsb03-surf2 focus-visible:outline-2 focus-visible:outline-tsb03-acc focus-visible:-outline-offset-2" href="#tsb-03-content">Ready to ship</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-3 py-2 text-[0.9rem] text-tsb03-ink no-underline border-b border-tsb03-line hover:bg-tsb03-surf2 focus-visible:outline-2 focus-visible:outline-tsb03-acc focus-visible:-outline-offset-2" href="#tsb-03-content">Returns queue</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-3 py-2 text-[0.9rem] text-tsb03-ink no-underline border-b border-tsb03-line hover:bg-tsb03-surf2 focus-visible:outline-2 focus-visible:outline-tsb03-acc focus-visible:-outline-offset-2" href="#tsb-03-content">Archived</a></li>
        </ul>
      </nav>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb03-bg: #f6f1e8;
  --color-tsb03-bg: oklch(95% 0.018 85);
  --color-tsb03-surf: #fffdf9;
  --color-tsb03-surf: oklch(99% 0.008 85);
  --color-tsb03-surf2: #efe7da;
  --color-tsb03-surf2: oklch(92% 0.022 80);
  --color-tsb03-line: #ddd1bd;
  --color-tsb03-line: oklch(85% 0.032 80);
  --color-tsb03-ink: #23201a;
  --color-tsb03-ink: oklch(24% 0.012 70);
  --color-tsb03-mut: #6d6455;
  --color-tsb03-mut: oklch(48% 0.02 75);
  --color-tsb03-acc: #8a4b1f;
  --color-tsb03-acc: oklch(48% 0.12 52);
  --color-tsb03-accsoft: #f2e4d5;
  --color-tsb03-accsoft: oklch(92% 0.03 60);
  --font-tsb03-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb03-display: 'Source Serif 4', 'Iowan Old Style', Palatino, Georgia, serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.tsb-03 {
  width: 100%;
  min-height: 100svh;
}

.tsb-03 *,
.tsb-03 *::before,
.tsb-03 *::after {
  box-sizing: border-box;
}
/* Token flip for the pure-CSS theme toggle, plus the two mandatory mirror blocks. */

.tsb-03:has(.tsb-03-theme-input:checked) {
  --color-tsb03-bg: #17140f;
  --color-tsb03-surf: #1f1b15;
  --color-tsb03-surf2: #292319;
  --color-tsb03-line: #3a3226;
  --color-tsb03-ink: #f2ece1;
  --color-tsb03-mut: #a89b87;
  --color-tsb03-acc: #e6a06a;
  --color-tsb03-acc: oklch(78% 0.11 55);
  --color-tsb03-accsoft: #35291d;
}

@media (prefers-color-scheme: dark) {
  .tsb-03 {
    --color-tsb03-bg: #17140f;
    --color-tsb03-surf: #1f1b15;
    --color-tsb03-surf2: #292319;
    --color-tsb03-line: #3a3226;
    --color-tsb03-ink: #f2ece1;
    --color-tsb03-mut: #a89b87;
    --color-tsb03-acc: #e6a06a;
    --color-tsb03-acc: oklch(78% 0.11 55);
    --color-tsb03-accsoft: #35291d;
  }

  .tsb-03:has(.tsb-03-theme-input:checked) {
    --color-tsb03-bg: #f6f1e8;
    --color-tsb03-surf: #fffdf9;
    --color-tsb03-surf2: #efe7da;
    --color-tsb03-line: #ddd1bd;
    --color-tsb03-ink: #23201a;
    --color-tsb03-mut: #6d6455;
    --color-tsb03-acc: #8a4b1f;
    --color-tsb03-acc: oklch(48% 0.12 52);
    --color-tsb03-accsoft: #f2e4d5;
  }
}

@media (prefers-color-scheme: light) {
  .tsb-03:has(.tsb-03-theme-input:checked) {
    --color-tsb03-bg: #17140f;
    --color-tsb03-surf: #1f1b15;
    --color-tsb03-surf2: #292319;
    --color-tsb03-line: #3a3226;
    --color-tsb03-ink: #f2ece1;
    --color-tsb03-mut: #a89b87;
    --color-tsb03-acc: #e6a06a;
    --color-tsb03-acc: oklch(78% 0.11 55);
    --color-tsb03-accsoft: #35291d;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tsb-03').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var stage = root.querySelector('.group'),
        drawer = root.querySelector('#tsb-03-drawer'),
        scrim = root.querySelector('[data-tsb-03-scrim]'),
        content = root.querySelector('#tsb-03-content'),
        openBtn = root.querySelector('#tsb-03-open'),
        supported = 'inert' in HTMLElement.prototype,
        returnTo = null;
    function behind() { return Array.prototype.slice.call(content.querySelectorAll('a[href], button:not([disabled])')); }
    function block(on) {
      if (supported) { content.inert = on; return; }
      content.setAttribute('aria-hidden', String(on));
      behind().forEach(function (el) { on ? el.setAttribute('tabindex', '-1') : el.removeAttribute('tabindex'); });
    }
    function onKey(e) { if (e.key === 'Escape') setOpen(false); }
    function setOpen(next) {
      if (next) returnTo = document.activeElement;
      drawer.hidden = scrim.hidden = !next;
      stage.toggleAttribute('data-open', next);
      openBtn.setAttribute('aria-expanded', String(next));
      block(next);
      if (next) {
        document.addEventListener('keydown', onKey);
        requestAnimationFrame(function () { drawer.querySelector('[data-tsb-03-close]').focus(); });
      } else {
        document.removeEventListener('keydown', onKey);
        (returnTo || openBtn).focus({ preventScroll: true });
      }
    }
    openBtn.addEventListener('click', function () { setOpen(true); });
    scrim.addEventListener('click', function () { setOpen(false); });
    root.querySelectorAll('[data-tsb-03-close]').forEach(function (b) { b.addEventListener('click', function () { setOpen(false); }); });
    root.__tsbCleanup = function () { document.removeEventListener('keydown', onKey); };
  });
})();
```
