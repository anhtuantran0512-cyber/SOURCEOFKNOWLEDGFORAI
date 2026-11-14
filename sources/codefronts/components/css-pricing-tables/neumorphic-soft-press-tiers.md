---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/neumorphic-soft-press-tiers/"
title: "Neumorphic Soft-Press Tiers"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "Tactile soft-UI pricing: cards extrude from a matching background with the signature dual light/dark shadows, and pressing a card's button physically sinks…"
has_js: "false"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Soft-Press Tiers
Source: https://codefronts.com/components/css-pricing-tables/neumorphic-soft-press-tiers/

Tactile soft-UI pricing: cards extrude from a matching background with the signature dual light/dark shadows, and pressing a card's button physically sinks it — the shadows invert to inset, mimicking a real button being pushed into the surface.
## HTML
```html
<section class="prc-18" aria-label="Neumorphic pricing tiers">
  <h2 class="prc-18__title">Choose your tier</h2>
  <div class="prc-18__grid" role="radiogroup" aria-label="Plan selection">
    <label class="prc-18__card"><input type="radio" name="prc-18-plan" class="prc-18__sr" value="calm"><h3>Calm</h3><p class="prc-18__price">$7<small>/mo</small></p><ul><li>10 sessions</li><li>Sleep stories</li></ul><span class="prc-18__btn">Select</span></label>
    <label class="prc-18__card"><input type="radio" name="prc-18-plan" class="prc-18__sr" value="focus" checked><h3>Focus</h3><p class="prc-18__price">$14<small>/mo</small></p><ul><li>Unlimited sessions</li><li>Focus soundscapes</li><li>Stats</li></ul><span class="prc-18__btn">Select</span></label>
    <label class="prc-18__card"><input type="radio" name="prc-18-plan" class="prc-18__sr" value="flow"><h3>Flow</h3><p class="prc-18__price">$21<small>/mo</small></p><ul><li>Everything in Focus</li><li>1:1 coaching</li></ul><span class="prc-18__btn">Select</span></label>
  </div>
</section>
```
## CSS
```css
.prc-18,
.prc-18 *,
.prc-18 *::before,
.prc-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-18 {
  --base: #e4e9f2;
  --accent: oklch(0.55 0.16 265);
  --lite: color-mix(in oklch,var(--base),white 70%);
  --shade: color-mix(in oklch,var(--base),#3a4664 22%);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--base);
  color: #2c3242;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 56px 24px;
}

.prc-18__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.prc-18__title {
  text-align: center;
  font-size: clamp(24px,3.6vw,34px);
  font-weight: 800;
  letter-spacing: -.02em;
  margin-bottom: 40px;
}

.prc-18__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: 26px;
  width: min(880px,100%);
  margin: 0 auto;
}

.prc-18__card {
  background: var(--base);
  border-radius: 24px;
  padding: 30px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  cursor: pointer;
  box-shadow: -9px -9px 20px var(--lite),9px 9px 20px var(--shade);
  border: 2px solid transparent;
  transition: box-shadow .3s,border-color .3s,transform .2s;
}

.prc-18__card:hover {
  transform: translateY(-3px);
}

.prc-18__card:has(.prc-18__sr:checked) {
  border-color: var(--accent);
  box-shadow: -4px -4px 12px var(--lite),4px 4px 12px var(--shade);
}

.prc-18__card:has(.prc-18__sr:focus-visible) {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.prc-18__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: #5f677e;
}

.prc-18__price {
  font-size: 42px;
  font-weight: 800;
  letter-spacing: -.03em;
}

.prc-18__price small {
  font-size: 15px;
  font-weight: 600;
  color: #7d86a0;
}

.prc-18__card ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 9px;
  font-size: 13.5px;
  color: #525a72;
  flex: 1;
  margin: 10px 0 20px;
}

.prc-18__card li::before {
  content: "●";
  font-size: 8px;
  vertical-align: 2px;
  color: var(--accent);
  margin-right: 10px;
}

.prc-18__btn {
  text-align: center;
  font-weight: 700;
  font-size: 13.5px;
  padding: 13px;
  border-radius: 14px;
  background: var(--base);
  color: #2c3242;
  box-shadow: -5px -5px 12px var(--lite),5px 5px 12px var(--shade);
  transition: box-shadow .18s,transform .18s,color .3s;
}

.prc-18__card:hover .prc-18__btn {
  color: var(--accent);
}

.prc-18__card:active .prc-18__btn {
  box-shadow: inset -4px -4px 10px var(--lite),inset 4px 4px 10px var(--shade);
  transform: translateY(1px);
}

.prc-18__card:has(.prc-18__sr:checked) .prc-18__btn {
  box-shadow: inset -4px -4px 10px var(--lite),inset 4px 4px 10px var(--shade);
  color: var(--accent);
}

@media (prefers-reduced-motion: reduce) {
  .prc-18__card,
    .prc-18__btn {
    transition-duration: .01s;
  }

  .prc-18__card:hover {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — dual light/dark box-shadows extrude cards from a same-color background; :active and :checked swap them to inset so buttons physically sink. Radio inputs carry the selection state. */
```
