---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/marker-underline/"
title: "Marker Highlight Underline CSS Blockquote"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "Three grades of hand-feel underline under one quote's key phrases, from cheapest to richest: (1) the modern text-decoration stack — thickness, offset, color…"
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Marker Highlight Underline CSS Blockquote
Source: https://codefronts.com/snippets/css-blockquotes/marker-underline/

Three grades of hand-feel underline under one quote's key phrases, from cheapest to richest: (1) the modern text-decoration stack — thickness, offset, color and skip-ink tuned into a confident marker stripe; (2) the gradient underline — a bottom-anchored background that sits BEHIND descenders like real marker ink, animatable via background-size; (3) the SVG stroke — an inline hand-drawn path with vector-effect and stroke-dash draw-in animation for true crayon energy. Same sentence, three budgets — pick per project.
## HTML
```html
<section class="bq-16" aria-label="Marker highlight underline blockquote demo">
  <div class="bq-16__stage">
    <figure class="bq-16__quote">
      <blockquote>
        <p>Write the docs <span class="bq-16__u1">as if the reader is tired</span>, ship the API <span class="bq-16__u2">as if the caller is distracted</span>, and design the defaults <span class="bq-16__u3">as if nobody reads either<svg viewBox="0 0 200 14" preserveAspectRatio="none" aria-hidden="true"><path d="M4 9c28-5 55 3 82-2s58-3 78 1c12 2 24 1 32-2" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round"/></svg></span>.</p>
      </blockquote>
      <figcaption class="bq-16__by">— <strong>Engineering onboarding wall</strong>, week one</figcaption>
      <ul class="bq-16__legend" aria-label="Techniques used, in order">
        <li><i class="bq-16__sw bq-16__sw--1" aria-hidden="true"></i>text-decoration stack</li>
        <li><i class="bq-16__sw bq-16__sw--2" aria-hidden="true"></i>gradient behind descenders</li>
        <li><i class="bq-16__sw bq-16__sw--3" aria-hidden="true"></i>SVG hand-drawn stroke</li>
      </ul>
    </figure>
    <p class="bq-16__chip" aria-hidden="true">3 underline grades · skip-ink:none · stroke-dash draw-in</p>
  </div>
</section>
```
## CSS
```css
.bq-16,
.bq-16 *,
.bq-16 *::before,
.bq-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.98 0.006 60);
  --ink: oklch(0.24 0.015 50);
  --mut: oklch(0.54 0.02 50);
  --marker: oklch(0.75 0.16 55);
  --m2: oklch(0.78 0.14 145);
  --m3: oklch(0.72 0.15 330);
  font-family: Georgia,'Times New Roman',serif;
  color: var(--ink);
}

.bq-16__stage {
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

.bq-16__quote {
  max-width: 56ch;
}

.bq-16__quote blockquote p {
  font-size: clamp(21px,2.8vw,28px);
  line-height: 1.72;
  text-wrap: pretty;
}

.bq-16__u1 {
  text-decoration-line: underline;
  text-decoration-color: color-mix(in oklch,var(--marker) 75%,transparent);
  text-decoration-thickness: .22em;
  text-underline-offset: .16em;
  text-decoration-skip-ink: none;
}

.bq-16__u2 {
  background: linear-gradient(color-mix(in oklch,var(--m2) 55%,transparent) 0 0) no-repeat 0 88%/100% .42em;
  -webkit-box-decoration-break: clone;
  box-decoration-break: clone;
  animation: bq16-draw 1.2s cubic-bezier(.6,0,.3,1) both;
  animation-delay: .3s;
}

@keyframes bq16-draw {
  from {
    background-size: 0% .42em;
  }

  to {
    background-size: 100% .42em;
  }
}

.bq-16__u3 {
  position: relative;
  white-space: nowrap;
}

.bq-16__u3 svg {
  position: absolute;
  left: -.1em;
  right: -.1em;
  bottom: -.28em;
  width: calc(100% + .2em);
  height: .4em;
  color: var(--m3);
  stroke-dasharray: 210;
  stroke-dashoffset: 210;
  animation: bq16-stroke 1s ease-out forwards;
  animation-delay: 1.1s;
}

@keyframes bq16-stroke {
  to {
    stroke-dashoffset: 0;
  }
}

.bq-16__by {
  margin-top: 18px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 13.5px;
  color: var(--mut);
}

.bq-16__by strong {
  color: var(--ink);
  font-weight: 650;
}

.bq-16__legend {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  margin-top: 16px;
  list-style: none;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--mut);
}

.bq-16__legend li {
  display: flex;
  align-items: center;
  gap: 6px;
}

.bq-16__sw {
  width: 16px;
  height: 5px;
  border-radius: 3px;
}

.bq-16__sw--1 {
  background: var(--marker);
}

.bq-16__sw--2 {
  background: var(--m2);
}

.bq-16__sw--3 {
  background: var(--m3);
}

.bq-16__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid oklch(0 0 0/.1);
  border-radius: 99px;
  background: oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .bq-16 * {
    transition-duration: .01ms !important;
    animation-duration: .01ms !important;
    animation-delay: 0s !important;
  }
}
```
