---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/pure-css-ornamental-divider-with-pseudo-elements/"
title: "Pure CSS Ornamental Divider with Pseudo-Elements"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "Five ornamental rules, each built from ONE element — a bare <hr> — with the glyph injected by content: attr(data-glyph) and the flanking rules painted as…"
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Ornamental Divider with Pseudo-Elements
Source: https://codefronts.com/snippets/css-dividers/pure-css-ornamental-divider-with-pseudo-elements/

Five ornamental rules, each built from ONE element — a bare <hr> — with the glyph injected by content: attr(data-glyph) and the flanking rules painted as backgrounds. No wrapper divs, no spans, no icon font. Because the ornament is a data attribute, one CSS rule serves diamonds, fleurons, asterisks and chevrons, and the markup stays a semantically correct thematic break.
## HTML
```html
<section class="div-08" aria-label="Ornamental pseudo-element divider demo">
  <div class="div-08__stage">
    <p class="div-08__eyebrow">one &lt;hr&gt; · zero extra markup</p>
    <h2 class="div-08__title">Ornaments from a data attribute</h2>
    <div class="div-08__set">
      <hr class="div-08__orn" data-glyph="❖">
      <hr class="div-08__orn" data-glyph="❦">
      <hr class="div-08__orn div-08__orn--cluster" data-glyph="✦ ✦ ✦">
      <hr class="div-08__orn div-08__orn--taper" data-glyph="§">
      <hr class="div-08__orn div-08__orn--heavy" data-glyph="◆">
    </div>
    <p class="div-08__chip">content:attr(data-glyph) · punched-through background · role="separator" kept</p>
  </div>
</section>
```
## CSS
```css
.div-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-08-bg);
  --div-08-bg: oklch(0.975 0.012 92);
  --div-08-ink: oklch(0.26 0.02 60);
  --div-08-mut: oklch(0.56 0.02 60);
  --div-08-line: oklch(0.26 0.02 60/.28);
  --div-08-acc: oklch(0.55 0.12 40);
  font-family: Georgia,'Iowan Old Style','Times New Roman',serif;
  color: var(--div-08-ink);
}

.div-08 *,
.div-08 *::before,
.div-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-08__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(20px,4vw,34px);
  padding: clamp(28px,6vw,72px) clamp(20px,5vw,56px);
  background: radial-gradient(110% 80% at 50% 0%,oklch(0.995 0.008 92),transparent);
}

.div-08__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--div-08-acc);
}

.div-08__title {
  font-size: clamp(28px,5vw,50px);
  line-height: 1.06;
  letter-spacing: -.02em;
  font-weight: 400;
  text-align: center;
  text-wrap: balance;
}

.div-08__set {
  width: min(90vw,560px);
  display: grid;
  gap: clamp(26px,5vw,44px);
}

.div-08__orn {
  position: relative;
  border: 0;
  height: 1px;
  background: linear-gradient(90deg,transparent,var(--div-08-line) 20%,var(--div-08-line) 80%,transparent);
}

.div-08__orn::before {
  content: attr(data-glyph);
  position: absolute;
  left: 50%;
  top: 50%;
  translate: -50% -50%;
  padding: 0 .7em;
  background: var(--div-08-bg);
  color: var(--div-08-acc);
  font-family: 'Segoe UI Symbol','Apple Symbols','Noto Sans Symbols 2','Segoe UI Historic',Georgia,serif;
  font-size: 22px;
  line-height: 1;
  transition: rotate .5s cubic-bezier(.65,0,.35,1),color .3s ease;
}

.div-08__orn:hover::before {
  rotate: 180deg;
  color: oklch(0.45 0.15 30);
}

.div-08__orn--cluster::before {
  letter-spacing: .34em;
  font-size: 14px;
  padding: 0 .9em;
}

.div-08__orn--taper {
  height: 3px;
  background: linear-gradient(90deg,transparent,var(--div-08-line) 30%,transparent 48%,transparent 52%,var(--div-08-line) 70%,transparent);
  -webkit-mask: linear-gradient(90deg,#0000,#000 8%,#000 92%,#0000);
  mask: linear-gradient(90deg,#0000,#000 8%,#000 92%,#0000);
}

.div-08__orn--taper::before {
  font-size: 17px;
  font-style: italic;
}

.div-08__orn--heavy {
  height: 4px;
  border-radius: 99px;
  background: linear-gradient(90deg,transparent,var(--div-08-acc) 26%,var(--div-08-acc) 74%,transparent);
  opacity: .75;
}

.div-08__orn--heavy::before {
  font-size: 13px;
  padding: 0 1em;
}

.div-08__chip {
  margin-top: 8px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-08-mut);
  padding: 8px 14px;
  border: 1px solid var(--div-08-line);
  border-radius: 99px;
  text-align: center;
  max-width: 92vw;
}

@media (prefers-reduced-motion: reduce) {
  .div-08__orn::before {
    transition: none;
  }
}
```
