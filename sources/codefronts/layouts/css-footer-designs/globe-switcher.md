---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/globe-switcher/"
title: "Multi-Language Footer with Currency Selector"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "The footer control international shoppers look for first: a language switcher and a currency selector that actually reformat a sample price using…"
has_js: "true"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Language Footer with Currency Selector
Source: https://codefronts.com/layouts/css-footer-designs/globe-switcher/

The footer control international shoppers look for first: a language switcher and a currency selector that actually reformat a sample price using Intl.NumberFormat — including the placement, separators and symbol conventions each locale expects. Native selects, correct lang and hreflang attributes, RTL-safe layout.
## HTML
```html
<section class="ft-24" aria-label="Multi-language and currency selector footer demo">
  <main class="ft-24__main">
    <p class="ft-24__eyebrow">Intl.NumberFormat · hreflang · logical properties</p>
    <h1 class="ft-24__title">Sell in 14 markets without lying about the price</h1>
    <p class="ft-24__sub">Change the language or the currency below — the sample price reformats using real locale data: symbol placement, separators and decimal rules included.</p>
  </main>
  <footer class="ft-24__foot">
    <section class="ft-24__region" aria-labelledby="ft-24-rh">
      <h2 class="ft-24__h" id="ft-24-rh">Region &amp; currency</h2>
      <div class="ft-24__controls">
        <div class="ft-24__ctl">
          <label class="ft-24__label" for="ft-24-lang">Language</label>
          <div class="ft-24__selwrap">
            <select class="ft-24__select" id="ft-24-lang">
              <optgroup label="Europe">
                <option value="en-GB" lang="en">English (UK)</option>
                <option value="de-DE" lang="de">Deutsch</option>
                <option value="fr-FR" lang="fr">Français</option>
                <option value="es-ES" lang="es">Español</option>
                <option value="nl-NL" lang="nl">Nederlands</option>
                <option value="pl-PL" lang="pl">Polski</option>
              </optgroup>
              <optgroup label="Americas">
                <option value="en-US" lang="en" selected>English (US)</option>
                <option value="pt-BR" lang="pt">Português (Brasil)</option>
                <option value="fr-CA" lang="fr">Français (Canada)</option>
              </optgroup>
              <optgroup label="Asia &amp; Pacific">
                <option value="ja-JP" lang="ja">日本語</option>
                <option value="ko-KR" lang="ko">한국어</option>
                <option value="en-AU" lang="en">English (Australia)</option>
              </optgroup>
              <optgroup label="Middle East">
                <option value="ar-AE" lang="ar">العربية</option>
                <option value="he-IL" lang="he">עברית</option>
              </optgroup>
            </select>
            <span class="ft-24__chev" aria-hidden="true"></span>
          </div>
        </div>
        <div class="ft-24__ctl">
          <label class="ft-24__label" for="ft-24-cur">Currency</label>
          <div class="ft-24__selwrap">
            <select class="ft-24__select" id="ft-24-cur">
              <option value="USD" selected>USD — US dollar</option>
              <option value="EUR">EUR — Euro</option>
              <option value="GBP">GBP — Pound sterling</option>
              <option value="CAD">CAD — Canadian dollar</option>
              <option value="AUD">AUD — Australian dollar</option>
              <option value="JPY">JPY — Japanese yen</option>
              <option value="BRL">BRL — Brazilian real</option>
              <option value="AED">AED — UAE dirham</option>
            </select>
            <span class="ft-24__chev" aria-hidden="true"></span>
          </div>
        </div>
        <div class="ft-24__preview">
          <p class="ft-24__plabel">Sample price</p>
          <p class="ft-24__price" id="ft-24-price">$1,284.50</p>
          <p class="ft-24__pnote" id="ft-24-note" role="status" aria-live="polite">Formatted for English (US)</p>
        </div>
      </div>
      <p class="ft-24__disclosure">Prices convert at the ECB reference rate plus 0.4%, updated daily at 16:00 CET. Import duties for non-EU destinations are shown at checkout, never after delivery.</p>
    </section>
    <div class="ft-24__cols">
      <div class="ft-24__brandcol">
        <div class="ft-24__brand"><span class="ft-24__mark" aria-hidden="true"></span>Meridiem</div>
        <p class="ft-24__blurb">Ships from Rotterdam, Newark and Osaka. 14 storefronts, one catalogue.</p>
        <ul class="ft-24__hreflang"><li><a class="ft-24__hl" href="#ft-24-a" hreflang="de-DE" lang="de">Deutschland</a></li><li><a class="ft-24__hl" href="#ft-24-a" hreflang="ja-JP" lang="ja">日本</a></li><li><a class="ft-24__hl" href="#ft-24-a" hreflang="fr-FR" lang="fr">France</a></li><li><a class="ft-24__hl" href="#ft-24-a" hreflang="x-default">All regions</a></li></ul>
      </div>
      <nav class="ft-24__col" aria-labelledby="ft-24-c1"><h2 class="ft-24__ch" id="ft-24-c1">Shop</h2><ul class="ft-24__list"><li><a class="ft-24__link" href="#ft-24-a">New arrivals</a></li><li><a class="ft-24__link" href="#ft-24-a">Best sellers</a></li><li><a class="ft-24__link" href="#ft-24-a">Gift cards</a></li></ul></nav>
      <nav class="ft-24__col" aria-labelledby="ft-24-c2"><h2 class="ft-24__ch" id="ft-24-c2">Orders</h2><ul class="ft-24__list"><li><a class="ft-24__link" href="#ft-24-a">Shipping &amp; duties</a></li><li><a class="ft-24__link" href="#ft-24-a">Track an order</a></li><li><a class="ft-24__link" href="#ft-24-a">Returns</a></li><li><a class="ft-24__link" href="#ft-24-a">Customs FAQ</a></li></ul></nav>
      <nav class="ft-24__col" aria-labelledby="ft-24-c3"><h2 class="ft-24__ch" id="ft-24-c3">Company</h2><ul class="ft-24__list"><li><a class="ft-24__link" href="#ft-24-a">About</a></li><li><a class="ft-24__link" href="#ft-24-a">Stockists</a></li><li><a class="ft-24__link" href="#ft-24-a">Contact</a></li></ul></nav>
    </div>
    <p class="ft-24__copy">© <time datetime="2026">2026</time> Meridiem Trading B.V. · VAT NL 8221.44.109.B01 · EORI NL822144109</p>
  </footer>
</section>
```
## CSS
```css
.ft-24 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-24-bg);
  --ft-24-bg: oklch(0.97 0.006 265);
  --ft-24-foot: oklch(0.18 0.024 265);
  --ft-24-ink: oklch(0.21 0.028 265);
  --ft-24-mut: oklch(0.53 0.02 265);
  --ft-24-fink: oklch(0.97 0.006 265);
  --ft-24-fmut: oklch(0.74 0.015 265);
  --ft-24-acc: oklch(0.76 0.15 85);
  --ft-24-line: oklch(0.97 0.006 265/.15);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-24-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-24 *,
.ft-24 *::before,
.ft-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-24 ul {
  list-style: none;
}

.ft-24__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(36px,7vh,80px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1160px)/2));
}

.ft-24__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: oklch(0.55 0.14 75);
}

.ft-24__title {
  font-size: clamp(28px,5vw,54px);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 17ch;
  text-wrap: balance;
}

.ft-24__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-24-mut);
  max-width: 58ch;
  text-wrap: pretty;
}

.ft-24__foot {
  background: var(--ft-24-foot);
  color: var(--ft-24-fink);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1160px)/2));
}

.ft-24__region {
  display: grid;
  gap: 14px;
  padding-block: clamp(28px,4vw,46px);
}

.ft-24__h {
  font-size: clamp(17px,2vw,21px);
  font-weight: 690;
  letter-spacing: -.025em;
}

.ft-24__controls {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(14rem,100%),1fr));
  gap: 14px;
  align-items: end;
}

.ft-24__ctl {
  display: grid;
  gap: 6px;
  min-width: 0;
}

.ft-24__label {
  font-size: 12px;
  font-weight: 640;
  letter-spacing: .03em;
  color: var(--ft-24-fmut);
}

.ft-24__selwrap {
  position: relative;
}

.ft-24__select {
  width: 100%;
  min-height: 50px;
  padding-inline: 15px 42px;
  border-radius: 13px;
  border: 1px solid var(--ft-24-line);
  background: oklch(0.97 0.006 265/.06);
  color: var(--ft-24-fink);
  font: inherit;
  font-size: 15px;
  appearance: none;
  -webkit-appearance: none;
  cursor: pointer;
  transition: border-color .2s ease,background .2s ease;
}

.ft-24__select:hover {
  background: oklch(0.97 0.006 265/.11);
}

.ft-24__select:focus-visible {
  outline: 2px solid var(--ft-24-acc);
  outline-offset: 2px;
  border-color: var(--ft-24-acc);
}

.ft-24__select option,
.ft-24__select optgroup {
  color: oklch(0.21 0.028 265);
  background: oklch(1 0 0);
}

.ft-24__chev {
  position: absolute;
  inset-inline-end: 16px;
  top: 50%;
  width: 9px;
  height: 9px;
  translate: 0 -70%;
  rotate: 45deg;
  border-inline-end: 1.8px solid var(--ft-24-fmut);
  border-block-end: 1.8px solid var(--ft-24-fmut);
  pointer-events: none;
}

.ft-24__preview {
  display: grid;
  gap: 2px;
  padding: 12px 16px;
  border-radius: 14px;
  background: color-mix(in oklch,var(--ft-24-acc) 12%,transparent);
  border: 1px solid color-mix(in oklch,var(--ft-24-acc) 30%,transparent);
}

.ft-24__plabel {
  font-size: 11.5px;
  font-weight: 650;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--ft-24-acc);
}

.ft-24__price {
  font-size: clamp(22px,2.6vw,28px);
  font-weight: 720;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.ft-24__pnote {
  font-size: 12.2px;
  color: var(--ft-24-fmut);
}

.ft-24__disclosure {
  font-size: 12.4px;
  line-height: 1.6;
  color: var(--ft-24-fmut);
  max-width: 76ch;
  text-wrap: pretty;
}

.ft-24__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(11rem,1fr));
  gap: clamp(22px,3vw,36px) clamp(16px,2.2vw,28px);
  padding-block: clamp(26px,3.6vw,42px);
  border-top: 1px solid var(--ft-24-line);
}

.ft-24__brandcol {
  display: grid;
  align-content: start;
  gap: 11px;
  min-width: 0;
}

.ft-24__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 17px;
  font-weight: 700;
  letter-spacing: -.025em;
}

.ft-24__mark {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: conic-gradient(from 200deg,var(--ft-24-acc),oklch(0.6 0.16 25),var(--ft-24-acc));
}

.ft-24__blurb {
  font-size: 14px;
  line-height: 1.55;
  color: var(--ft-24-fmut);
  max-width: 32ch;
}

.ft-24__hreflang {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.ft-24__hl {
  display: inline-flex;
  align-items: center;
  min-height: 34px;
  padding: 0 12px;
  border-radius: 99px;
  border: 1px solid var(--ft-24-line);
  font-size: 12.6px;
  color: var(--ft-24-fmut);
  text-decoration: none;
  transition: color .18s ease,border-color .18s ease,background .18s ease;
}

.ft-24__hl:hover {
  color: var(--ft-24-fink);
  border-color: var(--ft-24-acc);
  background: color-mix(in oklch,var(--ft-24-acc) 12%,transparent);
}

.ft-24__col {
  display: grid;
  align-content: start;
  gap: 4px;
  min-width: 0;
}

.ft-24__ch {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  margin-block-end: 8px;
}

.ft-24__list {
  display: grid;
  gap: 1px;
}

.ft-24__link {
  display: inline-flex;
  align-items: center;
  min-height: 36px;
  font-size: 14.2px;
  color: var(--ft-24-fmut);
  text-decoration: none;
  width: fit-content;
  transition: color .18s ease;
}

.ft-24__link:hover {
  color: var(--ft-24-acc);
}

.ft-24__link:focus-visible,
.ft-24__hl:focus-visible {
  outline: 2px solid var(--ft-24-acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.ft-24__copy {
  padding-block: 18px;
  padding-bottom: calc(18px + env(safe-area-inset-bottom,0px));
  border-top: 1px solid var(--ft-24-line);
  font-size: 12.4px;
  color: var(--ft-24-fmut);
}

@media (prefers-reduced-motion: reduce) {
  .ft-24 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ft-24');
  if (!root || root.dataset.ready) return;
  root.dataset.ready = '1';
  const lang = root.querySelector('#ft-24-lang');
  const cur = root.querySelector('#ft-24-cur');
  const price = root.querySelector('#ft-24-price');
  const note = root.querySelector('#ft-24-note');
  const AMOUNT = 1284.5;
  const render = (announce) => {
    const locale = lang.value, code = cur.value;
    let out;
    try { out = new Intl.NumberFormat(locale, { style: 'currency', currency: code }).format(AMOUNT); }
    catch (e) { out = code + ' ' + AMOUNT.toFixed(2); }
    price.textContent = out;
    price.setAttribute('lang', locale);
    const label = lang.options[lang.selectedIndex].textContent.trim();
    const rtl = /^(ar|he|fa|ur)/.test(locale);
    price.style.direction = rtl ? 'rtl' : 'ltr';
    note.textContent = 'Formatted for ' + label + ' in ' + code + (rtl ? ' · right-to-left locale' : '');
    if (announce) note.setAttribute('aria-live', 'polite');
  };
  lang.addEventListener('change', () => render(true));
  cur.addEventListener('change', () => render(true));
  render(false);
})();
```
