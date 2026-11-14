---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/exit-and-enter-timing-without-overlap/"
title: "Exit and Enter Timing Without Overlap"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "Two strategies, run side by side from one control so the difference is felt rather than described."
has_js: "true"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Exit and Enter Timing Without Overlap
Source: https://codefronts.com/motion/css-page-transitions/exit-and-enter-timing-without-overlap/

Two strategies, run side by side from one control so the difference is felt rather than described. Sequential animates the outgoing route out and then the incoming route in &mdash; safe, never overlapping, but the total is the sum of both halves and starts to feel sluggish past about 500ms. Overlapping runs both at once for a faster, smoother change, at the cost of having two routes in the DOM together, which needs absolute positioning and a height strategy.
## HTML
```html
<section class="pt-02" aria-labelledby="pt-02-h">
  <div class="pt-02__theme">
    <input class="pt-02__theme-input" type="checkbox" id="pt-02-theme">
    <label class="pt-02__theme-label" for="pt-02-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-02__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-02__stage">
    <header class="pt-02__head">
      <p class="pt-02__kicker">Page transitions / 02</p>
      <h2 class="pt-02__h" id="pt-02-h">Exit then enter, or both at once</h2>
      <p class="pt-02__lede">Both panes swap the same two routes with the same easing. Only the ordering differs. Routes are swapped in place by this demo&rsquo;s script &mdash; no router, no navigation.</p>
      <button class="pt-02__run" type="button" id="pt-02-run">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M8 5.5v13l11-6.5Z" fill="currentColor"/></svg>
        Run both transitions
      </button>
    </header>

    <div class="pt-02__grid">
      <article class="pt-02__pane" data-pt-02-mode="seq">
        <header class="pt-02__pane-head">
          <h3 class="pt-02__pane-h">Sequential</h3>
          <p class="pt-02__pane-sub">600ms total &mdash; 300 out, then 300 in</p>
        </header>
        <div class="pt-02__view">
          <div class="pt-02__overlay" aria-hidden="true"></div>
          <div class="pt-02__routes pt-02__routes--flow" data-pt-02-routes>
            <div class="pt-02__route" data-pt-02-route="a">
              <p class="pt-02__eyebrow">Inbox</p>
              <h4 class="pt-02__title">Fern &mdash; contract review</h4>
              <p class="pt-02__text">Sam Rivera left three comments on clause 4. Redlines are attached to the thread.</p>
              <p class="pt-02__meta">Received 09:14 &middot; 2 attachments</p>
            </div>
            <div class="pt-02__route" data-pt-02-route="b" hidden>
              <p class="pt-02__eyebrow">Archive</p>
              <h4 class="pt-02__title">Vale &mdash; renewal terms</h4>
              <p class="pt-02__text">Signed and filed. The renewal window opens in eleven weeks and auto-reminds the account owner.</p>
              <p class="pt-02__meta">Archived 14 Mar &middot; Jordan Lee</p>
            </div>
          </div>
        </div>
        <div class="pt-02__bars">
          <span class="pt-02__bar pt-02__bar--out" style="--pt-02-span:300"><i></i>exit 300ms</span>
          <span class="pt-02__bar pt-02__bar--in" style="--pt-02-span:300"><i></i>enter 300ms</span>
        </div>
      </article>

      <article class="pt-02__pane" data-pt-02-mode="over">
        <header class="pt-02__pane-head">
          <h3 class="pt-02__pane-h">Overlapping</h3>
          <p class="pt-02__pane-sub">320ms total &mdash; both halves share the window</p>
        </header>
        <div class="pt-02__view">
          <div class="pt-02__overlay" aria-hidden="true"></div>
          <div class="pt-02__routes pt-02__routes--stack" data-pt-02-routes>
            <div class="pt-02__route" data-pt-02-route="a">
              <p class="pt-02__eyebrow">Inbox</p>
              <h4 class="pt-02__title">Fern &mdash; contract review</h4>
              <p class="pt-02__text">Sam Rivera left three comments on clause 4. Redlines are attached to the thread.</p>
              <p class="pt-02__meta">Received 09:14 &middot; 2 attachments</p>
            </div>
            <div class="pt-02__route" data-pt-02-route="b" hidden>
              <p class="pt-02__eyebrow">Archive</p>
              <h4 class="pt-02__title">Vale &mdash; renewal terms</h4>
              <p class="pt-02__text">Signed and filed. The renewal window opens in eleven weeks and auto-reminds the account owner.</p>
              <p class="pt-02__meta">Archived 14 Mar &middot; Jordan Lee</p>
            </div>
          </div>
        </div>
        <div class="pt-02__bars">
          <span class="pt-02__bar pt-02__bar--both" style="--pt-02-span:320"><i></i>exit + enter 320ms</span>
        </div>
      </article>
    </div>

    <p class="pt-02__foot">Overlapping keeps two routes mounted for 320ms, so its pane stacks them with <code>position: absolute</code> inside a stage of fixed block size. Left in normal flow they would double the document height for the duration.</p>
  </div>
</section>
```
## CSS
```css
.pt-02 {
  --pt-02-bg: #f7f4ee;
  --pt-02-surf: #fffdf9;
  --pt-02-surf2: #efe9de;
  --pt-02-line: #ddd4c4;
  --pt-02-ink: #211d17;
  --pt-02-mut: #6b6153;
  --pt-02-acc: #9a4a1f;
  --pt-02-acc2: #2f5d50;
  --pt-02-shadow: 0 1px 2px rgba(33, 29, 23, 0.06), 0 8px 24px -12px rgba(33, 29, 23, 0.18);
  --pt-02-font-display: Georgia, "Iowan Old Style", "Times New Roman", serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-02-bg);
  color: var(--pt-02-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.pt-02 *,
.pt-02 *::before,
.pt-02 *::after {
  box-sizing: border-box;
}

.pt-02:has(.pt-02__theme-input:checked) {
  --pt-02-bg: #17140f;
  --pt-02-surf: #1f1b15;
  --pt-02-surf2: #272219;
  --pt-02-line: #3a3227;
  --pt-02-ink: #f4efe5;
  --pt-02-mut: #a89c88;
  --pt-02-acc: #e08a54;
  --pt-02-acc2: #7fbfa9;
  --pt-02-shadow: 0 1px 2px rgba(0, 0, 0, 0.5), 0 10px 28px -14px rgba(0, 0, 0, 0.7);
}

@media (prefers-color-scheme: dark) {
  .pt-02 {
    --pt-02-bg: #17140f;
    --pt-02-surf: #1f1b15;
    --pt-02-surf2: #272219;
    --pt-02-line: #3a3227;
    --pt-02-ink: #f4efe5;
    --pt-02-mut: #a89c88;
    --pt-02-acc: #e08a54;
    --pt-02-acc2: #7fbfa9;
    --pt-02-shadow: 0 1px 2px rgba(0, 0, 0, 0.5), 0 10px 28px -14px rgba(0, 0, 0, 0.7);
  }

  .pt-02:has(.pt-02__theme-input:checked) {
    --pt-02-bg: #f7f4ee;
    --pt-02-surf: #fffdf9;
    --pt-02-surf2: #efe9de;
    --pt-02-line: #ddd4c4;
    --pt-02-ink: #211d17;
    --pt-02-mut: #6b6153;
    --pt-02-acc: #9a4a1f;
    --pt-02-acc2: #2f5d50;
    --pt-02-shadow: 0 1px 2px rgba(33, 29, 23, 0.06), 0 8px 24px -12px rgba(33, 29, 23, 0.18);
  }
}

@media (prefers-color-scheme: light) {
  .pt-02:has(.pt-02__theme-input:checked) {
    --pt-02-bg: #17140f;
    --pt-02-surf: #1f1b15;
    --pt-02-surf2: #272219;
    --pt-02-line: #3a3227;
    --pt-02-ink: #f4efe5;
    --pt-02-mut: #a89c88;
    --pt-02-acc: #e08a54;
    --pt-02-acc2: #7fbfa9;
  }
}

@supports (color: oklch(0.5 0.1 40)) {
  .pt-02 {
    --pt-02-acc: oklch(0.5 0.14 45);
    --pt-02-acc2: oklch(0.45 0.07 168);
  }

  .pt-02:has(.pt-02__theme-input:checked) {
    --pt-02-acc: oklch(0.75 0.13 55);
    --pt-02-acc2: oklch(0.78 0.08 168);
  }

  @media (prefers-color-scheme: dark) {
    .pt-02 {
      --pt-02-acc: oklch(0.75 0.13 55);
      --pt-02-acc2: oklch(0.78 0.08 168);
    }

    .pt-02:has(.pt-02__theme-input:checked) {
      --pt-02-acc: oklch(0.5 0.14 45);
      --pt-02-acc2: oklch(0.45 0.07 168);
    }
  }
}

.pt-02__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-02__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 8;
}

.pt-02__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-02__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--pt-02-line);
  border-radius: 999px;
  background: var(--pt-02-surf);
  color: var(--pt-02-mut);
  cursor: pointer;
  box-shadow: var(--pt-02-shadow);
}

.pt-02__theme-label svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.pt-02__theme-input:focus-visible + .pt-02__theme-label {
  outline: 2px solid var(--pt-02-acc);
  outline-offset: 2px;
}

.pt-02__stage {
  max-inline-size: 72rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.5rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.5rem;
}

.pt-02__kicker {
  margin: 0 0 0.55rem;
  font-size: 0.74rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--pt-02-acc);
}

.pt-02__h {
  margin: 0 0 0.6rem;
  font-family: var(--pt-02-font-display);
  font-size: clamp(1.5rem, 4.6vw, 2.35rem);
  font-weight: 400;
  letter-spacing: -0.015em;
}

.pt-02__lede {
  margin: 0 0 1.1rem;
  max-inline-size: 44rem;
  color: var(--pt-02-mut);
  font-size: 0.96rem;
  text-wrap: pretty;
}

.pt-02__run {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  min-block-size: 2.75rem;
  padding: 0.5rem 1.1rem;
  border: 1px solid var(--pt-02-ink);
  border-radius: 999px;
  background: var(--pt-02-ink);
  color: var(--pt-02-bg);
  font: inherit;
  font-size: 0.92rem;
  font-weight: 600;
  cursor: pointer;
}

.pt-02__run svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.pt-02__run:hover {
  background: var(--pt-02-acc);
  border-color: var(--pt-02-acc);
}

.pt-02__run:focus-visible {
  outline: 2px solid var(--pt-02-acc);
  outline-offset: 3px;
}

.pt-02__run[disabled] {
  opacity: 0.55;
  cursor: progress;
}

.pt-02__grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.25rem;
}

@media (min-width: 52rem) {
  .pt-02__grid {
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  }
}

.pt-02__pane {
  min-inline-size: 0;
  display: grid;
  gap: 0.85rem;
  padding: 1.1rem;
  background: var(--pt-02-surf);
  border: 1px solid var(--pt-02-line);
  border-radius: 0.6rem;
  box-shadow: var(--pt-02-shadow);
}

.pt-02__pane-h {
  margin: 0 0 0.2rem;
  font-family: var(--pt-02-font-display);
  font-size: 1.15rem;
  font-weight: 400;
}

.pt-02__pane-sub {
  margin: 0;
  font-size: 0.78rem;
  letter-spacing: 0.02em;
  color: var(--pt-02-mut);
}

.pt-02__view {
  position: relative;
  overflow: hidden;
  min-inline-size: 0;
  block-size: 12.5rem;
  background: var(--pt-02-surf2);
  border-radius: 0.4rem;
}

.pt-02__overlay {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: var(--pt-02-ink);
  opacity: 0;
  pointer-events: none;
}

.pt-02__routes {
  position: relative;
  block-size: 100%;
}

.pt-02__routes--stack > .pt-02__route {
  position: absolute;
  inset: 0;
}

.pt-02__route {
  padding: 1rem 1.1rem;
  min-inline-size: 0;
}

.pt-02__route[hidden] {
  display: none;
}

.pt-02__eyebrow {
  margin: 0 0 0.4rem;
  font-size: 0.7rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--pt-02-acc2);
}

.pt-02__title {
  margin: 0 0 0.5rem;
  font-family: var(--pt-02-font-display);
  font-size: 1.1rem;
  font-weight: 400;
}

.pt-02__text {
  margin: 0 0 0.7rem;
  font-size: 0.9rem;
  color: var(--pt-02-mut);
  text-wrap: pretty;
}

.pt-02__meta {
  margin: 0;
  font-size: 0.76rem;
  color: var(--pt-02-mut);
  opacity: 0.85;
}

.pt-02__bars {
  display: grid;
  gap: 0.35rem;
}

.pt-02__bar {
  display: grid;
  gap: 0.25rem;
  font-size: 0.74rem;
  color: var(--pt-02-mut);
}

.pt-02__bar i {
  display: block;
  block-size: 0.35rem;
  border-radius: 999px;
  inline-size: calc(var(--pt-02-span) / 600 * 100%);
  background: var(--pt-02-line);
}

.pt-02__bar--out i {
  background: var(--pt-02-acc);
}

.pt-02__bar--in i {
  background: var(--pt-02-acc2);
}

.pt-02__bar--both i {
  background: linear-gradient(90deg, var(--pt-02-acc), var(--pt-02-acc2));
}

.pt-02__foot {
  margin: 0;
  font-size: 0.86rem;
  color: var(--pt-02-mut);
  max-inline-size: 52rem;
  text-wrap: pretty;
}

.pt-02__foot code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.86em;
}

@media (prefers-reduced-motion: reduce) {
  .pt-02__overlay {
    transition: none;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.pt-02');
const run = root.querySelector('#pt-02-run');
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const SEQ = 300, OVER = 320;
const timers = [];
const halves = (el, dir, ms, delay) => el.animate(
  dir === 'out'
    ? [{ opacity: 1, transform: 'none' }, { opacity: 0, transform: 'translateX(-1.5rem)' }]
    : [{ opacity: 0, transform: 'translateX(1.5rem)' }, { opacity: 1, transform: 'none' }],
  { duration: ms, delay, easing: 'cubic-bezier(0.4, 0, 0.2, 1)', fill: 'both' }
);
function swap(pane, mode) {
  const routes = [...pane.querySelectorAll('.pt-02__route')];
  const out = routes.find((r) => !r.hidden);
  const next = routes.find((r) => r !== out);
  const ov = pane.querySelector('.pt-02__overlay');
  const d = reduce.matches ? 0 : (mode === 'seq' ? SEQ : OVER);
  ov.animate([{ opacity: 0 }, { opacity: 0.14 }, { opacity: 0 }], { duration: mode === 'seq' ? d * 2 : d });
  if (mode === 'seq') {
    halves(out, 'out', d, 0);
    timers.push(setTimeout(() => { out.hidden = true; next.hidden = false; halves(next, 'in', d, 0); }, d));
  } else {
    halves(out, 'out', d, 0);
    next.hidden = false;
    halves(next, 'in', d, 0);
    timers.push(setTimeout(() => { out.hidden = true; }, d));
  }
}
function runBoth() {
  run.disabled = true;
  root.querySelectorAll('.pt-02__pane').forEach((p) => swap(p, p.getAttribute('data-pt-02-mode')));
  timers.push(setTimeout(() => { run.disabled = false; run.focus({ preventScroll: true }); }, reduce.matches ? 60 : SEQ * 2 + 40));
}
run.addEventListener('click', runBoth);
root.__ptCleanup = () => { timers.forEach(clearTimeout); run.replaceWith(run.cloneNode(true)); };
```
