---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dark-mode-toggle/localstorage-anti-flash-template/"
title: "LocalStorage Anti-Flash Template"
section: "snippets"
category: "css-dark-mode-toggle"
category_name: "CSS Dark Mode Toggles"
description: "An interactive simulation of the anti-FOUC pattern: an inline blocking IIFE reads localStorage before CSS loads and applies a data-dm05 attribute to prevent…"
has_js: "true"
---

Here's a working CSS Dark Mode Toggle from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: LocalStorage Anti-Flash Template
Source: https://codefronts.com/snippets/css-dark-mode-toggle/localstorage-anti-flash-template/

An interactive simulation of the anti-FOUC pattern: an inline blocking IIFE reads localStorage before CSS loads and applies a data-dm05 attribute to prevent any flash of white on dark pages.
## HTML
```html
<div class="dm-05" id="dm-05-root">
  <div class="dm-05__main">
    <div class="dm-05__topbar">
      <span class="dm-05__topbar-title">Anti-Flash Engine Active</span>
      <div class="dm-05__indicator"><div class="dm-05__led"></div>FOUC Protected</div>
    </div>
    <div class="dm-05__body">
      <span class="dm-05__eyebrow">⚡ localStorage</span>
      <h2 class="dm-05__title">Anti-Flash<br>Dark Mode</h2>
      <p class="dm-05__sub">An inline blocking IIFE in <code>&lt;head&gt;</code> reads localStorage <em>before</em> CSS loads, preventing any flash of unstyled white content. Simulate a page reload to see it work.</p>
      <div class="dm-05__console">
        <div class="dm-05__console-line">document.head &larr; inline script executes</div>
        <div class="dm-05__console-line">localStorage.getItem('theme') &rarr; <span id="dm-05-stored">null</span></div>
        <div class="dm-05__console-line dim">// CSS loads AFTER this block &rarr; no flash</div>
      </div>
      <div class="dm-05__refresh-row">
        <button class="dm-05__refresh-btn" id="dm-05-refresh">
          <i class="dm-05__refresh-icon">↺</i>Simulate Refresh
        </button>
        <button class="dm-05__toggle-btn" id="dm-05-toggle">
          <span id="dm-05-toggle-icon">🌙</span>
          <span id="dm-05-toggle-label">Switch to Dark</span>
        </button>
      </div>
    </div>
    <div class="dm-05__log">
      <div class="dm-05__log-title">Event log</div>
      <div class="dm-05__log-list" id="dm-05-log">
        <div class="dm-05__log-entry"><span class="ts">[init]</span>Page loaded — reading localStorage…</div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.dm-05,
.dm-05 *,
.dm-05 *::before,
.dm-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.dm-05 ::selection {
  background: #10b981;
  color: #000;
}

[data-dm05="dark"] .dm-05 {
  --bg: #030d08;
  --surface: #071a0f;
  --border: #0f3a1f;
  --text: #d1fae5;
  --muted: #4d7a5e;
  --accent: #10b981;
  --accent2: #34d399;
  --glow: rgba(16,185,129,0.3);
  --tag-bg: rgba(16,185,129,0.12);
  --console-bg: #010b05;
  --console-border: #0a2a12;
  --console-text: #34d399;
}

.dm-05 {
  --bg: #f0fdf8;
  --surface: #ffffff;
  --border: #d1fae5;
  --text: #064e3b;
  --muted: #6b8e7a;
  --accent: #059669;
  --accent2: #10b981;
  --glow: rgba(5,150,105,0.15);
  --tag-bg: rgba(5,150,105,0.1);
  --console-bg: #f0fdf4;
  --console-border: #bbf7d0;
  --console-text: #059669;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 24px;
  color: var(--text);
  transition: background 0.4s ease,color 0.4s ease;
}

.dm-05__main {
  width: min(520px,100%);
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 4px 40px rgba(0,0,0,0.06);
  transition: background 0.4s ease,border-color 0.4s ease,box-shadow 0.4s ease;
}

[data-dm05="dark"] .dm-05__main {
  box-shadow: 0 4px 40px var(--glow);
}

.dm-05__topbar {
  background: var(--accent);
  padding: 10px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.dm-05__topbar-title {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #fff;
}

.dm-05__indicator {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.8);
}

.dm-05__led {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #fff;
  animation: dm-05-pulse 2s ease-in-out infinite;
}

@keyframes dm-05-pulse {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0.3;
  }
}

.dm-05__body {
  padding: 32px 28px;
}

.dm-05__eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 3px 10px;
  border-radius: 99px;
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  background: var(--tag-bg);
  color: var(--accent);
  border: 1px solid rgba(5,150,105,0.2);
  margin-bottom: 12px;
  transition: background 0.4s ease,color 0.4s ease;
}

.dm-05__title {
  font-size: clamp(1.3rem,3.5vw,1.8rem);
  font-weight: 900;
  letter-spacing: -0.03em;
  color: var(--text);
  margin-bottom: 10px;
  transition: color 0.4s ease;
  line-height: 1.15;
}

.dm-05__sub {
  font-size: 0.85rem;
  line-height: 1.65;
  color: var(--muted);
  margin-bottom: 24px;
  transition: color 0.4s ease;
}
/* Console box */

.dm-05__console {
  background: var(--console-bg);
  border: 1px solid var(--console-border);
  border-radius: 12px;
  padding: 16px;
  font-family: monospace;
  margin-bottom: 20px;
  transition: background 0.4s ease,border-color 0.4s ease;
}

.dm-05__console-line {
  font-size: 0.75rem;
  line-height: 1.8;
  color: var(--console-text);
  transition: color 0.4s ease;
}

.dm-05__console-line::before {
  content: '> ';
  opacity: 0.5;
}

.dm-05__console-line.dim {
  opacity: 0.4;
}
/* Simulate refresh button */

.dm-05__refresh-row {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.dm-05__refresh-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 11px 22px;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  box-shadow: 0 3px 12px var(--glow);
  transition: background 0.3s ease,transform 0.2s ease,box-shadow 0.3s ease;
}

.dm-05__refresh-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 5px 20px var(--glow);
}

.dm-05__refresh-btn:active {
  transform: translateY(0);
}

.dm-05__refresh-btn.spinning .dm-05__refresh-icon {
  animation: dm-05-spin 0.6s linear;
}

@keyframes dm-05-spin {
  to {
    transform: rotate(360deg);
  }
}

.dm-05__refresh-icon {
  display: inline-block;
  font-style: normal;
}

.dm-05__toggle-btn {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 11px 18px;
  border-radius: 12px;
  border: 1.5px solid var(--border);
  cursor: pointer;
  background: transparent;
  color: var(--muted);
  font-size: 0.82rem;
  font-weight: 600;
  transition: border-color 0.3s ease,color 0.3s ease,background 0.3s ease;
}

.dm-05__toggle-btn:hover {
  border-color: var(--accent);
  color: var(--accent);
  background: var(--tag-bg);
}
/* History log */

.dm-05__log {
  border-top: 1px solid var(--border);
  padding: 16px 28px;
  transition: border-color 0.4s ease;
}

.dm-05__log-title {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 8px;
  transition: color 0.4s ease;
}

.dm-05__log-list {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.dm-05__log-entry {
  font-size: 0.72rem;
  color: var(--muted);
  font-family: monospace;
  transition: color 0.4s ease;
  opacity: 0;
  animation: dm-05-fadein 0.3s forwards;
}

@keyframes dm-05-fadein {
  to {
    opacity: 1;
  }
}

.dm-05__log-entry .ts {
  color: var(--accent);
  margin-right: 8px;
  opacity: 0.7;
}

@media (prefers-reduced-motion: reduce) {
  .dm-05,
    .dm-05 * {
    transition: none!important;
    animation: none!important;
  }
}
```

## JavaScript
```js
(()=>{
  const root=document.getElementById('dm-05-root');
  const storedSpan=document.getElementById('dm-05-stored');
  const toggleBtn=document.getElementById('dm-05-toggle');
  const toggleIcon=document.getElementById('dm-05-toggle-icon');
  const toggleLabel=document.getElementById('dm-05-toggle-label');
  const refreshBtn=document.getElementById('dm-05-refresh');
  const log=document.getElementById('dm-05-log');
  let dark=document.documentElement.getAttribute('data-dm05')==='dark';
  function addLog(msg){
    const el=document.createElement('div');
    el.className='dm-05__log-entry';
    const ts=new Date().toLocaleTimeString('en',{hour12:false,hour:'2-digit',minute:'2-digit',second:'2-digit'});
    el.innerHTML=`<span class="ts">[${ts}]</span>${msg}`;
    log.appendChild(el);
    if(log.children.length>6)log.removeChild(log.firstChild);
  }
  function applyTheme(isDark){
    dark=isDark;
    root.classList.toggle('is-dark',isDark);
    if(isDark){document.documentElement.setAttribute('data-dm05','dark');}
    else{document.documentElement.removeAttribute('data-dm05');}
    try{
      if(isDark)localStorage.setItem('dm05-theme','dark');
      else localStorage.removeItem('dm05-theme');
    }catch(e){}
    storedSpan.textContent=isDark?'"dark"':'null';
    toggleIcon.textContent=isDark?'☀️':'🌙';
    toggleLabel.textContent=isDark?'Switch to Light':'Switch to Dark';
  }
  toggleBtn.addEventListener('click',()=>{
    applyTheme(!dark);
    addLog(`Theme set to <strong>${dark?'dark':'light'}</strong> → saved to localStorage`);
  });
  refreshBtn.addEventListener('click',()=>{
    refreshBtn.classList.add('spinning');
    addLog('Simulating page reload…');
    setTimeout(()=>{
      const stored=dark?'dark':null;
      addLog(`localStorage['dm05-theme'] = ${stored?'"'+stored+'"':'null'} — applied BEFORE paint`);
      refreshBtn.classList.remove('spinning');
      addLog(`No FOUC — page painted in <strong>${dark?'dark':'light'}</strong> mode instantly ✓`);
    },600);
  });
  // Initial state
  storedSpan.textContent=dark?'"dark"':'null';
  toggleIcon.textContent=dark?'☀️':'🌙';
  toggleLabel.textContent=dark?'Switch to Light':'Switch to Dark';
  if(dark)addLog('Dark mode detected in localStorage — applied instantly');
})();
```
