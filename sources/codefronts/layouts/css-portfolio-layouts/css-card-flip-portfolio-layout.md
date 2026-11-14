---
source: "codefronts"
url: "https://codefronts.com/layouts/css-portfolio-layouts/css-card-flip-portfolio-layout/"
title: "CSS Card Flip Portfolio Layout"
section: "layouts"
category: "css-portfolio-layouts"
category_name: "CSS Portfolio Layouts"
description: "Project cards with two faces: the front is the artwork, and a corner button flips the card 180° in 3D to reveal the tech stack and live/code links on the back."
has_js: "true"
---

Here's a working CSS Portfolio Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Card Flip Portfolio Layout
Source: https://codefronts.com/layouts/css-portfolio-layouts/css-card-flip-portfolio-layout/

Project cards with two faces: the front is the artwork, and a corner button flips the card 180° in 3D to reveal the tech stack and live/code links on the back. The rotation is the classic perspective + preserve-3d + backface-visibility trio, but built the accessible way — a real button drives the flip (not a hover you can't perform on touch), links on the hidden face are inert until it's showing, and reduced-motion swaps the spin for a crossfade.
## HTML
```html
<section class="cpl-14" aria-label="Card flip portfolio demo">
  <div class="cpl-14__stage">
    <header class="cpl-14__head">
      <h2>Builds</h2>
      <p>Flip a card for the stack &amp; links</p>
    </header>
    <div class="cpl-14__grid">
      <article class="cpl-14__card">
        <div class="cpl-14__inner">
          <div class="cpl-14__face cpl-14__front" style="--img:url('https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=900&auto=format&fit=crop');--a:oklch(0.76 0.12 265);--b:oklch(0.46 0.16 290)">
            <span class="cpl-14__chip">Web app</span>
            <h3>Ledgerline</h3>
            <p>Bookkeeping for one-person studios</p>
          </div>
          <div class="cpl-14__face cpl-14__back">
            <h3>Ledgerline</h3>
            <ul><li>SvelteKit</li><li>PostgreSQL</li><li>Stripe</li><li>Fly.io</li></ul>
            <span class="cpl-14__links"><a href="#ledger-live">Live ↗</a><a href="#ledger-code">Code ↗</a></span>
          </div>
        </div>
        <button class="cpl-14__flip" type="button" aria-pressed="false" aria-label="Show project details"><i aria-hidden="true">⟲</i></button>
      </article>
      <article class="cpl-14__card">
        <div class="cpl-14__inner">
          <div class="cpl-14__face cpl-14__front" style="--img:url('https://images.unsplash.com/photo-1461749280684-dccba630e2f6?q=80&w=900&auto=format&fit=crop');--a:oklch(0.82 0.1 60);--b:oklch(0.54 0.15 35)">
            <span class="cpl-14__chip">CLI</span>
            <h3>packlight</h3>
            <p>Bundle-size budgets in CI</p>
          </div>
          <div class="cpl-14__face cpl-14__back">
            <h3>packlight</h3>
            <ul><li>Rust</li><li>GitHub Actions</li><li>WASM</li></ul>
            <span class="cpl-14__links"><a href="#pack-live">Docs ↗</a><a href="#pack-code">Code ↗</a></span>
          </div>
        </div>
        <button class="cpl-14__flip" type="button" aria-pressed="false" aria-label="Show project details"><i aria-hidden="true">⟲</i></button>
      </article>
      <article class="cpl-14__card">
        <div class="cpl-14__inner">
          <div class="cpl-14__face cpl-14__front" style="--img:url('https://images.unsplash.com/photo-1502680390469-be75c86b636f?q=80&w=900&auto=format&fit=crop');--a:oklch(0.78 0.11 165);--b:oklch(0.48 0.13 195)">
            <span class="cpl-14__chip">Mobile</span>
            <h3>Tidepool</h3>
            <p>Surf forecasts without the noise</p>
          </div>
          <div class="cpl-14__face cpl-14__back">
            <h3>Tidepool</h3>
            <ul><li>React Native</li><li>NOAA API</li><li>SQLite</li></ul>
            <span class="cpl-14__links"><a href="#tide-live">App Store ↗</a><a href="#tide-code">Code ↗</a></span>
          </div>
        </div>
        <button class="cpl-14__flip" type="button" aria-pressed="false" aria-label="Show project details"><i aria-hidden="true">⟲</i></button>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.cpl-14,
.cpl-14 *,
.cpl-14 *::before,
.cpl-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpl-14 {
  --bg: oklch(0.2 0.02 280);
  --card: oklch(0.26 0.02 280);
  --ink: oklch(0.95 0.006 90);
  --mut: oklch(0.66 0.015 280);
  --line: oklch(0.33 0.02 280);
  --acc: oklch(0.78 0.14 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cpl-14__stage {
  width: 100%;
  background: var(--bg);
  padding: clamp(18px,4cqi,28px);
  min-height: 100vh;
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.cpl-14__head {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 14px;
  margin-bottom: 18px;
}

.cpl-14__head h2 {
  font-size: 24px;
  letter-spacing: -.02em;
}

.cpl-14__head p {
  font-size: 12.5px;
  color: var(--mut);
}

.cpl-14__grid {
  display: grid;
  gap: 16px;
  grid-template-columns: repeat(auto-fit,minmax(min(215px,100%),1fr));
}

.cpl-14__card {
  position: relative;
  perspective: 1200px;
}

.cpl-14__inner {
  display: grid;
  transform-style: preserve-3d;
  transition: transform .7s cubic-bezier(.4,0,.2,1);
}

.cpl-14__card.is-flipped .cpl-14__inner {
  transform: rotateY(180deg);
}

.cpl-14__face {
  grid-area: 1/1;
  min-height: min(300px,34vh);
  border-radius: 16px;
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

.cpl-14__front {
  justify-content: flex-end;
  background-image: var(--img,none),linear-gradient(150deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
  color: oklch(0.98 0.005 90);
}

.cpl-14__chip {
  align-self: start;
  margin-bottom: auto;
  padding: 4px 10px;
  border-radius: 99px;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: .07em;
  text-transform: uppercase;
  background: oklch(1 0 0/.2);
  backdrop-filter: blur(4px);
}

.cpl-14__face h3 {
  font-size: 18px;
  letter-spacing: -.015em;
}

.cpl-14__front p {
  font-size: 12.5px;
  opacity: .85;
}

.cpl-14__back {
  transform: rotateY(180deg);
  background: var(--card);
  border: 1px solid var(--line);
  justify-content: flex-start;
}

.cpl-14__back ul {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 2px;
}

.cpl-14__back li {
  padding: 5px 10px;
  border-radius: 99px;
  font-size: 11px;
  font-weight: 700;
  border: 1px solid var(--line);
  color: var(--mut);
}

.cpl-14__links {
  display: flex;
  gap: 14px;
  margin-top: auto;
}

.cpl-14__links a {
  font-size: 13px;
  font-weight: 700;
  color: var(--acc);
  text-decoration: none;
  padding: 6px 0;
}

.cpl-14__links a:hover,
.cpl-14__links a:focus-visible {
  text-decoration: underline;
  text-underline-offset: 3px;
}

.cpl-14__links a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.cpl-14__flip {
  position: absolute;
  z-index: 2;
  top: 12px;
  right: 12px;
  width: 38px;
  height: 38px;
  border: none;
  border-radius: 50%;
  background: oklch(0.15 0.02 280/.55);
  color: oklch(0.96 0.005 90);
  backdrop-filter: blur(6px);
  cursor: pointer;
  font-size: 15px;
  display: grid;
  place-items: center;
  transition: background .2s,rotate .5s cubic-bezier(.4,0,.2,1),scale .2s;
}

.cpl-14__flip:hover {
  background: oklch(0.15 0.02 280/.8);
  scale: 1.08;
}

.cpl-14__flip:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cpl-14__card.is-flipped .cpl-14__flip {
  rotate: 180deg;
  background: var(--acc);
  color: oklch(0.2 0.02 280);
}

.cpl-14__front {
  position: relative;
}

.cpl-14__front::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: linear-gradient(to top,oklch(0.18 0.02 280/.78),transparent 55%);
}

.cpl-14__front>* {
  position: relative;
  z-index: 1;
}

@media (prefers-reduced-motion: reduce) {
  .cpl-14__inner {
    transform-style: flat;
    transition: none;
  }

  .cpl-14__card.is-flipped .cpl-14__inner {
    transform: none;
  }

  .cpl-14__face {
    transition: opacity .2s;
    transform: none;
  }

  .cpl-14__back {
    opacity: 0;
  }

  .cpl-14__card.is-flipped .cpl-14__back {
    opacity: 1;
  }

  .cpl-14__card.is-flipped .cpl-14__front {
    opacity: 0;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.cpl-14__card').forEach(function (card) {
    if (card.dataset.bound) return; card.dataset.bound = '1';
    var btn = card.querySelector('.cpl-14__flip');
    var front = card.querySelector('.cpl-14__front');
    var back = card.querySelector('.cpl-14__back');
    function sync() {
      var flipped = card.classList.contains('is-flipped');
      btn.setAttribute('aria-pressed', String(flipped));
      btn.setAttribute('aria-label', flipped ? 'Show project cover' : 'Show project details');
      back.toggleAttribute('inert', !flipped);
      front.toggleAttribute('inert', flipped);
    }
    btn.addEventListener('click', function () { card.classList.toggle('is-flipped'); sync(); });
    sync();
  });
})();
```
