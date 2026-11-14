---
source: "codefronts"
url: "https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-mosaic-image-gallery/"
title: "CSS Flexbox Mosaic Image Gallery"
section: "layouts"
category: "css-flexbox-layouts"
category_name: "CSS Flexbox Layouts"
description: "A photo mosaic gallery with three flex columns of varying weights (flex: 2, flex: 1, flex: 1.5) and variable-height tiles, each captioned with a category tag…"
has_js: "false"
---

Here's a working CSS Flexbox Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Flexbox Mosaic Image Gallery
Source: https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-mosaic-image-gallery/

A photo mosaic gallery with three flex columns of varying weights (flex: 2, flex: 1, flex: 1.5) and variable-height tiles, each captioned with a category tag and title — creating an asymmetric editorial grid like Unsplash or Pinterest.
## HTML
```html
<div class="fl-13">
  <div class="fl-13__header">
    <div class="fl-13__heading">
      <h2 class="fl-13__title">Editorial Gallery</h2>
      <span class="fl-13__count">126 photos</span>
    </div>
    <div class="fl-13__view-toggle">
      <button type="button" class="fl-13__view-btn is-active" aria-label="Mosaic view" aria-pressed="true">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="9" rx="1"/><rect x="14" y="3" width="7" height="5" rx="1"/><rect x="14" y="12" width="7" height="9" rx="1"/><rect x="3" y="16" width="7" height="5" rx="1"/></svg>
      </button>
      <button type="button" class="fl-13__view-btn" aria-label="List view" aria-pressed="false">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="18" x2="20" y2="18"/></svg>
      </button>
    </div>
  </div>

  <div class="fl-13__mosaic">

    <!-- Column 1: wide, two rows (short + tall) -->
    <div class="fl-13__col fl-13__col--wide">

      <div class="fl-13__tile fl-13__tile--short" style="--tile-grad:linear-gradient(135deg,#ec4899 0%,#7c3aed 60%,#1e1b4b 100%)">
        <div class="fl-13__tile-bg"></div>
        <div class="fl-13__tile-meta">
          <span class="fl-13__tile-tag">Abstract</span>
          <h3 class="fl-13__tile-title">Magenta Drift</h3>
        </div>
      </div>

      <div class="fl-13__tile fl-13__tile--tall" style="--tile-grad:linear-gradient(160deg,#0ea5e9 0%,#1e40af 55%,#0a1a2e 100%)">
        <div class="fl-13__tile-bg"></div>
        <div class="fl-13__tile-meta">
          <span class="fl-13__tile-tag">Aqua</span>
          <h3 class="fl-13__tile-title">Deep Ocean Study</h3>
          <p class="fl-13__tile-sub">14 images · Editorial</p>
        </div>
      </div>

    </div>

    <!-- Column 2: narrow, two tiles -->
    <div class="fl-13__col fl-13__col--narrow">

      <div class="fl-13__tile fl-13__tile--tall" style="--tile-grad:linear-gradient(160deg,#22c55e 0%,#15803d 55%,#0a1f10 100%)">
        <div class="fl-13__tile-bg"></div>
        <div class="fl-13__tile-meta">
          <span class="fl-13__tile-tag">Organic</span>
          <h3 class="fl-13__tile-title">Green Burst</h3>
        </div>
      </div>

      <div class="fl-13__tile fl-13__tile--short" style="--tile-grad:linear-gradient(135deg,#fbbf24 0%,#f97316 50%,#7c2d12 100%)">
        <div class="fl-13__tile-bg"></div>
        <div class="fl-13__tile-meta">
          <span class="fl-13__tile-tag">Ember</span>
          <h3 class="fl-13__tile-title">Solar Flare</h3>
        </div>
      </div>

    </div>

    <!-- Column 3: mid, two equal tiles -->
    <div class="fl-13__col fl-13__col--mid">

      <div class="fl-13__tile" style="--tile-grad:linear-gradient(135deg,#8b5cf6 0%,#5b21b6 55%,#1e1b4b 100%)">
        <div class="fl-13__tile-bg"></div>
        <div class="fl-13__tile-meta">
          <span class="fl-13__tile-tag">Cosmic</span>
          <h3 class="fl-13__tile-title">Nebula Fragment</h3>
        </div>
      </div>

      <div class="fl-13__tile" style="--tile-grad:linear-gradient(135deg,#f43f5e 0%,#9f1239 55%,#1a0512 100%)">
        <div class="fl-13__tile-bg"></div>
        <div class="fl-13__tile-meta">
          <span class="fl-13__tile-tag">Vermillion</span>
          <h3 class="fl-13__tile-title">Crimson Study</h3>
          <span class="fl-13__tile-more">+ 119 more</span>
        </div>
      </div>

    </div>

  </div>
</div>
```
## CSS
```css
.fl-13,
.fl-13 *,
.fl-13 *::before,
.fl-13 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.fl-13 ::selection {
  background: #ec4899;
  color: #fff;
}

.fl-13 {
  --bg: #0c0a0e;
  --surface: #16131a;
  --ink: #fff;
  --muted: rgba(255,255,255,0.55);
  --accent: #ec4899;
  --border: rgba(255,255,255,0.08);
  font-family: 'Barlow', system-ui, sans-serif;
  background: var(--bg);
  padding: 20px;
  border-radius: 16px;
  min-height: 500px;
}

.fl-13__header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 16px;
}

.fl-13__heading {
  display: flex;
  align-items: baseline;
  gap: 12px;
  min-width: 0;
}

.fl-13__title {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--ink);
  letter-spacing: -0.02em;
}

.fl-13__count {
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--muted);
  letter-spacing: 0.04em;
}

.fl-13__view-toggle {
  display: flex;
  gap: 4px;
  flex-shrink: 0;
}

.fl-13__view-btn {
  width: 30px;
  height: 30px;
  border-radius: 6px;
  background: rgba(255,255,255,0.04);
  border: 1px solid var(--border);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--muted);
  transition: background 0.15s, color 0.15s, border-color 0.15s;
}

.fl-13__view-btn:hover {
  color: var(--ink);
  background: rgba(255,255,255,0.08);
}

.fl-13__view-btn.is-active {
  background: rgba(236,72,153,0.12);
  color: var(--accent);
  border-color: rgba(236,72,153,0.45);
}
/*
  MOSAIC LAYOUT
  Outer container: flex row (3 columns) with proportional flex weights.
  Each column: flex column with two tiles of variable flex weight.
  Result: an asymmetric Pinterest-style grid where the LEFT column
  is widest (flex: 2), the MIDDLE narrowest (flex: 1), and the
  RIGHT in between (flex: 1.5).
*/

.fl-13__mosaic {
  display: flex;
  gap: 12px;
  height: 440px;
}

.fl-13__col {
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-width: 0;
}

.fl-13__col--wide {
  flex: 2;
}

.fl-13__col--narrow {
  flex: 1;
}

.fl-13__col--mid {
  flex: 1.5;
}

.fl-13__tile {
  flex: 1;
  border-radius: 12px;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  isolation: isolate;
  background: var(--surface);
}

.fl-13__tile--tall {
  flex: 1.8;
}

.fl-13__tile--short {
  flex: 1;
}
/* The "image": a gradient stand-in for a real photo. In production,
   replace .fl-13__tile-bg with <img src=...> at the same size + an
   object-fit: cover rule. The scale-on-hover effect still works. */

.fl-13__tile-bg {
  position: absolute;
  inset: 0;
  background: var(--tile-grad, linear-gradient(135deg, #6366f1, #1e1b4b));
  transition: transform 0.45s cubic-bezier(0.2, 0.6, 0.2, 1);
  z-index: 0;
}

.fl-13__tile:hover .fl-13__tile-bg {
  transform: scale(1.05);
}
/* Caption scrim — sits above the image, persistent (not hover-only).
   Linear gradient fades the bottom of the image so white text reads
   cleanly without darkening the whole image. */

.fl-13__tile::after {
  content: '';
  position: absolute;
  inset: auto 0 0 0;
  height: 65%;
  background: linear-gradient(to top,
      rgba(0,0,0,0.78) 0%,
      rgba(0,0,0,0.45) 35%,
      transparent 100%);
  z-index: 1;
  pointer-events: none;
}

.fl-13__tile-meta {
  position: absolute;
  left: 14px;
  right: 14px;
  bottom: 14px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 6px;
  z-index: 2;
  pointer-events: none;
}

.fl-13__tile-tag {
  display: inline-block;
  background: rgba(255,255,255,0.18);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  padding: 3px 10px;
  border-radius: 999px;
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #fff;
}

.fl-13__tile-title {
  font-size: 0.92rem;
  font-weight: 700;
  color: #fff;
  line-height: 1.25;
  letter-spacing: -0.01em;
  text-shadow: 0 1px 4px rgba(0,0,0,0.3);
}

.fl-13__tile-sub {
  font-size: 0.7rem;
  color: rgba(255,255,255,0.78);
  font-weight: 500;
}

.fl-13__tile-more {
  display: inline-block;
  margin-top: 2px;
  padding: 3px 9px;
  border-radius: 999px;
  background: rgba(255,255,255,0.18);
  border: 1px solid rgba(255,255,255,0.25);
  font-size: 0.65rem;
  font-weight: 700;
  color: #fff;
}
/* Smaller tiles need lighter caption so we don't drown the image */

.fl-13__col--narrow .fl-13__tile-title {
  font-size: 0.78rem;
}

.fl-13__col--narrow .fl-13__tile-meta {
  left: 10px;
  right: 10px;
  bottom: 10px;
  gap: 4px;
}

@media (max-width: 720px) {
  .fl-13 {
    padding: 14px;
  }

  .fl-13__mosaic {
    height: 520px;
  }
}

@media (max-width: 520px) {
  /* Below 520px the three-column row gets too cramped. Stack the
       columns vertically — still a flexbox layout, just flipped axis. */

  .fl-13__mosaic {
    flex-direction: column;
    height: auto;
  }

  .fl-13__col {
    flex-direction: row;
    flex: none;
    min-height: 180px;
  }

  .fl-13__col--wide .fl-13__tile--tall {
    flex: 1.6;
  }

  .fl-13__title {
    font-size: 1rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fl-13__tile-bg,
    .fl-13__view-btn {
    transition: none;
  }

  .fl-13__tile:hover .fl-13__tile-bg {
    transform: none;
  }
}
```
