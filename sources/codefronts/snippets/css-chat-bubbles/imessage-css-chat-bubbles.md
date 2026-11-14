---
source: "codefronts"
url: "https://codefronts.com/snippets/css-chat-bubbles/imessage-css-chat-bubbles/"
title: "iMessage CSS Chat Bubbles"
section: "snippets"
category: "css-chat-bubbles"
category_name: "CSS Chat Bubbles"
description: "An iOS-accurate message thread: true curved tails (not triangles), bubble grouping where only the last message in a run wears a tail, a blue↔green channel…"
has_js: "true"
---

Here's a working CSS Chat Bubble from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: iMessage CSS Chat Bubbles
Source: https://codefronts.com/snippets/css-chat-bubbles/imessage-css-chat-bubbles/

An iOS-accurate message thread: true curved tails (not triangles), bubble grouping where only the last message in a run wears a tail, a blue↔green channel switch for iMessage vs SMS, long-press tapback reactions that bloom out of the bubble, and a Delivered → Read receipt that updates in the live region. The composer sends real messages.
## HTML
```html
<div class="cb-02" data-channel="imessage">
  <button class="cb-02__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cb-02__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="cb-02__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>

  <section class="cb-02__phone" aria-label="Messages with Noor Haddad">
    <header class="cb-02__bar">
      <button class="cb-02__back" type="button" aria-label="Back to conversations">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M14.5 5.5 8 12l6.5 6.5" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <div class="cb-02__who">
        <img class="cb-02__avatar" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=facearea&facepad=2.6&w=160&h=160&q=70" width="44" height="44" alt="Noor Haddad" loading="lazy" decoding="async">
        <span class="cb-02__name">Noor Haddad</span>
      </div>
      <button class="cb-02__channel" type="button" aria-pressed="false" aria-label="Send as SMS instead of iMessage">
        <span class="cb-02__channel-dot" aria-hidden="true"></span>
        <span class="cb-02__channel-text">iMessage</span>
      </button>
    </header>

    <ol class="cb-02__thread" id="cb-02-thread" aria-label="Message transcript">
      <li class="cb-02__day"><time datetime="2027-02-11T09:04">Today 9:04</time></li>
      <li class="cb-02__turn cb-02__turn--in">
        <p class="cb-02__msg">Are we still on for the Shoreditch popup on Thursday?</p>
      </li>
      <li class="cb-02__turn cb-02__turn--out">
        <div class="cb-02__tap">
          <p class="cb-02__msg">Yes — doors at 7, I've got the keys</p>
          <button class="cb-02__tap-btn" type="button" aria-expanded="false" aria-label="React to: Yes — doors at 7, I've got the keys"></button>
          <div class="cb-02__rail" role="group" aria-label="Reactions" hidden></div>
        </div>
      </li>
      <li class="cb-02__turn cb-02__turn--out">
        <div class="cb-02__tap">
          <p class="cb-02__msg">Bringing the little projector too</p>
          <button class="cb-02__tap-btn" type="button" aria-expanded="false" aria-label="React to: Bringing the little projector too"></button>
          <div class="cb-02__rail" role="group" aria-label="Reactions" hidden></div>
        </div>
      </li>
      <li class="cb-02__turn cb-02__turn--in">
        <p class="cb-02__msg">Perfect. I'll sort the playlist and the tiny cups.</p>
      </li>
      <li class="cb-02__turn cb-02__turn--in">
        <p class="cb-02__msg cb-02__msg--jumbo">🎉</p>
      </li>
      <li class="cb-02__receipt" id="cb-02-receipt">Delivered</li>
    </ol>

    <div class="cb-02__composer">
      <button class="cb-02__plus" type="button" aria-label="Add attachment">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 6.5v11M6.5 12h11" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"/></svg>
      </button>
      <div class="cb-02__field">
        <textarea class="cb-02__input" id="cb-02-input" rows="1" placeholder="iMessage" aria-label="Message"></textarea>
        <button class="cb-02__send" id="cb-02-send" type="button" aria-label="Send message" disabled>
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 19V6m0 0-5.2 5.2M12 6l5.2 5.2" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
      </div>
    </div>
    <p class="cb-02__status" id="cb-02-status" role="status" aria-live="polite"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&display=swap');

@property --cb-02-bloom {
  syntax: '<number>';
  inherits: false;
  initial-value: 1;
}

.cb-02 {
  --bg: #eceef3;
  --thread: #ffffff;
  --ink: #080a0f;
  --muted: #7b8494;
  --line: #e4e7ee;
  --in: #e9e9eb;
  --in-ink: #080a0f;
  --out: #0a7cff;
  --out-ink: #ffffff;
  --sms: #2fd158;
  --ring: #0a7cff;
  --shadow: rgba(8,10,15,.16);
  --radius: 1.4rem;
  --sans: "Figtree",-apple-system,BlinkMacSystemFont,"SF Pro Text",ui-sans-serif,system-ui,sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
  background: radial-gradient(100% 70% at 50% 0%, color-mix(in oklab,var(--out) 16%,transparent), transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cb-02,
.cb-02 *,
.cb-02 *::before,
.cb-02 *::after {
  box-sizing: border-box;
}

.cb-02[data-channel="sms"] {
  --out: var(--sms);
  --out-ink: #ffffff;
  --ring: #1fa845;
}

@supports (color: oklch(0 0 0)) {
  .cb-02 {
    --bg: oklch(95.5% .006 265);
    --thread: oklch(100% 0 0);
    --ink: oklch(14% .015 265);
    --muted: oklch(60% .02 265);
    --line: oklch(92% .008 265);
    --in: oklch(92.5% .004 265);
    --out: oklch(58% .21 255);
    --sms: oklch(79% .19 148);
  }
}

.cb-02__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,3vw,1.6rem);
  inset-inline-end: clamp(.9rem,3vw,1.6rem);
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  z-index: 5;
  border-radius: 14px;
  border: 1px solid var(--line);
  background: var(--thread);
  color: var(--ink);
  box-shadow: 0 2px 10px -6px var(--shadow);
  transition: transform .25s cubic-bezier(.16,1,.3,1);
}

.cb-02__theme:hover {
  transform: translateY(-2px);
}

.cb-02__theme svg {
  inline-size: 20px;
  block-size: 20px;
}

.cb-02__sun {
  display: none;
}

.cb-02 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}
/* ── shell ── */

.cb-02__phone {
  inline-size: min(100%,26.5rem);
  max-block-size: min(88svh,44rem);
  display: grid;
  grid-template-rows: auto 1fr auto auto;
  border-radius: clamp(1.5rem,4vw,2.4rem);
  overflow: hidden;
  background: var(--thread);
  border: 1px solid var(--line);
  box-shadow: 0 40px 80px -50px var(--shadow), 0 2px 0 color-mix(in oklab,#fff 40%,transparent) inset;
  container-type: inline-size;
}
/* ── nav bar ── */

.cb-02__bar {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: .5rem;
  padding: .55rem .7rem;
  border-block-end: 1px solid var(--line);
  background: color-mix(in oklab,var(--thread) 82%,transparent);
  backdrop-filter: blur(20px) saturate(1.6);
}

.cb-02__back,
.cb-02__plus {
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border: 0;
  border-radius: 50%;
  background: transparent;
  color: var(--out);
}

.cb-02__back svg,
.cb-02__plus svg {
  inline-size: 22px;
  block-size: 22px;
}

.cb-02__back:hover,
.cb-02__plus:hover {
  background: color-mix(in oklab,var(--out) 10%,transparent);
}

.cb-02__who {
  display: flex;
  align-items: center;
  gap: .55rem;
  min-inline-size: 0;
}

.cb-02__avatar {
  inline-size: 34px;
  block-size: 34px;
  border-radius: 50%;
  object-fit: cover;
  background: var(--in);
}

.cb-02__name {
  font-weight: 600;
  font-size: .98rem;
  letter-spacing: -.015em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cb-02__channel {
  display: flex;
  align-items: center;
  gap: .35rem;
  cursor: pointer;
  min-block-size: 44px;
  padding: .3rem .6rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: transparent;
  color: var(--muted);
  font: inherit;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .01em;
}

.cb-02__channel-dot {
  inline-size: 8px;
  block-size: 8px;
  border-radius: 50%;
  background: var(--out);
  transition: background .3s;
}

.cb-02__channel:hover {
  color: var(--ink);
}
/* ── thread ── */

.cb-02__thread {
  list-style: none;
  margin: 0;
  padding: 1rem 1.1rem 1.4rem;
  display: grid;
  gap: .2rem;
  overflow-y: auto;
  overflow-x: clip;
  overflow-anchor: auto;
  scrollbar-width: thin;
  background: var(--thread);
}

.cb-02__day {
  justify-self: center;
  margin-block: .4rem .8rem;
  font-size: .7rem;
  font-weight: 600;
  color: var(--muted);
  letter-spacing: .02em;
}

.cb-02__turn {
  display: flex;
  margin-block-start: .28rem;
}

.cb-02__turn--in {
  justify-content: flex-start;
}

.cb-02__turn--out {
  justify-content: flex-end;
}

.cb-02__turn--in + .cb-02__turn--in,
.cb-02__turn--out + .cb-02__turn--out {
  margin-block-start: .14rem;
}

.cb-02__msg {
  position: relative;
  margin: 0;
  max-inline-size: min(20rem,76cqi);
  padding: .55rem .9rem;
  font-size: 1rem;
  line-height: 1.35;
  letter-spacing: -.01em;
  border-radius: var(--radius);
  text-wrap: pretty;
  overflow-wrap: anywhere;
  animation: cb-02-in .46s cubic-bezier(.16,1,.3,1) backwards;
}

.cb-02__turn--in .cb-02__msg {
  background: var(--in);
  color: var(--in-ink);
  transform-origin: 0 100%;
}

.cb-02__turn--out .cb-02__msg {
  background: var(--out);
  color: var(--out-ink);
  transform-origin: 100% 100%;
}

.cb-02__msg--jumbo {
  background: none !important;
  font-size: 2.6rem;
  line-height: 1;
  padding: .2rem .3rem;
}

.cb-02__msg--jumbo::before,
.cb-02__msg--jumbo::after {
  display: none;
}

@keyframes cb-02-in {
  from {
    opacity: 0;
    transform: translateY(8px) scale(.9);
  }

  to {
    opacity: 1;
    transform: none;
  }
}
/* grouping: squared inner corners inside a run */

.cb-02__turn--in + .cb-02__turn--in .cb-02__msg {
  border-start-start-radius: .45rem;
}

.cb-02__turn--in:has(+ .cb-02__turn--in) .cb-02__msg {
  border-end-start-radius: .45rem;
}

.cb-02__turn--out + .cb-02__turn--out .cb-02__msg {
  border-start-end-radius: .45rem;
}

.cb-02__turn--out:has(+ .cb-02__turn--out) .cb-02__msg {
  border-end-end-radius: .45rem;
}
/* ── the curved iOS tail: last of each run only ── */

.cb-02__turn--in:not(:has(+ .cb-02__turn--in)) .cb-02__msg::before,
.cb-02__turn--in:not(:has(+ .cb-02__turn--in)) .cb-02__msg::after,
.cb-02__turn--out:not(:has(+ .cb-02__turn--out)) .cb-02__msg::before,
.cb-02__turn--out:not(:has(+ .cb-02__turn--out)) .cb-02__msg::after {
  content: '';
  position: absolute;
  inset-block-end: 0;
  inline-size: 20px;
  block-size: 22px;
}

.cb-02__turn--in:not(:has(+ .cb-02__turn--in)) .cb-02__msg::before {
  background: var(--in);
  inset-inline-start: -7px;
  border-end-end-radius: 18px 15px;
}

.cb-02__turn--in:not(:has(+ .cb-02__turn--in)) .cb-02__msg::after {
  background: var(--thread);
  inset-inline-start: -21px;
  inline-size: 22px;
  border-end-end-radius: 12px;
}

.cb-02__turn--out:not(:has(+ .cb-02__turn--out)) .cb-02__msg::before {
  background: var(--out);
  inset-inline-end: -7px;
  border-end-start-radius: 18px 15px;
}

.cb-02__turn--out:not(:has(+ .cb-02__turn--out)) .cb-02__msg::after {
  background: var(--thread);
  inset-inline-end: -21px;
  inline-size: 22px;
  border-end-start-radius: 12px;
}
/* ── tapback ── */

.cb-02__tap {
  position: relative;
  display: flex;
}

.cb-02__tap-btn {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  border: 0;
  background: transparent;
  cursor: pointer;
  border-radius: var(--radius);
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}

.cb-02__rail {
  position: absolute;
  inset-block-end: calc(100% + .5rem);
  inset-inline-end: 0;
  z-index: 4;
  display: flex;
  gap: .15rem;
  padding: .3rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--thread) 86%,transparent);
  border: 1px solid var(--line);
  box-shadow: 0 18px 40px -22px var(--shadow);
  backdrop-filter: blur(18px) saturate(1.5);
  transition: opacity .3s, transform .3s cubic-bezier(.16,1,.3,1), display .3s allow-discrete;
}

.cb-02__rail[hidden] {
  display: none;
}

.cb-02__react {
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border: 0;
  border-radius: 50%;
  background: transparent;
  font-size: 1.35rem;
  line-height: 1;
  animation: cb-02-bloom .42s cubic-bezier(.16,1,.3,1) backwards;
  animation-delay: calc(var(--i) * 35ms);
  transition: transform .2s cubic-bezier(.16,1,.3,1), background .2s;
}

.cb-02__react:hover {
  transform: scale(1.22) translateY(-2px);
  background: color-mix(in oklab,var(--out) 12%,transparent);
}

.cb-02__react[aria-pressed="true"] {
  background: color-mix(in oklab,var(--out) 20%,transparent);
}

@keyframes cb-02-bloom {
  from {
    opacity: 0;
    transform: scale(.4) translateY(10px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@supports (transition-behavior: allow-discrete) {
  @starting-style {
    .cb-02__rail {
      opacity: 0;
      transform: translateY(8px) scale(.9);
    }
  }
}

.cb-02__badge {
  position: absolute;
  inset-block-start: -.55rem;
  inset-inline-start: -.55rem;
  z-index: 3;
  inline-size: 1.75rem;
  block-size: 1.75rem;
  display: grid;
  place-items: center;
  font-size: .9rem;
  border-radius: 50%;
  background: var(--in);
  border: 2px solid var(--thread);
  animation: cb-02-badge .5s cubic-bezier(.16,1,.3,1);
}

@keyframes cb-02-badge {
  0% {
    transform: scale(0);
  }

  60% {
    transform: scale(1.25);
  }

  100% {
    transform: scale(1);
  }
}

.cb-02__receipt {
  justify-self: end;
  margin-block-start: .3rem;
  padding-inline-end: .3rem;
  font-size: .68rem;
  font-weight: 600;
  color: var(--muted);
  letter-spacing: .02em;
}
/* ── composer ── */

.cb-02__composer {
  display: flex;
  align-items: flex-end;
  gap: .35rem;
  padding: .55rem .6rem .7rem;
  border-block-start: 1px solid var(--line);
  background: color-mix(in oklab,var(--thread) 84%,transparent);
  backdrop-filter: blur(20px);
}

.cb-02__field {
  position: relative;
  flex: 1;
  display: flex;
  align-items: flex-end;
  gap: .3rem;
  padding: .2rem .2rem .2rem .9rem;
  border: 1px solid var(--line);
  border-radius: 1.4rem;
  background: var(--thread);
}

.cb-02__field:focus-within {
  border-color: color-mix(in oklab,var(--out) 55%,var(--line));
}

.cb-02__input {
  flex: 1;
  border: 0;
  outline: 0;
  resize: none;
  background: transparent;
  color: var(--ink);
  font: inherit;
  font-size: 1rem;
  line-height: 1.4;
  padding-block: .55rem;
  max-block-size: 7rem;
}

@supports (field-sizing: content) {
  .cb-02__input {
    field-sizing: content;
  }
}

.cb-02__input::placeholder {
  color: var(--muted);
}

.cb-02__send {
  inline-size: 32px;
  block-size: 32px;
  margin: .12rem;
  flex: 0 0 auto;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 50%;
  background: var(--out);
  color: var(--out-ink);
  cursor: pointer;
  transition: transform .25s cubic-bezier(.16,1,.3,1), opacity .2s;
}

.cb-02__send svg {
  inline-size: 20px;
  block-size: 20px;
}

.cb-02__send:disabled {
  opacity: .32;
  cursor: not-allowed;
}

.cb-02__send:not(:disabled):hover {
  transform: scale(1.09);
}

.cb-02__status {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}
/* ── dark ── */

.cb-02[data-theme="dark"] {
  --bg: #07080b;
  --thread: #000000;
  --ink: #f2f4f8;
  --muted: #8a93a3;
  --line: #20242c;
  --in: #26262a;
  --in-ink: #f2f4f8;
  --shadow: rgba(0,0,0,.8);
}

.cb-02[data-theme="dark"] .cb-02__moon {
  display: none;
}

.cb-02[data-theme="dark"] .cb-02__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .cb-02:not([data-theme="light"]) {
    --bg: #07080b;
    --thread: #000000;
    --ink: #f2f4f8;
    --muted: #8a93a3;
    --line: #20242c;
    --in: #26262a;
    --in-ink: #f2f4f8;
    --shadow: rgba(0,0,0,.8);
  }

  .cb-02:not([data-theme="light"]) .cb-02__moon {
    display: none;
  }

  .cb-02:not([data-theme="light"]) .cb-02__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-02 *,
    .cb-02 *::before,
    .cb-02 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .cb-02__msg {
    border: 1px solid CanvasText;
  }

  .cb-02__msg::before,
    .cb-02__msg::after {
    forced-color-adjust: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.cb-02');
  if (!root) return;
  const thread = root.querySelector('#cb-02-thread');
  const input = root.querySelector('#cb-02-input');
  const send = root.querySelector('#cb-02-send');
  const status = root.querySelector('#cb-02-status');
  const receipt = root.querySelector('#cb-02-receipt');
  const channel = root.querySelector('.cb-02__channel');
  const REACTIONS = ['❤️', '👍', '👎', '😂', '‼️', '❓'];
  const NAMES = { '❤️': 'Loved', '👍': 'Liked', '👎': 'Disliked', '😂': 'Laughed at', '‼️': 'Emphasised', '❓': 'Questioned' };
  const HOLD = 400;
  const EMOJI_ONLY = /^(?:\p{Extended_Pictographic}|\p{Emoji_Component}|\uFE0F|\u200D|\s){1,3}$/u;

  /* ---- reaction rail, built once per outgoing bubble ---- */
  const fillRail = (rail) => {
    if (rail.childElementCount) return;
    REACTIONS.forEach((glyph, i) => {
      const b = document.createElement('button');
      b.type = 'button'; b.className = 'cb-02__react'; b.textContent = glyph;
      b.style.setProperty('--i', i);
      b.setAttribute('aria-pressed', 'false');
      b.setAttribute('aria-label', NAMES[glyph]);
      rail.append(b);
    });
  };
  const closeRails = (except) => root.querySelectorAll('.cb-02__rail').forEach((r) => {
    if (r === except) return;
    r.hidden = true;
    r.previousElementSibling.setAttribute('aria-expanded', 'false');
  });

  const wireTap = (tap) => {
    const btn = tap.querySelector('.cb-02__tap-btn');
    const rail = tap.querySelector('.cb-02__rail');
    const msg = tap.querySelector('.cb-02__msg');
    let timer = null, held = false;

    const open = () => {
      fillRail(rail); closeRails(rail);
      rail.hidden = false; btn.setAttribute('aria-expanded', 'true');
      rail.querySelector('.cb-02__react').focus();
    };
    btn.addEventListener('pointerdown', () => { held = false; timer = setTimeout(() => { held = true; open(); }, HOLD); });
    btn.addEventListener('pointerup', () => clearTimeout(timer));
    btn.addEventListener('pointerleave', () => clearTimeout(timer));
    btn.addEventListener('contextmenu', (e) => e.preventDefault());
    btn.addEventListener('click', () => { if (!held) open(); });

    rail.addEventListener('click', (e) => {
      const chip = e.target.closest('.cb-02__react');
      if (!chip) return;
      rail.querySelectorAll('.cb-02__react').forEach((c) => c.setAttribute('aria-pressed', 'false'));
      tap.querySelector('.cb-02__badge')?.remove();
      const badge = document.createElement('span');
      badge.className = 'cb-02__badge'; badge.textContent = chip.textContent;
      badge.setAttribute('aria-hidden', 'true');
      tap.append(badge);
      chip.setAttribute('aria-pressed', 'true');
      status.textContent = NAMES[chip.textContent] + ': ' + msg.textContent.trim();
      rail.hidden = true; btn.setAttribute('aria-expanded', 'false'); btn.focus();
    });
    rail.addEventListener('keydown', (e) => { if (e.key === 'Escape') { rail.hidden = true; btn.focus(); } });
  };
  root.querySelectorAll('.cb-02__tap').forEach(wireTap);
  document.addEventListener('click', (e) => { if (!e.target.closest('.cb-02__tap')) closeRails(null); });

  /* ---- composer ---- */
  const grow = () => {                                   // fallback for no field-sizing
    if (CSS.supports('field-sizing', 'content')) return;
    input.style.height = 'auto';
    input.style.height = Math.min(input.scrollHeight, 112) + 'px';
  };
  const scrollDown = () => { thread.scrollTop = thread.scrollHeight; };

  const push = (text) => {
    const li = document.createElement('li');
    li.className = 'cb-02__turn cb-02__turn--out';
    const tap = document.createElement('div');
    tap.className = 'cb-02__tap';
    const p = document.createElement('p');
    p.className = 'cb-02__msg' + (EMOJI_ONLY.test(text.trim()) ? ' cb-02__msg--jumbo' : '');
    p.textContent = text;
    const btn = document.createElement('button');
    btn.type = 'button'; btn.className = 'cb-02__tap-btn';
    btn.setAttribute('aria-expanded', 'false');
    btn.setAttribute('aria-label', 'React to: ' + text);
    const rail = document.createElement('div');
    rail.className = 'cb-02__rail'; rail.hidden = true;
    rail.setAttribute('role', 'group'); rail.setAttribute('aria-label', 'Reactions');
    tap.append(p, btn, rail); li.append(tap);
    thread.insertBefore(li, receipt);
    wireTap(tap);
    receipt.textContent = 'Sent';
    setTimeout(() => { receipt.textContent = 'Delivered'; }, 900);
    setTimeout(() => { receipt.textContent = 'Read 9:41'; status.textContent = 'Message read'; }, 2600);
    scrollDown();
  };

  input.addEventListener('input', () => { send.disabled = !input.value.trim(); grow(); });
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send.click(); }
  });
  send.addEventListener('click', () => {
    const text = input.value.trim();
    if (!text) return;
    push(text);
    input.value = ''; send.disabled = true; grow(); input.focus();
  });

  channel.addEventListener('click', () => {
    const sms = root.dataset.channel === 'imessage';
    root.dataset.channel = sms ? 'sms' : 'imessage';
    channel.setAttribute('aria-pressed', String(sms));
    channel.setAttribute('aria-label', sms ? 'Send as iMessage instead of SMS' : 'Send as SMS instead of iMessage');
    channel.querySelector('.cb-02__channel-text').textContent = sms ? 'SMS' : 'iMessage';
    input.placeholder = sms ? 'Text Message' : 'iMessage';
    status.textContent = sms ? 'Sending as SMS' : 'Sending as iMessage';
  });

  scrollDown();
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.cb-02');
  const btn = root && root.querySelector('.cb-02__theme');
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
