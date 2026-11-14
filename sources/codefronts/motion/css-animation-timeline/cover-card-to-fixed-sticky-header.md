---
source: "codefronts"
url: "https://codefronts.com/motion/css-animation-timeline/cover-card-to-fixed-sticky-header/"
title: "Cover Card to Fixed Sticky Header"
section: "motion"
category: "css-animation-timeline"
category_name: "CSS animation-timeline Demos"
description: "The recipe-blog / media-profile architecture: a fullscreen cover — photo, title, meta — folds down into a compact sticky top bar as the user scrolls into the…"
has_js: "false"
---

Here's a working CSS animation-timeline Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cover Card to Fixed Sticky Header
Source: https://codefronts.com/motion/css-animation-timeline/cover-card-to-fixed-sticky-header/

The recipe-blog / media-profile architecture: a fullscreen cover — photo, title, meta — folds down into a compact sticky top bar as the user scrolls into the article. Title glides from hero scale to nav scale, the photo dims into a backdrop, actions stay clickable throughout. No window.scrollY, no resize math.
## HTML
```html
<section class="sda-10" aria-label="Cover that folds into a sticky header" role="region" tabindex="0">
  <header class="sda-10__cover">
    <img class="sda-10__photo" src="https://picsum.photos/seed/kitchen-dusk/1400/900" width="1400" height="900" alt="Cast-iron pan of roasted vegetables on a dark table">
    <div class="sda-10__veil" aria-hidden="true"></div>
    <div class="sda-10__bar">
      <h2 class="sda-10__title">Midnight Harvest Roast</h2>
      <div class="sda-10__meta"><span>45 min</span><span aria-hidden="true">·</span><span>Serves 4</span><button class="sda-10__save" type="button">Save ♥</button></div>
    </div>
  </header>
  <article class="sda-10__article">
    <h3>Before you start</h3>
    <p>Scroll and watch the cover fold: the photograph dims into a backdrop, the title slides down its type ramp, and the whole card lands as a 76-pixel bar that stays pinned for the rest of the read.</p>
    <p>Every stage of that fold is one scroll-driven animation sharing a single <code>0 → 70vh</code> range — the title, veil and height are frame-locked, which is precisely what multi-listener JS versions struggle to guarantee during a fast flick.</p>
    <h3>Method</h3>
    <p>Quarter the squash and shallots; toss with oil, maple, and smoked salt. Roast hot — 230°C — turning once, until edges char and centres give.</p>
    <p>Fold through torn kale for the final five minutes. Finish with lemon, seeds, and too much black pepper. Rest in the pan; serve from it.</p>
    <p>Refresh this panel halfway down: the header paints already-folded, because a scroll timeline is resolved state, not replayed events.</p>
    <p class="sda-10__fin">Recipe ends — header still holding. ▍</p>
  </article>
</section>
```
## CSS
```css
.sda-10,
.sda-10 *,
.sda-10 *::before,
.sda-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sda-10 {
  --brand: oklch(0.45 0.09 40);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: oklch(0.96 0.008 60);
  color: oklch(0.25 0.02 40);
  width: 100%;
  height: 100vh;
  overflow-y: auto;
}

.sda-10__cover {
  position: sticky;
  top: 0;
  z-index: 10;
  height: 76px;
  overflow: hidden;
  display: flex;
  align-items: flex-end;
  background: var(--brand);
}

.sda-10__photo {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: .45;
}

.sda-10__veil {
  position: absolute;
  inset: 0;
  background: linear-gradient(rgba(30,18,8,.1),rgba(30,18,8,.72));
}

.sda-10__bar {
  position: relative;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 14px 24px;
  color: #fff;
}

.sda-10__title {
  font-size: 20px;
  font-weight: 800;
  letter-spacing: -.015em;
  text-shadow: 0 1px 12px rgba(0,0,0,.4);
}

.sda-10__meta {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  font-weight: 600;
  opacity: .95;
}

.sda-10__save {
  min-height: 44px;
  padding: 0 18px;
  border: 0;
  border-radius: 999px;
  font: 700 13.5px 'Segoe UI',system-ui,sans-serif;
  background: rgba(255,255,255,.92);
  color: var(--brand);
  cursor: pointer;
}

.sda-10__save:hover {
  background: #fff;
}

.sda-10__save:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 2px;
}

.sda-10__article {
  width: min(620px,100%);
  margin: 0 auto;
  padding: 44px 24px 34vh;
}

.sda-10__article h3 {
  font-size: 21px;
  font-weight: 800;
  letter-spacing: -.01em;
  margin: 26px 0 12px;
}

.sda-10__article p {
  font-size: 16px;
  line-height: 1.75;
  margin-bottom: 18px;
  color: oklch(0.35 0.02 40);
  text-wrap: pretty;
}

.sda-10__article code {
  font: 600 13.5px ui-monospace,Menlo,monospace;
  background: oklch(0.9 0.015 60);
  padding: 2px 6px;
  border-radius: 5px;
}

.sda-10__fin {
  color: oklch(0.55 0.03 40);
  font-style: italic;
}

.sda-10:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: -3px;
}

@supports (animation-timeline: scroll()) {
  .sda-10__cover {
    animation: sda-10-fold linear both;
    animation-timeline: scroll();
    animation-range: 0 70vh;
  }

  .sda-10__title {
    animation: sda-10-title linear both;
    animation-timeline: scroll();
    animation-range: 0 70vh;
  }

  .sda-10__photo {
    animation: sda-10-photo linear both;
    animation-timeline: scroll();
    animation-range: 0 70vh;
  }
}

@keyframes sda-10-fold {
  from {
    height: 100vh;
  }

  to {
    height: 76px;
  }
}

@keyframes sda-10-title {
  from {
    font-size: clamp(34px,6vw,58px);
  }

  to {
    font-size: 20px;
  }
}

@keyframes sda-10-photo {
  from {
    opacity: 1;
    transform: scale(1.06);
  }

  to {
    opacity: .45;
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sda-10__cover,
    .sda-10__title,
    .sda-10__photo {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — cover height, title scale and photo dim share one scroll() timeline over animation-range: 0 70vh, so the fold is frame-locked; fill-mode:both paints the correct state even on mid-page refresh. */
```
