---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/carbon-shelves/"
title: "Carbon Shelves Dark Mode File List"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "A file browser in the dark: folder tree, sortable column headers, alternating row tints derived with color-mix() rather than two hard-coded greys, and a…"
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Carbon Shelves Dark Mode File List
Source: https://codefronts.com/design-styles/css-dark-mode-ui/carbon-shelves/

A file browser in the dark: folder tree, sortable column headers, alternating row tints derived with color-mix() rather than two hard-coded greys, and a selected row marked by an accent edge plus a checked box — never colour alone. Row density, hover feedback and focus rings are all tuned for the case that actually happens: forty rows, scanned quickly, on a dim screen.
## HTML
```html
<div class="dmu-18">
  <div class="dmu-18__stage">
    <div class="dmu-18__app">
      <aside class="dmu-18__tree" aria-label="Folders">
        <p class="dmu-18__treeTitle">Shelves</p>
        <button class="dmu-18__folder dmu-18__folder--active" type="button" aria-current="true">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3.6 6.4h5.6l1.6 2.2h9.6v9.8H3.6Z"/></svg>
          Design system<span>128</span></button>
        <button class="dmu-18__folder" type="button">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3.6 6.4h5.6l1.6 2.2h9.6v9.8H3.6Z"/></svg>
          Brand<span>46</span></button>
        <button class="dmu-18__folder" type="button">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3.6 6.4h5.6l1.6 2.2h9.6v9.8H3.6Z"/></svg>
          Research<span>17</span></button>
        <button class="dmu-18__folder" type="button">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3.6 6.4h5.6l1.6 2.2h9.6v9.8H3.6Z"/></svg>
          Archive<span>904</span></button>
      </aside>

      <section class="dmu-18__main" aria-label="Files">
        <header class="dmu-18__bar">
          <div class="dmu-18__crumbs">Design system <span aria-hidden="true">/</span> tokens</div>
          <div class="dmu-18__barTools">
            <span class="dmu-18__count">4 of 128 selected</span>
            <input class="dmu-18__sr" type="checkbox" id="dmu-18-toggle">
            <label class="dmu-18__toggle" for="dmu-18-toggle">
              <svg class="dmu-18__sun" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2.8v2M12 19.2v2M2.8 12h2M19.2 12h2M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
              <svg class="dmu-18__moon" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.4A8.4 8.4 0 0 1 9.6 4a8.4 8.4 0 1 0 10.4 10.4Z"/></svg>
              <span class="dmu-18__sr">Toggle theme</span>
            </label>
          </div>
        </header>

        <div class="dmu-18__table" role="table">
          <div class="dmu-18__head" role="row">
            <span class="dmu-18__headCell" role="columnheader"><span class="dmu-18__sr">Select</span></span>
            <button class="dmu-18__sort" type="button" role="columnheader" aria-sort="ascending">Name
              <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 14l5-5 5 5"/></svg></button>
            <button class="dmu-18__sort" type="button" role="columnheader">Size</button>
            <button class="dmu-18__sort" type="button" role="columnheader">Modified</button>
            <button class="dmu-18__sort" type="button" role="columnheader">Owner</button>
          </div>

          <label class="dmu-18__row" role="row">
            <input type="checkbox" checked>
            <span class="dmu-18__box" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg></span>
            <span class="dmu-18__name"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 3.5h7l4.5 4.5v12H6.5Z"/><path d="M13.5 3.5V8H18"/></svg>theme.css</span>
            <span class="dmu-18__num">18.4 KB</span>
            <span class="dmu-18__num">14 Aug 09:12</span>
            <span class="dmu-18__owner">Alex Chen</span>
          </label>

          <label class="dmu-18__row" role="row">
            <input type="checkbox" checked>
            <span class="dmu-18__box" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg></span>
            <span class="dmu-18__name"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 3.5h7l4.5 4.5v12H6.5Z"/><path d="M13.5 3.5V8H18"/></svg>tokens.dark.json</span>
            <span class="dmu-18__num">6.1 KB</span>
            <span class="dmu-18__num">13 Aug 17:48</span>
            <span class="dmu-18__owner">Priya Sharma</span>
          </label>

          <label class="dmu-18__row" role="row">
            <input type="checkbox">
            <span class="dmu-18__box" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg></span>
            <span class="dmu-18__name"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 3.5h7l4.5 4.5v12H6.5Z"/><path d="M13.5 3.5V8H18"/></svg>App.tsx</span>
            <span class="dmu-18__num">24.9 KB</span>
            <span class="dmu-18__num">13 Aug 11:02</span>
            <span class="dmu-18__owner">Jordan Lee</span>
          </label>

          <label class="dmu-18__row" role="row">
            <input type="checkbox">
            <span class="dmu-18__box" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg></span>
            <span class="dmu-18__name"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 3.5h7l4.5 4.5v12H6.5Z"/><path d="M13.5 3.5V8H18"/></svg>next.config.mjs</span>
            <span class="dmu-18__num">1.8 KB</span>
            <span class="dmu-18__num">12 Aug 20:31</span>
            <span class="dmu-18__owner">Sam Rivera</span>
          </label>

          <label class="dmu-18__row" role="row">
            <input type="checkbox">
            <span class="dmu-18__box" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg></span>
            <span class="dmu-18__name"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 3.5h7l4.5 4.5v12H6.5Z"/><path d="M13.5 3.5V8H18"/></svg>package.json</span>
            <span class="dmu-18__num">3.4 KB</span>
            <span class="dmu-18__num">12 Aug 08:55</span>
            <span class="dmu-18__owner">Alex Chen</span>
          </label>

          <label class="dmu-18__row" role="row">
            <input type="checkbox">
            <span class="dmu-18__box" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg></span>
            <span class="dmu-18__name"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 3.5h7l4.5 4.5v12H6.5Z"/><path d="M13.5 3.5V8H18"/></svg>contrast-audit.mjs</span>
            <span class="dmu-18__num">9.2 KB</span>
            <span class="dmu-18__num">11 Aug 15:20</span>
            <span class="dmu-18__owner">Priya Sharma</span>
          </label>
        </div>
      </section>
    </div>
  </div>
</div>
```
## CSS
```css
.dmu-18 {
  --bg: #08090b;
  --surface: #101216;
  --toolbar: #0c0e12;
  --tree: #0b0d11;
  --ink: #eceef2;
  --muted: #8b93a1;
  --line: #1f232b;
  --hover: #181c22;
  --selected: #171d27;
  --accent: #5eead4;
  --accent-ink: #03211c;
  --focus: #99f6e4;
  --shadow: rgba(0,0,0,.7);
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"SF Mono","JetBrains Mono",Menlo,monospace;
  color-scheme: dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.dmu-18[data-theme="light"],
.dmu-18:has(#dmu-18-toggle:checked) {
  --bg: #eef0f3;
  --surface: #ffffff;
  --toolbar: #f8f9fb;
  --tree: #f4f5f8;
  --ink: #0d0f14;
  --muted: #5b6270;
  --line: #e2e5ea;
  --hover: #f2f4f7;
  --selected: #eaf7f4;
  --accent: #0f766e;
  --accent-ink: #ffffff;
  --focus: #0f766e;
  --shadow: rgba(13,15,20,.16);
  color-scheme: light;
}

@media (prefers-color-scheme: light) {
  .dmu-18:not([data-theme="dark"]):not(:has(#dmu-18-toggle:checked)) {
    --bg: #eef0f3;
    --surface: #ffffff;
    --toolbar: #f8f9fb;
    --tree: #f4f5f8;
    --ink: #0d0f14;
    --muted: #5b6270;
    --line: #e2e5ea;
    --hover: #f2f4f7;
    --selected: #eaf7f4;
    --accent: #0f766e;
    --accent-ink: #ffffff;
    --focus: #0f766e;
    --shadow: rgba(13,15,20,.16);
    color-scheme: light;
  }
  /* flip-back: light OS + checked restores the carbon base */

  .dmu-18:has(#dmu-18-toggle:checked) {
    --bg: #08090b;
    --surface: #101216;
    --toolbar: #0c0e12;
    --tree: #0b0d11;
    --ink: #eceef2;
    --muted: #8b93a1;
    --line: #1f232b;
    --hover: #181c22;
    --selected: #171d27;
    --accent: #5eead4;
    --accent-ink: #03211c;
    --focus: #99f6e4;
    --shadow: rgba(0,0,0,.7);
    color-scheme: dark;
  }
}

.dmu-18,
.dmu-18 *,
.dmu-18 *::before,
.dmu-18 *::after {
  box-sizing: border-box;
}

.dmu-18__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.dmu-18__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(.75rem,3.5vw,2.75rem);
}

.dmu-18__app {
  width: min(74rem,100%);
  display: grid;
  grid-template-columns: 1fr;
  border-radius: 1.1rem;
  overflow: hidden;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 40px 76px -50px var(--shadow);
}

@media (min-width: 56rem) {
  .dmu-18__app {
    grid-template-columns: 14rem 1fr;
  }
}

.dmu-18__tree {
  padding: .85rem .7rem;
  background: var(--tree);
  border-bottom: 1px solid var(--line);
  display: grid;
  gap: .15rem;
  align-content: start;
}

@media (min-width: 56rem) {
  .dmu-18__tree {
    border-bottom: 0;
    border-right: 1px solid var(--line);
  }
}

.dmu-18__treeTitle {
  margin: .1rem .5rem .5rem;
  font-size: .68rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.dmu-18__folder {
  display: flex;
  align-items: center;
  gap: .5rem;
  min-height: 2.5rem;
  padding: 0 .6rem;
  border: 0;
  border-radius: .55rem;
  cursor: pointer;
  font: inherit;
  font-size: .83rem;
  text-align: left;
  background: transparent;
  color: var(--muted);
  transition: background-color .16s ease, color .16s ease;
}

.dmu-18__folder svg {
  width: 1.05rem;
  height: 1.05rem;
  flex: none;
}

.dmu-18__folder span {
  margin-left: auto;
  font-family: var(--mono);
  font-size: .7rem;
  font-variant-numeric: tabular-nums;
}

.dmu-18__folder:hover {
  background: var(--hover);
  color: var(--ink);
}

.dmu-18__folder:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: -2px;
}

.dmu-18__folder--active {
  background: var(--hover);
  color: var(--ink);
}

.dmu-18__folder--active svg {
  color: var(--accent);
}

.dmu-18__main {
  display: grid;
  grid-template-rows: auto 1fr;
  min-width: 0;
}

.dmu-18__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  padding: .7rem .9rem;
  background: var(--toolbar);
  border-bottom: 1px solid var(--line);
}

.dmu-18__crumbs {
  display: flex;
  gap: .4rem;
  font-family: var(--mono);
  font-size: .75rem;
  color: var(--muted);
}

.dmu-18__barTools {
  display: flex;
  align-items: center;
  gap: .6rem;
}

.dmu-18__count {
  font-size: .75rem;
  color: var(--muted);
}

.dmu-18__toggle {
  display: grid;
  place-items: center;
  width: 2.4rem;
  height: 2.4rem;
  border-radius: .6rem;
  cursor: pointer;
  background: var(--surface);
  color: var(--ink);
  border: 1px solid var(--line);
  transition: background-color .18s ease;
}

.dmu-18__toggle:hover {
  background: var(--hover);
}

.dmu-18__toggle svg {
  width: 1.05rem;
  height: 1.05rem;
}

.dmu-18__sun {
  display: none;
}

.dmu-18__moon {
  display: block;
}

.dmu-18:has(#dmu-18-toggle:checked) .dmu-18__sun {
  display: block;
}

.dmu-18:has(#dmu-18-toggle:checked) .dmu-18__moon {
  display: none;
}

@media (prefers-color-scheme: light) {
  .dmu-18:not(:has(#dmu-18-toggle:checked)) .dmu-18__sun {
    display: block;
  }

  .dmu-18:not(:has(#dmu-18-toggle:checked)) .dmu-18__moon {
    display: none;
  }

  .dmu-18:has(#dmu-18-toggle:checked) .dmu-18__sun {
    display: none;
  }

  .dmu-18:has(#dmu-18-toggle:checked) .dmu-18__moon {
    display: block;
  }
}

.dmu-18:has(#dmu-18-toggle:focus-visible) .dmu-18__toggle {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-18__table {
  --cols: 2.5rem minmax(9rem,1fr) 6rem 8.5rem 8rem;
  display: grid;
  align-content: start;
}

@media (max-width: 46rem) {
  .dmu-18__table {
    --cols: 2.5rem 1fr 6rem;
  }

  .dmu-18__head > *:nth-child(4),
    .dmu-18__head > *:nth-child(5),
    .dmu-18__row > *:nth-child(5),
    .dmu-18__row > *:nth-child(6) {
    display: none;
  }
}

.dmu-18__head {
  display: grid;
  grid-template-columns: var(--cols);
  border-bottom: 1px solid var(--line);
}

.dmu-18__headCell {
  display: block;
  min-height: 2.5rem;
}

.dmu-18__sort {
  display: flex;
  align-items: center;
  gap: .3rem;
  min-height: 2.5rem;
  padding: 0 .65rem;
  border: 0;
  background: transparent;
  color: var(--muted);
  font: inherit;
  font-size: .72rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  cursor: pointer;
  text-align: left;
}

.dmu-18__sort svg {
  width: .85rem;
  height: .85rem;
  color: var(--accent);
}

.dmu-18__sort:hover {
  color: var(--ink);
}

.dmu-18__sort:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: -2px;
}

.dmu-18__row {
  position: relative;
  display: grid;
  grid-template-columns: var(--cols);
  align-items: center;
  min-height: 2.9rem;
  cursor: pointer;
  border-bottom: 1px solid var(--line);
  transition: background-color .16s ease;
}

.dmu-18__row:nth-child(even) {
  background: color-mix(in oklab,var(--surface),var(--ink) 3%);
}

.dmu-18__row:hover {
  background: var(--hover);
}

.dmu-18__row:has(input:checked) {
  background: var(--selected);
}

.dmu-18__row:has(input:checked)::before {
  content: '';
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  width: 2px;
  background: var(--accent);
}

.dmu-18__row:has(input:focus-visible) {
  outline: 2px solid var(--focus);
  outline-offset: -2px;
}

.dmu-18__row input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.dmu-18__box {
  justify-self: center;
  display: grid;
  place-items: center;
  width: 1.15rem;
  height: 1.15rem;
  border-radius: .3rem;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--accent-ink);
}

.dmu-18__box svg {
  width: .75rem;
  height: .75rem;
  opacity: 0;
}

.dmu-18__row:has(input:checked) .dmu-18__box {
  background: var(--accent);
  border-color: transparent;
}

.dmu-18__row:has(input:checked) .dmu-18__box svg {
  opacity: 1;
}

.dmu-18__name {
  display: flex;
  align-items: center;
  gap: .5rem;
  padding: 0 .65rem;
  font-family: var(--mono);
  font-size: .8rem;
  min-width: 0;
}

.dmu-18__name svg {
  width: 1rem;
  height: 1rem;
  flex: none;
  color: var(--muted);
}

.dmu-18__num {
  padding: 0 .65rem;
  font-family: var(--mono);
  font-size: .76rem;
  font-variant-numeric: tabular-nums;
  color: var(--muted);
}

.dmu-18__owner {
  padding: 0 .65rem;
  font-size: .78rem;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .dmu-18__row,
    .dmu-18__folder,
    .dmu-18__toggle {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-18__app,
    .dmu-18__box {
    border-color: CanvasText;
    box-shadow: none;
  }

  .dmu-18__row:has(input:checked) {
    background: Highlight;
    color: HighlightText;
  }

  .dmu-18__row:has(input:checked) .dmu-18__box {
    background: HighlightText;
  }
}
```
