---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/holding-scroll-position-across-a-route-swap/"
title: "Holding Scroll Position Across a Route Swap"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "Swapping route content resets the scroll offset, which is right for a genuine navigation and wrong for a filter change or a tab switch."
has_js: "true"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Holding Scroll Position Across a Route Swap
Source: https://codefronts.com/motion/css-page-transitions/holding-scroll-position-across-a-route-swap/

Swapping route content resets the scroll offset, which is right for a genuine navigation and wrong for a filter change or a tab switch. Three behaviours a router has to tell apart, each running on the same scroll container with the offset shown live: reset to top for a new page, restore a saved offset for back and forward, and preserve exactly where the user was for an in-page swap.
## HTML
```html
<section class="pt-03" aria-labelledby="pt-03-h">
  <div class="pt-03__theme">
    <input class="pt-03__theme-input" type="checkbox" id="pt-03-theme">
    <label class="pt-03__theme-label" for="pt-03-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-03__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-03__stage">
    <header class="pt-03__head">
      <p class="pt-03__kicker">Page transitions / 03</p>
      <h2 class="pt-03__h" id="pt-03-h">Three scroll policies, one container</h2>
      <p class="pt-03__lede">Scroll the feed down, then run each policy. Routes are DOM sections swapped by this demo&rsquo;s script; the scroll offset is read from the feed container itself.</p>
    </header>

    <div class="pt-03__panel">
      <nav class="pt-03__tabs" aria-label="Scroll policies">
        <button class="pt-03__tab" type="button" data-pt-03-policy="reset">
          <span class="pt-03__tab-name">Navigate</span><span class="pt-03__tab-desc">reset to top</span>
        </button>
        <button class="pt-03__tab" type="button" data-pt-03-policy="restore">
          <span class="pt-03__tab-name">Back</span><span class="pt-03__tab-desc">restore saved offset</span>
        </button>
        <button class="pt-03__tab" type="button" data-pt-03-policy="preserve">
          <span class="pt-03__tab-name">Filter</span><span class="pt-03__tab-desc">preserve exactly</span>
        </button>
      </nav>

      <div class="pt-03__readout">
        <p class="pt-03__ro"><span class="pt-03__ro-k">scrollTop</span><span class="pt-03__ro-v" id="pt-03-now">0px</span></p>
        <p class="pt-03__ro"><span class="pt-03__ro-k">saved</span><span class="pt-03__ro-v" id="pt-03-saved">&mdash;</span></p>
        <p class="pt-03__ro"><span class="pt-03__ro-k">last policy</span><span class="pt-03__ro-v" id="pt-03-policy">idle</span></p>
      </div>

      <div class="pt-03__viewport">
        <div class="pt-03__overlay" aria-hidden="true"></div>
        <div class="pt-03__feed" id="pt-03-feed" tabindex="-1">
          <main class="pt-03__route" id="pt-03-route">
            <h3 class="pt-03__route-h" id="pt-03-route-h">Deployments</h3>
            <ul class="pt-03__cards">
              <li class="pt-03__card"><b>orbit-web</b><span>production &middot; 4m ago</span><p>Passed all checks. Promoted by Alex Chen.</p></li>
              <li class="pt-03__card"><b>orbit-api</b><span>preview &middot; 12m ago</span><p>Branch fix/session-clock. Two review comments.</p></li>
              <li class="pt-03__card"><b>talon-docs</b><span>production &middot; 1h ago</span><p>Content-only change, cache purged.</p></li>
              <li class="pt-03__card"><b>orbit-worker</b><span>failed &middot; 2h ago</span><p>Build exceeded memory. Retried once.</p></li>
              <li class="pt-03__card"><b>prism-edge</b><span>production &middot; 3h ago</span><p>Regional rollout complete in four of four.</p></li>
              <li class="pt-03__card"><b>sable-admin</b><span>preview &middot; 5h ago</span><p>Priya Sharma requested changes.</p></li>
              <li class="pt-03__card"><b>fern-jobs</b><span>production &middot; 8h ago</span><p>Queue drained before cutover.</p></li>
              <li class="pt-03__card"><b>vale-status</b><span>production &middot; 11h ago</span><p>No incidents in the last 30 days.</p></li>
            </ul>
          </main>
        </div>
      </div>
      <p class="pt-03__note">Capture happens before the swap and the write lands while the overlay is opaque, so no intermediate scroll position is ever painted.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.pt-03 {
  --pt-03-bg: #eef1ec;
  --pt-03-surf: #f9faf7;
  --pt-03-surf2: #e3e8df;
  --pt-03-line: #cbd4c6;
  --pt-03-ink: #1b241d;
  --pt-03-mut: #5a6659;
  --pt-03-acc: #2f6b47;
  --pt-03-warm: #8a6a2f;
  --pt-03-font-display: "Avenir Next", "Segoe UI", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-03-bg);
  color: var(--pt-03-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.pt-03 *,
.pt-03 *::before,
.pt-03 *::after {
  box-sizing: border-box;
}

.pt-03:has(.pt-03__theme-input:checked) {
  --pt-03-bg: #101511;
  --pt-03-surf: #172019;
  --pt-03-surf2: #1e281f;
  --pt-03-line: #2d3a2e;
  --pt-03-ink: #e9efe8;
  --pt-03-mut: #93a292;
  --pt-03-acc: #6fc48f;
  --pt-03-warm: #d9b166;
}

@media (prefers-color-scheme: dark) {
  .pt-03 {
    --pt-03-bg: #101511;
    --pt-03-surf: #172019;
    --pt-03-surf2: #1e281f;
    --pt-03-line: #2d3a2e;
    --pt-03-ink: #e9efe8;
    --pt-03-mut: #93a292;
    --pt-03-acc: #6fc48f;
    --pt-03-warm: #d9b166;
  }

  .pt-03:has(.pt-03__theme-input:checked) {
    --pt-03-bg: #eef1ec;
    --pt-03-surf: #f9faf7;
    --pt-03-surf2: #e3e8df;
    --pt-03-line: #cbd4c6;
    --pt-03-ink: #1b241d;
    --pt-03-mut: #5a6659;
    --pt-03-acc: #2f6b47;
    --pt-03-warm: #8a6a2f;
  }
}

@media (prefers-color-scheme: light) {
  .pt-03:has(.pt-03__theme-input:checked) {
    --pt-03-bg: #101511;
    --pt-03-surf: #172019;
    --pt-03-surf2: #1e281f;
    --pt-03-line: #2d3a2e;
    --pt-03-ink: #e9efe8;
    --pt-03-mut: #93a292;
    --pt-03-acc: #6fc48f;
    --pt-03-warm: #d9b166;
  }
}

@supports (color: oklch(0.5 0.1 150)) {
  .pt-03 {
    --pt-03-acc: oklch(0.48 0.1 155);
  }

  .pt-03:has(.pt-03__theme-input:checked) {
    --pt-03-acc: oklch(0.8 0.12 155);
  }

  @media (prefers-color-scheme: dark) {
    .pt-03 {
      --pt-03-acc: oklch(0.8 0.12 155);
    }

    .pt-03:has(.pt-03__theme-input:checked) {
      --pt-03-acc: oklch(0.48 0.1 155);
    }
  }
}

.pt-03__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-03__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 8;
}

.pt-03__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-03__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 0;
  border-radius: 1rem;
  background: var(--pt-03-surf2);
  color: var(--pt-03-mut);
  cursor: pointer;
}

.pt-03__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pt-03__theme-input:focus-visible + .pt-03__theme-label {
  outline: 2px solid var(--pt-03-acc);
  outline-offset: 2px;
}

.pt-03__stage {
  max-inline-size: 60rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.5rem;
}

.pt-03__kicker {
  margin: 0 0 0.5rem;
  font-size: 0.74rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--pt-03-acc);
}

.pt-03__h {
  margin: 0 0 0.55rem;
  font-family: var(--pt-03-font-display);
  font-size: clamp(1.4rem, 4.4vw, 2.1rem);
  font-weight: 600;
  letter-spacing: -0.015em;
}

.pt-03__lede {
  margin: 0;
  max-inline-size: 42rem;
  color: var(--pt-03-mut);
  font-size: 0.95rem;
  text-wrap: pretty;
}

.pt-03__panel {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0.9rem;
}

.pt-03__tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.pt-03__tab {
  flex: 1 1 8rem;
  min-inline-size: 0;
  min-block-size: 2.75rem;
  display: grid;
  gap: 0.1rem;
  padding: 0.55rem 0.8rem;
  border: 0;
  border-radius: 1rem;
  background: var(--pt-03-surf);
  color: var(--pt-03-ink);
  font: inherit;
  text-align: start;
  cursor: pointer;
}

.pt-03__tab:hover {
  background: var(--pt-03-surf2);
}

.pt-03__tab:focus-visible {
  outline: 2px solid var(--pt-03-acc);
  outline-offset: 2px;
}

.pt-03__tab-name {
  font-family: var(--pt-03-font-display);
  font-size: 0.92rem;
  font-weight: 600;
}

.pt-03__tab-desc {
  font-size: 0.74rem;
  color: var(--pt-03-mut);
}

.pt-03__readout {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem 1.5rem;
  padding: 0.7rem 0.95rem;
  background: var(--pt-03-surf);
  border-radius: 1rem;
}

.pt-03__ro {
  margin: 0;
  display: flex;
  gap: 0.5rem;
  align-items: baseline;
  min-inline-size: 0;
}

.pt-03__ro-k {
  font-size: 0.72rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--pt-03-mut);
}

.pt-03__ro-v {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--pt-03-acc);
}

.pt-03__viewport {
  position: relative;
  overflow: hidden;
  border-radius: 1.25rem;
  background: var(--pt-03-surf);
}

.pt-03__overlay {
  position: absolute;
  inset: 0;
  z-index: 3;
  background: var(--pt-03-ink);
  opacity: 0;
  pointer-events: none;
  transition: opacity 200ms linear;
}

.pt-03[data-pt-03-cover="1"] .pt-03__overlay {
  opacity: 1;
}

.pt-03__feed {
  block-size: 20rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  padding: 1rem 1.1rem 1.5rem;
}

.pt-03__feed:focus-visible {
  outline: 2px solid var(--pt-03-acc);
  outline-offset: -3px;
}

.pt-03__route-h {
  margin: 0 0 0.8rem;
  font-family: var(--pt-03-font-display);
  font-size: 1.1rem;
  font-weight: 600;
}

.pt-03__cards {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.6rem;
}

.pt-03__card {
  min-inline-size: 0;
  display: grid;
  gap: 0.2rem;
  padding: 0.75rem 0.9rem;
  background: var(--pt-03-surf2);
  border-radius: 0.85rem;
}

.pt-03__card b {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.86rem;
}

.pt-03__card span {
  font-size: 0.72rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--pt-03-warm);
}

.pt-03__card p {
  margin: 0.15rem 0 0;
  font-size: 0.86rem;
  color: var(--pt-03-mut);
}

.pt-03__note {
  margin: 0;
  font-size: 0.85rem;
  color: var(--pt-03-mut);
  max-inline-size: 46rem;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .pt-03__overlay {
    transition-duration: 60ms;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.pt-03');
const feed = root.querySelector('#pt-03-feed');
const route = root.querySelector('#pt-03-route');
const out = { now: root.querySelector('#pt-03-now'), saved: root.querySelector('#pt-03-saved'), pol: root.querySelector('#pt-03-policy') };
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const store = new Map();
const timers = [];
const titles = { reset: 'Billing', restore: 'Deployments', preserve: 'Deployments &mdash; failed only' };
const paint = () => { out.now.textContent = Math.round(feed.scrollTop) + 'px'; };
if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
feed.addEventListener('scroll', paint, { passive: true });
function apply(policy) {
  const captured = feed.scrollTop;
  store.set('deployments', captured);
  out.saved.textContent = Math.round(captured) + 'px';
  out.pol.textContent = policy;
  root.setAttribute('data-pt-03-cover', '1');
  timers.push(setTimeout(() => {
    route.querySelector('.pt-03__route-h').innerHTML = titles[policy];
    if (policy === 'reset') feed.scrollTop = 0;
    if (policy === 'restore') feed.scrollTop = Math.min(store.get('deployments') || 0, feed.scrollHeight - feed.clientHeight);
    feed.focus({ preventScroll: true });
    paint();
    root.setAttribute('data-pt-03-cover', '0');
  }, reduce.matches ? 30 : 210));
}
root.querySelectorAll('[data-pt-03-policy]').forEach((b) => b.addEventListener('click', () => apply(b.getAttribute('data-pt-03-policy'))));
paint();
root.__ptCleanup = () => { timers.forEach(clearTimeout); feed.removeEventListener('scroll', paint); };
```
