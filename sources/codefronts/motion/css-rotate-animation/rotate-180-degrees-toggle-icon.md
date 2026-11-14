---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/rotate-180-degrees-toggle-icon/"
title: "Rotate 180 Degrees Toggle Icon"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "A disclosure chevron that turns exactly 180 degrees when its panel opens, driven by a checkbox and :has(:checked) with no JavaScript."
has_js: "false"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rotate 180 Degrees Toggle Icon
Source: https://codefronts.com/motion/css-rotate-animation/rotate-180-degrees-toggle-icon/

A disclosure chevron that turns exactly 180 degrees when its panel opens, driven by a checkbox and :has(:checked) with no JavaScript. Two details decide whether it feels mechanical or broken: transform-origin: center so the caret pivots in place instead of swinging out of its box, and a transition short enough — about 180ms — to read as a switch rather than a flourish.
## HTML
```html
<section class="rot-04" aria-labelledby="rot-04-h">
  <fieldset class="rot-04__theme">
    <legend class="rot-04__themelegend">Theme</legend>
    <input class="rot-04__themeinput" type="radio" name="rot-04-theme" id="rot-04-theme-auto" checked>
    <label class="rot-04__themeopt" for="rot-04-theme-auto">Auto</label>
    <input class="rot-04__themeinput" type="radio" name="rot-04-theme" id="rot-04-theme-light">
    <label class="rot-04__themeopt" for="rot-04-theme-light">Light</label>
    <input class="rot-04__themeinput" type="radio" name="rot-04-theme" id="rot-04-theme-dark">
    <label class="rot-04__themeopt" for="rot-04-theme-dark">Dark</label>
  </fieldset>

  <div class="rot-04__stage">
    <header class="rot-04__head">
      <p class="rot-04__eyebrow">Meridian · Deployment settings</p>
      <h2 class="rot-04__h" id="rot-04-h">One glyph, one angle, one origin</h2>
      <p class="rot-04__sub">Open a row. The caret turns 180 degrees about its own centre in 180 milliseconds — no script, no class toggle.</p>
    </header>

    <div class="rot-04__list">
      <div class="rot-04__row">
        <input class="rot-04__box" type="checkbox" id="rot-04-r1" checked>
        <label class="rot-04__trigger" for="rot-04-r1">
          <span class="rot-04__title">Build cache</span>
          <span class="rot-04__meta">Shared across branches</span>
          <span class="rot-04__chev" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M5 9.5 12 16l7-6.5" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"></path></svg>
          </span>
        </label>
        <div class="rot-04__panel">
          <div class="rot-04__panelinner">
            <p class="rot-04__p">Artifacts are keyed by lockfile hash and kept for fourteen days. A cold build on Ranger takes about four minutes; a warm one takes forty seconds.</p>
          </div>
        </div>
      </div>

      <div class="rot-04__row">
        <input class="rot-04__box" type="checkbox" id="rot-04-r2">
        <label class="rot-04__trigger" for="rot-04-r2">
          <span class="rot-04__title">Preview environments</span>
          <span class="rot-04__meta">One per pull request</span>
          <span class="rot-04__chev" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M5 9.5 12 16l7-6.5" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"></path></svg>
          </span>
        </label>
        <div class="rot-04__panel">
          <div class="rot-04__panelinner">
            <p class="rot-04__p">Each preview gets its own subdomain and a seeded database. Alex Chen owns the teardown job that reclaims them after seventy-two idle hours.</p>
          </div>
        </div>
      </div>

      <div class="rot-04__row">
        <input class="rot-04__box" type="checkbox" id="rot-04-r3">
        <label class="rot-04__trigger" for="rot-04-r3">
          <span class="rot-04__title">Rollback window</span>
          <span class="rot-04__meta">Instant for 30 minutes</span>
          <span class="rot-04__chev" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M5 9.5 12 16l7-6.5" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"></path></svg>
          </span>
        </label>
        <div class="rot-04__panel">
          <div class="rot-04__panelinner">
            <p class="rot-04__p">The previous release stays warm for half an hour after a deploy, so a rollback is a routing change rather than a rebuild.</p>
          </div>
        </div>
      </div>
    </div>

    <p class="rot-04__fine">Not a hamburger. A menu icon morphing into an X needs its bars translated and counter-rotated; a disclosure caret is one glyph flipped about <span class="rot-04__code">transform-origin: center</span>.</p>
  </div>
</section>
```
## CSS
```css
.rot-04 {
  --page: #eef3fb;
  --surface: #ffffff;
  --ink: #0b1b33;
  --muted: #5a6a85;
  --rule: #d5e0f0;
  --accent: #1b64d9;
  --flip: 180deg;
  --dur: 180ms;
  --radius: 0.625rem;
  --font-display: "Arial Narrow", "Helvetica Neue Condensed", "Liberation Sans Narrow", system-ui, sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(0 0 0)) {
  .rot-04 {
    --accent: oklch(0.53 0.19 260);
  }
}

.rot-04 *,
.rot-04 *::before,
.rot-04 *::after {
  box-sizing: border-box;
}

.rot-04__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.5rem, 4vw, 2.5rem);
  padding: clamp(1.25rem, 4vw, 3rem);
  padding-block-start: 5.25rem;
}

.rot-04__head {
  max-inline-size: 34rem;
  min-inline-size: 0;
  text-align: center;
}

.rot-04__eyebrow {
  margin: 0 0 0.6rem;
  font-family: var(--font-display);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-04__h {
  margin: 0 0 0.6rem;
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 5vw, 2.375rem);
  font-weight: 700;
  letter-spacing: 0.01em;
  text-transform: uppercase;
  line-height: 1.08;
}

.rot-04__sub {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-04__code {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.85em;
  padding: 0.1em 0.3em;
  border-radius: 0.25rem;
  background: color-mix(in srgb, var(--accent) 12%, transparent);
  color: var(--accent);
}

.rot-04__list {
  inline-size: min(100%, 34rem);
  display: grid;
  gap: 0.75rem;
}

.rot-04__row {
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  background: var(--surface);
  box-shadow: 0 3px 0 0 color-mix(in srgb, var(--ink) 10%, transparent);
  overflow: hidden;
}

.rot-04__box {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-04__trigger {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  align-items: center;
  gap: 0.15rem 1rem;
  min-block-size: 3.25rem;
  padding: 0.75rem 1rem;
  cursor: pointer;
  user-select: none;
}

.rot-04__title {
  grid-column: 1;
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  min-inline-size: 0;
}

.rot-04__meta {
  grid-column: 1;
  grid-row: 2;
  font-size: 0.75rem;
  color: var(--muted);
  min-inline-size: 0;
}

.rot-04__chev {
  grid-column: 2;
  grid-row: 1 / span 2;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  inline-size: 2.25rem;
  block-size: 2.25rem;
  border-radius: 50%;
  background: color-mix(in srgb, var(--accent) 10%, transparent);
  color: var(--accent);
  transform-origin: center;
  transition: transform var(--dur) cubic-bezier(0.3, 0.7, 0.3, 1), background-color var(--dur) linear;
}

.rot-04__panel {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows var(--dur) cubic-bezier(0.3, 0.7, 0.3, 1);
}

.rot-04__panelinner {
  overflow: hidden;
}

.rot-04__p {
  margin: 0;
  padding: 0 1rem 1rem;
  font-size: 0.875rem;
  line-height: 1.65;
  color: var(--muted);
  min-inline-size: 0;
}

.rot-04__row:has(.rot-04__box:checked) {
  border-color: color-mix(in srgb, var(--accent) 40%, var(--rule));
}

.rot-04__row:has(.rot-04__box:checked) .rot-04__chev {
  transform: rotate(var(--flip));
  background: var(--accent);
  color: var(--surface);
}

.rot-04__row:has(.rot-04__box:checked) .rot-04__panel {
  grid-template-rows: 1fr;
}

.rot-04__row:has(.rot-04__box:focus-visible) {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.rot-04__trigger:hover .rot-04__chev {
  background: color-mix(in srgb, var(--accent) 20%, transparent);
}

.rot-04__fine {
  inline-size: min(100%, 34rem);
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.7;
  color: var(--muted);
  text-align: center;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .rot-04__chev,
    .rot-04__panel {
    transition: none;
  }
}

.rot-04__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 8%, transparent);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: system-ui, sans-serif;
}

.rot-04__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-04__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-04__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: inherit;
  opacity: 0.55;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}

.rot-04__themeopt:hover {
  opacity: 0.85;
}

.rot-04__themeinput:checked + .rot-04__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-04__themeinput:focus-visible + .rot-04__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .rot-04__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-04__themeinput:checked + .rot-04__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: dark) {
  .rot-04:not(:has(#rot-04-theme-light:checked)) {
    --page: #060d1a;
    --surface: #0e1727;
    --ink: #e6edf9;
    --muted: #8d9db8;
    --rule: #1e2b42;
    --accent: #6aa6ff;
  }

  .rot-04:not(:has(#rot-04-theme-light:checked)) .rot-04__row {
    box-shadow: 0 3px 0 0 #0a1220;
  }

  .rot-04:not(:has(#rot-04-theme-light:checked)) .rot-04__row:has(.rot-04__box:checked) .rot-04__chev {
    color: #06101f;
  }
}

@media (prefers-color-scheme: light) {
  .rot-04:has(#rot-04-theme-dark:checked) {
    --page: #060d1a;
    --surface: #0e1727;
    --ink: #e6edf9;
    --muted: #8d9db8;
    --rule: #1e2b42;
    --accent: #6aa6ff;
  }
}

[data-theme="dark"] .rot-04:not(:has(#rot-04-theme-light:checked)) {
  --page: #060d1a;
  --surface: #0e1727;
  --ink: #e6edf9;
  --muted: #8d9db8;
  --rule: #1e2b42;
  --accent: #6aa6ff;
}

[data-theme="dark"] .rot-04:not(:has(#rot-04-theme-light:checked)) .rot-04__row:has(.rot-04__box:checked) .rot-04__chev {
  color: #06101f;
}

.rot-04:has(#rot-04-theme-dark:checked) {
  --page: #060d1a;
  --surface: #0e1727;
  --ink: #e6edf9;
  --muted: #8d9db8;
  --rule: #1e2b42;
  --accent: #6aa6ff;
}

.rot-04:has(#rot-04-theme-dark:checked) .rot-04__row {
  box-shadow: 0 3px 0 0 #0a1220;
}

.rot-04:has(#rot-04-theme-dark:checked) .rot-04__row:has(.rot-04__box:checked) .rot-04__chev {
  color: #06101f;
}

.rot-04:has(#rot-04-theme-light:checked) {
  --page: #eef3fb;
  --surface: #ffffff;
  --ink: #0b1b33;
  --muted: #5a6a85;
  --rule: #d5e0f0;
  --accent: #1b64d9;
}

.rot-04:has(#rot-04-theme-light:checked) .rot-04__row:has(.rot-04__box:checked) .rot-04__chev {
  color: #ffffff;
}
```
