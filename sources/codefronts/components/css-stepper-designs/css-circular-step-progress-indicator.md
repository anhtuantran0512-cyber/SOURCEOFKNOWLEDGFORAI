---
source: "codefronts"
url: "https://codefronts.com/components/css-stepper-designs/css-circular-step-progress-indicator/"
title: "CSS Circular Step Progress Indicator"
section: "components"
category: "css-stepper-designs"
category_name: "CSS Steppers"
description: "A centred SVG arc ring whose stroke-dashoffset advances per step, surrounded by a tile grid of clickable step cards — violet/purple accent on a near-black…"
has_js: "true"
---

Here's a working CSS Stepper from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Circular Step Progress Indicator
Source: https://codefronts.com/components/css-stepper-designs/css-circular-step-progress-indicator/

A centred SVG arc ring whose stroke-dashoffset advances per step, surrounded by a tile grid of clickable step cards — violet/purple accent on a near-black background ideal for dashboard headers.
## HTML
```html
<div class="stp-09">
  <div class="stp-09__shell">

    <!-- Big circular ring -->
    <div class="stp-09__circle-wrap">
      <div class="stp-09__ring">
        <svg class="stp-09__svg" viewBox="0 0 200 200">
          <defs>
            <linearGradient id="stp-09-grad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#8b5cf6"/>
              <stop offset="100%" stop-color="#ec4899"/>
            </linearGradient>
          </defs>
          <circle class="stp-09__track" cx="100" cy="100" r="90"/>
          <circle class="stp-09__arc" id="stp-09-arc" cx="100" cy="100" r="90"/>
        </svg>
        <div class="stp-09__ring-inner">
          <div class="stp-09__pct-big" id="stp-09-pct">25%</div>
          <div class="stp-09__pct-label">Complete</div>
          <div class="stp-09__step-count" id="stp-09-sc">Step 2 of 4</div>
        </div>
      </div>

      <!-- Linear pip row -->
      <div class="stp-09__track-row" id="stp-09-track">
        <div class="stp-09__pip done" data-i="1"><div class="stp-09__pnode">✓</div><span class="stp-09__plabel">Setup</span></div>
        <div class="stp-09__pip active" data-i="2"><div class="stp-09__pnode">2</div><span class="stp-09__plabel">Configure</span></div>
        <div class="stp-09__pip" data-i="3"><div class="stp-09__pnode">3</div><span class="stp-09__plabel">Integrate</span></div>
        <div class="stp-09__pip" data-i="4"><div class="stp-09__pnode">4</div><span class="stp-09__plabel">Launch</span></div>
      </div>
    </div>

    <!-- Step tiles grid -->
    <div class="stp-09__grid" id="stp-09-grid">
      <div class="stp-09__tile done" data-tile="1">
        <div class="stp-09__tile-step">Step 01</div>
        <div class="stp-09__tile-name">Project Setup</div>
        <div class="stp-09__tile-desc">Repository initialized, dependencies installed, CI configured.</div>
        <span class="stp-09__tile-badge">✓ Complete</span>
      </div>
      <div class="stp-09__tile active" data-tile="2">
        <div class="stp-09__tile-step">Step 02 · Active</div>
        <div class="stp-09__tile-name">Configuration</div>
        <div class="stp-09__tile-desc">Environment variables, feature flags, and API keys.</div>
        <span class="stp-09__tile-badge">● In Progress</span>
      </div>
      <div class="stp-09__tile" data-tile="3">
        <div class="stp-09__tile-step">Step 03</div>
        <div class="stp-09__tile-name">Integration</div>
        <div class="stp-09__tile-desc">Third-party services, webhooks, and data pipelines.</div>
        <span class="stp-09__tile-badge">Upcoming</span>
      </div>
      <div class="stp-09__tile" data-tile="4">
        <div class="stp-09__tile-step">Step 04</div>
        <div class="stp-09__tile-name">Launch</div>
        <div class="stp-09__tile-desc">Production deployment, monitoring, and rollout plan.</div>
        <span class="stp-09__tile-badge">Upcoming</span>
      </div>
    </div>

    <!-- Nav -->
    <div class="stp-09__nav">
      <button class="stp-09__btn stp-09__btn--ghost" id="stp-09-prev">← Prev</button>
      <button class="stp-09__btn stp-09__btn--primary" id="stp-09-next">Next Step →</button>
    </div>
  </div>
</div>
```
## CSS
```css
.stp-09,
.stp-09 *,
.stp-09 *::before,
.stp-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.stp-09 ::selection {
  background: #8b5cf6;
  color: #fff;
}

.stp-09 {
  --bg: #09090b;
  --card: #111113;
  --violet: #8b5cf6;
  --purple: #a78bfa;
  --pink: #ec4899;
  --white: #fafafa;
  --muted: #52525b;
  --border: #27272a;
  --success: #22c55e;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  background-image: radial-gradient(ellipse at 50% 50%,rgba(139,92,246,.04) 0%,transparent 70%);
}

.stp-09__shell {
  max-width: 680px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 48px;
}
/* big circular progress */

.stp-09__circle-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
}

.stp-09__ring {
  position: relative;
  width: 200px;
  height: 200px;
}

.stp-09__svg {
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}

.stp-09__track {
  fill: none;
  stroke: var(--border);
  stroke-width: 8;
}

.stp-09__arc {
  fill: none;
  stroke-width: 8;
  stroke-linecap: round;
  stroke-dasharray: 565;
  stroke-dashoffset: 565;
  stroke: url(#stp-09-grad);
  transition: stroke-dashoffset .7s cubic-bezier(.4,0,.2,1);
}

.stp-09__ring-inner {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.stp-09__pct-big {
  font-size: 36px;
  font-weight: 800;
  color: var(--white);
  letter-spacing: -.04em;
  line-height: 1;
}

.stp-09__pct-label {
  font-size: 11px;
  color: var(--muted);
  letter-spacing: .1em;
  text-transform: uppercase;
  margin-top: 4px;
}

.stp-09__step-count {
  font-size: 13px;
  color: var(--violet);
  font-weight: 600;
  margin-top: 2px;
}
/* step pills below ring */

.stp-09__track-row {
  display: flex;
  align-items: center;
  gap: 0;
  width: 100%;
  max-width: 480px;
}

.stp-09__pip {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  position: relative;
}

.stp-09__pip:not(:last-child)::after {
  content: '';
  position: absolute;
  top: 12px;
  left: calc(50% + 12px);
  width: calc(100% - 24px);
  height: 2px;
  background: var(--border);
  transition: background .5s;
}

.stp-09__pip.done::after {
  background: linear-gradient(90deg,var(--violet),var(--purple));
}

.stp-09__pip.done .stp-09__pnode {
  background: linear-gradient(135deg,var(--violet),var(--purple));
  border-color: transparent;
  color: #fff;
}

.stp-09__pip.active .stp-09__pnode {
  border-color: var(--violet);
  color: var(--violet);
  box-shadow: 0 0 0 4px rgba(139,92,246,.15),0 0 16px rgba(139,92,246,.25);
}

.stp-09__pnode {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  font-weight: 700;
  border: 2px solid var(--border);
  background: var(--card);
  color: var(--muted);
  transition: all .35s cubic-bezier(.34,1.56,.64,1);
}

.stp-09__plabel {
  font-size: 10px;
  color: var(--muted);
  text-align: center;
  letter-spacing: .04em;
  transition: color .3s;
}

.stp-09__pip.done .stp-09__plabel {
  color: var(--purple);
}

.stp-09__pip.active .stp-09__plabel {
  color: var(--white);
}
/* content grid */

.stp-09__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  width: 100%;
}

.stp-09__tile {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 20px;
  transition: border-color .3s,box-shadow .3s;
  position: relative;
  overflow: hidden;
}

.stp-09__tile::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg,rgba(139,92,246,.05),transparent);
  opacity: 0;
  transition: opacity .3s;
}

.stp-09__tile.active {
  border-color: rgba(139,92,246,.4);
  box-shadow: 0 0 24px rgba(139,92,246,.08);
}

.stp-09__tile.active::before {
  opacity: 1;
}

.stp-09__tile.done {
  border-color: rgba(139,92,246,.15);
}

.stp-09__tile-step {
  font-size: 10px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 6px;
  font-weight: 600;
}

.stp-09__tile.done .stp-09__tile-step {
  color: var(--violet);
}

.stp-09__tile.active .stp-09__tile-step {
  color: var(--purple);
}

.stp-09__tile-name {
  font-size: 15px;
  font-weight: 700;
  color: var(--muted);
  transition: color .3s;
}

.stp-09__tile.done .stp-09__tile-name,
.stp-09__tile.active .stp-09__tile-name {
  color: var(--white);
}

.stp-09__tile-desc {
  font-size: 12px;
  color: var(--muted);
  margin-top: 4px;
  line-height: 1.5;
}

.stp-09__tile-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  margin-top: 10px;
  padding: 3px 10px;
  border-radius: 999px;
  font-size: 10px;
  font-weight: 600;
  background: rgba(139,92,246,.12);
  border: 1px solid rgba(139,92,246,.2);
  color: var(--violet);
}

.stp-09__tile.done .stp-09__tile-badge {
  background: rgba(34,197,94,.1);
  border-color: rgba(34,197,94,.2);
  color: var(--success);
}

.stp-09__tile.active .stp-09__tile-badge {
  background: rgba(139,92,246,.2);
  animation: stp-09-pulse 2s ease-in-out infinite;
}

@keyframes stp-09-pulse {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .6;
  }
}
/* nav */

.stp-09__nav {
  display: flex;
  gap: 12px;
  align-items: center;
}

.stp-09__btn {
  padding: 10px 24px;
  border-radius: 10px;
  border: none;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all .2s;
}

.stp-09__btn--ghost {
  background: var(--border);
  color: var(--muted);
}

.stp-09__btn--ghost:hover {
  color: var(--white);
}

.stp-09__btn--primary {
  background: linear-gradient(135deg,var(--violet),var(--purple));
  color: #fff;
  box-shadow: 0 4px 16px rgba(139,92,246,.35);
}

.stp-09__btn--primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 24px rgba(139,92,246,.45);
}

@media (prefers-reduced-motion: reduce) {
  .stp-09__arc {
    transition: none;
  }

  .stp-09__tile.active .stp-09__tile-badge {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  let cur=2;
  const total=4;
  const pips=document.querySelectorAll('.stp-09__pip');
  const tiles=document.querySelectorAll('.stp-09__tile');
  const arc=document.getElementById('stp-09-arc');
  const pctEl=document.getElementById('stp-09-pct');
  const scEl=document.getElementById('stp-09-sc');
  const circumference=565;
  const badgeTexts=['✓ Complete','● In Progress','Upcoming','Upcoming'];
  const badgeClasses=['done','active','',''];

  function update(){
    // ring
    const pct=(cur-1)/(total-1);
    arc.style.strokeDashoffset=circumference-(circumference*pct);
    pctEl.textContent=Math.round(pct*100)+'%';
    scEl.textContent=`Step ${cur} of ${total}`;

    // pips
    pips.forEach((p,i)=>{
      p.classList.remove('done','active');
      const node=p.querySelector('.stp-09__pnode');
      if(i+1<cur){p.classList.add('done');node.textContent='✓';}
      else if(i+1===cur){p.classList.add('active');node.textContent=cur;}
      else node.textContent=i+1;
    });

    // tiles
    tiles.forEach((t,i)=>{
      t.classList.remove('done','active');
      const badge=t.querySelector('.stp-09__tile-badge');
      const step=t.querySelector('.stp-09__tile-step');
      if(i+1<cur){t.classList.add('done');badge.textContent='✓ Complete';step.textContent=`Step 0${i+1}`;}
      else if(i+1===cur){t.classList.add('active');badge.textContent='● In Progress';step.textContent=`Step 0${i+1} · Active`;}
      else{badge.textContent='Upcoming';step.textContent=`Step 0${i+1}`;}
    });
  }

  document.getElementById('stp-09-prev').addEventListener('click',()=>{cur=Math.max(1,cur-1);update();});
  document.getElementById('stp-09-next').addEventListener('click',()=>{cur=Math.min(total,cur+1);update();});
  update();
})();
```
