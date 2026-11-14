---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/brutalist-stamp/"
title: "Brutalist CSS Blockquote Design"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "Neo-brutalism's whole grammar in one component: 3px ink borders, a hard offset shadow with zero blur (box-shadow: 8px 8px 0), an unapologetic yellow,…"
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist CSS Blockquote Design
Source: https://codefronts.com/snippets/css-blockquotes/brutalist-stamp/

Neo-brutalism's whole grammar in one component: 3px ink borders, a hard offset shadow with zero blur (box-shadow: 8px 8px 0), an unapologetic yellow, uppercase mono labels, and no border-radius anywhere. The card presses INTO its own shadow on hover — translate(4px,4px) while the shadow shrinks to 4px — the tactile push-button move the style is famous for. A rotated attribution sticker breaks the grid just enough to prove the rawness is designed, not defaulted.
## HTML
```html
<section class="bq-08" aria-label="Brutalist blockquote demo">
  <div class="bq-08__stage">
    <figure class="bq-08__wrap">
      <div class="bq-08__card" tabindex="0">
        <p class="bq-08__label">Quote_004.txt</p>
        <blockquote>
          <p>Perfection is a lie the tools sell you. Ship the thing with the seams showing — at least everyone can see how it's made.</p>
        </blockquote>
      </div>
      <figcaption class="bq-08__sticker">— RIKO TANAKA, ZINE PUBLISHER</figcaption>
    </figure>
    <p class="bq-08__chip" aria-hidden="true">box-shadow:8px 8px 0 · translate press · radius:0</p>
  </div>
</section>
```
## CSS
```css
.bq-08,
.bq-08 *,
.bq-08 *::before,
.bq-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.93 0.02 95);
  --ink: oklch(0.2 0.01 90);
  --pop: oklch(0.9 0.18 100);
  --paper: oklch(0.99 0.005 95);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.bq-08__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 30px;
  padding: clamp(20px,5vw,56px);
  background: repeating-linear-gradient(0deg,transparent 0 23px,oklch(0.86 0.02 95) 23px 24px),var(--bg);
  overflow-y: auto;
}

.bq-08__wrap {
  position: relative;
  width: min(100%,540px);
}

.bq-08__card {
  border: 3px solid var(--ink);
  background: var(--pop);
  padding: 26px 28px 30px;
  box-shadow: 8px 8px 0 var(--ink);
  transition: translate .15s ease-out,box-shadow .15s ease-out;
  cursor: default;
}

.bq-08__card:hover,
.bq-08__card:focus-visible {
  translate: 4px 4px;
  box-shadow: 4px 4px 0 var(--ink);
}

.bq-08__card:focus-visible {
  outline: 3px dashed var(--ink);
  outline-offset: 4px;
}

.bq-08__label {
  display: inline-block;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  background: var(--ink);
  color: var(--paper);
  padding: 5px 9px;
  margin-bottom: 16px;
}

.bq-08__card blockquote p {
  font-size: clamp(19px,2.6vw,25px);
  line-height: 1.42;
  font-weight: 800;
  letter-spacing: -.015em;
  text-wrap: pretty;
}

.bq-08__sticker {
  position: absolute;
  right: -10px;
  bottom: -22px;
  rotate: -2deg;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .06em;
  background: var(--paper);
  border: 3px solid var(--ink);
  padding: 8px 12px;
  box-shadow: 5px 5px 0 var(--ink);
}

.bq-08__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  font-weight: 700;
  color: var(--ink);
  padding: 7px 13px;
  border: 2px solid var(--ink);
  background: var(--paper);
}

@media (prefers-reduced-motion: reduce) {
  .bq-08 * {
    transition-duration: .01ms !important;
  }
}
```
