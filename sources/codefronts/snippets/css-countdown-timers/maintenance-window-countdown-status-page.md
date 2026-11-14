---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/maintenance-window-countdown-status-page/"
title: "Maintenance Window Countdown Status Page"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "A scheduled-maintenance card that counts down to the window opening and then, at the moment it opens, flips to counting down to the window closing."
has_js: "false"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Maintenance Window Countdown Status Page
Source: https://codefronts.com/snippets/css-countdown-timers/maintenance-window-countdown-status-page/

A scheduled-maintenance card that counts down to the window opening and then, at the moment it opens, flips to counting down to the window closing. The affected-services list sits beside it with per-service impact, because during a window the only question anyone actually has is which parts still work.
## HTML
```html
<section class="cdt-14" aria-labelledby="cdt-14-title">
  <input class="cdt-14__tgl" type="checkbox" id="cdt-14-theme">
  <label class="cdt-14__tglbtn" for="cdt-14-theme">
    <svg class="cdt-14__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-14__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-14__darktext">Dark mode</span><span class="cdt-14__lighttext">Light mode</span>
  </label>
  <div class="cdt-14__stage">
    <header class="cdt-14__top">
      <p class="cdt-14__brand">Talon status</p>
      <span class="cdt-14__pill" data-level="scheduled">Scheduled maintenance</span>
    </header>

    <article class="cdt-14__card">
      <h2 class="cdt-14__title" id="cdt-14-title">Primary database failover · region eu-west</h2>
      <p class="cdt-14__meta">
        <time datetime="2026-08-22T01:00:00Z">Sat 22 Aug, 01:00 UTC</time> →
        <time datetime="2026-08-22T02:30:00Z">02:30 UTC</time> ·
        duration <time datetime="PT90M">90 minutes</time>
      </p>

      <div class="cdt-14__phases" role="timer" aria-label="Maintenance window countdown">
        <div class="cdt-14__phase">
          <p class="cdt-14__plabel">Window opens in</p>
          <p class="cdt-14__clock" aria-hidden="true"><em class="cdt-14__ah"></em><span>:</span><em class="cdt-14__amt"></em><em class="cdt-14__amu"></em><span>:</span><em class="cdt-14__ast"></em><em class="cdt-14__asu"></em></p>
          <p class="cdt-14__pfoot">Finish long-running exports before this reaches zero.</p>
        </div>
        <div class="cdt-14__phase cdt-14__phase2">
          <p class="cdt-14__plabel" data-live-phase>Window closes in</p>
          <p class="cdt-14__clock" aria-hidden="true"><em class="cdt-14__bh"></em><span>:</span><em class="cdt-14__bmt"></em><em class="cdt-14__bmu"></em><span>:</span><em class="cdt-14__bst"></em><em class="cdt-14__bsu"></em></p>
          <p class="cdt-14__pfoot">Failover in progress. Writes resume automatically when this reaches zero.</p>
        </div>
      </div>

      <dl class="cdt-14__svc">
        <div><dt>API · writes</dt><dd data-impact="down">Rejected with 503 for the full window</dd></div>
        <div><dt>API · reads</dt><dd data-impact="ok">Unaffected, served from replicas</dd></div>
        <div><dt>Dashboards</dt><dd data-impact="partial">Read-only, cached up to 5 minutes stale</dd></div>
        <div><dt>Scheduled exports</dt><dd data-impact="partial">Queued and replayed after the window</dd></div>
        <div><dt>Webhooks</dt><dd data-impact="partial">Retried with backoff for 24 hours</dd></div>
      </dl>

      <p class="cdt-14__foot">Posted by Jordan Lee · updates every 15 minutes during the window. Counters are CSS-only, so they measure from render; a live page seeds both remaining durations from the server.</p>
    </article>
  </div>
</section>
```
## CSS
```css
@property --cdt14-ah {
  syntax: '<integer>';
  inherits: false;
  initial-value: 1;
}

@property --cdt14-amt {
  syntax: '<integer>';
  inherits: false;
  initial-value: 1;
}

@property --cdt14-amu {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

@property --cdt14-ast {
  syntax: '<integer>';
  inherits: false;
  initial-value: 5;
}

@property --cdt14-asu {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

@property --cdt14-bh {
  syntax: '<integer>';
  inherits: false;
  initial-value: 1;
}

@property --cdt14-bmt {
  syntax: '<integer>';
  inherits: false;
  initial-value: 2;
}

@property --cdt14-bmu {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

@property --cdt14-bst {
  syntax: '<integer>';
  inherits: false;
  initial-value: 5;
}

@property --cdt14-bsu {
  syntax: '<integer>';
  inherits: false;
  initial-value: 9;
}

.cdt-14 {
  --page: #14120f;
  --surface-1: #1c1a16;
  --surface-2: #23201b;
  --ink: #f4f0e8;
  --muted: #a09889;
  --rule: #2e2a23;
  --accent: #f0a92c;
  --ok: #63c98a;
  --down: #f2705f;
  --mono: ui-monospace, "JetBrains Mono", "SFMono-Regular", Menlo, monospace;
  --font-display: "Geist", "Inter", ui-sans-serif, system-ui, sans-serif;
  --to-start: 4740s;
  --window: 5400s;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-display);
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-14 {
    --page: oklch(17% 0.012 70);
    --surface-1: oklch(21% 0.014 70);
    --surface-2: oklch(25% 0.016 70);
    --ink: oklch(95% 0.012 80);
    --muted: oklch(70% 0.02 78);
    --rule: oklch(30% 0.016 70);
    --accent: oklch(78% 0.14 72);
    --ok: oklch(78% 0.14 150);
    --down: oklch(70% 0.17 30);
  }
}

.cdt-14 *,
.cdt-14 *::before,
.cdt-14 *::after {
  box-sizing: border-box;
}

.cdt-14__stage {
  display: grid;
  gap: 14px;
  align-content: center;
  min-height: 100vh;
  max-inline-size: 780px;
  margin-inline: auto;
  padding: clamp(16px, 4vw, 48px);
}

.cdt-14__top {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 8px 14px;
}

.cdt-14__brand {
  margin: 0;
  font: 600 12px/1 var(--font-display);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-14__pill {
  padding: 5px 10px;
  border: 1px solid var(--accent);
  border-radius: 3px;
  font: 600 10.5px/1.4 var(--mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--accent);
}

.cdt-14__card {
  min-inline-size: 0;
  background: var(--surface-1);
  border: 1px solid var(--rule);
  border-radius: 6px;
}

.cdt-14__title {
  margin: 0;
  padding: clamp(16px, 3vw, 22px) clamp(16px, 3vw, 24px) 6px;
  font: 600 clamp(18px, 3.2vw, 24px)/1.25 var(--font-display);
  letter-spacing: -0.018em;
  text-wrap: balance;
}

.cdt-14__meta {
  margin: 0;
  padding: 0 clamp(16px, 3vw, 24px) clamp(14px, 3vw, 20px);
  border-block-end: 1px solid var(--rule);
  font: 400 12.5px/1.6 var(--mono);
  color: var(--muted);
  overflow-wrap: anywhere;
}

.cdt-14__phases {
  position: relative;
  padding: clamp(18px, 4vw, 26px) clamp(16px, 3vw, 24px);
  background: var(--surface-2);
  border-block-end: 1px solid var(--rule);
}

.cdt-14__plabel {
  margin: 0 0 8px;
  font: 600 10.5px/1 var(--font-display);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-14__clock {
  display: flex;
  align-items: baseline;
  margin: 0;
  font-variant-numeric: tabular-nums;
  color: var(--accent);
}

.cdt-14__clock em {
  font-style: normal;
  font: 500 clamp(38px, 11vw, 62px)/1 var(--mono);
  letter-spacing: -0.04em;
}

.cdt-14__clock span {
  font: 500 clamp(30px, 9vw, 50px)/1 var(--mono);
  opacity: 0.4;
}

.cdt-14__ah::before {
  content: counter(cdt14-ah);
  counter-reset: cdt14-ah var(--cdt14-ah);
}

.cdt-14__amt::before {
  content: counter(cdt14-amt);
  counter-reset: cdt14-amt var(--cdt14-amt);
}

.cdt-14__amu::before {
  content: counter(cdt14-amu);
  counter-reset: cdt14-amu var(--cdt14-amu);
}

.cdt-14__ast::before {
  content: counter(cdt14-ast);
  counter-reset: cdt14-ast var(--cdt14-ast);
}

.cdt-14__asu::before {
  content: counter(cdt14-asu);
  counter-reset: cdt14-asu var(--cdt14-asu);
}

.cdt-14__bh::before {
  content: counter(cdt14-bh);
  counter-reset: cdt14-bh var(--cdt14-bh);
}

.cdt-14__bmt::before {
  content: counter(cdt14-bmt);
  counter-reset: cdt14-bmt var(--cdt14-bmt);
}

.cdt-14__bmu::before {
  content: counter(cdt14-bmu);
  counter-reset: cdt14-bmu var(--cdt14-bmu);
}

.cdt-14__bst::before {
  content: counter(cdt14-bst);
  counter-reset: cdt14-bst var(--cdt14-bst);
}

.cdt-14__bsu::before {
  content: counter(cdt14-bsu);
  counter-reset: cdt14-bsu var(--cdt14-bsu);
}

.cdt-14__ah {
  animation: cdt14-ah var(--to-start) steps(2, end) forwards;
}

.cdt-14__amt {
  animation: cdt14-mt 3600s steps(6, end) infinite;
}

.cdt-14__amu {
  animation: cdt14-mu 600s steps(10, end) infinite;
}

.cdt-14__ast {
  animation: cdt14-st 60s steps(6, end) infinite;
}

.cdt-14__asu {
  animation: cdt14-su 10s steps(10, end) infinite;
}

.cdt-14__bh {
  animation: cdt14-bh var(--window) steps(2, end) var(--to-start) forwards;
}

.cdt-14__bmt {
  animation: cdt14-mt 3600s steps(6, end) var(--to-start) infinite;
}

.cdt-14__bmu {
  animation: cdt14-mu 600s steps(10, end) var(--to-start) infinite;
}

.cdt-14__bst {
  animation: cdt14-st 60s steps(6, end) var(--to-start) infinite;
}

.cdt-14__bsu {
  animation: cdt14-su 10s steps(10, end) var(--to-start) infinite;
}

@keyframes cdt14-ah {
  from {
    --cdt14-ah: 1;
  }

  to {
    --cdt14-ah: -1;
  }
}

@keyframes cdt14-bh {
  from {
    --cdt14-bh: 1;
  }

  to {
    --cdt14-bh: -1;
  }
}

@keyframes cdt14-mt {
  from {
    --cdt14-amt: 5;
    --cdt14-bmt: 5;
  }

  to {
    --cdt14-amt: -1;
    --cdt14-bmt: -1;
  }
}

@keyframes cdt14-mu {
  from {
    --cdt14-amu: 9;
    --cdt14-bmu: 9;
  }

  to {
    --cdt14-amu: 0;
    --cdt14-bmu: 0;
  }
}

@keyframes cdt14-st {
  from {
    --cdt14-ast: 5;
    --cdt14-bst: 5;
  }

  to {
    --cdt14-ast: 0;
    --cdt14-bst: 0;
  }
}

@keyframes cdt14-su {
  from {
    --cdt14-asu: 9;
    --cdt14-bsu: 9;
  }

  to {
    --cdt14-asu: 0;
    --cdt14-bsu: 0;
  }
}

.cdt-14__pfoot {
  margin: 12px 0 0;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-14__phase2 {
  position: absolute;
  inset: 0;
  padding: clamp(18px, 4vw, 26px) clamp(16px, 3vw, 24px);
  background: var(--surface-2);
  opacity: 0;
  visibility: hidden;
  animation: cdt14-flip 0.01s linear var(--to-start) forwards;
}

@keyframes cdt14-flip {
  from {
    opacity: 0;
    visibility: hidden;
  }

  to {
    opacity: 1;
    visibility: visible;
  }
}

.cdt-14__svc {
  display: grid;
  gap: 1px;
  margin: 0;
  background: var(--rule);
}

.cdt-14__svc > div {
  display: flex;
  flex-wrap: wrap;
  gap: 4px 14px;
  align-items: baseline;
  justify-content: space-between;
  padding: 11px clamp(16px, 3vw, 24px);
  background: var(--surface-1);
}

.cdt-14__svc dt {
  min-inline-size: 0;
  font: 500 12.5px/1.4 var(--mono);
}

.cdt-14__svc dd {
  min-inline-size: 0;
  margin: 0;
  font-size: 12.5px;
  line-height: 1.4;
  color: var(--muted);
  text-align: end;
}

.cdt-14__svc dd[data-impact="down"] {
  color: var(--down);
}

.cdt-14__svc dd[data-impact="ok"] {
  color: var(--ok);
}

.cdt-14__foot {
  margin: 0;
  padding: 13px clamp(16px, 3vw, 24px);
  border-block-start: 1px solid var(--rule);
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-14 {
  position: relative;
}

.cdt-14__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-14__tglbtn {
  position: absolute;
  inset-block-end: 14px;
  inset-inline-end: 14px;
  z-index: 20;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-block-size: 44px;
  min-inline-size: 44px;
  padding: 12px 14px;
  border: 1px solid currentColor;
  border-radius: 10px;
  background: transparent;
  color: inherit;
  font: 600 11px/1 system-ui, sans-serif;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  opacity: 0.62;
}

.cdt-14__tglbtn:hover {
  opacity: 1;
}

.cdt-14__tgl:focus-visible + .cdt-14__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-14__tglbtn svg {
  flex: none;
}

.cdt-14__moon,
.cdt-14__darktext {
  display: none;
}

.cdt-14:has(.cdt-14__tgl:checked) .cdt-14__sun,
.cdt-14:has(.cdt-14__tgl:checked) .cdt-14__lighttext {
  display: none;
}

.cdt-14:has(.cdt-14__tgl:checked) .cdt-14__moon {
  display: block;
}

.cdt-14:has(.cdt-14__tgl:checked) .cdt-14__darktext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-14__tglbtn {
    padding: 12px;
  }

  .cdt-14__darktext,
    .cdt-14__lighttext,
    .cdt-14:has(.cdt-14__tgl:checked) .cdt-14__darktext,
    .cdt-14:has(.cdt-14__tgl:checked) .cdt-14__lighttext {
    display: none;
  }
}
/* toggle in the system-dark case */

@media (prefers-color-scheme: dark) {
  .cdt-14:has(.cdt-14__tgl:checked) {
    --page: #f6f4f0;
    --surface-1: #ffffff;
    --surface-2: #f0ece4;
    --ink: #1a1712;
    --muted: #6c6559;
    --rule: #e2ddd2;
    --accent: #9a5f00;
    --ok: #1d7a44;
    --down: #c0352a;
  }
}

@media (prefers-color-scheme: light) {
  .cdt-14 {
    --page: #f6f4f0;
    --surface-1: #ffffff;
    --surface-2: #f0ece4;
    --ink: #1a1712;
    --muted: #6c6559;
    --rule: #e2ddd2;
    --accent: #9a5f00;
    --ok: #1d7a44;
    --down: #c0352a;
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-14:has(.cdt-14__tgl:checked) {
    --page: oklch(17% 0.012 70);
    --surface-1: oklch(21% 0.014 70);
    --surface-2: oklch(25% 0.016 70);
    --ink: oklch(95% 0.012 80);
    --muted: oklch(70% 0.02 78);
    --rule: oklch(30% 0.016 70);
    --accent: oklch(78% 0.14 72);
    --ok: oklch(78% 0.14 150);
    --down: oklch(70% 0.17 30);
  }
}

[data-theme="dark"] .cdt-14 {
  --page: #14120f;
  --surface-1: #1c1a16;
  --surface-2: #23201b;
  --ink: #f4f0e8;
  --muted: #a09889;
  --rule: #2e2a23;
  --accent: #f0a92c;
  --ok: #63c98a;
  --down: #f2705f;
}
```
