---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/marquee-header/"
title: "Marquee Header Accordion — Scrolling Ticker Titles on the Open Item"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "The open section's header becomes a ticker: its title duplicates into an infinite marquee scrolling across the row — ART DIRECTION ✦ ART DIRECTION ✦ — while…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Marquee Header Accordion — Scrolling Ticker Titles on the Open Item
Source: https://codefronts.com/navigation/css-accordions/marquee-header/

The open section's header becomes a ticker: its title duplicates into an infinite marquee scrolling across the row — ART DIRECTION ✦ ART DIRECTION ✦ — while closed headers sit still. Loud, fashion-editorial energy for lookbooks, drops and agency reels, with the marquee correctly pausable and motion-safe.
## HTML
```html
<section class="acc-26" aria-label="Marquee header accordion demo">
  <div class="acc-26__wrap">
    <p class="acc-26__kicker">Studio ØRE — Services</p>
    <details class="acc-26__item" open>
      <summary class="acc-26__sum">
        <span class="acc-26__static">Art direction</span>
        <span class="acc-26__marquee" aria-hidden="true"><span class="acc-26__track"><i>Art direction ✦ Art direction ✦ Art direction ✦ </i><i>Art direction ✦ Art direction ✦ Art direction ✦ </i></span></span>
      </summary>
      <div class="acc-26__body"><div><b>What</b><p>Campaign concepts, casting, set design and the shot list that holds it all together.</p></div><div><b>Recent</b><p>SS26 lookbook for Atelier Marin · rebrand film for the Vinter hotel group.</p></div></div>
    </details>
    <details class="acc-26__item">
      <summary class="acc-26__sum">
        <span class="acc-26__static">Editorial design</span>
        <span class="acc-26__marquee" aria-hidden="true"><span class="acc-26__track"><i>Editorial design ✦ Editorial design ✦ </i><i>Editorial design ✦ Editorial design ✦ </i></span></span>
      </summary>
      <div class="acc-26__body"><div><b>What</b><p>Magazines, catalogues and books — grids, type systems, and production through print.</p></div><div><b>Recent</b><p>Issue 9 of Field Notes quarterly · the 340-page Nordisk furniture catalogue.</p></div></div>
    </details>
    <details class="acc-26__item">
      <summary class="acc-26__sum">
        <span class="acc-26__static">Motion &amp; film</span>
        <span class="acc-26__marquee" aria-hidden="true"><span class="acc-26__track"><i>Motion &amp; film ✦ Motion &amp; film ✦ Motion &amp; film ✦ </i><i>Motion &amp; film ✦ Motion &amp; film ✦ Motion &amp; film ✦ </i></span></span>
      </summary>
      <div class="acc-26__body"><div><b>What</b><p>Title sequences, product film and social cuts — boards to color grade.</p></div><div><b>Recent</b><p>Launch film for the Aria headphone line · opening titles for DOCS/CPH.</p></div></div>
    </details>
  </div>
</section>
```
## CSS
```css
.acc-26,
.acc-26 *,
.acc-26 *::before,
.acc-26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-26 {
  --ink: #171512;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #e8e4dc;
  padding: 44px 24px;
}

.acc-26__wrap {
  width: min(640px,100%);
}

.acc-26__kicker {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #8b8272;
  margin-bottom: 14px;
}

.acc-26__item {
  border-top: 2px solid var(--ink);
}

.acc-26__item:last-of-type {
  border-bottom: 2px solid var(--ink);
}

.acc-26__sum {
  list-style: none;
  position: relative;
  display: block;
  min-height: 72px;
  cursor: pointer;
  overflow: hidden;
}

.acc-26__sum::-webkit-details-marker {
  display: none;
}

.acc-26__sum::marker {
  content: "";
}

.acc-26__static,
.acc-26__track i {
  font-size: clamp(26px,4.5vw,38px);
  font-weight: 850;
  letter-spacing: -.01em;
  text-transform: uppercase;
  color: var(--ink);
  line-height: 72px;
  white-space: nowrap;
}

.acc-26__static {
  display: block;
  padding: 0 4px;
  transition: opacity .2s;
}

.acc-26__sum:hover .acc-26__static {
  opacity: .55;
}

.acc-26__item[open] .acc-26__static {
  opacity: 0;
  position: absolute;
  inset: 0;
}

.acc-26__marquee {
  position: absolute;
  inset: 0;
  display: none;
}

.acc-26__item[open] .acc-26__marquee {
  display: block;
}

.acc-26__track {
  display: inline-flex;
  white-space: nowrap;
  animation: acc-26-scroll 14s linear infinite;
}

.acc-26__track i {
  font-style: normal;
}

.acc-26__sum:hover .acc-26__track,
.acc-26__item:focus-within .acc-26__track {
  animation-play-state: paused;
}

@keyframes acc-26-scroll {
  to {
    translate: -50% 0;
  }
}

.acc-26__body {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  padding: 6px 4px 26px;
}

.acc-26__body b {
  display: block;
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #8b8272;
  margin-bottom: 6px;
}

.acc-26__body p {
  font-size: 14.5px;
  line-height: 1.6;
  color: #40392e;
}

.acc-26__item[open] .acc-26__body {
  animation: acc-26-in .4s ease-out;
}

@keyframes acc-26-in {
  from {
    opacity: 0;
    translate: 0 -6px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.acc-26__sum:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 3px;
}

@media (max-width: 520px) {
  .acc-26__body {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .acc-26__track {
    animation: none;
  }

  .acc-26__item[open] .acc-26__marquee {
    display: none;
  }

  .acc-26__item[open] .acc-26__static {
    opacity: 1;
    position: static;
  }
}
```

## JavaScript
```js
/* No JavaScript — the open item's title becomes an exactly-doubled track animating translateX to -50% for a seamless loop; hover/focus pause it and reduced-motion swaps back to the static title. */
```
