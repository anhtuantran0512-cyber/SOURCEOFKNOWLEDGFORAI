---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/synthwave-neon/"
title: "Synthwave Neon"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "Retro 80s synthwave pricing — magenta and cyan neon over a perspective grid horizon, chrome heading reflection, sun gradient behind the cards."
has_js: "false"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Synthwave Neon
Source: https://codefronts.com/layouts/css-pricing-sections/synthwave-neon/

Retro 80s synthwave pricing — magenta and cyan neon over a perspective grid horizon, chrome heading reflection, sun gradient behind the cards. The aesthetic Vaporwave / Stranger Things landings ride on.
## HTML
```html
<section class="ps-15" aria-label="Pricing">
  <div class="ps-15__grid-bg" aria-hidden="true"></div>
  <div class="ps-15__sun" aria-hidden="true"></div>
  <header class="ps-15__head">
    <span class="ps-15__eye">★ Pricing ★</span>
    <h2>Choose your <em>signal.</em></h2>
  </header>
  <div class="ps-15__grid">
    <article class="ps-15__card">
      <h3>Wave</h3>
      <div class="ps-15__price">$15</div>
      <ul>
        <li>Solo channel</li>
        <li>5 GB</li>
        <li>Email reach</li>
      </ul>
      <a class="ps-15__cta" href="#wave">Tune in</a>
    </article>
    <article class="ps-15__card ps-15__pri">
      <span class="ps-15__tag">★ FAVORITE ★</span>
      <h3>Pulse</h3>
      <div class="ps-15__price">$39</div>
      <ul>
        <li>Multi-channel</li>
        <li>50 GB</li>
        <li>Live chat</li>
        <li>Custom domain</li>
      </ul>
      <a class="ps-15__cta ps-15__cta-pri" href="#pulse">Tune in</a>
    </article>
    <article class="ps-15__card">
      <h3>Storm</h3>
      <div class="ps-15__price">$99</div>
      <ul>
        <li>Unlimited</li>
        <li>500 GB</li>
        <li>SSO + SLA</li>
      </ul>
      <a class="ps-15__cta" href="#storm">Tune in</a>
    </article>
  </div>
</section>
```
## CSS
```css
.ps-15 {
  position: relative;
  overflow: hidden;
  contain: layout paint;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: linear-gradient(180deg, #0c0420 0%, #1a052e 60%, #2a0843 100%);
  color: #f0e6ff;
  font-family: 'Inter', system-ui, sans-serif;
}

.ps-15__grid-bg {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 220%;
  height: 50%;
  background: repeating-linear-gradient(0deg, transparent 0, transparent 24px, rgba(236,72,153,0.4) 24px, rgba(236,72,153,0.4) 25px), repeating-linear-gradient(90deg, transparent 0, transparent 24px, rgba(34,211,238,0.4) 24px, rgba(34,211,238,0.4) 25px);
  transform: translateX(-50%) perspective(700px) rotateX(60deg);
  transform-origin: center top;
  mask-image: linear-gradient(180deg, transparent 0%, #000 35%);
  -webkit-mask-image: linear-gradient(180deg, transparent 0%, #000 35%);
  z-index: 0;
}

.ps-15__sun {
  position: absolute;
  left: 50%;
  top: 30%;
  transform: translateX(-50%);
  width: 360px;
  height: 360px;
  border-radius: 50%;
  background: repeating-linear-gradient(180deg, transparent 0, transparent 16px, #0c0420 16px, #0c0420 19px), linear-gradient(180deg, #fde68a 0%, #f59e0b 30%, #ec4899 60%, #a855f7 90%);
  filter: blur(0.4px);
  opacity: 0.55;
  z-index: 0;
}

.ps-15__head {
  position: relative;
  z-index: 2;
  text-align: center;
  margin-bottom: clamp(24px, 4vw, 40px);
}

.ps-15__eye {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.4em;
  color: #22d3ee;
  margin-bottom: 14px;
  text-shadow: 0 0 8px #22d3ee;
}

.ps-15__head h2 {
  font-size: clamp(28px, 5vw, 48px);
  font-weight: 800;
  letter-spacing: -0.02em;
  margin: 0;
  background: linear-gradient(180deg, #fff 0%, #fff 50%, #f9a8d4 50%, #ec4899 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  text-shadow: 0 0 30px rgba(236,72,153,0.5);
}

.ps-15__head h2 em {
  font-style: italic;
}

.ps-15__grid {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
  max-width: 940px;
  margin: 0 auto;
  align-items: center;
}

.ps-15__card {
  position: relative;
  background: rgba(12,4,32,0.7);
  border: 1.5px solid #ec4899;
  border-radius: 4px;
  padding: 22px 20px 20px;
  display: flex;
  flex-direction: column;
  box-shadow: 0 0 0 1px rgba(236,72,153,0.4) inset, 0 0 24px rgba(236,72,153,0.3);
  backdrop-filter: blur(6px);
}

.ps-15__pri {
  border-color: #22d3ee;
  box-shadow: 0 0 0 1px rgba(34,211,238,0.5) inset, 0 0 30px rgba(34,211,238,0.5);
}

.ps-15__tag {
  position: absolute;
  top: -11px;
  left: 50%;
  transform: translateX(-50%);
  background: #0c0420;
  color: #22d3ee;
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.18em;
  padding: 3px 12px;
  border: 1px solid #22d3ee;
  text-shadow: 0 0 6px #22d3ee;
}

.ps-15__card h3 {
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  margin: 0 0 12px;
  color: #ec4899;
  text-shadow: 0 0 8px rgba(236,72,153,0.7);
}

.ps-15__pri h3 {
  color: #22d3ee;
  text-shadow: 0 0 8px rgba(34,211,238,0.7);
}

.ps-15__price {
  font-family: 'JetBrains Mono', monospace;
  font-size: 42px;
  font-weight: 800;
  letter-spacing: -0.02em;
  margin-bottom: 18px;
  color: #fff;
  text-shadow: 0 0 12px rgba(236,72,153,0.6);
}

.ps-15__pri .ps-15__price {
  text-shadow: 0 0 12px rgba(34,211,238,0.6);
}

.ps-15__card ul {
  list-style: none;
  padding: 0;
  margin: 0 0 20px;
  flex: 1;
  font-size: 13px;
  line-height: 1.95;
  color: #d6c8ee;
  font-family: 'JetBrains Mono', monospace;
}

.ps-15__card ul li::before {
  content: '▸ ';
  color: #ec4899;
}

.ps-15__pri ul li::before {
  color: #22d3ee;
}

.ps-15__cta {
  display: block;
  text-align: center;
  padding: 10px 14px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  text-decoration: none;
  background: transparent;
  color: #ec4899;
  border: 1.5px solid #ec4899;
  transition: background 0.15s, color 0.15s, box-shadow 0.15s;
}

.ps-15__cta-pri {
  color: #22d3ee;
  border-color: #22d3ee;
}

.ps-15__cta:hover {
  background: #ec4899;
  color: #0c0420;
  box-shadow: 0 0 16px #ec4899;
}

.ps-15__cta-pri:hover {
  background: #22d3ee;
  color: #0c0420;
  box-shadow: 0 0 16px #22d3ee;
}

.ps-15__cta:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 3px;
}

@media (max-width: 820px) {
  .ps-15__grid {
    grid-template-columns: 1fr;
    max-width: 360px;
  }

  .ps-15__sun {
    width: 240px;
    height: 240px;
    top: 22%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ps-15__cta {
    transition: none;
  }
}
```
