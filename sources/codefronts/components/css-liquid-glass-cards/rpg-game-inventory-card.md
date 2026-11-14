---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/rpg-game-inventory-card/"
title: "RPG Game Inventory Card"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "An RPG inventory panel where empty slots read as hollow, recessed glass compartments and filled slots hold a shimmering Liquid Glass item case — hover or…"
has_js: "false"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: RPG Game Inventory Card
Source: https://codefronts.com/components/css-liquid-glass-cards/rpg-game-inventory-card/

An RPG inventory panel where empty slots read as hollow, recessed glass compartments and filled slots hold a shimmering Liquid Glass item case — hover or focus a filled slot and a specular sheen sweeps across its face while the item lifts and its rarity glow intensifies. A framed HUD card with a title bar and gold counter.
## HTML
```html
<section class="lg-21" aria-label="Liquid glass RPG game inventory card demo">
  <article class="lg-21__panel">
    <header class="lg-21__bar"><h3 class="lg-21__title">Inventory</h3><span class="lg-21__gold" aria-label="1,240 gold">◉ 1,240</span></header>
    <div class="lg-21__grid" role="group" aria-label="Item slots">
      <button class="lg-21__slot" type="button" style="--rar:oklch(0.7 0.2 300)" aria-label="Void Blade, epic"><span class="lg-21__item" aria-hidden="true">⚔</span><span class="lg-21__qty">1</span></button>
      <button class="lg-21__slot" type="button" style="--rar:oklch(0.78 0.18 85)" aria-label="Sun Potion, rare, five held"><span class="lg-21__item" aria-hidden="true">⚗</span><span class="lg-21__qty">×5</span></button>
      <button class="lg-21__slot lg-21__slot--empty" type="button" aria-label="Empty slot"></button>
      <button class="lg-21__slot" type="button" style="--rar:oklch(0.72 0.19 155)" aria-label="Emerald Shield, uncommon"><span class="lg-21__item" aria-hidden="true">◈</span></button>
      <button class="lg-21__slot" type="button" style="--rar:oklch(0.7 0.2 20)" aria-label="Fire Rune, rare, two held"><span class="lg-21__item" aria-hidden="true">✦</span><span class="lg-21__qty">×2</span></button>
      <button class="lg-21__slot lg-21__slot--empty" type="button" aria-label="Empty slot"></button>
      <button class="lg-21__slot" type="button" style="--rar:oklch(0.72 0.16 240)" aria-label="Frost Orb, common"><span class="lg-21__item" aria-hidden="true">❄</span></button>
      <button class="lg-21__slot" type="button" style="--rar:oklch(0.75 0.18 55)" aria-label="Gold Key, rare"><span class="lg-21__item" aria-hidden="true">⚷</span></button>
      <button class="lg-21__slot lg-21__slot--empty" type="button" aria-label="Empty slot"></button>
    </div>
  </article>
</section>
```
## CSS
```css
.lg-21,
.lg-21 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-21 {
  width: 100%;
  display: grid;
  place-items: center;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 120% at 50% 10%,#1e293b,#020617 70%);
}

.lg-21__panel {
  width: min(340px,100%);
  padding: 18px;
  border-radius: 22px;
  isolation: isolate;
  color: #fff;
  background: color-mix(in oklab,white 9%,rgba(6,10,20,.4));
  border: 1px solid rgba(255,255,255,.22);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.32),0 30px 62px -30px rgba(0,0,0,.85);
  backdrop-filter: blur(20px) saturate(170%);
  -webkit-backdrop-filter: blur(20px) saturate(170%);
}

.lg-21__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 14px;
  margin-bottom: 14px;
  border-bottom: 1px solid rgba(255,255,255,.14);
}

.lg-21__title {
  font-size: 15px;
  font-weight: 800;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.lg-21__gold {
  font-size: 13px;
  font-weight: 800;
  color: #ffe6a3;
  font-variant-numeric: tabular-nums;
}

.lg-21__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 12px;
}

.lg-21__slot {
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
  backdrop-filter: blur(14px) saturate(170%);
  -webkit-backdrop-filter: blur(14px) saturate(170%);
  transition: transform .25s,box-shadow .3s;
}

.lg-21__slot--empty {
  background: rgba(255,255,255,.03);
  box-shadow: inset 0 3px 12px rgba(0,0,0,.55),inset 0 0 0 1px rgba(255,255,255,.05);
  cursor: default;
}

.lg-21__slot::after {
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

.lg-21__slot:not(.lg-21__slot--empty):hover,
.lg-21__slot:not(.lg-21__slot--empty):focus-visible {
  transform: translateY(-3px);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),inset 0 0 26px -4px var(--rar),0 18px 34px -16px rgba(0,0,0,.7),0 0 18px -4px var(--rar);
  outline: none;
}

.lg-21__slot:not(.lg-21__slot--empty):hover::after,
.lg-21__slot:not(.lg-21__slot--empty):focus-visible::after {
  animation: lg-21-sweep .6s ease-out;
}

@keyframes lg-21-sweep {
  from {
    left: -120%;
  }

  to {
    left: 140%;
  }
}

.lg-21__slot:focus-visible {
  box-shadow: inset 0 0 26px -4px var(--rar),0 0 0 3px #fff;
}

.lg-21__item {
  font-size: 26px;
  color: #fff;
  filter: drop-shadow(0 0 8px var(--rar));
}

.lg-21__qty {
  position: absolute;
  right: 5px;
  bottom: 4px;
  font-size: 10px;
  font-weight: 800;
  color: #fff;
  background: rgba(0,0,0,.5);
  padding: 1px 5px;
  border-radius: 6px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-21__slot {
    transition: none;
  }

  .lg-21__slot::after {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a grid of frosted slots; empty slots use an inset shadow to look hollow and recessed, while filled slots set a rarity --rar for their inner glow and sweep a one-shot specular shimmer (::after keyframe) on :hover/:focus-visible while lifting the item. */
```
