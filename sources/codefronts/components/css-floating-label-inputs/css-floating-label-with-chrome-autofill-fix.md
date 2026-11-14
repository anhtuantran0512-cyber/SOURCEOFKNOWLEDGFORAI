---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-label-inputs/css-floating-label-with-chrome-autofill-fix/"
title: "CSS Floating Label with Chrome Autofill Fix"
section: "components"
category: "css-floating-label-inputs"
category_name: "CSS Floating Label Inputs"
description: "The bug every login form ships with: Chrome autofills the email and the label crashes straight through the yellow text."
has_js: "false"
---

Here's a working CSS Floating Label Input from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Floating Label with Chrome Autofill Fix
Source: https://codefronts.com/components/css-floating-label-inputs/css-floating-label-with-chrome-autofill-fix/

The bug every login form ships with: Chrome autofills the email and the label crashes straight through the yellow text. This demo adds :autofill / :-webkit-autofill to the float selector so browser-filled values lift the label exactly like typed ones — and restyles the autofill highlight to match your theme. Variation: instead of shrinking in place, the label ESCAPES the field and docks above its top-left corner with spread letter-spacing — an eyebrow label.
## HTML
```html
<section class="flb-05" aria-label="Autofill-proof floating label demo">
  <form class="flb-05__form" novalidate>
    <h3 class="flb-05__title">Ship to</h3>
    <p class="flb-05__sub">Autofill this form from your browser — the labels stay floated.</p>
    <div class="flb-05__field">
      <input class="flb-05__input" type="text" id="flb-05-name" name="name" placeholder=" " autocomplete="name">
      <label class="flb-05__label" for="flb-05-name">Full name</label>
    </div>
    <div class="flb-05__field">
      <input class="flb-05__input" type="email" id="flb-05-email" name="email" placeholder=" " autocomplete="email">
      <label class="flb-05__label" for="flb-05-email">Email</label>
    </div>
    <div class="flb-05__field">
      <input class="flb-05__input" type="text" id="flb-05-street" name="street-address" placeholder=" " autocomplete="street-address">
      <label class="flb-05__label" for="flb-05-street">Street address</label>
    </div>
    <button class="flb-05__btn" type="submit">Save address</button>
  </form>
</section>
```
## CSS
```css
.flb-05,
.flb-05 *,
.flb-05 *::before,
.flb-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.flb-05 {
  --accent: oklch(0.6 0.15 180);
  --bg: #0f1420;
  --card: #171d2e;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg);
  padding: 40px 20px;
}

.flb-05__form {
  width: min(400px,100%);
  background: var(--card);
  border: 1px solid #232b42;
  border-radius: 20px;
  padding: 32px 30px;
  display: flex;
  flex-direction: column;
  gap: 28px;
}

.flb-05__title {
  font-size: 23px;
  font-weight: 800;
  color: #eef1fa;
  letter-spacing: -.02em;
}

.flb-05__sub {
  font-size: 13px;
  color: #8b93ad;
  margin-top: -12px;
  line-height: 1.5;
}

.flb-05__field {
  position: relative;
}

.flb-05__input {
  width: 100%;
  height: 56px;
  padding: 0 16px;
  font-size: 16px;
  color: #eef1fa;
  background: #101627;
  border: 1.5px solid #2b3450;
  border-radius: 12px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.flb-05__input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.6 0.15 180 / .16);
}

.flb-05__label {
  position: absolute;
  left: 16px;
  top: 50%;
  translate: 0 -50%;
  font-size: 16px;
  color: #79809b;
  pointer-events: none;
  transform-origin: left center;
  transition: transform .24s cubic-bezier(.3,.7,.3,1),color .24s,letter-spacing .24s;
}

.flb-05__input:focus ~ .flb-05__label,
.flb-05__input:not(:placeholder-shown) ~ .flb-05__label {
  transform: translate(-16px,-42px) scale(.7);
  letter-spacing: .08em;
  font-weight: 600;
}

.flb-05__input:autofill ~ .flb-05__label {
  transform: translate(-16px,-42px) scale(.7);
  letter-spacing: .08em;
  font-weight: 600;
}

.flb-05__input:-webkit-autofill ~ .flb-05__label {
  transform: translate(-16px,-42px) scale(.7);
  letter-spacing: .08em;
  font-weight: 600;
}

.flb-05__input:focus ~ .flb-05__label {
  color: var(--accent);
}

.flb-05__input:-webkit-autofill {
  -webkit-box-shadow: 0 0 0 1000px #101627 inset;
  -webkit-text-fill-color: #eef1fa;
  caret-color: #eef1fa;
  transition: background-color 99999s;
}

.flb-05__btn {
  height: 50px;
  border: none;
  border-radius: 12px;
  background: var(--accent);
  color: #04211e;
  font-size: 15px;
  font-weight: 800;
  cursor: pointer;
  transition: filter .15s;
}

.flb-05__btn:hover {
  filter: brightness(1.1);
}

.flb-05__btn:focus-visible,
.flb-05__input:focus-visible {
  outline: 3px solid oklch(0.6 0.15 180 / .5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .flb-05__label,
    .flb-05__input {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — :autofill and :-webkit-autofill (in separate rules) join the float selector so browser-autofilled values lift the label; an inset box-shadow re-skins Chrome's yellow autofill wash. */
```
