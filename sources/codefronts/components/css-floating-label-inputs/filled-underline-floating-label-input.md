---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-label-inputs/filled-underline-floating-label-input/"
title: "Filled & Underline Floating Label Input"
section: "components"
category: "css-floating-label-inputs"
category_name: "CSS Floating Label Inputs"
description: "The minimalist filled variant: a soft tinted field with only a bottom border, where focus sweeps an accent underline from the center outward while the label…"
has_js: "false"
---

Here's a working CSS Floating Label Input from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Filled & Underline Floating Label Input
Source: https://codefronts.com/components/css-floating-label-inputs/filled-underline-floating-label-input/

The minimalist filled variant: a soft tinted field with only a bottom border, where focus sweeps an accent underline from the center outward while the label floats — the calm, editorial style used by Material 'filled' fields, Stripe-era dashboards and most design-forward SaaS signups. Variation: a BLINK-SWAP float — the label fades out mid-field and re-materialises in its floated spot, timed to the underline sweep.
## HTML
```html
<section class="flb-10" aria-label="Filled underline floating label demo">
  <form class="flb-10__form" novalidate>
    <h3 class="flb-10__title">Stay in the loop</h3>
    <div class="flb-10__field">
      <input class="flb-10__input" type="text" id="flb-10-first" name="given-name" placeholder=" " autocomplete="given-name">
      <label class="flb-10__label" for="flb-10-first">First name</label>
    </div>
    <div class="flb-10__field">
      <input class="flb-10__input" type="email" id="flb-10-mail" name="email" placeholder=" " autocomplete="email">
      <label class="flb-10__label" for="flb-10-mail">Email address</label>
    </div>
    <button class="flb-10__btn" type="button">Subscribe</button>
  </form>
</section>
```
## CSS
```css
.flb-10,
.flb-10 *,
.flb-10 *::before,
.flb-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.flb-10 {
  --accent: oklch(0.55 0.15 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f7f8f8;
  padding: 40px 20px;
}

.flb-10__form {
  width: min(380px,100%);
  background: #fff;
  border-radius: 18px;
  padding: 34px 30px;
  box-shadow: 0 20px 50px -30px rgba(20,40,45,.3);
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.flb-10__title {
  font-size: 23px;
  font-weight: 800;
  color: #16232a;
  letter-spacing: -.02em;
}

.flb-10__field {
  position: relative;
}

.flb-10__input {
  width: 100%;
  height: 56px;
  padding: 22px 14px 6px;
  font-size: 16px;
  color: #16232a;
  background: oklch(0.55 0.15 200 / .07);
  border: none;
  border-bottom: 2px solid #b9c6cc;
  border-radius: 10px 10px 0 0;
  outline: none;
  transition: background .2s;
}

.flb-10__input:hover {
  background: oklch(0.55 0.15 200 / .11);
}

.flb-10__field::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 2px;
  background: var(--accent);
  transform: scaleX(0);
  transform-origin: center;
  transition: transform .25s ease;
}

.flb-10__field:focus-within::after {
  transform: scaleX(1);
}

.flb-10__label {
  position: absolute;
  left: 14px;
  top: 50%;
  translate: 0 -50%;
  font-size: 16px;
  color: #5d707a;
  pointer-events: none;
  transform-origin: left center;
  transition: transform .18s,color .18s;
}

.flb-10__input:focus ~ .flb-10__label,
.flb-10__input:not(:placeholder-shown) ~ .flb-10__label {
  transform: translateY(-13px) scale(.72);
  animation: flb-10-swap .32s both;
}

@keyframes flb-10-swap {
  0% {
    opacity: 1;
    transform: translateY(0) scale(1);
  }

  45% {
    opacity: 0;
    transform: translateY(5px) scale(1);
  }

  55% {
    opacity: 0;
    transform: translateY(-18px) scale(.72);
  }

  100% {
    opacity: 1;
    transform: translateY(-13px) scale(.72);
  }
}

.flb-10__input:focus ~ .flb-10__label {
  color: var(--accent);
}

.flb-10__btn {
  height: 50px;
  border: none;
  border-radius: 12px;
  background: #16232a;
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  transition: filter .15s;
}

.flb-10__btn:hover {
  filter: brightness(1.35);
}

.flb-10__btn:focus-visible,
.flb-10__input:focus-visible {
  outline: 3px solid oklch(0.55 0.15 200 / .5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .flb-10__label,
    .flb-10__input,
    .flb-10__field::after {
    transition: none;
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — :focus-within scales a ::after underline from scaleX(0) to scaleX(1); the float is the standard :placeholder-shown pattern. All motion is transform-only. */
```
