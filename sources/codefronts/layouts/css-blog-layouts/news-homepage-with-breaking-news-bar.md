---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/news-homepage-with-breaking-news-bar/"
title: "News Homepage with Breaking News Bar"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "A dense, information-first news front page: a live breaking bar that scrolls headlines with a CSS-only marquee (pausable, reduced-motion safe, and not the…"
has_js: "true"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: News Homepage with Breaking News Bar
Source: https://codefronts.com/layouts/css-blog-layouts/news-homepage-with-breaking-news-bar/

A dense, information-first news front page: a live breaking bar that scrolls headlines with a CSS-only marquee (pausable, reduced-motion safe, and not the deprecated <marquee>), a five-region grid with a lead story, a most-read column, and a two-row wire feed. Eight lines of JS keep the clock ticking — everything else is CSS.
## HTML
```html
<div class="bl-02">
  <div class="bl-02__bar" data-level="breaking">
    <p class="bl-02__barTag">Breaking</p>
    <div class="bl-02__ticker">
      <div class="bl-02__track">
        <ul class="bl-02__ticketList">
          <li><a href="#bl-02-main">Central bank holds rates for the third quarter running</a></li>
          <li><a href="#bl-02-main">Port strike enters day nine as talks resume in Antwerp</a></li>
          <li><a href="#bl-02-main">Regulator opens inquiry into ticketing platform fees</a></li>
          <li><a href="#bl-02-main">Wildfire crews contain 60% of the Kelowna perimeter</a></li>
        </ul>
        <ul class="bl-02__ticketList" aria-hidden="true">
          <li><a href="#bl-02-main" tabindex="-1">Central bank holds rates for the third quarter running</a></li>
          <li><a href="#bl-02-main" tabindex="-1">Port strike enters day nine as talks resume in Antwerp</a></li>
          <li><a href="#bl-02-main" tabindex="-1">Regulator opens inquiry into ticketing platform fees</a></li>
          <li><a href="#bl-02-main" tabindex="-1">Wildfire crews contain 60% of the Kelowna perimeter</a></li>
        </ul>
      </div>
    </div>
    <p class="bl-02__clock" data-clock>—</p>
  </div>

  <header class="bl-02__head">
    <a class="bl-02__logo" href="#bl-02-main">The Wire<span>·</span>Daily</a>
    <nav class="bl-02__nav" aria-label="Sections">
      <a href="#bl-02-main" aria-current="page">Top</a><a href="#bl-02-main">World</a><a href="#bl-02-main">Business</a>
      <a href="#bl-02-main">Politics</a><a href="#bl-02-main">Science</a><a href="#bl-02-main">Sport</a>
    </nav>
    <a class="bl-02__cta" href="#bl-02-main">Subscribe</a>
  </header>

  <main class="bl-02__main" id="bl-02-main">
    <article class="bl-02__lead">
      <p class="bl-02__flag">Live · Updated 4 min ago</p>
      <h1><a href="#bl-02-main">Coalition talks collapse hours before the budget deadline</a></h1>
      <figure class="bl-02__leadFig">
        <img src="https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?w=1200&amp;q=70&amp;auto=format&amp;fit=crop" alt="Parliament building exterior at dusk" width="1200" height="700" loading="eager" decoding="async">
        <figcaption>Negotiators left the chamber shortly after midnight. <span>Photo: Unsplash</span></figcaption>
      </figure>
      <p class="bl-02__standfirst">Three parties walked out of the finance committee within twenty minutes of each other, leaving the treasury with a working majority of one and a deadline it has already missed twice.</p>
      <p class="bl-02__byline">Daniel Ross and Aoife Byrne · <time datetime="2026-08-10T07:40">07:40 BST</time></p>
    </article>

    <section class="bl-02__second" aria-label="Secondary stories">
      <article><h2><a href="#bl-02-main">Treasury drafts contingency spending plan</a></h2><p>Officials say the fallback covers eleven weeks.</p></article>
      <article><h2><a href="#bl-02-main">What a missed budget actually triggers</a></h2><p>Explainer: the four automatic mechanisms.</p></article>
      <article><h2><a href="#bl-02-main">Markets shrug, then don't</a></h2><p>Gilts moved 14 basis points before the open.</p></article>
    </section>

    <aside class="bl-02__read" aria-labelledby="bl-02-read-h">
      <h2 id="bl-02-read-h">Most read</h2>
      <ol>
        <li><a href="#bl-02-main">The 19 seats that decide the vote</a></li>
        <li><a href="#bl-02-main">Interview: the whip who saw it coming</a></li>
        <li><a href="#bl-02-main">Rail fares rise again in September</a></li>
        <li><a href="#bl-02-main">A quiet change to student visa rules</a></li>
        <li><a href="#bl-02-main">Why the pothole budget doubled</a></li>
      </ol>
      <p class="bl-02__readNote">Ranked by completion, not clicks.</p>
    </aside>

    <section class="bl-02__wire" aria-labelledby="bl-02-wire-h">
      <h2 class="bl-02__wireHead" id="bl-02-wire-h">The wire</h2>
      <div class="bl-02__wireGrid">
        <article class="bl-02__wireCard">
          <a class="bl-02__thumb" href="#bl-02-main" tabindex="-1" aria-hidden="true"><img src="https://images.unsplash.com/photo-1444723121867-7a241cacace9?w=400&amp;q=60&amp;auto=format&amp;fit=crop" alt="" width="400" height="300" loading="lazy" decoding="async"></a>
          <div><p class="bl-02__cat">Business</p><h3><a href="#bl-02-main">Two supermarket chains confirm merger review filing</a></h3><p class="bl-02__stamp"><time datetime="2026-08-10T06:12">06:12</time> · 3 min</p></div>
        </article>
        <article class="bl-02__wireCard">
          <a class="bl-02__thumb" href="#bl-02-main" tabindex="-1" aria-hidden="true"><img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400&amp;q=60&amp;auto=format&amp;fit=crop" alt="" width="400" height="300" loading="lazy" decoding="async"></a>
          <div><p class="bl-02__cat">Science</p><h3><a href="#bl-02-main">Orbital debris rules tighten for commercial launches</a></h3><p class="bl-02__stamp"><time datetime="2026-08-10T05:48">05:48</time> · 5 min</p></div>
        </article>
        <article class="bl-02__wireCard">
          <a class="bl-02__thumb" href="#bl-02-main" tabindex="-1" aria-hidden="true"><img src="https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=400&amp;q=60&amp;auto=format&amp;fit=crop" alt="" width="400" height="300" loading="lazy" decoding="async"></a>
          <div><p class="bl-02__cat">Technology</p><h3><a href="#bl-02-main">Chip fab breaks ground outside Dresden</a></h3><p class="bl-02__stamp"><time datetime="2026-08-10T05:20">05:20</time> · 4 min</p></div>
        </article>
        <article class="bl-02__wireCard">
          <div><p class="bl-02__cat">World</p><h3><a href="#bl-02-main">Ceasefire monitors granted access to the northern corridor</a></h3><p class="bl-02__stamp"><time datetime="2026-08-10T04:55">04:55</time> · 6 min</p></div>
        </article>
        <article class="bl-02__wireCard">
          <div><p class="bl-02__cat">Sport</p><h3><a href="#bl-02-main">Late equaliser sends the tie to a replay</a></h3><p class="bl-02__stamp"><time datetime="2026-08-10T04:30">04:30</time> · 2 min</p></div>
        </article>
        <article class="bl-02__wireCard">
          <div><p class="bl-02__cat">Culture</p><h3><a href="#bl-02-main">National gallery returns two disputed bronzes</a></h3><p class="bl-02__stamp"><time datetime="2026-08-10T04:02">04:02</time> · 4 min</p></div>
        </article>
      </div>
    </section>
  </main>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&family=Source+Serif+4:opsz,[email protected],400;8..60,600;8..60,700&display=swap');

.bl-02 {
  --bg: #ffffff;
  --surface: #f7f7f8;
  --text: #0b0b0f;
  --muted: #5f6169;
  --line: #e3e4e8;
  --acc: #1d4ed8;
  --bar: #b91c1c;
  --bar-fg: #ffffff;
  --sans: "Archivo",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --serif: "Source Serif 4",ui-serif,Georgia,"Times New Roman",serif;
}

@supports (color: oklch(50% 0 0)) {
  .bl-02 {
    --bg: oklch(100% 0 0);
    --surface: oklch(97% .003 270);
    --text: oklch(14% .01 275);
    --muted: oklch(50% .015 272);
    --line: oklch(91% .006 272);
    --acc: oklch(48% .2 265);
    --bar: oklch(48% .19 27);
  }
}

@media (prefers-color-scheme: dark) {
  .bl-02:not([data-theme="light"]) {
    --bg: #0a0a0c;
    --surface: #14141a;
    --text: #f4f4f6;
    --muted: #9b9da6;
    --line: #26262e;
    --acc: #7c9cff;
    --bar: #dc2626;
  }
}

.bl-02[data-theme="dark"] {
  --bg: #0a0a0c;
  --surface: #14141a;
  --text: #f4f4f6;
  --muted: #9b9da6;
  --line: #26262e;
  --acc: #7c9cff;
  --bar: #dc2626;
}

.bl-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.bl-02,
.bl-02 *,
.bl-02 *::before,
.bl-02 *::after {
  box-sizing: border-box;
}

.bl-02 img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: var(--line);
}

.bl-02 a {
  color: inherit;
  text-decoration: none;
}

.bl-02 a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.bl-02__bar {
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto;
  align-items: center;
  gap: .75rem;
  background: var(--bar);
  color: var(--bar-fg);
  padding: 0 clamp(.75rem,2vw,1.5rem);
  min-height: 2.75rem;
}

.bl-02__barTag {
  margin: 0;
  font-size: .6875rem;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  padding: .3rem .55rem;
  border: 1px solid color-mix(in oklab,var(--bar-fg) 55%,transparent);
  border-radius: .25rem;
}

.bl-02__ticker {
  overflow: hidden;
  mask-image: linear-gradient(90deg,transparent,#000 3rem,#000 calc(100% - 3rem),transparent);
}

.bl-02__track {
  display: flex;
  width: max-content;
  animation: bl-02-roll 34s linear infinite;
}

.bl-02__ticker:hover .bl-02__track,
.bl-02__ticker:focus-within .bl-02__track {
  animation-play-state: paused;
}

@keyframes bl-02-roll {
  to {
    translate: -50% 0;
  }
}

.bl-02__ticketList {
  display: flex;
  margin: 0;
  padding: 0;
  list-style: none;
}

.bl-02__ticketList a {
  display: inline-flex;
  align-items: center;
  min-height: 2.75rem;
  padding-inline: 1.25rem;
  font-size: .875rem;
  font-weight: 500;
  white-space: nowrap;
}

.bl-02__ticketList a::before {
  content: "◆";
  font-size: .5rem;
  margin-inline-end: .75rem;
  opacity: .7;
}

.bl-02__ticketList a:hover {
  text-decoration: underline;
  text-underline-offset: .25em;
}

.bl-02__clock {
  margin: 0;
  font-size: .75rem;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
  letter-spacing: .04em;
}

.bl-02__head {
  position: sticky;
  top: 0;
  z-index: 6;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .75rem 1.5rem;
  padding: .75rem clamp(1rem,3vw,2.5rem);
  background: color-mix(in oklab,var(--bg) 88%,transparent);
  border-bottom: 1px solid var(--line);
}

@supports (backdrop-filter: blur(6px)) {
  .bl-02__head {
    backdrop-filter: blur(12px);
  }
}

.bl-02__logo {
  font-size: 1.25rem;
  font-weight: 800;
  letter-spacing: -.03em;
}

.bl-02__logo span {
  color: var(--bar);
  margin-inline: .15em;
}

.bl-02__nav {
  display: flex;
  flex-wrap: wrap;
  gap: .125rem;
  margin-inline-end: auto;
}

.bl-02__nav a {
  display: grid;
  place-items: center;
  min-height: 2.75rem;
  padding: 0 .7rem;
  border-radius: .375rem;
  font-size: .8125rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .06em;
  color: var(--muted);
}

.bl-02__nav a:hover {
  color: var(--text);
  background: var(--surface);
}

.bl-02__nav a[aria-current="page"] {
  color: var(--bg);
  background: var(--text);
}

.bl-02__cta {
  display: grid;
  place-items: center;
  min-height: 2.75rem;
  padding: 0 1.1rem;
  border-radius: .375rem;
  background: var(--acc);
  color: #fff;
  font-size: .8125rem;
  font-weight: 700;
  letter-spacing: .02em;
  transition: filter .18s ease;
}

.bl-02__cta:hover {
  filter: brightness(1.12);
}

.bl-02__main {
  display: grid;
  gap: clamp(1.5rem,2.5vw,2.5rem);
  grid-template-columns: minmax(0,1.6fr) minmax(0,1fr) minmax(0,.9fr);
  grid-template-areas: "lead second read" "wire wire read";
  align-items: start;
  max-width: 100rem;
  margin-inline: auto;
  padding: clamp(1.25rem,3vw,2.5rem) clamp(1rem,3vw,2.5rem) 4rem;
}

.bl-02__lead {
  grid-area: lead;
  display: grid;
  gap: .875rem;
}

.bl-02__flag {
  margin: 0;
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  justify-self: start;
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--bar);
}

.bl-02__flag::before {
  content: "";
  width: .5rem;
  height: .5rem;
  border-radius: 50%;
  background: var(--bar);
  animation: bl-02-pulse 2s ease-in-out infinite;
}

@keyframes bl-02-pulse {
  50% {
    opacity: .25;
    scale: .8;
  }
}

.bl-02__lead h1 {
  margin: 0;
  font-family: var(--serif);
  font-weight: 700;
  font-size: clamp(1.875rem,4.2vw,3.25rem);
  line-height: 1.02;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.bl-02__lead h1 a:hover {
  color: var(--acc);
}

.bl-02__leadFig {
  margin: 0;
  display: grid;
  gap: .5rem;
}

.bl-02__leadFig img {
  aspect-ratio: 12/7;
  border-radius: .25rem;
}

.bl-02__leadFig figcaption {
  font-size: .75rem;
  color: var(--muted);
  line-height: 1.5;
}

.bl-02__leadFig figcaption span {
  opacity: .7;
}

.bl-02__standfirst {
  margin: 0;
  font-family: var(--serif);
  font-size: 1.0625rem;
  line-height: 1.6;
  max-width: 62ch;
  text-wrap: pretty;
}

.bl-02__byline {
  margin: 0;
  font-size: .75rem;
  font-weight: 600;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: .06em;
  font-variant-numeric: tabular-nums;
}

.bl-02__second {
  grid-area: second;
  display: grid;
  gap: 1rem;
  align-content: start;
  padding-inline-start: clamp(0rem,1.5vw,1.5rem);
  border-inline-start: 1px solid var(--line);
}

.bl-02__second article {
  display: grid;
  gap: .35rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--line);
}

.bl-02__second article:last-child {
  border-bottom: 0;
  padding-bottom: 0;
}

.bl-02__second h2 {
  margin: 0;
  font-family: var(--serif);
  font-size: 1.25rem;
  font-weight: 600;
  line-height: 1.15;
  letter-spacing: -.015em;
  text-wrap: balance;
}

.bl-02__second h2 a:hover {
  color: var(--acc);
}

.bl-02__second p {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
  line-height: 1.5;
}

.bl-02__read {
  grid-area: read;
  position: sticky;
  top: 5rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: .5rem;
  padding: 1.25rem;
}

.bl-02__read h2 {
  margin: 0 0 .875rem;
  font-size: .6875rem;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
}

.bl-02__read ol {
  margin: 0;
  padding: 0;
  list-style: none;
  counter-reset: bl-02-read;
  display: grid;
}

.bl-02__read li {
  counter-increment: bl-02-read;
  border-top: 1px solid var(--line);
}

.bl-02__read li:first-child {
  border-top: 0;
}

.bl-02__read a {
  display: grid;
  grid-template-columns: 1.75rem 1fr;
  gap: .5rem;
  align-items: start;
  padding: .75rem 0;
  min-height: 2.75rem;
  font-size: .9375rem;
  line-height: 1.3;
  font-weight: 500;
  text-wrap: pretty;
}

.bl-02__read a::before {
  content: counter(bl-02-read);
  font-size: 1.125rem;
  font-weight: 800;
  color: color-mix(in oklab,var(--text) 22%,transparent);
  font-variant-numeric: tabular-nums;
}

.bl-02__read a:hover {
  color: var(--acc);
}

.bl-02__readNote {
  margin: .875rem 0 0;
  font-size: .6875rem;
  color: var(--muted);
}

.bl-02__wire {
  grid-area: wire;
  padding-top: 1.5rem;
  border-top: 2px solid var(--text);
}

.bl-02__wireHead {
  margin: 0 0 1rem;
  font-size: .75rem;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
}

.bl-02__wireGrid {
  display: grid;
  gap: 1rem 1.5rem;
  grid-template-columns: repeat(auto-fill,minmax(min(100%,19rem),1fr));
}

.bl-02__wireCard {
  container-type: inline-size;
  display: grid;
  gap: .75rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--line);
}

.bl-02__wireCard > div {
  display: grid;
  gap: .3rem;
  align-content: start;
}

.bl-02__thumb {
  display: block;
  aspect-ratio: 4/3;
  overflow: hidden;
  border-radius: .25rem;
}

.bl-02__cat {
  margin: 0;
  font-size: .625rem;
  font-weight: 800;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--acc);
}

.bl-02__wireCard h3 {
  margin: 0;
  font-size: 1rem;
  font-weight: 600;
  line-height: 1.25;
  letter-spacing: -.01em;
  text-wrap: pretty;
}

.bl-02__wireCard h3 a:hover {
  text-decoration: underline;
  text-underline-offset: .2em;
}

.bl-02__stamp {
  margin: 0;
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

@container (min-width: 22rem) {
  .bl-02__wireCard:has(.bl-02__thumb) {
    grid-template-columns: 6.5rem minmax(0,1fr);
    align-items: start;
  }
}

@media (max-width: 74rem) {
  .bl-02__main {
    grid-template-columns: minmax(0,1.6fr) minmax(0,1fr);
    grid-template-areas: "lead read" "second read" "wire wire";
  }
}

@media (max-width: 52rem) {
  .bl-02__main {
    grid-template-columns: minmax(0,1fr);
    grid-template-areas: "lead" "second" "read" "wire";
  }

  .bl-02__second {
    padding-inline-start: 0;
    border-inline-start: 0;
    border-top: 1px solid var(--line);
    padding-top: 1rem;
  }

  .bl-02__read {
    position: static;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bl-02__track {
    animation: none;
  }

  .bl-02 * {
    transition: none !important;
  }

  .bl-02__flag::before {
    animation: none;
  }

  .bl-02__ticker {
    overflow-x: auto;
  }
}

@media (forced-colors: active) {
  .bl-02__nav a[aria-current="page"],
    .bl-02__cta {
    forced-color-adjust: none;
    background: Highlight;
    color: HighlightText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.bl-02');
  if (!root) return;
  const clock = root.querySelector('[data-clock]');
  const fmt = new Intl.DateTimeFormat([], { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false });
  const tick = () => { clock.textContent = fmt.format(new Date()); };
  tick();
  const id = setInterval(tick, 1000);
  document.addEventListener('visibilitychange', () => { if (document.hidden) clearInterval(id); }, { once: true });
})();
```
