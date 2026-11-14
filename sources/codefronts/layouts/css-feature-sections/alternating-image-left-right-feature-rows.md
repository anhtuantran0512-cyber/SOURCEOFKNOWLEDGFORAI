---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/alternating-image-left-right-feature-rows/"
title: "Alternating Image Left Right Feature Rows"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "The zig-zag row layout every product marketing page eventually needs: four feature rows, media on one side and copy on the other, flipping direction every row."
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Alternating Image Left Right Feature Rows
Source: https://codefronts.com/layouts/css-feature-sections/alternating-image-left-right-feature-rows/

The zig-zag row layout every product marketing page eventually needs: four feature rows, media on one side and copy on the other, flipping direction every row. One :nth-child(even) rule owns the whole alternation, and a container query — not a viewport breakpoint — decides when a row folds to a single column, so the same rows drop into a narrow sidebar without new CSS.
## HTML
```html
<section class="fs-02" aria-labelledby="fs-02-heading">
  <div class="fs-02__hero" aria-hidden="true">
    <span class="fs-02__wordmark">Quill</span>
    <span class="fs-02__heronav">Product · Docs · Changelog</span>
  </div>

  <div class="fs-02__stage">
    <div class="fs-02__head">
      <h2 class="fs-02__heading" id="fs-02-heading">Everything a writing team argues about, settled</h2>
      <p class="fs-02__sub">Four rows, four opinions we have already had for you.</p>
    </div>

    <div class="fs-02__rows">
      <article class="fs-02__row">
        <div class="fs-02__media">
          <div class="fs-02__mock">
            <div class="fs-02__mockrow"><span class="fs-02__dot"></span><b>Draft: Q3 launch brief</b></div>
            <div class="fs-02__line" style="inline-size:92%"></div>
            <div class="fs-02__line" style="inline-size:78%"></div>
            <div class="fs-02__line fs-02__line--mark" style="inline-size:56%"></div>
            <div class="fs-02__line" style="inline-size:84%"></div>
          </div>
        </div>
        <div class="fs-02__copy">
          <p class="fs-02__chip">Editing</p>
          <h3 class="fs-02__rtitle">Suggestions that keep the author in charge</h3>
          <p class="fs-02__prose">Every edit lands as a suggestion with an owner and a reason. Accept the batch, or take the three that matter and leave the rest. Nothing rewrites your paragraph while you are still in it.</p>
          <ul class="fs-02__chips">
            <li>Inline threads</li><li>Batch accept</li><li>Reason required</li>
          </ul>
        </div>
      </article>

      <article class="fs-02__row">
        <div class="fs-02__media">
          <div class="fs-02__mock">
            <div class="fs-02__mockrow"><span class="fs-02__dot"></span><b>Version history</b></div>
            <div class="fs-02__stack">
              <div class="fs-02__ver"><b>v14</b><span>Priya Sharma · 2h ago</span></div>
              <div class="fs-02__ver fs-02__ver--on"><b>v13</b><span>Alex Chen · yesterday</span></div>
              <div class="fs-02__ver"><b>v12</b><span>Jordan Lee · Tuesday</span></div>
            </div>
          </div>
        </div>
        <div class="fs-02__copy">
          <p class="fs-02__chip">History</p>
          <h3 class="fs-02__rtitle">Restore a paragraph, not the whole document</h3>
          <p class="fs-02__prose">Versions are stored per block, so rolling back a mangled intro leaves the last four hours of work on the rest of the page untouched. Diffs read as prose, not as a wall of markup.</p>
          <ul class="fs-02__chips">
            <li>Block-level diff</li><li>Named checkpoints</li><li>90-day retention</li>
          </ul>
        </div>
      </article>

      <article class="fs-02__row">
        <div class="fs-02__media">
          <div class="fs-02__mock">
            <div class="fs-02__mockrow"><span class="fs-02__dot"></span><b>Publish targets</b></div>
            <div class="fs-02__grid">
              <div class="fs-02__cell">Web</div><div class="fs-02__cell">Newsletter</div>
              <div class="fs-02__cell">Docs site</div><div class="fs-02__cell">RSS</div>
            </div>
            <div class="fs-02__line" style="inline-size:64%"></div>
          </div>
        </div>
        <div class="fs-02__copy">
          <p class="fs-02__chip">Publishing</p>
          <h3 class="fs-02__rtitle">One source, four destinations, no copy-paste</h3>
          <p class="fs-02__prose">Write once and push to the site, the newsletter and the docs build in the same action. Each target keeps its own front matter, so the newsletter never inherits the docs sidebar.</p>
          <ul class="fs-02__chips">
            <li>Per-target front matter</li><li>Scheduled release</li><li>Draft previews</li>
          </ul>
        </div>
      </article>

      <article class="fs-02__row">
        <div class="fs-02__media">
          <div class="fs-02__mock">
            <div class="fs-02__mockrow"><span class="fs-02__dot"></span><b>Style report</b></div>
            <div class="fs-02__bars">
              <div><i style="inline-size:88%"></i><span>Voice</span></div>
              <div><i style="inline-size:71%"></i><span>Reading level</span></div>
              <div><i style="inline-size:94%"></i><span>Terminology</span></div>
            </div>
          </div>
        </div>
        <div class="fs-02__copy">
          <p class="fs-02__chip">Consistency</p>
          <h3 class="fs-02__rtitle">A house style the whole team can actually follow</h3>
          <p class="fs-02__prose">Load your terminology list once and every draft gets checked against it before review. Writers see the rule that fired and the sentence that broke it, side by side.</p>
          <ul class="fs-02__chips">
            <li>Custom term list</li><li>Per-space rules</li><li>Review gate</li>
          </ul>
        </div>
      </article>
    </div>
  </div>

  <div class="fs-02__below" aria-hidden="true">Read the changelog · Compare plans</div>
</section>
```
## CSS
```css
.fs-02 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --paper: #faf7f1;
  --paper: oklch(0.977 0.011 85);
  --card: #ffffff;
  --ink: #211f1b;
  --ink: oklch(0.24 0.011 70);
  --muted: #6c665c;
  --muted: oklch(0.53 0.017 75);
  --rule: #e3dcce;
  --rule: oklch(0.9 0.018 85);
  --accent: #2f6b46;
  --accent: oklch(0.46 0.089 155);
  --wash: #eef3ec;
  --wash: oklch(0.955 0.017 150);
  --rowgap: clamp(48px, 8vw, 96px);
  --font-display: "Rockwell", "Roboto Slab", "Bookman Old Style", Georgia, serif;
  background: var(--paper);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-02 *,
.fs-02 *::before,
.fs-02 *::after {
  box-sizing: border-box;
}

.fs-02__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
  justify-content: space-between;
  align-items: baseline;
  padding: 18px 22px;
  border-block-end: 1px solid var(--rule);
}

.fs-02__wordmark {
  font: 700 16px/1 var(--font-display);
  letter-spacing: -0.01em;
}

.fs-02__heronav {
  font-size: 12px;
  color: var(--muted);
}

.fs-02__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(36px, 7vw, 80px) 18px;
}

.fs-02__head {
  inline-size: 100%;
  max-inline-size: 66rem;
  min-inline-size: 0;
  margin: 0 0 clamp(36px, 6vw, 64px);
}

.fs-02__heading {
  margin: 0 0 12px;
  max-inline-size: 30ch;
  font: 400 clamp(28px, 5.4vw, 46px)/1.08 var(--font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.fs-02__sub {
  margin: 0;
  font-size: 15px;
  color: var(--muted);
}

.fs-02__rows {
  inline-size: 100%;
  max-inline-size: 66rem;
  min-inline-size: 0;
  display: grid;
  gap: var(--rowgap);
}

.fs-02__row {
  container-type: inline-size;
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  gap: clamp(22px, 4vw, 52px);
  align-items: center;
}

.fs-02__row:nth-child(even) .fs-02__media {
  grid-column: 2;
  grid-row: 1;
}

.fs-02__row:nth-child(even) .fs-02__copy {
  grid-column: 1;
  grid-row: 1;
}

.fs-02__media {
  min-inline-size: 0;
  background: var(--wash);
  border-radius: 4px;
  padding: clamp(16px, 3vw, 30px);
}

.fs-02__mock {
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 3px;
  padding: 16px;
}

.fs-02__mockrow {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 14px;
  font-size: 12px;
}

.fs-02__mockrow b {
  font-weight: 600;
  min-inline-size: 0;
}

.fs-02__dot {
  inline-size: 8px;
  block-size: 8px;
  border-radius: 50%;
  background: var(--accent);
  flex: none;
}

.fs-02__line {
  block-size: 8px;
  margin-block-end: 9px;
  border-radius: 2px;
  background: var(--rule);
}

.fs-02__line--mark {
  background: color-mix(in oklab, var(--accent) 40%, var(--rule));
}

.fs-02__stack {
  display: grid;
  gap: 8px;
}

.fs-02__ver {
  display: flex;
  flex-wrap: wrap;
  gap: 4px 10px;
  justify-content: space-between;
  padding: 10px 12px;
  border: 1px solid var(--rule);
  border-radius: 3px;
  font-size: 12px;
}

.fs-02__ver b {
  font-weight: 700;
}

.fs-02__ver span {
  color: var(--muted);
}

.fs-02__ver--on {
  border-color: var(--accent);
  background: color-mix(in oklab, var(--accent) 8%, transparent);
}

.fs-02__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 110px), 1fr));
  gap: 8px;
  margin-block-end: 14px;
}

.fs-02__cell {
  padding: 12px 10px;
  text-align: center;
  font-size: 12px;
  font-weight: 600;
  border: 1px dashed var(--rule);
  border-radius: 3px;
  min-inline-size: 0;
}

.fs-02__bars {
  display: grid;
  gap: 12px;
}

.fs-02__bars div {
  display: grid;
  gap: 5px;
}

.fs-02__bars i {
  display: block;
  block-size: 7px;
  border-radius: 2px;
  background: var(--accent);
}

.fs-02__bars span {
  font-size: 11px;
  color: var(--muted);
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.fs-02__copy {
  min-inline-size: 0;
}

.fs-02__chip {
  display: inline-block;
  margin: 0 0 14px;
  padding: 4px 10px;
  font: 700 10px/1.4 system-ui, sans-serif;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--accent);
  border: 1px solid color-mix(in oklab, var(--accent) 40%, transparent);
  border-radius: 2px;
}

.fs-02__rtitle {
  margin: 0 0 14px;
  font: 400 clamp(21px, 3vw, 30px)/1.15 var(--font-display);
  letter-spacing: -0.015em;
  text-wrap: balance;
}

.fs-02__prose {
  margin: 0 0 18px;
  max-inline-size: 46ch;
  font-size: 15px;
  line-height: 1.7;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-02__chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.fs-02__chips li {
  padding: 6px 11px;
  font-size: 11.5px;
  font-weight: 600;
  color: var(--ink);
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 999px;
}

.fs-02__below {
  padding: 18px 22px;
  border-block-start: 1px solid var(--rule);
  font-size: 12px;
  color: var(--muted);
}

@supports (container-type: inline-size) {
  @container (max-width: 46rem) {
    .fs-02__media,
        .fs-02__copy {
      grid-column: 1 !important;
    }

    .fs-02__media {
      grid-row: 1 !important;
    }

    .fs-02__copy {
      grid-row: 2 !important;
    }
  }
}

@supports not (container-type: inline-size) {
  @media (max-width: 780px) {
    .fs-02__row {
      grid-template-columns: minmax(0, 1fr);
    }

    .fs-02__row:nth-child(even) .fs-02__media {
      grid-column: 1;
      grid-row: 1;
    }

    .fs-02__row:nth-child(even) .fs-02__copy {
      grid-column: 1;
      grid-row: 2;
    }
  }
}

@container (max-width: 46rem) {
  .fs-02__row {
    grid-template-columns: minmax(0, 1fr);
  }
}

@media (prefers-color-scheme: dark) {
  .fs-02 {
    --paper: #17150f;
    --card: #1f1c15;
    --ink: #f4efe3;
    --muted: #a9a191;
    --rule: #322d22;
    --accent: #7fc79a;
    --wash: #201d16;
  }
}

[data-theme="dark"] .fs-02 {
  --paper: #17150f;
  --card: #1f1c15;
  --ink: #f4efe3;
  --muted: #a9a191;
  --rule: #322d22;
  --accent: #7fc79a;
  --wash: #201d16;
}
```
