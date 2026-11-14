---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/bounce-spring-ease-expand-faq/"
title: "Bounce Spring-Ease Expand FAQ"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "Spring physics without a physics engine: the linear() easing function lets CSS play back a real damped-spring curve — overshoot, wobble and settle — sampled…"
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bounce Spring-Ease Expand FAQ
Source: https://codefronts.com/snippets/css-faq-accordion/bounce-spring-ease-expand-faq/

Spring physics without a physics engine: the linear() easing function lets CSS play back a real damped-spring curve — overshoot, wobble and settle — sampled into a timing function. This FAQ's panels bounce open like they have mass, the icon over-rotates and recoils, and the tutorial explains how to generate your own linear() curves, when cubic-bezier's single overshoot is enough, and why springy opening must pair with boring closing.
## HTML
```html
<section class="cfa-13" aria-label="Spring bounce easing FAQ accordion">
  <div class="cfa-13__wrap">
    <header class="cfa-13__head">
      <span class="cfa-13__chip">transition-timing-function: linear(…)</span>
      <h1>Panels with mass</h1>
      <p>A real damped-spring curve, sampled into CSS. Open = bounce. Close = calm, on purpose.</p>
    </header>
    <div class="cfa-13__list">
      <div class="cfa-13__item">
        <input type="checkbox" id="cfa13-q1" class="cfa-13__cb" checked>
        <label class="cfa-13__q" for="cfa13-q1">What makes this a “spring”, not just easing?<i aria-hidden="true"></i></label>
        <div class="cfa-13__a"><div><p>The curve crosses its target more than once. This panel opens ~16% past its height, recoils, overshoots a little again, and settles — three crossings. A cubic-bezier can only manage one. That multi-crossing wobble is what your brain reads as mass and tension.</p></div></div>
      </div>
      <div class="cfa-13__item">
        <input type="checkbox" id="cfa13-q2" class="cfa-13__cb">
        <label class="cfa-13__q" for="cfa13-q2">Why doesn't it bounce when closing?<i aria-hidden="true"></i></label>
        <div class="cfa-13__a"><div><p>Deliberate asymmetry. A wobbly close feels like the UI resisting you. The trick: declare the spring transition on the <em>checked</em> state and a plain .35s ease-out on the base state — each direction gets its own physics.</p></div></div>
      </div>
      <div class="cfa-13__item">
        <input type="checkbox" id="cfa13-q3" class="cfa-13__cb">
        <label class="cfa-13__q" for="cfa13-q3">How do I make my own curve?<i aria-hidden="true"></i></label>
        <div class="cfa-13__a"><div><p>Use a linear() generator (search “linear easing generator”): set mass, stiffness and damping, and it exports the sampled point list. Damping ≈ 0.4 is cartoon, 0.55 (this demo) is playful-professional, 0.8 is barely-there luxury.</p></div></div>
      </div>
      <div class="cfa-13__item">
        <input type="checkbox" id="cfa13-q4" class="cfa-13__cb">
        <label class="cfa-13__q" for="cfa13-q4">Where should springs never be used?<i aria-hidden="true"></i></label>
        <div class="cfa-13__a"><div><p>Anywhere a user is about to click: the overshoot moves buttons under the cursor. And in prefers-reduced-motion — a spring is precisely the vestibular trigger that setting exists for; this demo drops to near-instant there.</p></div></div>
      </div>
    </div>
    <p class="cfa-13__foot">Open: .8s sampled spring · Close: .35s ease-out · Fallback: cubic-bezier(.34,1.56,.64,1). CodeFronts collection.</p>
  </div>
</section>
```
## CSS
```css
.cfa-13,
.cfa-13 *,
.cfa-13 *::before,
.cfa-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-13 {
  --bg: oklch(0.97 0.015 60);
  --panel: oklch(1 0 0);
  --ink: oklch(0.25 0.03 40);
  --mut: oklch(0.5 0.03 45);
  --line: oklch(0.89 0.02 55);
  --acc: oklch(0.62 0.19 35);
  --spring: linear(0,0.009,0.035 2.1%,0.141 4.4%,0.723 12.9%,0.938,1.077 20.4%,1.121,1.149 24.3%,1.159,1.163 27%,1.154,1.129 32.8%,1.051 39.6%,1.017 43.1%,0.991,0.977 51%,0.974 53.8%,0.975 57.1%,0.997 69.8%,1.003 76.9%,1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: radial-gradient(800px 500px at 90% 10%,oklch(0.93 0.05 45/.7),transparent 60%),var(--bg);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-13__wrap {
  width: min(100%,650px);
}

.cfa-13__chip {
  display: inline-block;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  font-weight: 600;
  color: var(--acc);
  padding: 6px 12px;
  background: color-mix(in oklch,var(--acc) 10%,transparent);
  border-radius: 99px;
}

.cfa-13__head h1 {
  margin-top: 14px;
  font-size: clamp(26px,4.5cqi,38px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-13__head p {
  margin-top: 8px;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--mut);
}

.cfa-13__list {
  margin-top: 26px;
  display: flex;
  flex-direction: column;
  gap: 11px;
}

.cfa-13__item {
  border: 1px solid var(--line);
  border-radius: 15px;
  background: var(--panel);
  overflow: hidden;
  box-shadow: 0 3px 12px oklch(0.4 0.06 40/.06);
  transition: border-color .3s;
}

.cfa-13__item:has(.cfa-13__cb:checked) {
  border-color: color-mix(in oklch,var(--acc) 40%,var(--line));
}

.cfa-13__cb {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cfa-13__q {
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

.cfa-13__q:hover {
  color: var(--acc);
}

.cfa-13__cb:focus-visible + .cfa-13__q {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 15px;
}

.cfa-13__q i {
  position: relative;
  flex: none;
  width: 24px;
  height: 24px;
  border-radius: 8px;
  background: color-mix(in oklch,var(--acc) 12%,transparent);
}

.cfa-13__q i::before,
.cfa-13__q i::after {
  content: "";
  position: absolute;
  inset: 0;
  margin: auto;
  width: 12px;
  height: 2px;
  border-radius: 2px;
  background: var(--acc);
  transition: rotate .35s ease-out;
}

.cfa-13__q i::after {
  rotate: 90deg;
}

.cfa-13__cb:checked + .cfa-13__q i::before {
  rotate: 180deg;
  transition: rotate .8s var(--spring);
}

.cfa-13__cb:checked + .cfa-13__q i::after {
  rotate: 180deg;
  scale: 0 1;
  transition: rotate .8s var(--spring),scale .8s var(--spring);
}

.cfa-13__a {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .35s ease-out;
}

.cfa-13__a>div {
  overflow: hidden;
  min-height: 0;
}

.cfa-13__a p {
  padding: 0 18px 17px;
  font-size: 14px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 60ch;
}

.cfa-13__cb:checked ~ .cfa-13__a {
  grid-template-rows: 1fr;
  transition: grid-template-rows .8s var(--spring);
}

@supports not (transition-timing-function: linear(0,1)) {
  .cfa-13__cb:checked ~ .cfa-13__a {
    transition: grid-template-rows .5s cubic-bezier(.34,1.56,.64,1);
  }

  .cfa-13__cb:checked + .cfa-13__q i::before,
    .cfa-13__cb:checked + .cfa-13__q i::after {
    transition: rotate .5s cubic-bezier(.34,1.56,.64,1),scale .5s cubic-bezier(.34,1.56,.64,1);
  }
}

.cfa-13__foot {
  margin-top: 22px;
  font-size: 12.5px;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-13 * {
    transition-duration: .01ms !important;
  }
}
```
