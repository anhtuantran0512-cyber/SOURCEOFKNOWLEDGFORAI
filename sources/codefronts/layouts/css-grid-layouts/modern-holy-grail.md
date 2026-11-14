---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/modern-holy-grail/"
title: "Modern Holy Grail"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "The legendary header/nav/main/aside/footer layout — the one that needed floats, negative margins and prayer for fifteen years — rebuilt as eleven lines of…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Modern Holy Grail
Source: https://codefronts.com/layouts/css-grid-layouts/modern-holy-grail/

The legendary header/nav/main/aside/footer layout — the one that needed floats, negative margins and prayer for fifteen years — rebuilt as eleven lines of grid-template-areas. Fluid center column via minmax(0,1fr), sidebars that never collapse below readable, and a single media query for mobile stacking.
## HTML
```html
<section class="cgl-04" aria-label="Modern holy grail layout demo">
  <div class="cgl-04__shell">
    <header class="cgl-04__header"><strong>header</strong><span>brand · search · account</span></header>
    <nav class="cgl-04__nav" aria-label="Primary"><strong>nav</strong><a href="#0">Dashboard</a><a href="#0">Projects</a><a href="#0">Reports</a><a href="#0">Settings</a></nav>
    <main class="cgl-04__main"><strong>main</strong><p>The fluid center: minmax(0, 1fr) absorbs all spare width and — crucially — is allowed to shrink below its content's natural size, so wide tables and code blocks scroll here instead of shoving the sidebars off-canvas.</p></main>
    <aside class="cgl-04__aside"><strong>aside</strong><p>Related links, ads, or a table of contents. Clamped between 140 and 200px.</p></aside>
    <footer class="cgl-04__footer"><strong>footer</strong><span>pinned by auto · 1fr · auto rows</span></footer>
  </div>
</section>
```
## CSS
```css
.cgl-04,
.cgl-04 *,
.cgl-04 *::before,
.cgl-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-04 {
  width: 100%;
  min-height: 100vh;
  --bg: oklch(0.2 0.03 250);
  --line: oklch(0.75 0.12 210);
  --txt: oklch(0.93 0.01 220);
  --dim: oklch(0.7 0.03 230);
  font-family: ui-monospace,'Cascadia Code',Menlo,monospace;
  background: repeating-linear-gradient(0deg,transparent 0 23px,oklch(0.75 0.12 210/.06) 23px 24px),repeating-linear-gradient(90deg,transparent 0 23px,oklch(0.75 0.12 210/.06) 23px 24px),var(--bg);
  color: var(--txt);
  padding: 1.4rem;
}

.cgl-04 .cgl-04__shell {
  display: grid;
  grid-template-areas: "header header header" "nav main aside" "footer footer footer";
  grid-template-columns: minmax(140px,180px) minmax(0,1fr) minmax(140px,200px);
  grid-template-rows: auto 1fr auto;
  gap: 10px;
  min-block-size: 380px;
}

.cgl-04 .cgl-04__shell>* {
  border: 1px dashed color-mix(in oklab,var(--line) 55%,transparent);
  border-radius: 10px;
  padding: .9rem;
  background: oklch(0.24 0.03 250/.8);
}

.cgl-04 strong {
  display: block;
  font-size: .7rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--line);
  margin-block-end: .5rem;
}

.cgl-04 .cgl-04__header {
  grid-area: header;
  display: flex;
  align-items: baseline;
  gap: 1rem;
}

.cgl-04 .cgl-04__header strong {
  margin: 0;
}

.cgl-04 .cgl-04__header span,
.cgl-04 .cgl-04__footer span {
  font-size: .75rem;
  color: var(--dim);
}

.cgl-04 .cgl-04__nav {
  grid-area: nav;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.cgl-04 .cgl-04__nav a {
  font-size: .8rem;
  color: var(--dim);
  text-decoration: none;
  padding: .4rem .5rem;
  border-radius: 6px;
}

.cgl-04 .cgl-04__nav a:hover {
  color: var(--txt);
  background: oklch(0.3 0.04 250);
}

.cgl-04 .cgl-04__nav a:focus-visible {
  outline: 2px solid var(--line);
  outline-offset: 2px;
}

.cgl-04 .cgl-04__main {
  grid-area: main;
}

.cgl-04 .cgl-04__aside {
  grid-area: aside;
}

.cgl-04 .cgl-04__footer {
  grid-area: footer;
  display: flex;
  align-items: baseline;
  gap: 1rem;
}

.cgl-04 .cgl-04__footer strong {
  margin: 0;
}

.cgl-04 p {
  font-size: .8rem;
  line-height: 1.7;
  color: var(--dim);
}

@media (max-width: 640px) {
  .cgl-04 .cgl-04__shell {
    grid-template-areas: "header" "nav" "main" "aside" "footer";
    grid-template-columns: 1fr;
    grid-template-rows: auto;
  }
}
```

## JavaScript
```js
/* No JavaScript — grid-template-areas draws the page as ASCII art; one media query restacks it without touching the HTML. */
```
