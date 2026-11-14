---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/stripe-inspired-minimalist/"
title: "Stripe-Inspired Minimalist"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "Crisp, flat, geometric fintech excellence: high-contrast type, generous field padding, and the signature two-layer soft shadow that makes a card float just…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stripe-Inspired Minimalist
Source: https://codefronts.com/components/css-login-forms/stripe-inspired-minimalist/

Crisp, flat, geometric fintech excellence: high-contrast type, generous field padding, and the signature two-layer soft shadow that makes a card float just enough. Zero fluff, all polish.
## HTML
```html
<section class="lf-05">
  <form class="lf-05__card" novalidate>
    <div class="lf-05__brand" aria-hidden="true">▮ Payflow</div>
    <h1 class="lf-05__h">Sign in to your account</h1>
    <label class="lf-05__field">
      <span class="lf-05__label">Email</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required>
    </label>
    <label class="lf-05__field">
      <span class="lf-05__label">Password</span>
      <input type="password" autocomplete="current-password" placeholder="Enter your password" required>
    </label>
    <button class="lf-05__submit" type="submit">Continue</button>
    <div class="lf-05__divider"><span>or</span></div>
    <button class="lf-05__ghost" type="button">Single sign-on (SSO)</button>
    <p class="lf-05__foot">Don't have an account? <a href="#">Sign up</a></p>
  </form>
</section>
```
## CSS
```css
.lf-05,
.lf-05 *,
.lf-05 *::before,
.lf-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-05 {
  --accent: oklch(0.53 0.2 277);
  --radius: 8px;
  --field-h: 44px;
  --pad: 12px 14px;
  --shadow: 0 1px 3px rgba(15,23,42,.1),0 1px 2px rgba(15,23,42,.06);
  font-family: ui-sans-serif,'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #f6f9fc;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-05__card {
  width: min(360px,100%);
  background: #fff;
  border-radius: 14px;
  padding: 34px 30px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: 0 8px 24px rgba(15,23,42,.08),0 2px 4px rgba(15,23,42,.04);
}

.lf-05__brand {
  font-size: 15px;
  font-weight: 700;
  color: var(--accent);
  letter-spacing: -.01em;
}

.lf-05__h {
  font-size: 20px;
  font-weight: 600;
  color: #1a1f36;
  letter-spacing: -.01em;
  margin-bottom: 2px;
}

.lf-05__field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.lf-05__label {
  font-size: 13px;
  font-weight: 600;
  color: #3c4257;
}

.lf-05__field input {
  height: var(--field-h);
  border: 1px solid #e0e4eb;
  border-radius: var(--radius);
  padding: var(--pad);
  font-size: 14.5px;
  color: #1a1f36;
  box-shadow: var(--shadow);
  transition: border-color .15s,box-shadow .15s;
}

.lf-05__field input::placeholder {
  color: #a3acc2;
}

.lf-05__field input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px oklch(0.53 0.2 277/.22);
}

.lf-05__submit {
  height: var(--field-h);
  border: 0;
  border-radius: var(--radius);
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 14.5px;
  font-weight: 600;
  box-shadow: var(--shadow);
  transition: filter .15s,transform .12s;
}

.lf-05__submit:hover {
  filter: brightness(1.07);
}

.lf-05__submit:active {
  transform: translateY(1px);
}

.lf-05__submit:focus-visible {
  outline: 3px solid oklch(0.53 0.2 277/.5);
  outline-offset: 2px;
}

.lf-05__divider {
  display: flex;
  align-items: center;
  gap: 12px;
  color: #8792a8;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: .06em;
}

.lf-05__divider::before,
.lf-05__divider::after {
  content: "";
  flex: 1;
  height: 1px;
  background: #e6e9f0;
}

.lf-05__ghost {
  height: var(--field-h);
  border: 1px solid #e0e4eb;
  border-radius: var(--radius);
  cursor: pointer;
  background: #fff;
  color: #1a1f36;
  font-size: 14px;
  font-weight: 600;
  box-shadow: var(--shadow);
  transition: background .15s;
}

.lf-05__ghost:hover {
  background: #f6f9fc;
}

.lf-05__ghost:focus-visible {
  outline: 3px solid oklch(0.53 0.2 277/.4);
  outline-offset: 2px;
}

.lf-05__foot {
  font-size: 13px;
  color: #697386;
  text-align: center;
}

.lf-05__foot a {
  color: var(--accent);
  font-weight: 600;
  text-decoration: none;
}

.lf-05__foot a:hover {
  text-decoration: underline;
}

@media (prefers-reduced-motion: reduce) {
  .lf-05 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — the whole look is layered box-shadow, hairline borders and a soft focus halo. */
```
