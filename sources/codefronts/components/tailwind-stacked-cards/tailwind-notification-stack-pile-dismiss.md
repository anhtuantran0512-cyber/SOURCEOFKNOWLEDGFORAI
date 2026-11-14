---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-notification-stack-pile-dismiss/"
title: "Tailwind Notification Stack Pile Dismiss"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "An OS-style alert pile: new notifications spring onto the top, older ones compress below, and one toggle switches the whole thing between a compact deck and…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Notification Stack Pile Dismiss
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-notification-stack-pile-dismiss/

An OS-style alert pile: new notifications spring onto the top, older ones compress below, and one toggle switches the whole thing between a compact deck and a spaced list. The two layouts are one data-open attribute on the pile &mdash; data-[open=true]: variants flip every card from absolute-and-scaled to relative-and-flat, so there is no second stylesheet for the expanded state.
## HTML
```html
<section class="stk-25 w-full min-h-svh flex items-center justify-center px-5 py-10 font-stk25-sans bg-stk25-bg" aria-label="Notification pile">
  <div class="w-[min(340px,100%)]">
    <div class="mb-4 flex items-center justify-between text-stk25-ink">
      <b class="text-base font-extrabold">Notifications</b>
      <button class="rounded-[9px] border border-stk25-line bg-transparent px-3 py-1.5 font-stk25-mono text-xs font-medium text-stk25-body cursor-pointer transition-colors duration-200 hover:bg-stk25-btn hover:text-white focus-visible:outline-3 focus-visible:outline-stk25-ring focus-visible:outline-offset-2" id="stk-25-exp" type="button" aria-expanded="false">Expand</button>
    </div>
    <div class="group relative h-30 transition-[height] duration-400 data-[open=true]:h-auto" id="stk-25-pile" data-open="false" aria-live="polite">
      <article class="absolute inset-x-0 top-0 flex flex-col gap-1 rounded-[14px] border border-stk25-line border-l-4 border-l-stk25-n1 bg-stk25-note px-4.5 py-4 text-stk25-ink shadow-[0_14px_30px_-18px_rgba(0,0,0,0.8)] [transform:translateY(calc(var(--d,0)*12px))_scale(calc(1-var(--d,0)*0.05))] [z-index:calc(20-var(--d,0))] transition-[transform,opacity] duration-450 ease-stk25 data-[gone=true]:opacity-0 data-[enter=true]:animate-stk25-pop group-data-[open=true]:relative group-data-[open=true]:transform-none group-data-[open=true]:mb-2.5 motion-reduce:transition-opacity motion-reduce:duration-200 motion-reduce:animate-none">
        <b class="text-sm font-extrabold">New comment</b>
        <span class="text-[13px] text-stk25-body">Dana replied to your thread.</span>
      </article>
      <article class="absolute inset-x-0 top-0 flex flex-col gap-1 rounded-[14px] border border-stk25-line border-l-4 border-l-stk25-n2 bg-stk25-note px-4.5 py-4 text-stk25-ink shadow-[0_14px_30px_-18px_rgba(0,0,0,0.8)] [transform:translateY(calc(var(--d,0)*12px))_scale(calc(1-var(--d,0)*0.05))] [z-index:calc(20-var(--d,0))] transition-[transform,opacity] duration-450 ease-stk25 data-[gone=true]:opacity-0 data-[enter=true]:animate-stk25-pop group-data-[open=true]:relative group-data-[open=true]:transform-none group-data-[open=true]:mb-2.5 motion-reduce:transition-opacity motion-reduce:duration-200 motion-reduce:animate-none">
        <b class="text-sm font-extrabold">Build passed</b>
        <span class="text-[13px] text-stk25-body">main deployed in 2m 14s.</span>
      </article>
      <article class="absolute inset-x-0 top-0 flex flex-col gap-1 rounded-[14px] border border-stk25-line border-l-4 border-l-stk25-n3 bg-stk25-note px-4.5 py-4 text-stk25-ink shadow-[0_14px_30px_-18px_rgba(0,0,0,0.8)] [transform:translateY(calc(var(--d,0)*12px))_scale(calc(1-var(--d,0)*0.05))] [z-index:calc(20-var(--d,0))] transition-[transform,opacity] duration-450 ease-stk25 data-[gone=true]:opacity-0 data-[enter=true]:animate-stk25-pop group-data-[open=true]:relative group-data-[open=true]:transform-none group-data-[open=true]:mb-2.5 motion-reduce:transition-opacity motion-reduce:duration-200 motion-reduce:animate-none">
        <b class="text-sm font-extrabold">Reminder</b>
        <span class="text-[13px] text-stk25-body">Standup starts in 10 minutes.</span>
      </article>
    </div>
    <div class="mt-4 flex gap-2.5">
      <button class="flex-1 rounded-[11px] border-0 bg-stk25-btn px-4 py-2.75 text-[13px] font-bold text-white cursor-pointer transition-colors duration-200 hover:bg-stk25-btnh focus-visible:outline-3 focus-visible:outline-stk25-ring focus-visible:outline-offset-2" id="stk-25-add" type="button">Simulate alert</button>
      <button class="flex-1 rounded-[11px] border-0 bg-stk25-btn px-4 py-2.75 text-[13px] font-bold text-white cursor-pointer transition-colors duration-200 hover:bg-stk25-btnh focus-visible:outline-3 focus-visible:outline-stk25-ring focus-visible:outline-offset-2" id="stk-25-dismiss" type="button">Dismiss top</button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk25-bg: #0e0f16;
  --color-stk25-bg: oklch(0.17 0.012 275);
  --color-stk25-note: #1b1e2a;
  --color-stk25-note: oklch(0.24 0.016 275);
  --color-stk25-line: #2a2e3c;
  --color-stk25-line: oklch(0.32 0.018 275);
  --color-stk25-btn: #242838;
  --color-stk25-btn: oklch(0.28 0.020 275);
  --color-stk25-btnh: #2e3346;
  --color-stk25-btnh: oklch(0.33 0.022 275);
  --color-stk25-ink: #eef0f6;
  --color-stk25-ink: oklch(0.95 0.006 275);
  --color-stk25-body: #a9adc0;
  --color-stk25-body: oklch(0.74 0.018 275);
  --color-stk25-ring: #5aa2e0;
  --color-stk25-ring: oklch(0.66 0.15 250);
  --color-stk25-n1: #4d8ade;
  --color-stk25-n1: oklch(0.66 0.15 250);
  --color-stk25-n2: #4bbd8c;
  --color-stk25-n2: oklch(0.68 0.15 150);
  --color-stk25-n3: #e0a03f;
  --color-stk25-n3: oklch(0.70 0.15 60);
  --color-stk25-n4: #b07ce0;
  --color-stk25-n4: oklch(0.66 0.15 300);
  --font-stk25-sans: 'Archivo', system-ui, sans-serif;
  --font-stk25-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-stk25: cubic-bezier(0.34, 1.4, 0.5, 1);
  --animate-stk25-pop: stk-25-pop 0.5s cubic-bezier(0.34, 1.56, 0.5, 1);
}

@keyframes stk-25-pop {
  from {
    transform: translateY(-40px) scale(0.9);
    opacity: 0;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.stk-25');
  if (!root) return;
  const pile = root.querySelector('#stk-25-pile');
  const toggle = root.querySelector('#stk-25-exp');
  const samples = [
    ['New follower', 'Sam started following you.', 'stk25-n4'],
    ['Payment received', '$49 from Acme Co.', 'stk25-n2'],
    ['Mention', 'You were tagged in #design.', 'stk25-n1'],
    ['Storage low', '92% of your quota used.', 'stk25-n3'],
  ];
  let s = 0;

  /* The depth cap is a rendering-cost decision, so it lives where the loop is:
     the fifth and the hundredth notification share a depth. */
  const paint = () => [...pile.children].forEach((n, i) => n.style.setProperty('--d', Math.min(i, 4)));

  function add() {
    const [title, body, tone] = samples[s++ % samples.length];
    const el = pile.firstElementChild.cloneNode(true);
    el.className = el.className.replace(/border-l-stk25-n\d/, 'border-l-' + tone);
    el.querySelector('b').textContent = title;
    el.querySelector('span').textContent = body;
    el.dataset.enter = 'true';
    pile.insertBefore(el, pile.firstElementChild);
    paint();
    el.addEventListener('animationend', () => { delete el.dataset.enter; }, { once: true });
  }

  function dismiss() {
    const top = pile.firstElementChild;
    if (!top) return;
    top.dataset.gone = 'true';
    top.addEventListener('transitionend', () => { top.remove(); paint(); }, { once: true });
  }

  root.querySelector('#stk-25-add').addEventListener('click', add);
  root.querySelector('#stk-25-dismiss').addEventListener('click', dismiss);
  toggle.addEventListener('click', () => {
    const open = pile.dataset.open !== 'true';
    pile.dataset.open = String(open);
    toggle.textContent = open ? 'Collapse' : 'Expand';
    toggle.setAttribute('aria-expanded', String(open));
  });
  root.addEventListener('keydown', (e) => { if (e.key === 'Escape') dismiss(); });

  paint();
})();
```
