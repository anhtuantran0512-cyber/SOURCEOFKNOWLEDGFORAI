---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/404-page-not-found-layout/"
title: "404 Page Not Found Layout"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "A 404 for a publication rather than an app: an oversized serif numeral, an asymmetric two-column composition with a rule down the middle, and a working…"
has_js: "true"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 404 Page Not Found Layout
Source: https://codefronts.com/snippets/css-empty-states/404-page-not-found-layout/

A 404 for a publication rather than an app: an oversized serif numeral, an asymmetric two-column composition with a rule down the middle, and a working archive search that filters a real index as you type &mdash; including its own nested empty result. The right column carries the most-read list, because on an editorial site the best recovery from a dead link is another good story.
## HTML
```html
<div class="est-14">
  <header class="est-14__top">
    <a class="est-14__brand" href="#est-14">The Long Field</a>
    <nav class="est-14__nav" aria-label="Sections">
      <a href="#est-14">Reporting</a>
      <a href="#est-14">Essays</a>
      <a href="#est-14">Interviews</a>
      <a href="#est-14">Archive</a>
    </nav>
    <a class="est-14__sub" href="#est-14">Subscribe</a>
  </header>

  <main class="est-14__main">
    <div class="est-14__left">
      <p class="est-14__num" aria-hidden="true">404</p>
      <h1 class="est-14__h1">This page has been unwritten</h1>
      <p class="est-14__p">The link you followed points at something we moved during the archive rebuild. The writing still exists &mdash; it just lives at a different address now.</p>

      <form class="est-14__form" id="est-14-form" role="search">
        <label class="est-14__flabel" for="est-14-input">Search the archive</label>
        <div class="est-14__frow">
          <input class="est-14__input" type="search" id="est-14-input" placeholder="A title, a name, a year" autocomplete="off">
          <button class="est-14__go" type="submit">Search</button>
        </div>
        <ul class="est-14__sugg" id="est-14-sugg" hidden></ul>
      </form>
    </div>

    <aside class="est-14__right">
      <p class="est-14__rlabel">Most read this month</p>
      <ol class="est-14__reads">
        <li><a href="#est-14"><span class="est-14__rk">Reporting</span><span class="est-14__rt">The village that bought its own grid</span></a></li>
        <li><a href="#est-14"><span class="est-14__rk">Essay</span><span class="est-14__rt">In defence of the slow newsroom</span></a></li>
        <li><a href="#est-14"><span class="est-14__rk">Interview</span><span class="est-14__rt">Forty years of tidal charts, by hand</span></a></li>
        <li><a href="#est-14"><span class="est-14__rk">Archive</span><span class="est-14__rt">What the 1998 floods taught the coast</span></a></li>
      </ol>
    </aside>
  </main>

  <footer class="est-14__foot">
    <span>Established 1974</span>
    <a href="#est-14">Contact the desk</a>
  </footer>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Instrument+Serif:ital@0;1&display=swap');

.est-14 {
  --paper: #f4f1ea;
  --card: #fdfcf8;
  --sunk: #eae5db;
  --line: #ddd6c9;
  --line-2: #c7bdac;
  --ink: #1d1b17;
  --muted: #5f5a51;
  --faint: #8d877c;
  --accent: #8a3f2c;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: auto minmax(0,1fr) auto;
  box-sizing: border-box;
  background: var(--paper);
  color: var(--ink);
  color-scheme: light;
  font-synthesis: none;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.est-14 *,
.est-14 *::before,
.est-14 *::after {
  box-sizing: border-box;
}

.est-14 [hidden] {
  display: none !important;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-14 {
    --paper: oklch(0.952 0.012 85);
    --card: oklch(0.99 0.006 85);
    --sunk: oklch(0.912 0.017 82);
    --line: oklch(0.872 0.021 82);
    --line-2: oklch(0.788 0.028 80);
    --ink: oklch(0.205 0.012 60);
    --muted: oklch(0.455 0.014 60);
    --faint: oklch(0.605 0.015 62);
    --accent: oklch(0.45 0.115 38);
  }
}

.est-14__top {
  display: flex;
  flex-wrap: wrap;
  gap: .75rem 1.75rem;
  align-items: baseline;
  padding: 1.15rem clamp(1rem,4vw,3.5rem);
  border-block-end: 1px solid var(--ink);
}

.est-14__brand {
  font-family: 'Instrument Serif',Georgia,serif;
  font-size: 1.5rem;
  letter-spacing: -.015em;
  color: var(--ink);
  text-decoration: none;
}

.est-14__nav {
  display: flex;
  flex-wrap: wrap;
  gap: 1.2rem;
}

.est-14__nav a {
  font-size: .84rem;
  letter-spacing: .01em;
  color: var(--muted);
  text-decoration: none;
  transition: color .16s;
}

.est-14__nav a:hover {
  color: var(--accent);
}

.est-14__sub {
  margin-inline-start: auto;
  font-size: .84rem;
  font-weight: 500;
  color: var(--accent);
  text-decoration: none;
  border-block-end: 1px solid var(--accent);
}

.est-14__main {
  inline-size: min(74rem,100%);
  justify-self: center;
  padding: clamp(1.75rem,5vw,4.5rem) clamp(1rem,4vw,3.5rem);
  display: grid;
  gap: clamp(1.75rem,5vw,4rem);
  grid-template-columns: minmax(0,1.65fr) minmax(0,1fr);
  align-items: start;
}

.est-14__left {
  min-inline-size: 0;
  display: grid;
  gap: .85rem;
  animation: est-14-in .6s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes est-14-in {
  from {
    opacity: 0;
    translate: 0 10px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.est-14__num {
  margin: 0;
  font-family: 'Instrument Serif',Georgia,serif;
  font-size: clamp(5rem,17vw,11rem);
  line-height: .78;
  letter-spacing: -.05em;
  color: var(--accent);
  opacity: .9;
}

.est-14__h1 {
  margin: .35rem 0 0;
  font-family: 'Instrument Serif',Georgia,serif;
  font-size: clamp(1.85rem,4.6vw,3rem);
  font-weight: 400;
  line-height: 1.03;
  letter-spacing: -.02em;
  text-wrap: balance;
  max-inline-size: 26ch;
}

.est-14__p {
  margin: 0;
  max-inline-size: 52ch;
  font-size: 1rem;
  line-height: 1.68;
  color: var(--muted);
  text-wrap: pretty;
}

.est-14__form {
  margin-block-start: 1.25rem;
  display: grid;
  gap: .55rem;
  max-inline-size: 32rem;
}

.est-14__flabel {
  font-family: 'Instrument Serif',Georgia,serif;
  font-style: italic;
  font-size: 1rem;
  color: var(--faint);
}

.est-14__frow {
  display: flex;
  gap: .5rem;
  flex-wrap: wrap;
}

.est-14__input {
  flex: 1 1 14rem;
  min-inline-size: 0;
  min-block-size: 3rem;
  padding: .75rem .9rem;
  font: inherit;
  font-size: .95rem;
  color: var(--ink);
  background: var(--card);
  border: 1px solid var(--line-2);
  border-radius: 2px;
  outline: none;
}

.est-14__input::placeholder {
  color: var(--faint);
}

.est-14__input:focus-visible {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklab, var(--accent) 14%, transparent);
}

.est-14__go {
  min-block-size: 3rem;
  padding: .75rem 1.25rem;
  font: inherit;
  font-size: .9rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--card);
  background: var(--ink);
  border: 1px solid var(--ink);
  border-radius: 2px;
  transition: background .18s;
}

.est-14__go:hover {
  background: var(--accent);
  border-color: var(--accent);
}

.est-14__go:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.est-14__sugg {
  margin: .35rem 0 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .15rem;
  border-block-start: 1px solid var(--line);
}

.est-14__sugg li {
  padding: .55rem .1rem;
  border-block-end: 1px solid var(--line);
  font-size: .9rem;
  color: var(--muted);
  animation: est-14-in .3s ease both;
}

.est-14__sugg li b {
  font-weight: 500;
  color: var(--ink);
}

.est-14__sugg li span {
  font-family: 'Instrument Serif',Georgia,serif;
  font-style: italic;
  color: var(--faint);
  font-size: .85rem;
  margin-inline-start: .4rem;
}

.est-14__right {
  min-inline-size: 0;
  display: grid;
  gap: .75rem;
  align-content: start;
  padding-inline-start: clamp(0rem,2vw,1.5rem);
  border-inline-start: 1px solid var(--line);
}

.est-14__rlabel {
  margin: 0;
  font-family: 'Geist',sans-serif;
  font-size: .72rem;
  font-weight: 500;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--faint);
}

.est-14__reads {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  counter-reset: est14;
}

.est-14__reads li {
  counter-increment: est14;
  border-block-end: 1px solid var(--line);
}

.est-14__reads a {
  display: grid;
  gap: .25rem;
  padding: .85rem 0;
  text-decoration: none;
  transition: padding-inline-start .2s ease;
}

.est-14__reads a::before {
  content: counter(est14, decimal-leading-zero);
  font-family: 'Geist',sans-serif;
  font-size: .7rem;
  letter-spacing: .1em;
  color: var(--accent);
}

.est-14__reads a:hover {
  padding-inline-start: .4rem;
}

.est-14__rk {
  font-size: .72rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--faint);
}

.est-14__rt {
  font-family: 'Instrument Serif',Georgia,serif;
  font-size: 1.12rem;
  line-height: 1.25;
  color: var(--ink);
}

.est-14__reads a:hover .est-14__rt {
  color: var(--accent);
}

.est-14__foot {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem 1.5rem;
  justify-content: space-between;
  padding: 1.1rem clamp(1rem,4vw,3.5rem);
  border-block-start: 1px solid var(--line);
  font-size: .8rem;
  color: var(--faint);
}

.est-14__foot a {
  color: var(--muted);
  text-decoration: none;
  border-block-end: 1px solid var(--line-2);
}

.est-14__foot a:hover {
  color: var(--accent);
  border-color: var(--accent);
}

@media (max-width: 760px) {
  .est-14__main {
    grid-template-columns: 1fr;
  }

  .est-14__right {
    padding-inline-start: 0;
    border-inline-start: 0;
    border-block-start: 1px solid var(--line);
    padding-block-start: 1.25rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .est-14 *,
    .est-14 *::before,
    .est-14 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-14__input,
    .est-14__go {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.est-14'); if(!root) return;
  var form = root.querySelector('#est-14-form'), input = root.querySelector('#est-14-input'), sugg = root.querySelector('#est-14-sugg');
  var index = [
    ['The village that bought its own grid','Reporting, 2026'],
    ['In defence of the slow newsroom','Essay, 2025'],
    ['Forty years of tidal charts, by hand','Interview, 2024'],
    ['What the 1998 floods taught the coast','Archive, 1998'],
    ['The last printing press in the county','Reporting, 2023']
  ];
  function render(q){
    var term = q.trim().toLowerCase();
    if(!term){ sugg.hidden = true; sugg.innerHTML = ''; return; }
    var hits = index.filter(function(r){ return r[0].toLowerCase().indexOf(term) > -1 || r[1].toLowerCase().indexOf(term) > -1; });
    sugg.hidden = false;
    sugg.innerHTML = hits.length
      ? hits.map(function(r){ return '<li><b>' + r[0] + '</b><span>' + r[1] + '</span></li>'; }).join('')
      : '<li><b>Nothing in the archive matches that</b><span>try a year, or a reporter name</span></li>';
  }
  input.addEventListener('input', function(){ render(input.value); });
  form.addEventListener('submit', function(e){ e.preventDefault(); render(input.value); });
})();
```
