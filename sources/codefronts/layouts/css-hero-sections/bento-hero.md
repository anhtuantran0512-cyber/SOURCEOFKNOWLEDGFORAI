---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/bento-hero/"
title: "Bento Hero"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Apple-style bento hero — one large headline tile with stat / quote / pill cells fanning around it. Matte-ceramic palette: salmon, terracotta, ivory, olive."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bento Hero
Source: https://codefronts.com/layouts/css-hero-sections/bento-hero/

Apple-style bento hero — one large headline tile with stat / quote / pill cells fanning around it. Matte-ceramic palette: salmon, terracotta, ivory, olive.
## HTML
```html
<section class="hs-19" aria-label="Hero">
  <article class="hs-19__hero">
    <span class="hs-19__eye">V2 — out now</span>
    <h2>The pottery <em>workbook</em> for serious hands.</h2>
    <a class="hs-19__cta" href="#start">Start the kiln →</a>
  </article>
  <article class="hs-19__stat">
    <strong>1,400</strong>
    <span>hand-thrown<br />pieces logged</span>
  </article>
  <article class="hs-19__quote">
    <p>“Replaced three notebooks and a chalkboard.”</p>
    <cite>— Mireya, Studio Verde</cite>
  </article>
  <article class="hs-19__pill"><span>★ 4.9</span><em>App Store</em></article>
  <article class="hs-19__cta-tile">
    <a href="#android">Android →</a>
  </article>
</section>
```
## CSS
```css
.hs-19 {
  display: grid;
  grid-template-columns: 1.4fr 0.8fr 0.8fr;
  grid-template-rows: auto auto;
  grid-template-areas: "hero hero stat" "hero hero quote" "pill cta  quote";
  gap: 14px;
  width: 100%;
  min-height: 100vh;
  padding: clamp(20px, 3vw, 32px);
  background: #f5ebde;
  font-family: 'Inter', system-ui, sans-serif;
  color: #2c1f15;
  box-sizing: border-box;
}

.hs-19 > article {
  border-radius: 16px;
  padding: clamp(18px, 2.5vw, 26px);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 10px;
}

.hs-19__hero {
  grid-area: hero;
  background: linear-gradient(160deg, #f4a48b, #d97766);
  color: #2c1f15;
}

.hs-19__eye {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.16em;
  background: #2c1f15;
  color: #f5ebde;
  padding: 4px 10px;
  border-radius: 999px;
  align-self: flex-start;
}

.hs-19__hero h2 {
  margin: 0;
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-size: clamp(28px, 4.5vw, 48px);
  font-weight: 600;
  letter-spacing: -0.015em;
  line-height: 1.05;
}

.hs-19__hero h2 em {
  color: #6b1f12;
  font-style: italic;
}

.hs-19__cta {
  align-self: flex-start;
  padding: 11px 20px;
  background: #2c1f15;
  color: #f5ebde;
  border-radius: 999px;
  text-decoration: none;
  font-weight: 600;
  font-size: 14px;
  transition: background 0.18s;
}

.hs-19__cta:hover {
  background: #6b1f12;
}

.hs-19__stat {
  grid-area: stat;
  background: #6b8a3e;
  color: #f5ebde;
}

.hs-19__stat strong {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(40px, 5vw, 64px);
  font-weight: 700;
  line-height: 1;
}

.hs-19__stat span {
  font-size: 13px;
  line-height: 1.35;
  opacity: 0.9;
}

.hs-19__quote {
  grid-area: quote;
  background: #2c1f15;
  color: #f5ebde;
}

.hs-19__quote p {
  font-family: 'Cormorant Garamond', serif;
  font-style: italic;
  font-size: 17px;
  margin: 0;
  line-height: 1.4;
}

.hs-19__quote cite {
  font-size: 11px;
  font-style: normal;
  letter-spacing: 0.06em;
  opacity: 0.7;
}

.hs-19__pill {
  grid-area: pill;
  background: #f5ebde;
  border: 2px solid #2c1f15;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}

.hs-19__pill span {
  font-weight: 800;
  font-size: 18px;
  color: #c69e3d;
}

.hs-19__pill em {
  font-style: normal;
  font-size: 11px;
  opacity: 0.7;
  letter-spacing: 0.06em;
}

.hs-19__cta-tile {
  grid-area: cta;
  background: #d97766;
  padding: 0 !important;
  align-items: stretch;
  justify-content: stretch;
}

.hs-19__cta-tile a {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  color: #2c1f15;
  text-decoration: none;
  font-weight: 700;
  font-size: 14.5px;
}

.hs-19__cta-tile a:hover {
  background: rgba(0,0,0,0.08);
}

@media (max-width: 720px) {
  .hs-19 {
    grid-template-columns: 1fr 1fr;
    grid-template-areas: "hero hero" "stat quote" "pill cta";
  }
}

@media (prefers-reduced-motion: reduce) {
  .hs-19__cta,
    .hs-19__cta-tile a {
    transition: none;
  }
}
```
