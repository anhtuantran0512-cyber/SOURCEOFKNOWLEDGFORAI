---
source: "codefronts"
url: "https://codefronts.com/motion/css-glitch-text-effect/spooky-horror-twitching-text/"
title: "Spooky Horror Twitching Text"
section: "motion"
category: "css-glitch-text-effect"
category_name: "CSS Glitch Text Effects"
description: "Ghostly white serif headline on a near-black background with erratic, asymmetric text-shadow layers that violently expand and collapse at irregular intervals…"
has_js: "false"
---

Here's a working CSS Glitch Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Spooky Horror Twitching Text
Source: https://codefronts.com/motion/css-glitch-text-effect/spooky-horror-twitching-text/

Ghostly white serif headline on a near-black background with erratic, asymmetric text-shadow layers that violently expand and collapse at irregular intervals -- for Halloween and dark gaming sites.
## HTML
```html
<div class="gt-08">
  <span class="gt-08__eyebrow">do not read aloud</span>
  <div style="position:relative">
    <span class="gt-08__word">HAUNTED</span>
    <span class="gt-08__ghost">HAUNTED</span>
  </div>
  <p class="gt-08__tagline">"it knows you're watching"</p>
</div>
```
## CSS
```css
.gt-08,
.gt-08 *,
.gt-08 *::before,
.gt-08 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-08 ::selection {
  background: #7f1d1d;
  color: #fff;
}

.gt-08 {
  --blood: #8b0000;
  --blood-bright: #dc2626;
  --ghost: rgba(255,255,255,0.85);
  --bg: #050005;
  min-height: 100vh;
  background: var(--bg);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 48px 20px;
  font-family: Georgia, 'Palatino Linotype', serif;
  position: relative;
  overflow: hidden;
}
/* Fog layers */

.gt-08::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse 60% 40% at 50% 60%, rgba(80,0,0,0.25) 0%, transparent 70%), radial-gradient(ellipse 80% 30% at 30% 100%, rgba(0,0,0,0.8) 0%, transparent 60%);
  pointer-events: none;
}
/* Blood drip from top */

.gt-08::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg,
      transparent 10%, var(--blood) 20%, var(--blood-bright) 30%,
      transparent 40%, var(--blood) 55%, var(--blood-bright) 70%,
      transparent 80%
    );
  box-shadow: 0 0 12px var(--blood);
}

.gt-08__eyebrow {
  font-size: 11px;
  letter-spacing: 6px;
  color: rgba(255,255,255,0.2);
  text-transform: uppercase;
}
/* The twitching horror text */

.gt-08__word {
  font-size: clamp(44px, 10vw, 90px);
  font-weight: 700;
  color: var(--ghost);
  letter-spacing: 10px;
  text-transform: uppercase;
  text-align: center;
  position: relative;
  /* Baseline red ghost-duplicate shadow + faint blood-glow so the
       horror atmosphere reads even between the twitch keyframes (which
       spent 80% of their cycle at text-shadow: 0). The animated frames
       still layer their wilder displacements on top. */
  text-shadow: -2px 0 rgba(180,0,0,0.45), 2px 0 rgba(100,0,0,0.45), 0 0 24px rgba(139,0,0,0.5);
  /* Animation duration slowed from 0.1s to 3s so individual twitch
       keyframes are visible to the eye (was 10 frames/sec — eye reads
       as a continuous blur). At 3s, each keyframe stop now lasts
       ~30-90ms which is the sweet spot for "perceptible jerk". */
  animation: gt-08-twitch 3s steps(1) infinite;
}

@keyframes gt-08-twitch {
  /* Calm states keep the baseline red ghost-shadow visible; flares
       amplify it dramatically at asymmetric intervals. Displacement
       amplitudes roughly doubled (-12px → -22px peak, etc) so the
       jerk visibly throws the word off-axis when it fires. */

  0% {
    text-shadow: -2px 0 rgba(180,0,0,0.45), 2px 0 rgba(100,0,0,0.45), 0 0 24px rgba(139,0,0,0.5);
    transform: translate(0,0);
  }

  12% {
    text-shadow: -6px 0 var(--blood-bright), 6px 0 rgba(255,100,100,0.7), 0 2px 24px var(--blood);
    transform: translate(-5px, 2px);
  }

  16% {
    text-shadow: -2px 0 rgba(180,0,0,0.45), 2px 0 rgba(100,0,0,0.45), 0 0 24px rgba(139,0,0,0.5);
    transform: translate(0,0);
  }

  27% {
    text-shadow: 10px -4px var(--blood), -10px 4px rgba(255,0,0,0.5), 0 0 48px rgba(139,0,0,0.85);
    transform: translate(7px,-4px);
  }

  30%,
    34%,
    60%,
    84%,
    100% {
    text-shadow: -2px 0 rgba(180,0,0,0.45), 2px 0 rgba(100,0,0,0.45), 0 0 24px rgba(139,0,0,0.5);
    transform: translate(0,0);
  }

  32% {
    text-shadow: 5px 0 rgba(255,100,100,0.9), -5px 0 var(--blood);
    transform: translate(3px,0);
  }

  55% {
    text-shadow: -16px 6px var(--blood-bright), 16px -6px rgba(180,0,0,0.85), 0 0 72px rgba(139,0,0,0.65);
    transform: translate(-9px,5px);
  }

  58% {
    text-shadow: 9px -3px rgba(255,50,50,0.75);
    transform: translate(5px,-3px);
  }

  78% {
    text-shadow: -5px 10px var(--blood), 5px -10px rgba(255,200,200,0.4);
    transform: translate(-3px,7px);
  }

  81% {
    text-shadow: -2px 0 rgba(180,0,0,0.45), 2px 0 rgba(100,0,0,0.45), 0 0 24px rgba(139,0,0,0.5);
    transform: translate(0,0);
  }

  93% {
    text-shadow: -22px 0 var(--blood-bright), 22px 0 rgba(100,0,0,1), 0 0 90px rgba(139,0,0,0.75);
    transform: translate(-12px,0);
  }

  96% {
    text-shadow: 12px 8px var(--blood);
    transform: translate(7px,5px);
  }
}

.gt-08__tagline {
  font-size: 13px;
  font-style: italic;
  color: rgba(255,255,255,0.2);
  letter-spacing: 2px;
  text-align: center;
}
/* Ghost flicker overlay */

.gt-08__ghost {
  position: absolute;
  font-size: clamp(44px, 10vw, 90px);
  font-weight: 700;
  letter-spacing: 10px;
  text-transform: uppercase;
  color: transparent;
  text-shadow: 0 0 0 transparent;
  animation: gt-08-ghost-appear 8s steps(1) infinite;
  pointer-events: none;
  white-space: nowrap;
}

@keyframes gt-08-ghost-appear {
  0%,
    94%,
    100% {
    opacity: 0;
  }

  95% {
    opacity: 0.06;
    color: rgba(255,255,255,0.06);
  }

  96% {
    opacity: 0;
  }

  97% {
    opacity: 0.03;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-08__word,
    .gt-08__ghost {
    animation: none;
  }

  .gt-08__word {
    text-shadow: 0 0 20px rgba(139,0,0,0.5);
  }
}
```
