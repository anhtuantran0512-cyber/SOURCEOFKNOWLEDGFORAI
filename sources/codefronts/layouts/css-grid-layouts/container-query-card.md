---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/container-query-card/"
title: "Container-Query Card"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "One card component, two layouts — decided by the card's OWN width, not the viewport."
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Container-Query Card
Source: https://codefronts.com/layouts/css-grid-layouts/container-query-card/

One card component, two layouts — decided by the card's OWN width, not the viewport. Dropped into the wide main column it goes horizontal; the identical markup in the narrow sidebar stacks vertically. This is the component-portability upgrade media queries could never deliver.
## HTML
```html
<section class="cgl-20" aria-label="Container query card demo">
  <div class="cgl-20__page">
    <main class="cgl-20__main">
      <p class="cgl-20__where">main · wide container → horizontal card</p>
      <div class="cgl-20__holder">
        <article class="cgl-20__card">
          <div class="cgl-20__media" role="img" aria-label="Coastal trail placeholder"></div>
          <div class="cgl-20__body"><h4>Coastal trail guide</h4><p>Same markup, same stylesheet. The card asked its container — not the viewport — how much room it has.</p><a href="#0">Read guide →</a></div>
        </article>
      </div>
    </main>
    <aside class="cgl-20__aside">
      <p class="cgl-20__where">aside · narrow → stacked</p>
      <div class="cgl-20__holder">
        <article class="cgl-20__card">
          <div class="cgl-20__media" role="img" aria-label="Coastal trail placeholder"></div>
          <div class="cgl-20__body"><h4>Coastal trail guide</h4><p>Identical component, adapted by @container.</p><a href="#0">Read guide →</a></div>
        </article>
      </div>
    </aside>
  </div>
</section>
```
## CSS
```css
.cgl-20,
.cgl-20 *,
.cgl-20 *::before,
.cgl-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-20 {
  width: 100%;
  min-height: 100vh;
  --peach: oklch(0.78 0.11 45);
  --ink: oklch(0.28 0.04 45);
  --bg: oklch(0.965 0.012 60);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 1.4rem;
}

.cgl-20 .cgl-20__page {
  display: grid;
  grid-template-columns: minmax(0,2fr) minmax(0,1fr);
  gap: 14px;
}

.cgl-20 .cgl-20__where {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .66rem;
  color: color-mix(in oklab,var(--ink) 60%,var(--bg));
  margin-block-end: .5rem;
}

.cgl-20 .cgl-20__holder {
  container-type: inline-size;
  container-name: card;
}

.cgl-20 .cgl-20__card {
  display: grid;
  grid-template-areas: "media" "body";
  border-radius: 14px;
  overflow: hidden;
  background: white;
  border: 1px solid color-mix(in oklab,var(--peach) 45%,white);
  box-shadow: 0 12px 28px -20px oklch(0.45 0.08 45/.7);
}

.cgl-20 .cgl-20__media {
  grid-area: media;
  min-block-size: 110px;
  background: linear-gradient(140deg,var(--peach),oklch(0.55 0.12 25));
}

.cgl-20 .cgl-20__body {
  grid-area: body;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: .5rem;
}

.cgl-20 h4 {
  font-size: clamp(.9rem,4.5cqi,1.15rem);
  color: var(--ink);
}

.cgl-20 .cgl-20__body p {
  font-size: .78rem;
  line-height: 1.55;
  color: color-mix(in oklab,var(--ink) 70%,white);
}

.cgl-20 .cgl-20__body a {
  font-size: .78rem;
  font-weight: 600;
  color: oklch(0.55 0.14 35);
  text-decoration: none;
  margin-block-start: auto;
}

.cgl-20 .cgl-20__body a:hover {
  text-decoration: underline;
}

.cgl-20 .cgl-20__body a:focus-visible {
  outline: 2px solid var(--peach);
  outline-offset: 2px;
}

@container card (min-width: 380px) {
  .cgl-20 .cgl-20__card {
    grid-template-areas: "media body";
    grid-template-columns: 140px minmax(0,1fr);
  }

  .cgl-20 .cgl-20__media {
    min-block-size: 100%;
  }
}

@media (max-width: 600px) {
  .cgl-20 .cgl-20__page {
    grid-template-columns: minmax(0,1fr);
  }
}
```

## JavaScript
```js
/* No JavaScript — container-type: inline-size on the wrapper; @container swaps the card's internal grid-template-areas. */
```
