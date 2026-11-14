---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/pure-css-checkbox-hack-faq-accordion-no-javascript/"
title: "Pure CSS Checkbox-Hack FAQ Accordion (no JavaScript)"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "The classic checkbox hack, rebuilt to 2026 standards: a visually-hidden <input type=checkbox> holds the open/closed state, its <label> is the question row,…"
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Checkbox-Hack FAQ Accordion (no JavaScript)
Source: https://codefronts.com/snippets/css-faq-accordion/pure-css-checkbox-hack-faq-accordion-no-javascript/

The classic checkbox hack, rebuilt to 2026 standards: a visually-hidden <input type=checkbox> holds the open/closed state, its <label> is the question row, and a grid-template-rows: 0fr → 1fr transition animates the answer to its natural height — no JavaScript, no max-height guessing, no clip. Because the state lives in a real form control, keyboard toggling (Tab + Space) and :focus-visible rings come free. Styled as a dark SaaS billing FAQ with an animated +/− indicator.
## HTML
```html
<section class="cfa-01" aria-label="Pure CSS checkbox-hack FAQ accordion">
  <div class="cfa-01__wrap">
    <header class="cfa-01__head">
      <span class="cfa-01__eyebrow">Billing &amp; plans</span>
      <h1>Frequently asked questions</h1>
      <p>Every panel below opens with zero JavaScript — the state is a hidden checkbox, the animation is a grid row.</p>
    </header>
    <div class="cfa-01__list">
      <div class="cfa-01__item">
        <input type="checkbox" id="cfa01-q1" class="cfa-01__cb" checked>
        <label class="cfa-01__q" for="cfa01-q1"><span>Can I switch plans mid-cycle?</span><i class="cfa-01__ic" aria-hidden="true"></i></label>
        <div class="cfa-01__a"><div><p>Yes — upgrades apply instantly and we prorate the difference on your next invoice. Downgrades take effect at the end of the current billing period so you never lose time you already paid for.</p></div></div>
      </div>
      <div class="cfa-01__item">
        <input type="checkbox" id="cfa01-q2" class="cfa-01__cb">
        <label class="cfa-01__q" for="cfa01-q2"><span>Do you offer an annual discount?</span><i class="cfa-01__ic" aria-hidden="true"></i></label>
        <div class="cfa-01__a"><div><p>Annual billing saves 20% on every tier and locks your price for the year. You can switch from monthly to annual at any time from Settings → Billing — the unused portion of your month is credited automatically.</p></div></div>
      </div>
      <div class="cfa-01__item">
        <input type="checkbox" id="cfa01-q3" class="cfa-01__cb">
        <label class="cfa-01__q" for="cfa01-q3"><span>What happens when my trial ends?</span><i class="cfa-01__ic" aria-hidden="true"></i></label>
        <div class="cfa-01__a"><div><p>Your workspace switches to the free tier — nothing is deleted. Projects over the free limit become read-only until you pick a plan, and we email you three days before so it is never a surprise.</p></div></div>
      </div>
      <div class="cfa-01__item">
        <input type="checkbox" id="cfa01-q4" class="cfa-01__cb">
        <label class="cfa-01__q" for="cfa01-q4"><span>Can I get a refund?</span><i class="cfa-01__ic" aria-hidden="true"></i></label>
        <div class="cfa-01__a"><div><p>Every paid plan has a 30-day money-back guarantee, no questions asked. Reply to any invoice email or write to [email protected] and we refund to the original payment method within 3–5 business days.</p></div></div>
      </div>
      <div class="cfa-01__item">
        <input type="checkbox" id="cfa01-q5" class="cfa-01__cb">
        <label class="cfa-01__q" for="cfa01-q5"><span>Is my payment data secure?</span><i class="cfa-01__ic" aria-hidden="true"></i></label>
        <div class="cfa-01__a"><div><p>Card details never touch our servers — payments run through a PCI-DSS Level 1 processor, and your dashboard only ever sees the last four digits. All traffic is TLS 1.3 end to end.</p></div></div>
      </div>
    </div>
    <p class="cfa-01__foot">Tab to a question, press <kbd>Space</kbd> — the hidden checkbox is a real form control. From the CodeFronts FAQ accordion collection.</p>
  </div>
</section>
```
## CSS
```css
.cfa-01,
.cfa-01 *,
.cfa-01 *::before,
.cfa-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-01 {
  --bg: oklch(0.15 0.02 275);
  --panel: oklch(0.2 0.025 275);
  --ink: oklch(0.96 0.005 260);
  --mut: oklch(0.68 0.02 265);
  --line: oklch(0.3 0.03 272);
  --acc: oklch(0.78 0.15 165);
  --speed: .45s;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: radial-gradient(1100px 600px at 80% -10%,oklch(0.24 0.05 200/.6),transparent 60%),var(--bg);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-01__wrap {
  width: min(100%,680px);
}

.cfa-01__eyebrow {
  display: inline-block;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
  padding: 6px 12px;
  border: 1px solid color-mix(in oklch,var(--acc) 35%,transparent);
  border-radius: 99px;
}

.cfa-01__head h1 {
  margin-top: 14px;
  font-size: clamp(26px,4.5cqi,38px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-01__head p {
  margin-top: 10px;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--mut);
  max-width: 54ch;
}

.cfa-01__list {
  margin-top: 28px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.cfa-01__item {
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--panel);
  overflow: hidden;
  transition: border-color var(--speed);
}

.cfa-01__item:has(.cfa-01__cb:checked) {
  border-color: color-mix(in oklch,var(--acc) 45%,var(--line));
}

.cfa-01__cb {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cfa-01__q {
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

.cfa-01__q:hover {
  color: var(--acc);
}

.cfa-01__cb:focus-visible + .cfa-01__q {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 14px;
}

.cfa-01__ic {
  position: relative;
  flex: none;
  width: 26px;
  height: 26px;
  border-radius: 8px;
  background: color-mix(in oklch,var(--acc) 14%,transparent);
}

.cfa-01__ic::before,
.cfa-01__ic::after {
  content: "";
  position: absolute;
  inset: 0;
  margin: auto;
  width: 12px;
  height: 2px;
  border-radius: 2px;
  background: var(--acc);
  transition: rotate var(--speed) cubic-bezier(.4,0,.2,1);
}

.cfa-01__ic::after {
  rotate: 90deg;
}

.cfa-01__cb:checked + .cfa-01__q .cfa-01__ic::after {
  rotate: 0deg;
}

.cfa-01__cb:checked + .cfa-01__q .cfa-01__ic::before {
  rotate: 180deg;
}

.cfa-01__a {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows var(--speed) cubic-bezier(.4,0,.2,1);
}

.cfa-01__a>div {
  overflow: hidden;
}

.cfa-01__a p {
  padding: 0 18px 17px;
  font-size: 14px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 60ch;
}

.cfa-01__cb:checked ~ .cfa-01__a {
  grid-template-rows: 1fr;
}

.cfa-01__foot {
  margin-top: 22px;
  font-size: 12.5px;
  color: var(--mut);
}

.cfa-01__foot kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  padding: 2px 7px;
  border: 1px solid var(--line);
  border-bottom-width: 2px;
  border-radius: 6px;
  background: var(--panel);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-01 * {
    transition-duration: .01ms !important;
  }
}
```
