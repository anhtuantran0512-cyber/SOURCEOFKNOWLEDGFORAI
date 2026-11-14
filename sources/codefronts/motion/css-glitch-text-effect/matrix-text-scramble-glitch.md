---
source: "codefronts"
url: "https://codefronts.com/motion/css-glitch-text-effect/matrix-text-scramble-glitch/"
title: "Matrix Text Scramble Glitch"
section: "motion"
category: "css-glitch-text-effect"
category_name: "CSS Glitch Text Effects"
description: "Bright-green monospaced terminal that cycles rapidly through random binary and symbol characters before locking onto the decrypted target word -- driven by a…"
has_js: "true"
---

Here's a working CSS Glitch Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Matrix Text Scramble Glitch
Source: https://codefronts.com/motion/css-glitch-text-effect/matrix-text-scramble-glitch/

Bright-green monospaced terminal that cycles rapidly through random binary and symbol characters before locking onto the decrypted target word -- driven by a JS scrambler with an animated Matrix rain backdrop.
## HTML
```html
<div class="gt-04">
  <div class="gt-04__rain" id="gt-04-rain"></div>
  <div class="gt-04__terminal">
    <span class="gt-04__prompt">root@matrix:~$ decrypt --payload</span>
    <div>
      <span class="gt-04__target" id="gt-04-text">INITIALIZING</span><span class="gt-04__cursor"></span>
    </div>
    <span class="gt-04__status" id="gt-04-status">[ SCANNING... ]</span>
    <button class="gt-04__btn" id="gt-04-btn">⟳ RE-RUN</button>
  </div>
</div>
```
## CSS
```css
.gt-04,
.gt-04 *,
.gt-04 *::before,
.gt-04 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-04 ::selection {
  background: #00ff00;
  color: #000;
}

.gt-04 {
  --matrix-green: #00ff41;
  --dim-green: #003b00;
  --mid-green: #00aa29;
  --bg: #010d01;
  min-height: 100vh;
  background: var(--bg);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 48px 20px;
  font-family: 'Courier New', 'Fira Code', monospace;
  position: relative;
  overflow: hidden;
}
/* Ambient rain columns in background */

.gt-04__rain {
  position: absolute;
  inset: 0;
  overflow: hidden;
  pointer-events: none;
  z-index: 0;
}

.gt-04__rain-col {
  position: absolute;
  top: -100%;
  font-size: 12px;
  color: var(--dim-green);
  line-height: 1.4;
  white-space: pre;
  animation: gt-04-rain-fall linear infinite;
  opacity: 0.4;
}

@keyframes gt-04-rain-fall {
  from {
    transform: translateY(0);
  }

  to {
    transform: translateY(200%);
  }
}

.gt-04__terminal {
  position: relative;
  z-index: 2;
  background: rgba(0,10,0,0.8);
  border: 1px solid var(--dim-green);
  border-radius: 6px;
  padding: 24px 36px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  box-shadow: 0 0 30px rgba(0,255,65,0.08);
}

.gt-04__prompt {
  font-size: 11px;
  color: var(--mid-green);
  letter-spacing: 1px;
}
/* The scramble text */

.gt-04__target {
  font-size: clamp(28px, 5vw, 52px);
  font-weight: 700;
  color: var(--matrix-green);
  letter-spacing: 4px;
  text-shadow: 0 0 10px var(--matrix-green), 0 0 30px rgba(0,255,65,0.4);
  min-height: 1.2em;
  position: relative;
}

.gt-04__cursor {
  display: inline-block;
  width: 3px;
  height: 0.85em;
  background: var(--matrix-green);
  margin-left: 3px;
  vertical-align: middle;
  animation: gt-04-blink 0.7s steps(1) infinite;
}

@keyframes gt-04-blink {
  0%,
    49% {
    opacity: 1;
  }

  50%,
    100% {
    opacity: 0;
  }
}

.gt-04__status {
  font-size: 11px;
  color: var(--mid-green);
  opacity: 0.6;
  letter-spacing: 2px;
}
/* Replay button */

.gt-04__btn {
  margin-top: 8px;
  align-self: flex-start;
  background: none;
  border: 1px solid var(--dim-green);
  color: var(--mid-green);
  font-family: inherit;
  font-size: 11px;
  letter-spacing: 3px;
  padding: 6px 16px;
  cursor: pointer;
  transition: border-color 0.2s, color 0.2s, box-shadow 0.2s;
  border-radius: 2px;
}

.gt-04__btn:hover {
  border-color: var(--matrix-green);
  color: var(--matrix-green);
  box-shadow: 0 0 10px rgba(0,255,65,0.2);
}

@media (prefers-reduced-motion: reduce) {
  .gt-04__rain-col {
    animation: none;
  }

  .gt-04__cursor {
    animation: none;
    opacity: 1;
  }
}
```

## JavaScript
```js
(function() {
  const CHARS = '01$#[]{}|<>ABCDEFabcdef∅∑∆πΩ';
  const WORDS = ['DECRYPTED', 'BREACH OK', 'ACCESS: ROOT', 'MATRIX v4.1', 'SYSTEM FREE'];
  let wordIdx = 0;

  /* Rain columns */
  const rain = document.getElementById('gt-04-rain');
  if (rain) {
    const cols = Math.floor(window.innerWidth / 20);
    for (let i = 0; i < Math.min(cols, 30); i++) {
      const col = document.createElement('div');
      col.className = 'gt-04__rain-col';
      col.style.left = (i * 100 / Math.min(cols, 30)) + '%';
      col.style.animationDuration = (6 + Math.random() * 10) + 's';
      col.style.animationDelay = (-Math.random() * 10) + 's';
      col.style.opacity = (0.1 + Math.random() * 0.35).toString();
      let str = '';
      for (let j = 0; j < 30; j++) str += (Math.random() < 0.5 ? '1' : '0') + '\n';
      col.textContent = str;
      rain.appendChild(col);
    }
  }

  function scramble(el, target, statusEl) {
    const len = target.length;
    let iter = 0;
    const total = len * 5;
    statusEl.textContent = '[ DECRYPTING... ]';
    const iv = setInterval(() => {
      let out = '';
      for (let i = 0; i < len; i++) {
        if (iter / 5 > i) {
          out += target[i];
        } else {
          out += CHARS[Math.floor(Math.random() * CHARS.length)];
        }
      }
      el.textContent = out;
      if (iter >= total) {
        clearInterval(iv);
        el.textContent = target;
        statusEl.textContent = '[ DECRYPTION COMPLETE ]';
      }
      iter++;
    }, 40);
  }

  const textEl = document.getElementById('gt-04-text');
  const statusEl = document.getElementById('gt-04-status');
  const btn = document.getElementById('gt-04-btn');

  function run() {
    const word = WORDS[wordIdx % WORDS.length];
    wordIdx++;
    if (textEl && statusEl) scramble(textEl, word, statusEl);
  }

  if (btn) btn.addEventListener('click', run);
  setTimeout(run, 600);
})();
```
