---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-label-inputs/dark-mode-floating-label-input-with-light-dark/"
title: "Dark Mode Floating Label Input with light-dark()"
section: "components"
category: "css-floating-label-inputs"
category_name: "CSS Floating Label Inputs"
description: "One set of rules, two themes: every colour in this field is a light-dark() pair, so the form follows the OS theme automatically — and an in-demo toggle flips…"
has_js: "false"
---

Here's a working CSS Floating Label Input from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Floating Label Input with light-dark()
Source: https://codefronts.com/components/css-floating-label-inputs/dark-mode-floating-label-input-with-light-dark/

One set of rules, two themes: every colour in this field is a light-dark() pair, so the form follows the OS theme automatically — and an in-demo toggle flips color-scheme live via :has(). High-contrast label states, autofill-safe fills, and a focus ring that stays visible on both backgrounds. Variation: a NEON RISE — in dark mode the floated label picks up a soft accent glow that reads as backlit; in light mode the glow resolves away via light-dark().
## HTML
```html
<section class="flb-11" aria-label="Dark mode floating label demo">
  <input type="checkbox" id="flb-11-dark" class="flb-11__switch">
  <div class="flb-11__stage">
    <form class="flb-11__form" novalidate>
      <div class="flb-11__head">
        <h3 class="flb-11__title">Welcome back</h3>
        <label class="flb-11__toggle" for="flb-11-dark"><span class="flb-11__knob" aria-hidden="true"></span><span class="flb-11__mode">Theme</span></label>
      </div>
      <div class="flb-11__field">
        <input class="flb-11__input" type="email" id="flb-11-email" name="email" placeholder=" " autocomplete="email">
        <label class="flb-11__label" for="flb-11-email">Email address</label>
      </div>
      <div class="flb-11__field">
        <input class="flb-11__input" type="password" id="flb-11-pass" name="password" placeholder=" " autocomplete="current-password">
        <label class="flb-11__label" for="flb-11-pass">Password</label>
      </div>
      <button class="flb-11__btn" type="button">Sign in</button>
    </form>
  </div>
</section>
```
## CSS
```css
.flb-11,
.flb-11 *,
.flb-11 *::before,
.flb-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.flb-11 {
  color-scheme: light;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
}

.flb-11:has(.flb-11__switch:checked) {
  color-scheme: dark;
}

.flb-11__switch {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.flb-11__stage {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  background: light-dark(#eef0f5,#0d1017);
  transition: background .3s;
}

.flb-11__form {
  width: min(380px,100%);
  background: light-dark(#ffffff,#171c28);
  border: 1px solid light-dark(#e3e6ee,#242c40);
  border-radius: 20px;
  padding: 30px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  box-shadow: 0 24px 60px -32px light-dark(rgba(24,28,60,.35),rgba(0,0,0,.7));
  transition: background .3s,border-color .3s;
}

.flb-11__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.flb-11__title {
  font-size: 23px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: light-dark(#181c2a,#eef1fa);
}

.flb-11__toggle {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  font-size: 12px;
  font-weight: 600;
  color: light-dark(#6a7086,#8b93ad);
}

.flb-11__knob {
  width: 38px;
  height: 22px;
  border-radius: 11px;
  background: light-dark(#cdd2e0,oklch(0.68 0.14 264));
  position: relative;
  transition: background .25s;
}

.flb-11__knob::after {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: #fff;
  transition: translate .25s;
}

.flb-11:has(.flb-11__switch:checked) .flb-11__knob::after {
  translate: 16px 0;
}

.flb-11__switch:focus-visible ~ .flb-11__stage .flb-11__knob {
  outline: 3px solid oklch(0.68 0.14 264 / .6);
  outline-offset: 2px;
}

.flb-11__field {
  position: relative;
}

.flb-11__input {
  width: 100%;
  height: 56px;
  padding: 22px 16px 6px;
  font-size: 16px;
  color: light-dark(#181c2a,#eef1fa);
  background: light-dark(#ffffff,#10141f);
  border: 1.5px solid light-dark(#d4d8e4,#2b3450);
  border-radius: 12px;
  outline: none;
  transition: border-color .2s,box-shadow .2s,background .3s;
}

.flb-11__input:focus {
  border-color: light-dark(oklch(0.52 0.18 264),oklch(0.72 0.14 264));
  box-shadow: 0 0 0 4px oklch(0.62 0.16 264 / .18);
}

.flb-11__label {
  position: absolute;
  left: 16px;
  top: 50%;
  translate: 0 -50%;
  font-size: 16px;
  color: light-dark(#71768b,#79809b);
  pointer-events: none;
  transform-origin: left center;
  transition: transform .18s,color .18s;
}

.flb-11__input:focus ~ .flb-11__label,
.flb-11__input:not(:placeholder-shown) ~ .flb-11__label {
  transform: translateY(-13px) scale(.72);
  letter-spacing: .04em;
  text-shadow: 0 0 14px light-dark(transparent,oklch(0.72 0.14 264 / .9));
}

.flb-11__input:focus ~ .flb-11__label {
  color: light-dark(oklch(0.52 0.18 264),oklch(0.75 0.13 264));
}

.flb-11__btn {
  height: 50px;
  border: none;
  border-radius: 12px;
  background: light-dark(oklch(0.52 0.18 264),oklch(0.72 0.14 264));
  color: light-dark(#ffffff,#0d1017);
  font-size: 15px;
  font-weight: 800;
  cursor: pointer;
  transition: filter .15s;
}

.flb-11__btn:hover {
  filter: brightness(1.1);
}

.flb-11__btn:focus-visible,
.flb-11__input:focus-visible {
  outline: 3px solid oklch(0.62 0.16 264 / .5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .flb-11 *,
    .flb-11 *::after {
    transition: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — every colour is a light-dark() pair; :has(checkbox:checked) flips color-scheme on the wrapper, re-resolving all tokens at once. In production, set color-scheme: light dark on :root and the OS decides. */
```
