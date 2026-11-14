---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/pure-css-faq-accordion-details-summary/"
title: "Pure CSS FAQ Accordion with <details> and <summary> (No JavaScript)"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "The definitive FAQ pattern: native <details>/<summary> styled into a clean, modern question list — SEO-crawlable answers, built-in keyboard support,…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS FAQ Accordion with <details> and <summary> (No JavaScript)
Source: https://codefronts.com/navigation/css-accordions/pure-css-faq-accordion-details-summary/

The definitive FAQ pattern: native <details>/<summary> styled into a clean, modern question list — SEO-crawlable answers, built-in keyboard support, screen-reader disclosure semantics and Chromium find-in-page that auto-opens the matching answer. Zero JavaScript, zero ARIA wiring needed: the browser does the accessibility for you.
## HTML
```html
<section class="acc-01" aria-label="FAQ accordion demo">
  <div class="acc-01__wrap">
    <p class="acc-01__kicker">Support</p>
    <h3 class="acc-01__title">Frequently asked questions</h3>
    <details class="acc-01__item" open>
      <summary class="acc-01__q">How is this accordion accessible without any ARIA?</summary>
      <div class="acc-01__a"><p>Native <code>&lt;details&gt;</code>/<code>&lt;summary&gt;</code> ships with disclosure semantics built in: screen readers announce "collapsed/expanded", Enter and Space toggle it, and no JavaScript or role attributes are needed. You only style it.</p></div>
    </details>
    <details class="acc-01__item">
      <summary class="acc-01__q">Will search engines index the hidden answers?</summary>
      <div class="acc-01__a"><p>Yes — the answers are real HTML in the document, not injected by JS. Google indexes them, and Chromium's find-in-page even auto-expands the matching item.</p></div>
    </details>
    <details class="acc-01__item">
      <summary class="acc-01__q">Can I open more than one question at a time?</summary>
      <div class="acc-01__a"><p>By default, yes — every item is independent. If you want opening one to close the others, add the same <code>name</code> attribute to each details element (see the exclusive accordion demo).</p></div>
    </details>
    <details class="acc-01__item">
      <summary class="acc-01__q">Does it work with JavaScript disabled?</summary>
      <div class="acc-01__a"><p>Completely. The toggle behavior is implemented by the browser itself, so this FAQ works in reader modes, RSS contexts and script-blocked environments.</p></div>
    </details>
  </div>
</section>
```
## CSS
```css
.acc-01,
.acc-01 *,
.acc-01 *::before,
.acc-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-01 {
  --accent: oklch(0.55 0.17 255);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f4f6fa;
  padding: 40px 20px;
}

.acc-01__wrap {
  width: min(620px,100%);
  background: #fff;
  border-radius: 18px;
  padding: 36px 34px;
  box-shadow: 0 24px 60px -34px rgba(20,35,70,.35);
}

.acc-01__kicker {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.acc-01__title {
  font-size: 26px;
  font-weight: 800;
  color: #16233b;
  letter-spacing: -.02em;
  margin: 6px 0 14px;
}

.acc-01__item {
  border-top: 1px solid #e5e9f2;
}

.acc-01__q {
  list-style: none;
  cursor: pointer;
  position: relative;
  padding: 18px 44px 18px 0;
  font-size: 16.5px;
  font-weight: 650;
  color: #1c2b47;
  transition: color .15s;
}

.acc-01__q::-webkit-details-marker {
  display: none;
}

.acc-01__q::marker {
  display: none;
  content: "";
}

.acc-01__q:hover {
  color: var(--accent);
}

.acc-01__q::after {
  content: "";
  position: absolute;
  right: 6px;
  top: 50%;
  width: 9px;
  height: 9px;
  border-right: 2.5px solid currentColor;
  border-bottom: 2.5px solid currentColor;
  transform: translateY(-70%) rotate(45deg);
  transition: transform .3s cubic-bezier(.4,0,.2,1);
  opacity: .65;
}

.acc-01__item[open] > .acc-01__q::after {
  transform: translateY(-30%) rotate(225deg);
}

.acc-01__item[open] > .acc-01__q {
  color: var(--accent);
}

.acc-01__a {
  padding: 0 24px 20px 0;
  font-size: 15px;
  line-height: 1.65;
  color: #4a5872;
}

.acc-01__a code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .88em;
  background: #eef2f9;
  padding: 2px 5px;
  border-radius: 5px;
  color: #31446b;
}

.acc-01__item[open] .acc-01__a {
  animation: acc-01-in .35s cubic-bezier(.2,.7,.3,1);
}

@keyframes acc-01-in {
  from {
    opacity: 0;
    translate: 0 -8px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.acc-01__q:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  border-radius: 6px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-01__item[open] .acc-01__a {
    animation: none;
  }

  .acc-01__q::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — native <details>/<summary> provides the toggle, keyboard support and screen-reader disclosure semantics. The [open] attribute drives the chevron rotation and the answer's entrance animation entirely in CSS. */
```
