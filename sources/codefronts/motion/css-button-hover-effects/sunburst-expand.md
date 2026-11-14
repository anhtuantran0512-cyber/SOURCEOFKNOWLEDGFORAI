---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/sunburst-expand/"
title: "Sunburst Expand"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A warm radiant CTA where a glow blooms from the centre on hover — a radial burst of light scales outward to flood the button, like a sunrise (an opaque…"
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sunburst Expand
Source: https://codefronts.com/motion/css-button-hover-effects/sunburst-expand/

A warm radiant CTA where a glow blooms from the centre on hover — a radial burst of light scales outward to flood the button, like a sunrise (an opaque flood, distinct from topic 28's fading ring).
## HTML
```html
<div class="bhe-34-group">
<section class="bhe-34a" aria-label="Sunburst expand button">
  <button class="bhe-34a__btn" type="button"><span class="bhe-34a__label">Start today</span></button>
</section>
<section class="bhe-34b" aria-label="Radial rays button">
  <button class="bhe-34b__btn" type="button"><span class="bhe-34b__rays" aria-hidden="true"></span><span class="bhe-34b__label">Shine</span></button>
</section>
</div>
```
## CSS
```css
.bhe-34-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-34-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-34a,
.bhe-34a *,
.bhe-34a *::before,
.bhe-34a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-34a {
  --warm: oklch(0.78 0.16 65);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #1a1206;
}

.bhe-34a__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  padding: 17px 44px;
  border: 1px solid color-mix(in oklab,var(--warm) 60%,transparent);
  border-radius: 9999px;
  cursor: pointer;
  background: color-mix(in oklab,var(--warm) 22%,#1a1206);
  transition: color .3s;
}

.bhe-34a__label {
  position: relative;
  z-index: 1;
  transition: text-shadow .3s;
}

.bhe-34a__btn::before {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 100%;
  height: 100%;
  transform: translate(-50%,-50%) scale(0);
  background: radial-gradient(circle,var(--warm) 0%,color-mix(in oklab,var(--warm) 70%,transparent) 45%,transparent 70%);
  transition: transform .5s cubic-bezier(.2,.9,.2,1);
  z-index: 0;
}

.bhe-34a__btn:hover::before,
.bhe-34a__btn:focus-visible::before {
  transform: translate(-50%,-50%) scale(2.4);
}

.bhe-34a__btn:hover .bhe-34a__label,
.bhe-34a__btn:focus-visible .bhe-34a__label {
  text-shadow: 0 0 12px rgba(255,240,210,.8);
}

.bhe-34a__btn:focus-visible {
  outline: 3px solid var(--warm);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-34a__btn::before {
    transition: none;
  }

  .bhe-34a__btn:hover::before,
    .bhe-34a__btn:focus-visible::before {
    transform: translate(-50%,-50%) scale(2.4);
  }
}

.bhe-34b,
.bhe-34b *,
.bhe-34b *::before,
.bhe-34b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-34b {
  --warm: oklch(0.82 0.16 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #171205;
}

.bhe-34b__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: #1a1206;
  padding: 17px 46px;
  border: none;
  border-radius: 9999px;
  cursor: pointer;
  background: var(--warm);
}

.bhe-34b__label {
  position: relative;
  z-index: 1;
}

.bhe-34b__rays {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 200%;
  aspect-ratio: 1;
  transform: translate(-50%,-50%) scale(0) rotate(0deg);
  background: repeating-conic-gradient(from 0deg,rgba(255,255,255,.5) 0deg 6deg,transparent 6deg 18deg);
  opacity: 0;
  transition: transform .6s cubic-bezier(.2,.9,.2,1),opacity .6s;
  z-index: 0;
}

.bhe-34b__btn:hover .bhe-34b__rays,
.bhe-34b__btn:focus-visible .bhe-34b__rays {
  transform: translate(-50%,-50%) scale(1) rotate(30deg);
  opacity: .6;
}

.bhe-34b__btn:focus-visible {
  outline: 3px solid #1a1206;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-34b__rays {
    transition: opacity .2s;
  }

  .bhe-34b__btn:hover .bhe-34b__rays,
    .bhe-34b__btn:focus-visible .bhe-34b__rays {
    transform: translate(-50%,-50%) scale(1);
    opacity: .4;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
