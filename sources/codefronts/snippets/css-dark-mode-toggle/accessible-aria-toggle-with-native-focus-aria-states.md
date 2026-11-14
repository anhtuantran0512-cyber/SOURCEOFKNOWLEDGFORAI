---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dark-mode-toggle/accessible-aria-toggle-with-native-focus-aria-states/"
title: "Accessible ARIA Toggle with Native Focus & ARIA States"
section: "snippets"
category: "css-dark-mode-toggle"
category_name: "CSS Dark Mode Toggles"
description: "A fully accessible dark mode switch with role=switch, aria-checked, keyboard navigation, and a live ARIA debugger panel that shows every attribute update in…"
has_js: "true"
---

Here's a working CSS Dark Mode Toggle from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible ARIA Toggle with Native Focus & ARIA States
Source: https://codefronts.com/snippets/css-dark-mode-toggle/accessible-aria-toggle-with-native-focus-aria-states/

A fully accessible dark mode switch with role=switch, aria-checked, keyboard navigation, and a live ARIA debugger panel that shows every attribute update in real time.
## HTML
```html
<div class="dm-09" id="dm-09-root">
  <!-- The accessible toggle -->
  <div class="dm-09__toggle-zone">
    <button
      class="dm-09__switch"
      id="dm-09-switch"
      role="switch"
      aria-checked="false"
      aria-label="Dark mode"
      tabindex="0"
    >
      <div class="dm-09__switch-knob">
        <span class="dm-09__switch-icon dm-09__switch-icon--light">☀️</span>
        <span class="dm-09__switch-icon dm-09__switch-icon--dark">🌙</span>
      </div>
    </button>
    <div class="dm-09__kb-hint">
      Press
      <span class="dm-09__key" id="dm-09-tab-key">Tab</span>
      to focus,
      <span class="dm-09__key" id="dm-09-space-key">Space</span>
      to toggle
    </div>
  </div>
  <!-- ARIA debugger panel -->
  <div class="dm-09__debugger">
    <div class="dm-09__debug-topbar">
      <span class="dm-09__debug-title">
        <span class="dm-09__debug-led"></span>
        Accessibility Debugger
      </span>
      <span class="dm-09__debug-badge">LIVE</span>
    </div>
    <div class="dm-09__debug-body">
      <div class="dm-09__attr-row" id="dm-09-row-role">
        <span class="dm-09__attr-key">role</span>
        <span class="dm-09__attr-val" id="dm-09-val-role">"switch"</span>
        <span class="dm-09__attr-status ok"></span>
      </div>
      <div class="dm-09__attr-row" id="dm-09-row-checked">
        <span class="dm-09__attr-key">aria-checked</span>
        <span class="dm-09__attr-val" id="dm-09-val-checked">"false"</span>
        <span class="dm-09__attr-status ok"></span>
      </div>
      <div class="dm-09__attr-row" id="dm-09-row-label">
        <span class="dm-09__attr-key">aria-label</span>
        <span class="dm-09__attr-val">"Dark mode"</span>
        <span class="dm-09__attr-status ok"></span>
      </div>
      <div class="dm-09__attr-row" id="dm-09-row-focus">
        <span class="dm-09__attr-key">:focus-visible</span>
        <span class="dm-09__attr-val" id="dm-09-val-focus">false</span>
        <span class="dm-09__attr-status warn" id="dm-09-status-focus"></span>
      </div>
      <div class="dm-09__attr-row" id="dm-09-row-kb">
        <span class="dm-09__attr-key">keyboard event</span>
        <span class="dm-09__attr-val" id="dm-09-val-kb">—</span>
        <span class="dm-09__attr-status ok"></span>
      </div>
      <div class="dm-09__live-region" aria-live="polite" aria-atomic="true" id="dm-09-live">
        <span class="dm-09__live-icon">📢</span>
        <span id="dm-09-live-text">Waiting for interaction…</span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.dm-09,
.dm-09 *,
.dm-09 *::before,
.dm-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.dm-09 ::selection {
  background: #22c55e;
  color: #000;
}

.dm-09 {
  --bg: #f8fdf9;
  --surface: #ffffff;
  --surface2: #f0fdf4;
  --border: #d1fae5;
  --text: #0f2a1a;
  --muted: #52836a;
  --accent: #16a34a;
  --accent2: #22c55e;
  --warn: #dc2626;
  --debug-bg: #f0fdf4;
  --debug-border: #bbf7d0;
  --debug-text: #15803d;
  --shadow: 0 4px 24px rgba(22,163,74,0.1);
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

.dm-09.is-dark {
  --bg: #020d06;
  --surface: #081a0e;
  --surface2: #0d2414;
  --border: #14422a;
  --text: #c8f0d8;
  --muted: #3a6a4e;
  --accent: #22c55e;
  --accent2: #4ade80;
  --debug-bg: #061208;
  --debug-border: #0f3018;
  --debug-text: #22c55e;
  --shadow: 0 4px 30px rgba(34,197,94,0.15);
}
/* ── Main toggle ── */

.dm-09__toggle-zone {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}
/* Custom focus-visible ring via CSS var */

.dm-09__switch {
  --focus-width: 3px;
  width: 80px;
  height: 44px;
  border-radius: 22px;
  border: 2px solid var(--border);
  cursor: pointer;
  background: var(--surface2);
  position: relative;
  display: flex;
  align-items: center;
  padding: 3px;
  transition: background 0.4s ease,border-color 0.4s ease,box-shadow 0.3s ease;
  outline: none;
}

.dm-09__switch:focus-visible {
  box-shadow: 0 0 0 var(--focus-width) var(--accent), 0 0 0 calc(var(--focus-width) + 2px) rgba(34,197,94,0.2);
}

.dm-09__switch[aria-checked="true"] {
  background: linear-gradient(135deg,#15803d,#22c55e);
  border-color: transparent;
  box-shadow: 0 3px 12px rgba(22,163,74,0.35);
}

.dm-09__switch-knob {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 2px 6px rgba(0,0,0,0.18);
  position: absolute;
  left: 3px;
  transition: transform 0.4s cubic-bezier(0.34,1.56,0.64,1),box-shadow 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
}

.dm-09__switch[aria-checked="true"] .dm-09__switch-knob {
  transform: translateX(36px);
  box-shadow: 0 2px 10px rgba(0,0,0,0.25);
}

.dm-09__switch-icon {
  transition: opacity 0.3s ease,transform 0.3s ease;
  position: absolute;
}

.dm-09__switch-icon--light {
  opacity: 1;
  transform: scale(1);
}

.dm-09__switch-icon--dark {
  opacity: 0;
  transform: scale(0.4);
}

.dm-09__switch[aria-checked="true"] .dm-09__switch-icon--light {
  opacity: 0;
  transform: scale(0.4);
}

.dm-09__switch[aria-checked="true"] .dm-09__switch-icon--dark {
  opacity: 1;
  transform: scale(1);
}
/* Keyboard hint pill */

.dm-09__kb-hint {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.7rem;
  color: var(--muted);
  transition: color 0.4s ease;
}

.dm-09__key {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 28px;
  height: 22px;
  padding: 0 6px;
  border-radius: 5px;
  border: 1.5px solid var(--border);
  background: var(--surface);
  font-size: 0.65rem;
  font-weight: 700;
  font-family: monospace;
  color: var(--text);
  box-shadow: 0 2px 0 var(--border);
  transition: all 0.4s ease;
}

.dm-09__key.pressed {
  transform: translateY(2px);
  box-shadow: none;
  background: var(--accent2);
  border-color: var(--accent);
  color: #fff;
}
/* ── ARIA Debugger panel ── */

.dm-09__debugger {
  width: min(480px,100%);
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: background 0.4s ease,border-color 0.4s ease,box-shadow 0.4s ease;
}

.dm-09__debug-topbar {
  background: var(--accent);
  padding: 10px 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.dm-09__debug-title {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #fff;
  display: flex;
  align-items: center;
  gap: 7px;
}

.dm-09__debug-led {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #4ade80;
  animation: dm-09-blink 1.5s ease-in-out infinite;
}

@keyframes dm-09-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0.2;
  }
}

.dm-09__debug-badge {
  font-size: 0.62rem;
  font-weight: 700;
  background: rgba(255,255,255,0.2);
  padding: 2px 8px;
  border-radius: 4px;
  color: #fff;
}

.dm-09__debug-body {
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
/* Attribute rows */

.dm-09__attr-row {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 14px;
  border-radius: 10px;
  background: var(--debug-bg);
  border: 1px solid var(--debug-border);
  transition: background 0.4s ease,border-color 0.4s ease;
}

.dm-09__attr-key {
  font-family: monospace;
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--debug-text);
  min-width: 130px;
  transition: color 0.4s ease;
}

.dm-09__attr-val {
  font-family: monospace;
  font-size: 0.78rem;
  color: var(--text);
  font-weight: 600;
  flex: 1;
  transition: color 0.4s ease;
}

.dm-09__attr-status {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
  transition: background 0.3s ease;
}

.dm-09__attr-status.ok {
  background: #22c55e;
}

.dm-09__attr-status.warn {
  background: #f59e0b;
}

.dm-09__attr-status.err {
  background: #ef4444;
}
/* Live region */

.dm-09__live-region {
  padding: 10px 14px;
  border-radius: 10px;
  background: var(--debug-bg);
  border: 1px solid var(--debug-border);
  font-size: 0.75rem;
  color: var(--debug-text);
  min-height: 36px;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: background 0.4s ease,border-color 0.4s ease,color 0.4s ease;
}

.dm-09__live-icon {
  font-size: 14px;
  flex-shrink: 0;
}
/* Flash animation for updates */

.dm-09__attr-row.flash {
  animation: dm-09-flash 0.4s ease-out;
}

@keyframes dm-09-flash {
  0% {
    background: rgba(34,197,94,0.25);
  }

  100% {
    background: var(--debug-bg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .dm-09,
    .dm-09 * {
    transition: none!important;
    animation: none!important;
  }
}
```

## JavaScript
```js
(()=>{
  const root=document.getElementById('dm-09-root');
  const sw=document.getElementById('dm-09-switch');
  const valChecked=document.getElementById('dm-09-val-checked');
  const valFocus=document.getElementById('dm-09-val-focus');
  const statusFocus=document.getElementById('dm-09-status-focus');
  const valKb=document.getElementById('dm-09-val-kb');
  const liveText=document.getElementById('dm-09-live-text');
  const rowChecked=document.getElementById('dm-09-row-checked');
  const rowFocus=document.getElementById('dm-09-row-focus');
  const tabKey=document.getElementById('dm-09-tab-key');
  const spaceKey=document.getElementById('dm-09-space-key');
  function flash(el){
    el.classList.remove('flash');
    void el.offsetWidth;
    el.classList.add('flash');
  }
  function toggle(){
    const on=sw.getAttribute('aria-checked')==='true';
    sw.setAttribute('aria-checked',!on);
    root.classList.toggle('is-dark',!on);
    valChecked.textContent='"'+ (!on)+'"';
    liveText.textContent='Dark mode '+ (!on?'enabled':'disabled');
    flash(rowChecked);
  }
  sw.addEventListener('click',toggle);
  sw.addEventListener('keydown',(e)=>{
    if(e.key===' '||e.key==='Enter'){
      e.preventDefault();
      valKb.textContent=`"${e.key}" keydown → toggle`;
      if(e.key===' ')spaceKey.classList.add('pressed');
      flash(document.getElementById('dm-09-row-kb'));
      toggle();
      setTimeout(()=>spaceKey.classList.remove('pressed'),200);
    }
  });
  sw.addEventListener('focus',()=>{
    valFocus.textContent='true';
    statusFocus.className='dm-09__attr-status ok';
    flash(rowFocus);
    tabKey.classList.add('pressed');
  });
  sw.addEventListener('blur',()=>{
    valFocus.textContent='false';
    statusFocus.className='dm-09__attr-status warn';
    tabKey.classList.remove('pressed');
  });
})();
```
