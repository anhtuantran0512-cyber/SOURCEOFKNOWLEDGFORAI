---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/stacked-cards/"
title: "Stacked Cards Deck Accordion — Overlapping Pull-Out Hand"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "Items rest as a fanned deck — each card overlapping the one above by half, peeking just its header edge like held playing cards."
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stacked Cards Deck Accordion — Overlapping Pull-Out Hand
Source: https://codefronts.com/navigation/css-accordions/stacked-cards/

Items rest as a fanned deck — each card overlapping the one above by half, peeking just its header edge like held playing cards. Selecting a card pulls it out of the stack: it slides down clear of the fan, flattens straight and opens, while the deck closes ranks above it. Spatial, tactile, and unlike any list-shaped accordion.
## HTML
```html
<section class="acc-30" aria-label="Stacked cards deck accordion demo">
  <div class="acc-30__wrap">
    <h3 class="acc-30__title">Case files</h3>
    <details class="acc-30__card" name="acc-30-deck" style="--i:0;--paper:#fdf6e3" open>
      <summary class="acc-30__tab">The Meridian Hotel rebrand<span class="acc-30__year">2026</span></summary>
      <div class="acc-30__page"><p>A 1920s grand hotel with a 2020s booking problem. We rebuilt the identity from the original brass signage letterforms — then let the website whisper instead of shout. Direct bookings up 61%.</p></div>
    </details>
    <details class="acc-30__card" name="acc-30-deck" style="--i:1;--paper:#f3f7ee">
      <summary class="acc-30__tab">Verdant — seed to shelf traceability<span class="acc-30__year">2025</span></summary>
      <div class="acc-30__page"><p>Every bag of coffee gets a passport. We designed the scan-to-story flow and the farmer-first data model behind it — 4 million scans in year one.</p></div>
    </details>
    <details class="acc-30__card" name="acc-30-deck" style="--i:2;--paper:#f0f4fa">
      <summary class="acc-30__tab">Nordfjord ferries wayfinding<span class="acc-30__year">2025</span></summary>
      <div class="acc-30__page"><p>Eleven terminals, four languages, one typographic system readable through rain at 40 knots. The pictograms are now the regional standard.</p></div>
    </details>
    <details class="acc-30__card" name="acc-30-deck" style="--i:3;--paper:#faf0f2">
      <summary class="acc-30__tab">Archive of the Common Loon<span class="acc-30__year">2024</span></summary>
      <div class="acc-30__page"><p>A sound archive as a public artwork: 40 years of lake recordings, one endless generative stream, and a listening cabin on the shore.</p></div>
    </details>
  </div>
</section>
```
## CSS
```css
.acc-30,
.acc-30 *,
.acc-30 *::before,
.acc-30 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-30 {
  --ink: #26221c;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #e7e2d8;
  padding: 44px 24px;
}

.acc-30__wrap {
  width: min(540px,100%);
}

.acc-30__title {
  font-size: 25px;
  font-weight: 800;
  color: var(--ink);
  letter-spacing: -.02em;
  margin-bottom: 26px;
}

.acc-30__card {
  position: relative;
  background: var(--paper);
  border: 1.5px solid rgba(60,50,30,.25);
  border-radius: 10px;
  box-shadow: 0 2px 6px -2px rgba(50,40,20,.25);
  rotate: calc((var(--i) - 1.5) * .9deg);
  z-index: calc(var(--i) + 1);
  transition: margin .45s cubic-bezier(.4,0,.2,1),rotate .45s cubic-bezier(.4,0,.2,1),box-shadow .45s;
}

.acc-30__card + .acc-30__card {
  margin-top: -44px;
}

.acc-30__card:hover {
  rotate: 0deg;
}

.acc-30__card[open] {
  rotate: 0deg;
  box-shadow: 0 24px 50px -22px rgba(50,40,20,.55);
  z-index: 10;
}

.acc-30__card[open] + .acc-30__card {
  margin-top: 18px;
}

.acc-30__card + .acc-30__card[open] {
  margin-top: 18px;
}

.acc-30__tab {
  list-style: none;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  min-height: 56px;
  padding: 8px 20px;
  font-size: 15.5px;
  font-weight: 700;
  color: var(--ink);
  cursor: pointer;
}

.acc-30__tab::-webkit-details-marker {
  display: none;
}

.acc-30__tab::marker {
  content: "";
}

.acc-30__year {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  font-weight: 600;
  color: #8d8371;
  background: rgba(60,50,30,.08);
  padding: 3px 9px;
  border-radius: 99px;
  flex: none;
}

.acc-30__card[open] .acc-30__year {
  background: var(--ink);
  color: var(--paper);
}

.acc-30__page {
  padding: 2px 20px 22px;
  font-size: 14.5px;
  line-height: 1.7;
  color: #4d4536;
  border-top: 1.5px dashed rgba(60,50,30,.25);
  margin: 0 12px;
  padding-left: 8px;
  padding-right: 8px;
  padding-top: 14px;
}

.acc-30__card[open] .acc-30__page {
  animation: acc-30-in .4s ease-out;
}

@keyframes acc-30-in {
  from {
    opacity: 0;
    translate: 0 -6px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.acc-30__tab:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 3px;
  border-radius: 8px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-30__card {
    transition: none;
    rotate: 0deg;
  }

  .acc-30__card[open] .acc-30__page {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — negative margins fan the cards into a pile with only header strips exposed; details[open] transitions margin, rotation and shadow so the chosen card pulls out flat while the deck closes ranks. */
```
