---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/css-custom-property-accent-color-toggle-breadcrumb/"
title: "CSS Custom-Property Accent-Color Toggle Breadcrumb"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A breadcrumb whose accent colour is a single custom property the user can switch live from a swatch row — hover, current, and focus all recolour instantly…"
has_js: "true"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Custom-Property Accent-Color Toggle Breadcrumb
Source: https://codefronts.com/navigation/css-breadcrumbs/css-custom-property-accent-color-toggle-breadcrumb/

A breadcrumb whose accent colour is a single custom property the user can switch live from a swatch row — hover, current, and focus all recolour instantly from one variable. Nine lines of JS persist the choice to localStorage so it survives reloads; the CSS is fully theme-agnostic.
## HTML
```html
<div class="bc-12">
  <div class="bc-12__swatches" role="group" aria-label="Accent colour">
    <button type="button" data-accent="oklch(0.6 0.18 265)" aria-label="Indigo accent" style="background:oklch(0.6 0.18 265)"></button>
    <button type="button" data-accent="oklch(0.65 0.17 25)" aria-label="Coral accent" style="background:oklch(0.65 0.17 25)"></button>
    <button type="button" data-accent="oklch(0.7 0.16 160)" aria-label="Emerald accent" style="background:oklch(0.7 0.16 160)"></button>
    <button type="button" data-accent="oklch(0.72 0.15 60)" aria-label="Amber accent" style="background:oklch(0.72 0.15 60)"></button>
  </div>
  <nav aria-label="Breadcrumb">
    <ol>
      <li><a href="#">Home</a></li>
      <li><a href="#">Settings</a></li>
      <li><a href="#">Appearance</a></li>
      <li><a href="#" aria-current="page">Accent Colour</a></li>
    </ol>
  </nav>
</div>
```
## CSS
```css
.bc-12 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  --bc-accent: oklch(0.6 0.18 265);
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 28px;
  background: oklch(0.98 0.004 265);
  place-items: center;
}

.bc-12 * {
  box-sizing: border-box;
}

.bc-12__swatches {
  display: flex;
  gap: 8px;
  margin-bottom: 20px;
}

.bc-12__swatches button {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  border: 2px solid #fff;
  box-shadow: 0 0 0 1px oklch(0.85 0.01 265);
  cursor: pointer;
  transition: transform .15s ease,box-shadow .15s ease;
}

.bc-12__swatches button:hover {
  transform: scale(1.12);
}

.bc-12__swatches button:focus-visible {
  outline: 2px solid var(--bc-accent);
  outline-offset: 3px;
}

.bc-12 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-12 li {
  display: flex;
  align-items: center;
}

.bc-12 li + li::before {
  content: "›";
  margin: 0 8px;
  color: oklch(0.72 0.02 265);
}

.bc-12 a {
  padding: 6px 11px;
  border-radius: 8px;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: oklch(0.45 0.03 265);
  text-decoration: none;
  transition: background-color .18s ease,color .18s ease;
}

.bc-12 a:hover {
  color: var(--bc-accent);
  background: color-mix(in oklab,var(--bc-accent) 12%,transparent);
}

.bc-12 a:focus-visible {
  outline: 2px solid var(--bc-accent);
  outline-offset: 2px;
}

.bc-12 li[aria-current="page"] a {
  color: #fff;
  background: var(--bc-accent);
}

@media (prefers-reduced-motion: reduce) {
  .bc-12 a,
    .bc-12__swatches button {
    transition: none;
  }
}
```

## JavaScript
```js
/* Live accent theming from one custom property, persisted to localStorage (9 lines) */
document.querySelectorAll('.bc-12').forEach((root) => {
  const KEY = 'bc28-accent';
  try { const saved = localStorage.getItem(KEY); if (saved) root.style.setProperty('--bc-accent', saved); } catch (e) {}
  root.querySelectorAll('.bc-12__swatches button').forEach((btn) => {
    btn.addEventListener('click', () => {
      const c = btn.dataset.accent;
      root.style.setProperty('--bc-accent', c);
      try { localStorage.setItem(KEY, c); } catch (e) {}
    });
  });
});
```
