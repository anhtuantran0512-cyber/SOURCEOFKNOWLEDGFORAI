---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-typewriter-loop-gradient-text-animation/"
title: "CSS Typewriter Loop Gradient Text Animation"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "A typewriter loop cycles through a curated list of words letter by letter, each rendered in a continuously scrolling gradient, with a blinking cursor and…"
has_js: "true"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typewriter Loop Gradient Text Animation
Source: https://codefronts.com/design-styles/css-gradient-text/css-typewriter-loop-gradient-text-animation/

A typewriter loop cycles through a curated list of words letter by letter, each rendered in a continuously scrolling gradient, with a blinking cursor and word chip indicators.
## HTML
```html
<div class="gt-18">
  <span class="gt-18__label">Typewriter gradient loop</span>
  <p class="gt-18__prefix">We design &nbsp;&nbsp;→</p>
  <div class="gt-18__stage">
    <span class="gt-18__typed" id="gt-18-typed">WEBSITES</span><span class="gt-18__cursor" aria-hidden="true">|</span>
  </div>
  <div class="gt-18__words-display" id="gt-18-chips"></div>
</div>
```
## CSS
```css
.gt-18,
.gt-18 *,
.gt-18 *::before,
.gt-18 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-18 {
  --bg: #0a0e18;
  font-family: 'JetBrains Mono', monospace;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3rem;
  padding: 3rem 2rem;
}

.gt-18__label {
  font-size: .65rem;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: #1a2a4a;
}

.gt-18__prefix {
  font-size: clamp(1rem, 3vw, 1.5rem);
  font-weight: 700;
  color: #3a5a8a;
  letter-spacing: .05em;
}

.gt-18__stage {
  display: flex;
  align-items: baseline;
  gap: .5rem;
  flex-wrap: wrap;
  justify-content: center;
}

.gt-18__typed {
  font-size: clamp(3rem, 11vw, 7rem);
  font-weight: 800;
  line-height: 1;
  background: linear-gradient(90deg, #4facfe 0%, #00f2fe 50%, #a855f7 100%);
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-18-gradshift 3s linear infinite;
  min-width: 2ch;
  display: inline-block;
}

.gt-18__cursor {
  font-size: clamp(3rem, 11vw, 7rem);
  font-weight: 800;
  line-height: 1;
  color: #4facfe;
  animation: gt-18-blink .8s step-end infinite;
  display: inline-block;
  margin-left: 2px;
}

.gt-18__words-display {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem 1.5rem;
  justify-content: center;
}

.gt-18__word-chip {
  font-size: .7rem;
  letter-spacing: .1em;
  padding: .3em .7em;
  border-radius: 4px;
  border: 1px solid #1a3060;
  color: #3a5a8a;
  transition: border-color .3s, color .3s;
}

.gt-18__word-chip.is-active {
  border-color: #4facfe;
  color: #4facfe;
  background: #4facfe10;
}

@keyframes gt-18-gradshift {
  0% {
    background-position: 0% center;
  }

  100% {
    background-position: 200% center;
  }
}

@keyframes gt-18-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-18__typed {
    animation: none;
    background-position: 0% center;
  }

  .gt-18__cursor {
    animation: none;
  }
}
```

## JavaScript
```js
(function() {
  const words = ['WEBSITES', 'PRODUCTS', 'SYSTEMS', 'BRANDS', 'FUTURES', 'MOTION'];
  const typed = document.getElementById('gt-18-typed');
  const chipsEl = document.getElementById('gt-18-chips');
  if (!typed) return;
  // Build chips
  words.forEach((w, i) => {
    const chip = document.createElement('span');
    chip.className = 'gt-18__word-chip' + (i === 0 ? ' is-active' : '');
    chip.textContent = w;
    chip.id = 'gt-18-chip-' + i;
    chipsEl.appendChild(chip);
  });
  let cur = 0;
  function setActive(idx) {
    document.querySelectorAll('.gt-18 .gt-18__word-chip').forEach((c,i) => {
      c.classList.toggle('is-active', i === idx);
    });
  }
  async function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }
  async function typeWord(word) {
    for (let i = 1; i <= word.length; i++) {
      typed.textContent = word.slice(0, i);
      await sleep(80);
    }
    await sleep(1400);
    for (let i = word.length; i > 0; i--) {
      typed.textContent = word.slice(0, i - 1);
      await sleep(50);
    }
  }
  async function loop() {
    while (true) {
      setActive(cur);
      await typeWord(words[cur]);
      cur = (cur + 1) % words.length;
    }
  }
  loop();
})();
```
