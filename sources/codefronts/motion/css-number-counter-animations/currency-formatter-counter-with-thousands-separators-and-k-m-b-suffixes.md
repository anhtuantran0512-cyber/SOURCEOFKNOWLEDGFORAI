---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/currency-formatter-counter-with-thousands-separators-and-k-m-b-suffixes/"
title: "Currency Formatter Counter with Thousands Separators & K/M/B Suffixes"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "Formatting is where most counters fall apart."
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Currency Formatter Counter with Thousands Separators & K/M/B Suffixes
Source: https://codefronts.com/motion/css-number-counter-animations/currency-formatter-counter-with-thousands-separators-and-k-m-b-suffixes/

Formatting is where most counters fall apart. This one wraps the tween in Intl.NumberFormat, so the same code renders $1,284,930 in en-US, 1.284.930 $ in de-DE, ₹12,84,930 in the Indian lakh grouping, and a compact $1.28M — correct separators, correct currency placement, correct decimals — while the digits still animate smoothly. Switch locale, currency and notation live.
## HTML
```html
<section class="cnc-09" aria-label="Currency formatter counter demo">
  <div class="cnc-09__stage">
    <article class="cnc-09__card">
      <p class="cnc-09__label">Gross merchandise volume</p>
      <p class="cnc-09__value"><span class="cnc-09__num">0</span></p>
      <p class="cnc-09__meta"><span class="cnc-09__exact"></span> · rolling 30 days</p>
      <div class="cnc-09__rows">
        <div class="cnc-09__row">
          <span class="cnc-09__rowlabel">Locale</span>
          <div class="cnc-09__seg" role="group" aria-label="Locale">
            <button class="cnc-09__opt" type="button" data-locale="en-US" aria-pressed="true">en-US</button>
            <button class="cnc-09__opt" type="button" data-locale="de-DE" aria-pressed="false">de-DE</button>
            <button class="cnc-09__opt" type="button" data-locale="en-IN" aria-pressed="false">en-IN</button>
            <button class="cnc-09__opt" type="button" data-locale="ja-JP" aria-pressed="false">ja-JP</button>
          </div>
        </div>
        <div class="cnc-09__row">
          <span class="cnc-09__rowlabel">Currency</span>
          <div class="cnc-09__seg" role="group" aria-label="Currency">
            <button class="cnc-09__opt" type="button" data-cur="USD" aria-pressed="true">USD</button>
            <button class="cnc-09__opt" type="button" data-cur="EUR" aria-pressed="false">EUR</button>
            <button class="cnc-09__opt" type="button" data-cur="GBP" aria-pressed="false">GBP</button>
            <button class="cnc-09__opt" type="button" data-cur="INR" aria-pressed="false">INR</button>
          </div>
        </div>
        <div class="cnc-09__row">
          <span class="cnc-09__rowlabel">Notation</span>
          <div class="cnc-09__seg" role="group" aria-label="Notation">
            <button class="cnc-09__opt" type="button" data-note="standard" aria-pressed="true">1,284,930</button>
            <button class="cnc-09__opt" type="button" data-note="compact" aria-pressed="false">1.3M</button>
          </div>
        </div>
      </div>
      <button class="cnc-09__replay" type="button">Replay count</button>
    </article>
    <p class="cnc-09__chip" aria-hidden="true">Intl.NumberFormat · hoisted formatters · compact notation · tabular-nums reserve</p>
  </div>
</section>
```
## CSS
```css
.cnc-09,
.cnc-09 *,
.cnc-09 *::before,
.cnc-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-09-bg: oklch(0.97 0.005 250);
  --cnc-09-card: oklch(1 0 0);
  --cnc-09-ink: oklch(0.21 0.02 265);
  --cnc-09-mut: oklch(0.55 0.02 265);
  --cnc-09-acc: oklch(0.52 0.16 245);
  background: var(--cnc-09-bg);
  color: var(--cnc-09-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-09__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(18px,4vw,48px);
}

.cnc-09__card {
  width: min(100%,520px);
  padding: clamp(22px,4vw,32px);
  border-radius: 22px;
  background: var(--cnc-09-card);
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 26px 62px oklch(0.4 0.03 265/.14);
}

.cnc-09__label {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--cnc-09-mut);
}

.cnc-09__value {
  margin-top: 12px;
  font-size: clamp(34px,6.6vw,52px);
  font-weight: 740;
  letter-spacing: -.05em;
  line-height: 1.05;
  color: var(--cnc-09-acc);
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-09__num {
  display: inline-block;
  min-width: 9ch;
}

.cnc-09__meta {
  margin-top: 10px;
  font-size: 12.5px;
  color: var(--cnc-09-mut);
  font-variant-numeric: tabular-nums;
}

.cnc-09__rows {
  display: grid;
  gap: 12px;
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid oklch(0 0 0/.08);
}

.cnc-09__row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}

.cnc-09__rowlabel {
  font-size: 12.5px;
  font-weight: 640;
  color: var(--cnc-09-mut);
}

.cnc-09__seg {
  display: flex;
  gap: 4px;
  padding: 4px;
  border-radius: 12px;
  background: oklch(0 0 0/.05);
}

.cnc-09__opt {
  min-height: 34px;
  padding: 0 11px;
  border: 0;
  border-radius: 9px;
  background: transparent;
  color: var(--cnc-09-mut);
  font: inherit;
  font-size: 12.5px;
  font-weight: 640;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  transition: background .2s,color .2s;
}

.cnc-09__opt:hover {
  color: var(--cnc-09-ink);
}

.cnc-09__opt[aria-pressed="true"] {
  background: var(--cnc-09-card);
  color: var(--cnc-09-ink);
  box-shadow: 0 1px 3px oklch(0 0 0/.14);
}

.cnc-09__opt:focus-visible {
  outline: 3px solid var(--cnc-09-acc);
  outline-offset: 2px;
}

.cnc-09__replay {
  width: 100%;
  min-height: 46px;
  margin-top: 20px;
  border: 0;
  border-radius: 12px;
  background: var(--cnc-09-ink);
  color: oklch(0.99 0 0);
  font: inherit;
  font-size: 14px;
  font-weight: 660;
  cursor: pointer;
  transition: transform .2s,background .2s;
}

.cnc-09__replay:hover {
  background: var(--cnc-09-acc);
  transform: translateY(-1px);
}

.cnc-09__replay:focus-visible {
  outline: 3px solid var(--cnc-09-acc);
  outline-offset: 3px;
}

.cnc-09__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-09-mut);
  padding: 7px 14px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,520px);
}

@media (max-width: 460px) {
  .cnc-09__seg {
    width: 100%;
  }

  .cnc-09__opt {
    flex: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cnc-09__replay {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.cnc-09__card').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    const numEl = card.querySelector('.cnc-09__num');
    const exactEl = card.querySelector('.cnc-09__exact');
    const TARGET = 1284930;
    let locale = 'en-US', currency = 'USD', notation = 'standard', fmt, exactFmt;

    const build = () => {                                   // rebuilt only on settings change
      const opts = { style: 'currency', currency, maximumFractionDigits: notation === 'compact' ? 1 : 0 };
      if (notation === 'compact') { opts.notation = 'compact'; opts.compactDisplay = 'short'; }
      try { fmt = new Intl.NumberFormat(locale, opts); }
      catch (e) { fmt = new Intl.NumberFormat(locale, { style: 'currency', currency }); }
      exactFmt = new Intl.NumberFormat(locale, { style: 'currency', currency, maximumFractionDigits: 2 });
      exactEl.textContent = 'exact ' + exactFmt.format(TARGET);
    };

    const run = () => {
      build();
      if (reduce) { numEl.textContent = fmt.format(TARGET); return; }
      const t0 = performance.now(), ms = 1800;
      const frame = (t) => {
        const p = Math.min(1, (t - t0) / ms);
        const v = p === 1 ? TARGET : Math.round(TARGET * (1 - Math.pow(1 - p, 4)));
        numEl.textContent = fmt.format(v);                  // format for display only
        if (p < 1) requestAnimationFrame(frame);
      };
      requestAnimationFrame(frame);
    };

    card.querySelectorAll('.cnc-09__opt').forEach((btn) => {
      btn.addEventListener('click', () => {
        [...btn.parentElement.children].forEach((b) => b.setAttribute('aria-pressed', String(b === btn)));
        if (btn.dataset.locale) locale = btn.dataset.locale;
        if (btn.dataset.cur) currency = btn.dataset.cur;
        if (btn.dataset.note) notation = btn.dataset.note;
        build();
        numEl.textContent = fmt.format(TARGET);
      });
    });
    card.querySelector('.cnc-09__replay').addEventListener('click', run);
    run();
  });
})();
```
