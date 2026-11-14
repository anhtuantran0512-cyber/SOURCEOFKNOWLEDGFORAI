---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/sticky-top-announcement-banner-css/"
title: "Sticky Top Announcement Bar"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "A sticky bar that condenses as you scroll with zero JavaScript."
has_js: "false"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Top Announcement Bar
Source: https://codefronts.com/snippets/css-banners-alerts/sticky-top-announcement-banner-css/

A sticky bar that condenses as you scroll with zero JavaScript. animation-timeline: scroll() drives the height, padding and type scale from scroll position, a second timeline paints the reading-progress line, and a hidden checkbox plus :has() gives it a real close button. Scroll the demo to watch the bar compress and the progress line fill.
## HTML
```html
<div class="ba-12">
  <input class="ba-12__vh" type="checkbox" id="ba-12-x">

  <div class="ba-12__bar" role="region" aria-labelledby="ba-12-h">
    <p class="ba-12__msg" id="ba-12-h">
      <span class="ba-12__tag">New</span>
      <span class="ba-12__main">Container queries are now in every browser we support</span>
      <span class="ba-12__aux">— the layout rewrite guide is 12 minutes and saves a fortnight</span>
    </p>
    <span class="ba-12__actions">
      <a class="ba-12__cta" href="#ba-12-read">
        Read the guide
        <svg viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="M4 10h11m-4.4-4.4L15 10l-4.4 4.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <label class="ba-12__x" for="ba-12-x" tabindex="0" role="button" aria-label="Dismiss announcement">
        <svg viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="m6 6 8 8m0-8-8 8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      </label>
    </span>
    <span class="ba-12__progress" aria-hidden="true"></span>
  </div>

  <article class="ba-12__page" id="ba-12-read">
    <header>
      <p class="ba-12__kicker">Layout · 12 min read</p>
      <h1>Stop writing media queries for components</h1>
      <p class="ba-12__standfirst">A media query asks about the window. A component almost never cares about the window — it cares about the space it was given.</p>
    </header>
    <p>The rewrite is smaller than it sounds. Most component-level breakpoints in a mature codebase exist to compensate for the fact that the component could not ask its own question. Give it the ability to ask, and roughly two thirds of them disappear.</p>
    <p>Start with the card that appears in the widest variety of slots. Wrap it in a container, declare <code>container-type: inline-size</code>, and convert only the breakpoints that were about the card's own width.</p>
    <p>Leave the page-level breakpoints alone. Grid template changes, sidebar collapses and typographic scale still belong to the viewport, and pretending otherwise produces a codebase where nobody can find where a decision was made.</p>
    <h2>What to do about the type scale</h2>
    <p>Container query units are the quiet upgrade. <code>cqi</code> resolves against the container's inline size, so a headline can scale with its column rather than with the browser window — the effect designers have wanted since the first fluid type article in 2016.</p>
    <p>Keep a floor and a ceiling. Unbounded fluid type is how you end up with 9px captions on a phone and 140px headlines on a television.</p>
    <p>Audit in the browser, not the codebase. Drag a component boundary and watch which numbers matter; the ones that never earn their keep can go.</p>
    <h2>Migration order that actually works</h2>
    <p>Cards, then media objects, then navigation, then page shells. Navigation is deceptively hard because it usually carries state, and page shells rarely benefit at all.</p>
    <p>Expect the diff to be mostly deletions. That is the point.</p>
    <p>Scroll back up: the bar has compressed, and the hairline under it tracks how far through this page you are — both from two CSS rules, no listeners, no layout thrash.</p>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700&family=Newsreader:opsz,[email protected],400;6..72,500&display=swap');

.ba-12 {
  --bar-z: 20;
  --pad: 1rem;
  --scale: 1;
  --dim: 1;
  --paper: #fbfaf8;
  --ink: #14130f;
  --bar: #14130f;
  --bar-ink: #fbfaf8;
  --muted: #6f6a60;
  --line: #e6e2d9;
  --acc: #1c62ff;
  --sans: "Schibsted Grotesk",ui-sans-serif,system-ui,-apple-system,sans-serif;
  --serif: "Newsreader",ui-serif,Georgia,"Times New Roman",serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--sans);
  scroll-padding-block-start: 5rem;
}

.ba-12 *,
.ba-12 *::before,
.ba-12 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-12 {
    --paper: oklch(98% .006 85);
    --ink: oklch(16% .012 70);
    --bar: oklch(16% .012 70);
    --muted: oklch(56% .014 72);
    --line: oklch(91% .01 82);
    --acc: oklch(55% .22 262);
  }
}

@media (prefers-color-scheme: dark) {
  .ba-12:not([data-theme="light"]) {
    --paper: #0d0c0a;
    --ink: #f6f4ef;
    --bar: #1a1815;
    --bar-ink: #f6f4ef;
    --muted: #9a938a;
    --line: #282420;
  }
}

.ba-12[data-theme="dark"] {
  --paper: #0d0c0a;
  --ink: #f6f4ef;
  --bar: #1a1815;
  --bar-ink: #f6f4ef;
  --muted: #9a938a;
  --line: #282420;
}

.ba-12__bar {
  position: sticky;
  z-index: var(--bar-z);
  top: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: clamp(.75rem,3vw,2rem);
  padding: var(--pad) clamp(1rem,4vw,2rem);
  background: var(--bar);
  color: var(--bar-ink);
  transition: opacity .3s ease, translate .35s cubic-bezier(.16,1,.3,1), display .35s allow-discrete;
}

.ba-12:has(#ba-12-x:checked) .ba-12__bar {
  display: none;
  opacity: 0;
  translate: 0 -100%;
}

.ba-12__msg {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .55rem;
  flex-wrap: wrap;
  min-width: 0;
  max-width: 78ch;
  font-size: calc(.9375rem * var(--scale));
  line-height: 1.35;
  letter-spacing: -.015em;
  text-wrap: balance;
}

.ba-12__tag {
  flex: none;
  font-size: calc(.625rem * var(--scale));
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  padding: .25rem .45rem;
  border-radius: .35rem;
  background: var(--acc);
  color: #fff;
}

.ba-12__main {
  font-weight: 600;
}

.ba-12__aux {
  color: color-mix(in oklab,var(--bar-ink) 60%,transparent);
  opacity: var(--dim);
}

.ba-12__actions {
  display: flex;
  align-items: center;
  gap: .4rem;
  flex: none;
}

.ba-12__cta {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  min-height: 2.25rem;
  padding: .45rem .85rem;
  border-radius: .6rem;
  text-decoration: none;
  font-size: calc(.8125rem * var(--scale));
  font-weight: 600;
  color: var(--bar-ink);
  border: 1px solid color-mix(in oklab,var(--bar-ink) 30%,transparent);
  transition: background .2s ease, border-color .2s ease;
}

.ba-12__cta svg {
  width: 1rem;
  height: 1rem;
  transition: translate .25s cubic-bezier(.16,1,.3,1);
}

.ba-12__cta:hover {
  background: color-mix(in oklab,var(--bar-ink) 12%,transparent);
  border-color: var(--bar-ink);
}

.ba-12__cta:hover svg {
  translate: .2rem 0;
}

.ba-12__x {
  display: grid;
  place-items: center;
  width: 2.25rem;
  height: 2.25rem;
  border-radius: .6rem;
  cursor: pointer;
  color: color-mix(in oklab,var(--bar-ink) 60%,transparent);
}

.ba-12__x:hover {
  color: var(--bar-ink);
  background: color-mix(in oklab,var(--bar-ink) 12%,transparent);
}

.ba-12__x svg {
  width: 1.05rem;
  height: 1.05rem;
}

.ba-12__x:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ba-12__progress {
  position: absolute;
  inset: auto 0 0 0;
  height: 2px;
  background: var(--acc);
  transform-origin: left;
  scale: 1 1;
}

.ba-12__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@supports (animation-timeline: scroll()) {
  .ba-12__bar {
    animation: ba-12-condense linear both;
    animation-timeline: scroll(nearest block);
    animation-range: 0 240px;
  }

  @keyframes ba-12-condense {
    to {
      --pad: .45rem;
      --scale: .86;
      --dim: 0;
    }
  }

  .ba-12__progress {
    scale: 0 1;
    animation: ba-12-fill linear both;
    animation-timeline: scroll(nearest block);
  }

  @keyframes ba-12-fill {
    from {
      scale: 0 1;
    }

    to {
      scale: 1 1;
    }
  }

  .ba-12__aux {
    transition: opacity .2s linear;
  }
}

.ba-12__page {
  max-width: 44rem;
  margin-inline: auto;
  padding: clamp(2rem,7vh,4rem) clamp(1.25rem,5vw,2rem) clamp(4rem,14vh,8rem);
  display: grid;
  gap: 1.15rem;
}

.ba-12__page header {
  display: grid;
  gap: .75rem;
  margin-block-end: .5rem;
}

.ba-12__kicker {
  margin: 0;
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--acc);
}

.ba-12__page h1 {
  margin: 0;
  font-size: clamp(2rem,6vw,3.25rem);
  font-weight: 600;
  line-height: 1.03;
  letter-spacing: -.045em;
  text-wrap: balance;
}

.ba-12__standfirst {
  margin: 0;
  font-family: var(--serif);
  font-size: clamp(1.0625rem,2.4vw,1.375rem);
  line-height: 1.55;
  color: var(--muted);
  max-width: 60ch;
  text-wrap: pretty;
}

.ba-12__page h2 {
  margin: 1.25rem 0 0;
  font-size: clamp(1.25rem,3vw,1.625rem);
  font-weight: 600;
  letter-spacing: -.03em;
}

.ba-12__page p {
  margin: 0;
  font-family: var(--serif);
  font-size: 1.0625rem;
  line-height: 1.72;
  max-width: 68ch;
  text-wrap: pretty;
}

.ba-12__page code {
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: .9em;
  padding: .1em .35em;
  border-radius: .3rem;
  background: color-mix(in oklab,var(--ink) 8%,transparent);
}

.ba-12__page figcaption {
  font-size: .8125rem;
  color: var(--muted);
}

.ba-12 a {
  color: var(--acc);
}

.ba-12 a:hover {
  color: color-mix(in oklab,var(--acc) 75%,var(--ink));
}

.ba-12 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

@media (max-width: 40rem) {
  .ba-12__aux {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ba-12__bar {
    animation: none !important;
    --pad: 1rem;
    --scale: 1;
    --dim: 1;
  }

  .ba-12__progress {
    animation: none !important;
    scale: 1 1;
  }

  .ba-12 * {
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .ba-12__bar {
    border-block-end: 1px solid CanvasText;
  }

  .ba-12__tag,
    .ba-12__progress {
    background: Highlight;
  }
}
```
