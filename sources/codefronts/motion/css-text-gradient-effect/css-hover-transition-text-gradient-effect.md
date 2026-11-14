---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/css-hover-transition-text-gradient-effect/"
title: "CSS Hover Transition Text Gradient Effect"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "A navigation and card component that transitions solid text into a gradient on hover using -webkit-text-fill-color transition."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Hover Transition Text Gradient Effect
Source: https://codefronts.com/motion/css-text-gradient-effect/css-hover-transition-text-gradient-effect/

A navigation and card component that transitions solid text into a gradient on hover using -webkit-text-fill-color transition.
## HTML
```html
<div class="tg-05">
  <div class="tg-05__card">
    <p class="tg-05__hint">Hover over any link</p>
    <nav class="tg-05__nav">
      <a href="#" class="tg-05__link">Home</a>
      <a href="#" class="tg-05__link">Features</a>
      <a href="#" class="tg-05__link">Pricing</a>
      <a href="#" class="tg-05__link">Blog</a>
      <a href="#" class="tg-05__link">Contact</a>
    </nav>
    <div class="tg-05__divider"></div>
    <div class="tg-05__cards">
      <div class="tg-05__tile">
        <h3 class="tg-05__tile-h">Analytics <span class="tg-05__arrow">→</span></h3>
        <p>Real-time dashboards for every metric your team cares about.</p>
      </div>
      <div class="tg-05__tile">
        <h3 class="tg-05__tile-h">Integrations <span class="tg-05__arrow">→</span></h3>
        <p>Connect to 200+ tools with one-click OAuth flows.</p>
      </div>
      <div class="tg-05__tile">
        <h3 class="tg-05__tile-h">Collaboration <span class="tg-05__arrow">→</span></h3>
        <p>Shared workspaces with granular permission controls.</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.tg-05,
.tg-05 *,
.tg-05 *::before,
.tg-05 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-05 ::selection {
  background: #7c3aed;
  color: #fff;
}

.tg-05 {
  --g-a: #7c3aed;
  --g-b: #ec4899;
  --bg: #0f0f14;
  --surface: #17171f;
  --text: #e2e8f0;
  --muted: #64748b;
  --solid: #94a3b8;
  --border: rgba(255,255,255,.07);
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
}

.tg-05__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 36px 32px;
  width: 100%;
  max-width: 580px;
}

.tg-05__hint {
  font-size: .75rem;
  font-weight: 600;
  letter-spacing: .1em;
  color: var(--muted);
  margin-bottom: 20px;
}

.tg-05__nav {
  display: flex;
  gap: 4px;
  flex-wrap: wrap;
  margin-bottom: 28px;
}
/* 
  Hover gradient technique:
  Gradient sits on ::before; opacity transitions from 0→1.
  -webkit-text-fill-color can't transition, so we use a pseudo-element
  trick: normal color fades out, gradient fades in via opacity on ::before.
  We achieve the gradient-on-hover by toggling background-clip on the element itself.
*/

.tg-05__link {
  position: relative;
  text-decoration: none;
  font-size: .95rem;
  font-weight: 600;
  padding: 8px 18px;
  border-radius: 8px;
  color: var(--solid);
  transition: color .3s;
  display: inline-block;
}

.tg-05__link::before {
  content: attr(data-hover, '');
  position: absolute;
  inset: 0;
  padding: 8px 18px;
  background: linear-gradient(90deg, var(--g-a), var(--g-b));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  opacity: 0;
  transition: opacity .3s;
  pointer-events: none;
}

.tg-05__link::after {
  content: attr(href, '');
  position: absolute;
  inset: 8px 18px;
  background: linear-gradient(90deg, var(--g-a), var(--g-b));
  -webkit-background-clip: text;
  background-clip: text;
  opacity: 0;
  transition: opacity .3s;
}
/* Simpler approach: fade out the solid text colour, overlay gradient clone */

.tg-05__link span {
  /* We'll use a direct CSS trick on the element */
}

.tg-05__link:hover {
  background: linear-gradient(90deg, var(--g-a), var(--g-b));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}
/* Smooth fade: CSS can't tween background-clip text, so we fade background colour instead */

.tg-05__link {
  background: linear-gradient(90deg, var(--g-a), var(--g-b));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: var(--solid);
  transition: -webkit-text-fill-color .25s;
}

.tg-05__link:hover {
  -webkit-text-fill-color: transparent;
}

.tg-05__divider {
  height: 1px;
  background: var(--border);
  margin-bottom: 28px;
}

.tg-05__cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 14px;
}

.tg-05__tile {
  background: rgba(255,255,255,.03);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 18px;
}

.tg-05__tile p {
  font-size: .8rem;
  color: var(--muted);
  line-height: 1.55;
  margin-top: 6px;
}

.tg-05__tile-h {
  font-size: .9375rem;
  font-weight: 700;
  color: var(--text);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.tg-05__arrow {
  color: var(--muted);
  font-weight: 400;
}

.tg-05__tile:hover .tg-05__tile-h {
  background: linear-gradient(90deg, var(--g-a), var(--g-b));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

@media (prefers-reduced-motion: reduce) {
  .tg-05__link,
    .tg-05__tile {
    transition: none;
  }
}
```
