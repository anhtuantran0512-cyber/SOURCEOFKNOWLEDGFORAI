---
source: "codefronts"
url: "https://codefronts.com/layouts/css-two-column-layout/css-two-column-article-layout/"
title: "CSS Two Column Article Layout"
section: "layouts"
category: "css-two-column-layout"
category_name: "CSS Two-Column Layouts"
description: "True newspaper-style text flow: one continuous article poured into two columns with column-count: 2, a hairline column-rule between them, a spanning headline…"
has_js: "false"
---

Here's a working CSS Two-Column Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Two Column Article Layout
Source: https://codefronts.com/layouts/css-two-column-layout/css-two-column-article-layout/

True newspaper-style text flow: one continuous article poured into two columns with column-count: 2, a hairline column-rule between them, a spanning headline (column-span: all), a drop cap and a pull-quote that text wraps around — CSS Multi-column, the two column layout grid and flexbox can’t do.
## HTML
```html
<section class="tcl-12" aria-label="Two column article layout demo">
  <article class="tcl-12__article" lang="en">
    <header class="tcl-12__top">
      <span class="tcl-12__section">Craft · Typography</span>
      <span class="tcl-12__date">31 July 2026</span>
    </header>
    <div class="tcl-12__flow">
      <h1 class="tcl-12__hed">The quiet return of the two-column page</h1>
      <p class="tcl-12__dek">Screens got wide. Lines got long. The oldest layout in publishing is fixing a very modern readability problem.</p>
      <p class="tcl-12__body tcl-12__body--first">For five hundred years, printers solved wide pages the same way: split the text. The column was never decoration — it was a reading tool, keeping each line short enough that the eye could find its way back to the next one without effort.</p>
      <p class="tcl-12__body">The web forgot this for a while. Fluid layouts stretched paragraphs to two hundred characters on desktop monitors, and readability research kept measuring what typographers already knew: comprehension drops as measure grows past about seventy-five characters.</p>
      <aside class="tcl-12__pull"><p>“The column was never decoration — it was a reading tool.”</p></aside>
      <p class="tcl-12__body">CSS Multi-column brings the printer’s fix to the browser in one declaration. Unlike grid, it flows a single story through the gaps — fill the first column, spill into the second — and balances their heights automatically, hyphenating and breaking with rules the specification borrowed directly from print.</p>
      <p class="tcl-12__body">Used with restraint — a feature, an editor’s letter, fine print — it reads beautifully. Used on a three-thousand-word essay it sends readers scrolling back to the top, which is why the pattern thrives in short-form editorial and nowhere else.</p>
    </div>
  </article>
</section>
```
## CSS
```css
.tcl-12,
.tcl-12 *,
.tcl-12 *::before,
.tcl-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tcl-12 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.22 0.01 60);
  --accent: oklch(0.5 0.12 30);
  font-family: Georgia,'Iowan Old Style',serif;
  color: var(--ink);
  background: oklch(0.975 0.006 80);
  padding: clamp(24px,4vw,56px);
}

.tcl-12__article {
  max-width: 820px;
  margin-inline: auto;
}

.tcl-12__top {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  border-bottom: 1px solid oklch(0.85 0.02 70);
  padding-bottom: 10px;
  margin-bottom: 22px;
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.tcl-12__section {
  font: 700 11px/1 inherit;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.tcl-12__date {
  font: 500 12px/1 inherit;
  color: color-mix(in oklab,var(--ink) 55%,transparent);
}

.tcl-12__flow {
  column-count: 2;
  column-gap: 3rem;
  column-rule: 1px solid oklch(0.86 0.02 70);
}

.tcl-12__hed {
  column-span: all;
  font-size: clamp(28px,4.2vw,44px);
  line-height: 1.08;
  letter-spacing: -.02em;
  font-weight: 700;
  margin-bottom: 10px;
  text-wrap: balance;
}

.tcl-12__dek {
  column-span: all;
  font-style: italic;
  font-size: clamp(15px,2vw,18px);
  line-height: 1.5;
  color: color-mix(in oklab,var(--ink) 65%,transparent);
  margin-bottom: 26px;
  text-wrap: pretty;
}

.tcl-12__body {
  font-size: 14.5px;
  line-height: 1.8;
  margin-bottom: 14px;
  text-wrap: pretty;
  hyphens: auto;
}

.tcl-12__body--first::first-letter {
  font-weight: 700;
  color: var(--accent);
  float: left;
  font-size: 52px;
  line-height: .85;
  padding: 4px 8px 0 0;
}

@supports (initial-letter: 3) {
  .tcl-12__body--first::first-letter {
    float: none;
    padding: 0 8px 0 0;
    font-size: inherit;
    initial-letter: 3;
  }
}

.tcl-12__pull {
  break-inside: avoid;
  border-block: 3px solid var(--ink);
  padding: 16px 4px;
  margin: 10px 0 18px;
}

.tcl-12__pull p {
  font-size: 19px;
  line-height: 1.4;
  font-weight: 700;
  letter-spacing: -.01em;
  text-wrap: balance;
}

@media (max-width: 620px) {
  .tcl-12__flow {
    column-count: 1;
    column-rule: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — column-count:2 + column-gap + column-rule flow one text stream through both columns; column-span:all lets the headline escape. */
```
