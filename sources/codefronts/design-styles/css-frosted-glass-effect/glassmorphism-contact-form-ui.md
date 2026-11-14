---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-frosted-glass-effect/glassmorphism-contact-form-ui/"
title: "Glassmorphism Contact Form UI"
section: "design-styles"
category: "css-frosted-glass-effect"
category_name: "CSS Frosted Glass Effects"
description: "A split-panel glassmorphism contact card with a teal-emerald info sidebar featuring animated availability status and rotating decorative rings, plus a glass…"
has_js: "true"
---

Here's a working CSS Frosted Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Contact Form UI
Source: https://codefronts.com/design-styles/css-frosted-glass-effect/glassmorphism-contact-form-ui/

A split-panel glassmorphism contact card with a teal-emerald info sidebar featuring animated availability status and rotating decorative rings, plus a glass form panel with floating labels, custom select, textarea character counter, and a multi-state submit button.
## HTML
```html
<div class="fg-07">
  <div class="fg-02__bg" aria-hidden="true">
    <div class="fg-02__glow fg-02__glow--1"></div>
    <div class="fg-02__glow fg-02__glow--2"></div>
    <div class="fg-02__dots"></div>
  </div>
  <article class="fg-02__card">
    <aside class="fg-02__info">
      <div class="fg-02__info-body">
        <div class="fg-02__avail">
          <span class="fg-02__avail-dot"></span>
          <span>Available for projects</span>
        </div>
        <h2 class="fg-02__info-title">Let&#8217;s build<br>something great</h2>
        <p class="fg-02__info-sub">Drop us a message and we&#8217;ll respond within 24 hours.</p>
        <ul class="fg-02__contacts" role="list">
          <li class="fg-02__ci">
            <span class="fg-02__ci-icon" aria-hidden="true">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            </span>
            <span>48 Market St, San Francisco</span>
          </li>
          <li class="fg-02__ci">
            <span class="fg-02__ci-icon" aria-hidden="true">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            </span>
            <span>[email protected]</span>
          </li>
          <li class="fg-02__ci">
            <span class="fg-02__ci-icon" aria-hidden="true">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12 19.79 19.79 0 0 1 1.65 3.34 2 2 0 0 1 3.64 1.16h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L7.91 8.94a16 16 0 0 0 6.29 6.29l.95-.95a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            </span>
            <span>+1 (415) 555-0192</span>
          </li>
        </ul>
      </div>
      <div class="fg-02__deco" aria-hidden="true">
        <svg class="fg-02__deco-r fg-02__deco-r--a" viewBox="0 0 200 200" fill="none"><circle cx="100" cy="100" r="92" stroke="rgba(20,184,166,.14)" stroke-width="1"/></svg>
        <svg class="fg-02__deco-r fg-02__deco-r--b" viewBox="0 0 200 200" fill="none"><circle cx="100" cy="100" r="92" stroke="rgba(20,184,166,.24)" stroke-width="1" stroke-dasharray="6 10"/></svg>
        <svg class="fg-02__deco-r fg-02__deco-r--c" viewBox="0 0 200 200" fill="none"><circle cx="100" cy="100" r="60" stroke="rgba(99,102,241,.2)" stroke-width="1" stroke-dasharray="3 7"/></svg>
      </div>
    </aside>
    <div class="fg-02__form-wrap">
      <h3 class="fg-02__form-title">Send a message</h3>
      <div class="fg-02__row2">
        <div class="fg-02__field">
          <input class="fg-02__input" type="text" id="fg-07-name" placeholder=" " autocomplete="name">
          <label class="fg-02__label" for="fg-07-name">Full name</label>
        </div>
        <div class="fg-02__field">
          <input class="fg-02__input" type="email" id="fg-07-email" placeholder=" " autocomplete="email">
          <label class="fg-02__label" for="fg-07-email">Email</label>
        </div>
      </div>
      <div class="fg-02__field fg-02__field--sel">
        <select class="fg-02__input fg-02__sel" id="fg-07-subject">
          <option value="" disabled selected></option>
          <option value="project">New project inquiry</option>
          <option value="collab">Collaboration proposal</option>
          <option value="support">Technical support</option>
          <option value="other">Other</option>
        </select>
        <label class="fg-02__label fg-02__label--top" for="fg-07-subject">Subject</label>
        <span class="fg-02__sel-arrow" aria-hidden="true">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
        </span>
      </div>
      <div class="fg-02__field fg-02__field--area">
        <textarea class="fg-02__input fg-02__ta" id="fg-07-msg" placeholder=" " maxlength="300" rows="4"></textarea>
        <label class="fg-02__label" for="fg-07-msg">Your message</label>
        <span class="fg-02__cnt"><span id="fg-07-count">0</span>/300</span>
      </div>
      <button type="button" class="fg-02__btn" id="fg-07-btn">
        <span class="fg-02__btn-txt">Send Message</span>
        <span class="fg-02__btn-ico" aria-hidden="true">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
        </span>
        <span class="fg-02__btn-spin" aria-hidden="true">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><circle cx="12" cy="12" r="10" opacity=".2"/><path d="M12 2a10 10 0 0 1 10 10"/></svg>
        </span>
      </button>
    </div>
    <div class="fg-02__ok" id="fg-07-ok" aria-live="polite">
      <div class="fg-02__ok-ring"><svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg></div>
      <p class="fg-02__ok-title">Message sent!</p>
      <p class="fg-02__ok-msg">We&#8217;ll get back to you within 24 hours.</p>
      <button type="button" class="fg-02__ok-back" id="fg-07-back">Send another &#8594;</button>
    </div>
  </article>
</div>
```
## CSS
```css
.fg-07,
.fg-07 *,
.fg-07 *::before,
.fg-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fg-07 ::selection {
  background: rgba(20,184,166,.4);
  color: #fff;
}

.fg-07 {
  --c-bg: #060614;
  --c-a: #14b8a6;
  --c-a2: #6366f1;
  --c-text: #e2e8f4;
  --c-muted: rgba(226,232,244,.5);
  --c-glass: rgba(255,255,255,.055);
  --c-border: rgba(255,255,255,.1);
  --c-field: rgba(255,255,255,.05);
  --c-fborder: rgba(255,255,255,.09);
  --t: .25s ease;
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--c-bg);
  position: relative;
  overflow: hidden;
  padding: 40px 20px;
}
/* ── animated background ── */

.fg-02__bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
}

.fg-02__glow {
  position: absolute;
  border-radius: 50%;
}

.fg-02__glow--1 {
  width: 520px;
  height: 520px;
  background: radial-gradient(circle,rgba(20,184,166,.3),transparent 70%);
  top: -130px;
  left: -130px;
  animation: fg-07-g1 20s ease-in-out infinite alternate;
}

.fg-02__glow--2 {
  width: 440px;
  height: 440px;
  background: radial-gradient(circle,rgba(99,102,241,.26),transparent 70%);
  bottom: -110px;
  right: -110px;
  animation: fg-07-g2 26s ease-in-out infinite alternate;
}

.fg-02__dots {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(rgba(255,255,255,.05) 1px,transparent 1px);
  background-size: 24px 24px;
}

@keyframes fg-07-g1 {
  to {
    transform: translate(100px,80px) scale(1.22);
  }
}

@keyframes fg-07-g2 {
  to {
    transform: translate(-90px,-110px) scale(1.18);
  }
}
/* ── split glass card ── */

.fg-02__card {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 800px;
  display: grid;
  grid-template-columns: 1fr 1.45fr;
  background: var(--c-glass);
  backdrop-filter: blur(22px) saturate(155%);
  -webkit-backdrop-filter: blur(22px) saturate(155%);
  border: 1px solid var(--c-border);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 12px 60px rgba(0,0,0,.55),0 1px 0 rgba(255,255,255,.08) inset;
}
/* ── info sidebar ── */

.fg-02__info {
  position: relative;
  overflow: hidden;
  padding: 44px 36px;
  background: rgba(20,184,166,.05);
  border-right: 1px solid rgba(255,255,255,.07);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.fg-02__info-body {
  position: relative;
  z-index: 1;
}

.fg-02__avail {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .4px;
  color: var(--c-a);
  padding: 5px 12px;
  border-radius: 20px;
  background: rgba(20,184,166,.11);
  border: 1px solid rgba(20,184,166,.25);
  margin-bottom: 18px;
  width: fit-content;
}

.fg-02__avail-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--c-a);
  box-shadow: 0 0 8px var(--c-a);
  animation: fg-07-pulse 2s ease-in-out infinite;
}

@keyframes fg-07-pulse {
  0%,
    100% {
    opacity: 1;
    transform: scale(1);
  }

  50% {
    opacity: .55;
    transform: scale(.75);
  }
}

.fg-02__info-title {
  font-size: clamp(22px,3vw,28px);
  font-weight: 800;
  letter-spacing: -.5px;
  color: var(--c-text);
  line-height: 1.25;
  margin-bottom: 12px;
}

.fg-02__info-sub {
  font-size: 14px;
  color: var(--c-muted);
  line-height: 1.65;
  margin-bottom: 30px;
}

.fg-02__contacts {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.fg-02__ci {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 13px;
  color: rgba(226,232,244,.8);
}

.fg-02__ci-icon {
  width: 34px;
  height: 34px;
  border-radius: 10px;
  flex-shrink: 0;
  background: rgba(20,184,166,.12);
  border: 1px solid rgba(20,184,166,.2);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--c-a);
}
/* ── decorative rotating rings ── */

.fg-02__deco {
  position: absolute;
  bottom: -40px;
  right: -40px;
  width: 210px;
  height: 210px;
  pointer-events: none;
}

.fg-02__deco-r {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.fg-02__deco-r--b {
  animation: fg-07-rot 32s linear infinite;
}

.fg-02__deco-r--c {
  animation: fg-07-rot 19s linear infinite reverse;
}

@keyframes fg-07-rot {
  to {
    transform: rotate(360deg);
  }
}
/* ── form wrap ── */

.fg-02__form-wrap {
  padding: 44px 40px;
}

.fg-02__form-title {
  font-size: 18px;
  font-weight: 700;
  color: var(--c-text);
  letter-spacing: -.3px;
  margin-bottom: 22px;
}

.fg-02__row2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}
/* ── floating-label field ── */

.fg-02__field {
  position: relative;
  margin-bottom: 14px;
}

.fg-02__input {
  width: 100%;
  background: var(--c-field);
  border: 1px solid var(--c-fborder);
  border-radius: 12px;
  padding: 20px 16px 8px;
  color: var(--c-text);
  font-size: 14px;
  outline: none;
  -webkit-appearance: none;
  appearance: none;
  transition: border-color var(--t),box-shadow var(--t);
}

.fg-02__input:focus {
  border-color: var(--c-a);
  box-shadow: 0 0 0 3px rgba(20,184,166,.2);
}

.fg-02__label {
  position: absolute;
  top: 14px;
  left: 16px;
  color: var(--c-muted);
  font-size: 14px;
  pointer-events: none;
  transition: top .2s,font-size .2s,letter-spacing .2s,color .2s;
}

.fg-02__input:focus~.fg-02__label,
.fg-02__input:not(:placeholder-shown)~.fg-02__label {
  top: 6px;
  font-size: 11px;
  letter-spacing: .3px;
  color: var(--c-a);
}

.fg-02__label--top {
  top: 6px;
  font-size: 11px;
  letter-spacing: .3px;
  color: var(--c-a);
}
/* ── select ── */

.fg-02__field--sel .fg-02__input {
  padding-right: 44px;
  cursor: pointer;
}

.fg-02__sel-arrow {
  position: absolute;
  right: 14px;
  top: 50%;
  transform: translateY(-50%);
  pointer-events: none;
  color: var(--c-muted);
  display: flex;
  align-items: center;
}
/* ── textarea + counter ── */

.fg-02__ta {
  resize: none;
  padding-bottom: 28px;
}

.fg-02__field--area {
  margin-bottom: 18px;
}

.fg-02__cnt {
  position: absolute;
  bottom: 10px;
  right: 14px;
  font-size: 11px;
  color: var(--c-muted);
  transition: color .2s;
  pointer-events: none;
}

.fg-02__cnt.is-warn {
  color: #f59e0b;
}

.fg-02__cnt.is-limit {
  color: #f87171;
}
/* ── submit button ── */

.fg-02__btn {
  width: 100%;
  padding: 14px 24px;
  border: none;
  border-radius: 12px;
  background: linear-gradient(135deg,var(--c-a) 0%,var(--c-a2) 100%);
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  box-shadow: 0 4px 22px rgba(20,184,166,.38);
  position: relative;
  overflow: hidden;
  transition: transform .15s,box-shadow .2s,opacity .2s;
}

.fg-02__btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -80%;
  width: 50%;
  height: 100%;
  background: linear-gradient(90deg,transparent,rgba(255,255,255,.2),transparent);
  animation: fg-07-shine 2.8s linear infinite;
}

@keyframes fg-07-shine {
  to {
    left: 160%;
  }
}

.fg-02__btn:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 6px 32px rgba(20,184,166,.55);
}

.fg-02__btn:active:not(:disabled) {
  transform: translateY(0);
}

.fg-02__btn:disabled {
  opacity: .65;
  cursor: not-allowed;
}

.fg-02__btn-spin {
  display: none;
}

.fg-02__btn-spin svg {
  animation: fg-07-spin .75s linear infinite;
}

@keyframes fg-07-spin {
  to {
    transform: rotate(360deg);
  }
}
/* ── success overlay ── */

.fg-02__ok {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  text-align: center;
  padding: 44px;
  background: rgba(6,6,20,.9);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  opacity: 0;
  pointer-events: none;
  transition: opacity .4s;
  z-index: 10;
}

.fg-02__ok.is-visible {
  opacity: 1;
  pointer-events: auto;
}

.fg-02__ok-ring {
  width: 76px;
  height: 76px;
  border-radius: 50%;
  background: linear-gradient(135deg,var(--c-a),#34d399);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 50px rgba(20,184,166,.55);
}

.fg-02__ok.is-visible .fg-02__ok-ring {
  animation: fg-07-pop .52s cubic-bezier(.175,.885,.32,1.275) both;
}

@keyframes fg-07-pop {
  from {
    transform: scale(0) rotate(-25deg);
  }

  to {
    transform: scale(1) rotate(0);
  }
}

.fg-02__ok-title {
  font-size: 28px;
  font-weight: 800;
  color: var(--c-text);
  letter-spacing: -.5px;
}

.fg-02__ok-msg {
  font-size: 14px;
  color: var(--c-muted);
  max-width: 280px;
  line-height: 1.65;
}

.fg-02__ok-back {
  margin-top: 4px;
  background: rgba(20,184,166,.14);
  border: 1px solid rgba(20,184,166,.3);
  border-radius: 10px;
  padding: 10px 26px;
  color: var(--c-a);
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: background var(--t),transform .15s;
}

.fg-02__ok-back:hover {
  background: rgba(20,184,166,.26);
  transform: translateY(-1px);
}

@media (max-width: 640px) {
  .fg-02__card {
    grid-template-columns: 1fr;
  }

  .fg-02__info {
    padding: 32px 28px;
  }

  .fg-02__deco {
    display: none;
  }

  .fg-02__form-wrap {
    padding: 32px 28px;
  }

  .fg-02__row2 {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fg-02__glow,
    .fg-02__deco-r,
    .fg-02__avail-dot,
    .fg-02__btn::before,
    .fg-02__btn-spin svg {
    animation: none;
  }

  .fg-02__input,
    .fg-02__label,
    .fg-02__ok,
    .fg-02__btn,
    .fg-02__ok-back,
    .fg-02__cnt {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var r=document.querySelector('.fg-07');
  if(!r)return;

  /* character counter */
  var ta=r.querySelector('#fg-07-msg');
  var cntNum=r.querySelector('#fg-07-count');
  var cntWrap=r.querySelector('.fg-02__cnt');
  if(ta&&cntNum&&cntWrap){
    ta.addEventListener('input',function(){
      var n=ta.value.length;
      cntNum.textContent=String(n);
      cntWrap.classList.toggle('is-warn',n>=240&&n<280);
      cntWrap.classList.toggle('is-limit',n>=280);
    });
  }

  /* submit flow: idle → loading → success */
  var btn=r.querySelector('#fg-07-btn');
  var okEl=r.querySelector('#fg-07-ok');
  var txtEl=r.querySelector('.fg-02__btn-txt');
  var icoEl=r.querySelector('.fg-02__btn-ico');
  var spnEl=r.querySelector('.fg-02__btn-spin');
  if(btn&&okEl&&txtEl&&icoEl&&spnEl){
    btn.addEventListener('click',function(){
      btn.disabled=true;
      txtEl.textContent='Sending…';
      icoEl.style.display='none';
      spnEl.style.display='inline-flex';
      setTimeout(function(){
        okEl.classList.add('is-visible');
        btn.disabled=false;
        txtEl.textContent='Send Message';
        icoEl.style.display='';
        spnEl.style.display='none';
      },1400);
    });
  }

  /* back / reset */
  var backBtn=r.querySelector('#fg-07-back');
  if(backBtn&&okEl){
    backBtn.addEventListener('click',function(){
      okEl.classList.remove('is-visible');
      r.querySelectorAll('.fg-02__input').forEach(function(inp){inp.value=''});
      if(cntNum)cntNum.textContent='0';
      if(cntWrap){cntWrap.classList.remove('is-warn','is-limit')}
    });
  }
})();
```
