---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/blur-morph-transition/"
title: "Blur Page Transition Between Routes"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "Blur as the cover: the outgoing route defocuses, the swap happens at peak blur, and the incoming route sharpens."
has_js: "true"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Blur Page Transition Between Routes
Source: https://codefronts.com/motion/css-page-transitions/blur-morph-transition/

Blur as the cover: the outgoing route defocuses, the swap happens at peak blur, and the incoming route sharpens. It reads as depth of field and suits a glass interface better than any geometric effect &mdash; with an honest caveat. A filter: blur() across a full viewport is the most expensive transition in this collection, and the cost meter says so.
## HTML
```html
<section class="pt-14" aria-labelledby="pt-14-h">
  <div class="pt-14__theme">
    <input class="pt-14__theme-input" type="checkbox" id="pt-14-theme">
    <label class="pt-14__theme-label" for="pt-14-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-14__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-14__stage">
    <header class="pt-14__head">
      <p class="pt-14__kicker">Page transitions / 14</p>
      <h2 class="pt-14__h" id="pt-14-h">Defocus, swap, sharpen</h2>
      <p class="pt-14__lede">Routes are DOM sections swapped by this demo&rsquo;s script at peak blur. The meter below is honest about what this effect costs compared with a fade.</p>
    </header>

    <div class="pt-14__app">
      <nav class="pt-14__side" aria-label="Library routes">
        <p class="pt-14__side-t">Orbit</p>
        <button class="pt-14__nav pt-14__nav--current" type="button" data-pt-14-route="library">Library</button>
        <button class="pt-14__nav" type="button" data-pt-14-route="queue">Queue</button>
        <button class="pt-14__nav" type="button" data-pt-14-route="devices">Devices</button>
      </nav>

      <div class="pt-14__view">
        <div class="pt-14__blur" data-pt-14-blur>
          <main class="pt-14__route" id="pt-14-route" tabindex="-1">
            <h3 class="pt-14__title">Library</h3>
            <p class="pt-14__text">1,412 items. Sorted by last played.</p>
            <ul class="pt-14__rows">
              <li><b>Ambient sets</b><span>84 items</span></li>
              <li><b>Field recordings</b><span>212 items</span></li>
              <li><b>Live sessions</b><span>39 items</span></li>
            </ul>
          </main>
        </div>
        <div class="pt-14__overlay" aria-hidden="true"></div>
      </div>
    </div>

    <figure class="pt-14__cost">
      <figcaption class="pt-14__cost-cap">Relative cost per frame</figcaption>
      <p class="pt-14__crow"><span>opacity fade</span><span class="pt-14__cbar" style="--pt-14-w:8%"></span><span>composited only</span></p>
      <p class="pt-14__crow"><span>clip-path wipe</span><span class="pt-14__cbar" style="--pt-14-w:18%"></span><span>composited only</span></p>
      <p class="pt-14__crow pt-14__crow--hot"><span>blur 16px</span><span class="pt-14__cbar" style="--pt-14-w:88%"></span><span>convolution per frame</span></p>
      <p class="pt-14__cost-t">Radius <b data-pt-14-radius>0</b>px live. The blur sits on one wrapper, not on each route, so only one layer is promoted.</p>
    </figure>
  </div>
</section>
```
## CSS
```css
.pt-14 {
  --pt-14-bg: #060b16;
  --pt-14-s1: rgba(255, 255, 255, 0.05);
  --pt-14-s2: rgba(255, 255, 255, 0.09);
  --pt-14-line: rgba(255, 255, 255, 0.14);
  --pt-14-ink: #eaf0ff;
  --pt-14-mut: #93a4c8;
  --pt-14-acc: #6ad6ff;
  --pt-14-glow: rgba(106, 214, 255, 0.25);
  --pt-14-font-display: "Helvetica Neue", "Inter", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: #060b16;
  background-image: radial-gradient(120% 80% at 15% 0%, #12224a 0%, #060b16 60%);
  color: var(--pt-14-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.pt-14 *,
.pt-14 *::before,
.pt-14 *::after {
  box-sizing: border-box;
}

.pt-14:has(.pt-14__theme-input:checked) {
  --pt-14-bg: #eef2fa;
  --pt-14-s1: rgba(10, 20, 45, 0.05);
  --pt-14-s2: rgba(10, 20, 45, 0.09);
  --pt-14-line: rgba(10, 20, 45, 0.14);
  --pt-14-ink: #0a142d;
  --pt-14-mut: #4d5f82;
  --pt-14-acc: #0a6d99;
  --pt-14-glow: rgba(10, 109, 153, 0.18);
  background-image: radial-gradient(120% 80% at 15% 0%, #ffffff 0%, #e3ebf8 60%);
}

@media (prefers-color-scheme: light) {
  .pt-14 {
    background-image: radial-gradient(120% 80% at 15% 0%, #12224a 0%, #060b16 60%);
  }

  .pt-14:has(.pt-14__theme-input:checked) {
    --pt-14-bg: #eef2fa;
    --pt-14-s1: rgba(10, 20, 45, 0.05);
    --pt-14-s2: rgba(10, 20, 45, 0.09);
    --pt-14-line: rgba(10, 20, 45, 0.14);
    --pt-14-ink: #0a142d;
    --pt-14-mut: #4d5f82;
    --pt-14-acc: #0a6d99;
    --pt-14-glow: rgba(10, 109, 153, 0.18);
    background-image: radial-gradient(120% 80% at 15% 0%, #ffffff 0%, #e3ebf8 60%);
  }
}

@media (prefers-color-scheme: dark) {
  .pt-14:has(.pt-14__theme-input:checked) {
    --pt-14-bg: #eef2fa;
    --pt-14-s1: rgba(10, 20, 45, 0.05);
    --pt-14-s2: rgba(10, 20, 45, 0.09);
    --pt-14-line: rgba(10, 20, 45, 0.14);
    --pt-14-ink: #0a142d;
    --pt-14-mut: #4d5f82;
    --pt-14-acc: #0a6d99;
    --pt-14-glow: rgba(10, 109, 153, 0.18);
    background-image: radial-gradient(120% 80% at 15% 0%, #ffffff 0%, #e3ebf8 60%);
  }
}

@supports (color: oklch(0.8 0.12 220)) {
  .pt-14 {
    --pt-14-acc: oklch(0.84 0.11 218);
  }

  .pt-14:has(.pt-14__theme-input:checked) {
    --pt-14-acc: oklch(0.52 0.11 218);
  }

  @media (prefers-color-scheme: dark) {
    .pt-14:has(.pt-14__theme-input:checked) {
      --pt-14-acc: oklch(0.52 0.11 218);
    }
  }
}

.pt-14__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-14__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
}

.pt-14__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-14__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--pt-14-line);
  border-radius: 1rem;
  background: var(--pt-14-s2);
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
  color: var(--pt-14-acc);
  cursor: pointer;
}

.pt-14__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pt-14__theme-input:focus-visible + .pt-14__theme-label {
  outline: 2px solid var(--pt-14-acc);
  outline-offset: 2px;
}

.pt-14__stage {
  max-inline-size: 64rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.4rem;
}

.pt-14__kicker {
  margin: 0 0 0.45rem;
  font-size: 0.73rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--pt-14-acc);
}

.pt-14__h {
  margin: 0 0 0.5rem;
  font-family: var(--pt-14-font-display);
  font-size: clamp(1.4rem, 4.4vw, 2.1rem);
  font-weight: 600;
  letter-spacing: -0.025em;
}

.pt-14__lede {
  margin: 0;
  max-inline-size: 42rem;
  color: var(--pt-14-mut);
  font-size: 0.94rem;
  text-wrap: pretty;
}

.pt-14__app {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0;
  overflow: hidden;
  border: 1px solid var(--pt-14-line);
  border-radius: 1.1rem;
  background: var(--pt-14-s1);
  -webkit-backdrop-filter: blur(18px);
  backdrop-filter: blur(18px);
  box-shadow: 0 30px 80px -40px var(--pt-14-glow);
}

@media (min-width: 44rem) {
  .pt-14__app {
    grid-template-columns: 11.5rem minmax(0, 1fr);
  }
}

.pt-14__side {
  min-inline-size: 0;
  display: grid;
  gap: 0.2rem;
  align-content: start;
  padding: 0.9rem;
  border-inline-end: 1px solid var(--pt-14-line);
}

.pt-14__side-t {
  margin: 0 0 0.7rem;
  font-family: var(--pt-14-font-display);
  font-size: 0.95rem;
  font-weight: 600;
}

.pt-14__nav {
  min-block-size: 2.75rem;
  display: flex;
  align-items: center;
  padding: 0.45rem 0.65rem;
  border: 0;
  border-radius: 0.6rem;
  background: transparent;
  color: var(--pt-14-mut);
  font: inherit;
  font-size: 0.88rem;
  text-align: start;
  cursor: pointer;
}

.pt-14__nav:hover {
  background: var(--pt-14-s2);
  color: var(--pt-14-ink);
}

.pt-14__nav--current {
  background: var(--pt-14-s2);
  color: var(--pt-14-acc);
  font-weight: 600;
}

.pt-14__nav:focus-visible {
  outline: 2px solid var(--pt-14-acc);
  outline-offset: 2px;
}

.pt-14__view {
  position: relative;
  overflow: hidden;
  min-inline-size: 0;
  min-block-size: 15rem;
}

.pt-14__blur {
  block-size: 100%;
  transition: filter 200ms linear, transform 200ms ease-out;
}

.pt-14[data-pt-14-blur="1"] .pt-14__blur {
  filter: blur(16px);
  transform: scale(1.03);
  will-change: filter, transform;
}

.pt-14__overlay {
  position: absolute;
  inset: 0;
  z-index: 3;
  background: var(--pt-14-bg);
  opacity: 0;
  pointer-events: none;
  transition: opacity 200ms linear;
}

.pt-14[data-pt-14-blur="1"] .pt-14__overlay {
  opacity: 0.25;
}

.pt-14__route {
  display: block;
  padding: clamp(1rem, 3vw, 1.6rem);
}

.pt-14__route:focus-visible {
  outline: 2px solid var(--pt-14-acc);
  outline-offset: -3px;
}

.pt-14__title {
  margin: 0 0 0.35rem;
  font-family: var(--pt-14-font-display);
  font-size: 1.15rem;
  font-weight: 600;
  letter-spacing: -0.02em;
}

.pt-14__text {
  margin: 0 0 1rem;
  font-size: 0.88rem;
  color: var(--pt-14-mut);
}

.pt-14__rows {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.5rem;
  max-inline-size: 32rem;
}

.pt-14__rows li {
  display: flex;
  justify-content: space-between;
  gap: 0.6rem;
  min-inline-size: 0;
  padding: 0.55rem 0.8rem;
  background: var(--pt-14-s2);
  border-radius: 0.6rem;
  font-size: 0.87rem;
}

.pt-14__rows span {
  color: var(--pt-14-mut);
  font-variant-numeric: tabular-nums;
}

.pt-14__cost {
  margin: 0;
  padding: 0.9rem 1rem;
  border: 1px solid var(--pt-14-line);
  border-radius: 0.9rem;
  background: var(--pt-14-s1);
}

.pt-14__cost-cap {
  font-size: 0.72rem;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: var(--pt-14-mut);
  margin-block-end: 0.6rem;
}

.pt-14__crow {
  margin: 0 0 0.4rem;
  display: grid;
  grid-template-columns: minmax(0, 7rem) minmax(0, 1fr) minmax(0, 9rem);
  gap: 0.6rem;
  align-items: center;
  font-size: 0.8rem;
  color: var(--pt-14-mut);
}

.pt-14__crow--hot {
  color: var(--pt-14-ink);
}

.pt-14__cbar {
  display: block;
  block-size: 0.4rem;
  border-radius: 999px;
  background: var(--pt-14-s2);
  position: relative;
  overflow: hidden;
}

.pt-14__cbar::after {
  content: "";
  position: absolute;
  inset: 0 auto 0 0;
  inline-size: var(--pt-14-w);
  background: var(--pt-14-acc);
}

.pt-14__crow--hot .pt-14__cbar::after {
  background: linear-gradient(90deg, var(--pt-14-acc), #ff8a5c);
}

.pt-14__cost-t {
  margin: 0.7rem 0 0;
  font-size: 0.8rem;
  color: var(--pt-14-mut);
}

.pt-14__cost-t b {
  font-family: ui-monospace, Menlo, monospace;
  color: var(--pt-14-acc);
}

@media (prefers-reduced-motion: reduce) {
  .pt-14[data-pt-14-blur="1"] .pt-14__blur {
    filter: none;
    transform: none;
  }

  .pt-14__blur,
    .pt-14__overlay {
    transition-duration: 60ms;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.pt-14');
const view = root.querySelector('#pt-14-route');
const radius = root.querySelector('[data-pt-14-radius]');
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const timers = []; let busy = false;
const pages = { library: ['Library', '1,412 items. Sorted by last played.', [['Ambient sets', '84 items'], ['Field recordings', '212 items'], ['Live sessions', '39 items']]],
  queue: ['Queue', 'Four items queued, 38 minutes remaining.', [['Up next', 'Coastal drift'], ['Then', 'Harbour, 4am'], ['Source', 'Devices: studio']]],
  devices: ['Devices', 'Three devices signed in to this account.', [['Studio monitor', 'active now'], ['Phone', '2h ago'], ['Kitchen speaker', 'yesterday']]] };
function go(key, btn) {
  if (busy || btn.classList.contains('pt-14__nav--current')) return;
  busy = true;
  root.setAttribute('data-pt-14-blur', '1');
  radius.textContent = reduce.matches ? '0' : '16';
  timers.push(setTimeout(() => {
    const [title, text, rows] = pages[key];
    view.innerHTML = '<h3 class="pt-14__title">' + title + '</h3><p class="pt-14__text">' + text + '</p><ul class="pt-14__rows">' + rows.map((r) => '<li><b>' + r[0] + '</b><span>' + r[1] + '</span></li>').join('') + '</ul>';
    root.querySelectorAll('[data-pt-14-route]').forEach((n) => n.classList.toggle('pt-14__nav--current', n === btn));
    view.focus({ preventScroll: true });
    root.setAttribute('data-pt-14-blur', '0');
    radius.textContent = '0';
    timers.push(setTimeout(() => { busy = false; }, reduce.matches ? 40 : 200));
  }, reduce.matches ? 50 : 210));
}
root.querySelectorAll('[data-pt-14-route]').forEach((b) => b.addEventListener('click', () => go(b.getAttribute('data-pt-14-route'), b)));
root.__ptCleanup = () => { timers.forEach(clearTimeout); root.setAttribute('data-pt-14-blur', '0'); };
```
