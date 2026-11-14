---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-label-inputs/css-auto-growing-textarea-with-floating-label/"
title: "CSS Auto-Growing Textarea with Floating Label"
section: "components"
category: "css-floating-label-inputs"
category_name: "CSS Floating Label Inputs"
description: "Floating labels on multi-line input, solved: the label pins to the TOP of the textarea (not vertical center), floats into a frosted chip so multi-line text…"
has_js: "false"
---

Here's a working CSS Floating Label Input from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Auto-Growing Textarea with Floating Label
Source: https://codefronts.com/components/css-floating-label-inputs/css-auto-growing-textarea-with-floating-label/

Floating labels on multi-line input, solved: the label pins to the TOP of the textarea (not vertical center), floats into a frosted chip so multi-line text scrolls cleanly beneath it, and the field itself auto-grows with content via field-sizing:content — the 2024 CSS property that retires every autosize JS library.
## HTML
```html
<section class="flb-14" aria-label="Textarea floating label demo">
  <form class="flb-14__form" novalidate>
    <h3 class="flb-14__title">Tell us what happened</h3>
    <div class="flb-14__field">
      <input class="flb-14__input" type="text" id="flb-14-subject" name="subject" placeholder=" ">
      <label class="flb-14__label" for="flb-14-subject">Subject</label>
    </div>
    <div class="flb-14__field flb-14__field--area">
      <textarea class="flb-14__area" id="flb-14-msg" name="message" placeholder=" " rows="3" maxlength="600" aria-describedby="flb-14-msg-hint"></textarea>
      <label class="flb-14__label flb-14__label--area" for="flb-14-msg">Describe the issue</label>
      <p class="flb-14__hint" id="flb-14-msg-hint">The field grows as you type — up to 600 characters</p>
    </div>
    <button class="flb-14__btn" type="button">Submit report</button>
  </form>
</section>
```
## CSS
```css
.flb-14,
.flb-14 *,
.flb-14 *::before,
.flb-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.flb-14 {
  --accent: oklch(0.55 0.16 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #eef1f6;
  padding: 40px 20px;
}

.flb-14__form {
  width: min(440px,100%);
  background: #fff;
  border-radius: 20px;
  padding: 32px 30px;
  box-shadow: 0 24px 60px -32px rgba(24,34,64,.35);
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.flb-14__title {
  font-size: 23px;
  font-weight: 800;
  color: #1a2030;
  letter-spacing: -.02em;
}

.flb-14__field {
  position: relative;
}

.flb-14__input {
  width: 100%;
  height: 56px;
  padding: 22px 16px 6px;
  font-size: 16px;
  color: #1a2030;
  background: #fff;
  border: 1.5px solid #d3d8e4;
  border-radius: 12px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.flb-14__area {
  width: 100%;
  min-height: 120px;
  max-height: 320px;
  padding: 14px 16px 14px;
  font-size: 16px;
  font-family: inherit;
  line-height: 1.55;
  color: #1a2030;
  background: #fff;
  border: 1.5px solid #d3d8e4;
  border-radius: 12px;
  outline: none;
  resize: vertical;
  field-sizing: content;
  transition: border-color .2s,box-shadow .2s;
}

.flb-14__input:focus,
.flb-14__area:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.55 0.16 250 / .13);
}

.flb-14__label {
  position: absolute;
  left: 16px;
  top: 50%;
  translate: 0 -50%;
  font-size: 16px;
  color: #7a8299;
  pointer-events: none;
  transform-origin: left center;
  transition: transform .22s,color .22s,background-color .22s;
  z-index: 2;
}

.flb-14__label--area {
  top: 26px;
  padding: 3px 10px;
  margin-left: -10px;
  border-radius: 8px 8px 8px 0;
}

.flb-14__input:focus ~ .flb-14__label,
.flb-14__input:not(:placeholder-shown) ~ .flb-14__label {
  transform: translateY(-13px) scale(.72);
}

.flb-14__area:focus ~ .flb-14__label--area,
.flb-14__area:not(:placeholder-shown) ~ .flb-14__label--area {
  transform: translate(-16px,-34px) scale(.8);
  background: var(--accent);
  color: #fff;
}

.flb-14__input:focus ~ .flb-14__label {
  color: var(--accent);
}

.flb-14__area:focus ~ .flb-14__label--area {
  color: #fff;
}

.flb-14__hint {
  font-size: 12.5px;
  color: #7a8299;
  margin-top: 6px;
  line-height: 1.4;
}

.flb-14__btn {
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

.flb-14__btn:hover {
  filter: brightness(1.1);
}

.flb-14__btn:focus-visible,
.flb-14__input:focus-visible,
.flb-14__area:focus-visible {
  outline: 3px solid oklch(0.55 0.16 250 / .5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .flb-14__label,
    .flb-14__input,
    .flb-14__area {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — field-sizing:content auto-grows the textarea between min/max-height; the label anchors to the first text line and floats into a backdrop-filter chip so scrolling text stays legible beneath it. */
```
