---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/footer-pinned-sidebar/"
title: "CSS Sidebar Menu with Sticky User Profile Footer"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "Navigation up top, user profile locked to the bottom — the one-line layout answer is margin-top:auto in a flex column."
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sidebar Menu with Sticky User Profile Footer
Source: https://codefronts.com/layouts/css-sidebar-layouts/footer-pinned-sidebar/

Navigation up top, user profile locked to the bottom — the one-line layout answer is margin-top:auto in a flex column. The middle nav scrolls independently when it outgrows the rail, while brand header and profile footer never move, with fade masks hinting at the scrollable overflow.
## HTML
```html
<section class="sbl-17">
  <aside class="sbl-17__rail">
    <div class="sbl-17__brand"><span aria-hidden="true"></span>Basecamp OS</div>
    <nav class="sbl-17__nav" aria-label="Main">
      <a href="#" aria-current="page">Today</a><a href="#">Projects</a><a href="#">Messages</a><a href="#">Schedule</a><a href="#">Docs &amp; files</a><a href="#">Check-ins</a><a href="#">Reports</a><a href="#">Integrations</a><a href="#">Templates</a><a href="#">Archive</a>
    </nav>
    <a class="sbl-17__user" href="#">
      <span class="sbl-17__avatar" aria-hidden="true">JV<i></i></span>
      <span class="sbl-17__id"><strong>Jonas Vieira</strong><small>Product · online</small></span>
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="m8 9 4-4 4 4m-8 6 4 4 4-4"/></svg>
    </a>
  </aside>
  <main class="sbl-17__main"><h1>Today</h1><p>The nav scrolls in the middle (note the fade masks); brand and profile never move. One margin-top:auto does the pinning.</p></main>
</section>
```
## CSS
```css
.sbl-17,
.sbl-17 *,
.sbl-17 *::before,
.sbl-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-17 {
  --panel: oklch(0.17 0.016 60);
  --ink: oklch(0.94 0.006 60);
  --mut: oklch(0.65 0.015 60);
  --line: oklch(0.28 0.018 60);
  --accent: oklch(0.76 0.13 65);
  display: grid;
  grid-template-columns: 256px 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.13 0.012 60);
  color: var(--ink);
}

.sbl-17__rail {
  display: flex;
  flex-direction: column;
  height: 100%;
  background: var(--panel);
  border-right: 1px solid var(--line);
}

.sbl-17__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font: 700 15px/1 system-ui,sans-serif;
  padding: 20px 22px 16px;
}

.sbl-17__brand span {
  width: 26px;
  height: 26px;
  border-radius: 8px;
  background: conic-gradient(from 300deg,var(--accent),oklch(0.6 0.14 30));
}

.sbl-17__nav {
  flex: 1;
  min-height: 0;
  overflow-y: auto;
  overscroll-behavior: contain;
  display: flex;
  flex-direction: column;
  gap: 2px;
  padding: 8px 12px;
  scroll-padding: 20px 0;
  -webkit-mask-image: linear-gradient(180deg,transparent,#000 16px,#000 calc(100% - 16px),transparent);
  mask-image: linear-gradient(180deg,transparent,#000 16px,#000 calc(100% - 16px),transparent);
}

.sbl-17__nav a {
  flex: none;
  padding: 11px 14px;
  border-radius: 10px;
  font: 500 14px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  transition: background-color .18s ease,color .18s ease;
}

.sbl-17__nav a:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 6%,transparent);
}

.sbl-17__nav a[aria-current="page"] {
  color: var(--ink);
  background: color-mix(in oklab,var(--accent) 16%,transparent);
  box-shadow: inset 2px 0 0 var(--accent);
}

.sbl-17__nav a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-17__user {
  margin-top: auto;
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 11px;
  padding: 14px 16px;
  border-top: 1px solid var(--line);
  text-decoration: none;
  color: inherit;
  transition: background-color .18s ease;
}

.sbl-17__user:hover {
  background: color-mix(in oklab,var(--ink) 5%,transparent);
}

.sbl-17__user:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.sbl-17__avatar {
  position: relative;
  display: grid;
  place-items: center;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  font: 700 11px/1 system-ui,sans-serif;
  color: #fff;
  background: linear-gradient(135deg,var(--accent),oklch(0.55 0.15 30));
}

.sbl-17__avatar i {
  position: absolute;
  right: -1px;
  bottom: -1px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: oklch(0.75 0.17 155);
  border: 2px solid var(--panel);
}

.sbl-17__id strong {
  display: block;
  font: 600 13px/1.2 system-ui,sans-serif;
}

.sbl-17__id small {
  font: 400 11px/1.3 system-ui,sans-serif;
  color: var(--mut);
}

.sbl-17__user svg {
  width: 15px;
  height: 15px;
  fill: none;
  stroke: var(--mut);
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sbl-17__main {
  padding: 32px;
  overflow-y: auto;
}

.sbl-17__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-17__main p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.6;
  max-width: 47ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-17__nav a,
    .sbl-17__user {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — flex column rail; margin-top:auto pins the profile, flex:1 + min-height:0 makes only the nav scroll, mask-image fades the overflow. */
```
