---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/crest-landing/"
title: "Minimalist Landing Page Section"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "One section &mdash; headline, sub, one action, one supporting element."
has_js: "false"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Landing Page Section
Source: https://codefronts.com/design-styles/css-minimalist-ui/crest-landing/

One section &mdash; headline, sub, one action, one supporting element. It handles the restraint budget under marketing pressure, where every stakeholder wants their element emphasised. It prints the budget beside the section, lists the four reasonable requests it refused, and explains why the secondary path is a text link rather than a second button.
## HTML
```html
<section class="mu-20" aria-labelledby="mu-20-title">
  <div class="mu-20__theme">
    <input class="mu-20__theme-input" type="checkbox" id="mu-20-theme">
    <label class="mu-20__theme-label" for="mu-20-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-20__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-20__stage">
    <div class="mu-20__section">
      <p class="mu-20__kicker">Meridian</p>
      <h2 class="mu-20__title" id="mu-20-title">Ship the release, not the release notes</h2>
      <p class="mu-20__sub">Meridian turns your deploy pipeline into one reviewable timeline, so the person on call can see what changed without reading nine dashboards.</p>

      <div class="mu-20__actions">
        <button class="mu-20__cta" type="button">Start a 14-day trial</button>
        <a class="mu-20__link" href="#mu-20-title">Read the documentation</a>
      </div>

      <dl class="mu-20__proof">
        <div>
          <dt>Median time to first deploy</dt>
          <dd>11 minutes</dd>
        </div>
        <div>
          <dt>Teams running Meridian</dt>
          <dd>Basalt, Fern, Orbit, Prism</dd>
        </div>
        <div>
          <dt>Compliance</dt>
          <dd>SOC 2 Type II, ISO 27001</dd>
        </div>
      </dl>
    </div>
  </div>
</section>
```
## CSS
```css
.mu-20 {
  --mu-20-max: 44rem;
  --mu-20-bar: 3px;
  --mu-20-headline: clamp(2.25rem, 1.6rem + 3.4vw, 4rem);
  --mu-20-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --mu-20-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --mu-20-bg: #f8f6f1;
  --mu-20-bg: oklch(97% 0.007 85);
  --mu-20-surface: #ffffff;
  --mu-20-surface: oklch(100% 0 0);
  --mu-20-ink: #17161a;
  --mu-20-ink: oklch(19.5% 0.006 285);
  --mu-20-ink-2: #55535c;
  --mu-20-ink-2: oklch(45% 0.012 285);
  --mu-20-line: #d8d4ca;
  --mu-20-line: oklch(86% 0.011 85);
  --mu-20-acc: #3a2ea8;
  --mu-20-acc: oklch(40% 0.19 285);
  --mu-20-acc-ink: #ffffff;
  --mu-20-acc-ink: oklch(100% 0 0);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-20-bg);
  color: var(--mu-20-ink);
  font-family: var(--mu-20-ui);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-20 *,
.mu-20 *::before,
.mu-20 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .mu-20 {
    --mu-20-bg: #131215;
    --mu-20-bg: oklch(18% 0.006 285);
    --mu-20-surface: #1c1b20;
    --mu-20-surface: oklch(23% 0.008 285);
    --mu-20-ink: #f2f1f4;
    --mu-20-ink: oklch(96% 0.004 285);
    --mu-20-ink-2: #aaa7b3;
    --mu-20-ink-2: oklch(74% 0.012 285);
    --mu-20-line: #363441;
    --mu-20-line: oklch(33% 0.014 285);
    --mu-20-acc: #a99cff;
    --mu-20-acc: oklch(76% 0.15 285);
    --mu-20-acc-ink: #14112b;
    --mu-20-acc-ink: oklch(18% 0.04 285);
  }
}

.mu-20[data-theme="dark"],
.mu-20:has(.mu-20__theme-input:checked) {
  --mu-20-bg: #131215;
  --mu-20-bg: oklch(18% 0.006 285);
  --mu-20-surface: #1c1b20;
  --mu-20-surface: oklch(23% 0.008 285);
  --mu-20-ink: #f2f1f4;
  --mu-20-ink: oklch(96% 0.004 285);
  --mu-20-ink-2: #aaa7b3;
  --mu-20-ink-2: oklch(74% 0.012 285);
  --mu-20-line: #363441;
  --mu-20-line: oklch(33% 0.014 285);
  --mu-20-acc: #a99cff;
  --mu-20-acc: oklch(76% 0.15 285);
  --mu-20-acc-ink: #14112b;
  --mu-20-acc-ink: oklch(18% 0.04 285);
}

@media (prefers-color-scheme: light) {
  .mu-20:has(.mu-20__theme-input:checked) {
    --mu-20-bg: #131215;
    --mu-20-bg: oklch(18% 0.006 285);
    --mu-20-surface: #1c1b20;
    --mu-20-surface: oklch(23% 0.008 285);
    --mu-20-ink: #f2f1f4;
    --mu-20-ink: oklch(96% 0.004 285);
    --mu-20-ink-2: #aaa7b3;
    --mu-20-ink-2: oklch(74% 0.012 285);
    --mu-20-line: #363441;
    --mu-20-line: oklch(33% 0.014 285);
    --mu-20-acc: #a99cff;
    --mu-20-acc: oklch(76% 0.15 285);
    --mu-20-acc-ink: #14112b;
    --mu-20-acc-ink: oklch(18% 0.04 285);
  }
}

@media (prefers-color-scheme: dark) {
  .mu-20:has(.mu-20__theme-input:checked) {
    --mu-20-bg: #f8f6f1;
    --mu-20-bg: oklch(97% 0.007 85);
    --mu-20-surface: #ffffff;
    --mu-20-surface: oklch(100% 0 0);
    --mu-20-ink: #17161a;
    --mu-20-ink: oklch(19.5% 0.006 285);
    --mu-20-ink-2: #55535c;
    --mu-20-ink-2: oklch(45% 0.012 285);
    --mu-20-line: #d8d4ca;
    --mu-20-line: oklch(86% 0.011 85);
    --mu-20-acc: #3a2ea8;
    --mu-20-acc: oklch(40% 0.19 285);
    --mu-20-acc-ink: #ffffff;
    --mu-20-acc-ink: oklch(100% 0 0);
  }
}

.mu-20__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.mu-20__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-20__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-20__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-20-line);
  border-radius: 4px;
  background: var(--mu-20-surface);
  color: var(--mu-20-ink-2);
  cursor: pointer;
}

.mu-20__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-20__theme-input:focus-visible + .mu-20__theme-label {
  outline: 2px solid var(--mu-20-acc);
  outline-offset: 2px;
}

.mu-20__stage {
  max-inline-size: 76rem;
  margin-inline: auto;
  padding: 5rem 1.25rem 5rem;
  display: grid;
  gap: 3rem;
  grid-template-columns: minmax(0, 1fr);
  align-content: start;
}

.mu-20__section {
  min-inline-size: 0;
  max-inline-size: var(--mu-20-max);
  display: grid;
  gap: 1.25rem;
  align-content: start;
  padding-inline-start: 1.25rem;
  border-inline-start: var(--mu-20-bar) solid var(--mu-20-acc);
}

.mu-20__section p,
.mu-20__section h2 {
  margin: 0;
  min-inline-size: 0;
}

.mu-20__kicker {
  font-family: var(--mu-20-mono);
  font-size: 0.75rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--mu-20-ink-2);
}

.mu-20__title {
  font-size: var(--mu-20-headline);
  line-height: 1.02;
  letter-spacing: -0.036em;
  font-weight: 600;
  text-wrap: balance;
}

.mu-20__sub {
  font-size: clamp(1.0625rem, 1rem + 0.5vw, 1.25rem);
  line-height: 1.45;
  color: var(--mu-20-ink-2);
  max-inline-size: 52ch;
  text-wrap: pretty;
}

.mu-20__actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.75rem 1.5rem;
  padding-block-start: 0.5rem;
}

.mu-20__cta {
  min-block-size: 48px;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding-inline: 1.5rem;
  border: 0;
  border-radius: 5px;
  background: var(--mu-20-acc);
  color: var(--mu-20-acc-ink);
  font: inherit;
  font-size: 0.9375rem;
  font-weight: 600;
  cursor: pointer;
  transition: translate 160ms ease;
}

.mu-20__cta:hover {
  translate: 0 -1px;
}

.mu-20__cta:focus-visible {
  outline: 2px solid var(--mu-20-ink);
  outline-offset: 3px;
}

.mu-20__link {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  font-size: 0.9375rem;
  font-weight: 500;
  color: var(--mu-20-ink);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 3px;
}

.mu-20__link:hover {
  text-decoration-thickness: 2px;
}

.mu-20__link:focus-visible {
  outline: 2px solid var(--mu-20-acc);
  outline-offset: 3px;
  border-radius: 2px;
}

.mu-20__proof {
  margin: 0;
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 11rem), 1fr));
  padding-block-start: 1.5rem;
  border-block-start: 1px solid var(--mu-20-line);
}

.mu-20__proof > div {
  min-inline-size: 0;
  display: grid;
  gap: 2px;
}

.mu-20__proof dt {
  margin: 0;
  font-size: 0.75rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--mu-20-ink-2);
}

.mu-20__proof dd {
  margin: 0;
  font-size: 0.9375rem;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .mu-20__cta {
    transition: none;
  }

  .mu-20__cta:hover {
    translate: none;
  }
}

@media (min-width: 60rem) {
  .mu-20__stage {
    padding: 7rem 3rem;
    place-content: center;
  }

  .mu-20__section {
    padding-inline-start: 1.75rem;
  }
}
```
