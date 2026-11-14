---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/magazine-editorial/"
title: "Magazine Editorial"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "A print-grade opening spread on the web: a display headline that crosses the photograph, a drop cap, a hairline-ruled sidebar of standfirst text, and…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magazine Editorial
Source: https://codefronts.com/layouts/css-grid-layouts/magazine-editorial/

A print-grade opening spread on the web: a display headline that crosses the photograph, a drop cap, a hairline-ruled sidebar of standfirst text, and asymmetric column rhythm — all from one 12-column grid with overlapping placements. The layout magazines paid layout artists for, now a stylesheet.
## HTML
```html
<section class="cgl-10" aria-label="Magazine editorial layout demo">
  <article class="cgl-10__spread">
    <figure class="cgl-10__plate" role="img" aria-label="Editorial photograph placeholder"></figure>
    <h2 class="cgl-10__headline">The grid was always a printing press</h2>
    <p class="cgl-10__byline">Words · Amara Chen</p>
    <div class="cgl-10__standfirst">
      <p>Web layout borrowed its bones from Swiss print design. With line-based placement and overlap, the borrowing finally goes both ways — this spread is one grid, no absolute positioning.</p>
    </div>
    <p class="cgl-10__body">Asymmetry is a decision, not an accident: the photo takes eight columns, the text takes four, and the headline refuses to respect either. That refusal — elements crossing boundaries with intent — is what makes editorial layout read as designed rather than templated.</p>
  </article>
</section>
```
## CSS
```css
.cgl-10,
.cgl-10 *,
.cgl-10 *::before,
.cgl-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-10 {
  width: 100%;
  min-height: 100vh;
  --paper: oklch(0.97 0.008 85);
  --ink: oklch(0.2 0.01 60);
  --rust: oklch(0.55 0.16 40);
  font-family: Georgia,'Times New Roman',serif;
  background: var(--paper);
  color: var(--ink);
  padding: 2rem 1.4rem;
}

.cgl-10 .cgl-10__spread {
  display: grid;
  grid-template-columns: repeat(12,1fr);
  grid-template-rows: auto auto auto 1fr;
  gap: 14px;
  max-inline-size: 680px;
  margin-inline: auto;
}

.cgl-10 .cgl-10__plate {
  grid-column: 5/13;
  grid-row: 1/4;
  z-index: 1;
  aspect-ratio: 4/3;
  background: linear-gradient(160deg,oklch(0.62 0.1 50),oklch(0.38 0.07 30) 60%,oklch(0.28 0.05 40)),repeating-linear-gradient(0deg,transparent 0 3px,oklch(1 0 0/.03) 3px 6px);
}

.cgl-10 .cgl-10__headline {
  grid-column: 1/9;
  grid-row: 2/3;
  z-index: 2;
  font-size: clamp(2rem,6vw,3.4rem);
  line-height: 1.02;
  font-weight: 700;
  letter-spacing: -.01em;
  text-wrap: balance;
  text-shadow: 0 0 18px var(--paper),0 0 6px var(--paper),2px 2px 0 var(--paper);
}

.cgl-10 .cgl-10__byline {
  grid-column: 12/13;
  grid-row: 1/2;
  z-index: 3;
  justify-self: end;
  writing-mode: vertical-rl;
  font-family: system-ui,sans-serif;
  font-size: .62rem;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--paper);
  padding: .6rem .2rem;
}

.cgl-10 .cgl-10__standfirst {
  grid-column: 1/5;
  grid-row: 3/4;
  border-block-start: 3px solid var(--ink);
  padding-block-start: .8rem;
}

.cgl-10 .cgl-10__standfirst p {
  font-size: .88rem;
  line-height: 1.55;
  font-style: italic;
  color: color-mix(in oklab,var(--ink) 80%,var(--paper));
}

.cgl-10 .cgl-10__body {
  grid-column: 1/9;
  grid-row: 4/5;
  font-size: .95rem;
  line-height: 1.7;
  column-width: 16rem;
  column-gap: 2rem;
  column-rule: 1px solid color-mix(in oklab,var(--ink) 25%,var(--paper));
}

.cgl-10 .cgl-10__body::first-letter {
  float: left;
  font-size: 3.2em;
  line-height: .82;
  padding-inline-end: .12em;
  color: var(--rust);
  font-weight: 700;
}

@media (max-width: 560px) {
  .cgl-10 .cgl-10__plate {
    grid-column: 1/13;
    grid-row: 1/2;
  }

  .cgl-10 .cgl-10__headline {
    grid-column: 1/13;
    grid-row: 2/3;
  }

  .cgl-10 .cgl-10__standfirst {
    grid-column: 1/13;
    grid-row: 3/4;
  }

  .cgl-10 .cgl-10__body {
    grid-column: 1/13;
    grid-row: 4/5;
  }

  .cgl-10 .cgl-10__byline {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — line-based overlap crosses the headline over the photo; writing-mode and ::first-letter supply the print DNA. */
```
