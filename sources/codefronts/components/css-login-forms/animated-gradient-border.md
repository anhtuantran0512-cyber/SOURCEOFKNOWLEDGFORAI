---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/animated-gradient-border/"
title: "Animated Gradient Border"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "A glowing conic-gradient light continuously rotates around the login card's edge — the fast-moving-tech accent — rendered on the GPU via an animated custom…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Gradient Border
Source: https://codefronts.com/components/css-login-forms/animated-gradient-border/

A glowing conic-gradient light continuously rotates around the login card's edge — the fast-moving-tech accent — rendered on the GPU via an animated custom property so it never stutters the desktop.
## HTML
```html
<section class="lf-21">
  <div class="lf-21__wrap">
    <form class="lf-21__card" novalidate>
      <h1 class="lf-21__h">Sign in</h1>
      <p class="lf-21__sub">Ship faster with Comet.</p>
      <label class="lf-21__field"><span class="lf-21__label">Email</span>
        <input type="email" autocomplete="email" placeholder="[email protected]" required></label>
      <label class="lf-21__field"><span class="lf-21__label">Password</span>
        <input type="password" autocomplete="current-password" placeholder="••••••••" required></label>
      <button class="lf-21__submit" type="submit">Continue</button>
    </form>
  </div>
</section>
```
## CSS
```css
@property --lf-21-spin {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.lf-21,
.lf-21 *,
.lf-21 *::before,
.lf-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-21 {
  --radius: 20px;
  --field-h: 48px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #07080d;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-21__wrap {
  position: relative;
  width: min(360px,100%);
  border-radius: var(--radius);
  padding: 2px;
  isolation: isolate;
}

.lf-21__wrap::before,
.lf-21__wrap::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  z-index: -1;
  background: conic-gradient(from var(--lf-21-spin),oklch(0.7 0.2 20),oklch(0.72 0.18 300),oklch(0.75 0.16 200),oklch(0.78 0.18 130),oklch(0.7 0.2 20));
  animation: lf-21-rotate 5s linear infinite;
}

.lf-21__wrap::after {
  filter: blur(16px);
  opacity: .7;
}

.lf-21__card {
  position: relative;
  border-radius: calc(var(--radius) - 2px);
  background: #12141d;
  padding: 34px 30px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  color: #eceef6;
}

.lf-21__h {
  font-size: 24px;
  font-weight: 700;
}

.lf-21__sub {
  font-size: 13.5px;
  color: #8b92a6;
  margin-top: -8px;
  margin-bottom: 4px;
}

.lf-21__field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.lf-21__label {
  font-size: 13px;
  font-weight: 600;
  color: #b7bdd0;
}

.lf-21__field input {
  height: var(--field-h);
  border: 1.5px solid #2a2f3d;
  border-radius: 11px;
  padding: 0 14px;
  font-size: 15px;
  color: #eceef6;
  background: #0e1019;
  transition: border-color .18s,box-shadow .18s;
}

.lf-21__field input::placeholder {
  color: #5f6780;
}

.lf-21__field input:focus-visible {
  outline: none;
  border-color: oklch(0.72 0.18 300);
  box-shadow: 0 0 0 4px oklch(0.72 0.18 300/.22);
}

.lf-21__submit {
  height: var(--field-h);
  margin-top: 4px;
  border: 0;
  border-radius: 11px;
  cursor: pointer;
  color: #0a0b10;
  font-size: 15px;
  font-weight: 700;
  background: linear-gradient(90deg,oklch(0.82 0.15 130),oklch(0.82 0.14 200));
  transition: filter .18s,transform .12s;
}

.lf-21__submit:hover {
  filter: brightness(1.08);
}

.lf-21__submit:active {
  transform: scale(.985);
}

.lf-21__submit:focus-visible {
  outline: 3px solid oklch(0.82 0.15 130/.6);
  outline-offset: 3px;
}

@keyframes lf-21-rotate {
  to {
    --lf-21-spin: 360deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .lf-21__wrap::before,
    .lf-21__wrap::after {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — an @property angle animates a conic-gradient ring on the GPU behind the card. */
```
