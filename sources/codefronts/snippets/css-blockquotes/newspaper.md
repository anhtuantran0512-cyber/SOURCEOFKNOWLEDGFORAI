---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/newspaper/"
title: "Multi-Column Newspaper Editorial Blockquote"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "A broadsheet page set with CSS multi-column layout — the one layout module built for exactly this and used by almost nobody: column-count flows the story…"
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Column Newspaper Editorial Blockquote
Source: https://codefronts.com/snippets/css-blockquotes/newspaper/

A broadsheet page set with CSS multi-column layout — the one layout module built for exactly this and used by almost nobody: column-count flows the story into three columns, column-rule draws the hairlines between them, hyphens: auto justifies like typeset copy, and the centerpiece quote uses column-span: all to break out across every column mid-flow, the move newspapers have made since the linotype era. Drop caps via ::first-letter, small-caps standfirst, and a masthead complete the broadsheet grammar.
## HTML
```html
<section class="bq-20" aria-label="Multi-column newspaper editorial blockquote demo" lang="en">
  <div class="bq-20__stage">
    <article class="bq-20__paper">
      <header class="bq-20__masthead">
        <p class="bq-20__ears">Vol. CXIV · No. 218</p>
        <p class="bq-20__title">The Morning Ledger</p>
        <p class="bq-20__ears">Tuesday, August 5, 2026</p>
      </header>
      <h1 class="bq-20__head">The quiet return of the printed page's best ideas</h1>
      <p class="bq-20__standfirst">Web typography spent twenty years reinventing what compositors solved by hand — now the CSS to do it properly ships in every browser</p>
      <div class="bq-20__body">
        <p>For most of the web's life, the column was a metaphor rather than a measurement. Text ran the full width of whatever glass it landed on, and the craft of the compositor — the measured line, the balanced page, the rule between columns — survived only in PDFs and nostalgia.</p>
        <p>The tools arrived quietly. Multi-column layout shipped, then column rules, then spanning elements; hyphenation dictionaries came to every major engine. What did not arrive was the habit of using them.</p>
        <blockquote class="bq-20__crossing">
          <p>“A newspaper page is an argument about attention — every rule, gutter and crossing quote tells the eye what matters next.”</p>
          <footer>— Edda Marston, <cite>The Composed Page</cite> (2024)</footer>
        </blockquote>
        <p>Designers who grew up on component libraries often meet these properties with suspicion, as if flowing text were a legacy behavior. Yet the reading research is stubborn: shorter measures read faster, and rules between columns cut skip-backs by a measurable fraction.</p>
        <p>The crossing quote above is one property doing what frameworks cannot: interrupting a live text flow, borrowing its full width, and handing the reader back to the exact sentence they left. The linotype operators had a word for it. They called it Tuesday.</p>
      </div>
    </article>
    <p class="bq-20__chip" aria-hidden="true">columns:3 · column-rule · column-span:all · hyphens:auto</p>
  </div>
</section>
```
## CSS
```css
.bq-20,
.bq-20 *,
.bq-20 *::before,
.bq-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-20 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --paper: oklch(0.97 0.008 90);
  --ink: oklch(0.22 0.01 70);
  --mut: oklch(0.46 0.012 70);
  --hair: oklch(0.75 0.015 80);
  --acc: oklch(0.45 0.1 30);
  font-family: Georgia,'Times New Roman',serif;
  color: var(--ink);
}

.bq-20__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 22px;
  padding: clamp(16px,4vw,48px);
  background: oklch(0.88 0.015 85);
  overflow-y: auto;
}

.bq-20__paper {
  width: min(100%,860px);
  background: var(--paper);
  padding: clamp(22px,4vw,44px);
  box-shadow: 0 2px 4px oklch(0.3 0.02 80/.12),0 18px 44px oklch(0.3 0.02 80/.18);
  container-type: inline-size;
}

.bq-20__masthead {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  border-bottom: 3px double var(--ink);
  padding-bottom: 10px;
}

.bq-20__title {
  font-size: clamp(20px,3.4cqi,30px);
  font-weight: 800;
  letter-spacing: .02em;
  font-variant: small-caps;
}

.bq-20__ears {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 10px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--mut);
  white-space: nowrap;
}

.bq-20__head {
  font-size: clamp(24px,4.4cqi,40px);
  line-height: 1.08;
  letter-spacing: -.015em;
  font-weight: 750;
  text-wrap: balance;
  margin-top: 20px;
}

.bq-20__standfirst {
  margin-top: 10px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--hair);
  font-size: 14.5px;
  font-style: italic;
  color: var(--mut);
  text-wrap: pretty;
}

.bq-20__body {
  margin-top: 18px;
  columns: 3;
  column-gap: 2.2em;
  column-rule: 1px solid var(--hair);
  font-size: 13.5px;
  line-height: 1.62;
  hyphens: auto;
  text-align: justify;
}

.bq-20__body>p+p {
  margin-top: .7em;
}

.bq-20__body>p:first-child::first-letter {
  float: left;
  font-size: 3.1em;
  line-height: .82;
  padding: .06em .12em 0 0;
  font-weight: 700;
  color: var(--acc);
}

.bq-20__crossing {
  column-span: all;
  margin-block: 1em;
  padding-block: .85em;
  border-block: 2px solid var(--ink);
  text-align: center;
}

.bq-20__crossing p {
  font-size: clamp(17px,2.6cqi,23px);
  line-height: 1.4;
  font-weight: 600;
  font-style: italic;
  letter-spacing: -.01em;
  text-wrap: balance;
  hyphens: none;
}

.bq-20__crossing footer {
  margin-top: 8px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 11px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--mut);
  font-style: normal;
}

@container (width < 680px) {
  .bq-20__body {
    columns: 2;
  }
}

@container (width < 460px) {
  .bq-20__body {
    columns: 1;
    column-rule: none;
    text-align: left;
    hyphens: none;
  }
}

.bq-20__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  background: var(--paper);
}

@media (prefers-reduced-motion: reduce) {
  .bq-20 * {
    transition-duration: .01ms !important;
  }
}
```
