---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/slide-transition/"
title: "Slide Page Transition Left and Right"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "A directional slide where the direction comes from navigation intent rather than from the effect: moving forward through a flow slides one way, going back…"
has_js: "true"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Slide Page Transition Left and Right
Source: https://codefronts.com/motion/css-page-transitions/slide-transition/

A directional slide where the direction comes from navigation intent rather than from the effect: moving forward through a flow slides one way, going back slides the other. Built on a wizard with a progress rail, which is the case where direction carries the most meaning &mdash; the movement tells the user whether they advanced or retreated.
## HTML
```html
<section class="pt-11" aria-labelledby="pt-11-h">
  <div class="pt-11__theme">
    <input class="pt-11__theme-input" type="checkbox" id="pt-11-theme">
    <label class="pt-11__theme-label" for="pt-11-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-11__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-11__stage">
    <header class="pt-11__head">
      <p class="pt-11__kicker">Page transitions / 11</p>
      <h2 class="pt-11__h" id="pt-11-h">Direction comes from intent</h2>
      <p class="pt-11__lede">Steps are DOM sections swapped by this demo&rsquo;s script. Forward slides one way, back slides the other, and jumping through the rail picks the sign from the index difference.</p>
    </header>

    <div class="pt-11__wizard">
      <nav class="pt-11__rail" aria-label="Onboarding steps">
        <button class="pt-11__step pt-11__step--current" type="button" data-pt-11-step="0"><span class="pt-11__dot"></span>Workspace</button>
        <button class="pt-11__step" type="button" data-pt-11-step="1"><span class="pt-11__dot"></span>Members</button>
        <button class="pt-11__step" type="button" data-pt-11-step="2"><span class="pt-11__dot"></span>Regions</button>
        <button class="pt-11__step" type="button" data-pt-11-step="3"><span class="pt-11__dot"></span>Review</button>
      </nav>

      <div class="pt-11__view">
        <div class="pt-11__overlay" aria-hidden="true"></div>
        <main class="pt-11__route" id="pt-11-route" tabindex="-1">
          <p class="pt-11__eyebrow">Step 1 of 4</p>
          <h3 class="pt-11__title">Name the workspace</h3>
          <p class="pt-11__text">This is what collaborators see in the switcher. It can be changed later without breaking links.</p>
          <ul class="pt-11__fields">
            <li><b>Workspace</b><span>Aperture</span></li>
            <li><b>URL</b><span>aperture.orbit.dev</span></li>
          </ul>
        </main>
      </div>

      <div class="pt-11__actions">
        <button class="pt-11__btn" type="button" data-pt-11-move="-1">Back</button>
        <button class="pt-11__btn pt-11__btn--primary" type="button" data-pt-11-move="1">Continue</button>
        <p class="pt-11__dir">dir <b data-pt-11-dir>+1</b></p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.pt-11 {
  --pt-11-bg: #fdf2f8;
  --pt-11-s1: #ffffff;
  --pt-11-s2: #fce7f3;
  --pt-11-s3: #ede9fe;
  --pt-11-line: #f3d3e6;
  --pt-11-ink: #2b1b2c;
  --pt-11-mut: #7a5f78;
  --pt-11-acc: #b0409a;
  --pt-11-acc2: #6d5ae0;
  --pt-11-dir: 1;
  --pt-11-font-display: "Nunito", "Avenir Next", "Segoe UI Rounded", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-11-bg);
  color: var(--pt-11-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.pt-11 *,
.pt-11 *::before,
.pt-11 *::after {
  box-sizing: border-box;
}

.pt-11:has(.pt-11__theme-input:checked) {
  --pt-11-bg: #17111a;
  --pt-11-s1: #1f1725;
  --pt-11-s2: #2a1f31;
  --pt-11-s3: #241f3d;
  --pt-11-line: #3a2c44;
  --pt-11-ink: #f7edf6;
  --pt-11-mut: #b39cb2;
  --pt-11-acc: #f19ada;
  --pt-11-acc2: #a99bff;
}

@media (prefers-color-scheme: dark) {
  .pt-11 {
    --pt-11-bg: #17111a;
    --pt-11-s1: #1f1725;
    --pt-11-s2: #2a1f31;
    --pt-11-s3: #241f3d;
    --pt-11-line: #3a2c44;
    --pt-11-ink: #f7edf6;
    --pt-11-mut: #b39cb2;
    --pt-11-acc: #f19ada;
    --pt-11-acc2: #a99bff;
  }

  .pt-11:has(.pt-11__theme-input:checked) {
    --pt-11-bg: #fdf2f8;
    --pt-11-s1: #ffffff;
    --pt-11-s2: #fce7f3;
    --pt-11-s3: #ede9fe;
    --pt-11-line: #f3d3e6;
    --pt-11-ink: #2b1b2c;
    --pt-11-mut: #7a5f78;
    --pt-11-acc: #b0409a;
    --pt-11-acc2: #6d5ae0;
  }
}

@media (prefers-color-scheme: light) {
  .pt-11:has(.pt-11__theme-input:checked) {
    --pt-11-bg: #17111a;
    --pt-11-s1: #1f1725;
    --pt-11-s2: #2a1f31;
    --pt-11-s3: #241f3d;
    --pt-11-line: #3a2c44;
    --pt-11-ink: #f7edf6;
    --pt-11-mut: #b39cb2;
    --pt-11-acc: #f19ada;
    --pt-11-acc2: #a99bff;
  }
}

@supports (color: oklch(0.6 0.2 340)) {
  .pt-11 {
    --pt-11-acc: oklch(0.55 0.19 340);
    --pt-11-acc2: oklch(0.55 0.18 285);
  }

  .pt-11:has(.pt-11__theme-input:checked) {
    --pt-11-acc: oklch(0.8 0.13 340);
    --pt-11-acc2: oklch(0.79 0.11 285);
  }

  @media (prefers-color-scheme: dark) {
    .pt-11 {
      --pt-11-acc: oklch(0.8 0.13 340);
      --pt-11-acc2: oklch(0.79 0.11 285);
    }

    .pt-11:has(.pt-11__theme-input:checked) {
      --pt-11-acc: oklch(0.55 0.19 340);
      --pt-11-acc2: oklch(0.55 0.18 285);
    }
  }
}

.pt-11__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-11__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
}

.pt-11__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-11__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 0;
  border-radius: 1.4rem;
  background: var(--pt-11-s2);
  color: var(--pt-11-acc);
  cursor: pointer;
}

.pt-11__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pt-11__theme-input:focus-visible + .pt-11__theme-label {
  outline: 2px solid var(--pt-11-acc2);
  outline-offset: 2px;
}

.pt-11__stage {
  max-inline-size: 58rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.5rem;
}

.pt-11__kicker {
  margin: 0 0 0.45rem;
  font-family: var(--pt-11-font-display);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--pt-11-acc);
}

.pt-11__h {
  margin: 0 0 0.5rem;
  font-family: var(--pt-11-font-display);
  font-size: clamp(1.45rem, 4.6vw, 2.15rem);
  font-weight: 800;
  letter-spacing: -0.02em;
}

.pt-11__lede {
  margin: 0;
  max-inline-size: 42rem;
  color: var(--pt-11-mut);
  font-size: 0.94rem;
  text-wrap: pretty;
}

.pt-11__wizard {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1rem;
}

.pt-11__rail {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.pt-11__step {
  flex: 1 1 7rem;
  min-inline-size: 0;
  min-block-size: 2.75rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.45rem 0.7rem;
  border: 0;
  border-radius: 1.4rem;
  background: var(--pt-11-s1);
  color: var(--pt-11-mut);
  font-family: var(--pt-11-font-display);
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
}

.pt-11__dot {
  inline-size: 0.55rem;
  block-size: 0.55rem;
  border-radius: 999px;
  background: var(--pt-11-line);
  flex: none;
}

.pt-11__step--current {
  background: var(--pt-11-s3);
  color: var(--pt-11-ink);
}

.pt-11__step--current .pt-11__dot {
  background: var(--pt-11-acc2);
}

.pt-11__step--done .pt-11__dot {
  background: var(--pt-11-acc);
}

.pt-11__step:focus-visible {
  outline: 2px solid var(--pt-11-acc2);
  outline-offset: 2px;
}

.pt-11__view {
  position: relative;
  overflow: hidden;
  min-inline-size: 0;
  block-size: 14.5rem;
  background: var(--pt-11-s1);
  border-radius: 1.5rem;
}

.pt-11__overlay {
  position: absolute;
  inset: 0;
  z-index: 3;
  background: var(--pt-11-s2);
  opacity: 0;
  pointer-events: none;
  transition: opacity 150ms linear;
}

.pt-11[data-pt-11-cover="1"] .pt-11__overlay {
  opacity: 0.6;
}

.pt-11__route {
  position: absolute;
  inset: 0;
  padding: clamp(1rem, 3vw, 1.5rem);
  overflow-y: auto;
}

.pt-11__route:focus-visible {
  outline: 2px solid var(--pt-11-acc2);
  outline-offset: -3px;
}

.pt-11[data-pt-11-phase="out"] .pt-11__route {
  transform: translateX(calc(var(--pt-11-dir) * -14%));
  opacity: 0;
  transition: transform 170ms ease-in, opacity 170ms linear;
}

.pt-11[data-pt-11-phase="in"] .pt-11__route {
  animation: pt-11-enter 280ms cubic-bezier(0.16, 0.84, 0.24, 1) both;
}

@keyframes pt-11-enter {
  from {
    transform: translateX(calc(var(--pt-11-dir) * 14%));
    opacity: 0;
  }

  to {
    transform: none;
    opacity: 1;
  }
}

.pt-11__eyebrow {
  margin: 0 0 0.35rem;
  font-family: var(--pt-11-font-display);
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--pt-11-acc2);
}

.pt-11__title {
  margin: 0 0 0.55rem;
  font-family: var(--pt-11-font-display);
  font-size: 1.2rem;
  font-weight: 800;
  letter-spacing: -0.015em;
}

.pt-11__text {
  margin: 0 0 0.9rem;
  max-inline-size: 36rem;
  font-size: 0.9rem;
  color: var(--pt-11-mut);
  text-wrap: pretty;
}

.pt-11__fields {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.45rem;
  max-inline-size: 30rem;
}

.pt-11__fields li {
  display: flex;
  justify-content: space-between;
  gap: 0.6rem;
  min-inline-size: 0;
  padding: 0.5rem 0.75rem;
  background: var(--pt-11-s2);
  border-radius: 0.8rem;
  font-size: 0.85rem;
}

.pt-11__fields span {
  color: var(--pt-11-mut);
}

.pt-11__actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem;
}

.pt-11__btn {
  min-block-size: 2.75rem;
  padding: 0.5rem 1.2rem;
  border: 0;
  border-radius: 1.4rem;
  background: var(--pt-11-s2);
  color: var(--pt-11-ink);
  font-family: var(--pt-11-font-display);
  font-size: 0.9rem;
  font-weight: 700;
  cursor: pointer;
}

.pt-11__btn--primary {
  background: var(--pt-11-acc2);
  color: #fff;
}

.pt-11__btn[disabled] {
  opacity: 0.45;
  cursor: default;
}

.pt-11__btn:focus-visible {
  outline: 2px solid var(--pt-11-acc);
  outline-offset: 2px;
}

.pt-11__dir {
  margin: 0 0 0 auto;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.76rem;
  color: var(--pt-11-mut);
}

.pt-11__dir b {
  color: var(--pt-11-acc);
}

@media (prefers-reduced-motion: reduce) {
  .pt-11[data-pt-11-phase="out"] .pt-11__route {
    transform: none;
    transition-duration: 60ms;
  }

  .pt-11[data-pt-11-phase="in"] .pt-11__route {
    animation: none;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.pt-11');
const view = root.querySelector('#pt-11-route');
const steps = [...root.querySelectorAll('[data-pt-11-step]')];
const dirOut = root.querySelector('[data-pt-11-dir]');
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const timers = []; let at = 0;
const data = [
  ['Name the workspace', 'This is what collaborators see in the switcher. It can be changed later without breaking links.', [['Workspace', 'Aperture'], ['URL', 'aperture.orbit.dev']]],
  ['Invite members', 'Invitations expire after seven days. Roles can be changed at any time.', [['Admins', 'Priya Sharma'], ['Editors', 'Alex Chen, Jordan Lee']]],
  ['Choose regions', 'Pick where workloads run first. Additional regions can be added without redeploying.', [['Primary', 'eu-west'], ['Failover', 'us-east']]],
  ['Review', 'Nothing is created until you confirm. Every value here is editable afterwards.', [['Workspace', 'Aperture'], ['Members', '3 invited'], ['Regions', 'eu-west, us-east']]]
];
function go(next) {
  if (next < 0 || next > data.length - 1 || next === at) return;
  const dir = next > at ? 1 : -1;
  at = next;
  root.style.setProperty('--pt-11-dir', dir);
  dirOut.textContent = dir > 0 ? '+1' : '-1';
  root.setAttribute('data-pt-11-cover', '1'); root.setAttribute('data-pt-11-phase', 'out');
  timers.push(setTimeout(() => {
    const [title, text, fields] = data[at];
    view.innerHTML = '<p class="pt-11__eyebrow">Step ' + (at + 1) + ' of 4</p><h3 class="pt-11__title">' + title + '</h3><p class="pt-11__text">' + text + '</p><ul class="pt-11__fields">' + fields.map((f) => '<li><b>' + f[0] + '</b><span>' + f[1] + '</span></li>').join('') + '</ul>';
    steps.forEach((s, i) => { s.classList.toggle('pt-11__step--current', i === at); s.classList.toggle('pt-11__step--done', i < at); });
    root.querySelector('[data-pt-11-move="-1"]').disabled = at === 0;
    root.querySelector('[data-pt-11-move="1"]').disabled = at === data.length - 1;
    view.focus({ preventScroll: true });
    root.setAttribute('data-pt-11-phase', 'in'); root.setAttribute('data-pt-11-cover', '0');
  }, reduce.matches ? 40 : 175));
}
steps.forEach((s) => s.addEventListener('click', () => go(Number(s.getAttribute('data-pt-11-step')))));
root.querySelectorAll('[data-pt-11-move]').forEach((b) => b.addEventListener('click', () => go(at + Number(b.getAttribute('data-pt-11-move')))));
root.querySelector('[data-pt-11-move="-1"]').disabled = true;
root.__ptCleanup = () => { timers.forEach(clearTimeout); };
```
