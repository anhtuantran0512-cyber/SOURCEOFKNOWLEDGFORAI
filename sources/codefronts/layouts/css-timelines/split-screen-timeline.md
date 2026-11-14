---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/split-screen-timeline/"
title: "Comparison Dual Timeline — Two Histories on One Spine"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "Two parallel stories on a shared chronological spine: company A on the left, company B on the right, year markers riding the center rail, with color-coded…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Comparison Dual Timeline — Two Histories on One Spine
Source: https://codefronts.com/layouts/css-timelines/split-screen-timeline/

Two parallel stories on a shared chronological spine: company A on the left, company B on the right, year markers riding the center rail, with color-coded sides announced in headers (never color alone) — the format for rivalry retrospectives, before/after process comparisons and 'us vs the old way' marketing pages.
## HTML
```html
<section class="tls-29" aria-label="Comparison dual timeline demo">
  <div class="tls-29__inner">
    <h3 class="tls-29__title">Two roads to the same market</h3>
    <div class="tls-29__heads" aria-hidden="true"><p class="tls-29__hA">Meridian Co.</p><span></span><p class="tls-29__hB">Alto Labs</p></div>
    <ol class="tls-29__grid" role="list">
      <li class="tls-29__year" style="grid-row:1"><time datetime="2021">2021</time></li>
      <li class="tls-29__ev tls-29__ev--a" data-side="Meridian" style="grid-row:1"><h4>Raises $30M Series B</h4><p>Bets on enterprise sales and a 40-person go-to-market org.</p></li>
      <li class="tls-29__ev tls-29__ev--b" data-side="Alto" style="grid-row:1"><h4>Two founders, open beta</h4><p>Ships a free tier and answers every support email personally.</p></li>
      <li class="tls-29__year" style="grid-row:2"><time datetime="2023">2023</time></li>
      <li class="tls-29__ev tls-29__ev--a" data-side="Meridian" style="grid-row:2"><h4>500 enterprise logos</h4><p>Revenue up 4×; NPS quietly down 20 points.</p></li>
      <li class="tls-29__ev tls-29__ev--b" data-side="Alto" style="grid-row:2"><h4>100k self-serve users</h4><p>Still four people. The free tier becomes the funnel.</p></li>
      <li class="tls-29__year" style="grid-row:3"><time datetime="2026">2026</time></li>
      <li class="tls-29__ev tls-29__ev--a" data-side="Meridian" style="grid-row:3"><h4>Acquired for $400M</h4><p>The enterprise book of business was the asset.</p></li>
      <li class="tls-29__ev tls-29__ev--b" data-side="Alto" style="grid-row:3"><h4>Profitably independent</h4><p>Twelve people, no board, and the category's best-loved product.</p></li>
    </ol>
  </div>
</section>
```
## CSS
```css
.tls-29,
.tls-29 *,
.tls-29 *::before,
.tls-29 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-29 {
  min-height: 100vh;
  width: 100%;
  --a: #1d4ed8;
  --b: #b45309;
  --tl-line: #e5e5e5;
  --tl-ink: #171717;
  --tl-mut: #737373;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #fafafa;
  padding: 64px 24px;
  display: grid;
  place-items: center;
}

.tls-29__inner {
  width: min(780px,100%);
}

.tls-29__title {
  font-size: clamp(22px,3.5vw,28px);
  font-weight: 800;
  color: var(--tl-ink);
  letter-spacing: -.02em;
  text-align: center;
  margin-bottom: 26px;
}

.tls-29__heads {
  display: grid;
  grid-template-columns: 1fr 56px 1fr;
  margin-bottom: 18px;
}

.tls-29__hA,
.tls-29__hB {
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
  text-align: center;
  padding: 8px 0;
  border-radius: 8px;
}

.tls-29__hA {
  color: var(--a);
  background: #eff4ff;
}

.tls-29__hB {
  color: var(--b);
  background: #fff7ea;
}

.tls-29__grid {
  list-style: none;
  display: grid;
  grid-template-columns: 1fr 56px 1fr;
  row-gap: 26px;
  position: relative;
}

.tls-29__grid::before {
  content: '';
  position: absolute;
  left: 50%;
  translate: -50% 0;
  top: -6px;
  bottom: -6px;
  width: 2px;
  background: var(--tl-line);
}

.tls-29__year {
  grid-column: 2;
  align-self: start;
  justify-self: center;
  z-index: 1;
}

.tls-29__year time {
  display: grid;
  place-items: center;
  width: 48px;
  height: 28px;
  font-size: 12.5px;
  font-weight: 800;
  color: var(--tl-ink);
  background: #fff;
  border: 2px solid var(--tl-line);
  border-radius: 999px;
}

.tls-29__ev {
  background: #fff;
  border: 1px solid var(--tl-line);
  border-radius: 14px;
  padding: 16px 18px;
}

.tls-29__ev--a {
  grid-column: 1;
  margin-right: 14px;
  border-top-right-radius: 4px;
  border-top: 3px solid var(--a);
}

.tls-29__ev--b {
  grid-column: 3;
  margin-left: 14px;
  border-top-left-radius: 4px;
  border-top: 3px solid var(--b);
}

.tls-29__ev h4 {
  font-size: 15px;
  font-weight: 750;
  color: var(--tl-ink);
  letter-spacing: -.01em;
  margin-bottom: 5px;
}

.tls-29__ev p {
  font-size: 13.5px;
  line-height: 1.55;
  color: var(--tl-mut);
  text-wrap: pretty;
}

@media (max-width: 620px) {
  .tls-29__heads {
    display: none;
  }

  .tls-29__grid {
    grid-template-columns: 1fr;
    row-gap: 14px;
  }

  .tls-29__grid::before {
    display: none;
  }

  .tls-29__year,
    .tls-29__ev--a,
    .tls-29__ev--b {
    grid-column: 1;
    grid-row: auto!important;
    margin: 0;
  }

  .tls-29__year {
    justify-self: start;
  }

  .tls-29__ev::before {
    content: attr(data-side);
    display: inline-block;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: .1em;
    text-transform: uppercase;
    margin-bottom: 8px;
    padding: 2px 9px;
    border-radius: 999px;
  }

  .tls-29__ev--a::before {
    color: var(--a);
    background: #eff4ff;
  }

  .tls-29__ev--b::before {
    color: var(--b);
    background: #fff7ea;
  }
}
```

## JavaScript
```js
/* No JavaScript — paired events share an explicit grid-row across the 1fr/56px/1fr spine; the mobile collapse regenerates side labels from attr(data-side) so meaning survives the reorder. */
```
