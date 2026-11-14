---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/faq-with-expand-all-simultaneously-multi-open-pattern/"
title: "FAQ with Expand-All-Simultaneously Multi-Open Pattern"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "The comparison-friendly FAQ: every panel opens and stays open independently, so users can read three answers side by side — the pattern research keeps…"
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: FAQ with Expand-All-Simultaneously Multi-Open Pattern
Source: https://codefronts.com/snippets/css-faq-accordion/faq-with-expand-all-simultaneously-multi-open-pattern/

The comparison-friendly FAQ: every panel opens and stays open independently, so users can read three answers side by side — the pattern research keeps showing beats only-one-open for comprehension tasks. Built on the checkbox hack so it is pure CSS, with a live "N of 6 open" progress readout powered entirely by CSS counters and :has() — a genuinely JS-free piece of UI state that surprises most developers.
## HTML
```html
<section class="cfa-04" aria-label="Multi-open FAQ accordion with open counter">
  <div class="cfa-04__wrap">
    <header class="cfa-04__head">
      <h1>Compare answers freely</h1>
      <p>Every panel stays open independently — read across, not one-at-a-time. The counter below is pure CSS.</p>
    </header>
    <div class="cfa-04__grid">
      <div class="cfa-04__list">
        <div class="cfa-04__item">
          <input type="checkbox" id="cfa04-q1" class="cfa-04__cb" checked>
          <label class="cfa-04__q" for="cfa04-q1">What is the difference between the Starter and Pro plan?<i aria-hidden="true"></i></label>
          <div class="cfa-04__a"><div><p>Starter covers one workspace with core analytics. Pro adds unlimited workspaces, funnels, cohort reports and priority support — most teams upgrade when they hit three projects.</p></div></div>
        </div>
        <div class="cfa-04__item">
          <input type="checkbox" id="cfa04-q2" class="cfa-04__cb" checked>
          <label class="cfa-04__q" for="cfa04-q2">Which plan do agencies usually pick?<i aria-hidden="true"></i></label>
          <div class="cfa-04__a"><div><p>Agencies almost always run Pro with the client-billing add-on: each client becomes a workspace with its own invoice line, and you can hand off ownership when an engagement ends.</p></div></div>
        </div>
        <div class="cfa-04__item">
          <input type="checkbox" id="cfa04-q3" class="cfa-04__cb">
          <label class="cfa-04__q" for="cfa04-q3">Can I mix plans across one team?<i aria-hidden="true"></i></label>
          <div class="cfa-04__a"><div><p>No — a workspace has one plan for everyone in it. You can, however, run different plans on different workspaces under the same organization and consolidate the billing.</p></div></div>
        </div>
        <div class="cfa-04__item">
          <input type="checkbox" id="cfa04-q4" class="cfa-04__cb">
          <label class="cfa-04__q" for="cfa04-q4">Is there a nonprofit or education discount?<i aria-hidden="true"></i></label>
          <div class="cfa-04__a"><div><p>Registered nonprofits and accredited educators get 50% off Pro, verified once a year. Student projects are free on Starter with a .edu / .ac address.</p></div></div>
        </div>
        <div class="cfa-04__item">
          <input type="checkbox" id="cfa04-q5" class="cfa-04__cb">
          <label class="cfa-04__q" for="cfa04-q5">What happens to my data if I downgrade?<i aria-hidden="true"></i></label>
          <div class="cfa-04__a"><div><p>Nothing is deleted. Reports beyond the Starter limits freeze read-only, and re-upgrading unfreezes them instantly with full history intact.</p></div></div>
        </div>
        <div class="cfa-04__item">
          <input type="checkbox" id="cfa04-q6" class="cfa-04__cb">
          <label class="cfa-04__q" for="cfa04-q6">Do you have a public roadmap?<i aria-hidden="true"></i></label>
          <div class="cfa-04__a"><div><p>Yes — roadmap.example.com shows what is planned, building and shipped. Every feature request you upvote notifies you on release.</p></div></div>
        </div>
      </div>
      <div class="cfa-04__meta">
        <span class="cfa-04__count" aria-hidden="true"></span>
        <span class="cfa-04__hint">counted by CSS, not JS</span>
      </div>
    </div>
    <p class="cfa-04__foot">Pattern note: multi-open beats only-one-open when users compare answers. From the CodeFronts FAQ collection.</p>
  </div>
</section>
```
## CSS
```css
.cfa-04,
.cfa-04 *,
.cfa-04 *::before,
.cfa-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-04 {
  --bg: oklch(0.17 0.02 300);
  --panel: oklch(0.22 0.025 300);
  --ink: oklch(0.96 0.005 300);
  --mut: oklch(0.68 0.02 300);
  --line: oklch(0.32 0.03 300);
  --acc: oklch(0.75 0.17 330);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: radial-gradient(900px 500px at 15% 0%,oklch(0.25 0.06 330/.5),transparent 60%),var(--bg);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-04__wrap {
  width: min(100%,680px);
}

.cfa-04__head h1 {
  font-size: clamp(26px,4.5cqi,38px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-04__head p {
  margin-top: 8px;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--mut);
}

.cfa-04__grid {
  margin-top: 24px;
  display: grid;
}

.cfa-04__meta {
  order: -1;
  display: flex;
  align-items: baseline;
  gap: 10px;
  margin-bottom: 12px;
}

.cfa-04__list {
  counter-reset: cfa04open;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.cfa-04__item {
  border: 1px solid var(--line);
  border-radius: 13px;
  background: var(--panel);
  overflow: hidden;
  transition: border-color .3s;
}

.cfa-04__item:has(.cfa-04__cb:checked) {
  counter-increment: cfa04open;
  border-color: color-mix(in oklch,var(--acc) 45%,var(--line));
}

.cfa-04__count::after {
  content: counter(cfa04open) " of 6 open";
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  font-weight: 700;
  color: var(--acc);
  padding: 6px 12px;
  background: color-mix(in oklch,var(--acc) 12%,transparent);
  border-radius: 99px;
}

.cfa-04__hint {
  font-size: 11.5px;
  color: var(--mut);
  letter-spacing: .04em;
}

.cfa-04__cb {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cfa-04__q {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 44px;
  padding: 15px 17px;
  cursor: pointer;
  font-size: 15px;
  font-weight: 650;
  letter-spacing: -.01em;
  transition: color .2s;
}

.cfa-04__q:hover {
  color: var(--acc);
}

.cfa-04__cb:focus-visible + .cfa-04__q {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 13px;
}

.cfa-04__q i {
  position: relative;
  flex: none;
  width: 22px;
  height: 22px;
}

.cfa-04__q i::before,
.cfa-04__q i::after {
  content: "";
  position: absolute;
  inset: 0;
  margin: auto;
  width: 12px;
  height: 2px;
  border-radius: 2px;
  background: var(--acc);
  transition: rotate .4s cubic-bezier(.4,0,.2,1);
}

.cfa-04__q i::after {
  rotate: 90deg;
}

.cfa-04__cb:checked + .cfa-04__q i::after {
  rotate: 0deg;
}

.cfa-04__cb:checked + .cfa-04__q i::before {
  rotate: -180deg;
}

.cfa-04__a {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .4s cubic-bezier(.4,0,.2,1);
}

.cfa-04__a>div {
  overflow: hidden;
}

.cfa-04__a p {
  padding: 0 17px 16px;
  font-size: 13.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 60ch;
}

.cfa-04__cb:checked ~ .cfa-04__a {
  grid-template-rows: 1fr;
}

.cfa-04__foot {
  margin-top: 22px;
  font-size: 12.5px;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-04 * {
    transition-duration: .01ms !important;
  }
}
```
