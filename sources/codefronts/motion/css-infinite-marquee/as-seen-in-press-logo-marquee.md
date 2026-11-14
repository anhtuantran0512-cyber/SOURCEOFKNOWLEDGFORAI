---
source: "codefronts"
url: "https://codefronts.com/motion/css-infinite-marquee/as-seen-in-press-logo-marquee/"
title: "\"As Seen In\" Press Logo Marquee (Pure CSS, Seamless Loop)"
section: "motion"
category: "css-infinite-marquee"
category_name: "CSS Infinite Marquee Designs"
description: "The classic trust-builder under a hero section: a grayscale press-logo strip that scrolls forever with zero JavaScript, fades out at both edges with a CSS…"
has_js: "false"
---

Here's a working CSS Infinite Marquee Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: "As Seen In" Press Logo Marquee (Pure CSS, Seamless Loop)
Source: https://codefronts.com/motion/css-infinite-marquee/as-seen-in-press-logo-marquee/

The classic trust-builder under a hero section: a grayscale press-logo strip that scrolls forever with zero JavaScript, fades out at both edges with a CSS mask, wakes to full color on hover, and ships a real WCAG-compliant pause button wired entirely with :has() — the exact pattern SaaS landing pages use for 'as seen in Forbes / TechCrunch' bars.
## HTML
```html
<section class="mqs-01" aria-label="As seen in press logo marquee demo">
  <div class="mqs-01__inner">
    <div class="mqs-01__head">
      <p class="mqs-01__eyebrow">As seen in</p>
      <input class="mqs-01__pauseBox" type="checkbox" id="mqs-01-pause">
      <label class="mqs-01__pauseBtn" for="mqs-01-pause"><span class="mqs-01__pauseIcon" aria-hidden="true"></span><span class="mqs-01__pauseTxt">Pause</span><span class="mqs-01__playTxt">Play</span></label>
    </div>
    <div class="mqs-01__viewport">
      <div class="mqs-01__group">
        <span class="mqs-01__logo mqs-01__logo--serif">The Daily Ledger</span>
        <span class="mqs-01__logo mqs-01__logo--caps">TECHWIRE</span>
        <span class="mqs-01__logo mqs-01__logo--script">Founder Weekly</span>
        <span class="mqs-01__logo mqs-01__logo--mono">signal_</span>
        <span class="mqs-01__logo mqs-01__logo--serif">Morning Brief</span>
        <span class="mqs-01__logo mqs-01__logo--caps">PRODUCT POST</span>
      </div>
      <div class="mqs-01__group" aria-hidden="true">
        <span class="mqs-01__logo mqs-01__logo--serif">The Daily Ledger</span>
        <span class="mqs-01__logo mqs-01__logo--caps">TECHWIRE</span>
        <span class="mqs-01__logo mqs-01__logo--script">Founder Weekly</span>
        <span class="mqs-01__logo mqs-01__logo--mono">signal_</span>
        <span class="mqs-01__logo mqs-01__logo--serif">Morning Brief</span>
        <span class="mqs-01__logo mqs-01__logo--caps">PRODUCT POST</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.mqs-01,
.mqs-01 *,
.mqs-01 *::before,
.mqs-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.mqs-01 {
  min-height: 100vh;
  width: 100%;
  --gap: 64px;
  --speed: 28s;
  --ink: #1c1917;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #faf9f7;
  padding: 64px 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.mqs-01__inner {
  width: min(920px,100%);
}

.mqs-01__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 26px;
}

.mqs-01__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: #a8a29e;
}

.mqs-01__pauseBox {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.mqs-01__pauseBtn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  font-weight: 600;
  color: #78716c;
  border: 1px solid #e7e5e4;
  border-radius: 999px;
  padding: 6px 14px;
  cursor: pointer;
  user-select: none;
  transition: border-color .15s,color .15s;
}

.mqs-01__pauseBtn:hover {
  border-color: #a8a29e;
  color: var(--ink);
}

.mqs-01__pauseBox:focus-visible + .mqs-01__pauseBtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.mqs-01__pauseIcon {
  width: 8px;
  height: 10px;
  border-inline: 2.5px solid currentColor;
}

.mqs-01__playTxt {
  display: none;
}

.mqs-01:has(.mqs-01__pauseBox:checked) .mqs-01__pauseTxt {
  display: none;
}

.mqs-01:has(.mqs-01__pauseBox:checked) .mqs-01__playTxt {
  display: inline;
}

.mqs-01:has(.mqs-01__pauseBox:checked) .mqs-01__pauseIcon {
  border-inline: none;
  border-left: 9px solid currentColor;
  border-block: 5px solid transparent;
  width: 0;
  height: 0;
}

.mqs-01__viewport {
  display: flex;
  gap: var(--gap);
  overflow: hidden;
  padding-block: 8px;
  mask-image: linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);
  -webkit-mask-image: linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);
}

.mqs-01__group {
  flex: none;
  display: flex;
  align-items: center;
  gap: var(--gap);
  animation: mqs-01-scroll var(--speed) linear infinite;
  will-change: transform;
}

@keyframes mqs-01-scroll {
  to {
    transform: translateX(calc(-100% - var(--gap)));
  }
}

.mqs-01__viewport:hover .mqs-01__group,
.mqs-01__viewport:focus-within .mqs-01__group,
.mqs-01:has(.mqs-01__pauseBox:checked) .mqs-01__group {
  animation-play-state: paused;
}

.mqs-01__logo {
  flex: none;
  font-size: 22px;
  color: var(--ink);
  filter: grayscale(1);
  opacity: .45;
  transition: filter .25s,opacity .25s;
  cursor: default;
}

.mqs-01__logo:hover {
  filter: grayscale(0);
  opacity: 1;
}

.mqs-01__logo--serif {
  font-family: Georgia,'Times New Roman',serif;
  font-weight: 700;
  letter-spacing: -.01em;
}

.mqs-01__logo--caps {
  font-weight: 800;
  font-size: 18px;
  letter-spacing: .14em;
}

.mqs-01__logo--script {
  font-family: Georgia,serif;
  font-style: italic;
  font-weight: 600;
  color: #7c2d12;
}

.mqs-01__logo--mono {
  font-family: ui-monospace,'Cascadia Code',Menlo,monospace;
  font-weight: 700;
  color: #365314;
}

@media (prefers-reduced-motion: reduce) {
  .mqs-01__group {
    animation: none;
  }

  .mqs-01__viewport {
    overflow-x: auto;
    mask-image: none;
    -webkit-mask-image: none;
  }

  .mqs-01__logo {
    filter: none;
    opacity: .8;
  }

  .mqs-01__pauseBtn {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the loop is two identical flex groups each translated by calc(-100% - var(--gap)); the pause button is a checkbox read with :has(:checked). */
```
