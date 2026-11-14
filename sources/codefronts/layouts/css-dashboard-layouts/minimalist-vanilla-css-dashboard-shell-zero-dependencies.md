---
source: "codefronts"
url: "https://codefronts.com/layouts/css-dashboard-layouts/minimalist-vanilla-css-dashboard-shell-zero-dependencies/"
title: "Minimalist Vanilla CSS Dashboard Shell (Zero Dependencies)"
section: "layouts"
category: "css-dashboard-layouts"
category_name: "CSS Dashboard Layouts"
description: "Forty-five lines of commented CSS."
has_js: "false"
---

Here's a working CSS Dashboard Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Vanilla CSS Dashboard Shell (Zero Dependencies)
Source: https://codefronts.com/layouts/css-dashboard-layouts/minimalist-vanilla-css-dashboard-shell-zero-dependencies/

Forty-five lines of commented CSS. Zero JavaScript, zero classes-per-pixel utility soup, zero build step — a complete dashboard shell styled almost entirely through semantic landmarks (header, nav, main, aside, footer) so it drops straight into server-rendered PHP, Django or Rails templates. The CSS is the tutorial: every line carries a comment saying what it earns. Delete the comments and it fits in a tweet thread.
## HTML
```html
<section class="cdl-12" aria-label="Vanilla zero-dependency shell demo">
  <div class="cdl-12__shell">
    <header><strong>Plainboard</strong><a href="#docs">Docs</a><a href="#account">Account</a></header>
    <nav aria-label="Primary">
      <a href="#home" aria-current="page">Home</a>
      <a href="#projects">Projects</a>
      <a href="#tasks">Tasks</a>
      <a href="#invoices">Invoices</a>
      <a href="#team">Team</a>
    </nav>
    <main>
      <h1>Home</h1>
      <div class="cdl-12__stats">
        <section><h2>Open tasks</h2><p>23</p></section>
        <section><h2>Due this week</h2><p>7</p></section>
        <section><h2>Hours logged</h2><p>31.5</p></section>
      </div>
      <section>
        <h2>Recent activity</h2>
        <ul>
          <li>Invoice <b>#204</b> sent to Harper &amp; Co <time>10:41</time></li>
          <li>Task <b>“Migrate DNS”</b> completed <time>09:12</time></li>
          <li>New project <b>Riverside</b> created <time>Yesterday</time></li>
          <li>Task <b>“QA pass”</b> assigned to Sam <time>Yesterday</time></li>
        </ul>
      </section>
    </main>
    <footer>Rendered server-side · no client framework · <a href="#src">view source</a></footer>
  </div>
</section>
```
## CSS
```css
.cdl-12,
.cdl-12 *,
.cdl-12 *::before,
.cdl-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdl-12 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  --accent: oklch(0.55 0.15 250);
  --ink: oklch(0.27 0.01 250);
  --mut: oklch(0.52 0.015 250);
  --edge: oklch(0.9 0.008 250);
  --paper: oklch(0.985 0.003 250);
  --pad: 14px;
  font-family: system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}
/* ——— the ~45-line shell starts here ——— */

.cdl-12 .cdl-12__shell {
  width: 100%;
  height: 100vh;
  display: grid;
  grid-template-columns: 220px minmax(0,1fr);
  grid-template-rows: auto minmax(0,1fr) auto;
  grid-template-areas: "header header" "nav main" "footer footer";
  border: 1px solid var(--edge);
  border-radius: 14px;
  overflow: hidden;
  background: var(--paper);
}

.cdl-12 .cdl-12__shell>header {
  grid-area: header;
  display: flex;
  align-items: center;
  gap: 16px;
  padding: var(--pad);
  background: white;
  border-bottom: 1px solid var(--edge);
}

.cdl-12 .cdl-12__shell>header strong {
  margin-right: auto;
  font-size: 15px;
}

.cdl-12 .cdl-12__shell>nav {
  grid-area: nav;
  display: flex;
  flex-direction: column;
  gap: 2px;
  padding: var(--pad);
  border-right: 1px solid var(--edge);
  background: white;
}

.cdl-12 .cdl-12__shell>main {
  grid-area: main;
  overflow-y: auto;
  overscroll-behavior: contain;
  padding: calc(var(--pad)*1.3);
  display: grid;
  gap: var(--pad);
  align-content: start;
}

.cdl-12 .cdl-12__shell>footer {
  grid-area: footer;
  padding: 10px var(--pad);
  font-size: 11.5px;
  color: var(--mut);
  background: white;
  border-top: 1px solid var(--edge);
}

.cdl-12 .cdl-12__shell a {
  color: var(--accent);
  text-decoration: none;
  font-size: 13px;
  font-weight: 550;
}

.cdl-12 .cdl-12__shell a:hover {
  text-decoration: underline;
  text-underline-offset: 3px;
}

.cdl-12 .cdl-12__shell a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: 3px;
}

.cdl-12 .cdl-12__shell>nav a {
  color: var(--mut);
  padding: 9px 12px;
  border-radius: 8px;
}

.cdl-12 .cdl-12__shell>nav a:hover {
  background: color-mix(in oklch,var(--accent) 6%,white);
  color: var(--ink);
  text-decoration: none;
}

.cdl-12 .cdl-12__shell>nav a[aria-current=page] {
  background: color-mix(in oklch,var(--accent) 12%,white);
  color: color-mix(in oklch,var(--accent) 75%,black);
}

.cdl-12 .cdl-12__shell h1 {
  font-size: 18px;
  letter-spacing: -.01em;
}

.cdl-12 .cdl-12__shell main section {
  background: white;
  border: 1px solid var(--edge);
  border-radius: 11px;
  padding: var(--pad);
}

.cdl-12 .cdl-12__shell main h2 {
  font-size: 11px;
  font-weight: 650;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 6px;
}

.cdl-12__stats {
  display: grid;
  gap: var(--pad);
  grid-template-columns: repeat(auto-fit,minmax(min(150px,100%),1fr));
}

.cdl-12__stats p {
  font-size: 24px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.cdl-12 .cdl-12__shell ul {
  list-style: none;
  display: grid;
  gap: 1px;
}

.cdl-12 .cdl-12__shell li {
  display: flex;
  gap: 6px;
  align-items: baseline;
  font-size: 13px;
  padding: 9px 2px;
  border-bottom: 1px solid color-mix(in oklch,var(--edge) 55%,transparent);
}

.cdl-12 .cdl-12__shell li:last-child {
  border-bottom: none;
}

.cdl-12 .cdl-12__shell li b {
  font-weight: 600;
}

.cdl-12 .cdl-12__shell li time {
  margin-left: auto;
  font-size: 11px;
  color: var(--mut);
  font-variant-numeric: tabular-nums;
}

@container (max-width: 620px) {
  .cdl-12 .cdl-12__shell {
    grid-template-columns: minmax(0,1fr);
    grid-template-areas: "header" "nav" "main" "footer";
    grid-template-rows: auto auto minmax(0,1fr) auto;
  }

  .cdl-12 .cdl-12__shell>nav {
    flex-direction: row;
    overflow-x: auto;
    border-right: none;
    border-bottom: 1px solid var(--edge);
  }
}
/* ——— shell ends ——— */
```
