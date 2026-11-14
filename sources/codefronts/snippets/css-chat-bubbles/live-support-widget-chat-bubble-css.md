---
source: "codefronts"
url: "https://codefronts.com/snippets/css-chat-bubbles/live-support-widget-chat-bubble-css/"
title: "Live Support Widget Chat Bubble CSS"
section: "snippets"
category: "css-chat-bubbles"
category_name: "CSS Chat Bubbles"
description: "A floating support launcher that expands into a real conversation card — built on the Popover API, so the browser handles the top layer, light-dismiss,…"
has_js: "true"
---

Here's a working CSS Chat Bubble from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Live Support Widget Chat Bubble CSS
Source: https://codefronts.com/snippets/css-chat-bubbles/live-support-widget-chat-bubble-css/

A floating support launcher that expands into a real conversation card — built on the Popover API, so the browser handles the top layer, light-dismiss, Escape, and focus return with no JavaScript at all. @starting-style gives it an origin-anchored open animation, an unread badge counts waiting replies, quick-reply chips send canned questions, and the agent answers with a typing pause first.
## HTML
```html
<div class="cb-07">
  <button class="cb-07__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cb-07__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="cb-07__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>

  <button class="cb-07__launch" id="cb-07-launch" type="button" popovertarget="cb-07-card" aria-label="Open support chat">
    <svg class="cb-07__ico-chat" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 11.6c0 4.1-3.8 7.4-8.5 7.4a9.6 9.6 0 0 1-2.6-.35L5 20.5l1.2-3.3A7 7 0 0 1 3.5 11.6C3.5 7.5 7.3 4.2 12 4.2s8.5 3.3 8.5 7.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><circle cx="8.6" cy="11.6" r="1.15" fill="currentColor"/><circle cx="12" cy="11.6" r="1.15" fill="currentColor"/><circle cx="15.4" cy="11.6" r="1.15" fill="currentColor"/></svg>
    <svg class="cb-07__ico-close" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.5 6.5l11 11m0-11-11 11" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"/></svg>
    <span class="cb-07__badge" id="cb-07-badge" aria-hidden="true">1</span>
  </button>
  <p class="cb-07__sr" id="cb-07-unread" role="status" aria-live="polite">1 unread reply from support</p>

  <div class="cb-07__card" id="cb-07-card" popover="auto" aria-label="Support chat">
    <header class="cb-07__head">
      <span class="cb-07__agent">
        <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=facearea&facepad=2.8&w=160&h=160&q=70" width="40" height="40" alt="Rosa, support specialist" loading="lazy" decoding="async">
        <span class="cb-07__pulse" aria-hidden="true"></span>
      </span>
      <span class="cb-07__ident">
        <b>Rosa · Support</b>
        <small>Replies in about 2 minutes</small>
      </span>
      <button class="cb-07__x" type="button" popovertarget="cb-07-card" popovertargetaction="hide" aria-label="Close support chat">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      </button>
    </header>

    <ol class="cb-07__thread" id="cb-07-thread" aria-label="Support conversation">
      <li class="cb-07__turn cb-07__turn--in">
        <p class="cb-07__msg">Hi! I'm Rosa. Ask me anything about billing, shipping or returns.</p>
        <time class="cb-07__t" datetime="2027-04-02T09:31">09:31</time>
      </li>
      <li class="cb-07__turn cb-07__turn--in">
        <p class="cb-07__msg">If it's faster, pick one of the shortcuts below.</p>
        <time class="cb-07__t" datetime="2027-04-02T09:31">09:31</time>
      </li>
    </ol>

    <div class="cb-07__quick" role="group" aria-label="Common questions">
      <button class="cb-07__chip" type="button" data-k="track">Track my order</button>
      <button class="cb-07__chip" type="button" data-k="return">Start a return</button>
      <button class="cb-07__chip" type="button" data-k="invoice">Resend invoice</button>
    </div>

    <div class="cb-07__composer">
      <input class="cb-07__input" id="cb-07-input" type="text" placeholder="Write a message…" aria-label="Message support">
      <button class="cb-07__send" id="cb-07-send" type="button" aria-label="Send message" disabled>
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 12 20 5l-3.2 14.5-4.6-4.3-3 2.4z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
      </button>
    </div>
    <p class="cb-07__sr" id="cb-07-status" role="status" aria-live="polite"></p>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap');

.cb-07 {
  --bg: #eef0f4;
  --surface: #ffffff;
  --ink: #0d1017;
  --muted: #666f7e;
  --line: #e4e7ee;
  --in: #f1f3f8;
  --in-ink: #0d1017;
  --out: #ff5a2b;
  --out-ink: #ffffff;
  --live: #22c55e;
  --ring: #ff5a2b;
  --shadow: rgba(13,16,23,.2);
  --w: 22.5rem;
  --sans: "Outfit",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
  background: radial-gradient(80% 60% at 90% 100%, color-mix(in oklab,var(--out) 16%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cb-07,
.cb-07 *,
.cb-07 *::before,
.cb-07 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .cb-07 {
    --bg: oklch(95.5% .006 265);
    --surface: oklch(100% 0 0);
    --ink: oklch(16% .02 265);
    --muted: oklch(52% .02 265);
    --line: oklch(92% .008 265);
    --in: oklch(96.5% .006 265);
    --out: oklch(65% .2 35);
    --live: oklch(75% .18 148);
  }
}

.cb-07__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cb-07 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.cb-07__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,3vw,1.6rem);
  inset-inline-end: clamp(.9rem,3vw,1.6rem);
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 14px;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--ink);
  transition: transform .25s cubic-bezier(.16,1,.3,1);
}

.cb-07__theme:hover {
  transform: translateY(-2px);
}

.cb-07__theme svg {
  inline-size: 20px;
  block-size: 20px;
}

.cb-07__sun {
  display: none;
}
/* ── launcher ── */

.cb-07__launch {
  position: absolute;
  inset-block-end: clamp(1rem,4vw,2rem);
  inset-inline-end: clamp(1rem,4vw,2rem);
  inline-size: 60px;
  block-size: 60px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border: 0;
  border-radius: 50%;
  background: var(--out);
  color: var(--out-ink);
  box-shadow: 0 18px 40px -14px color-mix(in oklab,var(--out) 60%,transparent), 0 2px 6px -2px var(--shadow);
  transition: transform .35s cubic-bezier(.16,1,.3,1), box-shadow .3s;
}

.cb-07__launch:hover {
  transform: translateY(-3px) scale(1.04);
}

.cb-07__launch svg {
  inline-size: 26px;
  block-size: 26px;
  transition: opacity .25s, rotate .35s cubic-bezier(.16,1,.3,1);
}

.cb-07__ico-close {
  position: absolute;
  opacity: 0;
  rotate: -40deg;
}

.cb-07__launch[aria-expanded="true"] .cb-07__ico-chat {
  opacity: 0;
  rotate: 40deg;
}

.cb-07__launch[aria-expanded="true"] .cb-07__ico-close {
  opacity: 1;
  rotate: 0deg;
}

.cb-07__launch::after {
  content: '';
  position: absolute;
  inset: -6px;
  border-radius: 50%;
  border: 2px solid color-mix(in oklab,var(--out) 50%,transparent);
  animation: cb-07-ping 2.6s cubic-bezier(.16,1,.3,1) infinite;
}

@keyframes cb-07-ping {
  0% {
    scale: .85;
    opacity: .7;
  }

  70%,
    100% {
    scale: 1.25;
    opacity: 0;
  }
}

.cb-07__launch[aria-expanded="true"]::after {
  animation: none;
  opacity: 0;
}

.cb-07__badge {
  position: absolute;
  inset-block-start: -2px;
  inset-inline-end: -2px;
  min-inline-size: 1.4rem;
  block-size: 1.4rem;
  padding-inline: .3rem;
  display: grid;
  place-items: center;
  border-radius: 999px;
  background: var(--ink);
  color: var(--surface);
  font-size: .72rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  outline: 2px solid var(--surface);
}

.cb-07__badge[hidden] {
  display: none;
}
/* ── card: popover in the top layer ── */

.cb-07__card {
  position: fixed;
  inset: auto clamp(1rem,4vw,2rem) calc(clamp(1rem,4vw,2rem) + 74px) auto;
  inline-size: min(var(--w),calc(100vw - 2rem));
  max-block-size: min(78svh,34rem);
  margin: 0;
  padding: 0;
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  overflow: clip;
  display: grid;
  grid-template-rows: auto 1fr auto auto;
  background: var(--surface);
  color: var(--ink);
  box-shadow: 0 40px 90px -40px var(--shadow);
  transform-origin: 100% 100%;
  opacity: 0;
  scale: .9;
  translate: 0 12px;
  transition: opacity .32s cubic-bezier(.16,1,.3,1), scale .32s cubic-bezier(.16,1,.3,1), translate .32s cubic-bezier(.16,1,.3,1), overlay .32s allow-discrete, display .32s allow-discrete;
}

.cb-07__card:popover-open {
  opacity: 1;
  scale: 1;
  translate: 0 0;
}

@starting-style {
  .cb-07__card:popover-open {
    opacity: 0;
    scale: .9;
    translate: 0 12px;
  }
}

.cb-07__card::backdrop {
  background: transparent;
}

@supports (anchor-name: --x) {
  .cb-07__launch {
    anchor-name: --cb-07-launch;
  }

  .cb-07__card {
    position-anchor: --cb-07-launch;
    position-area: block-start span-inline-start;
    inset: auto;
    margin-block-end: .9rem;
    position-try-fallbacks: flip-block, flip-inline;
  }
}

.cb-07__head {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: .7rem;
  padding: .85rem 1rem;
  border-block-end: 1px solid var(--line);
  background: linear-gradient(180deg,color-mix(in oklab,var(--out) 12%,var(--surface)),var(--surface));
}

.cb-07__agent {
  position: relative;
  display: block;
  inline-size: 40px;
  block-size: 40px;
}

.cb-07__agent img {
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  object-fit: cover;
  background: var(--in);
}

.cb-07__pulse {
  position: absolute;
  inset-block-end: -1px;
  inset-inline-end: -1px;
  inline-size: .7rem;
  block-size: .7rem;
  border-radius: 50%;
  background: var(--live);
  outline: 2px solid var(--surface);
}

.cb-07__ident {
  display: grid;
}

.cb-07__ident b {
  font-size: .92rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.cb-07__ident small {
  font-size: .72rem;
  color: var(--muted);
}

.cb-07__x {
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border: 0;
  border-radius: .8rem;
  background: transparent;
  color: var(--muted);
}

.cb-07__x:hover {
  background: var(--in);
  color: var(--ink);
}

.cb-07__x svg {
  inline-size: 18px;
  block-size: 18px;
}

.cb-07__thread {
  list-style: none;
  margin: 0;
  padding: 1rem;
  display: grid;
  gap: .5rem;
  align-content: start;
  overflow-y: auto;
  overflow-x: clip;
  scrollbar-width: thin;
}

.cb-07__turn {
  display: grid;
  gap: .15rem;
  justify-items: start;
  max-inline-size: 88%;
}

.cb-07__turn--out {
  justify-items: end;
  justify-self: end;
}

.cb-07__msg {
  margin: 0;
  padding: .6rem .9rem;
  font-size: .92rem;
  line-height: 1.5;
  text-wrap: pretty;
  border-radius: 1.1rem 1.1rem 1.1rem .3rem;
  background: var(--in);
  color: var(--in-ink);
  animation: cb-07-pop .42s cubic-bezier(.16,1,.3,1) backwards;
}

.cb-07__turn--out .cb-07__msg {
  background: var(--out);
  color: var(--out-ink);
  border-radius: 1.1rem 1.1rem .3rem 1.1rem;
}

@keyframes cb-07-pop {
  from {
    opacity: 0;
    translate: 0 6px;
    scale: .96;
  }

  to {
    opacity: 1;
    translate: 0;
    scale: 1;
  }
}

.cb-07__t {
  font-size: .64rem;
  font-weight: 600;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.cb-07__dots {
  display: inline-flex;
  gap: .22rem;
  padding: .75rem .9rem;
  border-radius: 1.1rem 1.1rem 1.1rem .3rem;
  background: var(--in);
}

.cb-07__dots i {
  inline-size: .4rem;
  block-size: .4rem;
  border-radius: 50%;
  background: var(--muted);
  animation: cb-07-dot 1.2s ease-in-out infinite;
  animation-delay: calc(var(--i) * 130ms);
}

@keyframes cb-07-dot {
  0%,
    80%,
    100% {
    opacity: .35;
    translate: 0 0;
  }

  35% {
    opacity: 1;
    translate: 0 -55%;
  }
}

.cb-07__quick {
  display: flex;
  flex-wrap: wrap;
  gap: .35rem;
  padding: 0 1rem .35rem;
}

.cb-07__chip {
  min-block-size: 36px;
  padding: .4rem .75rem;
  border-radius: 999px;
  cursor: pointer;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--muted);
  font: inherit;
  font-size: .78rem;
  font-weight: 500;
  transition: transform .22s cubic-bezier(.16,1,.3,1), border-color .2s, color .2s;
}

.cb-07__chip:hover {
  transform: translateY(-2px);
  color: var(--ink);
  border-color: color-mix(in oklab,var(--out) 50%,var(--line));
}

.cb-07__composer {
  display: flex;
  gap: .4rem;
  padding: .7rem 1rem 1rem;
  border-block-start: 1px solid var(--line);
}

.cb-07__input {
  flex: 1;
  min-block-size: 44px;
  padding-inline: .9rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: var(--in);
  color: var(--ink);
  font: inherit;
  font-size: .92rem;
  outline: 0;
  transition: border-color .25s, background .25s;
}

.cb-07__input::placeholder {
  color: var(--muted);
}

.cb-07__input:focus {
  border-color: color-mix(in oklab,var(--out) 55%,var(--line));
  background: var(--surface);
}

.cb-07__send {
  inline-size: 44px;
  block-size: 44px;
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

.cb-07__send svg {
  inline-size: 19px;
  block-size: 19px;
}

.cb-07__send:disabled {
  opacity: .3;
  cursor: not-allowed;
}

.cb-07__send:not(:disabled):hover {
  transform: scale(1.08);
}

@media (max-width: 30rem) {
  .cb-07__card {
    inline-size: calc(100vw - 1.5rem);
    max-block-size: 70svh;
  }
}
/* dark */

.cb-07[data-theme="dark"] {
  --bg: #0a0c10;
  --surface: #14181f;
  --ink: #eef1f6;
  --muted: #8f98a7;
  --line: #242a34;
  --in: #1c222c;
  --in-ink: #eef1f6;
  --shadow: rgba(0,0,0,.75);
}

.cb-07[data-theme="dark"] .cb-07__moon {
  display: none;
}

.cb-07[data-theme="dark"] .cb-07__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .cb-07:not([data-theme="light"]) {
    --bg: #0a0c10;
    --surface: #14181f;
    --ink: #eef1f6;
    --muted: #8f98a7;
    --line: #242a34;
    --in: #1c222c;
    --in-ink: #eef1f6;
    --shadow: rgba(0,0,0,.75);
  }

  .cb-07:not([data-theme="light"]) .cb-07__moon {
    display: none;
  }

  .cb-07:not([data-theme="light"]) .cb-07__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-07 *,
    .cb-07 *::before,
    .cb-07 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .cb-07__card,
    .cb-07__msg,
    .cb-07__launch {
    border: 1px solid CanvasText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.cb-07');
  if (!root) return;
  const launch = root.querySelector('#cb-07-launch');
  const card = root.querySelector('#cb-07-card');
  const thread = root.querySelector('#cb-07-thread');
  const input = root.querySelector('#cb-07-input');
  const send = root.querySelector('#cb-07-send');
  const badge = root.querySelector('#cb-07-badge');
  const unread = root.querySelector('#cb-07-unread');
  const status = root.querySelector('#cb-07-status');

  const REPLIES = {
    track: "Your order left our Manchester hub this morning — the courier is showing delivery tomorrow before 6pm. Want the tracking link?",
    return: "No problem. Returns are free within 30 days: I've emailed you a prepaid label, just drop the parcel at any locker.",
    invoice: "Done — invoice #48120 is on its way to the address on your account. It should land within a minute or two.",
    default: "Thanks, I've got that. Give me a moment to pull up your account and I'll come straight back to you."
  };
  const clock = () => {
    const d = new Date();
    return String(d.getHours()).padStart(2, '0') + ':' + String(d.getMinutes()).padStart(2, '0');
  };

  const bubble = (text, out) => {
    const li = document.createElement('li');
    li.className = 'cb-07__turn cb-07__turn--' + (out ? 'out' : 'in');
    const p = document.createElement('p');
    p.className = 'cb-07__msg'; p.textContent = text;
    const t = document.createElement('time');
    t.className = 'cb-07__t'; t.dateTime = new Date().toISOString(); t.textContent = clock();
    li.append(p, t); thread.append(li);
    thread.scrollTop = thread.scrollHeight;
    return li;
  };

  const typing = () => {
    const li = document.createElement('li');
    li.className = 'cb-07__turn cb-07__turn--in';
    li.innerHTML = '<span class="cb-07__dots" aria-hidden="true"><i style="--i:0"></i><i style="--i:1"></i><i style="--i:2"></i></span>';
    thread.append(li); thread.scrollTop = thread.scrollHeight;
    return li;
  };

  const answer = (key) => {
    const t = typing();
    setTimeout(() => {
      t.remove();
      bubble(REPLIES[key] || REPLIES.default, false);
      status.textContent = 'Rosa replied';
    }, 1500);
  };

  const ask = (text, key) => {
    bubble(text, true);
    status.textContent = 'Message sent';
    answer(key || 'default');
  };

  input.addEventListener('input', () => { send.disabled = !input.value.trim(); });
  input.addEventListener('keydown', (e) => { if (e.key === 'Enter') send.click(); });
  send.addEventListener('click', () => {
    const v = input.value.trim();
    if (!v) return;
    input.value = ''; send.disabled = true; ask(v);
    input.focus();
  });
  root.querySelectorAll('.cb-07__chip').forEach((c) => {
    c.addEventListener('click', () => ask(c.textContent.trim(), c.dataset.k));
  });

  /* the popover reports its own state — no click bookkeeping needed */
  card.addEventListener('toggle', (e) => {
    const open = e.newState === 'open';
    launch.setAttribute('aria-expanded', String(open));
    launch.setAttribute('aria-label', open ? 'Close support chat' : 'Open support chat');
    if (!open) return;
    badge.hidden = true;
    unread.textContent = '';
    thread.scrollTop = thread.scrollHeight;
    setTimeout(() => input.focus(), 340);
  });
  launch.setAttribute('aria-expanded', 'false');
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.cb-07');
  const btn = root && root.querySelector('.cb-07__theme');
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
