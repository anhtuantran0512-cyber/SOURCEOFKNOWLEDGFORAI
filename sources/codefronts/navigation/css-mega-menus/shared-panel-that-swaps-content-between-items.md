---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/shared-panel-that-swaps-content-between-items/"
title: "Shared Panel That Swaps Content Between Items"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "Instead of one panel per nav item, a single container swaps its contents as the active item changes."
has_js: "true"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Shared Panel That Swaps Content Between Items
Source: https://codefronts.com/navigation/css-mega-menus/shared-panel-that-swaps-content-between-items/

Instead of one panel per nav item, a single container swaps its contents as the active item changes. That keeps the open and close animation continuous when moving between items rather than closing and reopening, and it is what most large sites actually ship. Built here as a streaming service header, with the sections pre-rendered and toggled through the hidden attribute so focus survives every swap.
## HTML
```html
<section class="mm-12" aria-labelledby="mm-12-title">
  <h2 class="mm-12__sr" id="mm-12-title">Prism TV</h2>

  <div class="mm-12__theme">
    <input class="mm-12__theme-input" type="checkbox" id="mm-12-theme">
    <label class="mm-12__theme-label" for="mm-12-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-12__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="mm-12__shell">
    <div class="mm-12__bar">
      <a class="mm-12__brand" href="#mm-12-title">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3 3 19h18Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M12 9v10" stroke="currentColor" stroke-width="1.2" opacity=".6"/></svg>
        Prism<b>TV</b>
      </a>

      <nav class="mm-12__nav" aria-label="Primary">
        <ul class="mm-12__list">
          <li><button class="mm-12__trigger" type="button" data-mm12-for="mm-12-sec-browse" aria-expanded="false" aria-controls="mm-12-panel">Browse</button></li>
          <li><button class="mm-12__trigger" type="button" data-mm12-for="mm-12-sec-live" aria-expanded="false" aria-controls="mm-12-panel">Live</button></li>
          <li><button class="mm-12__trigger" type="button" data-mm12-for="mm-12-sec-kids" aria-expanded="false" aria-controls="mm-12-panel">Kids</button></li>
          <li><a class="mm-12__plain" href="#mm-12-title">My list</a></li>
        </ul>
      </nav>

      <div class="mm-12__utils">
        <span class="mm-12__search" aria-hidden="true">
          <svg viewBox="0 0 24 24" focusable="false"><circle cx="11" cy="11" r="6.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        </span>
        <span class="mm-12__avatar" aria-hidden="true">SR</span>
      </div>
    </div>

    <div class="mm-12__panel" id="mm-12-panel" aria-label="Browse">
      <div class="mm-12__sections">
        <div class="mm-12__rail" role="presentation">
          <span class="mm-12__rail-tab" data-mm12-tab="mm-12-sec-browse">Browse</span>
          <span class="mm-12__rail-tab" data-mm12-tab="mm-12-sec-live">Live</span>
          <span class="mm-12__rail-tab" data-mm12-tab="mm-12-sec-kids">Kids</span>
        </div>

        <section class="mm-12__section" id="mm-12-sec-browse" aria-label="Browse">
          <div class="mm-12__cols">
            <div class="mm-12__col">
              <h3 class="mm-12__col-head">Genres</h3>
              <ul class="mm-12__links"><li><a href="#mm-12-title">Drama</a></li><li><a href="#mm-12-title">Documentary</a></li><li><a href="#mm-12-title">Comedy</a></li><li><a href="#mm-12-title">Thriller</a></li></ul>
            </div>
            <div class="mm-12__col">
              <h3 class="mm-12__col-head">Collections</h3>
              <ul class="mm-12__links"><li><a href="#mm-12-title">Prism Originals</a></li><li><a href="#mm-12-title">Award winners</a></li><li><a href="#mm-12-title">Leaving soon</a></li></ul>
            </div>
            <ul class="mm-12__tiles">
              <li><a href="#mm-12-title"><span class="mm-12__art mm-12__art--a" aria-hidden="true"></span><b>Northwind</b><span>S2 &middot; new episode</span></a></li>
              <li><a href="#mm-12-title"><span class="mm-12__art mm-12__art--b" aria-hidden="true"></span><b>The Long Coast</b><span>Documentary</span></a></li>
              <li><a href="#mm-12-title"><span class="mm-12__art mm-12__art--c" aria-hidden="true"></span><b>Basalt</b><span>Limited series</span></a></li>
            </ul>
          </div>
        </section>

        <section class="mm-12__section" id="mm-12-sec-live" aria-label="Live" hidden>
          <div class="mm-12__cols">
            <div class="mm-12__col">
              <h3 class="mm-12__col-head">Channels</h3>
              <ul class="mm-12__links"><li><a href="#mm-12-title">Prism One</a></li><li><a href="#mm-12-title">Prism News</a></li><li><a href="#mm-12-title">Prism Sport</a></li></ul>
            </div>
            <div class="mm-12__col">
              <h3 class="mm-12__col-head">Tonight</h3>
              <ul class="mm-12__links"><li><a href="#mm-12-title">20:00 &mdash; Match of the week</a></li><li><a href="#mm-12-title">21:30 &mdash; Late review</a></li></ul>
            </div>
            <ul class="mm-12__tiles">
              <li><a href="#mm-12-title"><span class="mm-12__art mm-12__art--d" aria-hidden="true"></span><b>On now</b><span>Prism News at Six</span></a></li>
              <li><a href="#mm-12-title"><span class="mm-12__art mm-12__art--a" aria-hidden="true"></span><b>Up next</b><span>Coastal Rescue</span></a></li>
            </ul>
          </div>
        </section>

        <section class="mm-12__section" id="mm-12-sec-kids" aria-label="Kids" hidden>
          <div class="mm-12__cols">
            <div class="mm-12__col">
              <h3 class="mm-12__col-head">Ages</h3>
              <ul class="mm-12__links"><li><a href="#mm-12-title">Under 5</a></li><li><a href="#mm-12-title">5 to 8</a></li><li><a href="#mm-12-title">9 and up</a></li></ul>
            </div>
            <div class="mm-12__col">
              <h3 class="mm-12__col-head">Controls</h3>
              <ul class="mm-12__links"><li><a href="#mm-12-title">Profile PIN</a></li><li><a href="#mm-12-title">Watch limits</a></li></ul>
            </div>
            <ul class="mm-12__tiles">
              <li><a href="#mm-12-title"><span class="mm-12__art mm-12__art--e" aria-hidden="true"></span><b>Fern and Friends</b><span>S4</span></a></li>
              <li><a href="#mm-12-title"><span class="mm-12__art mm-12__art--b" aria-hidden="true"></span><b>Orbit Explorers</b><span>New</span></a></li>
            </ul>
          </div>
        </section>
      </div>
    </div>
  </header>

  <main class="mm-12__page">
    <p class="mm-12__continue">Continue watching</p>
    <div class="mm-12__row">
      <span class="mm-12__thumb mm-12__art--c" aria-hidden="true"></span>
      <span class="mm-12__thumb mm-12__art--a" aria-hidden="true"></span>
      <span class="mm-12__thumb mm-12__art--d" aria-hidden="true"></span>
      <span class="mm-12__thumb mm-12__art--b" aria-hidden="true"></span>
    </div>
  </main>
</section>
```
## CSS
```css
.mm-12 {
  --mm-12-bg: #070a14;
  --mm-12-solid: #101728;
  --mm-12-surf: rgba(16, 23, 40, 0.72);
  --mm-12-surf: color-mix(in oklab, #101728 76%, transparent);
  --mm-12-line: #223052;
  --mm-12-ink: #e9eefb;
  --mm-12-mut: #93a3c6;
  --mm-12-acc: #6aa8ff;
  --mm-12-acc: oklch(74% 0.15 258);
  --mm-12-blur: 16px;
  --mm-12-swap: 280ms;
  --mm-12-font-display: "Helvetica Neue", "Inter", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background-color: var(--mm-12-bg);
  background-image: radial-gradient(60rem 30rem at 18% -8%, rgba(106, 168, 255, 0.22), transparent 62%), radial-gradient(52rem 26rem at 92% 6%, rgba(168, 85, 247, 0.18), transparent 60%);
  color: var(--mm-12-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.mm-12 *,
.mm-12 *::before,
.mm-12 *::after {
  box-sizing: border-box;
}

.mm-12 :focus-visible {
  outline: 2px solid var(--mm-12-acc);
  outline-offset: 3px;
  border-radius: 8px;
}

.mm-12__sr {
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

.mm-12:has(.mm-12__theme-input:checked) {
  --mm-12-bg: #eef2fb;
  --mm-12-solid: #ffffff;
  --mm-12-surf: rgba(255, 255, 255, 0.8);
  --mm-12-surf: color-mix(in oklab, #ffffff 80%, transparent);
  --mm-12-line: #ccd8f0;
  --mm-12-ink: #0b1730;
  --mm-12-mut: #55688a;
  --mm-12-acc: #1d4ed8;
  --mm-12-acc: oklch(48% 0.21 262);
}

@media (prefers-color-scheme: light) {
  .mm-12 {
    --mm-12-bg: #eef2fb;
    --mm-12-solid: #ffffff;
    --mm-12-surf: rgba(255, 255, 255, 0.8);
    --mm-12-surf: color-mix(in oklab, #ffffff 80%, transparent);
    --mm-12-line: #ccd8f0;
    --mm-12-ink: #0b1730;
    --mm-12-mut: #55688a;
    --mm-12-acc: #1d4ed8;
    --mm-12-acc: oklch(48% 0.21 262);
  }

  .mm-12:has(.mm-12__theme-input:checked) {
    --mm-12-bg: #070a14;
    --mm-12-solid: #101728;
    --mm-12-surf: rgba(16, 23, 40, 0.72);
    --mm-12-surf: color-mix(in oklab, #101728 76%, transparent);
    --mm-12-line: #223052;
    --mm-12-ink: #e9eefb;
    --mm-12-mut: #93a3c6;
    --mm-12-acc: #6aa8ff;
    --mm-12-acc: oklch(74% 0.15 258);
  }
}

@media (prefers-color-scheme: dark) {
  .mm-12:has(.mm-12__theme-input:checked) {
    --mm-12-bg: #eef2fb;
    --mm-12-solid: #ffffff;
    --mm-12-surf: rgba(255, 255, 255, 0.8);
    --mm-12-surf: color-mix(in oklab, #ffffff 80%, transparent);
    --mm-12-line: #ccd8f0;
    --mm-12-ink: #0b1730;
    --mm-12-mut: #55688a;
    --mm-12-acc: #1d4ed8;
    --mm-12-acc: oklch(48% 0.21 262);
  }
}

.mm-12__theme {
  position: absolute;
  inset-block-start: clamp(1.5rem, 4vw, 2.2rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-12__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-12__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mm-12-line);
  border-radius: 14px;
  background: var(--mm-12-solid);
  color: var(--mm-12-ink);
  cursor: pointer;
}

.mm-12__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-12__theme-input:focus-visible + .mm-12__theme-label {
  outline: 2px solid var(--mm-12-acc);
  outline-offset: 3px;
}

.mm-12__shell {
  position: relative;
  z-index: 10;
  inline-size: min(76rem, calc(100% - 2rem));
  margin: clamp(1rem, 3vw, 1.75rem) auto 0;
  border: 1px solid var(--mm-12-line);
  border-radius: 20px;
  background: var(--mm-12-surf);
  -webkit-backdrop-filter: blur(var(--mm-12-blur));
  backdrop-filter: blur(var(--mm-12-blur));
  overflow: hidden;
  box-shadow: 0 30px 70px -42px rgba(0, 0, 0, 0.8);
}

.mm-12__bar {
  display: flex;
  align-items: center;
  gap: clamp(0.5rem, 2vw, 1.75rem);
  flex-wrap: wrap;
  min-block-size: 68px;
  padding-inline: clamp(0.85rem, 2.5vw, 1.4rem) 64px;
  border-block-end: 1px solid var(--mm-12-line);
}

.mm-12__brand {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  color: var(--mm-12-ink);
  text-decoration: none;
  font: 700 1.05rem/1 var(--mm-12-font-display);
  letter-spacing: -0.03em;
}

.mm-12__brand b {
  color: var(--mm-12-acc);
}

.mm-12__brand svg {
  inline-size: 20px;
  block-size: 20px;
  color: var(--mm-12-acc);
}

.mm-12__nav {
  min-inline-size: 0;
}

.mm-12__list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.15rem;
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
}

.mm-12__trigger,
.mm-12__plain {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.95rem;
  border: 0;
  border-radius: 10px;
  background: transparent;
  color: var(--mm-12-ink);
  font: 600 0.92rem/1 var(--mm-12-font-display);
  text-decoration: none;
  cursor: pointer;
}

.mm-12__trigger[aria-expanded="true"] {
  background: color-mix(in oklab, var(--mm-12-acc) 16%, transparent);
  color: var(--mm-12-acc);
}

.mm-12__utils {
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.mm-12__search {
  display: grid;
  place-items: center;
  inline-size: 40px;
  block-size: 40px;
  border-radius: 999px;
  border: 1px solid var(--mm-12-line);
  color: var(--mm-12-mut);
}

.mm-12__search svg {
  inline-size: 18px;
  block-size: 18px;
}

.mm-12__avatar {
  display: grid;
  place-items: center;
  inline-size: 34px;
  block-size: 34px;
  border-radius: 10px;
  background: color-mix(in oklab, var(--mm-12-acc) 24%, transparent);
  color: var(--mm-12-acc);
  font: 700 0.74rem/1 var(--mm-12-font-display);
}

.mm-12__panel {
  position: relative;
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows var(--mm-12-swap) cubic-bezier(0.22, 1, 0.36, 1);
}

.mm-12__panel--open {
  grid-template-rows: 1fr;
}

.mm-12__sections {
  min-block-size: 0;
  overflow: hidden;
}

.mm-12__rail {
  display: flex;
  gap: 0.35rem;
  flex-wrap: wrap;
  padding: 0.75rem clamp(0.85rem, 2.5vw, 1.4rem) 0;
}

.mm-12__rail-tab {
  min-block-size: 26px;
  display: inline-flex;
  align-items: center;
  padding-inline: 0.65rem;
  border-radius: 999px;
  font: 600 0.68rem/1 var(--mm-12-font-display);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--mm-12-mut);
  background: color-mix(in oklab, var(--mm-12-ink) 8%, transparent);
}

.mm-12__rail-tab[data-mm12-active] {
  background: var(--mm-12-acc);
  color: #04101f;
}

.mm-12__section {
  padding: clamp(0.9rem, 2.6vw, 1.4rem) clamp(0.85rem, 2.5vw, 1.4rem) clamp(1.1rem, 3vw, 1.6rem);
}

.mm-12__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 11rem), 1fr));
  gap: clamp(0.85rem, 2.6vw, 2rem);
}

.mm-12__col {
  min-inline-size: 0;
}

.mm-12__col-head {
  margin: 0 0 0.4rem;
  font: 700 0.68rem/1 var(--mm-12-font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--mm-12-mut);
}

.mm-12__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1px;
}

.mm-12__links a {
  display: flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.5rem;
  margin-inline: -0.5rem;
  border-radius: 8px;
  color: var(--mm-12-ink);
  text-decoration: none;
  font-size: 0.9rem;
  min-inline-size: 0;
}

.mm-12__links a:hover {
  background: color-mix(in oklab, var(--mm-12-acc) 12%, transparent);
  color: var(--mm-12-acc);
}

.mm-12__tiles {
  grid-column: span 2;
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 9rem), 1fr));
  gap: 0.6rem;
  min-inline-size: 0;
}

.mm-12__tiles a {
  display: grid;
  gap: 2px;
  color: var(--mm-12-ink);
  text-decoration: none;
  min-inline-size: 0;
}

.mm-12__art {
  display: block;
  aspect-ratio: 16 / 9;
  border-radius: 10px;
}

.mm-12__art--a {
  background: linear-gradient(140deg, #3b82f6, #8b5cf6);
}

.mm-12__art--b {
  background: linear-gradient(140deg, #0ea5e9, #14b8a6);
}

.mm-12__art--c {
  background: linear-gradient(140deg, #f43f5e, #f59e0b);
}

.mm-12__art--d {
  background: linear-gradient(140deg, #6366f1, #0ea5e9);
}

.mm-12__art--e {
  background: linear-gradient(140deg, #22c55e, #84cc16);
}

.mm-12__tiles b {
  font: 600 0.88rem/1.25 var(--mm-12-font-display);
  min-inline-size: 0;
}

.mm-12__tiles a > span:last-child {
  font-size: 0.74rem;
  color: var(--mm-12-mut);
}

.mm-12__tiles a:hover b {
  color: var(--mm-12-acc);
}

.mm-12__page {
  inline-size: min(76rem, calc(100% - 2rem));
  margin-inline: auto;
  padding-block: clamp(1.75rem, 5vw, 3rem);
}

.mm-12__continue {
  margin: 0 0 0.6rem;
  font: 700 0.72rem/1 var(--mm-12-font-display);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--mm-12-mut);
}

.mm-12__row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 11rem), 1fr));
  gap: 0.6rem;
}

.mm-12__thumb {
  display: block;
  aspect-ratio: 16 / 9;
  border-radius: 12px;
}

@media (max-width: 52rem) {
  .mm-12__bar {
    flex-direction: column;
    align-items: stretch;
    padding-block: 0.6rem;
  }

  .mm-12__list {
    flex-direction: column;
  }

  .mm-12__utils {
    margin-inline-start: 0;
  }

  .mm-12__tiles {
    grid-column: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .mm-12__panel {
    transition-duration: 1ms;
  }
}
/* Entry signature — the shared panel slides its content in laterally, columns trailing from the end edge */

.mm-12__cols {
  opacity: 0;
  translate: 18px 0;
  transition: opacity 200ms ease, translate 360ms cubic-bezier(0.22, 1, 0.36, 1);
}

.mm-12__panel--open .mm-12__cols {
  opacity: 1;
  translate: 0 0;
}

.mm-12__col {
  opacity: 0;
  translate: 12px 0;
  transition: opacity 220ms ease, translate 320ms cubic-bezier(0.22, 1, 0.36, 1);
}

.mm-12__panel--open .mm-12__col {
  opacity: 1;
  translate: 0 0;
}

.mm-12__panel--open .mm-12__col:nth-last-child(1) {
  transition-delay: 40ms;
}

.mm-12__panel--open .mm-12__col:nth-last-child(2) {
  transition-delay: 90ms;
}

.mm-12__panel--open .mm-12__col:nth-last-child(3) {
  transition-delay: 140ms;
}

.mm-12__panel--open .mm-12__col:nth-last-child(n+4) {
  transition-delay: 190ms;
}

@media (prefers-reduced-motion: reduce) {
  .mm-12__cols,
    .mm-12__col {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-12__cols,
    .mm-12__col {
    opacity: 1;
    translate: none;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.mm-12');
const shell = root.querySelector('.mm-12__shell');
const nav = root.querySelector('.mm-12__nav');
const panel = root.querySelector('.mm-12__panel');
const triggers = Array.from(nav.querySelectorAll('.mm-12__trigger'));
const tabs = Array.from(root.querySelectorAll('[data-mm12-tab]'));
const canHover = window.matchMedia('(hover: hover)');

const show = (id, trigger) => {
  root.querySelectorAll('.mm-12__section').forEach((s) => { s.hidden = s.id !== id; });
  tabs.forEach((t) => t.toggleAttribute('data-mm12-active', t.dataset.mm12Tab === id));
  triggers.forEach((t) => t.setAttribute('aria-expanded', String(t === trigger)));
  panel.classList.add('mm-12__panel--open');
  panel.setAttribute('aria-label', trigger.textContent.trim());
};
const close = () => {
  panel.classList.remove('mm-12__panel--open');
  triggers.forEach((t) => t.setAttribute('aria-expanded', 'false'));
};

const onClick = (e) => {
  const t = e.target.closest('.mm-12__trigger');
  if (!t) return;
  // Hover already opened this section; a click must not close it again.
  if (t.getAttribute('aria-expanded') === 'true') { if (!canHover.matches) close(); return; }
  show(t.dataset.mm12For, t);
};
const onOver = (e) => {
  if (!canHover.matches) return;
  const t = e.target.closest('.mm-12__trigger');
  if (t) show(t.dataset.mm12For, t);
};
const onLeave = () => { if (!shell.contains(document.activeElement)) close(); };
const onKey = (e) => {
  if (e.key !== 'Escape') return;
  const active = triggers.find((t) => t.getAttribute('aria-expanded') === 'true');
  close();
  if (active) active.focus();
};
const onFocusOut = (e) => { if (!e.relatedTarget || !shell.contains(e.relatedTarget)) close(); };

nav.addEventListener('click', onClick);
nav.addEventListener('pointerover', onOver);
shell.addEventListener('pointerleave', onLeave);
shell.addEventListener('keydown', onKey);
shell.addEventListener('focusout', onFocusOut);

root.__mmCleanup = () => {
  nav.removeEventListener('click', onClick);
  nav.removeEventListener('pointerover', onOver);
  shell.removeEventListener('pointerleave', onLeave);
  shell.removeEventListener('keydown', onKey);
  shell.removeEventListener('focusout', onFocusOut);
};
```
