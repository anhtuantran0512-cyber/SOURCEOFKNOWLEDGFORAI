---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/highlighted-run/"
title: "Inline Highlighted Text CSS Blockquote"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "A quote where the key phrases carry a painted highlight — built on the semantic <mark> element with the one property that makes multi-line highlights…"
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inline Highlighted Text CSS Blockquote
Source: https://codefronts.com/snippets/css-blockquotes/highlighted-run/

A quote where the key phrases carry a painted highlight — built on the semantic <mark> element with the one property that makes multi-line highlights survive: box-decoration-break: clone, which re-applies the padding and rounded corners on every wrapped fragment instead of slicing the highlight open at line breaks. Two highlight voices are shown — a solid wash and a skewed 'hand-swiped' variant via a transformed ::before — and the demo explains when <mark> is semantically right versus a styled <em>.
## HTML
```html
<section class="bq-15" aria-label="Inline highlighted text blockquote demo">
  <div class="bq-15__stage">
    <figure class="bq-15__quote">
      <p class="bq-15__kicker">Annotated · from the postmortem</p>
      <blockquote>
        <p>The outage taught us that <mark class="bq-15__hl">alerting is a design problem, not a tooling problem</mark> — we had forty dashboards and zero answers. The fix wasn't another graph; it was deciding, in advance, <mark class="bq-15__hl bq-15__hl--swipe">which three numbers mean the site is healthy</mark> and paging on nothing else.</p>
      </blockquote>
      <figcaption class="bq-15__by">Incident review, <cite>Q3 Reliability Report</cite> — highlights by the SRE lead</figcaption>
    </figure>
    <p class="bq-15__chip" aria-hidden="true">&lt;mark&gt; · box-decoration-break:clone · skewed ::before swipe</p>
  </div>
</section>
```
## CSS
```css
.bq-15,
.bq-15 *,
.bq-15 *::before,
.bq-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.985 0.004 95);
  --ink: oklch(0.25 0.015 80);
  --mut: oklch(0.54 0.015 80);
  --hl: oklch(0.88 0.16 95);
  --hl2: oklch(0.85 0.1 340);
  font-family: Georgia,'Times New Roman',serif;
  color: var(--ink);
}

.bq-15__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(20px,5vw,56px);
  background: var(--bg);
  overflow-y: auto;
}

.bq-15__quote {
  max-width: 58ch;
}

.bq-15__kicker {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 16px;
}

.bq-15__quote blockquote p {
  font-size: clamp(19px,2.5vw,25px);
  line-height: 1.68;
  text-wrap: pretty;
}

.bq-15__hl {
  background: color-mix(in oklch,var(--hl) 55%,transparent);
  padding: .08em .3em;
  border-radius: .3em;
  -webkit-box-decoration-break: clone;
  box-decoration-break: clone;
  color: inherit;
}

.bq-15__hl--swipe {
  position: relative;
  background: none;
  padding: 0;
}

.bq-15__hl--swipe::before {
  content: '';
  position: absolute;
  inset: -.04em -.28em;
  background: color-mix(in oklch,var(--hl2) 62%,transparent);
  border-radius: .4em .2em .45em .25em;
  transform: skewX(-8deg) rotate(-.6deg);
  z-index: -1;
}

.bq-15__by {
  margin-top: 20px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 13px;
  color: var(--mut);
}

.bq-15__by cite {
  font-style: italic;
}

.bq-15__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid oklch(0 0 0/.1);
  border-radius: 99px;
  background: oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .bq-15 * {
    transition-duration: .01ms !important;
  }
}
```
