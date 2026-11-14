---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/css-text-gradient-on-multiline-paragraph/"
title: "CSS Text Gradient on Multiline Paragraph"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "An editorial article demonstrating how background-clip text gradients behave across line-wrapped headings and multiline blockquote elements."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Gradient on Multiline Paragraph
Source: https://codefronts.com/motion/css-text-gradient-effect/css-text-gradient-on-multiline-paragraph/

An editorial article demonstrating how background-clip text gradients behave across line-wrapped headings and multiline blockquote elements.
## HTML
```html
<div class="tg-19">
  <div class="tg-19__article">
    <p class="tg-19__kicker">TECHNIQUE SPOTLIGHT</p>
    <h1 class="tg-19__headline tg-19__grad">Design is not just<br>what it looks like—<br>it's how it works.</h1>
    <p class="tg-19__body">When a gradient is applied to a multiline element, the <code>background-size</code> covers the full bounding box of the element. This means each line samples a different horizontal section of the gradient, creating a natural shift from top to bottom.</p>
    <blockquote class="tg-19__quote tg-19__grad-para">
      The bounding box of a multiline element spans all its lines. A <code>linear-gradient(to right)</code> stretches across the full width of the widest line — narrower lines sample only part of it, which is why short lines at the end appear different in hue.
    </blockquote>
    <p class="tg-19__note">Tip: Use <code>display: block</code> or <code>display: inline-block</code> rather than <code>display: inline</code> to ensure the bounding box wraps all lines uniformly.</p>
  </div>
</div>
```
## CSS
```css
.tg-19,
.tg-19 *,
.tg-19 *::before,
.tg-19 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-19 ::selection {
  background: #4338ca;
  color: #e0e7ff;
}

.tg-19 {
  --g-a: #4338ca;
  --g-b: #7c3aed;
  --g-c: #a21caf;
  --bg: #fafaf9;
  --text: #1c1917;
  --muted: #78716c;
  --border: #e7e5e4;
  font-family: Georgia, 'Times New Roman', serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 0;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

.tg-19__article {
  max-width: 660px;
  width: 100%;
  padding: 44px 28px;
}

.tg-19__kicker {
  font-family: system-ui, sans-serif;
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .14em;
  color: var(--muted);
  margin-bottom: 16px;
}
/*
  Multiline gradient headline: `display: block` is key — it ensures the
  bounding box spans the full container width. The gradient then stretches
  across that box and clips to each character.
*/

.tg-19__grad {
  display: block;
  background: linear-gradient(110deg, var(--g-a) 0%, var(--g-b) 50%, var(--g-c) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.tg-19__headline {
  font-size: clamp(1.8rem, 5vw, 2.75rem);
  font-weight: 700;
  line-height: 1.25;
  letter-spacing: -.02em;
  margin-bottom: 24px;
}

.tg-19__body {
  font-family: system-ui, sans-serif;
  font-size: .9rem;
  color: var(--muted);
  line-height: 1.75;
  margin-bottom: 20px;
}

.tg-19__body code,
.tg-19__note code {
  font-family: monospace;
  font-size: .82em;
  background: #f0eee8;
  border-radius: 3px;
  padding: 1px 5px;
  color: var(--g-b);
}
/* Paragraph-level gradient: works well on body text when used sparingly */

.tg-19__grad-para {
  display: block;
  background: linear-gradient(110deg, var(--g-a) 0%, var(--g-b) 60%, var(--g-c) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.tg-19__quote {
  font-size: 1.05rem;
  line-height: 1.7;
  border-left: 3px solid;
  border-image: linear-gradient(to bottom, var(--g-a), var(--g-c)) 1;
  padding-left: 20px;
  margin: 0 0 20px;
  font-style: italic;
}

.tg-19__quote code {
  font-family: monospace;
  font-size: .82em;
  background: rgba(67,56,202,.08);
  border-radius: 3px;
  padding: 1px 5px;
  -webkit-text-fill-color: var(--g-b);
  font-style: normal;
}

.tg-19__note {
  font-family: system-ui, sans-serif;
  font-size: .8rem;
  color: var(--muted);
  line-height: 1.6;
}

@media (prefers-reduced-motion: reduce) {
}
```
