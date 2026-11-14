---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-table-currency-switcher/"
title: "Tailwind Pricing Table with Currency Switcher (USD, GBP, EUR, AUD)"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "Regional pricing for global SaaS: a segmented USD / GBP / EUR / AUD control morphs every price on the grid — fade, blur, swap, return — and announces the…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Table with Currency Switcher (USD, GBP, EUR, AUD)
Source: https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-table-currency-switcher/

Regional pricing for global SaaS: a segmented USD / GBP / EUR / AUD control morphs every price on the grid — fade, blur, swap, return — and announces the change once to screen readers. The script only sets a data-swap attribute; group-data-swap/g: utilities own the whole animation, and the JS reads its timing from the utility's computed transition-duration.
## HTML
```html
<section class="tpt-02 w-full min-h-svh grid place-items-center bg-tpt02-bg bg-[radial-gradient(80%_60%_at_50%_0%,var(--color-tpt02-glow),transparent_70%)] px-5 py-16 font-tpt02-sans text-tpt02-ink antialiased" aria-label="Pricing table with currency switcher" data-tpt02-root>
  <div class="grid w-full max-w-5xl justify-items-center gap-9">
    <header class="grid justify-items-center gap-5 text-center">
      <h2 class="text-[clamp(26px,3.8vw,40px)] font-bold tracking-[-0.03em] text-balance">Priced for wherever you build</h2>
      <fieldset class="flex rounded-full bg-tpt02-card p-1 ring-1 ring-white/10">
        <legend class="sr-only">Currency</legend>
        <label class="grid min-h-10 min-w-16 cursor-pointer place-items-center rounded-full px-3 font-tpt02-mono text-[13px] font-semibold text-tpt02-mut transition-colors hover:text-tpt02-ink has-checked:bg-tpt02-acc has-checked:text-tpt02-on-acc has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tpt02-acc"><input class="sr-only" type="radio" name="tpt02-cur" value="USD" checked>USD</label>
        <label class="grid min-h-10 min-w-16 cursor-pointer place-items-center rounded-full px-3 font-tpt02-mono text-[13px] font-semibold text-tpt02-mut transition-colors hover:text-tpt02-ink has-checked:bg-tpt02-acc has-checked:text-tpt02-on-acc has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tpt02-acc"><input class="sr-only" type="radio" name="tpt02-cur" value="GBP">GBP</label>
        <label class="grid min-h-10 min-w-16 cursor-pointer place-items-center rounded-full px-3 font-tpt02-mono text-[13px] font-semibold text-tpt02-mut transition-colors hover:text-tpt02-ink has-checked:bg-tpt02-acc has-checked:text-tpt02-on-acc has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tpt02-acc"><input class="sr-only" type="radio" name="tpt02-cur" value="EUR">EUR</label>
        <label class="grid min-h-10 min-w-16 cursor-pointer place-items-center rounded-full px-3 font-tpt02-mono text-[13px] font-semibold text-tpt02-mut transition-colors hover:text-tpt02-ink has-checked:bg-tpt02-acc has-checked:text-tpt02-on-acc has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tpt02-acc"><input class="sr-only" type="radio" name="tpt02-cur" value="AUD">AUD</label>
      </fieldset>
    </header>
    <div class="group/g grid w-full gap-5 md:grid-cols-3" data-grid>
      <article class="flex flex-col rounded-2xl bg-tpt02-card p-7 ring-1 ring-white/8">
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt02-mut uppercase">Hobby</h3>
        <p data-amount data-usd="9" class="mt-3 h-[52px] text-[46px] leading-[52px] font-bold tracking-[-0.035em] tabular-nums transition duration-280 group-data-swap/g:translate-y-1.5 group-data-swap/g:opacity-0 group-data-swap/g:blur-[2px] motion-reduce:duration-0">$9</p>
        <span class="mt-1 text-[13px] text-tpt02-mut">per month</span>
        <ul class="mt-6 grid flex-1 content-start gap-2.5 text-sm text-tpt02-body *:flex *:gap-2.5 *:before:text-tpt02-acc *:before:content-['—']"><li>1 site</li><li>10k monthly visits</li><li>SSL &amp; CDN</li></ul>
        <a href="#" class="mt-7 grid min-h-11 place-items-center rounded-xl text-sm font-semibold text-tpt02-ink no-underline ring-1 ring-white/15 transition hover:ring-tpt02-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpt02-acc">Get Hobby</a>
      </article>
      <article class="relative flex flex-col rounded-2xl bg-tpt02-card-hi p-7 ring-1 ring-tpt02-acc/70 shadow-[0_30px_60px_-30px_var(--color-tpt02-acc)]">
        <span aria-hidden="true" class="pointer-events-none absolute inset-x-10 -top-px h-px bg-linear-to-r from-transparent via-tpt02-acc to-transparent"></span>
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt02-acc uppercase">Studio</h3>
        <p data-amount data-usd="24" class="mt-3 h-[52px] text-[46px] leading-[52px] font-bold tracking-[-0.035em] tabular-nums transition duration-280 group-data-swap/g:translate-y-1.5 group-data-swap/g:opacity-0 group-data-swap/g:blur-[2px] motion-reduce:duration-0">$24</p>
        <span class="mt-1 text-[13px] text-tpt02-mut">per month</span>
        <ul class="mt-6 grid flex-1 content-start gap-2.5 text-sm text-tpt02-body *:flex *:gap-2.5 *:before:text-tpt02-acc *:before:content-['—']"><li>10 sites</li><li>500k monthly visits</li><li>Privacy-first analytics</li><li>Form handling</li></ul>
        <a href="#" class="mt-7 grid min-h-11 place-items-center rounded-xl bg-tpt02-acc text-sm font-semibold text-tpt02-on-acc no-underline transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpt02-acc">Get Studio</a>
      </article>
      <article class="flex flex-col rounded-2xl bg-tpt02-card p-7 ring-1 ring-white/8">
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt02-mut uppercase">Agency</h3>
        <p data-amount data-usd="69" class="mt-3 h-[52px] text-[46px] leading-[52px] font-bold tracking-[-0.035em] tabular-nums transition duration-280 group-data-swap/g:translate-y-1.5 group-data-swap/g:opacity-0 group-data-swap/g:blur-[2px] motion-reduce:duration-0">$69</p>
        <span class="mt-1 text-[13px] text-tpt02-mut">per month</span>
        <ul class="mt-6 grid flex-1 content-start gap-2.5 text-sm text-tpt02-body *:flex *:gap-2.5 *:before:text-tpt02-acc *:before:content-['—']"><li>Unlimited sites</li><li>5M monthly visits</li><li>White-label dashboards</li></ul>
        <a href="#" class="mt-7 grid min-h-11 place-items-center rounded-xl text-sm font-semibold text-tpt02-ink no-underline ring-1 ring-white/15 transition hover:ring-tpt02-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpt02-acc">Get Agency</a>
      </article>
    </div>
    <p data-tax class="text-[13px] text-tpt02-mut">Prices in USD, excl. sales tax. Cancel anytime.</p>
    <p role="status" aria-live="polite" class="sr-only" data-status></p>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tpt02-mono text-[11.5px] text-tpt02-mut ring-1 ring-white/10">data-swap · group-data-swap/g: · has-checked: segmented radios</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt02-bg: #0c1019;
  --color-tpt02-bg: oklch(0.16 0.02 260);
  --color-tpt02-glow: #10324080;
  --color-tpt02-glow: oklch(0.3 0.06 215 / 0.5);
  --color-tpt02-card: #161c29;
  --color-tpt02-card: oklch(0.22 0.025 260);
  --color-tpt02-card-hi: #1a2231;
  --color-tpt02-card-hi: oklch(0.245 0.03 250);
  --color-tpt02-ink: #eef1f8;
  --color-tpt02-ink: oklch(0.96 0.008 260);
  --color-tpt02-body: #c3c9d8;
  --color-tpt02-body: oklch(0.84 0.02 260);
  --color-tpt02-mut: #9ea6bb;
  --color-tpt02-mut: oklch(0.73 0.025 260);
  --color-tpt02-acc: #2ec4d6;
  --color-tpt02-acc: oklch(0.75 0.13 205);
  --color-tpt02-on-acc: #06151a;
  --color-tpt02-on-acc: oklch(0.18 0.03 210);
  --font-tpt02-sans: 'Geist', system-ui, sans-serif;
  --font-tpt02-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-02 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-tpt02-root]').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const grid = root.querySelector('[data-grid]');
    const amounts = [...grid.querySelectorAll('[data-amount]')];
    const tax = root.querySelector('[data-tax]');
    const status = root.querySelector('[data-status]');
    const RATES = {
      USD: { r: 1, tax: 'excl. sales tax' },
      GBP: { r: 0.78, tax: 'excl. VAT' },
      EUR: { r: 0.92, tax: 'excl. VAT' },
      AUD: { r: 1.5, tax: 'excl. GST' },
    };
    const fmt = (v, cur) => new Intl.NumberFormat('en', { style: 'currency', currency: cur, maximumFractionDigits: 0 }).format(v);
    const dur = () => parseFloat(getComputedStyle(amounts[0]).transitionDuration) * 1000 || 0;
    let t = 0;
    root.querySelectorAll('input[name="tpt02-cur"]').forEach((input) => {
      input.addEventListener('change', () => {
        const cur = input.value;
        const { r } = RATES[cur];
        clearTimeout(t);
        grid.setAttribute('data-swap', '');
        t = setTimeout(() => {
          amounts.forEach((el) => { el.textContent = fmt(Math.round(el.dataset.usd * r), cur); });
          tax.textContent = 'Prices in ' + cur + ', ' + RATES[cur].tax + '. Cancel anytime.';
          status.textContent = 'Prices now shown in ' + cur;
          grid.removeAttribute('data-swap');
        }, dur());
      });
    });
  });
})();
```
