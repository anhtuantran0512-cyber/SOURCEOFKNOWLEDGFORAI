---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/price-card-hero/"
title: "Price Card Hero"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Heritage-banking pricing-led hero — copy left, single-tier brass-on-forest pricing card right."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Price Card Hero
Source: https://codefronts.com/layouts/css-hero-sections/price-card-hero/

Heritage-banking pricing-led hero — copy left, single-tier brass-on-forest pricing card right. The 37signals-style "we have one price" treatment with a vintage finance feel.
## HTML
```html
<section class="hs-22" aria-label="Hero">
  <div class="hs-22__copy">
    <span class="hs-22__eye">— Est. 1924 · still independent</span>
    <h2>One ledger. <em>One price.</em> One ridiculously responsive team.</h2>
    <p>
      The bookkeeping software trusted by family-owned businesses since before "SaaS" was a word.
    </p>
  </div>
  <article class="hs-22__card">
    <header>
      <span>The Members' Plan</span>
      <span class="hs-22__badge">No tiers</span>
    </header>
    <div class="hs-22__price"><em>$</em><strong>49</strong><span>/ month, all in</span></div>
    <ul>
      <li>Unlimited invoices</li>
      <li>Multi-entity ledger</li>
      <li>Audit-ready exports</li>
      <li>A real human for support</li>
    </ul>
    <a class="hs-22__cta" href="#join">Become a member</a>
  </article>
</section>
```
## CSS
```css
.hs-22 {
  display: grid;
  grid-template-columns: 1.05fr 1fr;
  width: 100%;
  min-height: 100vh;
  padding: clamp(28px, 5vw, 64px) clamp(20px, 5vw, 56px);
  gap: clamp(28px, 4vw, 64px);
  align-items: center;
  background: #f5ecd8;
  font-family: 'Inter', system-ui, sans-serif;
  color: #1a3322;
  box-sizing: border-box;
}

.hs-22__eye {
  display: block;
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-style: italic;
  font-size: 16px;
  color: #8a7a3a;
  margin-bottom: 14px;
}

.hs-22 h2 {
  margin: 0 0 16px;
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(28px, 4.5vw, 46px);
  font-weight: 700;
  letter-spacing: -0.015em;
  line-height: 1.1;
  color: #1a3322;
}

.hs-22 h2 em {
  color: #8a7a3a;
  font-style: italic;
}

.hs-22 p {
  margin: 0;
  font-size: 15.5px;
  line-height: 1.6;
  color: #4a5a48;
  max-width: 460px;
}

.hs-22__card {
  background: #1a3322;
  color: #f5ecd8;
  padding: clamp(24px, 3vw, 36px);
  border-radius: 0;
  border: 2px solid #8a7a3a;
  box-shadow: inset 0 0 0 4px #1a3322, inset 0 0 0 5px rgba(138,122,58,0.4);
}

.hs-22__card header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  padding-bottom: 16px;
  border-bottom: 1px solid #8a7a3a;
  margin-bottom: 18px;
}

.hs-22__badge {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  letter-spacing: 0.12em;
  padding: 2px 8px;
  border: 1px solid #8a7a3a;
  color: #c0a960;
}

.hs-22__price {
  display: flex;
  align-items: baseline;
  gap: 6px;
  margin-bottom: 22px;
}

.hs-22__price em {
  font-size: 24px;
  font-style: normal;
  color: #8a7a3a;
  font-weight: 700;
}

.hs-22__price strong {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(56px, 6vw, 80px);
  font-weight: 800;
  line-height: 1;
  color: #f5ecd8;
}

.hs-22__price span {
  font-size: 13px;
  color: #c0a960;
}

.hs-22__card ul {
  list-style: none;
  padding: 0;
  margin: 0 0 24px;
  font-size: 14px;
  line-height: 1.95;
  color: #c8d2c4;
}

.hs-22__card ul li::before {
  content: '✓ ';
  color: #c0a960;
  font-weight: 800;
}

.hs-22__cta {
  display: block;
  text-align: center;
  padding: 14px 24px;
  background: #c0a960;
  color: #1a3322;
  text-decoration: none;
  font-weight: 800;
  font-size: 14.5px;
  letter-spacing: 0.04em;
  border: 0;
  transition: background 0.15s;
}

.hs-22__cta:hover {
  background: #f5ecd8;
}

@media (max-width: 720px) {
  .hs-22 {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hs-22__cta {
    transition: none;
  }
}
```
