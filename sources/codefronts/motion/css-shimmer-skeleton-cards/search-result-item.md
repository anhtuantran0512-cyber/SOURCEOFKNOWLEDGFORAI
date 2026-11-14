---
source: "codefronts"
url: "https://codefronts.com/motion/css-shimmer-skeleton-cards/search-result-item/"
title: "Search Result Item"
section: "motion"
category: "css-shimmer-skeleton-cards"
category_name: "CSS Shimmer Skeleton Cards"
description: "A SERP-anatomy skeleton with modern polish: a favicon dot + breadcrumb line, a large link-blue-tinted title bar, then a two-line snippet — with deliberately…"
has_js: "false"
---

Here's a working CSS Shimmer Skeleton Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Search Result Item
Source: https://codefronts.com/motion/css-shimmer-skeleton-cards/search-result-item/

A SERP-anatomy skeleton with modern polish: a favicon dot + breadcrumb line, a large link-blue-tinted title bar, then a two-line snippet — with deliberately larger spacing between title block and snippet than between snippet lines. Ideal for site search, docs search and any query-driven list users scan vertically.
## HTML
```html
<section class="ssc-07" aria-label="Search result skeleton demo">
  <div class="ssc-07__list" role="status" aria-busy="true">
    <span class="ssc-sr">Loading search results…</span>
    <div class="ssc-07__result" aria-hidden="true">
      <div class="ssc-07__crumb"><div class="ssc-sk ssc-07__favicon"></div><div class="ssc-sk ssc-07__url" style="width:34%"></div></div>
      <div class="ssc-sk ssc-07__title" style="width:62%"></div>
      <div class="ssc-07__snippet">
        <div class="ssc-sk ssc-07__line" style="width:100%"></div>
        <div class="ssc-sk ssc-07__line" style="width:78%"></div>
      </div>
    </div>
    <div class="ssc-07__result" aria-hidden="true">
      <div class="ssc-07__crumb"><div class="ssc-sk ssc-07__favicon"></div><div class="ssc-sk ssc-07__url" style="width:28%"></div></div>
      <div class="ssc-sk ssc-07__title" style="width:74%"></div>
      <div class="ssc-07__snippet">
        <div class="ssc-sk ssc-07__line" style="width:96%"></div>
        <div class="ssc-sk ssc-07__line" style="width:60%"></div>
      </div>
    </div>
    <div class="ssc-07__result" aria-hidden="true">
      <div class="ssc-07__crumb"><div class="ssc-sk ssc-07__favicon"></div><div class="ssc-sk ssc-07__url" style="width:38%"></div></div>
      <div class="ssc-sk ssc-07__title" style="width:56%"></div>
      <div class="ssc-07__snippet">
        <div class="ssc-sk ssc-07__line" style="width:100%"></div>
        <div class="ssc-sk ssc-07__line" style="width:84%"></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.ssc-07,
.ssc-07 *,
.ssc-07 *::before,
.ssc-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ssc-07 {
  --link: oklch(0.55 0.18 262);
  --sk-bg: oklch(0.91 0.008 260);
  --sk-shine: rgba(255,255,255,.8);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.985 0.004 260),oklch(0.95 0.01 260));
}

.ssc-07 .ssc-sk {
  position: relative;
  overflow: hidden;
  background: var(--sk-bg);
  border-radius: 5px;
}

.ssc-07 .ssc-sk::after {
  content: "";
  position: absolute;
  inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(105deg,transparent 30%,var(--sk-shine) 50%,transparent 70%);
  animation: ssc-07-shimmer 1.8s ease-in-out infinite;
}

@keyframes ssc-07-shimmer {
  100% {
    transform: translateX(100%);
  }
}

.ssc-07 .ssc-sr {
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

.ssc-07 .ssc-07__list {
  position: relative;
  width: min(520px,100%);
  display: flex;
  flex-direction: column;
  gap: 28px;
}

.ssc-07 .ssc-07__result {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.ssc-07 .ssc-07__result:nth-child(3) .ssc-sk::after {
  animation-delay: .12s;
}

.ssc-07 .ssc-07__result:nth-child(4) .ssc-sk::after {
  animation-delay: .24s;
}

.ssc-07 .ssc-07__crumb {
  display: flex;
  align-items: center;
  gap: 8px;
}

.ssc-07 .ssc-07__favicon {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
  border-radius: 50%;
}

.ssc-07 .ssc-07__url {
  height: 9px;
  border-radius: 999px;
}

.ssc-07 .ssc-07__title {
  height: 20px;
  border-radius: 6px;
  background: color-mix(in oklab,var(--link) 18%,var(--sk-bg));
}

.ssc-07 .ssc-07__snippet {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-top: 6px;
}

.ssc-07 .ssc-07__line {
  height: 10px;
}

@media (prefers-reduced-motion: reduce) {
  .ssc-07 .ssc-sk::after {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — asymmetric spacing + a color-mix link-blue title bar reproduce SERP information scent. */
```
