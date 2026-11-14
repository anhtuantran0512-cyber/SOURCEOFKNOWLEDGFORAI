---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/numbered-steps/"
title: "Numbered Steps Accordion — Process Timeline for Onboarding Flows"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "An accordion that reads as a process: oversized 01–04 step numerals in circles joined by a vertical connector line, with the open step's circle filling in…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Numbered Steps Accordion — Process Timeline for Onboarding Flows
Source: https://codefronts.com/navigation/css-accordions/numbered-steps/

An accordion that reads as a process: oversized 01–04 step numerals in circles joined by a vertical connector line, with the open step's circle filling in accent and its number knocked out white. The go-to pattern for onboarding checklists, how-it-works sections and multi-stage service explainers.
## HTML
```html
<section class="acc-08" aria-label="Numbered steps accordion demo">
  <div class="acc-08__wrap">
    <p class="acc-08__kicker">Getting started</p>
    <h3 class="acc-08__title">Up and running in four steps</h3>
    <details class="acc-08__step" name="acc-08-steps" open>
      <summary class="acc-08__sum"><span class="acc-08__num">01</span><span class="acc-08__lab">Create your workspace</span></summary>
      <div class="acc-08__body"><p>Pick a workspace URL and invite your first teammates. Everything is soft-deletable for 30 days, so explore freely.</p></div>
    </details>
    <details class="acc-08__step" name="acc-08-steps">
      <summary class="acc-08__sum"><span class="acc-08__num">02</span><span class="acc-08__lab">Connect your data</span></summary>
      <div class="acc-08__body"><p>OAuth into your warehouse or drop a CSV. Schemas are inferred automatically and every column gets a profiling report.</p></div>
    </details>
    <details class="acc-08__step" name="acc-08-steps">
      <summary class="acc-08__sum"><span class="acc-08__num">03</span><span class="acc-08__lab">Build your first dashboard</span></summary>
      <div class="acc-08__body"><p>Start from a template or a blank canvas. Charts stay linked to source queries, so refreshed data flows through instantly.</p></div>
    </details>
    <details class="acc-08__step" name="acc-08-steps">
      <summary class="acc-08__sum"><span class="acc-08__num">04</span><span class="acc-08__lab">Share with your team</span></summary>
      <div class="acc-08__body"><p>Publish to a link, embed in Notion, or schedule a Monday-morning email digest. Viewers don't need a seat.</p></div>
    </details>
  </div>
</section>
```
## CSS
```css
.acc-08,
.acc-08 *,
.acc-08 *::before,
.acc-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-08 {
  --accent: oklch(0.55 0.18 25);
  --dot: 44px;
  --line-w: 2px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #faf5f2;
  padding: 40px 20px;
}

.acc-08__wrap {
  width: min(560px,100%);
  background: #fff;
  border-radius: 20px;
  padding: 38px 36px;
  box-shadow: 0 24px 60px -34px rgba(80,30,20,.3);
}

.acc-08__kicker {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.acc-08__title {
  font-size: 25px;
  font-weight: 800;
  color: #2b1d18;
  letter-spacing: -.02em;
  margin: 6px 0 22px;
}

.acc-08__step {
  position: relative;
  padding-bottom: 8px;
}

.acc-08__step::before {
  content: "";
  position: absolute;
  left: calc(var(--dot)/2 - var(--line-w)/2);
  top: var(--dot);
  bottom: -6px;
  width: var(--line-w);
  background: #eadfd8;
}

.acc-08__step:last-of-type::before {
  display: none;
}

.acc-08__sum {
  list-style: none;
  display: grid;
  grid-template-columns: var(--dot) 1fr;
  align-items: center;
  gap: 16px;
  min-height: 56px;
  cursor: pointer;
}

.acc-08__sum::-webkit-details-marker {
  display: none;
}

.acc-08__sum::marker {
  content: "";
}

.acc-08__num {
  width: var(--dot);
  height: var(--dot);
  display: grid;
  place-content: center;
  border: var(--line-w) solid #e3d4cb;
  border-radius: 50%;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 14px;
  font-weight: 700;
  color: #a08575;
  background: #fff;
  transition: all .3s cubic-bezier(.4,0,.2,1);
  position: relative;
  z-index: 1;
}

.acc-08__lab {
  font-size: 17px;
  font-weight: 700;
  color: #2b1d18;
  transition: color .2s;
}

.acc-08__sum:hover .acc-08__num {
  border-color: var(--accent);
  color: var(--accent);
}

.acc-08__step[open] .acc-08__num {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
  transform: scale(1.06);
}

.acc-08__step[open] .acc-08__lab {
  color: var(--accent);
}

.acc-08__body {
  display: grid;
  grid-template-columns: var(--dot) 1fr;
  gap: 16px;
}

.acc-08__body p {
  grid-column: 2;
  padding: 6px 8px 16px 0;
  font-size: 14.5px;
  line-height: 1.65;
  color: #5d4c42;
}

.acc-08__step[open] .acc-08__body {
  animation: acc-08-in .4s cubic-bezier(.2,.7,.3,1);
}

@keyframes acc-08-in {
  from {
    opacity: 0;
    translate: 0 -6px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.acc-08__sum:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  border-radius: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-08__num {
    transition: none;
  }

  .acc-08__step[open] .acc-08__body {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — per-item ::before segments draw the timeline connector, details[open] fills the step circle, and name="acc-08-steps" keeps one step focal at a time. */
```
