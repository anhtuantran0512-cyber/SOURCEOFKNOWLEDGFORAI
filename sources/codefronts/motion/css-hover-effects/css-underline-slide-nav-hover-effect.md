---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-underline-slide-nav-hover-effect/"
title: "CSS Underline Slide Nav Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Navigation links where a sliding underline bar glides between items — six distinct sliding and morphing underline styles."
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Underline Slide Nav Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-underline-slide-nav-hover-effect/

Navigation links where a sliding underline bar glides between items — six distinct sliding and morphing underline styles.
## HTML
```html
<div class="hv-25">
  <p class="hv-25__label">Underline Slide Nav — 6 Styles</p>

  <nav class="hv-25__nav hv-25__nav--grow-left">
    <a class="hv-25__link" href="#">Home</a>
    <a class="hv-25__link" href="#">About</a>
    <a class="hv-25__link" href="#">Work</a>
    <a class="hv-25__link" href="#">Contact</a>
    <span class="hv-25__sub">Grow from Left</span>
  </nav>

  <nav class="hv-25__nav hv-25__nav--center">
    <a class="hv-25__link" href="#">Home</a>
    <a class="hv-25__link" href="#">About</a>
    <a class="hv-25__link" href="#">Work</a>
    <a class="hv-25__link" href="#">Contact</a>
    <span class="hv-25__sub">Expand from Centre</span>
  </nav>

  <nav class="hv-25__nav hv-25__nav--overline">
    <a class="hv-25__link" href="#">Home</a>
    <a class="hv-25__link" href="#">About</a>
    <a class="hv-25__link" href="#">Work</a>
    <a class="hv-25__link" href="#">Contact</a>
    <span class="hv-25__sub">Top Overline</span>
  </nav>

  <nav class="hv-25__nav hv-25__nav--double">
    <a class="hv-25__link" href="#">Home</a>
    <a class="hv-25__link" href="#">About</a>
    <a class="hv-25__link" href="#">Work</a>
    <a class="hv-25__link" href="#">Contact</a>
    <span class="hv-25__sub">Double Line</span>
  </nav>

  <nav class="hv-25__nav hv-25__nav--thick">
    <a class="hv-25__link" href="#">Home</a>
    <a class="hv-25__link" href="#">About</a>
    <a class="hv-25__link" href="#">Work</a>
    <a class="hv-25__link" href="#">Contact</a>
    <span class="hv-25__sub">Thick Fill Highlight</span>
  </nav>

  <nav class="hv-25__nav hv-25__nav--dot">
    <a class="hv-25__link" href="#">Home</a>
    <a class="hv-25__link" href="#">About</a>
    <a class="hv-25__link" href="#">Work</a>
    <a class="hv-25__link" href="#">Contact</a>
    <span class="hv-25__sub">Dot Indicator</span>
  </nav>
</div>
```
## CSS
```css
.hv-25,
.hv-25 *,
.hv-25 *::before,
.hv-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-25 {
  --ul-color: #7c6af7;
  --ul-h: 2px;
  font-family: system-ui, sans-serif;
  background: #0b0b0f;
  padding: 3rem 2rem;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 2.8rem;
}

.hv-25__label {
  text-align: center;
  color: #555;
  font-size: .72rem;
  letter-spacing: .15em;
  text-transform: uppercase;
}

.hv-25__nav {
  display: flex;
  align-items: center;
  gap: 2rem;
  flex-wrap: wrap;
  position: relative;
}

.hv-25__sub {
  margin-left: auto;
  color: #444;
  font-size: .68rem;
  letter-spacing: .1em;
  text-transform: uppercase;
}

.hv-25__link {
  color: #ccc;
  text-decoration: none;
  font-size: .95rem;
  font-weight: 500;
  position: relative;
  padding-bottom: 4px;
  transition: color .25s;
}

.hv-25__link:hover {
  color: #fff;
}
/* ── 1. Grow from Left ── */

.hv-25__nav--grow-left .hv-25__link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: var(--ul-h);
  background: var(--ul-color);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .3s cubic-bezier(.4,0,.2,1);
}

.hv-25__nav--grow-left .hv-25__link:hover::after {
  transform: scaleX(1);
}
/* ── 2. Expand from Centre ── */

.hv-25__nav--center .hv-25__link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 100%;
  height: var(--ul-h);
  background: var(--ul-color);
  transform: scaleX(0) translateX(-50%);
  transform-origin: center;
  transition: transform .3s cubic-bezier(.4,0,.2,1);
}

.hv-25__nav--center .hv-25__link:hover::after {
  transform: scaleX(1) translateX(-50%);
}
/* ── 3. Overline ── */

.hv-25__nav--overline .hv-25__link {
  padding-bottom: 0;
  padding-top: 4px;
}

.hv-25__nav--overline .hv-25__link::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: var(--ul-h);
  background: var(--ul-color);
  transform: scaleX(0);
  transform-origin: right;
  transition: transform .3s cubic-bezier(.4,0,.2,1);
}

.hv-25__nav--overline .hv-25__link:hover::before {
  transform: scaleX(1);
  transform-origin: left;
}
/* ── 4. Double Line ── */

.hv-25__nav--double .hv-25__link::before,
.hv-25__nav--double .hv-25__link::after {
  content: '';
  position: absolute;
  left: 0;
  width: 100%;
  height: var(--ul-h);
  background: var(--ul-color);
  transform: scaleX(0);
  transition: transform .35s cubic-bezier(.4,0,.2,1);
}

.hv-25__nav--double .hv-25__link::before {
  top: 0;
  transform-origin: right;
}

.hv-25__nav--double .hv-25__link::after {
  bottom: 0;
  transform-origin: left;
}

.hv-25__nav--double .hv-25__link:hover::before,
.hv-25__nav--double .hv-25__link:hover::after {
  transform: scaleX(1);
}
/* ── 5. Thick Fill Highlight ── */

.hv-25__nav--thick .hv-25__link::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: -6px;
  width: calc(100% + 12px);
  height: 34px;
  background: var(--ul-color);
  border-radius: 4px;
  transform: scaleY(0);
  transform-origin: bottom;
  transition: transform .28s cubic-bezier(.34,1.56,.64,1);
  z-index: -1;
}

.hv-25__nav--thick .hv-25__link:hover::after {
  transform: scaleY(1);
}

.hv-25__nav--thick .hv-25__link {
  z-index: 0;
}
/* ── 6. Dot Indicator ── */

.hv-25__nav--dot .hv-25__link {
  padding-bottom: 8px;
}

.hv-25__nav--dot .hv-25__link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--ul-color);
  transform: translateX(-50%) scale(0);
  transition: transform .25s cubic-bezier(.34,1.56,.64,1);
}

.hv-25__nav--dot .hv-25__link:hover::after {
  transform: translateX(-50%) scale(1);
}

@media (prefers-reduced-motion: reduce) {
  .hv-25__link::before,
    .hv-25__link::after {
    transition: none !important;
  }
}
```
