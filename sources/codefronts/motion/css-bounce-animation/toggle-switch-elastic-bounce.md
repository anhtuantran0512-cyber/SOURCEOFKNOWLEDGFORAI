---
source: "codefronts"
url: "https://codefronts.com/motion/css-bounce-animation/toggle-switch-elastic-bounce/"
title: "Toggle Switch Elastic Bounce"
section: "motion"
category: "css-bounce-animation"
category_name: "CSS Bounce Animations"
description: "A dark mode toggle switch with elastic bounce — the knob slides across and \"lands\" with a spring squash at the edge, mimicking a physical switch snapping…"
has_js: "false"
---

Here's a working CSS Bounce Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Toggle Switch Elastic Bounce
Source: https://codefronts.com/motion/css-bounce-animation/toggle-switch-elastic-bounce/

A dark mode toggle switch with elastic bounce — the knob slides across and "lands" with a spring squash at the edge, mimicking a physical switch snapping into position. iOS Settings / Figma toolbar / GitHub theme picker aesthetic. Pure CSS via <input type="checkbox"> + :checked — no JavaScript needed. The bounce reads as "switch has snapped, state is committed."
## HTML
```html
<div class="bn-10">
  <p class="bn-10__label">Click to toggle</p>
  <label class="bn-10__toggle">
    <input type="checkbox" class="bn-10__input" checked />
    <span class="bn-10__track" aria-hidden="true">
      <span class="bn-10__knob"></span>
    </span>
    <span class="bn-10__text">Dark mode</span>
  </label>
  <p class="bn-10__hint">The knob undershoots, then overshoots + squashes as it lands.</p>
</div>
```
## CSS
```css
.bn-10 {
  --page-bg: #0f172a;
  --surface: #1e293b;
  --ink: #f1f5f9;
  --sub: #94a3b8;
  --track-off: #334155;
  --track-on: #8b5cf6;
  --knob: #ffffff;
  --knob-shadow: rgba(139,92,246,.4);
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
  background: radial-gradient(60% 60% at 50% 50%, rgba(139,92,246,.14) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
  text-align: center;
}

.bn-10 *,
.bn-10 *::before,
.bn-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bn-10 ::selection {
  background: var(--track-on);
  color: #fff;
}

.bn-10__label {
  font-size: .9rem;
  font-weight: 600;
  color: var(--sub);
  letter-spacing: .02em;
}

.bn-10__toggle {
  display: inline-flex;
  align-items: center;
  gap: 14px;
  padding: 16px 28px;
  border-radius: 14px;
  background: var(--surface);
  cursor: pointer;
  box-shadow: 0 12px 32px -12px rgba(0,0,0,.4);
  min-height: 44px;
}

.bn-10__input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
  width: 0;
  height: 0;
}

.bn-10__track {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 32px;
  border-radius: 16px;
  background: var(--track-off);
  transition: background .38s cubic-bezier(.55,0,.45,1);
  flex-shrink: 0;
}

.bn-10__knob {
  position: absolute;
  top: 3px;
  left: 3px;
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: var(--knob);
  box-shadow: 0 4px 10px -2px rgba(0,0,0,.4),0 0 0 0 var(--knob-shadow);
  transition: transform .38s cubic-bezier(.68,-0.6,.32,1.6),box-shadow .38s ease;
  will-change: transform;
}

.bn-10__input:checked ~ .bn-10__track {
  background: var(--track-on);
}

.bn-10__input:checked ~ .bn-10__track .bn-10__knob {
  transform: translateX(28px);
  box-shadow: 0 4px 10px -2px rgba(0,0,0,.4),0 0 12px 2px var(--knob-shadow);
  animation: bn-10-squash .35s cubic-bezier(.34,1.56,.64,1);
}

@keyframes bn-10-squash {
  0% {
    transform: translateX(28px) scale(1);
  }

  60% {
    transform: translateX(28px) scaleX(1.15) scaleY(.85);
  }

  100% {
    transform: translateX(28px) scale(1);
  }
}

.bn-10__text {
  font-size: .95rem;
  font-weight: 700;
  letter-spacing: -.005em;
}

.bn-10__toggle:focus-within {
  outline: 2px solid var(--track-on);
  outline-offset: 4px;
}

.bn-10__hint {
  font-size: .78rem;
  color: var(--sub);
  max-width: 360px;
  line-height: 1.5;
}

@media (prefers-reduced-motion: reduce) {
  .bn-10__knob {
    transition: transform .25s cubic-bezier(.22,1,.36,1)!important;
    animation: none!important;
  }

  .bn-10__input:checked ~ .bn-10__track .bn-10__knob {
    animation: none!important;
  }
}
```
