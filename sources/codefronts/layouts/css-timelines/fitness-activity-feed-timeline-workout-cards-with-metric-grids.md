---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/fitness-activity-feed-timeline-workout-cards-with-metric-grids/"
title: "Fitness Activity Feed Timeline — Workout Cards with Metric Grids"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "A Strava-flavored vertical feed: day-grouped workout cards with CSS-drawn activity glyphs, tabular metric rows (distance · pace · time), a personal-record…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fitness Activity Feed Timeline — Workout Cards with Metric Grids
Source: https://codefronts.com/layouts/css-timelines/fitness-activity-feed-timeline-workout-cards-with-metric-grids/

A Strava-flavored vertical feed: day-grouped workout cards with CSS-drawn activity glyphs, tabular metric rows (distance · pace · time), a personal-record flare, and effort bars — the mobile-first card timeline pattern that fits health apps, habit trackers and any per-day activity log.
## HTML
```html
<section class="tls-05" aria-label="Fitness activity timeline demo">
  <div class="tls-05__phone">
    <header class="tls-05__top"><p class="tls-05__title">Activity</p><p class="tls-05__week">Week 29 · 42.3 km</p></header>
    <div class="tls-05__feed" tabindex="0">
      <p class="tls-05__day">Today · <time datetime="2026-07-18">Jul 18</time></p>
      <article class="tls-05__card" style="--c:#fc5200;--e:.85">
        <span class="tls-05__tile" aria-hidden="true">Ru</span>
        <div class="tls-05__body">
          <p class="tls-05__name">Morning Run <span class="tls-05__pr">PR</span></p>
          <dl class="tls-05__mx"><div><dt>Distance</dt><dd>12.48 km</dd></div><div><dt>Pace</dt><dd>4:52 /km</dd></div><div><dt>Time</dt><dd>1:00:44</dd></div></dl>
          <div class="tls-05__effort" aria-hidden="true"><span class="tls-05__ebar"></span></div><span class="tls-05__sr">Effort 8.5 out of 10</span>
        </div>
      </article>
      <article class="tls-05__card" style="--c:#7c3aed;--e:.4">
        <span class="tls-05__tile" aria-hidden="true">Yo</span>
        <div class="tls-05__body">
          <p class="tls-05__name">Evening Yoga</p>
          <dl class="tls-05__mx"><div><dt>Duration</dt><dd>35:00</dd></div><div><dt>Focus</dt><dd>Mobility</dd></div><div><dt>Cal</dt><dd>124</dd></div></dl>
          <div class="tls-05__effort" aria-hidden="true"><span class="tls-05__ebar"></span></div><span class="tls-05__sr">Effort 4 out of 10</span>
        </div>
      </article>
      <p class="tls-05__day">Yesterday · <time datetime="2026-07-17">Jul 17</time></p>
      <article class="tls-05__card" style="--c:#0ea5e9;--e:.7">
        <span class="tls-05__tile" aria-hidden="true">Cy</span>
        <div class="tls-05__body">
          <p class="tls-05__name">Gravel Loop</p>
          <dl class="tls-05__mx"><div><dt>Distance</dt><dd>29.80 km</dd></div><div><dt>Speed</dt><dd>24.1 km/h</dd></div><div><dt>Time</dt><dd>1:14:09</dd></div></dl>
          <div class="tls-05__effort" aria-hidden="true"><span class="tls-05__ebar"></span></div><span class="tls-05__sr">Effort 7 out of 10</span>
        </div>
      </article>
      <article class="tls-05__card" style="--c:#059669;--e:.3">
        <span class="tls-05__tile" aria-hidden="true">Wa</span>
        <div class="tls-05__body">
          <p class="tls-05__name">Lunch Walk</p>
          <dl class="tls-05__mx"><div><dt>Distance</dt><dd>3.12 km</dd></div><div><dt>Pace</dt><dd>11:04 /km</dd></div><div><dt>Time</dt><dd>34:32</dd></div></dl>
          <div class="tls-05__effort" aria-hidden="true"><span class="tls-05__ebar"></span></div><span class="tls-05__sr">Effort 3 out of 10</span>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.tls-05,
.tls-05 *,
.tls-05 *::before,
.tls-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-05 {
  min-height: 100vh;
  width: 100%;
  --tl-line: #ebe7e2;
  --tl-ink: #241f1a;
  --tl-mut: #8a8178;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f7f4f0;
  padding: 56px 24px;
  display: grid;
  place-items: center;
}

.tls-05__phone {
  width: min(400px,100%);
  background: #fffdfb;
  border: 1px solid var(--tl-line);
  border-radius: 22px;
  overflow: hidden;
  box-shadow: 0 8px 30px -18px rgba(60,40,20,.25);
}

.tls-05__top {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  padding: 18px 20px 12px;
}

.tls-05__title {
  font-size: 19px;
  font-weight: 800;
  color: var(--tl-ink);
  letter-spacing: -.02em;
}

.tls-05__week {
  font-size: 12px;
  font-weight: 600;
  color: var(--tl-mut);
}

.tls-05__feed {
  max-height: 420px;
  overflow-y: auto;
  padding: 0 14px 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.tls-05__day {
  position: sticky;
  top: 0;
  z-index: 2;
  background: #fffdfb;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--tl-mut);
  padding: 10px 6px 6px;
}

.tls-05__card {
  display: flex;
  gap: 12px;
  background: #fff;
  border: 1px solid var(--tl-line);
  border-radius: 14px;
  padding: 14px;
  transition: border-color .15s,transform .15s;
}

.tls-05__card:hover {
  border-color: var(--c);
  transform: translateY(-1px);
}

.tls-05__tile {
  flex: none;
  width: 40px;
  height: 40px;
  border-radius: 12px;
  display: grid;
  place-items: center;
  font-size: 13px;
  font-weight: 800;
  color: #fff;
  background: var(--c);
}

.tls-05__body {
  flex: 1;
  min-width: 0;
}

.tls-05__name {
  font-size: 14.5px;
  font-weight: 700;
  color: var(--tl-ink);
}

.tls-05__pr {
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: .08em;
  color: #b45309;
  background: #fef3c7;
  border-radius: 5px;
  padding: 2px 6px;
  margin-left: 6px;
  vertical-align: 2px;
  position: relative;
}

.tls-05__mx {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 8px;
  margin-top: 9px;
}

.tls-05__mx dt {
  font-size: 10px;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--tl-mut);
}

.tls-05__mx dd {
  font-size: 13.5px;
  font-weight: 700;
  color: var(--tl-ink);
  font-variant-numeric: tabular-nums;
  margin-top: 1px;
}

.tls-05__effort {
  height: 4px;
  border-radius: 2px;
  background: #f1ede8;
  margin-top: 10px;
  overflow: hidden;
}

.tls-05__ebar {
  display: block;
  height: 100%;
  border-radius: 2px;
  background: var(--c);
  transform-origin: left;
  transform: scaleX(var(--e,0));
}

.tls-05__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.tls-05__feed:focus-visible {
  outline: 2px solid #fc5200;
  outline-offset: -2px;
}
```

## JavaScript
```js
/* No JavaScript — day headers pin with position:sticky inside the feed's own scroll; effort bars scale from an inline --e token with hidden text equivalents. */
```
