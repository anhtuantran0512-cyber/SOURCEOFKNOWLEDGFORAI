---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-frosted-glass-effect/frosted-glass-modal-popup/"
title: "Frosted Glass Modal Popup"
section: "design-styles"
category: "css-frosted-glass-effect"
category_name: "CSS Frosted Glass Effects"
description: "An alert dialog that blurs and dims the entire background page content with a CSS backdrop-filter overlay."
has_js: "true"
---

Here's a working CSS Frosted Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Frosted Glass Modal Popup
Source: https://codefronts.com/design-styles/css-frosted-glass-effect/frosted-glass-modal-popup/

An alert dialog that blurs and dims the entire background page content with a CSS backdrop-filter overlay. Features a glass modal with warning icon, destructive confirm / cancel button pair, success feedback state, ESC key support, and overlay-click dismissal.
## HTML
```html
<div class="fg-15">
  <div class="fg-10__bg" aria-hidden="true">
    <div class="fg-10__glow fg-10__glow--1"></div>
    <div class="fg-10__glow fg-10__glow--2"></div>
  </div>
  <div class="fg-10__page" aria-hidden="true">
    <div class="fg-10__pg-card">
      <div class="fg-10__pg-bar fg-10__pg-bar--1"></div>
      <div class="fg-10__pg-lines"><div></div><div></div><div></div></div>
    </div>
    <div class="fg-10__pg-card fg-10__pg-card--mid">
      <div class="fg-10__pg-circle"></div>
      <div class="fg-10__pg-lines"><div></div><div></div></div>
      <button class="fg-10__trigger" id="fg-15-open">Delete Project</button>
    </div>
    <div class="fg-10__pg-card">
      <div class="fg-10__pg-bar fg-10__pg-bar--2"></div>
      <div class="fg-10__pg-lines"><div></div><div></div><div></div></div>
    </div>
  </div>
  <div class="fg-10__overlay" id="fg-15-overlay" aria-hidden="true">
    <div class="fg-10__modal" id="fg-15-modal" role="alertdialog" aria-modal="true" aria-labelledby="fg-15-title" aria-describedby="fg-15-msg">
      <button class="fg-10__close" id="fg-15-close" aria-label="Close dialog">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      <div class="fg-10__modal-icon" id="fg-15-icon">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
      </div>
      <h2 class="fg-10__modal-title" id="fg-15-title">Confirm Deletion</h2>
      <p class="fg-10__modal-msg" id="fg-15-msg">This action will permanently delete <strong>Project Aurora</strong> and all its files. This cannot be undone.</p>
      <div class="fg-10__modal-btns" id="fg-15-btns">
        <button class="fg-10__btn fg-10__btn--cancel" id="fg-15-cancel">Cancel</button>
        <button class="fg-10__btn fg-10__btn--del" id="fg-15-confirm">
          <span class="fg-10__btn-txt">Delete Project</span>
          <span class="fg-10__btn-spin"></span>
        </button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fg-15,
.fg-15 *,
.fg-15 *::before,
.fg-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fg-15 ::selection {
  background: rgba(239,68,68,.4);
  color: #fff;
}

.fg-15 {
  --c-bg: #080818;
  --c-red: #ef4444;
  --c-red2: #dc2626;
  --c-glass: rgba(255,255,255,.06);
  --c-border: rgba(255,255,255,.1);
  --c-text: #eef0ff;
  --c-muted: rgba(238,240,255,.5);
  --t: .25s ease;
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  background: var(--c-bg);
}

.fg-10__bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
  z-index: 0;
}

.fg-10__glow {
  position: absolute;
  border-radius: 50%;
}

.fg-10__glow--1 {
  width: 400px;
  height: 400px;
  background: radial-gradient(circle,rgba(99,102,241,.2),transparent 70%);
  top: -80px;
  left: -80px;
  animation: fg-15-g1 22s ease-in-out infinite alternate;
}

.fg-10__glow--2 {
  width: 360px;
  height: 360px;
  background: radial-gradient(circle,rgba(239,68,68,.15),transparent 70%);
  bottom: -80px;
  right: -80px;
  animation: fg-15-g2 18s ease-in-out infinite alternate;
}

@keyframes fg-15-g1 {
  to {
    transform: translate(60px,80px) scale(1.15);
  }
}

@keyframes fg-15-g2 {
  to {
    transform: translate(-60px,-60px) scale(1.1);
  }
}

.fg-10__page {
  position: relative;
  z-index: 1;
  min-height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  padding: 40px 20px;
  flex-wrap: wrap;
}

.fg-10__pg-card {
  width: 180px;
  height: 220px;
  background: var(--c-glass);
  backdrop-filter: blur(16px) saturate(140%);
  -webkit-backdrop-filter: blur(16px) saturate(140%);
  border: 1px solid var(--c-border);
  border-radius: 18px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  pointer-events: none;
}

.fg-10__pg-card--mid {
  pointer-events: all;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
}

.fg-10__pg-bar {
  height: 8px;
  border-radius: 4px;
}

.fg-10__pg-bar--1 {
  background: linear-gradient(90deg,#6366f1,#8b5cf6);
  width: 100%;
}

.fg-10__pg-bar--2 {
  background: linear-gradient(90deg,#10b981,#14b8a6);
  width: 80%;
}

.fg-10__pg-lines {
  display: flex;
  flex-direction: column;
  gap: 7px;
  flex: 1;
}

.fg-10__pg-lines div {
  height: 8px;
  border-radius: 4px;
  background: rgba(255,255,255,.08);
}

.fg-10__pg-lines div:nth-child(2) {
  width: 75%;
}

.fg-10__pg-lines div:nth-child(3) {
  width: 55%;
}

.fg-10__pg-circle {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: linear-gradient(135deg,rgba(239,68,68,.3),rgba(220,38,38,.2));
  border: 1px solid rgba(239,68,68,.3);
}

.fg-10__trigger {
  padding: 10px 20px;
  border: 1px solid rgba(239,68,68,.4);
  border-radius: 10px;
  background: rgba(239,68,68,.12);
  color: #f87171;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  transition: background var(--t),transform .15s;
}

.fg-10__trigger:hover {
  background: rgba(239,68,68,.22);
  transform: translateY(-1px);
}

.fg-10__overlay {
  position: absolute;
  inset: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  background: rgba(0,0,0,0);
  backdrop-filter: blur(0px);
  -webkit-backdrop-filter: blur(0px);
  opacity: 0;
  pointer-events: none;
  transition: opacity .25s ease,background .25s ease,backdrop-filter .25s ease,-webkit-backdrop-filter .25s ease;
}

.fg-10__overlay.is-open {
  opacity: 1;
  pointer-events: all;
  background: rgba(0,0,0,.55);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.fg-10__modal {
  position: relative;
  width: 100%;
  max-width: 400px;
  background: rgba(15,15,35,.85);
  backdrop-filter: blur(24px) saturate(160%);
  -webkit-backdrop-filter: blur(24px) saturate(160%);
  border: 1px solid var(--c-border);
  border-radius: 22px;
  padding: 32px 28px 28px;
  box-shadow: 0 24px 80px rgba(0,0,0,.7),0 1px 0 rgba(255,255,255,.1) inset;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  transform: translateY(-16px);
  opacity: 0;
  transition: transform .3s cubic-bezier(.34,1.36,.64,1),opacity .25s ease;
}

.fg-10__overlay.is-open .fg-10__modal {
  transform: translateY(0);
  opacity: 1;
}

.fg-10__close {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 32px;
  height: 32px;
  border: 1px solid var(--c-border);
  border-radius: 50%;
  background: rgba(255,255,255,.06);
  color: rgba(255,255,255,.6);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background var(--t);
}

.fg-10__close:hover {
  background: rgba(255,255,255,.12);
  color: var(--c-text);
}

.fg-10__modal-icon {
  width: 64px;
  height: 64px;
  border-radius: 20px;
  background: linear-gradient(135deg,rgba(239,68,68,.25),rgba(220,38,38,.15));
  border: 1px solid rgba(239,68,68,.3);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 18px;
  color: #f87171;
}

.fg-10__modal-icon.is-success {
  background: linear-gradient(135deg,rgba(16,185,129,.25),rgba(5,150,105,.15));
  border-color: rgba(16,185,129,.3);
  color: #34d399;
}

.fg-10__modal-title {
  font-size: 20px;
  font-weight: 800;
  color: var(--c-text);
  letter-spacing: -.3px;
  margin-bottom: 10px;
}

.fg-10__modal-msg {
  font-size: 14px;
  color: var(--c-muted);
  line-height: 1.65;
  margin-bottom: 24px;
}

.fg-10__modal-msg strong {
  color: var(--c-text);
  font-weight: 700;
}

.fg-10__modal-btns {
  display: flex;
  gap: 10px;
  width: 100%;
}

.fg-10__btn {
  flex: 1;
  padding: 13px;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  transition: background var(--t),transform .15s,box-shadow .2s;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.fg-10__btn--cancel {
  background: rgba(255,255,255,.08);
  border: 1px solid var(--c-border);
  color: var(--c-text);
}

.fg-10__btn--cancel:hover {
  background: rgba(255,255,255,.13);
}

.fg-10__btn--del {
  background: linear-gradient(135deg,var(--c-red),var(--c-red2));
  border: none;
  color: #fff;
  box-shadow: 0 4px 18px rgba(239,68,68,.35);
}

.fg-10__btn--del:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 6px 24px rgba(239,68,68,.5);
}

.fg-10__btn--del:disabled {
  opacity: .7;
  cursor: not-allowed;
  transform: none;
}

.fg-10__btn-spin {
  display: none;
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255,255,255,.3);
  border-top-color: #fff;
  border-radius: 50%;
  animation: fg-15-spin .7s linear infinite;
}

@keyframes fg-15-spin {
  to {
    transform: rotate(360deg);
  }
}

.fg-10__btn--del.is-loading .fg-10__btn-txt {
  display: none;
}

.fg-10__btn--del.is-loading .fg-10__btn-spin {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .fg-10__glow,
    .fg-10__btn-spin {
    animation: none;
  }

  .fg-10__overlay,
    .fg-10__modal,
    .fg-10__btn,
    .fg-10__trigger,
    .fg-10__close {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var r=document.querySelector('.fg-15');
  if(!r)return;
  var overlay=r.querySelector('#fg-15-overlay');
  var modal=r.querySelector('#fg-15-modal');
  var icon=r.querySelector('#fg-15-icon');
  var title=r.querySelector('#fg-15-title');
  var msg=r.querySelector('#fg-15-msg');
  var btns=r.querySelector('#fg-15-btns');
  var confirmBtn=r.querySelector('#fg-15-confirm');
  var escHandler;
  function openModal(){
    overlay.classList.add('is-open');
    overlay.setAttribute('aria-hidden','false');
    escHandler=function(e){if(e.key==='Escape')closeModal()};
    document.addEventListener('keydown',escHandler);
    setTimeout(function(){confirmBtn&&confirmBtn.focus()},300);
  }
  function closeModal(){
    overlay.classList.remove('is-open');
    overlay.setAttribute('aria-hidden','true');
    document.removeEventListener('keydown',escHandler);
    setTimeout(function(){
      icon.classList.remove('is-success');
      icon.innerHTML='<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>';
      title.textContent='Confirm Deletion';
      msg.innerHTML='This action will permanently delete <strong>Project Aurora</strong> and all its files. This cannot be undone.';
      btns.style.display='';
      confirmBtn.classList.remove('is-loading');
      confirmBtn.disabled=false;
    },300);
  }
  r.querySelector('#fg-15-open').addEventListener('click',openModal);
  r.querySelector('#fg-15-close').addEventListener('click',closeModal);
  r.querySelector('#fg-15-cancel').addEventListener('click',closeModal);
  overlay.addEventListener('click',function(e){if(e.target===overlay)closeModal()});
  confirmBtn.addEventListener('click',function(){
    confirmBtn.classList.add('is-loading');confirmBtn.disabled=true;
    r.querySelector('#fg-15-cancel').disabled=true;
    setTimeout(function(){
      confirmBtn.classList.remove('is-loading');
      icon.classList.add('is-success');
      icon.innerHTML='<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>';
      title.textContent='Deleted Successfully';
      msg.innerHTML='<strong>Project Aurora</strong> and all associated files have been permanently removed.';
      btns.style.display='none';
      setTimeout(closeModal,1800);
    },1400);
  });
})();
```
