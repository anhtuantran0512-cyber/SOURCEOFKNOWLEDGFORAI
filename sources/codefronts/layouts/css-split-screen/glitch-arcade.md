---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/glitch-arcade/"
title: "Glitch Arcade"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Cyber-arcade split — deep purple base with neon-green and magenta."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glitch Arcade
Source: https://codefronts.com/layouts/css-split-screen/glitch-arcade/

Cyber-arcade split — deep purple base with neon-green and magenta. Continuous glitch overlay shifts the colored layers in/out across the seam. Different from Tokyo Neon (sidebars): this is dystopian-arcade not tokyo-pop, dark green vs hot magenta.
## HTML
```html
<section class="ss-cyb" aria-label="Cyberpunk arcade split">
  <article class="ss-cyb-left">
    <span class="ss-cyb-glitch ss-cyb-glitch-l" aria-hidden="true"></span>
    <header>
      <span class="ss-cyb-coin">// LOAD &gt;&gt;</span>
      <h2 data-text="GHOST PROTOCOL">GHOST<br />PROTOCOL</h2>
    </header>
    <p>Free-to-play. Pay-to-survive.</p>
    <div class="ss-cyb-meter">
      <span>SYSTEM_INTEGRITY</span>
      <div class="ss-cyb-bar"><span class="ss-cyb-fill" style="width: 73%"></span></div>
      <em>73%</em>
    </div>
  </article>
  <article class="ss-cyb-right">
    <span class="ss-cyb-glitch ss-cyb-glitch-r" aria-hidden="true"></span>
    <ul class="ss-cyb-leader">
      <li><span>01</span><strong>RAVEN_Z</strong><b>9128</b></li>
      <li><span>02</span><strong>v0id_X</strong><b>8044</b></li>
      <li class="me"><span>03</span><strong>YOU</strong><b>7621</b></li>
      <li><span>04</span><strong>n3on_Q</strong><b>6890</b></li>
    </ul>
    <button type="button" class="ss-cyb-cta">/ ENTER /</button>
    <span class="ss-cyb-warn">⚠ HIGH RISK SECTOR</span>
  </article>
</section>
```
## CSS
```css
.ss-cyb {
  width: 100%;
  position: relative;
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 100vh;
  font-family: 'Courier New', 'Helvetica Neue', sans-serif;
  background: #0a0014;
  color: #e8e0ff;
  border-radius: 0;
  overflow: hidden;
  isolation: isolate;
}

.ss-cyb::after {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg, rgba(0,0,0,0.15) 0 1px, transparent 1px 4px);
  mix-blend-mode: overlay;
  pointer-events: none;
  z-index: 5;
}

.ss-cyb-left,
.ss-cyb-right {
  position: relative;
  padding: 36px 32px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  isolation: isolate;
}

.ss-cyb-left {
  background: radial-gradient(70% 80% at 30% 30%, rgba(0,255,140,0.18) 0%, transparent 60%), linear-gradient(160deg, #1a0040 0%, #0a0014 100%);
  border-right: 2px solid #00ff8c;
  box-shadow: 12px 0 30px rgba(0,255,140,0.15);
}

.ss-cyb-right {
  background: radial-gradient(70% 80% at 70% 70%, rgba(255,0,170,0.18) 0%, transparent 60%), linear-gradient(200deg, #2a0044 0%, #0a0014 100%);
}

.ss-cyb-glitch {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(0deg, transparent 0 8px, rgba(0,255,140,0.06) 8px 9px);
  animation: ss-cyb-jitter 2.4s steps(8) infinite;
  z-index: -1;
}

.ss-cyb-glitch-r {
  background: repeating-linear-gradient(0deg, transparent 0 8px, rgba(255,0,170,0.07) 8px 9px);
  animation-duration: 1.8s;
  animation-direction: reverse;
}

@keyframes ss-cyb-jitter {
  0%,
    100% {
    transform: translate(0);
  }

  20% {
    transform: translate(-2px, 1px);
  }

  40% {
    transform: translate(1px, -1px);
  }

  60% {
    transform: translate(-1px, 2px);
  }

  80% {
    transform: translate(2px, 0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ss-cyb-glitch {
    animation: none;
  }
}

.ss-cyb-coin {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.28em;
  color: #00ff8c;
  text-shadow: 0 0 12px rgba(0,255,140,0.6);
}

.ss-cyb-left h2 {
  margin: 4px 0 0;
  font-family: 'Helvetica Neue', sans-serif;
  font-size: clamp(36px, 6vw, 64px);
  font-weight: 900;
  line-height: 0.92;
  color: #fff;
  letter-spacing: -0.03em;
  font-style: italic;
  position: relative;
  text-shadow: -2px 0 0 #00ff8c, 2px 0 0 #ff00aa, 0 0 30px rgba(255,255,255,0.3);
}

.ss-cyb-left p {
  margin: 0;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.16em;
  color: #ff00aa;
  text-transform: uppercase;
}

.ss-cyb-meter {
  margin-top: auto;
  padding: 14px;
  background: rgba(0,255,140,0.06);
  border: 1px solid rgba(0,255,140,0.4);
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.ss-cyb-meter span {
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.22em;
  color: #00ff8c;
}

.ss-cyb-bar {
  height: 8px;
  background: rgba(0,0,0,0.5);
  border: 1px solid rgba(0,255,140,0.3);
}

.ss-cyb-fill {
  display: block;
  height: 100%;
  background: linear-gradient(90deg, #00ff8c 0%, #ff00aa 100%);
  box-shadow: 0 0 12px #00ff8c;
}

.ss-cyb-meter em {
  align-self: flex-end;
  font-family: 'Helvetica Neue', sans-serif;
  font-size: 22px;
  font-weight: 900;
  font-style: italic;
  color: #00ff8c;
  text-shadow: 0 0 10px rgba(0,255,140,0.6);
}

.ss-cyb-leader {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.ss-cyb-leader li {
  display: grid;
  grid-template-columns: 28px 1fr auto;
  align-items: center;
  gap: 12px;
  padding: 8px 10px;
  font-size: 14px;
  border: 1px solid rgba(255,0,170,0.2);
  background: rgba(0,0,0,0.3);
}

.ss-cyb-leader li.me {
  background: rgba(255,0,170,0.16);
  border-color: #ff00aa;
  box-shadow: 0 0 12px rgba(255,0,170,0.3);
}

.ss-cyb-leader li span {
  font-size: 11px;
  font-weight: 800;
  color: #ff00aa;
  letter-spacing: 0.16em;
}

.ss-cyb-leader li strong {
  font-size: 13px;
  font-weight: 700;
  color: #fff;
  letter-spacing: 0.08em;
}

.ss-cyb-leader li b {
  font-family: 'Helvetica Neue', sans-serif;
  font-style: italic;
  font-weight: 800;
  color: #00ff8c;
  text-shadow: 0 0 8px rgba(0,255,140,0.5);
}

.ss-cyb-cta {
  align-self: flex-start;
  padding: 14px 26px;
  background: #ff00aa;
  color: #0a0014;
  border: 0;
  font-family: 'Helvetica Neue', sans-serif;
  font-size: 14px;
  font-weight: 900;
  letter-spacing: 0.18em;
  cursor: pointer;
  box-shadow: 0 0 24px rgba(255,0,170,0.5);
  transition: background 0.14s, transform 0.12s;
  font-style: italic;
}

.ss-cyb-cta:hover {
  background: #00ff8c;
  box-shadow: 0 0 24px rgba(0,255,140,0.5);
}

.ss-cyb-cta:active {
  transform: scale(0.97);
}

.ss-cyb-warn {
  align-self: flex-start;
  padding: 4px 10px;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: 0.18em;
  color: #ffd400;
  background: rgba(255,212,0,0.1);
  border: 1px dashed #ffd400;
  margin-top: auto;
}

@media (max-width: 720px) {
  .ss-cyb {
    grid-template-columns: 1fr;
  }

  .ss-cyb-left {
    border-right: 0;
    border-bottom: 2px solid #00ff8c;
    box-shadow: 0 12px 30px rgba(0,255,140,0.15);
  }
}
```
