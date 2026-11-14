---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/zigzag-torn-paper-cut-divider-css/"
title: "Zigzag Torn Paper Cut Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "Sawtooth and torn-paper edges without a single image, using a conic-gradient mask instead of the old stacked-triangle background hack."
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Zigzag Torn Paper Cut Divider CSS
Source: https://codefronts.com/snippets/css-dividers/zigzag-torn-paper-cut-divider-css/

Sawtooth and torn-paper edges without a single image, using a conic-gradient mask instead of the old stacked-triangle background hack. One --tooth token sets the pitch; the same recipe cuts a full-width section seam, both edges of a receipt, and a perforated ticket stub. Because it is a mask, the teeth cut through photographs and gradients alike — backgrounds show through the notches instead of faking them with a matching colour.
## HTML
```html
<section class="div-06" aria-label="Zigzag torn paper divider demo">
  <div class="div-06__top">
    <p class="div-06__eyebrow">conic-gradient() mask</p>
    <h2 class="div-06__title">Tear the section, don't fake it</h2>
    <p class="div-06__sub">The teeth are cut out of this panel, so the photograph below shows through them.</p>
  </div>
  <div class="div-06__bottom">
    <div class="div-06__receipt">
      <p class="div-06__rhead">CODEFRONTS · RECEIPT</p>
      <dl class="div-06__line"><dt>Divider pitch</dt><dd>22px</dd></dl>
      <dl class="div-06__line"><dt>Tooth depth</dt><dd>11px</dd></dl>
      <dl class="div-06__line"><dt>Images used</dt><dd>0</dd></dl>
      <dl class="div-06__line div-06__line--tot"><dt>Total</dt><dd>1 mask</dd></dl>
    </div>
    <p class="div-06__chip">mask-composite:add · two conic layers · --tooth pitch</p>
  </div>
</section>
```
## CSS
```css
.div-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-06-bg);
  --div-06-bg: oklch(0.22 0.02 285);
  --div-06-paper: oklch(0.97 0.014 85);
  --div-06-ink: oklch(0.25 0.02 60);
  --div-06-mut: oklch(0.55 0.02 60);
  --div-06-acc: oklch(0.66 0.19 25);
  --div-06-tooth: 22px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  position: relative;
  isolation: isolate;
}

.div-06 *,
.div-06 *::before,
.div-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-06::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(180deg,oklch(0.24 0.03 290/.2),oklch(0.18 0.02 285/.9)),url("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1600&auto=format&fit=crop") center/cover no-repeat;
}

.div-06__top {
  --m: conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) 50%/var(--div-06-tooth) 100%;
  -webkit-mask: var(--m);
  mask: var(--m);
  background: linear-gradient(140deg,var(--div-06-paper),oklch(0.93 0.02 80));
  color: var(--div-06-ink);
  min-height: 52svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: 13px;
  text-align: center;
  padding: clamp(34px,7vw,78px) clamp(20px,5vw,56px) calc(var(--div-06-tooth)/2 + clamp(30px,5vw,60px));
}

.div-06__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--div-06-acc);
}

.div-06__title {
  font-size: clamp(28px,5vw,52px);
  line-height: 1.05;
  letter-spacing: -.03em;
  font-weight: 700;
  max-width: 18ch;
  text-wrap: balance;
}

.div-06__sub {
  max-width: 46ch;
  font-size: clamp(14px,1.7vw,17px);
  line-height: 1.6;
  color: var(--div-06-mut);
  text-wrap: pretty;
}

.div-06__bottom {
  min-height: 48svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: 22px;
  padding: clamp(34px,6vw,64px) clamp(20px,5vw,56px);
}

.div-06__receipt {
  --m1: conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) 50% 100%/var(--div-06-tooth) 50% repeat-x;
  --m2: conic-gradient(from 135deg at top,#0000,#000 1deg 89deg,#0000 90deg) 50% 0/var(--div-06-tooth) 50% repeat-x;
  -webkit-mask: var(--m1),var(--m2);
  mask: var(--m1),var(--m2);
  width: min(88vw,340px);
  background: var(--div-06-paper);
  color: var(--div-06-ink);
  padding: calc(var(--div-06-tooth)/2 + 20px) 26px;
  filter: drop-shadow(0 16px 28px oklch(0 0 0/.42));
  font-family: ui-monospace,Menlo,Consolas,monospace;
}

.div-06__rhead {
  font-size: 11.5px;
  letter-spacing: .2em;
  text-align: center;
  padding-bottom: 12px;
  border-bottom: 1.5px dashed oklch(0.25 0.02 60/.3);
  margin-bottom: 12px;
}

.div-06__line {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  font-size: 12.5px;
  padding: 5px 0;
  color: var(--div-06-mut);
}

.div-06__line dd {
  color: var(--div-06-ink);
  font-weight: 600;
}

.div-06__line--tot {
  border-top: 1.5px dashed oklch(0.25 0.02 60/.3);
  margin-top: 8px;
  padding-top: 11px;
  font-size: 14px;
}

.div-06__line--tot dt,
.div-06__line--tot dd {
  color: var(--div-06-acc);
  font-weight: 700;
}

.div-06__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: oklch(0.9 0.01 285/.75);
  padding: 8px 14px;
  border: 1px solid oklch(1 0 0/.18);
  border-radius: 99px;
  text-align: center;
}
```
