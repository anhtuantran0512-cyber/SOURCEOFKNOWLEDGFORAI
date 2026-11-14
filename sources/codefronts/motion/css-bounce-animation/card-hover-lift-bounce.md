---
source: "codefronts"
url: "https://codefronts.com/motion/css-bounce-animation/card-hover-lift-bounce/"
title: "Card Hover Lift Bounce"
section: "motion"
category: "css-bounce-animation"
category_name: "CSS Bounce Animations"
description: "A single pricing / feature card that lifts and bounces on hover — the elevation change with elastic settle makes the card feel physical and interactive."
has_js: "false"
---

Here's a working CSS Bounce Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Card Hover Lift Bounce
Source: https://codefronts.com/motion/css-bounce-animation/card-hover-lift-bounce/

A single pricing / feature card that lifts and bounces on hover — the elevation change with elastic settle makes the card feel physical and interactive. Editorial off-white surface with deep-charcoal ink and gold accent. Stripe / Linear / Vercel pricing table aesthetic — the pattern users search for when building comparison surfaces where hover should reward attention without shouting.
## HTML
```html
<div class="bn-07">
  <p class="bn-07__label">Hover the card</p>
  <article class="bn-07__card">
    <span class="bn-07__badge">Most popular</span>
    <h3>Pro</h3>
    <p class="bn-07__price"><strong>$29</strong><span>/month</span></p>
    <ul>
      <li>Unlimited projects</li>
      <li>Priority email support</li>
      <li>Advanced analytics</li>
    </ul>
    <button class="bn-07__cta" type="button">Upgrade to Pro</button>
  </article>
</div>
```
## CSS
```css
.bn-07 {
  --page-bg: #fafaf7;
  --card: #ffffff;
  --ink: #1c1917;
  --sub: #78716c;
  --gold: #b58840;
  --gold-dark: #916a2a;
  --line: #e7e5e0;
  --good: #059669;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 64px 32px;
  background: var(--page-bg);
  color: var(--ink);
}

.bn-07 *,
.bn-07 *::before,
.bn-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bn-07 ::selection {
  background: var(--gold);
  color: #fff;
}

.bn-07__label {
  font-size: .9rem;
  font-weight: 600;
  color: var(--sub);
  letter-spacing: .02em;
}

.bn-07__card {
  position: relative;
  width: min(280px,100%);
  padding: 28px 26px;
  border: 1px solid var(--gold);
  border-radius: 14px;
  background: var(--card);
  display: flex;
  flex-direction: column;
  gap: 14px;
  box-shadow: 0 8px 24px -8px rgba(181,136,64,.28);
  transition: transform .3s ease-out,box-shadow .3s ease-out;
  will-change: transform;
}

@media (hover: hover) {
  .bn-07__card:hover {
    animation: bn-07-lift .5s cubic-bezier(.34,1.56,.64,1) forwards;
    box-shadow: 0 30px 50px -12px rgba(28,25,23,.24);
  }

  @keyframes bn-07-lift {
    0% {
      transform: translateY(0);
    }

    30% {
      transform: translateY(-18px);
    }

    60% {
      transform: translateY(-8px);
    }

    100% {
      transform: translateY(-12px);
    }
  }
}

.bn-07__badge {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  padding: 5px 14px;
  border-radius: 999px;
  background: var(--gold);
  color: #fff;
  font-size: .68rem;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
  box-shadow: 0 6px 12px -2px rgba(181,136,64,.45);
}

.bn-07__card h3 {
  font-size: .8rem;
  font-weight: 800;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--sub);
}

.bn-07__price {
  display: flex;
  align-items: baseline;
  gap: 4px;
}

.bn-07__price strong {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: 2.4rem;
  font-weight: 800;
  letter-spacing: -.02em;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
}

.bn-07__price span {
  font-size: .85rem;
  color: var(--sub);
  font-weight: 500;
}

.bn-07__card ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.bn-07__card li {
  position: relative;
  padding-left: 22px;
  font-size: .88rem;
  color: var(--ink);
  line-height: 1.5;
}

.bn-07__card li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 6px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: rgba(5,150,105,.14);
}

.bn-07__card li::after {
  content: '';
  position: absolute;
  left: 4px;
  top: 9px;
  width: 6px;
  height: 3px;
  border: 2px solid var(--good);
  border-top: none;
  border-right: none;
  transform: rotate(-45deg);
}

.bn-07__cta {
  padding: 12px 18px;
  border: none;
  border-radius: 9px;
  background: var(--gold);
  color: #fff;
  font-family: inherit;
  font-size: .9rem;
  font-weight: 700;
  cursor: pointer;
  transition: background .18s ease;
}

.bn-07__cta:hover {
  background: var(--gold-dark);
}

.bn-07__cta:focus-visible {
  outline: 2px solid var(--gold);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .bn-07__card {
    animation: none!important;
    transition: background .18s ease;
  }

  @media (hover: hover) {
    .bn-07__card:hover {
      animation: none!important;
      transform: none!important;
      background: #f8f8f4;
    }
  }
}
```
