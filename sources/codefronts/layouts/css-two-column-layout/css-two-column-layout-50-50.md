---
source: "codefronts"
url: "https://codefronts.com/layouts/css-two-column-layout/css-two-column-layout-50-50/"
title: "CSS Two Column Layout 50 50"
section: "layouts"
category: "css-two-column-layout"
category_name: "CSS Two-Column Layouts"
description: "A perfect 50 50 split layout with repeat(2, 1fr) — two equal halves meeting at a crisp centre seam, styled as a comparison landing (\"Design\" vs \"Engineer\")…"
has_js: "false"
---

Here's a working CSS Two-Column Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Two Column Layout 50 50
Source: https://codefronts.com/layouts/css-two-column-layout/css-two-column-layout-50-50/

A perfect 50 50 split layout with repeat(2, 1fr) — two equal halves meeting at a crisp centre seam, styled as a comparison landing ("Design" vs "Engineer") with mirrored panels, contrasting themes and hover states. The go-to pattern for comparisons, dual CTAs and split cards.
## HTML
```html
<section class="tcl-05" aria-label="50 50 split two column layout demo">
  <div class="tcl-05__split">
    <a class="tcl-05__half tcl-05__half--light" href="#design">
      <span class="tcl-05__num">50%</span>
      <h2>Design</h2>
      <p>Tokens, type scales and motion specs — explore the visual system behind the product.</p>
      <span class="tcl-05__go">Explore design →</span>
    </a>
    <span class="tcl-05__seam" aria-hidden="true">repeat(2, 1fr)</span>
    <a class="tcl-05__half tcl-05__half--dark" href="#engineering">
      <span class="tcl-05__num">50%</span>
      <h2>Engineer</h2>
      <p>Components, APIs and performance budgets — see how the system ships to production.</p>
      <span class="tcl-05__go">Explore engineering →</span>
    </a>
  </div>
</section>
```
## CSS
```css
.tcl-05,
.tcl-05 *,
.tcl-05 *::before,
.tcl-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tcl-05 {
  width: 100%;
  min-height: 100vh;
  --warm: oklch(0.68 0.15 60);
  --cool: oklch(0.68 0.14 250);
  background: linear-gradient(90deg,oklch(0.96 0.03 60) 50%,oklch(0.96 0.03 250) 50%);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.tcl-05__split {
  position: relative;
  display: grid;
  grid-template-columns: repeat(2,1fr);
  min-height: 460px;
}

.tcl-05__half {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 14px;
  padding: clamp(28px,5vw,64px);
  text-decoration: none;
  overflow: hidden;
  transition: transform .3s cubic-bezier(.2,.9,.2,1);
}

.tcl-05__half h2 {
  font-size: clamp(30px,4.5vw,52px);
  letter-spacing: -.03em;
  line-height: 1;
}

.tcl-05__half p {
  font-size: 14.5px;
  line-height: 1.6;
  max-width: 36ch;
  text-wrap: pretty;
}

.tcl-05__num {
  font: 700 clamp(64px,9vw,120px)/1 inherit;
  letter-spacing: -.05em;
  opacity: .1;
  position: absolute;
  top: 12px;
  right: 20px;
  pointer-events: none;
}

.tcl-05__go {
  font: 600 14px/1 inherit;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: 6px;
  transition: gap .2s;
}

.tcl-05__half:hover .tcl-05__go {
  gap: 12px;
}

.tcl-05__half:hover {
  transform: translateY(-4px);
}

.tcl-05__half:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: -6px;
}

.tcl-05__half--light {
  background: linear-gradient(160deg,oklch(0.96 0.02 70),oklch(0.9 0.06 60));
  color: oklch(0.3 0.06 50);
}

.tcl-05__half--light .tcl-05__go {
  color: oklch(0.5 0.14 45);
}

.tcl-05__half--dark {
  background: linear-gradient(200deg,oklch(0.28 0.05 260),oklch(0.2 0.04 265));
  color: oklch(0.93 0.02 250);
}

.tcl-05__half--dark .tcl-05__go {
  color: var(--cool);
}

.tcl-05__seam {
  position: absolute;
  left: 50%;
  top: 50%;
  translate: -50% -50%;
  z-index: 2;
  font: 600 11px/1 ui-monospace,monospace;
  background: #fff;
  color: oklch(0.35 0.03 260);
  border: 1px solid oklch(0.85 0.02 260);
  border-radius: 99px;
  padding: 8px 14px;
  box-shadow: 0 8px 20px -8px rgba(0,0,0,.35);
  pointer-events: none;
  white-space: nowrap;
}

@media (max-width: 700px) {
  .tcl-05__split {
    grid-template-columns: 1fr;
  }

  .tcl-05__half {
    min-height: 230px;
  }

  .tcl-05__seam {
    top: 50%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tcl-05__half {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — repeat(2,1fr) makes two mathematically equal tracks; the seam badge is absolutely positioned at left:50%. */
```
