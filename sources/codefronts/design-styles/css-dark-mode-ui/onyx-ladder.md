---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/onyx-ladder/"
title: "Onyx Ladder Dark Mode Timeline"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "A changelog you would actually read: five events alternating either side of a central rail, each in an elevated onyx card with a monospaced timestamp, a…"
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Onyx Ladder Dark Mode Timeline
Source: https://codefronts.com/design-styles/css-dark-mode-ui/onyx-ladder/

A changelog you would actually read: five events alternating either side of a central rail, each in an elevated onyx card with a monospaced timestamp, a typed badge and a node that sits on the rail rather than beside it. The alternating layout is pure grid — no absolute positioning, no magic numbers — and it collapses to a single left-rail column on narrow screens without changing the markup.
## HTML
```html
<div class="dmu-19">
  <div class="dmu-19__stage">
    <div class="dmu-19__wrap">
      <header class="dmu-19__head">
        <p class="dmu-19__kicker">Changelog</p>
        <h1 class="dmu-19__h1">Shipped this week</h1>
        <p class="dmu-19__lede">Five releases, one rail. Timestamps are tabular so the column reads as a single edge.</p>
      </header>

      <ol class="dmu-19__list">
        <li class="dmu-19__item">
          <span class="dmu-19__node" aria-hidden="true"></span>
          <article class="dmu-19__card">
            <div class="dmu-19__cardTop">
              <span class="dmu-19__badge dmu-19__badge--feature">Feature</span>
              <time class="dmu-19__time" datetime="2026-08-14T09:12">14 Aug &middot; 09:12</time>
            </div>
            <h2 class="dmu-19__title">Three-state theme switcher</h2>
            <p class="dmu-19__body">System / Light / Dark now persists per workspace, and the rendering path stays pure CSS.</p>
            <p class="dmu-19__by">Alex Chen</p>
          </article>
        </li>

        <li class="dmu-19__item">
          <span class="dmu-19__node" aria-hidden="true"></span>
          <article class="dmu-19__card">
            <div class="dmu-19__cardTop">
              <span class="dmu-19__badge dmu-19__badge--fix">Fix</span>
              <time class="dmu-19__time" datetime="2026-08-13T17:48">13 Aug &middot; 17:48</time>
            </div>
            <h2 class="dmu-19__title">Toggle flipped one way only</h2>
            <p class="dmu-19__body">Added the nested-media restore rule so the switch works for visitors whose OS already matched the default.</p>
            <p class="dmu-19__by">Priya Sharma</p>
          </article>
        </li>

        <li class="dmu-19__item">
          <span class="dmu-19__node" aria-hidden="true"></span>
          <article class="dmu-19__card">
            <div class="dmu-19__cardTop">
              <span class="dmu-19__badge dmu-19__badge--perf">Perf</span>
              <time class="dmu-19__time" datetime="2026-08-13T11:02">13 Aug &middot; 11:02</time>
            </div>
            <h2 class="dmu-19__title">Dropped 12 kB from the theme layer</h2>
            <p class="dmu-19__body">Semantic tokens now derive from four primitives, so the second theme costs one media block instead of a stylesheet.</p>
            <p class="dmu-19__by">Jordan Lee</p>
          </article>
        </li>

        <li class="dmu-19__item">
          <span class="dmu-19__node" aria-hidden="true"></span>
          <article class="dmu-19__card">
            <div class="dmu-19__cardTop">
              <span class="dmu-19__badge dmu-19__badge--a11y">Access</span>
              <time class="dmu-19__time" datetime="2026-08-12T20:31">12 Aug &middot; 20:31</time>
            </div>
            <h2 class="dmu-19__title">Focus rings audited at 3:1</h2>
            <p class="dmu-19__body">Every interactive control has a per-theme ring token with a 2px outline and a 2px offset.</p>
            <p class="dmu-19__by">Sam Rivera</p>
          </article>
        </li>

        <li class="dmu-19__item">
          <span class="dmu-19__node" aria-hidden="true"></span>
          <article class="dmu-19__card">
            <div class="dmu-19__cardTop">
              <span class="dmu-19__badge dmu-19__badge--feature">Feature</span>
              <time class="dmu-19__time" datetime="2026-08-11T15:20">11 Aug &middot; 15:20</time>
            </div>
            <h2 class="dmu-19__title">theme-color syncs per scheme</h2>
            <p class="dmu-19__body">Mobile browser chrome now follows the active surface instead of the operating system.</p>
            <p class="dmu-19__by">Alex Chen</p>
          </article>
        </li>
      </ol>
    </div>
  </div>
</div>
```
## CSS
```css
.dmu-19 {
  --bg: #07080a;
  --surface: #0f1114;
  --raised: #15181d;
  --ink: #eceef1;
  --muted: #8a919c;
  --line: #212530;
  --rail: rgba(236,238,241,.13);
  --accent: #c4b5fd;
  --feature: #a5b4fc;
  --fix: #fcd34d;
  --perf: #7ee0b0;
  --a11y: #7dd3fc;
  --shadow: rgba(0,0,0,.75);
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"SF Mono","JetBrains Mono",Menlo,monospace;
  color-scheme: dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(110% 60% at 50% 0%,#0d1015,var(--bg) 60%),var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.dmu-19,
.dmu-19 *,
.dmu-19 *::before,
.dmu-19 *::after {
  box-sizing: border-box;
}

.dmu-19__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  justify-items: center;
  align-content: center;
  padding: clamp(1.25rem,4vw,3.5rem);
}

.dmu-19__wrap {
  width: min(64rem,100%);
  display: grid;
  gap: clamp(1.25rem,3vw,2rem);
}

.dmu-19__head {
  display: grid;
  gap: .4rem;
  justify-items: center;
  text-align: center;
}

.dmu-19__kicker {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.dmu-19__h1 {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.3rem);
  font-weight: 650;
  letter-spacing: -.035em;
}

.dmu-19__lede {
  margin: 0;
  font-size: .92rem;
  color: var(--muted);
  max-width: 48ch;
  text-wrap: pretty;
}

.dmu-19__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 1rem;
  background: linear-gradient(var(--rail),var(--rail)) no-repeat 1rem 0 / 1px 100%;
}

@media (min-width: 52rem) {
  .dmu-19__list {
    background-position: 50% 0;
  }
}

.dmu-19__item {
  display: grid;
  grid-template-columns: 2rem 1fr;
  align-items: start;
}

@media (min-width: 52rem) {
  .dmu-19__item {
    grid-template-columns: 1fr 2.5rem 1fr;
  }
}

.dmu-19__node {
  grid-column: 1;
  justify-self: center;
  margin-top: 1.25rem;
  width: .7rem;
  height: .7rem;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 0 4px var(--bg), 0 0 0 5px var(--line);
}

@media (min-width: 52rem) {
  .dmu-19__node {
    grid-column: 2;
  }
}

.dmu-19__card {
  grid-column: 2;
  display: grid;
  gap: .4rem;
  padding: 1.05rem 1.15rem;
  border-radius: .95rem;
  background: linear-gradient(180deg,var(--raised),var(--surface));
  border: 1px solid var(--line);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.04), 0 22px 44px -38px var(--shadow);
  transition: translate .22s cubic-bezier(.16,1,.3,1), border-color .22s ease;
}

@media (min-width: 52rem) {
  .dmu-19__item:nth-child(odd) .dmu-19__card {
    grid-column: 1;
  }

  .dmu-19__item:nth-child(even) .dmu-19__card {
    grid-column: 3;
  }
}

.dmu-19__card:hover {
  translate: 0 -2px;
  border-color: color-mix(in oklab,var(--accent) 40%,var(--line));
}

.dmu-19__cardTop {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .75rem;
}

.dmu-19__badge {
  display: inline-flex;
  align-items: center;
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  padding: .24rem .5rem;
  border-radius: .35rem;
  border: 1px solid currentColor;
}

.dmu-19__badge--feature {
  color: var(--feature);
}

.dmu-19__badge--fix {
  color: var(--fix);
}

.dmu-19__badge--perf {
  color: var(--perf);
}

.dmu-19__badge--a11y {
  color: var(--a11y);
}

.dmu-19__time {
  font-family: var(--mono);
  font-size: .72rem;
  font-variant-numeric: tabular-nums;
  color: var(--muted);
}

.dmu-19__title {
  margin: 0;
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.dmu-19__body {
  margin: 0;
  font-size: .85rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.dmu-19__by {
  margin: .15rem 0 0;
  font-size: .74rem;
  color: var(--muted);
  opacity: .85;
}

@media (prefers-reduced-motion: reduce) {
  .dmu-19__card {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-19__card {
    border-color: CanvasText;
    box-shadow: none;
  }

  .dmu-19__node {
    background: CanvasText;
    box-shadow: none;
  }

  .dmu-19__list {
    background: none;
  }
}
```
