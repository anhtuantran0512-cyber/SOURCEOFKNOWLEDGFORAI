---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/empty-shopping-cart-state/"
title: "Empty Shopping Cart State"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "An empty bag that behaves like a shop rather than a dead end: the bag panel on the left, three pieces the store actually wants to move on the right, and…"
has_js: "true"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Empty Shopping Cart State
Source: https://codefronts.com/snippets/css-empty-states/empty-shopping-cart-state/

An empty bag that behaves like a shop rather than a dead end: the bag panel on the left, three pieces the store actually wants to move on the right, and adding one turns the empty state into a real line item with a subtotal and a checkout. Warm paper, an Instrument Serif headline, a dotted letterpress texture and a slowly rotating dashed seal &mdash; boutique retail rather than SaaS.
## HTML
```html
<div class="est-03">
  <header class="est-03__top">
    <a class="est-03__brand" href="#est-03">Fold &amp; Vessel</a>
    <nav class="est-03__nav" aria-label="Shop">
      <a href="#est-03">Ceramics</a>
      <a href="#est-03">Glassware</a>
      <a href="#est-03">Linen</a>
      <a href="#est-03">Journal</a>
    </nav>
    <div class="est-03__tools">
      <button class="est-03__tool" type="button" aria-label="Search">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="11" cy="11" r="6.2" stroke="currentColor" stroke-width="1.6"/><path d="m15.8 15.8 3.6 3.6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
      </button>
      <button class="est-03__tool est-03__tool--bag" type="button" aria-label="Bag">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6.5 8h11l1 11.5h-13z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M9.3 8V6.6a2.7 2.7 0 0 1 5.4 0V8" stroke="currentColor" stroke-width="1.6"/></svg>
        <span class="est-03__bagdot" id="est-03-dot" hidden></span>
      </button>
    </div>
  </header>

  <main class="est-03__main">
    <section class="est-03__bag" aria-labelledby="est-03-h">
      <div class="est-03__empty" id="est-03-empty">
        <span class="est-03__seal" aria-hidden="true">
          <svg viewBox="0 0 60 60" fill="none" focusable="false">
            <circle cx="30" cy="30" r="28.4" stroke="currentColor" stroke-width="1" stroke-dasharray="2 4"/>
            <path d="M20 24h20l1.6 18H18.4z" stroke="currentColor" stroke-width="1.2" stroke-linejoin="round"/>
            <path d="M25.6 24v-2.4a4.4 4.4 0 0 1 8.8 0V24" stroke="currentColor" stroke-width="1.2"/>
          </svg>
        </span>
        <h1 class="est-03__h1" id="est-03-h">Your bag is waiting</h1>
        <p class="est-03__p">Everything is made in small runs, so pieces move quickly. Start with the shapes people keep coming back for.</p>
        <div class="est-03__acts">
          <a class="est-03__pri" href="#est-03">Shop the collection</a>
          <a class="est-03__sec" href="#est-03">Reorder from July</a>
        </div>
      </div>

      <ul class="est-03__lines" id="est-03-lines" hidden></ul>
      <div class="est-03__sum" id="est-03-sum" hidden>
        <div class="est-03__sumrow"><span>Subtotal</span><span id="est-03-total">&mdash;</span></div>
        <div class="est-03__sumrow est-03__sumrow--faint"><span>Shipping</span><span>Calculated at checkout</span></div>
        <a class="est-03__pri est-03__pri--wide" href="#est-03">Checkout</a>
      </div>
    </section>

    <aside class="est-03__rec" aria-label="Popular pieces">
      <p class="est-03__reclabel">Kept coming back</p>
      <ul class="est-03__cards">
        <li class="est-03__card">
          <figure class="est-03__shot">
            <img src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=560&amp;q=80&amp;auto=format&amp;fit=crop" alt="Stoneware cup on a pale surface" loading="lazy" decoding="async">
          </figure>
          <div class="est-03__cbody">
            <p class="est-03__cname">Ash stoneware cup</p>
            <p class="est-03__cmeta">Matte glaze &middot; 240ml</p>
            <div class="est-03__crow">
              <span class="est-03__price">&pound;28</span>
              <button class="est-03__add" type="button" data-add="Ash stoneware cup" data-price="28">Add</button>
            </div>
          </div>
        </li>
        <li class="est-03__card">
          <figure class="est-03__shot">
            <img src="https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=560&amp;q=80&amp;auto=format&amp;fit=crop" alt="Ceramic mug and saucer" loading="lazy" decoding="async">
          </figure>
          <div class="est-03__cbody">
            <p class="est-03__cname">Saucer set of two</p>
            <p class="est-03__cmeta">Sand clay &middot; 14cm</p>
            <div class="est-03__crow">
              <span class="est-03__price">&pound;42</span>
              <button class="est-03__add" type="button" data-add="Saucer set of two" data-price="42">Add</button>
            </div>
          </div>
        </li>
        <li class="est-03__card">
          <figure class="est-03__shot">
            <img src="https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=560&amp;q=80&amp;auto=format&amp;fit=crop" alt="Dark ceramic vessel with coffee" loading="lazy" decoding="async">
          </figure>
          <div class="est-03__cbody">
            <p class="est-03__cname">Ink pour-over jug</p>
            <p class="est-03__cmeta">Iron glaze &middot; 600ml</p>
            <div class="est-03__crow">
              <span class="est-03__price">&pound;56</span>
              <button class="est-03__add" type="button" data-add="Ink pour-over jug" data-price="56">Add</button>
            </div>
          </div>
        </li>
      </ul>
    </aside>
  </main>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Instrument+Serif:ital@0;1&display=swap');

.est-03 {
  --paper: #f6f1e8;
  --card: #fffdf8;
  --sunk: #efe8dc;
  --line: #e2d9c9;
  --line-2: #d2c6b1;
  --ink: #241f19;
  --muted: #6a6055;
  --faint: #8f8577;
  --clay: #a4562c;
  --olive: #5d6444;
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

.est-03 *,
.est-03 *::before,
.est-03 *::after {
  box-sizing: border-box;
}

.est-03 [hidden] {
  display: none !important;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-03 {
    --paper: oklch(0.958 0.015 82);
    --card: oklch(0.988 0.008 82);
    --sunk: oklch(0.925 0.019 80);
    --line: oklch(0.885 0.022 80);
    --line-2: oklch(0.82 0.03 78);
    --ink: oklch(0.235 0.018 55);
    --muted: oklch(0.475 0.021 60);
    --faint: oklch(0.605 0.02 62);
    --clay: oklch(0.53 0.115 45);
    --olive: oklch(0.47 0.055 115);
  }
}

.est-03__top {
  display: flex;
  flex-wrap: wrap;
  gap: .75rem 1.5rem;
  align-items: center;
  justify-content: space-between;
  padding: 1.1rem clamp(1rem,4vw,3rem);
  border-block-end: 1px solid var(--line);
  background: color-mix(in oklab, var(--paper) 85%, transparent);
  backdrop-filter: blur(8px);
}

.est-03__brand {
  font-family: 'Instrument Serif',Georgia,serif;
  font-size: 1.35rem;
  letter-spacing: -.01em;
  color: var(--ink);
  text-decoration: none;
}

.est-03__nav {
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem;
}

.est-03__nav a {
  font-size: .86rem;
  color: var(--muted);
  text-decoration: none;
  padding-block: .25rem;
  border-block-end: 1px solid transparent;
  transition: color .16s, border-color .16s;
}

.est-03__nav a:hover {
  color: var(--ink);
  border-color: var(--clay);
}

.est-03__tools {
  display: flex;
  gap: .4rem;
}

.est-03__tool {
  position: relative;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  color: var(--ink);
  background: transparent;
  border: 1px solid transparent;
  border-radius: 50%;
  transition: background .16s, border-color .16s;
}

.est-03__tool svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.est-03__tool:hover {
  background: var(--sunk);
  border-color: var(--line);
}

.est-03__bagdot {
  position: absolute;
  inset-block-start: .45rem;
  inset-inline-end: .45rem;
  inline-size: .45rem;
  block-size: .45rem;
  border-radius: 50%;
  background: var(--clay);
  box-shadow: 0 0 0 2px var(--paper);
  animation: est-03-pop .3s cubic-bezier(.2,.8,.3,1.4) both;
}

@keyframes est-03-pop {
  from {
    scale: 0;
  }

  to {
    scale: 1;
  }
}

.est-03__main {
  min-inline-size: 0;
  padding: clamp(1.5rem,5vw,4rem) clamp(1rem,4vw,3rem);
  display: grid;
  gap: clamp(1.5rem,4vw,3.5rem);
  grid-template-columns: repeat(auto-fit,minmax(min(20rem,100%),1fr));
  align-items: start;
}

.est-03__bag {
  min-inline-size: 0;
  display: grid;
  gap: 1rem;
  align-content: start;
}

.est-03__empty {
  display: grid;
  gap: .7rem;
  padding: clamp(1.5rem,3vw,2.5rem) clamp(1.25rem,3vw,2.25rem);
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 6px;
  box-shadow: 0 1px 0 var(--line), 0 34px 60px -50px rgba(36,31,25,.55);
  background-image: radial-gradient(color-mix(in oklab, var(--line-2) 45%, transparent) .6px, transparent .6px);
  background-size: 14px 14px;
  background-blend-mode: multiply;
  animation: est-03-in .55s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes est-03-in {
  from {
    opacity: 0;
    translate: 0 8px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.est-03__seal {
  inline-size: 3.75rem;
  block-size: 3.75rem;
  display: grid;
  place-items: center;
  color: var(--clay);
  animation: est-03-turn 30s linear infinite;
}

.est-03__seal svg {
  inline-size: 100%;
  block-size: 100%;
}

@keyframes est-03-turn {
  to {
    rotate: 360deg;
  }
}

.est-03__h1 {
  margin: .25rem 0 0;
  font-family: 'Instrument Serif',Georgia,serif;
  font-size: clamp(1.9rem,4.5vw,2.9rem);
  font-weight: 400;
  letter-spacing: -.015em;
  line-height: 1.04;
  text-wrap: balance;
}

.est-03__p {
  margin: 0;
  max-inline-size: 38ch;
  font-size: .95rem;
  line-height: 1.62;
  color: var(--muted);
  text-wrap: pretty;
}

.est-03__acts {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  margin-block-start: .6rem;
}

.est-03__pri {
  min-block-size: 2.85rem;
  display: inline-flex;
  align-items: center;
  padding: .7rem 1.25rem;
  font-size: .88rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--card);
  background: var(--ink);
  border: 1px solid var(--ink);
  border-radius: 2px;
  text-decoration: none;
  transition: background .18s, color .18s, translate .16s;
}

.est-03__pri:hover {
  background: var(--clay);
  border-color: var(--clay);
  translate: 0 -1px;
}

.est-03__pri--wide {
  justify-content: center;
  margin-block-start: .4rem;
}

.est-03__sec {
  min-block-size: 2.85rem;
  display: inline-flex;
  align-items: center;
  padding: .7rem 1.1rem;
  font-size: .88rem;
  cursor: pointer;
  color: var(--ink);
  background: transparent;
  border: 1px solid var(--line-2);
  border-radius: 2px;
  text-decoration: none;
  transition: background .18s;
}

.est-03__sec:hover {
  background: var(--sunk);
}

.est-03__lines {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .5rem;
}

.est-03__line {
  display: grid;
  grid-template-columns: minmax(0,1fr) auto auto;
  gap: .5rem 1rem;
  align-items: center;
  padding: .9rem 1rem;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 4px;
  animation: est-03-in .4s cubic-bezier(.2,.7,.3,1) both;
}

.est-03__lname {
  min-inline-size: 0;
  display: grid;
  gap: .15rem;
}

.est-03__lname b {
  font-size: .92rem;
  font-weight: 500;
}

.est-03__lname span {
  font-size: .78rem;
  color: var(--faint);
}

.est-03__lprice {
  font-size: .92rem;
  font-variant-numeric: tabular-nums;
}

.est-03__lx {
  inline-size: 1.9rem;
  block-size: 1.9rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  color: var(--faint);
  background: transparent;
  border: 1px solid transparent;
  border-radius: 50%;
  font-size: 1rem;
  line-height: 1;
}

.est-03__lx:hover {
  color: var(--ink);
  background: var(--sunk);
  border-color: var(--line);
}

.est-03__sum {
  display: grid;
  gap: .4rem;
  padding: 1rem 1.1rem;
  border: 1px solid var(--line);
  border-radius: 4px;
  background: var(--sunk);
}

.est-03__sumrow {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  font-size: .9rem;
}

.est-03__sumrow--faint {
  color: var(--faint);
  font-size: .8rem;
}

.est-03__sumrow span:last-child {
  font-variant-numeric: tabular-nums;
}

.est-03__rec {
  min-inline-size: 0;
  display: grid;
  gap: .85rem;
  align-content: start;
}

.est-03__reclabel {
  margin: 0;
  font-family: 'Instrument Serif',Georgia,serif;
  font-style: italic;
  font-size: 1.05rem;
  color: var(--muted);
}

.est-03__cards {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .9rem;
  grid-template-columns: repeat(auto-fit,minmax(min(11rem,100%),1fr));
}

.est-03__card {
  display: grid;
  grid-template-rows: auto auto;
  overflow: hidden;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 4px;
  transition: translate .18s, box-shadow .22s, border-color .18s;
}

.est-03__card:hover {
  translate: 0 -2px;
  border-color: var(--line-2);
  box-shadow: 0 22px 34px -30px rgba(36,31,25,.7);
}

.est-03__shot {
  margin: 0;
  aspect-ratio: 4/5;
  overflow: hidden;
  background: linear-gradient(150deg, var(--sunk), color-mix(in oklab, var(--clay) 14%, var(--sunk)));
}

.est-03__shot img {
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  display: block;
  filter: saturate(.92) contrast(1.02);
}

.est-03__cbody {
  display: grid;
  gap: .3rem;
  padding: .8rem .85rem .9rem;
}

.est-03__cname {
  margin: 0;
  font-size: .88rem;
  font-weight: 500;
  letter-spacing: -.012em;
}

.est-03__cmeta {
  margin: 0;
  font-size: .76rem;
  color: var(--faint);
}

.est-03__crow {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .5rem;
  margin-block-start: .3rem;
}

.est-03__price {
  font-size: .9rem;
  font-variant-numeric: tabular-nums;
}

.est-03__add {
  min-block-size: 2.25rem;
  padding: .4rem .8rem;
  font: inherit;
  font-size: .8rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--ink);
  background: transparent;
  border: 1px solid var(--line-2);
  border-radius: 2px;
  transition: background .16s, color .16s, border-color .16s;
}

.est-03__add:hover {
  color: var(--card);
  background: var(--olive);
  border-color: var(--olive);
}

.est-03__add[data-in] {
  color: var(--card);
  background: var(--olive);
  border-color: var(--olive);
}

.est-03__tool:focus-visible,
.est-03__add:focus-visible,
.est-03__pri:focus-visible,
.est-03__sec:focus-visible,
.est-03__lx:focus-visible,
.est-03__nav a:focus-visible,
.est-03__brand:focus-visible {
  outline: 2px solid var(--clay);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .est-03 *,
    .est-03 *::before,
    .est-03 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-03__empty,
    .est-03__card,
    .est-03__pri,
    .est-03__add {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.est-03'); if(!root) return;
  var empty = root.querySelector('#est-03-empty'), lines = root.querySelector('#est-03-lines'),
      sum = root.querySelector('#est-03-sum'), total = root.querySelector('#est-03-total'), dot = root.querySelector('#est-03-dot');
  var bag = [];
  function paint(){
    empty.hidden = bag.length > 0;
    lines.hidden = sum.hidden = dot.hidden = bag.length === 0;
    lines.innerHTML = bag.map(function(it, i){
      return '<li class="est-03__line"><span class="est-03__lname"><b>' + it.name + '</b><span>Ships in 2 days</span></span>' +
             '<span class="est-03__lprice">&pound;' + it.price + '</span>' +
             '<button class="est-03__lx" type="button" data-rm="' + i + '" aria-label="Remove ' + it.name + '">&times;</button></li>';
    }).join('');
    total.innerHTML = '&pound;' + bag.reduce(function(a,b){ return a + b.price; }, 0);
    root.querySelectorAll('.est-03__add').forEach(function(b){
      b.toggleAttribute('data-in', bag.some(function(it){ return it.name === b.dataset.add; }));
      b.textContent = bag.some(function(it){ return it.name === b.dataset.add; }) ? 'In bag' : 'Add';
    });
  }
  root.addEventListener('click', function(e){
    var add = e.target.closest('[data-add]'), rm = e.target.closest('[data-rm]');
    if(add){
      if(!bag.some(function(it){ return it.name === add.dataset.add; })) bag.push({ name: add.dataset.add, price: +add.dataset.price });
      paint();
    } else if(rm){
      bag.splice(+rm.dataset.rm, 1); paint();
    }
  });
  paint();
})();
```
