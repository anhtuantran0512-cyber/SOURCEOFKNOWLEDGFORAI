---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/film-strip-portfolio/"
title: "Flight Itinerary Timeline — Segments, Layover and Timezone Footnotes"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "The booking-confirmation pattern: flight legs as airport-code pairs joined by a dotted route with a plane glyph riding it, duration bars proportional to real…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Flight Itinerary Timeline — Segments, Layover and Timezone Footnotes
Source: https://codefronts.com/layouts/css-timelines/film-strip-portfolio/

The booking-confirmation pattern: flight legs as airport-code pairs joined by a dotted route with a plane glyph riding it, duration bars proportional to real flight time, and the layover rendered as an honest dashed gap with a 'short connection' warning chip — the domain where a timeline's geometry genuinely helps people not miss planes.
## HTML
```html
<section class="tls-31" aria-label="Flight itinerary timeline demo">
  <div class="tls-31__card">
    <header class="tls-31__head">
      <h3 class="tls-31__title">SFO → Rome</h3>
      <p class="tls-31__meta"><time datetime="2026-09-12">Fri, Sep 12 2026</time> · 1 stop · 14h 20m total</p>
    </header>
    <ol class="tls-31__legs" role="list">
      <li class="tls-31__leg" style="--dur:470">
        <div class="tls-31__ap"><b>SFO</b><span>San Francisco</span><time datetime="2026-09-12T14:10-07:00">14:10</time></div>
        <div class="tls-31__route"><span class="tls-31__plane" aria-hidden="true">▸</span><span class="tls-31__dur">7h 50m · VA 204</span></div>
        <div class="tls-31__ap tls-31__ap--arr"><b>JFK</b><span>New York</span><time datetime="2026-09-12T22:00-04:00">22:00</time></div>
      </li>
      <li class="tls-31__stop" data-tight="true">
        <span class="tls-31__stopline" aria-hidden="true"></span>
        <p class="tls-31__stopchip">⏱ 55 min connection — short<span class="tls-31__sr">, tight connection warning</span></p>
        <span class="tls-31__stopline" aria-hidden="true"></span>
      </li>
      <li class="tls-31__leg" style="--dur:335">
        <div class="tls-31__ap"><b>JFK</b><span>New York</span><time datetime="2026-09-12T22:55-04:00">22:55</time></div>
        <div class="tls-31__route"><span class="tls-31__plane" aria-hidden="true">▸</span><span class="tls-31__dur">8h 20m · VA 88</span></div>
        <div class="tls-31__ap tls-31__ap--arr"><b>FCO</b><span>Rome</span><time datetime="2026-09-13T13:15+02:00">13:15<sup>+1</sup></time></div>
      </li>
    </ol>
    <footer class="tls-31__foot"><p><sup>+1</sup> Arrives the next calendar day. All times local.</p></footer>
  </div>
</section>
```
## CSS
```css
.tls-31,
.tls-31 *,
.tls-31 *::before,
.tls-31 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-31 {
  min-height: 100vh;
  width: 100%;
  --tl-accent: #1d4ed8;
  --tl-line: #e2e8f0;
  --tl-ink: #0f172a;
  --tl-mut: #64748b;
  --tl-warn: #b45309;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f1f5f9;
  padding: 64px 24px;
  display: grid;
  place-items: center;
}

.tls-31__card {
  width: min(600px,100%);
  background: #fff;
  border: 1px solid var(--tl-line);
  border-radius: 18px;
  padding: 26px 28px;
  box-shadow: 0 12px 36px -24px rgb(15 23 42 / .35);
}

.tls-31__head {
  padding-bottom: 18px;
  border-bottom: 1px solid var(--tl-line);
  margin-bottom: 20px;
}

.tls-31__title {
  font-size: clamp(20px,3.5vw,25px);
  font-weight: 800;
  color: var(--tl-ink);
  letter-spacing: -.02em;
}

.tls-31__meta {
  font-size: 12.5px;
  color: var(--tl-mut);
  margin-top: 4px;
}

.tls-31__legs {
  list-style: none;
  display: flex;
  flex-direction: column;
}

.tls-31__leg {
  display: flex;
  align-items: center;
  gap: 16px;
}

.tls-31__ap {
  flex: none;
  width: 96px;
  display: grid;
  gap: 1px;
}

.tls-31__ap--arr {
  text-align: right;
}

.tls-31__ap b {
  font-size: 22px;
  font-weight: 800;
  color: var(--tl-ink);
  letter-spacing: .02em;
}

.tls-31__ap span {
  font-size: 11px;
  color: var(--tl-mut);
}

.tls-31__ap time {
  font-size: 13.5px;
  font-weight: 700;
  color: var(--tl-accent);
  font-variant-numeric: tabular-nums;
}

.tls-31__ap sup {
  font-size: 9px;
  color: var(--tl-warn);
  font-weight: 800;
}

.tls-31__route {
  position: relative;
  flex-grow: var(--dur,300);
  border-top: 2px dotted #b6c4d8;
  margin-top: 4px;
  min-width: 80px;
}

.tls-31__plane {
  position: absolute;
  top: -11px;
  left: 50%;
  translate: -50% 0;
  color: var(--tl-accent);
  font-size: 14px;
  background: #fff;
  padding-inline: 5px;
}

.tls-31__dur {
  position: absolute;
  top: 8px;
  left: 50%;
  translate: -50% 0;
  font-size: 10.5px;
  font-weight: 600;
  color: var(--tl-mut);
  white-space: nowrap;
}

.tls-31__stop {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 18px 0 18px 40px;
  gap: 6px;
}

.tls-31__stopline {
  width: 2px;
  height: 16px;
  background: repeating-linear-gradient(180deg,#b6c4d8 0 4px,transparent 4px 8px);
}

.tls-31__stopchip {
  font-size: 11.5px;
  font-weight: 700;
  color: var(--tl-mut);
  background: #f8fafc;
  border: 1px solid var(--tl-line);
  border-radius: 999px;
  padding: 5px 12px;
}

.tls-31__stop[data-tight="true"] .tls-31__stopchip {
  color: var(--tl-warn);
  background: #fffbeb;
  border-color: #fde68a;
}

.tls-31__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.tls-31__foot {
  margin-top: 20px;
  padding-top: 14px;
  border-top: 1px solid var(--tl-line);
}

.tls-31__foot p {
  font-size: 11px;
  color: var(--tl-mut);
}

.tls-31__foot sup {
  color: var(--tl-warn);
  font-weight: 800;
}

@media (max-width: 520px) {
  .tls-31__leg {
    flex-direction: column;
    align-items: stretch;
    gap: 6px;
  }

  .tls-31__ap,
    .tls-31__ap--arr {
    width: auto;
    text-align: left;
    display: flex;
    align-items: baseline;
    gap: 10px;
  }

  .tls-31__route {
    min-height: 34px;
    flex-grow: 0;
  }

  .tls-31__stop {
    padding-left: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — route widths grow proportionally to flight minutes via flex-grow:var(--dur); the layover is a first-class list item whose data-tight attribute flips the warning chip. */
```
