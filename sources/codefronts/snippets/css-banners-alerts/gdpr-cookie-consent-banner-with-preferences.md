---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/gdpr-cookie-consent-banner-with-preferences/"
title: "GDPR Cookie Consent Banner with Preferences"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "A consent card that actually satisfies the thing regulators care about: reject is as easy as accept, and every optional purpose has its own switch."
has_js: "true"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: GDPR Cookie Consent Banner with Preferences
Source: https://codefronts.com/snippets/css-banners-alerts/gdpr-cookie-consent-banner-with-preferences/

A consent card that actually satisfies the thing regulators care about: reject is as easy as accept, and every optional purpose has its own switch. The preferences drawer animates open from height:0 to height:auto using ::details-content and interpolate-size:allow-keywords, the live "3 of 4 purposes allowed" readout is pure CSS counters reading :has(:checked), and the card enters and leaves with @starting-style + transition-behavior:allow-discrete so there is no JavaScript animation code at all.
## HTML
```html
<div class="ba-01">
  <div class="ba-01__page" aria-hidden="true">
    <div class="ba-01__nav"><span class="ba-01__logo">Northline</span><span class="ba-01__navLinks"><span></span><span></span><span></span></span></div>
    <div class="ba-01__hero">
      <p class="ba-01__eyebrow">Field Report</p>
      <h2>Grid-scale storage, one county at a time</h2>
      <p class="ba-01__lede">A five-part series on the quiet infrastructure build-out happening behind the substation fence.</p>
    </div>
    <div class="ba-01__grid"><span></span><span></span><span></span></div>
  </div>

  <section class="ba-01__card" id="ba-01-card" role="region" aria-labelledby="ba-01-title">
    <div class="ba-01__head">
      <span class="ba-01__mark" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 2.8 20 6v5.6c0 4.6-3.2 8.2-8 9.6-4.8-1.4-8-5-8-9.6V6z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="m8.6 12.2 2.3 2.3 4.5-4.7" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </span>
      <div>
        <h2 class="ba-01__title" id="ba-01-title">Your privacy choices</h2>
        <p class="ba-01__body">We use cookies to run the site and, with your permission, to measure what people read and to personalise what we show you. You can change this any time.</p>
      </div>
    </div>

    <details class="ba-01__panel" id="ba-01-panel">
      <summary class="ba-01__summary">
        <span>Manage purposes</span>
        <svg class="ba-01__chev" viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="m4 6.2 4 4 4-4" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </summary>
      <div class="ba-01__panelInner">
        <ul class="ba-01__cats">
          <li class="ba-01__row" data-locked="true">
            <div class="ba-01__rowText">
              <p class="ba-01__rowT">Strictly necessary</p>
              <p class="ba-01__rowD">Session, security and load balancing. Always on — the site cannot run without these.</p>
            </div>
            <label class="ba-01__sw">
              <input type="checkbox" checked disabled>
              <span class="ba-01__track" aria-hidden="true"><span class="ba-01__knob"></span></span>
              <span class="ba-01__vh">Strictly necessary cookies (required)</span>
            </label>
          </li>
          <li class="ba-01__row">
            <div class="ba-01__rowText">
              <p class="ba-01__rowT">Analytics <span class="ba-01__pill">4 vendors</span></p>
              <p class="ba-01__rowD">Aggregate page and scroll depth reporting. No cross-site identifiers.</p>
            </div>
            <label class="ba-01__sw">
              <input type="checkbox" data-opt="analytics" checked>
              <span class="ba-01__track" aria-hidden="true"><span class="ba-01__knob"></span></span>
              <span class="ba-01__vh">Allow analytics cookies</span>
            </label>
          </li>
          <li class="ba-01__row">
            <div class="ba-01__rowText">
              <p class="ba-01__rowT">Personalisation</p>
              <p class="ba-01__rowD">Remembers your reading list, region and text size across visits.</p>
            </div>
            <label class="ba-01__sw">
              <input type="checkbox" data-opt="personalisation" checked>
              <span class="ba-01__track" aria-hidden="true"><span class="ba-01__knob"></span></span>
              <span class="ba-01__vh">Allow personalisation cookies</span>
            </label>
          </li>
          <li class="ba-01__row">
            <div class="ba-01__rowText">
              <p class="ba-01__rowT">Advertising <span class="ba-01__pill">18 partners</span></p>
              <p class="ba-01__rowD">Measures campaigns and limits how often you see the same creative.</p>
            </div>
            <label class="ba-01__sw">
              <input type="checkbox" data-opt="advertising">
              <span class="ba-01__track" aria-hidden="true"><span class="ba-01__knob"></span></span>
              <span class="ba-01__vh">Allow advertising cookies</span>
            </label>
          </li>
        </ul>
        <p class="ba-01__tally"><span class="ba-01__vh">Currently </span></p>
      </div>
    </details>

    <div class="ba-01__actions">
      <button class="ba-01__btn ba-01__btn--ghost" type="button" data-act="reject">Reject optional</button>
      <button class="ba-01__btn ba-01__btn--ghost" type="button" data-act="save">Save choices</button>
      <button class="ba-01__btn ba-01__btn--primary" type="button" data-act="all">Accept all</button>
    </div>
    <p class="ba-01__legal"><a href="#ba-01-card">Privacy notice</a><span aria-hidden="true">·</span><a href="#ba-01-card">Cookie register</a><span aria-hidden="true">·</span>Consent stored 12 months</p>
  </section>

  <button class="ba-01__reopen" type="button" data-act="reopen" hidden>
    <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 2.8 20 6v5.6c0 4.6-3.2 8.2-8 9.6-4.8-1.4-8-5-8-9.6V6z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
    Privacy choices
  </button>
  <p class="ba-01__status" role="status" aria-live="polite"></p>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=Newsreader:opsz,[email protected],400;6..72,500&display=swap');

.ba-01 {
  --bg: #0b0d12;
  --page: #11141b;
  --surface: #161a23;
  --text: #f2f4f8;
  --muted: #9aa3b2;
  --line: #252b37;
  --acc: #7c5cff;
  --acc-ink: #ffffff;
  --ok: #22c55e;
  --glass: .72;
  --sans: "Instrument Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --serif: "Newsreader",ui-serif,Georgia,serif;
  interpolate-size: allow-keywords;
  container-type: inline-size;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  overflow: clip;
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.ba-01 *,
.ba-01 *::before,
.ba-01 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-01 {
    --bg: oklch(16% .02 268);
    --page: oklch(19% .022 268);
    --surface: oklch(22% .025 268);
    --text: oklch(97% .006 268);
    --muted: oklch(72% .022 268);
    --line: oklch(31% .026 268);
    --acc: oklch(66% .19 292);
    --ok: oklch(72% .17 150);
  }
}

@media (prefers-color-scheme: light) {
  .ba-01:not([data-theme="dark"]) {
    --bg: #f4f5f8;
    --page: #ffffff;
    --surface: #ffffff;
    --text: #111318;
    --muted: #5c6472;
    --line: #e3e6ec;
    --acc: #5b3df5;
    --glass: .86;
  }
}

.ba-01[data-theme="light"] {
  --bg: #f4f5f8;
  --page: #ffffff;
  --surface: #ffffff;
  --text: #111318;
  --muted: #5c6472;
  --line: #e3e6ec;
  --acc: #5b3df5;
  --glass: .86;
}

.ba-01::before {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  background: radial-gradient(60rem 40rem at 82% -10%, color-mix(in oklab,var(--acc) 26%,transparent), transparent 62%), radial-gradient(40rem 30rem at 8% 108%, color-mix(in oklab,var(--acc) 14%,transparent), transparent 60%);
}
/* mock page behind the banner */

.ba-01__page {
  position: relative;
  z-index: 1;
  max-width: 72rem;
  margin-inline: auto;
  padding: clamp(1.25rem,4vw,3rem) clamp(1.25rem,5vw,3rem) clamp(16rem,34vh,22rem);
  display: grid;
  gap: clamp(1.5rem,4vw,2.75rem);
}

.ba-01__nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.ba-01__logo {
  font-weight: 700;
  letter-spacing: -.03em;
  font-size: 1.0625rem;
}

.ba-01__navLinks {
  display: flex;
  gap: .75rem;
}

.ba-01__navLinks span {
  display: block;
  width: 3.25rem;
  height: .5rem;
  border-radius: 999px;
  background: var(--line);
}

.ba-01__hero {
  display: grid;
  gap: .85rem;
  max-width: 44ch;
}

.ba-01__eyebrow {
  margin: 0;
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--acc);
}

.ba-01__hero h2 {
  margin: 0;
  font-size: clamp(2rem,6.5cqw,3.5rem);
  line-height: 1.02;
  letter-spacing: -.045em;
  font-weight: 600;
  text-wrap: balance;
}

.ba-01__lede {
  margin: 0;
  font-family: var(--serif);
  font-size: clamp(1rem,2cqw,1.1875rem);
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.ba-01__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(12rem,1fr));
  gap: 1rem;
}

.ba-01__grid span {
  display: block;
  height: clamp(6rem,14vh,9rem);
  border-radius: 1rem;
  border: 1px solid var(--line);
  background: var(--page);
}
/* consent card */

.ba-01__card {
  position: fixed;
  z-index: 5;
  inset: auto auto 1.25rem 1.25rem;
  width: min(30rem,calc(100% - 2.5rem));
  display: grid;
  gap: 1rem;
  padding: 1.25rem;
  border-radius: 1.5rem;
  border: 1px solid color-mix(in oklab,var(--line) 80%,var(--text) 4%);
  background: color-mix(in oklab,var(--surface) calc(var(--glass) * 100%),transparent);
  box-shadow: 0 2.5rem 5rem -1.5rem rgb(0 0 0 / .55), 0 0 0 1px rgb(255 255 255 / .04) inset;
  transition: opacity .4s ease, translate .5s cubic-bezier(.16,1,.3,1), scale .5s cubic-bezier(.16,1,.3,1), display .5s allow-discrete;
}

@supports (backdrop-filter: blur(1px)) {
  .ba-01__card {
    backdrop-filter: blur(22px) saturate(1.5);
  }
}

@starting-style {
  .ba-01__card {
    opacity: 0;
    translate: 0 1.5rem;
    scale: .97;
  }
}

.ba-01__card[hidden] {
  display: none;
  opacity: 0;
  translate: 0 1rem;
  scale: .98;
}

.ba-01__head {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: .85rem;
  align-items: start;
}

.ba-01__mark {
  display: grid;
  place-items: center;
  width: 2.5rem;
  height: 2.5rem;
  border-radius: .85rem;
  color: var(--acc);
  background: color-mix(in oklab,var(--acc) 16%,transparent);
  border: 1px solid color-mix(in oklab,var(--acc) 32%,transparent);
}

.ba-01__mark svg {
  width: 1.375rem;
  height: 1.375rem;
}

.ba-01__title {
  margin: 0 0 .3rem;
  font-size: 1.0625rem;
  font-weight: 650;
  letter-spacing: -.02em;
}

.ba-01__body {
  margin: 0;
  font-size: .875rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 52ch;
  text-wrap: pretty;
}

.ba-01__panel {
  border: 1px solid var(--line);
  border-radius: 1rem;
  background: color-mix(in oklab,var(--bg) 45%,transparent);
}

.ba-01__summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .5rem;
  min-height: 2.75rem;
  padding: .65rem .9rem;
  cursor: pointer;
  list-style: none;
  font-size: .8125rem;
  font-weight: 600;
  letter-spacing: -.01em;
  border-radius: 1rem;
}

.ba-01__summary::-webkit-details-marker {
  display: none;
}

.ba-01__summary:hover {
  color: var(--acc);
}

.ba-01__chev {
  width: 1rem;
  height: 1rem;
  transition: rotate .35s cubic-bezier(.16,1,.3,1);
}

.ba-01__panel[open] .ba-01__chev {
  rotate: 180deg;
}

.ba-01__panel::details-content {
  block-size: 0;
  overflow: clip;
  opacity: 0;
  transition: block-size .45s cubic-bezier(.16,1,.3,1), opacity .3s ease, content-visibility .45s allow-discrete;
}

.ba-01__panel[open]::details-content {
  block-size: auto;
  opacity: 1;
}

.ba-01__panelInner {
  padding: 0 .9rem .9rem;
}

.ba-01__cats {
  counter-reset: allowed 0;
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
}

.ba-01__row {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: .75rem;
  align-items: center;
  padding: .7rem 0;
  border-top: 1px solid var(--line);
}

.ba-01__row:has(input:checked) {
  counter-increment: allowed;
}

.ba-01__row[data-locked] .ba-01__rowT {
  color: var(--muted);
}

.ba-01__rowT {
  margin: 0 0 .2rem;
  display: flex;
  align-items: center;
  gap: .4rem;
  font-size: .8125rem;
  font-weight: 600;
}

.ba-01__rowD {
  margin: 0;
  font-size: .75rem;
  line-height: 1.5;
  color: var(--muted);
  max-width: 44ch;
  text-wrap: pretty;
}

.ba-01__pill {
  font-size: .625rem;
  font-weight: 700;
  letter-spacing: .04em;
  padding: .1rem .35rem;
  border-radius: .35rem;
  color: var(--muted);
  background: color-mix(in oklab,var(--text) 8%,transparent);
  font-variant-numeric: tabular-nums;
}

.ba-01__sw {
  display: grid;
  place-items: center;
  min-width: 2.75rem;
  min-height: 2.75rem;
  cursor: pointer;
}

.ba-01__sw input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
}

.ba-01__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ba-01__track {
  display: block;
  width: 2.5rem;
  height: 1.5rem;
  border-radius: 999px;
  padding: .1875rem;
  background: color-mix(in oklab,var(--text) 14%,transparent);
  border: 1px solid var(--line);
  transition: background .25s ease, border-color .25s ease;
}

.ba-01__knob {
  display: block;
  width: 1.0625rem;
  height: 1.0625rem;
  border-radius: 999px;
  background: var(--text);
  transition: translate .32s cubic-bezier(.34,1.56,.64,1), background .25s ease;
}

.ba-01__sw input:checked + .ba-01__track {
  background: var(--acc);
  border-color: transparent;
}

.ba-01__sw input:checked + .ba-01__track .ba-01__knob {
  translate: 1rem 0;
  background: var(--acc-ink);
}

.ba-01__sw input:disabled + .ba-01__track {
  opacity: .5;
  cursor: not-allowed;
}

.ba-01__sw input:focus-visible + .ba-01__track {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.ba-01__tally {
  margin: .75rem 0 0;
  padding-top: .7rem;
  border-top: 1px solid var(--line);
  font-size: .75rem;
  font-weight: 600;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.ba-01__tally::after {
  content: counter(allowed) " of 4 purposes allowed";
}

.ba-01__actions {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
}

.ba-01__btn {
  flex: 1 1 8rem;
  min-height: 2.75rem;
  padding: .65rem 1rem;
  border-radius: .85rem;
  cursor: pointer;
  font: inherit;
  font-size: .8125rem;
  font-weight: 600;
  letter-spacing: -.01em;
  border: 1px solid var(--line);
  background: color-mix(in oklab,var(--text) 6%,transparent);
  color: var(--text);
  transition: background .22s ease, border-color .22s ease, translate .22s ease;
}

.ba-01__btn:hover {
  border-color: color-mix(in oklab,var(--acc) 50%,var(--line));
  translate: 0 -1px;
}

.ba-01__btn:active {
  translate: 0 0;
  scale: .985;
}

.ba-01__btn--primary {
  background: var(--acc);
  border-color: transparent;
  color: var(--acc-ink);
}

.ba-01__btn--primary:hover {
  background: color-mix(in oklab,var(--acc) 88%,white);
}

.ba-01__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ba-01__legal {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .45rem;
  align-items: center;
  font-size: .6875rem;
  color: var(--muted);
}

.ba-01__legal a {
  color: var(--muted);
  text-decoration: underline;
  text-underline-offset: 2px;
}

.ba-01__legal a:hover {
  color: var(--acc);
}

.ba-01__reopen {
  position: fixed;
  z-index: 5;
  inset: auto auto 1.25rem 1.25rem;
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-height: 2.75rem;
  padding: .6rem 1rem;
  border-radius: 999px;
  cursor: pointer;
  font: inherit;
  font-size: .8125rem;
  font-weight: 600;
  color: var(--text);
  border: 1px solid var(--line);
  background: color-mix(in oklab,var(--surface) 88%,transparent);
  box-shadow: 0 1rem 2rem -1rem rgb(0 0 0 / .5);
}

@supports (backdrop-filter: blur(1px)) {
  .ba-01__reopen {
    backdrop-filter: blur(14px);
  }
}

.ba-01__reopen svg {
  width: 1.0625rem;
  height: 1.0625rem;
  color: var(--acc);
}

.ba-01__reopen:hover {
  border-color: color-mix(in oklab,var(--acc) 55%,var(--line));
}

.ba-01__reopen:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ba-01__status {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@container (max-width: 34rem) {
  .ba-01__card {
    inset: auto 0 0 0;
    width: 100%;
    border-radius: 1.5rem 1.5rem 0 0;
    border-inline: 0;
    border-block-end: 0;
  }

  .ba-01__actions .ba-01__btn {
    flex: 1 1 100%;
  }

  .ba-01__reopen {
    inset: auto 1rem 1rem auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ba-01 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .ba-01__card,
    .ba-01__panel,
    .ba-01__btn {
    border: 1px solid CanvasText;
  }

  .ba-01__sw input:checked + .ba-01__track {
    background: Highlight;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ba-01');
  if (!root) return;
  const card = root.querySelector('#ba-01-card');
  const panel = root.querySelector('#ba-01-panel');
  const reopen = root.querySelector('[data-act="reopen"]');
  const status = root.querySelector('.ba-01__status');
  const opts = [...root.querySelectorAll('input[data-opt]')];

  const commit = (label) => {
    // persist here, e.g. localStorage.setItem('consent', JSON.stringify(state))
    const on = opts.filter((i) => i.checked).map((i) => i.dataset.opt);
    status.textContent = label + ' — allowed: ' + (on.join(', ') || 'essential only');
    card.hidden = true;
    panel.open = false;
    reopen.hidden = false;
    reopen.focus();
  };

  root.addEventListener('click', (e) => {
    const act = e.target.closest('[data-act]')?.dataset.act;
    if (!act) return;
    if (act === 'all') { opts.forEach((i) => (i.checked = true)); commit('All purposes accepted'); }
    if (act === 'reject') { opts.forEach((i) => (i.checked = false)); commit('Optional purposes rejected'); }
    if (act === 'save') commit('Preferences saved');
    if (act === 'reopen') { reopen.hidden = true; card.hidden = false; panel.open = true; panel.querySelector('summary').focus(); }
  });
})();
```
