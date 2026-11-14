---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-multi-step-form-card-stack/"
title: "Tailwind Multi Step Form Card Stack"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "A wizard as a deck."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Multi Step Form Card Stack
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-multi-step-form-card-stack/

A wizard as a deck. The four [data-state] rules become four data-[state=…] variant sets typed on every card, so a step's whole life &mdash; waiting behind, in focus, sunk to the back &mdash; reads in one class list. Native constraint validation gates the advance, inert keeps focus out of the cards behind, and user-invalid: paints the error state without a single line of script.
## HTML
```html
<section class="stk-07 w-full min-h-svh flex items-center justify-center px-5 py-12 font-stk07-sans bg-stk07-bg" aria-label="Multi-step form stack">
  <div class="w-[min(400px,100%)]">
    <div class="h-1.5 mb-4.5 rounded-full bg-stk07-track overflow-hidden">
      <span class="block h-full w-1/3 rounded-full bg-stk07-accent transition-[width] duration-450 ease-stk07 motion-reduce:transition-none" id="stk-07-fill"></span>
    </div>
    <form class="relative h-85" id="stk-07-deck" novalidate>
      <fieldset class="absolute inset-0 flex flex-col gap-3 border-0 rounded-[20px] bg-white p-7 shadow-[0_24px_50px_-30px_rgba(20,24,50,0.5)] transition-[transform,opacity] duration-500 ease-stk07 data-[state=active]:z-3 data-[state=active]:translate-y-0 data-[state=active]:scale-100 data-[state=active]:opacity-100 data-[state=next]:z-2 data-[state=next]:translate-y-6 data-[state=next]:scale-[0.93] data-[state=next]:opacity-55 data-[state=next2]:z-1 data-[state=next2]:translate-y-11 data-[state=next2]:scale-[0.86] data-[state=next2]:opacity-30 data-[state=done]:z-0 data-[state=done]:translate-y-20 data-[state=done]:scale-[0.8] data-[state=done]:opacity-0 motion-reduce:transition-none">
        <p class="m-0 font-stk07-mono text-xs font-bold tracking-[0.12em] uppercase text-stk07-accent">Step 1 of 3</p>
        <h3 class="m-0 text-[23px] font-extrabold tracking-[-0.02em] text-stk07-ink">Your details</h3>
        <label class="flex flex-col gap-1.5 text-[13px] font-semibold text-stk07-label">Full name
          <input class="font-inherit font-normal px-3.5 py-2.75 rounded-[11px] border-[1.5px] border-stk07-line bg-stk07-field text-stk07-ink focus:outline-none focus:border-stk07-accent focus:ring-3 focus:ring-stk07-accent/20 user-invalid:border-stk07-bad" required type="text" placeholder="Alex Rivera">
        </label>
        <label class="flex flex-col gap-1.5 text-[13px] font-semibold text-stk07-label">Email
          <input class="font-inherit font-normal px-3.5 py-2.75 rounded-[11px] border-[1.5px] border-stk07-line bg-stk07-field text-stk07-ink focus:outline-none focus:border-stk07-accent focus:ring-3 focus:ring-stk07-accent/20 user-invalid:border-stk07-bad" required type="email" placeholder="[email protected]">
        </label>
        <div class="mt-auto flex items-center justify-between">
          <span></span>
          <button class="rounded-[11px] border-0 bg-stk07-accent px-5 py-2.75 text-sm font-bold text-white cursor-pointer transition-[transform,filter] duration-150 hover:brightness-110 active:scale-95 focus-visible:outline-3 focus-visible:outline-stk07-accent focus-visible:outline-offset-2" data-act="next" type="button">Continue</button>
        </div>
      </fieldset>
      <fieldset class="absolute inset-0 flex flex-col gap-3 border-0 rounded-[20px] bg-white p-7 shadow-[0_24px_50px_-30px_rgba(20,24,50,0.5)] transition-[transform,opacity] duration-500 ease-stk07 data-[state=active]:z-3 data-[state=active]:translate-y-0 data-[state=active]:scale-100 data-[state=active]:opacity-100 data-[state=next]:z-2 data-[state=next]:translate-y-6 data-[state=next]:scale-[0.93] data-[state=next]:opacity-55 data-[state=next2]:z-1 data-[state=next2]:translate-y-11 data-[state=next2]:scale-[0.86] data-[state=next2]:opacity-30 data-[state=done]:z-0 data-[state=done]:translate-y-20 data-[state=done]:scale-[0.8] data-[state=done]:opacity-0 motion-reduce:transition-none">
        <p class="m-0 font-stk07-mono text-xs font-bold tracking-[0.12em] uppercase text-stk07-accent">Step 2 of 3</p>
        <h3 class="m-0 text-[23px] font-extrabold tracking-[-0.02em] text-stk07-ink">Your project</h3>
        <label class="flex flex-col gap-1.5 text-[13px] font-semibold text-stk07-label">Project name
          <input class="font-inherit font-normal px-3.5 py-2.75 rounded-[11px] border-[1.5px] border-stk07-line bg-stk07-field text-stk07-ink focus:outline-none focus:border-stk07-accent focus:ring-3 focus:ring-stk07-accent/20 user-invalid:border-stk07-bad" required type="text" placeholder="Northwind redesign">
        </label>
        <label class="flex flex-col gap-1.5 text-[13px] font-semibold text-stk07-label">Budget
          <select class="font-inherit font-normal px-3.5 py-2.75 rounded-[11px] border-[1.5px] border-stk07-line bg-stk07-field text-stk07-ink focus:outline-none focus:border-stk07-accent focus:ring-3 focus:ring-stk07-accent/20 user-invalid:border-stk07-bad" required>
            <option value="">Select&hellip;</option><option>&lt; $5k</option><option>$5k&ndash;$20k</option><option>$20k+</option>
          </select>
        </label>
        <div class="mt-auto flex items-center justify-between">
          <button class="rounded-[11px] border-0 bg-transparent text-sm font-semibold text-stk07-label cursor-pointer hover:text-stk07-ink focus-visible:outline-3 focus-visible:outline-stk07-accent focus-visible:outline-offset-2" data-act="back" type="button">Back</button>
          <button class="rounded-[11px] border-0 bg-stk07-accent px-5 py-2.75 text-sm font-bold text-white cursor-pointer transition-[transform,filter] duration-150 hover:brightness-110 active:scale-95 focus-visible:outline-3 focus-visible:outline-stk07-accent focus-visible:outline-offset-2" data-act="next" type="button">Continue</button>
        </div>
      </fieldset>
      <fieldset class="absolute inset-0 flex flex-col gap-3 border-0 rounded-[20px] bg-white p-7 shadow-[0_24px_50px_-30px_rgba(20,24,50,0.5)] transition-[transform,opacity] duration-500 ease-stk07 data-[state=active]:z-3 data-[state=active]:translate-y-0 data-[state=active]:scale-100 data-[state=active]:opacity-100 data-[state=next]:z-2 data-[state=next]:translate-y-6 data-[state=next]:scale-[0.93] data-[state=next]:opacity-55 data-[state=next2]:z-1 data-[state=next2]:translate-y-11 data-[state=next2]:scale-[0.86] data-[state=next2]:opacity-30 data-[state=done]:z-0 data-[state=done]:translate-y-20 data-[state=done]:scale-[0.8] data-[state=done]:opacity-0 motion-reduce:transition-none">
        <p class="m-0 font-stk07-mono text-xs font-bold tracking-[0.12em] uppercase text-stk07-accent">Step 3 of 3</p>
        <h3 class="m-0 text-[23px] font-extrabold tracking-[-0.02em] text-stk07-ink">Almost done</h3>
        <label class="flex flex-col gap-1.5 text-[13px] font-semibold text-stk07-label">Anything else?
          <textarea class="font-inherit font-normal px-3.5 py-2.75 rounded-[11px] border-[1.5px] border-stk07-line bg-stk07-field text-stk07-ink focus:outline-none focus:border-stk07-accent focus:ring-3 focus:ring-stk07-accent/20" rows="3" placeholder="Timeline, links, context&hellip;"></textarea>
        </label>
        <div class="mt-auto flex items-center justify-between">
          <button class="rounded-[11px] border-0 bg-transparent text-sm font-semibold text-stk07-label cursor-pointer hover:text-stk07-ink focus-visible:outline-3 focus-visible:outline-stk07-accent focus-visible:outline-offset-2" data-act="back" type="button">Back</button>
          <button class="rounded-[11px] border-0 bg-stk07-accent px-5 py-2.75 text-sm font-bold text-white cursor-pointer transition-[transform,filter] duration-150 hover:brightness-110 active:scale-95 focus-visible:outline-3 focus-visible:outline-stk07-accent focus-visible:outline-offset-2" data-act="done" type="button">Submit &check;</button>
        </div>
      </fieldset>
      <div class="absolute inset-0 z-4 grid place-items-center rounded-[20px] bg-white p-8 text-center text-[17px] font-semibold text-stk07-ink shadow-[0_24px_50px_-30px_rgba(20,24,50,0.5)] hidden not-hidden:grid" id="stk-07-thanks" hidden>Thanks &mdash; we&rsquo;ll be in touch within a day.</div>
    </form>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk07-bg: #f2f3f7;
  --color-stk07-bg: oklch(0.96 0.004 265);
  --color-stk07-ink: #1a1d27;
  --color-stk07-ink: oklch(0.24 0.014 265);
  --color-stk07-label: #4a4f5e;
  --color-stk07-label: oklch(0.44 0.014 265);
  --color-stk07-line: #d6d9e2;
  --color-stk07-line: oklch(0.88 0.008 265);
  --color-stk07-field: #f8f9fb;
  --color-stk07-field: oklch(0.98 0.003 265);
  --color-stk07-track: #dde0e8;
  --color-stk07-track: oklch(0.90 0.008 265);
  --color-stk07-accent: #5b78e8;
  --color-stk07-accent: oklch(0.62 0.17 262);
  --color-stk07-bad: #dd5a44;
  --color-stk07-bad: oklch(0.62 0.20 22);
  --font-stk07-sans: 'Archivo', system-ui, sans-serif;
  --font-stk07-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-stk07: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.stk-07');
  if (!root) return;
  const deck = root.querySelector('#stk-07-deck');
  const cards = [...deck.querySelectorAll('fieldset')];
  const fill = root.querySelector('#stk-07-fill');
  const thanks = root.querySelector('#stk-07-thanks');
  let i = 0;

  /* The controller sets ONE attribute per card. What each state looks like
     lives in the data-[state=…] variants on the cards themselves. */
  function paint() {
    cards.forEach((c, idx) => {
      c.dataset.state = idx < i ? 'done' : idx === i ? 'active' : idx === i + 1 ? 'next' : 'next2';
      c.toggleAttribute('inert', idx !== i);
      c.setAttribute('aria-current', idx === i ? 'step' : 'false');
    });
    fill.style.width = ((i + 1) / cards.length * 100) + '%';
    const first = cards[i].querySelector('input,select,textarea');
    if (first) setTimeout(() => first.focus(), 260);
  }

  function valid(card) {
    for (const f of card.querySelectorAll('input,select,textarea')) {
      if (!f.checkValidity()) { f.reportValidity(); return false; }
    }
    return true;
  }

  deck.addEventListener('click', (e) => {
    const act = e.target.closest('[data-act]');
    if (!act) return;
    if (act.dataset.act === 'next' && valid(cards[i])) { i = Math.min(i + 1, cards.length - 1); paint(); }
    if (act.dataset.act === 'back') { i = Math.max(i - 1, 0); paint(); }
    if (act.dataset.act === 'done' && valid(cards[i])) {
      cards.forEach((c) => { c.dataset.state = 'done'; c.setAttribute('inert', ''); });
      fill.style.width = '100%';
      thanks.hidden = false;
      thanks.focus?.();
    }
  });

  paint();
})();
```
