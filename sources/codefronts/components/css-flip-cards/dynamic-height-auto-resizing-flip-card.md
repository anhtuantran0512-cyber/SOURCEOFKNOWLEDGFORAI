---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/dynamic-height-auto-resizing-flip-card/"
title: "Dynamic Height Auto-Resizing Flip Card"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "A card that adapts its height fluidly to varying content lengths on the front versus the back — no explicit pixel heights, no JavaScript."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dynamic Height Auto-Resizing Flip Card
Source: https://codefronts.com/components/css-flip-cards/dynamic-height-auto-resizing-flip-card/

A card that adapts its height fluidly to varying content lengths on the front versus the back — no explicit pixel heights, no JavaScript.
## HTML
```html
<div class="fc-17">
  <div class="fc-17__heading">
    <h2>Dynamic-Height Auto-Resizing Flip Card</h2>
    <p>No fixed heights — adapts to any content length on front or back</p>
    <p style="margin-top:6px"><code>display:grid</code> + opacity/rotateY cross-fade</p>
  </div>
  <div class="fc-17__cards-row">
    <!-- Card A: short front, long back -->
    <div class="fc-17__card-wrap">
      <div class="fc-17__face fc-17__face--front">
        <div class="fc-17__f-label">Dynamic Card A</div>
        <div class="fc-17__f-title">Short Front</div>
        <div class="fc-17__f-teaser">This front face has minimal content. The back has much more.</div>
        <div class="fc-17__f-hint">Hover to expand →</div>
      </div>
      <div class="fc-17__face fc-17__face--back">
        <div class="fc-17__b-label">Full Detail · Back</div>
        <div class="fc-17__b-title">Extended Back Content</div>
        <div class="fc-17__b-body">The grid technique means this back face can contain as much content as needed and the card height will adapt automatically — no hardcoded pixel heights required.</div>
        <div class="fc-17__b-list">
          <div class="fc-17__b-item"><span class="fc-17__b-dot"></span>Both faces sit in the same CSS grid cell (1/1)</div>
          <div class="fc-17__b-item"><span class="fc-17__b-dot"></span>Opacity + rotateY creates the cross-fade flip</div>
          <div class="fc-17__b-item"><span class="fc-17__b-dot"></span>The tallest face dictates the wrapper height</div>
          <div class="fc-17__b-item"><span class="fc-17__b-dot"></span>No JavaScript needed — pure CSS grid trick</div>
        </div>
      </div>
    </div>
    <!-- Card B: long front, short back -->
    <div class="fc-17__card-wrap">
      <div class="fc-17__face fc-17__face--front">
        <div class="fc-17__f-label">Dynamic Card B</div>
        <div class="fc-17__f-title">Longer Front Content</div>
        <div class="fc-17__f-teaser">This card has a lot more text on the front — multiple paragraphs, a list of items, and a closing note — and still no height is specified anywhere in the CSS.</div>
        <div class="fc-17__b-list" style="margin-top:12px">
          <div class="fc-17__b-item"><span class="fc-17__b-dot" style="background:#f472b6"></span>Point one with some detail</div>
          <div class="fc-17__b-item"><span class="fc-17__b-dot" style="background:#f472b6"></span>Point two with some detail</div>
          <div class="fc-17__b-item"><span class="fc-17__b-dot" style="background:#f472b6"></span>Point three with some detail</div>
        </div>
        <div class="fc-17__f-hint">Hover for brief summary →</div>
      </div>
      <div class="fc-17__face fc-17__face--back">
        <div class="fc-17__b-label">TL;DR · Back</div>
        <div class="fc-17__b-title">Short Summary</div>
        <div class="fc-17__b-body">The grid stacking approach lets each face own its natural height. No JS. No fixed pixels.</div>
      </div>
    </div>
  </div>
  <div class="fc-17__note">
    Technique: both <code>.front</code> and <code>.back</code> use <code>grid-area: 1/1</code> so they overlap in the same grid cell. The tallest visible face sets the wrapper height. On hover, opacity fades to 0 while <code>rotateY(±90deg)</code> adds depth — a CSS-only auto-height flip card.
  </div>
</div>
```
## CSS
```css
.fc-17,
.fc-17 *,
.fc-17 *::before,
.fc-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-17 ::selection {
  background: #8b5cf6;
  color: #fff;
}

.fc-17 {
  --bg: #08060e;
  --violet: #8b5cf6;
  --purple: #a855f7;
  --white: #faf5ff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 50% 30%,#0f0820,#08060e 65%);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 24px;
  color: var(--white);
}

.fc-17__heading {
  text-align: center;
}

.fc-17__heading h2 {
  font-size: 16px;
  font-weight: 700;
  color: var(--white);
}

.fc-17__heading p {
  font-size: 11px;
  color: rgba(250,245,255,.4);
  margin-top: 4px;
}

.fc-17__heading code {
  background: rgba(139,92,246,.15);
  border: 1px solid rgba(139,92,246,.25);
  color: var(--violet);
  padding: 1px 6px;
  border-radius: 4px;
  font-size: 11px;
}
/* The key technique: grid with 1 column so both faces stack,
   only the visible one takes up height */

.fc-17__cards-row {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  justify-content: center;
}

.fc-17__card-wrap {
  width: 280px;
  /* The magic: a grid container where both faces overlap in the same cell */
  display: grid;
  grid-template-rows: 1fr;
}
/* hover trigger on wrapper */

.fc-17__card-wrap:hover .fc-17__face--front {
  opacity: 0;
  transform: rotateY(90deg);
}

.fc-17__card-wrap:hover .fc-17__face--back {
  opacity: 1;
  transform: rotateY(0deg);
}

.fc-17__face--front,
.fc-17__face--back {
  /* overlap in same grid row */
  grid-area: 1/1;
  border-radius: 16px;
  transition: opacity .35s ease, transform .5s cubic-bezier(.4,0,.2,1);
  overflow: hidden;
}

.fc-17__face--front {
  background: linear-gradient(145deg,#130e28,#0a0718);
  border: 1px solid rgba(139,92,246,.2);
  padding: 24px;
  opacity: 1;
  transform: rotateY(0deg);
}

.fc-17__face--back {
  background: linear-gradient(145deg,#0e1a28,#080f18);
  border: 1px solid rgba(56,189,248,.2);
  padding: 24px;
  opacity: 0;
  transform: rotateY(-90deg);
  /* back starts hidden — no explicit height needed */
}
/* FRONT content — short */

.fc-17__f-label {
  font-size: 9px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--violet);
  font-weight: 700;
  margin-bottom: 10px;
}

.fc-17__f-title {
  font-size: 18px;
  font-weight: 800;
  color: var(--white);
  margin-bottom: 8px;
}

.fc-17__f-teaser {
  font-size: 13px;
  color: rgba(250,245,255,.5);
  line-height: 1.6;
}

.fc-17__f-hint {
  font-size: 10px;
  color: rgba(250,245,255,.2);
  margin-top: 14px;
  letter-spacing: .08em;
}
/* BACK content — variable, longer */

.fc-17__b-label {
  font-size: 9px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: #38bdf8;
  font-weight: 700;
  margin-bottom: 10px;
}

.fc-17__b-title {
  font-size: 16px;
  font-weight: 800;
  color: var(--white);
  margin-bottom: 10px;
}

.fc-17__b-body {
  font-size: 13px;
  color: rgba(250,245,255,.65);
  line-height: 1.7;
}

.fc-17__b-list {
  margin-top: 10px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.fc-17__b-item {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  font-size: 12px;
  color: rgba(250,245,255,.6);
}

.fc-17__b-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #38bdf8;
  flex-shrink: 0;
  margin-top: 5px;
}
/* card 2 has even more content */

.fc-17__card-wrap:nth-child(2) .fc-17__face--front {
  background: linear-gradient(145deg,#1a0e18,#0f0810);
}

.fc-17__card-wrap:nth-child(2) .fc-17__face--back {
  background: linear-gradient(145deg,#0a1a0e,#060e08);
}

.fc-17__card-wrap:nth-child(2) .fc-17__f-label {
  color: #f472b6;
}

.fc-17__card-wrap:nth-child(2) .fc-17__b-label {
  color: #4ade80;
}

.fc-17__card-wrap:nth-child(2) .fc-17__b-dot {
  background: #4ade80;
}
/* technique note */

.fc-17__note {
  max-width: 580px;
  padding: 16px 20px;
  border-radius: 12px;
  background: rgba(139,92,246,.06);
  border: 1px solid rgba(139,92,246,.15);
  font-size: 12px;
  color: rgba(250,245,255,.5);
  line-height: 1.7;
  text-align: center;
}

.fc-17__note code {
  color: var(--violet);
  background: rgba(139,92,246,.12);
  padding: 0 4px;
  border-radius: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .fc-17__face--front,
    .fc-17__face--back {
    transition: none;
  }
}
```
