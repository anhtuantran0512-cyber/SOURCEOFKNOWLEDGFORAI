---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/realistic-flickering-neon-sign/"
title: "Realistic Flickering Neon Sign"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "A weathered gas-discharge sign where one tube stutters and drops out of power on an irregular timeline — the 'broken vintage bulb' realism devs hunt for,…"
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Realistic Flickering Neon Sign
Source: https://codefronts.com/motion/css-neon-text-effect/realistic-flickering-neon-sign/

A weathered gas-discharge sign where one tube stutters and drops out of power on an irregular timeline — the 'broken vintage bulb' realism devs hunt for, achieved with a hand-tuned multi-step @keyframes, no JS.
## HTML
```html
<div class="cnt-06">
  <div class="cnt-06__wall">
    <h2 class="cnt-06__sign">
      <span class="cnt-06__steady">BAR</span>
      <span class="cnt-06__flick">OPEN</span>
    </h2>
  </div>
</div>
```
## CSS
```css
.cnt-06,
.cnt-06 *,
.cnt-06 *::before,
.cnt-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-06 ::selection {
  background: oklch(0.78 0.2 25);
  color: #fff;
}

.cnt-06 {
  --accent: oklch(0.78 0.21 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 20px;
  background: radial-gradient(90% 90% at 50% 40%,#171012,#080506);
}

.cnt-06__wall {
  position: relative;
  padding: 56px 60px;
  border-radius: 8px;
  background: repeating-linear-gradient(115deg,#0f0b0c 0 22px,#120d0e 22px 44px);
  box-shadow: inset 0 0 120px rgba(0,0,0,.7);
}

.cnt-06__sign {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  font-size: clamp(48px,11vw,104px);
  font-weight: 800;
  letter-spacing: .06em;
  line-height: 1;
  color: #fff;
}

.cnt-06__steady {
  color: var(--accent);
  text-shadow: 0 0 5px #fff,0 0 12px var(--accent),0 0 28px var(--accent),0 0 60px var(--accent);
}

.cnt-06__flick {
  color: var(--accent);
  animation: cnt-06-flicker 5.5s infinite;
}

@keyframes cnt-06-flicker {
  0%,
    100% {
    opacity: 1;
    text-shadow: 0 0 5px #fff,0 0 14px var(--accent),0 0 34px var(--accent),0 0 74px var(--accent);
  }

  2% {
    opacity: .25;
    text-shadow: 0 0 3px color-mix(in oklch,var(--accent) 40%,transparent);
  }

  4% {
    opacity: 1;
    text-shadow: 0 0 5px #fff,0 0 14px var(--accent),0 0 34px var(--accent);
  }

  8% {
    opacity: .3;
    text-shadow: none;
  }

  9% {
    opacity: 1;
    text-shadow: 0 0 5px #fff,0 0 14px var(--accent),0 0 34px var(--accent);
  }

  40% {
    opacity: 1;
  }

  41% {
    opacity: .2;
    text-shadow: none;
  }

  42.5% {
    opacity: 1;
    text-shadow: 0 0 5px #fff,0 0 14px var(--accent),0 0 34px var(--accent);
  }

  70%,
    72% {
    opacity: 1;
  }

  71% {
    opacity: .35;
    text-shadow: 0 0 4px color-mix(in oklch,var(--accent) 50%,transparent);
  }

  88% {
    opacity: 1;
  }

  89% {
    opacity: .28;
    text-shadow: none;
  }

  90% {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cnt-06__flick {
    animation: none;
    text-shadow: 0 0 5px #fff,0 0 14px var(--accent),0 0 34px var(--accent),0 0 74px var(--accent);
  }
}
```

## JavaScript
```js
/* No JavaScript — an intentionally irregular @keyframes fakes a failing tube. */
```
