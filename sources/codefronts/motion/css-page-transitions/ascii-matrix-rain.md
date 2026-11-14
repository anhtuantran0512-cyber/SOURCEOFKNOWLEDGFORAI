---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/ascii-matrix-rain/"
title: "Terminal Text Page Transition Overlay"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "A monospace overlay that types a short line while the route swaps, then clears."
has_js: "true"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Terminal Text Page Transition Overlay
Source: https://codefronts.com/motion/css-page-transitions/ascii-matrix-rain/

A monospace overlay that types a short line while the route swaps, then clears. It suits developer tooling, where a command line is the interface metaphor rather than a decoration. Two requirements are non-negotiable: the typed text is decorative, so the overlay is aria-hidden, and under reduced motion nothing types at all &mdash; the line appears complete and the swap happens immediately.
## HTML
```html
<section class="pt-19" aria-labelledby="pt-19-h">
  <div class="pt-19__theme">
    <input class="pt-19__theme-input" type="checkbox" id="pt-19-theme">
    <label class="pt-19__theme-label" for="pt-19-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-19__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-19__stage">
    <header class="pt-19__head">
      <p class="pt-19__kicker">Page transitions / 19</p>
      <h2 class="pt-19__h" id="pt-19-h">Type the cover, swap, clear</h2>
      <p class="pt-19__lede">Views are DOM sections swapped by this demo&rsquo;s script when the line finishes. The typed line is decorative and the overlay is hidden from assistive technology.</p>
    </header>

    <div class="pt-19__term">
      <div class="pt-19__bar">
        <span class="pt-19__dot"></span><span class="pt-19__dot"></span><span class="pt-19__dot"></span>
        <p class="pt-19__path">ranger@prod : ~/deployments</p>
      </div>

      <div class="pt-19__view">
        <div class="pt-19__overlay" aria-hidden="true">
          <p class="pt-19__typed"><span class="pt-19__prompt">$</span> <span data-pt-19-line></span><span class="pt-19__caret"></span></p>
        </div>
        <main class="pt-19__route" id="pt-19-route" tabindex="-1">
          <h3 class="pt-19__title">deployments</h3>
          <pre class="pt-19__out">ID       BRANCH        STATE     AGE
d-41ac   main          ready     4m
d-41ab   fix/session   building  9m
d-41a9   main          ready     1h
d-419f   chore/deps    error     3h</pre>
          <p class="pt-19__hint">4 deployments, 1 error. Promotion is a pointer move.</p>
        </main>
      </div>

      <nav class="pt-19__cmds" aria-label="Views">
        <button class="pt-19__cmd pt-19__cmd--current" type="button" data-pt-19-route="deployments">deployments</button>
        <button class="pt-19__cmd" type="button" data-pt-19-route="logs">logs</button>
        <button class="pt-19__cmd" type="button" data-pt-19-route="env">env</button>
      </nav>
    </div>
  </div>
</section>
```
## CSS
```css
.pt-19 {
  --pt-19-bg: #05080a;
  --pt-19-s1: #0a1013;
  --pt-19-s2: #0f171b;
  --pt-19-line: #1b2a30;
  --pt-19-ink: #d6f5e3;
  --pt-19-mut: #6d9385;
  --pt-19-acc: #46f08a;
  --pt-19-font-display: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-19-bg);
  color: var(--pt-19-ink);
  font-family: var(--pt-19-font-display);
  line-height: 1.55;
}

.pt-19 *,
.pt-19 *::before,
.pt-19 *::after {
  box-sizing: border-box;
}

.pt-19:has(.pt-19__theme-input:checked) {
  --pt-19-bg: #f2f6f3;
  --pt-19-s1: #ffffff;
  --pt-19-s2: #e8efea;
  --pt-19-line: #cfdcd4;
  --pt-19-ink: #0b1a12;
  --pt-19-mut: #4f6b5d;
  --pt-19-acc: #0d7a44;
}

@media (prefers-color-scheme: light) {
  .pt-19 {
    --pt-19-bg: #05080a;
    --pt-19-s1: #0a1013;
    --pt-19-s2: #0f171b;
    --pt-19-line: #1b2a30;
    --pt-19-ink: #d6f5e3;
    --pt-19-mut: #6d9385;
    --pt-19-acc: #46f08a;
  }

  .pt-19:has(.pt-19__theme-input:checked) {
    --pt-19-bg: #f2f6f3;
    --pt-19-s1: #ffffff;
    --pt-19-s2: #e8efea;
    --pt-19-line: #cfdcd4;
    --pt-19-ink: #0b1a12;
    --pt-19-mut: #4f6b5d;
    --pt-19-acc: #0d7a44;
  }
}

@media (prefers-color-scheme: dark) {
  .pt-19:has(.pt-19__theme-input:checked) {
    --pt-19-bg: #f2f6f3;
    --pt-19-s1: #ffffff;
    --pt-19-s2: #e8efea;
    --pt-19-line: #cfdcd4;
    --pt-19-ink: #0b1a12;
    --pt-19-mut: #4f6b5d;
    --pt-19-acc: #0d7a44;
  }
}

@supports (color: oklch(0.85 0.2 150)) {
  .pt-19 {
    --pt-19-acc: oklch(0.87 0.2 152);
  }

  .pt-19:has(.pt-19__theme-input:checked) {
    --pt-19-acc: oklch(0.5 0.13 152);
  }

  @media (prefers-color-scheme: dark) {
    .pt-19:has(.pt-19__theme-input:checked) {
      --pt-19-acc: oklch(0.5 0.13 152);
    }
  }
}

.pt-19__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-19__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
}

.pt-19__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-19__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--pt-19-line);
  background: var(--pt-19-s1);
  color: var(--pt-19-acc);
  cursor: pointer;
}

.pt-19__theme-label svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.pt-19__theme-input:focus-visible + .pt-19__theme-label {
  outline: 2px solid var(--pt-19-acc);
  outline-offset: 2px;
}

.pt-19__stage {
  max-inline-size: 58rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.4rem;
}

.pt-19__kicker {
  margin: 0 0 0.45rem;
  font-size: 0.72rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--pt-19-acc);
}

.pt-19__h {
  margin: 0 0 0.5rem;
  font-size: clamp(1.3rem, 4.2vw, 1.95rem);
  font-weight: 600;
  letter-spacing: -0.01em;
}

.pt-19__lede {
  margin: 0;
  max-inline-size: 42rem;
  color: var(--pt-19-mut);
  font-size: 0.88rem;
  text-wrap: pretty;
}

.pt-19__term {
  border: 1px solid var(--pt-19-line);
  border-radius: 0.5rem;
  overflow: hidden;
  background: var(--pt-19-s1);
}

.pt-19__bar {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.5rem 0.7rem;
  background: var(--pt-19-s2);
  border-block-end: 1px solid var(--pt-19-line);
}

.pt-19__dot {
  inline-size: 0.55rem;
  block-size: 0.55rem;
  border-radius: 999px;
  background: var(--pt-19-line);
}

.pt-19__dot:first-child {
  background: var(--pt-19-acc);
}

.pt-19__path {
  margin: 0 0 0 0.6rem;
  font-size: 0.74rem;
  color: var(--pt-19-mut);
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.pt-19__view {
  position: relative;
  overflow: hidden;
  min-inline-size: 0;
  min-block-size: 14rem;
}

.pt-19__overlay {
  position: absolute;
  inset: 0;
  z-index: 3;
  display: none;
  align-content: start;
  padding: clamp(0.9rem, 3vw, 1.4rem);
  background: var(--pt-19-bg);
  pointer-events: none;
}

.pt-19[data-pt-19-typing="1"] .pt-19__overlay {
  display: grid;
}

.pt-19__typed {
  margin: 0;
  font-size: 0.9rem;
  color: var(--pt-19-acc);
}

.pt-19__prompt {
  color: var(--pt-19-mut);
}

.pt-19__caret {
  display: inline-block;
  inline-size: 0.55em;
  block-size: 1em;
  margin-inline-start: 0.1em;
  background: var(--pt-19-acc);
  vertical-align: -0.15em;
  animation: pt-19-blink 900ms steps(1) infinite;
}

@keyframes pt-19-blink {
  0%,
    49% {
    opacity: 1;
  }

  50%,
    100% {
    opacity: 0;
  }
}

.pt-19__route {
  display: block;
  padding: clamp(0.9rem, 3vw, 1.4rem);
}

.pt-19__route:focus-visible {
  outline: 2px solid var(--pt-19-acc);
  outline-offset: -3px;
}

.pt-19__title {
  margin: 0 0 0.7rem;
  font-size: 0.9rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--pt-19-mut);
}

.pt-19__out {
  margin: 0 0 0.8rem;
  overflow-x: auto;
  font-size: 0.8rem;
  line-height: 1.8;
  color: var(--pt-19-ink);
}

.pt-19__hint {
  margin: 0;
  font-size: 0.78rem;
  color: var(--pt-19-mut);
}

.pt-19__cmds {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
  padding: 0.5rem;
  border-block-start: 1px solid var(--pt-19-line);
  background: var(--pt-19-s2);
}

.pt-19__cmd {
  min-block-size: 2.75rem;
  padding: 0.4rem 0.85rem;
  border: 1px solid var(--pt-19-line);
  background: transparent;
  color: var(--pt-19-mut);
  font: inherit;
  font-size: 0.8rem;
  cursor: pointer;
}

.pt-19__cmd--current {
  border-color: var(--pt-19-acc);
  color: var(--pt-19-acc);
}

.pt-19__cmd:focus-visible {
  outline: 2px solid var(--pt-19-acc);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .pt-19__caret {
    animation: none;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.pt-19');
const view = root.querySelector('#pt-19-route');
const lineEl = root.querySelector('[data-pt-19-line]');
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const timers = []; let typer = null; let busy = false;
const pages = {
  deployments: ['ranger ls deployments', 'deployments', 'ID       BRANCH        STATE     AGE\nd-41ac   main          ready     4m\nd-41ab   fix/session   building  9m\nd-41a9   main          ready     1h\nd-419f   chore/deps    error     3h', '4 deployments, 1 error. Promotion is a pointer move.'],
  logs: ['ranger logs --tail 4', 'logs', '14:02:11  info   promoted d-41ac to production\n14:02:09  info   health check passed in 4 regions\n13:58:44  warn   cold start 812ms on eu-west\n13:51:02  error  build d-419f exceeded memory', 'Streamed live. Retention is 30 days.'],
  env: ['ranger env list', 'env', 'KEY               SCOPE        UPDATED\nDATABASE_URL      production   2d ago\nSESSION_SECRET    production   11d ago\nFEATURE_SPLIT     preview      4h ago', 'Values are write-only once set.']
};
function go(key, btn) {
  if (busy || btn.classList.contains('pt-19__cmd--current')) return;
  busy = true;
  const [cmd, title, out, hint] = pages[key];
  root.setAttribute('data-pt-19-typing', '1');
  const finish = () => {
    view.innerHTML = '<h3 class="pt-19__title">' + title + '</h3><pre class="pt-19__out">' + out + '</pre><p class="pt-19__hint">' + hint + '</p>';
    root.querySelectorAll('[data-pt-19-route]').forEach((c) => c.classList.toggle('pt-19__cmd--current', c === btn));
    view.focus({ preventScroll: true });
    timers.push(setTimeout(() => { root.setAttribute('data-pt-19-typing', '0'); lineEl.textContent = ''; busy = false; }, 160));
  };
  if (reduce.matches) { lineEl.textContent = cmd; timers.push(setTimeout(finish, 120)); return; }
  let i = 0; lineEl.textContent = '';
  typer = setInterval(() => {
    lineEl.textContent = cmd.slice(0, ++i);
    if (i >= cmd.length) { clearInterval(typer); typer = null; timers.push(setTimeout(finish, 180)); }
  }, 22);
}
root.querySelectorAll('[data-pt-19-route]').forEach((b) => b.addEventListener('click', () => go(b.getAttribute('data-pt-19-route'), b)));
root.__ptCleanup = () => { if (typer) clearInterval(typer); timers.forEach(clearTimeout); root.setAttribute('data-pt-19-typing', '0'); };
```
