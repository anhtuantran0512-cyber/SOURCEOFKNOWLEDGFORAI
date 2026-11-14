---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/curved-arch-section-divider-css/"
title: "Curved Arch Section Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "Concave and convex arches between full-width sections — and not an SVG in sight."
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Curved Arch Section Divider CSS
Source: https://codefronts.com/snippets/css-dividers/curved-arch-section-divider-css/

Concave and convex arches between full-width sections — and not an SVG in sight. The whole curve is one elliptical border-radius on an overlay block, which means it is resolution-independent, animatable, and themable with a single background token. A :has()-driven toggle flips the page between the two curvatures so you can feel the difference before choosing.
## HTML
```html
<section class="div-05" aria-label="Curved arch section divider demo">
  <div class="div-05__top">
    <div class="div-05__photo" aria-hidden="true"></div>
    <div class="div-05__copy">
      <p class="div-05__eyebrow">border-radius · elliptical</p>
      <h2 class="div-05__title">An arch, drawn by one property</h2>
    </div>
    <div class="div-05__arch" aria-hidden="true"></div>
  </div>
  <div class="div-05__bottom">
    <p class="div-05__lede">The slash in <code>50% 50% 0 0 / 100% 100% 0 0</code> splits horizontal radii from vertical ones — that is the entire curve.</p>
    <label class="div-05__toggle">
      <input class="div-05__cb" id="div-05-flip" type="checkbox">
      <span class="div-05__track" aria-hidden="true"><span class="div-05__knob"></span></span>
      <span class="div-05__tlab">Concave scoop</span>
    </label>
    <p class="div-05__chip">:has(:checked) flips curvature · zero JavaScript</p>
  </div>
</section>
```
## CSS
```css
.div-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-05-bg);
  --div-05-bg: oklch(0.955 0.018 60);
  --div-05-top: oklch(0.32 0.06 25);
  --div-05-ink: oklch(0.97 0.015 60);
  --div-05-dark: oklch(0.28 0.03 40);
  --div-05-mut: oklch(0.55 0.03 40);
  --div-05-acc: oklch(0.72 0.15 45);
  --div-05-h: clamp(52px,9vw,120px);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-05-dark);
}

.div-05 *,
.div-05 *::before,
.div-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-05__top {
  position: relative;
  min-height: 54svh;
  display: grid;
  place-items: center;
  padding: clamp(34px,7vw,80px) clamp(20px,5vw,56px) calc(var(--div-05-h) + 24px);
  overflow: hidden;
  isolation: isolate;
  color: var(--div-05-ink);
}

.div-05__photo {
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(150deg,oklch(0.4 0.08 30),oklch(0.24 0.05 20)),url("https://images.unsplash.com/photo-1520175480921-4edfa2983e0f?q=80&w=1600&auto=format&fit=crop") center/cover no-repeat;
  background-blend-mode: multiply,normal;
}

.div-05__copy {
  max-width: 48ch;
  text-align: center;
  display: grid;
  gap: 12px;
}

.div-05__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--div-05-acc);
}

.div-05__title {
  font-size: clamp(28px,5vw,52px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.div-05__arch {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: var(--div-05-h);
  background: var(--div-05-bg);
  border-radius: 50% 50% 0 0/100% 100% 0 0;
  pointer-events: none;
  transition: opacity .45s cubic-bezier(.65,0,.35,1);
}

.div-05:has(.div-05__cb:checked) .div-05__arch {
  opacity: 0;
}

.div-05__bottom {
  position: relative;
}

.div-05__bottom::before {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  height: var(--div-05-h);
  background: linear-gradient(150deg,oklch(0.4 0.08 30),oklch(0.24 0.05 20)),url("https://images.unsplash.com/photo-1520175480921-4edfa2983e0f?q=80&w=1600&auto=format&fit=crop") center/cover no-repeat;
  background-blend-mode: multiply,normal;
  border-radius: 0 0 50% 50%/0 0 100% 100%;
  pointer-events: none;
  opacity: 0;
  transition: opacity .45s cubic-bezier(.65,0,.35,1);
  z-index: 1;
}

.div-05:has(.div-05__cb:checked) .div-05__bottom::before {
  opacity: 1;
}

.div-05__bottom {
  min-height: 46svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: 20px;
  padding: clamp(28px,5vw,60px) clamp(20px,5vw,56px);
  text-align: center;
}

.div-05__lede {
  max-width: 52ch;
  font-size: clamp(15px,1.9vw,19px);
  line-height: 1.62;
  text-wrap: pretty;
}

.div-05__lede code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .84em;
  background: oklch(0.72 0.15 45/.16);
  padding: 2px 7px;
  border-radius: 6px;
}

.div-05__toggle {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  min-height: 44px;
  cursor: pointer;
  user-select: none;
}

.div-05__cb {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.div-05__track {
  width: 52px;
  height: 30px;
  border-radius: 99px;
  background: oklch(0.28 0.03 40/.16);
  display: flex;
  align-items: center;
  padding: 3px;
  transition: background .28s ease;
}

.div-05__knob {
  width: 24px;
  height: 24px;
  border-radius: 99px;
  background: oklch(1 0 0);
  box-shadow: 0 2px 7px oklch(0.28 0.03 40/.3);
  transition: transform .28s cubic-bezier(.65,0,.35,1);
}

.div-05__cb:checked+.div-05__track {
  background: var(--div-05-acc);
}

.div-05__cb:checked+.div-05__track .div-05__knob {
  transform: translateX(22px);
}

.div-05__cb:focus-visible+.div-05__track {
  outline: 2px solid var(--div-05-acc);
  outline-offset: 3px;
}

.div-05__tlab {
  font-size: 14px;
  font-weight: 600;
}

.div-05__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--div-05-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.28 0.03 40/.16);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .div-05 * {
    transition-duration: .01ms !important;
  }
}
```
