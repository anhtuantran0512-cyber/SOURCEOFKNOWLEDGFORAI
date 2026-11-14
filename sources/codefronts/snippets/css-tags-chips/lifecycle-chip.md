---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/lifecycle-chip/"
title: "Process State Workflow Badge CSS"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "The badge system every CI, deployment and order-tracking screen needs: one component, five states — queued, running, success, failed, blocked — driven…"
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Process State Workflow Badge CSS
Source: https://codefronts.com/snippets/css-tags-chips/lifecycle-chip/

The badge system every CI, deployment and order-tracking screen needs: one component, five states — queued, running, success, failed, blocked — driven entirely by a data-state attribute. Each state pairs its color with unique geometry (hollow dot, conic spinner, drawn check, ×, dash) so the system survives color-blindness and grayscale printing; the running spinner is a conic gradient in a masked ring, the check strokes itself in via an SVG dash animation, and a pipeline table plus a step tracker show both halves of the pattern working.
## HTML
```html
<section class="ctc-24" aria-label="Workflow state badge demo">
  <div class="ctc-24__stage">
    <div class="ctc-24__wrap">
      <header class="ctc-24__head">
        <p class="ctc-24__kicker">Workflow badges · one attribute, five geometries</p>
        <h1>Readable in grayscale, bindable in one line</h1>
      </header>
      <div class="ctc-24__panel">
        <p class="ctc-24__lab">01 · The five states — distinct silhouette per state, not just color</p>
        <div class="ctc-24__row">
          <span class="ctc-24__badge" data-state="queued"><i></i>Queued</span>
          <span class="ctc-24__badge" data-state="running"><i></i>Running</span>
          <span class="ctc-24__badge" data-state="success"><i><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5 6.5 12 13 4.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></i>Success</span>
          <span class="ctc-24__badge" data-state="failed"><i></i>Failed</span>
          <span class="ctc-24__badge" data-state="blocked"><i></i>Blocked</span>
        </div>
      </div>
      <div class="ctc-24__panel">
        <p class="ctc-24__lab">02 · Pipeline — set data-state from your job payload, done</p>
        <ul class="ctc-24__table">
          <li><code>#2481</code><b>deploy · production</b><span class="ctc-24__badge ctc-24__badge--sm" data-state="running"><i></i>Running</span><time>1m 12s</time></li>
          <li><code>#2480</code><b>build · main</b><span class="ctc-24__badge ctc-24__badge--sm" data-state="success"><i><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5 6.5 12 13 4.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></i>Success</span><time>4m 03s</time></li>
          <li><code>#2479</code><b>e2e · pr-1142</b><span class="ctc-24__badge ctc-24__badge--sm" data-state="failed"><i></i>Failed</span><time>2m 44s</time></li>
          <li><code>#2478</code><b>deploy · staging</b><span class="ctc-24__badge ctc-24__badge--sm" data-state="blocked"><i></i>Blocked</span><time>—</time></li>
          <li><code>#2477</code><b>build · pr-1141</b><span class="ctc-24__badge ctc-24__badge--sm" data-state="queued"><i></i>Queued</span><time>—</time></li>
        </ul>
      </div>
      <div class="ctc-24__panel">
        <p class="ctc-24__lab">03 · Step tracker — same badges, connectors inherit the state above</p>
        <ol class="ctc-24__steps">
          <li data-state="success"><span class="ctc-24__badge ctc-24__badge--dot" data-state="success"><i><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5 6.5 12 13 4.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></i></span><div><b>Order confirmed</b><small>Jul 31, 14:20</small></div></li>
          <li data-state="success"><span class="ctc-24__badge ctc-24__badge--dot" data-state="success"><i><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5 6.5 12 13 4.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></i></span><div><b>Packed</b><small>Aug 1, 09:05</small></div></li>
          <li data-state="running"><span class="ctc-24__badge ctc-24__badge--dot" data-state="running"><i></i></span><div><b>In transit</b><small>Left Sydney facility</small></div></li>
          <li data-state="queued"><span class="ctc-24__badge ctc-24__badge--dot" data-state="queued"><i></i></span><div><b>Delivery</b><small>Estimated Aug 4</small></div></li>
        </ol>
      </div>
      <p class="ctc-24__note">Five states, five silhouettes — ring, spinner, check, ×, dash — so the system survives grayscale. The spinner rotates the <em>element</em>; rotating the gradient itself would need <code>@property</code>.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-24,
.ctc-24 *,
.ctc-24 *::before,
.ctc-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-24 {
  --bg: oklch(0.2 0.018 270);
  --panel: oklch(0.24 0.02 270);
  --ink: oklch(0.95 0.008 270);
  --mut: oklch(0.64 0.02 270);
  --line: oklch(0.325 0.022 270);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-24__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 55cqi at 85% -10%,oklch(0.3 0.06 250/.5),transparent 62%),var(--bg);
  container: ctc24/inline-size;
}

.ctc-24__wrap {
  width: min(640px,100%);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ctc-24__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.72 0.14 250);
}

.ctc-24__head h1 {
  font-size: clamp(22px,3.5cqi,34px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin: 8px 0 8px;
}

.ctc-24__panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 16px 18px;
}

.ctc-24__lab {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 14px;
}

.ctc-24__row {
  display: flex;
  flex-wrap: wrap;
  gap: 11px;
}

.ctc-24__badge {
  --c: oklch(0.7 0.02 270);
  --s: 1;
  display: inline-flex;
  align-items: center;
  gap: calc(8px*var(--s));
  min-height: calc(40px*var(--s));
  padding: 0 calc(15px*var(--s));
  border-radius: 99px;
  font-size: calc(12.5px*var(--s));
  font-weight: 750;
  letter-spacing: .02em;
  color: var(--c);
  background: color-mix(in oklch,var(--c) 12%,transparent);
  border: 1px solid color-mix(in oklch,var(--c) 32%,transparent);
}

.ctc-24__badge i {
  position: relative;
  flex: none;
  width: calc(14px*var(--s));
  height: calc(14px*var(--s));
  display: grid;
  place-items: center;
}

.ctc-24__badge svg {
  width: 100%;
  height: 100%;
}

.ctc-24__badge[data-state="queued"] {
  --c: oklch(0.7 0.02 270);
}

.ctc-24__badge[data-state="queued"] i::before {
  content: "";
  position: absolute;
  inset: 1px;
  border-radius: 50%;
  border: 2px solid currentColor;
  opacity: .75;
}

.ctc-24__badge[data-state="running"] {
  --c: oklch(0.72 0.15 250);
}

.ctc-24__badge[data-state="running"] i::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  padding: 2.2px;
  background: conic-gradient(transparent 12%,currentColor);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  animation: ctc24-spin .9s linear infinite;
}

@keyframes ctc24-spin {
  to {
    rotate: 360deg;
  }
}

.ctc-24__badge[data-state="success"] {
  --c: oklch(0.72 0.16 150);
}

.ctc-24__badge[data-state="success"] svg path {
  stroke-dasharray: 26;
  stroke-dashoffset: 26;
  animation: ctc24-draw .5s ease-out .1s forwards;
}

@keyframes ctc24-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.ctc-24__badge[data-state="failed"] {
  --c: oklch(0.68 0.19 25);
}

.ctc-24__badge[data-state="failed"] i::before,
.ctc-24__badge[data-state="failed"] i::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 75%;
  height: 2.2px;
  border-radius: 2px;
  background: currentColor;
  translate: -50% -50%;
}

.ctc-24__badge[data-state="failed"] i::before {
  rotate: 45deg;
}

.ctc-24__badge[data-state="failed"] i::after {
  rotate: -45deg;
}

.ctc-24__badge[data-state="blocked"] {
  --c: oklch(0.78 0.13 85);
}

.ctc-24__badge[data-state="blocked"] i::before {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 70%;
  height: 2.4px;
  border-radius: 2px;
  background: currentColor;
  translate: -50% -50%;
}

.ctc-24__badge--sm {
  --s: .82;
}

.ctc-24__badge--dot {
  --s: 1;
  min-height: 36px;
  width: 36px;
  padding: 0;
  justify-content: center;
  border-radius: 50%;
}

.ctc-24__table {
  list-style: none;
  display: flex;
  flex-direction: column;
}

.ctc-24__table li {
  display: grid;
  grid-template-columns: auto 1fr auto auto;
  align-items: center;
  gap: 13px;
  padding: 10px 10px;
  border-radius: 10px;
  transition: background .18s;
}

.ctc-24__table li:hover {
  background: oklch(1 0 0/.05);
}

.ctc-24__table code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  color: var(--mut);
}

.ctc-24__table b {
  font-size: 13px;
  font-weight: 650;
}

.ctc-24__table time {
  font-size: 11.5px;
  color: var(--mut);
  font-variant-numeric: tabular-nums;
  min-width: 56px;
  text-align: right;
}

.ctc-24__steps {
  list-style: none;
  display: flex;
  flex-direction: column;
}

.ctc-24__steps li {
  position: relative;
  display: flex;
  gap: 14px;
  padding-bottom: 22px;
}

.ctc-24__steps li:last-child {
  padding-bottom: 0;
}

.ctc-24__steps li::before {
  content: "";
  position: absolute;
  left: 17.5px;
  top: 38px;
  bottom: 2px;
  width: 2px;
  border-radius: 2px;
  background: var(--line);
}

.ctc-24__steps li:last-child::before {
  display: none;
}

.ctc-24__steps li[data-state="success"]::before {
  background: color-mix(in oklch,oklch(0.72 0.16 150) 55%,transparent);
}

.ctc-24__steps li[data-state="running"]::before {
  background: linear-gradient(oklch(0.72 0.15 250/.55),var(--line));
}

.ctc-24__steps b {
  display: block;
  font-size: 13.5px;
  font-weight: 750;
  padding-top: 2px;
}

.ctc-24__steps small {
  font-size: 11.5px;
  color: var(--mut);
}

.ctc-24__note {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  border-left: 3px solid oklch(0.72 0.14 250);
  padding-left: 12px;
}

.ctc-24__note code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: oklch(1 0 0/.09);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

@container ctc24 (width < 500px) {
  .ctc-24__table li {
    grid-template-columns: 1fr auto;
  }

  .ctc-24__table code,
    .ctc-24__table time {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ctc-24__badge[data-state="running"] i::before {
    animation-duration: 2.5s;
  }

  .ctc-24__badge[data-state="success"] svg path {
    animation: none;
    stroke-dashoffset: 0;
  }
}
```
