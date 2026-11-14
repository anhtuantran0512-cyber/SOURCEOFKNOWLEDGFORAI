---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/quantum-superposition-rating/"
title: "Quantum Superposition Rating"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A rating widget where the score exists in quantum superposition cycling through all five states simultaneously until the user clicks Observe to collapse the…"
has_js: "true"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Quantum Superposition Rating
Source: https://codefronts.com/components/css-star-ratings/quantum-superposition-rating/

A rating widget where the score exists in quantum superposition cycling through all five states simultaneously until the user clicks Observe to collapse the wave function to a definite value.
## HTML
```html
<div class="sr-19">
  <div class="sr-19__card">
    <!-- Starfield bg -->
    <div class="sr-19__stars-bg" id="sr-19-starfield"></div>

    <div class="sr-19__inner">
      <div class="sr-19__header">
        <div class="sr-19__eyebrow">ψ Quantum Rating Interface</div>
        <div class="sr-19__title">Wave Function Collapse</div>
        <div class="sr-19__sub">Score exists in superposition — observe to collapse</div>
      </div>

      <!-- Orb -->
      <div class="sr-19__orb-wrap">
        <div class="sr-19__wave-labels">
          <span class="sr-19__wave-label">|ψ⟩</span>
          <span class="sr-19__wave-label">∑|n⟩</span>
        </div>
        <div class="sr-19__orb">
          <div class="sr-19__prob-ring"></div>
          <div class="sr-19__prob-ring"></div>
          <div class="sr-19__prob-ring"></div>
          <div class="sr-19__orb-core">
            <span class="sr-19__orb-val superposed" id="sr-19-orb-val">?</span>
          </div>
        </div>
        <button class="sr-19__collapse-btn" id="sr-19-collapse">⬡ Observe</button>
      </div>

      <!-- State selector -->
      <div class="sr-19__states">
        <input type="radio" id="sr-19-s1" name="sr-19-q" value="1">
        <label for="sr-19-s1" class="sr-19__state-btn">
          <span class="sr-19__state-psi">|1⟩</span>
          <span class="sr-19__state-n">n=1</span>
        </label>

        <input type="radio" id="sr-19-s2" name="sr-19-q" value="2">
        <label for="sr-19-s2" class="sr-19__state-btn">
          <span class="sr-19__state-psi">|2⟩</span>
          <span class="sr-19__state-n">n=2</span>
        </label>

        <input type="radio" id="sr-19-s3" name="sr-19-q" value="3">
        <label for="sr-19-s3" class="sr-19__state-btn">
          <span class="sr-19__state-psi">|3⟩</span>
          <span class="sr-19__state-n">n=3</span>
        </label>

        <input type="radio" id="sr-19-s4" name="sr-19-q" value="4">
        <label for="sr-19-s4" class="sr-19__state-btn">
          <span class="sr-19__state-psi">|4⟩</span>
          <span class="sr-19__state-n">n=4</span>
        </label>

        <input type="radio" id="sr-19-s5" name="sr-19-q" value="5">
        <label for="sr-19-s5" class="sr-19__state-btn">
          <span class="sr-19__state-psi">|5⟩</span>
          <span class="sr-19__state-n">n=5</span>
        </label>
      </div>

      <!-- Probability amplitude bars -->
      <div class="sr-19__prob-bars" id="sr-19-bars">
        <div class="sr-19__prob-row">
          <span class="sr-19__prob-state">|1⟩</span>
          <div class="sr-19__prob-track"><div class="sr-19__prob-fill" id="sr-19-p1" style="width:20%"></div></div>
          <span class="sr-19__prob-pct" id="sr-19-pv1">20%</span>
        </div>
        <div class="sr-19__prob-row">
          <span class="sr-19__prob-state">|2⟩</span>
          <div class="sr-19__prob-track"><div class="sr-19__prob-fill" id="sr-19-p2" style="width:20%"></div></div>
          <span class="sr-19__prob-pct" id="sr-19-pv2">20%</span>
        </div>
        <div class="sr-19__prob-row">
          <span class="sr-19__prob-state">|3⟩</span>
          <div class="sr-19__prob-track"><div class="sr-19__prob-fill" id="sr-19-p3" style="width:20%"></div></div>
          <span class="sr-19__prob-pct" id="sr-19-pv3">20%</span>
        </div>
        <div class="sr-19__prob-row">
          <span class="sr-19__prob-state">|4⟩</span>
          <div class="sr-19__prob-track"><div class="sr-19__prob-fill" id="sr-19-p4" style="width:20%"></div></div>
          <span class="sr-19__prob-pct" id="sr-19-pv4">20%</span>
        </div>
        <div class="sr-19__prob-row">
          <span class="sr-19__prob-state">|5⟩</span>
          <div class="sr-19__prob-track"><div class="sr-19__prob-fill" id="sr-19-p5" style="width:20%"></div></div>
          <span class="sr-19__prob-pct" id="sr-19-pv5">20%</span>
        </div>
      </div>

      <button class="sr-19__submit" id="sr-19-submit">Collapse Wave Function</button>
    </div>
  </div>
</div>
```
## CSS
```css
.sr-19,
.sr-19 *,
.sr-19 *::before,
.sr-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-19 ::selection {
  background: #818cf8;
  color: #fff;
}

.sr-19 {
  --indigo: #818cf8;
  --indigo2: #4f46e5;
  --cyan: #22d3ee;
  --bg: #02020f;
  --bg-card: #04041a;
  --text: #e0e7ff;
  --text-muted: #3b3f6e;
  --border: rgba(129,140,248,0.1);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

.sr-19__card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 32px 36px 28px;
  max-width: 480px;
  width: 100%;
  position: relative;
  overflow: hidden;
  box-shadow: 0 0 100px rgba(129,140,248,0.07), 0 30px 80px rgba(0,0,0,0.95);
}
/* Starfield */

.sr-19__stars-bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.sr-19__star {
  position: absolute;
  border-radius: 50%;
  background: var(--indigo);
  opacity: 0;
  animation: sr-19-twinkle var(--dur, 3s) var(--delay, 0s) ease-in-out infinite;
}

@keyframes sr-19-twinkle {
  0%,
    100% {
    opacity: 0;
    transform: scale(0.5);
  }

  50% {
    opacity: var(--op,0.6);
    transform: scale(1);
  }
}

.sr-19__inner {
  position: relative;
  z-index: 1;
}

.sr-19__header {
  margin-bottom: 24px;
}

.sr-19__eyebrow {
  font-size: 0.62rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  color: var(--indigo);
  opacity: 0.6;
  margin-bottom: 6px;
}

.sr-19__title {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 4px;
}

.sr-19__sub {
  font-size: 0.78rem;
  color: var(--text-muted);
}
/* Quantum orb — superposition spinner */

.sr-19__orb-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 160px;
  margin-bottom: 24px;
  position: relative;
}

.sr-19__orb {
  width: 100px;
  height: 100px;
  position: relative;
}
/* Probability rings */

.sr-19__prob-ring {
  position: absolute;
  border-radius: 50%;
  border: 1px solid;
  animation: sr-19-orbit linear infinite;
}

.sr-19__prob-ring:nth-child(1) {
  inset: -10px;
  border-color: rgba(129,140,248,0.4);
  animation-duration: 4s;
}

.sr-19__prob-ring:nth-child(2) {
  inset: -22px;
  border-color: rgba(34,211,238,0.25);
  animation-duration: 6s;
  animation-direction: reverse;
}

.sr-19__prob-ring:nth-child(3) {
  inset: -36px;
  border-color: rgba(129,140,248,0.12);
  animation-duration: 9s;
}

@keyframes sr-19-orbit {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }
}
/* Orbiting probability dots */

.sr-19__prob-ring::before,
.sr-19__prob-ring::after {
  content: '';
  position: absolute;
  border-radius: 50%;
  background: var(--indigo);
  box-shadow: 0 0 8px var(--indigo);
}

.sr-19__prob-ring:nth-child(1)::before {
  width: 6px;
  height: 6px;
  top: -3px;
  left: 50%;
  margin-left: -3px;
}

.sr-19__prob-ring:nth-child(1)::after {
  width: 4px;
  height: 4px;
  bottom: -2px;
  left: 50%;
  margin-left: -2px;
  background: var(--cyan);
  box-shadow: 0 0 6px var(--cyan);
}

.sr-19__prob-ring:nth-child(2)::before {
  width: 5px;
  height: 5px;
  top: -2.5px;
  left: 30%;
  background: var(--cyan);
  box-shadow: 0 0 8px var(--cyan);
}

.sr-19__prob-ring:nth-child(3)::before {
  width: 4px;
  height: 4px;
  top: -2px;
  left: 70%;
}
/* Core sphere */

.sr-19__orb-core {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, rgba(129,140,248,0.6), rgba(79,70,229,0.8) 50%, rgba(4,4,26,0.9));
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 30px rgba(129,140,248,0.3), inset 0 0 20px rgba(0,0,0,0.5);
}

.sr-19__orb-val {
  font-size: 1.8rem;
  font-weight: 900;
  color: #fff;
  transition: all 0.3s;
  text-shadow: 0 0 20px rgba(255,255,255,0.5);
}
/* Superposition state — shimmer all values */

.sr-19__orb-val.superposed {
  animation: sr-19-superpose 0.2s steps(1) infinite;
}

@keyframes sr-19-superpose {
  0% {
    content: '1';
    opacity: 0.5;
    color: #f87171;
  }

  20% {
    content: '2';
    opacity: 0.7;
    color: #fb923c;
  }

  40% {
    content: '3';
    opacity: 0.6;
    color: var(--indigo);
  }

  60% {
    content: '4';
    opacity: 0.8;
    color: var(--cyan);
  }

  80% {
    content: '5';
    opacity: 0.9;
    color: #a3e635;
  }
}
/* Wave function side labels */

.sr-19__wave-labels {
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  justify-content: space-between;
  padding: 0 8px;
  pointer-events: none;
}

.sr-19__wave-label {
  font-size: 0.6rem;
  color: var(--text-muted);
  font-family: monospace;
}
/* Collapse button */

.sr-19__collapse-btn {
  position: absolute;
  bottom: 12px;
  left: 50%;
  transform: translateX(-50%);
  padding: 6px 18px;
  border: 1px solid rgba(129,140,248,0.3);
  background: rgba(129,140,248,0.06);
  color: var(--indigo);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
  cursor: pointer;
  border-radius: 20px;
  transition: all 0.2s;
  font-family: inherit;
}

.sr-19__collapse-btn:hover {
  background: rgba(129,140,248,0.12);
  box-shadow: 0 0 20px rgba(129,140,248,0.2);
}
/* State selector */

.sr-19__states {
  display: grid;
  grid-template-columns: repeat(5,1fr);
  gap: 8px;
  margin-bottom: 20px;
}

.sr-19__states input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-19__state-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  padding: 10px 4px;
  border: 1px solid var(--border);
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.25s;
}

.sr-19__state-btn:hover {
  border-color: rgba(129,140,248,0.3);
  background: rgba(129,140,248,0.04);
}

.sr-19__states input:checked + .sr-19__state-btn {
  border-color: var(--indigo);
  background: rgba(129,140,248,0.1);
  box-shadow: 0 0 16px rgba(129,140,248,0.15);
}

.sr-19__state-psi {
  font-size: 1.1rem;
  color: var(--text-muted);
  transition: color 0.2s;
}

.sr-19__states input:checked + .sr-19__state-btn .sr-19__state-psi {
  color: var(--indigo);
  text-shadow: 0 0 10px rgba(129,140,248,0.5);
}

.sr-19__state-n {
  font-size: 0.62rem;
  color: var(--text-muted);
  transition: color 0.2s;
}

.sr-19__states input:checked + .sr-19__state-btn .sr-19__state-n {
  color: var(--indigo);
}
/* Probability bars */

.sr-19__prob-bars {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 20px;
}

.sr-19__prob-row {
  display: flex;
  align-items: center;
  gap: 10px;
}

.sr-19__prob-state {
  font-size: 0.65rem;
  color: var(--text-muted);
  width: 48px;
  font-family: monospace;
}

.sr-19__prob-track {
  flex: 1;
  height: 4px;
  background: rgba(129,140,248,0.06);
  border-radius: 2px;
  overflow: hidden;
}

.sr-19__prob-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--indigo2), var(--indigo));
  border-radius: 2px;
  box-shadow: 0 0 6px var(--indigo);
  transition: width 0.6s cubic-bezier(.4,0,.2,1);
}

.sr-19__prob-pct {
  font-size: 0.62rem;
  color: var(--indigo);
  width: 32px;
  text-align: right;
  font-family: monospace;
}
/* Submit */

.sr-19__submit {
  width: 100%;
  padding: 13px;
  background: linear-gradient(135deg, var(--indigo2), var(--indigo));
  border: none;
  border-radius: 12px;
  color: #fff;
  font-size: 0.88rem;
  font-weight: 700;
  cursor: pointer;
  transition: opacity 0.2s, transform 0.15s;
  box-shadow: 0 4px 20px rgba(129,140,248,0.3);
  letter-spacing: 0.3px;
}

.sr-19__submit:hover {
  opacity: 0.9;
  transform: translateY(-1px);
}

@media (prefers-reduced-motion: reduce) {
  .sr-19__prob-ring {
    animation: none;
  }

  .sr-19__orb-val.superposed {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  // Generate starfield
  const sf = document.getElementById('sr-19-starfield');
  if(sf){
    for(let i=0;i<40;i++){
      const s = document.createElement('div');
      s.className = 'sr-19__star';
      const sz = Math.random()*2+1;
      s.style.cssText = `width:${sz}px;height:${sz}px;top:${Math.random()*100}%;left:${Math.random()*100}%;--dur:${2+Math.random()*4}s;--delay:${Math.random()*3}s;--op:${0.3+Math.random()*0.5};`;
      sf.appendChild(s);
    }
  }

  let collapsed = false;
  let selectedVal = null;

  // Superposing animation
  const orbVal = document.getElementById('sr-19-orb-val');
  const vals = ['1','2','3','4','5'];
  let vIdx = 0;
  let superInterval = setInterval(()=>{
    if(!collapsed && orbVal){
      vIdx = (vIdx+1)%5;
      orbVal.textContent = vals[vIdx];
    }
  }, 200);

  // Probability distributions per selection
  const probs = [
    [70, 15, 8, 5, 2],
    [15, 65, 12, 5, 3],
    [8,  12, 60, 15, 5],
    [5,   8, 12, 65, 10],
    [2,   5,  8, 15, 70],
  ];

  function updateProbs(idx){
    const p = probs[idx];
    for(let i=1;i<=5;i++){
      const bar = document.getElementById(`sr-19-p${i}`);
      const val = document.getElementById(`sr-19-pv${i}`);
      if(bar) bar.style.width = p[i-1]+'%';
      if(val) val.textContent = p[i-1]+'%';
    }
  }

  document.querySelectorAll('input[name="sr-19-q"]').forEach((inp,i)=>{
    inp.addEventListener('change',()=>{
      selectedVal = i+1;
      collapsed = false;
      if(orbVal){
        orbVal.textContent = '?';
        orbVal.classList.add('superposed');
        clearInterval(superInterval);
        superInterval = setInterval(()=>{
          if(!collapsed && orbVal){
            vIdx=(vIdx+1)%5;
            orbVal.textContent=vals[vIdx];
          }
        },200);
      }
      updateProbs(i);
    });
  });

  // Observe / collapse
  document.getElementById('sr-19-collapse').addEventListener('click',()=>{
    if(selectedVal===null){
      // Random collapse
      selectedVal = Math.ceil(Math.random()*5);
      const radio = document.getElementById(`sr-19-s${selectedVal}`);
      if(radio) radio.checked = true;
      updateProbs(selectedVal-1);
    }
    collapsed = true;
    clearInterval(superInterval);
    if(orbVal){
      orbVal.textContent = selectedVal;
      orbVal.classList.remove('superposed');
    }
    // Collapse probs to 100% on selected
    for(let i=1;i<=5;i++){
      const bar = document.getElementById(`sr-19-p${i}`);
      const val = document.getElementById(`sr-19-pv${i}`);
      if(bar) bar.style.width = (i===selectedVal?'100':'0')+'%';
      if(val) val.textContent  = (i===selectedVal?'100':'0')+'%';
    }
  });

  // Re-enter superposition on submit
  document.getElementById('sr-19-submit').addEventListener('click',()=>{
    if(!selectedVal) return;
    collapsed = false;
    if(orbVal){ orbVal.textContent='?'; orbVal.classList.add('superposed'); }
    clearInterval(superInterval);
    superInterval = setInterval(()=>{
      if(!collapsed&&orbVal){ vIdx=(vIdx+1)%5; orbVal.textContent=vals[vIdx]; }
    },200);
    alert(`Rating submitted: |${selectedVal}⟩ collapsed ✓`);
  });
})();
```
