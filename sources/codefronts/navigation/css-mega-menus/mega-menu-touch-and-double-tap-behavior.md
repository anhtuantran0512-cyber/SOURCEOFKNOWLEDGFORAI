---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/mega-menu-touch-and-double-tap-behavior/"
title: "Mega Menu Touch and Double Tap Behavior"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "On touch, a hover-opened menu whose trigger is also a link needs two taps &mdash; the first opens the panel, the second follows the link &mdash; and users…"
has_js: "true"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mega Menu Touch and Double Tap Behavior
Source: https://codefronts.com/navigation/css-mega-menus/mega-menu-touch-and-double-tap-behavior/

On touch, a hover-opened menu whose trigger is also a link needs two taps &mdash; the first opens the panel, the second follows the link &mdash; and users almost never discover that. This mobile storefront separates the jobs: the trigger is a <button> that only opens, the section's own destination is the first link inside the panel, and pointerdown branches on pointerType so hybrid laptops behave too.
## HTML
```html
<section class="mm-10" aria-labelledby="mm-10-title">
  <h2 class="mm-10__sr" id="mm-10-title">Nova</h2>

  <div class="mm-10__theme">
    <input class="mm-10__theme-input" type="checkbox" id="mm-10-theme">
    <label class="mm-10__theme-label" for="mm-10-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-10__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mm-10__stage">
    <div class="mm-10__device">
      <div class="mm-10__status" aria-hidden="true"><span>9:41</span><span class="mm-10__status-dots"></span></div>

      <header class="mm-10__header">
        <div class="mm-10__bar">
          <span class="mm-10__icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" focusable="false"><path d="M4 7h16M4 12h16M4 17h16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          </span>
          <a class="mm-10__brand" href="#mm-10-title">NOVA</a>
          <span class="mm-10__icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" focusable="false"><path d="M6 7h12l-1.2 11H7.2Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M9.5 7a2.5 2.5 0 0 1 5 0" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>
          </span>
        </div>

        <nav class="mm-10__nav" aria-label="Primary">
          <ul class="mm-10__list">
            <li class="mm-10__item">
              <button class="mm-10__trigger" type="button" aria-expanded="false" aria-controls="mm-10-panel-shop" data-mm-10-tap>
                Shop
                <svg class="mm-10__chev" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
              </button>
              <div class="mm-10__panel" id="mm-10-panel-shop" aria-label="Shop">
                <a class="mm-10__overview" href="#mm-10-title">
                  <b>Shop all</b><span>420 styles in stock</span>
                </a>
                <ul class="mm-10__links">
                  <li><a href="#mm-10-title">Running<span>128</span></a></li>
                  <li><a href="#mm-10-title">Trail<span>64</span></a></li>
                  <li><a href="#mm-10-title">Recovery<span>31</span></a></li>
                  <li><a href="#mm-10-title">Accessories<span>92</span></a></li>
                </ul>
              </div>
            </li>

            <li class="mm-10__item">
              <button class="mm-10__trigger" type="button" aria-expanded="false" aria-controls="mm-10-panel-collections" data-mm-10-tap>
                Collections
                <svg class="mm-10__chev" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
              </button>
              <div class="mm-10__panel" id="mm-10-panel-collections" aria-label="Collections">
                <a class="mm-10__overview" href="#mm-10-title"><b>All collections</b><span>Seasonal drops</span></a>
                <ul class="mm-10__links">
                  <li><a href="#mm-10-title">Winter series<span>new</span></a></li>
                  <li><a href="#mm-10-title">Long distance<span>24</span></a></li>
                </ul>
              </div>
            </li>

            <li class="mm-10__item">
              <button class="mm-10__trigger" type="button" aria-expanded="false" aria-controls="mm-10-panel-stories" data-mm-10-tap>
                Stories
                <svg class="mm-10__chev" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
              </button>
              <div class="mm-10__panel" id="mm-10-panel-stories" aria-label="Stories">
                <a class="mm-10__overview" href="#mm-10-title"><b>All stories</b><span>Athlete diaries and field tests</span></a>
                <ul class="mm-10__links">
                  <li><a href="#mm-10-title">Athlete diaries<span>12</span></a></li>
                  <li><a href="#mm-10-title">Field testing<span>7</span></a></li>
                </ul>
              </div>
            </li>
          </ul>
        </nav>
      </header>

      <main class="mm-10__page">
        <p class="mm-10__promo">Free returns for 60 days</p>
        <div class="mm-10__tile">
          <p class="mm-10__tile-k">New in</p>
          <p class="mm-10__tile-h">Nova Drift 3</p>
          <p class="mm-10__tile-m">&pound;135 &middot; four colourways</p>
        </div>
      </main>
    </div>
  </div>
</section>
```
## CSS
```css
.mm-10 {
  --mm-10-bg: #fdf2f8;
  --mm-10-surf: #ffffff;
  --mm-10-line: #f3d8e6;
  --mm-10-ink: #2c1a26;
  --mm-10-mut: #7b6070;
  --mm-10-acc: #be185d;
  --mm-10-acc: oklch(52% 0.2 355);
  --mm-10-on-acc: #ffffff;
  --mm-10-acc2: #7c3aed;
  --mm-10-acc2: oklch(52% 0.24 295);
  --mm-10-radius: 34px;
  --mm-10-font-display: "Quicksand", "Avenir Next", ui-rounded, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background-color: var(--mm-10-bg);
  background-image: radial-gradient(70rem 34rem at 12% -10%, color-mix(in oklab, var(--mm-10-acc2) 18%, transparent), transparent 62%), radial-gradient(50rem 28rem at 95% 8%, color-mix(in oklab, var(--mm-10-acc) 16%, transparent), transparent 60%);
  color: var(--mm-10-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.mm-10 *,
.mm-10 *::before,
.mm-10 *::after {
  box-sizing: border-box;
}

.mm-10 :focus-visible {
  outline: 2px solid var(--mm-10-acc);
  outline-offset: 3px;
  border-radius: 12px;
}

.mm-10__sr {
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

.mm-10:has(.mm-10__theme-input:checked) {
  --mm-10-bg: #150d13;
  --mm-10-surf: #1f1520;
  --mm-10-line: #3a2733;
  --mm-10-ink: #fbeef5;
  --mm-10-mut: #b795a8;
  --mm-10-acc: #f9a8d4;
  --mm-10-acc: oklch(80% 0.13 350);
  --mm-10-on-acc: #12100e;
  --mm-10-acc2: #c4b5fd;
  --mm-10-acc2: oklch(81% 0.1 295);
}

@media (prefers-color-scheme: dark) {
  .mm-10 {
    --mm-10-bg: #150d13;
    --mm-10-surf: #1f1520;
    --mm-10-line: #3a2733;
    --mm-10-ink: #fbeef5;
    --mm-10-mut: #b795a8;
    --mm-10-acc: #f9a8d4;
    --mm-10-acc: oklch(80% 0.13 350);
    --mm-10-on-acc: #12100e;
    --mm-10-acc2: #c4b5fd;
    --mm-10-acc2: oklch(81% 0.1 295);
  }

  .mm-10:has(.mm-10__theme-input:checked) {
    --mm-10-bg: #fdf2f8;
    --mm-10-surf: #ffffff;
    --mm-10-line: #f3d8e6;
    --mm-10-ink: #2c1a26;
    --mm-10-mut: #7b6070;
    --mm-10-acc: #be185d;
    --mm-10-acc: oklch(52% 0.2 355);
    --mm-10-on-acc: #ffffff;
    --mm-10-acc2: #7c3aed;
    --mm-10-acc2: oklch(52% 0.24 295);
  }
}

@media (prefers-color-scheme: light) {
  .mm-10:has(.mm-10__theme-input:checked) {
    --mm-10-bg: #150d13;
    --mm-10-surf: #1f1520;
    --mm-10-line: #3a2733;
    --mm-10-ink: #fbeef5;
    --mm-10-mut: #b795a8;
    --mm-10-acc: #f9a8d4;
    --mm-10-acc: oklch(80% 0.13 350);
    --mm-10-on-acc: #12100e;
    --mm-10-acc2: #c4b5fd;
    --mm-10-acc2: oklch(81% 0.1 295);
  }
}

.mm-10__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-10__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-10__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mm-10-line);
  border-radius: 999px;
  background: var(--mm-10-surf);
  color: var(--mm-10-ink);
  cursor: pointer;
  box-shadow: 0 10px 24px -14px rgba(44, 26, 38, 0.6);
}

.mm-10__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-10__theme-input:focus-visible + .mm-10__theme-label {
  outline: 2px solid var(--mm-10-acc);
  outline-offset: 3px;
}

.mm-10__stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  place-items: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(3.5rem, 9vw, 5rem) clamp(0.75rem, 4vw, 2rem);
}

.mm-10__device {
  inline-size: min(23rem, 100%);
  border: 1px solid var(--mm-10-line);
  border-radius: var(--mm-10-radius);
  background: var(--mm-10-surf);
  box-shadow: 0 40px 90px -44px rgba(44, 26, 38, 0.7);
  overflow: hidden;
}

.mm-10__status {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.6rem 1.2rem 0.2rem;
  font: 700 0.76rem/1 var(--mm-10-font-display);
  color: var(--mm-10-mut);
}

.mm-10__status-dots {
  inline-size: 40px;
  block-size: 6px;
  border-radius: 999px;
  background: color-mix(in oklab, var(--mm-10-ink) 18%, transparent);
}

.mm-10__header {
  position: relative;
  z-index: 5;
}

.mm-10__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
  padding: 0.35rem 0.7rem;
}

.mm-10__brand {
  color: var(--mm-10-acc);
  text-decoration: none;
  font: 800 1.1rem/1 var(--mm-10-font-display);
  letter-spacing: 0.16em;
}

.mm-10__icon {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  color: var(--mm-10-ink);
}

.mm-10__icon svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-10__nav {
  padding: 0.25rem 0.7rem 0.7rem;
}

.mm-10__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.4rem;
}

.mm-10__item {
  position: relative;
  min-inline-size: 0;
}

.mm-10__trigger {
  inline-size: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
  min-block-size: 48px;
  padding-inline: 0.9rem;
  border: 1px solid var(--mm-10-line);
  border-radius: 16px;
  background: var(--mm-10-surf);
  color: var(--mm-10-ink);
  font: 700 0.98rem/1 var(--mm-10-font-display);
  cursor: pointer;
  touch-action: manipulation;
}

.mm-10__chev {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 200ms ease;
}

.mm-10__item--open > .mm-10__trigger,
.mm-10__item:hover > .mm-10__trigger,
.mm-10__item:focus-within > .mm-10__trigger {
  background: color-mix(in oklab, var(--mm-10-acc) 14%, var(--mm-10-surf));
  border-color: color-mix(in oklab, var(--mm-10-acc) 40%, var(--mm-10-line));
  color: var(--mm-10-acc);
}

.mm-10__item--open > .mm-10__trigger .mm-10__chev,
.mm-10__item:hover > .mm-10__trigger .mm-10__chev,
.mm-10__item:focus-within > .mm-10__trigger .mm-10__chev {
  transform: rotate(180deg);
}

.mm-10__panel {
  position: relative;
  display: none;
  margin-block-start: 0.4rem;
  padding: 0.5rem;
  border-radius: 16px;
  background: color-mix(in oklab, var(--mm-10-acc2) 9%, var(--mm-10-surf));
}

.mm-10__item--open > .mm-10__panel,
.mm-10__item:focus-within > .mm-10__panel {
  display: block;
}

@media (hover: hover) and (pointer: fine) {
  .mm-10__item:hover > .mm-10__panel {
    display: block;
  }
}

.mm-10__overview {
  display: grid;
  gap: 1px;
  min-block-size: 54px;
  align-content: center;
  padding: 0.4rem 0.8rem;
  border-radius: 12px;
  background: var(--mm-10-acc);
  color: var(--mm-10-on-acc);
  text-decoration: none;
}

.mm-10__overview b {
  font: 700 0.94rem/1.2 var(--mm-10-font-display);
}

.mm-10__overview span {
  font-size: 0.72rem;
  opacity: 0.88;
}

.mm-10__links {
  list-style: none;
  margin: 0.35rem 0 0;
  padding: 0;
  display: grid;
  gap: 2px;
}

.mm-10__links a {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
  min-block-size: 48px;
  padding-inline: 0.8rem;
  border-radius: 12px;
  color: var(--mm-10-ink);
  text-decoration: none;
  font-size: 0.92rem;
}

.mm-10__links a span {
  font: 700 0.72rem/1 var(--mm-10-font-display);
  color: var(--mm-10-mut);
}

.mm-10__links a:hover {
  background: color-mix(in oklab, var(--mm-10-acc) 12%, transparent);
}

.mm-10__page {
  padding: 0.25rem 0.7rem 1rem;
  display: grid;
  gap: 0.6rem;
}

.mm-10__promo {
  margin: 0;
  display: grid;
  place-items: center;
  min-block-size: 34px;
  border-radius: 999px;
  background: color-mix(in oklab, var(--mm-10-acc2) 16%, transparent);
  font: 700 0.72rem/1 var(--mm-10-font-display);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--mm-10-acc2);
}

.mm-10__tile {
  display: grid;
  gap: 2px;
  padding: 1.1rem 1.2rem;
  border-radius: 20px;
  background: linear-gradient(150deg, color-mix(in oklab, var(--mm-10-acc) 22%, transparent), color-mix(in oklab, var(--mm-10-acc2) 20%, transparent));
}

.mm-10__tile-k {
  margin: 0;
  font: 700 0.68rem/1 var(--mm-10-font-display);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--mm-10-acc);
}

.mm-10__tile-h {
  margin: 0;
  font: 800 1.5rem/1.1 var(--mm-10-font-display);
  letter-spacing: -0.02em;
}

.mm-10__tile-m {
  margin: 0;
  font-size: 0.85rem;
  color: var(--mm-10-mut);
}

@media (prefers-reduced-motion: reduce) {
  .mm-10__chev {
    transition-duration: 1ms;
  }
}
/* Entry signature — rows fall downward out of the trigger, tuned for touch */

.mm-10__links li {
  opacity: 0;
  translate: 0 -8px;
  transition: opacity 180ms ease, translate 280ms cubic-bezier(0.22, 1, 0.36, 1);
}

.mm-10__item:hover > .mm-10__panel .mm-10__links li,
.mm-10__item:focus-within > .mm-10__panel .mm-10__links li,
.mm-10__item--open > .mm-10__panel .mm-10__links li {
  opacity: 1;
  translate: 0 0;
}

.mm-10__links li:nth-child(1) {
  transition-delay: 20ms;
}

.mm-10__links li:nth-child(2) {
  transition-delay: 65ms;
}

.mm-10__links li:nth-child(3) {
  transition-delay: 110ms;
}

.mm-10__links li:nth-child(4) {
  transition-delay: 155ms;
}

.mm-10__links li:nth-child(5) {
  transition-delay: 200ms;
}

.mm-10__links li:nth-child(6) {
  transition-delay: 245ms;
}

.mm-10__links li:nth-child(n+7) {
  transition-delay: 245ms;
}

@media (prefers-reduced-motion: reduce) {
  .mm-10__links li {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-10__links li {
    opacity: 1;
    translate: none;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.mm-10');
const nav = root.querySelector('.mm-10__nav');

const setOpen = (item, on) => { item.classList.toggle('mm-10__item--open', on); item.querySelector('.mm-10__trigger').setAttribute('aria-expanded', String(on)); };
const closeAll = () => nav.querySelectorAll('.mm-10__item--open').forEach((i) => setOpen(i, false));
const toggle = (item) => { const open = item.classList.contains('mm-10__item--open'); closeAll(); setOpen(item, !open); };

const onPointerDown = (e) => {
  const trigger = e.target.closest('[data-mm-10-tap]');
  if (!trigger) return;
  if (e.pointerType !== 'mouse') e.preventDefault();
  toggle(trigger.closest('.mm-10__item'));
};
const onKey = (e) => {
  const item = e.target.closest('.mm-10__item');
  if (!item) return;
  if (e.key === 'Escape') { setOpen(item, false); item.querySelector('.mm-10__trigger').focus(); }
  if ((e.key === 'Enter' || e.key === ' ') && e.target.matches('[data-mm-10-tap]')) { e.preventDefault(); toggle(item); }
};

nav.addEventListener('pointerdown', onPointerDown);
nav.addEventListener('keydown', onKey);

root.__mmCleanup = () => {
  nav.removeEventListener('pointerdown', onPointerDown);
  nav.removeEventListener('keydown', onKey);
};
```
