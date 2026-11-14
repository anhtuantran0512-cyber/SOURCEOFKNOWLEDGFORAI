---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/horizontal-scroll/"
title: "Tabbed Era Timeline — Radio-Button Period Switcher, Zero JS"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "A horizontal era bar where clicking a period (or arrowing between them with a keyboard) swaps the detail panel below — powered entirely by hidden radio…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tabbed Era Timeline — Radio-Button Period Switcher, Zero JS
Source: https://codefronts.com/layouts/css-timelines/horizontal-scroll/

A horizontal era bar where clicking a period (or arrowing between them with a keyboard) swaps the detail panel below — powered entirely by hidden radio inputs and :checked sibling selectors. The pattern for 'company history by era', museum exhibits and product generations, with a sliding underline indicator that moves between tabs using only CSS.
## HTML
```html
<section class="tls-22" aria-label="Tabbed era timeline demo">
  <div class="tls-22__widget">
    <input class="tls-22__radio tls-22__r1" type="radio" name="tls-22-era" id="tls-22-e1" checked>
    <input class="tls-22__radio tls-22__r2" type="radio" name="tls-22-era" id="tls-22-e2">
    <input class="tls-22__radio tls-22__r3" type="radio" name="tls-22-era" id="tls-22-e3">
    <div class="tls-22__bar">
      <label class="tls-22__tab tls-22__tab--1" for="tls-22-e1"><b>1994–2003</b><span>The garage years</span></label>
      <label class="tls-22__tab tls-22__tab--2" for="tls-22-e2"><b>2004–2014</b><span>Going global</span></label>
      <label class="tls-22__tab tls-22__tab--3" for="tls-22-e3"><b>2015–2026</b><span>The platform era</span></label>
    </div>
    <div class="tls-22__panels">
      <div class="tls-22__panel tls-22__panel--1">
        <ol class="tls-22__rail" role="list">
          <li class="tls-22__stop"><time datetime="1994">1994</time><p>Founded above a print shop with a single fax machine.</p></li>
          <li class="tls-22__stop"><time datetime="1998">1998</time><p>First website — a price list and a promise to call back.</p></li>
          <li class="tls-22__stop"><time datetime="2003">2003</time><p>Employee #10 hired; the fax machine retires.</p></li>
        </ol>
      </div>
      <div class="tls-22__panel tls-22__panel--2">
        <ol class="tls-22__rail" role="list">
          <li class="tls-22__stop"><time datetime="2006">2006</time><p>First international office opens in Toronto.</p></li>
          <li class="tls-22__stop"><time datetime="2010">2010</time><p>The catalog goes fully online; stores become showrooms.</p></li>
          <li class="tls-22__stop"><time datetime="2014">2014</time><p>One millionth customer, celebrated with terrible cake.</p></li>
        </ol>
      </div>
      <div class="tls-22__panel tls-22__panel--3">
        <ol class="tls-22__rail" role="list">
          <li class="tls-22__stop"><time datetime="2017">2017</time><p>API launched; other companies start building on us.</p></li>
          <li class="tls-22__stop"><time datetime="2022">2022</time><p>Carbon-neutral operations across all facilities.</p></li>
          <li class="tls-22__stop"><time datetime="2026">2026</time><p>Thirty-two years in — and the founder still answers support tickets on Fridays.</p></li>
        </ol>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.tls-22,
.tls-22 *,
.tls-22 *::before,
.tls-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-22 {
  min-height: 100vh;
  width: 100%;
  --tl-accent: #be123c;
  --tl-line: #f1e4e7;
  --tl-ink: #27141a;
  --tl-mut: #8d707a;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #fdf9fa;
  padding: 64px 24px;
  display: grid;
  place-items: center;
}

.tls-22__widget {
  width: min(680px,100%);
}

.tls-22__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.tls-22__bar {
  position: relative;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  border-bottom: 2px solid var(--tl-line);
}

.tls-22__bar::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: calc(100% / 3);
  height: 3px;
  background: var(--tl-accent);
  border-radius: 2px;
  transition: translate .3s cubic-bezier(.5,0,.2,1);
}

.tls-22__r2:checked ~ .tls-22__bar::after {
  translate: 100% 0;
}

.tls-22__r3:checked ~ .tls-22__bar::after {
  translate: 200% 0;
}

.tls-22__tab {
  display: grid;
  gap: 2px;
  text-align: center;
  padding: 14px 10px;
  cursor: pointer;
  transition: opacity .2s;
}

.tls-22__tab b {
  font-size: 15px;
  font-weight: 800;
  color: var(--tl-ink);
  letter-spacing: -.01em;
}

.tls-22__tab span {
  font-size: 11.5px;
  color: var(--tl-mut);
}

.tls-22__tab {
  opacity: .5;
}

.tls-22__tab:hover {
  opacity: .8;
}

.tls-22__r1:checked ~ .tls-22__bar .tls-22__tab--1,
.tls-22__r2:checked ~ .tls-22__bar .tls-22__tab--2,
.tls-22__r3:checked ~ .tls-22__bar .tls-22__tab--3 {
  opacity: 1;
}

.tls-22__r1:focus-visible ~ .tls-22__bar .tls-22__tab--1,
.tls-22__r2:focus-visible ~ .tls-22__bar .tls-22__tab--2,
.tls-22__r3:focus-visible ~ .tls-22__bar .tls-22__tab--3 {
  outline: 2px solid var(--tl-accent);
  outline-offset: -2px;
  border-radius: 6px;
}

.tls-22__panels {
  padding-top: 30px;
}

.tls-22__panel {
  display: none;
}

.tls-22__r1:checked ~ .tls-22__panels .tls-22__panel--1,
.tls-22__r2:checked ~ .tls-22__panels .tls-22__panel--2,
.tls-22__r3:checked ~ .tls-22__panels .tls-22__panel--3 {
  display: block;
}

@media (prefers-reduced-motion: no-preference) {
  .tls-22__r1:checked ~ .tls-22__panels .tls-22__panel--1,
    .tls-22__r2:checked ~ .tls-22__panels .tls-22__panel--2,
    .tls-22__r3:checked ~ .tls-22__panels .tls-22__panel--3 {
    animation: tls-22-in .3s ease;
  }

  @keyframes tls-22-in {
    from {
      opacity: 0;
      transform: translateY(8px);
    }
  }
}

.tls-22__rail {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 18px;
  position: relative;
  padding-top: 22px;
}

.tls-22__rail::before {
  content: '';
  position: absolute;
  top: 5px;
  left: 8%;
  right: 8%;
  height: 2px;
  background: var(--tl-line);
}

.tls-22__stop {
  position: relative;
  text-align: center;
}

.tls-22__stop::before {
  content: '';
  position: absolute;
  top: -22px;
  left: 50%;
  translate: -50% 0;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--tl-accent);
  border: 3px solid #fdf9fa;
}

.tls-22__stop time {
  font-size: 13px;
  font-weight: 800;
  color: var(--tl-accent);
}

.tls-22__stop p {
  font-size: 13px;
  line-height: 1.55;
  color: var(--tl-mut);
  margin-top: 6px;
  text-wrap: pretty;
}

@media (max-width: 560px) {
  .tls-22__rail {
    grid-template-columns: 1fr;
    gap: 14px;
    padding-top: 0;
  }

  .tls-22__rail::before {
    display: none;
  }

  .tls-22__stop {
    text-align: left;
  }

  .tls-22__stop::before {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — three same-name radios drive panels and the sliding underline via :checked ~ sibling selectors; radio groups give correct tab keyboard semantics (one tab stop + arrow keys) natively. */
```
