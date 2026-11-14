---
source: "codefronts"
url: "https://codefronts.com/motion/css-typewriter-effect/css-typewriter-matrix-scramble-decode/"
title: "CSS Typewriter Matrix Scramble Decode"
section: "motion"
category: "css-typewriter-effect"
category_name: "CSS Typewriter Effect Designs"
description: "Random characters scramble across the target string before each letter snaps to its final value — a hacker-movie decode effect powered by JS with CSS glow…"
has_js: "true"
---

Here's a working CSS Typewriter Effect Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typewriter Matrix Scramble Decode
Source: https://codefronts.com/motion/css-typewriter-effect/css-typewriter-matrix-scramble-decode/

Random characters scramble across the target string before each letter snaps to its final value — a hacker-movie decode effect powered by JS with CSS glow styling.
## HTML
```html
<div class="tw-11">
  <div class="tw-11__screen">
    <div class="tw-11__scan"></div>
    <p class="tw-11__status">DECRYPTING PAYLOAD</p>
    <div class="tw-11__output" id="tw-11-output" aria-label="ACCESS GRANTED" aria-live="off"></div>
    <button class="tw-11__btn" id="tw-11-run">▶ DECODE</button>
  </div>
</div>
```
## CSS
```css
.tw-11,
.tw-11 *,
.tw-11 *::before,
.tw-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tw-11 ::selection {
  background: #00ff41;
  color: #000;
}

.tw-11 {
  --green: #00ff41;
  --dim: #003d10;
  --bg: #020a03;
  font-family: 'Courier New', monospace;
  min-height: 340px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
}

.tw-11__screen {
  width: 100%;
  max-width: 480px;
  border: 1px solid #0a2a0a;
  border-radius: 8px;
  padding: 32px 24px;
  position: relative;
  overflow: hidden;
  background: #030c03;
  box-shadow: 0 0 40px rgba(0,255,65,0.08), inset 0 0 40px rgba(0,0,0,0.5);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 20px;
}

.tw-11__scan {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
      0deg, transparent, transparent 2px, rgba(0,255,65,0.03) 2px, rgba(0,255,65,0.03) 4px
    );
  pointer-events: none;
}

.tw-11__status {
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  color: var(--dim);
}

.tw-11__output {
  font-size: clamp(1.4rem, 4vw, 2rem);
  font-weight: 700;
  color: var(--green);
  text-shadow: 0 0 10px rgba(0,255,65,0.6);
  letter-spacing: 0.08em;
  min-height: 1.4em;
  display: flex;
  flex-wrap: wrap;
  gap: 0;
}

.tw-11__output .tw-11-char {
  display: inline-block;
  color: var(--dim);
  text-shadow: none;
  transition: color 0.1s, text-shadow 0.1s;
}

.tw-11__output .tw-11-char.locked {
  color: var(--green);
  text-shadow: 0 0 12px rgba(0,255,65,0.8);
}

.tw-11__btn {
  background: transparent;
  border: 1px solid var(--dim);
  color: var(--green);
  font-family: inherit;
  font-size: 0.78rem;
  letter-spacing: 0.15em;
  padding: 8px 18px;
  cursor: pointer;
  border-radius: 4px;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.tw-11__btn:hover {
  border-color: var(--green);
  box-shadow: 0 0 12px rgba(0,255,65,0.2);
}

@media (prefers-reduced-motion: reduce) {
  .tw-11__output .tw-11-char {
    transition: none;
  }
}
```

## JavaScript
```js
(function() {
  const container = document.getElementById('tw-11-output');
  const btn = document.getElementById('tw-11-run');
  if (!container) return;

  const TARGET = 'ACCESS GRANTED';
  const NOISE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*<>?/|';
  const SCRAMBLE_FRAMES = 10;
  const CHAR_DELAY = 60;

  let intervals = [];

  function rand(str) {
    return str[Math.floor(Math.random() * str.length)];
  }

  function run() {
    intervals.forEach(clearInterval);
    intervals = [];
    container.innerHTML = '';

    const spans = TARGET.split('').map((ch) => {
      const span = document.createElement('span');
      span.className = 'tw-11-char';
      span.textContent = ch === ' ' ? ' ' : rand(NOISE);
      container.appendChild(span);
      return { span, final: ch };
    });

    spans.forEach(({ span, final }, i) => {
      if (final === ' ') { span.textContent = ' '; return; }
      let frames = 0;
      const startDelay = i * CHAR_DELAY;
      setTimeout(() => {
        const iv = setInterval(() => {
          if (frames >= SCRAMBLE_FRAMES) {
            clearInterval(iv);
            span.textContent = final;
            span.classList.add('locked');
          } else {
            span.textContent = rand(NOISE);
            frames++;
          }
        }, 40);
        intervals.push(iv);
      }, startDelay);
    });
  }

  btn.addEventListener('click', run);
  run();
})();
```
