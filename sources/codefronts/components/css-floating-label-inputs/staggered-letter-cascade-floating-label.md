---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-label-inputs/staggered-letter-cascade-floating-label/"
title: "Staggered Letter-Cascade Floating Label"
section: "components"
category: "css-floating-label-inputs"
category_name: "CSS Floating Label Inputs"
description: "The float becomes typography in motion: each letter of the label rises individually in a rippling cascade, like a wave rolling left to right — pure CSS…"
has_js: "false"
---

Here's a working CSS Floating Label Input from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Staggered Letter-Cascade Floating Label
Source: https://codefronts.com/components/css-floating-label-inputs/staggered-letter-cascade-floating-label/

The float becomes typography in motion: each letter of the label rises individually in a rippling cascade, like a wave rolling left to right — pure CSS transition-delay stagger per letter, zero keyframe JS, and the real accessible label text kept intact for screen readers underneath the animated letters.
## HTML
```html
<section class="flb-01" aria-label="Staggered letter cascade floating label demo">
  <form class="flb-01__form" novalidate>
    <h3 class="flb-01__title">Join the studio</h3>
    <div class="flb-01__field">
      <input class="flb-01__input" type="text" id="flb-01-name" name="name" placeholder=" " autocomplete="name">
      <label class="flb-01__label" for="flb-01-name">
        <span class="flb-01__sr">Your name</span>
        <span aria-hidden="true"><span class="flb-01__ch" style="--i:0">Y</span><span class="flb-01__ch" style="--i:1">o</span><span class="flb-01__ch" style="--i:2">u</span><span class="flb-01__ch" style="--i:3">r</span><span class="flb-01__ch flb-01__ch--sp" style="--i:4"> </span><span class="flb-01__ch" style="--i:5">n</span><span class="flb-01__ch" style="--i:6">a</span><span class="flb-01__ch" style="--i:7">m</span><span class="flb-01__ch" style="--i:8">e</span></span>
      </label>
    </div>
    <div class="flb-01__field">
      <input class="flb-01__input" type="email" id="flb-01-mail" name="email" placeholder=" " autocomplete="email">
      <label class="flb-01__label" for="flb-01-mail">
        <span class="flb-01__sr">Email</span>
        <span aria-hidden="true"><span class="flb-01__ch" style="--i:0">E</span><span class="flb-01__ch" style="--i:1">m</span><span class="flb-01__ch" style="--i:2">a</span><span class="flb-01__ch" style="--i:3">i</span><span class="flb-01__ch" style="--i:4">l</span></span>
      </label>
    </div>
    <button class="flb-01__btn" type="button">Apply</button>
  </form>
</section>
```
## CSS
```css
.flb-01,
.flb-01 *,
.flb-01 *::before,
.flb-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.flb-01 {
  --accent: oklch(0.6 0.19 320);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f6f0f6;
  padding: 40px 20px;
}

.flb-01__form {
  width: min(380px,100%);
  background: #fff;
  border-radius: 20px;
  padding: 34px 30px;
  box-shadow: 0 24px 60px -32px rgba(70,20,70,.35);
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.flb-01__title {
  font-size: 23px;
  font-weight: 800;
  color: #241a24;
  letter-spacing: -.02em;
}

.flb-01__field {
  position: relative;
}

.flb-01__input {
  width: 100%;
  height: 56px;
  padding: 22px 16px 6px;
  font-size: 16px;
  color: #241a24;
  background: #fff;
  border: 1.5px solid #e3d5e3;
  border-radius: 12px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.flb-01__input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.6 0.19 320 / .13);
}

.flb-01__label {
  position: absolute;
  left: 16px;
  top: 50%;
  translate: 0 -50%;
  font-size: 16px;
  color: #96829b;
  pointer-events: none;
}

.flb-01__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.flb-01__ch {
  display: inline-block;
  transform-origin: left bottom;
  transition: transform .34s cubic-bezier(.3,1.6,.4,1) calc(var(--i) * 30ms),color .25s calc(var(--i) * 30ms);
}

.flb-01__ch--sp {
  width: .35em;
}

.flb-01__input:focus ~ .flb-01__label .flb-01__ch,
.flb-01__input:not(:placeholder-shown) ~ .flb-01__label .flb-01__ch {
  transform: translateY(-14px) scale(.72);
  color: var(--accent);
}

.flb-01__btn {
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

.flb-01__btn:hover {
  filter: brightness(1.1);
}

.flb-01__btn:focus-visible,
.flb-01__input:focus-visible {
  outline: 3px solid oklch(0.6 0.19 320 / .5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .flb-01__ch {
    transition-delay: 0s;
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — each letter span carries an --i index; transition-delay: calc(var(--i) * 30ms) staggers one shared float trigger into a left-to-right wave. Real label text stays intact for screen readers in a visually-hidden span. */
```
