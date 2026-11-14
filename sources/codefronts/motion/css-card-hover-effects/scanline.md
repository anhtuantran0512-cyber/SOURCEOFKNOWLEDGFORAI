---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/scanline/"
title: "Scanline"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A retro CRT terminal card with phosphor-green text, static scanlines, a sweeping refresh beam, and a blinking cursor."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scanline
Source: https://codefronts.com/motion/css-card-hover-effects/scanline/

A retro CRT terminal card with phosphor-green text, static scanlines, a sweeping refresh beam, and a blinking cursor. Great for cybersecurity, retro-tech, archival, or developer products that lean into a vintage-computing identity.
## HTML
```html
<div class="card-14">
  <article class="card-14__card">
    <div class="card-14__inner">
      <span class="card-14__head">&gt; SYSTEM/READY_</span>
      <h2 class="card-14__title">VAULT<br>OS 9<span class="card-14__cursor">&nbsp;</span></h2>
      <p class="card-14__desc">Cold-storage terminal for archival data. Phosphor-green display, zero network exposure.</p>
      <div class="card-14__stat">
        <span>UPTIME 4096d</span>
        <span>MEM 64K OK</span>
      </div>
    </div>
    <div class="card-14__lines"></div>
    <div class="card-14__beam"></div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=VT323&family=Share+Tech+Mono&display=swap');

.card-14,
.card-14 *,
.card-14 *::before,
.card-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-14 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #04110a;
  font-family: 'Share Tech Mono', monospace;
  padding: 2rem;
}

.card-14__card {
  position: relative;
  width: 340px;
  height: 430px;
  border-radius: 10px;
  background: #021006;
  cursor: pointer;
  overflow: hidden;
  border: 1px solid #0c5;
  box-shadow: 0 0 25px rgba(0,255,120,0.12), inset 0 0 30px rgba(0,255,120,0.05);
}

.card-14__inner {
  position: relative;
  z-index: 1;
  height: 100%;
  padding: 2.2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #38ff8e;
  text-shadow: 0 0 4px rgba(56,255,142,0.6);
}

.card-14__head {
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  opacity: 0.7;
}

.card-14__title {
  font-family: 'VT323', monospace;
  font-size: 3.4rem;
  line-height: 0.95;
}

.card-14__cursor {
  display: inline-block;
  width: 0.6ch;
  background: #38ff8e;
  animation: card-14-blink 1s steps(1) infinite;
}

@keyframes card-14-blink {
  50% {
    opacity: 0;
  }
}

.card-14__desc {
  font-size: 0.85rem;
  line-height: 1.6;
  opacity: 0.85;
}

.card-14__stat {
  display: flex;
  justify-content: space-between;
  font-size: 0.75rem;
  border-top: 1px dashed rgba(56,255,142,0.4);
  padding-top: 0.8rem;
  opacity: 0.7;
}

.card-14__lines {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: repeating-linear-gradient(
      0deg,
      rgba(0,0,0,0.25) 0 1px,
      transparent 1px 3px
    );
  pointer-events: none;
}

.card-14__beam {
  position: absolute;
  left: 0;
  right: 0;
  height: 80px;
  top: -80px;
  z-index: 3;
  background: linear-gradient(
      to bottom,
      transparent,
      rgba(56,255,142,0.18) 50%,
      transparent
    );
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.card-14__card:hover .card-14__beam {
  opacity: 1;
  animation: card-14-sweep 2s linear infinite;
}

@keyframes card-14-sweep {
  0% {
    top: -80px;
  }

  100% {
    top: 100%;
  }
}

.card-14__card::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 4;
  pointer-events: none;
  background: radial-gradient(ellipse at center, transparent 60%, rgba(0,0,0,0.5));
}

@media (prefers-reduced-motion: reduce) {
  .card-14__cursor,
    .card-14__beam {
    animation: none !important;
  }
}
```
