---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/otp-verify/"
title: "OTP Verify"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "The multi-factor confirmation screen: six evenly-sized digit boxes in a grid that auto-advance as you type, accept a full paste, and backspace back — the…"
has_js: "true"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: OTP Verify
Source: https://codefronts.com/components/css-login-forms/otp-verify/

The multi-factor confirmation screen: six evenly-sized digit boxes in a grid that auto-advance as you type, accept a full paste, and backspace back — the standard email / SMS code entry, done accessibly.
## HTML
```html
<section class="lf-25">
  <form class="lf-25__card" novalidate>
    <h1 class="lf-25__h">Verify your identity</h1>
    <p class="lf-25__sub">Enter the 6-digit code we sent to your email.</p>
    <div class="lf-25__otp" role="group" aria-label="6-digit verification code">
      <input class="lf-25__box" type="text" inputmode="numeric" autocomplete="one-time-code" maxlength="1" pattern="[0-9]" placeholder="•" aria-label="Digit 1">
      <input class="lf-25__box" type="text" inputmode="numeric" maxlength="1" pattern="[0-9]" placeholder="•" aria-label="Digit 2">
      <input class="lf-25__box" type="text" inputmode="numeric" maxlength="1" pattern="[0-9]" placeholder="•" aria-label="Digit 3">
      <input class="lf-25__box" type="text" inputmode="numeric" maxlength="1" pattern="[0-9]" placeholder="•" aria-label="Digit 4">
      <input class="lf-25__box" type="text" inputmode="numeric" maxlength="1" pattern="[0-9]" placeholder="•" aria-label="Digit 5">
      <input class="lf-25__box" type="text" inputmode="numeric" maxlength="1" pattern="[0-9]" placeholder="•" aria-label="Digit 6">
    </div>
    <button class="lf-25__submit" type="submit">Verify</button>
    <p class="lf-25__foot">Didn't get it? <a href="#">Resend code</a></p>
  </form>
</section>
```
## CSS
```css
.lf-25,
.lf-25 *,
.lf-25 *::before,
.lf-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-25 {
  --accent: oklch(0.56 0.18 265);
  --box: 52px;
  --radius: 11px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #eef1f7;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-25__card {
  width: min(400px,100%);
  background: #fff;
  border: 1px solid #e5e9f2;
  border-radius: 18px;
  padding: 34px 30px;
  text-align: center;
  box-shadow: 0 22px 50px -38px rgba(16,24,60,.5);
}

.lf-25__h {
  font-size: 22px;
  font-weight: 700;
  color: #1a2237;
}

.lf-25__sub {
  font-size: 13.5px;
  color: #767d97;
  margin: 6px 0 22px;
  line-height: 1.5;
}

.lf-25__otp {
  display: grid;
  grid-template-columns: repeat(6,1fr);
  gap: 9px;
  margin-bottom: 22px;
}

.lf-25__box {
  height: var(--box);
  min-width: 0;
  text-align: center;
  font-size: 22px;
  font-weight: 700;
  color: #1a2237;
  border: 1.5px solid #d5dbe8;
  border-radius: var(--radius);
  background: #fafbfe;
  transition: border-color .16s,box-shadow .16s,transform .12s;
}

.lf-25__box::placeholder {
  color: #c3c9d8;
}

.lf-25__box:not(:placeholder-shown) {
  border-color: var(--accent);
  background: oklch(0.56 0.18 265/.05);
}

.lf-25__box:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.56 0.18 265/.2);
  transform: translateY(-2px);
}

.lf-25__submit {
  width: 100%;
  height: 50px;
  border: 0;
  border-radius: var(--radius);
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  transition: filter .18s,transform .12s;
}

.lf-25__submit:hover {
  filter: brightness(1.07);
}

.lf-25__submit:active {
  transform: scale(.99);
}

.lf-25__submit:focus-visible {
  outline: 3px solid oklch(0.56 0.18 265/.5);
  outline-offset: 2px;
}

.lf-25__foot {
  font-size: 13px;
  color: #767d97;
  margin-top: 16px;
}

.lf-25__foot a {
  color: var(--accent);
  font-weight: 600;
  text-decoration: none;
}

.lf-25__foot a:hover {
  text-decoration: underline;
}

@media (max-width: 420px) {
  .lf-25 {
    --box: 46px;
  }

  .lf-25__box {
    font-size: 19px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .lf-25 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
const boxes = [...document.querySelectorAll('.lf-25__box')];
boxes.forEach((box, i) => {
  box.addEventListener('input', () => {
    box.value = box.value.replace(/[^0-9]/g, '').slice(0, 1);
    if (box.value && i < boxes.length - 1) boxes[i + 1].focus();
  });
  box.addEventListener('keydown', (e) => {
    if (e.key === 'Backspace' && !box.value && i > 0) boxes[i - 1].focus();
  });
  box.addEventListener('paste', (e) => {
    e.preventDefault();
    const digits = (e.clipboardData.getData('text') || '').replace(/[^0-9]/g, '').split('');
    boxes.forEach((b, j) => { if (digits[j] != null) b.value = digits[j]; });
    boxes[Math.min(digits.length, boxes.length) - 1]?.focus();
  });
});
```
