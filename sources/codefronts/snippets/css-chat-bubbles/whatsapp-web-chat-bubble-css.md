---
source: "codefronts"
url: "https://codefronts.com/snippets/css-chat-bubbles/whatsapp-web-chat-bubble-css/"
title: "WhatsApp Web Chat Bubble CSS"
section: "snippets"
category: "css-chat-bubbles"
category_name: "CSS Chat Bubbles"
description: "The message-thread mechanics that make a mobile-messenger layout feel right: a timestamp and tick pair that floats inside the bubble and lets the last line…"
has_js: "true"
---

Here's a working CSS Chat Bubble from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: WhatsApp Web Chat Bubble CSS
Source: https://codefronts.com/snippets/css-chat-bubbles/whatsapp-web-chat-bubble-css/

The message-thread mechanics that make a mobile-messenger layout feel right: a timestamp and tick pair that floats inside the bubble and lets the last line of text wrap around it, tinted outgoing bubbles with clip-path tails, a sticky date divider, a quoted-reply block, and a receipt that walks sent → delivered → read. Send a message and watch all four states run.
## HTML
```html
<div class="cb-08">
  <button class="cb-08__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cb-08__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="cb-08__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>

  <section class="cb-08__app" aria-label="Chat with Tobias Lund">
    <header class="cb-08__bar">
      <img class="cb-08__pic" src="https://images.unsplash.com/photo-1531123897727-8f129e1688ce?auto=format&fit=facearea&facepad=2.8&w=160&h=160&q=70" width="42" height="42" alt="Tobias Lund" loading="lazy" decoding="async">
      <span class="cb-08__ident"><b>Tobias Lund</b><small>online</small></span>
      <span class="cb-08__tools">
        <button type="button" aria-label="Search in conversation"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.2" stroke="currentColor" stroke-width="1.8"/><path d="m15.6 15.6 3.9 3.9" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button>
        <button type="button" aria-label="Conversation menu"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="5.5" r="1.6" fill="currentColor"/><circle cx="12" cy="12" r="1.6" fill="currentColor"/><circle cx="12" cy="18.5" r="1.6" fill="currentColor"/></svg></button>
      </span>
    </header>

    <ol class="cb-08__thread" id="cb-08-thread" aria-label="Messages">
      <li class="cb-08__day"><span>Yesterday</span></li>
      <li class="cb-08__turn cb-08__turn--in">
        <div class="cb-08__msg">
          <span class="cb-08__meta"><time datetime="2027-05-08T19:02">19:02</time></span>
          Bench is booked for Saturday morning. Bring the good coffee.
        </div>
      </li>
      <li class="cb-08__turn cb-08__turn--out">
        <div class="cb-08__msg">
          <span class="cb-08__meta">
            <time datetime="2027-05-08T19:05">19:05</time>
            <span class="cb-08__tick" data-state="read" role="img" aria-label="Read">
              <svg viewBox="0 0 20 14" fill="none" aria-hidden="true" focusable="false"><path class="cb-08__tick-1" d="M1.5 7.6 5 11l6.6-8" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/><path class="cb-08__tick-2" d="M7.6 7.6 11 11l6.6-8" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
          </span>
          Already ground it. 6:30 or is that cruel?
        </div>
      </li>
      <li class="cb-08__day"><span>Today</span></li>
      <li class="cb-08__turn cb-08__turn--in">
        <div class="cb-08__msg">
          <blockquote class="cb-08__quote">
            <b>You</b>
            <span>Already ground it. 6:30 or is that cruel?</span>
          </blockquote>
          <span class="cb-08__meta"><time datetime="2027-05-09T07:44">07:44</time></span>
          It's cruel and I'll be there. Meet by the north gate.
        </div>
      </li>
      <li class="cb-08__turn cb-08__turn--in">
        <div class="cb-08__msg cb-08__msg--jumbo">
          <span class="cb-08__meta"><time datetime="2027-05-09T07:44">07:44</time></span>
          ☕️
        </div>
      </li>
      <li class="cb-08__turn cb-08__turn--out">
        <div class="cb-08__msg">
          <span class="cb-08__meta">
            <time datetime="2027-05-09T07:51">07:51</time>
            <span class="cb-08__tick" data-state="delivered" role="img" aria-label="Delivered">
              <svg viewBox="0 0 20 14" fill="none" aria-hidden="true" focusable="false"><path class="cb-08__tick-1" d="M1.5 7.6 5 11l6.6-8" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/><path class="cb-08__tick-2" d="M7.6 7.6 11 11l6.6-8" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
          </span>
          North gate, 6:30. I'm bringing the flask that keeps things properly hot.
        </div>
      </li>
    </ol>

    <div class="cb-08__composer">
      <button class="cb-08__icon" type="button" aria-label="Add emoji"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.4" stroke="currentColor" stroke-width="1.7"/><circle cx="9.3" cy="10.2" r="1.15" fill="currentColor"/><circle cx="14.7" cy="10.2" r="1.15" fill="currentColor"/><path d="M8.6 14.4a4.2 4.2 0 0 0 6.8 0" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg></button>
      <button class="cb-08__icon" type="button" aria-label="Attach file"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M13.7 6.6 7.4 12.9a3.1 3.1 0 0 0 4.4 4.4l7.1-7.1a4.7 4.7 0 0 0-6.6-6.6L5 11" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg></button>
      <input class="cb-08__input" id="cb-08-input" type="text" placeholder="Type a message" aria-label="Type a message">
      <button class="cb-08__send" id="cb-08-send" type="button" aria-label="Send message" disabled><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 12 20 5l-3.2 14.5-4.6-4.3-3 2.4z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg></button>
    </div>
    <p class="cb-08__sr" id="cb-08-status" role="status" aria-live="polite"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

.cb-08 {
  --bg: #d9dbd5;
  --app: #f0f2f5;
  --ink: #111b21;
  --muted: #667781;
  --line: #e2e5e9;
  --in: #ffffff;
  --in-ink: #111b21;
  --out: #d9fdd3;
  --out-ink: #111b21;
  --acc: #00a884;
  --read: #53bdeb;
  --shadow: rgba(11,20,26,.16);
  --sans: "DM Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(.75rem,3vw,2.5rem);
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cb-08,
.cb-08 *,
.cb-08 *::before,
.cb-08 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .cb-08 {
    --bg: oklch(88% .008 130);
    --app: oklch(95.5% .004 250);
    --ink: oklch(20% .02 220);
    --muted: oklch(53% .02 220);
    --out: oklch(94.5% .06 140);
    --acc: oklch(65% .13 165);
  }
}

.cb-08__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cb-08 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cb-08__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,3vw,1.6rem);
  inset-inline-end: clamp(.9rem,3vw,1.6rem);
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  z-index: 4;
  border-radius: 14px;
  border: 1px solid var(--line);
  background: var(--app);
  color: var(--ink);
  transition: transform .25s cubic-bezier(.16,1,.3,1);
}

.cb-08__theme:hover {
  transform: translateY(-2px);
}

.cb-08__theme svg {
  inline-size: 20px;
  block-size: 20px;
}

.cb-08__sun {
  display: none;
}

.cb-08__app {
  inline-size: min(100%,32rem);
  max-block-size: min(90svh,46rem);
  display: grid;
  grid-template-rows: auto 1fr auto auto;
  overflow: hidden;
  border-radius: 1rem;
  background: var(--app);
  box-shadow: 0 30px 70px -45px var(--shadow);
}

.cb-08__bar {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: .75rem;
  padding: .6rem .8rem;
  background: var(--app);
  border-block-end: 1px solid var(--line);
}

.cb-08__pic {
  inline-size: 42px;
  block-size: 42px;
  border-radius: 50%;
  object-fit: cover;
  background: var(--line);
}

.cb-08__ident {
  display: grid;
  min-inline-size: 0;
}

.cb-08__ident b {
  font-size: .98rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.cb-08__ident small {
  font-size: .74rem;
  color: var(--muted);
}

.cb-08__tools {
  display: flex;
  gap: .15rem;
}

.cb-08__tools button,
.cb-08__icon {
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border: 0;
  border-radius: 50%;
  background: transparent;
  color: var(--muted);
}

.cb-08__tools button svg,
.cb-08__icon svg {
  inline-size: 21px;
  block-size: 21px;
}

.cb-08__tools button:hover,
.cb-08__icon:hover {
  background: color-mix(in oklab,var(--ink) 7%,transparent);
  color: var(--ink);
}
/* ── wallpaper: pure CSS, no image request ── */

.cb-08__thread {
  list-style: none;
  margin: 0;
  padding: .85rem .9rem 1.2rem;
  display: grid;
  gap: .3rem;
  align-content: start;
  overflow-y: auto;
  overflow-x: clip;
  scrollbar-width: thin;
  background-color: #efe7de;
  background-image: radial-gradient(circle at 20% 30%, rgba(0,0,0,.035) 0 2px, transparent 2px), radial-gradient(circle at 70% 60%, rgba(0,0,0,.03) 0 3px, transparent 3px), radial-gradient(circle at 45% 85%, rgba(0,0,0,.028) 0 2px, transparent 2px), linear-gradient(140deg, rgba(255,255,255,.5), transparent 60%);
  background-size: 120px 120px, 190px 190px, 150px 150px, 100% 100%;
}

.cb-08__day {
  position: sticky;
  inset-block-start: 0;
  z-index: 2;
  justify-self: center;
  margin-block: .5rem .7rem;
}

.cb-08__day span {
  display: inline-block;
  padding: .28rem .8rem;
  border-radius: .5rem;
  background: color-mix(in oklab,var(--app) 92%,transparent);
  color: var(--muted);
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .02em;
  text-transform: uppercase;
  box-shadow: 0 1px 2px var(--shadow);
  backdrop-filter: blur(6px);
}

.cb-08__turn {
  display: flex;
}

.cb-08__turn--out {
  justify-content: flex-end;
}

.cb-08__msg {
  position: relative;
  max-inline-size: min(24rem,80%);
  padding: .44rem .6rem .5rem .65rem;
  font-size: .95rem;
  line-height: 1.42;
  letter-spacing: -.005em;
  overflow-wrap: anywhere;
  text-wrap: pretty;
  border-radius: .55rem;
  background: var(--in);
  color: var(--in-ink);
  box-shadow: 0 1px 1px var(--shadow);
  animation: cb-08-in .38s cubic-bezier(.16,1,.3,1) backwards;
}

.cb-08__turn--in .cb-08__msg {
  border-start-start-radius: 0;
}

.cb-08__turn--out .cb-08__msg {
  background: var(--out);
  color: var(--out-ink);
  border-start-end-radius: 0;
}

@keyframes cb-08-in {
  from {
    opacity: 0;
    translate: 0 6px;
  }

  to {
    opacity: 1;
    translate: 0;
  }
}
/* tails via clip-path — they inherit the bubble fill */

.cb-08__turn--in .cb-08__msg::after,
.cb-08__turn--out .cb-08__msg::after {
  content: '';
  position: absolute;
  inset-block-start: 0;
  inline-size: 9px;
  block-size: 14px;
  background: inherit;
}

.cb-08__turn--in .cb-08__msg::after {
  inset-inline-start: -8px;
  clip-path: polygon(100% 0, 0 0, 100% 100%);
}

.cb-08__turn--out .cb-08__msg::after {
  inset-inline-end: -8px;
  clip-path: polygon(0 0, 100% 0, 0 100%);
}
/* the float that lets text wrap around the timestamp */

.cb-08__meta {
  float: inline-end;
  display: inline-flex;
  align-items: center;
  gap: .22rem;
  margin-inline-start: .55rem;
  margin-block-end: -.15rem;
  translate: 0 .4em;
  font-size: .66rem;
  font-weight: 500;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.cb-08__tick {
  display: inline-flex;
  color: var(--muted);
}

.cb-08__tick svg {
  inline-size: 1.05rem;
  block-size: .75rem;
}

.cb-08__tick[data-state="sent"] .cb-08__tick-2 {
  display: none;
}

.cb-08__tick[data-state="read"] {
  color: var(--read);
}

.cb-08__msg--jumbo {
  background: none !important;
  box-shadow: none;
  font-size: 2.4rem;
  line-height: 1.1;
  padding: .1rem .4rem;
}

.cb-08__msg--jumbo::after {
  display: none;
}

.cb-08__msg--jumbo .cb-08__meta {
  font-size: .62rem;
  translate: 0 0;
  margin-block-start: 1.9rem;
}

.cb-08__quote {
  margin: 0 0 .3rem;
  padding: .35rem .55rem;
  border-radius: .35rem;
  display: grid;
  gap: .1rem;
  background: color-mix(in oklab,var(--acc) 12%,transparent);
  border-inline-start: 3px solid var(--acc);
}

.cb-08__quote b {
  font-size: .78rem;
  color: var(--acc);
}

.cb-08__quote span {
  font-size: .82rem;
  color: var(--muted);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.cb-08__composer {
  display: flex;
  align-items: center;
  gap: .3rem;
  padding: .5rem .6rem;
  background: var(--app);
  border-block-start: 1px solid var(--line);
}

.cb-08__input {
  flex: 1;
  min-block-size: 44px;
  padding-inline: .9rem;
  border: 0;
  border-radius: .65rem;
  background: var(--in);
  color: var(--ink);
  font: inherit;
  font-size: .95rem;
  outline: 0;
}

.cb-08__input::placeholder {
  color: var(--muted);
}

.cb-08__send {
  inline-size: 44px;
  block-size: 44px;
  flex: 0 0 auto;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 50%;
  background: var(--acc);
  color: #fff;
  cursor: pointer;
  transition: transform .25s cubic-bezier(.16,1,.3,1), opacity .2s;
}

.cb-08__send svg {
  inline-size: 20px;
  block-size: 20px;
}

.cb-08__send:disabled {
  opacity: .35;
  cursor: not-allowed;
}

.cb-08__send:not(:disabled):hover {
  transform: scale(1.08);
}
/* dark */

.cb-08[data-theme="dark"] {
  --bg: #0b141a;
  --app: #202c33;
  --ink: #e9edef;
  --muted: #8696a0;
  --line: #2a3942;
  --in: #202c33;
  --in-ink: #e9edef;
  --out: #005c4b;
  --out-ink: #e9edef;
  --shadow: rgba(0,0,0,.6);
}

.cb-08[data-theme="dark"] .cb-08__thread {
  background-color: #0c1317;
  background-image: radial-gradient(circle at 20% 30%, rgba(255,255,255,.028) 0 2px, transparent 2px), radial-gradient(circle at 70% 60%, rgba(255,255,255,.024) 0 3px, transparent 3px), radial-gradient(circle at 45% 85%, rgba(255,255,255,.02) 0 2px, transparent 2px), linear-gradient(140deg, rgba(255,255,255,.03), transparent 60%);
}

.cb-08[data-theme="dark"] .cb-08__moon {
  display: none;
}

.cb-08[data-theme="dark"] .cb-08__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .cb-08:not([data-theme="light"]) {
    --bg: #0b141a;
    --app: #202c33;
    --ink: #e9edef;
    --muted: #8696a0;
    --line: #2a3942;
    --in: #202c33;
    --in-ink: #e9edef;
    --out: #005c4b;
    --out-ink: #e9edef;
    --shadow: rgba(0,0,0,.6);
  }

  .cb-08:not([data-theme="light"]) .cb-08__thread {
    background-color: #0c1317;
    background-image: radial-gradient(circle at 20% 30%, rgba(255,255,255,.028) 0 2px, transparent 2px), radial-gradient(circle at 70% 60%, rgba(255,255,255,.024) 0 3px, transparent 3px), radial-gradient(circle at 45% 85%, rgba(255,255,255,.02) 0 2px, transparent 2px), linear-gradient(140deg, rgba(255,255,255,.03), transparent 60%);
  }

  .cb-08:not([data-theme="light"]) .cb-08__moon {
    display: none;
  }

  .cb-08:not([data-theme="light"]) .cb-08__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-08 *,
    .cb-08 *::before,
    .cb-08 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .cb-08__msg {
    border: 1px solid CanvasText;
  }

  .cb-08__tick[data-state="read"] {
    color: Highlight;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.cb-08');
  if (!root) return;
  const thread = root.querySelector('#cb-08-thread');
  const input = root.querySelector('#cb-08-input');
  const send = root.querySelector('#cb-08-send');
  const status = root.querySelector('#cb-08-status');
  const STEPS = [['sent', 'Sent', 500], ['delivered', 'Delivered', 1400], ['read', 'Read', 3200]];

  const TICK = '<svg viewBox="0 0 20 14" fill="none" aria-hidden="true" focusable="false">'
    + '<path class="cb-08__tick-1" d="M1.5 7.6 5 11l6.6-8" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>'
    + '<path class="cb-08__tick-2" d="M7.6 7.6 11 11l6.6-8" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>';

  const clock = () => {
    const d = new Date();
    return String(d.getHours()).padStart(2, '0') + ':' + String(d.getMinutes()).padStart(2, '0');
  };

  send.addEventListener('click', () => {
    const text = input.value.trim();
    if (!text) return;
    const li = document.createElement('li');
    li.className = 'cb-08__turn cb-08__turn--out';
    const msg = document.createElement('div');
    msg.className = 'cb-08__msg';
    const meta = document.createElement('span');
    meta.className = 'cb-08__meta';
    const t = document.createElement('time');
    t.dateTime = new Date().toISOString(); t.textContent = clock();
    const tick = document.createElement('span');
    tick.className = 'cb-08__tick'; tick.dataset.state = 'sent';
    tick.setAttribute('role', 'img'); tick.setAttribute('aria-label', 'Sending');
    tick.innerHTML = TICK;
    meta.append(t, tick);
    msg.append(meta, document.createTextNode(text));   /* meta first — floats need to precede the text */
    li.append(msg); thread.append(li);
    thread.scrollTop = thread.scrollHeight;
    input.value = ''; send.disabled = true; input.focus();

    STEPS.forEach(([state, label, delay]) => setTimeout(() => {
      tick.dataset.state = state;
      tick.setAttribute('aria-label', label);
      if (state === 'read') status.textContent = 'Your message was read';
    }, delay));
    status.textContent = 'Message sent';
  });

  input.addEventListener('input', () => { send.disabled = !input.value.trim(); });
  input.addEventListener('keydown', (e) => { if (e.key === 'Enter') send.click(); });
  thread.scrollTop = thread.scrollHeight;
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.cb-08');
  const btn = root && root.querySelector('.cb-08__theme');
  if (!btn) return;
  const isDark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    btn.setAttribute('aria-pressed', String(isDark()));
    btn.setAttribute('aria-label', isDark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  sync();
})();
```
