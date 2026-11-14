---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/card-flip-reset/"
title: "Card Flip Reset"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "The Forgot Password lives on the back of the login card."
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Card Flip Reset
Source: https://codefronts.com/components/css-login-forms/card-flip-reset/

The Forgot Password lives on the back of the login card. Click the reset link and the whole card rotates in 3D to reveal the recovery form — no page redirect, no glitchy bleed-through.
## HTML
```html
<section class="lf-11">
  <div class="lf-11__stage">
    <input type="checkbox" class="lf-11__flip" id="lf-11-flip" aria-label="Show password reset form">
    <div class="lf-11__card">
      <form class="lf-11__face lf-11__face--front" novalidate>
        <h2 class="lf-11__h">Sign in</h2>
        <input type="email" placeholder="Email" autocomplete="email" required>
        <input type="password" placeholder="Password" autocomplete="current-password" required>
        <button type="submit">Log in</button>
        <label class="lf-11__link" for="lf-11-flip">Forgot password?</label>
      </form>
      <form class="lf-11__face lf-11__face--back" novalidate>
        <h2 class="lf-11__h">Reset password</h2>
        <p class="lf-11__note">Enter your email and we'll send a reset link.</p>
        <input type="email" placeholder="Email" autocomplete="email" required>
        <button type="submit">Send link</button>
        <label class="lf-11__link" for="lf-11-flip">← Back to sign in</label>
      </form>
    </div>
  </div>
</section>
```
## CSS
```css
.lf-11,
.lf-11 *,
.lf-11 *::before,
.lf-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-11 {
  --accent: oklch(0.55 0.18 25);
  --radius: 12px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #f5f2ef;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-11__stage {
  width: min(360px,100%);
  perspective: 1400px;
}

.lf-11__flip {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}

.lf-11__card {
  position: relative;
  width: 100%;
  min-height: 400px;
  transform-style: preserve-3d;
  transition: transform .7s cubic-bezier(.4,0,.2,1);
}

.lf-11__flip:checked ~ .lf-11__card {
  transform: rotateY(180deg);
}

.lf-11__flip:focus-visible ~ .lf-11__card {
  outline: 3px solid oklch(0.55 0.18 25/.5);
  outline-offset: 6px;
  border-radius: 20px;
}

.lf-11__face {
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  background: #fff;
  border: 1px solid #eadfd6;
  border-radius: 18px;
  padding: 36px 32px;
  display: flex;
  flex-direction: column;
  gap: 13px;
  box-shadow: 0 24px 56px -38px rgba(60,30,10,.5);
}

.lf-11__face--back {
  transform: rotateY(180deg);
}

.lf-11__h {
  font-size: 23px;
  font-weight: 700;
  color: #2a1c12;
  margin-bottom: 4px;
}

.lf-11__note {
  font-size: 13.5px;
  line-height: 1.5;
  color: #8a7565;
  margin-top: -6px;
  margin-bottom: 4px;
}

.lf-11__face input {
  height: 46px;
  border: 1.5px solid #e0d3c8;
  border-radius: var(--radius);
  padding: 0 14px;
  font-size: 14.5px;
  color: #2a1c12;
  background: #fdfbf9;
  transition: border-color .18s,box-shadow .18s;
}

.lf-11__face input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.55 0.18 25/.16);
}

.lf-11__face button {
  height: 46px;
  margin-top: 2px;
  border: 0;
  border-radius: var(--radius);
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  transition: filter .18s,transform .12s;
}

.lf-11__face button:hover {
  filter: brightness(1.06);
}

.lf-11__face button:active {
  transform: scale(.985);
}

.lf-11__face button:focus-visible {
  outline: 3px solid oklch(0.55 0.18 25/.5);
  outline-offset: 2px;
}

.lf-11__link {
  align-self: center;
  font-size: 13px;
  color: var(--accent);
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
}

.lf-11__link:hover {
  text-decoration: underline;
}

@media (prefers-reduced-motion: reduce) {
  .lf-11__card {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a preserve-3d card rotates via a focusable checkbox; both faces hide their backface. */
```
