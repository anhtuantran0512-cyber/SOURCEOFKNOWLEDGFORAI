---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/logo-wall/"
title: "Logo Wall"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "The 'trusted by' section done properly: an auto-fit wall where hairline dividers between every cell come from a 1px gap over a background color — one…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Logo Wall
Source: https://codefronts.com/layouts/css-grid-layouts/logo-wall/

The 'trusted by' section done properly: an auto-fit wall where hairline dividers between every cell come from a 1px gap over a background color — one declaration replacing the border-collapse puzzle of nth-child edge cases. Logos sit grayscale at 60%, waking to full color on hover.
## HTML
```html
<section class="cgl-29" aria-label="Logo wall demo">
  <h3 class="cgl-29__title">Powering front-ends at</h3>
  <ul class="cgl-29__wall">
    <li><a href="#0" style="--f:Georgia,serif"><b>Meridian</b></a></li>
    <li><a href="#0" style="--f:ui-monospace,monospace"><b>hexlab_</b></a></li>
    <li><a href="#0"><b>NORTHBEAM</b></a></li>
    <li><a href="#0" style="--f:Georgia,serif"><b><i>Foundry &amp; Co.</i></b></a></li>
    <li><a href="#0"><b>plexus</b></a></li>
    <li><a href="#0" style="--f:ui-monospace,monospace"><b>[cadence]</b></a></li>
    <li><a href="#0"><b>Waypoint</b></a></li>
    <li><a href="#0" style="--f:Georgia,serif"><b>Aurelia</b></a></li>
  </ul>
</section>
```
## CSS
```css
.cgl-29,
.cgl-29 *,
.cgl-29 *::before,
.cgl-29 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-29 {
  width: 100%;
  min-height: 100vh;
  --paper: oklch(0.97 0.006 90);
  --hairline: oklch(0.86 0.012 90);
  --ink: oklch(0.3 0.02 60);
  font-family: system-ui,sans-serif;
  background: var(--paper);
  padding: 1.8rem 1.4rem;
}

.cgl-29 .cgl-29__title {
  font-size: .72rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  text-align: center;
  color: color-mix(in oklab,var(--ink) 55%,var(--paper));
  margin-block-end: 1.2rem;
}

.cgl-29 .cgl-29__wall {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(140px,100%),1fr));
  gap: 1px;
  background: var(--hairline);
  border: 1px solid var(--hairline);
  border-radius: 12px;
  overflow: hidden;
}

.cgl-29 .cgl-29__wall li {
  background: var(--paper);
}

.cgl-29 .cgl-29__wall a {
  display: grid;
  place-items: center;
  min-block-size: 76px;
  padding: 1rem;
  text-decoration: none;
  filter: grayscale(1) opacity(.6);
  transition: filter .3s ease;
}

.cgl-29 .cgl-29__wall a:hover,
.cgl-29 .cgl-29__wall a:focus-visible {
  filter: none;
  outline: none;
  background: color-mix(in oklab,var(--hairline) 30%,var(--paper));
}

.cgl-29 .cgl-29__wall b {
  font-family: var(--f,system-ui);
  font-size: 1.02rem;
  letter-spacing: .02em;
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .cgl-29 .cgl-29__wall a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — gap:1px over a hairline background draws every divider; grayscale filters unify the marks. */
```
