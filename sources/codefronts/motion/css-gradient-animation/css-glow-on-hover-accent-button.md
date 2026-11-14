---
source: "codefronts"
url: "https://codefronts.com/motion/css-gradient-animation/css-glow-on-hover-accent-button/"
title: "CSS Glow on Hover Accent Button"
section: "motion"
category: "css-gradient-animation"
category_name: "CSS Gradient Animations"
description: "Three button variants — gradient-fill shift, gradient border glow, and flood fill — where the colour palette activates and shifts only on hover, using…"
has_js: "false"
---

Here's a working CSS Gradient Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glow on Hover Accent Button
Source: https://codefronts.com/motion/css-gradient-animation/css-glow-on-hover-accent-button/

Three button variants — gradient-fill shift, gradient border glow, and flood fill — where the colour palette activates and shifts only on hover, using pseudo-elements and CSS transitions for zero-JS interactivity.
## HTML
```html
<div class="ga-05">
  <div class="ga-05__row">
    <span class="ga-05__label">Gradient Fill Shift</span>
    <button class="ga-05__btn ga-05__btn--filled">Get Started Free ↗</button>
    <button class="ga-05__btn ga-05__btn--filled" style="--c1:#059669;--c2:#0ea5e9;--c3:#7c3aed;">Deploy Now</button>
    <button class="ga-05__btn ga-05__btn--filled" style="--c1:#db2777;--c2:#f59e0b;--c3:#ef4444;">Go Premium</button>
  </div>
  <div class="ga-05__row">
    <span class="ga-05__label">Gradient Border Glow</span>
    <button class="ga-05__btn ga-05__btn--ghost">Connect Wallet</button>
    <button class="ga-05__btn ga-05__btn--ghost" style="--c1:#0ea5e9;--c2:#6366f1;--c3:#a855f7;">View Docs</button>
  </div>
  <div class="ga-05__row">
    <span class="ga-05__label">Flood Fill on Hover</span>
    <button class="ga-05__btn ga-05__btn--flood">Subscribe</button>
    <button class="ga-05__btn ga-05__btn--flood" style="--c1:#d946ef;--c2:#f43f5e;">Join Waitlist</button>
    <button class="ga-05__btn ga-05__btn--flood" style="--c1:#0891b2;--c2:#0d9488;">Learn More</button>
  </div>
</div>
```
## CSS
```css
.ga-05,
.ga-05 *,
.ga-05 *::before,
.ga-05 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ga-05 ::selection {
  background: rgba(139,92,246,.4);
  color: #fff;
}

.ga-05 {
  --c1: #7c3aed;
  --c2: #06b6d4;
  --c3: #ec4899;
  --bg: #0d0d18;
  --dur: .5s;
  width: 100%;
  min-height: 100vh;
  background: var(--bg);
  font-family: system-ui, -apple-system, sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 48px;
  padding: 48px 24px;
}
/* ── Variant A: gradient background shifts on hover ── */

.ga-05__btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 14px 32px;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: .01em;
  overflow: hidden;
  transition: transform var(--dur) ease, box-shadow var(--dur) ease;
  z-index: 0;
}
/* Shared gradient layer that slides in */

.ga-05__btn::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: linear-gradient(135deg, var(--c1), var(--c2), var(--c3));
  background-size: 200% 200%;
  background-position: 0% 50%;
  transition: background-position .6s ease, opacity var(--dur) ease;
  z-index: -1;
}
/* Glow halo */

.ga-05__btn::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: 14px;
  background: linear-gradient(135deg, var(--c1), var(--c2), var(--c3));
  background-size: 200% 200%;
  background-position: 0% 50%;
  filter: blur(16px);
  opacity: 0;
  transition: opacity var(--dur) ease, background-position .6s ease;
  z-index: -2;
}

.ga-05__btn:hover::before {
  background-position: 100% 50%;
}

.ga-05__btn:hover::after {
  opacity: .65;
  background-position: 100% 50%;
}

.ga-05__btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(124,58,237,.3);
}

.ga-05__btn:active {
  transform: translateY(0);
}
/* Variant A — filled */

.ga-05__btn--filled {
  background: linear-gradient(135deg, var(--c1), var(--c1));
  color: #fff;
}

.ga-05__btn--filled::before {
  opacity: 0;
}

.ga-05__btn--filled:hover::before {
  opacity: 1;
}
/* Variant B — ghost with gradient border */

.ga-05__btn--ghost {
  background: transparent;
  color: #fff;
  padding: 13px 31px;
  /* 1px less to account for border */
}

.ga-05__btn--ghost::before {
  /* Gradient border trick: wrapper with gradient bg, inner mask */
  background: linear-gradient(var(--bg), var(--bg)) padding-box, linear-gradient(135deg, rgba(124,58,237,.35), rgba(6,182,212,.35)) border-box;
  border: 1px solid transparent;
  opacity: 1;
  transition: background var(--dur) ease;
}

.ga-05__btn--ghost:hover::before {
  background: linear-gradient(var(--bg), var(--bg)) padding-box, linear-gradient(135deg, var(--c1), var(--c2), var(--c3)) border-box;
}

.ga-05__btn--ghost:hover {
  box-shadow: 0 0 0 3px rgba(124,58,237,.15);
}
/* Variant C — outline that floods with gradient fill */

.ga-05__btn--flood {
  background: transparent;
  color: #fff;
  border: 1.5px solid rgba(255,255,255,.15);
  overflow: hidden;
}

.ga-05__btn--flood::before {
  opacity: 0;
  background: linear-gradient(135deg, var(--c1), var(--c2));
  background-size: 100% 100%;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .4s cubic-bezier(.22,1,.36,1), opacity .1s;
}

.ga-05__btn--flood:hover::before {
  opacity: 1;
  transform: scaleX(1);
}

.ga-05__btn--flood:hover {
  border-color: transparent;
}
/* Row layout */

.ga-05__row {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  align-items: center;
  justify-content: center;
}

.ga-05__label {
  font-size: .7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .1em;
  color: rgba(255,255,255,.3);
  text-align: center;
  margin-bottom: -32px;
  width: 100%;
}

@media (prefers-reduced-motion: reduce) {
  .ga-05__btn,
    .ga-05__btn::before,
    .ga-05__btn::after {
    transition: none;
    animation: none;
  }
}
```
