---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-payment-checkout-modal-3d-paper-fold/"
title: "Tailwind Payment Checkout Modal with 3D Paper Fold Entrance"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A card-entry checkout that unfolds from the top like an envelope — rotate-x-[-70deg] to flat, ease-out, no overshoot, because payment wants precision rather…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Payment Checkout Modal with 3D Paper Fold Entrance
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-payment-checkout-modal-3d-paper-fold/

A card-entry checkout that unfolds from the top like an envelope — rotate-x-[-70deg] to flat, ease-out, no overshoot, because payment wants precision rather than bounce. The port states the fold as open:starting: on the dialog inside a perspective-* stage and keeps the original's abandonment guard on Esc.
## HTML
```html
<section class="tw-04 w-full min-h-svh grid place-items-center bg-tw04-bg font-tw04-sans px-6 py-10">
  <button type="button" data-tw04-open class="inline-flex items-center justify-center min-h-11 px-7 rounded-lg border-0 text-[15px] font-bold text-white bg-tw04-brand tabular-nums shadow-[0_8px_20px_-6px_var(--color-tw04-glow)] cursor-pointer transition-[background-color,translate] duration-200 hover:bg-tw04-brandhover hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tw04-brand focus-visible:outline-offset-2 motion-reduce:hover:translate-y-0">Complete purchase · $29.00</button>

  <dialog id="tw-04-dlg" aria-labelledby="tw-04-title" class="m-auto w-[min(460px,94vw)] p-0 border-0 bg-transparent perspective-[1600px] open:backdrop:bg-tw04-scrim open:backdrop:backdrop-blur-[6px]">
    <div class="relative px-8 pt-8 pb-6 rounded-xl bg-tw04-card text-tw04-ink text-left shadow-[0_40px_60px_-20px_#0a0e2759] origin-top transform-3d backface-hidden opacity-0 rotate-x-[-70deg] transition-[opacity,rotate,overlay,display] duration-500 ease-[cubic-bezier(.22,1,.36,1)] transition-discrete group-open:opacity-100 in-[dialog[open]]:opacity-100 in-[dialog[open]]:rotate-x-0 starting:in-[dialog[open]]:opacity-0 starting:in-[dialog[open]]:rotate-x-[-70deg] motion-reduce:transition-[opacity] motion-reduce:duration-150 motion-reduce:rotate-x-0">
      <button type="button" data-tw04-close aria-label="Close dialog" class="absolute top-3.5 right-3.5 grid place-items-center size-9 rounded-lg border-0 bg-transparent text-tw04-sub text-base cursor-pointer transition-colors duration-200 hover:bg-tw04-well hover:text-tw04-ink focus-visible:outline-2 focus-visible:outline-tw04-brand focus-visible:outline-offset-2">&#10005;</button>

      <p class="inline-flex items-center gap-2 mb-3.5 text-xs font-semibold tracking-wide text-tw04-sub"><span aria-hidden="true" class="text-xs">&#128274;</span>Secured by Stripe</p>
      <h2 id="tw-04-title" class="mb-[18px] text-[1.45rem] font-extrabold tracking-[-0.015em] leading-tight">Complete your purchase</h2>

      <div class="mb-5 px-[18px] py-4 rounded-[9px] border border-tw04-line bg-tw04-well">
        <div class="flex justify-between items-baseline py-[5px] text-sm text-tw04-sub"><span>Pro plan · monthly</span><strong class="font-semibold text-tw04-ink tabular-nums">$25.00</strong></div>
        <div class="flex justify-between items-baseline py-[5px] text-sm text-tw04-sub"><span>Tax (16%)</span><strong class="font-semibold text-tw04-ink tabular-nums">$4.00</strong></div>
        <div class="flex justify-between items-baseline pt-2.5 mt-[5px] border-t border-tw04-line text-[15px]"><span class="font-bold text-tw04-ink">Total</span><strong class="text-base font-extrabold text-tw04-ink tabular-nums">$29.00 USD</strong></div>
      </div>

      <form method="dialog" class="flex flex-col gap-3 mb-[18px]">
        <label class="flex flex-col gap-1.5">
          <span class="text-xs font-semibold tracking-wide text-tw04-sub">Card number</span>
          <input type="text" autofocus required inputmode="numeric" autocomplete="cc-number" placeholder="1234 1234 1234 1234" class="min-h-11 px-3.5 rounded-lg border border-tw04-line bg-tw04-card text-[15px] text-tw04-ink tabular-nums placeholder:text-tw04-sub transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tw04-brand focus:shadow-[0_0_0_3px_var(--color-tw04-ring)]">
        </label>
        <div class="grid grid-cols-2 gap-2.5 max-[400px]:grid-cols-1">
          <label class="flex flex-col gap-1.5">
            <span class="text-xs font-semibold tracking-wide text-tw04-sub">Expiry</span>
            <input type="text" required inputmode="numeric" autocomplete="cc-exp" placeholder="MM / YY" class="min-h-11 px-3.5 rounded-lg border border-tw04-line bg-tw04-card text-[15px] text-tw04-ink tabular-nums placeholder:text-tw04-sub transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tw04-brand focus:shadow-[0_0_0_3px_var(--color-tw04-ring)]">
          </label>
          <label class="flex flex-col gap-1.5">
            <span class="text-xs font-semibold tracking-wide text-tw04-sub">CVC</span>
            <input type="text" required inputmode="numeric" pattern="[0-9]{3,4}" autocomplete="cc-csc" placeholder="CVC" class="min-h-11 px-3.5 rounded-lg border border-tw04-line bg-tw04-card text-[15px] text-tw04-ink tabular-nums placeholder:text-tw04-sub transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tw04-brand focus:shadow-[0_0_0_3px_var(--color-tw04-ring)]">
          </label>
        </div>
        <div class="grid grid-cols-[1fr_auto] gap-2.5 max-[400px]:grid-cols-1">
          <label class="flex flex-col gap-1.5">
            <span class="text-xs font-semibold tracking-wide text-tw04-sub">Cardholder name</span>
            <input type="text" required autocomplete="cc-name" placeholder="Alex Chen" class="min-h-11 px-3.5 rounded-lg border border-tw04-line bg-tw04-card text-[15px] text-tw04-ink placeholder:text-tw04-sub transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tw04-brand focus:shadow-[0_0_0_3px_var(--color-tw04-ring)]">
          </label>
          <label class="flex flex-col gap-1.5">
            <span class="text-xs font-semibold tracking-wide text-tw04-sub">ZIP</span>
            <input type="text" required autocomplete="postal-code" placeholder="94103" class="min-h-11 w-[7rem] max-[400px]:w-full px-3.5 rounded-lg border border-tw04-line bg-tw04-card text-[15px] text-tw04-ink tabular-nums placeholder:text-tw04-sub transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tw04-brand focus:shadow-[0_0_0_3px_var(--color-tw04-ring)]">
          </label>
        </div>
        <button type="submit" class="min-h-11 mt-1.5 px-5 rounded-lg border-0 bg-tw04-brand text-base font-bold text-white tabular-nums cursor-pointer transition-[background-color,translate] duration-200 hover:bg-tw04-brandhover active:translate-y-px focus-visible:outline-2 focus-visible:outline-tw04-brand focus-visible:outline-offset-[3px] motion-reduce:active:translate-y-0">Pay $29.00</button>
      </form>

      <div class="pt-4 text-center border-t border-tw04-line">
        <span aria-hidden="true" class="block mb-1.5 font-tw04-mono text-xs font-bold tracking-[0.14em] text-tw04-sub">VISA · MC · AMEX · DISC</span>
        <p class="text-xs text-tw04-sub">You'll be charged $29.00 today. Cancel anytime.</p>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tw04-bg: #f7f8fa;
  --color-tw04-bg: oklch(0.98 0.003 255);
  --color-tw04-card: #ffffff;
  --color-tw04-card: oklch(1 0 0);
  --color-tw04-well: #fafbfc;
  --color-tw04-well: oklch(0.98 0.003 255);
  --color-tw04-ink: #0a0e27;
  --color-tw04-ink: oklch(0.19 0.05 275);
  --color-tw04-sub: #697386;
  --color-tw04-sub: oklch(0.56 0.02 265);
  --color-tw04-line: #e6e8ec;
  --color-tw04-line: oklch(0.92 0.004 265);
  --color-tw04-brand: #635bff;
  --color-tw04-brand: oklch(0.55 0.22 277);
  --color-tw04-brandhover: #4f46e5;
  --color-tw04-brandhover: oklch(0.5 0.22 277);
  --color-tw04-ring: #635bff2e;
  --color-tw04-ring: oklch(0.55 0.22 277 / 0.18);
  --color-tw04-glow: #635bff80;
  --color-tw04-glow: oklch(0.55 0.22 277 / 0.5);
  --color-tw04-scrim: #0a0e278c;
  --color-tw04-scrim: oklch(0.19 0.05 275 / 0.55);
  --font-tw04-sans: 'Outfit', system-ui, sans-serif;
  --font-tw04-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tw-04 {
  width: 100%;
}

#tw-04-dlg::backdrop {
  background: oklch(0.19 0.05 275 / 0);
  backdrop-filter: blur(0px);
  transition: background .25s ease, backdrop-filter .25s ease, overlay .25s allow-discrete, display .25s allow-discrete;
}

@starting-style {
  #tw-04-dlg[open]::backdrop {
    background: oklch(0.19 0.05 275 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tw-04-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tw-04');
  var dlg = root.querySelector('#tw-04-dlg');
  var card = dlg.firstElementChild;
  root.querySelector('[data-tw04-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelector('[data-tw04-close]').addEventListener('click', function () { dlg.close(); });
  // Abandonment guard: Esc fires 'cancel', which is preventable. Ask before discarding.
  dlg.addEventListener('cancel', function (e) {
    var dirty = Array.prototype.some.call(dlg.querySelectorAll('input'), function (i) { return i.value.length > 0; });
    if (dirty && !confirm('You have unsaved payment info. Leave anyway?')) e.preventDefault();
  });
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
