---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-label-inputs/gradient-ink-floating-label-with-animated-underline-draw/"
title: "Gradient-Ink Floating Label with Animated Underline Draw"
section: "components"
category: "css-floating-label-inputs"
category_name: "CSS Floating Label Inputs"
description: "The floated label turns into flowing gradient ink: background-clip:text pours an animated three-stop gradient through the letters while a matching gradient…"
has_js: "false"
---

Here's a working CSS Floating Label Input from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient-Ink Floating Label with Animated Underline Draw
Source: https://codefronts.com/components/css-floating-label-inputs/gradient-ink-floating-label-with-animated-underline-draw/

The floated label turns into flowing gradient ink: background-clip:text pours an animated three-stop gradient through the letters while a matching gradient underline draws itself beneath the input — a premium 'ink signature' feel for hero forms, waitlists and product launches.
## HTML
```html
<section class="flb-02" aria-label="Gradient ink floating label demo">
  <form class="flb-02__form" novalidate>
    <h3 class="flb-02__title">Reserve your invite</h3>
    <div class="flb-02__field">
      <input class="flb-02__input" type="text" id="flb-02-handle" name="nickname" placeholder=" " autocomplete="nickname">
      <label class="flb-02__label" for="flb-02-handle">Pick a handle</label>
    </div>
    <div class="flb-02__field">
      <input class="flb-02__input" type="email" id="flb-02-mail" name="email" placeholder=" " autocomplete="email">
      <label class="flb-02__label" for="flb-02-mail">Email address</label>
    </div>
    <button class="flb-02__btn" type="button">Join the waitlist</button>
  </form>
</section>
```
## CSS
```css
.flb-02,
.flb-02 *,
.flb-02 *::before,
.flb-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.flb-02 {
  --ink: linear-gradient(90deg,oklch(0.55 0.2 300),oklch(0.6 0.18 220),oklch(0.62 0.19 20),oklch(0.55 0.2 300));
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #141118;
  padding: 40px 20px;
}

.flb-02__form {
  width: min(390px,100%);
  background: #1d1924;
  border: 1px solid #2e2839;
  border-radius: 20px;
  padding: 34px 30px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.flb-02__title {
  font-size: 23px;
  font-weight: 800;
  color: #f2eef7;
  letter-spacing: -.02em;
}

.flb-02__field {
  position: relative;
}

.flb-02__input {
  width: 100%;
  height: 56px;
  padding: 22px 16px 6px;
  font-size: 16px;
  color: #f2eef7;
  background: #161320;
  border: 1.5px solid #332c42;
  border-radius: 12px 12px 4px 4px;
  outline: none;
  transition: border-color .2s;
}

.flb-02__input:focus {
  border-color: #4a4060;
}

.flb-02__field::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 2.5px;
  border-radius: 2px;
  background: var(--ink) 0 0/220% 100%;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .4s cubic-bezier(.25,.8,.3,1) .12s;
}

.flb-02__input:focus ~ .flb-02__label ~ .flb-02__nope {
  display: none;
}

.flb-02__field:focus-within::after,
.flb-02__field:has(.flb-02__input:not(:placeholder-shown))::after {
  transform: scaleX(1);
  animation: flb-02-flow 4s linear infinite;
}

.flb-02__label {
  position: absolute;
  left: 16px;
  top: 50%;
  translate: 0 -50%;
  font-size: 16px;
  pointer-events: none;
  transform-origin: left center;
  background: var(--ink) 0 0/220% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: #8d84a0;
  transition: transform .25s cubic-bezier(.3,1.2,.4,1),-webkit-text-fill-color .3s;
}

.flb-02__input:focus ~ .flb-02__label,
.flb-02__input:not(:placeholder-shown) ~ .flb-02__label {
  transform: translateY(-13px) scale(.74);
  font-weight: 700;
  -webkit-text-fill-color: transparent;
  animation: flb-02-flow 4s linear infinite;
}

@keyframes flb-02-flow {
  to {
    background-position: -220% 0;
  }
}

.flb-02__btn {
  height: 50px;
  border: none;
  border-radius: 12px;
  background: var(--ink) 0 0/220% 100%;
  color: #fff;
  font-size: 15px;
  font-weight: 800;
  cursor: pointer;
  transition: filter .15s;
}

.flb-02__btn:hover {
  filter: brightness(1.15);
}

.flb-02__btn:focus-visible,
.flb-02__input:focus-visible {
  outline: 3px solid oklch(0.6 0.18 220 / .6);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .flb-02__label,
    .flb-02__field::after {
    animation: none;
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — background-clip:text paints an animated gradient through the floated label (revealed by flipping -webkit-text-fill-color to transparent), while the field's ::after draws a matching gradient underline via scaleX. */
```
