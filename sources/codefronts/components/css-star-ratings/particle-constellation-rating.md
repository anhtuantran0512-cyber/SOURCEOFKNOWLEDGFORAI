---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/particle-constellation-rating/"
title: "Particle Constellation Rating"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A Canvas widget where selecting a rating morphs a field of particles into a named constellation from Lone Star to Full Galaxy, with nodes lerping smoothly to…"
has_js: "true"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Particle Constellation Rating
Source: https://codefronts.com/components/css-star-ratings/particle-constellation-rating/

A Canvas widget where selecting a rating morphs a field of particles into a named constellation from Lone Star to Full Galaxy, with nodes lerping smoothly to new positions and links drawing between them.
## HTML
```html
<div class="sr-21">
  <div class="sr-21__card">
    <div class="sr-21__header">
      <div>
        <div class="sr-21__eyebrow">Stellar Mapping System</div>
        <div class="sr-21__title">Constellation Rating</div>
      </div>
      <div class="sr-21__constellation-name" id="sr-21-cname">Choose your star</div>
    </div>

    <div class="sr-21__canvas-wrap">
      <canvas class="sr-21__canvas" id="sr-21-canvas"></canvas>
    </div>

    <div class="sr-21__orbs">
      <input type="radio" id="sr-21-c1" name="sr-21-ct" value="1">
      <label for="sr-21-c1" class="sr-21__orb-label">
        <div class="sr-21__orb-circle">1</div>
        <span class="sr-21__orb-name">Lone<br>Star</span>
      </label>

      <input type="radio" id="sr-21-c2" name="sr-21-ct" value="2">
      <label for="sr-21-c2" class="sr-21__orb-label">
        <div class="sr-21__orb-circle">2</div>
        <span class="sr-21__orb-name">Binary<br>System</span>
      </label>

      <input type="radio" id="sr-21-c3" name="sr-21-ct" value="3">
      <label for="sr-21-c3" class="sr-21__orb-label">
        <div class="sr-21__orb-circle">3</div>
        <span class="sr-21__orb-name">Orion's<br>Belt</span>
      </label>

      <input type="radio" id="sr-21-c4" name="sr-21-ct" value="4">
      <label for="sr-21-c4" class="sr-21__orb-label">
        <div class="sr-21__orb-circle">4</div>
        <span class="sr-21__orb-name">Southern<br>Cross</span>
      </label>

      <input type="radio" id="sr-21-c5" name="sr-21-ct" value="5">
      <label for="sr-21-c5" class="sr-21__orb-label">
        <div class="sr-21__orb-circle">5</div>
        <span class="sr-21__orb-name">Full<br>Galaxy</span>
      </label>
    </div>

    <div class="sr-21__meta">
      <div class="sr-21__meta-stat">
        <span class="sr-21__meta-val" id="sr-21-starcount">—</span>
        <span class="sr-21__meta-key">Stars</span>
      </div>
      <div class="sr-21__meta-stat">
        <span class="sr-21__meta-val" id="sr-21-links">—</span>
        <span class="sr-21__meta-key">Links</span>
      </div>
      <div class="sr-21__meta-stat">
        <span class="sr-21__meta-val" id="sr-21-mag">—</span>
        <span class="sr-21__meta-key">Magnitude</span>
      </div>
    </div>

    <button class="sr-21__submit">Map Constellation</button>
  </div>
</div>
```
## CSS
```css
.sr-21,
.sr-21 *,
.sr-21 *::before,
.sr-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-21 ::selection {
  background: #f0abfc;
  color: #1a0030;
}

.sr-21 {
  --fuchsia: #d946ef;
  --fuchsia2: #a21caf;
  --pink: #f0abfc;
  --bg: #08020e;
  --bg-card: #0d0416;
  --text: #fae8ff;
  --text-muted: #6b21a8;
  --border: rgba(217,70,239,0.1);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

.sr-21__card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 28px 32px;
  max-width: 480px;
  width: 100%;
  position: relative;
  overflow: hidden;
  box-shadow: 0 0 80px rgba(217,70,239,0.06), 0 30px 80px rgba(0,0,0,0.95);
}

.sr-21__header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
}

.sr-21__eyebrow {
  font-size: 0.62rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--fuchsia);
  opacity: 0.6;
  margin-bottom: 5px;
}

.sr-21__title {
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--text);
}

.sr-21__constellation-name {
  font-size: 0.7rem;
  color: var(--fuchsia);
  text-align: right;
  font-style: italic;
  opacity: 0.7;
  transition: all 0.3s;
  min-width: 80px;
}
/* Canvas */

.sr-21__canvas-wrap {
  height: 180px;
  margin-bottom: 20px;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(217,70,239,0.08);
  position: relative;
}

.sr-21__canvas {
  width: 100%;
  height: 100%;
  display: block;
}
/* Rating selector — cosmic orbs */

.sr-21__orbs {
  display: flex;
  justify-content: center;
  gap: 14px;
  margin-bottom: 20px;
}

.sr-21__orbs input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-21__orb-label {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  cursor: pointer;
}

.sr-21__orb-circle {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: rgba(217,70,239,0.06);
  border: 1px solid rgba(217,70,239,0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  font-weight: 900;
  color: var(--text-muted);
  transition: all 0.3s cubic-bezier(.34,1.56,.64,1);
  position: relative;
}

.sr-21__orb-circle::after {
  content: '';
  position: absolute;
  inset: -6px;
  border-radius: 50%;
  border: 1px solid transparent;
  transition: border-color 0.3s, transform 0.3s;
}

.sr-21__orbs input:checked + .sr-21__orb-label .sr-21__orb-circle {
  background: rgba(217,70,239,0.18);
  border-color: var(--fuchsia);
  color: var(--pink);
  box-shadow: 0 0 20px rgba(217,70,239,0.4), 0 0 40px rgba(217,70,239,0.15);
  transform: scale(1.15);
}

.sr-21__orbs input:checked + .sr-21__orb-label .sr-21__orb-circle::after {
  border-color: rgba(217,70,239,0.3);
  animation: sr-21-ring-out 1.6s ease-out infinite;
}

@keyframes sr-21-ring-out {
  0% {
    transform: scale(1);
    opacity: 0.6;
  }

  100% {
    transform: scale(1.5);
    opacity: 0;
  }
}

.sr-21__orb-name {
  font-size: 0.6rem;
  color: var(--text-muted);
  transition: color 0.2s;
  text-align: center;
  line-height: 1.2;
}

.sr-21__orbs input:checked + .sr-21__orb-label .sr-21__orb-name {
  color: var(--fuchsia);
}
/* Star count row */

.sr-21__meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  padding: 10px 14px;
  background: rgba(217,70,239,0.04);
  border-radius: 10px;
  border: 1px solid var(--border);
}

.sr-21__meta-stat {
  text-align: center;
}

.sr-21__meta-val {
  font-size: 1.1rem;
  font-weight: 900;
  color: var(--fuchsia);
  display: block;
}

.sr-21__meta-key {
  font-size: 0.58rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
/* Submit */

.sr-21__submit {
  width: 100%;
  padding: 12px;
  background: linear-gradient(135deg, var(--fuchsia2), var(--fuchsia));
  border: none;
  border-radius: 10px;
  color: #fff;
  font-size: 0.88rem;
  font-weight: 700;
  cursor: pointer;
  transition: opacity 0.2s, transform 0.15s;
  box-shadow: 0 4px 20px rgba(217,70,239,0.3);
}

.sr-21__submit:hover {
  opacity: 0.9;
  transform: translateY(-1px);
}

@media (prefers-reduced-motion: reduce) {
  .sr-21__orb-circle::after {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  const canvas = document.getElementById('sr-21-canvas');
  if(!canvas) return;
  const ctx = canvas.getContext('2d');

  function resize(){
    const p = canvas.parentElement;
    canvas.width = p.offsetWidth;
    canvas.height = p.offsetHeight;
  }
  resize(); window.addEventListener('resize', resize);

  // Constellation node definitions per level
  const constellations = [
    { // Level 1: single star
      nodes: [[0.5, 0.5]],
      links: [],
      name: 'Solaris', stars: 1, links_n: 0, mag: '-1.4'
    },
    { // Level 2: binary
      nodes: [[0.35,0.5],[0.65,0.5]],
      links: [[0,1]],
      name: 'Gemini', stars: 2, links_n: 1, mag: '-0.7'
    },
    { // Level 3: Orion's belt
      nodes: [[0.25,0.5],[0.5,0.42],[0.75,0.5]],
      links: [[0,1],[1,2]],
      name: 'Orion', stars: 3, links_n: 2, mag: '+1.2'
    },
    { // Level 4: Cross
      nodes: [[0.5,0.25],[0.28,0.5],[0.5,0.75],[0.72,0.5]],
      links: [[0,1],[0,3],[1,2],[2,3],[0,2]],
      name: 'Crux', stars: 4, links_n: 5, mag: '+2.8'
    },
    { // Level 5: Full galaxy — many nodes
      nodes: [
        [0.5,0.15],[0.78,0.3],[0.85,0.6],[0.65,0.82],[0.35,0.82],
        [0.15,0.6],[0.22,0.3],[0.5,0.5],[0.5,0.72],[0.72,0.45]
      ],
      links: [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,0],[7,0],[7,2],[7,4],[7,6],[8,3],[8,5],[9,1],[9,2]],
      name: 'Andromeda', stars: 10, links_n: 15, mag: '+5.0'
    }
  ];

  let animatedNodes = [];
  let targetNodes   = [];
  let currentLinks  = [];
  let currentColor  = [217,70,239];
  let phase = 0;
  let raf;

  function lerp(a,b,t){ return a+(b-a)*t; }

  const colors = [
    [150,130,255], [200,100,255], [217,70,239], [240,100,180], [255,130,220]
  ];

  function setLevel(idx){
    const C = constellations[idx];
    const W = canvas.width, H = canvas.height;
    currentLinks = C.links;
    currentColor = colors[idx];
    targetNodes = C.nodes.map(([x,y])=>({ x: x*W, y: y*H, r: 0 }));

    // Initialize animatedNodes if needed
    if(animatedNodes.length===0){
      animatedNodes = targetNodes.map(n=>({ x: W/2, y: H/2, r: 0 }));
    } else {
      // Interpolate from previous positions
      const prev = animatedNodes.slice();
      animatedNodes = targetNodes.map((n,i)=>({
        x: (prev[i]||{ x: W/2 }).x,
        y: (prev[i]||{ y: H/2 }).y,
        r: 0
      }));
    }

    document.getElementById('sr-21-cname').textContent  = C.name;
    document.getElementById('sr-21-starcount').textContent = C.stars;
    document.getElementById('sr-21-links').textContent   = C.links_n;
    document.getElementById('sr-21-mag').textContent     = C.mag;

    if(!raf) raf = requestAnimationFrame(draw);
  }

  // Background stars (static)
  const bgStars = Array.from({length:60},()=>({
    x: Math.random(), y: Math.random(),
    r: Math.random()*1.2+0.3,
    opacity: Math.random()*0.3+0.05
  }));

  function draw(){
    phase += 0.015;
    const W = canvas.width, H = canvas.height;
    ctx.clearRect(0,0,W,H);

    // BG stars
    bgStars.forEach(s=>{
      ctx.beginPath();
      ctx.arc(s.x*W, s.y*H, s.r, 0, Math.PI*2);
      ctx.fillStyle = `rgba(240,171,252,${s.opacity + Math.sin(phase+s.x*10)*0.05})`;
      ctx.fill();
    });

    if(targetNodes.length===0) { raf = null; return; }

    const [r,g,b] = currentColor;

    // Lerp animated nodes toward targets
    let moving = false;
    for(let i=0;i<Math.max(animatedNodes.length,targetNodes.length);i++){
      if(!animatedNodes[i]) animatedNodes[i] = { x: W/2, y: H/2, r: 0 };
      if(!targetNodes[i])  targetNodes[i]  = animatedNodes[i];
      const dx = targetNodes[i].x - animatedNodes[i].x;
      const dy = targetNodes[i].y - animatedNodes[i].y;
      if(Math.abs(dx)+Math.abs(dy)>0.5){
        animatedNodes[i].x += dx*0.07;
        animatedNodes[i].y += dy*0.07;
        moving = true;
      } else {
        animatedNodes[i].x = targetNodes[i].x;
        animatedNodes[i].y = targetNodes[i].y;
      }
    }

    // Draw links
    currentLinks.forEach(([a,b])=>{
      const na = animatedNodes[a], nb = animatedNodes[b];
      if(!na||!nb) return;
      const grad = ctx.createLinearGradient(na.x,na.y,nb.x,nb.y);
      grad.addColorStop(0, `rgba(${r},${g},${b},0.6)`);
      grad.addColorStop(1, `rgba(${r},${g},${b},0.3)`);
      ctx.beginPath();
      ctx.moveTo(na.x,na.y); ctx.lineTo(nb.x,nb.y);
      ctx.strokeStyle = grad;
      ctx.lineWidth = 1;
      ctx.shadowColor = `rgb(${r},${g},${b})`;
      ctx.shadowBlur = 4;
      ctx.stroke();
      ctx.shadowBlur = 0;
    });

    // Draw nodes
    animatedNodes.forEach((n,i)=>{
      if(i >= targetNodes.length) return;
      const pulse = 3 + Math.sin(phase + i)*1.5;

      // Glow
      const grd = ctx.createRadialGradient(n.x,n.y,0,n.x,n.y,pulse*4);
      grd.addColorStop(0,`rgba(${r},${g},${b},0.4)`);
      grd.addColorStop(1,'transparent');
      ctx.beginPath(); ctx.arc(n.x,n.y,pulse*4,0,Math.PI*2);
      ctx.fillStyle=grd; ctx.fill();

      // Core
      ctx.beginPath(); ctx.arc(n.x,n.y,pulse,0,Math.PI*2);
      ctx.fillStyle=`rgb(${r},${g},${b})`;
      ctx.shadowColor=`rgb(${r},${g},${b})`; ctx.shadowBlur=10;
      ctx.fill(); ctx.shadowBlur=0;

      // Highlight
      ctx.beginPath(); ctx.arc(n.x-pulse*0.3,n.y-pulse*0.3,pulse*0.35,0,Math.PI*2);
      ctx.fillStyle='rgba(255,255,255,0.5)'; ctx.fill();
    });

    raf = requestAnimationFrame(draw);
  }

  document.querySelectorAll('input[name="sr-21-ct"]').forEach((inp,i)=>{
    inp.addEventListener('change',()=>setLevel(i));
  });

  // Idle background draw
  raf = requestAnimationFrame(draw);
})();
```
