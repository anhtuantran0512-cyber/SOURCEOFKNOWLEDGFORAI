---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/css-blockquote-with-large-decorative-quotation-marks/"
title: "CSS Blockquote with Large Decorative Quotation Marks"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "The single most-searched blockquote treatment: an editorial serif quote crowned by a giant decorative opening mark."
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Blockquote with Large Decorative Quotation Marks
Source: https://codefronts.com/snippets/css-blockquotes/css-blockquote-with-large-decorative-quotation-marks/

The single most-searched blockquote treatment: an editorial serif quote crowned by a giant decorative opening mark. The glyph is a ::before pseudo-element — zero extra markup, invisible to screen readers — drawn at 9× body size in a lighter tint, tucked behind the first line with a negative margin so it decorates rather than displaces. Attribution sits in a <figcaption> outside the <blockquote> (the spec-correct pattern almost every tutorial gets wrong), and text-wrap: balance keeps the ragged edge even at every width.
## HTML
```html
<section class="bq-01" aria-label="Large decorative quotation marks blockquote demo">
  <div class="bq-01__stage">
    <figure class="bq-01__quote">
      <blockquote>
        <p>Typography is the craft of endowing human language with a durable visual form. It is what turns a wall of words into a voice.</p>
      </blockquote>
      <figcaption>
        <span class="bq-01__rule" aria-hidden="true"></span>
        <span><strong>Robert Bringhurst</strong> · The Elements of Typographic Style</span>
      </figcaption>
    </figure>
    <p class="bq-01__chip" aria-hidden="true">::before &nbsp;·&nbsp; content:'\201C' &nbsp;·&nbsp; color-mix()</p>
  </div>
</section>
```
## CSS
```css
.bq-01,
.bq-01 *,
.bq-01 *::before,
.bq-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.97 0.008 85);
  --ink: oklch(0.24 0.02 60);
  --mut: oklch(0.52 0.02 60);
  --acc: oklch(0.55 0.13 40);
  font-family: Georgia,'Times New Roman',serif;
  color: var(--ink);
}

.bq-01__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(120% 90% at 50% 0%,oklch(0.99 0.005 85),var(--bg));
  overflow-y: auto;
}

.bq-01__quote {
  max-width: 62ch;
}

.bq-01__quote blockquote::before {
  content: '\201C';
  display: block;
  height: .62em;
  font-size: 8.5em;
  line-height: 1;
  font-family: Georgia,serif;
  color: color-mix(in oklch,var(--acc) 32%,transparent);
}

.bq-01__quote blockquote {
  margin: -.08em 0 0 -.06em;
}

.bq-01__quote p {
  font-size: clamp(22px,3.4vw,34px);
  line-height: 1.42;
  letter-spacing: -.01em;
  text-wrap: balance;
  font-style: italic;
}

.bq-01__quote figcaption {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-top: 26px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-style: normal;
  font-size: 14px;
  color: var(--mut);
}

.bq-01__quote figcaption strong {
  color: var(--ink);
  font-weight: 650;
}

.bq-01__rule {
  width: 44px;
  height: 2px;
  background: var(--acc);
  flex: none;
}

.bq-01__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid color-mix(in oklch,var(--ink) 14%,transparent);
  border-radius: 99px;
  background: oklch(1 0 0/.55);
}

@media (prefers-reduced-motion: reduce) {
  .bq-01 * {
    transition-duration: .01ms !important;
  }
}
```
