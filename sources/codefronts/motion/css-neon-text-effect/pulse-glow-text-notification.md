---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/pulse-glow-text-notification/"
title: "Pulse-Glow Text Notification"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "A subtle, breathing neon status line for dashboards and admin panels — the kind of 'something needs your attention' pulse that reads as alive without shouting."
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pulse-Glow Text Notification
Source: https://codefronts.com/motion/css-neon-text-effect/pulse-glow-text-notification/

A subtle, breathing neon status line for dashboards and admin panels — the kind of 'something needs your attention' pulse that reads as alive without shouting. A soft dot and label inhale and exhale their glow together.
## HTML
```html
<div class="cnt-04">
  <div class="cnt-04__row">
    <span class="cnt-04__dot" aria-hidden="true"></span>
    <span class="cnt-04__msg"><strong>3 deployments</strong> awaiting review</span>
  </div>
</div>
```
## CSS
```css
.cnt-04,
.cnt-04 *,
.cnt-04 *::before,
.cnt-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-04 ::selection {
  background: oklch(0.86 0.19 150);
  color: #03140b;
}

.cnt-04 {
  --accent: oklch(0.86 0.2 150);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: radial-gradient(120% 120% at 50% 30%,#0b100d,#050705);
}

.cnt-04__row {
  display: inline-flex;
  align-items: center;
  gap: 14px;
  padding: 16px 24px;
  border-radius: 12px;
  background: #0a0d0b;
  border: 1px solid #182018;
  box-shadow: 0 30px 60px -40px #000;
}

.cnt-04__dot {
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: var(--accent);
  animation: cnt-04-breathe 2.4s ease-in-out infinite;
}

.cnt-04__msg {
  font-size: 16px;
  letter-spacing: .01em;
  color: var(--accent);
  animation: cnt-04-breathe 2.4s ease-in-out infinite;
}

.cnt-04__msg strong {
  color: #eafff2;
  font-weight: 700;
}

@keyframes cnt-04-breathe {
  0%,
    100% {
    opacity: .72;
    text-shadow: 0 0 4px color-mix(in oklch,var(--accent) 55%,transparent);
    box-shadow: 0 0 4px color-mix(in oklch,var(--accent) 50%,transparent);
  }

  50% {
    opacity: 1;
    text-shadow: 0 0 8px var(--accent),0 0 20px var(--accent),0 0 40px color-mix(in oklch,var(--accent) 60%,transparent);
    box-shadow: 0 0 10px var(--accent),0 0 22px color-mix(in oklch,var(--accent) 60%,transparent);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cnt-04__dot,
    .cnt-04__msg {
    animation: none;
    text-shadow: 0 0 10px var(--accent);
    opacity: 1;
  }
}
```

## JavaScript
```js
/* No JavaScript — one eased @keyframes 'breathe' shared by dot and label. */
```
