---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-popover-fallback-polyfill/"
title: "Tailwind Popover Fallback and Polyfill"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "Popover and anchor positioning ship on different timelines, so one test isn't enough."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Popover Fallback and Polyfill
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-popover-fallback-polyfill/

Popover and anchor positioning ship on different timelines, so one test isn't enough. The script detects three features — popover, anchor positioning and discrete transitions — writes each to a data-* attribute on the root, and every visual reads them through group-data-[anchor=yes]/root: variants. The panel layers up: a plain positioned box with no API, popover dismissal on top, anchoring on top of that.
## HTML
```html
<section data-tpop16-root data-popover="unknown" data-anchor="unknown" data-discrete="unknown" class="tpop-16 transition-[--tpop16-d] duration-300 ease-in-out motion-reduce:transition-none dark:[--tpop16-d:1] [[data-theme=dark]_&]:[--tpop16-d:1] [[data-theme=light]_&]:[--tpop16-d:0] group/root relative w-full min-h-svh bg-tpop16-bg px-4 py-9.5 font-tpop16-sans text-tpop16-ink" aria-label="Popover fallback and polyfill demo">
  <div class="grid min-h-[calc(100svh-76px)] max-w-full place-items-center">
    <div class="w-full min-w-0 max-w-[27rem] rounded-xl border border-tpop16-rule bg-tpop16-s1 px-4.5 pt-5 pb-4.5 shadow-[0_16px_36px_-28px_oklch(0.2_0.02_255/0.5)]">
      <p class="mb-2 text-[10.5px] font-bold uppercase tracking-[0.2em] text-tpop16-mut">Support probe</p>
      <h2 class="mb-4 text-[clamp(20px,4.4vw,25px)] font-semibold leading-tight tracking-[-0.02em]">Three features, three tests</h2>
      <dl class="mb-4 grid gap-px overflow-hidden rounded-lg border border-tpop16-rule bg-tpop16-rule">
        <div class="flex min-w-0 flex-wrap items-center justify-between gap-2 bg-tpop16-s2 px-3 py-2.5">
          <dt class="min-w-0 font-tpop16-mono text-[12.5px] font-semibold">popover attribute</dt>
          <dd id="tpop-16-r1" class="rounded-full bg-tpop16-rule/60 px-2 py-0.5 text-[11px] font-bold uppercase tracking-[0.06em] text-tpop16-mut group-data-[popover=yes]/root:bg-tpop16-ok/12 group-data-[popover=yes]/root:text-tpop16-ok group-data-[popover=no]/root:bg-tpop16-no/12 group-data-[popover=no]/root:text-tpop16-no">checking…</dd>
        </div>
        <div class="flex min-w-0 flex-wrap items-center justify-between gap-2 bg-tpop16-s2 px-3 py-2.5">
          <dt class="min-w-0 font-tpop16-mono text-[12.5px] font-semibold">anchor-name</dt>
          <dd id="tpop-16-r2" class="rounded-full bg-tpop16-rule/60 px-2 py-0.5 text-[11px] font-bold uppercase tracking-[0.06em] text-tpop16-mut group-data-[anchor=yes]/root:bg-tpop16-ok/12 group-data-[anchor=yes]/root:text-tpop16-ok group-data-[anchor=no]/root:bg-tpop16-no/12 group-data-[anchor=no]/root:text-tpop16-no">checking…</dd>
        </div>
        <div class="flex min-w-0 flex-wrap items-center justify-between gap-2 bg-tpop16-s2 px-3 py-2.5">
          <dt class="min-w-0 font-tpop16-mono text-[12.5px] font-semibold">allow-discrete</dt>
          <dd id="tpop-16-r3" class="rounded-full bg-tpop16-rule/60 px-2 py-0.5 text-[11px] font-bold uppercase tracking-[0.06em] text-tpop16-mut group-data-[discrete=yes]/root:bg-tpop16-ok/12 group-data-[discrete=yes]/root:text-tpop16-ok group-data-[discrete=no]/root:bg-tpop16-no/12 group-data-[discrete=no]/root:text-tpop16-no">checking…</dd>
        </div>
      </dl>
      <button id="tpop-16-trigger" type="button" popovertarget="tpop-16-panel" aria-expanded="false" class="min-h-11 w-full cursor-pointer rounded-lg bg-tpop16-ink px-3.5 text-[13.5px] font-semibold text-tpop16-s1 transition-colors [anchor-name:--tpop16-a] hover:bg-tpop16-ink/88 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop16-ok aria-expanded:bg-tpop16-ink/80">Open the layered panel</button>
      <p class="mt-3 text-[12.5px] leading-relaxed text-tpop16-mut">The panel is a plain positioned box first, a popover second, and anchored third.</p>
    </div>
  </div>

  <div popover="auto" id="tpop-16-panel" role="group" aria-label="Layered panel" class="absolute inset-x-4 bottom-4 m-0 w-auto max-w-[calc(100%-32px)] rounded-xl border border-tpop16-rule bg-tpop16-s1 p-3.5 text-tpop16-ink opacity-100 shadow-[0_18px_36px_-22px_oklch(0.2_0.02_255/0.5)] transition-[opacity,translate,display,overlay] duration-150 ease-out transition-discrete [position-anchor:--tpop16-a] [position-area:block-end_span-inline-end] [position-try-fallbacks:flip-block] starting:open:-translate-y-1 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:fixed supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:mt-2 supports-[anchor-name:--a]:w-[min(21rem,calc(100vw-32px))] supports-[anchor-name:--a]:max-w-[calc(100vw-32px)]">
    <p class="mb-2.5 text-[11px] font-bold uppercase tracking-[0.16em] text-tpop16-mut">Layer report</p>
    <ul class="grid gap-2">
      <li class="flex min-w-0 items-start gap-2.5 text-[13px] leading-normal"><span aria-hidden="true" class="mt-1.5 size-1.5 flex-none rounded-full bg-tpop16-ok"></span><span><strong class="font-semibold">Baseline</strong> · absolutely positioned, no top layer</span></li>
      <li class="flex min-w-0 items-start gap-2.5 text-[13px] leading-normal opacity-45 group-data-[popover=yes]/root:opacity-100"><span aria-hidden="true" class="mt-1.5 size-1.5 flex-none rounded-full bg-tpop16-rule group-data-[popover=yes]/root:bg-tpop16-ok"></span><span><strong class="font-semibold">Enhanced</strong> · popover owns dismissal and the top layer</span></li>
      <li class="flex min-w-0 items-start gap-2.5 text-[13px] leading-normal opacity-45 group-data-[anchor=yes]/root:opacity-100"><span aria-hidden="true" class="mt-1.5 size-1.5 flex-none rounded-full bg-tpop16-rule group-data-[anchor=yes]/root:bg-tpop16-ok"></span><span><strong class="font-semibold">Enhanced</strong> · anchor positioning owns placement</span></li>
      <li class="flex min-w-0 items-start gap-2.5 text-[13px] leading-normal opacity-45 group-data-[discrete=yes]/root:opacity-100"><span aria-hidden="true" class="mt-1.5 size-1.5 flex-none rounded-full bg-tpop16-rule group-data-[discrete=yes]/root:bg-tpop16-ok"></span><span><strong class="font-semibold">Enhanced</strong> · allow-discrete owns the entry fade</span></li>
    </ul>
    <p class="mt-3 border-t border-tpop16-rule pt-2.5 text-[12px] leading-normal text-tpop16-mut">Polyfill for the attribute: <span class="font-tpop16-mono text-tpop16-ink">popover-polyfill</span> from Open UI. No equivalent exists for anchoring.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpop16-bg: #eef0f3;
  --color-tpop16-bg: oklch(0.955 0.005 255);
  --color-tpop16-s1: #ffffff;
  --color-tpop16-s1: oklch(1 0 0);
  --color-tpop16-s2: #f7f8fa;
  --color-tpop16-s2: oklch(0.98 0.003 255);
  --color-tpop16-ink: #171b22;
  --color-tpop16-ink: oklch(0.22 0.015 260);
  --color-tpop16-mut: #575e69;
  --color-tpop16-mut: oklch(0.48 0.02 258);
  --color-tpop16-rule: #d7dbe1;
  --color-tpop16-rule: oklch(0.89 0.01 258);
  --color-tpop16-ok: #006647;
  --color-tpop16-ok: oklch(0.45 0.1 165);
  --color-tpop16-no: #99351b;
  --color-tpop16-no: oklch(0.47 0.14 35);
  --font-tpop16-sans: 'Geist', system-ui, sans-serif;
  --font-tpop16-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Theme dial: 0 = light, 1 = dark. Registered so the root can transition it. */

@property --tpop16-d {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles — plus the dark palette. Each @theme colour is
   re-declared on the root as a light/dark mix of the dial, so every utility (and every open
   popover, which inherits from the root) follows it. Light value last, dark value first. */

.tpop-16 {
  width: 100%;
  min-height: 100svh;
  --color-tpop16-bg: color-mix(in oklch, oklch(0.16 0.01 258) calc(var(--tpop16-d) * 100%), oklch(0.955 0.005 255));
  --color-tpop16-s1: color-mix(in oklch, oklch(0.21 0.012 258) calc(var(--tpop16-d) * 100%), oklch(1 0 0));
  --color-tpop16-s2: color-mix(in oklch, oklch(0.185 0.011 258) calc(var(--tpop16-d) * 100%), oklch(0.98 0.003 255));
  --color-tpop16-ink: color-mix(in oklch, oklch(0.94 0.008 258) calc(var(--tpop16-d) * 100%), oklch(0.22 0.015 260));
  --color-tpop16-mut: color-mix(in oklch, oklch(0.73 0.02 258) calc(var(--tpop16-d) * 100%), oklch(0.48 0.02 258));
  --color-tpop16-rule: color-mix(in oklch, oklch(0.3 0.014 258) calc(var(--tpop16-d) * 100%), oklch(0.89 0.01 258));
  --color-tpop16-ok: color-mix(in oklch, oklch(0.78 0.11 165) calc(var(--tpop16-d) * 100%), oklch(0.45 0.1 165));
  --color-tpop16-no: color-mix(in oklch, oklch(0.76 0.13 35) calc(var(--tpop16-d) * 100%), oklch(0.47 0.14 35));
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('[data-tpop16-root]');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const hasPopover = HTMLElement.prototype.hasOwnProperty('popover');
  const hasAnchor = !!(window.CSS && CSS.supports('anchor-name: --a'));
  const hasDiscrete = !!(window.CSS && CSS.supports('transition-behavior: allow-discrete'));
  root.dataset.popover = hasPopover ? 'yes' : 'no';
  root.dataset.anchor = hasAnchor ? 'yes' : 'no';
  root.dataset.discrete = hasDiscrete ? 'yes' : 'no';
  document.getElementById('tpop-16-r1').textContent = hasPopover ? 'supported' : 'missing · polyfill';
  document.getElementById('tpop-16-r2').textContent = hasAnchor ? 'supported' : 'missing · fallback';
  document.getElementById('tpop-16-r3').textContent = hasDiscrete ? 'supported' : 'missing · no fade';
  const panel = document.getElementById('tpop-16-panel');
  const trigger = document.getElementById('tpop-16-trigger');
  if (hasPopover) {
    panel.addEventListener('toggle', (e) => trigger.setAttribute('aria-expanded', String(e.newState === 'open')));
  } else {
    panel.hidden = true;
    trigger.addEventListener('click', () => {
      panel.hidden = !panel.hidden;
      trigger.setAttribute('aria-expanded', String(!panel.hidden));
    });
  }
})();
```
