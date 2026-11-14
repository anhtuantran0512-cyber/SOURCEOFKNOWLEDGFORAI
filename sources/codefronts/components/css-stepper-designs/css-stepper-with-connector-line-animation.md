---
source: "codefronts"
url: "https://codefronts.com/components/css-stepper-designs/css-stepper-with-connector-line-animation/"
title: "CSS Stepper With Connector Line Animation"
section: "components"
category: "css-stepper-designs"
category_name: "CSS Steppers"
description: "Animated fill connector lines in both horizontal and vertical layouts — a shimmer sweep runs along the line as each step completes, with ripple ring bursts…"
has_js: "true"
---

Here's a working CSS Stepper from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Stepper With Connector Line Animation
Source: https://codefronts.com/components/css-stepper-designs/css-stepper-with-connector-line-animation/

Animated fill connector lines in both horizontal and vertical layouts — a shimmer sweep runs along the line as each step completes, with ripple ring bursts on the active node and a rose/orange/amber gradient palette.
## HTML
```html
<div class="stp-12">
  <div class="stp-12__wrap">

    <!-- Horizontal with animated fill -->
    <div class="stp-12__horz">
      <div class="stp-12__horz-label">Horizontal — Animated Connector Fill</div>
      <div class="stp-12__h-track" id="stp-12-h">
        <div class="stp-12__h-step done" data-hi="1">
          <div class="stp-12__h-node">✓</div>
          <span class="stp-12__h-label">Initiate</span>
        </div>
        <div class="stp-12__h-connector" data-ci="1"><div class="stp-12__h-connector-fill" style="width:100%"></div></div>
        <div class="stp-12__h-step done" data-hi="2">
          <div class="stp-12__h-node">✓</div>
          <span class="stp-12__h-label">Configure</span>
        </div>
        <div class="stp-12__h-connector active" data-ci="2"><div class="stp-12__h-connector-fill" style="width:60%"></div></div>
        <div class="stp-12__h-step active" data-hi="3">
          <div class="stp-12__h-node">3</div>
          <span class="stp-12__h-label">Build</span>
        </div>
        <div class="stp-12__h-connector" data-ci="3"><div class="stp-12__h-connector-fill" style="width:0%"></div></div>
        <div class="stp-12__h-step" data-hi="4">
          <div class="stp-12__h-node">4</div>
          <span class="stp-12__h-label">Test</span>
        </div>
        <div class="stp-12__h-connector" data-ci="4"><div class="stp-12__h-connector-fill" style="width:0%"></div></div>
        <div class="stp-12__h-step" data-hi="5">
          <div class="stp-12__h-node">5</div>
          <span class="stp-12__h-label">Deploy</span>
        </div>
      </div>
    </div>

    <!-- Vertical with animated fill lines -->
    <div class="stp-12__vert" id="stp-12-v">

      <div class="stp-12__v-entry done" data-vi="1">
        <div class="stp-12__v-spine" style="grid-column:1;grid-row:1 / span 1">
          <div class="stp-12__v-node">✓</div>
          <div class="stp-12__v-line"><div class="stp-12__v-line-fill" style="height:100%"></div></div>
        </div>
        <div class="stp-12__v-content" style="grid-column:2;grid-row:1">
          <div class="stp-12__v-step-tag">Step 01 · Completed</div>
          <div class="stp-12__v-title">Project Kickoff</div>
          <div class="stp-12__v-desc">Stakeholder alignment, scope definition, and milestone planning locked in.</div>
          <div class="stp-12__v-meta">✓ Completed 3 Jan 2026</div>
        </div>
      </div>

      <div class="stp-12__v-entry done" data-vi="2">
        <div class="stp-12__v-spine" style="grid-column:1;grid-row:2 / span 1">
          <div class="stp-12__v-node">✓</div>
          <div class="stp-12__v-line"><div class="stp-12__v-line-fill" style="height:100%"></div></div>
        </div>
        <div class="stp-12__v-content" style="grid-column:2;grid-row:2">
          <div class="stp-12__v-step-tag">Step 02 · Completed</div>
          <div class="stp-12__v-title">Design Phase</div>
          <div class="stp-12__v-desc">Wireframes approved, component library built, and brand tokens exported.</div>
          <div class="stp-12__v-meta">✓ Completed 14 Feb 2026</div>
        </div>
      </div>

      <div class="stp-12__v-entry active" data-vi="3">
        <div class="stp-12__v-spine" style="grid-column:1;grid-row:3 / span 1">
          <div class="stp-12__v-node">3</div>
          <div class="stp-12__v-line"><div class="stp-12__v-line-fill" style="height:0%"></div></div>
        </div>
        <div class="stp-12__v-content" style="grid-column:2;grid-row:3">
          <div class="stp-12__v-step-tag">Step 03 · In Progress</div>
          <div class="stp-12__v-title">Development Sprint</div>
          <div class="stp-12__v-desc">Feature development, API integration, and unit test coverage underway.</div>
          <div class="stp-12__v-meta">● Started 1 Mar 2026</div>
        </div>
      </div>

      <div class="stp-12__v-entry" data-vi="4">
        <div class="stp-12__v-spine" style="grid-column:1;grid-row:4 / span 1">
          <div class="stp-12__v-node">4</div>
          <div class="stp-12__v-line"><div class="stp-12__v-line-fill" style="height:0%"></div></div>
        </div>
        <div class="stp-12__v-content" style="grid-column:2;grid-row:4">
          <div class="stp-12__v-step-tag">Step 04</div>
          <div class="stp-12__v-title">QA &amp; Staging</div>
          <div class="stp-12__v-desc">Full regression, performance audits, and stakeholder UAT on staging.</div>
          <div class="stp-12__v-meta">— Scheduled Apr 2026</div>
        </div>
      </div>

      <div class="stp-12__v-entry" data-vi="5">
        <div class="stp-12__v-spine" style="grid-column:1;grid-row:5 / span 1">
          <div class="stp-12__v-node">5</div>
          <!-- no line after last -->
        </div>
        <div class="stp-12__v-content" style="grid-column:2;grid-row:5">
          <div class="stp-12__v-step-tag">Step 05</div>
          <div class="stp-12__v-title">Production Launch</div>
          <div class="stp-12__v-desc">Canary rollout, monitoring alerts active, and public release.</div>
          <div class="stp-12__v-meta">— Scheduled May 2026</div>
        </div>
      </div>

    </div>

    <!-- Nav -->
    <div class="stp-12__nav">
      <button class="stp-12__btn stp-12__btn--ghost" id="stp-12-back">← Previous</button>
      <button class="stp-12__btn stp-12__btn--primary" id="stp-12-next">Mark Complete →</button>
    </div>
  </div>
</div>
```
## CSS
```css
.stp-12,
.stp-12 *,
.stp-12 *::before,
.stp-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.stp-12 ::selection {
  background: #f43f5e;
  color: #fff;
}

.stp-12 {
  --bg: #fef2f2;
  --white: #fff;
  --rose: #f43f5e;
  --orange: #fb923c;
  --amber: #fbbf24;
  --dark: #1c0a0a;
  --mid: #7f1d1d;
  --muted: #f87171;
  --border: #fde8e8;
  --grad: linear-gradient(90deg,#f43f5e,#fb923c,#fbbf24);
  --gradv: linear-gradient(180deg,#f43f5e,#fb923c,#fbbf24);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background-image: radial-gradient(ellipse at 20% 80%,rgba(244,63,94,.06),transparent 50%), radial-gradient(ellipse at 80% 20%,rgba(251,146,60,.06),transparent 50%);
}

.stp-12__wrap {
  max-width: 740px;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 64px;
}
/* ── Horizontal animated connector ── */

.stp-12__horz {
  width: 100%;
}

.stp-12__horz-label {
  font-size: 11px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 700;
  text-align: center;
  margin-bottom: 28px;
}

.stp-12__h-track {
  display: flex;
  align-items: center;
  position: relative;
}

.stp-12__h-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
  position: relative;
  z-index: 1;
}

.stp-12__h-connector {
  flex: 1;
  height: 4px;
  background: var(--border);
  border-radius: 2px;
  position: relative;
  overflow: hidden;
  margin: 0 -2px;
}

.stp-12__h-connector-fill {
  height: 100%;
  width: 0%;
  border-radius: 2px;
  background: var(--grad);
  transition: width .6s cubic-bezier(.4,0,.2,1);
  position: relative;
}
/* shimmer on connector fill */

.stp-12__h-connector-fill::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg,transparent,rgba(255,255,255,.5),transparent);
  background-size: 200% 100%;
  animation: stp-12-shimmer 1.5s linear infinite;
  opacity: 0;
}

.stp-12__h-connector.active .stp-12__h-connector-fill::after {
  opacity: 1;
}

@keyframes stp-12-shimmer {
  0% {
    background-position: 200%;
  }

  100% {
    background-position: -200%;
  }
}

.stp-12__h-node {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: 700;
  background: var(--white);
  border: 3px solid var(--border);
  color: #c4b0b0;
  transition: all .4s cubic-bezier(.34,1.56,.64,1);
  position: relative;
  box-shadow: 0 2px 12px rgba(244,63,94,.06);
}
/* ripple ring on active */

.stp-12__h-node::before {
  content: '';
  position: absolute;
  inset: -6px;
  border-radius: 50%;
  border: 2px solid var(--rose);
  opacity: 0;
  transition: all .4s;
}

.stp-12__h-step.done .stp-12__h-node {
  background: var(--grad);
  border-color: transparent;
  color: #fff;
  box-shadow: 0 4px 20px rgba(244,63,94,.3);
}

.stp-12__h-step.active .stp-12__h-node {
  border-color: var(--rose);
  color: var(--rose);
  box-shadow: 0 4px 24px rgba(244,63,94,.25);
  animation: stp-12-ring 2s ease-in-out infinite;
}

.stp-12__h-step.active .stp-12__h-node::before {
  opacity: .4;
  animation: stp-12-ripple 1.5s ease-out infinite;
}

@keyframes stp-12-ring {
  0%,
    100% {
    box-shadow: 0 4px 24px rgba(244,63,94,.25);
  }

  50% {
    box-shadow: 0 4px 36px rgba(244,63,94,.45);
  }
}

@keyframes stp-12-ripple {
  0% {
    opacity: .5;
    transform: scale(1);
  }

  100% {
    opacity: 0;
    transform: scale(1.4);
  }
}

.stp-12__h-label {
  font-size: 11px;
  font-weight: 600;
  color: #c4b0b0;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: .06em;
  transition: color .3s;
  max-width: 64px;
}

.stp-12__h-step.done .stp-12__h-label {
  color: var(--rose);
}

.stp-12__h-step.active .stp-12__h-label {
  color: var(--dark);
}
/* ── Vertical animated connector ── */

.stp-12__vert {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 0 20px;
  align-items: stretch;
}

.stp-12__v-spine {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 6px;
}

.stp-12__v-node {
  width: 44px;
  height: 44px;
  border-radius: 14px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 700;
  background: var(--white);
  border: 2px solid var(--border);
  color: #c4b0b0;
  transition: all .4s cubic-bezier(.34,1.56,.64,1);
  box-shadow: 0 2px 8px rgba(244,63,94,.06);
}

.stp-12__v-entry.done .stp-12__v-node {
  background: var(--gradv);
  border-color: transparent;
  color: #fff;
  box-shadow: 0 4px 16px rgba(244,63,94,.3);
}

.stp-12__v-entry.active .stp-12__v-node {
  border-color: var(--rose);
  color: var(--rose);
  box-shadow: 0 4px 20px rgba(244,63,94,.2),0 0 0 4px rgba(244,63,94,.1);
}

.stp-12__v-line {
  width: 4px;
  flex: 1;
  min-height: 24px;
  margin: 6px 0;
  border-radius: 2px;
  background: var(--border);
  position: relative;
  overflow: hidden;
}

.stp-12__v-line-fill {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 0%;
  background: var(--gradv);
  border-radius: 2px;
  transition: height .6s cubic-bezier(.4,0,.2,1);
}

.stp-12__v-entry.done+.stp-12__v-gap .stp-12__v-line-fill {
  height: 100%;
}

.stp-12__v-entry {
  display: contents;
}

.stp-12__v-content {
  padding: 6px 0 28px;
}

.stp-12__v-entry:last-child .stp-12__v-content {
  padding-bottom: 0;
}

.stp-12__v-step-tag {
  font-size: 10px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: #c4b0b0;
  font-weight: 700;
  margin-bottom: 4px;
}

.stp-12__v-entry.done .stp-12__v-step-tag,
.stp-12__v-entry.active .stp-12__v-step-tag {
  color: var(--rose);
}

.stp-12__v-title {
  font-size: 17px;
  font-weight: 700;
  color: #c4b0b0;
  margin-bottom: 4px;
  transition: color .3s;
}

.stp-12__v-entry.done .stp-12__v-title,
.stp-12__v-entry.active .stp-12__v-title {
  color: var(--dark);
}

.stp-12__v-desc {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.6;
}

.stp-12__v-entry.active .stp-12__v-desc {
  color: var(--mid);
}

.stp-12__v-meta {
  font-size: 11px;
  color: #c4b0b0;
  margin-top: 6px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.stp-12__v-entry.done .stp-12__v-meta {
  color: var(--rose);
}

.stp-12__v-entry.active .stp-12__v-meta {
  color: var(--rose);
}
/* nav row */

.stp-12__nav {
  display: flex;
  justify-content: center;
  gap: 12px;
}

.stp-12__btn {
  padding: 12px 28px;
  border-radius: 12px;
  border: none;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  transition: all .2s;
}

.stp-12__btn--ghost {
  background: var(--white);
  border: 1.5px solid var(--border);
  color: var(--muted);
}

.stp-12__btn--ghost:hover {
  border-color: var(--rose);
  color: var(--dark);
}

.stp-12__btn--primary {
  background: var(--grad);
  color: #fff;
  box-shadow: 0 4px 20px rgba(244,63,94,.3);
}

.stp-12__btn--primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 32px rgba(244,63,94,.4);
}

@media (prefers-reduced-motion: reduce) {
  .stp-12__h-step.active .stp-12__h-node {
    animation: none;
  }

  .stp-12__h-step.active .stp-12__h-node::before {
    animation: none;
  }

  .stp-12__h-connector-fill::after {
    animation: none;
  }

  .stp-12__h-connector-fill,
    .stp-12__v-line-fill {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  let cur=3;
  const hSteps=document.querySelectorAll('.stp-12__h-step');
  const hCons=document.querySelectorAll('.stp-12__h-connector');
  const vEntries=document.querySelectorAll('.stp-12__v-entry');
  const total=5;

  const vMeta=[
    '✓ Completed 3 Jan 2026','✓ Completed 14 Feb 2026',
    '● Started 1 Mar 2026','— Scheduled Apr 2026','— Scheduled May 2026'
  ];
  const vTags=['Step 01 · Completed','Step 02 · Completed','Step 03 · In Progress','Step 04','Step 05'];

  function update(){
    // horizontal
    hSteps.forEach((s,i)=>{
      s.classList.remove('done','active');
      const node=s.querySelector('.stp-12__h-node');
      if(i+1<cur){s.classList.add('done');node.textContent='✓';}
      else if(i+1===cur){s.classList.add('active');node.textContent=cur;}
      else node.textContent=i+1;
    });
    hCons.forEach((c,i)=>{
      c.classList.remove('active');
      const fill=c.querySelector('.stp-12__h-connector-fill');
      if(i+1<cur){fill.style.width='100%';}
      else if(i+1===cur){c.classList.add('active');fill.style.width='55%';}
      else fill.style.width='0%';
    });
    // vertical
    vEntries.forEach((e,i)=>{
      e.classList.remove('done','active');
      const node=e.querySelector('.stp-12__v-node');
      const tag=e.querySelector('.stp-12__v-step-tag');
      const meta=e.querySelector('.stp-12__v-meta');
      const lineFill=e.querySelector('.stp-12__v-line-fill');
      if(i+1<cur){
        e.classList.add('done');node.textContent='✓';
        if(tag) tag.textContent=vTags[i].replace('In Progress','Completed').replace('Step 0'+String(i+1),'Step 0'+String(i+1)+' · Completed');
        if(lineFill) lineFill.style.height='100%';
      } else if(i+1===cur){
        e.classList.add('active');node.textContent=cur;
        if(tag) tag.textContent='Step 0'+cur+' · In Progress';
        if(lineFill) lineFill.style.height='0%';
      } else {
        node.textContent=i+1;
        if(tag) tag.textContent='Step 0'+(i+1);
        if(lineFill) lineFill.style.height='0%';
      }
    });
  }

  document.getElementById('stp-12-back').addEventListener('click',()=>{cur=Math.max(1,cur-1);update();});
  document.getElementById('stp-12-next').addEventListener('click',()=>{cur=Math.min(total,cur+1);update();});
  update();
})();
```
