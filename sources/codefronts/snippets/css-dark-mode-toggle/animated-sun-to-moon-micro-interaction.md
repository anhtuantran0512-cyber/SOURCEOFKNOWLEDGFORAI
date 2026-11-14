---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dark-mode-toggle/animated-sun-to-moon-micro-interaction/"
title: "Animated Sun-to-Moon Micro-Interaction"
section: "snippets"
category: "css-dark-mode-toggle"
category_name: "CSS Dark Mode Toggles"
description: "A sky panorama where a sun morphs into a crescent moon — rays collapse via CSS transforms, a moon rises with spring easing, craters fade in, and stars…"
has_js: "true"
---

Here's a working CSS Dark Mode Toggle from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Sun-to-Moon Micro-Interaction
Source: https://codefronts.com/snippets/css-dark-mode-toggle/animated-sun-to-moon-micro-interaction/

A sky panorama where a sun morphs into a crescent moon — rays collapse via CSS transforms, a moon rises with spring easing, craters fade in, and stars twinkle into view. Zero images, zero SVG files.
## HTML
```html
<div class="dm-02" id="dm-02-root">
  <div class="dm-02__sky">
    <div class="dm-02__stars">
      <div class="dm-02__star-dot"></div>
      <div class="dm-02__star-dot"></div>
      <div class="dm-02__star-dot"></div>
      <div class="dm-02__star-dot"></div>
      <div class="dm-02__star-dot"></div>
      <div class="dm-02__star-dot"></div>
    </div>
    <div class="dm-02__cloud dm-02__cloud--1"></div>
    <div class="dm-02__cloud dm-02__cloud--2"></div>
    <div class="dm-02__body-wrap">
      <div class="dm-02__sun">
        <div class="dm-02__ray"></div><div class="dm-02__ray"></div>
        <div class="dm-02__ray"></div><div class="dm-02__ray"></div>
        <div class="dm-02__ray"></div><div class="dm-02__ray"></div>
        <div class="dm-02__ray"></div><div class="dm-02__ray"></div>
      </div>
      <div class="dm-02__moon">
        <div class="dm-02__crater"></div>
        <div class="dm-02__crater"></div>
        <div class="dm-02__crater"></div>
      </div>
    </div>
    <div class="dm-02__horizon"></div>
  </div>
  <button class="dm-02__btn" id="dm-02-btn" aria-label="Toggle day/night" aria-pressed="false">
    <span class="dm-02__btn-icon dm-02__btn-icon--sun">☀️</span>
    <span class="dm-02__btn-icon dm-02__btn-icon--moon">🌙</span>
  </button>
  <div class="dm-02__panel">
    <span class="dm-02__panel-eyebrow">◈ Micro-interaction</span>
    <h2 class="dm-02__panel-title">Sun morphs into Moon</h2>
    <p class="dm-02__panel-body">Rays collapse via <code>height + transform</code>. A moon rises with <code>translateY</code> spring easing. The crescent shape is a pure CSS <code>box-shadow: inset</code> overlay — zero images, zero SVG files.</p>
  </div>
</div>
```
## CSS
```css
.dm-02,
.dm-02 *,
.dm-02 *::before,
.dm-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.dm-02 ::selection {
  background: #fbbf24;
  color: #111;
}

.dm-02 {
  --dur: 0.7s;
  --bg: #fffbf0;
  --sky-from: #bae6fd;
  --sky-to: #fde68a;
  --text: #1c1400;
  --muted: #78716c;
  --surface: #ffffff;
  --border: #fde68a;
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
  transition: background var(--dur) ease,color var(--dur) ease;
}

.dm-02.is-dark {
  --bg: #050918;
  --sky-from: #0a0a2e;
  --sky-to: #1a1060;
  --text: #e0e8ff;
  --muted: #7a80a8;
  --surface: #0e0d28;
  --border: #2a2660;
}
/* Sky panorama */

.dm-02__sky {
  width: min(480px,100%);
  height: 180px;
  border-radius: 24px;
  background: linear-gradient(to bottom,var(--sky-from),var(--sky-to));
  position: relative;
  overflow: hidden;
  border: 1.5px solid var(--border);
  transition: background var(--dur) ease,border-color var(--dur) ease;
  box-shadow: 0 8px 40px rgba(0,0,0,0.08);
}

.dm-02.is-dark .dm-02__sky {
  box-shadow: 0 8px 40px rgba(157,100,255,0.15);
}
/* Horizon line */

.dm-02__horizon {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 50px;
  background: linear-gradient(to top,#86efac,#bbf7d0);
  border-radius: 0 0 22px 22px;
  transition: background var(--dur) ease;
}

.dm-02.is-dark .dm-02__horizon {
  background: linear-gradient(to top,#1a2a3a,#0e1a2a);
}
/* Clouds */

.dm-02__cloud {
  position: absolute;
  background: #fff;
  border-radius: 40px;
  opacity: 0.85;
  transition: opacity var(--dur) ease,transform var(--dur) ease;
}

.dm-02__cloud--1 {
  width: 80px;
  height: 28px;
  top: 30px;
  left: 40px;
}

.dm-02__cloud--1::before {
  content: '';
  position: absolute;
  width: 50px;
  height: 50px;
  background: #fff;
  border-radius: 50%;
  top: -20px;
  left: 10px;
}

.dm-02__cloud--1::after {
  content: '';
  position: absolute;
  width: 35px;
  height: 35px;
  background: #fff;
  border-radius: 50%;
  top: -12px;
  left: 35px;
}

.dm-02__cloud--2 {
  width: 60px;
  height: 20px;
  top: 50px;
  right: 60px;
  opacity: 0.6;
}

.dm-02__cloud--2::before {
  content: '';
  position: absolute;
  width: 36px;
  height: 36px;
  background: #fff;
  border-radius: 50%;
  top: -14px;
  left: 8px;
}

.dm-02.is-dark .dm-02__cloud {
  opacity: 0;
  transform: translateX(-20px);
}
/* Stars field */

.dm-02__stars {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.dm-02__star-dot {
  position: absolute;
  border-radius: 50%;
  background: #c8d8ff;
  opacity: 0;
  transform: scale(0);
  transition: opacity var(--dur) ease,transform var(--dur) ease;
  animation: dm-02-twinkle 2s ease-in-out infinite;
}

.dm-02.is-dark .dm-02__star-dot {
  opacity: 1;
  transform: scale(1);
}

.dm-02__star-dot:nth-child(1) {
  width: 3px;
  height: 3px;
  top: 15%;
  left: 10%;
  animation-delay: 0s;
}

.dm-02__star-dot:nth-child(2) {
  width: 2px;
  height: 2px;
  top: 25%;
  left: 25%;
  animation-delay: 0.3s;
}

.dm-02__star-dot:nth-child(3) {
  width: 4px;
  height: 4px;
  top: 10%;
  left: 50%;
  animation-delay: 0.6s;
}

.dm-02__star-dot:nth-child(4) {
  width: 2px;
  height: 2px;
  top: 30%;
  left: 70%;
  animation-delay: 0.9s;
}

.dm-02__star-dot:nth-child(5) {
  width: 3px;
  height: 3px;
  top: 18%;
  left: 85%;
  animation-delay: 0.2s;
}

.dm-02__star-dot:nth-child(6) {
  width: 2px;
  height: 2px;
  top: 40%;
  left: 60%;
  animation-delay: 1.1s;
}

@keyframes dm-02-twinkle {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0.3;
  }
}
/* The main celestial body */

.dm-02__body-wrap {
  position: absolute;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 80px;
}

.dm-02__sun {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%,#fef08a,#f59e0b,#d97706);
  box-shadow: 0 0 0 8px rgba(251,191,36,0.2),0 0 60px rgba(245,158,11,0.6),0 0 100px rgba(245,158,11,0.2);
  position: absolute;
  transition: transform var(--dur) cubic-bezier(0.34,1.56,0.64,1),opacity var(--dur) ease,box-shadow var(--dur) ease;
}

.dm-02.is-dark .dm-02__sun {
  transform: translateY(-120px) scale(0.6);
  opacity: 0;
}
/* Sun rays */

.dm-02__ray {
  position: absolute;
  width: 4px;
  background: linear-gradient(to top,#fde68a,transparent);
  border-radius: 2px;
  top: 50%;
  left: 50%;
  margin-left: -2px;
  transform-origin: 2px 0;
  transition: transform var(--dur) cubic-bezier(0.34,1.56,0.64,1),opacity var(--dur) ease,height var(--dur) ease;
}

.dm-02__ray:nth-child(1) {
  height: 22px;
  transform: translateY(-52px) rotate(0deg);
}

.dm-02__ray:nth-child(2) {
  height: 18px;
  transform: translateY(-50px) rotate(45deg);
}

.dm-02__ray:nth-child(3) {
  height: 22px;
  transform: translateY(-52px) rotate(90deg);
}

.dm-02__ray:nth-child(4) {
  height: 18px;
  transform: translateY(-50px) rotate(135deg);
}

.dm-02__ray:nth-child(5) {
  height: 22px;
  transform: translateY(-52px) rotate(180deg);
}

.dm-02__ray:nth-child(6) {
  height: 18px;
  transform: translateY(-50px) rotate(225deg);
}

.dm-02__ray:nth-child(7) {
  height: 22px;
  transform: translateY(-52px) rotate(270deg);
}

.dm-02__ray:nth-child(8) {
  height: 18px;
  transform: translateY(-50px) rotate(315deg);
}

.dm-02.is-dark .dm-02__ray {
  opacity: 0;
  height: 4px;
}
/* Moon */

.dm-02__moon {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  background: radial-gradient(circle at 40% 40%,#e0d9ff,#c4b5ff,#a78bfa);
  box-shadow: 0 0 0 6px rgba(167,139,250,0.15),0 0 40px rgba(167,139,250,0.4),inset -14px -8px 0 4px rgba(80,60,180,0.35);
  position: absolute;
  top: 5px;
  left: 5px;
  transform: translateY(100px) scale(0.5);
  opacity: 0;
  transition: transform var(--dur) cubic-bezier(0.34,1.56,0.64,1),opacity var(--dur) ease,box-shadow var(--dur) ease;
}

.dm-02.is-dark .dm-02__moon {
  transform: translateY(0) scale(1);
  opacity: 1;
}
/* Moon craters */

.dm-02__crater {
  position: absolute;
  border-radius: 50%;
  background: rgba(60,40,140,0.3);
  transition: opacity var(--dur) ease;
  opacity: 0;
}

.dm-02.is-dark .dm-02__crater {
  opacity: 1;
}

.dm-02__crater:nth-child(1) {
  width: 16px;
  height: 16px;
  top: 18%;
  left: 20%;
}

.dm-02__crater:nth-child(2) {
  width: 10px;
  height: 10px;
  top: 52%;
  left: 18%;
  background: rgba(60,40,140,0.2);
}

.dm-02__crater:nth-child(3) {
  width: 12px;
  height: 12px;
  top: 36%;
  left: 58%;
}
/* Button */

.dm-02__btn {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  border: none;
  cursor: pointer;
  background: linear-gradient(135deg,#fde68a,#f59e0b);
  box-shadow: 0 4px 20px rgba(245,158,11,0.4),0 0 0 4px rgba(251,191,36,0.15);
  font-size: 28px;
  line-height: 1;
  transition: background var(--dur) ease,box-shadow var(--dur) ease,transform 0.2s ease;
  position: relative;
  overflow: hidden;
}

.dm-02__btn:hover {
  transform: scale(1.08);
}

.dm-02__btn:active {
  transform: scale(0.95);
}

.dm-02.is-dark .dm-02__btn {
  background: linear-gradient(135deg,#a78bfa,#7c3aed);
  box-shadow: 0 4px 20px rgba(124,58,237,0.5),0 0 0 4px rgba(167,139,250,0.2);
}

.dm-02__btn-icon {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity var(--dur) ease,transform var(--dur) ease;
}

.dm-02__btn-icon--sun {
  opacity: 1;
  transform: scale(1);
}

.dm-02__btn-icon--moon {
  opacity: 0;
  transform: scale(0.3) rotate(-90deg);
}

.dm-02.is-dark .dm-02__btn-icon--sun {
  opacity: 0;
  transform: scale(0.3) rotate(90deg);
}

.dm-02.is-dark .dm-02__btn-icon--moon {
  opacity: 1;
  transform: scale(1) rotate(0deg);
}
/* Info panel */

.dm-02__panel {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 20px;
  padding: 28px 28px;
  width: min(480px,100%);
  transition: background var(--dur) ease,border-color var(--dur) ease;
  box-shadow: 0 4px 24px rgba(0,0,0,0.06);
}

.dm-02.is-dark .dm-02__panel {
  box-shadow: 0 4px 24px rgba(100,60,255,0.1);
}

.dm-02__panel-eyebrow {
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #f59e0b;
  margin-bottom: 8px;
  display: block;
  transition: color var(--dur) ease;
}

.dm-02.is-dark .dm-02__panel-eyebrow {
  color: #a78bfa;
}

.dm-02__panel-title {
  font-size: 1.25rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: var(--text);
  margin-bottom: 8px;
  transition: color var(--dur) ease;
}

.dm-02__panel-body {
  font-size: 0.85rem;
  line-height: 1.65;
  color: var(--muted);
  transition: color var(--dur) ease;
}

.dm-02__panel-body code {
  font-family: monospace;
  font-size: 0.82em;
  background: rgba(245,158,11,0.1);
  color: #d97706;
  padding: 1px 5px;
  border-radius: 4px;
  transition: background var(--dur) ease,color var(--dur) ease;
}

.dm-02.is-dark .dm-02__panel-body code {
  background: rgba(167,139,250,0.12);
  color: #a78bfa;
}

@media (prefers-reduced-motion: reduce) {
  .dm-02,
    .dm-02 * {
    transition: none!important;
    animation: none!important;
  }
}
```

## JavaScript
```js
const root=document.getElementById('dm-02-root');
const btn=document.getElementById('dm-02-btn');
btn.addEventListener('click',()=>{
  const dark=root.classList.toggle('is-dark');
  btn.setAttribute('aria-pressed',dark);
});
```
