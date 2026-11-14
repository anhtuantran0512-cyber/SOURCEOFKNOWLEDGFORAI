---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-label-inputs/accessible-floating-label-input-aria-wcag/"
title: "Accessible Floating Label Input (ARIA + WCAG)"
section: "components"
category: "css-floating-label-inputs"
category_name: "CSS Floating Label Inputs"
description: "The floating label pattern audited: real for/id label binding, aria-describedby hint wiring, a required marker that isn't colour-only, WCAG-AA contrast in…"
has_js: "false"
---

Here's a working CSS Floating Label Input from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Floating Label Input (ARIA + WCAG)
Source: https://codefronts.com/components/css-floating-label-inputs/accessible-floating-label-input-aria-wcag/

The floating label pattern audited: real for/id label binding, aria-describedby hint wiring, a required marker that isn't colour-only, WCAG-AA contrast in both label states, a thick :focus-visible ring, and float sizes that never drop below readable — a reference implementation you can put in front of a screen reader with confidence. Variation: a NO-SHRINK float — the label barely scales (16px stays 13.6px), bolds instead, and grows an accent tick, so low-vision users never lose it.
## HTML
```html
<section class="flb-07" aria-label="Accessibility-first floating label demo">
  <form class="flb-07__form" novalidate>
    <h3 class="flb-07__title">Contact details</h3>
    <div class="flb-07__field">
      <input class="flb-07__input" type="text" id="flb-07-name" name="name" placeholder=" " required autocomplete="name" aria-describedby="flb-07-name-hint">
      <label class="flb-07__label" for="flb-07-name">Full name <span class="flb-07__req" aria-hidden="true">*</span></label>
      <p class="flb-07__hint" id="flb-07-name-hint">Required — as it appears on your ID</p>
    </div>
    <div class="flb-07__field">
      <input class="flb-07__input" type="tel" id="flb-07-tel" name="tel" placeholder=" " autocomplete="tel" aria-describedby="flb-07-tel-hint">
      <label class="flb-07__label" for="flb-07-tel">Phone number</label>
      <p class="flb-07__hint" id="flb-07-tel-hint">Optional — include country code</p>
    </div>
    <button class="flb-07__btn" type="submit">Save contact</button>
  </form>
</section>
```
## CSS
```css
.flb-07,
.flb-07 *,
.flb-07 *::before,
.flb-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.flb-07 {
  --accent: oklch(0.5 0.19 264);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #eef0f4;
  padding: 40px 20px;
}

.flb-07__form {
  width: min(400px,100%);
  background: #fff;
  border-radius: 18px;
  padding: 32px 30px;
  box-shadow: 0 20px 50px -28px rgba(24,28,60,.3);
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.flb-07__title {
  font-size: 23px;
  font-weight: 800;
  color: #171a26;
  letter-spacing: -.02em;
  margin-bottom: 14px;
}

.flb-07__field {
  position: relative;
  padding-bottom: 30px;
}

.flb-07__input {
  width: 100%;
  height: 58px;
  padding: 24px 16px 6px;
  font-size: 16px;
  color: #171a26;
  background: #fff;
  border: 2px solid #c2c7d4;
  border-radius: 10px;
  outline: none;
  transition: border-color .2s;
}

.flb-07__input:hover {
  border-color: #9aa0b2;
}

.flb-07__input:focus {
  border-color: var(--accent);
}

.flb-07__input:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.flb-07__label {
  position: absolute;
  left: 16px;
  top: 29px;
  translate: 0 -50%;
  font-size: 16px;
  color: #5a5f6e;
  pointer-events: none;
  transform-origin: left center;
  transition: transform .18s,color .18s;
}

.flb-07__input:focus ~ .flb-07__label,
.flb-07__input:not(:placeholder-shown) ~ .flb-07__label {
  transform: translateY(-15px) scale(.85);
  font-weight: 700;
}

.flb-07__label::before {
  content: "";
  display: inline-block;
  width: 0;
  height: 3px;
  border-radius: 2px;
  background: var(--accent);
  vertical-align: middle;
  transition: width .2s,margin-right .2s;
}

.flb-07__input:focus ~ .flb-07__label::before,
.flb-07__input:not(:placeholder-shown) ~ .flb-07__label::before {
  width: 12px;
  margin-right: 6px;
}

.flb-07__input:focus ~ .flb-07__label {
  color: var(--accent);
}

.flb-07__req {
  color: oklch(0.5 0.19 25);
  font-weight: 700;
}

.flb-07__hint {
  position: absolute;
  left: 2px;
  bottom: 6px;
  font-size: 12.5px;
  color: #5a5f6e;
  line-height: 1.35;
}

.flb-07__btn {
  height: 52px;
  border: none;
  border-radius: 10px;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  transition: filter .15s;
}

.flb-07__btn:hover {
  filter: brightness(1.12);
}

.flb-07__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .flb-07__label,
    .flb-07__input {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the accessibility layer is pure semantics: label[for]+id binding, aria-describedby hints, the required attribute, and :focus-visible rings. The float is the standard :placeholder-shown pattern. */
```
