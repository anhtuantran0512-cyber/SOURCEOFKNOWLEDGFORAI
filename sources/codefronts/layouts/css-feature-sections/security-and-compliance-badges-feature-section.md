---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/security-and-compliance-badges-feature-section/"
title: "Security and Compliance Badges Feature Section"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "The block a security reviewer scrolls to first: six compliance badges in a grid — SOC 2 Type II, HIPAA, GDPR, ISO 27001, PCI DSS, FedRAMP — each revealing…"
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Security and Compliance Badges Feature Section
Source: https://codefronts.com/layouts/css-feature-sections/security-and-compliance-badges-feature-section/

The block a security reviewer scrolls to first: six compliance badges in a grid — SOC 2 Type II, HIPAA, GDPR, ISO 27001, PCI DSS, FedRAMP — each revealing its scope and audit date on hover or keyboard focus, with three supporting security callouts underneath covering encryption, SSO and audit logging. Dark charcoal ground, amber accent, dot-grid texture.
## HTML
```html
<section class="fs-09" aria-labelledby="fs-09-heading">
  <div class="fs-09__hero" aria-hidden="true">
    <span class="fs-09__wordmark">Basalt</span>
    <span class="fs-09__heronav">Infrastructure for regulated teams</span>
  </div>

  <div class="fs-09__stage">
    <div class="fs-09__head">
      <p class="fs-09__eyebrow">Trust &amp; compliance</p>
      <h2 class="fs-09__heading" id="fs-09-heading">Every control your security review asks about</h2>
      <p class="fs-09__sub">Hover or tab through a badge for its scope and last audit. Reports are available under NDA.</p>
    </div>

    <ul class="fs-09__badges">
      <li class="fs-09__badge" tabindex="0">
        <span class="fs-09__bmark" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M12 3l8 4v6c0 4-3.5 7-8 8-4.5-1-8-4-8-8V7z"/><path d="M9 12l2.2 2.2L15.5 10"/></svg></span>
        <span class="fs-09__bname">SOC 2 Type II</span>
        <span class="fs-09__tip" role="note">Annual audit, continuous monitoring. Latest report March, covering security, availability and confidentiality.</span>
      </li>
      <li class="fs-09__badge" tabindex="0">
        <span class="fs-09__bmark" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M12 4v16M4 12h16"/><circle cx="12" cy="12" r="9"/></svg></span>
        <span class="fs-09__bname">HIPAA</span>
        <span class="fs-09__tip" role="note">BAA signed on request. PHI isolated to a dedicated tenant with per-field encryption keys.</span>
      </li>
      <li class="fs-09__badge" tabindex="0">
        <span class="fs-09__bmark" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></span>
        <span class="fs-09__bname">GDPR</span>
        <span class="fs-09__tip" role="note">EU data residency in Frankfurt and Dublin. DPA, SCCs and a 30-day deletion SLA.</span>
      </li>
      <li class="fs-09__badge" tabindex="0">
        <span class="fs-09__bmark" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="4" y="4" width="16" height="16" rx="3"/><path d="M8 12h8M12 8v8"/></svg></span>
        <span class="fs-09__bname">ISO 27001</span>
        <span class="fs-09__tip" role="note">Certified since 2022, surveillance audit each year. Statement of applicability shared under NDA.</span>
      </li>
      <li class="fs-09__badge" tabindex="0">
        <span class="fs-09__bmark" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18"/></svg></span>
        <span class="fs-09__bname">PCI DSS</span>
        <span class="fs-09__tip" role="note">Level 1 service provider. Card data tokenised at the edge; we never store a PAN.</span>
      </li>
      <li class="fs-09__badge" tabindex="0">
        <span class="fs-09__bmark" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M4 20V8l8-4 8 4v12z"/><path d="M10 20v-6h4v6"/></svg></span>
        <span class="fs-09__bname">FedRAMP</span>
        <span class="fs-09__tip" role="note">Moderate baseline, agency-sponsored. In-process listing with the JAB; ATO letters available.</span>
      </li>
    </ul>

    <div class="fs-09__callouts">
      <article class="fs-09__callout">
        <h3 class="fs-09__ctitle"><span class="fs-09__cmark" aria-hidden="true"><svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="5" y="10" width="14" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg></span>Encryption you hold the keys to</h3>
        <p class="fs-09__cprose">TLS 1.3 in transit, AES-256 at rest, and per-field envelope encryption with keys in your own KMS. Rotate a key and historical rows re-wrap in the background.</p>
      </article>
      <article class="fs-09__callout">
        <h3 class="fs-09__ctitle"><span class="fs-09__cmark" aria-hidden="true"><svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="9" cy="9" r="4"/><path d="M15 20a6 6 0 0 0-12 0M15 7h6M18 4v6"/></svg></span>SSO, SAML and SCIM on every plan</h3>
        <p class="fs-09__cprose">Directory-driven access with group-to-role mapping. Deprovisioning propagates in under sixty seconds, and session revocation is immediate.</p>
      </article>
      <article class="fs-09__callout">
        <h3 class="fs-09__ctitle"><span class="fs-09__cmark" aria-hidden="true"><svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 4h14v16H5z"/><path d="M9 9h6M9 13h6M9 17h3"/></svg></span>Audit logs that survive an audit</h3>
        <p class="fs-09__cprose">Immutable entries with actor, resource and before-and-after state, streamed to your SIEM and retained for seven years on request.</p>
      </article>
    </div>
  </div>

  <div class="fs-09__below" aria-hidden="true">Trust centre · Sub-processors · Report a vulnerability</div>
</section>
```
## CSS
```css
.fs-09 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #1b1815;
  --bg: oklch(0.23 0.011 60);
  --card: #241f1b;
  --card: oklch(0.27 0.013 60);
  --ink: #f6f1ea;
  --ink: oklch(0.96 0.012 80);
  --muted: #a99b8b;
  --muted: oklch(0.71 0.024 75);
  --rule: #3a332c;
  --rule: oklch(0.35 0.014 65);
  --accent: #f0a92c;
  --accent: oklch(0.78 0.14 78);
  --badge-min: 150px;
  --dots: radial-gradient(circle at 1px 1px, rgba(246, 241, 234, 0.07) 1px, transparent 0);
  --font-display: "Rockwell", "Roboto Slab", "Bookman Old Style", Georgia, serif;
  background: var(--bg);
  background-image: var(--dots);
  background-size: 18px 18px;
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-09 *,
.fs-09 *::before,
.fs-09 *::after {
  box-sizing: border-box;
}

.fs-09__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
  justify-content: space-between;
  align-items: baseline;
  padding: 16px 20px;
  border-block-end: 1px solid var(--rule);
}

.fs-09__wordmark {
  font: 700 16px/1 var(--font-display);
  letter-spacing: 0.02em;
}

.fs-09__heronav {
  font-size: 12px;
  color: var(--muted);
}

.fs-09__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(28px, 5vw, 58px) 16px;
}

.fs-09__head {
  inline-size: 100%;
  max-inline-size: 66rem;
  min-inline-size: 0;
  margin: 0 0 26px;
}

.fs-09__eyebrow {
  margin: 0 0 12px;
  font: 700 10.5px/1 system-ui, sans-serif;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--accent);
}

.fs-09__heading {
  margin: 0 0 10px;
  max-inline-size: 28ch;
  font: 400 clamp(25px, 4.6vw, 39px)/1.12 var(--font-display);
  letter-spacing: -0.015em;
  text-wrap: balance;
}

.fs-09__sub {
  margin: 0;
  max-inline-size: 54ch;
  font-size: 14px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-09__badges {
  inline-size: 100%;
  max-inline-size: 66rem;
  min-inline-size: 0;
  margin: 0 0 clamp(22px, 4vw, 38px);
  padding: 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, var(--badge-min)), 1fr));
  gap: 10px;
}

.fs-09__badge {
  position: relative;
  min-inline-size: 0;
  display: grid;
  place-items: center;
  gap: 9px;
  padding: 18px 12px;
  text-align: center;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 4px;
  cursor: default;
}

.fs-09__badge:hover,
.fs-09__badge:focus-within,
.fs-09__badge:focus-visible {
  border-color: var(--accent);
}

.fs-09__badge:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fs-09__bmark {
  display: grid;
  place-items: center;
  inline-size: 40px;
  block-size: 40px;
  border-radius: 50%;
  color: var(--accent);
  border: 1px solid color-mix(in oklab, var(--accent) 40%, var(--rule));
}

.fs-09__bname {
  font: 700 12px/1.3 var(--font-display);
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.fs-09__tip {
  position: absolute;
  inset-block-end: calc(100% + 8px);
  inset-inline: -4px;
  z-index: 3;
  padding: 10px 12px;
  font: 400 12px/1.5 system-ui, sans-serif;
  text-align: start;
  color: var(--ink);
  background: #100e0c;
  background: color-mix(in oklab, var(--bg) 70%, black);
  border: 1px solid var(--accent);
  border-radius: 4px;
  opacity: 0;
  visibility: hidden;
  transform: translateY(4px);
  transition: opacity .16s ease, transform .16s ease, visibility .16s;
}

.fs-09__badge:hover .fs-09__tip,
.fs-09__badge:focus-within .fs-09__tip,
.fs-09__badge:focus-visible .fs-09__tip {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.fs-09__callouts {
  inline-size: 100%;
  max-inline-size: 66rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr));
  gap: 12px;
}

.fs-09__callout {
  min-inline-size: 0;
  padding: 18px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 4px;
  border-block-start: 2px solid var(--accent);
}

.fs-09__ctitle {
  display: grid;
  grid-template-columns: 26px minmax(0, 1fr);
  align-items: center;
  gap: 10px;
  margin: 0 0 10px;
  font: 400 16px/1.3 var(--font-display);
  letter-spacing: -0.01em;
}

.fs-09__cmark {
  display: grid;
  place-items: center;
  color: var(--accent);
}

.fs-09__cprose {
  margin: 0;
  font-size: 13.5px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-09__below {
  padding: 16px 20px;
  border-block-start: 1px solid var(--rule);
  font-size: 12px;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .fs-09__tip {
    transition: none;
  }
}

@media (prefers-color-scheme: light) {
  .fs-09 {
    --bg: #f7f3ec;
    --card: #fffdf9;
    --ink: #201b16;
    --muted: #6d6157;
    --rule: #ddd4c6;
    --accent: #9a5c05;
    --dots: radial-gradient(circle at 1px 1px, rgba(32, 27, 22, 0.08) 1px, transparent 0);
  }

  .fs-09__tip {
    background: #201b16;
    color: #fdf9f3;
  }
}

[data-theme="dark"] .fs-09 {
  --bg: #1b1815;
  --card: #241f1b;
  --ink: #f6f1ea;
  --muted: #a99b8b;
  --rule: #3a332c;
  --accent: #f0a92c;
  --dots: radial-gradient(circle at 1px 1px, rgba(246, 241, 234, 0.07) 1px, transparent 0);
}

[data-theme="dark"] .fs-09 .fs-09__tip {
  background: #100e0c;
  color: var(--ink);
}
```
