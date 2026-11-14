---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/multi-level-dropdown-hamburger-menu-nested-accordion/"
title: "Multi-Level Accordion Hamburger Dropdown Menu CSS"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "Nested navigation with zero JavaScript and zero fake semantics: every level is a native <details>/<summary> — free keyboard support, free screen-reader…"
has_js: "false"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Level Accordion Hamburger Dropdown Menu CSS
Source: https://codefronts.com/navigation/css-hamburger-menus/multi-level-dropdown-hamburger-menu-nested-accordion/

Nested navigation with zero JavaScript and zero fake semantics: every level is a native <details>/<summary> — free keyboard support, free screen-reader disclosure announcements, free state. The 2024-25 platform upgrades do the rest: the name attribute makes top-level sections exclusive (opening Shop closes Support, accordion behavior that used to be a JS staple), and ::details-content + interpolate-size animate the expansion in supporting engines while everything else gets an honest instant toggle.
## HTML
```html
<section class="chm-22" aria-label="Multi-level accordion menu demo">
  <div class="chm-22__stage">
    <aside class="chm-22__drawer" aria-label="Menu">
      <header class="chm-22__head"><b>Browse</b><span class="chm-22__x" aria-hidden="true"><i></i><i></i><i></i></span></header>
      <nav aria-label="Categories">
        <details class="chm-22__d1" name="chm22-top" open>
          <summary><svg class="chm-22__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>Shop<b class="chm-22__badge">312</b></summary>
          <ul class="chm-22__l2">
            <li><a href="#new">New arrivals</a></li>
            <li>
              <details class="chm-22__d2">
                <summary><svg class="chm-22__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>Clothing</summary>
                <ul class="chm-22__l3">
                  <li><a href="#knitwear">Knitwear</a></li>
                  <li><a href="#outerwear">Outerwear</a></li>
                  <li><a href="#denim">Denim</a></li>
                </ul>
              </details>
            </li>
            <li>
              <details class="chm-22__d2">
                <summary><svg class="chm-22__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>Objects</summary>
                <ul class="chm-22__l3">
                  <li><a href="#ceramics">Ceramics</a></li>
                  <li><a href="#lighting">Lighting</a></li>
                </ul>
              </details>
            </li>
            <li><a href="#archive-sale">Archive sale</a></li>
          </ul>
        </details>
        <details class="chm-22__d1" name="chm22-top">
          <summary><svg class="chm-22__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>Stories</summary>
          <ul class="chm-22__l2">
            <li><a href="#studio-visits">Studio visits</a></li>
            <li><a href="#process">Process notes</a></li>
          </ul>
        </details>
        <details class="chm-22__d1" name="chm22-top">
          <summary><svg class="chm-22__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>Support</summary>
          <ul class="chm-22__l2">
            <li><a href="#shipping">Shipping &amp; returns</a></li>
            <li><a href="#care">Care guides</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </details>
        <a class="chm-22__solo" href="#account">Account</a>
      </nav>
    </aside>
    <p class="chm-22__note" aria-hidden="true">native <code>&lt;details name&gt;</code> — top level is exclusive, keyboard &amp; screen-reader support built in, 0 JS</p>
  </div>
</section>
```
## CSS
```css
.chm-22,
.chm-22 *,
.chm-22 *::before,
.chm-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-22 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.97 0.006 130);
  --panel: oklch(1 0 0);
  --edge: oklch(0.89 0.012 130);
  --ink: oklch(0.24 0.02 140);
  --mut: oklch(0.5 0.018 140);
  --acc: oklch(0.55 0.14 150);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.chm-22__stage {
  min-height: 480px;
  border-radius: 18px;
  border: 1px solid var(--edge);
  background: var(--bg);
  padding: 26px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  align-items: center;
  justify-content: center;
}

.chm-22__drawer {
  width: min(340px,100%);
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: 18px;
  box-shadow: 0 22px 48px -30px oklch(0.3 0.05 145/.55);
  overflow: hidden;
}

.chm-22__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 18px 12px;
  border-bottom: 1px solid var(--edge);
}

.chm-22__head b {
  font-size: 16px;
  letter-spacing: -.01em;
}

.chm-22__x {
  position: relative;
  width: 18px;
  height: 12px;
  opacity: .5;
}

.chm-22__x i {
  position: absolute;
  left: 0;
  width: 18px;
  height: 2px;
  border-radius: 2px;
  background: var(--ink);
}

.chm-22__x i:nth-child(1) {
  top: 0;
}

.chm-22__x i:nth-child(2) {
  top: 5px;
}

.chm-22__x i:nth-child(3) {
  top: 10px;
}

.chm-22 nav {
  padding: 8px 10px 12px;
  display: grid;
}

.chm-22 summary {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 46px;
  padding: 0 10px;
  border-radius: 10px;
  font-size: 14.5px;
  font-weight: 700;
  cursor: pointer;
  list-style: none;
  transition: background .15s,color .15s;
}

.chm-22 summary::-webkit-details-marker {
  display: none;
}

.chm-22 summary:hover {
  background: oklch(0.96 0.01 135);
}

.chm-22 summary:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.chm-22__chev {
  width: 15px;
  height: 15px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  flex: none;
  color: var(--mut);
  transition: rotate .25s cubic-bezier(.2,.7,.2,1);
}

details[open]>summary .chm-22__chev {
  rotate: 90deg;
  color: var(--acc);
}

details[open]>summary {
  color: var(--acc);
}

.chm-22__badge {
  margin-left: auto;
  font-size: 10.5px;
  font-weight: 700;
  color: var(--mut);
  background: oklch(0.94 0.01 135);
  border-radius: 99px;
  padding: 2.5px 8px;
  font-variant-numeric: tabular-nums;
}

.chm-22__l2 {
  list-style: none;
  padding: 2px 0 8px 14px;
  margin-left: 16px;
  border-left: 1.5px solid var(--edge);
  display: grid;
}

.chm-22__l3 {
  list-style: none;
  padding: 2px 0 6px 14px;
  margin-left: 16px;
  border-left: 1.5px solid var(--edge);
  display: grid;
}

.chm-22__l2 a,
.chm-22__l3 a,
.chm-22__solo {
  display: flex;
  align-items: center;
  min-height: 42px;
  padding: 0 10px;
  border-radius: 9px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  transition: background .15s,color .15s,translate .2s;
}

.chm-22__l2 a:hover,
.chm-22__l3 a:hover,
.chm-22__solo:hover,
.chm-22__l2 a:focus-visible,
.chm-22__l3 a:focus-visible,
.chm-22__solo:focus-visible {
  background: oklch(0.96 0.01 135);
  color: var(--ink);
  translate: 2px 0;
}

.chm-22__l2 a:focus-visible,
.chm-22__l3 a:focus-visible,
.chm-22__solo:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.chm-22__d2 summary {
  min-height: 42px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--mut);
}

.chm-22__d2[open]>summary {
  color: var(--acc);
}

.chm-22__solo {
  font-weight: 700;
  color: var(--ink);
  border-top: 1px solid var(--edge);
  border-radius: 0;
  margin-top: 6px;
  padding-top: 4px;
}

@supports (interpolate-size: allow-keywords) {
  .chm-22 {
    background: var(--bg);
    width: 100%;
    min-height: 100vh;
    box-sizing: border-box;
    interpolate-size: allow-keywords;
  }

  .chm-22 details::details-content {
    block-size: 0;
    overflow: hidden;
    transition: block-size .35s cubic-bezier(.2,.7,.2,1),content-visibility .35s allow-discrete;
  }

  .chm-22 details[open]::details-content {
    block-size: auto;
  }
}

.chm-22__note {
  font-size: 12px;
  color: var(--mut);
  text-align: center;
  text-wrap: pretty;
}

.chm-22__note code {
  font: 11px ui-monospace,Menlo,Consolas,monospace;
  background: oklch(0.92 0.012 135);
  border-radius: 5px;
  padding: 1.5px 6px;
}

@media (prefers-reduced-motion: reduce) {
  .chm-22 * {
    transition-duration: .01s !important;
  }
}
```
