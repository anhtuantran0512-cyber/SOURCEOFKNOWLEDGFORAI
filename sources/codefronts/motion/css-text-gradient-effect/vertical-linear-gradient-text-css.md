---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/vertical-linear-gradient-text-css/"
title: "Vertical Linear Gradient Text CSS"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "A split-layout demo contrasting horizontal and vertical gradient directions, including writing-mode: vertical-rl sidebar labels."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Linear Gradient Text CSS
Source: https://codefronts.com/motion/css-text-gradient-effect/vertical-linear-gradient-text-css/

A split-layout demo contrasting horizontal and vertical gradient directions, including writing-mode: vertical-rl sidebar labels.
## HTML
```html
<div class="tg-13">
  <div class="tg-13__layout">
    <aside class="tg-13__sidebar">
      <h2 class="tg-13__section-word tg-13__v1">Build</h2>
      <h2 class="tg-13__section-word tg-13__v2">Ship</h2>
      <h2 class="tg-13__section-word tg-13__v3">Grow</h2>
    </aside>
    <main class="tg-13__body">
      <p class="tg-13__kicker">VERTICAL GRADIENT TEXT</p>
      <p class="tg-13__explain">A top-to-bottom <code>linear-gradient</code> fades from a vivid top colour to a lighter or contrasting shade at the bottom, reinforcing visual hierarchy — brighter at the top catches the eye, the fade draws it downward.</p>
      <div class="tg-13__demo-block">
        <h1 class="tg-13__hero-word tg-13__fade-down">Framework</h1>
        <h1 class="tg-13__hero-word tg-13__fade-up">Platform</h1>
      </div>
    </main>
  </div>
</div>
```
## CSS
```css
.tg-13,
.tg-13 *,
.tg-13 *::before,
.tg-13 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-13 ::selection {
  background: #1d4ed8;
  color: #e0f2fe;
}

.tg-13 {
  --top-a: #1d4ed8;
  --bot-a: #60a5fa;
  --top-b: #9333ea;
  --bot-b: #f472b6;
  --top-c: #0284c7;
  --bot-c: #38bdf8;
  --top-h: #f59e0b;
  --bot-h: rgba(245,158,11,.2);
  --top-p: #7c3aed;
  --bot-p: rgba(124,58,237,.25);
  --bg: #f1f5f9;
  --surface: #ffffff;
  --text: #0f172a;
  --muted: #64748b;
  --border: #e2e8f0;
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
}

.tg-13__layout {
  display: flex;
  min-height: 100vh;
}

.tg-13__sidebar {
  background: #0f172a;
  width: 100px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 4px;
  padding: 24px 0;
}
/* Vertical gradients on sidebar words */

.tg-13__section-word {
  font-size: 1.25rem;
  font-weight: 900;
  letter-spacing: .08em;
  writing-mode: vertical-rl;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}
/* background-image (not shorthand) — shorthand resets background-clip
   to border-box and the text clipping above silently fails. */

.tg-13__v1 {
  background-image: linear-gradient(180deg, var(--top-a), var(--bot-a));
}

.tg-13__v2 {
  background-image: linear-gradient(180deg, var(--top-b), var(--bot-b));
}

.tg-13__v3 {
  background-image: linear-gradient(180deg, var(--top-c), var(--bot-c));
}

.tg-13__body {
  padding: 36px 32px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex: 1;
}

.tg-13__kicker {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .14em;
  color: var(--muted);
  margin-bottom: 14px;
}

.tg-13__explain {
  font-size: .875rem;
  color: var(--muted);
  line-height: 1.7;
  max-width: 440px;
  margin-bottom: 28px;
}

.tg-13__explain code {
  background: var(--border);
  border-radius: 3px;
  padding: 1px 5px;
  font-size: .8em;
  color: var(--top-b);
}

.tg-13__demo-block {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}
/*
  Vertical (top→bottom) gradients: use `to bottom` direction.
  The lighter/transparent end at the bottom simulates a gentle fade-out.
*/

.tg-13__hero-word {
  font-size: clamp(2.5rem, 7vw, 4rem);
  font-weight: 900;
  letter-spacing: -.04em;
  line-height: 1;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  /* inline-block + padding ensure the gradient clips to the glyph
       shape (block-level <h1> with background-image would otherwise
       paint the gradient on the full row width even when text content
       is narrow). */
  display: inline-block;
  padding: 0 .05em .1em;
}

.tg-13__fade-down {
  background-image: linear-gradient(to bottom, var(--top-h) 0%, var(--bot-h) 100%);
}

.tg-13__fade-up {
  background-image: linear-gradient(to top, var(--top-p) 0%, var(--bot-p) 100%);
}

@media (prefers-reduced-motion: reduce) {
}
```
