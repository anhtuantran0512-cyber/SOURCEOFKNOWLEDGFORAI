---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/3d-tilt-cards/"
title: "3D Tilt Cards"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "Three pricing cards in 3D perspective, tilting back when not hovered and snapping forward on hover."
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Tilt Cards
Source: https://codefronts.com/layouts/css-pricing-sections/3d-tilt-cards/

Three pricing cards in 3D perspective, tilting back when not hovered and snapping forward on hover. Purple → cyan gradient surface, layered shadow stack giving real depth. perspective() + rotateY(), no JS.
## HTML
```html
<section class="ps-14" aria-label="Pricing">
  <header class="ps-14__head">
    <h2>Pricing with depth.</h2>
    <p>Hover to bring a plan forward.</p>
  </header>
  <div class="ps-14__stage">
    <article class="ps-14__card ps-14__l">
      <h3>Lite</h3>
      <div class="ps-14__price"><em>$</em>9<span>/mo</span></div>
      <ul>
        <li>Personal projects</li>
        <li>5 GB storage</li>
        <li>Community support</li>
      </ul>
      <a class="ps-14__cta" href="#lite">Pick Lite</a>
    </article>
    <article class="ps-14__card ps-14__c">
      <span class="ps-14__pill">Best fit</span>
      <h3>Plus</h3>
      <div class="ps-14__price"><em>$</em>29<span>/mo</span></div>
      <ul>
        <li>Unlimited projects</li>
        <li>50 GB storage</li>
        <li>Priority support</li>
        <li>Custom domains</li>
      </ul>
      <a class="ps-14__cta ps-14__cta-pri" href="#plus">Pick Plus</a>
    </article>
    <article class="ps-14__card ps-14__r">
      <h3>Power</h3>
      <div class="ps-14__price"><em>$</em>79<span>/mo</span></div>
      <ul>
        <li>Everything in Plus</li>
        <li>SSO + audit logs</li>
        <li>Dedicated CSM</li>
      </ul>
      <a class="ps-14__cta" href="#power">Pick Power</a>
    </article>
  </div>
</section>
```
## CSS
```css
.ps-14 {
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: radial-gradient(60% 60% at 50% 0%, rgba(124,58,237,0.18), transparent 60%), radial-gradient(60% 60% at 50% 100%, rgba(34,211,238,0.14), transparent 60%), #0d0a1a;
  color: #e9e6ff;
  font-family: 'Inter', system-ui, sans-serif;
  perspective: 1400px;
}

.ps-14__head {
  text-align: center;
  margin-bottom: clamp(24px, 4vw, 40px);
}

.ps-14__head h2 {
  font-size: clamp(24px, 3.6vw, 36px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 8px;
  color: #fff;
}

.ps-14__head p {
  color: #a8a0c8;
  margin: 0;
  font-size: 14px;
}

.ps-14__stage {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
  max-width: 980px;
  margin: 0 auto;
  transform-style: preserve-3d;
  align-items: center;
}

.ps-14__card {
  position: relative;
  background: linear-gradient(160deg, rgba(124,58,237,0.18), rgba(34,211,238,0.10));
  border: 1px solid rgba(167,139,250,0.25);
  border-radius: 16px;
  padding: 26px 22px 22px;
  display: flex;
  flex-direction: column;
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  transform-origin: center;
  transition: transform 0.4s cubic-bezier(.22,1,.36,1), box-shadow 0.4s;
  box-shadow: 0 10px 30px rgba(13,10,26,0.5);
}

.ps-14__l {
  transform: rotateY(14deg) translateZ(-30px);
}

.ps-14__c {
  transform: translateZ(0);
  z-index: 2;
}

.ps-14__r {
  transform: rotateY(-14deg) translateZ(-30px);
}

.ps-14__card:hover {
  transform: rotateY(0) translateZ(20px) translateY(-4px);
  box-shadow: 0 24px 60px rgba(124,58,237,0.4);
  z-index: 3;
}

.ps-14__c {
  background: linear-gradient(160deg, rgba(124,58,237,0.32), rgba(34,211,238,0.18));
  border-color: rgba(34,211,238,0.45);
}

.ps-14__pill {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(135deg, #a78bfa, #22d3ee);
  color: #0d0a1a;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 5px 12px;
  border-radius: 999px;
}

.ps-14__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin: 0 0 12px;
  color: #c4b5fd;
}

.ps-14__c h3 {
  color: #67e8f9;
}

.ps-14__price {
  display: flex;
  align-items: baseline;
  gap: 4px;
  font-size: 38px;
  font-weight: 800;
  letter-spacing: -0.03em;
  margin-bottom: 18px;
  color: #fff;
}

.ps-14__price em {
  font-size: 0.5em;
  font-style: normal;
  padding-right: 2px;
  opacity: 0.7;
}

.ps-14__price span {
  font-size: 0.32em;
  font-weight: 500;
  opacity: 0.65;
  margin-left: 6px;
}

.ps-14__card ul {
  list-style: none;
  padding: 0;
  margin: 0 0 22px;
  flex: 1;
  font-size: 13px;
  line-height: 1.95;
  color: #c4bde0;
}

.ps-14__card ul li::before {
  content: '◆';
  color: #a78bfa;
  display: inline-block;
  width: 20px;
  font-size: 9px;
}

.ps-14__c ul li::before {
  color: #22d3ee;
}

.ps-14__cta {
  display: block;
  text-align: center;
  padding: 11px 16px;
  border-radius: 9px;
  background: rgba(167,139,250,0.12);
  color: #c4b5fd;
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 600;
  border: 1px solid rgba(167,139,250,0.3);
  transition: background 0.18s, color 0.18s;
}

.ps-14__cta-pri {
  background: linear-gradient(135deg, #a78bfa, #22d3ee);
  color: #0d0a1a;
  border-color: transparent;
}

.ps-14__cta:hover {
  background: rgba(167,139,250,0.28);
  color: #fff;
}

.ps-14__cta:focus-visible {
  outline: 2px solid #22d3ee;
  outline-offset: 3px;
}

@media (max-width: 820px) {
  .ps-14__stage {
    grid-template-columns: 1fr;
    max-width: 380px;
    perspective: none;
  }

  .ps-14__l,
    .ps-14__c,
    .ps-14__r {
    transform: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ps-14__card {
    transition: none;
  }

  .ps-14__l,
    .ps-14__c,
    .ps-14__r {
    transform: none;
  }

  .ps-14__card:hover {
    transform: none;
  }
}
```
