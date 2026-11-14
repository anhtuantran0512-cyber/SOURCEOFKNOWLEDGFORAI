---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/text-shadow-direction-movement/"
title: "Text Shadow Direction Movement"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "Your cursor becomes the room's lamp: every heading on the board casts its shadow AWAY from the pointer, and the shadows stretch longer and softer as the…"
has_js: "true"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Text Shadow Direction Movement
Source: https://codefronts.com/motion/css-text-hover-effects/text-shadow-direction-movement/

Your cursor becomes the room's lamp: every heading on the board casts its shadow AWAY from the pointer, and the shadows stretch longer and softer as the light gets further away — all three cards disagreeing about shadow direction at once, which is exactly what sells a single shared light source. Twenty lines of JS do vector math (pointer→element, inverted, distance-scaled) into three custom properties per heading; text-shadow consumes them. A warm glow pool follows the cursor across the board so you can SEE the lamp you're holding.
## HTML
```html
<section class="cth-25" aria-label="Dynamic light source shadow demo">
  <div class="cth-25__stage" id="cth25-board">
    <div class="cth-25__scene">
      <header class="cth-25__head">
        <h1 class="cth-25__title cth-25__lit">The Lamp Test</h1>
        <p class="cth-25__sub">Move the cursor &mdash; you're holding the light. Every shadow points away from it; length and blur grow with distance.</p>
      </header>
      <div class="cth-25__cards">
        <a class="cth-25__card" href="#cth25-board"><h2 class="cth-25__lit">Umbra</h2><p>The hard core of a shadow &mdash; short and sharp when light is near.</p></a>
        <a class="cth-25__card" href="#cth25-board"><h2 class="cth-25__lit">Penumbra</h2><p>The soft fringe &mdash; watch blur climb as the lamp walks away.</p></a>
        <a class="cth-25__card" href="#cth25-board"><h2 class="cth-25__lit">Cast</h2><p>Direction disagrees per card &mdash; that's what sells one shared lamp.</p></a>
      </div>
      <p class="cth-25__hint">JS writes <code>--sx --sy --sb</code> per heading; CSS owns the <code>text-shadow</code>. No pointer? The fallback values ARE the resting design.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-25,
.cth-25 *,
.cth-25 *::before,
.cth-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-25 {
  --bg: oklch(0.95 0.008 85);
  --ink: oklch(0.24 0.02 275);
  --mut: oklch(0.5 0.02 275);
  --card: oklch(0.985 0.005 85);
  --line: oklch(0.88 0.012 85);
  --sh: oklch(0.25 0.03 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-25__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  container: cth25/inline-size;
  background: radial-gradient(340px 340px at var(--lx,50%) var(--ly,25%),oklch(0.99 0.03 90/.9),transparent 70%),var(--bg);
}

.cth-25__scene {
  width: min(100%,860px);
  display: flex;
  flex-direction: column;
  gap: clamp(20px,3.6cqi,32px);
}

.cth-25__head {
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: center;
}

.cth-25__title {
  font-size: clamp(40px,8cqi,76px);
  font-weight: 900;
  letter-spacing: -.03em;
  line-height: 1;
}

.cth-25__lit {
  text-shadow: var(--sx,0px) var(--sy,5px) var(--sb,9px) color-mix(in oklch,var(--sh) 38%,transparent);
  transition: text-shadow .08s linear;
}

.cth-25__sub {
  font-size: 14.5px;
  line-height: 1.65;
  color: var(--mut);
  max-width: 52ch;
}

.cth-25__cards {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: clamp(12px,2.4cqi,20px);
}

.cth-25__card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: clamp(16px,3cqi,24px);
  text-decoration: none;
  color: inherit;
  display: flex;
  flex-direction: column;
  gap: 8px;
  transition: border-color .3s ease;
}

.cth-25__card:hover,
.cth-25__card:focus-visible {
  border-color: var(--ink);
}

.cth-25__card:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.cth-25__card h2 {
  font-size: clamp(22px,3.6cqi,30px);
  font-weight: 850;
  letter-spacing: -.02em;
}

.cth-25__card p {
  font-size: 13px;
  line-height: 1.6;
  color: var(--mut);
}

.cth-25__hint {
  text-align: center;
  font-size: 12.5px;
  color: var(--mut);
}

.cth-25__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.9 0.01 85);
  padding: 1px 6px;
  border-radius: 4px;
}

@container cth25 (width < 620px) {
  .cth-25__cards {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cth-25__lit {
    transition: none !important;
  }
}
```

## JavaScript
```js
(function(){
  var board=document.getElementById('cth25-board');
  if(!board)return;
  var targets=[].slice.call(board.querySelectorAll('.cth-25__lit'));
  var rects=[];
  function measure(){rects=targets.map(function(el){return el.getBoundingClientRect();});}
  measure();
  addEventListener('resize',measure);
  board.addEventListener('scroll',measure);
  board.addEventListener('pointermove',function(e){
    var br=board.getBoundingClientRect();
    board.style.setProperty('--lx',((e.clientX-br.left)/br.width*100).toFixed(1)+'%');
    board.style.setProperty('--ly',((e.clientY-br.top)/br.height*100).toFixed(1)+'%');
    targets.forEach(function(el,i){
      var r=rects[i]||el.getBoundingClientRect();
      var dx=(r.left+r.width/2)-e.clientX,dy=(r.top+r.height/2)-e.clientY;
      var d=Math.hypot(dx,dy)||1,pull=Math.min(d/14,18);
      el.style.setProperty('--sx',(dx/d*pull).toFixed(1)+'px');
      el.style.setProperty('--sy',(dy/d*pull).toFixed(1)+'px');
      el.style.setProperty('--sb',(2+pull*1.1).toFixed(1)+'px');
    });
  });
})();
```
