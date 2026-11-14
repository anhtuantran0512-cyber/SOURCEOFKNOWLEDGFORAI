---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/scroll-state-container-queries/"
title: "Scroll State Container Queries"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "container-type: scroll-state turns three previously script-only facts into CSS: whether an element is currently stuck, whether its scroll container can still…"
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll State Container Queries
Source: https://codefronts.com/layouts/css-container-queries/scroll-state-container-queries/

container-type: scroll-state turns three previously script-only facts into CSS: whether an element is currently stuck, whether its scroll container can still scroll, and whether a snap target is snapped. All three state families are shown annotated in one scroller, replacing the IntersectionObserver sentinel trick that was the only way to detect them for years.
## HTML
```html
<section class="cq-08" aria-labelledby="cq-08-h">
  <fieldset class="cq-08__theme">
    <legend class="cq-08__themelegend">Theme</legend>
    <input class="cq-08__themeinput" type="radio" name="cq-08-theme" id="cq-08-theme-auto" checked>
    <label class="cq-08__themeopt" for="cq-08-theme-auto">Auto</label>
    <input class="cq-08__themeinput" type="radio" name="cq-08-theme" id="cq-08-theme-light">
    <label class="cq-08__themeopt" for="cq-08-theme-light">Light</label>
    <input class="cq-08__themeinput" type="radio" name="cq-08-theme" id="cq-08-theme-dark">
    <label class="cq-08__themeopt" for="cq-08-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-08__stage">
    <header class="cq-08__head">
      <h2 class="cq-08__h" id="cq-08-h">Stuck, scrollable, snapped</h2>
      <p class="cq-08__lede">Scroll the panel. Every badge below is styled by a scroll-state query, not by a listener.</p>
      <p class="cq-08__gate">Static state shown &mdash; this engine has not shipped <code>container-type: scroll-state</code>.</p>
    </header>

    <div class="cq-08__scroller">
      <div class="cq-08__marker">
        <p class="cq-08__label"><span class="cq-08__off">stuck: top &mdash; not matched</span><span class="cq-08__on">stuck: top</span></p>
      </div>

      <section class="cq-08__snap" aria-label="Panel one">
        <span class="cq-08__chip"><span class="cq-08__off">snapped: y &mdash; no</span><span class="cq-08__on">snapped: y</span></span>
        <h3>Orbit release 4.2</h3>
        <p>Queue drains twice as fast under burst load; the retry budget is now per tenant.</p>
      </section>
      <section class="cq-08__snap" aria-label="Panel two">
        <span class="cq-08__chip"><span class="cq-08__off">snapped: y &mdash; no</span><span class="cq-08__on">snapped: y</span></span>
        <h3>Sable ingest limits</h3>
        <p>Batch size raised to sixteen thousand rows with the same p99 write latency.</p>
      </section>
      <section class="cq-08__snap" aria-label="Panel three">
        <span class="cq-08__chip"><span class="cq-08__off">snapped: y &mdash; no</span><span class="cq-08__on">snapped: y</span></span>
        <h3>Talon audit trail</h3>
        <p>Every mutation now carries the actor, the source and the prior value.</p>
      </section>

      <div class="cq-08__more">
        <span class="cq-08__morechip">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 9l6 6 6-6" stroke="currentColor" stroke-width="2.75" stroke-linecap="round" stroke-linejoin="round"/></svg>
          scrollable: bottom
        </span>
      </div>
    </div>

    <dl class="cq-08__legend">
      <div><dt>stuck</dt><dd>top / bottom / inline-start / inline-end &mdash; container must be <code>position: sticky</code></dd></div>
      <div><dt>scrollable</dt><dd>can the nearest scrollport still scroll that way</dd></div>
      <div><dt>snapped</dt><dd>x / y / block / inline &mdash; container must be a snap target</dd></div>
    </dl>
  </div>
</section>
```
## CSS
```css
.cq-08,
.cq-08[data-theme="light"] {
  --bg: #e8e6f2;
  --glass: rgba(255, 255, 255, 0.62);
  --surf: rgba(255, 255, 255, 0.78);
  --line: rgba(60, 50, 110, 0.16);
  --ink: #191430;
  --mut: #5b5480;
  --acc: #6d3ff0;
  --on: #0d0820;
}

.cq-08[data-theme="dark"] {
  --bg: #0b0918;
  --glass: rgba(30, 24, 56, 0.55);
  --surf: rgba(38, 30, 70, 0.6);
  --line: rgba(180, 165, 255, 0.18);
  --ink: #efeaff;
  --mut: #a99fd6;
  --acc: #a78bfa;
  --on: #0d0820;
}

@media (prefers-color-scheme: dark) {
  .cq-08:not([data-theme="light"]) {
    --bg: #0b0918;
    --glass: rgba(30, 24, 56, 0.55);
    --surf: rgba(38, 30, 70, 0.6);
    --line: rgba(180, 165, 255, 0.18);
    --ink: #efeaff;
    --mut: #a99fd6;
    --acc: #a78bfa;
    --on: #0d0820;
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-08,
    .cq-08[data-theme="light"] {
    --acc: oklch(0.5 0.24 292);
  }

  .cq-08[data-theme="dark"] {
    --acc: oklch(0.76 0.16 292);
  }

  @media (prefers-color-scheme: dark) {
    .cq-08:not([data-theme="light"]) {
      --acc: oklch(0.76 0.16 292);
    }
  }
}

.cq-08 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: radial-gradient(120% 80% at 15% 0%, color-mix(in srgb, var(--acc) 18%, var(--bg)), var(--bg) 60%);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.cq-08 *,
.cq-08 *::before,
.cq-08 *::after {
  box-sizing: border-box;
}

.cq-08__stage {
  max-width: 56rem;
  margin-inline: auto;
  padding: clamp(1rem, 3vw, 2.5rem);
  display: grid;
  gap: 1rem;
}

.cq-08__h {
  margin: 0;
  font-size: clamp(1.25rem, 1rem + 1.8vw, 1.8rem);
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.cq-08__lede {
  margin: 0.3rem 0 0;
  color: var(--mut);
  font-size: 0.85rem;
  max-width: 52ch;
}

.cq-08__gate {
  margin: 0.5rem 0 0;
  padding: 0.4rem 0.6rem;
  border-radius: 6px;
  border: 1px dashed var(--line);
  font-size: 0.72rem;
  color: var(--mut);
}

.cq-08__gate code {
  font-family: ui-monospace, Menlo, monospace;
}

@supports (container-type: scroll-state) {
  .cq-08__gate {
    display: none;
  }
}

.cq-08__scroller {
  block-size: 17rem;
  overflow-y: auto;
  scroll-snap-type: y proximity;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--glass);
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
  padding: 0 0.75rem 0.75rem;
}

.cq-08__marker {
  position: sticky;
  inset-block-start: 0;
  container-type: scroll-state;
  container-name: cq-08-stick;
  padding-block: 0.6rem;
  z-index: 2;
}

.cq-08__label {
  margin: 0;
  display: inline-flex;
  align-items: center;
  min-block-size: 2rem;
  padding: 0 0.7rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: var(--surf);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.72rem;
  letter-spacing: 0.04em;
  color: var(--mut);
}

.cq-08__on {
  display: none;
}

.cq-08__snap {
  container-type: scroll-state;
  container-name: cq-08-snap;
  scroll-snap-align: start;
  scroll-margin-block-start: 3.25rem;
  margin-block-end: 0.75rem;
  padding: 1rem;
  border-radius: 12px;
  border: 1px solid var(--line);
  background: var(--surf);
}

.cq-08__snap h3 {
  margin: 0.5rem 0 0.25rem;
  font-size: 1rem;
  font-weight: 650;
}

.cq-08__snap p {
  margin: 0;
  font-size: 0.83rem;
  color: var(--mut);
}

.cq-08__chip {
  display: inline-flex;
  align-items: center;
  min-block-size: 1.6rem;
  padding: 0 0.55rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.66rem;
  letter-spacing: 0.04em;
  color: var(--mut);
}

.cq-08__more {
  container-type: scroll-state;
  container-name: cq-08-scroll;
  position: sticky;
  inset-block-end: 0;
  display: flex;
  justify-content: center;
}

.cq-08__morechip {
  display: none;
  align-items: center;
  gap: 0.35rem;
  min-block-size: 1.9rem;
  padding: 0 0.7rem;
  border-radius: 999px;
  background: var(--acc);
  color: var(--on);
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.68rem;
  font-weight: 700;
}

.cq-08__morechip svg {
  inline-size: 0.9rem;
  block-size: 0.9rem;
}

@supports (container-type: scroll-state) {
  @container cq-08-stick scroll-state(stuck: top) {
    .cq-08__label {
      background: var(--acc);
      color: var(--on);
      border-color: transparent;
      font-weight: 700;
    }

    .cq-08__off {
      display: none;
    }

    .cq-08__on {
      display: inline;
    }
  }

  @container cq-08-snap scroll-state(snapped: y) {
    .cq-08__snap {
      border-color: var(--acc);
    }

    .cq-08__chip {
      background: var(--acc);
      color: var(--on);
      border-color: transparent;
      font-weight: 700;
    }

    .cq-08__chip .cq-08__off {
      display: none;
    }

    .cq-08__chip .cq-08__on {
      display: inline;
    }
  }

  @container cq-08-scroll scroll-state(scrollable: bottom) {
    .cq-08__morechip {
      display: inline-flex;
    }
  }
}

.cq-08__legend {
  margin: 0;
  display: grid;
  gap: 0.4rem;
  padding-top: 0.85rem;
  border-top: 1px solid var(--line);
  font-size: 0.76rem;
}

.cq-08__legend div {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  min-inline-size: 0;
}

.cq-08__legend dt {
  font-family: ui-monospace, Menlo, monospace;
  font-weight: 700;
  color: var(--acc);
  flex: none;
}

.cq-08__legend dd {
  margin: 0;
  color: var(--mut);
}

.cq-08__legend code {
  font-family: ui-monospace, Menlo, monospace;
}

@media (prefers-reduced-motion: reduce) {
  .cq-08__scroller {
    scroll-behavior: auto;
  }
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-08 {
  position: relative;
}

.cq-08__theme {
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

.cq-08__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-08__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-08__themeopt {
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

.cq-08__themeopt:hover {
  opacity: 0.85;
}

.cq-08__themeinput:checked + .cq-08__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-08__themeinput:focus-visible + .cq-08__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-08:has(#cq-08-theme-light:checked) {
  --bg: #e8e6f2;
  --glass: rgba(255, 255, 255, 0.62);
  --surf: rgba(255, 255, 255, 0.78);
  --line: rgba(60, 50, 110, 0.16);
  --ink: #191430;
  --mut: #5b5480;
  --acc: #6d3ff0;
  --on: #0d0820;
}

.cq-08:has(#cq-08-theme-dark:checked) {
  --bg: #0b0918;
  --glass: rgba(30, 24, 56, 0.55);
  --surf: rgba(38, 30, 70, 0.6);
  --line: rgba(180, 165, 255, 0.18);
  --ink: #efeaff;
  --mut: #a99fd6;
  --acc: #a78bfa;
  --on: #0d0820;
}
```
