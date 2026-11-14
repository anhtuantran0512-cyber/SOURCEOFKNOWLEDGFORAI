---
source: "codefronts"
url: "https://codefronts.com/motion/css-typewriter-effect/css-typewriter-glitch-on-type/"
title: "CSS Typewriter Glitch on Type"
section: "motion"
category: "css-typewriter-effect"
category_name: "CSS Typewriter Effect Designs"
description: "Each character causes a brief glitch distortion on the preceding text as it lands — RGB channel splitting and clip-path slice distortion fire per-keystroke…"
has_js: "true"
---

Here's a working CSS Typewriter Effect Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typewriter Glitch on Type
Source: https://codefronts.com/motion/css-typewriter-effect/css-typewriter-glitch-on-type/

Each character causes a brief glitch distortion on the preceding text as it lands — RGB channel splitting and clip-path slice distortion fire per-keystroke via JS class toggling.
## HTML
```html
<div class="tw-12">
  <div class="tw-12__stage">
    <div class="tw-12__chip">SYSTEM BREACH</div>
    <div class="tw-12__wrap">
      <div class="tw-12__text" id="tw-12-text" data-text=""></div>
    </div>
    <div class="tw-12__controls">
      <button id="tw-12-restart" class="tw-12__btn">↺ REINITIALISE</button>
    </div>
  </div>
</div>
```
## CSS
```css
.tw-12,
.tw-12 *,
.tw-12 *::before,
.tw-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tw-12 ::selection {
  background: #ef4444;
  color: #1a0000;
}

.tw-12 {
  --red: #ef4444;
  --cyan: #22d3ee;
  --bg: #0a0000;
  --text: #f8fafc;
  font-family: 'Courier New', monospace;
  min-height: 340px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.tw-12__stage {
  width: 100%;
  max-width: 500px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.tw-12__chip {
  font-size: 0.68rem;
  letter-spacing: 0.25em;
  color: var(--red);
  border: 1px solid rgba(239,68,68,0.3);
  display: inline-block;
  padding: 4px 10px;
  border-radius: 3px;
}

.tw-12__wrap {
  position: relative;
  overflow: hidden;
  min-height: 3.5rem;
}

.tw-12__text {
  font-size: clamp(1.4rem, 4.5vw, 2.2rem);
  font-weight: 700;
  color: var(--text);
  line-height: 1.3;
  position: relative;
  white-space: pre-wrap;
  word-break: break-word;
}

.tw-12__text::before,
.tw-12__text::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  overflow: hidden;
  opacity: 0;
  pointer-events: none;
}

.tw-12__text.glitching::before {
  opacity: 0.8;
  color: var(--red);
  transform: translateX(-4px);
  clip-path: inset(var(--ct, 20%) 0 var(--cb, 60%) 0);
}

.tw-12__text.glitching::after {
  opacity: 0.8;
  color: var(--cyan);
  transform: translateX(4px);
  clip-path: inset(var(--ct2, 50%) 0 var(--cb2, 30%) 0);
}

.tw-12__controls {
  display: flex;
  gap: 12px;
}

.tw-12__btn {
  background: transparent;
  border: 1px solid rgba(239,68,68,0.3);
  color: var(--red);
  font-family: inherit;
  font-size: 0.75rem;
  letter-spacing: 0.12em;
  padding: 7px 16px;
  cursor: pointer;
  border-radius: 4px;
  transition: border-color 0.2s;
}

.tw-12__btn:hover {
  border-color: var(--red);
}

@media (prefers-reduced-motion: reduce) {
  .tw-12__text.glitching::before,
    .tw-12__text.glitching::after {
    opacity: 0;
  }
}
```

## JavaScript
```js
(function() {
  const el = document.getElementById('tw-12-text');
  const btn = document.getElementById('tw-12-restart');
  if (!el) return;

  const LINES = [
    'Firewall bypassed.',
    'Injecting payload...',
    'Root access obtained.'
  ];

  let timer = null;
  let lineIdx = 0;
  let charIdx = 0;

  function glitch() {
    const t1 = Math.random() * 40;
    const t2 = t1 + 10 + Math.random() * 20;
    el.style.setProperty('--ct', t1 + '%');
    el.style.setProperty('--cb', (100 - t2) + '%');
    el.style.setProperty('--ct2', (t1 + 30) % 80 + '%');
    el.style.setProperty('--cb2', (100 - t2 - 10) + '%');
    el.classList.add('glitching');
    setTimeout(() => el.classList.remove('glitching'), 80);
  }

  function typeNext() {
    const line = LINES[lineIdx];
    if (charIdx <= line.length) {
      const current = line.slice(0, charIdx);
      el.textContent = current;
      el.dataset.text = current;
      if (charIdx > 0) glitch();
      charIdx++;
      timer = setTimeout(typeNext, 70 + Math.random() * 40);
    } else {
      timer = setTimeout(() => {
        lineIdx = (lineIdx + 1) % LINES.length;
        charIdx = 0;
        timer = setTimeout(typeNext, 300);
      }, 1800);
    }
  }

  function restart() {
    clearTimeout(timer);
    el.textContent = '';
    el.dataset.text = '';
    el.classList.remove('glitching');
    lineIdx = 0; charIdx = 0;
    timer = setTimeout(typeNext, 400);
  }

  btn.addEventListener('click', restart);
  restart();
})();
```
