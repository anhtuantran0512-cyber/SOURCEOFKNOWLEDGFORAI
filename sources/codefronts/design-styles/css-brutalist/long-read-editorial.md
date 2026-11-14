---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/long-read-editorial/"
title: "Brutalist Editorial Long Read"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "An editorial long read with zero decoration: an oversized serif headline, a hard-ruled byline strip, one wide-measure column, pull quotes set off by 6px…"
has_js: "false"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Editorial Long Read
Source: https://codefronts.com/design-styles/css-brutalist/long-read-editorial/

An editorial long read with zero decoration: an oversized serif headline, a hard-ruled byline strip, one wide-measure column, pull quotes set off by 6px rules rather than styling, and a drop cap built with initial-letter. The reading-progress bar at the top is a scroll-driven CSS animation — no scroll listener, no JavaScript at all.
## HTML
```html
<div class="brt-21">
  <input class="brt-21__sr" type="checkbox" id="brt-21-dark">
  <label class="brt-21__theme" for="brt-21-dark">
    <svg class="brt-21__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-21__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    <span class="brt-21__vh">Dark theme</span>
  </label>
  <div class="brt-21__progress" aria-hidden="true"></div>

  <div class="brt-21__stage">
    <article class="brt-21__article">
      <header class="brt-21__head">
        <p class="brt-21__kicker">INFRASTRUCTURE / REPORTING</p>
        <h1 class="brt-21__h">The Warehouse That Refused To Be Optimised</h1>
        <p class="brt-21__standfirst">For eleven years a distribution depot outside Doncaster has beaten every forecasting system sent to fix it. We spent a week on the floor finding out why.</p>
        <div class="brt-21__byline">
          <p>By <b>Priya Sharma</b></p>
          <p><time datetime="2026-08-12">12 August 2026</time></p>
          <p>18 min read</p>
        </div>
      </header>

      <div class="brt-21__body">
        <p>The pallet arrives at 04:12, eighteen minutes ahead of a schedule that has never once been met on purpose. Nobody on the loading bay looks at a screen. The forklift driver, a man named Ade who has worked here since the depot opened, reverses into a gap that the warehouse management system insists is occupied, and unloads twenty-four crates into it.</p>
        <p>By 06:00 the system has been wrong four times and the shift has absorbed every error without comment. This is what the consultants describe, in a report I was shown but not permitted to photograph, as an <em>informal compensation layer</em>. On the floor it is called knowing where things are.</p>

        <figure class="brt-21__fig">
          <img class="brt-21__img" src="https://images.unsplash.com/photo-1553413077-190dd305871c?w=1000&amp;h=620&amp;fit=crop&amp;auto=format" width="1000" height="620" alt="Wide view of a warehouse aisle stacked with pallets under strip lighting" loading="lazy" decoding="async">
          <figcaption>Aisle C at the start of the early shift. The racking numbering here has not matched the system's map since a 2019 refit.</figcaption>
        </figure>

        <h2 class="brt-21__h2">Eleven years, six systems</h2>
        <p>The first system went in during 2015 and lasted nine months. The second was a customisation of the first. The third was chosen because the second had failed, which is the reason most systems are chosen. Every deployment followed the same arc: a pilot that worked, a rollout that half-worked, and a slow accumulation of manual overrides until the software became a formality performed twice a shift.</p>

        <aside class="brt-21__pull">
          <p>The building is not resisting technology. It is resisting a description of itself that has never been accurate.</p>
        </aside>

        <p>What none of the six systems modelled was the weather. Not the temperature — the wind. The depot's eastern doors face open farmland, and a strong easterly makes the smaller doors unsafe to keep open, which routes every inbound pallet through a single bay for as long as the wind lasts. The floor knows this. The forecast lives on a whiteboard by the kettle.</p>
        <p>Ade's version is shorter. "It works because we know it," he says, and then, after a pause long enough to be deliberate: "They keep buying software that knows the drawing."</p>

        <h2 class="brt-21__h2">The cost of the compensation layer</h2>
        <p>There is a real cost, and the floor pays it. Three staff hold most of the undocumented knowledge. Two of them are within four years of retirement. When one was off for six weeks in 2024 with a broken wrist, dispatch accuracy fell eleven points and did not recover until the day he came back — a number the depot manager keeps written on the inside cover of a notebook rather than in any system.</p>
        <p>The seventh procurement round closes in October. The specification, for the first time, includes a section on how the software will learn from the floor rather than instruct it. Whether that survives contact with a vendor demonstration is the question everyone here has answered privately and nobody will answer on record.</p>
        <p>At 13:40 the wind picks up. Without a word, two of the bay doors come down and the queue re-forms at bay four. On the screen in the office, the plan does not change.</p>
      </div>

      <footer class="brt-21__foot">
        <p>Reporting supported by the Depot Records Project. Photographs by Sam Rivera.</p>
      </footer>
    </article>
  </div>
</div>
```
## CSS
```css
.brt-21 {
  --page: #f4f2ec;
  --panel: #ffffff;
  --ink: #000000;
  --muted: #3a3a3a;
  --edge: #000000;
  --rule: 6px;
  --mono: ui-monospace,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: 'Times New Roman',Times,Georgia,serif;
  font-size: 18px;
}

.brt-21 *,
.brt-21 *::before,
.brt-21 *::after {
  box-sizing: border-box;
  border-radius: 0;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-21 {
    --page: oklch(0.957 0.008 90);
    --panel: oklch(1 0 0);
    --ink: oklch(0 0 0);
    --muted: oklch(0.34 0 0);
  }
}

.brt-21__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.brt-21__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.brt-21__theme {
  position: fixed;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 10;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  background: var(--panel);
  color: var(--ink);
  border: 3px solid var(--edge);
  box-shadow: 4px 4px 0 var(--edge);
  cursor: pointer;
}

.brt-21__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-21__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-21__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--edge);
}

.brt-21__sr:focus-visible + .brt-21__theme {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-21__sun {
  display: none;
}

.brt-21__progress {
  position: fixed;
  inset-block-start: 0;
  inset-inline: 0;
  block-size: 8px;
  background: var(--ink);
  z-index: 9;
  scale: 0 1;
  transform-origin: left center;
  display: none;
}

@supports (animation-timeline: scroll()) {
  .brt-21__progress {
    display: block;
    animation: brt-21-progress linear both;
    animation-timeline: scroll(root block);
  }

  @keyframes brt-21-progress {
    to {
      scale: 1 1;
    }
  }
}

.brt-21__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  justify-items: center;
  padding: clamp(1.25rem,4vw,3.5rem) clamp(1rem,4vw,2.5rem);
}

.brt-21__article {
  inline-size: min(48rem,100%);
}

.brt-21__head {
  padding-inline-end: 3.5rem;
}

.brt-21__kicker {
  margin: 0 0 .9rem;
  font-family: var(--mono);
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .2em;
}

.brt-21__h {
  margin: 0;
  font-size: clamp(2.3rem,7.5vw,4.4rem);
  font-weight: 700;
  letter-spacing: -.03em;
  line-height: .98;
  text-wrap: balance;
}

.brt-21__standfirst {
  margin: 1.1rem 0 0;
  max-inline-size: 56ch;
  font-size: clamp(1.1rem,2.4vw,1.4rem);
  line-height: 1.4;
  text-wrap: pretty;
}

.brt-21__byline {
  display: flex;
  flex-wrap: wrap;
  gap: .35rem 2rem;
  margin-block-start: 1.5rem;
  padding-block: .6rem;
  border-block: var(--rule) solid var(--edge);
  border-block-end-width: 3px;
  font-family: var(--mono);
  font-size: .76rem;
  letter-spacing: .08em;
  text-transform: uppercase;
}

.brt-21__byline p {
  margin: 0;
}

.brt-21__byline b {
  font-weight: 700;
}

.brt-21__body {
  margin-block-start: 2rem;
  max-inline-size: 68ch;
  font-size: 1.06rem;
  line-height: 1.65;
}

.brt-21__body p {
  margin: 0 0 1.35rem;
  text-wrap: pretty;
}

.brt-21__body > p:first-of-type::first-letter {
  initial-letter: 3 3;
  font-weight: 700;
  padding-inline-end: .08em;
}

@supports not (initial-letter: 3) {
  .brt-21__body > p:first-of-type::first-letter {
    float: left;
    font-size: 3.8em;
    line-height: .8;
    padding-inline-end: .06em;
    font-weight: 700;
  }
}

.brt-21__h2 {
  margin: 2.5rem 0 1rem;
  padding-block-start: .6rem;
  border-block-start: 3px solid var(--edge);
  font-size: clamp(1.4rem,3.4vw,1.9rem);
  font-weight: 700;
  letter-spacing: -.02em;
  line-height: 1.1;
}

.brt-21__fig {
  margin: 2rem 0;
  padding: 0;
}

.brt-21__img {
  display: block;
  inline-size: 100%;
  aspect-ratio: 16/10;
  object-fit: cover;
  border: 3px solid var(--edge);
  background: var(--panel);
}

.brt-21__fig figcaption {
  margin-block-start: .5rem;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
  letter-spacing: .04em;
  color: var(--muted);
}

.brt-21__pull {
  margin: 2.25rem 0;
  padding-block: 1.1rem;
  border-block: var(--rule) solid var(--edge);
}

.brt-21__pull p {
  margin: 0;
  font-size: clamp(1.3rem,3.6vw,1.9rem);
  font-weight: 700;
  line-height: 1.18;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.brt-21__body em {
  font-style: italic;
}

.brt-21__foot {
  margin-block-start: 2.5rem;
  padding-block-start: .7rem;
  border-block-start: 3px solid var(--edge);
  font-family: var(--mono);
  font-size: .74rem;
  letter-spacing: .06em;
  color: var(--muted);
}

.brt-21__foot p {
  margin: 0;
}

.brt-21:has(#brt-21-dark:checked) {
  --page: #000000;
  --panel: #0a0a0a;
  --ink: #ffffff;
  --muted: #bdbdbd;
  --edge: #ffffff;
}

.brt-21:has(#brt-21-dark:checked) .brt-21__moon {
  display: none;
}

.brt-21:has(#brt-21-dark:checked) .brt-21__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-21:not(:has(#brt-21-dark:checked)) {
    --page: #000000;
    --panel: #0a0a0a;
    --ink: #ffffff;
    --muted: #bdbdbd;
    --edge: #ffffff;
  }

  .brt-21:not(:has(#brt-21-dark:checked)) .brt-21__moon {
    display: none;
  }

  .brt-21:not(:has(#brt-21-dark:checked)) .brt-21__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-21 *,
    .brt-21 *::before,
    .brt-21 *::after {
    transition: none !important;
  }

  .brt-21__progress {
    animation: none !important;
    scale: 1 1;
  }
}

@media print {
  .brt-21__progress,
    .brt-21__theme {
    display: none;
  }

  .brt-21 {
    background: #fff;
    font-size: 11pt;
  }
}

@media (forced-colors: active) {
  .brt-21__img,
    .brt-21__theme {
    border-color: CanvasText;
    box-shadow: none;
  }

  .brt-21__progress {
    background: CanvasText;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-21__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```
