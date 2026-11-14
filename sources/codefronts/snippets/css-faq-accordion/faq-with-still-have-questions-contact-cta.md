---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/faq-with-still-have-questions-contact-cta/"
title: "FAQ with \"Still Have Questions?\" Contact CTA"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "The conversion completion of every FAQ: a \"Still have questions?\" CTA card that catches the users your answers didn't — the difference between a dead-end…"
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: FAQ with "Still Have Questions?" Contact CTA
Source: https://codefronts.com/snippets/css-faq-accordion/faq-with-still-have-questions-contact-cta/

The conversion completion of every FAQ: a "Still have questions?" CTA card that catches the users your answers didn't — the difference between a dead-end page and a support funnel. A warm gradient panel with an overlapping avatar group (the classic "real humans reply" trust signal), response-time promise, and two-tier actions: primary chat button, secondary email link. The tutorial covers CTA placement logic, the avatar-stack CSS, and why exactly two actions is the tested sweet spot.
## HTML
```html
<section class="cfa-20" aria-label="FAQ with contact call to action">
  <div class="cfa-20__wrap">
    <header class="cfa-20__head">
      <h1>Frequently asked questions</h1>
      <p>And for everything we didn't think of — real humans, four-hour replies.</p>
    </header>
    <div class="cfa-20__list">
      <details class="cfa-20__item" open>
        <summary class="cfa-20__q">Can I try before buying?<i aria-hidden="true"></i></summary>
        <div class="cfa-20__a"><p>Every plan starts with a 14-day full-featured trial, no card required. Trial workspaces convert in place — nothing to migrate when you subscribe.</p></div>
      </details>
      <details class="cfa-20__item">
        <summary class="cfa-20__q">How does seat billing work mid-month?<i aria-hidden="true"></i></summary>
        <div class="cfa-20__a"><p>Added seats are prorated to the day; removed seats credit your next invoice. The billing page shows a live preview of the next charge before you confirm anything.</p></div>
      </details>
      <details class="cfa-20__item">
        <summary class="cfa-20__q">Do you have an uptime SLA?<i aria-hidden="true"></i></summary>
        <div class="cfa-20__a"><p>99.9% on Business, 99.99% on Enterprise, both with service credits. The status page keeps five years of incident history public — judge us on it.</p></div>
      </details>
      <details class="cfa-20__item">
        <summary class="cfa-20__q">Can I export my data?<i aria-hidden="true"></i></summary>
        <div class="cfa-20__a"><p>Anytime, in full: JSON, CSV and attachments via one-click export or the API. Your data is yours — leaving must be easy for staying to mean anything.</p></div>
      </details>
    </div>
    <aside class="cfa-20__cta">
      <div class="cfa-20__avatars" aria-hidden="true">
        <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=200&auto=format&fit=crop" width="44" height="44" alt="">
        <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop" width="44" height="44" alt="">
        <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=200&auto=format&fit=crop" width="44" height="44" alt="">
      </div>
      <h2>Still have questions?</h2>
      <p>Our support team replies within 4 hours, every day including weekends.</p>
      <div class="cfa-20__actions">
        <a class="cfa-20__primary" href="#cfa20-chat">Chat with us</a>
        <a class="cfa-20__secondary" href="mailto:[email protected]">[email protected]</a>
      </div>
    </aside>
    <p class="cfa-20__foot">The CTA sits after the list on purpose — it catches users at the exact moment the answers ran out. CodeFronts collection.</p>
  </div>
</section>
```
## CSS
```css
.cfa-20,
.cfa-20 *,
.cfa-20 *::before,
.cfa-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-20 {
  --bg: oklch(0.975 0.008 75);
  --panel: oklch(1 0 0);
  --ink: oklch(0.25 0.025 55);
  --mut: oklch(0.5 0.025 55);
  --line: oklch(0.89 0.015 70);
  --acc: oklch(0.6 0.16 50);
  --cta-bg: oklch(0.25 0.04 55);
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

.cfa-20__wrap {
  width: min(100%,640px);
}

.cfa-20__head h1 {
  font-size: clamp(26px,4.5cqi,38px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-20__head p {
  margin-top: 8px;
  font-size: 14.5px;
  color: var(--mut);
}

.cfa-20__list {
  margin-top: 24px;
  display: flex;
  flex-direction: column;
  gap: 9px;
  interpolate-size: allow-keywords;
}

.cfa-20__item {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 13px;
  transition: border-color .3s;
}

.cfa-20__item[open] {
  border-color: color-mix(in oklch,var(--acc) 40%,var(--line));
}

.cfa-20__q {
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

.cfa-20__q::-webkit-details-marker {
  display: none;
}

.cfa-20__q:hover {
  color: var(--acc);
}

.cfa-20__q:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 13px;
}

.cfa-20__q i {
  flex: none;
  width: 8px;
  height: 8px;
  border-right: 2px solid var(--acc);
  border-bottom: 2px solid var(--acc);
  rotate: 45deg;
  translate: 0 -2px;
  transition: rotate .35s;
}

.cfa-20__item[open] .cfa-20__q i {
  rotate: 225deg;
  translate: 0 2px;
}

.cfa-20__a p {
  padding: 0 17px 16px;
  font-size: 13.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 60ch;
}

@supports (interpolate-size: allow-keywords) {
  .cfa-20__item::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .35s cubic-bezier(.4,0,.2,1),opacity .3s,content-visibility .35s allow-discrete;
  }

  .cfa-20__item[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

.cfa-20__cta {
  margin-top: 22px;
  padding: 30px clamp(20px,4cqi,36px);
  border-radius: 20px;
  text-align: center;
  color: oklch(0.97 0.01 70);
  background: linear-gradient(140deg,var(--cta-bg),color-mix(in oklch,var(--cta-bg) 70%,var(--acc)));
  box-shadow: 0 20px 48px oklch(0.3 0.06 50/.25);
}

.cfa-20__avatars {
  display: flex;
  justify-content: center;
}

.cfa-20__avatars img {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: 3px solid var(--cta-bg);
  object-fit: cover;
  margin-left: -12px;
}

.cfa-20__avatars img:first-child {
  margin-left: 0;
}

.cfa-20__cta h2 {
  margin-top: 14px;
  font-size: clamp(20px,3cqi,26px);
  font-weight: 800;
  letter-spacing: -.02em;
}

.cfa-20__cta>p {
  margin-top: 7px;
  font-size: 13.5px;
  line-height: 1.6;
  color: oklch(0.85 0.02 65);
}

.cfa-20__actions {
  margin-top: 18px;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
}

.cfa-20__primary {
  display: inline-flex;
  align-items: center;
  min-height: 46px;
  padding: 0 24px;
  border-radius: 12px;
  background: oklch(0.97 0.01 70);
  color: var(--cta-bg);
  font-size: 14px;
  font-weight: 800;
  text-decoration: none;
  transition: translate .2s,box-shadow .2s;
}

.cfa-20__primary:hover,
.cfa-20__primary:focus-visible {
  translate: 0 -2px;
  box-shadow: 0 10px 24px oklch(0.1 0.03 50/.35);
}

.cfa-20__primary:focus-visible {
  outline: 2px solid oklch(0.97 0.01 70);
  outline-offset: 3px;
}

.cfa-20__secondary {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  color: oklch(0.9 0.03 60);
  font-size: 13.5px;
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 4px;
  transition: color .2s;
}

.cfa-20__secondary:hover,
.cfa-20__secondary:focus-visible {
  color: oklch(0.97 0.01 70);
}

.cfa-20__secondary:focus-visible {
  outline: 2px solid oklch(0.9 0.03 60);
  outline-offset: 3px;
  border-radius: 6px;
}

.cfa-20__foot {
  margin-top: 20px;
  font-size: 12.5px;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-20 *,
    .cfa-20 .cfa-20__item::details-content {
    transition-duration: .01ms !important;
  }
}
```
