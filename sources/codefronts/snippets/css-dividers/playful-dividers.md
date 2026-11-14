---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/playful-dividers/"
title: "Bouncing Animated Dots Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "Three dots that bounce between two rules — the smallest possible piece of motion design, and a masterclass in stagger."
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bouncing Animated Dots Divider CSS
Source: https://codefronts.com/snippets/css-dividers/playful-dividers/

Three dots that bounce between two rules — the smallest possible piece of motion design, and a masterclass in stagger. The delays are negative, not positive, so every dot is already mid-cycle on the first frame instead of the row standing still for half a second. Includes the physically-correct easing pair that makes a bounce read as gravity rather than as a sine wave.
## HTML
```html
<section class="div-22" aria-label="Bouncing animated dots divider demo">
  <div class="div-22__stage">
    <p class="div-22__eyebrow">negative stagger · per-keyframe easing</p>
    <h2 class="div-22__title">Motion, in three dots</h2>
    <div class="div-22__rule" role="separator" aria-label="Divider">
      <span class="div-22__dots" aria-hidden="true">
        <span class="div-22__dot"></span><span class="div-22__dot"></span><span class="div-22__dot"></span>
      </span>
    </div>
    <p class="div-22__sub">Every dot starts mid-flight because the delays are negative — nothing waits its turn.</p>
    <div class="div-22__rule div-22__rule--pulse" role="separator" aria-label="Divider">
      <span class="div-22__dots div-22__dots--pulse" aria-hidden="true">
        <span class="div-22__dot"></span><span class="div-22__dot"></span><span class="div-22__dot"></span><span class="div-22__dot"></span><span class="div-22__dot"></span>
      </span>
    </div>
    <p class="div-22__chip">animation-delay:-.22s · cubic-bezier(.3,0,.7,0) up · (.3,1,.7,1) down</p>
  </div>
</section>
```
## CSS
```css
.div-22 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-22-bg);
  --div-22-bg: oklch(0.965 0.008 250);
  --div-22-ink: oklch(0.24 0.02 262);
  --div-22-mut: oklch(0.56 0.02 262);
  --div-22-line: oklch(0.24 0.02 262/.16);
  --div-22-acc: oklch(0.62 0.17 268);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-22-ink);
}

.div-22 *,
.div-22 *::before,
.div-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-22__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(18px,3.4vw,30px);
  text-align: center;
  padding: clamp(28px,6vw,72px) clamp(20px,5vw,56px);
  background: radial-gradient(100% 70% at 50% 0%,oklch(1 0 0),transparent);
}

.div-22__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--div-22-acc);
}

.div-22__title {
  font-size: clamp(28px,5.4vw,54px);
  line-height: 1.05;
  letter-spacing: -.03em;
  font-weight: 700;
}

.div-22__rule {
  width: min(90vw,520px);
  display: flex;
  align-items: center;
  gap: 20px;
}

.div-22__rule::before,
.div-22__rule::after {
  content: '';
  flex: 1 1 0;
  height: 1px;
  background: var(--div-22-line);
}

.div-22__dots {
  display: flex;
  align-items: flex-end;
  gap: 9px;
  height: 26px;
  padding-bottom: 2px;
}

.div-22__dot {
  width: 9px;
  height: 9px;
  border-radius: 99px;
  background: var(--div-22-acc);
  animation: div-22-bounce 1.1s infinite;
}

.div-22__dot:nth-child(1) {
  animation-delay: -.22s;
}

.div-22__dot:nth-child(2) {
  animation-delay: -.11s;
}

.div-22__dot:nth-child(3) {
  animation-delay: 0s;
}

@keyframes div-22-bounce {
  0%,
    100% {
    translate: 0 0;
    animation-timing-function: cubic-bezier(.3,0,.7,0);
    box-shadow: 0 2px 5px oklch(0.62 0.17 268/.45);
  }

  50% {
    translate: 0 -13px;
    animation-timing-function: cubic-bezier(.3,1,.7,1);
    box-shadow: 0 9px 9px oklch(0.62 0.17 268/.16);
  }
}

.div-22__rule--pulse::before,
.div-22__rule--pulse::after {
  background: linear-gradient(90deg,transparent,var(--div-22-line));
}

.div-22__rule--pulse::after {
  background: linear-gradient(90deg,var(--div-22-line),transparent);
}

.div-22__dots--pulse {
  align-items: center;
  height: 18px;
  gap: 11px;
}

.div-22__dots--pulse .div-22__dot {
  width: 7px;
  height: 7px;
  background: oklch(0.7 0.13 300);
  animation: div-22-pulse 1.6s ease-in-out infinite;
  box-shadow: none;
}

.div-22__dots--pulse .div-22__dot:nth-child(1) {
  animation-delay: -.4s;
}

.div-22__dots--pulse .div-22__dot:nth-child(2) {
  animation-delay: -.3s;
}

.div-22__dots--pulse .div-22__dot:nth-child(3) {
  animation-delay: -.2s;
}

.div-22__dots--pulse .div-22__dot:nth-child(4) {
  animation-delay: -.1s;
}

.div-22__dots--pulse .div-22__dot:nth-child(5) {
  animation-delay: 0s;
}

@keyframes div-22-pulse {
  0%,
    100% {
    scale: .65;
    opacity: .4;
  }

  50% {
    scale: 1.5;
    opacity: 1;
  }
}

.div-22__sub {
  max-width: 46ch;
  font-size: clamp(14px,1.8vw,17px);
  line-height: 1.62;
  color: var(--div-22-mut);
  text-wrap: pretty;
}

.div-22__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-22-mut);
  padding: 8px 14px;
  border: 1px solid var(--div-22-line);
  border-radius: 99px;
  max-width: 92vw;
  overflow-wrap: anywhere;
}

@media (prefers-reduced-motion: reduce) {
  .div-22__dot {
    animation: none;
    translate: 0 0;
  }
}
```
