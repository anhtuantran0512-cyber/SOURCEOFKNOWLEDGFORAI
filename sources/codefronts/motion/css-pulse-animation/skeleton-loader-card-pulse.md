---
source: "codefronts"
url: "https://codefronts.com/motion/css-pulse-animation/skeleton-loader-card-pulse/"
title: "Skeleton Loader Card Pulse"
section: "motion"
category: "css-pulse-animation"
category_name: "CSS Pulse Animations"
description: "Content-loading skeleton screens — the LinkedIn / Facebook / YouTube pattern for graceful data fetching."
has_js: "false"
---

Here's a working CSS Pulse Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skeleton Loader Card Pulse
Source: https://codefronts.com/motion/css-pulse-animation/skeleton-loader-card-pulse/

Content-loading skeleton screens — the LinkedIn / Facebook / YouTube pattern for graceful data fetching. 3 stacked feed cards each with an avatar circle, author line, three text blocks, and a media thumbnail — all animated with a diagonal shimmer sweep that reads as "content is on its way." Neutral gray canvas (#f8fafc) with light gray placeholders (#e2e8f0) and a bright shimmer highlight (#f8fafc) sweeping diagonally.
## HTML
```html
<div class="pl-11">
  <header class="pl-11__head">
    <div class="pl-11__brand">
      <span class="pl-11__brand-logo" aria-hidden="true">◇</span>
      <span>Northlight</span>
    </div>
    <div class="pl-11__nav-links">
      <span class="pl-11__nav-item pl-11__nav-item--sel">Feed</span>
      <span class="pl-11__nav-item">Projects</span>
      <span class="pl-11__nav-item">Notifications</span>
    </div>
  </header>
  <section class="pl-11__feed" role="status" aria-live="polite" aria-label="Loading 3 feed items">
    <article class="pl-11__card">
      <header class="pl-11__card-head">
        <div class="pl-11__sk pl-11__sk--avatar"></div>
        <div class="pl-11__card-meta">
          <div class="pl-11__sk pl-11__sk--name"></div>
          <div class="pl-11__sk pl-11__sk--stamp"></div>
        </div>
      </header>
      <div class="pl-11__sk pl-11__sk--text pl-11__sk--wide"></div>
      <div class="pl-11__sk pl-11__sk--text pl-11__sk--mid"></div>
      <div class="pl-11__sk pl-11__sk--text pl-11__sk--short"></div>
      <div class="pl-11__sk pl-11__sk--thumb"></div>
    </article>
    <article class="pl-11__card">
      <header class="pl-11__card-head">
        <div class="pl-11__sk pl-11__sk--avatar"></div>
        <div class="pl-11__card-meta">
          <div class="pl-11__sk pl-11__sk--name"></div>
          <div class="pl-11__sk pl-11__sk--stamp"></div>
        </div>
      </header>
      <div class="pl-11__sk pl-11__sk--text pl-11__sk--wide"></div>
      <div class="pl-11__sk pl-11__sk--text pl-11__sk--mid"></div>
    </article>
    <article class="pl-11__card">
      <header class="pl-11__card-head">
        <div class="pl-11__sk pl-11__sk--avatar"></div>
        <div class="pl-11__card-meta">
          <div class="pl-11__sk pl-11__sk--name"></div>
          <div class="pl-11__sk pl-11__sk--stamp"></div>
        </div>
      </header>
      <div class="pl-11__sk pl-11__sk--text pl-11__sk--wide"></div>
      <div class="pl-11__sk pl-11__sk--text pl-11__sk--short"></div>
      <div class="pl-11__sk pl-11__sk--thumb"></div>
    </article>
  </section>
</div>
```
## CSS
```css
.pl-11 {
  --page-bg: #f8fafc;
  --card: #ffffff;
  --ink: #0f172a;
  --sub: #64748b;
  --placeholder: #e2e8f0;
  --shimmer: #f1f5f9;
  --shimmer-highlight: #ffffff;
  --line: #e2e8f0;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: grid;
  grid-template-rows: auto 1fr;
  gap: 16px;
  padding: 24px;
  background: var(--page-bg);
  color: var(--ink);
}

.pl-11 *,
.pl-11 *::before,
.pl-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pl-11 ::selection {
  background: #0ea5e9;
  color: #fff;
}

.pl-11__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 20px;
  border-radius: 11px;
  background: var(--card);
  border: 1px solid var(--line);
  box-shadow: 0 1px 3px rgba(15,23,42,.05);
}

.pl-11__brand {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 700;
  font-size: .9rem;
  letter-spacing: -.01em;
}

.pl-11__brand-logo {
  color: #0ea5e9;
  font-size: 1.1rem;
}

.pl-11__nav-links {
  display: flex;
  gap: 4px;
}

.pl-11__nav-item {
  padding: 5px 12px;
  border-radius: 6px;
  font-size: .78rem;
  font-weight: 600;
  color: var(--sub);
  cursor: pointer;
  transition: background .15s ease,color .15s ease;
}

.pl-11__nav-item:hover {
  background: #f1f5f9;
  color: var(--ink);
}

.pl-11__nav-item--sel {
  background: #f1f5f9;
  color: var(--ink);
}

.pl-11__feed {
  display: flex;
  flex-direction: column;
  gap: 12px;
  width: min(560px,100%);
  justify-self: center;
}

.pl-11__card {
  padding: 16px;
  border-radius: 11px;
  background: var(--card);
  border: 1px solid var(--line);
  box-shadow: 0 1px 3px rgba(15,23,42,.05);
}

.pl-11__card-head {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

.pl-11__card-meta {
  display: flex;
  flex-direction: column;
  gap: 6px;
  flex: 1;
}
/* Skeleton primitive — gradient shimmer sweep */

.pl-11__sk {
  border-radius: 5px;
  background: linear-gradient(100deg,var(--placeholder) 20%,var(--shimmer-highlight) 50%,var(--placeholder) 80%);
  background-size: 200% 100%;
  background-position: -100% 0;
  animation: pl-11-shimmer 1.6s linear infinite;
}

@keyframes pl-11-shimmer {
  0% {
    background-position: -100% 0;
  }

  100% {
    background-position: 200% 0;
  }
}

.pl-11__sk--avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  flex-shrink: 0;
}

.pl-11__sk--name {
  height: 12px;
  width: 35%;
  border-radius: 3px;
}

.pl-11__sk--stamp {
  height: 10px;
  width: 22%;
  border-radius: 3px;
}

.pl-11__sk--text {
  height: 11px;
  border-radius: 3px;
  margin-bottom: 8px;
}

.pl-11__sk--wide {
  width: 100%;
}

.pl-11__sk--mid {
  width: 80%;
}

.pl-11__sk--short {
  width: 55%;
}

.pl-11__sk--thumb {
  width: 100%;
  height: 140px;
  border-radius: 8px;
  margin-top: 6px;
}

@media (prefers-reduced-motion: reduce) {
  .pl-11__sk {
    animation: none!important;
    background: var(--placeholder)!important;
  }
}
```
