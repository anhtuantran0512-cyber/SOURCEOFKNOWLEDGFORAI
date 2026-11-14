---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/gradient-horizontal-rule-css/"
title: "Gradient Horizontal Rule CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "Four upgrades to the humblest element in HTML, all on a real <hr> so the semantics survive: a fade-to-transparent hairline, a multi-stop brand spectrum, a…"
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Horizontal Rule CSS
Source: https://codefronts.com/snippets/css-dividers/gradient-horizontal-rule-css/

Four upgrades to the humblest element in HTML, all on a real <hr> so the semantics survive: a fade-to-transparent hairline, a multi-stop brand spectrum, a hard-stop colour-band rule, and an animated sheen driven by @property so the gradient position is a genuinely interpolatable value. Every version resets the browser's inset border first — the step most snippets skip.
## HTML
```html
<section class="div-03" aria-label="Gradient horizontal rule divider demo">
  <div class="div-03__stage">
    <header class="div-03__head">
      <p class="div-03__eyebrow">&lt;hr&gt; · four gradient treatments</p>
      <h2 class="div-03__title">Rules worth reading</h2>
    </header>
    <div class="div-03__row"><span class="div-03__lab">Fade to transparent</span><hr class="div-03__hr div-03__hr--fade"></div>
    <div class="div-03__row"><span class="div-03__lab">Brand spectrum</span><hr class="div-03__hr div-03__hr--spectrum"></div>
    <div class="div-03__row"><span class="div-03__lab">Hard colour bands</span><hr class="div-03__hr div-03__hr--bands"></div>
    <div class="div-03__row"><span class="div-03__lab">Animated sheen</span><hr class="div-03__hr div-03__hr--sheen"></div>
    <p class="div-03__chip">border:0 · @property &lt;percentage&gt; · mask-image feather</p>
  </div>
</section>
```
## CSS
```css
@property --div-03-pos {
  syntax: '<percentage>';
  inherits: false;
  initial-value: -20%;
}

.div-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-03-bg);
  --div-03-bg: oklch(0.16 0.02 275);
  --div-03-ink: oklch(0.96 0.008 270);
  --div-03-mut: oklch(0.66 0.02 270);
  --div-03-acc: oklch(0.72 0.16 305);
  --div-03-acc2: oklch(0.78 0.15 200);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-03-ink);
}

.div-03 *,
.div-03 *::before,
.div-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-03__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(18px,3vw,30px);
  padding: clamp(28px,6vw,72px) clamp(20px,5vw,56px);
  background: radial-gradient(85% 60% at 50% 0%,oklch(0.24 0.06 300/.75),transparent);
}

.div-03__head {
  text-align: center;
  display: grid;
  gap: 10px;
  margin-bottom: 6px;
}

.div-03__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--div-03-acc);
}

.div-03__title {
  font-size: clamp(27px,4.6vw,46px);
  line-height: 1.05;
  letter-spacing: -.03em;
  font-weight: 700;
}

.div-03__row {
  width: min(92vw,620px);
  display: grid;
  gap: 11px;
}

.div-03__lab {
  font-size: 12.5px;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--div-03-mut);
  font-weight: 600;
}

.div-03__hr {
  border: 0;
  height: 3px;
  border-radius: 99px;
  width: 100%;
}

.div-03__hr--fade {
  background: linear-gradient(90deg,transparent,var(--div-03-acc),transparent);
}

.div-03__hr--spectrum {
  background: linear-gradient(90deg,oklch(0.75 0.17 25),oklch(0.8 0.16 75),oklch(0.8 0.15 150),var(--div-03-acc2),var(--div-03-acc));
  -webkit-mask-image: linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);
  mask-image: linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);
}

.div-03__hr--bands {
  height: 6px;
  background: linear-gradient(90deg,oklch(0.75 0.17 25) 0 20%,oklch(0.8 0.16 75) 20% 40%,oklch(0.8 0.15 150) 40% 60%,var(--div-03-acc2) 60% 80%,var(--div-03-acc) 80% 100%);
}

.div-03__hr--sheen {
  height: 4px;
  background: radial-gradient(closest-side,oklch(0.99 0.02 300),transparent) var(--div-03-pos) 50%/30% 240% no-repeat,linear-gradient(90deg,oklch(0.4 0.06 290),oklch(0.45 0.07 250));
  animation: div-03-sweep 3.6s cubic-bezier(.65,0,.35,1) infinite;
  -webkit-mask-image: linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);
  mask-image: linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);
}

@keyframes div-03-sweep {
  0% {
    --div-03-pos: -20%;
  }

  100% {
    --div-03-pos: 120%;
  }
}

.div-03__chip {
  margin-top: 8px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--div-03-mut);
  padding: 8px 14px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .div-03__hr--sheen {
    animation: none;
    --div-03-pos: 50%;
  }
}
```
