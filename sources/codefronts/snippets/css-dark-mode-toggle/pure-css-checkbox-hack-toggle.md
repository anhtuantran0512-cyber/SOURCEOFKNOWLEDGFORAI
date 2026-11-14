---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dark-mode-toggle/pure-css-checkbox-hack-toggle/"
title: "Pure CSS Checkbox Hack Toggle"
section: "snippets"
category: "css-dark-mode-toggle"
category_name: "CSS Dark Mode Toggles"
description: "A zero-JavaScript theme switcher driven by a hidden input:checked state propagated upward through the DOM via CSS :has() — no event listeners, no hydration…"
has_js: "false"
---

Here's a working CSS Dark Mode Toggle from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Checkbox Hack Toggle
Source: https://codefronts.com/snippets/css-dark-mode-toggle/pure-css-checkbox-hack-toggle/

A zero-JavaScript theme switcher driven by a hidden input:checked state propagated upward through the DOM via CSS :has() — no event listeners, no hydration cost.
## HTML
```html
<div class="dm-01">
  <input type="checkbox" id="dm-01-toggle">
  <div class="dm-01__wrap">
    <div class="dm-01__card">
      <div class="dm-01__header">
        <div class="dm-01__logo">
          <div class="dm-01__logo-mark">◈</div>
          <span class="dm-01__logo-name">codefronts</span>
        </div>
        <label class="dm-01__toggle-label" for="dm-01-toggle" aria-label="Toggle dark mode">
          <div class="dm-01__track">
            <div class="dm-01__knob">
              <span class="dm-01__knob-icon dm-01__knob-icon--sun">☀</span>
              <span class="dm-01__knob-icon dm-01__knob-icon--moon">☽</span>
            </div>
          </div>
        </label>
      </div>
      <div class="dm-01__tag">✦ Zero JavaScript</div>
      <h2 class="dm-01__title">Pure CSS<br><em>Checkbox Hack</em></h2>
      <p class="dm-01__body">A hidden <code>input:checked</code> state propagated upward via <code>:has()</code>. The entire page theme shifts by rewriting CSS custom properties — zero script, zero event listeners, zero hydration cost.</p>
      <div class="dm-01__grid">
        <div class="dm-01__stat"><span class="dm-01__stat-n">0</span><span class="dm-01__stat-l">JS bytes</span></div>
        <div class="dm-01__stat"><span class="dm-01__stat-n">:has</span><span class="dm-01__stat-l">CSS magic</span></div>
        <div class="dm-01__stat"><span class="dm-01__stat-n">∞</span><span class="dm-01__stat-l">perf score</span></div>
      </div>
    </div>
    <div class="dm-01__pills">
      <span class="dm-01__pill">:has() selector</span>
      <span class="dm-01__pill">:checked state</span>
      <span class="dm-01__pill">CSS custom props</span>
      <span class="dm-01__pill">No JavaScript</span>
      <span class="dm-01__pill">SSR safe</span>
    </div>
  </div>
</div>
```
## CSS
```css
.dm-01,
.dm-01 *,
.dm-01 *::before,
.dm-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.dm-01 ::selection {
  background: #7c6af7;
  color: #fff;
}

.dm-01 {
  --dur: 0.55s;
  --ease: cubic-bezier(0.34,1.56,0.64,1);
  --bg: #f4f1ff;
  --surface: #ffffff;
  --surface2: #f8f6ff;
  --border: #e0daff;
  --text: #1a1530;
  --muted: #8b85a8;
  --accent: #7c6af7;
  --accent2: #e91e8c;
  --glow: rgba(124,106,247,0.25);
  --card-shadow: 0 2px 0 #e0daff,0 8px 32px rgba(124,106,247,0.08),0 1px 3px rgba(0,0,0,0.06);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  transition: background var(--dur) ease,color var(--dur) ease;
  color: var(--text);
}

#dm-01-toggle {
  display: none;
}

.dm-01:has(#dm-01-toggle:checked) {
  --bg: #08061a;
  --surface: #0f0c24;
  --surface2: #13102c;
  --border: #2a244a;
  --text: #e8e3ff;
  --muted: #6e6a92;
  --accent: #9d8eff;
  --accent2: #ff6eb4;
  --glow: rgba(157,142,255,0.3);
  --card-shadow: 0 2px 0 #2a244a,0 8px 40px rgba(157,142,255,0.15),0 1px 3px rgba(0,0,0,0.5);
}

.dm-01__wrap {
  width: min(520px,100%);
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.dm-01__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 28px;
  padding: 40px 36px;
  box-shadow: var(--card-shadow);
  transition: background var(--dur) ease,border-color var(--dur) ease,box-shadow var(--dur) ease;
  position: relative;
  overflow: hidden;
}

.dm-01__card::before {
  content: '';
  position: absolute;
  top: -80px;
  right: -80px;
  width: 220px;
  height: 220px;
  border-radius: 50%;
  background: radial-gradient(circle,var(--glow),transparent 70%);
  transition: background var(--dur) ease;
  pointer-events: none;
}

.dm-01__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 36px;
}

.dm-01__logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.dm-01__logo-mark {
  width: 32px;
  height: 32px;
  border-radius: 10px;
  background: linear-gradient(135deg,var(--accent),var(--accent2));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
  box-shadow: 0 2px 8px var(--glow);
  transition: background var(--dur) ease,box-shadow var(--dur) ease;
}

.dm-01__logo-name {
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--text);
  transition: color var(--dur) ease;
  letter-spacing: -0.01em;
}
/* The actual toggle */

.dm-01__toggle-label {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  user-select: none;
}

.dm-01__track {
  width: 64px;
  height: 34px;
  border-radius: 17px;
  background: var(--surface2);
  border: 1.5px solid var(--border);
  position: relative;
  transition: background var(--dur) ease,border-color var(--dur) ease,box-shadow var(--dur) ease;
}

.dm-01:has(#dm-01-toggle:checked) .dm-01__track {
  background: linear-gradient(135deg,var(--accent),var(--accent2));
  border-color: transparent;
  box-shadow: 0 0 16px var(--glow),0 2px 8px rgba(0,0,0,0.3);
}

.dm-01__knob {
  position: absolute;
  top: 4px;
  left: 4px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 2px 6px rgba(0,0,0,0.2);
  transition: transform var(--dur) var(--ease),box-shadow var(--dur) ease;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
}

.dm-01:has(#dm-01-toggle:checked) .dm-01__knob {
  transform: translateX(30px);
  box-shadow: 0 2px 10px rgba(0,0,0,0.4);
}

.dm-01__knob-icon {
  transition: opacity var(--dur) ease,transform var(--dur) ease;
  position: absolute;
  line-height: 1;
}

.dm-01__knob-icon--sun {
  opacity: 1;
  transform: scale(1) rotate(0deg);
}

.dm-01__knob-icon--moon {
  opacity: 0;
  transform: scale(0.4) rotate(-90deg);
}

.dm-01:has(#dm-01-toggle:checked) .dm-01__knob-icon--sun {
  opacity: 0;
  transform: scale(0.4) rotate(90deg);
}

.dm-01:has(#dm-01-toggle:checked) .dm-01__knob-icon--moon {
  opacity: 1;
  transform: scale(1) rotate(0deg);
}

.dm-01__tag {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 3px 10px;
  border-radius: 99px;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  background: linear-gradient(135deg,var(--accent),var(--accent2));
  color: #fff;
  margin-bottom: 14px;
  box-shadow: 0 2px 8px var(--glow);
}

.dm-01__title {
  font-size: clamp(1.6rem,4vw,2.2rem);
  font-weight: 900;
  letter-spacing: -0.04em;
  color: var(--text);
  transition: color var(--dur) ease;
  line-height: 1.1;
  margin-bottom: 12px;
}

.dm-01__title em {
  font-style: normal;
  background: linear-gradient(90deg,var(--accent),var(--accent2));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.dm-01__body {
  font-size: 0.9rem;
  color: var(--muted);
  line-height: 1.65;
  transition: color var(--dur) ease;
  margin-bottom: 28px;
}

.dm-01__body code {
  font-family: monospace;
  background: var(--surface2);
  padding: 1px 5px;
  border-radius: 4px;
  font-size: 0.85em;
  color: var(--accent);
  border: 1px solid var(--border);
  transition: background var(--dur) ease,color var(--dur) ease,border-color var(--dur) ease;
}

.dm-01__grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 12px;
}

.dm-01__stat {
  background: var(--surface2);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 16px 10px;
  text-align: center;
  transition: background var(--dur) ease,border-color var(--dur) ease;
}

.dm-01__stat-n {
  font-size: 1.4rem;
  font-weight: 900;
  background: linear-gradient(135deg,var(--accent),var(--accent2));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  display: block;
}

.dm-01__stat-l {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
  transition: color var(--dur) ease;
  display: block;
  margin-top: 3px;
}
/* Second mini card */

.dm-01__pills {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.dm-01__pill {
  padding: 6px 14px;
  border-radius: 99px;
  border: 1.5px solid var(--border);
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--muted);
  transition: border-color var(--dur) ease,color var(--dur) ease,background var(--dur) ease;
}

.dm-01:has(#dm-01-toggle:checked) .dm-01__pill {
  border-color: var(--accent);
  color: var(--accent);
  background: rgba(157,142,255,0.08);
}

@media (prefers-reduced-motion: reduce) {
  .dm-01,
    .dm-01 * {
    transition: none!important;
  }
}
```
