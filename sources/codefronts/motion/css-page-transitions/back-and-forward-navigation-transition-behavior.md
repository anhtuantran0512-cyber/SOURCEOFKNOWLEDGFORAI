---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/back-and-forward-navigation-transition-behavior/"
title: "Back and Forward Navigation Transition Behavior"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "Browser back should reverse the transition, not replay it forward."
has_js: "true"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Back and Forward Navigation Transition Behavior
Source: https://codefronts.com/motion/css-page-transitions/back-and-forward-navigation-transition-behavior/

Browser back should reverse the transition, not replay it forward. A slide that moves left on navigate has to move right on back, or the user's sense of direction breaks. Direction is tracked through the history entry itself and applied to the transition as a signed custom property, with the whole stack drawn on screen so you can watch the index move.
## HTML
```html
<section class="pt-08" aria-labelledby="pt-08-h">
  <div class="pt-08__theme">
    <input class="pt-08__theme-input" type="checkbox" id="pt-08-theme">
    <label class="pt-08__theme-label" for="pt-08-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-08__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-08__stage">
    <header class="pt-08__head">
      <p class="pt-08__kicker">Page transitions / 08</p>
      <h2 class="pt-08__h" id="pt-08-h">Back reverses, forward advances</h2>
      <p class="pt-08__lede">An in-memory history stack stands in for the real one &mdash; this frame is sandboxed, so no genuine entries are pushed. Direction is read from the entry index, exactly as it would be from <code>event.state</code>.</p>
    </header>

    <div class="pt-08__chrome">
      <div class="pt-08__controls">
        <button class="pt-08__nav" type="button" data-pt-08-move="-1" aria-label="Back">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M14 6l-6 6 6 6" fill="none" stroke="currentColor" stroke-width="2"/></svg>
        </button>
        <button class="pt-08__nav" type="button" data-pt-08-move="1" aria-label="Forward">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M10 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2"/></svg>
        </button>
        <p class="pt-08__dir">dir <b data-pt-08-dir>+1</b></p>
      </div>

      <nav class="pt-08__tabs" aria-label="Project tabs">
        <button class="pt-08__tab pt-08__tab--current" type="button" data-pt-08-route="overview">Overview</button>
        <button class="pt-08__tab" type="button" data-pt-08-route="members">Members</button>
        <button class="pt-08__tab" type="button" data-pt-08-route="audit">Audit log</button>
      </nav>

      <div class="pt-08__view">
        <div class="pt-08__overlay" aria-hidden="true"></div>
        <main class="pt-08__route" id="pt-08-route" tabindex="-1">
          <h3 class="pt-08__title">Overview</h3>
          <p class="pt-08__text">Sable production workspace. Three environments, two regions, eleven collaborators.</p>
          <ul class="pt-08__kv">
            <li><b>Environment</b><span>production</span></li>
            <li><b>Region</b><span>eu-west, us-east</span></li>
            <li><b>Owner</b><span>Priya Sharma</span></li>
          </ul>
        </main>
      </div>

      <ol class="pt-08__stack" data-pt-08-stack aria-label="History stack">
        <li class="pt-08__entry pt-08__entry--current"><b>0</b><span>overview</span></li>
      </ol>
    </div>
  </div>
</section>
```
## CSS
```css
.pt-08 {
  --pt-08-bg: #0a1524;
  --pt-08-s1: #10203a;
  --pt-08-s2: #16294a;
  --pt-08-line: #24406b;
  --pt-08-ink: #e7eefb;
  --pt-08-mut: #8ea5c9;
  --pt-08-acc: #58c8f5;
  --pt-08-dir: 1;
  --pt-08-font-display: "Helvetica Neue", "Arial Narrow", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-08-bg);
  color: var(--pt-08-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.pt-08 *,
.pt-08 *::before,
.pt-08 *::after {
  box-sizing: border-box;
}

.pt-08:has(.pt-08__theme-input:checked) {
  --pt-08-bg: #f2f5fa;
  --pt-08-s1: #ffffff;
  --pt-08-s2: #e6ecf6;
  --pt-08-line: #c8d5e8;
  --pt-08-ink: #0b1626;
  --pt-08-mut: #4f6482;
  --pt-08-acc: #0b6a94;
}

@media (prefers-color-scheme: light) {
  .pt-08 {
    --pt-08-bg: #0a1524;
    --pt-08-s1: #10203a;
    --pt-08-s2: #16294a;
    --pt-08-line: #24406b;
    --pt-08-ink: #e7eefb;
    --pt-08-mut: #8ea5c9;
    --pt-08-acc: #58c8f5;
  }

  .pt-08:has(.pt-08__theme-input:checked) {
    --pt-08-bg: #f2f5fa;
    --pt-08-s1: #ffffff;
    --pt-08-s2: #e6ecf6;
    --pt-08-line: #c8d5e8;
    --pt-08-ink: #0b1626;
    --pt-08-mut: #4f6482;
    --pt-08-acc: #0b6a94;
  }
}

@media (prefers-color-scheme: dark) {
  .pt-08:has(.pt-08__theme-input:checked) {
    --pt-08-bg: #f2f5fa;
    --pt-08-s1: #ffffff;
    --pt-08-s2: #e6ecf6;
    --pt-08-line: #c8d5e8;
    --pt-08-ink: #0b1626;
    --pt-08-mut: #4f6482;
    --pt-08-acc: #0b6a94;
  }
}

@supports (color: oklch(0.8 0.12 230)) {
  .pt-08 {
    --pt-08-acc: oklch(0.82 0.11 228);
  }

  .pt-08:has(.pt-08__theme-input:checked) {
    --pt-08-acc: oklch(0.52 0.11 228);
  }

  @media (prefers-color-scheme: dark) {
    .pt-08:has(.pt-08__theme-input:checked) {
      --pt-08-acc: oklch(0.52 0.11 228);
    }
  }
}

.pt-08__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-08__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
}

.pt-08__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-08__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 0;
  border-inline-start: 1px solid var(--pt-08-line);
  border-block-end: 1px solid var(--pt-08-line);
  background: var(--pt-08-s1);
  color: var(--pt-08-mut);
  cursor: pointer;
}

.pt-08__theme-label svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.pt-08__theme-input:focus-visible + .pt-08__theme-label {
  outline: 2px solid var(--pt-08-acc);
  outline-offset: -2px;
}

.pt-08__stage {
  max-inline-size: 62rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.4rem;
}

.pt-08__kicker {
  margin: 0 0 0.45rem;
  font-family: var(--pt-08-font-display);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--pt-08-acc);
}

.pt-08__h {
  margin: 0 0 0.5rem;
  font-family: var(--pt-08-font-display);
  font-size: clamp(1.35rem, 4.4vw, 2.05rem);
  font-weight: 700;
  letter-spacing: 0.02em;
  text-transform: uppercase;
}

.pt-08__lede {
  margin: 0;
  max-inline-size: 44rem;
  color: var(--pt-08-mut);
  font-size: 0.93rem;
  text-wrap: pretty;
}

.pt-08__lede code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.86em;
}

.pt-08__chrome {
  border: 1px solid var(--pt-08-line);
}

.pt-08__controls {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.4rem;
  border-block-end: 1px solid var(--pt-08-line);
}

.pt-08__nav {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 0;
  background: transparent;
  color: var(--pt-08-mut);
  cursor: pointer;
}

.pt-08__nav svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pt-08__nav:hover:not([disabled]) {
  background: var(--pt-08-s2);
  color: var(--pt-08-ink);
}

.pt-08__nav[disabled] {
  opacity: 0.35;
  cursor: default;
}

.pt-08__nav:focus-visible {
  outline: 2px solid var(--pt-08-acc);
  outline-offset: -2px;
}

.pt-08__dir {
  margin: 0 0 0 auto;
  padding-inline-end: 3.5rem;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.76rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--pt-08-mut);
}

.pt-08__dir b {
  color: var(--pt-08-acc);
}

.pt-08__tabs {
  display: flex;
  flex-wrap: wrap;
  border-block-end: 1px solid var(--pt-08-line);
}

.pt-08__tab {
  min-block-size: 2.75rem;
  padding: 0.5rem 1rem;
  border: 0;
  border-inline-end: 1px solid var(--pt-08-line);
  background: transparent;
  color: var(--pt-08-mut);
  font-family: var(--pt-08-font-display);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  cursor: pointer;
}

.pt-08__tab--current {
  background: var(--pt-08-s2);
  color: var(--pt-08-acc);
  box-shadow: inset 0 -2px 0 var(--pt-08-acc);
}

.pt-08__tab:focus-visible {
  outline: 2px solid var(--pt-08-acc);
  outline-offset: -3px;
}

.pt-08__view {
  position: relative;
  overflow: hidden;
  min-inline-size: 0;
  min-block-size: 14rem;
  background: var(--pt-08-s1);
}

.pt-08__overlay {
  position: absolute;
  inset: 0;
  z-index: 3;
  background: var(--pt-08-bg);
  opacity: 0;
  pointer-events: none;
  transition: opacity 150ms linear;
}

.pt-08[data-pt-08-cover="1"] .pt-08__overlay {
  opacity: 0.85;
}

.pt-08__route {
  display: block;
  padding: clamp(1rem, 3vw, 1.6rem);
}

.pt-08__route:focus-visible {
  outline: 2px solid var(--pt-08-acc);
  outline-offset: -3px;
}

.pt-08[data-pt-08-phase="out"] .pt-08__route {
  transform: translateX(calc(var(--pt-08-dir) * -8%));
  opacity: 0;
  transition: transform 180ms cubic-bezier(0.4, 0, 1, 1), opacity 180ms linear;
}

.pt-08[data-pt-08-phase="in"] .pt-08__route {
  animation: pt-08-enter 260ms cubic-bezier(0, 0, 0.2, 1) both;
}

@keyframes pt-08-enter {
  from {
    transform: translateX(calc(var(--pt-08-dir) * 8%));
    opacity: 0;
  }

  to {
    transform: none;
    opacity: 1;
  }
}

.pt-08__title {
  margin: 0 0 0.6rem;
  font-family: var(--pt-08-font-display);
  font-size: 1.05rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.pt-08__text {
  margin: 0 0 0.9rem;
  max-inline-size: 40rem;
  font-size: 0.9rem;
  color: var(--pt-08-mut);
  text-wrap: pretty;
}

.pt-08__kv {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.4rem;
  max-inline-size: 34rem;
}

.pt-08__kv li {
  display: flex;
  justify-content: space-between;
  gap: 0.7rem;
  min-inline-size: 0;
  padding-block-end: 0.4rem;
  border-block-end: 1px solid var(--pt-08-line);
  font-size: 0.85rem;
}

.pt-08__kv span {
  color: var(--pt-08-mut);
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.78rem;
}

.pt-08__stack {
  list-style: none;
  margin: 0;
  padding: 0.5rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
  border-block-start: 1px solid var(--pt-08-line);
}

.pt-08__entry {
  display: flex;
  align-items: baseline;
  gap: 0.4rem;
  padding: 0.35rem 0.6rem;
  background: var(--pt-08-s2);
  font-size: 0.75rem;
  color: var(--pt-08-mut);
}

.pt-08__entry b {
  font-family: ui-monospace, Menlo, monospace;
}

.pt-08__entry--current {
  color: var(--pt-08-bg);
  background: var(--pt-08-acc);
}

@media (prefers-reduced-motion: reduce) {
  .pt-08[data-pt-08-phase="out"] .pt-08__route {
    transform: none;
    transition-duration: 60ms;
  }

  .pt-08[data-pt-08-phase="in"] .pt-08__route {
    animation: none;
  }

  .pt-08__overlay {
    transition-duration: 60ms;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.pt-08');
const view = root.querySelector('#pt-08-route');
const stackEl = root.querySelector('[data-pt-08-stack]');
const dirOut = root.querySelector('[data-pt-08-dir]');
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const pages = { overview: ['Overview', 'Sable production workspace. Three environments, two regions, eleven collaborators.', [['Environment', 'production'], ['Region', 'eu-west, us-east'], ['Owner', 'Priya Sharma']]],
  members: ['Members', 'Eleven collaborators. Two invitations are still outstanding.', [['Admins', 'Priya Sharma, Alex Chen'], ['Editors', '7'], ['Invited', 'Sam Rivera, Jordan Lee']]],
  audit: ['Audit log', 'Retained for 90 days. Exports are signed and streamed to your bucket.', [['Latest', 'role change 14:02'], ['Events today', '38'], ['Retention', '90 days']]] };
const stack = [{ i: 0, key: 'overview' }]; let index = 0; const timers = [];
function render() {
  stackEl.innerHTML = stack.map((e) => '<li class="pt-08__entry' + (e.i === index ? ' pt-08__entry--current' : '') + '"><b>' + e.i + '</b><span>' + e.key + '</span></li>').join('');
  root.querySelector('[data-pt-08-move="-1"]').disabled = index === 0;
  root.querySelector('[data-pt-08-move="1"]').disabled = index === stack.length - 1;
}
function transition(key, dir) {
  root.style.setProperty('--pt-08-dir', dir);
  dirOut.textContent = dir > 0 ? '+1' : '-1';
  root.setAttribute('data-pt-08-cover', '1'); root.setAttribute('data-pt-08-phase', 'out');
  timers.push(setTimeout(() => {
    const [title, text, kv] = pages[key];
    view.innerHTML = '<h3 class="pt-08__title">' + title + '</h3><p class="pt-08__text">' + text + '</p><ul class="pt-08__kv">' + kv.map((r) => '<li><b>' + r[0] + '</b><span>' + r[1] + '</span></li>').join('') + '</ul>';
    root.querySelectorAll('[data-pt-08-route]').forEach((t) => t.classList.toggle('pt-08__tab--current', t.getAttribute('data-pt-08-route') === key));
    view.focus({ preventScroll: true });
    root.setAttribute('data-pt-08-phase', 'in'); root.setAttribute('data-pt-08-cover', '0');
    render();
  }, reduce.matches ? 40 : 190));
}
function push(key) {
  if (stack[index].key === key) return;
  stack.length = index + 1;
  stack.push({ i: stack.length, key });
  index = stack.length - 1;
  transition(key, 1);
}
function pop(delta) {
  const next = index + delta; if (next < 0 || next > stack.length - 1) return;
  const dir = next < index ? -1 : 1; index = next;
  root.dispatchEvent(new CustomEvent('pt-08-popstate', { detail: { i: next, dir } }));
}
root.addEventListener('pt-08-popstate', (e) => transition(stack[e.detail.i].key, e.detail.dir));
root.querySelectorAll('[data-pt-08-route]').forEach((b) => b.addEventListener('click', () => push(b.getAttribute('data-pt-08-route'))));
root.querySelectorAll('[data-pt-08-move]').forEach((b) => b.addEventListener('click', () => pop(Number(b.getAttribute('data-pt-08-move')))));
render();
root.__ptCleanup = () => { timers.forEach(clearTimeout); };
```
