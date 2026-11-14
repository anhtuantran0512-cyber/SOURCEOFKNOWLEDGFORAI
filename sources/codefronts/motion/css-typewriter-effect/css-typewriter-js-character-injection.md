---
source: "codefronts"
url: "https://codefronts.com/motion/css-typewriter-effect/css-typewriter-js-character-injection/"
title: "CSS Typewriter JS Character Injection"
section: "motion"
category: "css-typewriter-effect"
category_name: "CSS Typewriter Effect Designs"
description: "JavaScript injects characters one by one into the DOM at a configurable speed, enabling proportional fonts, dynamic strings, pause-on-hover, and…"
has_js: "true"
---

Here's a working CSS Typewriter Effect Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typewriter JS Character Injection
Source: https://codefronts.com/motion/css-typewriter-effect/css-typewriter-js-character-injection/

JavaScript injects characters one by one into the DOM at a configurable speed, enabling proportional fonts, dynamic strings, pause-on-hover, and click-to-restart — all styled with CSS.
## HTML
```html
<div class="tw-10">
  <div class="tw-10__card">
    <div class="tw-10__prompt">claude@studio:~$</div>
    <div class="tw-10__output" id="tw-10-output" data-state="typing" aria-live="polite"></div>
    <button class="tw-10__restart" id="tw-10-restart">↺ Restart</button>
  </div>
</div>
```
## CSS
```css
.tw-10,
.tw-10 *,
.tw-10 *::before,
.tw-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tw-10 ::selection {
  background: #7c3aed;
  color: #f5f3ff;
}

.tw-10 {
  --violet: #7c3aed;
  --lavender: #a78bfa;
  --bg: #09050f;
  --card: #120e1f;
  --border: #2a1f45;
  font-family: 'Courier New', monospace;
  min-height: 340px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
}

.tw-10__card {
  width: 100%;
  max-width: 500px;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 32px 28px;
  box-shadow: 0 24px 64px rgba(124,58,237,0.15);
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.tw-10__prompt {
  font-size: 0.8rem;
  color: var(--lavender);
  opacity: 0.6;
}

.tw-10__output {
  font-size: clamp(1.1rem, 3.5vw, 1.5rem);
  color: #f5f3ff;
  min-height: 2.4em;
  line-height: 1.5;
  position: relative;
}

.tw-10__output::after {
  content: '';
  display: inline-block;
  width: 2px;
  height: 1.1em;
  background: var(--lavender);
  vertical-align: middle;
  margin-left: 2px;
  animation: tw-10-blink 0.75s steps(2) infinite;
}

.tw-10__output[data-state="done"]::after {
  background: var(--violet);
  animation-duration: 1.2s;
}

.tw-10__restart {
  align-self: flex-start;
  background: transparent;
  border: 1px solid var(--border);
  color: var(--lavender);
  font-family: inherit;
  font-size: 0.8rem;
  padding: 6px 14px;
  border-radius: 6px;
  cursor: pointer;
  transition: border-color 0.2s, color 0.2s;
}

.tw-10__restart:hover {
  border-color: var(--lavender);
  color: #fff;
}

@keyframes tw-10-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tw-10__output::after {
    animation: none;
    opacity: 1;
  }
}
```

## JavaScript
```js
(function() {
  const el = document.getElementById('tw-10-output');
  const btn = document.getElementById('tw-10-restart');
  if (!el) return;

  const strings = [
    'Designing with intention, building with precision.',
    'Every pixel tells a story.',
    'Code is craft. Make it beautiful.'
  ];
  let strIdx = 0, charIdx = 0, timer = null;

  function getDelay(char) {
    if ('.!?'.includes(char)) return 520;
    if (',;:'.includes(char)) return 240;
    return 55 + Math.random() * 30;
  }

  function type() {
    const str = strings[strIdx];
    if (charIdx < str.length) {
      el.textContent += str[charIdx];
      charIdx++;
      timer = setTimeout(type, getDelay(str[charIdx - 1]));
    } else {
      el.dataset.state = 'done';
      timer = setTimeout(() => {
        erase();
      }, 2200);
    }
  }

  function erase() {
    const str = strings[strIdx];
    if (el.textContent.length > 0) {
      el.textContent = el.textContent.slice(0, -1);
      el.dataset.state = 'typing';
      timer = setTimeout(erase, 28);
    } else {
      strIdx = (strIdx + 1) % strings.length;
      charIdx = 0;
      timer = setTimeout(type, 400);
    }
  }

  function restart() {
    clearTimeout(timer);
    el.textContent = '';
    el.dataset.state = 'typing';
    strIdx = 0; charIdx = 0;
    timer = setTimeout(type, 300);
  }

  btn.addEventListener('click', restart);
  restart();
})();
```
