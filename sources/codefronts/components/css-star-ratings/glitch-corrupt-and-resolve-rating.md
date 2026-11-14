---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/glitch-corrupt-and-resolve-rating/"
title: "Glitch Corrupt-and-Resolve Rating"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A terminal-red rating widget where selecting a level triggers a 14-step character scramble with RGB channel splitting, horizontal noise bars, and screen…"
has_js: "true"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glitch Corrupt-and-Resolve Rating
Source: https://codefronts.com/components/css-star-ratings/glitch-corrupt-and-resolve-rating/

A terminal-red rating widget where selecting a level triggers a 14-step character scramble with RGB channel splitting, horizontal noise bars, and screen shake before the true score resolves cleanly.
## HTML
```html
<div class="sr-22">
  <div class="sr-22__card">
    <div class="sr-22__inner">
      <div class="sr-22__topbar">
        <span class="sr-22__sys">// ERR_RATE_SYS v0.9β</span>
        <span class="sr-22__err">⚠ SIGNAL UNSTABLE</span>
      </div>

      <!-- Score display -->
      <div class="sr-22__score-display">
        <div class="sr-22__noise-bars" id="sr-22-noise">
          <div class="sr-22__noise-bar" style="top:15%"></div>
          <div class="sr-22__noise-bar" style="top:38%"></div>
          <div class="sr-22__noise-bar" style="top:62%"></div>
          <div class="sr-22__noise-bar" style="top:80%"></div>
        </div>
        <div class="sr-22__score-main" id="sr-22-score" data-text="?">?</div>
        <div class="sr-22__score-label" id="sr-22-score-lbl">Awaiting signal...</div>
      </div>

      <!-- Input buttons -->
      <div class="sr-22__inputs">
        <input type="radio" id="sr-22-i1" name="sr-22-g" value="1">
        <label for="sr-22-i1" class="sr-22__input-btn">
          <span class="sr-22__btn-num">1</span>NULL
        </label>

        <input type="radio" id="sr-22-i2" name="sr-22-g" value="2">
        <label for="sr-22-i2" class="sr-22__input-btn">
          <span class="sr-22__btn-num">2</span>GLCH
        </label>

        <input type="radio" id="sr-22-i3" name="sr-22-g" value="3">
        <label for="sr-22-i3" class="sr-22__input-btn">
          <span class="sr-22__btn-num">3</span>SYNC
        </label>

        <input type="radio" id="sr-22-i4" name="sr-22-g" value="4">
        <label for="sr-22-i4" class="sr-22__input-btn">
          <span class="sr-22__btn-num">4</span>LOCK
        </label>

        <input type="radio" id="sr-22-i5" name="sr-22-g" value="5">
        <label for="sr-22-i5" class="sr-22__input-btn">
          <span class="sr-22__btn-num">5</span>MAX
        </label>
      </div>

      <div class="sr-22__status">
        <div class="sr-22__status-indicator" id="sr-22-dot"></div>
        <span class="sr-22__status-text" id="sr-22-status">// waiting for input</span>
      </div>

      <div class="sr-22__footer">
        <button class="sr-22__btn sr-22__btn--primary">Transmit</button>
        <button class="sr-22__btn sr-22__btn--ghost">Abort</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sr-22,
.sr-22 *,
.sr-22 *::before,
.sr-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-22 ::selection {
  background: #ff0066;
  color: #fff;
}

.sr-22 {
  --red: #ff0066;
  --red2: #cc0044;
  --cyan: #00ffcc;
  --yellow: #ffe600;
  --bg: #050005;
  --bg-card: #0a000a;
  --text: #fff;
  --text-muted: #440033;
  --border: rgba(255,0,102,0.12);
  font-family: 'SF Mono', 'Fira Code', 'Courier New', monospace;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

.sr-22__card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 32px 36px;
  max-width: 480px;
  width: 100%;
  position: relative;
  overflow: hidden;
  box-shadow: 0 0 80px rgba(255,0,102,0.06), 0 30px 80px rgba(0,0,0,0.98);
}
/* Scanline flicker */

.sr-22__card::after {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
      0deg, transparent, transparent 3px, rgba(255,0,102,0.02) 4px
    );
  pointer-events: none;
  z-index: 0;
  animation: sr-22-scanflick 8s linear infinite;
}

@keyframes sr-22-scanflick {
  0%,
    98% {
    opacity: 1;
  }

  99% {
    opacity: 0.6;
  }

  100% {
    opacity: 1;
  }
}

.sr-22__inner {
  position: relative;
  z-index: 1;
}
/* Top bar */

.sr-22__topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(255,0,102,0.1);
}

.sr-22__sys {
  font-size: 0.62rem;
  color: var(--red);
  letter-spacing: 2px;
  opacity: 0.6;
}

.sr-22__err {
  font-size: 0.62rem;
  color: var(--yellow);
  letter-spacing: 1px;
  animation: sr-22-blink 2s step-end infinite;
}

@keyframes sr-22-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0;
  }
}
/* Giant glitch score display */

.sr-22__score-display {
  text-align: center;
  margin-bottom: 28px;
  min-height: 120px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
}

.sr-22__score-main {
  font-size: 7rem;
  font-weight: 900;
  line-height: 1;
  color: var(--text);
  position: relative;
  display: inline-block;
  transition: color 0.1s;
}
/* Glitch layers */

.sr-22__score-main::before,
.sr-22__score-main::after {
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  font-size: inherit;
  font-weight: inherit;
  line-height: inherit;
}

.sr-22__score-main::before {
  color: var(--cyan);
  clip-path: inset(0 0 70% 0);
  transform: translateX(-3px);
  opacity: 0;
}

.sr-22__score-main::after {
  color: var(--red);
  clip-path: inset(60% 0 0 0);
  transform: translateX(3px);
  opacity: 0;
}

.sr-22__score-main.glitching::before {
  animation: sr-22-glitch-top 0.6s steps(4) forwards;
}

.sr-22__score-main.glitching::after {
  animation: sr-22-glitch-bot 0.6s steps(4) forwards;
}

.sr-22__score-main.glitching {
  animation: sr-22-shake 0.6s steps(4) forwards;
}

@keyframes sr-22-glitch-top {
  0% {
    clip-path: inset(0 0 80% 0);
    transform: translateX(-8px);
    opacity: 1;
  }

  25% {
    clip-path: inset(10% 0 60% 0);
    transform: translateX(6px);
  }

  50% {
    clip-path: inset(30% 0 40% 0);
    transform: translateX(-4px);
  }

  75% {
    clip-path: inset(50% 0 20% 0);
    transform: translateX(2px);
  }

  100% {
    clip-path: inset(0);
    transform: translateX(0);
    opacity: 0;
  }
}

@keyframes sr-22-glitch-bot {
  0% {
    clip-path: inset(70% 0 0 0);
    transform: translateX(8px);
    opacity: 1;
  }

  25% {
    clip-path: inset(50% 0 10% 0);
    transform: translateX(-6px);
  }

  50% {
    clip-path: inset(30% 0 30% 0);
    transform: translateX(4px);
  }

  75% {
    clip-path: inset(10% 0 50% 0);
    transform: translateX(-2px);
  }

  100% {
    clip-path: inset(0);
    transform: translateX(0);
    opacity: 0;
  }
}

@keyframes sr-22-shake {
  0% {
    transform: translate(-4px, -2px);
  }

  20% {
    transform: translate(4px, 2px);
  }

  40% {
    transform: translate(-2px, 4px);
  }

  60% {
    transform: translate(2px, -4px);
  }

  80% {
    transform: translate(-1px, 1px);
  }

  100% {
    transform: translate(0, 0);
  }
}

.sr-22__score-label {
  font-size: 0.65rem;
  letter-spacing: 3px;
  color: var(--red);
  text-transform: uppercase;
  margin-top: 4px;
  opacity: 0.6;
}
/* Corruption bars (horizontal noise) */

.sr-22__noise-bars {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
  opacity: 0;
}

.sr-22__noise-bars.active {
  opacity: 1;
  animation: sr-22-noise-fade 0.8s ease forwards;
}

@keyframes sr-22-noise-fade {
  0% {
    opacity: 1;
  }

  100% {
    opacity: 0;
  }
}

.sr-22__noise-bar {
  position: absolute;
  left: 0;
  right: 0;
  height: 3px;
  animation: sr-22-noise-slide 0.2s steps(1) infinite;
}

@keyframes sr-22-noise-slide {
  0% {
    transform: translateX(-5%);
    background: rgba(0,255,204,0.3);
  }

  33% {
    transform: translateX(5%);
    background: rgba(255,0,102,0.3);
  }

  66% {
    transform: translateX(-3%);
    background: rgba(255,230,0,0.2);
  }

  100% {
    transform: translateX(2%);
    background: rgba(0,255,204,0.15);
  }
}
/* Input grid */

.sr-22__inputs {
  display: grid;
  grid-template-columns: repeat(5,1fr);
  gap: 6px;
  margin-bottom: 20px;
}

.sr-22__inputs input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-22__input-btn {
  display: block;
  text-align: center;
  padding: 12px 4px;
  border: 1px solid rgba(255,0,102,0.15);
  border-radius: 2px;
  cursor: pointer;
  font-size: 0.65rem;
  letter-spacing: 1px;
  color: var(--text-muted);
  text-transform: uppercase;
  transition: all 0.2s;
  position: relative;
  overflow: hidden;
}

.sr-22__input-btn:hover {
  border-color: rgba(255,0,102,0.4);
  color: var(--red);
  background: rgba(255,0,102,0.04);
}

.sr-22__inputs input:checked + .sr-22__input-btn {
  border-color: var(--red);
  color: var(--red);
  background: rgba(255,0,102,0.08);
  box-shadow: 0 0 16px rgba(255,0,102,0.2), inset 0 0 10px rgba(255,0,102,0.04);
}
/* Sweep glow on active */

.sr-22__inputs input:checked + .sr-22__input-btn::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(255,0,102,0.1), transparent);
  animation: sr-22-sweep-btn 1.2s ease-in-out infinite;
}

@keyframes sr-22-sweep-btn {
  0%,
    100% {
    transform: translateY(-100%);
  }

  50% {
    transform: translateY(100%);
  }
}

.sr-22__btn-num {
  display: block;
  font-size: 1.2rem;
  font-weight: 900;
  margin-bottom: 2px;
  color: inherit;
}
/* Status line */

.sr-22__status {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 16px;
}

.sr-22__status-indicator {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--text-muted);
  transition: background 0.3s, box-shadow 0.3s;
}

.sr-22__status-indicator.online {
  background: var(--red);
  box-shadow: 0 0 8px var(--red);
  animation: sr-22-blink 1s step-end infinite;
}

.sr-22__status-text {
  font-size: 0.62rem;
  color: var(--text-muted);
  letter-spacing: 1px;
  transition: color 0.3s;
}

.sr-22__status-text.active {
  color: var(--red);
}
/* Submit */

.sr-22__footer {
  display: flex;
  gap: 8px;
}

.sr-22__btn {
  flex: 1;
  padding: 11px;
  border-radius: 2px;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  cursor: pointer;
  border: 1px solid;
  transition: all 0.2s;
  font-family: inherit;
}

.sr-22__btn--primary {
  background: var(--red);
  border-color: var(--red);
  color: #fff;
  box-shadow: 0 0 20px rgba(255,0,102,0.3);
}

.sr-22__btn--primary:hover {
  background: var(--red2);
  box-shadow: 0 0 30px rgba(255,0,102,0.4);
}

.sr-22__btn--ghost {
  background: transparent;
  border-color: rgba(255,0,102,0.15);
  color: var(--text-muted);
}

.sr-22__btn--ghost:hover {
  border-color: rgba(255,0,102,0.4);
  color: var(--red);
}

@media (prefers-reduced-motion: reduce) {
  .sr-22__score-main.glitching,
    .sr-22__score-main.glitching::before,
    .sr-22__score-main.glitching::after,
    .sr-22__noise-bars.active,
    .sr-22__card::after {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  const scoreEl = document.getElementById('sr-22-score');
  const lblEl   = document.getElementById('sr-22-score-lbl');
  const dotEl   = document.getElementById('sr-22-dot');
  const statusEl= document.getElementById('sr-22-status');
  const noiseEl = document.getElementById('sr-22-noise');

  const glitchChars = '!@#$%^&*01Ω∆ΨΦ░▒▓';
  const statuses = [
    '// error: signal null',
    '// warning: low coherence',
    '// info: signal synced',
    '// ok: lock acquired',
    '// excellent: max signal',
  ];

  function randomChar(){ return glitchChars[Math.floor(Math.random()*glitchChars.length)]; }

  function glitchIn(finalVal, finalLabel){
    if(!scoreEl) return;

    // Trigger noise bars
    if(noiseEl){
      noiseEl.classList.remove('active');
      void noiseEl.offsetWidth;
      noiseEl.classList.add('active');
    }

    // Trigger shake
    scoreEl.classList.remove('glitching');
    void scoreEl.offsetWidth;
    scoreEl.classList.add('glitching');

    // Scramble for 500ms then resolve
    let iterations = 0;
    const total = 14;
    const interval = setInterval(()=>{
      if(iterations < total){
        scoreEl.textContent = randomChar();
        scoreEl.setAttribute('data-text', randomChar());
        iterations++;
      } else {
        clearInterval(interval);
        scoreEl.textContent = finalVal;
        scoreEl.setAttribute('data-text', finalVal);
        if(lblEl) lblEl.textContent = finalLabel;
      }
    }, 40);
  }

  const labels = ['Signal null','Low coherence','Synced','Lock acquired','Max signal — optimal'];

  document.querySelectorAll('input[name="sr-22-g"]').forEach((inp,i)=>{
    inp.addEventListener('change',()=>{
      glitchIn(String(i+1), labels[i]);
      if(dotEl) { dotEl.classList.add('online'); }
      if(statusEl){ statusEl.textContent = statuses[i]; statusEl.classList.add('active'); }
    });
  });
})();
```
