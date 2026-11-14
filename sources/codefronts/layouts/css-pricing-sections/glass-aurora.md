---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/glass-aurora/"
title: "Glass Aurora"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "Frosted-glass pricing cards floating over a slow-drifting aurora gradient — radial blobs that orbit behind the cards."
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glass Aurora
Source: https://codefronts.com/layouts/css-pricing-sections/glass-aurora/

Frosted-glass pricing cards floating over a slow-drifting aurora gradient — radial blobs that orbit behind the cards. backdrop-filter: blur() over layered conic / radial gradients. Ice-blue palette, the high-end consumer-app pricing treatment.
## HTML
```html
<section class="ps-10" aria-label="Pricing">
  <div class="ps-10__blobs" aria-hidden="true">
    <span class="ps-10__b1"></span>
    <span class="ps-10__b2"></span>
    <span class="ps-10__b3"></span>
  </div>
  <header class="ps-10__head">
    <h2>Pricing, on the house.</h2>
    <p>Three tiers, all built on the same calm interface.</p>
  </header>
  <div class="ps-10__grid">
    <article class="ps-10__card">
      <h3>Drift</h3>
      <div class="ps-10__price"><em>$</em>0<span>free</span></div>
      <ul>
        <li>Personal projects</li>
        <li>1 GB storage</li>
        <li>Community access</li>
      </ul>
      <a class="ps-10__cta" href="#drift">Get started</a>
    </article>
    <article class="ps-10__card ps-10__mid">
      <span class="ps-10__pill">Recommended</span>
      <h3>Float</h3>
      <div class="ps-10__price"><em>$</em>18<span>/mo</span></div>
      <ul>
        <li>Unlimited projects</li>
        <li>30 GB storage</li>
        <li>Priority email support</li>
        <li>Custom domains</li>
      </ul>
      <a class="ps-10__cta ps-10__cta-pri" href="#float">Choose Float</a>
    </article>
    <article class="ps-10__card">
      <h3>Stratos</h3>
      <div class="ps-10__price"><em>$</em>56<span>/mo</span></div>
      <ul>
        <li>Everything in Float</li>
        <li>SSO + audit logs</li>
        <li>Dedicated success manager</li>
      </ul>
      <a class="ps-10__cta" href="#stratos">Talk to sales</a>
    </article>
  </div>
</section>
```
## CSS
```css
.ps-10 {
  position: relative;
  overflow: hidden;
  contain: layout paint;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: #050a1a;
  color: #e6f0ff;
  font-family: 'Inter', system-ui, sans-serif;
}

.ps-10__blobs {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
}

.ps-10__blobs span {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  opacity: 0.7;
  animation: ps-10-drift 22s ease-in-out infinite alternate;
}

.ps-10__b1 {
  top: -10%;
  left: -10%;
  width: 380px;
  height: 380px;
  background: radial-gradient(circle, #38bdf8 0%, transparent 60%);
  animation-delay: -3s;
}

.ps-10__b2 {
  top: 20%;
  right: -8%;
  width: 320px;
  height: 320px;
  background: radial-gradient(circle, #818cf8 0%, transparent 60%);
  animation-delay: -8s;
}

.ps-10__b3 {
  bottom: -15%;
  left: 30%;
  width: 360px;
  height: 360px;
  background: radial-gradient(circle, #22d3ee 0%, transparent 60%);
  animation-delay: -14s;
}

@keyframes ps-10-drift {
  0% {
    transform: translate(0,0) scale(1);
  }

  50% {
    transform: translate(40px,-30px) scale(1.08);
  }

  100% {
    transform: translate(-30px,30px) scale(0.95);
  }
}

.ps-10__head {
  position: relative;
  z-index: 2;
  text-align: center;
  margin-bottom: clamp(28px, 4vw, 44px);
}

.ps-10__head h2 {
  font-size: clamp(24px, 3.6vw, 36px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 8px;
  color: #fff;
}

.ps-10__head p {
  color: #b8c4dc;
  margin: 0;
  font-size: 14px;
}

.ps-10__grid {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
  max-width: 980px;
  margin: 0 auto;
  align-items: center;
}

.ps-10__card {
  position: relative;
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 18px;
  padding: 26px 22px 22px;
  display: flex;
  flex-direction: column;
  backdrop-filter: blur(20px) saturate(140%);
  -webkit-backdrop-filter: blur(20px) saturate(140%);
  box-shadow: 0 18px 48px rgba(0,0,0,0.25);
}

.ps-10__mid {
  background: rgba(255,255,255,0.1);
  border-color: rgba(56,189,248,0.4);
  transform: scale(1.04);
  box-shadow: 0 0 0 1px rgba(56,189,248,0.4) inset, 0 22px 56px rgba(56,189,248,0.18);
}

.ps-10__pill {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(90deg, #38bdf8, #818cf8);
  color: #050a1a;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 5px 12px;
  border-radius: 999px;
}

.ps-10__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin: 0 0 12px;
  color: #93c5fd;
}

.ps-10__price {
  display: flex;
  align-items: baseline;
  gap: 4px;
  font-size: 42px;
  font-weight: 800;
  letter-spacing: -0.03em;
  margin-bottom: 18px;
  color: #fff;
}

.ps-10__price em {
  font-size: 0.5em;
  font-style: normal;
  padding-right: 2px;
  opacity: 0.7;
}

.ps-10__price span {
  font-size: 0.32em;
  font-weight: 500;
  opacity: 0.65;
  margin-left: 6px;
}

.ps-10__card ul {
  list-style: none;
  padding: 0;
  margin: 0 0 22px;
  flex: 1;
  font-size: 13.5px;
  line-height: 1.9;
  color: #d1ddee;
}

.ps-10__card ul li::before {
  content: '◇';
  color: #38bdf8;
  display: inline-block;
  width: 20px;
}

.ps-10__cta {
  display: block;
  text-align: center;
  padding: 11px 16px;
  border-radius: 10px;
  background: rgba(255,255,255,0.08);
  color: #93c5fd;
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 600;
  border: 1px solid rgba(147,197,253,0.3);
  transition: background 0.18s, color 0.18s;
}

.ps-10__cta-pri {
  background: linear-gradient(90deg, #38bdf8, #818cf8);
  color: #050a1a;
  border-color: transparent;
}

.ps-10__cta:hover {
  background: rgba(255,255,255,0.18);
  color: #fff;
}

.ps-10__cta-pri:hover {
  background: linear-gradient(90deg, #7dd3fc, #a5b4fc);
  color: #050a1a;
}

.ps-10__cta:focus-visible {
  outline: 2px solid #38bdf8;
  outline-offset: 3px;
}

@media (max-width: 820px) {
  .ps-10__grid {
    grid-template-columns: 1fr;
    max-width: 380px;
  }

  .ps-10__mid {
    transform: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ps-10__blobs span {
    animation: none;
  }

  .ps-10__cta {
    transition: none;
  }
}
```
