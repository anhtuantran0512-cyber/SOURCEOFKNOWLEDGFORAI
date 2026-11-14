---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sticky-elements/detect-css-sticky-element-stuck-class/"
title: "Detect CSS Sticky Element Stuck Class"
section: "layouts"
category: "css-sticky-elements"
category_name: "CSS Sticky Elements"
description: "The question behind half the sticky questions: “how do I style it differently WHILE it's stuck?” This demo answers twice, live, with a HUD showing both…"
has_js: "true"
---

Here's a working CSS Sticky Element from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Detect CSS Sticky Element Stuck Class
Source: https://codefronts.com/layouts/css-sticky-elements/detect-css-sticky-element-stuck-class/

The question behind half the sticky questions: “how do I style it differently WHILE it's stuck?” This demo answers twice, live, with a HUD showing both sensors. Sensor one is 2026 CSS — container-type: scroll-state with @container scroll-state(stuck: top), zero JavaScript, fires the exact frame the pin engages. Sensor two is the 12-line IntersectionObserver sentinel that toggles an .is-stuck class everywhere else. Same declarations, two triggers — ship both today, delete the JS in a year or two.
## HTML
```html
<section class="cst-17" aria-label="Detect stuck sticky element demo">
  <div class="cst-17__stage" id="cst17-top">
    <section class="cst-17__hero">
      <p class="cst-17__kicker">Two sensors, one truth</p>
      <h1>It knows when<br>it's stuck.</h1>
      <p class="cst-17__sub">The toolbar below starts as a floating pill. The moment it pins, it stretches full-bleed, grows a blur and a shadow, and flips its badge to PINNED — detected by CSS <code>scroll-state(stuck: top)</code> where supported, and by an IntersectionObserver sentinel everywhere. The HUD shows both sensors live.</p>
      <div class="cst-17__hud" role="status">
        <span class="cst-17__chip">CSS scroll-state: <em data-cst17-css data-on="0">checking…</em></span>
        <span class="cst-17__chip">JS .is-stuck: <em data-cst17-js data-on="0">false</em></span>
      </div>
    </section>
    <div class="cst-17__sentinel" aria-hidden="true"></div>
    <div class="cst-17__pin">
      <div class="cst-17__bar">
        <span class="cst-17__state"><i aria-hidden="true"></i><b></b></span>
        <nav class="cst-17__filters" aria-label="Filter activity">
          <a href="#cst17-feed" aria-current="true">All</a>
          <a href="#cst17-feed">Deploys</a>
          <a href="#cst17-feed">Design</a>
          <a href="#cst17-feed">Reviews</a>
        </nav>
        <span class="cst-17__week">Wk 31</span>
      </div>
    </div>
    <main class="cst-17__feed" id="cst17-feed">
      <article><i style="--h:265">MA</i><p><strong>Miriam</strong> deployed <code>checkout-v9</code> to production — 0 regressions, 41s rollout</p><time>2m</time></article>
      <article><i style="--h:150">DO</i><p><strong>Dele</strong> merged the sticky-header refactor — scroll listeners deleted: <strong>7</strong></p><time>18m</time></article>
      <article><i style="--h:40">JP</i><p><strong>June</strong> posted 4 motion specs to the design system — reduced-motion variants included</p><time>1h</time></article>
      <article><i style="--h:320">TB</i><p><strong>Theo</strong> approved the checkout a11y review — WCAG 2.2 AA, zero blockers</p><time>2h</time></article>
      <article><i style="--h:200">HK</i><p><strong>Hana</strong> shipped tokens v12 — oklch everywhere, hex retired with honors</p><time>3h</time></article>
      <article><i style="--h:90">RS</i><p><strong>Rafael</strong> cut p95 LCP to <strong>1.4s</strong> on product pages — image priority hints</p><time>5h</time></article>
      <article><i style="--h:10">JT</i><p><strong>Jaya</strong> opened RFC-118: adopt scroll-state queries behind @supports</p><time>7h</time></article>
      <article><i style="--h:230">SO</i><p><strong>Sam</strong> A/B result: sticky add-to-cart bar +11.8% mobile conversion — shipping to 100%</p><time>9h</time></article>
      <article><i style="--h:120">AW</i><p><strong>Ada</strong> deleted 2,300 lines of scrollspy JS — replaced by 40 lines of CSS + one observer</p><time>Yesterday</time></article>
      <article><i style="--h:300">BC</i><p><strong>Bea</strong> refreshed the brand gradients — conic, tasteful, allegedly final</p><time>Yesterday</time></article>
      <article><i style="--h:170">CW</i><p><strong>Casey</strong> wired the data table's frozen columns (demo 10 pattern) into the ops dashboard</p><time>Tue</time></article>
      <article><i style="--h:60">MF</i><p><strong>Marco</strong> fixed the iOS safe-area padding on the bottom bar — env() max() combo</p><time>Tue</time></article>
    </main>
    <footer class="cst-17__footer"><p><strong>Pulse</strong> — a demo from the CodeFronts sticky-elements collection. Scroll back up: both sensors release in the same frame.</p><a href="#cst17-top">Back to top ↑</a></footer>
  </div>
</section>
```
## CSS
```css
.cst-17,
.cst-17 *,
.cst-17 *::before,
.cst-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cst-17 {
  --bg: oklch(0.17 0.012 265);
  --pane: oklch(0.22 0.015 265);
  --ink: oklch(0.93 0.006 265);
  --mut: oklch(0.66 0.012 265);
  --line: oklch(0.32 0.018 265);
  --acc: oklch(0.85 0.19 130);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.cst-17__stage {
  width: 100%;
  container: cst17/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
  scroll-behavior: smooth;
}

.cst-17__hero {
  min-height: 74svh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 44px clamp(20px,5cqi,56px);
  background: radial-gradient(70cqi 50cqi at 85% 10%,oklch(0.3 0.06 130/.35),transparent 65%),radial-gradient(60cqi 45cqi at 0% 100%,oklch(0.28 0.05 265/.6),transparent 70%);
}

.cst-17__kicker {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--acc);
  margin-bottom: 14px;
}

.cst-17__hero h1 {
  font-size: clamp(42px,9cqi,100px);
  line-height: .94;
  letter-spacing: -.04em;
  font-weight: 800;
}

.cst-17__sub {
  margin-top: 20px;
  max-width: 58ch;
  font-size: 15px;
  line-height: 1.7;
  color: var(--mut);
}

.cst-17__sub code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .87em;
  background: oklch(0.27 0.02 265);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--ink);
}

.cst-17__hud {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 26px;
}

.cst-17__chip {
  display: flex;
  align-items: center;
  gap: 7px;
  min-height: 38px;
  padding: 0 14px;
  border-radius: 99px;
  border: 1px solid var(--line);
  background: oklch(0.2 0.014 265);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  color: var(--mut);
}

.cst-17__chip em {
  font-style: normal;
  font-weight: 700;
  color: var(--mut);
}

.cst-17__chip em[data-on="1"] {
  color: var(--acc);
}

.cst-17__sentinel {
  height: 1px;
}

.cst-17__pin {
  position: sticky;
  top: 0;
  z-index: 8;
  container-type: scroll-state;
}

.cst-17__bar {
  display: flex;
  align-items: center;
  gap: clamp(10px,2cqi,18px);
  width: 100%;
  max-width: 640px;
  margin-inline: auto;
  min-height: 56px;
  padding: 8px clamp(12px,2.5cqi,18px);
  border-radius: 99px;
  background: oklch(0.26 0.02 265);
  border: 1px solid var(--line);
  box-shadow: 0 8px 26px oklch(0 0 0/.35);
  transition: max-width .4s cubic-bezier(.2,.7,.2,1),border-radius .4s,background .3s,box-shadow .3s,border-color .3s;
}

.cst-17__state {
  display: flex;
  align-items: center;
  gap: 8px;
  min-width: 96px;
}

.cst-17__state i {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: oklch(0.6 0.03 265);
  box-shadow: 0 0 0 3px oklch(0.6 0.03 265/.25);
  transition: background .3s,box-shadow .3s;
}

.cst-17__state b {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--mut);
}

.cst-17__state b::after {
  content: "floating";
}

.cst-17__filters {
  display: flex;
  gap: 3px;
  margin-inline: auto;
  overflow-x: auto;
  scrollbar-width: none;
}

.cst-17__filters::-webkit-scrollbar {
  display: none;
}

.cst-17__filters a {
  display: grid;
  place-items: center;
  min-height: 40px;
  padding: 0 14px;
  border-radius: 99px;
  font-size: 12.5px;
  font-weight: 650;
  color: var(--mut);
  text-decoration: none;
  white-space: nowrap;
  transition: color .2s,background .2s;
}

.cst-17__filters a:hover,
.cst-17__filters a:focus-visible {
  color: var(--ink);
  background: oklch(0.3 0.02 265);
}

.cst-17__filters a[aria-current] {
  color: oklch(0.15 0.01 265);
  background: var(--acc);
}

.cst-17__filters a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cst-17__week {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  font-weight: 700;
  color: var(--mut);
  padding-right: 6px;
}

.cst-17__pin.is-stuck .cst-17__bar {
  max-width: 100%;
  border-radius: 0;
  background: color-mix(in oklch,oklch(0.19 0.015 265) 85%,transparent);
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
  border-color: transparent;
  border-bottom: 1px solid var(--line);
  box-shadow: 0 14px 40px oklch(0 0 0/.4);
}

.cst-17__pin.is-stuck .cst-17__state i {
  background: var(--acc);
  box-shadow: 0 0 0 3px oklch(0.85 0.19 130/.25);
}

.cst-17__pin.is-stuck .cst-17__state b {
  color: var(--acc);
}

.cst-17__pin.is-stuck .cst-17__state b::after {
  content: "pinned";
}

@supports (container-type: scroll-state) {
  @container scroll-state(stuck: top) {
    .cst-17__bar {
      max-width: 100%;
      border-radius: 0;
      background: color-mix(in oklch,oklch(0.19 0.015 265) 85%,transparent);
      -webkit-backdrop-filter: blur(12px);
      backdrop-filter: blur(12px);
      border-color: transparent;
      border-bottom: 1px solid var(--line);
      box-shadow: 0 14px 40px oklch(0 0 0/.4);
    }

    .cst-17__state i {
      background: var(--acc);
      box-shadow: 0 0 0 3px oklch(0.85 0.19 130/.25);
    }

    .cst-17__state b {
      color: var(--acc);
    }

    .cst-17__state b::after {
      content: "pinned";
    }
  }
}

.cst-17__feed {
  display: grid;
  gap: 10px;
  padding: 26px clamp(20px,5cqi,56px) 34px;
  max-width: 860px;
  margin-inline: auto;
}

.cst-17__feed article {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 16px;
  border-radius: 14px;
  background: var(--pane);
  border: 1px solid var(--line);
  transition: border-color .2s,translate .2s;
}

.cst-17__feed article:hover {
  border-color: oklch(0.42 0.03 265);
  translate: 0 -1px;
}

.cst-17__feed i {
  flex: none;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-style: normal;
  font-size: 12px;
  font-weight: 800;
  color: oklch(0.15 0.01 265);
  background: linear-gradient(140deg,oklch(0.8 0.12 var(--h,130)),oklch(0.62 0.14 calc(var(--h,130) + 40)));
}

.cst-17__feed p {
  font-size: 13.5px;
  line-height: 1.55;
  color: var(--mut);
}

.cst-17__feed p strong {
  color: var(--ink);
  font-weight: 700;
}

.cst-17__feed p code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .88em;
  background: oklch(0.28 0.02 265);
  padding: 1px 6px;
  border-radius: 5px;
  color: var(--acc);
}

.cst-17__feed time {
  margin-left: auto;
  flex: none;
  font-size: 11.5px;
  color: oklch(0.55 0.012 265);
  font-variant-numeric: tabular-nums;
}

.cst-17__footer {
  display: flex;
  flex-wrap: wrap;
  gap: 14px 26px;
  align-items: center;
  justify-content: space-between;
  padding: 10px clamp(20px,5cqi,56px) 40px;
  max-width: 860px;
  margin-inline: auto;
}

.cst-17__footer p {
  font-size: 12.5px;
  color: var(--mut);
  max-width: 56ch;
}

.cst-17__footer a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 16px;
  border-radius: 11px;
  font-size: 13px;
  font-weight: 700;
  color: oklch(0.15 0.01 265);
  background: var(--acc);
  text-decoration: none;
  transition: translate .2s,filter .2s;
}

.cst-17__footer a:hover,
.cst-17__footer a:focus-visible {
  translate: 0 -2px;
  filter: brightness(1.08);
}

.cst-17__footer a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

@container cst17 (width < 560px) {
  .cst-17__week {
    display: none;
  }

  .cst-17__state {
    min-width: auto;
  }

  .cst-17__feed time {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cst-17__stage {
    scroll-behavior: auto;
  }

  .cst-17 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const stage = document.querySelector('.cst-17__stage');
  if (!stage || stage.dataset.stuckInit) return;
  stage.dataset.stuckInit = '1';
  const pin = stage.querySelector('.cst-17__pin');
  const sentinel = stage.querySelector('.cst-17__sentinel');
  const hudJs = stage.querySelector('[data-cst17-js]');
  const hudCss = stage.querySelector('[data-cst17-css]');
  if (hudCss) {
    const ok = typeof CSS !== 'undefined' && CSS.supports('container-type: scroll-state');
    hudCss.textContent = ok ? 'supported' : 'not here yet';
    hudCss.dataset.on = ok ? '1' : '0';
  }
  if (!pin || !sentinel) return;
  new IntersectionObserver(([entry]) => {
    const stuck = !entry.isIntersecting;
    pin.classList.toggle('is-stuck', stuck);
    if (hudJs) { hudJs.textContent = String(stuck); hudJs.dataset.on = stuck ? '1' : '0'; }
  }, { root: stage, threshold: 0 }).observe(sentinel);
})();
```
