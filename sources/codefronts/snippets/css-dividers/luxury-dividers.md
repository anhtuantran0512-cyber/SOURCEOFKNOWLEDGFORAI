---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/luxury-dividers/"
title: "Luxury Minimalist Gold Accent HR Line CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "Luxury on the web is mostly restraint plus one exact detail."
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Luxury Minimalist Gold Accent HR Line CSS
Source: https://codefronts.com/snippets/css-dividers/luxury-dividers/

Luxury on the web is mostly restraint plus one exact detail. This divider is a 1px hairline, a 44px gold accent segment, and an enormous amount of air — with the accent segment animating in on a slow cubic curve. The measurable trick is using a fractional height with a device-pixel-ratio media query so the hairline is genuinely 1 physical pixel on retina, not a fuzzy 2.
## HTML
```html
<section class="div-14" aria-label="Luxury minimalist gold hr divider demo">
  <div class="div-14__stage">
    <p class="div-14__brand">MAISON&nbsp;&nbsp;CF</p>
    <hr class="div-14__rule">
    <h2 class="div-14__title">Atelier Collection</h2>
    <p class="div-14__sub">Nine pieces. Hand-finished. Released once a year.</p>
    <hr class="div-14__rule div-14__rule--wide">
    <div class="div-14__meta">
      <span>EST. 1974</span><span class="div-14__dot" aria-hidden="true"></span><span>PARIS</span><span class="div-14__dot" aria-hidden="true"></span><span>NO. 09</span>
    </div>
    <p class="div-14__chip">1px hairline · .5px at 2dppx · 44px gold segment</p>
  </div>
</section>
```
## CSS
```css
.div-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-14-bg);
  --div-14-bg: oklch(0.978 0.006 85);
  --div-14-ink: oklch(0.23 0.012 60);
  --div-14-mut: oklch(0.56 0.014 60);
  --div-14-line: color-mix(in oklch,var(--div-14-ink) 16%,transparent);
  --div-14-gold: oklch(0.74 0.1 84);
  --div-14-seg: 44px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-14-ink);
}

.div-14 *,
.div-14 *::before,
.div-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-14__stage {
  min-height: 100svh;
  width: min(92vw,620px);
  margin-inline: auto;
  display: grid;
  align-content: center;
  justify-items: center;
  text-align: center;
  padding: clamp(32px,6vw,80px) 0;
}

.div-14__brand {
  font-size: 12px;
  letter-spacing: .42em;
  text-indent: .42em;
  color: var(--div-14-mut);
  font-weight: 600;
}

.div-14__rule {
  width: 100%;
  border: 0;
  height: 1px;
  background: var(--div-14-line);
  position: relative;
  margin-block: clamp(30px,6.5vw,74px);
}

.div-14__rule::after {
  content: '';
  position: absolute;
  left: 50%;
  top: 50%;
  translate: -50% -50%;
  width: var(--div-14-seg);
  height: 2px;
  background: var(--div-14-gold);
  transform-origin: 50% 50%;
  animation: div-14-reveal 1.2s cubic-bezier(.16,1,.3,1) both;
}

.div-14__rule--wide::after {
  width: calc(var(--div-14-seg) * 2.4);
  height: 1px;
  animation-delay: .25s;
}

@keyframes div-14-reveal {
  from {
    scale: 0 1;
    opacity: 0;
  }

  to {
    scale: 1 1;
    opacity: 1;
  }
}

@media (min-resolution: 2dppx) {
  .div-14__rule {
    height: .5px;
  }
}

.div-14__title {
  font-family: Georgia,'Iowan Old Style',serif;
  font-size: clamp(30px,6.4vw,62px);
  line-height: 1.04;
  letter-spacing: .005em;
  font-weight: 400;
}

.div-14__sub {
  margin-top: 16px;
  font-size: clamp(13.5px,1.7vw,16px);
  line-height: 1.7;
  color: var(--div-14-mut);
  letter-spacing: .03em;
}

.div-14__meta {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
  flex-wrap: wrap;
  font-size: 10.5px;
  letter-spacing: .28em;
  color: var(--div-14-mut);
}

.div-14__dot {
  width: 3px;
  height: 3px;
  border-radius: 99px;
  background: var(--div-14-gold);
}

.div-14__chip {
  margin-top: clamp(26px,5vw,54px);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-14-mut);
  padding: 8px 14px;
  border: 1px solid var(--div-14-line);
  border-radius: 99px;
  letter-spacing: .02em;
}

@media (prefers-reduced-motion: reduce) {
  .div-14__rule::after {
    animation: none;
  }
}
```
