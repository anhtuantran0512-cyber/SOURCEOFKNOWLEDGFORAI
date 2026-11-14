---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/tooltip-text-reveal/"
title: "Tooltip Text Reveal"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "Definition tooltips on the jargon in a SaaS feature list — pure CSS, but built like product UI, not a CodePen: the bubble is ::after reading attr(data-tip)…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tooltip Text Reveal
Source: https://codefronts.com/motion/css-text-hover-effects/tooltip-text-reveal/

Definition tooltips on the jargon in a SaaS feature list — pure CSS, but built like product UI, not a CodePen: the bubble is ::after reading attr(data-tip) with an ::before arrow; it fades/lifts in on a 350ms INTENT delay (so drive-by cursors never trigger a flicker storm) yet hides instantly on exit and shows instantly on keyboard focus — three different timings, all from transition-delay placement. Terms are real <button>s with aria-describedby pointing at screen-reader text, because a tooltip a screen reader can't hear is a decoration, not a tooltip.
## HTML
```html
<section class="cth-28" aria-label="CSS tooltip text reveal demo">
  <div class="cth-28__stage">
    <div class="cth-28__card">
      <p class="cth-28__eyebrow">Ledgerline &mdash; what's in the Pro tier</p>
      <h2 class="cth-28__title">Every export, explained on hover</h2>
      <ul class="cth-28__list">
        <li>Nightly
          <button class="cth-28__term" type="button" data-tip="Data copied straight from disk to network — no serialization step, no CPU spike at 2am." aria-describedby="cth28-d1">zero-copy exports<i class="cth-28__sr" id="cth28-d1">Data copied straight from disk to network — no serialization step, no CPU spike at 2am.</i></button>
          to your warehouse.</li>
        <li>Ledgers stay consistent under
          <button class="cth-28__term" type="button" data-tip="Multiple writers land in one agreed order — nobody's Tuesday overwrites somebody's Monday." aria-describedby="cth28-d2">multi-writer ordering<i class="cth-28__sr" id="cth28-d2">Multiple writers land in one agreed order — nobody's Tuesday overwrites somebody's Monday.</i></button>
          at any scale.</li>
        <li>Vaults are
          <button class="cth-28__term" type="button" data-tip="Your data never leaves the region you pinned it to. Auditors love this one weird trick." aria-describedby="cth28-d3">region-pinned<i class="cth-28__sr" id="cth28-d3">Your data never leaves the region you pinned it to. Auditors love this one weird trick.</i></button>
          by default.</li>
      </ul>
      <p class="cth-28__hint">Hover a dotted term (350ms intent delay) or <kbd>Tab</kbd> to it (instant). Bubble = <code>::after</code> + <code>attr(data-tip)</code>; screen readers get <code>aria-describedby</code>.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-28,
.cth-28 *,
.cth-28 *::before,
.cth-28 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-28 {
  --bg: oklch(0.97 0.005 230);
  --card: oklch(1 0 0);
  --ink: oklch(0.25 0.02 250);
  --mut: oklch(0.52 0.02 250);
  --acc: oklch(0.55 0.15 240);
  --line: oklch(0.9 0.008 240);
  --tip-bg: oklch(0.24 0.02 255);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-28__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: var(--bg);
  padding: clamp(20px,4vw,56px);
  container: cth28/inline-size;
}

.cth-28__card {
  width: min(100%,620px);
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: clamp(24px,4.6cqi,40px);
  box-shadow: 0 20px 60px oklch(0.4 0.05 245/.1);
}

.cth-28__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--acc);
}

.cth-28__title {
  font-size: clamp(22px,3.8cqi,30px);
  font-weight: 850;
  letter-spacing: -.02em;
  margin-top: 8px;
}

.cth-28__list {
  list-style: none;
  margin-top: 18px;
  display: flex;
  flex-direction: column;
}

.cth-28__list li {
  font-size: 16.5px;
  line-height: 1.75;
  color: var(--mut);
  padding: 14px 2px;
  border-bottom: 1px solid var(--line);
}

.cth-28__term {
  position: relative;
  display: inline;
  border: 0;
  background: none;
  cursor: help;
  font: inherit;
  font-weight: 700;
  color: var(--ink);
  border-bottom: 2px dotted var(--acc);
  padding-bottom: 1px;
  transition: color .2s,border-color .2s;
}

.cth-28__term:hover,
.cth-28__term:focus-visible {
  color: var(--acc);
}

.cth-28__term:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 2px;
}

.cth-28__term::after {
  content: attr(data-tip);
  position: absolute;
  bottom: calc(100% + 11px);
  left: 50%;
  z-index: 5;
  width: max-content;
  max-width: 26ch;
  padding: 10px 13px;
  border-radius: 10px;
  background: var(--tip-bg);
  color: oklch(0.96 0.005 240);
  font-size: 12.5px;
  font-weight: 550;
  line-height: 1.55;
  text-align: left;
  box-shadow: 0 12px 30px oklch(0.2 0.03 255/.35);
  translate: -50% 6px;
  opacity: 0;
  scale: .94;
  pointer-events: none;
  transition: opacity .22s ease,translate .22s ease,scale .22s ease;
  transition-delay: 0s;
}

.cth-28__term::before {
  content: '';
  position: absolute;
  bottom: calc(100% + 5px);
  left: 50%;
  z-index: 5;
  border: 6px solid transparent;
  border-top-color: var(--tip-bg);
  translate: -50% 6px;
  opacity: 0;
  pointer-events: none;
  transition: opacity .22s ease,translate .22s ease;
  transition-delay: 0s;
}

.cth-28__term:hover::after,
.cth-28__term:hover::before {
  opacity: 1;
  translate: -50% 0;
  scale: 1;
  pointer-events: auto;
  transition-delay: .35s;
}

.cth-28__term:focus-visible::after,
.cth-28__term:focus-visible::before {
  opacity: 1;
  translate: -50% 0;
  scale: 1;
  transition-delay: 0s;
}

.cth-28__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cth-28__hint {
  margin-top: 16px;
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
}

.cth-28__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.94 0.006 240);
  padding: 1px 6px;
  border-radius: 4px;
}

.cth-28__hint kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  border: 1px solid var(--line);
  border-bottom-width: 2px;
  border-radius: 5px;
  padding: 2px 6px;
  background: oklch(0.98 0.003 240);
}

@media (prefers-reduced-motion: reduce) {
  .cth-28 *,
    .cth-28 *::before,
    .cth-28 *::after {
    transition-duration: .01ms !important;
  }
}
```
