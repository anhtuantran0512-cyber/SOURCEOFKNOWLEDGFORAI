---
source: "codefronts"
url: "https://codefronts.com/layouts/css-card-grid-layout/css-team-directory-face-grid/"
title: "CSS Team Directory Face Grid"
section: "layouts"
category: "css-card-grid-layout"
category_name: "CSS Card Grid Layouts"
description: "A centered profile-card directory where each circular avatar breaks the top edge of its card using a negative margin pulled over a card with extra top…"
has_js: "false"
---

Here's a working CSS Card Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Team Directory Face Grid
Source: https://codefronts.com/layouts/css-card-grid-layout/css-team-directory-face-grid/

A centered profile-card directory where each circular avatar breaks the top edge of its card using a negative margin pulled over a card with extra top padding to make room.
## HTML
```html
<div class="cg-05">
  <div class="cg-05__grid">
    <article class="cg-05__card">
      <div class="cg-05__avatar" style="background:linear-gradient(135deg,#fbbf24,#f97316)"></div>
      <h3 class="cg-05__name">Dana Whitfield</h3>
      <p class="cg-05__role">Head of Product Design</p>
      <div class="cg-05__social"><span>in</span><span>tw</span><span>gh</span></div>
    </article>
    <article class="cg-05__card">
      <div class="cg-05__avatar" style="background:linear-gradient(135deg,#34d399,#0ea5e9)"></div>
      <h3 class="cg-05__name">Idris Bello</h3>
      <p class="cg-05__role">Staff Engineer</p>
      <div class="cg-05__social"><span>in</span><span>tw</span><span>gh</span></div>
    </article>
    <article class="cg-05__card">
      <div class="cg-05__avatar" style="background:linear-gradient(135deg,#f472b6,#a855f7)"></div>
      <h3 class="cg-05__name">Lena Ferraro</h3>
      <p class="cg-05__role">VP of Customer Success</p>
      <div class="cg-05__social"><span>in</span><span>tw</span><span>gh</span></div>
    </article>
  </div>
</div>
```
## CSS
```css
.cg-05,
.cg-05 *,
.cg-05 *::before,
.cg-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cg-05 ::selection {
  background: #a855f7;
  color: #fff;
}

.cg-05 {
  --muted: #6b7280;
  background: #f3f1ee;
  min-height: 100vh;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  padding: 64px 24px 48px;
}

.cg-05__grid {
  max-width: 880px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(200px,1fr));
  gap: 24px;
  row-gap: 56px;
}

.cg-05__card {
  position: relative;
  background: #fff;
  border: 1px solid #e7e4dd;
  border-radius: 16px;
  padding: 56px 20px 24px;
  text-align: center;
  transition: box-shadow .25s ease, transform .25s ease;
}

.cg-05__card:hover {
  transform: translateY(-3px);
  box-shadow: 0 16px 32px -20px rgba(31,41,55,.25);
}

.cg-05__avatar {
  width: 84px;
  height: 84px;
  border-radius: 50%;
  margin: -50px auto 12px;
  border: 4px solid #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,.12);
}

.cg-05__name {
  font-size: 1rem;
  font-weight: 700;
  color: #1f2937;
}

.cg-05__role {
  font-size: .82rem;
  color: var(--muted);
  margin-top: 4px;
}

.cg-05__social {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 16px;
}

.cg-05__social span {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f3f1ee;
  color: #374151;
  font-size: .68rem;
  font-weight: 700;
  text-transform: uppercase;
  transition: background .2s ease, color .2s ease;
}

.cg-05__social span:hover {
  background: #1f2937;
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .cg-05__card,
    .cg-05__social span {
    transition: none;
  }

  .cg-05__card:hover {
    transform: none;
  }
}
```
