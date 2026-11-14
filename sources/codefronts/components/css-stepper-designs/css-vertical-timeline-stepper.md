---
source: "codefronts"
url: "https://codefronts.com/components/css-stepper-designs/css-vertical-timeline-stepper/"
title: "CSS Vertical Timeline Stepper"
section: "components"
category: "css-stepper-designs"
category_name: "CSS Steppers"
description: "A vertical spine stepper where each step expands into a full content card when active, with fuchsia accent connectors, slide-in panel transitions, and a…"
has_js: "true"
---

Here's a working CSS Stepper from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Vertical Timeline Stepper
Source: https://codefronts.com/components/css-stepper-designs/css-vertical-timeline-stepper/

A vertical spine stepper where each step expands into a full content card when active, with fuchsia accent connectors, slide-in panel transitions, and a running progress bar on the left rail.
## HTML
```html
<div class="stp-04">
  <div class="stp-04__wrap">
    <div class="stp-04__header">
      <div class="stp-04__eyebrow">Application Process</div>
      <div class="stp-04__title">Complete Your Application</div>
      <div class="stp-04__sub">Follow each step to submit your application in minutes</div>
    </div>

    <div class="stp-04__timeline" id="stp-04-timeline">

      <div class="stp-04__entry is-done" data-step="1">
        <div class="stp-04__spine">
          <div class="stp-04__node">✓</div>
          <div class="stp-04__line"></div>
        </div>
        <div class="stp-04__content">
          <span class="stp-04__step-tag">Step 1</span>
          <div class="stp-04__step-name">Personal Information</div>
          <div class="stp-04__step-desc">Basic details about you — name, email, date of birth.</div>
          <span class="stp-04__done-badge">✓ Completed</span>
        </div>
      </div>

      <div class="stp-04__entry is-done" data-step="2">
        <div class="stp-04__spine">
          <div class="stp-04__node">✓</div>
          <div class="stp-04__line"></div>
        </div>
        <div class="stp-04__content">
          <span class="stp-04__step-tag">Step 2</span>
          <div class="stp-04__step-name">Address & Location</div>
          <div class="stp-04__step-desc">Your current residence and contact address.</div>
          <span class="stp-04__done-badge">✓ Completed</span>
        </div>
      </div>

      <div class="stp-04__entry is-active" data-step="3">
        <div class="stp-04__spine">
          <div class="stp-04__node">3</div>
          <div class="stp-04__line"></div>
        </div>
        <div class="stp-04__content">
          <span class="stp-04__step-tag">Step 3 · In Progress</span>
          <div class="stp-04__step-name">Employment History</div>
          <div class="stp-04__step-desc">Tell us about your last two positions.</div>
          <div class="stp-04__card">
            <div class="stp-04__field">
              <label class="stp-04__fl">Current Job Title</label>
              <input class="stp-04__in" placeholder="Senior Product Designer">
            </div>
            <div class="stp-04__field">
              <label class="stp-04__fl">Company Name</label>
              <input class="stp-04__in" placeholder="Acme Corp">
            </div>
            <div class="stp-04__field">
              <label class="stp-04__fl">Years of Experience</label>
              <input class="stp-04__in" placeholder="5">
            </div>
            <div class="stp-04__cta">
              <button class="stp-04__btn stp-04__btn--ghost" id="stp-04-back">← Back</button>
              <button class="stp-04__btn stp-04__btn--primary" id="stp-04-next">Save &amp; Continue →</button>
            </div>
          </div>
        </div>
      </div>

      <div class="stp-04__entry" data-step="4">
        <div class="stp-04__spine">
          <div class="stp-04__node">4</div>
          <div class="stp-04__line"></div>
        </div>
        <div class="stp-04__content">
          <span class="stp-04__step-tag">Step 4</span>
          <div class="stp-04__step-name">Documents Upload</div>
          <div class="stp-04__step-desc">Upload your CV, cover letter, and ID documents.</div>
          <div class="stp-04__card">
            <div style="text-align:center;padding:16px;border:2px dashed var(--border);border-radius:10px;color:var(--muted);font-size:13px">
              📎 Drag &amp; drop files or <span style="color:var(--fuchsia);cursor:pointer">browse</span>
            </div>
            <div class="stp-04__cta" style="margin-top:12px">
              <button class="stp-04__btn stp-04__btn--ghost" id="stp-04-back2">← Back</button>
              <button class="stp-04__btn stp-04__btn--primary" id="stp-04-next2">Submit →</button>
            </div>
          </div>
        </div>
      </div>

      <div class="stp-04__entry" data-step="5">
        <div class="stp-04__spine">
          <div class="stp-04__node">5</div>
          <div class="stp-04__line"></div>
        </div>
        <div class="stp-04__content">
          <span class="stp-04__step-tag">Step 5</span>
          <div class="stp-04__step-name">Review &amp; Submit</div>
          <div class="stp-04__step-desc">Final check before we process your application.</div>
          <div class="stp-04__card">
            <div style="font-size:13px;color:var(--mid);margin-bottom:12px">Everything looks great! Click submit when ready.</div>
            <div class="stp-04__cta">
              <button class="stp-04__btn stp-04__btn--ghost" id="stp-04-back3">← Back</button>
              <button class="stp-04__btn stp-04__btn--primary" id="stp-04-submit">Submit Application ✓</button>
            </div>
          </div>
        </div>
      </div>

    </div>

    <div class="stp-04__complete" id="stp-04-complete">
      <div class="stp-04__complete-icon">🎉</div>
      <div class="stp-04__complete-title">Application Submitted!</div>
      <div class="stp-04__complete-msg">We'll review your application and get back to you within 3 business days.</div>
    </div>
  </div>
</div>
```
## CSS
```css
.stp-04,
.stp-04 *,
.stp-04 *::before,
.stp-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.stp-04 ::selection {
  background: #d946ef;
  color: #fff;
}

.stp-04 {
  --bg: #faf5ff;
  --card: #fff;
  --purple: #9333ea;
  --fuchsia: #d946ef;
  --dark: #1e0a2e;
  --mid: #6b21a8;
  --muted: #a78bca;
  --border: #e9d5ff;
  --done: #7c3aed;
  --success: #16a34a;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 60px 20px;
  background-image: radial-gradient(circle at 70% 20%,rgba(217,70,239,.06),transparent 40%);
}

.stp-04__wrap {
  max-width: 600px;
  width: 100%;
}

.stp-04__header {
  margin-bottom: 40px;
}

.stp-04__eyebrow {
  font-size: 11px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--fuchsia);
  font-weight: 700;
  margin-bottom: 8px;
}

.stp-04__title {
  font-size: 28px;
  font-weight: 800;
  color: var(--dark);
  letter-spacing: -.03em;
  line-height: 1.2;
}

.stp-04__sub {
  font-size: 14px;
  color: var(--muted);
  margin-top: 6px;
}
/* vertical stepper */

.stp-04__timeline {
  position: relative;
  padding-left: 0;
}

.stp-04__entry {
  display: flex;
  gap: 0;
  position: relative;
  margin-bottom: 0;
}
/* left spine */

.stp-04__spine {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 56px;
  flex-shrink: 0;
}

.stp-04__node {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 700;
  background: var(--border);
  color: var(--muted);
  transition: all .4s cubic-bezier(.34,1.56,.64,1);
  border: 2px solid var(--border);
  flex-shrink: 0;
  position: relative;
  z-index: 1;
}

.stp-04__line {
  width: 2px;
  flex: 1;
  min-height: 32px;
  background: var(--border);
  transition: background .4s;
  margin: 4px 0;
}

.stp-04__entry:last-child .stp-04__line {
  display: none;
}
/* states */

.stp-04__entry.is-done .stp-04__node {
  background: linear-gradient(135deg,var(--purple),var(--fuchsia));
  border-color: var(--fuchsia);
  color: #fff;
  box-shadow: 0 0 0 4px rgba(217,70,239,.15),0 4px 16px rgba(147,51,234,.3);
}

.stp-04__entry.is-done .stp-04__line {
  background: linear-gradient(180deg,var(--fuchsia),var(--purple));
}

.stp-04__entry.is-active .stp-04__node {
  background: #fff;
  border-color: var(--fuchsia);
  border-width: 2px;
  color: var(--fuchsia);
  box-shadow: 0 0 0 6px rgba(217,70,239,.12),0 4px 20px rgba(217,70,239,.3);
  animation: stp-04-glow 2s ease-in-out infinite;
}

.stp-04__entry.is-active .stp-04__line {
  background: linear-gradient(180deg,var(--muted),var(--border));
}

@keyframes stp-04-glow {
  0%,
    100% {
    box-shadow: 0 0 0 6px rgba(217,70,239,.12),0 4px 20px rgba(217,70,239,.3);
  }

  50% {
    box-shadow: 0 0 0 10px rgba(217,70,239,.06),0 4px 28px rgba(217,70,239,.45);
  }
}
/* right content */

.stp-04__content {
  flex: 1;
  padding: 8px 0 32px 16px;
}

.stp-04__entry:last-child .stp-04__content {
  padding-bottom: 0;
}

.stp-04__step-tag {
  display: inline-block;
  font-size: 10px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 600;
  margin-bottom: 4px;
}

.stp-04__entry.is-done .stp-04__step-tag {
  color: var(--fuchsia);
}

.stp-04__entry.is-active .stp-04__step-tag {
  color: var(--fuchsia);
}

.stp-04__step-name {
  font-size: 17px;
  font-weight: 700;
  color: var(--muted);
  margin-bottom: 4px;
  transition: color .3s;
}

.stp-04__entry.is-done .stp-04__step-name {
  color: var(--dark);
}

.stp-04__entry.is-active .stp-04__step-name {
  color: var(--dark);
}

.stp-04__step-desc {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.6;
}

.stp-04__entry.is-active .stp-04__step-desc {
  color: var(--mid);
}
/* active card */

.stp-04__card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 20px;
  margin-top: 14px;
  box-shadow: 0 4px 24px rgba(147,51,234,.08);
  display: none;
}

.stp-04__entry.is-active .stp-04__card {
  display: block;
}

.stp-04__field {
  margin-bottom: 12px;
}

.stp-04__fl {
  font-size: 11px;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 5px;
  display: block;
}

.stp-04__in {
  width: 100%;
  padding: 10px 14px;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--dark);
  font-size: 14px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.stp-04__in:focus {
  border-color: var(--fuchsia);
  box-shadow: 0 0 0 3px rgba(217,70,239,.12);
}

.stp-04__done-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(22,163,74,.1);
  border: 1px solid rgba(22,163,74,.2);
  color: var(--success);
  font-size: 12px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 999px;
  margin-top: 8px;
}
/* cta */

.stp-04__cta {
  margin-top: 8px;
  display: flex;
  gap: 10px;
  align-items: center;
}

.stp-04__btn {
  padding: 10px 22px;
  border-radius: 8px;
  border: none;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all .2s;
}

.stp-04__btn--primary {
  background: linear-gradient(135deg,var(--purple),var(--fuchsia));
  color: #fff;
  box-shadow: 0 4px 16px rgba(147,51,234,.3);
}

.stp-04__btn--primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 24px rgba(217,70,239,.4);
}

.stp-04__btn--ghost {
  background: transparent;
  border: 1px solid var(--border);
  color: var(--muted);
}

.stp-04__btn--ghost:hover {
  border-color: var(--purple);
  color: var(--dark);
}
/* completion */

.stp-04__complete {
  margin-top: 32px;
  background: linear-gradient(135deg,rgba(147,51,234,.08),rgba(217,70,239,.06));
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 28px;
  text-align: center;
  display: none;
}

.stp-04__complete.show {
  display: block;
  animation: stp-04-fadein .5s ease;
}

@keyframes stp-04-fadein {
  from {
    opacity: 0;
    transform: translateY(8px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.stp-04__complete-icon {
  font-size: 40px;
  margin-bottom: 12px;
}

.stp-04__complete-title {
  font-size: 20px;
  font-weight: 800;
  color: var(--dark);
}

.stp-04__complete-msg {
  font-size: 14px;
  color: var(--muted);
  margin-top: 6px;
}

@media (prefers-reduced-motion: reduce) {
  .stp-04__entry.is-active .stp-04__node {
    animation: none;
  }

  .stp-04__complete {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  let cur=3;
  const entries=document.querySelectorAll('.stp-04__entry');
  const complete=document.getElementById('stp-04-complete');

  function go(n){
    if(n>entries.length){
      entries.forEach(e=>{e.classList.remove('is-active');e.classList.add('is-done');e.querySelector('.stp-04__node').textContent='✓'});
      complete.classList.add('show');return;
    }
    cur=n;
    entries.forEach((e,i)=>{
      e.classList.remove('is-done','is-active');
      const node=e.querySelector('.stp-04__node');
      if(i+1<cur){e.classList.add('is-done');node.textContent='✓';}
      else if(i+1===cur){e.classList.add('is-active');node.textContent=cur;}
      else{node.textContent=i+1;}
    });
    complete.classList.remove('show');
  }

  document.getElementById('stp-04-next').onclick=()=>go(cur+1);
  document.getElementById('stp-04-back').onclick=()=>go(Math.max(1,cur-1));
  document.getElementById('stp-04-next2').onclick=()=>go(cur+1);
  document.getElementById('stp-04-back2').onclick=()=>go(Math.max(1,cur-1));
  document.getElementById('stp-04-submit').onclick=()=>go(cur+1);
  document.getElementById('stp-04-back3').onclick=()=>go(Math.max(1,cur-1));
})();
```
