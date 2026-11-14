---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/accessible-empty-state-aria-live/"
title: "Accessible Empty State (ARIA Live)"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "The accessible version of a no-results state, in a library catalogue: a visually hidden role=\"status\" region announces the outcome, focus moves to the…"
has_js: "true"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Empty State (ARIA Live)
Source: https://codefronts.com/snippets/css-empty-states/accessible-empty-state-aria-live/

The accessible version of a no-results state, in a library catalogue: a visually hidden role="status" region announces the outcome, focus moves to the results container so a screen reader lands on the message rather than hunting for it, and the recovery suggestions are real buttons that re-run the search. Nothing about the accessibility work is visible &mdash; which is the point.
## HTML
```html
<div class="est-17">
  <a class="est-17__skip" href="#est-17-results">Skip to results</a>
  <div class="est-17__shell">
    <header class="est-17__top">
      <span class="est-17__brand">Ordnance Library</span>
      <nav class="est-17__nav" aria-label="Catalogue">
        <a href="#est-17">Maps</a>
        <a href="#est-17">Surveys</a>
        <a href="#est-17">Photographs</a>
      </nav>
    </header>

    <main class="est-17__main">
      <form class="est-17__form" id="est-17-form" role="search">
        <label class="est-17__label" for="est-17-q">Search the catalogue</label>
        <div class="est-17__row">
          <input class="est-17__input" type="search" id="est-17-q" name="q" value="tidal survey 1974" autocomplete="off"
                 aria-describedby="est-17-hint" aria-controls="est-17-results">
          <button class="est-17__go" type="submit">Search</button>
        </div>
        <p class="est-17__hint" id="est-17-hint">Type at least two characters. Results update when you press Search.</p>
      </form>

      <div class="est-17__vh" role="status" aria-live="polite" aria-atomic="true" id="est-17-live"></div>

      <section class="est-17__results" id="est-17-results" tabindex="-1" aria-labelledby="est-17-rh">
        <h2 class="est-17__rh" id="est-17-rh">Results</h2>

        <div class="est-17__empty" id="est-17-empty">
          <span class="est-17__glyph" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" focusable="false"><rect x="4" y="5" width="16" height="14" rx="2.2" stroke="currentColor" stroke-width="1.6"/><path d="M8 9.5h8M8 13h5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
          </span>
          <p class="est-17__eh">No catalogue entries for that phrase</p>
          <p class="est-17__ep">Sheet numbers are indexed without spaces, and surveys before 1980 are filed by county rather than year.</p>
          <ul class="est-17__tries">
            <li><button class="est-17__try" type="button" data-q="tidal survey">tidal survey</button></li>
            <li><button class="est-17__try" type="button" data-q="devon county 1974">devon county 1974</button></li>
            <li><button class="est-17__try" type="button" data-q="sheet 118">sheet 118</button></li>
          </ul>
        </div>

        <ol class="est-17__list" id="est-17-list" hidden></ol>
      </section>
    </main>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.est-17 {
  --bg: #f7f7f4;
  --surface: #ffffff;
  --sunk: #eff0eb;
  --line: #e4e5df;
  --line-2: #d1d2ca;
  --ink: #191a17;
  --muted: #585a53;
  --faint: #878980;
  --accent: #1f5c4d;
  --focus: #0b62d6;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  color-scheme: light;
  font-synthesis: none;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.est-17 *,
.est-17 *::before,
.est-17 *::after {
  box-sizing: border-box;
}

.est-17 [hidden] {
  display: none !important;
}

.est-17__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-17 {
    --bg: oklch(0.974 0.005 110);
    --surface: oklch(1 0 0);
    --sunk: oklch(0.955 0.006 110);
    --line: oklch(0.918 0.006 110);
    --line-2: oklch(0.858 0.008 110);
    --ink: oklch(0.19 0.008 120);
    --muted: oklch(0.465 0.01 120);
    --faint: oklch(0.615 0.011 120);
    --accent: oklch(0.4 0.075 168);
    --focus: oklch(0.52 0.19 258);
  }
}

.est-17__skip {
  position: absolute;
  inset-block-start: .5rem;
  inset-inline-start: .5rem;
  z-index: 9;
  translate: 0 -160%;
  padding: .6rem .9rem;
  font-size: .85rem;
  font-weight: 500;
  color: #fff;
  background: var(--accent);
  border-radius: 8px;
  text-decoration: none;
  transition: translate .18s ease;
}

.est-17__skip:focus-visible {
  translate: 0 0;
  outline: 3px solid var(--focus);
  outline-offset: 2px;
}

.est-17__shell {
  inline-size: min(60rem,100%);
  justify-self: center;
  display: grid;
  grid-template-rows: auto minmax(0,1fr);
  align-content: start;
}

.est-17__top {
  display: flex;
  flex-wrap: wrap;
  gap: .75rem 1.75rem;
  align-items: baseline;
  padding: 1.15rem clamp(1rem,3vw,2rem);
  border-block-end: 1px solid var(--line);
}

.est-17__brand {
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -.025em;
}

.est-17__nav {
  display: flex;
  gap: 1.15rem;
}

.est-17__nav a {
  font-size: .85rem;
  color: var(--muted);
  text-decoration: none;
  border-block-end: 1px solid transparent;
  transition: color .16s, border-color .16s;
}

.est-17__nav a:hover {
  color: var(--ink);
  border-color: var(--accent);
}

.est-17__main {
  padding: clamp(1.5rem,4vw,3rem) clamp(1rem,3vw,2rem);
  display: grid;
  gap: 1.5rem;
  align-content: start;
}

.est-17__form {
  display: grid;
  gap: .5rem;
  max-inline-size: 34rem;
}

.est-17__label {
  font-size: .9rem;
  font-weight: 600;
  letter-spacing: -.015em;
}

.est-17__row {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
}

.est-17__input {
  flex: 1 1 15rem;
  min-inline-size: 0;
  min-block-size: 2.9rem;
  padding: .7rem .9rem;
  font: inherit;
  font-size: .92rem;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--line-2);
  border-radius: 10px;
  outline: none;
}

.est-17__input:focus-visible {
  border-color: var(--focus);
  box-shadow: 0 0 0 3px color-mix(in oklab, var(--focus) 22%, transparent);
}

.est-17__go {
  min-block-size: 2.9rem;
  padding: .7rem 1.15rem;
  font: inherit;
  font-size: .88rem;
  font-weight: 500;
  cursor: pointer;
  color: #fff;
  background: var(--accent);
  border: 1px solid transparent;
  border-radius: 10px;
  transition: translate .16s, background .16s;
}

.est-17__go:hover {
  translate: 0 -1px;
  background: color-mix(in oklab, var(--accent) 88%, #000);
}

.est-17__hint {
  margin: 0;
  font-size: .8rem;
  color: var(--faint);
}

.est-17__results {
  display: grid;
  gap: 1rem;
}

.est-17__results:focus-visible {
  outline: 3px solid var(--focus);
  outline-offset: 6px;
  border-radius: 12px;
}

.est-17__rh {
  margin: 0;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .7rem;
  font-weight: 500;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--faint);
}

.est-17__empty {
  display: grid;
  justify-items: center;
  text-align: center;
  gap: .5rem;
  padding: clamp(2rem,6vh,3.25rem) 1.5rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 18px;
  box-shadow: 0 1px 2px rgba(25,26,23,.04);
  animation: est-17-in .45s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes est-17-in {
  from {
    opacity: 0;
    translate: 0 6px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.est-17__glyph {
  inline-size: 3.4rem;
  block-size: 3.4rem;
  display: grid;
  place-items: center;
  margin-block-end: .4rem;
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 8%, var(--surface));
  border-radius: 14px;
  box-shadow: 0 0 0 1px color-mix(in oklab, var(--accent) 18%, transparent);
}

.est-17__glyph svg {
  inline-size: 1.45rem;
  block-size: 1.45rem;
}

.est-17__eh {
  margin: 0;
  font-size: 1.08rem;
  font-weight: 600;
  letter-spacing: -.022em;
  text-wrap: balance;
}

.est-17__ep {
  margin: 0;
  max-inline-size: 48ch;
  font-size: .89rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.est-17__tries {
  margin: .9rem 0 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  justify-content: center;
}

.est-17__try {
  min-block-size: 2.6rem;
  padding: .6rem .9rem;
  font: inherit;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .8rem;
  cursor: pointer;
  color: var(--ink);
  background: var(--sunk);
  border: 1px solid var(--line-2);
  border-radius: 9px;
  transition: background .16s, border-color .16s;
}

.est-17__try:hover {
  background: color-mix(in oklab, var(--accent) 10%, var(--sunk));
  border-color: var(--accent);
}

.est-17__try:focus-visible,
.est-17__go:focus-visible,
.est-17__nav a:focus-visible {
  outline: 3px solid var(--focus);
  outline-offset: 2px;
}

.est-17__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .5rem;
}

.est-17__item {
  display: grid;
  gap: .25rem;
  padding: .9rem 1.05rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 13px;
  animation: est-17-in .4s cubic-bezier(.2,.7,.3,1) both;
}

.est-17__it {
  font-size: .93rem;
  font-weight: 500;
  letter-spacing: -.015em;
}

.est-17__im {
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .74rem;
  color: var(--faint);
}

@media (prefers-reduced-motion: reduce) {
  .est-17 *,
    .est-17 *::before,
    .est-17 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-17__empty,
    .est-17__item,
    .est-17__go,
    .est-17__try {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.est-17'); if(!root) return;
  var form = root.querySelector('#est-17-form'), input = root.querySelector('#est-17-q'),
      live = root.querySelector('#est-17-live'), empty = root.querySelector('#est-17-empty'),
      list = root.querySelector('#est-17-list'), results = root.querySelector('#est-17-results');
  var catalogue = [
    ['Tidal survey of the Exe estuary','SURV-1974-118 &middot; Devon &middot; 1974'],
    ['Coastal profile, Teignmouth to Dawlish','SURV-1974-121 &middot; Devon &middot; 1974'],
    ['Sheet 118, first edition','MAP-118-1 &middot; Devon &middot; 1969']
  ];
  function announce(msg){ live.textContent = ''; setTimeout(function(){ live.textContent = msg; }, 40); }
  function run(q){
    var term = q.trim().toLowerCase();
    var hits = term.length < 2 ? [] : catalogue.filter(function(r){
      return (r[0] + ' ' + r[1]).toLowerCase().replace(/&middot;/g,'').indexOf(term) > -1;
    });
    if(hits.length){
      empty.hidden = true; list.hidden = false;
      list.innerHTML = hits.map(function(r){
        return '<li class="est-17__item"><span class="est-17__it">' + r[0] + '</span><span class="est-17__im">' + r[1] + '</span></li>';
      }).join('');
      announce(hits.length + (hits.length === 1 ? ' entry found for ' : ' entries found for ') + q);
    } else {
      empty.hidden = false; list.hidden = true; list.innerHTML = '';
      announce('No catalogue entries for ' + q + '. Three suggested searches are listed.');
    }
    results.focus();
  }
  form.addEventListener('submit', function(e){ e.preventDefault(); run(input.value); });
  root.addEventListener('click', function(e){
    var t = e.target.closest('[data-q]'); if(!t) return;
    input.value = t.dataset.q; run(t.dataset.q);
  });
  announce('No catalogue entries for ' + input.value + '. Three suggested searches are listed.');
})();
```
