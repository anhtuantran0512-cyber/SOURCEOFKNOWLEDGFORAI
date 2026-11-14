---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/hover-reactive-profile-bio-card/"
title: "Hover-Reactive Profile Bio Card"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A creator bio card where a circular avatar breaks out and overlaps the top edge of the frosted glass panel."
has_js: "true"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hover-Reactive Profile Bio Card
Source: https://codefronts.com/components/css-liquid-glass-cards/hover-reactive-profile-bio-card/

A creator bio card where a circular avatar breaks out and overlaps the top edge of the frosted glass panel. As you move the cursor, the avatar casts a dynamic drop-shadow that swings and warps across the backdrop — as if a real light source were moving — while the whole card tilts with subtle parallax between avatar and pane.
## HTML
```html
<section class="lg-16" aria-label="Hover-reactive liquid glass profile bio card demo">
  <article class="lg-16__card" id="lg-16-card">
    <span class="lg-16__shadow" aria-hidden="true"></span>
    <div class="lg-16__avatar" role="img" aria-label="Avatar of Devin Cole">DC</div>
    <div class="lg-16__panel">
      <h3 class="lg-16__name">Devin Cole <span class="lg-16__verified" aria-label="Verified">✓</span></h3>
      <p class="lg-16__role">Motion Designer · Toronto</p>
      <p class="lg-16__bio">I animate interfaces that feel physical. Currently exploring Liquid Glass for the web.</p>
      <div class="lg-16__stats"><span><b>312</b> posts</span><span><b>24.8k</b> followers</span></div>
      <button class="lg-16__follow" type="button">Follow</button>
    </div>
  </article>
</section>
```
## CSS
```css
.lg-16,
.lg-16 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-16 {
  width: 100%;
  --accent: oklch(0.66 0.19 300);
  display: grid;
  place-items: center;
  min-height: 100vh;
  padding: 24px;
  perspective: 1000px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 120% at 25% 0%,#a78bfa,#6d28d9 45%,#1e1b4b);
}

.lg-16__card {
  position: relative;
  width: min(300px,100%);
  margin-top: 52px;
  transform-style: preserve-3d;
  transition: transform .25s ease;
  transform: perspective(900px) rotateX(calc(var(--py,0)*-6deg)) rotateY(calc(var(--px,0)*6deg));
}

.lg-16__shadow {
  position: absolute;
  top: -30px;
  left: 50%;
  width: 86px;
  height: 86px;
  border-radius: 50%;
  background: rgba(0,0,0,.55);
  filter: blur(16px);
  transform: translate(calc(-50% + var(--px,0)*-34px),calc(var(--py,0)*-22px));
  pointer-events: none;
}

.lg-16__avatar {
  position: absolute;
  top: -46px;
  left: 50%;
  transform: translateX(-50%) translateZ(55px);
  width: 92px;
  height: 92px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 30px;
  font-weight: 800;
  color: #fff;
  background: repeating-linear-gradient(45deg,#4c1d95,#4c1d95 8px,#6d28d9 8px,#6d28d9 16px);
  border: 3px solid rgba(255,255,255,.7);
}

.lg-16__panel {
  padding: 60px 24px 24px;
  border-radius: 24px;
  text-align: center;
  isolation: isolate;
  color: #fff;
  background: color-mix(in oklab,white 13%,transparent);
  border: 1px solid rgba(255,255,255,.4);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.55),0 30px 60px -30px rgba(0,0,0,.75);
  backdrop-filter: blur(22px) saturate(180%);
  -webkit-backdrop-filter: blur(22px) saturate(180%);
}

.lg-16__name {
  font-size: 20px;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 7px;
}

.lg-16__verified {
  width: 20px;
  height: 20px;
  font-size: 12px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: var(--accent);
  color: #fff;
}

.lg-16__role {
  font-size: 13px;
  color: rgba(255,255,255,.8);
  margin-top: 5px;
}

.lg-16__bio {
  font-size: 13px;
  line-height: 1.55;
  color: rgba(255,255,255,.85);
  margin: 12px 0;
}

.lg-16__stats {
  display: flex;
  justify-content: center;
  gap: 22px;
  margin: 8px 0 18px;
  font-size: 12px;
  color: rgba(255,255,255,.82);
}

.lg-16__stats b {
  display: block;
  font-size: 16px;
  color: #fff;
}

.lg-16__follow {
  width: 100%;
  min-height: 44px;
  border: 0;
  border-radius: 12px;
  cursor: pointer;
  font-weight: 700;
  font-size: 15px;
  color: #fff;
  background: var(--accent);
  box-shadow: 0 10px 24px -10px var(--accent);
}

.lg-16__follow:hover {
  filter: brightness(1.08);
}

.lg-16__follow:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-16__card {
    transition: none;
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const card = document.querySelector('#lg-16-card');
  if (!card) return;
  card.addEventListener('pointermove', (e) => {
    const r = card.getBoundingClientRect();
    card.style.setProperty('--px', ((e.clientX - r.left)/r.width * 2 - 1).toFixed(3));
    card.style.setProperty('--py', ((e.clientY - r.top)/r.height * 2 - 1).toFixed(3));
  });
  card.addEventListener('pointerleave', () => { card.style.setProperty('--px', 0); card.style.setProperty('--py', 0); });
})();
```
