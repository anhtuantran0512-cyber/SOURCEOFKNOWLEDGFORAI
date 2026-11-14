---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/audit-log-activity/"
title: "Audit Log Activity Page"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "An enterprise-grade audit log with zero JavaScript: category filter chips (Auth, Members, Billing, API) powered by :has(), events grouped by day, each row…"
has_js: "false"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Audit Log Activity Page
Source: https://codefronts.com/layouts/css-settings-pages/audit-log-activity/

An enterprise-grade audit log with zero JavaScript: category filter chips (Auth, Members, Billing, API) powered by :has(), events grouped by day, each row showing actor, action, target, IP and time, severity markers for risky events, and expandable rows built on native <details> that reveal full metadata and a before/after diff. A CSS counter prints the number of matching events live as you filter.
## HTML
```html
<section class="csp-16">
  <div class="csp-16__wrap">
    <header class="csp-16__head"><div><h1>Audit log</h1><p>A tamper-evident record of security and admin activity. Retained for 365 days on Business.</p></div></header>

    <fieldset class="csp-16__chips">
      <legend class="csp-16__sr">Filter by category</legend>
      <input type="radio" name="csp16-c" id="csp16-all" checked><label for="csp16-all">All events</label>
      <input type="radio" name="csp16-c" id="csp16-auth"><label for="csp16-auth">Authentication</label>
      <input type="radio" name="csp16-c" id="csp16-members"><label for="csp16-members">Members</label>
      <input type="radio" name="csp16-c" id="csp16-billing"><label for="csp16-billing">Billing</label>
      <input type="radio" name="csp16-c" id="csp16-api"><label for="csp16-api">API</label>
    </fieldset>

    <div class="csp-16__log">
      <div class="csp-16__day">
        <h2>Today</h2>
        <details class="csp-16__ev" data-cat="members" data-sev="high">
          <summary><span class="csp-16__av" style="--h:265">AM</span><span class="csp-16__what"><b>Ava Mitchell</b> changed role of <b>Jordan Lee</b> from Member to <b>Admin</b></span><span class="csp-16__cat">Members</span><time datetime="2026-10-07T14:32Z">14:32</time></summary>
          <div class="csp-16__body"><dl><div><dt>Event</dt><dd>member.role_updated</dd></div><div><dt>IP address</dt><dd>73.162.xx.xx · San Francisco, US</dd></div><div><dt>User agent</dt><dd>Chrome 129 · macOS</dd></div><div><dt>Request ID</dt><dd>req_8Fq2LmZ0</dd></div></dl><pre class="csp-16__diff"><span class="del">- role: "member"</span>
<span class="add">+ role: "admin"</span></pre></div>
        </details>
        <details class="csp-16__ev" data-cat="api">
          <summary><span class="csp-16__av" style="--h:150">JL</span><span class="csp-16__what"><b>Jordan Lee</b> created API key <b>Billing worker</b></span><span class="csp-16__cat">API</span><time datetime="2026-10-07T11:05Z">11:05</time></summary>
          <div class="csp-16__body"><dl><div><dt>Event</dt><dd>api_key.created</dd></div><div><dt>Scope</dt><dd>Restricted · invoices:read</dd></div><div><dt>IP address</dt><dd>81.2.xx.xx · London, UK</dd></div></dl></div>
        </details>
        <details class="csp-16__ev" data-cat="auth" data-sev="high">
          <summary><span class="csp-16__av csp-16__av--sys">!</span><span class="csp-16__what">Sign-in blocked for <b>[email protected]</b> — 5 failed attempts</span><span class="csp-16__cat">Auth</span><time datetime="2026-10-07T03:47Z">03:47</time></summary>
          <div class="csp-16__body"><dl><div><dt>Event</dt><dd>auth.lockout</dd></div><div><dt>IP address</dt><dd>185.220.xx.xx · Frankfurt, DE</dd></div><div><dt>Action taken</dt><dd>Account locked 30 min · owner notified</dd></div></dl></div>
        </details>
      </div>
      <div class="csp-16__day">
        <h2>Yesterday</h2>
        <details class="csp-16__ev" data-cat="billing">
          <summary><span class="csp-16__av" style="--h:265">AM</span><span class="csp-16__what"><b>Ava Mitchell</b> added 2 seats to the <b>Pro</b> plan</span><span class="csp-16__cat">Billing</span><time datetime="2026-10-06T16:20Z">16:20</time></summary>
          <div class="csp-16__body"><dl><div><dt>Event</dt><dd>subscription.updated</dd></div><div><dt>Prorated charge</dt><dd>$27.20</dd></div></dl><pre class="csp-16__diff"><span class="del">- seats: 6</span>
<span class="add">+ seats: 8</span></pre></div>
        </details>
        <details class="csp-16__ev" data-cat="auth">
          <summary><span class="csp-16__av" style="--h:330">PR</span><span class="csp-16__what"><b>Priya Raman</b> enabled two-factor authentication</span><span class="csp-16__cat">Auth</span><time datetime="2026-10-06T09:12Z">09:12</time></summary>
          <div class="csp-16__body"><dl><div><dt>Event</dt><dd>auth.mfa_enabled</dd></div><div><dt>Method</dt><dd>Authenticator app (TOTP)</dd></div></dl></div>
        </details>
        <details class="csp-16__ev" data-cat="members">
          <summary><span class="csp-16__av" style="--h:200">JL</span><span class="csp-16__what"><b>Jordan Lee</b> invited <b>[email protected]</b> as Member</span><span class="csp-16__cat">Members</span><time datetime="2026-10-06T08:41Z">08:41</time></summary>
          <div class="csp-16__body"><dl><div><dt>Event</dt><dd>member.invited</dd></div><div><dt>Expires</dt><dd>Oct 13, 2026</dd></div></dl></div>
        </details>
      </div>
      <p class="csp-16__total"> matching · times shown in UTC</p>
    </div>
  </div>
</section>
```
## CSS
```css
.csp-16,
.csp-16 *,
.csp-16 *::before,
.csp-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-16 {
  --bg: oklch(0.15 0.012 265);
  --surface: oklch(0.19 0.014 265);
  --raised: oklch(0.225 0.016 265);
  --text: oklch(0.95 0.006 265);
  --muted: oklch(0.7 0.015 265);
  --line: oklch(0.29 0.016 265);
  --accent: oklch(0.75 0.13 255);
  --bad: oklch(0.7 0.18 25);
  --ok: oklch(0.78 0.15 155);
  color-scheme: dark;
  container-type: inline-size;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 40px 22px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--text);
  width: 100%;
}

.csp-16__sr {
  position: absolute!important;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.csp-16__wrap {
  max-width: 900px;
  margin-inline: auto;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.csp-16__head h1 {
  font: 700 30px/1.1 system-ui,sans-serif;
  letter-spacing: -.025em;
}

.csp-16__head p {
  font: 400 14.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 6px;
}

.csp-16__chips {
  border: 0;
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.csp-16__chips input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.csp-16__chips label {
  min-height: 38px;
  display: grid;
  place-items: center;
  padding: 0 15px;
  border: 1px solid var(--line);
  border-radius: 999px;
  font: 600 13px/1 system-ui,sans-serif;
  color: var(--muted);
  cursor: pointer;
  transition: all .15s;
}

.csp-16__chips label:hover {
  color: var(--text);
  border-color: oklch(0.4 0.02 265);
}

.csp-16__chips input:checked+label {
  color: oklch(0.18 0.03 255);
  background: var(--accent);
  border-color: transparent;
}

.csp-16__chips input:focus-visible+label {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-16__log {
  counter-reset: csp16;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.csp-16__day {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.csp-16__day h2 {
  position: sticky;
  top: 0;
  z-index: 1;
  padding: 6px 0;
  font: 600 11.5px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
  background: var(--bg);
}

.csp-16__ev {
  counter-increment: csp16;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  transition: background .2s,border-color .2s;
}

.csp-16__ev[open] {
  background: var(--raised);
  border-color: oklch(0.38 0.03 265);
}

.csp-16__ev[data-sev="high"] {
  box-shadow: inset 3px 0 0 var(--bad);
}

.csp-16__ev summary {
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto auto 18px;
  align-items: center;
  gap: 12px;
  min-height: 60px;
  padding: 10px 16px;
  cursor: pointer;
  list-style: none;
  border-radius: 14px;
}

.csp-16__ev summary::-webkit-details-marker {
  display: none;
}

.csp-16__ev summary::after {
  content: "";
  width: 8px;
  height: 8px;
  border: solid var(--muted);
  border-width: 0 1.6px 1.6px 0;
  rotate: 45deg;
  translate: 0 -2px;
  transition: rotate .2s;
}

.csp-16__ev[open] summary::after {
  rotate: 225deg;
  translate: 0 2px;
}

.csp-16__ev summary:hover {
  background: oklch(1 0 0/.025);
}

.csp-16__ev summary:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.csp-16__av {
  display: grid;
  place-items: center;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  font: 650 12px/1 system-ui,sans-serif;
  color: oklch(0.9 0.06 var(--h));
  background: oklch(0.35 0.08 var(--h));
}

.csp-16__av--sys {
  color: var(--bad);
  background: oklch(0.7 0.18 25/.15);
  font-size: 15px;
}

.csp-16__what {
  font: 400 14px/1.45 system-ui,sans-serif;
  color: var(--muted);
  text-wrap: pretty;
}

.csp-16__what b {
  color: var(--text);
  font-weight: 600;
}

.csp-16__cat {
  padding: 4px 9px;
  border-radius: 6px;
  font: 600 11px/1 system-ui,sans-serif;
  color: var(--muted);
  background: oklch(1 0 0/.06);
  white-space: nowrap;
}

.csp-16__ev time {
  font: 500 12.5px/1 ui-monospace,Menlo,monospace;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.csp-16__body {
  display: flex;
  flex-direction: column;
  gap: 14px;
  padding: 4px 16px 18px 62px;
  animation: csp16-in .25s ease;
}

.csp-16__body dl {
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(200px,1fr));
  gap: 12px;
}

.csp-16__body dt {
  font: 600 11px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 5px;
}

.csp-16__body dd {
  font: 500 13px/1.35 ui-monospace,Menlo,monospace;
  color: var(--text);
  word-break: break-word;
}

.csp-16__diff {
  padding: 12px 14px;
  border-radius: 10px;
  background: var(--bg);
  border: 1px solid var(--line);
  font: 500 12.5px/1.7 ui-monospace,Menlo,monospace;
  overflow-x: auto;
}

.csp-16__diff .del {
  display: block;
  color: oklch(0.78 0.13 25);
  background: oklch(0.7 0.18 25/.1);
  margin-inline: -14px;
  padding-inline: 14px;
}

.csp-16__diff .add {
  display: block;
  color: var(--ok);
  background: oklch(0.78 0.15 155/.1);
  margin-inline: -14px;
  padding-inline: 14px;
}

.csp-16__total {
  font: 500 12.5px/1.4 system-ui,sans-serif;
  color: var(--muted);
}

.csp-16__total::before {
  content: counter(csp16) " events";
  color: var(--text);
  font-weight: 650;
}

.csp-16:has(#csp16-auth:checked) .csp-16__ev:not([data-cat="auth"]),
.csp-16:has(#csp16-members:checked) .csp-16__ev:not([data-cat="members"]),
.csp-16:has(#csp16-billing:checked) .csp-16__ev:not([data-cat="billing"]),
.csp-16:has(#csp16-api:checked) .csp-16__ev:not([data-cat="api"]) {
  display: none;
}

.csp-16:has(#csp16-auth:checked) .csp-16__day:not(:has([data-cat="auth"])),
.csp-16:has(#csp16-members:checked) .csp-16__day:not(:has([data-cat="members"])),
.csp-16:has(#csp16-billing:checked) .csp-16__day:not(:has([data-cat="billing"])),
.csp-16:has(#csp16-api:checked) .csp-16__day:not(:has([data-cat="api"])) {
  display: none;
}

@keyframes csp16-in {
  from {
    opacity: 0;
    translate: 0 -4px;
  }
}

@container (max-width: 620px) {
  .csp-16__ev summary {
    grid-template-columns: auto minmax(0,1fr) 18px;
    grid-template-areas: "av what chev" "av meta meta";
  }

  .csp-16__av {
    grid-area: av;
    align-self: start;
  }

  .csp-16__what {
    grid-area: what;
  }

  .csp-16__ev summary::after {
    grid-area: chev;
  }

  .csp-16__cat {
    grid-area: meta;
    justify-self: start;
  }

  .csp-16__ev time {
    grid-area: meta;
    justify-self: end;
  }

  .csp-16__body {
    padding-left: 16px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .csp-16 * {
    transition: none!important;
    animation: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript by design — <details>, :has() filters and CSS counters do the work. */
```
