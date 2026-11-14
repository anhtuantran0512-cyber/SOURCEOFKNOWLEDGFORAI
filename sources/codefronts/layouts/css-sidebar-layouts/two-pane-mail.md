---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/two-pane-mail/"
title: "Two-Pane Webmail UI Layout with CSS Flexbox & Grid"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The classic list/detail split every mail client, messenger and support inbox uses: a fixed folder rail, a 320px scrollable message list with unread…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Two-Pane Webmail UI Layout with CSS Flexbox & Grid
Source: https://codefronts.com/layouts/css-sidebar-layouts/two-pane-mail/

The classic list/detail split every mail client, messenger and support inbox uses: a fixed folder rail, a 320px scrollable message list with unread indicators, and a reading pane — three independent scroll regions in one grid, with the selected message tinted via aria-selected and unread rows styled from a data attribute.
## HTML
```html
<section class="sbl-12">
  <aside class="sbl-12__folders" aria-label="Folders">
    <button class="sbl-12__compose" type="button">Compose</button>
    <nav><a href="#" aria-current="page">Inbox <span>12</span></a><a href="#">Starred</a><a href="#">Sent</a><a href="#">Drafts <span>2</span></a><a href="#">Archive</a></nav>
  </aside>
  <div class="sbl-12__list" role="listbox" aria-label="Messages">
    <a class="sbl-12__msg" href="#" data-unread role="option" aria-selected="false"><span class="sbl-12__dot" aria-hidden="true"></span><span class="sbl-12__body"><strong>Priya Raman</strong><em>Q3 roadmap review — the container query rollout is ahead of schedule and I think we can…</em></span><time>09:41</time></a>
    <a class="sbl-12__msg" href="#" role="option" aria-selected="true"><span class="sbl-12__dot" aria-hidden="true"></span><span class="sbl-12__body"><strong>Marcus Webb</strong><em>Re: Design tokens sync — agreed, let's move the semantic layer into the base package…</em></span><time>08:17</time></a>
    <a class="sbl-12__msg" href="#" data-unread role="option" aria-selected="false"><span class="sbl-12__dot" aria-hidden="true"></span><span class="sbl-12__body"><strong>Linear</strong><em>Weekly digest: 14 issues closed, 3 in review. Cycle 42 completes Friday.</em></span><time>Mon</time></a>
    <a class="sbl-12__msg" href="#" role="option" aria-selected="false"><span class="sbl-12__dot" aria-hidden="true"></span><span class="sbl-12__body"><strong>Amara Osei</strong><em>Accessibility audit results — great news on the focus-visible coverage, two items left…</em></span><time>Mon</time></a>
  </div>
  <main class="sbl-12__read">
    <h1>Re: Design tokens sync</h1>
    <p class="sbl-12__meta">Marcus Webb · to Design Platform · 08:17</p>
    <p>Agreed — let's move the semantic layer into the base package. The component tokens can then alias into it, which keeps theming to a single override point.</p>
    <p>I'll draft the migration doc today. The mail list on your left scrolls independently of this pane — three scroll regions, one grid.</p>
  </main>
</section>
```
## CSS
```css
.sbl-12,
.sbl-12 *,
.sbl-12 *::before,
.sbl-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-12 {
  --panel: oklch(0.965 0.005 240);
  --ink: oklch(0.25 0.02 240);
  --mut: oklch(0.5 0.015 240);
  --line: oklch(0.89 0.007 240);
  --accent: oklch(0.52 0.17 255);
  display: grid;
  grid-template-columns: 200px 320px 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: #fff;
  color: var(--ink);
}

.sbl-12__folders {
  background: var(--panel);
  border-right: 1px solid var(--line);
  padding: 16px 10px;
  overflow-y: auto;
}

.sbl-12__compose {
  width: 100%;
  padding: 11px;
  border: none;
  border-radius: 10px;
  background: var(--accent);
  color: #fff;
  font: 600 13.5px/1 system-ui,sans-serif;
  cursor: pointer;
  margin-bottom: 14px;
  transition: filter .2s ease;
}

.sbl-12__compose:hover {
  filter: brightness(1.1);
}

.sbl-12__compose:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-12__folders nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.sbl-12__folders a {
  display: flex;
  justify-content: space-between;
  padding: 9px 12px;
  border-radius: 9px;
  font: 500 13.5px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
}

.sbl-12__folders a span {
  font-size: 11.5px;
  color: var(--accent);
  font-weight: 600;
}

.sbl-12__folders a:hover {
  background: color-mix(in oklab,var(--ink) 5%,transparent);
  color: var(--ink);
}

.sbl-12__folders a[aria-current="page"] {
  background: color-mix(in oklab,var(--accent) 11%,transparent);
  color: var(--ink);
  font-weight: 600;
}

.sbl-12__folders a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.sbl-12__list {
  border-right: 1px solid var(--line);
  overflow-y: auto;
  overscroll-behavior: contain;
}

.sbl-12__msg {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 10px;
  align-items: start;
  padding: 13px 14px;
  border-bottom: 1px solid var(--line);
  text-decoration: none;
  color: inherit;
  transition: background-color .15s ease;
}

.sbl-12__msg:hover {
  background: color-mix(in oklab,var(--ink) 3.5%,transparent);
}

.sbl-12__msg[aria-selected="true"] {
  background: color-mix(in oklab,var(--accent) 9%,transparent);
  box-shadow: inset 2.5px 0 0 var(--accent);
}

.sbl-12__msg:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.sbl-12__dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  margin-top: 5px;
  background: transparent;
}

.sbl-12__msg[data-unread] .sbl-12__dot {
  background: var(--accent);
}

.sbl-12__body {
  min-width: 0;
  display: grid;
  gap: 3px;
}

.sbl-12__body strong {
  font: 500 13.5px/1.2 system-ui,sans-serif;
}

.sbl-12__msg[data-unread] .sbl-12__body strong {
  font-weight: 700;
}

.sbl-12__body em {
  font: 400 12.5px/1.45 system-ui,sans-serif;
  font-style: normal;
  color: var(--mut);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.sbl-12__msg time {
  font: 500 11.5px/1 system-ui,sans-serif;
  color: var(--mut);
  margin-top: 2px;
}

.sbl-12__read {
  overflow-y: auto;
  padding: 32px 38px;
}

.sbl-12__read h1 {
  font: 650 20px/1.25 system-ui,sans-serif;
}

.sbl-12__meta {
  font: 500 12.5px/1 system-ui,sans-serif;
  color: var(--mut);
  margin: 10px 0 22px;
}

.sbl-12__read p {
  font-size: 14px;
  line-height: 1.7;
  max-width: 60ch;
  color: oklch(0.35 0.015 240);
  margin-bottom: 14px;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-12__msg,
    .sbl-12__compose {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — three independent scroll panes in one grid; unread and selected states style from data-unread and aria-selected attributes. */
```
