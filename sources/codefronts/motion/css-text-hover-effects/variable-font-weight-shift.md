---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/variable-font-weight-shift/"
title: "Variable Font Weight Shift"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "Menu items that swell from Light 300 to ExtraBold 800 under the cursor — continuously, through every intermediate weight, because with a variable font…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Variable Font Weight Shift
Source: https://codefronts.com/motion/css-text-hover-effects/variable-font-weight-shift/

Menu items that swell from Light 300 to ExtraBold 800 under the cursor — continuously, through every intermediate weight, because with a variable font font-weight is an ANIMATABLE AXIS, not four frozen files. And the companion trick that makes it shippable: bold glyphs are wider, so each label hides a bold ghost of itself (a ::after reading data-text) that reserves the maximum width up front — the row never reflows, the classic 'menu shudder' bug solved in four lines. The section tags morph the opposite way, bold→light, as their row loses focus.
## HTML
```html
<section class="cth-20" aria-label="Variable font weight shift demo">
  <div class="cth-20__stage">
    <div class="cth-20__scene">
      <header class="cth-20__head">
        <p class="cth-20__eyebrow">Grain &amp; Gradient &mdash; issue index</p>
        <span class="cth-20__chip">wght 300 &rarr; 800, one axis</span>
      </header>
      <nav class="cth-20__menu" aria-label="Issues">
        <a class="cth-20__item" href="#cth20-top" id="cth20-top" data-text="The Typography Issue"><em>01</em><span class="cth-20__label" data-text="The Typography Issue">The Typography Issue</span></a>
        <a class="cth-20__item" href="#cth20-top" data-text="Color, Carefully"><em>02</em><span class="cth-20__label" data-text="Color, Carefully">Color, Carefully</span></a>
        <a class="cth-20__item" href="#cth20-top" data-text="Grids Against Chaos"><em>03</em><span class="cth-20__label" data-text="Grids Against Chaos">Grids Against Chaos</span></a>
        <a class="cth-20__item" href="#cth20-top" data-text="Motion With Manners"><em>04</em><span class="cth-20__label" data-text="Motion With Manners">Motion With Manners</span></a>
      </nav>
      <p class="cth-20__hint">Hover a title: every intermediate weight renders &mdash; and the row never shifts, because a hidden bold twin (<code>::after</code> + <code>attr(data-text)</code>) reserved the width on day one.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Manrope:[email protected]&display=swap');

.cth-20,
.cth-20 *,
.cth-20 *::before,
.cth-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-20 {
  --bg: oklch(0.97 0.005 60);
  --ink: oklch(0.22 0.012 50);
  --mut: oklch(0.55 0.015 55);
  --acc: oklch(0.58 0.16 40);
  --line: oklch(0.89 0.008 55);
  font-family: 'Manrope','Segoe UI',system-ui,sans-serif;
  font-synthesis-weight: none;
  color: var(--ink);
}

.cth-20__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: var(--bg);
  padding: clamp(20px,4vw,56px);
  container: cth20/inline-size;
}

.cth-20__scene {
  width: min(100%,720px);
  display: flex;
  flex-direction: column;
  gap: clamp(16px,3cqi,24px);
}

.cth-20__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  flex-wrap: wrap;
  padding-bottom: 14px;
  border-bottom: 1.5px solid var(--ink);
}

.cth-20__eyebrow {
  font-size: 12.5px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-20__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--acc);
  border: 1px solid color-mix(in oklch,var(--acc) 40%,transparent);
  border-radius: 99px;
  padding: 5px 11px;
}

.cth-20__menu {
  display: flex;
  flex-direction: column;
}

.cth-20__item {
  display: flex;
  align-items: baseline;
  gap: clamp(14px,3cqi,24px);
  padding: clamp(12px,2.4cqi,18px) 4px;
  border-bottom: 1px solid var(--line);
  text-decoration: none;
  color: inherit;
}

.cth-20__item em {
  font-style: normal;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  font-weight: 700;
  color: var(--mut);
  transition: font-weight .45s ease,color .3s ease;
}

.cth-20__label {
  display: block;
  font-size: clamp(24px,4.8cqi,40px);
  font-weight: 300;
  letter-spacing: -.015em;
  line-height: 1.2;
  transition: font-weight .45s ease,color .3s ease;
}

.cth-20__label::after {
  content: attr(data-text);
  display: block;
  height: 0;
  overflow: hidden;
  font-weight: 800;
  visibility: hidden;
}

.cth-20__item:hover .cth-20__label,
.cth-20__item:focus-visible .cth-20__label {
  font-weight: 800;
  color: var(--acc);
}

.cth-20__item:hover em,
.cth-20__item:focus-visible em {
  font-weight: 250;
  color: color-mix(in oklch,var(--mut) 60%,transparent);
}

.cth-20__item:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 4px;
}

.cth-20__hint {
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 60ch;
}

.cth-20__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.92 0.006 55);
  padding: 1px 6px;
  border-radius: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .cth-20 * {
    transition-duration: .01ms !important;
  }
}
```
