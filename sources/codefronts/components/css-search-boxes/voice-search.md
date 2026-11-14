---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/voice-search/"
title: "CSS Search Bar with Voice Input Microphone Button"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "Tap the mic and the field enters a listening state: concentric rings pulse out of the button, a live waveform of CSS bars reacts, and the placeholder changes…"
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Search Bar with Voice Input Microphone Button
Source: https://codefronts.com/components/css-search-boxes/voice-search/

Tap the mic and the field enters a listening state: concentric rings pulse out of the button, a live waveform of CSS bars reacts, and the placeholder changes to a listening prompt. State is one data-state attribute plus aria-pressed — no Web Speech API needed to build or test the UI.
## HTML
```html
<div class="sb-11">
  <button class="sb-11__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-11__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-11__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-11__stage">
    <div class="sb-11__bar" role="search" data-state="idle">
      <svg class="sb-11__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      <label class="sb-11__vh" for="sb-11-input">Search by voice or type your query</label>
      <input class="sb-11__input" id="sb-11-input" type="search" placeholder="Search or hold to speak" autocomplete="off">

      <span class="sb-11__wave" aria-hidden="true">
        <span style="--d:0ms"></span><span style="--d:120ms"></span><span style="--d:60ms"></span><span style="--d:220ms"></span>
        <span style="--d:90ms"></span><span style="--d:180ms"></span><span style="--d:40ms"></span><span style="--d:140ms"></span>
      </span>

      <button class="sb-11__mic" id="sb-11-mic" type="button" aria-pressed="false" aria-label="Search by voice">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="3" width="6" height="11" rx="3" stroke="currentColor" stroke-width="1.8"/><path d="M5.5 11.5a6.5 6.5 0 0 0 13 0M12 18v3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      </button>
      <p class="sb-11__vh" id="sb-11-status" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-11 {
  --bg: #f5f6fa;
  --card: #ffffff;
  --ink: #111827;
  --muted: #6b7280;
  --line: #e5e7eb;
  --acc: #4f46e5;
  --acc-soft: rgba(79,70,229,.14);
  --live: #dc2626;
  --ring: #4f46e5;
  --shadow: rgba(17,24,39,.16);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: radial-gradient(42rem 24rem at 50% 8%, #ffffff, var(--bg) 70%);
  -webkit-font-smoothing: antialiased;
}

.sb-11 *,
.sb-11 *::before,
.sb-11 *::after {
  box-sizing: border-box;
}

.sb-11__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-11__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-11__bar {
  display: flex;
  align-items: center;
  gap: .7rem;
  inline-size: min(31rem,100%);
  min-block-size: 58px;
  padding-inline: 1.1rem .55rem;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: var(--card);
  box-shadow: 0 2px 4px rgba(17,24,39,.04);
  transition: border-color .22s, box-shadow .22s;
}

.sb-11__bar:focus-within {
  border-color: var(--acc);
  box-shadow: 0 0 0 4px var(--acc-soft);
}

.sb-11__bar[data-state="listening"] {
  border-color: var(--live);
  box-shadow: 0 0 0 4px rgba(220,38,38,.12);
}

.sb-11__ico {
  inline-size: 19px;
  block-size: 19px;
  flex: none;
  color: var(--muted);
}

.sb-11__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .97rem/1 inherit;
}

.sb-11__input::placeholder {
  color: var(--muted);
}

.sb-11__input:focus {
  outline: none;
}

.sb-11__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-11__wave {
  display: flex;
  align-items: center;
  gap: 3px;
  block-size: 20px;
  opacity: 0;
  transition: opacity .2s;
}

.sb-11__wave span {
  inline-size: 3px;
  block-size: 100%;
  border-radius: 2px;
  background: var(--live);
  scale: 1 .18;
  transform-origin: center;
}

.sb-11__bar[data-state="listening"] .sb-11__wave {
  opacity: 1;
}

.sb-11__bar[data-state="listening"] .sb-11__wave span {
  animation: sb-11-bar .82s ease-in-out infinite alternate;
  animation-delay: var(--d,0ms);
}

@keyframes sb-11-bar {
  from {
    scale: 1 .18;
  }

  to {
    scale: 1 1;
  }
}

.sb-11__mic {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 46px;
  block-size: 46px;
  flex: none;
  border: 0;
  border-radius: 13px;
  background: var(--acc-soft);
  color: var(--acc);
  cursor: pointer;
  transition: background .2s, color .2s, scale .12s;
}

.sb-11__mic:hover {
  background: color-mix(in srgb, var(--acc) 22%, transparent);
}

.sb-11__mic:active {
  scale: .95;
}

.sb-11__mic:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.sb-11__mic svg {
  inline-size: 20px;
  block-size: 20px;
  position: relative;
  z-index: 2;
}

.sb-11__bar[data-state="listening"] .sb-11__mic {
  background: var(--live);
  color: #fff;
}

.sb-11__mic::before,
.sb-11__mic::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  border: 2px solid var(--live);
  opacity: 0;
  pointer-events: none;
}

.sb-11__bar[data-state="listening"] .sb-11__mic::before,
.sb-11__bar[data-state="listening"] .sb-11__mic::after {
  animation: sb-11-ring 1.8s ease-out infinite;
}

.sb-11__bar[data-state="listening"] .sb-11__mic::after {
  animation-delay: .6s;
}

@keyframes sb-11-ring {
  0% {
    opacity: .55;
    scale: 1;
  }

  100% {
    opacity: 0;
    scale: 2.1;
  }
}

.sb-11[data-theme="dark"] {
  --bg: #0c0f16;
  --card: #141926;
  --ink: #eef1f7;
  --muted: #8b93a5;
  --line: #222a3a;
  --acc: #8b83ff;
  --acc-soft: rgba(139,131,255,.18);
  --live: #ff6b6b;
  --ring: #8b83ff;
  --shadow: rgba(0,0,0,.7);
  background: radial-gradient(42rem 24rem at 50% 8%, #161c2b, var(--bg) 70%);
}

@media (prefers-color-scheme: dark) {
  .sb-11:not([data-theme="light"]) {
    --bg: #0c0f16;
    --card: #141926;
    --ink: #eef1f7;
    --muted: #8b93a5;
    --line: #222a3a;
    --acc: #8b83ff;
    --acc-soft: rgba(139,131,255,.18);
    --live: #ff6b6b;
    --ring: #8b83ff;
    --shadow: rgba(0,0,0,.7);
    background: radial-gradient(42rem 24rem at 50% 8%, #161c2b, var(--bg) 70%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-11 *,
    .sb-11 *::before,
    .sb-11 *::after {
    animation: none !important;
    transition: none !important;
  }

  .sb-11__bar[data-state="listening"] .sb-11__wave span {
    scale: 1 .7;
  }
}

@media (forced-colors: active) {
  .sb-11__bar,
    .sb-11__mic {
    border: 1px solid CanvasText;
  }

  .sb-11__bar[data-state="listening"] .sb-11__mic {
    background: Highlight;
    color: HighlightText;
  }
}

.sb-11__theme {
  position: absolute;
  inset-block-start: clamp(.75rem,2vw,1.25rem);
  inset-inline-end: clamp(.75rem,2vw,1.25rem);
  z-index: 50;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  padding: 0;
  border-radius: 999px;
  border: 1px solid rgba(0,0,0,.12);
  color: currentColor;
  background: rgba(255,255,255,.72);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1), border-color .25s ease;
}

.sb-11[data-theme="dark"] .sb-11__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-11:not([data-theme="light"]) .sb-11__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-11__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-11[data-theme="dark"] .sb-11__theme:hover,
.sb-11:not([data-theme="light"]) .sb-11__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-11__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-11__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-11__sun {
  display: none;
}

.sb-11__theme[aria-pressed="true"] .sb-11__sun {
  display: block;
}

.sb-11__theme[aria-pressed="true"] .sb-11__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-11__theme {
    transition: none;
  }

  .sb-11__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sb-11');
  if (!root) return;
  const bar = root.querySelector('.sb-11__bar');
  const btn = root.querySelector('#sb-11-mic');
  const input = root.querySelector('#sb-11-input');
  const status = root.querySelector('#sb-11-status');

  const setState = (listening) => {
    bar.dataset.state = listening ? 'listening' : 'idle';
    btn.setAttribute('aria-pressed', String(listening));
    input.placeholder = listening ? 'Listening… speak now' : 'Search or hold to speak';
    status.textContent = listening ? 'Listening' : 'Voice input stopped';
  };
  btn.addEventListener('click', () => setState(bar.dataset.state !== 'listening'));
  input.addEventListener('keydown', (e) => { if (e.key === 'Escape') setState(false); });
})();
(()=>{const r=document.querySelector('.sb-11');if(!r)return;const t=r.querySelector('.sb-11__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
