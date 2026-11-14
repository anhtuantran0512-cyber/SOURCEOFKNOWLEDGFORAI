---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/flip-element-continuity-without-the-api/"
title: "FLIP Element Continuity Without the API"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "Making one element look like it survives a route change with no View Transitions API: measure First, apply Last, Invert the difference with a transform, then…"
has_js: "true"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: FLIP Element Continuity Without the API
Source: https://codefronts.com/motion/css-page-transitions/flip-element-continuity-without-the-api/

Making one element look like it survives a route change with no View Transitions API: measure First, apply Last, Invert the difference with a transform, then Play to identity. A thumbnail grows into a detail hero, with the measured rectangles drawn on screen. This is the technique the API automates for you &mdash; knowing it by hand is what lets you ship the effect in Safari today.
## HTML
```html
<section class="pt-05" aria-labelledby="pt-05-h">
  <div class="pt-05__theme">
    <input class="pt-05__theme-input" type="checkbox" id="pt-05-theme">
    <label class="pt-05__theme-label" for="pt-05-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-05__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-05__stage">
    <header class="pt-05__head">
      <p class="pt-05__kicker">Page transitions / 05</p>
      <h2 class="pt-05__h" id="pt-05-h">First, Last, Invert, Play</h2>
      <p class="pt-05__lede">Pick a release to open its detail route. The thumbnail is the same element in both routes &mdash; only its measured rect changes. Routing is simulated in-page by this demo&rsquo;s script.</p>
    </header>

    <div class="pt-05__view">
      <div class="pt-05__overlay" aria-hidden="true"></div>

      <div class="pt-05__route" data-pt-05-route="grid">
        <h3 class="pt-05__route-h" id="pt-05-grid-h">Nova releases</h3>
        <ul class="pt-05__grid">
          <li class="pt-05__cell">
            <button class="pt-05__open" type="button" data-pt-05-open="atlas">
              <span class="pt-05__thumb pt-05__thumb--a" data-pt-05-flip="atlas" aria-hidden="true"></span>
              <span class="pt-05__cell-t">Atlas 4.2</span>
              <span class="pt-05__cell-m">Shipped &middot; 12 Aug</span>
            </button>
          </li>
          <li class="pt-05__cell">
            <button class="pt-05__open" type="button" data-pt-05-open="pulse">
              <span class="pt-05__thumb pt-05__thumb--b" data-pt-05-flip="pulse" aria-hidden="true"></span>
              <span class="pt-05__cell-t">Pulse 1.9</span>
              <span class="pt-05__cell-m">Shipped &middot; 04 Aug</span>
            </button>
          </li>
          <li class="pt-05__cell">
            <button class="pt-05__open" type="button" data-pt-05-open="relay">
              <span class="pt-05__thumb pt-05__thumb--c" data-pt-05-flip="relay" aria-hidden="true"></span>
              <span class="pt-05__cell-t">Relay 3.0</span>
              <span class="pt-05__cell-m">Beta &middot; 28 Jul</span>
            </button>
          </li>
        </ul>
      </div>

      <div class="pt-05__route" data-pt-05-route="detail" hidden>
        <button class="pt-05__back" type="button" data-pt-05-back>
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M14 6l-6 6 6 6" fill="none" stroke="currentColor" stroke-width="2"/></svg>
          All releases
        </button>
        <div class="pt-05__hero">
          <span class="pt-05__hero-img" data-pt-05-flip-target aria-hidden="true"></span>
          <div class="pt-05__hero-body">
            <h3 class="pt-05__route-h" id="pt-05-detail-h" tabindex="-1">Atlas 4.2</h3>
            <p class="pt-05__text">Session clock rewritten against the shared worker. Median cold start down 240ms across all three regions.</p>
            <p class="pt-05__meta">Alex Chen &middot; 41 commits &middot; 12 Aug</p>
          </div>
        </div>
      </div>

      <div class="pt-05__measure" data-pt-05-measure aria-hidden="true">
        <span class="pt-05__rect pt-05__rect--first" data-pt-05-first><i>First</i></span>
        <span class="pt-05__rect pt-05__rect--last" data-pt-05-last><i>Last</i></span>
      </div>
    </div>

    <dl class="pt-05__nums">
      <div><dt>translate</dt><dd data-pt-05-out="t">&mdash;</dd></div>
      <div><dt>scale</dt><dd data-pt-05-out="s">&mdash;</dd></div>
      <div><dt>read order</dt><dd data-pt-05-out="o">idle</dd></div>
    </dl>
  </div>
</section>
```
## CSS
```css
.pt-05 {
  --pt-05-bg: #050506;
  --pt-05-s1: #0e0f12;
  --pt-05-s2: #16181d;
  --pt-05-line: #24272f;
  --pt-05-ink: #f2f4f7;
  --pt-05-mut: #8e95a3;
  --pt-05-acc: #c8f24a;
  --pt-05-acc2: #7a8ef0;
  --pt-05-font-display: "Helvetica Neue", "Inter", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-05-bg);
  color: var(--pt-05-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.pt-05 *,
.pt-05 *::before,
.pt-05 *::after {
  box-sizing: border-box;
}

.pt-05:has(.pt-05__theme-input:checked) {
  --pt-05-bg: #f4f5f7;
  --pt-05-s1: #ffffff;
  --pt-05-s2: #ebedf1;
  --pt-05-line: #d5d9e0;
  --pt-05-ink: #0c0d10;
  --pt-05-mut: #5d6472;
  --pt-05-acc: #5d7a00;
  --pt-05-acc2: #3a4bc8;
}

@media (prefers-color-scheme: light) {
  .pt-05 {
    --pt-05-bg: #050506;
    --pt-05-s1: #0e0f12;
    --pt-05-s2: #16181d;
    --pt-05-line: #24272f;
    --pt-05-ink: #f2f4f7;
    --pt-05-mut: #8e95a3;
    --pt-05-acc: #c8f24a;
    --pt-05-acc2: #7a8ef0;
  }

  .pt-05:has(.pt-05__theme-input:checked) {
    --pt-05-bg: #f4f5f7;
    --pt-05-s1: #ffffff;
    --pt-05-s2: #ebedf1;
    --pt-05-line: #d5d9e0;
    --pt-05-ink: #0c0d10;
    --pt-05-mut: #5d6472;
    --pt-05-acc: #5d7a00;
    --pt-05-acc2: #3a4bc8;
  }
}

@media (prefers-color-scheme: dark) {
  .pt-05:has(.pt-05__theme-input:checked) {
    --pt-05-bg: #f4f5f7;
    --pt-05-s1: #ffffff;
    --pt-05-s2: #ebedf1;
    --pt-05-line: #d5d9e0;
    --pt-05-ink: #0c0d10;
    --pt-05-mut: #5d6472;
    --pt-05-acc: #5d7a00;
    --pt-05-acc2: #3a4bc8;
  }
}

@supports (color: oklch(0.9 0.2 120)) {
  .pt-05 {
    --pt-05-acc: oklch(0.9 0.2 118);
  }

  .pt-05:has(.pt-05__theme-input:checked) {
    --pt-05-acc: oklch(0.55 0.15 118);
  }

  @media (prefers-color-scheme: dark) {
    .pt-05:has(.pt-05__theme-input:checked) {
      --pt-05-acc: oklch(0.55 0.15 118);
    }
  }
}

.pt-05__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-05__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
}

.pt-05__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-05__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 0;
  border-radius: 0.75rem;
  background: var(--pt-05-s2);
  color: var(--pt-05-mut);
  cursor: pointer;
  box-shadow: 0 0 0 1px var(--pt-05-line), 0 8px 28px -14px var(--pt-05-acc);
}

.pt-05__theme-label svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.pt-05__theme-input:focus-visible + .pt-05__theme-label {
  outline: 2px solid var(--pt-05-acc);
  outline-offset: 2px;
}

.pt-05__stage {
  max-inline-size: 64rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.4rem;
}

.pt-05__kicker {
  margin: 0 0 0.5rem;
  font-size: 0.72rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--pt-05-acc);
}

.pt-05__h {
  margin: 0 0 0.55rem;
  font-family: var(--pt-05-font-display);
  font-size: clamp(1.45rem, 4.6vw, 2.25rem);
  font-weight: 700;
  letter-spacing: -0.025em;
}

.pt-05__lede {
  margin: 0;
  max-inline-size: 44rem;
  color: var(--pt-05-mut);
  font-size: 0.95rem;
  text-wrap: pretty;
}

.pt-05__view {
  position: relative;
  overflow: hidden;
  min-inline-size: 0;
  min-block-size: 22rem;
  background: var(--pt-05-s1);
  border-radius: 1.1rem;
  box-shadow: 0 0 0 1px var(--pt-05-line), 0 30px 70px -40px var(--pt-05-acc2);
}

.pt-05__overlay {
  position: absolute;
  inset: 0;
  z-index: 4;
  background: var(--pt-05-bg);
  opacity: 0;
  pointer-events: none;
  transition: opacity 160ms linear;
}

.pt-05[data-pt-05-cover="1"] .pt-05__overlay {
  opacity: 0.72;
}

.pt-05__route {
  padding: clamp(1rem, 3vw, 1.6rem);
}

.pt-05__route[hidden] {
  display: none;
}

.pt-05__route-h {
  margin: 0 0 0.9rem;
  font-family: var(--pt-05-font-display);
  font-size: 1.1rem;
  font-weight: 700;
  letter-spacing: -0.01em;
}

.pt-05__route-h:focus-visible {
  outline: 2px solid var(--pt-05-acc);
  outline-offset: 3px;
}

.pt-05__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0.75rem;
}

@media (min-width: 34rem) {
  .pt-05__grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

.pt-05__cell {
  min-inline-size: 0;
}

.pt-05__open {
  inline-size: 100%;
  min-block-size: 2.75rem;
  display: grid;
  gap: 0.4rem;
  padding: 0.75rem;
  border: 0;
  border-radius: 0.9rem;
  background: var(--pt-05-s2);
  color: var(--pt-05-ink);
  font: inherit;
  text-align: start;
  cursor: pointer;
}

.pt-05__open:hover {
  box-shadow: 0 0 0 1px var(--pt-05-acc);
}

.pt-05__open:focus-visible {
  outline: 2px solid var(--pt-05-acc);
  outline-offset: 2px;
}

.pt-05__thumb {
  display: block;
  block-size: 4.5rem;
  border-radius: 0.6rem;
}

.pt-05__thumb--a {
  background: linear-gradient(135deg, #c8f24a, #2f6f4a);
}

.pt-05__thumb--b {
  background: linear-gradient(135deg, #7a8ef0, #2b2f6b);
}

.pt-05__thumb--c {
  background: linear-gradient(135deg, #f0a07a, #6b2f2f);
}

.pt-05__cell-t {
  font-weight: 600;
  font-size: 0.92rem;
}

.pt-05__cell-m {
  font-size: 0.75rem;
  color: var(--pt-05-mut);
}

.pt-05__back {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  min-block-size: 2.75rem;
  margin-block-end: 0.8rem;
  padding: 0.4rem 0.8rem 0.4rem 0.5rem;
  border: 0;
  border-radius: 999px;
  background: var(--pt-05-s2);
  color: var(--pt-05-ink);
  font: inherit;
  font-size: 0.85rem;
  cursor: pointer;
}

.pt-05__back svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.pt-05__back:focus-visible {
  outline: 2px solid var(--pt-05-acc);
  outline-offset: 2px;
}

.pt-05__hero {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1rem;
}

@media (min-width: 40rem) {
  .pt-05__hero {
    grid-template-columns: minmax(0, 14rem) minmax(0, 1fr);
  }
}

.pt-05__hero-img {
  display: block;
  block-size: 10rem;
  border-radius: 0.9rem;
  background: linear-gradient(135deg, #c8f24a, #2f6f4a);
}

.pt-05__hero-body {
  min-inline-size: 0;
}

.pt-05__text {
  margin: 0 0 0.6rem;
  font-size: 0.92rem;
  color: var(--pt-05-mut);
  text-wrap: pretty;
}

.pt-05__meta {
  margin: 0;
  font-size: 0.76rem;
  color: var(--pt-05-mut);
  opacity: 0.8;
}

.pt-05__measure {
  position: absolute;
  inset: 0;
  z-index: 5;
  pointer-events: none;
}

.pt-05__rect {
  position: absolute;
  display: none;
  border: 1px dashed var(--pt-05-acc);
  border-radius: 0.5rem;
}

.pt-05__rect i {
  position: absolute;
  inset-block-start: -1.15rem;
  inset-inline-start: 0;
  font-size: 0.62rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  font-style: normal;
  color: var(--pt-05-acc);
}

.pt-05__rect--last {
  border-style: solid;
  border-color: var(--pt-05-acc2);
}

.pt-05__rect--last i {
  color: var(--pt-05-acc2);
}

.pt-05[data-pt-05-measured="1"] .pt-05__rect {
  display: block;
}

.pt-05__nums {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1.75rem;
}

.pt-05__nums div {
  min-inline-size: 0;
}

.pt-05__nums dt {
  font-size: 0.68rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--pt-05-mut);
}

.pt-05__nums dd {
  margin: 0.1rem 0 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.84rem;
  color: var(--pt-05-acc);
}

@media (prefers-reduced-motion: reduce) {
  .pt-05__overlay {
    transition-duration: 40ms;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.pt-05');
const routes = { grid: root.querySelector('[data-pt-05-route="grid"]'), detail: root.querySelector('[data-pt-05-route="detail"]') };
const target = root.querySelector('[data-pt-05-flip-target]');
const out = (k, v) => { root.querySelector('[data-pt-05-out="' + k + '"]').textContent = v; };
const box = (el, node) => { const b = el.getBoundingClientRect(), p = root.querySelector('.pt-05__view').getBoundingClientRect();
  Object.assign(node.style, { inset: (b.top - p.top) + 'px auto auto ' + (b.left - p.left) + 'px', width: b.width + 'px', height: b.height + 'px' }); return b; };
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const timers = [];
function open(key, btn) {
  const thumb = btn.querySelector('[data-pt-05-flip]');
  const first = box(thumb, root.querySelector('[data-pt-05-first]'));
  routes.grid.hidden = true; routes.detail.hidden = false;
  root.querySelector('#pt-05-detail-h').textContent = btn.querySelector('.pt-05__cell-t').textContent;
  target.style.background = getComputedStyle(thumb).backgroundImage;
  const last = box(target, root.querySelector('[data-pt-05-last]'));
  root.setAttribute('data-pt-05-measured', '1');
  const dx = first.left - last.left, dy = first.top - last.top, sx = first.width / last.width, sy = first.height / last.height;
  out('t', Math.round(dx) + 'px, ' + Math.round(dy) + 'px'); out('s', sx.toFixed(2) + ', ' + sy.toFixed(2)); out('o', 'first then last, same task');
  if (!reduce.matches && target.animate) target.animate(
    [{ transformOrigin: 'top left', transform: 'translate(' + dx + 'px,' + dy + 'px) scale(' + sx + ',' + sy + ')' }, { transformOrigin: 'top left', transform: 'none' }],
    { duration: 420, easing: 'cubic-bezier(0.2, 0.9, 0.25, 1)' });
  root.querySelector('#pt-05-detail-h').focus({ preventScroll: true });
  timers.push(setTimeout(() => { root.setAttribute('data-pt-05-measured', '0'); }, 900));
}
function back() { routes.detail.hidden = true; routes.grid.hidden = false; out('o', 'idle'); root.querySelector('[data-pt-05-open]').focus({ preventScroll: true }); }
root.querySelectorAll('[data-pt-05-open]').forEach((b) => b.addEventListener('click', () => open(b.getAttribute('data-pt-05-open'), b)));
root.querySelector('[data-pt-05-back]').addEventListener('click', back);
root.__ptCleanup = () => { timers.forEach(clearTimeout); };
```
