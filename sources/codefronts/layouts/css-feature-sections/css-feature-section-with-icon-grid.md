---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/css-feature-section-with-icon-grid/"
title: "Feature Section with Icon Grid Layout"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "The canonical icon grid, rebuilt: six cells in a 3x2 arrangement that reflows to 2x3 and then single file, each with a duotone inline SVG, a title and a…"
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Feature Section with Icon Grid Layout
Source: https://codefronts.com/layouts/css-feature-sections/css-feature-section-with-icon-grid/

The canonical icon grid, rebuilt: six cells in a 3x2 arrangement that reflows to 2x3 and then single file, each with a duotone inline SVG, a title and a two-line description. Duotone comes from one accent variable and an opacity layer inside the same SVG, so the whole grid retints from a single custom property and needs no icon font or sprite sheet.
## HTML
```html
<section class="fs-13" aria-labelledby="fs-13-heading">
  <div class="fs-13__hero" aria-hidden="true">
    <span class="fs-13__wordmark">Sundial</span>
    <span class="fs-13__heronav">Scheduling infrastructure</span>
  </div>

  <div class="fs-13__stage">
    <div class="fs-13__head">
      <p class="fs-13__eyebrow">Platform</p>
      <h2 class="fs-13__heading" id="fs-13-heading">Six things you would otherwise build twice</h2>
      <p class="fs-13__sub">Everything below ships on day one, on every plan.</p>
    </div>

    <ul class="fs-13__grid">
      <li class="fs-13__cell">
        <span class="fs-13__plate" aria-hidden="true">
          <svg viewBox="0 0 32 32" width="24" height="24"><path d="M4 8a4 4 0 0 1 4-4h16a4 4 0 0 1 4 4v16a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4z" fill="currentColor" opacity="0.22"/><path d="M11 4v5M21 4v5M4 13h24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        </span>
        <h3 class="fs-13__ctitle">Timezone maths you never write</h3>
        <p class="fs-13__cprose">Availability resolves in the attendee's zone, including the two weeks a year when the offsets disagree.</p>
      </li>
      <li class="fs-13__cell">
        <span class="fs-13__plate" aria-hidden="true">
          <svg viewBox="0 0 32 32" width="24" height="24"><circle cx="16" cy="16" r="12" fill="currentColor" opacity="0.22"/><path d="M16 9v7l5 3" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        </span>
        <h3 class="fs-13__ctitle">Buffers and travel time</h3>
        <p class="fs-13__cprose">Per-event padding, minimum notice and a daily cap, enforced before a slot is ever offered.</p>
      </li>
      <li class="fs-13__cell">
        <span class="fs-13__plate" aria-hidden="true">
          <svg viewBox="0 0 32 32" width="24" height="24"><path d="M6 6h20v14H6z" fill="currentColor" opacity="0.22"/><path d="M6 6h20v20l-6-6H6z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>
        </span>
        <h3 class="fs-13__ctitle">Reminders that reduce no-shows</h3>
        <p class="fs-13__cprose">Email and SMS sequences per event type, with reschedule links that survive a forwarded invite.</p>
      </li>
      <li class="fs-13__cell">
        <span class="fs-13__plate" aria-hidden="true">
          <svg viewBox="0 0 32 32" width="24" height="24"><circle cx="12" cy="12" r="6" fill="currentColor" opacity="0.22"/><path d="M22 26a10 10 0 0 0-20 0M22 8h8M26 4v8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        </span>
        <h3 class="fs-13__ctitle">Round-robin across a team</h3>
        <p class="fs-13__cprose">Distribute by load, territory or skill tag, with a manual override that logs who changed it.</p>
      </li>
      <li class="fs-13__cell">
        <span class="fs-13__plate" aria-hidden="true">
          <svg viewBox="0 0 32 32" width="24" height="24"><path d="M4 24 12 10l8 8 8-12v18z" fill="currentColor" opacity="0.22"/><path d="M4 24 12 10l8 8 8-12" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>
        </span>
        <h3 class="fs-13__ctitle">Booking analytics per link</h3>
        <p class="fs-13__cprose">Views, completions and drop-off by step, exportable to the warehouse on a schedule.</p>
      </li>
      <li class="fs-13__cell">
        <span class="fs-13__plate" aria-hidden="true">
          <svg viewBox="0 0 32 32" width="24" height="24"><path d="M16 4l10 5v8c0 6-4.5 9.5-10 11-5.5-1.5-10-5-10-11V9z" fill="currentColor" opacity="0.22"/><path d="M11.5 16.5 15 20l6-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
        <h3 class="fs-13__ctitle">Consent and retention controls</h3>
        <p class="fs-13__cprose">Regional storage, per-event retention windows and a deletion API your privacy team can point at.</p>
      </li>
    </ul>
  </div>

  <div class="fs-13__below" aria-hidden="true">Docs · API reference · Pricing</div>
</section>
```
## CSS
```css
.fs-13 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #f5f6f8;
  --page: oklch(0.968 0.004 265);
  --card: #ffffff;
  --ink: #15171d;
  --ink: oklch(0.22 0.009 275);
  --muted: #5a6070;
  --muted: oklch(0.49 0.016 272);
  --rule: #e0e3e9;
  --rule: oklch(0.9 0.007 265);
  --accent: #6d4df6;
  --accent: oklch(0.55 0.22 288);
  --gap: 18px;
  --font-display: "Inter Tight", "Geist", system-ui, -apple-system, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-13 *,
.fs-13 *::before,
.fs-13 *::after {
  box-sizing: border-box;
}

.fs-13__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
  justify-content: space-between;
  align-items: baseline;
  padding: 16px 22px;
  background: var(--card);
  border-block-end: 1px solid var(--rule);
}

.fs-13__wordmark {
  font: 700 15px/1 var(--font-display);
  letter-spacing: -0.03em;
}

.fs-13__heronav {
  font-size: 12px;
  color: var(--muted);
}

.fs-13__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(30px, 5.5vw, 66px) 18px;
}

.fs-13__head {
  inline-size: 100%;
  max-inline-size: 66rem;
  min-inline-size: 0;
  margin: 0 0 clamp(22px, 4vw, 38px);
}

.fs-13__eyebrow {
  margin: 0 0 12px;
  font: 650 10.5px/1 var(--font-display);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.fs-13__heading {
  margin: 0 0 10px;
  max-inline-size: 28ch;
  font: 650 clamp(26px, 4.8vw, 40px)/1.1 var(--font-display);
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.fs-13__sub {
  margin: 0;
  font-size: 14.5px;
  color: var(--muted);
}

.fs-13__grid {
  inline-size: 100%;
  max-inline-size: 66rem;
  min-inline-size: 0;
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr));
  gap: var(--gap);
}

.fs-13__cell {
  min-inline-size: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 22px 20px 24px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 14px;
  box-shadow: 0 1px 2px rgba(21, 23, 29, 0.04), 0 8px 22px -14px rgba(21, 23, 29, 0.22);
}

.fs-13__plate {
  display: grid;
  place-items: center;
  inline-size: 46px;
  block-size: 46px;
  border-radius: 13px;
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 12%, var(--card));
  box-shadow: inset 0 0 0 1px color-mix(in oklab, var(--accent) 24%, transparent);
  transition: transform .2s ease, background-color .2s ease;
}

.fs-13__cell:hover .fs-13__plate {
  transform: scale(1.06);
  background: color-mix(in oklab, var(--accent) 20%, var(--card));
}

.fs-13__ctitle {
  margin: 0;
  font: 650 16px/1.3 var(--font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.fs-13__cprose {
  margin: 0;
  max-inline-size: 40ch;
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-13__below {
  padding: 16px 22px;
  background: var(--card);
  border-block-start: 1px solid var(--rule);
  font-size: 12px;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .fs-13__plate {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .fs-13 {
    --page: #101218;
    --card: #171a22;
    --ink: #eef0f5;
    --muted: #99a0b2;
    --rule: #262a34;
    --accent: #a08cff;
  }

  .fs-13__cell {
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.4), 0 10px 26px -16px rgba(0, 0, 0, 0.8);
  }
}

[data-theme="dark"] .fs-13 {
  --page: #101218;
  --card: #171a22;
  --ink: #eef0f5;
  --muted: #99a0b2;
  --rule: #262a34;
  --accent: #a08cff;
}
```
