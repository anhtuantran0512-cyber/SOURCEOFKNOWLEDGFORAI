---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-sidebar-focus-trap-and-restore-on-close/"
title: "Tailwind Sidebar Focus Trap and Restore on Close"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "A modal sidebar makes three promises to a keyboard user: focus moves in, focus stays in, focus comes back."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sidebar Focus Trap and Restore on Close
Source: https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-sidebar-focus-trap-and-restore-on-close/

A modal sidebar makes three promises to a keyboard user: focus moves in, focus stays in, focus comes back. The trap is hand-wired script &mdash; it has to be &mdash; but everything visual moves into the class list: the drawer states its closed and open transforms on itself and reads the open state through group-data-open:, so the whole [data-open] .drawer rule disappears.
## HTML
```html
<section class="tsb-02 block relative w-full min-h-svh bg-tsb02-bg text-tsb02-ink font-tsb02-sans leading-[1.55]" aria-label="Meridian sprint board">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-02-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-02-theme">
    <label class="grid place-items-center w-11 h-11 rounded-[0.7rem] border border-tsb02-line bg-tsb02-surf text-tsb02-ink cursor-pointer shadow-[0_0.15rem_0.5rem_oklch(20%_0.04_265/0.1)] peer-focus-visible:outline-2 peer-focus-visible:outline-tsb02-acc peer-focus-visible:outline-offset-2" for="tsb-02-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="group relative overflow-hidden grid grid-rows-[auto_minmax(0,1fr)] min-h-svh bg-tsb02-bg">
    <div class="flex flex-wrap items-center gap-2 py-2.5 pl-4 pr-[4.2rem] bg-tsb02-deep text-tsb02-ondeep" id="tsb-02-bg">
      <p class="mr-auto m-0 font-bold tracking-[-0.01em]">Meridian</p>
      <a class="inline-flex items-center min-h-11 px-2.5 rounded-lg text-[0.9rem] text-tsb02-ondeep/80 no-underline hover:text-tsb02-ondeep focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#tsb-02-main">Sprint 24</a>
      <a class="inline-flex items-center min-h-11 px-2.5 rounded-lg text-[0.9rem] text-tsb02-ondeep/80 no-underline hover:text-tsb02-ondeep focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#tsb-02-main">Backlog</a>
      <button class="order-3 inline-flex items-center gap-2 min-h-11 px-3.5 rounded-[0.6rem] border-0 bg-tsb02-acc text-tsb02-onacc font-tsb02-sans text-[0.9rem] font-semibold cursor-pointer [&>svg]:w-4 [&>svg]:h-4 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" type="button" id="tsb-02-open" aria-expanded="false" aria-controls="tsb-02-drawer">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 7h16M4 12h16M4 17h16" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
        Project menu
      </button>
    </div>

    <main class="grid grid-cols-[minmax(0,1fr)] content-start gap-3.5 p-4.5 min-w-0 sm:grid-cols-2 sm:p-6.5 lg:grid-cols-4 lg:p-8" id="tsb-02-main" aria-label="Sprint board">
      <article class="min-w-0 p-4 rounded-[0.8rem] bg-tsb02-surf border border-tsb02-line"><p class="m-0 mb-1.5 text-[0.7rem] tracking-[0.1em] uppercase text-tsb02-acc">In review</p><h3 class="m-0 mb-1.5 text-[0.98rem] leading-[1.25]">Rate limit on token exchange</h3><p class="m-0 text-[0.8rem] text-tsb02-mut">Priya Sharma &middot; 3 files</p></article>
      <article class="min-w-0 p-4 rounded-[0.8rem] bg-tsb02-surf border border-tsb02-line"><p class="m-0 mb-1.5 text-[0.7rem] tracking-[0.1em] uppercase text-tsb02-acc">In progress</p><h3 class="m-0 mb-1.5 text-[0.98rem] leading-[1.25]">Audit log retention window</h3><p class="m-0 text-[0.8rem] text-tsb02-mut">Jordan Lee &middot; 8 files</p></article>
      <article class="min-w-0 p-4 rounded-[0.8rem] bg-tsb02-surf border border-tsb02-line"><p class="m-0 mb-1.5 text-[0.7rem] tracking-[0.1em] uppercase text-tsb02-acc">Blocked</p><h3 class="m-0 mb-1.5 text-[0.98rem] leading-[1.25]">Billing webhook replay</h3><p class="m-0 text-[0.8rem] text-tsb02-mut">Sam Rivera &middot; 1 file</p></article>
      <article class="min-w-0 p-4 rounded-[0.8rem] bg-tsb02-surf border border-tsb02-line"><p class="m-0 mb-1.5 text-[0.7rem] tracking-[0.1em] uppercase text-tsb02-acc">Shipped</p><h3 class="m-0 mb-1.5 text-[0.98rem] leading-[1.25]">Session revoke endpoint</h3><p class="m-0 text-[0.8rem] text-tsb02-mut">Ada Okafor &middot; 5 files</p></article>
    </main>

    <div class="absolute inset-0 z-20 bg-[oklch(18%_0.03_265/0.5)] [&[hidden]]:hidden" data-tsb-02-scrim hidden></div>

    <div class="absolute inset-y-0 left-0 z-30 flex flex-col w-[min(19rem,86%)] bg-tsb02-surf border-r border-tsb02-line shadow-[0_1.5rem_3rem_oklch(18%_0.04_265/0.22)] -translate-x-full transition-transform duration-[240ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-data-open:translate-x-0 motion-reduce:duration-[1ms] [&[hidden]]:hidden" id="tsb-02-drawer" role="dialog" aria-modal="true" aria-labelledby="tsb-02-dh" hidden>
      <header class="flex items-center gap-2 px-3.5 py-3 border-b border-tsb02-line">
        <h3 class="mr-auto m-0 text-base font-bold" id="tsb-02-dh">Meridian project</h3>
        <button class="grid place-items-center w-11 h-11 rounded-[0.6rem] border border-tsb02-line bg-transparent text-tsb02-ink cursor-pointer [&>svg]:w-4 [&>svg]:h-4 focus-visible:outline-2 focus-visible:outline-tsb02-acc focus-visible:outline-offset-2" type="button" data-tsb-02-close>
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Close project menu</span>
        </button>
      </header>
      <nav class="flex-1 min-h-0 overflow-y-auto p-2 [overscroll-behavior:contain]" aria-label="Meridian project">
        <ul class="list-none m-0 p-0">
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.55rem] text-[0.93rem] text-tsb02-ink no-underline hover:bg-tsb02-accsoft focus-visible:outline-2 focus-visible:outline-tsb02-acc focus-visible:outline-offset-2 aria-[current=page]:bg-tsb02-accsoft aria-[current=page]:text-tsb02-acc aria-[current=page]:font-semibold" href="#tsb-02-main" aria-current="page">Sprint board</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.55rem] text-[0.93rem] text-tsb02-ink no-underline hover:bg-tsb02-accsoft focus-visible:outline-2 focus-visible:outline-tsb02-acc focus-visible:outline-offset-2" href="#tsb-02-main">Backlog</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.55rem] text-[0.93rem] text-tsb02-ink no-underline hover:bg-tsb02-accsoft focus-visible:outline-2 focus-visible:outline-tsb02-acc focus-visible:outline-offset-2" href="#tsb-02-main">Deployments</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.55rem] text-[0.93rem] text-tsb02-ink no-underline hover:bg-tsb02-accsoft focus-visible:outline-2 focus-visible:outline-tsb02-acc focus-visible:outline-offset-2" href="#tsb-02-main">Audit log</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.55rem] text-[0.93rem] text-tsb02-ink no-underline hover:bg-tsb02-accsoft focus-visible:outline-2 focus-visible:outline-tsb02-acc focus-visible:outline-offset-2" href="#tsb-02-main">Team settings</a></li>
        </ul>
      </nav>
      <footer class="px-3.5 py-2.5 border-t border-tsb02-line">
        <button class="w-full min-h-11 rounded-[0.6rem] border border-tsb02-line bg-transparent text-tsb02-ink font-tsb02-sans text-[0.9rem] font-semibold cursor-pointer focus-visible:outline-2 focus-visible:outline-tsb02-acc focus-visible:outline-offset-2" type="button" data-tsb-02-close>Done</button>
      </footer>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb02-bg: #f2f4f9;
  --color-tsb02-bg: oklch(96% 0.008 265);
  --color-tsb02-surf: #ffffff;
  --color-tsb02-surf: oklch(100% 0 0);
  --color-tsb02-deep: #101a34;
  --color-tsb02-deep: oklch(21% 0.06 265);
  --color-tsb02-line: #d5dbe8;
  --color-tsb02-line: oklch(88% 0.015 265);
  --color-tsb02-ink: #0d1428;
  --color-tsb02-ink: oklch(17% 0.04 265);
  --color-tsb02-mut: #5c6684;
  --color-tsb02-mut: oklch(48% 0.03 265);
  --color-tsb02-acc: #2f4de0;
  --color-tsb02-acc: oklch(50% 0.2 267);
  --color-tsb02-accsoft: #e5e9fd;
  --color-tsb02-accsoft: oklch(94% 0.03 267);
  --color-tsb02-ondeep: #eaeefb;
  --color-tsb02-ondeep: oklch(94% 0.015 265);
  --color-tsb02-onacc: #ffffff;
  --color-tsb02-onacc: oklch(100% 0 0);
  --font-tsb02-sans: 'Space Grotesk', system-ui, 'Segoe UI', sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.tsb-02 {
  width: 100%;
  min-height: 100svh;
}

.tsb-02 *,
.tsb-02 *::before,
.tsb-02 *::after {
  box-sizing: border-box;
}
/* Token flip for the pure-CSS theme toggle, with the two mandatory mirror blocks.
   Not expressible as utilities: it sets variables for a subtree, not a property on
   an element. --color-tsb02-onacc flips too, because dark accent needs dark ink on it. */

.tsb-02:has(.tsb-02-theme-input:checked) {
  --color-tsb02-bg: #070b16;
  --color-tsb02-surf: #101728;
  --color-tsb02-deep: #060a14;
  --color-tsb02-line: #212b45;
  --color-tsb02-ink: #e9edf9;
  --color-tsb02-mut: #93a0c0;
  --color-tsb02-acc: #93a8ff;
  --color-tsb02-acc: oklch(80% 0.12 268);
  --color-tsb02-accsoft: #1a2344;
  --color-tsb02-ondeep: #e9edf9;
  --color-tsb02-onacc: #070b16;
}

@media (prefers-color-scheme: dark) {
  .tsb-02 {
    --color-tsb02-bg: #070b16;
    --color-tsb02-surf: #101728;
    --color-tsb02-deep: #060a14;
    --color-tsb02-line: #212b45;
    --color-tsb02-ink: #e9edf9;
    --color-tsb02-mut: #93a0c0;
    --color-tsb02-acc: #93a8ff;
    --color-tsb02-acc: oklch(80% 0.12 268);
    --color-tsb02-accsoft: #1a2344;
    --color-tsb02-ondeep: #e9edf9;
    --color-tsb02-onacc: #070b16;
  }

  .tsb-02:has(.tsb-02-theme-input:checked) {
    --color-tsb02-bg: #f2f4f9;
    --color-tsb02-surf: #ffffff;
    --color-tsb02-deep: #101a34;
    --color-tsb02-line: #d5dbe8;
    --color-tsb02-ink: #0d1428;
    --color-tsb02-mut: #5c6684;
    --color-tsb02-acc: #2f4de0;
    --color-tsb02-acc: oklch(50% 0.2 267);
    --color-tsb02-accsoft: #e5e9fd;
    --color-tsb02-ondeep: #eaeefb;
    --color-tsb02-onacc: #ffffff;
  }
}

@media (prefers-color-scheme: light) {
  .tsb-02:has(.tsb-02-theme-input:checked) {
    --color-tsb02-bg: #070b16;
    --color-tsb02-surf: #101728;
    --color-tsb02-deep: #060a14;
    --color-tsb02-line: #212b45;
    --color-tsb02-ink: #e9edf9;
    --color-tsb02-mut: #93a0c0;
    --color-tsb02-acc: #93a8ff;
    --color-tsb02-acc: oklch(80% 0.12 268);
    --color-tsb02-accsoft: #1a2344;
    --color-tsb02-ondeep: #e9edf9;
    --color-tsb02-onacc: #070b16;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tsb-02').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var stage = root.querySelector('.group'),
        drawer = root.querySelector('#tsb-02-drawer'),
        scrim = root.querySelector('[data-tsb-02-scrim]'),
        trigger = root.querySelector('#tsb-02-open'),
        SEL = 'a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])',
        returnTo = null;
    function focusables() {
      return Array.prototype.slice.call(drawer.querySelectorAll(SEL))
        .filter(function (el) { return el.offsetParent !== null; });
    }
    function onKey(e) {
      if (e.key === 'Escape') { close(); return; }
      if (e.key !== 'Tab') return;
      var f = focusables(); if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
    function open() {
      returnTo = document.activeElement;
      drawer.hidden = false; scrim.hidden = false;
      stage.setAttribute('data-open', '');
      trigger.setAttribute('aria-expanded', 'true');
      requestAnimationFrame(function () { drawer.querySelector('[data-tsb-02-close]').focus(); });
      document.addEventListener('keydown', onKey);
    }
    function close() {
      document.removeEventListener('keydown', onKey);
      stage.removeAttribute('data-open');
      trigger.setAttribute('aria-expanded', 'false');
      drawer.hidden = true; scrim.hidden = true;
      (returnTo || trigger).focus({ preventScroll: true });
      returnTo = null;
    }
    trigger.addEventListener('click', open);
    scrim.addEventListener('click', close);
    root.querySelectorAll('[data-tsb-02-close]').forEach(function (b) { b.addEventListener('click', close); });
    root.__tsbCleanup = function () { document.removeEventListener('keydown', onKey); };
  });
})();
```
