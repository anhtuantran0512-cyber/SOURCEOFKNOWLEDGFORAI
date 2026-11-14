---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/page-transition-overlay-cover-swap-reveal/"
title: "Page Transition Overlay Cover Swap Reveal"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "The reference build the other nineteen demos borrow from."
has_js: "true"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Page Transition Overlay Cover Swap Reveal
Source: https://codefronts.com/motion/css-page-transitions/page-transition-overlay-cover-swap-reveal/

The reference build the other nineteen demos borrow from. Four phases, each labelled and timed: an overlay covers the viewport, the route content swaps while the overlay is fully opaque, the overlay reveals the new route, and the overlay is removed from the accessibility tree. One rule governs the whole pattern &mdash; the swap must land inside the opaque window, because swapping early shows the content changing and swapping late flashes a blank frame.
## HTML
```html
<section class="pt-01" aria-labelledby="pt-01-h">
  <div class="pt-01__theme">
    <input class="pt-01__theme-input" type="checkbox" id="pt-01-theme">
    <label class="pt-01__theme-label" for="pt-01-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-01__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-01__stage">
    <header class="pt-01__head">
      <p class="pt-01__kicker">Page transitions / 01 &middot; reference lifecycle</p>
      <h2 class="pt-01__h" id="pt-01-h">Cover, swap, reveal, clean up</h2>
      <p class="pt-01__lede">Routes are DOM sections swapped in place by this demo&rsquo;s own script &mdash; there is no router and no real navigation. Pick a page to run the lifecycle.</p>
    </header>

    <div class="pt-01__doc">
      <nav class="pt-01__toc" aria-label="Documentation pages">
        <p class="pt-01__toc-title">Basalt docs</p>
        <ul class="pt-01__toc-list">
          <li><button class="pt-01__toc-link pt-01__toc-link--current" type="button" data-pt-01-route="install">Installation</button></li>
          <li><button class="pt-01__toc-link" type="button" data-pt-01-route="deploy">Deployments</button></li>
          <li><button class="pt-01__toc-link" type="button" data-pt-01-route="tokens">API tokens</button></li>
        </ul>
        <p class="pt-01__toc-note">Simulated routing &middot; in-page swap</p>
      </nav>

      <div class="pt-01__viewport">
        <div class="pt-01__overlay" aria-hidden="true"><span class="pt-01__overlay-text">opaque &mdash; swapping</span></div>
        <main class="pt-01__route" id="pt-01-route" tabindex="-1">
          <p class="pt-01__eyebrow">Getting started</p>
          <h3 class="pt-01__title">Installation</h3>
          <p class="pt-01__text">Add the Basalt CLI, authenticate once, and link the working directory to a project. Every later command reads the link file, so this is the only interactive step.</p>
          <pre class="pt-01__code"><code>npm i -g @basalt/cli
basalt login
basalt link</code></pre>
          <p class="pt-01__text">Linking writes <code>.basalt/project.json</code>. Commit it if the whole team deploys from local machines.</p>
        </main>
      </div>
    </div>

    <figure class="pt-01__tl">
      <figcaption class="pt-01__tl-cap">Phase timeline &mdash; 640ms total</figcaption>
      <ol class="pt-01__tl-track">
        <li class="pt-01__ph" data-pt-01-phase="cover" style="--pt-01-w:260"><span class="pt-01__ph-bar"></span><span class="pt-01__ph-name">1 cover</span><span class="pt-01__ph-ms">260ms</span></li>
        <li class="pt-01__ph pt-01__ph--hold" data-pt-01-phase="swap" style="--pt-01-w:60"><span class="pt-01__ph-bar"></span><span class="pt-01__ph-name">2 swap</span><span class="pt-01__ph-ms">60ms opaque</span></li>
        <li class="pt-01__ph" data-pt-01-phase="reveal" style="--pt-01-w:320"><span class="pt-01__ph-bar"></span><span class="pt-01__ph-name">3 reveal</span><span class="pt-01__ph-ms">320ms</span></li>
        <li class="pt-01__ph" data-pt-01-phase="done" style="--pt-01-w:120"><span class="pt-01__ph-bar"></span><span class="pt-01__ph-name">4 clean up</span><span class="pt-01__ph-ms">focus + aria</span></li>
      </ol>
      <p class="pt-01__tl-rule">The swap fires at the midpoint of phase 2. Early &rarr; the change is visible. Late &rarr; a blank frame flashes.</p>
    </figure>
  </div>
</section>
```
## CSS
```css
.pt-01 {
  --pt-01-bg: #f5f6f8;
  --pt-01-surf: #ffffff;
  --pt-01-surf2: #eceef2;
  --pt-01-line: #d8dbe2;
  --pt-01-ink: #14161b;
  --pt-01-mut: #5b6270;
  --pt-01-acc: #2b4ee0;
  --pt-01-acc-soft: #e6eafd;
  --pt-01-ov: #14161b;
  --pt-01-ov-ink: #f5f6f8;
  --pt-01-font-display: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-01-bg);
  color: var(--pt-01-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  font-size: 100%;
  line-height: 1.55;
}

.pt-01 *,
.pt-01 *::before,
.pt-01 *::after {
  box-sizing: border-box;
}

.pt-01:has(.pt-01__theme-input:checked) {
  --pt-01-bg: #0d0f13;
  --pt-01-surf: #15181e;
  --pt-01-surf2: #1c2028;
  --pt-01-line: #2a2f39;
  --pt-01-ink: #eef0f4;
  --pt-01-mut: #98a0b0;
  --pt-01-acc: #8aa2ff;
  --pt-01-acc-soft: #1d2440;
  --pt-01-ov: #eef0f4;
  --pt-01-ov-ink: #0d0f13;
}

@media (prefers-color-scheme: dark) {
  .pt-01 {
    --pt-01-bg: #0d0f13;
    --pt-01-surf: #15181e;
    --pt-01-surf2: #1c2028;
    --pt-01-line: #2a2f39;
    --pt-01-ink: #eef0f4;
    --pt-01-mut: #98a0b0;
    --pt-01-acc: #8aa2ff;
    --pt-01-acc-soft: #1d2440;
    --pt-01-ov: #eef0f4;
    --pt-01-ov-ink: #0d0f13;
  }

  .pt-01:has(.pt-01__theme-input:checked) {
    --pt-01-bg: #f5f6f8;
    --pt-01-surf: #ffffff;
    --pt-01-surf2: #eceef2;
    --pt-01-line: #d8dbe2;
    --pt-01-ink: #14161b;
    --pt-01-mut: #5b6270;
    --pt-01-acc: #2b4ee0;
    --pt-01-acc-soft: #e6eafd;
    --pt-01-ov: #14161b;
    --pt-01-ov-ink: #f5f6f8;
  }
}

@media (prefers-color-scheme: light) {
  .pt-01:has(.pt-01__theme-input:checked) {
    --pt-01-bg: #0d0f13;
    --pt-01-surf: #15181e;
    --pt-01-surf2: #1c2028;
    --pt-01-line: #2a2f39;
    --pt-01-ink: #eef0f4;
    --pt-01-mut: #98a0b0;
    --pt-01-acc: #8aa2ff;
    --pt-01-acc-soft: #1d2440;
    --pt-01-ov: #eef0f4;
    --pt-01-ov-ink: #0d0f13;
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .pt-01 {
    --pt-01-acc: oklch(0.48 0.19 267);
  }

  .pt-01:has(.pt-01__theme-input:checked) {
    --pt-01-acc: oklch(0.78 0.12 267);
  }

  @media (prefers-color-scheme: dark) {
    .pt-01 {
      --pt-01-acc: oklch(0.78 0.12 267);
    }

    .pt-01:has(.pt-01__theme-input:checked) {
      --pt-01-acc: oklch(0.48 0.19 267);
    }
  }
}

.pt-01__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-01__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 8;
}

.pt-01__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-01__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--pt-01-line);
  border-radius: 0.25rem;
  background: var(--pt-01-surf);
  color: var(--pt-01-mut);
  cursor: pointer;
}

.pt-01__theme-label svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.pt-01__theme-input:focus-visible + .pt-01__theme-label {
  outline: 2px solid var(--pt-01-acc);
  outline-offset: 2px;
  color: var(--pt-01-ink);
}

.pt-01__stage {
  max-inline-size: 68rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.5rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.75rem;
}

.pt-01__head {
  border-block-end: 1px solid var(--pt-01-line);
  padding-block-end: 1.25rem;
}

.pt-01__kicker {
  margin: 0 0 0.5rem;
  font-family: var(--pt-01-font-display);
  font-size: 0.72rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--pt-01-mut);
}

.pt-01__h {
  margin: 0 0 0.6rem;
  font-family: var(--pt-01-font-display);
  font-size: clamp(1.35rem, 4.2vw, 2rem);
  font-weight: 600;
  letter-spacing: -0.01em;
}

.pt-01__lede {
  margin: 0;
  max-inline-size: 46rem;
  color: var(--pt-01-mut);
  font-size: 0.95rem;
  text-wrap: pretty;
}

.pt-01__doc {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.25rem;
}

@media (min-width: 46rem) {
  .pt-01__doc {
    grid-template-columns: 13rem minmax(0, 1fr);
  }
}

.pt-01__toc {
  min-inline-size: 0;
  border-inline-start: 2px solid var(--pt-01-line);
  padding-inline-start: 1rem;
}

.pt-01__toc-title {
  margin: 0 0 0.75rem;
  font-family: var(--pt-01-font-display);
  font-size: 0.7rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--pt-01-mut);
}

.pt-01__toc-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.25rem;
}

.pt-01__toc-link {
  display: flex;
  align-items: center;
  inline-size: 100%;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.65rem;
  border: 0;
  border-radius: 0.2rem;
  background: transparent;
  color: var(--pt-01-mut);
  font: inherit;
  font-size: 0.9rem;
  text-align: start;
  cursor: pointer;
}

.pt-01__toc-link:hover {
  background: var(--pt-01-surf2);
  color: var(--pt-01-ink);
}

.pt-01__toc-link:focus-visible {
  outline: 2px solid var(--pt-01-acc);
  outline-offset: 2px;
}

.pt-01__toc-link--current {
  background: var(--pt-01-acc-soft);
  color: var(--pt-01-ink);
  font-weight: 600;
  box-shadow: inset 2px 0 0 var(--pt-01-acc);
}

.pt-01__toc-note {
  margin: 1rem 0 0;
  font-family: var(--pt-01-font-display);
  font-size: 0.66rem;
  color: var(--pt-01-mut);
  opacity: 0.85;
}

.pt-01__viewport {
  position: relative;
  overflow: hidden;
  min-inline-size: 0;
  min-block-size: 21rem;
  background: var(--pt-01-surf);
  border: 1px solid var(--pt-01-line);
  border-radius: 0.35rem;
}

.pt-01__overlay {
  position: absolute;
  inset: 0;
  z-index: 3;
  display: grid;
  place-items: center;
  background: var(--pt-01-ov);
  color: var(--pt-01-ov-ink);
  transform: scaleY(0);
  transform-origin: bottom center;
  pointer-events: none;
}

.pt-01__overlay-text {
  font-family: var(--pt-01-font-display);
  font-size: 0.72rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  opacity: 0;
}

.pt-01[data-pt-01-state="cover"] .pt-01__overlay {
  animation: pt-01-cover 260ms cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

.pt-01[data-pt-01-state="swap"] .pt-01__overlay {
  transform: scaleY(1);
}

.pt-01[data-pt-01-state="swap"] .pt-01__overlay-text {
  opacity: 0.75;
}

.pt-01[data-pt-01-state="reveal"] .pt-01__overlay {
  transform-origin: top center;
  animation: pt-01-reveal 320ms cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

@keyframes pt-01-cover {
  from {
    transform: scaleY(0);
  }

  to {
    transform: scaleY(1);
  }
}

@keyframes pt-01-reveal {
  from {
    transform: scaleY(1);
  }

  to {
    transform: scaleY(0);
  }
}

.pt-01__route {
  display: block;
  padding: clamp(1.1rem, 3vw, 1.9rem);
  min-inline-size: 0;
}

.pt-01__route:focus-visible {
  outline: 2px solid var(--pt-01-acc);
  outline-offset: -3px;
}

.pt-01__eyebrow {
  margin: 0 0 0.4rem;
  font-family: var(--pt-01-font-display);
  font-size: 0.68rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--pt-01-acc);
}

.pt-01__title {
  margin: 0 0 0.7rem;
  font-family: var(--pt-01-font-display);
  font-size: 1.3rem;
  font-weight: 600;
}

.pt-01__text {
  margin: 0 0 0.9rem;
  max-inline-size: 40rem;
  font-size: 0.94rem;
  color: var(--pt-01-mut);
  text-wrap: pretty;
}

.pt-01__text code,
.pt-01__code code {
  font-family: var(--pt-01-font-display);
  font-size: 0.86em;
}

.pt-01__code {
  margin: 0 0 0.9rem;
  padding: 0.85rem 1rem;
  overflow-x: auto;
  background: var(--pt-01-surf2);
  border-radius: 0.25rem;
  border-inline-start: 2px solid var(--pt-01-acc);
  color: var(--pt-01-ink);
  font-size: 0.82rem;
  line-height: 1.7;
}

.pt-01__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0.55rem;
  max-inline-size: 40rem;
}

.pt-01__list li {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 0.75rem;
  justify-content: space-between;
  min-inline-size: 0;
  padding-block-end: 0.55rem;
  border-block-end: 1px solid var(--pt-01-line);
  font-size: 0.88rem;
}

.pt-01__list b {
  font-weight: 600;
}

.pt-01__list span {
  color: var(--pt-01-mut);
  font-family: var(--pt-01-font-display);
  font-size: 0.78rem;
}

.pt-01__tl {
  margin: 0;
}

.pt-01__tl-cap {
  margin-block-end: 0.65rem;
  font-family: var(--pt-01-font-display);
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--pt-01-mut);
}

.pt-01__tl-track {
  list-style: none;
  margin: 0 0 0.7rem;
  padding: 0;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0.5rem;
}

@media (min-width: 34rem) {
  .pt-01__tl-track {
    grid-template-columns: 260fr 60fr 320fr 120fr;
  }
}

.pt-01__ph {
  min-inline-size: 0;
  display: grid;
  gap: 0.3rem;
}

.pt-01__ph-bar {
  display: block;
  block-size: 0.4rem;
  border-radius: 999px;
  background: var(--pt-01-line);
}

.pt-01__ph--hold .pt-01__ph-bar {
  background: repeating-linear-gradient(90deg, var(--pt-01-line) 0 3px, transparent 3px 6px);
}

.pt-01__ph-name {
  font-family: var(--pt-01-font-display);
  font-size: 0.76rem;
  font-weight: 600;
}

.pt-01__ph-ms {
  font-size: 0.72rem;
  color: var(--pt-01-mut);
}

.pt-01__ph[data-pt-01-active] .pt-01__ph-bar {
  background: var(--pt-01-acc);
}

.pt-01__ph[data-pt-01-active] .pt-01__ph-name {
  color: var(--pt-01-acc);
}

.pt-01__tl-rule {
  margin: 0;
  padding: 0.7rem 0.85rem;
  background: var(--pt-01-surf2);
  border-radius: 0.25rem;
  font-size: 0.84rem;
  color: var(--pt-01-mut);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .pt-01[data-pt-01-state="cover"] .pt-01__overlay,
    .pt-01[data-pt-01-state="reveal"] .pt-01__overlay {
    animation: none;
  }

  .pt-01[data-pt-01-state="cover"] .pt-01__overlay {
    transform: scaleY(1);
    opacity: 0.001;
  }

  .pt-01__route {
    transition: opacity 90ms linear;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.pt-01');
const view = root.querySelector('.pt-01__route');
const links = [...root.querySelectorAll('[data-pt-01-route]')];
const phases = [...root.querySelectorAll('.pt-01__ph')];
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const PHASES = { cover: 260, swap: 60, reveal: 320 };
const pages = {
  install: ['Getting started', 'Installation', '<p class="pt-01__text">Add the Basalt CLI, authenticate once, and link the working directory to a project.</p><pre class="pt-01__code"><code>npm i -g @basalt/cli\nbasalt login\nbasalt link</code></pre>'],
  deploy: ['Guides', 'Deployments', '<p class="pt-01__text">Every push to a linked branch builds an immutable deployment. Promotion is a pointer move, so rollback is instant.</p><ul class="pt-01__list"><li><b>Preview builds</b><span>on every push</span></li><li><b>Promote to production</b><span>pointer move</span></li><li><b>Rollback window</b><span>90 days</span></li></ul>'],
  tokens: ['Reference', 'API tokens', '<p class="pt-01__text">Tokens are scoped per project and never shown twice. Rotate on a schedule and keep the CI token separate from personal ones.</p><ul class="pt-01__list"><li><b>ci-deploy</b><span>Jordan Lee &middot; 41d left</span></li><li><b>local-cli</b><span>Priya Sharma &middot; 12d left</span></li></ul>']
};
const timers = [];
let busy = false;
function go(key, btn) {
  if (busy || btn.classList.contains('pt-01__toc-link--current')) return;
  busy = true;
  links.forEach((l) => l.classList.toggle('pt-01__toc-link--current', l === btn));
  const step = (name, ms, fn) => timers.push(setTimeout(() => { root.setAttribute('data-pt-01-state', name); phases.forEach((p) => p.toggleAttribute('data-pt-01-active', p.getAttribute('data-pt-01-phase') === name)); fn && fn(); }, ms));
  const t = reduce.matches ? { cover: 0, swap: 0, reveal: 0 } : PHASES;
  step('cover', 0);
  step('swap', t.cover, () => {
    const [eyebrow, title, body] = pages[key];
    view.innerHTML = '<p class="pt-01__eyebrow">' + eyebrow + '</p><h3 class="pt-01__title">' + title + '</h3>' + body;
    view.focus({ preventScroll: true });
  });
  step('reveal', t.cover + t.swap);
  step('done', t.cover + t.swap + t.reveal, () => { root.setAttribute('data-pt-01-state', 'idle'); busy = false; });
}
links.forEach((btn) => btn.addEventListener('click', () => go(btn.getAttribute('data-pt-01-route'), btn)));
root.__ptCleanup = () => { timers.forEach(clearTimeout); links.forEach((b) => b.replaceWith(b.cloneNode(true))); };
```
