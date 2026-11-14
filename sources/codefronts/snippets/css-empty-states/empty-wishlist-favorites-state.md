---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/empty-wishlist-favorites-state/"
title: "Empty Wishlist / Favorites State"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "Three saved-state tabs in a boutique storefront, each with its own empty message, driven entirely by CSS state: radios plus :has() switch the panels, ghost…"
has_js: "false"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Empty Wishlist / Favorites State
Source: https://codefronts.com/snippets/css-empty-states/empty-wishlist-favorites-state/

Three saved-state tabs in a boutique storefront, each with its own empty message, driven entirely by CSS state: radios plus :has() switch the panels, ghost product frames sit behind the first card so the grid still reads as a grid, and a row of recently viewed pieces gives the page somewhere to go.
## HTML
```html
<div class="est-09">
  <header class="est-09__top">
    <a class="est-09__brand" href="#est-09">Maren &amp; Co</a>
    <nav class="est-09__nav" aria-label="Shop">
      <a href="#est-09">New in</a>
      <a href="#est-09">Knitwear</a>
      <a href="#est-09">Outerwear</a>
      <a href="#est-09">Archive</a>
    </nav>
    <span class="est-09__acct">Account</span>
  </header>

  <main class="est-09__main">
    <div class="est-09__head">
      <h1 class="est-09__h1">Saved</h1>
      <p class="est-09__hp">Pieces you keep, price drops you asked us to watch, and the sizes we will hold for you.</p>
    </div>

    <div class="est-09__tabs">
      <input class="est-09__radio" type="radio" name="est-09-tab" id="est-09-t1" checked>
      <input class="est-09__radio" type="radio" name="est-09-tab" id="est-09-t2">
      <input class="est-09__radio" type="radio" name="est-09-tab" id="est-09-t3">
      <div class="est-09__tabrow" role="tablist">
        <label class="est-09__tab" for="est-09-t1">Saved pieces</label>
        <label class="est-09__tab" for="est-09-t2">Price alerts</label>
        <label class="est-09__tab" for="est-09-t3">Size holds</label>
      </div>

      <section class="est-09__panel" data-panel="1">
        <div class="est-09__ghosts" aria-hidden="true">
          <span></span><span></span><span></span><span></span>
        </div>
        <div class="est-09__empty">
          <span class="est-09__heart" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 19.5S4.5 14.8 4.5 9.9A3.9 3.9 0 0 1 12 8a3.9 3.9 0 0 1 7.5 1.9c0 4.9-7.5 9.6-7.5 9.6z" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/></svg>
          </span>
          <p class="est-09__eh">Nothing saved yet</p>
          <p class="est-09__ep">Tap the heart on any piece and it waits here &mdash; we will tell you before it sells out.</p>
          <a class="est-09__pri" href="#est-09">Browse new in</a>
        </div>
      </section>

      <section class="est-09__panel" data-panel="2">
        <div class="est-09__empty">
          <span class="est-09__heart" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M5 19h14M8 15V9.5M12 15V6M16 15v-4" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>
          </span>
          <p class="est-09__eh">No price alerts running</p>
          <p class="est-09__ep">Set one on a piece and we email you the moment it moves &mdash; once per item, never a digest.</p>
          <a class="est-09__pri" href="#est-09">See the archive sale</a>
        </div>
      </section>

      <section class="est-09__panel" data-panel="3">
        <div class="est-09__empty">
          <span class="est-09__heart" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" focusable="false"><rect x="4.5" y="7" width="15" height="12" rx="2" stroke="currentColor" stroke-width="1.3"/><path d="M9 7V5.5A3 3 0 0 1 15 5.5V7" stroke="currentColor" stroke-width="1.3"/></svg>
          </span>
          <p class="est-09__eh">No sizes on hold</p>
          <p class="est-09__ep">In-store staff can hold a size for 48 hours. Ask at the counter and it appears here.</p>
          <a class="est-09__pri" href="#est-09">Find a store</a>
        </div>
      </section>
    </div>

    <section class="est-09__seen">
      <h2 class="est-09__seenh">Last looked at</h2>
      <ul class="est-09__cards">
        <li class="est-09__card">
          <figure class="est-09__shot"><img src="https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=520&amp;q=80&amp;auto=format&amp;fit=crop" alt="Folded wool coat on a bench" loading="lazy" decoding="async"></figure>
          <p class="est-09__cn">Merino wool coat</p>
          <p class="est-09__cp">&pound;340</p>
        </li>
        <li class="est-09__card">
          <figure class="est-09__shot"><img src="https://images.unsplash.com/photo-1483985988355-763728e1935b?w=520&amp;q=80&amp;auto=format&amp;fit=crop" alt="Clothing rail in a boutique" loading="lazy" decoding="async"></figure>
          <p class="est-09__cn">Boxy cotton shirt</p>
          <p class="est-09__cp">&pound;95</p>
        </li>
        <li class="est-09__card">
          <figure class="est-09__shot"><img src="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=520&amp;q=80&amp;auto=format&amp;fit=crop" alt="Model wearing knitwear" loading="lazy" decoding="async"></figure>
          <p class="est-09__cn">Ribbed knit vest</p>
          <p class="est-09__cp">&pound;120</p>
        </li>
      </ul>
    </section>
  </main>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Instrument+Serif:ital@0;1&display=swap');

.est-09 {
  --paper: #f7f4ef;
  --card: #fffefb;
  --sunk: #efe9e0;
  --line: #e3dcd1;
  --line-2: #cfc5b6;
  --ink: #20201d;
  --muted: #63605a;
  --faint: #918d85;
  --accent: #7b5c3e;
  --pink: #a5606a;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: auto minmax(0,1fr);
  box-sizing: border-box;
  background: var(--paper);
  color: var(--ink);
  color-scheme: light;
  font-synthesis: none;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.est-09 *,
.est-09 *::before,
.est-09 *::after {
  box-sizing: border-box;
}

.est-09 [hidden] {
  display: none !important;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-09 {
    --paper: oklch(0.966 0.008 80);
    --card: oklch(0.993 0.004 80);
    --sunk: oklch(0.932 0.013 78);
    --line: oklch(0.895 0.014 78);
    --line-2: oklch(0.815 0.019 76);
    --ink: oklch(0.215 0.008 70);
    --muted: oklch(0.46 0.01 70);
    --faint: oklch(0.615 0.011 70);
    --accent: oklch(0.45 0.06 62);
    --pink: oklch(0.55 0.09 15);
  }
}

.est-09__top {
  display: flex;
  flex-wrap: wrap;
  gap: .75rem 1.5rem;
  align-items: center;
  justify-content: space-between;
  padding: 1.1rem clamp(1rem,4vw,3rem);
  border-block-end: 1px solid var(--line);
}

.est-09__brand {
  font-family: 'Instrument Serif',Georgia,serif;
  font-size: 1.3rem;
  color: var(--ink);
  text-decoration: none;
}

.est-09__nav {
  display: flex;
  flex-wrap: wrap;
  gap: 1.2rem;
}

.est-09__nav a {
  font-size: .85rem;
  color: var(--muted);
  text-decoration: none;
  padding-block: .2rem;
  border-block-end: 1px solid transparent;
  transition: color .16s, border-color .16s;
}

.est-09__nav a:hover {
  color: var(--ink);
  border-color: var(--accent);
}

.est-09__acct {
  font-size: .85rem;
  color: var(--muted);
}

.est-09__main {
  min-inline-size: 0;
  inline-size: min(72rem,100%);
  justify-self: center;
  padding: clamp(1.5rem,4.5vw,3.5rem) clamp(1rem,4vw,3rem);
  display: grid;
  gap: clamp(1.5rem,4vw,2.75rem);
  align-content: start;
}

.est-09__head {
  display: grid;
  gap: .5rem;
}

.est-09__h1 {
  margin: 0;
  font-family: 'Instrument Serif',Georgia,serif;
  font-size: clamp(2rem,5vw,3rem);
  font-weight: 400;
  letter-spacing: -.02em;
  line-height: 1;
}

.est-09__hp {
  margin: 0;
  max-inline-size: 52ch;
  font-size: .95rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.est-09__tabs {
  display: grid;
  gap: 1.25rem;
}

.est-09__radio {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

.est-09__tabrow {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  border-block-end: 1px solid var(--line);
}

.est-09__tab {
  padding: .55rem .1rem;
  margin-block-end: -1px;
  cursor: pointer;
  font-size: .88rem;
  color: var(--faint);
  border-block-end: 1.5px solid transparent;
  transition: color .18s, border-color .18s;
}

.est-09__tab:hover {
  color: var(--ink);
}

.est-09__tabs:has(#est-09-t1:checked) .est-09__tab[for="est-09-t1"],
.est-09__tabs:has(#est-09-t2:checked) .est-09__tab[for="est-09-t2"],
.est-09__tabs:has(#est-09-t3:checked) .est-09__tab[for="est-09-t3"] {
  color: var(--ink);
  border-color: var(--ink);
}

#est-09-t1:focus-visible ~ .est-09__tabrow .est-09__tab[for="est-09-t1"],
#est-09-t2:focus-visible ~ .est-09__tabrow .est-09__tab[for="est-09-t2"],
#est-09-t3:focus-visible ~ .est-09__tabrow .est-09__tab[for="est-09-t3"] {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.est-09__panel {
  display: none;
  position: relative;
}

.est-09__tabs:has(#est-09-t1:checked) [data-panel="1"],
.est-09__tabs:has(#est-09-t2:checked) [data-panel="2"],
.est-09__tabs:has(#est-09-t3:checked) [data-panel="3"] {
  display: grid;
  animation: est-09-in .45s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes est-09-in {
  from {
    opacity: 0;
    translate: 0 6px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.est-09__ghosts {
  position: absolute;
  inset: 0;
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 1rem;
  opacity: .55;
}

.est-09__ghosts span {
  border: 1px dashed var(--line-2);
  border-radius: 3px;
  background: linear-gradient(160deg, var(--card), var(--sunk));
}

.est-09__ghosts span:nth-child(2) {
  opacity: .75;
}

.est-09__ghosts span:nth-child(3) {
  opacity: .5;
}

.est-09__ghosts span:nth-child(4) {
  opacity: .3;
}

.est-09__empty {
  position: relative;
  z-index: 1;
  justify-self: center;
  inline-size: min(30rem,100%);
  display: grid;
  justify-items: center;
  text-align: center;
  gap: .5rem;
  padding: clamp(2.25rem,7vw,4rem) clamp(1.25rem,3vw,2rem);
  margin-block: clamp(1rem,3vw,2rem);
  background: color-mix(in oklab, var(--card) 88%, transparent);
  backdrop-filter: blur(3px);
  border: 1px solid var(--line);
  border-radius: 4px;
  box-shadow: 0 30px 60px -50px rgba(32,32,29,.6);
}

.est-09__heart {
  inline-size: 3.25rem;
  block-size: 3.25rem;
  display: grid;
  place-items: center;
  margin-block-end: .4rem;
  color: var(--pink);
  border: 1px solid var(--line);
  border-radius: 50%;
  background: var(--card);
}

.est-09__heart svg {
  inline-size: 1.5rem;
  block-size: 1.5rem;
  animation: est-09-beat 4.5s ease-in-out infinite;
}

@keyframes est-09-beat {
  0%,
    100% {
    scale: 1;
  }

  45% {
    scale: 1.08;
  }

  55% {
    scale: 1.02;
  }
}

.est-09__eh {
  margin: 0;
  font-family: 'Instrument Serif',Georgia,serif;
  font-size: clamp(1.4rem,3vw,1.85rem);
  font-weight: 400;
  line-height: 1.1;
  text-wrap: balance;
}

.est-09__ep {
  margin: 0;
  max-inline-size: 40ch;
  font-size: .9rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.est-09__pri {
  min-block-size: 2.85rem;
  display: inline-flex;
  align-items: center;
  margin-block-start: .7rem;
  padding: .7rem 1.2rem;
  font-size: .87rem;
  font-weight: 500;
  color: var(--card);
  background: var(--ink);
  border: 1px solid var(--ink);
  border-radius: 2px;
  text-decoration: none;
  transition: background .18s, translate .16s;
}

.est-09__pri:hover {
  background: var(--accent);
  border-color: var(--accent);
  translate: 0 -1px;
}

.est-09__seen {
  display: grid;
  gap: .9rem;
}

.est-09__seenh {
  margin: 0;
  font-family: 'Instrument Serif',Georgia,serif;
  font-style: italic;
  font-size: 1.15rem;
  font-weight: 400;
  color: var(--muted);
}

.est-09__cards {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(min(12rem,100%),1fr));
}

.est-09__card {
  display: grid;
  gap: .4rem;
}

.est-09__shot {
  margin: 0 0 .3rem;
  aspect-ratio: 3/4;
  overflow: hidden;
  border-radius: 3px;
  background: linear-gradient(160deg,var(--sunk),color-mix(in oklab,var(--accent) 12%,var(--sunk)));
}

.est-09__shot img {
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  display: block;
  filter: saturate(.9);
  transition: scale .5s cubic-bezier(.2,.7,.3,1);
}

.est-09__card:hover .est-09__shot img {
  scale: 1.03;
}

.est-09__cn {
  margin: 0;
  font-size: .87rem;
  font-weight: 500;
}

.est-09__cp {
  margin: 0;
  font-size: .83rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

@media (max-width: 700px) {
  .est-09__ghosts {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (prefers-reduced-motion: reduce) {
  .est-09 *,
    .est-09 *::before,
    .est-09 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-09__empty,
    .est-09__pri,
    .est-09__heart {
    border-color: CanvasText;
  }
}
```
