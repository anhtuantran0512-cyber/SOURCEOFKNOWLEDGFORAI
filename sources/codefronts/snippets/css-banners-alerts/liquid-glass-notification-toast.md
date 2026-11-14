---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/liquid-glass-notification-toast/"
title: "Geo and Currency Switcher Bar"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "The bar every international store needs, wearing a liquid-glass treatment that holds up in 2027: layered backdrop-filter blur and saturation, a specular edge…"
has_js: "true"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Geo and Currency Switcher Bar
Source: https://codefronts.com/snippets/css-banners-alerts/liquid-glass-notification-toast/

The bar every international store needs, wearing a liquid-glass treatment that holds up in 2027: layered backdrop-filter blur and saturation, a specular edge built from a masked gradient border, and a slow sweep of highlight across the surface. Change country and every price on the page re-formats through Intl.NumberFormat — real currency behaviour, not a symbol swap.
## HTML
```html
<div class="ba-11">
  <div class="ba-11__shop">
    <header class="ba-11__head">
      <p class="ba-11__brand">Vantage Optics</p>
      <p class="ba-11__ship" data-shipline>Shipping to United Kingdom · duties included</p>
    </header>
    <ul class="ba-11__grid">
      <li><p class="ba-11__name">Meridian 38</p><p class="ba-11__price" data-base="129900">£1,299.00</p></li>
      <li><p class="ba-11__name">Monitor One</p><p class="ba-11__price" data-base="24900">£249.00</p></li>
      <li><p class="ba-11__name">Court Low</p><p class="ba-11__price" data-base="9500">£95.00</p></li>
    </ul>
  </div>

  <aside class="ba-11__toast ba-11__glass" data-toast role="region" aria-labelledby="ba-11-h">
    <span class="ba-11__sweep" aria-hidden="true"></span>
    <span class="ba-11__pin" aria-hidden="true">
      <svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="12" cy="12" r="8.6" stroke="currentColor" stroke-width="1.6"/><path d="M3.6 12h16.8M12 3.4c2.3 2.4 3.4 5.3 3.4 8.6s-1.1 6.2-3.4 8.6c-2.3-2.4-3.4-5.3-3.4-8.6S9.7 5.8 12 3.4z" stroke="currentColor" stroke-width="1.4"/></svg>
    </span>

    <div class="ba-11__copy">
      <h2 class="ba-11__h" id="ba-11-h">Looks like you're in <span data-detected>Germany</span></h2>
      <p class="ba-11__note">Switch to see prices in your currency with local duties and delivery times.</p>
    </div>

    <div class="ba-11__controls">
      <span class="ba-11__selectWrap">
        <label class="ba-11__vh" for="ba-11-country">Country or region</label>
        <select id="ba-11-country" data-country>
          <option value="GB">🇬🇧 United Kingdom · GBP</option>
          <option value="DE" selected>🇩🇪 Germany · EUR</option>
          <option value="US">🇺🇸 United States · USD</option>
          <option value="CA">🇨🇦 Canada · CAD</option>
          <option value="AU">🇦🇺 Australia · AUD</option>
          <option value="JP">🇯🇵 Japan · JPY</option>
        </select>
        <svg viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><path d="m4 6.4 4 4 4-4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </span>
      <button class="ba-11__apply" type="button" data-apply>Switch region</button>
      <button class="ba-11__stay" type="button" data-stay>Stay on UK site</button>
    </div>
    <p class="ba-11__fx" data-fx>Rates are indicative and confirmed at checkout.</p>
  </aside>
  <p class="ba-11__live" role="status" aria-live="polite"></p>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap');

.ba-11 {
  --glass-blur: 26px;
  --glass-tint: .16;
  --bg: #0b0e14;
  --ink: #f3f5f9;
  --muted: #a0a8b6;
  --line: #242a34;
  --surface: #141922;
  --acc: #8be9ff;
  --acc-2: #c9a3ff;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --serif: "Instrument Serif",ui-serif,Georgia,serif;
  container-type: inline-size;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  overflow: clip;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.ba-11 *,
.ba-11 *::before,
.ba-11 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-11 {
    --bg: oklch(15% .015 265);
    --surface: oklch(20% .018 265);
    --ink: oklch(96% .006 265);
    --muted: oklch(73% .018 265);
    --line: oklch(28% .02 265);
    --acc: oklch(85% .12 210);
    --acc-2: oklch(80% .13 300);
  }
}

@media (prefers-color-scheme: light) {
  .ba-11:not([data-theme="dark"]) {
    --bg: #eef1f6;
    --surface: #ffffff;
    --ink: #0c1017;
    --muted: #5c6472;
    --line: #dde2ea;
    --glass-tint: .55;
  }
}

.ba-11::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  background: radial-gradient(38rem 26rem at 12% 8%, color-mix(in oklab,var(--acc) 22%,transparent), transparent 60%), radial-gradient(34rem 24rem at 88% 92%, color-mix(in oklab,var(--acc-2) 22%,transparent), transparent 62%);
}

.ba-11__shop {
  position: relative;
  z-index: 1;
  max-width: 64rem;
  margin-inline: auto;
  padding: clamp(1.25rem,4vw,2.5rem) clamp(1rem,4vw,2rem) clamp(15rem,32vh,20rem);
}

.ba-11__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  margin-block-end: clamp(1rem,3vw,1.75rem);
}

.ba-11__brand {
  margin: 0;
  font-family: var(--serif);
  font-size: clamp(1.5rem,4cqw,2.125rem);
  letter-spacing: -.02em;
}

.ba-11__ship {
  margin: 0;
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.ba-11__grid {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
}

.ba-11__grid li {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: baseline;
  gap: .5rem 1rem;
  padding: .95rem .25rem;
  border-block-start: 1px solid var(--line);
}

.ba-11__grid li:last-child {
  border-block-end: 1px solid var(--line);
}

.ba-11__name {
  margin: 0;
  font-size: .9375rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.ba-11__price {
  margin: 0;
  font-size: 1rem;
  font-weight: 600;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
  transition: color .3s ease, opacity .3s ease;
}

.ba-11__price[data-flash] {
  color: var(--acc);
  opacity: 1;
}

.ba-11__toast {
  position: fixed;
  z-index: 5;
  inset: auto 50% clamp(1rem,3vw,2rem) auto;
  translate: 50% 0;
  width: min(38rem,calc(100% - 2rem));
  display: grid;
  grid-template-columns: auto 1fr;
  gap: .75rem 1rem;
  align-items: start;
  padding: 1.1rem 1.2rem;
  border-radius: 1.5rem;
  overflow: hidden;
  background: color-mix(in oklab,var(--surface) calc(var(--glass-tint) * 100%), transparent);
  box-shadow: 0 2rem 4rem -1.5rem rgb(0 0 0 / .55);
  transition: opacity .35s ease, translate .45s cubic-bezier(.16,1,.3,1), display .45s allow-discrete;
}

@starting-style {
  .ba-11__toast {
    opacity: 0;
    translate: 50% 1.5rem;
  }
}

.ba-11__toast[hidden] {
  display: none;
  opacity: 0;
  translate: 50% 1rem;
}

@supports (backdrop-filter: blur(1px)) {
  .ba-11__glass {
    backdrop-filter: blur(var(--glass-blur)) saturate(1.8) brightness(1.05);
  }
}

@supports not (backdrop-filter: blur(1px)) {
  .ba-11__glass {
    background: color-mix(in oklab,var(--surface) 94%,transparent);
    border: 1px solid var(--line);
  }
}

.ba-11__glass::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1px;
  pointer-events: none;
  background: linear-gradient(150deg, rgb(255 255 255 / .5), transparent 38%, transparent 62%, rgb(255 255 255 / .16));
  mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  mask-composite: exclude;
  -webkit-mask-composite: xor;
}

.ba-11__sweep {
  position: absolute;
  inset: -40% -10%;
  pointer-events: none;
  opacity: .5;
  background: linear-gradient(100deg, transparent 38%, rgb(255 255 255 / .3) 50%, transparent 62%);
  translate: -60% 0;
  animation: ba-11-sweep 9s cubic-bezier(.45,0,.55,1) infinite;
}

@keyframes ba-11-sweep {
  0%,
    70% {
    translate: -70% 0;
  }

  100% {
    translate: 70% 0;
  }
}

.ba-11__pin {
  display: grid;
  place-items: center;
  width: 2.5rem;
  height: 2.5rem;
  border-radius: .9rem;
  color: var(--acc);
  background: color-mix(in oklab,var(--acc) 16%,transparent);
  border: 1px solid color-mix(in oklab,var(--acc) 30%,transparent);
}

.ba-11__pin svg {
  width: 1.4rem;
  height: 1.4rem;
}

.ba-11__copy {
  min-width: 0;
}

.ba-11__h {
  margin: 0 0 .25rem;
  font-size: 1.0625rem;
  font-weight: 600;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.ba-11__h span {
  font-family: var(--serif);
  font-weight: 400;
  font-style: italic;
}

.ba-11__note {
  margin: 0;
  font-size: .8125rem;
  line-height: 1.55;
  color: var(--muted);
  max-width: 52ch;
  text-wrap: pretty;
}

.ba-11__controls {
  grid-column: 2;
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  align-items: center;
}

.ba-11__selectWrap {
  position: relative;
  flex: 1 1 13rem;
  min-width: 0;
}

.ba-11__selectWrap svg {
  position: absolute;
  inset-inline-end: .75rem;
  inset-block-start: 50%;
  translate: 0 -50%;
  width: 1rem;
  height: 1rem;
  pointer-events: none;
  color: var(--muted);
}

.ba-11__controls select {
  appearance: none;
  width: 100%;
  min-height: 2.75rem;
  padding: .7rem 2.25rem .7rem .85rem;
  font: inherit;
  font-size: .875rem;
  color: var(--ink);
  border-radius: .85rem;
  cursor: pointer;
  background: color-mix(in oklab,var(--ink) 8%,transparent);
  border: 1px solid color-mix(in oklab,var(--ink) 16%,transparent);
}

.ba-11__controls select option {
  background: var(--surface);
  color: var(--ink);
}

.ba-11__apply {
  min-height: 2.75rem;
  padding: .7rem 1.2rem;
  border: 0;
  border-radius: .85rem;
  cursor: pointer;
  font: inherit;
  font-size: .875rem;
  font-weight: 600;
  letter-spacing: -.01em;
  background: var(--ink);
  color: var(--bg);
  transition: translate .2s cubic-bezier(.16,1,.3,1), box-shadow .2s ease;
}

.ba-11__apply:hover {
  translate: 0 -1px;
  box-shadow: 0 .8rem 1.6rem -.8rem rgb(0 0 0 / .5);
}

.ba-11__stay {
  min-height: 2.75rem;
  padding: .7rem .95rem;
  border-radius: .85rem;
  cursor: pointer;
  font: inherit;
  font-size: .8125rem;
  font-weight: 500;
  color: var(--muted);
  background: transparent;
  border: 1px solid color-mix(in oklab,var(--ink) 14%,transparent);
}

.ba-11__stay:hover {
  color: var(--ink);
}

.ba-11__fx {
  grid-column: 2;
  margin: 0;
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.ba-11__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.ba-11 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ba-11 a {
  color: var(--acc);
}

@container (max-width: 36rem) {
  .ba-11__toast {
    grid-template-columns: 1fr;
    padding: 1rem;
  }

  .ba-11__pin {
    display: none;
  }

  .ba-11__controls,
    .ba-11__fx {
    grid-column: 1;
  }

  .ba-11__apply,
    .ba-11__stay {
    flex: 1 1 100%;
    text-align: center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ba-11 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .ba-11__toast {
    border: 1px solid CanvasText;
    background: Canvas;
  }

  .ba-11__apply {
    background: Highlight;
    color: HighlightText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ba-11');
  if (!root) return;
  const REGIONS = {
    GB: { name: 'United Kingdom', locale: 'en-GB', cur: 'GBP', fx: 1, ship: 'Free delivery in 2 days · duties included' },
    DE: { name: 'Germany', locale: 'de-DE', cur: 'EUR', fx: 1.17, ship: 'Kostenloser Versand in 3-4 Tagen · inkl. Zoll' },
    US: { name: 'United States', locale: 'en-US', cur: 'USD', fx: 1.27, ship: 'Free delivery in 4-6 days · duties at checkout' },
    CA: { name: 'Canada', locale: 'en-CA', cur: 'CAD', fx: 1.73, ship: 'Free delivery in 5-7 days · duties at checkout' },
    AU: { name: 'Australia', locale: 'en-AU', cur: 'AUD', fx: 1.94, ship: 'Free delivery in 6-8 days · GST included' },
    JP: { name: 'Japan', locale: 'ja-JP', cur: 'JPY', fx: 197, ship: '3-5日でお届け · 関税込み' },
  };
  const toast = root.querySelector('[data-toast]');
  const select = root.querySelector('[data-country]');
  const live = root.querySelector('.ba-11__live');

  const apply = (code) => {
    const r = REGIONS[code];
    const nf = new Intl.NumberFormat(r.locale, { style: 'currency', currency: r.cur });
    root.querySelectorAll('[data-base]').forEach((el) => {
      el.textContent = nf.format((Number(el.dataset.base) / 100) * r.fx);
      el.dataset.flash = '1';
      setTimeout(() => delete el.dataset.flash, 600);
    });
    root.querySelector('[data-shipline]').textContent = 'Shipping to ' + r.name + ' · ' + r.ship;
    root.querySelector('[data-fx]').textContent = '1 GBP ≈ ' + new Intl.NumberFormat(r.locale, { style: 'currency', currency: r.cur }).format(r.fx) + ' · indicative, confirmed at checkout';
    live.textContent = 'Prices now shown in ' + r.cur + ' for ' + r.name + '.';
  };

  root.querySelector('[data-apply]').addEventListener('click', () => { apply(select.value); toast.hidden = true; });
  root.querySelector('[data-stay]').addEventListener('click', () => { apply('GB'); toast.hidden = true; });
  select.addEventListener('change', () => { root.querySelector('[data-detected]').textContent = REGIONS[select.value].name; });
})();
```
