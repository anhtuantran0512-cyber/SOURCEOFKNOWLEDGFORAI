---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-typewriter-text-animation/"
title: "Pure CSS Typewriter Effect Single Line"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "The definitive single-line typewriter: a ch-width animation snapped by steps() so exactly one character appears per tick, with a blinking caret — shown three…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Typewriter Effect Single Line
Source: https://codefronts.com/motion/css-text-animations/css-typewriter-text-animation/

The definitive single-line typewriter: a ch-width animation snapped by steps() so exactly one character appears per tick, with a blinking caret — shown three ways: a terminal prompt, a serif marketing hero, and an infinite type-and-delete loop.
## HTML
```html
<div class="cat-06-group">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="cat-06a" aria-label="Terminal typewriter effect">
  <div class="cat-06a__win">
    <div class="cat-06a__bar" aria-hidden="true"><i></i><i></i><i></i><em>codefronts — zsh</em></div>
    <p class="cat-06a__row"><span class="cat-06a__prompt" aria-hidden="true">➜&nbsp;~&nbsp;</span><span class="cat-06a__type">npm create future-app</span></p>
    <p class="cat-06a__hint" aria-hidden="true">▲ 21 characters · steps(21) · 2.4s</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
<section class="cat-06b" aria-label="Serif hero typewriter effect">
  <div class="cat-06b__stage">
    <p class="cat-06b__kicker">Codefronts Studio</p>
    <h1 class="cat-06b__title"><span class="cat-06b__type">Design that ships itself.</span></h1>
    <p class="cat-06b__sub">Typewriter pacing, zero JavaScript — the whole sentence lives in the HTML.</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-06c" aria-label="Looping typewriter effect">
  <h1 class="cat-06c__line"><span class="cat-06c__type">Build. Ship. Repeat.</span></h1>
  <p class="cat-06c__hint" aria-hidden="true">types → holds → deletes → loops</p>
</section>
</div>
```
## CSS
```css
.cat-06-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-06-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-06a,
.cat-06a *,
.cat-06a *::before,
.cat-06a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-06a {
  --green: oklch(0.87 0.19 152);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(130% 100% at 50% 0%,#131a24,#0a0e14);
  font-family: 'JetBrains Mono',ui-monospace,'SF Mono',Menlo,monospace;
}

.cat-06a__win {
  width: min(560px,100%);
  border-radius: 14px;
  background: #0d1420;
  border: 1px solid rgba(148,180,255,.14);
  box-shadow: 0 30px 60px -30px rgba(0,0,0,.8),inset 0 1px 0 rgba(255,255,255,.05);
  overflow: hidden;
}

.cat-06a__bar {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
  background: rgba(255,255,255,.04);
  border-bottom: 1px solid rgba(148,180,255,.1);
}

.cat-06a__bar i {
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: #3a4456;
}

.cat-06a__bar i:nth-child(1) {
  background: #ff5f57;
}

.cat-06a__bar i:nth-child(2) {
  background: #febc2e;
}

.cat-06a__bar i:nth-child(3) {
  background: #28c840;
}

.cat-06a__bar em {
  margin-left: auto;
  font-style: normal;
  font-size: 11px;
  color: rgba(200,215,240,.45);
}

.cat-06a__row {
  display: flex;
  align-items: baseline;
  padding: 28px 22px 10px;
  font-size: 17px;
  color: #e8f0ff;
}

.cat-06a__prompt {
  color: var(--green);
  font-weight: 700;
}

.cat-06a__type {
  display: inline-block;
  overflow: hidden;
  white-space: nowrap;
  max-width: 21ch;
  border-right: 2px solid var(--green);
  padding-right: 2px;
  animation: cat-06a-typing 2.4s steps(21) .6s both,cat-06a-caret .8s step-end infinite;
}

.cat-06a__hint {
  padding: 0 22px 24px;
  font-size: 11px;
  letter-spacing: .08em;
  color: rgba(200,215,240,.35);
}

@keyframes cat-06a-typing {
  from {
    max-width: 0;
  }
}

@keyframes cat-06a-caret {
  50% {
    border-color: transparent;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-06a__type {
    animation: cat-06a-caret 1.2s step-end infinite;
    max-width: 21ch;
  }
}

.cat-06b,
.cat-06b *,
.cat-06b *::before,
.cat-06b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-06b {
  --ink: #1c1917;
  --amber: oklch(0.72 0.16 65);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#faf6ef,#f2ead9);
  font-family: 'Playfair Display',Georgia,'Times New Roman',serif;
}

.cat-06b__stage {
  text-align: center;
  max-width: 860px;
}

.cat-06b__kicker {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .34em;
  text-transform: uppercase;
  color: rgba(28,25,23,.5);
  margin-bottom: 22px;
}

.cat-06b__title {
  font-size: clamp(30px,5vw,58px);
  font-weight: 600;
  color: var(--ink);
  letter-spacing: -.01em;
}

.cat-06b__type {
  display: inline-block;
  overflow: hidden;
  white-space: nowrap;
  vertical-align: bottom;
  max-width: 25ch;
  border-right: 3px solid var(--amber);
  padding-right: 6px;
  animation: cat-06b-typing 2.6s steps(25) .5s both,cat-06b-caret .75s step-end infinite;
}

.cat-06b__sub {
  margin-top: 22px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 15px;
  color: rgba(28,25,23,.55);
  opacity: 0;
  animation: cat-06b-fade .8s ease 3.3s forwards;
}

@keyframes cat-06b-typing {
  from {
    max-width: 0;
  }
}

@keyframes cat-06b-caret {
  50% {
    border-color: transparent;
  }
}

@keyframes cat-06b-fade {
  to {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-06b__type {
    animation: none;
    max-width: 25ch;
    border-color: transparent;
  }

  .cat-06b__sub {
    animation: none;
    opacity: 1;
  }
}

.cat-06c,
.cat-06c *,
.cat-06c *::before,
.cat-06c *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-06c {
  --cyan: oklch(0.85 0.14 195);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: 48px 24px;
  background: #0b0f16;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-06c__line {
  font-size: clamp(30px,5vw,56px);
  font-weight: 600;
  color: #eef3fb;
  letter-spacing: -.02em;
}

.cat-06c__type {
  display: inline-block;
  overflow: hidden;
  white-space: nowrap;
  vertical-align: bottom;
  font-family: ui-monospace,'JetBrains Mono',Menlo,monospace;
  border-right: 3px solid var(--cyan);
  padding-right: 5px;
  animation: cat-06c-loop 6s infinite,cat-06c-caret .7s step-end infinite;
}

.cat-06c__hint {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: rgba(180,200,230,.35);
  text-align: center;
}

@keyframes cat-06c-loop {
  0% {
    max-width: 0;
    animation-timing-function: steps(20);
  }

  42% {
    max-width: 20ch;
  }

  72% {
    max-width: 20ch;
    animation-timing-function: steps(20);
  }

  96%,
    100% {
    max-width: 0;
  }
}

@keyframes cat-06c-caret {
  50% {
    border-color: transparent;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-06c__type {
    animation: cat-06c-caret 1.2s step-end infinite;
    max-width: 20ch;
  }
}
```

## JavaScript
```js
/* No JavaScript — width animates 0 → 21ch snapped by steps(21); a border-right caret blinks with step-end. */

/* No JavaScript — same steps() width sweep in a proportional serif; 25ch is hand-tuned to the sentence and the subline fades in after typing ends. */

/* No JavaScript — one keyframe track types (0→42%), holds (→72%), then deletes (→100%); each segment carries its own steps(20) timing function. */
```
