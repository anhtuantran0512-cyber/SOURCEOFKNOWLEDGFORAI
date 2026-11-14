---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-label-inputs/responsive-floating-label-for-mobile-no-ios-zoom/"
title: "Responsive Floating Label for Mobile (No iOS Zoom)"
section: "components"
category: "css-floating-label-inputs"
category_name: "CSS Floating Label Inputs"
description: "The mobile survival kit for floating labels: 16px minimum input text so iOS Safari never zoom-jumps the viewport, clamp()-fluid field heights and label…"
has_js: "false"
---

Here's a working CSS Floating Label Input from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Floating Label for Mobile (No iOS Zoom)
Source: https://codefronts.com/components/css-floating-label-inputs/responsive-floating-label-for-mobile-no-ios-zoom/

The mobile survival kit for floating labels: 16px minimum input text so iOS Safari never zoom-jumps the viewport, clamp()-fluid field heights and label sizes, ≥48px touch targets, thumb-friendly spacing, and a float distance that scales with the field so labels never collide with text on a 320px screen. Variation: the label floats into a tinted HIGHLIGHT LANE — a soft accent band fades in across the top of the field, giving the small label its own visible track at every width.
## HTML
```html
<section class="flb-13" aria-label="Responsive mobile floating label demo">
  <form class="flb-13__form" novalidate>
    <h3 class="flb-13__title">Get a quote</h3>
    <p class="flb-13__sub">Resize this panel — type, spacing and float distance scale fluidly.</p>
    <div class="flb-13__field">
      <input class="flb-13__input" type="text" id="flb-13-name" name="name" placeholder=" " autocomplete="name">
      <label class="flb-13__label" for="flb-13-name">Full name</label>
    </div>
    <div class="flb-13__field">
      <input class="flb-13__input" type="tel" id="flb-13-tel" name="tel" placeholder=" " inputmode="tel" autocomplete="tel">
      <label class="flb-13__label" for="flb-13-tel">Mobile number</label>
    </div>
    <div class="flb-13__field">
      <input class="flb-13__input" type="text" id="flb-13-zip" name="postal-code" placeholder=" " inputmode="numeric" autocomplete="postal-code">
      <label class="flb-13__label" for="flb-13-zip">ZIP / Postcode</label>
    </div>
    <button class="flb-13__btn" type="button">Send my quote</button>
  </form>
</section>
```
## CSS
```css
.flb-13,
.flb-13 *,
.flb-13 *::before,
.flb-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.flb-13 {
  --accent: oklch(0.6 0.16 150);
  --gap: clamp(14px,4vw,22px);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #eff4ef;
  padding: clamp(16px,5vw,48px) clamp(12px,4vw,24px);
}

.flb-13__form {
  width: min(420px,100%);
  background: #fff;
  border-radius: clamp(14px,3vw,22px);
  padding: clamp(20px,6vw,36px) clamp(16px,5vw,32px);
  box-shadow: 0 22px 55px -30px rgba(20,50,25,.35);
  display: flex;
  flex-direction: column;
  gap: var(--gap);
}

.flb-13__title {
  font-size: clamp(20px,5.5vw,26px);
  font-weight: 800;
  color: #17251a;
  letter-spacing: -.02em;
}

.flb-13__sub {
  font-size: clamp(12.5px,3.4vw,14px);
  color: #5f7264;
  line-height: 1.5;
  margin-top: calc(var(--gap) * -.55);
}

.flb-13__field {
  position: relative;
}

.flb-13__input {
  width: 100%;
  height: clamp(54px,13vw,60px);
  padding: clamp(20px,5vw,24px) 16px clamp(4px,1.5vw,7px);
  font-size: max(16px,clamp(16px,4.2vw,17px));
  color: #17251a;
  background: #fff;
  border: 1.5px solid #ccd8cf;
  border-radius: 12px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.flb-13__input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.6 0.16 150 / .15);
}

.flb-13__label {
  position: absolute;
  left: 16px;
  top: 50%;
  translate: 0 -50%;
  font-size: max(16px,clamp(16px,4.2vw,17px));
  color: #6d7f72;
  pointer-events: none;
  transform-origin: left center;
  transition: transform .18s,color .18s;
  z-index: 2;
}

.flb-13__field::before {
  content: "";
  position: absolute;
  left: 2px;
  right: 2px;
  top: 2px;
  height: clamp(22px,5.5vw,26px);
  border-radius: 10px 10px 0 0;
  background: oklch(0.6 0.16 150 / 0);
  transition: background .25s;
  pointer-events: none;
  z-index: 1;
}

.flb-13__field:focus-within::before,
.flb-13__field:has(.flb-13__input:not(:placeholder-shown))::before {
  background: oklch(0.6 0.16 150 / .12);
}

.flb-13__input:focus ~ .flb-13__label,
.flb-13__input:not(:placeholder-shown) ~ .flb-13__label {
  transform: translateY(clamp(-14px,-3vw,-12px)) scale(.7);
}

.flb-13__input:focus ~ .flb-13__label {
  color: var(--accent);
}

.flb-13__btn {
  height: clamp(48px,12vw,54px);
  border: none;
  border-radius: 12px;
  background: var(--accent);
  color: #fff;
  font-size: clamp(15px,4vw,16px);
  font-weight: 700;
  cursor: pointer;
  transition: filter .15s;
}

.flb-13__btn:hover {
  filter: brightness(1.08);
}

.flb-13__btn:focus-visible,
.flb-13__input:focus-visible {
  outline: 3px solid oklch(0.6 0.16 150 / .5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .flb-13__label,
    .flb-13__input {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — clamp() drives fluid field heights, paddings and float distance; a hard max(16px, …) floor on input font-size prevents the iOS Safari focus-zoom. */
```
