---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sticky-elements/css-position-sticky-not-working-overflow/"
title: "CSS Position Sticky Not Working Overflow"
section: "layouts"
category: "css-sticky-elements"
category_name: "CSS Sticky Elements"
description: "The bug lab for the most-Googled sticky question of all."
has_js: "false"
---

Here's a working CSS Sticky Element from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Position Sticky Not Working Overflow
Source: https://codefronts.com/layouts/css-sticky-elements/css-position-sticky-not-working-overflow/

The bug lab for the most-Googled sticky question of all. Two identical columns scroll side by side: in the left one, a wrapper with overflow: hidden silently murders the sticky pill; in the right one, the SAME wrapper uses overflow: clip — and the pill sticks perfectly. Because hidden creates a scroll container (one that never scrolls) while clip only clips. Below the lab: the 60-second debugging drill and the five failure modes ranked by how often they're the culprit.
## HTML
```html
<section class="cst-16" aria-label="Sticky not working because of overflow demo">
  <div class="cst-16__stage" id="cst16-top">
    <section class="cst-16__intro">
      <p class="cst-16__kicker">The bug lab · overflow vs sticky</p>
      <h1>Same CSS. One property apart.</h1>
      <p>Both pills below declare <code>position: sticky; top: 64px</code>. Their wrappers differ by ONE value — scroll and watch the left one die.</p>
    </section>
    <div class="cst-16__lab">
      <div class="cst-16__col">
        <p class="cst-16__tag cst-16__tag--bad"><span aria-hidden="true">✗</span>wrapper: overflow: hidden</p>
        <div class="cst-16__wrap cst-16__wrap--hidden">
          <p class="cst-16__pill cst-16__pill--bad">I never stick — my wrapper became my scrollport</p>
          <article><h3>Why it fails</h3><p>overflow: hidden turns the wrapper into a scroll container. The pill obediently pins to it — but the wrapper never scrolls, so the pin never engages. The property isn't broken; it's aimed at the wrong scroller.</p></article>
          <article><h3>The usual suspects</h3><p>A rounded-corner card clipping its image zoom. A section hiding a decorative blob. A carousel library's viewport div. All of them innocent-looking, all of them scroll containers.</p></article>
          <article><h3>The tell</h3><p>DevTools shows position: sticky computed and valid. No warning, no error. The element just… scrolls away like a normal block. Silence is the signature of this bug.</p></article>
          <article><h3>Depth doesn't matter</h3><p>The offender can be one level up or nine. Any hidden/auto/scroll ancestor between the pill and the page scroller claims the pin for itself.</p></article>
        </div>
      </div>
      <div class="cst-16__col">
        <p class="cst-16__tag cst-16__tag--good"><span aria-hidden="true">✓</span>wrapper: overflow: clip</p>
        <div class="cst-16__wrap cst-16__wrap--clip">
          <p class="cst-16__pill cst-16__pill--good">I stick at top: 64px — clip is not a scroll container</p>
          <article><h3>Why it works</h3><p>overflow: clip clips paint and nothing else. No scroll machinery, no scrollport, no claim on descendants — the pill keeps pinning to the real page scroller above.</p></article>
          <article><h3>Same clipping power</h3><p>Anything that bleeds past this wrapper is still sheared off, exactly like hidden — decorative overflow control without the positioning side effects.</p></article>
          <article><h3>Cheaper, too</h3><p>Clip boxes skip the scroll infrastructure entirely: no scroll events possible, no programmatic scrollTo, less engine bookkeeping. It's the value hidden always wanted to be.</p></article>
          <article><h3>Adopted everywhere</h3><p>Chrome 90, Firefox 81, Safari 16 — safe to ship since 2023. Most overflow: hidden in the wild can be find-and-replaced today.</p></article>
        </div>
      </div>
    </div>
    <section class="cst-16__drill">
      <h2>The 60-second debugging drill</h2>
      <p>Paste in DevTools with your sticky element selected — it names every ancestor that creates a scroll container:</p>
      <pre><code>let n = $0;   // your sticky element
while (n = n.parentElement){
  const o = getComputedStyle(n).overflow;
  if (!o.includes('visible') &amp;&amp; !o.includes('clip'))
    console.warn('sticky-breaker →', o, n);
}</code></pre>
      <ol class="cst-16__list">
        <li><strong>Overflow ancestor</strong> (this page) — swap to <code>overflow: clip</code>, or move the sticky above the wrapper.</li>
        <li><strong>Stretched flex/grid child</strong> — add <code>align-self: flex-start</code> / <code>start</code>. Full drill in demo 05.</li>
        <li><strong>Parent exactly as tall as the sticky</strong> — no travel range. Make the parent taller or hoist the sticky a level.</li>
        <li><strong>No inset declared</strong> — sticky without <code>top</code>/<code>bottom</code> has no threshold. Add <code>top: 0</code>.</li>
        <li><strong>Wrong scroller on purpose</strong> — an <code>overflow: auto</code> panel is a legit pin target (demos 07, 09). Confirm which scroller you MEANT.</li>
      </ol>
    </section>
    <footer class="cst-16__footer"><p><strong>The bug lab</strong> — a demo from the CodeFronts sticky-elements collection.</p><a href="#cst16-top">Back to top ↑</a></footer>
  </div>
</section>
```
## CSS
```css
.cst-16,
.cst-16 *,
.cst-16 *::before,
.cst-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cst-16 {
  --bg: oklch(0.975 0.003 280);
  --ink: oklch(0.23 0.015 280);
  --mut: oklch(0.51 0.012 280);
  --line: oklch(0.9 0.007 280);
  --bad: oklch(0.56 0.19 25);
  --good: oklch(0.55 0.15 150);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.cst-16__stage {
  width: 100%;
  container: cst16/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.cst-16__intro {
  padding: clamp(30px,6cqi,64px) clamp(18px,4cqi,44px) clamp(20px,3cqi,32px);
}

.cst-16__kicker {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--bad);
  margin-bottom: 12px;
}

.cst-16__intro h1 {
  font-size: clamp(30px,6cqi,60px);
  line-height: 1;
  letter-spacing: -.035em;
  font-weight: 800;
  margin-bottom: 14px;
}

.cst-16__intro p {
  max-width: 58ch;
  font-size: 15px;
  line-height: 1.6;
  color: var(--mut);
}

.cst-16__intro code,
.cst-16__drill p code,
.cst-16__list code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .87em;
  background: oklch(0.91 0.008 280);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--ink);
}

.cst-16__lab {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: clamp(12px,2.5cqi,24px);
  padding: 0 clamp(18px,4cqi,44px);
}

.cst-16__tag {
  position: sticky;
  top: 10px;
  z-index: 3;
  display: flex;
  align-items: center;
  gap: 8px;
  width: fit-content;
  min-height: 34px;
  padding: 0 13px;
  border-radius: 99px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  font-weight: 700;
  margin-bottom: 12px;
}

.cst-16__tag span {
  font-size: 13px;
}

.cst-16__tag--bad {
  color: oklch(0.98 0 0);
  background: var(--bad);
}

.cst-16__tag--good {
  color: oklch(0.98 0 0);
  background: var(--good);
}

.cst-16__wrap {
  border-radius: 18px;
  border: 1.5px dashed;
  padding: 14px;
  display: grid;
  gap: 12px;
}

.cst-16__wrap--hidden {
  overflow: hidden;
  border-color: oklch(0.56 0.19 25/.5);
  background: oklch(0.97 0.01 25/.4);
}

.cst-16__wrap--clip {
  overflow: clip;
  border-color: oklch(0.55 0.15 150/.5);
  background: oklch(0.97 0.01 150/.4);
}

.cst-16__pill {
  position: sticky;
  top: 64px;
  z-index: 2;
  padding: 12px 16px;
  border-radius: 12px;
  font-size: 12.5px;
  font-weight: 700;
  line-height: 1.45;
  color: oklch(0.99 0 0);
  box-shadow: 0 8px 22px oklch(0.3 0.05 280/.18);
}

.cst-16__pill--bad {
  background: linear-gradient(120deg,oklch(0.52 0.17 25),oklch(0.42 0.15 15));
}

.cst-16__pill--good {
  background: linear-gradient(120deg,oklch(0.5 0.13 155),oklch(0.42 0.12 175));
}

.cst-16__wrap article {
  padding: 16px;
  border-radius: 13px;
  background: oklch(1 0 0);
  border: 1px solid var(--line);
}

.cst-16__wrap h3 {
  font-size: 13.5px;
  letter-spacing: -.005em;
  margin-bottom: 7px;
}

.cst-16__wrap article p {
  font-size: 12.5px;
  line-height: 1.65;
  color: var(--mut);
}

.cst-16__drill {
  margin: clamp(26px,4cqi,44px) clamp(18px,4cqi,44px);
  padding: clamp(20px,3.5cqi,34px);
  border-radius: 20px;
  background: oklch(0.22 0.015 280);
  color: oklch(0.93 0.005 280);
}

.cst-16__drill h2 {
  font-size: clamp(20px,3.2cqi,28px);
  letter-spacing: -.02em;
  font-weight: 800;
  margin-bottom: 10px;
}

.cst-16__drill>p {
  font-size: 13.5px;
  color: oklch(0.72 0.01 280);
  margin-bottom: 14px;
}

.cst-16__drill>p code {
  background: oklch(0.32 0.02 280);
  color: oklch(0.93 0.005 280);
}

.cst-16__drill pre {
  overflow-x: auto;
  padding: 16px 18px;
  border-radius: 13px;
  background: oklch(0.17 0.012 280);
  border: 1px solid oklch(0.34 0.02 280);
  margin-bottom: 18px;
}

.cst-16__drill pre code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12.5px;
  line-height: 1.65;
  color: oklch(0.85 0.05 150);
  background: none;
  padding: 0;
}

.cst-16__list {
  list-style: none;
  display: grid;
  gap: 10px;
  counter-reset: drill;
}

.cst-16__list li {
  counter-increment: drill;
  position: relative;
  padding: 12px 14px 12px 46px;
  border-radius: 12px;
  background: oklch(0.26 0.015 280);
  font-size: 13px;
  line-height: 1.6;
  color: oklch(0.8 0.008 280);
}

.cst-16__list li::before {
  content: counter(drill);
  position: absolute;
  left: 14px;
  top: 12px;
  display: grid;
  place-items: center;
  width: 22px;
  height: 22px;
  border-radius: 7px;
  font-size: 11.5px;
  font-weight: 800;
  color: oklch(0.2 0.01 280);
  background: oklch(0.8 0.1 150);
}

.cst-16__list strong {
  color: oklch(0.95 0.005 280);
}

.cst-16__list code {
  background: oklch(0.34 0.02 280);
  color: oklch(0.93 0.005 280);
}

.cst-16__footer {
  display: flex;
  flex-wrap: wrap;
  gap: 14px 26px;
  align-items: center;
  justify-content: space-between;
  padding: 0 clamp(18px,4cqi,44px) 38px;
}

.cst-16__footer p {
  font-size: 12.5px;
  color: var(--mut);
}

.cst-16__footer a {
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

.cst-16__footer a:hover,
.cst-16__footer a:focus-visible {
  border-color: var(--good);
}

.cst-16__footer a:focus-visible {
  outline: 2px solid var(--good);
  outline-offset: 3px;
}

@container cst16 (width < 620px) {
  .cst-16__lab {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cst-16 * {
    transition-duration: .01ms !important;
  }
}
```
