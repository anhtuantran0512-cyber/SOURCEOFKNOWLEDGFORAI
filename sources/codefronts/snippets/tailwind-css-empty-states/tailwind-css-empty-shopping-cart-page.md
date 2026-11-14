---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-empty-shopping-cart-page/"
title: "Tailwind CSS Empty Shopping Cart Page"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "An e-commerce bag that is empty but never a dead end: an editorial headline, two clear paths (shop, reorder) and a shelf of best-sellers you can add straight…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Empty Shopping Cart Page
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-empty-shopping-cart-page/

An e-commerce bag that is empty but never a dead end: an editorial headline, two clear paths (shop, reorder) and a shelf of best-sellers you can add straight into the bag. Add one and the empty state gives way to line items, a subtotal and a free-delivery progress bar — a conversion detail the CSS original didn't have.
## HTML
```html
<div class="tes-03 group/root w-full min-h-svh bg-tes03-bg font-tes03-sans text-tes03-ink antialiased" data-bag="empty">
  <header class="flex flex-wrap items-center gap-x-8 gap-y-3 border-b border-tes03-line px-[clamp(1rem,4vw,3rem)] py-4">
    <a href="#" class="font-tes03-serif text-2xl tracking-tight focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes03-acc">Fold &amp; Vessel</a>
    <nav aria-label="Shop" class="order-3 flex w-full gap-5 overflow-x-auto text-sm text-tes03-mut sm:order-none sm:w-auto sm:flex-1">
      <a href="#" class="py-2 transition-colors hover:text-tes03-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes03-acc">Ceramics</a>
      <a href="#" class="py-2 transition-colors hover:text-tes03-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes03-acc">Glassware</a>
      <a href="#" class="py-2 transition-colors hover:text-tes03-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes03-acc">Linen</a>
      <a href="#" class="py-2 transition-colors hover:text-tes03-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes03-acc">Journal</a>
    </nav>
    <div class="ml-auto flex gap-1">
      <button type="button" aria-label="Search" class="grid size-11 place-items-center rounded-full transition-colors hover:bg-tes03-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes03-acc"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.5"/><path d="m16 16 4 4"/></svg></button>
      <button type="button" aria-label="Bag" class="relative grid size-11 place-items-center rounded-full transition-colors hover:bg-tes03-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes03-acc"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 8h14l-1.2 11.2a1.5 1.5 0 0 1-1.5 1.3H7.7a1.5 1.5 0 0 1-1.5-1.3z"/><path d="M9 8V6.5a3 3 0 0 1 6 0V8"/></svg><span id="tes03-count" hidden class="absolute top-1 right-1 grid h-4.5 min-w-4.5 place-items-center rounded-full bg-tes03-acc px-1 text-[10px] font-semibold text-white"></span></button>
    </div>
  </header>
  <main class="mx-auto grid w-full max-w-6xl gap-[clamp(2rem,5vw,4rem)] px-[clamp(1rem,4vw,3rem)] py-[clamp(2rem,6vw,4.5rem)] lg:grid-cols-[minmax(0,26rem)_minmax(0,1fr)]">
    <section aria-labelledby="tes03-h" class="grid content-start gap-6">
      <div class="grid justify-items-start gap-4 group-data-[bag=full]/root:hidden">
        <span aria-hidden="true" class="relative grid size-18 place-items-center rounded-full bg-tes03-card text-tes03-acc shadow-[0_0_0_8px_var(--color-tes03-sunk)] ring-1 ring-tes03-line"><svg class="size-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 8h14l-1.2 11.2a1.5 1.5 0 0 1-1.5 1.3H7.7a1.5 1.5 0 0 1-1.5-1.3z"/><path d="M9 8V6.5a3 3 0 0 1 6 0V8M9.5 13.5c1.4 1.2 3.6 1.2 5 0"/></svg></span>
        <h1 id="tes03-h" class="mt-2 font-tes03-serif text-[clamp(2.3rem,5vw,3.4rem)] leading-[1.02] tracking-tight text-balance">Your bag is <em class="text-tes03-acc">waiting</em></h1>
        <p class="max-w-[34ch] text-[15px]/7 text-tes03-mut text-pretty">Everything is made in small runs, so pieces move quickly. Start with the shapes people keep coming back for.</p>
        <div class="flex flex-wrap gap-2.5 pt-1">
          <a href="#" class="inline-flex min-h-11 items-center rounded-full bg-tes03-ink px-6 text-sm font-medium text-tes03-bg transition hover:bg-tes03-acc active:scale-[.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes03-acc">Shop the collection</a>
          <a href="#" class="inline-flex min-h-11 items-center rounded-full border border-tes03-line2 px-5 text-sm transition hover:border-tes03-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes03-acc">Reorder from July</a>
        </div>
        <p class="flex items-center gap-2 pt-2 text-xs text-tes03-mut"><svg class="size-4 text-tes03-olive" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M3 7h11v9H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="17.5" r="1.6"/><circle cx="17" cy="17.5" r="1.6"/></svg>Free UK delivery over £80 · returns within 30 days</p>
      </div>
      <div class="hidden gap-5 group-data-[bag=full]/root:grid">
        <h2 class="font-tes03-serif text-4xl tracking-tight">Your bag</h2>
        <div class="grid gap-2 rounded-2xl bg-tes03-card p-4 ring-1 ring-tes03-line">
          <p id="tes03-ship" role="status" class="text-[13px] text-tes03-mut"></p>
          <div aria-hidden="true" class="h-1.5 overflow-hidden rounded-full bg-tes03-sunk"><span id="tes03-bar" class="block h-full w-0 rounded-full bg-tes03-olive transition-[width] duration-500 ease-out"></span></div>
        </div>
        <ul id="tes03-lines" class="divide-y divide-tes03-line border-y border-tes03-line"></ul>
        <div class="grid gap-2 text-sm">
          <div class="flex justify-between"><span>Subtotal</span><span id="tes03-total" class="font-semibold tabular-nums">£0</span></div>
          <div class="flex justify-between text-tes03-mut"><span>Shipping</span><span>Calculated at checkout</span></div>
        </div>
        <a href="#" class="inline-flex min-h-12 items-center justify-center rounded-full bg-tes03-ink text-sm font-medium text-tes03-bg transition hover:bg-tes03-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes03-acc">Checkout</a>
      </div>
    </section>
    <aside aria-labelledby="tes03-rec" class="grid content-start gap-4">
      <p id="tes03-rec" class="font-tes03-serif text-xl italic text-tes03-mut">Kept coming back</p>
      <ul class="grid grid-cols-[repeat(auto-fill,minmax(11rem,1fr))] gap-4">
        <li class="group overflow-hidden rounded-2xl bg-tes03-card ring-1 ring-tes03-line">
          <figure class="aspect-4/5 overflow-hidden bg-tes03-sunk"><img src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=560&amp;q=80&amp;auto=format&amp;fit=crop" alt="Stoneware cup on a pale surface" width="560" height="700" loading="lazy" decoding="async" class="size-full object-cover transition-transform duration-500 group-hover:scale-105"></figure>
          <div class="grid gap-0.5 p-3.5"><p class="text-sm font-medium">Ash stoneware cup</p><p class="text-xs text-tes03-mut">Matte glaze · 240ml</p>
            <div class="mt-2.5 flex items-center justify-between"><span class="text-sm tabular-nums">£28</span><button type="button" data-add="Ash stoneware cup" data-price="28" class="min-h-11 rounded-full border border-tes03-line2 px-4 text-xs font-medium transition hover:border-tes03-ink data-in:border-tes03-olive data-in:bg-tes03-olive data-in:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes03-acc">Add</button></div></div>
        </li>
        <li class="group overflow-hidden rounded-2xl bg-tes03-card ring-1 ring-tes03-line">
          <figure class="aspect-4/5 overflow-hidden bg-tes03-sunk"><img src="https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=560&amp;q=80&amp;auto=format&amp;fit=crop" alt="Ceramic mug and saucer" width="560" height="700" loading="lazy" decoding="async" class="size-full object-cover transition-transform duration-500 group-hover:scale-105"></figure>
          <div class="grid gap-0.5 p-3.5"><p class="text-sm font-medium">Saucer set of two</p><p class="text-xs text-tes03-mut">Sand clay · 14cm</p>
            <div class="mt-2.5 flex items-center justify-between"><span class="text-sm tabular-nums">£42</span><button type="button" data-add="Saucer set of two" data-price="42" class="min-h-11 rounded-full border border-tes03-line2 px-4 text-xs font-medium transition hover:border-tes03-ink data-in:border-tes03-olive data-in:bg-tes03-olive data-in:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes03-acc">Add</button></div></div>
        </li>
        <li class="group overflow-hidden rounded-2xl bg-tes03-card ring-1 ring-tes03-line">
          <figure class="aspect-4/5 overflow-hidden bg-tes03-sunk"><img src="https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=560&amp;q=80&amp;auto=format&amp;fit=crop" alt="Dark ceramic vessel with coffee" width="560" height="700" loading="lazy" decoding="async" class="size-full object-cover transition-transform duration-500 group-hover:scale-105"></figure>
          <div class="grid gap-0.5 p-3.5"><p class="text-sm font-medium">Ink pour-over jug</p><p class="text-xs text-tes03-mut">Iron glaze · 600ml</p>
            <div class="mt-2.5 flex items-center justify-between"><span class="text-sm tabular-nums">£56</span><button type="button" data-add="Ink pour-over jug" data-price="56" class="min-h-11 rounded-full border border-tes03-line2 px-4 text-xs font-medium transition hover:border-tes03-ink data-in:border-tes03-olive data-in:bg-tes03-olive data-in:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes03-acc">Add</button></div></div>
        </li>
      </ul>
    </aside>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes03-bg: #f8f4ee;
  --color-tes03-bg: oklch(0.966 0.011 75);
  --color-tes03-card: #fffdf9;
  --color-tes03-card: oklch(0.993 0.005 75);
  --color-tes03-sunk: #efe8dd;
  --color-tes03-sunk: oklch(0.93 0.017 75);
  --color-tes03-line: #e4dbcd;
  --color-tes03-line: oklch(0.893 0.021 75);
  --color-tes03-line2: #cdc0ad;
  --color-tes03-line2: oklch(0.81 0.03 75);
  --color-tes03-ink: #231c15;
  --color-tes03-ink: oklch(0.23 0.018 60);
  --color-tes03-mut: #64594c;
  --color-tes03-mut: oklch(0.47 0.022 65);
  --color-tes03-acc: #a65126;
  --color-tes03-acc: oklch(0.54 0.13 45);
  --color-tes03-olive: #56633a;
  --color-tes03-olive: oklch(0.47 0.065 120);
  --font-tes03-sans: 'Geist', system-ui, sans-serif;
  --font-tes03-serif: 'Instrument Serif', Georgia, serif;
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-03 {
  width: 100%;
  min-height: 100svh;
}

.tes-03 [hidden] {
  display: none !important;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tes-03');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const $ = (s) => root.querySelector(s);
  const FREE = 80;
  let bag = [];
  const paint = () => {
    const sum = bag.reduce((a, b) => a + b.price, 0);
    root.dataset.bag = bag.length ? 'full' : 'empty';
    $('#tes03-count').hidden = !bag.length;
    $('#tes03-count').textContent = bag.length;
    $('#tes03-total').textContent = '\u00a3' + sum;
    $('#tes03-bar').style.width = Math.min(100, (sum / FREE) * 100) + '%';
    $('#tes03-ship').textContent = sum >= FREE ? 'You have free UK delivery.' : '\u00a3' + (FREE - sum) + ' away from free UK delivery.';
    $('#tes03-lines').innerHTML = bag.map((it, i) =>
      '<li class="flex items-center gap-3 py-3.5 transition-[opacity,translate] duration-300 starting:translate-y-1 starting:opacity-0">' +
      '<span class="grid flex-1"><b class="text-sm font-medium">' + it.name + '</b><span class="text-xs text-tes03-mut">Ships in 2 days</span></span>' +
      '<span class="text-sm tabular-nums">\u00a3' + it.price + '</span>' +
      '<button type="button" data-rm="' + i + '" aria-label="Remove ' + it.name + '" class="grid size-11 place-items-center rounded-full text-tes03-mut hover:bg-tes03-sunk hover:text-tes03-ink">\u00d7</button></li>'
    ).join('');
    root.querySelectorAll('[data-add]').forEach((b) => {
      const inBag = bag.some((it) => it.name === b.dataset.add);
      b.toggleAttribute('data-in', inBag);
      b.textContent = inBag ? 'In bag' : 'Add';
    });
  };
  root.addEventListener('click', (e) => {
    const add = e.target.closest('[data-add]');
    const rm = e.target.closest('[data-rm]');
    if (add && !bag.some((it) => it.name === add.dataset.add)) bag.push({ name: add.dataset.add, price: +add.dataset.price });
    else if (rm) bag.splice(+rm.dataset.rm, 1);
    else return;
    paint();
  });
  paint();
})();
```
