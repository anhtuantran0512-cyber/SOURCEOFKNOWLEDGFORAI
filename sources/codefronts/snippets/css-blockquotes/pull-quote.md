---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/pull-quote/"
title: "Article Pull Quote CSS Design with Wrap Text"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "The magazine move: a pull quote floated into the article so body text wraps around it — with the two details that separate print-quality from blog-quality."
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Article Pull Quote CSS Design with Wrap Text
Source: https://codefronts.com/snippets/css-blockquotes/pull-quote/

The magazine move: a pull quote floated into the article so body text wraps around it — with the two details that separate print-quality from blog-quality. Semantically it's an <aside>, not a <blockquote> (a pull quote REPEATS text from the article; quoting yourself with blockquote double-announces it to screen readers). Typographically, shape-outside: margin-box plus a generous margin carves a soft channel around the float, and a top rule + oversized mark anchor the quote's own hierarchy inside the wrap.
## HTML
```html
<section class="bq-11" aria-label="Pull quote with wrapped text demo">
  <div class="bq-11__stage">
    <article class="bq-11__article">
      <p class="bq-11__kicker">The Craft Issue · Longform</p>
      <h1>What we lost when everything became a feed</h1>
      <div class="bq-11__body">
        <aside class="bq-11__pull" aria-label="Pull quote">
          <p>Pages had edges. A feed has no edges, and so it has no shape — and nothing without a shape can be finished.</p>
        </aside>
        <p>Print editors used to speak about the architecture of a page the way builders speak about load: every column carried weight, and white space was a decision someone signed off on. A reader could feel — without ever articulating it — that the page had been <em>composed</em>.</p>
        <p>Pages had edges. A feed has no edges, and so it has no shape — and nothing without a shape can be finished. The infinite scroll made publishing cheaper and reading thinner in the same gesture, and we are still doing the accounting.</p>
        <p>The designers interviewed for this piece kept returning to the same word: boundaries. Not as nostalgia, but as a craft constraint that made every inclusion mean something.</p>
      </div>
    </article>
    <p class="bq-11__chip" aria-hidden="true">float:inline-end · shape-outside · &lt;aside&gt; not &lt;blockquote&gt;</p>
  </div>
</section>
```
## CSS
```css
.bq-11,
.bq-11 *,
.bq-11 *::before,
.bq-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.975 0.006 75);
  --ink: oklch(0.24 0.015 60);
  --quiet: oklch(0.42 0.015 60);
  --mut: oklch(0.55 0.02 60);
  --acc: oklch(0.58 0.16 25);
  font-family: Georgia,'Times New Roman',serif;
  color: var(--ink);
}

.bq-11__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(20px,5vw,56px);
  background: var(--bg);
  overflow-y: auto;
}

.bq-11__article {
  width: min(100%,66ch);
  container-type: inline-size;
}

.bq-11__kicker {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--acc);
  margin-bottom: 10px;
}

.bq-11__article h1 {
  font-size: clamp(26px,3.6vw,38px);
  line-height: 1.14;
  letter-spacing: -.02em;
  font-weight: 700;
  text-wrap: balance;
  margin-bottom: 20px;
}

.bq-11__body {
  display: flow-root;
  font-size: 16px;
  line-height: 1.75;
  color: var(--quiet);
}

.bq-11__body>p+p {
  margin-top: 14px;
}

.bq-11__pull {
  float: right;
  float: inline-end;
  width: min(46%,300px);
  margin: .35em 0 .8em 1.6em;
  shape-outside: margin-box;
  border-top: 3px solid var(--acc);
  padding-top: .55em;
}

.bq-11__pull p {
  font-size: 1.45em;
  line-height: 1.3;
  font-weight: 700;
  letter-spacing: -.015em;
  color: var(--ink);
  text-wrap: pretty;
}

.bq-11__pull p::before {
  content: '\201C';
  color: var(--acc);
}

@container (width < 520px) {
  .bq-11__pull {
    float: none;
    width: 100%;
    margin: 1.2em 0;
  }
}

.bq-11__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid oklch(0 0 0/.1);
  border-radius: 99px;
  background: oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .bq-11 * {
    transition-duration: .01ms !important;
  }
}
```
