---
source: "codefronts"
url: "https://codefronts.com/snippets/css-blockquotes/drop-shadow-float/"
title: "Floating CSS Blockquote with Drop Shadow"
section: "snippets"
category: "css-blockquotes"
category_name: "CSS Blockquotes"
description: "Why professional shadows never look like box-shadow: 0 4px 8px rgba(0,0,0,.3): real elevation is a stack. This card layers five shadows whose offsets and…"
has_js: "false"
---

Here's a working CSS Blockquote from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating CSS Blockquote with Drop Shadow
Source: https://codefronts.com/snippets/css-blockquotes/drop-shadow-float/

Why professional shadows never look like box-shadow: 0 4px 8px rgba(0,0,0,.3): real elevation is a stack. This card layers five shadows whose offsets and blurs follow a geometric ramp (1,2,4,8,16px) with alphas that decay as they spread — the ambient-plus-key model real light produces. The card breathes between two elevation levels on hover, a decorative quote mark floats on its own higher layer, and an elevation ruler beside the card shows the same stack at three intensities so you can calibrate your own scale.
## HTML
```html
<section class="bq-17" aria-label="Floating blockquote with layered drop shadow demo">
  <div class="bq-17__stage">
    <div class="bq-17__row">
      <figure class="bq-17__card" tabindex="0">
        <span class="bq-17__mark" aria-hidden="true">“</span>
        <blockquote>
          <p>Depth is information. A shadow tells the eye what is interactive, what is modal, and what is furniture — before a single word is read.</p>
        </blockquote>
        <figcaption class="bq-17__by"><strong>Field Guide to Interface Light</strong> · ch. 3, Elevation</figcaption>
      </figure>
      <div class="bq-17__ruler" aria-hidden="true">
        <div class="bq-17__lvl bq-17__lvl--1"><span>e1 · resting</span></div>
        <div class="bq-17__lvl bq-17__lvl--2"><span>e2 · raised</span></div>
        <div class="bq-17__lvl bq-17__lvl--3"><span>e3 · floating</span></div>
      </div>
    </div>
    <p class="bq-17__chip" aria-hidden="true">5-layer 1→16px ramp · hue-tinted shadow · ::after opacity hover</p>
  </div>
</section>
```
## CSS
```css
.bq-17,
.bq-17 *,
.bq-17 *::before,
.bq-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bq-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --bg: oklch(0.955 0.008 255);
  --card: oklch(1 0 0);
  --ink: oklch(0.27 0.02 260);
  --mut: oklch(0.53 0.02 260);
  --acc: oklch(0.55 0.15 265);
  --sh: 0.2 0.02 260;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.bq-17__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(20px,5vw,56px);
  background: linear-gradient(160deg,oklch(0.97 0.006 250),var(--bg));
  overflow-y: auto;
}

.bq-17__row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: clamp(24px,4vw,48px);
}

.bq-17__card {
  position: relative;
  width: min(100%,440px);
  padding: 30px 32px 26px;
  border-radius: 20px;
  background: var(--card);
  box-shadow: 0 1px 1px oklch(var(--sh)/.05),0 2px 2px oklch(var(--sh)/.05),0 4px 4px oklch(var(--sh)/.06),0 8px 8px oklch(var(--sh)/.06),0 16px 24px oklch(var(--sh)/.08);
  transition: translate .3s cubic-bezier(.2,.7,.2,1);
}

.bq-17__card::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  box-shadow: 0 2px 2px oklch(var(--sh)/.06),0 4px 4px oklch(var(--sh)/.06),0 8px 8px oklch(var(--sh)/.07),0 16px 16px oklch(var(--sh)/.07),0 32px 44px oklch(var(--sh)/.12);
  opacity: 0;
  transition: opacity .3s;
  pointer-events: none;
  z-index: -1;
}

.bq-17__card:hover,
.bq-17__card:focus-visible {
  translate: 0 -6px;
}

.bq-17__card:hover::after,
.bq-17__card:focus-visible::after {
  opacity: 1;
}

.bq-17__card:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.bq-17__mark {
  position: absolute;
  top: -22px;
  left: 24px;
  display: grid;
  place-items: center;
  width: 48px;
  height: 48px;
  border-radius: 14px;
  background: var(--acc);
  color: oklch(0.98 0.005 265);
  font-family: Georgia,serif;
  font-size: 34px;
  line-height: 0;
  padding-top: 14px;
  box-shadow: 0 2px 3px oklch(var(--sh)/.15),0 8px 16px oklch(var(--sh)/.2);
}

.bq-17__card blockquote p {
  font-size: 16.5px;
  line-height: 1.66;
  text-wrap: pretty;
  margin-top: 8px;
}

.bq-17__by {
  margin-top: 16px;
  font-size: 12.5px;
  color: var(--mut);
}

.bq-17__by strong {
  color: var(--ink);
  font-weight: 650;
}

.bq-17__ruler {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.bq-17__lvl {
  display: grid;
  place-items: center;
  width: 150px;
  height: 52px;
  border-radius: 12px;
  background: var(--card);
}

.bq-17__lvl span {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  color: var(--mut);
}

.bq-17__lvl--1 {
  box-shadow: 0 1px 1px oklch(var(--sh)/.06),0 2px 3px oklch(var(--sh)/.07);
}

.bq-17__lvl--2 {
  box-shadow: 0 1px 1px oklch(var(--sh)/.05),0 3px 4px oklch(var(--sh)/.06),0 8px 12px oklch(var(--sh)/.08);
}

.bq-17__lvl--3 {
  box-shadow: 0 1px 1px oklch(var(--sh)/.05),0 4px 4px oklch(var(--sh)/.06),0 8px 10px oklch(var(--sh)/.07),0 20px 32px oklch(var(--sh)/.12);
}

.bq-17__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--mut);
  padding: 7px 13px;
  border: 1px solid oklch(0 0 0/.09);
  border-radius: 99px;
  background: var(--card);
}

@media (prefers-reduced-motion: reduce) {
  .bq-17 * {
    transition-duration: .01ms !important;
  }
}
```
