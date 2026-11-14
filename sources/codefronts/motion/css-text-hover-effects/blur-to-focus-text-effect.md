---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/blur-to-focus-text-effect/"
title: "Blur to Focus Text Effect"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "A photographer's index that behaves like a lens: at rest every essay title is crisp; the moment the list is hovered, everything EXCEPT the current line falls…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Blur to Focus Text Effect
Source: https://codefronts.com/motion/css-text-hover-effects/blur-to-focus-text-effect/

A photographer's index that behaves like a lens: at rest every essay title is crisp; the moment the list is hovered, everything EXCEPT the current line falls out of focus — blur(4px), dimmed, slightly smaller — and your line stays tack sharp. It's the depth-of-field metaphor applied to a menu, done with one selector pair (.list:hover .item:not(:hover)) and mirrored for keyboards with :has(:focus-visible). Underneath, the inverse classic: a single redacted-feeling line that starts blurred and resolves on approach.
## HTML
```html
<section class="cth-13" aria-label="Blur to focus list demo">
  <div class="cth-13__stage">
    <div class="cth-13__scene">
      <header class="cth-13__head">
        <p class="cth-13__eyebrow">Field Notes &mdash; six essays on light</p>
        <span class="cth-13__chip">.list:hover .row:not(:hover)</span>
      </header>
      <ol class="cth-13__list">
        <li class="cth-13__row"><a href="#cth13-top" id="cth13-top"><span class="cth-13__title">Fog line at Bodega Bay</span><span class="cth-13__meta">35mm &middot; 06:12</span></a></li>
        <li class="cth-13__row"><a href="#cth13-top"><span class="cth-13__title">Sodium lamps, last winter</span><span class="cth-13__meta">digital &middot; 23:40</span></a></li>
        <li class="cth-13__row"><a href="#cth13-top"><span class="cth-13__title">The greenhouse negatives</span><span class="cth-13__meta">120 film &middot; noon</span></a></li>
        <li class="cth-13__row"><a href="#cth13-top"><span class="cth-13__title">Harbour glass, overexposed</span><span class="cth-13__meta">35mm &middot; 15:55</span></a></li>
        <li class="cth-13__row"><a href="#cth13-top"><span class="cth-13__title">Aurora over the car park</span><span class="cth-13__meta">digital &middot; 01:03</span></a></li>
      </ol>
      <p class="cth-13__secret"><a href="#cth13-top">P.S. &mdash; the seventh essay was never published. Hover to read why.</a></p>
      <p class="cth-13__hint">Hover the index: everything but your line drops out of focus. <kbd>Tab</kbd> does the same via <code>:has(:focus-visible)</code>.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-13,
.cth-13 *,
.cth-13 *::before,
.cth-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-13 {
  --bg: oklch(0.975 0.004 90);
  --ink: oklch(0.24 0.01 80);
  --mut: oklch(0.55 0.015 80);
  --acc: oklch(0.58 0.14 60);
  --line: oklch(0.9 0.008 85);
  font-family: Georgia,'Times New Roman',serif;
  color: var(--ink);
}

.cth-13__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: var(--bg);
  padding: clamp(20px,4vw,56px);
  container: cth13/inline-size;
}

.cth-13__scene {
  width: min(100%,700px);
  display: flex;
  flex-direction: column;
  gap: clamp(16px,3cqi,24px);
}

.cth-13__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  flex-wrap: wrap;
  padding-bottom: 14px;
  border-bottom: 1.5px solid var(--ink);
}

.cth-13__eyebrow {
  font-size: 13px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--mut);
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-weight: 700;
}

.cth-13__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--acc);
  border: 1px solid color-mix(in oklch,var(--acc) 40%,transparent);
  border-radius: 99px;
  padding: 5px 11px;
}

.cth-13__list {
  list-style: none;
  counter-reset: cth13;
}

.cth-13__row {
  counter-increment: cth13;
  border-bottom: 1px solid var(--line);
}

.cth-13__row a {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 18px;
  padding: clamp(13px,2.4cqi,19px) 4px;
  text-decoration: none;
  color: inherit;
}

.cth-13__row a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 4px;
}

.cth-13__title {
  font-size: clamp(21px,3.8cqi,32px);
  font-weight: 600;
  letter-spacing: -.01em;
  line-height: 1.25;
  filter: blur(0) saturate(1);
  opacity: 1;
  scale: 1;
  transition: filter .25s ease,opacity .25s ease,scale .25s ease;
}

.cth-13__title::before {
  content: '0' counter(cth13) '  ';
  font-size: 12px;
  color: var(--acc);
  font-family: ui-monospace,Menlo,monospace;
  letter-spacing: .05em;
}

.cth-13__meta {
  font-size: 12px;
  color: var(--mut);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  white-space: nowrap;
  transition: opacity .25s ease;
}

.cth-13__list:hover .cth-13__row:not(:hover) .cth-13__title,
.cth-13__list:has(:focus-visible) .cth-13__row:not(:has(:focus-visible)) .cth-13__title {
  filter: blur(4px) saturate(.6);
  opacity: .4;
  scale: .985;
  transition-duration: .5s;
}

.cth-13__list:hover .cth-13__row:not(:hover) .cth-13__meta,
.cth-13__list:has(:focus-visible) .cth-13__row:not(:has(:focus-visible)) .cth-13__meta {
  opacity: .25;
  transition-duration: .5s;
}

.cth-13__secret {
  padding-top: 6px;
}

.cth-13__secret a {
  font-style: italic;
  font-size: 15px;
  color: var(--mut);
  text-decoration: none;
  filter: blur(3.5px);
  transition: filter .45s ease,color .45s ease;
}

.cth-13__secret a:hover,
.cth-13__secret a:focus-visible {
  filter: blur(0);
  color: var(--acc);
}

.cth-13__secret a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cth-13__hint {
  font-size: 12.5px;
  color: var(--mut);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cth-13__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.93 0.008 85);
  padding: 1px 6px;
  border-radius: 4px;
}

.cth-13__hint kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  border: 1px solid var(--line);
  border-bottom-width: 2px;
  border-radius: 5px;
  padding: 2px 6px;
  background: oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cth-13 * {
    transition-duration: .01ms !important;
  }
}
```
