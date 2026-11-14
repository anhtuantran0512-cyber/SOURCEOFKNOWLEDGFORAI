---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/nature-trail/"
title: "Nature Trail Timeline — Winding Dashed Path with Waypoint Badges"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "An itinerary that walks: waypoints connected by a winding dashed trail built from alternating border-radius arcs (no SVG path), elevation chips,…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Nature Trail Timeline — Winding Dashed Path with Waypoint Badges
Source: https://codefronts.com/layouts/css-timelines/nature-trail/

An itinerary that walks: waypoints connected by a winding dashed trail built from alternating border-radius arcs (no SVG path), elevation chips, distance-between labels riding the curves, and a trailhead-to-summit narrative — the organic layout for hiking guides, travel itineraries and campus tours.
## HTML
```html
<section class="tls-18" aria-label="Hiking trail timeline demo">
  <div class="tls-18__map">
    <header class="tls-18__head"><h3 class="tls-18__h">Ridgeline Loop · 11.2 km</h3><p class="tls-18__sub">Trailhead to summit, four waypoints</p></header>
    <ol class="tls-18__trail" role="list">
      <li class="tls-18__wp">
        <span class="tls-18__badge" aria-hidden="true"></span>
        <div class="tls-18__card"><p class="tls-18__name">Fern Creek Trailhead</p><p class="tls-18__meta"><span class="tls-18__elev">320 m</span> · <time datetime="2026-07-18T07:30">07:30</time> · parking, water</p></div>
      </li>
      <li class="tls-18__leg" aria-hidden="true">
        <svg class="tls-18__arc" viewBox="0 0 400 110" preserveAspectRatio="none" aria-hidden="true"><path d="M 30 10 C 30 70, 370 40, 370 100" fill="none" stroke="var(--tl-trail)" stroke-width="3" stroke-dasharray="6 8" stroke-linecap="round"/></svg>
        <span class="tls-18__dist">2.8 km · +180 m</span>
      </li>
      <li class="tls-18__wp">
        <span class="tls-18__badge" aria-hidden="true"></span>
        <div class="tls-18__card"><p class="tls-18__name">Mossbridge Crossing</p><p class="tls-18__meta"><span class="tls-18__elev">500 m</span> · <time datetime="2026-07-18T08:40">08:40</time> · last shade before the ridge</p></div>
      </li>
      <li class="tls-18__leg" aria-hidden="true">
        <svg class="tls-18__arc" viewBox="0 0 400 110" preserveAspectRatio="none" aria-hidden="true"><path d="M 370 10 C 370 70, 30 40, 30 100" fill="none" stroke="var(--tl-trail)" stroke-width="3" stroke-dasharray="6 8" stroke-linecap="round"/></svg>
        <span class="tls-18__dist">3.1 km · +420 m</span>
      </li>
      <li class="tls-18__wp">
        <span class="tls-18__badge" aria-hidden="true"></span>
        <div class="tls-18__card"><p class="tls-18__name">Kestrel Saddle</p><p class="tls-18__meta"><span class="tls-18__elev">920 m</span> · <time datetime="2026-07-18T10:35">10:35</time> · exposed — check wind</p></div>
      </li>
      <li class="tls-18__leg" aria-hidden="true">
        <svg class="tls-18__arc" viewBox="0 0 400 110" preserveAspectRatio="none" aria-hidden="true"><path d="M 30 10 C 30 70, 370 40, 370 100" fill="none" stroke="var(--tl-trail)" stroke-width="3" stroke-dasharray="6 8" stroke-linecap="round"/></svg>
        <span class="tls-18__dist">1.4 km · +160 m</span>
      </li>
      <li class="tls-18__wp tls-18__wp--summit">
        <span class="tls-18__badge" aria-hidden="true"></span>
        <div class="tls-18__card"><p class="tls-18__name">Ridgeline Summit</p><p class="tls-18__meta"><span class="tls-18__elev">1,080 m</span> · <time datetime="2026-07-18T11:20">11:20</time> · 360° views, log book</p></div>
      </li>
    </ol>
  </div>
</section>
```
## CSS
```css
.tls-18,
.tls-18 *,
.tls-18 *::before,
.tls-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-18 {
  min-height: 100vh;
  width: 100%;
  --tl-trail: #8a5a2b;
  --tl-ink: #2f3a2a;
  --tl-mut: #7d8a72;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f1f0e4;
  padding: 56px 24px;
  display: grid;
  place-items: center;
}

.tls-18__map {
  width: min(560px,100%);
  background: #f8f7ee radial-gradient(340px 240px at 15% 20%,rgba(138,90,43,.05),transparent),radial-gradient(300px 220px at 85% 70%,rgba(90,110,70,.06),transparent);
  border: 1px solid #e0ddc8;
  border-radius: 18px;
  padding: 28px 30px 34px;
}

.tls-18__head {
  margin-bottom: 20px;
}

.tls-18__h {
  font-family: Georgia,serif;
  font-size: clamp(19px,3vw,24px);
  font-weight: 700;
  color: var(--tl-ink);
}

.tls-18__sub {
  font-size: 12.5px;
  color: var(--tl-mut);
  margin-top: 3px;
}

.tls-18__trail {
  list-style: none;
  counter-reset: tls-wp;
  display: flex;
  flex-direction: column;
}
/* Waypoint rows use :nth-child to alternate left/right layout. WPs sit
   at ol child positions 1, 3, 5, 7. Odd-index WPs (1, 5) stay on the
   LEFT (default). Even-index WPs (3, 7) go on the RIGHT via row-reverse. */

.tls-18__wp {
  counter-increment: tls-wp;
  display: flex;
  align-items: center;
  gap: 14px;
  position: relative;
  z-index: 1;
}

.tls-18__trail>li:nth-child(3),
.tls-18__trail>li:nth-child(7) {
  flex-direction: row-reverse;
  text-align: right;
}

.tls-18__trail>li:nth-child(3) .tls-18__card,
.tls-18__trail>li:nth-child(7) .tls-18__card {
  align-items: flex-end;
}

.tls-18__badge {
  flex: none;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: #fff;
  border: 3px solid var(--tl-trail);
  display: grid;
  place-items: center;
  color: var(--tl-trail);
  font-weight: 800;
  font-size: 13px;
  position: relative;
  z-index: 2;
}

.tls-18__badge::before {
  content: counter(tls-wp);
}

.tls-18__wp--summit .tls-18__badge {
  background: var(--tl-trail);
  color: #f8f7ee;
}

.tls-18__card {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.tls-18__name {
  font-family: Georgia,serif;
  font-size: 16.5px;
  font-weight: 700;
  color: var(--tl-ink);
}

.tls-18__meta {
  font-size: 12px;
  color: var(--tl-mut);
}

.tls-18__elev {
  font-family: ui-monospace,Menlo,monospace;
  font-weight: 700;
  color: var(--tl-trail);
  font-variant-numeric: tabular-nums;
}
/* Legs are SVG-driven diagonal S-curves. Each SVG uses a cubic bezier
   from top-left to bottom-right (or reversed on the middle leg) so the
   dashed path actually connects the waypoint badges at opposite ends of
   the arc — impossible with border-radius alone. preserveAspectRatio:none
   lets the path stretch to fit any container width. The odd-position leg
   goes LEFT→RIGHT, the middle leg (nth-child(4)) goes RIGHT→LEFT. */

.tls-18__leg {
  position: relative;
  height: 88px;
  display: grid;
  place-items: center;
  overflow: visible;
  margin-block: -8px;
}

.tls-18__arc {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.tls-18__dist {
  position: relative;
  z-index: 1;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .06em;
  color: var(--tl-mut);
  background: #f8f7ee;
  border: 1px solid #e0ddc8;
  border-radius: 999px;
  padding: 3px 11px;
}

@media (max-width: 480px) {
  .tls-18__trail>li:nth-child(3),
    .tls-18__trail>li:nth-child(7) {
    flex-direction: row;
    text-align: left;
  }

  .tls-18__trail>li:nth-child(3) .tls-18__card,
    .tls-18__trail>li:nth-child(7) .tls-18__card {
    align-items: flex-start;
  }

  .tls-18__leg {
    height: 44px;
  }

  .tls-18__arc {
    left: calc(17px - 50%);
    right: auto;
    width: 100%;
    transform: none;
  }

  .tls-18__arc path {
    d: path('M 30 0 L 30 110');
  }
}
```

## JavaScript
```js
/* No JavaScript — the winding path is inline SVG cubic-bezier curves that connect waypoint badges diagonally; on narrow screens the arcs collapse to a straight left rail via a media query. */
```
