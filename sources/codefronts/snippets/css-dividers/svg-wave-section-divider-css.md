---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/svg-wave-section-divider-css/"
title: "SVG Wave Section Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "The most-requested section transition on the web: a hero dissolving into the next block through a stack of SVG waves."
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SVG Wave Section Divider CSS
Source: https://codefronts.com/snippets/css-dividers/svg-wave-section-divider-css/

The most-requested section transition on the web: a hero dissolving into the next block through a stack of SVG waves. Two seamlessly tiling paths ride at different speeds for real parallax, both filled with currentColor so the wave is literally the next section leaking upward — change one token and the whole seam re-themes. preserveAspectRatio="none" lets the wave stretch to any viewport without re-authoring the path.
## HTML
```html
<section class="div-01" aria-label="SVG wave section divider demo">
  <div class="div-01__hero">
    <div class="div-01__photo" aria-hidden="true"></div>
    <div class="div-01__copy">
      <p class="div-01__eyebrow">Section A · hero</p>
      <h2 class="div-01__title">Dissolve the seam, not the design</h2>
      <p class="div-01__sub">Two tiling SVG paths drift at different speeds, both filled with the next section's colour.</p>
    </div>
    <div class="div-01__wave div-01__wave--back" aria-hidden="true">
      <svg viewBox="0 0 2880 120" preserveAspectRatio="none" focusable="false"><path d="M0,80 C240,112 420,44 720,74 C1020,104 1200,42 1440,80 C1680,112 1860,44 2160,74 C2460,104 2640,42 2880,80 L2880,120 L0,120 Z"/></svg>
    </div>
    <div class="div-01__wave div-01__wave--front" aria-hidden="true">
      <svg viewBox="0 0 2880 120" preserveAspectRatio="none" focusable="false"><path d="M0,62 C180,20 360,104 720,62 C1080,20 1260,104 1440,62 C1620,20 1800,104 2160,62 C2520,20 2700,104 2880,62 L2880,120 L0,120 Z"/></svg>
    </div>
  </div>
  <div class="div-01__next">
    <p class="div-01__eyebrow div-01__eyebrow--dark">Section B · content</p>
    <p class="div-01__lede">The wave is filled with <code>currentColor</code>, so this panel's background and the divider can never drift out of sync.</p>
    <p class="div-01__chip">preserveAspectRatio="none" · tiling 2880 viewBox · translateX(-50%)</p>
  </div>
</section>
```
## CSS
```css
.div-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-01-bg);
  --div-01-bg: oklch(0.28 0.07 232);
  --div-01-next: oklch(0.965 0.012 90);
  --div-01-ink: oklch(0.98 0.01 230);
  --div-01-dark: oklch(0.26 0.03 240);
  --div-01-mut: oklch(0.52 0.02 240);
  --div-01-acc: oklch(0.78 0.14 190);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-01-ink);
}

.div-01 *,
.div-01 *::before,
.div-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-01__hero {
  position: relative;
  min-height: 58svh;
  display: grid;
  place-items: center;
  padding: clamp(36px,7vw,84px) clamp(20px,5vw,56px) clamp(80px,12vw,150px);
  overflow: hidden;
  isolation: isolate;
}

.div-01__photo {
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(160deg,oklch(0.34 0.09 228),oklch(0.22 0.06 258)),url("https://images.unsplash.com/photo-1505142468610-359e7d316be0?q=80&w=1600&auto=format&fit=crop") center/cover no-repeat;
  background-blend-mode: multiply,normal;
  filter: saturate(1.05);
}

.div-01__copy {
  max-width: 56ch;
  text-align: center;
  display: grid;
  gap: 14px;
}

.div-01__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--div-01-acc);
}

.div-01__eyebrow--dark {
  color: oklch(0.5 0.11 200);
}

.div-01__title {
  font-size: clamp(29px,5.2vw,54px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.div-01__sub {
  font-size: clamp(14px,1.7vw,17px);
  line-height: 1.6;
  color: oklch(0.9 0.02 220/.86);
  text-wrap: pretty;
}

.div-01__wave {
  position: absolute;
  inset: auto 0 -1px;
  height: clamp(64px,9vw,132px);
  line-height: 0;
  pointer-events: none;
  color: var(--div-01-next);
}

.div-01__wave svg {
  width: 200%;
  height: 100%;
  display: block;
  fill: currentColor;
}

.div-01__wave--back {
  opacity: .42;
  height: clamp(78px,11vw,158px);
}

.div-01__wave--back svg {
  animation: div-01-drift 21s linear infinite;
}

.div-01__wave--front svg {
  animation: div-01-drift 13s linear infinite;
}

@keyframes div-01-drift {
  to {
    transform: translateX(-50%);
  }
}

.div-01__next {
  min-height: 42svh;
  background: var(--div-01-next);
  color: var(--div-01-dark);
  display: grid;
  place-content: center;
  justify-items: center;
  gap: 16px;
  padding: clamp(28px,5vw,60px) clamp(20px,5vw,56px) clamp(36px,6vw,70px);
  text-align: center;
}

.div-01__lede {
  max-width: 52ch;
  font-size: clamp(15px,1.9vw,19px);
  line-height: 1.62;
  text-wrap: pretty;
}

.div-01__lede code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .86em;
  background: oklch(0.5 0.11 200/.12);
  padding: 2px 7px;
  border-radius: 6px;
}

.div-01__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--div-01-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.26 0.03 240/.16);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .div-01 svg {
    animation: none !important;
  }
}
```
