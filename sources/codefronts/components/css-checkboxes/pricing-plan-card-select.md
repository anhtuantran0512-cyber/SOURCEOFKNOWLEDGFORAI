---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/pricing-plan-card-select/"
title: "Pricing Plan Card Select"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "A full pricing block that becomes the control: on selection the whole card gains an accent border, a corner check badge and a slight lift."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pricing Plan Card Select
Source: https://codefronts.com/components/css-checkboxes/pricing-plan-card-select/

A full pricing block that becomes the control: on selection the whole card gains an accent border, a corner check badge and a slight lift. The conversion-focused pattern for onboarding, plan pickers and add-on grids.
## HTML
```html
<section class="cb-03" aria-label="Pricing plan selector">
  <div class="cb-03__grid">
    <label class="cb-03__card"><input type="checkbox" class="cb-03__input">
      <span class="cb-03__badge" aria-hidden="true"></span>
      <span class="cb-03__name">Starter</span>
      <span class="cb-03__price">$9<span>/mo</span></span>
      <span class="cb-03__feat">3 projects · 1 seat · community support</span>
    </label>
    <label class="cb-03__card"><input type="checkbox" class="cb-03__input" checked>
      <span class="cb-03__badge" aria-hidden="true"></span>
      <span class="cb-03__tag">Popular</span>
      <span class="cb-03__name">Growth</span>
      <span class="cb-03__price">$29<span>/mo</span></span>
      <span class="cb-03__feat">Unlimited projects · 5 seats · priority support</span>
    </label>
    <label class="cb-03__card"><input type="checkbox" class="cb-03__input">
      <span class="cb-03__badge" aria-hidden="true"></span>
      <span class="cb-03__name">Scale</span>
      <span class="cb-03__price">$79<span>/mo</span></span>
      <span class="cb-03__feat">SSO · audit logs · dedicated CSM</span>
    </label>
  </div>
</section>
```
## CSS
```css
.cb-03,
.cb-03 *,
.cb-03 *::before,
.cb-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-03 ::selection {
  background: oklch(0.6 0.17 285);
  color: #fff;
}

.cb-03 {
  --accent: oklch(0.55 0.19 285);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #f5f4f8;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-03__grid {
  width: min(760px,100%);
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 16px;
}

.cb-03__input {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}

.cb-03__card {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 6px;
  cursor: pointer;
  padding: 22px 20px;
  background: #fff;
  border: 2px solid #e5e4ee;
  border-radius: 16px;
  box-shadow: 0 10px 26px -22px rgba(30,20,60,.6);
  transition: border-color .25s,box-shadow .25s,transform .25s cubic-bezier(.2,.8,.2,1);
}

.cb-03__tag {
  position: absolute;
  top: -10px;
  left: 20px;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: #fff;
  background: var(--accent);
  padding: 3px 9px;
  border-radius: 999px;
}

.cb-03__name {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #8b88a0;
}

.cb-03__price {
  font-size: 32px;
  font-weight: 800;
  color: #22203a;
}

.cb-03__price span {
  font-size: 14px;
  font-weight: 600;
  color: #9b98ad;
}

.cb-03__feat {
  font-size: 12.5px;
  line-height: 1.5;
  color: #6f6c83;
  margin-top: 2px;
}

.cb-03__badge {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  border: 2px solid #d7d5e4;
  background: #fff;
  transition: border-color .25s,background .25s;
}

.cb-03__badge::after {
  content: "";
  position: absolute;
  inset: 0;
  background: #fff;
  opacity: 0;
  transform: scale(.4);
  transition: opacity .25s,transform .25s;
  -webkit-mask: no-repeat center/13px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/13px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-03__card:hover {
  border-color: #c7c4dd;
}

.cb-03__input:checked ~ .cb-03__badge {
  background: var(--accent);
  border-color: var(--accent);
}

.cb-03__input:checked ~ .cb-03__badge::after {
  opacity: 1;
  transform: scale(1);
}

.cb-03__input:checked ~ * {
}

.cb-03__card:has(:checked) {
  border-color: var(--accent);
  transform: translateY(-4px);
  box-shadow: 0 22px 40px -24px rgba(80,40,180,.55);
}

.cb-03__card:has(:focus-visible) {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (max-width: 640px) {
  .cb-03__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-03__card,
    .cb-03__badge,
    .cb-03__badge::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — :checked + :has() style the whole card and badge. */
```
