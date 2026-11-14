---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/newspaper-dividers/"
title: "Multi-Column Newspaper Rule Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "Real newspaper typography, in three properties."
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Column Newspaper Rule Divider CSS
Source: https://codefronts.com/snippets/css-dividers/newspaper-dividers/

Real newspaper typography, in three properties. CSS multi-column gives you column-rule — a vertical hairline drawn in the gutter automatically, at the right height, that reflows when the column count changes and disappears when the layout drops to one column. Paired with a double-rule masthead and a hanging section label, it turns any article into a broadsheet without a single wrapper div.
## HTML
```html
<section class="div-21" aria-label="Newspaper column rule divider demo">
  <div class="div-21__stage">
    <header class="div-21__masthead">
      <p class="div-21__dateline">VOL. XXVI · FRIDAY EDITION · CODEFRONTS</p>
      <h2 class="div-21__logo">The Daily Rule</h2>
    </header>
    <p class="div-21__standfirst">Multi-column layout draws its own dividers — and removes them when the columns do.</p>
    <div class="div-21__cols">
      <p>Compositors set metal rules between columns by hand, one lead strip at a time, because the eye needs a boundary that a gutter alone cannot supply. The browser now does it with a single property, and does it better: the rule appears only where two columns actually meet.</p>
      <p>That is the quiet advantage of <b>column-rule</b> over a border on a wrapper. Borders belong to boxes, and boxes do not know how many siblings survived a reflow. A column rule belongs to the gutter itself.</p>
      <p>Give the shorthand a minimum column width and the layout collapses gracefully on a phone, taking its rules with it. No media query is involved at any point, which is roughly the opposite of how most people build a three-column article.</p>
      <p>Set <b>break-inside:avoid</b> on anything boxed — a pull quote, a figure, a card — or the engine will happily slice it across the gutter and your beautiful rule will run straight through the middle of it.</p>
    </div>
    <p class="div-21__chip">columns:3 220px · column-rule · column-span:all</p>
  </div>
</section>
```
## CSS
```css
.div-21 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-21-bg);
  --div-21-bg: oklch(0.965 0.008 88);
  --div-21-ink: oklch(0.2 0.012 60);
  --div-21-mut: oklch(0.5 0.015 60);
  --div-21-line: oklch(0.2 0.012 60/.42);
  --div-21-acc: oklch(0.48 0.13 25);
  font-family: Georgia,'Iowan Old Style','Times New Roman',serif;
  color: var(--div-21-ink);
}

.div-21 *,
.div-21 *::before,
.div-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-21__stage {
  min-height: 100svh;
  width: min(94vw,860px);
  margin-inline: auto;
  display: grid;
  align-content: center;
  gap: 16px;
  padding: clamp(26px,5vw,64px) 0;
}

.div-21__masthead {
  text-align: center;
  padding-bottom: 12px;
  background: linear-gradient(var(--div-21-line) 0 0) 0 100%/100% 3px no-repeat;
}

.div-21__dateline {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10px;
  letter-spacing: .24em;
  color: var(--div-21-mut);
  padding-bottom: 10px;
  background: linear-gradient(var(--div-21-line) 0 0) 0 100%/100% 1px no-repeat;
  margin-bottom: 12px;
}

.div-21__logo {
  font-size: clamp(32px,7.6vw,72px);
  line-height: 1;
  font-weight: 400;
  letter-spacing: -.015em;
  font-variant: small-caps;
}

.div-21__standfirst {
  text-align: center;
  font-size: clamp(15px,2.1vw,19px);
  line-height: 1.5;
  font-style: italic;
  color: var(--div-21-mut);
  max-width: 56ch;
  margin-inline: auto;
  padding-bottom: 14px;
  text-wrap: balance;
}

.div-21__cols {
  columns: 3 210px;
  column-gap: clamp(20px,3.4vw,36px);
  column-rule: 1px solid var(--div-21-line);
  text-align: justify;
  hyphens: auto;
}

.div-21__cols p {
  font-size: clamp(13.5px,1.6vw,15.5px);
  line-height: 1.62;
  margin-bottom: 1em;
  break-inside: avoid-column;
  text-indent: 1.2em;
}

.div-21__cols p:first-child {
  text-indent: 0;
}

.div-21__cols b {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  font-weight: 600;
  color: var(--div-21-acc);
}

.div-21__chip {
  justify-self: center;
  margin-top: 8px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-21-mut);
  padding: 8px 14px;
  border: 1px solid var(--div-21-line);
  border-radius: 99px;
}
```
