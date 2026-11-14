---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/arrow-key-navigation-across-menu-columns/"
title: "Arrow Key Navigation Across Menu Columns"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "Whether arrow keys belong in a mega menu, and how far to take them."
has_js: "true"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Arrow Key Navigation Across Menu Columns
Source: https://codefronts.com/navigation/css-mega-menus/arrow-key-navigation-across-menu-columns/

Whether arrow keys belong in a mega menu, and how far to take them. &larr; and &rarr; move between top-level items with a roving tabindex, &darr; enters the open panel, Escape reverses it. Inside the panel the links stay in the ordinary tab order, because forcing a 2D grid model onto columns of links usually makes things worse.
## HTML
```html
<section class="mm-08" aria-labelledby="mm-08-title">
  <h2 class="mm-08__sr" id="mm-08-title">Prism</h2>

  <div class="mm-08__theme">
    <input class="mm-08__theme-input" type="checkbox" id="mm-08-theme">
    <label class="mm-08__theme-label" for="mm-08-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-08__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="mm-08__header">
    <div class="mm-08__bar">
      <a class="mm-08__brand" href="#mm-08-title">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3 3 19h18Z" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linejoin="round"/><path d="M12 3v16" stroke="currentColor" stroke-width="1.2" opacity=".6"/></svg>
        Prism
      </a>

      <nav class="mm-08__nav" aria-label="Primary">
        <ul class="mm-08__list">
          <li class="mm-08__item">
            <button class="mm-08__trigger" type="button" tabindex="0" aria-expanded="false" aria-controls="mm-08-panel-accounts">Accounts</button>
            <div class="mm-08__panel" id="mm-08-panel-accounts" aria-label="Accounts">
              <div class="mm-08__panel-inner">
                <section class="mm-08__col" aria-labelledby="mm-08-h-personal">
                  <h3 class="mm-08__col-head" id="mm-08-h-personal">Personal</h3>
                  <ul class="mm-08__links"><li><a href="#mm-08-title">Everyday account</a></li><li><a href="#mm-08-title">Savings pots</a></li><li><a href="#mm-08-title">Joint accounts</a></li><li><a href="#mm-08-title">Currency wallets</a></li></ul>
                </section>
                <section class="mm-08__col" aria-labelledby="mm-08-h-business">
                  <h3 class="mm-08__col-head" id="mm-08-h-business">Business</h3>
                  <ul class="mm-08__links"><li><a href="#mm-08-title">Company account</a></li><li><a href="#mm-08-title">Expense cards</a></li><li><a href="#mm-08-title">Payroll</a></li></ul>
                </section>
                <section class="mm-08__col" aria-labelledby="mm-08-h-credit">
                  <h3 class="mm-08__col-head" id="mm-08-h-credit">Credit</h3>
                  <ul class="mm-08__links"><li><a href="#mm-08-title">Overdraft</a></li><li><a href="#mm-08-title">Business loan</a></li><li><a href="#mm-08-title">Invoice finance</a></li></ul>
                </section>
                <section class="mm-08__col" aria-labelledby="mm-08-h-manage">
                  <h3 class="mm-08__col-head" id="mm-08-h-manage">Manage</h3>
                  <ul class="mm-08__links"><li><a href="#mm-08-title">Statements</a></li><li><a href="#mm-08-title">Standing orders</a></li><li><a href="#mm-08-title">Card controls</a></li></ul>
                </section>
              </div>
            </div>
          </li>

          <li class="mm-08__item">
            <button class="mm-08__trigger" type="button" tabindex="-1" aria-expanded="false" aria-controls="mm-08-panel-payments">Payments</button>
            <div class="mm-08__panel" id="mm-08-panel-payments" aria-label="Payments">
              <div class="mm-08__panel-inner">
                <section class="mm-08__col" aria-labelledby="mm-08-h-send">
                  <h3 class="mm-08__col-head" id="mm-08-h-send">Send</h3>
                  <ul class="mm-08__links"><li><a href="#mm-08-title">Domestic transfer</a></li><li><a href="#mm-08-title">International</a></li><li><a href="#mm-08-title">Bulk payments</a></li></ul>
                </section>
                <section class="mm-08__col" aria-labelledby="mm-08-h-collect">
                  <h3 class="mm-08__col-head" id="mm-08-h-collect">Collect</h3>
                  <ul class="mm-08__links"><li><a href="#mm-08-title">Direct debit</a></li><li><a href="#mm-08-title">Payment links</a></li><li><a href="#mm-08-title">Subscriptions</a></li></ul>
                </section>
                <section class="mm-08__col" aria-labelledby="mm-08-h-fx">
                  <h3 class="mm-08__col-head" id="mm-08-h-fx">Currency</h3>
                  <ul class="mm-08__links"><li><a href="#mm-08-title">Live rates</a></li><li><a href="#mm-08-title">Forward contracts</a></li></ul>
                </section>
              </div>
            </div>
          </li>

          <li class="mm-08__item">
            <button class="mm-08__trigger" type="button" tabindex="-1" aria-expanded="false" aria-controls="mm-08-panel-support">Support</button>
            <div class="mm-08__panel" id="mm-08-panel-support" aria-label="Support">
              <div class="mm-08__panel-inner">
                <section class="mm-08__col" aria-labelledby="mm-08-h-help">
                  <h3 class="mm-08__col-head" id="mm-08-h-help">Help</h3>
                  <ul class="mm-08__links"><li><a href="#mm-08-title">Contact the team</a></li><li><a href="#mm-08-title">Dispute a payment</a></li><li><a href="#mm-08-title">Lost card</a></li></ul>
                </section>
                <section class="mm-08__col" aria-labelledby="mm-08-h-status">
                  <h3 class="mm-08__col-head" id="mm-08-h-status">Service</h3>
                  <ul class="mm-08__links"><li><a href="#mm-08-title">Status page</a></li><li><a href="#mm-08-title">Planned maintenance</a></li></ul>
                </section>
              </div>
            </div>
          </li>
        </ul>
      </nav>

      <div class="mm-08__utils">
        <a class="mm-08__signin" href="#mm-08-title">Log in</a>
        <a class="mm-08__cta" href="#mm-08-title">Open an account</a>
      </div>
    </div>
  </header>

  <main class="mm-08__page">
    <div class="mm-08__cards">
      <article class="mm-08__card">
        <p class="mm-08__card-k">Everyday</p>
        <p class="mm-08__card-n">&pound;4,182.60</p>
        <p class="mm-08__card-m">Prism Everyday &middot; &bull;&bull;&bull;&bull; 4417</p>
      </article>
      <article class="mm-08__card mm-08__card--alt">
        <p class="mm-08__card-k">Savings</p>
        <p class="mm-08__card-n">&pound;12,940.00</p>
        <p class="mm-08__card-m">4.6% AER &middot; paid monthly</p>
      </article>
      <article class="mm-08__card">
        <p class="mm-08__card-k">Business</p>
        <p class="mm-08__card-n">&pound;38,205.14</p>
        <p class="mm-08__card-m">Fern Studio Ltd</p>
      </article>
    </div>
  </main>
</section>
```
## CSS
```css
.mm-08 {
  --mm-08-bg: #eef4f1;
  --mm-08-surf: #ffffff;
  --mm-08-line: #d3e0da;
  --mm-08-ink: #17211d;
  --mm-08-mut: #5c6b65;
  --mm-08-acc: #047857;
  --mm-08-acc: oklch(50% 0.12 165);
  --mm-08-on-acc: #ffffff;
  --mm-08-ring: 2px;
  --mm-08-font-display: "Nunito", "Avenir Next", ui-rounded, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background-color: var(--mm-08-bg);
  background-image: radial-gradient(64rem 30rem at 90% -10%, color-mix(in oklab, var(--mm-08-acc) 14%, transparent), transparent 62%);
  color: var(--mm-08-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.mm-08 *,
.mm-08 *::before,
.mm-08 *::after {
  box-sizing: border-box;
}

.mm-08 :focus-visible {
  outline: var(--mm-08-ring) solid var(--mm-08-acc);
  outline-offset: 3px;
  border-radius: 10px;
}

.mm-08__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.mm-08:has(.mm-08__theme-input:checked) {
  --mm-08-bg: #0a1310;
  --mm-08-surf: #121e19;
  --mm-08-line: #23342c;
  --mm-08-ink: #e9f3ee;
  --mm-08-mut: #9ab0a6;
  --mm-08-acc: #34d399;
  --mm-08-acc: oklch(80% 0.14 165);
  --mm-08-on-acc: #12100e;
}

@media (prefers-color-scheme: dark) {
  .mm-08 {
    --mm-08-bg: #0a1310;
    --mm-08-surf: #121e19;
    --mm-08-line: #23342c;
    --mm-08-ink: #e9f3ee;
    --mm-08-mut: #9ab0a6;
    --mm-08-acc: #34d399;
    --mm-08-acc: oklch(80% 0.14 165);
    --mm-08-on-acc: #12100e;
  }

  .mm-08:has(.mm-08__theme-input:checked) {
    --mm-08-bg: #eef4f1;
    --mm-08-surf: #ffffff;
    --mm-08-line: #d3e0da;
    --mm-08-ink: #17211d;
    --mm-08-mut: #5c6b65;
    --mm-08-acc: #047857;
    --mm-08-acc: oklch(50% 0.12 165);
    --mm-08-on-acc: #ffffff;
  }
}

@media (prefers-color-scheme: light) {
  .mm-08:has(.mm-08__theme-input:checked) {
    --mm-08-bg: #0a1310;
    --mm-08-surf: #121e19;
    --mm-08-line: #23342c;
    --mm-08-ink: #e9f3ee;
    --mm-08-mut: #9ab0a6;
    --mm-08-acc: #34d399;
    --mm-08-acc: oklch(80% 0.14 165);
    --mm-08-on-acc: #12100e;
  }
}

.mm-08__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-08__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-08__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mm-08-line);
  border-radius: 16px;
  background: var(--mm-08-surf);
  color: var(--mm-08-ink);
  cursor: pointer;
  box-shadow: 0 6px 16px -8px rgba(23, 33, 29, 0.5);
}

.mm-08__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-08__theme-input:focus-visible + .mm-08__theme-label {
  outline: var(--mm-08-ring) solid var(--mm-08-acc);
  outline-offset: 3px;
}

.mm-08__header {
  position: relative;
  z-index: 10;
  inline-size: min(76rem, calc(100% - 2rem));
  margin: clamp(1rem, 3vw, 1.75rem) auto 0;
  border-radius: 20px;
  background: var(--mm-08-surf);
  box-shadow: 0 16px 40px -26px rgba(23, 33, 29, 0.6);
}

.mm-08__bar {
  display: flex;
  align-items: center;
  gap: clamp(0.5rem, 2vw, 1.5rem);
  flex-wrap: wrap;
  min-block-size: 68px;
  padding-inline: clamp(0.85rem, 2vw, 1.4rem) 64px;
}

.mm-08__brand {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  color: var(--mm-08-ink);
  text-decoration: none;
  font: 800 1.15rem/1 var(--mm-08-font-display);
  letter-spacing: -0.02em;
}

.mm-08__brand svg {
  inline-size: 22px;
  block-size: 22px;
  color: var(--mm-08-acc);
}

.mm-08__nav {
  min-inline-size: 0;
}

.mm-08__list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.2rem;
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
}

.mm-08__item {
  position: static;
}

.mm-08__trigger {
  min-block-size: 44px;
  padding-inline: 1rem;
  border: 0;
  border-radius: 999px;
  background: transparent;
  color: var(--mm-08-ink);
  font: 700 0.9rem/1 var(--mm-08-font-display);
  cursor: pointer;
}

.mm-08__item--open > .mm-08__trigger,
.mm-08__item:hover > .mm-08__trigger,
.mm-08__item:focus-within > .mm-08__trigger {
  background: color-mix(in oklab, var(--mm-08-acc) 16%, transparent);
  color: color-mix(in oklab, var(--mm-08-acc) 70%, var(--mm-08-ink));
}

.mm-08__utils {
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.mm-08__signin {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.7rem;
  color: var(--mm-08-mut);
  text-decoration: none;
  font: 700 0.86rem/1 var(--mm-08-font-display);
}

.mm-08__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 1.1rem;
  border-radius: 999px;
  background: var(--mm-08-acc);
  color: var(--mm-08-on-acc);
  text-decoration: none;
  font: 700 0.86rem/1 var(--mm-08-font-display);
}

.mm-08__panel {
  position: absolute;
  inset-inline: 0;
  inset-block-start: 100%;
  z-index: 30;
  border-radius: 20px;
  background: var(--mm-08-surf);
  box-shadow: 0 26px 60px -30px rgba(23, 33, 29, 0.7);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: translateY(-6px) scale(0.995);
  transition: opacity 170ms ease, transform 170ms ease, visibility 0s linear 170ms;
}

.mm-08__item--open > .mm-08__panel,
.mm-08__item:focus-within > .mm-08__panel {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transform: none;
  transition-delay: 0s;
}

@media (hover: hover) {
  .mm-08__item:hover > .mm-08__panel {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    transform: none;
    transition-delay: 0s;
  }
}

.mm-08__panel-inner {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 11rem), 1fr));
  gap: clamp(0.75rem, 2.4vw, 1.75rem);
  padding: clamp(1rem, 3vw, 1.6rem);
}

.mm-08__col {
  min-inline-size: 0;
}

.mm-08__col-head {
  margin: 0 0 0.35rem;
  font: 800 0.72rem/1 var(--mm-08-font-display);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--mm-08-mut);
}

.mm-08__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 2px;
}

.mm-08__links a {
  display: flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.6rem;
  margin-inline: -0.6rem;
  border-radius: 10px;
  color: var(--mm-08-ink);
  text-decoration: none;
  font-size: 0.9rem;
  min-inline-size: 0;
}

.mm-08__links a:hover {
  background: color-mix(in oklab, var(--mm-08-acc) 10%, transparent);
  color: var(--mm-08-acc);
}

.mm-08__page {
  inline-size: min(76rem, calc(100% - 2rem));
  margin-inline: auto;
  padding-block: clamp(2rem, 6vw, 3.5rem);
}

.mm-08__cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr));
  gap: 0.85rem;
}

.mm-08__card {
  display: grid;
  gap: 3px;
  padding: 1.1rem 1.25rem;
  border-radius: 18px;
  background: var(--mm-08-surf);
  box-shadow: 0 14px 34px -26px rgba(23, 33, 29, 0.6);
  min-inline-size: 0;
}

.mm-08__card--alt {
  background: color-mix(in oklab, var(--mm-08-acc) 14%, var(--mm-08-surf));
}

.mm-08__card-k {
  margin: 0;
  font: 800 0.68rem/1 var(--mm-08-font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--mm-08-mut);
}

.mm-08__card-n {
  margin: 0;
  font: 800 clamp(1.4rem, 4vw, 1.9rem)/1 var(--mm-08-font-display);
  letter-spacing: -0.02em;
  font-variant-numeric: tabular-nums;
}

.mm-08__card-m {
  margin: 0;
  font-size: 0.8rem;
  color: var(--mm-08-mut);
}

@media (max-width: 52rem) {
  .mm-08__bar {
    flex-direction: column;
    align-items: stretch;
    padding-block: 0.6rem;
  }

  .mm-08__list {
    flex-direction: column;
  }

  .mm-08__utils {
    margin-inline-start: 0;
  }

  .mm-08__panel {
    position: static;
    opacity: 1;
    visibility: visible;
    transform: none;
    box-shadow: none;
    display: none;
  }

  .mm-08__item--open > .mm-08__panel,
    .mm-08__item:focus-within > .mm-08__panel {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .mm-08__panel {
    transition-duration: 1ms;
  }
}

@media (hover: hover) and (pointer: fine) {
  .mm-08__trigger {
    position: relative;
  }

  .mm-08__item:hover > .mm-08__trigger::after,
    .mm-08__item:focus-within > .mm-08__trigger::after {
    content: "";
    position: absolute;
    inset-inline: 0;
    inset-block-start: 100%;
    block-size: 16px;
  }
}
/* Entry signature — rows spring open horizontally from their leading edge */

.mm-08__links li,
.mm-08__cards li {
  opacity: 0;
  scale: 0.92;
  transform-origin: 0 50%;
  transition: opacity 180ms ease, scale 440ms cubic-bezier(0.34, 1.56, 0.64, 1);
}

.mm-08__item:hover > .mm-08__panel .mm-08__links li,
.mm-08__item:focus-within > .mm-08__panel .mm-08__links li,
.mm-08__item--open > .mm-08__panel .mm-08__links li {
  opacity: 1;
  scale: 1;
}

.mm-08__item:hover > .mm-08__panel .mm-08__cards li,
.mm-08__item:focus-within > .mm-08__panel .mm-08__cards li,
.mm-08__item--open > .mm-08__panel .mm-08__cards li {
  opacity: 1;
  scale: 1;
}

.mm-08__links li:nth-child(1) {
  transition-delay: 25ms;
}

.mm-08__links li:nth-child(2) {
  transition-delay: 60ms;
}

.mm-08__links li:nth-child(3) {
  transition-delay: 95ms;
}

.mm-08__links li:nth-child(4) {
  transition-delay: 130ms;
}

.mm-08__links li:nth-child(5) {
  transition-delay: 165ms;
}

.mm-08__links li:nth-child(6) {
  transition-delay: 200ms;
}

.mm-08__links li:nth-child(n+7) {
  transition-delay: 200ms;
}

.mm-08__cards li:nth-child(1) {
  transition-delay: 120ms;
}

.mm-08__cards li:nth-child(2) {
  transition-delay: 180ms;
}

.mm-08__cards li:nth-child(3) {
  transition-delay: 240ms;
}

.mm-08__cards li:nth-child(n+4) {
  transition-delay: 240ms;
}

@media (prefers-reduced-motion: reduce) {
  .mm-08__links li,
    .mm-08__cards li {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-08__links li,
    .mm-08__cards li {
    opacity: 1;
    scale: 1;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.mm-08');
const nav = root.querySelector('.mm-08__nav');
const triggers = Array.from(nav.querySelectorAll('.mm-08__trigger'));

const setOpen = (item, on) => { item.classList.toggle('mm-08__item--open', on); item.querySelector('.mm-08__trigger').setAttribute('aria-expanded', String(on)); };
const rove = (i) => { triggers.forEach((t, n) => { t.tabIndex = n === i ? 0 : -1; }); triggers[i].focus(); };

const onKey = (e) => {
  const trigger = e.target.closest('.mm-08__trigger');
  const item = e.target.closest('.mm-08__item');
  if (trigger) {
    const i = triggers.indexOf(trigger);
    if (e.key === 'ArrowRight') { e.preventDefault(); rove((i + 1) % triggers.length); }
    else if (e.key === 'ArrowLeft') { e.preventDefault(); rove((i - 1 + triggers.length) % triggers.length); }
    else if (e.key === 'Home') { e.preventDefault(); rove(0); }
    else if (e.key === 'End') { e.preventDefault(); rove(triggers.length - 1); }
    else if (e.key === 'ArrowDown') {
      e.preventDefault();
      setOpen(item, true);
      const first = item.querySelector('.mm-08__links a');
      if (first) first.focus();
    }
  }
  if (e.key === 'Escape' && item) {
    e.preventDefault();
    setOpen(item, false);
    item.querySelector('.mm-08__trigger').focus();
  }
};
const onClick = (e) => {
  const t = e.target.closest('.mm-08__trigger');
  if (!t) return;
  const item = t.closest('.mm-08__item');
  const open = item.classList.contains('mm-08__item--open');
  nav.querySelectorAll('.mm-08__item--open').forEach((i) => setOpen(i, false));
  setOpen(item, !open);
  rove(triggers.indexOf(t));
};
const onFocusOut = (e) => {
  const item = e.target.closest('.mm-08__item');
  if (item && (!e.relatedTarget || !item.contains(e.relatedTarget))) setOpen(item, false);
};

nav.addEventListener('keydown', onKey);
nav.addEventListener('click', onClick);
nav.addEventListener('focusout', onFocusOut);

root.__mmCleanup = () => {
  nav.removeEventListener('keydown', onKey);
  nav.removeEventListener('click', onClick);
  nav.removeEventListener('focusout', onFocusOut);
};
```
