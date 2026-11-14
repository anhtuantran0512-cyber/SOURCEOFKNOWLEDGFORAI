---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sticky-elements/css-sticky-header-on-scroll-example/"
title: "CSS Sticky Header on Scroll Example"
section: "layouts"
category: "css-sticky-elements"
category_name: "CSS Sticky Elements"
description: "The canonical pattern, built the way it should be shipped in 2026: one declaration — position: sticky; top: 0 — pins the nav, backdrop-filter keeps content…"
has_js: "false"
---

Here's a working CSS Sticky Element from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sticky Header on Scroll Example
Source: https://codefronts.com/layouts/css-sticky-elements/css-sticky-header-on-scroll-example/

The canonical pattern, built the way it should be shipped in 2026: one declaration — position: sticky; top: 0 — pins the nav, backdrop-filter keeps content legible sliding beneath it, and scroll-padding-top stops anchor links from burying headings under the bar. No fixed-position layout jump, no body padding hack, no scroll listener. Everything else on the page is just proof it works.
## HTML
```html
<section class="cst-01" aria-label="CSS sticky header on scroll demo">
  <div class="cst-01__stage" id="cst01-top">
    <a class="cst-01__skip" href="#cst01-main">Skip to content</a>
    <header class="cst-01__header">
      <a class="cst-01__brand" href="#cst01-top"><i aria-hidden="true"></i>Relay</a>
      <nav class="cst-01__nav" aria-label="Primary">
        <a href="#cst01-product">Product</a>
        <a href="#cst01-uptime">Uptime</a>
        <a href="#cst01-pricing">Pricing</a>
        <a href="#cst01-docs">Docs</a>
      </nav>
      <a class="cst-01__cta" href="#cst01-pricing">Start free</a>
    </header>
    <main id="cst01-main">
      <section class="cst-01__hero">
        <p class="cst-01__kicker">Status pages, minus the panic</p>
        <h1>The header stays.<br>The page moves on.</h1>
        <p class="cst-01__sub">Scroll — the nav above is <code>position: sticky; top: 0</code>. It keeps its slot in the layout, then pins to the viewport the moment it would leave. No jump, no body-padding hack, no JavaScript.</p>
        <div class="cst-01__actions">
          <a class="cst-01__btn cst-01__btn--solid" href="#cst01-product">See it stick ↓</a>
          <a class="cst-01__btn" href="#cst01-docs">Read the docs</a>
        </div>
        <dl class="cst-01__stats">
          <div><dt>99.99%</dt><dd>uptime SLA</dd></div>
          <div><dt>0px</dt><dd>layout shift on pin</dd></div>
          <div><dt>1 line</dt><dd>of CSS to enable</dd></div>
        </dl>
      </section>
      <section class="cst-01__band" id="cst01-product">
        <h2>Why sticky beats fixed</h2>
        <div class="cst-01__cards">
          <article><span>01</span><h3>No layout jump</h3><p>A sticky header keeps its slot in normal flow, so the page never lurches by 64px the way it does the frame a header turns <code>position: fixed</code>.</p></article>
          <article><span>02</span><h3>No padding hacks</h3><p>Fixed headers force a matching <code>padding-top</code> on the body — and a second edit every time the header height changes. Sticky needs nothing.</p></article>
          <article><span>03</span><h3>Scoped by design</h3><p>Sticky pins inside its parent and its scroll container, so it can retire at a section boundary instead of haunting the entire page.</p></article>
        </div>
      </section>
      <section class="cst-01__band cst-01__band--tint" id="cst01-uptime">
        <h2>Anchors respect the header</h2>
        <p class="cst-01__lede">Every in-page link on this demo lands 76px early, because the scroller declares <code>scroll-padding-top: 76px</code>. Headings are never buried under the pinned bar — try the nav links above.</p>
        <div class="cst-01__ticks" role="img" aria-label="90-day uptime, one bar per day, all above 99.9 percent">
          <i style="--h:82%"></i><i style="--h:96%"></i><i style="--h:90%"></i><i style="--h:100%"></i><i style="--h:94%"></i><i style="--h:88%"></i><i style="--h:98%"></i><i style="--h:92%"></i><i style="--h:100%"></i><i style="--h:85%"></i><i style="--h:97%"></i><i style="--h:91%"></i><i style="--h:100%"></i><i style="--h:95%"></i><i style="--h:89%"></i><i style="--h:99%"></i><i style="--h:93%"></i><i style="--h:86%"></i><i style="--h:100%"></i><i style="--h:96%"></i><i style="--h:90%"></i><i style="--h:98%"></i><i style="--h:84%"></i><i style="--h:100%"></i><i style="--h:92%"></i><i style="--h:97%"></i><i style="--h:88%"></i><i style="--h:100%"></i>
        </div>
      </section>
      <section class="cst-01__cta-band" id="cst01-pricing">
        <h2>Free for 3 status pages</h2>
        <p>No card. No sales call. One sticky header, forever.</p>
        <a class="cst-01__btn cst-01__btn--solid" href="#cst01-top">Back to top ↑</a>
      </section>
      <footer class="cst-01__footer" id="cst01-docs">
        <div>
          <strong>Relay</strong>
          <p>A demo page from the CodeFronts sticky-elements collection. The footer exists so the header has somewhere to be sticky <em>from</em>.</p>
        </div>
        <nav aria-label="Footer"><a href="#cst01-top">Top</a><a href="#cst01-product">Product</a><a href="#cst01-uptime">Uptime</a><a href="#cst01-pricing">Pricing</a></nav>
      </footer>
    </main>
  </div>
</section>
```
## CSS
```css
.cst-01,
.cst-01 *,
.cst-01 *::before,
.cst-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cst-01 {
  --bg: oklch(0.98 0.004 250);
  --ink: oklch(0.21 0.02 255);
  --mut: oklch(0.5 0.015 255);
  --line: oklch(0.9 0.008 255);
  --acc: oklch(0.55 0.21 262);
  --navH: 64px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.cst-01__stage {
  width: 100%;
  container: cst01/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
  scroll-padding-top: 76px;
  scroll-behavior: smooth;
}

.cst-01__skip {
  position: absolute;
  z-index: 20;
  left: 16px;
  top: -60px;
  padding: 10px 16px;
  border-radius: 0 0 10px 10px;
  background: var(--ink);
  color: var(--bg);
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  transition: translate .2s;
}

.cst-01__skip:focus-visible {
  translate: 0 60px;
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cst-01__header {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  gap: clamp(14px,3cqi,30px);
  height: var(--navH);
  padding: 0 clamp(18px,4cqi,40px);
  background: color-mix(in oklch,var(--bg) 78%,transparent);
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid color-mix(in oklch,var(--line) 80%,transparent);
}

.cst-01__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.cst-01__brand i {
  width: 12px;
  height: 12px;
  border-radius: 3px;
  rotate: 45deg;
  background: conic-gradient(from 40deg,var(--acc),oklch(0.72 0.14 200),var(--acc));
}

.cst-01__nav {
  display: flex;
  gap: 2px;
  margin-inline: auto;
}

.cst-01__nav a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 13px;
  border-radius: 9px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  transition: color .2s,background .2s;
}

.cst-01__nav a:hover,
.cst-01__nav a:focus-visible {
  color: var(--ink);
  background: oklch(0.93 0.01 255);
}

.cst-01__nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cst-01__cta {
  display: grid;
  place-items: center;
  min-height: 38px;
  padding: 0 16px;
  border-radius: 99px;
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  color: oklch(0.99 0 0);
  background: var(--ink);
  transition: background .2s,translate .2s;
}

.cst-01__cta:hover,
.cst-01__cta:focus-visible {
  background: var(--acc);
  translate: 0 -1px;
}

.cst-01__cta:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-01__hero {
  min-height: calc(100svh - var(--navH));
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 56px clamp(18px,5cqi,48px);
  background: radial-gradient(90cqi 60cqi at 85% -10%,color-mix(in oklch,var(--acc) 14%,transparent),transparent 70%),radial-gradient(70cqi 50cqi at -10% 110%,oklch(0.9 0.05 200/.5),transparent 70%);
}

.cst-01__kicker {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
  margin-bottom: 14px;
}

.cst-01__hero h1 {
  font-size: clamp(38px,8cqi,76px);
  line-height: 1.02;
  letter-spacing: -.035em;
  font-weight: 800;
  max-width: 14ch;
}

.cst-01__sub {
  margin-top: 18px;
  max-width: 56ch;
  font-size: 15.5px;
  line-height: 1.65;
  color: var(--mut);
}

.cst-01__sub code,
.cst-01__band code,
.cst-01__lede code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .88em;
  background: oklch(0.93 0.012 255);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--ink);
}

.cst-01__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 26px;
}

.cst-01__btn {
  display: grid;
  place-items: center;
  min-height: 46px;
  padding: 0 20px;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 700;
  text-decoration: none;
  color: var(--ink);
  border: 1.5px solid var(--line);
  background: oklch(1 0 0/.6);
  transition: border-color .2s,translate .2s,background .2s;
}

.cst-01__btn:hover,
.cst-01__btn:focus-visible {
  border-color: var(--acc);
  translate: 0 -2px;
}

.cst-01__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-01__btn--solid {
  background: var(--acc);
  border-color: var(--acc);
  color: oklch(0.99 0 0);
}

.cst-01__btn--solid:hover,
.cst-01__btn--solid:focus-visible {
  background: color-mix(in oklch,var(--acc) 85%,black);
}

.cst-01__stats {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(20px,5cqi,54px);
  margin-top: clamp(30px,6cqi,60px);
}

.cst-01__stats dt {
  font-size: clamp(22px,3.4cqi,30px);
  font-weight: 800;
  letter-spacing: -.02em;
  font-variant-numeric: tabular-nums;
}

.cst-01__stats dd {
  font-size: 12.5px;
  color: var(--mut);
  margin-top: 2px;
}

.cst-01__band {
  padding: clamp(40px,8cqi,84px) clamp(18px,5cqi,48px);
  scroll-margin-top: 0;
}

.cst-01__band h2,
.cst-01__cta-band h2 {
  font-size: clamp(24px,4cqi,36px);
  letter-spacing: -.025em;
  font-weight: 800;
  margin-bottom: 22px;
}

.cst-01__band--tint {
  background: oklch(0.955 0.008 250);
}

.cst-01__cards {
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(auto-fit,minmax(min(230px,100%),1fr));
}

.cst-01__cards article {
  padding: 22px;
  border-radius: 16px;
  background: oklch(1 0 0);
  border: 1px solid var(--line);
  transition: translate .25s cubic-bezier(.2,.7,.2,1),box-shadow .25s;
}

.cst-01__cards article:hover {
  translate: 0 -3px;
  box-shadow: 0 12px 28px oklch(0.3 0.03 260/.08);
}

.cst-01__cards span {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  font-weight: 700;
  color: var(--acc);
}

.cst-01__cards h3 {
  font-size: 16.5px;
  letter-spacing: -.01em;
  margin: 8px 0 8px;
}

.cst-01__cards p {
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--mut);
}

.cst-01__lede {
  max-width: 62ch;
  font-size: 15px;
  line-height: 1.65;
  color: var(--mut);
}

.cst-01__ticks {
  display: flex;
  align-items: flex-end;
  gap: 4px;
  height: 120px;
  margin-top: 28px;
  padding: 16px;
  border-radius: 14px;
  background: oklch(1 0 0);
  border: 1px solid var(--line);
}

.cst-01__ticks i {
  flex: 1;
  height: var(--h);
  border-radius: 3px;
  background: linear-gradient(to top,var(--acc),oklch(0.72 0.14 200));
  opacity: .85;
}

.cst-01__cta-band {
  padding: clamp(44px,9cqi,90px) clamp(18px,5cqi,48px);
  text-align: center;
  background: linear-gradient(160deg,oklch(0.24 0.03 262),oklch(0.3 0.06 262));
  color: oklch(0.98 0 0);
}

.cst-01__cta-band h2 {
  margin-bottom: 8px;
}

.cst-01__cta-band p {
  color: oklch(0.8 0.02 255);
  margin-bottom: 24px;
  font-size: 14.5px;
}

.cst-01__cta-band .cst-01__btn--solid {
  display: inline-grid;
  background: oklch(0.98 0 0);
  border-color: oklch(0.98 0 0);
  color: oklch(0.24 0.03 262);
}

.cst-01__footer {
  display: flex;
  flex-wrap: wrap;
  gap: 26px;
  justify-content: space-between;
  align-items: flex-start;
  padding: 32px clamp(18px,5cqi,48px) 44px;
  border-top: 1px solid var(--line);
}

.cst-01__footer strong {
  font-size: 14px;
}

.cst-01__footer p {
  max-width: 44ch;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  margin-top: 6px;
}

.cst-01__footer nav {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
}

.cst-01__footer nav a {
  display: grid;
  place-items: center;
  min-height: 40px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 13px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
}

.cst-01__footer nav a:hover,
.cst-01__footer nav a:focus-visible {
  color: var(--ink);
  background: oklch(0.93 0.01 255);
}

.cst-01__footer nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

@container cst01 (width < 560px) {
  .cst-01__nav {
    display: none;
  }

  .cst-01__stats {
    gap: 20px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cst-01__stage {
    scroll-behavior: auto;
  }

  .cst-01 * {
    transition-duration: .01ms !important;
  }
}
```
