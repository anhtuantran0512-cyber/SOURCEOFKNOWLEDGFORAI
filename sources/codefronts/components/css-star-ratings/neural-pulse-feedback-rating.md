---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/neural-pulse-feedback-rating/"
title: "Neural Pulse Feedback Rating"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A Canvas-rendered multi-harmonic brainwave that morphs frequency, amplitude, color, and waveform complexity in real-time as you switch between Flatline,…"
has_js: "true"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neural Pulse Feedback Rating
Source: https://codefronts.com/components/css-star-ratings/neural-pulse-feedback-rating/

A Canvas-rendered multi-harmonic brainwave that morphs frequency, amplitude, color, and waveform complexity in real-time as you switch between Flatline, Delta, Theta, Alpha, and Gamma burst rating levels.
## HTML
```html
<div class="sr-17">
  <div class="sr-17__card">
    <div class="sr-17__inner">
      <div class="sr-17__top">
        <div>
          <div class="sr-17__eyebrow">Neural Feedback Interface</div>
          <div class="sr-17__title">Cognitive Response Rating</div>
        </div>
        <div class="sr-17__live-badge">
          <div class="sr-17__live-dot"></div>LIVE
        </div>
      </div>

      <!-- Neural wave display -->
      <div class="sr-17__wave-wrap">
        <canvas class="sr-17__wave-canvas" id="sr-17-canvas"></canvas>
      </div>

      <!-- Node selector -->
      <div class="sr-17__selector">
        <input type="radio" id="sr-17-n1" name="sr-17-n" value="1">
        <label for="sr-17-n1" class="sr-17__node">
          <div class="sr-17__node-circle">1</div>
          <span class="sr-17__node-label">Flat<br>line</span>
        </label>

        <input type="radio" id="sr-17-n2" name="sr-17-n" value="2">
        <label for="sr-17-n2" class="sr-17__node">
          <div class="sr-17__node-circle">2</div>
          <span class="sr-17__node-label">Delta<br>wave</span>
        </label>

        <input type="radio" id="sr-17-n3" name="sr-17-n" value="3">
        <label for="sr-17-n3" class="sr-17__node">
          <div class="sr-17__node-circle">3</div>
          <span class="sr-17__node-label">Theta<br>wave</span>
        </label>

        <input type="radio" id="sr-17-n4" name="sr-17-n" value="4">
        <label for="sr-17-n4" class="sr-17__node">
          <div class="sr-17__node-circle">4</div>
          <span class="sr-17__node-label">Alpha<br>wave</span>
        </label>

        <input type="radio" id="sr-17-n5" name="sr-17-n" value="5">
        <label for="sr-17-n5" class="sr-17__node">
          <div class="sr-17__node-circle">5</div>
          <span class="sr-17__node-label">Gamma<br>burst</span>
        </label>
      </div>

      <div class="sr-17__stats">
        <div class="sr-17__stat">
          <span class="sr-17__stat-val" id="sr-17-hz">—</span>
          <span class="sr-17__stat-key">Freq Hz</span>
        </div>
        <div class="sr-17__stat">
          <span class="sr-17__stat-val" id="sr-17-amp">—</span>
          <span class="sr-17__stat-key">Amplitude</span>
        </div>
        <div class="sr-17__stat">
          <span class="sr-17__stat-val" id="sr-17-coh">—</span>
          <span class="sr-17__stat-key">Coherence</span>
        </div>
      </div>

      <div class="sr-17__actions">
        <button class="sr-17__btn sr-17__btn--primary">Encode Signal</button>
        <button class="sr-17__btn sr-17__btn--ghost">Reset</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sr-17,
.sr-17 *,
.sr-17 *::before,
.sr-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-17 ::selection {
  background: #a855f7;
  color: #fff;
}

.sr-17 {
  --violet: #a855f7;
  --violet2: #7c3aed;
  --pink: #ec4899;
  --bg: #05020a;
  --bg-card: #080514;
  --text: #f0e6ff;
  --text-muted: #5a4080;
  --border: rgba(168,85,247,0.12);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

.sr-17__card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 32px 36px 28px;
  max-width: 500px;
  width: 100%;
  position: relative;
  overflow: hidden;
  box-shadow: 0 0 80px rgba(168,85,247,0.06), 0 30px 80px rgba(0,0,0,0.9);
}
/* Radial aurora bg */

.sr-17__card::before {
  content: '';
  position: absolute;
  inset: -50%;
  background: radial-gradient(ellipse at 50% 0%, rgba(168,85,247,0.08) 0%, transparent 60%);
  pointer-events: none;
  animation: sr-17-aurora 6s ease-in-out infinite;
}

@keyframes sr-17-aurora {
  0%,
    100% {
    transform: scaleX(1) translateY(0);
    opacity: 0.5;
  }

  50% {
    transform: scaleX(1.3) translateY(-10%);
    opacity: 1;
  }
}

.sr-17__inner {
  position: relative;
  z-index: 1;
}

.sr-17__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 20px;
}

.sr-17__eyebrow {
  font-size: 0.65rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--violet);
  opacity: 0.7;
  margin-bottom: 6px;
}

.sr-17__title {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--text);
}

.sr-17__live-badge {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.65rem;
  font-weight: 700;
  color: var(--pink);
  background: rgba(236,72,153,0.1);
  border: 1px solid rgba(236,72,153,0.2);
  border-radius: 20px;
  padding: 4px 10px;
  letter-spacing: 1px;
}

.sr-17__live-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--pink);
  animation: sr-17-pulse-dot 1s ease-in-out infinite;
}

@keyframes sr-17-pulse-dot {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(1.5);
    opacity: 0.5;
  }
}
/* Neural wave canvas area */

.sr-17__wave-wrap {
  position: relative;
  height: 100px;
  margin-bottom: 24px;
  border-bottom: 1px solid var(--border);
}

.sr-17__wave-canvas {
  width: 100%;
  height: 100%;
}
/* Y-axis labels */

.sr-17__y-labels {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  pointer-events: none;
}

.sr-17__y-label {
  font-size: 0.55rem;
  color: var(--text-muted);
  font-family: 'SF Mono', monospace;
}
/* Intensity selector */

.sr-17__selector {
  display: flex;
  gap: 10px;
  justify-content: center;
  margin-bottom: 24px;
}

.sr-17__selector input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-17__node {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  cursor: pointer;
}

.sr-17__node-circle {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: 2px solid rgba(168,85,247,0.2);
  background: rgba(168,85,247,0.04);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.9rem;
  font-weight: 800;
  color: var(--text-muted);
  transition: all 0.3s cubic-bezier(.34,1.56,.64,1);
  position: relative;
}

.sr-17__node-circle::after {
  content: '';
  position: absolute;
  inset: -4px;
  border-radius: 50%;
  border: 1px solid transparent;
  transition: all 0.3s;
}

.sr-17__selector input:checked + .sr-17__node .sr-17__node-circle {
  border-color: var(--violet);
  background: rgba(168,85,247,0.15);
  color: var(--violet);
  box-shadow: 0 0 20px rgba(168,85,247,0.3), 0 0 40px rgba(168,85,247,0.1);
  transform: scale(1.15);
}

.sr-17__selector input:checked + .sr-17__node .sr-17__node-circle::after {
  border-color: rgba(168,85,247,0.3);
  animation: sr-17-ring-pulse 1.5s ease-out infinite;
}

@keyframes sr-17-ring-pulse {
  0% {
    transform: scale(1);
    opacity: 1;
  }

  100% {
    transform: scale(1.6);
    opacity: 0;
  }
}

.sr-17__node-label {
  font-size: 0.62rem;
  color: var(--text-muted);
  text-align: center;
  letter-spacing: 0.5px;
  transition: color 0.2s;
  line-height: 1.2;
}

.sr-17__selector input:checked + .sr-17__node .sr-17__node-label {
  color: var(--violet);
}
/* Stats row */

.sr-17__stats {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 12px;
  margin-bottom: 20px;
}

.sr-17__stat {
  background: rgba(168,85,247,0.04);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 10px 12px;
  text-align: center;
}

.sr-17__stat-val {
  font-size: 1.3rem;
  font-weight: 900;
  color: var(--violet);
  display: block;
  margin-bottom: 2px;
  transition: all 0.4s;
}

.sr-17__stat-key {
  font-size: 0.6rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.sr-17__actions {
  display: flex;
  gap: 10px;
}

.sr-17__btn {
  flex: 1;
  padding: 12px;
  border-radius: 10px;
  font-size: 0.82rem;
  font-weight: 700;
  cursor: pointer;
  border: none;
  transition: all 0.2s;
}

.sr-17__btn--primary {
  background: linear-gradient(135deg, var(--violet2), var(--violet));
  color: #fff;
  box-shadow: 0 4px 20px rgba(168,85,247,0.3);
}

.sr-17__btn--primary:hover {
  opacity: 0.9;
  transform: translateY(-1px);
}

.sr-17__btn--ghost {
  background: transparent;
  color: var(--text-muted);
  border: 1px solid var(--border);
}

.sr-17__btn--ghost:hover {
  border-color: var(--violet);
  color: var(--violet);
}

@media (prefers-reduced-motion: reduce) {
  .sr-17__card::before,
    .sr-17__live-dot {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  const canvas = document.getElementById('sr-17-canvas');
  if(!canvas) return;
  const ctx = canvas.getContext('2d');

  // Level configs: [frequency, amplitude, speed, color]
  const levels = [
    { freq: 0.5,  amp: 2,  speed: 0.02, color: '#5a4080', hz: '0.5',  ampLabel: '2µV',   coh: '12%' },
    { freq: 2,    amp: 10, speed: 0.04, color: '#7c3aed', hz: '2.4',  ampLabel: '10µV',  coh: '34%' },
    { freq: 5,    amp: 22, speed: 0.06, color: '#a855f7', hz: '5.8',  ampLabel: '22µV',  coh: '58%' },
    { freq: 10,   amp: 34, speed: 0.09, color: '#c084fc', hz: '10.2', ampLabel: '34µV',  coh: '79%' },
    { freq: 40,   amp: 46, speed: 0.16, color: '#ec4899', hz: '40.0', ampLabel: '46µV',  coh: '99%' },
  ];

  let currentLevel = 1; // index
  let targetLevel  = 1;
  let blendFactor  = 0;
  let phase = 0;
  let raf;

  function resize(){
    const rect = canvas.parentElement.getBoundingClientRect();
    canvas.width  = rect.width;
    canvas.height = rect.height || 100;
  }
  resize();
  window.addEventListener('resize', resize);

  function lerp(a,b,t){ return a+(b-a)*t; }

  function drawWave(t){
    const W = canvas.width, H = canvas.height;
    ctx.clearRect(0,0,W,H);

    const cur  = levels[currentLevel];
    const tgt  = levels[targetLevel];
    blendFactor = Math.min(blendFactor + 0.03, 1);

    const freq  = lerp(cur.freq,  tgt.freq,  blendFactor);
    const amp   = lerp(cur.amp,   tgt.amp,   blendFactor);
    const speed = lerp(cur.speed, tgt.speed, blendFactor);

    // Interpolate color
    function hexToRgb(h){
      const r = parseInt(h.slice(1,3),16), g=parseInt(h.slice(3,5),16), b=parseInt(h.slice(5,7),16);
      return [r,g,b];
    }
    const [r1,g1,b1] = hexToRgb(cur.color);
    const [r2,g2,b2] = hexToRgb(tgt.color);
    const rc = Math.round(lerp(r1,r2,blendFactor));
    const gc = Math.round(lerp(g1,g2,blendFactor));
    const bc = Math.round(lerp(b1,b2,blendFactor));
    const color = `rgb(${rc},${gc},${bc})`;
    const colorGlow = `rgba(${rc},${gc},${bc},0.3)`;

    phase += speed;

    // Draw subtle grid lines
    ctx.strokeStyle = 'rgba(168,85,247,0.05)';
    ctx.lineWidth = 1;
    for(let y = H/4; y < H; y += H/4){
      ctx.beginPath(); ctx.moveTo(0,y); ctx.lineTo(W,y); ctx.stroke();
    }

    // Draw glow trail
    ctx.beginPath();
    ctx.lineWidth = 6;
    ctx.strokeStyle = colorGlow;
    for(let x=0; x<=W; x++){
      const t2 = x/W;
      // Multi-harmonic: main + overtone
      const y = H/2
        - Math.sin(t2 * freq * Math.PI * 2 + phase) * amp
        - Math.sin(t2 * freq * Math.PI * 4 + phase*1.3) * amp*0.3
        - Math.sin(t2 * freq * Math.PI * 0.5 + phase*0.7) * amp*0.5;
      x===0 ? ctx.moveTo(x,y) : ctx.lineTo(x,y);
    }
    ctx.stroke();

    // Draw sharp line on top
    ctx.beginPath();
    ctx.lineWidth = 2;
    ctx.strokeStyle = color;
    ctx.shadowColor = color;
    ctx.shadowBlur = 8;
    for(let x=0; x<=W; x++){
      const t2 = x/W;
      const y = H/2
        - Math.sin(t2 * freq * Math.PI * 2 + phase) * amp
        - Math.sin(t2 * freq * Math.PI * 4 + phase*1.3) * amp*0.3
        - Math.sin(t2 * freq * Math.PI * 0.5 + phase*0.7) * amp*0.5;
      x===0 ? ctx.moveTo(x,y) : ctx.lineTo(x,y);
    }
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Scan dot at the tip (right edge)
    const tipX = W;
    const tipY = H/2
      - Math.sin(freq*Math.PI*2+phase)*amp
      - Math.sin(freq*Math.PI*4+phase*1.3)*amp*0.3
      - Math.sin(freq*Math.PI*0.5+phase*0.7)*amp*0.5;

    ctx.beginPath();
    ctx.arc(tipX, tipY, 4, 0, Math.PI*2);
    ctx.fillStyle = color;
    ctx.shadowColor = color; ctx.shadowBlur = 14;
    ctx.fill();
    ctx.shadowBlur = 0;

    raf = requestAnimationFrame(drawWave);
  }

  drawWave();

  // Radio change
  document.querySelectorAll('input[name="sr-17-n"]').forEach((inp,i)=>{
    inp.addEventListener('change',()=>{
      currentLevel = targetLevel;
      targetLevel  = i;
      blendFactor  = 0;

      const lv = levels[i];
      document.getElementById('sr-17-hz').textContent  = lv.hz;
      document.getElementById('sr-17-amp').textContent = lv.ampLabel;
      document.getElementById('sr-17-coh').textContent = lv.coh;
    });
  });
})();
```
