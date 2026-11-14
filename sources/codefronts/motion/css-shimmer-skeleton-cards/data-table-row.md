---
source: "codefronts"
url: "https://codefronts.com/motion/css-shimmer-skeleton-cards/data-table-row/"
title: "Data Table Row"
section: "motion"
category: "css-shimmer-skeleton-cards"
category_name: "CSS Shimmer Skeleton Cards"
description: "A terminal-dark table skeleton for admin dashboards: a header row of brighter pills above five zebra-striped rows of cyan-tinted cells, all sitting on a…"
has_js: "false"
---

Here's a working CSS Shimmer Skeleton Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Data Table Row
Source: https://codefronts.com/motion/css-shimmer-skeleton-cards/data-table-row/

A terminal-dark table skeleton for admin dashboards: a header row of brighter pills above five zebra-striped rows of cyan-tinted cells, all sitting on a glass panel over a faint blueprint grid. The monospace-console aesthetic tells ops users "data is coming" without a single default gray.
## HTML
```html
<section class="ssc-03" aria-label="Data table row skeleton demo">
  <div class="ssc-03__table" role="status" aria-busy="true">
    <span class="ssc-sr">Loading table data…</span>
    <div aria-hidden="true">
      <div class="ssc-03__row ssc-03__row--head">
        <div class="ssc-sk ssc-03__pill" style="width:55%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:70%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:70%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:70%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:80%"></div>
      </div>
      <div class="ssc-03__row">
        <div class="ssc-sk ssc-03__pill" style="width:80%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:55%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:65%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:45%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:90%"></div>
      </div>
      <div class="ssc-03__row">
        <div class="ssc-sk ssc-03__pill" style="width:65%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:70%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:50%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:60%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:90%"></div>
      </div>
      <div class="ssc-03__row">
        <div class="ssc-sk ssc-03__pill" style="width:88%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:45%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:70%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:55%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:90%"></div>
      </div>
      <div class="ssc-03__row">
        <div class="ssc-sk ssc-03__pill" style="width:72%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:60%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:58%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:48%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:90%"></div>
      </div>
      <div class="ssc-03__row">
        <div class="ssc-sk ssc-03__pill" style="width:60%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:52%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:66%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:58%"></div>
        <div class="ssc-sk ssc-03__pill" style="width:90%"></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.ssc-03,
.ssc-03 *,
.ssc-03 *::before,
.ssc-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ssc-03 {
  --cell: oklch(0.75 0.1 220);
  --sk-bg: oklch(0.75 0.1 220 / .1);
  --sk-shine: oklch(0.85 0.08 220 / .18);
  font-family: ui-monospace,'Cascadia Code',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: repeating-linear-gradient(0deg,transparent 0 31px,oklch(0.75 0.1 220 / .05) 31px 32px),repeating-linear-gradient(90deg,transparent 0 31px,oklch(0.75 0.1 220 / .05) 31px 32px),oklch(0.17 0.02 240);
}

.ssc-03 .ssc-sk {
  position: relative;
  overflow: hidden;
  background: var(--sk-bg);
  border-radius: 999px;
}

.ssc-03 .ssc-sk::after {
  content: "";
  position: absolute;
  inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(105deg,transparent 30%,var(--sk-shine) 50%,transparent 70%);
  animation: ssc-03-shimmer 1.8s ease-in-out infinite;
}

@keyframes ssc-03-shimmer {
  100% {
    transform: translateX(100%);
  }
}

.ssc-03 .ssc-sr {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}

.ssc-03 .ssc-03__table {
  position: relative;
  width: min(640px,100%);
  background: rgba(255,255,255,.03);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid oklch(0.75 0.1 220 / .18);
  border-radius: 16px;
  padding: 8px 20px;
  box-shadow: 0 24px 50px -28px rgba(0,0,0,.8);
}

.ssc-03 .ssc-03__row {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr .8fr;
  gap: 18px;
  align-items: center;
  padding: 15px 0;
  border-bottom: 1px solid oklch(0.75 0.1 220 / .08);
}

.ssc-03 .ssc-03__row:last-child {
  border-bottom: none;
}

.ssc-03 .ssc-03__row:nth-child(even):not(.ssc-03__row--head) {
  opacity: .55;
}

.ssc-03 .ssc-03__row--head .ssc-03__pill {
  height: 9px;
  background: oklch(0.75 0.1 220 / .22);
}

.ssc-03 .ssc-03__pill {
  height: 12px;
}

@media (max-width: 520px) {
  .ssc-03__row {
    grid-template-columns: 2fr 1fr 1fr;
  }

  .ssc-03__row .ssc-03__pill:nth-child(n+4) {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ssc-03 .ssc-sk::after {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — rows share the live table's grid tracks; :nth-child(even) opacity fakes zebra striping for free. */
```
