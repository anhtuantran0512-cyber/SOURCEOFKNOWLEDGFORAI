---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/filtered-list-no-matches-state/"
title: "Filtered List No Matches State"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "Filtering with zero JavaScript: three facet checkboxes over a five-person hiring pipeline, and an inline empty card that appears only for the combination…"
has_js: "false"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Filtered List No Matches State
Source: https://codefronts.com/snippets/css-empty-states/filtered-list-no-matches-state/

Filtering with zero JavaScript: three facet checkboxes over a five-person hiring pipeline, and an inline empty card that appears only for the combination that genuinely returns nothing &mdash; senior plus design &mdash; driven entirely by chained :has() on the form root.
## HTML
```html
<div class="est-06">
  <form class="est-06__q" id="est-06-form">
    <aside class="est-06__filters">
      <p class="est-06__flabel">Pipeline filters</p>
      <fieldset class="est-06__group">
        <legend>Seniority</legend>
        <label class="est-06__f"><input type="checkbox" id="est-06-senior"><span class="est-06__box" aria-hidden="true"></span>Senior only</label>
      </fieldset>
      <fieldset class="est-06__group">
        <legend>Discipline</legend>
        <label class="est-06__f"><input type="checkbox" id="est-06-design"><span class="est-06__box" aria-hidden="true"></span>Design</label>
      </fieldset>
      <fieldset class="est-06__group">
        <legend>Location</legend>
        <label class="est-06__f"><input type="checkbox" id="est-06-remote"><span class="est-06__box" aria-hidden="true"></span>Remote</label>
      </fieldset>
      <button class="est-06__clear" type="reset">Clear all</button>
    </aside>

    <section class="est-06__pane">
      <header class="est-06__phead">
        <h1 class="est-06__h1">Product engineering &mdash; open pipeline</h1>
        <div class="est-06__chips">
          <label class="est-06__chip" for="est-06-senior" data-for="senior">Senior only</label>
          <label class="est-06__chip" for="est-06-design" data-for="design">Design</label>
          <label class="est-06__chip" for="est-06-remote" data-for="remote">Remote</label>
        </div>
      </header>

      <ul class="est-06__list">
        <li class="est-06__item" data-level="senior" data-team="eng" data-loc="remote">
          <span class="est-06__ava" aria-hidden="true">AK</span>
          <span class="est-06__imain"><span class="est-06__iname">Ana Kowalski</span><span class="est-06__imeta">Staff engineer &middot; Remote, Lisbon</span></span>
          <span class="est-06__stage">Onsite loop</span>
        </li>
        <li class="est-06__item" data-level="mid" data-team="eng" data-loc="onsite">
          <span class="est-06__ava" aria-hidden="true">BT</span>
          <span class="est-06__imain"><span class="est-06__iname">Ben Tran</span><span class="est-06__imeta">Backend engineer &middot; Berlin office</span></span>
          <span class="est-06__stage">Tech screen</span>
        </li>
        <li class="est-06__item" data-level="senior" data-team="eng" data-loc="onsite">
          <span class="est-06__ava" aria-hidden="true">CN</span>
          <span class="est-06__imain"><span class="est-06__iname">Chi Nakamura</span><span class="est-06__imeta">Senior platform engineer &middot; Berlin office</span></span>
          <span class="est-06__stage">Offer drafted</span>
        </li>
        <li class="est-06__item" data-level="mid" data-team="design" data-loc="remote">
          <span class="est-06__ava" aria-hidden="true">DO</span>
          <span class="est-06__imain"><span class="est-06__iname">Dee Osei</span><span class="est-06__imeta">Product designer &middot; Remote, Accra</span></span>
          <span class="est-06__stage">Portfolio review</span>
        </li>
        <li class="est-06__item" data-level="junior" data-team="design" data-loc="onsite">
          <span class="est-06__ava" aria-hidden="true">EL</span>
          <span class="est-06__imain"><span class="est-06__iname">Eli Lindqvist</span><span class="est-06__imeta">Junior designer &middot; Stockholm office</span></span>
          <span class="est-06__stage">Intro call</span>
        </li>
      </ul>

      <div class="est-06__empty">
        <span class="est-06__glyph" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M4 6h16M7 12h10M10 18h4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><path d="M3 3l18 18" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
        </span>
        <p class="est-06__eh">No senior designers in this pipeline</p>
        <p class="est-06__ep">Senior design roles are handled by the brand team. Drop one filter to see the rest.</p>
        <div class="est-06__eacts">
          <label class="est-06__drop" for="est-06-design">Drop the design filter</label>
          <label class="est-06__drop est-06__drop--alt" for="est-06-senior">Drop senior only</label>
        </div>
      </div>
    </section>
  </form>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.est-06 {
  --bg: #fafaf9;
  --surface: #ffffff;
  --sunk: #f2f3f2;
  --line: #e4e6e4;
  --line-2: #d3d6d3;
  --ink: #15181a;
  --muted: #585d61;
  --faint: #888e92;
  --accent: #155e63;
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

.est-06 *,
.est-06 *::before,
.est-06 *::after {
  box-sizing: border-box;
}

.est-06 [hidden] {
  display: none !important;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-06 {
    --bg: oklch(0.982 0.003 130);
    --surface: oklch(1 0 0);
    --sunk: oklch(0.962 0.004 150);
    --line: oklch(0.918 0.005 150);
    --line-2: oklch(0.868 0.007 150);
    --ink: oklch(0.185 0.008 200);
    --muted: oklch(0.46 0.011 200);
    --faint: oklch(0.62 0.012 200);
    --accent: oklch(0.42 0.075 200);
  }
}

.est-06__q {
  inline-size: min(74rem,100%);
  justify-self: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(1.25rem,4vw,3rem) clamp(1rem,3vw,2rem);
  display: grid;
  gap: clamp(1rem,3vw,2.25rem);
  grid-template-columns: minmax(0,15rem) minmax(0,1fr);
  align-content: start;
  align-items: start;
}

.est-06__filters {
  display: grid;
  gap: 1.1rem;
  align-content: start;
  padding: 1.15rem 1.1rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 16px;
  box-shadow: 0 1px 2px rgba(20,24,26,.04);
}

.est-06__flabel {
  margin: 0;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .68rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--faint);
}

.est-06__group {
  margin: 0;
  padding: 0;
  border: 0;
  display: grid;
  gap: .5rem;
}

.est-06__group legend {
  padding: 0;
  font-size: .78rem;
  font-weight: 500;
  color: var(--faint);
}

.est-06__f {
  display: flex;
  align-items: center;
  gap: .6rem;
  font-size: .88rem;
  cursor: pointer;
  color: var(--ink);
}

.est-06__f input {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

.est-06__box {
  position: relative;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  flex: none;
  border: 1.5px solid var(--line-2);
  border-radius: 5px;
  background: var(--surface);
  transition: background .18s, border-color .18s;
}

.est-06__box::after {
  content: '';
  position: absolute;
  inset-block-start: .16rem;
  inset-inline-start: .3rem;
  inline-size: .42rem;
  block-size: .22rem;
  border-inline-start: 2px solid #fff;
  border-block-end: 2px solid #fff;
  rotate: -45deg;
  opacity: 0;
  transition: opacity .16s;
}

.est-06__f input:checked + .est-06__box {
  background: var(--accent);
  border-color: var(--accent);
}

.est-06__f input:checked + .est-06__box::after {
  opacity: 1;
}

.est-06__f input:focus-visible + .est-06__box {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.est-06__clear {
  justify-self: start;
  padding: .5rem .8rem;
  min-block-size: 2.5rem;
  display: inline-flex;
  align-items: center;
  cursor: pointer;
  font-size: .82rem;
  font-weight: 500;
  color: var(--ink);
  background: var(--sunk);
  border: 1px solid var(--line);
  border-radius: 9px;
  transition: background .16s;
}

.est-06__clear:hover {
  background: var(--line);
}

.est-06__clear {
  font: inherit;
}

.est-06__clear:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.est-06__pane {
  min-inline-size: 0;
  display: grid;
  gap: 1rem;
  align-content: start;
}

.est-06__phead {
  display: grid;
  gap: .7rem;
}

.est-06__h1 {
  margin: 0;
  font-size: clamp(1.25rem,2.8vw,1.7rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.15;
  text-wrap: balance;
}

.est-06__chips {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
  min-block-size: 1.9rem;
}

.est-06__chip {
  display: none;
  align-items: center;
  gap: .4rem;
  padding: .3rem .6rem;
  cursor: pointer;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .72rem;
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 8%, var(--surface));
  border: 1px solid color-mix(in oklab, var(--accent) 25%, transparent);
  border-radius: 7px;
}

.est-06__chip::after {
  content: 'x';
  font-size: .7rem;
  opacity: .6;
}

.est-06__q:has(#est-06-senior:checked) .est-06__chip[data-for="senior"],
.est-06__q:has(#est-06-design:checked) .est-06__chip[data-for="design"],
.est-06__q:has(#est-06-remote:checked) .est-06__chip[data-for="remote"] {
  display: inline-flex;
}

.est-06__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .5rem;
}

.est-06__item {
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto;
  gap: .25rem .8rem;
  align-items: center;
  padding: .85rem 1rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 13px;
  transition: border-color .16s, translate .16s, box-shadow .2s;
}

.est-06__item:hover {
  border-color: var(--line-2);
  translate: 0 -1px;
  box-shadow: 0 14px 26px -24px rgba(20,24,26,.6);
}

.est-06__ava {
  inline-size: 2.15rem;
  block-size: 2.15rem;
  display: grid;
  place-items: center;
  border-radius: 50%;
  font-size: .72rem;
  font-weight: 600;
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 10%, var(--surface));
  box-shadow: inset 0 0 0 1px color-mix(in oklab, var(--accent) 20%, transparent);
}

.est-06__imain {
  min-inline-size: 0;
  display: grid;
  gap: .15rem;
}

.est-06__iname {
  font-size: .92rem;
  font-weight: 500;
  letter-spacing: -.015em;
}

.est-06__imeta {
  font-size: .78rem;
  color: var(--faint);
}

.est-06__stage {
  padding: .25rem .55rem;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .68rem;
  color: var(--muted);
  background: var(--sunk);
  border: 1px solid var(--line);
  border-radius: 6px;
  white-space: nowrap;
}

.est-06__q:has(#est-06-senior:checked) .est-06__item:not([data-level="senior"]) {
  display: none;
}

.est-06__q:has(#est-06-design:checked) .est-06__item:not([data-team="design"]) {
  display: none;
}

.est-06__q:has(#est-06-remote:checked) .est-06__item:not([data-loc="remote"]) {
  display: none;
}

.est-06__empty {
  display: none;
  justify-items: center;
  text-align: center;
  gap: .45rem;
  padding: clamp(2rem,7vh,3.5rem) 1.5rem;
  background: var(--surface);
  border: 1px dashed var(--line-2);
  border-radius: 18px;
  background-image: radial-gradient(color-mix(in oklab, var(--line-2) 60%, transparent) .7px, transparent .7px);
  background-size: 16px 16px;
  animation: est-06-in .45s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes est-06-in {
  from {
    opacity: 0;
    scale: .985;
  }

  to {
    opacity: 1;
    scale: 1;
  }
}

.est-06__q:has(#est-06-senior:checked):has(#est-06-design:checked) .est-06__empty {
  display: grid;
}

.est-06__q:has(#est-06-senior:checked):has(#est-06-design:checked) .est-06__list {
  display: none;
}

.est-06__glyph {
  inline-size: 3.4rem;
  block-size: 3.4rem;
  display: grid;
  place-items: center;
  margin-block-end: .5rem;
  color: var(--accent);
  background: var(--surface);
  border: 1px solid color-mix(in oklab, var(--accent) 20%, var(--line));
  border-radius: 50%;
}

.est-06__glyph svg {
  inline-size: 1.4rem;
  block-size: 1.4rem;
}

.est-06__eh {
  margin: 0;
  font-size: 1.05rem;
  font-weight: 600;
  letter-spacing: -.022em;
  text-wrap: balance;
}

.est-06__ep {
  margin: 0;
  max-inline-size: 42ch;
  font-size: .88rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.est-06__eacts {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  justify-content: center;
  margin-block-start: .9rem;
}

.est-06__drop {
  min-block-size: 2.75rem;
  display: inline-flex;
  align-items: center;
  padding: .65rem 1rem;
  cursor: pointer;
  font-size: .85rem;
  font-weight: 500;
  color: #fff;
  background: var(--accent);
  border: 1px solid transparent;
  border-radius: 11px;
  transition: translate .16s, background .16s;
}

.est-06__drop:hover {
  translate: 0 -1px;
  background: color-mix(in oklab, var(--accent) 88%, #000);
}

.est-06__drop--alt {
  color: var(--ink);
  background: var(--surface);
  border-color: var(--line-2);
}

.est-06__drop--alt:hover {
  background: var(--sunk);
}

@media (max-width: 820px) {
  .est-06__q {
    grid-template-columns: 1fr;
  }

  .est-06__filters {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: .9rem 1.25rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .est-06 *,
    .est-06 *::before,
    .est-06 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-06__item,
    .est-06__empty,
    .est-06__drop,
    .est-06__filters {
    border-color: CanvasText;
  }
}
```
