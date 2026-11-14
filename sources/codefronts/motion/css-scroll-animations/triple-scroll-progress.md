---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/triple-scroll-progress/"
title: "Scroll Timeline Reference and Progress Binding"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "The reference build for the whole collection."
has_js: "false"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll Timeline Reference and Progress Binding
Source: https://codefronts.com/motion/css-scroll-animations/triple-scroll-progress/

The reference build for the whole collection. One indicator is bound with animation-timeline: scroll(), every part of the scroll() function is named beside it, and a live percentage readout proves the progress is the scroll offset itself rather than a timer. Start here before any other demo, then read the rule that catches everyone: animation-duration is ignored.
## HTML
```html
<section class="sa-09" aria-labelledby="sa-09-h">
  <fieldset class="sa-09__theme">
    <legend class="sa-09__themelegend">Theme</legend>
    <input class="sa-09__themeinput" type="radio" name="sa-09-theme" id="sa-09-theme-auto" checked>
    <label class="sa-09__themeopt" for="sa-09-theme-auto">Auto</label>
    <input class="sa-09__themeinput" type="radio" name="sa-09-theme" id="sa-09-theme-light">
    <label class="sa-09__themeopt" for="sa-09-theme-light">Light</label>
    <input class="sa-09__themeinput" type="radio" name="sa-09-theme" id="sa-09-theme-dark">
    <label class="sa-09__themeopt" for="sa-09-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-09__stage">
    <header class="sa-09__head">
      <p class="sa-09__eyebrow">Reference build 01</p>
      <h2 class="sa-09__h" id="sa-09-h">Progress bound to a scroll offset</h2>
      <p class="sa-09__sub">Scroll the panel. The indicator is not playing — it is being read. Halfway down is halfway through, and scrolling up runs it backward.</p>
    </header>

    <dl class="sa-09__roles">
      <div class="sa-09__role"><dt class="sa-09__rdt">Scroller</dt><dd class="sa-09__rdd">the release-notes panel below</dd></div>
      <div class="sa-09__role"><dt class="sa-09__rdt">Subject</dt><dd class="sa-09__rdd">the sticky fill bar inside it</dd></div>
      <div class="sa-09__role"><dt class="sa-09__rdt">Axis</dt><dd class="sa-09__rdd">block</dd></div>
    </dl>

    <div class="sa-09__frame">
      <div class="sa-09__scroller" id="sa-09-scroller" tabindex="0" role="region" aria-label="Meridian release notes, scrollable">
        <div class="sa-09__sticky">
          <div class="sa-09__track"><span class="sa-09__fill"></span></div>
          <p class="sa-09__readout"><span class="sa-09__num"></span><span class="sa-09__pct">%</span><span class="sa-09__rlabel">resolved progress</span></p>
        </div>
        <div class="sa-09__doc">
          <h3 class="sa-09__dh">Meridian 4.2 — release notes</h3>
          <p class="sa-09__p">Deploy to production now runs the migration check before the image build, so a bad schema fails in twelve seconds rather than four minutes.</p>
          <p class="sa-09__p">Sync 4 repositories replaces the old per-repo poll. Fern, Basalt, Talon and Vale share one webhook queue and one retry budget.</p>
          <p class="sa-09__p">Invite teammate accepts a comma-separated list. Alex Chen reported the paste-a-spreadsheet-column case; it works now.</p>
          <p class="sa-09__p">Audit log entries carry the acting token id. Priya Sharma asked for this during the Orbit review and it is on by default.</p>
          <p class="sa-09__p">Scheduled exports moved to the queue workers, so a large export no longer blocks interactive requests for the whole account.</p>
          <p class="sa-09__p">Region failover is manual for now. Jordan Lee is drafting the automatic promotion path for 4.3.</p>
          <p class="sa-09__p">Removed the legacy v1 token endpoint. Sam Rivera confirmed no account has called it in ninety days.</p>
          <p class="sa-09__p">Billing invoices render server-side, which cut the PDF path from three services down to one.</p>
          <p class="sa-09__p">Webhook retries back off to a maximum of six attempts. Beyond that the delivery is parked and surfaced in the dashboard.</p>
          <p class="sa-09__p">Search indexes rebuild incrementally. A full reindex on the Basalt account went from fifty minutes to four.</p>
          <p class="sa-09__p">Personal access tokens can be scoped per repository. Alex Chen asked for this after the Fern migration.</p>
          <p class="sa-09__p">The activity feed paginates by cursor rather than by page number, so entries no longer shift under you mid-read.</p>
          <p class="sa-09__p">Environment variables are diffed before a deploy, and the diff is attached to the change record.</p>
          <p class="sa-09__p">Known issue: the audit export still truncates at fifty thousand rows. A streaming export lands in 4.3.</p>
        </div>
      </div>

      <aside class="sa-09__annot">
        <p class="sa-09__acode"><span class="sa-09__akey">animation-timeline</span>: scroll(<span class="sa-09__aarg">nearest</span> <span class="sa-09__aarg2">block</span>);</p>
        <ul class="sa-09__alist">
          <li class="sa-09__ai"><span class="sa-09__aarg">nearest</span> — the scroller. Nearest ancestor scroll container. Also <span class="sa-09__mono">root</span>, <span class="sa-09__mono">self</span>, <span class="sa-09__mono">closest</span>.</li>
          <li class="sa-09__ai"><span class="sa-09__aarg2">block</span> — the axis, on the scroller. Also <span class="sa-09__mono">inline</span>, <span class="sa-09__mono">x</span>, <span class="sa-09__mono">y</span>.</li>
          <li class="sa-09__ai sa-09__ai--warn"><span class="sa-09__mono">animation-duration</span> is ignored here. There is no time on this timeline — only offset.</li>
        </ul>
      </aside>
    </div>
  </div>
</section>
```
## CSS
```css
.sa-09 {
  --page: #f4f6fa;
  --surface: #ffffff;
  --ink: #0f1729;
  --muted: #5b6780;
  --rule: #ccd7e8;
  --grid: #e5ecf6;
  --accent: #1d5bd6;
  --page: oklch(97.2% 0.011 250);
  --surface: oklch(100% 0 0);
  --ink: oklch(21% 0.045 262);
  --muted: oklch(51% 0.035 258);
  --rule: oklch(85% 0.032 250);
  --grid: oklch(94% 0.018 250);
  --accent: oklch(50% 0.19 260);
  --font-display: ui-monospace, "JetBrains Mono", "SFMono-Regular", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  position: relative;
  padding: 3.5rem 1rem 3rem;
  background: var(--page);
  background-image: linear-gradient(var(--grid) 1px, transparent 1px), linear-gradient(90deg, var(--grid) 1px, transparent 1px);
  background-size: 2rem 2rem;
  color: var(--ink);
  font-family: system-ui, sans-serif;
  -webkit-font-smoothing: antialiased;
}

.sa-09 *,
.sa-09 *::before,
.sa-09 *::after {
  box-sizing: border-box;
}

.sa-09__stage {
  max-inline-size: 60rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.sa-09__head {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.sa-09__eyebrow {
  margin: 0;
  font-family: var(--font-display);
  font-size: 0.6875rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-09__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.375rem, 4vw, 2rem);
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1.15;
}

.sa-09__sub {
  margin: 0;
  max-inline-size: 46rem;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-09__roles {
  display: flex;
  flex-wrap: wrap;
  gap: 0 1.5rem;
  margin: 0;
  padding: 0.75rem 1rem;
  border-block: 1px solid var(--rule);
  background: color-mix(in srgb, var(--surface) 70%, transparent);
}

.sa-09__role {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
  min-inline-size: 0;
}

.sa-09__rdt {
  font-family: var(--font-display);
  font-size: 0.6875rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}

.sa-09__rdd {
  margin: 0;
  font-size: 0.8125rem;
  font-weight: 600;
}

.sa-09__frame {
  display: grid;
  grid-template-columns: minmax(0, 1.55fr) minmax(0, 1fr);
  gap: 1rem;
  align-items: start;
}

.sa-09__scroller {
  block-size: 60vh;
  min-block-size: 20rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  border: 1px solid var(--rule);
  background: var(--surface);
  scroll-timeline-name: --sa-09-track;
  scroll-timeline-axis: block;
}

.sa-09__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sa-09__sticky {
  position: sticky;
  inset-block-start: 0;
  z-index: 2;
  display: flex;
  align-items: center;
  gap: 0.875rem;
  padding: 0.75rem 1rem;
  border-block-end: 1px solid var(--rule);
  background: color-mix(in srgb, var(--surface) 92%, transparent);
  backdrop-filter: blur(6px);
}

.sa-09__track {
  flex: 1 1 auto;
  min-inline-size: 0;
  block-size: 0.375rem;
  background: var(--grid);
  border-radius: 0;
  overflow: hidden;
}

.sa-09__fill {
  display: block;
  block-size: 100%;
  inline-size: 100%;
  background: var(--accent);
  transform-origin: left center;
  transform: scaleX(1);
}

.sa-09__readout {
  display: flex;
  align-items: baseline;
  gap: 0.25rem;
  margin: 0;
  font-family: var(--font-display);
}

.sa-09__num {
  font-size: 1.125rem;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.sa-09__num::after {
  content: "100";
}

.sa-09__pct {
  font-size: 0.75rem;
  color: var(--muted);
}

.sa-09__rlabel {
  margin-inline-start: 0.375rem;
  font-size: 0.625rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
}

.sa-09__doc {
  min-block-size: calc(100% + 6rem);
  padding: 1.25rem 1.25rem 3rem;
  display: flex;
  flex-direction: column;
  gap: 0.875rem;
}

.sa-09__dh {
  margin: 0;
  font-family: var(--font-display);
  font-size: 0.9375rem;
  font-weight: 600;
}

.sa-09__p {
  margin: 0;
  font-size: 0.875rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-09__annot {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  padding: 1rem;
  border: 1px solid var(--rule);
  border-block-start: 3px solid var(--accent);
  background: var(--surface);
}

.sa-09__acode {
  margin: 0;
  font-family: var(--font-display);
  font-size: 0.8125rem;
  line-height: 1.5;
  word-break: break-word;
}

.sa-09__akey {
  color: var(--accent);
  font-weight: 600;
}

.sa-09__aarg {
  border-block-end: 2px solid var(--accent);
  font-weight: 600;
}

.sa-09__aarg2 {
  border-block-end: 2px dotted var(--ink);
  font-weight: 600;
}

.sa-09__alist {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.625rem;
}

.sa-09__ai {
  font-size: 0.8125rem;
  line-height: 1.5;
  color: var(--muted);
  padding-block-start: 0.625rem;
  border-block-start: 1px solid var(--rule);
  text-wrap: pretty;
}

.sa-09__ai--warn {
  color: var(--ink);
  font-weight: 500;
}

.sa-09__mono {
  font-family: var(--font-display);
  font-size: 0.78em;
  padding: 0.05em 0.3em;
  background: var(--grid);
}

@property --sa-09-p {
  syntax: "<integer>";
  inherits: true;
  initial-value: 100;
}

@keyframes sa-09-fill {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

@keyframes sa-09-count {
  from {
    --sa-09-p: 0;
  }

  to {
    --sa-09-p: 100;
  }
}

@supports (animation-timeline: scroll()) {
  .sa-09__fill {
    animation: sa-09-fill linear both;
    animation-timeline: scroll(nearest block);
  }

  .sa-09__readout {
    animation: sa-09-count linear both;
    animation-timeline: scroll(nearest block);
  }

  .sa-09__num::after {
    content: counter(sa-09-c);
    counter-reset: sa-09-c var(--sa-09-p);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-09__fill {
    animation: none;
    transform: scaleX(1);
  }
}

.sa-09__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: inline-flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid var(--rule);
  background: var(--surface);
}

.sa-09__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-09__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-09__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  font-family: var(--font-display);
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-09__themeinput:checked + .sa-09__themeopt {
  color: var(--surface);
  background: var(--ink);
}

.sa-09__themeinput:focus-visible + .sa-09__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 48rem) {
  .sa-09__frame {
    grid-template-columns: minmax(0, 1fr);
  }

  .sa-09 {
    padding-block-start: 4.5rem;
  }
}

@media (forced-colors: active) {
  .sa-09__fill {
    background: Highlight;
  }

  .sa-09__themeinput:checked + .sa-09__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-09:not(:has(#sa-09-theme-light:checked)) {
    --page: #080b12;
    --surface: #101725;
    --ink: #e8eefb;
    --muted: #93a2c0;
    --rule: #22304a;
    --grid: #131c2c;
    --accent: #6ea8ff;
  }
}

@media (prefers-color-scheme: light) {
  .sa-09:has(#sa-09-theme-dark:checked) {
    --page: #080b12;
    --surface: #101725;
    --ink: #e8eefb;
    --muted: #93a2c0;
    --rule: #22304a;
    --grid: #131c2c;
    --accent: #6ea8ff;
  }
}

[data-theme="dark"] .sa-09:not(:has(#sa-09-theme-light:checked)) {
  --page: #080b12;
  --surface: #101725;
  --ink: #e8eefb;
  --muted: #93a2c0;
  --rule: #22304a;
  --grid: #131c2c;
  --accent: #6ea8ff;
}

.sa-09:has(#sa-09-theme-dark:checked) {
  --page: #080b12;
  --surface: #101725;
  --ink: #e8eefb;
  --muted: #93a2c0;
  --rule: #22304a;
  --grid: #131c2c;
  --accent: #6ea8ff;
}

.sa-09:has(#sa-09-theme-light:checked) {
  --page: #f4f6fa;
  --surface: #ffffff;
  --ink: #0f1729;
  --muted: #5b6780;
  --rule: #ccd7e8;
  --grid: #e5ecf6;
  --accent: #1d5bd6;
}
```
