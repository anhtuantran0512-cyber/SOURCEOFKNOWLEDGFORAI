---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/hero-banner-gradient-overlay/"
title: "Hero Banner Gradient Overlay"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "A real-photo travel hero showing the three overlays that make text readable on any image: a directional scrim gradient, a brand duotone tint via blend modes,…"
has_js: "false"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hero Banner Gradient Overlay
Source: https://codefronts.com/design-styles/css-gradient-ui/hero-banner-gradient-overlay/

A real-photo travel hero showing the three overlays that make text readable on any image: a directional scrim gradient, a brand duotone tint via blend modes, and an eased bottom fade for captions — each labelled on the live layout.
## HTML
```html
<div class="cgu-10-group">
<section class="cgu-10" aria-label="Hero banner gradient overlay demo">
  <div class="cgu-10__hero">
    <div class="cgu-10__content">
      <span class="cgu-10__badge">Patagonia · Expedition 2027</span>
      <h2 class="cgu-10__title">Text you can read.<br>A photo you can still see.</h2>
      <p class="cgu-10__sub">A directional scrim darkens only where the copy sits — the peaks stay bright. That's the whole trick.</p>
      <div class="cgu-10__row">
        <button class="cgu-10__btn" type="button">Plan the route</button>
        <button class="cgu-10__btn cgu-10__btn--ghost" type="button">Watch the film</button>
      </div>
    </div>
    <figure class="cgu-10__caption">
      <figcaption>Cerro Torre at dawn — the caption bar under this line fades in with an eased 5-stop gradient, not a hard 2-stop edge.</figcaption>
    </figure>
  </div>
  <div class="cgu-10__legend">
    <p><strong>Layer 1</strong> directional scrim <code>75deg</code></p>
    <p><strong>Layer 2</strong> duotone tint <code>background-blend-mode: multiply</code> (badge)</p>
    <p><strong>Layer 3</strong> eased bottom fade (caption)</p>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-10-group {
  display: block;
  width: 100%;
}

.cgu-10,
.cgu-10 *,
.cgu-10 *::before,
.cgu-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgu-10 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  grid-template-rows: 1fr auto;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #fff;
  background: #080716;
}

.cgu-10__hero {
  position: relative;
  display: grid;
  align-content: center;
  padding: 80px clamp(24px,7vw,96px);
  min-height: 82vh;
  background: linear-gradient(75deg,rgba(8,7,22,.88) 0%,rgba(8,7,22,.55) 42%,rgba(8,7,22,.08) 68%,rgba(8,7,22,0) 80%),url("https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1800&q=80") center/cover no-repeat;
}

.cgu-10__content {
  position: relative;
  width: min(620px,100%);
  display: grid;
  gap: 20px;
  justify-items: start;
}

.cgu-10__badge {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .2em;
  text-transform: uppercase;
  padding: 8px 16px;
  border-radius: 9999px;
  color: #fff;
  background: linear-gradient(120deg,#7c3aed,#0ea5e9),rgba(255,255,255,.2);
  background-blend-mode: multiply;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.3);
}

.cgu-10__title {
  font-size: clamp(34px,5.4vw,66px);
  font-weight: 850;
  letter-spacing: -.025em;
  line-height: 1.04;
  text-wrap: balance;
}

.cgu-10__sub {
  max-width: 44ch;
  font-size: 16px;
  line-height: 1.65;
  color: rgba(255,255,255,.88);
  text-wrap: pretty;
}

.cgu-10__row {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 8px;
}

.cgu-10__btn {
  font: inherit;
  font-size: 15px;
  font-weight: 750;
  color: #0b1024;
  padding: 14px 30px;
  border: none;
  border-radius: 9999px;
  cursor: pointer;
  background: linear-gradient(180deg,#fff,#dbeafe);
  transition: transform .3s,box-shadow .3s;
  box-shadow: 0 14px 32px -14px rgba(0,0,0,.6);
}

.cgu-10__btn:hover,
.cgu-10__btn:focus-visible {
  transform: translateY(-2px);
}

.cgu-10__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.cgu-10__btn--ghost {
  color: #fff;
  background: rgba(255,255,255,.12);
  box-shadow: inset 0 0 0 1.5px rgba(255,255,255,.55);
}

.cgu-10__caption {
  position: absolute;
  inset: auto 0 0 0;
  padding: 64px clamp(24px,7vw,96px) 22px;
  background: linear-gradient(to top,rgba(5,4,14,.85) 0%,rgba(5,4,14,.62) 34%,rgba(5,4,14,.3) 62%,rgba(5,4,14,.09) 82%,rgba(5,4,14,0) 100%);
}

.cgu-10__caption figcaption {
  font-size: 13px;
  line-height: 1.55;
  color: rgba(255,255,255,.85);
  max-width: 74ch;
}

.cgu-10__legend {
  display: flex;
  gap: 26px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 22px 24px;
  border-top: 1px solid rgba(255,255,255,.08);
}

.cgu-10__legend p {
  font-size: 12.5px;
  color: #9aa0c0;
}

.cgu-10__legend strong {
  color: #e3e6ff;
  font-weight: 750;
  margin-right: 6px;
}

.cgu-10__legend code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  color: #93c5fd;
  background: rgba(147,197,253,.1);
  padding: 1px 5px;
  border-radius: 5px;
}

@media (prefers-reduced-motion: reduce) {
  .cgu-10__btn {
    transition: box-shadow .2s;
  }
}
```

## JavaScript
```js
/* No JavaScript — the scrim, duotone badge tint (background-blend-mode: multiply) and eased caption fade are all background layers. */
```
