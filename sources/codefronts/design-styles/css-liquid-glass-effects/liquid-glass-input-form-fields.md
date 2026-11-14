---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-input-form-fields/"
title: "Liquid Glass Input Form Fields"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "A sign-up form where the fields are translucent glass tiles over a soft gradient, and on focus a glowing refractive border lights up and travels around the…"
has_js: "false"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Input Form Fields
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-input-form-fields/

A sign-up form where the fields are translucent glass tiles over a soft gradient, and on focus a glowing refractive border lights up and travels around the active input. Turns a boring checkout form into a premium moment — pure CSS, fully labelled, keyboard-friendly.
## HTML
```html
<section class="lg-07" aria-label="Liquid glass form fields">
  <form class="lg-07__form" novalidate>
    <h3 class="lg-07__head">Create account</h3>
    <div class="lg-07__field"><label class="lg-07__label" for="lg-07-name">Full name</label><span class="lg-07__wrap"><input class="lg-07__input" id="lg-07-name" type="text" placeholder="Ada Lovelace" autocomplete="name"></span></div>
    <div class="lg-07__field"><label class="lg-07__label" for="lg-07-email">Email</label><span class="lg-07__wrap"><input class="lg-07__input" id="lg-07-email" type="email" placeholder="[email protected]" autocomplete="email"></span></div>
    <div class="lg-07__field"><label class="lg-07__label" for="lg-07-pass">Password</label><span class="lg-07__wrap"><input class="lg-07__input" id="lg-07-pass" type="password" placeholder="••••••••" autocomplete="new-password"></span></div>
    <button class="lg-07__submit" type="submit">Sign up</button>
  </form>
</section>
```
## CSS
```css
.lg-07,
.lg-07 *,
.lg-07 *::before,
.lg-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --lg-07-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.lg-07 {
  --accent: oklch(0.68 0.19 285);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: conic-gradient(from 210deg at 30% 30%,#2a2350,#3a2a60,#1c2450,#2a2350);
}

.lg-07__form {
  width: min(400px,92vw);
  padding: 34px;
  border-radius: 26px;
  background: color-mix(in oklab,white 10%,transparent);
  border: 1px solid rgba(255,255,255,.28);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4),0 30px 60px -30px rgba(0,0,0,.6);
  backdrop-filter: blur(22px) saturate(170%);
  -webkit-backdrop-filter: blur(22px) saturate(170%);
}

.lg-07__head {
  color: #fff;
  font-size: 24px;
  font-weight: 800;
  margin-bottom: 22px;
}

.lg-07__field {
  margin-bottom: 18px;
}

.lg-07__label {
  display: block;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: rgba(255,255,255,.7);
  margin-bottom: 7px;
}

.lg-07__wrap {
  position: relative;
  display: block;
}

.lg-07__input {
  position: relative;
  z-index: 1;
  display: block;
  width: 100%;
  font-size: 15px;
  color: #fff;
  padding: 13px 15px;
  border-radius: 14px;
  border: 1px solid rgba(255,255,255,.25);
  background: color-mix(in oklab,white 8%,transparent);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.3);
  outline: none;
  transition: background .2s;
}

.lg-07__input::placeholder {
  color: rgba(255,255,255,.5);
}

.lg-07__wrap::before {
  content: "";
  position: absolute;
  inset: -2px;
  border-radius: 16px;
  padding: 2px;
  background: conic-gradient(from var(--lg-07-angle),var(--accent),oklch(0.7 0.18 200),oklch(0.72 0.17 330),var(--accent));
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask-composite: exclude;
  opacity: 0;
  transition: opacity .3s;
  pointer-events: none;
}

.lg-07__wrap:focus-within::before {
  opacity: 1;
  animation: lg-07-spin 3s linear infinite;
}

.lg-07__wrap:focus-within .lg-07__input {
  background: color-mix(in oklab,white 14%,transparent);
}

.lg-07__submit {
  width: 100%;
  margin-top: 6px;
  font-size: 16px;
  font-weight: 700;
  color: #fff;
  padding: 14px;
  border-radius: 14px;
  border: 1px solid color-mix(in oklab,var(--accent) 40%,white);
  cursor: pointer;
  background: linear-gradient(180deg,color-mix(in oklab,var(--accent) 85%,white),var(--accent));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 14px 28px -16px rgba(0,0,0,.6);
  transition: transform .15s;
}

.lg-07__submit:hover {
  transform: translateY(-2px);
}

.lg-07__submit:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@keyframes lg-07-spin {
  to {
    --lg-07-angle: 360deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .lg-07__field:focus-within::before {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — :focus-within lights each field, and an @property-driven conic-gradient (masked to a 1px rim) spins the refractive border around the active input. */
```
