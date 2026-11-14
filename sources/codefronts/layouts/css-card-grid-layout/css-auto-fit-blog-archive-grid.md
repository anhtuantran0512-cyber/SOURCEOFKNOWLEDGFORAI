---
source: "codefronts"
url: "https://codefronts.com/layouts/css-card-grid-layout/css-auto-fit-blog-archive-grid/"
title: "CSS Auto-Fit Blog Archive Grid"
section: "layouts"
category: "css-card-grid-layout"
category_name: "CSS Card Grid Layouts"
description: "A self-adjusting editorial archive that adds or drops columns purely via grid-template-columns: repeat(auto-fit, minmax(...)) — no media queries required."
has_js: "false"
---

Here's a working CSS Card Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Auto-Fit Blog Archive Grid
Source: https://codefronts.com/layouts/css-card-grid-layout/css-auto-fit-blog-archive-grid/

A self-adjusting editorial archive that adds or drops columns purely via grid-template-columns: repeat(auto-fit, minmax(...)) — no media queries required.
## HTML
```html
<div class="cg-01">
  <div class="cg-01__header">
    <span class="cg-01__kicker">Latest Articles</span>
    <h2 class="cg-01__title">The Auto-Fit Archive</h2>
  </div>
  <div class="cg-01__grid">
    <article class="cg-01__card">
      <div class="cg-01__media">
        <span class="cg-01__badge">Engineering</span>
        <div class="cg-01__img" style="background:linear-gradient(135deg,#3b82f6,#1e3a8a)"></div>
      </div>
      <div class="cg-01__body">
        <h3 class="cg-01__headline">Designing Resilient Grid Systems for the Modern Web</h3>
        <p class="cg-01__excerpt">How auto-fit and minmax remove the need for breakpoint-driven column math.</p>
        <div class="cg-01__meta"><span>Maya Chen</span><span>•</span><span>6 min read</span></div>
      </div>
    </article>
    <article class="cg-01__card">
      <div class="cg-01__media">
        <span class="cg-01__badge">Design</span>
        <div class="cg-01__img" style="background:linear-gradient(135deg,#f472b6,#7c3aed)"></div>
      </div>
      <div class="cg-01__body">
        <h3 class="cg-01__headline">Typography Scales That Don't Break on Mobile</h3>
        <p class="cg-01__excerpt">A practical look at clamp(), fluid type, and readable line lengths.</p>
        <div class="cg-01__meta"><span>Sam Osei</span><span>•</span><span>4 min read</span></div>
      </div>
    </article>
    <article class="cg-01__card">
      <div class="cg-01__media">
        <span class="cg-01__badge">Product</span>
        <div class="cg-01__img" style="background:linear-gradient(135deg,#34d399,#065f46)"></div>
      </div>
      <div class="cg-01__body">
        <h3 class="cg-01__headline">Shipping Faster With Component-Driven Layouts</h3>
        <p class="cg-01__excerpt">Lessons from rebuilding a design system around composable grid primitives.</p>
        <div class="cg-01__meta"><span>Priya Nair</span><span>•</span><span>8 min read</span></div>
      </div>
    </article>
  </div>
</div>
```
## CSS
```css
.cg-01,
.cg-01 *,
.cg-01 *::before,
.cg-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cg-01 ::selection {
  background: #3b82f6;
  color: #fff;
}

.cg-01 {
  --bg: #fafafa;
  --card: #ffffff;
  --ink: #0f172a;
  --muted: #64748b;
  --line: #e2e8f0;
  --accent: #3b82f6;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 48px 24px;
  color: var(--ink);
}

.cg-01__header {
  max-width: 1100px;
  margin: 0 auto 32px;
}

.cg-01__kicker {
  font-size: .75rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--accent);
  font-weight: 700;
}

.cg-01__title {
  font-size: clamp(1.5rem,3vw,2.25rem);
  font-weight: 800;
  margin-top: 6px;
  letter-spacing: -.02em;
}

.cg-01__grid {
  max-width: 1100px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(280px,1fr));
  gap: 28px;
}

.cg-01__card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 14px;
  overflow: hidden;
  transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
}

.cg-01__card:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 32px -16px rgba(15,23,42,.18);
  border-color: transparent;
}

.cg-01__media {
  position: relative;
  aspect-ratio: 16/9;
  overflow: hidden;
}

.cg-01__img {
  width: 100%;
  height: 100%;
  transition: transform .5s ease;
}

.cg-01__card:hover .cg-01__img {
  transform: scale(1.06);
}

.cg-01__badge {
  position: absolute;
  top: 14px;
  left: 14px;
  z-index: 2;
  background: rgba(255,255,255,.92);
  color: var(--ink);
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .04em;
  padding: 5px 10px;
  border-radius: 999px;
}

.cg-01__body {
  padding: 18px 20px 20px;
}

.cg-01__headline {
  font-size: 1.05rem;
  font-weight: 700;
  line-height: 1.35;
  letter-spacing: -.01em;
  overflow-wrap: break-word;
}

.cg-01__excerpt {
  font-size: .875rem;
  color: var(--muted);
  margin-top: 8px;
  line-height: 1.5;
}

.cg-01__meta {
  display: flex;
  gap: 8px;
  margin-top: 14px;
  font-size: .78rem;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .cg-01__card,
    .cg-01__img {
    transition: none;
  }

  .cg-01__card:hover {
    transform: none;
  }
}
```
