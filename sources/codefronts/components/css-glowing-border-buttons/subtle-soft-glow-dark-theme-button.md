---
source: "codefronts"
url: "https://codefronts.com/components/css-glowing-border-buttons/subtle-soft-glow-dark-theme-button/"
title: "Subtle Soft Glow Dark Theme Button"
section: "components"
category: "css-glowing-border-buttons"
category_name: "CSS Glowing Border Buttons"
description: "The 'invisible craft' button for developer docs and minimalist SaaS: at rest it's a quiet outlined control; on hover the border warms by one step and a glow…"
has_js: "false"
---

Here's a working CSS Glowing Border Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Subtle Soft Glow Dark Theme Button
Source: https://codefronts.com/components/css-glowing-border-buttons/subtle-soft-glow-dark-theme-button/

The 'invisible craft' button for developer docs and minimalist SaaS: at rest it's a quiet outlined control; on hover the border warms by one step and a glow so faint you feel it more than see it settles around the edge. The whole effect lives inside a 12% opacity budget — restraint as a feature.
## HTML
```html
<section class="gbb-11" aria-label="Subtle soft glow dark theme buttons demo">
  <div class="gbb-11__row">
    <button class="gbb-11__btn gbb-11__btn--primary" type="button">Read the docs</button>
    <button class="gbb-11__btn" type="button">View changelog</button>
  </div>
</section>
```
## CSS
```css
.gbb-11,
.gbb-11 *,
.gbb-11 *::before,
.gbb-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gbb-11 {
  --acc: oklch(0.72 0.09 240);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: oklch(0.16 0.008 260);
}

.gbb-11 .gbb-11__row {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  justify-content: center;
}

.gbb-11 .gbb-11__btn {
  cursor: pointer;
  border-radius: 10px;
  padding: 13px 24px;
  font: 500 14px/1 'Segoe UI',system-ui,sans-serif;
  color: rgba(255,255,255,.78);
  background: oklch(0.19 0.01 260);
  border: 1px solid color-mix(in oklab,var(--acc) 12%,rgba(255,255,255,.1));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.06),0 0 24px color-mix(in oklab,var(--acc) 0%,transparent);
  transition: border-color .4s ease,box-shadow .4s ease,color .4s ease,background .4s ease;
}

.gbb-11 .gbb-11__btn:hover,
.gbb-11 .gbb-11__btn:focus-visible {
  color: #fff;
  border-color: color-mix(in oklab,var(--acc) 32%,rgba(255,255,255,.14));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.08),0 0 24px color-mix(in oklab,var(--acc) 12%,transparent);
}

.gbb-11 .gbb-11__btn--primary {
  color: #fff;
  background: color-mix(in oklab,var(--acc) 14%,oklch(0.2 0.012 260));
  border-color: color-mix(in oklab,var(--acc) 28%,rgba(255,255,255,.12));
}

.gbb-11 .gbb-11__btn--primary:hover,
.gbb-11 .gbb-11__btn--primary:focus-visible {
  border-color: color-mix(in oklab,var(--acc) 55%,rgba(255,255,255,.14));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.1),0 0 24px color-mix(in oklab,var(--acc) 22%,transparent);
}

.gbb-11 .gbb-11__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.gbb-11 .gbb-11__btn:active {
  background: oklch(0.17 0.01 260);
}

@media (prefers-reduced-motion: reduce) {
  .gbb-11 .gbb-11__btn {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — three sub-threshold changes (border step, 12% halo, label brighten) on a slow 400ms ease compound into quiet polish. */
```
