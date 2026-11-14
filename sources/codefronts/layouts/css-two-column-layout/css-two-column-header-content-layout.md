---
source: "codefronts"
url: "https://codefronts.com/layouts/css-two-column-layout/css-two-column-header-content-layout/"
title: "CSS Two Column Header Content Layout"
section: "layouts"
category: "css-two-column-layout"
category_name: "CSS Two-Column Layouts"
description: "The classic \"holy grail lite\": a full-width sticky header with a two column body underneath, declared once with grid-template-areas — the header spans both…"
has_js: "false"
---

Here's a working CSS Two-Column Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Two Column Header Content Layout
Source: https://codefronts.com/layouts/css-two-column-layout/css-two-column-header-content-layout/

The classic "holy grail lite": a full-width sticky header with a two column body underneath, declared once with grid-template-areas — the header spans both tracks, nav takes a 220px rail, main fills the rest. The readable, refactor-safe way to structure a whole app or docs page.
## HTML
```html
<section class="tcl-10" aria-label="Header and two column content layout demo">
  <div class="tcl-10__app">
    <header class="tcl-10__header">
      <div class="tcl-10__brand"><i></i>Ledgerline <span>Docs</span></div>
      <span class="tcl-10__area">grid-area: header</span>
      <a class="tcl-10__hbtn" href="#api">API status</a>
    </header>
    <nav class="tcl-10__nav" aria-label="Docs navigation">
      <span class="tcl-10__area">nav · 220px</span>
      <b>Getting started</b>
      <a href="#install" aria-current="page">Installation</a>
      <a href="#auth">Authentication</a>
      <a href="#first">Your first invoice</a>
      <b>Core concepts</b>
      <a href="#accounts">Accounts</a>
      <a href="#webhooks">Webhooks</a>
    </nav>
    <main class="tcl-10__main">
      <span class="tcl-10__area">main · minmax(0, 1fr)</span>
      <h1>Installation</h1>
      <p>Install the SDK, set your key, and you’re three lines from your first ledger entry. The header above spans both columns from a single <code>grid-template-areas</code> declaration — scroll to see it stick.</p>
      <pre class="tcl-10__code"><code>npm install @ledgerline/sdk

import { Ledger } from "@ledgerline/sdk";
const ledger = new Ledger(process.env.LL_KEY);</code></pre>
      <div class="tcl-10__callout"><b>Tip</b><span>Keys are scoped per environment. Use a test key locally — it writes to a sandbox ledger you can wipe at any time.</span></div>
      <h2>Verify the connection</h2>
      <p>Call <code>ledger.ping()</code> — a healthy response returns your account id and region. If you see a 401, your key belongs to a different environment than the endpoint you’re calling.</p>
    </main>
  </div>
</section>
```
## CSS
```css
.tcl-10,
.tcl-10 *,
.tcl-10 *::before,
.tcl-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tcl-10 {
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.65 0.15 85);
  --ink: oklch(0.25 0.02 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  background: oklch(0.97 0.006 85);
}

.tcl-10__app {
  display: grid;
  grid-template-columns: 220px minmax(0,1fr);
  grid-template-rows: auto 1fr;
  grid-template-areas: "header header" "nav main";
  min-height: 540px;
  max-width: 1060px;
  margin-inline: auto;
}

.tcl-10__header {
  grid-area: header;
  position: sticky;
  top: 0;
  z-index: 5;
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 14px 22px;
  background: color-mix(in oklab,oklch(0.99 0.003 85) 88%,transparent);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid oklch(0.89 0.015 85);
}

.tcl-10__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-weight: 700;
  font-size: 15.5px;
  letter-spacing: -.01em;
}

.tcl-10__brand i {
  width: 24px;
  height: 24px;
  border-radius: 7px;
  background: conic-gradient(from 40deg,var(--accent),oklch(0.5 0.13 60));
}

.tcl-10__brand span {
  font-weight: 500;
  color: color-mix(in oklab,var(--ink) 55%,transparent);
}

.tcl-10__area {
  font: 600 10px/1 ui-monospace,monospace;
  letter-spacing: .05em;
  color: oklch(0.55 0.11 85);
  border: 1px dashed oklch(0.78 0.06 85);
  border-radius: 99px;
  padding: 4px 8px;
  justify-self: start;
  align-self: start;
}

.tcl-10__header .tcl-10__area {
  margin-left: auto;
}

.tcl-10__hbtn {
  font: 600 13px/1 inherit;
  color: var(--ink);
  text-decoration: none;
  border: 1.5px solid oklch(0.85 0.03 85);
  border-radius: 9px;
  padding: 9px 14px;
  transition: border-color .15s,background .15s;
}

.tcl-10__hbtn:hover {
  border-color: var(--accent);
  background: color-mix(in oklab,var(--accent) 8%,transparent);
}

.tcl-10__hbtn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.tcl-10__nav {
  grid-area: nav;
  display: grid;
  gap: 2px;
  align-content: start;
  padding: 20px 14px;
  border-right: 1px solid oklch(0.9 0.012 85);
}

.tcl-10__nav b {
  font-size: 11px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: color-mix(in oklab,var(--ink) 52%,transparent);
  padding: 14px 10px 6px;
}

.tcl-10__nav a {
  font-size: 13.5px;
  color: var(--ink);
  text-decoration: none;
  padding: 8px 10px;
  border-radius: 8px;
  transition: background .15s;
}

.tcl-10__nav a:hover {
  background: color-mix(in oklab,var(--accent) 10%,transparent);
}

.tcl-10__nav a[aria-current="page"] {
  background: color-mix(in oklab,var(--accent) 16%,transparent);
  font-weight: 600;
}

.tcl-10__nav a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.tcl-10__main {
  grid-area: main;
  display: grid;
  gap: 16px;
  align-content: start;
  padding: clamp(20px,3vw,36px);
  min-width: 0;
}

.tcl-10__main h1 {
  font-size: clamp(24px,3vw,32px);
  letter-spacing: -.02em;
}

.tcl-10__main h2 {
  font-size: 19px;
  letter-spacing: -.015em;
  margin-top: 8px;
}

.tcl-10__main p {
  font-size: 14.5px;
  line-height: 1.7;
  color: color-mix(in oklab,var(--ink) 78%,transparent);
  max-width: 62ch;
  text-wrap: pretty;
}

.tcl-10__main code {
  font: 600 12.5px ui-monospace,monospace;
  background: color-mix(in oklab,var(--accent) 14%,transparent);
  border-radius: 5px;
  padding: 2px 6px;
}

.tcl-10__code {
  background: oklch(0.23 0.02 85);
  border-radius: 12px;
  padding: 18px;
  overflow-x: auto;
}

.tcl-10__code code {
  font: 500 13px/1.7 ui-monospace,monospace;
  color: oklch(0.88 0.05 95);
  background: none;
  padding: 0;
}

.tcl-10__callout {
  display: flex;
  gap: 12px;
  align-items: baseline;
  font-size: 13.5px;
  line-height: 1.6;
  background: color-mix(in oklab,var(--accent) 9%,transparent);
  border: 1px solid color-mix(in oklab,var(--accent) 30%,transparent);
  border-radius: 12px;
  padding: 14px 16px;
  max-width: 62ch;
}

.tcl-10__callout b {
  color: oklch(0.5 0.12 85);
}

@media (max-width: 700px) {
  .tcl-10__app {
    grid-template-columns: 1fr;
    grid-template-areas: "header" "nav" "main";
    grid-template-rows: auto auto 1fr;
  }

  .tcl-10__nav {
    border-right: 0;
    border-bottom: 1px solid oklch(0.9 0.012 85);
    grid-auto-flow: row;
  }
}
```

## JavaScript
```js
/* No JavaScript — grid-template-areas ("header header" / "nav main") lays out the whole app; position:sticky pins the header inside the flow. */
```
