---
source: "codefronts"
url: "https://codefronts.com/motion/css-bounce-animation/dvd-screensaver-viewport-bounce/"
title: "DVD Screensaver Viewport Bounce"
section: "motion"
category: "css-bounce-animation"
category_name: "CSS Bounce Animations"
description: "The cult DVD screensaver bounce — a logo travels diagonally across the viewport and cleanly bounces off all four edges, hoping to land perfectly in a corner…"
has_js: "false"
---

Here's a working CSS Bounce Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: DVD Screensaver Viewport Bounce
Source: https://codefronts.com/motion/css-bounce-animation/dvd-screensaver-viewport-bounce/

The cult DVD screensaver bounce — a logo travels diagonally across the viewport and cleanly bounces off all four edges, hoping to land perfectly in a corner (the internet's favorite unsolved problem). Retro dark surface with an 80s neon-purple logo. Pure CSS with separate X and Y keyframes at coprime durations so the trajectory never visually repeats. Zero JavaScript. Every 90s kid searches for this at some point.
## HTML
```html
<div class="bn-15">
  <p class="bn-15__label">DVD screensaver viewport bounce</p>
  <div class="bn-15__viewport" aria-hidden="true">
    <div class="bn-15__logo">DVD</div>
  </div>
  <p class="bn-15__hint">X + Y keyframes at coprime durations — trajectory never visually repeats.</p>
</div>
```
## CSS
```css
.bn-15 {
  --page-bg: #050510;
  --viewport-bg: #0a0a18;
  --ink: #f5f5fa;
  --sub: #8b8ba0;
  --neon-a: #a855f7;
  --neon-b: #22d3ee;
  --line: #1a1a30;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
  padding: 32px;
  background: radial-gradient(80% 60% at 50% 50%, rgba(168,85,247,.08) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
  text-align: center;
}

.bn-15 *,
.bn-15 *::before,
.bn-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bn-15 ::selection {
  background: var(--neon-a);
  color: #050510;
}

.bn-15__label {
  font-size: .9rem;
  font-weight: 600;
  color: var(--sub);
  letter-spacing: .02em;
}

.bn-15__viewport {
  position: relative;
  width: min(600px,100%);
  aspect-ratio: 16/9;
  background: var(--viewport-bg);
  border: 1px solid var(--line);
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 20px 40px -12px rgba(168,85,247,.14),inset 0 0 60px rgba(168,85,247,.08);
}

.bn-15__logo {
  position: absolute;
  top: 0;
  left: 0;
  padding: 10px 22px;
  border-radius: 10px;
  background: linear-gradient(135deg,var(--neon-a),var(--neon-b));
  color: #fff;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 1.1rem;
  font-weight: 900;
  letter-spacing: .08em;
  box-shadow: 0 0 20px rgba(168,85,247,.5),0 0 40px rgba(34,211,238,.35);
  animation: bn-15-x 4.7s linear infinite alternate, bn-15-y 3.3s linear infinite alternate;
  will-change: transform;
}

@keyframes bn-15-x {
  0% {
    transform: translateX(0);
  }

  100% {
    transform: translateX(calc(600px - 100%));
  }
}

@keyframes bn-15-y {
  0% {
    transform: translateY(0);
  }

  100% {
    transform: translateY(calc(340px - 100%));
  }
}
/* Combine both transforms via the CSS animation composition — modern browsers stack */

@supports (animation-composition: add) {
  .bn-15__logo {
    animation-composition: add;
  }
}
/* Fallback for browsers without composition: single combined keyframe (won't produce independent X/Y coprime bounce but stays visually acceptable) */

@supports not (animation-composition: add) {
  .bn-15__logo {
    animation: bn-15-combined 4.7s linear infinite alternate;
  }

  @keyframes bn-15-combined {
    0% {
      transform: translate(0,0);
    }

    25% {
      transform: translate(calc(600px - 100%),40px);
    }

    50% {
      transform: translate(calc(600px - 100%),calc(340px - 100%));
    }

    75% {
      transform: translate(0,calc(340px - 100%));
    }

    100% {
      transform: translate(0,0);
    }
  }
}

.bn-15__hint {
  font-size: .78rem;
  color: var(--sub);
  max-width: 400px;
  line-height: 1.5;
}

@media (prefers-reduced-motion: reduce) {
  .bn-15__logo {
    animation: none!important;
    transform: translate(calc((600px - 100%) / 2),calc((340px - 100%) / 2))!important;
  }
}
```
