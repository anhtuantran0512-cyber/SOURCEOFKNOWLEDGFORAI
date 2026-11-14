---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/vertical-rail/"
title: "Thick Vertical Accent Rail CSS Blockquote"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "The left border grown up into architecture: a 10px rail carrying a vertical gradient, drawn with border-image so a real border can hold a gradient at all —…"
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Thick Vertical Accent Rail CSS Blockquote
Source: https://codefronts.com/snippets/css-blockquotes/vertical-rail/

The left border grown up into architecture: a 10px rail carrying a vertical gradient, drawn with border-image so a real border can hold a gradient at all — plus a grid layout where the rail is its own column, letting a label sit rotated inside it writing-mode: vertical-rl style. Where demo 05 whispers, this one declares: statement quotes for reports, annual reviews and manifesto pages, with the rail's gradient tuned so its midpoint aligns with the quote's optical center.
## HTML
```html
<section class="bq-13" aria-label="Thick vertical accent rail blockquote demo">
  <div class="bq-13__stage">
    <figure class="bq-13__grid">
      <div class="bq-13__rail" aria-hidden="true"><span>FIELD NOTES — VOL 7</span></div>
      <div class="bq-13__content">
        <blockquote>
          <p>We didn't set out to build infrastructure. We set out to answer one support ticket properly, and infrastructure is what answering it properly turned out to require.</p>
        </blockquote>
        <figcaption class="bq-13__by"><strong>Yusuf Adeyemi</strong> · Founding Engineer, Cachet</figcaption>
      </div>
    </figure>
    <p class="bq-13__chip" aria-hidden="true">border-image gradient rail · grid-column rail · writing-mode:vertical-rl</p>
  </div>
</section>
```
## CSS
```css
.bq-13,
.bq-13 *,
.bq-13 *::before,
.bq-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.2 0.015 260);
  --ink: oklch(0.96 0.008 250);
  --mut: oklch(0.66 0.02 255);
  --a: oklch(0.78 0.14 85);
  --b: oklch(0.65 0.19 30);
  --c: oklch(0.6 0.2 330);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.bq-13__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 28px;
  padding: clamp(20px,5vw,56px);
  background: linear-gradient(200deg,oklch(0.24 0.02 270),var(--bg) 60%);
  overflow-y: auto;
}

.bq-13__grid {
  display: grid;
  grid-template-columns: 14px 1fr;
  gap: 26px;
  width: min(100%,620px);
}

.bq-13__rail {
  display: grid;
  place-items: end center;
  background: linear-gradient(180deg,var(--a),var(--b) 55%,var(--c));
  border-radius: 0;
  padding-block: 14px;
}

.bq-13__rail span {
  writing-mode: vertical-rl;
  rotate: 180deg;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .22em;
  color: oklch(0.15 0.02 260/.85);
  white-space: nowrap;
}

.bq-13__content blockquote p {
  font-size: clamp(20px,2.8vw,28px);
  line-height: 1.44;
  font-weight: 650;
  letter-spacing: -.018em;
  text-wrap: pretty;
}

.bq-13__by {
  margin-top: 18px;
  font-size: 14px;
  color: var(--mut);
}

.bq-13__by strong {
  color: var(--ink);
  font-weight: 650;
  background: linear-gradient(90deg,var(--a),var(--b));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.bq-13__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .bq-13 * {
    transition-duration: .01ms !important;
  }
}
```
