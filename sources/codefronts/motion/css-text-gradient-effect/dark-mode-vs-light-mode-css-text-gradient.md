---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/dark-mode-vs-light-mode-css-text-gradient/"
title: "Dark Mode vs Light Mode CSS Text Gradient"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "A toggle-enabled card that switches between vivid neon gradients (dark) and rich jewel-tone gradients (light) via CSS variables and a JS class swap."
has_js: "true"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode vs Light Mode CSS Text Gradient
Source: https://codefronts.com/motion/css-text-gradient-effect/dark-mode-vs-light-mode-css-text-gradient/

A toggle-enabled card that switches between vivid neon gradients (dark) and rich jewel-tone gradients (light) via CSS variables and a JS class swap.
## HTML
```html
<div class="tg-20" id="tg-20-root">
  <div class="tg-20__card">
    <div class="tg-20__header">
      <div class="tg-20__brand">
        <span class="tg-20__icon">◈</span>
        <span class="tg-20__brand-name"><span class="tg-20__grad">Lumis</span></span>
      </div>
      <button class="tg-20__toggle" id="tg-20-toggle" aria-label="Toggle colour scheme">
        <span class="tg-20__toggle-icon tg-20__moon">☾</span>
        <span class="tg-20__toggle-icon tg-20__sun">☀</span>
      </button>
    </div>
    <h1 class="tg-20__title">Adaptive <span class="tg-20__grad">Colour</span><br>for Every Context</h1>
    <p class="tg-20__body">Gradient variables swap automatically between light and dark schemes via <code>prefers-color-scheme</code> and a JS toggle. Vivid saturated gradients work on dark backgrounds; softer, deeper tones on light.</p>
    <div class="tg-20__chips">
      <span class="tg-20__chip tg-20__grad-text">Dark: vivid neon</span>
      <span class="tg-20__chip tg-20__grad-text-alt">Light: rich jewel</span>
    </div>
  </div>
</div>
```
## CSS
```css
.tg-20,
.tg-20 *,
.tg-20 *::before,
.tg-20 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
/* Dark defaults */

.tg-20 {
  /* Dark-mode gradient: vivid, high-saturation */
  --grad: linear-gradient(110deg, #f0abfc 0%, #818cf8 50%, #38bdf8 100%);
  --grad-alt: linear-gradient(110deg, #34d399 0%, #06b6d4 100%);
  --bg: #06030f;
  --surface: #10101a;
  --text: #f0e7ff;
  --muted: rgba(240,231,255,.5);
  --border: rgba(255,255,255,.08);
  --toggle-bg: rgba(255,255,255,.07);
  --moon-op: 1;
  --sun-op: 0;
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 44px 24px;
  transition: background .3s, color .3s;
}
/* Light-mode override via media query */

@media (prefers-color-scheme: light) {
  .tg-20:not(.tg-20--force-dark) {
    --grad: linear-gradient(110deg, #4f46e5 0%, #7c3aed 55%, #a21caf 100%);
    --grad-alt: linear-gradient(110deg, #0f766e 0%, #0284c7 100%);
    --bg: #f8fafc;
    --surface: #ffffff;
    --text: #0f172a;
    --muted: #64748b;
    --border: #e2e8f0;
    --toggle-bg: #e2e8f0;
    --moon-op: 0;
    --sun-op: 1;
  }
}
/* JS-toggled light class */

.tg-20--light {
  --grad: linear-gradient(110deg, #4f46e5 0%, #7c3aed 55%, #a21caf 100%);
  --grad-alt: linear-gradient(110deg, #0f766e 0%, #0284c7 100%);
  --bg: #f8fafc;
  --surface: #ffffff;
  --text: #0f172a;
  --muted: #64748b;
  --border: #e2e8f0;
  --toggle-bg: #e2e8f0;
  --moon-op: 0;
  --sun-op: 1;
}

.tg-20__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 36px 32px;
  max-width: 520px;
  width: 100%;
  transition: background .3s, border-color .3s;
}

.tg-20__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 28px;
}

.tg-20__brand {
  display: flex;
  align-items: center;
  gap: 8px;
}

.tg-20__icon {
  font-size: 1.3rem;
  background: var(--grad);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.tg-20__brand-name {
  font-size: 1.25rem;
  font-weight: 800;
}
/* Reusable gradient text — driven by --grad variable */

.tg-20__grad {
  background: var(--grad);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.tg-20__grad-text {
  background: var(--grad);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.tg-20__grad-text-alt {
  background: var(--grad-alt);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.tg-20__toggle {
  background: var(--toggle-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 8px 12px;
  cursor: pointer;
  transition: background .2s;
  position: relative;
  width: 44px;
  height: 36px;
}

.tg-20__toggle-icon {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  font-size: 1rem;
  transition: opacity .25s;
}

.tg-20__moon {
  opacity: var(--moon-op);
}

.tg-20__sun {
  opacity: var(--sun-op);
}

.tg-20__title {
  font-size: clamp(1.6rem, 5vw, 2.5rem);
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -.03em;
  color: var(--text);
  margin-bottom: 16px;
  transition: color .3s;
}

.tg-20__body {
  font-size: .875rem;
  color: var(--muted);
  line-height: 1.7;
  margin-bottom: 22px;
  transition: color .3s;
}

.tg-20__body code {
  font-size: .8em;
  background: var(--border);
  border-radius: 3px;
  padding: 1px 5px;
  color: inherit;
  filter: brightness(1.5);
}

.tg-20__chips {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.tg-20__chip {
  font-size: .8rem;
  font-weight: 700;
  padding: 5px 14px;
  border-radius: 99px;
  border: 1px solid var(--border);
}

@media (prefers-reduced-motion: reduce) {
  .tg-20,
    .tg-20__card,
    .tg-20__title,
    .tg-20__body,
    .tg-20__toggle {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('tg-20-root');
  var btn  = document.getElementById('tg-20-toggle');
  var light = false;
  btn.addEventListener('click', function(){
    light = !light;
    root.classList.toggle('tg-20--light', light);
    root.classList.toggle('tg-20--force-dark', !light);
  });
})();
```
