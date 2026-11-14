---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/pending-state-when-the-next-route-is-slow/"
title: "Pending State When the Next Route Is Slow"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "When the next route genuinely takes time, the transition needs a third state between exit and enter."
has_js: "true"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pending State When the Next Route Is Slow
Source: https://codefronts.com/motion/css-page-transitions/pending-state-when-the-next-route-is-slow/

When the next route genuinely takes time, the transition needs a third state between exit and enter. Three timings make it feel right: show nothing for the first 200ms so fast navigations never flash an indicator, show the pending state after that, and hold it for a minimum once shown so it cannot flicker. All three are labelled and adjustable, with a live region announcing the state without stealing focus.
## HTML
```html
<section class="pt-07" aria-labelledby="pt-07-h">
  <div class="pt-07__theme">
    <input class="pt-07__theme-input" type="checkbox" id="pt-07-theme">
    <label class="pt-07__theme-label" for="pt-07-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-07__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-07__stage">
    <header class="pt-07__head">
      <p class="pt-07__kicker">Page transitions / 07</p>
      <h2 class="pt-07__h" id="pt-07-h">Three timings that stop the flicker</h2>
      <p class="pt-07__lede">Pick a simulated speed, then navigate. The route swap is in-page and the network is a timer, but the thresholds are the ones you would ship.</p>
    </header>

    <div class="pt-07__cols">
      <div class="pt-07__phone">
        <div class="pt-07__notch" aria-hidden="true"></div>
        <div class="pt-07__screen">
          <div class="pt-07__overlay" aria-hidden="true">
            <span class="pt-07__dots"><i></i><i></i><i></i></span>
            <span class="pt-07__ov-t">Loading</span>
          </div>
          <main class="pt-07__route" id="pt-07-route" tabindex="-1">
            <p class="pt-07__eyebrow">Quill</p>
            <h3 class="pt-07__title">Team settings</h3>
            <ul class="pt-07__rows">
              <li><b>Members</b><span>14 active</span></li>
              <li><b>Pending invites</b><span>2</span></li>
              <li><b>Default role</b><span>Editor</span></li>
            </ul>
          </main>
          <nav class="pt-07__tabbar" aria-label="App routes">
            <button class="pt-07__tab pt-07__tab--current" type="button" data-pt-07-route="team">Team</button>
            <button class="pt-07__tab" type="button" data-pt-07-route="billing">Billing</button>
            <button class="pt-07__tab" type="button" data-pt-07-route="usage">Usage</button>
          </nav>
        </div>
      </div>

      <div class="pt-07__panel">
        <div class="pt-07__speeds" role="group" aria-label="Simulated response time">
          <button class="pt-07__speed pt-07__speed--on" type="button" data-pt-07-ms="120">120ms<span>no indicator</span></button>
          <button class="pt-07__speed" type="button" data-pt-07-ms="260">260ms<span>min display holds</span></button>
          <button class="pt-07__speed" type="button" data-pt-07-ms="2200">2.2s<span>full pending</span></button>
          <button class="pt-07__speed pt-07__speed--fail" type="button" data-pt-07-ms="fail">fail<span>terminal state</span></button>
        </div>

        <ol class="pt-07__thresholds">
          <li data-pt-07-th="delay"><b>200ms</b><span>delay before showing</span></li>
          <li data-pt-07-th="min"><b>400ms</b><span>minimum display once shown</span></li>
          <li data-pt-07-th="swap"><b>on ready</b><span>swap inside the opaque window</span></li>
        </ol>

        <p class="pt-07__live" id="pt-07-live" role="status" aria-live="polite">Idle</p>
        <p class="pt-07__log" data-pt-07-log>No navigation yet.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.pt-07 {
  --pt-07-bg: #191714;
  --pt-07-s1: #221f1b;
  --pt-07-s2: #2c2822;
  --pt-07-line: #3b3529;
  --pt-07-ink: #f3ede2;
  --pt-07-mut: #a89d8a;
  --pt-07-acc: #e0a33c;
  --pt-07-bad: #e06a4c;
  --pt-07-glass: rgba(243, 237, 226, 0.06);
  --pt-07-font-display: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-07-bg);
  color: var(--pt-07-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.pt-07 *,
.pt-07 *::before,
.pt-07 *::after {
  box-sizing: border-box;
}

.pt-07:has(.pt-07__theme-input:checked) {
  --pt-07-bg: #f7f4ef;
  --pt-07-s1: #ffffff;
  --pt-07-s2: #eee9e0;
  --pt-07-line: #ded6c8;
  --pt-07-ink: #1d1a15;
  --pt-07-mut: #6a6154;
  --pt-07-acc: #96631a;
  --pt-07-bad: #a83c22;
  --pt-07-glass: rgba(29, 26, 21, 0.05);
}

@media (prefers-color-scheme: light) {
  .pt-07 {
    --pt-07-bg: #191714;
    --pt-07-s1: #221f1b;
    --pt-07-s2: #2c2822;
    --pt-07-line: #3b3529;
    --pt-07-ink: #f3ede2;
    --pt-07-mut: #a89d8a;
    --pt-07-acc: #e0a33c;
    --pt-07-bad: #e06a4c;
    --pt-07-glass: rgba(243, 237, 226, 0.06);
  }

  .pt-07:has(.pt-07__theme-input:checked) {
    --pt-07-bg: #f7f4ef;
    --pt-07-s1: #ffffff;
    --pt-07-s2: #eee9e0;
    --pt-07-line: #ded6c8;
    --pt-07-ink: #1d1a15;
    --pt-07-mut: #6a6154;
    --pt-07-acc: #96631a;
    --pt-07-bad: #a83c22;
    --pt-07-glass: rgba(29, 26, 21, 0.05);
  }
}

@media (prefers-color-scheme: dark) {
  .pt-07:has(.pt-07__theme-input:checked) {
    --pt-07-bg: #f7f4ef;
    --pt-07-s1: #ffffff;
    --pt-07-s2: #eee9e0;
    --pt-07-line: #ded6c8;
    --pt-07-ink: #1d1a15;
    --pt-07-mut: #6a6154;
    --pt-07-acc: #96631a;
    --pt-07-bad: #a83c22;
    --pt-07-glass: rgba(29, 26, 21, 0.05);
  }
}

@supports (color: oklch(0.8 0.13 75)) {
  .pt-07 {
    --pt-07-acc: oklch(0.78 0.13 72);
  }

  .pt-07:has(.pt-07__theme-input:checked) {
    --pt-07-acc: oklch(0.52 0.11 72);
  }

  @media (prefers-color-scheme: dark) {
    .pt-07:has(.pt-07__theme-input:checked) {
      --pt-07-acc: oklch(0.52 0.11 72);
    }
  }
}

.pt-07__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-07__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
}

.pt-07__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-07__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--pt-07-line);
  border-radius: 0.9rem;
  background: var(--pt-07-glass);
  backdrop-filter: blur(8px);
  color: var(--pt-07-mut);
  cursor: pointer;
}

.pt-07__theme-label svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.pt-07__theme-input:focus-visible + .pt-07__theme-label {
  outline: 2px solid var(--pt-07-acc);
  outline-offset: 2px;
}

.pt-07__stage {
  max-inline-size: 62rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.5rem;
}

.pt-07__kicker {
  margin: 0 0 0.45rem;
  font-family: var(--pt-07-font-display);
  font-size: 0.72rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--pt-07-acc);
}

.pt-07__h {
  margin: 0 0 0.5rem;
  font-family: var(--pt-07-font-display);
  font-size: clamp(1.3rem, 4.2vw, 1.95rem);
  font-weight: 600;
  letter-spacing: -0.01em;
}

.pt-07__lede {
  margin: 0;
  max-inline-size: 42rem;
  color: var(--pt-07-mut);
  font-size: 0.93rem;
  text-wrap: pretty;
}

.pt-07__cols {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.4rem;
  align-items: start;
}

@media (min-width: 50rem) {
  .pt-07__cols {
    grid-template-columns: minmax(0, 17rem) minmax(0, 1fr);
  }
}

.pt-07__phone {
  position: relative;
  min-inline-size: 0;
  max-inline-size: 17rem;
  margin-inline: auto;
  padding: 0.55rem;
  background: var(--pt-07-s2);
  border: 1px solid var(--pt-07-line);
  border-radius: 1.9rem;
  box-shadow: 0 24px 60px -30px rgba(0, 0, 0, 0.6);
}

.pt-07__notch {
  block-size: 0.35rem;
  inline-size: 3.5rem;
  margin: 0 auto 0.45rem;
  border-radius: 999px;
  background: var(--pt-07-line);
}

.pt-07__screen {
  position: relative;
  overflow: hidden;
  block-size: 21rem;
  border-radius: 1.45rem;
  background: var(--pt-07-s1);
  display: grid;
  grid-template-rows: minmax(0, 1fr) auto;
}

.pt-07__overlay {
  position: absolute;
  inset: 0;
  z-index: 4;
  display: grid;
  place-items: center;
  gap: 0.6rem;
  align-content: center;
  background: var(--pt-07-glass);
  backdrop-filter: blur(10px);
  opacity: 0;
  pointer-events: none;
  transition: opacity 140ms linear;
}

.pt-07[data-pt-07-pending="1"] .pt-07__overlay {
  opacity: 1;
}

.pt-07__dots {
  display: flex;
  gap: 0.3rem;
}

.pt-07__dots i {
  inline-size: 0.4rem;
  block-size: 0.4rem;
  border-radius: 999px;
  background: var(--pt-07-acc);
  animation: pt-07-pulse 900ms ease-in-out infinite;
}

.pt-07__dots i:nth-child(2) {
  animation-delay: 150ms;
}

.pt-07__dots i:nth-child(3) {
  animation-delay: 300ms;
}

@keyframes pt-07-pulse {
  0%,
    100% {
    opacity: 0.3;
    transform: translateY(0);
  }

  50% {
    opacity: 1;
    transform: translateY(-0.2rem);
  }
}

.pt-07__ov-t {
  font-family: var(--pt-07-font-display);
  font-size: 0.72rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--pt-07-mut);
}

.pt-07__route {
  padding: 1rem 0.95rem;
  min-inline-size: 0;
  overflow-y: auto;
}

.pt-07__route:focus-visible {
  outline: 2px solid var(--pt-07-acc);
  outline-offset: -3px;
}

.pt-07__eyebrow {
  margin: 0 0 0.3rem;
  font-family: var(--pt-07-font-display);
  font-size: 0.66rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--pt-07-acc);
}

.pt-07__title {
  margin: 0 0 0.75rem;
  font-family: var(--pt-07-font-display);
  font-size: 1.05rem;
  font-weight: 600;
}

.pt-07__rows {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.5rem;
}

.pt-07__rows li {
  display: flex;
  justify-content: space-between;
  gap: 0.6rem;
  min-inline-size: 0;
  padding-block-end: 0.45rem;
  border-block-end: 1px solid var(--pt-07-line);
  font-size: 0.84rem;
}

.pt-07__rows span {
  color: var(--pt-07-mut);
  font-family: var(--pt-07-font-display);
  font-size: 0.78rem;
}

.pt-07__tabbar {
  display: flex;
  gap: 0.25rem;
  padding: 0.4rem;
  border-block-start: 1px solid var(--pt-07-line);
}

.pt-07__tab {
  flex: 1 1 0;
  min-inline-size: 0;
  min-block-size: 2.75rem;
  border: 0;
  border-radius: 0.7rem;
  background: transparent;
  color: var(--pt-07-mut);
  font: inherit;
  font-size: 0.78rem;
  cursor: pointer;
}

.pt-07__tab--current {
  background: var(--pt-07-s2);
  color: var(--pt-07-ink);
  font-weight: 600;
}

.pt-07__tab:focus-visible {
  outline: 2px solid var(--pt-07-acc);
  outline-offset: 2px;
}

.pt-07__panel {
  min-inline-size: 0;
  display: grid;
  gap: 0.9rem;
  align-content: start;
}

.pt-07__speeds {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.pt-07__speed {
  flex: 1 1 6.5rem;
  min-inline-size: 0;
  min-block-size: 2.75rem;
  display: grid;
  gap: 0.1rem;
  padding: 0.45rem 0.7rem;
  border: 1px solid var(--pt-07-line);
  border-radius: 0.7rem;
  background: var(--pt-07-s1);
  color: var(--pt-07-ink);
  font-family: var(--pt-07-font-display);
  font-size: 0.85rem;
  text-align: start;
  cursor: pointer;
}

.pt-07__speed span {
  font-family: system-ui, sans-serif;
  font-size: 0.68rem;
  color: var(--pt-07-mut);
}

.pt-07__speed--on {
  border-color: var(--pt-07-acc);
  color: var(--pt-07-acc);
}

.pt-07__speed--fail {
  color: var(--pt-07-bad);
}

.pt-07__speed:focus-visible {
  outline: 2px solid var(--pt-07-acc);
  outline-offset: 2px;
}

.pt-07__thresholds {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.4rem;
}

.pt-07__thresholds li {
  display: flex;
  align-items: baseline;
  gap: 0.7rem;
  padding: 0.5rem 0.7rem;
  background: var(--pt-07-s1);
  border-inline-start: 2px solid var(--pt-07-line);
}

.pt-07__thresholds li[data-pt-07-hit] {
  border-inline-start-color: var(--pt-07-acc);
}

.pt-07__thresholds b {
  font-family: var(--pt-07-font-display);
  font-size: 0.9rem;
  min-inline-size: 4.5rem;
}

.pt-07__thresholds span {
  font-size: 0.8rem;
  color: var(--pt-07-mut);
}

.pt-07__live {
  margin: 0;
  padding: 0.55rem 0.75rem;
  background: var(--pt-07-s2);
  border-radius: 0.5rem;
  font-family: var(--pt-07-font-display);
  font-size: 0.8rem;
  color: var(--pt-07-acc);
}

.pt-07__log {
  margin: 0;
  font-size: 0.8rem;
  color: var(--pt-07-mut);
}

@media (prefers-reduced-motion: reduce) {
  .pt-07__overlay {
    transition-duration: 50ms;
  }

  .pt-07__dots i {
    animation: none;
    opacity: 0.8;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.pt-07');
const view = root.querySelector('#pt-07-route');
const live = root.querySelector('#pt-07-live');
const log = root.querySelector('[data-pt-07-log]');
const DELAY = 200, MIN = 400;
const timers = []; let speed = 120; let busy = false;
const pages = { team: ['Team settings', [['Members', '14 active'], ['Pending invites', '2'], ['Default role', 'Editor']]],
  billing: ['Billing', [['Plan', 'Scale annual'], ['Next invoice', '18 Sep'], ['Seats', '14 of 25']]],
  usage: ['Usage', [['Requests', '2.1M this month'], ['Bandwidth', '840 GB'], ['Overage', 'none']]] };
const mark = (k, on) => root.querySelector('[data-pt-07-th="' + k + '"]').toggleAttribute('data-pt-07-hit', on);
async function go(key, btn) {
  if (busy) return; busy = true;
  ['delay', 'min', 'swap'].forEach((k) => mark(k, false));
  live.textContent = 'Loading ' + pages[key][0];
  let shownAt = 0;
  const pending = setTimeout(() => { root.setAttribute('data-pt-07-pending', '1'); shownAt = performance.now(); mark('delay', true); }, DELAY);
  timers.push(pending);
  const ok = speed !== 'fail';
  await new Promise((r) => timers.push(setTimeout(r, ok ? speed : 900)));
  clearTimeout(pending);
  if (!ok) { root.setAttribute('data-pt-07-pending', '0'); live.textContent = 'Could not load ' + pages[key][0]; log.textContent = 'Terminal state: overlay cleared, previous route kept, error announced politely.'; busy = false; return; }
  const held = shownAt ? Math.max(0, MIN - (performance.now() - shownAt)) : 0;
  if (held) mark('min', true);
  timers.push(setTimeout(() => {
    const [title, rows] = pages[key];
    view.innerHTML = '<p class="pt-07__eyebrow">Quill</p><h3 class="pt-07__title">' + title + '</h3><ul class="pt-07__rows">' + rows.map((r) => '<li><b>' + r[0] + '</b><span>' + r[1] + '</span></li>').join('') + '</ul>';
    root.querySelectorAll('.pt-07__tab').forEach((t) => t.classList.toggle('pt-07__tab--current', t === btn));
    root.setAttribute('data-pt-07-pending', '0'); mark('swap', true); view.focus({ preventScroll: true });
    live.textContent = title + ' loaded';
    log.textContent = shownAt ? 'Indicator shown at ' + DELAY + 'ms and held ' + MIN + 'ms minimum.' : 'Resolved in ' + speed + 'ms — under the ' + DELAY + 'ms threshold, so no indicator was shown.';
    busy = false;
  }, held));
}
root.querySelectorAll('[data-pt-07-ms]').forEach((b) => b.addEventListener('click', () => {
  speed = b.getAttribute('data-pt-07-ms') === 'fail' ? 'fail' : Number(b.getAttribute('data-pt-07-ms'));
  root.querySelectorAll('[data-pt-07-ms]').forEach((x) => x.classList.toggle('pt-07__speed--on', x === b));
}));
root.querySelectorAll('[data-pt-07-route]').forEach((b) => b.addEventListener('click', () => go(b.getAttribute('data-pt-07-route'), b)));
root.__ptCleanup = () => { timers.forEach(clearTimeout); };
```
