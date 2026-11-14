---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-label-inputs/password-input-with-show-hide-toggle-and-floating-label/"
title: "Password Input with Show/Hide Toggle and Floating Label"
section: "components"
category: "css-floating-label-inputs"
category_name: "CSS Floating Label Inputs"
description: "The login-form workhorse: a floating label password field with an in-field visibility toggle that swaps type between password and text — the eye button is a…"
has_js: "true"
---

Here's a working CSS Floating Label Input from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Password Input with Show/Hide Toggle and Floating Label
Source: https://codefronts.com/components/css-floating-label-inputs/password-input-with-show-hide-toggle-and-floating-label/

The login-form workhorse: a floating label password field with an in-field visibility toggle that swaps type between password and text — the eye button is a real <button> with aria-pressed and a dynamic label, sized 44px for touch, and positioned so it never collides with the floating label or the value. Variation: a SPRINGY float — an overshoot cubic-bezier makes the label bounce past its floated position and settle, adding play without a single keyframe.
## HTML
```html
<section class="flb-15" aria-label="Password floating label with toggle demo">
  <form class="flb-15__form" novalidate>
    <h3 class="flb-15__title">Choose a password</h3>
    <div class="flb-15__field">
      <input class="flb-15__input" type="password" id="flb-15-pass" name="new-password" placeholder=" " autocomplete="new-password" minlength="8" aria-describedby="flb-15-hint">
      <label class="flb-15__label" for="flb-15-pass">Password</label>
      <button class="flb-15__eye" type="button" id="flb-15-toggle" aria-pressed="false" aria-label="Show password" aria-controls="flb-15-pass">
        <svg class="flb-15__ic flb-15__ic--show" aria-hidden="true" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.5-6.5 10-6.5S22 12 22 12s-3.5 6.5-10 6.5S2 12 2 12Z"></path><circle cx="12" cy="12" r="3"></circle></svg>
        <svg class="flb-15__ic flb-15__ic--hide" aria-hidden="true" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.5-6.5 10-6.5S22 12 22 12s-3.5 6.5-10 6.5S2 12 2 12Z"></path><circle cx="12" cy="12" r="3"></circle><path d="m4 4 16 16"></path></svg>
      </button>
      <p class="flb-15__hint" id="flb-15-hint">At least 8 characters</p>
    </div>
    <button class="flb-15__btn" type="submit">Create account</button>
  </form>
</section>
```
## CSS
```css
.flb-15,
.flb-15 *,
.flb-15 *::before,
.flb-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.flb-15 {
  --accent: oklch(0.55 0.18 264);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f1f2f7;
  padding: 40px 20px;
}

.flb-15__form {
  width: min(380px,100%);
  background: #fff;
  border-radius: 20px;
  padding: 32px 30px;
  box-shadow: 0 24px 60px -32px rgba(24,28,60,.35);
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.flb-15__title {
  font-size: 23px;
  font-weight: 800;
  color: #191c2b;
  letter-spacing: -.02em;
}

.flb-15__field {
  position: relative;
  padding-bottom: 24px;
}

.flb-15__input {
  width: 100%;
  height: 56px;
  padding: 22px 58px 6px 16px;
  font-size: 16px;
  color: #191c2b;
  background: #fff;
  border: 1.5px solid #d6d9e4;
  border-radius: 12px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.flb-15__input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.55 0.18 264 / .14);
}

.flb-15__label {
  position: absolute;
  left: 16px;
  top: 28px;
  translate: 0 -50%;
  font-size: 16px;
  color: #7a7f93;
  pointer-events: none;
  transform-origin: left center;
  transition: transform .5s cubic-bezier(.3,1.8,.4,.9),color .2s;
}

.flb-15__input:focus ~ .flb-15__label,
.flb-15__input:not(:placeholder-shown) ~ .flb-15__label {
  transform: translateY(-13px) scale(.72);
}

.flb-15__input:focus ~ .flb-15__label {
  color: var(--accent);
}

.flb-15__eye {
  position: absolute;
  right: 6px;
  top: 6px;
  width: 44px;
  height: 44px;
  display: grid;
  place-items: center;
  border: none;
  background: transparent;
  border-radius: 10px;
  color: #7a7f93;
  cursor: pointer;
  transition: color .15s,background .15s;
}

.flb-15__eye:hover {
  color: #191c2b;
  background: #f0f1f6;
}

.flb-15__eye:focus-visible {
  outline: 3px solid oklch(0.55 0.18 264 / .5);
  outline-offset: 1px;
}

.flb-15__ic {
  grid-area: 1/1;
  transition: opacity .15s;
}

.flb-15__ic--hide {
  opacity: 0;
}

.flb-15__eye[aria-pressed="true"] .flb-15__ic--show {
  opacity: 0;
}

.flb-15__eye[aria-pressed="true"] .flb-15__ic--hide {
  opacity: 1;
}

.flb-15__hint {
  position: absolute;
  left: 2px;
  bottom: 2px;
  font-size: 12.5px;
  color: #7a7f93;
}

.flb-15__btn {
  height: 50px;
  border: none;
  border-radius: 12px;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  transition: filter .15s;
}

.flb-15__btn:hover {
  filter: brightness(1.1);
}

.flb-15__btn:focus-visible,
.flb-15__input:focus-visible {
  outline: 3px solid oklch(0.55 0.18 264 / .5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .flb-15__label,
    .flb-15__input,
    .flb-15__ic {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const input = document.querySelector('#flb-15-pass');
  const btn = document.querySelector('#flb-15-toggle');
  btn.addEventListener('click', () => {
    const show = input.type === 'password';
    input.type = show ? 'text' : 'password';
    btn.setAttribute('aria-pressed', String(show));
    btn.setAttribute('aria-label', show ? 'Hide password' : 'Show password');
  });
})();
```
