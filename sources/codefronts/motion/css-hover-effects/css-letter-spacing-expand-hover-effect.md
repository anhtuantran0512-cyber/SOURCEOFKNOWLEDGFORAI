---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-letter-spacing-expand-hover-effect/"
title: "CSS Letter Spacing Expand Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Five typographic hover states that animate letter-spacing from tight to airy — standard expand, collapse-in, stagger fade-out, per-letter scale, and tracking…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Letter Spacing Expand Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-letter-spacing-expand-hover-effect/

Five typographic hover states that animate letter-spacing from tight to airy — standard expand, collapse-in, stagger fade-out, per-letter scale, and tracking shift with fade — demonstrating how spacing transitions alone can carry expressive weight.
## HTML
```html
<div class="hv-03">
  <div class="hv-03__stack">
    <div class="hv-03__row">
      <span class="hv-03__word hv-03__word--expand">EXPAND</span>
      <span class="hv-03__tag">letter-spacing expand</span>
    </div>
    <div class="hv-03__row">
      <span class="hv-03__word hv-03__word--collapse">COLLAPSE</span>
      <span class="hv-03__tag">tracking collapse-in</span>
    </div>
    <div class="hv-03__row">
      <span class="hv-03__word hv-03__word--fade">
        <span>D</span><span>R</span><span>I</span><span>F</span><span>T</span>
      </span>
      <span class="hv-03__tag">stagger fade-out</span>
    </div>
    <div class="hv-03__row">
      <span class="hv-03__word hv-03__word--bold">BOLD TRACK</span>
      <span class="hv-03__tag">weight + spacing</span>
    </div>
    <div class="hv-03__row">
      <span class="hv-03__word hv-03__word--glow">RADIANCE</span>
      <span class="hv-03__tag">spacing + glow</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-03,
.hv-03 *,
.hv-03 *::before,
.hv-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-03 ::selection {
  background: #7c3aed;
  color: #fff;
}

.hv-03 {
  --bg: #0d0d14;
  --text: #ede9fe;
  --dim: #6b7280;
  --purple: #a78bfa;
  --pink: #f472b6;
  --cyan: #67e8f9;
  --amber: #fbbf24;
  --white: #fff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-03__stack {
  display: flex;
  flex-direction: column;
  gap: 16px;
  width: min(700px,100%);
}

.hv-03__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 28px 36px;
  background: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 12px;
  gap: 20px;
  overflow: hidden;
}

.hv-03__tag {
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--dim);
  white-space: nowrap;
  flex-shrink: 0;
}
/* shared word base */

.hv-03__word {
  font-size: clamp(1.4rem,4vw,2rem);
  font-weight: 700;
  cursor: default;
  display: inline-block;
  transition: letter-spacing .4s cubic-bezier(.4,0,.2,1),color .4s,opacity .4s;
}
/* 1 — standard expand */

.hv-03__word--expand {
  color: var(--purple);
  letter-spacing: .02em;
}

.hv-03__word--expand:hover {
  letter-spacing: .35em;
  color: var(--text);
}
/* 2 — collapse-in */

.hv-03__word--collapse {
  color: var(--pink);
  letter-spacing: .4em;
}

.hv-03__word--collapse:hover {
  letter-spacing: .02em;
  color: var(--white);
}
/* 3 — stagger via nth-child span */

.hv-03__word--fade {
  display: inline-flex;
  gap: 0;
  font-size: clamp(1.4rem,4vw,2rem);
  font-weight: 700;
  color: var(--cyan);
  letter-spacing: .02em;
}

.hv-03__word--fade span {
  display: inline-block;
  transition: letter-spacing .4s cubic-bezier(.4,0,.2,1),opacity .4s;
}

.hv-03__word--fade:hover span {
  letter-spacing: .2em;
  opacity: .3;
}

.hv-03__word--fade span:nth-child(1) {
  transition-delay: .00s;
}

.hv-03__word--fade span:nth-child(2) {
  transition-delay: .04s;
}

.hv-03__word--fade span:nth-child(3) {
  transition-delay: .08s;
}

.hv-03__word--fade span:nth-child(4) {
  transition-delay: .12s;
}

.hv-03__word--fade span:nth-child(5) {
  transition-delay: .16s;
}
/* 4 — bold + tracking */

.hv-03__word--bold {
  color: var(--amber);
  letter-spacing: .02em;
  font-weight: 400;
  transition: letter-spacing .35s,font-weight .35s,color .35s;
}

.hv-03__word--bold:hover {
  letter-spacing: .25em;
  font-weight: 900;
  color: var(--white);
}
/* 5 — spacing + glow */

.hv-03__word--glow {
  color: var(--text);
  letter-spacing: .06em;
  transition: letter-spacing .5s cubic-bezier(.4,0,.2,1),text-shadow .5s,color .5s;
}

.hv-03__word--glow:hover {
  letter-spacing: .3em;
  color: #fff;
  text-shadow: 0 0 20px var(--purple),0 0 60px var(--pink);
}

@media (max-width: 520px) {
  .hv-03__row {
    flex-direction: column;
    align-items: flex-start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-03__word,
    .hv-03__word--fade span {
    transition: none!important;
  }
}
```
