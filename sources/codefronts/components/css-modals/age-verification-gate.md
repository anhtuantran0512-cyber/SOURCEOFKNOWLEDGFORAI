---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/age-verification-gate/"
title: "Age Verification Gate"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A full-screen entry gate that blurs and blocks the site until the visitor confirms they're of legal age — the zero-JS compliance overlay for alcohol, gaming…"
has_js: "false"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Age Verification Gate
Source: https://codefronts.com/components/css-modals/age-verification-gate/

A full-screen entry gate that blurs and blocks the site until the visitor confirms they're of legal age — the zero-JS compliance overlay for alcohol, gaming and regulated e-commerce, driven entirely by :has() and one checkbox.
## HTML
```html
<div class="cm-03">
  <article class="cm-03__content">
    <h1 class="cm-03__brand">CASK &amp; OAK</h1>
    <p class="cm-03__copy">Small-batch single malt, aged in highland oak. Explore the reserve collection.</p>
    <div class="cm-03__cards" aria-hidden="true"><span></span><span></span><span></span></div>
  </article>

  <input type="checkbox" id="cm-03-ok" class="cm-03__sr">
  <div class="cm-03__gate" role="dialog" aria-modal="true" aria-labelledby="cm-03-t" aria-describedby="cm-03-d">
    <div class="cm-03__panel">
      <div class="cm-03__mark" aria-hidden="true">21+</div>
      <h2 id="cm-03-t" class="cm-03__title">Are you of legal drinking age?</h2>
      <p id="cm-03-d" class="cm-03__desc">You must be 21 or older to enter this site.</p>
      <div class="cm-03__row">
        <label for="cm-03-ok" class="cm-03__btn cm-03__btn--yes" role="button" tabindex="0">Yes, I am 21+</label>
        <a href="https://responsibility.org" class="cm-03__btn cm-03__btn--no">No, exit</a>
      </div>
      <p class="cm-03__fine">Please enjoy responsibly.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.cm-03,
.cm-03 *,
.cm-03 *::before,
.cm-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cm-03 {
  --accent: oklch(0.76 0.13 70);
  position: relative;
  overflow: hidden;
  font-family: system-ui,'Segoe UI',sans-serif;
  min-height: 100dvh;
  background: radial-gradient(120% 120% at 50% 0%,#1a140c,#0b0805);
}

.cm-03__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.cm-03__content {
  min-height: 100dvh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 22px;
  padding: 40px;
  text-align: center;
  filter: blur(9px);
  transform: scale(1.02);
  transition: filter .5s,transform .5s;
}

.cm-03:has(#cm-03-ok:checked) .cm-03__content {
  filter: none;
  transform: none;
}

.cm-03__brand {
  font-size: clamp(38px,9vw,74px);
  font-weight: 800;
  letter-spacing: .12em;
  color: #f2e6d2;
}

.cm-03__copy {
  max-width: 44ch;
  font-size: 16px;
  line-height: 1.6;
  color: #b6a894;
}

.cm-03__cards {
  display: flex;
  gap: 16px;
  margin-top: 8px;
}

.cm-03__cards span {
  width: 90px;
  height: 120px;
  border-radius: 12px;
  background: linear-gradient(160deg,#2a2015,#1a130a);
  border: 1px solid #3a2c1a;
}

.cm-03__gate {
  position: fixed;
  inset: 0;
  z-index: 10;
  display: grid;
  place-items: center;
  padding: 24px;
  background: rgba(8,6,4,.78);
  backdrop-filter: blur(3px);
  transition: opacity .45s,visibility .45s;
}

.cm-03:has(#cm-03-ok:checked) .cm-03__gate {
  opacity: 0;
  visibility: hidden;
}

.cm-03__panel {
  width: min(430px,94vw);
  padding: 40px 34px;
  text-align: center;
  border-radius: 20px;
  background: linear-gradient(180deg,#1c150d,#140f08);
  border: 1px solid #3a2c1a;
  box-shadow: 0 40px 90px -30px #000;
}

.cm-03__mark {
  width: 78px;
  height: 78px;
  margin: 0 auto 22px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 26px;
  font-weight: 800;
  letter-spacing: .02em;
  color: var(--accent);
  border: 2px solid color-mix(in oklch,var(--accent) 55%,transparent);
  box-shadow: 0 0 40px -10px var(--accent),inset 0 0 24px -12px var(--accent);
}

.cm-03__title {
  font-size: 22px;
  font-weight: 700;
  color: #f3e9d8;
  margin-bottom: 10px;
}

.cm-03__desc {
  font-size: 14px;
  color: #a99a84;
  margin-bottom: 26px;
}

.cm-03__row {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
}

.cm-03__btn {
  cursor: pointer;
  padding: 13px 24px;
  border-radius: 11px;
  font: 600 14px system-ui;
  text-decoration: none;
  transition: filter .2s,background .2s,border-color .2s;
}

.cm-03__btn--yes {
  background: var(--accent);
  color: #1c1206;
  border: 1px solid var(--accent);
}

.cm-03__btn--yes:hover {
  filter: brightness(1.08);
}

.cm-03__btn--no {
  background: transparent;
  color: #a99a84;
  border: 1px solid #4a3a24;
}

.cm-03__btn--no:hover {
  border-color: #6a5436;
  color: #c9bba3;
}

.cm-03__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cm-03__fine {
  margin-top: 22px;
  font-size: 12px;
  letter-spacing: .06em;
  color: #7a6c56;
}

@media (prefers-reduced-motion: reduce) {
  .cm-03__content,
    .cm-03__gate {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
/* No JavaScript — one hidden checkbox + :has() blurs the page and hides the gate. */
```
