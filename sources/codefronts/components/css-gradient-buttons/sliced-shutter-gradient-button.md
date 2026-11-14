---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/sliced-shutter-gradient-button/"
title: "Sliced Shutter Gradient Button"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A CTA cut into six vertical strips that roll from a sunset gradient to an ocean gradient in a staggered piano-wave, with each strip windowing its exact…"
has_js: "false"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sliced Shutter Gradient Button
Source: https://codefronts.com/components/css-gradient-buttons/sliced-shutter-gradient-button/

A CTA cut into six vertical strips that roll from a sunset gradient to an ocean gradient in a staggered piano-wave, with each strip windowing its exact column of one continuous gradient so the seams are invisible.
## HTML
```html
<div class="gx-20">
  <article class="gx-20__article">
    <p class="gx-20__kicker">Case study · 07</p>
    <h2 class="gx-20__title">Concrete <em>&amp;</em> Fog</h2>
    <p class="gx-20__copy">How a brutalist archive in Porto was rebuilt as a single-page experience — 40 percent lighter, twice as legible.</p>
    <button class="gx-20__btn" type="button">
      <span class="gx-20__slices" aria-hidden="true">
        <span class="gx-20__slice"></span>
        <span class="gx-20__slice"></span>
        <span class="gx-20__slice"></span>
        <span class="gx-20__slice"></span>
        <span class="gx-20__slice"></span>
        <span class="gx-20__slice"></span>
      </span>
      <span class="gx-20__label">Read the study <span class="gx-20__arrow">→</span></span>
    </button>
    <p class="gx-20__note">12 min read — no paywall</p>
  </article>
</div>
```
## CSS
```css
.gx-20,
.gx-20 *,
.gx-20 *::before,
.gx-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gx-20 ::selection {
  background: #f43f5e;
  color: #fff7ed;
}

.gx-20 {
  --paper: #f4f1ea;
  --ink: #1c1917;
  --mut: #78716c;
  --n: 6;
  /* slice count */
  --grad-a: linear-gradient(110deg,#f59e0b 0%,#f43f5e 52%,#8b5cf6 100%);
  --grad-b: linear-gradient(110deg,#06b6d4 0%,#3b82f6 52%,#6366f1 100%);
  --ease: cubic-bezier(.76,0,.24,1);
  font-family: Georgia,'Times New Roman',serif;
  background: var(--paper);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.gx-20__article {
  max-width: 520px;
  text-align: center;
}

.gx-20__kicker {
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--mut);
}

.gx-20__title {
  margin-top: 14px;
  font-size: clamp(30px,5vw,42px);
  font-weight: 400;
  letter-spacing: -.01em;
  color: var(--ink);
  line-height: 1.1;
}

.gx-20__title em {
  font-style: italic;
}

.gx-20__copy {
  margin: 14px auto 0;
  max-width: 40ch;
  font-size: 15px;
  line-height: 1.6;
  color: var(--mut);
}
/* The button: six slices, each windowing its exact column of ONE
   oversized gradient via background-size / background-position math. */

.gx-20__btn {
  position: relative;
  display: inline-flex;
  margin-top: 28px;
  border: 0;
  padding: 0;
  background: none;
  border-radius: 14px;
  overflow: hidden;
  cursor: pointer;
  isolation: isolate;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  box-shadow: 0 18px 32px -16px rgba(244,63,94,.45);
  transition: box-shadow .6s ease,transform .3s ease;
}

.gx-20__btn:hover {
  box-shadow: 0 18px 32px -16px rgba(59,130,246,.5);
}

.gx-20__btn:active {
  transform: scale(.98);
}

.gx-20__btn:focus-visible {
  outline: 2.5px solid #3b82f6;
  outline-offset: 4px;
}

.gx-20__slices {
  position: absolute;
  inset: 0;
  display: flex;
  z-index: -1;
}

.gx-20__slice {
  position: relative;
  flex: 1;
  overflow: hidden;
  /* half-pixel overlap kills subpixel seams between flex slices */
  margin-right: -.5px;
}

.gx-20__slice:nth-child(1) {
  --i: 0;
}

.gx-20__slice:nth-child(2) {
  --i: 1;
}

.gx-20__slice:nth-child(3) {
  --i: 2;
}

.gx-20__slice:nth-child(4) {
  --i: 3;
}

.gx-20__slice:nth-child(5) {
  --i: 4;
}

.gx-20__slice:nth-child(6) {
  --i: 5;
}

.gx-20__slice::before,
.gx-20__slice::after {
  content: "";
  position: absolute;
  inset: 0;
  background-image: var(--grad-a);
  background-size: calc(var(--n)*100% + 3px) 100%;
  background-position: calc(var(--i)/(var(--n) - 1)*100%) 0;
  transition: transform .55s var(--ease);
  transition-delay: calc(var(--i)*55ms);
  will-change: transform;
}

.gx-20__slice::after {
  background-image: var(--grad-b);
  transform: translateY(100%);
}

.gx-20__btn:hover .gx-20__slice::before,
.gx-20__btn:focus-visible .gx-20__slice::before {
  transform: translateY(-100%);
}

.gx-20__btn:hover .gx-20__slice::after,
.gx-20__btn:focus-visible .gx-20__slice::after {
  transform: translateY(0);
}

.gx-20__label {
  position: relative;
  z-index: 1;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 17px 34px;
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  letter-spacing: .04em;
  text-shadow: 0 1px 2px rgba(0,0,0,.18);
  transition: letter-spacing .55s var(--ease);
}

.gx-20__btn:hover .gx-20__label,
.gx-20__btn:focus-visible .gx-20__label {
  letter-spacing: .09em;
}

.gx-20__arrow {
  display: inline-block;
  transition: transform .55s var(--ease) .12s;
}

.gx-20__btn:hover .gx-20__arrow,
.gx-20__btn:focus-visible .gx-20__arrow {
  transform: translateX(5px);
}

.gx-20__note {
  margin-top: 16px;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  font-size: 12px;
  letter-spacing: .03em;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .gx-20__slice::before,
    .gx-20__slice::after,
    .gx-20__label,
    .gx-20__arrow,
    .gx-20__btn {
    transition-duration: .01s;
    transition-delay: 0s;
  }
}
```
