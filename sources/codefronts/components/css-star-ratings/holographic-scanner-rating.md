---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/holographic-scanner-rating/"
title: "Holographic Scanner Rating"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A terminal-aesthetic rating widget with a sweeping green CSS scan beam, CRT scanline overlay, corner bracket chrome, and a score that scrambles via JS…"
has_js: "true"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Holographic Scanner Rating
Source: https://codefronts.com/components/css-star-ratings/holographic-scanner-rating/

A terminal-aesthetic rating widget with a sweeping green CSS scan beam, CRT scanline overlay, corner bracket chrome, and a score that scrambles via JS character substitution before resolving cleanly on selection.
## HTML
```html
<div class="sr-16">
  <div class="sr-16__card">
    <div class="sr-16__inner">
      <div class="sr-16__header">
        <span class="sr-16__sys-label">// NEURO-SCAN RATING SYS v2.7</span>
        <div class="sr-16__status-dot"></div>
      </div>

      <!-- Scanner window -->
      <div class="sr-16__scanner">
        <div class="sr-16__beam-trail"></div>
        <div class="sr-16__beam"></div>
        <div class="sr-16__matrix">
          <div class="sr-16__score-big" id="sr-16-score">0.0</div>
          <div class="sr-16__scan-text" id="sr-16-scan-txt">Awaiting target lock...</div>
        </div>
      </div>

      <!-- Data readout -->
      <div class="sr-16__readout">
        <div class="sr-16__readout-row">
          <span class="sr-16__readout-key">Signal</span>
          <div class="sr-16__readout-bar"><div class="sr-16__readout-fill" id="sr-16-bar1" style="width:72%"></div></div>
          <span class="sr-16__readout-val">72%</span>
        </div>
        <div class="sr-16__readout-row">
          <span class="sr-16__readout-key">Resonance</span>
          <div class="sr-16__readout-bar"><div class="sr-16__readout-fill" id="sr-16-bar2" style="width:48%"></div></div>
          <span class="sr-16__readout-val">48%</span>
        </div>
        <div class="sr-16__readout-row">
          <span class="sr-16__readout-key">Coherence</span>
          <div class="sr-16__readout-bar"><div class="sr-16__readout-fill" id="sr-16-bar3" style="width:61%"></div></div>
          <span class="sr-16__readout-val">61%</span>
        </div>
      </div>

      <!-- Level selector -->
      <div class="sr-16__levels">
        <input type="radio" id="sr-16-l1" name="sr-16-lv" value="1">
        <label for="sr-16-l1" class="sr-16__level-btn">
          <span class="sr-16__level-btn__num">1</span>NULL
        </label>
        <input type="radio" id="sr-16-l2" name="sr-16-lv" value="2">
        <label for="sr-16-l2" class="sr-16__level-btn">
          <span class="sr-16__level-btn__num">2</span>LOW
        </label>
        <input type="radio" id="sr-16-l3" name="sr-16-lv" value="3">
        <label for="sr-16-l3" class="sr-16__level-btn">
          <span class="sr-16__level-btn__num">3</span>MED
        </label>
        <input type="radio" id="sr-16-l4" name="sr-16-lv" value="4">
        <label for="sr-16-l4" class="sr-16__level-btn">
          <span class="sr-16__level-btn__num">4</span>HIGH
        </label>
        <input type="radio" id="sr-16-l5" name="sr-16-lv" value="5">
        <label for="sr-16-l5" class="sr-16__level-btn">
          <span class="sr-16__level-btn__num">5</span>MAX
        </label>
      </div>

      <div class="sr-16__footer">
        <span class="sr-16__coords" id="sr-16-coords">LAT:0.000 · LNG:0.000 · ALT:0m</span>
        <button class="sr-16__submit">Transmit</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sr-16,
.sr-16 *,
.sr-16 *::before,
.sr-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-16 ::selection {
  background: #00ff88;
  color: #000;
}

.sr-16 {
  --green: #00ff88;
  --green2: #00cc66;
  --green-dim: rgba(0,255,136,0.08);
  --bg: #010a05;
  --bg-card: #020e07;
  --grid: rgba(0,255,136,0.04);
  --text: #ccffe6;
  --text-muted: #3a7a56;
  font-family: 'SF Mono', 'Fira Code', 'Courier New', monospace;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

.sr-16__card {
  background: var(--bg-card);
  border: 1px solid rgba(0,255,136,0.15);
  border-radius: 4px;
  padding: 32px 36px 28px;
  max-width: 480px;
  width: 100%;
  position: relative;
  overflow: hidden;
  box-shadow: 0 0 60px rgba(0,255,136,0.05), inset 0 0 60px rgba(0,0,0,0.5);
}
/* Grid scanlines */

.sr-16__card::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: linear-gradient(var(--grid) 1px, transparent 1px), linear-gradient(90deg, var(--grid) 1px, transparent 1px);
  background-size: 24px 24px;
  pointer-events: none;
  z-index: 0;
}
/* CRT scanline overlay */

.sr-16__card::after {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(0,0,0,0.08) 2px,
      rgba(0,0,0,0.08) 4px
    );
  pointer-events: none;
  z-index: 0;
}

.sr-16__inner {
  position: relative;
  z-index: 1;
}

.sr-16__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(0,255,136,0.1);
}

.sr-16__sys-label {
  font-size: 0.65rem;
  color: var(--green);
  letter-spacing: 2px;
  text-transform: uppercase;
  opacity: 0.7;
}

.sr-16__status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--green);
  box-shadow: 0 0 10px var(--green);
  animation: sr-16-blink 1.4s ease-in-out infinite;
}

@keyframes sr-16-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0.2;
  }
}
/* Scanner window */

.sr-16__scanner {
  position: relative;
  height: 160px;
  border: 1px solid rgba(0,255,136,0.2);
  border-radius: 2px;
  margin-bottom: 24px;
  overflow: hidden;
  background: rgba(0,255,136,0.02);
}
/* Corner brackets */

.sr-16__scanner::before,
.sr-16__scanner::after {
  content: '';
  position: absolute;
  width: 16px;
  height: 16px;
  border-color: var(--green);
  border-style: solid;
  opacity: 0.6;
}

.sr-16__scanner::before {
  top: 6px;
  left: 6px;
  border-width: 2px 0 0 2px;
}

.sr-16__scanner::after {
  bottom: 6px;
  right: 6px;
  border-width: 0 2px 2px 0;
}
/* Horizontal scan beam */

.sr-16__beam {
  position: absolute;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--green), transparent);
  box-shadow: 0 0 12px 2px rgba(0,255,136,0.5);
  top: 0;
  animation: sr-16-scan 2.4s cubic-bezier(.4,0,.6,1) infinite;
}

@keyframes sr-16-scan {
  0% {
    top: 0%;
    opacity: 0;
  }

  5% {
    opacity: 1;
  }

  95% {
    opacity: 1;
  }

  100% {
    top: 100%;
    opacity: 0;
  }
}
/* Beam trail */

.sr-16__beam-trail {
  position: absolute;
  left: 0;
  right: 0;
  background: linear-gradient(180deg, transparent, rgba(0,255,136,0.05));
  top: 0;
  animation: sr-16-trail 2.4s cubic-bezier(.4,0,.6,1) infinite;
}

@keyframes sr-16-trail {
  0% {
    height: 0%;
    top: 0;
  }

  100% {
    height: 100%;
    top: 0;
  }
}
/* Score matrix — revealed by scan */

.sr-16__matrix {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 8px;
}

.sr-16__score-big {
  font-size: 4rem;
  font-weight: 900;
  line-height: 1;
  color: var(--green);
  text-shadow: 0 0 30px var(--green), 0 0 60px rgba(0,255,136,0.3);
  letter-spacing: -2px;
  transition: all 0.5s ease;
  opacity: 0.15;
}

.sr-16__score-big.active {
  opacity: 1;
  animation: sr-16-glitch 0.4s steps(1) forwards;
}

@keyframes sr-16-glitch {
  0% {
    clip-path: inset(0 0 80% 0);
    transform: translateX(-4px);
  }

  20% {
    clip-path: inset(20% 0 60% 0);
    transform: translateX(4px);
  }

  40% {
    clip-path: inset(40% 0 40% 0);
    transform: translateX(-2px);
  }

  60% {
    clip-path: inset(60% 0 20% 0);
    transform: translateX(2px);
  }

  80% {
    clip-path: inset(80% 0 0% 0);
    transform: translateX(-1px);
  }

  100% {
    clip-path: inset(0);
    transform: translateX(0);
  }
}

.sr-16__scan-text {
  font-size: 0.65rem;
  letter-spacing: 3px;
  color: var(--green);
  opacity: 0.5;
  text-transform: uppercase;
}
/* Data readout bars */

.sr-16__readout {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 20px;
}

.sr-16__readout-row {
  display: flex;
  align-items: center;
  gap: 10px;
}

.sr-16__readout-key {
  font-size: 0.6rem;
  color: var(--text-muted);
  letter-spacing: 1px;
  width: 72px;
  flex-shrink: 0;
  text-transform: uppercase;
}

.sr-16__readout-bar {
  flex: 1;
  height: 3px;
  background: rgba(0,255,136,0.08);
  position: relative;
  overflow: hidden;
}

.sr-16__readout-fill {
  height: 100%;
  background: var(--green);
  box-shadow: 0 0 8px var(--green);
  width: 0;
  transition: width 0.8s cubic-bezier(.4,0,.2,1);
}

.sr-16__readout-val {
  font-size: 0.6rem;
  color: var(--green);
  width: 32px;
  text-align: right;
  opacity: 0.7;
}
/* Rating selector — 5 level buttons */

.sr-16__levels {
  display: grid;
  grid-template-columns: repeat(5,1fr);
  gap: 6px;
  margin-bottom: 20px;
}

.sr-16__levels input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-16__level-btn {
  display: block;
  text-align: center;
  padding: 10px 4px 8px;
  border: 1px solid rgba(0,255,136,0.15);
  border-radius: 2px;
  font-size: 0.65rem;
  letter-spacing: 1px;
  color: var(--text-muted);
  cursor: pointer;
  text-transform: uppercase;
  transition: all 0.2s;
  position: relative;
  overflow: hidden;
}

.sr-16__level-btn:hover {
  border-color: rgba(0,255,136,0.4);
  color: var(--green);
  background: var(--green-dim);
}

.sr-16__levels input:checked + .sr-16__level-btn {
  border-color: var(--green);
  color: var(--green);
  background: rgba(0,255,136,0.08);
  box-shadow: 0 0 16px rgba(0,255,136,0.15), inset 0 0 12px rgba(0,255,136,0.05);
}

.sr-16__level-btn__num {
  display: block;
  font-size: 1.1rem;
  font-weight: 900;
  margin-bottom: 3px;
  color: inherit;
}
/* Active scan pulse on selected */

.sr-16__levels input:checked + .sr-16__level-btn::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 0%, rgba(0,255,136,0.06) 50%, transparent 100%);
  animation: sr-16-pulse-btn 1.5s ease-in-out infinite;
}

@keyframes sr-16-pulse-btn {
  0%,
    100% {
    transform: translateY(-100%);
  }

  50% {
    transform: translateY(100%);
  }
}

.sr-16__footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.sr-16__coords {
  font-size: 0.6rem;
  color: var(--text-muted);
  letter-spacing: 1px;
  opacity: 0.5;
}

.sr-16__submit {
  padding: 8px 24px;
  border: 1px solid var(--green);
  background: transparent;
  color: var(--green);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  cursor: pointer;
  border-radius: 2px;
  transition: background 0.2s, box-shadow 0.2s;
}

.sr-16__submit:hover {
  background: rgba(0,255,136,0.1);
  box-shadow: 0 0 20px rgba(0,255,136,0.2);
}

@media (prefers-reduced-motion: reduce) {
  .sr-16__beam,
    .sr-16__beam-trail,
    .sr-16__status-dot {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  const tiers = ['NULL','LOW','MED','HIGH','MAX'];
  const barData = [
    [[14,72],[28,44],[42,88],[56,91],[70,100]],   // bar1
    [[10,48],[20,32],[30,61],[40,78],[50,94]],     // bar2
    [[8,61],[16,42],[24,73],[32,85],[40,98]],      // bar3
  ];
  const txts = [
    'Signal degraded · retry',
    'Partial lock acquired',
    'Lock confirmed · nominal',
    'Strong coherence · above threshold',
    'Maximum resonance · optimal',
  ];

  function setBar(id,valId,pct){
    const b = document.getElementById(id);
    const v = document.getElementById(valId);
    if(b) b.style.width = pct+'%';
    if(v) v.textContent = pct+'%';
  }

  document.querySelectorAll('input[name="sr-16-lv"]').forEach((inp,i)=>{
    inp.addEventListener('change',()=>{
      const scoreEl = document.getElementById('sr-16-score');
      const txtEl   = document.getElementById('sr-16-scan-txt');
      const coordEl = document.getElementById('sr-16-coords');

      // Glitch-in the score
      if(scoreEl){
        scoreEl.classList.remove('active');
        void scoreEl.offsetWidth;
        scoreEl.textContent = (i+1)+'.0';
        scoreEl.classList.add('active');
      }
      if(txtEl) txtEl.textContent = txts[i];

      // Animate bars
      setBar('sr-16-bar1','',barData[0][i][1]);
      setBar('sr-16-bar2','',barData[1][i][1]);
      setBar('sr-16-bar3','',barData[2][i][1]);
      document.querySelectorAll('.sr-16__readout-val').forEach((v,j)=>{
        v.textContent = [barData[0][i][1],barData[1][i][1],barData[2][i][1]][j]+'%';
      });

      // Update coords with pseudo random
      const lat = (48.2 + i*2.3).toFixed(3);
      const lng = (11.5 + i*1.7).toFixed(3);
      if(coordEl) coordEl.textContent = `LAT:${lat} · LNG:${lng} · ALT:${(i+1)*42}m`;
    });
  });
})();
```
