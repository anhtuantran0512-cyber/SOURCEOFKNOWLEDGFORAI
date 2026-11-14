---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/css-feature-section-with-floating-mockup/"
title: "Feature Section with Floating Phone Mockup"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "A split feature block with three callouts on the left and a phone drawn entirely in CSS on the right, tilted a few degrees and floating on a soft contact…"
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Feature Section with Floating Phone Mockup
Source: https://codefronts.com/layouts/css-feature-sections/css-feature-section-with-floating-mockup/

A split feature block with three callouts on the left and a phone drawn entirely in CSS on the right, tilted a few degrees and floating on a soft contact shadow. The frame, bezel, notch and app screen are all elements — no image, no 4MB PNG, no export cycle — so the screen content is real text that reflows and stays readable at any size.
## HTML
```html
<section class="fs-21" aria-labelledby="fs-21-heading">
  <div class="fs-21__hero" aria-hidden="true">
    <span class="fs-21__wordmark">Sundial</span>
    <span class="fs-21__heronav">For freelancers who invoice</span>
  </div>

  <div class="fs-21__stage">
    <div class="fs-21__split">
      <div class="fs-21__copy">
        <p class="fs-21__eyebrow">On the phone</p>
        <h2 class="fs-21__heading" id="fs-21-heading">Your books, closed before you leave the site</h2>
        <p class="fs-21__intro">Sundial turns the hour you spend on admin every evening into the ninety seconds it should be.</p>
        <ul class="fs-21__callouts">
          <li class="fs-21__callout">
            <span class="fs-21__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="4" y="4" width="16" height="16" rx="3"/><path d="M8 10h8M8 14h5"/></svg></span>
            <div><h3 class="fs-21__ctitle">Invoice from the job, not the desk</h3><p class="fs-21__cprose">Finish a job, tap once, and the invoice goes out with the hours and parts already filled in.</p></div>
          </li>
          <li class="fs-21__callout">
            <span class="fs-21__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M12 3v18M7 8h10M7 16h10"/></svg></span>
            <div><h3 class="fs-21__ctitle">Chasing that you do not do</h3><p class="fs-21__cprose">Polite reminders at seven, fourteen and thirty days, stopping the moment the money lands.</p></div>
          </li>
          <li class="fs-21__callout">
            <span class="fs-21__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M4 18V9M10 18V5M16 18v-6M3 21h18"/></svg></span>
            <div><h3 class="fs-21__ctitle">Tax set aside as you earn</h3><p class="fs-21__cprose">A running estimate with a pot that fills automatically, so January is a formality.</p></div>
          </li>
        </ul>
        <a class="fs-21__cta" href="#fs-21-heading">Try it on your next invoice</a>
      </div>

      <div class="fs-21__mockwrap" aria-hidden="true">
        <div class="fs-21__phone">
          <span class="fs-21__notch"></span>
          <div class="fs-21__screen">
            <div class="fs-21__apphead"><b>This month</b><span>August</span></div>
            <div class="fs-21__balance">
              <span class="fs-21__blabel">Paid</span>
              <span class="fs-21__bvalue">£8,420</span>
              <span class="fs-21__bmeta">£2,160 outstanding · 3 invoices</span>
            </div>
            <div class="fs-21__txns">
              <div class="fs-21__txn"><b>Fern Studio</b><i>£1,200 · paid</i></div>
              <div class="fs-21__txn"><b>Orbit Ltd</b><i>£860 · due in 4d</i></div>
              <div class="fs-21__txn fs-21__txn--late"><b>Vale &amp; Co</b><i>£1,300 · 12d late</i></div>
              <div class="fs-21__txn"><b>Basalt Group</b><i>£2,240 · paid</i></div>
            </div>
            <div class="fs-21__tabs"><span class="fs-21__tab" data-on></span><span class="fs-21__tab"></span><span class="fs-21__tab"></span></div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="fs-21__below" aria-hidden="true">iOS and Android · Free for your first five invoices</div>
</section>
```
## CSS
```css
.fs-21 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #f4f2ef;
  --page: oklch(0.965 0.005 70);
  --card: #ffffff;
  --ink: #191817;
  --ink: oklch(0.22 0.004 60);
  --muted: #57534d;
  --muted: oklch(0.47 0.008 65);
  --rule: #e0dcd6;
  --rule: oklch(0.89 0.007 70);
  --accent: #e2604a;
  --accent: oklch(0.65 0.16 30);
  --screen: #faf8f5;
  --phone-w: 268px;
  --tilt: -4deg;
  --font-display: "Iowan Old Style", Georgia, "Times New Roman", serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-21 *,
.fs-21 *::before,
.fs-21 *::after {
  box-sizing: border-box;
}

.fs-21__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
  justify-content: space-between;
  align-items: baseline;
  padding: 20px 24px;
  border-block-end: 1px solid var(--rule);
}

.fs-21__wordmark {
  font: 400 20px/1 var(--font-display);
  letter-spacing: -0.01em;
}

.fs-21__heronav {
  font-size: 12.5px;
  color: var(--muted);
}

.fs-21__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  padding: clamp(30px, 6vw, 68px) 20px;
}

.fs-21__split {
  inline-size: 100%;
  max-inline-size: 64rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr);
  gap: clamp(24px, 5vw, 56px);
  align-items: center;
}

.fs-21__copy {
  min-inline-size: 0;
}

.fs-21__eyebrow {
  margin: 0 0 14px;
  font: 700 10.5px/1 system-ui, sans-serif;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--accent);
}

.fs-21__heading {
  margin: 0 0 14px;
  max-inline-size: 24ch;
  font: 400 clamp(27px, 5vw, 42px)/1.08 var(--font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.fs-21__intro {
  margin: 0 0 26px;
  max-inline-size: 46ch;
  font-size: 15px;
  line-height: 1.7;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-21__callouts {
  margin: 0 0 28px;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 18px;
}

.fs-21__callout {
  display: grid;
  grid-template-columns: 38px minmax(0, 1fr);
  gap: 14px;
  align-items: start;
}

.fs-21__icon {
  display: grid;
  place-items: center;
  inline-size: 38px;
  block-size: 38px;
  border-radius: 50%;
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 12%, var(--page));
}

.fs-21__ctitle {
  margin: 0 0 5px;
  font: 600 15.5px/1.3 system-ui, sans-serif;
  letter-spacing: -0.01em;
}

.fs-21__cprose {
  margin: 0;
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-21__cta {
  display: inline-flex;
  align-items: center;
  min-height: 48px;
  padding: 0 22px;
  font: 600 14px/1 system-ui, sans-serif;
  color: var(--card);
  background: var(--ink);
  border-radius: 999px;
  text-decoration: none;
}

.fs-21__cta:hover {
  background: var(--accent);
}

.fs-21__cta:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fs-21__mockwrap {
  display: grid;
  place-items: center;
  min-inline-size: 0;
  transform: rotate(var(--tilt));
}

.fs-21__phone {
  position: relative;
  inline-size: var(--phone-w);
  max-inline-size: 100%;
  aspect-ratio: 9 / 18.5;
  padding: 11px;
  background: #1d1c1b;
  background: color-mix(in oklab, var(--ink) 92%, black);
  border-radius: 40px;
  box-shadow: inset 0 0 0 1.5px rgba(255, 255, 255, 0.14);
  filter: drop-shadow(0 26px 30px rgba(25, 24, 23, 0.28)) drop-shadow(0 6px 10px rgba(25, 24, 23, 0.18));
}

.fs-21__notch {
  position: absolute;
  inset-block-start: 15px;
  inset-inline-start: 50%;
  translate: -50% 0;
  inline-size: 62px;
  block-size: 6px;
  border-radius: 99px;
  background: rgba(255, 255, 255, 0.22);
}

.fs-21__screen {
  block-size: 100%;
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 26px 13px 13px;
  background: var(--screen);
  border-radius: 30px;
  overflow: hidden;
}

.fs-21__apphead {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  font-size: 11px;
  color: var(--muted);
}

.fs-21__apphead b {
  font: 400 15px/1 var(--font-display);
  color: var(--ink);
}

.fs-21__balance {
  padding: 13px;
  border-radius: 14px;
  background: var(--ink);
  color: var(--screen);
  display: grid;
  gap: 3px;
}

.fs-21__blabel {
  font-size: 9.5px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  opacity: 0.7;
}

.fs-21__bvalue {
  font: 400 26px/1 var(--font-display);
  letter-spacing: -0.02em;
}

.fs-21__bmeta {
  font-size: 10px;
  opacity: 0.78;
}

.fs-21__txns {
  display: grid;
  gap: 6px;
}

.fs-21__txn {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 8px;
  padding: 9px 11px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 10px;
}

.fs-21__txn b {
  font-size: 11.5px;
  font-weight: 600;
  min-inline-size: 0;
}

.fs-21__txn i {
  font-style: normal;
  font-size: 10px;
  color: var(--muted);
}

.fs-21__txn--late {
  border-color: color-mix(in oklab, var(--accent) 45%, var(--rule));
  background: color-mix(in oklab, var(--accent) 8%, var(--card));
}

.fs-21__txn--late i {
  color: color-mix(in oklab, var(--accent) 80%, black);
}

.fs-21__tabs {
  display: flex;
  gap: 6px;
  justify-content: center;
  margin-block-start: auto;
  padding-block-start: 10px;
  border-block-start: 1px solid var(--rule);
}

.fs-21__tab {
  inline-size: 26px;
  block-size: 4px;
  border-radius: 99px;
  background: var(--rule);
}

.fs-21__tab[data-on] {
  background: var(--accent);
}

.fs-21__below {
  padding: 18px 24px;
  border-block-start: 1px solid var(--rule);
  font-size: 12.5px;
  color: var(--muted);
}

@media (max-width: 860px) {
  .fs-21__split {
    grid-template-columns: minmax(0, 1fr);
  }

  .fs-21 {
    --phone-w: 232px;
  }
}

@media (max-width: 640px) {
  .fs-21__mockwrap {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fs-21__mockwrap {
    transform: none;
  }
}

@media (prefers-color-scheme: dark) {
  .fs-21 {
    --page: #131211;
    --card: #1c1a18;
    --ink: #f3f0eb;
    --muted: #a49c92;
    --rule: #2c2926;
    --accent: #ff8168;
    --screen: #201d1a;
  }

  .fs-21__phone {
    background: #0b0a09;
    box-shadow: inset 0 0 0 1.5px rgba(255, 255, 255, 0.1);
    filter: drop-shadow(0 26px 34px rgba(0, 0, 0, 0.6));
  }

  .fs-21__balance {
    background: var(--accent);
    color: #1a1210;
  }

  .fs-21__cta {
    color: #131211;
    background: var(--ink);
  }
}

[data-theme="dark"] .fs-21 {
  --page: #131211;
  --card: #1c1a18;
  --ink: #f3f0eb;
  --muted: #a49c92;
  --rule: #2c2926;
  --accent: #ff8168;
  --screen: #201d1a;
}

[data-theme="dark"] .fs-21 .fs-21__cta {
  color: #131211;
  background: var(--ink);
}
```
