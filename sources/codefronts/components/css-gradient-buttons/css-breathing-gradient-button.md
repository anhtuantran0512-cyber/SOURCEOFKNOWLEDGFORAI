---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/css-breathing-gradient-button/"
title: "CSS Breathing Gradient Button"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A mindfulness-app CTA that breathes on a 5-second cycle — the pill gently inhales via a subtle transform:scale(1.045), its gradient slides across itself, and…"
has_js: "false"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Breathing Gradient Button
Source: https://codefronts.com/components/css-gradient-buttons/css-breathing-gradient-button/

A mindfulness-app CTA that breathes on a 5-second cycle — the pill gently inhales via a subtle transform:scale(1.045), its gradient slides across itself, and the ambient glow swells and settles. No shape morphing, no label fade, just a calm rhythm matching an app's meditative practice.
## HTML
```html
<div class="gb-03">
  <div class="gb-03__card">
    <p class="gb-03__kicker"><span class="gb-03__kicker-dot"></span> Slow product design</p>
    <h3 class="gb-03__title">Interfaces that breathe.</h3>
    <p class="gb-03__copy">Not every button needs to bark for attention. Some breathe with the user's attention span — inhale, pause, exhale. Ours does it on a five-second cycle when idle.</p>
    <button class="gb-03__btn" type="button">
      <span class="gb-03__lab">Start your practice</span>
    </button>
    <p class="gb-03__foot">Hover to hold the breath · pure <code>@keyframes</code> · GPU-only</p>
  </div>
</div>
```
## CSS
```css
.gb-03,
.gb-03 *,
.gb-03 *::before,
.gb-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-03 ::selection {
  background: #67e8f9;
  color: #0a1417;
}

.gb-03 {
  --bg: #f4f1ea;
  --panel: #ffffff;
  --line: rgba(41,54,66,.10);
  --c1: #5eead4;
  --c2: #7c6cff;
  --c3: #f0abfc;
  --ink: #1d2937;
  --mut: #5a6879;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background: radial-gradient(60% 80% at 20% 0%, rgba(94,234,212,.16) 0%, transparent 55%), radial-gradient(70% 90% at 100% 100%, rgba(240,171,252,.12) 0%, transparent 60%), var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
  color: var(--ink);
}

.gb-03__card {
  width: min(440px,100%);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 32px 32px 28px;
  box-shadow: 0 30px 60px -30px rgba(41,54,66,.22);
  text-align: center;
}

.gb-03__kicker {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #0d9488;
  margin-bottom: 14px;
}

.gb-03__kicker-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, #a7f3d0, #10b981);
  animation: gb-03-dot-pulse 4s ease-in-out infinite;
}

@keyframes gb-03-dot-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: .85;
  }

  50% {
    transform: scale(1.35);
    opacity: 1;
  }
}

.gb-03__title {
  font-family: Georgia,"Times New Roman",serif;
  font-size: 26px;
  font-weight: 800;
  letter-spacing: -.015em;
  line-height: 1.15;
  margin-bottom: 10px;
  color: var(--ink);
}

.gb-03__copy {
  font-size: 14px;
  line-height: 1.6;
  color: var(--mut);
  margin-bottom: 32px;
}

.gb-03__btn {
  --w: 280px;
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: var(--w);
  padding: 16px 26px;
  border: 0;
  border-radius: 999px;
  color: #fff;
  font-family: inherit;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .01em;
  cursor: pointer;
  background: linear-gradient(135deg, var(--c1) 0%, var(--c2) 55%, var(--c3) 100%);
  background-size: 200% 200%;
  white-space: nowrap;
  box-shadow: 0 14px 32px -12px rgba(124,108,255,.45);
  animation: gb-03-breathe 5s cubic-bezier(.45,0,.55,1) infinite;
  transform-origin: center;
  will-change: transform, background-position, filter;
}

.gb-03__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gb-03__btn:hover {
  animation-play-state: paused;
}

.gb-03__lab {
  position: relative;
}

@keyframes gb-03-breathe {
  0%,
    100% {
    transform: scale(1);
    background-position: 0% 50%;
    filter: hue-rotate(0deg) saturate(1);
    box-shadow: 0 14px 32px -12px rgba(124,108,255,.45);
  }

  50% {
    transform: scale(1.045);
    background-position: 100% 50%;
    filter: hue-rotate(30deg) saturate(1.08);
    box-shadow: 0 22px 44px -14px rgba(240,171,252,.5);
  }
}

.gb-03__foot {
  font-size: 11.5px;
  color: var(--mut);
  letter-spacing: .02em;
  margin-top: 24px;
}

.gb-03__foot code {
  font-family: "JetBrains Mono", ui-monospace, monospace;
  font-size: 10.5px;
  background: rgba(124,108,255,.10);
  color: #5b4dff;
  padding: 1px 6px;
  border-radius: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .gb-03__btn {
    animation: none;
    filter: none;
    transform: none;
  }

  .gb-03__kicker-dot {
    animation: none;
  }
}
```
