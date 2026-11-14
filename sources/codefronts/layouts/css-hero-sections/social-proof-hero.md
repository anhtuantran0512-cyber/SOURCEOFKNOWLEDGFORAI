---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/social-proof-hero/"
title: "Social Proof Hero"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Mediterranean-tone social-proof hero — star rating pill above the headline, customer logo wall on warm cream, olive serif headlines with aubergine accents."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Social Proof Hero
Source: https://codefronts.com/layouts/css-hero-sections/social-proof-hero/

Mediterranean-tone social-proof hero — star rating pill above the headline, customer logo wall on warm cream, olive serif headlines with aubergine accents.
## HTML
```html
<section class="hs-07" aria-label="Hero">
  <div class="hs-07__inner">
    <span class="hs-07__stars" aria-label="Rated 4.9 out of 5"
      >★★★★★ <em>4.9 from 12,400 reviews</em></span
    >
    <h2>Recipes from <em>real grandmothers,</em> measured for real kitchens.</h2>
    <p>Saved by 500,000 home cooks who never want to scroll past life-stories again.</p>
    <a class="hs-07__cta" href="#start">Open the cookbook</a>
    <ul class="hs-07__logos" aria-label="Featured by">
      <li>NYT</li>
      <li>BON APPÉTIT</li>
      <li>EATER</li>
      <li>GUARDIAN</li>
      <li>SAVEUR</li>
    </ul>
  </div>
</section>
```
## CSS
```css
.hs-07 {
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: clamp(28px, 5vw, 64px) clamp(20px, 5vw, 56px);
  background: radial-gradient(70% 60% at 50% 0%, #f7ecd3, transparent 70%), #faf3e3;
  font-family: 'Inter', system-ui, sans-serif;
  color: #3a2845;
  box-sizing: border-box;
}

.hs-07__inner {
  max-width: 720px;
  text-align: center;
  width: 100%;
}

.hs-07__stars {
  display: inline-block;
  padding: 6px 14px;
  background: #fff;
  border: 1px solid #e2c89a;
  border-radius: 999px;
  color: #c9962b;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.04em;
  margin-bottom: 22px;
}

.hs-07__stars em {
  color: #6b614f;
  font-style: normal;
  font-weight: 500;
  margin-left: 6px;
}

.hs-07 h2 {
  margin: 0 0 16px;
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-size: clamp(32px, 5vw, 52px);
  font-weight: 600;
  letter-spacing: -0.01em;
  line-height: 1.1;
  color: #3a4f2a;
}

.hs-07 h2 em {
  color: #6b1e4a;
  font-style: italic;
}

.hs-07 p {
  margin: 0 auto 28px;
  font-size: 16px;
  line-height: 1.55;
  color: #6b614f;
  max-width: 480px;
}

.hs-07__cta {
  display: inline-block;
  padding: 13px 26px;
  background: #6b1e4a;
  color: #faf3e3;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 700;
  font-size: 14px;
  letter-spacing: 0.04em;
  margin-bottom: 32px;
  transition: background 0.18s;
}

.hs-07__cta:hover {
  background: #4a1232;
}

.hs-07__logos {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: clamp(20px, 4vw, 38px);
  justify-content: center;
  padding-top: 24px;
  border-top: 1px solid #e2c89a;
}

.hs-07__logos li {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: #6b614f;
}

@media (prefers-reduced-motion: reduce) {
  .hs-07__cta {
    transition: none;
  }
}
```
