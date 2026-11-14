---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/css-gradient-ghost-button-hover-fill/"
title: "CSS Gradient Ghost Button Hover Fill"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "An editorial ghost button with a gradient border and gradient text that floods with its full teal-to-lime fill on hover via a scaleY-unrolling pseudo-element."
has_js: "false"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Ghost Button Hover Fill
Source: https://codefronts.com/components/css-gradient-buttons/css-gradient-ghost-button-hover-fill/

An editorial ghost button with a gradient border and gradient text that floods with its full teal-to-lime fill on hover via a scaleY-unrolling pseudo-element.
## HTML
```html
<div class="gb-05">
  <article class="gb-05__article">
    <p class="gb-05__kicker">Field Notes · Issue 07</p>
    <h3 class="gb-05__h">The quiet return of the kitchen garden</h3>
    <p class="gb-05__p">Twelve growers on why small plots, old seeds and slow seasons are winning back a generation raised on same-day delivery.</p>
    <div class="gb-05__actions">
      <button class="gb-05__ghost" type="button"><span>Read the story</span></button>
      <button class="gb-05__plain" type="button">Save for later</button>
    </div>
  </article>
</div>
```
## CSS
```css
.gb-05,
.gb-05 *,
.gb-05 *::before,
.gb-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-05 ::selection {
  background: #0d9488;
  color: #fff;
}

.gb-05 {
  --teal: #0d9488;
  --emerald: #10b981;
  --lime: #84cc16;
  --ink: #1a2e2a;
  --paper: #f7f9f4;
  font-family: Georgia,"Times New Roman",serif;
  background: var(--paper);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.gb-05__article {
  max-width: 460px;
  width: 100%;
  border-top: 3px solid var(--ink);
  padding-top: 28px;
}

.gb-05__kicker {
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 2.5px;
  text-transform: uppercase;
  color: var(--teal);
  margin-bottom: 14px;
}

.gb-05__h {
  font-size: 30px;
  line-height: 1.2;
  font-weight: 700;
  color: var(--ink);
  margin-bottom: 14px;
  letter-spacing: -.3px;
}

.gb-05__p {
  font-size: 15.5px;
  line-height: 1.7;
  color: #5b6b64;
  margin-bottom: 30px;
}

.gb-05__actions {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
}
/* Ghost baseline: transparent body, gradient only on the 2px border
   and the text. The full gradient fill lives on ::before at scaleY(0)
   and unrolls upward on hover — transform only, fully compositable. */

.gb-05__ghost {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  padding: 14px 30px;
  border: 2px solid transparent;
  border-radius: 10px;
  background: linear-gradient(var(--paper),var(--paper)) padding-box, linear-gradient(100deg,var(--teal),var(--emerald) 55%,var(--lime)) border-box;
  font-family: inherit;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  color: transparent;
  -webkit-tap-highlight-color: transparent;
  transition: box-shadow .35s ease;
}

.gb-05__ghost span {
  background: linear-gradient(100deg,var(--teal),var(--emerald) 55%,var(--lime));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  transition: color .28s ease .06s;
}

.gb-05__ghost::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(100deg,var(--teal),var(--emerald) 55%,var(--lime));
  transform: scaleY(0);
  transform-origin: bottom;
  transition: transform .38s cubic-bezier(.65,0,.35,1);
}

.gb-05__ghost:hover::before,
.gb-05__ghost:focus-visible::before {
  transform: scaleY(1);
}

.gb-05__ghost:hover span,
.gb-05__ghost:focus-visible span {
  color: #fff;
  transition-delay: .1s;
}

.gb-05__ghost:hover {
  box-shadow: 0 10px 24px -10px rgba(13,148,136,.5);
}

.gb-05__ghost:active::before {
  filter: brightness(.94);
}

.gb-05__ghost:focus-visible {
  outline: 3px solid var(--emerald);
  outline-offset: 3px;
}

.gb-05__plain {
  padding: 14px 8px;
  border: none;
  background: none;
  font-family: inherit;
  font-size: 15px;
  font-weight: 700;
  color: #87958e;
  cursor: pointer;
  text-decoration: underline;
  text-underline-offset: 4px;
  transition: color .25s ease;
}

.gb-05__plain:hover {
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .gb-05__ghost,
    .gb-05__ghost::before,
    .gb-05__ghost span {
    transition: none;
  }
}
```
