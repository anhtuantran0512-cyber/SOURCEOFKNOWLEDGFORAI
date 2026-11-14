---
source: "codefronts"
url: "https://codefronts.com/motion/css-infinite-marquee/sponsor-exhibitor-banner-tier-rows/"
title: "Sponsor & Exhibitor Banner with Gold / Silver Tier Rows"
section: "motion"
category: "css-infinite-marquee"
category_name: "CSS Infinite Marquee Designs"
description: "Built for event and conference landing pages: a compact sponsor strip where the Gold tier scrolls large and slow (maximum eyeball time per sponsor) and the…"
has_js: "false"
---

Here's a working CSS Infinite Marquee Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sponsor & Exhibitor Banner with Gold / Silver Tier Rows
Source: https://codefronts.com/motion/css-infinite-marquee/sponsor-exhibitor-banner-tier-rows/

Built for event and conference landing pages: a compact sponsor strip where the Gold tier scrolls large and slow (maximum eyeball time per sponsor) and the Silver tier runs smaller and faster below it — tier hierarchy expressed purely through size and speed, in a sliver of vertical space.
## HTML
```html
<section class="mqs-03" aria-label="Sponsor tier banner marquee demo">
  <div class="mqs-03__banner">
    <div class="mqs-03__row">
      <span class="mqs-03__tier">Gold</span>
      <div class="mqs-03__viewport">
        <div class="mqs-03__group" style="--size:20px;--speed:34s">
          <span class="mqs-03__logo">HELIOSPAY</span><span class="mqs-03__logo">Vantage Cloud</span><span class="mqs-03__logo">Kestrel Labs</span><span class="mqs-03__logo">ORBITDESK</span><span class="mqs-03__logo">Praxa</span>
        </div>
        <div class="mqs-03__group" style="--size:20px;--speed:34s" aria-hidden="true">
          <span class="mqs-03__logo">HELIOSPAY</span><span class="mqs-03__logo">Vantage Cloud</span><span class="mqs-03__logo">Kestrel Labs</span><span class="mqs-03__logo">ORBITDESK</span><span class="mqs-03__logo">Praxa</span>
        </div>
      </div>
    </div>
    <div class="mqs-03__row mqs-03__row--silver">
      <span class="mqs-03__tier">Silver</span>
      <div class="mqs-03__viewport">
        <div class="mqs-03__group" style="--size:14px;--speed:22s">
          <span class="mqs-03__logo">Fathom</span><span class="mqs-03__logo">Brightline</span><span class="mqs-03__logo">Copperleaf</span><span class="mqs-03__logo">Nimbus IO</span><span class="mqs-03__logo">Tallgrass</span><span class="mqs-03__logo">Meridian</span><span class="mqs-03__logo">Slateworks</span>
        </div>
        <div class="mqs-03__group" style="--size:14px;--speed:22s" aria-hidden="true">
          <span class="mqs-03__logo">Fathom</span><span class="mqs-03__logo">Brightline</span><span class="mqs-03__logo">Copperleaf</span><span class="mqs-03__logo">Nimbus IO</span><span class="mqs-03__logo">Tallgrass</span><span class="mqs-03__logo">Meridian</span><span class="mqs-03__logo">Slateworks</span>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.mqs-03,
.mqs-03 *,
.mqs-03 *::before,
.mqs-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.mqs-03 {
  min-height: 100vh;
  width: 100%;
  --gap: 44px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #111113;
  padding: 56px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.mqs-03__banner {
  width: 100%;
  border-block: 1px solid #2a2a2e;
  padding-block: 18px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.mqs-03__row {
  display: flex;
  align-items: center;
  gap: 18px;
}

.mqs-03__tier {
  flex: none;
  width: 34px;
  writing-mode: vertical-rl;
  rotate: 180deg;
  text-align: center;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: #d4a537;
}

.mqs-03__row--silver .mqs-03__tier {
  color: #8e9299;
}

.mqs-03__viewport {
  flex: 1;
  display: flex;
  gap: var(--gap);
  overflow: hidden;
  mask-image: linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);
  -webkit-mask-image: linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);
}

.mqs-03__group {
  flex: none;
  display: flex;
  align-items: center;
  gap: var(--gap);
  animation: mqs-03-scroll var(--speed) linear infinite;
  will-change: transform;
}

@keyframes mqs-03-scroll {
  to {
    transform: translateX(calc(-100% - var(--gap)));
  }
}

.mqs-03__banner:hover .mqs-03__group,
.mqs-03__banner:focus-within .mqs-03__group {
  animation-play-state: paused;
}

.mqs-03__logo {
  flex: none;
  position: relative;
  font-size: var(--size);
  font-weight: 700;
  letter-spacing: .04em;
  color: #e8e6e1;
}

.mqs-03__row--silver .mqs-03__logo {
  color: #a9adb4;
  font-weight: 600;
}

.mqs-03__logo::after {
  content: '·';
  position: absolute;
  right: calc(var(--gap) / -2);
  top: 50%;
  translate: 50% -50%;
  color: #3f3f46;
}

@media (prefers-reduced-motion: reduce) {
  .mqs-03__group {
    animation: none;
  }

  .mqs-03__viewport {
    overflow-x: auto;
    mask-image: none;
    -webkit-mask-image: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — tier hierarchy is two CSS tokens (--size, --speed) per row on one shared keyframe. */
```
