---
source: "codefronts"
url: "https://codefronts.com/snippets/css-variable-dark-mode-system/data-theme-toggle-with-localstorage/"
title: "CSS Variable Dark Mode Toggle with data-theme Attribute and localStorage Persistence"
section: "snippets"
category: "css-variable-dark-mode-system"
category_name: "CSS Variable Dark Mode Systems"
description: "The interactive header switch users actually expect: one button flips data-theme=\"dark\" on the root, CSS swaps the five variables instantly, and the choice…"
has_js: "true"
---

Here's a working CSS Variable Dark Mode System from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Variable Dark Mode Toggle with data-theme Attribute and localStorage Persistence
Source: https://codefronts.com/snippets/css-variable-dark-mode-system/data-theme-toggle-with-localstorage/

The interactive header switch users actually expect: one button flips data-theme="dark" on the root, CSS swaps the five variables instantly, and the choice is saved to localStorage so it survives reloads and navigation. About ten lines of vanilla JS — no framework, no ThemeProvider, no dependency.
## HTML
```html
<section class="cdm-02" data-theme="light">
  <header class="cdm-02__bar">
    <span class="cdm-02__brand"><span class="cdm-02__mark" aria-hidden="true"></span>Aurora Docs</span>
    <button class="cdm-02__toggle" type="button" aria-pressed="false">
      <span class="cdm-02__icons" aria-hidden="true">
        <svg class="cdm-02__sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4.5"/><path d="M12 1.5v3m0 15v3M1.5 12h3m15 0h3M4.6 4.6l2.1 2.1m10.6 10.6 2.1 2.1m0-14.8-2.1 2.1M6.7 17.3l-2.1 2.1"/></svg>
        <svg class="cdm-02__moon" viewBox="0 0 24 24"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5Z"/></svg>
      </span>
      <span class="cdm-02__label">Dark</span>
    </button>
  </header>
  <main class="cdm-02__body">
    <h1>Ship a toggle in ten lines</h1>
    <p>Click the switch. Your choice is written to <code>localStorage</code>, so it sticks on reload — CSS handles every color from five variables.</p>
    <div class="cdm-02__row">
      <input class="cdm-02__field" type="text" placeholder="Native input follows the theme" aria-label="Demo input">
      <a class="cdm-02__cta" href="#">Read the guide</a>
    </div>
  </main>
</section>
```
## CSS
```css
.cdm-02,
.cdm-02 *,
.cdm-02 *::before,
.cdm-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdm-02 {
  --bg: oklch(0.98 0.004 250);
  --surface: oklch(1 0 0);
  --text: oklch(0.24 0.02 265);
  --border: oklch(0.9 0.008 265);
  --accent: oklch(0.55 0.19 292);
  --muted: color-mix(in oklab,var(--text) 60%,var(--bg));
  --hover: color-mix(in oklab,var(--text) 7%,transparent);
  color-scheme: light;
  display: flex;
  flex-direction: column;
  width: 100%;
  min-height: 100vh;
  min-height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--text);
  transition: background-color .3s ease,color .3s ease;
}

.cdm-02[data-theme="dark"] {
  --bg: oklch(0.16 0.02 292);
  --surface: oklch(0.21 0.02 292);
  --text: oklch(0.95 0.005 292);
  --border: oklch(0.32 0.02 292);
  --accent: oklch(0.74 0.16 292);
  color-scheme: dark;
}

.cdm-02__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 24px;
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  transition: background-color .3s ease,border-color .3s ease;
}

.cdm-02__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font: 700 16px/1 system-ui,sans-serif;
}

.cdm-02__mark {
  width: 24px;
  height: 24px;
  border-radius: 7px;
  background: conic-gradient(from 200deg,var(--accent),oklch(from var(--accent) l c calc(h + 60)));
}

.cdm-02__toggle {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-height: 44px;
  padding: 0 16px;
  border: 1px solid var(--border);
  border-radius: 999px;
  background: var(--bg);
  color: var(--text);
  font: 600 13px/1 system-ui,sans-serif;
  cursor: pointer;
  transition: background-color .2s ease,border-color .2s ease;
}

.cdm-02__toggle:hover {
  background: var(--hover);
}

.cdm-02__toggle:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cdm-02__icons {
  position: relative;
  display: inline-block;
  width: 17px;
  height: 17px;
  flex-shrink: 0;
}

.cdm-02__toggle svg {
  position: absolute;
  inset: 0;
  width: 17px;
  height: 17px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.9;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: opacity .25s ease,transform .25s ease;
}

.cdm-02__moon {
  opacity: 0;
  transform: rotate(-40deg);
}

.cdm-02[data-theme="dark"] .cdm-02__sun {
  opacity: 0;
  transform: rotate(40deg);
}

.cdm-02[data-theme="dark"] .cdm-02__moon {
  opacity: 1;
  transform: rotate(0);
}

.cdm-02__body {
  flex: 1;
  display: grid;
  align-content: center;
  gap: 16px;
  max-width: 620px;
  padding: 48px 24px;
}

.cdm-02__body h1 {
  font: 700 clamp(24px,4vw,34px)/1.15 system-ui,sans-serif;
  letter-spacing: -.01em;
}

.cdm-02__body p {
  font: 400 15px/1.65 system-ui,sans-serif;
  color: var(--muted);
  text-wrap: pretty;
}

.cdm-02__body code {
  font: 600 13px/1 ui-monospace,Menlo,monospace;
  padding: 2px 6px;
  border-radius: 5px;
  background: var(--hover);
  color: var(--text);
}

.cdm-02__row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 8px;
}

.cdm-02__field {
  flex: 1;
  min-width: 220px;
  min-height: 44px;
  padding: 0 14px;
  border: 1px solid var(--border);
  border-radius: 10px;
  background: var(--surface);
  color: var(--text);
  font: 400 14px/1 system-ui,sans-serif;
}

.cdm-02__field:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
  border-color: var(--accent);
}

.cdm-02__cta {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 22px;
  border-radius: 10px;
  font: 600 14px/1 system-ui,sans-serif;
  text-decoration: none;
  color: #fff;
  background: var(--accent);
  transition: filter .2s ease;
}

.cdm-02__cta:hover {
  filter: brightness(1.08);
}

.cdm-02__cta:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .cdm-02,
    .cdm-02 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
(function () {
  var KEY = 'cf-theme';
  var root = document.querySelector('.cdm-02');
  var btn  = root.querySelector('.cdm-02__toggle');
  var lbl  = root.querySelector('.cdm-02__label');

  // restore saved choice (falls back to the light default)
  try { var saved = localStorage.getItem(KEY); if (saved) root.dataset.theme = saved; } catch (e) {}

  function sync() {
    var dark = root.dataset.theme === 'dark';
    btn.setAttribute('aria-pressed', String(dark));
    lbl.textContent = dark ? 'Light' : 'Dark';
  }
  sync();

  btn.addEventListener('click', function () {
    var next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem(KEY, next); } catch (e) {}
    sync();
  });
})();
```
