---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-wcag-accessible-hamburger-menu-example/"
title: "Tailwind WCAG Accessible Hamburger Menu Example"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "The audit-proof build: a drawer implemented as a true modal dialog &mdash; role=dialog, aria-modal, focus moved in, trapped, restored, background inert,…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind WCAG Accessible Hamburger Menu Example
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-wcag-accessible-hamburger-menu-example/

The audit-proof build: a drawer implemented as a true modal dialog &mdash; role=dialog, aria-modal, focus moved in, trapped, restored, background inert, Escape wired, 44px targets, visible rings, reduced-motion path. Every requirement is tied to its WCAG success criterion, and in utilities the two that are usually missed &mdash; target size and focus visibility &mdash; are impossible to overlook because they are typed on every control.
## HTML
```html
<section class="thb-17 w-full min-h-svh grid justify-center content-start bg-thb17-bg font-thb17-sans text-thb17-ink px-5 py-9" aria-label="WCAG accessible hamburger menu demo">
  <div class="group relative w-[min(420px,88vw)] h-135 rounded-3xl overflow-hidden bg-thb17-bg border border-thb17-edge">
    <div id="thb17-page" class="h-full">
      <header class="flex items-center justify-between h-17 pl-5.5 pr-3.5 bg-thb17-panel border-b border-thb17-edge">
        <span class="flex items-center gap-2.5 text-[15.5px] font-bold">
          <i class="w-5 h-5 rounded-md bg-thb17-acc" aria-hidden="true"></i>CivicWorks
        </span>
        <button type="button" aria-expanded="false" aria-controls="thb17-menu" aria-label="Open navigation" class="flex items-center gap-2.5 min-h-11 min-w-11 px-3.5 rounded-[10px] border-2 border-thb17-ink bg-thb17-panel font-thb17-sans text-[13.5px] font-bold text-thb17-ink cursor-pointer transition-[background,color] duration-200 hover:bg-thb17-ink hover:text-thb17-panel focus-visible:outline-3 focus-visible:outline-thb17-focus focus-visible:outline-offset-2">
          <span class="relative block w-4.25 h-3.25" aria-hidden="true">
            <i class="absolute left-0 top-0 w-4.25 h-[2.5px] rounded-sm bg-current"></i>
            <i class="absolute left-0 top-[5.25px] w-4.25 h-[2.5px] rounded-sm bg-current"></i>
            <i class="absolute left-0 top-[10.5px] w-4.25 h-[2.5px] rounded-sm bg-current"></i>
          </span>
          <span aria-hidden="true">Menu</span>
        </button>
      </header>
      <div class="grid justify-items-start gap-3.5 p-5.5" aria-hidden="true">
        <div class="mb-1.5 px-3.25 py-2 rounded-lg bg-thb17-pass text-white text-xs font-extrabold tracking-[0.08em]">WCAG 2.2 AA</div>
        <div class="h-3 w-[84%] rounded-full bg-thb17-line"></div>
        <div class="h-3 w-[66%] rounded-full bg-thb17-line"></div>
        <div class="h-3 w-[75%] rounded-full bg-thb17-line"></div>
      </div>
    </div>
    <div aria-hidden="true" class="absolute inset-0 z-2 bg-[oklch(0.2_0.03_258/0.5)] opacity-0 invisible [transition:opacity_.3s,visibility_0s_.3s] group-data-open:opacity-100 group-data-open:visible group-data-open:[transition:opacity_.3s,visibility_0s_0s]"></div>
    <aside id="thb17-menu" role="dialog" aria-modal="true" aria-labelledby="thb17-title" tabindex="-1" class="absolute inset-y-0 right-0 z-3 flex flex-col w-[min(88%,330px)] bg-thb17-panel border-l border-thb17-edge shadow-[-20px_0_44px_-20px_oklch(0.2_0.04_258/0.5)] translate-x-full invisible [transition:translate_.38s_var(--ease-thb17),visibility_0s_.38s] group-data-open:translate-x-0 group-data-open:visible group-data-open:[transition:translate_.38s_var(--ease-thb17),visibility_0s_0s] motion-reduce:translate-x-0 motion-reduce:opacity-0 motion-reduce:[transition:opacity_.15s,visibility_0s_.15s] motion-reduce:group-data-open:opacity-100 motion-reduce:group-data-open:[transition:opacity_.15s]">
      <header class="flex items-center justify-between pt-4 pb-3 pl-5.5 pr-3.5 border-b-2 border-thb17-ink">
        <b id="thb17-title" class="text-[17px] font-bold">Navigation</b>
        <button type="button" aria-label="Close navigation" class="grid place-items-center min-h-11 min-w-11 rounded-[10px] border-2 border-thb17-ink bg-thb17-panel text-thb17-ink cursor-pointer transition-[background,color] duration-200 hover:bg-thb17-ink hover:text-thb17-panel focus-visible:outline-3 focus-visible:outline-thb17-focus focus-visible:outline-offset-2">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg>
        </button>
      </header>
      <nav aria-label="Primary">
        <ul class="list-none grid gap-0.5 px-3 py-2.5">
          <li><a href="#services" aria-current="page" class="flex items-center min-h-11 px-3 rounded-[9px] text-[15.5px] font-semibold text-thb17-ink underline decoration-transparent underline-offset-[3px] transition-[background,text-decoration-color] duration-150 hover:bg-thb17-hover hover:decoration-thb17-acc focus-visible:outline-3 focus-visible:outline-thb17-focus focus-visible:-outline-offset-3 aria-current:text-thb17-acc aria-current:font-bold aria-current:bg-[color-mix(in_oklch,var(--color-thb17-acc)_10%,transparent)]">Services</a></li>
          <li><a href="#permits" class="flex items-center min-h-11 px-3 rounded-[9px] text-[15.5px] font-semibold text-thb17-ink underline decoration-transparent underline-offset-[3px] transition-[background,text-decoration-color] duration-150 hover:bg-thb17-hover hover:decoration-thb17-acc focus-visible:outline-3 focus-visible:outline-thb17-focus focus-visible:-outline-offset-3">Permits &amp; licences</a></li>
          <li><a href="#payments" class="flex items-center min-h-11 px-3 rounded-[9px] text-[15.5px] font-semibold text-thb17-ink underline decoration-transparent underline-offset-[3px] transition-[background,text-decoration-color] duration-150 hover:bg-thb17-hover hover:decoration-thb17-acc focus-visible:outline-3 focus-visible:outline-thb17-focus focus-visible:-outline-offset-3">Payments</a></li>
          <li><a href="#accessibility" class="flex items-center min-h-11 px-3 rounded-[9px] text-[15.5px] font-semibold text-thb17-ink underline decoration-transparent underline-offset-[3px] transition-[background,text-decoration-color] duration-150 hover:bg-thb17-hover hover:decoration-thb17-acc focus-visible:outline-3 focus-visible:outline-thb17-focus focus-visible:-outline-offset-3">Accessibility statement</a></li>
          <li><a href="#contact" class="flex items-center min-h-11 px-3 rounded-[9px] text-[15.5px] font-semibold text-thb17-ink underline decoration-transparent underline-offset-[3px] transition-[background,text-decoration-color] duration-150 hover:bg-thb17-hover hover:decoration-thb17-acc focus-visible:outline-3 focus-visible:outline-thb17-focus focus-visible:-outline-offset-3">Contact us</a></li>
        </ul>
      </nav>
      <p class="mt-auto px-5.5 py-4 border-t border-thb17-edge text-xs leading-[1.9] text-thb17-mut text-pretty" aria-hidden="true">
        <kbd class="px-1.5 py-0.5 rounded-[5px] border-[1.5px] border-b-[3px] border-thb17-edge bg-thb17-bg font-thb17-mono text-[10.5px] font-bold">Tab</kbd> cycles inside &middot;
        <kbd class="px-1.5 py-0.5 rounded-[5px] border-[1.5px] border-b-[3px] border-thb17-edge bg-thb17-bg font-thb17-mono text-[10.5px] font-bold">Esc</kbd> closes &amp; restores focus &middot; page behind is <code class="px-1.25 py-0.5 rounded bg-thb17-line font-thb17-mono text-[11px]">inert</code>
      </p>
    </aside>
    <p role="status" aria-live="polite" class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb17-bg: #fafafc;
  --color-thb17-bg: oklch(0.98 0.004 250);
  --color-thb17-panel: #ffffff;
  --color-thb17-panel: oklch(1 0 0);
  --color-thb17-hover: #f0f1f6;
  --color-thb17-hover: oklch(0.95 0.008 255);
  --color-thb17-edge: #d7d9e2;
  --color-thb17-edge: oklch(0.87 0.01 250);
  --color-thb17-line: #e4e5ec;
  --color-thb17-line: oklch(0.9 0.008 250);
  --color-thb17-ink: #2b2e3d;
  --color-thb17-ink: oklch(0.22 0.02 255);
  --color-thb17-mut: #5f6377;
  --color-thb17-mut: oklch(0.45 0.018 255);
  --color-thb17-acc: #3b4fb8;
  --color-thb17-acc: oklch(0.48 0.16 258);
  --color-thb17-focus: #4a5ee0;
  --color-thb17-focus: oklch(0.55 0.2 262);
  --color-thb17-pass: #2f7d55;
  --color-thb17-pass: oklch(0.5 0.14 155);
  --font-thb17-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb17-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb17: cubic-bezier(0.32, 0.72, 0.28, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-17 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.thb-17 > .group').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var page = stage.querySelector('#thb17-page'),
        menu = stage.querySelector('#thb17-menu'),
        burger = stage.querySelector('button[aria-controls="thb17-menu"]'),
        closeBtn = stage.querySelector('button[aria-label="Close navigation"]'),
        scrim = stage.querySelector('div[aria-hidden="true"]'),
        live = stage.querySelector('[role="status"]'),
        opener = null;
    function focusables() {
      return menu.querySelectorAll('a[href], button, input, select, textarea, [tabindex]:not([tabindex="-1"])');
    }
    function set(open) {
      stage.toggleAttribute('data-open', open);
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
      if (open) {
        opener = document.activeElement;
        page.setAttribute('inert', '');
        closeBtn.focus();
        live.textContent = 'Navigation opened';
      } else {
        page.removeAttribute('inert');
        (opener || burger).focus();
        live.textContent = 'Navigation closed';
      }
    }
    burger.addEventListener('click', function () { set(true); });
    closeBtn.addEventListener('click', function () { set(false); });
    scrim.addEventListener('click', function () { set(false); });
    stage.addEventListener('keydown', function (e) {
      if (!stage.hasAttribute('data-open')) return;
      if (e.key === 'Escape') { set(false); return; }
      if (e.key !== 'Tab') return;
      var f = focusables(), first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
  });
})();
```
