---
source: "codefronts"
url: "https://codefronts.com/layouts/css-card-grid-layout/css-featured-article-magazine-grid/"
title: "CSS Featured Article Magazine Grid"
section: "layouts"
category: "css-card-grid-layout"
category_name: "CSS Card Grid Layouts"
description: "An editorial homepage layout with one hero featured story occupying the full left side and 4 supporting article cards on the right — the exact hierarchy…"
has_js: "false"
---

Here's a working CSS Card Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Featured Article Magazine Grid
Source: https://codefronts.com/layouts/css-card-grid-layout/css-featured-article-magazine-grid/

An editorial homepage layout with one hero featured story occupying the full left side and 4 supporting article cards on the right — the exact hierarchy pattern NYT, Substack, Medium, and The Verge converge on. Real bylines, real categories, real read-times, real publication dates.
## HTML
```html
<div class="cg-14">
  <header class="cg-14__masthead">
    <span class="cg-14__brand">The Quarterly</span>
    <span class="cg-14__date">Issue 38 · Summer 2026</span>
  </header>

  <div class="cg-14__grid">

    <article class="cg-14__hero">
      <div class="cg-14__hero-img"></div>
      <div class="cg-14__hero-body">
        <span class="cg-14__cat cg-14__cat--politics">Politics</span>
        <h2 class="cg-14__hero-title">The Quiet Reformers Behind 2026's Strangest Bipartisan Bill</h2>
        <p class="cg-14__hero-dek">A coalition of 14 senators, six think tanks, and a Reddit forum spent three years drafting the housing reform nobody believed could pass. It just did.</p>
        <footer class="cg-14__hero-meta">
          <div class="cg-14__byline">
            <div class="cg-14__avatar cg-14__avatar--1"></div>
            <span><strong>Maya Chen</strong> · Politics Editor</span>
          </div>
          <span class="cg-14__meta-dot">●</span>
          <span class="cg-14__meta-time">14 min read</span>
          <span class="cg-14__meta-dot">●</span>
          <span class="cg-14__meta-date">June 28, 2026</span>
        </footer>
      </div>
    </article>

    <div class="cg-14__support">

      <article class="cg-14__card">
        <div class="cg-14__thumb cg-14__thumb--1"></div>
        <div class="cg-14__cardbody">
          <span class="cg-14__cat cg-14__cat--tech">Tech</span>
          <h3 class="cg-14__cardtitle">The Engineer Who Resigned Over an AI Memo</h3>
          <span class="cg-14__meta-time">8 min · June 27</span>
        </div>
      </article>

      <article class="cg-14__card">
        <div class="cg-14__thumb cg-14__thumb--2"></div>
        <div class="cg-14__cardbody">
          <span class="cg-14__cat cg-14__cat--culture">Culture</span>
          <h3 class="cg-14__cardtitle">Why the Best Bookstores in 2026 Have Bouncers</h3>
          <span class="cg-14__meta-time">6 min · June 26</span>
        </div>
      </article>

      <article class="cg-14__card">
        <div class="cg-14__thumb cg-14__thumb--3"></div>
        <div class="cg-14__cardbody">
          <span class="cg-14__cat cg-14__cat--climate">Climate</span>
          <h3 class="cg-14__cardtitle">The Farmers Quietly Outsmarting the Drought</h3>
          <span class="cg-14__meta-time">11 min · June 25</span>
        </div>
      </article>

      <article class="cg-14__card">
        <div class="cg-14__thumb cg-14__thumb--4"></div>
        <div class="cg-14__cardbody">
          <span class="cg-14__cat cg-14__cat--biz">Business</span>
          <h3 class="cg-14__cardtitle">Inside the Five-Day Workweek Comeback</h3>
          <span class="cg-14__meta-time">9 min · June 24</span>
        </div>
      </article>

    </div>

  </div>
</div>
```
## CSS
```css
.cg-14,
.cg-14 *,
.cg-14 *::before,
.cg-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cg-14 ::selection {
  background: #0f172a;
  color: #fff;
}

.cg-14 {
  --bg: #fffefb;
  --card: #ffffff;
  --ink: #0f172a;
  --muted: #64748b;
  --line: #e7e3d8;
  --serif: Georgia,"Times New Roman",serif;
  --cat-politics: #0f172a;
  --cat-tech: #0ea5e9;
  --cat-culture: #c026d3;
  --cat-climate: #16a34a;
  --cat-biz: #dc2626;
  min-height: 100vh;
  background: var(--bg);
  padding: clamp(24px,3vw,40px) clamp(20px,3vw,40px);
  font-family: -apple-system,BlinkMacSystemFont,"Inter","Segoe UI",sans-serif;
  color: var(--ink);
}

.cg-14__masthead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 0 18px;
  border-bottom: 2px solid var(--ink);
  margin-bottom: clamp(24px,3vw,40px);
  max-width: 1240px;
  margin-left: auto;
  margin-right: auto;
  flex-wrap: wrap;
  gap: 12px;
}

.cg-14__brand {
  font-family: var(--serif);
  font-weight: 900;
  font-style: italic;
  font-size: clamp(1.5rem,2.4vw,2rem);
  letter-spacing: -.01em;
}

.cg-14__date {
  font-size: .78rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--muted);
}

.cg-14__grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr;
  gap: clamp(20px,2.6vw,36px);
  max-width: 1240px;
  margin: 0 auto;
}
/* Hero article */

.cg-14__hero {
  display: flex;
  flex-direction: column;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 14px;
  overflow: hidden;
  transition: transform .25s,box-shadow .25s;
}

.cg-14__hero:hover {
  transform: translateY(-3px);
  box-shadow: 0 18px 36px -18px rgba(15,23,42,.18);
}

.cg-14__hero-img {
  height: clamp(220px,28vw,360px);
  background: linear-gradient(180deg,rgba(15,23,42,0) 60%,rgba(15,23,42,.4)), linear-gradient(135deg,#dc2626 0%,#7c1d1d 60%,#1a0a0a 100%);
}

.cg-14__hero-body {
  padding: clamp(22px,2.4vw,32px);
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.cg-14__cat {
  align-self: flex-start;
  font-size: .66rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: #fff;
  padding: 4px 10px;
  border-radius: 3px;
}

.cg-14__cat--politics {
  background: var(--cat-politics);
}

.cg-14__cat--tech {
  background: var(--cat-tech);
}

.cg-14__cat--culture {
  background: var(--cat-culture);
}

.cg-14__cat--climate {
  background: var(--cat-climate);
}

.cg-14__cat--biz {
  background: var(--cat-biz);
}

.cg-14__hero-title {
  font-family: var(--serif);
  font-size: clamp(1.6rem,2.8vw,2.4rem);
  font-weight: 900;
  line-height: 1.1;
  letter-spacing: -.02em;
}

.cg-14__hero-dek {
  font-size: clamp(.95rem,1.15vw,1.06rem);
  color: var(--muted);
  line-height: 1.5;
}

.cg-14__hero-meta {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
  font-size: .82rem;
  color: var(--muted);
  padding-top: 14px;
  border-top: 1px solid var(--line);
  margin-top: 4px;
}

.cg-14__byline {
  display: flex;
  align-items: center;
  gap: 10px;
}

.cg-14__avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
}

.cg-14__avatar--1 {
  background: linear-gradient(135deg,#f9c1cf,#d97a99);
}

.cg-14__byline strong {
  color: var(--ink);
  font-weight: 700;
}

.cg-14__meta-dot {
  opacity: .4;
  font-size: .5rem;
}

.cg-14__meta-time,
.cg-14__meta-date {
  font-weight: 600;
}
/* Supporting articles — nested 2x2 grid */

.cg-14__support {
  display: grid;
  grid-template-rows: repeat(4,1fr);
  gap: clamp(12px,1.4vw,16px);
}

.cg-14__card {
  display: flex;
  gap: 14px;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 14px;
  transition: transform .25s,box-shadow .25s;
  cursor: pointer;
}

.cg-14__card:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 22px -14px rgba(15,23,42,.18);
}

.cg-14__thumb {
  width: 96px;
  height: 96px;
  border-radius: 8px;
  flex-shrink: 0;
}

.cg-14__thumb--1 {
  background: linear-gradient(135deg,#0ea5e9,#0c4a6e);
}

.cg-14__thumb--2 {
  background: linear-gradient(135deg,#c026d3,#581c87);
}

.cg-14__thumb--3 {
  background: linear-gradient(135deg,#16a34a,#14532d);
}

.cg-14__thumb--4 {
  background: linear-gradient(135deg,#dc2626,#7c1d1d);
}

.cg-14__cardbody {
  display: flex;
  flex-direction: column;
  gap: 6px;
  min-width: 0;
  flex: 1;
  justify-content: space-between;
}

.cg-14__cardtitle {
  font-family: var(--serif);
  font-size: clamp(.95rem,1.2vw,1.1rem);
  font-weight: 800;
  line-height: 1.22;
  letter-spacing: -.005em;
  color: var(--ink);
}

.cg-14__cardbody .cg-14__meta-time {
  font-size: .74rem;
  color: var(--muted);
  font-weight: 600;
}

@media (max-width: 900px) {
  .cg-14__grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 520px) {
  .cg-14__card {
    flex-direction: column;
  }

  .cg-14__thumb {
    width: 100%;
    height: 140px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cg-14__hero,
    .cg-14__card {
    transition: none;
  }
}
```
