---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/floating-label-login/"
title: "Floating Label Login"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "The Material-modern favourite: the placeholder text sits inside the field, then glides up to a miniaturised top label the moment the field is focused or…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Label Login
Source: https://codefronts.com/components/css-login-forms/floating-label-login/

The Material-modern favourite: the placeholder text sits inside the field, then glides up to a miniaturised top label the moment the field is focused or filled — done entirely in CSS, no JavaScript trackers.
## HTML
```html
<section class="lf-03">
  <form class="lf-03__form" novalidate>
    <h1 class="lf-03__h">Log in</h1>
    <div class="lf-03__field">
      <input class="lf-03__input" id="lf-03-email" type="email" autocomplete="email" placeholder=" " required>
      <label class="lf-03__label" for="lf-03-email">Email address</label>
    </div>
    <div class="lf-03__field">
      <input class="lf-03__input" id="lf-03-pw" type="password" autocomplete="current-password" placeholder=" " required>
      <label class="lf-03__label" for="lf-03-pw">Password</label>
    </div>
    <div class="lf-03__row">
      <label class="lf-03__remember"><input type="checkbox"> Remember me</label>
      <a class="lf-03__link" href="#">Forgot?</a>
    </div>
    <button class="lf-03__submit" type="submit">Continue</button>
  </form>
</section>
```
## CSS
```css
.lf-03,
.lf-03 *,
.lf-03 *::before,
.lf-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-03 {
  --accent: oklch(0.55 0.17 200);
  --field-h: 56px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #f3f6f8;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-03__form {
  width: min(360px,100%);
  background: #fff;
  border: 1px solid #e3e8ee;
  border-radius: 16px;
  padding: 32px 28px;
  display: flex;
  flex-direction: column;
  gap: 22px;
  box-shadow: 0 22px 50px -36px rgba(16,32,48,.5);
}

.lf-03__h {
  font-size: 24px;
  font-weight: 700;
  color: #12222b;
  letter-spacing: -.01em;
}

.lf-03__field {
  position: relative;
}

.lf-03__input {
  width: 100%;
  height: var(--field-h);
  border: 0;
  border-bottom: 2px solid #cdd6dd;
  background: transparent;
  padding: 18px 2px 4px;
  font-size: 16px;
  color: #12222b;
  transition: border-color .2s;
}

.lf-03__input:focus-visible {
  outline: none;
}

.lf-03__field:focus-within .lf-03__input {
  border-bottom-color: var(--accent);
}

.lf-03__label {
  position: absolute;
  left: 2px;
  top: 18px;
  font-size: 16px;
  color: #8695a0;
  pointer-events: none;
  transform-origin: left top;
  transition: transform .18s ease,color .18s ease;
}

.lf-03__input:focus + .lf-03__label,
.lf-03__input:not(:placeholder-shown) + .lf-03__label {
  transform: translateY(-16px) scale(.76);
  color: var(--accent);
}

.lf-03__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 13px;
}

.lf-03__remember {
  display: flex;
  align-items: center;
  gap: 7px;
  color: #54636d;
  cursor: pointer;
}

.lf-03__remember input {
  width: 15px;
  height: 15px;
  accent-color: var(--accent);
}

.lf-03__link {
  color: var(--accent);
  font-weight: 600;
  text-decoration: none;
}

.lf-03__link:hover {
  text-decoration: underline;
}

.lf-03__submit {
  height: 52px;
  border: 0;
  border-radius: 12px;
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  transition: filter .18s,transform .12s;
}

.lf-03__submit:hover {
  filter: brightness(1.06);
}

.lf-03__submit:active {
  transform: scale(.985);
}

.lf-03__submit:focus-visible {
  outline: 3px solid oklch(0.55 0.17 200/.5);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .lf-03__label,
    .lf-03__input {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the label floats via :placeholder-shown + :focus and a sibling combinator. */
```
