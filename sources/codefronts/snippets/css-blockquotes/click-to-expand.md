---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/click-to-expand/"
title: "Expandable Read More CSS Blockquote"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "Read-more without JavaScript, built on the disclosure element the platform already ships: <details>/<summary> gives you the toggle, keyboard support and…"
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Expandable Read More CSS Blockquote
Source: https://codefronts.com/snippets/css-blockquotes/click-to-expand/

Read-more without JavaScript, built on the disclosure element the platform already ships: <details>/<summary> gives you the toggle, keyboard support and screen-reader semantics for free. The 2026 upgrades make it feel engineered: the collapsed preview is a -webkit-line-clamp truncation with a fade-out gradient sitting under the summary, the label swaps between 'Read the full quote' and 'Show less' via details[open] selectors, the chevron rotates, and — in engines that support interpolate-size: allow-keywords — the open/close actually animates height, the thing everyone thinks requires JS.
## HTML
```html
<section class="bq-24" aria-label="Expandable read more blockquote demo">
  <div class="bq-24__stage">
    <figure class="bq-24__card">
      <p class="bq-24__kicker">From “The Craftsman” · Richard Sennett</p>
      <details class="bq-24__details">
        <summary class="bq-24__summary">
          <span class="bq-24__more">Read the full quote</span>
          <span class="bq-24__less">Show less</span>
          <svg class="bq-24__chev" viewBox="0 0 16 16" width="15" height="15" aria-hidden="true"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </summary>
        <blockquote class="bq-24__rest">
          <p>It is the ability to focus on the work rather than ourselves that makes craft possible at all — and every workshop, digital or wooden, is finally an argument for patience over speed.</p>
        </blockquote>
      </details>
      <blockquote class="bq-24__preview">
        <p>Craftsmanship names an enduring, basic human impulse: the desire to do a job well for its own sake. It cuts a far wider swath than skilled manual labor; it serves the programmer, the doctor, the artist, and the parent alike — anyone whose practice improves through the discipline of critique.</p>
      </blockquote>
    </figure>
    <p class="bq-24__chip" aria-hidden="true">&lt;details&gt; disclosure · line-clamp teaser · interpolate-size height animation</p>
  </div>
</section>
```
## CSS
```css
.bq-24,
.bq-24 *,
.bq-24 *::before,
.bq-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@supports (interpolate-size: allow-keywords) {
  .bq-24 {
    width: 100%;
    min-height: 100vh;
    min-height: 100svh;
    display: block;
    interpolate-size: allow-keywords;
  }
}

.bq-24 {
  --bg: oklch(0.965 0.007 40);
  --card: oklch(1 0 0);
  --ink: oklch(0.26 0.015 45);
  --quiet: oklch(0.42 0.015 45);
  --mut: oklch(0.55 0.015 45);
  --acc: oklch(0.58 0.14 40);
  font-family: Georgia,'Times New Roman',serif;
  color: var(--ink);
}

.bq-24__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(20px,5vw,56px);
  background: var(--bg);
  overflow-y: auto;
}

.bq-24__card {
  width: min(100%,540px);
  background: var(--card);
  border: 1px solid oklch(0 0 0/.08);
  border-radius: 18px;
  padding: clamp(24px,4vw,34px);
  box-shadow: 0 2px 6px oklch(0.35 0.03 45/.06),0 16px 40px oklch(0.35 0.03 45/.09);
  display: flex;
  flex-direction: column;
}

.bq-24__kicker {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
  margin-bottom: 14px;
}

.bq-24__preview {
  position: relative;
  order: -1;
  margin-bottom: 2px;
}

.bq-24__preview p {
  font-size: 17.5px;
  line-height: 1.68;
  color: var(--quiet);
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  overflow: hidden;
  text-wrap: pretty;
}

.bq-24__preview::after {
  content: '';
  position: absolute;
  inset: auto 0 0;
  height: 1.7em;
  background: linear-gradient(transparent,var(--card));
  pointer-events: none;
  transition: opacity .3s;
}

.bq-24__details {
  display: contents;
}

.bq-24__card:has(.bq-24__details[open]) .bq-24__preview p {
  -webkit-line-clamp: none;
}

.bq-24__card:has(.bq-24__details[open]) .bq-24__preview::after {
  opacity: 0;
}

.bq-24__rest p {
  font-size: 17.5px;
  line-height: 1.68;
  color: var(--quiet);
  padding-top: .6em;
  text-wrap: pretty;
}

.bq-24__details::details-content {
  block-size: 0;
  overflow: hidden;
  transition: block-size .45s cubic-bezier(.2,.7,.2,1),content-visibility .45s allow-discrete;
}

.bq-24__details[open]::details-content {
  block-size: auto;
}

.bq-24__summary {
  order: 1;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  align-self: flex-start;
  margin-top: 14px;
  min-height: 44px;
  padding: 0 4px;
  list-style: none;
  cursor: pointer;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 13.5px;
  font-weight: 650;
  color: var(--acc);
  border-radius: 8px;
}

.bq-24__summary::marker {
  content: '';
}

.bq-24__summary::-webkit-details-marker {
  display: none;
}

.bq-24__summary:hover {
  text-decoration: underline;
  text-underline-offset: 3px;
}

.bq-24__summary:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.bq-24__less {
  display: none;
}

.bq-24__details[open] .bq-24__less {
  display: inline;
}

.bq-24__details[open] .bq-24__more {
  display: none;
}

.bq-24__chev {
  transition: rotate .3s;
}

.bq-24__details[open] .bq-24__chev {
  rotate: 180deg;
}

.bq-24__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid oklch(0 0 0/.1);
  border-radius: 99px;
  background: var(--card);
}

@media (prefers-reduced-motion: reduce) {
  .bq-24 * {
    transition-duration: .01ms !important;
  }
}
```
