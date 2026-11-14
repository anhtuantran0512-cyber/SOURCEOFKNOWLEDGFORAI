---
source: "codefronts"
url: "https://codefronts.com/motion/css-pulse-animation/video-play-button-overlay-pulse/"
title: "Video Play Button Overlay Pulse"
section: "motion"
category: "css-pulse-animation"
category_name: "CSS Pulse Animations"
description: "A landing-page hero video overlay — dark cinematic thumbnail with a static amber play triangle in a circular container that casts an expansive transparent…"
has_js: "false"
---

Here's a working CSS Pulse Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Video Play Button Overlay Pulse
Source: https://codefronts.com/motion/css-pulse-animation/video-play-button-overlay-pulse/

A landing-page hero video overlay — dark cinematic thumbnail with a static amber play triangle in a circular container that casts an expansive transparent pulsing shadow outward. The pulse tempts a click without competing with the video itself. Editorial dark palette (#0d0d10) with amber #f59e0b play button — New Yorker / The Atlantic / editorial video convention. Playfair Display headline overlay for magazine-cinematic feel.
## HTML
```html
<div class="pl-03">
  <div class="pl-03__scrim"></div>
  <div class="pl-03__content">
    <p class="pl-03__eyebrow">The Long Read · Episode 04</p>
    <h1 class="pl-03__title">How they built the last<br/>independent search engine.</h1>
    <p class="pl-03__meta">A 4-part documentary series · Chapter 1: The founding room</p>
  </div>
  <button class="pl-03__play" type="button" aria-label="Play video — The Long Read Episode 04">
    <svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor" aria-hidden="true">
      <path d="M8 5v14l11-7z"/>
    </svg>
  </button>
  <span class="pl-03__runtime">03:24</span>
</div>
```
## CSS
```css
.pl-03 {
  --bg: #0d0d10;
  --ink: #f5f5f0;
  --sub: #a8a29e;
  --amber: #f59e0b;
  --amber-glow: rgba(245,158,11,.35);
  font-family: -apple-system,BlinkMacSystemFont,Georgia,'Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(70% 90% at 30% 40%, rgba(90,70,40,.35) 0%, transparent 60%), radial-gradient(60% 80% at 80% 70%, rgba(60,40,30,.25) 0%, transparent 55%), linear-gradient(135deg,#1a1512 0%,var(--bg) 60%);
  color: var(--ink);
}

.pl-03 *,
.pl-03 *::before,
.pl-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pl-03 ::selection {
  background: var(--amber);
  color: var(--bg);
}

.pl-03__scrim {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 55%, transparent 25%, rgba(0,0,0,.5) 85%);
  pointer-events: none;
}

.pl-03__content {
  position: absolute;
  left: 0;
  right: 0;
  top: 14%;
  text-align: center;
  padding: 0 24px;
}

.pl-03__eyebrow {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--amber);
  margin-bottom: 12px;
}

.pl-03__title {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: clamp(1.6rem,3.8vw,2.6rem);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.15;
  margin-bottom: 10px;
  text-shadow: 0 2px 20px rgba(0,0,0,.5);
}

.pl-03__meta {
  font-size: .85rem;
  color: var(--sub);
  font-style: italic;
}

.pl-03__play {
  position: relative;
  width: 88px;
  height: 88px;
  border: none;
  border-radius: 50%;
  background: rgba(245,158,11,.95);
  color: var(--bg);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8px 40px -8px rgba(245,158,11,.6);
  transition: transform .18s ease,background .18s ease;
  z-index: 2;
}

.pl-03__play svg {
  margin-left: 4px;
}

.pl-03__play:hover {
  background: var(--amber);
  transform: scale(1.06);
}

.pl-03__play:active {
  transform: scale(.98);
}

.pl-03__play:focus-visible {
  outline: 2px solid var(--amber);
  outline-offset: 6px;
}
/* Halo pulse — dual pseudo-elements, wide + slow for cinematic feel */

.pl-03__play::before,
.pl-03__play::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: var(--amber-glow);
  pointer-events: none;
  z-index: 0;
  animation: pl-03-halo 2.4s ease-out infinite;
}

.pl-03__play::after {
  animation-delay: 1.2s;
}

@keyframes pl-03-halo {
  0% {
    transform: scale(1);
    opacity: .35;
  }

  70% {
    transform: scale(2.4);
    opacity: 0;
  }

  100% {
    transform: scale(2.6);
    opacity: 0;
  }
}

.pl-03__runtime {
  position: absolute;
  bottom: 24px;
  right: 24px;
  padding: 5px 10px;
  border-radius: 5px;
  background: rgba(0,0,0,.7);
  color: var(--ink);
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .04em;
  font-variant-numeric: tabular-nums;
  backdrop-filter: blur(4px);
  z-index: 2;
}

@media (prefers-reduced-motion: reduce) {
  .pl-03__play::before,
    .pl-03__play::after {
    animation: none!important;
  }
}
```
