---
source: "codefronts"
url: "https://codefronts.com/motion/css-infinite-marquee/flash-sale-announcement-bar/"
title: "Flash Sale Announcement Bar — Fast, High-Contrast, Dismissible"
section: "motion"
category: "css-infinite-marquee"
category_name: "CSS Infinite Marquee Designs"
description: "The urgency pattern e-commerce lives on: a fast, high-contrast marquee bar pinned to the top of the page shouting a limited-time offer, with a working…"
has_js: "false"
---

Here's a working CSS Infinite Marquee Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Flash Sale Announcement Bar — Fast, High-Contrast, Dismissible
Source: https://codefronts.com/motion/css-infinite-marquee/flash-sale-announcement-bar/

The urgency pattern e-commerce lives on: a fast, high-contrast marquee bar pinned to the top of the page shouting a limited-time offer, with a working promo-code link, a dismiss button that collapses the bar with pure CSS (:has() + a checkbox), and a grid-template-rows animation so the page content slides up smoothly instead of jumping.
## HTML
```html
<section class="mqs-06" aria-label="Flash sale announcement bar demo">
  <input class="mqs-06__closeBox" type="checkbox" id="mqs-06-close">
  <div class="mqs-06__collapse">
    <div class="mqs-06__clip">
      <div class="mqs-06__bar">
        <div class="mqs-06__viewport">
          <div class="mqs-06__group">
            <span class="mqs-06__msg">Flash sale — 40% off everything ends tonight</span><span class="mqs-06__zap" aria-hidden="true">⚡</span>
            <span class="mqs-06__msg">Use code <a class="mqs-06__code" href="#deal">BLITZ40</a> at checkout</span><span class="mqs-06__zap" aria-hidden="true">⚡</span>
          </div>
          <div class="mqs-06__group" aria-hidden="true">
            <span class="mqs-06__msg">Flash sale — 40% off everything ends tonight</span><span class="mqs-06__zap">⚡</span>
            <span class="mqs-06__msg">Use code <span class="mqs-06__code">BLITZ40</span> at checkout</span><span class="mqs-06__zap">⚡</span>
          </div>
        </div>
        <label class="mqs-06__closeBtn" for="mqs-06-close" title="Dismiss announcement"><span aria-hidden="true">✕</span><span class="mqs-06__sr">Dismiss announcement</span></label>
      </div>
    </div>
  </div>
  <div class="mqs-06__page">
    <p class="mqs-06__hint">↑ Page content — dismiss the bar and watch it glide up (pure CSS, no JS).</p>
  </div>
</section>
```
## CSS
```css
.mqs-06,
.mqs-06 *,
.mqs-06 *::before,
.mqs-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.mqs-06 {
  min-height: 100vh;
  width: 100%;
  --gap: 36px;
  --speed: 14s;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #fafaf9;
}

.mqs-06__closeBox {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.mqs-06__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.mqs-06__collapse {
  display: grid;
  grid-template-rows: 1fr;
  transition: grid-template-rows .3s ease;
}

.mqs-06:has(.mqs-06__closeBox:checked) .mqs-06__collapse {
  grid-template-rows: 0fr;
}

.mqs-06__clip {
  min-height: 0;
  overflow: hidden;
}

.mqs-06__bar {
  display: flex;
  align-items: stretch;
  background: #fde047;
  border-bottom: 2px solid #1c1917;
}

.mqs-06__viewport {
  flex: 1;
  display: flex;
  gap: var(--gap);
  overflow: hidden;
  padding-block: 11px;
}

.mqs-06__group {
  flex: none;
  display: flex;
  align-items: center;
  gap: var(--gap);
  animation: mqs-06-scroll var(--speed) linear infinite;
  will-change: transform;
}

@keyframes mqs-06-scroll {
  to {
    transform: translateX(calc(-100% - var(--gap)));
  }
}

.mqs-06__viewport:hover .mqs-06__group,
.mqs-06__viewport:focus-within .mqs-06__group {
  animation-play-state: paused;
}

.mqs-06__msg {
  flex: none;
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: #1c1917;
}

.mqs-06__zap {
  flex: none;
  font-size: 12px;
}

.mqs-06__code {
  color: #1c1917;
  text-decoration: underline;
  text-underline-offset: 3px;
  text-decoration-thickness: 2px;
  border-radius: 3px;
}

.mqs-06__code:hover {
  background: #1c1917;
  color: #fde047;
  text-decoration: none;
  padding-inline: 4px;
}

.mqs-06__code:focus-visible {
  outline: 2px solid #1c1917;
  outline-offset: 2px;
}

.mqs-06__closeBtn {
  flex: none;
  display: grid;
  place-items: center;
  width: 42px;
  font-size: 14px;
  font-weight: 700;
  color: #1c1917;
  cursor: pointer;
  border-left: 2px solid #1c1917;
  transition: background .15s;
}

.mqs-06__closeBtn:hover {
  background: #facc15;
}

.mqs-06__closeBox:focus-visible ~ .mqs-06__collapse .mqs-06__closeBtn {
  outline: 2px solid #1c1917;
  outline-offset: -4px;
}

.mqs-06__page {
  padding: 56px 24px 64px;
  text-align: center;
}

.mqs-06__hint {
  font-size: 13px;
  color: #a8a29e;
}

@media (prefers-reduced-motion: reduce) {
  .mqs-06__group {
    animation: none;
  }

  .mqs-06__viewport {
    overflow-x: auto;
  }

  .mqs-06__collapse {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — dismissal is a checkbox + :has(:checked) flipping grid-template-rows 1fr→0fr (the modern animate-to-height-auto trick). Add 2 lines of localStorage if dismissal should persist. */
```
