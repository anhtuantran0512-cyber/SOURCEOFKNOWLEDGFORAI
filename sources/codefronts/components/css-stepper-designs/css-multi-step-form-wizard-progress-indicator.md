---
source: "codefronts"
url: "https://codefronts.com/components/css-stepper-designs/css-multi-step-form-wizard-progress-indicator/"
title: "CSS Multi-Step Form Wizard Progress Indicator"
section: "components"
category: "css-stepper-designs"
category_name: "CSS Steppers"
description: "A 4-step account-creation wizard with animated node states, gradient connector lines, scoped pulse keyframe on the active step, and a checkmark success panel…"
has_js: "true"
---

Here's a working CSS Stepper from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Multi-Step Form Wizard Progress Indicator
Source: https://codefronts.com/components/css-stepper-designs/css-multi-step-form-wizard-progress-indicator/

A 4-step account-creation wizard with animated node states, gradient connector lines, scoped pulse keyframe on the active step, and a checkmark success panel — all navigated by prev/next JS.
## HTML
```html
<div class="stp-01">
  <div class="stp-01__card">
    <div class="stp-01__header">
      <div class="stp-01__title">Create Your Account</div>
      <div class="stp-01__sub">Complete all steps to get started</div>
    </div>

    <div class="stp-01__steps" id="stp-01-steps">
      <div class="stp-01__step is-done" data-step="1">
        <div class="stp-01__node">1</div>
        <span class="stp-01__node-label">Profile</span>
      </div>
      <div class="stp-01__step is-active" data-step="2">
        <div class="stp-01__node">2</div>
        <span class="stp-01__node-label">Details</span>
      </div>
      <div class="stp-01__step" data-step="3">
        <div class="stp-01__node">3</div>
        <span class="stp-01__node-label">Billing</span>
      </div>
      <div class="stp-01__step" data-step="4">
        <div class="stp-01__node">4</div>
        <span class="stp-01__node-label">Review</span>
      </div>
    </div>

    <!-- Panel 1 -->
    <div class="stp-01__panel" data-panel="1">
      <div class="stp-01__panel-title">Personal Profile</div>
      <div class="stp-01__row">
        <div class="stp-01__field"><label class="stp-01__label">First Name</label><input class="stp-01__input" placeholder="Alex" value="Alex"></div>
        <div class="stp-01__field"><label class="stp-01__label">Last Name</label><input class="stp-01__input" placeholder="Morgan" value="Morgan"></div>
      </div>
      <div class="stp-01__field"><label class="stp-01__label">Email Address</label><input class="stp-01__input" placeholder="[email protected]" value="[email protected]"></div>
    </div>

    <!-- Panel 2 -->
    <div class="stp-01__panel is-active" data-panel="2">
      <div class="stp-01__panel-title">Account Details</div>
      <div class="stp-01__field"><label class="stp-01__label">Username</label><input class="stp-01__input" placeholder="@alexmorgan"></div>
      <div class="stp-01__field"><label class="stp-01__label">Role</label><input class="stp-01__input" placeholder="Frontend Engineer"></div>
      <div class="stp-01__field"><label class="stp-01__label">Company</label><input class="stp-01__input" placeholder="Acme Corp"></div>
    </div>

    <!-- Panel 3 -->
    <div class="stp-01__panel" data-panel="3">
      <div class="stp-01__panel-title">Billing Information</div>
      <div class="stp-01__field"><label class="stp-01__label">Card Number</label><input class="stp-01__input" placeholder="4242 4242 4242 4242"></div>
      <div class="stp-01__row">
        <div class="stp-01__field"><label class="stp-01__label">Expiry</label><input class="stp-01__input" placeholder="MM / YY"></div>
        <div class="stp-01__field"><label class="stp-01__label">CVV</label><input class="stp-01__input" placeholder="•••"></div>
      </div>
    </div>

    <!-- Panel 4 -->
    <div class="stp-01__panel" data-panel="4">
      <div class="stp-01__panel-title">Review &amp; Confirm</div>
      <div class="stp-01__summary">
        <div class="stp-01__summary-item"><div class="stp-01__summary-key">Name</div><div class="stp-01__summary-val">Alex Morgan</div></div>
        <div class="stp-01__summary-item"><div class="stp-01__summary-key">Email</div><div class="stp-01__summary-val">[email protected]</div></div>
        <div class="stp-01__summary-item"><div class="stp-01__summary-key">Username</div><div class="stp-01__summary-val">@alexmorgan</div></div>
        <div class="stp-01__summary-item"><div class="stp-01__summary-key">Plan</div><div class="stp-01__summary-val">Pro · $29/mo</div></div>
      </div>
    </div>

    <!-- Success -->
    <div class="stp-01__panel" data-panel="5">
      <div class="stp-01__success">
        <div class="stp-01__success-icon">✓</div>
        <div class="stp-01__success-title">Account Created!</div>
        <div class="stp-01__success-msg">Welcome aboard. Check your email to verify your account.</div>
      </div>
    </div>

    <div class="stp-01__nav" id="stp-01-nav">
      <div class="stp-01__fraction">Step <span id="stp-01-cur">2</span> of <span>4</span></div>
      <button class="stp-01__btn stp-01__btn--back" id="stp-01-back">← Back</button>
      <button class="stp-01__btn stp-01__btn--next" id="stp-01-next">Continue →</button>
    </div>
  </div>
</div>
```
## CSS
```css
.stp-01,
.stp-01 *,
.stp-01 *::before,
.stp-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.stp-01 ::selection {
  background: #7c3aed;
  color: #fff;
}

.stp-01 {
  --bg: #0d0d1a;
  --card: #16162a;
  --border: #2a2a4a;
  --purple: #7c3aed;
  --violet: #a855f7;
  --pink: #ec4899;
  --white: #f0f0ff;
  --muted: #6b6b9a;
  --success: #10b981;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

.stp-01__card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 48px 40px;
  max-width: 640px;
  width: 100%;
  box-shadow: 0 32px 80px rgba(124,58,237,.15),0 0 0 1px rgba(124,58,237,.1);
}

.stp-01__header {
  text-align: center;
  margin-bottom: 40px;
}

.stp-01__title {
  font-size: 22px;
  font-weight: 700;
  color: var(--white);
  letter-spacing: -.02em;
}

.stp-01__sub {
  font-size: 13px;
  color: var(--muted);
  margin-top: 6px;
}
/* stepper track */

.stp-01__steps {
  display: flex;
  align-items: center;
  margin-bottom: 44px;
  position: relative;
}

.stp-01__step {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
  position: relative;
  z-index: 1;
}

.stp-01__node {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 700;
  border: 2px solid var(--border);
  background: var(--card);
  color: var(--muted);
  transition: all .4s cubic-bezier(.34,1.56,.64,1);
  position: relative;
}

.stp-01__node-label {
  font-size: 11px;
  color: var(--muted);
  margin-top: 10px;
  letter-spacing: .06em;
  text-transform: uppercase;
  text-align: center;
  transition: color .3s;
}
/* connector lines */

.stp-01__step:not(:last-child)::after {
  content: '';
  position: absolute;
  top: 22px;
  left: calc(50% + 22px);
  width: calc(100% - 44px);
  height: 2px;
  background: var(--border);
  z-index: 0;
}

.stp-01__step.is-done::after {
  background: linear-gradient(90deg,var(--purple),var(--violet));
}
/* states */

.stp-01__step.is-done .stp-01__node {
  background: linear-gradient(135deg,var(--purple),var(--violet));
  border-color: var(--violet);
  color: #fff;
  box-shadow: 0 0 20px rgba(124,58,237,.5);
}

.stp-01__step.is-done .stp-01__node::after {
  content: '✓';
  position: absolute;
  font-size: 16px;
}

.stp-01__step.is-done .stp-01__node-label {
  color: var(--violet);
}

.stp-01__step.is-active .stp-01__node {
  background: transparent;
  border-color: var(--purple);
  border-width: 2px;
  color: var(--purple);
  box-shadow: 0 0 0 6px rgba(124,58,237,.15),0 0 24px rgba(124,58,237,.3);
  animation: stp-01-pulse 2s ease-in-out infinite;
}

.stp-01__step.is-active .stp-01__node-label {
  color: var(--white);
}

@keyframes stp-01-pulse {
  0%,
    100% {
    box-shadow: 0 0 0 6px rgba(124,58,237,.15),0 0 24px rgba(124,58,237,.3);
  }

  50% {
    box-shadow: 0 0 0 10px rgba(124,58,237,.08),0 0 32px rgba(124,58,237,.4);
  }
}
/* form area */

.stp-01__panel {
  display: none;
}

.stp-01__panel.is-active {
  display: block;
}

.stp-01__panel-title {
  font-size: 18px;
  font-weight: 600;
  color: var(--white);
  margin-bottom: 20px;
}

.stp-01__field {
  margin-bottom: 16px;
}

.stp-01__label {
  font-size: 12px;
  color: var(--muted);
  letter-spacing: .06em;
  text-transform: uppercase;
  margin-bottom: 6px;
  display: block;
}

.stp-01__input {
  width: 100%;
  padding: 12px 16px;
  background: rgba(255,255,255,.04);
  border: 1px solid var(--border);
  border-radius: 10px;
  color: var(--white);
  font-size: 14px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.stp-01__input::placeholder {
  color: var(--muted);
}

.stp-01__input:focus {
  border-color: var(--purple);
  box-shadow: 0 0 0 3px rgba(124,58,237,.2);
}

.stp-01__row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}
/* summary */

.stp-01__summary {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.stp-01__summary-item {
  background: rgba(124,58,237,.08);
  border: 1px solid rgba(124,58,237,.2);
  border-radius: 10px;
  padding: 14px 16px;
}

.stp-01__summary-key {
  font-size: 11px;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: .06em;
}

.stp-01__summary-val {
  font-size: 14px;
  color: var(--white);
  font-weight: 600;
  margin-top: 4px;
}
/* navigation */

.stp-01__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 32px;
  gap: 12px;
}

.stp-01__btn {
  padding: 12px 28px;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  border: none;
  transition: all .2s;
}

.stp-01__btn--back {
  background: transparent;
  border: 1px solid var(--border);
  color: var(--muted);
}

.stp-01__btn--back:hover {
  border-color: var(--purple);
  color: var(--white);
}

.stp-01__btn--next {
  background: linear-gradient(135deg,var(--purple),var(--violet));
  color: #fff;
  box-shadow: 0 4px 20px rgba(124,58,237,.4);
  margin-left: auto;
}

.stp-01__btn--next:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 28px rgba(124,58,237,.5);
}

.stp-01__btn--submit {
  background: linear-gradient(135deg,var(--success),#34d399);
  color: #fff;
  box-shadow: 0 4px 20px rgba(16,185,129,.4);
  margin-left: auto;
}
/* success */

.stp-01__success {
  text-align: center;
  padding: 20px 0;
}

.stp-01__success-icon {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: linear-gradient(135deg,var(--success),#34d399);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
  margin: 0 auto 20px;
  box-shadow: 0 0 40px rgba(16,185,129,.4);
  animation: stp-01-pop .5s cubic-bezier(.34,1.56,.64,1);
}

@keyframes stp-01-pop {
  from {
    transform: scale(0);
    opacity: 0;
  }

  to {
    transform: scale(1);
    opacity: 1;
  }
}

.stp-01__success-title {
  font-size: 22px;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 8px;
}

.stp-01__success-msg {
  font-size: 14px;
  color: var(--muted);
}
/* progress fraction */

.stp-01__fraction {
  font-size: 12px;
  color: var(--muted);
}

.stp-01__fraction span {
  color: var(--violet);
  font-weight: 700;
}

@media (prefers-reduced-motion: reduce) {
  .stp-01__step.is-active .stp-01__node {
    animation: none;
  }

  .stp-01__success-icon {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  const steps=document.querySelectorAll('.stp-01__step');
  const panels=document.querySelectorAll('.stp-01__panel');
  const btnNext=document.getElementById('stp-01-next');
  const btnBack=document.getElementById('stp-01-back');
  const curEl=document.getElementById('stp-01-cur');
  const nav=document.getElementById('stp-01-nav');
  let cur=2;
  const total=4;

  function update(){
    steps.forEach((s,i)=>{
      s.classList.remove('is-done','is-active');
      if(i+1<cur) s.classList.add('is-done');
      else if(i+1===cur) s.classList.add('is-active');
    });
    panels.forEach((p,i)=>{
      p.classList.remove('is-active');
      if(parseInt(p.dataset.panel)===cur||(cur>total&&parseInt(p.dataset.panel)===5)) p.classList.add('is-active');
    });
    curEl.textContent=Math.min(cur,total);
    btnBack.style.display=cur<=1?'none':'';
    if(cur>total){
      nav.style.display='none';
    } else if(cur===total){
      btnNext.textContent='Submit ✓';
      btnNext.className='stp-01__btn stp-01__btn--submit';
    } else {
      btnNext.textContent='Continue →';
      btnNext.className='stp-01__btn stp-01__btn--next';
    }
  }

  btnNext.addEventListener('click',()=>{cur=Math.min(cur+1,total+1);update();});
  btnBack.addEventListener('click',()=>{cur=Math.max(cur-1,1);update();});
  update();
})();
```
