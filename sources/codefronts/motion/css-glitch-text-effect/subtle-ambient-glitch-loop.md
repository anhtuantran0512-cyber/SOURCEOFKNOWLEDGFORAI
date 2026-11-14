---
source: "codefronts"
url: "https://codefronts.com/motion/css-glitch-text-effect/subtle-ambient-glitch-loop/"
title: "Subtle Ambient Glitch Loop"
section: "motion"
category: "css-glitch-text-effect"
category_name: "CSS Glitch Text Effects"
description: "A near-invisible micro-glitch on a light-mode product card that slips a single horizontal band 4px left for one frame every 4 seconds -- ambient, accessible,…"
has_js: "false"
---

Here's a working CSS Glitch Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Subtle Ambient Glitch Loop
Source: https://codefronts.com/motion/css-glitch-text-effect/subtle-ambient-glitch-loop/

A near-invisible micro-glitch on a light-mode product card that slips a single horizontal band 4px left for one frame every 4 seconds -- ambient, accessible, and zero-distraction for production UI.
## HTML
```html
<div class="gt-06">
  <div class="gt-06__card">
    <span class="gt-06__overline">Enterprise Platform</span>
    <h2 class="gt-06__headline" data-text="Invisible Artifacts">Invisible Artifacts</h2>
    <p class="gt-06__body">An ambient micro-glitch that fires every 4 seconds. Blink and you'll miss it — a single horizontal band slips 4px to the left for one frame then snaps back. No layout repaints, zero jank.</p>
    <div class="gt-06__chips">
      <span class="gt-06__chip">Pure CSS</span>
      <span class="gt-06__chip">0 JS</span>
      <span class="gt-06__chip">Ambient Loop</span>
    </div>
  </div>
</div>
```
## CSS
```css
.gt-06,
.gt-06 *,
.gt-06 *::before,
.gt-06 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-06 ::selection {
  background: #1d4ed8;
  color: #fff;
}

.gt-06 {
  --blue: #1d4ed8;
  --blue-light: #60a5fa;
  --bg: #f8faff;
  --text: #0f172a;
  --border: #e2e8f0;
  --muted: #64748b;
  min-height: 100vh;
  background: var(--bg);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 48px 20px;
  font-family: 'Inter', system-ui, sans-serif;
}
/* Light-mode product card context */

.gt-06__card {
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 40px 48px;
  max-width: 420px;
  width: 100%;
  box-shadow: 0 4px 24px rgba(15,23,42,0.06);
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.gt-06__overline {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 3px;
  color: var(--blue);
  text-transform: uppercase;
}
/* The ambient glitch text — almost undetectable until you watch closely */

.gt-06__headline {
  position: relative;
  font-size: clamp(26px, 4vw, 38px);
  font-weight: 800;
  color: var(--text);
  letter-spacing: -0.5px;
  line-height: 1.15;
  /* Permanent faint blue/red ghost-shadow keeps the "subtle" identity
       while still signalling glitch in the gallery thumbnail (the
       original opacity:0 idle state caught a plain headline 95% of
       the time, defeating the whole gallery preview). */
  text-shadow: -1px 0 rgba(59,130,246,0.45), 1px 0 rgba(239,68,68,0.45);
}
/* Blue chromatic layer — sits in the UPPER third of the headline.
   When the headline wraps to two lines, this band slices just the
   top of line 1. Previously both pseudos shared the same mid-band
   (38-52%), which on a 2-line headline landed in the gap BETWEEN
   the two lines and rendered as a phantom duplicate of line 1 below
   itself. Splitting into upper-band (this) + lower-band (::after)
   matches the classic Lucas-Bebber chromatic-aberration recipe. */

.gt-06__headline::before {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  font: inherit;
  color: var(--blue);
  clip-path: polygon(0 8%, 100% 8%, 100% 28%, 0 28%);
  opacity: 0.5;
  transform: translateX(-3px);
  animation: gt-06-slip-upper 5s steps(1) infinite;
}
/* Red chromatic layer — sits in the LOWER third of the headline.
   On a 2-line headline this lands inside line 2; on a 1-line headline
   it lands at the bottom of the single line. Either way, it does
   NOT overlap with the upper band. */

.gt-06__headline::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  font: inherit;
  color: #ef4444;
  clip-path: polygon(0 72%, 100% 72%, 100% 92%, 0 92%);
  opacity: 0.5;
  transform: translateX(3px);
  animation: gt-06-slip-lower 5s steps(1) infinite;
  animation-delay: 0.08s;
}

@keyframes gt-06-slip-upper {
  /* Calm baseline — upper band, small left offset */

  0%,
    46%,
    56%,
    89%,
    98%,
    100% {
    opacity: 0.5;
    transform: translateX(-3px);
    clip-path: polygon(0 8%, 100% 8%, 100% 28%, 0 28%);
  }
  /* Mid-loop burst — upper band moves left aggressively */

  47% {
    opacity: 1;
    transform: translateX(-14px);
    clip-path: polygon(0 4%, 100% 4%, 100% 24%, 0 24%);
  }

  50% {
    opacity: 0.95;
    transform: translateX(10px);
    clip-path: polygon(0 12%, 100% 12%, 100% 32%, 0 32%);
  }

  52% {
    opacity: 0.85;
    transform: translateX(-6px);
    clip-path: polygon(0 8%, 100% 8%, 100% 28%, 0 28%);
  }

  54% {
    opacity: 0.65;
    transform: translateX(-3px);
  }
  /* End-of-loop burst — bigger displacement */

  90% {
    opacity: 1;
    transform: translateX(-16px);
    clip-path: polygon(0 4%, 100% 4%, 100% 24%, 0 24%);
  }

  93% {
    opacity: 0.95;
    transform: translateX(12px);
    clip-path: polygon(0 12%, 100% 12%, 100% 32%, 0 32%);
  }

  95% {
    opacity: 0.85;
    transform: translateX(-8px);
  }

  97% {
    opacity: 0.65;
    transform: translateX(-3px);
  }
}

@keyframes gt-06-slip-lower {
  /* Calm baseline — lower band, small right offset */

  0%,
    46%,
    56%,
    89%,
    98%,
    100% {
    opacity: 0.5;
    transform: translateX(3px);
    clip-path: polygon(0 72%, 100% 72%, 100% 92%, 0 92%);
  }
  /* Mid-loop burst — lower band moves RIGHT (opposite direction
       from upper) for that anaglyph-glasses chromatic split look */

  47% {
    opacity: 1;
    transform: translateX(14px);
    clip-path: polygon(0 68%, 100% 68%, 100% 88%, 0 88%);
  }

  50% {
    opacity: 0.95;
    transform: translateX(-10px);
    clip-path: polygon(0 76%, 100% 76%, 100% 96%, 0 96%);
  }

  52% {
    opacity: 0.85;
    transform: translateX(6px);
    clip-path: polygon(0 72%, 100% 72%, 100% 92%, 0 92%);
  }

  54% {
    opacity: 0.65;
    transform: translateX(3px);
  }
  /* End-of-loop burst — bigger displacement */

  90% {
    opacity: 1;
    transform: translateX(16px);
    clip-path: polygon(0 68%, 100% 68%, 100% 88%, 0 88%);
  }

  93% {
    opacity: 0.95;
    transform: translateX(-12px);
    clip-path: polygon(0 76%, 100% 76%, 100% 96%, 0 96%);
  }

  95% {
    opacity: 0.85;
    transform: translateX(8px);
  }

  97% {
    opacity: 0.65;
    transform: translateX(3px);
  }
}

.gt-06__body {
  font-size: 14px;
  color: var(--muted);
  line-height: 1.65;
  margin-top: 8px;
}

.gt-06__chips {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-top: 4px;
}

.gt-06__chip {
  font-size: 11px;
  font-weight: 500;
  padding: 3px 10px;
  background: #eff6ff;
  color: var(--blue);
  border-radius: 100px;
  letter-spacing: 0.5px;
}

@media (prefers-reduced-motion: reduce) {
  .gt-06__headline::before,
    .gt-06__headline::after {
    animation: none;
    opacity: 0;
  }
}
```
