---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/game-inventory-slot-cards/"
title: "Game Inventory Slot Cards"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A grid of identical Liquid Glass inventory slots — the frosted item cases from a game HUD."
has_js: "false"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Game Inventory Slot Cards
Source: https://codefronts.com/components/css-liquid-glass-cards/game-inventory-slot-cards/

A grid of identical Liquid Glass inventory slots — the frosted item cases from a game HUD. Hover or focus a slot and a specular shimmer sweeps across its glass face while the item lifts and its rarity glow intensifies. Empty slots read as darker recessed glass. Pure CSS, keyboard-navigable.
## HTML
```html
<section class="lg-13" aria-label="Liquid glass game inventory slot cards demo">
  <div class="lg-13__grid" role="group" aria-label="Inventory">
    <button class="lg-13__slot" type="button" style="--rar:oklch(0.7 0.2 300)" aria-label="Void Blade, epic"><span class="lg-13__item" aria-hidden="true">⚔</span><span class="lg-13__qty">1</span></button>
    <button class="lg-13__slot" type="button" style="--rar:oklch(0.78 0.18 85)" aria-label="Sun Potion, rare"><span class="lg-13__item" aria-hidden="true">⚗</span><span class="lg-13__qty">×5</span></button>
    <button class="lg-13__slot" type="button" style="--rar:oklch(0.72 0.19 155)" aria-label="Emerald Shield, uncommon"><span class="lg-13__item" aria-hidden="true">◈</span></button>
    <button class="lg-13__slot lg-13__slot--empty" type="button" aria-label="Empty slot"></button>
    <button class="lg-13__slot" type="button" style="--rar:oklch(0.7 0.2 20)" aria-label="Fire Rune, rare"><span class="lg-13__item" aria-hidden="true">✦</span><span class="lg-13__qty">×2</span></button>
    <button class="lg-13__slot" type="button" style="--rar:oklch(0.72 0.16 240)" aria-label="Frost Orb, common"><span class="lg-13__item" aria-hidden="true">❄</span></button>
    <button class="lg-13__slot lg-13__slot--empty" type="button" aria-label="Empty slot"></button>
    <button class="lg-13__slot" type="button" style="--rar:oklch(0.75 0.18 55)" aria-label="Gold Key, rare"><span class="lg-13__item" aria-hidden="true">⚷</span></button>
  </div>
</section>
```
## CSS
```css
.lg-13,
.lg-13 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-13 {
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 120% at 50% 10%,#1e293b,#020617 70%);
}

.lg-13__grid {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 12px;
  width: min(360px,100%);
}

.lg-13__slot {
  position: relative;
  aspect-ratio: 1;
  min-height: 44px;
  border: 0;
  border-radius: 16px;
  cursor: pointer;
  overflow: hidden;
  isolation: isolate;
  display: grid;
  place-items: center;
  background: color-mix(in oklab,white 10%,transparent);
  border: 1px solid rgba(255,255,255,.28);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4),inset 0 0 20px -6px var(--rar,transparent),0 14px 30px -18px rgba(0,0,0,.7);
  backdrop-filter: blur(16px) saturate(170%);
  -webkit-backdrop-filter: blur(16px) saturate(170%);
  transition: transform .25s,box-shadow .3s;
}

.lg-13__slot--empty {
  background: rgba(255,255,255,.04);
  box-shadow: inset 0 2px 10px rgba(0,0,0,.5),inset 0 0 0 1px rgba(255,255,255,.06);
  cursor: default;
}

.lg-13__slot::after {
  content: "";
  position: absolute;
  top: -60%;
  left: -120%;
  width: 60%;
  height: 220%;
  background: linear-gradient(90deg,transparent,rgba(255,255,255,.55),transparent);
  transform: rotate(22deg);
  pointer-events: none;
}

.lg-13__slot:not(.lg-13__slot--empty):hover,
.lg-13__slot:not(.lg-13__slot--empty):focus-visible {
  transform: translateY(-3px);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),inset 0 0 26px -4px var(--rar),0 18px 34px -16px rgba(0,0,0,.7),0 0 18px -4px var(--rar);
  outline: none;
}

.lg-13__slot:not(.lg-13__slot--empty):hover::after,
.lg-13__slot:not(.lg-13__slot--empty):focus-visible::after {
  animation: lg-13-sweep .6s ease-out;
}

@keyframes lg-13-sweep {
  from {
    left: -120%;
  }

  to {
    left: 140%;
  }
}

.lg-13__slot:focus-visible {
  box-shadow: inset 0 0 26px -4px var(--rar),0 0 0 3px #fff;
}

.lg-13__item {
  font-size: 26px;
  color: #fff;
  filter: drop-shadow(0 0 8px var(--rar));
}

.lg-13__qty {
  position: absolute;
  right: 5px;
  bottom: 4px;
  font-size: 10px;
  font-weight: 800;
  color: #fff;
  background: rgba(0,0,0,.45);
  padding: 1px 5px;
  border-radius: 6px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-13__slot {
    transition: none;
  }

  .lg-13__slot::after {
    display: none;
  }
}

@media (max-width: 420px) {
  .lg-13__grid {
    grid-template-columns: repeat(3,1fr);
  }
}
```

## JavaScript
```js
/* No JavaScript — a responsive grid of frosted slots; each sets a rarity --rar for its inner glow, and :hover/:focus-visible sweeps a one-shot specular shimmer (::after keyframe) while lifting the item. */
```
