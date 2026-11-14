---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/long-form-article-reading-progress/"
title: "Long-Form Article Reading Progress"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "The reading-progress bar without the scroll listener: animation-timeline: scroll() ties a scale-x animation directly to the document's scroll position, so it…"
has_js: "false"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Long-Form Article Reading Progress
Source: https://codefronts.com/layouts/css-blog-layouts/long-form-article-reading-progress/

The reading-progress bar without the scroll listener: animation-timeline: scroll() ties a scale-x animation directly to the document's scroll position, so it runs off the main thread and costs nothing. Wrapped around it, a proper long-form page — full-bleed hero, breakout figures, a sticky chapter rail and a 68ch measure.
## HTML
```html
<div class="bl-07">
  <div class="bl-07__progressTrack" aria-hidden="true"><div class="bl-07__progress"></div></div>

  <article class="bl-07__article">
    <header class="bl-07__hero">
      <img src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=1600&amp;q=70&amp;auto=format&amp;fit=crop" alt="Fog moving through a valley of pine forest at dawn" width="1600" height="900" loading="eager" decoding="async">
      <div class="bl-07__heroText">
        <p class="bl-07__kicker">Field Notes · 24 min read</p>
        <h1>The forest that measures itself</h1>
        <p class="bl-07__dek">Four thousand sensors, one contested dataset, and the researchers who spent a decade arguing about what counts as evidence.</p>
        <p class="bl-07__byline">By Ines Halvorsen · <time datetime="2026-08-04">4 August 2026</time></p>
      </div>
    </header>

    <nav class="bl-07__chapters" aria-label="Chapters">
      <p>Chapters</p>
      <ol>
        <li><a href="#bl-07-c1" aria-current="location">The ridge</a></li>
        <li><a href="#bl-07-c2">A decade of noise</a></li>
        <li><a href="#bl-07-c3">What the trees said</a></li>
      </ol>
    </nav>

    <div class="bl-07__body">
      <p class="bl-07__lede">The first sensor went up in 2016, screwed into a Douglas fir at shoulder height by a graduate student who has since left science entirely. It is still transmitting.</p>

      <h2 id="bl-07-c1">The ridge</h2>
      <p>Nobody on the original team expected the array to outlive the grant. It was meant to run for eighteen months — long enough to publish, short enough to be cheap — and then be quietly decommissioned. Instead the sensors kept reporting, the batteries kept being replaced by a rotating cast of volunteers, and the dataset grew into something none of the original questions were designed to answer.</p>
      <p>That is the part worth sitting with. A measurement programme that survives its own hypothesis becomes a different kind of object: not an experiment, but an archive.</p>

      <figure class="bl-07__figure bl-07__figure--bleed">
        <img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=1600&amp;q=70&amp;auto=format&amp;fit=crop" alt="Sunlight through tall trees in a dense forest" width="1600" height="900" loading="lazy" decoding="async">
        <figcaption>The northern transect, where sensor density is highest. <span>Photo: Unsplash</span></figcaption>
      </figure>

      <h2 id="bl-07-c2">A decade of noise</h2>
      <p>By 2019 the array was producing 40 million readings a year and almost no papers. The problem was not volume; it was that every interesting signal sat inside a band of variance that three different groups modelled three different ways.</p>
      <blockquote class="bl-07__quote">
        <p>“We spent four years learning that our error bars were the finding.”</p>
        <cite>Dr Petra Lindqvist, project lead 2018–2024</cite>
      </blockquote>
      <p>What broke the deadlock was not better statistics but better bookkeeping. When the team finally published its calibration history — every battery swap, every replaced thermistor, every week a sensor sat under snow — the disagreements collapsed into a single, boring, defensible curve.</p>

      <figure class="bl-07__figure">
        <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=1200&amp;q=70&amp;auto=format&amp;fit=crop" alt="Mountain lake reflecting a forested slope" width="1200" height="700" loading="lazy" decoding="async">
        <figcaption>Downslope of the array, the control site has no instrumentation at all.</figcaption>
      </figure>

      <h2 id="bl-07-c3">What the trees said</h2>
      <p>The published result is modest: the forest is warming slightly faster at the canopy than at the ground, and the gap widens in drought years. It fits inside a sentence. It took ten years, four institutions and an unbudgeted volunteer rota to earn.</p>
      <p>Halvorsen's last visit was in June. The original sensor — the one screwed in at shoulder height in 2016 — now sits at chest height on a noticeably thicker trunk, still reporting every fifteen minutes, still uncalibrated against anything except its own long memory.</p>
      <p class="bl-07__end">Ines Halvorsen writes about measurement. This piece was reported over three visits between 2024 and 2026.</p>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,600;1,6..72,400&family=Manrope:wght@400;500;600;700&display=swap');

.bl-07 {
  --bg: #fbfaf8;
  --text: #16181a;
  --muted: #6c7075;
  --line: #e2e0da;
  --acc: #0f766e;
  --hero-h: 68svh;
  --measure: 68ch;
  --serif: "Newsreader",ui-serif,Georgia,serif;
  --sans: "Manrope",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
}

@supports (color: oklch(50% 0 0)) {
  .bl-07 {
    --bg: oklch(98.5% .004 95);
    --text: oklch(19% .008 240);
    --muted: oklch(52% .01 240);
    --line: oklch(90% .008 95);
    --acc: oklch(48% .1 180);
  }
}

@media (prefers-color-scheme: dark) {
  .bl-07:not([data-theme="light"]) {
    --bg: #0d0f10;
    --text: #f1f2f2;
    --muted: #9aa0a4;
    --line: #25292b;
    --acc: #5eead4;
  }
}

.bl-07[data-theme="dark"] {
  --bg: #0d0f10;
  --text: #f1f2f2;
  --muted: #9aa0a4;
  --line: #25292b;
  --acc: #5eead4;
}

.bl-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--serif);
  -webkit-font-smoothing: antialiased;
}

.bl-07,
.bl-07 *,
.bl-07 *::before,
.bl-07 *::after {
  box-sizing: border-box;
}

.bl-07 a {
  color: inherit;
}

.bl-07 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 2px;
}

.bl-07 ::selection {
  background: color-mix(in oklab,var(--acc) 25%,transparent);
}

.bl-07__progressTrack {
  position: fixed;
  inset-block-start: 0;
  inset-inline: 0;
  z-index: 20;
  height: 3px;
  background: color-mix(in oklab,var(--text) 10%,transparent);
}

.bl-07__progress {
  height: 100%;
  width: 100%;
  background: var(--acc);
  transform-origin: left;
  scale: 0 1;
  opacity: .35;
}

@supports (animation-timeline: scroll()) {
  .bl-07__progress {
    opacity: 1;
    animation: bl-07-progress linear both;
    animation-timeline: scroll(root block);
  }
}

@keyframes bl-07-progress {
  from {
    scale: 0 1;
  }

  to {
    scale: 1 1;
  }
}

@supports not (animation-timeline: scroll()) {
  .bl-07__progress {
    scale: 1 1;
    opacity: .28;
  }
}

.bl-07__article {
  display: grid;
  grid-template-columns: [full-start] minmax(1rem,1fr) [content-start] min(var(--measure),100% - 2rem) [content-end] minmax(1rem,1fr) [full-end];
}

.bl-07__article > * {
  grid-column: content;
}

.bl-07__body {
  grid-column: full-start / full-end;
}

.bl-07__hero {
  grid-column: full;
  position: relative;
  min-height: var(--hero-h);
  display: grid;
  align-items: end;
  isolation: isolate;
}

.bl-07__hero img {
  position: absolute;
  inset: 0;
  z-index: -2;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: var(--line);
}

.bl-07__hero::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(to top,rgba(6,8,10,.92) 8%,rgba(6,8,10,.55) 45%,rgba(6,8,10,.15) 80%);
}

.bl-07__heroText {
  display: grid;
  gap: .9rem;
  color: #fff;
  padding: clamp(2rem,6vw,5rem) clamp(1.25rem,6vw,6rem);
  max-width: 52rem;
}

.bl-07__kicker {
  margin: 0;
  font-family: var(--sans);
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: #a7f3d0;
}

.bl-07__hero h1 {
  margin: 0;
  font-weight: 300;
  font-size: clamp(2.25rem,6.5vw,5rem);
  line-height: .98;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.bl-07__dek {
  margin: 0;
  font-size: clamp(1.0625rem,2vw,1.375rem);
  line-height: 1.55;
  color: rgba(255,255,255,.82);
  max-width: 50ch;
  text-wrap: pretty;
}

.bl-07__byline {
  margin: 0;
  font-family: var(--sans);
  font-size: .8125rem;
  letter-spacing: .03em;
  color: rgba(255,255,255,.7);
}

.bl-07__chapters {
  position: sticky;
  top: 0;
  z-index: 10;
  grid-column: full;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .5rem 1.5rem;
  padding: .75rem clamp(1.25rem,6vw,6rem);
  border-bottom: 1px solid var(--line);
  background: color-mix(in oklab,var(--bg) 88%,transparent);
  font-family: var(--sans);
}

@supports (backdrop-filter: blur(6px)) {
  .bl-07__chapters {
    backdrop-filter: blur(12px);
  }
}

.bl-07__chapters p {
  margin: 0;
  font-size: .625rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--muted);
}

.bl-07__chapters ol {
  display: flex;
  flex-wrap: wrap;
  gap: .25rem 1.25rem;
  margin: 0;
  padding: 0;
  list-style: none;
  counter-reset: bl-07-ch;
}

.bl-07__chapters li {
  counter-increment: bl-07-ch;
}

.bl-07__chapters a {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 2.5rem;
  font-size: .8125rem;
  font-weight: 500;
  color: var(--muted);
  text-decoration: none;
}

.bl-07__chapters a::before {
  content: "0" counter(bl-07-ch);
  font-size: .625rem;
  color: var(--acc);
  font-variant-numeric: tabular-nums;
}

.bl-07__chapters a:hover {
  color: var(--text);
}

.bl-07__chapters a[aria-current] {
  color: var(--text);
  text-decoration: underline;
  text-underline-offset: .3em;
  text-decoration-color: var(--acc);
}

.bl-07__body {
  padding-block: clamp(2.5rem,6vw,4.5rem) clamp(4rem,10vw,8rem);
  display: grid;
  gap: 1.5rem;
  grid-template-columns: subgrid;
}

.bl-07__body > * {
  grid-column: content;
}

.bl-07__lede {
  margin: 0;
  font-size: clamp(1.25rem,2.4vw,1.625rem);
  line-height: 1.5;
  letter-spacing: -.015em;
  color: var(--text);
  text-wrap: pretty;
}

.bl-07__body h2 {
  margin: clamp(1.5rem,3vw,2.5rem) 0 0;
  font-family: var(--sans);
  font-weight: 700;
  font-size: .75rem;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--acc);
  scroll-margin-block-start: 5rem;
}

.bl-07__body p {
  margin: 0;
  font-size: 1.1875rem;
  line-height: 1.75;
  text-wrap: pretty;
}

.bl-07__figure {
  margin: clamp(1rem,2vw,2rem) 0;
  display: grid;
  gap: .65rem;
}

.bl-07__figure img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: .375rem;
  background: var(--line);
}

.bl-07__figure figcaption {
  font-family: var(--sans);
  font-size: .8125rem;
  line-height: 1.5;
  color: var(--muted);
}

.bl-07__figure figcaption span {
  opacity: .65;
}

.bl-07__figure--bleed {
  grid-column: full;
  margin-inline: 0;
}

.bl-07__figure--bleed img {
  border-radius: 0;
  aspect-ratio: 16/9;
  object-fit: cover;
}

.bl-07__figure--bleed figcaption {
  padding-inline: clamp(1.25rem,6vw,6rem);
}

@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .bl-07__figure {
      animation: bl-07-rise linear both;
      animation-timeline: view();
      animation-range: entry 0% entry 55%;
    }

    @keyframes bl-07-rise {
      from {
        opacity: 0;
        translate: 0 2rem;
      }

      to {
        opacity: 1;
        translate: 0 0;
      }
    }
  }
}

.bl-07__quote {
  margin: clamp(1.5rem,3vw,2.5rem) 0;
  padding-inline-start: 1.5rem;
  border-inline-start: 2px solid var(--acc);
  display: grid;
  gap: .6rem;
}

.bl-07__quote p {
  margin: 0;
  font-size: clamp(1.375rem,3vw,1.875rem);
  line-height: 1.3;
  font-style: italic;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.bl-07__quote cite {
  font-family: var(--sans);
  font-style: normal;
  font-size: .8125rem;
  color: var(--muted);
}

.bl-07__end {
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--line);
  font-family: var(--sans);
  font-size: .875rem !important;
  line-height: 1.6 !important;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .bl-07__figure {
    animation: none !important;
    opacity: 1 !important;
    translate: none !important;
  }

  .bl-07 * {
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .bl-07__progress {
    background: Highlight;
  }
}
```

## JavaScript
```js

/* grid items default to min-width:auto; 0 lets wide media and long words
   stay inside their track instead of forcing the column open */
.bl-07__article > *{min-width:0;}
.bl-07__body > *{min-width:0;}

```
