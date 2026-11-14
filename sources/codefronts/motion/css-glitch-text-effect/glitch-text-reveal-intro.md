---
source: "codefronts"
url: "https://codefronts.com/motion/css-glitch-text-effect/glitch-text-reveal-intro/"
title: "Glitch Text Reveal Intro"
section: "motion"
category: "css-glitch-text-effect"
category_name: "CSS Glitch Text Effects"
description: "Page-load title reveal where the headline scales up from zero opacity while heavily distorted, then resolves into clean solid white typography in under 1.2…"
has_js: "true"
---

Here's a working CSS Glitch Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glitch Text Reveal Intro
Source: https://codefronts.com/motion/css-glitch-text-effect/glitch-text-reveal-intro/

Page-load title reveal where the headline scales up from zero opacity while heavily distorted, then resolves into clean solid white typography in under 1.2 seconds -- a one-shot entry animation with a JS replay trigger.
## HTML
```html
<div class="gt-11">
  <div class="gt-11__scene" id="gt-11-scene">
    <h1 class="gt-11__title" data-text="CODEFRONTS">CODEFRONTS</h1>
    <span class="gt-11__tagline">developer gallery · 2027</span>
  </div>
  <button class="gt-11__replay" id="gt-11-replay">↺ Replay Intro</button>
</div>
```
## CSS
```css
.gt-11,
.gt-11 *,
.gt-11 *::before,
.gt-11 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-11 ::selection {
  background: #10b981;
  color: #000;
}

.gt-11 {
  --emerald: #10b981;
  --teal: #14b8a6;
  --bg: #010a07;
  --text: #ecfdf5;
  min-height: 100vh;
  background: var(--bg);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  padding: 48px 20px;
  font-family: 'Inter', system-ui, sans-serif;
  position: relative;
  overflow: hidden;
}

.gt-11__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}
/* Main reveal — title enters distorted, resolves cleanly */

.gt-11__title {
  position: relative;
  font-size: clamp(36px, 7vw, 72px);
  font-weight: 900;
  letter-spacing: -1px;
  color: var(--text);
  animation: gt-11-reveal-main 1.2s cubic-bezier(0.23,1,0.32,1) both;
}

@keyframes gt-11-reveal-main {
  0% {
    opacity: 0;
    transform: scale(0.85) translateY(10px);
    filter: blur(4px);
    text-shadow: none;
  }

  20% {
    opacity: 0.7;
    transform: scale(1.04) translateY(-4px);
    filter: blur(1px);
    text-shadow: -8px 0 var(--emerald), 8px 0 rgba(0,255,200,0.5), 0 0 30px rgba(16,185,129,0.6);
  }

  40% {
    opacity: 0.5;
    transform: scale(0.97) translateY(2px);
    text-shadow: 4px -2px var(--teal), -4px 2px rgba(16,185,129,0.4);
  }

  60% {
    opacity: 0.9;
    transform: scale(1.01) translateY(-1px);
    text-shadow: 0 0 20px rgba(16,185,129,0.3);
  }

  80% {
    opacity: 1;
    transform: scale(1.002) translateY(0);
    text-shadow: 0 0 10px rgba(16,185,129,0.15);
  }

  100% {
    opacity: 1;
    transform: scale(1) translateY(0);
    text-shadow: none;
  }
}
/* Channel offsets during reveal */

.gt-11__title::before {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  font: inherit;
  color: var(--emerald);
  clip-path: polygon(0 0, 100% 0, 100% 40%, 0 40%);
  animation: gt-11-channel-top 1.2s steps(1) both;
}

.gt-11__title::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  font: inherit;
  color: var(--teal);
  clip-path: polygon(0 60%, 100% 60%, 100% 100%, 0 100%);
  animation: gt-11-channel-bot 1.2s steps(1) both;
}

@keyframes gt-11-channel-top {
  0%,
    100% {
    opacity: 0;
    transform: translateX(0);
  }

  10% {
    opacity: 1;
    transform: translateX(-12px);
  }

  30% {
    opacity: 0.8;
    transform: translateX(8px);
  }

  50% {
    opacity: 0.4;
    transform: translateX(-3px);
  }

  70% {
    opacity: 0.1;
  }

  80% {
    opacity: 0;
  }
}

@keyframes gt-11-channel-bot {
  0%,
    100% {
    opacity: 0;
    transform: translateX(0);
  }

  10% {
    opacity: 1;
    transform: translateX(12px);
  }

  30% {
    opacity: 0.8;
    transform: translateX(-8px);
  }

  50% {
    opacity: 0.4;
    transform: translateX(3px);
  }

  70% {
    opacity: 0.1;
  }

  80% {
    opacity: 0;
  }
}

.gt-11__tagline {
  font-size: 13px;
  letter-spacing: 6px;
  color: var(--emerald);
  text-transform: uppercase;
  opacity: 0;
  animation: gt-11-fade-in 0.5s ease 1s both;
}

@keyframes gt-11-fade-in {
  from {
    opacity: 0;
    transform: translateY(6px);
  }

  to {
    opacity: 0.7;
    transform: translateY(0);
  }
}
/* Replay trigger */

.gt-11__replay {
  margin-top: 12px;
  font-size: 11px;
  letter-spacing: 3px;
  color: rgba(16,185,129,0.4);
  cursor: pointer;
  border: none;
  background: none;
  font-family: inherit;
  text-transform: uppercase;
  transition: color 0.2s;
  padding: 6px 12px;
}

.gt-11__replay:hover {
  color: var(--emerald);
}

@media (prefers-reduced-motion: reduce) {
  .gt-11__title,
    .gt-11__title::before,
    .gt-11__title::after,
    .gt-11__tagline {
    animation: none;
    opacity: 1;
  }

  .gt-11__title::before,
    .gt-11__title::after {
    display: none;
  }
}
```

## JavaScript
```js
(function() {
  const btn = document.getElementById('gt-11-replay');
  const scene = document.getElementById('gt-11-scene');
  if (!btn || !scene) return;
  btn.addEventListener('click', function() {
    /* Force re-run by cloning node */
    const clone = scene.cloneNode(true);
    scene.parentNode.replaceChild(clone, scene);
  });
})();
```
