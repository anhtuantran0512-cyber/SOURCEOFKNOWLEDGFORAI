---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/neon-glow-button-hover-effect/"
title: "Neon Glow Button Hover Effect"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "A flat, resting outline button that ignites into a saturated neon tube the exact moment the cursor arrives — the single most-searched neon CTA pattern in…"
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Glow Button Hover Effect
Source: https://codefronts.com/motion/css-neon-text-effect/neon-glow-button-hover-effect/

A flat, resting outline button that ignites into a saturated neon tube the exact moment the cursor arrives — the single most-searched neon CTA pattern in Tier-1 markets. One transition, no images, no JS.
## HTML
```html
<div class="cnt-01">
  <a class="cnt-01__btn" href="#" role="button">
    <span class="cnt-01__label">Get Early Access</span>
  </a>
  <p class="cnt-01__hint">hover / focus the button</p>
</div>
```
## CSS
```css
.cnt-01,
.cnt-01 *,
.cnt-01 *::before,
.cnt-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-01 ::selection {
  background: oklch(0.9 0.2 195);
  color: #04100f;
}

.cnt-01 {
  --accent: oklch(0.86 0.16 195);
  --glow: 34px;
  --spread: 2px;
  --dur: .4s;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 26px;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: radial-gradient(120% 120% at 50% 20%,#0c0f10,#050505);
}

.cnt-01__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 20px 46px;
  border-radius: 999px;
  text-decoration: none;
  font-size: 19px;
  font-weight: 600;
  letter-spacing: .02em;
  color: var(--accent);
  border: 1.5px solid color-mix(in oklch,var(--accent) 70%,transparent);
  background: color-mix(in oklch,var(--accent) 5%,#060809);
  box-shadow: 0 0 0 0 transparent;
  transition: color var(--dur),background var(--dur),border-color var(--dur),box-shadow var(--dur),text-shadow var(--dur);
}

.cnt-01__btn::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(115deg,transparent 20%,color-mix(in oklch,var(--accent) 55%,white) 50%,transparent 80%);
  transform: translateX(-130%);
  transition: transform .55s ease;
}

.cnt-01__btn:hover,
.cnt-01__btn:focus-visible {
  outline: none;
  color: #eafffd;
  border-color: var(--accent);
  background: color-mix(in oklch,var(--accent) 78%,#040807);
  text-shadow: 0 0 10px color-mix(in oklch,var(--accent) 80%,white);
  box-shadow: inset 0 0 12px color-mix(in oklch,var(--accent) 60%,white), inset 0 0 2px #fff, 0 0 var(--spread) var(--accent), 0 0 var(--glow) color-mix(in oklch,var(--accent) 85%,transparent), 0 0 calc(var(--glow) * 2.4) color-mix(in oklch,var(--accent) 45%,transparent);
}

.cnt-01__btn:hover::before,
.cnt-01__btn:focus-visible::before {
  transform: translateX(130%);
}

.cnt-01__btn:active {
  transform: translateY(1px) scale(.99);
}

.cnt-01__hint {
  font: 12px ui-monospace,Menlo,monospace;
  letter-spacing: .26em;
  text-transform: uppercase;
  color: color-mix(in oklch,var(--accent) 45%,#5a6b6a);
}

@media (prefers-reduced-motion: reduce) {
  .cnt-01__btn,
    .cnt-01__btn::before {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the ignite is a pure :hover / :focus-visible transition. */
```
