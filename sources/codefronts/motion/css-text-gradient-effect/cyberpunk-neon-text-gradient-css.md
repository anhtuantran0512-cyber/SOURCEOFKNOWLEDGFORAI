---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/cyberpunk-neon-text-gradient-css/"
title: "Cyberpunk Neon Text Gradient CSS"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "A CRT-scanline terminal UI with electric pink, cyan, and purple neon gradients amplified by CSS drop-shadow filters for a glow effect."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cyberpunk Neon Text Gradient CSS
Source: https://codefronts.com/motion/css-text-gradient-effect/cyberpunk-neon-text-gradient-css/

A CRT-scanline terminal UI with electric pink, cyan, and purple neon gradients amplified by CSS drop-shadow filters for a glow effect.
## HTML
```html
<div class="tg-09">
  <div class="tg-09__scene">
    <div class="tg-09__scanlines" aria-hidden="true"></div>
    <div class="tg-09__content">
      <p class="tg-09__sys">SYS://NEXUS_2077 — USER AUTHENTICATED</p>
      <h1 class="tg-09__title"><span class="tg-09__g1">CYBER</span><span class="tg-09__g2">PUNK</span></h1>
      <h2 class="tg-09__sub-title"><span class="tg-09__g3">NEON</span> <span class="tg-09__g4">INTERFACE</span></h2>
      <div class="tg-09__row">
        <div class="tg-09__stat"><span class="tg-09__stat-v tg-09__g1">78%</span><span>THREAT</span></div>
        <div class="tg-09__stat"><span class="tg-09__stat-v tg-09__g3">4096</span><span>CREDITS</span></div>
        <div class="tg-09__stat"><span class="tg-09__stat-v tg-09__g2">LEVEL 9</span><span>CLEARANCE</span></div>
      </div>
      <div class="tg-09__bar-wrap">
        <span class="tg-09__bar-lbl">NEURAL SYNC</span>
        <div class="tg-09__bar"><div class="tg-09__bar-fill"></div></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.tg-09,
.tg-09 *,
.tg-09 *::before,
.tg-09 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-09 ::selection {
  background: #ff2d78;
  color: #000;
}

.tg-09 {
  --pink: #ff2d78;
  --cyan: #00f0ff;
  --purple: #bc00ff;
  --yellow: #ffe600;
  --bg: #05020d;
  --text: #e0d7f0;
  --muted: #4a3f6a;
  font-family: 'Courier New', monospace;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 24px;
}

.tg-09__scene {
  position: relative;
  width: 100%;
  max-width: 620px;
  border: 1px solid rgba(0,240,255,.2);
  border-radius: 4px;
  overflow: hidden;
  padding: 36px 32px;
  background: rgba(5,2,13,.9);
}
/* CRT scanlines overlay */

.tg-09__scanlines {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(0,240,255,.025) 2px,
      rgba(0,240,255,.025) 4px
    );
  pointer-events: none;
  z-index: 10;
}

.tg-09__content {
  position: relative;
  z-index: 1;
}

.tg-09__sys {
  font-size: .65rem;
  letter-spacing: .12em;
  color: rgba(0,240,255,.5);
  margin-bottom: 20px;
  animation: tg-09-blink 2s step-end infinite;
}

@keyframes tg-09-blink {
  50% {
    opacity: .4;
  }
}
/* Shared gradient text helpers */

.tg-09__g1 {
  background: linear-gradient(90deg, var(--pink) 0%, var(--purple) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  filter: drop-shadow(0 0 8px var(--pink));
}

.tg-09__g2 {
  background: linear-gradient(90deg, var(--cyan) 0%, #0088ff 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  filter: drop-shadow(0 0 8px var(--cyan));
}

.tg-09__g3 {
  background: linear-gradient(90deg, var(--yellow) 0%, #ff8c00 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  filter: drop-shadow(0 0 6px var(--yellow));
}

.tg-09__g4 {
  background: linear-gradient(90deg, var(--purple) 0%, var(--pink) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.tg-09__title {
  font-size: clamp(3rem, 10vw, 5.5rem);
  font-weight: 900;
  line-height: 1;
  letter-spacing: .05em;
  display: flex;
  gap: .2em;
}

.tg-09__sub-title {
  font-size: clamp(1.1rem, 4vw, 2rem);
  font-weight: 700;
  letter-spacing: .15em;
  margin: 8px 0 28px;
}

.tg-09__row {
  display: flex;
  gap: 28px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}

.tg-09__stat {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.tg-09__stat-v {
  font-size: 1.4rem;
  font-weight: 700;
}

.tg-09__stat span:last-child {
  font-size: .6rem;
  letter-spacing: .12em;
  color: var(--muted);
}

.tg-09__bar-wrap {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.tg-09__bar-lbl {
  font-size: .65rem;
  letter-spacing: .12em;
  color: var(--muted);
}

.tg-09__bar {
  height: 4px;
  background: rgba(255,255,255,.06);
  border-radius: 2px;
  overflow: hidden;
}

.tg-09__bar-fill {
  height: 100%;
  width: 73%;
  background: linear-gradient(90deg, var(--cyan), var(--purple), var(--pink));
  background-size: 200%;
  animation: tg-09-scan 2s linear infinite;
}

@keyframes tg-09-scan {
  0% {
    background-position: 0%;
  }

  100% {
    background-position: 200%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tg-09__sys,
    .tg-09__bar-fill {
    animation: none;
  }
}
```
