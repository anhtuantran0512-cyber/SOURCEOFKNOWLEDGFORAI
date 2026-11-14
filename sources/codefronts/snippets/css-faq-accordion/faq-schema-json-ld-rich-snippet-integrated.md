---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/faq-schema-json-ld-rich-snippet-integrated/"
title: "FAQ Schema JSON-LD Rich Snippet Integrated"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "A FAQ page wearing its structured data: the visible accordion is mirrored 1:1 by a FAQPage JSON-LD block in the same markup, making answers eligible for rich…"
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: FAQ Schema JSON-LD Rich Snippet Integrated
Source: https://codefronts.com/snippets/css-faq-accordion/faq-schema-json-ld-rich-snippet-integrated/

A FAQ page wearing its structured data: the visible accordion is mirrored 1:1 by a FAQPage JSON-LD block in the same markup, making answers eligible for rich results and — increasingly important — cleanly parseable by AI search and answer engines. The demo renders a mock Google SERP preview showing what the rich result looks like, and the tutorial covers the eligibility reality (Google restricts FAQ rich results to government/health sites since 2023, but the markup still matters), the match-the-visible-content rule, and validation workflow.
## HTML
```html
<section class="cfa-22" aria-label="FAQ with JSON-LD structured data">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {"@type":"Question","name":"How long does shipping take?","acceptedAnswer":{"@type":"Answer","text":"Standard shipping takes 3–5 business days in the US, UK, Canada and Australia. Express 1–2 day options are available at checkout."}},
      {"@type":"Question","name":"What is your return policy?","acceptedAnswer":{"@type":"Answer","text":"Returns are free for 60 days from delivery. Start a return from your order email; refunds process within 3–5 days of the carrier scan."}},
      {"@type":"Question","name":"Do you ship internationally?","acceptedAnswer":{"@type":"Answer","text":"Yes — to 40+ countries with duties calculated at checkout, so there are no surprise fees at the door."}},
      {"@type":"Question","name":"How can I track my order?","acceptedAnswer":{"@type":"Answer","text":"Every order emails a tracked link at dispatch, and live status appears on your account's orders page."}}
    ]
  }
  </script>
  <div class="cfa-22__wrap">
    <header class="cfa-22__head">
      <span class="cfa-22__chip">&lt;script type="application/ld+json"&gt;</span>
      <h1>Machine-readable FAQ</h1>
      <p>The accordion below is mirrored 1:1 in a FAQPage JSON-LD block — same four answers, one for humans, one for crawlers and AI engines.</p>
    </header>
    <div class="cfa-22__serp" role="img" aria-label="Mock search result showing FAQ rich snippet">
      <div class="cfa-22__serp-url">example.com › help › shipping</div>
      <div class="cfa-22__serp-title">Shipping &amp; Returns FAQ — Example Store</div>
      <div class="cfa-22__serp-desc">Answers about delivery times, returns, international shipping and order tracking.</div>
      <div class="cfa-22__serp-faq">
        <div class="cfa-22__serp-q">How long does shipping take? <b>⌄</b></div>
        <div class="cfa-22__serp-q">What is your return policy? <b>⌄</b></div>
      </div>
      <span class="cfa-22__serp-tag">what the rich result renders (where eligible)</span>
    </div>
    <div class="cfa-22__list">
      <details class="cfa-22__item" open>
        <summary class="cfa-22__q">How long does shipping take?<i aria-hidden="true"></i></summary>
        <div class="cfa-22__a"><p>Standard shipping takes 3–5 business days in the US, UK, Canada and Australia. Express 1–2 day options are available at checkout.</p></div>
      </details>
      <details class="cfa-22__item">
        <summary class="cfa-22__q">What is your return policy?<i aria-hidden="true"></i></summary>
        <div class="cfa-22__a"><p>Returns are free for 60 days from delivery. Start a return from your order email; refunds process within 3–5 days of the carrier scan.</p></div>
      </details>
      <details class="cfa-22__item">
        <summary class="cfa-22__q">Do you ship internationally?<i aria-hidden="true"></i></summary>
        <div class="cfa-22__a"><p>Yes — to 40+ countries with duties calculated at checkout, so there are no surprise fees at the door.</p></div>
      </details>
      <details class="cfa-22__item">
        <summary class="cfa-22__q">How can I track my order?<i aria-hidden="true"></i></summary>
        <div class="cfa-22__a"><p>Every order emails a tracked link at dispatch, and live status appears on your account's orders page.</p></div>
      </details>
    </div>
    <p class="cfa-22__foot">Rule #1: the JSON must match the visible content. Validate with the Rich Results Test. CodeFronts collection.</p>
  </div>
</section>
```
## CSS
```css
.cfa-22,
.cfa-22 *,
.cfa-22 *::before,
.cfa-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-22 {
  --bg: oklch(0.98 0.005 250);
  --panel: oklch(1 0 0);
  --ink: oklch(0.22 0.025 255);
  --mut: oklch(0.5 0.02 252);
  --line: oklch(0.9 0.01 250);
  --acc: oklch(0.5 0.17 262);
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

.cfa-22__wrap {
  width: min(100%,640px);
}

.cfa-22__chip {
  display: inline-block;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  font-weight: 600;
  color: var(--acc);
  padding: 6px 12px;
  background: color-mix(in oklch,var(--acc) 9%,transparent);
  border-radius: 99px;
}

.cfa-22__head h1 {
  margin-top: 12px;
  font-size: clamp(26px,4.5cqi,38px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-22__head p {
  margin-top: 8px;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--mut);
}

.cfa-22__serp {
  position: relative;
  margin-top: 20px;
  padding: 16px 18px 30px;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
  font-family: arial,'Segoe UI',sans-serif;
}

.cfa-22__serp-url {
  font-size: 12px;
  color: oklch(0.35 0.02 150);
}

.cfa-22__serp-title {
  margin-top: 3px;
  font-size: 17px;
  color: oklch(0.45 0.19 262);
}

.cfa-22__serp-desc {
  margin-top: 3px;
  font-size: 12.5px;
  color: var(--mut);
}

.cfa-22__serp-faq {
  margin-top: 10px;
  border-top: 1px solid var(--line);
}

.cfa-22__serp-q {
  display: flex;
  justify-content: space-between;
  padding: 9px 2px;
  font-size: 13px;
  color: var(--ink);
  border-bottom: 1px solid var(--line);
}

.cfa-22__serp-q b {
  color: var(--mut);
  font-weight: 400;
}

.cfa-22__serp-tag {
  position: absolute;
  right: 12px;
  bottom: 8px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 10px;
  color: var(--acc);
}

.cfa-22__list {
  margin-top: 18px;
  display: flex;
  flex-direction: column;
  gap: 9px;
  interpolate-size: allow-keywords;
}

.cfa-22__item {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 13px;
  transition: border-color .3s;
}

.cfa-22__item[open] {
  border-color: color-mix(in oklch,var(--acc) 40%,var(--line));
}

.cfa-22__q {
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

.cfa-22__q::-webkit-details-marker {
  display: none;
}

.cfa-22__q:hover {
  color: var(--acc);
}

.cfa-22__q:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 13px;
}

.cfa-22__q i {
  flex: none;
  width: 8px;
  height: 8px;
  border-right: 2px solid var(--acc);
  border-bottom: 2px solid var(--acc);
  rotate: 45deg;
  translate: 0 -2px;
  transition: rotate .35s;
}

.cfa-22__item[open] .cfa-22__q i {
  rotate: 225deg;
  translate: 0 2px;
}

.cfa-22__a p {
  padding: 0 17px 16px;
  font-size: 13.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 60ch;
}

@supports (interpolate-size: allow-keywords) {
  .cfa-22__item::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .35s cubic-bezier(.4,0,.2,1),opacity .3s,content-visibility .35s allow-discrete;
  }

  .cfa-22__item[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

.cfa-22__foot {
  margin-top: 20px;
  font-size: 12.5px;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-22 *,
    .cfa-22 .cfa-22__item::details-content {
    transition-duration: .01ms !important;
  }
}
```
