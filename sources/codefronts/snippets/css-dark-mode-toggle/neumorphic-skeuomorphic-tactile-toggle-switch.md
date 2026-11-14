---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dark-mode-toggle/neumorphic-skeuomorphic-tactile-toggle-switch/"
title: "Neumorphic Skeuomorphic Tactile Toggle Switch"
section: "snippets"
category: "css-dark-mode-toggle"
category_name: "CSS Dark Mode Toggles"
description: "A physically satisfying 3D-molded toggle — extruded in light mode with outset shadows, it literally sinks into the page with inset shadows on press."
has_js: "true"
---

Here's a working CSS Dark Mode Toggle from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Skeuomorphic Tactile Toggle Switch
Source: https://codefronts.com/snippets/css-dark-mode-toggle/neumorphic-skeuomorphic-tactile-toggle-switch/

A physically satisfying 3D-molded toggle — extruded in light mode with outset shadows, it literally sinks into the page with inset shadows on press. Dark mode adds a cyan neon glow radiating from the thumb.
## HTML
```html
<div class="dm-07" id="dm-07-root">
  <div class="dm-07__widget">
    <button class="dm-07__shell" id="dm-07-btn" aria-label="Toggle dark mode" aria-pressed="false">
      <div class="dm-07__track">
        <div class="dm-07__glow-strip"></div>
        <div class="dm-07__thumb">
          <span class="dm-07__thumb-icon dm-07__thumb-icon--sun">☀</span>
          <span class="dm-07__thumb-icon dm-07__thumb-icon--moon">🌙</span>
        </div>
      </div>
    </button>
    <div class="dm-07__label-row">
      <span class="dm-07__label-text" id="dm-07-label">Light Mode</span>
    </div>
    <div class="dm-07__dots">
      <div class="dm-07__dot is-active" data-idx="0"></div>
      <div class="dm-07__dot" data-idx="1"></div>
    </div>
  </div>
  <div class="dm-07__cards">
    <div class="dm-07__card">
      <span class="dm-07__card-icon">🧱</span>
      <div class="dm-07__card-title">Extruded</div>
      <p class="dm-07__card-body">Offset shadows give raised, physical feel — light from top-left, shadow bottom-right.</p>
    </div>
    <div class="dm-07__card">
      <span class="dm-07__card-icon">💠</span>
      <div class="dm-07__card-title">Inset Press</div>
      <p class="dm-07__card-body">Toggling reverses to <code>box-shadow: inset</code> — the button physically sinks in.</p>
    </div>
    <div class="dm-07__card">
      <span class="dm-07__card-icon">⚡</span>
      <div class="dm-07__card-title">Neon Glow</div>
      <p class="dm-07__card-body">Dark active state adds cyan glow radiating from thumb — zero images.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.dm-07,
.dm-07 *,
.dm-07 *::before,
.dm-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.dm-07 ::selection {
  background: #3b82f6;
  color: #fff;
}

.dm-07 {
  --bg: #e8ecf2;
  --surface: #e8ecf2;
  --text: #2d3a4a;
  --muted: #6e7f91;
  --accent: #3b82f6;
  --neon: #06b6d4;
  --light-shadow: #ffffff;
  --dark-shadow: #c2cad6;
  --inner-l: rgba(255,255,255,0.9);
  --inner-d: rgba(163,174,189,0.6);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 40px;
  color: var(--text);
  transition: background 0.6s ease,color 0.6s ease;
}

.dm-07.is-dark {
  --bg: #1a1e2a;
  --surface: #1a1e2a;
  --text: #c8d4e8;
  --muted: #4a5568;
  --accent: #38bdf8;
  --neon: #00e5ff;
  --light-shadow: #22283a;
  --dark-shadow: #12151f;
  --inner-l: rgba(50,58,80,0.8);
  --inner-d: rgba(10,12,18,0.9);
}
/* The main neumorphic toggle */

.dm-07__widget {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 28px;
}
/* Outer extruded shell */

.dm-07__shell {
  width: 180px;
  height: 90px;
  border-radius: 45px;
  background: var(--surface);
  box-shadow: 8px 8px 20px var(--dark-shadow), -8px -8px 20px var(--light-shadow);
  padding: 10px;
  cursor: pointer;
  border: none;
  position: relative;
  transition: background 0.6s ease,box-shadow 0.5s ease;
  display: flex;
  align-items: center;
}
/* OFF state (extruded) */

.dm-07__shell:not(.is-on) {
  box-shadow: 8px 8px 20px var(--dark-shadow), -8px -8px 20px var(--light-shadow);
}
/* ON state (pressed in) */

.dm-07__shell.is-on {
  box-shadow: inset 6px 6px 14px var(--dark-shadow), inset -6px -6px 14px var(--light-shadow);
}
/* Inner track groove */

.dm-07__track {
  width: 100%;
  height: 100%;
  border-radius: 38px;
  background: var(--surface);
  box-shadow: inset 3px 3px 8px var(--dark-shadow), inset -3px -3px 8px var(--light-shadow);
  position: relative;
  overflow: hidden;
  transition: background 0.6s ease,box-shadow 0.5s ease;
}

.dm-07__shell.is-on .dm-07__track {
  background: linear-gradient(135deg,#0c2340,#0a1a3a);
  box-shadow: inset 3px 3px 10px #06101e,inset -3px -3px 10px #142a50;
}
/* Thumb */

.dm-07__thumb {
  position: absolute;
  top: 4px;
  left: 4px;
  width: 62px;
  height: 62px;
  border-radius: 50%;
  background: var(--surface);
  box-shadow: 4px 4px 10px var(--dark-shadow), -4px -4px 10px var(--light-shadow);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 26px;
  transition: transform 0.55s cubic-bezier(0.34,1.56,0.64,1), background 0.6s ease, box-shadow 0.5s ease;
}

.dm-07__shell.is-on .dm-07__thumb {
  transform: translateX(88px);
  background: radial-gradient(circle at 35% 35%,#1e4080,#0a2050);
  box-shadow: 0 0 20px rgba(56,189,248,0.5), 0 0 40px rgba(0,229,255,0.2), 4px 4px 10px #06101e, -4px -4px 10px #1a3060;
}

.dm-07__thumb-icon {
  transition: opacity 0.4s ease,transform 0.4s ease;
  position: absolute;
  line-height: 1;
}

.dm-07__thumb-icon--sun {
  opacity: 1;
  transform: scale(1);
}

.dm-07__thumb-icon--moon {
  opacity: 0;
  transform: scale(0.4);
}

.dm-07__shell.is-on .dm-07__thumb-icon--sun {
  opacity: 0;
  transform: scale(0.4);
}

.dm-07__shell.is-on .dm-07__thumb-icon--moon {
  opacity: 1;
  transform: scale(1);
}
/* Neon glow strip when on */

.dm-07__glow-strip {
  position: absolute;
  inset: 0;
  border-radius: 38px;
  background: linear-gradient(90deg,transparent,rgba(56,189,248,0.1),transparent);
  opacity: 0;
  transition: opacity 0.6s ease;
}

.dm-07__shell.is-on .dm-07__glow-strip {
  opacity: 1;
}
/* Embossed label under toggle */

.dm-07__label-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.dm-07__label-text {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
  text-shadow: 1px 1px 0 var(--light-shadow),-1px -1px 0 var(--dark-shadow);
  transition: color 0.6s ease,text-shadow 0.6s ease;
}

.dm-07.is-dark .dm-07__label-text {
  text-shadow: none;
}
/* The demo info cards around it */

.dm-07__cards {
  display: flex;
  gap: 16px;
  width: min(440px,100%);
}

.dm-07__card {
  flex: 1;
  border-radius: 20px;
  padding: 20px 16px;
  background: var(--surface);
  box-shadow: 5px 5px 14px var(--dark-shadow), -5px -5px 14px var(--light-shadow);
  transition: background 0.6s ease,box-shadow 0.5s ease;
}

.dm-07.is-dark .dm-07__card {
  box-shadow: 5px 5px 14px var(--dark-shadow), -5px -5px 14px var(--light-shadow);
}

.dm-07__card-icon {
  font-size: 22px;
  margin-bottom: 8px;
  display: block;
}

.dm-07__card-title {
  font-size: 0.8rem;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 4px;
  transition: color 0.6s ease;
}

.dm-07__card-body {
  font-size: 0.72rem;
  line-height: 1.55;
  color: var(--muted);
  transition: color 0.6s ease;
}
/* Neon accent text in dark */

.dm-07.is-dark .dm-07__card-title {
  color: var(--accent);
}
/* Active indicator dots */

.dm-07__dots {
  display: flex;
  gap: 6px;
  justify-content: center;
}

.dm-07__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--surface);
  box-shadow: 2px 2px 5px var(--dark-shadow), -2px -2px 5px var(--light-shadow);
  transition: background 0.4s ease,box-shadow 0.4s ease;
}

.dm-07__dot.is-active {
  background: var(--accent);
  box-shadow: 0 0 8px var(--accent),0 0 16px rgba(56,189,248,0.3);
}

@media (prefers-reduced-motion: reduce) {
  .dm-07,
    .dm-07 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
const root=document.getElementById('dm-07-root');
const btn=document.getElementById('dm-07-btn');
const label=document.getElementById('dm-07-label');
const dots=[...document.querySelectorAll('.dm-07__dot')];
btn.addEventListener('click',()=>{
  const on=btn.classList.toggle('is-on');
  root.classList.toggle('is-dark',on);
  btn.setAttribute('aria-pressed',on);
  label.textContent=on?'Dark Mode':'Light Mode';
  dots.forEach((d,i)=>d.classList.toggle('is-active',on?(i===1):(i===0)));
});
```
