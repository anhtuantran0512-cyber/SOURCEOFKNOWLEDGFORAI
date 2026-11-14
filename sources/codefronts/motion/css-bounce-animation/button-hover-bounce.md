---
source: "codefronts"
url: "https://codefronts.com/motion/css-bounce-animation/button-hover-bounce/"
title: "Button Hover Bounce"
section: "motion"
category: "css-bounce-animation"
category_name: "CSS Bounce Animations"
description: "A primary CTA button with a hover-triggered bounce micro-interaction — the button lifts and settles with elastic overshoot when the pointer arrives, giving…"
has_js: "false"
---

Here's a working CSS Bounce Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Button Hover Bounce
Source: https://codefronts.com/motion/css-bounce-animation/button-hover-bounce/

A primary CTA button with a hover-triggered bounce micro-interaction — the button lifts and settles with elastic overshoot when the pointer arrives, giving it a physical, clickable feel. Warm orange (#f97316) e-commerce CTA color, satisfying tactile feedback the moment users hover. The interaction reads as "press me" without the intrusive infinite pulse of always-on CTAs.
## HTML
```html
<div class="bn-06">
  <p class="bn-06__label">Hover the button</p>
  <button class="bn-06__cta" type="button">
    <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <circle cx="9" cy="21" r="1"/>
      <circle cx="20" cy="21" r="1"/>
      <path d="M1 1h4l2.7 13.4a2 2 0 002 1.6h9.7a2 2 0 002-1.6L23 6H6"/>
    </svg>
    <span>Add to cart · $168</span>
  </button>
  <p class="bn-06__hint">The button lifts + squashes on hover, then settles.</p>
</div>
```
## CSS
```css
.bn-06 {
  --page-bg: #fef7ed;
  --ink: #3a2a1a;
  --sub: #8b7355;
  --brand: #f97316;
  --brand-dark: #ea580c;
  --brand-deep: #c2410c;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
  padding: 32px;
  background: radial-gradient(70% 60% at 20% 20%, rgba(249,115,22,.08) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
  text-align: center;
}

.bn-06 *,
.bn-06 *::before,
.bn-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bn-06 ::selection {
  background: var(--brand);
  color: #fff;
}

.bn-06__label {
  font-size: .9rem;
  font-weight: 600;
  color: var(--sub);
  letter-spacing: .02em;
}

.bn-06__cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 16px 34px;
  border: none;
  border-radius: 11px;
  background: var(--brand);
  color: #fff;
  font-family: inherit;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 12px 28px -8px rgba(249,115,22,.5);
  transition: background .18s ease,box-shadow .18s ease;
  will-change: transform;
}

.bn-06__cta:hover {
  background: var(--brand-dark);
  box-shadow: 0 16px 36px -8px rgba(249,115,22,.55);
}

.bn-06__cta:active {
  background: var(--brand-deep);
}

.bn-06__cta:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 4px;
}

@media (hover: hover) {
  .bn-06__cta:hover {
    animation: bn-06-hover .38s cubic-bezier(.34,1.56,.64,1) forwards;
  }

  @keyframes bn-06-hover {
    0% {
      transform: translateY(0) scale(1);
    }

    40% {
      transform: translateY(-6px) scaleY(.96) scaleX(1.04);
    }

    100% {
      transform: translateY(0) scale(1);
    }
  }
}

.bn-06__hint {
  font-size: .78rem;
  color: var(--sub);
  max-width: 320px;
  line-height: 1.5;
}

@media (prefers-reduced-motion: reduce) {
  .bn-06__cta {
    animation: none!important;
    transform: none!important;
  }

  @media (hover: hover) {
    .bn-06__cta:hover {
      animation: none!important;
    }
  }
}
```
