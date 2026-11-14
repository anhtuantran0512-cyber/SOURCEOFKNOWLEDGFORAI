---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/aurora-drift/"
title: "Aurora Drift Accordion — Dark Ambient Glow that Follows the Open Item"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "The collection's closer: a deep-night page where a soft aurora blob drifts perpetually behind frosted items — and when you open a section, the glow gathers…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Aurora Drift Accordion — Dark Ambient Glow that Follows the Open Item
Source: https://codefronts.com/navigation/css-accordions/aurora-drift/

The collection's closer: a deep-night page where a soft aurora blob drifts perpetually behind frosted items — and when you open a section, the glow gathers AROUND it, blooming through the glass while the item lifts gently. Ambient, slow and atmospheric: for meditation apps, night-mode products and premium 'calm tech' brands.
## HTML
```html
<section class="acc-32" aria-label="Aurora drift ambient accordion demo">
  <div class="acc-32__sky">
    <div class="acc-32__wrap">
      <p class="acc-32__kicker">Drift · evening practice</p>
      <h3 class="acc-32__title">Tonight's session</h3>
      <details class="acc-32__item" style="--halo:oklch(0.7 0.19 300 / .35)" open>
        <summary class="acc-32__sum">Settling in<span class="acc-32__min">4 min</span></summary>
        <div class="acc-32__body"><p>Find the position you'd choose if no one was watching. We begin with three unhurried breaths and permission to do this badly.</p></div>
      </details>
      <details class="acc-32__item" style="--halo:oklch(0.72 0.17 220 / .35)">
        <summary class="acc-32__sum">Body weather<span class="acc-32__min">9 min</span></summary>
        <div class="acc-32__body"><p>A slow scan from crown to heels, noting sensation the way you'd note weather — present, passing, none of it a problem.</p></div>
      </details>
      <details class="acc-32__item" style="--halo:oklch(0.75 0.15 160 / .35)">
        <summary class="acc-32__sum">The long exhale<span class="acc-32__min">7 min</span></summary>
        <div class="acc-32__body"><p>Breath lengthens on its own once counted: in for four, out for six. The exhale is where the day is allowed to end.</p></div>
      </details>
      <details class="acc-32__item" style="--halo:oklch(0.8 0.12 90 / .3)">
        <summary class="acc-32__sum">Rest<span class="acc-32__min">5 min</span></summary>
        <div class="acc-32__body"><p>Nothing to follow now. The bell will find you in five minutes; until then the practice is only staying.</p></div>
      </details>
    </div>
  </div>
</section>
```
## CSS
```css
.acc-32,
.acc-32 *,
.acc-32 *::before,
.acc-32 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-32 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #0a0c14;
}

.acc-32__sky {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 44px 24px;
  overflow: hidden;
}

.acc-32__sky::before,
.acc-32__sky::after {
  content: "";
  position: absolute;
  width: 420px;
  height: 420px;
  border-radius: 50%;
  filter: blur(70px);
  pointer-events: none;
}

.acc-32__sky::before {
  background: radial-gradient(circle,oklch(0.55 0.2 300 / .4),transparent 70%);
  top: -10%;
  left: 5%;
  animation: acc-32-drift1 26s ease-in-out infinite alternate;
}

.acc-32__sky::after {
  background: radial-gradient(circle,oklch(0.6 0.16 200 / .35),transparent 70%);
  bottom: -15%;
  right: 0%;
  animation: acc-32-drift2 19s ease-in-out infinite alternate;
}

@keyframes acc-32-drift1 {
  to {
    translate: 40% 30%;
  }
}

@keyframes acc-32-drift2 {
  to {
    translate: -35% -25%;
  }
}

.acc-32__wrap {
  position: relative;
  z-index: 1;
  width: min(520px,100%);
}

.acc-32__kicker {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: rgba(255,255,255,.45);
}

.acc-32__title {
  font-size: 26px;
  font-weight: 750;
  color: rgba(255,255,255,.94);
  letter-spacing: -.01em;
  margin: 6px 0 20px;
}

.acc-32__item {
  position: relative;
  margin-bottom: 12px;
  transition: translate .5s cubic-bezier(.3,1,.4,1);
}

.acc-32__item::before {
  content: "";
  position: absolute;
  inset: -30px;
  background: radial-gradient(closest-side,var(--halo),transparent);
  scale: 0;
  opacity: 0;
  transition: scale .9s cubic-bezier(.2,.7,.3,1),opacity .9s;
  pointer-events: none;
  border-radius: 50%;
}

.acc-32__item[open] {
  translate: 0 -2px;
}

.acc-32__item[open]::before {
  scale: 1;
  opacity: 1;
}

.acc-32__sum {
  position: relative;
  z-index: 1;
  list-style: none;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  min-height: 58px;
  padding: 8px 20px;
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 14px;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  font-size: 16px;
  font-weight: 650;
  color: rgba(255,255,255,.92);
  cursor: pointer;
  transition: border-color .4s,background .4s;
}

@supports not (backdrop-filter: blur(1px)) {
  .acc-32__sum {
    background: rgba(20,23,38,.9);
  }
}

.acc-32__sum::-webkit-details-marker {
  display: none;
}

.acc-32__sum::marker {
  content: "";
}

.acc-32__sum:hover {
  border-color: rgba(255,255,255,.28);
}

.acc-32__item[open] .acc-32__sum {
  border-color: rgba(255,255,255,.3);
  background: rgba(255,255,255,.09);
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
}

.acc-32__min {
  font-size: 12px;
  font-weight: 600;
  color: rgba(255,255,255,.5);
  background: rgba(255,255,255,.08);
  padding: 4px 10px;
  border-radius: 99px;
  flex: none;
}

.acc-32__body {
  position: relative;
  z-index: 1;
  padding: 16px 20px 18px;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.12);
  border-top: none;
  border-radius: 0 0 14px 14px;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  font-size: 14.5px;
  line-height: 1.7;
  color: rgba(255,255,255,.72);
}

@supports not (backdrop-filter: blur(1px)) {
  .acc-32__body {
    background: rgba(20,23,38,.88);
  }
}

.acc-32__item[open] .acc-32__body {
  animation: acc-32-in .5s ease-out;
}

@keyframes acc-32-in {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

.acc-32__sum:focus-visible {
  outline: 3px solid rgba(255,255,255,.85);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-32__sky::before,
    .acc-32__sky::after {
    animation: none;
  }

  .acc-32__item,
    .acc-32__item::before {
    transition: opacity .3s;
  }

  .acc-32__item[open] .acc-32__body {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a global aurora drifts on two never-syncing loops while each item carries its own halo pseudo-element, scaled from 0 to bloom around whichever details is open. */
```
