---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/infinite-sliding-kinetic-marquee/"
title: "Infinite Sliding Kinetic Marquee"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A kinetic editorial CTA that trades a static label for a continuously scrolling marquee on hover — the phrase repeats and slides endlessly across the pill."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Infinite Sliding Kinetic Marquee
Source: https://codefronts.com/motion/css-button-hover-effects/infinite-sliding-kinetic-marquee/

A kinetic editorial CTA that trades a static label for a continuously scrolling marquee on hover — the phrase repeats and slides endlessly across the pill.
## HTML
```html
<div class="bhe-07-group">
<section class="bhe-07a" aria-label="Kinetic marquee button">
  <button class="bhe-07a__btn" type="button" aria-label="Book tickets"><span class="bhe-07a__static" aria-hidden="true">Book tickets</span><span class="bhe-07a__track" aria-hidden="true"><span>Book tickets</span><span>Book tickets</span><span>Book tickets</span><span>Book tickets</span></span></button>
</section>
<section class="bhe-07b" aria-label="Vertical marquee button">
  <button class="bhe-07b__btn" type="button" aria-label="Shop the drop"><span class="bhe-07b__col" aria-hidden="true"><span>Shop the drop</span><span>Shop the drop</span></span></button>
</section>
</div>
```
## CSS
```css
.bhe-07-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-07-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-07a,
.bhe-07a *,
.bhe-07a *::before,
.bhe-07a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-07a {
  --accent: oklch(0.55 0.2 15);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #faf7f2;
}

.bhe-07a__btn {
  position: relative;
  overflow: hidden;
  width: 230px;
  height: 60px;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: .04em;
  color: #fff;
  border: none;
  border-radius: 9999px;
  cursor: pointer;
  background: var(--accent);
}

.bhe-07a__static {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  transition: opacity .2s;
}

.bhe-07a__track {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  gap: 34px;
  padding-left: 34px;
  white-space: nowrap;
  opacity: 0;
  transition: opacity .2s;
}

.bhe-07a__btn:hover .bhe-07a__static,
.bhe-07a__btn:focus-visible .bhe-07a__static {
  opacity: 0;
}

.bhe-07a__btn:hover .bhe-07a__track,
.bhe-07a__btn:focus-visible .bhe-07a__track {
  opacity: 1;
  animation: bhe-07a-scroll 6s linear infinite;
}

.bhe-07a__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@keyframes bhe-07a-scroll {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(-50%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-07a__btn:hover .bhe-07a__track,
    .bhe-07a__btn:focus-visible .bhe-07a__track {
    animation: none;
    opacity: 0;
  }

  .bhe-07a__btn:hover .bhe-07a__static,
    .bhe-07a__btn:focus-visible .bhe-07a__static {
    opacity: 1;
  }
}

.bhe-07b,
.bhe-07b *,
.bhe-07b *::before,
.bhe-07b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-07b {
  --accent: oklch(0.55 0.18 285);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #0e0b1a;
}

.bhe-07b__btn {
  position: relative;
  overflow: hidden;
  width: 220px;
  height: 58px;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: var(--accent);
}

.bhe-07b__col {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
}

.bhe-07b__col span {
  display: grid;
  place-items: center;
  height: 58px;
  flex: none;
}

.bhe-07b__btn:hover .bhe-07b__col,
.bhe-07b__btn:focus-visible .bhe-07b__col {
  animation: bhe-07b-roll 1.6s linear infinite;
}

.bhe-07b__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@keyframes bhe-07b-roll {
  from {
    transform: translateY(0);
  }

  to {
    transform: translateY(-58px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-07b__btn:hover .bhe-07b__col,
    .bhe-07b__btn:focus-visible .bhe-07b__col {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
