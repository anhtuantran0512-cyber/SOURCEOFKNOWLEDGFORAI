---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/ledger-news/"
title: "Minimalist Article Layout and Typography"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "One article column: measure, rhythm, a lead paragraph, one pull quote."
has_js: "false"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Article Layout and Typography
Source: https://codefronts.com/design-styles/css-minimalist-ui/ledger-news/

One article column: measure, rhythm, a lead paragraph, one pull quote. It applies the ratio from demo 01 and the block-level rhythm from demo 07 to real prose, at the size a reader actually meets them &mdash; a column, not a homepage. Measure in ch, one step for the lead, one pull quote, and a caption in the interface face so it reads as apparatus rather than prose.
## HTML
```html
<section class="mu-18" aria-labelledby="mu-18-title">
  <div class="mu-18__theme">
    <input class="mu-18__theme-input" type="checkbox" id="mu-18-theme">
    <label class="mu-18__theme-label" for="mu-18-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-18__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-18__stage">
    <article class="mu-18__article">
      <header class="mu-18__header">
        <p class="mu-18__kicker">Craft</p>
        <h2 class="mu-18__title" id="mu-18-title">The column is the whole design</h2>
        <p class="mu-18__byline">
          <span>Alex Chen</span>
          <span class="mu-18__dot" aria-hidden="true">&middot;</span>
          <span>8 min read</span>
          <span class="mu-18__dot" aria-hidden="true">&middot;</span>
          <time datetime="2026-08-30">30 August 2026</time>
        </p>
      </header>

      <p class="mu-18__lead">Measure, rhythm and one moment of emphasis. Everything else an article layout appears to need &mdash; rules, cards, sidebars, badges &mdash; is scaffolding around a column that was already working.</p>

      <p class="mu-18__body">Set the measure first. Between 60 and 75 characters is the band where continuous reading stays comfortable, and expressing it in character units rather than pixels means it follows the type size instead of fighting it. A reader who zooms to 140% keeps the same measure, because the measure was never a pixel value.</p>

      <p class="mu-18__body">Then set the rhythm. One unit, every margin a multiple of it, headings taking two units of leading where the body takes one. The effect is not decorative: it removes the small inconsistencies that make a page feel unfinished without ever giving the reader something specific to point at.</p>

      <h3 class="mu-18__h3">One moment of emphasis</h3>

      <p class="mu-18__body">The lead paragraph above is one step up the scale. Not three &mdash; one. A lead set at heading size becomes a second headline and the reader has to work out which of the two is the title, which is the exact cognitive cost the hierarchy was supposed to remove.</p>

      <blockquote class="mu-18__quote">
        <p>A pull quote is a navigation device. If it does not reward stopping, it is a gap in the column with type in it.</p>
      </blockquote>

      <p class="mu-18__body">The same restraint applies to the quote. Set it in the body family, one or two steps up, and never repeat the sentence directly above it &mdash; a quote that echoes the previous line tells a scanning reader they have already read this part and can safely leave.</p>

      <figure class="mu-18__figure">
        <div class="mu-18__frame" role="img" aria-label="Tonal placeholder standing in for an article image, 16 by 9">
          <span class="mu-18__frame-note">16:9 image area</span>
        </div>
        <figcaption class="mu-18__caption">Captions sit in the interface face, one size below the body, so they read as apparatus rather than prose.</figcaption>
      </figure>

      <p class="mu-18__body">What is deliberately absent: a reading-progress bar, related-article cards, a share rail, and an author box with a photograph. Each is defensible on some sites and none of them make this column easier to read, which is the only question this component has to answer.</p>
    </article>
  </div>
</section>
```
## CSS
```css
.mu-18 {
  --mu-18-measure: 66ch;
  --mu-18-rhythm: 1.6rem;
  --mu-18-ratio: 1.25;
  --mu-18-body: 1.125rem;
  --mu-18-serif: ui-serif, Georgia, "Iowan Old Style", "Palatino Linotype", Palatino, serif;
  --mu-18-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --mu-18-bg: #fbf8f2;
  --mu-18-bg: oklch(97.8% 0.01 92);
  --mu-18-surface: #f2ece0;
  --mu-18-surface: oklch(93.5% 0.016 90);
  --mu-18-ink: #1a1813;
  --mu-18-ink: oklch(20% 0.008 80);
  --mu-18-ink-2: #56503f;
  --mu-18-ink-2: oklch(45% 0.016 82);
  --mu-18-line: #ddd5c2;
  --mu-18-line: oklch(87% 0.018 88);
  --mu-18-acc: #7a3b12;
  --mu-18-acc: oklch(42% 0.11 50);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-18-bg);
  color: var(--mu-18-ink);
  font-family: var(--mu-18-serif);
  line-height: 1.6;
  -webkit-text-size-adjust: 100%;
}

.mu-18 *,
.mu-18 *::before,
.mu-18 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .mu-18 {
    --mu-18-bg: #16130e;
    --mu-18-bg: oklch(18.5% 0.008 80);
    --mu-18-surface: #211d15;
    --mu-18-surface: oklch(24% 0.012 85);
    --mu-18-ink: #f4f0e6;
    --mu-18-ink: oklch(96% 0.01 90);
    --mu-18-ink-2: #b2a992;
    --mu-18-ink-2: oklch(75% 0.018 88);
    --mu-18-line: #3c352a;
    --mu-18-line: oklch(33% 0.014 85);
    --mu-18-acc: #e79a63;
    --mu-18-acc: oklch(76% 0.12 55);
  }
}

.mu-18[data-theme="dark"],
.mu-18:has(.mu-18__theme-input:checked) {
  --mu-18-bg: #16130e;
  --mu-18-bg: oklch(18.5% 0.008 80);
  --mu-18-surface: #211d15;
  --mu-18-surface: oklch(24% 0.012 85);
  --mu-18-ink: #f4f0e6;
  --mu-18-ink: oklch(96% 0.01 90);
  --mu-18-ink-2: #b2a992;
  --mu-18-ink-2: oklch(75% 0.018 88);
  --mu-18-line: #3c352a;
  --mu-18-line: oklch(33% 0.014 85);
  --mu-18-acc: #e79a63;
  --mu-18-acc: oklch(76% 0.12 55);
}

@media (prefers-color-scheme: light) {
  .mu-18:has(.mu-18__theme-input:checked) {
    --mu-18-bg: #16130e;
    --mu-18-bg: oklch(18.5% 0.008 80);
    --mu-18-surface: #211d15;
    --mu-18-surface: oklch(24% 0.012 85);
    --mu-18-ink: #f4f0e6;
    --mu-18-ink: oklch(96% 0.01 90);
    --mu-18-ink-2: #b2a992;
    --mu-18-ink-2: oklch(75% 0.018 88);
    --mu-18-line: #3c352a;
    --mu-18-line: oklch(33% 0.014 85);
    --mu-18-acc: #e79a63;
    --mu-18-acc: oklch(76% 0.12 55);
  }
}

@media (prefers-color-scheme: dark) {
  .mu-18:has(.mu-18__theme-input:checked) {
    --mu-18-bg: #fbf8f2;
    --mu-18-bg: oklch(97.8% 0.01 92);
    --mu-18-surface: #f2ece0;
    --mu-18-surface: oklch(93.5% 0.016 90);
    --mu-18-ink: #1a1813;
    --mu-18-ink: oklch(20% 0.008 80);
    --mu-18-ink-2: #56503f;
    --mu-18-ink-2: oklch(45% 0.016 82);
    --mu-18-line: #ddd5c2;
    --mu-18-line: oklch(87% 0.018 88);
    --mu-18-acc: #7a3b12;
    --mu-18-acc: oklch(42% 0.11 50);
  }
}

.mu-18__sr {
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

.mu-18__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-18__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-18__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-18-line);
  border-radius: 50%;
  background: var(--mu-18-bg);
  color: var(--mu-18-ink-2);
  cursor: pointer;
}

.mu-18__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-18__theme-input:focus-visible + .mu-18__theme-label {
  outline: 2px solid var(--mu-18-acc);
  outline-offset: 2px;
}

.mu-18__stage {
  inline-size: 100%;
  padding: 4.5rem 1.25rem 5rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  justify-items: center;
}

.mu-18__article {
  min-inline-size: 0;
  inline-size: 100%;
  max-inline-size: var(--mu-18-measure);
  font-size: var(--mu-18-body);
}

.mu-18__article > * {
  margin-block: 0 var(--mu-18-rhythm);
  min-inline-size: 0;
}

.mu-18__article > :last-child {
  margin-block-end: 0;
}

.mu-18__header {
  display: grid;
  gap: 0.5rem;
  padding-block-end: var(--mu-18-rhythm);
  border-block-end: 1px solid var(--mu-18-line);
}

.mu-18__header p {
  margin: 0;
}

.mu-18__kicker {
  font-family: var(--mu-18-ui);
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--mu-18-acc);
}

.mu-18__title {
  margin: 0;
  font-size: clamp(2rem, 1.5rem + 2.6vw, 3.25rem);
  line-height: 1.06;
  letter-spacing: -0.028em;
  font-weight: 600;
  text-wrap: balance;
}

.mu-18__byline {
  display: flex;
  flex-wrap: wrap;
  gap: 0.375rem;
  font-family: var(--mu-18-ui);
  font-size: 0.8125rem;
  color: var(--mu-18-ink-2);
}

.mu-18__dot {
  color: var(--mu-18-line);
}

.mu-18__lead {
  font-size: calc(var(--mu-18-body) * var(--mu-18-ratio));
  line-height: 1.45;
  letter-spacing: -0.012em;
  text-wrap: pretty;
}

.mu-18__lead::first-letter {
  float: inline-start;
  font-size: 3.1em;
  line-height: 0.84;
  padding-inline-end: 0.08em;
  padding-block-start: 0.04em;
  font-weight: 600;
  color: var(--mu-18-acc);
}

@supports (initial-letter: 3) or (-webkit-initial-letter: 3) {
  .mu-18__lead::first-letter {
    float: none;
    -webkit-initial-letter: 3;
    initial-letter: 3;
    font-size: inherit;
    line-height: inherit;
    padding: 0;
    margin-inline-end: 0.1em;
  }
}

.mu-18__body {
  text-wrap: pretty;
}

.mu-18__h3 {
  font-family: var(--mu-18-ui);
  font-size: 0.8125rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--mu-18-ink-2);
  margin-block: calc(var(--mu-18-rhythm) * 1.5) var(--mu-18-rhythm);
}

.mu-18__quote {
  margin-block: calc(var(--mu-18-rhythm) * 1.5);
  margin-inline: 0;
  padding-inline-start: 1.25rem;
  border-inline-start: 2px solid var(--mu-18-acc);
}

.mu-18__quote p {
  margin: 0;
  font-size: calc(var(--mu-18-body) * var(--mu-18-ratio));
  line-height: 1.4;
  letter-spacing: -0.014em;
  text-wrap: pretty;
  hanging-punctuation: first;
}

.mu-18__figure {
  margin-block: calc(var(--mu-18-rhythm) * 1.5);
  margin-inline: 0;
}

.mu-18__frame {
  aspect-ratio: 16 / 9;
  inline-size: 100%;
  display: grid;
  place-items: center;
  border-radius: 3px;
  background: var(--mu-18-surface);
  border: 1px solid var(--mu-18-line);
  margin-block-end: 0.75rem;
}

.mu-18__frame-note {
  font-family: var(--mu-18-ui);
  font-size: 0.75rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--mu-18-ink-2);
}

.mu-18__caption {
  font-family: var(--mu-18-ui);
  font-size: 0.8125rem;
  line-height: 1.5;
  color: var(--mu-18-ink-2);
  text-wrap: pretty;
}

@media (min-width: 56rem) {
  .mu-18__stage {
    padding-block-start: 6rem;
    padding-inline: 3rem;
  }
}
```
