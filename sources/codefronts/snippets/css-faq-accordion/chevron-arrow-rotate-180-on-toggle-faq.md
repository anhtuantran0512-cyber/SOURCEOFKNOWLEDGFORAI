---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/chevron-arrow-rotate-180-on-toggle-faq/"
title: "Chevron/Arrow Rotate 180° on Toggle FAQ"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "The definitive treatment of the web's most-copied micro-interaction."
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Chevron/Arrow Rotate 180° on Toggle FAQ
Source: https://codefronts.com/snippets/css-faq-accordion/chevron-arrow-rotate-180-on-toggle-faq/

The definitive treatment of the web's most-copied micro-interaction. Three chevron builds side by side in one FAQ — inline SVG (crisp at any size), a two-border CSS chevron (zero assets), and a Unicode arrow (one character) — each rotating 180° on toggle with the same shared timing, plus the UX rules for which direction a closed chevron should point and why the rotation must match the panel's duration.
## HTML
```html
<section class="cfa-11" aria-label="Chevron rotate on toggle FAQ">
  <div class="cfa-11__wrap">
    <header class="cfa-11__head">
      <h1>The 180° chevron, three ways</h1>
      <p>Same rotation, three icon builds — SVG, pure CSS borders, Unicode. One <code>--speed</code> token keeps icon and panel in sync.</p>
    </header>
    <div class="cfa-11__list">
      <details class="cfa-11__item" open>
        <summary class="cfa-11__q"><span class="cfa-11__tagchip">A · inline SVG</span>Which icon build should production use?
          <span class="cfa-11__chev cfa-11__chev--svg" aria-hidden="true"><svg viewBox="0 0 16 16" width="16" height="16"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <div class="cfa-11__a"><p>This one. <code>stroke: currentColor</code> inherits your text color automatically, the rounded caps stay crisp at every DPI, and rotating the whole svg element avoids every alignment quirk the other two builds carry.</p></div>
      </details>
      <details class="cfa-11__item">
        <summary class="cfa-11__q"><span class="cfa-11__tagchip">B · CSS borders</span>How does the zero-asset chevron work?
          <span class="cfa-11__chev cfa-11__chev--css" aria-hidden="true"></span>
        </summary>
        <div class="cfa-11__a"><p>A 9px square with only its right and bottom borders, pre-rotated 45° — so “rotate 180°” actually means <code>rotate: 225deg</code>, and a 2px <code>translate</code> nudge re-centers its optical middle. Zero assets, two gotchas.</p></div>
      </details>
      <details class="cfa-11__item">
        <summary class="cfa-11__q"><span class="cfa-11__tagchip">C · Unicode</span>When is a text arrow good enough?
          <span class="cfa-11__chev cfa-11__chev--uni" aria-hidden="true">⌄</span>
        </summary>
        <div class="cfa-11__a"><p>Prototypes and plain-text contexts. It costs one character, but its baseline position depends on the font stack — the <code>line-height: 1</code> and explicit sizing here tame it, mostly. Ship SVG when it matters.</p></div>
      </details>
      <details class="cfa-11__item">
        <summary class="cfa-11__q"><span class="cfa-11__tagchip">UX</span>Which way should a closed chevron point?
          <span class="cfa-11__chev cfa-11__chev--svg" aria-hidden="true"><svg viewBox="0 0 16 16" width="16" height="16"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <div class="cfa-11__a"><p>Down when closed (“content continues below”), up when open. Right-pointing chevrons signal navigation into another screen — using one on an accordion misleads screen-magnifier and low-vision users especially. And match the rotation duration to the panel: mismatched timings read as jank.</p></div>
      </details>
    </div>
    <p class="cfa-11__foot">All three rotate with <code>rotate: 180deg</code> (B: 225deg) over the shared <code>--speed: .4s</code>. CodeFronts collection.</p>
  </div>
</section>
```
## CSS
```css
.cfa-11,
.cfa-11 *,
.cfa-11 *::before,
.cfa-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-11 {
  --bg: oklch(0.97 0.008 250);
  --panel: oklch(1 0 0);
  --ink: oklch(0.23 0.03 255);
  --mut: oklch(0.5 0.02 252);
  --line: oklch(0.89 0.012 250);
  --acc: oklch(0.55 0.18 250);
  --speed: .4s;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: var(--bg);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-11__wrap {
  width: min(100%,660px);
}

.cfa-11__head h1 {
  font-size: clamp(26px,4.5cqi,38px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-11__head p {
  margin-top: 8px;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--mut);
}

.cfa-11__head code,
.cfa-11__a code,
.cfa-11__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .87em;
  background: color-mix(in oklch,var(--acc) 9%,transparent);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

.cfa-11__list {
  margin-top: 26px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  interpolate-size: allow-keywords;
}

.cfa-11__item {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
  box-shadow: 0 2px 8px oklch(0.4 0.05 250/.05);
  transition: border-color .3s;
}

.cfa-11__item[open] {
  border-color: color-mix(in oklch,var(--acc) 35%,var(--line));
}

.cfa-11__q {
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 44px;
  padding: 15px 18px;
  cursor: pointer;
  font-size: 15px;
  font-weight: 650;
  list-style: none;
  transition: color .2s;
}

.cfa-11__q::-webkit-details-marker {
  display: none;
}

.cfa-11__q:hover {
  color: var(--acc);
}

.cfa-11__q:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 14px;
}

.cfa-11__tagchip {
  flex: none;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .05em;
  color: var(--acc);
  padding: 4px 8px;
  background: color-mix(in oklch,var(--acc) 10%,transparent);
  border-radius: 6px;
}

.cfa-11__chev {
  margin-left: auto;
  flex: none;
  display: grid;
  place-items: center;
  color: var(--mut);
  transition: rotate var(--speed) cubic-bezier(.4,0,.2,1),color .25s;
}

.cfa-11__item[open] .cfa-11__chev {
  color: var(--acc);
}

.cfa-11__item[open] .cfa-11__chev--svg {
  rotate: 180deg;
}

.cfa-11__chev--css {
  width: 9px;
  height: 9px;
  border-right: 2px solid currentColor;
  border-bottom: 2px solid currentColor;
  rotate: 45deg;
  translate: 0 -2px;
}

.cfa-11__item[open] .cfa-11__chev--css {
  rotate: 225deg;
  translate: 0 2px;
}

.cfa-11__chev--uni {
  font-size: 18px;
  line-height: 1;
  font-weight: 700;
  translate: 0 -2px;
}

.cfa-11__item[open] .cfa-11__chev--uni {
  rotate: 180deg;
  translate: 0 2px;
}

.cfa-11__a p {
  padding: 0 18px 17px;
  font-size: 14px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 60ch;
}

@supports (interpolate-size: allow-keywords) {
  .cfa-11__item::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height var(--speed) cubic-bezier(.4,0,.2,1),opacity .32s,content-visibility var(--speed) allow-discrete;
  }

  .cfa-11__item[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

.cfa-11__foot {
  margin-top: 22px;
  font-size: 12.5px;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-11 *,
    .cfa-11 .cfa-11__item::details-content {
    transition-duration: .01ms !important;
  }
}
```
