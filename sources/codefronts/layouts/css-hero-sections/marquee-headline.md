---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/marquee-headline/"
title: "Marquee Headline"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "A single phrase scrolls horizontally on a loop with a counter-direction line beneath."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Marquee Headline
Source: https://codefronts.com/layouts/css-hero-sections/marquee-headline/

A single phrase scrolls horizontally on a loop with a counter-direction line beneath. Hot tangerine on chocolate brown — the streetwear / drop-culture treatment.
## HTML
```html
<section class="hs-14" aria-label="Hero">
  <div class="hs-14__track hs-14__r" aria-hidden="true">
    <span
      >EVERYTHING SELLS OUT · EVERYTHING SELLS OUT · EVERYTHING SELLS OUT · EVERYTHING SELLS OUT ·
    </span>
    <span
      >EVERYTHING SELLS OUT · EVERYTHING SELLS OUT · EVERYTHING SELLS OUT · EVERYTHING SELLS OUT ·
    </span>
  </div>
  <div class="hs-14__inner">
    <h2>Drop 04. <em>Tuesday 11am EST.</em></h2>
    <p>72 pieces. No restock. No back-orders. No DM begging.</p>
    <a class="hs-14__cta" href="#join">Set the alarm</a>
  </div>
  <div class="hs-14__track hs-14__l" aria-hidden="true">
    <span>NO RESTOCK · NO RESTOCK · NO RESTOCK · NO RESTOCK · NO RESTOCK · NO RESTOCK · </span>
    <span>NO RESTOCK · NO RESTOCK · NO RESTOCK · NO RESTOCK · NO RESTOCK · NO RESTOCK · </span>
  </div>
</section>
```
## CSS
```css
.hs-14 {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 100%;
  min-height: 100vh;
  padding: 0;
  background: #2a1410;
  font-family: 'Inter', system-ui, sans-serif;
  color: #ffe4d6;
  box-sizing: border-box;
  overflow: hidden;
  contain: layout paint;
}

.hs-14__track {
  display: flex;
  gap: 32px;
  white-space: nowrap;
  overflow: hidden;
  width: 100%;
  min-width: 0;
  max-width: 100vw;
  padding: 18px 0;
  font-family: 'Inter', sans-serif;
  font-size: clamp(32px, 5vw, 52px);
  font-weight: 900;
  font-style: italic;
  letter-spacing: -0.01em;
  background: #f04e23;
  color: #2a1410;
  border-block: 4px solid #2a1410;
}

.hs-14__track span {
  animation: hs-14-roll 22s linear infinite;
  flex-shrink: 0;
}

.hs-14__r span {
  animation-direction: normal;
}

.hs-14__l {
  background: #2a1410;
  color: #f04e23;
  border-color: #f04e23;
}

.hs-14__l span {
  animation-direction: reverse;
}

@keyframes hs-14-roll {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(-100%);
  }
}

.hs-14__inner {
  flex: 1;
  display: grid;
  place-items: center;
  padding: clamp(24px, 4vw, 56px);
  text-align: center;
}

.hs-14 h2 {
  margin: 0 0 14px;
  font-size: clamp(32px, 5vw, 52px);
  font-weight: 900;
  letter-spacing: -0.025em;
  line-height: 1.05;
  color: #ffe4d6;
}

.hs-14 h2 em {
  color: #f5b148;
  font-style: italic;
}

.hs-14 p {
  margin: 0 auto 22px;
  font-size: 16px;
  color: #c8a899;
  max-width: 460px;
  line-height: 1.55;
}

.hs-14__cta {
  display: inline-block;
  padding: 13px 28px;
  background: #f5b148;
  color: #2a1410;
  border-radius: 0;
  text-decoration: none;
  font-weight: 800;
  font-size: 14.5px;
  letter-spacing: 0.04em;
  transition: background 0.15s;
}

.hs-14__cta:hover {
  background: #ffe4d6;
}

@media (prefers-reduced-motion: reduce) {
  .hs-14__track span {
    animation: none;
  }

  .hs-14__cta {
    transition: none;
  }
}
```
