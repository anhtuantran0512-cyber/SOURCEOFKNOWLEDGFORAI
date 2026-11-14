---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/claymorphism-with-glassmorphism-hybrid/"
title: "Claymorphism with Glassmorphism Hybrid"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "The hybrid that dominates 2026 product pages: clay geometry and clay shadow layering, but the fill is frosted glass."
has_js: "false"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Claymorphism with Glassmorphism Hybrid
Source: https://codefronts.com/design-styles/css-claymorphism/claymorphism-with-glassmorphism-hybrid/

The hybrid that dominates 2026 product pages: clay geometry and clay shadow layering, but the fill is frosted glass. A blurred photographic backdrop shows through the card while the inset highlight keeps the puffy silhouette — so it still reads as a solid object rather than a floating pane. Includes the rim-light border trick that keeps glass edges visible on both bright and dark imagery.
## HTML
```html
<section class="cl-05" aria-label="Claymorphism with glassmorphism hybrid card demo">
  <div class="cl-05__stage">
    <div class="cl-05__scene">
      <div class="cl-05__photo" aria-hidden="true"></div>
      <div class="cl-05__blobs" aria-hidden="true"><i></i><i></i></div>
      <article class="cl-05__card">
        <header class="cl-05__top">
          <span class="cl-05__badge">Frosted clay</span>
          <span class="cl-05__dot" aria-hidden="true"></span>
        </header>
        <h2 class="cl-05__h">Aurora Pass</h2>
        <p class="cl-05__body">Clay geometry, glass fill. The inset sheen keeps the puffy silhouette while the backdrop shows through.</p>
        <dl class="cl-05__stats">
          <div><dt>Blur</dt><dd>26px</dd></div>
          <div><dt>Tint</dt><dd>26%</dd></div>
          <div><dt>Radius</dt><dd>40px</dd></div>
        </dl>
        <div class="cl-05__actions">
          <button class="cl-05__btn cl-05__btn--solid" type="button">Get the pass</button>
          <button class="cl-05__btn" type="button">Details</button>
        </div>
      </article>
    </div>
    <p class="cl-05__chip" aria-hidden="true">backdrop-filter: blur + saturate · rim-light hairline · brighter inset sheen</p>
  </div>
</section>
```
## CSS
```css
.cl-05,
.cl-05 *,
.cl-05 *::before,
.cl-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--cl-05-bg);
  --cl-05-bg: oklch(0.32 0.09 285);
  --cl-05-tint: oklch(0.86 0.09 300);
  --cl-05-shade: oklch(0.22 0.09 285/.7);
  --cl-05-ink: oklch(0.99 0.01 300);
  --cl-05-mut: oklch(0.88 0.03 300/.82);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-05-ink);
}

.cl-05__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 22px;
  padding: clamp(20px,5vw,56px);
}

.cl-05__scene {
  position: relative;
  isolation: isolate;
  display: grid;
  place-items: center;
  width: min(100%,760px);
  min-height: min(74vh,520px);
  padding: clamp(18px,4vw,44px);
  border-radius: 48px;
  overflow: hidden;
  background: linear-gradient(140deg,oklch(0.45 0.16 300),oklch(0.38 0.14 250));
  box-shadow: 0 40px 80px -30px oklch(0.15 0.06 285/.8);
}

.cl-05__photo {
  position: absolute;
  inset: 0;
  z-index: -2;
  background: center/cover no-repeat url('https://images.unsplash.com/photo-1502691876148-a84978e59af8?q=80&w=1400&auto=format&fit=crop'),linear-gradient(140deg,oklch(0.5 0.17 305),oklch(0.34 0.13 250));
  opacity: .92;
  scale: 1.02;
  animation: cl-05-drift 26s ease-in-out infinite alternate;
}

@keyframes cl-05-drift {
  to {
    scale: 1.1;
    translate: -2% 1%;
  }
}

.cl-05__blobs {
  position: absolute;
  inset: 0;
  z-index: -1;
}

.cl-05__blobs i {
  position: absolute;
  width: 44%;
  aspect-ratio: 1;
  border-radius: 50%;
  filter: blur(6px);
  opacity: .55;
}

.cl-05__blobs i:nth-child(1) {
  left: -8%;
  top: -12%;
  background: oklch(0.8 0.16 30/.55);
}

.cl-05__blobs i:nth-child(2) {
  right: -10%;
  bottom: -14%;
  background: oklch(0.82 0.15 175/.5);
}

.cl-05__card {
  display: grid;
  gap: 14px;
  width: min(100%,392px);
  padding: clamp(24px,3.4vw,34px);
  border-radius: 40px;
  border: 1px solid color-mix(in oklch,white 42%,transparent);
  background: color-mix(in oklch,var(--cl-05-tint) 24%,transparent);
  -webkit-backdrop-filter: blur(26px) saturate(1.7);
  backdrop-filter: blur(26px) saturate(1.7);
  box-shadow: 0 30px 60px -20px var(--cl-05-shade),inset 0 -18px 30px -14px var(--cl-05-shade),inset 0 20px 30px -10px oklch(1 0 0/.5);
  transition: translate .45s cubic-bezier(.34,1.3,.5,1),box-shadow .45s;
}

.cl-05__card:hover {
  translate: 0 -8px;
  box-shadow: 0 44px 80px -26px var(--cl-05-shade),inset 0 -18px 30px -14px var(--cl-05-shade),inset 0 22px 32px -10px oklch(1 0 0/.58);
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .cl-05__card {
    background: color-mix(in oklch,var(--cl-05-tint) 88%,transparent);
    color: oklch(0.28 0.06 290);
  }
}

.cl-05__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.cl-05__badge {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  padding: 7px 13px;
  border-radius: 99px;
  background: oklch(1 0 0/.2);
  box-shadow: inset 0 -4px 8px -6px var(--cl-05-shade),inset 0 6px 8px -5px oklch(1 0 0/.6);
}

.cl-05__dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: oklch(0.85 0.17 150);
  box-shadow: 0 0 0 4px oklch(0.85 0.17 150/.22),inset 0 3px 4px -2px oklch(1 0 0/.9);
}

.cl-05__h {
  font-size: clamp(26px,4vw,34px);
  font-weight: 780;
  letter-spacing: -.025em;
}

.cl-05__body {
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--cl-05-mut);
  text-wrap: pretty;
}

.cl-05__stats {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 10px;
  margin-top: 2px;
}

.cl-05__stats div {
  display: grid;
  gap: 3px;
  padding: 12px 14px;
  border-radius: 22px;
  background: oklch(1 0 0/.14);
  box-shadow: inset 0 -6px 10px -8px var(--cl-05-shade),inset 0 8px 10px -6px oklch(1 0 0/.5);
}

.cl-05__stats dt {
  font-size: 10.5px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--cl-05-mut);
}

.cl-05__stats dd {
  font-size: 15px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.cl-05__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 6px;
}

.cl-05__btn {
  min-height: 48px;
  padding: 0 22px;
  border: 1px solid oklch(1 0 0/.3);
  border-radius: 26px;
  font: inherit;
  font-size: 14px;
  font-weight: 660;
  color: var(--cl-05-ink);
  cursor: pointer;
  background: oklch(1 0 0/.14);
  box-shadow: inset 0 -8px 12px -9px var(--cl-05-shade),inset 0 9px 12px -7px oklch(1 0 0/.55);
  transition: translate .2s,background .25s;
}

.cl-05__btn:hover {
  background: oklch(1 0 0/.24);
  translate: 0 -2px;
}

.cl-05__btn:active {
  translate: 0 2px;
  box-shadow: inset 0 8px 14px -8px var(--cl-05-shade);
}

.cl-05__btn:focus-visible {
  outline: 3px solid var(--cl-05-ink);
  outline-offset: 3px;
}

.cl-05__btn--solid {
  border-color: transparent;
  color: oklch(0.26 0.07 290);
  background: oklch(0.94 0.05 300/.92);
  box-shadow: 0 14px 24px -14px var(--cl-05-shade),inset 0 -8px 12px -9px oklch(0.6 0.1 290/.5),inset 0 9px 12px -7px oklch(1 0 0);
}

.cl-05__btn--solid:hover {
  background: oklch(0.97 0.04 300/.96);
}

.cl-05__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cl-05-mut);
  padding: 9px 16px;
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.1);
  box-shadow: inset 0 6px 10px -6px oklch(1 0 0/.35);
}

@media (prefers-reduced-motion: reduce) {
  .cl-05__photo {
    animation: none;
  }

  .cl-05 * {
    transition-duration: .01ms !important;
  }
}

@media (prefers-reduced-transparency: reduce) {
  .cl-05__card {
    background: color-mix(in oklch,var(--cl-05-tint) 92%,transparent);
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    color: oklch(0.26 0.06 290);
  }
}
```
