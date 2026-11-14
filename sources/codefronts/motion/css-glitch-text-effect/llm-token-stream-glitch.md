---
source: "codefronts"
url: "https://codefronts.com/motion/css-glitch-text-effect/llm-token-stream-glitch/"
title: "LLM Token Stream Glitch"
section: "motion"
category: "css-glitch-text-effect"
category_name: "CSS Glitch Text Effects"
description: "A 2027-era AI chat surface that streams tokens character-by-character like ChatGPT or Claude, then mid-stream the model hallucinates — a wrong token appears,…"
has_js: "true"
---

Here's a working CSS Glitch Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: LLM Token Stream Glitch
Source: https://codefronts.com/motion/css-glitch-text-effect/llm-token-stream-glitch/

A 2027-era AI chat surface that streams tokens character-by-character like ChatGPT or Claude, then mid-stream the model hallucinates — a wrong token appears, gets struck through with a red line, gets replaced, the cursor flickers, and the stream continues. Loops infinitely through a pool of sample completions.
## HTML
```html
<div class="gt-15">
  <div class="gt-15__chrome">
    <div class="gt-15__badge">
      <span class="gt-15__dot"></span>
      <span class="gt-15__model">claude-5-opus · streaming</span>
    </div>
  </div>
  <div class="gt-15__output" id="gt-15-out"></div>
  <div class="gt-15__footer">
    <span class="gt-15__chip" id="gt-15-ttft">TTFT 142ms</span>
    <span class="gt-15__chip" id="gt-15-rate">1,247 tok/s</span>
    <span class="gt-15__chip">ctx 200k</span>
    <span class="gt-15__chip gt-15__chip--accent">★ thinking model</span>
  </div>
</div>
```
## CSS
```css
.gt-15,
.gt-15 *,
.gt-15 *::before,
.gt-15 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-15 ::selection {
  background: rgba(124,108,255,0.4);
  color: #fff;
}

.gt-15 {
  --bg: #0a0a14;
  --surface: #12121f;
  --border: rgba(255,255,255,0.06);
  --text: #e8e6f5;
  --muted: #8c8aae;
  --accent: #00ffaa;
  --warn: #f59e0b;
  --error: #ef4444;
  --cursor: #00ffaa;
  font-family: 'JetBrains Mono', 'SF Mono', 'Menlo', ui-monospace, monospace;
  background: radial-gradient(ellipse at top, #1a1a2e 0%, var(--bg) 60%);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
  color: var(--text);
}

.gt-15__chrome {
  width: 100%;
  max-width: 720px;
  display: flex;
  justify-content: flex-start;
  margin-bottom: 16px;
}

.gt-15__badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 6px 12px 6px 8px;
  border-radius: 100px;
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.02em;
  color: var(--muted);
}

.gt-15__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 12px var(--accent);
  animation: gt-15-pulse 2s ease-in-out infinite;
}

.gt-15__model {
  color: var(--text);
}

@keyframes gt-15-pulse {
  0%,
    100% {
    opacity: 1;
    box-shadow: 0 0 12px var(--accent);
  }

  50% {
    opacity: 0.5;
    box-shadow: 0 0 4px var(--accent);
  }
}

.gt-15__output {
  width: 100%;
  max-width: 720px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 28px 32px;
  min-height: 180px;
  font-size: clamp(15px, 1.6vw, 19px);
  line-height: 1.65;
  color: var(--text);
  position: relative;
  overflow: hidden;
}
/* Per-character span — slides in from below */

.gt-15__char {
  display: inline-block;
  opacity: 0;
  transform: translateY(4px);
  animation: gt-15-char-in 80ms cubic-bezier(.34,1.4,.64,1) forwards;
  white-space: pre;
}

@keyframes gt-15-char-in {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
/* Wrong token — gets struck through and replaced */

.gt-15__wrong {
  position: relative;
  display: inline-block;
  color: var(--warn);
  white-space: pre;
}

.gt-15__wrong::after {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  width: 0;
  height: 2px;
  background: var(--error);
  box-shadow: 0 0 6px var(--error);
  animation: gt-15-strike 280ms cubic-bezier(.65,0,.35,1) forwards;
  animation-delay: 200ms;
}

@keyframes gt-15-strike {
  to {
    width: 100%;
  }
}

.gt-15__wrong.is-removing {
  animation: gt-15-fade-collapse 200ms ease forwards;
}

@keyframes gt-15-fade-collapse {
  to {
    opacity: 0;
    max-width: 0;
  }
}
/* Cursor */

.gt-15__cursor {
  display: inline-block;
  width: 8px;
  height: 1.1em;
  background: var(--cursor);
  vertical-align: text-bottom;
  margin-left: 1px;
  animation: gt-15-blink 0.6s steps(2) infinite;
  box-shadow: 0 0 8px var(--cursor);
}

@keyframes gt-15-blink {
  50% {
    opacity: 0;
  }
}

.gt-15__cursor.is-flickering {
  animation: gt-15-flicker 120ms steps(1) 3;
}

@keyframes gt-15-flicker {
  0%,
    100% {
    opacity: 1;
    background: var(--cursor);
  }

  50% {
    opacity: 0;
    background: var(--warn);
  }
}
/* Thinking state */

.gt-15__thinking {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: var(--muted);
  font-style: italic;
}

.gt-15__spinner {
  width: 14px;
  height: 14px;
  animation: gt-15-spin 1s linear infinite;
}

@keyframes gt-15-spin {
  to {
    transform: rotate(360deg);
  }
}

.gt-15__dots {
  display: inline-block;
  min-width: 18px;
  text-align: left;
}

.gt-15__dots::after {
  content: '...';
  animation: gt-15-dots 1.2s steps(4) infinite;
}

@keyframes gt-15-dots {
  0% {
    content: '';
  }

  25% {
    content: '.';
  }

  50% {
    content: '..';
  }

  75% {
    content: '...';
  }

  100% {
    content: '';
  }
}

.gt-15__footer {
  width: 100%;
  max-width: 720px;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 14px;
}

.gt-15__chip {
  background: rgba(255,255,255,0.04);
  border: 1px solid var(--border);
  padding: 4px 10px;
  border-radius: 100px;
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 0.04em;
  color: var(--muted);
}

.gt-15__chip--accent {
  background: rgba(0,255,170,0.08);
  border-color: rgba(0,255,170,0.2);
  color: var(--accent);
}

@media (prefers-reduced-motion: reduce) {
  .gt-15__dot,
    .gt-15__cursor,
    .gt-15__spinner,
    .gt-15__dots::after {
    animation: none;
  }

  .gt-15__char {
    animation: none;
    opacity: 1;
    transform: none;
  }

  .gt-15__wrong::after {
    animation: none;
    width: 100%;
  }
}
```

## JavaScript
```js
(function() {
  const out = document.getElementById('gt-15-out');
  const ttft = document.getElementById('gt-15-ttft');
  const rate = document.getElementById('gt-15-rate');
  if (!out) return;

  /* Sentences with hallucination markers: `{ pos: char index, wrong: 'text', right: 'text' }` */
  const samples = [
    {
      text: "The capital of Australia is _Sydney_ Canberra, founded in 1913.",
      corrections: [{ wrong: 'Sydney', right: 'Canberra' }]
    },
    {
      text: "GPT-5 was released in _2024_ 2025 with 10x the inference speed.",
      corrections: [{ wrong: '2024', right: '2025' }]
    },
    {
      text: "Transformers were introduced in the _2018_ 2017 paper Attention Is All You Need.",
      corrections: [{ wrong: '2018', right: '2017' }]
    },
    {
      text: "The model has _128k_ 200k token context with full attention.",
      corrections: [{ wrong: '128k', right: '200k' }]
    },
  ];

  let sampleIdx = 0;
  let charIdx = 0;
  let current = null;
  let interval = null;

  function clear() {
    out.innerHTML = '';
    charIdx = 0;
    current = samples[sampleIdx];
  }

  function appendCursor() {
    const c = document.createElement('span');
    c.className = 'gt-15__cursor';
    out.appendChild(c);
    return c;
  }

  function removeCursor() {
    const c = out.querySelector('.gt-15__cursor');
    if (c) c.remove();
  }

  function appendChar(ch) {
    removeCursor();
    const span = document.createElement('span');
    span.className = 'gt-15__char';
    span.textContent = ch;
    out.appendChild(span);
    appendCursor();
  }

  function flickerCursor() {
    const c = out.querySelector('.gt-15__cursor');
    if (!c) return;
    c.classList.add('is-flickering');
    setTimeout(() => c.classList.remove('is-flickering'), 360);
  }

  function injectWrongToken(text) {
    return new Promise(resolve => {
      removeCursor();
      const span = document.createElement('span');
      span.className = 'gt-15__char gt-15__wrong';
      span.textContent = text;
      out.appendChild(span);
      appendCursor();
      // After strikethrough completes (200ms delay + 280ms anim), pause, replace
      setTimeout(() => {
        flickerCursor();
        setTimeout(() => {
          span.classList.add('is-removing');
          setTimeout(() => { span.remove(); resolve(); }, 200);
        }, 200);
      }, 480);
    });
  }

  async function streamSample() {
    clear();
    /* Parse the text: anything between two underscores is a wrong token to inject + correct.
       e.g. "Sydney _wrong_ correct" → stream chars up to the marker, inject wrong, replace with correct. */
    const parts = current.text.split(/_([^_]+)_ /);
    for (let i = 0; i < parts.length; i++) {
      if (i % 2 === 0) {
        // Plain text — stream char by char
        for (const ch of parts[i]) {
          appendChar(ch);
          await wait(30 + Math.random() * 20);
        }
      } else {
        // Wrong token — inject + strikethrough + replace with NEXT plain part
        await injectWrongToken(parts[i]);
        // The NEXT iteration's even-index part is the replacement — stream its first word fast then continue normally
      }
    }
    await wait(2200);
    sampleIdx = (sampleIdx + 1) % samples.length;
    showThinking();
  }

  function showThinking() {
    out.innerHTML = `<span class="gt-15__thinking"><svg class="gt-15__spinner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M21 12a9 9 0 1 1-6.219-8.56"/></svg>Thinking<span class="gt-15__dots"></span></span>`;
    setTimeout(() => {
      streamSample();
      ttft.textContent = 'TTFT ' + (120 + Math.floor(Math.random() * 60)) + 'ms';
      rate.textContent = (1100 + Math.floor(Math.random() * 400)).toLocaleString() + ' tok/s';
    }, 900);
  }

  function wait(ms) { return new Promise(r => setTimeout(r, ms)); }

  current = samples[0];
  streamSample();
})();
```
