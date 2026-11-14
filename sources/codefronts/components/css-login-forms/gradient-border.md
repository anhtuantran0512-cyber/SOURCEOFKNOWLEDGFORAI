---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/gradient-border/"
title: "Gradient Border"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "A dark-mode SaaS card wrapped in a fine multi-colour gradient hairline — achieved without nested wrapper divs, using the modern border background-clip trick…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Border
Source: https://codefronts.com/components/css-login-forms/gradient-border/

A dark-mode SaaS card wrapped in a fine multi-colour gradient hairline — achieved without nested wrapper divs, using the modern border background-clip trick for a crisp, single-element frame.
## HTML
```html
<section class="lf-14">
  <form class="lf-14__card" novalidate>
    <h1 class="lf-14__h">Sign in</h1>
    <p class="lf-14__sub">Access your dashboard.</p>
    <label class="lf-14__field"><span class="lf-14__label">Email</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required></label>
    <label class="lf-14__field"><span class="lf-14__label">Password</span>
      <input type="password" autocomplete="current-password" placeholder="••••••••" required></label>
    <button class="lf-14__submit" type="submit">Continue</button>
  </form>
</section>
```
## CSS
```css
.lf-14,
.lf-14 *,
.lf-14 *::before,
.lf-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-14 {
  --radius: 18px;
  --field-h: 48px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #0b0d13;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-14__card {
  width: min(360px,100%);
  border: 1.5px solid transparent;
  border-radius: var(--radius);
  padding: 34px 30px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  color: #e9ecf5;
  background: linear-gradient(#151823,#151823) padding-box, linear-gradient(135deg,oklch(0.7 0.2 20),oklch(0.7 0.18 300),oklch(0.75 0.16 200)) border-box;
  box-shadow: 0 30px 70px -44px #000;
}

.lf-14__h {
  font-size: 23px;
  font-weight: 700;
}

.lf-14__sub {
  font-size: 13.5px;
  color: #8b92a6;
  margin-top: -8px;
  margin-bottom: 4px;
}

.lf-14__field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.lf-14__label {
  font-size: 13px;
  font-weight: 600;
  color: #b7bdd0;
}

.lf-14__field input {
  height: var(--field-h);
  border: 1.5px solid #2a2f3d;
  border-radius: 11px;
  padding: 0 14px;
  font-size: 15px;
  color: #e9ecf5;
  background: #101320;
  transition: border-color .18s,box-shadow .18s;
}

.lf-14__field input::placeholder {
  color: #5f6780;
}

.lf-14__field input:focus-visible {
  outline: none;
  border-color: oklch(0.7 0.18 300);
  box-shadow: 0 0 0 4px oklch(0.7 0.18 300/.22);
}

.lf-14__submit {
  height: var(--field-h);
  margin-top: 4px;
  border: 0;
  border-radius: 11px;
  cursor: pointer;
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  background: linear-gradient(135deg,oklch(0.65 0.2 20),oklch(0.62 0.18 300));
  transition: filter .18s,transform .12s;
}

.lf-14__submit:hover {
  filter: brightness(1.08);
}

.lf-14__submit:active {
  transform: scale(.985);
}

.lf-14__submit:focus-visible {
  outline: 3px solid oklch(0.7 0.18 300/.6);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .lf-14 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — a single-element gradient frame via background-clip padding-box + border-box. */
```
