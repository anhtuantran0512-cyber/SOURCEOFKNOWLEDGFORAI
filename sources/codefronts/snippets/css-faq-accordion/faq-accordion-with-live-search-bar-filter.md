---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/faq-accordion-with-live-search-bar-filter/"
title: "FAQ Accordion with Live Search Bar Filter"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "Type-to-filter FAQ: a search bar live-narrows the question list as you type, matching against question AND answer text, auto-expanding matched items so the…"
has_js: "true"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: FAQ Accordion with Live Search Bar Filter
Source: https://codefronts.com/snippets/css-faq-accordion/faq-accordion-with-live-search-bar-filter/

Type-to-filter FAQ: a search bar live-narrows the question list as you type, matching against question AND answer text, auto-expanding matched items so the hit is visible, with a result count for screen readers (aria-live) and a designed no-results state that suggests clearing. 24 lines of dependency-free JavaScript on top of the native details accordion — the honest minimum for search, with every UX and a11y decision explained.
## HTML
```html
<section class="cfa-18" aria-label="FAQ with live search filter">
  <div class="cfa-18__wrap">
    <header class="cfa-18__head">
      <h1>Search the FAQ</h1>
      <p>Matches run against questions <em>and</em> answers — try “refund”, “VAT”, or gibberish for the empty state.</p>
    </header>
    <div class="cfa-18__bar">
      <svg class="cfa-18__glass" viewBox="0 0 20 20" width="16" height="16" aria-hidden="true"><circle cx="9" cy="9" r="6" fill="none" stroke="currentColor" stroke-width="2"/><path d="M13.5 13.5L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      <input type="search" id="cfa18-search" class="cfa-18__input" placeholder="Type to filter questions…" aria-label="Search frequently asked questions">
      <span class="cfa-18__count" id="cfa18-count" aria-live="polite"></span>
    </div>
    <div class="cfa-18__list" id="cfa18-list">
      <details class="cfa-18__item" open>
        <summary class="cfa-18__q">How do refunds work?<i aria-hidden="true"></i></summary>
        <div class="cfa-18__a"><p>Full refund within 30 days of purchase, self-serve from your order page — money back to the original method in 3–5 business days, VAT included and corrected on the credit note.</p></div>
      </details>
      <details class="cfa-18__item">
        <summary class="cfa-18__q">Do prices include VAT?<i aria-hidden="true"></i></summary>
        <div class="cfa-18__a"><p>Consumer prices include VAT for EU and UK customers; business customers with a valid VAT ID are reverse-charged. US sales tax is added at checkout by state.</p></div>
      </details>
      <details class="cfa-18__item">
        <summary class="cfa-18__q">Can I use one license on two machines?<i aria-hidden="true"></i></summary>
        <div class="cfa-18__a"><p>Yes — licenses are per person, not per device. Sign in on up to three machines; deactivating an old one from the dashboard frees a slot instantly.</p></div>
      </details>
      <details class="cfa-18__item">
        <summary class="cfa-18__q">Is there a student discount?<i aria-hidden="true"></i></summary>
        <div class="cfa-18__a"><p>50% off with a current academic email or ISIC card, verified once a year. It stacks with nothing else, but it beats every coupon we have ever issued.</p></div>
      </details>
      <details class="cfa-18__item">
        <summary class="cfa-18__q">What happens to updates after my license expires?<i aria-hidden="true"></i></summary>
        <div class="cfa-18__a"><p>The perpetual-fallback model: the app keeps working forever at the last version your license covered; renewing unlocks another year of updates. No subscription hostage-taking.</p></div>
      </details>
      <details class="cfa-18__item">
        <summary class="cfa-18__q">Do you offer purchase orders for schools?<i aria-hidden="true"></i></summary>
        <div class="cfa-18__a"><p>Yes — POs from accredited institutions are NET-30, with W-9 and vendor forms available for download. Email a PO and quantities; keys arrive with the countersigned invoice.</p></div>
      </details>
    </div>
    <div class="cfa-18__empty" id="cfa18-empty" hidden>
      <b>No questions match.</b>
      <p>Try fewer words, or <button type="button" class="cfa-18__clear" id="cfa18-clear">clear the search</button>.</p>
    </div>
    <p class="cfa-18__foot">24 lines of vanilla JS: match on textContent, hide via the <code>hidden</code> attribute, announce via <code>aria-live</code>. CodeFronts collection.</p>
  </div>
</section>
```
## CSS
```css
.cfa-18,
.cfa-18 *,
.cfa-18 *::before,
.cfa-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-18 {
  --bg: oklch(0.16 0.02 250);
  --panel: oklch(0.21 0.022 250);
  --ink: oklch(0.95 0.007 245);
  --mut: oklch(0.67 0.018 248);
  --line: oklch(0.31 0.025 250);
  --acc: oklch(0.78 0.13 200);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: radial-gradient(1000px 550px at 50% -15%,oklch(0.24 0.05 210/.55),transparent 60%),var(--bg);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-18__wrap {
  width: min(100%,660px);
}

.cfa-18__head h1 {
  font-size: clamp(26px,4.5cqi,38px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-18__head p {
  margin-top: 8px;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--mut);
}

.cfa-18__bar {
  position: relative;
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 22px;
  padding: 0 16px;
  min-height: 52px;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
  transition: border-color .25s,box-shadow .25s;
}

.cfa-18__bar:focus-within {
  border-color: var(--acc);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--acc) 25%,transparent);
}

.cfa-18__glass {
  flex: none;
  color: var(--mut);
}

.cfa-18__input {
  flex: 1;
  min-width: 0;
  min-height: 44px;
  background: none;
  border: 0;
  outline: 0;
  font: inherit;
  font-size: 15px;
  color: var(--ink);
}

.cfa-18__input::placeholder {
  color: var(--mut);
}

.cfa-18__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
}

.cfa-18__count {
  flex: none;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  font-weight: 600;
  color: var(--acc);
  white-space: nowrap;
}

.cfa-18__list {
  margin-top: 14px;
  display: flex;
  flex-direction: column;
  gap: 9px;
  interpolate-size: allow-keywords;
}

.cfa-18__item {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 13px;
  transition: border-color .3s;
}

.cfa-18__item[open] {
  border-color: color-mix(in oklch,var(--acc) 40%,var(--line));
}

.cfa-18__q {
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

.cfa-18__q::-webkit-details-marker {
  display: none;
}

.cfa-18__q:hover {
  color: var(--acc);
}

.cfa-18__q:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 13px;
}

.cfa-18__q i {
  flex: none;
  width: 8px;
  height: 8px;
  border-right: 2px solid var(--acc);
  border-bottom: 2px solid var(--acc);
  rotate: 45deg;
  translate: 0 -2px;
  transition: rotate .35s;
}

.cfa-18__item[open] .cfa-18__q i {
  rotate: 225deg;
  translate: 0 2px;
}

.cfa-18__a p {
  padding: 0 17px 16px;
  font-size: 13.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 60ch;
}

@supports (interpolate-size: allow-keywords) {
  .cfa-18__item::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .35s cubic-bezier(.4,0,.2,1),opacity .3s,content-visibility .35s allow-discrete;
  }

  .cfa-18__item[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

.cfa-18__empty {
  margin-top: 16px;
  padding: 26px 20px;
  text-align: center;
  border: 1px dashed var(--line);
  border-radius: 14px;
  color: var(--mut);
}

.cfa-18__empty b {
  color: var(--ink);
  font-size: 15px;
}

.cfa-18__empty p {
  margin-top: 6px;
  font-size: 13.5px;
}

.cfa-18__clear {
  font: inherit;
  font-weight: 700;
  color: var(--acc);
  background: none;
  border: 0;
  cursor: pointer;
  text-decoration: underline;
  text-underline-offset: 3px;
  min-height: 44px;
  padding: 0 4px;
}

.cfa-18__clear:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  border-radius: 6px;
}

.cfa-18__foot {
  margin-top: 20px;
  font-size: 12.5px;
  color: var(--mut);
}

.cfa-18__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .88em;
  background: oklch(0.27 0.025 250);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-18 *,
    .cfa-18 .cfa-18__item::details-content {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cfa-18');if(!root||root.dataset.cfa18)return;root.dataset.cfa18='1';
  var input=root.querySelector('#cfa18-search'),count=root.querySelector('#cfa18-count'),
      empty=root.querySelector('#cfa18-empty'),items=[].slice.call(root.querySelectorAll('.cfa-18__item'));
  items.forEach(function(d){d.dataset.initOpen=d.open?'1':''});
  function filter(){
    var q=input.value.trim().toLowerCase(),hits=0;
    items.forEach(function(d){
      var hit=!q||d.textContent.toLowerCase().indexOf(q)>-1;
      d.hidden=!hit;
      if(q&&hit)d.open=true;
      if(!q)d.open=!!d.dataset.initOpen;
      if(hit)hits++;
    });
    count.textContent=q?hits+' of '+items.length+' questions':'';
    empty.hidden=hits>0;
  }
  input.addEventListener('input',filter);
  root.querySelector('#cfa18-clear').addEventListener('click',function(){input.value='';filter();input.focus()});
})();
```
