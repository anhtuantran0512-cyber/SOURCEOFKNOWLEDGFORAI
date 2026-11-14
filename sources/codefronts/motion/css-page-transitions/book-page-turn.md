---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/book-page-turn/"
title: "Book Page Turn Transition Effect CSS"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "A 3D page turn: the outgoing page rotates away around its spine edge while the incoming page is revealed underneath."
has_js: "true"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Book Page Turn Transition Effect CSS
Source: https://codefronts.com/motion/css-page-transitions/book-page-turn/

A 3D page turn: the outgoing page rotates away around its spine edge while the incoming page is revealed underneath. It belongs to editorial content, where a page turn is the reader's real mental model, and it is the one effect here that genuinely needs 3D. The trap is flattening &mdash; perspective on the wrong ancestor and the whole thing collapses to a flat squash.
## HTML
```html
<section class="pt-15" aria-labelledby="pt-15-h">
  <div class="pt-15__theme">
    <input class="pt-15__theme-input" type="checkbox" id="pt-15-theme">
    <label class="pt-15__theme-label" for="pt-15-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-15__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-15__stage">
    <header class="pt-15__masthead">
      <p class="pt-15__kicker">Page transitions / 15</p>
      <h2 class="pt-15__h" id="pt-15-h">The Basalt Review</h2>
      <p class="pt-15__lede">Sections are DOM nodes swapped by this demo&rsquo;s script while the turning page is edge-on. Nothing navigates &mdash; the book is in-page.</p>
    </header>

    <div class="pt-15__book">
      <div class="pt-15__spine" aria-hidden="true"></div>
      <div class="pt-15__pages">
        <div class="pt-15__leaf" data-pt-15-leaf aria-hidden="true"></div>
        <main class="pt-15__page" id="pt-15-page" tabindex="-1">
          <p class="pt-15__folio">Section I &middot; page 12</p>
          <h3 class="pt-15__title">On the pleasure of a slow interface</h3>
          <p class="pt-15__body">There is a kind of software that hurries you, and another kind that lets you arrive. The difference is rarely in the speed of the machine.</p>
          <p class="pt-15__body">A page turn is not decoration in a reading interface. It is the reader&rsquo;s own model of where they are, borrowed and made literal.</p>
          <p class="pt-15__by">Priya Sharma</p>
        </main>
      </div>
    </div>

    <div class="pt-15__controls">
      <button class="pt-15__turn" type="button" data-pt-15-turn="-1">&larr; Previous</button>
      <p class="pt-15__count"><b data-pt-15-at>1</b> of 3</p>
      <button class="pt-15__turn" type="button" data-pt-15-turn="1">Next &rarr;</button>
    </div>
  </div>
</section>
```
## CSS
```css
.pt-15 {
  --pt-15-bg: #f0ebe1;
  --pt-15-paper: #fbf8f1;
  --pt-15-paper2: #f3ede1;
  --pt-15-line: #d9d0be;
  --pt-15-ink: #1c1a16;
  --pt-15-mut: #6b6355;
  --pt-15-acc: #7a2e22;
  --pt-15-font-display: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-15-bg);
  background-image: radial-gradient(rgba(28, 26, 22, 0.035) 1px, transparent 1px);
  background-size: 4px 4px;
  color: var(--pt-15-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.6;
}

.pt-15 *,
.pt-15 *::before,
.pt-15 *::after {
  box-sizing: border-box;
}

.pt-15:has(.pt-15__theme-input:checked) {
  --pt-15-bg: #14120f;
  --pt-15-paper: #1d1a15;
  --pt-15-paper2: #241f19;
  --pt-15-line: #37301f;
  --pt-15-ink: #f2ece0;
  --pt-15-mut: #a89e8c;
  --pt-15-acc: #e0836f;
  background-image: radial-gradient(rgba(242, 236, 224, 0.04) 1px, transparent 1px);
}

@media (prefers-color-scheme: dark) {
  .pt-15 {
    --pt-15-bg: #14120f;
    --pt-15-paper: #1d1a15;
    --pt-15-paper2: #241f19;
    --pt-15-line: #37301f;
    --pt-15-ink: #f2ece0;
    --pt-15-mut: #a89e8c;
    --pt-15-acc: #e0836f;
    background-image: radial-gradient(rgba(242, 236, 224, 0.04) 1px, transparent 1px);
  }

  .pt-15:has(.pt-15__theme-input:checked) {
    --pt-15-bg: #f0ebe1;
    --pt-15-paper: #fbf8f1;
    --pt-15-paper2: #f3ede1;
    --pt-15-line: #d9d0be;
    --pt-15-ink: #1c1a16;
    --pt-15-mut: #6b6355;
    --pt-15-acc: #7a2e22;
    background-image: radial-gradient(rgba(28, 26, 22, 0.035) 1px, transparent 1px);
  }
}

@media (prefers-color-scheme: light) {
  .pt-15:has(.pt-15__theme-input:checked) {
    --pt-15-bg: #14120f;
    --pt-15-paper: #1d1a15;
    --pt-15-paper2: #241f19;
    --pt-15-line: #37301f;
    --pt-15-ink: #f2ece0;
    --pt-15-mut: #a89e8c;
    --pt-15-acc: #e0836f;
    background-image: radial-gradient(rgba(242, 236, 224, 0.04) 1px, transparent 1px);
  }
}

@supports (color: oklch(0.4 0.12 30)) {
  .pt-15 {
    --pt-15-acc: oklch(0.42 0.13 32);
  }

  .pt-15:has(.pt-15__theme-input:checked) {
    --pt-15-acc: oklch(0.74 0.12 38);
  }

  @media (prefers-color-scheme: dark) {
    .pt-15 {
      --pt-15-acc: oklch(0.74 0.12 38);
    }

    .pt-15:has(.pt-15__theme-input:checked) {
      --pt-15-acc: oklch(0.42 0.13 32);
    }
  }
}

.pt-15__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-15__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
}

.pt-15__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-15__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--pt-15-line);
  border-radius: 0.2rem;
  background: var(--pt-15-paper);
  color: var(--pt-15-mut);
  cursor: pointer;
}

.pt-15__theme-label svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.pt-15__theme-input:focus-visible + .pt-15__theme-label {
  outline: 2px solid var(--pt-15-acc);
  outline-offset: 2px;
}

.pt-15__stage {
  max-inline-size: 54rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.4rem;
}

.pt-15__masthead {
  text-align: center;
  border-block-end: 2px solid var(--pt-15-ink);
  padding-block-end: 1rem;
}

.pt-15__kicker {
  margin: 0 0 0.5rem;
  font-size: 0.72rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--pt-15-mut);
}

.pt-15__h {
  margin: 0 0 0.5rem;
  font-family: var(--pt-15-font-display);
  font-size: clamp(1.8rem, 6vw, 2.9rem);
  font-weight: 400;
  letter-spacing: -0.01em;
}

.pt-15__lede {
  margin: 0 auto;
  max-inline-size: 34rem;
  color: var(--pt-15-mut);
  font-size: 0.9rem;
  text-wrap: pretty;
}

.pt-15__book {
  position: relative;
  perspective: 1400px;
  min-inline-size: 0;
}

.pt-15__spine {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: 0.5rem;
  background: linear-gradient(90deg, rgba(0, 0, 0, 0.18), transparent);
  z-index: 4;
  pointer-events: none;
}

.pt-15__pages {
  position: relative;
  transform-style: preserve-3d;
  min-block-size: 19rem;
  background: var(--pt-15-paper);
  border: 1px solid var(--pt-15-line);
  box-shadow: 0 20px 50px -30px rgba(0, 0, 0, 0.45);
}

.pt-15__leaf {
  position: absolute;
  inset: 0;
  z-index: 3;
  transform-origin: left center;
  transform: rotateY(0deg);
  backface-visibility: hidden;
  opacity: 0;
  pointer-events: none;
  background: linear-gradient(100deg, var(--pt-15-paper2) 0%, var(--pt-15-paper) 45%, rgba(0, 0, 0, 0.14) 100%);
}

.pt-15[data-pt-15-turning="1"] .pt-15__leaf {
  opacity: 1;
  animation: pt-15-turn 620ms cubic-bezier(0.4, 0.05, 0.2, 1) both;
}

@keyframes pt-15-turn {
  from {
    transform: rotateY(0deg);
  }

  to {
    transform: rotateY(-118deg);
  }
}

.pt-15__page {
  position: relative;
  z-index: 1;
  display: block;
  padding: clamp(1.2rem, 4vw, 2.4rem);
}

.pt-15__page:focus-visible {
  outline: 2px solid var(--pt-15-acc);
  outline-offset: -4px;
}

.pt-15__folio {
  margin: 0 0 0.7rem;
  font-size: 0.74rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--pt-15-mut);
}

.pt-15__title {
  margin: 0 0 0.8rem;
  font-family: var(--pt-15-font-display);
  font-size: clamp(1.35rem, 4.2vw, 1.9rem);
  font-weight: 400;
  line-height: 1.2;
  max-inline-size: 28rem;
}

.pt-15__body {
  margin: 0 0 0.8rem;
  max-inline-size: 32rem;
  font-family: var(--pt-15-font-display);
  font-size: 1.02rem;
  color: var(--pt-15-ink);
  text-wrap: pretty;
}

.pt-15__by {
  margin: 0;
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--pt-15-acc);
}

.pt-15__controls {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 0.75rem 1.25rem;
}

.pt-15__turn {
  min-block-size: 2.75rem;
  padding: 0.5rem 1.1rem;
  border: 1px solid var(--pt-15-ink);
  background: transparent;
  color: var(--pt-15-ink);
  font-family: var(--pt-15-font-display);
  font-size: 0.95rem;
  cursor: pointer;
}

.pt-15__turn:hover:not([disabled]) {
  background: var(--pt-15-ink);
  color: var(--pt-15-paper);
}

.pt-15__turn[disabled] {
  opacity: 0.4;
  cursor: default;
}

.pt-15__turn:focus-visible {
  outline: 2px solid var(--pt-15-acc);
  outline-offset: 3px;
}

.pt-15__count {
  margin: 0;
  font-size: 0.82rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--pt-15-mut);
}

@media (prefers-reduced-motion: reduce) {
  .pt-15[data-pt-15-turning="1"] .pt-15__leaf {
    animation: none;
    opacity: 0;
  }

  .pt-15__page {
    transition: opacity 90ms linear;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.pt-15');
const page = root.querySelector('#pt-15-page');
const atOut = root.querySelector('[data-pt-15-at]');
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const timers = []; let at = 0; let busy = false;
const spreads = [
  ['Section I &middot; page 12', 'On the pleasure of a slow interface', ['There is a kind of software that hurries you, and another kind that lets you arrive. The difference is rarely in the speed of the machine.', 'A page turn is not decoration in a reading interface. It is the reader&rsquo;s own model of where they are, borrowed and made literal.'], 'Priya Sharma'],
  ['Section II &middot; page 26', 'Against the infinite scroll', ['A page has edges, and edges are how a reader measures progress. Remove them and reading becomes an activity with no shape.', 'The scroll was never a reading format. It was a storage format that we mistook for one.'], 'Alex Chen'],
  ['Section III &middot; page 41', 'What the margin is for', ['Every generous margin is an argument about attention: that the words deserve room, and the reader deserves somewhere to rest.', 'Density is cheap. Rhythm is not.'], 'Sam Rivera']
];
function turn(delta) {
  const next = at + delta;
  if (busy || next < 0 || next > spreads.length - 1) return;
  busy = true; at = next;
  root.setAttribute('data-pt-15-turning', '1');
  timers.push(setTimeout(() => {
    const [folio, title, paras, by] = spreads[at];
    page.innerHTML = '<p class="pt-15__folio">' + folio + '</p><h3 class="pt-15__title">' + title + '</h3>' + paras.map((p) => '<p class="pt-15__body">' + p + '</p>').join('') + '<p class="pt-15__by">' + by + '</p>';
    atOut.textContent = at + 1;
    root.querySelector('[data-pt-15-turn="-1"]').disabled = at === 0;
    root.querySelector('[data-pt-15-turn="1"]').disabled = at === spreads.length - 1;
    page.focus({ preventScroll: true });
  }, reduce.matches ? 40 : 300));
  timers.push(setTimeout(() => { root.setAttribute('data-pt-15-turning', '0'); busy = false; }, reduce.matches ? 90 : 640));
}
root.querySelectorAll('[data-pt-15-turn]').forEach((b) => b.addEventListener('click', () => turn(Number(b.getAttribute('data-pt-15-turn')))));
root.querySelector('[data-pt-15-turn="-1"]').disabled = true;
root.__ptCleanup = () => { timers.forEach(clearTimeout); root.setAttribute('data-pt-15-turning', '0'); };
```
