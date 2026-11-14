---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/css-text-gradient-with-text-stroke-outline/"
title: "CSS Text Gradient with Text Stroke Outline"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "Combines -webkit-text-stroke with background-clip gradient fill, demonstrating stroke-only, fill-only, and stroke-plus-fill patterns side by side."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Gradient with Text Stroke Outline
Source: https://codefronts.com/motion/css-text-gradient-effect/css-text-gradient-with-text-stroke-outline/

Combines -webkit-text-stroke with background-clip gradient fill, demonstrating stroke-only, fill-only, and stroke-plus-fill patterns side by side.
## HTML
```html
<div class="tg-16">
  <div class="tg-16__wrapper">
    <p class="tg-16__label">COMBINING STROKE + GRADIENT FILL</p>
    <h1 class="tg-16__outlined">OUTLINE</h1>
    <h2 class="tg-16__stroked">Gradient Fill + Stroke</h2>
    <div class="tg-16__grid">
      <div class="tg-16__example">
        <span class="tg-16__ex-lbl">Stroke only</span>
        <span class="tg-16__stroke-only">Type</span>
      </div>
      <div class="tg-16__example">
        <span class="tg-16__ex-lbl">Fill only</span>
        <span class="tg-16__fill-only">Type</span>
      </div>
      <div class="tg-16__example">
        <span class="tg-16__ex-lbl">Stroke + Fill</span>
        <span class="tg-16__both">Type</span>
      </div>
    </div>
    <p class="tg-16__note">Apply <code>-webkit-text-stroke</code> first, then layer gradient via <code>background-clip: text</code>. The stroke paints on top of the clipped gradient fill.</p>
  </div>
</div>
```
## CSS
```css
.tg-16,
.tg-16 *,
.tg-16 *::before,
.tg-16 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-16 ::selection {
  background: #0f172a;
  color: #e0f2fe;
}

.tg-16 {
  --g-a: #38bdf8;
  --g-b: #818cf8;
  --g-c: #e879f9;
  --bg: #030609;
  --text: #f1f5f9;
  --muted: #475569;
  --border: rgba(255,255,255,.07);
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 44px 24px;
}

.tg-16__wrapper {
  max-width: 640px;
  width: 100%;
}

.tg-16__label {
  font-size: .65rem;
  font-weight: 700;
  letter-spacing: .16em;
  color: var(--muted);
  margin-bottom: 16px;
}
/*
  Outlined text: -webkit-text-stroke sets a stroke colour/width,
  and -webkit-text-fill-color: transparent makes the fill invisible,
  leaving only the outline. We can layer a gradient behind via background-clip
  to colour the visible stroke area.
*/

.tg-16__outlined {
  font-size: clamp(3.5rem, 12vw, 6.5rem);
  font-weight: 900;
  letter-spacing: .04em;
  line-height: 1;
  -webkit-text-stroke: 2px transparent;
  /* Use background + clip to colour the stroke itself */
  background: linear-gradient(90deg, var(--g-a), var(--g-b), var(--g-c));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  /* Add stroke on top via paint-order if supported */
  paint-order: stroke fill;
  -webkit-text-stroke: 2px rgba(56,189,248,.6);
  margin-bottom: 8px;
  display: block;
}
/*
  Fill + stroke combined: gradient fill is applied through background-clip,
  then -webkit-text-stroke paints over it. Use a semi-transparent or
  complementary stroke colour to preserve the gradient beneath.
*/

.tg-16__stroked {
  font-size: clamp(1.6rem, 5vw, 2.8rem);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.1;
  background: linear-gradient(90deg, var(--g-a) 0%, var(--g-b) 50%, var(--g-c) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  -webkit-text-stroke: 1px rgba(232,121,249,.45);
  display: block;
  margin-bottom: 32px;
}

.tg-16__grid {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  margin-bottom: 28px;
}

.tg-16__example {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.tg-16__ex-lbl {
  font-size: .7rem;
  color: var(--muted);
  letter-spacing: .06em;
}

.tg-16__stroke-only {
  font-size: 3rem;
  font-weight: 900;
  -webkit-text-stroke: 2px var(--g-a);
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.tg-16__fill-only {
  font-size: 3rem;
  font-weight: 900;
  background: linear-gradient(90deg, var(--g-b), var(--g-c));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.tg-16__both {
  font-size: 3rem;
  font-weight: 900;
  background: linear-gradient(90deg, var(--g-a), var(--g-b), var(--g-c));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  -webkit-text-stroke: 1.5px rgba(255,255,255,.35);
}

.tg-16__note {
  font-size: .8rem;
  color: var(--muted);
  line-height: 1.65;
}

.tg-16__note code {
  background: rgba(255,255,255,.07);
  border-radius: 3px;
  padding: 1px 5px;
  color: var(--g-a);
  font-size: .78em;
}

@media (prefers-reduced-motion: reduce) {
}
```
