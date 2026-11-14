---
source: "codefronts"
url: "https://codefronts.com/layouts/css-card-grid-layout/css-asymmetric-bento-box-feature-grid/"
title: "CSS Asymmetric Bento Box Feature Grid"
section: "layouts"
category: "css-card-grid-layout"
category_name: "CSS Card Grid Layouts"
description: "An Apple-style bento layout where one hero tile spans two columns and two rows while smaller tiles wrap around it using grid-column and grid-row spans on a…"
has_js: "false"
---

Here's a working CSS Card Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Asymmetric Bento Box Feature Grid
Source: https://codefronts.com/layouts/css-card-grid-layout/css-asymmetric-bento-box-feature-grid/

An Apple-style bento layout where one hero tile spans two columns and two rows while smaller tiles wrap around it using grid-column and grid-row spans on a dark, glow-bordered canvas.
## HTML
```html
<div class="cg-02">
  <div class="cg-02__grid">
    <div class="cg-02__tile cg-02__tile--hero" style="--glow:#7c6af7">
      <div class="cg-02__icon" style="background:#7c6af7"></div>
      <h3>Real-Time Sync Engine</h3>
      <p>Every change propagates across devices in under 80ms with conflict-free merge resolution.</p>
    </div>
    <div class="cg-02__tile" style="--glow:#00d4ff">
      <div class="cg-02__icon" style="background:#00d4ff"></div>
      <h3>Edge Caching</h3>
      <p>Global CDN with smart invalidation.</p>
    </div>
    <div class="cg-02__tile" style="--glow:#ff6b9d">
      <div class="cg-02__icon" style="background:#ff6b9d"></div>
      <h3>Zero-Config Auth</h3>
      <p>Drop-in identity, fully managed.</p>
    </div>
    <div class="cg-02__tile" style="--glow:#ffd166">
      <div class="cg-02__icon" style="background:#ffd166"></div>
      <h3>Usage Insights</h3>
      <p>Live dashboards, no setup.</p>
    </div>
    <div class="cg-02__tile" style="--glow:#34d399">
      <div class="cg-02__icon" style="background:#34d399"></div>
      <h3>Type-Safe SDKs</h3>
      <p>Generated clients for every stack.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.cg-02,
.cg-02 *,
.cg-02 *::before,
.cg-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cg-02 ::selection {
  background: #7c6af7;
  color: #fff;
}

.cg-02 {
  --radius: 20px;
  background: #08070d;
  min-height: 100vh;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  padding: 48px 24px;
  color: #f5f5fa;
}

.cg-02__grid {
  max-width: 1000px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(4,1fr);
  grid-auto-rows: 140px;
  gap: 18px;
}

.cg-02__tile {
  position: relative;
  grid-column: span 2;
  grid-row: span 1;
  border-radius: var(--radius);
  padding: 24px;
  background: linear-gradient(#0f0e18,#0f0e18) padding-box, linear-gradient(135deg, var(--glow), transparent 70%) border-box;
  border: 1px solid transparent;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 8px;
  transition: transform .3s ease, box-shadow .3s ease;
}

.cg-02__tile:hover {
  transform: translateY(-3px);
  box-shadow: 0 0 0 1px var(--glow), 0 20px 40px -20px var(--glow);
}

.cg-02__tile--hero {
  grid-column: span 2;
  grid-row: span 2;
}

.cg-02__tile h3 {
  font-size: 1.05rem;
  font-weight: 700;
  letter-spacing: -.01em;
}

.cg-02__tile--hero h3 {
  font-size: 1.4rem;
}

.cg-02__tile p {
  font-size: .82rem;
  color: rgba(245,245,250,.55);
  line-height: 1.45;
  margin-top: 2px;
}

.cg-02__icon {
  width: 34px;
  height: 34px;
  border-radius: 9px;
  margin-bottom: 4px;
  opacity: .9;
}

@media (max-width: 640px) {
  .cg-02__grid {
    grid-template-columns: repeat(2,1fr);
  }

  .cg-02__tile {
    grid-column: span 1;
  }

  .cg-02__tile--hero {
    grid-column: span 2;
    grid-row: span 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cg-02__tile {
    transition: none;
  }

  .cg-02__tile:hover {
    transform: none;
  }
}
```
