---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/css-saas-features-section-2025/"
title: "SaaS Modern Features Section Grid"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "A contemporary six-cell product grid: layered dark surfaces, a gradient hairline that lights up on hover, an animated icon tile and a Learn more link whose…"
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS Modern Features Section Grid
Source: https://codefronts.com/layouts/css-feature-sections/css-saas-features-section-2025/

A contemporary six-cell product grid: layered dark surfaces, a gradient hairline that lights up on hover, an animated icon tile and a Learn more link whose arrow slides on interaction. The gradient rim is a masked border rather than a wrapper div, so cards keep a single element and the accent can shift hue per row without new markup.
## HTML
```html
<section class="fs-19" aria-labelledby="fs-19-heading">
  <div class="fs-19__hero" aria-hidden="true">
    <span class="fs-19__wordmark">Aperture Cloud</span>
    <span class="fs-19__heronav">Product · Customers · Docs</span>
  </div>

  <div class="fs-19__stage">
    <div class="fs-19__head">
      <p class="fs-19__eyebrow">The platform</p>
      <h2 class="fs-19__heading" id="fs-19-heading">Everything between your repository and your users</h2>
      <p class="fs-19__sub">Six primitives, one control plane, no glue code to maintain.</p>
    </div>

    <ul class="fs-19__grid">
      <li class="fs-19__card">
        <span class="fs-19__tile" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M12 3 3 8l9 5 9-5z"/><path d="M3 14l9 5 9-5"/></svg></span>
        <h3 class="fs-19__ctitle">Global CDN with edge functions</h3>
        <p class="fs-19__cprose">Static assets and dynamic handlers on the same 310-location network, so personalisation does not cost you a round trip to origin.</p>
        <a class="fs-19__more" href="#fs-19-heading">Learn more <span aria-hidden="true">→</span></a>
      </li>
      <li class="fs-19__card">
        <span class="fs-19__tile" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M7 9h6M7 13h10"/></svg></span>
        <h3 class="fs-19__ctitle">Type-safe API generation</h3>
        <p class="fs-19__cprose">Your schema produces clients, mocks and fixtures for four languages, versioned in the same commit as the change.</p>
        <a class="fs-19__more" href="#fs-19-heading">Learn more <span aria-hidden="true">→</span></a>
      </li>
      <li class="fs-19__card">
        <span class="fs-19__tile" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M4 19V9M10 19V5M16 19v-7M22 19h-20"/></svg></span>
        <h3 class="fs-19__ctitle">Observability without an agent</h3>
        <p class="fs-19__cprose">Traces, logs and metrics correlated by request id out of the box, retained for thirty days on every plan.</p>
        <a class="fs-19__more" href="#fs-19-heading">Learn more <span aria-hidden="true">→</span></a>
      </li>
      <li class="fs-19__card">
        <span class="fs-19__tile" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/></svg></span>
        <h3 class="fs-19__ctitle">Scheduled jobs with real retries</h3>
        <p class="fs-19__cprose">Cron with exponential backoff, a dead-letter queue and a replay button, rather than a lambda and a prayer.</p>
        <a class="fs-19__more" href="#fs-19-heading">Learn more <span aria-hidden="true">→</span></a>
      </li>
      <li class="fs-19__card">
        <span class="fs-19__tile" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M12 3l8 4v6c0 4-3.5 7-8 8-4.5-1-8-4-8-8V7z"/><path d="M9.5 12.5 12 15l3.5-4"/></svg></span>
        <h3 class="fs-19__ctitle">Native SSO with SCIM provisioning</h3>
        <p class="fs-19__cprose">SAML and OIDC on every tier, with directory-driven roles and deprovisioning that lands inside a minute.</p>
        <a class="fs-19__more" href="#fs-19-heading">Learn more <span aria-hidden="true">→</span></a>
      </li>
      <li class="fs-19__card">
        <span class="fs-19__tile" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M5 12h14M12 5v14" stroke-linecap="round"/><rect x="3" y="3" width="18" height="18" rx="4"/></svg></span>
        <h3 class="fs-19__ctitle">Preview environments per branch</h3>
        <p class="fs-19__cprose">Seeded data, its own subdomain and a teardown on merge, posted back to the pull request automatically.</p>
        <a class="fs-19__more" href="#fs-19-heading">Learn more <span aria-hidden="true">→</span></a>
      </li>
    </ul>
  </div>

  <div class="fs-19__below" aria-hidden="true">Compare plans · Status · Changelog</div>
</section>
```
## CSS
```css
.fs-19 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --s0: #0b0d16;
  --s0: oklch(0.17 0.024 275);
  --s1: #121523;
  --s1: oklch(0.21 0.028 275);
  --s2: #1a1e30;
  --s2: oklch(0.26 0.032 275);
  --ink: #f0f1f7;
  --muted: #9aa0bb;
  --muted: oklch(0.73 0.028 276);
  --rule: #232841;
  --rule: oklch(0.3 0.035 275);
  --accent-a: #7c6cff;
  --accent-a: oklch(0.66 0.19 285);
  --accent-b: #3ecfd4;
  --accent-b: oklch(0.81 0.12 195);
  --font-display: "Geist", "Inter Tight", system-ui, -apple-system, sans-serif;
  background: var(--s0);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-19 *,
.fs-19 *::before,
.fs-19 *::after {
  box-sizing: border-box;
}

.fs-19__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
  justify-content: space-between;
  align-items: baseline;
  padding: 16px 22px;
  border-block-end: 1px solid var(--rule);
}

.fs-19__wordmark {
  font: 650 15px/1 var(--font-display);
  letter-spacing: -0.03em;
}

.fs-19__heronav {
  font-size: 12px;
  color: var(--muted);
}

.fs-19__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(30px, 5.5vw, 66px) 18px;
}

.fs-19__head {
  inline-size: 100%;
  max-inline-size: 68rem;
  min-inline-size: 0;
  margin: 0 0 clamp(24px, 4vw, 40px);
}

.fs-19__eyebrow {
  display: inline-block;
  margin: 0 0 14px;
  padding: 5px 11px;
  font: 650 10.5px/1 var(--font-display);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--ink);
  background: var(--s2);
  border: 1px solid var(--rule);
  border-radius: 999px;
}

.fs-19__heading {
  margin: 0 0 10px;
  max-inline-size: 28ch;
  font: 650 clamp(27px, 5vw, 43px)/1.08 var(--font-display);
  letter-spacing: -0.04em;
  text-wrap: balance;
}

.fs-19__sub {
  margin: 0;
  font-size: 15px;
  color: var(--muted);
}

.fs-19__grid {
  inline-size: 100%;
  max-inline-size: 68rem;
  min-inline-size: 0;
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 275px), 1fr));
  gap: 16px;
}

.fs-19__card {
  min-inline-size: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 22px 20px 20px;
  border: 1px solid transparent;
  border-radius: 16px;
  background: linear-gradient(var(--s2), var(--s2)) padding-box, linear-gradient(150deg, var(--rule), var(--rule)) border-box;
  transition: background .25s ease;
}

.fs-19__card:hover,
.fs-19__card:focus-within {
  background: linear-gradient(var(--s2), var(--s2)) padding-box, linear-gradient(150deg, var(--accent-a), var(--accent-b)) border-box;
}

.fs-19__tile {
  display: grid;
  place-items: center;
  inline-size: 42px;
  block-size: 42px;
  border-radius: 12px;
  color: var(--ink);
  background: linear-gradient(145deg, color-mix(in oklab, var(--accent-a) 32%, var(--s2)), color-mix(in oklab, var(--accent-b) 26%, var(--s2)));
  transition: transform .25s ease, filter .25s ease;
}

.fs-19__card:hover .fs-19__tile,
.fs-19__card:focus-within .fs-19__tile {
  transform: rotate(-4deg) scale(1.05);
  filter: brightness(1.15);
}

.fs-19__ctitle {
  margin: 0;
  font: 650 16.5px/1.3 var(--font-display);
  letter-spacing: -0.025em;
  text-wrap: balance;
}

.fs-19__cprose {
  margin: 0;
  font-size: 13.5px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-19__more {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  align-self: start;
  margin-block-start: auto;
  min-height: 44px;
  font: 600 13px/1 var(--font-display);
  color: var(--accent-b);
  text-decoration: none;
}

.fs-19__more span {
  transition: transform .2s ease;
}

.fs-19__more:hover span,
.fs-19__more:focus-visible span {
  transform: translateX(4px);
}

.fs-19__more:focus-visible {
  outline: 2px solid var(--accent-b);
  outline-offset: 3px;
  border-radius: 6px;
}

.fs-19__below {
  padding: 16px 22px;
  border-block-start: 1px solid var(--rule);
  font-size: 12px;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .fs-19__card,
    .fs-19__tile,
    .fs-19__more span {
    transition: none;
  }
}

@media (prefers-color-scheme: light) {
  .fs-19 {
    --s0: #f6f7fb;
    --s1: #ffffff;
    --s2: #ffffff;
    --ink: #12152a;
    --muted: #5b6280;
    --rule: #dfe2ee;
    --accent-a: #5b46e0;
    --accent-b: #0d8f9c;
  }

  .fs-19__tile {
    color: #ffffff;
    background: linear-gradient(145deg, var(--accent-a), var(--accent-b));
  }

  .fs-19__eyebrow {
    color: var(--ink);
    background: #ffffff;
  }
}

[data-theme="dark"] .fs-19 {
  --s0: #0b0d16;
  --s2: #1a1e30;
  --ink: #f0f1f7;
  --muted: #9aa0bb;
  --rule: #232841;
  --accent-a: #7c6cff;
  --accent-b: #3ecfd4;
}
```
