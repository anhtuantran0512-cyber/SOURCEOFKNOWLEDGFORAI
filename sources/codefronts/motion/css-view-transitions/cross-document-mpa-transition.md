---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/cross-document-mpa-transition/"
title: "Cross Document MPA Transition"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "The piece most developers do not know exists: a single at-rule, @view-transition { navigation: auto; }, shipped in the stylesheet of both pages, and…"
has_js: "false"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cross Document MPA Transition
Source: https://codefronts.com/motion/css-view-transitions/cross-document-mpa-transition/

The piece most developers do not know exists: a single at-rule, @view-transition { navigation: auto; }, shipped in the stylesheet of both pages, and same-origin navigations animate with no JavaScript at all. Static sites, Astro, Rails and Django get SPA-feeling page changes for free. The preview swaps two documents inside one browser frame with a pure-CSS switch, because a sandboxed frame cannot perform a real navigation.
## HTML
```html
<section class="vtr-02" aria-labelledby="vtr-02-heading">
  <fieldset class="vtr-02__theme">
    <legend class="vtr-02__themelegend">Theme</legend>
    <input class="vtr-02__themeinput" type="radio" name="vtr-02-theme" id="vtr-02-theme-auto" checked>
    <label class="vtr-02__themeopt" for="vtr-02-theme-auto">Auto</label>
    <input class="vtr-02__themeinput" type="radio" name="vtr-02-theme" id="vtr-02-theme-light">
    <label class="vtr-02__themeopt" for="vtr-02-theme-light">Light</label>
    <input class="vtr-02__themeinput" type="radio" name="vtr-02-theme" id="vtr-02-theme-dark">
    <label class="vtr-02__themeopt" for="vtr-02-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-02__stage">
    <header>
      <p class="vtr-02__kicker">Cross document · zero JavaScript</p>
      <h2 class="vtr-02__heading" id="vtr-02-heading">Two documents, one at-rule</h2>
      <p class="vtr-02__sub">Click the two filenames in the toolbar. The chrome persists, the document body changes — the shape of what the at-rule gives you for free.</p>
    </header>

    <pre class="vtr-02__rule"><code>@view-transition { navigation: auto; }   /* in the stylesheet both pages load */</code></pre>

    <div class="vtr-02__browser">
      <input class="vtr-02__radio" type="radio" name="vtr-02-page" id="vtr-02-a" checked>
      <input class="vtr-02__radio" type="radio" name="vtr-02-page" id="vtr-02-b">

      <div class="vtr-02__bar">
        <span class="vtr-02__dots" aria-hidden="true"><span></span><span></span><span></span></span>
        <span class="vtr-02__url" aria-hidden="true"><span>basalt.example / index.html</span><span>basalt.example / pricing.html</span></span>
        <span class="vtr-02__links">
          <label class="vtr-02__link" for="vtr-02-a">index.html</label>
          <label class="vtr-02__link" for="vtr-02-b">pricing.html</label>
        </span>
      </div>

      <div class="vtr-02__viewport">
        <article class="vtr-02__page vtr-02__page--a">
          <div class="vtr-02__body">
            <p class="vtr-02__docname">Document one · outgoing</p>
            <div class="vtr-02__hero"></div>
            <h3 class="vtr-02__title">Basalt ships static, feels dynamic</h3>
            <p class="vtr-02__copy">The old page is snapshotted before it unloads. Its stylesheet carries the rule, so the browser is allowed to take that snapshot.</p>
          </div>
        </article>

        <article class="vtr-02__page vtr-02__page--b">
          <div class="vtr-02__body">
            <p class="vtr-02__docname">Document two · incoming</p>
            <div class="vtr-02__hero"></div>
            <h3 class="vtr-02__title">Pricing that reads in one screen</h3>
            <p class="vtr-02__copy">The new page carries the rule too, so it accepts the transition and pairs any shared names with the snapshot it inherited.</p>
          </div>
        </article>
      </div>
    </div>

    <ul class="vtr-02__reqs">
      <li class="vtr-02__req">
        <svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M2 8.4l3.4 3.4L14 3.6" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>
        <span><strong>Same origin</strong><span>A navigation to another origin never transitions.</span></span>
      </li>
      <li class="vtr-02__req">
        <svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M2 8.4l3.4 3.4L14 3.6" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>
        <span><strong>Rule on both pages</strong><span>Outgoing and incoming documents each need it.</span></span>
      </li>
      <li class="vtr-02__req">
        <svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M2 8.4l3.4 3.4L14 3.6" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>
        <span><strong>No preventDefault</strong><span>A router that intercepts the click owns the navigation.</span></span>
      </li>
    </ul>

    <p class="vtr-02__note">Honest caveat: this preview runs in a sandboxed frame with an opaque origin, so a <em>real</em> cross-document navigation cannot happen here — the toolbar switch is a pure-CSS stand-in (<code>:has(:checked)</code> plus a crossfade) for the effect. Ship the at-rule in two same-origin pages and the browser drives the identical change itself, with no switch and no script.</p>
  </div>
</section>
```
## CSS
```css
.vtr-02 {
  --bg: #eef3fb;
  --surface: #ffffff;
  --chrome: #f4f7fd;
  --line: #d3ddee;
  --ink: #101a2c;
  --muted: #5b6a85;
  --accent: #1d4ed8;
  --accent-soft: #e3ecff;
  --font-display: system-ui, "Segoe UI", sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  color-scheme: light dark;
}

.vtr-02 *,
.vtr-02 *::before,
.vtr-02 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-02 {
    --bg: oklch(95.5% 0.018 254);
    --surface: oklch(100% 0 0);
    --chrome: oklch(97.5% 0.012 254);
    --line: oklch(88% 0.03 254);
    --ink: oklch(21% 0.045 262);
    --muted: oklch(52% 0.04 258);
    --accent: oklch(50% 0.2 265);
    --accent-soft: oklch(93.5% 0.04 262);
  }
}

@media (prefers-color-scheme: dark) {
  .vtr-02 {
    --bg: #0a1020;
    --surface: #121b30;
    --chrome: #16203a;
    --line: #26324f;
    --ink: #e8eefb;
    --muted: #93a3c2;
    --accent: #7ea2ff;
    --accent-soft: #1c2949;
  }
}

.vtr-02[data-theme="light"] {
  --bg: #eef3fb;
  --surface: #ffffff;
  --chrome: #f4f7fd;
  --line: #d3ddee;
  --ink: #101a2c;
  --muted: #5b6a85;
  --accent: #1d4ed8;
  --accent-soft: #e3ecff;
}

.vtr-02[data-theme="dark"] {
  --bg: #0a1020;
  --surface: #121b30;
  --chrome: #16203a;
  --line: #26324f;
  --ink: #e8eefb;
  --muted: #93a3c2;
  --accent: #7ea2ff;
  --accent-soft: #1c2949;
}

.vtr-02__stage {
  max-width: 66rem;
  margin: 0 auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.5rem);
  display: grid;
  gap: 1.5rem;
}

.vtr-02__kicker {
  margin: 0 0 0.4rem;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-02__heading {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.4rem, 4.4vw, 2.1rem);
  font-weight: 700;
  letter-spacing: -0.025em;
}

.vtr-02__sub {
  margin: 0.45rem 0 0;
  color: var(--muted);
  font-size: 0.92rem;
  max-width: 40rem;
}

.vtr-02__browser {
  border: 1px solid var(--line);
  border-radius: 0.65rem;
  background: var(--surface);
  overflow: hidden;
  min-inline-size: 0;
  box-shadow: 0 1px 2px rgba(16, 26, 44, 0.06), 0 8px 24px -18px rgba(16, 26, 44, 0.4);
}

.vtr-02__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  border: 0;
  clip-path: inset(50%);
  overflow: hidden;
}

.vtr-02__bar {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
  padding: 0.55rem 0.7rem;
  background: var(--chrome);
  border-bottom: 1px solid var(--line);
}

.vtr-02__links {
  display: flex;
  gap: 0.3rem;
}

.vtr-02__link {
  padding: 0.3rem 0.6rem;
  border-radius: 0.3rem;
  cursor: pointer;
  border: 1px solid transparent;
  color: var(--muted);
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.68rem;
  transition: color 0.15s, background 0.15s, border-color 0.15s;
}

.vtr-02__link:hover {
  color: var(--ink);
  background: var(--surface);
}

.vtr-02__browser:has(#vtr-02-a:checked) [for="vtr-02-a"],
.vtr-02__browser:has(#vtr-02-b:checked) [for="vtr-02-b"] {
  color: var(--accent);
  background: var(--accent-soft);
  border-color: var(--line);
}

.vtr-02__browser:has(#vtr-02-a:focus-visible) [for="vtr-02-a"],
.vtr-02__browser:has(#vtr-02-b:focus-visible) [for="vtr-02-b"] {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.vtr-02__dots {
  display: flex;
  gap: 0.3rem;
}

.vtr-02__dots span {
  width: 0.5rem;
  height: 0.5rem;
  border-radius: 999px;
  background: var(--line);
}

.vtr-02__url {
  flex: 1 1 12rem;
  min-inline-size: 0;
  display: grid;
  padding: 0.3rem 0.55rem;
  border-radius: 0.3rem;
  background: var(--surface);
  border: 1px solid var(--line);
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.68rem;
  color: var(--muted);
}

.vtr-02__url span {
  grid-area: 1 / 1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  opacity: 0;
  transition: opacity 0.28s ease;
}

.vtr-02__browser:has(#vtr-02-a:checked) .vtr-02__url span:first-child,
.vtr-02__browser:has(#vtr-02-b:checked) .vtr-02__url span:last-child {
  opacity: 1;
}

.vtr-02__viewport {
  display: grid;
}

.vtr-02__page {
  grid-area: 1 / 1;
  min-inline-size: 0;
  opacity: 0;
  visibility: hidden;
  transform: translateY(0.6rem) scale(0.99);
  transition: opacity 0.34s ease, transform 0.34s cubic-bezier(0.2, 0.7, 0.2, 1), visibility 0.34s;
}

.vtr-02__browser:has(#vtr-02-a:checked) .vtr-02__page--a,
.vtr-02__browser:has(#vtr-02-b:checked) .vtr-02__page--b {
  opacity: 1;
  visibility: visible;
  transform: none;
}

.vtr-02__body {
  padding: 1rem 1.1rem 1.25rem;
  display: grid;
  gap: 0.7rem;
}

.vtr-02__docname {
  margin: 0;
  font-size: 0.68rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}

.vtr-02__title {
  margin: 0;
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 700;
  letter-spacing: -0.015em;
}

.vtr-02__hero {
  height: 4.5rem;
  border-radius: 0.4rem;
  background: linear-gradient(120deg, #1d4ed8, #4f8dff 55%, #a6c4ff);
}

.vtr-02__page--b .vtr-02__hero {
  background: linear-gradient(120deg, #0f766e, #2dd4bf 60%, #a7f3d0);
}

.vtr-02__copy {
  margin: 0;
  font-size: 0.8rem;
  line-height: 1.55;
  color: var(--muted);
}

.vtr-02__rule {
  margin: 0;
  padding: 0.75rem 0.9rem;
  overflow-x: auto;
  border: 1px dashed var(--line);
  border-radius: 0.4rem;
  background: var(--accent-soft);
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.7rem;
  line-height: 1.6;
  color: var(--ink);
}

.vtr-02__reqs {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0.55rem;
  grid-template-columns: 1fr;
}

@media (min-width: 40rem) {
  .vtr-02__reqs {
    grid-template-columns: repeat(3, 1fr);
  }
}

.vtr-02__req {
  display: grid;
  grid-template-columns: 1.1rem 1fr;
  gap: 0.5rem;
  padding: 0.7rem 0.8rem;
  border-radius: 0.5rem;
  border: 1px solid var(--line);
  background: var(--surface);
  font-size: 0.78rem;
  line-height: 1.45;
  min-inline-size: 0;
}

.vtr-02__req svg {
  color: var(--accent);
  margin-top: 0.1rem;
}

.vtr-02__req strong {
  display: block;
  font-size: 0.78rem;
}

.vtr-02__req span {
  color: var(--muted);
}

.vtr-02__note {
  margin: 0;
  padding: 0.7rem 0.85rem;
  border-left: 2px solid var(--accent);
  background: var(--accent-soft);
  font-size: 0.78rem;
  line-height: 1.5;
  color: var(--ink);
}

@view-transition {
  navigation: auto;
}

@media (prefers-reduced-motion: reduce) {
  .vtr-02__page,
    .vtr-02__url span,
    .vtr-02__link {
    transition-duration: 1ms;
  }

  ::view-transition-group(*) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-02 {
  position: relative;
}

.vtr-02__theme {
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

.vtr-02__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-02__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-02__themeopt {
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

.vtr-02__themeopt:hover {
  opacity: 0.85;
}

.vtr-02__themeinput:checked + .vtr-02__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-02__themeinput:focus-visible + .vtr-02__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-02:has(#vtr-02-theme-light:checked) {
  --bg: #eef3fb;
  --surface: #ffffff;
  --chrome: #f4f7fd;
  --line: #d3ddee;
  --ink: #101a2c;
  --muted: #5b6a85;
  --accent: #1d4ed8;
  --accent-soft: #e3ecff;
}

.vtr-02:has(#vtr-02-theme-dark:checked) {
  --bg: #0a1020;
  --surface: #121b30;
  --chrome: #16203a;
  --line: #26324f;
  --ink: #e8eefb;
  --muted: #93a3c2;
  --accent: #7ea2ff;
  --accent-soft: #1c2949;
}
```
