---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/progress-track/"
title: "Multi-Step Checkout & Form Wizard CSS Breadcrumb Indicator"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "Breadcrumbs reimagined as a checkout/wizard progress bar: numbered circular step badges (auto-numbered with CSS counters), connecting progress lines that…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Step Checkout & Form Wizard CSS Breadcrumb Indicator
Source: https://codefronts.com/navigation/css-breadcrumbs/progress-track/

Breadcrumbs reimagined as a checkout/wizard progress bar: numbered circular step badges (auto-numbered with CSS counters), connecting progress lines that fill for completed steps, and clear done / current / upcoming states — the Cart › Shipping › Payment › Review pattern, all in CSS with no manual numbering.
## HTML
```html
<nav class="bc-27" aria-label="Checkout progress">
  <ol>
    <li data-state="done"><span class="bc-27__badge" aria-hidden="true"></span><span class="bc-27__label">Cart</span><span class="bc-27__sr">completed</span></li>
    <li data-state="done"><span class="bc-27__badge" aria-hidden="true"></span><span class="bc-27__label">Shipping</span><span class="bc-27__sr">completed</span></li>
    <li data-state="current" aria-current="step"><span class="bc-27__badge" aria-hidden="true"></span><span class="bc-27__label">Payment</span></li>
    <li data-state="upcoming"><span class="bc-27__badge" aria-hidden="true"></span><span class="bc-27__label">Review</span></li>
  </ol>
</nav>
```
## CSS
```css
.bc-27 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.6 0.16 250);
  --done: oklch(0.65 0.14 160);
  --mut: oklch(0.85 0.01 250);
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 36px 30px;
  background: oklch(0.98 0.004 250);
  place-items: center;
}

.bc-27 * {
  box-sizing: border-box;
}

.bc-27 ol {
  counter-reset: step;
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-27 li {
  position: relative;
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  text-align: center;
}

.bc-27 li::before {
  content: "";
  position: absolute;
  top: 16px;
  left: -50%;
  width: 100%;
  height: 3px;
  background: var(--mut);
  z-index: 0;
}

.bc-27 li:first-child::before {
  display: none;
}

.bc-27 li[data-state="done"]::before,
.bc-27 li[data-state="current"]::before {
  background: var(--done);
}

.bc-27__badge {
  counter-increment: step;
  position: relative;
  z-index: 1;
  display: grid;
  place-items: center;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  font: 700 14px/1 system-ui,sans-serif;
  background: #fff;
  color: oklch(0.6 0.01 250);
  border: 2px solid var(--mut);
}

.bc-27__badge::after {
  content: counter(step);
}

.bc-27 li[data-state="done"] .bc-27__badge {
  background: var(--done);
  border-color: var(--done);
  color: #fff;
}

.bc-27 li[data-state="done"] .bc-27__badge::after {
  content: "✓";
}

.bc-27 li[data-state="current"] .bc-27__badge {
  border-color: var(--accent);
  color: var(--accent);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--accent) 20%,transparent);
}

.bc-27__label {
  font: 600 13px/1.2 system-ui,sans-serif;
  color: oklch(0.5 0.02 250);
}

.bc-27 li[data-state="current"] .bc-27__label {
  color: oklch(0.3 0.02 250);
}

.bc-27 li[data-state="upcoming"] .bc-27__label {
  color: oklch(0.68 0.01 250);
}

.bc-27__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}

@media (max-width: 520px) {
  .bc-27__label {
    font-size: 11.5px;
  }
}
```

## JavaScript
```js
/* No JavaScript — CSS counters auto-number the step badges (content:counter(step)); data-state paints done/current/upcoming and fills the connector lines. */
```
