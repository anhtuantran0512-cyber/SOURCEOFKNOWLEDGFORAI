---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/news-article-with-sticky-sidebar/"
title: "News Article with Sticky Sidebar"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "The workhorse news template: article body on the left at a strict measure, a related-stories rail on the right that sticks through the read, a key-points…"
has_js: "false"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: News Article with Sticky Sidebar
Source: https://codefronts.com/layouts/css-blog-layouts/news-article-with-sticky-sidebar/

The workhorse news template: article body on the left at a strict measure, a related-stories rail on the right that sticks through the read, a key-points summary box at the top (the thing readers actually use), and an inline “read next” card that appears mid-article without breaking the column.
## HTML
```html
<div class="bl-15">
  <header class="bl-15__masthead">
    <a class="bl-15__logo" href="#">The Meridian</a>
    <nav class="bl-15__nav" aria-label="Sections"><a href="#">World</a><a href="#" aria-current="page">Energy</a><a href="#">Markets</a><a href="#">Opinion</a></nav>
    <p class="bl-15__date"><time datetime="2026-08-10">10 Aug 2026</time></p>
  </header>

  <div class="bl-15__wrap">
    <article class="bl-15__article">
      <p class="bl-15__section">Energy · Grid</p>
      <h1>Four countries agree to share a single balancing market for offshore wind</h1>
      <p class="bl-15__standfirst">The deal replaces four national balancing mechanisms with one auction, and it commits each state to publishing curtailment data within 24 hours — a transparency clause that nearly sank the talks twice.</p>
      <div class="bl-15__byline">
        <img src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=100&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="100" height="100" loading="lazy" decoding="async">
        <p><strong>By Hannah Oduya</strong><span>Energy correspondent, Brussels · <time datetime="2026-08-10T06:15">06:15 CEST</time> · 7 min read</span></p>
      </div>

      <figure class="bl-15__lead">
        <img src="https://images.unsplash.com/photo-1548337138-e87d889cc369?w=1200&amp;q=70&amp;auto=format&amp;fit=crop" alt="Offshore wind turbines seen from the water at dawn" width="1200" height="700" loading="eager" fetchpriority="high" decoding="async">
        <figcaption>The North Sea cluster now accounts for 31% of the four countries' combined generation. <span>Photo: Unsplash</span></figcaption>
      </figure>

      <div class="bl-15__body">
        <aside class="bl-15__keys" aria-labelledby="bl-15-keys-h">
          <h2 id="bl-15-keys-h">The key points</h2>
          <ul>
            <li>One shared balancing auction replaces four national mechanisms from April 2027.</li>
            <li>Curtailment data must be published within 24 hours, per site.</li>
            <li>Cost of capital for new projects is expected to fall by 40-70 basis points.</li>
            <li>Two states retain a veto on interconnector outages until 2029.</li>
          </ul>
        </aside>

        <p>Negotiators announced the agreement shortly after 05:00, ending eleven months of talks that at one point collapsed entirely over which regulator would hold the auction data. The compromise gives operational control to a new joint body but keeps the raw measurements in each national register, mirrored hourly.</p>
        <p>For developers, the practical change is smaller than the political one. A single balancing market means a project bidding into the North Sea no longer needs to model four different imbalance regimes, which two of the four largest bidders have said publicly adds between 40 and 70 basis points to their cost of capital.</p>
        <p>The transparency clause is the part that will be watched. Curtailment — paying a wind farm to stop producing because the grid cannot carry the power — has until now been reported quarterly and in aggregate. From April 2027 it must be published per site within a day.</p>

        <aside class="bl-15__next">
          <p class="bl-15__nextTag">Read next</p>
          <h2><a href="#">The 41 hours in February when the grid paid to stop the wind</a></h2>
          <p>An investigation into last winter's curtailment payments, and the two substations that caused most of them.</p>
        </aside>

        <p>Not everyone is satisfied. Two of the four states negotiated a veto over interconnector outages until 2029, which grid operators in the other two say reintroduces exactly the national discretion the agreement was meant to remove.</p>
        <p>“It is a single market with two emergency brakes still bolted on,” said one operator's representative, who was not authorised to speak publicly. “That is still better than four separate cars.”</p>
        <p>The agreement now goes to four parliaments. Officials expect ratification by December, with the joint body standing up in the second quarter of 2027.</p>
        <p class="bl-15__end">Additional reporting from Copenhagen and The Hague.</p>
      </div>
    </article>

    <aside class="bl-15__rail" aria-labelledby="bl-15-rail-h">
      <div class="bl-15__railInner">
        <h2 class="bl-15__railHead" id="bl-15-rail-h">Related stories</h2>
        <ol class="bl-15__related">
          <li><a href="#"><span>Grid</span><strong>Interconnector delays push three projects past 2030</strong><i>5 min read</i></a></li>
          <li><a href="#"><span>Markets</span><strong>Why negative electricity prices are now normal in May</strong><i>8 min read</i></a></li>
          <li><a href="#"><span>Analysis</span><strong>The balancing market explained in five charts</strong><i>6 min read</i></a></li>
          <li><a href="#"><span>Policy</span><strong>Who actually owns the North Sea's cables</strong><i>11 min read</i></a></li>
          <li><a href="#"><span>Energy</span><strong>Denmark's curtailment register, one year on</strong><i>7 min read</i></a></li>
        </ol>
        <div class="bl-15__brief">
          <h3>Energy Briefing</h3>
          <p>The week's grid and power-market reporting, every Friday.</p>
          <a class="bl-15__briefCta" href="#">Get the newsletter</a>
        </div>
      </div>
    </aside>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&family=Newsreader:opsz,[email protected],400;6..72,500&display=swap');

.bl-15 {
  --bg: #ffffff;
  --surface: #f6f7f8;
  --text: #0c0e10;
  --muted: #5b6167;
  --line: #e2e5e8;
  --acc: #0b5f4a;
  --stick: 1.5rem;
  --rail-max: calc(100svh - 3rem);
  --sans: "Archivo",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --serif: "Newsreader",ui-serif,Georgia,serif;
}

@supports (color: oklch(50% 0 0)) {
  .bl-15 {
    --bg: oklch(100% 0 0);
    --surface: oklch(97% .003 220);
    --text: oklch(15% .008 230);
    --muted: oklch(48% .012 230);
    --line: oklch(91% .006 225);
    --acc: oklch(42% .1 165);
  }
}

@media (prefers-color-scheme: dark) {
  .bl-15:not([data-theme="light"]) {
    --bg: #0a0c0d;
    --surface: #14171a;
    --text: #eef1f2;
    --muted: #98a0a6;
    --line: #23282c;
    --acc: #4ade9f;
  }
}

.bl-15[data-theme="dark"] {
  --bg: #0a0c0d;
  --surface: #14171a;
  --text: #eef1f2;
  --muted: #98a0a6;
  --line: #23282c;
  --acc: #4ade9f;
}

.bl-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--serif);
  -webkit-font-smoothing: antialiased;
}

.bl-15,
.bl-15 *,
.bl-15 *::before,
.bl-15 *::after {
  box-sizing: border-box;
}

.bl-15 a {
  color: inherit;
  text-decoration: none;
}

.bl-15 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 2px;
}

.bl-15 img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: var(--line);
}

.bl-15__masthead {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .5rem 1.5rem;
  padding: .85rem clamp(1.25rem,4vw,3rem);
  border-bottom: 2px solid var(--text);
  font-family: var(--sans);
}

.bl-15__logo {
  font-size: 1.25rem;
  font-weight: 800;
  letter-spacing: -.035em;
}

.bl-15__nav {
  display: flex;
  flex-wrap: wrap;
  gap: .125rem;
  margin-inline-end: auto;
}

.bl-15__nav a {
  display: grid;
  place-items: center;
  min-height: 2.5rem;
  padding: 0 .7rem;
  border-radius: .25rem;
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--muted);
}

.bl-15__nav a:hover {
  color: var(--text);
  background: var(--surface);
}

.bl-15__nav a[aria-current="page"] {
  color: var(--acc);
}

.bl-15__date {
  margin: 0;
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-15__wrap {
  display: grid;
  gap: clamp(1.5rem,3vw,3rem);
  align-items: start;
  grid-template-columns: minmax(0,1fr) clamp(16rem,24vw,21rem);
  max-width: 86rem;
  margin-inline: auto;
  padding: clamp(1.5rem,3.5vw,3rem) clamp(1.25rem,4vw,3rem) clamp(3rem,7vw,5rem);
}

.bl-15__article {
  display: grid;
  gap: 1.1rem;
  min-width: 0;
}

.bl-15__section {
  margin: 0;
  font-family: var(--sans);
  font-size: .6875rem;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.bl-15__article h1 {
  margin: 0;
  font-family: var(--sans);
  font-size: clamp(1.875rem,4.4vw,3rem);
  font-weight: 800;
  line-height: 1.04;
  letter-spacing: -.035em;
  max-width: 34ch;
  text-wrap: balance;
}

.bl-15__standfirst {
  margin: 0;
  font-size: clamp(1.0625rem,1.9vw,1.3125rem);
  line-height: 1.6;
  color: var(--muted);
  max-width: 62ch;
  text-wrap: pretty;
}

.bl-15__byline {
  display: flex;
  align-items: center;
  gap: .75rem;
  padding-block: .5rem 1rem;
  border-bottom: 1px solid var(--line);
}

.bl-15__byline img {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  flex: 0 0 auto;
}

.bl-15__byline p {
  margin: 0;
  display: grid;
  gap: .1rem;
  font-family: var(--sans);
  font-size: .875rem;
}

.bl-15__byline span {
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-15__lead {
  margin: 0;
  display: grid;
  gap: .5rem;
}

.bl-15__lead img {
  aspect-ratio: 12/7;
  border-radius: .375rem;
}

.bl-15__lead figcaption {
  font-family: var(--sans);
  font-size: .75rem;
  line-height: 1.5;
  color: var(--muted);
}

.bl-15__lead figcaption span {
  opacity: .65;
}

.bl-15__body {
  display: grid;
  row-gap: 1.35rem;
  grid-template-columns: [wide-start] minmax(0,1fr) [narrow-start] min(64ch,100%) [narrow-end] minmax(0,1fr) [wide-end];
  padding-top: .5rem;
}

.bl-15__body > * {
  grid-column: narrow;
  margin: 0;
}

.bl-15__body p {
  font-size: 1.125rem;
  line-height: 1.72;
  text-wrap: pretty;
}

.bl-15__keys {
  grid-column: wide;
  padding: clamp(1rem,2.5vw,1.5rem);
  border-radius: .75rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-inline-start: 3px solid var(--acc);
}

.bl-15__keys h2 {
  margin: 0 0 .75rem;
  font-family: var(--sans);
  font-size: .6875rem;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.bl-15__keys ul {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .5rem;
}

.bl-15__keys li {
  display: grid;
  grid-template-columns: 1rem minmax(0,1fr);
  gap: .6rem;
  font-size: 1rem;
  line-height: 1.55;
  text-wrap: pretty;
}

.bl-15__keys li::before {
  content: "—";
  color: var(--acc);
  font-family: var(--sans);
}

.bl-15__next {
  grid-column: wide;
  display: grid;
  gap: .4rem;
  padding: clamp(1rem,2.5vw,1.5rem);
  border-block: 1px solid var(--line);
  background: linear-gradient(90deg,color-mix(in oklab,var(--acc) 6%,transparent),transparent 70%);
}

.bl-15__nextTag {
  margin: 0;
  font-family: var(--sans);
  font-size: .625rem !important;
  font-weight: 800;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--acc);
}

.bl-15__next h2 {
  margin: 0;
  font-family: var(--sans);
  font-size: clamp(1.125rem,2.4vw,1.4375rem);
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.bl-15__next h2 a {
  background: linear-gradient(currentColor,currentColor) 0 100%/0 1px no-repeat;
  transition: background-size .35s cubic-bezier(.16,1,.3,1);
}

.bl-15__next h2 a:hover {
  background-size: 100% 1px;
}

.bl-15__next p {
  font-size: .9375rem !important;
  line-height: 1.6 !important;
  color: var(--muted);
}

.bl-15__end {
  padding-top: 1.25rem;
  border-top: 1px solid var(--line);
  font-family: var(--sans);
  font-size: .8125rem !important;
  line-height: 1.6 !important;
  color: var(--muted);
  font-style: italic;
}

.bl-15__rail {
  position: sticky;
  top: var(--stick);
  align-self: start;
  min-width: 0;
}

.bl-15__railInner {
  display: grid;
  gap: 1.25rem;
  max-height: var(--rail-max);
  overflow: auto;
  scrollbar-width: thin;
  padding: 1.25rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: .75rem;
}

.bl-15__railHead {
  margin: 0;
  font-family: var(--sans);
  font-size: .6875rem;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
}

.bl-15__related {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
}

.bl-15__related li + li {
  border-top: 1px solid var(--line);
}

.bl-15__related a {
  display: grid;
  gap: .25rem;
  padding: .85rem 0;
  min-height: 2.75rem;
}

.bl-15__related span {
  font-family: var(--sans);
  font-size: .5625rem;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.bl-15__related strong {
  font-family: var(--sans);
  font-size: .9375rem;
  font-weight: 600;
  line-height: 1.3;
  letter-spacing: -.015em;
  text-wrap: pretty;
}

.bl-15__related i {
  font-family: var(--sans);
  font-style: normal;
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-15__related a:hover strong {
  color: var(--acc);
}

.bl-15__brief {
  display: grid;
  gap: .5rem;
  padding-top: 1.25rem;
  border-top: 1px solid var(--line);
}

.bl-15__brief h3 {
  margin: 0;
  font-family: var(--sans);
  font-size: .9375rem;
  font-weight: 700;
  letter-spacing: -.015em;
}

.bl-15__brief p {
  margin: 0;
  font-size: .875rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.bl-15__briefCta {
  justify-self: start;
  display: grid;
  place-items: center;
  min-height: 2.75rem;
  padding: 0 1.1rem;
  margin-top: .25rem;
  border-radius: .375rem;
  background: var(--acc);
  color: #fff;
  font-family: var(--sans);
  font-size: .8125rem;
  font-weight: 700;
  transition: filter .18s ease;
}

.bl-15__briefCta:hover {
  filter: brightness(1.1);
}

@media (max-width: 64rem) {
  .bl-15__wrap {
    grid-template-columns: minmax(0,1fr);
  }

  .bl-15__rail {
    position: static;
  }

  .bl-15__railInner {
    max-height: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bl-15 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .bl-15__briefCta {
    forced-color-adjust: none;
    background: Highlight;
    color: HighlightText;
  }
}
```
