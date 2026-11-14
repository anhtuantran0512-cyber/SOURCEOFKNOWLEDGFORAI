---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tables/tailwind-shopping-cart-table-quantity-stepper-live-totals/"
title: "Tailwind Shopping Cart Table with Quantity Stepper & Live Totals"
section: "snippets"
category: "tailwind-css-tables"
category_name: "Tailwind CSS Tables"
description: "A light, warm checkout cart that actually works: steppers recalculate every line, the subtotal, shipping and total; removing an item swipes the row out and…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Shopping Cart Table with Quantity Stepper & Live Totals
Source: https://codefronts.com/snippets/tailwind-css-tables/tailwind-shopping-cart-table-quantity-stepper-live-totals/

A light, warm checkout cart that actually works: steppers recalculate every line, the subtotal, shipping and total; removing an item swipes the row out and collapses it; and a free-shipping progress bar tells the shopper how far they are from the threshold. The summary moves beside the table at wide container sizes — the layout every Tier-1 storefront uses.
## HTML
```html
<section class="ttb-05 grid-cols-1 w-full min-h-svh grid place-items-center bg-ttb05-bg px-5 py-14 font-ttb05-sans text-ttb05-ink" aria-label="Shopping cart table demo">
  <div id="ttb05-cart" class="group/cart @container w-full max-w-5xl">
    <header class="mb-6 flex flex-wrap items-end justify-between gap-3">
      <div>
        <h2 class="text-2xl font-extrabold tracking-[-0.02em]">Your cart</h2>
        <p class="mt-1 text-sm text-ttb05-mut"><span data-count>4 items</span> · ships in 1–2 business days</p>
      </div>
      <a href="#" class="text-sm font-semibold text-ttb05-acc-ink underline decoration-ttb05-acc/40 underline-offset-4 hover:decoration-ttb05-acc">Continue shopping</a>
    </header>
    <div class="grid grid-cols-1 items-start gap-6 @3xl:grid-cols-[minmax(0,1fr)_20rem]">
      <div class="relative min-w-0 overflow-x-auto rounded-2xl bg-white shadow-[0_1px_2px_oklch(0_0_0/0.04),0_12px_32px_-12px_oklch(0.4_0.05_50/0.18)] ring-1 ring-ttb05-line">
        <table class="w-full border-collapse text-left text-sm group-data-empty/cart:hidden">
          <caption class="sr-only">Items in your shopping cart</caption>
          <thead class="[&_th]:border-b [&_th]:border-ttb05-line [&_th]:px-5 [&_th]:py-3.5 [&_th]:text-[11px] [&_th]:font-bold [&_th]:tracking-[0.12em] [&_th]:text-ttb05-mut [&_th]:uppercase">
            <tr><th scope="col">Product</th><th scope="col" class="text-right max-sm:hidden">Price</th><th scope="col" class="text-center">Qty</th><th scope="col" class="text-right">Total</th><th scope="col"><span class="sr-only">Remove</span></th></tr>
          </thead>
          <tbody class="[&_td]:px-5 [&_td]:py-5 [&_td]:align-middle max-sm:[&_td]:px-2.5 max-sm:[&_td:first-child]:pl-4">
            <tr data-price="249" data-name="ProSound ANC Headphones" class="border-b border-ttb05-line transition duration-300 data-removing:translate-x-6 data-removing:opacity-0 motion-reduce:transition-none">
              <td><div class="group/p flex items-center gap-4"><span aria-hidden="true" class="grid size-16 max-sm:size-12 flex-none place-items-center rounded-xl bg-linear-135 from-amber-200 to-amber-400 text-sm font-extrabold text-amber-900/70 ring-1 ring-black/5 transition group-hover/p:-rotate-3 group-hover/p:scale-105 motion-reduce:transition-none">ANC</span><div><div class="font-bold">ProSound ANC Headphones</div><div class="mt-0.5 text-xs text-ttb05-mut max-sm:hidden">Midnight black · PS-ANC-900</div><span class="mt-1.5 inline-block rounded bg-ttb05-acc/10 px-1.5 py-0.5 text-[11px] font-semibold text-ttb05-acc-ink">In stock</span></div></div></td>
              <td class="text-right text-ttb05-mut tabular-nums max-sm:hidden">$249.00</td>
              <td><div class="mx-auto flex w-max items-center rounded-xl ring-1 ring-ttb05-line"><button type="button" data-step="-1" aria-label="Decrease quantity of ProSound ANC Headphones" class="grid h-11 w-10 place-items-center rounded-l-xl text-lg font-bold text-ttb05-mut transition hover:bg-ttb05-acc hover:text-white disabled:pointer-events-none disabled:opacity-35 focus-visible:outline-2 focus-visible:outline-ttb05-acc">−</button><input type="number" min="1" max="99" value="1" aria-label="Quantity of ProSound ANC Headphones" class="h-11 w-10 bg-transparent text-center font-bold tabular-nums [appearance:textfield] focus:outline-none [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:appearance-none"><button type="button" data-step="1" aria-label="Increase quantity of ProSound ANC Headphones" class="grid h-11 w-10 place-items-center rounded-r-xl text-lg font-bold text-ttb05-mut transition hover:bg-ttb05-acc hover:text-white focus-visible:outline-2 focus-visible:outline-ttb05-acc">+</button></div></td>
              <td data-line class="text-right text-[15px] font-extrabold tabular-nums">$249.00</td>
              <td class="w-0"><button type="button" data-remove aria-label="Remove ProSound ANC Headphones" class="grid size-11 place-items-center rounded-xl text-ttb05-mut transition hover:bg-red-50 hover:text-red-600 focus-visible:outline-2 focus-visible:outline-red-600"><svg class="size-4.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button></td>
            </tr>
            <tr data-price="129" data-name="MechKey RGB Keyboard" class="border-b border-ttb05-line transition duration-300 data-removing:translate-x-6 data-removing:opacity-0 motion-reduce:transition-none">
              <td><div class="group/p flex items-center gap-4"><span aria-hidden="true" class="grid size-16 max-sm:size-12 flex-none place-items-center rounded-xl bg-linear-135 from-indigo-200 to-indigo-400 text-sm font-extrabold text-indigo-950/60 ring-1 ring-black/5 transition group-hover/p:-rotate-3 group-hover/p:scale-105 motion-reduce:transition-none">TKL</span><div><div class="font-bold">MechKey RGB Keyboard</div><div class="mt-0.5 text-xs text-ttb05-mut max-sm:hidden">Arctic white · MK-RGB-TKL</div><span class="mt-1.5 inline-block rounded bg-ttb05-acc/10 px-1.5 py-0.5 text-[11px] font-semibold text-ttb05-acc-ink">Best seller</span></div></div></td>
              <td class="text-right text-ttb05-mut tabular-nums max-sm:hidden">$129.00</td>
              <td><div class="mx-auto flex w-max items-center rounded-xl ring-1 ring-ttb05-line"><button type="button" data-step="-1" aria-label="Decrease quantity of MechKey RGB Keyboard" class="grid h-11 w-10 place-items-center rounded-l-xl text-lg font-bold text-ttb05-mut transition hover:bg-ttb05-acc hover:text-white disabled:pointer-events-none disabled:opacity-35 focus-visible:outline-2 focus-visible:outline-ttb05-acc">−</button><input type="number" min="1" max="99" value="2" aria-label="Quantity of MechKey RGB Keyboard" class="h-11 w-10 bg-transparent text-center font-bold tabular-nums [appearance:textfield] focus:outline-none [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:appearance-none"><button type="button" data-step="1" aria-label="Increase quantity of MechKey RGB Keyboard" class="grid h-11 w-10 place-items-center rounded-r-xl text-lg font-bold text-ttb05-mut transition hover:bg-ttb05-acc hover:text-white focus-visible:outline-2 focus-visible:outline-ttb05-acc">+</button></div></td>
              <td data-line class="text-right text-[15px] font-extrabold tabular-nums">$258.00</td>
              <td class="w-0"><button type="button" data-remove aria-label="Remove MechKey RGB Keyboard" class="grid size-11 place-items-center rounded-xl text-ttb05-mut transition hover:bg-red-50 hover:text-red-600 focus-visible:outline-2 focus-visible:outline-red-600"><svg class="size-4.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button></td>
            </tr>
            <tr data-price="79" data-name="ErgoClick Pro Mouse" class="transition duration-300 data-removing:translate-x-6 data-removing:opacity-0 motion-reduce:transition-none">
              <td><div class="group/p flex items-center gap-4"><span aria-hidden="true" class="grid size-16 max-sm:size-12 flex-none place-items-center rounded-xl bg-linear-135 from-emerald-200 to-emerald-400 text-sm font-extrabold text-emerald-950/60 ring-1 ring-black/5 transition group-hover/p:-rotate-3 group-hover/p:scale-105 motion-reduce:transition-none">G5</span><div><div class="font-bold">ErgoClick Pro Mouse</div><div class="mt-0.5 text-xs text-ttb05-mut max-sm:hidden">Graphite · EC-PRO-G502</div></div></div></td>
              <td class="text-right text-ttb05-mut tabular-nums max-sm:hidden">$79.00</td>
              <td><div class="mx-auto flex w-max items-center rounded-xl ring-1 ring-ttb05-line"><button type="button" data-step="-1" aria-label="Decrease quantity of ErgoClick Pro Mouse" class="grid h-11 w-10 place-items-center rounded-l-xl text-lg font-bold text-ttb05-mut transition hover:bg-ttb05-acc hover:text-white disabled:pointer-events-none disabled:opacity-35 focus-visible:outline-2 focus-visible:outline-ttb05-acc">−</button><input type="number" min="1" max="99" value="1" aria-label="Quantity of ErgoClick Pro Mouse" class="h-11 w-10 bg-transparent text-center font-bold tabular-nums [appearance:textfield] focus:outline-none [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:appearance-none"><button type="button" data-step="1" aria-label="Increase quantity of ErgoClick Pro Mouse" class="grid h-11 w-10 place-items-center rounded-r-xl text-lg font-bold text-ttb05-mut transition hover:bg-ttb05-acc hover:text-white focus-visible:outline-2 focus-visible:outline-ttb05-acc">+</button></div></td>
              <td data-line class="text-right text-[15px] font-extrabold tabular-nums">$79.00</td>
              <td class="w-0"><button type="button" data-remove aria-label="Remove ErgoClick Pro Mouse" class="grid size-11 place-items-center rounded-xl text-ttb05-mut transition hover:bg-red-50 hover:text-red-600 focus-visible:outline-2 focus-visible:outline-red-600"><svg class="size-4.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button></td>
            </tr>
          </tbody>
        </table>
        <p class="hidden px-6 py-16 text-center text-ttb05-mut group-data-empty/cart:block">Your cart is empty. <a href="#" class="font-semibold text-ttb05-acc-ink underline underline-offset-4">Browse best sellers</a></p>
      </div>
      <aside class="rounded-2xl bg-white p-6 shadow-[0_1px_2px_oklch(0_0_0/0.04),0_12px_32px_-12px_oklch(0.4_0.05_50/0.18)] ring-1 ring-ttb05-line" aria-label="Order summary">
        <h3 class="text-base font-extrabold">Order summary</h3>
        <div class="mt-4 rounded-xl bg-ttb05-bg p-3.5">
          <p data-ship-msg class="text-xs font-semibold text-ttb05-ink">You’ve unlocked free express shipping</p>
          <div class="mt-2 h-1.5 overflow-hidden rounded-full bg-ttb05-line"><div data-bar class="h-full w-full rounded-full bg-linear-to-r from-ttb05-acc to-amber-400 transition-[width] duration-500 motion-reduce:transition-none"></div></div>
        </div>
        <dl class="mt-5 grid gap-3 text-sm [&_dd]:text-right [&_dd]:font-semibold [&_dd]:tabular-nums [&_dt]:text-ttb05-mut">
          <div class="flex justify-between"><dt>Subtotal</dt><dd data-subtotal>$586.00</dd></div>
          <div class="flex justify-between"><dt>Shipping</dt><dd data-shipping class="text-emerald-700">Free</dd></div>
          <div class="flex justify-between border-t border-ttb05-line pt-3 text-base"><dt class="font-bold text-ttb05-ink!">Total</dt><dd data-total class="text-lg font-extrabold">$586.00</dd></div>
        </dl>
        <a href="#" class="mt-6 flex min-h-12 items-center justify-center gap-2 rounded-xl bg-linear-to-r from-ttb05-acc to-orange-400 font-extrabold text-white shadow-[0_10px_24px_-10px_var(--color-ttb05-acc)] transition hover:-translate-y-0.5 hover:shadow-[0_14px_30px_-10px_var(--color-ttb05-acc)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttb05-acc group-data-empty/cart:pointer-events-none group-data-empty/cart:opacity-40 motion-reduce:transition-none">Checkout <span aria-hidden="true">→</span></a>
        <p class="mt-3 text-center text-xs text-ttb05-mut">Taxes calculated at checkout · 30-day returns</p>
        <p role="status" class="sr-only"></p>
      </aside>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb05-bg: #faf7f3;
  --color-ttb05-bg: oklch(0.98 0.007 70);
  --color-ttb05-line: #ece6de;
  --color-ttb05-line: oklch(0.93 0.012 70);
  --color-ttb05-ink: #1c1712;
  --color-ttb05-ink: oklch(0.2 0.015 60);
  --color-ttb05-mut: #6b6157;
  --color-ttb05-mut: oklch(0.5 0.02 60);
  --color-ttb05-acc: #f97316;
  --color-ttb05-acc: oklch(0.7 0.19 47);
  --color-ttb05-acc-ink: #b44a0c;
  --color-ttb05-acc-ink: oklch(0.53 0.15 45);
  --font-ttb05-sans: 'Manrope', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-05 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('ttb05-cart');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const FREE = 500, SHIP = 12;
  const fmt = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' });
  const q = (s) => root.querySelector(s);
  const status = q('[role="status"]');
  const recalc = () => {
    const rows = Array.from(root.querySelectorAll('tbody tr[data-price]:not([data-removing])'));
    let sub = 0, items = 0;
    rows.forEach((r) => {
      const input = r.querySelector('input');
      const n = Math.max(1, Math.min(99, parseInt(input.value, 10) || 1));
      input.value = n;
      const line = n * Number(r.dataset.price);
      r.querySelector('[data-line]').textContent = fmt.format(line);
      r.querySelector('[data-step="-1"]').disabled = n <= 1;
      sub += line;
      items += n;
    });
    const ship = sub === 0 || sub >= FREE ? 0 : SHIP;
    q('[data-subtotal]').textContent = fmt.format(sub);
    q('[data-shipping]').textContent = ship ? fmt.format(ship) : 'Free';
    q('[data-total]').textContent = fmt.format(sub + ship);
    q('[data-count]').textContent = items + (items === 1 ? ' item' : ' items');
    q('[data-bar]').style.width = Math.min(100, sub / FREE * 100) + '%';
    q('[data-ship-msg]').textContent = sub >= FREE ? 'You’ve unlocked free express shipping' : 'Add ' + fmt.format(FREE - sub) + ' more for free express shipping';
    root.toggleAttribute('data-empty', rows.length === 0);
  };
  root.addEventListener('click', (e) => {
    const step = e.target.closest('[data-step]');
    if (step) {
      const input = step.closest('tr').querySelector('input');
      input.value = (parseInt(input.value, 10) || 1) + Number(step.dataset.step);
      recalc();
      return;
    }
    const rm = e.target.closest('[data-remove]');
    if (rm) {
      const tr = rm.closest('tr');
      tr.setAttribute('data-removing', '');
      status.textContent = tr.dataset.name + ' removed from cart';
      recalc();
      setTimeout(() => tr.remove(), 320);
    }
  });
  root.addEventListener('change', (e) => { if (e.target.matches('input[type="number"]')) recalc(); });
  recalc();
})();
```
