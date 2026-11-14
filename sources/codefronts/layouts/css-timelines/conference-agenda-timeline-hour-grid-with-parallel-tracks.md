---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/conference-agenda-timeline-hour-grid-with-parallel-tracks/"
title: "Conference Agenda Timeline — Hour Grid with Parallel Tracks"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "A day-of-event schedule the calendar-app way: an hour ruler down the left, two stage columns across, and every session block sized by its real duration — 30…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Conference Agenda Timeline — Hour Grid with Parallel Tracks
Source: https://codefronts.com/layouts/css-timelines/conference-agenda-timeline-hour-grid-with-parallel-tracks/

A day-of-event schedule the calendar-app way: an hour ruler down the left, two stage columns across, and every session block sized by its real duration — 30 minutes = 1 grid row — so the geometry IS the schedule. Overlaps are impossible to misread, gaps are honest, and a lunch block spans both tracks with one declaration.
## HTML
```html
<section class="tls-08" aria-label="Conference agenda timeline demo">
  <div class="tls-08__inner">
    <header class="tls-08__head"><h3 class="tls-08__title">DevConf — Day 1</h3><p class="tls-08__date"><time datetime="2026-09-12">Sept 12, 2026</time></p></header>
    <div class="tls-08__tracks" aria-hidden="true"><span></span><p style="--t:#4f46e5">Main stage</p><p style="--t:#0f766e">Workshop room</p></div>
    <div class="tls-08__grid" style="--now:6">
      <div class="tls-08__nowline" aria-hidden="true"></div>
      <p class="tls-08__hr" style="grid-row:1">9:00</p>
      <p class="tls-08__hr" style="grid-row:3">10:00</p>
      <p class="tls-08__hr" style="grid-row:5">11:00</p>
      <p class="tls-08__hr" style="grid-row:7">12:00</p>
      <p class="tls-08__hr" style="grid-row:9">13:00</p>
      <p class="tls-08__hr" style="grid-row:11">14:00</p>
      <p class="tls-08__hr" style="grid-row:13">15:00</p>
      <article class="tls-08__ses" style="--t:#4f46e5;grid-column:2;grid-row:1/span 2"><time>9:00</time><h4>Opening keynote</h4><p>Main stage · Dana Cruz</p></article>
      <article class="tls-08__ses" style="--t:#0f766e;grid-column:3;grid-row:2/span 3"><time>9:30</time><h4>Hands-on: container queries</h4><p>Workshop room · Sam Idowu</p></article>
      <article class="tls-08__ses" style="--t:#4f46e5;grid-column:2;grid-row:4/span 2"><time>10:30</time><h4>Scroll-driven animations in production</h4><p>Main stage · Petra Váš</p></article>
      <article class="tls-08__ses tls-08__ses--break" style="grid-column:2/-1;grid-row:7/span 2"><time>12:00</time><h4>Lunch</h4><p>Sponsored by Harbourly</p></article>
      <article class="tls-08__ses" style="--t:#4f46e5;grid-column:2;grid-row:9/span 2"><time>13:00</time><h4>The :has() revolution</h4><p>Main stage · Lee Tran</p></article>
      <article class="tls-08__ses" style="--t:#0f766e;grid-column:3;grid-row:9/span 4"><time>13:00</time><h4>Workshop: design tokens at scale</h4><p>Workshop room · Ana Reyes</p></article>
      <article class="tls-08__ses" style="--t:#4f46e5;grid-column:2;grid-row:12/span 2"><time>14:30</time><h4>Closing panel</h4><p>Main stage · All speakers</p></article>
    </div>
  </div>
</section>
```
## CSS
```css
.tls-08,
.tls-08 *,
.tls-08 *::before,
.tls-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-08 {
  min-height: 100vh;
  width: 100%;
  --tl-line: #e4e4e7;
  --tl-ink: #18181b;
  --tl-mut: #71717a;
  --row: 34px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f4f4f5;
  padding: 64px 24px;
  display: grid;
  place-items: center;
}

.tls-08__inner {
  width: min(720px,100%);
}

.tls-08__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 20px;
}

.tls-08__title {
  font-size: clamp(20px,3.5vw,26px);
  font-weight: 800;
  color: var(--tl-ink);
  letter-spacing: -.02em;
}

.tls-08__date {
  font-size: 12.5px;
  color: var(--tl-mut);
}

.tls-08__tracks {
  display: grid;
  grid-template-columns: 64px 1fr 1fr;
  gap: 8px;
  margin-bottom: 10px;
}

.tls-08__tracks p {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--t);
  background: #fff;
  border: 1px solid var(--tl-line);
  border-radius: 8px;
  text-align: center;
  padding: 7px 4px;
}

.tls-08__grid {
  position: relative;
  display: grid;
  grid-template-columns: 64px 1fr 1fr;
  grid-template-rows: repeat(14,var(--row));
  column-gap: 8px;
  background: #fff;
  border: 1px solid var(--tl-line);
  border-radius: 14px;
  padding: 14px;
  background-image: repeating-linear-gradient(180deg,transparent 0,transparent calc(var(--row) - 1px),#f0f0f2 calc(var(--row) - 1px),#f0f0f2 var(--row));
  background-origin: content-box;
  background-clip: content-box;
}

.tls-08__nowline {
  position: absolute;
  left: 78px;
  right: 14px;
  top: calc(14px + var(--now) * var(--row));
  height: 2px;
  background: #dc2626;
  z-index: 2;
  pointer-events: none;
}

.tls-08__nowline::before {
  content: '';
  position: absolute;
  left: -5px;
  top: -4px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #dc2626;
}

.tls-08__hr {
  grid-column: 1;
  font-size: 11px;
  font-weight: 700;
  color: var(--tl-mut);
  font-variant-numeric: tabular-nums;
  padding-top: 2px;
}

.tls-08__ses {
  position: relative;
  z-index: 1;
  background: color-mix(in srgb,var(--t,#71717a) 8%,#fff);
  border: 1px solid color-mix(in srgb,var(--t,#71717a) 30%,#fff);
  border-left: 3px solid var(--t,#71717a);
  border-radius: 8px;
  padding: 7px 10px;
  margin: 1px 0;
  overflow: hidden;
}

.tls-08__ses time {
  font-size: 10px;
  font-weight: 800;
  color: var(--t,#71717a);
  font-variant-numeric: tabular-nums;
}

.tls-08__ses h4 {
  font-size: 12.5px;
  font-weight: 750;
  color: var(--tl-ink);
  line-height: 1.25;
  letter-spacing: -.01em;
  margin: 2px 0;
}

.tls-08__ses p {
  font-size: 10.5px;
  color: var(--tl-mut);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.tls-08__ses--break {
  background: #fafafa;
  border: 1px dashed var(--tl-line);
  border-left: 1px dashed var(--tl-line);
  text-align: center;
}

.tls-08__ses--break time {
  color: var(--tl-mut);
}

@media (max-width: 560px) {
  .tls-08__tracks {
    display: none;
  }

  .tls-08__grid {
    grid-template-columns: 1fr;
    grid-template-rows: none;
    background-image: none;
  }

  .tls-08__nowline,
    .tls-08__hr {
    display: none;
  }

  .tls-08__ses {
    grid-column: 1!important;
    grid-row: auto!important;
    margin: 3px 0;
  }

  .tls-08__ses p {
    white-space: normal;
  }
}
```

## JavaScript
```js
/* No JavaScript — sessions are grid-row: start / span slots (30min = 1 row); the slot ruling is a repeating gradient locked to the same row unit; the now-line is one --now custom property. */
```
