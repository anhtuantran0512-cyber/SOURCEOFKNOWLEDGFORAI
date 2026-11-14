---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/page-transition-effect/"
title: "View Transition Names and Pseudo Elements"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "The CSS surface of the View Transition API: view-transition-name on the elements that should be treated as the same thing across a DOM change, and…"
has_js: "true"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: View Transition Names and Pseudo Elements
Source: https://codefronts.com/motion/css-transition-designs/page-transition-effect/

The CSS surface of the View Transition API: view-transition-name on the elements that should be treated as the same thing across a DOM change, and ::view-transition-old() / ::view-transition-new() to style the crossfade the browser generates. A card expands into a detail panel in the same document. Covers the unique-name trap, where two elements sharing a name kill the transition silently.
## HTML
```html
<section class="trn-12" aria-labelledby="trn-12-heading">
  <div class="trn-12__stage">
    <div class="trn-12__theme">
      <input class="trn-12__themecb" type="checkbox" id="trn-12-theme">
      <label class="trn-12__themebtn" for="trn-12-theme">
        <span class="trn-12__themeico" aria-hidden="true">
          <svg class="trn-12__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-12__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-12__head">
      <p class="trn-12__kicker">view-transition-name</p>
      <h2 class="trn-12__heading" id="trn-12-heading">One element, two states, one snapshot pair</h2>
      <p class="trn-12__sub">Expand a release. The card and the panel share a name, so the browser tweens them as the same object.</p>
      <p class="trn-12__status" id="trn-12-status" role="status">View transitions: checking…</p>
    </header>

    <div class="trn-12__list" id="trn-12-list" data-open="none">
      <article class="trn-12__item" data-id="r91">
        <div class="trn-12__card" style="view-transition-name: trn-12-card-r91">
          <p class="trn-12__badge">Ranger &middot; 4.9.1</p>
          <h3 class="trn-12__title">Scheduler moved to leases</h3>
          <p class="trn-12__excerpt">Jobs now hold a 30-second lease instead of a lock, so a crashed worker no longer blocks the queue.</p>
          <button class="trn-12__more" type="button" data-trn-12-open="r91">Read release notes</button>
        </div>
      </article>

      <article class="trn-12__item" data-id="r90">
        <div class="trn-12__card" style="view-transition-name: trn-12-card-r90">
          <p class="trn-12__badge">Ranger &middot; 4.9.0</p>
          <h3 class="trn-12__title">Per-project rate limits</h3>
          <p class="trn-12__excerpt">Limits are now evaluated per project rather than per token, with a shared burst pool.</p>
          <button class="trn-12__more" type="button" data-trn-12-open="r90">Read release notes</button>
        </div>
      </article>
    </div>

    <div class="trn-12__detail" id="trn-12-detail" hidden>
      <div class="trn-12__panel" id="trn-12-panel">
        <p class="trn-12__badge" id="trn-12-dbadge">Ranger</p>
        <h3 class="trn-12__dtitle" id="trn-12-dtitle">Release</h3>
        <p class="trn-12__dbody" id="trn-12-dbody">Detail</p>
        <ul class="trn-12__facts">
          <li>Rollout: 12% of projects, expanding daily</li>
          <li>Owner: Alex Chen</li>
          <li>Rollback: single flag, no migration</li>
        </ul>
        <button class="trn-12__back" type="button" data-trn-12-close>Back to releases</button>
      </div>
    </div>

    <code class="trn-12__code">::view-transition-old(trn-12-card-r91), ::view-transition-new(trn-12-card-r91) { animation-duration: 320ms }</code>
  </div>
</section>
```
## CSS
```css
.trn-12 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #fff7fb;
  --page: oklch(0.98 0.014 340);
  --card: #ffffff;
  --ink: #1a0d18;
  --ink: oklch(0.2 0.03 340);
  --muted: #6b4f63;
  --muted: oklch(0.5 0.04 340);
  --accent: #e0197f;
  --accent: oklch(0.6 0.24 355);
  --mint: #b6f3dd;
  --mint: oklch(0.92 0.08 165);
  --lemon: #fff2a8;
  --lemon: oklch(0.95 0.11 100);
  --font-display: "Archivo", "Roboto Condensed", "Oswald", system-ui, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-12 *,
.trn-12 *::before,
.trn-12 *::after {
  box-sizing: border-box;
}

.trn-12__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(26px, 5vw, 60px) 16px;
}

.trn-12__head {
  inline-size: 100%;
  max-inline-size: 52rem;
  min-inline-size: 0;
  margin: 0 0 22px;
}

.trn-12__kicker {
  margin: 0 0 10px;
  font: 600 11.5px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.08em;
  color: var(--accent);
}

.trn-12__heading {
  margin: 0 0 10px;
  font: 700 clamp(25px, 5vw, 40px)/1.05 var(--font-display);
  letter-spacing: -0.01em;
  text-transform: uppercase;
  text-wrap: balance;
}

.trn-12__sub {
  margin: 0 0 12px;
  max-inline-size: 50ch;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-12__status {
  margin: 0;
  display: inline-block;
  padding: 5px 10px;
  background: var(--lemon);
  border-radius: 4px;
  font: 600 11.5px/1 ui-monospace, Menlo, monospace;
  color: var(--ink);
}

.trn-12__list {
  inline-size: 100%;
  max-inline-size: 52rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
  gap: 14px;
}

.trn-12__item {
  min-inline-size: 0;
}

.trn-12__card {
  min-inline-size: 0;
  block-size: 100%;
  padding: 18px;
  background: var(--card);
  border-radius: 10px;
}

.trn-12__badge {
  margin: 0 0 10px;
  display: inline-block;
  padding: 4px 9px;
  background: var(--mint);
  border-radius: 3px;
  font: 700 10.5px/1 var(--font-display);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ink);
}

.trn-12__title {
  margin: 0 0 8px;
  font: 700 19px/1.15 var(--font-display);
  letter-spacing: -0.01em;
  text-wrap: balance;
}

.trn-12__excerpt {
  margin: 0 0 14px;
  font-size: 13.5px;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-12__more,
.trn-12__back {
  min-height: 44px;
  padding: 0 16px;
  border: 0;
  border-radius: 6px;
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font: 700 12.5px/1 var(--font-display);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  transition: background-color 180ms ease, transform 180ms cubic-bezier(.2, .8, .3, 1);
}

.trn-12__more:hover,
.trn-12__back:hover {
  transform: translateY(-1px);
  background: #b31363;
}

.trn-12__more:focus-visible,
.trn-12__back:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.trn-12__detail {
  inline-size: 100%;
  max-inline-size: 52rem;
  min-inline-size: 0;
}

.trn-12__detail[hidden] {
  display: none;
}

.trn-12__panel {
  padding: 22px;
  background: var(--card);
  border-radius: 10px;
}

.trn-12__dtitle {
  margin: 0 0 10px;
  font: 700 clamp(21px, 3.6vw, 28px)/1.1 var(--font-display);
  letter-spacing: -0.01em;
  text-wrap: balance;
}

.trn-12__dbody {
  margin: 0 0 16px;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-12__facts {
  margin: 0 0 18px;
  padding: 0 0 0 18px;
  display: grid;
  gap: 7px;
  font-size: 13px;
  line-height: 1.5;
  color: var(--muted);
}

.trn-12__code {
  display: block;
  inline-size: 100%;
  max-inline-size: 52rem;
  margin-block-start: 18px;
  padding: 10px 12px;
  background: var(--card);
  border-radius: 6px;
  font: 400 11px/1.55 ui-monospace, Menlo, monospace;
  color: var(--muted);
  overflow-wrap: anywhere;
}

@supports (view-transition-name: none) {
  .trn-12__panel {
    view-transition-name: trn-12-panel;
  }

  ::view-transition-group(trn-12-card-r91),
    ::view-transition-group(trn-12-card-r90),
    ::view-transition-group(trn-12-panel) {
    animation-duration: 340ms;
    animation-timing-function: cubic-bezier(.2, .8, .3, 1);
  }

  ::view-transition-old(trn-12-card-r91),
    ::view-transition-new(trn-12-card-r91),
    ::view-transition-old(trn-12-card-r90),
    ::view-transition-new(trn-12-card-r90),
    ::view-transition-old(trn-12-panel),
    ::view-transition-new(trn-12-panel) {
    animation-duration: 320ms;
  }
}

@media (max-width: 480px) {
  .trn-12__code {
    font-size: 10px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .trn-12__more,
    .trn-12__back {
    transition: background-color 140ms ease;
  }

  .trn-12__more:hover,
    .trn-12__back:hover {
    transform: none;
  }

  @supports (view-transition-name: none) {
    ::view-transition-group(trn-12-card-r91),
        ::view-transition-group(trn-12-card-r90),
        ::view-transition-group(trn-12-panel) {
      animation-duration: 120ms;
    }
  }
}

@media (prefers-color-scheme: dark) {
  .trn-12 {
    --page: #150911;
    --page: oklch(0.18 0.03 340);
    --card: #1f0f19;
    --card: oklch(0.22 0.035 340);
    --ink: #ffe9f4;
    --ink: oklch(0.95 0.03 340);
    --muted: #c39cb2;
    --muted: oklch(0.75 0.05 340);
    --accent: #ff5ba8;
    --accent: oklch(0.73 0.2 355);
    --mint: #1f4a3d;
    --lemon: #4a4318;
  }

  .trn-12__badge {
    color: #b6f3dd;
  }

  .trn-12__status {
    color: #fff2a8;
  }

  .trn-12__more,
    .trn-12__back {
    color: #150911;
  }

  .trn-12__more:hover,
    .trn-12__back:hover {
    background: #ff8cc2;
  }
}

[data-theme="dark"] .trn-12 {
  --page: #150911;
  --card: #1f0f19;
  --ink: #ffe9f4;
  --muted: #c39cb2;
  --accent: #ff5ba8;
  --mint: #1f4a3d;
  --lemon: #4a4318;
}

[data-theme="dark"] .trn-12__badge {
  color: #b6f3dd;
}

[data-theme="dark"] .trn-12__status {
  color: #fff2a8;
}

[data-theme="dark"] .trn-12__more,
[data-theme="dark"] .trn-12__back {
  color: #150911;
}

.trn-12__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-12__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-12__themebtn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 14px;
  border: 1px solid currentColor;
  border-radius: 999px;
  cursor: pointer;
  color: var(--muted);
  font: 500 11px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  transition: color 200ms ease, opacity 200ms ease;
}

.trn-12__themebtn:hover {
  color: var(--ink);
}

.trn-12__themecb:focus-visible + .trn-12__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-12__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-12__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-12__sun {
  opacity: 1;
}

.trn-12__moon {
  opacity: 0.34;
}

.trn-12:has(#trn-12-theme:checked) .trn-12__sun {
  opacity: 0.34;
}

.trn-12:has(#trn-12-theme:checked) .trn-12__moon {
  opacity: 1;
}

@media (prefers-color-scheme: light) {
  .trn-12:has(#trn-12-theme:checked) {
    --page: #150911;
    --page: oklch(0.18 0.03 340);
    --card: #1f0f19;
    --card: oklch(0.22 0.035 340);
    --ink: #ffe9f4;
    --ink: oklch(0.95 0.03 340);
    --muted: #c39cb2;
    --muted: oklch(0.75 0.05 340);
    --accent: #ff5ba8;
    --accent: oklch(0.73 0.2 355);
    --mint: #1f4a3d;
    --lemon: #4a4318;
  }

  .trn-12:has(#trn-12-theme:checked) .trn-12__badge {
    color: #b6f3dd;
  }

  .trn-12:has(#trn-12-theme:checked) .trn-12__status {
    color: #fff2a8;
  }

  .trn-12:has(#trn-12-theme:checked) .trn-12__more,
    .trn-12:has(#trn-12-theme:checked) .trn-12__back {
    color: #150911;
  }

  .trn-12:has(#trn-12-theme:checked) .trn-12__more:hover,
    .trn-12:has(#trn-12-theme:checked) .trn-12__back:hover {
    background: #ff8cc2;
  }
}

@media (prefers-color-scheme: dark) {
  .trn-12:has(#trn-12-theme:checked) {
    --page: #fff7fb;
    --page: oklch(0.98 0.014 340);
    --card: #ffffff;
    --ink: #1a0d18;
    --ink: oklch(0.2 0.03 340);
    --muted: #6b4f63;
    --muted: oklch(0.5 0.04 340);
    --accent: #e0197f;
    --accent: oklch(0.6 0.24 355);
    --mint: #b6f3dd;
    --mint: oklch(0.92 0.08 165);
    --lemon: #fff2a8;
    --lemon: oklch(0.95 0.11 100);
    --font-display: "Archivo", "Roboto Condensed", "Oswald", system-ui, sans-serif;
    background: var(--page);
  }

  .trn-12:has(#trn-12-theme:checked) .trn-12__badge {
    margin: 0 0 10px;
    display: inline-block;
    padding: 4px 9px;
    background: var(--mint);
    border-radius: 3px;
    font: 700 10.5px/1 var(--font-display);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--ink);
  }

  .trn-12:has(#trn-12-theme:checked) .trn-12__status {
    margin: 0;
    display: inline-block;
    padding: 5px 10px;
    background: var(--lemon);
    border-radius: 4px;
    font: 600 11.5px/1 ui-monospace, Menlo, monospace;
    color: var(--ink);
  }

  .trn-12:has(#trn-12-theme:checked) .trn-12__more,
    .trn-12:has(#trn-12-theme:checked) .trn-12__back {
    min-height: 44px;
    padding: 0 16px;
    border: 0;
    border-radius: 6px;
    cursor: pointer;
    background: var(--accent);
    color: #fff;
    font: 700 12.5px/1 var(--font-display);
    letter-spacing: 0.06em;
    text-transform: uppercase;
    transition: background-color 180ms ease, transform 180ms cubic-bezier(.2, .8, .3, 1);
  }

  .trn-12:has(#trn-12-theme:checked) .trn-12__more:hover,
    .trn-12:has(#trn-12-theme:checked) .trn-12__back:hover {
    transform: translateY(-1px);
    background: #b31363;
  }

  .trn-12:has(#trn-12-theme:checked) .trn-12__sun {
    opacity: 1;
  }

  .trn-12:has(#trn-12-theme:checked) .trn-12__moon {
    opacity: 0.34;
  }
}
```

## JavaScript
```js
const trn12 = document.querySelector('.trn-12');
if (trn12) {
  const notes = { r91: ['Ranger 4.9.1', 'Scheduler moved to leases', 'A worker now renews a 30-second lease while it holds a job. If it dies, the lease expires and the job returns to the queue instead of waiting for a lock timeout.'], r90: ['Ranger 4.9.0', 'Per-project rate limits', 'Limits are evaluated per project with a shared burst pool, so one noisy token can no longer exhaust an organisation quota.'] };
  const supported = typeof document.startViewTransition === 'function';
  const swap = (fn) => supported ? document.startViewTransition(fn) : fn();
  trn12.querySelector('#trn-12-status').textContent = supported ? 'View transitions: supported — cards morph' : 'View transitions: unavailable — instant swap';
  for (const btn of trn12.querySelectorAll('[data-trn-12-open]')) {
    btn.addEventListener('click', () => swap(() => {
      const [badge, title, body] = notes[btn.getAttribute('data-trn-12-open')];
      trn12.querySelector('#trn-12-dbadge').textContent = badge;
      trn12.querySelector('#trn-12-dtitle').textContent = title;
      trn12.querySelector('#trn-12-dbody').textContent = body;
      trn12.querySelector('#trn-12-list').hidden = true;
      trn12.querySelector('#trn-12-detail').hidden = false;
    }));
  }
  trn12.querySelector('[data-trn-12-close]').addEventListener('click', () => swap(() => {
    trn12.querySelector('#trn-12-detail').hidden = true;
    trn12.querySelector('#trn-12-list').hidden = false;
  }));
}
```
