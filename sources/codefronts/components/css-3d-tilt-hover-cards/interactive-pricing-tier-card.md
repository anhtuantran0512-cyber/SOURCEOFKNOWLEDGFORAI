---
source: "codefronts"
url: "https://codefronts.com/components/css-3d-tilt-hover-cards/interactive-pricing-tier-card/"
title: "Interactive Pricing Tier Card"
section: "components"
category: "css-3d-tilt-hover-cards"
category_name: "CSS 3D Tilt Hover Cards"
description: "A three-tier pricing row where every card tilts toward the cursor, but the featured Pro tier adds a scale boost and a violet glow that intensifies with hover…"
has_js: "true"
---

Here's a working CSS 3D Tilt Hover Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive Pricing Tier Card
Source: https://codefronts.com/components/css-3d-tilt-hover-cards/interactive-pricing-tier-card/

A three-tier pricing row where every card tilts toward the cursor, but the featured Pro tier adds a scale boost and a violet glow that intensifies with hover — the classic SaaS landing-page trick for steering eyes (and clicks) to the plan you want sold. One shared handler drives all three cards.
## HTML
```html
<section class="thc-03" aria-label="Pricing tier tilt cards demo">
  <div class="thc-03__row">
    <article class="thc-03__card" tabindex="0" aria-label="Starter plan, 12 dollars per month">
      <h3 class="thc-03__tier">Starter</h3>
      <p class="thc-03__price"><strong>$12</strong><span>/mo</span></p>
      <ul class="thc-03__feats"><li>3 projects</li><li>Community support</li><li>1 GB storage</li></ul>
      <button class="thc-03__cta" type="button">Choose Starter</button>
    </article>
    <article class="thc-03__card thc-03__card--featured" tabindex="0" aria-label="Pro plan, 29 dollars per month, most popular">
      <span class="thc-03__badge">MOST POPULAR</span>
      <h3 class="thc-03__tier">Pro</h3>
      <p class="thc-03__price"><strong>$29</strong><span>/mo</span></p>
      <ul class="thc-03__feats"><li>Unlimited projects</li><li>Priority support</li><li>100 GB storage</li></ul>
      <button class="thc-03__cta thc-03__cta--solid" type="button">Choose Pro</button>
    </article>
    <article class="thc-03__card" tabindex="0" aria-label="Team plan, 79 dollars per month">
      <h3 class="thc-03__tier">Team</h3>
      <p class="thc-03__price"><strong>$79</strong><span>/mo</span></p>
      <ul class="thc-03__feats"><li>Everything in Pro</li><li>SSO &amp; audit log</li><li>Unlimited storage</li></ul>
      <button class="thc-03__cta" type="button">Choose Team</button>
    </article>
  </div>
</section>
```
## CSS
```css
.thc-03,
.thc-03 *,
.thc-03 *::before,
.thc-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.thc-03 {
  --glow: oklch(0.62 0.21 295);
  --ink: oklch(0.94 0.01 280);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(90% 100% at 50% 0%,oklch(0.24 0.06 295 / .8),transparent 60%),oklch(0.15 0.02 285);
}

.thc-03 .thc-03__row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  width: min(760px,100%);
}

.thc-03 .thc-03__card {
  position: relative;
  flex: 1 1 200px;
  max-width: 240px;
  padding: 26px 22px;
  border-radius: 20px;
  background: linear-gradient(165deg,oklch(0.22 0.03 290),oklch(0.18 0.025 285));
  border: 1px solid rgba(255,255,255,.1);
  transform: perspective(1000px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg)) scale(var(--pop,1));
  transition: transform .55s cubic-bezier(.2,.9,.3,1.1),box-shadow .55s ease;
  box-shadow: 0 20px 44px -26px rgba(0,0,0,.8);
}

.thc-03 .thc-03__card.is-live {
  transition: transform .08s linear,box-shadow .3s ease;
}

.thc-03 .thc-03__card:focus-visible {
  outline: 3px solid var(--glow);
  outline-offset: 4px;
}

.thc-03 .thc-03__card--featured {
  border-color: color-mix(in oklab,var(--glow) 55%,transparent);
  box-shadow: 0 20px 50px -22px color-mix(in oklab,var(--glow) 55%,transparent);
}

.thc-03 .thc-03__card--featured.is-live {
  --pop: 1.045;
  box-shadow: 0 28px 64px -20px color-mix(in oklab,var(--glow) 75%,transparent);
}

.thc-03 .thc-03__badge {
  position: absolute;
  top: -11px;
  left: 50%;
  translate: -50% 0;
  font: 700 9.5px/1 'Segoe UI',sans-serif;
  letter-spacing: .12em;
  color: #fff;
  background: linear-gradient(120deg,var(--glow),oklch(0.55 0.2 330));
  padding: 7px 12px;
  border-radius: 999px;
}

.thc-03 .thc-03__tier {
  font-size: 15px;
  font-weight: 600;
  color: rgba(255,255,255,.75);
}

.thc-03 .thc-03__price {
  margin-top: 10px;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
}

.thc-03 .thc-03__price strong {
  font-size: 36px;
  font-weight: 800;
}

.thc-03 .thc-03__price span {
  font-size: 13px;
  color: rgba(255,255,255,.5);
}

.thc-03 .thc-03__feats {
  list-style: none;
  margin-top: 16px;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.thc-03 .thc-03__feats li {
  font-size: 13px;
  color: rgba(255,255,255,.7);
  padding-left: 18px;
  background: linear-gradient(var(--glow),var(--glow)) no-repeat 0 55%/8px 2px;
}

.thc-03 .thc-03__cta {
  margin-top: 20px;
  width: 100%;
  height: 40px;
  border-radius: 10px;
  font: 600 13px 'Segoe UI',sans-serif;
  cursor: pointer;
  color: var(--ink);
  background: transparent;
  border: 1px solid rgba(255,255,255,.25);
  transition: background .25s ease;
}

.thc-03 .thc-03__cta:hover {
  background: rgba(255,255,255,.08);
}

.thc-03 .thc-03__cta--solid {
  border: none;
  color: #fff;
  background: linear-gradient(120deg,var(--glow),oklch(0.55 0.2 330));
}

.thc-03 .thc-03__cta:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .thc-03 .thc-03__card {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const cards = document.querySelectorAll('.thc-03 .thc-03__card');
  if (!cards.length) return;
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const MAX = 9;
  cards.forEach((card) => {          // one bind loop — adding a 4th tier is pure HTML
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
      card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
      card.classList.add('is-live'); // featured card also picks up its scale boost here
    });
    card.addEventListener('pointerleave', () => {
      card.classList.remove('is-live');
      card.style.setProperty('--rx', '0deg');
      card.style.setProperty('--ry', '0deg');
    });
  });
})();
```
