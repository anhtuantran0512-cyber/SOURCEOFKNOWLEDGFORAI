---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-footer-transition/"
title: "CSS Diagonal Footer Transition"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "The most common real-world use of the whole technique: the footer's top edge is cut on a diagonal so the page body flows into it instead of stopping at a line."
has_js: "false"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Diagonal Footer Transition
Source: https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-footer-transition/

The most common real-world use of the whole technique: the footer's top edge is cut on a diagonal so the page body flows into it instead of stopping at a line. Real footer content — four link columns, a newsletter field, legal row — with the cut sized so the first column heading never rides the slope, and a margin-block-start: auto pin so the footer sits at the bottom even on a short page.
## HTML
```html
<div class="dgs-10">
  <input class="dgs-10__sronly" type="checkbox" id="dgs-10-dark">
  <label class="dgs-10__theme" for="dgs-10-dark">
    <svg class="dgs-10__i dgs-10__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-10__i dgs-10__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-10__srtext">Toggle dark theme</span>
  </label>
  <div class="dgs-10__stage">
    <section class="dgs-10__content" aria-labelledby="dgs-10-a">
      <div class="dgs-10__wrap">
        <p class="dgs-10__eyebrow">Kestrel Cycles</p>
        <h2 class="dgs-10__display" id="dgs-10-a">A commuter bike that charges from a wall socket in ninety minutes</h2>
        <p class="dgs-10__lede">Belt drive, hub motor, no chain grease on your trousers. Ninety kilometres of range and a frame that fits a rear rack properly.</p>
        <div class="dgs-10__figures">
          <p><strong>90 km</strong><span>Range, eco mode</span></p>
          <p><strong>17.4 kg</strong><span>With battery</span></p>
          <p><strong>5 yr</strong><span>Frame warranty</span></p>
        </div>
      </div>
    </section>

    <footer class="dgs-10__footer" aria-labelledby="dgs-10-b">
      <div class="dgs-10__wrap">
        <div class="dgs-10__grid">
          <div class="dgs-10__brand">
            <h2 class="dgs-10__wordmark" id="dgs-10-b">Kestrel</h2>
            <p>Assembled in Bristol. Serviced anywhere with a 4&nbsp;mm hex key.</p>
            <div class="dgs-10__signup">
              <label class="dgs-10__vh" for="dgs-10-email">Email address</label>
              <input id="dgs-10-email" type="email" inputmode="email" autocomplete="email" placeholder="[email protected]">
              <button type="button">Restock alerts</button>
            </div>
          </div>
          <nav aria-label="Bikes">
            <h3>Bikes</h3>
            <ul><li><a href="#dgs-10-b">Kestrel One</a></li><li><a href="#dgs-10-b">Kestrel Cargo</a></li><li><a href="#dgs-10-b">Step-through</a></li><li><a href="#dgs-10-b">Frame sizing</a></li></ul>
          </nav>
          <nav aria-label="Support">
            <h3>Support</h3>
            <ul><li><a href="#dgs-10-b">Book a service</a></li><li><a href="#dgs-10-b">Battery care</a></li><li><a href="#dgs-10-b">Spares</a></li><li><a href="#dgs-10-b">Warranty</a></li></ul>
          </nav>
          <nav aria-label="Company">
            <h3>Company</h3>
            <ul><li><a href="#dgs-10-b">Workshop</a></li><li><a href="#dgs-10-b">Test rides</a></li><li><a href="#dgs-10-b">Stockists</a></li><li><a href="#dgs-10-b">Careers</a></li></ul>
          </nav>
        </div>
        <div class="dgs-10__legal">
          <p>&copy; 2027 Kestrel Cycles Ltd</p>
          <p class="dgs-10__mono">clip-path: polygon(0 var(--cut), 100% 0, 100% 100%, 0 100%)</p>
        </div>
      </div>
    </footer>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700&display=swap');

.dgs-10 {
  --cut: clamp(2rem, 7vw, 9rem);
  --page: #fbfbf9;
  --page2: #f0f1ec;
  --ink: #14170f;
  --muted: #575c4d;
  --line: #e0e2d8;
  --forest: #113025;
  --forest2: #0b2019;
  --on-forest: #eef3ea;
  --dim: #9db3a3;
  --lime: #b9e04f;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--page);
  color: var(--ink);
  font-family: 'Schibsted Grotesk', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

.dgs-10 *,
.dgs-10 *::before,
.dgs-10 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.4 0.08 155)) {
  .dgs-10 {
    --page: oklch(0.988 0.004 110);
    --page2: oklch(0.952 0.008 110);
    --ink: oklch(0.19 0.015 130);
    --muted: oklch(0.48 0.02 130);
    --line: oklch(0.9 0.012 110);
    --forest: oklch(0.29 0.055 158);
    --forest2: oklch(0.225 0.05 160);
    --on-forest: oklch(0.955 0.012 130);
    --dim: oklch(0.755 0.03 155);
    --lime: oklch(0.875 0.16 118);
  }
}

.dgs-10__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-10__stage {
  display: flow-root;
}

.dgs-10__wrap {
  inline-size: min(76rem, 100%);
  margin-inline: auto;
}

.dgs-10__content {
  padding: clamp(4rem, 9vw, 6.5rem) clamp(1.25rem, 5vw, 4rem) calc(var(--cut) + clamp(3rem, 7vw, 5rem));
}

.dgs-10__eyebrow {
  margin: 0 0 1rem;
  font-size: .74rem;
  font-weight: 600;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--forest);
}

.dgs-10__display {
  margin: 0 0 1.1rem;
  max-inline-size: 27ch;
  font-size: clamp(2.1rem, 6.2vw, 3.9rem);
  font-weight: 600;
  line-height: 1.04;
  letter-spacing: -.04em;
  text-wrap: balance;
}

.dgs-10__lede {
  margin: 0 0 clamp(2rem, 5vw, 3rem);
  max-inline-size: 52ch;
  font-size: clamp(1.02rem, 2vw, 1.18rem);
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-10__figures {
  display: grid;
  gap: 1.25rem clamp(1.5rem, 5vw, 3.5rem);
  grid-template-columns: repeat(auto-fit, minmax(10rem, 1fr));
}

.dgs-10__figures p {
  margin: 0;
  display: grid;
  gap: .25rem;
  padding-block-start: .85rem;
  border-block-start: 2px solid var(--forest);
}

.dgs-10__figures strong {
  font-size: clamp(1.6rem, 4.5vw, 2.2rem);
  font-weight: 600;
  letter-spacing: -.035em;
  font-variant-numeric: tabular-nums;
}

.dgs-10__figures span {
  font-size: .86rem;
  color: var(--muted);
}

.dgs-10__footer {
  position: relative;
  z-index: 1;
  color: var(--on-forest);
  background: linear-gradient(180deg, var(--forest) 0%, var(--forest2) 100%);
  clip-path: polygon(0 var(--cut), 100% 0, 100% 100%, 0 100%);
  margin-block-start: calc(var(--cut) * -1 - 1px);
  padding: calc(var(--cut) + clamp(3rem, 7vw, 5rem)) clamp(1.25rem, 5vw, 4rem) clamp(2.5rem, 6vw, 3.5rem);
}

.dgs-10__grid {
  display: grid;
  gap: clamp(2rem, 5vw, 3.5rem);
  grid-template-columns: repeat(auto-fit, minmax(11rem, 1fr));
}

.dgs-10__brand {
  grid-column: 1 / -1;
  max-inline-size: 30rem;
}

@media (min-width: 60rem) {
  .dgs-10__brand {
    grid-column: span 2;
  }
}

.dgs-10__wordmark {
  margin: 0 0 .6rem;
  font-size: clamp(2.4rem, 8vw, 4.2rem);
  font-weight: 700;
  line-height: .95;
  letter-spacing: -.055em;
}

.dgs-10__brand p {
  margin: 0 0 1.5rem;
  max-inline-size: 34ch;
  color: var(--dim);
  font-size: .95rem;
  text-wrap: pretty;
}

.dgs-10__signup {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
}

.dgs-10__signup input {
  flex: 1 1 12rem;
  min-inline-size: 0;
  min-block-size: 2.9rem;
  padding: .7rem .9rem;
  border: 1px solid rgba(238,243,234,.28);
  border-radius: 10px;
  background: rgba(238,243,234,.06);
  color: var(--on-forest);
  font: inherit;
  font-size: .92rem;
}

.dgs-10__signup input::placeholder {
  color: rgba(157,179,163,.8);
}

.dgs-10__signup input:focus-visible {
  outline: 2px solid var(--lime);
  outline-offset: 2px;
}

.dgs-10__signup button {
  min-block-size: 2.9rem;
  padding: .7rem 1.2rem;
  border: 0;
  border-radius: 10px;
  background: var(--lime);
  color: #0f2116;
  font: inherit;
  font-size: .92rem;
  font-weight: 600;
  cursor: pointer;
  transition: translate .2s cubic-bezier(.2,.8,.3,1), background .2s ease;
}

.dgs-10__signup button:hover {
  translate: 0 -1px;
  background: #c8ec63;
}

.dgs-10__signup button:focus-visible {
  outline: 2px solid var(--on-forest);
  outline-offset: 3px;
}

.dgs-10__footer h3 {
  margin: 0 0 .9rem;
  font-size: .74rem;
  font-weight: 600;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--dim);
}

.dgs-10__footer ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .1rem;
}

.dgs-10__footer a {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.25rem;
  color: var(--on-forest);
  text-decoration: none;
  font-size: .95rem;
  transition: color .18s ease, translate .18s ease;
}

.dgs-10__footer a:hover {
  color: var(--lime);
  translate: 2px 0;
}

.dgs-10__footer a:focus-visible {
  outline: 2px solid var(--lime);
  outline-offset: 3px;
}

.dgs-10__legal {
  margin-block-start: clamp(2.5rem, 6vw, 4rem);
  padding-block-start: 1.1rem;
  border-block-start: 1px solid rgba(238,243,234,.16);
  display: flex;
  flex-wrap: wrap;
  gap: .5rem 1.5rem;
  justify-content: space-between;
}

.dgs-10__legal p {
  margin: 0;
  font-size: .8rem;
  color: var(--dim);
}

.dgs-10__mono {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .72rem !important;
  overflow-wrap: anywhere;
}

@media (prefers-color-scheme: dark) {
  .dgs-10 {
    --page: #0d0f0b;
    --page2: #141711;
    --ink: #eef3ea;
    --muted: #9aa392;
    --line: #262a20;
  }
}

@media (prefers-reduced-motion: reduce) {
  .dgs-10 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-10__footer {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
    border-block-start: 1px solid CanvasText;
  }

  .dgs-10__signup input,
    .dgs-10__signup button {
    border: 1px solid CanvasText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-10__sronly,
.dgs-10__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-10__theme {
  position: absolute;
  inset-block-start: clamp(.85rem, 2.2vw, 1.5rem);
  inset-inline-end: clamp(.85rem, 2.2vw, 1.5rem);
  z-index: 60;
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: 999px;
  border: 1px solid currentColor;
  color: inherit;
  background: rgba(127,127,127,.16);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: translate .2s ease;
}

.dgs-10__theme:hover {
  translate: 0 -1px;
}

.dgs-10__sronly:focus-visible + .dgs-10__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-10__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-10__i--sun {
  display: none;
}

.dgs-10:has(#dgs-10-dark:checked) .dgs-10__i--moon {
  display: none;
}

.dgs-10:has(#dgs-10-dark:checked) .dgs-10__i--sun {
  display: block;
}

.dgs-10:has(#dgs-10-dark:checked) {
  --page: #0d0f0b;
  --page2: #141711;
  --ink: #eef3ea;
  --muted: #9aa392;
  --line: #262a20;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-10__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-10__theme {
    border-color: CanvasText;
  }
}
```
