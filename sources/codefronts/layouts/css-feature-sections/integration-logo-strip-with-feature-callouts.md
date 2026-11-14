---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/integration-logo-strip-with-feature-callouts/"
title: "Integration Logo Strip with Feature Callouts"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "A works-with-your-stack strip: twelve integration marks in a hairline grid across the top, then three callouts spelling out what those connections actually…"
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Integration Logo Strip with Feature Callouts
Source: https://codefronts.com/layouts/css-feature-sections/integration-logo-strip-with-feature-callouts/

A works-with-your-stack strip: twelve integration marks in a hairline grid across the top, then three callouts spelling out what those connections actually buy you — SSO in sixty seconds, Slack alerts, GitHub-native workflows. Everything is inline SVG on a monochrome ground, so the logos sit at one visual weight and the copy underneath carries the argument.
## HTML
```html
<section class="fs-06" aria-labelledby="fs-06-heading">
  <div class="fs-06__hero" aria-hidden="true">
    <span class="fs-06__wordmark">ORBIT</span>
    <span class="fs-06__heronav">Product / Integrations / Enterprise</span>
  </div>

  <div class="fs-06__stage">
    <div class="fs-06__head">
      <p class="fs-06__eyebrow">Works with your stack</p>
      <h2 class="fs-06__heading" id="fs-06-heading">Twelve systems, connected before your standup ends</h2>
    </div>

    <ul class="fs-06__strip">
      <li class="fs-06__cell"><span class="fs-06__mark" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M8 12h8"/></svg></span><span class="fs-06__lname">Basalt</span></li>
      <li class="fs-06__cell"><span class="fs-06__mark" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M12 3v18"/></svg></span><span class="fs-06__lname">Fern</span></li>
      <li class="fs-06__cell"><span class="fs-06__mark" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 20 12 4l8 16z"/></svg></span><span class="fs-06__lname">Talon</span></li>
      <li class="fs-06__cell"><span class="fs-06__mark" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="4" y="4" width="7" height="7"/><rect x="13" y="13" width="7" height="7"/></svg></span><span class="fs-06__lname">Nova</span></li>
      <li class="fs-06__cell"><span class="fs-06__mark" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3l7 4v10l-7 4-7-4V7z"/></svg></span><span class="fs-06__lname">Ranger</span></li>
      <li class="fs-06__cell"><span class="fs-06__mark" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="8" cy="12" r="4"/><circle cx="16" cy="12" r="4"/></svg></span><span class="fs-06__lname">Sable</span></li>
      <li class="fs-06__cell"><span class="fs-06__mark" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h16M12 4v16" stroke-linecap="round"/></svg></span><span class="fs-06__lname">Quill</span></li>
      <li class="fs-06__cell"><span class="fs-06__mark" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 17 12 5l7 12z"/><path d="M8 17h8"/></svg></span><span class="fs-06__lname">Vale</span></li>
      <li class="fs-06__cell"><span class="fs-06__mark" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="7" width="18" height="10" rx="5"/><circle cx="8" cy="12" r="2"/></svg></span><span class="fs-06__lname">Meridian</span></li>
      <li class="fs-06__cell"><span class="fs-06__mark" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M6 6l12 12M18 6 6 18"/></svg></span><span class="fs-06__lname">Aperture</span></li>
      <li class="fs-06__cell"><span class="fs-06__mark" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 4v16M6 9l6-5 6 5"/></svg></span><span class="fs-06__lname">Prism</span></li>
      <li class="fs-06__cell"><span class="fs-06__mark" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r="9"/></svg></span><span class="fs-06__lname">Sundial</span></li>
    </ul>

    <div class="fs-06__callouts">
      <article class="fs-06__callout">
        <p class="fs-06__ckicker">01 / Identity</p>
        <h3 class="fs-06__ctitle">SSO wired in sixty seconds</h3>
        <p class="fs-06__cprose">Point us at your IdP metadata URL and provisioning starts on the next login. SCIM groups map to Orbit roles without a support ticket.</p>
        <a class="fs-06__clink" href="#fs-06-heading">Identity setup guide</a>
      </article>
      <article class="fs-06__callout">
        <p class="fs-06__ckicker">02 / Alerting</p>
        <h3 class="fs-06__ctitle">Alerts land where the team already is</h3>
        <p class="fs-06__cprose">Route by severity to a channel, a rotation or a person. Threads carry the run history, so nobody re-opens a resolved incident.</p>
        <a class="fs-06__clink" href="#fs-06-heading">Alert routing reference</a>
      </article>
      <article class="fs-06__callout">
        <p class="fs-06__ckicker">03 / Workflow</p>
        <h3 class="fs-06__ctitle">Checks that run in the pull request</h3>
        <p class="fs-06__cprose">Every change opens with a preview environment and a diff of the affected datasets, posted as a status check on the branch.</p>
        <a class="fs-06__clink" href="#fs-06-heading">CI integration docs</a>
      </article>
    </div>
  </div>

  <div class="fs-06__below" aria-hidden="true">Full connector catalogue · Request an integration</div>
</section>
```
## CSS
```css
.fs-06 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --paper: #ffffff;
  --ink: #0b0b0b;
  --ink: oklch(0.15 0 0);
  --muted: #6b6b6b;
  --muted: oklch(0.53 0 0);
  --rule: #dcdcdc;
  --rule: oklch(0.89 0 0);
  --accent: #0b0b0b;
  --strip-pad: 14px;
  --font-display: "Helvetica Neue", "Inter Tight", system-ui, -apple-system, sans-serif;
  background: var(--paper);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-06 *,
.fs-06 *::before,
.fs-06 *::after {
  box-sizing: border-box;
}

.fs-06__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 14px;
  justify-content: space-between;
  align-items: baseline;
  padding: 14px 18px;
  border-block-end: 1px solid var(--rule);
}

.fs-06__wordmark {
  font: 700 13px/1 var(--font-display);
  letter-spacing: 0.3em;
}

.fs-06__heronav {
  font-size: 11.5px;
  letter-spacing: 0.06em;
  color: var(--muted);
  text-transform: uppercase;
}

.fs-06__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(26px, 5vw, 56px) 16px;
}

.fs-06__head {
  inline-size: 100%;
  max-inline-size: 64rem;
  min-inline-size: 0;
  margin: 0 0 20px;
}

.fs-06__eyebrow {
  margin: 0 0 12px;
  font: 700 10px/1 var(--font-display);
  letter-spacing: 0.34em;
  text-transform: uppercase;
  color: var(--muted);
}

.fs-06__heading {
  margin: 0;
  max-inline-size: 26ch;
  font: 500 clamp(24px, 4.4vw, 38px)/1.08 var(--font-display);
  letter-spacing: -0.025em;
  text-wrap: balance;
}

.fs-06__strip {
  inline-size: 100%;
  max-inline-size: 64rem;
  min-inline-size: 0;
  margin: 0 0 clamp(24px, 4vw, 44px);
  padding: 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 120px), 1fr));
  border: 1px solid var(--rule);
  border-block-end: 0;
  border-inline-end: 0;
  overflow: hidden;
}

.fs-06__cell {
  min-inline-size: 0;
  display: grid;
  place-items: center;
  gap: 7px;
  padding: var(--strip-pad) 8px;
  border-inline-end: 1px solid var(--rule);
  border-block-end: 1px solid var(--rule);
  color: var(--muted);
  filter: grayscale(1);
  transition: color .16s ease, background-color .16s ease, filter .16s ease;
}

.fs-06__cell:hover,
.fs-06__cell:focus-within {
  color: var(--ink);
  background: color-mix(in oklab, var(--ink) 4%, var(--paper));
  filter: none;
}

.fs-06__mark {
  display: inline-flex;
}

.fs-06__lname {
  font: 600 10.5px/1 var(--font-display);
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.fs-06__callouts {
  inline-size: 100%;
  max-inline-size: 64rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr));
  gap: 1px;
  background: var(--rule);
  border: 1px solid var(--rule);
}

.fs-06__callout {
  min-inline-size: 0;
  padding: clamp(16px, 2.6vw, 26px);
  background: var(--paper);
}

.fs-06__ckicker {
  margin: 0 0 14px;
  font: 700 10px/1 var(--font-display);
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--muted);
}

.fs-06__ctitle {
  margin: 0 0 10px;
  font: 500 clamp(16px, 2vw, 19px)/1.25 var(--font-display);
  letter-spacing: -0.015em;
  text-wrap: balance;
}

.fs-06__cprose {
  margin: 0 0 16px;
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-06__clink {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  font: 600 12px/1 var(--font-display);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--ink);
  text-decoration: none;
  border-block-end: 1px solid var(--ink);
}

.fs-06__clink:hover {
  color: var(--muted);
  border-color: var(--muted);
}

.fs-06__clink:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 4px;
}

.fs-06__below {
  padding: 14px 18px;
  border-block-start: 1px solid var(--rule);
  font-size: 11.5px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .fs-06__cell {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .fs-06 {
    --paper: #0b0b0b;
    --ink: #f4f4f4;
    --muted: #8f8f8f;
    --rule: #262626;
    --accent: #f4f4f4;
  }
}

[data-theme="dark"] .fs-06 {
  --paper: #0b0b0b;
  --ink: #f4f4f4;
  --muted: #8f8f8f;
  --rule: #262626;
  --accent: #f4f4f4;
}
```
