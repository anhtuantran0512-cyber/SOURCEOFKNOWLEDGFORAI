---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/streaming-response-typing-button/"
title: "Streaming Response Typing Button"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "The modern async shape: a send button whose pending state is a typing indicator rather than a spinner, because the response streams in rather than arriving…"
has_js: "true"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Streaming Response Typing Button
Source: https://codefronts.com/components/css-loading-buttons/streaming-response-typing-button/

The modern async shape: a send button whose pending state is a typing indicator rather than a spinner, because the response streams in rather than arriving all at once. Three dots pulse inside the button while tokens land, an explicit stop control appears beside it so the user can interrupt, and a mid-stream failure leaves the partial text on screen with a retry.
## HTML
```html
<div class="lb-10">
  <div class="lb-10__stage">
    <section class="lb-10__chat" aria-labelledby="lb-10-h">
      <h2 class="lb-10__h" id="lb-10-h">Assistant</h2>

      <div class="lb-10__thread">
        <p class="lb-10__msg lb-10__msg--me">Summarise the migration risks in two sentences.</p>
        <p class="lb-10__msg lb-10__msg--ai" id="lb-10-out">Ask something to start the stream.</p>
      </div>

      <div class="lb-10__composer">
        <span class="lb-10__input" id="lb-10-input">Summarise the migration risks…</span>
        <button class="lb-10__stopbtn" type="button" id="lb-10-stop" hidden>
          <span class="lb-10__square" aria-hidden="true"></span>
          Stop
        </button>
        <button class="lb-10__send" type="button" id="lb-10-btn" data-state="idle" aria-busy="false" aria-label="Send message">
          <span class="lb-10__ic lb-10__ic--send" aria-hidden="true">
            <svg viewBox="0 0 20 20" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 10h11M10.5 5.5 15 10l-4.5 4.5"/></svg>
          </span>
          <span class="lb-10__ic lb-10__ic--dots" aria-hidden="true"><i></i><i></i><i></i></span>
        </button>
      </div>

      <div class="lb-10__foot">
        <label class="lb-10__toggle"><input type="checkbox" id="lb-10-fail"> Drop the stream halfway</label>
        <p class="lb-10__live" id="lb-10-live" role="status" aria-live="polite">Idle.</p>
        <p class="lb-10__alert" id="lb-10-alert" role="alert"></p>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-10 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #000000;
  --surface: #0a0a0c;
  --ink: #f2f0f7;
  --muted: #8d8a99;
  --rule: #1d1d22;
  --accent: #8b5cf6;
  --bad: #ff7a66;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  padding: 40px 16px;
}

.lb-10 *,
.lb-10 *::before,
.lb-10 *::after {
  box-sizing: border-box;
}

.lb-10__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-10__chat {
  inline-size: 100%;
  max-inline-size: 34rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 18px;
  padding: 20px;
}

.lb-10__h {
  margin: 0 0 16px;
  font-size: 12px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 600;
}

.lb-10__thread {
  display: grid;
  gap: 10px;
  margin-block-end: 16px;
}

.lb-10__msg {
  margin: 0;
  font-size: 13.5px;
  line-height: 1.6;
  padding: 12px 14px;
  border-radius: 14px;
  min-inline-size: 0;
}

.lb-10__msg--me {
  background: #17171c;
  color: var(--ink);
  justify-self: end;
  max-inline-size: 90%;
}

.lb-10__msg--ai {
  background: transparent;
  border: 1px solid var(--rule);
  color: var(--muted);
  min-block-size: 76px;
}

.lb-10__composer {
  display: flex;
  gap: 10px;
  align-items: center;
  padding: 8px 8px 8px 16px;
  border: 1px solid var(--rule);
  border-radius: 999px;
  min-inline-size: 0;
}

.lb-10__input {
  flex: 1 1 auto;
  min-inline-size: 0;
  font-size: 13px;
  color: var(--muted);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.lb-10__send {
  appearance: none;
  flex: none;
  inline-size: 44px;
  block-size: 44px;
  border: 0;
  border-radius: 50%;
  background: var(--accent);
  color: #0b0611;
  display: grid;
  place-items: center;
  cursor: pointer;
  transition: box-shadow 260ms ease, background 200ms ease;
}

.lb-10__send:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.lb-10__send[data-state="pending"] {
  box-shadow: 0 0 0 4px rgba(139, 92, 246, .22), 0 0 26px rgba(139, 92, 246, .5);
}

.lb-10__send[data-state="error"] {
  background: var(--bad);
}

.lb-10__ic {
  display: none;
}

.lb-10__send[data-state="idle"] .lb-10__ic--send,
.lb-10__send[data-state="done"] .lb-10__ic--send,
.lb-10__send[data-state="error"] .lb-10__ic--send {
  display: inline-flex;
}

.lb-10__send[data-state="pending"] .lb-10__ic--dots {
  display: inline-flex;
  align-items: center;
  gap: 3px;
}

.lb-10__ic--dots i {
  inline-size: 4px;
  block-size: 4px;
  border-radius: 50%;
  background: currentColor;
  animation: lb-10-bounce 900ms ease-in-out infinite;
}

.lb-10__ic--dots i:nth-child(2) {
  animation-delay: 140ms;
}

.lb-10__ic--dots i:nth-child(3) {
  animation-delay: 280ms;
}

@keyframes lb-10-bounce {
  0%,
    100% {
    transform: translateY(1.5px);
    opacity: .4;
  }

  50% {
    transform: translateY(-1.5px);
    opacity: 1;
  }
}

.lb-10__stopbtn {
  appearance: none;
  flex: none;
  border: 1px solid var(--rule);
  background: transparent;
  color: var(--ink);
  border-radius: 999px;
  font: inherit;
  font-size: 12px;
  font-weight: 560;
  padding: 0 14px;
  min-block-size: 44px;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  cursor: pointer;
}

.lb-10__stopbtn[hidden] {
  display: none;
}

.lb-10__stopbtn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.lb-10__square {
  inline-size: 9px;
  block-size: 9px;
  border-radius: 2px;
  background: currentColor;
  flex: none;
}

.lb-10__msg--ai[data-state="pending"]::after {
  content: "";
  display: inline-flex;
  vertical-align: middle;
  inline-size: 26px;
  block-size: 5px;
  margin-inline-start: 6px;
  background: radial-gradient(circle 2.5px at 3px 50%, currentColor 96%, transparent), radial-gradient(circle 2.5px at 13px 50%, currentColor 96%, transparent), radial-gradient(circle 2.5px at 23px 50%, currentColor 96%, transparent);
  animation: lb-10-fade 900ms ease-in-out infinite;
}

@keyframes lb-10-fade {
  0%,
    100% {
    opacity: .3;
  }

  50% {
    opacity: 1;
  }
}

.lb-10__foot {
  margin: 14px 0 0;
  display: grid;
  gap: 4px;
}

.lb-10__toggle {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  color: var(--muted);
  min-height: 44px;
  min-inline-size: 0;
}

.lb-10__toggle input {
  accent-color: var(--accent);
  inline-size: 15px;
  block-size: 15px;
}

.lb-10__live {
  margin: 0;
  font-size: 12px;
  color: var(--muted);
  min-inline-size: 0;
}

.lb-10__alert {
  margin: 0;
  min-block-size: 17px;
  font-size: 12.5px;
  font-weight: 560;
  color: var(--bad);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .lb-10__msg--ai[data-state="pending"]::after {
    animation: none;
    opacity: .8;
  }

  .lb-10__ic--dots i {
    animation: none;
    opacity: .85;
  }

  .lb-10__send {
    transition: none;
  }
}

@media (prefers-color-scheme: light) {
  .lb-10 {
    --bg: #f5f4f8;
    --surface: #ffffff;
    --ink: #16141c;
    --muted: #6d6a79;
    --rule: #e3e1ea;
    --accent: #6d3ff0;
    --bad: #c4402c;
  }

  .lb-10__msg--me {
    background: #ecebf2;
  }

  .lb-10__send {
    color: #fbf9ff;
  }
}

[data-theme="light"] .lb-10 {
  --bg: #f5f4f8;
  --surface: #ffffff;
  --ink: #16141c;
  --muted: #6d6a79;
  --rule: #e3e1ea;
  --accent: #6d3ff0;
  --bad: #c4402c;
}
```

## JavaScript
```js
const btn = document.getElementById('lb-10-btn');
const out = document.getElementById('lb-10-out');
const live = document.getElementById('lb-10-live');
const alertBox = document.getElementById('lb-10-alert');
const failBox = document.getElementById('lb-10-fail');
const words = 'Two risks stand out: the dual-write window can drop rows if a shard fails mid-copy, and the rollback path has never been exercised under production load.'.split(' ');
let stream;
let i = 0;

const stopBtn = document.getElementById('lb-10-stop');

const finish = (state, name, message) => {
  clearInterval(stream);
  btn.dataset.state = state;
  btn.setAttribute('aria-busy', 'false');
  btn.setAttribute('aria-label', name);
  out.removeAttribute('data-state');
  stopBtn.hidden = true;
  live.textContent = message;
};

stopBtn.addEventListener('click', () => finish('idle', 'Send message', 'Stopped. The partial answer is kept.'));

btn.addEventListener('click', () => {
  if (btn.dataset.state === 'pending') return;
  clearInterval(stream);
  i = 0;
  out.textContent = '';
  out.dataset.state = 'pending';
  alertBox.textContent = '';
  btn.dataset.state = 'pending';
  btn.setAttribute('aria-busy', 'true');
  stopBtn.hidden = false;
  live.textContent = 'Response streaming';
  stream = setInterval(() => {
    if (failBox.checked && i === 12) {
      finish('error', 'Retry message', 'Stream failed.');
      alertBox.textContent = 'Stream dropped after 12 tokens. The partial answer is kept — press retry.';
      return;
    }
    out.textContent += (i ? ' ' : '') + words[i];
    i += 1;
    if (i >= words.length) finish('done', 'Send message', 'Response complete.');
  }, 110);
});
```
