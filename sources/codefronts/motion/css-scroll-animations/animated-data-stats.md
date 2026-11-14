---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/animated-data-stats/"
title: "Timeline Scope Across DOM Branches"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "A named timeline is visible only to descendants of the element that declares it, which fails the moment your sticky header is a sibling of the content column…"
has_js: "false"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Timeline Scope Across DOM Branches
Source: https://codefronts.com/motion/css-scroll-animations/animated-data-stats/

A named timeline is visible only to descendants of the element that declares it, which fails the moment your sticky header is a sibling of the content column rather than inside it. timeline-scope on a common ancestor lifts that visibility so a sibling branch can subscribe — and it is the least-supported property in this collection, so it ships behind a gate.
## HTML
```html
<section class="sa-15" aria-labelledby="sa-15-h">
  <fieldset class="sa-15__theme">
    <legend class="sa-15__themelegend">Theme</legend>
    <input class="sa-15__themeinput" type="radio" name="sa-15-theme" id="sa-15-theme-auto" checked>
    <label class="sa-15__themeopt" for="sa-15-theme-auto">Auto</label>
    <input class="sa-15__themeinput" type="radio" name="sa-15-theme" id="sa-15-theme-light">
    <label class="sa-15__themeopt" for="sa-15-theme-light">Light</label>
    <input class="sa-15__themeinput" type="radio" name="sa-15-theme" id="sa-15-theme-dark">
    <label class="sa-15__themeopt" for="sa-15-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-15__stage">
    <header class="sa-15__head">
      <p class="sa-15__eyebrow">timeline-scope</p>
      <h2 class="sa-15__h" id="sa-15-h">A timeline crossing into a sibling branch</h2>
      <p class="sa-15__sub">The scroller on the right publishes <span class="sa-15__mono">--sa-15-doc</span>. The header on the left is not inside it. Only <span class="sa-15__mono">timeline-scope</span> on their shared parent makes that subscription legal.</p>
    </header>

    <div class="sa-15__split">
      <div class="sa-15__branch">
        <p class="sa-15__btag">Branch A · header</p>
        <div class="sa-15__hdr">
          <p class="sa-15__hname">Vale · Field guide</p>
          <div class="sa-15__hbar"><span class="sa-15__hfill"></span></div>
          <p class="sa-15__hmeta">consumes <span class="sa-15__mono">--sa-15-doc</span> from a sibling</p>
        </div>
        <p class="sa-15__wire" aria-hidden="true"></p>
        <p class="sa-15__scopecode"><span class="sa-15__key">timeline-scope</span>: --sa-15-doc;<br><span class="sa-15__cmt">on the shared parent</span></p>
      </div>

      <div class="sa-15__col">
        <p class="sa-15__btag">Branch B · content, owns the timeline</p>
        <div class="sa-15__scroller" tabindex="0" role="region" aria-label="Vale field guide, scrollable">
          <div class="sa-15__doc">
            <p class="sa-15__local"><span class="sa-15__localfill"></span></p>
            <h3 class="sa-15__dh">Onboarding a new region</h3>
            <p class="sa-15__p">Provision the edge cache before the database replica. Sam Rivera keeps a checklist in the Vale runbook and it has not changed since March.</p>
            <p class="sa-15__p">Sync 4 repositories against the region manifest. A missing manifest entry is the most common cause of a half-provisioned region.</p>
            <p class="sa-15__p">Invite teammate for the on-call rotation before the first deploy, not after. Jordan Lee learned this the hard way in Orbit.</p>
            <p class="sa-15__p">Run the smoke suite twice — once cold, once warm. Cold catches configuration, warm catches capacity.</p>
            <p class="sa-15__p">Deploy to production behind a flag at 5% for an hour. Alex Chen reviews the error budget before it widens.</p>
            <p class="sa-15__p">File the region record in the audit log with the acting token id, then close the change ticket.</p>
            <p class="sa-15__p">Capacity headroom is checked twice: once against the seven-day peak, once against the projected quarter. Both live in the Vale planning sheet.</p>
            <p class="sa-15__p">Rotate the region signing key before handover, not after. Priya Sharma keeps the rotation window at fourteen days.</p>
            <p class="sa-15__p">Set the error budget alert to page rather than to email. A region without paging is a region nobody watches.</p>
            <p class="sa-15__p">Add the new region to the status page in the same change, so the first incident does not also become a communications incident.</p>
            <p class="sa-15__p">Hand the runbook to the on-call rotation and have someone who did not build the region walk it end to end.</p>
            <p class="sa-15__p">Archive the provisioning branch once the region has been live for a week. Nothing is more confusing than two live runbooks.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.sa-15 {
  --page: #eef1e9;
  --surface: #ffffff;
  --ink: #1a1f18;
  --muted: #5a6455;
  --rule: #cdd6c6;
  --accent: #3f7a52;
  --page: oklch(94.5% 0.014 130);
  --surface: oklch(100% 0 0);
  --ink: oklch(22% 0.02 140);
  --muted: oklch(48% 0.024 140);
  --rule: oklch(86% 0.02 132);
  --accent: oklch(52% 0.09 155);
  --font-display: ui-rounded, "SF Pro Rounded", "Segoe UI Variable", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  position: relative;
  padding: 4rem 1.25rem 3.5rem;
  background: var(--page);
  background-image: radial-gradient(60rem 30rem at 15% 0%, color-mix(in srgb, var(--accent) 14%, transparent), transparent 70%);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

.sa-15 *,
.sa-15 *::before,
.sa-15 *::after {
  box-sizing: border-box;
}

.sa-15__stage {
  max-inline-size: 62rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.sa-15__head {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.sa-15__eyebrow {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-15__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 4.2vw, 2.25rem);
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1.12;
}

.sa-15__sub {
  margin: 0;
  max-inline-size: 44rem;
  font-size: 0.9375rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-15__mono {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.85em;
  color: var(--accent);
}

.sa-15__split {
  display: grid;
  grid-template-columns: minmax(0, 0.85fr) minmax(0, 1.15fr);
  gap: 1.25rem;
  align-items: start;
  timeline-scope: --sa-15-doc;
}

.sa-15__branch,
.sa-15__col {
  display: flex;
  flex-direction: column;
  gap: 0.625rem;
  min-inline-size: 0;
}

.sa-15__btag {
  margin: 0;
  font-size: 0.625rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.sa-15__hdr {
  display: flex;
  flex-direction: column;
  gap: 0.625rem;
  padding: 1.125rem 1.25rem;
  border: 1px solid color-mix(in srgb, var(--ink) 12%, transparent);
  border-radius: 1rem;
  background: color-mix(in srgb, var(--surface) 60%, transparent);
  backdrop-filter: blur(12px) saturate(140%);
  box-shadow: 0 1rem 2rem -1rem color-mix(in srgb, var(--accent) 45%, transparent);
}

.sa-15__hname {
  margin: 0;
  font-family: var(--font-display);
  font-size: 1.125rem;
  font-weight: 600;
}

.sa-15__hbar {
  block-size: 0.5rem;
  border-radius: 999px;
  background: color-mix(in srgb, var(--ink) 10%, transparent);
  overflow: hidden;
}

.sa-15__hfill {
  display: block;
  block-size: 100%;
  inline-size: 100%;
  border-radius: 999px;
  background: var(--accent);
  transform-origin: left center;
  transform: scaleX(1);
}

.sa-15__hmeta {
  margin: 0;
  font-size: 0.75rem;
  color: var(--muted);
}

.sa-15__wire {
  margin: 0;
  block-size: 3.5rem;
  border-inline-start: 2px dashed var(--accent);
  margin-inline-start: 1.5rem;
  position: relative;
}

.sa-15__wire::after {
  content: "";
  position: absolute;
  inset-block-end: 0;
  inset-inline-start: -0.3125rem;
  inline-size: 0.5rem;
  block-size: 0.5rem;
  border-radius: 999px;
  background: var(--accent);
}

.sa-15__scopecode {
  margin: 0;
  padding: 0.75rem 0.875rem;
  border-radius: 0.75rem;
  background: color-mix(in srgb, var(--ink) 6%, transparent);
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.75rem;
  line-height: 1.6;
}

.sa-15__key {
  color: var(--accent);
  font-weight: 600;
}

.sa-15__cmt {
  color: var(--muted);
}

.sa-15__scroller {
  block-size: 56vh;
  min-block-size: 19rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  border-radius: 1rem;
  border: 1px solid var(--rule);
  background: var(--surface);
  scroll-timeline: --sa-15-doc block;
}

.sa-15__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sa-15__doc {
  min-block-size: calc(100% + 6rem);
  padding: 1rem 1.25rem 3rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.sa-15__local {
  position: sticky;
  inset-block-start: 0;
  margin: 0;
  block-size: 0.25rem;
  border-radius: 999px;
  background: color-mix(in srgb, var(--ink) 8%, transparent);
  overflow: hidden;
}

.sa-15__localfill {
  display: block;
  block-size: 100%;
  inline-size: 100%;
  background: color-mix(in srgb, var(--accent) 55%, transparent);
  transform-origin: left center;
  transform: scaleX(1);
}

.sa-15__dh {
  margin: 0;
  font-family: var(--font-display);
  font-size: 1.0625rem;
  font-weight: 600;
}

.sa-15__p {
  margin: 0;
  font-size: 0.875rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

@keyframes sa-15-fill {
  from {
    transform: scaleX(0.02);
  }

  to {
    transform: scaleX(1);
  }
}

@supports (animation-timeline: scroll()) {
  .sa-15__localfill {
    animation: sa-15-fill linear both;
    animation-timeline: scroll(nearest block);
  }
}

@supports (timeline-scope: --sa-15-doc) {
  .sa-15__hfill {
    animation: sa-15-fill linear both;
    animation-timeline: --sa-15-doc;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-15__hfill,
    .sa-15__localfill {
    animation: none;
    transform: scaleX(1);
  }
}

.sa-15__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
  display: inline-flex;
  gap: 0.125rem;
  margin: 0;
  padding: 0.25rem;
  border: 1px solid color-mix(in srgb, var(--ink) 12%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, var(--surface) 70%, transparent);
  backdrop-filter: blur(8px);
}

.sa-15__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-15__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-15__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.75rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-15__themeinput:checked + .sa-15__themeopt {
  color: var(--surface);
  background: var(--accent);
}

.sa-15__themeinput:focus-visible + .sa-15__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 48rem) {
  .sa-15__split {
    grid-template-columns: minmax(0, 1fr);
  }

  .sa-15__wire {
    block-size: 2rem;
  }

  .sa-15 {
    padding-block-start: 4.5rem;
  }
}

@media (forced-colors: active) {
  .sa-15__hfill,
    .sa-15__localfill {
    background: Highlight;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-15:not(:has(#sa-15-theme-light:checked)) {
    --page: #101410;
    --surface: #171d17;
    --ink: #e8efe6;
    --muted: #97a494;
    --rule: #263025;
    --accent: #6ec48c;
  }

  .sa-15:not(:has(#sa-15-theme-light:checked)) .sa-15__themeinput:checked + .sa-15__themeopt {
    color: #101410;
  }
}

@media (prefers-color-scheme: light) {
  .sa-15:has(#sa-15-theme-dark:checked) {
    --page: #101410;
    --surface: #171d17;
    --ink: #e8efe6;
    --muted: #97a494;
    --rule: #263025;
    --accent: #6ec48c;
  }

  .sa-15:has(#sa-15-theme-dark:checked) .sa-15__themeinput:checked + .sa-15__themeopt {
    color: #101410;
  }
}

[data-theme="dark"] .sa-15:not(:has(#sa-15-theme-light:checked)) {
  --page: #101410;
  --surface: #171d17;
  --ink: #e8efe6;
  --muted: #97a494;
  --rule: #263025;
  --accent: #6ec48c;
}

.sa-15:has(#sa-15-theme-dark:checked) {
  --page: #101410;
  --surface: #171d17;
  --ink: #e8efe6;
  --muted: #97a494;
  --rule: #263025;
  --accent: #6ec48c;
}

.sa-15:has(#sa-15-theme-dark:checked) .sa-15__themeinput:checked + .sa-15__themeopt {
  color: #101410;
}

.sa-15:has(#sa-15-theme-light:checked) {
  --page: #eef1e9;
  --surface: #ffffff;
  --ink: #1a1f18;
  --muted: #5a6455;
  --rule: #cdd6c6;
  --accent: #3f7a52;
}
```
