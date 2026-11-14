---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/centered-classic/"
title: "Centered Classic"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "The artisanal SaaS hero — eyebrow, serif headline, prose subhead, a single deep-terracotta primary CTA flanked by a quiet ghost button."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Centered Classic
Source: https://codefronts.com/layouts/css-hero-sections/centered-classic/

The artisanal SaaS hero — eyebrow, serif headline, prose subhead, a single deep-terracotta primary CTA flanked by a quiet ghost button. Sage on warm cream, the small-batch tools-for-makers aesthetic.
## HTML
```html
<section class="hs-01" aria-label="Hero">
  <div class="hs-01__inner">
    <span class="hs-01__eye">— A new kind of workspace</span>
    <h2>Make small things <em>that matter.</em></h2>
    <p>
      The toolkit for craftspeople who treat the work, the customer, and the calendar with the same
      care.
    </p>
    <div class="hs-01__cta">
      <a class="hs-01__btn hs-01__btn-pri" href="#start">Start free trial →</a>
      <a class="hs-01__btn" href="#tour">Watch the tour</a>
    </div>
    <p class="hs-01__foot">Free for 14 days · no card · cancel any time</p>
  </div>
</section>
```
## CSS
```css
.hs-01 {
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: clamp(32px, 6vw, 80px) clamp(20px, 5vw, 56px);
  background: radial-gradient(60% 80% at 50% 0%, rgba(200,160,120,0.18), transparent 70%), #f5f1e6;
  font-family: 'Cormorant Garamond', 'Georgia', serif;
  color: #2d3a2e;
  box-sizing: border-box;
}

.hs-01__inner {
  max-width: 640px;
  text-align: center;
}

.hs-01__eye {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  letter-spacing: 0.18em;
  color: #6b7d5a;
  margin-bottom: 18px;
}

.hs-01 h2 {
  margin: 0 0 18px;
  font-size: clamp(36px, 6vw, 60px);
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1.05;
  color: #1a2418;
}

.hs-01 h2 em {
  color: #c8553d;
  font-style: italic;
}

.hs-01 p {
  margin: 0 auto 28px;
  font-family: 'Inter', system-ui, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #4a5447;
  max-width: 460px;
}

.hs-01__cta {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 18px;
}

.hs-01__btn {
  display: inline-block;
  padding: 13px 22px;
  border-radius: 4px;
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.01em;
  text-decoration: none;
  transition: transform 0.18s, background 0.18s;
}

.hs-01__btn-pri {
  background: #c8553d;
  color: #fff8ed;
  box-shadow: 0 2px 0 #8d3a25;
}

.hs-01__btn-pri:hover {
  transform: translateY(-1px);
  background: #b94a32;
}

.hs-01__btn {
  background: transparent;
  color: #2d3a2e;
  border: 1px solid #2d3a2e;
}

.hs-01__btn:hover {
  background: #2d3a2e;
  color: #f5f1e6;
}

.hs-01__foot {
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 11px !important;
  color: #8a9080 !important;
  margin: 0 !important;
  max-width: none !important;
  letter-spacing: 0.04em;
}

@media (prefers-reduced-motion: reduce) {
  .hs-01__btn {
    transition: none;
  }
}
```
