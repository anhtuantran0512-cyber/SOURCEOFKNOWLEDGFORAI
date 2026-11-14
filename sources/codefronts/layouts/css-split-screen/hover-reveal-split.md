---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/hover-reveal-split/"
title: "Hover Reveal Split"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "K-pop concert poster — hot pink + electric cyan + chrome."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hover Reveal Split
Source: https://codefronts.com/layouts/css-split-screen/hover-reveal-split/

K-pop concert poster — hot pink + electric cyan + chrome. Two halves; hover/tap each to grow it from 50% to 70%, the other shrinks. Pure CSS via flex-grow transition; massive condensed type and chromatic-aberration headlines complete the album-cover feel.
## HTML
```html
<section class="ss-kpop" aria-label="Album release split">
  <article class="ss-kpop-side ss-kpop-pink">
    <span class="ss-kpop-eye">SIDE A</span>
    <h2><span>NEON</span><span>HEART</span></h2>
    <p>Vol. 03 · Out now</p>
    <div class="ss-kpop-track">
      <span>01 ⟡ Midnight Drive</span>
      <span>02 ⟡ Lights Off</span>
      <span>03 ⟡ Pink Static</span>
    </div>
    <button type="button" class="ss-kpop-cta">▶ PLAY</button>
  </article>
  <article class="ss-kpop-side ss-kpop-cyan">
    <span class="ss-kpop-eye">SIDE B</span>
    <h2><span>CYBER</span><span>BLOOM</span></h2>
    <p>Vol. 03 · Out now</p>
    <div class="ss-kpop-track">
      <span>04 ⟡ Glass Hearts</span>
      <span>05 ⟡ Hologram</span>
      <span>06 ⟡ Echo Park</span>
    </div>
    <button type="button" class="ss-kpop-cta">▶ PLAY</button>
  </article>
</section>
```
## CSS
```css
.ss-kpop {
  width: 100%;
  display: flex;
  min-height: 100vh;
  font-family: 'Helvetica Neue', sans-serif;
  background: #0a0014;
  border-radius: 0;
  overflow: hidden;
  isolation: isolate;
}

.ss-kpop-side {
  flex: 1 1 50%;
  position: relative;
  padding: 36px 32px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  cursor: pointer;
  transition: flex-grow 0.4s cubic-bezier(0.32, 0.72, 0, 1);
  overflow: hidden;
  isolation: isolate;
}

.ss-kpop-side:hover,
.ss-kpop-side:focus-within {
  flex-grow: 1.6;
}

.ss-kpop-pink {
  background: repeating-linear-gradient(0deg, transparent 0 4px, rgba(0,0,0,0.05) 4px 5px), radial-gradient(60% 80% at 30% 30%, #ff52aa 0%, #c41560 100%);
  color: #fff;
  border-right: 2px solid #fff;
}

.ss-kpop-cyan {
  background: repeating-linear-gradient(0deg, transparent 0 4px, rgba(0,0,0,0.05) 4px 5px), radial-gradient(60% 80% at 70% 70%, #00e5ff 0%, #0080a8 100%);
  color: #0a0014;
}

.ss-kpop-pink::before,
.ss-kpop-cyan::before {
  content: '';
  position: absolute;
  width: 220px;
  height: 220px;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.85), rgba(255,255,255,0.2) 50%, transparent 70%);
  z-index: -1;
}

.ss-kpop-pink::before {
  top: -60px;
  right: -60px;
}

.ss-kpop-cyan::before {
  bottom: -60px;
  left: -60px;
}

.ss-kpop-eye {
  font-family: 'Courier New', monospace;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.32em;
}

.ss-kpop-pink .ss-kpop-eye {
  color: #ffd400;
  text-shadow: 0 0 10px rgba(255,212,0,0.4);
}

.ss-kpop-cyan .ss-kpop-eye {
  color: #ff00aa;
}

.ss-kpop-side h2 {
  margin: 0;
  font-size: clamp(48px, 8vw, 96px);
  font-weight: 900;
  line-height: 0.85;
  letter-spacing: -0.04em;
  display: flex;
  flex-direction: column;
  font-style: italic;
}

.ss-kpop-side h2 span:nth-child(2) {
  align-self: flex-end;
}

.ss-kpop-pink h2 {
  color: #fff;
  text-shadow: -3px 0 0 #00e5ff, 3px 0 0 #ffd400;
}

.ss-kpop-cyan h2 {
  color: #0a0014;
  text-shadow: -3px 0 0 #ff52aa, 3px 0 0 #ffd400;
}

.ss-kpop-side p {
  margin: 0;
  font-family: 'Courier New', monospace;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.2em;
}

.ss-kpop-pink p {
  color: #ffd400;
}

.ss-kpop-cyan p {
  color: #0a0014;
}

.ss-kpop-track {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 14px 0;
  border-top: 1px solid currentColor;
  border-bottom: 1px solid currentColor;
  font-family: 'Courier New', monospace;
  font-size: 12.5px;
  font-weight: 700;
  letter-spacing: 0.06em;
  opacity: 0.9;
}

.ss-kpop-cta {
  margin-top: auto;
  align-self: flex-start;
  padding: 12px 22px;
  background: #fff;
  color: #0a0014;
  border: 0;
  font-family: 'Courier New', monospace;
  font-size: 14px;
  font-weight: 900;
  letter-spacing: 0.16em;
  cursor: pointer;
  transition: transform 0.12s;
}

.ss-kpop-pink .ss-kpop-cta {
  background: #ffd400;
  color: #c41560;
}

.ss-kpop-cyan .ss-kpop-cta {
  background: #ff52aa;
  color: #fff;
}

.ss-kpop-cta:hover {
  transform: scale(1.05);
}

@media (max-width: 720px) {
  .ss-kpop {
    flex-direction: column;
  }

  .ss-kpop-side {
    flex: 1 1 auto;
  }

  .ss-kpop-side:hover,
    .ss-kpop-side:focus-within {
    flex-grow: 1;
  }

  .ss-kpop-pink {
    border-right: 0;
    border-bottom: 2px solid #fff;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ss-kpop-side {
    transition: none;
  }
}
```
