---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/minimalist-bold-text-gradient-css/"
title: "Minimalist Bold Text Gradient CSS"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "An editorial type specimen showcasing dual-tone gradients on heavy 900-weight fonts at multiple sizes for maximum impact."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Bold Text Gradient CSS
Source: https://codefronts.com/motion/css-text-gradient-effect/minimalist-bold-text-gradient-css/

An editorial type specimen showcasing dual-tone gradients on heavy 900-weight fonts at multiple sizes for maximum impact.
## HTML
```html
<div class="tg-04">
  <div class="tg-04__inner">
    <p class="tg-04__kicker">TYPE SCALE SPECIMEN</p>
    <h1 class="tg-04__word" data-text="Clarity">Clarity</h1>
    <h2 class="tg-04__word tg-04__word--two" data-text="Purpose">Purpose</h2>
    <h3 class="tg-04__word tg-04__word--three" data-text="Impact">Impact</h3>
    <div class="tg-04__rule"></div>
    <p class="tg-04__caption">Dual-tone linear gradients on heavy weights create editorial impact without imagery. The gradient stop travels left-to-right, producing a colour shift that reads clearly at every size.</p>
  </div>
</div>
```
## CSS
```css
.tg-04,
.tg-04 *,
.tg-04 *::before,
.tg-04 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-04 ::selection {
  background: #1e1b4b;
  color: #e0e7ff;
}

.tg-04 {
  --g-a: #1e1b4b;
  --g-b: #6366f1;
  --g-a2: #312e81;
  --g-b2: #a21caf;
  --g-a3: #0f172a;
  --g-b3: #0ea5e9;
  --bg: #ffffff;
  --muted: #64748b;
  --rule: #e2e8f0;
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 32px;
}

.tg-04__inner {
  max-width: 640px;
  width: 100%;
}

.tg-04__kicker {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .18em;
  color: var(--muted);
  margin-bottom: 16px;
}
/* Shared gradient text mixin pattern. Use inline-block so the
   element's box width equals its glyph width — combined with
   background-clip:text this guarantees the gradient paints inside
   the glyph shape (not as a full-width bar across the block). */

.tg-04__word {
  font-weight: 900;
  line-height: .95;
  letter-spacing: -.04em;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  display: inline-block;
  padding: 0 .05em .1em;
  /* prevents descender clipping in Firefox */
}

.tg-04__inner > .tg-04__word {
  display: block;
}

.tg-04__inner > .tg-04__word + .tg-04__word {
  margin-top: 4px;
}

.tg-04__word {
  font-size: clamp(4rem, 14vw, 7.5rem);
  background-image: linear-gradient(90deg, var(--g-a) 0%, var(--g-b) 100%);
}

.tg-04__word--two {
  font-size: clamp(3rem, 10vw, 5.5rem);
  background-image: linear-gradient(90deg, var(--g-a2) 0%, var(--g-b2) 100%);
}

.tg-04__word--three {
  font-size: clamp(2rem, 7vw, 3.75rem);
  background-image: linear-gradient(90deg, var(--g-a3) 0%, var(--g-b3) 100%);
}

.tg-04__rule {
  height: 1px;
  background: var(--rule);
  margin: 28px 0;
}

.tg-04__caption {
  font-size: .9rem;
  color: var(--muted);
  line-height: 1.7;
  max-width: 520px;
}

@media (prefers-reduced-motion: reduce) {
}
```
