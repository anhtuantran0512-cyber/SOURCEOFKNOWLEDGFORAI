---
source: "codefronts"
url: "https://codefronts.com/snippets/css-chat-bubbles/responsive-full-chat-screen-flexbox-css/"
title: "Responsive Full Chat Screen Flexbox CSS"
section: "snippets"
category: "css-chat-bubbles"
category_name: "CSS Chat Bubbles"
description: "A complete two-pane messenger shell that becomes a single-pane mobile app without a media query — the breakpoint is a container query, so the same component…"
has_js: "true"
---

Here's a working CSS Chat Bubble from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Full Chat Screen Flexbox CSS
Source: https://codefronts.com/snippets/css-chat-bubbles/responsive-full-chat-screen-flexbox-css/

A complete two-pane messenger shell that becomes a single-pane mobile app without a media query — the breakpoint is a container query, so the same component works full-screen, in a split view or inside a 380 px sidebar. Scrollable history with a pinned composer, sticky date headers, an auto-growing textarea, unread pills, three switchable conversations and a back button that only exists in the narrow layout.
## HTML
```html
<div class="cb-11" data-pane="list">
  <button class="cb-11__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cb-11__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="cb-11__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>

  <div class="cb-11__app">
    <aside class="cb-11__list" aria-label="Conversations">
      <div class="cb-11__list-top">
        <h2 class="cb-11__brand">Threads</h2>
        <div class="cb-11__search">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.2" stroke="currentColor" stroke-width="1.8"/><path d="m15.6 15.6 3.9 3.9" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          <input id="cb-11-search" type="search" placeholder="Search conversations" aria-label="Search conversations">
        </div>
      </div>
      <ul class="cb-11__convos" id="cb-11-convos">
        <li>
          <button class="cb-11__convo" type="button" data-id="ana" aria-current="true">
            <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=facearea&facepad=2.8&w=120&h=120&q=70" width="44" height="44" alt="" loading="lazy" decoding="async">
            <span class="cb-11__convo-text"><b>Ana Ferreira</b><small>Sent the revised floor plan</small></span>
            <span class="cb-11__convo-side"><time datetime="2027-07-21T11:02">11:02</time></span>
          </button>
        </li>
        <li>
          <button class="cb-11__convo" type="button" data-id="build">
            <img src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=facearea&facepad=2.8&w=120&h=120&q=70" width="44" height="44" alt="" loading="lazy" decoding="async">
            <span class="cb-11__convo-text"><b>Build crew</b><small>Milos: scaffolding is up</small></span>
            <span class="cb-11__convo-side"><time datetime="2027-07-21T10:38">10:38</time><em class="cb-11__pill">3</em></span>
          </button>
        </li>
        <li>
          <button class="cb-11__convo" type="button" data-id="lena">
            <img src="https://images.unsplash.com/photo-1502685104226-ee32379fefbe?auto=format&fit=facearea&facepad=2.8&w=120&h=120&q=70" width="44" height="44" alt="" loading="lazy" decoding="async">
            <span class="cb-11__convo-text"><b>Lena Brandt</b><small>Can we push to Thursday?</small></span>
            <span class="cb-11__convo-side"><time datetime="2027-07-20T18:14">Yest.</time></span>
          </button>
        </li>
      </ul>
    </aside>

    <main class="cb-11__main">
      <header class="cb-11__head">
        <button class="cb-11__back" id="cb-11-back" type="button" aria-label="Back to conversations">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M14.5 5.5 8 12l6.5 6.5" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <img class="cb-11__head-pic" id="cb-11-head-pic" src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=facearea&facepad=2.8&w=120&h=120&q=70" width="40" height="40" alt="" loading="lazy" decoding="async">
        <span class="cb-11__head-text"><b id="cb-11-head-name">Ana Ferreira</b><small id="cb-11-head-sub">Active 4 minutes ago</small></span>
        <button class="cb-11__icon" type="button" aria-label="Start a call"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.2 4.5h3l1.4 3.4-2 1.5a10 10 0 0 0 5.5 5.5l1.5-2 3.4 1.4v3a1.6 1.6 0 0 1-1.8 1.6C10.6 18.4 5.6 13.4 4.6 6.3A1.6 1.6 0 0 1 6.2 4.5Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg></button>
      </header>

      <ol class="cb-11__msgs" id="cb-11-msgs" aria-label="Message history"></ol>

      <div class="cb-11__composer">
        <button class="cb-11__icon" type="button" aria-label="Attach a file"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M13.7 6.6 7.4 12.9a3.1 3.1 0 0 0 4.4 4.4l7.1-7.1a4.7 4.7 0 0 0-6.6-6.6L5 11" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg></button>
        <textarea class="cb-11__input" id="cb-11-input" rows="1" placeholder="Write a message…" aria-label="Write a message"></textarea>
        <button class="cb-11__send" id="cb-11-send" type="button" aria-label="Send message" disabled><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 19V6m0 0-5.4 5.4M12 6l5.4 5.4" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
      </div>
    </main>
  </div>
  <p class="cb-11__sr" id="cb-11-status" role="status" aria-live="polite"></p>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&display=swap');

.cb-11 {
  --bg: #f6f7f9;
  --surface: #ffffff;
  --panel: #fbfbfd;
  --ink: #0c0f15;
  --muted: #68717f;
  --line: #e6e9ef;
  --in: #f0f2f6;
  --in-ink: #0c0f15;
  --out: #2f6bff;
  --out-ink: #ffffff;
  --acc: #2f6bff;
  --pill: #ff4d4f;
  --shadow: rgba(12,15,21,.14);
  --side: 20rem;
  --sans: "Instrument Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  position: relative;
  container-type: inline-size;
  width: 100%;
  min-height: 100vh;
  min-height: 100dvh;
  display: grid;
  place-items: stretch;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cb-11,
.cb-11 *,
.cb-11 *::before,
.cb-11 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .cb-11 {
    --bg: oklch(97% .004 265);
    --surface: oklch(100% 0 0);
    --panel: oklch(98.6% .003 265);
    --ink: oklch(16% .02 265);
    --muted: oklch(53% .02 265);
    --line: oklch(92% .008 265);
    --in: oklch(95.5% .006 265);
    --out: oklch(55% .21 262);
    --acc: oklch(55% .21 262);
  }
}

.cb-11__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cb-11 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cb-11__theme {
  position: absolute;
  inset-block-start: .75rem;
  inset-inline-end: .75rem;
  z-index: 6;
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 14px;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--ink);
  box-shadow: 0 2px 10px -6px var(--shadow);
  transition: transform .25s cubic-bezier(.16,1,.3,1);
}

.cb-11__theme:hover {
  transform: translateY(-2px);
}

.cb-11__theme svg {
  inline-size: 20px;
  block-size: 20px;
}

.cb-11__sun {
  display: none;
}
/* ── shell ── */

.cb-11__app {
  display: grid;
  grid-template-columns: var(--side) minmax(0,1fr);
  block-size: 100%;
  min-block-size: 100vh;
  min-block-size: 100dvh;
  background: var(--surface);
}
/* ── conversation list ── */

.cb-11__list {
  display: grid;
  grid-template-rows: auto minmax(0,1fr);
  min-inline-size: 0;
  border-inline-end: 1px solid var(--line);
  background: var(--panel);
}

.cb-11__list-top {
  display: grid;
  gap: .75rem;
  padding: 1.1rem 1rem .85rem;
  border-block-end: 1px solid var(--line);
}

.cb-11__brand {
  margin: 0;
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: -.03em;
}

.cb-11__search {
  position: relative;
  display: flex;
  align-items: center;
}

.cb-11__search svg {
  position: absolute;
  inset-inline-start: .7rem;
  inline-size: 17px;
  block-size: 17px;
  color: var(--muted);
}

.cb-11__search input {
  inline-size: 100%;
  min-block-size: 44px;
  padding-inline: 2.2rem .8rem;
  border-radius: .85rem;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--ink);
  font: inherit;
  font-size: .9rem;
  outline: 0;
  transition: border-color .25s;
}

.cb-11__search input::placeholder {
  color: var(--muted);
}

.cb-11__search input:focus {
  border-color: color-mix(in oklab,var(--acc) 55%,var(--line));
}

.cb-11__convos {
  list-style: none;
  margin: 0;
  padding: .5rem;
  display: grid;
  gap: .15rem;
  align-content: start;
  overflow-y: auto;
  scrollbar-gutter: stable;
  scrollbar-width: thin;
}

.cb-11__convo {
  inline-size: 100%;
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto;
  align-items: center;
  gap: .7rem;
  padding: .65rem .7rem;
  border: 0;
  border-radius: 1rem;
  background: transparent;
  color: inherit;
  font: inherit;
  text-align: start;
  cursor: pointer;
  transition: background .2s, transform .2s cubic-bezier(.16,1,.3,1);
}

.cb-11__convo:hover {
  background: color-mix(in oklab,var(--acc) 7%,transparent);
}

.cb-11__convo[aria-current="true"] {
  background: color-mix(in oklab,var(--acc) 12%,transparent);
}

.cb-11__convo img {
  inline-size: 44px;
  block-size: 44px;
  border-radius: 50%;
  object-fit: cover;
  background: var(--in);
}

.cb-11__convo-text {
  display: grid;
  gap: .1rem;
  min-inline-size: 0;
}

.cb-11__convo-text b {
  font-size: .92rem;
  font-weight: 600;
  letter-spacing: -.015em;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.cb-11__convo-text small {
  font-size: .8rem;
  color: var(--muted);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.cb-11__convo-side {
  display: grid;
  gap: .25rem;
  justify-items: end;
}

.cb-11__convo-side time {
  font-size: .68rem;
  font-weight: 500;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.cb-11__pill {
  min-inline-size: 1.25rem;
  block-size: 1.25rem;
  padding-inline: .3rem;
  display: grid;
  place-items: center;
  border-radius: 999px;
  background: var(--pill);
  color: #fff;
  font-style: normal;
  font-size: .68rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}
/* ── thread pane ── */

.cb-11__main {
  display: grid;
  grid-template-rows: auto minmax(0,1fr) auto;
  min-inline-size: 0;
  background: var(--surface);
}

.cb-11__head {
  display: flex;
  align-items: center;
  gap: .7rem;
  padding: .7rem 4rem .7rem .9rem;
  border-block-end: 1px solid var(--line);
  background: color-mix(in oklab,var(--surface) 86%,transparent);
  backdrop-filter: blur(16px);
}

.cb-11__back {
  display: none;
  inline-size: 44px;
  block-size: 44px;
  place-items: center;
  border: 0;
  border-radius: .8rem;
  background: transparent;
  color: var(--acc);
  cursor: pointer;
}

.cb-11__back svg {
  inline-size: 22px;
  block-size: 22px;
}

.cb-11__head-pic {
  inline-size: 40px;
  block-size: 40px;
  border-radius: 50%;
  object-fit: cover;
  background: var(--in);
}

.cb-11__head-text {
  display: grid;
  min-inline-size: 0;
  margin-inline-end: auto;
}

.cb-11__head-text b {
  font-size: .98rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.cb-11__head-text small {
  font-size: .74rem;
  color: var(--muted);
}

.cb-11__icon {
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  flex: 0 0 auto;
  cursor: pointer;
  border: 0;
  border-radius: .8rem;
  background: transparent;
  color: var(--muted);
}

.cb-11__icon svg {
  inline-size: 21px;
  block-size: 21px;
}

.cb-11__icon:hover {
  background: var(--in);
  color: var(--ink);
}

.cb-11__msgs {
  list-style: none;
  margin: 0;
  padding: 1.1rem clamp(.9rem,4cqi,2.5rem) 1.4rem;
  display: grid;
  gap: .35rem;
  align-content: start;
  overflow-y: auto;
  overflow-x: clip;
  overflow-anchor: auto;
  scrollbar-gutter: stable;
  scrollbar-width: thin;
}

.cb-11__date {
  position: sticky;
  inset-block-start: -.2rem;
  z-index: 1;
  justify-self: center;
  margin-block: .5rem .8rem;
}

.cb-11__date span {
  display: inline-block;
  padding: .25rem .75rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--surface) 88%,var(--in));
  color: var(--muted);
  font-size: .68rem;
  font-weight: 600;
  letter-spacing: .04em;
  text-transform: uppercase;
  border: 1px solid var(--line);
  backdrop-filter: blur(8px);
}

.cb-11__turn {
  display: flex;
  margin-block-start: .15rem;
}

.cb-11__turn--out {
  justify-content: flex-end;
}

.cb-11__msg {
  margin: 0;
  max-inline-size: min(32rem,74cqi);
  padding: .65rem 1rem;
  font-size: clamp(.92rem,.25cqi + .88rem,1.02rem);
  line-height: 1.5;
  letter-spacing: -.008em;
  text-wrap: pretty;
  overflow-wrap: anywhere;
  border-radius: 1.25rem;
  background: var(--in);
  color: var(--in-ink);
  animation: cb-11-in .42s cubic-bezier(.16,1,.3,1) backwards;
}

.cb-11__turn--in .cb-11__msg {
  border-end-start-radius: .4rem;
}

.cb-11__turn--out .cb-11__msg {
  background: var(--out);
  color: var(--out-ink);
  border-end-end-radius: .4rem;
}

@keyframes cb-11-in {
  from {
    opacity: 0;
    translate: 0 8px;
    scale: .98;
  }

  to {
    opacity: 1;
    translate: 0;
    scale: 1;
  }
}

.cb-11__composer {
  display: flex;
  align-items: flex-end;
  gap: .4rem;
  padding: .7rem clamp(.9rem,4cqi,2.5rem) 1rem;
  border-block-start: 1px solid var(--line);
  background: color-mix(in oklab,var(--surface) 88%,transparent);
  backdrop-filter: blur(16px);
}

.cb-11__input {
  flex: 1;
  min-block-size: 44px;
  max-block-size: 7.5rem;
  padding: .7rem 1rem;
  resize: none;
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  background: var(--panel);
  color: var(--ink);
  font: inherit;
  font-size: .98rem;
  line-height: 1.45;
  outline: 0;
  transition: border-color .25s, background .25s;
}

@supports (field-sizing: content) {
  .cb-11__input {
    field-sizing: content;
  }
}

.cb-11__input::placeholder {
  color: var(--muted);
}

.cb-11__input:focus {
  border-color: color-mix(in oklab,var(--acc) 55%,var(--line));
  background: var(--surface);
}

.cb-11__send {
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

.cb-11__send svg {
  inline-size: 20px;
  block-size: 20px;
}

.cb-11__send:disabled {
  opacity: .3;
  cursor: not-allowed;
}

.cb-11__send:not(:disabled):hover {
  transform: scale(1.08);
}
/* ── the breakpoint: the component's own width, not the viewport's ── */

@container (max-width: 46rem) {
  .cb-11__app {
    grid-template-columns: minmax(0,1fr);
  }

  .cb-11__back {
    display: grid;
  }

  .cb-11[data-pane="list"] .cb-11__main {
    display: none;
  }

  .cb-11[data-pane="thread"] .cb-11__list {
    display: none;
  }
}
/* dark */

.cb-11[data-theme="dark"] {
  --bg: #080a0e;
  --surface: #101319;
  --panel: #0c0f14;
  --ink: #eef1f6;
  --muted: #8b94a3;
  --line: #1f242e;
  --in: #1a1f28;
  --in-ink: #eef1f6;
  --shadow: rgba(0,0,0,.75);
}

.cb-11[data-theme="dark"] .cb-11__moon {
  display: none;
}

.cb-11[data-theme="dark"] .cb-11__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .cb-11:not([data-theme="light"]) {
    --bg: #080a0e;
    --surface: #101319;
    --panel: #0c0f14;
    --ink: #eef1f6;
    --muted: #8b94a3;
    --line: #1f242e;
    --in: #1a1f28;
    --in-ink: #eef1f6;
    --shadow: rgba(0,0,0,.75);
  }

  .cb-11:not([data-theme="light"]) .cb-11__moon {
    display: none;
  }

  .cb-11:not([data-theme="light"]) .cb-11__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-11 *,
    .cb-11 *::before,
    .cb-11 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .cb-11__msg {
    border: 1px solid CanvasText;
  }

  .cb-11__convo[aria-current="true"] {
    outline: 2px solid Highlight;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.cb-11');
  if (!root) return;
  const msgs = root.querySelector('#cb-11-msgs');
  const input = root.querySelector('#cb-11-input');
  const send = root.querySelector('#cb-11-send');
  const back = root.querySelector('#cb-11-back');
  const status = root.querySelector('#cb-11-status');
  const search = root.querySelector('#cb-11-search');
  const headPic = root.querySelector('#cb-11-head-pic');
  const headName = root.querySelector('#cb-11-head-name');
  const headSub = root.querySelector('#cb-11-head-sub');

  const THREADS = {
    ana: {
      name: 'Ana Ferreira', sub: 'Active 4 minutes ago',
      pic: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=facearea&facepad=2.8&w=120&h=120&q=70',
      log: [['date', 'Monday'], ['in', 'Revised floor plan is in the shared folder — I moved the stair core two metres north.'], ['out', 'That frees the whole east wall. Does the structure still work?'], ['in', 'It does. Two extra columns in the basement, nothing above ground.'], ['date', 'Today'], ['in', 'Client sees it at two. Anything you want me to lead with?'], ['out', 'Lead with the light. The rest follows from that.']]
    },
    build: {
      name: 'Build crew', sub: '6 members · 3 unread',
      pic: 'https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=facearea&facepad=2.8&w=120&h=120&q=70',
      log: [['date', 'Today'], ['in', 'Milos: scaffolding is up on the north face.'], ['in', 'Priya: concrete pour moved to Thursday 6am — forecast is dry.'], ['in', 'Milos: we need the revised anchor spec before then.'], ['out', 'Sending it tonight. Thursday works.']]
    },
    lena: {
      name: 'Lena Brandt', sub: 'Active yesterday',
      pic: 'https://images.unsplash.com/photo-1502685104226-ee32379fefbe?auto=format&fit=facearea&facepad=2.8&w=120&h=120&q=70',
      log: [['date', 'Yesterday'], ['in', 'Can we push the walkthrough to Thursday? The joiners are a day behind.'], ['out', "Thursday afternoon is fine. Two o'clock?"], ['in', "Perfect. I'll bring the finish samples."]]
    }
  };

  const render = (id) => {
    const t = THREADS[id];
    msgs.textContent = '';
    t.log.forEach(([kind, text]) => {
      if (kind === 'date') {
        const li = document.createElement('li');
        li.className = 'cb-11__date';
        const s = document.createElement('span'); s.textContent = text;
        li.append(s); msgs.append(li);
        return;
      }
      const li = document.createElement('li');
      li.className = 'cb-11__turn cb-11__turn--' + kind;
      const p = document.createElement('p');
      p.className = 'cb-11__msg'; p.textContent = text;
      li.append(p); msgs.append(li);
    });
    headPic.src = t.pic; headName.textContent = t.name; headSub.textContent = t.sub;
    msgs.setAttribute('aria-label', 'Message history with ' + t.name);
    msgs.scrollTop = msgs.scrollHeight;
  };

  root.querySelectorAll('.cb-11__convo').forEach((btn) => {
    btn.addEventListener('click', () => {
      root.querySelectorAll('.cb-11__convo').forEach((b) => b.removeAttribute('aria-current'));
      btn.setAttribute('aria-current', 'true');
      btn.querySelector('.cb-11__pill')?.remove();
      render(btn.dataset.id);
      root.dataset.pane = 'thread';
      status.textContent = 'Opened conversation with ' + THREADS[btn.dataset.id].name;
    });
  });
  back.addEventListener('click', () => {
    root.dataset.pane = 'list';
    root.querySelector('.cb-11__convo[aria-current="true"]')?.focus();
  });

  const grow = () => {
    if (CSS.supports('field-sizing', 'content')) return;
    input.style.height = 'auto';
    input.style.height = Math.min(input.scrollHeight, 120) + 'px';
  };
  input.addEventListener('input', () => { send.disabled = !input.value.trim(); grow(); });
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send.click(); }
  });
  send.addEventListener('click', () => {
    const text = input.value.trim();
    if (!text) return;
    const li = document.createElement('li');
    li.className = 'cb-11__turn cb-11__turn--out';
    const p = document.createElement('p');
    p.className = 'cb-11__msg'; p.textContent = text;
    li.append(p); msgs.append(li);
    msgs.scrollTop = msgs.scrollHeight;          /* never scrollIntoView — it moves the page */
    input.value = ''; send.disabled = true; grow(); input.focus();
    status.textContent = 'Message sent';
  });

  /* filter the list in place */
  search.addEventListener('input', () => {
    const q = search.value.trim().toLowerCase();
    root.querySelectorAll('.cb-11__convos > li').forEach((li) => {
      li.hidden = !!q && !li.textContent.toLowerCase().includes(q);
    });
  });

  render('ana');
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.cb-11');
  const btn = root && root.querySelector('.cb-11__theme');
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
