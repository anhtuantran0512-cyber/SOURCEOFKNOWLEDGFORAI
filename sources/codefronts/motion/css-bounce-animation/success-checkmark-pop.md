---
source: "codefronts"
url: "https://codefronts.com/motion/css-bounce-animation/success-checkmark-pop/"
title: "Success Checkmark Pop"
section: "motion"
category: "css-bounce-animation"
category_name: "CSS Bounce Animations"
description: "A payment / form-submit success confirmation — mint circle scales up with elastic overshoot, then the checkmark draws in via stroke-dashoffset."
has_js: "false"
---

Here's a working CSS Bounce Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Success Checkmark Pop
Source: https://codefronts.com/motion/css-bounce-animation/success-checkmark-pop/

A payment / form-submit success confirmation — mint circle scales up with elastic overshoot, then the checkmark draws in via stroke-dashoffset. Stripe checkout / Apple Pay / Shopify payment success aesthetic (mint #d1fae5 success surface + emerald #065f46 check). The bounce reads as "you're good." The classic two-stage cascade — circle pops, then check draws — that every well-designed confirmation UI uses.
## HTML
```html
<div class="bn-03" role="status" aria-live="polite">
  <span class="bn-03__circle" aria-hidden="true">
    <svg viewBox="0 0 52 52" width="72" height="72" aria-hidden="true">
      <path class="bn-03__check-path" d="M14 27 l8 8 l16 -18" fill="none" stroke="currentColor" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </span>
  <p class="bn-03__label">Payment received</p>
</div>
```
## CSS
```css
.bn-03 {
  --page-bg: #f0fdf4;
  --ink: #052e1a;
  --sub: #4b6b58;
  --mint: #d1fae5;
  --emerald: #065f46;
  --emerald-soft: rgba(6,95,70,.24);
  font-family: -apple-system,BlinkMacSystemFont,'SF Pro Rounded','Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 32px;
  background: radial-gradient(60% 60% at 50% 50%, rgba(16,185,129,.12) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
  text-align: center;
}

.bn-03 *,
.bn-03 *::before,
.bn-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bn-03 ::selection {
  background: var(--emerald);
  color: #fff;
}

.bn-03__circle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background: var(--mint);
  color: var(--emerald);
  transform: scale(0);
  animation: bn-03-pop .5s cubic-bezier(.34,1.56,.64,1) forwards;
  box-shadow: 0 20px 40px -10px var(--emerald-soft);
}

@keyframes bn-03-pop {
  0% {
    transform: scale(0);
  }

  40% {
    transform: scale(1.15);
  }

  70% {
    transform: scale(.95);
  }

  100% {
    transform: scale(1);
  }
}

.bn-03__check-path {
  stroke-dasharray: 44;
  stroke-dashoffset: 44;
  animation: bn-03-draw .4s cubic-bezier(.65,0,.35,1) .3s forwards;
}

@keyframes bn-03-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.bn-03__label {
  font-size: 1.1rem;
  font-weight: 800;
  letter-spacing: -.01em;
  color: var(--ink);
  opacity: 0;
  animation: bn-03-fade .3s ease-out .55s forwards;
}

@keyframes bn-03-fade {
  from {
    opacity: 0;
    transform: translateY(6px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bn-03__circle,
    .bn-03__check-path,
    .bn-03__label {
    animation: none!important;
  }

  .bn-03__circle {
    transform: scale(1)!important;
  }

  .bn-03__check-path {
    stroke-dashoffset: 0!important;
  }

  .bn-03__label {
    opacity: 1!important;
    transform: none!important;
  }
}
```
