---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/faq-with-mutually-exclusive-q-panels-only-one-open-ux/"
title: "FAQ with Mutually Exclusive Q Panels (only-one-open UX)"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "Only-one-open used to mean JavaScript closing siblings — now it is a single HTML attribute."
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: FAQ with Mutually Exclusive Q Panels (only-one-open UX)
Source: https://codefronts.com/snippets/css-faq-accordion/faq-with-mutually-exclusive-q-panels-only-one-open-ux/

Only-one-open used to mean JavaScript closing siblings — now it is a single HTML attribute. Give every <details> the same name value and the browser enforces exclusivity like radio buttons: opening one closes the previous, state stays in the DOM, and keyboard/AT behavior remains native. This demo styles it as a pricing-page FAQ with an active-item accent rail, and documents the radio-hack fallback for legacy targets in the tutorial.
## HTML
```html
<section class="cfa-03" aria-label="Exclusive one-open FAQ accordion">
  <div class="cfa-03__wrap">
    <header class="cfa-03__head">
      <span class="cfa-03__chip">name="faq" · zero JS exclusivity</span>
      <h1>Pricing questions, answered</h1>
      <p>Open any question — the browser closes the previous one. One attribute, no JavaScript.</p>
    </header>
    <div class="cfa-03__list">
      <details class="cfa-03__item" name="cfa03-faq" open>
        <summary class="cfa-03__q"><span class="cfa-03__n">01</span>Is there a free plan?<i class="cfa-03__chev" aria-hidden="true"></i></summary>
        <div class="cfa-03__a"><p>Yes — free forever for up to 3 projects and 2 seats, with no card required. It is a real plan, not a trial: teams ship production work on it every day.</p></div>
      </details>
      <details class="cfa-03__item" name="cfa03-faq">
        <summary class="cfa-03__q"><span class="cfa-03__n">02</span>What counts as a “seat”?<i class="cfa-03__chev" aria-hidden="true"></i></summary>
        <div class="cfa-03__a"><p>Anyone who can edit. Viewers and commenters are unlimited and free on every plan — you only pay for people who change things.</p></div>
      </details>
      <details class="cfa-03__item" name="cfa03-faq">
        <summary class="cfa-03__q"><span class="cfa-03__n">03</span>Do prices include tax?<i class="cfa-03__chev" aria-hidden="true"></i></summary>
        <div class="cfa-03__a"><p>Prices are shown pre-tax; VAT/GST is added at checkout based on your billing country. US customers see applicable state sales tax. Every invoice is tax-compliant for expensing.</p></div>
      </details>
      <details class="cfa-03__item" name="cfa03-faq">
        <summary class="cfa-03__q"><span class="cfa-03__n">04</span>Can I pay by invoice?<i class="cfa-03__chev" aria-hidden="true"></i></summary>
        <div class="cfa-03__a"><p>Annual plans over $2,000 can be paid by bank transfer with NET-30 terms. Contact sales and we will set up procurement, security review and a countersigned DPA if you need one.</p></div>
      </details>
    </div>
    <p class="cfa-03__foot">Closed questions dim via <code>.list:has([open])</code> — attention follows the open panel. CodeFronts collection.</p>
  </div>
</section>
```
## CSS
```css
.cfa-03,
.cfa-03 *,
.cfa-03 *::before,
.cfa-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-03 {
  --bg: oklch(0.98 0.005 270);
  --panel: oklch(1 0 0);
  --ink: oklch(0.22 0.03 275);
  --mut: oklch(0.52 0.025 270);
  --line: oklch(0.9 0.012 270);
  --acc: oklch(0.55 0.2 275);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: linear-gradient(180deg,color-mix(in oklch,var(--acc) 6%,var(--bg)),var(--bg) 40%);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-03__wrap {
  width: min(100%,660px);
}

.cfa-03__chip {
  display: inline-block;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  font-weight: 600;
  color: var(--acc);
  padding: 6px 12px;
  background: color-mix(in oklch,var(--acc) 10%,transparent);
  border-radius: 99px;
}

.cfa-03__head h1 {
  margin-top: 14px;
  font-size: clamp(26px,4.5cqi,38px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-03__head p {
  margin-top: 8px;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--mut);
}

.cfa-03__list {
  margin-top: 26px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  interpolate-size: allow-keywords;
}

.cfa-03__item {
  position: relative;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
  overflow: hidden;
  transition: border-color .3s,box-shadow .3s;
}

.cfa-03__item::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background: var(--acc);
  scale: 1 0;
  transition: scale .35s cubic-bezier(.4,0,.2,1);
}

.cfa-03__item[open] {
  border-color: color-mix(in oklch,var(--acc) 35%,var(--line));
  box-shadow: 0 12px 32px oklch(0.4 0.1 275/.1);
}

.cfa-03__item[open]::before {
  scale: 1 1;
}

.cfa-03__list:has([open]) .cfa-03__item:not([open]) .cfa-03__q {
  opacity: .72;
}

.cfa-03__q {
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 44px;
  padding: 16px 18px;
  cursor: pointer;
  font-size: 15.5px;
  font-weight: 650;
  list-style: none;
  transition: opacity .3s;
}

.cfa-03__q::-webkit-details-marker {
  display: none;
}

.cfa-03__q:hover {
  opacity: 1 !important;
}

.cfa-03__q:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 14px;
}

.cfa-03__n {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  font-weight: 700;
  color: var(--acc);
}

.cfa-03__chev {
  margin-left: auto;
  flex: none;
  width: 9px;
  height: 9px;
  border-right: 2px solid var(--mut);
  border-bottom: 2px solid var(--mut);
  rotate: 45deg;
  translate: 0 -2px;
  transition: rotate .35s,border-color .3s;
}

.cfa-03__item[open] .cfa-03__chev {
  rotate: 225deg;
  translate: 0 2px;
  border-color: var(--acc);
}

.cfa-03__a p {
  padding: 0 18px 17px 47px;
  font-size: 14px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 58ch;
}

@supports (interpolate-size: allow-keywords) {
  .cfa-03__item::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .38s cubic-bezier(.4,0,.2,1),opacity .3s,content-visibility .38s allow-discrete;
  }

  .cfa-03__item[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

.cfa-03__foot {
  margin-top: 22px;
  font-size: 12.5px;
  color: var(--mut);
}

.cfa-03__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .88em;
  background: color-mix(in oklch,var(--acc) 8%,transparent);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-03 *,
    .cfa-03 .cfa-03__item::details-content {
    transition-duration: .01ms !important;
  }
}
```
