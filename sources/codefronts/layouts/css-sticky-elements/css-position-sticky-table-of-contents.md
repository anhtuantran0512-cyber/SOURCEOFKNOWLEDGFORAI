---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sticky-elements/css-position-sticky-table-of-contents/"
title: "CSS Position Sticky Table of Contents"
section: "layouts"
category: "css-sticky-elements"
category_name: "CSS Sticky Elements"
description: "The 'On this page' rail every documentation site ships: a sticky TOC that rides beside long-form content, highlights the section you're reading via a 14-line…"
has_js: "true"
---

Here's a working CSS Sticky Element from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Position Sticky Table of Contents
Source: https://codefronts.com/layouts/css-sticky-elements/css-position-sticky-table-of-contents/

The 'On this page' rail every documentation site ships: a sticky TOC that rides beside long-form content, highlights the section you're reading via a 14-line IntersectionObserver, and shows a reading-progress bar scrubbed by pure CSS animation-timeline: scroll(). The sticky part costs two declarations; the scrollspy is the smallest correct one you'll find — no scroll math, no throttling, no getBoundingClientRect.
## HTML
```html
<section class="cst-06" aria-label="Sticky table of contents demo">
  <div class="cst-06__stage" id="cst06-top">
    <header class="cst-06__mast">
      <a class="cst-06__brand" href="#cst06-top">stickydocs<span>/manual</span></a>
      <span class="cst-06__ver">v3.2</span>
    </header>
    <div class="cst-06__layout">
      <main class="cst-06__doc">
        <p class="cst-06__kicker">Reference · Layout</p>
        <h1>position: sticky — the missing manual</h1>
        <p class="cst-06__lede">Everything the spec means but doesn't say out loud, in six short sections. The rail on the right is the demo: sticky, scroll-spied, and progress-tracked.</p>
        <section id="cst06-model">
          <h2>1. How sticking actually works</h2>
          <p>A sticky element is relatively positioned until its box crosses the threshold you set with an inset property, then it becomes visually fixed — but only within the bounds of its containing block. It never leaves the layout: the space it occupied stays occupied, which is why sticky headers don't cause the content jump that fixed headers do.</p>
          <p>Think of it as an element on a leash. The leash is tied to its parent; the element may press against the viewport edge, but the moment the parent's far edge arrives, the leash pulls it away. Both behaviors — the pinning and the release — are the same mechanism.</p>
        </section>
        <section id="cst06-cage">
          <h2>2. The containing block is the cage</h2>
          <p>Sticky offsets are resolved against the nearest scrollport, but the element can never escape its containing block — its direct parent's padding box, usually. A sticky element inside a short parent has a short leash: it pins for a few pixels and immediately gets dragged off. This is a feature. Section headers in demo 07 use exactly this to push each other out of the way.</p>
          <p>The corollary: to make something stick longer, you don't touch the sticky element — you make its parent taller, or move the sticky up one level in the DOM.</p>
        </section>
        <section id="cst06-offsets">
          <h2>3. Offsets are thresholds, not positions</h2>
          <p><code>top: 24px</code> does not mean “place me 24px from the top.” It means “begin pinning when my top edge would cross 24px from the scrollport's top.” Before that moment the offset does nothing at all — which is why a sticky element with <code>top</code> set renders exactly where normal flow puts it on page load.</p>
          <p>You can set opposing offsets: an element with both <code>top</code> and <code>bottom</code> pins against whichever edge it approaches, useful for rails that should stay visible in both scroll directions.</p>
        </section>
        <section id="cst06-failures">
          <h2>4. The classic failure modes</h2>
          <p>Ninety percent of broken sticky is one of four bugs: an <code>overflow</code> value other than visible/clip on an ancestor (the ancestor becomes the scrollport — one that never scrolls); a stretched flex or grid child (no travel range); a parent exactly as tall as the element (no travel range again); or a missing inset property (no threshold, no pin).</p>
          <p>Demos 05 and 16 in this collection turn each of these into a visible, fixable example. Debug in that order — overflow first — and you'll rarely need more than a minute.</p>
        </section>
        <section id="cst06-a11y">
          <h2>5. Accessibility of pinned chrome</h2>
          <p>Pinned bars eat viewport. Respect three budgets: keep combined sticky chrome under ~30% of the smallest viewport you support; give every in-page anchor a <code>scroll-margin-top</code> so headings never land beneath the chrome; and make sure focus outlines aren't clipped by the pinned element's edge — a focused link half-hidden under a sticky header fails WCAG 2.4.11 (Focus Not Obscured).</p>
          <p>For screen reader users, sticking is invisible — the DOM order is the experience. Which is one more reason to prefer sticky (in-flow) over fixed (out-of-flow teleportation).</p>
        </section>
        <section id="cst06-modern">
          <h2>6. Where sticky meets 2026 CSS</h2>
          <p>Sticky is no longer a lone property; it's a system. <code>scroll-state(stuck)</code> container queries let descendants restyle when pinning happens (demo 17). <code>animation-timeline: scroll()</code> drives this page's progress bar without JavaScript. And <code>scroll-margin</code>/<code>scroll-padding</code> negotiate between anchors and pinned chrome.</p>
          <p>Learn the four failure modes, wire the offsets to custom properties, and sticky becomes the most dependable tool in the scroll UX kit.</p>
        </section>
      </main>
      <aside class="cst-06__toc" aria-label="On this page">
        <div class="cst-06__progress" aria-hidden="true"><i></i></div>
        <h3>On this page</h3>
        <nav>
          <a href="#cst06-model" aria-current="true">How sticking works</a>
          <a href="#cst06-cage">The containing block</a>
          <a href="#cst06-offsets">Offsets are thresholds</a>
          <a href="#cst06-failures">Classic failure modes</a>
          <a href="#cst06-a11y">Accessibility</a>
          <a href="#cst06-modern">Sticky in 2026</a>
        </nav>
        <a class="cst-06__ghfake" href="#cst06-top">Edit this page ↗</a>
      </aside>
    </div>
    <footer class="cst-06__footer"><p><strong>stickydocs</strong> — a demo from the CodeFronts sticky-elements collection.</p><a href="#cst06-top">Back to top ↑</a></footer>
  </div>
</section>
```
## CSS
```css
.cst-06,
.cst-06 *,
.cst-06 *::before,
.cst-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cst-06 {
  --bg: oklch(0.985 0.003 240);
  --ink: oklch(0.23 0.015 250);
  --mut: oklch(0.52 0.012 250);
  --line: oklch(0.91 0.006 250);
  --acc: oklch(0.55 0.16 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.cst-06__stage {
  width: 100%;
  container: cst06/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
  scroll-behavior: smooth;
}

.cst-06__mast {
  position: sticky;
  top: 0;
  z-index: 5;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 52px;
  padding: 0 clamp(18px,4cqi,44px);
  background: color-mix(in oklch,var(--bg) 85%,transparent);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
}

.cst-06__brand {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 14.5px;
  font-weight: 700;
  color: inherit;
  text-decoration: none;
}

.cst-06__brand span {
  color: var(--mut);
  font-weight: 400;
}

.cst-06__brand:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.cst-06__ver {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 99px;
  background: oklch(0.93 0.03 250/.6);
  color: var(--acc);
}

.cst-06__layout {
  display: grid;
  grid-template-columns: minmax(0,1fr) 248px;
  gap: clamp(24px,4cqi,56px);
  padding: clamp(26px,4.5cqi,50px) clamp(18px,4cqi,44px);
  align-items: start;
}

.cst-06__doc {
  max-width: 70ch;
}

.cst-06__kicker {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--acc);
  margin-bottom: 12px;
}

.cst-06__doc h1 {
  font-size: clamp(28px,4.6cqi,44px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 800;
  margin-bottom: 14px;
  text-wrap: balance;
}

.cst-06__lede {
  font-size: 16px;
  line-height: 1.6;
  color: var(--mut);
  margin-bottom: 10px;
}

.cst-06__doc section {
  padding-top: 26px;
  scroll-margin-top: 66px;
}

.cst-06__doc h2 {
  font-size: 20px;
  letter-spacing: -.015em;
  font-weight: 750;
  margin-bottom: 12px;
}

.cst-06__doc p {
  font-size: 14.5px;
  line-height: 1.75;
  color: oklch(0.36 0.015 250);
  margin-bottom: 13px;
}

.cst-06__doc code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .87em;
  background: oklch(0.925 0.01 250);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--ink);
}

.cst-06__toc {
  position: sticky;
  top: 66px;
  align-self: start;
  max-height: calc(100vh - 90px);
  max-height: calc(100svh - 90px);
  overflow: auto;
  padding: 16px 16px 14px;
  border-radius: 16px;
  background: oklch(1 0 0/.75);
  border: 1px solid var(--line);
  scrollbar-width: thin;
}

.cst-06__progress {
  height: 4px;
  border-radius: 99px;
  background: oklch(0.92 0.008 250);
  overflow: hidden;
  margin-bottom: 14px;
}

.cst-06__progress i {
  display: block;
  height: 100%;
  border-radius: 99px;
  background: linear-gradient(to right,var(--acc),oklch(0.7 0.13 200));
  transform-origin: left;
  scale: 0 1;
  animation: cst06-read linear both;
  animation-timeline: scroll(nearest);
}

@keyframes cst06-read {
  to {
    scale: 1 1;
  }
}

@supports not (animation-timeline: scroll()) {
  .cst-06__progress {
    display: none;
  }
}

.cst-06__toc h3 {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 8px;
}

.cst-06__toc nav {
  display: grid;
}

.cst-06__toc nav a {
  display: flex;
  align-items: center;
  min-height: 38px;
  padding: 0 10px;
  margin: 0 -4px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  border-left: 2px solid transparent;
  transition: color .2s,background .2s,border-color .2s;
}

.cst-06__toc nav a:hover,
.cst-06__toc nav a:focus-visible {
  color: var(--ink);
  background: oklch(0.94 0.008 250);
}

.cst-06__toc nav a[aria-current] {
  color: var(--acc);
  border-left-color: var(--acc);
  background: oklch(0.93 0.03 250/.5);
}

.cst-06__toc nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cst-06__ghfake {
  display: flex;
  align-items: center;
  min-height: 40px;
  margin-top: 10px;
  padding: 0 10px;
  border-top: 1px solid var(--line);
  font-size: 12px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
}

.cst-06__ghfake:hover,
.cst-06__ghfake:focus-visible {
  color: var(--acc);
}

.cst-06__ghfake:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 6px;
}

.cst-06__footer {
  display: flex;
  flex-wrap: wrap;
  gap: 14px 26px;
  align-items: center;
  justify-content: space-between;
  padding: 28px clamp(18px,4cqi,44px) 38px;
  border-top: 1px solid var(--line);
}

.cst-06__footer p {
  font-size: 12.5px;
  color: var(--mut);
}

.cst-06__footer a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 700;
  color: var(--ink);
  text-decoration: none;
  border: 1.5px solid var(--line);
  transition: border-color .2s;
}

.cst-06__footer a:hover,
.cst-06__footer a:focus-visible {
  border-color: var(--acc);
}

.cst-06__footer a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

@container cst06 (width < 660px) {
  .cst-06__layout {
    grid-template-columns: 1fr;
  }

  .cst-06__toc {
    position: static;
    max-height: none;
    order: -1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cst-06__stage {
    scroll-behavior: auto;
  }

  .cst-06__progress i {
    animation: none;
    scale: 1 1;
  }

  .cst-06 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const stage = document.querySelector('.cst-06__stage');
  if (!stage || stage.dataset.spyInit) return;
  stage.dataset.spyInit = '1';
  const links = [...stage.querySelectorAll('.cst-06__toc nav a')];
  const byId = new Map(links.map((a) => [a.getAttribute('href').slice(1), a]));
  const spy = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (!e.isIntersecting) continue;
      links.forEach((a) => a.removeAttribute('aria-current'));
      byId.get(e.target.id)?.setAttribute('aria-current', 'true');
    }
  }, { root: stage, rootMargin: '-15% 0px -75% 0px' });
  stage.querySelectorAll('.cst-06__doc section[id]').forEach((s) => spy.observe(s));
})();
```
