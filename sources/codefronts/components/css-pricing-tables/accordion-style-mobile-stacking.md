---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/accordion-style-mobile-stacking/"
title: "Accordion-Style Mobile Stacking"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "One component, two personalities: on desktop it's a straight 3-column comparison; squeeze it into a narrow container and each plan collapses into a tappable…"
has_js: "false"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accordion-Style Mobile Stacking
Source: https://codefronts.com/components/css-pricing-tables/accordion-style-mobile-stacking/

One component, two personalities: on desktop it's a straight 3-column comparison; squeeze it into a narrow container and each plan collapses into a tappable accordion with only the essentials visible — powered by container queries, so it adapts to its container, not the viewport.
## HTML
```html
<section class="prc-20" aria-label="Responsive pricing that stacks into accordions">
  <div class="prc-20__container">
    <div class="prc-20__grid">
      <article class="prc-20__card">
        <input type="checkbox" id="prc-20-a" class="prc-20__sr">
        <label for="prc-20-a" class="prc-20__head"><h3>Solo</h3><svg class="prc-20__chev" width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M2 5l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></label>
        <p class="prc-20__price">$9<small>/mo</small></p>
        <div class="prc-20__fold"><ul class="prc-20__feat"><li>1 user</li><li>5 GB storage</li><li>Email support</li><li>Mobile app</li></ul></div>
        <a href="#" class="prc-20__cta">Choose Solo</a>
      </article>
      <article class="prc-20__card prc-20__card--hot">
        <input type="checkbox" id="prc-20-b" class="prc-20__sr" checked>
        <label for="prc-20-b" class="prc-20__head"><h3>Team</h3><svg class="prc-20__chev" width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M2 5l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></label>
        <p class="prc-20__price">$29<small>/mo</small></p>
        <div class="prc-20__fold"><ul class="prc-20__feat"><li>10 users</li><li>500 GB storage</li><li>Priority support</li><li>Admin console</li><li>Guest access</li></ul></div>
        <a href="#" class="prc-20__cta prc-20__cta--hot">Choose Team</a>
      </article>
      <article class="prc-20__card">
        <input type="checkbox" id="prc-20-c" class="prc-20__sr">
        <label for="prc-20-c" class="prc-20__head"><h3>Org</h3><svg class="prc-20__chev" width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M2 5l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></label>
        <p class="prc-20__price">$79<small>/mo</small></p>
        <div class="prc-20__fold"><ul class="prc-20__feat"><li>Unlimited users</li><li>Unlimited storage</li><li>SSO / SCIM</li><li>Audit log</li><li>99.9% SLA</li></ul></div>
        <a href="#" class="prc-20__cta">Choose Org</a>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.prc-20,
.prc-20 *,
.prc-20 *::before,
.prc-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-20 {
  --accent: oklch(0.6 0.17 175);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f2f6f5;
  color: #152220;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
}

.prc-20__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.prc-20__container {
  container-type: inline-size;
  width: min(900px,100%);
}

.prc-20__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 18px;
}

.prc-20__card {
  background: #fff;
  border: 1.5px solid #dde8e5;
  border-radius: 18px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.prc-20__card--hot {
  border-color: var(--accent);
}

.prc-20__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.prc-20__head h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #5c706c;
}

.prc-20__chev {
  display: none;
  color: #5c706c;
  transition: transform .3s;
}

.prc-20__price {
  font-size: 38px;
  font-weight: 800;
  letter-spacing: -.03em;
}

.prc-20__price small {
  font-size: 14px;
  font-weight: 600;
  color: #7d908c;
}

.prc-20__fold {
  display: grid;
  grid-template-rows: 1fr;
  transition: grid-template-rows .4s cubic-bezier(.6,0,.2,1);
}

.prc-20__feat {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 13.5px;
  color: #3e524e;
  overflow: hidden;
  min-height: 0;
}

.prc-20__feat li::before {
  content: "✓";
  color: var(--accent);
  font-weight: 700;
  margin-right: 8px;
}

.prc-20__cta {
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  font-size: 13.5px;
  padding: 12px;
  border-radius: 11px;
  border: 1.5px solid #dde8e5;
  color: #152220;
  transition: border-color .2s;
  margin-top: auto;
}

.prc-20__cta:hover {
  border-color: var(--accent);
}

.prc-20__cta--hot {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}

.prc-20__cta:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@container (max-width: 640px) {
  .prc-20__grid {
    grid-template-columns: 1fr;
    gap: 12px;
  }

  .prc-20__head {
    cursor: pointer;
  }

  .prc-20__chev {
    display: block;
  }

  .prc-20__card:has(.prc-20__sr:checked) .prc-20__chev {
    transform: rotate(180deg);
  }

  .prc-20__fold {
    grid-template-rows: 0fr;
  }

  .prc-20__card:has(.prc-20__sr:checked) .prc-20__fold {
    grid-template-rows: 1fr;
  }

  .prc-20__feat {
    margin-bottom: 0;
  }

  .prc-20__card:has(.prc-20__sr:focus-visible) {
    outline: 3px solid var(--accent);
    outline-offset: 2px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .prc-20__fold,
    .prc-20__chev {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — a container query flips the grid from 3 columns to stacked accordions below 640px of container width; checkbox + :has() folds each feature list via grid-template-rows 0fr→1fr. Price and CTA stay outside the fold, always visible. */
```
