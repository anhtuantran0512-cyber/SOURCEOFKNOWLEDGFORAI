---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/css-alert-banner-with-icon-alignment/"
title: "Alert Banner with Icon Alignment"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "The alignment problem every design system hits: an icon next to text that must stay optically centred on the first line, not on the whole block, and not…"
has_js: "false"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Alert Banner with Icon Alignment
Source: https://codefronts.com/snippets/css-banners-alerts/css-alert-banner-with-icon-alignment/

The alignment problem every design system hits: an icon next to text that must stay optically centred on the first line, not on the whole block, and not drift when the text wraps to three lines. Solved properly with the lh unit — calc((1lh - var(--icon)) / 2) — and shown against the two wrong ways so the difference is impossible to unsee.
## HTML
```html
<div class="ba-15">
  <div class="ba-15__stack">
    <div class="ba-15__alert" data-variant="info" role="status">
      <div class="ba-15__row">
        <svg class="ba-15__icon" viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="7.6" stroke="currentColor" stroke-width="1.6"/><path d="M10 9.2v4.4M10 6.5h.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <div class="ba-15__text">
          <p class="ba-15__title">Single line: the icon sits on the optical centre of the line box</p>
        </div>
      </div>
    </div>

    <div class="ba-15__alert" data-variant="warning" role="status">
      <div class="ba-15__row">
        <svg class="ba-15__icon" viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="M10 3.2 17.6 16.4H2.4z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M10 8v3.6M10 13.9h.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <div class="ba-15__text">
          <p class="ba-15__title">Multi-line: the icon stays on the first line</p>
          <p class="ba-15__body">Because the offset is <code>calc((1lh - var(--icon)) / 2)</code> it tracks the line box, not the block. Add a paragraph, change the font size, switch to a condensed face — the icon does not move relative to the first line of text.</p>
        </div>
      </div>
    </div>

    <div class="ba-15__alert" data-variant="success" role="status">
      <div class="ba-15__row">
        <svg class="ba-15__icon" viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="7.6" stroke="currentColor" stroke-width="1.6"/><path d="m6.6 10.4 2.5 2.5 4.7-5.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div class="ba-15__text">
          <p class="ba-15__title">With a heading and actions</p>
          <p class="ba-15__body">The text column carries <code>min-width:0</code>, so a long unbroken token like <code>https://status.example.com/incidents/2026-08-10-eu-west-1-write-latency</code> wraps instead of widening the grid.</p>
          <p class="ba-15__acts"><a href="#ba-15-a">View incident</a><a href="#ba-15-a">Subscribe to updates</a></p>
        </div>
      </div>
    </div>

    <div class="ba-15__alert" data-variant="danger" data-dense="true" role="status">
      <div class="ba-15__row">
        <svg class="ba-15__icon" viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="7.6" stroke="currentColor" stroke-width="1.6"/><path d="m7.4 7.4 5.2 5.2m0-5.2-5.2 5.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <div class="ba-15__text">
          <p class="ba-15__title">Dense variant, smaller icon and type</p>
          <p class="ba-15__body">Same rule, different tokens: <code>--icon:1rem</code> and a 13px body. Nothing was overridden.</p>
        </div>
      </div>
    </div>

    <div class="ba-15__compare">
      <div class="ba-15__alert ba-15__alert--wrong" data-variant="info" data-how="center">
        <div class="ba-15__row">
          <svg class="ba-15__icon" viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="7.6" stroke="currentColor" stroke-width="1.6"/><path d="M10 9.2v4.4M10 6.5h.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          <div class="ba-15__text">
            <p class="ba-15__title"><span class="ba-15__flag">align-items: center</span></p>
            <p class="ba-15__body">Centred on the block, so the icon drifts downwards as soon as the copy runs to a second or third line. This is the default mistake.</p>
          </div>
        </div>
      </div>

      <div class="ba-15__alert ba-15__alert--wrong" data-variant="info" data-how="hard">
        <div class="ba-15__row">
          <svg class="ba-15__icon" viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="7.6" stroke="currentColor" stroke-width="1.6"/><path d="M10 9.2v4.4M10 6.5h.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          <div class="ba-15__text">
            <p class="ba-15__title"><span class="ba-15__flag">margin-block-start: 3px</span></p>
            <p class="ba-15__body">Correct at exactly one font size. Change the scale, or let a user zoom text, and it is wrong again — with no way for the component to know.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

.ba-15 {
  --bg: #f5f6f8;
  --surface: #ffffff;
  --ink: #0f1216;
  --muted: #5f6773;
  --line: #e2e5ea;
  --blue: #2563eb;
  --green: #0f9d58;
  --amber: #d97706;
  --red: #dc2626;
  --sans: "Instrument Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  box-sizing: border-box;
  padding: clamp(1rem,4vw,3rem);
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.ba-15 *,
.ba-15 *::before,
.ba-15 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-15 {
    --bg: oklch(97% .005 265);
    --surface: oklch(100% 0 0);
    --ink: oklch(19% .014 265);
    --muted: oklch(55% .016 265);
    --line: oklch(91% .01 265);
    --blue: oklch(55% .2 262);
    --green: oklch(60% .16 150);
    --amber: oklch(65% .16 62);
    --red: oklch(57% .21 27);
  }
}

@media (prefers-color-scheme: dark) {
  .ba-15:not([data-theme="light"]) {
    --bg: #0b0d11;
    --surface: #14171d;
    --ink: #eef1f5;
    --muted: #98a0ac;
    --line: #232830;
  }
}

.ba-15[data-theme="dark"] {
  --bg: #0b0d11;
  --surface: #14171d;
  --ink: #eef1f5;
  --muted: #98a0ac;
  --line: #232830;
}

.ba-15__stack {
  width: min(46rem,100%);
  display: grid;
  gap: .85rem;
}

.ba-15__alert {
  --v: var(--blue);
  --icon: 1.25rem;
  --gap: .8rem;
  padding: 1rem 1.1rem;
  border-radius: 1rem;
  background: color-mix(in oklab,var(--v) 8%,var(--surface));
  border: 1px solid color-mix(in oklab,var(--v) 26%,var(--line));
  box-shadow: 0 1px 2px rgb(15 18 22 / .04);
}

.ba-15__alert[data-variant="success"] {
  --v: var(--green);
}

.ba-15__alert[data-variant="warning"] {
  --v: var(--amber);
}

.ba-15__alert[data-variant="danger"] {
  --v: var(--red);
}

.ba-15__alert[data-dense="true"] {
  --icon: 1rem;
  padding: .75rem .85rem;
}

.ba-15__alert[data-dense="true"] .ba-15__title {
  font-size: .8125rem;
}

.ba-15__alert[data-dense="true"] .ba-15__body {
  font-size: .8125rem;
}

.ba-15__row {
  display: grid;
  grid-template-columns: auto minmax(0,1fr);
  gap: var(--gap);
  align-items: start;
}

.ba-15__icon {
  inline-size: var(--icon);
  block-size: var(--icon);
  flex: none;
  color: var(--v);
  margin-block-start: calc((1.5em - var(--icon)) / 2);
}

@supports (margin-block-start: calc((1lh - 1rem) / 2)) {
  .ba-15__icon {
    margin-block-start: calc((1lh - var(--icon)) / 2);
  }
}

.ba-15__text {
  min-width: 0;
  display: grid;
  gap: .3rem;
}

.ba-15__title {
  margin: 0;
  font-size: .9375rem;
  font-weight: 650;
  line-height: 1.5;
  letter-spacing: -.015em;
  color: color-mix(in oklab,var(--v) 55%,var(--ink));
  text-wrap: pretty;
}

@supports (text-box-trim: trim-both) {
  .ba-15__title {
    text-box-trim: trim-both;
    text-box-edge: cap alphabetic;
  }

  .ba-15__text {
    gap: .55rem;
  }
}

.ba-15__body {
  margin: 0;
  font-size: .875rem;
  line-height: 1.55;
  color: var(--muted);
  max-width: 68ch;
  text-wrap: pretty;
  overflow-wrap: anywhere;
}

.ba-15__body code,
.ba-15__title code {
  font-family: var(--mono);
  font-size: .85em;
  padding: .1em .3em;
  border-radius: .3rem;
  background: color-mix(in oklab,var(--ink) 8%,transparent);
  overflow-wrap: anywhere;
}

.ba-15__acts {
  margin: .2rem 0 0;
  display: flex;
  flex-wrap: wrap;
  gap: .85rem;
}

.ba-15__acts a {
  font-size: .8125rem;
  font-weight: 600;
  color: var(--v);
  text-decoration: underline;
  text-underline-offset: 3px;
  text-decoration-thickness: 1.5px;
}

.ba-15__acts a:hover {
  text-decoration-thickness: 2.5px;
}

.ba-15__compare {
  display: grid;
  gap: .85rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,18rem),1fr));
  margin-block-start: .5rem;
}

.ba-15__alert--wrong {
  background: var(--surface);
  border-style: dashed;
  border-color: color-mix(in oklab,var(--ink) 18%,transparent);
}

.ba-15__alert--wrong .ba-15__icon {
  color: color-mix(in oklab,var(--ink) 45%,transparent);
}

.ba-15__alert--wrong .ba-15__title {
  color: var(--ink);
}

.ba-15__alert[data-how="center"] .ba-15__row {
  align-items: center;
}

.ba-15__alert[data-how="center"] .ba-15__icon {
  margin-block-start: 0;
}

.ba-15__alert[data-how="hard"] .ba-15__icon {
  margin-block-start: 3px;
}

.ba-15__flag {
  display: inline-block;
  font-family: var(--mono);
  font-size: .6875rem;
  font-weight: 500;
  padding: .2rem .4rem;
  border-radius: .35rem;
  letter-spacing: -.01em;
  color: var(--muted);
  background: color-mix(in oklab,var(--ink) 8%,transparent);
}

.ba-15 a {
  color: var(--blue);
}

.ba-15 :focus-visible {
  outline: 2px solid var(--blue);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .ba-15 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .ba-15__alert {
    border: 1px solid CanvasText;
  }
}
```
