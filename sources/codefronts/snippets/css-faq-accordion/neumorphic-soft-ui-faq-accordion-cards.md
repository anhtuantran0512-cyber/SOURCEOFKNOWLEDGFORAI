---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/neumorphic-soft-ui-faq-accordion-cards/"
title: "Neumorphic Soft-UI FAQ Accordion Cards"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "Soft-UI done responsibly: FAQ cards extruded from a single-material surface using the twin-shadow trick (light source top-left, shade bottom-right), pressing…"
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Soft-UI FAQ Accordion Cards
Source: https://codefronts.com/snippets/css-faq-accordion/neumorphic-soft-ui-faq-accordion-cards/

Soft-UI done responsibly: FAQ cards extruded from a single-material surface using the twin-shadow trick (light source top-left, shade bottom-right), pressing physically inset when opened — the material metaphor doing the state communication. The demo bakes in the two fixes that make neumorphism shippable rather than a Dribbble liability: real borders on focus, and text contrast held at WCAG AA even though the palette is all one hue.
## HTML
```html
<section class="cfa-09" aria-label="Neumorphic soft-UI FAQ accordion">
  <div class="cfa-09__wrap">
    <header class="cfa-09__head">
      <h1>Device support</h1>
      <p>One material, one light source. Open a card and it presses into the surface.</p>
    </header>
    <div class="cfa-09__list">
      <details class="cfa-09__item" open>
        <summary class="cfa-09__q"><span class="cfa-09__dot" aria-hidden="true"></span>How do I pair a new device?<i class="cfa-09__chev" aria-hidden="true"></i></summary>
        <div class="cfa-09__a"><p>Hold the side button for 3 seconds until the ring pulses, then open the app — pairing is automatic within arm's reach. Up to 8 devices can stay paired to one account.</p></div>
      </details>
      <details class="cfa-09__item">
        <summary class="cfa-09__q"><span class="cfa-09__dot" aria-hidden="true"></span>Why won't it charge past 80%?<i class="cfa-09__chev" aria-hidden="true"></i></summary>
        <div class="cfa-09__a"><p>That is battery care mode, on by default — it doubles cell lifespan. Toggle “Full charge” in the app for trips; it reverts automatically after 48 hours.</p></div>
      </details>
      <details class="cfa-09__item">
        <summary class="cfa-09__q"><span class="cfa-09__dot" aria-hidden="true"></span>Is it waterproof?<i class="cfa-09__chev" aria-hidden="true"></i></summary>
        <div class="cfa-09__a"><p>IP68 — pool and shower safe, and rinsing after salt water is recommended. The charging contacts are corrosion-sealed, so no port covers to lose.</p></div>
      </details>
      <details class="cfa-09__item">
        <summary class="cfa-09__q"><span class="cfa-09__dot" aria-hidden="true"></span>How do I factory reset?<i class="cfa-09__chev" aria-hidden="true"></i></summary>
        <div class="cfa-09__a"><p>Settings → Device → Reset in the app, or hold both buttons for 10 seconds until three pulses. Your data stays in the cloud and restores on next pairing.</p></div>
      </details>
    </div>
    <p class="cfa-09__foot">Twin shadows out = raised · inset = pressed. Contrast held at AA despite the single-hue palette.</p>
  </div>
</section>
```
## CSS
```css
.cfa-09,
.cfa-09 *,
.cfa-09 *::before,
.cfa-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-09 {
  --surface: oklch(0.92 0.018 250);
  --hi: color-mix(in oklch,var(--surface) 35%,white);
  --lo: color-mix(in oklch,var(--surface) 72%,oklch(0.55 0.06 260));
  --ink: oklch(0.3 0.04 260);
  --mut: oklch(0.45 0.035 258);
  --acc: oklch(0.55 0.16 262);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: var(--surface);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-09__wrap {
  width: min(100%,600px);
}

.cfa-09__head h1 {
  font-size: clamp(26px,4.5cqi,36px);
  font-weight: 800;
  letter-spacing: -.02em;
}

.cfa-09__head p {
  margin-top: 8px;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--mut);
}

.cfa-09__list {
  margin-top: 28px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  interpolate-size: allow-keywords;
}

.cfa-09__item {
  background: var(--surface);
  border-radius: 20px;
  box-shadow: -8px -8px 18px var(--hi),8px 8px 18px var(--lo);
  transition: box-shadow .35s cubic-bezier(.4,0,.2,1);
}

.cfa-09__item:not([open]):hover {
  box-shadow: -10px -10px 22px var(--hi),10px 10px 22px var(--lo);
}

.cfa-09__item[open] {
  box-shadow: inset -6px -6px 14px var(--hi),inset 6px 6px 14px var(--lo);
}

.cfa-09__q {
  display: flex;
  align-items: center;
  gap: 13px;
  min-height: 44px;
  padding: 18px 20px;
  cursor: pointer;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.01em;
  list-style: none;
  border-radius: 20px;
  transition: translate .25s;
}

.cfa-09__q::-webkit-details-marker {
  display: none;
}

.cfa-09__item[open] .cfa-09__q {
  translate: 1px 1px;
}

.cfa-09__q:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cfa-09__dot {
  flex: none;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--acc);
  box-shadow: -2px -2px 4px var(--hi),2px 2px 4px var(--lo);
  transition: background .3s;
}

.cfa-09__chev {
  margin-left: auto;
  flex: none;
  width: 9px;
  height: 9px;
  border-right: 2.5px solid var(--mut);
  border-bottom: 2.5px solid var(--mut);
  border-radius: 1px;
  rotate: 45deg;
  translate: 0 -2px;
  transition: rotate .35s,border-color .3s;
}

.cfa-09__item[open] .cfa-09__chev {
  rotate: 225deg;
  translate: 0 2px;
  border-color: var(--acc);
}

.cfa-09__a p {
  padding: 0 20px 19px 42px;
  font-size: 13.5px;
  line-height: 1.75;
  color: var(--mut);
  max-width: 56ch;
}

@supports (interpolate-size: allow-keywords) {
  .cfa-09__item::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .38s cubic-bezier(.4,0,.2,1),opacity .3s,content-visibility .38s allow-discrete;
  }

  .cfa-09__item[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

.cfa-09__foot {
  margin-top: 24px;
  font-size: 12px;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-09 *,
    .cfa-09 .cfa-09__item::details-content {
    transition-duration: .01ms !important;
  }
}
```
