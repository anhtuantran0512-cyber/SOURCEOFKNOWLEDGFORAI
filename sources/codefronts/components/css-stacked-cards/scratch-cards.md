---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/scratch-cards/"
title: "Scratch Cards"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "An overlapping double-card where the top layer is a scratch-off coating: drag your cursor or finger across it and the surface erases to reveal a promo code…"
has_js: "true"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scratch Cards
Source: https://codefronts.com/components/css-stacked-cards/scratch-cards/

An overlapping double-card where the top layer is a scratch-off coating: drag your cursor or finger across it and the surface erases to reveal a promo code on the card beneath. Includes a keyboard-friendly reveal and a reset.
## HTML
```html
<section class="scd-27" aria-label="Scratch card">
  <div class="scd-27__wrap">
    <div class="scd-27__prize"><p class="scd-27__k">You won</p><b class="scd-27__code">LUCKY-40</b><p class="scd-27__note">40% off your next pack</p></div>
    <canvas class="scd-27__foil" id="scd-27-canvas" width="300" height="180" role="img" aria-label="Scratch-off coating hiding a promo code"></canvas>
    <div class="scd-27__ctl"><button id="scd-27-reveal">Reveal</button><button id="scd-27-reset">Reset</button></div>
  </div>
</section>
```
## CSS
```css
.scd-27,
.scd-27 *,
.scd-27 *::before,
.scd-27 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-27 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #141019;
}

.scd-27__wrap {
  position: relative;
  width: 300px;
}

.scd-27__prize {
  position: relative;
  height: 180px;
  border-radius: 18px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
  background: linear-gradient(150deg,oklch(0.74 0.16 90),oklch(0.68 0.17 40));
  color: #3a1f00;
  box-shadow: 0 20px 44px -22px rgba(0,0,0,.7);
}

.scd-27__k {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  opacity: .8;
}

.scd-27__code {
  font-size: 34px;
  font-weight: 900;
  letter-spacing: .05em;
}

.scd-27__note {
  font-size: 13px;
  opacity: .85;
}

.scd-27__foil {
  position: absolute;
  top: 0;
  left: 0;
  width: 300px;
  height: 180px;
  border-radius: 18px;
  cursor: crosshair;
  touch-action: none;
  transition: opacity .5s;
}

.scd-27__foil.scd-27__done {
  opacity: 0;
  pointer-events: none;
}

.scd-27__ctl {
  display: flex;
  gap: 10px;
  margin-top: 16px;
}

.scd-27__ctl button {
  flex: 1;
  padding: 10px;
  border-radius: 11px;
  border: 1px solid #333a4e;
  background: #20232f;
  color: #fff;
  font-weight: 700;
  font-size: 13px;
  cursor: pointer;
  transition: background .2s;
}

.scd-27__ctl button:hover {
  background: #2b2f3e;
}

.scd-27__ctl button:focus-visible {
  outline: 3px solid oklch(0.72 0.16 60);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .scd-27__foil {
    transition: opacity .2s;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.scd-27');
  const canvas = root.querySelector('#scd-27-canvas');
  const ctx = canvas.getContext('2d');
  const W = 300, H = 180, dpr = window.devicePixelRatio || 1;
  function coat(){
    canvas.width = W * dpr; canvas.height = H * dpr; ctx.scale(dpr, dpr);
    const g = ctx.createLinearGradient(0,0,W,H); g.addColorStop(0,'#9aa0b4'); g.addColorStop(1,'#6b7186');
    ctx.globalCompositeOperation = 'source-over'; ctx.fillStyle = g; ctx.fillRect(0,0,W,H);
    ctx.fillStyle = 'rgba(255,255,255,.14)'; ctx.font = 'bold 15px Segoe UI, sans-serif'; ctx.textAlign='center';
    ctx.fillText('SCRATCH HERE', W/2, H/2+5);
    canvas.classList.remove('scd-27__done');
  }
  let drawing = false;
  function scratch(x,y){ ctx.globalCompositeOperation='destination-out'; ctx.beginPath(); ctx.arc(x,y,18,0,7); ctx.fill(); }
  function pos(e){ const r=canvas.getBoundingClientRect(); return [(e.clientX-r.left)*(W/r.width),(e.clientY-r.top)*(H/r.height)]; }
  function cleared(){ const d=ctx.getImageData(0,0,canvas.width,canvas.height).data; let c=0; for(let i=3;i<d.length;i+=4*40) if(d[i]===0) c++; return c/(d.length/(4*40)); }
  canvas.addEventListener('pointerdown', e => { drawing=true; canvas.setPointerCapture(e.pointerId); const [x,y]=pos(e); scratch(x,y); });
  canvas.addEventListener('pointermove', e => { if(!drawing) return; const [x,y]=pos(e); scratch(x,y); });
  canvas.addEventListener('pointerup', () => { drawing=false; if(cleared()>0.5) reveal(); });
  function reveal(){ canvas.classList.add('scd-27__done'); }
  root.querySelector('#scd-27-reveal').addEventListener('click', reveal);
  root.querySelector('#scd-27-reset').addEventListener('click', coat);
  coat();
})();
```
