---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/art-deco-dividers/"
title: "Art Deco Geometric Gold Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "Gold is not a colour, it is a gradient — a warm-to-pale-to-warm ramp that reads as reflected light."
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Art Deco Geometric Gold Divider CSS
Source: https://codefronts.com/snippets/css-dividers/art-deco-dividers/

Gold is not a colour, it is a gradient — a warm-to-pale-to-warm ramp that reads as reflected light. This divider stacks that ramp across a mirrored chevron ornament, a stepped ziggurat rule and a background-clip:text headline, using logical mirroring (scaleX(-1) on ::after) so the whole ornament is authored once and reflected, guaranteeing perfect symmetry at every width.
## HTML
```html
<section class="div-11" aria-label="Art deco geometric gold divider demo">
  <div class="div-11__stage">
    <p class="div-11__eyebrow">MCMXXV</p>
    <div class="div-11__deco" role="separator" aria-label="Ornamental divider">
      <span class="div-11__lozenge" aria-hidden="true"></span>
    </div>
    <h2 class="div-11__title">The Gilded Rule</h2>
    <div class="div-11__zig" aria-hidden="true"></div>
    <p class="div-11__sub">Five gradient stops, one mirrored ornament, no images.</p>
    <div class="div-11__deco div-11__deco--slim" role="separator" aria-label="Ornamental divider">
      <span class="div-11__lozenge div-11__lozenge--sm" aria-hidden="true"></span>
    </div>
    <p class="div-11__chip">background-clip:text · scale:-1 1 mirroring · clip-path chevrons</p>
  </div>
</section>
```
## CSS
```css
.div-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-11-bg);
  --div-11-bg: oklch(0.19 0.025 265);
  --div-11-ink: oklch(0.94 0.015 90);
  --div-11-mut: oklch(0.68 0.03 88);
  --div-11-gold: linear-gradient(100deg,oklch(0.62 0.11 78) 0%,oklch(0.86 0.13 92) 24%,oklch(0.98 0.05 96) 42%,oklch(0.82 0.14 88) 60%,oklch(0.58 0.1 72) 100%);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-11-ink);
}

.div-11 *,
.div-11 *::before,
.div-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-11__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(14px,2.6vw,24px);
  text-align: center;
  padding: clamp(30px,6vw,72px) clamp(20px,5vw,56px);
  background: radial-gradient(80% 60% at 50% 42%,oklch(0.26 0.04 268/.9),transparent);
}

.div-11__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .44em;
  text-indent: .44em;
  color: oklch(0.78 0.11 88);
}

.div-11__deco {
  width: min(88vw,480px);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
}

.div-11__deco::before,
.div-11__deco::after {
  content: '';
  flex: 1 1 0;
  height: 3px;
  background: var(--div-11-gold);
  clip-path: polygon(0 33%,100% 0,100% 100%,0 67%);
}

.div-11__deco::after {
  scale: -1 1;
}

.div-11__deco--slim::before,
.div-11__deco--slim::after {
  height: 2px;
  opacity: .75;
}

.div-11__lozenge {
  width: 16px;
  height: 16px;
  flex: none;
  background: var(--div-11-gold);
  clip-path: polygon(50% 0,100% 50%,50% 100%,0 50%);
  box-shadow: 0 0 18px oklch(0.82 0.14 88/.35);
}

.div-11__lozenge--sm {
  width: 9px;
  height: 9px;
}

.div-11__title {
  font-family: Georgia,'Iowan Old Style',serif;
  font-size: clamp(34px,7.4vw,78px);
  line-height: 1;
  letter-spacing: .02em;
  font-weight: 400;
  background: var(--div-11-gold);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  padding: .06em .1em;
}

.div-11__zig {
  width: min(80vw,340px);
  height: 11px;
  background: var(--div-11-gold);
  -webkit-mask: repeating-linear-gradient(90deg,#000 0 11px,#0000 11px 22px) 0 0/100% 6px no-repeat,linear-gradient(#000 0 0) 0 100%/100% 3px no-repeat;
  mask: repeating-linear-gradient(90deg,#000 0 11px,#0000 11px 22px) 0 0/100% 6px no-repeat,linear-gradient(#000 0 0) 0 100%/100% 3px no-repeat;
  opacity: .9;
}

.div-11__sub {
  max-width: 44ch;
  font-size: clamp(14px,1.8vw,17px);
  line-height: 1.6;
  color: var(--div-11-mut);
  letter-spacing: .02em;
  text-wrap: pretty;
}

.div-11__chip {
  margin-top: 10px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-11-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.82 0.14 88/.28);
  border-radius: 2px;
  max-width: 92vw;
}
```
