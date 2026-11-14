---
source: "codefronts"
url: "https://codefronts.com/components/css-stepper-designs/css-breadcrumb-style-step-tracker/"
title: "CSS Breadcrumb Style Step Tracker"
section: "components"
category: "css-stepper-designs"
category_name: "CSS Steppers"
description: "Three synced breadcrumb-style step tracker variants — chevron arrow tabs, a pill strip, and a dashed dot-connector row — all driven by one prev/next…"
has_js: "true"
---

Here's a working CSS Stepper from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Breadcrumb Style Step Tracker
Source: https://codefronts.com/components/css-stepper-designs/css-breadcrumb-style-step-tracker/

Three synced breadcrumb-style step tracker variants — chevron arrow tabs, a pill strip, and a dashed dot-connector row — all driven by one prev/next controller with an amber/gold colour scheme.
## HTML
```html
<div class="stp-07">

  <!-- Chevron breadcrumbs -->
  <div class="stp-07__crumbs" id="stp-07-crumbs">
    <div class="stp-07__crumb done"><span class="stp-07__crumb-num">01</span><span class="stp-07__crumb-name">Discovery</span></div>
    <div class="stp-07__crumb done"><span class="stp-07__crumb-num">02</span><span class="stp-07__crumb-name">Proposal</span></div>
    <div class="stp-07__crumb active"><span class="stp-07__crumb-num">03</span><span class="stp-07__crumb-name">Review</span></div>
    <div class="stp-07__crumb"><span class="stp-07__crumb-num">04</span><span class="stp-07__crumb-name">Approval</span></div>
    <div class="stp-07__crumb"><span class="stp-07__crumb-num">05</span><span class="stp-07__crumb-name">Delivery</span></div>
  </div>

  <!-- Pill strip -->
  <div class="stp-07__pills" id="stp-07-pills">
    <div class="stp-07__pill done"><div class="stp-07__pill-dot">✓</div><span class="stp-07__pill-label">Research</span></div>
    <div class="stp-07__sep">›</div>
    <div class="stp-07__pill done"><div class="stp-07__pill-dot">✓</div><span class="stp-07__pill-label">Wireframe</span></div>
    <div class="stp-07__sep">›</div>
    <div class="stp-07__pill active"><div class="stp-07__pill-dot">3</div><span class="stp-07__pill-label">Design</span></div>
    <div class="stp-07__sep">›</div>
    <div class="stp-07__pill"><div class="stp-07__pill-dot">4</div><span class="stp-07__pill-label">Prototype</span></div>
    <div class="stp-07__sep">›</div>
    <div class="stp-07__pill"><div class="stp-07__pill-dot">5</div><span class="stp-07__pill-label">Handoff</span></div>
    <div class="stp-07__sep">›</div>
    <div class="stp-07__pill"><div class="stp-07__pill-dot">6</div><span class="stp-07__pill-label">Launch</span></div>
  </div>

  <!-- Dashed dots -->
  <div class="stp-07__dots" id="stp-07-dotline">
    <div class="stp-07__dot-step done"><div class="stp-07__dot-node">✓</div><span class="stp-07__dot-label">Init</span></div>
    <div class="stp-07__dot-step done"><div class="stp-07__dot-node">✓</div><span class="stp-07__dot-label">Build</span></div>
    <div class="stp-07__dot-step active"><div class="stp-07__dot-node">3</div><span class="stp-07__dot-label">Test</span></div>
    <div class="stp-07__dot-step"><div class="stp-07__dot-node">4</div><span class="stp-07__dot-label">Stage</span></div>
    <div class="stp-07__dot-step"><div class="stp-07__dot-node">5</div><span class="stp-07__dot-label">Deploy</span></div>
    <div class="stp-07__dot-step"><div class="stp-07__dot-node">6</div><span class="stp-07__dot-label">Monitor</span></div>
    <div class="stp-07__dot-step"><div class="stp-07__dot-node">7</div><span class="stp-07__dot-label">Done</span></div>
  </div>

  <!-- Card -->
  <div class="stp-07__card">
    <div class="stp-07__card-top">
      <div class="stp-07__card-title" id="stp-07-title">Step 3 — Review & Iterate</div>
      <span class="stp-07__badge" id="stp-07-badge">In Progress</span>
    </div>
    <div class="stp-07__card-body" id="stp-07-body">Three different breadcrumb-style step trackers above are all in sync. Chevron arrows, pill strips, and dashed dot connectors each show the same progress state. Click Next or Back to advance all three simultaneously.</div>
    <div class="stp-07__card-nav">
      <button class="stp-07__btn stp-07__btn--ghost" id="stp-07-back">← Back</button>
      <button class="stp-07__btn stp-07__btn--primary" id="stp-07-next">Next Step →</button>
    </div>
  </div>
</div>
```
## CSS
```css
.stp-07,
.stp-07 *,
.stp-07 *::before,
.stp-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.stp-07 ::selection {
  background: #f59e0b;
  color: #000;
}

.stp-07 {
  --bg: #1c1400;
  --card: #241c00;
  --amber: #f59e0b;
  --yellow: #fbbf24;
  --gold: #d97706;
  --white: #fef3c7;
  --muted: #78614a;
  --border: #3d2e00;
  --dark: #0c0900;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 40px;
  background-image: radial-gradient(ellipse at 50% 0%,rgba(245,158,11,.07) 0%,transparent 60%);
}
/* ── Row 1: chevron breadcrumb track ── */

.stp-07__crumbs {
  display: flex;
  align-items: stretch;
  max-width: 720px;
  width: 100%;
  overflow: hidden;
  border-radius: 12px;
  border: 1px solid var(--border);
}

.stp-07__crumb {
  flex: 1;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 3px;
  padding: 16px 28px 16px 36px;
  background: var(--card);
  cursor: pointer;
  transition: background .3s;
  min-width: 0;
}

.stp-07__crumb:first-child {
  padding-left: 20px;
}
/* left cut */

.stp-07__crumb::before {
  content: '';
  position: absolute;
  left: -1px;
  top: 0;
  border-top: 40px solid transparent;
  border-bottom: 40px solid transparent;
  border-left: 18px solid var(--bg);
  z-index: 2;
}

.stp-07__crumb:first-child::before {
  display: none;
}
/* right chevron */

.stp-07__crumb::after {
  content: '';
  position: absolute;
  right: -18px;
  top: 0;
  border-top: 40px solid transparent;
  border-bottom: 40px solid transparent;
  border-left: 18px solid var(--card);
  z-index: 3;
  transition: border-left-color .3s;
}

.stp-07__crumb:last-child::after {
  display: none;
}

.stp-07__crumb.done {
  background: rgba(245,158,11,.12);
}

.stp-07__crumb.done::after {
  border-left-color: rgba(245,158,11,.12);
}

.stp-07__crumb.active {
  background: rgba(245,158,11,.2);
}

.stp-07__crumb.active::after {
  border-left-color: rgba(245,158,11,.2);
}

.stp-07__crumb-num {
  font-size: 11px;
  font-weight: 700;
  color: var(--muted);
  transition: color .3s;
}

.stp-07__crumb-name {
  font-size: 12px;
  font-weight: 600;
  color: var(--muted);
  transition: color .3s;
  white-space: nowrap;
}

.stp-07__crumb.done .stp-07__crumb-num,
.stp-07__crumb.done .stp-07__crumb-name {
  color: var(--amber);
}

.stp-07__crumb.active .stp-07__crumb-num,
.stp-07__crumb.active .stp-07__crumb-name {
  color: var(--yellow);
}
/* ── Row 2: pill badge strip ── */

.stp-07__pills {
  display: flex;
  align-items: center;
  gap: 0;
  max-width: 720px;
  width: 100%;
}

.stp-07__pill {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 18px;
  background: var(--card);
  border: 1px solid var(--border);
  border-right: none;
  cursor: pointer;
  transition: background .25s;
  position: relative;
}

.stp-07__pill:first-child {
  border-radius: 10px 0 0 10px;
}

.stp-07__pill:last-child {
  border-right: 1px solid var(--border);
  border-radius: 0 10px 10px 0;
}

.stp-07__pill-dot {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  font-weight: 700;
  background: var(--border);
  color: var(--muted);
  transition: all .3s;
}

.stp-07__pill-label {
  font-size: 12px;
  font-weight: 600;
  color: var(--muted);
  transition: color .25s;
  white-space: nowrap;
}

.stp-07__pill.done {
  background: rgba(245,158,11,.1);
}

.stp-07__pill.done .stp-07__pill-dot {
  background: var(--amber);
  color: #000;
}

.stp-07__pill.done .stp-07__pill-label {
  color: var(--amber);
}

.stp-07__pill.active {
  background: rgba(245,158,11,.18);
}

.stp-07__pill.active .stp-07__pill-dot {
  background: var(--yellow);
  color: #000;
  box-shadow: 0 0 0 3px rgba(251,191,36,.25);
}

.stp-07__pill.active .stp-07__pill-label {
  color: var(--yellow);
}
/* separator arrow */

.stp-07__sep {
  font-size: 12px;
  color: var(--muted);
  padding: 0 2px;
  background: var(--card);
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
}
/* ── Row 3: dashed step dots ── */

.stp-07__dots {
  display: flex;
  align-items: center;
  max-width: 720px;
  width: 100%;
}

.stp-07__dot-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  flex: 1;
  position: relative;
}

.stp-07__dot-step:not(:last-child)::after {
  content: '';
  position: absolute;
  top: 12px;
  left: calc(50% + 12px);
  width: calc(100% - 24px);
  height: 0;
  border-top: 2px dashed var(--border);
  transition: border-color .4s;
}

.stp-07__dot-step.done::after {
  border-color: var(--amber);
}

.stp-07__dot-step.done:nth-child(2)::after {
  border-color: var(--gold);
}

.stp-07__dot-node {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: 2px solid var(--border);
  background: var(--card);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  color: var(--muted);
  transition: all .35s cubic-bezier(.34,1.56,.64,1);
  font-weight: 700;
}

.stp-07__dot-step.done .stp-07__dot-node {
  border-color: var(--amber);
  background: var(--amber);
  color: #000;
}

.stp-07__dot-step.active .stp-07__dot-node {
  border-color: var(--yellow);
  background: var(--yellow);
  color: #000;
  box-shadow: 0 0 0 4px rgba(251,191,36,.2),0 0 16px rgba(251,191,36,.3);
  transform: scale(1.3);
}

.stp-07__dot-label {
  font-size: 10px;
  color: var(--muted);
  letter-spacing: .06em;
  text-transform: uppercase;
  text-align: center;
  transition: color .3s;
}

.stp-07__dot-step.done .stp-07__dot-label {
  color: var(--amber);
}

.stp-07__dot-step.active .stp-07__dot-label {
  color: var(--white);
}
/* content card */

.stp-07__card {
  max-width: 720px;
  width: 100%;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 28px 32px;
}

.stp-07__card-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.stp-07__card-title {
  font-size: 18px;
  font-weight: 700;
  color: var(--white);
}

.stp-07__badge {
  padding: 4px 12px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 700;
  background: rgba(245,158,11,.15);
  border: 1px solid rgba(245,158,11,.3);
  color: var(--amber);
}

.stp-07__card-body {
  font-size: 14px;
  color: var(--muted);
  line-height: 1.7;
}

.stp-07__card-nav {
  display: flex;
  justify-content: space-between;
  margin-top: 24px;
}

.stp-07__btn {
  padding: 10px 24px;
  border-radius: 8px;
  border: none;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all .2s;
}

.stp-07__btn--ghost {
  background: var(--border);
  color: var(--muted);
}

.stp-07__btn--ghost:hover {
  color: var(--white);
}

.stp-07__btn--primary {
  background: linear-gradient(135deg,var(--amber),var(--yellow));
  color: #000;
  box-shadow: 0 4px 16px rgba(245,158,11,.3);
}

.stp-07__btn--primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 24px rgba(245,158,11,.4);
}

@media (prefers-reduced-motion: reduce) {
  .stp-07__dot-step.active .stp-07__dot-node {
    transform: none;
  }
}
```

## JavaScript
```js
(function(){
  let cur=3;
  const crumbs=document.querySelectorAll('.stp-07__crumb');
  const pills=document.querySelectorAll('.stp-07__pill');
  const dots=document.querySelectorAll('.stp-07__dot-step');
  const title=document.getElementById('stp-07-title');
  const badge=document.getElementById('stp-07-badge');
  const body=document.getElementById('stp-07-body');

  const steps=[
    {t:'Step 1 — Discovery',b:'Gathering requirements and stakeholder input.',done:false},
    {t:'Step 2 — Proposal',b:'Crafting a detailed project proposal.',done:false},
    {t:'Step 3 — Review & Iterate',b:'Three different breadcrumb-style step trackers above are all in sync. Click Next or Back to advance all three simultaneously.',done:false},
    {t:'Step 4 — Approval',b:'Getting sign-off from all stakeholders.',done:false},
    {t:'Step 5 — Delivery',b:'Final deliverables packaged and shipped.',done:false},
  ];

  function update(){
    crumbs.forEach((c,i)=>{
      c.classList.remove('done','active');
      if(i+1<cur)c.classList.add('done');
      else if(i+1===cur)c.classList.add('active');
    });
    pills.forEach((p,i)=>{
      p.classList.remove('done','active');
      if(i+1<cur)p.classList.add('done');
      else if(i+1===cur)p.classList.add('active');
      const dot=p.querySelector('.stp-07__pill-dot');
      if(dot) dot.textContent=i+1<cur?'✓':i+1;
    });
    dots.forEach((d,i)=>{
      d.classList.remove('done','active');
      if(i+1<cur)d.classList.add('done');
      else if(i+1===cur)d.classList.add('active');
      const node=d.querySelector('.stp-07__dot-node');
      if(node) node.textContent=i+1<cur?'✓':i+1;
    });
    const s=steps[Math.min(cur,crumbs.length)-1]||steps[steps.length-1];
    title.textContent=s.t;
    body.textContent=s.b;
    badge.textContent=cur>crumbs.length?'Complete':'In Progress';
  }

  document.getElementById('stp-07-back').addEventListener('click',()=>{cur=Math.max(1,cur-1);update();});
  document.getElementById('stp-07-next').addEventListener('click',()=>{cur=Math.min(crumbs.length+1,cur+1);update();});
  update();
})();
```
