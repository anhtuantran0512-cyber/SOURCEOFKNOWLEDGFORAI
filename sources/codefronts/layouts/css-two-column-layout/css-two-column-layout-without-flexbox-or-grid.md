---
source: "codefronts"
url: "https://codefronts.com/layouts/css-two-column-layout/css-two-column-layout-without-flexbox-or-grid/"
title: "CSS Two Column Layout Without Flexbox or Grid"
section: "layouts"
category: "css-two-column-layout"
category_name: "CSS Two-Column Layouts"
description: "Two columns with zero flexbox and zero grid: display: inline-block at width: 50% with box-sizing: border-box, the font-size: 0 whitespace fix, and…"
has_js: "false"
---

Here's a working CSS Two-Column Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Two Column Layout Without Flexbox or Grid
Source: https://codefronts.com/layouts/css-two-column-layout/css-two-column-layout-without-flexbox-or-grid/

Two columns with zero flexbox and zero grid: display: inline-block at width: 50% with box-sizing: border-box, the font-size: 0 whitespace fix, and vertical-align: top — the bulletproof pattern for strict email clients, ultra-light pages and understanding how layout worked before 2015. Includes the display: table-cell alternative in the notes.
## HTML
```html
<section class="tcl-16" aria-label="Two column layout without flexbox or grid demo">
  <div class="tcl-16__card">
    <header class="tcl-16__head">
      <b>Dispatch №9</b>
      <span>A newsletter layout that renders everywhere — even with CSS half-off</span>
    </header>
    <div class="tcl-16__cols"><div class="tcl-16__col tcl-16__col--main">
        <span class="tcl-16__chip">inline-block · 50% · border-box</span>
        <h2>No flex. No grid. Still two columns.</h2>
        <p>These columns are plain <code>inline-block</code> boxes. The parent’s <code>font-size: 0</code> removes the whitespace gap between them, and <code>vertical-align: top</code> keeps them level — the same three lines powering millions of HTML emails right now.</p>
        <p>It isn’t nostalgia. Outlook, older webmail and CSS-sanitising clients still strip or ignore modern layout, and this pattern is what survives the strip.</p>
      </div><div class="tcl-16__col tcl-16__col--side">
        <div class="tcl-16__box">
          <h3>Why it still matters</h3>
          <ul>
            <li>HTML email templates</li>
            <li>Ultra-light landing pages</li>
            <li>Legacy enterprise browsers</li>
            <li>Learning layout fundamentals</li>
          </ul>
          <a class="tcl-16__btn" href="#archive">Read the archive</a>
        </div>
      </div></div>
  </div>
</section>
```
## CSS
```css
.tcl-16,
.tcl-16 *,
.tcl-16 *::before,
.tcl-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tcl-16 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.27 0.03 280);
  --accent: oklch(0.55 0.16 280);
  font-family: Verdana,Geneva,'Segoe UI',sans-serif;
  color: var(--ink);
  background: oklch(0.94 0.015 280);
  padding: clamp(20px,3.5vw,48px);
}

.tcl-16__card {
  max-width: 840px;
  margin-inline: auto;
  background: #fff;
  border: 1px solid oklch(0.86 0.02 280);
  border-radius: 4px;
  overflow: hidden;
  box-shadow: 0 14px 30px -24px oklch(0.35 0.08 280/.8);
}

.tcl-16__head {
  display: block;
  background: var(--ink);
  color: #fff;
  padding: 18px 26px;
}

.tcl-16__head b {
  display: block;
  font-size: 19px;
  letter-spacing: .02em;
}

.tcl-16__head span {
  display: block;
  font-size: 12px;
  color: oklch(0.78 0.04 280);
  margin-top: 4px;
}
/* the whole technique: */

.tcl-16__cols {
  font-size: 0;
}
/* kill inter-tag whitespace */

.tcl-16__col {
  display: inline-block;
  width: 50%;
  vertical-align: top;
  font-size: 14px;
}
/* restore size */

.tcl-16__col--main {
  padding: 26px 22px 26px 26px;
}

.tcl-16__col--side {
  padding: 26px 26px 26px 8px;
}

.tcl-16__chip {
  display: inline-block;
  font: 700 10px/1 'Courier New',monospace;
  letter-spacing: .04em;
  color: var(--accent);
  border: 1px dashed color-mix(in oklab,var(--accent) 55%,transparent);
  padding: 5px 8px;
  margin-bottom: 14px;
}

.tcl-16__col h2 {
  font-size: clamp(18px,2.4vw,24px);
  line-height: 1.25;
  letter-spacing: -.01em;
  margin-bottom: 12px;
  text-wrap: balance;
}

.tcl-16__col p {
  font-size: 13.5px;
  line-height: 1.7;
  margin-bottom: 12px;
  color: color-mix(in oklab,var(--ink) 80%,transparent);
  text-wrap: pretty;
}

.tcl-16__col code {
  font: 700 12px 'Courier New',monospace;
  background: color-mix(in oklab,var(--accent) 10%,transparent);
  padding: 1px 5px;
}

.tcl-16__box {
  background: oklch(0.96 0.012 280);
  border: 1px solid oklch(0.88 0.02 280);
  border-radius: 4px;
  padding: 18px;
}

.tcl-16__box h3 {
  font-size: 13px;
  letter-spacing: .05em;
  text-transform: uppercase;
  margin-bottom: 10px;
}

.tcl-16__box ul {
  list-style: none;
  margin-bottom: 14px;
}

.tcl-16__box li {
  font-size: 12.5px;
  line-height: 1.5;
  padding: 6px 0 6px 14px;
  position: relative;
  border-bottom: 1px dotted oklch(0.86 0.02 280);
}

.tcl-16__box li::before {
  content: "›";
  position: absolute;
  left: 0;
  color: var(--accent);
  font-weight: 700;
}

.tcl-16__btn {
  display: block;
  text-align: center;
  font-size: 13px;
  font-weight: 700;
  color: #fff;
  background: var(--accent);
  text-decoration: none;
  padding: 12px;
  border-radius: 3px;
}

.tcl-16__btn:hover {
  background: oklch(0.48 0.16 280);
}

.tcl-16__btn:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 2px;
}

@media (max-width: 600px) {
  .tcl-16__col {
    width: 100%;
  }

  .tcl-16__col--side {
    padding: 0 26px 26px;
  }
}
```

## JavaScript
```js
/* No JavaScript — display:inline-block at width:50% with box-sizing:border-box; parent font-size:0 removes the whitespace gap and vertical-align:top levels the columns. */
```
