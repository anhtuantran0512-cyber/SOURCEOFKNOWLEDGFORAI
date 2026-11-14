---
source: "codefronts"
url: "https://codefronts.com/motion/css-bounce-animation/floating-hovering-element/"
title: "Floating Hovering Element"
section: "motion"
category: "css-bounce-animation"
category_name: "CSS Bounce Animations"
description: "A soft, weightless bounce that loops indefinitely to make an illustration, badge, or icon look like it's floating in mid-air."
has_js: "false"
---

Here's a working CSS Bounce Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Hovering Element
Source: https://codefronts.com/motion/css-bounce-animation/floating-hovering-element/

A soft, weightless bounce that loops indefinitely to make an illustration, badge, or icon look like it's floating in mid-air. Sky-blue soft pastel palette with a rounded card element that gently rises and falls in an infinite ease-in-out cycle. Perfect for hero illustrations, achievement badges, mascots, or any element that needs to feel "alive" without demanding attention. Uses alternate iteration so the up-and-down motion never resets — smooth continuous drift.
## HTML
```html
<div class="bn-12">
  <p class="bn-12__label">Weightless float loop</p>
  <div class="bn-12__badge" aria-hidden="true">
    <svg viewBox="0 0 24 24" width="44" height="44" fill="currentColor" aria-hidden="true">
      <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
    </svg>
  </div>
  <p class="bn-12__hint">The badge rises and falls infinitely with <code>alternate</code> iteration.</p>
</div>
```
## CSS
```css
.bn-12 {
  --page-bg: #e0f2fe;
  --surface: #ffffff;
  --ink: #075985;
  --sub: #0369a1;
  --accent: #0ea5e9;
  --accent-hi: #38bdf8;
  --shadow: rgba(2,132,199,.35);
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 32px;
  background: radial-gradient(60% 60% at 50% 40%, rgba(14,165,233,.18) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
  text-align: center;
}

.bn-12 *,
.bn-12 *::before,
.bn-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bn-12 ::selection {
  background: var(--accent);
  color: #fff;
}

.bn-12__label {
  font-size: .9rem;
  font-weight: 600;
  color: var(--sub);
  letter-spacing: .02em;
}

.bn-12__badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 120px;
  height: 120px;
  border-radius: 32px;
  background: linear-gradient(135deg,var(--accent-hi),var(--accent));
  color: #fff;
  box-shadow: 0 20px 40px -12px var(--shadow);
  animation: bn-12-float 2.4s ease-in-out infinite alternate, bn-12-shadow 2.4s ease-in-out infinite alternate;
  will-change: transform;
}

@keyframes bn-12-float {
  0% {
    transform: translateY(0);
  }

  100% {
    transform: translateY(-16px);
  }
}

@keyframes bn-12-shadow {
  0% {
    box-shadow: 0 20px 40px -12px var(--shadow);
  }

  100% {
    box-shadow: 0 32px 52px -14px var(--shadow);
  }
}

.bn-12__hint {
  font-size: .78rem;
  color: var(--sub);
  max-width: 360px;
  line-height: 1.5;
  opacity: .85;
}

.bn-12__hint code {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .72rem;
  padding: 1px 5px;
  border-radius: 4px;
  background: rgba(14,165,233,.14);
  color: var(--sub);
}

@media (prefers-reduced-motion: reduce) {
  .bn-12__badge {
    animation: none!important;
    transform: none!important;
  }
}
```
