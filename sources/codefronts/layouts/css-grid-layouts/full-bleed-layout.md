---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/full-bleed-layout/"
title: "Full-Bleed Layout"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "The layout every long-form article needs: body text locked to a readable 65ch measure, while images and pull-quotes break out to the full viewport width — no…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full-Bleed Layout
Source: https://codefronts.com/layouts/css-grid-layouts/full-bleed-layout/

The layout every long-form article needs: body text locked to a readable 65ch measure, while images and pull-quotes break out to the full viewport width — no negative margins, no calc() hacks, no wrapper divs. One named-line grid does all of it, and any child can opt into full bleed with a single class.
## HTML
```html
<section class="cgl-01" aria-label="Full-bleed layout demo">
  <article class="cgl-01__article">
    <header class="cgl-01__head">
      <p class="cgl-01__kicker">Layout Pattern № 01</p>
      <h2>The measure stays put. The imagery doesn't.</h2>
    </header>
    <p>Body copy locks to a comfortable 65-character measure, centred by two elastic gutter tracks. Resize the page — the text column holds while the gutters breathe.</p>
    <figure class="cgl-01__media cgl-01__media--bleed">
      <div class="cgl-01__ph" role="img" aria-label="Full-width placeholder image"></div>
      <figcaption>This figure spans grid-column: full — edge to edge, no negative margins.</figcaption>
    </figure>
    <p>Back in the content column, as if nothing happened. Any element can opt out with one class; everything else flows normally.</p>
    <blockquote class="cgl-01__quote cgl-01__quote--bleed"><p>"Full bleed is a grid decision, not a margin hack."</p></blockquote>
  </article>
</section>
```
## CSS
```css
.cgl-01,
.cgl-01 *,
.cgl-01 *::before,
.cgl-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-01 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.24 0.02 60);
  --paper: oklch(0.97 0.012 85);
  --accent: oklch(0.55 0.14 40);
  font-family: Georgia,'Times New Roman',serif;
  color: var(--ink);
  background: var(--paper);
}

.cgl-01 .cgl-01__article {
  display: grid;
  grid-template-columns: [full-start] minmax(1.5rem,1fr) [content-start] min(65ch,100% - 3rem) [content-end] minmax(1.5rem,1fr) [full-end];
  row-gap: 1.4rem;
  padding-block: 3rem;
}

.cgl-01 .cgl-01__article>* {
  grid-column: content;
}

.cgl-01 .cgl-01__media--bleed,
.cgl-01 .cgl-01__quote--bleed {
  grid-column: full;
}

.cgl-01 .cgl-01__kicker {
  font-family: system-ui,sans-serif;
  font-size: .72rem;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--accent);
  margin-block-end: .6rem;
}

.cgl-01 h2 {
  font-size: clamp(1.5rem,4vw,2.2rem);
  line-height: 1.15;
  text-wrap: balance;
}

.cgl-01 p {
  font-size: 1.02rem;
  line-height: 1.65;
}

.cgl-01 .cgl-01__ph {
  inline-size: 100%;
  aspect-ratio: 21/7;
  background: linear-gradient(115deg,oklch(0.62 0.13 40),oklch(0.48 0.1 25) 50%,oklch(0.35 0.07 50)),repeating-linear-gradient(-45deg,transparent 0 18px,oklch(1 0 0/.06) 18px 36px);
  background-blend-mode: overlay,normal;
}

.cgl-01 figcaption {
  font-family: system-ui,sans-serif;
  font-size: .75rem;
  color: color-mix(in oklab,var(--ink) 60%,var(--paper));
  padding-inline: 1.5rem;
  padding-block-start: .5rem;
}

.cgl-01 .cgl-01__quote--bleed {
  background: var(--ink);
  color: var(--paper);
  padding-block: 2.2rem;
  padding-inline: 1.5rem;
  display: grid;
  grid-template-columns: inherit;
}

.cgl-01 .cgl-01__quote--bleed p {
  grid-column: content;
  font-size: clamp(1.2rem,3vw,1.6rem);
  font-style: italic;
  line-height: 1.4;
}

@supports not (display: grid) {
  .cgl-01 .cgl-01__article {
    max-inline-size: 65ch;
    margin-inline: auto;
    padding-inline: 1.5rem;
  }
}
```

## JavaScript
```js
/* No JavaScript — named grid lines create a 'content' and 'full' area; children opt into bleed with grid-column: full. */
```
