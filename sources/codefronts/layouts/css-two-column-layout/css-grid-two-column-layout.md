---
source: "codefronts"
url: "https://codefronts.com/layouts/css-two-column-layout/css-grid-two-column-layout/"
title: "CSS Grid Two Column Layout"
section: "layouts"
category: "css-two-column-layout"
category_name: "CSS Two-Column Layouts"
description: "A native CSS Grid two column layout using grid-template-columns: 1fr 1fr with a clean gap — the 2D-correct way to pair text with a visual."
has_js: "false"
---

Here's a working CSS Two-Column Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Grid Two Column Layout
Source: https://codefronts.com/layouts/css-two-column-layout/css-grid-two-column-layout/

A native CSS Grid two column layout using grid-template-columns: 1fr 1fr with a clean gap — the 2D-correct way to pair text with a visual. This demo aligns a feature story against a pure-CSS product mock, shows fr-unit sizing, place-content alignment and a one-line responsive collapse.
## HTML
```html
<section class="tcl-02" aria-label="CSS Grid two column layout demo">
  <div class="tcl-02__grid">
    <div class="tcl-02__copy">
      <span class="tcl-02__eyebrow">grid-template-columns: 1fr 1fr</span>
      <h2 class="tcl-02__title">Two tracks. One gap. Zero hacks.</h2>
      <p class="tcl-02__lede">Fraction units divide the row after the gutter is reserved, so a grid two column layout can never overflow the way percentage floats did. Alignment is one property, not a pile of wrappers.</p>
      <ul class="tcl-02__points">
        <li><b>fr units</b> — free-space sizing that respects the gap</li>
        <li><b>align-items: center</b> — vertical centring in one line</li>
        <li><b>order</b> — visual reorder without touching the DOM</li>
      </ul>
      <a class="tcl-02__cta" href="#grid-guide">Read the grid guide</a>
    </div>
    <figure class="tcl-02__visual" role="img" aria-label="Stylized editor window with a two-column grid overlay">
      <div class="tcl-02__win">
        <div class="tcl-02__winbar"><i></i><i></i><i></i><span>layout.css</span></div>
        <div class="tcl-02__cols"><div class="tcl-02__col"><b>1fr</b></div><div class="tcl-02__gaptag">gap</div><div class="tcl-02__col"><b>1fr</b></div></div>
        <code class="tcl-02__code">display: grid;<br>grid-template-columns: 1fr 1fr;<br>gap: 2rem;</code>
      </div>
    </figure>
  </div>
</section>
```
## CSS
```css
.tcl-02,
.tcl-02 *,
.tcl-02 *::before,
.tcl-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tcl-02 {
  width: 100%;
  min-height: 100vh;
  --brand: oklch(0.72 0.14 175);
  --bg: oklch(0.22 0.02 220);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: oklch(0.95 0.01 220);
  background: radial-gradient(110% 130% at 85% -10%,color-mix(in oklab,var(--brand) 22%,transparent),transparent 55%),var(--bg);
  padding: clamp(28px,5vw,64px);
}

.tcl-02__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: clamp(28px,5vw,64px);
  align-items: center;
  max-width: 1040px;
  margin-inline: auto;
}

.tcl-02__copy {
  display: grid;
  gap: 18px;
  justify-items: start;
  min-width: 0;
}

.tcl-02__eyebrow {
  font: 600 11px/1 ui-monospace,monospace;
  letter-spacing: .08em;
  color: var(--brand);
  border: 1px solid color-mix(in oklab,var(--brand) 45%,transparent);
  border-radius: 99px;
  padding: 6px 11px;
}

.tcl-02__title {
  font-size: clamp(26px,3.4vw,38px);
  line-height: 1.12;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.tcl-02__lede {
  font-size: 15px;
  line-height: 1.65;
  color: oklch(0.78 0.02 220);
  text-wrap: pretty;
}

.tcl-02__points {
  list-style: none;
  display: grid;
  gap: 10px;
  font-size: 13.5px;
  color: oklch(0.83 0.02 220);
}

.tcl-02__points li {
  display: flex;
  gap: 10px;
  align-items: baseline;
}

.tcl-02__points li::before {
  content: "";
  flex: none;
  width: 7px;
  height: 7px;
  border-radius: 2px;
  background: var(--brand);
  transform: translateY(-1px) rotate(45deg);
}

.tcl-02__points b {
  color: #fff;
}

.tcl-02__cta {
  font: 600 14px/1 inherit;
  color: var(--bg);
  background: var(--brand);
  text-decoration: none;
  padding: 13px 22px;
  border-radius: 10px;
  transition: transform .2s,box-shadow .2s;
}

.tcl-02__cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 24px -12px var(--brand);
}

.tcl-02__cta:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.tcl-02__visual {
  min-width: 0;
}

.tcl-02__win {
  background: oklch(0.27 0.02 220);
  border: 1px solid oklch(0.36 0.02 220);
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 30px 60px -30px rgba(0,0,0,.7);
}

.tcl-02__winbar {
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 11px 14px;
  border-bottom: 1px solid oklch(0.34 0.02 220);
}

.tcl-02__winbar i {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: oklch(0.45 0.03 220);
}

.tcl-02__winbar span {
  margin-left: auto;
  font: 500 11px/1 ui-monospace,monospace;
  color: oklch(0.65 0.02 220);
}

.tcl-02__cols {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: stretch;
  gap: 0;
  padding: 18px 18px 6px;
}

.tcl-02__col {
  display: grid;
  place-items: center;
  height: 110px;
  border: 1.5px dashed color-mix(in oklab,var(--brand) 60%,transparent);
  border-radius: 10px;
  background: color-mix(in oklab,var(--brand) 10%,transparent);
}

.tcl-02__col b {
  font: 700 15px/1 ui-monospace,monospace;
  color: var(--brand);
}

.tcl-02__gaptag {
  align-self: center;
  font: 600 10px/1 ui-monospace,monospace;
  color: oklch(0.7 0.02 220);
  writing-mode: vertical-rl;
  padding: 8px 6px;
}

.tcl-02__code {
  display: block;
  font: 500 12.5px/1.7 ui-monospace,monospace;
  color: oklch(0.8 0.03 175);
  padding: 12px 18px 18px;
}

@media (max-width: 760px) {
  .tcl-02__grid {
    grid-template-columns: 1fr;
  }

  .tcl-02__visual {
    order: 1;
  }
}
```

## JavaScript
```js
/* No JavaScript — grid-template-columns:1fr 1fr + gap builds the layout; one media query collapses it to a single track. */
```
