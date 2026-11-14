---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-click-to-front-stacked-cards-cycle/"
title: "Tailwind Click to Front Stacked Cards Cycle"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "A queue you browse by clicking the front card: it flings sideways, drops to the bottom of the pile and glides back in at the rear."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Click to Front Stacked Cards Cycle
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-click-to-front-stacked-cards-cycle/

A queue you browse by clicking the front card: it flings sideways, drops to the bottom of the pile and glides back in at the rear. Depth is a number, not DOM order &mdash; every card reads its own --depth through [transform:translateY(calc(var(--depth)*16px))_scale(calc(1-var(--depth)*0.05))] and [z-index:calc(10-var(--depth))], so the script only ever repaints one integer per card.
## HTML
```html
<section class="stk-09 w-full min-h-svh flex flex-col items-center justify-center gap-7 px-5 py-12 font-stk09-sans bg-stk09-bg" aria-label="Click-to-front card deck">
  <div class="relative w-[min(320px,86vw)] h-55" id="stk-09-deck">
    <button class="absolute inset-0 flex flex-col gap-2 border-0 cursor-pointer rounded-[20px] bg-stk09-c1 p-6 text-left text-white shadow-[0_24px_46px_-26px_rgba(0,0,0,0.8)] [transform:translateY(calc(var(--depth,0)*16px))_scale(calc(1-var(--depth,0)*0.05))] [z-index:calc(10-var(--depth,0))] transition-[transform,opacity] duration-500 ease-stk09 data-[sending=true]:opacity-0 data-[sending=true]:duration-450 data-[sending=true]:ease-in data-[sending=true]:[transform:translateX(130%)_rotate(12deg)] focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-3 motion-reduce:duration-200" type="button">
      <span class="font-stk09-mono text-xs font-bold tracking-[0.08em] opacity-85">Ticket #4821</span>
      <b class="text-xl font-extrabold tracking-[-0.02em]">Payment retry loop</b>
      <i class="mt-auto font-stk09-mono text-xs not-italic opacity-85">High &middot; Billing</i>
    </button>
    <button class="absolute inset-0 flex flex-col gap-2 border-0 cursor-pointer rounded-[20px] bg-stk09-c2 p-6 text-left text-white shadow-[0_24px_46px_-26px_rgba(0,0,0,0.8)] [transform:translateY(calc(var(--depth,0)*16px))_scale(calc(1-var(--depth,0)*0.05))] [z-index:calc(10-var(--depth,0))] transition-[transform,opacity] duration-500 ease-stk09 data-[sending=true]:opacity-0 data-[sending=true]:duration-450 data-[sending=true]:ease-in data-[sending=true]:[transform:translateX(130%)_rotate(12deg)] focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-3 motion-reduce:duration-200" type="button">
      <span class="font-stk09-mono text-xs font-bold tracking-[0.08em] opacity-85">Ticket #4822</span>
      <b class="text-xl font-extrabold tracking-[-0.02em]">Slow search on mobile</b>
      <i class="mt-auto font-stk09-mono text-xs not-italic opacity-85">Medium &middot; Web</i>
    </button>
    <button class="absolute inset-0 flex flex-col gap-2 border-0 cursor-pointer rounded-[20px] bg-stk09-c3 p-6 text-left text-white shadow-[0_24px_46px_-26px_rgba(0,0,0,0.8)] [transform:translateY(calc(var(--depth,0)*16px))_scale(calc(1-var(--depth,0)*0.05))] [z-index:calc(10-var(--depth,0))] transition-[transform,opacity] duration-500 ease-stk09 data-[sending=true]:opacity-0 data-[sending=true]:duration-450 data-[sending=true]:ease-in data-[sending=true]:[transform:translateX(130%)_rotate(12deg)] focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-3 motion-reduce:duration-200" type="button">
      <span class="font-stk09-mono text-xs font-bold tracking-[0.08em] opacity-85">Ticket #4823</span>
      <b class="text-xl font-extrabold tracking-[-0.02em]">Export to CSV missing</b>
      <i class="mt-auto font-stk09-mono text-xs not-italic opacity-85">Low &middot; Reports</i>
    </button>
    <button class="absolute inset-0 flex flex-col gap-2 border-0 cursor-pointer rounded-[20px] bg-stk09-c4 p-6 text-left text-white shadow-[0_24px_46px_-26px_rgba(0,0,0,0.8)] [transform:translateY(calc(var(--depth,0)*16px))_scale(calc(1-var(--depth,0)*0.05))] [z-index:calc(10-var(--depth,0))] transition-[transform,opacity] duration-500 ease-stk09 data-[sending=true]:opacity-0 data-[sending=true]:duration-450 data-[sending=true]:ease-in data-[sending=true]:[transform:translateX(130%)_rotate(12deg)] focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-3 motion-reduce:duration-200" type="button">
      <span class="font-stk09-mono text-xs font-bold tracking-[0.08em] opacity-85">Ticket #4824</span>
      <b class="text-xl font-extrabold tracking-[-0.02em]">SSO redirect fails</b>
      <i class="mt-auto font-stk09-mono text-xs not-italic opacity-85">High &middot; Auth</i>
    </button>
  </div>
  <div class="flex flex-col items-center gap-2">
    <button class="rounded-xl border border-stk09-line bg-stk09-btn px-5.5 py-2.75 text-sm font-bold text-white cursor-pointer transition-colors duration-200 hover:bg-stk09-btnh focus-visible:outline-3 focus-visible:outline-stk09-ring focus-visible:outline-offset-2" id="stk-09-next" type="button">Next ticket &#8635;</button>
    <p class="sr-only" id="stk-09-live" aria-live="polite"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk09-bg: #101219;
  --color-stk09-bg: oklch(0.19 0.012 265);
  --color-stk09-btn: #232838;
  --color-stk09-btn: oklch(0.28 0.018 265);
  --color-stk09-btnh: #2e3446;
  --color-stk09-btnh: oklch(0.33 0.02 265);
  --color-stk09-line: #333a4e;
  --color-stk09-line: oklch(0.36 0.02 265);
  --color-stk09-ring: #5aa2e0;
  --color-stk09-ring: oklch(0.66 0.15 250);
  --color-stk09-c1: #d2604c;
  --color-stk09-c1: oklch(0.63 0.17 20);
  --color-stk09-c2: #45ab7c;
  --color-stk09-c2: oklch(0.66 0.15 150);
  --color-stk09-c3: #4d8ade;
  --color-stk09-c3: oklch(0.64 0.16 250);
  --color-stk09-c4: #9b6ed6;
  --color-stk09-c4: oklch(0.64 0.16 300);
  --font-stk09-sans: 'Archivo', system-ui, sans-serif;
  --font-stk09-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-stk09: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.stk-09');
  if (!root) return;
  const deck = root.querySelector('#stk-09-deck');
  const live = root.querySelector('#stk-09-live');

  /* The controller writes ONE integer per card. Translate, scale and z-index
     are all derived from it by arbitrary calc() utilities in the markup. */
  const paint = () => [...deck.children].forEach((c, i) => c.style.setProperty('--depth', i));

  function cycle() {
    const front = deck.firstElementChild;
    if (!front) return;
    front.dataset.sending = 'true';
    front.addEventListener('transitionend', () => {
      delete front.dataset.sending;
      deck.appendChild(front);
      paint();
      const title = deck.firstElementChild.querySelector('b');
      if (title) live.textContent = 'Now showing ' + title.textContent;
    }, { once: true });
  }

  deck.addEventListener('click', (e) => {
    if (e.target.closest('button') === deck.firstElementChild) cycle();
  });
  root.querySelector('#stk-09-next').addEventListener('click', cycle);
  paint();
})();
```
