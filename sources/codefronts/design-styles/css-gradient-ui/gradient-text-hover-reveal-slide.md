---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/gradient-text-hover-reveal-slide/"
title: "Gradient Text Hover Reveal / Slide"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "An oversized editorial menu where each entry floods with its own gradient on hover — a left-to-right wipe driven by animatable background-size on the clipped…"
has_js: "false"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Text Hover Reveal / Slide
Source: https://codefronts.com/design-styles/css-gradient-ui/gradient-text-hover-reveal-slide/

An oversized editorial menu where each entry floods with its own gradient on hover — a left-to-right wipe driven by animatable background-size on the clipped text, plus an index number and a meta line that answer the hover in sync.
## HTML
```html
<div class="cgu-13-group">
<section class="cgu-13" aria-label="Gradient text hover reveal demos">
  <div class="cgu-13__inner">
    <header class="cgu-13__head">
      <p class="cgu-13__eyebrow">13 · Hover reveal</p>
      <p class="cgu-13__hint">Hover — or Tab through — each line</p>
    </header>
    <nav class="cgu-13__menu" aria-label="Studio index">
      <a class="cgu-13__item" href="#work" style="--g1:#38bdf8;--g2:#818cf8"><span class="cgu-13__no" aria-hidden="true">01</span><span class="cgu-13__word">Work</span><span class="cgu-13__meta">14 case studies</span></a>
      <a class="cgu-13__item" href="#studio" style="--g1:#f472b6;--g2:#fb923c"><span class="cgu-13__no" aria-hidden="true">02</span><span class="cgu-13__word">Studio</span><span class="cgu-13__meta">est. 2019, Lisbon</span></a>
      <a class="cgu-13__item" href="#journal" style="--g1:#34d399;--g2:#a3e635"><span class="cgu-13__no" aria-hidden="true">03</span><span class="cgu-13__word">Journal</span><span class="cgu-13__meta">notes on craft</span></a>
      <a class="cgu-13__item" href="#contact" style="--g1:#fbbf24;--g2:#f43f5e"><span class="cgu-13__no" aria-hidden="true">04</span><span class="cgu-13__word">Contact</span><span class="cgu-13__meta">[email protected]</span></a>
    </nav>
    <p class="cgu-13__foot">One element per line — the wipe is two stacked backgrounds on the same clipped text, no extra spans.</p>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-13-group {
  display: block;
  width: 100%;
}

.cgu-13,
.cgu-13 *,
.cgu-13 *::before,
.cgu-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgu-13 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #eef0ff;
  background: #0b0a12;
}

.cgu-13__inner {
  width: min(820px,100%);
  display: grid;
  gap: 30px;
}

.cgu-13__head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 16px;
  flex-wrap: wrap;
}

.cgu-13__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #fb923c;
}

.cgu-13__hint {
  font-size: 13px;
  color: #7c81a3;
}

.cgu-13__menu {
  display: grid;
}

.cgu-13__item {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: baseline;
  gap: 26px;
  padding: 26px 8px;
  text-decoration: none;
  border-bottom: 1px solid rgba(255,255,255,.09);
}

.cgu-13__item:first-child {
  border-top: 1px solid rgba(255,255,255,.09);
}

.cgu-13__no {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 13px;
  color: #5c6180;
  transition: color .35s;
}

.cgu-13__word {
  font-size: clamp(38px,7vw,76px);
  font-weight: 850;
  letter-spacing: -.03em;
  line-height: 1;
  color: #8a8fa8;
  transition: background-size .55s cubic-bezier(.2,.8,.2,1),transform .55s cubic-bezier(.2,.8,.2,1);
}

@supports (background-clip: text) or (-webkit-background-clip: text) {
  .cgu-13__word {
    background: linear-gradient(90deg,var(--g1),var(--g2)) no-repeat 0 0 / 0% 100%,linear-gradient(#8a8fa8,#8a8fa8);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }
}

.cgu-13__meta {
  font-size: 13px;
  color: #5c6180;
  opacity: 0;
  transform: translateX(-8px);
  transition: opacity .4s .08s,transform .4s .08s;
}

.cgu-13__item:hover .cgu-13__word,
.cgu-13__item:focus-visible .cgu-13__word {
  background-size: 100% 100%,100% 100%;
  transform: translateX(10px);
}

.cgu-13__item:hover .cgu-13__no,
.cgu-13__item:focus-visible .cgu-13__no {
  color: var(--g1);
}

.cgu-13__item:hover .cgu-13__meta,
.cgu-13__item:focus-visible .cgu-13__meta {
  opacity: 1;
  transform: translateX(0);
}

.cgu-13__item:focus-visible {
  outline: 2px solid var(--g1);
  outline-offset: 4px;
  border-radius: 6px;
}

.cgu-13__foot {
  font-size: 13px;
  color: #7c81a3;
}

@media (prefers-reduced-motion: reduce) {
  .cgu-13__word,
    .cgu-13__meta {
    transition: none;
  }

  .cgu-13__item:hover .cgu-13__word {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the wipe grows one gradient layer's background-size over a solid resting layer, both clipped to the same glyphs. */
```
