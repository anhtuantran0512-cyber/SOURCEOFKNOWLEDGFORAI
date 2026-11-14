---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/css-gradient-button-hover-effect/"
title: "CSS Gradient Button Hover Effect"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A side-by-side lab comparing the two production fixes for smooth gradient hovers — sliding an oversized background-position versus cross-fading a second…"
has_js: "false"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Button Hover Effect
Source: https://codefronts.com/components/css-gradient-buttons/css-gradient-button-hover-effect/

A side-by-side lab comparing the two production fixes for smooth gradient hovers — sliding an oversized background-position versus cross-fading a second gradient layer with opacity.
## HTML
```html
<div class="gb-06">
  <div class="gb-06__grid">
    <div class="gb-06__cell">
      <span class="gb-06__tag">Technique A</span>
      <button class="gb-06__btn gb-06__btn--shift" type="button">Join the beta</button>
      <p class="gb-06__desc">Oversized gradient, animated <code>background-position</code> — the classic smooth-shift fix.</p>
    </div>
    <div class="gb-06__cell">
      <span class="gb-06__tag">Technique B</span>
      <button class="gb-06__btn gb-06__btn--fade" type="button">Join the beta</button>
      <p class="gb-06__desc">Second gradient cross-fades in via <code>opacity</code> on a pseudo-element layer.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.gb-06,
.gb-06 *,
.gb-06 *::before,
.gb-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-06 ::selection {
  background: #818cf8;
  color: #0a0e1f;
}

.gb-06 {
  --aurora-a: #38bdf8;
  --aurora-b: #818cf8;
  --aurora-c: #e879f9;
  --dusk-a: #f97316;
  --dusk-b: #db2777;
  --bg: #0a0e1f;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.gb-06__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(230px,1fr));
  gap: 22px;
  width: 100%;
  max-width: 560px;
}

.gb-06__cell {
  background: #101631;
  border: 1px solid rgba(255,255,255,.06);
  border-radius: 18px;
  padding: 30px 26px;
  text-align: center;
}

.gb-06__tag {
  display: inline-block;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 1.8px;
  text-transform: uppercase;
  color: #8b93b8;
  margin-bottom: 20px;
}
/* Technique A — background-position shift. background-image itself
   can't transition, but sliding an oversized gradient can. */

.gb-06__btn {
  width: 100%;
  padding: 15px 26px;
  border: none;
  border-radius: 12px;
  font-family: inherit;
  font-size: 15px;
  font-weight: 700;
  color: #fff;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.gb-06__btn--shift {
  background-image: linear-gradient(100deg,var(--aurora-a),var(--aurora-b) 40%,var(--aurora-c) 80%,var(--aurora-a));
  background-size: 250% auto;
  background-position: left center;
  transition: background-position .55s ease,box-shadow .4s ease;
  box-shadow: 0 8px 22px -10px rgba(56,189,248,.6);
}

.gb-06__btn--shift:hover {
  background-position: right center;
  box-shadow: 0 10px 26px -10px rgba(232,121,249,.65);
}
/* Technique B — opacity cross-fade. Base gradient on the button,
   second gradient on ::before fading in. Opacity = compositor-only. */

.gb-06__btn--fade {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  background-image: linear-gradient(100deg,var(--aurora-b),var(--aurora-a));
  box-shadow: 0 8px 22px -10px rgba(129,140,248,.6);
  transition: box-shadow .4s ease;
}

.gb-06__btn--fade::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: inherit;
  background-image: linear-gradient(100deg,var(--dusk-a),var(--dusk-b));
  opacity: 0;
  transition: opacity .5s ease;
}

.gb-06__btn--fade:hover::before {
  opacity: 1;
}

.gb-06__btn--fade:hover {
  box-shadow: 0 10px 26px -10px rgba(219,39,119,.65);
}

.gb-06__btn:active {
  transform: scale(.98);
}

.gb-06__btn:focus-visible {
  outline: 3px solid var(--aurora-b);
  outline-offset: 3px;
}

.gb-06__desc {
  margin-top: 16px;
  font-size: 12.5px;
  line-height: 1.55;
  color: #5d6690;
}

.gb-06__desc code {
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: 11px;
  color: #a5b4fc;
  background: rgba(129,140,248,.12);
  padding: 1px 5px;
  border-radius: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .gb-06__btn--shift,
    .gb-06__btn--fade,
    .gb-06__btn--fade::before {
    transition: none;
  }
}
```
