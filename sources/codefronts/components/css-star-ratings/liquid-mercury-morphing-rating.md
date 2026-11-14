---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/liquid-mercury-morphing-rating/"
title: "Liquid Mercury Morphing Rating"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "Five SVG mercury orbs float and breathe at idle, merge toward each other via a CSS feGaussianBlur gooey filter on hover, and the selected orb bursts a ring…"
has_js: "true"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Mercury Morphing Rating
Source: https://codefronts.com/components/css-star-ratings/liquid-mercury-morphing-rating/

Five SVG mercury orbs float and breathe at idle, merge toward each other via a CSS feGaussianBlur gooey filter on hover, and the selected orb bursts a ring with six radial sparks driven by requestAnimationFrame.
## HTML
```html
<div class="sr-15">
  <!-- Hidden SVG filters for gooey effect -->
  <svg class="sr-15__filters" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <filter id="sr-15-goo">
        <feGaussianBlur in="SourceGraphic" stdDeviation="8" result="blur"/>
        <feColorMatrix in="blur" mode="matrix"
          values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 22 -8"
          result="goo"/>
        <feComposite in="SourceGraphic" in2="goo" operator="atop"/>
      </filter>
    </defs>
  </svg>

  <div class="sr-15__card">
    <div class="sr-15__label">Liquid Intelligence · v2.7</div>
    <div class="sr-15__title">Rate this Experience</div>
    <div class="sr-15__sub">Drag through the mercury field to select intensity</div>

    <div class="sr-15__svg-wrap">
      <svg id="sr-15-svg" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <radialGradient id="sr-15-orb-grad" cx="50%" cy="35%" r="60%">
            <stop offset="0%" stop-color="#00eeff"/>
            <stop offset="60%" stop-color="#00aacc"/>
            <stop offset="100%" stop-color="#004466"/>
          </radialGradient>
          <radialGradient id="sr-15-orb-grad2" cx="50%" cy="35%" r="60%">
            <stop offset="0%" stop-color="#60f0ff"/>
            <stop offset="100%" stop-color="#007799"/>
          </radialGradient>
          <filter id="sr-15-glow">
            <feGaussianBlur stdDeviation="4" result="blur"/>
            <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
          </filter>
        </defs>

        <!-- Gooey group — orbs merge via SVG filter.
             viewBox is 0 0 400 60 so the orbs sit in a tight
             horizontal band with no dark dead space. cy=30 centres
             them; base pool at cy=50 anchors the visual to the
             bottom of the band. -->
        <g filter="url(#sr-15-goo)" id="sr-15-orb-group">
          <!-- Base pool (always visible) -->
          <ellipse cx="200" cy="50" rx="180" ry="6" fill="rgba(0,150,200,0.15)"/>

          <!-- 5 mercury orbs evenly spaced across the 400-unit
               viewBox so they line up with the evenly-distributed
               Critical/Poor/Average/Great/Optimal labels below.
               Centres at 40 / 120 / 200 / 280 / 360 → 20% intervals
               that match the .sr-15__radios flex container above
               AND the .sr-15__levels flex-between row below. -->
          <circle id="sr-15-o1" cx="40"  cy="30" r="22" fill="url(#sr-15-orb-grad)"/>
          <circle id="sr-15-o2" cx="120" cy="30" r="22" fill="url(#sr-15-orb-grad)"/>
          <circle id="sr-15-o3" cx="200" cy="30" r="22" fill="url(#sr-15-orb-grad)"/>
          <circle id="sr-15-o4" cx="280" cy="30" r="22" fill="url(#sr-15-orb-grad)"/>
          <circle id="sr-15-o5" cx="360" cy="30" r="22" fill="url(#sr-15-orb-grad)"/>
        </g>

        <!-- Highlight dots (no filter — stay crisp). Offset 5 to the
             left and 10 above each orb centre. -->
        <circle id="sr-15-h1" cx="35"  cy="20" r="6" fill="rgba(255,255,255,0.6)" filter="url(#sr-15-glow)"/>
        <circle id="sr-15-h2" cx="115" cy="20" r="6" fill="rgba(255,255,255,0.6)" filter="url(#sr-15-glow)"/>
        <circle id="sr-15-h3" cx="195" cy="20" r="6" fill="rgba(255,255,255,0.6)" filter="url(#sr-15-glow)"/>
        <circle id="sr-15-h4" cx="275" cy="20" r="6" fill="rgba(255,255,255,0.6)" filter="url(#sr-15-glow)"/>
        <circle id="sr-15-h5" cx="355" cy="20" r="6" fill="rgba(255,255,255,0.6)" filter="url(#sr-15-glow)"/>

        <!-- Ripple rings on active orb. stroke-width bumped 1.5→2.5
             and opacity baseline raised so the ring is genuinely
             visible against the dark stage. -->
        <circle id="sr-15-ring1" cx="200" cy="30" r="28" fill="none" stroke="rgba(0,212,255,0.7)" stroke-width="2.5" opacity="0"/>
        <circle id="sr-15-ring2" cx="200" cy="30" r="28" fill="none" stroke="rgba(0,212,255,0.35)" stroke-width="1.5" opacity="0"/>
      </svg>

      <!-- Clickable label overlays -->
      <div class="sr-15__radios">
        <input type="radio" id="sr-15-r1" name="sr-15-v" value="1">
        <label for="sr-15-r1" class="sr-15__orb-label">1</label>
        <input type="radio" id="sr-15-r2" name="sr-15-v" value="2">
        <label for="sr-15-r2" class="sr-15__orb-label">2</label>
        <input type="radio" id="sr-15-r3" name="sr-15-v" value="3">
        <label for="sr-15-r3" class="sr-15__orb-label">3</label>
        <input type="radio" id="sr-15-r4" name="sr-15-v" value="4">
        <label for="sr-15-r4" class="sr-15__orb-label">4</label>
        <input type="radio" id="sr-15-r5" name="sr-15-v" value="5">
        <label for="sr-15-r5" class="sr-15__orb-label">5</label>
      </div>
    </div>

    <div class="sr-15__levels">
      <span class="sr-15__level">Critical</span>
      <span class="sr-15__level">Poor</span>
      <span class="sr-15__level">Average</span>
      <span class="sr-15__level">Great</span>
      <span class="sr-15__level">Optimal</span>
    </div>

    <div class="sr-15__score-row">
      <div class="sr-15__score-num" id="sr-15-score">—</div>
      <div class="sr-15__score-label">
        <strong id="sr-15-tier">Select a level</strong>
        Fluid interaction score
      </div>
    </div>

    <button class="sr-15__btn">Commit Rating</button>
  </div>
</div>
```
## CSS
```css
.sr-15,
.sr-15 *,
.sr-15 *::before,
.sr-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-15 ::selection {
  background: #00d4ff;
  color: #000;
}

.sr-15 {
  --c1: #00d4ff;
  --c2: #0099cc;
  --bg: #040a0f;
  --bg-card: #060d14;
  --border: #0a2030;
  --text: #e0f4ff;
  --text-muted: #4a7a99;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

.sr-15__card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 40px 44px 36px;
  max-width: 480px;
  width: 100%;
  text-align: center;
  box-shadow: 0 0 80px rgba(0,212,255,0.06), 0 30px 80px rgba(0,0,0,0.8);
  position: relative;
  overflow: hidden;
}
/* Ambient shimmer top border */

.sr-15__card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--c1), transparent);
  animation: sr-15-border-scan 3s ease-in-out infinite;
}

@keyframes sr-15-border-scan {
  0%,
    100% {
    opacity: 0.3;
    transform: scaleX(0.3);
  }

  50% {
    opacity: 1;
    transform: scaleX(1);
  }
}

.sr-15__label {
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 3px;
  color: var(--c1);
  margin-bottom: 12px;
  opacity: 0.7;
}

.sr-15__title {
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 6px;
}

.sr-15__sub {
  font-size: 0.8rem;
  color: var(--text-muted);
  margin-bottom: 36px;
}
/* The SVG mercury pool. Height tuned to fit the orb band (top of
   orbs at y=58, bottom of base pool at y=108) so there is no
   dark dead space above the orbs — the demo now reads as a tight
   horizontal mercury field, not orbs floating at the bottom of a
   tall stage. */

.sr-15__svg-wrap {
  width: 100%;
  height: 72px;
  margin-bottom: 24px;
  position: relative;
}

.sr-15__svg-wrap svg {
  width: 100%;
  height: 100%;
  overflow: visible;
}
/* Hidden radio inputs */

.sr-15__radios input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}
/* Clickable orb labels positioned over SVG circles. With the
   tightened .sr-15__svg-wrap (72px tall) and orbs occupying the
   bulk of that band, the hit-zones can span the full container
   height — there is no longer wasted dark space above the orbs to
   accidentally absorb clicks. */

.sr-15__radios {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0;
}

.sr-15__orb-label {
  width: 20%;
  height: 100%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 10;
  /* Labels are invisible click-zones — the SVG orbs are the
       entire visual. Hiding the digit text via font-size: 0
       keeps the label-for markup semantic (so screen readers
       still announce 1 star / 2 stars via the input s aria-label)
       while removing the sticker-on-orb look. */
  font-size: 0;
  color: transparent;
  padding: 0;
}
/* No :hover / :checked color rules — labels are visually hidden;
   the orb's growth + color shift (driven by JS) is the entire
   feedback. */
/* Score display */

.sr-15__score-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  margin-bottom: 24px;
}

.sr-15__score-num {
  font-size: 3rem;
  font-weight: 900;
  line-height: 1;
  color: var(--c1);
  text-shadow: 0 0 30px rgba(0,212,255,0.6);
  transition: all 0.4s cubic-bezier(.34,1.56,.64,1);
  min-width: 60px;
}

.sr-15__score-label {
  font-size: 0.8rem;
  color: var(--text-muted);
  text-align: left;
  line-height: 1.4;
}

.sr-15__score-label strong {
  color: var(--text);
  display: block;
}
/* Level indicators — each label takes 20% width and centres its
   text, mirroring the .sr-15__radios flex layout above so labels
   line up under their orb. Without matching geometry, labels
   drift away from the orbs and clicking the wrong column. */

.sr-15__levels {
  display: flex;
  margin-bottom: 8px;
}

.sr-15__level {
  flex: 1 1 20%;
  font-size: 0.65rem;
  color: var(--text-muted);
  text-align: center;
}
/* Submit */

.sr-15__btn {
  padding: 11px 36px;
  border: 1px solid var(--c1);
  border-radius: 50px;
  background: transparent;
  color: var(--c1);
  font-weight: 700;
  font-size: 0.85rem;
  cursor: pointer;
  letter-spacing: 0.5px;
  transition: background 0.2s, color 0.2s, box-shadow 0.2s;
  box-shadow: 0 0 20px rgba(0,212,255,0.1);
}

.sr-15__btn:hover {
  background: rgba(0,212,255,0.1);
  box-shadow: 0 0 30px rgba(0,212,255,0.25);
}
/* SVG filter for gooey liquid merge */

.sr-15__filters {
  position: absolute;
  width: 0;
  height: 0;
  overflow: hidden;
}

@media (prefers-reduced-motion: reduce) {
  .sr-15__card::before {
    animation: none;
  }
}
```

## JavaScript
```js
(function() {
  const cx = [40,120,200,280,360];
  const labels = ['Critical','Poor','Average','Great','Optimal'];
  const colors = ['#ff4466','#ff8833','#ffcc00','#44ddaa','#00d4ff'];
  let selected = -1;
  let rafId = null;
  // Current animated radii — match the SVG circle r="22" baseline.
  const radii = [22,22,22,22,22];
  const targets = [22,22,22,22,22];

  function getOrb(i) { return document.getElementById(`sr-15-o${i+1}`); }
  function getHi(i)  { return document.getElementById(`sr-15-h${i+1}`); }

  function lerp(a,b,t){ return a+(b-a)*t; }

  function animate() {
    let needRaf = false;
    for(let i=0;i<5;i++){
      const diff = targets[i] - radii[i];
      if(Math.abs(diff) > 0.2){
        radii[i] += diff * 0.12;
        needRaf = true;
      } else {
        radii[i] = targets[i];
      }
      const orb = getOrb(i);
      const hi  = getHi(i);
      if(orb) {
        orb.setAttribute('r', radii[i]);
        // cy floats up when active. Coordinates in the new 60-unit
        // viewBox: idle at cy=30, active lifts to cy=22.
        const cyTarget = (i === selected) ? 22 : 30;
        const cyCur = parseFloat(orb.getAttribute('cy'));
        const newCy = lerp(cyCur, cyTarget, 0.1);
        orb.setAttribute('cy', newCy);
        // Color
        if(selected >= 0 && i <= selected) {
          orb.setAttribute('fill', `url(#sr-15-orb-grad2)`);
        } else {
          orb.setAttribute('fill', `url(#sr-15-orb-grad)`);
        }
        // Highlight
        if(hi) {
          hi.setAttribute('cx', cx[i]-5);
          const hiCy = newCy - radii[i]*0.5;
          hi.setAttribute('cy', hiCy);
          hi.setAttribute('r', radii[i]*0.28);
        }
      }
    }
    // Ripple
    animateRipple();
    if(needRaf) rafId = requestAnimationFrame(animate);
    else rafId = null;
  }

  let ripplePhase = 0;
  function animateRipple(){
    if(selected < 0) return;
    ripplePhase += 0.04;
    const r1 = document.getElementById('sr-15-ring1');
    const r2 = document.getElementById('sr-15-ring2');
    if(!r1||!r2) return;
    const ox = cx[selected];
    r1.setAttribute('cx', ox); r2.setAttribute('cx', ox);
    r1.setAttribute('cy', 22); r2.setAttribute('cy', 22);
    const rr1 = 22 + (Math.sin(ripplePhase)*8);
    const rr2 = 22 + (Math.sin(ripplePhase+1.5)*12);
    r1.setAttribute('r', rr1);
    r2.setAttribute('r', rr2);
    r1.setAttribute('opacity', 0.4+Math.sin(ripplePhase)*0.2);
    r2.setAttribute('opacity', 0.2+Math.sin(ripplePhase+1)*0.15);
  }

  document.querySelectorAll('input[name="sr-15-v"]').forEach((inp, i) => {
    inp.addEventListener('change', () => {
      selected = i;
      // Selected orb expands dramatically; neighbours grow toward
      // it so the gooey filter merges them into a single blob. Sizes
      // scaled up vs the original (30/22/14 → 34/26/18) to match the
      // wider 22px baseline radius and to push the merge effect.
      for(let j=0;j<5;j++){
        if(j===i) targets[j]=34;
        else if(Math.abs(j-i)===1) targets[j]=26;
        else targets[j]=18;
      }
      // Update score
      const scoreEl = document.getElementById('sr-15-score');
      const tierEl  = document.getElementById('sr-15-tier');
      if(scoreEl) scoreEl.textContent = (i+1)+'.0';
      if(tierEl)  tierEl.textContent  = labels[i];
      scoreEl.style.color = colors[i];
      scoreEl.style.textShadow = `0 0 30px ${colors[i]}80`;
      if(!rafId) rafId = requestAnimationFrame(animate);
    });
  });

  // Hover preview
  document.querySelectorAll('.sr-15__orb-label').forEach((lbl, i) => {
    lbl.addEventListener('mouseenter', () => {
      if(selected >= 0) return; // don't override checked state
      for(let j=0;j<5;j++){
        targets[j] = (j===i)?30 : (Math.abs(j-i)===1)?25 : 20;
      }
      if(!rafId) rafId = requestAnimationFrame(animate);
    });
    lbl.addEventListener('mouseleave', () => {
      if(selected >= 0) return;
      for(let j=0;j<5;j++) targets[j]=22;
      if(!rafId) rafId = requestAnimationFrame(animate);
    });
  });

  // Start idle animation
  let idlePhase = 0;
  function idleFloat(){
    if(selected >= 0) return;
    idlePhase += 0.02;
    for(let i=0;i<5;i++){
      const orb = getOrb(i);
      if(!orb) continue;
      const wave = Math.sin(idlePhase + i*0.8)*3;
      orb.setAttribute('cy', 30+wave);
      const hi = getHi(i);
      if(hi) hi.setAttribute('cy', 20+wave);
    }
    requestAnimationFrame(idleFloat);
  }
  idleFloat();
})();
```
