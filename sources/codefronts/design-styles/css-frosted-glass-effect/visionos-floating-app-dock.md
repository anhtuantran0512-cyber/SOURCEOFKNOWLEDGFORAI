---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-frosted-glass-effect/visionos-floating-app-dock/"
title: "VisionOS Floating App Dock"
section: "design-styles"
category: "css-frosted-glass-effect"
category_name: "CSS Frosted Glass Effects"
description: "A spatial-computing dock aesthetic inspired by Apple Vision Pro — a thick glass capsule housing six app icons with unique gradient tiles, hover…"
has_js: "true"
---

Here's a working CSS Frosted Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: VisionOS Floating App Dock
Source: https://codefronts.com/design-styles/css-frosted-glass-effect/visionos-floating-app-dock/

A spatial-computing dock aesthetic inspired by Apple Vision Pro — a thick glass capsule housing six app icons with unique gradient tiles, hover scale-and-glow, bounce-on-click, and a floating glass app window that opens per-app with content and a close button.
## HTML
```html
<div class="fg-16">
  <div class="fg-11__env" aria-hidden="true">
    <div class="fg-11__orb fg-11__orb--1"></div>
    <div class="fg-11__orb fg-11__orb--2"></div>
    <div class="fg-11__orb fg-11__orb--3"></div>
    <div class="fg-11__grid"></div>
  </div>
  <div class="fg-11__scene">
    <div class="fg-11__win-wrap">
      <div class="fg-11__win" id="fg-16-win" aria-live="polite" aria-atomic="true">
        <div class="fg-11__win-hd">
          <div class="fg-11__win-icon" id="fg-16-win-icon"></div>
          <p class="fg-11__win-title" id="fg-16-win-title"></p>
          <button class="fg-11__win-close" id="fg-16-win-close" aria-label="Close app">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
          </button>
        </div>
        <div class="fg-11__win-body" id="fg-16-win-body"></div>
      </div>
    </div>
    <div class="fg-11__dock" role="toolbar" aria-label="App dock">
      <div class="fg-11__icons" id="fg-16-icons"></div>
    </div>
    <div class="fg-11__pip-row" aria-hidden="true">
      <span class="fg-11__pip fg-11__pip--on"></span>
      <span class="fg-11__pip"></span>
      <span class="fg-11__pip"></span>
    </div>
  </div>
</div>
```
## CSS
```css
.fg-16,
.fg-16 *,
.fg-16 *::before,
.fg-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fg-16 ::selection {
  background: rgba(99,102,241,.5);
  color: #fff;
}

.fg-16 {
  --c-bg: #030308;
  --c-glass: rgba(255,255,255,.06);
  --c-border: rgba(255,255,255,.1);
  --c-text: #eef0ff;
  --c-muted: rgba(238,240,255,.5);
  --t: .25s ease;
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  background: radial-gradient(ellipse 80% 60% at 50% 100%,rgba(30,20,60,.9),var(--c-bg) 70%);
}

.fg-11__env {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
}

.fg-11__orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
}

.fg-11__orb--1 {
  width: 500px;
  height: 300px;
  background: radial-gradient(ellipse,rgba(99,102,241,.2),transparent 70%);
  bottom: -100px;
  left: 50%;
  transform: translateX(-50%);
  animation: fg-16-o1 20s ease-in-out infinite alternate;
}

.fg-11__orb--2 {
  width: 300px;
  height: 300px;
  background: radial-gradient(circle,rgba(168,85,247,.15),transparent 70%);
  top: 10%;
  left: 5%;
  animation: fg-16-o2 25s ease-in-out infinite alternate;
}

.fg-11__orb--3 {
  width: 280px;
  height: 280px;
  background: radial-gradient(circle,rgba(20,184,166,.12),transparent 70%);
  top: 15%;
  right: 5%;
  animation: fg-16-o3 18s ease-in-out infinite alternate;
}

.fg-11__grid {
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(255,255,255,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.025) 1px,transparent 1px);
  background-size: 40px 40px;
}

@keyframes fg-16-o1 {
  to {
    transform: translateX(-50%) scale(1.2) translateY(-30px);
  }
}

@keyframes fg-16-o2 {
  to {
    transform: translate(50px,40px) scale(1.15);
  }
}

@keyframes fg-16-o3 {
  to {
    transform: translate(-40px,30px) scale(1.1);
  }
}

.fg-11__scene {
  position: relative;
  z-index: 1;
  min-height: 520px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  padding: 30px 20px 40px;
}

.fg-11__win-wrap {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding-bottom: 24px;
}

.fg-11__win {
  width: 100%;
  max-width: 340px;
  background: rgba(15,12,30,.8);
  backdrop-filter: blur(28px) saturate(180%);
  -webkit-backdrop-filter: blur(28px) saturate(180%);
  border: 1px solid var(--c-border);
  border-radius: 20px;
  box-shadow: 0 16px 60px rgba(0,0,0,.6),0 1px 0 rgba(255,255,255,.1) inset;
  opacity: 0;
  transform: translateY(14px);
  transition: opacity .3s ease,transform .35s cubic-bezier(.34,1.2,.64,1);
  pointer-events: none;
  overflow: hidden;
}

.fg-11__win.is-open {
  opacity: 1;
  transform: translateY(0);
  pointer-events: all;
}

.fg-11__win-hd {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 18px 14px;
  border-bottom: 1px solid rgba(255,255,255,.07);
}

.fg-11__win-icon {
  width: 32px;
  height: 32px;
  border-radius: 9px;
  flex-shrink: 0;
}

.fg-11__win-title {
  flex: 1;
  font-size: 15px;
  font-weight: 700;
  color: var(--c-text);
}

.fg-11__win-close {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.12);
  color: rgba(255,255,255,.55);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background var(--t);
}

.fg-11__win-close:hover {
  background: rgba(239,68,68,.25);
  color: #f87171;
}

.fg-11__win-body {
  padding: 16px 18px 20px;
  min-height: 100px;
  color: var(--c-muted);
  font-size: 13px;
  line-height: 1.65;
}

.fg-11__dock {
  background: rgba(255,255,255,.07);
  backdrop-filter: blur(40px) saturate(200%);
  -webkit-backdrop-filter: blur(40px) saturate(200%);
  border: 1px solid rgba(255,255,255,.16);
  border-radius: 50px;
  padding: 14px 18px;
  box-shadow: 0 8px 48px rgba(0,0,0,.5),0 1px 0 rgba(255,255,255,.15) inset,0 -1px 0 rgba(0,0,0,.3) inset;
  position: relative;
}

.fg-11__dock::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50px;
  background: linear-gradient(180deg,rgba(255,255,255,.08) 0%,transparent 60%);
  pointer-events: none;
}

.fg-11__icons {
  display: flex;
  align-items: center;
  gap: 12px;
}

.fg-11__app {
  width: 56px;
  height: 56px;
  border-radius: 16px;
  cursor: pointer;
  position: relative;
  transition: transform .2s cubic-bezier(.34,1.4,.64,1),box-shadow .2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  border: 1px solid rgba(255,255,255,.15);
}

.fg-11__app:hover {
  transform: scale(1.18) translateY(-5px);
}

.fg-11__app.is-bounce {
  animation: fg-16-bounce .35s ease forwards;
}

.fg-11__app.is-active::after {
  content: '';
  position: absolute;
  bottom: -18px;
  left: 50%;
  transform: translateX(-50%);
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: rgba(255,255,255,.7);
}

@keyframes fg-16-bounce {
  0% {
    transform: scale(1) translateY(0);
  }

  25% {
    transform: scale(.82) translateY(4px);
  }

  65% {
    transform: scale(1.12) translateY(-6px);
  }

  100% {
    transform: scale(1) translateY(0);
  }
}

.fg-11__app-icon {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: none;
}

.fg-11__pip-row {
  display: flex;
  gap: 5px;
  margin-top: 16px;
  align-items: center;
}

.fg-11__pip {
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: rgba(255,255,255,.2);
}

.fg-11__pip--on {
  background: rgba(255,255,255,.6);
  width: 14px;
  border-radius: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .fg-11__orb {
    animation: none;
  }

  .fg-11__app.is-bounce {
    animation: none;
  }

  .fg-11__app,
    .fg-11__win,
    .fg-11__win-close {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var r=document.querySelector('.fg-16');
  if(!r)return;
  var APPS=[
    {name:'Files',grad:'linear-gradient(135deg,#3b82f6,#2563eb)',glow:'rgba(59,130,246,.6)',content:'<p><strong>Recent Files</strong></p><br><div style="display:flex;flex-direction:column;gap:8px"><div style="display:flex;align-items:center;gap:10px;padding:8px;background:rgba(255,255,255,.05);border-radius:8px;font-size:12px;color:#eef0ff"><svg width="14" height="14" viewBox="0 0 24 24" fill="#3b82f6"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8" fill="none" stroke="#3b82f6" stroke-width="2"/></svg>Project Aurora.fig</div><div style="display:flex;align-items:center;gap:10px;padding:8px;background:rgba(255,255,255,.05);border-radius:8px;font-size:12px;color:#eef0ff"><svg width="14" height="14" viewBox="0 0 24 24" fill="#6366f1"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8" fill="none" stroke="#6366f1" stroke-width="2"/></svg>Presentation.pptx</div></div>',icon:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,.9)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>'},
    {name:'Mail',grad:'linear-gradient(135deg,#ef4444,#dc2626)',glow:'rgba(239,68,68,.6)',content:'<p><strong>Inbox</strong> <span style="font-size:11px;background:rgba(239,68,68,.25);color:#f87171;padding:2px 7px;border-radius:10px;margin-left:6px">3 new</span></p><br><div style="display:flex;flex-direction:column;gap:7px"><div style="padding:9px;background:rgba(255,255,255,.06);border-radius:8px;font-size:12px;border-left:3px solid #ef4444"><p style="color:#eef0ff;font-weight:600;margin-bottom:3px">Alex Chen</p><p style="color:rgba(238,240,255,.5)">Re: Design Review tomorrow...</p></div><div style="padding:9px;background:rgba(255,255,255,.04);border-radius:8px;font-size:12px"><p style="color:#eef0ff;font-weight:600;margin-bottom:3px">Product Team</p><p style="color:rgba(238,240,255,.5)">Sprint planning — see you at 10</p></div></div>',icon:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,.9)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>'},
    {name:'Calendar',grad:'linear-gradient(135deg,#f59e0b,#d97706)',glow:'rgba(245,158,11,.6)',content:'<p><strong>Today &mdash; Monday</strong></p><br><div style="display:flex;flex-direction:column;gap:7px"><div style="padding:9px 12px;background:rgba(255,255,255,.06);border-radius:8px;border-left:3px solid #6366f1;font-size:12px"><p style="color:#eef0ff;font-weight:600">9:00 AM &mdash; Team Standup</p></div><div style="padding:9px 12px;background:rgba(255,255,255,.04);border-radius:8px;border-left:3px solid #8b5cf6;font-size:12px"><p style="color:#eef0ff;font-weight:600">2:30 PM &mdash; Design Review</p></div><div style="padding:9px 12px;background:rgba(255,255,255,.04);border-radius:8px;border-left:3px solid #10b981;font-size:12px"><p style="color:#eef0ff;font-weight:600">4:00 PM &mdash; Client Sync</p></div></div>',icon:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,.9)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>'},
    {name:'Browser',grad:'linear-gradient(135deg,#06b6d4,#0891b2)',glow:'rgba(6,182,212,.6)',content:'<div style="background:rgba(255,255,255,.07);border-radius:8px;padding:8px 12px;font-size:11px;color:rgba(238,240,255,.5);margin-bottom:12px;display:flex;align-items:center;gap:6px"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>codefronts.com</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:7px"><div style="padding:12px 8px;background:rgba(255,255,255,.05);border-radius:8px;text-align:center;font-size:11px;color:rgba(238,240,255,.6)">Bookmarks</div><div style="padding:12px 8px;background:rgba(255,255,255,.05);border-radius:8px;text-align:center;font-size:11px;color:rgba(238,240,255,.6)">History</div><div style="padding:12px 8px;background:rgba(255,255,255,.05);border-radius:8px;text-align:center;font-size:11px;color:rgba(238,240,255,.6)">Downloads</div><div style="padding:12px 8px;background:rgba(255,255,255,.05);border-radius:8px;text-align:center;font-size:11px;color:rgba(238,240,255,.6)">Reading List</div></div>',icon:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,.9)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>'},
    {name:'Photos',grad:'linear-gradient(135deg,#ec4899,#8b5cf6,#3b82f6)',glow:'rgba(139,92,246,.6)',content:'<p><strong>Recents</strong></p><br><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:5px"><div style="aspect-ratio:1;border-radius:6px;background:linear-gradient(135deg,#f59e0b,#ec4899)"></div><div style="aspect-ratio:1;border-radius:6px;background:linear-gradient(135deg,#6366f1,#3b82f6)"></div><div style="aspect-ratio:1;border-radius:6px;background:linear-gradient(135deg,#10b981,#06b6d4)"></div><div style="aspect-ratio:1;border-radius:6px;background:linear-gradient(135deg,#ec4899,#f97316)"></div><div style="aspect-ratio:1;border-radius:6px;background:linear-gradient(135deg,#8b5cf6,#6366f1)"></div><div style="aspect-ratio:1;border-radius:6px;background:linear-gradient(135deg,#14b8a6,#22c55e)"></div></div>',icon:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,.9)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5" fill="rgba(255,255,255,.9)"/><polyline points="21 15 16 10 5 21"/></svg>'},
    {name:'Settings',grad:'linear-gradient(135deg,#64748b,#475569)',glow:'rgba(100,116,139,.6)',content:'<div style="display:flex;flex-direction:column;gap:1px"><div style="display:flex;align-items:center;justify-content:space-between;padding:11px 12px;background:rgba(255,255,255,.05);border-radius:8px 8px 0 0;font-size:13px;color:#eef0ff"><span>Wi-Fi</span><span style="font-size:11px;color:#22c55e">Connected</span></div><div style="display:flex;align-items:center;justify-content:space-between;padding:11px 12px;background:rgba(255,255,255,.05);font-size:13px;color:#eef0ff"><span>Bluetooth</span><span style="font-size:11px;color:#3b82f6">On</span></div><div style="display:flex;align-items:center;justify-content:space-between;padding:11px 12px;background:rgba(255,255,255,.05);border-radius:0 0 8px 8px;font-size:13px;color:#eef0ff"><span>Notifications</span><span style="font-size:11px;color:rgba(238,240,255,.4)">Off</span></div></div>',icon:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,.9)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>'}
  ];
  var win=r.querySelector('#fg-16-win');
  var winIcon=r.querySelector('#fg-16-win-icon');
  var winTitle=r.querySelector('#fg-16-win-title');
  var winBody=r.querySelector('#fg-16-win-body');
  var closeBtn=r.querySelector('#fg-16-win-close');
  var iconsEl=r.querySelector('#fg-16-icons');
  var activeIdx=-1;
  APPS.forEach(function(app,i){
    var el=document.createElement('div');
    el.className='fg-11__app';
    el.style.background=app.grad;
    el.style.setProperty('--glow',app.glow);
    el.setAttribute('role','button');
    el.setAttribute('aria-label',app.name);
    el.setAttribute('tabindex','0');
    el.innerHTML='<div class="fg-11__app-icon">'+app.icon+'</div>';
    el.addEventListener('mouseenter',function(){el.style.boxShadow='0 8px 30px '+app.glow});
    el.addEventListener('mouseleave',function(){if(activeIdx!==i)el.style.boxShadow=''});
    function activate(){
      el.classList.remove('is-bounce');
      void el.offsetWidth;
      el.classList.add('is-bounce');
      el.addEventListener('animationend',function h(){el.classList.remove('is-bounce');el.removeEventListener('animationend',h)});
      if(activeIdx===i){win.classList.remove('is-open');iconsEl.querySelectorAll('.fg-11__app').forEach(function(a){a.classList.remove('is-active');a.style.boxShadow=''});activeIdx=-1;return}
      activeIdx=i;
      iconsEl.querySelectorAll('.fg-11__app').forEach(function(a,j){a.classList.toggle('is-active',j===i);if(j!==i)a.style.boxShadow=''});
      winIcon.style.background=app.grad;
      winTitle.textContent=app.name;
      winBody.innerHTML=app.content;
      win.classList.add('is-open');
    }
    el.addEventListener('click',activate);
    el.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();activate()}});
    iconsEl.appendChild(el);
  });
  closeBtn.addEventListener('click',function(){
    win.classList.remove('is-open');
    iconsEl.querySelectorAll('.fg-11__app').forEach(function(a){a.classList.remove('is-active');a.style.boxShadow=''});
    activeIdx=-1;
  });
})();
```
