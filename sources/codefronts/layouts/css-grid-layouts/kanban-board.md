---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/kanban-board/"
title: "Kanban Board"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "A Trello-style board built on the column-flow trick: grid-auto-flow: column + grid-auto-columns sizes every new list identically without declaring counts,…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Kanban Board
Source: https://codefronts.com/layouts/css-grid-layouts/kanban-board/

A Trello-style board built on the column-flow trick: grid-auto-flow: column + grid-auto-columns sizes every new list identically without declaring counts, the board scroll-snaps horizontally on mobile, and each column's inner card stack scrolls independently while headers stay pinned.
## HTML
```html
<section class="cgl-18" aria-label="Kanban board demo">
  <div class="cgl-18__board" role="list" aria-label="Board columns">
    <section class="cgl-18__col" role="listitem"><header><h4>Backlog</h4><span>4</span></header>
      <div class="cgl-18__stack">
        <article class="cgl-18__card" style="--p:oklch(0.7 0.14 250)">Refactor auth flow<em>API</em></article>
        <article class="cgl-18__card" style="--p:oklch(0.75 0.13 150)">Empty-state illustrations<em>Design</em></article>
        <article class="cgl-18__card" style="--p:oklch(0.7 0.14 250)">Rate-limit webhooks<em>API</em></article>
        <article class="cgl-18__card" style="--p:oklch(0.78 0.14 85)">Docs: quickstart rewrite<em>Docs</em></article>
      </div>
    </section>
    <section class="cgl-18__col" role="listitem"><header><h4>In progress</h4><span>2</span></header>
      <div class="cgl-18__stack">
        <article class="cgl-18__card" style="--p:oklch(0.68 0.19 25)">Billing dunning emails<em>Urgent</em></article>
        <article class="cgl-18__card" style="--p:oklch(0.75 0.13 150)">Grid layout collection<em>Design</em></article>
      </div>
    </section>
    <section class="cgl-18__col" role="listitem"><header><h4>Review</h4><span>1</span></header>
      <div class="cgl-18__stack">
        <article class="cgl-18__card" style="--p:oklch(0.7 0.14 250)">Subgrid pricing table<em>API</em></article>
      </div>
    </section>
    <section class="cgl-18__col" role="listitem"><header><h4>Done</h4><span>3</span></header>
      <div class="cgl-18__stack">
        <article class="cgl-18__card is-done" style="--p:oklch(0.6 0.02 250)">Dark mode tokens<em>Design</em></article>
        <article class="cgl-18__card is-done" style="--p:oklch(0.6 0.02 250)">Onboarding checklist<em>Growth</em></article>
        <article class="cgl-18__card is-done" style="--p:oklch(0.6 0.02 250)">CDN migration<em>Infra</em></article>
      </div>
    </section>
  </div>
</section>
```
## CSS
```css
.cgl-18,
.cgl-18 *,
.cgl-18 *::before,
.cgl-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-18 {
  width: 100%;
  min-height: 100vh;
  --bg: oklch(0.19 0.02 270);
  --col: oklch(0.23 0.025 270);
  --line: oklch(0.32 0.03 270);
  --txt: oklch(0.93 0.01 270);
  --dim: oklch(0.66 0.02 270);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 1.2rem;
}

.cgl-18 .cgl-18__board {
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: clamp(230px,28vw,290px);
  gap: 12px;
  block-size: 340px;
  overflow-x: auto;
  overscroll-behavior-x: contain;
  scroll-snap-type: x proximity;
  scroll-padding-inline: 4px;
  padding-block-end: 8px;
}

.cgl-18 .cgl-18__col {
  scroll-snap-align: start;
  display: grid;
  grid-template-rows: auto minmax(0,1fr);
  background: var(--col);
  border: 1px solid var(--line);
  border-radius: 14px;
  overflow: hidden;
}

.cgl-18 .cgl-18__col header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: .75rem .9rem;
  border-block-end: 1px solid var(--line);
}

.cgl-18 h4 {
  font-size: .82rem;
  color: var(--txt);
}

.cgl-18 .cgl-18__col header span {
  font-size: .68rem;
  font-variant-numeric: tabular-nums;
  color: var(--dim);
  background: var(--bg);
  border-radius: 999px;
  padding: .15rem .5rem;
}

.cgl-18 .cgl-18__stack {
  overflow-y: auto;
  padding: .7rem;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.cgl-18 .cgl-18__card {
  background: oklch(0.28 0.025 270);
  border: 1px solid var(--line);
  border-inline-start: 3px solid var(--p);
  border-radius: 9px;
  padding: .65rem .75rem;
  font-size: .78rem;
  line-height: 1.4;
  color: var(--txt);
  display: flex;
  flex-direction: column;
  gap: .4rem;
  cursor: grab;
}

.cgl-18 .cgl-18__card:hover {
  border-color: color-mix(in oklab,var(--p) 60%,var(--line));
}

.cgl-18 .cgl-18__card em {
  font-style: normal;
  font-size: .62rem;
  letter-spacing: .06em;
  inline-size: fit-content;
  color: var(--p);
  background: color-mix(in oklab,var(--p) 14%,transparent);
  border-radius: 5px;
  padding: .12rem .4rem;
}

.cgl-18 .cgl-18__card.is-done {
  opacity: .55;
  text-decoration: line-through;
}

.cgl-18 .cgl-18__card.is-done em {
  text-decoration: none;
}
```

## JavaScript
```js
/* No JavaScript — grid-auto-flow: column mints identical columns on demand; scroll-snap makes the board swipeable. */
```
