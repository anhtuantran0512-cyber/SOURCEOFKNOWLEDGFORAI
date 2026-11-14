---
source: "codefronts"
url: "https://codefronts.com/components/css-stepper-designs/css-animated-step-indicator-with-icons/"
title: "CSS Animated Step Indicator With Icons"
section: "components"
category: "css-stepper-designs"
category_name: "CSS Steppers"
description: "Icon bubble steps with a checkmark overlay pop animation, an SVG arc ring that advances its stroke-dashoffset per step, and a teal/emerald colour scheme —…"
has_js: "true"
---

Here's a working CSS Stepper from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Step Indicator With Icons
Source: https://codefronts.com/components/css-stepper-designs/css-animated-step-indicator-with-icons/

Icon bubble steps with a checkmark overlay pop animation, an SVG arc ring that advances its stroke-dashoffset per step, and a teal/emerald colour scheme — designed for onboarding and setup flows.
## HTML
```html
<div class="stp-05">
  <div class="stp-05__wrap">
    <div class="stp-05__label">Onboarding Flow</div>
    <div class="stp-05__title">Set Up Your Workspace</div>

    <div class="stp-05__stepper" id="stp-05-stepper">
      <div class="stp-05__item is-done" data-i="1">
        <div class="stp-05__bubble">🎨<div class="stp-05__check">✓</div></div>
        <span class="stp-05__name">Theme</span>
        <span class="stp-05__sub">Appearance</span>
      </div>
      <div class="stp-05__item is-done" data-i="2">
        <div class="stp-05__bubble">👥<div class="stp-05__check">✓</div></div>
        <span class="stp-05__name">Team</span>
        <span class="stp-05__sub">Invite members</span>
      </div>
      <div class="stp-05__item active" data-i="3">
        <div class="stp-05__bubble">🔗<div class="stp-05__check">✓</div></div>
        <span class="stp-05__name">Integrations</span>
        <span class="stp-05__sub">Connect apps</span>
      </div>
      <div class="stp-05__item" data-i="4">
        <div class="stp-05__bubble">📊<div class="stp-05__check">✓</div></div>
        <span class="stp-05__name">Analytics</span>
        <span class="stp-05__sub">Set up tracking</span>
      </div>
      <div class="stp-05__item" data-i="5">
        <div class="stp-05__bubble">🚀<div class="stp-05__check">✓</div></div>
        <span class="stp-05__name">Launch</span>
        <span class="stp-05__sub">Go live</span>
      </div>
    </div>

    <div class="stp-05__panel">
      <div class="stp-05__panel-inner" data-panel="1">
        <div class="stp-05__panel-title">Choose Your Theme</div>
        <div class="stp-05__panel-desc">Personalise your workspace with colours and typography that match your brand.</div>
        <div class="stp-05__tags"><span class="stp-05__tag">Dark Mode</span><span class="stp-05__tag">Custom Palette</span><span class="stp-05__tag">Font Scale</span></div>
      </div>
      <div class="stp-05__panel-inner" data-panel="2">
        <div class="stp-05__panel-title">Invite Your Team</div>
        <div class="stp-05__panel-desc">Add teammates by email. Assign roles and set permissions for each member.</div>
        <div class="stp-05__tags"><span class="stp-05__tag">Admin</span><span class="stp-05__tag">Editor</span><span class="stp-05__tag">Viewer</span></div>
      </div>
      <div class="stp-05__panel-inner active" data-panel="3">
        <div class="stp-05__panel-title">Connect Integrations</div>
        <div class="stp-05__panel-desc">Link your favourite tools — Slack, GitHub, Figma, Linear and more — to keep everything in sync.</div>
        <div class="stp-05__tags"><span class="stp-05__tag">Slack</span><span class="stp-05__tag">GitHub</span><span class="stp-05__tag">Figma</span><span class="stp-05__tag">Linear</span><span class="stp-05__tag">Notion</span></div>
        <div class="stp-05__progress">
          <svg class="stp-05__ring" viewBox="0 0 44 44">
            <circle class="bg" cx="22" cy="22" r="20"/>
            <circle class="fg" id="stp-05-ring" cx="22" cy="22" r="20"/>
          </svg>
          <div>
            <div class="stp-05__pct" id="stp-05-pct">40%</div>
            <div class="stp-05__pct-label">Overall Progress</div>
          </div>
        </div>
      </div>
      <div class="stp-05__panel-inner" data-panel="4">
        <div class="stp-05__panel-title">Configure Analytics</div>
        <div class="stp-05__panel-desc">Set up event tracking, conversion goals, and dashboard widgets to stay on top of performance.</div>
        <div class="stp-05__tags"><span class="stp-05__tag">Events</span><span class="stp-05__tag">Goals</span><span class="stp-05__tag">Funnels</span></div>
      </div>
      <div class="stp-05__panel-inner" data-panel="5">
        <div class="stp-05__panel-title">🚀 Ready to Launch!</div>
        <div class="stp-05__panel-desc">Your workspace is fully configured. Click Launch to go live and start collaborating with your team.</div>
        <div class="stp-05__tags"><span class="stp-05__tag">All systems go</span><span class="stp-05__tag">5 steps complete</span></div>
      </div>

      <div class="stp-05__nav">
        <button class="stp-05__btn stp-05__btn--prev" id="stp-05-prev">← Previous</button>
        <button class="stp-05__btn stp-05__btn--next" id="stp-05-next">Continue →</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.stp-05,
.stp-05 *,
.stp-05 *::before,
.stp-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.stp-05 ::selection {
  background: #059669;
  color: #fff;
}

.stp-05 {
  --bg: #041a14;
  --card: #071f18;
  --emerald: #10b981;
  --teal: #14b8a6;
  --lime: #84cc16;
  --dark: #d1fae5;
  --muted: #2d6a54;
  --border: #0d3d2e;
  --white: #ecfdf5;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  background-image: radial-gradient(ellipse at 30% 60%,rgba(16,185,129,.08) 0%,transparent 55%), radial-gradient(ellipse at 80% 20%,rgba(20,184,166,.06) 0%,transparent 40%);
}

.stp-05__wrap {
  max-width: 700px;
  width: 100%;
}

.stp-05__label {
  font-size: 10px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--emerald);
  font-weight: 700;
  text-align: center;
  margin-bottom: 12px;
}

.stp-05__title {
  font-size: 26px;
  font-weight: 800;
  color: var(--white);
  text-align: center;
  letter-spacing: -.02em;
  margin-bottom: 40px;
}
/* stepper */

.stp-05__stepper {
  display: flex;
  align-items: flex-start;
  gap: 0;
  margin-bottom: 48px;
}

.stp-05__item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  position: relative;
}
/* connector */

.stp-05__item:not(:last-child)::after {
  content: '';
  position: absolute;
  top: 32px;
  left: calc(50% + 32px);
  width: calc(100% - 64px);
  height: 2px;
  background: var(--border);
  transition: background .5s ease;
}

.stp-05__item.done::after {
  background: linear-gradient(90deg,var(--emerald),var(--teal));
  animation: stp-05-flash .4s ease;
}

@keyframes stp-05-flash {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}
/* icon bubble */

.stp-05__bubble {
  width: 64px;
  height: 64px;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 26px;
  background: var(--border);
  border: 2px solid var(--muted);
  transition: all .4s cubic-bezier(.34,1.56,.64,1);
  position: relative;
  overflow: hidden;
}

.stp-05__bubble::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg,rgba(255,255,255,.05),transparent);
  opacity: 0;
  transition: opacity .3s;
}

.stp-05__item.done .stp-05__bubble {
  background: linear-gradient(135deg,rgba(16,185,129,.25),rgba(20,184,166,.15));
  border-color: var(--emerald);
  box-shadow: 0 0 24px rgba(16,185,129,.3),inset 0 1px 0 rgba(255,255,255,.1);
}

.stp-05__item.done .stp-05__bubble::before {
  opacity: 1;
}

.stp-05__item.active .stp-05__bubble {
  background: linear-gradient(135deg,rgba(16,185,129,.15),rgba(132,204,22,.1));
  border-color: var(--teal);
  box-shadow: 0 0 0 6px rgba(16,185,129,.1),0 0 32px rgba(16,185,129,.3);
  animation: stp-05-bob 2.5s ease-in-out infinite;
}

@keyframes stp-05-bob {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-4px);
  }
}
/* checkmark overlay */

.stp-05__check {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  background: linear-gradient(135deg,var(--emerald),var(--teal));
  border-radius: 18px;
  opacity: 0;
  transform: scale(.5);
  transition: all .3s cubic-bezier(.34,1.56,.64,1);
}

.stp-05__item.done .stp-05__check {
  opacity: 1;
  transform: scale(1);
}

.stp-05__name {
  font-size: 12px;
  font-weight: 600;
  color: var(--muted);
  text-align: center;
  letter-spacing: .04em;
  text-transform: uppercase;
  transition: color .3s;
}

.stp-05__item.done .stp-05__name {
  color: var(--emerald);
}

.stp-05__item.active .stp-05__name {
  color: var(--white);
}

.stp-05__sub {
  font-size: 11px;
  color: var(--border);
  text-align: center;
  transition: color .3s;
}

.stp-05__item.active .stp-05__sub {
  color: var(--muted);
}

.stp-05__item.done .stp-05__sub {
  color: var(--muted);
}
/* content panel */

.stp-05__panel {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 28px 32px;
  min-height: 200px;
  position: relative;
  overflow: hidden;
}

.stp-05__panel::before {
  content: '';
  position: absolute;
  top: -60px;
  right: -60px;
  width: 180px;
  height: 180px;
  border-radius: 50%;
  background: radial-gradient(circle,rgba(16,185,129,.08),transparent);
}

.stp-05__panel-inner {
  display: none;
}

.stp-05__panel-inner.active {
  display: block;
  animation: stp-05-in .35s ease;
}

@keyframes stp-05-in {
  from {
    opacity: 0;
    transform: translateX(10px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.stp-05__panel-title {
  font-size: 18px;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 8px;
}

.stp-05__panel-desc {
  font-size: 14px;
  color: var(--muted);
  line-height: 1.7;
  margin-bottom: 20px;
}

.stp-05__tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

.stp-05__tag {
  padding: 4px 12px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 600;
  background: rgba(16,185,129,.12);
  border: 1px solid rgba(16,185,129,.25);
  color: var(--emerald);
}

.stp-05__nav {
  display: flex;
  justify-content: space-between;
  margin-top: 24px;
}

.stp-05__btn {
  padding: 10px 24px;
  border-radius: 10px;
  border: none;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all .2s;
}

.stp-05__btn--prev {
  background: var(--border);
  color: var(--muted);
}

.stp-05__btn--prev:hover {
  color: var(--white);
}

.stp-05__btn--next {
  background: linear-gradient(135deg,var(--emerald),var(--teal));
  color: #fff;
  box-shadow: 0 4px 16px rgba(16,185,129,.3);
}

.stp-05__btn--next:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 24px rgba(16,185,129,.4);
}
/* progress ring */

.stp-05__progress {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  margin-bottom: 20px;
}

.stp-05__ring {
  width: 52px;
  height: 52px;
}

.stp-05__ring circle {
  fill: none;
  stroke-width: 4;
  stroke-linecap: round;
}

.stp-05__ring .bg {
  stroke: var(--border);
}

.stp-05__ring .fg {
  stroke: var(--emerald);
  stroke-dasharray: 126;
  stroke-dashoffset: 126;
  transform: rotate(-90deg);
  transform-origin: center;
  transition: stroke-dashoffset .5s ease;
}

.stp-05__pct {
  font-size: 13px;
  font-weight: 700;
  color: var(--emerald);
}

.stp-05__pct-label {
  font-size: 12px;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .stp-05__item.active .stp-05__bubble {
    animation: none;
  }

  .stp-05__item.done::after,
    .stp-05__panel-inner.active {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  let cur=3;
  const items=document.querySelectorAll('.stp-05__item');
  const panels=document.querySelectorAll('.stp-05__panel-inner');
  const ring=document.getElementById('stp-05-ring');
  const pct=document.getElementById('stp-05-pct');
  const total=5;

  function update(){
    items.forEach((item,i)=>{
      item.classList.remove('done','active','is-done');
      if(i+1<cur) item.classList.add('done');
      else if(i+1===cur) item.classList.add('active');
    });
    panels.forEach(p=>{
      p.classList.remove('active');
      if(parseInt(p.dataset.panel)===cur) p.classList.add('active');
    });
    const p=((cur-1)/(total-1)*100).toFixed(0);
    const offset=126-(126*(cur-1)/(total-1));
    ring.style.strokeDashoffset=offset;
    pct.textContent=p+'%';
    document.getElementById('stp-05-prev').disabled=cur<=1;
    document.getElementById('stp-05-next').textContent=cur===total?'Launch 🚀':'Continue →';
  }

  document.getElementById('stp-05-prev').addEventListener('click',()=>{cur=Math.max(1,cur-1);update();});
  document.getElementById('stp-05-next').addEventListener('click',()=>{cur=Math.min(total,cur+1);update();});
  update();
})();
```
