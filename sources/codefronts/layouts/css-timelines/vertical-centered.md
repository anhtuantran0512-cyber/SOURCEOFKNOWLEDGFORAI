---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/vertical-centered/"
title: "Zigzag Alternating Timeline — Container Query Responsive"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "The classic center-spine zigzag — cards alternating left and right of a vertical rail with arrow notches pointing at their markers — made truly portable: it…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Zigzag Alternating Timeline — Container Query Responsive
Source: https://codefronts.com/layouts/css-timelines/vertical-centered/

The classic center-spine zigzag — cards alternating left and right of a vertical rail with arrow notches pointing at their markers — made truly portable: it reshapes to a single left-rail column when its CONTAINER drops below 560px, not the viewport. Drop it in a sidebar, a modal or a split view and it lays itself out correctly with zero configuration.
## HTML
```html
<section class="tls-21" aria-label="Zigzag container query timeline demo">
  <div class="tls-21__frame">
    <h3 class="tls-21__title">Company milestones</h3>
    <div class="tls-21__container">
      <ol class="tls-21__grid" role="list">
        <li class="tls-21__item">
          <div class="tls-21__card">
            <time class="tls-21__date" datetime="2022">2022</time>
            <h4 class="tls-21__h">Founded in a garage</h4>
            <p class="tls-21__p">Two founders, one whiteboard, no name for six weeks.</p>
          </div>
        </li>
        <li class="tls-21__item">
          <div class="tls-21__card">
            <time class="tls-21__date" datetime="2023">2023</time>
            <h4 class="tls-21__h">Seed round</h4>
            <p class="tls-21__p">$2.4M to hire the first five engineers and a very good office dog.</p>
          </div>
        </li>
        <li class="tls-21__item">
          <div class="tls-21__card">
            <time class="tls-21__date" datetime="2024">2024</time>
            <h4 class="tls-21__h">First enterprise customer</h4>
            <p class="tls-21__p">A 3,000-seat rollout that rewrote our definition of 'edge case'.</p>
          </div>
        </li>
        <li class="tls-21__item">
          <div class="tls-21__card">
            <time class="tls-21__date" datetime="2025">2025</time>
            <h4 class="tls-21__h">Series A</h4>
            <p class="tls-21__p">$18M led by our earliest angel. The dog got a title.</p>
          </div>
        </li>
      </ol>
    </div>
  </div>
</section>
```
## CSS
```css
.tls-21,
.tls-21 *,
.tls-21 *::before,
.tls-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-21 {
  min-height: 100vh;
  width: 100%;
  --tl-accent: #0e7490;
  --tl-line: #d3e3e8;
  --tl-card: #ffffff;
  --tl-bg: #f2f7f9;
  --tl-ink: #164252;
  --tl-mut: #5e7d8a;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--tl-bg);
  padding: 64px 24px;
  display: grid;
  place-items: center;
}

.tls-21__frame {
  width: min(760px,100%);
}

.tls-21__title {
  font-size: clamp(22px,3.5vw,28px);
  font-weight: 800;
  color: var(--tl-ink);
  letter-spacing: -.02em;
  text-align: center;
  margin-bottom: 36px;
}

.tls-21__container {
  container-type: inline-size;
}

.tls-21__grid {
  list-style: none;
  display: grid;
  grid-template-columns: 1fr 48px 1fr;
}

.tls-21__item {
  position: relative;
  padding-bottom: 28px;
}

.tls-21__item:nth-child(odd) {
  grid-column: 1;
}

.tls-21__item:nth-child(even) {
  grid-column: 3;
}

.tls-21__item::before {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  width: 2px;
  background: var(--tl-line);
}

.tls-21__item:nth-child(odd)::before {
  right: -25px;
}

.tls-21__item:nth-child(even)::before {
  left: -25px;
}

.tls-21__item:last-child::before {
  bottom: auto;
  height: 28px;
}

.tls-21__item::after {
  content: '';
  position: absolute;
  top: 22px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--tl-accent);
  border: 3px solid var(--tl-bg);
  z-index: 1;
}

.tls-21__item:nth-child(odd)::after {
  right: -31px;
}

.tls-21__item:nth-child(even)::after {
  left: -31px;
}

.tls-21__card {
  position: relative;
  background: var(--tl-card);
  border: 1px solid var(--tl-line);
  border-radius: 14px;
  padding: 18px 20px;
  box-shadow: 0 2px 10px -6px rgba(20,66,82,.15);
}

.tls-21__card::after {
  content: '';
  position: absolute;
  top: 22px;
  width: 12px;
  height: 12px;
  background: var(--tl-card);
  border: 1px solid var(--tl-line);
  rotate: 45deg;
}

.tls-21__item:nth-child(odd) .tls-21__card::after {
  right: -7px;
  border-left: none;
  border-bottom: none;
}

.tls-21__item:nth-child(even) .tls-21__card::after {
  left: -7px;
  border-right: none;
  border-top: none;
}

.tls-21__date {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .1em;
  color: var(--tl-accent);
}

.tls-21__h {
  font-size: 16.5px;
  font-weight: 750;
  color: var(--tl-ink);
  margin: 5px 0 5px;
  letter-spacing: -.01em;
}

.tls-21__p {
  font-size: 13.5px;
  line-height: 1.55;
  color: var(--tl-mut);
  text-wrap: pretty;
}

@container (max-width: 560px) {
  .tls-21__grid {
    grid-template-columns: 24px 1fr;
  }

  .tls-21__item:nth-child(odd),
    .tls-21__item:nth-child(even) {
    grid-column: 2;
  }

  .tls-21__item:nth-child(odd)::before,
    .tls-21__item:nth-child(even)::before {
    left: -13px;
    right: auto;
  }

  .tls-21__item:nth-child(odd)::after,
    .tls-21__item:nth-child(even)::after {
    left: -19px;
    right: auto;
  }

  .tls-21__item:nth-child(odd) .tls-21__card::after,
    .tls-21__item:nth-child(even) .tls-21__card::after {
    left: -7px;
    right: auto;
    border: 1px solid var(--tl-line);
    border-right: none;
    border-top: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — container-type:inline-size on the wrapper + one @container (max-width:560px) block flips the zigzag to a single left-rail column based on the CONTAINER's width, not the viewport. */
```
