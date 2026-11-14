---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/dna-helix-strand-rating/"
title: "DNA Helix Strand Rating"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A rotating 3D helix of 10 base pairs animated by requestAnimationFrame using sin/cos for helical geometry — base pairs light up in sequence-coded colors…"
has_js: "true"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: DNA Helix Strand Rating
Source: https://codefronts.com/components/css-star-ratings/dna-helix-strand-rating/

A rotating 3D helix of 10 base pairs animated by requestAnimationFrame using sin/cos for helical geometry — base pairs light up in sequence-coded colors corresponding to the selected rating level.
## HTML
```html
<div class="sr-20">
  <div class="sr-20__card">
    <div class="sr-20__header">
      <div class="sr-20__title-group">
        <div class="sr-20__eyebrow">Genomic Rating Protocol</div>
        <div class="sr-20__title">DNA Sequence Score</div>
      </div>
      <div class="sr-20__score-badge">
        <span class="sr-20__badge-val" id="sr-20-bval">—</span>
        <span class="sr-20__badge-label">RATING</span>
      </div>
    </div>

    <!-- DNA Helix visual -->
    <div class="sr-20__helix-wrap">
      <div class="sr-20__helix" id="sr-20-helix">
        <div class="sr-20__strand sr-20__strand--left"></div>
        <div class="sr-20__strand sr-20__strand--right"></div>
        <!-- 10 base pairs — JS positions and lights them -->
      </div>
    </div>

    <!-- Level selector -->
    <div class="sr-20__controls">
      <div class="sr-20__ctrl-label">Select expression level</div>
      <div class="sr-20__strands">
        <input type="radio" id="sr-20-v1" name="sr-20-dna" value="1">
        <label for="sr-20-v1" class="sr-20__strand-btn">
          <span class="sr-20__strand-n">1</span>
          <span class="sr-20__strand-code">AT</span>
        </label>

        <input type="radio" id="sr-20-v2" name="sr-20-dna" value="2">
        <label for="sr-20-v2" class="sr-20__strand-btn">
          <span class="sr-20__strand-n">2</span>
          <span class="sr-20__strand-code">GC</span>
        </label>

        <input type="radio" id="sr-20-v3" name="sr-20-dna" value="3">
        <label for="sr-20-v3" class="sr-20__strand-btn">
          <span class="sr-20__strand-n">3</span>
          <span class="sr-20__strand-code">TA</span>
        </label>

        <input type="radio" id="sr-20-v4" name="sr-20-dna" value="4">
        <label for="sr-20-v4" class="sr-20__strand-btn">
          <span class="sr-20__strand-n">4</span>
          <span class="sr-20__strand-code">CG</span>
        </label>

        <input type="radio" id="sr-20-v5" name="sr-20-dna" value="5">
        <label for="sr-20-v5" class="sr-20__strand-btn">
          <span class="sr-20__strand-n">5</span>
          <span class="sr-20__strand-code">AA</span>
        </label>
      </div>
    </div>

    <div class="sr-20__sequence" id="sr-20-seq">
      5'— <span>· · · · · · · · · ·</span> —3'
    </div>

    <button class="sr-20__submit">Sequence &amp; Submit</button>
  </div>
</div>
```
## CSS
```css
.sr-20,
.sr-20 *,
.sr-20 *::before,
.sr-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-20 ::selection {
  background: #22d3ee;
  color: #000;
}

.sr-20 {
  --cyan: #22d3ee;
  --cyan2: #06b6d4;
  --emerald: #34d399;
  --rose: #f43f5e;
  --amber: #fbbf24;
  --violet: #a78bfa;
  --bg: #010c10;
  --bg-card: #021018;
  --text: #cffafe;
  --text-muted: #164e63;
  --border: rgba(34,211,238,0.1);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

.sr-20__card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 28px 32px;
  max-width: 480px;
  width: 100%;
  position: relative;
  overflow: hidden;
  box-shadow: 0 0 80px rgba(34,211,238,0.05), 0 30px 80px rgba(0,0,0,0.9);
}
/* Top ambient glow */

.sr-20__card::before {
  content: '';
  position: absolute;
  top: -40px;
  left: 50%;
  transform: translateX(-50%);
  width: 200px;
  height: 80px;
  background: radial-gradient(ellipse, rgba(34,211,238,0.1), transparent 70%);
  pointer-events: none;
}

.sr-20__header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 20px;
}

.sr-20__title-group {
}

.sr-20__eyebrow {
  font-size: 0.62rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--cyan);
  opacity: 0.6;
  margin-bottom: 5px;
}

.sr-20__title {
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--text);
}

.sr-20__score-badge {
  min-width: 52px;
  height: 52px;
  border-radius: 12px;
  background: rgba(34,211,238,0.06);
  border: 1px solid rgba(34,211,238,0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.sr-20__badge-val {
  font-size: 1.3rem;
  font-weight: 900;
  color: var(--cyan);
  text-shadow: 0 0 16px rgba(34,211,238,0.5);
  transition: all 0.4s;
}

.sr-20__badge-label {
  font-size: 0.5rem;
  color: var(--text-muted);
  margin-top: 1px;
}
/* The DNA helix */

.sr-20__helix-wrap {
  display: flex;
  justify-content: center;
  height: 160px;
  margin-bottom: 24px;
  perspective: 600px;
  position: relative;
}

.sr-20__helix {
  width: 200px;
  height: 160px;
  position: relative;
  transform-style: preserve-3d;
}
/* Each base pair is a row of 3 elements: left dot, connecting bar, right dot */

.sr-20__pair {
  position: absolute;
  width: 100%;
  display: flex;
  align-items: center;
  transform-style: preserve-3d;
}

.sr-20__dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  flex-shrink: 0;
  transition: all 0.4s ease;
  position: relative;
}

.sr-20__dot--left {
  background: rgba(34,211,238,0.15);
  box-shadow: none;
}

.sr-20__dot--right {
  background: rgba(34,211,238,0.15);
  box-shadow: none;
}

.sr-20__dot.lit-a {
  background: var(--cyan);
  box-shadow: 0 0 12px var(--cyan), 0 0 24px rgba(34,211,238,0.4);
}

.sr-20__dot.lit-b {
  background: var(--emerald);
  box-shadow: 0 0 12px var(--emerald), 0 0 24px rgba(52,211,153,0.4);
}

.sr-20__dot.lit-c {
  background: var(--rose);
  box-shadow: 0 0 12px var(--rose), 0 0 24px rgba(244,63,94,0.4);
}

.sr-20__dot.lit-d {
  background: var(--amber);
  box-shadow: 0 0 12px var(--amber), 0 0 24px rgba(251,191,36,0.4);
}

.sr-20__dot.lit-e {
  background: var(--violet);
  box-shadow: 0 0 12px var(--violet), 0 0 24px rgba(167,139,250,0.4);
}

.sr-20__bar {
  flex: 1;
  height: 2px;
  background: rgba(34,211,238,0.08);
  transition: background 0.4s, box-shadow 0.4s;
}

.sr-20__bar.lit {
  background: rgba(34,211,238,0.4);
  box-shadow: 0 0 6px rgba(34,211,238,0.3);
}
/* Helix strands */

.sr-20__strand {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 2px;
  background: linear-gradient(180deg, transparent, rgba(34,211,238,0.2), transparent);
}

.sr-20__strand--left {
  left: 6px;
}

.sr-20__strand--right {
  right: 6px;
}
/* Base labels */

.sr-20__base-label {
  position: absolute;
  font-size: 0.5rem;
  color: var(--text-muted);
  font-family: monospace;
  pointer-events: none;
  transition: color 0.3s;
}
/* Rating controls */

.sr-20__controls {
  margin-bottom: 20px;
}

.sr-20__ctrl-label {
  font-size: 0.68rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 10px;
}

.sr-20__strands {
  display: flex;
  gap: 8px;
}

.sr-20__strands input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-20__strand-btn {
  flex: 1;
  padding: 10px 4px;
  text-align: center;
  border: 1px solid var(--border);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.25s;
  position: relative;
  overflow: hidden;
}

.sr-20__strand-btn:hover {
  border-color: rgba(34,211,238,0.3);
  background: rgba(34,211,238,0.04);
}

.sr-20__strands input:checked + .sr-20__strand-btn {
  border-color: var(--cyan);
  background: rgba(34,211,238,0.08);
  box-shadow: 0 0 16px rgba(34,211,238,0.12);
}

.sr-20__strand-n {
  font-size: 1rem;
  font-weight: 900;
  color: var(--text-muted);
  display: block;
  margin-bottom: 3px;
  transition: color 0.2s;
}

.sr-20__strand-code {
  font-size: 0.58rem;
  color: var(--text-muted);
  font-family: monospace;
  letter-spacing: 1px;
  transition: color 0.2s;
}

.sr-20__strands input:checked + .sr-20__strand-btn .sr-20__strand-n {
  color: var(--cyan);
}

.sr-20__strands input:checked + .sr-20__strand-btn .sr-20__strand-code {
  color: rgba(34,211,238,0.6);
}
/* Sequence display */

.sr-20__sequence {
  font-family: monospace;
  font-size: 0.65rem;
  color: var(--text-muted);
  letter-spacing: 2px;
  margin-bottom: 20px;
  padding: 8px 12px;
  background: rgba(34,211,238,0.03);
  border: 1px solid var(--border);
  border-radius: 6px;
  transition: all 0.3s;
}

.sr-20__sequence span {
  color: var(--cyan);
}
/* Submit */

.sr-20__submit {
  width: 100%;
  padding: 12px;
  background: linear-gradient(135deg, #0891b2, var(--cyan));
  border: none;
  border-radius: 10px;
  color: #001a1f;
  font-size: 0.88rem;
  font-weight: 800;
  cursor: pointer;
  transition: opacity 0.2s, transform 0.15s;
  box-shadow: 0 4px 20px rgba(34,211,238,0.25);
}

.sr-20__submit:hover {
  opacity: 0.9;
  transform: translateY(-1px);
}

@media (prefers-reduced-motion: reduce) {
  .sr-20__dot,
    .sr-20__bar,
    .sr-20__badge-val {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  const helix = document.getElementById('sr-20-helix');
  if(!helix) return;

  const PAIRS = 10;
  const litColors = ['lit-a','lit-b','lit-c','lit-d','lit-e'];
  const seqBases  = ['AT','GC','TA','CG','AA'];
  const seqStrings = [
    '5\'— <span>A·T·A·T·· · · · ·</span> —3\'',
    '5\'— <span>A·T·G·C·G·C· · · ·</span> —3\'',
    '5\'— <span>A·T·G·C·T·A·T·A· ·</span> —3\'',
    '5\'— <span>A·T·G·C·T·A·C·G·C·G</span> —3\'',
    '5\'— <span>A·T·G·C·T·A·C·G·A·A</span> —3\'',
  ];

  // Build base pairs
  const pairs = [];
  for(let i=0;i<PAIRS;i++){
    const pair = document.createElement('div');
    pair.className = 'sr-20__pair';
    // Sinusoidal vertical position
    const t = i/(PAIRS-1);
    const yPct = t*100;
    pair.style.top = `${yPct}%`;
    // Horizontal offset based on helix rotation
    const angle = (i/PAIRS)*Math.PI*2 - Math.PI/2;
    const spread = 50 + Math.sin(angle)*40; // 10 to 90% width
    pair.innerHTML = `
      <div class="sr-20__dot sr-20__dot--left" id="sr-20-dl-${i}"></div>
      <div class="sr-20__bar" id="sr-20-bar-${i}" style="opacity:${0.3+Math.abs(Math.sin(angle))*0.7}"></div>
      <div class="sr-20__dot sr-20__dot--right" id="sr-20-dr-${i}"></div>
    `;
    helix.appendChild(pair);
    pairs.push(pair);
  }

  // Helix rotation animation
  let rotAngle = 0;
  function animateHelix(){
    rotAngle += 0.008;
    for(let i=0;i<PAIRS;i++){
      const angle = (i/PAIRS)*Math.PI*2 + rotAngle;
      const sinVal = Math.sin(angle);
      const cosVal = Math.cos(angle);
      // X offsets for left and right dots
      const lx = 50 + sinVal*42; // percent of helix width
      const rx = 50 - sinVal*42;
      const pair = pairs[i];
      if(!pair) continue;
      // Scale based on perspective (Z depth)
      const scale = 0.7 + (cosVal+1)*0.15;
      const dotL = document.getElementById(`sr-20-dl-${i}`);
      const dotR = document.getElementById(`sr-20-dr-${i}`);
      const bar  = document.getElementById(`sr-20-bar-${i}`);
      if(dotL) { dotL.style.transform = `scale(${scale})`; }
      if(dotR) { dotR.style.transform = `scale(${scale})`; }
      if(bar)  { bar.style.opacity = 0.15 + (cosVal+1)*0.35; }
    }
    requestAnimationFrame(animateHelix);
  }
  animateHelix();

  let currentLit = 0;

  function lightPairs(count, colorClass){
    for(let i=0;i<PAIRS;i++){
      const dl = document.getElementById(`sr-20-dl-${i}`);
      const dr = document.getElementById(`sr-20-dr-${i}`);
      const bar= document.getElementById(`sr-20-bar-${i}`);
      litColors.forEach(c=>{ if(dl)dl.classList.remove(c); if(dr)dr.classList.remove(c); });
      if(bar) bar.classList.remove('lit');
      if(i < count){
        if(dl){ dl.classList.add(colorClass); }
        if(dr){ dr.classList.add(colorClass); }
        if(bar){ bar.classList.add('lit'); }
      }
    }
  }

  document.querySelectorAll('input[name="sr-20-dna"]').forEach((inp,i)=>{
    inp.addEventListener('change',()=>{
      const count = (i+1)*2; // 2,4,6,8,10 pairs lit
      lightPairs(count, litColors[i]);
      document.getElementById('sr-20-bval').textContent = i+1;
      const seqEl = document.getElementById('sr-20-seq');
      if(seqEl) seqEl.innerHTML = seqStrings[i];
    });
  });
})();
```
