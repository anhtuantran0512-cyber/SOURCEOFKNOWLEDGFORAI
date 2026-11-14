---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-label-inputs/conic-border-beam-floating-label-property-animation/"
title: "Conic Border-Beam Floating Label (@property Animation)"
section: "components"
category: "css-floating-label-inputs"
category_name: "CSS Floating Label Inputs"
description: "A comet of light orbits the field's border while the label floats into a glowing chip: a registered @property custom angle drives a smoothly rotating…"
has_js: "false"
---

Here's a working CSS Floating Label Input from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Conic Border-Beam Floating Label (@property Animation)
Source: https://codefronts.com/components/css-floating-label-inputs/conic-border-beam-floating-label-property-animation/

A comet of light orbits the field's border while the label floats into a glowing chip: a registered @property custom angle drives a smoothly rotating conic-gradient border — the 'border beam' effect from top-tier AI product sites, done with zero JavaScript and zero SVG.
## HTML
```html
<section class="flb-03" aria-label="Conic border beam floating label demo">
  <form class="flb-03__form" novalidate>
    <h3 class="flb-03__title">Access the beta</h3>
    <div class="flb-03__field">
      <input class="flb-03__input" type="email" id="flb-03-mail" name="email" placeholder=" " autocomplete="email">
      <label class="flb-03__label" for="flb-03-mail">Work email</label>
    </div>
    <div class="flb-03__field">
      <input class="flb-03__input" type="text" id="flb-03-key" name="invite" placeholder=" " autocomplete="off">
      <label class="flb-03__label" for="flb-03-key">Invite code</label>
    </div>
    <button class="flb-03__btn" type="button">Unlock access</button>
  </form>
</section>
```
## CSS
```css
@property --flb03-a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.flb-03,
.flb-03 *,
.flb-03 *::before,
.flb-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.flb-03 {
  --accent: oklch(0.75 0.15 190);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #0a0d12;
  padding: 40px 20px;
}

.flb-03__form {
  width: min(380px,100%);
  background: #11151d;
  border: 1px solid #1f2633;
  border-radius: 20px;
  padding: 34px 30px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.flb-03__title {
  font-size: 23px;
  font-weight: 800;
  color: #e8eef5;
  letter-spacing: -.02em;
}

.flb-03__field {
  position: relative;
  border-radius: 13px;
}

.flb-03__field::before {
  content: "";
  position: absolute;
  inset: -1.5px;
  border-radius: 14px;
  background: conic-gradient(from var(--flb03-a),transparent 0deg 300deg,var(--accent) 330deg,transparent 360deg);
  opacity: 0;
  transition: opacity .3s;
  pointer-events: none;
}

.flb-03__field:focus-within::before {
  opacity: 1;
  animation: flb-03-orbit 2.6s linear infinite;
}

@keyframes flb-03-orbit {
  to {
    --flb03-a: 360deg;
  }
}

.flb-03__input {
  position: relative;
  width: 100%;
  height: 56px;
  padding: 22px 16px 6px;
  font-size: 16px;
  color: #e8eef5;
  background: #0d1117;
  border: 1.5px solid #273042;
  border-radius: 12px;
  outline: none;
  transition: border-color .2s;
}

.flb-03__input:focus {
  border-color: transparent;
}

.flb-03__label {
  position: absolute;
  left: 16px;
  top: 50%;
  translate: 0 -50%;
  font-size: 16px;
  color: #75809a;
  pointer-events: none;
  transform-origin: left center;
  padding: 2px 9px;
  margin-left: -9px;
  border-radius: 7px;
  transition: transform .28s cubic-bezier(.3,1.3,.4,1),color .25s,background-color .25s,box-shadow .25s;
  z-index: 1;
}

.flb-03__input:focus ~ .flb-03__label,
.flb-03__input:not(:placeholder-shown) ~ .flb-03__label {
  transform: translateY(-14px) scale(.74);
  background: #0a0d12;
  color: var(--accent);
  box-shadow: 0 0 16px -2px oklch(0.75 0.15 190 / .45);
}

.flb-03__btn {
  height: 50px;
  border: none;
  border-radius: 12px;
  background: var(--accent);
  color: #04252a;
  font-size: 15px;
  font-weight: 800;
  cursor: pointer;
  transition: filter .15s,box-shadow .2s;
}

.flb-03__btn:hover {
  filter: brightness(1.1);
  box-shadow: 0 0 24px -6px var(--accent);
}

.flb-03__btn:focus-visible,
.flb-03__input:focus-visible {
  outline: 3px solid oklch(0.75 0.15 190 / .55);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .flb-03__field:focus-within::before {
    animation: none;
  }

  .flb-03__label {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — @property registers --flb03-a as a typed <angle>, making the conic-gradient border interpolable; @keyframes spins it only while :focus-within matches. The floated label lands in a glowing chip lit by the same accent. */
```
