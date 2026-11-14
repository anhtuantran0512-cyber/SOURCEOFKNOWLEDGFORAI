---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/glitch-text-effect/"
title: "Glitch Text Effect"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "The cyberpunk staple, engineered instead of copy-pasted: two full clones of the headline live in ::before/::after via content:attr(data-text) — zero extra…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glitch Text Effect
Source: https://codefronts.com/motion/css-text-hover-effects/glitch-text-effect/

The cyberpunk staple, engineered instead of copy-pasted: two full clones of the headline live in ::before/::after via content:attr(data-text) — zero extra markup, zero extra words for screen readers — offset ±2px into red and cyan, and shredded by clip-path inset() slices that jump on a steps() timeline. At rest the sign is calm with one hairline of chromatic aberration; hover detonates it. All transform/clip/opacity — no layout, no repaint storms — and reduced-motion users get the aberration without the seizure-bait strobing.
## HTML
```html
<section class="cth-06" aria-label="Glitch text hover demo">
  <div class="cth-06__stage">
    <div class="cth-06__scene">
      <p class="cth-06__sys">///&nbsp;SIGNAL 07 &mdash; UNSTABLE FEED</p>
      <a class="cth-06__glitch" href="#cth06-top" id="cth06-top" data-text="NULLSECT//26">NULLSECT//26</a>
      <p class="cth-06__sub">Live briefing &mdash; offensive security summit &middot; night block</p>
      <div class="cth-06__meta">
        <span class="cth-06__cell">OCT 31</span>
        <span class="cth-06__cell">SYDNEY + STREAM</span>
        <span class="cth-06__cell cth-06__cell--hot">HOLD TO CORRUPT</span>
      </div>
      <p class="cth-06__hint">Hover or focus the title. Two <code>attr(data-text)</code> clones, red and cyan, shredded by <code>clip-path</code> on a <code>steps()</code> clock.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-06,
.cth-06 *,
.cth-06 *::before,
.cth-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-06 {
  --bg: oklch(0.14 0.01 270);
  --ink: oklch(0.96 0.005 200);
  --mut: oklch(0.6 0.02 250);
  --red: oklch(0.62 0.24 22);
  --cyan: oklch(0.8 0.13 200);
  font-family: ui-monospace,'Cascadia Code',Menlo,Consolas,monospace;
  color: var(--ink);
}

.cth-06__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: radial-gradient(90% 70% at 50% 30%,oklch(0.18 0.015 275),var(--bg) 70%);
  padding: clamp(20px,4vw,56px);
  container: cth06/inline-size;
  position: relative;
  overflow: clip;
}

.cth-06__stage::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(0deg,oklch(1 0 0/.035) 0 1px,transparent 1px 3px);
}

.cth-06__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: clamp(14px,2.6cqi,22px);
  position: relative;
}

.cth-06__sys {
  font-size: 11.5px;
  letter-spacing: .3em;
  color: var(--mut);
}

.cth-06__glitch {
  position: relative;
  display: inline-block;
  font-size: clamp(38px,9.4cqi,96px);
  font-weight: 800;
  letter-spacing: -.01em;
  line-height: 1.05;
  color: var(--ink);
  text-decoration: none;
  text-shadow: 1px 0 color-mix(in oklch,var(--red) 55%,transparent),-1px 0 color-mix(in oklch,var(--cyan) 55%,transparent);
}

.cth-06__glitch:focus-visible {
  outline: 2px solid var(--cyan);
  outline-offset: 10px;
}

.cth-06__glitch::before,
.cth-06__glitch::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  opacity: 0;
  pointer-events: none;
}

.cth-06__glitch::before {
  color: var(--red);
  z-index: -1;
}

.cth-06__glitch::after {
  color: var(--cyan);
  z-index: -2;
}

.cth-06__glitch:hover,
.cth-06__glitch:focus-visible {
  animation: cth06-base .8s steps(2,jump-none) infinite;
}

.cth-06__glitch:hover::before,
.cth-06__glitch:focus-visible::before {
  opacity: .9;
  animation: cth06-sliceA .7s steps(2,jump-none) infinite;
}

.cth-06__glitch:hover::after,
.cth-06__glitch:focus-visible::after {
  opacity: .9;
  animation: cth06-sliceB .9s steps(2,jump-none) infinite;
}

@keyframes cth06-base {
  0%,
    100% {
    transform: translate(0,0);
  }

  25% {
    transform: translate(1px,0) skewX(.4deg);
  }

  50% {
    transform: translate(-1px,0);
  }

  75% {
    transform: translate(0,1px) skewX(-.4deg);
  }
}

@keyframes cth06-sliceA {
  0% {
    clip-path: inset(12% -2% 61% -2%);
    transform: translate(-3px,-2px);
  }

  25% {
    clip-path: inset(46% -2% 32% -2%);
    transform: translate(3px,1px) skewX(2deg);
  }

  50% {
    clip-path: inset(78% -2% 5% -2%);
    transform: translate(-2px,2px);
  }

  75% {
    clip-path: inset(4% -2% 82% -2%);
    transform: translate(2px,-1px);
  }

  100% {
    clip-path: inset(33% -2% 51% -2%);
    transform: translate(-3px,0);
  }
}

@keyframes cth06-sliceB {
  0% {
    clip-path: inset(64% -2% 18% -2%);
    transform: translate(3px,1px);
  }

  25% {
    clip-path: inset(8% -2% 74% -2%);
    transform: translate(-3px,-1px) skewX(-2deg);
  }

  50% {
    clip-path: inset(41% -2% 39% -2%);
    transform: translate(2px,2px);
  }

  75% {
    clip-path: inset(84% -2% 2% -2%);
    transform: translate(-2px,0);
  }

  100% {
    clip-path: inset(21% -2% 58% -2%);
    transform: translate(3px,-2px);
  }
}

.cth-06__sub {
  font-size: 13.5px;
  letter-spacing: .06em;
  color: var(--mut);
}

.cth-06__meta {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin-top: 4px;
}

.cth-06__cell {
  font-size: 11px;
  letter-spacing: .18em;
  padding: 9px 14px;
  border: 1px solid oklch(0.32 0.02 260);
  color: var(--mut);
}

.cth-06__cell--hot {
  color: var(--cyan);
  border-color: color-mix(in oklch,var(--cyan) 45%,transparent);
}

.cth-06__hint {
  font-size: 12px;
  color: var(--mut);
  max-width: 56ch;
  line-height: 1.7;
}

.cth-06__hint code {
  font-size: .92em;
  background: oklch(0.24 0.015 270);
  padding: 1px 6px;
  border-radius: 4px;
  color: var(--cyan);
}

@media (prefers-reduced-motion: reduce) {
  .cth-06 *,
    .cth-06 *::before,
    .cth-06 *::after {
    animation: none !important;
  }
}
```
