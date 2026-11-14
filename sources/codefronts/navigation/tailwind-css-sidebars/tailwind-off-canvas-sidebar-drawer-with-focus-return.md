---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-off-canvas-sidebar-drawer-with-focus-return/"
title: "Tailwind Off Canvas Sidebar Drawer with Focus Return"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "The full contract in one demo, and the collection's closing argument for the port: focus in, focus trapped, background inert, Esc closes, focus returns…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Off Canvas Sidebar Drawer with Focus Return
Source: https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-off-canvas-sidebar-drawer-with-focus-return/

The full contract in one demo, and the collection's closing argument for the port: focus in, focus trapped, background inert, Esc closes, focus returns &mdash; all in script, because all of it is behaviour &mdash; while every pixel of the drawer's two states lives in one class list on one element. Demos 02, 03 and 19 are the same lesson at increasing completeness.
## HTML
```html
<section class="tsb-19 block relative w-full min-h-svh bg-tsb19-bg text-tsb19-ink font-tsb19-sans leading-[1.55]" aria-label="Fern Daily">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-19-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-19-theme">
    <label class="grid place-items-center w-11 h-11 rounded-[0.5rem] border border-tsb19-line bg-tsb19-surf text-tsb19-ink cursor-pointer shadow-[0_0.4rem_1rem_oklch(0%_0_0/0.25)] peer-focus-visible:outline-2 peer-focus-visible:outline-tsb19-acc peer-focus-visible:outline-offset-2" for="tsb-19-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="group relative overflow-hidden h-svh bg-tsb19-surf" id="tsb-19-screen">
    <div class="flex flex-col h-full transition-opacity duration-200 inert:opacity-40 motion-reduce:transition-none" id="tsb-19-page">
      <div class="flex items-center gap-2.5 py-2.5 pl-2.5 pr-[4.2rem] border-b border-tsb19-line">
        <button class="grid place-items-center w-11 h-11 rounded-[0.5rem] border-0 bg-tsb19-surf2 text-tsb19-ink cursor-pointer [&>svg]:w-5 [&>svg]:h-5 focus-visible:outline-2 focus-visible:outline-tsb19-acc focus-visible:outline-offset-2" type="button" id="tsb-19-open" aria-expanded="false" aria-controls="tsb-19-drawer">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 7h16M4 12h16M4 17h16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Open sections</span>
        </button>
        <p class="m-0 font-tsb19-display text-[1.15rem] font-bold tracking-[0.04em] uppercase text-tsb19-acc">Fern Daily</p>
      </div>
      <article class="flex-1 min-h-0 overflow-y-auto px-5 pt-4.5 pb-10 [overscroll-behavior:contain] r46:px-9 r46:pt-8 r46:pb-12">
        <p class="m-0 mb-1 font-tsb19-display text-[0.74rem] tracking-[0.14em] uppercase text-tsb19-acc">Infrastructure</p>
        <h2 class="m-0 mb-1.5 max-w-[34rem] font-tsb19-display text-[clamp(1.5rem,4vw,2.2rem)] leading-[1.08]">Regions added in the third quarter</h2>
        <p class="m-0 mb-4 text-[0.82rem] text-tsb19-mut">Alex Chen &middot; 6 min read</p>
        <p class="m-0 mb-3 max-w-[38rem] text-[0.94rem] text-tsb19-mut text-pretty">Three new regions came online this quarter, each with an independent control plane and its own certificate authority.</p>
        <p class="m-0 mb-3 max-w-[38rem] text-[0.94rem] text-tsb19-mut text-pretty">Promotion remains a pointer move, so rollback stays instant even across regions. The verification step is the slow part, and it is deliberately manual.</p>
        <p class="m-0 mb-3 max-w-[38rem] text-[0.94rem] text-tsb19-mut text-pretty">Failover drills now run monthly per region, with an observer from a second team. The runbook lives in the handbook under Operations.</p>
        <a class="inline-flex items-center min-h-11 text-[0.9rem] font-semibold text-tsb19-acc focus-visible:outline-2 focus-visible:outline-tsb19-acc focus-visible:outline-offset-2" href="#tsb-19-screen">Read the full report</a>
      </article>
    </div>

    <div class="absolute inset-0 z-20 bg-[oklch(12%_0.01_60/0.5)] [&[hidden]]:hidden" data-tsb-19-scrim hidden></div>

    <div class="absolute inset-y-0 left-0 z-30 flex flex-col w-[min(15rem,80%)] bg-tsb19-surf border-r border-tsb19-line shadow-[0.6rem_0_2rem_oklch(0%_0_0/0.35)] -translate-x-full transition-transform duration-[260ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-data-open:translate-x-0 motion-reduce:duration-[1ms] [&[hidden]]:hidden" id="tsb-19-drawer" role="dialog" aria-modal="true" aria-labelledby="tsb-19-dh" hidden>
      <div class="flex items-center gap-1.5 px-2.5 py-2 border-b border-tsb19-line">
        <p class="mr-auto m-0 font-tsb19-display text-[0.78rem] tracking-[0.14em] uppercase text-tsb19-mut" id="tsb-19-dh">Sections</p>
        <button class="grid place-items-center w-11 h-11 rounded-[0.5rem] border-0 bg-tsb19-surf2 text-tsb19-ink cursor-pointer [&>svg]:w-4 [&>svg]:h-4 focus-visible:outline-2 focus-visible:outline-tsb19-acc focus-visible:outline-offset-2" type="button" data-tsb-19-close>
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Close sections</span>
        </button>
      </div>
      <nav class="flex-1 min-h-0 overflow-y-auto p-1 [overscroll-behavior:contain]" aria-label="Fern Daily sections">
        <ul class="list-none m-0 p-0">
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.4rem] text-[0.89rem] text-tsb19-ink no-underline hover:bg-tsb19-surf2 focus-visible:outline-2 focus-visible:outline-tsb19-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb19-accsoft aria-[current=page]:text-tsb19-acc aria-[current=page]:font-semibold" href="#tsb-19-screen" aria-current="page">Infrastructure</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.4rem] text-[0.89rem] text-tsb19-ink no-underline hover:bg-tsb19-surf2 focus-visible:outline-2 focus-visible:outline-tsb19-acc focus-visible:-outline-offset-2" href="#tsb-19-screen">Security</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.4rem] text-[0.89rem] text-tsb19-ink no-underline hover:bg-tsb19-surf2 focus-visible:outline-2 focus-visible:outline-tsb19-acc focus-visible:-outline-offset-2" href="#tsb-19-screen">Billing</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.4rem] text-[0.89rem] text-tsb19-ink no-underline hover:bg-tsb19-surf2 focus-visible:outline-2 focus-visible:outline-tsb19-acc focus-visible:-outline-offset-2" href="#tsb-19-screen">Field notes</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.4rem] text-[0.89rem] text-tsb19-ink no-underline hover:bg-tsb19-surf2 focus-visible:outline-2 focus-visible:outline-tsb19-acc focus-visible:-outline-offset-2" href="#tsb-19-screen">Audit log</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.4rem] text-[0.89rem] text-tsb19-ink no-underline hover:bg-tsb19-surf2 focus-visible:outline-2 focus-visible:outline-tsb19-acc focus-visible:-outline-offset-2" href="#tsb-19-screen">Newsletters</a></li>
          <li><a class="flex items-center min-w-0 min-h-11 px-2.5 py-2 rounded-[0.4rem] text-[0.89rem] text-tsb19-ink no-underline hover:bg-tsb19-surf2 focus-visible:outline-2 focus-visible:outline-tsb19-acc focus-visible:-outline-offset-2" href="#tsb-19-screen">Archive</a></li>
        </ul>
      </nav>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb19-bg: #1c1a18;
  --color-tsb19-bg: oklch(23% 0.008 60);
  --color-tsb19-surf: #262320;
  --color-tsb19-surf: oklch(27% 0.01 60);
  --color-tsb19-surf2: #302c28;
  --color-tsb19-surf2: oklch(31% 0.012 60);
  --color-tsb19-line: #3d3833;
  --color-tsb19-line: oklch(37% 0.014 60);
  --color-tsb19-ink: #f5efe8;
  --color-tsb19-ink: oklch(95% 0.012 70);
  --color-tsb19-mut: #ab9f93;
  --color-tsb19-mut: oklch(71% 0.02 70);
  --color-tsb19-acc: #ef7a52;
  --color-tsb19-acc: oklch(70% 0.16 40);
  --color-tsb19-accsoft: #3a251c;
  --color-tsb19-accsoft: oklch(30% 0.05 40);
  --font-tsb19-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb19-display: 'Archivo Narrow', 'Roboto Condensed', ui-sans-serif, system-ui, sans-serif;
  --breakpoint-r46: 46rem;
}
/* Root rule: the full-bleed contract. The screen inside it is h-svh, because two
   independent scroll panes need a bounded stage. */

.tsb-19 {
  width: 100%;
  min-height: 100svh;
}

.tsb-19 *,
.tsb-19 *::before,
.tsb-19 *::after {
  box-sizing: border-box;
}
/* Dark-first demo: the @theme block IS the dark palette, light mirror below. */

.tsb-19:has(.tsb-19-theme-input:checked) {
  --color-tsb19-bg: #f8f4ef;
  --color-tsb19-surf: #ffffff;
  --color-tsb19-surf2: #efe9e2;
  --color-tsb19-line: #ded5cb;
  --color-tsb19-ink: #221e1a;
  --color-tsb19-mut: #6a6058;
  --color-tsb19-acc: #9e3d18;
  --color-tsb19-acc: oklch(48% 0.14 40);
  --color-tsb19-accsoft: #f6e2d8;
}

@media (prefers-color-scheme: light) {
  .tsb-19 {
    --color-tsb19-bg: #f8f4ef;
    --color-tsb19-surf: #ffffff;
    --color-tsb19-surf2: #efe9e2;
    --color-tsb19-line: #ded5cb;
    --color-tsb19-ink: #221e1a;
    --color-tsb19-mut: #6a6058;
    --color-tsb19-acc: #9e3d18;
    --color-tsb19-acc: oklch(48% 0.14 40);
    --color-tsb19-accsoft: #f6e2d8;
  }

  .tsb-19:has(.tsb-19-theme-input:checked) {
    --color-tsb19-bg: #1c1a18;
    --color-tsb19-surf: #262320;
    --color-tsb19-surf2: #302c28;
    --color-tsb19-line: #3d3833;
    --color-tsb19-ink: #f5efe8;
    --color-tsb19-mut: #ab9f93;
    --color-tsb19-acc: #ef7a52;
    --color-tsb19-acc: oklch(70% 0.16 40);
    --color-tsb19-accsoft: #3a251c;
  }
}

@media (prefers-color-scheme: dark) {
  .tsb-19:has(.tsb-19-theme-input:checked) {
    --color-tsb19-bg: #f8f4ef;
    --color-tsb19-surf: #ffffff;
    --color-tsb19-surf2: #efe9e2;
    --color-tsb19-line: #ded5cb;
    --color-tsb19-ink: #221e1a;
    --color-tsb19-mut: #6a6058;
    --color-tsb19-acc: #9e3d18;
    --color-tsb19-acc: oklch(48% 0.14 40);
    --color-tsb19-accsoft: #f6e2d8;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tsb-19').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var screen = root.querySelector('#tsb-19-screen'),
        drawer = root.querySelector('#tsb-19-drawer'),
        page = root.querySelector('#tsb-19-page'),
        scrim = root.querySelector('[data-tsb-19-scrim]'),
        trigger = root.querySelector('#tsb-19-open'),
        supportsInert = 'inert' in HTMLElement.prototype,
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
      drawer.hidden = scrim.hidden = false;
      screen.setAttribute('data-open', '');
      trigger.setAttribute('aria-expanded', 'true');
      if (supportsInert) page.inert = true; else page.setAttribute('aria-hidden', 'true');
      document.addEventListener('keydown', onKey);
      requestAnimationFrame(function () { drawer.querySelector('[data-tsb-19-close]').focus(); });
    }
    function close() {
      document.removeEventListener('keydown', onKey);
      if (supportsInert) page.inert = false; else page.removeAttribute('aria-hidden');
      screen.removeAttribute('data-open');
      trigger.setAttribute('aria-expanded', 'false');
      drawer.hidden = scrim.hidden = true;
      (returnTo || trigger).focus({ preventScroll: true });
      returnTo = null;
    }
    trigger.addEventListener('click', open);
    scrim.addEventListener('click', close);
    root.querySelectorAll('[data-tsb-19-close]').forEach(function (b) { b.addEventListener('click', close); });
    root.__tsbCleanup = function () {
      document.removeEventListener('keydown', onKey);
      if (supportsInert) page.inert = false;
    };
  });
})();
```
