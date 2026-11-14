---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/spotlight-pricing/"
title: "Spotlight Pricing"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "Cards illuminate where the cursor moves — a CSS variable carries pointer X/Y and a radial gradient renders the spotlight."
has_js: "true"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Spotlight Pricing
Source: https://codefronts.com/layouts/css-pricing-sections/spotlight-pricing/

Cards illuminate where the cursor moves — a CSS variable carries pointer X/Y and a radial gradient renders the spotlight. Black + amber, the developer-tool / OSS-pricing aesthetic. JS only updates two CSS variables; everything else is CSS.
## HTML
```html
<section class="ps-20" aria-label="Pricing">
  <header class="ps-20__head">
    <h2>Move the light. Read the price.</h2>
    <p>Cursor-aware cards. Real cards, real prices, real keyboard support.</p>
  </header>
  <div class="ps-20__grid">
    <article class="ps-20__card" tabindex="0">
      <div class="ps-20__glow" aria-hidden="true"></div>
      <h3>OSS</h3>
      <div class="ps-20__price">$0<span>open source</span></div>
      <ul>
        <li>Self-hosted</li>
        <li>MIT licence</li>
        <li>GitHub issues</li>
      </ul>
      <a class="ps-20__cta" href="#oss">Clone the repo</a>
    </article>
    <article class="ps-20__card ps-20__best" tabindex="0">
      <div class="ps-20__glow" aria-hidden="true"></div>
      <span class="ps-20__pill">Recommended</span>
      <h3>Cloud</h3>
      <div class="ps-20__price">$24<span>/mo</span></div>
      <ul>
        <li>Hosted &amp; maintained</li>
        <li>Auto-updates + backups</li>
        <li>Email support</li>
        <li>API access</li>
      </ul>
      <a class="ps-20__cta ps-20__cta-pri" href="#cloud">Choose Cloud</a>
    </article>
    <article class="ps-20__card" tabindex="0">
      <div class="ps-20__glow" aria-hidden="true"></div>
      <h3>Self-Hosted Pro</h3>
      <div class="ps-20__price">$199<span>/yr</span></div>
      <ul>
        <li>Commercial licence</li>
        <li>Priority email support</li>
        <li>Audit logs</li>
      </ul>
      <a class="ps-20__cta" href="#shp">Buy licence</a>
    </article>
  </div>
</section>
```
## CSS
```css
.ps-20 {
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: #050505;
  color: #f5e6c8;
  font-family: 'JetBrains Mono', 'Inter', system-ui, sans-serif;
}

.ps-20__head {
  text-align: center;
  margin-bottom: clamp(24px, 4vw, 40px);
}

.ps-20__head h2 {
  font-family: 'Inter', sans-serif;
  font-size: clamp(22px, 3.4vw, 32px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 8px;
  color: #fff;
}

.ps-20__head p {
  color: #8a7656;
  margin: 0;
  font-size: 13.5px;
}

.ps-20__grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
  max-width: 980px;
  margin: 0 auto;
  align-items: stretch;
}

.ps-20__card {
  position: relative;
  overflow: hidden;
  background: #0a0a0a;
  border: 1px solid #2a2418;
  border-radius: 14px;
  padding: 24px 22px 20px;
  display: flex;
  flex-direction: column;
  isolation: isolate;
}

.ps-20__glow {
  position: absolute;
  inset: 0;
  background: radial-gradient(180px circle at var(--ps-20__x, 50%) var(--ps-20__y, 50%),
      rgba(245,158,11,0.4) 0%, rgba(245,158,11,0.1) 30%, transparent 60%);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.25s;
  z-index: 0;
}

.ps-20__card:hover .ps-20__glow,
.ps-20__card:focus-within .ps-20__glow {
  opacity: 1;
}

.ps-20__card > *:not(.ps-20__glow) {
  position: relative;
  z-index: 1;
}

.ps-20__card {
  transition: border-color 0.2s, transform 0.2s;
}

.ps-20__card:hover,
.ps-20__card:focus-within {
  border-color: #f59e0b;
  transform: translateY(-2px);
}

.ps-20__card:focus {
  outline: 0;
}

.ps-20__card:focus-visible {
  outline: 2px solid #f59e0b;
  outline-offset: 3px;
}

.ps-20__best {
  border-color: #b45309;
  background: linear-gradient(180deg, #1a0f02, #0a0a0a);
}

.ps-20__pill {
  display: inline-block;
  align-self: flex-start;
  background: #f59e0b;
  color: #050505;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 3px 10px;
  border-radius: 4px;
  margin-bottom: 10px;
}

.ps-20__card h3 {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  margin: 0 0 12px;
  color: #f59e0b;
}

.ps-20__price {
  font-family: 'JetBrains Mono', monospace;
  font-size: 38px;
  font-weight: 800;
  letter-spacing: -0.03em;
  margin-bottom: 18px;
  color: #fff;
  display: flex;
  align-items: baseline;
  gap: 8px;
}

.ps-20__price span {
  font-size: 12px;
  font-weight: 500;
  color: #8a7656;
  letter-spacing: 0.04em;
}

.ps-20__card ul {
  list-style: none;
  padding: 0;
  margin: 0 0 20px;
  flex: 1;
  font-size: 12.5px;
  line-height: 2;
  color: #d8c69a;
}

.ps-20__card ul li::before {
  content: '> ';
  color: #f59e0b;
}

.ps-20__cta {
  display: block;
  text-align: center;
  padding: 10px 16px;
  border-radius: 6px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  text-decoration: none;
  background: transparent;
  color: #f59e0b;
  border: 1.5px solid #b45309;
  transition: background 0.18s, color 0.18s, border-color 0.18s;
}

.ps-20__cta-pri {
  background: #f59e0b;
  color: #050505;
  border-color: #f59e0b;
}

.ps-20__cta:hover {
  background: #f59e0b;
  color: #050505;
  border-color: #f59e0b;
}

.ps-20__cta:focus-visible {
  outline: 2px solid #f59e0b;
  outline-offset: 3px;
}

@media (max-width: 820px) {
  .ps-20__grid {
    grid-template-columns: 1fr;
    max-width: 360px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ps-20__card,
    .ps-20__glow,
    .ps-20__cta {
    transition: none;
  }
}
```

## JavaScript
```js
(function () {
  var cards = document.querySelectorAll('.ps-20__card');
  cards.forEach(function (card) {
    card.addEventListener('pointermove', function (e) {
      var rect = card.getBoundingClientRect();
      var x = ((e.clientX - rect.left) / rect.width) * 100;
      var y = ((e.clientY - rect.top) / rect.height) * 100;
      card.style.setProperty('--ps-20__x', x + '%');
      card.style.setProperty('--ps-20__y', y + '%');
    });
    card.addEventListener('focus', function () {
      card.style.setProperty('--ps-20__x', '50%');
      card.style.setProperty('--ps-20__y', '50%');
    });
  });
})();
```
