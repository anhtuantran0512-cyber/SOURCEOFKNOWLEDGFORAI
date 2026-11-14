---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/inline-micro-empty-state-component/"
title: "Inline / Micro Empty State Component"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "The empty state for small places, shown where it actually happens: a sidebar widget, a dashboard tile and a table cell, all rendering the same component…"
has_js: "false"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inline / Micro Empty State Component
Source: https://codefronts.com/snippets/css-empty-states/inline-micro-empty-state-component/

The empty state for small places, shown where it actually happens: a sidebar widget, a dashboard tile and a table cell, all rendering the same component inside one product page. It responds to its container, not the viewport &mdash; drag the right edge of the first tile and the illustration goes, then the body copy, then the layout flattens.
## HTML
```html
<div class="est-20">
  <div class="est-20__shell">
    <aside class="est-20__rail">
      <span class="est-20__logo">Runway</span>
      <nav class="est-20__nav">
        <a class="est-20__nl est-20__nl--on" href="#est-20" aria-current="page">Today</a>
        <a class="est-20__nl" href="#est-20">Spend</a>
        <a class="est-20__nl" href="#est-20">Vendors</a>
        <a class="est-20__nl" href="#est-20">Approvals</a>
      </nav>

      <div class="est-20__widget">
        <p class="est-20__wtitle">Starred reports</p>
        <div class="est-20__slot">
          <div class="est-20__micro">
            <span class="est-20__art" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 4.5l2.4 5 5.4.7-4 3.8 1 5.3L12 16.6 7.2 19.3l1-5.3-4-3.8 5.4-.7z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
            </span>
            <span class="est-20__mtext">
              <span class="est-20__mh">No starred reports</span>
              <span class="est-20__mp">Star one to pin it to this rail.</span>
            </span>
            <button class="est-20__mbtn" type="button">Browse</button>
          </div>
        </div>
      </div>
    </aside>

    <main class="est-20__main">
      <header class="est-20__top">
        <h1 class="est-20__h1">Today</h1>
        <div class="est-20__tacts">
          <button class="est-20__seg est-20__seg--on" type="button">This month</button>
          <button class="est-20__seg" type="button">Quarter</button>
          <button class="est-20__ava" type="button" aria-label="Account">EM</button>
        </div>
      </header>

      <div class="est-20__grid">
        <section class="est-20__tile">
          <p class="est-20__ttitle">Team activity</p>
          <div class="est-20__resize"><div class="est-20__slot">
            <div class="est-20__micro">
              <span class="est-20__art" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" focusable="false"><rect x="3.5" y="6" width="17" height="12" rx="2.5" stroke="currentColor" stroke-width="1.6"/><path d="M3.5 10h17M8 14h6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
              </span>
              <span class="est-20__mtext">
                <span class="est-20__mh">No activity today</span>
                <span class="est-20__mp">Comments, mentions and status changes from your team appear here.</span>
              </span>
              <button class="est-20__mbtn" type="button">Follow a project</button>
            </div>
          </div></div>
        </section>

        <section class="est-20__tile est-20__tile--warn">
          <p class="est-20__ttitle">Budget</p>
          <div class="est-20__slot">
            <div class="est-20__micro">
              <span class="est-20__art" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M4 18V9M10 18V5M16 18v-6M21 18H3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
              </span>
              <span class="est-20__mtext">
                <span class="est-20__mh">No spend yet</span>
                <span class="est-20__mp">Usage is billed monthly.</span>
              </span>
              <button class="est-20__mbtn" type="button">Set a budget</button>
            </div>
          </div>
        </section>

        <section class="est-20__tile est-20__tile--wide">
          <p class="est-20__ttitle">Vendor invoices</p>
          <div class="est-20__table">
            <div class="est-20__thead"><span>Vendor</span><span>Terms</span><span>Next charge</span></div>
            <div class="est-20__slot est-20__slot--cell">
              <div class="est-20__micro">
                <span class="est-20__art" aria-hidden="true">
                  <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6 3.5h9l3.5 3.5v13.5H6z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M14.6 3.8V7.4h3.6M9 12h6M9 15.5h4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
                </span>
                <span class="est-20__mtext">
                  <span class="est-20__mh">No invoices this month</span>
                  <span class="est-20__mp">Vendors on annual terms will not appear until renewal.</span>
                </span>
                <button class="est-20__mbtn" type="button">Add a vendor</button>
              </div>
            </div>
          </div>
        </section>
      </div>
    </main>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.est-20 {
  --bg: #f6f6f8;
  --surface: #ffffff;
  --sunk: #f0f1f4;
  --line: #e4e5ea;
  --line-2: #d3d5db;
  --ink: #14151a;
  --muted: #575a63;
  --faint: #888b94;
  --accent: #2f4bb8;
  --warn: #9a6412;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  color-scheme: light;
  font-synthesis: none;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.est-20 *,
.est-20 *::before,
.est-20 *::after {
  box-sizing: border-box;
}

.est-20 [hidden] {
  display: none !important;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-20 {
    --bg: oklch(0.972 0.003 280);
    --surface: oklch(1 0 0);
    --sunk: oklch(0.955 0.004 280);
    --line: oklch(0.918 0.005 280);
    --line-2: oklch(0.865 0.007 280);
    --ink: oklch(0.175 0.009 280);
    --muted: oklch(0.465 0.011 280);
    --faint: oklch(0.625 0.012 280);
    --accent: oklch(0.45 0.16 272);
    --warn: oklch(0.52 0.1 75);
  }
}

.est-20__shell {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-columns: min(15rem,24vw) minmax(0,1fr);
}

.est-20__rail {
  display: grid;
  grid-template-rows: auto auto minmax(0,1fr);
  gap: 1.15rem;
  align-content: start;
  padding: 1.15rem .85rem;
  border-inline-end: 1px solid var(--line);
  background: var(--surface);
}

.est-20__logo {
  padding-inline: .4rem;
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -.025em;
}

.est-20__nav {
  display: grid;
  gap: .1rem;
}

.est-20__nl {
  padding: .45rem .6rem;
  border-radius: 8px;
  text-decoration: none;
  font-size: .86rem;
  color: var(--muted);
  transition: color .16s, background .16s;
}

.est-20__nl:hover {
  color: var(--ink);
  background: var(--sunk);
}

.est-20__nl--on {
  color: var(--ink);
  background: var(--sunk);
  box-shadow: inset 0 0 0 1px var(--line);
}

.est-20__widget {
  display: grid;
  gap: .5rem;
  align-content: start;
}

.est-20__wtitle {
  margin: 0;
  padding-inline: .4rem;
  font-size: .78rem;
  font-weight: 500;
  color: var(--faint);
}

.est-20__main {
  min-inline-size: 0;
  display: grid;
  grid-template-rows: auto minmax(0,1fr);
  align-content: start;
}

.est-20__top {
  display: flex;
  flex-wrap: wrap;
  gap: .75rem 1.25rem;
  align-items: center;
  justify-content: space-between;
  padding: 1rem clamp(1rem,3vw,2rem);
  border-block-end: 1px solid var(--line);
}

.est-20__h1 {
  margin: 0;
  font-size: clamp(1.3rem,3vw,1.75rem);
  font-weight: 600;
  letter-spacing: -.032em;
}

.est-20__tacts {
  display: flex;
  align-items: center;
  gap: .4rem;
}

.est-20__seg {
  min-block-size: 2.4rem;
  padding: .5rem .85rem;
  font: inherit;
  font-size: .83rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--muted);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 9px;
  transition: color .16s, background .16s;
}

.est-20__seg:hover {
  color: var(--ink);
  background: var(--sunk);
}

.est-20__seg--on {
  color: var(--ink);
  background: var(--sunk);
  border-color: var(--line-2);
}

.est-20__ava {
  inline-size: 2.2rem;
  block-size: 2.2rem;
  margin-inline-start: .35rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 50%;
  font: inherit;
  font-size: .7rem;
  font-weight: 600;
  color: #fff;
  background: var(--accent);
  border: 0;
}

.est-20__grid {
  padding: clamp(1rem,3vw,2rem);
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(min(17rem,100%),1fr));
  align-content: start;
  align-items: start;
}

.est-20__tile {
  display: grid;
  gap: .7rem;
  align-content: start;
  padding: 1rem 1.05rem 1.15rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 16px;
  box-shadow: 0 1px 2px rgba(20,21,26,.04);
}

.est-20__tile--wide {
  grid-column: 1 / -1;
}

.est-20__resize {
  resize: horizontal;
  overflow: auto;
  inline-size: 100%;
  min-inline-size: 9rem;
  max-inline-size: 100%;
  padding-block-end: .4rem;
}

.est-20__ttitle {
  margin: 0;
  font-size: .85rem;
  font-weight: 600;
  letter-spacing: -.015em;
}

.est-20__tile--warn {
  background: color-mix(in oklab, var(--warn) 5%, var(--surface));
  border-color: color-mix(in oklab, var(--warn) 22%, var(--line));
}

.est-20__slot {
  container-type: inline-size;
  container-name: micro;
  inline-size: 100%;
}

.est-20__micro {
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto;
  gap: .55rem .8rem;
  align-items: center;
  padding: .85rem .9rem;
  background: var(--sunk);
  border: 1px solid var(--line);
  border-radius: 13px;
}

.est-20__art {
  inline-size: 2.4rem;
  block-size: 2.4rem;
  display: grid;
  place-items: center;
  border-radius: 9px;
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 9%, var(--surface));
  box-shadow: inset 0 0 0 1px color-mix(in oklab, var(--accent) 16%, transparent);
}

.est-20__art svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.est-20__tile--warn .est-20__art {
  color: var(--warn);
  background: color-mix(in oklab, var(--warn) 12%, var(--surface));
  box-shadow: inset 0 0 0 1px color-mix(in oklab, var(--warn) 22%, transparent);
}

.est-20__mtext {
  min-inline-size: 0;
  display: grid;
  gap: .15rem;
}

.est-20__mh {
  font-size: clamp(.87rem, 3.8cqi, 1rem);
  font-weight: 600;
  letter-spacing: -.015em;
  line-height: 1.25;
  overflow-wrap: anywhere;
}

.est-20__mp {
  font-size: clamp(.76rem, 3.1cqi, .83rem);
  line-height: 1.45;
  color: var(--muted);
  text-wrap: pretty;
}

.est-20__mbtn {
  min-block-size: 2.75rem;
  padding: .6rem .85rem;
  font: inherit;
  font-size: .81rem;
  font-weight: 500;
  cursor: pointer;
  white-space: nowrap;
  color: #fff;
  background: var(--accent);
  border: 1px solid transparent;
  border-radius: 9px;
  transition: translate .16s, filter .16s;
}

.est-20__mbtn:hover {
  translate: 0 -1px;
  filter: brightness(1.08);
}

.est-20__tile--warn .est-20__mbtn {
  background: var(--warn);
}

.est-20__mbtn:focus-visible,
.est-20__seg:focus-visible,
.est-20__ava:focus-visible,
.est-20__nl:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@container micro (max-width: 23rem) {
  .est-20__art {
    display: none;
  }

  .est-20__micro {
    grid-template-columns: minmax(0,1fr) auto;
  }
}

@container micro (max-width: 19rem) {
  .est-20__mp {
    display: none;
  }
}

@container micro (max-width: 16rem) {
  .est-20__micro {
    grid-template-columns: minmax(0,1fr);
    gap: .55rem;
  }

  .est-20__mbtn {
    inline-size: 100%;
  }
}

@supports (container-type: inline-size) {
  @container style(--tone: warning) {
    .est-20__micro {
      border-color: color-mix(in oklab, var(--warn) 30%, var(--line));
    }
  }
}

.est-20__table {
  display: grid;
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: 12px;
}

.est-20__thead {
  display: grid;
  grid-template-columns: minmax(0,2fr) minmax(0,1fr) minmax(0,1fr);
  gap: 1rem;
  padding: .55rem .9rem;
  background: var(--sunk);
  border-block-end: 1px solid var(--line);
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .65rem;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: var(--faint);
}

.est-20__slot--cell {
  padding: .85rem;
}

.est-20__slot--cell .est-20__micro {
  background: var(--surface);
}

@media (max-width: 900px) {
  .est-20__shell {
    grid-template-columns: 1fr;
  }

  .est-20__rail {
    grid-template-rows: auto;
    grid-template-columns: auto minmax(0,1fr);
    align-items: center;
    border-inline-end: 0;
    border-block-end: 1px solid var(--line);
  }

  .est-20__nav {
    display: flex;
    flex-wrap: wrap;
    gap: .35rem;
  }

  .est-20__widget {
    display: none;
  }

  .est-20__tile--wide {
    grid-column: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .est-20 *,
    .est-20 *::before,
    .est-20 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-20__tile,
    .est-20__micro,
    .est-20__mbtn {
    border-color: CanvasText;
  }
}
```
