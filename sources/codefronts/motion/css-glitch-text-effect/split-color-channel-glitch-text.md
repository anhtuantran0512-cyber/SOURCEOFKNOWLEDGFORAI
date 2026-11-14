---
source: "codefronts"
url: "https://codefronts.com/motion/css-glitch-text-effect/split-color-channel-glitch-text/"
title: "Split Color-Channel Glitch Text"
section: "motion"
category: "css-glitch-text-effect"
category_name: "CSS Glitch Text Effects"
description: "The main headline text is color:transparent -- only the red and blue pseudo-element channels are visible, slowly drifting apart at different rates via smooth…"
has_js: "false"
---

Here's a working CSS Glitch Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Split Color-Channel Glitch Text
Source: https://codefronts.com/motion/css-glitch-text-effect/split-color-channel-glitch-text/

The main headline text is color:transparent -- only the red and blue pseudo-element channels are visible, slowly drifting apart at different rates via smooth ease-in-out keyframes, with a violent sync snap that briefly clips the channels to non-overlapping bands.
## HTML
```html
<div class="gt-14">
  <span class="gt-14__eyebrow">Chromatic Aberration</span>
  <div class="gt-14__chroma" data-text="ABERRANT">ABERRANT</div>
  <div class="gt-14__legend">
    <div class="gt-14__channel"><div class="gt-14__swatch gt-14__swatch--r"></div>Red Ch.</div>
    <div class="gt-14__channel"><div class="gt-14__swatch gt-14__swatch--b"></div>Blue Ch.</div>
  </div>
</div>
```
## CSS
```css
.gt-14,
.gt-14 *,
.gt-14 *::before,
.gt-14 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-14 ::selection {
  background: #e2e8f0;
  color: #000;
}

.gt-14 {
  --red-ch: #ff2020;
  --blue-ch: #2060ff;
  --bg: #08080f;
  --text: #f0f0ff;
  min-height: 100vh;
  background: var(--bg);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 28px;
  padding: 48px 20px;
  font-family: 'Inter', system-ui, sans-serif;
  position: relative;
  overflow: hidden;
}
/* Subtle lens-aberration vignette */

.gt-14::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse 80% 60% at 50% 50%, transparent 50%, rgba(0,0,0,0.5) 100%);
  pointer-events: none;
}

.gt-14__eyebrow {
  font-size: 10px;
  letter-spacing: 5px;
  color: rgba(240,240,255,0.3);
  text-transform: uppercase;
}
/* Container: color:transparent so only channel ghosts show */

.gt-14__chroma {
  position: relative;
  font-size: clamp(44px, 9vw, 90px);
  font-weight: 900;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: transparent;
  /* The main layer is invisible */
  user-select: none;
}
/* Red channel — drifts left */

.gt-14__chroma::before {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  font: inherit;
  letter-spacing: inherit;
  color: var(--red-ch);
  mix-blend-mode: screen;
  animation: gt-14-red-drift 3.5s ease-in-out infinite alternate;
  opacity: 0.85;
}
/* Blue channel — drifts right */

.gt-14__chroma::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  font: inherit;
  letter-spacing: inherit;
  color: var(--blue-ch);
  mix-blend-mode: screen;
  animation: gt-14-blue-drift 3.5s ease-in-out infinite alternate;
  opacity: 0.85;
}
/* Where red + blue overlap → white/violet shows naturally */

@keyframes gt-14-red-drift {
  0% {
    transform: translate(-6px, 0);
  }

  25% {
    transform: translate(-4px, 1px);
  }

  50% {
    transform: translate(-8px, -1px);
  }

  75% {
    transform: translate(-3px, 0);
  }

  100% {
    transform: translate(-10px, 1px);
  }
}

@keyframes gt-14-blue-drift {
  0% {
    transform: translate(6px, 0);
  }

  25% {
    transform: translate(9px, -1px);
  }

  50% {
    transform: translate(4px, 1px);
  }

  75% {
    transform: translate(11px, 0);
  }

  100% {
    transform: translate(5px, -1px);
  }
}
/* Violent snap glitch intermittently */

.gt-14__chroma::before {
  animation: gt-14-red-drift 3.5s ease-in-out infinite alternate, gt-14-red-snap 5s steps(1) infinite;
}

.gt-14__chroma::after {
  animation: gt-14-blue-drift 3.5s ease-in-out infinite alternate, gt-14-blue-snap 5s steps(1) infinite;
}

@keyframes gt-14-red-snap {
  0%,
    88%,
    100% {
    clip-path: none;
  }

  89% {
    transform: translate(-20px, 0);
    clip-path: polygon(0 20%, 100% 20%, 100% 45%, 0 45%);
  }

  90% {
    transform: translate(-14px, 2px);
    clip-path: polygon(0 55%, 100% 55%, 100% 80%, 0 80%);
  }

  91% {
    transform: translate(-6px, 0);
    clip-path: none;
  }
}

@keyframes gt-14-blue-snap {
  0%,
    88%,
    100% {
    clip-path: none;
  }

  89% {
    transform: translate(22px, 0);
    clip-path: polygon(0 20%, 100% 20%, 100% 45%, 0 45%);
  }

  90% {
    transform: translate(15px, -2px);
    clip-path: polygon(0 55%, 100% 55%, 100% 80%, 0 80%);
  }

  91% {
    transform: translate(6px, 0);
    clip-path: none;
  }
}

.gt-14__legend {
  display: flex;
  gap: 24px;
  align-items: center;
}

.gt-14__channel {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  letter-spacing: 2px;
  color: rgba(240,240,255,0.4);
  text-transform: uppercase;
}

.gt-14__swatch {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}

.gt-14__swatch--r {
  background: var(--red-ch);
  box-shadow: 0 0 8px var(--red-ch);
}

.gt-14__swatch--b {
  background: var(--blue-ch);
  box-shadow: 0 0 8px var(--blue-ch);
}

@media (prefers-reduced-motion: reduce) {
  .gt-14__chroma::before {
    animation: none;
    transform: translate(-6px,0);
  }

  .gt-14__chroma::after {
    animation: none;
    transform: translate(6px,0);
  }
}
```
