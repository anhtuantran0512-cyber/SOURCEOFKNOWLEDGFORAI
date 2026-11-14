---
source: "codefronts"
url: "https://codefronts.com/motion/css-glitch-text-effect/css-glitch-text-hover-effect/"
title: "CSS Glitch Text Hover Effect"
section: "motion"
category: "css-glitch-text-effect"
category_name: "CSS Glitch Text Effects"
description: "Clean, readable white text on a dark card that executes a violent 0.35-second RGB-split burst on hover then instantly returns to pristine typography -- zero…"
has_js: "false"
---

Here's a working CSS Glitch Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glitch Text Hover Effect
Source: https://codefronts.com/motion/css-glitch-text-effect/css-glitch-text-hover-effect/

Clean, readable white text on a dark card that executes a violent 0.35-second RGB-split burst on hover then instantly returns to pristine typography -- zero animation when at rest.
## HTML
```html
<div class="gt-02">
  <div class="gt-02__card">
    <span class="gt-02__eyebrow">Product Launch 2027</span>
    <span class="gt-02__word" data-text="HOVER ME">HOVER ME</span>
    <p class="gt-02__body">A single burst of violent chromatic slice on mouse enter, then instant snap back to clean readability.</p>
    <span class="gt-02__hint">↑ move cursor over the text above</span>
  </div>
</div>
```
## CSS
```css
.gt-02,
.gt-02 *,
.gt-02 *::before,
.gt-02 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-02 ::selection {
  background: #7c3aed;
  color: #fff;
}

.gt-02 {
  --accent: #7c3aed;
  --accent2: #e879f9;
  --bg: #0f0f13;
  --text: #f0f0f8;
  --muted: rgba(240,240,248,0.4);
  min-height: 100vh;
  background: var(--bg);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  padding: 48px 24px;
  font-family: 'Inter', 'Helvetica Neue', system-ui, sans-serif;
}

.gt-02__card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 16px;
  padding: 40px 56px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  align-items: flex-start;
}

.gt-02__eyebrow {
  font-size: 11px;
  letter-spacing: 3px;
  color: var(--accent2);
  text-transform: uppercase;
  font-weight: 500;
}
/* The glitch word — calm until hover */

.gt-02__word {
  position: relative;
  display: inline-block;
  font-size: clamp(36px, 6vw, 64px);
  font-weight: 800;
  color: var(--text);
  letter-spacing: -1px;
  cursor: default;
  user-select: none;
  /* Baseline magenta/cyan ghost-shadow signals "glitchable" even
       in the idle state — otherwise the gallery thumbnail captures
       plain white text with zero glitch cue. Hover still fires the
       dramatic RGB slice burst on top. */
  text-shadow: -2px 0 rgba(255,0,255,0.5), 2px 0 rgba(0,255,255,0.5);
}

.gt-02__word::before,
.gt-02__word::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  font: inherit;
  letter-spacing: inherit;
  opacity: 0;
  transition: opacity 0s;
}

.gt-02__word::before {
  color: #f0f;
  clip-path: polygon(0 20%, 100% 20%, 100% 45%, 0 45%);
}

.gt-02__word::after {
  color: #0ff;
  clip-path: polygon(0 55%, 100% 55%, 100% 80%, 0 80%);
}
/* Trigger on hover */

.gt-02__word:hover::before {
  opacity: 1;
  animation: gt-02-up 0.35s steps(1) forwards;
}

.gt-02__word:hover::after {
  opacity: 1;
  animation: gt-02-down 0.35s steps(1) forwards;
}

@keyframes gt-02-up {
  0% {
    transform: translateX(0);
    opacity: 1;
    clip-path: polygon(0 20%, 100% 20%, 100% 45%, 0 45%);
  }

  20% {
    transform: translateX(-8px);
    clip-path: polygon(0 15%, 100% 15%, 100% 40%, 0 40%);
  }

  40% {
    transform: translateX(7px);
    clip-path: polygon(0 22%, 100% 22%, 100% 50%, 0 50%);
  }

  60% {
    transform: translateX(-4px);
    clip-path: polygon(0 18%, 100% 18%, 100% 38%, 0 38%);
  }

  80% {
    transform: translateX(2px);
    clip-path: polygon(0 20%, 100% 20%, 100% 42%, 0 42%);
  }

  100% {
    transform: translateX(0);
    opacity: 0;
  }
}

@keyframes gt-02-down {
  0% {
    transform: translateX(0);
    opacity: 1;
    clip-path: polygon(0 55%, 100% 55%, 100% 80%, 0 80%);
  }

  20% {
    transform: translateX(8px);
    clip-path: polygon(0 58%, 100% 58%, 100% 78%, 0 78%);
  }

  40% {
    transform: translateX(-6px);
    clip-path: polygon(0 52%, 100% 52%, 100% 82%, 0 82%);
  }

  60% {
    transform: translateX(4px);
    clip-path: polygon(0 56%, 100% 56%, 100% 76%, 0 76%);
  }

  80% {
    transform: translateX(-2px);
    clip-path: polygon(0 55%, 100% 55%, 100% 80%, 0 80%);
  }

  100% {
    transform: translateX(0);
    opacity: 0;
  }
}

.gt-02__body {
  font-size: 15px;
  color: var(--muted);
  max-width: 320px;
  line-height: 1.6;
  margin-top: 4px;
}

.gt-02__hint {
  font-size: 11px;
  color: rgba(240,240,248,0.25);
  margin-top: 12px;
  letter-spacing: 1px;
}

@media (prefers-reduced-motion: reduce) {
  .gt-02__word::before,
    .gt-02__word::after {
    display: none;
  }
}
```
