---
source: "codefronts"
url: "https://codefronts.com/snippets/css-variable-dark-mode-system/three-way-system-light-dark-switcher/"
title: "Three-Way Theme Switcher (System, Light, Dark) with matchMedia and CSS Custom Properties"
section: "snippets"
category: "css-variable-dark-mode-system"
category_name: "CSS Variable Dark Mode Systems"
description: "What every modern SaaS ships: a segmented Appearance control with System, Light, and Dark."
has_js: "true"
---

Here's a working CSS Variable Dark Mode System from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Three-Way Theme Switcher (System, Light, Dark) with matchMedia and CSS Custom Properties
Source: https://codefronts.com/snippets/css-variable-dark-mode-system/three-way-system-light-dark-switcher/

What every modern SaaS ships: a segmented Appearance control with System, Light, and Dark. It defaults to System — honoring the OS via window.matchMedia — but lets users force an explicit override that persists. The key detail most tutorials miss: while in System mode, the UI must live-update when the OS flips, and it does here via a matchMedia change listener.
## HTML
```html
<section class="cdm-04" data-theme="system">
  <div class="cdm-04__panel">
    <div class="cdm-04__head">
      <h1>Appearance</h1>
      <p>Choose how CodeFronts looks. <strong>System</strong> follows your OS and updates live when it changes.</p>
    </div>
    <div class="cdm-04__seg" role="radiogroup" aria-label="Theme">
      <label class="cdm-04__opt"><input type="radio" name="cdm4" value="system" checked><span><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8m-4-4v4"/></svg>System</span></label>
      <label class="cdm-04__opt"><input type="radio" name="cdm4" value="light"><span><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.5"/><path d="M12 1.5v3m0 15v3M1.5 12h3m15 0h3M4.6 4.6l2.1 2.1m10.6 10.6 2.1 2.1m0-14.8-2.1 2.1M6.7 17.3l-2.1 2.1"/></svg>Light</span></label>
      <label class="cdm-04__opt"><input type="radio" name="cdm4" value="dark"><span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5Z"/></svg>Dark</span></label>
    </div>
    <p class="cdm-04__resolved">Currently showing: <strong id="cdm-04-res">—</strong></p>
  </div>
</section>
```
## CSS
```css
.cdm-04,
.cdm-04 *,
.cdm-04 *::before,
.cdm-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdm-04 {
  --bg: oklch(0.98 0.004 250);
  --surface: oklch(1 0 0);
  --text: oklch(0.24 0.02 265);
  --border: oklch(0.9 0.008 265);
  --accent: oklch(0.56 0.16 155);
  --muted: color-mix(in oklab,var(--text) 60%,var(--bg));
  --track: color-mix(in oklab,var(--text) 6%,var(--bg));
  color-scheme: light;
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 32px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--text);
  transition: background-color .3s ease,color .3s ease;
}

.cdm-04[data-theme="light"] {
  color-scheme: light;
}

.cdm-04[data-theme="dark"] {
  --bg: oklch(0.16 0.02 240);
  --surface: oklch(0.21 0.02 240);
  --text: oklch(0.95 0.005 240);
  --border: oklch(0.32 0.02 240);
  --accent: oklch(0.74 0.14 155);
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .cdm-04[data-theme="system"] {
    --bg: oklch(0.16 0.02 240);
    --surface: oklch(0.21 0.02 240);
    --text: oklch(0.95 0.005 240);
    --border: oklch(0.32 0.02 240);
    --accent: oklch(0.74 0.14 155);
    color-scheme: dark;
  }
}

.cdm-04__panel {
  width: min(440px,100%);
  display: flex;
  flex-direction: column;
  gap: 22px;
  padding: 30px;
  border-radius: 20px;
  background: var(--surface);
  border: 1px solid var(--border);
  box-shadow: 0 18px 50px -26px oklch(0 0 0 / .4);
  transition: background-color .3s ease,border-color .3s ease;
}

.cdm-04__head h1 {
  font: 700 22px/1.15 system-ui,sans-serif;
  letter-spacing: -.01em;
  margin-bottom: 8px;
}

.cdm-04__head p {
  font: 400 14px/1.6 system-ui,sans-serif;
  color: var(--muted);
  text-wrap: pretty;
}

.cdm-04__seg {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 4px;
  padding: 4px;
  border-radius: 13px;
  background: var(--track);
  border: 1px solid var(--border);
}

.cdm-04__opt {
  position: relative;
}

.cdm-04__opt input {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.cdm-04__opt span {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 7px;
  min-height: 40px;
  border-radius: 9px;
  font: 600 13px/1 system-ui,sans-serif;
  color: var(--muted);
  transition: background-color .2s ease,color .2s ease;
}

.cdm-04__opt svg {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cdm-04__opt input:checked + span {
  background: var(--surface);
  color: var(--text);
  box-shadow: 0 1px 4px oklch(0 0 0 / .18),0 0 0 1px var(--border);
}

.cdm-04__opt input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cdm-04__resolved {
  font: 400 13px/1 system-ui,sans-serif;
  color: var(--muted);
}

.cdm-04__resolved strong {
  color: var(--accent);
  text-transform: capitalize;
}

@media (prefers-reduced-motion: reduce) {
  .cdm-04,
    .cdm-04 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
(function () {
  var KEY = 'cf-theme-mode';
  var root = document.querySelector('.cdm-04');
  var res  = root.querySelector('#cdm-04-res');
  var radios = root.querySelectorAll('input[name="cdm4"]');
  var mql = matchMedia('(prefers-color-scheme: dark)');

  function apply() {
    var mode = root.dataset.theme;                       // system | light | dark
    var resolved = mode === 'system' ? (mql.matches ? 'dark' : 'light') : mode;
    res.textContent = mode === 'system' ? 'System · ' + resolved : resolved;
    radios.forEach(function (r) { r.setAttribute('aria-checked', String(r.checked)); });
  }

  // restore saved mode (default: system)
  var saved = 'system';
  try { saved = localStorage.getItem(KEY) || 'system'; } catch (e) {}
  root.dataset.theme = saved;
  radios.forEach(function (r) { r.checked = (r.value === saved); });
  apply();

  radios.forEach(function (r) {
    r.addEventListener('change', function () {
      root.dataset.theme = r.value;
      try { localStorage.setItem(KEY, r.value); } catch (e) {}
      apply();
    });
  });

  // live-update while the user is in System mode and the OS flips
  mql.addEventListener('change', function () {
    if (root.dataset.theme === 'system') apply();
  });
})();
```
