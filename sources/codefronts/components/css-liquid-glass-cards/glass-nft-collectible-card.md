---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/glass-nft-collectible-card/"
title: "Glass NFT Collectible Card"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A collectible / NFT showcase card where the artwork sits behind a Liquid Glass 'protective case' — a refractive pane with a holographic sheen that shifts…"
has_js: "false"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glass NFT Collectible Card
Source: https://codefronts.com/components/css-liquid-glass-cards/glass-nft-collectible-card/

A collectible / NFT showcase card where the artwork sits behind a Liquid Glass 'protective case' — a refractive pane with a holographic sheen that shifts colour as the card tilts, plus an animated glowing aura behind the art. The premium, futuristic treatment Web3 and gaming projects search for.
## HTML
```html
<section class="lg-11" aria-label="Glass NFT collectible card demo">
  <article class="lg-11__card">
    <div class="lg-11__stage">
      <span class="lg-11__aura" aria-hidden="true"></span>
      <div class="lg-11__art" role="img" aria-label="Collectible artwork: Prism Golem #024"><span class="lg-11__ph">artwork</span></div>
      <span class="lg-11__holo" aria-hidden="true"></span>
    </div>
    <div class="lg-11__info">
      <div class="lg-11__titles"><h3>Prism Golem</h3><span class="lg-11__rare">Legendary · #024</span></div>
      <div class="lg-11__bidrow"><div><span class="lg-11__cap">Current bid</span><span class="lg-11__price">4.20 ETH</span></div><button class="lg-11__bid" type="button">Place bid</button></div>
    </div>
  </article>
</section>
```
## CSS
```css
.lg-11,
.lg-11 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --holo {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.lg-11 {
  --a: oklch(0.72 0.2 300);
  --b: oklch(0.78 0.18 200);
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 24px;
  perspective: 1000px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 120% at 50% 0%,#1e1b4b,#0b1020 70%);
}

.lg-11__card {
  width: min(280px,100%);
  border-radius: 24px;
  padding: 14px;
  isolation: isolate;
  background: color-mix(in oklab,white 8%,transparent);
  border: 1px solid rgba(255,255,255,.28);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4),0 34px 70px -30px rgba(0,0,0,.85);
  backdrop-filter: blur(16px) saturate(170%);
  -webkit-backdrop-filter: blur(16px) saturate(170%);
  transition: transform .5s ease;
  transform-style: preserve-3d;
}

.lg-11__card:hover {
  transform: rotateY(-8deg) rotateX(6deg);
}

.lg-11__stage {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  aspect-ratio: 1;
}

.lg-11__aura {
  position: absolute;
  inset: -30%;
  background: conic-gradient(from 0deg,var(--a),var(--b),var(--a));
  filter: blur(24px);
  animation: lg-11-spin 8s linear infinite;
  opacity: .8;
}

@keyframes lg-11-spin {
  to {
    transform: rotate(360deg);
  }
}

.lg-11__art {
  position: absolute;
  inset: 8px;
  border-radius: 12px;
  display: grid;
  place-items: center;
  background: repeating-linear-gradient(45deg,#312e81,#312e81 10px,#4338ca 10px,#4338ca 20px);
  border: 1px solid rgba(255,255,255,.3);
}

.lg-11__ph {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  color: rgba(255,255,255,.7);
}

.lg-11__holo {
  position: absolute;
  inset: 0;
  background: conic-gradient(from var(--holo),transparent,rgba(255,255,255,.4),transparent 30%,rgba(120,200,255,.4) 55%,transparent 70%);
  mix-blend-mode: screen;
  animation: lg-11-holo 6s linear infinite;
  pointer-events: none;
}

@keyframes lg-11-holo {
  to {
    --holo: 360deg;
  }
}

.lg-11__info {
  padding: 14px 6px 6px;
  color: #fff;
}

.lg-11__titles {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.lg-11__titles h3 {
  font-size: 18px;
  font-weight: 800;
}

.lg-11__rare {
  font-size: 11px;
  font-weight: 700;
  color: #c7d2fe;
}

.lg-11__bidrow {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-top: 14px;
}

.lg-11__cap {
  display: block;
  font-size: 10px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(255,255,255,.65);
}

.lg-11__price {
  font-size: 20px;
  font-weight: 800;
}

.lg-11__bid {
  min-height: 44px;
  padding: 0 18px;
  border: 0;
  border-radius: 12px;
  cursor: pointer;
  font-weight: 700;
  color: #fff;
  background: linear-gradient(120deg,var(--a),var(--b));
  box-shadow: 0 10px 24px -10px var(--a);
}

.lg-11__bid:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-11__aura,
    .lg-11__holo {
    animation: none;
  }

  .lg-11__card:hover {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — an animated conic aura glows behind the artwork while a screen-blended conic holo sweep (@property --holo) plays over a frosted glass case, and a hover perspective tilt travels the sheen. */
```
