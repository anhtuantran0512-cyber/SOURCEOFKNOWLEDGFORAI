---
source: "codefronts"
url: "https://codefronts.com/motion/css-infinite-marquee/vertical-marquee-agency-services/"
title: "Vertical Infinite Marquee — Agency Services Column"
section: "motion"
category: "css-infinite-marquee"
category_name: "CSS Infinite Marquee Designs"
description: "The agency-hero staple: a vertical column of services scrolling upward beside bold static copy, with a top-and-bottom mask fade and one 'live' highlighted…"
has_js: "false"
---

Here's a working CSS Infinite Marquee Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Infinite Marquee — Agency Services Column
Source: https://codefronts.com/motion/css-infinite-marquee/vertical-marquee-agency-services/

The agency-hero staple: a vertical column of services scrolling upward beside bold static copy, with a top-and-bottom mask fade and one 'live' highlighted row at center height — the same duplicated-group math as horizontal marquees, rotated 90 degrees with flex-direction:column and translateY.
## HTML
```html
<section class="mqs-10" aria-label="Vertical marquee demo">
  <div class="mqs-10__inner">
    <div class="mqs-10__copy">
      <p class="mqs-10__eyebrow">Full-service studio</p>
      <h3 class="mqs-10__hero">We do the whole thing.</h3>
      <p class="mqs-10__sub">Strategy through ship. One team, no handoffs.</p>
    </div>
    <div class="mqs-10__col">
      <div class="mqs-10__band" aria-hidden="true"></div>
      <div class="mqs-10__viewport">
        <div class="mqs-10__group">
          <span class="mqs-10__row">Brand identity</span>
          <span class="mqs-10__row">Web design</span>
          <span class="mqs-10__row">Product strategy</span>
          <span class="mqs-10__row">Motion &amp; 3D</span>
          <span class="mqs-10__row">Design systems</span>
          <span class="mqs-10__row">Development</span>
        </div>
        <div class="mqs-10__group" aria-hidden="true">
          <span class="mqs-10__row">Brand identity</span>
          <span class="mqs-10__row">Web design</span>
          <span class="mqs-10__row">Product strategy</span>
          <span class="mqs-10__row">Motion &amp; 3D</span>
          <span class="mqs-10__row">Design systems</span>
          <span class="mqs-10__row">Development</span>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.mqs-10,
.mqs-10 *,
.mqs-10 *::before,
.mqs-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.mqs-10 {
  min-height: 100vh;
  width: 100%;
  --gap: 0px;
  --speed: 16s;
  --accent: #4f46e5;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f4f4f8;
  padding: 64px 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.mqs-10__inner {
  width: min(880px,100%);
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: center;
  gap: 40px;
}

.mqs-10__eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 12px;
}

.mqs-10__hero {
  font-size: clamp(28px,4.5vw,42px);
  font-weight: 800;
  color: #18181b;
  letter-spacing: -.03em;
  line-height: 1.05;
  text-wrap: balance;
}

.mqs-10__sub {
  font-size: 14.5px;
  color: #71717a;
  margin-top: 12px;
  max-width: 36ch;
  text-wrap: pretty;
}

.mqs-10__col {
  position: relative;
  width: min(300px,42vw);
}

.mqs-10__band {
  position: absolute;
  left: -10px;
  right: -10px;
  top: 50%;
  height: 64px;
  translate: 0 -50%;
  border-block: 2px solid var(--accent);
  background: rgb(79 70 229 / .06);
  border-radius: 4px;
  z-index: 1;
  pointer-events: none;
}

.mqs-10__viewport {
  display: flex;
  flex-direction: column;
  gap: var(--gap);
  height: 340px;
  overflow: hidden;
  mask-image: linear-gradient(180deg,transparent,#000 18%,#000 82%,transparent);
  -webkit-mask-image: linear-gradient(180deg,transparent,#000 18%,#000 82%,transparent);
}

.mqs-10__group {
  flex: none;
  display: flex;
  flex-direction: column;
  gap: var(--gap);
  animation: mqs-10-scroll var(--speed) linear infinite;
  will-change: transform;
}

@keyframes mqs-10-scroll {
  to {
    transform: translateY(calc(-100% - var(--gap)));
  }
}

.mqs-10__col:hover .mqs-10__group,
.mqs-10__col:focus-within .mqs-10__group {
  animation-play-state: paused;
}

.mqs-10__row {
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 19px;
  font-weight: 700;
  color: #3f3f46;
  letter-spacing: -.01em;
}

@media (max-width: 640px) {
  .mqs-10__inner {
    grid-template-columns: 1fr;
    justify-items: center;
    text-align: center;
  }

  .mqs-10__viewport {
    max-height: 45vh;
  }
}

@media (prefers-reduced-motion: reduce) {
  .mqs-10__group {
    animation: none;
  }

  .mqs-10__viewport {
    overflow-y: auto;
    mask-image: none;
    -webkit-mask-image: none;
  }

  .mqs-10__band {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the horizontal pattern rotated: flex-direction:column, an explicit viewport height, translateY(calc(-100% - var(--gap))), and a 180deg mask. */
```
