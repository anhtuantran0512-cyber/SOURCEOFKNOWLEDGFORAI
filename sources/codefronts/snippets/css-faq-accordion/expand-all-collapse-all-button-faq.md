---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/expand-all-collapse-all-button-faq/"
title: "Expand All / Collapse All Button FAQ"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "The bulk controls every long FAQ needs: Expand all / Collapse all buttons over a native details accordion — the pattern power-users hit for Ctrl+F, printing,…"
has_js: "true"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Expand All / Collapse All Button FAQ
Source: https://codefronts.com/snippets/css-faq-accordion/expand-all-collapse-all-button-faq/

The bulk controls every long FAQ needs: Expand all / Collapse all buttons over a native details accordion — the pattern power-users hit for Ctrl+F, printing, and legal review. 14 lines of JS loop the open attribute; the interesting engineering is the button state logic: each button disables when it would do nothing (everything already open/closed), computed from a single count, so the controls always tell the truth about what they can do. Printing expands everything automatically via a print stylesheet trick documented in the tutorial.
## HTML
```html
<section class="cfa-19" aria-label="FAQ with expand all and collapse all">
  <div class="cfa-19__wrap">
    <header class="cfa-19__head">
      <div>
        <h1>Rental agreement FAQ</h1>
        <p>Bulk controls for readers who skim, search, or print. Buttons disable when they'd do nothing.</p>
      </div>
      <div class="cfa-19__ctrl" role="group" aria-label="Bulk expand controls">
        <button type="button" class="cfa-19__btn" id="cfa19-expand">Expand all</button>
        <button type="button" class="cfa-19__btn" id="cfa19-collapse" disabled>Collapse all</button>
      </div>
    </header>
    <div class="cfa-19__list" id="cfa19-list">
      <details class="cfa-19__item">
        <summary class="cfa-19__q">How much is the security deposit?<i aria-hidden="true"></i></summary>
        <div class="cfa-19__a"><p>One month's rent, held in a government-approved deposit scheme within 14 days of payment — you receive the scheme certificate by email, and interest accrues to you, not us.</p></div>
      </details>
      <details class="cfa-19__item">
        <summary class="cfa-19__q">Are pets allowed?<i aria-hidden="true"></i></summary>
        <div class="cfa-19__a"><p>Cats and dogs under 25kg, with a pet addendum and a refundable pet deposit of $300. Aquariums under 100L need no addendum; exotic animals are case-by-case.</p></div>
      </details>
      <details class="cfa-19__item">
        <summary class="cfa-19__q">Who handles repairs?<i aria-hidden="true"></i></summary>
        <div class="cfa-19__a"><p>Report through the tenant portal — urgent issues (water, heat, locks) get a 4-hour response window, everything else 3 business days. Repairs under $150 caused by normal wear are always on us.</p></div>
      </details>
      <details class="cfa-19__item">
        <summary class="cfa-19__q">Can I sublet or list on Airbnb?<i aria-hidden="true"></i></summary>
        <div class="cfa-19__a"><p>Long-term subletting is allowed with written consent and a referenced subtenant. Short-term letting is not permitted — it breaches both the lease and most building insurance policies.</p></div>
      </details>
      <details class="cfa-19__item">
        <summary class="cfa-19__q">How do I end the tenancy?<i aria-hidden="true"></i></summary>
        <div class="cfa-19__a"><p>Two months' written notice after the initial fixed term, served via the portal. The move-out checklist and cleaning standard are attached to the lease — deposits return within 10 days of a clear inspection.</p></div>
      </details>
      <details class="cfa-19__item">
        <summary class="cfa-19__q">What happens if rent is late?<i aria-hidden="true"></i></summary>
        <div class="cfa-19__a"><p>A 5-day grace period applies before any fee. After that it is a flat $50, never compounding — and if something has gone wrong, talk to us first; payment plans beat penalties for everyone.</p></div>
      </details>
    </div>
    <p class="cfa-19__foot">Printing this page auto-expands every answer — one <code>@media print</code> rule. Try print preview. CodeFronts collection.</p>
  </div>
</section>
```
## CSS
```css
.cfa-19,
.cfa-19 *,
.cfa-19 *::before,
.cfa-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-19 {
  --bg: oklch(0.975 0.008 145);
  --panel: oklch(1 0 0);
  --ink: oklch(0.24 0.03 155);
  --mut: oklch(0.48 0.025 150);
  --line: oklch(0.89 0.015 148);
  --acc: oklch(0.52 0.14 155);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: var(--bg);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-19__wrap {
  width: min(100%,680px);
}

.cfa-19__head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 18px;
  flex-wrap: wrap;
}

.cfa-19__head h1 {
  font-size: clamp(24px,4cqi,34px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-19__head p {
  margin-top: 7px;
  font-size: 14px;
  line-height: 1.6;
  color: var(--mut);
  max-width: 44ch;
}

.cfa-19__ctrl {
  display: flex;
  gap: 8px;
}

.cfa-19__btn {
  min-height: 44px;
  padding: 0 18px;
  border-radius: 11px;
  border: 1px solid color-mix(in oklch,var(--acc) 45%,var(--line));
  background: var(--panel);
  font: inherit;
  font-size: 13.5px;
  font-weight: 700;
  color: var(--acc);
  cursor: pointer;
  transition: background .2s,translate .15s,opacity .2s;
}

.cfa-19__btn:hover:not(:disabled) {
  background: color-mix(in oklch,var(--acc) 10%,var(--panel));
  translate: 0 -1px;
}

.cfa-19__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cfa-19__btn:disabled {
  opacity: .45;
  cursor: default;
}

.cfa-19__list {
  margin-top: 22px;
  display: flex;
  flex-direction: column;
  gap: 9px;
  interpolate-size: allow-keywords;
}

.cfa-19__item {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 13px;
  transition: border-color .3s;
}

.cfa-19__item[open] {
  border-color: color-mix(in oklch,var(--acc) 40%,var(--line));
}

.cfa-19__q {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 44px;
  padding: 15px 17px;
  cursor: pointer;
  font-size: 15px;
  font-weight: 650;
  list-style: none;
  transition: color .2s;
}

.cfa-19__q::-webkit-details-marker {
  display: none;
}

.cfa-19__q:hover {
  color: var(--acc);
}

.cfa-19__q:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 13px;
}

.cfa-19__q i {
  flex: none;
  width: 8px;
  height: 8px;
  border-right: 2px solid var(--acc);
  border-bottom: 2px solid var(--acc);
  rotate: 45deg;
  translate: 0 -2px;
  transition: rotate .35s;
}

.cfa-19__item[open] .cfa-19__q i {
  rotate: 225deg;
  translate: 0 2px;
}

.cfa-19__a p {
  padding: 0 17px 16px;
  font-size: 13.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 60ch;
}

@supports (interpolate-size: allow-keywords) {
  .cfa-19__item::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .35s cubic-bezier(.4,0,.2,1),opacity .3s,content-visibility .35s allow-discrete;
  }

  .cfa-19__item[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

.cfa-19__foot {
  margin-top: 20px;
  font-size: 12.5px;
  color: var(--mut);
}

.cfa-19__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .88em;
  background: color-mix(in oklch,var(--acc) 8%,transparent);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

@media print {
  .cfa-19__ctrl {
    display: none;
  }

  .cfa-19__item::details-content {
    display: block !important;
    height: auto !important;
    opacity: 1 !important;
    overflow: visible !important;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cfa-19 *,
    .cfa-19 .cfa-19__item::details-content {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cfa-19');if(!root||root.dataset.cfa19)return;root.dataset.cfa19='1';
  var items=[].slice.call(root.querySelectorAll('.cfa-19__item')),
      ex=root.querySelector('#cfa19-expand'),co=root.querySelector('#cfa19-collapse');
  function sync(){
    var open=items.filter(function(d){return d.open}).length;
    ex.disabled=open===items.length;
    co.disabled=open===0;
  }
  ex.addEventListener('click',function(){items.forEach(function(d){d.open=true})});
  co.addEventListener('click',function(){items.forEach(function(d){d.open=false})});
  items.forEach(function(d){d.addEventListener('toggle',sync)});
  sync();
})();
```
