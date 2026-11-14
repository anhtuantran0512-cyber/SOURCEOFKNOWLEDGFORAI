---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/fixed-sticky-header-with-shrinking-hamburger-icon/"
title: "Sticky Navbar Shrinking Hamburger Icon on Scroll"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "The shrinking header, finally without a scroll listener: CSS scroll-driven animations bind a keyframe track to the scroll position itself, so the navbar…"
has_js: "false"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Navbar Shrinking Hamburger Icon on Scroll
Source: https://codefronts.com/navigation/css-hamburger-menus/fixed-sticky-header-with-shrinking-hamburger-icon/

The shrinking header, finally without a scroll listener: CSS scroll-driven animations bind a keyframe track to the scroll position itself, so the navbar compresses from 76px to 56px, the wordmark tightens, the burger slims and a frosted border fades in — all proportional to the first 140px of scroll, running compositor-side even mid-fling. Scroll the card's content and watch; there is no JavaScript on this page, and the scrubbing is bidirectional for free.
## HTML
```html
<section class="chm-25" aria-label="Shrinking sticky navbar on scroll demo">
  <div class="chm-25__stage">
    <div class="chm-25__scroll">
      <header class="chm-25__bar">
        <input type="checkbox" id="chm25-t" class="chm-25__state">
        <div class="chm-25__row">
          <span class="chm-25__brand">Meridian</span>
          <label for="chm25-t" class="chm-25__burger" aria-hidden="true"><span><i></i><i></i><i></i></span></label>
        </div>
        <nav class="chm-25__panel" aria-label="Primary">
          <ul>
            <li><a href="#journal">Journal</a></li>
            <li><a href="#maps">Maps</a></li>
            <li><a href="#expeditions">Expeditions</a></li>
          </ul>
        </nav>
      </header>
      <div class="chm-25__body" aria-hidden="true">
        <div class="chm-25__hero"><b>Scroll ↓</b><span>the header compresses over the first 140px — pure CSS</span></div>
        <div class="chm-25__ln" style="--w:88%"></div><div class="chm-25__ln" style="--w:72%"></div><div class="chm-25__ln" style="--w:80%"></div><div class="chm-25__ln" style="--w:56%"></div>
        <div class="chm-25__card"></div>
        <div class="chm-25__ln" style="--w:84%"></div><div class="chm-25__ln" style="--w:66%"></div><div class="chm-25__ln" style="--w:77%"></div><div class="chm-25__ln" style="--w:49%"></div>
        <div class="chm-25__card chm-25__card--b"></div>
        <div class="chm-25__ln" style="--w:81%"></div><div class="chm-25__ln" style="--w:59%"></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.chm-25,
.chm-25 *,
.chm-25 *::before,
.chm-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-25 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.985 0.004 250);
  --edge: oklch(0.9 0.008 250);
  --ink: oklch(0.24 0.018 255);
  --mut: oklch(0.54 0.014 255);
  --acc: oklch(0.55 0.15 240);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  display: grid;
  justify-content: center;
}

.chm-25__stage {
  width: min(420px,88cqi,88vw);
  height: 540px;
  border-radius: 24px;
  overflow: hidden;
  background: var(--bg);
  border: 1px solid var(--edge);
}

.chm-25__scroll {
  height: 100%;
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-gutter: stable;
}

.chm-25__bar {
  position: sticky;
  top: 0;
  z-index: 2;
  padding: 18px 20px;
  background: oklch(0.985 0.004 250/.4);
  animation: chm25-shrink linear both;
  animation-timeline: scroll(nearest);
  animation-range: 0 140px;
}

@keyframes chm25-shrink {
  to {
    padding-block: 8px;
    background: oklch(0.99 0.003 250/.85);
    box-shadow: 0 1px 0 var(--edge),0 8px 24px -18px oklch(0 0 0/.3);
    -webkit-backdrop-filter: blur(10px);
    backdrop-filter: blur(10px);
  }
}

.chm-25__state {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.chm-25__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.chm-25__brand {
  font-size: 17px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  animation: chm25-brand linear both;
  animation-timeline: scroll(nearest);
  animation-range: 0 140px;
}

@keyframes chm25-brand {
  to {
    font-size: 14.5px;
    letter-spacing: .1em;
  }
}

.chm-25__burger {
  width: 46px;
  height: 46px;
  display: grid;
  place-items: center;
  border: 1px solid var(--edge);
  border-radius: 12px;
  background: oklch(1 0 0);
  cursor: pointer;
  transition: background .2s;
  animation: chm25-btn linear both;
  animation-timeline: scroll(nearest);
  animation-range: 0 140px;
}

@keyframes chm25-btn {
  to {
    width: 38px;
    height: 38px;
    border-radius: 10px;
  }
}

.chm-25__burger:hover {
  background: oklch(0.96 0.006 250);
}

.chm-25__state:focus-visible ~ .chm-25__row .chm-25__burger {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.chm-25__burger span {
  position: relative;
  width: 18px;
  height: 12px;
  display: block;
  scale: 1;
  animation: chm25-ico linear both;
  animation-timeline: scroll(nearest);
  animation-range: 0 140px;
}

@keyframes chm25-ico {
  to {
    scale: .85;
  }
}

.chm-25__burger i {
  position: absolute;
  left: 0;
  width: 18px;
  height: 2px;
  border-radius: 2px;
  background: var(--ink);
  transition: translate .28s,rotate .28s .04s,opacity .2s;
}

.chm-25__burger i:nth-child(1) {
  top: 0;
}

.chm-25__burger i:nth-child(2) {
  top: 5px;
}

.chm-25__burger i:nth-child(3) {
  top: 10px;
}

.chm-25__state:checked ~ .chm-25__row .chm-25__burger i:nth-child(1) {
  translate: 0 5px;
  rotate: 45deg;
}

.chm-25__state:checked ~ .chm-25__row .chm-25__burger i:nth-child(2) {
  opacity: 0;
}

.chm-25__state:checked ~ .chm-25__row .chm-25__burger i:nth-child(3) {
  translate: 0 -5px;
  rotate: -45deg;
}

.chm-25__panel {
  display: grid;
  grid-template-rows: 0fr;
  opacity: 0;
  transition: grid-template-rows .35s cubic-bezier(.2,.7,.2,1),opacity .25s;
}

.chm-25__state:checked ~ .chm-25__panel {
  grid-template-rows: 1fr;
  opacity: 1;
}

.chm-25__panel ul {
  list-style: none;
  overflow: hidden;
  min-height: 0;
}

.chm-25__panel a {
  display: flex;
  align-items: center;
  min-height: 44px;
  padding: 0 4px;
  font-size: 14px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  border-bottom: 1px solid color-mix(in oklch,var(--edge) 60%,transparent);
  transition: color .15s,padding .2s;
}

.chm-25__panel a:hover,
.chm-25__panel a:focus-visible {
  color: var(--acc);
  padding-left: 10px;
}

.chm-25__panel a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.chm-25__panel li:first-child a {
  margin-top: 12px;
  border-top: 1px solid color-mix(in oklch,var(--edge) 60%,transparent);
}

.chm-25__body {
  padding: 18px 20px 26px;
  display: grid;
  gap: 14px;
}

.chm-25__hero {
  height: 200px;
  border-radius: 16px;
  background: linear-gradient(150deg,oklch(0.9 0.04 235),oklch(0.82 0.07 255));
  display: flex;
  flex-direction: column;
  justify-content: end;
  gap: 4px;
  padding: 18px;
}

.chm-25__hero b {
  font-size: 24px;
  letter-spacing: -.01em;
}

.chm-25__hero span {
  font-size: 12.5px;
  color: oklch(0.4 0.05 255);
}

.chm-25__card {
  height: 130px;
  border-radius: 14px;
  background: oklch(1 0 0);
  border: 1px solid var(--edge);
}

.chm-25__card--b {
  background: linear-gradient(150deg,oklch(0.93 0.02 200),oklch(0.88 0.04 180));
}

.chm-25__ln {
  height: 11px;
  width: var(--w);
  border-radius: 99px;
  background: oklch(0.91 0.006 250);
}

@media (prefers-reduced-motion: reduce) {
  .chm-25 * {
    animation: none !important;
    transition-duration: .01s !important;
  }
}
```
