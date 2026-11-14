---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-restaurant-reservation-modal-origami-fan-panels/"
title: "Tailwind Restaurant Reservation Modal with Cascading Fan Panels"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "An OpenTable-style booking sheet whose three panels — date, time, party — fan down in sequence."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Restaurant Reservation Modal with Cascading Fan Panels
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-restaurant-reservation-modal-origami-fan-panels/

An OpenTable-style booking sheet whose three panels — date, time, party — fan down in sequence. The port keeps the cascade as one animate-tw14-fan theme animation with three delays, and drives every selection from aria-[checked=true]: so the chips' look and their announced state are the same fact.
## HTML
```html
<section class="tw-14 w-full min-h-svh grid place-items-center bg-tw14-bg font-tw14-sans px-6 py-10">
  <button type="button" data-tw14-open class="inline-flex items-center justify-center min-h-11 px-7 rounded-md border border-tw14-brand bg-transparent font-tw14-display text-[15px] font-bold tracking-wide text-tw14-brand cursor-pointer transition-colors duration-200 hover:bg-tw14-brand hover:text-tw14-card focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2">Reserve a table</button>

  <dialog id="tw-14-dlg" aria-labelledby="tw-14-title" class="group m-auto w-[min(480px,94vw)] p-0 border-0 bg-transparent perspective-[1400px] opacity-0 transition-[opacity,overlay,display] duration-300 transition-discrete open:opacity-100 open:starting:opacity-0 open:backdrop:bg-tw14-scrim open:backdrop:backdrop-blur-[6px]">
    <div class="relative rounded-[14px] overflow-hidden bg-tw14-card text-left text-tw14-ink shadow-[0_40px_60px_-20px_#2a1a1066]">
      <button type="button" data-tw14-close aria-label="Close dialog" class="absolute top-3.5 right-3.5 z-10 grid place-items-center size-11 rounded-lg border-0 bg-tw14-glass text-[15px] text-tw14-sub cursor-pointer transition-colors duration-200 hover:bg-white hover:text-tw14-ink focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2">&#10005;</button>

      <div class="px-7 pt-[26px] pb-5 text-center border-b border-tw14-line">
        <p class="mb-1.5 text-xs font-bold uppercase tracking-[0.16em] text-tw14-gold">Osteria Bellini</p>
        <h2 id="tw-14-title" class="font-tw14-display text-2xl font-extrabold tracking-[-0.015em] leading-tight">Reserve your table</h2>
      </div>

      <div class="px-7 py-5 border-b border-tw14-line opacity-0 [transform:rotateX(-90deg)] origin-top backface-hidden group-open:animate-tw14-fan [animation-delay:150ms]! max-sm:[animation-delay:100ms]! motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:[transform:none]">
        <h3 class="mb-3 text-xs font-bold uppercase tracking-[0.1em] text-tw14-sub">Choose a date</h3>
        <div role="radiogroup" aria-label="Date" class="flex gap-1.5 overflow-x-auto pb-0.5">
          <button type="button" role="radio" aria-checked="false" class="shrink-0 flex flex-col items-center min-w-[52px] min-h-11 px-2.5 py-2 rounded-lg border border-tw14-line bg-white cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2"><span class="mb-0.5 text-[0.66rem] font-semibold uppercase tracking-wide opacity-80">Thu</span><strong class="text-base font-extrabold tabular-nums">28</strong></button>
          <button type="button" role="radio" aria-checked="true" class="shrink-0 flex flex-col items-center min-w-[52px] min-h-11 px-2.5 py-2 rounded-lg border border-tw14-line bg-white cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2"><span class="mb-0.5 text-[0.66rem] font-semibold uppercase tracking-wide opacity-80">Fri</span><strong class="text-base font-extrabold tabular-nums">29</strong></button>
          <button type="button" role="radio" aria-checked="false" class="shrink-0 flex flex-col items-center min-w-[52px] min-h-11 px-2.5 py-2 rounded-lg border border-tw14-line bg-white cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2"><span class="mb-0.5 text-[0.66rem] font-semibold uppercase tracking-wide opacity-80">Sat</span><strong class="text-base font-extrabold tabular-nums">30</strong></button>
          <button type="button" role="radio" aria-checked="false" class="shrink-0 flex flex-col items-center min-w-[52px] min-h-11 px-2.5 py-2 rounded-lg border border-tw14-line bg-white cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2"><span class="mb-0.5 text-[0.66rem] font-semibold uppercase tracking-wide opacity-80">Sun</span><strong class="text-base font-extrabold tabular-nums">31</strong></button>
          <button type="button" role="radio" aria-checked="false" class="shrink-0 flex flex-col items-center min-w-[52px] min-h-11 px-2.5 py-2 rounded-lg border border-tw14-line bg-white cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2"><span class="mb-0.5 text-[0.66rem] font-semibold uppercase tracking-wide opacity-80">Mon</span><strong class="text-base font-extrabold tabular-nums">1</strong></button>
          <button type="button" role="radio" aria-checked="false" class="shrink-0 flex flex-col items-center min-w-[52px] min-h-11 px-2.5 py-2 rounded-lg border border-tw14-line bg-white cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2"><span class="mb-0.5 text-[0.66rem] font-semibold uppercase tracking-wide opacity-80">Tue</span><strong class="text-base font-extrabold tabular-nums">2</strong></button>
          <button type="button" role="radio" aria-checked="false" class="shrink-0 flex flex-col items-center min-w-[52px] min-h-11 px-2.5 py-2 rounded-lg border border-tw14-line bg-white cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2"><span class="mb-0.5 text-[0.66rem] font-semibold uppercase tracking-wide opacity-80">Wed</span><strong class="text-base font-extrabold tabular-nums">3</strong></button>
        </div>
      </div>

      <div class="px-7 py-5 border-b border-tw14-line opacity-0 [transform:rotateX(-90deg)] origin-top backface-hidden group-open:animate-tw14-fan [animation-delay:320ms]! max-sm:[animation-delay:200ms]! motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:[transform:none]">
        <h3 class="mb-3 text-xs font-bold uppercase tracking-[0.1em] text-tw14-sub">Choose a time</h3>
        <div role="radiogroup" aria-label="Time" class="grid grid-cols-4 gap-1.5 max-[400px]:grid-cols-3">
          <button type="button" role="radio" aria-checked="false" class="min-h-11 px-1.5 rounded-md border border-tw14-line bg-white text-[13px] font-semibold text-tw14-ink cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2">6:00 PM</button>
          <button type="button" role="radio" aria-checked="false" class="min-h-11 px-1.5 rounded-md border border-tw14-line bg-white text-[13px] font-semibold text-tw14-ink cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2">6:30 PM</button>
          <button type="button" role="radio" aria-checked="true" class="min-h-11 px-1.5 rounded-md border border-tw14-line bg-white text-[13px] font-semibold text-tw14-ink cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2">7:00 PM</button>
          <button type="button" role="radio" aria-checked="false" class="min-h-11 px-1.5 rounded-md border border-tw14-line bg-white text-[13px] font-semibold text-tw14-ink cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2">7:30 PM</button>
          <button type="button" role="radio" aria-checked="false" class="min-h-11 px-1.5 rounded-md border border-tw14-line bg-white text-[13px] font-semibold text-tw14-ink cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2">8:00 PM</button>
          <button type="button" role="radio" aria-checked="false" class="min-h-11 px-1.5 rounded-md border border-tw14-line bg-white text-[13px] font-semibold text-tw14-ink cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2">8:30 PM</button>
          <button type="button" role="radio" aria-checked="false" disabled class="min-h-11 px-1.5 rounded-md border border-tw14-line bg-white text-[13px] font-semibold text-tw14-ink disabled:opacity-40 disabled:line-through disabled:cursor-not-allowed">9:00 PM</button>
          <button type="button" role="radio" aria-checked="false" class="min-h-11 px-1.5 rounded-md border border-tw14-line bg-white text-[13px] font-semibold text-tw14-ink cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2">9:30 PM</button>
        </div>
      </div>

      <div class="px-7 py-5 opacity-0 [transform:rotateX(-90deg)] origin-top backface-hidden group-open:animate-tw14-fan [animation-delay:490ms]! max-sm:[animation-delay:300ms]! motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:[transform:none]">
        <div class="flex flex-wrap justify-between items-center gap-3.5 mb-4">
          <div>
            <h3 class="text-xs font-bold uppercase tracking-[0.1em] text-tw14-sub">Party size</h3>
            <p class="mt-1 text-xs text-tw14-sub">Larger parties call the maître d'</p>
          </div>
          <div role="radiogroup" aria-label="Party size" class="flex gap-1.5">
            <button type="button" role="radio" aria-checked="false" class="size-11 rounded-md border border-tw14-line bg-white text-sm font-bold text-tw14-ink cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2">2</button>
            <button type="button" role="radio" aria-checked="false" class="size-11 rounded-md border border-tw14-line bg-white text-sm font-bold text-tw14-ink cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2">3</button>
            <button type="button" role="radio" aria-checked="true" class="size-11 rounded-md border border-tw14-line bg-white text-sm font-bold text-tw14-ink cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2">4</button>
            <button type="button" role="radio" aria-checked="false" class="size-11 rounded-md border border-tw14-line bg-white text-sm font-bold text-tw14-ink cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2">5</button>
            <button type="button" role="radio" aria-checked="false" class="size-11 rounded-md border border-tw14-line bg-white text-sm font-bold text-tw14-ink cursor-pointer transition-colors duration-200 hover:border-tw14-brand aria-[checked=true]:bg-tw14-brand aria-[checked=true]:border-tw14-brand aria-[checked=true]:text-white focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-2">6</button>
          </div>
        </div>
        <button type="button" data-tw14-close class="w-full min-h-11 px-5 py-3.5 rounded-lg border-0 bg-tw14-ink text-sm font-bold text-tw14-card cursor-pointer transition-[background-color,translate] duration-200 hover:bg-black hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tw14-brand focus-visible:outline-offset-[3px] motion-reduce:hover:translate-y-0">Reserve · Fri Jul 29, 7:00 PM · Party of 4</button>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tw14-bg: #f5efe0;
  --color-tw14-bg: oklch(0.95 0.025 85);
  --color-tw14-card: #faf6ec;
  --color-tw14-card: oklch(0.97 0.018 90);
  --color-tw14-ink: #2a1a10;
  --color-tw14-ink: oklch(0.26 0.04 50);
  --color-tw14-sub: #5f4c38;
  --color-tw14-sub: oklch(0.43 0.04 65);
  --color-tw14-line: #e8dcc4;
  --color-tw14-line: oklch(0.9 0.03 85);
  --color-tw14-brand: #8b1a1a;
  --color-tw14-brand: oklch(0.42 0.16 27);
  --color-tw14-gold: #8a6f2a;
  --color-tw14-gold: oklch(0.55 0.1 85);
  --color-tw14-glass: #ffffff99;
  --color-tw14-glass: oklch(1 0 0 / 0.6);
  --color-tw14-scrim: #2a1a108c;
  --color-tw14-scrim: oklch(0.26 0.04 50 / 0.55);
  --font-tw14-sans: 'Outfit', system-ui, sans-serif;
  --font-tw14-display: 'Playfair Display', Georgia, serif;
  --animate-tw14-fan: tw14-fan .5s cubic-bezier(.22, 1, .36, 1) forwards;
}

.tw-14 {
  width: 100%;
}

@keyframes tw14-fan {
  from {
    opacity: 0;
    transform: rotateX(-90deg);
  }

  to {
    opacity: 1;
    transform: rotateX(0deg);
  }
}

#tw-14-dlg::backdrop {
  background: oklch(0.26 0.04 50 / 0);
  backdrop-filter: blur(0px);
  transition: background .3s ease, backdrop-filter .3s ease, overlay .3s allow-discrete, display .3s allow-discrete;
}

@starting-style {
  #tw-14-dlg[open]::backdrop {
    background: oklch(0.26 0.04 50 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tw-14-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tw-14');
  var dlg = root.querySelector('#tw-14-dlg');
  var card = dlg.firstElementChild;
  root.querySelector('[data-tw14-open]').addEventListener('click', function () {
    dlg.showModal();
    var sel = dlg.querySelector('[role=radio][aria-checked=true]');
    if (sel) sel.focus();
  });
  root.querySelectorAll('[data-tw14-close]').forEach(function (b) {
    b.addEventListener('click', function () { dlg.close(); });
  });
  root.querySelectorAll('[role=radiogroup]').forEach(function (group) {
    group.addEventListener('click', function (e) {
      var btn = e.target.closest('[role=radio]:not([disabled])');
      if (!btn) return;
      group.querySelectorAll('[role=radio]').forEach(function (r) { r.setAttribute('aria-checked', String(r === btn)); });
    });
  });
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
