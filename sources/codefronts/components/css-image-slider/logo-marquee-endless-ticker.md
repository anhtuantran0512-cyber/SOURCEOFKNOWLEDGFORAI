---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/logo-marquee-endless-ticker/"
title: "Logo Marquee Endless Ticker"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "Logo marquee endless ticker — continuous crawl of client logos for B2B and agency sites, the classic Trusted by strip you see on Stripe, Vercel, Notion,…"
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Logo Marquee Endless Ticker
Source: https://codefronts.com/components/css-image-slider/logo-marquee-endless-ticker/

Logo marquee endless ticker — continuous crawl of client logos for B2B and agency sites, the classic Trusted by strip you see on Stripe, Vercel, Notion, Linear, and Shopify Plus landing pages. A dual-cloned track loops forever with one @keyframes and pauses on hover; grayscale by default, brand-color on hover. Zero JavaScript, seamless wrap, no visible loop seam.
## HTML
```html
<div class="cis-18">
  <p class="cis-18__label">Trusted by teams at</p>
  <div class="cis-18__stage">
    <div class="cis-18__track">
      <span class="cis-18__logo">NORTHWIND</span>
      <span class="cis-18__logo">Ampersand</span>
      <span class="cis-18__logo">LOOMLABS</span>
      <span class="cis-18__logo">Tidepool</span>
      <span class="cis-18__logo">VELA</span>
      <span class="cis-18__logo">Quanta·</span>
      <span class="cis-18__logo" aria-hidden="true">NORTHWIND</span>
      <span class="cis-18__logo" aria-hidden="true">Ampersand</span>
      <span class="cis-18__logo" aria-hidden="true">LOOMLABS</span>
      <span class="cis-18__logo" aria-hidden="true">Tidepool</span>
      <span class="cis-18__logo" aria-hidden="true">VELA</span>
      <span class="cis-18__logo" aria-hidden="true">Quanta·</span>
    </div>
  </div>
</div>
```
## CSS
```css
.cis-18,
.cis-18 *,
.cis-18 *::before,
.cis-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-18 ::selection {
  background: oklch(0.85 0.05 250);
  color: #0a0c14;
}

.cis-18 {
  --speed: 26s;
  --fade: 14%;
  --text: #c7ccdb;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--text);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  background: linear-gradient(180deg,#0a0c12,#0e1119);
}

.cis-18__label {
  font: 700 11px ui-monospace,Menlo,monospace;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: #5c6377;
}

.cis-18__stage {
  width: min(920px,98vw);
  overflow: hidden;
  -webkit-mask-image: linear-gradient(90deg,transparent,#000 var(--fade),#000 calc(100% - var(--fade)),transparent);
  mask-image: linear-gradient(90deg,transparent,#000 var(--fade),#000 calc(100% - var(--fade)),transparent);
}

.cis-18__track {
  display: flex;
  align-items: center;
  gap: 64px;
  width: max-content;
  animation: cis-18-scroll var(--speed) linear infinite;
  will-change: transform;
}

.cis-18__stage:hover .cis-18__track {
  animation-play-state: paused;
}

.cis-18__logo {
  font-size: 26px;
  font-weight: 800;
  letter-spacing: -.01em;
  white-space: nowrap;
  color: var(--text);
  opacity: .62;
  transition: opacity .3s,color .3s;
  cursor: default;
}

.cis-18__logo:hover {
  opacity: 1;
  color: #fff;
}

@keyframes cis-18-scroll {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(-50%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cis-18__track {
    animation: none;
    flex-wrap: wrap;
    justify-content: center;
  }
}
```

## JavaScript
```js
/* No JavaScript — one @keyframes translateX(-50%) loop over a doubled logo track. */
```
