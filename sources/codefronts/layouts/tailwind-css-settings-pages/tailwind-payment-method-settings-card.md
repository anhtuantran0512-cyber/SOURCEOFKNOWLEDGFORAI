---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-payment-method-settings-card/"
title: "Tailwind Payment Method Settings Card"
section: "layouts"
category: "tailwind-css-settings-pages"
category_name: "Tailwind CSS Settings Pages"
description: "A premium payment-methods panel: saved cards and a bank account as a selectable radio list, and an add-card form with a holographic 3D card preview that…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Payment Method Settings Card
Source: https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-payment-method-settings-card/

A premium payment-methods panel: saved cards and a bank account as a selectable radio list, and an add-card form with a holographic 3D card preview that mirrors every keystroke, recolours itself for Visa, Mastercard or Amex, and flips to its back the moment the CVC field takes focus — all four transform pieces are Tailwind v4 3D utilities.
## HTML
```html
<section data-tsp05 class="tsp-05 group/pay w-full min-h-svh bg-tsp05-bg px-4 py-10 font-tsp05-sans text-tsp05-ink antialiased sm:px-8 sm:py-14" aria-labelledby="tsp-05-h">
  <div class="mx-auto grid w-full max-w-6xl gap-8">
    <header><h1 id="tsp-05-h" class="text-3xl font-extrabold tracking-tight">Payment methods</h1><p class="mt-1 text-tsp05-mut">Choose how Northwind pays for its subscription.</p></header>
    <div class="grid gap-6 lg:grid-cols-[minmax(0,1fr)_minmax(0,1.1fr)]">
      <div class="grid content-start gap-6">
        <fieldset data-methods class="grid gap-3 rounded-3xl border border-tsp05-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)] sm:p-6">
          <legend class="sr-only">Default payment method</legend>
          <p class="text-sm font-bold">Saved methods</p>
          <label class="group/m flex min-h-11 cursor-pointer items-center gap-4 rounded-2xl border border-tsp05-line p-4 transition hover:border-tsp05-acc/40 has-checked:border-tsp05-acc has-checked:bg-tsp05-acc/5 has-checked:ring-4 has-checked:ring-tsp05-acc/10 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp05-acc"><input type="radio" name="tsp-05-method" class="sr-only" checked><span class="grid h-9 w-13 flex-none place-items-center rounded-lg bg-linear-135 from-blue-600 to-indigo-900 text-[10px] font-extrabold italic tracking-wider text-white">VISA</span><span class="min-w-0 flex-1"><span class="flex items-center gap-2 font-semibold">Visa ending 4242 <span class="rounded-full bg-tsp05-acc/10 px-2 py-0.5 text-[11px] font-bold text-tsp05-acc">Default</span></span><span class="block text-sm text-tsp05-mut">Expires 08 / 28 · Ava Mitchell</span></span><span class="grid size-5 flex-none place-items-center rounded-full border-2 border-tsp05-line group-has-checked/m:border-tsp05-acc group-has-checked/m:bg-tsp05-acc"><span class="size-1.5 rounded-full bg-white opacity-0 group-has-checked/m:opacity-100"></span></span></label>
          <label class="group/m flex min-h-11 cursor-pointer items-center gap-4 rounded-2xl border border-tsp05-line p-4 transition hover:border-tsp05-acc/40 has-checked:border-tsp05-acc has-checked:bg-tsp05-acc/5 has-checked:ring-4 has-checked:ring-tsp05-acc/10 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp05-acc"><input type="radio" name="tsp-05-method" class="sr-only"><span class="grid h-9 w-13 flex-none place-items-center rounded-lg bg-linear-135 from-orange-500 to-rose-800"><span class="flex -space-x-1.5"><span class="size-3.5 rounded-full bg-red-500/90"></span><span class="size-3.5 rounded-full bg-amber-400/90"></span></span></span><span class="min-w-0 flex-1"><span class="flex items-center gap-2 font-semibold">Mastercard ending 8210 <span class="rounded-full bg-amber-100 px-2 py-0.5 text-[11px] font-bold text-amber-700">Expires soon</span></span><span class="block text-sm text-tsp05-mut">Expires 11 / 26 · Finance team</span></span><span class="grid size-5 flex-none place-items-center rounded-full border-2 border-tsp05-line group-has-checked/m:border-tsp05-acc group-has-checked/m:bg-tsp05-acc"><span class="size-1.5 rounded-full bg-white opacity-0 group-has-checked/m:opacity-100"></span></span></label>
          <label class="group/m flex min-h-11 cursor-pointer items-center gap-4 rounded-2xl border border-tsp05-line p-4 transition hover:border-tsp05-acc/40 has-checked:border-tsp05-acc has-checked:bg-tsp05-acc/5 has-checked:ring-4 has-checked:ring-tsp05-acc/10 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp05-acc"><input type="radio" name="tsp-05-method" class="sr-only"><span class="grid h-9 w-13 flex-none place-items-center rounded-lg bg-tsp05-ink text-white"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M3 21h18M5 21V10M19 21V10M9 21v-7M15 21v-7M2 10l10-6 10 6z"/></svg></span><span class="min-w-0 flex-1"><span class="flex items-center gap-2 font-semibold">US bank account ••6789 <span class="rounded-full bg-emerald-50 px-2 py-0.5 text-[11px] font-bold text-emerald-700">Verified</span></span><span class="block text-sm text-tsp05-mut">ACH debit · Chase</span></span><span class="grid size-5 flex-none place-items-center rounded-full border-2 border-tsp05-line group-has-checked/m:border-tsp05-acc group-has-checked/m:bg-tsp05-acc"><span class="size-1.5 rounded-full bg-white opacity-0 group-has-checked/m:opacity-100"></span></span></label>
        </fieldset>
        <div class="grid gap-3 rounded-3xl border border-tsp05-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)] sm:p-6">
          <div class="flex items-center justify-between"><p class="text-sm font-bold">Billing address</p><button type="button" class="min-h-11 rounded-xl px-3 text-sm font-semibold text-tsp05-acc transition hover:bg-tsp05-acc/5 focus-visible:outline-2 focus-visible:outline-tsp05-acc">Edit</button></div>
          <p class="text-sm leading-relaxed text-tsp05-mut">Northwind Co.<br>500 Market Street, Suite 300<br>San Francisco, CA 94105 · United States<br>Tax ID: US 94-1234567</p>
        </div>
      </div>

      <form data-form class="grid content-start gap-6 rounded-3xl border border-tsp05-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)] sm:p-7" aria-labelledby="tsp-05-add">
        <h2 id="tsp-05-add" class="text-sm font-bold">Add a card</h2>
        <div class="perspective-[1400px]" aria-hidden="true">
          <div data-card data-brand="none" class="group/card relative mx-auto aspect-[1.586] w-full max-w-sm transition-transform duration-700 ease-[cubic-bezier(.3,.7,.2,1)] transform-3d group-has-[#tsp-05-cvc:focus]/pay:rotate-y-180 motion-reduce:transition-none">
            <div class="absolute inset-0 grid grid-rows-[auto_1fr_auto] overflow-hidden rounded-2xl bg-linear-135 from-zinc-700 to-zinc-950 p-5 text-white shadow-[0_30px_50px_-20px_rgb(0_0_0/0.5)] backface-hidden transition-colors group-data-[brand=visa]/card:from-blue-600 group-data-[brand=visa]/card:to-indigo-950 group-data-[brand=mastercard]/card:from-orange-500 group-data-[brand=mastercard]/card:to-rose-900 group-data-[brand=amex]/card:from-teal-500 group-data-[brand=amex]/card:to-cyan-950 sm:p-6">
              <span class="pointer-events-none absolute inset-0 bg-[linear-gradient(115deg,transparent_30%,rgb(255_255_255/0.22)_45%,transparent_60%)] mix-blend-overlay"></span>
              <span class="pointer-events-none absolute -right-16 -top-16 size-48 rounded-full bg-white/10 blur-2xl"></span>
              <div class="relative flex items-start justify-between"><span class="h-8 w-11 rounded-md bg-linear-to-br from-amber-100 via-amber-300 to-amber-500 shadow-inner"></span><span data-brand-label class="text-sm font-extrabold italic tracking-wider">CARD</span></div>
              <p data-out-number class="relative self-center font-tsp05-mono text-lg tracking-[0.14em] sm:text-xl">•••• •••• •••• ••••</p>
              <div class="relative flex items-end justify-between gap-4 text-xs"><div class="min-w-0"><p class="text-[10px] uppercase tracking-widest text-white/60">Card holder</p><p data-out-name class="truncate font-semibold uppercase tracking-wide">Your name</p></div><div><p class="text-[10px] uppercase tracking-widest text-white/60">Expires</p><p data-out-exp class="font-tsp05-mono font-medium">MM/YY</p></div></div>
            </div>
            <div class="absolute inset-0 overflow-hidden rounded-2xl bg-linear-135 from-zinc-700 to-zinc-950 text-white shadow-[0_30px_50px_-20px_rgb(0_0_0/0.5)] backface-hidden rotate-y-180 group-data-[brand=visa]/card:from-blue-600 group-data-[brand=visa]/card:to-indigo-950 group-data-[brand=mastercard]/card:from-orange-500 group-data-[brand=mastercard]/card:to-rose-900 group-data-[brand=amex]/card:from-teal-500 group-data-[brand=amex]/card:to-cyan-950">
              <div class="mt-6 h-11 bg-black/80"></div>
              <div class="mx-5 mt-5 flex items-center justify-end rounded-md bg-[repeating-linear-gradient(90deg,#fff_0_6px,#f1f1f1_6px_12px)] px-3 py-2"><span data-out-cvc class="font-tsp05-mono text-sm font-medium italic text-zinc-900">•••</span></div>
              <p class="mx-5 mt-3 text-[10px] leading-snug text-white/60">The 3 or 4 digit security code on the back of your card.</p>
            </div>
          </div>
        </div>
        <div class="grid gap-4 sm:grid-cols-2">
          <label class="grid gap-1.5 sm:col-span-2"><span class="text-sm font-semibold">Card number</span><input name="number" inputmode="numeric" autocomplete="cc-number" placeholder="1234 1234 1234 1234" required minlength="15" class="min-h-11 rounded-xl border border-tsp05-line bg-white px-3.5 font-tsp05-mono text-sm tracking-wider shadow-xs outline-none transition focus:border-tsp05-acc focus:ring-4 focus:ring-tsp05-acc/15 user-invalid:border-rose-500"></label>
          <label class="grid gap-1.5 sm:col-span-2"><span class="text-sm font-semibold">Name on card</span><input name="name" autocomplete="cc-name" placeholder="Ava Mitchell" required class="min-h-11 rounded-xl border border-tsp05-line bg-white px-3.5 text-sm shadow-xs outline-none transition focus:border-tsp05-acc focus:ring-4 focus:ring-tsp05-acc/15 user-invalid:border-rose-500"></label>
          <label class="grid gap-1.5"><span class="text-sm font-semibold">Expiry</span><input name="exp" inputmode="numeric" autocomplete="cc-exp" placeholder="MM / YY" required minlength="5" class="min-h-11 rounded-xl border border-tsp05-line bg-white px-3.5 font-tsp05-mono text-sm shadow-xs outline-none transition focus:border-tsp05-acc focus:ring-4 focus:ring-tsp05-acc/15 user-invalid:border-rose-500"></label>
          <label class="grid gap-1.5"><span class="text-sm font-semibold">CVC</span><input id="tsp-05-cvc" name="cvc" inputmode="numeric" autocomplete="cc-csc" placeholder="123" required minlength="3" maxlength="4" class="min-h-11 rounded-xl border border-tsp05-line bg-white px-3.5 font-tsp05-mono text-sm shadow-xs outline-none transition focus:border-tsp05-acc focus:ring-4 focus:ring-tsp05-acc/15 user-invalid:border-rose-500"></label>
        </div>
        <label class="flex min-h-11 cursor-pointer items-center gap-3 text-sm font-medium"><input type="checkbox" name="default" class="size-4 accent-tsp05-acc">Make this my default payment method</label>
        <div class="flex flex-wrap items-center justify-between gap-3 border-t border-tsp05-line pt-5">
          <p class="flex items-center gap-2 text-xs text-tsp05-mut"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M7 11V7a5 5 0 0 1 10 0v4M5 11h14v10H5z"/></svg>Encrypted and tokenised — we never store your full number.</p>
          <button type="submit" class="inline-flex min-h-11 items-center rounded-xl bg-tsp05-acc px-5 text-sm font-bold text-white shadow-[0_10px_24px_-10px_var(--color-tsp05-acc)] transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp05-acc">Save card</button>
        </div>
        <p data-status role="status" aria-live="polite" class="text-sm font-semibold text-emerald-700 empty:hidden"></p>
      </form>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsp05-bg: #f6f5fa;
  --color-tsp05-bg: oklch(0.973 0.006 297);
  --color-tsp05-ink: #1a1625;
  --color-tsp05-ink: oklch(0.205 0.025 297);
  --color-tsp05-mut: #645e72;
  --color-tsp05-mut: oklch(0.5 0.03 297);
  --color-tsp05-line: #e7e4ef;
  --color-tsp05-line: oklch(0.925 0.012 297);
  --color-tsp05-acc: #7c3aed;
  --color-tsp05-acc: oklch(0.541 0.247 293);
  --font-tsp05-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tsp05-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tsp-05 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('[data-tsp05]');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const form = root.querySelector('[data-form]');
  const card = root.querySelector('[data-card]');
  const out = (k) => root.querySelector('[data-out-' + k + ']');
  const digits = (v) => v.replace(/[^0-9]/g, '');
  const brandOf = (d) => (/^3[47]/.test(d) ? 'amex' : /^4/.test(d) ? 'visa' : /^(5[1-5]|2[2-7])/.test(d) ? 'mastercard' : 'none');
  const labels = { visa: 'VISA', mastercard: 'mastercard', amex: 'AMEX', none: 'CARD' };
  const group = (d, brand) => {
    if (brand === 'amex') return [d.slice(0, 4), d.slice(4, 10), d.slice(10, 15)].filter(Boolean).join(' ');
    return (d.slice(0, 16).match(/.{1,4}/g) || []).join(' ');
  };
  const f = form.elements;
  f.number.addEventListener('input', () => {
    const d = digits(f.number.value);
    const brand = brandOf(d);
    f.number.value = group(d, brand);
    card.dataset.brand = brand;
    root.querySelector('[data-brand-label]').textContent = labels[brand];
    const mask = brand === 'amex' ? '•••• •••••• •••••' : '•••• •••• •••• ••••';
    out('number').textContent = f.number.value + mask.slice(f.number.value.length);
  });
  f.name.addEventListener('input', () => { out('name').textContent = f.name.value || 'Your name'; });
  f.exp.addEventListener('input', (e) => {
    let d = digits(f.exp.value).slice(0, 4);
    if (d.length === 1 && +d > 1) d = '0' + d;
    f.exp.value = d.length > 2 ? d.slice(0, 2) + '/' + d.slice(2) : d + (d.length === 2 && e.inputType !== 'deleteContentBackward' ? '/' : '');
    out('exp').textContent = f.exp.value || 'MM/YY';
  });
  f.cvc.addEventListener('input', () => { f.cvc.value = digits(f.cvc.value).slice(0, 4); out('cvc').textContent = f.cvc.value || '•••'; });
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!form.checkValidity()) { form.reportValidity(); return; }
    const d = digits(f.number.value), brand = card.dataset.brand;
    const list = root.querySelector('[data-methods]');
    const tpl = list.querySelector('label');
    const row = tpl.cloneNode(true);
    const tile = row.querySelector('span');
    tile.className = tile.className.replace(/from-[a-z]+-[0-9]+ to-[a-z]+-[0-9]+/, brand === 'mastercard' ? 'from-orange-500 to-rose-800' : brand === 'amex' ? 'from-teal-500 to-cyan-900' : 'from-blue-600 to-indigo-900');
    tile.textContent = labels[brand] === 'mastercard' ? 'MC' : labels[brand];
    const title = row.querySelector('.font-semibold');
    title.textContent = (brand === 'none' ? 'Card' : brand[0].toUpperCase() + brand.slice(1)) + ' ending ' + d.slice(-4) + ' ';
    if (f.default.checked) { const b = document.createElement('span'); b.className = 'rounded-full bg-tsp05-acc/10 px-2 py-0.5 text-[11px] font-bold text-tsp05-acc'; b.textContent = 'Default'; title.appendChild(b); list.querySelectorAll('.bg-tsp05-acc\\/10').forEach((x) => x.remove()); }
    row.querySelector('.text-sm').textContent = 'Expires ' + f.exp.value.replace('/', ' / ') + ' · ' + f.name.value;
    list.appendChild(row);
    row.querySelector('input').checked = true;
    root.querySelector('[data-status]').textContent = 'Card ending ' + d.slice(-4) + ' saved.';
    form.reset(); card.dataset.brand = 'none';
    out('number').textContent = '•••• •••• •••• ••••'; out('name').textContent = 'Your name'; out('exp').textContent = 'MM/YY'; out('cvc').textContent = '•••';
    root.querySelector('[data-brand-label]').textContent = 'CARD';
  });
})();
```
