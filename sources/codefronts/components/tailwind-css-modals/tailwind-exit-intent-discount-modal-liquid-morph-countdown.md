---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-exit-intent-discount-modal-liquid-morph-countdown/"
title: "Tailwind Exit-Intent Discount Modal with Live Countdown and Coupon Copy"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A last-chance offer that morphs in at a tilt — goo filter, 0.4 scale, &minus;4&deg; rotate, settling on an overshoot curve. The port makes the two things the…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Exit-Intent Discount Modal with Live Countdown and Coupon Copy
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-exit-intent-discount-modal-liquid-morph-countdown/

A last-chance offer that morphs in at a tilt — goo filter, 0.4 scale, &minus;4&deg; rotate, settling on an overshoot curve. The port makes the two things the original only described real: the countdown actually counts down (persisted for the session, so it cannot be gamed by a reload) and the coupon copies to the clipboard.
## HTML
```html
<section class="tw-13 w-full min-h-svh grid place-items-center bg-tw13-bg font-tw13-sans px-6 py-10">
  <svg width="0" height="0" class="absolute" aria-hidden="true">
    <defs>
      <filter id="tw-13-goo">
        <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="blur"/>
        <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 20 -8" result="goo"/>
        <feComposite in="SourceGraphic" in2="goo" operator="atop"/>
      </filter>
    </defs>
  </svg>

  <button type="button" data-tw13-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-lg border border-dashed border-tw13-sub bg-transparent text-sm font-semibold text-tw13-sub cursor-pointer transition-colors duration-200 hover:border-tw13-ink hover:text-tw13-ink focus-visible:outline-2 focus-visible:outline-tw13-start focus-visible:outline-offset-2">Simulate exit intent</button>

  <dialog id="tw-13-dlg" aria-labelledby="tw-13-title" class="m-auto w-[min(440px,94vw)] p-0 border-0 rounded-[18px] text-center text-tw13-ink bg-tw13-card shadow-[0_40px_70px_-15px_var(--color-tw13-glow)] opacity-0 scale-[0.4] -rotate-4 [filter:url(#tw-13-goo)] transition-[opacity,scale,rotate,filter,overlay,display] duration-[550ms] ease-[cubic-bezier(.34,1.56,.64,1)] [transition-delay:0ms,0ms,0ms,550ms] transition-discrete open:opacity-100 open:scale-100 open:rotate-0 open:[filter:none] open:starting:opacity-0 open:starting:scale-[0.4] open:starting:-rotate-4 open:backdrop:bg-tw13-scrim open:backdrop:backdrop-blur-[8px] motion-reduce:transition-[opacity] motion-reduce:duration-200 motion-reduce:scale-100 motion-reduce:rotate-0 motion-reduce:[filter:none]">
    <div class="relative px-[30px] pt-[34px] pb-6">
      <button type="button" data-tw13-close aria-label="Close dialog" class="absolute top-3.5 right-3.5 grid place-items-center size-9 rounded-lg border-0 bg-transparent text-[15px] text-tw13-sub cursor-pointer transition-colors duration-200 hover:bg-tw13-tint hover:text-tw13-ink focus-visible:outline-2 focus-visible:outline-tw13-start focus-visible:outline-offset-2">&#10005;</button>

      <p class="inline-block mb-3.5 px-3 py-1.5 rounded-full bg-tw13-urgenttint text-xs font-extrabold uppercase tracking-[0.16em] text-tw13-urgent">Wait!</p>

      <h2 id="tw-13-title" class="flex flex-col gap-1.5 mb-5">
        <span class="font-tw13-display text-[2.6rem] font-black tracking-[-0.03em] leading-none bg-linear-to-br from-tw13-start to-tw13-end bg-clip-text text-transparent">15% OFF</span>
        <span class="text-base font-semibold text-tw13-ink">your first order — before you go.</span>
      </h2>

      <div class="flex flex-col gap-0.5 mb-4 px-4 py-2.5 rounded-[9px] bg-tw13-urgenttint text-tw13-urgent">
        <span class="text-[0.68rem] font-bold uppercase tracking-wide">Offer expires in</span>
        <span data-tw13-timer aria-live="off" class="font-tw13-mono text-[1.35rem] font-extrabold tabular-nums">10:00</span>
      </div>

      <div class="flex justify-between items-center gap-3.5 mb-4 py-3 pl-[18px] pr-3.5 rounded-[9px] border border-dashed border-tw13-start bg-tw13-tint text-left">
        <span class="flex flex-col gap-0.5">
          <span class="text-[0.66rem] font-bold uppercase tracking-wide text-tw13-sub">Your code</span>
          <span data-tw13-code class="font-tw13-mono text-[1.05rem] font-extrabold tracking-wide text-tw13-ink">SAVE15</span>
        </span>
        <button type="button" data-tw13-copy class="min-h-11 px-4 rounded-md border-0 bg-tw13-ink text-xs font-bold text-white cursor-pointer transition-colors duration-200 hover:bg-black focus-visible:outline-2 focus-visible:outline-tw13-start focus-visible:outline-offset-2">Copy</button>
      </div>
      <p data-tw13-copied aria-live="polite" class="sr-only"></p>

      <button type="button" autofocus data-tw13-close class="w-full min-h-11 mb-2.5 px-5 py-[15px] rounded-[9px] border-0 bg-linear-to-br from-tw13-start to-tw13-end text-base font-extrabold text-white shadow-[0_12px_24px_-8px_var(--color-tw13-glow)] cursor-pointer transition-[translate,box-shadow] duration-200 hover:-translate-y-px hover:shadow-[0_16px_30px_-8px_var(--color-tw13-glow)] focus-visible:outline-2 focus-visible:outline-tw13-start focus-visible:outline-offset-[3px] motion-reduce:hover:translate-y-0">Claim my discount &rarr;</button>
      <button type="button" data-tw13-close class="w-full min-h-11 px-4 rounded-md border-0 bg-transparent text-[13px] text-tw13-sub underline cursor-pointer transition-colors duration-200 hover:text-tw13-ink focus-visible:outline-2 focus-visible:outline-tw13-start focus-visible:outline-offset-2">Continue browsing</button>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tw13-bg: #faf5ff;
  --color-tw13-bg: oklch(0.97 0.02 310);
  --color-tw13-card: #ffffff;
  --color-tw13-card: oklch(1 0 0);
  --color-tw13-ink: #1e1b4b;
  --color-tw13-ink: oklch(0.26 0.09 285);
  --color-tw13-sub: #5c6270;
  --color-tw13-sub: oklch(0.51 0.02 268);
  --color-tw13-start: #9333ea;
  --color-tw13-start: oklch(0.55 0.25 303);
  --color-tw13-end: #db2777;
  --color-tw13-end: oklch(0.59 0.22 6);
  --color-tw13-urgent: #c81e1e;
  --color-tw13-urgent: oklch(0.53 0.2 27);
  --color-tw13-urgenttint: #dc26261f;
  --color-tw13-urgenttint: oklch(0.58 0.21 27 / 0.1);
  --color-tw13-tint: #a855f714;
  --color-tw13-tint: oklch(0.63 0.23 303 / 0.08);
  --color-tw13-glow: #a855f773;
  --color-tw13-glow: oklch(0.63 0.23 303 / 0.45);
  --color-tw13-scrim: #1e1b4bb3;
  --color-tw13-scrim: oklch(0.26 0.09 285 / 0.7);
  --font-tw13-sans: 'Outfit', system-ui, sans-serif;
  --font-tw13-display: 'Playfair Display', Georgia, serif;
  --font-tw13-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tw-13 {
  width: 100%;
}

#tw-13-dlg::backdrop {
  background: oklch(0.26 0.09 285 / 0);
  backdrop-filter: blur(0px);
  transition: background .3s ease, backdrop-filter .3s ease, overlay .3s allow-discrete, display .3s allow-discrete;
}

@starting-style {
  #tw-13-dlg[open]::backdrop {
    background: oklch(0.26 0.09 285 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tw-13-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tw-13');
  var dlg = root.querySelector('#tw-13-dlg');
  var card = dlg.firstElementChild;
  var out = root.querySelector('[data-tw13-timer]');
  var said = root.querySelector('[data-tw13-copied]');
  var KEY = 'tw13-offer-deadline';
  var WINDOW_MS = 10 * 60 * 1000;
  var tick;

  // Honest urgency: the deadline persists for the session, so a reload does not reset it.
  function deadline() {
    var stored = +sessionStorage.getItem(KEY);
    if (!stored || stored < Date.now()) { stored = Date.now() + WINDOW_MS; sessionStorage.setItem(KEY, stored); }
    return stored;
  }
  function paint() {
    var left = Math.max(0, deadline() - Date.now());
    var m = Math.floor(left / 60000), s = Math.floor(left / 1000) % 60;
    out.textContent = (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
    if (left === 0) clearInterval(tick);
  }

  root.querySelector('[data-tw13-open]').addEventListener('click', function () {
    dlg.showModal(); paint(); tick = setInterval(paint, 1000);
  });
  dlg.addEventListener('close', function () { clearInterval(tick); });
  root.querySelectorAll('[data-tw13-close]').forEach(function (b) {
    b.addEventListener('click', function () { dlg.close(); });
  });
  root.querySelector('[data-tw13-copy]').addEventListener('click', function (e) {
    var code = root.querySelector('[data-tw13-code]').textContent;
    if (navigator.clipboard) navigator.clipboard.writeText(code);
    e.currentTarget.textContent = 'Copied';
    said.textContent = 'Discount code ' + code + ' copied to clipboard.';
  });
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
