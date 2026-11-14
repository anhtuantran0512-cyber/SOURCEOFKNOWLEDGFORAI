---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/interactive-floating-badges/"
title: "Interactive Floating Badges"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "\"Save 20%\" and \"Best Value\" badges that live: they bob gently on an idle loop, then react to card hover by perking up — tilting, scaling and snapping to…"
has_js: "false"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive Floating Badges
Source: https://codefronts.com/components/css-pricing-tables/interactive-floating-badges/

"Save 20%" and "Best Value" badges that live: they bob gently on an idle loop, then react to card hover by perking up — tilting, scaling and snapping to attention — giving pricing tiers a playful, tactile personality without a single script.
## HTML
```html
<section class="prc-07" aria-label="Pricing with animated badges">
  <div class="prc-07__grid">
    <article class="prc-07__card">
      <span class="prc-07__badge prc-07__badge--tag" aria-hidden="true">Save 20%</span>
      <h3>Annual</h3><p class="prc-07__price">$96<small>/yr</small></p>
      <p class="prc-07__note">Two months free — 20% off monthly.</p>
      <a href="#" class="prc-07__cta">Choose Annual</a>
    </article>
    <article class="prc-07__card">
      <span class="prc-07__badge prc-07__badge--star" aria-hidden="true">Best<br>Value</span>
      <h3>2-Year</h3><p class="prc-07__price">$160<small>/2 yr</small></p>
      <p class="prc-07__note">Our best value — 33% off monthly.</p>
      <a href="#" class="prc-07__cta prc-07__cta--hot">Choose 2-Year</a>
    </article>
    <article class="prc-07__card">
      <span class="prc-07__badge prc-07__badge--new" aria-hidden="true">New</span>
      <h3>Lifetime</h3><p class="prc-07__price">$399<small> once</small></p>
      <p class="prc-07__note">Pay once, keep it forever. New tier.</p>
      <a href="#" class="prc-07__cta">Choose Lifetime</a>
    </article>
  </div>
</section>
```
## CSS
```css
.prc-07,
.prc-07 *,
.prc-07 *::before,
.prc-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-07 {
  --accent: oklch(0.62 0.2 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #fdf6f0;
  color: #241d18;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 64px 24px;
}

.prc-07__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: 22px;
  width: min(880px,100%);
}

.prc-07__card {
  position: relative;
  background: #fff;
  border: 1.5px solid #eadfd5;
  border-radius: 20px;
  padding: 34px 28px 28px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  transition: border-color .25s,transform .25s;
}

.prc-07__card:hover {
  border-color: var(--accent);
  transform: translateY(-4px);
}

.prc-07__badge {
  position: absolute;
  font-weight: 800;
  animation: prc-07-bob 3.2s ease-in-out infinite;
  transition: transform .3s cubic-bezier(.4,1.8,.4,1);
  will-change: transform;
}

.prc-07__card:hover .prc-07__badge {
  animation-play-state: paused;
}

.prc-07__badge--tag {
  top: -14px;
  right: 20px;
  font-size: 11.5px;
  letter-spacing: .05em;
  text-transform: uppercase;
  background: oklch(0.62 0.2 25);
  color: #fff;
  padding: 6px 13px;
  border-radius: 99px 99px 99px 4px;
  box-shadow: 0 8px 18px -8px oklch(0.62 0.2 25/.7);
}

.prc-07__card:hover .prc-07__badge--tag {
  transform: scale(1.12) rotate(-5deg);
}

.prc-07__badge--star {
  top: -26px;
  right: 14px;
  width: 64px;
  height: 64px;
  display: grid;
  place-items: center;
  text-align: center;
  font-size: 10.5px;
  line-height: 1.15;
  text-transform: uppercase;
  letter-spacing: .03em;
  color: #241d18;
  background: oklch(0.85 0.16 90);
  clip-path: polygon(50% 0,61% 12%,76% 6%,79% 22%,95% 25%,88% 39%,100% 50%,88% 61%,95% 75%,79% 78%,76% 94%,61% 88%,50% 100%,39% 88%,24% 94%,21% 78%,5% 75%,12% 61%,0 50%,12% 39%,5% 25%,21% 22%,24% 6%,39% 12%);
  animation-delay: -1.1s;
}

.prc-07__card:hover .prc-07__badge--star {
  transform: scale(1.18) rotate(12deg);
}

.prc-07__badge--new {
  top: -12px;
  right: 24px;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  background: #241d18;
  color: #fff;
  padding: 6px 12px;
  border-radius: 8px;
  animation-delay: -2.2s;
}

.prc-07__card:hover .prc-07__badge--new {
  transform: scale(1.1) rotate(4deg);
}

@keyframes prc-07-bob {
  0%,
    100% {
    transform: translateY(0) rotate(0deg);
  }

  50% {
    transform: translateY(-5px) rotate(2deg);
  }
}

.prc-07__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #8c7f72;
}

.prc-07__price {
  font-size: 42px;
  font-weight: 800;
  letter-spacing: -.03em;
}

.prc-07__price small {
  font-size: 15px;
  font-weight: 600;
  color: #8c7f72;
}

.prc-07__note {
  font-size: 13.5px;
  color: #6b6055;
  line-height: 1.5;
  flex: 1;
  margin-bottom: 16px;
}

.prc-07__cta {
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  font-size: 13.5px;
  padding: 12px;
  border-radius: 11px;
  border: 1.5px solid #eadfd5;
  color: #241d18;
  transition: border-color .2s,background .2s;
}

.prc-07__cta:hover {
  border-color: var(--accent);
}

.prc-07__cta--hot {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}

.prc-07__cta:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .prc-07__badge {
    animation: none;
    transition-duration: .01s;
  }

  .prc-07__card {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — badges idle on an infinite bob keyframe; card hover pauses the loop (animation-play-state) and a spring-eased transition snaps each badge into its reaction pose. */
```
