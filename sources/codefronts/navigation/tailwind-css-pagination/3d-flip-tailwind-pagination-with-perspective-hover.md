---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/3d-flip-tailwind-pagination-with-perspective-hover/"
title: "3D Flip Tailwind Pagination with Perspective Hover"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "Every page key is a two-faced keycap: the number on the front, the same number on a coral face behind it."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Flip Tailwind Pagination with Perspective Hover
Source: https://codefronts.com/navigation/tailwind-css-pagination/3d-flip-tailwind-pagination-with-perspective-hover/

Every page key is a two-faced keycap: the number on the front, the same number on a coral face behind it. Hover or keyboard focus turns the cap half a revolution on X with -rotate-x-180 inside transform-3d, and backface-hidden lets the browser decide which face is lit. The port gives each key its own perspective-normal, keeps the current page still, and wires real page state with a ten-line script that only sets attributes.
## HTML
```html
<section class="tpg-16 w-full min-h-svh grid place-items-center bg-tpg16-bg bg-[radial-gradient(70%_55%_at_50%_0%,var(--color-tpg16-glow),transparent_70%)] px-4 py-14 font-tpg16-sans text-tpg16-ink antialiased sm:px-5" aria-label="3D flip pagination demo">
  <div class="grid w-full justify-items-center gap-7">
    <article id="tpg-16-archive" class="w-full max-w-[40rem] rounded-[1.375rem] bg-tpg16-card shadow-tpg16-card ring-1 ring-tpg16-line transition duration-700 ease-[cubic-bezier(.16,1,.3,1)] starting:translate-y-2 starting:opacity-0">
      <header class="flex flex-wrap items-end justify-between gap-x-6 gap-y-2 border-b border-tpg16-line px-4 pt-6 pb-5 sm:px-7">
        <div>
          <p class="font-tpg16-mono text-[11px] font-medium tracking-[0.14em] text-tpg16-hl uppercase">Field Notes &middot; Archive</p>
          <h2 class="mt-1.5 text-[1.625rem] leading-tight font-bold tracking-[-0.03em]">Essays on making things</h2>
        </div>
        <p class="font-tpg16-mono text-xs text-tpg16-mut tabular-nums">20 essays &middot; 2024&ndash;2026</p>
      </header>
      <ol class="divide-y divide-tpg16-line px-4 sm:px-7" start="9">
        <li class="flex items-baseline gap-4 py-4"><span class="w-6 flex-none font-tpg16-mono text-xs text-tpg16-mut tabular-nums">09</span><span class="min-w-0 flex-1"><span class="block text-[15px] font-semibold tracking-[-0.01em]">The quiet power of default settings</span><span class="mt-0.5 block text-[13px] text-tpg16-mut">On the decisions nobody notices making</span></span><span class="flex-none font-tpg16-mono text-xs text-tpg16-mut tabular-nums">7 min</span></li>
        <li class="flex items-baseline gap-4 py-4"><span class="w-6 flex-none font-tpg16-mono text-xs text-tpg16-mut tabular-nums">10</span><span class="min-w-0 flex-1"><span class="block text-[15px] font-semibold tracking-[-0.01em]">Drawing with constraints</span><span class="mt-0.5 block text-[13px] text-tpg16-mut">Why a grid is a promise, not a cage</span></span><span class="flex-none font-tpg16-mono text-xs text-tpg16-mut tabular-nums">11 min</span></li>
        <li class="flex items-baseline gap-4 py-4"><span class="w-6 flex-none font-tpg16-mono text-xs text-tpg16-mut tabular-nums">11</span><span class="min-w-0 flex-1"><span class="block text-[15px] font-semibold tracking-[-0.01em]">A field guide to friction</span><span class="mt-0.5 block text-[13px] text-tpg16-mut">Where slowing people down is the kind thing</span></span><span class="flex-none font-tpg16-mono text-xs text-tpg16-mut tabular-nums">9 min</span></li>
        <li class="flex items-baseline gap-4 py-4"><span class="w-6 flex-none font-tpg16-mono text-xs text-tpg16-mut tabular-nums">12</span><span class="min-w-0 flex-1"><span class="block text-[15px] font-semibold tracking-[-0.01em]">Notes from a type foundry</span><span class="mt-0.5 block text-[13px] text-tpg16-mut">Three weeks of kerning one lowercase g</span></span><span class="flex-none font-tpg16-mono text-xs text-tpg16-mut tabular-nums">14 min</span></li>
      </ol>
      <footer class="flex flex-col items-center gap-4 rounded-b-[1.375rem] border-t border-tpg16-line bg-tpg16-well px-3 py-5 sm:flex-row sm:justify-between sm:px-7">
        <p data-status="" role="status" aria-live="polite" class="order-last text-[13px] text-tpg16-mut tabular-nums sm:order-first">Showing <strong data-range="" class="font-semibold text-tpg16-hl">9–12</strong> of 20</p>
        <nav aria-label="Pagination">
          <ol class="flex items-center gap-0.5 sm:gap-1.5">
            <li><button type="button" data-step="-1" aria-label="Previous page" class="group size-11 cursor-pointer rounded-xl perspective-normal focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg16-ring disabled:cursor-not-allowed disabled:opacity-45 sm:size-12"><span class="relative block size-full transition-transform duration-500 ease-[cubic-bezier(.34,1.3,.5,1)] transform-3d motion-safe:group-[:not([aria-current=page]):not(:disabled):is(:hover,:focus-visible)]:-rotate-x-180 motion-reduce:transition-none"><span class="absolute inset-0 grid place-items-center rounded-xl bg-tpg16-card text-tpg16-ink shadow-tpg16-key ring-1 ring-tpg16-line backface-hidden motion-reduce:group-hover:bg-tpg16-raise"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="absolute inset-0 grid rotate-x-180 place-items-center rounded-xl bg-linear-to-br from-tpg16-acc to-tpg16-acc2 text-tpg16-onacc shadow-tpg16-on backface-hidden" aria-hidden="true"><svg viewBox="0 0 20 20" width="18" height="18"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span></span></button></li>
            <li><button type="button" data-page="1" aria-label="Page 1" class="group size-11 cursor-pointer rounded-xl perspective-normal focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg16-ring aria-[current=page]:cursor-default sm:size-12"><span class="relative block size-full transition-transform duration-500 ease-[cubic-bezier(.34,1.3,.5,1)] transform-3d motion-safe:group-[:not([aria-current=page]):not(:disabled):is(:hover,:focus-visible)]:-rotate-x-180 motion-reduce:transition-none"><span class="absolute inset-0 grid place-items-center rounded-xl bg-tpg16-card text-[15px] font-semibold text-tpg16-ink tabular-nums shadow-tpg16-key ring-1 ring-tpg16-line backface-hidden group-aria-[current=page]:bg-linear-to-br group-aria-[current=page]:from-tpg16-acc group-aria-[current=page]:to-tpg16-acc2 group-aria-[current=page]:font-bold group-aria-[current=page]:text-tpg16-onacc group-aria-[current=page]:shadow-tpg16-on group-aria-[current=page]:ring-tpg16-acc2/30 motion-reduce:group-hover:bg-tpg16-raise">1</span><span class="absolute inset-0 grid rotate-x-180 place-items-center rounded-xl bg-linear-to-br from-tpg16-coral to-tpg16-coral2 text-[15px] font-bold text-tpg16-oncoral tabular-nums shadow-tpg16-back backface-hidden" aria-hidden="true">1</span></span></button></li>
            <li><button type="button" data-page="2" aria-label="Page 2" class="group size-11 cursor-pointer rounded-xl perspective-normal focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg16-ring aria-[current=page]:cursor-default sm:size-12"><span class="relative block size-full transition-transform duration-500 ease-[cubic-bezier(.34,1.3,.5,1)] transform-3d motion-safe:group-[:not([aria-current=page]):not(:disabled):is(:hover,:focus-visible)]:-rotate-x-180 motion-reduce:transition-none"><span class="absolute inset-0 grid place-items-center rounded-xl bg-tpg16-card text-[15px] font-semibold text-tpg16-ink tabular-nums shadow-tpg16-key ring-1 ring-tpg16-line backface-hidden group-aria-[current=page]:bg-linear-to-br group-aria-[current=page]:from-tpg16-acc group-aria-[current=page]:to-tpg16-acc2 group-aria-[current=page]:font-bold group-aria-[current=page]:text-tpg16-onacc group-aria-[current=page]:shadow-tpg16-on group-aria-[current=page]:ring-tpg16-acc2/30 motion-reduce:group-hover:bg-tpg16-raise">2</span><span class="absolute inset-0 grid rotate-x-180 place-items-center rounded-xl bg-linear-to-br from-tpg16-coral to-tpg16-coral2 text-[15px] font-bold text-tpg16-oncoral tabular-nums shadow-tpg16-back backface-hidden" aria-hidden="true">2</span></span></button></li>
            <li><button type="button" data-page="3" aria-label="Page 3" aria-current="page" class="group size-11 cursor-pointer rounded-xl perspective-normal focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg16-ring aria-[current=page]:cursor-default sm:size-12"><span class="relative block size-full transition-transform duration-500 ease-[cubic-bezier(.34,1.3,.5,1)] transform-3d motion-safe:group-[:not([aria-current=page]):not(:disabled):is(:hover,:focus-visible)]:-rotate-x-180 motion-reduce:transition-none"><span class="absolute inset-0 grid place-items-center rounded-xl bg-tpg16-card text-[15px] font-semibold text-tpg16-ink tabular-nums shadow-tpg16-key ring-1 ring-tpg16-line backface-hidden group-aria-[current=page]:bg-linear-to-br group-aria-[current=page]:from-tpg16-acc group-aria-[current=page]:to-tpg16-acc2 group-aria-[current=page]:font-bold group-aria-[current=page]:text-tpg16-onacc group-aria-[current=page]:shadow-tpg16-on group-aria-[current=page]:ring-tpg16-acc2/30 motion-reduce:group-hover:bg-tpg16-raise">3</span><span class="absolute inset-0 grid rotate-x-180 place-items-center rounded-xl bg-linear-to-br from-tpg16-coral to-tpg16-coral2 text-[15px] font-bold text-tpg16-oncoral tabular-nums shadow-tpg16-back backface-hidden" aria-hidden="true">3</span></span></button></li>
            <li><button type="button" data-page="4" aria-label="Page 4" class="group size-11 cursor-pointer rounded-xl perspective-normal focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg16-ring aria-[current=page]:cursor-default sm:size-12"><span class="relative block size-full transition-transform duration-500 ease-[cubic-bezier(.34,1.3,.5,1)] transform-3d motion-safe:group-[:not([aria-current=page]):not(:disabled):is(:hover,:focus-visible)]:-rotate-x-180 motion-reduce:transition-none"><span class="absolute inset-0 grid place-items-center rounded-xl bg-tpg16-card text-[15px] font-semibold text-tpg16-ink tabular-nums shadow-tpg16-key ring-1 ring-tpg16-line backface-hidden group-aria-[current=page]:bg-linear-to-br group-aria-[current=page]:from-tpg16-acc group-aria-[current=page]:to-tpg16-acc2 group-aria-[current=page]:font-bold group-aria-[current=page]:text-tpg16-onacc group-aria-[current=page]:shadow-tpg16-on group-aria-[current=page]:ring-tpg16-acc2/30 motion-reduce:group-hover:bg-tpg16-raise">4</span><span class="absolute inset-0 grid rotate-x-180 place-items-center rounded-xl bg-linear-to-br from-tpg16-coral to-tpg16-coral2 text-[15px] font-bold text-tpg16-oncoral tabular-nums shadow-tpg16-back backface-hidden" aria-hidden="true">4</span></span></button></li>
            <li><button type="button" data-page="5" aria-label="Page 5" class="group size-11 cursor-pointer rounded-xl perspective-normal focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg16-ring aria-[current=page]:cursor-default sm:size-12"><span class="relative block size-full transition-transform duration-500 ease-[cubic-bezier(.34,1.3,.5,1)] transform-3d motion-safe:group-[:not([aria-current=page]):not(:disabled):is(:hover,:focus-visible)]:-rotate-x-180 motion-reduce:transition-none"><span class="absolute inset-0 grid place-items-center rounded-xl bg-tpg16-card text-[15px] font-semibold text-tpg16-ink tabular-nums shadow-tpg16-key ring-1 ring-tpg16-line backface-hidden group-aria-[current=page]:bg-linear-to-br group-aria-[current=page]:from-tpg16-acc group-aria-[current=page]:to-tpg16-acc2 group-aria-[current=page]:font-bold group-aria-[current=page]:text-tpg16-onacc group-aria-[current=page]:shadow-tpg16-on group-aria-[current=page]:ring-tpg16-acc2/30 motion-reduce:group-hover:bg-tpg16-raise">5</span><span class="absolute inset-0 grid rotate-x-180 place-items-center rounded-xl bg-linear-to-br from-tpg16-coral to-tpg16-coral2 text-[15px] font-bold text-tpg16-oncoral tabular-nums shadow-tpg16-back backface-hidden" aria-hidden="true">5</span></span></button></li>
            <li><button type="button" data-step="1" aria-label="Next page" class="group size-11 cursor-pointer rounded-xl perspective-normal focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg16-ring disabled:cursor-not-allowed disabled:opacity-45 sm:size-12"><span class="relative block size-full transition-transform duration-500 ease-[cubic-bezier(.34,1.3,.5,1)] transform-3d motion-safe:group-[:not([aria-current=page]):not(:disabled):is(:hover,:focus-visible)]:-rotate-x-180 motion-reduce:transition-none"><span class="absolute inset-0 grid place-items-center rounded-xl bg-tpg16-card text-tpg16-ink shadow-tpg16-key ring-1 ring-tpg16-line backface-hidden motion-reduce:group-hover:bg-tpg16-raise"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="absolute inset-0 grid rotate-x-180 place-items-center rounded-xl bg-linear-to-br from-tpg16-acc to-tpg16-acc2 text-tpg16-onacc shadow-tpg16-on backface-hidden" aria-hidden="true"><svg viewBox="0 0 20 20" width="18" height="18"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span></span></button></li>
          </ol>
        </nav>
      </footer>
    </article>
    <p aria-hidden="true" class="max-w-full rounded-2xl px-3.5 py-2 text-center font-tpg16-mono text-[11.5px] text-tpg16-mut ring-1 ring-tpg16-line">perspective-normal &middot; transform-3d &middot; backface-hidden &middot; -rotate-x-180</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg16-bg: #fbf0ee;
  --color-tpg16-bg: oklch(0.962 0.016 22);
  --color-tpg16-glow: #fecdd399;
  --color-tpg16-glow: oklch(0.9 0.07 12 / 0.6);
  --color-tpg16-card: #fffaf9;
  --color-tpg16-card: oklch(0.992 0.005 22);
  --color-tpg16-well: #fdf3f1;
  --color-tpg16-well: oklch(0.973 0.012 22);
  --color-tpg16-raise: #fbe1dd;
  --color-tpg16-raise: oklch(0.935 0.035 20);
  --color-tpg16-ink: #2b1216;
  --color-tpg16-ink: oklch(0.24 0.045 15);
  --color-tpg16-mut: #7c474c;
  --color-tpg16-mut: oklch(0.47 0.07 15);
  --color-tpg16-line: #f2d6d3;
  --color-tpg16-line: oklch(0.9 0.032 20);
  --color-tpg16-hl: #b91c1c;
  --color-tpg16-hl: oklch(0.505 0.19 25);
  --color-tpg16-acc: #dc2626;
  --color-tpg16-acc: oklch(0.577 0.215 27);
  --color-tpg16-acc2: #be123c;
  --color-tpg16-acc2: oklch(0.514 0.199 17);
  --color-tpg16-coral: #ff8f7e;
  --color-tpg16-coral: oklch(0.76 0.15 30);
  --color-tpg16-coral2: #fb7185;
  --color-tpg16-coral2: oklch(0.712 0.194 13);
  --color-tpg16-oncoral: #450a0a;
  --color-tpg16-oncoral: oklch(0.26 0.09 25);
  --color-tpg16-onacc: #ffffff;
  --color-tpg16-onacc: oklch(1 0 0);
  --color-tpg16-ring: #dc2626;
  --color-tpg16-ring: oklch(0.577 0.215 27);
  --color-tpg16-hi: #ffffffb3;
  --color-tpg16-hi: oklch(1 0 0 / 0.7);
  --font-tpg16-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tpg16-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tpg16-card: 0 1px 2px oklch(0.4 0.1 20 / 0.08), 0 22px 50px -18px oklch(0.5 0.18 20 / 0.3);
  --shadow-tpg16-key: 0 1px 0 var(--color-tpg16-hi) inset, 0 2px 0 oklch(0.5 0.12 20 / 0.12);
  --shadow-tpg16-on: 0 10px 24px -8px oklch(0.55 0.21 25 / 0.7), inset 0 1px 0 oklch(1 0 0 / 0.3);
  --shadow-tpg16-back: 0 10px 22px -10px oklch(0.6 0.19 18 / 0.7), inset 0 1px 0 oklch(1 0 0 / 0.35);
}

@media (prefers-color-scheme: dark) {
  .tpg-16:not([data-theme="light"]) {
    --color-tpg16-bg: #1a0a0d;
    --color-tpg16-bg: oklch(0.17 0.032 15);
    --color-tpg16-glow: #7f1d1d59;
    --color-tpg16-glow: oklch(0.36 0.12 22 / 0.35);
    --color-tpg16-card: #251215;
    --color-tpg16-card: oklch(0.215 0.036 15);
    --color-tpg16-well: #200f12;
    --color-tpg16-well: oklch(0.195 0.033 15);
    --color-tpg16-raise: #38191d;
    --color-tpg16-raise: oklch(0.285 0.05 15);
    --color-tpg16-ink: #fcefef;
    --color-tpg16-ink: oklch(0.96 0.013 15);
    --color-tpg16-mut: #d4a5a9;
    --color-tpg16-mut: oklch(0.77 0.05 15);
    --color-tpg16-line: #40222a;
    --color-tpg16-line: oklch(0.31 0.045 12);
    --color-tpg16-hl: #fda4af;
    --color-tpg16-hl: oklch(0.81 0.11 12);
    --color-tpg16-ring: #fb7185;
    --color-tpg16-ring: oklch(0.712 0.194 13);
    --color-tpg16-hi: #ffffff12;
    --color-tpg16-hi: oklch(1 0 0 / 0.07);
  }
}

.tpg-16[data-theme="dark"] {
  --color-tpg16-bg: #1a0a0d;
  --color-tpg16-bg: oklch(0.17 0.032 15);
  --color-tpg16-glow: #7f1d1d59;
  --color-tpg16-glow: oklch(0.36 0.12 22 / 0.35);
  --color-tpg16-card: #251215;
  --color-tpg16-card: oklch(0.215 0.036 15);
  --color-tpg16-well: #200f12;
  --color-tpg16-well: oklch(0.195 0.033 15);
  --color-tpg16-raise: #38191d;
  --color-tpg16-raise: oklch(0.285 0.05 15);
  --color-tpg16-ink: #fcefef;
  --color-tpg16-ink: oklch(0.96 0.013 15);
  --color-tpg16-mut: #d4a5a9;
  --color-tpg16-mut: oklch(0.77 0.05 15);
  --color-tpg16-line: #40222a;
  --color-tpg16-line: oklch(0.31 0.045 12);
  --color-tpg16-hl: #fda4af;
  --color-tpg16-hl: oklch(0.81 0.11 12);
  --color-tpg16-ring: #fb7185;
  --color-tpg16-ring: oklch(0.712 0.194 13);
  --color-tpg16-hi: #ffffff12;
  --color-tpg16-hi: oklch(1 0 0 / 0.07);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-16 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tpg-16-archive');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const pages = Array.from(root.querySelectorAll('[data-page]'));
  const prev = root.querySelector('[data-step="-1"]');
  const next = root.querySelector('[data-step="1"]');
  const range = root.querySelector('[data-range]');
  const per = 4, total = 20, last = pages.length;
  let cur = 3;
  const go = (n) => {
    cur = Math.min(last, Math.max(1, n));
    pages.forEach((b, i) => {
      if (i + 1 === cur) b.setAttribute('aria-current', 'page');
      else b.removeAttribute('aria-current');
    });
    prev.disabled = cur === 1;
    next.disabled = cur === last;
    if ([prev, next].indexOf(document.activeElement) > -1 && document.activeElement.disabled) pages[cur - 1].focus();
    const a = (cur - 1) * per + 1, z = Math.min(total, cur * per);
    range.textContent = a + '–' + z;
  };
  pages.forEach((b) => b.addEventListener('click', () => go(Number(b.dataset.page))));
  prev.addEventListener('click', () => go(cur - 1));
  next.addEventListener('click', () => go(cur + 1));
  go(cur);
})();
```
