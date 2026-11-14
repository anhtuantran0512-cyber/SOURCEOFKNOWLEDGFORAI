---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/shipping-address-form-with-autocomplete/"
title: "Shipping Address Form with Autocomplete"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "An address form that does the typing for you twice over: correct HTML autocomplete tokens so browsers and password managers fill every field in one tap, plus…"
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Shipping Address Form with Autocomplete
Source: https://codefronts.com/components/css-forms/shipping-address-form-with-autocomplete/

An address form that does the typing for you twice over: correct HTML autocomplete tokens so browsers and password managers fill every field in one tap, plus an accessible WAI-ARIA combobox that suggests full addresses as you type, navigable with arrow keys and Enter. The postcode label, placeholder and pattern adapt to the selected Tier-1 country (US ZIP, UK postcode, Canadian postal code, AU postcode), and delivery speed is a set of radio cards with live arrival dates.
## HTML
```html
<div class="frm-04">
  <button type="button" class="frm-04__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-04__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-04__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-04__stage">
    <div class="frm-04__card" role="form" aria-labelledby="frm-04-title">
      <div class="frm-04__map" aria-hidden="true"><span class="frm-04__pin"></span><span class="frm-04__pulse"></span></div>
      <div class="frm-04__body">
        <h2 id="frm-04-title">Where should we send it?</h2>
        <p class="frm-04__sub">Start typing your address — or fill it in manually.</p>
        <div class="frm-04__field">
          <label for="frm-04-country">Country / region</label>
          <select id="frm-04-country" autocomplete="shipping country">
            <option value="US">United States</option><option value="GB">United Kingdom</option><option value="CA">Canada</option><option value="AU">Australia</option><option value="NZ">New Zealand</option>
          </select>
        </div>
        <div class="frm-04__field frm-04__combo">
          <label for="frm-04-line1">Street address</label>
          <div class="frm-04__inputwrap">
            <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="m20 20-4-4"/></svg>
            <input id="frm-04-line1" type="text" role="combobox" aria-autocomplete="list" aria-expanded="false" aria-controls="frm-04-list" autocomplete="shipping address-line1" placeholder="Start typing, e.g. 1 Market" required>
          </div>
          <ul id="frm-04-list" class="frm-04__list" role="listbox" aria-label="Address suggestions" hidden></ul>
          <p class="frm-04__sr" aria-live="polite" id="frm-04-live"></p>
        </div>
        <div class="frm-04__field"><label for="frm-04-line2">Apartment, suite, etc. <span class="frm-04__opt">Optional</span></label><input id="frm-04-line2" type="text" autocomplete="shipping address-line2"></div>
        <div class="frm-04__grid3">
          <div class="frm-04__field"><label for="frm-04-city">City</label><input id="frm-04-city" type="text" autocomplete="shipping address-level2" required></div>
          <div class="frm-04__field"><label for="frm-04-region" class="frm-04__regionlabel">State</label><input id="frm-04-region" type="text" autocomplete="shipping address-level1" required></div>
          <div class="frm-04__field"><label for="frm-04-zip" class="frm-04__ziplabel">ZIP code</label><input id="frm-04-zip" type="text" autocomplete="shipping postal-code" required pattern="\d{5}(-\d{4})?" placeholder="94103" aria-describedby="frm-04-zip-err"><p class="frm-04__err" id="frm-04-zip-err">Enter a valid <span class="frm-04__zipname">ZIP code</span>.</p></div>
        </div>
        <fieldset class="frm-04__ship">
          <legend>Delivery speed</legend>
          <label class="frm-04__opt-card"><input type="radio" name="frm-04-speed" data-days="5" checked><span class="frm-04__dot" aria-hidden="true"></span><span><b>Standard</b><small>Arrives <span class="frm-04__eta"></span></small></span><em>Free</em></label>
          <label class="frm-04__opt-card"><input type="radio" name="frm-04-speed" data-days="2"><span class="frm-04__dot" aria-hidden="true"></span><span><b>Express</b><small>Arrives <span class="frm-04__eta"></span></small></span><em>$9.95</em></label>
          <label class="frm-04__opt-card"><input type="radio" name="frm-04-speed" data-days="1"><span class="frm-04__dot" aria-hidden="true"></span><span><b>Next day</b><small>Arrives <span class="frm-04__eta"></span></small></span><em>$19.95</em></label>
        </fieldset>
        <label class="frm-04__bill"><input type="checkbox" checked><span>Billing address is the same as shipping</span></label>
        <button class="frm-04__cta" type="button">Continue to payment</button>
        <p class="frm-04__status" role="status"></p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Albert+Sans:wght@400;500;600;700&display=swap');

.frm-04 {
  --bg: #e9efe9;
  --surface: #ffffff;
  --soft: #f3f6f3;
  --ink: #102016;
  --muted: #5a6b60;
  --line: #dbe3dc;
  --accent: #0f766e;
  --on-accent: #fff;
  --mark: #ccfbf1;
  --bad: #c2410c;
  --sans: "Albert Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --ease: cubic-bezier(.16,1,.3,1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@media (prefers-color-scheme: dark) {
  .frm-04:not([data-theme="light"]) {
    --bg: #0b1310;
    --surface: #111c17;
    --soft: #16241e;
    --ink: #e3efe8;
    --muted: #8da397;
    --line: #24362d;
    --accent: #2dd4bf;
    --on-accent: #032420;
    --mark: #134e4a;
    --bad: #fb923c;
  }
}

.frm-04[data-theme="dark"] {
  --bg: #0b1310;
  --surface: #111c17;
  --soft: #16241e;
  --ink: #e3efe8;
  --muted: #8da397;
  --line: #24362d;
  --accent: #2dd4bf;
  --on-accent: #032420;
  --mark: #134e4a;
  --bad: #fb923c;
}

.frm-04,
.frm-04 *,
.frm-04 *::before,
.frm-04 *::after {
  box-sizing: border-box;
}

.frm-04__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,5vw,4rem);
}

.frm-04__card {
  width: 100%;
  max-width: 36rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  overflow: hidden;
  box-shadow: 0 30px 60px -35px rgba(16,32,22,.45);
}

.frm-04__map {
  position: relative;
  height: 9rem;
  background: radial-gradient(circle at 50% 60%, color-mix(in oklab,var(--accent) 18%,transparent), transparent 40%), repeating-linear-gradient(28deg, transparent 0 34px, color-mix(in oklab,var(--line) 90%,var(--ink) 6%) 34px 36px), repeating-linear-gradient(-62deg, transparent 0 58px, color-mix(in oklab,var(--line) 90%,var(--ink) 6%) 58px 61px), linear-gradient(160deg, var(--soft), color-mix(in oklab,var(--accent) 8%,var(--soft)));
  border-bottom: 1px solid var(--line);
}

.frm-04__map::after {
  content: '';
  position: absolute;
  left: -5%;
  right: -5%;
  top: 62%;
  height: 10px;
  background: color-mix(in oklab,var(--surface) 80%,transparent);
  rotate: -6deg;
  box-shadow: 0 0 0 1px var(--line);
}

.frm-04__pin {
  position: absolute;
  z-index: 2;
  left: 50%;
  top: 22%;
  width: 1.75rem;
  height: 1.75rem;
  translate: -50% 0;
  border-radius: 50% 50% 50% 0;
  rotate: -45deg;
  background: var(--accent);
  box-shadow: 0 6px 12px -4px color-mix(in oklab,var(--accent) 70%,black);
  animation: frm-04-drop .9s var(--ease) both;
}

.frm-04__pin::after {
  content: '';
  position: absolute;
  inset: 30%;
  border-radius: 50%;
  background: var(--surface);
}

.frm-04__pulse {
  position: absolute;
  z-index: 1;
  left: 50%;
  top: calc(22% + 1.9rem);
  width: 1rem;
  height: .4rem;
  translate: -50% 0;
  border-radius: 50%;
  background: color-mix(in oklab,var(--accent) 50%,transparent);
  animation: frm-04-pulse 2.2s ease-out infinite;
}

.frm-04.is-filled .frm-04__pin {
  animation: frm-04-hop .6s var(--ease);
}

@keyframes frm-04-drop {
  from {
    translate: -50% -60px;
    opacity: 0;
  }
}

@keyframes frm-04-hop {
  40% {
    translate: -50% -14px;
  }
}

@keyframes frm-04-pulse {
  from {
    scale: 1;
    opacity: .9;
  }

  to {
    scale: 5;
    opacity: 0;
  }
}

.frm-04__body {
  display: grid;
  gap: 1.1rem;
  padding: clamp(1.25rem,5vw,2.25rem);
}

.frm-04 h2 {
  margin: 0;
  font-size: clamp(1.5rem,4vw,1.85rem);
  letter-spacing: -.025em;
}

.frm-04__sub {
  margin: -.6rem 0 .1rem;
  color: var(--muted);
}

.frm-04__field {
  display: grid;
  gap: .4rem;
  position: relative;
}

.frm-04 label,
.frm-04 legend {
  font-size: .85rem;
  font-weight: 600;
}

.frm-04__opt {
  font-weight: 400;
  color: var(--muted);
  margin-left: .25rem;
}

.frm-04 input[type="text"],
.frm-04 select {
  width: 100%;
  min-height: 3rem;
  padding: .7rem .95rem;
  border-radius: .8rem;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--ink);
  font: inherit;
  font-size: 1rem;
  transition: border-color .2s, box-shadow .25s var(--ease);
}

.frm-04 select {
  appearance: none;
  padding-right: 2.5rem;
  cursor: pointer;
  background: var(--surface) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%235a6b60' stroke-width='2' stroke-linecap='round'%3E%3Cpath d='m6 9 6 6 6-6'/%3E%3C/svg%3E") no-repeat right .8rem center / 1.1rem;
}

.frm-04 input:focus-visible,
.frm-04 select:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--accent) 20%,transparent);
}

.frm-04 input:user-invalid {
  border-color: var(--bad);
}

.frm-04__err {
  display: none;
  margin: 0;
  font-size: .78rem;
  color: var(--bad);
}

.frm-04__field:has(input:user-invalid) .frm-04__err {
  display: block;
}

.frm-04__inputwrap {
  position: relative;
}

.frm-04__inputwrap svg {
  position: absolute;
  left: .9rem;
  top: 50%;
  translate: 0 -50%;
  width: 1.1rem;
  height: 1.1rem;
  fill: none;
  stroke: var(--muted);
  stroke-width: 1.8;
  stroke-linecap: round;
  pointer-events: none;
}

.frm-04 .frm-04__inputwrap input {
  padding-left: 2.6rem;
}

.frm-04__list {
  position: absolute;
  z-index: 10;
  top: calc(100% + .35rem);
  left: 0;
  right: 0;
  margin: 0;
  padding: .35rem;
  list-style: none;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1rem;
  box-shadow: 0 20px 40px -18px rgba(0,0,0,.35);
  max-height: 16rem;
  overflow: auto;
  animation: frm-04-pop .25s var(--ease);
}

@keyframes frm-04-pop {
  from {
    opacity: 0;
    translate: 0 -6px;
  }
}

.frm-04__list li {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: .15rem .7rem;
  padding: .65rem .75rem;
  border-radius: .7rem;
  cursor: pointer;
}

.frm-04__list li::before {
  content: '';
  grid-row: span 2;
  align-self: center;
  width: 1.9rem;
  height: 1.9rem;
  border-radius: .55rem;
  background: var(--soft) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%230f766e' stroke-width='1.8'%3E%3Cpath d='M12 21s-6-5.3-6-10.5A6 6 0 0 1 18 10.5C18 15.7 12 21 12 21Z'/%3E%3Ccircle cx='12' cy='10.5' r='2'/%3E%3C/svg%3E") no-repeat center / 1rem;
}

.frm-04__list b {
  font-weight: 600;
  font-size: .95rem;
}

.frm-04__list small {
  color: var(--muted);
  font-size: .8rem;
}

.frm-04__list mark {
  background: var(--mark);
  color: inherit;
  border-radius: .2rem;
  padding: 0 .1rem;
}

.frm-04__list li[aria-selected="true"],
.frm-04__list li:hover {
  background: var(--soft);
}

.frm-04__list li[aria-selected="true"] {
  box-shadow: inset 3px 0 0 var(--accent);
}

.frm-04__list .frm-04__none {
  display: block;
  color: var(--muted);
  cursor: default;
}

.frm-04__list .frm-04__none::before {
  display: none;
}

.frm-04__grid3 {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,9rem),1fr));
}

.frm-04__ship {
  border: 0;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .55rem;
}

.frm-04__ship legend {
  margin-bottom: .55rem;
  padding: 0;
}

.frm-04__opt-card {
  position: relative;
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: .85rem;
  padding: .85rem 1rem;
  border: 1px solid var(--line);
  border-radius: 1rem;
  cursor: pointer;
  transition: border-color .2s, background .2s, box-shadow .25s;
  font-weight: 400 !important;
}

.frm-04__opt-card input {
  position: absolute;
  opacity: 0;
  inset: 0;
  margin: 0;
  cursor: pointer;
}

.frm-04__opt-card b {
  display: block;
  font-size: .95rem;
}

.frm-04__opt-card small {
  color: var(--muted);
  font-size: .82rem;
}

.frm-04__opt-card em {
  font-style: normal;
  font-weight: 600;
  font-size: .92rem;
}

.frm-04__dot {
  width: 1.2rem;
  height: 1.2rem;
  border-radius: 50%;
  border: 2px solid var(--line);
  transition: border .25s var(--ease);
}

.frm-04__opt-card:hover {
  border-color: color-mix(in oklab,var(--accent) 40%,var(--line));
}

.frm-04__opt-card:has(input:checked) {
  border-color: var(--accent);
  background: color-mix(in oklab,var(--accent) 6%,var(--surface));
  box-shadow: 0 0 0 1px var(--accent);
}

.frm-04__opt-card:has(input:checked) .frm-04__dot {
  border: 6px solid var(--accent);
}

.frm-04__opt-card:has(input:focus-visible) {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.frm-04__bill {
  display: flex;
  align-items: center;
  gap: .6rem;
  min-height: 2.75rem;
  font-weight: 400 !important;
  color: var(--muted);
  cursor: pointer;
}

.frm-04__bill input {
  width: 1.15rem;
  height: 1.15rem;
  accent-color: var(--accent);
  margin: 0;
}

.frm-04__cta {
  min-height: 3.25rem;
  border: 0;
  border-radius: .9rem;
  font: inherit;
  font-weight: 600;
  font-size: 1rem;
  color: var(--on-accent);
  background: var(--accent);
  cursor: pointer;
  transition: translate .2s var(--ease), filter .2s;
  box-shadow: 0 12px 24px -14px var(--accent);
}

.frm-04__cta:hover {
  translate: 0 -2px;
  filter: brightness(1.08);
}

.frm-04__cta:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.frm-04__status {
  margin: -.4rem 0 0;
  text-align: center;
  font-size: .85rem;
  color: var(--accent);
}

.frm-04__status:empty {
  display: none;
}

.frm-04__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .frm-04 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .frm-04__list li[aria-selected="true"] {
    background: Highlight;
    color: HighlightText;
  }

  .frm-04__opt-card:has(input:checked) {
    outline: 2px solid Highlight;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-04 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-04__theme {
  position: absolute;
  top: 16px;
  right: 16px;
  z-index: 20;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  padding: 0;
  border-radius: 999px;
  border: 1px solid color-mix(in srgb, currentColor 22%, transparent);
  background: color-mix(in srgb, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background-color .2s, transform .2s;
}

.frm-04__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-04__theme:active {
  transform: scale(.94);
}

.frm-04__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-04__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-04__theme .frm-04__sun,
.frm-04__theme[aria-pressed="true"] .frm-04__moon {
  display: none;
}

.frm-04__theme[aria-pressed="true"] .frm-04__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-04__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-04__theme {
    border-color: ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.frm-04').forEach((root) => {
    const btn = root.querySelector(':scope > [data-theme-toggle]');
    if (!btn || btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const mq = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : mq.matches);
    const sync = () => {
      const dark = isDark();
      btn.setAttribute('aria-pressed', String(dark));
      btn.title = dark ? 'Switch to light mode' : 'Switch to dark mode';
    };
    btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
    mq.addEventListener('change', sync);
    new MutationObserver(sync).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
    sync();
  });
})();
(() => {
  const root = document.querySelector('.frm-04');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const ADDRESSES = [
    { c: 'US', line1: '1 Market Street', city: 'San Francisco', region: 'CA', zip: '94105' },
    { c: 'US', line1: '1600 Amphitheatre Parkway', city: 'Mountain View', region: 'CA', zip: '94043' },
    { c: 'US', line1: '350 Fifth Avenue', city: 'New York', region: 'NY', zip: '10118' },
    { c: 'US', line1: '233 South Wacker Drive', city: 'Chicago', region: 'IL', zip: '60606' },
    { c: 'GB', line1: '10 Downing Street', city: 'London', region: 'Greater London', zip: 'SW1A 2AA' },
    { c: 'GB', line1: '221B Baker Street', city: 'London', region: 'Greater London', zip: 'NW1 6XE' },
    { c: 'GB', line1: '1 Princes Street', city: 'Edinburgh', region: 'Midlothian', zip: 'EH2 2EQ' },
    { c: 'CA', line1: '290 Bremner Boulevard', city: 'Toronto', region: 'ON', zip: 'M5V 3L9' },
    { c: 'CA', line1: '1 Market Square', city: 'Saint John', region: 'NB', zip: 'E2L 4Z6' },
    { c: 'AU', line1: '1 Macquarie Street', city: 'Sydney', region: 'NSW', zip: '2000' },
    { c: 'AU', line1: '10 Market Lane', city: 'Melbourne', region: 'VIC', zip: '3000' },
    { c: 'NZ', line1: '1 Queen Street', city: 'Auckland', region: 'Auckland', zip: '1010' }
  ];
  const COUNTRY = {
    US: { zip: 'ZIP code', ph: '94103', re: '\\d{5}(-\\d{4})?', region: 'State' },
    GB: { zip: 'Postcode', ph: 'SW1A 1AA', re: '[A-Za-z]{1,2}\\d[A-Za-z\\d]? ?\\d[A-Za-z]{2}', region: 'County' },
    CA: { zip: 'Postal code', ph: 'K1A 0B1', re: '[A-Za-z]\\d[A-Za-z] ?\\d[A-Za-z]\\d', region: 'Province' },
    AU: { zip: 'Postcode', ph: '2000', re: '\\d{4}', region: 'State / territory' },
    NZ: { zip: 'Postcode', ph: '1010', re: '\\d{4}', region: 'Region' }
  };
  const input = $('#frm-04-line1'), list = $('#frm-04-list'), live = $('#frm-04-live'), country = $('#frm-04-country');
  let results = [], active = -1;
  const esc = (s) => s.replace(/[&<>"]/g, (ch) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[ch]);
  const hl = (text, q) => { const i = text.toLowerCase().indexOf(q.toLowerCase()); return i < 0 ? esc(text) : esc(text.slice(0, i)) + '<mark>' + esc(text.slice(i, i + q.length)) + '</mark>' + esc(text.slice(i + q.length)); };
  const close = () => { list.hidden = true; input.setAttribute('aria-expanded', 'false'); input.removeAttribute('aria-activedescendant'); active = -1; };
  const setActive = (i) => {
    active = i;
    list.querySelectorAll('[role="option"]').forEach((li, j) => li.setAttribute('aria-selected', j === i));
    if (i >= 0) { input.setAttribute('aria-activedescendant', 'frm-04-opt-' + i); const el = list.children[i]; if (el) list.scrollTop = Math.max(0, el.offsetTop - list.clientHeight + el.offsetHeight); }
  };
  const open = () => {
    const q = input.value.trim();
    if (q.length < 2) { close(); return; }
    results = ADDRESSES.filter((a) => a.c === country.value && (a.line1 + ' ' + a.city).toLowerCase().includes(q.toLowerCase())).slice(0, 6);
    list.innerHTML = results.length
      ? results.map((a, i) => '<li role="option" id="frm-04-opt-' + i + '" aria-selected="false"><b>' + hl(a.line1, q) + '</b><small>' + esc(a.city + ', ' + a.region + ' ' + a.zip) + '</small></li>').join('')
      : '<li class="frm-04__none" role="option" aria-disabled="true">No matches — keep typing or enter manually.</li>';
    list.hidden = false; input.setAttribute('aria-expanded', 'true');
    live.textContent = results.length ? results.length + ' suggestions. Use up and down arrows to review.' : 'No suggestions.';
    setActive(-1);
  };
  const pick = (i) => {
    const a = results[i]; if (!a) return;
    input.value = a.line1; $('#frm-04-city').value = a.city; $('#frm-04-region').value = a.region; $('#frm-04-zip').value = a.zip;
    close(); live.textContent = 'Address filled: ' + a.line1 + ', ' + a.city;
    root.classList.remove('is-filled'); void root.offsetWidth; root.classList.add('is-filled');
    $('#frm-04-line2').focus();
  };
  input.addEventListener('input', open);
  input.addEventListener('keydown', (e) => {
    if (list.hidden && e.key === 'ArrowDown') { open(); return; }
    if (e.key === 'ArrowDown') { e.preventDefault(); setActive(Math.min(results.length - 1, active + 1)); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); setActive(Math.max(0, active - 1)); }
    else if (e.key === 'Enter' && active >= 0) { e.preventDefault(); pick(active); }
    else if (e.key === 'Escape') close();
  });
  list.addEventListener('mousedown', (e) => { const li = e.target.closest('[id^="frm-04-opt-"]'); if (li) { e.preventDefault(); pick(Number(li.id.split('-').pop())); } });
  input.addEventListener('blur', () => setTimeout(close, 120));
  const applyCountry = () => {
    const c = COUNTRY[country.value], zip = $('#frm-04-zip');
    $('.frm-04__ziplabel').textContent = c.zip; $('.frm-04__zipname').textContent = c.zip;
    $('.frm-04__regionlabel').textContent = c.region; zip.placeholder = c.ph; zip.pattern = c.re;
  };
  country.addEventListener('change', () => { applyCountry(); close(); });
  applyCountry();
  const d = new Intl.DateTimeFormat('en-US', { weekday: 'short', month: 'short', day: 'numeric' });
  root.querySelectorAll('.frm-04__opt-card').forEach((card) => {
    const days = Number(card.querySelector('input').dataset.days), t = new Date();
    let added = 0; while (added < days) { t.setDate(t.getDate() + 1); if (t.getDay() % 6) added++; }
    card.querySelector('.frm-04__eta').textContent = d.format(t);
  });
  $('.frm-04__cta').addEventListener('click', () => {
    const bad = [...root.querySelectorAll('input[required]')].find((f) => !f.checkValidity());
    if (bad) { bad.focus(); bad.reportValidity(); return; }
    $('.frm-04__status').textContent = 'Address saved. Continuing to payment…';
  });
})();
```
