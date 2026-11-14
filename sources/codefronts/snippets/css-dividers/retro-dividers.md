---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/retro-dividers/"
title: "8-Bit Retro Pixelated Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "Pixel art without a single image file."
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 8-Bit Retro Pixelated Divider CSS
Source: https://codefronts.com/snippets/css-dividers/retro-dividers/

Pixel art without a single image file. A checkerboard rule from one conic-gradient, a stepped staircase divider, and a scrolling dither band — all sized in whole "pixels" from a --px token so the artwork stays crisp at any scale. The animation uses steps() timing, because 8-bit motion that eases is 8-bit motion that's wrong.
## HTML
```html
<section class="div-20" aria-label="8-bit retro pixelated divider demo">
  <div class="div-20__stage">
    <p class="div-20__eyebrow">STAGE 1-1</p>
    <h2 class="div-20__title">PIXEL RULE</h2>
    <div class="div-20__checker" role="separator" aria-label="Divider"></div>
    <div class="div-20__hud">
      <span>SCORE 026000</span><span class="div-20__vs" aria-hidden="true"></span><span>LIVES ×3</span>
    </div>
    <div class="div-20__stairs" role="separator" aria-label="Divider"></div>
    <p class="div-20__sub">One conic-gradient. One --px token. steps() timing, because 8-bit motion never eases.</p>
    <div class="div-20__dither" role="separator" aria-label="Divider"></div>
    <p class="div-20__chip">conic-gradient checkerboard · steps(8,end) · image-rendering:pixelated</p>
  </div>
</section>
```
## CSS
```css
.div-20 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-20-bg);
  --div-20-bg: oklch(0.19 0.03 265);
  --div-20-ink: oklch(0.88 0.16 140);
  --div-20-ink2: oklch(0.62 0.13 145);
  --div-20-mut: oklch(0.66 0.05 200);
  --div-20-acc: oklch(0.83 0.16 85);
  --div-20-px: 8px;
  font-family: ui-monospace,'Courier New',Menlo,monospace;
  color: var(--div-20-ink);
  image-rendering: pixelated;
}

.div-20 *,
.div-20 *::before,
.div-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-20__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(16px,3vw,26px);
  text-align: center;
  padding: clamp(28px,6vw,72px) clamp(20px,5vw,56px);
  width: min(94vw,620px);
  margin-inline: auto;
}

.div-20__eyebrow {
  font-size: 11.5px;
  letter-spacing: .34em;
  color: var(--div-20-acc);
}

.div-20__title {
  font-size: clamp(30px,7.6vw,72px);
  line-height: 1;
  letter-spacing: .06em;
  font-weight: 700;
  text-shadow: calc(var(--div-20-px)/2) calc(var(--div-20-px)/2) 0 var(--div-20-ink2);
}

.div-20__checker {
  width: 100%;
  height: calc(var(--div-20-px) * 2);
  background: conic-gradient(var(--div-20-ink) 0 25%,transparent 0 50%,var(--div-20-ink) 0 75%,transparent 0) 0 0/calc(var(--div-20-px) * 2) calc(var(--div-20-px) * 2);
  animation: div-20-march 1.2s steps(8,end) infinite;
}

@keyframes div-20-march {
  to {
    background-position: calc(var(--div-20-px) * 16) 0;
  }
}

.div-20__hud {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: clamp(12px,3vw,22px);
  font-size: clamp(11px,2vw,14px);
  letter-spacing: .14em;
  color: var(--div-20-acc);
}

.div-20__vs {
  width: var(--div-20-px);
  height: calc(var(--div-20-px) * 3);
  background: repeating-linear-gradient(180deg,var(--div-20-ink) 0 var(--div-20-px),transparent var(--div-20-px) calc(var(--div-20-px) * 2));
}

.div-20__stairs {
  width: 100%;
  height: calc(var(--div-20-px) * 3);
  background: linear-gradient(var(--div-20-ink2) 0 0);
  -webkit-mask: repeating-linear-gradient(90deg,#000 0 var(--div-20-px),#0000 var(--div-20-px) calc(var(--div-20-px) * 2)) 0 0/100% var(--div-20-px) no-repeat,linear-gradient(#000 0 0) 0 var(--div-20-px)/100% var(--div-20-px) no-repeat,repeating-linear-gradient(90deg,#0000 0 var(--div-20-px),#000 var(--div-20-px) calc(var(--div-20-px) * 2)) 0 100%/100% var(--div-20-px) no-repeat;
  mask: repeating-linear-gradient(90deg,#000 0 var(--div-20-px),#0000 var(--div-20-px) calc(var(--div-20-px) * 2)) 0 0/100% var(--div-20-px) no-repeat,linear-gradient(#000 0 0) 0 var(--div-20-px)/100% var(--div-20-px) no-repeat,repeating-linear-gradient(90deg,#0000 0 var(--div-20-px),#000 var(--div-20-px) calc(var(--div-20-px) * 2)) 0 100%/100% var(--div-20-px) no-repeat;
}

.div-20__dither {
  width: 100%;
  height: calc(var(--div-20-px) * 3);
  background: conic-gradient(var(--div-20-acc) 0 25%,transparent 0 50%,var(--div-20-acc) 0 75%,transparent 0) 0 0/calc(var(--div-20-px) * 2) calc(var(--div-20-px) * 2);
  opacity: .55;
  -webkit-mask: linear-gradient(90deg,#000,#0000);
  mask: linear-gradient(90deg,#000,#0000);
}

.div-20__sub {
  max-width: 46ch;
  font-size: clamp(12.5px,1.8vw,15px);
  line-height: 1.7;
  color: var(--div-20-mut);
}

.div-20__chip {
  font-size: 10.5px;
  color: var(--div-20-mut);
  padding: 8px 12px;
  border: 2px solid var(--div-20-ink2);
  max-width: 100%;
  overflow-wrap: anywhere;
}

@media (prefers-reduced-motion: reduce) {
  .div-20__checker {
    animation: none;
  }
}
```
