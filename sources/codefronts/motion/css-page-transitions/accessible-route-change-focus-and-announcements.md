---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/accessible-route-change-focus-and-announcements/"
title: "Accessible Route Change Focus and Announcements"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "A client-side route change is invisible to assistive technology: the URL changes, the DOM swaps, and nothing is announced &mdash; often with focus stranded…"
has_js: "true"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Route Change Focus and Announcements
Source: https://codefronts.com/motion/css-page-transitions/accessible-route-change-focus-and-announcements/

A client-side route change is invisible to assistive technology: the URL changes, the DOM swaps, and nothing is announced &mdash; often with focus stranded on a link that no longer exists. Three parts fix it: move focus to the new route's heading, announce the new title through a polite live region, and keep the transition overlay out of the accessibility tree. The announcement log shows exactly what a screen reader would receive.
## HTML
```html
<section class="pt-09" aria-labelledby="pt-09-h">
  <div class="pt-09__theme">
    <input class="pt-09__theme-input" type="checkbox" id="pt-09-theme">
    <label class="pt-09__theme-label" for="pt-09-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-09__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-09__stage">
    <header class="pt-09__head">
      <p class="pt-09__kicker">Page transitions / 09</p>
      <h2 class="pt-09__h" id="pt-09-h">What a screen reader receives</h2>
      <p class="pt-09__lede">Routes are swapped in place by this demo&rsquo;s script. Every navigation moves focus to the new heading, writes one polite announcement, and leaves the overlay out of the accessibility tree.</p>
    </header>

    <div class="pt-09__cols">
      <nav class="pt-09__side" aria-label="Settings sections">
        <button class="pt-09__item pt-09__item--current" type="button" data-pt-09-route="profile">Profile</button>
        <button class="pt-09__item" type="button" data-pt-09-route="security">Security</button>
        <button class="pt-09__item" type="button" data-pt-09-route="notifications">Notifications</button>
      </nav>

      <div class="pt-09__view">
        <div class="pt-09__overlay" aria-hidden="true"></div>
        <main class="pt-09__route" id="pt-09-route">
          <h3 class="pt-09__title" id="pt-09-route-h" tabindex="-1">Profile</h3>
          <p class="pt-09__text">How you appear to everyone in the Ranger workspace.</p>
          <dl class="pt-09__fields">
            <div><dt>Name</dt><dd>Jordan Lee</dd></div>
            <div><dt>Handle</dt><dd>jordan</dd></div>
            <div><dt>Timezone</dt><dd>Europe/Lisbon</dd></div>
          </dl>
        </main>
      </div>

      <div class="pt-09__aside">
        <p class="pt-09__aside-t">Announcement log</p>
        <p class="pt-09__status" id="pt-09-live" role="status" aria-live="polite"></p>
        <ol class="pt-09__log" data-pt-09-log>
          <li><b>ready</b><span>Profile &mdash; heading focused</span></li>
        </ol>
        <p class="pt-09__aside-n">The live region above is the real one. The list mirrors it so the behaviour is visible without a screen reader.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.pt-09 {
  --pt-09-bg: #f7f7f8;
  --pt-09-s1: #ffffff;
  --pt-09-s2: #ededf0;
  --pt-09-line: #dcdce0;
  --pt-09-ink: #121214;
  --pt-09-mut: #5f6066;
  --pt-09-acc: #6d3ae0;
  --pt-09-font-display: "Helvetica Neue", "Segoe UI", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-09-bg);
  color: var(--pt-09-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.pt-09 *,
.pt-09 *::before,
.pt-09 *::after {
  box-sizing: border-box;
}

.pt-09:has(.pt-09__theme-input:checked) {
  --pt-09-bg: #0e0e10;
  --pt-09-s1: #16161a;
  --pt-09-s2: #1e1e23;
  --pt-09-line: #2a2a31;
  --pt-09-ink: #f2f2f4;
  --pt-09-mut: #9a9aa4;
  --pt-09-acc: #b092ff;
}

@media (prefers-color-scheme: dark) {
  .pt-09 {
    --pt-09-bg: #0e0e10;
    --pt-09-s1: #16161a;
    --pt-09-s2: #1e1e23;
    --pt-09-line: #2a2a31;
    --pt-09-ink: #f2f2f4;
    --pt-09-mut: #9a9aa4;
    --pt-09-acc: #b092ff;
  }

  .pt-09:has(.pt-09__theme-input:checked) {
    --pt-09-bg: #f7f7f8;
    --pt-09-s1: #ffffff;
    --pt-09-s2: #ededf0;
    --pt-09-line: #dcdce0;
    --pt-09-ink: #121214;
    --pt-09-mut: #5f6066;
    --pt-09-acc: #6d3ae0;
  }
}

@media (prefers-color-scheme: light) {
  .pt-09:has(.pt-09__theme-input:checked) {
    --pt-09-bg: #0e0e10;
    --pt-09-s1: #16161a;
    --pt-09-s2: #1e1e23;
    --pt-09-line: #2a2a31;
    --pt-09-ink: #f2f2f4;
    --pt-09-mut: #9a9aa4;
    --pt-09-acc: #b092ff;
  }
}

@supports (color: oklch(0.5 0.2 290)) {
  .pt-09 {
    --pt-09-acc: oklch(0.48 0.2 290);
  }

  .pt-09:has(.pt-09__theme-input:checked) {
    --pt-09-acc: oklch(0.78 0.13 290);
  }

  @media (prefers-color-scheme: dark) {
    .pt-09 {
      --pt-09-acc: oklch(0.78 0.13 290);
    }

    .pt-09:has(.pt-09__theme-input:checked) {
      --pt-09-acc: oklch(0.48 0.2 290);
    }
  }
}

.pt-09__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-09__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
}

.pt-09__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-09__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 0;
  background: transparent;
  color: var(--pt-09-mut);
  cursor: pointer;
}

.pt-09__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pt-09__theme-label:hover {
  color: var(--pt-09-ink);
}

.pt-09__theme-input:focus-visible + .pt-09__theme-label {
  outline: 2px solid var(--pt-09-acc);
  outline-offset: 2px;
}

.pt-09__stage {
  max-inline-size: 70rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.6rem;
}

.pt-09__kicker {
  margin: 0 0 0.45rem;
  font-size: 0.73rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--pt-09-acc);
}

.pt-09__h {
  margin: 0 0 0.5rem;
  font-family: var(--pt-09-font-display);
  font-size: clamp(1.4rem, 4.4vw, 2.1rem);
  font-weight: 600;
  letter-spacing: -0.02em;
}

.pt-09__lede {
  margin: 0;
  max-inline-size: 46rem;
  color: var(--pt-09-mut);
  font-size: 0.94rem;
  text-wrap: pretty;
}

.pt-09__cols {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.25rem;
  align-items: start;
}

@media (min-width: 54rem) {
  .pt-09__cols {
    grid-template-columns: 10.5rem minmax(0, 1fr) 15rem;
  }
}

.pt-09__side {
  display: grid;
  gap: 0.15rem;
  min-inline-size: 0;
}

.pt-09__item {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.7rem;
  border: 0;
  background: transparent;
  color: var(--pt-09-mut);
  font: inherit;
  font-size: 0.9rem;
  text-align: start;
  cursor: pointer;
  border-radius: 0.4rem;
}

.pt-09__item:hover {
  background: var(--pt-09-s2);
  color: var(--pt-09-ink);
}

.pt-09__item--current {
  color: var(--pt-09-acc);
  font-weight: 600;
}

.pt-09__item:focus-visible {
  outline: 2px solid var(--pt-09-acc);
  outline-offset: 2px;
}

.pt-09__view {
  position: relative;
  overflow: hidden;
  min-inline-size: 0;
  min-block-size: 15rem;
}

.pt-09__overlay {
  position: absolute;
  inset: 0;
  z-index: 3;
  background: var(--pt-09-bg);
  opacity: 0;
  pointer-events: none;
  transition: opacity 130ms linear;
}

.pt-09[data-pt-09-cover="1"] .pt-09__overlay {
  opacity: 1;
}

.pt-09__route {
  display: block;
  min-inline-size: 0;
}

.pt-09__title {
  margin: 0 0 0.5rem;
  font-family: var(--pt-09-font-display);
  font-size: 1.35rem;
  font-weight: 600;
  letter-spacing: -0.015em;
}

.pt-09__title:focus-visible {
  outline: 2px solid var(--pt-09-acc);
  outline-offset: 4px;
}

.pt-09__text {
  margin: 0 0 1.1rem;
  max-inline-size: 38rem;
  font-size: 0.93rem;
  color: var(--pt-09-mut);
  text-wrap: pretty;
}

.pt-09__fields {
  margin: 0;
  display: grid;
  gap: 0.75rem;
  max-inline-size: 34rem;
}

.pt-09__fields div {
  display: grid;
  grid-template-columns: minmax(0, 9rem) minmax(0, 1fr);
  gap: 0.5rem;
  padding-block-end: 0.75rem;
  border-block-end: 1px solid var(--pt-09-line);
}

.pt-09__fields dt {
  font-size: 0.82rem;
  color: var(--pt-09-mut);
}

.pt-09__fields dd {
  margin: 0;
  font-size: 0.9rem;
}

.pt-09__aside {
  min-inline-size: 0;
  display: grid;
  gap: 0.6rem;
  align-content: start;
  padding-inline-start: 1rem;
  border-inline-start: 1px solid var(--pt-09-line);
}

.pt-09__aside-t {
  margin: 0;
  font-size: 0.72rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--pt-09-mut);
}

.pt-09__status {
  margin: 0;
  font-size: 0.86rem;
  font-weight: 600;
  color: var(--pt-09-acc);
  min-block-size: 1.3rem;
}

.pt-09__log {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.45rem;
}

.pt-09__log li {
  display: grid;
  gap: 0.1rem;
  font-size: 0.8rem;
}

.pt-09__log b {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.7rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--pt-09-mut);
  font-weight: 400;
}

.pt-09__log span {
  color: var(--pt-09-ink);
}

.pt-09__aside-n {
  margin: 0.3rem 0 0;
  font-size: 0.76rem;
  color: var(--pt-09-mut);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .pt-09__overlay {
    transition-duration: 50ms;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.pt-09');
const view = root.querySelector('#pt-09-route');
const live = root.querySelector('#pt-09-live');
const log = root.querySelector('[data-pt-09-log]');
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const timers = [];
const pages = { profile: ['Profile', 'How you appear to everyone in the Ranger workspace.', [['Name', 'Jordan Lee'], ['Handle', 'jordan'], ['Timezone', 'Europe/Lisbon']]],
  security: ['Security', 'Sign-in methods and active sessions for this account.', [['Passkeys', '2 registered'], ['Recovery codes', '8 unused'], ['Sessions', '3 devices']]],
  notifications: ['Notifications', 'What Ranger sends you, and where it sends it.', [['Deploy failures', 'email and push'], ['Weekly digest', 'email'], ['Mentions', 'push']]] };
const note = (k, v) => { log.insertAdjacentHTML('afterbegin', '<li><b>' + k + '</b><span>' + v + '</span></li>');
  while (log.children.length > 5) log.lastElementChild.remove(); };
function go(key, btn) {
  root.setAttribute('data-pt-09-cover', '1');
  timers.push(setTimeout(() => {
    const [title, text, fields] = pages[key];
    view.innerHTML = '<h3 class="pt-09__title" id="pt-09-route-h" tabindex="-1">' + title + '</h3><p class="pt-09__text">' + text + '</p><dl class="pt-09__fields">' + fields.map((f) => '<div><dt>' + f[0] + '</dt><dd>' + f[1] + '</dd></div>').join('') + '</dl>';
    root.querySelectorAll('[data-pt-09-route]').forEach((b) => b.classList.toggle('pt-09__item--current', b === btn));
    root.querySelector('#pt-09-route-h').focus({ preventScroll: true });
    root.setAttribute('data-pt-09-cover', '0');
    live.textContent = title + ' — Ranger settings';
    note('focus', title + ' heading, tabindex -1');
    note('polite', title + ' — Ranger settings');
  }, reduce.matches ? 40 : 140));
}
root.querySelectorAll('[data-pt-09-route]').forEach((b) => b.addEventListener('click', () => go(b.getAttribute('data-pt-09-route'), b)));
root.__ptCleanup = () => { timers.forEach(clearTimeout); };
```
