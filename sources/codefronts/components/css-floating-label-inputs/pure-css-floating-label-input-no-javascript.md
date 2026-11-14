---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-label-inputs/pure-css-floating-label-input-no-javascript/"
title: "Pure CSS Floating Label Input (No JavaScript)"
section: "components"
category: "css-floating-label-inputs"
category_name: "CSS Floating Label Inputs"
description: "The canonical zero-dependency floating label: the label sits inside the field as ghost text, then floats up and shrinks the instant the user focuses or types…"
has_js: "false"
---

Here's a working CSS Floating Label Input from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Floating Label Input (No JavaScript)
Source: https://codefronts.com/components/css-floating-label-inputs/pure-css-floating-label-input-no-javascript/

The canonical zero-dependency floating label: the label sits inside the field as ghost text, then floats up and shrinks the instant the user focuses or types — driven entirely by :placeholder-shown and :focus, with no input listeners, no framework, and a perfect INP score.
## HTML
```html
<section class="flb-04" aria-label="Pure CSS floating label demo">
  <form class="flb-04__form" novalidate>
    <h3 class="flb-04__title">Sign in</h3>
    <div class="flb-04__field">
      <input class="flb-04__input" type="email" id="flb-04-email" name="email" placeholder=" " autocomplete="email">
      <label class="flb-04__label" for="flb-04-email">Email address</label>
    </div>
    <div class="flb-04__field">
      <input class="flb-04__input" type="text" id="flb-04-name" name="name" placeholder=" " autocomplete="name">
      <label class="flb-04__label" for="flb-04-name">Full name</label>
    </div>
    <button class="flb-04__btn" type="button">Continue</button>
  </form>
</section>
```
## CSS
```css
.flb-04,
.flb-04 *,
.flb-04 *::before,
.flb-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.flb-04 {
  --accent: oklch(0.55 0.18 264);
  --radius: 12px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f2f3f7;
  padding: 40px 20px;
}

.flb-04__form {
  width: min(380px,100%);
  background: #fff;
  border-radius: 20px;
  padding: 34px 30px;
  box-shadow: 0 24px 60px -30px rgba(24,28,60,.35);
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.flb-04__title {
  font-size: 24px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: #191c2b;
}

.flb-04__field {
  position: relative;
}

.flb-04__input {
  width: 100%;
  height: 56px;
  padding: 22px 16px 6px;
  font-size: 16px;
  color: #191c2b;
  background: #fff;
  border: 1.5px solid #d6d9e4;
  border-radius: var(--radius);
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.flb-04__input:hover {
  border-color: #b4b9cc;
}

.flb-04__input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.55 0.18 264 / .14);
}

.flb-04__label {
  position: absolute;
  left: 16px;
  top: 50%;
  translate: 0 -50%;
  font-size: 16px;
  color: #7a7f93;
  pointer-events: none;
  transform-origin: left center;
  transition: transform .18s ease,color .18s ease;
}

.flb-04__input:focus ~ .flb-04__label,
.flb-04__input:not(:placeholder-shown) ~ .flb-04__label {
  transform: translateY(-13px) scale(.72);
}

.flb-04__input:focus ~ .flb-04__label {
  color: var(--accent);
}

.flb-04__btn {
  height: 50px;
  border: none;
  border-radius: var(--radius);
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  transition: filter .15s,transform .15s;
}

.flb-04__btn:hover {
  filter: brightness(1.08);
}

.flb-04__btn:active {
  transform: scale(.98);
}

.flb-04__btn:focus-visible,
.flb-04__input:focus-visible {
  outline: 3px solid oklch(0.55 0.18 264 / .5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .flb-04__label,
    .flb-04__input,
    .flb-04__btn {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — placeholder=" " + :placeholder-shown / :focus drive the float entirely in CSS. Zero listeners, zero hydration, perfect INP. */
```
