---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/fashion-dividers/"
title: "Editorial Thin Double-Line Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "The double rule is a typographic device, not just two lines — the classical form pairs a heavy line with a light one, and the order signals whether the break…"
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Editorial Thin Double-Line Divider CSS
Source: https://codefronts.com/snippets/css-dividers/fashion-dividers/

The double rule is a typographic device, not just two lines — the classical form pairs a heavy line with a light one, and the order signals whether the break opens or closes a section. This demo shows border-style:double, the two-background alternative that lets you control each weight independently, and the asymmetric "Oxford rule" that magazine art directors actually use.
## HTML
```html
<section class="div-17" aria-label="Editorial thin double-line divider demo">
  <article class="div-17__stage">
    <p class="div-17__kicker">LOOKBOOK · AUTUMN</p>
    <hr class="div-17__oxford">
    <h2 class="div-17__title">Weight, Gap, Weight</h2>
    <p class="div-17__body">The classical double rule is asymmetric on purpose. Heavy over light opens a section and points the reader downward; light over heavy closes one and lifts the eye back up the column.</p>
    <hr class="div-17__double">
    <p class="div-17__cap">border-style:double — one property, three equal parts, no independent control.</p>
    <hr class="div-17__oxford div-17__oxford--close">
    <p class="div-17__cap">Two background layers — 1px over 3px. The same rule, reversed, closes the section.</p>
    <hr class="div-17__inset">
    <p class="div-17__chip">linear-gradient(c 0 0) idiom · Oxford rule · double needs ≥3px</p>
  </article>
</section>
```
## CSS
```css
.div-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-17-bg);
  --div-17-bg: oklch(0.968 0.005 250);
  --div-17-ink: oklch(0.21 0.014 265);
  --div-17-mut: oklch(0.53 0.016 265);
  --div-17-line: oklch(0.21 0.014 265/.7);
  --div-17-acc: oklch(0.58 0.14 25);
  font-family: Georgia,'Iowan Old Style','Times New Roman',serif;
  color: var(--div-17-ink);
}

.div-17 *,
.div-17 *::before,
.div-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-17__stage {
  min-height: 100svh;
  width: min(92vw,60ch);
  margin-inline: auto;
  display: grid;
  align-content: center;
  padding: clamp(30px,6vw,76px) 0;
}

.div-17__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .24em;
  color: var(--div-17-acc);
}

.div-17__oxford {
  border: 0;
  height: 7px;
  margin-block: 14px 22px;
  background: linear-gradient(var(--div-17-line) 0 0) 0 0/100% 3px no-repeat,linear-gradient(var(--div-17-line) 0 0) 0 100%/100% 1px no-repeat;
}

.div-17__oxford--close {
  background: linear-gradient(var(--div-17-line) 0 0) 0 0/100% 1px no-repeat,linear-gradient(var(--div-17-line) 0 0) 0 100%/100% 3px no-repeat;
  margin-block: 26px;
}

.div-17__title {
  font-size: clamp(30px,5.6vw,56px);
  line-height: 1.06;
  letter-spacing: -.022em;
  font-weight: 400;
  margin-bottom: 18px;
  text-wrap: balance;
}

.div-17__body {
  font-size: clamp(16px,2vw,19px);
  line-height: 1.68;
  text-wrap: pretty;
}

.div-17__double {
  border: 0;
  border-top: 3px double var(--div-17-line);
  margin-block: 28px;
}

.div-17__cap {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--div-17-mut);
}

.div-17__inset {
  border: 0;
  height: 5px;
  margin-block: 26px 20px;
  background: linear-gradient(var(--div-17-line) 0 0) 0 0/100% 2px no-repeat,linear-gradient(var(--div-17-acc) 0 0) 0 100%/56% 1px no-repeat;
}

.div-17__chip {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-17-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.21 0.014 265/.18);
  border-radius: 99px;
}
```
