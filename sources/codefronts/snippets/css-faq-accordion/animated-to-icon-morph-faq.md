---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/animated-to-icon-morph-faq/"
title: "Animated + to − Icon Morph FAQ"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "The +/− morph elevated from \"vertical bar fades out\" to a piece of choreography: both bars of the plus rotate 180° together while the vertical bar's scale…"
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated + to − Icon Morph FAQ
Source: https://codefronts.com/snippets/css-faq-accordion/animated-to-icon-morph-faq/

The +/− morph elevated from "vertical bar fades out" to a piece of choreography: both bars of the plus rotate 180° together while the vertical bar's scale collapses, so the icon appears to twist itself into a minus. Built from two 2px pseudo-element bars — no SVG, no icon font — inside a tinted chip that swells on hover. Includes the overshoot variant (rotates past, settles back) and the reduced-motion story, because icon whimsy must never cost accessibility.
## HTML
```html
<section class="cfa-12" aria-label="Plus to minus icon morph FAQ">
  <div class="cfa-12__wrap">
    <header class="cfa-12__head">
      <h1>Studio FAQ</h1>
      <p>Watch the plus twist itself into a minus — both bars rotate, one collapses along its length.</p>
    </header>
    <div class="cfa-12__list">
      <div class="cfa-12__item">
        <input type="checkbox" id="cfa12-q1" class="cfa-12__cb" checked>
        <label class="cfa-12__q" for="cfa12-q1">Do you take on freelance projects?<i class="cfa-12__ic" aria-hidden="true"></i></label>
        <div class="cfa-12__a"><div><p>Selectively — two or three a quarter, usually brand systems or product design sprints. Send a short brief with timeline and budget range; we reply within two business days either way.</p></div></div>
      </div>
      <div class="cfa-12__item">
        <input type="checkbox" id="cfa12-q2" class="cfa-12__cb">
        <label class="cfa-12__q" for="cfa12-q2">What does a typical engagement cost?<i class="cfa-12__ic" aria-hidden="true"></i></label>
        <div class="cfa-12__a"><div><p>Sprints start at $12k for two weeks; full brand systems run $40–90k depending on scope. Fixed-price after discovery — we don't bill hours, so a slow Tuesday is our problem, not yours.</p></div></div>
      </div>
      <div class="cfa-12__item">
        <input type="checkbox" id="cfa12-q3" class="cfa-12__cb">
        <label class="cfa-12__q" for="cfa12-q3">Can we hire you to work inside our team?<i class="cfa-12__ic" aria-hidden="true"></i></label>
        <div class="cfa-12__a"><div><p>Yes — embedded engagements of 1–3 months, joining your standups and shipping in your codebase or design system. It is the fastest way to transfer taste, not just deliverables.</p></div></div>
      </div>
      <div class="cfa-12__item">
        <input type="checkbox" id="cfa12-q4" class="cfa-12__cb">
        <label class="cfa-12__q" for="cfa12-q4">Who owns the work?<i class="cfa-12__ic" aria-hidden="true"></i></label>
        <div class="cfa-12__a"><div><p>You do, fully, on final payment — source files, fonts we licensed for you, the lot. We keep the right to show the work in our portfolio unless the contract says otherwise.</p></div></div>
      </div>
    </div>
    <p class="cfa-12__foot">The morph: <code>::before rotate 180°</code> + <code>::after rotate 180° &amp; scale 0 1</code>, one springy bezier. CodeFronts collection.</p>
  </div>
</section>
```
## CSS
```css
.cfa-12,
.cfa-12 *,
.cfa-12 *::before,
.cfa-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-12 {
  --bg: oklch(0.2 0.03 145);
  --panel: oklch(0.25 0.035 148);
  --ink: oklch(0.96 0.01 140);
  --mut: oklch(0.72 0.03 142);
  --line: oklch(0.34 0.04 146);
  --acc: oklch(0.85 0.17 130);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: radial-gradient(900px 600px at 0% 0%,oklch(0.27 0.06 130/.6),transparent 55%),var(--bg);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-12__wrap {
  width: min(100%,640px);
}

.cfa-12__head h1 {
  font-size: clamp(28px,4.5cqi,40px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-12__head p {
  margin-top: 8px;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--mut);
}

.cfa-12__list {
  margin-top: 26px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.cfa-12__item {
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--panel);
  overflow: hidden;
  transition: border-color .3s;
}

.cfa-12__item:has(.cfa-12__cb:checked) {
  border-color: color-mix(in oklch,var(--acc) 40%,var(--line));
}

.cfa-12__cb {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cfa-12__q {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 44px;
  padding: 16px 18px;
  cursor: pointer;
  font-size: 15.5px;
  font-weight: 650;
  letter-spacing: -.01em;
  transition: color .2s;
}

.cfa-12__q:hover {
  color: var(--acc);
}

.cfa-12__cb:focus-visible + .cfa-12__q {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 14px;
}

.cfa-12__ic {
  position: relative;
  flex: none;
  width: 26px;
  height: 26px;
  border-radius: 9px;
  background: color-mix(in oklch,var(--acc) 13%,transparent);
  color: var(--mut);
  transition: scale .25s,color .3s;
}

.cfa-12__q:hover .cfa-12__ic {
  scale: 1.12;
  color: var(--acc);
}

.cfa-12__cb:checked + .cfa-12__q .cfa-12__ic {
  color: var(--acc);
}

.cfa-12__ic::before,
.cfa-12__ic::after {
  content: "";
  position: absolute;
  inset: 0;
  margin: auto;
  width: 14px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  transition: rotate .45s cubic-bezier(.5,-0.3,.3,1.3),scale .45s cubic-bezier(.5,-0.3,.3,1.3);
}

.cfa-12__ic::after {
  rotate: 90deg;
}

.cfa-12__cb:checked + .cfa-12__q .cfa-12__ic::before {
  rotate: 180deg;
}

.cfa-12__cb:checked + .cfa-12__q .cfa-12__ic::after {
  rotate: 180deg;
  scale: 0 1;
}

.cfa-12__a {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .45s cubic-bezier(.4,0,.2,1);
}

.cfa-12__a>div {
  overflow: hidden;
  min-height: 0;
}

.cfa-12__a p {
  padding: 0 18px 17px;
  font-size: 14px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 60ch;
}

.cfa-12__cb:checked ~ .cfa-12__a {
  grid-template-rows: 1fr;
}

.cfa-12__foot {
  margin-top: 22px;
  font-size: 12.5px;
  color: var(--mut);
}

.cfa-12__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .88em;
  background: oklch(0.3 0.04 146);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-12 * {
    transition-duration: .01ms !important;
  }
}
```
