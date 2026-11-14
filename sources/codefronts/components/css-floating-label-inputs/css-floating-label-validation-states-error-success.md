---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-label-inputs/css-floating-label-validation-states-error-success/"
title: "CSS Floating Label Validation States (Error + Success)"
section: "components"
category: "css-floating-label-inputs"
category_name: "CSS Floating Label Inputs"
description: "CSS-only inline validation done politely: fields stay neutral until the user has actually interacted, then :user-invalid turns the border and floated label…"
has_js: "false"
---

Here's a working CSS Floating Label Input from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Floating Label Validation States (Error + Success)
Source: https://codefronts.com/components/css-floating-label-inputs/css-floating-label-validation-states-error-success/

CSS-only inline validation done politely: fields stay neutral until the user has actually interacted, then :user-invalid turns the border and floated label red with a subtle shake, and :user-valid confirms with green and a checkmark — no JavaScript validators, no premature red walls on page load. Variation: the label performs a full 3D rotateX flip as it floats — a card-flip motion that visually stamps the new state.
## HTML
```html
<section class="flb-06" aria-label="Floating label validation demo">
  <form class="flb-06__form">
    <h3 class="flb-06__title">Create account</h3>
    <div class="flb-06__field">
      <input class="flb-06__input" type="email" id="flb-06-email" name="email" placeholder=" " required autocomplete="email" aria-describedby="flb-06-email-msg">
      <label class="flb-06__label" for="flb-06-email">Email address</label>
      <p class="flb-06__msg" id="flb-06-email-msg">Enter a valid email, e.g. [email protected]</p>
    </div>
    <div class="flb-06__field">
      <input class="flb-06__input" type="text" id="flb-06-user" name="username" placeholder=" " required minlength="4" pattern="[a-zA-Z0-9_]+" autocomplete="username" aria-describedby="flb-06-user-msg">
      <label class="flb-06__label" for="flb-06-user">Username</label>
      <p class="flb-06__msg" id="flb-06-user-msg">4+ characters — letters, numbers, underscores</p>
    </div>
    <button class="flb-06__btn" type="submit">Sign up</button>
  </form>
</section>
```
## CSS
```css
.flb-06,
.flb-06 *,
.flb-06 *::before,
.flb-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.flb-06 {
  --accent: oklch(0.55 0.18 264);
  --err: oklch(0.55 0.19 25);
  --ok: oklch(0.58 0.15 155);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f4f3f0;
  padding: 40px 20px;
}

.flb-06__form {
  width: min(400px,100%);
  background: #fff;
  border-radius: 20px;
  padding: 32px 30px;
  box-shadow: 0 24px 60px -32px rgba(40,36,20,.35);
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.flb-06__title {
  font-size: 23px;
  font-weight: 800;
  color: #221f18;
  letter-spacing: -.02em;
  margin-bottom: 12px;
}

.flb-06__field {
  position: relative;
  padding-bottom: 26px;
}

.flb-06__input {
  width: 100%;
  height: 56px;
  padding: 22px 44px 6px 16px;
  font-size: 16px;
  color: #221f18;
  background: #fff;
  border: 1.5px solid #d9d6cd;
  border-radius: 12px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.flb-06__input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.55 0.18 264 / .13);
}

.flb-06__label {
  position: absolute;
  left: 16px;
  top: 28px;
  translate: 0 -50%;
  font-size: 16px;
  color: #8a8578;
  pointer-events: none;
  transform-origin: left center;
  transition: transform .4s cubic-bezier(.35,.7,.3,1),color .2s;
}

.flb-06__input:focus ~ .flb-06__label,
.flb-06__input:not(:placeholder-shown) ~ .flb-06__label {
  transform: perspective(320px) translateY(-13px) rotateX(360deg) scale(.72);
}

.flb-06__input:focus ~ .flb-06__label {
  color: var(--accent);
}

.flb-06__msg {
  position: absolute;
  left: 2px;
  bottom: 4px;
  font-size: 12px;
  color: #9a9588;
  transition: color .2s;
  line-height: 1.3;
}

.flb-06__field:has(.flb-06__input:user-invalid) {
  animation: flb-06-shake .3s ease;
}

.flb-06__input:user-invalid {
  border-color: var(--err);
  box-shadow: 0 0 0 4px oklch(0.55 0.19 25 / .12);
}

.flb-06__input:user-invalid ~ .flb-06__label {
  color: var(--err);
}

.flb-06__input:user-invalid ~ .flb-06__msg {
  color: var(--err);
  font-weight: 600;
}

.flb-06__input:user-valid {
  border-color: var(--ok);
}

.flb-06__input:user-valid ~ .flb-06__label {
  color: var(--ok);
}

.flb-06__field::after {
  content: "✓";
  position: absolute;
  right: 16px;
  top: 28px;
  translate: 0 -50%;
  font-size: 17px;
  font-weight: 800;
  color: var(--ok);
  opacity: 0;
  transition: opacity .2s;
}

.flb-06__field:has(.flb-06__input:user-valid)::after {
  opacity: 1;
}

@keyframes flb-06-shake {
  20% {
    transform: translateX(-5px);
  }

  40% {
    transform: translateX(5px);
  }

  60% {
    transform: translateX(-3px);
  }

  80% {
    transform: translateX(3px);
  }
}

.flb-06__btn {
  height: 50px;
  border: none;
  border-radius: 12px;
  background: #221f18;
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  transition: filter .15s;
}

.flb-06__btn:hover {
  filter: brightness(1.25);
}

.flb-06__btn:focus-visible,
.flb-06__input:focus-visible {
  outline: 3px solid oklch(0.55 0.18 264 / .5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .flb-06__field:has(.flb-06__input:user-invalid) {
    animation: none;
  }

  .flb-06__label,
    .flb-06__input {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — :user-invalid / :user-valid apply error and success palettes only AFTER the user interacts; native constraint validation (required, type=email, minlength, pattern) does the checking. */
```
