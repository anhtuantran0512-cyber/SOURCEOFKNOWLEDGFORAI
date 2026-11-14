---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/modern-glassmorphism-floating-sidebar-design-in-css/"
title: "Floating Sidebar Stacking and Overlay Order"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "Why a floating sidebar with z-index: 9999 can still vanish behind a card."
has_js: "false"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Sidebar Stacking and Overlay Order
Source: https://codefronts.com/navigation/css-sidebar-navigation/modern-glassmorphism-floating-sidebar-design-in-css/

Why a floating sidebar with z-index: 9999 can still vanish behind a card. A transform, filter, opacity below 1 or will-change on an ancestor creates a stacking context, and z-index only orders siblings inside their own context &mdash; so the number is being compared against the wrong things. The panel and its backdrop are siblings in one deliberately isolated context, which is the arrangement that survives.
## HTML
```html
<section class="sdb-18" aria-label="Nova stage">
  <div class="sdb-18__theme">
    <input class="sdb-18__theme-input" type="checkbox" id="sdb-18-theme">
    <label class="sdb-18__theme-label" for="sdb-18-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-18__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-18__scene">
    <div class="sdb-18__content" id="sdb-18-lib">
      <p class="sdb-18__scene-title">Continue watching</p>
      <div class="sdb-18__cards">
        <article class="sdb-18__card"><p>Harbour Wall</p><span>ep 4</span></article>
        <article class="sdb-18__card"><p>Field Recordings</p><span>ep 11</span></article>
        <article class="sdb-18__card"><p>Slack Water</p><span>ep 2</span></article>
        <article class="sdb-18__card"><p>Kestrel</p><span>ep 7</span></article>
        <article class="sdb-18__card"><p>Two Bells</p><span>ep 1</span></article>
        <article class="sdb-18__card"><p>Low Tide</p><span>ep 9</span></article>
      </div>
    </div>

    <div class="sdb-18__layer">
      <div class="sdb-18__backdrop" aria-hidden="true"></div>
      <nav class="sdb-18__panel" aria-label="Nova library">
        <p class="sdb-18__panel-title">Library</p>
        <ul class="sdb-18__list">
          <li><a class="sdb-18__link" href="#sdb-18-lib" aria-current="page">Continue watching</a></li>
          <li><a class="sdb-18__link" href="#sdb-18-lib">My list</a></li>
          <li><a class="sdb-18__link" href="#sdb-18-lib">Downloads</a></li>
          <li><a class="sdb-18__link" href="#sdb-18-lib">Channels</a></li>
          <li><a class="sdb-18__link" href="#sdb-18-lib">Settings</a></li>
        </ul>
      </nav>
    </div>
  </div>
</section>
```
## CSS
```css
.sdb-18 {
  --sdb-18-bg: #070c1a;
  --sdb-18-surf: #0e1730;
  --sdb-18-glass: rgba(20, 32, 64, 0.62);
  --sdb-18-line: #1f2c4d;
  --sdb-18-ink: #e8ecfa;
  --sdb-18-mut: #8e9bc0;
  --sdb-18-acc: #6ff2d0;
  --sdb-18-acc: oklch(88% 0.13 172);
  --sdb-18-acc-soft: #10332f;
  --sdb-18-font-display: "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-18-bg);
  color: var(--sdb-18-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-18 *,
.sdb-18 *::before,
.sdb-18 *::after {
  box-sizing: border-box;
}

.sdb-18:has(.sdb-18__theme-input:checked) {
  --sdb-18-bg: #eef1f8;
  --sdb-18-surf: #ffffff;
  --sdb-18-glass: rgba(255, 255, 255, 0.68);
  --sdb-18-line: #d3d9e8;
  --sdb-18-ink: #101527;
  --sdb-18-mut: #565f7a;
  --sdb-18-acc: #0a6f5c;
  --sdb-18-acc: oklch(46% 0.1 172);
  --sdb-18-acc-soft: #d3ece6;
}

@media (prefers-color-scheme: light) {
  .sdb-18 {
    --sdb-18-bg: #eef1f8;
    --sdb-18-surf: #ffffff;
    --sdb-18-glass: rgba(255, 255, 255, 0.68);
    --sdb-18-line: #d3d9e8;
    --sdb-18-ink: #101527;
    --sdb-18-mut: #565f7a;
    --sdb-18-acc: #0a6f5c;
    --sdb-18-acc: oklch(46% 0.1 172);
    --sdb-18-acc-soft: #d3ece6;
  }

  .sdb-18:has(.sdb-18__theme-input:checked) {
    --sdb-18-bg: #070c1a;
    --sdb-18-surf: #0e1730;
    --sdb-18-glass: rgba(20, 32, 64, 0.62);
    --sdb-18-line: #1f2c4d;
    --sdb-18-ink: #e8ecfa;
    --sdb-18-mut: #8e9bc0;
    --sdb-18-acc: #6ff2d0;
    --sdb-18-acc: oklch(88% 0.13 172);
    --sdb-18-acc-soft: #10332f;
  }
}

@media (prefers-color-scheme: dark) {
  .sdb-18:has(.sdb-18__theme-input:checked) {
    --sdb-18-bg: #eef1f8;
    --sdb-18-surf: #ffffff;
    --sdb-18-glass: rgba(255, 255, 255, 0.68);
    --sdb-18-line: #d3d9e8;
    --sdb-18-ink: #101527;
    --sdb-18-mut: #565f7a;
    --sdb-18-acc: #0a6f5c;
    --sdb-18-acc: oklch(46% 0.1 172);
    --sdb-18-acc-soft: #d3ece6;
  }
}

.sdb-18__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 90;
}

.sdb-18__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-18__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 0.9rem;
  border: 1px solid var(--sdb-18-line);
  background: var(--sdb-18-surf);
  color: var(--sdb-18-ink);
  cursor: pointer;
}

.sdb-18__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-18__theme-input:focus-visible + .sdb-18__theme-label {
  outline: 2px solid var(--sdb-18-acc);
  outline-offset: 2px;
}

.sdb-18__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}
/* isolation: isolate declares this subtree as one stacking unit deliberately,
   rather than getting a context by accident from a transform. */

.sdb-18__scene {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  min-block-size: 100vh;
  background: var(--sdb-18-surf);
  padding: 1.25rem;
}

@media (min-width: 46rem) {
  .sdb-18__scene {
    padding: 2rem;
  }
}

.sdb-18__content {
  min-inline-size: 0;
  padding-inline-end: 4rem;
}

@media (min-width: 46rem) {
  .sdb-18__content {
    padding-inline-end: 17rem;
  }
}

.sdb-18__scene-title {
  margin: 0 0 0.9rem;
  font-family: var(--sdb-18-font-display);
  font-size: 0.78rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--sdb-18-mut);
}

.sdb-18__cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(8.5rem, 1fr));
  gap: 0.7rem;
}

.sdb-18__card {
  min-inline-size: 0;
  aspect-ratio: 3 / 4;
  padding: 0.7rem;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 0.15rem;
  border-radius: 0.8rem;
  background: var(--sdb-18-bg);
  border: 1px solid var(--sdb-18-line);
}

.sdb-18__card p {
  margin: 0;
  font-size: 0.88rem;
  font-weight: 600;
  min-inline-size: 0;
}

.sdb-18__card span {
  font-size: 0.74rem;
  color: var(--sdb-18-mut);
}

.sdb-18__card:nth-child(2) {
  border-color: var(--sdb-18-acc);
}

.sdb-18__layer {
  position: absolute;
  inset: 0;
  z-index: 20;
  pointer-events: none;
}

.sdb-18__backdrop {
  position: absolute;
  inset: 0;
  z-index: 30;
  background: rgba(4, 8, 20, 0.28);
}

.sdb-18__panel {
  position: absolute;
  z-index: 40;
  inset-block: 1.5rem;
  inset-inline-end: 1.5rem;
  inline-size: min(14.5rem, 62%);
  pointer-events: auto;
  display: flex;
  flex-direction: column;
  padding: 0.8rem;
  border-radius: 1rem;
  border: 1px solid var(--sdb-18-line);
  background: var(--sdb-18-glass);
  -webkit-backdrop-filter: blur(14px) saturate(140%);
  backdrop-filter: blur(14px) saturate(140%);
  box-shadow: 0 1.2rem 2.6rem rgba(3, 6, 16, 0.45);
}

.sdb-18__panel-title {
  margin: 0 0 0.6rem;
  font-family: var(--sdb-18-font-display);
  font-size: 0.7rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--sdb-18-mut);
}

.sdb-18__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.15rem;
}

.sdb-18__link {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: 0.45rem 0.6rem;
  border-radius: 0.7rem;
  color: var(--sdb-18-ink);
  text-decoration: none;
  font-size: 0.88rem;
  min-inline-size: 0;
}

.sdb-18__link:hover {
  background: var(--sdb-18-acc-soft);
}

.sdb-18__link[aria-current="page"] {
  background: var(--sdb-18-acc);
  color: var(--sdb-18-bg);
  font-weight: 650;
}

.sdb-18__link:focus-visible {
  outline: 2px solid var(--sdb-18-acc);
  outline-offset: 2px;
}

@media (max-width: 32rem) {
  .sdb-18__layer {
    position: static;
  }

  .sdb-18__backdrop {
    display: none;
  }

  .sdb-18__panel {
    position: static;
    inline-size: 100%;
    margin-block-start: 1rem;
  }

  .sdb-18__content {
    padding-inline-end: 0;
  }
}
```
