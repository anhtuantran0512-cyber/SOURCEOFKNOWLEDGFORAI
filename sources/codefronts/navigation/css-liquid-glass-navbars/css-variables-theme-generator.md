---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/css-variables-theme-generator/"
title: "CSS Variables Theme Generator"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "A liquid-glass navbar wired entirely to CSS custom properties, with live controls that retune it in real time: blur radius, glass tint, opacity and accent…"
has_js: "true"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Variables Theme Generator
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/css-variables-theme-generator/

A liquid-glass navbar wired entirely to CSS custom properties, with live controls that retune it in real time: blur radius, glass tint, opacity and accent hue all flow from a handful of variables. Flip light/dark, drag the sliders, and the whole bar re-themes with no re-render.
## HTML
```html
<section class="nb-11" id="nb-11-root" data-theme="dark" aria-label="CSS variables glass theme generator demo">
  <header class="nb-11__bar">
    <span class="nb-11__brand">◈ Themer</span>
    <nav class="nb-11__nav" aria-label="Primary">
      <a class="nb-11__link" href="#nb-11" aria-current="page">Home</a>
      <a class="nb-11__link" href="#nb-11">Tokens</a>
      <a class="nb-11__link" href="#nb-11">Export</a>
    </nav>
    <button class="nb-11__cta" type="button">Save</button>
  </header>
  <form class="nb-11__panel" aria-label="Theme controls">
    <label class="nb-11__ctl">Blur <input type="range" id="nb-11-blur" min="4" max="40" value="22"></label>
    <label class="nb-11__ctl">Tint alpha <input type="range" id="nb-11-alpha" min="4" max="40" value="14"></label>
    <label class="nb-11__ctl">Hue <input type="range" id="nb-11-hue" min="0" max="360" value="265"></label>
    <fieldset class="nb-11__modes"><legend class="nb-11__lg">Mode</legend>
      <label><input type="radio" name="nb-11-mode" value="dark" checked> Dark</label>
      <label><input type="radio" name="nb-11-mode" value="light"> Light</label>
    </fieldset>
  </form>
</section>
```
## CSS
```css
.nb-11,
.nb-11 *,
.nb-11 *::before,
.nb-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-11 {
  --glass-blur: 22px;
  --glass-alpha: 14%;
  --tint-hue: 265;
  --accent: oklch(0.66 0.2 var(--tint-hue));
  --fg: #fff;
  --panel-bg: rgba(255,255,255,.08);
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 22px;
  justify-content: center;
  align-items: center;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(circle at 30% 20%,oklch(0.5 0.22 var(--tint-hue)),#0a0a12 70%);
  transition: background .4s;
}

.nb-11[data-theme="light"] {
  --fg: #101018;
  --glass-alpha: 55%;
  --panel-bg: rgba(255,255,255,.5);
  background: radial-gradient(circle at 30% 20%,oklch(0.9 0.09 var(--tint-hue)),#e7e7ef 70%);
}

.nb-11__bar {
  display: flex;
  align-items: center;
  gap: 18px;
  width: min(720px,100%);
  padding: 13px 16px;
  border-radius: 18px;
  color: var(--fg);
  background: color-mix(in oklab,var(--fg) var(--glass-alpha),transparent);
  border: 1px solid color-mix(in oklab,var(--fg) 30%,transparent);
  box-shadow: inset 0 1px 0 color-mix(in oklab,var(--fg) 45%,transparent),0 18px 40px -22px rgba(0,0,0,.6);
  backdrop-filter: blur(var(--glass-blur)) saturate(180%);
  -webkit-backdrop-filter: blur(var(--glass-blur)) saturate(180%);
  transition: backdrop-filter .3s,background .3s;
}

.nb-11__brand {
  font-size: 16px;
  font-weight: 800;
}

.nb-11__nav {
  display: flex;
  gap: 4px;
  margin-inline-start: auto;
}

.nb-11__link {
  min-height: 40px;
  display: flex;
  align-items: center;
  padding: 0 14px;
  border-radius: 10px;
  text-decoration: none;
  color: var(--fg);
  opacity: .82;
  font-size: 14.5px;
  font-weight: 600;
  transition: background .2s,opacity .2s;
}

.nb-11__link[aria-current] {
  opacity: 1;
  background: color-mix(in oklab,var(--fg) 18%,transparent);
}

.nb-11__link:hover {
  opacity: 1;
}

.nb-11__link:focus-visible,
.nb-11__cta:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.nb-11__cta {
  min-height: 40px;
  padding: 0 18px;
  border-radius: 10px;
  border: 0;
  background: var(--accent);
  color: #fff;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
}

.nb-11__panel {
  display: flex;
  flex-wrap: wrap;
  gap: 14px 22px;
  align-items: center;
  width: min(720px,100%);
  padding: 16px;
  border-radius: 16px;
  color: var(--fg);
  background: var(--panel-bg);
  border: 1px solid color-mix(in oklab,var(--fg) 20%,transparent);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}

.nb-11__ctl {
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-size: 12px;
  font-weight: 600;
  color: var(--fg);
}

.nb-11__ctl input {
  accent-color: var(--accent);
}

.nb-11__modes {
  display: flex;
  gap: 14px;
  align-items: center;
  border: 0;
  font-size: 13px;
  color: var(--fg);
}

.nb-11__lg {
  font-size: 12px;
  font-weight: 700;
  margin-right: 4px;
}

.nb-11__modes label {
  display: flex;
  align-items: center;
  gap: 5px;
  cursor: pointer;
}

@media (prefers-reduced-motion: reduce) {
  .nb-11,
    .nb-11__bar {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#nb-11-root');
  if (!root) return;
  const set = (k,v) => root.style.setProperty(k, v);
  root.querySelector('#nb-11-blur').addEventListener('input', e => set('--glass-blur', e.target.value + 'px'));
  root.querySelector('#nb-11-alpha').addEventListener('input', e => set('--glass-alpha', e.target.value + '%'));
  root.querySelector('#nb-11-hue').addEventListener('input', e => set('--tint-hue', e.target.value));
  root.querySelectorAll('input[name="nb-11-mode"]').forEach(r =>
    r.addEventListener('change', e => { root.dataset.theme = e.target.value; }));
})();
```
