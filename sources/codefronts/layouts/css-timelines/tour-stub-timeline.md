---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/tour-stub-timeline/"
title: "Concert Tour Timeline — Ticket Stub Cards with Perforated Edges"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "Every event a ticket: tour dates rendered as stub cards with real punched notches (radial-gradient masks), perforated tear lines, rotated date tabs and a…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Concert Tour Timeline — Ticket Stub Cards with Perforated Edges
Source: https://codefronts.com/layouts/css-timelines/tour-stub-timeline/

Every event a ticket: tour dates rendered as stub cards with real punched notches (radial-gradient masks), perforated tear lines, rotated date tabs and a sold-out stamp — the textured timeline for concert schedules, festival lineups, event series and travel itineraries.
## HTML
```html
<section class="tls-10" aria-label="Tour dates timeline demo">
  <div class="tls-10__wrap">
    <h3 class="tls-10__h">The Static Bloom — North America ’26</h3>
    <ol class="tls-10__list" role="list">
      <li class="tls-10__row">
        <span class="tls-10__node" aria-hidden="true"></span>
        <article class="tls-10__stub">
          <div class="tls-10__tab" aria-hidden="true">JUL</div>
          <div class="tls-10__main">
            <time class="tls-10__date" datetime="2026-07-24">Fri, Jul 24</time>
            <p class="tls-10__venue">Kings Theatre</p>
            <p class="tls-10__city">Brooklyn, NY</p>
          </div>
          <div class="tls-10__tear">
            <span class="tls-10__seat">GA · Doors 7pm</span>
            <span class="tls-10__price">$45</span>
          </div>
        </article>
      </li>
      <li class="tls-10__row">
        <span class="tls-10__node" aria-hidden="true"></span>
        <article class="tls-10__stub" data-status="soldout">
          <div class="tls-10__tab" aria-hidden="true">JUL</div>
          <div class="tls-10__main">
            <time class="tls-10__date" datetime="2026-07-27">Mon, Jul 27</time>
            <p class="tls-10__venue">The Anthem</p>
            <p class="tls-10__city">Washington, DC</p>
            <p class="tls-10__status">Sold out</p>
          </div>
          <div class="tls-10__tear">
            <span class="tls-10__seat">GA · Doors 7pm</span>
            <span class="tls-10__price">$45</span>
          </div>
        </article>
      </li>
      <li class="tls-10__row">
        <span class="tls-10__node" aria-hidden="true"></span>
        <article class="tls-10__stub">
          <div class="tls-10__tab" aria-hidden="true">AUG</div>
          <div class="tls-10__main">
            <time class="tls-10__date" datetime="2026-08-02">Sun, Aug 2</time>
            <p class="tls-10__venue">Thalia Hall</p>
            <p class="tls-10__city">Chicago, IL</p>
          </div>
          <div class="tls-10__tear">
            <span class="tls-10__seat">Balcony · Doors 6:30pm</span>
            <span class="tls-10__price">$52</span>
          </div>
        </article>
      </li>
    </ol>
  </div>
</section>
```
## CSS
```css
.tls-10,
.tls-10 *,
.tls-10 *::before,
.tls-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-10 {
  min-height: 100vh;
  width: 100%;
  --tl-paper: #fff8ec;
  --tl-accent: #b91c1c;
  --tl-ink: #292018;
  --tl-mut: #95866f;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #1c1917 radial-gradient(1200px 400px at 50% -10%,#33291f,transparent);
  padding: 56px 24px;
  display: grid;
  place-items: center;
}

.tls-10__wrap {
  width: min(560px,100%);
}

.tls-10__h {
  font-family: Georgia,serif;
  font-size: clamp(20px,3.4vw,27px);
  font-weight: 700;
  color: #f5efe4;
  letter-spacing: -.01em;
  margin-bottom: 26px;
}

.tls-10__list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.tls-10__row {
  position: relative;
  padding-left: 34px;
}

.tls-10__row::before {
  content: '';
  position: absolute;
  left: 8px;
  top: -10px;
  bottom: -10px;
  width: 2px;
  background: repeating-linear-gradient(180deg,#57493a 0 6px,transparent 6px 12px);
}

.tls-10__row:first-child::before {
  top: 26px;
}

.tls-10__row:last-child::before {
  bottom: calc(100% - 26px);
}

.tls-10__node {
  position: absolute;
  left: 3.5px;
  top: 22px;
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: var(--tl-accent);
  box-shadow: 0 0 0 4px #1c1917;
}

.tls-10__stub {
  display: flex;
  align-items: stretch;
  background: var(--tl-paper);
  border-radius: 10px;
  overflow: hidden;
  transition: transform .18s,box-shadow .18s;
  -webkit-mask: radial-gradient(9px at left 71%,transparent 97%,#000) left / 51% 100% no-repeat,radial-gradient(9px at right 71%,transparent 97%,#000) right / 51% 100% no-repeat;
  mask: radial-gradient(9px at left 71%,transparent 97%,#000) left / 51% 100% no-repeat,radial-gradient(9px at right 71%,transparent 97%,#000) right / 51% 100% no-repeat;
}

.tls-10__stub:hover {
  transform: translateY(-3px) rotate(-.4deg);
}

.tls-10__tab {
  flex: none;
  width: 38px;
  display: grid;
  place-items: center;
  writing-mode: vertical-rl;
  rotate: 180deg;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .3em;
  color: var(--tl-paper);
  background: var(--tl-accent);
}

.tls-10__main {
  flex: 1;
  padding: 14px 18px;
  position: relative;
}

.tls-10__date {
  display: block;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--tl-accent);
}

.tls-10__venue {
  font-family: Georgia,serif;
  font-size: 19px;
  font-weight: 700;
  color: var(--tl-ink);
  margin-top: 3px;
}

.tls-10__city {
  font-size: 12.5px;
  color: var(--tl-mut);
  margin-top: 2px;
}

.tls-10__status {
  position: absolute;
  right: 10px;
  top: 12px;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--tl-accent);
  border: 2px solid var(--tl-accent);
  border-radius: 4px;
  padding: 3px 8px;
  rotate: -8deg;
  opacity: .85;
}

.tls-10__stub[data-status="soldout"] .tls-10__main {
  opacity: .75;
}

.tls-10__stub[data-status="soldout"] {
  filter: saturate(.55);
}

.tls-10__tear {
  flex: none;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 4px;
  padding: 12px 16px;
  border-left: 2px dashed #d9c9a8;
  text-align: right;
}

.tls-10__seat {
  font-size: 10.5px;
  color: var(--tl-mut);
}

.tls-10__price {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 16px;
  font-weight: 700;
  color: var(--tl-ink);
}

@media (prefers-reduced-motion: reduce) {
  .tls-10__stub {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the punched notches are a two-part radial-gradient mask (works over any page background); perforation is a dashed border; the month tab is writing-mode:vertical-rl. */
```
