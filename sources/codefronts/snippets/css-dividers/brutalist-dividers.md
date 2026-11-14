---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/brutalist-dividers/"
title: "Neo-Brutalist Heavy Border Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "Brutalism's whole grammar in one divider: a 6px black slab, a hard unblurred offset shadow, zero border-radius, and a marching hazard-stripe rule built from…"
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neo-Brutalist Heavy Border Divider CSS
Source: https://codefronts.com/snippets/css-dividers/brutalist-dividers/

Brutalism's whole grammar in one divider: a 6px black slab, a hard unblurred offset shadow, zero border-radius, and a marching hazard-stripe rule built from a single repeating-linear-gradient. The trick that makes stripes scroll seamlessly is animating background-position by exactly one tile — get that number wrong and the pattern visibly stutters every loop.
## HTML
```html
<section class="div-10" aria-label="Neo-brutalist heavy border divider demo">
  <div class="div-10__stage">
    <div class="div-10__card">
      <p class="div-10__eyebrow">SECTION 01 / SPECS</p>
      <h2 class="div-10__title">HEAVY<br>BORDERS</h2>
    </div>
    <hr class="div-10__slab">
    <div class="div-10__hazard" role="separator" aria-label="Hazard divider">
      <span class="div-10__stamp">DIVIDER</span>
    </div>
    <hr class="div-10__slab div-10__slab--thin">
    <p class="div-10__note">Unblurred offset shadows. Zero radius. √2 stripe travel.</p>
    <p class="div-10__chip">repeating-linear-gradient(45deg) · background-position × 1.414</p>
  </div>
</section>
```
## CSS
```css
.div-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-10-bg);
  --div-10-bg: oklch(0.93 0.13 105);
  --div-10-ink: oklch(0.18 0.012 265);
  --div-10-acc: oklch(0.99 0 0);
  --div-10-acc2: oklch(0.68 0.21 355);
  --div-10-tile: 30px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-10-ink);
}

.div-10 *,
.div-10 *::before,
.div-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-10__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: stretch;
  gap: clamp(18px,3.4vw,30px);
  padding: clamp(28px,6vw,72px) clamp(20px,5vw,56px);
  width: min(94vw,660px);
  margin-inline: auto;
}

.div-10__card {
  background: var(--div-10-acc);
  border: 4px solid var(--div-10-ink);
  box-shadow: 9px 9px 0 0 var(--div-10-ink);
  padding: clamp(22px,4vw,34px);
}

.div-10__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .2em;
  color: var(--div-10-acc2);
  font-weight: 700;
  margin-bottom: 10px;
}

.div-10__title {
  font-size: clamp(38px,9vw,86px);
  line-height: .9;
  letter-spacing: -.045em;
  font-weight: 900;
  text-transform: uppercase;
}

.div-10__slab {
  border: 0;
  height: 9px;
  background: var(--div-10-ink);
  box-shadow: 7px 7px 0 0 var(--div-10-acc2);
}

.div-10__slab--thin {
  height: 4px;
  box-shadow: 5px 5px 0 0 var(--div-10-ink);
}

.div-10__hazard {
  position: relative;
  height: clamp(46px,7vw,62px);
  border: 4px solid var(--div-10-ink);
  background: repeating-linear-gradient(45deg,var(--div-10-ink) 0 calc(var(--div-10-tile)/2),var(--div-10-acc) calc(var(--div-10-tile)/2) var(--div-10-tile));
  animation: div-10-march 1.15s linear infinite;
  display: grid;
  place-items: center;
  box-shadow: 9px 9px 0 0 var(--div-10-ink);
}

@keyframes div-10-march {
  to {
    background-position: calc(var(--div-10-tile) * 1.414) 0;
  }
}

.div-10__stamp {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(13px,2.2vw,17px);
  font-weight: 800;
  letter-spacing: .24em;
  background: var(--div-10-bg);
  border: 3px solid var(--div-10-ink);
  padding: 7px 16px;
  color: var(--div-10-ink);
}

.div-10__note {
  font-size: clamp(14px,2vw,17px);
  font-weight: 700;
  line-height: 1.5;
  text-transform: uppercase;
  letter-spacing: .01em;
}

.div-10__chip {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  padding: 8px 14px;
  border: 2.5px solid var(--div-10-ink);
  background: var(--div-10-acc);
  max-width: 100%;
  overflow-wrap: anywhere;
}

@media (prefers-reduced-motion: reduce) {
  .div-10__hazard {
    animation: none;
  }
}
```
