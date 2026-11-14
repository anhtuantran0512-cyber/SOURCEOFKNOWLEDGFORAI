---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/asymmetric-type/"
title: "Asymmetric Type"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Construction-site asymmetric typography — broken across columns with intentional misalignment, hi-vis safety yellow on concrete grey, black hard rules."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Asymmetric Type
Source: https://codefronts.com/layouts/css-hero-sections/asymmetric-type/

Construction-site asymmetric typography — broken across columns with intentional misalignment, hi-vis safety yellow on concrete grey, black hard rules.
## HTML
```html
<section class="hs-12" aria-label="Hero">
  <div class="hs-12__grid">
    <span class="hs-12__tag">/ ZONE 4</span>
    <h2 class="hs-12__h">
      <span class="hs-12__l1">UNDER</span>
      <span class="hs-12__l2">construction.</span>
      <span class="hs-12__l3">Always.</span>
    </h2>
    <span class="hs-12__amp">&amp;</span>
    <p class="hs-12__p">
      Software you ship is software that's still being built. We make CI fast enough to do it on the
      dev's terms — not the build's.
    </p>
    <a class="hs-12__cta" href="#start">DEPLOY →</a>
    <span class="hs-12__stripe" aria-hidden="true"></span>
  </div>
</section>
```
## CSS
```css
.hs-12 {
  display: grid;
  place-items: stretch;
  width: 100%;
  min-height: 100vh;
  padding: clamp(24px, 4vw, 48px);
  background: #c8c4be;
  font-family: 'Inter', system-ui, sans-serif;
  color: #0a0a0a;
  box-sizing: border-box;
  overflow: hidden;
}

.hs-12__grid {
  position: relative;
  display: grid;
  grid-template-columns: 1fr 1fr 0.6fr;
  grid-template-rows: auto 1fr auto auto;
  gap: 14px;
  width: 100%;
}

.hs-12__tag {
  grid-column: 1 / 2;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.2em;
  background: #f5d028;
  padding: 4px 10px;
  align-self: start;
  justify-self: start;
}

.hs-12__h {
  grid-column: 1 / 4;
  margin: 0;
  font-family: 'Inter', sans-serif;
  font-weight: 900;
  line-height: 0.85;
  letter-spacing: -0.04em;
  text-transform: uppercase;
}

.hs-12__l1 {
  display: block;
  font-size: clamp(60px, 11vw, 130px);
}

.hs-12__l2 {
  display: block;
  font-size: clamp(40px, 8vw, 90px);
  margin-left: clamp(40px, 12vw, 180px);
  color: #f5d028;
  -webkit-text-stroke: 2px #0a0a0a;
}

.hs-12__l3 {
  display: block;
  font-size: clamp(40px, 8vw, 90px);
  margin-left: clamp(80px, 24vw, 360px);
}

.hs-12__amp {
  grid-column: 3;
  grid-row: 3;
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(80px, 14vw, 160px);
  font-weight: 800;
  font-style: italic;
  color: #0a0a0a;
  line-height: 1;
  align-self: end;
  justify-self: end;
}

.hs-12__p {
  grid-column: 1 / 3;
  grid-row: 3;
  font-size: 14px;
  line-height: 1.55;
  max-width: 380px;
  color: #2a2a2a;
  margin: 0;
  align-self: end;
  border-left: 4px solid #f5d028;
  padding-left: 14px;
}

.hs-12__cta {
  grid-column: 1 / 2;
  grid-row: 4;
  display: inline-block;
  padding: 14px 26px;
  background: #0a0a0a;
  color: #f5d028;
  font-family: 'JetBrains Mono', monospace;
  font-weight: 800;
  font-size: 14px;
  letter-spacing: 0.16em;
  text-decoration: none;
  border: 0;
  align-self: start;
  justify-self: start;
  transition: background 0.15s;
}

.hs-12__cta:hover {
  background: #f5d028;
  color: #0a0a0a;
}

.hs-12__stripe {
  grid-column: 2 / 4;
  grid-row: 4;
  height: 14px;
  align-self: center;
  background: repeating-linear-gradient(45deg, #0a0a0a 0 12px, #f5d028 12px 24px);
}

@media (max-width: 720px) {
  .hs-12__l2,
    .hs-12__l3 {
    margin-left: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hs-12__cta {
    transition: none;
  }
}
```
