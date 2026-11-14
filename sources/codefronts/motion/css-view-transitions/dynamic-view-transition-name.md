---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/dynamic-view-transition-name/"
title: "Dynamic View Transition Name"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "A list rendered from data cannot carry hand-written view-transition-name values in a stylesheet, because each name must be unique in the document and the set…"
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dynamic View Transition Name
Source: https://codefronts.com/motion/css-view-transitions/dynamic-view-transition-name/

A list rendered from data cannot carry hand-written view-transition-name values in a stylesheet, because each name must be unique in the document and the set changes at runtime. The fix is to set the name on the two participating elements immediately before the transition and clear it immediately after, so only the pair that is actually morphing is ever named.
## HTML
```html
<section class="vtr-03" aria-labelledby="vtr-03-heading">
  <fieldset class="vtr-03__theme">
    <legend class="vtr-03__themelegend">Theme</legend>
    <input class="vtr-03__themeinput" type="radio" name="vtr-03-theme" id="vtr-03-theme-auto" checked>
    <label class="vtr-03__themeopt" for="vtr-03-theme-auto">Auto</label>
    <input class="vtr-03__themeinput" type="radio" name="vtr-03-theme" id="vtr-03-theme-light">
    <label class="vtr-03__themeopt" for="vtr-03-theme-light">Light</label>
    <input class="vtr-03__themeinput" type="radio" name="vtr-03-theme" id="vtr-03-theme-dark">
    <label class="vtr-03__themeopt" for="vtr-03-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-03__stage">
    <header class="vtr-03__head">
      <p class="vtr-03__kicker">Runtime naming</p>
      <h2 class="vtr-03__heading" id="vtr-03-heading">Name the pair, then clear it</h2>
      <p class="vtr-03__sub">Pin any alert to the top. The name exists only while that one transition runs.</p>
    </header>

    <div class="vtr-03__grid">
      <div class="vtr-03__panel">
        <div class="vtr-03__pinned" id="vtr-03-pinned" aria-live="polite">
          <p class="vtr-03__slotlabel">Pinned</p>
          <article class="vtr-03__row vtr-03__row--pinned" data-vtr03-id="a">
            <span class="vtr-03__sev vtr-03__sev--high">P1</span>
            <span class="vtr-03__rowtext"><strong>Latency spike on orbit-api</strong><span>p99 at 1.8s · eu-west-1</span></span>
          </article>
        </div>
        <ul class="vtr-03__list" id="vtr-03-list">
          <li><article class="vtr-03__row" data-vtr03-id="b">
            <span class="vtr-03__sev">P3</span>
            <span class="vtr-03__rowtext"><strong>Certificate renews in 9 days</strong><span>prism.internal · automated</span></span>
            <button class="vtr-03__pin" type="button" data-vtr03-pin="b">Pin</button>
          </article></li>
          <li><article class="vtr-03__row" data-vtr03-id="c">
            <span class="vtr-03__sev vtr-03__sev--mid">P2</span>
            <span class="vtr-03__rowtext"><strong>Queue depth above threshold</strong><span>sable-workers · 4,120 jobs</span></span>
            <button class="vtr-03__pin" type="button" data-vtr03-pin="c">Pin</button>
          </article></li>
          <li><article class="vtr-03__row" data-vtr03-id="d">
            <span class="vtr-03__sev">P3</span>
            <span class="vtr-03__rowtext"><strong>Disk usage 71% on vale-db-2</strong><span>steady for 6 hours</span></span>
            <button class="vtr-03__pin" type="button" data-vtr03-pin="d">Pin</button>
          </article></li>
        </ul>
      </div>

      <aside class="vtr-03__trace" aria-label="What runs on each pin">
        <p class="vtr-03__tracelabel">Per transition</p>
        <ol class="vtr-03__steps">
          <li><code>el.style.viewTransitionName = 'vtr-03-active'</code><span>Before the call. The old snapshot needs it.</span></li>
          <li><code>document.startViewTransition(move)</code><span>The callback reparents the row, synchronously.</span></li>
          <li><code>await t.finished</code><span>Wait for the animation, not a timeout.</span></li>
          <li><code>el.style.viewTransitionName = ''</code><span>In a finally block, so it always runs.</span></li>
        </ol>
        <p class="vtr-03__warn">Skip step four and the next pin is a duplicate name — the transition aborts with no error.</p>
      </aside>
    </div>
  </div>
</section>
```
## CSS
```css
.vtr-03 {
  --bg: #070d1a;
  --surface: #0e1729;
  --surface-2: #131f36;
  --line: #1e2d4a;
  --ink: #e9f0ff;
  --muted: #8ba0c4;
  --accent: #22d3ee;
  --accent-soft: #0d2f3a;
  --font-display: system-ui, "Segoe UI", sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  color-scheme: dark light;
}

.vtr-03 *,
.vtr-03 *::before,
.vtr-03 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-03 {
    --bg: oklch(16% 0.035 260);
    --surface: oklch(21% 0.04 260);
    --surface-2: oklch(26% 0.045 258);
    --line: oklch(33% 0.045 258);
    --ink: oklch(95% 0.015 250);
    --muted: oklch(70% 0.035 250);
    --accent: oklch(80% 0.14 200);
    --accent-soft: oklch(30% 0.07 205);
  }
}

@media (prefers-color-scheme: light) {
  .vtr-03 {
    --bg: #eef3fa;
    --surface: #ffffff;
    --surface-2: #f3f7fd;
    --line: #d5e0ef;
    --ink: #0c1526;
    --muted: #56688a;
    --accent: #0e7490;
    --accent-soft: #dff5fb;
  }
}

.vtr-03[data-theme="light"] {
  --bg: #eef3fa;
  --surface: #ffffff;
  --surface-2: #f3f7fd;
  --line: #d5e0ef;
  --ink: #0c1526;
  --muted: #56688a;
  --accent: #0e7490;
  --accent-soft: #dff5fb;
}

.vtr-03[data-theme="dark"] {
  --bg: #070d1a;
  --surface: #0e1729;
  --surface-2: #131f36;
  --line: #1e2d4a;
  --ink: #e9f0ff;
  --muted: #8ba0c4;
  --accent: #22d3ee;
  --accent-soft: #0d2f3a;
}

.vtr-03__stage {
  max-width: 64rem;
  margin: 0 auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.5rem);
  display: grid;
  gap: 1.5rem;
}

.vtr-03__kicker {
  margin: 0 0 0.4rem;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-03__heading {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.4rem, 4.4vw, 2rem);
  font-weight: 650;
  letter-spacing: -0.02em;
}

.vtr-03__sub {
  margin: 0.4rem 0 0;
  color: var(--muted);
  font-size: 0.9rem;
  max-width: 36rem;
}

.vtr-03__grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;
}

@media (min-width: 58rem) {
  .vtr-03__grid {
    grid-template-columns: 1.35fr 1fr;
  }
}

.vtr-03__panel {
  border-radius: 0.75rem;
  padding: 0.85rem;
  background: var(--surface);
  box-shadow: 0 0 0 1px var(--line), 0 18px 40px -28px rgba(34, 211, 238, 0.55);
  display: grid;
  gap: 0.7rem;
  align-content: start;
  min-inline-size: 0;
}

.vtr-03__slotlabel,
.vtr-03__tracelabel {
  margin: 0 0 0.45rem;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.64rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.vtr-03__pinned {
  padding: 0.6rem;
  border-radius: 0.6rem;
  border: 1px dashed var(--line);
}

.vtr-03__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0.45rem;
}

.vtr-03__row {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 0.7rem;
  align-items: center;
  padding: 0.65rem 0.7rem;
  border-radius: 0.5rem;
  background: var(--surface-2);
  border: 1px solid var(--line);
  min-inline-size: 0;
}

.vtr-03__row--pinned {
  grid-template-columns: auto 1fr;
  background: var(--accent-soft);
  border-color: var(--accent);
}

.vtr-03__sev {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.66rem;
  padding: 0.2rem 0.4rem;
  border-radius: 0.25rem;
  background: var(--line);
  color: var(--muted);
}

.vtr-03__sev--high {
  background: #7f1d1d;
  color: #fecaca;
}

.vtr-03__sev--mid {
  background: #78350f;
  color: #fde68a;
}

.vtr-03__rowtext {
  display: grid;
  gap: 0.15rem;
  min-inline-size: 0;
}

.vtr-03__rowtext strong {
  font-size: 0.84rem;
  font-weight: 600;
}

.vtr-03__rowtext span {
  font-size: 0.72rem;
  color: var(--muted);
}

.vtr-03__pin {
  min-height: 44px;
  padding: 0 0.85rem;
  border-radius: 0.4rem;
  border: 1px solid var(--accent);
  background: transparent;
  color: var(--accent);
  font-size: 0.76rem;
  font-weight: 600;
  cursor: pointer;
}

.vtr-03__pin:hover {
  background: var(--accent-soft);
}

.vtr-03__pin:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.vtr-03__trace {
  border-radius: 0.75rem;
  padding: 0.9rem 1rem;
  background: var(--surface);
  border: 1px solid var(--line);
  min-inline-size: 0;
}

.vtr-03__steps {
  margin: 0;
  padding-left: 1.1rem;
  display: grid;
  gap: 0.6rem;
  font-size: 0.76rem;
  color: var(--muted);
}

.vtr-03__steps code {
  display: block;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.7rem;
  color: var(--ink);
  word-break: break-word;
}

.vtr-03__steps span {
  display: block;
  margin-top: 0.15rem;
}

.vtr-03__warn {
  margin: 0.9rem 0 0;
  padding: 0.6rem 0.7rem;
  border-radius: 0.4rem;
  background: var(--accent-soft);
  font-size: 0.74rem;
  line-height: 1.5;
  color: var(--ink);
}

::view-transition-group(vtr-03-active) {
  animation-duration: 380ms;
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(vtr-03-active) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-03 {
  position: relative;
}

.vtr-03__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 8%, transparent);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: system-ui, sans-serif;
}

.vtr-03__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-03__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-03__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: inherit;
  opacity: 0.55;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}

.vtr-03__themeopt:hover {
  opacity: 0.85;
}

.vtr-03__themeinput:checked + .vtr-03__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-03__themeinput:focus-visible + .vtr-03__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-03:has(#vtr-03-theme-light:checked) {
  --bg: #eef3fa;
  --surface: #ffffff;
  --surface-2: #f3f7fd;
  --line: #d5e0ef;
  --ink: #0c1526;
  --muted: #56688a;
  --accent: #0e7490;
  --accent-soft: #dff5fb;
}

.vtr-03:has(#vtr-03-theme-dark:checked) {
  --bg: #070d1a;
  --surface: #0e1729;
  --surface-2: #131f36;
  --line: #1e2d4a;
  --ink: #e9f0ff;
  --muted: #8ba0c4;
  --accent: #22d3ee;
  --accent-soft: #0d2f3a;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-03');
  if (!root || root.dataset.vtr03) return;
  root.dataset.vtr03 = 'on';
  const slot = root.querySelector('#vtr-03-pinned');
  const list = root.querySelector('#vtr-03-list');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let busy = false;
  const move = (row) => {
    const out = slot.querySelector('.vtr-03__row');
    out.classList.remove('vtr-03__row--pinned');
    out.insertAdjacentHTML('beforeend', '<button class="vtr-03__pin" type="button" data-vtr03-pin="' + out.dataset.vtr03Id + '">Pin</button>');
    list.insertAdjacentHTML('beforeend', '<li></li>');
    list.lastElementChild.append(out);
    row.querySelector('.vtr-03__pin').remove();
    row.classList.add('vtr-03__row--pinned');
    slot.append(row);
  };
  root.addEventListener('click', async (e) => {
    const btn = e.target.closest('[data-vtr03-pin]');
    if (!btn || busy) return;
    const row = btn.closest('.vtr-03__row');
    const li = row.parentElement;
    if (!document.startViewTransition || reduce.matches) { move(row); li.remove(); return; }
    busy = true;
    row.style.viewTransitionName = 'vtr-03-active';
    try { await document.startViewTransition(() => { move(row); li.remove(); }).finished; }
    finally { row.style.viewTransitionName = ''; busy = false; }
  });
})();
```
