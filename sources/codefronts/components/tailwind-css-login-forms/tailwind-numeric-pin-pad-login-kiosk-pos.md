---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-numeric-pin-pad-login-kiosk-pos/"
title: "Tailwind Numeric PIN Pad Login for Kiosks and POS"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "A numeric PIN entry for kiosks, POS terminals and mobile web: a rigid 3&times;4 keypad of big round keys feeding a row of masked dots, with a press that…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Numeric PIN Pad Login for Kiosks and POS
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-numeric-pin-pad-login-kiosk-pos/

A numeric PIN entry for kiosks, POS terminals and mobile web: a rigid 3&times;4 keypad of big round keys feeding a row of masked dots, with a press that scales and a delete key. The port keeps the script to state and moves the filled-dot look to data-[on]:, so the handler sets an attribute instead of toggling a class name it has to remember.
## HTML
```html
<section class="tlf-27 w-full min-h-svh grid place-items-center bg-tlf27-stage font-tlf27-sans p-6">
  <form novalidate class="tlf-27-form w-[min(340px,100%)] p-8 text-center bg-tlf27-card border border-tlf27-edge rounded-[22px] shadow-[0_30px_70px_-44px_black]">
    <h1 class="mb-5 text-[19px] font-semibold text-tlf27-ink">Enter your PIN</h1>
    <div aria-hidden="true" class="tlf-27-dots flex justify-center gap-4 mb-7">
      <span class="size-3.5 rounded-full border-2 border-tlf27-dot bg-transparent transition-[background-color,border-color,scale] duration-150 data-[on]:bg-tlf27-acc data-[on]:border-tlf27-acc data-[on]:scale-115 motion-reduce:transition-colors"></span>
      <span class="size-3.5 rounded-full border-2 border-tlf27-dot bg-transparent transition-[background-color,border-color,scale] duration-150 data-[on]:bg-tlf27-acc data-[on]:border-tlf27-acc data-[on]:scale-115 motion-reduce:transition-colors"></span>
      <span class="size-3.5 rounded-full border-2 border-tlf27-dot bg-transparent transition-[background-color,border-color,scale] duration-150 data-[on]:bg-tlf27-acc data-[on]:border-tlf27-acc data-[on]:scale-115 motion-reduce:transition-colors"></span>
      <span class="size-3.5 rounded-full border-2 border-tlf27-dot bg-transparent transition-[background-color,border-color,scale] duration-150 data-[on]:bg-tlf27-acc data-[on]:border-tlf27-acc data-[on]:scale-115 motion-reduce:transition-colors"></span>
    </div>
    <input class="tlf-27-value" type="hidden" name="pin">
    <p class="tlf-27-status sr-only" role="status" aria-live="polite">0 of 4 digits entered</p>
    <div role="group" aria-label="PIN keypad" class="grid grid-cols-3 gap-3.5 justify-items-center">
      <button type="button" data-d="1" class="tlf-27-key size-16 rounded-full cursor-pointer bg-tlf27-key border-[1.5px] border-tlf27-keyedge text-tlf27-ink text-2xl font-medium transition-[background-color,border-color,scale] duration-100 hover:bg-tlf27-keyhover hover:border-tlf27-dot active:scale-90 active:bg-tlf27-press active:border-tlf27-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf27-ring motion-reduce:transition-colors motion-reduce:active:scale-100">1</button>
      <button type="button" data-d="2" class="tlf-27-key size-16 rounded-full cursor-pointer bg-tlf27-key border-[1.5px] border-tlf27-keyedge text-tlf27-ink text-2xl font-medium transition-[background-color,border-color,scale] duration-100 hover:bg-tlf27-keyhover hover:border-tlf27-dot active:scale-90 active:bg-tlf27-press active:border-tlf27-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf27-ring motion-reduce:transition-colors motion-reduce:active:scale-100">2</button>
      <button type="button" data-d="3" class="tlf-27-key size-16 rounded-full cursor-pointer bg-tlf27-key border-[1.5px] border-tlf27-keyedge text-tlf27-ink text-2xl font-medium transition-[background-color,border-color,scale] duration-100 hover:bg-tlf27-keyhover hover:border-tlf27-dot active:scale-90 active:bg-tlf27-press active:border-tlf27-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf27-ring motion-reduce:transition-colors motion-reduce:active:scale-100">3</button>
      <button type="button" data-d="4" class="tlf-27-key size-16 rounded-full cursor-pointer bg-tlf27-key border-[1.5px] border-tlf27-keyedge text-tlf27-ink text-2xl font-medium transition-[background-color,border-color,scale] duration-100 hover:bg-tlf27-keyhover hover:border-tlf27-dot active:scale-90 active:bg-tlf27-press active:border-tlf27-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf27-ring motion-reduce:transition-colors motion-reduce:active:scale-100">4</button>
      <button type="button" data-d="5" class="tlf-27-key size-16 rounded-full cursor-pointer bg-tlf27-key border-[1.5px] border-tlf27-keyedge text-tlf27-ink text-2xl font-medium transition-[background-color,border-color,scale] duration-100 hover:bg-tlf27-keyhover hover:border-tlf27-dot active:scale-90 active:bg-tlf27-press active:border-tlf27-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf27-ring motion-reduce:transition-colors motion-reduce:active:scale-100">5</button>
      <button type="button" data-d="6" class="tlf-27-key size-16 rounded-full cursor-pointer bg-tlf27-key border-[1.5px] border-tlf27-keyedge text-tlf27-ink text-2xl font-medium transition-[background-color,border-color,scale] duration-100 hover:bg-tlf27-keyhover hover:border-tlf27-dot active:scale-90 active:bg-tlf27-press active:border-tlf27-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf27-ring motion-reduce:transition-colors motion-reduce:active:scale-100">6</button>
      <button type="button" data-d="7" class="tlf-27-key size-16 rounded-full cursor-pointer bg-tlf27-key border-[1.5px] border-tlf27-keyedge text-tlf27-ink text-2xl font-medium transition-[background-color,border-color,scale] duration-100 hover:bg-tlf27-keyhover hover:border-tlf27-dot active:scale-90 active:bg-tlf27-press active:border-tlf27-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf27-ring motion-reduce:transition-colors motion-reduce:active:scale-100">7</button>
      <button type="button" data-d="8" class="tlf-27-key size-16 rounded-full cursor-pointer bg-tlf27-key border-[1.5px] border-tlf27-keyedge text-tlf27-ink text-2xl font-medium transition-[background-color,border-color,scale] duration-100 hover:bg-tlf27-keyhover hover:border-tlf27-dot active:scale-90 active:bg-tlf27-press active:border-tlf27-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf27-ring motion-reduce:transition-colors motion-reduce:active:scale-100">8</button>
      <button type="button" data-d="9" class="tlf-27-key size-16 rounded-full cursor-pointer bg-tlf27-key border-[1.5px] border-tlf27-keyedge text-tlf27-ink text-2xl font-medium transition-[background-color,border-color,scale] duration-100 hover:bg-tlf27-keyhover hover:border-tlf27-dot active:scale-90 active:bg-tlf27-press active:border-tlf27-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf27-ring motion-reduce:transition-colors motion-reduce:active:scale-100">9</button>
      <span aria-hidden="true" class="size-16"></span>
      <button type="button" data-d="0" class="tlf-27-key size-16 rounded-full cursor-pointer bg-tlf27-key border-[1.5px] border-tlf27-keyedge text-tlf27-ink text-2xl font-medium transition-[background-color,border-color,scale] duration-100 hover:bg-tlf27-keyhover hover:border-tlf27-dot active:scale-90 active:bg-tlf27-press active:border-tlf27-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf27-ring motion-reduce:transition-colors motion-reduce:active:scale-100">0</button>
      <button type="button" data-del aria-label="Delete last digit" class="tlf-27-key size-16 rounded-full cursor-pointer bg-tlf27-key border-[1.5px] border-tlf27-keyedge text-tlf27-mut text-xl transition-[background-color,border-color,scale] duration-100 hover:bg-tlf27-keyhover hover:border-tlf27-dot active:scale-90 active:bg-tlf27-press active:border-tlf27-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf27-ring motion-reduce:transition-colors motion-reduce:active:scale-100">&#9003;</button>
    </div>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf27-stage: #12151d;
  --color-tlf27-stage: oklch(0.18 0.012 265);
  --color-tlf27-card: #1a1f2b;
  --color-tlf27-card: oklch(0.23 0.014 265);
  --color-tlf27-edge: #262c3a;
  --color-tlf27-edge: oklch(0.28 0.016 265);
  --color-tlf27-key: #212635;
  --color-tlf27-key: oklch(0.26 0.016 265);
  --color-tlf27-keyhover: #2b3244;
  --color-tlf27-keyhover: oklch(0.31 0.018 265);
  --color-tlf27-keyedge: #333b4d;
  --color-tlf27-keyedge: oklch(0.33 0.018 265);
  --color-tlf27-dot: #4a5468;
  --color-tlf27-dot: oklch(0.43 0.02 265);
  --color-tlf27-ink: #e8ebf3;
  --color-tlf27-ink: oklch(0.93 0.008 265);
  --color-tlf27-mut: #a8b0c4;
  --color-tlf27-mut: oklch(0.75 0.018 265);
  --color-tlf27-acc: #7b90e8;
  --color-tlf27-acc: oklch(0.68 0.15 265);
  --color-tlf27-press: #2f3a5e;
  --color-tlf27-press: oklch(0.68 0.15 265 / 0.25);
  --color-tlf27-ring: #a3b2ef;
  --color-tlf27-ring: oklch(0.68 0.15 265 / 0.6);
  --font-tlf27-sans: 'Figtree', system-ui, sans-serif;
}

.tlf-27 {
  width: 100%;
  min-height: 100svh;
  color-scheme: dark;
}
```

## JavaScript
```js
const section = document.querySelector('.tlf-27');
const dots = [...section.querySelectorAll('.tlf-27-dots span')];
const value = section.querySelector('.tlf-27-value');
const status = section.querySelector('.tlf-27-status');
const MAX = dots.length;
let pin = '';

function render() {
  dots.forEach((d, i) => {
    if (i < pin.length) d.setAttribute('data-on', '');
    else d.removeAttribute('data-on');
  });
  value.value = pin;
  status.textContent = pin.length + ' of ' + MAX + ' digits entered';
}

section.querySelectorAll('.tlf-27-key').forEach((key) => {
  key.addEventListener('click', () => {
    if (key.hasAttribute('data-del')) pin = pin.slice(0, -1);
    else if (pin.length < MAX) pin += key.dataset.d;
    render();
    if (pin.length === MAX) setTimeout(() => { pin = ''; render(); }, 600);
  });
});

render();
```
