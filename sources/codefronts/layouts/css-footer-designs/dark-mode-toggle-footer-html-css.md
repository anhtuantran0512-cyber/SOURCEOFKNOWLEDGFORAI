---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/dark-mode-toggle-footer-html-css/"
title: "Dark Mode Toggle Footer HTML CSS"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "A theme switch that lives where users actually look for it — in the footer — and does it the 2026 way: color-scheme plus the light-dark() function, so a…"
has_js: "true"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Toggle Footer HTML CSS
Source: https://codefronts.com/layouts/css-footer-designs/dark-mode-toggle-footer-html-css/

A theme switch that lives where users actually look for it — in the footer — and does it the 2026 way: color-scheme plus the light-dark() function, so a single token list serves both themes with no duplicated [data-theme="dark"] block. Three states, because "follow my system" is a real preference and a two-state toggle silently overrides it.
## HTML
```html
<section class="ft-06" aria-label="Dark mode toggle footer demo">
  <main class="ft-06__main">
    <p class="ft-06__eyebrow">color-scheme · light-dark()</p>
    <h1 class="ft-06__title">One token list. Two themes. Three states.</h1>
    <p class="ft-06__sub">Every colour below is declared once with <code>light-dark()</code>. The switch in the footer changes <code>color-scheme</code>, which repaints the tokens, the scrollbar and the form controls together.</p>
    <div class="ft-06__demo">
      <label class="ft-06__field"><span>Native control, native theme</span><input class="ft-06__input" type="text" value="[email protected]" aria-label="Sample input"></label>
      <div class="ft-06__swatches" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
    </div>
  </main>
  <footer class="ft-06__foot">
    <div class="ft-06__brand"><span class="ft-06__mark" aria-hidden="true"></span>Lumen</div>
    <nav class="ft-06__nav" aria-label="Footer">
      <a class="ft-06__link" href="#ft-06-a">Docs</a>
      <a class="ft-06__link" href="#ft-06-a">Components</a>
      <a class="ft-06__link" href="#ft-06-a">Tokens</a>
      <a class="ft-06__link" href="#ft-06-a">GitHub</a>
    </nav>
    <div class="ft-06__theme" role="group" aria-label="Colour theme">
      <span class="ft-06__thumb" aria-hidden="true"></span>
      <button class="ft-06__opt" type="button" data-theme-set="light" aria-pressed="false"><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4"/></svg>Light</button>
      <button class="ft-06__opt" type="button" data-theme-set="auto" aria-pressed="true"><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M8 20h8"/></svg>Auto</button>
      <button class="ft-06__opt" type="button" data-theme-set="dark" aria-pressed="false"><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z"/></svg>Dark</button>
    </div>
    <p class="ft-06__copy">© <time datetime="2026">2026</time> Lumen UI</p>
    <p class="ft-06__live" id="ft-06-live" role="status" aria-live="polite"></p>
  </footer>
</section>
```
## CSS
```css
.ft-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  color-scheme: light dark;
  --ft-06-bg: light-dark(oklch(0.98 0.004 250),oklch(0.16 0.018 265));
  --ft-06-surface: light-dark(oklch(1 0 0),oklch(0.21 0.02 265));
  --ft-06-ink: light-dark(oklch(0.21 0.02 265),oklch(0.96 0.005 265));
  --ft-06-mut: light-dark(oklch(0.53 0.018 265),oklch(0.72 0.015 265));
  --ft-06-acc: light-dark(oklch(0.55 0.19 285),oklch(0.78 0.15 285));
  --ft-06-line: light-dark(oklch(0.21 0.02 265/.12),oklch(0.96 0.005 265/.14));
  background: var(--ft-06-bg);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-06-ink);
  -webkit-font-smoothing: antialiased;
  transition: background .35s ease,color .35s ease;
}

.ft-06[data-theme="light"] {
  color-scheme: light;
}

.ft-06[data-theme="dark"] {
  color-scheme: dark;
}

.ft-06 *,
.ft-06 *::before,
.ft-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-06__main {
  display: grid;
  align-content: center;
  gap: 16px;
  padding-block: clamp(44px,9vh,100px);
  padding-inline: max(clamp(20px,5vw,44px),calc((100% - 1000px)/2));
  background: radial-gradient(70% 55% at 85% 5%,color-mix(in oklch,var(--ft-06-acc) 16%,transparent),transparent);
}

.ft-06__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--ft-06-acc);
}

.ft-06__title {
  font-size: clamp(30px,5.6vw,58px);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 16ch;
  text-wrap: balance;
}

.ft-06__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-06-mut);
  max-width: 58ch;
  text-wrap: pretty;
}

.ft-06__sub code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  padding: 2px 6px;
  border-radius: 5px;
  background: color-mix(in oklch,var(--ft-06-ink) 8%,transparent);
}

.ft-06__demo {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 18px;
  margin-block-start: 8px;
}

.ft-06__field {
  display: grid;
  gap: 6px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .02em;
  color: var(--ft-06-mut);
}

.ft-06__input {
  min-height: 44px;
  padding: 0 14px;
  border-radius: 11px;
  border: 1px solid var(--ft-06-line);
  background: var(--ft-06-surface);
  color: var(--ft-06-ink);
  font: inherit;
  font-size: 14.5px;
  min-width: 16rem;
}

.ft-06__input:focus-visible {
  outline: 2px solid var(--ft-06-acc);
  outline-offset: 2px;
}

.ft-06__swatches {
  display: flex;
  gap: 6px;
}

.ft-06__swatches i {
  width: 34px;
  height: 34px;
  border-radius: 9px;
  border: 1px solid var(--ft-06-line);
}

.ft-06__swatches i:nth-child(1) {
  background: var(--ft-06-bg);
}

.ft-06__swatches i:nth-child(2) {
  background: var(--ft-06-surface);
}

.ft-06__swatches i:nth-child(3) {
  background: var(--ft-06-mut);
}

.ft-06__swatches i:nth-child(4) {
  background: var(--ft-06-ink);
}

.ft-06__swatches i:nth-child(5) {
  background: var(--ft-06-acc);
}

.ft-06__foot {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 14px clamp(16px,2.5vw,28px);
  padding-block: 18px;
  padding-bottom: calc(18px + env(safe-area-inset-bottom,0px));
  padding-inline: max(clamp(20px,5vw,44px),calc((100% - 1000px)/2));
  background: var(--ft-06-surface);
  border-top: 1px solid var(--ft-06-line);
}

.ft-06__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.ft-06__mark {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: conic-gradient(from 0deg,var(--ft-06-acc),oklch(0.75 0.15 200),var(--ft-06-acc));
  box-shadow: 0 0 16px -4px var(--ft-06-acc);
}

.ft-06__nav {
  display: flex;
  flex-wrap: wrap;
  gap: 2px;
}

.ft-06__link {
  display: flex;
  align-items: center;
  min-height: 40px;
  padding: 0 11px;
  border-radius: 9px;
  font-size: 14px;
  font-weight: 600;
  color: var(--ft-06-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.ft-06__link:hover {
  color: var(--ft-06-ink);
  background: color-mix(in oklch,var(--ft-06-ink) 6%,transparent);
}

.ft-06__theme {
  position: relative;
  display: flex;
  gap: 2px;
  margin-inline-start: auto;
  padding: 4px;
  border-radius: 13px;
  background: color-mix(in oklch,var(--ft-06-ink) 6%,transparent);
  border: 1px solid var(--ft-06-line);
}

.ft-06__thumb {
  position: absolute;
  inset-block: 4px;
  left: 4px;
  width: calc((100% - 8px)/3);
  border-radius: 10px;
  background: var(--ft-06-surface);
  box-shadow: 0 2px 8px -3px oklch(0 0 0/.35);
  translate: calc(var(--ft-06-i,1) * 100%) 0;
  transition: translate .32s cubic-bezier(.2,.8,.2,1);
}

.ft-06__opt {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  min-height: 38px;
  padding: 0 13px;
  border: 0;
  border-radius: 10px;
  background: transparent;
  font: inherit;
  font-size: 13px;
  font-weight: 600;
  color: var(--ft-06-mut);
  cursor: pointer;
  transition: color .2s ease;
}

.ft-06__opt[aria-pressed="true"] {
  color: var(--ft-06-acc);
}

.ft-06__opt:hover {
  color: var(--ft-06-ink);
}

.ft-06__opt:focus-visible,
.ft-06__link:focus-visible {
  outline: 2px solid var(--ft-06-acc);
  outline-offset: 2px;
}

.ft-06__copy {
  font-size: 13px;
  color: var(--ft-06-mut);
}

.ft-06__live {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@media (max-width: 820px) {
  .ft-06__theme {
    margin-inline-start: 0;
    order: 4;
  }

  .ft-06__copy {
    order: 5;
    margin-inline-start: auto;
  }
}

@media (max-width: 480px) {
  .ft-06__theme {
    width: 100%;
  }

  .ft-06__opt {
    flex: 1;
    justify-content: center;
  }
}

@supports not (color: light-dark(#fff,#000)) {
  .ft-06 {
    --ft-06-bg: oklch(0.98 0.004 250);
    --ft-06-surface: oklch(1 0 0);
    --ft-06-ink: oklch(0.21 0.02 265);
    --ft-06-mut: oklch(0.53 0.018 265);
    --ft-06-acc: oklch(0.55 0.19 285);
    --ft-06-line: oklch(0.21 0.02 265/.12);
  }

  @media (prefers-color-scheme: dark) {
    .ft-06:not([data-theme="light"]) {
      --ft-06-bg: oklch(0.16 0.018 265);
      --ft-06-surface: oklch(0.21 0.02 265);
      --ft-06-ink: oklch(0.96 0.005 265);
      --ft-06-mut: oklch(0.72 0.015 265);
      --ft-06-acc: oklch(0.78 0.15 285);
      --ft-06-line: oklch(0.96 0.005 265/.14);
    }
  }

  .ft-06[data-theme="dark"] {
    --ft-06-bg: oklch(0.16 0.018 265);
    --ft-06-surface: oklch(0.21 0.02 265);
    --ft-06-ink: oklch(0.96 0.005 265);
    --ft-06-mut: oklch(0.72 0.015 265);
    --ft-06-acc: oklch(0.78 0.15 285);
    --ft-06-line: oklch(0.96 0.005 265/.14);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-06 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ft-06');
  if (!root || root.dataset.ready) return;
  root.dataset.ready = '1';
  const KEY = 'ft-06-theme';
  const opts = [...root.querySelectorAll('.ft-06__opt')];
  const live = root.querySelector('#ft-06-live');
  const order = ['light', 'auto', 'dark'];
  const apply = (mode, announce) => {
    if (mode === 'auto') root.removeAttribute('data-theme');
    else root.dataset.theme = mode;
    root.style.setProperty('--ft-06-i', order.indexOf(mode));
    opts.forEach((o) => o.setAttribute('aria-pressed', String(o.dataset.themeSet === mode)));
    try { localStorage.setItem(KEY, mode); } catch (e) {}
    if (announce) live.textContent = 'Theme set to ' + mode;
  };
  const set = (mode) => {
    if (document.startViewTransition && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
      document.startViewTransition(() => apply(mode, true));
    } else apply(mode, true);
  };
  opts.forEach((o) => o.addEventListener('click', () => set(o.dataset.themeSet)));
  let saved = 'auto';
  try { saved = localStorage.getItem(KEY) || 'auto'; } catch (e) {}
  apply(order.includes(saved) ? saved : 'auto', false);
})();
```
