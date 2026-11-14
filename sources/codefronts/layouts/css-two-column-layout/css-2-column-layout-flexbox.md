---
source: "codefronts"
url: "https://codefronts.com/layouts/css-two-column-layout/css-2-column-layout-flexbox/"
title: "CSS 2 Column Layout Flexbox"
section: "layouts"
category: "css-two-column-layout"
category_name: "CSS Two-Column Layouts"
description: "The modern default: a flexbox two column layout with a fluid 68% content area and a 32% sidebar built with flex-basis percentages and gap — no floats, no…"
has_js: "false"
---

Here's a working CSS Two-Column Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS 2 Column Layout Flexbox
Source: https://codefronts.com/layouts/css-two-column-layout/css-2-column-layout-flexbox/

The modern default: a flexbox two column layout with a fluid 68% content area and a 32% sidebar built with flex-basis percentages and gap — no floats, no clearfix, no JavaScript. Both columns are automatically equal height, making this the copy-paste answer for dashboards, docs pages and content + sidebar layouts.
## HTML
```html
<section class="tcl-01" aria-label="Flexbox two column layout demo">
  <div class="tcl-01__shell">
    <main class="tcl-01__main">
      <span class="tcl-01__eyebrow">flex: 0 0 68%</span>
      <h2 class="tcl-01__title">Traffic overview</h2>
      <p class="tcl-01__lede">The primary column holds your main content and flexes from a 68% basis. The sidebar takes the remaining 32% — resize the page and watch both columns share one gap token.</p>
      <div class="tcl-01__metrics">
        <div class="tcl-01__metric"><strong>84,210</strong><span>Sessions</span><em class="tcl-01__up">+12.4%</em></div>
        <div class="tcl-01__metric"><strong>3m 42s</strong><span>Avg. visit</span><em class="tcl-01__up">+0.8%</em></div>
        <div class="tcl-01__metric"><strong>2.9%</strong><span>Bounce delta</span><em class="tcl-01__down">−1.1%</em></div>
      </div>
      <div class="tcl-01__chart" role="img" aria-label="Bar chart of weekly sessions">
        <i style="--v:42%"></i><i style="--v:58%"></i><i style="--v:49%"></i><i style="--v:74%"></i><i style="--v:66%"></i><i style="--v:88%"></i><i style="--v:97%"></i>
      </div>
    </main>
    <aside class="tcl-01__aside" aria-label="Recent activity">
      <span class="tcl-01__eyebrow">flex: 1 1 32%</span>
      <h3 class="tcl-01__subtitle">Activity</h3>
      <ul class="tcl-01__feed">
        <li><b>Deploy shipped</b><span>v2.14 to production · 8m ago</span></li>
        <li><b>New top referrer</b><span>news.ycombinator.com · 1h ago</span></li>
        <li><b>Goal reached</b><span>10k newsletter signups · 3h ago</span></li>
      </ul>
      <a class="tcl-01__link" href="#report">View full report →</a>
    </aside>
  </div>
</section>
```
## CSS
```css
.tcl-01,
.tcl-01 *,
.tcl-01 *::before,
.tcl-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tcl-01 {
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.55 0.19 275);
  --ink: oklch(0.25 0.03 275);
  --gap: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  background: oklch(0.97 0.01 275);
  padding: clamp(24px,4vw,48px);
}

.tcl-01__shell {
  display: flex;
  gap: var(--gap);
  max-width: 1040px;
  margin-inline: auto;
}

.tcl-01__main {
  flex: 0 0 68%;
  min-width: 0;
  background: #fff;
  border: 1px solid oklch(0.9 0.02 275);
  border-radius: 16px;
  padding: clamp(20px,3vw,32px);
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.tcl-01__aside {
  flex: 1 1 32%;
  min-width: 0;
  background: color-mix(in oklab,var(--accent) 6%,#fff);
  border: 1px solid color-mix(in oklab,var(--accent) 18%,transparent);
  border-radius: 16px;
  padding: clamp(20px,3vw,28px);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.tcl-01__eyebrow {
  align-self: flex-start;
  font: 600 11px/1 ui-monospace,monospace;
  letter-spacing: .08em;
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 10%,transparent);
  border-radius: 99px;
  padding: 6px 10px;
}

.tcl-01__title {
  font-size: clamp(22px,3vw,30px);
  letter-spacing: -.02em;
  text-wrap: pretty;
}

.tcl-01__subtitle {
  font-size: 17px;
  letter-spacing: -.01em;
}

.tcl-01__lede {
  font-size: 14.5px;
  line-height: 1.6;
  color: color-mix(in oklab,var(--ink) 70%,transparent);
  text-wrap: pretty;
}

.tcl-01__metrics {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.tcl-01__metric {
  flex: 1 1 120px;
  display: grid;
  gap: 2px;
  background: oklch(0.975 0.005 275);
  border: 1px solid oklch(0.92 0.01 275);
  border-radius: 12px;
  padding: 14px;
}

.tcl-01__metric strong {
  font-size: 20px;
  letter-spacing: -.02em;
}

.tcl-01__metric span {
  font-size: 12px;
  color: color-mix(in oklab,var(--ink) 55%,transparent);
}

.tcl-01__up {
  font: 600 11.5px/1 inherit;
  font-style: normal;
  color: oklch(0.55 0.15 150);
}

.tcl-01__down {
  font: 600 11.5px/1 inherit;
  font-style: normal;
  color: oklch(0.55 0.19 25);
}

.tcl-01__chart {
  display: flex;
  align-items: flex-end;
  gap: 10px;
  height: 120px;
  padding: 12px;
  background: oklch(0.975 0.005 275);
  border: 1px solid oklch(0.92 0.01 275);
  border-radius: 12px;
}

.tcl-01__chart i {
  flex: 1;
  height: var(--v);
  background: linear-gradient(180deg,color-mix(in oklab,var(--accent) 80%,white),var(--accent));
  border-radius: 6px 6px 2px 2px;
  animation: tcl-01-rise .7s cubic-bezier(.2,.9,.2,1) backwards;
}

.tcl-01__chart i:nth-child(2) {
  animation-delay: .05s;
}

.tcl-01__chart i:nth-child(3) {
  animation-delay: .1s;
}

.tcl-01__chart i:nth-child(4) {
  animation-delay: .15s;
}

.tcl-01__chart i:nth-child(5) {
  animation-delay: .2s;
}

.tcl-01__chart i:nth-child(6) {
  animation-delay: .25s;
}

.tcl-01__chart i:nth-child(7) {
  animation-delay: .3s;
}

.tcl-01__feed {
  list-style: none;
  display: grid;
  gap: 12px;
}

.tcl-01__feed li {
  display: grid;
  gap: 2px;
  padding-left: 14px;
  border-left: 2px solid color-mix(in oklab,var(--accent) 45%,transparent);
}

.tcl-01__feed b {
  font-size: 13.5px;
}

.tcl-01__feed span {
  font-size: 12px;
  color: color-mix(in oklab,var(--ink) 55%,transparent);
}

.tcl-01__link {
  margin-top: auto;
  font: 600 13.5px/1 inherit;
  color: var(--accent);
  text-decoration: none;
}

.tcl-01__link:hover {
  text-decoration: underline;
}

.tcl-01__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
  border-radius: 4px;
}

@keyframes tcl-01-rise {
  from {
    transform: scaleY(0);
    transform-origin: bottom;
  }
}

@media (max-width: 720px) {
  .tcl-01__shell {
    flex-direction: column;
  }

  .tcl-01__main,
    .tcl-01__aside {
    flex: 1 1 auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tcl-01__chart i {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — display:flex + gap does the layout; flex-basis 68%/32% sets the split and one media query stacks it on mobile. */
```
