---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/offline-no-internet-connection-state/"
title: "Offline / No Internet Connection State"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "Offline as a state with inventory: the queue of unsynced edits is on screen, each row named and timestamped, so the user knows exactly what is at risk."
has_js: "true"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Offline / No Internet Connection State
Source: https://codefronts.com/snippets/css-empty-states/offline-no-internet-connection-state/

Offline as a state with inventory: the queue of unsynced edits is on screen, each row named and timestamped, so the user knows exactly what is at risk. Check connection reconnects, the sidebar light and the orb turn green, every row flips to synced in a short stagger, and the copy changes from a warning to a receipt. The reassurance is the list, not the sentence.
## HTML
```html
<div class="est-12">
  <div class="est-12__shell">
    <aside class="est-12__side">
      <span class="est-12__logo">Quill</span>
      <nav class="est-12__nav">
        <a class="est-12__nl est-12__nl--on" href="#est-12" aria-current="page">All notes</a>
        <a class="est-12__nl" href="#est-12">Shared with me</a>
        <a class="est-12__nl" href="#est-12">Templates</a>
        <a class="est-12__nl" href="#est-12">Trash</a>
      </nav>
      <div class="est-12__conn" id="est-12-conn">
        <span class="est-12__connlight" aria-hidden="true"></span>
        <span class="est-12__conntext" id="est-12-conntext">Offline</span>
      </div>
    </aside>

    <main class="est-12__main">
      <div class="est-12__stage" id="est-12-stage">
        <span class="est-12__orb" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" focusable="false">
            <path d="M4 8.5a12 12 0 0 1 16 0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
            <path d="M7 12.2a8 8 0 0 1 10 0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
            <path d="M9.8 15.8a4 4 0 0 1 4.4 0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
            <circle cx="12" cy="19" r="1.2" fill="currentColor"/>
            <path d="M3 3l18 18" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
          </svg>
        </span>
        <h1 class="est-12__h1" id="est-12-h">You are working offline</h1>
        <p class="est-12__p" id="est-12-p">Everything you type is saved on this device. Three edits are waiting to sync and nothing will be overwritten.</p>

        <ul class="est-12__queue" id="est-12-queue">
          <li class="est-12__qi"><span class="est-12__qdot" aria-hidden="true"></span><span class="est-12__qname">Q3 supplier review</span><span class="est-12__qstate">edited 4 min ago</span></li>
          <li class="est-12__qi"><span class="est-12__qdot" aria-hidden="true"></span><span class="est-12__qname">Warehouse handover</span><span class="est-12__qstate">edited 11 min ago</span></li>
          <li class="est-12__qi"><span class="est-12__qdot" aria-hidden="true"></span><span class="est-12__qname">Interview notes &mdash; Dee O.</span><span class="est-12__qstate">created offline</span></li>
        </ul>

        <div class="est-12__acts">
          <button class="est-12__pri" type="button" id="est-12-retry">Check connection</button>
          <button class="est-12__ghost" type="button">Keep writing offline</button>
        </div>
      </div>
    </main>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.est-12 {
  --bg: #f6f6f7;
  --surface: #ffffff;
  --sunk: #eeeff1;
  --line: #e4e5e8;
  --line-2: #d2d4d8;
  --ink: #17181c;
  --muted: #5b5e66;
  --faint: #8a8d95;
  --accent: #3a3d78;
  --ok: #2c6c50;
  --warn: #8a6a24;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  color-scheme: light;
  font-synthesis: none;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.est-12 *,
.est-12 *::before,
.est-12 *::after {
  box-sizing: border-box;
}

.est-12 [hidden] {
  display: none !important;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-12 {
    --bg: oklch(0.972 0.002 285);
    --surface: oklch(1 0 0);
    --sunk: oklch(0.952 0.003 285);
    --line: oklch(0.918 0.004 285);
    --line-2: oklch(0.862 0.006 285);
    --ink: oklch(0.18 0.008 280);
    --muted: oklch(0.47 0.01 280);
    --faint: oklch(0.625 0.011 280);
    --accent: oklch(0.38 0.085 280);
    --ok: oklch(0.48 0.085 158);
    --warn: oklch(0.55 0.09 80);
  }
}

.est-12__shell {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-columns: min(14rem,22vw) minmax(0,1fr);
}

.est-12__side {
  display: grid;
  grid-template-rows: auto minmax(0,1fr) auto;
  gap: 1.25rem;
  padding: 1.15rem .85rem;
  border-inline-end: 1px solid var(--line);
  background: var(--surface);
}

.est-12__logo {
  padding-inline: .4rem;
  font-size: 1.02rem;
  font-weight: 600;
  letter-spacing: -.025em;
}

.est-12__nav {
  display: grid;
  gap: .1rem;
  align-content: start;
}

.est-12__nl {
  padding: .45rem .6rem;
  border-radius: 8px;
  text-decoration: none;
  font-size: .86rem;
  color: var(--muted);
  transition: color .16s, background .16s;
}

.est-12__nl:hover {
  color: var(--ink);
  background: var(--sunk);
}

.est-12__nl--on {
  color: var(--ink);
  background: var(--sunk);
  box-shadow: inset 0 0 0 1px var(--line);
}

.est-12__conn {
  display: flex;
  align-items: center;
  gap: .5rem;
  padding: .6rem .7rem;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--sunk);
}

.est-12__connlight {
  inline-size: .5rem;
  block-size: .5rem;
  border-radius: 50%;
  background: var(--warn);
  box-shadow: 0 0 0 3px color-mix(in oklab, var(--warn) 18%, transparent);
  animation: est-12-blink 2.4s ease-in-out infinite;
}

@keyframes est-12-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .4;
  }
}

.est-12__conntext {
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .7rem;
  letter-spacing: .04em;
  color: var(--muted);
}

.est-12__conn[data-online] .est-12__connlight {
  background: var(--ok);
  box-shadow: 0 0 0 3px color-mix(in oklab, var(--ok) 18%, transparent);
  animation: none;
}

.est-12__main {
  position: relative;
  min-inline-size: 0;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3rem);
  background: radial-gradient(80% 60% at 50% 8%, color-mix(in oklab, var(--accent) 6%, transparent), transparent 60%), repeating-linear-gradient(180deg, color-mix(in oklab, var(--line) 55%, transparent) 0 1px, transparent 1px 2.25rem), var(--bg);
}

.est-12__stage {
  inline-size: min(34rem,100%);
  display: grid;
  justify-items: center;
  text-align: center;
  gap: .6rem;
  padding: clamp(1.75rem,4vw,2.75rem);
  background: color-mix(in oklab, var(--surface) 94%, transparent);
  border: 1px solid var(--line);
  border-radius: 22px;
  backdrop-filter: blur(6px);
  box-shadow: 0 1px 2px rgba(23,24,28,.04), 0 40px 80px -60px rgba(23,24,28,.55);
  animation: est-12-in .55s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes est-12-in {
  from {
    opacity: 0;
    translate: 0 10px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.est-12__orb {
  position: relative;
  inline-size: 3.75rem;
  block-size: 3.75rem;
  display: grid;
  place-items: center;
  margin-block-end: .35rem;
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 7%, var(--surface));
  border-radius: 50%;
  box-shadow: 0 0 0 1px color-mix(in oklab, var(--accent) 16%, transparent);
}

.est-12__orb svg {
  inline-size: 1.65rem;
  block-size: 1.65rem;
}

.est-12__orb::after {
  content: '';
  position: absolute;
  inset: -.5rem;
  border-radius: 50%;
  border: 1px dashed color-mix(in oklab, var(--accent) 22%, transparent);
  animation: est-12-turn 24s linear infinite;
}

@keyframes est-12-turn {
  to {
    rotate: 360deg;
  }
}

.est-12__stage[data-online] .est-12__orb {
  color: var(--ok);
  background: color-mix(in oklab, var(--ok) 8%, var(--surface));
  box-shadow: 0 0 0 1px color-mix(in oklab, var(--ok) 20%, transparent);
}

.est-12__h1 {
  margin: 0;
  font-size: clamp(1.3rem,3vw,1.8rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.15;
  text-wrap: balance;
}

.est-12__p {
  margin: 0;
  max-inline-size: 46ch;
  font-size: .92rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.est-12__queue {
  margin: .9rem 0 0;
  padding: 0;
  list-style: none;
  inline-size: 100%;
  display: grid;
  gap: .35rem;
}

.est-12__qi {
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto;
  gap: .6rem;
  align-items: center;
  text-align: start;
  padding: .65rem .8rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 11px;
}

.est-12__qdot {
  inline-size: .45rem;
  block-size: .45rem;
  border-radius: 50%;
  background: var(--warn);
}

.est-12__stage[data-online] .est-12__qdot {
  background: var(--ok);
}

.est-12__qname {
  min-inline-size: 0;
  font-size: .86rem;
  font-weight: 500;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.est-12__qstate {
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .68rem;
  color: var(--faint);
  white-space: nowrap;
}

.est-12__acts {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  justify-content: center;
  margin-block-start: 1rem;
}

.est-12__pri {
  min-block-size: 2.8rem;
  padding: .68rem 1.1rem;
  font: inherit;
  font-size: .88rem;
  font-weight: 500;
  cursor: pointer;
  color: #fff;
  background: var(--accent);
  border: 1px solid transparent;
  border-radius: 11px;
  box-shadow: 0 10px 22px -16px color-mix(in oklab, var(--accent) 80%, transparent);
  transition: translate .16s, background .16s;
}

.est-12__pri:hover {
  translate: 0 -1px;
  background: color-mix(in oklab, var(--accent) 88%, #000);
}

.est-12__pri:disabled {
  opacity: .65;
  cursor: progress;
  translate: none;
}

.est-12__ghost {
  min-block-size: 2.8rem;
  padding: .68rem 1.05rem;
  font: inherit;
  font-size: .88rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--line-2);
  border-radius: 11px;
  transition: background .16s;
}

.est-12__ghost:hover {
  background: var(--sunk);
}

.est-12__pri:focus-visible,
.est-12__ghost:focus-visible,
.est-12__nl:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 820px) {
  .est-12__shell {
    grid-template-columns: 1fr;
  }

  .est-12__side {
    grid-template-rows: auto;
    grid-template-columns: auto minmax(0,1fr) auto;
    align-items: center;
    border-inline-end: 0;
    border-block-end: 1px solid var(--line);
  }

  .est-12__nav {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .est-12 *,
    .est-12 *::before,
    .est-12 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-12__stage,
    .est-12__qi,
    .est-12__pri {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.est-12'); if(!root) return;
  var retry = root.querySelector('#est-12-retry'), stage = root.querySelector('#est-12-stage'),
      conn = root.querySelector('#est-12-conn'), conntext = root.querySelector('#est-12-conntext'),
      h = root.querySelector('#est-12-h'), p = root.querySelector('#est-12-p'),
      items = root.querySelectorAll('.est-12__qstate');
  retry.addEventListener('click', function(){
    if(stage.hasAttribute('data-online')) return;
    retry.disabled = true; retry.textContent = 'Reconnecting';
    conntext.textContent = 'Reconnecting';
    setTimeout(function(){
      stage.setAttribute('data-online',''); conn.setAttribute('data-online','');
      conntext.textContent = 'Online';
      h.textContent = 'Back online, everything synced';
      p.textContent = 'All three edits reached the server in order. Nothing needed merging.';
      items.forEach(function(el, i){ setTimeout(function(){ el.textContent = 'synced'; }, 180 * i); });
      retry.disabled = false; retry.textContent = 'Open Q3 supplier review';
    }, 1400);
  });
})();
```
