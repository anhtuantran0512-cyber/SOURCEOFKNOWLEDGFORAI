---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/css-gradient-text-clipping/"
title: "CSS Gradient Text / Clipping"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "A type-specimen screen of gradient text done properly: a static aurora headline, an animated flowing display line, a conic-stamped numeral and a subtle…"
has_js: "false"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Text / Clipping
Source: https://codefronts.com/design-styles/css-gradient-ui/css-gradient-text-clipping/

A type-specimen screen of gradient text done properly: a static aurora headline, an animated flowing display line, a conic-stamped numeral and a subtle two-tone body lockup — with the accessibility rule most tutorials skip.
## HTML
```html
<div class="cgu-12-group">
<section class="cgu-12" aria-label="CSS gradient text clipping demos">
  <div class="cgu-12__inner">
    <header class="cgu-12__head">
      <p class="cgu-12__eyebrow">12 · Gradient text</p>
    </header>
    <h2 class="cgu-12__display">Paint moves.<br>Glyphs hold still.</h2>
    <p class="cgu-12__flowline">This line's gradient flows through the letters forever.</p>
    <div class="cgu-12__row">
      <div class="cgu-12__numeral" aria-hidden="true">27</div>
      <div class="cgu-12__copy">
        <h3 class="cgu-12__h3">The four required lines</h3>
        <p class="cgu-12__body">Background gradient, <strong>-webkit-background-clip: text</strong>, the unprefixed clip, and <strong>transparent color</strong> — plus a <strong>@supports guard</strong> so unsupported engines show solid readable text instead of nothing. That guard is the difference between a demo and production.</p>
        <p class="cgu-12__note">← A conic gradient clips just as happily as a linear one.</p>
      </div>
    </div>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-12-group {
  display: block;
  width: 100%;
}

.cgu-12,
.cgu-12 *,
.cgu-12 *::before,
.cgu-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgu-12 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #eef0ff;
  background: radial-gradient(110% 80% at 50% 108%,#141028 0%,#0a0912 55%);
}

.cgu-12__inner {
  width: min(880px,100%);
  display: grid;
  gap: 34px;
}

.cgu-12__head {
  text-align: center;
}

.cgu-12__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #c4b5fd;
}

.cgu-12__display {
  font-size: clamp(44px,8vw,104px);
  font-weight: 900;
  letter-spacing: -.035em;
  line-height: .98;
  text-align: center;
  text-wrap: balance;
  color: #dbeafe;
}

@supports (background-clip: text) or (-webkit-background-clip: text) {
  .cgu-12__display {
    background: linear-gradient(100deg,#7dd3fc 0%,#c4b5fd 45%,#f9a8d4 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }
}

.cgu-12__flowline {
  font-size: clamp(19px,3vw,30px);
  font-weight: 800;
  letter-spacing: -.01em;
  text-align: center;
  color: #fca5a5;
}

@supports (background-clip: text) or (-webkit-background-clip: text) {
  .cgu-12__flowline {
    background: linear-gradient(90deg,#f472b6,#fbbf24,#34d399,#38bdf8,#f472b6);
    background-size: 250% 100%;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    animation: cgu12-flow 6s linear infinite;
  }
}

.cgu-12__row {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 38px;
  align-items: center;
  margin-top: 14px;
  padding: 34px;
  border-radius: 24px;
  border: 1px solid rgba(255,255,255,.07);
  background: rgba(255,255,255,.025);
}

.cgu-12__numeral {
  font-size: clamp(90px,14vw,168px);
  font-weight: 900;
  letter-spacing: -.05em;
  line-height: 1;
  color: #a5b4fc;
}

@supports (background-clip: text) or (-webkit-background-clip: text) {
  .cgu-12__numeral {
    background: conic-gradient(from 210deg at 50% 40%,#38bdf8,#a78bfa,#f472b6,#fbbf24,#38bdf8);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }
}

.cgu-12__h3 {
  font-size: 21px;
  font-weight: 800;
  margin-bottom: 10px;
}

.cgu-12__body {
  font-size: 15px;
  line-height: 1.7;
  color: #aab0cc;
  text-wrap: pretty;
}

.cgu-12__body strong {
  font-weight: 750;
  color: #e2e8ff;
}

@supports (background-clip: text) or (-webkit-background-clip: text) {
  .cgu-12__body strong {
    background: linear-gradient(100deg,#7dd3fc,#f9a8d4);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }
}

.cgu-12__note {
  margin-top: 12px;
  font-size: 13px;
  color: #7c81a3;
}

@keyframes cgu12-flow {
  to {
    background-position: -250% 0;
  }
}

@media (max-width: 620px) {
  .cgu-12__row {
    grid-template-columns: 1fr;
    text-align: center;
  }

  .cgu-12__note {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cgu-12__flowline {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — background-clip: text throughout, with every transparent color wrapped in @supports so unsupported engines render solid readable text. */
```
