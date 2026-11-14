---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-cursor-typewriter-blink-animation/"
title: "CSS Marquee Horizontal Text Scroll Continuous"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "The infinite ticker rebuilt correctly: a duplicated track translated -50% for a mathematically seamless loop, with masked fade edges and hover-pause — as a…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Marquee Horizontal Text Scroll Continuous
Source: https://codefronts.com/motion/css-text-animations/css-cursor-typewriter-blink-animation/

The infinite ticker rebuilt correctly: a duplicated track translated -50% for a mathematically seamless loop, with masked fade edges and hover-pause — as a SaaS metrics strip and as a two-row fashion band counter-scrolling outlined against filled type.
## HTML
```html
<div class="cat-20-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-20a" aria-label="Continuous metrics ticker">
  <div class="cat-20a__card">
    <p class="cat-20a__label">Live platform stats — hover to pause</p>
    <div class="cat-20a__viewport">
      <div class="cat-20a__track">
        <ul class="cat-20a__list">
          <li>99.99% uptime</li><li aria-hidden="true">✦</li><li>4ms median latency</li><li aria-hidden="true">✦</li><li>12,400 teams shipped today</li><li aria-hidden="true">✦</li><li>SOC 2 Type II</li><li aria-hidden="true">✦</li><li>190+ regions</li><li aria-hidden="true">✦</li>
        </ul>
        <ul class="cat-20a__list" aria-hidden="true">
          <li>99.99% uptime</li><li>✦</li><li>4ms median latency</li><li>✦</li><li>12,400 teams shipped today</li><li>✦</li><li>SOC 2 Type II</li><li>✦</li><li>190+ regions</li><li>✦</li>
        </ul>
      </div>
    </div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">
<section class="cat-20b" aria-label="Two row counter scrolling text band">
  <div class="cat-20b__band" role="img" aria-label="Spring drop 2027 — new season banner">
    <div class="cat-20b__row cat-20b__row--solid" aria-hidden="true"><span>SPRING DROP 2027&nbsp;—&nbsp;NEW SEASON&nbsp;—&nbsp;SPRING DROP 2027&nbsp;—&nbsp;NEW SEASON&nbsp;—&nbsp;</span><span>SPRING DROP 2027&nbsp;—&nbsp;NEW SEASON&nbsp;—&nbsp;SPRING DROP 2027&nbsp;—&nbsp;NEW SEASON&nbsp;—&nbsp;</span></div>
    <div class="cat-20b__row cat-20b__row--ghost" aria-hidden="true"><span>WORLDWIDE SHIPPING&nbsp;—&nbsp;MEMBERS FIRST&nbsp;—&nbsp;WORLDWIDE SHIPPING&nbsp;—&nbsp;MEMBERS FIRST&nbsp;—&nbsp;</span><span>WORLDWIDE SHIPPING&nbsp;—&nbsp;MEMBERS FIRST&nbsp;—&nbsp;WORLDWIDE SHIPPING&nbsp;—&nbsp;MEMBERS FIRST&nbsp;—&nbsp;</span></div>
  </div>
</section>
</div>
```
## CSS
```css
.cat-20-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-20-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-20a,
.cat-20a *,
.cat-20a *::before,
.cat-20a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-20a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#141926,#0a0d15 70%);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-20a__card {
  width: min(760px,100%);
  display: grid;
  gap: 18px;
}

.cat-20a__label {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: rgba(170,190,225,.45);
  text-align: center;
}

.cat-20a__viewport {
  overflow: hidden;
  border-block: 1px solid rgba(255,255,255,.1);
  padding: 20px 0;
  -webkit-mask-image: linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);
  mask-image: linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);
}

.cat-20a__track {
  display: flex;
  width: max-content;
  animation: cat-20a-scroll 22s linear infinite;
}

.cat-20a__viewport:hover .cat-20a__track {
  animation-play-state: paused;
}

.cat-20a__list {
  display: flex;
  align-items: center;
  gap: 34px;
  padding-right: 34px;
  list-style: none;
  font-size: 19px;
  font-weight: 500;
  color: #dde6f5;
  white-space: nowrap;
}

.cat-20a__list li:nth-child(even) {
  color: oklch(0.84 0.16 165);
  font-size: 12px;
}

@keyframes cat-20a-scroll {
  to {
    transform: translateX(-50%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-20a__track {
    animation: none;
  }

  .cat-20a__viewport {
    overflow-x: auto;
  }
}

.cat-20b,
.cat-20b *,
.cat-20b *::before,
.cat-20b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-20b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 0;
  background: #141210;
  overflow: hidden;
}

.cat-20b__band {
  display: grid;
  gap: 6px;
  transform: rotate(-2deg) scale(1.04);
  font-family: 'Anton',Impact,'Segoe UI',sans-serif;
}

.cat-20b__row {
  display: flex;
  white-space: nowrap;
  width: max-content;
  font-size: clamp(44px,7.5vw,92px);
  letter-spacing: .02em;
  line-height: 1.05;
}

.cat-20b__row--solid {
  color: oklch(0.9 0.18 95);
  animation: cat-20b-l 26s linear infinite;
}

.cat-20b__row--ghost {
  color: transparent;
  -webkit-text-stroke: 1.5px rgba(240,235,220,.5);
  animation: cat-20b-l 26s linear infinite reverse;
}

@keyframes cat-20b-l {
  to {
    transform: translateX(-50%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-20b__row {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the list renders twice inside a max-content track; translateX(-50%) makes the last frame identical to the first, so the loop is seamless. */

/* No JavaScript — two duplicated rows share one keyframe; the outlined row runs it with animation-direction:reverse for the counter-scroll. */
```
