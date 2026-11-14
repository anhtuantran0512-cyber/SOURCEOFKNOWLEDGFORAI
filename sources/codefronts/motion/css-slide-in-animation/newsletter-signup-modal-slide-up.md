---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/newsletter-signup-modal-slide-up/"
title: "Newsletter Signup Modal Slide-Up"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "A Substack-style newsletter signup modal that slides up from below with a semi-transparent backdrop, showing a clean form with email input, subscribe CTA,…"
has_js: "false"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Newsletter Signup Modal Slide-Up
Source: https://codefronts.com/motion/css-slide-in-animation/newsletter-signup-modal-slide-up/

A Substack-style newsletter signup modal that slides up from below with a semi-transparent backdrop, showing a clean form with email input, subscribe CTA, subscriber count, and "unsubscribe anytime" trust signal — the pattern used by Substack, Beehiiv, Ghost, and modern creator newsletters.
## HTML
```html
<div class="sl-16">
  <div class="sl-16__backdrop"></div>
  <div class="sl-16__modal" role="dialog" aria-modal="true" aria-labelledby="sl-16-title">
    <div class="sl-16__badge">
      <span class="sl-16__dot"></span>
      12,847 subscribers · Free weekly
    </div>
    <h2 class="sl-16__title" id="sl-16-title">Join the CSS newsletter</h2>
    <p class="sl-16__copy">Every Tuesday: one new CSS technique with a working demo. Real code, real use cases, zero fluff. Written by an engineer, for engineers.</p>
    <form class="sl-16__form">
      <input type="email" placeholder="[email protected]" readonly value="[email protected]">
      <button type="button" class="sl-16__cta">Subscribe</button>
    </form>
    <ul class="sl-16__trust">
      <li>✓ Free forever</li>
      <li>✓ Weekly · 1 email</li>
      <li>✓ Unsubscribe anytime</li>
    </ul>
  </div>
</div>
```
## CSS
```css
.sl-16 {
  --bg: #0a0e1c;
  --card: #fefefe;
  --accent: #7c3aed;
  --ink: #0a0a14;
  --sub: #5b5b6b;
  --good: #22c55e;
  --line: #e5e5eb;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: var(--bg);
  color: var(--ink);
  overflow: hidden;
}

.sl-16 *,
.sl-16 *::before,
.sl-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-16 ::selection {
  background: var(--accent);
  color: #fff;
}

.sl-16__backdrop {
  position: absolute;
  inset: 0;
  background: rgba(5,8,20,.72);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  opacity: 0;
  animation: sl-16-fade .3s ease-out forwards;
}

.sl-16__modal {
  position: relative;
  z-index: 1;
  width: min(460px,100%);
  padding: 32px 30px 28px;
  background: var(--card);
  border-radius: 16px;
  box-shadow: 0 40px 60px -20px rgba(0,0,0,.5);
  opacity: 0;
  transform: translateY(50px) scale(.96);
  animation: sl-16-modal .5s cubic-bezier(.16,1,.3,1) .1s forwards;
  text-align: center;
}

.sl-16__badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 5px 12px;
  border-radius: 999px;
  background: rgba(124,58,237,.08);
  font-size: .74rem;
  font-weight: 600;
  color: var(--accent);
  margin-bottom: 20px;
}

.sl-16__dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--good);
  box-shadow: 0 0 8px rgba(34,197,94,.6);
  animation: sl-16-pulse 2s ease-in-out infinite;
}

.sl-16__title {
  font-size: 1.6rem;
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.15;
  margin-bottom: 12px;
}

.sl-16__copy {
  font-size: .95rem;
  color: var(--sub);
  line-height: 1.55;
  margin-bottom: 24px;
}

.sl-16__form {
  display: flex;
  gap: 8px;
  margin-bottom: 16px;
}

.sl-16__form input {
  flex: 1;
  min-width: 0;
  padding: 12px 14px;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: #f8f8fa;
  color: var(--ink);
  font-family: inherit;
  font-size: .9rem;
}

.sl-16__form input:focus {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
  border-color: transparent;
}

.sl-16__cta {
  padding: 12px 22px;
  border: none;
  border-radius: 9px;
  background: var(--accent);
  color: #fff;
  font-family: inherit;
  font-size: .9rem;
  font-weight: 700;
  cursor: pointer;
  transition: background .18s ease,transform .12s ease;
  white-space: nowrap;
}

.sl-16__cta:hover {
  background: #6d28d9;
  transform: translateY(-1px);
}

.sl-16__trust {
  list-style: none;
  display: flex;
  justify-content: center;
  gap: 14px;
  flex-wrap: wrap;
  padding-top: 16px;
  border-top: 1px solid var(--line);
}

.sl-16__trust li {
  font-size: .72rem;
  color: var(--sub);
  font-weight: 500;
}

@keyframes sl-16-fade {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

@keyframes sl-16-modal {
  from {
    opacity: 0;
    transform: translateY(50px) scale(.96);
  }

  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@keyframes sl-16-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: .9;
  }

  50% {
    transform: scale(1.4);
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sl-16__backdrop,
    .sl-16__modal,
    .sl-16__dot {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}
```
