---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/minimalist-dark-mode-header-glow/"
title: "Minimalist Dark-Mode Header Glow"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "The restrained, high-end SaaS take on neon: no storefront flash, just a faint premium halo behind clean type so a dark-mode hero feels lit-from-within."
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Dark-Mode Header Glow
Source: https://codefronts.com/motion/css-neon-text-effect/minimalist-dark-mode-header-glow/

The restrained, high-end SaaS take on neon: no storefront flash, just a faint premium halo behind clean type so a dark-mode hero feels lit-from-within. What upmarket product designers search for instead of 'neon'.
## HTML
```html
<div class="cnt-08">
  <header class="cnt-08__hero">
    <p class="cnt-08__eyebrow">Introducing v3</p>
    <h2 class="cnt-08__h">Ship dark-mode UI that feels <span class="cnt-08__hi">lit from within</span></h2>
    <p class="cnt-08__lead">A premium halo — not a storefront. Faint, cool, and completely composited.</p>
  </header>
</div>
```
## CSS
```css
.cnt-08,
.cnt-08 *,
.cnt-08 *::before,
.cnt-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-08 ::selection {
  background: oklch(0.78 0.12 230);
  color: #04101a;
}

.cnt-08 {
  --halo: oklch(0.9 0.03 240);
  --accent: oklch(0.8 0.13 230);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: radial-gradient(60% 60% at 50% 38%,#141821,#0d1117 70%);
}

.cnt-08__hero {
  max-width: 640px;
  text-align: center;
}

.cnt-08__eyebrow {
  font: 12px ui-monospace,Menlo,monospace;
  letter-spacing: .32em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 20px;
  text-shadow: 0 0 12px color-mix(in oklch,var(--accent) 55%,transparent);
}

.cnt-08__h {
  font-size: clamp(30px,5.4vw,52px);
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: -.01em;
  color: #f2f5fa;
  text-wrap: balance;
  text-shadow: 0 0 1px rgba(255,255,255,.4),0 0 22px rgba(220,232,255,.14),0 0 60px color-mix(in oklch,var(--halo) 22%,transparent);
}

.cnt-08__hi {
  color: var(--accent);
  text-shadow: 0 0 8px color-mix(in oklch,var(--accent) 60%,transparent),0 0 28px color-mix(in oklch,var(--accent) 40%,transparent);
  border-bottom: 2px solid transparent;
  background: linear-gradient(90deg,transparent,var(--accent),transparent) bottom/100% 2px no-repeat;
}

.cnt-08__lead {
  margin-top: 20px;
  font-size: 16px;
  line-height: 1.6;
  color: #9aa4b4;
}

@media (prefers-reduced-motion: reduce) {
}
```

## JavaScript
```js
/* No JavaScript — a deliberately static, faint premium halo. */
```
