---
source: "codefronts"
url: "https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-masonry-style-layout/"
title: "CSS Flexbox Masonry-Style Layout"
section: "layouts"
category: "css-flexbox-layouts"
category_name: "CSS Flexbox Layouts"
description: "A multi-column masonry-style card waterfall using flex-direction: column and flex-wrap: wrap with a fixed container height — no JavaScript required."
has_js: "false"
---

Here's a working CSS Flexbox Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Flexbox Masonry-Style Layout
Source: https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-masonry-style-layout/

A multi-column masonry-style card waterfall using flex-direction: column and flex-wrap: wrap with a fixed container height — no JavaScript required.
## HTML
```html
<div class="fl-04">
  <div class="fl-04__header">
    <h2 class="fl-04__title">CSS Flexbox Masonry-Style Layout</h2>
    <div class="fl-04__badge">flex-direction: column + flex-wrap</div>
  </div>

  <div class="fl-04__masonry">

    <!-- Col items — varied heights via padding/content -->
    <div class="fl-04__item">
      <div class="fl-04__item-visual" style="height:100px; background:linear-gradient(135deg,#1a0a2e,#4a1a8c)">
        <div class="fl-04__shape" style="width:52px;height:52px;background:#e040fb;opacity:0.7"></div>
      </div>
      <div class="fl-04__item-body">
        <div class="fl-04__item-cat">Layout</div>
        <div class="fl-04__item-title">Column-Wrap Masonry</div>
        <div class="fl-04__item-text">Set <code>flex-direction: column</code> and <code>flex-wrap: wrap</code> with a fixed container height to make items flow into natural columns.</div>
        <div class="fl-04__item-tags">
          <div class="fl-04__tag">flex-wrap</div>
          <div class="fl-04__tag">column</div>
        </div>
      </div>
    </div>

    <div class="fl-04__item">
      <div class="fl-04__item-visual" style="height:70px; background:linear-gradient(135deg,#001a33,#004080)">
        <div class="fl-04__shape" style="width:44px;height:44px;background:#06b6d4;opacity:0.8;border-radius:30% 70% 70% 30%"></div>
      </div>
      <div class="fl-04__item-body">
        <div class="fl-04__item-cat">Sizing</div>
        <div class="fl-04__item-title">Item Width</div>
        <div class="fl-04__item-text">Items need a fixed <code>width</code> (e.g. 33%) — not <code>flex</code> shorthand — so each column stays the same width.</div>
      </div>
    </div>

    <div class="fl-04__item">
      <div class="fl-04__item-visual" style="height:130px; background:linear-gradient(135deg,#1a0500,#4d1a00)">
        <div class="fl-04__shape" style="width:68px;height:68px;background:#f59e0b;opacity:0.8;border-radius:60% 40% 30% 70%"></div>
      </div>
      <div class="fl-04__item-body">
        <div class="fl-04__item-cat">Container</div>
        <div class="fl-04__item-title">The Height Constraint Controls Column Count</div>
        <div class="fl-04__item-text">The container's fixed height determines when items wrap to a new column. Taller height = fewer columns. This is the key insight for this technique.</div>
        <div class="fl-04__item-tags">
          <div class="fl-04__tag">height</div>
          <div class="fl-04__tag">wrap boundary</div>
        </div>
      </div>
    </div>

    <div class="fl-04__item">
      <div class="fl-04__item-visual" style="height:90px; background:linear-gradient(135deg,#001a12,#004d35)">
        <div class="fl-04__shape" style="width:56px;height:56px;background:#10b981;opacity:0.8;border-radius:40% 60% 55% 45%"></div>
      </div>
      <div class="fl-04__item-body">
        <div class="fl-04__item-cat">Gap</div>
        <div class="fl-04__item-title">Gutters with gap</div>
        <div class="fl-04__item-text">The <code>gap</code> shorthand sets row and column gutters uniformly without margin edge-cases.</div>
      </div>
    </div>

    <div class="fl-04__item">
      <div class="fl-04__item-visual" style="height:80px; background:linear-gradient(135deg,#1a0a1a,#4a1a4a)">
        <div class="fl-04__shape" style="width:48px;height:48px;background:#e040fb;opacity:0.7"></div>
      </div>
      <div class="fl-04__item-body">
        <div class="fl-04__item-cat">Caveat</div>
        <div class="fl-04__item-title">Reading Order Is Top-Down</div>
        <div class="fl-04__item-text">Items flow column-first, not row-first. For strict row order, use CSS Grid instead.</div>
      </div>
    </div>

    <div class="fl-04__item">
      <div class="fl-04__item-visual" style="height:110px; background:linear-gradient(135deg,#1a1000,#4d3300)">
        <div class="fl-04__shape" style="width:62px;height:62px;background:#f59e0b;opacity:0.7;border-radius:50% 50% 30% 70%"></div>
      </div>
      <div class="fl-04__item-body">
        <div class="fl-04__item-cat">Responsive</div>
        <div class="fl-04__item-title">Dynamic Column Count via Container Height</div>
        <div class="fl-04__item-text">Use a CSS custom property for container height and update it via JS or @media queries to control how many columns appear at each breakpoint.</div>
        <div class="fl-04__item-tags">
          <div class="fl-04__tag">responsive</div>
          <div class="fl-04__tag">custom props</div>
        </div>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.fl-04,
.fl-04 *,
.fl-04 *::before,
.fl-04 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.fl-04 ::selection {
  background: #e040fb;
  color: #fff;
}

.fl-04 {
  --bg: #f4f0ff;
  --surface: #fff;
  --ink: #1a0a2e;
  --muted: #8a7fa8;
  --accent: #7c3aed;
  --accent2: #e040fb;
  --accent3: #06b6d4;
  --accent4: #f59e0b;
  --border: rgba(124,58,237,0.12);
  font-family: 'Space Grotesk', sans-serif;
  background: var(--bg);
  padding: 24px;
  border-radius: 16px;
  min-height: 500px;
}

.fl-04__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.fl-04__title {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--ink);
}

.fl-04__badge {
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  background: var(--accent);
  color: #fff;
  padding: 4px 10px;
  border-radius: 20px;
}
/*
  Flexbox masonry: flex-direction column + flex-wrap wrap
  Height of container controls how many items per column.
  Items flow top→bottom then start a new column.
  Defensive overflow:hidden prevents excess columns from bleeding past
  the parent width at narrow viewports — the masonry algorithm doesn't
  shrink column count on its own, it just keeps packing.
*/

.fl-04__masonry {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  gap: 12px;
  height: 760px;
  /* controls column count at desktop width */
  overflow: hidden;
}

.fl-04__item {
  width: calc(33.33% - 8px);
  background: var(--surface);
  border-radius: 14px;
  overflow: hidden;
  border: 1px solid var(--border);
  break-inside: avoid;
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  transition: transform 0.2s, box-shadow 0.2s;
}

.fl-04__item:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 30px rgba(124,58,237,0.15);
}

.fl-04__item-visual {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.fl-04__item-visual-inner {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.fl-04__shape {
  border-radius: 50%;
  animation: fl-04-float 4s ease-in-out infinite;
}

@keyframes fl-04-float {
  0%,
    100% {
    transform: translateY(0) rotate(0deg);
  }

  50% {
    transform: translateY(-6px) rotate(8deg);
  }
}

.fl-04__item:nth-child(3n+2) .fl-04__shape {
  animation-delay: -1.5s;
}

.fl-04__item:nth-child(3n+3) .fl-04__shape {
  animation-delay: -3s;
}

.fl-04__item-body {
  padding: 14px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  flex: 1;
}

.fl-04__item-cat {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}

.fl-04__item-title {
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--ink);
  line-height: 1.3;
}

.fl-04__item-text {
  font-size: 0.77rem;
  color: var(--muted);
  line-height: 1.6;
}

.fl-04__item-tags {
  display: flex;
  gap: 4px;
  flex-wrap: wrap;
  margin-top: 4px;
}

.fl-04__tag {
  font-size: 0.65rem;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 20px;
  background: rgba(124,58,237,0.1);
  color: var(--accent);
}
/* Responsive masonry. The flex-direction:column masonry algorithm
   doesn't auto-reduce column count when items get narrow — we have to
   adjust the container height + item width per breakpoint or items
   keep wrapping into more columns. */

@media (max-width: 760px) {
  .fl-04__masonry {
    height: 1100px;
  }

  .fl-04__item {
    width: calc(50% - 6px);
  }
}

@media (max-width: 520px) {
  .fl-04__masonry {
    flex-wrap: nowrap;
    height: auto;
    overflow: visible;
  }

  .fl-04__item {
    width: 100%;
  }

  .fl-04__header {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fl-04__shape {
    animation: none;
  }

  .fl-04__item {
    transition: none;
  }
}
```
