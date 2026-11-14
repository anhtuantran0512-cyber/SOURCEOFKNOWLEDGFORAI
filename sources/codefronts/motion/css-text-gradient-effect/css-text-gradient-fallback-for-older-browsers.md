---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/css-text-gradient-fallback-for-older-browsers/"
title: "CSS Text Gradient Fallback for Older Browsers"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "A layered fallback reference with three tiers: plain color, @supports-guarded gradient, and the complete pattern for cross-browser safety."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Gradient Fallback for Older Browsers
Source: https://codefronts.com/motion/css-text-gradient-effect/css-text-gradient-fallback-for-older-browsers/

A layered fallback reference with three tiers: plain color, @supports-guarded gradient, and the complete pattern for cross-browser safety.
## HTML
```html
<div class="tg-17">
  <div class="tg-17__doc">
    <h2 class="tg-17__h">Browser Compatibility Strategy</h2>
    <p class="tg-17__intro">A layered fallback ensures gradient text looks great in modern browsers and degrades gracefully in older ones — no JavaScript required.</p>

    <div class="tg-17__layer-list">
      <div class="tg-17__layer">
        <span class="tg-17__badge tg-17__badge--1">Layer 1</span>
        <div>
          <strong>Solid color fallback</strong>
          <p>Set a plain <code>color</code> first. Browsers that don't support <code>background-clip: text</code> will render this.</p>
          <span class="tg-17__demo-text tg-17__solid">Solid Fallback</span>
        </div>
      </div>
      <div class="tg-17__layer">
        <span class="tg-17__badge tg-17__badge--2">Layer 2</span>
        <div>
          <strong>@supports guard</strong>
          <p>Wrap gradient text rules in <code>@supports (-webkit-background-clip: text)</code> to scope them to capable browsers only.</p>
          <span class="tg-17__demo-text tg-17__guarded">Guarded Gradient</span>
        </div>
      </div>
      <div class="tg-17__layer">
        <span class="tg-17__badge tg-17__badge--3">Layer 3</span>
        <div>
          <strong>Result in all engines</strong>
          <p>Modern browsers get the gradient; IE/old Android fall back to the solid <code>color</code> — readable in both cases.</p>
          <span class="tg-17__demo-text tg-17__final">Final Output</span>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.tg-17,
.tg-17 *,
.tg-17 *::before,
.tg-17 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-17 ::selection {
  background: #3b82f6;
  color: #fff;
}

.tg-17 {
  /* Picked endpoints far apart on the spectrum (cobalt → magenta) so
       the gradient transition is obvious — adjacent-hue gradients
       (e.g. blue→violet) read as a flat colour at smaller sizes. */
  --g-a: #2563eb;
  --g-b: #ec4899;
  --bg: #f8fafc;
  --text: #0f172a;
  --muted: #64748b;
  --border: #e2e8f0;
  --surface: #ffffff;
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 44px 28px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

.tg-17__doc {
  max-width: 640px;
  width: 100%;
}

.tg-17__h {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--text);
  letter-spacing: -.02em;
  margin-bottom: 10px;
}

.tg-17__intro {
  color: var(--muted);
  font-size: .9rem;
  line-height: 1.7;
  margin-bottom: 28px;
  max-width: 540px;
}

.tg-17__layer-list {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.tg-17__layer {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px 20px 20px 16px;
  display: flex;
  gap: 16px;
  align-items: flex-start;
}

.tg-17__layer strong {
  display: block;
  font-size: .9375rem;
  color: var(--text);
  margin-bottom: 4px;
}

.tg-17__layer p {
  font-size: .8125rem;
  color: var(--muted);
  line-height: 1.55;
  margin-bottom: 10px;
}

.tg-17__layer code {
  background: #f1f5f9;
  border-radius: 3px;
  padding: 1px 5px;
  font-size: .78em;
  color: var(--g-b);
}

.tg-17__badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: .65rem;
  font-weight: 700;
  letter-spacing: .06em;
  border-radius: 6px;
  padding: 4px 8px;
  flex-shrink: 0;
  margin-top: 2px;
  white-space: nowrap;
}

.tg-17__badge--1 {
  background: #fef9c3;
  color: #854d0e;
}

.tg-17__badge--2 {
  background: #dbeafe;
  color: #1e40af;
}

.tg-17__badge--3 {
  background: #f3e8ff;
  color: #6b21a8;
}
/* Demo text: Layer 1 — solid fallback colour only */

.tg-17__solid {
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--g-a);
  /* Fallback: plain colour */
  display: block;
  letter-spacing: -.02em;
}
/* Layer 2 — @supports guard */

.tg-17__guarded {
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--g-b);
  /* Fallback */
  display: block;
  letter-spacing: -.02em;
}

@supports (-webkit-background-clip: text) or (background-clip: text) {
  .tg-17__guarded {
    /* Use background-image (not the shorthand) so background-clip
           below survives. The shorthand would reset background-clip to
           border-box. */
    background-image: linear-gradient(90deg, var(--g-a), var(--g-b));
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
    display: inline-block;
    padding: 0 .05em .1em;
  }
}
/* Layer 3 — complete pattern with @supports */

.tg-17__final {
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--g-a);
  display: block;
  letter-spacing: -.02em;
}

@supports (-webkit-background-clip: text) or (background-clip: text) {
  .tg-17__final {
    background-image: linear-gradient(90deg, var(--g-a) 0%, var(--g-b) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
    display: inline-block;
    padding: 0 .05em .1em;
  }
}

@media (prefers-reduced-motion: reduce) {
}
```
