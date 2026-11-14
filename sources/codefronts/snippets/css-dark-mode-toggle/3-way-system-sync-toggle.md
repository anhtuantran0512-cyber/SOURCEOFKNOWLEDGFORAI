---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dark-mode-toggle/3-way-system-sync-toggle/"
title: "3-Way System Sync Toggle"
section: "snippets"
category: "css-dark-mode-toggle"
category_name: "CSS Dark Mode Toggles"
description: "A glassmorphism segmented control with Light, Dark, and System modes — the glider pill positions itself using live getBoundingClientRect(), and System mode…"
has_js: "true"
---

Here's a working CSS Dark Mode Toggle from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3-Way System Sync Toggle
Source: https://codefronts.com/snippets/css-dark-mode-toggle/3-way-system-sync-toggle/

A glassmorphism segmented control with Light, Dark, and System modes — the glider pill positions itself using live getBoundingClientRect(), and System mode wires a matchMedia listener to the OS.
## HTML
```html
<div class="dm-04" id="dm-04-root">
  <div class="dm-04__control" id="dm-04-control">
    <div class="dm-04__glider" id="dm-04-glider"></div>
    <button class="dm-04__segment is-active" data-mode="light" aria-pressed="true">
      <span class="dm-04__segment-icon">☀️</span>
      <span class="dm-04__segment-label">Light</span>
    </button>
    <button class="dm-04__segment" data-mode="dark" aria-pressed="false">
      <span class="dm-04__segment-icon">🌙</span>
      <span class="dm-04__segment-label">Dark</span>
    </button>
    <button class="dm-04__segment" data-mode="system" aria-pressed="false">
      <span class="dm-04__segment-icon">⚙️</span>
      <span class="dm-04__segment-label">System</span>
    </button>
  </div>
  <div class="dm-04__os">
    <div class="dm-04__os-bar">
      <div class="dm-04__os-dots">
        <div class="dm-04__os-dot"></div>
        <div class="dm-04__os-dot"></div>
        <div class="dm-04__os-dot"></div>
      </div>
      <span class="dm-04__os-title">Settings</span>
      <span class="dm-04__mode-badge" id="dm-04-badge">Light</span>
    </div>
    <div class="dm-04__os-body">
      <h2 class="dm-04__os-heading">Appearance</h2>
      <p class="dm-04__os-sub">Manual override takes precedence over OS preference. System mode syncs with <code>prefers-color-scheme</code> automatically.</p>
      <div class="dm-04__sys-row" id="dm-04-sys-row">
        <span class="dm-04__sys-icon" id="dm-04-sys-icon">🖥️</span>
        <div class="dm-04__sys-info">
          <span class="dm-04__sys-label" id="dm-04-sys-label">System preference: Light</span>
          <span class="dm-04__sys-desc" id="dm-04-sys-desc">Detected via matchMedia API</span>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.dm-04,
.dm-04 *,
.dm-04 *::before,
.dm-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.dm-04 ::selection {
  background: #6366f1;
  color: #fff;
}

.dm-04 {
  --bg: #f8f7ff;
  --surface: rgba(255,255,255,0.85);
  --border: rgba(99,102,241,0.15);
  --text: #18174a;
  --muted: #6b7280;
  --accent: #6366f1;
  --active-bg: rgba(99,102,241,0.12);
  --glow: rgba(99,102,241,0.2);
  --track: #e5e7eb;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  background-image: radial-gradient(circle at 20% 30%,rgba(99,102,241,0.06) 0%,transparent 50%), radial-gradient(circle at 80% 70%,rgba(168,85,247,0.06) 0%,transparent 50%);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 32px;
  color: var(--text);
  transition: --bg 0.5s ease,background 0.5s ease,color 0.5s ease;
}

.dm-04.is-dark {
  --bg: #08071a;
  --surface: rgba(15,14,36,0.9);
  --border: rgba(99,102,241,0.25);
  --text: #e0dfff;
  --muted: #6b6d8c;
  --active-bg: rgba(99,102,241,0.2);
  --glow: rgba(99,102,241,0.35);
  --track: #1e1d40;
  background-image: radial-gradient(circle at 20% 30%,rgba(99,102,241,0.12) 0%,transparent 50%), radial-gradient(circle at 80% 70%,rgba(168,85,247,0.1) 0%,transparent 50%);
}
/* Segmented control */

.dm-04__control {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 6px;
  display: flex;
  gap: 2px;
  box-shadow: 0 4px 24px var(--glow),0 1px 3px rgba(0,0,0,0.06);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  position: relative;
  width: min(360px,100%);
  transition: background 0.5s ease,border-color 0.5s ease,box-shadow 0.5s ease;
}

.dm-04__segment {
  flex: 1;
  padding: 12px 8px;
  border-radius: 14px;
  border: none;
  cursor: pointer;
  background: transparent;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
  position: relative;
  z-index: 1;
  transition: background 0.3s ease,color 0.3s ease;
}

.dm-04__segment-icon {
  font-size: 20px;
  line-height: 1;
}

.dm-04__segment-label {
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  color: var(--muted);
  transition: color 0.3s ease;
  text-transform: uppercase;
}

.dm-04__segment.is-active .dm-04__segment-label {
  color: var(--accent);
}
/* Glider pill */

.dm-04__glider {
  position: absolute;
  top: 6px;
  height: calc(100% - 12px);
  border-radius: 14px;
  background: var(--active-bg);
  border: 1px solid rgba(99,102,241,0.3);
  box-shadow: 0 2px 8px var(--glow);
  transition: left 0.4s cubic-bezier(0.34,1.3,0.64,1),width 0.4s cubic-bezier(0.34,1.3,0.64,1);
  pointer-events: none;
  z-index: 0;
}
/* Preview OS window */

.dm-04__os {
  width: min(400px,100%);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 8px 48px rgba(0,0,0,0.12),0 1px 3px rgba(0,0,0,0.08);
  border: 1px solid var(--border);
  background: var(--surface);
  backdrop-filter: blur(20px);
  transition: background 0.5s ease,border-color 0.5s ease,box-shadow 0.5s ease;
}

.dm-04.is-dark .dm-04__os {
  box-shadow: 0 8px 48px rgba(99,102,241,0.2),0 1px 3px rgba(0,0,0,0.5);
}

.dm-04__os-bar {
  padding: 14px 18px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 10px;
  transition: border-color 0.5s ease;
}

.dm-04__os-dots {
  display: flex;
  gap: 5px;
}

.dm-04__os-dot {
  width: 11px;
  height: 11px;
  border-radius: 50%;
}

.dm-04__os-dot:nth-child(1) {
  background: #ff5f57;
}

.dm-04__os-dot:nth-child(2) {
  background: #febc2e;
}

.dm-04__os-dot:nth-child(3) {
  background: #28c840;
}

.dm-04__os-title {
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--muted);
  flex: 1;
  text-align: center;
  transition: color 0.5s ease;
}

.dm-04__mode-badge {
  padding: 3px 10px;
  border-radius: 99px;
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  background: var(--active-bg);
  color: var(--accent);
  border: 1px solid rgba(99,102,241,0.3);
  transition: background 0.5s ease,color 0.5s ease;
}

.dm-04__os-body {
  padding: 24px;
}

.dm-04__os-heading {
  font-size: 1.2rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: var(--text);
  margin-bottom: 6px;
  transition: color 0.5s ease;
}

.dm-04__os-sub {
  font-size: 0.83rem;
  color: var(--muted);
  line-height: 1.6;
  margin-bottom: 20px;
  transition: color 0.5s ease;
}
/* System pref row */

.dm-04__sys-row {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 16px;
  border-radius: 12px;
  background: var(--active-bg);
  border: 1px solid var(--border);
  transition: background 0.5s ease,border-color 0.5s ease;
}

.dm-04__sys-icon {
  font-size: 24px;
}

.dm-04__sys-info {
}

.dm-04__sys-label {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text);
  transition: color 0.5s ease;
  display: block;
}

.dm-04__sys-desc {
  font-size: 0.72rem;
  color: var(--muted);
  transition: color 0.5s ease;
}

@media (prefers-reduced-motion: reduce) {
  .dm-04,
    .dm-04 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
(()=>{
  const root=document.getElementById('dm-04-root');
  const glider=document.getElementById('dm-04-glider');
  const segs=[...document.querySelectorAll('.dm-04__segment')];
  const badge=document.getElementById('dm-04-badge');
  const sysIcon=document.getElementById('dm-04-sys-icon');
  const sysLabel=document.getElementById('dm-04-sys-label');
  const sysDesc=document.getElementById('dm-04-sys-desc');
  const mq=window.matchMedia('(prefers-color-scheme:dark)');
  let mode='light';
  function moveGlider(idx){
    const seg=segs[idx];
    const ctrl=seg.closest('#dm-04-control');
    const ctrlRect=ctrl.getBoundingClientRect();
    const segRect=seg.getBoundingClientRect();
    glider.style.left=(segRect.left-ctrlRect.left)+'px';
    glider.style.width=segRect.width+'px';
  }
  function applyMode(m){
    mode=m;
    const isDark=(m==='dark')||(m==='system'&&mq.matches);
    root.classList.toggle('is-dark',isDark);
    const labels={light:'Light',dark:'Dark',system:'System'};
    badge.textContent=labels[m];
    const sysDark=mq.matches;
    sysIcon.textContent=sysDark?'🌙':'☀️';
    sysLabel.textContent='System preference: '+(sysDark?'Dark':'Light');
    sysDesc.textContent=m==='system'?'Active — following OS preference':'Overridden by manual selection';
    segs.forEach((s,i)=>{
      const active=s.dataset.mode===m;
      s.classList.toggle('is-active',active);
      s.setAttribute('aria-pressed',active);
      if(active)moveGlider(i);
    });
  }
  segs.forEach(s=>s.addEventListener('click',()=>applyMode(s.dataset.mode)));
  mq.addEventListener('change',()=>{ if(mode==='system')applyMode('system'); });
  // Initial glider position
  requestAnimationFrame(()=>applyMode('light'));
})();
```
