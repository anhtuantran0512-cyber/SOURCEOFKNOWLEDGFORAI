---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-mobile-swipe-card-stack-translate3d/"
title: "Tailwind Mobile Swipe Card Stack Translate3d"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "A thumb-first media deck that loops forever."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mobile Swipe Card Stack Translate3d
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-mobile-swipe-card-stack-translate3d/

A thumb-first media deck that loops forever. Depth is one --d per card feeding a translate3d and a scale; the drag writes a live translate3d inline; and the commit flings the card off and re-appends it to the back. The port's contribution is that [touch-action:none], will-change-transform and data-[drag=true]:transition-none now sit on the card, where anyone debugging a janky swipe will look first.
## HTML
```html
<section class="stk-20 w-full min-h-svh flex flex-col items-center justify-center gap-[22px] px-5 py-10 font-stk20-sans bg-stk20-bg" aria-label="Touch swipe media stack">
  <div class="relative w-[min(300px,84vw)] h-95 focus-visible:outline-3 focus-visible:outline-stk20-ring focus-visible:outline-offset-8 focus-visible:rounded-[26px]" id="stk-20-deck" tabindex="0" role="group" aria-label="Photo deck. Swipe, or use the arrow keys.">
    <article class="absolute inset-0 overflow-hidden rounded-[22px] bg-stk20-card cursor-grab select-none will-change-transform [touch-action:none] shadow-[0_24px_50px_-26px_rgba(0,0,0,0.85)] [transform:translate3d(0,calc(var(--d,0)*14px),0)_scale(calc(1-var(--d,0)*0.05))] [z-index:calc(10-var(--d,0))] transition-[transform,opacity] duration-450 ease-stk20 data-[drag=true]:transition-none data-[drag=true]:cursor-grabbing data-[fly=true]:opacity-0 motion-reduce:duration-200">
      <img class="block size-full object-cover pointer-events-none" src="https://picsum.photos/seed/tw-sw-1/360/440" width="360" height="440" alt="Narrow lane in Kyoto at dusk">
      <span class="absolute left-4 bottom-3.5 font-stk20-mono text-base font-bold text-white [text-shadow:0_2px_10px_rgba(0,0,0,0.6)]">Kyoto &middot; JP</span>
    </article>
    <article class="absolute inset-0 overflow-hidden rounded-[22px] bg-stk20-card cursor-grab select-none will-change-transform [touch-action:none] shadow-[0_24px_50px_-26px_rgba(0,0,0,0.85)] [transform:translate3d(0,calc(var(--d,0)*14px),0)_scale(calc(1-var(--d,0)*0.05))] [z-index:calc(10-var(--d,0))] transition-[transform,opacity] duration-450 ease-stk20 data-[drag=true]:transition-none data-[drag=true]:cursor-grabbing data-[fly=true]:opacity-0 motion-reduce:duration-200">
      <img class="block size-full object-cover pointer-events-none" src="https://picsum.photos/seed/tw-sw-2/360/440" width="360" height="440" alt="Red cabins on the Lofoten shoreline">
      <span class="absolute left-4 bottom-3.5 font-stk20-mono text-base font-bold text-white [text-shadow:0_2px_10px_rgba(0,0,0,0.6)]">Lofoten &middot; NO</span>
    </article>
    <article class="absolute inset-0 overflow-hidden rounded-[22px] bg-stk20-card cursor-grab select-none will-change-transform [touch-action:none] shadow-[0_24px_50px_-26px_rgba(0,0,0,0.85)] [transform:translate3d(0,calc(var(--d,0)*14px),0)_scale(calc(1-var(--d,0)*0.05))] [z-index:calc(10-var(--d,0))] transition-[transform,opacity] duration-450 ease-stk20 data-[drag=true]:transition-none data-[drag=true]:cursor-grabbing data-[fly=true]:opacity-0 motion-reduce:duration-200">
      <img class="block size-full object-cover pointer-events-none" src="https://picsum.photos/seed/tw-sw-3/360/440" width="360" height="440" alt="Cracked salt flats in the Atacama">
      <span class="absolute left-4 bottom-3.5 font-stk20-mono text-base font-bold text-white [text-shadow:0_2px_10px_rgba(0,0,0,0.6)]">Atacama &middot; CL</span>
    </article>
    <article class="absolute inset-0 overflow-hidden rounded-[22px] bg-stk20-card cursor-grab select-none will-change-transform [touch-action:none] shadow-[0_24px_50px_-26px_rgba(0,0,0,0.85)] [transform:translate3d(0,calc(var(--d,0)*14px),0)_scale(calc(1-var(--d,0)*0.05))] [z-index:calc(10-var(--d,0))] transition-[transform,opacity] duration-450 ease-stk20 data-[drag=true]:transition-none data-[drag=true]:cursor-grabbing data-[fly=true]:opacity-0 motion-reduce:duration-200">
      <img class="block size-full object-cover pointer-events-none" src="https://picsum.photos/seed/tw-sw-4/360/440" width="360" height="440" alt="Lake and peaks above Queenstown">
      <span class="absolute left-4 bottom-3.5 font-stk20-mono text-base font-bold text-white [text-shadow:0_2px_10px_rgba(0,0,0,0.6)]">Queenstown &middot; NZ</span>
    </article>
  </div>
  <div class="flex items-center gap-4.5">
    <button class="grid place-items-center size-11.5 rounded-full border border-stk20-line bg-stk20-btn text-2xl text-white cursor-pointer transition-colors duration-200 hover:bg-stk20-btnh focus-visible:outline-3 focus-visible:outline-stk20-ring focus-visible:outline-offset-2" id="stk-20-prev" type="button" aria-label="Previous card">&lsaquo;</button>
    <p class="m-0 min-w-15 text-center font-stk20-mono text-[13px] text-stk20-muted" id="stk-20-live" aria-live="polite"></p>
    <button class="grid place-items-center size-11.5 rounded-full border border-stk20-line bg-stk20-btn text-2xl text-white cursor-pointer transition-colors duration-200 hover:bg-stk20-btnh focus-visible:outline-3 focus-visible:outline-stk20-ring focus-visible:outline-offset-2" id="stk-20-next" type="button" aria-label="Next card">&rsaquo;</button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk20-bg: #12131b;
  --color-stk20-bg: oklch(0.20 0.014 275);
  --color-stk20-card: #1d1f2a;
  --color-stk20-card: oklch(0.25 0.016 275);
  --color-stk20-btn: #20232f;
  --color-stk20-btn: oklch(0.26 0.016 275);
  --color-stk20-btnh: #2b2f3e;
  --color-stk20-btnh: oklch(0.32 0.018 275);
  --color-stk20-line: #333a4e;
  --color-stk20-line: oklch(0.36 0.02 275);
  --color-stk20-muted: #9aa0b4;
  --color-stk20-muted: oklch(0.70 0.018 275);
  --color-stk20-ring: #5aa2e0;
  --color-stk20-ring: oklch(0.68 0.15 250);
  --font-stk20-sans: 'Archivo', system-ui, sans-serif;
  --font-stk20-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-stk20: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.stk-20');
  if (!root) return;
  const deck = root.querySelector('#stk-20-deck');
  const live = root.querySelector('#stk-20-live');
  const THRESHOLD = 80;

  function paint() {
    [...deck.children].forEach((c, i) => c.style.setProperty('--d', i));
    const label = deck.firstElementChild.querySelector('span');
    live.textContent = label ? label.textContent : '';
    bind(deck.firstElementChild);
  }

  function sendBack(card) {
    card.dataset.fly = 'true';
    card.addEventListener('transitionend', () => {
      delete card.dataset.fly;
      card.style.transform = '';
      deck.appendChild(card);
      paint();
    }, { once: true });
  }

  function bringFront() {
    deck.insertBefore(deck.lastElementChild, deck.firstElementChild);
    paint();
  }

  function bind(card) {
    if (card.dataset.bound) return;
    card.dataset.bound = '1';
    let sx = 0, dx = 0, drag = false;

    card.addEventListener('pointerdown', (e) => {
      if (card !== deck.firstElementChild) return;
      drag = true; sx = e.clientX;
      card.setPointerCapture(e.pointerId);
      card.dataset.drag = 'true';
    });

    /* translate3d, not translateX: the card gets its own composited layer, so
       the drag never touches layout or paint. */
    card.addEventListener('pointermove', (e) => {
      if (!drag) return;
      dx = e.clientX - sx;
      card.style.transform = 'translate3d(' + dx + 'px,0,0) rotate(' + (dx / 22) + 'deg)';
    });

    card.addEventListener('pointerup', () => {
      if (!drag) return;
      drag = false;
      delete card.dataset.drag;
      if (Math.abs(dx) > THRESHOLD) {
        const dir = dx > 0 ? 1 : -1;
        card.style.transform = 'translate3d(' + dir * 140 + '%,0,0) rotate(' + dir * 18 + 'deg)';
        sendBack(card);
      } else {
        card.style.transform = '';
      }
      dx = 0;
    });
  }

  root.querySelector('#stk-20-next').addEventListener('click', () => {
    const c = deck.firstElementChild;
    c.style.transform = 'translate3d(-140%,0,0) rotate(-16deg)';
    sendBack(c);
  });
  root.querySelector('#stk-20-prev').addEventListener('click', bringFront);
  deck.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') { const c = deck.firstElementChild; c.style.transform = 'translate3d(-140%,0,0)'; sendBack(c); }
    if (e.key === 'ArrowRight') bringFront();
  });

  paint();
})();
```
