---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-inline-word-swap-hover-effect/"
title: "CSS Inline Word Swap Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Text elements where hovering swaps out a word or phrase with an alternate, animated via clip-path, translateY, or opacity transitions — six swap styles."
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Inline Word Swap Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-inline-word-swap-hover-effect/

Text elements where hovering swaps out a word or phrase with an alternate, animated via clip-path, translateY, or opacity transitions — six swap styles.
## HTML
```html
<div class="hv-28">
  <p class="hv-28__label">Inline Word Swap — 6 Styles</p>

  <div class="hv-28__row">
    <a class="hv-28__link hv-28__link--slide-up" href="#" aria-label="Design Systems">
      <span class="hv-28__word hv-28__word--out">Design</span>
      <span class="hv-28__word hv-28__word--in" aria-hidden="true">Systems</span>
    </a>
    <span class="hv-28__style">Slide Up</span>
  </div>

  <div class="hv-28__row">
    <a class="hv-28__link hv-28__link--clip" href="#" aria-label="Make it Work">
      <span class="hv-28__word hv-28__word--out">Make it</span>
      <span class="hv-28__word hv-28__word--in" aria-hidden="true">Work</span>
    </a>
    <span class="hv-28__style">Clip Reveal</span>
  </div>

  <div class="hv-28__row">
    <a class="hv-28__link hv-28__link--fade" href="#" aria-label="Start Now">
      <span class="hv-28__word hv-28__word--out">Start</span>
      <span class="hv-28__word hv-28__word--in" aria-hidden="true">Now</span>
    </a>
    <span class="hv-28__style">Fade Cross</span>
  </div>

  <div class="hv-28__row">
    <a class="hv-28__link hv-28__link--scale" href="#" aria-label="Build Fast">
      <span class="hv-28__word hv-28__word--out">Build</span>
      <span class="hv-28__word hv-28__word--in" aria-hidden="true">Fast</span>
    </a>
    <span class="hv-28__style">Scale In</span>
  </div>

  <div class="hv-28__row">
    <a class="hv-28__link hv-28__link--blur" href="#" aria-label="Ship Ship">
      <span class="hv-28__word hv-28__word--out">Ship</span>
      <span class="hv-28__word hv-28__word--in" aria-hidden="true">Ship</span>
    </a>
    <span class="hv-28__style">Blur Swap</span>
  </div>

  <div class="hv-28__row">
    <a class="hv-28__link hv-28__link--rotate" href="#" aria-label="Create Iterate">
      <span class="hv-28__word hv-28__word--out">Create</span>
      <span class="hv-28__word hv-28__word--in" aria-hidden="true">Iterate</span>
    </a>
    <span class="hv-28__style">Flip Down</span>
  </div>
</div>
```
## CSS
```css
.hv-28,
.hv-28 *,
.hv-28 *::before,
.hv-28 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-28 {
  --swap-color: #7c6af7;
  font-family: system-ui, sans-serif;
  background: #0b0b0e;
  padding: 3rem 2rem;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  align-items: flex-start;
  max-width: 600px;
  margin: 0 auto;
}

.hv-28__label {
  color: #444;
  font-size: .72rem;
  letter-spacing: .15em;
  text-transform: uppercase;
  align-self: center;
}

.hv-28__row {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.hv-28__style {
  color: #3a3a50;
  font-size: .68rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  min-width: 90px;
}

.hv-28__link {
  text-decoration: none;
  font-size: 1.6rem;
  font-weight: 700;
  position: relative;
  display: inline-block;
  overflow: hidden;
  min-width: 8ch;
  height: 1.2em;
  line-height: 1.2;
  vertical-align: bottom;
}

.hv-28__word {
  display: block;
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  white-space: nowrap;
  line-height: inherit;
}
/* ── 1. Slide Up ── */

.hv-28__link--slide-up .hv-28__word--out {
  color: #ccc;
  transition: transform .3s cubic-bezier(.4,0,.2,1);
}

.hv-28__link--slide-up .hv-28__word--in {
  color: var(--swap-color);
  transform: translateY(100%);
  transition: transform .3s cubic-bezier(.4,0,.2,1);
}

.hv-28__link--slide-up:hover .hv-28__word--out {
  transform: translateY(-100%);
}

.hv-28__link--slide-up:hover .hv-28__word--in {
  transform: translateY(0);
}
/* ── 2. Clip Reveal ── */

.hv-28__link--clip .hv-28__word--out {
  color: #ccc;
  transition: clip-path .3s cubic-bezier(.4,0,.2,1);
  clip-path: inset(0 0 0 0);
}

.hv-28__link--clip .hv-28__word--in {
  color: var(--swap-color);
  clip-path: inset(0 100% 0 0);
  transition: clip-path .3s cubic-bezier(.4,0,.2,1);
}

.hv-28__link--clip:hover .hv-28__word--out {
  clip-path: inset(0 0 0 100%);
}

.hv-28__link--clip:hover .hv-28__word--in {
  clip-path: inset(0 0 0 0);
}
/* ── 3. Fade Cross ── */

.hv-28__link--fade .hv-28__word--out {
  color: #ccc;
  transition: opacity .25s;
}

.hv-28__link--fade .hv-28__word--in {
  color: var(--swap-color);
  opacity: 0;
  transition: opacity .25s .1s;
}

.hv-28__link--fade:hover .hv-28__word--out {
  opacity: 0;
}

.hv-28__link--fade:hover .hv-28__word--in {
  opacity: 1;
}
/* ── 4. Scale In ── */

.hv-28__link--scale .hv-28__word--out {
  color: #ccc;
  transition: opacity .25s, transform .25s;
}

.hv-28__link--scale .hv-28__word--in {
  color: var(--swap-color);
  opacity: 0;
  transform: scale(.6);
  transition: opacity .3s .05s, transform .3s .05s cubic-bezier(.34,1.56,.64,1);
}

.hv-28__link--scale:hover .hv-28__word--out {
  opacity: 0;
  transform: scale(1.3);
}

.hv-28__link--scale:hover .hv-28__word--in {
  opacity: 1;
  transform: scale(1);
}
/* ── 5. Blur Swap ── */

.hv-28__link--blur .hv-28__word--out {
  color: #ccc;
  transition: filter .3s, opacity .3s;
}

.hv-28__link--blur .hv-28__word--in {
  color: var(--swap-color);
  filter: blur(8px);
  opacity: 0;
  transition: filter .3s .05s, opacity .3s .05s;
}

.hv-28__link--blur:hover .hv-28__word--out {
  filter: blur(8px);
  opacity: 0;
}

.hv-28__link--blur:hover .hv-28__word--in {
  filter: blur(0);
  opacity: 1;
}
/* ── 6. Flip Down ── */

.hv-28__link--rotate {
  perspective: 300px;
}

.hv-28__link--rotate .hv-28__word--out {
  color: #ccc;
  transition: transform .35s cubic-bezier(.4,0,.2,1), opacity .25s;
  transform-origin: bottom;
}

.hv-28__link--rotate .hv-28__word--in {
  color: var(--swap-color);
  transform: rotateX(-90deg);
  transform-origin: top;
  opacity: 0;
  transition: transform .35s cubic-bezier(.4,0,.2,1) .05s, opacity .2s .05s;
}

.hv-28__link--rotate:hover .hv-28__word--out {
  transform: rotateX(90deg);
  opacity: 0;
}

.hv-28__link--rotate:hover .hv-28__word--in {
  transform: rotateX(0);
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .hv-28__word {
    transition: none !important;
  }
}
```
