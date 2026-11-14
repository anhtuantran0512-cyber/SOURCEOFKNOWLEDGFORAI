---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/glassmorphic/"
title: "Glassmorphism Pill Badge Effect"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "Glass that actually reads as glass — not gray soup."
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Pill Badge Effect
Source: https://codefronts.com/snippets/css-tags-chips/glassmorphic/

Glass that actually reads as glass — not gray soup. The recipe is four layers, each doing one job: a low-alpha white fill, backdrop-filter blur(14px) saturate(1.6) so colors behind intensify instead of dying, a 1px top-edge highlight faking caught light, and a soft drop shadow separating pane from photo. Light and dark glass variants share the recipe with flipped alphas, and every pill is proven on the one surface that breaks fake glass: a real photograph.
## HTML
```html
<section class="ctc-11" aria-label="Glassmorphism pill badge demo">
  <div class="ctc-11__stage">
    <div class="ctc-11__wrap">
      <header class="ctc-11__head">
        <p class="ctc-11__kicker">Glassmorphism · blur + saturate + caught light</p>
        <h1>Four layers make glass</h1>
      </header>
      <figure class="ctc-11__photo">
        <div class="ctc-11__pills">
          <span class="ctc-11__pill"><i class="ctc-11__dot"></i>Now boarding</span>
          <span class="ctc-11__pill">Alpine Loop · 4 days</span>
          <span class="ctc-11__pill ctc-11__pill--dark">From $1,290</span>
          <button class="ctc-11__pill ctc-11__pill--btn" type="button">Save trip<i class="ctc-11__plus" aria-hidden="true"></i></button>
        </div>
        <figcaption class="ctc-11__card">
          <div><b>Dolomites traverse</b><small>Cortina d'Ampezzo → Val Gardena</small></div>
          <span class="ctc-11__pill ctc-11__pill--sm">4.9 ★</span>
        </figcaption>
      </figure>
      <div class="ctc-11__grid">
        <div class="ctc-11__cell ctc-11__cell--light">
          <p>Light glass · <code>oklch(1 0 0/.16)</code> fill</p>
          <div class="ctc-11__row">
            <span class="ctc-11__pill">Editors' pick</span>
            <span class="ctc-11__pill"><i class="ctc-11__dot"></i>3 spots left</span>
          </div>
        </div>
        <div class="ctc-11__cell ctc-11__cell--dark">
          <p>Dark glass · flipped alphas</p>
          <div class="ctc-11__row">
            <span class="ctc-11__pill ctc-11__pill--dark">Night mode</span>
            <span class="ctc-11__pill ctc-11__pill--dark">21:40 departure</span>
          </div>
        </div>
      </div>
      <p class="ctc-11__note">The pane is <code>blur(14px) saturate(1.6)</code> — the saturate half keeps the photo's color alive through the glass. The 1px inset white top edge is the light a real pane catches.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-11,
.ctc-11 *,
.ctc-11 *::before,
.ctc-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-11 {
  --bg: oklch(0.22 0.03 260);
  --ink: oklch(0.96 0.005 260);
  --mut: oklch(0.72 0.02 260);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-11__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(75cqi 60cqi at 85% -12%,oklch(0.4 0.1 300/.5),transparent 62%),radial-gradient(60cqi 50cqi at -8% 112%,oklch(0.38 0.09 220/.5),transparent 60%),var(--bg);
  container: ctc11/inline-size;
}

.ctc-11__wrap {
  width: min(720px,100%);
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.ctc-11__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.8 0.1 220);
}

.ctc-11__head h1 {
  font-size: clamp(24px,3.8cqi,38px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin: 8px 0 4px;
}

.ctc-11__photo {
  position: relative;
  min-height: 300px;
  border-radius: 22px;
  overflow: clip;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 18px;
  background-image: url(https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1200&q=60),linear-gradient(150deg,oklch(0.7 0.1 230),oklch(0.45 0.12 280));
  background-size: cover;
  background-position: center;
}

.ctc-11__pills {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: flex-start;
}

.ctc-11__pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 18px;
  border-radius: 99px;
  font-size: 13.5px;
  font-weight: 700;
  color: oklch(0.16 0.02 260);
  text-shadow: 0 1px 2px oklch(1 0 0/.35);
  background: oklch(1 0 0/.16);
  -webkit-backdrop-filter: blur(14px) saturate(1.6);
  backdrop-filter: blur(14px) saturate(1.6);
  border: 1px solid oklch(1 0 0/.32);
  box-shadow: inset 0 1px 0 oklch(1 0 0/.45),0 8px 24px oklch(0 0 0/.18);
  transition: background .25s,translate .2s,box-shadow .25s;
}

@supports not (backdrop-filter: blur(1px)) {
  .ctc-11__pill {
    background: oklch(0.96 0.005 260/.88);
    text-shadow: none;
  }
}

.ctc-11__pill--dark {
  color: oklch(0.97 0.005 260);
  text-shadow: 0 1px 3px oklch(0 0 0/.45);
  background: oklch(0.15 0.02 260/.35);
  border-color: oklch(1 0 0/.14);
  box-shadow: inset 0 1px 0 oklch(1 0 0/.12),0 8px 24px oklch(0 0 0/.28);
}

@supports not (backdrop-filter: blur(1px)) {
  .ctc-11__pill--dark {
    background: oklch(0.2 0.02 260/.92);
  }
}

.ctc-11__pill--btn {
  cursor: pointer;
  font: inherit;
  font-size: 13.5px;
  font-weight: 800;
}

.ctc-11__pill--btn:hover,
.ctc-11__pill--btn:focus-visible {
  background: oklch(1 0 0/.3);
  translate: 0 -2px;
  box-shadow: inset 0 1px 0 oklch(1 0 0/.55),0 12px 28px oklch(0 0 0/.24);
}

.ctc-11__pill--btn:focus-visible {
  outline: 2px solid oklch(1 0 0/.9);
  outline-offset: 2px;
}

.ctc-11__pill--sm {
  min-height: 36px;
  padding: 0 13px;
  font-size: 12.5px;
}

.ctc-11__dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: oklch(0.75 0.19 148);
  box-shadow: 0 0 0 3px oklch(0.75 0.19 148/.3);
}

.ctc-11__plus {
  position: relative;
  width: 16px;
  height: 16px;
}

.ctc-11__plus::before,
.ctc-11__plus::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 11px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  translate: -50% -50%;
}

.ctc-11__plus::after {
  rotate: 90deg;
}

.ctc-11__card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 13px 16px;
  border-radius: 16px;
  color: oklch(0.16 0.02 260);
  background: oklch(1 0 0/.18);
  -webkit-backdrop-filter: blur(16px) saturate(1.5);
  backdrop-filter: blur(16px) saturate(1.5);
  border: 1px solid oklch(1 0 0/.35);
  box-shadow: inset 0 1px 0 oklch(1 0 0/.45),0 10px 30px oklch(0 0 0/.2);
}

@supports not (backdrop-filter: blur(1px)) {
  .ctc-11__card {
    background: oklch(0.96 0.005 260/.9);
  }
}

.ctc-11__card b {
  display: block;
  font-size: 14.5px;
  font-weight: 800;
}

.ctc-11__card small {
  font-size: 12px;
  opacity: .75;
}

.ctc-11__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.ctc-11__cell {
  border-radius: 18px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  background-size: cover;
  background-position: center;
}

.ctc-11__cell p {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .1em;
  text-transform: uppercase;
}

.ctc-11__cell code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .95em;
  letter-spacing: 0;
  text-transform: none;
}

.ctc-11__cell--light {
  background-image: url(https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=800&q=60),linear-gradient(140deg,oklch(0.75 0.1 150),oklch(0.55 0.1 200));
  color: oklch(0.98 0 0);
  text-shadow: 0 1px 4px oklch(0 0 0/.4);
}

.ctc-11__cell--dark {
  background-image: url(https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=800&q=60),linear-gradient(140deg,oklch(0.35 0.08 260),oklch(0.2 0.04 280));
  color: oklch(0.98 0 0);
  text-shadow: 0 1px 4px oklch(0 0 0/.4);
}

.ctc-11__row {
  display: flex;
  flex-wrap: wrap;
  gap: 9px;
}

.ctc-11__note {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  border-left: 3px solid oklch(0.8 0.1 220);
  padding-left: 12px;
}

.ctc-11__note code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: oklch(1 0 0/.1);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

@container ctc11 (width < 560px) {
  .ctc-11__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ctc-11 * {
    transition-duration: .01ms !important;
  }
}
```
