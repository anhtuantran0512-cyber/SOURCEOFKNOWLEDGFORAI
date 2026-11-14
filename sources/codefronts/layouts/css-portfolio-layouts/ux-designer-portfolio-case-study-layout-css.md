---
source: "codefronts"
url: "https://codefronts.com/layouts/css-portfolio-layouts/ux-designer-portfolio-case-study-layout-css/"
title: "UX Designer Portfolio Case Study Layout CSS"
section: "layouts"
category: "css-portfolio-layouts"
category_name: "CSS Portfolio Layouts"
description: "The case-study page hiring managers actually want to read: a header that states role, team and timeline up front; a three-stat outcome strip (the numbers…"
has_js: "false"
---

Here's a working CSS Portfolio Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: UX Designer Portfolio Case Study Layout CSS
Source: https://codefronts.com/layouts/css-portfolio-layouts/ux-designer-portfolio-case-study-layout-css/

The case-study page hiring managers actually want to read: a header that states role, team and timeline up front; a three-stat outcome strip (the numbers first, not last); a problem statement set as a real pull quote; a wireframe evidence grid; and a numbered process rail drawn entirely with CSS counters. The measure is capped at 62ch because case studies are reading, and reading has rules.
## HTML
```html
<section class="cpl-10" aria-label="UX case study layout demo">
  <div class="cpl-10__stage">
    <article class="cpl-10__study">
      <header class="cpl-10__head">
        <p class="cpl-10__crumb"><a href="#work">Work</a> / Meridian Health</p>
        <h2>Rebooking a missed appointment in under a minute</h2>
        <dl class="cpl-10__facts">
          <div><dt>Role</dt><dd>Lead product designer</dd></div>
          <div><dt>Team</dt><dd>2 eng · PM · researcher</dd></div>
          <div><dt>Timeline</dt><dd>6 weeks, shipped Q2 2026</dd></div>
        </dl>
      </header>
      <div class="cpl-10__stats full">
        <div><strong>-42%</strong><span>no-show rate on rebooked slots</span></div>
        <div><strong>54s</strong><span>median rebooking time, was 4m 10s</span></div>
        <div><strong>+18</strong><span>NPS among rebooking patients</span></div>
      </div>
      <h3><i aria-hidden="true"></i>Problem</h3>
      <figure class="cpl-10__quote">
        <blockquote>Patients who missed an appointment had to phone the clinic — during the same working hours they'd missed it for.</blockquote>
        <figcaption>— Research synthesis, 14 patient interviews</figcaption>
      </figure>
      <p>Missed-appointment recovery was the clinic's largest silent revenue leak. The existing flow assumed a desktop patient portal login that 71% of patients had never activated.</p>
      <h3><i aria-hidden="true"></i>Exploration</h3>
      <div class="cpl-10__wires full">
        <figure class="cpl-10__wire" style="--n:'A'"><span>SMS deep link</span></figure>
        <figure class="cpl-10__wire" style="--n:'B'"><span>3-slot picker</span></figure>
        <figure class="cpl-10__wire cpl-10__wire--pick" style="--n:'C'"><span>One-tap confirm ✓</span></figure>
        <figure class="cpl-10__wire" style="--n:'D'"><span>Fallback: call me</span></figure>
      </div>
      <h3><i aria-hidden="true"></i>Process</h3>
      <ol class="cpl-10__steps">
        <li><h4>Shadow the front desk</h4><p>Two days of call shadowing put a number on it: 40% of inbound calls were rebooking.</p></li>
        <li><h4>Prototype against real slots</h4><p>Wizard-of-Oz SMS prototype with live calendar data — 9 of 11 patients rebooked unaided.</p></li>
        <li><h4>Cut the flow to three taps</h4><p>Dropped account creation entirely; the appointment token in the SMS is the auth.</p></li>
        <li><h4>Instrument and ship</h4><p>Events on every step; the 54s median comes from the first 6 weeks of production data.</p></li>
      </ol>
      <h3><i aria-hidden="true"></i>Outcome</h3>
      <p>The three-tap flow now handles 83% of rebookings with no human in the loop. Front-desk call volume dropped enough to remove the overflow answering service — the feature paid for itself in nine weeks.</p>
      <nav class="cpl-10__next full" aria-label="More case studies">
        <a href="#prev">← Sift error language</a>
        <a href="#next">Fieldnote design system →</a>
      </nav>
    </article>
  </div>
</section>
```
## CSS
```css
.cpl-10,
.cpl-10 *,
.cpl-10 *::before,
.cpl-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpl-10 {
  --bg: oklch(0.98 0.004 90);
  --ink: oklch(0.25 0.02 270);
  --mut: oklch(0.53 0.015 270);
  --line: oklch(0.9 0.008 270);
  --acc: oklch(0.55 0.16 250);
  --wash: oklch(0.94 0.01 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cpl-10__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.cpl-10__study {
  display: grid;
  grid-template-columns: 1fr min(62ch,100%) 1fr;
  row-gap: 18px;
  padding: clamp(22px,4cqi,36px) clamp(16px,3cqi,26px) 40px;
}

.cpl-10__study>* {
  grid-column: 2;
}

.cpl-10__study>.full {
  grid-column: 1/-1;
}

.cpl-10__crumb {
  font-size: 12px;
  color: var(--mut);
}

.cpl-10__crumb a {
  color: var(--acc);
  text-decoration: none;
  font-weight: 600;
  padding: 4px 0;
}

.cpl-10__crumb a:hover,
.cpl-10__crumb a:focus-visible {
  text-decoration: underline;
  text-underline-offset: 3px;
}

.cpl-10__head h2 {
  font-size: clamp(22px,3.6cqi,30px);
  line-height: 1.15;
  letter-spacing: -.025em;
  margin-top: 8px;
  text-wrap: balance;
}

.cpl-10__facts {
  display: flex;
  flex-wrap: wrap;
  gap: 10px 28px;
  margin-top: 16px;
}

.cpl-10__facts dt {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--mut);
}

.cpl-10__facts dd {
  font-size: 13px;
  font-weight: 600;
  margin-top: 2px;
}

.cpl-10__stats {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(170px,100%),1fr));
  gap: 10px;
  padding: 16px;
  border-radius: 16px;
  background: linear-gradient(135deg,var(--wash),oklch(0.95 0.015 280));
  margin-top: 6px;
}

.cpl-10__stats div {
  display: grid;
  gap: 2px;
  padding: 8px 12px;
}

.cpl-10__stats strong {
  font-size: 29px;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
  color: var(--acc);
}

.cpl-10__stats span {
  font-size: 12px;
  line-height: 1.4;
  color: var(--mut);
}

.cpl-10__study h3 {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--mut);
  margin-top: 14px;
}

.cpl-10__study h3 i {
  width: 22px;
  height: 2px;
  border-radius: 2px;
  background: var(--acc);
}

.cpl-10__quote {
  padding: 4px 0 4px 20px;
  border-left: 3px solid var(--acc);
}

.cpl-10__quote blockquote {
  font-size: 17.5px;
  line-height: 1.45;
  letter-spacing: -.01em;
  font-weight: 600;
  text-wrap: pretty;
}

.cpl-10__quote figcaption {
  margin-top: 8px;
  font-size: 12px;
  color: var(--mut);
}

.cpl-10__study p {
  font-size: 14px;
  line-height: 1.7;
  color: oklch(0.4 0.015 270);
  text-wrap: pretty;
}

.cpl-10__wires {
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(min(150px,100%),1fr));
  gap: 10px;
  margin-top: 6px;
}

.cpl-10__wire {
  position: relative;
  aspect-ratio: 3/4;
  border-radius: 12px;
  background: var(--wash);
  border: 1.5px dashed oklch(0.75 0.03 250);
  display: grid;
  place-items: end center;
  padding: 12px;
  transition: border-color .2s,translate .2s;
}

.cpl-10__wire::before {
  content: var(--n);
  position: absolute;
  top: 10px;
  left: 12px;
  font-size: 11px;
  font-weight: 800;
  color: var(--mut);
}

.cpl-10__wire span {
  font-size: 11.5px;
  font-weight: 600;
  color: var(--mut);
  text-align: center;
}

.cpl-10__wire:hover {
  translate: 0 -2px;
  border-color: var(--acc);
}

.cpl-10__wire--pick {
  border-style: solid;
  border-color: var(--acc);
  background: oklch(0.93 0.03 250);
}

.cpl-10__wire--pick span {
  color: var(--acc);
}

.cpl-10__steps {
  list-style: none;
  counter-reset: cpl10;
  display: grid;
  gap: 14px;
}

.cpl-10__steps li {
  counter-increment: cpl10;
  display: grid;
  grid-template-columns: 34px 1fr;
  gap: 2px 14px;
}

.cpl-10__steps li::before {
  content: counter(cpl10,decimal-leading-zero);
  grid-row: span 2;
  font-size: 12px;
  font-weight: 800;
  color: var(--acc);
  font-variant-numeric: tabular-nums;
  border: 1px solid var(--line);
  border-radius: 9px;
  width: 34px;
  height: 34px;
  display: grid;
  place-items: center;
}

.cpl-10__steps h4 {
  font-size: 14.5px;
  letter-spacing: -.01em;
  align-self: center;
}

.cpl-10__steps p {
  font-size: 13px !important;
  grid-column: 2;
}

.cpl-10__next {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 16px;
  padding-top: 18px;
  border-top: 1px solid var(--line);
}

.cpl-10__next a {
  font-size: 13px;
  font-weight: 700;
  color: var(--ink);
  text-decoration: none;
  padding: 8px 0;
  transition: color .2s;
}

.cpl-10__next a:hover,
.cpl-10__next a:focus-visible {
  color: var(--acc);
}

.cpl-10__next a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .cpl-10 * {
    transition-duration: .01ms !important;
  }
}
```
