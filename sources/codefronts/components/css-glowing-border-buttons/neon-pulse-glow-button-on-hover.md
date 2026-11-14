---
source: "codefronts"
url: "https://codefronts.com/components/css-glowing-border-buttons/neon-pulse-glow-button-on-hover/"
title: "Neon Pulse Glow Button on Hover"
section: "components"
category: "css-glowing-border-buttons"
category_name: "CSS Glowing Border Buttons"
description: "The esports lobby classic: a cyan sign-tube button that snaps to full neon on hover — four stacked box-shadow layers, a matching text-shadow, and a heartbeat…"
has_js: "false"
---

Here's a working CSS Glowing Border Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Pulse Glow Button on Hover
Source: https://codefronts.com/components/css-glowing-border-buttons/neon-pulse-glow-button-on-hover/

The esports lobby classic: a cyan sign-tube button that snaps to full neon on hover — four stacked box-shadow layers, a matching text-shadow, and a heartbeat pulse that keeps throbbing while the cursor stays. Reads exactly like a bent-glass sign because the shadow layers mimic how real neon light falls off.
## HTML
```html
<section class="gbb-02" aria-label="Neon pulse glow button demo">
  <button class="gbb-02__btn" type="button">Enter the Arena</button>
</section>
```
## CSS
```css
.gbb-02,
.gbb-02 *,
.gbb-02 *::before,
.gbb-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gbb-02 {
  --neon: oklch(0.85 0.15 195);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(60% 80% at 50% 100%,oklch(0.2 0.05 220 / .7),transparent 60%),oklch(0.12 0.02 250);
}

.gbb-02 .gbb-02__btn {
  cursor: pointer;
  padding: 15px 36px;
  border-radius: 12px;
  border: 2px solid var(--neon);
  background: color-mix(in oklab,var(--neon) 6%,transparent);
  font: 700 15px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #eafcff;
  text-shadow: 0 0 8px color-mix(in oklab,var(--neon) 70%,transparent);
  box-shadow: 0 0 6px color-mix(in oklab,var(--neon) 35%,transparent),0 0 18px color-mix(in oklab,var(--neon) 18%,transparent),inset 0 0 10px color-mix(in oklab,var(--neon) 12%,transparent);
  transition: box-shadow .2s ease,text-shadow .2s ease,background .2s ease;
}

.gbb-02 .gbb-02__btn:hover,
.gbb-02 .gbb-02__btn:focus-visible {
  background: color-mix(in oklab,var(--neon) 12%,transparent);
  text-shadow: 0 0 6px var(--neon),0 0 20px color-mix(in oklab,var(--neon) 80%,transparent);
  animation: gbb02-pulse 1.6s ease-in-out .2s infinite;
  box-shadow: 0 0 6px var(--neon),0 0 22px color-mix(in oklab,var(--neon) 60%,transparent),0 0 48px color-mix(in oklab,var(--neon) 35%,transparent),inset 0 0 16px color-mix(in oklab,var(--neon) 20%,transparent);
}

.gbb-02 .gbb-02__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

.gbb-02 .gbb-02__btn:active {
  transform: scale(.97);
}

@keyframes gbb02-pulse {
  0%,
    100% {
    box-shadow: 0 0 6px var(--neon),0 0 22px color-mix(in oklab,var(--neon) 60%,transparent),0 0 48px color-mix(in oklab,var(--neon) 35%,transparent),inset 0 0 16px color-mix(in oklab,var(--neon) 20%,transparent);
  }

  50% {
    box-shadow: 0 0 8px var(--neon),0 0 32px color-mix(in oklab,var(--neon) 75%,transparent),0 0 72px color-mix(in oklab,var(--neon) 50%,transparent),inset 0 0 22px color-mix(in oklab,var(--neon) 28%,transparent);
  }
}

@media (prefers-reduced-motion: reduce) {
  .gbb-02 .gbb-02__btn:hover,
    .gbb-02 .gbb-02__btn:focus-visible {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — layered box-shadow + text-shadow mimic neon falloff; an infinite keyframe pulses only the outer halo layers on hover. */
```
