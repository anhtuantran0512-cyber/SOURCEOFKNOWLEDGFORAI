---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/gradient-text-button-link-css/"
title: "Gradient Text Button Link CSS"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "Three button patterns — ghost with gradient label, gradient border via mask, and filled gradient — demonstrating every CTA gradient variant."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Text Button Link CSS
Source: https://codefronts.com/motion/css-text-gradient-effect/gradient-text-button-link-css/

Three button patterns — ghost with gradient label, gradient border via mask, and filled gradient — demonstrating every CTA gradient variant.
## HTML
```html
<div class="tg-06">
  <div class="tg-06__panel">
    <h2 class="tg-06__heading">Ready to launch?</h2>
    <p class="tg-06__sub">Pick the interaction pattern that fits your design system.</p>
    <div class="tg-06__grid">
      <div class="tg-06__col">
        <p class="tg-06__tag">Ghost with gradient label</p>
        <a href="#" class="tg-06__btn tg-06__btn--ghost">
          <span class="tg-06__label">Get started free</span>
        </a>
        <a href="#" class="tg-06__btn tg-06__btn--ghost">
          <span class="tg-06__label">View documentation →</span>
        </a>
      </div>
      <div class="tg-06__col">
        <p class="tg-06__tag">Solid gradient border</p>
        <a href="#" class="tg-06__btn tg-06__btn--border">
          <span class="tg-06__label">Start building</span>
        </a>
        <a href="#" class="tg-06__btn tg-06__btn--border">
          <span class="tg-06__label">Talk to sales</span>
        </a>
      </div>
      <div class="tg-06__col">
        <p class="tg-06__tag">Filled gradient</p>
        <a href="#" class="tg-06__btn tg-06__btn--filled">Upgrade to Pro</a>
        <a href="#" class="tg-06__btn tg-06__btn--filled tg-06__btn--sm">Learn more</a>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.tg-06,
.tg-06 *,
.tg-06 *::before,
.tg-06 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-06 ::selection {
  background: #7c3aed;
  color: #fff;
}

.tg-06 {
  --g-a: #f59e0b;
  --g-b: #ef4444;
  --g-c: #ec4899;
  --bg: #0c0c10;
  --surface: #15151d;
  --text: #f1f5f9;
  --muted: #64748b;
  --border: rgba(255,255,255,.09);
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.tg-06__panel {
  max-width: 640px;
  width: 100%;
}

.tg-06__heading {
  font-size: clamp(1.6rem, 4vw, 2.5rem);
  font-weight: 800;
  color: var(--text);
  letter-spacing: -.03em;
  margin-bottom: 10px;
}

.tg-06__sub {
  color: var(--muted);
  font-size: .9375rem;
  margin-bottom: 36px;
}

.tg-06__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 28px;
}

.tg-06__col {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.tg-06__tag {
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .09em;
  color: var(--muted);
  margin-bottom: 4px;
}
/* Base button */

.tg-06__btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  font-size: .9rem;
  font-weight: 700;
  padding: 11px 22px;
  border-radius: 9px;
  transition: transform .2s, box-shadow .2s, opacity .2s;
  cursor: pointer;
}

.tg-06__btn:hover {
  transform: translateY(-2px);
}
/* Ghost: transparent bg, gradient text label */

.tg-06__btn--ghost {
  background: transparent;
  border: 1.5px solid var(--border);
  color: var(--text);
}

.tg-06__btn--ghost .tg-06__label {
  background: linear-gradient(90deg, var(--g-a), var(--g-c));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.tg-06__btn--ghost:hover {
  border-color: rgba(239,68,68,.4);
}
/* Border gradient: pseudo-element creates gradient border, inner bg clips it */

.tg-06__btn--border {
  position: relative;
  background: var(--surface);
  border: none;
  padding: 12px 23px;
  /* +1 for pseudo border */
  isolation: isolate;
}

.tg-06__btn--border::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1.5px;
  background: linear-gradient(90deg, var(--g-a), var(--g-c));
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: destination-out;
  mask-composite: exclude;
  pointer-events: none;
}

.tg-06__btn--border .tg-06__label {
  background: linear-gradient(90deg, var(--g-a), var(--g-c));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}
/* Filled */

.tg-06__btn--filled {
  background: linear-gradient(90deg, var(--g-a), var(--g-b), var(--g-c));
  color: #fff;
}

.tg-06__btn--filled:hover {
  box-shadow: 0 8px 24px rgba(239,68,68,.35);
  opacity: .9;
}

.tg-06__btn--sm {
  font-size: .8rem;
  padding: 8px 18px;
}

@media (prefers-reduced-motion: reduce) {
  .tg-06__btn {
    transition: none;
  }
}
```
