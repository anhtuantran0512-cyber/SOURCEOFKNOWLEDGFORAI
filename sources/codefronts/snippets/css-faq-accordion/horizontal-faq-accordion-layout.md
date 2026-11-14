---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/horizontal-faq-accordion-layout/"
title: "Horizontal FAQ Accordion Layout"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "The showpiece: five photo panels standing shoulder to shoulder, the active one unfolding sideways to reveal its Q&A while the others compress into elegant…"
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal FAQ Accordion Layout
Source: https://codefronts.com/snippets/css-faq-accordion/horizontal-faq-accordion-layout/

The showpiece: five photo panels standing shoulder to shoulder, the active one unfolding sideways to reveal its Q&A while the others compress into elegant spines with vertically-written titles. Demo 10's fr-unit trick rotated 90° — grid-template-columns animating between 0fr and 1fr shares — plus writing-mode for the spine labels and radio-hack state so it is still pure CSS. The pattern behind a hundred award-site "expanding image accordion" hero sections, with the FAQ content making it useful.
## HTML
```html
<section class="cfa-15" aria-label="Horizontal FAQ accordion">
  <div class="cfa-15__stage">
    <div class="cfa-15__wrap">
      <header class="cfa-15__head">
        <h1>Plan your expedition</h1>
        <p>Five questions standing sideways — the open one unfolds. Arrow keys move between panels.</p>
      </header>
      <div class="cfa-15__strip">
        <div class="cfa-15__panel" style="--img:url('https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1200&auto=format&fit=crop')">
          <input type="radio" name="cfa15" id="cfa15-p1" class="cfa-15__rb" checked>
          <label class="cfa-15__spine" for="cfa15-p1"><h3>When to go?</h3></label>
          <div class="cfa-15__body"><div><h2>When is the best season?</h2><p>June through September for the high passes — long days, stable weather, open refuges. Shoulder months halve the crowds but add real weather risk above 2,500m.</p></div></div>
        </div>
        <div class="cfa-15__panel" style="--img:url('https://images.unsplash.com/photo-1551632811-561732d1e306?q=80&w=1200&auto=format&fit=crop')">
          <input type="radio" name="cfa15" id="cfa15-p2" class="cfa-15__rb">
          <label class="cfa-15__spine" for="cfa15-p2"><h3>Fitness level</h3></label>
          <div class="cfa-15__body"><div><h2>How fit do I need to be?</h2><p>Comfortable hiking 6–7 hours with a daypack, two days in a row. Our grade-2 routes need no technical skills; if you can do a hilly half-day hike smiling, twelve training weeks gets you there.</p></div></div>
        </div>
        <div class="cfa-15__panel" style="--img:url('https://images.unsplash.com/photo-1501554728187-ce583db33af7?q=80&w=1200&auto=format&fit=crop')">
          <input type="radio" name="cfa15" id="cfa15-p3" class="cfa-15__rb">
          <label class="cfa-15__spine" for="cfa15-p3"><h3>What's included</h3></label>
          <div class="cfa-15__body"><div><h2>What does the price include?</h2><p>Guides, refuge nights, breakfasts and dinners, luggage transfer between stages and safety kit. Flights, lunches and insurance are yours — full packing list on booking.</p></div></div>
        </div>
        <div class="cfa-15__panel" style="--img:url('https://images.unsplash.com/photo-1522163182402-834f871fd851?q=80&w=1200&auto=format&fit=crop')">
          <input type="radio" name="cfa15" id="cfa15-p4" class="cfa-15__rb">
          <label class="cfa-15__spine" for="cfa15-p4"><h3>Group size</h3></label>
          <div class="cfa-15__body"><div><h2>How big are the groups?</h2><p>Max 10, average 7, two certified guides per group. Solo travellers are half of every departure — the refuge table does the introductions by night two.</p></div></div>
        </div>
        <div class="cfa-15__panel" style="--img:url('https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?q=80&w=1200&auto=format&fit=crop')">
          <input type="radio" name="cfa15" id="cfa15-p5" class="cfa-15__rb">
          <label class="cfa-15__spine" for="cfa15-p5"><h3>Cancellation</h3></label>
          <div class="cfa-15__body"><div><h2>What if I need to cancel?</h2><p>Free date changes until 30 days out, full refund minus deposit until 14, and the deposit converts to credit after that. Weather cancellations on our side refund everything.</p></div></div>
        </div>
      </div>
      <p class="cfa-15__foot">grid-template-columns 0fr→1fr + flex-grow transition — demo 10's trick, rotated. Folds vertical under 720px.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cfa-15,
.cfa-15 *,
.cfa-15 *::before,
.cfa-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-15 {
  --ink: oklch(0.98 0.004 250);
  --mut: oklch(0.88 0.01 250);
  --acc: oklch(0.8 0.15 80);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-15__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: oklch(0.17 0.02 260);
  container: cfa15/inline-size;
}

.cfa-15__wrap {
  width: min(100%,1020px);
}

.cfa-15__head h1 {
  font-size: clamp(26px,4cqi,40px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-15__head p {
  margin-top: 8px;
  font-size: 14.5px;
  color: var(--mut);
}

.cfa-15__strip {
  margin-top: 26px;
  display: flex;
  gap: 10px;
  min-height: 420px;
}

.cfa-15__panel {
  position: relative;
  flex: 1;
  display: grid;
  grid-template-columns: 64px 0fr;
  border-radius: 18px;
  overflow: hidden;
  background-image: linear-gradient(oklch(0.2 0.03 260/.25),oklch(0.15 0.03 260/.7)),var(--img);
  background-size: cover;
  background-position: center;
  transition: grid-template-columns .6s cubic-bezier(.3,.8,.25,1),flex-grow .6s cubic-bezier(.3,.8,.25,1),outline-color .2s;
  outline: 2px solid transparent;
  outline-offset: 3px;
}

.cfa-15__panel:has(.cfa-15__rb:checked) {
  grid-template-columns: 64px 1fr;
  flex-grow: 3.2;
}

.cfa-15__panel:has(.cfa-15__rb:focus-visible) {
  outline-color: var(--acc);
}

.cfa-15__panel:not(:has(:checked)):hover {
  flex-grow: 1.15;
}

.cfa-15__rb {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cfa-15__spine {
  display: grid;
  place-items: end center;
  padding: 18px 0;
  cursor: pointer;
  min-width: 44px;
}

.cfa-15__spine h3 {
  writing-mode: vertical-rl;
  rotate: 180deg;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  text-shadow: 0 1px 12px oklch(0.15 0.03 260/.8);
  transition: color .3s;
}

.cfa-15__panel:has(:checked) .cfa-15__spine h3,
.cfa-15__spine:hover h3 {
  color: var(--acc);
}

.cfa-15__body {
  overflow: hidden;
  min-width: 0;
  display: grid;
  align-items: end;
}

.cfa-15__body>div {
  width: max(260px,26cqi);
  padding: 22px 24px 22px 8px;
  opacity: 0;
  translate: 14px 0;
  transition: opacity .4s .15s,translate .5s .15s cubic-bezier(.3,.8,.25,1);
}

.cfa-15__panel:has(:checked) .cfa-15__body>div {
  opacity: 1;
  translate: 0 0;
}

.cfa-15__body h2 {
  font-size: clamp(17px,2cqi,22px);
  font-weight: 800;
  letter-spacing: -.02em;
}

.cfa-15__body p {
  margin-top: 9px;
  font-size: 13.5px;
  line-height: 1.65;
  color: var(--mut);
}

.cfa-15__foot {
  margin-top: 20px;
  font-size: 12.5px;
  color: var(--mut);
}

@container cfa15 (width < 720px) {
  .cfa-15__strip {
    flex-direction: column;
    min-height: 0;
  }

  .cfa-15__panel {
    grid-template-columns: 1fr;
    grid-template-rows: 56px 0fr;
    transition: grid-template-rows .5s cubic-bezier(.3,.8,.25,1);
  }

  .cfa-15__panel:has(.cfa-15__rb:checked) {
    grid-template-columns: 1fr;
    grid-template-rows: 56px 1fr;
    flex-grow: 1;
  }

  .cfa-15__spine {
    place-items: center start;
    padding: 0 18px;
    min-height: 44px;
  }

  .cfa-15__spine h3 {
    writing-mode: horizontal-tb;
    rotate: none;
  }

  .cfa-15__body {
    min-height: 0;
  }

  .cfa-15__body>div {
    width: 100%;
    padding: 0 18px 20px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cfa-15 * {
    transition-duration: .01ms !important;
    transition-delay: 0ms !important;
  }
}
```
