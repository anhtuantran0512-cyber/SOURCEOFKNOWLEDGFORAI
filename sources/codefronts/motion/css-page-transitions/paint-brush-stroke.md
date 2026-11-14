---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/paint-brush-stroke/"
title: "Brush Stroke Page Transition Mask"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "An SVG mask carries a thick, tapered brush path; animating its stroke-dashoffset paints the mask on, which sweeps the overlay across the viewport as a single…"
has_js: "true"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brush Stroke Page Transition Mask
Source: https://codefronts.com/motion/css-page-transitions/paint-brush-stroke/

An SVG mask carries a thick, tapered brush path; animating its stroke-dashoffset paints the mask on, which sweeps the overlay across the viewport as a single stroke and then lifts it the same way. Higher fidelity than the radial bleed in demo 16, and the place where namespacing matters most &mdash; SVG mask ids are document-global, so two demos both defining one means the second silently wins.
## HTML
```html
<section class="pt-20" aria-labelledby="pt-20-h">
  <div class="pt-20__theme">
    <input class="pt-20__theme-input" type="checkbox" id="pt-20-theme">
    <label class="pt-20__theme-label" for="pt-20-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-20__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-20__stage">
    <header class="pt-20__head">
      <p class="pt-20__kicker">Page transitions / 20</p>
      <h2 class="pt-20__h" id="pt-20-h">One stroke, painted and lifted</h2>
      <p class="pt-20__lede">Rooms are DOM sections swapped by this demo&rsquo;s script at full coverage. The mask id is namespaced <code>pt-20-brush-mask</code> because SVG ids are shared across the whole document.</p>
    </header>

    <div class="pt-20__frame">
      <div class="pt-20__view">
        <svg class="pt-20__brush" viewBox="0 0 800 400" preserveAspectRatio="none" aria-hidden="true" focusable="false">
          <defs>
            <mask id="pt-20-brush-mask" maskUnits="userSpaceOnUse" x="0" y="0" width="800" height="400">
              <path class="pt-20__stroke" d="M-120 150 C 140 40, 300 330, 520 190 S 760 60, 940 210" pathLength="1" fill="none" stroke="#fff" stroke-width="420" stroke-linecap="round"/>
            </mask>
          </defs>
          <rect class="pt-20__paint" x="0" y="0" width="800" height="400" mask="url(#pt-20-brush-mask)"/>
        </svg>

        <main class="pt-20__room" id="pt-20-room" tabindex="-1">
          <p class="pt-20__eyebrow">Room 1 &middot; Ground floor</p>
          <h3 class="pt-20__title">Marks and Weather</h3>
          <p class="pt-20__text">Twenty-two works on paper made outdoors between 1962 and 1971. Hung in the order they were painted.</p>
          <dl class="pt-20__facts">
            <div><dt>Works</dt><dd>22</dd></div>
            <div><dt>Medium</dt><dd>Ink, gouache</dd></div>
            <div><dt>Until</dt><dd>30 Nov</dd></div>
          </dl>
        </main>
      </div>

      <nav class="pt-20__rooms" aria-label="Rooms">
        <button class="pt-20__room-btn pt-20__room-btn--current" type="button" data-pt-20-room="one">Room 1</button>
        <button class="pt-20__room-btn" type="button" data-pt-20-room="two">Room 2</button>
        <button class="pt-20__room-btn" type="button" data-pt-20-room="three">Room 3</button>
      </nav>
    </div>
  </div>
</section>
```
## CSS
```css
.pt-20 {
  --pt-20-bg: #f4f1ea;
  --pt-20-s1: #fdfbf6;
  --pt-20-s2: #eae5da;
  --pt-20-line: #d5cec0;
  --pt-20-ink: #191713;
  --pt-20-mut: #6a6255;
  --pt-20-acc: #c2431f;
  --pt-20-font-display: "Rockwell", "Roboto Slab", "Bookman Old Style", Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-20-bg);
  background-image: radial-gradient(rgba(25, 23, 19, 0.03) 1px, transparent 1px);
  background-size: 3px 3px;
  color: var(--pt-20-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.6;
}

.pt-20 *,
.pt-20 *::before,
.pt-20 *::after {
  box-sizing: border-box;
}

.pt-20:has(.pt-20__theme-input:checked) {
  --pt-20-bg: #141210;
  --pt-20-s1: #1c1a16;
  --pt-20-s2: #24211c;
  --pt-20-line: #363128;
  --pt-20-ink: #f3efe6;
  --pt-20-mut: #a69d8d;
  --pt-20-acc: #ef7a4f;
  background-image: radial-gradient(rgba(243, 239, 230, 0.035) 1px, transparent 1px);
}

@media (prefers-color-scheme: dark) {
  .pt-20 {
    --pt-20-bg: #141210;
    --pt-20-s1: #1c1a16;
    --pt-20-s2: #24211c;
    --pt-20-line: #363128;
    --pt-20-ink: #f3efe6;
    --pt-20-mut: #a69d8d;
    --pt-20-acc: #ef7a4f;
    background-image: radial-gradient(rgba(243, 239, 230, 0.035) 1px, transparent 1px);
  }

  .pt-20:has(.pt-20__theme-input:checked) {
    --pt-20-bg: #f4f1ea;
    --pt-20-s1: #fdfbf6;
    --pt-20-s2: #eae5da;
    --pt-20-line: #d5cec0;
    --pt-20-ink: #191713;
    --pt-20-mut: #6a6255;
    --pt-20-acc: #c2431f;
    background-image: radial-gradient(rgba(25, 23, 19, 0.03) 1px, transparent 1px);
  }
}

@media (prefers-color-scheme: light) {
  .pt-20:has(.pt-20__theme-input:checked) {
    --pt-20-bg: #141210;
    --pt-20-s1: #1c1a16;
    --pt-20-s2: #24211c;
    --pt-20-line: #363128;
    --pt-20-ink: #f3efe6;
    --pt-20-mut: #a69d8d;
    --pt-20-acc: #ef7a4f;
    background-image: radial-gradient(rgba(243, 239, 230, 0.035) 1px, transparent 1px);
  }
}

@supports (color: oklch(0.55 0.17 35)) {
  .pt-20 {
    --pt-20-acc: oklch(0.55 0.17 36);
  }

  .pt-20:has(.pt-20__theme-input:checked) {
    --pt-20-acc: oklch(0.73 0.14 42);
  }

  @media (prefers-color-scheme: dark) {
    .pt-20 {
      --pt-20-acc: oklch(0.73 0.14 42);
    }

    .pt-20:has(.pt-20__theme-input:checked) {
      --pt-20-acc: oklch(0.55 0.17 36);
    }
  }
}

.pt-20__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-20__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
}

.pt-20__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-20__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--pt-20-line);
  border-radius: 0.3rem;
  background: var(--pt-20-s1);
  color: var(--pt-20-acc);
  cursor: pointer;
}

.pt-20__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pt-20__theme-input:focus-visible + .pt-20__theme-label {
  outline: 2px solid var(--pt-20-acc);
  outline-offset: 2px;
}

.pt-20__stage {
  max-inline-size: 62rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.5rem;
}

.pt-20__kicker {
  margin: 0 0 0.45rem;
  font-family: var(--pt-20-font-display);
  font-size: 0.76rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--pt-20-acc);
}

.pt-20__h {
  margin: 0 0 0.5rem;
  font-family: var(--pt-20-font-display);
  font-size: clamp(1.5rem, 4.8vw, 2.3rem);
  font-weight: 700;
  letter-spacing: -0.015em;
}

.pt-20__lede {
  margin: 0;
  max-inline-size: 42rem;
  color: var(--pt-20-mut);
  font-size: 0.94rem;
  text-wrap: pretty;
}

.pt-20__lede code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.86em;
}

.pt-20__frame {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0.9rem;
}

.pt-20__view {
  position: relative;
  overflow: hidden;
  min-inline-size: 0;
  min-block-size: 17rem;
  background: var(--pt-20-s1);
  border: 1px solid var(--pt-20-line);
}

.pt-20__brush {
  position: absolute;
  inset: 0;
  z-index: 3;
  inline-size: 100%;
  block-size: 100%;
  pointer-events: none;
}

.pt-20__paint {
  fill: var(--pt-20-acc);
}

.pt-20__stroke {
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
}

.pt-20[data-pt-20-phase="paint"] .pt-20__stroke {
  animation: pt-20-paint 420ms cubic-bezier(0.5, 0, 0.4, 1) both;
}

.pt-20[data-pt-20-phase="lift"] .pt-20__stroke {
  animation: pt-20-lift 460ms cubic-bezier(0.5, 0, 0.4, 1) both;
}

@keyframes pt-20-paint {
  from {
    stroke-dashoffset: 1;
  }

  to {
    stroke-dashoffset: 0;
  }
}

@keyframes pt-20-lift {
  from {
    stroke-dashoffset: 0;
  }

  to {
    stroke-dashoffset: -1;
  }
}

.pt-20__room {
  display: block;
  padding: clamp(1.1rem, 3.5vw, 2rem);
}

.pt-20__room:focus-visible {
  outline: 2px solid var(--pt-20-acc);
  outline-offset: -4px;
}

.pt-20__eyebrow {
  margin: 0 0 0.5rem;
  font-size: 0.74rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--pt-20-mut);
}

.pt-20__title {
  margin: 0 0 0.7rem;
  font-family: var(--pt-20-font-display);
  font-size: clamp(1.35rem, 4.4vw, 2rem);
  font-weight: 700;
  letter-spacing: -0.02em;
}

.pt-20__text {
  margin: 0 0 1.1rem;
  max-inline-size: 34rem;
  font-size: 0.95rem;
  color: var(--pt-20-mut);
  text-wrap: pretty;
}

.pt-20__facts {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem 2rem;
}

.pt-20__facts div {
  min-inline-size: 0;
}

.pt-20__facts dt {
  font-size: 0.7rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--pt-20-mut);
}

.pt-20__facts dd {
  margin: 0.1rem 0 0;
  font-family: var(--pt-20-font-display);
  font-size: 1rem;
  font-weight: 700;
}

.pt-20__rooms {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.pt-20__room-btn {
  flex: 1 1 7rem;
  min-inline-size: 0;
  min-block-size: 2.75rem;
  border: 1px solid var(--pt-20-line);
  border-radius: 0.3rem;
  background: var(--pt-20-s1);
  color: var(--pt-20-mut);
  font-family: var(--pt-20-font-display);
  font-size: 0.88rem;
  cursor: pointer;
}

.pt-20__room-btn--current {
  background: var(--pt-20-ink);
  border-color: var(--pt-20-ink);
  color: var(--pt-20-bg);
}

.pt-20__room-btn:focus-visible {
  outline: 2px solid var(--pt-20-acc);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .pt-20[data-pt-20-phase="paint"] .pt-20__stroke,
    .pt-20[data-pt-20-phase="lift"] .pt-20__stroke {
    animation: none;
    stroke-dashoffset: 1;
  }

  .pt-20__room {
    transition: opacity 90ms linear;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.pt-20');
const view = root.querySelector('#pt-20-room');
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const timers = []; let busy = false;
const rooms = {
  one: ['Room 1 &middot; Ground floor', 'Marks and Weather', 'Twenty-two works on paper made outdoors between 1962 and 1971. Hung in the order they were painted.', [['Works', '22'], ['Medium', 'Ink, gouache'], ['Until', '30 Nov']]],
  two: ['Room 2 &middot; Ground floor', 'The Long Table', 'A single work, nine metres, shown flat for the first time since it was made.', [['Works', '1'], ['Medium', 'Oil on linen'], ['Until', '18 Jan']]],
  three: ['Room 3 &middot; First floor', 'Studies for a Wall', 'Preparatory drawings for the west wall, with the surviving cartoon and two rejected schemes.', [['Works', '31'], ['Medium', 'Chalk, wash'], ['Until', '14 Mar']]]
};
function go(key, btn) {
  if (busy || btn.classList.contains('pt-20__room-btn--current')) return;
  busy = true;
  root.setAttribute('data-pt-20-phase', 'paint');
  timers.push(setTimeout(() => {
    const [eyebrow, title, text, facts] = rooms[key];
    view.innerHTML = '<p class="pt-20__eyebrow">' + eyebrow + '</p><h3 class="pt-20__title">' + title + '</h3><p class="pt-20__text">' + text + '</p><dl class="pt-20__facts">' + facts.map((f) => '<div><dt>' + f[0] + '</dt><dd>' + f[1] + '</dd></div>').join('') + '</dl>';
    root.querySelectorAll('[data-pt-20-room]').forEach((b) => b.classList.toggle('pt-20__room-btn--current', b === btn));
    view.focus({ preventScroll: true });
    root.setAttribute('data-pt-20-phase', 'lift');
    timers.push(setTimeout(() => { root.setAttribute('data-pt-20-phase', 'idle'); busy = false; }, reduce.matches ? 40 : 470));
  }, reduce.matches ? 40 : 430));
}
root.querySelectorAll('[data-pt-20-room]').forEach((b) => b.addEventListener('click', () => go(b.getAttribute('data-pt-20-room'), b)));
root.__ptCleanup = () => { timers.forEach(clearTimeout); root.setAttribute('data-pt-20-phase', 'idle'); };
```
