---
source: "codefronts"
url: "https://codefronts.com/motion/css-pulse-animation/voice-search-mic-pulse/"
title: "Voice Search Mic Pulse"
section: "motion"
category: "css-pulse-animation"
category_name: "CSS Pulse Animations"
description: "A voice-assistant modal showing an active listening state — microphone icon at the center with expanding concentric rings pulsing outward + a live waveform…"
has_js: "true"
---

Here's a working CSS Pulse Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Voice Search Mic Pulse
Source: https://codefronts.com/motion/css-pulse-animation/voice-search-mic-pulse/

A voice-assistant modal showing an active listening state — microphone icon at the center with expanding concentric rings pulsing outward + a live waveform of vertical bars responding to "voice input." Deep purple gradient background (#4c1d95 to #7c3aed) with white mic icon and glassmorphic modal card. Google Assistant / Alexa / Siri modal aesthetic. The pulse conveys "I'm actively listening, keep speaking."
## HTML
```html
<div class="pl-15">
  <div class="pl-15__modal" role="dialog" aria-modal="true" aria-labelledby="pl-15-title">
    <button class="pl-15__close" aria-label="Cancel voice input">
      <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true">
        <line x1="6" y1="6" x2="18" y2="18"/>
        <line x1="18" y1="6" x2="6" y2="18"/>
      </svg>
    </button>
    <p class="pl-15__eyebrow">Northlight Assistant</p>
    <h2 class="pl-15__title" id="pl-15-title">Listening…</h2>
    <button class="pl-15__mic" aria-label="Stop listening">
      <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>
        <path d="M19 10v2a7 7 0 0 1-14 0v-2"/>
        <line x1="12" y1="19" x2="12" y2="23"/>
        <line x1="8" y1="23" x2="16" y2="23"/>
      </svg>
    </button>
    <div class="pl-15__wave" aria-hidden="true">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
    </div>
    <p class="pl-15__hint">Say something like <em>"What's the weather today?"</em></p>
    <p class="pl-15__status" aria-live="polite">Listening now · release to send</p>
  </div>
</div>
```
## CSS
```css
.pl-15 {
  --brand-a: #4c1d95;
  --brand-b: #7c3aed;
  --brand-glow: rgba(167,139,250,.5);
  --ink: #f5f3ff;
  --sub: #c4b5fd;
  --white: #ffffff;
  font-family: -apple-system,BlinkMacSystemFont,'SF Pro Rounded','Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(60% 100% at 20% 0%, rgba(167,139,250,.3) 0%, transparent 55%), radial-gradient(70% 100% at 100% 100%, rgba(124,58,237,.35) 0%, transparent 55%), linear-gradient(135deg,var(--brand-a) 0%,var(--brand-b) 100%);
  color: var(--ink);
}

.pl-15 *,
.pl-15 *::before,
.pl-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pl-15 ::selection {
  background: var(--white);
  color: var(--brand-a);
}

.pl-15__modal {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: min(420px,100%);
  padding: 36px 28px 28px;
  border-radius: 20px;
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.14);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  box-shadow: 0 30px 80px -20px rgba(76,29,149,.6);
}

.pl-15__close {
  position: absolute;
  top: 14px;
  right: 14px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 34px;
  height: 34px;
  border: none;
  border-radius: 50%;
  background: rgba(255,255,255,.1);
  color: var(--ink);
  cursor: pointer;
  transition: background .15s ease;
}

.pl-15__close:hover {
  background: rgba(255,255,255,.2);
}

.pl-15__close:focus-visible {
  outline: 2px solid var(--white);
  outline-offset: 2px;
}

.pl-15__eyebrow {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--sub);
  margin-bottom: 8px;
}

.pl-15__title {
  font-size: 1.6rem;
  font-weight: 700;
  letter-spacing: -.02em;
  line-height: 1.1;
  margin-bottom: 32px;
}
/* Mic button with concentric outward rings */

.pl-15__mic {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 80px;
  height: 80px;
  border: none;
  border-radius: 50%;
  background: var(--white);
  color: var(--brand-a);
  cursor: pointer;
  box-shadow: 0 10px 30px -8px rgba(255,255,255,.4);
  margin-bottom: 22px;
  z-index: 1;
  transition: transform .15s ease;
}

.pl-15__mic:hover {
  transform: scale(1.03);
}

.pl-15__mic:focus-visible {
  outline: 3px solid var(--white);
  outline-offset: 6px;
}

.pl-15__mic svg {
  position: relative;
  z-index: 1;
}

.pl-15__mic::before,
.pl-15__mic::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: var(--brand-glow);
  pointer-events: none;
  z-index: 0;
  animation: pl-15-ring 1.8s ease-out infinite;
}

.pl-15__mic::after {
  animation-delay: .9s;
}

@keyframes pl-15-ring {
  0% {
    transform: scale(1);
    opacity: .55;
  }

  70% {
    transform: scale(2.3);
    opacity: 0;
  }

  100% {
    transform: scale(2.4);
    opacity: 0;
  }
}
/* Waveform bars — 5 vertical bars with coprime durations */

.pl-15__wave {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  height: 36px;
  margin-bottom: 20px;
}

.pl-15__wave span {
  display: inline-block;
  width: 4px;
  height: 100%;
  border-radius: 2px;
  background: var(--white);
  transform-origin: center;
}

.pl-15__wave span:nth-child(1) {
  animation: pl-15-bar .6s ease-in-out -.2s infinite;
}

.pl-15__wave span:nth-child(2) {
  animation: pl-15-bar .9s ease-in-out -.5s infinite;
}

.pl-15__wave span:nth-child(3) {
  animation: pl-15-bar .7s ease-in-out -.1s infinite;
}

.pl-15__wave span:nth-child(4) {
  animation: pl-15-bar .8s ease-in-out -.4s infinite;
}

.pl-15__wave span:nth-child(5) {
  animation: pl-15-bar .5s ease-in-out 0s infinite;
}

@keyframes pl-15-bar {
  0%,
    100% {
    transform: scaleY(.3);
  }

  50% {
    transform: scaleY(1);
  }
}

.pl-15__hint {
  font-size: .88rem;
  color: var(--sub);
  text-align: center;
  line-height: 1.4;
  margin-bottom: 14px;
}

.pl-15__hint em {
  color: var(--white);
  font-style: normal;
  font-weight: 600;
}

.pl-15__status {
  padding: 8px 14px;
  border-radius: 8px;
  background: rgba(0,0,0,.15);
  color: var(--sub);
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .04em;
}

@media (prefers-reduced-motion: reduce) {
  .pl-15__mic::before,
    .pl-15__mic::after,
    .pl-15__wave span {
    animation: none!important;
    transform: none!important;
  }

  .pl-15__mic::before,
    .pl-15__mic::after {
    opacity: 0!important;
  }

  .pl-15__wave span {
    transform: scaleY(.7)!important;
  }
}
```

## JavaScript
```js
(function(){
  // Demo cycle: pulses through listening → thinking → done states so gallery
  // + preview show meaningful motion. In production, replace with real Web
  // Speech API integration:
  //   const recog = new webkitSpeechRecognition();
  //   recog.continuous = true; recog.onresult = ...
  var root = document.querySelector('.pl-15');
  if (!root) return;
  var title = root.querySelector('#pl-15-title');
  var status = root.querySelector('.pl-15__status');
  if (!title || !status) return;

  var states = [
    { title: 'Listening…',       status: 'Say something now',           delay: 3500 },
    { title: 'Thinking…',        status: 'Processing your request',     delay: 1500 },
    { title: 'Here you go',      status: 'Weather · sunny, 72°F',       delay: 2500 },
  ];
  var i = 0;
  function next(){
    var s = states[i % states.length];
    title.textContent = s.title;
    status.textContent = s.status;
    i++;
    setTimeout(next, s.delay);
  }
  setTimeout(next, 3500);
})();
```
