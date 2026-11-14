---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/minimalist-border-left-css-alert/"
title: "Left Border Accent Alert"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "The quietest alert that still reads at a glance: an accent stripe on the leading edge, a hairline everywhere else, and type doing the rest."
has_js: "false"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Left Border Accent Alert
Source: https://codefronts.com/snippets/css-banners-alerts/minimalist-border-left-css-alert/

The quietest alert that still reads at a glance: an accent stripe on the leading edge, a hairline everywhere else, and type doing the rest. Built with border-inline-start rather than border-left, so it mirrors correctly in Arabic and Hebrew with no extra CSS, and each of the four variants can be dismissed with pure CSS.
## HTML
```html
<div class="ba-16">
  <div class="ba-16__stack">
    <div class="ba-16__a" data-v="info">
      <input class="ba-16__vh" type="checkbox" id="ba-16-x1">
      <p class="ba-16__label">Note</p>
      <div class="ba-16__body">
        <p class="ba-16__title">Deployments now build on Node 24 by default</p>
        <p class="ba-16__text">Existing projects keep their pinned version until you change it in project settings. Nothing rebuilds automatically.</p>
      </div>
      <label class="ba-16__x" for="ba-16-x1" tabindex="0" role="button" aria-label="Dismiss note">
        <svg viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><path d="m5 5 6 6m0-6-6 6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
      </label>
    </div>

    <div class="ba-16__a" data-v="success">
      <input class="ba-16__vh" type="checkbox" id="ba-16-x2">
      <p class="ba-16__label">Done</p>
      <div class="ba-16__body">
        <p class="ba-16__title">Custom domain verified</p>
        <p class="ba-16__text">TLS is issued and HSTS is on. The certificate renews 30 days before expiry with no action from you.</p>
      </div>
      <label class="ba-16__x" for="ba-16-x2" tabindex="0" role="button" aria-label="Dismiss confirmation">
        <svg viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><path d="m5 5 6 6m0-6-6 6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
      </label>
    </div>

    <div class="ba-16__a" data-v="warning">
      <input class="ba-16__vh" type="checkbox" id="ba-16-x3">
      <p class="ba-16__label">Check</p>
      <div class="ba-16__body">
        <p class="ba-16__title">Two environment variables are unused</p>
        <p class="ba-16__text"><code>STRIPE_LEGACY_KEY</code> and <code>SENTRY_DSN_OLD</code> have not been read in 90 days. Removing them will not trigger a rebuild.</p>
        <p class="ba-16__acts"><a href="#ba-16-a">Review variables</a><a href="#ba-16-a">Ignore for 30 days</a></p>
      </div>
      <label class="ba-16__x" for="ba-16-x3" tabindex="0" role="button" aria-label="Dismiss warning">
        <svg viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><path d="m5 5 6 6m0-6-6 6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
      </label>
    </div>

    <div class="ba-16__a" data-v="danger">
      <input class="ba-16__vh" type="checkbox" id="ba-16-x4">
      <p class="ba-16__label">Failed</p>
      <div class="ba-16__body">
        <p class="ba-16__title">Build 4,281 failed in 38 seconds</p>
        <p class="ba-16__text">Type error in <code>src/checkout/total.ts:44</code> — <code>Money</code> is not assignable to <code>number</code>. The previous deployment is still serving traffic.</p>
        <p class="ba-16__acts"><a href="#ba-16-a">Open log</a><a href="#ba-16-a">Retry build</a></p>
      </div>
      <label class="ba-16__x" for="ba-16-x4" tabindex="0" role="button" aria-label="Dismiss failure">
        <svg viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><path d="m5 5 6 6m0-6-6 6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
      </label>
    </div>

    <div class="ba-16__a ba-16__a--rtl" data-v="info" dir="rtl" lang="ar">
      <p class="ba-16__label">ملاحظة</p>
      <div class="ba-16__body">
        <p class="ba-16__title">نفس الشريط، على الجهة الصحيحة</p>
        <p class="ba-16__text">لأن الحدّ مُعرَّف باستخدام <code>border-inline-start</code>، ينعكس تلقائيًا مع اتجاه الكتابة دون أي قواعد إضافية.</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

.ba-16 {
  --tint: 6%;
  --bg: #fafafa;
  --surface: #ffffff;
  --ink: #111214;
  --muted: #63676e;
  --line: #e6e7ea;
  --blue: #2563eb;
  --green: #0e9f6e;
  --amber: #c2740a;
  --red: #d3312a;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
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

.ba-16 *,
.ba-16 *::before,
.ba-16 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-16 {
    --bg: oklch(98% .002 265);
    --surface: oklch(100% 0 0);
    --ink: oklch(17% .008 265);
    --muted: oklch(53% .012 265);
    --line: oklch(92% .006 265);
    --blue: oklch(55% .2 262);
    --green: oklch(62% .15 160);
    --amber: oklch(60% .14 62);
    --red: oklch(56% .2 27);
  }
}

@media (prefers-color-scheme: dark) {
  .ba-16:not([data-theme="light"]) {
    --bg: #0a0b0d;
    --surface: #121317;
    --ink: #eeeff2;
    --muted: #969aa3;
    --line: #212328;
    --tint: 10%;
  }
}

.ba-16[data-theme="dark"] {
  --bg: #0a0b0d;
  --surface: #121317;
  --ink: #eeeff2;
  --muted: #969aa3;
  --line: #212328;
  --tint: 10%;
}

.ba-16__stack {
  width: min(42rem,100%);
  display: grid;
  gap: .7rem;
}

.ba-16__a {
  --v: var(--blue);
  position: relative;
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto;
  gap: .25rem .9rem;
  align-items: start;
  padding-block: .95rem;
  padding-inline: 1.05rem 1rem;
  border: 1px solid var(--line);
  border-inline-start: 3px solid var(--v);
  background: color-mix(in oklab,var(--v) var(--tint),var(--surface));
  transition: opacity .3s ease, translate .3s cubic-bezier(.16,1,.3,1), display .3s allow-discrete;
}

@starting-style {
  .ba-16__a {
    opacity: 0;
    translate: 0 .4rem;
  }
}

.ba-16__a[data-v="success"] {
  --v: var(--green);
}

.ba-16__a[data-v="warning"] {
  --v: var(--amber);
}

.ba-16__a[data-v="danger"] {
  --v: var(--red);
}

.ba-16__a:has(input:checked) {
  display: none;
  opacity: 0;
  translate: 0 -.4rem;
}

.ba-16__label {
  margin: 0;
  grid-row: 1 / span 2;
  align-self: start;
  font-family: var(--mono);
  font-size: .625rem;
  font-weight: 500;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--v);
  padding-block-start: .15rem;
  white-space: nowrap;
}

.ba-16__body {
  grid-column: 2;
  min-width: 0;
  display: grid;
  gap: .25rem;
}

.ba-16__title {
  margin: 0;
  font-size: .9375rem;
  font-weight: 600;
  line-height: 1.45;
  letter-spacing: -.02em;
  text-wrap: pretty;
}

.ba-16__text {
  margin: 0;
  font-size: .875rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 68ch;
  text-wrap: pretty;
  overflow-wrap: anywhere;
}

.ba-16__text code {
  font-family: var(--mono);
  font-size: .85em;
  padding: .08em .3em;
  border-radius: .25rem;
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 8%,transparent);
}

.ba-16__acts {
  margin: .35rem 0 0;
  display: flex;
  flex-wrap: wrap;
  gap: .85rem;
}

.ba-16__acts a {
  font-size: .8125rem;
  font-weight: 600;
  color: var(--v);
  text-decoration: underline;
  text-underline-offset: 3px;
  text-decoration-thickness: 1.5px;
}

.ba-16__acts a:hover {
  text-decoration-thickness: 2.5px;
}

.ba-16__x {
  grid-column: 3;
  display: grid;
  place-items: center;
  width: 2.25rem;
  height: 2.25rem;
  margin: -.4rem -.35rem 0 0;
  border-radius: .5rem;
  cursor: pointer;
  color: var(--muted);
  transition: color .2s ease, background .2s ease;
}

.ba-16__x:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 7%,transparent);
}

.ba-16__x svg {
  width: .95rem;
  height: .95rem;
}

.ba-16__x:focus-visible {
  outline: 2px solid var(--v);
  outline-offset: 2px;
}

.ba-16__a--rtl {
  margin-block-start: .5rem;
}

.ba-16__a--rtl .ba-16__text {
  line-height: 1.85;
}

.ba-16__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.ba-16 a {
  color: var(--blue);
}

.ba-16 :focus-visible {
  outline: 2px solid var(--blue);
  outline-offset: 2px;
}

@media (max-width: 30rem) {
  .ba-16__a {
    grid-template-columns: minmax(0,1fr) auto;
  }

  .ba-16__label {
    grid-row: auto;
    grid-column: 1;
  }

  .ba-16__body {
    grid-column: 1 / -1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ba-16 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .ba-16__a {
    border: 1px solid CanvasText;
    border-inline-start: 3px solid Highlight;
  }
}
```
