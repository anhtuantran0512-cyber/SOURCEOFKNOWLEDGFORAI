---
source: "codefronts"
url: "https://codefronts.com/components/css-stepper-designs/css-onboarding-stepper-flow/"
title: "CSS Onboarding Stepper Flow"
section: "components"
category: "css-stepper-designs"
category_name: "CSS Steppers"
description: "A full-panel onboarding layout with a left sidebar step list, animated slide-in content panels, choice card selections, a live progress bar, and a coral/rose…"
has_js: "true"
---

Here's a working CSS Stepper from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Onboarding Stepper Flow
Source: https://codefronts.com/components/css-stepper-designs/css-onboarding-stepper-flow/

A full-panel onboarding layout with a left sidebar step list, animated slide-in content panels, choice card selections, a live progress bar, and a coral/rose colour scheme built for SaaS welcome flows.
## HTML
```html
<div class="stp-06">
  <div class="stp-06__outer">
    <!-- Sidebar -->
    <div class="stp-06__sidebar">
      <div class="stp-06__brand">Sprout <span>·</span> Setup</div>
      <nav class="stp-06__nav" id="stp-06-nav">
        <div class="stp-06__nav-item done"><div class="stp-06__nav-dot">✓</div><span class="stp-06__nav-text">Your Account</span></div>
        <div class="stp-06__nav-item done"><div class="stp-06__nav-dot">✓</div><span class="stp-06__nav-text">Your Goal</span></div>
        <div class="stp-06__nav-item active"><div class="stp-06__nav-dot">3</div><span class="stp-06__nav-text">Your Team</span></div>
        <div class="stp-06__nav-item"><div class="stp-06__nav-dot">4</div><span class="stp-06__nav-text">Workspace</span></div>
        <div class="stp-06__nav-item"><div class="stp-06__nav-dot">5</div><span class="stp-06__nav-text">Finish</span></div>
      </nav>
      <div class="stp-06__sidebar-progress">
        <div class="stp-06__sidebar-progress-label">Setup progress — <span id="stp-06-pct">40%</span></div>
        <div class="stp-06__sidebar-bar"><div class="stp-06__sidebar-fill" id="stp-06-fill" style="width:40%"></div></div>
      </div>
    </div>

    <!-- Content -->
    <div class="stp-06__content">
      <div class="stp-06__step-display" id="stp-06-step-display">Step 3 of 5</div>
      <div class="stp-06__step-title" id="stp-06-step-title">Tell Us About Your Team</div>
      <div class="stp-06__step-desc" id="stp-06-step-desc">We'll tailor the experience for your team size and structure.</div>

      <div class="stp-06__pane" data-pane="1">
        <div class="stp-06__field"><label class="stp-06__fl">Full Name</label><input class="stp-06__in" placeholder="Jamie Rivers" value="Jamie Rivers"></div>
        <div class="stp-06__field"><label class="stp-06__fl">Work Email</label><input class="stp-06__in" placeholder="[email protected]" value="[email protected]"></div>
        <div class="stp-06__row">
          <div class="stp-06__field"><label class="stp-06__fl">Password</label><input class="stp-06__in" type="password" placeholder="••••••••"></div>
          <div class="stp-06__field"><label class="stp-06__fl">Confirm</label><input class="stp-06__in" type="password" placeholder="••••••••"></div>
        </div>
      </div>

      <div class="stp-06__pane" data-pane="2">
        <div class="stp-06__choices">
          <div class="stp-06__choice"><div class="stp-06__choice-icon">📈</div><div class="stp-06__choice-name">Grow Sales</div><div class="stp-06__choice-desc">Increase revenue & leads</div></div>
          <div class="stp-06__choice picked"><div class="stp-06__choice-icon">🤝</div><div class="stp-06__choice-name">Improve CX</div><div class="stp-06__choice-desc">Better customer experience</div></div>
          <div class="stp-06__choice"><div class="stp-06__choice-icon">⚙️</div><div class="stp-06__choice-name">Automate</div><div class="stp-06__choice-desc">Streamline operations</div></div>
          <div class="stp-06__choice"><div class="stp-06__choice-icon">🎯</div><div class="stp-06__choice-name">Analytics</div><div class="stp-06__choice-desc">Data-driven decisions</div></div>
        </div>
      </div>

      <div class="stp-06__pane active" data-pane="3">
        <div class="stp-06__choices">
          <div class="stp-06__choice"><div class="stp-06__choice-icon">👤</div><div class="stp-06__choice-name">Solo</div><div class="stp-06__choice-desc">Just me</div></div>
          <div class="stp-06__choice picked"><div class="stp-06__choice-icon">👥</div><div class="stp-06__choice-name">Small</div><div class="stp-06__choice-desc">2–10 people</div></div>
          <div class="stp-06__choice"><div class="stp-06__choice-icon">🏢</div><div class="stp-06__choice-name">Mid</div><div class="stp-06__choice-desc">11–50 people</div></div>
          <div class="stp-06__choice"><div class="stp-06__choice-icon">🏙️</div><div class="stp-06__choice-name">Enterprise</div><div class="stp-06__choice-desc">50+ people</div></div>
        </div>
      </div>

      <div class="stp-06__pane" data-pane="4">
        <div class="stp-06__field"><label class="stp-06__fl">Workspace Name</label><input class="stp-06__in" placeholder="Acme Corp Workspace"></div>
        <div class="stp-06__field"><label class="stp-06__fl">Workspace URL</label><input class="stp-06__in" placeholder="acme.sprout.io"></div>
        <div class="stp-06__field"><label class="stp-06__fl">Industry</label><input class="stp-06__in" placeholder="SaaS / Technology"></div>
      </div>

      <div class="stp-06__pane" data-pane="5">
        <div style="text-align:center;padding:20px 0">
          <div style="font-size:56px;margin-bottom:16px;animation:stp-06-in .4s ease">🎉</div>
          <div style="font-size:22px;font-weight:800;color:var(--dark);margin-bottom:8px">You're all set!</div>
          <div style="font-size:14px;color:#9ca3af">Your workspace is ready. Let's start growing together.</div>
        </div>
      </div>

      <div class="stp-06__footer">
        <button class="stp-06__skip" id="stp-06-skip">Skip this step</button>
        <div class="stp-06__foot-right">
          <button class="stp-06__btn stp-06__btn--ghost" id="stp-06-back">Back</button>
          <button class="stp-06__btn stp-06__btn--primary" id="stp-06-next">Continue →</button>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.stp-06,
.stp-06 *,
.stp-06 *::before,
.stp-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.stp-06 ::selection {
  background: #e11d48;
  color: #fff;
}

.stp-06 {
  --bg: #fff1f2;
  --white: #fff;
  --rose: #e11d48;
  --pink: #fb7185;
  --coral: #f43f5e;
  --dark: #1a0510;
  --mid: #9f1239;
  --muted: #fda4af;
  --border: #fecdd3;
  --success: #059669;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

.stp-06__outer {
  max-width: 900px;
  width: 100%;
  display: grid;
  grid-template-columns: 260px 1fr;
  background: var(--white);
  border-radius: 24px;
  box-shadow: 0 24px 80px rgba(225,29,72,.12),0 0 0 1px var(--border);
  overflow: hidden;
  min-height: 520px;
}
/* left sidebar nav */

.stp-06__sidebar {
  background: linear-gradient(180deg,var(--rose),var(--coral));
  padding: 40px 24px;
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
}

.stp-06__sidebar::before {
  content: '';
  position: absolute;
  top: -60px;
  right: -60px;
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background: rgba(255,255,255,.08);
}

.stp-06__sidebar::after {
  content: '';
  position: absolute;
  bottom: -40px;
  left: -40px;
  width: 140px;
  height: 140px;
  border-radius: 50%;
  background: rgba(255,255,255,.06);
}

.stp-06__brand {
  font-size: 20px;
  font-weight: 800;
  color: #fff;
  letter-spacing: -.02em;
  margin-bottom: 36px;
  position: relative;
  z-index: 1;
}

.stp-06__brand span {
  opacity: .6;
  font-weight: 400;
}

.stp-06__nav {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 6px;
  position: relative;
  z-index: 1;
}

.stp-06__nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 14px;
  border-radius: 12px;
  cursor: pointer;
  transition: all .25s;
}

.stp-06__nav-item.done {
  background: rgba(255,255,255,.12);
}

.stp-06__nav-item.active {
  background: rgba(255,255,255,.2);
  box-shadow: 0 2px 12px rgba(0,0,0,.1);
}

.stp-06__nav-dot {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 700;
  background: rgba(255,255,255,.15);
  color: rgba(255,255,255,.5);
  transition: all .3s;
  border: 1.5px solid rgba(255,255,255,.2);
}

.stp-06__nav-item.done .stp-06__nav-dot {
  background: rgba(255,255,255,.9);
  color: var(--rose);
  border-color: transparent;
}

.stp-06__nav-item.active .stp-06__nav-dot {
  background: #fff;
  color: var(--rose);
  border-color: transparent;
  box-shadow: 0 0 0 3px rgba(255,255,255,.3);
}

.stp-06__nav-text {
  font-size: 13px;
  font-weight: 600;
  color: rgba(255,255,255,.5);
  transition: color .3s;
}

.stp-06__nav-item.done .stp-06__nav-text {
  color: rgba(255,255,255,.8);
}

.stp-06__nav-item.active .stp-06__nav-text {
  color: #fff;
}
/* sidebar progress bar */

.stp-06__sidebar-progress {
  margin-top: auto;
  position: relative;
  z-index: 1;
  padding-top: 24px;
}

.stp-06__sidebar-progress-label {
  font-size: 11px;
  color: rgba(255,255,255,.6);
  margin-bottom: 8px;
}

.stp-06__sidebar-bar {
  height: 4px;
  background: rgba(255,255,255,.2);
  border-radius: 2px;
  overflow: hidden;
}

.stp-06__sidebar-fill {
  height: 100%;
  background: #fff;
  border-radius: 2px;
  transition: width .4s ease;
}
/* right content */

.stp-06__content {
  padding: 48px 40px;
  display: flex;
  flex-direction: column;
}

.stp-06__step-display {
  font-size: 11px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 600;
  margin-bottom: 6px;
}

.stp-06__step-title {
  font-size: 26px;
  font-weight: 800;
  color: var(--dark);
  letter-spacing: -.02em;
  margin-bottom: 6px;
}

.stp-06__step-desc {
  font-size: 14px;
  color: #9ca3af;
  line-height: 1.7;
  margin-bottom: 28px;
}
/* panels */

.stp-06__pane {
  display: none;
  flex: 1;
}

.stp-06__pane.active {
  display: block;
  animation: stp-06-in .3s ease;
}

@keyframes stp-06-in {
  from {
    opacity: 0;
    transform: translateY(8px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.stp-06__field {
  margin-bottom: 16px;
}

.stp-06__fl {
  font-size: 12px;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #6b7280;
  margin-bottom: 6px;
  display: block;
}

.stp-06__in {
  width: 100%;
  padding: 12px 16px;
  background: #f9fafb;
  border: 1.5px solid #e5e7eb;
  border-radius: 10px;
  color: var(--dark);
  font-size: 14px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.stp-06__in:focus {
  background: #fff;
  border-color: var(--rose);
  box-shadow: 0 0 0 3px rgba(225,29,72,.1);
}

.stp-06__row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}
/* choice cards */

.stp-06__choices {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 20px;
}

.stp-06__choice {
  padding: 16px;
  border-radius: 12px;
  border: 2px solid #e5e7eb;
  cursor: pointer;
  transition: all .25s;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 6px;
}

.stp-06__choice:hover {
  border-color: var(--pink);
  background: #fff1f2;
}

.stp-06__choice.picked {
  border-color: var(--rose);
  background: #fff1f2;
  box-shadow: 0 0 0 3px rgba(225,29,72,.1);
}

.stp-06__choice-icon {
  font-size: 22px;
}

.stp-06__choice-name {
  font-size: 13px;
  font-weight: 700;
  color: var(--dark);
}

.stp-06__choice-desc {
  font-size: 11px;
  color: #9ca3af;
}
/* nav buttons */

.stp-06__footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: auto;
  padding-top: 24px;
  border-top: 1px solid var(--border);
}

.stp-06__skip {
  font-size: 13px;
  color: #9ca3af;
  cursor: pointer;
  background: none;
  border: none;
  transition: color .2s;
}

.stp-06__skip:hover {
  color: var(--dark);
}

.stp-06__foot-right {
  display: flex;
  gap: 10px;
}

.stp-06__btn {
  padding: 11px 24px;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  border: none;
  transition: all .2s;
}

.stp-06__btn--ghost {
  background: #f3f4f6;
  color: #6b7280;
}

.stp-06__btn--ghost:hover {
  background: #e5e7eb;
  color: var(--dark);
}

.stp-06__btn--primary {
  background: linear-gradient(135deg,var(--rose),var(--coral));
  color: #fff;
  box-shadow: 0 4px 16px rgba(225,29,72,.3);
}

.stp-06__btn--primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 24px rgba(225,29,72,.4);
}

@media (max-width: 600px) {
  .stp-06__outer {
    grid-template-columns: 1fr;
  }

  .stp-06__sidebar {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .stp-06__pane.active,
    .stp-06__btn--primary {
    animation: none;
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  let cur=3;
  const total=5;
  const navItems=document.querySelectorAll('.stp-06__nav-item');
  const panes=document.querySelectorAll('.stp-06__pane');
  const fill=document.getElementById('stp-06-fill');
  const pct=document.getElementById('stp-06-pct');
  const stepDisplay=document.getElementById('stp-06-step-display');
  const stepTitle=document.getElementById('stp-06-step-title');
  const stepDesc=document.getElementById('stp-06-step-desc');
  const nextBtn=document.getElementById('stp-06-next');

  const titles=['Your Account','Your Goal','Your Team','Workspace','All Done!'];
  const descs=[
    'Create your personal account to get started.',
    'What do you want to achieve with Sprout?',
    'We\'ll tailor the experience for your team size.',
    'Set up your shared workspace.',
    'Your workspace is configured and ready to go.'
  ];

  function update(){
    navItems.forEach((n,i)=>{
      n.classList.remove('done','active');
      const dot=n.querySelector('.stp-06__nav-dot');
      if(i+1<cur){n.classList.add('done');dot.textContent='✓';}
      else if(i+1===cur){n.classList.add('active');dot.textContent=cur;}
      else dot.textContent=i+1;
    });
    panes.forEach(p=>{
      p.classList.remove('active');
      if(parseInt(p.dataset.pane)===cur) p.classList.add('active');
    });
    const p=((cur-1)/(total-1)*100).toFixed(0);
    fill.style.width=p+'%';
    pct.textContent=p+'%';
    stepDisplay.textContent=`Step ${cur} of ${total}`;
    stepTitle.textContent=titles[cur-1];
    stepDesc.textContent=descs[cur-1];
    nextBtn.textContent=cur===total?'Go to Dashboard →':'Continue →';
    document.getElementById('stp-06-back').style.display=cur<=1?'none':'';
    document.getElementById('stp-06-skip').style.display=cur===total?'none':'';
  }

  document.getElementById('stp-06-next').addEventListener('click',()=>{cur=Math.min(total,cur+1);update();});
  document.getElementById('stp-06-back').addEventListener('click',()=>{cur=Math.max(1,cur-1);update();});
  document.getElementById('stp-06-skip').addEventListener('click',()=>{cur=Math.min(total,cur+1);update();});
  document.querySelectorAll('.stp-06__choice').forEach(c=>{
    c.addEventListener('click',()=>{
      const siblings=c.parentElement.querySelectorAll('.stp-06__choice');
      siblings.forEach(s=>s.classList.remove('picked'));
      c.classList.add('picked');
    });
  });
  update();
})();
```
