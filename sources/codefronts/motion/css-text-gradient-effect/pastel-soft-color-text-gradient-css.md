---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/pastel-soft-color-text-gradient-css/"
title: "Pastel Soft Color Text Gradient CSS"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "A lifestyle blog layout with warm pastel gradients in the 60–90% lightness range across headings and article card titles."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pastel Soft Color Text Gradient CSS
Source: https://codefronts.com/motion/css-text-gradient-effect/pastel-soft-color-text-gradient-css/

A lifestyle blog layout with warm pastel gradients in the 60–90% lightness range across headings and article card titles.
## HTML
```html
<div class="tg-12">
  <div class="tg-12__container">
    <div class="tg-12__blog-header">
      <div class="tg-12__chip">Lifestyle · 4 min</div>
      <h1 class="tg-12__title">The art of<br><span class="tg-12__soft">slow mornings</span></h1>
      <p class="tg-12__intro">Gentle routines and intentional starts that reshape how you work, rest, and create throughout the day.</p>
    </div>
    <div class="tg-12__card-row">
      <article class="tg-12__card">
        <h3 class="tg-12__card-title tg-12__g-rose">Mindful journaling</h3>
        <p>Five minutes of unstructured writing before checking any screen.</p>
      </article>
      <article class="tg-12__card">
        <h3 class="tg-12__card-title tg-12__g-sky">Herbal rituals</h3>
        <p>Brewing tea as a meditative practice — warmth, aroma, presence.</p>
      </article>
      <article class="tg-12__card">
        <h3 class="tg-12__card-title tg-12__g-mint">Gentle movement</h3>
        <p>Ten minutes of stretching outdoors to anchor the body in the day.</p>
      </article>
    </div>
  </div>
</div>
```
## CSS
```css
.tg-12,
.tg-12 *,
.tg-12 *::before,
.tg-12 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-12 ::selection {
  background: #fbcfe8;
  color: #831843;
}

.tg-12 {
  --rose-a: #fda4af;
  --rose-b: #f9a8d4;
  --sky-a: #7dd3fc;
  --sky-b: #a5b4fc;
  --mint-a: #86efac;
  --mint-b: #6ee7b7;
  --bg: #fdf8f6;
  --surface: #ffffff;
  --text: #1e1b1a;
  --muted: #7c6f67;
  --border: #f0e8e4;
  font-family: 'Georgia', serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 0;
}

.tg-12__container {
  padding: 44px 32px;
  max-width: 700px;
  margin: 0 auto;
}

.tg-12__chip {
  font-family: system-ui, sans-serif;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .1em;
  color: var(--muted);
  margin-bottom: 18px;
}

.tg-12__title {
  font-size: clamp(2rem, 5vw, 3.25rem);
  font-weight: 700;
  line-height: 1.15;
  color: var(--text);
  letter-spacing: -.02em;
  margin-bottom: 18px;
}
/*
  Pastel gradients: use soft, desaturated-leaning colours in the 60–90%
  lightness range. The key is to keep both gradient stops within the same 
  warm/cool family so the blend stays harmonious and never muddy.
*/

.tg-12__soft {
  background: linear-gradient(110deg, var(--rose-a) 0%, var(--sky-a) 50%, var(--mint-a) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.tg-12__intro {
  font-size: 1.0625rem;
  color: var(--muted);
  line-height: 1.75;
  max-width: 560px;
  margin-bottom: 36px;
}

.tg-12__card-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(175px, 1fr));
  gap: 16px;
}

.tg-12__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 22px 20px;
}

.tg-12__card p {
  font-family: system-ui, sans-serif;
  font-size: .875rem;
  color: var(--muted);
  line-height: 1.6;
  margin-top: 8px;
}

.tg-12__card-title {
  font-size: 1.1rem;
  font-weight: 700;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  display: inline-block;
  padding: 0 .05em .1em;
}
/* CRITICAL: use background-image (not the shorthand 'background')
   because the shorthand resets background-clip to its initial
   border-box value, breaking the text clipping above. */

.tg-12__g-rose {
  background-image: linear-gradient(90deg, var(--rose-a), var(--rose-b));
}

.tg-12__g-sky {
  background-image: linear-gradient(90deg, var(--sky-a),  var(--sky-b));
}

.tg-12__g-mint {
  background-image: linear-gradient(90deg, var(--mint-a), var(--mint-b));
}

@media (prefers-reduced-motion: reduce) {
}
```
