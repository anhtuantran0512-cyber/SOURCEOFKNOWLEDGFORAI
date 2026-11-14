---
source: "codefronts"
url: "https://codefronts.com/components/css-stepper-designs/css-dark-mode-stepper-component/"
title: "CSS Dark Mode Stepper Component"
section: "components"
category: "css-stepper-designs"
category_name: "CSS Steppers"
description: "A dark green/teal step component with a tab rail showing step sublabels, a mini progress bar beneath the rail, a light/dark theme toggle, and a completion…"
has_js: "true"
---

Here's a working CSS Stepper from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Dark Mode Stepper Component
Source: https://codefronts.com/components/css-stepper-designs/css-dark-mode-stepper-component/

A dark green/teal step component with a tab rail showing step sublabels, a mini progress bar beneath the rail, a light/dark theme toggle, and a completion summary panel at the final step.
## HTML
```html
<div class="stp-11">
  <div class="stp-11__eyebrow">
    <div class="stp-11__dot-live"></div>
    Dark Mode Stepper · 4 Steps
  </div>

  <div class="stp-11__card">
    <!-- Rail -->
    <div class="stp-11__rail" id="stp-11-rail">
      <div class="stp-11__rail-item done" data-r="1">
        <div class="stp-11__rail-num">✓</div>
        <div class="stp-11__rail-text"><div class="stp-11__rail-label">Account</div><div class="stp-11__rail-sublabel">Done</div></div>
      </div>
      <div class="stp-11__rail-item done" data-r="2">
        <div class="stp-11__rail-num">✓</div>
        <div class="stp-11__rail-text"><div class="stp-11__rail-label">Preferences</div><div class="stp-11__rail-sublabel">Done</div></div>
      </div>
      <div class="stp-11__rail-item active" data-r="3">
        <div class="stp-11__rail-num">3</div>
        <div class="stp-11__rail-text"><div class="stp-11__rail-label">Notifications</div><div class="stp-11__rail-sublabel">In progress</div></div>
      </div>
      <div class="stp-11__rail-item" data-r="4">
        <div class="stp-11__rail-num">4</div>
        <div class="stp-11__rail-text"><div class="stp-11__rail-label">Review</div><div class="stp-11__rail-sublabel">Next</div></div>
      </div>
    </div>

    <!-- Body -->
    <div class="stp-11__body">
      <div class="stp-11__mini-bar"><div class="stp-11__mini-fill" id="stp-11-fill" style="width:50%"></div></div>

      <div class="stp-11__pane" data-pane="1">
        <div class="stp-11__pane-head"><div class="stp-11__pane-title">Account Setup</div><div class="stp-11__pane-desc">Create your secure account credentials.</div></div>
        <div class="stp-11__field"><label class="stp-11__fl">Email</label><input class="stp-11__in" placeholder="[email protected]"></div>
        <div class="stp-11__row2">
          <div class="stp-11__field"><label class="stp-11__fl">Username</label><input class="stp-11__in" placeholder="@handle"></div>
          <div class="stp-11__field"><label class="stp-11__fl">Password</label><input class="stp-11__in" type="password" placeholder="••••••••"></div>
        </div>
      </div>

      <div class="stp-11__pane" data-pane="2">
        <div class="stp-11__pane-head"><div class="stp-11__pane-title">Preferences</div><div class="stp-11__pane-desc">Personalise your experience.</div></div>
        <div class="stp-11__field"><label class="stp-11__fl">Display Name</label><input class="stp-11__in" placeholder="Jordan Blake"></div>
        <div class="stp-11__field"><label class="stp-11__fl">Time Zone</label><input class="stp-11__in" placeholder="UTC-08:00 Pacific"></div>
        <div class="stp-11__field"><label class="stp-11__fl">Language</label><input class="stp-11__in" placeholder="English (US)"></div>
      </div>

      <div class="stp-11__pane active" data-pane="3">
        <div class="stp-11__pane-head"><div class="stp-11__pane-title">Notification Settings</div><div class="stp-11__pane-desc">Choose what you want to hear about.</div></div>
        <div class="stp-11__toggles">
          <div class="stp-11__toggle">
            <div class="stp-11__toggle-info"><div class="stp-11__toggle-name">Email Digest</div><div class="stp-11__toggle-desc">Weekly summary of your activity</div></div>
            <div class="stp-11__sw on" tabindex="0" role="switch"></div>
          </div>
          <div class="stp-11__toggle">
            <div class="stp-11__toggle-info"><div class="stp-11__toggle-name">Push Alerts</div><div class="stp-11__toggle-desc">Real-time browser notifications</div></div>
            <div class="stp-11__sw" tabindex="0" role="switch"></div>
          </div>
          <div class="stp-11__toggle">
            <div class="stp-11__toggle-info"><div class="stp-11__toggle-name">Product Updates</div><div class="stp-11__toggle-desc">New features and changelog</div></div>
            <div class="stp-11__sw on" tabindex="0" role="switch"></div>
          </div>
        </div>
      </div>

      <div class="stp-11__pane" data-pane="4">
        <div class="stp-11__pane-head"><div class="stp-11__pane-title">Review &amp; Confirm</div><div class="stp-11__pane-desc">Everything looks right?</div></div>
        <div class="stp-11__review">
          <div class="stp-11__review-row"><span class="stp-11__review-key">Username</span><span class="stp-11__review-val">@jordanblake</span></div>
          <div class="stp-11__review-row"><span class="stp-11__review-key">Email</span><span class="stp-11__review-val">[email protected]</span></div>
          <div class="stp-11__review-row"><span class="stp-11__review-key">Time Zone</span><span class="stp-11__review-val">UTC-08:00 Pacific</span></div>
          <div class="stp-11__review-row"><span class="stp-11__review-key">Email Digest</span><span class="stp-11__review-val" style="color:var(--green)">✓ Enabled</span></div>
          <div class="stp-11__review-row"><span class="stp-11__review-key">Push Alerts</span><span class="stp-11__review-val" style="color:var(--muted)">Disabled</span></div>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="stp-11__foot">
      <span class="stp-11__step-text">Step <strong id="stp-11-cur">3</strong> of <strong>4</strong></span>
      <div class="stp-11__foot-btns">
        <button class="stp-11__btn stp-11__btn--ghost" id="stp-11-back">Back</button>
        <button class="stp-11__btn stp-11__btn--primary" id="stp-11-next">Continue →</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.stp-11,
.stp-11 *,
.stp-11 *::before,
.stp-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.stp-11 ::selection {
  background: #34d399;
  color: #000;
}

.stp-11 {
  --bg: #0f0f0f;
  --surface: #181818;
  --elevated: #222;
  --green: #34d399;
  --teal: #2dd4bf;
  --white: #f5f5f5;
  --muted: #525252;
  --border: #2a2a2a;
  --text: #e5e5e5;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 32px;
}
/* ─ Top label ─ */

.stp-11__eyebrow {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 500;
}

.stp-11__dot-live {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--green);
  animation: stp-11-blink 1.5s ease-in-out infinite;
}

@keyframes stp-11-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .3;
  }
}
/* ─ Main card ─ */

.stp-11__card {
  max-width: 620px;
  width: 100%;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  overflow: hidden;
}
/* ─ Step rail ─ */

.stp-11__rail {
  display: flex;
  border-bottom: 1px solid var(--border);
  background: var(--bg);
}

.stp-11__rail-item {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 16px;
  position: relative;
  border-right: 1px solid var(--border);
  cursor: pointer;
  transition: background .2s;
}

.stp-11__rail-item:last-child {
  border-right: none;
}

.stp-11__rail-item:hover {
  background: rgba(255,255,255,.02);
}

.stp-11__rail-item.active {
  background: rgba(52,211,153,.04);
}

.stp-11__rail-item.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg,var(--green),var(--teal));
}

.stp-11__rail-num {
  width: 28px;
  height: 28px;
  border-radius: 8px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 700;
  background: var(--border);
  color: var(--muted);
  transition: all .3s;
}

.stp-11__rail-item.done .stp-11__rail-num {
  background: rgba(52,211,153,.15);
  color: var(--green);
}

.stp-11__rail-item.active .stp-11__rail-num {
  background: rgba(52,211,153,.2);
  color: var(--green);
  box-shadow: 0 0 12px rgba(52,211,153,.2);
}

.stp-11__rail-text {
  min-width: 0;
}

.stp-11__rail-label {
  font-size: 12px;
  font-weight: 600;
  color: var(--muted);
  white-space: nowrap;
  transition: color .3s;
}

.stp-11__rail-item.done .stp-11__rail-label {
  color: var(--green);
}

.stp-11__rail-item.active .stp-11__rail-label {
  color: var(--text);
}

.stp-11__rail-sublabel {
  font-size: 10px;
  color: var(--muted);
  display: none;
}

.stp-11__rail-item.active .stp-11__rail-sublabel {
  display: block;
}
/* ─ Body ─ */

.stp-11__body {
  padding: 28px 28px 24px;
}
/* progress micro bar */

.stp-11__mini-bar {
  height: 3px;
  background: var(--border);
  border-radius: 2px;
  margin-bottom: 24px;
  overflow: hidden;
}

.stp-11__mini-fill {
  height: 100%;
  border-radius: 2px;
  background: linear-gradient(90deg,var(--green),var(--teal));
  transition: width .4s ease;
}

.stp-11__pane {
  display: none;
}

.stp-11__pane.active {
  display: block;
  animation: stp-11-in .3s ease;
}

@keyframes stp-11-in {
  from {
    opacity: 0;
    transform: translateX(8px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.stp-11__pane-head {
  margin-bottom: 20px;
}

.stp-11__pane-title {
  font-size: 17px;
  font-weight: 700;
  color: var(--white);
}

.stp-11__pane-desc {
  font-size: 13px;
  color: var(--muted);
  margin-top: 4px;
}
/* fields */

.stp-11__field {
  margin-bottom: 14px;
}

.stp-11__fl {
  font-size: 11px;
  font-weight: 500;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: .06em;
  margin-bottom: 5px;
  display: block;
}

.stp-11__in {
  width: 100%;
  padding: 10px 14px;
  background: var(--elevated);
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--white);
  font-size: 14px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.stp-11__in::placeholder {
  color: var(--muted);
}

.stp-11__in:focus {
  border-color: var(--green);
  box-shadow: 0 0 0 2px rgba(52,211,153,.1);
}

.stp-11__row2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}
/* toggle switches */

.stp-11__toggles {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.stp-11__toggle {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 16px;
  background: var(--elevated);
  border: 1px solid var(--border);
  border-radius: 10px;
}

.stp-11__toggle-info {
  flex: 1;
}

.stp-11__toggle-name {
  font-size: 14px;
  font-weight: 600;
  color: var(--text);
}

.stp-11__toggle-desc {
  font-size: 12px;
  color: var(--muted);
  margin-top: 2px;
}

.stp-11__sw {
  width: 40px;
  height: 22px;
  border-radius: 11px;
  background: var(--border);
  position: relative;
  cursor: pointer;
  transition: background .25s;
  flex-shrink: 0;
}

.stp-11__sw.on {
  background: var(--green);
}

.stp-11__sw::after {
  content: '';
  position: absolute;
  top: 3px;
  left: 3px;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: #fff;
  transition: transform .25s;
  box-shadow: 0 1px 4px rgba(0,0,0,.3);
}

.stp-11__sw.on::after {
  transform: translateX(18px);
}
/* review table */

.stp-11__review {
  display: grid;
  gap: 10px;
}

.stp-11__review-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 14px;
  background: var(--elevated);
  border-radius: 8px;
  border: 1px solid var(--border);
}

.stp-11__review-key {
  font-size: 12px;
  color: var(--muted);
  font-weight: 500;
}

.stp-11__review-val {
  font-size: 13px;
  color: var(--white);
  font-weight: 600;
}
/* footer nav */

.stp-11__foot {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 28px;
  border-top: 1px solid var(--border);
  background: var(--bg);
}

.stp-11__step-text {
  font-size: 12px;
  color: var(--muted);
}

.stp-11__step-text strong {
  color: var(--green);
}

.stp-11__foot-btns {
  display: flex;
  gap: 10px;
}

.stp-11__btn {
  padding: 9px 22px;
  border-radius: 8px;
  border: none;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all .2s;
}

.stp-11__btn--ghost {
  background: var(--border);
  color: var(--muted);
}

.stp-11__btn--ghost:hover {
  color: var(--white);
}

.stp-11__btn--primary {
  background: linear-gradient(135deg,var(--green),var(--teal));
  color: #000;
}

.stp-11__btn--primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(52,211,153,.25);
}

@media (prefers-reduced-motion: reduce) {
  .stp-11__dot-live {
    animation: none;
  }

  .stp-11__pane.active {
    animation: none;
  }

  .stp-11__mini-fill {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  let cur=3;
  const total=4;
  const rails=document.querySelectorAll('.stp-11__rail-item');
  const panes=document.querySelectorAll('.stp-11__pane');
  const fill=document.getElementById('stp-11-fill');
  const curEl=document.getElementById('stp-11-cur');
  const nextBtn=document.getElementById('stp-11-next');
  const sublabels=['Done','Done','In progress','Next'];

  function update(){
    rails.forEach((r,i)=>{
      r.classList.remove('done','active');
      const num=r.querySelector('.stp-11__rail-num');
      const sub=r.querySelector('.stp-11__rail-sublabel');
      if(i+1<cur){r.classList.add('done');num.textContent='✓';if(sub)sub.textContent='Done';}
      else if(i+1===cur){r.classList.add('active');num.textContent=cur;if(sub)sub.textContent='In progress';}
      else{num.textContent=i+1;if(sub)sub.textContent=i+1===cur+1?'Next':''}
    });
    panes.forEach(p=>{
      p.classList.remove('active');
      if(parseInt(p.dataset.pane)===cur) p.classList.add('active');
    });
    fill.style.width=((cur-1)/(total-1)*100)+'%';
    curEl.textContent=cur;
    nextBtn.textContent=cur===total?'Confirm & Finish ✓':'Continue →';
    document.getElementById('stp-11-back').style.display=cur<=1?'none':'';
  }

  document.querySelectorAll('.stp-11__sw').forEach(sw=>{
    sw.addEventListener('click',()=>sw.classList.toggle('on'));
  });
  document.getElementById('stp-11-back').addEventListener('click',()=>{cur=Math.max(1,cur-1);update();});
  document.getElementById('stp-11-next').addEventListener('click',()=>{cur=Math.min(total,cur+1);update();});
  update();
})();
```
