---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/team-member-spotlight-card/"
title: "Team Member Spotlight Card"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A team-roster card with a dynamic spotlight that tracks the cursor across the glass face — a soft specular highlight glides over the frosted surface like…"
has_js: "true"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Team Member Spotlight Card
Source: https://codefronts.com/components/css-liquid-glass-cards/team-member-spotlight-card/

A team-roster card with a dynamic spotlight that tracks the cursor across the glass face — a soft specular highlight glides over the frosted surface like light raking across real glass, brightening the rim and lifting the portrait as it passes. Works as a grid of cards, each with its own independent spotlight.
## HTML
```html
<section class="lg-17" aria-label="Liquid glass team member spotlight cards demo">
  <div class="lg-17__grid">
    <article class="lg-17__card" tabindex="0"><div class="lg-17__glow" aria-hidden="true"></div><div class="lg-17__ava" role="img" aria-label="Portrait of Ana Ruiz">AR</div><h3 class="lg-17__name">Ana Ruiz</h3><p class="lg-17__role">Head of Design</p><button class="lg-17__msg" type="button">Message</button></article>
    <article class="lg-17__card" tabindex="0"><div class="lg-17__glow" aria-hidden="true"></div><div class="lg-17__ava" role="img" aria-label="Portrait of Ben Osei">BO</div><h3 class="lg-17__name">Ben Osei</h3><p class="lg-17__role">Staff Engineer</p><button class="lg-17__msg" type="button">Message</button></article>
  </div>
</section>
```
## CSS
```css
.lg-17,
.lg-17 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-17 {
  width: 100%;
  --accent: oklch(0.78 0.15 200);
  display: grid;
  place-items: center;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: conic-gradient(from 210deg at 40% 50%,#0f172a,#155e75,#1e3a8a,#0f172a);
  background-size: 220% 220%;
  animation: lg-17-bg 22s ease-in-out infinite;
}

@keyframes lg-17-bg {
  50% {
    background-position: 100% 100%;
  }
}

.lg-17__grid {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  justify-content: center;
}

.lg-17__card {
  --mx: 50%;
  --my: 0%;
  position: relative;
  width: 180px;
  padding: 24px 20px;
  border-radius: 22px;
  text-align: center;
  overflow: hidden;
  isolation: isolate;
  color: #fff;
  background: color-mix(in oklab,white 11%,transparent);
  border: 1px solid rgba(255,255,255,.32);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.45),0 24px 50px -28px rgba(0,0,0,.7);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  transition: transform .3s;
}

.lg-17__card:hover,
.lg-17__card:focus-visible {
  transform: translateY(-4px);
  outline: none;
}

.lg-17__card:focus-visible {
  box-shadow: inset 0 1px 0 rgba(255,255,255,.45),0 0 0 3px #fff;
}

.lg-17__glow {
  position: absolute;
  inset: 0;
  background: radial-gradient(160px 160px at var(--mx) var(--my),color-mix(in oklab,var(--accent) 55%,transparent),transparent 60%);
  mix-blend-mode: screen;
  pointer-events: none;
  transition: background .1s linear;
}

.lg-17__ava {
  position: relative;
  width: 72px;
  height: 72px;
  margin: 0 auto 14px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 24px;
  font-weight: 800;
  color: #fff;
  background: repeating-linear-gradient(45deg,#0e7490,#0e7490 7px,#0891b2 7px,#0891b2 14px);
  border: 2px solid rgba(255,255,255,.6);
}

.lg-17__name {
  position: relative;
  font-size: 17px;
  font-weight: 800;
}

.lg-17__role {
  position: relative;
  font-size: 12.5px;
  color: rgba(255,255,255,.8);
  margin-top: 3px;
}

.lg-17__msg {
  position: relative;
  width: 100%;
  min-height: 44px;
  margin-top: 16px;
  border: 0;
  border-radius: 11px;
  cursor: pointer;
  font-weight: 700;
  font-size: 13.5px;
  color: #06232b;
  background: color-mix(in oklab,var(--accent) 82%,white);
  box-shadow: 0 8px 20px -10px var(--accent);
}

.lg-17__msg:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-17 {
    animation: none;
  }

  .lg-17__card {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.lg-17__card').forEach((card) => {
    let raf;
    const move = (e) => {
      const r = card.getBoundingClientRect();
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(() => {
        card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        card.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    };
    card.addEventListener('pointermove', move);
    card.addEventListener('pointerleave', () => { card.style.setProperty('--mx', '50%'); card.style.setProperty('--my', '0%'); });
    card.addEventListener('focus', () => { card.style.setProperty('--mx', '50%'); card.style.setProperty('--my', '40%'); });
  });
})();
```
