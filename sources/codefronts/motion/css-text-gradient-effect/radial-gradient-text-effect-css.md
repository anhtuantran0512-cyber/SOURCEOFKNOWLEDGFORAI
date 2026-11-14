---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/radial-gradient-text-effect-css/"
title: "Radial Gradient Text Effect CSS"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "Four radial-gradient text examples where the brightest colour radiates from the centre of each character, fading toward the edges."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Radial Gradient Text Effect CSS
Source: https://codefronts.com/motion/css-text-gradient-effect/radial-gradient-text-effect-css/

Four radial-gradient text examples where the brightest colour radiates from the centre of each character, fading toward the edges.
## HTML
```html
<div class="tg-14">
  <div class="tg-14__wrapper">
    <h1 class="tg-14__big tg-14__radial-a">Radiate</h1>
    <h2 class="tg-14__med tg-14__radial-b">Energy outward</h2>
    <div class="tg-14__card-row">
      <div class="tg-14__card">
        <h3 class="tg-14__card-h tg-14__radial-c">Expand</h3>
        <p>Radial gradients grow from a central point, making text feel like it emanates light.</p>
      </div>
      <div class="tg-14__card">
        <h3 class="tg-14__card-h tg-14__radial-d">Focus</h3>
        <p>A darker perimeter naturally draws the eye to the bright centre of the letterforms.</p>
      </div>
    </div>
    <p class="tg-14__code-hint"><code>radial-gradient(circle at 50% 50%, …)</code></p>
  </div>
</div>
```
## CSS
```css
.tg-14,
.tg-14 *,
.tg-14 *::before,
.tg-14 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-14 ::selection {
  background: #7c3aed44;
  color: #fff;
}

.tg-14 {
  --center-a: #fde68a;
  --edge-a: #f59e0b;
  --center-b: #c4b5fd;
  --edge-b: #7c3aed;
  --center-c: #7dd3fc;
  --edge-c: #1d4ed8;
  --center-d: #fbcfe8;
  --edge-d: #be185d;
  --bg: #09080f;
  --surface: rgba(255,255,255,.04);
  --text: #e2e8f0;
  --muted: #64748b;
  --border: rgba(255,255,255,.07);
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 44px 24px;
}

.tg-14__wrapper {
  max-width: 620px;
  width: 100%;
  text-align: center;
}
/*
  Radial gradient text: circle at 50% 50% places the brightest colour at
  the exact centre of the element's bounding box. As the gradient clips
  to the text, the middle of each character glows and edges fade.
  Adjust the first stop percentage to control the glow spread.
*/

.tg-14__radial-a {
  background: radial-gradient(circle at 50% 50%, var(--center-a) 0%, var(--edge-a) 65%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.tg-14__radial-b {
  background: radial-gradient(ellipse at 40% 60%, var(--center-b) 0%, var(--edge-b) 75%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.tg-14__radial-c {
  background: radial-gradient(circle at 50% 40%, var(--center-c) 0%, var(--edge-c) 80%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.tg-14__radial-d {
  background: radial-gradient(circle at 50% 40%, var(--center-d) 0%, var(--edge-d) 80%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.tg-14__big {
  font-size: clamp(4rem, 12vw, 7rem);
  font-weight: 900;
  letter-spacing: -.05em;
  line-height: 1;
  margin-bottom: 8px;
}

.tg-14__med {
  font-size: clamp(1.5rem, 5vw, 2.75rem);
  font-weight: 700;
  letter-spacing: -.03em;
  margin-bottom: 32px;
}

.tg-14__card-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin-bottom: 24px;
  text-align: left;
}

.tg-14__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px;
}

.tg-14__card-h {
  font-size: 1.4rem;
  font-weight: 800;
  margin-bottom: 8px;
}

.tg-14__card p {
  font-size: .825rem;
  color: var(--muted);
  line-height: 1.6;
}

.tg-14__code-hint {
  font-size: .8rem;
  color: var(--muted);
}

.tg-14__code-hint code {
  background: rgba(255,255,255,.06);
  padding: 3px 8px;
  border-radius: 4px;
  font-size: .78rem;
  color: #c4b5fd;
}

@media (prefers-reduced-motion: reduce) {
}
```
