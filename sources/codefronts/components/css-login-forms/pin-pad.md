---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/pin-pad/"
title: "Pin Pad"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "A numeric PIN entry for kiosks, POS terminals and mobile web: a rigid 3×4 keypad of big round touch buttons feeding a row of masked dots, with a satisfying…"
has_js: "true"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pin Pad
Source: https://codefronts.com/components/css-login-forms/pin-pad/

A numeric PIN entry for kiosks, POS terminals and mobile web: a rigid 3×4 keypad of big round touch buttons feeding a row of masked dots, with a satisfying press state and a delete key.
## HTML
```html
<section class="lf-27">
  <form class="lf-27__card" novalidate>
    <h1 class="lf-27__h">Enter your PIN</h1>
    <div class="lf-27__dots" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
    <input class="lf-27__value" type="hidden" name="pin">
    <div class="lf-27__pad" role="group" aria-label="PIN keypad">
      <button class="lf-27__key" type="button" data-d="1">1</button>
      <button class="lf-27__key" type="button" data-d="2">2</button>
      <button class="lf-27__key" type="button" data-d="3">3</button>
      <button class="lf-27__key" type="button" data-d="4">4</button>
      <button class="lf-27__key" type="button" data-d="5">5</button>
      <button class="lf-27__key" type="button" data-d="6">6</button>
      <button class="lf-27__key" type="button" data-d="7">7</button>
      <button class="lf-27__key" type="button" data-d="8">8</button>
      <button class="lf-27__key" type="button" data-d="9">9</button>
      <span class="lf-27__spacer" aria-hidden="true"></span>
      <button class="lf-27__key" type="button" data-d="0">0</button>
      <button class="lf-27__key lf-27__key--del" type="button" data-del aria-label="Delete last digit">⌫</button>
    </div>
  </form>
</section>
```
## CSS
```css
.lf-27,
.lf-27 *,
.lf-27 *::before,
.lf-27 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-27 {
  --accent: oklch(0.6 0.16 265);
  --key: 64px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #12151d;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-27__card {
  width: min(320px,100%);
  background: #1a1f2b;
  border: 1px solid #262c3a;
  border-radius: 22px;
  padding: 34px 28px;
  text-align: center;
  box-shadow: 0 30px 70px -44px #000;
}

.lf-27__h {
  font-size: 19px;
  font-weight: 600;
  color: #e8ebf3;
  margin-bottom: 20px;
}

.lf-27__dots {
  display: flex;
  justify-content: center;
  gap: 16px;
  margin-bottom: 28px;
}

.lf-27__dots span {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  border: 2px solid #3a4256;
  background: transparent;
  transition: background .18s,border-color .18s,transform .18s;
}

.lf-27__dots span.is-on {
  background: var(--accent);
  border-color: var(--accent);
  transform: scale(1.15);
}

.lf-27__pad {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 14px;
  justify-items: center;
}

.lf-27__key {
  width: var(--key);
  height: var(--key);
  border-radius: 50%;
  border: 1.5px solid #2c3342;
  cursor: pointer;
  background: #212635;
  color: #e8ebf3;
  font-size: 24px;
  font-weight: 500;
  transition: background .14s,transform .1s,border-color .14s;
}

.lf-27__key:hover {
  background: #283044;
  border-color: #3a4256;
}

.lf-27__key:active {
  transform: scale(.9);
  background: oklch(0.6 0.16 265/.25);
  border-color: var(--accent);
}

.lf-27__key:focus-visible {
  outline: 3px solid oklch(0.6 0.16 265/.6);
  outline-offset: 2px;
}

.lf-27__key--del {
  font-size: 20px;
  color: #98a0b4;
}

.lf-27__spacer {
  width: var(--key);
  height: var(--key);
}

@media (prefers-reduced-motion: reduce) {
  .lf-27 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
const sec = document.querySelector('.lf-27');
const dots = [...sec.querySelectorAll('.lf-27__dots span')];
const value = sec.querySelector('.lf-27__value');
const MAX = dots.length;
let pin = '';
const render = () => dots.forEach((d, i) => d.classList.toggle('is-on', i < pin.length));
sec.querySelectorAll('.lf-27__key').forEach((key) => {
  key.addEventListener('click', () => {
    if (key.hasAttribute('data-del')) { pin = pin.slice(0, -1); }
    else if (pin.length < MAX) { pin += key.dataset.d; }
    value.value = pin;
    render();
    if (pin.length === MAX) setTimeout(() => { pin = ''; value.value = ''; render(); }, 500);
  });
});
```
