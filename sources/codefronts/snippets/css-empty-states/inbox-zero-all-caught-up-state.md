---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/inbox-zero-all-caught-up-state/"
title: "Inbox Zero / All Caught Up State"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "Inbox zero in a three-pane mail client, where both panes have to say something: the list shows the cleared state with the time of the last archive, and the…"
has_js: "true"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inbox Zero / All Caught Up State
Source: https://codefronts.com/snippets/css-empty-states/inbox-zero-all-caught-up-state/

Inbox zero in a three-pane mail client, where both panes have to say something: the list shows the cleared state with the time of the last archive, and the reading pane stays quiet rather than shouting a second celebration. Undo last archive brings the thread back into both panes at once, which is the only reason a user visits this screen at all.
## HTML
```html
<div class="est-04">
  <div class="est-04__shell">
    <aside class="est-04__rail" aria-label="Mailboxes">
      <button class="est-04__compose" type="button">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 20h4l10-10-4-4L4 16z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="m14.5 5.5 4 4" stroke="currentColor" stroke-width="1.6"/></svg>
        Compose
      </button>
      <nav class="est-04__boxes">
        <a class="est-04__box est-04__box--on" href="#est-04" aria-current="page">Inbox</a>
        <a class="est-04__box" href="#est-04">Starred</a>
        <a class="est-04__box" href="#est-04">Snoozed</a>
        <a class="est-04__box" href="#est-04">Sent</a>
        <a class="est-04__box" href="#est-04">Archive</a>
      </nav>
      <div class="est-04__labels">
        <a class="est-04__label" href="#est-04"><i data-c="a" aria-hidden="true"></i>Customers</a>
        <a class="est-04__label" href="#est-04"><i data-c="b" aria-hidden="true"></i>Suppliers</a>
        <a class="est-04__label" href="#est-04"><i data-c="c" aria-hidden="true"></i>Finance</a>
      </div>
    </aside>

    <section class="est-04__list" aria-label="Inbox">
      <header class="est-04__lhead">
        <span class="est-04__lname">Inbox</span>
        <div class="est-04__lacts">
          <button class="est-04__icon" type="button" aria-label="Refresh">
            <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M19 12a7 7 0 1 1-2.6-5.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="M19 5v4h-4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
          <button class="est-04__icon" type="button" aria-label="Filter">
            <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M4 7h16M7 12h10M10 17h4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          </button>
        </div>
      </header>

      <div class="est-04__lbody" aria-live="polite">
        <div class="est-04__zero" id="est-04-zero">
          <span class="est-04__badge" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
          <p class="est-04__zh">Inbox zero</p>
          <p class="est-04__zp">Last message cleared at 09:14. Nothing new until the next sync.</p>
          <button class="est-04__undo" type="button" id="est-04-undo">Undo last archive</button>
        </div>
        <ol class="est-04__threads" id="est-04-threads" hidden>
          <li class="est-04__thread est-04__thread--on">
            <span class="est-04__avatar" aria-hidden="true">RB</span>
            <span class="est-04__tmain">
              <span class="est-04__trow"><span class="est-04__tfrom">Rosa Bianchi</span><span class="est-04__ttime">09:12</span></span>
              <span class="est-04__tsub">Re: Q3 supplier contract &mdash; signed copy</span>
              <span class="est-04__tprev">Attaching the countersigned version. One clause moved to page four&hellip;</span>
            </span>
          </li>
        </ol>
      </div>
    </section>

    <section class="est-04__reader" aria-label="Message">
      <div class="est-04__quiet" id="est-04-quiet">
        <span class="est-04__mark" aria-hidden="true"></span>
        <p class="est-04__qp">No message selected</p>
      </div>
      <article class="est-04__msg" id="est-04-msg" hidden>
        <header class="est-04__mhead">
          <h1 class="est-04__msub">Re: Q3 supplier contract &mdash; signed copy</h1>
          <div class="est-04__mfrom">
            <span class="est-04__avatar" aria-hidden="true">RB</span>
            <span class="est-04__mmeta"><b>Rosa Bianchi</b><span>to me &middot; 09:12</span></span>
          </div>
        </header>
        <div class="est-04__mbody">
          <p>Attaching the countersigned version. One clause moved to page four, everything else is as agreed on the call.</p>
          <p>If the finance team needs the original stamped copy I can courier it this week.</p>
          <p>Rosa</p>
        </div>
        <div class="est-04__mfoot">
          <button class="est-04__reply" type="button">Reply</button>
          <button class="est-04__archive" type="button" id="est-04-arch">Archive</button>
        </div>
      </article>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap');

.est-04 {
  --bg: #f4f5f6;
  --surface: #ffffff;
  --sunk: #eceef0;
  --line: #e2e5e8;
  --line-2: #d3d7dc;
  --ink: #15171a;
  --muted: #5c6167;
  --faint: #8b9098;
  --accent: #2f6f52;
  --blue: #33507d;
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

.est-04 *,
.est-04 *::before,
.est-04 *::after {
  box-sizing: border-box;
}

.est-04 [hidden] {
  display: none !important;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-04 {
    --bg: oklch(0.965 0.004 240);
    --surface: oklch(1 0 0);
    --sunk: oklch(0.945 0.005 240);
    --line: oklch(0.912 0.006 240);
    --line-2: oklch(0.862 0.008 240);
    --ink: oklch(0.18 0.008 250);
    --muted: oklch(0.47 0.012 250);
    --faint: oklch(0.635 0.013 250);
    --accent: oklch(0.5 0.085 158);
    --blue: oklch(0.42 0.075 258);
  }
}

.est-04__shell {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-columns: min(13.5rem,22vw) minmax(0,1.05fr) minmax(0,1.55fr);
}

.est-04__rail {
  display: grid;
  gap: 1.25rem;
  align-content: start;
  padding: 1rem .75rem;
  border-inline-end: 1px solid var(--line);
  background: var(--surface);
}

.est-04__compose {
  display: flex;
  align-items: center;
  gap: .5rem;
  min-block-size: 2.6rem;
  padding: .6rem .9rem;
  cursor: pointer;
  font: inherit;
  font-size: .88rem;
  font-weight: 500;
  color: var(--surface);
  background: var(--ink);
  border: 1px solid var(--ink);
  border-radius: 11px;
  transition: background .16s, translate .16s;
}

.est-04__compose svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.est-04__compose:hover {
  background: var(--blue);
  border-color: var(--blue);
  translate: 0 -1px;
}

.est-04__boxes,
.est-04__labels {
  display: grid;
  gap: .1rem;
}

.est-04__box,
.est-04__label {
  display: flex;
  align-items: center;
  gap: .55rem;
  padding: .45rem .6rem;
  border-radius: 8px;
  text-decoration: none;
  font-size: .86rem;
  color: var(--muted);
  transition: background .16s, color .16s;
}

.est-04__box:hover,
.est-04__label:hover {
  background: var(--sunk);
  color: var(--ink);
}

.est-04__box--on {
  color: var(--ink);
  font-weight: 500;
  background: var(--sunk);
  box-shadow: inset 0 0 0 1px var(--line);
}

.est-04__label i {
  inline-size: .5rem;
  block-size: .5rem;
  border-radius: 2px;
  background: var(--faint);
}

.est-04__label i[data-c="a"] {
  background: var(--blue);
}

.est-04__label i[data-c="b"] {
  background: var(--accent);
}

.est-04__label i[data-c="c"] {
  background: #b4813f;
}

.est-04__list {
  min-inline-size: 0;
  display: grid;
  grid-template-rows: auto minmax(0,1fr);
  border-inline-end: 1px solid var(--line);
  background: var(--surface);
}

.est-04__lhead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .75rem;
  padding: .85rem 1rem;
  border-block-end: 1px solid var(--line);
}

.est-04__lname {
  font-size: .92rem;
  font-weight: 600;
  letter-spacing: -.015em;
}

.est-04__lacts {
  display: flex;
  gap: .25rem;
}

.est-04__icon {
  inline-size: 2rem;
  block-size: 2rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  color: var(--faint);
  background: transparent;
  border: 1px solid transparent;
  border-radius: 8px;
  transition: color .16s, background .16s;
}

.est-04__icon svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.est-04__icon:hover {
  color: var(--ink);
  background: var(--sunk);
  border-color: var(--line);
}

.est-04__lbody {
  min-block-size: 0;
  padding: 1rem .85rem;
}

.est-04__zero {
  display: grid;
  justify-items: center;
  text-align: center;
  gap: .4rem;
  padding: clamp(1.5rem,6vh,3.5rem) 1rem;
  animation: est-04-in .5s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes est-04-in {
  from {
    opacity: 0;
    translate: 0 6px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.est-04__badge {
  position: relative;
  inline-size: 3.25rem;
  block-size: 3.25rem;
  display: grid;
  place-items: center;
  margin-block-end: .5rem;
  border-radius: 50%;
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 9%, var(--surface));
  box-shadow: 0 0 0 1px color-mix(in oklab, var(--accent) 22%, transparent);
}

.est-04__badge::after {
  content: '';
  position: absolute;
  inset: -.55rem;
  border-radius: 50%;
  border: 1px solid color-mix(in oklab, var(--accent) 26%, transparent);
  animation: est-04-breathe 5s ease-in-out infinite;
}

@keyframes est-04-breathe {
  0%,
    100% {
    opacity: .85;
    scale: 1;
  }

  50% {
    opacity: .35;
    scale: 1.06;
  }
}

.est-04__badge svg {
  inline-size: 1.35rem;
  block-size: 1.35rem;
}

.est-04__zh {
  margin: 0;
  font-size: 1.02rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.est-04__zp {
  margin: 0;
  max-inline-size: 28ch;
  font-size: .82rem;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.est-04__undo {
  margin-block-start: .7rem;
  min-block-size: 2.5rem;
  padding: .55rem .9rem;
  font: inherit;
  font-size: .82rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--line-2);
  border-radius: 10px;
  transition: background .16s, translate .16s;
}

.est-04__undo:hover {
  background: var(--sunk);
  translate: 0 -1px;
}

.est-04__threads {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .25rem;
}

.est-04__thread {
  display: grid;
  grid-template-columns: auto minmax(0,1fr);
  gap: .65rem;
  padding: .7rem .75rem;
  border-radius: 11px;
  cursor: pointer;
  background: var(--surface);
  border: 1px solid transparent;
  animation: est-04-in .4s cubic-bezier(.2,.7,.3,1) both;
}

.est-04__thread:hover {
  background: var(--sunk);
}

.est-04__thread--on {
  background: var(--sunk);
  border-color: var(--line);
}

.est-04__avatar {
  inline-size: 2rem;
  block-size: 2rem;
  display: grid;
  place-items: center;
  border-radius: 50%;
  font-size: .7rem;
  font-weight: 600;
  color: var(--surface);
  background: var(--blue);
}

.est-04__tmain {
  min-inline-size: 0;
  display: grid;
  gap: .15rem;
}

.est-04__trow {
  display: flex;
  justify-content: space-between;
  gap: .5rem;
}

.est-04__tfrom {
  font-size: .85rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.est-04__ttime {
  font-size: .72rem;
  color: var(--faint);
}

.est-04__tsub {
  font-size: .82rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.est-04__tprev {
  font-size: .78rem;
  color: var(--faint);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.est-04__reader {
  min-inline-size: 0;
  display: grid;
  background: var(--bg);
}

.est-04__quiet {
  place-self: center;
  display: grid;
  justify-items: center;
  gap: .9rem;
  padding: 2rem;
}

.est-04__mark {
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 50%;
  border: 1px dashed var(--line-2);
  background: radial-gradient(circle at 50% 50%, color-mix(in oklab, var(--ink) 8%, transparent) 0 22%, transparent 23%);
}

.est-04__qp {
  margin: 0;
  font-size: .85rem;
  color: var(--faint);
}

.est-04__msg {
  align-self: start;
  inline-size: min(44rem,100%);
  margin: clamp(1rem,3vw,2rem);
  display: grid;
  gap: 1rem;
  padding: clamp(1.25rem,3vw,2rem);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 16px;
  box-shadow: 0 1px 2px rgba(20,22,26,.04), 0 30px 60px -50px rgba(20,22,26,.5);
  animation: est-04-in .45s cubic-bezier(.2,.7,.3,1) both;
}

.est-04__mhead {
  display: grid;
  gap: .85rem;
  padding-block-end: 1rem;
  border-block-end: 1px solid var(--line);
}

.est-04__msub {
  margin: 0;
  font-size: clamp(1.1rem,2.4vw,1.4rem);
  font-weight: 600;
  letter-spacing: -.025em;
  line-height: 1.2;
  text-wrap: balance;
}

.est-04__mfrom {
  display: flex;
  align-items: center;
  gap: .6rem;
}

.est-04__mmeta {
  display: grid;
}

.est-04__mmeta b {
  font-size: .85rem;
  font-weight: 600;
}

.est-04__mmeta span {
  font-size: .76rem;
  color: var(--faint);
}

.est-04__mbody {
  display: grid;
  gap: .75rem;
}

.est-04__mbody p {
  margin: 0;
  font-size: .92rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.est-04__mfoot {
  display: flex;
  gap: .5rem;
}

.est-04__reply,
.est-04__archive {
  min-block-size: 2.6rem;
  padding: .6rem 1rem;
  font: inherit;
  font-size: .85rem;
  font-weight: 500;
  cursor: pointer;
  border-radius: 10px;
  transition: background .16s, translate .16s;
}

.est-04__reply {
  color: var(--surface);
  background: var(--ink);
  border: 1px solid var(--ink);
}

.est-04__reply:hover {
  background: var(--blue);
  border-color: var(--blue);
  translate: 0 -1px;
}

.est-04__archive {
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--line-2);
}

.est-04__archive:hover {
  background: var(--sunk);
}

.est-04__compose:focus-visible,
.est-04__icon:focus-visible,
.est-04__undo:focus-visible,
.est-04__reply:focus-visible,
.est-04__archive:focus-visible,
.est-04__box:focus-visible,
.est-04__label:focus-visible {
  outline: 2px solid var(--blue);
  outline-offset: 2px;
}

@media (max-width: 1000px) {
  .est-04__shell {
    grid-template-columns: minmax(0,1fr) minmax(0,1.4fr);
  }

  .est-04__rail {
    display: none;
  }
}

@media (max-width: 700px) {
  .est-04__shell {
    grid-template-columns: 1fr;
    grid-template-rows: auto auto;
  }

  .est-04__list {
    border-inline-end: 0;
    border-block-end: 1px solid var(--line);
  }
}

@media (prefers-reduced-motion: reduce) {
  .est-04 *,
    .est-04 *::before,
    .est-04 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-04__msg,
    .est-04__badge,
    .est-04__undo {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.est-04'); if(!root) return;
  var zero = root.querySelector('#est-04-zero'), threads = root.querySelector('#est-04-threads'),
      quiet = root.querySelector('#est-04-quiet'), msg = root.querySelector('#est-04-msg'),
      undo = root.querySelector('#est-04-undo'), arch = root.querySelector('#est-04-arch');
  function show(hasMail){
    zero.hidden = hasMail; threads.hidden = !hasMail;
    quiet.hidden = hasMail; msg.hidden = !hasMail;
  }
  undo.addEventListener('click', function(){ show(true); });
  arch.addEventListener('click', function(){ show(false); });
  show(false);
})();
```
