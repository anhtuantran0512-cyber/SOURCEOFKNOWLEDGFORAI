---
source: "codefronts"
url: "https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-magazine-article-layout/"
title: "CSS Flexbox Magazine Article Layout"
section: "layouts"
category: "css-flexbox-layouts"
category_name: "CSS Flexbox Layouts"
description: "A classic editorial magazine layout with a two-thirds article column, one-third sidebar, drop cap, pull quotes, and a multi-column body text — built with…"
has_js: "false"
---

Here's a working CSS Flexbox Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Flexbox Magazine Article Layout
Source: https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-magazine-article-layout/

A classic editorial magazine layout with a two-thirds article column, one-third sidebar, drop cap, pull quotes, and a multi-column body text — built with flex and CSS columns.
## HTML
```html
<div class="fl-08">
  <div class="fl-08__masthead">
    <div class="fl-08__masthead-name">Flex<em>Mag</em></div>
    <div class="fl-08__masthead-date">June 2025 · Issue 47</div>
  </div>

  <div class="fl-08__category-bar">
    <div class="fl-08__cat-tab is-active">Design</div>
    <div class="fl-08__cat-tab">Technology</div>
    <div class="fl-08__cat-tab">Culture</div>
    <div class="fl-08__cat-tab">Opinion</div>
    <div class="fl-08__cat-tab">Data</div>
  </div>

  <div class="fl-08__body">

    <!-- Article column -->
    <div class="fl-08__article-col">
      <div class="fl-08__kicker">
        <div class="fl-08__kicker-label">Cover Story</div>
        <div class="fl-08__kicker-line"></div>
      </div>
      <h1 class="fl-08__headline">The <em>Flexbox</em> Layout Technique That Changed Everything</h1>
      <div class="fl-08__standfirst">How a single CSS property — <code>flex</code> — replaced decades of float hacks, table tricks, and inline-block nightmares to give designers true layout superpowers.</div>
      <div class="fl-08__byline">
        <div class="fl-08__author-avatar">SR</div>
        <div>
          <div class="fl-08__author-name">Sofia Reyes</div>
          <div class="fl-08__author-role">Senior Design Editor</div>
        </div>
        <div class="fl-08__meta">June 12, 2025<br>8 min read</div>
      </div>
      <div class="fl-08__hero">
        <div class="fl-08__hero-text">flex</div>
        <div class="fl-08__hero-label">Illustration: FlexMag / CSS Visual Studio</div>
      </div>
      <div class="fl-08__body-text fl-08__drop-cap">
        <p>Before flexbox arrived in browsers, building a simple three-column layout with equal-height columns was a multi-hack ordeal — you needed faux backgrounds, table-cell hacks, or JavaScript height equalisers. The magazine layout you are reading now is achieved with two flex containers, two lines of alignment CSS, and nothing else.</p>
        <p>The key insight of flexbox is that it separates the axis of layout from the axis of alignment. The main axis — controlled by <code>flex-direction</code> — decides how items are placed. The cross axis — governed by <code>align-items</code> and <code>align-self</code> — decides how they stretch or anchor within their row or column.</p>
      </div>
    </div>

    <!-- Sidebar -->
    <aside class="fl-08__sidebar">
      <div>
        <div class="fl-08__sidebar-section-title">Related Articles</div>
        <div class="fl-08__related-item">
          <div class="fl-08__related-thumb" style="background:linear-gradient(135deg,#1a0010,#5a0040)">
            <span style="font-size:1.2rem">📐</span>
          </div>
          <div>
            <div class="fl-08__related-title">Grid vs Flexbox: When to Use Each</div>
            <div class="fl-08__related-meta">4 min · Design</div>
          </div>
        </div>
        <div class="fl-08__related-item">
          <div class="fl-08__related-thumb" style="background:linear-gradient(135deg,#001a10,#004d30)">
            <span style="font-size:1.2rem">📱</span>
          </div>
          <div>
            <div class="fl-08__related-title">Responsive Layouts Without Media Queries</div>
            <div class="fl-08__related-meta">6 min · CSS</div>
          </div>
        </div>
        <div class="fl-08__related-item">
          <div class="fl-08__related-thumb" style="background:linear-gradient(135deg,#1a1000,#4d3300)">
            <span style="font-size:1.2rem">⚡</span>
          </div>
          <div>
            <div class="fl-08__related-title">Performance Wins With Modern CSS</div>
            <div class="fl-08__related-meta">5 min · Perf</div>
          </div>
        </div>
      </div>
      <div>
        <div class="fl-08__sidebar-section-title">Topics</div>
        <div class="fl-08__tag-cloud">
          <div class="fl-08__tag">Flexbox</div>
          <div class="fl-08__tag">Layout</div>
          <div class="fl-08__tag">CSS Grid</div>
          <div class="fl-08__tag">Responsive</div>
          <div class="fl-08__tag">Typography</div>
          <div class="fl-08__tag">Design Systems</div>
        </div>
      </div>
    </aside>

  </div>
</div>
```
## CSS
```css
.fl-08,
.fl-08 *,
.fl-08 *::before,
.fl-08 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.fl-08 ::selection {
  background: #e11d48;
  color: #fff;
}

.fl-08 {
  --bg: #fffdf9;
  --surface: #fff;
  --ink: #1a1008;
  --muted: #78716c;
  --accent: #e11d48;
  --accent2: #d97706;
  --border: #e8e0d5;
  font-family: 'DM Sans', sans-serif;
  background: var(--bg);
  padding: 0;
  border-radius: 16px;
  overflow: hidden;
  min-height: 500px;
  border: 1px solid var(--border);
}
/* Magazine masthead */

.fl-08__masthead {
  background: var(--ink);
  padding: 14px 28px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.fl-08__masthead-name {
  font-family: 'Fraunces', serif;
  font-size: 1.4rem;
  font-weight: 900;
  color: #fff;
  letter-spacing: -0.02em;
}

.fl-08__masthead-name em {
  color: var(--accent);
  font-style: normal;
}

.fl-08__masthead-date {
  font-size: 0.72rem;
  color: rgba(255,255,255,0.45);
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
/* Category banner */

.fl-08__category-bar {
  display: flex;
  align-items: center;
  gap: 0;
  border-bottom: 1px solid var(--border);
  padding: 0 28px;
  overflow-x: auto;
}

.fl-08__cat-tab {
  padding: 8px 14px;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
  white-space: nowrap;
  cursor: pointer;
  border-bottom: 2px solid transparent;
  transition: color 0.2s, border-color 0.2s;
}

.fl-08__cat-tab.is-active {
  color: var(--accent);
  border-bottom-color: var(--accent);
}

.fl-08__cat-tab:hover {
  color: var(--ink);
}
/* Main layout: flex row — body col (2/3) + sidebar (1/3) */

.fl-08__body {
  display: flex;
  min-height: 0;
}
/* Left body: flex column */

.fl-08__article-col {
  flex: 2;
  min-width: 0;
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  border-right: 1px solid var(--border);
}

.fl-08__kicker {
  display: flex;
  align-items: center;
  gap: 10px;
}

.fl-08__kicker-label {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
}

.fl-08__kicker-line {
  flex: 1;
  height: 1px;
  background: var(--border);
}

.fl-08__headline {
  font-family: 'Fraunces', serif;
  font-size: 1.7rem;
  font-weight: 900;
  color: var(--ink);
  line-height: 1.15;
  letter-spacing: -0.02em;
}

.fl-08__headline em {
  color: var(--accent);
  font-style: italic;
}

.fl-08__standfirst {
  font-family: 'Fraunces', serif;
  font-style: italic;
  font-size: 0.95rem;
  color: var(--muted);
  line-height: 1.6;
  border-left: 3px solid var(--accent);
  padding-left: 14px;
}

.fl-08__byline {
  display: flex;
  align-items: center;
  gap: 10px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border);
}

.fl-08__author-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, #e11d48, #9f1239);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.72rem;
  font-weight: 800;
  color: #fff;
  flex-shrink: 0;
}

.fl-08__author-name {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--ink);
}

.fl-08__author-role {
  font-size: 0.68rem;
  color: var(--muted);
}

.fl-08__meta {
  margin-left: auto;
  font-size: 0.68rem;
  color: var(--muted);
  text-align: right;
}
/* Hero image placeholder */

.fl-08__hero {
  border-radius: 10px;
  overflow: hidden;
  height: 130px;
  background: linear-gradient(135deg, #1a0510, #5a0f2e);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.fl-08__hero-text {
  font-family: 'Fraunces', serif;
  font-size: 2rem;
  font-weight: 900;
  font-style: italic;
  color: rgba(255,255,255,0.12);
  letter-spacing: -0.04em;
  user-select: none;
}

.fl-08__hero-label {
  position: absolute;
  bottom: 10px;
  left: 10px;
  font-size: 0.62rem;
  color: rgba(255,255,255,0.4);
  font-weight: 600;
}
/* Drop cap + body text */

.fl-08__body-text {
  font-size: 0.82rem;
  color: var(--muted);
  line-height: 1.8;
  columns: 2;
  column-gap: 20px;
}

.fl-08__drop-cap::first-letter {
  font-family: 'Fraunces', serif;
  font-size: 3.2em;
  font-weight: 900;
  color: var(--accent);
  float: left;
  line-height: 0.75;
  margin: 0.08em 0.06em 0 0;
}
/* Right sidebar */

.fl-08__sidebar {
  flex: 1;
  min-width: 0;
  padding: 24px 20px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.fl-08__sidebar-section-title {
  font-size: 0.62rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent2);
  margin-bottom: 10px;
  padding-bottom: 6px;
  border-bottom: 1px solid var(--border);
}

.fl-08__related-item {
  display: flex;
  gap: 10px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border);
  cursor: pointer;
}

.fl-08__related-item:last-child {
  border-bottom: none;
}

.fl-08__related-thumb {
  width: 50px;
  height: 50px;
  border-radius: 6px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.fl-08__related-title {
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--ink);
  line-height: 1.3;
  margin-bottom: 4px;
}

.fl-08__related-meta {
  font-size: 0.65rem;
  color: var(--muted);
}

.fl-08__tag-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.fl-08__tag {
  font-size: 0.68rem;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 4px;
  background: rgba(225,29,72,0.06);
  color: var(--accent);
  cursor: pointer;
  transition: background 0.2s;
}

.fl-08__tag:hover {
  background: rgba(225,29,72,0.15);
}

@media (prefers-reduced-motion: reduce) {
  .fl-08__tag,
    .fl-08__cat-tab {
    transition: none;
  }
}
```
