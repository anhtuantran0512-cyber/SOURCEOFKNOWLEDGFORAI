---
source: "codefronts"
url: "https://codefronts.com/components/css-stepper-designs/css-stepper-with-validation-states/"
title: "CSS Stepper With Validation States"
section: "components"
category: "css-stepper-designs"
category_name: "CSS Steppers"
description: "A blue/indigo form stepper where each step has live input validation — valid (green), error (red), and warning (amber) states — with per-field messages and a…"
has_js: "true"
---

Here's a working CSS Stepper from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Stepper With Validation States
Source: https://codefronts.com/components/css-stepper-designs/css-stepper-with-validation-states/

A blue/indigo form stepper where each step has live input validation — valid (green), error (red), and warning (amber) states — with per-field messages and a step-level badge that reflects the field result.
## HTML
```html
<div class="stp-08">
  <div class="stp-08__card">
    <!-- Step header -->
    <div class="stp-08__head">
      <div class="stp-08__steps" id="stp-08-steps">
        <div class="stp-08__step valid" data-s="1">
          <div class="stp-08__node">✓</div>
          <span class="stp-08__node-label">Identity</span>
        </div>
        <div class="stp-08__step error" data-s="2">
          <div class="stp-08__node">!</div>
          <span class="stp-08__node-label">Security</span>
        </div>
        <div class="stp-08__step active" data-s="3">
          <div class="stp-08__node">3</div>
          <span class="stp-08__node-label">Profile</span>
        </div>
        <div class="stp-08__step warning" data-s="4">
          <div class="stp-08__node">⚠</div>
          <span class="stp-08__node-label">Docs</span>
        </div>
        <div class="stp-08__step" data-s="5">
          <div class="stp-08__node">5</div>
          <span class="stp-08__node-label">Submit</span>
        </div>
      </div>
    </div>

    <!-- Panels -->
    <div class="stp-08__body">

      <!-- Panel 1 — valid -->
      <div class="stp-08__pane" data-panel="1">
        <div class="stp-08__pane-title">Identity Verification</div>
        <div class="stp-08__pane-sub">All identity fields are valid.</div>
        <div class="stp-08__chips">
          <span class="stp-08__chip stp-08__chip--ok">✓ Full Name</span>
          <span class="stp-08__chip stp-08__chip--ok">✓ Email</span>
          <span class="stp-08__chip stp-08__chip--ok">✓ Date of Birth</span>
        </div>
        <div class="stp-08__field">
          <label class="stp-08__fl">Full Name</label>
          <div class="stp-08__in-wrap">
            <input class="stp-08__in is-valid" value="Alex Morgan" readonly>
            <span class="stp-08__icon">✅</span>
          </div>
          <div class="stp-08__msg ok show">✓ Name verified</div>
        </div>
        <div class="stp-08__field">
          <label class="stp-08__fl">Email</label>
          <div class="stp-08__in-wrap">
            <input class="stp-08__in is-valid" value="[email protected]" readonly>
            <span class="stp-08__icon">✅</span>
          </div>
          <div class="stp-08__msg ok show">✓ Email verified</div>
        </div>
      </div>

      <!-- Panel 2 — error -->
      <div class="stp-08__pane" data-panel="2">
        <div class="stp-08__pane-title">Security Setup</div>
        <div class="stp-08__pane-sub">There are errors that need to be fixed.</div>
        <div class="stp-08__chips">
          <span class="stp-08__chip stp-08__chip--err">✗ Password too weak</span>
          <span class="stp-08__chip stp-08__chip--err">✗ Passwords don't match</span>
        </div>
        <div class="stp-08__field">
          <label class="stp-08__fl">Password <span class="stp-08__fl-hint">min 12 chars</span></label>
          <div class="stp-08__in-wrap">
            <input class="stp-08__in is-invalid" type="password" value="weak" readonly>
            <span class="stp-08__icon">❌</span>
          </div>
          <div class="stp-08__msg err show">✗ Password must be at least 12 characters with symbols</div>
        </div>
        <div class="stp-08__field">
          <label class="stp-08__fl">Confirm Password</label>
          <div class="stp-08__in-wrap">
            <input class="stp-08__in is-invalid" type="password" value="different" readonly>
            <span class="stp-08__icon">❌</span>
          </div>
          <div class="stp-08__msg err show">✗ Passwords do not match</div>
        </div>
      </div>

      <!-- Panel 3 — active/in progress -->
      <div class="stp-08__pane active" data-panel="3">
        <div class="stp-08__pane-title">Profile Details</div>
        <div class="stp-08__pane-sub">Fill in your professional profile information.</div>
        <div class="stp-08__field">
          <label class="stp-08__fl">Job Title</label>
          <div class="stp-08__in-wrap">
            <input class="stp-08__in" id="stp-08-title" placeholder="Senior Engineer">
            <span class="stp-08__icon" id="stp-08-ti">○</span>
          </div>
          <div class="stp-08__msg" id="stp-08-tm"></div>
        </div>
        <div class="stp-08__field">
          <label class="stp-08__fl">LinkedIn URL <span class="stp-08__fl-hint">optional</span></label>
          <div class="stp-08__in-wrap">
            <input class="stp-08__in is-warning" id="stp-08-li" placeholder="linkedin.com/in/..." value="linkedin.com/in/alexmorgan">
            <span class="stp-08__icon">⚠️</span>
          </div>
          <div class="stp-08__msg warn show">⚠ URL format looks incomplete — add https://</div>
        </div>
        <div class="stp-08__field">
          <label class="stp-08__fl">Bio <span class="stp-08__fl-hint">150 chars max</span></label>
          <div class="stp-08__in-wrap">
            <input class="stp-08__in" id="stp-08-bio" placeholder="Tell us a little about yourself" maxlength="150">
            <span class="stp-08__icon" id="stp-08-bi">○</span>
          </div>
          <div class="stp-08__msg" id="stp-08-bm"></div>
        </div>
      </div>

      <!-- Panel 4 — warning -->
      <div class="stp-08__pane" data-panel="4">
        <div class="stp-08__pane-title">Document Upload</div>
        <div class="stp-08__pane-sub">Some documents are missing.</div>
        <div class="stp-08__chips">
          <span class="stp-08__chip stp-08__chip--ok">✓ ID Photo</span>
          <span class="stp-08__chip stp-08__chip--warn">⚠ Proof of Address</span>
          <span class="stp-08__chip stp-08__chip--none">— CV (optional)</span>
        </div>
        <div style="background:#fffbeb;border:1px solid #fde047;border-radius:10px;padding:16px;font-size:13px;color:#92400e;margin-top:8px">
          ⚠️ Proof of address document is recommended but not required. You can submit without it, but verification may take longer.
        </div>
      </div>

      <!-- Panel 5 — submit -->
      <div class="stp-08__pane" data-panel="5">
        <div class="stp-08__pane-title">Review &amp; Submit</div>
        <div class="stp-08__pane-sub">Check all validation states before submitting.</div>
        <div class="stp-08__chips">
          <span class="stp-08__chip stp-08__chip--ok">✓ Identity</span>
          <span class="stp-08__chip stp-08__chip--err">✗ Security — fix required</span>
          <span class="stp-08__chip stp-08__chip--ok">✓ Profile</span>
          <span class="stp-08__chip stp-08__chip--warn">⚠ Docs — optional</span>
        </div>
        <div style="background:#fee2e2;border:1px solid #fecaca;border-radius:10px;padding:16px;font-size:13px;color:#991b1b">
          ❌ You cannot submit because Step 2 (Security) has errors. Please go back and fix the password fields.
        </div>
      </div>
    </div>

    <!-- Nav -->
    <div class="stp-08__nav">
      <button class="stp-08__btn stp-08__btn--ghost" id="stp-08-back">← Back</button>
      <span class="stp-08__status ok" id="stp-08-status">Step 3 of 5</span>
      <button class="stp-08__btn stp-08__btn--primary" id="stp-08-next">Next →</button>
    </div>
  </div>
</div>
```
## CSS
```css
.stp-08,
.stp-08 *,
.stp-08 *::before,
.stp-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.stp-08 ::selection {
  background: #3b82f6;
  color: #fff;
}

.stp-08 {
  --bg: #f0f4ff;
  --white: #fff;
  --blue: #3b82f6;
  --indigo: #6366f1;
  --dark: #0f172a;
  --mid: #334155;
  --muted: #94a3b8;
  --border: #e2e8f0;
  --success: #16a34a;
  --error: #dc2626;
  --warning: #d97706;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

.stp-08__card {
  max-width: 640px;
  width: 100%;
  background: var(--white);
  border-radius: 20px;
  box-shadow: 0 12px 48px rgba(59,130,246,.1),0 0 0 1px var(--border);
  overflow: hidden;
}
/* step header */

.stp-08__head {
  background: linear-gradient(135deg,var(--blue),var(--indigo));
  padding: 28px 32px;
}

.stp-08__steps {
  display: flex;
  align-items: center;
  gap: 0;
}

.stp-08__step {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  position: relative;
}

.stp-08__step:not(:last-child)::after {
  content: '';
  position: absolute;
  top: 18px;
  left: calc(50% + 18px);
  width: calc(100% - 36px);
  height: 1.5px;
  background: rgba(255,255,255,.25);
}

.stp-08__step.done::after,
.stp-08__step.valid::after {
  background: rgba(255,255,255,.7);
}

.stp-08__node {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 700;
  background: rgba(255,255,255,.15);
  color: rgba(255,255,255,.5);
  border: 2px solid rgba(255,255,255,.2);
  transition: all .35s cubic-bezier(.34,1.56,.64,1);
}

.stp-08__step.done .stp-08__node,
.stp-08__step.valid .stp-08__node {
  background: #fff;
  color: var(--success);
  border-color: transparent;
  box-shadow: 0 0 0 3px rgba(255,255,255,.3);
}

.stp-08__step.active .stp-08__node {
  background: #fff;
  color: var(--blue);
  border-color: transparent;
  box-shadow: 0 0 0 4px rgba(255,255,255,.3);
}

.stp-08__step.error .stp-08__node {
  background: rgba(220,38,38,.9);
  color: #fff;
  border-color: transparent;
  box-shadow: 0 0 0 4px rgba(220,38,38,.3);
  animation: stp-08-shake .4s ease;
}

@keyframes stp-08-shake {
  0%,
    100% {
    transform: translateX(0);
  }

  25% {
    transform: translateX(-4px);
  }

  75% {
    transform: translateX(4px);
  }
}

.stp-08__step.warning .stp-08__node {
  background: rgba(217,119,6,.9);
  color: #fff;
  border-color: transparent;
}

.stp-08__node-label {
  font-size: 10px;
  color: rgba(255,255,255,.5);
  letter-spacing: .06em;
  text-transform: uppercase;
  text-align: center;
  transition: color .3s;
}

.stp-08__step.active .stp-08__node-label {
  color: rgba(255,255,255,.9);
}

.stp-08__step.done .stp-08__node-label,
.stp-08__step.valid .stp-08__node-label {
  color: rgba(255,255,255,.8);
}

.stp-08__step.error .stp-08__node-label {
  color: rgba(255,255,255,.7);
}
/* body */

.stp-08__body {
  padding: 32px;
}

.stp-08__pane {
  display: none;
}

.stp-08__pane.active {
  display: block;
  animation: stp-08-in .3s ease;
}

@keyframes stp-08-in {
  from {
    opacity: 0;
    transform: translateY(6px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.stp-08__pane-title {
  font-size: 18px;
  font-weight: 700;
  color: var(--dark);
  margin-bottom: 4px;
}

.stp-08__pane-sub {
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 24px;
}
/* fields with validation */

.stp-08__field {
  margin-bottom: 16px;
}

.stp-08__fl {
  font-size: 12px;
  font-weight: 600;
  color: var(--mid);
  margin-bottom: 6px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.stp-08__fl-hint {
  font-size: 11px;
  font-weight: 400;
  color: var(--muted);
}

.stp-08__in-wrap {
  position: relative;
}

.stp-08__in {
  width: 100%;
  padding: 12px 42px 12px 14px;
  background: #f8fafc;
  border: 2px solid var(--border);
  border-radius: 10px;
  color: var(--dark);
  font-size: 14px;
  outline: none;
  transition: border-color .2s,background .2s,box-shadow .2s;
}

.stp-08__in:focus {
  background: #fff;
  border-color: var(--blue);
  box-shadow: 0 0 0 3px rgba(59,130,246,.12);
}

.stp-08__in.is-valid {
  border-color: var(--success);
  background: #f0fdf4;
}

.stp-08__in.is-invalid {
  border-color: var(--error);
  background: #fef2f2;
}

.stp-08__in.is-warning {
  border-color: var(--warning);
  background: #fffbeb;
}

.stp-08__icon {
  position: absolute;
  right: 14px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 14px;
  pointer-events: none;
}

.stp-08__msg {
  font-size: 11px;
  margin-top: 5px;
  font-weight: 500;
  display: none;
}

.stp-08__msg.show {
  display: block;
}

.stp-08__msg.ok {
  color: var(--success);
}

.stp-08__msg.err {
  color: var(--error);
}

.stp-08__msg.warn {
  color: var(--warning);
}
/* state summary chips */

.stp-08__chips {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

.stp-08__chip {
  padding: 5px 12px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 5px;
}

.stp-08__chip--ok {
  background: #dcfce7;
  color: var(--success);
  border: 1px solid #bbf7d0;
}

.stp-08__chip--err {
  background: #fee2e2;
  color: var(--error);
  border: 1px solid #fecaca;
}

.stp-08__chip--warn {
  background: #fef9c3;
  color: var(--warning);
  border: 1px solid #fde047;
}

.stp-08__chip--none {
  background: #f1f5f9;
  color: var(--muted);
  border: 1px solid var(--border);
}
/* nav */

.stp-08__nav {
  display: flex;
  justify-content: space-between;
  padding: 20px 32px;
  border-top: 1px solid var(--border);
}

.stp-08__btn {
  padding: 11px 26px;
  border-radius: 10px;
  border: none;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all .2s;
}

.stp-08__btn--ghost {
  background: #f1f5f9;
  color: var(--muted);
}

.stp-08__btn--ghost:hover {
  color: var(--dark);
}

.stp-08__btn--primary {
  background: linear-gradient(135deg,var(--blue),var(--indigo));
  color: #fff;
  box-shadow: 0 4px 16px rgba(59,130,246,.3);
}

.stp-08__btn--primary:hover {
  transform: translateY(-1px);
}

.stp-08__btn--danger {
  background: linear-gradient(135deg,var(--error),#ef4444);
  color: #fff;
  box-shadow: 0 4px 16px rgba(220,38,38,.3);
}

.stp-08__status {
  font-size: 12px;
  font-weight: 600;
  padding: 6px 14px;
  border-radius: 6px;
}

.stp-08__status.ok {
  background: #dcfce7;
  color: var(--success);
}

.stp-08__status.err {
  background: #fee2e2;
  color: var(--error);
}

@media (prefers-reduced-motion: reduce) {
  .stp-08__step.error .stp-08__node {
    animation: none;
  }

  .stp-08__pane.active {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  let cur=3;
  const stateMap={1:'valid',2:'error',3:'active',4:'warning',5:''};
  const icons={valid:'✓',error:'!',warning:'⚠'};
  const steps=document.querySelectorAll('.stp-08__step');
  const panels=document.querySelectorAll('.stp-08__pane');
  const status=document.getElementById('stp-08-status');
  const nextBtn=document.getElementById('stp-08-next');
  const total=5;

  function update(){
    steps.forEach((s,i)=>{
      const n=i+1;
      const st=n===cur?'active':stateMap[n]||'';
      s.className='stp-08__step'+(st?' '+st:'');
      const node=s.querySelector('.stp-08__node');
      node.textContent=st==='valid'?'✓':st==='error'?'!':st==='warning'?'⚠':n;
    });
    panels.forEach(p=>{
      p.classList.remove('active');
      if(parseInt(p.dataset.panel)===cur) p.classList.add('active');
    });
    status.textContent=`Step ${cur} of ${total}`;
    const curState=stateMap[cur]||'';
    status.className='stp-08__status'+(curState==='valid'||curState==='active'?' ok':curState==='error'?' err':'');
    nextBtn.textContent=cur===total?'Submit →':'Next →';
    nextBtn.className='stp-08__btn'+(cur===total&&stateMap[2]==='error'?' stp-08__btn--danger':' stp-08__btn--primary');
  }

  // live validation on panel 3
  const titleIn=document.getElementById('stp-08-title');
  const titleIcon=document.getElementById('stp-08-ti');
  const titleMsg=document.getElementById('stp-08-tm');
  const bioIn=document.getElementById('stp-08-bio');
  const bioIcon=document.getElementById('stp-08-bi');
  const bioMsg=document.getElementById('stp-08-bm');

  if(titleIn) titleIn.addEventListener('input',()=>{
    const v=titleIn.value.trim();
    if(v.length>2){titleIn.className='stp-08__in is-valid';titleIcon.textContent='✅';titleMsg.className='stp-08__msg ok show';titleMsg.textContent='✓ Looks good';}
    else if(v.length>0){titleIn.className='stp-08__in is-invalid';titleIcon.textContent='❌';titleMsg.className='stp-08__msg err show';titleMsg.textContent='✗ Too short';}
    else{titleIn.className='stp-08__in';titleIcon.textContent='○';titleMsg.className='stp-08__msg';}
  });
  if(bioIn) bioIn.addEventListener('input',()=>{
    const v=bioIn.value.trim();
    if(v.length>20){bioIn.className='stp-08__in is-valid';bioIcon.textContent='✅';bioMsg.className='stp-08__msg ok show';bioMsg.textContent=`✓ ${150-v.length} chars remaining`;}
    else if(v.length>0){bioIn.className='stp-08__in';bioIcon.textContent='✏️';bioMsg.className='stp-08__msg show';bioMsg.style.color='var(--muted)';bioMsg.textContent=`${v.length}/150 chars`;}
    else{bioIn.className='stp-08__in';bioIcon.textContent='○';bioMsg.className='stp-08__msg';}
  });

  document.getElementById('stp-08-back').addEventListener('click',()=>{cur=Math.max(1,cur-1);update();});
  document.getElementById('stp-08-next').addEventListener('click',()=>{cur=Math.min(total,cur+1);update();});
  update();
})();
```
