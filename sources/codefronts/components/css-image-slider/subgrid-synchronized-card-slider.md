---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/subgrid-synchronized-card-slider/"
title: "Subgrid Synchronized Card Slider"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "CSS subgrid synchronized card slider — horizontal carousel where the kicker, title, image, body copy, and button of every card line up perfectly across the…"
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Subgrid Synchronized Card Slider
Source: https://codefronts.com/components/css-image-slider/subgrid-synchronized-card-slider/

CSS subgrid synchronized card slider — horizontal carousel where the kicker, title, image, body copy, and button of every card line up perfectly across the row no matter how long each title runs. Uses grid-template-rows: subgrid to align tracks between siblings, replacing the JavaScript equal-height loop most React and Vue carousel libraries still ship. Pure CSS, zero script.
## HTML
```html
<div class="cis-07">
  <div class="cis-07__rail">
    <article class="cis-07__card">
      <span class="cis-07__ey">Analytics</span>
      <h3 class="cis-07__title">Real-time dashboards</h3>
      <div class="cis-07__media"><img src="https://picsum.photos/seed/cis07a/600/440" alt="Dashboard on a screen"></div>
      <p class="cis-07__body">Live metrics streamed to every seat.</p>
      <button class="cis-07__cta" type="button">Explore</button>
    </article>
    <article class="cis-07__card">
      <span class="cis-07__ey">Automation</span>
      <h3 class="cis-07__title">Workflows that run themselves while you sleep</h3>
      <div class="cis-07__media"><img src="https://picsum.photos/seed/cis07b/600/440" alt="Abstract circuitry"></div>
      <p class="cis-07__body">Chain triggers and actions with a visual builder — no code, no cron jobs, no surprises.</p>
      <button class="cis-07__cta" type="button">Explore</button>
    </article>
    <article class="cis-07__card">
      <span class="cis-07__ey">Security</span>
      <h3 class="cis-07__title">SSO &amp; audit logs</h3>
      <div class="cis-07__media"><img src="https://picsum.photos/seed/cis07c/600/440" alt="Locked vault door"></div>
      <p class="cis-07__body">Enterprise-grade access control.</p>
      <button class="cis-07__cta" type="button">Explore</button>
    </article>
    <article class="cis-07__card">
      <span class="cis-07__ey">Support</span>
      <h3 class="cis-07__title">Humans, 24/7</h3>
      <div class="cis-07__media"><img src="https://picsum.photos/seed/cis07d/600/440" alt="Support headset"></div>
      <p class="cis-07__body">Real people answering within minutes, in the timezone you actually work in.</p>
      <button class="cis-07__cta" type="button">Explore</button>
    </article>
  </div>
</div>
```
## CSS
```css
.cis-07,
.cis-07 *,
.cis-07 *::before,
.cis-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-07 ::selection {
  background: oklch(0.85 0.15 200);
  color: #04141a;
}

.cis-07 {
  --accent: oklch(0.8 0.13 205);
  --card: 290px;
  --surface: #12141c;
  --line: #242836;
  --text: #eef1f7;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--text);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 44px 0;
  background: radial-gradient(120% 110% at 50% 0%,#151824,#0a0b10);
}

.cis-07__rail {
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: var(--card);
  grid-template-rows: auto auto auto 1fr auto;
  gap: 0 20px;
  width: min(920px,96vw);
  margin: 0 auto;
  padding: 6px max(18px,calc(50% - 460px)) 18px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  scrollbar-width: none;
}

.cis-07__rail::-webkit-scrollbar {
  display: none;
}

.cis-07__card {
  display: grid;
  grid-row: 1 / -1;
  grid-template-rows: subgrid;
  scroll-snap-align: center;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 18px;
  overflow: hidden;
  padding: 0;
}

.cis-07__ey {
  padding: 18px 18px 0;
  font: 700 11px ui-monospace,Menlo,monospace;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--accent);
}

.cis-07__title {
  padding: 8px 18px 0;
  font-size: 19px;
  font-weight: 700;
  line-height: 1.15;
  text-wrap: balance;
}

.cis-07__media {
  margin: 14px 0 0;
  aspect-ratio: 15/11;
  overflow: hidden;
}

.cis-07__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.cis-07__body {
  padding: 14px 18px 0;
  font-size: 13.5px;
  line-height: 1.5;
  color: #9aa0b2;
}

.cis-07__cta {
  margin: 16px 18px 18px;
  padding: 10px;
  border: 0;
  border-radius: 10px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 700;
  color: #04141a;
  background: var(--accent);
  transition: filter .2s;
}

.cis-07__cta:hover {
  filter: brightness(1.1);
}

@media (prefers-reduced-motion: reduce) {
  .cis-07__rail {
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
/* No JavaScript — grid-template-rows:subgrid syncs the rows across every card. */
```
