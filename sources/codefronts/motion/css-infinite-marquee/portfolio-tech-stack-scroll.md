---
source: "codefronts"
url: "https://codefronts.com/motion/css-infinite-marquee/portfolio-tech-stack-scroll/"
title: "Portfolio Tech Stack Marquee — Developer Skills Scroll"
section: "motion"
category: "css-infinite-marquee"
category_name: "CSS Infinite Marquee Designs"
description: "The 'Skills' section upgrade for developer portfolios: technology chips with monogram icons drifting in a slim rail, each chip snapping to full color and…"
has_js: "false"
---

Here's a working CSS Infinite Marquee Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Portfolio Tech Stack Marquee — Developer Skills Scroll
Source: https://codefronts.com/motion/css-infinite-marquee/portfolio-tech-stack-scroll/

The 'Skills' section upgrade for developer portfolios: technology chips with monogram icons drifting in a slim rail, each chip snapping to full color and lifting on hover, plus a direction toggle (a checkbox flipping animation-direction with :has()) that doubles as a tiny easter egg for visitors who find it.
## HTML
```html
<section class="mqs-08" aria-label="Tech stack marquee demo">
  <div class="mqs-08__inner">
    <div class="mqs-08__head">
      <h3 class="mqs-08__title">Tools I ship with</h3>
      <input class="mqs-08__revBox" type="checkbox" id="mqs-08-rev">
      <label class="mqs-08__revBtn" for="mqs-08-rev">⇄ Reverse</label>
    </div>
    <ul class="mqs-08__srList">
      <li>TypeScript</li><li>React</li><li>Node.js</li><li>PostgreSQL</li><li>Tailwind CSS</li><li>Rust</li><li>Docker</li><li>Figma</li>
    </ul>
    <div class="mqs-08__rail" aria-hidden="true">
      <div class="mqs-08__group">
        <span class="mqs-08__chip" style="--c:#3178c6"><span class="mqs-08__tile">TS</span>TypeScript</span>
        <span class="mqs-08__chip" style="--c:#149eca"><span class="mqs-08__tile">Re</span>React</span>
        <span class="mqs-08__chip" style="--c:#5fa04e"><span class="mqs-08__tile">No</span>Node.js</span>
        <span class="mqs-08__chip" style="--c:#336791"><span class="mqs-08__tile">Pg</span>PostgreSQL</span>
        <span class="mqs-08__chip" style="--c:#0ea5e9"><span class="mqs-08__tile">Tw</span>Tailwind CSS</span>
        <span class="mqs-08__chip" style="--c:#b7410e"><span class="mqs-08__tile">Rs</span>Rust</span>
        <span class="mqs-08__chip" style="--c:#2496ed"><span class="mqs-08__tile">Dk</span>Docker</span>
        <span class="mqs-08__chip" style="--c:#a259ff"><span class="mqs-08__tile">Fg</span>Figma</span>
      </div>
      <div class="mqs-08__group">
        <span class="mqs-08__chip" style="--c:#3178c6"><span class="mqs-08__tile">TS</span>TypeScript</span>
        <span class="mqs-08__chip" style="--c:#149eca"><span class="mqs-08__tile">Re</span>React</span>
        <span class="mqs-08__chip" style="--c:#5fa04e"><span class="mqs-08__tile">No</span>Node.js</span>
        <span class="mqs-08__chip" style="--c:#336791"><span class="mqs-08__tile">Pg</span>PostgreSQL</span>
        <span class="mqs-08__chip" style="--c:#0ea5e9"><span class="mqs-08__tile">Tw</span>Tailwind CSS</span>
        <span class="mqs-08__chip" style="--c:#b7410e"><span class="mqs-08__tile">Rs</span>Rust</span>
        <span class="mqs-08__chip" style="--c:#2496ed"><span class="mqs-08__tile">Dk</span>Docker</span>
        <span class="mqs-08__chip" style="--c:#a259ff"><span class="mqs-08__tile">Fg</span>Figma</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.mqs-08,
.mqs-08 *,
.mqs-08 *::before,
.mqs-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.mqs-08 {
  min-height: 100vh;
  width: 100%;
  --gap: 14px;
  --speed: 26s;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #0c0a09;
  padding: 64px 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.mqs-08__inner {
  width: min(860px,100%);
}

.mqs-08__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 24px;
}

.mqs-08__title {
  font-size: clamp(18px,3vw,23px);
  font-weight: 800;
  color: #fafaf9;
  letter-spacing: -.02em;
}

.mqs-08__revBox {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.mqs-08__revBtn {
  font-size: 12px;
  font-weight: 600;
  color: #a8a29e;
  border: 1px solid #292524;
  border-radius: 999px;
  padding: 6px 14px;
  cursor: pointer;
  user-select: none;
  transition: color .15s,border-color .15s;
}

.mqs-08__revBtn:hover {
  color: #fafaf9;
  border-color: #57534e;
}

.mqs-08__revBox:focus-visible + .mqs-08__revBtn {
  outline: 2px solid #fafaf9;
  outline-offset: 2px;
}

.mqs-08__srList {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.mqs-08__rail {
  display: flex;
  gap: var(--gap);
  overflow: hidden;
  padding-block: 6px;
  mask-image: linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent);
  -webkit-mask-image: linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent);
}

.mqs-08__group {
  flex: none;
  display: flex;
  gap: var(--gap);
  animation: mqs-08-scroll var(--speed) linear infinite;
  will-change: transform;
}

@keyframes mqs-08-scroll {
  to {
    transform: translateX(calc(-100% - var(--gap)));
  }
}

.mqs-08:has(.mqs-08__revBox:checked) .mqs-08__group {
  animation-direction: reverse;
}

.mqs-08__rail:hover .mqs-08__group {
  animation-play-state: paused;
}

.mqs-08__chip {
  flex: none;
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 13.5px;
  font-weight: 600;
  color: #d6d3d1;
  background: #1c1917;
  border: 1px solid #292524;
  border-radius: 999px;
  padding: 7px 16px 7px 7px;
  filter: grayscale(.85);
  transition: filter .2s,transform .2s,border-color .2s;
  cursor: default;
}

.mqs-08__chip:hover {
  filter: grayscale(0);
  transform: translateY(-2px);
  border-color: var(--c);
}

.mqs-08__tile {
  width: 26px;
  height: 26px;
  border-radius: 8px;
  display: grid;
  place-items: center;
  font-size: 11px;
  font-weight: 800;
  color: #fff;
  background: var(--c);
}

@media (prefers-reduced-motion: reduce) {
  .mqs-08__rail {
    overflow: visible;
    mask-image: none;
    -webkit-mask-image: none;
    flex-wrap: wrap;
  }

  .mqs-08__group {
    animation: none;
    flex-wrap: wrap;
  }

  .mqs-08__group + .mqs-08__group {
    display: none;
  }

  .mqs-08__chip {
    filter: none;
  }

  .mqs-08__revBtn {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the reverse toggle is a checkbox + :has(:checked) flipping animation-direction; modern engines re-map progress so the rail changes course smoothly. */
```
