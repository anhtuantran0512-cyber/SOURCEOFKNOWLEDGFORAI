---
source: "codefronts"
url: "https://codefronts.com/components/css-glowing-border-buttons/minimalist-outer-glow-box-shadow-button/"
title: "Minimalist Outer Glow Box-Shadow Button"
section: "components"
category: "css-glowing-border-buttons"
category_name: "CSS Glowing Border Buttons"
description: "The restrained e-commerce workhorse: a solid brand-colored Add to Cart whose glow is a single soft box-shadow in the button's own color, swelling gently on…"
has_js: "false"
---

Here's a working CSS Glowing Border Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Outer Glow Box-Shadow Button
Source: https://codefronts.com/components/css-glowing-border-buttons/minimalist-outer-glow-box-shadow-button/

The restrained e-commerce workhorse: a solid brand-colored Add to Cart whose glow is a single soft box-shadow in the button's own color, swelling gently on hover with a 2px lift. No gradients, no animation loops — just the shadow discipline that makes conversion buttons feel pressable on light themes.
## HTML
```html
<section class="gbb-08" aria-label="Minimalist outer glow button demo">
  <button class="gbb-08__btn" type="button"><svg class="gbb-08__cart" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>Add to Cart &mdash; $64</button>
</section>
```
## CSS
```css
.gbb-08,
.gbb-08 *,
.gbb-08 *::before,
.gbb-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gbb-08 {
  --brand: oklch(0.55 0.2 275);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.985 0.003 260),oklch(0.955 0.006 260));
}

.gbb-08 .gbb-08__btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  border: none;
  border-radius: 14px;
  padding: 16px 30px;
  font: 600 15px/1 'Segoe UI',system-ui,sans-serif;
  color: #fff;
  background: var(--brand);
  box-shadow: 0 10px 25px -8px color-mix(in oklab,var(--brand) 55%,transparent);
  transition: box-shadow .25s ease,transform .25s ease,background .25s ease;
}

.gbb-08 .gbb-08__cart {
  width: 18px;
  height: 18px;
}

.gbb-08 .gbb-08__btn:hover,
.gbb-08 .gbb-08__btn:focus-visible {
  transform: translateY(-2px);
  background: color-mix(in oklab,var(--brand) 92%,#fff);
  box-shadow: 0 16px 34px -10px color-mix(in oklab,var(--brand) 70%,transparent);
}

.gbb-08 .gbb-08__btn:focus-visible {
  outline: 3px solid color-mix(in oklab,var(--brand) 55%,transparent);
  outline-offset: 3px;
}

.gbb-08 .gbb-08__btn:active {
  transform: translateY(0);
  transition-duration: .08s;
  box-shadow: 0 6px 16px -8px color-mix(in oklab,var(--brand) 60%,transparent);
}

@media (prefers-reduced-motion: reduce) {
  .gbb-08 .gbb-08__btn {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a downward-cast, brand-tinted box-shadow at two strengths + a 2px lift; the fast :active press sells the physicality. */
```
