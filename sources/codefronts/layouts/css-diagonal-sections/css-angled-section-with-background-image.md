---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-angled-section-with-background-image/"
title: "CSS Angled Section with Background Image"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "An angled band laid over a photograph: background-size: cover, a two-stop scrim so the headline holds contrast wherever the image is bright, and the clip…"
has_js: "false"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Angled Section with Background Image
Source: https://codefronts.com/layouts/css-diagonal-sections/css-angled-section-with-background-image/

An angled band laid over a photograph: background-size: cover, a two-stop scrim so the headline holds contrast wherever the image is bright, and the clip cutting both the picture and the overlay as one. The important detail is that the image has to extend past the cut — clip the element and the photo is clipped with it, so any under-sized background reveals the page behind the diagonal.
## HTML
```html
<div class="dgs-04">
  <input class="dgs-04__sronly" type="checkbox" id="dgs-04-dark">
  <label class="dgs-04__theme" for="dgs-04-dark">
    <svg class="dgs-04__i dgs-04__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-04__i dgs-04__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-04__srtext">Toggle dark theme</span>
  </label>
  <fieldset class="dgs-04__ctl">
    <legend class="dgs-04__vh">Photo band controls</legend>
    <input class="dgs-04__sr" type="radio" name="dgs-04-f" id="dgs-04-f1"><label for="dgs-04-f1">Top</label>
    <input class="dgs-04__sr" type="radio" name="dgs-04-f" id="dgs-04-f2" checked><label for="dgs-04-f2">Centre</label>
    <input class="dgs-04__sr" type="radio" name="dgs-04-f" id="dgs-04-f3"><label for="dgs-04-f3">Base</label>
    <input class="dgs-04__sr" type="checkbox" id="dgs-04-tint"><label for="dgs-04-tint">Duotone</label>
  </fieldset>

  <div class="dgs-04__stage">
    <section class="dgs-04__above" aria-labelledby="dgs-04-a">
      <div class="dgs-04__wrap">
        <p class="dgs-04__eyebrow">Hollow &amp; Pine — Cabins</p>
        <h2 class="dgs-04__display" id="dgs-04-a">Twenty-nine cabins, none within sight of another</h2>
        <p class="dgs-04__lede">Wood-fired water, a bookshelf instead of a television, and a gravel track that keeps the world a mile back. Two-night minimum, October through May.</p>
      </div>
    </section>

    <section class="dgs-04__photo" aria-labelledby="dgs-04-b">
      <img class="dgs-04__img" src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&amp;fit=crop&amp;w=2000&amp;q=70" alt="Fog moving through a dense conifer forest at first light" width="2000" height="1200" loading="lazy" decoding="async">
      <div class="dgs-04__scrim"></div>
      <div class="dgs-04__wrap dgs-04__over">
        <p class="dgs-04__eyebrow dgs-04__eyebrow--light">Wilder Ridge, Vermont</p>
        <h2 class="dgs-04__h2" id="dgs-04-b">The photograph is the band, not a backdrop</h2>
        <p class="dgs-04__body">The <code class="dgs-04__code">&lt;img&gt;</code> is a real element inside the section with <code class="dgs-04__code">object-fit: cover</code>, so it keeps its aspect ratio, respects <code class="dgs-04__code">loading</code> hints and stays legible to assistive tech. The angle lives on the section, and a fallback fill sits underneath so a failed request never collapses the layout.</p>
        <dl class="dgs-04__facts">
          <div><dt>Sleeps</dt><dd>2&ndash;4</dd></div>
          <div><dt>Nearest road</dt><dd>1.2 mi</dd></div>
          <div><dt>From</dt><dd>$240<span>/night</span></dd></div>
        </dl>
      </div>
    </section>

    <section class="dgs-04__below" aria-labelledby="dgs-04-c">
      <div class="dgs-04__wrap">
        <h2 class="dgs-04__h3" id="dgs-04-c">Three cabins with winter openings</h2>
        <ul class="dgs-04__cards">
          <li>
            <img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&amp;fit=crop&amp;w=800&amp;q=70" alt="Sunlight through birch trunks in an open wood" width="800" height="600" loading="lazy" decoding="async">
            <strong>Birch Hollow</strong><span>Sleeps 2 · Wood stove · Jan 14&ndash;18</span>
          </li>
          <li>
            <img src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&amp;fit=crop&amp;w=800&amp;q=70" alt="A still lake beneath snow-dusted mountains" width="800" height="600" loading="lazy" decoding="async">
            <strong>Long Water</strong><span>Sleeps 4 · Lake access · Feb 2&ndash;9</span>
          </li>
          <li>
            <img src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&amp;fit=crop&amp;w=800&amp;q=70" alt="A ridge line of mountains under low cloud" width="800" height="600" loading="lazy" decoding="async">
            <strong>High Saddle</strong><span>Sleeps 2 · Off-grid · Feb 20&ndash;24</span>
          </li>
        </ul>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,500;1,6..72,300&family=Instrument+Sans:wght@400;500;600&display=swap');

.dgs-04 {
  --cut: clamp(2rem, 6vw, 8rem);
  --focal: 50%;
  --paper: #fbfaf8;
  --paper2: #eeece7;
  --ink: #191a17;
  --muted: #5f6159;
  --line: #ddd9d1;
  --shot: #232a26;
  --on-shot: #f7f6f2;
  --accent: #3f6b4f;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--paper);
  color: var(--ink);
  font-family: 'Instrument Sans', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

.dgs-04 *,
.dgs-04 *::before,
.dgs-04 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.5 0.08 150)) {
  .dgs-04 {
    --paper: oklch(0.985 0.004 90);
    --paper2: oklch(0.932 0.006 90);
    --ink: oklch(0.2 0.008 130);
    --muted: oklch(0.5 0.01 130);
    --line: oklch(0.878 0.008 90);
    --shot: oklch(0.26 0.02 160);
    --on-shot: oklch(0.972 0.005 90);
    --accent: oklch(0.5 0.075 155);
  }
}

.dgs-04__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-04__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.dgs-04__ctl {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 40;
  margin: 0;
  padding: .25rem;
  display: flex;
  gap: .15rem;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: rgba(251,250,248,.88);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
}

.dgs-04__ctl label {
  min-inline-size: 2.9rem;
  min-block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding-inline: .7rem;
  border-radius: 7px;
  font-size: .76rem;
  font-weight: 500;
  color: var(--muted);
  cursor: pointer;
  transition: background .2s ease, color .2s ease;
}

.dgs-04__ctl label:hover {
  color: var(--ink);
}

.dgs-04__sr:checked + label {
  background: var(--ink);
  color: var(--paper);
}

.dgs-04__sr:focus-visible + label {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.dgs-04__stage {
  display: flow-root;
}

.dgs-04__wrap {
  inline-size: min(70rem, 100%);
  margin-inline: auto;
}

.dgs-04__above {
  padding: clamp(4rem, 10vw, 7rem) clamp(1.25rem, 5vw, 4rem) calc(var(--cut) + clamp(2.5rem, 6vw, 4.5rem));
}

.dgs-04__eyebrow {
  margin: 0 0 1rem;
  font-size: .74rem;
  font-weight: 600;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--accent);
}

.dgs-04__eyebrow--light {
  color: rgba(247,246,242,.85);
}

.dgs-04__display {
  margin: 0 0 1.1rem;
  max-inline-size: 24ch;
  font-family: 'Newsreader', ui-serif, Georgia, serif;
  font-weight: 300;
  font-size: clamp(2.3rem, 7.5vw, 4.6rem);
  line-height: 1.02;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.dgs-04__lede {
  margin: 0;
  max-inline-size: 50ch;
  font-size: clamp(1.02rem, 2vw, 1.18rem);
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-04__photo {
  position: relative;
  z-index: 1;
  isolation: isolate;
  background: var(--shot);
  color: var(--on-shot);
  clip-path: polygon(0 var(--cut), 100% 0, 100% calc(100% - var(--cut)), 0 100%);
  margin-block: calc(var(--cut) * -1 - 1px);
  padding: calc(var(--cut) + clamp(3rem, 7vw, 5rem)) clamp(1.25rem, 5vw, 4rem) calc(var(--cut) + clamp(3rem, 7vw, 5rem));
}

.dgs-04__img {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  object-position: 50% var(--focal);
  z-index: -2;
  transition: object-position .4s ease, filter .4s ease;
}

.dgs-04__scrim {
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(105deg, rgba(12,16,14,.86) 0%, rgba(12,16,14,.62) 46%, rgba(12,16,14,.2) 100%);
}

.dgs-04__over {
  position: relative;
}

.dgs-04__h2 {
  margin: 0 0 1rem;
  max-inline-size: 26ch;
  font-family: 'Newsreader', ui-serif, Georgia, serif;
  font-weight: 300;
  font-size: clamp(1.8rem, 5vw, 3.2rem);
  line-height: 1.05;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.dgs-04__body {
  margin: 0 0 1.75rem;
  max-inline-size: 54ch;
  color: rgba(247,246,242,.82);
  text-wrap: pretty;
}

.dgs-04__code {
  font-family: ui-monospace, 'SF Mono', Menlo, monospace;
  font-size: .86em;
  padding: .1em .35em;
  border-radius: 4px;
  background: rgba(255,255,255,.14);
}

.dgs-04__facts {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem clamp(1.5rem, 5vw, 3.5rem);
}

.dgs-04__facts > div {
  padding-block-start: .7rem;
  border-block-start: 1px solid rgba(247,246,242,.4);
  min-inline-size: 7rem;
}

.dgs-04__facts dt {
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: rgba(247,246,242,.7);
}

.dgs-04__facts dd {
  margin: .3rem 0 0;
  font-family: 'Newsreader', serif;
  font-size: clamp(1.4rem, 3.5vw, 1.9rem);
  font-variant-numeric: tabular-nums;
}

.dgs-04__facts span {
  font-family: 'Instrument Sans', sans-serif;
  font-size: .78rem;
  opacity: .75;
}

.dgs-04__below {
  background: var(--paper2);
  padding: calc(var(--cut) + clamp(3rem, 7vw, 5rem)) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6rem);
}

.dgs-04__h3 {
  margin: 0 0 1.75rem;
  font-family: 'Newsreader', ui-serif, Georgia, serif;
  font-weight: 300;
  font-size: clamp(1.5rem, 4vw, 2.3rem);
  letter-spacing: -.02em;
}

.dgs-04__cards {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1.25rem;
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
}

.dgs-04__cards li {
  display: grid;
  gap: .5rem;
}

.dgs-04__cards img {
  inline-size: 100%;
  block-size: clamp(9rem, 22vw, 13rem);
  object-fit: cover;
  border-radius: 12px;
  background: var(--shot);
  transition: scale .35s cubic-bezier(.2,.8,.3,1);
}

.dgs-04__cards li:hover img {
  scale: 1.015;
}

.dgs-04__cards strong {
  font-size: 1.02rem;
  letter-spacing: -.01em;
}

.dgs-04__cards span {
  font-size: .86rem;
  color: var(--muted);
}

.dgs-04:has(#dgs-04-f1:checked) {
  --focal: 12%;
}

.dgs-04:has(#dgs-04-f3:checked) {
  --focal: 88%;
}

.dgs-04:has(#dgs-04-tint:checked) .dgs-04__img {
  filter: grayscale(1) contrast(1.08);
}

.dgs-04:has(#dgs-04-tint:checked) .dgs-04__scrim {
  background: linear-gradient(105deg, rgba(24,44,34,.9) 0%, rgba(30,52,40,.66) 50%, rgba(63,107,79,.35) 100%);
  mix-blend-mode: multiply;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-04 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-04__scrim {
    display: none;
  }

  .dgs-04__photo {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
  }

  .dgs-04__img {
    opacity: .25;
  }

  .dgs-04__ctl label {
    border: 1px solid CanvasText;
  }

  .dgs-04__sr:checked + label {
    background: Highlight;
    color: HighlightText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-04__sronly,
.dgs-04__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-04__theme {
  position: absolute;
  inset-block-start: clamp(.85rem, 2.2vw, 1.5rem);
  inset-inline-end: clamp(.85rem, 2.2vw, 1.5rem);
  z-index: 60;
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: 999px;
  border: 1px solid currentColor;
  color: inherit;
  background: rgba(127,127,127,.16);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: translate .2s ease;
}

.dgs-04__theme:hover {
  translate: 0 -1px;
}

.dgs-04__sronly:focus-visible + .dgs-04__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-04__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-04__i--sun {
  display: none;
}

.dgs-04:has(#dgs-04-dark:checked) .dgs-04__i--moon {
  display: none;
}

.dgs-04:has(#dgs-04-dark:checked) .dgs-04__i--sun {
  display: block;
}

.dgs-04:has(#dgs-04-dark:checked) {
  --paper: #101318;
  --ink: #eef2f8;
  --muted: #98a2b3;
  --line: #242a35;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-04__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-04__theme {
    border-color: CanvasText;
  }
}
```
