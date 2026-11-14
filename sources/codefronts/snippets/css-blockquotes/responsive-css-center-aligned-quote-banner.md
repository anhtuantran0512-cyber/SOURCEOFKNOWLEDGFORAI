---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/responsive-css-center-aligned-quote-banner/"
title: "Responsive CSS Center-Aligned Quote Banner"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "The full-width statement banner that anchors landing pages and section breaks: a quote centered on both axes with grid place-content, sized by clamp() so it…"
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive CSS Center-Aligned Quote Banner
Source: https://codefronts.com/snippets/css-blockquotes/responsive-css-center-aligned-quote-banner/

The full-width statement banner that anchors landing pages and section breaks: a quote centered on both axes with grid place-content, sized by clamp() so it is fluid between 28px and 56px without a single media query, and balanced with text-wrap: balance so no lonely word ever wraps alone. Flanking hairline rules are drawn by the grid itself (two 1px column tracks), and a subtle radial spotlight lifts the center of the banner — the whole composition is 100% CSS layout primitives, no absolute positioning anywhere.
## HTML
```html
<section class="bq-04" aria-label="Center aligned quote banner demo">
  <div class="bq-04__stage">
    <figure class="bq-04__banner">
      <p class="bq-04__kicker">From the keynote</p>
      <blockquote>
        <p>Make the easy path and the right path the same path.</p>
      </blockquote>
      <figcaption class="bq-04__by">
        <span class="bq-04__line" aria-hidden="true"></span>
        <span><strong>Amara Chen</strong> — Head of Platform, Fieldday</span>
        <span class="bq-04__line" aria-hidden="true"></span>
      </figcaption>
    </figure>
    <p class="bq-04__chip" aria-hidden="true">place-content:center · clamp() · text-wrap:balance</p>
  </div>
</section>
```
## CSS
```css
.bq-04,
.bq-04 *,
.bq-04 *::before,
.bq-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-04 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.17 0.02 285);
  --ink: oklch(0.96 0.01 280);
  --mut: oklch(0.68 0.03 285);
  --acc: oklch(0.78 0.12 330);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.bq-04__stage {
  position: relative;
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: 30px;
  padding: clamp(20px,5vw,56px);
  text-align: center;
  background: radial-gradient(60% 45% at 50% 42%,oklch(0.28 0.06 320/.55),transparent 70%),var(--bg);
  overflow-y: auto;
}

.bq-04__banner {
  display: grid;
  justify-items: center;
  gap: 22px;
  max-width: 900px;
}

.bq-04__kicker {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: var(--acc);
}

.bq-04__banner blockquote p {
  font-size: clamp(28px,2.2vw + 16px,56px);
  line-height: 1.18;
  font-weight: 750;
  letter-spacing: -.025em;
  text-wrap: balance;
  max-width: 22ch;
}

.bq-04__by {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 18px;
  width: min(100%,560px);
  font-size: 14px;
  color: var(--mut);
}

.bq-04__by strong {
  color: var(--ink);
  font-weight: 650;
}

.bq-04__line {
  height: 1px;
  background: color-mix(in oklch,var(--ink) 22%,transparent);
}

.bq-04__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid color-mix(in oklch,var(--ink) 16%,transparent);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .bq-04 * {
    transition-duration: .01ms !important;
  }
}
```
