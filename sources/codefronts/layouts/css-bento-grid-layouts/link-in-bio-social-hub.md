---
source: "codefronts"
url: "https://codefronts.com/layouts/css-bento-grid-layouts/link-in-bio-social-hub/"
title: "Link-in-Bio Social Hub"
section: "layouts"
category: "css-bento-grid-layouts"
category_name: "CSS Bento Grid Layouts"
description: "A mobile-first, pure-CSS link-in-bio bento grid that mimics iOS home-screen widgets: rounded high-contrast blocks holding a profile avatar, a working…"
has_js: "false"
---

Here's a working CSS Bento Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Link-in-Bio Social Hub
Source: https://codefronts.com/layouts/css-bento-grid-layouts/link-in-bio-social-hub/

A mobile-first, pure-CSS link-in-bio bento grid that mimics iOS home-screen widgets: rounded high-contrast blocks holding a profile avatar, a working dark-mode toggle built with :has() and zero JavaScript, streaming platform links and a mini newsletter signup — the lightweight personal landing page developers search for as a Linktree alternative. Variant B is a loud neon-contrast poster take.
## HTML
```html
<div class="bgl-06-group">
<section class="bgl-06a" aria-labelledby="bgl-06a-h">
  <div class="bgl-06a__hub">
    <div class="bgl-06a__grid">
      <article class="bgl-06a__card bgl-06a__me">
        <img class="bgl-06a__avatar" src="https://picsum.photos/seed/bglbio/200/200" alt="Noa Lindqvist" loading="lazy">
        <h2 id="bgl-06a-h">Noa Lindqvist</h2>
        <p>Producer &amp; DJ &mdash; Stockholm. New EP out now.</p>
      </article>
      <div class="bgl-06a__card bgl-06a__toggle">
        <label class="bgl-06a__switch" for="bgl-06a-mode">
          <input type="checkbox" id="bgl-06a-mode">
          <span class="bgl-06a__knob" aria-hidden="true"></span>
          <span class="bgl-06a__mode">Dark mode</span>
        </label>
      </div>
      <a class="bgl-06a__card bgl-06a__link" href="#" style="--brand:oklch(0.72 0.2 145)"><b>&#9654;</b>Listen on Spotify<em>2.1M monthly</em></a>
      <a class="bgl-06a__card bgl-06a__link" href="#" style="--brand:oklch(0.62 0.23 25)"><b>&#9654;</b>Watch on YouTube<em>New video</em></a>
      <a class="bgl-06a__card bgl-06a__sq" href="#" style="--brand:oklch(0.65 0.19 320)">IG</a>
      <a class="bgl-06a__card bgl-06a__sq" href="#" style="--brand:oklch(0.6 0.17 250)">TT</a>
      <form class="bgl-06a__card bgl-06a__news" action="#" method="post">
        <label for="bgl-06a-email">Monthly mixtape, no spam</label>
        <div class="bgl-06a__row">
          <input id="bgl-06a-email" type="email" name="email" placeholder="[email protected]" required>
          <button type="submit">Join</button>
        </div>
      </form>
    </div>
  </div>
</section>
<section class="bgl-06b" aria-labelledby="bgl-06b-h">
  <div class="bgl-06b__grid">
    <article class="bgl-06b__card bgl-06b__hero" style="--tile:oklch(0.85 0.19 95);--tink:#141406">
      <h2 id="bgl-06b-h">RIO&nbsp;MARS</h2><p>Illustrator on tour &mdash; 12 cities, one sketchbook.</p>
    </article>
    <a class="bgl-06b__card" href="#" style="--tile:oklch(0.66 0.23 25);--tink:#fff">Prints shop<b aria-hidden="true">&rarr;</b></a>
    <a class="bgl-06b__card" href="#" style="--tile:oklch(0.62 0.21 300);--tink:#fff">Commissions<b aria-hidden="true">&rarr;</b></a>
    <a class="bgl-06b__card" href="#" style="--tile:oklch(0.7 0.17 200);--tink:#0a1416">Tour dates<b aria-hidden="true">&rarr;</b></a>
    <a class="bgl-06b__card" href="#" style="--tile:oklch(0.78 0.2 145);--tink:#0b160c">Newsletter<b aria-hidden="true">&rarr;</b></a>
    <a class="bgl-06b__card bgl-06b__wide" href="#" style="--tile:#fff;--tink:#141414">Watch the studio vlog<b aria-hidden="true">&rarr;</b></a>
  </div>
</section>
</div>
```
## CSS
```css
.bgl-06-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.bgl-06-group > section {
  flex: 1 1 480px;
  min-width: 320px;
}

.bgl-06a,
.bgl-06a *,
.bgl-06a *::before,
.bgl-06a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bgl-06a {
  width: 100%;
  min-height: 100vh;
  container-type: inline-size;
  font-family: 'Segoe UI',system-ui,sans-serif;
  padding: 48px 20px;
  background: linear-gradient(160deg,#c7ceda,#aeb6c6);
}

.bgl-06a__hub {
  --bg: rgba(255,255,255,.72);
  --ink: #17181c;
  --sub: rgba(23,24,28,.55);
  --tile: rgba(255,255,255,.85);
  --gap: 12px;
  --radius: 22px;
  max-width: 420px;
  margin: 0 auto;
  transition: background .4s;
}

.bgl-06a__hub:has(input:checked) {
  --bg: rgba(22,23,28,.85);
  --ink: #f4f4f6;
  --sub: rgba(244,244,246,.55);
  --tile: rgba(38,40,48,.9);
}

.bgl-06a__grid {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: var(--gap);
  padding: var(--gap);
  border-radius: calc(var(--radius) + var(--gap));
  background: var(--bg);
  backdrop-filter: blur(14px);
  transition: background .4s;
}

.bgl-06a__card {
  grid-column: span 4;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 6px;
  min-height: 64px;
  padding: 18px;
  border-radius: var(--radius);
  background: var(--tile);
  color: var(--ink);
  transition: background .4s,color .4s,transform .25s;
}

.bgl-06a__me {
  align-items: center;
  text-align: center;
  gap: 8px;
  padding: 26px 18px;
}

.bgl-06a__avatar {
  width: 76px;
  height: 76px;
  border-radius: 50%;
  object-fit: cover;
}

.bgl-06a__me h2 {
  font-size: 21px;
  font-weight: 800;
  letter-spacing: -.01em;
}

.bgl-06a__me p {
  font-size: 13.5px;
  color: var(--sub);
  text-wrap: pretty;
}

.bgl-06a__toggle {
  padding: 12px 18px;
}

.bgl-06a__switch {
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 44px;
  cursor: pointer;
  font-size: 14.5px;
  font-weight: 700;
}

.bgl-06a__switch input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.bgl-06a__knob {
  position: relative;
  flex: none;
  width: 50px;
  height: 30px;
  border-radius: 9999px;
  background: rgba(120,124,140,.4);
  transition: background .3s;
}

.bgl-06a__knob::after {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 3px rgba(0,0,0,.3);
  transition: transform .3s cubic-bezier(.2,.9,.2,1);
}

.bgl-06a__switch input:checked~.bgl-06a__knob {
  background: oklch(0.7 0.17 155);
}

.bgl-06a__switch input:checked~.bgl-06a__knob::after {
  transform: translateX(20px);
}

.bgl-06a__switch input:focus-visible~.bgl-06a__knob {
  outline: 3px solid oklch(0.6 0.19 262);
  outline-offset: 2px;
}

.bgl-06a__link {
  flex-direction: row;
  align-items: center;
  gap: 14px;
  min-height: 64px;
  font-size: 15.5px;
  font-weight: 700;
  text-decoration: none;
}

.bgl-06a__link b {
  display: grid;
  place-items: center;
  flex: none;
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: var(--brand);
  color: #fff;
  font-size: 13px;
}

.bgl-06a__link em {
  margin-left: auto;
  font-style: normal;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--sub);
}

.bgl-06a__link:hover,
.bgl-06a__sq:hover {
  transform: scale(1.02);
}

.bgl-06a__link:active,
.bgl-06a__sq:active {
  transform: scale(.98);
}

.bgl-06a__link:focus-visible,
.bgl-06a__sq:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 2px;
}

.bgl-06a__sq {
  grid-column: span 2;
  align-items: center;
  min-height: 76px;
  font-size: 19px;
  font-weight: 800;
  text-decoration: none;
  color: #fff;
  background: var(--brand);
}

.bgl-06a__news label {
  font-size: 13.5px;
  font-weight: 700;
}

.bgl-06a__row {
  display: flex;
  gap: 8px;
}

.bgl-06a__row input {
  flex: 1;
  min-width: 0;
  min-height: 44px;
  padding: 0 14px;
  font-size: 14px;
  font-family: inherit;
  color: var(--ink);
  border: 1px solid rgba(120,124,140,.35);
  border-radius: 12px;
  background: transparent;
}

.bgl-06a__row input:focus-visible {
  outline: 3px solid oklch(0.6 0.19 262);
  outline-offset: 1px;
}

.bgl-06a__row button {
  min-height: 44px;
  padding: 0 20px;
  font-size: 14px;
  font-weight: 800;
  font-family: inherit;
  color: var(--bg);
  border: none;
  border-radius: 12px;
  background: var(--ink);
  cursor: pointer;
  transition: transform .2s,background .4s,color .4s;
}

.bgl-06a__row button:hover {
  transform: translateY(-1px);
}

.bgl-06a__row button:focus-visible {
  outline: 3px solid oklch(0.6 0.19 262);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .bgl-06a__card,
    .bgl-06a__knob,
    .bgl-06a__knob::after,
    .bgl-06a__row button {
    transition: none;
  }

  .bgl-06a__link:hover,
    .bgl-06a__sq:hover {
    transform: none;
  }
}

.bgl-06b,
.bgl-06b *,
.bgl-06b *::before,
.bgl-06b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bgl-06b {
  width: 100%;
  min-height: 100vh;
  --gap: 12px;
  --radius: 20px;
  container-type: inline-size;
  font-family: 'Segoe UI',system-ui,sans-serif;
  padding: 48px 20px;
  background: #131313;
}

.bgl-06b__grid {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: var(--gap);
  max-width: 440px;
  margin: 0 auto;
}

.bgl-06b__card {
  grid-column: span 2;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 10px;
  min-height: 110px;
  padding: 18px;
  border-radius: var(--radius);
  background: var(--tile);
  color: var(--tink);
  font-size: 16.5px;
  font-weight: 800;
  letter-spacing: -.01em;
  text-decoration: none;
  transition: transform .25s cubic-bezier(.2,.9,.2,1),box-shadow .25s;
}

.bgl-06b__card b {
  font-weight: 800;
  transition: transform .25s;
}

a.bgl-06b__card:hover {
  transform: translate(-3px,-3px);
  box-shadow: 5px 5px 0 rgba(255,255,255,.18);
}

a.bgl-06b__card:hover b {
  transform: translateX(4px);
}

a.bgl-06b__card:active {
  transform: translate(0,0);
  box-shadow: none;
}

a.bgl-06b__card:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.bgl-06b__hero {
  grid-column: span 4;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  gap: 6px;
  min-height: 170px;
}

.bgl-06b__hero h2 {
  font-size: clamp(38px,10cqw,52px);
  font-weight: 900;
  letter-spacing: -.04em;
  line-height: .95;
}

.bgl-06b__hero p {
  font-size: 14.5px;
  font-weight: 600;
  text-wrap: pretty;
}

.bgl-06b__wide {
  grid-column: span 4;
}

@media (prefers-reduced-motion: reduce) {
  .bgl-06b__card,
    .bgl-06b__card b {
    transition: none;
  }

  a.bgl-06b__card:hover {
    transform: none;
    box-shadow: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the dark-mode toggle is a real labelled checkbox; .hub:has(input:checked) swaps one custom-property palette and every tile re-themes via inherited variables. */

/* No JavaScript — high-contrast poster tiles on a 4-column mobile grid; hover lifts each tile diagonally with a hard offset shadow. */
```
