---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-stroke-draw-submit-button-loading-state/"
title: "Tailwind Stroke Draw Submit Button Loading State"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "Three real states carried by one outline, with the script setting a single attribute and every visual consequence following from data-* variants:…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stroke Draw Submit Button Loading State
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-stroke-draw-submit-button-loading-state/

Three real states carried by one outline, with the script setting a single attribute and every visual consequence following from data-* variants: data-[state=busy]:bg-svgb15-stroke/7 on the button, group-data-[state=done]:opacity-100 on its children. No class juggling in JavaScript &mdash; and group-data-[state=idle]:group-hover:[stroke-dashoffset:0] stacks two variants to say draw on hover, but only while idle.
## HTML
```html
<section class="svgb-15 relative block w-full min-h-svh bg-svgb15-bg text-svgb15-fg font-svgb15-sans">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-15-theme">
  <label class="absolute z-[5] top-4 right-4 grid place-items-center size-11 rounded-full border border-current/20 bg-current/7 cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/14 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-15-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="min-h-svh grid place-items-center p-[clamp(20px,5vw,68px)]">
    <div class="w-full max-w-115 flex flex-col gap-[18px] p-[clamp(22px,4vw,34px)] rounded-[26px] bg-svgb15-card [box-shadow:var(--svgb-15-card-sh)]">
      <p class="m-0 font-svgb15-mono text-[11px] tracking-[0.22em] uppercase text-svgb15-muted">Northlight Supply</p>
      <ul class="list-none m-0 p-0 flex flex-col gap-3">
        <li class="grid grid-cols-[44px_1fr_auto] gap-3.5 items-center">
          <img class="size-11 rounded-xl object-cover" src="https://picsum.photos/seed/svgb15lamp/200/200" alt="" width="200" height="200" loading="lazy" decoding="async">
          <span class="text-[14.5px] [&_em]:not-italic [&_em]:text-svgb15-muted">Arc desk lamp <em>&times;1</em></span>
          <span class="text-sm tabular-nums text-svgb15-muted">&euro;148.00</span>
        </li>
        <li class="grid grid-cols-[44px_1fr_auto] gap-3.5 items-center">
          <img class="size-11 rounded-xl object-cover" src="https://picsum.photos/seed/svgb15shade/200/200" alt="" width="200" height="200" loading="lazy" decoding="async">
          <span class="text-[14.5px] [&_em]:not-italic [&_em]:text-svgb15-muted">Linen shade <em>&times;2</em></span>
          <span class="text-sm tabular-nums text-svgb15-muted">&euro;62.00</span>
        </li>
      </ul>
      <div class="grid grid-cols-[1fr_auto] gap-x-4 gap-y-[7px] py-4 border-y border-svgb15-rest text-[13.5px] tabular-nums text-svgb15-muted">
        <span>Subtotal</span><span>&euro;210.00</span>
        <span>Shipping</span><span>&euro;9.50</span>
        <span class="text-[17px] font-bold text-svgb15-fg">Total</span><span class="text-[17px] font-bold text-svgb15-fg">&euro;219.50</span>
      </div>

      <div class="flex flex-col items-start gap-3">
        <button class="svgb-15__btn group relative w-[min(300px,100%)] h-17 grid place-items-center border-0 p-0 rounded-full bg-svgb15-stroke/14 text-base font-bold tracking-[-0.01em] cursor-pointer transition-[background-color] duration-[260ms] motion-reduce:transition-none disabled:cursor-default data-[state=busy]:bg-svgb15-stroke/7 data-[state=done]:bg-svgb15-ok/14 focus-visible:outline-2 focus-visible:outline-svgb15-stroke focus-visible:outline-offset-4" type="button" data-state="idle">
          <svg class="absolute inset-0 w-full h-full overflow-visible [&_rect]:fill-none [&_rect]:[stroke-linecap:round]" viewBox="0 0 300 68" aria-hidden="true">
            <rect class="stroke-svgb15-rest [stroke-width:1.5]" x="2" y="2" width="296" height="64" rx="32" pathLength="1"/>
            <rect class="stroke-svgb15-stroke [stroke-width:2.2] [stroke-dasharray:1] [stroke-dashoffset:1] [transition:stroke-dashoffset_620ms_cubic-bezier(0.22,1,0.36,1),stroke_300ms_ease] motion-reduce:transition-none group-data-[state=idle]:group-hover:[stroke-dashoffset:0] group-data-[state=idle]:group-focus-visible:[stroke-dashoffset:0] group-data-[state=done]:stroke-svgb15-ok group-data-[state=done]:[stroke-dashoffset:0] group-data-[state=done]:[transition-duration:300ms]" x="2" y="2" width="296" height="64" rx="32" pathLength="1"/>
            <rect class="stroke-svgb15-stroke [stroke-width:2.6] [stroke-dasharray:0.25_0.75] [stroke-dashoffset:0] opacity-0 group-data-[state=busy]:opacity-100 group-data-[state=busy]:animate-svgb15-orbit motion-reduce:!animate-none motion-reduce:[stroke-dasharray:0.5_0.5] motion-reduce:group-data-[state=busy]:opacity-70" x="2" y="2" width="296" height="64" rx="32" pathLength="1"/>
          </svg>
          <span class="relative z-[1] grid transition-[translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] motion-reduce:transition-none group-data-[state=done]:-translate-x-3.5">
            <span class="[grid-area:1/1] opacity-100 transition-opacity duration-200 motion-reduce:transition-none group-data-[state=busy]:opacity-0 group-data-[state=done]:opacity-0">Pay &euro;219.50</span>
            <span class="[grid-area:1/1] opacity-0 transition-opacity duration-200 motion-reduce:transition-none group-data-[state=busy]:opacity-100">Authorising</span>
            <span class="[grid-area:1/1] opacity-0 transition-opacity duration-200 motion-reduce:transition-none group-data-[state=done]:opacity-100">Paid</span>
          </span>
          <svg class="absolute z-[1] right-[22px] top-1/2 -translate-y-1/2 size-[22px] opacity-0 transition-opacity duration-200 motion-reduce:transition-none group-data-[state=done]:opacity-100" viewBox="0 0 24 24" aria-hidden="true">
            <path class="fill-none stroke-svgb15-ok [stroke-width:2.6] [stroke-linecap:round] [stroke-linejoin:round] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[420ms] delay-[120ms] ease-[cubic-bezier(0.22,1,0.36,1)] motion-reduce:transition-none group-data-[state=done]:[stroke-dashoffset:0]" d="M5 12.5 10 17.5 19 7.5" pathLength="1"/>
          </svg>
        </button>
        <p class="svgb-15__status m-0 font-svgb15-mono text-[11px] text-svgb15-muted" role="status" aria-live="polite">Card &bull;&bull;&bull;&bull; 4242 &middot; ready</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb15-bg: #07100d;
  --color-svgb15-bg: oklch(0.16 0.02 165);
  --color-svgb15-fg: #eaf2ee;
  --color-svgb15-fg: oklch(0.95 0.012 165);
  --color-svgb15-muted: #85978f;
  --color-svgb15-muted: oklch(0.655 0.018 165);
  --color-svgb15-card: #0e1815;
  --color-svgb15-card: oklch(0.215 0.022 165);
  --color-svgb15-rest: rgba(234, 242, 238, 0.14);
  --color-svgb15-rest: oklch(0.95 0.012 165 / 0.14);
  --color-svgb15-stroke: #57e3a8;
  --color-svgb15-stroke: oklch(0.85 0.15 160);
  --color-svgb15-ok: #9dff6f;
  --color-svgb15-ok: oklch(0.91 0.19 132);
  --font-svgb15-sans: 'Manrope', system-ui, sans-serif;
  --font-svgb15-mono: 'JetBrains Mono', ui-monospace, monospace;
  /* a quarter-length segment travelling one whole normalised path */
  --animate-svgb15-orbit: svgb15-orbit 1.1s linear infinite;
}

@keyframes svgb15-orbit {
  to {
    stroke-dashoffset: -1;
  }
}

.svgb-15 {
  --svgb-15-card-sh: inset 0 1px 0 oklch(1 0 0 / 0.05), 0 34px 80px -50px #000;
}

.svgb-15:has(#svgb-15-theme:checked) {
  --color-svgb15-bg: #eef3f0;
  --color-svgb15-bg: oklch(0.95 0.008 165);
  --color-svgb15-fg: #0f1714;
  --color-svgb15-fg: oklch(0.19 0.018 165);
  --color-svgb15-muted: #566159;
  --color-svgb15-muted: oklch(0.49 0.016 160);
  --color-svgb15-card: #ffffff;
  --color-svgb15-card: oklch(1 0 0);
  --color-svgb15-rest: rgba(15, 23, 20, 0.14);
  --color-svgb15-rest: oklch(0.19 0.018 165 / 0.14);
  --color-svgb15-stroke: #0a6b4b;
  --color-svgb15-stroke: oklch(0.46 0.12 162);
  --color-svgb15-ok: #2f6b12;
  --color-svgb15-ok: oklch(0.48 0.15 132);
  --svgb-15-card-sh: 0 1px 2px oklch(0 0 0 / 0.05), 0 30px 70px -50px oklch(0 0 0 / 0.4);
}
```

## JavaScript
```js
/* State machine only: the script never animates, it just sets data-state and ARIA. */
(function () {
  var root = document.querySelector('.svgb-15');
  if (!root) return;
  var btn = root.querySelector('.svgb-15__btn');
  var status = root.querySelector('.svgb-15__status');
  var timers = new Set();

  function later(fn, ms) {
    var id = setTimeout(function () { timers.delete(id); fn(); }, ms);
    timers.add(id);
  }

  function setState(state, message) {
    btn.dataset.state = state;
    btn.setAttribute('aria-busy', state === 'busy' ? 'true' : 'false');
    btn.disabled = state === 'busy';
    status.textContent = message;
  }

  btn.addEventListener('click', function () {
    if (btn.dataset.state !== 'idle') return;
    setState('busy', 'Authorising with your bank');
    later(function () {
      setState('done', 'Paid EUR 219.50 - receipt sent');
      later(function () { setState('idle', 'Card 4242 - ready'); }, 2600);
    }, 1800);
  });

  root.__svgb15Cleanup = function () {
    timers.forEach(clearTimeout);
    timers.clear();
  };
})();
```
