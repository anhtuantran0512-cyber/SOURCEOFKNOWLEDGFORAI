---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/magnetic-field-lines-rating/"
title: "Magnetic Field Lines Rating"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A Canvas-rendered dipole magnetic field where field line density, curvature, and color intensity increase with the selected rating level — driven by real…"
has_js: "true"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magnetic Field Lines Rating
Source: https://codefronts.com/components/css-star-ratings/magnetic-field-lines-rating/

A Canvas-rendered dipole magnetic field where field line density, curvature, and color intensity increase with the selected rating level — driven by real dipole field line integration mathematics.
## HTML
```html
<div class="sr-18">
  <div class="sr-18__card">
    <div class="sr-18__header">
      <span class="sr-18__label">Magnetic Field Intensity</span>
      <span class="sr-18__reading">B = <span id="sr-18-tesla">0.00</span> T</span>
    </div>

    <!-- Canvas for magnetic field lines -->
    <div class="sr-18__field-wrap">
      <canvas class="sr-18__field-canvas" id="sr-18-canvas"></canvas>
      <div class="sr-18__field-overlay" id="sr-18-overlay">SELECT INTENSITY</div>
    </div>

    <!-- Slider controls -->
    <div class="sr-18__controls">
      <div class="sr-18__controls-label">Drag to set field strength</div>
      <div class="sr-18__slider-row">
        <div class="sr-18__radios" id="sr-18-radios">
          <div class="sr-18__track">
            <div class="sr-18__track-fill" id="sr-18-fill"></div>
          </div>
          <!-- Notch dots anchored to 0/25/50/75/100% — same
               coordinate space as the thumb and the tier labels
               below, so all three layers line up visually. -->
          <span class="sr-18__seg-notch" data-pos="1"></span>
          <span class="sr-18__seg-notch" data-pos="2"></span>
          <span class="sr-18__seg-notch" data-pos="3"></span>
          <span class="sr-18__seg-notch" data-pos="4"></span>
          <span class="sr-18__seg-notch" data-pos="5"></span>
          <div class="sr-18__thumb" id="sr-18-thumb"></div>

          <input type="radio" id="sr-18-v1" name="sr-18-mag" value="1">
          <label for="sr-18-v1" class="sr-18__radio-seg"></label>

          <input type="radio" id="sr-18-v2" name="sr-18-mag" value="2">
          <label for="sr-18-v2" class="sr-18__radio-seg"></label>

          <input type="radio" id="sr-18-v3" name="sr-18-mag" value="3">
          <label for="sr-18-v3" class="sr-18__radio-seg"></label>

          <input type="radio" id="sr-18-v4" name="sr-18-mag" value="4">
          <label for="sr-18-v4" class="sr-18__radio-seg"></label>

          <input type="radio" id="sr-18-v5" name="sr-18-mag" value="5">
          <label for="sr-18-v5" class="sr-18__radio-seg"></label>
        </div>
        <div class="sr-18__slider-val" id="sr-18-val">—</div>
      </div>
    </div>

    <div class="sr-18__tiers" id="sr-18-tiers">
      <span class="sr-18__tier-item">Weak</span>
      <span class="sr-18__tier-item">Faint</span>
      <span class="sr-18__tier-item">Moderate</span>
      <span class="sr-18__tier-item">Strong</span>
      <span class="sr-18__tier-item">Extreme</span>
    </div>

    <div class="sr-18__submit-row">
      <button class="sr-18__btn sr-18__btn--primary">Log Reading</button>
      <button class="sr-18__btn sr-18__btn--ghost">Reset</button>
    </div>
  </div>
</div>
```
## CSS
```css
.sr-18,
.sr-18 *,
.sr-18 *::before,
.sr-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-18 ::selection {
  background: #f97316;
  color: #000;
}

.sr-18 {
  --fire: #f97316;
  --fire2: #ef4444;
  --fire3: #fbbf24;
  --bg: #0a0500;
  --bg-card: #0d0800;
  --text: #fff3e0;
  --text-muted: #7a5030;
  --border: rgba(249,115,22,0.12);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

.sr-18__card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 28px 32px 28px;
  max-width: 480px;
  width: 100%;
  box-shadow: 0 0 80px rgba(249,115,22,0.05), 0 30px 80px rgba(0,0,0,0.9);
  position: relative;
  overflow: hidden;
}
/* Ambient heat haze */

.sr-18__card::before {
  content: '';
  position: absolute;
  bottom: -30px;
  left: 50%;
  transform: translateX(-50%);
  width: 60%;
  height: 60px;
  background: radial-gradient(ellipse, rgba(249,115,22,0.12), transparent 70%);
  pointer-events: none;
  animation: sr-18-haze 3s ease-in-out infinite;
}

@keyframes sr-18-haze {
  0%,
    100% {
    transform: translateX(-50%) scaleX(0.8);
    opacity: 0.5;
  }

  50% {
    transform: translateX(-50%) scaleX(1.2);
    opacity: 1;
  }
}

.sr-18__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.sr-18__label {
  font-size: 0.65rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--fire);
  opacity: 0.6;
}

.sr-18__reading {
  font-size: 0.7rem;
  color: var(--text-muted);
  font-family: monospace;
}

.sr-18__reading span {
  color: var(--fire3);
}
/* Canvas field viz */

.sr-18__field-wrap {
  position: relative;
  height: 180px;
  margin-bottom: 24px;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid rgba(249,115,22,0.08);
}

.sr-18__field-canvas {
  width: 100%;
  height: 100%;
  display: block;
}
/* Intensity label overlay */

.sr-18__field-overlay {
  position: absolute;
  bottom: 10px;
  right: 12px;
  font-size: 0.65rem;
  color: rgba(249,115,22,0.5);
  font-family: monospace;
  pointer-events: none;
}
/* Rating controls */

.sr-18__controls {
  margin-bottom: 20px;
}

.sr-18__controls-label {
  font-size: 0.7rem;
  color: var(--text-muted);
  margin-bottom: 10px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.sr-18__slider-row {
  display: flex;
  align-items: center;
  gap: 12px;
}
/* Hidden radios driving the slider illusion */

.sr-18__radios {
  display: flex;
  gap: 0;
  flex: 1;
  position: relative;
}

.sr-18__radios input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-18__radio-seg {
  flex: 1;
  height: 44px;
  cursor: pointer;
  position: relative;
}
/* Track */

.sr-18__track {
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  height: 4px;
  background: rgba(249,115,22,0.1);
  transform: translateY(-50%);
  border-radius: 2px;
  pointer-events: none;
}

.sr-18__track-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--fire2), var(--fire), var(--fire3));
  border-radius: 2px;
  width: 0%;
  transition: width 0.4s cubic-bezier(.34,1.2,.64,1);
  box-shadow: 0 0 8px rgba(249,115,22,0.5);
}
/* Thumb dot */

.sr-18__thumb {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--fire);
  border: 2px solid #fff;
  box-shadow: 0 0 14px rgba(249,115,22,0.7);
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  left: 0%;
  margin-left: -10px;
  transition: left 0.4s cubic-bezier(.34,1.2,.64,1);
  pointer-events: none;
  z-index: 2;
}
/* Notch dots — absolutely positioned at 0/25/50/75/100% so they
   share the same coordinate space as the thumb (which JS animates
   to those exact percentages) and the tier labels below (which
   use justify-content: space-between, hitting the same edges).
   translate(-50%, -50%) centres each dot on its anchor point. */

.sr-18__seg-notch {
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: rgba(249,115,22,0.3);
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  z-index: 1;
  pointer-events: none;
  transition: background 0.2s, transform 0.2s;
}

.sr-18__seg-notch[data-pos="1"] {
  left: 0%;
}

.sr-18__seg-notch[data-pos="2"] {
  left: 25%;
}

.sr-18__seg-notch[data-pos="3"] {
  left: 50%;
}

.sr-18__seg-notch[data-pos="4"] {
  left: 75%;
}

.sr-18__seg-notch[data-pos="5"] {
  left: 100%;
}
/* Active-notch highlight driven by the selected radio. Uses
   :has() on the parent because notches are siblings BEFORE the
   inputs in the DOM (the ~ general sibling combinator only matches
   forward, so :has() is required to look backwards from radio to
   notch). Supported everywhere modern (Chrome 105+, Safari 15.4+,
   Firefox 121+). */

.sr-18__radios:has(input#sr-18-v1:checked) .sr-18__seg-notch[data-pos="1"],
.sr-18__radios:has(input#sr-18-v2:checked) .sr-18__seg-notch[data-pos="2"],
.sr-18__radios:has(input#sr-18-v3:checked) .sr-18__seg-notch[data-pos="3"],
.sr-18__radios:has(input#sr-18-v4:checked) .sr-18__seg-notch[data-pos="4"],
.sr-18__radios:has(input#sr-18-v5:checked) .sr-18__seg-notch[data-pos="5"] {
  background: var(--fire);
  transform: translate(-50%, -50%) scale(1.5);
}

.sr-18__slider-val {
  font-size: 1.4rem;
  font-weight: 900;
  color: var(--fire);
  text-shadow: 0 0 20px rgba(249,115,22,0.5);
  min-width: 28px;
  text-align: right;
  transition: all 0.3s;
}
/* Tier labels */

.sr-18__tiers {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
  padding: 0 4px;
}

.sr-18__tier-item {
  text-align: center;
  font-size: 0.62rem;
  color: var(--text-muted);
  transition: color 0.2s;
}

.sr-18__tier-item.active {
  color: var(--fire);
}
/* Submit row */

.sr-18__submit-row {
  display: flex;
  gap: 10px;
}

.sr-18__btn {
  flex: 1;
  padding: 12px;
  border-radius: 10px;
  font-size: 0.84rem;
  font-weight: 700;
  cursor: pointer;
  border: none;
  transition: all 0.2s;
}

.sr-18__btn--primary {
  background: linear-gradient(135deg, var(--fire2), var(--fire));
  color: #fff;
  box-shadow: 0 4px 20px rgba(249,115,22,0.3);
}

.sr-18__btn--primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 28px rgba(249,115,22,0.4);
}

.sr-18__btn--ghost {
  background: transparent;
  color: var(--text-muted);
  border: 1px solid var(--border);
}

@media (prefers-reduced-motion: reduce) {
  .sr-18__card::before {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  const canvas = document.getElementById('sr-18-canvas');
  if(!canvas) return;
  const ctx = canvas.getContext('2d');

  let currentStrength = 0;
  let targetStrength  = 0;
  let raf;

  function resize(){
    const p = canvas.parentElement;
    canvas.width  = p.offsetWidth;
    canvas.height = p.offsetHeight;
  }
  resize();
  window.addEventListener('resize',resize);

  function lerp(a,b,t){ return a+(b-a)*t; }

  function drawField(strength){
    const W = canvas.width, H = canvas.height;
    ctx.clearRect(0,0,W,H);

    if(strength < 0.01) return;

    // Two poles: left and right of center
    const poles = [
      { x: W*0.3, y: H*0.5, polarity:  1 },
      { x: W*0.7, y: H*0.5, polarity: -1 },
    ];

    const lineCount = Math.floor(6 + strength * 10);
    const colors = [
      [239,68,68],   // level 1
      [249,115,22],  // level 2
      [251,191,36],  // level 3
      [249,115,22],  // level 4
      [239,68,68],   // level 5
    ];
    const ci = Math.min(Math.floor(strength * 4.99), 4);
    const [r,g,b] = colors[ci];

    // Draw field lines from positive pole
    for(let k=0; k<lineCount; k++){
      const angle = (k / lineCount) * Math.PI * 2;
      const px = poles[0].x, py = poles[0].y;

      ctx.beginPath();
      let x = px + Math.cos(angle)*8;
      let y = py + Math.sin(angle)*8;
      ctx.moveTo(x,y);

      const alpha = 0.15 + strength*0.5;
      ctx.strokeStyle = `rgba(${r},${g},${b},${Math.min(alpha,0.85)})`;
      ctx.lineWidth = 0.8 + strength*0.8;
      ctx.shadowColor = `rgb(${r},${g},${b})`;
      ctx.shadowBlur = 2 + strength*4;

      // Field line integration
      for(let step=0; step<200; step++){
        let fx=0, fy=0;
        for(const pole of poles){
          const dx = x - pole.x, dy = y - pole.y;
          const dist2 = dx*dx + dy*dy;
          const dist  = Math.sqrt(dist2)+0.01;
          const force = pole.polarity / dist2;
          fx += force * dx/dist;
          fy += force * dy/dist;
        }
        const mag = Math.sqrt(fx*fx+fy*fy)+0.001;
        const stepSize = 2 + strength*2;
        x += (fx/mag)*stepSize;
        y += (fy/mag)*stepSize;

        // Stop if out of bounds or near negative pole
        if(x<0||x>W||y<0||y>H) break;
        const dx2=x-poles[1].x, dy2=y-poles[1].y;
        if(dx2*dx2+dy2*dy2<100) break;

        ctx.lineTo(x,y);
      }
      ctx.stroke();
    }
    ctx.shadowBlur = 0;

    // Draw pole markers
    for(const pole of poles){
      const grad = ctx.createRadialGradient(pole.x, pole.y, 0, pole.x, pole.y, 14*strength+6);
      grad.addColorStop(0, `rgba(${r},${g},${b},0.9)`);
      grad.addColorStop(1, 'transparent');
      ctx.beginPath();
      ctx.arc(pole.x, pole.y, 6, 0, Math.PI*2);
      ctx.fillStyle = grad;
      ctx.fill();
      ctx.beginPath();
      ctx.arc(pole.x, pole.y, 4, 0, Math.PI*2);
      ctx.fillStyle = `rgb(${r},${g},${b})`;
      ctx.fill();
    }
  }

  function tick(){
    currentStrength = lerp(currentStrength, targetStrength, 0.06);
    if(Math.abs(currentStrength - targetStrength) > 0.002){
      drawField(currentStrength);
      raf = requestAnimationFrame(tick);
    } else {
      currentStrength = targetStrength;
      drawField(currentStrength);
      raf = null;
    }
  }

  const teslaVals = ['0.12','0.48','1.20','3.50','9.40'];
  const overlays  = ['WEAK · 0.12T','FAINT · 0.48T','MODERATE · 1.2T','STRONG · 3.5T','EXTREME · 9.4T'];

  document.querySelectorAll('input[name="sr-18-mag"]').forEach((inp,i)=>{
    inp.addEventListener('change',()=>{
      targetStrength = (i+1)/5;

      // Thumb + fill
      const pct = (i/(5-1))*100;
      document.getElementById('sr-18-fill').style.width  = pct+'%';
      document.getElementById('sr-18-thumb').style.left  = pct+'%';
      document.getElementById('sr-18-val').textContent   = i+1;
      document.getElementById('sr-18-tesla').textContent = teslaVals[i];
      document.getElementById('sr-18-overlay').textContent = overlays[i];

      // Tier highlights
      document.querySelectorAll('.sr-18__tier-item').forEach((t,j)=>{
        t.classList.toggle('active', j===i);
      });

      if(!raf) raf = requestAnimationFrame(tick);
    });
  });
})();
```
