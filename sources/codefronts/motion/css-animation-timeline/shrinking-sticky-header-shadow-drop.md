---
source: "codefronts"
url: "https://codefronts.com/motion/css-animation-timeline/shrinking-sticky-header-shadow-drop/"
title: "Shrinking Sticky Header + Shadow Drop"
section: "motion"
category: "css-animation-timeline"
category_name: "CSS animation-timeline Demos"
description: "The SaaS-navbar classic without a single scroll listener: a tall, transparent hero navigation compresses into a compact, frosted, shadowed bar over the first…"
has_js: "false"
---

Here's a working CSS animation-timeline Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Shrinking Sticky Header + Shadow Drop
Source: https://codefronts.com/motion/css-animation-timeline/shrinking-sticky-header-shadow-drop/

The SaaS-navbar classic without a single scroll listener: a tall, transparent hero navigation compresses into a compact, frosted, shadowed bar over the first 160px of scroll — logo scales down, background fades in, shadow drops — all scrubbed by animation-timeline: scroll() with a pixel-perfect animation-range.
## HTML
```html
<section class="sda-03" aria-label="Page with shrinking sticky header" role="region" tabindex="0">
  <header class="sda-03__nav">
    <span class="sda-03__logo">north◆star</span>
    <nav class="sda-03__links" aria-label="Primary"><a href="#" onclick="return false">Product</a><a href="#" onclick="return false">Pricing</a><a href="#" onclick="return false">Docs</a><a class="sda-03__cta" href="#" onclick="return false">Start free</a></nav>
  </header>
  <div class="sda-03__hero"><h2>Scroll. Watch the nav earn its keep.</h2><p>160 pixels of scroll drive the whole transition — padding, backdrop, shadow and logo scale — with zero event listeners.</p></div>
  <div class="sda-03__body">
    <h3>Why not just toggle a .scrolled class?</h3>
    <p>A class toggle is binary: the bar jumps between two states at a threshold, and the listener that powers it runs on the main thread for the lifetime of the page. Here the transition is continuous — half-scrolled means half-shrunk — and it costs nothing after style resolution.</p>
    <p>Refresh this panel mid-scroll and the header is already compact on first paint. JS versions flash their tall state until hydration catches up; a scroll timeline is resolved before the first frame renders.</p>
    <p>Keep scrolling to confirm the end state holds forever — <code>animation-fill-mode: both</code> clamps the keyframes outside the 160px range, so there is nothing to re-trigger, ever.</p>
    <p>Scroll back to the very top and the bar relaxes to its tall, transparent hero state — perfectly reversible, because it was never a state machine in the first place.</p>
  </div>
</section>
```
## CSS
```css
.sda-03,
.sda-03 *,
.sda-03 *::before,
.sda-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sda-03 {
  --ink: oklch(0.25 0.02 260);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(oklch(0.93 0.03 220),#f6f7f9 420px);
  color: var(--ink);
  width: 100%;
  height: 100vh;
  overflow-y: auto;
}

.sda-03__nav {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  padding: 14px 28px;
  background: rgba(255,255,255,.92);
  border-bottom: 1px solid rgba(20,25,45,.12);
  box-shadow: 0 8px 24px -14px rgba(20,25,45,.35);
  backdrop-filter: blur(10px);
}

.sda-03__logo {
  font-weight: 800;
  font-size: 19px;
  letter-spacing: -.02em;
  transform-origin: left center;
}

.sda-03__links {
  display: flex;
  align-items: center;
  gap: 22px;
}

.sda-03__links a {
  font-size: 14px;
  font-weight: 600;
  color: var(--ink);
  text-decoration: none;
}

.sda-03__links a:hover {
  color: oklch(0.55 0.18 264);
}

.sda-03__links a:focus-visible {
  outline: 2px solid oklch(0.55 0.18 264);
  outline-offset: 3px;
  border-radius: 4px;
}

.sda-03__cta {
  background: oklch(0.55 0.18 264);
  color: #fff !important;
  padding: 8px 16px;
  border-radius: 999px;
}

.sda-03__cta:hover {
  background: oklch(0.48 0.18 264);
}

.sda-03__hero {
  min-height: 62vh;
  display: grid;
  place-content: center;
  text-align: center;
  padding: 40px 24px;
  gap: 14px;
}

.sda-03__hero h2 {
  font-size: clamp(28px,4.5vw,46px);
  font-weight: 800;
  letter-spacing: -.025em;
  text-wrap: pretty;
}

.sda-03__hero p {
  font-size: 17px;
  color: oklch(0.45 0.03 260);
  max-width: 52ch;
  margin: 0 auto;
  line-height: 1.6;
}

.sda-03__body {
  width: min(640px,100%);
  margin: 0 auto;
  padding: 30px 24px 30vh;
}

.sda-03__body h3 {
  font-size: 22px;
  font-weight: 700;
  margin-bottom: 14px;
  letter-spacing: -.01em;
}

.sda-03__body p {
  font-size: 16px;
  line-height: 1.7;
  margin-bottom: 20px;
  color: oklch(0.35 0.02 260);
  text-wrap: pretty;
}

.sda-03__body code {
  font: 600 13.5px ui-monospace,Menlo,monospace;
  background: #e8eaf1;
  padding: 2px 6px;
  border-radius: 5px;
}

.sda-03:focus-visible {
  outline: 3px solid oklch(0.55 0.18 264);
  outline-offset: -3px;
}

@supports (animation-timeline: scroll()) {
  .sda-03__nav {
    animation: sda-03-condense linear both;
    animation-timeline: scroll();
    animation-range: 0 160px;
  }

  .sda-03__logo {
    animation: sda-03-logo linear both;
    animation-timeline: scroll();
    animation-range: 0 160px;
  }
}

@keyframes sda-03-condense {
  from {
    padding-top: 30px;
    padding-bottom: 30px;
    background: rgba(255,255,255,0);
    border-color: transparent;
    box-shadow: 0 8px 24px -14px rgba(20,25,45,0);
    backdrop-filter: blur(0px);
  }

  to {
    padding-top: 14px;
    padding-bottom: 14px;
    background: rgba(255,255,255,.92);
    border-color: rgba(20,25,45,.12);
    box-shadow: 0 8px 24px -14px rgba(20,25,45,.35);
    backdrop-filter: blur(10px);
  }
}

@keyframes sda-03-logo {
  from {
    transform: scale(1.35);
  }

  to {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sda-03__nav,
    .sda-03__logo {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the header's condense + shadow and the logo's scale are both scrubbed over the first 160px of scroll via animation-range: 0 160px on a scroll() timeline. */
```
