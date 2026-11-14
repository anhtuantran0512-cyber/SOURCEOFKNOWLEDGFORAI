---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/classic-mark/"
title: "Classic Left Border CSS Blockquote Snippet"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "The canonical snippet — 4px solid left border, light wash, italic serif — that every CMS, CMS theme and CSS course reaches for first, written the way it…"
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Classic Left Border CSS Blockquote Snippet
Source: https://codefronts.com/snippets/css-blockquotes/classic-mark/

The canonical snippet — 4px solid left border, light wash, italic serif — that every CMS, CMS theme and CSS course reaches for first, written the way it should be written in 2026: tokens for every value, a wash derived with color-mix() instead of a hand-picked gray, spec-correct cite placement, and a smart-quotes bonus using the CSS quotes property so nested quotes get language-correct marks automatically. This is the one to teach from: every other demo in the collection is a mutation of these ten lines.
## HTML
```html
<section class="bq-07" aria-label="Classic left border blockquote demo">
  <div class="bq-07__stage">
    <article class="bq-07__article">
      <h1>The ten lines everyone starts with</h1>
      <p>Ask a room of developers to style a quote and most will type the same thing from muscle memory. As one CSS textbook puts it:</p>
      <figure class="bq-07__fig">
        <blockquote class="bq-07__quote">
          <p>The left-border blockquote persists because it solves the real problem — <q>where does the quote end?</q> — with one line of CSS and no ambiguity.</p>
        </blockquote>
        <figcaption class="bq-07__cap">Sarah Drasner, <cite>Notes on Modern CSS</cite></figcaption>
      </figure>
      <p>Note the nested <em>inner quote</em> above: it got single marks automatically. That's the <code>quotes</code> property tracking depth — no hard-coded characters anywhere.</p>
    </article>
    <p class="bq-07__chip" aria-hidden="true">quotes · open-quote/close-quote · color-mix() wash</p>
  </div>
</section>
```
## CSS
```css
.bq-07,
.bq-07 *,
.bq-07 *::before,
.bq-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.98 0.005 240);
  --ink: oklch(0.26 0.015 250);
  --quiet: oklch(0.44 0.015 250);
  --mut: oklch(0.55 0.015 250);
  --rule: oklch(0.62 0.1 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.bq-07__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(20px,5vw,56px);
  background: var(--bg);
  overflow-y: auto;
}

.bq-07__article {
  max-width: 60ch;
  font-size: 16px;
  line-height: 1.7;
}

.bq-07__article h1 {
  font-size: clamp(22px,3vw,30px);
  letter-spacing: -.02em;
  margin-bottom: 14px;
  text-wrap: balance;
}

.bq-07__article>p {
  color: var(--quiet);
  text-wrap: pretty;
}

.bq-07__article>p+p,
.bq-07__fig+p {
  margin-top: 14px;
}

.bq-07__article code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .86em;
  background: oklch(0.93 0.01 250);
  padding: 1.5px 6px;
  border-radius: 5px;
}

.bq-07__fig {
  margin-block: 1.5em;
}

.bq-07__quote {
  border-left: 4px solid var(--rule);
  background: color-mix(in oklch,var(--rule) 10%,transparent);
  padding: 14px 20px;
  border-radius: 0 10px 10px 0;
  font-family: Georgia,'Times New Roman',serif;
  font-style: italic;
  quotes: '\201C' '\201D' '\2018' '\2019';
}

.bq-07__quote p {
  font-size: 1.05em;
  line-height: 1.65;
  color: var(--quiet);
}

.bq-07__quote p::before {
  content: open-quote;
}

.bq-07__quote p::after {
  content: close-quote;
}

.bq-07__quote q {
  quotes: inherit;
  font-weight: 600;
}

.bq-07__cap {
  margin-top: 8px;
  padding-left: 24px;
  font-size: 13px;
  color: var(--mut);
}

.bq-07__cap cite {
  font-style: italic;
}

.bq-07__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid oklch(0 0 0/.1);
  border-radius: 99px;
  background: oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .bq-07 * {
    transition-duration: .01ms !important;
  }
}
```
